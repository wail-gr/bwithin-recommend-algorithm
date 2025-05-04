import React, { useState } from 'react';
import { fetchIslamicContent } from './IslamicViewAPI';
import './IslamicView.css';

export default function IslamicView() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSearch = (topic) => {
    if (topic) {
      const response = fetchIslamicContent(topic);
      setAnswer(response);
    }
  };

  return (
    <div className="islamic-view-container">
      <h1>Understand Islamic Views</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSearch(query)}
        placeholder="Enter a topic (e.g. justice, prayer, etc.)"
        className="search-input"
      />
      <button onClick={() => handleSearch(query)} className="search-button">
        Search
      </button>

      <div className="answer-container">
        {answer ? (
          <p>{answer}</p>
        ) : (
          <p>Enter a topic to get the Islamic perspective.</p>
        )}
      </div>
    </div>
  );
}
