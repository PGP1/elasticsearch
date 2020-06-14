printf "%s\n" "Running TEST 1 - Testing cluster health..."
python3 01_cluster_health.py
printf "%s\n" "Running TEST 2 - Testing data insertion..."
python3 02_insert_data.py
printf "%s\n" "Running TEST 2 - Testing query functionality"
python3 03_query_index.py
printf "%s\n" "Running TEST 2 - Testing delete functionality "
python3 04_delete_data.py