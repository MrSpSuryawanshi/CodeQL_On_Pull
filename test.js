// This JavaScript file intentionally contains security issues for demonstration purposes.

// Example of a potential Cross-Site Scripting (XSS) vulnerability
function displayMessage(message) {
  document.getElementById('output').innerHTML = message;
}

// Example of a potential SQL Injection vulnerability
function fetchUserData(userId) {
  const sqlQuery = `SELECT * FROM users WHERE id = ${userId}`;
  // Execute the SQL query (for demonstration purposes only, not in a real application)
  // ...

  return result;
}

// Example of a potential code injection vulnerability
function executeUserInput(input) {
  eval(input);
}

// Example of an insecure regular expression
const regex = new RegExp(userInput); // userInput is not sanitized

// Example of a potential insecure use of local storage
localStorage.setItem('secret', 'my-secret-data');
localStorage.getItem('secret'); // Insecure for sensitive data

// Hardcoded API keys or credentials
const apiKey = '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';

// Writing sensitive data to console
console.log('This is a sensitive message: ' + sensitiveData);
