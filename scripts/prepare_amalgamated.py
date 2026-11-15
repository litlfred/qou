import os, glob, re, shutil

def run():
    base_dir = "/Users/litlfred/space_cats/qou/folio/quantum-observable-universe"
    out_dir = "/Users/litlfred/space_cats/qou/amalgamated_input"
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    
    ts_files = glob.glob(f"{base_dir}/*/*.ts")
    
    total_amalgamated = 0
    total_blocks = 0
    for ts_file in ts_files:
        chapter_dir = os.path.dirname(ts_file)
        chapter_name = os.path.basename(chapter_dir)
        
        content = open(ts_file).read()
        content = re.sub(r'//.*', '', content)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        for idx, match in enumerate(re.finditer(r'blocks\s*:\s*\[(.*?)\]', content, re.DOTALL)):
            arr_content = match.group(1)
            blocks = re.findall(r'"([^"]+)"', arr_content)
            
            # Filter valid blocks
            valid_blocks = []
            for b in blocks:
                if 'proof' in b or 'data' in b or 'table' in b:
                    continue
                md_path = os.path.join(chapter_dir, f"{b}.md")
                if os.path.exists(md_path):
                    valid_blocks.append(b)
            
            if len(valid_blocks) > 0:
                # Amalgamate
                out_path = os.path.join(out_dir, f"{chapter_name}_seq{idx}.md")
                with open(out_path, "w") as f:
                    for b in valid_blocks:
                        md_path = os.path.join(chapter_dir, f"{b}.md")
                        b_content = open(md_path).read()
                        f.write(f"<!-- FILE_START: {b}.md -->\n")
                        f.write(b_content)
                        if not b_content.endswith("\n"):
                            f.write("\n")
                        f.write(f"<!-- FILE_END: {b}.md -->\n\n")
                total_amalgamated += 1
                total_blocks += len(valid_blocks)

    print(f"Created {total_amalgamated} amalgamated sections in {out_dir}")
    print(f"Total narrative blocks included: {total_blocks}")

if __name__ == "__main__":
    run()
