def index_lessons(lessons):
    for lesson in lessons:
        for chunk in split_into_chunks(lesson):
            chunk.bm25_vec = bm25_vector(chunk.text)
            chunk.dense_vec = embed_model.encode(chunk.text)
            save_to_index(chunk)

def retrieve_and_rank(query, user):
    # 1. Embed query
    q_bm25 = bm25_vector(query)
    q_dense = embed_model.encode(query)
    # 2. Retrieve
    bm25_hits  = bm25_index.search(q_bm25, top_k=100)
    dense_hits  = vector_index.search(q_dense, top_k=100)
    # 3. Fuse
    fused = reciprocal_rank_fusion([bm25_hits, dense_hits], k=60)
    # 4. Feature extraction & pre-ranking
    features = []
    for chunk in fused[:50]:
        f = {
            'sim': cosine(q_dense, chunk.dense_vec),
            'lex': chunk.bm25_score,
            'user': cosine(user.profile_vec, chunk.dense_vec),
            'tone': tone_match(query, chunk.tone_tag)
        }
        features.append((chunk, f))
    # 5. Learning-to-rank
    ranked = ranker.predict_sorted(features)
    # 6. Bandit selection
    final = contextual_bandit.select(ranked, context=query)
    return final[:10]

def update_feedback(user, interactions):
    for chunk_id, reward in interactions:
        # reward = 1 if clicked/liked/bookmarked, else 0
        contextual_bandit.update(user.id, chunk_id, reward, post_contexts)
        user.profile_vec = update_user_embedding(user.profile_vec, chunk_id, reward)
