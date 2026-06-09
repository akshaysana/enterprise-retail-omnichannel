import numpy as np

# Rows = 4 Retail Locations (0: Store Alpha, 1: Store Beta, 2: Store Gamma, 3: Store Delta)
# Columns = 4 Operational Metrics (0: Revenue, 1: Footfall, 2: Online Orders, 3: Returns)
store_performance_matrix = np.array([
    [45.0,  12000.0,  850.0,   120.0],  # Store Alpha
    [32.0,  np.nan,   420.0,   95.0],   # Store Beta
    [58.0,  18500.0,  np.nan,  210.0],  # Store Gamma
    [29.0,  9800.0,   310.0,   80.0]    # Store Delta
])

print("•••• MASTER RETAIL AUDIT ••••\n")

print("=== NAN FILTER ===\n")

nan_filter = np.isnan(store_performance_matrix)
store_performance_matrix[nan_filter] = 0.0
print(store_performance_matrix,"\n")

print("=== CORE STORE & OPERATION PERFORMANCE ===\n")

core_engine_window = store_performance_matrix[1:3, 1:3]
print("Performance for Store Beta (Footfall & Online Orders): ", core_engine_window[0])
print("Performance for Store Gamma (Footfall & Online Orders): ", core_engine_window[1], "\n")

print("=== TOTAL REVENUE FOR ALL THE STORE'S ===\n")

sum_store_performance = np.sum(store_performance_matrix, axis=1)
print("Total sum of revenue of store 'Alpha': ", sum_store_performance[0])
print("Total sum of revenue of store 'Beta': ", sum_store_performance[1])
print("Total sum of revenue of store 'Gamma': ", sum_store_performance[2])
print("Total sum of revenue of store 'Delta': ", sum_store_performance[3], "\n")

print("=== MAX OPERATION PERFORMANCE ===\n")

peak_performance = np.max(store_performance_matrix, axis=0)
print("Max performance of 'Revenue' operation: ", peak_performance[0])
print("Max performance of 'Footfall' operation: ", peak_performance[1])
print("Max performance of 'Online Orders' operation: ", peak_performance[2])
print("Max performance of 'Returns' operation: ", peak_performance[3], "\n")