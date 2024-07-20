from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import parse_query, construct_sql, execute_query

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/query', methods=['POST'])
def query():
    try:
        user_query = request.json.get('query')
        app.logger.info(f"Received query: {user_query}")
        parsed_info = parse_query(user_query)
        app.logger.info(f"Parsed query: {parsed_info}")
        sql_query = construct_sql(parsed_info)
        app.logger.info(f"Constructed SQL: {sql_query}")
        result = execute_query(sql_query)
        app.logger.info(f"Query result: {result}")
        return jsonify(result.to_dict(orient='records'))
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
