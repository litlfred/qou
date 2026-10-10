import os, glob, re, json

def merge_qa_sidecar(target_qa_path, source_qa_data):
    if not os.path.exists(target_qa_path):
        target_data = {"criteria": {}}
    else:
        try:
            with open(target_qa_path) as f:
                target_data = json.load(f)
        except json.JSONDecodeError:
            target_data = {"criteria": {}}
            
    if "criteria" not in target_data:
        target_data["criteria"] = {}
        
    flow_data = source_qa_data.get("criteria", {}).get("milnor-amalgamated-flow")
    if flow_data:
        target_data["criteria"]["milnor-amalgamated-flow"] = flow_data
        with open(target_qa_path, "w") as f:
            json.dump(target_data, f, indent=2)

def run():
    base_dir = "/Users/litlfred/space_cats/qou/folio/quantum-observable-universe"
    done_dir = "/Users/litlfred/space_cats/qou/amalgamated_done"
    
    if not os.path.exists(done_dir):
        print(f"Directory {done_dir} does not exist.")
        return
        
    done_files = glob.glob(f"{done_dir}/*.md")
    total_blocks_written = 0
    
    for df in done_files:
        chapter_name = os.path.basename(df).split('_seq')[0]
        chapter_dir = os.path.join(base_dir, chapter_name)
        
        qa_file = df + ".qa.json"
        qa_data = None
        if os.path.exists(qa_file):
            try:
                with open(qa_file) as qf:
                    qa_data = json.load(qf)
            except json.JSONDecodeError:
                pass
        
        content = open(df).read()
        
        pattern = r'<!-- FILE_START:\s*(.*?\.md)\s*-->\n?(.*?)\n?<!-- FILE_END:\s*\1\s*-->'
        
        for match in re.finditer(pattern, content, re.DOTALL):
            filename = match.group(1)
            block_content = match.group(2)
            
            out_path = os.path.join(chapter_dir, filename)
            if os.path.exists(out_path):
                with open(out_path, "w") as out_f:
                    out_f.write(block_content)
                    if not block_content.endswith("\n"):
                        out_f.write("\n")
                total_blocks_written += 1
                
                if qa_data:
                    block_qa_path = out_path.replace(".md", ".qa.json")
                    merge_qa_sidecar(block_qa_path, qa_data)
            else:
                print(f"Warning: {out_path} does not exist. Skipping.")
                
    print(f"Split and wrote {total_blocks_written} blocks back to {base_dir}, alongside their QA sidecars.")

if __name__ == "__main__":
    run()
