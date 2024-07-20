import React from 'react';
import QueryForm from './components/QueryForm';

function App() {
    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
            <div className="max-w-2xl w-full bg-white shadow-md rounded-lg p-6">
                <h1 className="text-2xl font-bold mb-4 text-center">ByteGenie Event Query App</h1>
                <QueryForm />
            </div>
        </div>
    );
}

export default App;
