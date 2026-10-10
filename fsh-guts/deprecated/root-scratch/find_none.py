import os, json

qou_dir = "."
content_dir = os.path.join(qou_dir, "content")

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".ts"):
            ts_path = os.path.join(root, file)
            # read block type
            try:
                with open(ts_path, 'r') as f:
                    content = f.read()
                    if 'type: "theorem"' in content or 'type: "lemma"' in content or 'type: "proposition"' in content or 'type: "corollary"' in content:
                        block_name = file[:-3]
                        # check if lean file exists
                        # check in content dir and also recursively?
                        # actually we can just check if any lean file has this block name in qou
                        lean_file = None
                        for r2, d2, f2 in os.walk(content_dir):
                            for fl in f2:
                                if fl.endswith(".lean") and (fl == f"{block_name}.lean" or fl == f"{block_name.replace('-', '_')}.lean"):
                                    lean_file = fl
                                    break
                        if lean_file is None:
                            print(f"Missing: {ts_path}")
            except:
                pass
