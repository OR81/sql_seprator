import sqlparse

def split_queries(sql_file_path, queries_per_file=20):
    with open(sql_file_path, 'r') as file:
        sql_content = file.read()

    # Use sqlparse to split SQL content into individual queries
    parsed_queries = sqlparse.split(sql_content)

    # Split the queries into chunks of size queries_per_file
    query_chunks = [parsed_queries[i:i + queries_per_file] for i in range(0, len(parsed_queries), queries_per_file)]

    # Save each chunk into a separate file
    for chunk_index, query_chunk in enumerate(query_chunks, start=1):
        with open(f'query_chunk_{chunk_index}.sql', 'w') as output_file:
            output_file.write('\n'.join(query_chunk))

if __name__ == "__main__":
    sql_file_path = "../sql_27_nov.sql"  # Replace with the path to your SQL file
    queries_per_file = 500  # Change this value to the desired number of queries per file
    split_queries(sql_file_path, queries_per_file)

