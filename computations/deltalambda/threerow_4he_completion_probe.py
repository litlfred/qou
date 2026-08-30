#!/usr/bin/env python3
"""threerow_4he_completion_probe.py — fill in the ⁴He (n=12) leg of the ≥3-row
sign-crossing object, and place its crossing on the A-ladder.

UNIT 1 of the bean qou-prjo follow-up to #4829.

#4829 left ⁴He as a "documented SANDBOX COMPUTE LIMIT (no mpfr Rust kernel)".
That diagnosis was an implementation artifact — see `threerow_chi_sparse.py`:
the dense `np.eye(dim)` in the #4829 `chi_atom` densified an already-sparse
CSR Hoefsmit operator and forced an O(dim³)-per-letter product.  Keeping the
identity sparse and accumulating the trace column-batch-wise makes the whole
ℓ≥3 stratum of 12 a seconds-to-a-minute computation in pure Python + scipy,
with NO native kernel and NO truncation.

Object (identical to #4829, no approximation, FULL ℓ≥3 sum — 70 partitions):

    F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3}  y_λ(q) · χ^λ(β_K; q) · Δ_λ

  * Δ_λ = (−1)^{n(λ)}·dim V_λ  — PROVED, value-only
    (`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`).
  * y_λ(q) — LIVE closed form `schur_principal_mpmath.y_lambda_at_q0_mpmath`
    (EXPERIMENTAL PROTON ANCHOR; NOT the muon-serving
    `wedderburn_jones_markov.y_lambda_at` cache — AGENTS.md straddle hazard).
  * χ^λ(β_K;q) — sparse-kernel Hecke character of the q-running color-weighted
    nuclide braid; layer-pure (word AND seminormal matrices at the SAME q).

NO TRUNCATION.  Every one of the 70 ℓ≥3 partitions of 12 is summed.  Per the
brief: a truncation to the dominant |Δ_λ| terms would only be admissible with a
rigorous bound on the neglected remainder; none is available, so none is taken.

Reported:
  1. the physical interval q ∈ (1, q₀]  — does ⁴He cross below the substrate?
  2. the BEYOND-SUBSTRATE DIAGNOSTIC RAY q ∈ (q₀, 4]  — ⚠ NOT a physical claim;
     it exists only to locate the zero of the analytic object, so ⁴He can be
     placed on the same A-ladder as n=6 and n=9 (UNIT 2).
  3. the per-λ decomposition at q₀ and either side of any crossing.

DISCIPLINE.  0 free parameters; AME never used (not even as a check here);
proton anchor recorded in the witness; scope-(a)/(b) honest.
"""
from __future__ import annotations

import json
import sys
import time
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),
    str(Path(__file__).resolve().parent.parent / "substrate"),
    str(Path(__file__).resolve().parent.parent / "hecke"),
]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from threerow_sign_crossing_probe import fmt_f64_limited  # noqa: E402
from threerow_chi_sparse import chi_atom_sparse, self_check  # noqa: E402
from threerow_sign_crossing_probe import delta_lambda, bisect_cross, Q0, Q_LO, ZN  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath, partitions_of  # noqa: E402
from _precision import set_compute_dps, str_at_true_precision  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

Q_RAY_MAX = mp.mpf("4.0")
N_PHYS = 11      # grid points on the physical interval (1, q₀]
N_RAY = 13       # grid points on the diagnostic ray (q₀, 4]

# Bisection budget. Each F evaluation at n=12 costs ~32 s, so iteration count is
# the dominant wall-clock term and must be chosen, not defaulted.
#
#   PHYSICAL crossing: bisected. 18 iterations on a bracket of width ~0.014 gives
#   ~5e-8 resolution — already far finer than the f64 character path warrants,
#   and the crossing location IS the reported quantity here.
#
#   DIAGNOSTIC ray crossings: NOT bisected. Their exact location is not
#   load-bearing (only which side of q₀ the FIRST crossing falls on matters), and
#   bisecting four of them at 30 iterations cost >60 min of wall clock on the
#   first run for digits nobody should quote. Brackets are reported instead —
#   cheaper AND more honest about the resolution actually available.
N_BISECT_PHYS = 18

COMP = Path(__file__).resolve().parent.parent

_LAM12 = None


# Chosen once and independent of the data: the convention-C value this probe
# recorded was O(1) (F(q0) = -5.9468...), while f64 chi noise on an O(1)
# product is ~1e-16.  A threshold below 1e-16 cannot be met by a genuinely
# non-vanishing object.  NOT tuned to the measurement.
F_ZERO_TOL_4HE = mp.mpf("1e-30")

def lam_l3(n: int) -> list[tuple[int, ...]]:
    return [lam for lam in partitions_of(n) if len(lam) >= 3]


_F_CACHE: dict[tuple[int, int, str], mp.mpf] = {}


def F_sparse(Z: int, N: int, q: mp.mpf, progress: str = "") -> mp.mpf:
    """FULL ℓ≥3 sum (no truncation) via the sparse character kernel. Memoized —
    each evaluation costs ~32 s at n=12, and the grid/bisection paths revisit
    endpoints."""
    ck = (Z, N, mp.nstr(q, 40))
    if ck in _F_CACHE:
        return _F_CACHE[ck]
    n = 3 * (Z + N)
    y = y_lambda_at_q0_mpmath(n, q)
    tot = mp.mpf(0)
    lams = lam_l3(n)
    t0 = time.time()
    for i, lam in enumerate(lams):
        tot += y[lam] * chi_atom_sparse(lam, Z, N, q) * delta_lambda(lam)
        if progress and (i + 1) % 20 == 0:
            el = time.time() - t0
            eta = el / (i + 1) * (len(lams) - i - 1)
            print(f"      {progress} λ {i+1}/{len(lams)}  elapsed {el:.0f}s  ETA {eta:.0f}s",
                  flush=True)
    _F_CACHE[ck] = tot
    return tot


def geom(lo: mp.mpf, hi: mp.mpf, npts: int) -> list[mp.mpf]:
    a, b = mp.log(lo - 1), mp.log(hi - 1)
    return [1 + mp.e ** (a + (b - a) * k / (npts - 1)) for k in range(npts)]


def validate_4he_chi() -> mp.mpf | None:
    """Cross-check χ^λ(β_4He;q₀) against the canonical atom-chi-rust-4he witness."""
    wf = COMP / "atom-chi-rust-4he.witness.json"
    if not wf.exists():
        return None
    ref = json.loads(wf.read_text())["data"]["atom"]["by_partition"]
    worst = mp.mpf(0)
    for e in ref:
        lam = tuple(e["partition"])
        r = mp.mpf(e["chi_lambda"])
        mine = chi_atom_sparse(lam, 2, 2, Q0)
        worst = max(worst, abs(mine - r) / (abs(r) + mp.mpf("1e-40")))
    return worst


def main() -> int:
    print("=" * 88)
    print(" UNIT 1 — ⁴He (n=12) ≥3-row signed trace: completing the #4829 table")
    print("=" * 88)
    print(f" q₀ (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")
    lams = lam_l3(12)
    print(f" ℓ≥3 stratum of 12: {len(lams)} partitions, FULL sum (no truncation)")

    # ── gate 0: sparse kernel ≡ #4829 dense kernel ─────────────────────────
    print("\n" + "─" * 88)
    print(" 0.  kernel gate — sparse χ vs the #4829 dense χ_atom (must be f64-identical)")
    print("─" * 88)
    kernel_rel = self_check()

    # ── gate 1: χ^λ(β_4He;q₀) vs the canonical rust witness ────────────────
    print("\n" + "─" * 88)
    print(" 1.  convention gate — χ^λ(β_4He;q₀) vs canonical atom-chi-rust-4he.witness.json")
    print("─" * 88)
    t0 = time.time()
    chi_rel = validate_4he_chi()
    if chi_rel is None:
        print("  (no atom-chi-rust-4he witness present — convention gate SKIPPED)")
    else:
        print(f"  max rel diff = {float(chi_rel):.3e}  "
              f"({'OK' if chi_rel < 1e-5 else 'FAIL'})   ({time.time()-t0:.0f}s)")

    # ── 2. physical interval ───────────────────────────────────────────────
    print("\n" + "─" * 88)
    print(" 2.  PHYSICAL interval  q ∈ (1, q₀]")
    print("─" * 88)
    Z, N = ZN["4He"]
    f = lambda q: F_sparse(Z, N, q)
    grid_p = geom(Q_LO, Q0, N_PHYS)
    vals_p = []
    t0 = time.time()
    for k, q in enumerate(grid_p):
        v = F_sparse(Z, N, q, progress=f"[4He {k+1}/{N_PHYS}]")
        vals_p.append(v)
        el = time.time() - t0
        print(f"   q={mp.nstr(q,10):14s} F={float(v):+.6e}   "
              f"({el:.0f}s elapsed, ETA {el/(k+1)*(N_PHYS-k-1):.0f}s)", flush=True)
    cross_p = []
    for i in range(len(grid_p) - 1):
        a, b = vals_p[i], vals_p[i + 1]
        if a != 0 and b != 0 and (a > 0) != (b > 0):
            cross_p.append(bisect_cross(f, grid_p[i], grid_p[i + 1], a, b,
                                        iters=N_BISECT_PHYS))
    print(f"\n   ⁴He  F(q_lo)={float(vals_p[0]):+.6e}   F(q₀)={float(vals_p[-1]):+.6e}"
          f"   sign {int(mp.sign(vals_p[0])):+d}→{int(mp.sign(vals_p[-1])):+d}")
    print(f"   crossings on (1,q₀] (PHYSICAL): "
          f"{[float(c) for c in cross_p] if cross_p else 'none'}")

    # ── 3. diagnostic ray ──────────────────────────────────────────────────
    print("\n" + "─" * 88)
    print(" 3.  DIAGNOSTIC RAY  q ∈ (q₀, 4]   ⚠ BEYOND-SUBSTRATE — NOT a physical claim")
    print("─" * 88)
    grid_r = geom(Q0 * mp.mpf("1.0000001"), Q_RAY_MAX, N_RAY)
    vals_r = []
    t0 = time.time()
    for k, q in enumerate(grid_r):
        v = F_sparse(Z, N, q)
        vals_r.append(v)
        el = time.time() - t0
        print(f"   q={mp.nstr(q,10):14s} F={float(v):+.6e}   "
              f"({el:.0f}s elapsed, ETA {el/(k+1)*(N_RAY-k-1):.0f}s)", flush=True)
    # Brackets, NOT bisected values — see the N_BISECT_PHYS note. The ray
    # crossing locations are not load-bearing; only which side of q₀ the FIRST
    # one falls on matters, and a bracket states that without implying digits the
    # f64 character path cannot support.
    seq_q = [vals_p[-1]] + vals_r
    seq_g = [Q0] + grid_r
    cross_r_brackets = []
    for i in range(len(seq_g) - 1):
        a, b = seq_q[i], seq_q[i + 1]
        if a != 0 and b != 0 and (a > 0) != (b > 0):
            cross_r_brackets.append([seq_g[i], seq_g[i + 1]])
    print(f"\n   sign changes on (q₀,4] (DIAGNOSTIC ONLY, reported as BRACKETS): "
          f"{[f'({float(lo):.4f},{float(hi):.4f})' for lo, hi in cross_r_brackets] if cross_r_brackets else 'none'}")

    # ── 4. per-λ decomposition at q₀ ───────────────────────────────────────
    print("\n" + "─" * 88)
    print(" 4.  per-λ decomposition of F_4He at q₀ (which ℓ≥3 block sets the sign)")
    print("─" * 88)
    y0 = y_lambda_at_q0_mpmath(12, Q0)
    rows = []
    for lam in lams:
        t = y0[lam] * chi_atom_sparse(lam, Z, N, Q0) * delta_lambda(lam)
        rows.append((lam, delta_lambda(lam), t))
    rows.sort(key=lambda r: -abs(r[2]))
    for lam, d, t in rows[:8]:
        print(f"     {str(lam):24s} Δ={d:+7d}  term={float(t):+.6e}")
    print(f"     {'TOTAL':24s} {'':>9}  term={float(vals_p[-1]):+.6e}")
    # cancellation ratio: |leading term| / |total| — how delicate is the sign?
    canc = abs(rows[0][2]) / (abs(vals_p[-1]) + mp.mpf("1e-300"))
    print(f"     leading/total magnitude ratio = {float(canc):.2f}×  "
          f"(f64 noise floor ≈ {float(abs(rows[0][2])*mp.mpf('2.2e-16')):.2e})")

    # ── verdict ────────────────────────────────────────────────────────────
    print("\n" + "=" * 88)
    print(" VERDICT (⁴He, n=12)")
    print(f"   sign on the PHYSICAL interval: {int(mp.sign(vals_p[0])):+d} → "
          f"{int(mp.sign(vals_p[-1])):+d}   crossings: "
          f"{[float(c) for c in cross_p] if cross_p else 'none'}")
    print(f"   first DIAGNOSTIC sign change above q₀ (bracket): "
          + (f"[{float(cross_r_brackets[0][0]):.6f}, "
             f"{float(cross_r_brackets[0][1]):.6f}]"
             if cross_r_brackets else "none on (q₀,4]"))
    print("   A-ladder (first crossing q):  n=6 ≈ 1.0537 [≤q₀] · n=9 ≈ 1.43–1.46 [>q₀] · "
          f"n=12 {'≈ %.5f [≤q₀]' % float(cross_p[0]) if cross_p else '— none ≤ q₀'}")
    print("=" * 88)

    # ── witness ────────────────────────────────────────────────────────────
    w = WitnessBuilder("threerow-4he-completion", engine="mpmath+f64-sparse-seminormal",
                       output_dir=Path(__file__).resolve().parent)
    w.set_description(
        "UNIT 1 of bean qou-prjo follow-up to #4829: completes the ⁴He (n=12) leg of "
        "F_K(q)=Σ_{λ⊢3A,ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ, which #4829 had recorded as a "
        "sandbox compute limit. No native kernel and no truncation were needed — the "
        "limit was an implementation artifact (a dense np.eye densifying the sparse "
        "CSR Hoefsmit operator, forcing O(dim³) per word letter). The sparse kernel "
        "(threerow_chi_sparse.py) is an EXACT reorganisation of the same f64 "
        "arithmetic, gated bit-level against the #4829 dense path. FULL ℓ≥3 sum over "
        "all 70 partitions of 12. Δ_λ=(−1)^{n(λ)}·dim (PROVED value-only); y_λ via "
        "live schur_principal_mpmath (EXPERIMENTAL PROTON ANCHOR, not the muon cache); "
        "layer-pure. 0 free parameters; AME not used."
    )
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.Q); live closed-form y_λ")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("n_partitions_l_ge_3", len(lams))
    w.add_parameter("truncation", "none — full ℓ≥3 sum over all 70 partitions of 12")
    w.add_parameter("chi_kernel", "sparse CSR Hoefsmit seminormal + batched-column trace "
                                  "(exact reorganisation of the #4829 dense path)")
    w.add_parameter("chi_precision", "f64 (no mpfr Rust kernel; precision class unchanged "
                                     "by the reorganisation)")
    w.add_data("kernel_gate_max_rel_vs_dense", fmt_f64_limited(kernel_rel))
    w.add_data("chi_vs_rust_witness_max_rel_at_q0",
               fmt_f64_limited(chi_rel) if chi_rel is not None else None)
    w.add_data("physical_interval", {
        # q_grid is a pure-mpmath geometric grid; F comes off the f64 χ kernel.
        "q_grid": [str_at_true_precision(q) for q in grid_p],
        "F_values": [fmt_f64_limited(v) for v in vals_p],
        "F_at_qlo": fmt_f64_limited(vals_p[0]),
        "F_at_q0": fmt_f64_limited(vals_p[-1]),
        "sign_qlo": int(mp.sign(vals_p[0])), "sign_q0": int(mp.sign(vals_p[-1])),
        "crossings": [fmt_f64_limited(c) for c in cross_p],
    })
    w.add_data("diagnostic_ray_above_q0", {
        "q_grid": [str_at_true_precision(q) for q in grid_r],
        "F_values": [fmt_f64_limited(v) for v in vals_r],
        "sign_change_brackets": [[str_at_true_precision(lo),
                                  str_at_true_precision(hi)]
                                 for lo, hi in cross_r_brackets],
        "first_sign_change_bracket":
            [str_at_true_precision(cross_r_brackets[0][0]),
             str_at_true_precision(cross_r_brackets[0][1])]
            if cross_r_brackets else None,
        "n_sign_changes": len(cross_r_brackets),
        "bisected": False,
        "why_not_bisected": (
            "The ray crossing LOCATIONS are not load-bearing — only which side of "
            "q₀ the first sign change falls on matters. Bisecting them at n=12 "
            "(~32 s per F evaluation) cost >60 min of wall clock on the first run "
            "for digits the f64 character path cannot support anyway. Brackets are "
            "reported instead: cheaper, and honest about the available resolution."
        ),
        "ray_max_q": str_at_true_precision(Q_RAY_MAX),
    })
    w.add_data("per_partition_at_q0_top8", [
        {"partition": list(l), "delta": int(d), "term": fmt_f64_limited(t)}
        for l, d, t in rows[:8]])
    w.add_data("leading_over_total_ratio_at_q0", fmt_f64_limited(canc))
    w.add_assertion("kernel_matches_dense_path", 1 if kernel_rel < 1e-12 else 0, 1)
    if chi_rel is not None:
        w.add_assertion("chi_convention_matches_rust_witness",
                        1 if chi_rel < 1e-5 else 0, 1)
    # These two stood here as
    #     w.add_assertion("4He_sign_at_q0",  int(mp.sign(vals_p[-1])), int(mp.sign(vals_p[-1])))
    #     w.add_assertion("4He_sign_at_qlo", int(mp.sign(vals_p[0])),  int(mp.sign(vals_p[0])))
    # i.e. `x == x` — tautologies that could never fail.  Between conventions C and D
    # the object went from F(q0) = -5.9468... to identically zero and the sign went
    # -1 -> 0, and both still reported passed.  A sign is a MEASUREMENT: it is
    # recorded via add_data below, which is what recording is for.
    _max_abs_F = max(abs(v) for v in vals_p)
    w.add_assertion("three_row_object_is_structural_zero",
                    1 if _max_abs_F < F_ZERO_TOL_4HE else 0, 1)
    w.add_data("4He_sign_at_q0_measured", int(mp.sign(vals_p[-1])))
    w.add_data("4He_sign_at_qlo_measured", int(mp.sign(vals_p[0])))
    w.add_data("4He_max_abs_F_on_grid", fmt_f64_limited(_max_abs_F))
    w.add_caveat(
        "BEYOND-SUBSTRATE DIAGNOSTIC. The 'diagnostic_ray_above_q0' block reports F at "
        "q > q₀ ≈ 1.10998 (experimental proton anchor). That is NOT a physical regime "
        "and no value on the ray is a prediction; the ray exists only to locate the "
        "zero of the analytic object so ⁴He can be placed on the same A-ladder as n=6 "
        "and n=9."
    )
    w.add_caveat(
        "NO TRUNCATION was applied: all 70 ℓ≥3 partitions of 12 are summed. A "
        "dominant-|Δ_λ| truncation was considered and REJECTED — no rigorous bound on "
        "the neglected remainder is available, and an unbounded truncation would not "
        "be a result."
    )
    w.add_caveat(
        "χ^λ is f64 (pure-Python Hoefsmit seminormal; no mpfr kernel in this sandbox). "
        "The sparse reorganisation changes the COST, not the precision class; it is "
        "gated bit-level against the #4829 dense path (max rel diff ~1e-15). Sign "
        "conclusions are reported together with the leading/total cancellation ratio "
        "so the reader can see how far the total sits above the f64 noise floor."
    )
    w.add_caveat(
        "value_only object: F_K is NOT a binding energy (Δ_λ is value-only). Only the "
        "SIGN structure of the ≥3-row trace weighting is tested here. The extensive "
        "super-pairwise magnitude term remains OPEN (bean qou-prjo)."
    )
    w.save()
    print("\nwitness -> threerow-4he-completion.witness.json")
    ok = kernel_rel < 1e-12 and (chi_rel is None or chi_rel < 1e-5)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
