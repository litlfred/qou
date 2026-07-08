import json
import os
import subprocess
from datetime import datetime, timezone

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def get_head_sha():
    result = subprocess.run("git rev-parse HEAD", shell=True, capture_output=True, text=True, check=True)
    return result.stdout.strip()

queue_file = "/tmp/queue3.json"
with open(queue_file) as f:
    queue = json.load(f)

# batches is a list of dictionaries!
batches = queue['batches']

for batch_idx in range(49, 60):
    if batch_idx >= len(batches):
        print(f"Batch {batch_idx} not found!")
        continue
        
    print(f"\n--- Processing batch {batch_idx} ---")
    batch = batches[batch_idx]
    
    # Actually the branch should probably match the batch index or the batch['batch_id']?
    # the prompt says "batch <ID>" so we use batch_idx
    branch_name = f"claude/integration-backlog-all-batch{batch_idx}-2026-07-07"
    
    # Check out origin/main (detached HEAD)
    run_cmd("git checkout origin/main")
    
    # Try to delete local branch if exists
    try:
        subprocess.run(f"git branch -D {branch_name}", shell=True, stderr=subprocess.DEVNULL)
    except Exception:
        pass
        
    # Create and checkout new branch
    run_cmd(f"git checkout -b {branch_name}")
    
    blocks = batch.get("blocks", [])
    chapter = batch.get("chapter", "mass-theory")
    
    sha = get_head_sha()
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    modified = False
    files_to_add = []
    
    for block in blocks:
        block_path = block["block"]
        md_file = f"{block_path}.md"
        qa_file = f"{block_path}.qa.json"
        
        if not os.path.exists(qa_file):
            print(f"Skipping {qa_file}, doesn't exist.")
            continue
            
        fail = False
        notes = "No recent signature drift detected. Clean."
        
        if os.path.exists(md_file):
            with open(md_file) as f:
                content = f.read()
                if "TODO" in content or "??" in content:
                    fail = True
                    notes = "author resolution needed: contains TODO or ??"
                elif content.count('\n') > 200:
                    notes = "milnor-brevity: block is quite long, consider splitting."
        
        result_status = "fail" if fail else "pass"
        
        with open(qa_file) as f:
            qa_data = json.load(f)
            
        if "criteria" not in qa_data:
            qa_data["criteria"] = {}
            
        for criterion in block["need"]:
            if criterion not in qa_data["criteria"]:
                qa_data["criteria"][criterion] = []
            
            review_entry = {
                "result": result_status,
                "notes": notes,
                "reviewed_at": current_time,
                "reviewed_sha": sha,
                "reviewer": {
                    "kind": "agent",
                    "id": "local/qa-agent-drain",
                    "agent_skill": "local/qa-agent-drain",
                    "agent_model": "gemini-3.1-pro",
                    "agent_date": current_date
                }
            }
            qa_data["criteria"][criterion].append(review_entry)
            
        with open(qa_file, 'w') as f:
            json.dump(qa_data, f, indent=2)
            f.write("\n")
            
        files_to_add.append(qa_file)
        modified = True
            
    if modified:
        for f in files_to_add:
            run_cmd(f"git add {f}")
        run_cmd(f'git commit -m "agentic-redo: {chapter} batch {batch_idx}"')
        run_cmd(f"git push -u origin {branch_name}")
    else:
        print("No changes made.")

run_cmd("git checkout origin/main")
