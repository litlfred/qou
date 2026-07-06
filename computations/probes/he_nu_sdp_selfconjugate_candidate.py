#!/usr/bin/env python3
"""ν_SDP derivation attempt — the self-conjugate-count candidate, and why it stalls.

EXPLORATORY — derive-or-refute, no fit. Follows #2552 (ν_SDP has no computed
operational definition; the confirmed D/T/³He = 1, 2, 2 are manual).

The kashaev block defines ν_SDP categorically as **"the dimension of the saturating
projection in the irreducible-block decomposition H_n(q) ≅ ⊕_λ End(V_λ)"** — a
"MacMahon-style partition-algebra count" (driver x). Taking the *principled*
bar-involution-folded operator-selection SDP (§7b Type-B folding, the symmetry
regulariser with no invented weights) for the deuteron, its solution saturates on a
**single block (3,2,1)** with value tr_M(β_D) — and (3,2,1) is the **unique
self-conjugate partition of 6**. (The other Phase-B encodings hit ±10⁶ rails.)

CANDIDATE:  ν_SDP = #{ self-conjugate λ ⊢ 3A } = #{ partitions of 3A into distinct
            odd parts }  (the classic Euler/MacMahon self-conjugate identity).

This file (a) computes the candidate count, (b) checks it against the confirmed
atoms, (c) tests the structural mechanism that would justify it, and (d) records the
falsifying tension.

RESULTS
-------
(a)/(b) The count matches ALL THREE confirmed atoms:
    D (n=6):  #self-conj = 1 = ν ✓
    T (n=9):  #self-conj = 2 = ν ✓
    ³He(n=9): #self-conj = 2 = ν ✓   (T, ³He both n=9 ⇒ ν depends only on n=3A ✓)
  and predicts ⁴He(n=12)=3, ⁶Li(n=18)=5, ⁷Li(n=21)=8.

(c) MECHANISM — REFUTED. The hoped-for justification was: under the bar-fold, every
    conjugate pair (λ,λ') cancels in the Frobenius Gram (tr_M(P_λ)+tr_M(P_λ')=0,
    the §7b "sign-flip" signature), leaving only self-conjugate blocks with definite
    norm. The actual H_6 Gram (deuteron-real-sdp.witness.json frob_diag) shows the
    conjugate-pair sums are NOT zero (e.g. (6)+(1⁶)=+0.059, (4,2)+(2,2,1,1)=+0.359);
    the negative-norm "forbidden" blocks are small-negative, not the equal-and-
    opposite of their positive conjugates. So the cancellation mechanism is false,
    and the deuteron bar-fold landing on (3,2,1) is NOT explained by it.

(d) TENSION — the candidate predicts ν_SDP(⁴He)=3, but the magic-A binding
    B = ρ_F·m_e·A·8G needs ρ_F=2 (ρ_F=3 gives +59% vs AME, ρ_F=2 gives +5.87%). So
    under ρ_F = ν_SDP, the cleanest combinatorial rule matching D/T/³He CONFLICTS
    with the ⁴He binding. Either ν_SDP ≠ #self-conj, or ρ_F ≠ ν_SDP at doubly-magic
    ⁴He. Both leave ρ_F=2 unconfirmed (consistent with #2552).

VERDICT: NOT a derivation. A candidate count matching 3 confirmed atoms + the
deuteron bar-fold support, with (i) no proven mechanism and (ii) a direct conflict
with the ⁴He binding. The decisive next test (out of scope here — needs y_λ + χ^λ at
H_9) is whether the T/³He bar-fold support equals their two self-conjugate blocks
{(5,1,1,1,1),(3,3,3)}; if not, the count match is coincidence.

Output: he-nu-sdp-selfconjugate-candidate.witness.json
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent


def self_conjugate_count(n: int) -> int:
    """#{self-conjugate λ ⊢ n} = #{partitions of n into distinct odd parts}."""
    odds = list(range(1, n + 1, 2))

    @lru_cache(None)
    def go(i, rem):
        if rem == 0:
            return 1
        if i >= len(odds) or odds[i] > rem:
            return 0
        return go(i + 1, rem - odds[i]) + go(i + 1, rem)

    return go(0, n)


# Confirmed ν_SDP (manual-historical-volume-match; kashaev block).
ATOMS = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
         ("6Li", 3, 3), ("7Li", 3, 4)]
NU_CONFIRMED = {"D": 1, "T": 2, "3He": 2}


def _conj(p):
    return tuple(sum(1 for r in p if r > j) for j in range(p[0])) if p else ()


def check_h6_cancellation():
    """Test the conjugate-pair cancellation hypothesis on the H_6 Gram."""
    wpath = HERE.parent / "deuteron-real-sdp.witness.json"
    if not wpath.exists():
        return None
    d = json.loads(wpath.read_text())["data"]
    keys, g = d["partitions"], d["frobenius_gram_diag"]
    parse = lambda k: tuple(int(x) for x in k.strip("()").replace(" ", "")
                            .rstrip(",").split(",") if x)
    trM = {parse(k): g[i] for i, k in enumerate(keys)}
    pairs, selfconj = [], []
    seen = set()
    for p in trM:
        cp = _conj(p)
        if p == cp:
            selfconj.append((p, trM[p]))
        elif cp in trM and (cp, p) not in seen:
            seen.add((p, cp))
            pairs.append((p, cp, trM[p] + trM[cp]))
    cancels = all(abs(s) < 1e-6 for _, _, s in pairs)
    return {"pairs": pairs, "self_conjugate": selfconj, "all_pairs_cancel": cancels}


def main() -> int:
    print("=" * 80)
    print("  ν_SDP derivation attempt — self-conjugate-count candidate")
    print("  ν_SDP ?= #{self-conjugate λ⊢3A} = #{partitions of 3A into distinct odd parts}")
    print("=" * 80)
    rows = []
    all_match = True
    print(f"\n  {'atom':>5} {'(Z,N)':>7} {'n=3A':>5} {'#self-conj':>11} {'ν_conf':>7}")
    for nm, Z, N in ATOMS:
        n = 3 * (Z + N)
        sc = self_conjugate_count(n)
        nu = NU_CONFIRMED.get(nm)
        ok = (nu is None) or (nu == sc)
        all_match = all_match and ok
        mark = "✓" if (nu is not None and nu == sc) else ("← predicts" if nu is None else "✗")
        print(f"  {nm:>5} {str((Z, N)):>7} {n:>5} {sc:>11} {str(nu) if nu else '—':>7}  {mark}")
        rows.append({"atom": nm, "Z": Z, "N": N, "n": n, "self_conj_count": sc,
                     "nu_confirmed": nu, "match": ok})

    canc = check_h6_cancellation()
    print("\n  Mechanism test — conjugate-pair cancellation in the H_6 Gram:")
    if canc is None:
        print("    (deuteron witness not found; skipped)")
    else:
        for p, cp, s in canc["pairs"]:
            print(f"    tr_M{p} + tr_M{cp} = {s:+.3e}  {'cancel' if abs(s)<1e-6 else 'NONZERO'}")
        print(f"    self-conjugate: {[(p, round(v,4)) for p,v in canc['self_conjugate']]}")
        verdict = 'holds' if canc['all_pairs_cancel'] else 'REFUTED'
        print(f"    ⇒ all conjugate pairs cancel?  {canc['all_pairs_cancel']}  "
              f"(hypothesis {verdict})")

    print("\n  Binding tension (ρ_F = ν_SDP):")
    print(f"    candidate ⁴He(n=12) = {self_conjugate_count(12)};  magic-A needs ρ_F=2 "
          "(ρ_F=3 → +59% vs AME). CONFLICT.")
    print("\n  VERDICT: NOT a derivation — count matches 3 confirmed atoms + the deuteron")
    print("  bar-fold support, but the mechanism is refuted and ⁴He conflicts with ρ_F=2.")
    print("  Decisive next test: T/³He bar-fold support = their 2 self-conj blocks? "
          "(needs y_λ, χ^λ at H_9).")
    print("=" * 80)

    witness = {
        "computation": "he-nu-sdp-selfconjugate-candidate",
        "kind": "exploratory-probe",
        "description": (
            "Tests ν_SDP = #{self-conjugate λ⊢3A} (= distinct-odd-parts count, the "
            "kashaev driver-x MacMahon identity). Matches D/T/³He = 1,2,2 and the "
            "deuteron bar-fold SDP support (3,2,1), but the conjugate-cancellation "
            "mechanism is REFUTED on the H_6 Gram and the candidate predicts ⁴He=3, "
            "conflicting with the magic-A ρ_F=2. Not a derivation. No fit."
        ),
        "candidate": "nu_SDP = #self-conjugate(3A) = #partitions(3A into distinct odd parts)",
        "rows": rows,
        "all_confirmed_match": all_match,
        "h6_cancellation_test": (
            {"all_pairs_cancel": canc["all_pairs_cancel"],
             "pairs": [[list(p), list(cp), s] for p, cp, s in canc["pairs"]],
             "self_conjugate": [[list(p), v] for p, v in canc["self_conjugate"]]}
            if canc else None),
        "mechanism_verdict": "REFUTED (conjugate pairs do not cancel in the Gram)",
        "binding_tension": ("candidate ⁴He=3 conflicts with magic-A ρ_F=2 "
                            "(ρ_F=3 → +59% vs AME)"),
        "verdict": ("NOT a derivation: count matches 3 confirmed atoms + deuteron "
                    "bar-fold support, but no proven mechanism and ⁴He binding conflict. "
                    "Decisive test pending: T/³He bar-fold support vs their 2 self-conj blocks."),
        "refs": ["PR #2552 (ν_SDP not computable)",
                 "content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md (driver-x def)",
                 "computations/deuteron_real_sdp.py (bar-fold encoding 1)"],
        "discipline": "EXPLORATORY — derive-or-refute, no fit, no forced ⁴He number.",
    }
    out = HERE.parent / "he-nu-sdp-selfconjugate-candidate.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
