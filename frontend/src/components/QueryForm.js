import React, { useState } from 'react';
import axios from 'axios';
import Results from './Results';

function QueryForm() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/query', { query });
            setResults(response.data);
            setError('');
        } catch (error) {
            console.error('Error fetching data', error);
            setError('Error fetching data: ' + (error.response?.data?.error || error.message));
        }
    };

    return (
        <div className="max-w-xl mx-auto p-4">
            <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
                <textarea
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Enter your query"
                    required
                    className="px-4 py-2 border border-gray-300 rounded-md"
                />
                <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">
                    Submit
                </button>
            </form>
            {error && <div className="text-red-500 mt-4">{error}</div>}
            <Results results={results} />
        </div>
    );
}

export default QueryForm;
