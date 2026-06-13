import json

with open('folio-assistant/computations/chi-lambda-he4-full-partition-table.witness.json') as f:
    chi_data = json.load(f)['data']['per_partition_chi_lambda']

with open('folio-assistant/computations/wenzl-y-lambda-h12.witness.json') as f:
    y_data = json.load(f)['data']['per_partition']

chi_dict = {str(item['partition']): item['chi_lambda_he4'] for item in chi_data}
y_dict = {str(item['partition']): float(item['y_lambda']) for item in y_data}

total_tr = 0.0
tr_93_84_102 = 0.0
tr_2row = 0.0

for part_str, chi in chi_dict.items():
    if part_str in y_dict:
        y = y_dict[part_str]
        val = y * chi
        total_tr += val
        
        # Check if 2-row
        part = json.loads(part_str)
        if len(part) <= 2:
            tr_2row += val
            if part in [[9,3], [8,4], [10,2]]:
                tr_93_84_102 += val

print(f"Total tr_M(beta_He4) = {total_tr}")
print(f"Sum over 2-row = {tr_2row}")
print(f"Sum over (9,3), (8,4), (10,2) = {tr_93_84_102}")

m_e = 0.510998950
print(f"Implied binding (total) = {total_tr * m_e}")
print(f"Implied binding (2-row) = {tr_2row * m_e}")

