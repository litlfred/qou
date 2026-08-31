"""Resolve a vacuous-green-baseline merge conflict STRUCTURALLY.

Semantics: base holds set B; ours removed Ra; theirs removed Rt. The correct
merge is B - (Ra u Rt) = ours n theirs. Computed on parsed JSON, so a
malformed result is impossible -- unlike regex hunk surgery, which silently
leaves a trailing comma when a deleted hunk held the array's last element.

REFUSES if either side ADDED an entry: the baseline is shrink-only by design,
and an addition is a real defect that must not be auto-resolved away.
"""
import json, subprocess, sys
P = "computations/audits/vacuous-green-baseline.json"
def stage(n):
    return json.loads(subprocess.run(["git","show",f":{n}:{P}"],
                                     capture_output=True, text=True, check=True).stdout)
base, ours, theirs = stage(1), stage(2), stage(3)
b, o, t = set(base["live"]), set(ours["live"]), set(theirs["live"])
for name, s in (("ours", o), ("theirs", t)):
    added = s - b
    if added:
        sys.exit(f"REFUSING: {name} ADDED {len(added)} entry(ies) to a shrink-only "
                 f"baseline: {sorted(added)[:3]}")
keep = o & t
merged = dict(ours)
merged["live"] = [x for x in base["live"] if x in keep]   # base order preserved
json.dump(merged, open(P, "w"), indent=2)
open(P, "a").write("\n")
print(f"  base {len(b)} -> ours {len(o)} (-{len(b-o)}), theirs {len(t)} (-{len(b-t)}) "
      f"=> merged {len(merged['live'])} (-{len(b)-len(merged['live'])})")

# ---------------------------------------------------------------------------
# WHY THIS EXISTS (qou-srvu, 2026-08-30)
#
# Five drain branches (slices A-E) each removed a disjoint set of entries from
# `computations/audits/vacuous-green-baseline.json`. Each merges CLEANLY into
# main on its own; from the second onward they conflict with each other,
# because git's 3-way merge cannot tell that two deletions of ADJACENT lines
# are both correct.
#
# The conflict is mechanical and the resolution is NOT a side-pick:
#   - "take ours"   silently discards the other slice's drains
#   - "take theirs" silently discards this slice's drains
#   - the correct answer is the UNION of deletions = ours n theirs
#
# Do not resolve these by hand or by regex. A first attempt here edited the
# conflict hunks textually and produced INVALID JSON -- a hunk happened to
# contain the array's last element, so the survivor kept its trailing comma.
# Parsing both sides and intersecting cannot fail that way.
#
# Verified end to end: merging A,B,C,D,E into main in that order with this
# resolver yields baseline 423 -> 364, exactly 8+9+12+11+19 = 59 removed with
# zero double-counting, and the merged tree's own ratchet agrees.
#
# USAGE (mid-merge, with the conflict staged):
#     python3 scripts/resolve-vacuous-green-baseline-merge.py
#     git add computations/audits/vacuous-green-baseline.json
#     git merge --continue
#
# ALWAYS re-run the ratchet on the merged tree afterwards -- the resolver
# makes the baseline consistent, it does not verify the tree against it:
#     python3 computations/audits/vacuous_green_witness_audit.py
