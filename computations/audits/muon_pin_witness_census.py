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

Measured 2026-08-26, same script both ends:

    match on                    counts               2026-08-16   2026-08-26
    1.109978595   (10 digits)   all three values        871          477
    1.1099785955573347 (full)   canonical pin only      468          149

AGENTS.md's recorded 870 is the ten-digit reading and is correct. An agent
matching only the canonical literal gets 149 and concludes the figure is stale
by ~6x. That happened on 2026-08-26 and was one edit away from replacing a
correct number with one answering a different question.

Reads git, not the working tree, so it can measure any revision:

    python3 computations/audits/muon_pin_witness_census.py            # HEAD
    python3 computations/audits/muon_pin_witness_census.py <rev>

Emits no witness — it is a measurement tool, and its output belongs in whatever
prose quotes a count, next to the prefix that produced it.
"""
import subprocess, sys
rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
files = [f for f in subprocess.run(["git","ls-tree","-r","--name-only",rev],
         capture_output=True,text=True).stdout.splitlines()
         if f.startswith("computations/") and f.endswith(".witness.json")]
prefixes = ["1.1099785","1.10997859","1.109978595","1.1099785955","1.1099785955573347"]
counts = {p:0 for p in prefixes}
for f in files:
    t = subprocess.run(["git","show",f"{rev}:{f}"],capture_output=True).stdout.decode("utf-8","replace")
    for p in prefixes:
        if p in t: counts[p]+=1
print(f"  rev {rev[:12]}  tracked {len(files)}")
for p in prefixes:
    note = "  <-- AMBIGUOUS: also matches proton" if p in ("1.1099785","1.10997859") else ""
    print(f"    {p:<22} {counts[p]}{note}")
