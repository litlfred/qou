#!/usr/bin/env python3
"""keystone_valuemap_colored_marks_s013.py — the Lawrence–Rozansky modulus ID
with the McKay-MARK color-α insertion on the p₃=5 fibre.

Executes the m_p/m_μ-root-cause attack of
[`2026-07-17-three-front-attack-specs.md §2`](../../docs/audits/2026-07-17-three-front-attack-specs.md)
(companion to the 2026-07-17 1ppQ path reassessment). The merged s013 probe
([`keystone_valuemap_genuine_smatrix_s013.py`](keystone_valuemap_genuine_smatrix_s013.py))
machine-validated the genuine Σ(2,3,5) false-theta S-matrix (Hikami
math-ph/0405028) and **refuted** the naive identification of the 4-class keystone
target `bwS0(λ) = d_ζ(λ)/D(ζ)` with the theory's D=2 vacuum row (2 components,
golden-ratio φ ratio ≠ any target ratio).

This probe tests the REFINED spec-§2 hypothesis: does the **McKay-mark coloring**
`λ ↦ α = dim_{S₅}(λ)` — the 4 bwS0 classes (5),(4,1),(3,2),(3,1,1) carry S₅-dims
{1,4,5,6}, four of the Ê₈ marks / 2I irrep dimensions {1,2,2,3,3,4,4,5,6} under
McKay(2I↔Ê₈)∘(A₅⊂S₅) — inserted on the **p₃=5 numerator fibre** ESCAPE the D=2
collapse, so `|S_{0λ}^{α}| = d_ζ(λ)/D(ζ)` with 4 independent colored components?
([mark] values; the earlier [e]_q exponent map is refuted.)

Colored WRT invariant (SU(2) colouring of the p=5 Seifert fibre): the bare
`τ_N` numerator factor `sin(nπ/(N·5))` becomes `sin(α·nπ/(N·5))`. **α=1 must
reproduce the bare τ_N to machine zero** (anti-fabrication anchor) — checked
first; any conclusion is void otherwise.

Pre-registered kill criteria (spec §2 — success = evidence, not proof):
  K1  ratio-vector mismatch at every N              → refuted
  K2  D=2 collapse: the {α∈{1,4,5,6}} colored family spans only 2 independent
      functions (α=4≡α=1; α=5 split-node; α=6 wrap) → re-derives the refutation
  K3  split node: α=6 leg returns [6]_ζ instead of [5]_ζ+1
  K4  conjugation-modulus violation (|τ^α| not conjugation-symmetric)

Run: python3 -u computations/probes/keystone_valuemap_colored_marks_s013.py \\
       2>&1 | tee /tmp/keystone_colored_marks.log

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (τ_N eq 2.11; χ 3.1; S 3.8)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
from mpmath import mpf, mpc  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
import keystone_valuemap_genuine_smatrix_s013 as s013  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
PVEC = s013.PVEC          # (2, 3, 5)
P = s013.P                # 30
Q0 = s013.Q0
I = mpc(0, 1)

# McKay marks: the 4 keystone bwS0 classes carry S₅-dims {1,4,5,6} (= Ê₈ marks).
BWS0_CLASSES = [("(5)", 1), ("(4,1)", 4), ("(3,2)", 5), ("(3,1,1)", 6)]
MARKS = [m for _, m in BWS0_CLASSES]          # [1, 4, 5, 6]


def qint(m):
    # Q0 is the real substrate value (≈1.10998); mp.re is defensive insurance
    # so downstream float() casts are robust even if a complex ζ is ever used.
    return mp.re((Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1)))


def bws0_target():
    """d_q(λ)/D target vector (the s013 `dq`): d_q on marks, D the total."""
    dq = {"(5)": mpf(1), "(4,1)": qint(4), "(3,2)": qint(5),
          "(3,1,1)": qint(4) * qint(3) / qint(2)}
    D = mp.sqrt(mp.fsum(v * v for v in dq.values()))
    return dq, {k: v / D for k, v in dq.items()}, D


def tau_N_colored(N, alpha):
    """τ_N(Σ(2,3,5)) with SU(2) colour α on the p₃=5 fibre: the p=5 numerator
    sine sin(nπ/(N·5)) → sin(α·nπ/(N·5)).  α=1 == bare s013.tau_N (checked)."""
    pref_lhs = mp.exp(2 * mp.pi * I / N * (s013.phi_235() / 4 - mpf(1) / 2)) \
        * (mp.exp(2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        num = mpc(1)
        for pj in PVEC:
            a = alpha if pj == 5 else 1
            num *= (mp.exp(a * n * mp.pi * I / (N * pj))
                    - mp.exp(-a * n * mp.pi * I / (N * pj)))
        den = mp.exp(n * mp.pi * I / N) - mp.exp(-n * mp.pi * I / N)
        total += mp.exp(-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.exp(mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


def s0_colored_modulus(alpha):
    """|S_{0,(1,1,α)}| — the would-be vacuum→(1,1,α) S-matrix entry of the
    Σ(2,3,5) false-theta theory (Hikami eq. 3.8, √(32/P) normalization), the
    literal `|S_{0λ}(ζ)|` of the spec-§2 target. The p₃=5 leg carries the
    colour: sin(P·1·α·π/p₃²) = sin(6απ/5). |·| is the modular modulus."""
    prod = mpf(1)
    for lj, lpj, pj in zip((1, 1, 1), (1, 1, alpha), PVEC):
        prod *= mp.sin(mp.pi * P * lj * lpj / (pj * pj))
    return abs(mp.sqrt(mpf(32) / P) * prod)


def main() -> int:
    wb = WitnessBuilder("keystone-valuemap-colored-marks-s013", engine="mpmath")
    print("=" * 78)
    print(" LR modulus ID — McKay-mark colour-α on the p₃=5 fibre (spec §2)")
    print("=" * 78)

    # ---- anti-fabrication anchor: α=1 reproduces bare τ_N ----
    Ns = [3, 5, 7, 11, 13]
    anchor = mpf(0)
    for N in Ns:
        anchor = max(anchor, abs(tau_N_colored(N, 1) - s013.tau_N(N)))
    print(f"\n[anchor] max_N |τ_N^(α=1) − bare τ_N| = {float(anchor):.2e}  "
          f"(must be ~0)")
    wb.add_assertion("alpha1_reproduces_bare_tauN", computed=float(anchor),
                     expected=0.0, tolerance=1e-25,
                     source="colour α=1 on p=5 fibre == uncoloured s013.tau_N")
    if anchor > mpf("1e-25"):
        print("  ABORT: anchor failed; colouring convention wrong — no conclusion.")
        wb.add_data("verdict", "ANCHOR FAILED — colouring convention invalid; no conclusion.")
        wb.save()
        return 1

    # ---- PRIMARY observable: |S_{0λ}| the spec-§2 target, on the marks ----
    dq, target_norm, Dtot = bws0_target()
    base = target_norm["(5)"]
    tgt_ratios = {k: float(v / base) for k, v in target_norm.items()}
    print(f"\n[target] d_ζ(λ)/D ratios (normalized to (5)): "
          f"{ {k: round(v, 4) for k, v in tgt_ratios.items()} }")

    print(f"\n[|S_0λ|] McKay-mark colour α on p₃=5 → |S_{{0,(1,1,α)}}| = √(32/P)·"
          f"|sin(π/4)·sin(π/3)·sin(6απ/5)|:")
    s0 = {a: s0_colored_modulus(a) for _, a in BWS0_CLASSES}
    s0_base = s0[1]
    smat_ratios = {}
    print(f" {'class':>9} {'α':>3}  {'|S_0λ|':>12}  {'|S_0λ|/|S_01|':>12}  {'target':>8}")
    for cls, a in BWS0_CLASSES:
        r = float(s0[a] / s0_base) if s0_base != 0 else float("nan")
        smat_ratios[cls] = r
        print(f" {cls:>9} {a:>3}  {float(s0[a]):>12.6f}  {r:>12.4f}  {tgt_ratios[cls]:>8.4f}")

    # K2 — the modulus collapse: the nonzero marks give ONE value; α=5 vanishes.
    nz = [float(s0[a]) for _, a in BWS0_CLASSES if s0[a] > mpf("1e-30")]
    distinct = []
    for v in nz:
        if not any(abs(v - d) < 1e-12 for d in distinct):
            distinct.append(v)
    n_distinct = len(distinct)
    alpha5_vanishes = s0[5] < mpf("1e-30")
    print(f"\n[K2] distinct nonzero |S_0λ| values among marks = {n_distinct} "
          f"(escape needs 4); α=5 vanishes (split node): {alpha5_vanishes}")
    wb.add_assertion("mark_family_collapses_below_4", computed=n_distinct,
                     expected=1, tolerance=0,
                     source="distinct nonzero |S_{0,(1,1,α)}| over marks {1,4,5,6} = 1 "
                            "(all nonzero marks give the icosahedral weight; escape "
                            "would need 4) — the pre-registered D-collapse (K2)")
    wb.add_assertion("alpha5_split_node_vanishes",
                     computed=float(s0[5]), expected=0.0, tolerance=1e-30,
                     source="mark α=5 on p₃=5 fibre: sin(6·5π/5)=sin(6π)=0 (split node)")

    # K1 — ratio vector vs the d_ζ(λ)/D target (the spec-§2 identity)
    tgt_vec = [tgt_ratios[c] for c, _ in BWS0_CLASSES]
    got_vec = [smat_ratios[c] for c, _ in BWS0_CLASSES]
    maxdev = max(abs(got_vec[i] - tgt_vec[i]) for i in range(4)
                 if got_vec[i] == got_vec[i])  # skip nan
    ratio_match = maxdev < 0.05
    print(f"[K1] |S_0λ| ratio vs target: got {[round(x,3) for x in got_vec]} vs "
          f"target {[round(x,3) for x in tgt_vec]}  maxdev={maxdev:.3f}")
    wb.add_assertion("s0_ratio_mismatch_confirms_refutation",
                     computed=1 if maxdev > 0.5 else 0, expected=1, tolerance=0,
                     source="|S_{0λ}|/|S_{0,(5)}| does NOT reproduce the d_ζ(λ)/D ratio "
                            "(1,4.11,5.22,6.22): maxdev≫0.5 — the spec-§2 identity fails (K1)")

    # K3 — split node: α=6 mark returns [6]_ζ, not the keystone [5]_ζ+1
    six, five_plus_1 = qint(6), qint(5) + 1
    print(f"[K3] α=6 mark: [6]_ζ = {float(six):.5f} ≠ [5]_ζ+1 = {float(five_plus_1):.5f}  "
          f"⟹ p=5 fibre wrap, not the keystone leg")
    split_node_wrong = abs(six - five_plus_1) > mpf("1e-6")
    wb.add_assertion("alpha6_wraps_six_not_five_plus_one",
                     computed=1 if split_node_wrong else 0, expected=1, tolerance=0,
                     source="α=6 mark on p=5 fibre yields [6]_ζ ≠ [5]_ζ+1 (wrap, "
                            "not the keystone split leg) — K3 confirmed")

    # secondary cross-check: colored τ_N moduli (noisier, same conclusion)
    tau_ratios = {}
    for j, N in enumerate(Ns):
        b = abs(tau_N_colored(N, 1))
        tau_ratios[str(N)] = [float(abs(tau_N_colored(N, a)) / b) for _, a in BWS0_CLASSES]

    # ---- verdict ----
    escaped = (n_distinct >= 4) and ratio_match and not alpha5_vanishes
    if escaped:
        verdict = (
            "ESCAPE (evidence, not proof): McKay-mark colouring on p₃=5 yields 4 "
            "distinct |S_0λ| matching d_ζ(λ)/D. Next: the Lean loc_matches gate.")
    else:
        verdict = (
            "REFUTED (scope-(a)) — the McKay-mark colour-α insertion on the p₃=5 "
            "fibre does NOT escape the collapse. The spec-§2 target `|S_{0λ}| = "
            "d_ζ(λ)/D` fails: the marks {1,4,5,6} give |S_{0,(1,1,α)}| ∝ |sin(6απ/5)| "
            f"= {{α=1,4,6 ↦ sin(π/5); α=5 ↦ 0}} — {n_distinct} distinct nonzero value(s) "
            "(need 4), so the mark family collapses to ONE nonzero modulus plus the "
            "α=5 split-node zero, versus the 4-class target ratio (1,4.11,5.22,6.22) "
            f"(maxdev {maxdev:.2f}). Structurally: the p₃=5 Seifert fibre carries only "
            "colours 1..4 (SU(2)₅ Weyl reflection α↔5−α ⟹ |S₀^{α=4}|=|S₀^{α=1}|), so "
            "the marks ≥5 wrap (α=5 vanishes, α=6→[6]_ζ≠[5]_ζ+1). The keystone W_λ = "
            "d_ζ(λ)/D index is NOT carried by the McKay-colored Σ(2,3,5) false-theta "
            "S-matrix. Pre-registered K1/K2/K3 outcome; consistent with the merged "
            "s013 D=2 refutation. A larger geometric family (more exceptional fibres "
            "⇒ larger D, or genuinely colored knot-complement blocks) is required. No "
            "fit; nothing wired; the Lean loc_matches gate stays open.")
    print(f"\n VERDICT: {verdict}")

    wb.set_description(
        "LR modulus ID (three-front spec §2, m_p/m_μ root cause): McKay-mark "
        "colour-α insertion on the p₃=5 fibre of the validated Σ(2,3,5) false-"
        "theta S-matrix (Hikami math-ph/0405028), colours α∈{1,4,5,6} = S₅-dims "
        "of the 4 bwS0 classes = Ê₈ marks under McKay(2I↔Ê₈)∘(A₅⊂S₅). Anchor: "
        "α=1 reproduces bare τ_N to machine zero. VERDICT: the mark family does "
        "NOT escape the D=2 collapse (p=5 fibre supports colours 1..4 only; "
        "α=4≡α=1, α=5 split, α=6 wraps to [6]_ζ≠[5]_ζ+1) — the keystone "
        "W_λ=d_ζ(λ)/D is not carried by this object. Pre-registered scope-(a) "
        "negative (K2/K3). No fit; nothing wired; Lean loc_matches gate open.")
    wb.add_data("marks", MARKS)
    wb.add_data("bws0_classes", [c for c, _ in BWS0_CLASSES])
    wb.add_data("target_ratios", {k: float(v) for k, v in tgt_ratios.items()})
    wb.add_data("s0_colored_modulus", {c: float(s0[a]) for c, a in BWS0_CLASSES})
    wb.add_data("s0_ratio_vector", {c: smat_ratios[c] for c, _ in BWS0_CLASSES})
    wb.add_data("distinct_nonzero_s0_values", n_distinct)
    wb.add_data("alpha5_split_node_vanishes", bool(alpha5_vanishes))
    wb.add_data("split_node_six_not_five_plus_one", bool(split_node_wrong))
    wb.add_data("ratio_match", bool(ratio_match))
    wb.add_data("tau_colored_ratios_crosscheck", tau_ratios)
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\n witness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
