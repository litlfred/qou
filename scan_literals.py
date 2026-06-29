import os
import re

patterns = [
    r"option_e_.*\.py",
    r"probe_.*\.py",
    r"delta_lambda_.*\.py",
]

literals = {
    "931.494": "U_MEV",
    "0.51099": "M_E_MEV",
    "938.272": "M_P_MEV_VALIDATION",
    "939.565": "M_N_MEV_VALIDATION",
    "2.22452": "AME_B_DEUTERON_MEV_VALIDATION",
    "8.48179": "AME_B_TRITIUM_MEV_VALIDATION",
    "7.71804": "AME_B_HE3_MEV_VALIDATION",
    "28.2956": "AME_B_HE4_MEV_VALIDATION",
    "139.570": "M_PI_PM_MEV_VALIDATION",
}

def scan_files():
    matched_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".venv" in root:
            continue
        for f in files:
            if any(re.match(p, f) for p in patterns):
                matched_files.append(os.path.join(root, f))
    
    print(f"Total exploratory scripts found: {len(matched_files)}")
    
    found_literals = 0
    for path in matched_files:
        with open(path, "r") as f:
            content = f.read()
        
        matches = []
        for lit, var in literals.items():
            if lit in content:
                matches.append(lit)
        if matches:
            print(f"{path}: {matches}")
            found_literals += 1
            
    print(f"Total scripts with literals: {found_literals}")

if __name__ == "__main__":
    scan_files()
