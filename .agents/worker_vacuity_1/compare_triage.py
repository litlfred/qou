import json

with open('/Users/litlfred/space_cats/qou/docs/audits/2026-06-17-lean-vacuity-axiom-audit.json', 'r') as f:
    new_audit = json.load(f)

with open('/Users/litlfred/space_cats/qou/docs/audits/2026-06-18-self-assuming-projection-triage.json', 'r') as f:
    old_triage = json.load(f)

# Collect self-assuming projection findings from new audit
new_flagged = []
for filepath, defects in new_audit.get('flagged', {}).items():
    for defect in defects:
        if defect.get('category') == 'proof-no-self-assuming-projection':
            new_flagged.append({
                'file': filepath,
                'line': defect.get('line'),
                'decl': defect.get('decl'),
                'exempt': defect.get('exempt', False)
            })

# Collect from old triage
old_flagged = []
for cand in old_triage.get('candidates', []):
    old_flagged.append({
        'file': cand.get('file'),
        'line': cand.get('line'),
        'decl': cand.get('decl'),
        'verdict': cand.get('verdict')
    })
for cand in old_triage.get('legitimate', []):
    old_flagged.append({
        'file': cand.get('file'),
        'line': cand.get('line'),
        'decl': cand.get('decl'),
        'verdict': cand.get('verdict')
    })

print(f"New self-assuming-projection count: {len(new_flagged)}")
print(f"Old triage candidates count: {len(old_flagged)}")

# Check for differences
new_set = {(f['file'], f['line'], f['decl']) for f in new_flagged}
old_set = {(f['file'], f['line'], f['decl']) for f in old_flagged}

new_only = new_set - old_set
old_only = old_set - new_set

print(f"Items in new audit but not in old triage: {len(new_only)}")
for item in new_only:
    print(f"  New: {item}")

print(f"Items in old triage but not in new audit: {len(old_only)}")
for item in old_only:
    print(f"  Old: {item}")
