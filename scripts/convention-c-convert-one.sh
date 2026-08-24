#!/usr/bin/env bash
# Measure ONE convention-C site: baseline -> convert -> diff. Does NOT commit.
#
# The per-site read is the point (see #5565: the automated sweep was 0-for-2),
# so this automates only the MEASUREMENT, never the judgement. It prints the
# baseline movement, the convention-only witness diff, and a WHOLE-FILE stdout
# diff -- whole-file because diffing tails misaligned once when a provenance
# line shifted the window and nearly produced a false finding.
#
#   scripts/convention-c-convert-one.sh <producer.py> <witness.json> '<old z line>' '<new z expr>'
set -uo pipefail
P="$1"; W="$2"; OLD="$3"; NEW="$4"
T=$(mktemp -d)

git checkout -- "$W" "$P" 2>/dev/null
cp "$W" "$T/committed.json"
timeout 900 python3 -u "$P" > "$T/base.log" 2>&1; echo "baseline exit=$?"
python3 - "$W" "$T/committed.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[2])); b=json.load(open(sys.argv[1]))
def flat(o,p=''):
    r={}
    if isinstance(o,dict):
        for k,v in o.items(): r.update(flat(v,p+'/'+k))
    elif isinstance(o,list):
        for i,v in enumerate(o): r.update(flat(v,f'{p}[{i}]'))
    else: r[p]=o
    return r
S=('computedAt','durationMs','commitSha','invocation','environment','scriptCommitSha','scriptHash','generated','timestamp','upstream_witness_hashes')
fa,fb=flat(a),flat(b)
m=[k for k in sorted(set(fa)|set(fb)) if fa.get(k)!=fb.get(k) and not any(s in k for s in S)]
print(f"BASELINE moved: {len(m)}")
for k in m[:4]: print(f"   {k}: {str(fa.get(k))[:34]} -> {str(fb.get(k))[:34]}")
PY

cp "$W" "$T/base.json"
python3 - "$P" "$OLD" "$NEW" <<'PY'
import sys
p,old,new=sys.argv[1],sys.argv[2],sys.argv[3]
s=open(p).read()
if old not in s:
    print("!! ANCHOR NOT FOUND -- no change made"); sys.exit(2)
open(p,'w').write(s.replace(old,new,1)); print("converted")
PY
[ $? -ne 0 ] && { echo "aborting"; exit 2; }

timeout 900 python3 -u "$P" > "$T/conv.log" 2>&1; echo "converted exit=$?"
python3 - "$W" "$T/base.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[2])); b=json.load(open(sys.argv[1]))
def flat(o,p=''):
    r={}
    if isinstance(o,dict):
        for k,v in o.items(): r.update(flat(v,p+'/'+k))
    elif isinstance(o,list):
        for i,v in enumerate(o): r.update(flat(v,f'{p}[{i}]'))
    else: r[p]=o
    return r
S=('computedAt','durationMs','commitSha','invocation','environment','scriptCommitSha','scriptHash','generated','timestamp','upstream_witness_hashes')
fa,fb=flat(a),flat(b)
m=[k for k in sorted(set(fa)|set(fb)) if fa.get(k)!=fb.get(k) and not any(s in k for s in S)]
print(f"CONVENTION-ONLY diff: {len(m)} fields")
for k in m[:8]: print(f"   {k}\n      C: {str(fa.get(k))[:36]}\n      D: {str(fb.get(k))[:36]}")
PY
echo "--- stdout diff (WHOLE file, provenance lines dropped) ---"
diff <(grep -v "environment:" "$T/base.log") <(grep -v "environment:" "$T/conv.log") && echo "  IDENTICAL"
