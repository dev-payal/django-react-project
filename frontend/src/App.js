import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [country, setCountry] = useState({});
  const [guess, setGuess] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchRandomCountry(); // Fetch a random country on page load
  }, []);

  const fetchRandomCountry = async () => {
    try {
      const response = await axios.get('country/');
      setCountry(response.data);
    } catch (error) {
      console.error('Error fetching random country:', error);
    }
  };

  const checkGuess = () => {
    if (guess.length === 0) {
      setMessage('Please enter a valid guess')
    }
    else if (guess.toLowerCase() === country.capital.toLowerCase()) {
      setMessage('Correct!');
    } else {
      setMessage(`Incorrect Answer. The correct answer is ${country.capital}.`);
    }
    setGuess('');
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h1 className="text-center">Guess the Capital</h1>
          <div className="text-center">
            <p>Country: {country.name}</p>
            <input
              type="text"
              className="form-control"
              placeholder="Enter your guess"
              value={guess}
              onChange={(e) => setGuess(e.target.value)}
            />
            <button
              className="btn btn-primary btn-block mt-2"
              onClick={checkGuess}
            >
              Check
            </button>
            <p className="mt-3">{message}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
