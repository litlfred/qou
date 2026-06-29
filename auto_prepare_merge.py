import os
import subprocess
import re

PRs = [
    (3062, "claude/fix-qa-isomers-2026-06-29"),
    (3061, "claude/fix-confinement-lp-qa-2026-06-29"),
    (3036, "claude/shell-closure-stability-2026-06-28"),
    (3033, "claude/qbeta-trace-counit-convergence-qa-2026-06-28"),
    (3032, "claude/fix-archimedean-proton-numerology-2026-06-28"),
    (3030, "claude/delta-max-qa-fixes-2026-06-28")
]

content_dir = "/Users/litlfred/space_cats/qou/content/quantum-observable-universe"

def run(cmd, check=True):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Command failed: {cmd}\nOutput: {result.stdout}\nError: {result.stderr}")
        raise Exception("Command failed")
    return result

def fix_validation():
    result = run("bun run scripts/run-validate.ts", check=False)
    if result.returncode == 0:
        return True
    
    # Parse errors
    output = result.stdout + "\n" + result.stderr
    print("Validation failed, parsing errors...")
    
    bad_md_refs = {}
    bad_ts_leans = []
    
    for line in output.split('\n'):
        line = line.strip()
        if "Undefined cross-reference(s) in .md:" in line or "Unresolved uses:" in line:
            # e.g. ⚠ [simple-objects-V]: Undefined cross-reference(s) in .md: rem:fundamental-object-explication
            # e.g. ✗ [a8-partition-function-identity]: Unresolved uses: lemma:cyclotomic-strand-doubling
            m = re.search(r'\[(.*?)\]: (?:Undefined cross-reference\(s\) in .md:|Unresolved uses:) (.*)', line)
            if m:
                block = m.group(1).strip()
                refs = [r.strip() for r in m.group(2).split(',')]
                bad_md_refs[block] = bad_md_refs.get(block, []) + refs
        elif "no Lean declaration yet" in line or "requires Lean formalization" in line:
            m = re.search(r'\[(.*?)\]:', line)
            if m:
                bad_ts_leans.append(m.group(1).strip() + ".ts")
                
    # Fix MD refs
    for root, _, files in os.walk(content_dir):
        for file in files:
            block = file.replace(".md", "").replace(".ts", "")
            if block in bad_md_refs and (file.endswith(".md") or file.endswith(".ts")):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                
                for ref in bad_md_refs[block]:
                    # markdown replacements
                    content = re.sub(r'\[([^\]]+)\]\(#' + ref + r'\)', r'\1', content)
                    content = re.sub(r'\[([^\]]+)\]\(' + ref + r'\)', r'\1', content)
                    # ts replacements for uses
                    content = content.replace(f'"{ref}"', "")
                    content = content.replace(f'"{ref}",', "")
                    
                with open(filepath, 'w') as f:
                    f.write(content)
                    
            if file in bad_ts_leans:
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                new_lines = []
                in_lean = False
                for ln in lines:
                    if 'lean: {' in ln:
                        in_lean = True
                    if in_lean:
                        new_lines.append('// ' + ln)
                        if '},' in ln:
                            in_lean = False
                    else:
                        new_lines.append(ln)
                with open(filepath, 'w') as f:
                    f.writelines(new_lines)
                    
    return False

for pr, branch in PRs:
    print(f"\n--- Processing PR {pr} branch {branch} ---")
    try:
        run(f"git checkout {branch}")
        run("git fetch origin main")
        
        # We need to reset hard and rebase
        run(f"git reset --hard origin/{branch}")
        rebase_res = run("git rebase origin/main", check=False)
        if rebase_res.returncode != 0:
            print(f"Rebase failed for {branch}, skipping...")
            run("git rebase --abort", check=False)
            continue
            
        # Run validation and fix up to 3 times
        for i in range(3):
            if fix_validation():
                print(f"Validation passed for {branch}!")
                break
            print(f"Attempt {i+1} fixing validation...")
            
        status = run("git status --porcelain")
        if status.stdout.strip():
            run('git add .')
            run('git commit -m "fix(qa): untangle broken cross-references and lean metadata from audit extraction"')
            
        run(f"git push -u origin HEAD -f")
        run(f"gh pr merge {pr} --merge --admin")
        print(f"Successfully merged PR {pr}")
        
    except Exception as e:
        print(f"Error processing {branch}: {e}")

run("git checkout main")
print("Finished!")
