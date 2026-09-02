#!/usr/bin/env python3
"""Census muon-pinned witnesses — and make the PREFIX you matched on explicit.

Why this exists as a script rather than a remembered number: "carries the muon
fingerprint" is ambiguous in this corpus. `muon_pin_three_values_probe.py`
establishes that THREE different values are all called "the muon q0" — the
frozen canonical pin 1.1099785955573347..., and the lepton-tower derivation at
CODATA 2018 (...55541805...) and 2022 (...56427390...) — diverging at the 13th
significant digit. So the prefix length silently selects which of the three you
are counting, and two agents measuring "the muon witnesses" can differ by 3x
while both being right.

Measured with this script, same method at every end:

    match on                    counts            2026-08-16  2026-08-26  2026-08-30
    1.109978595   (10 digits)   all three values      871         477         404
    1.1099785955573347 (full)   the pin A only        468         149          40

NOTE the 2026-08-30 column is AFTER the anchor moved (fca08de7d29, 2026-08-28:
A retired, C canonical). From that revision on, the ladder measures the wrong
thing -- see the --by-value output, which discriminates A vs B vs C instead. The
ladder is kept because prose in the corpus quotes its numbers and they must stay
reproducible, not because it is the right question now.

AGENTS.md's recorded 870 is the ten-digit reading and is correct. An agent
matching only the then-canonical literal gets 149 and concludes the figure is
stale by ~6x. That happened on 2026-08-26 and was one edit away from replacing a
correct number with one answering a different question.

The same trap has a second mouth now that the anchor has moved: matching the
literal that USED to be canonical measures what is left to migrate, and matching
the one that IS canonical measures what is already done. Neither is "the muon
witnesses". Say which you ran.

Reads git, not the working tree, so it can measure any revision:

    python3 computations/audits/muon_pin_witness_census.py            # HEAD
    python3 computations/audits/muon_pin_witness_census.py <rev>
    python3 computations/audits/muon_pin_witness_census.py <rev> --list  # name them

Emits no witness — it is a measurement tool, and its output belongs in whatever
prose quotes a count, next to the prefix that produced it.
"""
import subprocess, sys
rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
files = [f for f in subprocess.run(["git","ls-tree","-r","--name-only",rev],
         capture_output=True,text=True).stdout.splitlines()
         if f.startswith("computations/") and f.endswith(".witness.json")]
prefixes = ["1.1099785","1.10997859","1.109978595","1.1099785955","1.1099785955573347"]

# The ladder above answers "how many carry SOME muon-ish value". After the
# 2026-08-28 anchor move (fca08de7d29) that is no longer the operative question:
# A is retired, C is canonical, and B was never canonical here. The ladder cannot
# tell them apart -- every one of its rungs is a prefix of at least two of the
# three, so `1.1099785955` counts B and a truncated A together and NOTHING in it
# matches C at all. These three discriminate, and they are the migration scope.
VALUES = {
    "A  retired frozen pin      ": "1.1099785955573347",
    "B  CODATA 2018 derivation  ": "1.10997859555418",
    "C  CODATA 2022 (CANONICAL) ": "1.10997859564273",
}

counts = {p:0 for p in prefixes}
vcounts = {k:0 for k in VALUES}
vfiles = {k:[] for k in VALUES}
multi = []
for f in files:
    t = subprocess.run(["git","show",f"{rev}:{f}"],capture_output=True).stdout.decode("utf-8","replace")
    for p in prefixes:
        if p in t: counts[p]+=1
    hit = [k for k,v in VALUES.items() if v in t]
    for k in hit:
        vcounts[k]+=1; vfiles[k].append(f)
    if len(hit) > 1:
        multi.append((f, [k.split()[0] for k in hit]))

print(f"  rev {rev[:12]}  tracked {len(files)}")
print("\n  PREFIX LADDER (how many carry some muon-ish value; rungs OVERLAP)")
for p in prefixes:
    note = "  <-- AMBIGUOUS: also matches proton" if p in ("1.1099785","1.10997859") else ""
    print(f"    {p:<22} {counts[p]}{note}")

print("\n  BY VALUE (discriminating -- this is the migration scope)")
for k,v in VALUES.items():
    print(f"    {k} {v:<20} {vcounts[k]}")
print(f"\n    carrying MORE THAN ONE of A/B/C: {len(multi)}"
      "   (a deliberate comparison, or a straddle -- triage, do not bulk-migrate)")
for f,h in multi[:15]:
    print(f"      {'+'.join(h):<6} {f}")
if len(multi) > 15:
    print(f"      ... and {len(multi)-15} more")

if "--list" in sys.argv:
    for k in VALUES:
        print(f"\n  == {k.strip()} ({vcounts[k]})")
        for f in vfiles[k]:
            print(f"     {f}")
