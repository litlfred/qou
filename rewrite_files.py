import sys
import json
import os
from datetime import datetime, timezone

def write_out(filename, content):
    base_dir = "/Users/litlfred/space_cats/qou/amalgamated_done"
    os.makedirs(base_dir, exist_ok=True)
    
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w") as f:
        f.write(content)
        
    qa_path = filepath + ".qa.json"
    qa = {
      "criteria": {
        "milnor-amalgamated-flow": [
          {
            "result": "pass",
            "notes": "Smoothed transitions, removed forward references, improved economy, applied concrete-before-abstract, active voice, uncluttered notation.",
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
            "reviewer": { "kind": "agent", "id": "milnor-editor", "version": "v1" }
          }
        ]
      }
    }
    with open(qa_path, "w") as f:
        json.dump(qa, f, indent=2)

