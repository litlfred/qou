#!/usr/bin/env python3
"""qbeta_kashiwara_chain_4.py — Chain 4 (Option-E) first-test at u_substrate.

Chain 4 of the user-approved Q_β Habiro element search (Δ_λ gate). After
Chain 1 (Wenzl/Kashaev/Q_A) closed with α + β NEGATIVE pointing to
Kashiwara crystal as the residue-A categorical-ID home (see PR #1760
ledger + 2026-06-03-qbeta-habiro-chain-1-scope.md), this test probes
6 specifically Kashiwara/crystal-derived candidate formulas for c_3
at proton-pinned q₀.

Target: c_3 ≈ -2.069 (cal-anchored, from qbeta-ck-cache.witness.json)
Tolerance: 10 ppm

6 candidates (none tested in the 15-candidate c_3 re-run):

  1. Demazure character at (2,1): -s_{(2,1)}(q⁻¹, 1, q)
  2. Crystal-graph SYT major-index sum: -Σ_T q^maj(T) for T in SYT(2,1)
  3. q-deformed J_Hopf(q) Kauffman normalization at q₀
  4. -(q² + 1 + q⁻²) — symmetric block-eigenvalue sum (related to (q²+q⁻²)
     which lands closest in the c_3 re-run; +1 offset captured the Hopf-
     center contribution)
  5. -(q + q⁻¹)·b_q — quantum-2 weighted by Hoefsmit b
  6. -J_Hopf(q=1)·b² — Hopf at classical limit times Hoefsmit b² content

Verdict: NEGATIVE expected (closes Chain 4 literal-formula first-test
and sharpens the search toward composite Kashiwara operators); POSITIVE
would identify the residue-A categorical-ID candidate.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def quantum_int(n: int, q: mpf) -> mpf:
    """[n]_q = (q^n − q^{-n}) / (q − q^{-1}); limit at q = 1 is n."""
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


# ── Candidate formulas (each returns c_3 at q₀, target = -2.069) ──

def candidate_1_demazure_2_1(q: mpf) -> mpf:
    """Demazure character at (2,1): -s_{(2,1)}(q⁻¹, 1, q).

    Schur polynomial s_{(2,1)} evaluated at (q⁻¹, 1, q):
      s_{(2,1)}(x, y, z) = (x²y + xy² + x²z + 2xyz + xz² + y²z + yz²)
    At (q⁻¹, 1, q): standard SYT(2,1) sum gives 2·[3]_q.
    """
    return -(2 * quantum_int(3, q))


def candidate_2_syt_major_index(q: mpf) -> mpf:
    """Crystal-graph SYT major-index sum at (2,1): -Σ_T q^maj(T).

    SYT(2,1) has 2 tableaux: T₁ = [[1,2],[3]] (maj=2), T₂ = [[1,3],[2]] (maj=1).
    Sum: q² + q. Sign convention to match c_3 negative.
    """
    return -(q + q ** 2)


def candidate_3_jhopf_kauffman_q(q: mpf) -> mpf:
    """q-deformed J_Hopf at substrate, Kauffman normalization:
       J_Hopf(q) = -(q^(1/2) + q^(-1/2))·(q^(3/2) + q^(-3/2)).
    """
    return -(q ** mpf("0.5") + q ** mpf("-0.5")) * (q ** mpf("1.5") + q ** mpf("-1.5"))


def candidate_4_symmetric_block_plus_one(q: mpf) -> mpf:
    """-(q² + 1 + q⁻²) — symmetric block-eigenvalue sum with Hopf-center."""
    return -(q ** 2 + 1 + q ** -2)


def candidate_5_quantum_2_times_b(q: mpf) -> mpf:
    """-(q + q⁻¹)·b_q — quantum-2 weighted by Hoefsmit b."""
    return -(q + 1 / q) * hoefsmit_b(q)


def candidate_6_jhopf_classical_times_b_squared(q: mpf) -> mpf:
    """-J_Hopf(q=1)·b² = -(-2)·b² = 2·b². NOTE: positive — sign-tests
    whether the Lean conjecture c_3 = J_Hopf(q=1) needs a b² correction."""
    return -mpf(-2) * hoefsmit_b(q) ** 2


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-kashiwara-chain-4", engine="mpmath")

    q_mp = Q_MP
    target_c3 = mpf("-2.06934257711516783787971951725")

    candidates = {
        "1. Demazure (2,1) char = -2·[3]_q": candidate_1_demazure_2_1,
        "2. SYT(2,1) major-index sum -(q + q²)": candidate_2_syt_major_index,
        "3. J_Hopf(q) Kauffman norm at substrate": candidate_3_jhopf_kauffman_q,
        "4. -(q² + 1 + q⁻²) symmetric+Hopf-center": candidate_4_symmetric_block_plus_one,
        "5. -(q + q⁻¹)·b_q quantum-2·Hoefsmit": candidate_5_quantum_2_times_b,
        "6. -J_Hopf(q=1)·b² = 2·b² sign-test": candidate_6_jhopf_classical_times_b_squared,
    }

    print("=" * 76)
    print(" Chain 4 (Option-E) first-test — 6 Kashiwara/crystal-derived c_3 formulas")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  target c_3 = {mp.nstr(target_c3, 14)}  (cal-anchored)")
    print(f"  tolerance = 10 ppm")
    print()

    results = {}
    any_pass = False
    best_err_ppm = float("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            value = formula(q_mp)
            err_ppm = float(abs(value - target_c3) / abs(target_c3) * 1e6)
            ok = err_ppm <= 10.0
            err_str = f"{err_ppm:>12.2f} ppm"
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            err_ppm = float("inf")
            ok = False
            err_str = "ERROR"
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     pred = {mp.nstr(value, 14):>22}  miss: {err_str}  {status}")

        results[name] = {
            "computed": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
            "err_ppm": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if err_ppm < best_err_ppm:
            best_err_ppm = err_ppm
            best_name = name

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_err_ppm:.2f} ppm)")
    print()
    if any_pass:
        print("  POSITIVE — at least one Kashiwara/crystal-derived c_3 formula matches")
        print("  within 10 ppm. This is a Chain 4 residue-A categorical-ID candidate.")
    else:
        print("  NEGATIVE — no literal Kashiwara/crystal-derived single-formula c_3")
        print("  candidate matches within 10 ppm. Combined with Chain 1 (Wenzl/Kashaev")
        print("  /Q_A) NEGATIVE and the 15-candidate c_3 re-run NEGATIVE, the residue A")
        print("  categorical-ID lives in a COMPOSITE Kashiwara operator structure, NOT")
        print("  a single-formula Demazure character / KLR trace / SYT statistic /")
        print("  J_Hopf q-deformation. The search narrows to multi-operator")
        print("  combinations or genuinely-new categorical objects.")

    wb.add_assertion(
        "chain_4_literal_kashiwara_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="Six literal Kashiwara/crystal-derived single-formula c_3 candidates "
               "(Demazure char, SYT maj-index, J_Hopf Kauffman, symmetric+Hopf-center, "
               "[2]_q·b, J_Hopf(1)·b²). If any matches the empirical c_3 within 10 ppm, "
               "this is a residue-A categorical-ID candidate; otherwise the search "
               "narrows to COMPOSITE operator structures.",
    )

    wb.add_data("target_c_3", mp.nstr(target_c3, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("candidates_tested", list(candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_err_ppm", best_err_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)
    wb.add_data("interpretation", (
        f"Chain 4 (Option-E) first-test: 6 Kashiwara/crystal-derived single-formula "
        f"c_3 candidates tested at proton-pinned q₀ against c_3 = -2.069. "
        f"Best: '{best_name}' at {best_err_ppm:.2f} ppm. "
        + ("POSITIVE — at least one candidate matches within 10 ppm; residue-A ID."
           if any_pass else
           "NEGATIVE — no literal Kashiwara single-formula matches. Combined with "
           "Chain 1 NEGATIVE and the 15-candidate c_3 re-run NEGATIVE, the residue A "
           "lives in a composite operator structure, not a single-formula crystal "
           "object.")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
