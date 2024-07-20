import React from 'react';

function Results({ results }) {
    if (results.length === 0) {
        return <div className="mt-4">No results found.</div>;
    }

    return (
        <div className="mt-4">
            <h2 className="text-lg font-semibold mb-2">Results</h2>
            <ul className="space-y-2">
                {results.map((result, index) => (
                    <li key={index} className="p-4 border border-gray-300 rounded-md">
                        {Object.keys(result).map((key) => (
                            <div key={key}>
                                <strong>{key}:</strong> {result[key]}
                            </div>
                        ))}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Results;
