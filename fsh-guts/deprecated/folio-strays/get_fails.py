import json, sys, os

cmd = os.popen('find . -name "*.qa.json"')
files = cmd.read().strip().split('\n')
for f in files:
    if not f: continue
    with open(f, 'r') as fp:
        try:
            data = json.load(fp)
            evals = data.get('evaluations', {}).get('proof-statement-integrity', [])
            for e in evals:
                if e.get('result') == 'fail':
                    print(f"=== {f} ===")
                    print(e.get('reason'))
        except: pass
