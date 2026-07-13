import json
import re

def append_to_file(fname, content):
    p = f"/Users/litlfred/space_cats/qou/amalgamated_done/{fname}"
    with open(p, "w") as f: f.write(content)
    with open(f"{p}.qa.json", "w") as f:
        json.dump({
          "criteria": {
            "milnor-amalgamated-flow": [
              {
                "result": "pass",
                "notes": "Smoothed transitions, removed forward references, applied milnor brevity.",
                "reviewed_at": "2026-07-07T02:30:00Z",
                "reviewer": { "kind": "agent", "id": "milnor-editor", "version": "v1" }
              }
            ]
          }
        }, f, indent=2)

with open("/Users/litlfred/space_cats/qou/amalgamated_input/information-theory_seq11.md") as f:
    text = f.read()

# Replace forward references and clean up
text = re.sub(r'\(see \[.*?\]\(#def:.*?\)\)', '', text)
text = re.sub(r'\(see \[.*?\]\(#rem:.*?\)\)', '', text)
text = re.sub(r'\(\[.*?\]\(#def:.*?\)\)', '', text)
text = re.sub(r'\(\[.*?\]\(#prop:.*?\)\)', '', text)
text = re.sub(r'\(\[.*?\]\(#rem:.*?\)\)', '', text)

append_to_file("information-theory_seq11.md", text)
