#!/usr/bin/env python3
"""
r11a_three_factor_separability_probe.py — R11-a: derive-or-refute the proposed 3-FACTOR
multiplicative closure of the deuteron/triton/neutron-ladder miss (bean z2bn / #3808 round-11).

CONTEXT (consumes the committed R10 witness — no recompute, anti-duplication). R10
(`deuteron_ladder_falsification_probe.py`, 2026-07-14) established that the Model-G miss
`miss(k, A_light) = deficit − [3b·C(k,2)·[k≥3] + k·A_light·b]` peaks at a FIXED k=3 across all
three (kα)+X ladders — X = n/d/t, A_light = 1/2/3 — the 3-α Brunnian onset, NOT a resonance at
k=A_light. #3808 (round-11) proposed the residual miss factorizes as a 3-FACTOR product:

    miss(k, A_light)  ?=  E(k) · amp(A_light) · parity(k)          [the R11-a hypothesis]

with E(k) a fixed k-envelope (peak at k=3), amp(A_light) an A_light-amplitude (near-linear at the
peak), parity(k) a bar-parity fall. THIS PROBE tests that multiplicative separability directly and
derives-or-refutes each factor. Falsification-first (compute-author §3.3); no fitted constant is
wired; scope-(a).

MISS TABLE (read from the R10 witness, MeV):

        A_light=1     A_light=2     A_light=3
  k=1      —           −0.090         0.122
  k=2     0.009         2.807         6.440
  k=3     2.838 ★       5.818 ★       8.048 ★      (★ = peak, fixed at k=3)
  k=4     1.377         1.632         2.679

TWO STRUCTURAL TESTS:

  (T1) Multiplicative separability. If miss = E(k)·amp(A), then normalizing each ladder by its own
       k=3 value must give an A_light-INDEPENDENT envelope Ê(k) = miss(k,A)/miss(3,A). Test whether
       the normalized k=2 (and k=4) rows agree across the three ladders.

  (T2) Brunnian hard-gate. The μ̄₁₂₃ triple-linking (Milnor) invariant is the first genuinely
       3-cluster topological invariant — pairwise linking (k≤2 α-pairs) cannot detect a Borromean
       triple (all pairwise lk = 0 yet μ̄₁₂₃ ≠ 0). A PURE triple-gate would force miss(k<3) = 0.
       Test whether the miss actually vanishes below k=3.

FINDINGS (scope-(a)):
  (T1) REFUTED — the normalized k=2 envelope is 0.003 / 0.483 / 0.800 across A_light = 1/2/3
       (varies >250×), so the miss is NOT a clean E(k)·amp(A_light) product. It requires at least
       TWO ADDITIVE channels: a k=3-peaked 3-cluster term + an A_light-graded term whose k=2 weight
       grows with A_light.
  (T2) REFUTED as a *pure* hard gate — miss(k=2) is 2.807 / 6.440 (d/t), not 0, so a Brunnian-
       triple-only envelope is excluded; there is a pairwise-detectable k=2 channel below the
       triple onset. The Brunnian μ̄₁₂₃ structure grounds the k=3 PEAK / interior-max (the first
       irreducible 3-cluster term), but is not the sole source.

NET: the 3-factor MULTIPLICATIVE closure is refuted; the honest structure is additive-2-channel
(3-cluster peak ⊕ A_light-graded pairwise), consistent with R9's P1/P2 interior-max prunes. This
narrows R11-a: the derivation target is the ADDITIVE split, not a product. No fit; scope-(a).

Audit: docs/audits/2026-07-17-r11a-three-factor-separability-refuted.md
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "deuteron-ladder-falsification.witness.json"


def load_ladders():
    w = json.load(open(WITNESS))
    ladders = {}
    for key, Al in [("neutron_ladder_A_light_1", 1),
                    ("deuteron_ladder_A_light_2", 2),
                    ("triton_ladder_A_light_3", 3)]:
        ladders[Al] = {rec["k"]: (iso, rec["miss_MeV"]) for iso, rec in w[key].items()}
    return ladders


def main() -> int:
    ladders = load_ladders()
    print("=== R11-a: derive-or-refute the 3-factor multiplicative closure of the ladder miss ===\n")

    print("miss(k, A_light) [MeV], from the committed R10 witness:")
    print(f"  {'k':>2} | {'A=1':>8} {'A=2':>8} {'A=3':>8}")
    for k in (1, 2, 3, 4):
        row = []
        for Al in (1, 2, 3):
            v = ladders[Al].get(k)
            row.append(f"{v[1]:8.3f}" if v else f"{'—':>8}")
        star = "  ★ peak" if k == 3 else ""
        print(f"  {k:>2} | {' '.join(row)}{star}")

    # ---- (T1) multiplicative separability: normalize each ladder by its k=3 peak ----
    print("\n--- (T1) Multiplicative separability  miss(k,A) ?= E(k)·amp(A) ---")
    print("  Normalize each ladder by its own k=3 value ⇒ envelope Ê(k)=miss(k,A)/miss(3,A).")
    print("  If separable, Ê(k) is A_light-INDEPENDENT (same across the three columns).")
    print(f"  {'k':>2} | {'Ê|A=1':>8} {'Ê|A=2':>8} {'Ê|A=3':>8}   spread(max/min)")
    separable = True
    for k in (1, 2, 3, 4):
        norms = []
        for Al in (1, 2, 3):
            v = ladders[Al].get(k)
            peak = ladders[Al][3][1]
            norms.append(v[1] / peak if v else None)
        present = [x for x in norms if x is not None]
        cells = " ".join(f"{x:8.3f}" if x is not None else f"{'—':>8}" for x in norms)
        # spread among positive entries (k=1 has sign noise near zero → skip)
        pos = [x for x in present if x > 0.02]
        spread = (max(pos) / min(pos)) if len(pos) >= 2 else float("nan")
        flag = ""
        if k in (2, 4) and len(pos) >= 2 and spread > 1.5:
            separable = False
            flag = "  ← envelope varies with A_light ⇒ NOT separable"
        print(f"  {k:>2} | {cells}   {spread:6.2f}x{flag}")
    print(f"\n  (T1) multiplicative separability: {'HOLDS' if separable else 'REFUTED'}"
          f" — the k=2 normalized envelope varies "
          f"{ladders[1][2][1]/ladders[1][3][1]:.3f}/{ladders[2][2][1]/ladders[2][3][1]:.3f}"
          f"/{ladders[3][2][1]/ladders[3][3][1]:.3f} across A_light=1/2/3.")

    # ---- (T2) Brunnian hard-gate: does the miss vanish below k=3? ----
    print("\n--- (T2) Brunnian triple hard-gate  miss(k<3) ?= 0 ---")
    print("  μ̄₁₂₃ (Milnor triple-linking) is the first 3-cluster invariant; pairwise linking")
    print("  (k≤2) cannot detect a Borromean triple. A PURE triple-gate forces miss(k<3)=0.")
    below = []
    for Al in (1, 2, 3):
        for k in (1, 2):
            v = ladders[Al].get(k)
            if v:
                below.append((k, Al, v[0], v[1]))
    nonzero_below = [(k, Al, iso, m) for (k, Al, iso, m) in below if abs(m) > 0.2]
    for k, Al, iso, m in below:
        tag = "  ← NONZERO below k=3" if abs(m) > 0.2 else "  (≈0, closed)"
        print(f"   k={k} A_light={Al} {iso:>4}: miss={m:7.3f}{tag}")
    hardgate = len(nonzero_below) == 0
    print(f"\n  (T2) pure Brunnian hard-gate: {'HOLDS' if hardgate else 'REFUTED'} — "
          f"{len(nonzero_below)} isotope(s) carry nonzero miss at k<3 "
          f"(e.g. ¹⁰B {ladders[2][2][1]:.2f}, ¹¹B {ladders[3][2][1]:.2f} MeV). The μ̄₁₂₃ triple")
    print("  structure grounds the k=3 PEAK (first irreducible 3-cluster term), not a hard gate.")

    # ---- Net structural conclusion ----
    print("\n### Net (scope-(a)):")
    print("  • The 3-FACTOR MULTIPLICATIVE closure E(k)·amp(A)·parity(k) is REFUTED (T1).")
    print("  • A pure Brunnian-triple hard gate is REFUTED (T2) — a pairwise k=2 channel exists.")
    print("  • Honest structure: ADDITIVE 2-channel — a k=3-peaked 3-cluster term ⊕ an A_light-")
    print("    graded pairwise term (k=2 weight grows with A_light). Consistent with R9 P1/P2")
    print("    interior-max prunes. R11-a derivation target = the additive split, NOT a product.")
    print("  • No fitted constant wired; magnitudes not interpreted (numerology guard).")

    ok = (not separable) and (not hardgate)
    try:
        sys.path.insert(0, str(HERE.parent / "substrate"))
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("r11a-three-factor-separability", engine="python (witness-fed R10)")
        wb.set_description(
            "R11-a (z2bn/#3808): derive-or-refute the proposed 3-FACTOR multiplicative closure "
            "miss(k,A_light)=E(k)·amp(A_light)·parity(k) of the deuteron/triton/neutron-ladder miss "
            "(consumes the committed R10 deuteron-ladder-falsification witness; no recompute). "
            "(T1) Multiplicative separability REFUTED: normalizing each ladder by its k=3 peak gives "
            "a k=2 envelope 0.003/0.483/0.800 across A_light=1/2/3 (>250× spread) — the miss is not "
            "E(k)·amp(A). (T2) Pure Brunnian μ̄₁₂₃ triple hard-gate REFUTED: miss is nonzero at k=2 "
            "(¹⁰B 2.81, ¹¹B 6.44 MeV), so a triple-linking-only envelope is excluded; μ̄₁₂₃ grounds "
            "the k=3 PEAK (first irreducible 3-cluster term) not a hard gate. NET: the multiplicative "
            "closure is refuted; honest structure is ADDITIVE 2-channel (k=3-peaked 3-cluster ⊕ "
            "A_light-graded pairwise), consistent with R9 P1/P2 interior-max prunes; R11-a target = "
            "the additive split. Scope-(a), no fit, no wiring, magnitudes not interpreted.")
        wb.add_data("miss_table", {f"k{k}_A{Al}": ladders[Al][k][1]
                                   for Al in (1, 2, 3) for k in (1, 2, 3, 4) if k in ladders[Al]})
        wb.add_data("normalized_k2_envelope",
                    {f"A{Al}": ladders[Al][2][1] / ladders[Al][3][1] for Al in (1, 2, 3)})
        wb.add_data("multiplicative_separable", bool(separable))
        wb.add_data("brunnian_hard_gate", bool(hardgate))
        wb.add_assertion(
            name="three_factor_multiplicative_closure_refuted",
            computed=str(int(bool(ok))), expected="1", tolerance=0,
            source=("The proposed miss=E(k)·amp(A_light)·parity(k) product is refuted: the "
                    "k=3-normalized k=2 envelope varies 0.003/0.483/0.800 across A_light=1/2/3 "
                    "(T1), and the miss is nonzero at k=2 so a pure Brunnian triple hard-gate is "
                    "also refuted (T2). Honest structure = additive 2-channel (k=3-peaked 3-cluster "
                    "⊕ A_light-graded pairwise). Scope-(a); no fit."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
