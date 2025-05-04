// Example function to simulate fetching Islamic perspectives based on topic
export function fetchIslamicContent(topic) {
    const content = {
      prayer: "In Islam, prayer (Salah) is one of the five pillars and is a direct way of connecting with Allah.",
      justice: "Justice in Islam is a fundamental principle that guides Muslims in their personal and societal lives.",
      charity: "Charity (Zakat) is a means of helping the poor and purifying wealth in Islam.",
      fasting: "Fasting during the month of Ramadan is a way to gain spiritual benefits and empathy for the needy.",
      love: "Love in Islam is viewed as a force that connects people and leads them to live with kindness and compassion."
    };
  
    // If topic is found, return the respective perspective
    if (content[topic.toLowerCase()]) {
      return content[topic.toLowerCase()];
    } else {
      return "Sorry, no content available for this topic. Try another one.";
    }
  }
  