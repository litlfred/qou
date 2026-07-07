import os, glob

def run():
    input_dir = "/Users/litlfred/space_cats/qou/amalgamated_input"
    files = sorted(glob.glob(f"{input_dir}/*.md"))
    
    batch_size = 20
    batch_idx = 0
    for i in range(0, len(files), batch_size):
        batch = files[i:i+batch_size]
        batch_char = chr(97 + batch_idx) if batch_idx < 26 else f"a{chr(97 + batch_idx - 26)}"
        batch_file = f"/Users/litlfred/space_cats/qou/amalgamated_batch_{batch_char}"
        with open(batch_file, "w") as f:
            for bf in batch:
                f.write(os.path.basename(bf) + "\n")
        batch_idx += 1
    print(f"Created {batch_idx} batches.")

if __name__ == "__main__":
    run()
