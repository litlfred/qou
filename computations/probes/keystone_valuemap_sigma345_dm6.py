#!/usr/bin/env python3
"""s013 redirect (i) — the LARGER-D Seifert lead: does Σ(3,4,5) (D=6, γ=4 flat
connections) host the 4-class keystone target the D=2 Σ(2,3,5) row could not?

Context. The genuine Σ(2,3,5) false-theta S-matrix vacuum row was settled
NEGATIVE at the modular level (2026-07-02, keystone_valuemap_genuine_smatrix):
it is 2-dimensional, ∝ (sin π/5, sin 2π/5), ratio = golden φ. The keystone
target bwS0(λ) = d_q(λ)/D at n=5 is a 4-CLASS family with ratios
(1, 4.110, 5.220, 6.220). The refutation note listed one un-run redirect:

    "(i) Seifert manifolds with larger D whose S-matrix row could host 4
     classes — e.g. D(3,4,5) = (2·3·4)/4 = 6, γ(3,4,5) = 4 flat connections."

Σ(3,4,5) is the smallest pairwise-coprime Brieskorn sphere whose flat-connection
count is exactly 4 = the number of bwS0 classes at n=5. This probe extends the
already-VALIDATED Hikami machinery (eq. 3.1 characters, eq. 3.8 S-matrix — the
same generic code, re-pointed to PVEC=(3,4,5)) and tests the type + value match,
anchored by the S² = 1 involution property (the anti-fabrication check that
caught sign errors in the (2,3,5) transcription).

Two levels of result, kept distinct per the (a)/(b) refutation-scope rule:

  * VALUE (numerical, single-q₀): compute the genuine D=6 vacuum row (fixed
    algebraic constants), sort its magnitudes, and test whether any admissible
    4-subset reproduces (1, 4.110, 5.220, 6.220).

  * ROBUSTNESS (structural softener): the genuine modular S-matrix entries
    √(32/P)·∏ sin(P ℓⱼℓ'ⱼπ/pⱼ²) are RATIONAL-ANGLE SINES — manifestly
    INDEPENDENT of the substrate q₀. bwS0(λ) = d_q(λ)/D is a non-constant
    function of q₀ (dq_i/dq₀ ≠ 0, computed here). So a compact-modular match, if
    any, holds only at the single substrate point and is non-robust — exactly the
    reason the 2026-07-02 screen probe redirected the value map to the
    NON-COMPACT (q₀-dependent) q-Bessel vacuum row. This does NOT by itself
    exclude a single-point coincidence; the numerical test above decides that.

No fit; the S-matrix is transcribed verbatim from the validated (2,3,5) probe
(Hikami eq. 3.8) with only PVEC/P changed; nothing wired; CAL-1/2/3 untouched.

Output: keystone-valuemap-sigma345-dm6.witness.json

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694 (eqs. 3.1, 3.8)
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

PVEC = (3, 4, 5)
P = PVEC[0] * PVEC[1] * PVEC[2]          # 60
TWO_P = 2 * P                            # 120
Q0 = mpf("1.1099785955541805")

# bwS0 target: d_q(λ)/D at n=5, the 4 conjugation-class representatives
#   (5)      → [1]_q            = 1
#   (4,1)    → [4]_q            ≈ 4.110
#   (3,2)    → [5]_q            ≈ 5.220
#   (3,1,1)  → [4]_q[3]_q/[2]_q ≈ 6.220   (self-conjugate; sole product)


def qint(m, q=Q0):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def bwS0_targets(q=Q0):
    return {
        "(5)": mpf(1),
        "(4,1)": qint(4, q),
        "(3,2)": qint(5, q),
        "(3,1,1)": qint(4, q) * qint(3, q) / qint(2, q),
    }


# ── Hikami eq. (3.1): odd periodic character (generic in PVEC/P) ──────────────
def chi_hikami(triple):
    """χ^{(ℓ1,ℓ2,ℓ3)}_{2P}: +1 at n ≡ P(1+Σ εⱼℓⱼ/pⱼ) mod 2P with ε1ε2ε3=−1,
    −1 with +1, else 0. Returns {residue mod 2P: ±1}. Requires the argument to
    be integral (holds when P·ℓⱼ/pⱼ ∈ ℤ, i.e. pⱼ | P·ℓⱼ — true since pⱼ | P)."""
    out = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            for e3 in (-1, 1):
                val = Fraction(P) * (1
                                     + Fraction(e1 * triple[0], PVEC[0])
                                     + Fraction(e2 * triple[1], PVEC[1])
                                     + Fraction(e3 * triple[2], PVEC[2]))
                assert val.denominator == 1
                r = int(val) % TWO_P
                out[r] = 1 if e1 * e2 * e3 == -1 else -1
    return out


# ── Hikami eq. (3.8): the D×D modular S-matrix (generic in PVEC/P) ────────────
def s_entry(l, lp):
    """S^{ℓ'}_{ℓ} = √(32/P)·(−1)^{1+P+PΣ(ℓⱼ+ℓ'ⱼ)/pⱼ+(ℓ×ℓ')·p}·∏ sin(P ℓⱼℓ'ⱼπ/pⱼ²)."""
    expo = Fraction(1 + P)
    for lj, lpj, pj in zip(l, lp, PVEC):
        expo += Fraction(P * (lj + lpj), pj)
    cross = ((l[1] * lp[2] - l[2] * lp[1]) * PVEC[0]
             + (l[2] * lp[0] - l[0] * lp[2]) * PVEC[1]
             + (l[0] * lp[1] - l[1] * lp[0]) * PVEC[2])
    expo += cross
    assert expo.denominator == 1
    sign = (-1) ** (int(expo) % 2)
    prod = mpf(1)
    for lj, lpj, pj in zip(l, lp, PVEC):
        prod *= mp.sin(mp.pi * P * lj * lpj / (pj * pj))
    return mp.sqrt(mpf(32) / P) * sign * prod


def independent_triples():
    """Enumerate ℓⱼ ∈ {1..pⱼ−1}, group by identical χ-table → the D independent
    vector-valued components. The vacuum class is the one containing (1,1,1)."""
    classes = []           # list of (representative_triple, chi_table)
    seen_tables = []
    for l1 in range(1, PVEC[0]):
        for l2 in range(1, PVEC[1]):
            for l3 in range(1, PVEC[2]):
                tbl = chi_hikami((l1, l2, l3))
                # skip the all-zero character (non-contributing), if any
                if not tbl:
                    continue
                key = tuple(sorted(tbl.items()))
                # identify with its bar-image class (same table)
                if key in seen_tables:
                    continue
                seen_tables.append(key)
                classes.append(((l1, l2, l3), tbl))
    return classes


def min_support(tbl):
    """Leading support residue → effective CS label n; CS = −n²/(4P)."""
    return min(r for r in tbl if r != 0)


def run():
    out = {"pvec": list(PVEC), "P": P, "q0": float(Q0)}

    classes = independent_triples()
    reps = [c[0] for c in classes]
    out["num_independent_components_D"] = len(reps)
    out["D_formula"] = (PVEC[0] - 1) * (PVEC[1] - 1) * (PVEC[2] - 1) // 4
    out["representatives"] = [list(r) for r in reps]

    # vacuum class index (the one containing (1,1,1))
    vac_idx = next(i for i, r in enumerate(reps) if r == (1, 1, 1))
    out["vacuum_triple"] = list(reps[vac_idx])

    # full D×D S-matrix + involution anchor
    D = len(reps)
    S = [[s_entry(reps[i], reps[j]) for j in range(D)] for i in range(D)]
    s2 = [[mp.fsum(S[i][k] * S[k][j] for k in range(D)) for j in range(D)]
          for i in range(D)]
    max_off = max(abs(s2[i][j] - (1 if i == j else 0))
                  for i in range(D) for j in range(D))
    out["S_squared_minus_I_maxabs"] = mp.nstr(max_off, 6)
    out["S_squared_is_identity"] = bool(max_off < mpf("1e-30"))

    # rows orthonormal ⇒ vacuum row entries² sum to 1 (a second exact anchor)
    vac_row = S[vac_idx]
    row_norm = mp.fsum(x * x for x in vac_row)
    out["vacuum_row_norm_sq"] = mp.nstr(row_norm, 12)
    out["vacuum_row_is_unit"] = bool(abs(row_norm - 1) < mpf("1e-30"))

    # effective CS labels per component (diagnostic)
    cs = {}
    for i, (rep, tbl) in enumerate(classes):
        n = min_support(tbl)
        cs[str(list(rep))] = {"n": n, "CS": f"-{n*n}/{4*P}"}
    out["effective_CS_labels"] = cs

    # the genuine vacuum row (fixed algebraic constants, q₀-INDEPENDENT)
    row_abs = sorted((abs(x) for x in vac_row), reverse=True)
    out["vacuum_row_abs_sorted"] = [mp.nstr(x, 30) for x in row_abs]
    # normalise so the smallest nonzero entry = 1 (ratio structure)
    nz = [x for x in row_abs if x > mpf("1e-40")]
    out["num_nonzero_vacuum_entries"] = len(nz)
    base = nz[-1]
    ratios_desc = [mp.nstr(x / base, 12) for x in nz]
    out["vacuum_row_ratios_over_smallest"] = ratios_desc

    # bwS0 targets and the match test
    tgt = bwS0_targets()
    tgt_sorted = sorted(tgt.values())            # ascending: 1, 4.11, 5.22, 6.22
    out["bwS0_targets"] = {k: mp.nstr(v, 12) for k, v in tgt.items()}
    out["bwS0_targets_sorted"] = [mp.nstr(v, 12) for v in tgt_sorted]

    # test: does any ascending 4-subset of the normalised row match the 4 targets?
    from itertools import combinations
    ratios_asc = sorted(x / base for x in nz)
    best_err = None
    best_sub = None
    for sub in combinations(range(len(ratios_asc)), 4):
        cand = [ratios_asc[i] for i in sub]
        # both ascending; compare elementwise relative error
        err = max(abs(cand[k] / tgt_sorted[k] - 1) for k in range(4))
        if best_err is None or err < best_err:
            best_err = err
            best_sub = [mp.nstr(c, 10) for c in cand]
    out["best_4subset"] = best_sub
    out["best_4subset_max_relerr"] = mp.nstr(best_err, 8)
    matched = bool(best_err < mpf("0.01"))
    out["value_match_within_1pct"] = matched

    # ROBUSTNESS softener: bwS0 targets move with q₀; the geometric row does not
    dq = mpf("1e-6")
    tgt_lo = sorted(bwS0_targets(Q0 - dq).values())
    tgt_hi = sorted(bwS0_targets(Q0 + dq).values())
    slopes = [mp.nstr((hi - lo) / (2 * dq), 8) for lo, hi in zip(tgt_lo, tgt_hi)]
    out["bwS0_dtarget_dq0"] = slopes
    out["bwS0_is_q0_dependent"] = bool(
        max(abs((hi - lo) / (2 * dq)) for lo, hi in zip(tgt_lo, tgt_hi)) > mpf("0.1"))
    out["geometric_row_is_q0_independent"] = True  # rational-angle sines, no q₀

    out["verdict"] = (
        "MATCH — Σ(3,4,5) vacuum row hosts the 4-class target (see best_4subset); "
        "check q₀-robustness before wiring."
        if matched else
        "REFUTED-as-is (scope (a)): the genuine Σ(3,4,5) D=6 modular vacuum row "
        "does not reproduce the 4-class bwS0 target (1, 4.110, 5.220, 6.220) within "
        "1%. Softener (scope (b), invariant = q₀-independence of rational-angle "
        "modular sines): no COMPACT Seifert modular S-matrix vacuum row — a tuple "
        "of fixed algebraic constants — can track the q₀-dependent bwS0(λ)=d_q/D as "
        "the substrate modulus varies; a single-q₀ coincidence is the only way, and "
        "it does not occur here. Confirms the 2026-07-02 redirect to the NON-COMPACT "
        "q-Bessel (q₀-dependent) vacuum row as the sole viable geometric object.")
    return out


def report(res):
    print("# s013 redirect (i) — Σ(3,4,5) larger-D Seifert value-map gate\n")
    print(f"- D(3,4,5) = {res['D_formula']}; enumerated independent components = "
          f"**{res['num_independent_components_D']}**; representatives "
          f"{res['representatives']}")
    print(f"- vacuum triple = {res['vacuum_triple']}")
    print(f"- S² = I (anti-fabrication anchor): **{res['S_squared_is_identity']}** "
          f"(max |S²−I| = {res['S_squared_minus_I_maxabs']})")
    print(f"- vacuum row unit-norm (orthonormality anchor): "
          f"**{res['vacuum_row_is_unit']}** (‖row‖² = {res['vacuum_row_norm_sq']})")
    print(f"- vacuum row |entries| (sorted): {res['vacuum_row_abs_sorted']}")
    print(f"- nonzero entries: {res['num_nonzero_vacuum_entries']}; "
          f"ratios over smallest: {res['vacuum_row_ratios_over_smallest']}")
    print(f"- bwS0 targets (ascending): {res['bwS0_targets_sorted']}")
    print(f"- best 4-subset: {res['best_4subset']}  "
          f"(max rel err {res['best_4subset_max_relerr']})")
    print(f"- **value match within 1%: {res['value_match_within_1pct']}**")
    print(f"- bwS0 dtarget/dq₀ = {res['bwS0_dtarget_dq0']} "
          f"(q₀-dependent: {res['bwS0_is_q0_dependent']}); geometric row "
          f"q₀-independent: {res['geometric_row_is_q0_independent']}")
    print(f"\n**VERDICT:** {res['verdict']}")


def main():
    res = run()
    report(res)
    wb = WitnessBuilder("keystone-valuemap-sigma345-dm6",
                        engine="mpmath", output_dir=HERE)
    wb.set_description(
        "s013 redirect (i): extend the validated Hikami eq.3.1/3.8 machinery to "
        "Σ(3,4,5) (D=6, γ=4 flat connections) and test whether its D=6 modular "
        "vacuum row reproduces the 4-class keystone target bwS0=d_q/D = "
        "(1,4.110,5.220,6.220). S²=I + unit-row anchors; q₀-robustness softener. "
        "No fit; nothing wired.")
    for k, v in res.items():
        wb.add_data(k, v)
    wb.add_assertion("S_squared_is_identity", str(res["S_squared_is_identity"]),
                     "True",
                     source="eq.3.8 involution — anti-fabrication anchor on the "
                            "transcription (a sign/factor error breaks S²=I)")
    wb.add_assertion("value_match_within_1pct", str(res["value_match_within_1pct"]),
                     "False",
                     source="refutation gate: if a future transcription change "
                            "produces a 1% match this must FAIL so the near-match "
                            "gets re-adjudicated")
    path = wb.save()
    print(f"\nwitness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
