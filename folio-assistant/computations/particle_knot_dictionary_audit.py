#!/usr/bin/env python3
"""Audit: find all particle-knot identifications in the paper, cross-check
against canonical sources of truth (confined-particle.md +
knot-particle-dictionary.md), flag inconsistencies.

Sources of truth:
  - confined-particle.md: GB-NF / Hecke-element registry
      quark    = [σ_0]
      proton   = [B_3(uud)]   3-strand Borromean
      neutron  = [B_3(udd)]   3-strand Borromean
      electron = [σ_1^3]      = trefoil 3_1 in B_2

  - knot-particle-dictionary.md: knot-type / closed-braid table
      neutrino  = unknot T_{1,0} = 0_1
      electron  = trefoil T_{2,3} = 3_1
      muon      = cinquefoil T_{2,5} = 5_1
      tau       = septafoil T_{2,7} = 7_1
      quarks    = unknots in B_3 (crossing-oriented)
      photon    = empty point (?)
      Higgs     = figure-eight 4_1

INCONSISTENCY: appendix-knot-periodic-table.tex says
  Protons as left trefoils  ← WRONG (should be B_3(uud))
  Neutrons as unknots       ← WRONG (should be B_3(udd); unknot = neutrino)
  Electrons as right trefoils ← AMBIGUOUS (chirality unclear)
"""
from __future__ import annotations
import re
from pathlib import Path
from collections import defaultdict


# Patterns to flag — particle-knot identification claims
PATTERNS = [
    # The "WRONG" patterns
    (r"[Pp]roton[s]?\s+(?:are|=|as)\s+.{0,30}trefoil", "PROTON = trefoil (WRONG; should be B_3(uud))"),
    (r"[Nn]eutron[s]?\s+(?:are|=|as)\s+.{0,30}unknot", "NEUTRON = unknot (WRONG; unknot = neutrino, neutron = B_3(udd))"),
    (r"[Pp]roton[s]?\s+(?:are|=|as).{0,40}T_\{?2,3\}?", "PROTON = T_{2,3} (WRONG)"),
    (r"[Nn]eutron[s]?\s+(?:are|=|as).{0,30}K_\{?0_1\}?", "NEUTRON = K_{0_1} (WRONG)"),
    # Should-be patterns
    (r"[Pp]roton[s]?\s+(?:are|=|as).{0,30}[Bb]orr|B_3.uud", "PROTON = B_3(uud) (correct)"),
    (r"[Nn]eutron[s]?\s+(?:are|=|as).{0,30}[Bb]orr|B_3.udd", "NEUTRON = B_3(udd) (correct)"),
    (r"[Nn]eutrino.{0,30}unknot|unknot.{0,30}neutrino|T_\{?1,0\}?", "NEUTRINO = unknot (correct)"),
    (r"[Ee]lectron.{0,30}trefoil|trefoil.{0,30}electron", "ELECTRON = trefoil (correct)"),
    (r"[Pp]hoton.{0,40}empty|[Pp]hoton.{0,40}point|photon.{0,30}\\varnothing", "PHOTON = empty/point (current; user wants 4-term)"),
]


def audit_file(path: Path):
    """Yield (line_no, line, label) for each match."""
    try:
        lines = path.read_text().splitlines()
    except (UnicodeDecodeError, OSError):
        return
    for i, line in enumerate(lines, 1):
        for pattern, label in PATTERNS:
            if re.search(pattern, line):
                yield i, line.strip()[:120], label


def main():
    base = Path("content/quantum-observable-universe")
    chapters = Path("chapters")

    counts = defaultdict(int)
    findings_by_label = defaultdict(list)

    for d in [base, chapters]:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            for line_no, line, label in audit_file(path):
                counts[label] += 1
                findings_by_label[label].append((path, line_no, line))
        for path in sorted(d.rglob("*.tex")):
            for line_no, line, label in audit_file(path):
                counts[label] += 1
                findings_by_label[label].append((path, line_no, line))

    print("=" * 80)
    print("PARTICLE-KNOT IDENTIFICATION AUDIT")
    print("=" * 80)
    print()

    # WRONG patterns first (must-fix)
    print("WRONG PATTERNS (must fix):")
    print("-" * 80)
    n_wrong = 0
    for label, hits in findings_by_label.items():
        if "WRONG" not in label:
            continue
        n_wrong += len(hits)
        print(f"\n[{label}] — {len(hits)} occurrences")
        for path, line_no, line in hits[:5]:
            rel = path.relative_to(Path("."))
            print(f"  {rel}:{line_no}")
            print(f"    {line[:100]}")
        if len(hits) > 5:
            print(f"  ... and {len(hits) - 5} more")

    if n_wrong == 0:
        print("\n  (none found — clean)")
    print()

    # Correct patterns (sanity check)
    print("CORRECT PATTERNS (sources of truth):")
    print("-" * 80)
    for label, hits in sorted(findings_by_label.items()):
        if "WRONG" in label or "user wants" in label:
            continue
        if "(correct)" not in label:
            continue
        print(f"  [{label}]: {len(hits)} occurrences")
    print()

    # Photon (user-flagged for change)
    print("USER-FLAGGED FOR REVISION (4-term photon):")
    print("-" * 80)
    for label, hits in findings_by_label.items():
        if "user wants" not in label:
            continue
        print(f"\n[{label}] — {len(hits)} occurrences")
        for path, line_no, line in hits[:5]:
            rel = path.relative_to(Path("."))
            print(f"  {rel}:{line_no}")
            print(f"    {line[:100]}")
        if len(hits) > 5:
            print(f"  ... and {len(hits) - 5} more")
    print()

    print("=" * 80)
    print(f"TOTAL: {sum(counts.values())} matches across all patterns")
    print(f"  WRONG: {n_wrong}  (must fix)")
    print(f"  user-flagged: {sum(c for l, c in counts.items() if 'user wants' in l)}")


if __name__ == "__main__":
    main()
