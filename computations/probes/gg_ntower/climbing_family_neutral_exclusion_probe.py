#!/usr/bin/env python3
"""Linking neutrality excludes the climbing family e0 e2 Sigma1^c, c >= 1 (bean qou-cds1, route A).

Lean twin: QOU.MassTheory.ClimbingFamilyNeutralExclusion (core Lean, sorry-free).

Independent check in exact integer arithmetic (no floats). For each c the four braid words of
(q - s0)(q - s2) Sigma1^c, Sigma1 = s1 s0 s2 s1, are closed on four strands; the closure
components are the cycles of the strand permutation, and a word is linking-neutral when every
component's signed self-crossing count and every pairwise signed crossing count is zero
(the definition of QOU.PhotonU1NeutralCut.Neutral, carried to four strands).

Expected: c = 0 keeps only the identity word; every c >= 1 keeps nothing; writhe of each word
lies in [4c, 4c+2]. Controls: V = s0 s1^-1 is neutral, Sigma1 is not.
This is a filter on braid words, not a numerical prediction; no q0 enters.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
N = 4
SIGMA1 = [(1, 1), (0, 1), (2, 1), (1, 1)]
JONES = {"1": [], "s0": [(0, 1)], "s2": [(2, 1)], "s0s2": [(0, 1), (2, 1)]}


def components(word):
    pos = list(range(N))  # pos[k] = strand label at position k
    for i, _ in word:
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    # strand starting at position k ends at the position where label k sits; closure maps k -> that
    end = {lab: k for k, lab in enumerate(pos)}
    comp, seen = {}, set()
    for s in range(N):
        if s in seen:
            continue
        cyc, x = [], s
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = end[x]
        for x in cyc:
            comp[x] = min(cyc)
    return comp


def pair_counts(word):
    comp = components(word)
    pos = list(range(N))
    counts = {}
    for i, e in word:
        a, b = sorted((comp[pos[i]], comp[pos[i + 1]]))
        counts[(a, b)] = counts.get((a, b), 0) + e
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return counts


def neutral(word):
    return all(v == 0 for v in pair_counts(word).values())


def writhe(word):
    return sum(e for _, e in word)


def main():
    checks, rows = {}, []
    for c in range(0, 6):
        kept = []
        for name, w in JONES.items():
            word = w + SIGMA1 * c
            wr, nt = writhe(word), neutral(word)
            rows.append({"c": c, "term": name, "writhe": wr, "neutral": nt})
            assert 4 * c <= wr <= 4 * c + 2
            if nt:
                kept.append(name)
        checks[f"c={c}_kept"] = kept
    checks["c0_keeps_identity_only"] = checks["c=0_kept"] == ["1"]
    checks["c>=1_keeps_nothing"] = all(checks[f"c={c}_kept"] == [] for c in range(1, 6))
    checks["control_V_neutral"] = neutral([(0, 1), (1, -1)])
    checks["control_Sigma1_not_neutral"] = not neutral(SIGMA1)
    ok = all(checks[k] for k in ("c0_keeps_identity_only", "c>=1_keeps_nothing",
                                 "control_V_neutral", "control_Sigma1_not_neutral"))
    out = {
        "computation": "climbing-family-neutral-exclusion",
        "scriptFile": Path(__file__).name,
        "kind": "structural filter check (exact integers; no q0, no search, no selection)",
        "beans": ["qou-cds1", "qou-4f8t"],
        "q0Anchor": "independent",
        "q0AnchorReason": ("pure braid-word combinatorics in exact integers; the producer "
                           "imports only json and pathlib and never reads q0"),
        "lean": "QOU.MassTheory.ClimbingFamilyNeutralExclusion.not_neutral_support",
        "scope": ("(b) structural exclusion, invariant = writhe homomorphism; braid group "
                  "algebra of B4 before the Hecke quotient. In H4(q), e0e2 Sigma1 = q^2 e0e2, "
                  "so the Hecke image is not addressed."),
        "checks": checks,
        "rows": rows,
        "all_pass": ok,
    }
    (HERE / "climbing-family-neutral-exclusion.witness.json").write_text(
        json.dumps(out, indent=1) + "\n")
    print(json.dumps(checks, indent=1))
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
