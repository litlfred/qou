import sys
import json
import subprocess

def resolve():
    files = subprocess.check_output(['git', 'diff', '--name-only', '--diff-filter=U']).decode().splitlines()
    if not files:
        return False
    for f in files:
        if not f.endswith('.json'):
            print(f"Skipping non-json conflict: {f}")
            continue
            
        try:
            subprocess.check_call(['git', 'checkout', '--theirs', f])
            with open(f) as fp:
                our_data = json.load(fp)
                
            subprocess.check_call(['git', 'checkout', '--ours', f])
            with open(f) as fp:
                main_data = json.load(fp)
                
            for k, v in our_data.get('criteria', {}).items():
                if k not in main_data.setdefault('criteria', {}):
                    main_data['criteria'][k] = v
                else:
                    # just blindly extend because we assume they are different reviews
                    # or only add if not present by some hash
                    for review in (v if isinstance(v, list) else [v]):
                        # simple deduplication by reviewer id + date
                        existing = [r.get('reviewer', {}).get('id') for r in main_data['criteria'][k]]
                        if review.get('reviewer', {}).get('id') not in existing:
                            main_data['criteria'][k].append(review)
                            
            main_data['updated_at'] = max(main_data.get('updated_at', ''), our_data.get('updated_at', ''))
            
            with open(f, 'w') as fp:
                json.dump(main_data, fp, indent=2, ensure_ascii=False)
                fp.write('\n')
            subprocess.check_call(['git', 'add', f])
            print(f"Resolved {f}")
        except Exception as e:
            print(f"Error resolving {f}: {e}")
            return False
    return True

if __name__ == "__main__":
    resolve()
