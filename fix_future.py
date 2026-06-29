import os

def fix_future_imports():
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".venv" in root:
            continue
        for f in files:
            if not f.endswith(".py"):
                continue
                
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8") as f_in:
                    lines = f_in.readlines()
            except UnicodeDecodeError:
                continue
                
            has_future = any(line.strip().startswith("from __future__") for line in lines)
            injected_idx = -1
            for i, line in enumerate(lines):
                if line.startswith("from computations.substrate.codata_constants import"):
                    injected_idx = i
                    break
                    
            if has_future and injected_idx != -1:
                # Find last future index
                last_future = -1
                for i, line in enumerate(lines):
                    if line.strip().startswith("from __future__"):
                        last_future = i
                        
                if injected_idx < last_future:
                    print(f"Fixing {path}")
                    # Remove the injected line
                    injected_line = lines.pop(injected_idx)
                    # The last_future index has shifted if injected_idx < last_future
                    new_idx = last_future
                    lines.insert(new_idx, injected_line)
                    
                    with open(path, "w", encoding="utf-8") as f_out:
                        f_out.writelines(lines)

if __name__ == "__main__":
    fix_future_imports()
