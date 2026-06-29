import os
import re

patterns = [
    r"option_e_.*\.py",
    r"probe_.*\.py",
    r"delta_lambda_.*\.py",
]

literal_map = {
    r"931\.494\d*": "U_MEV",
    r"0\.51099895\d*": "M_E_MEV",
    r"938\.272\d*": "M_P_MEV_VALIDATION",
    r"939\.565\d*": "M_N_MEV_VALIDATION",
    r"2\.22452": "AME_B_DEUTERON_MEV_VALIDATION",
    r"8\.48179\d*": "AME_B_TRITIUM_MEV_VALIDATION",
    r"7\.7180[46]": "AME_B_HE3_MEV_VALIDATION",
    r"28\.2956\d*": "AME_B_HE4_MEV_VALIDATION",
    r"139\.57039": "M_PI_PM_MEV_VALIDATION",
}

def process_files():
    matched_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".venv" in root:
            continue
        for f in files:
            if any(re.match(p, f) for p in patterns):
                matched_files.append(os.path.join(root, f))
    
    for path in matched_files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            continue
            
        used_vars = set()
        new_content = content
        
        for lit_re, var_name in literal_map.items():
            # Match mpf("123") or mp.mpf('123') or float("123")
            pattern1 = r"(?:mp\.mpf|mpf|float)\([\"']" + lit_re + r"[\"']\)"
            # Match just "123" or '123'
            pattern2 = r"[\"']" + lit_re + r"[\"']"
            # Match bare literal 123.456
            pattern3 = r"\b" + lit_re + r"\b"
            
            def repl(m):
                used_vars.add(var_name)
                return var_name
                
            new_content, c1 = re.subn(pattern1, repl, new_content)
            new_content, c2 = re.subn(pattern2, repl, new_content)
            new_content, c3 = re.subn(pattern3, repl, new_content)
            
        if used_vars:
            print(f"Updating {path} with {used_vars}")
            
            # Need to figure out the import path.
            # Usually files are in computations/ or computations/probes/ or docs/audits/scripts/
            # We will try to add `import sys; sys.path.insert(0, ...)` if we can't just use absolute path.
            # But wait, QOU scripts usually just run. Let's add:
            # `from computations.substrate.codata_constants import ...`
            # and let python resolve it from the root directory.
            
            import_stmt = f"from computations.substrate.codata_constants import {', '.join(sorted(list(used_vars)))}"
            
            # Insert after the docstring or at the top
            if new_content.startswith('"""'):
                end_doc = new_content.find('"""', 3)
                if end_doc != -1:
                    new_content = new_content[:end_doc+3] + "\n" + import_stmt + "\n" + new_content[end_doc+3:]
                else:
                    new_content = import_stmt + "\n" + new_content
            elif new_content.startswith('#!'):
                newline_pos = new_content.find('\n')
                new_content = new_content[:newline_pos+1] + import_stmt + "\n" + new_content[newline_pos+1:]
            else:
                new_content = import_stmt + "\n" + new_content
                
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

if __name__ == "__main__":
    process_files()
