#!/usr/bin/env python3
"""threerow_isospin_parity_probe.py — the controlled test cannot discriminate under D.

REPAIRED 2026-08-25 (bean `qou-iav7`).  The probe was UNFINISHABLE and, where it did
run, would have produced an isospin verdict computed from round-off.  What it argues
is kept; what it measured is not, because the object it measured is identically zero.

WHAT IT ASKS.  Does the >=3-row sign crossing depend on ISOSPIN (Z=N vs Z!=N), or only
on the strand count n = 3A?  The A-ladder {D,T,3He,4He} cannot say, because there
isospin and strand count move together (Z=N <=> A even <=> n in {6,12,18}).  So it
holds n FIXED and varies only (Z,N):

      n =  6 :  D(1,1)   [Z=N]  vs  pp(2,0), nn(0,2)  [Z!=N]
      n = 12 :  4He(2,2) [Z=N]  vs  4Li(3,1), 4H(1,3) [Z!=N]

That design is sound and is kept.  pp, nn, 4Li, 4H are COMBINATORIAL probes, not bound
nuclides; no physical claim is made about them and AME is never consulted.

WHY IT CANNOT ANSWER, UNDER CONVENTION D
-----------------------------------------
`F_iso` sums only over `len(lam) >= min_rows` (default 3).  Convention D pins the Wenzl
level at r = 2, so `y_lam = 0` for every partition with three or more rows
(`schurPrincipal_eq_zero_iff`, `wenzlLevel_conventionD`, both sorry-free).  The object
being scanned is therefore identically zero **for every (Z,N)** — 7 of 11 partitions at
n = 6, and 70 of 77 at n = 12, are weight-zero.  The test returns the same answer for
every isospin class because it returns nothing at all.

Measured here at n = 6, the whole controlled test in 0.6 s:

      case   (Z,N)   class     F(1.001)     F(1.05)      F(q0)      F(1.2)       F(2)
      D      (1,1)   Z=N       0.0          0.0          0.0        7.42e-51     1.88e-46
      pp     (2,0)   Z!=N      0.0          0.0          0.0        4.60e-51     2.12e-46
      nn     (0,2)   Z!=N      0.0          0.0          0.0        7.41e-51     1.57e-46

THE TRAP, AND IT IS THIS PROBE'S DESIGN THAT CREATES IT.  The residuals above are
round-off, and they are **(Z,N)-DEPENDENT** — the braid word is by construction the only
thing that varies, so the noise is exactly what varies with isospin.  Nor is it stable:
at q = 1.2 the order is D ~ nn > pp, and by q = 2 it has inverted to pp > D > nn.  A
bisect-on-sign-change over that produces isospin-CORRELATED crossings that are pure
artifact, and the old verdict logic

      predicted = (isospin_class == "Z=N");  observed = crosses_below_q0
      holds = all(predicted == observed)

would have reported them as a surviving pattern.  A well-designed control over a null
object manufactures precisely the correlation it was built to test for.

THE n=12 LEG IS NOT RUN, AND DOES NOT NEED TO BE.  Measured: 54.5 s for ONE grid point
(4He at q0), so the old 26-point x 3-case sweep is ~71 minutes — which is why this probe
never reached its own `w.save()` and why no witness of it has ever existed.  But its
answer is already known: the vanishing is proved for ALL n, so no amount of compute can
return anything but zero.  The unfinishable leg is unnecessary, not merely expensive.

WHAT IS DROPPED.  The convention-C branch geometry: `U_STAR`, `Q_STAR = 1.27844957658`
(root of -u^6-u^4+u^3+u^2+1), the "real-level branch (1,q*)" and the "diagnostic ray
(q*,4]".  Under D, `Q^r = Q^2` is entire — verified here at q* itself — so there is no
pole, the level is the constant 2, and q* is an ordinary point.  The file previously
hardcoded C for the branch while calling `_wenzl_constants` (D) for the level: the same
straddle `qou-qdtk` documents in `threerow_qcross_trend_probe`, independently written.

WHAT SURVIVES, AND IS RE-VERIFIED HERE
---------------------------------------
  * THE CONFOUND.  Combinatorial, convention-independent: in {D,T,3He,4He,6Li,7Li},
    Z=N <=> A even, so the A-ladder cannot separate isospin from strand count.
  * THE COST LAW.  `Sum_{lam|-n} (dim V_lam)^2 = n!` exactly — a hard bound from an
    identity, not a sandbox limitation.  6Li (n=18) and 7Li (n=21) are out of reach by
    orders of magnitude whatever the convention.  NOTE: the per-point baseline is now
    the MEASURED 54.5 s at n=12, not the 32.0 s previously hardcoded; the old table
    understated every projection by ~1.7x.
  * THE INTERFACE CENSUS.  `word_composition` reads the braid word itself, not the
    weights, so it is unaffected by the vanishing.

SCOPE.  Scope-(a), about this probe.  Nothing here refutes the isospin question, which
remains open and un-probed; the finding is that THIS instrument cannot address it,
because its discriminating object carries no weight in the canonical convention.  A
probe that could would have to be built on an object D does not annihilate.

Measurement only.  Nothing is fitted, nothing is wired, AME is never used.
"""
from __future__ import annotations

import os, sys, math, time, warnings
from pathlib import Path

for _p in ("/home/user/qou/computations", "/home/user/qou/computations/substrate",
           "/home/user/qou/computations/hecke", "/home/user/qou/computations/deltalambda"):
    if _p not in sys.path:
        sys.path.insert(0, _p)
sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate"),
                str(Path(__file__).resolve().parent.parent / "hecke")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from collections import Counter  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    partitions_of, _f_lambda, schur_principal_mpmath, _wenzl_constants)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from threerow_chi_sparse import chi_atom_sparse  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

Q0 = mp.mpf(Q_50_DIGIT_STR)

# Convention C's pole, kept ONLY to show the live level function is regular where C had
# one. It bounds no sweep and enters no result. Under D, Q^r = Q^2 is entire.
_U_STAR_C = mp.findroot(lambda u: -u**6 - u**4 + u**3 + u**2 + 1, mp.mpf("1.13"))
Q_STAR_C = _U_STAR_C ** 2

# Null tolerance, chosen once and justified rather than fitted: the convention-C values
# this family recorded were O(1) (|F(q0)| ran 0.19 to 5.9 in the sibling probes), while
# f64 chi noise on an O(1) product is ~1e-16. A threshold below 1e-16 therefore cannot
# be met by a genuinely non-vanishing object.
F_NULL_TOL = mp.mpf("1e-30")

# MEASURED on this container: one grid point of the n=12 leg (4He at q0) took 54.5 s.
# The previous table hardcoded 32.0 and understated every projection by ~1.7x.
SEC_PER_POINT_N12_MEASURED = 54.5
OUTDIR = Path(os.environ.get("QOU_OUTDIR", str(Path(__file__).resolve().parent)))

# (label, Z, N, isospin class)
CASES_N6 = [("D", 1, 1, "Z=N"), ("pp", 2, 0, "Z!=N"), ("nn", 0, 2, "Z!=N")]
CASES_N12 = [("4He", 2, 2, "Z=N"), ("4Li", 3, 1, "Z!=N"), ("4H", 1, 3, "Z!=N")]


def delta_lambda(lam) -> int:
    conj = tuple(sum(1 for p in lam if p > i) for i in range(lam[0])) if lam else ()
    return math.prod((-1) ** (p * (p - 1) // 2) for p in conj) * _f_lambda(tuple(lam))


def F_iso(Z, N, q, min_rows=3):
    """F_K(q) = Σ_{ℓ≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ, y_λ via the closed-form normaliser."""
    n = 3 * (Z + N)
    Q, QR = _wenzl_constants(q)
    pref = ((1 - Q) / (1 - QR)) ** n          # = 1/Z(q), dual-Cauchy closed form
    tot = mp.mpf(0)
    for lam in partitions_of(n):
        if len(lam) < min_rows:
            continue
        tot += schur_principal_mpmath(lam, q) * pref * chi_atom_sparse(lam, Z, N, q) \
            * delta_lambda(lam)
    return tot


# bisect() and scan() were removed with the crossing sweep. They bisected on a sign
# change of an object that is identically zero under D, so every crossing they located
# was a round-off sign flip -- and, because the braid word is the only varying input,
# an isospin-correlated one. See the module docstring and the witness caveat.


def word_composition(Z, N, q):
    """Interface-type census of the braid word — the candidate structural mechanism.

    `atom_braid_word_3A` builds p-p interfaces from σ, n-n from σ⁻¹, and p-n from the
    color-weighted average, so a Z≠N excess is visible as an imbalance here."""
    w = atom_braid_word_3A(Z, N, include_inter=True, q=q)
    sig = Counter((round(float(c), 9), round(float(d), 9)) for c, d, g in w)
    return {"word_length": len(w),
            "distinct_interface_types": len(sig),
            "census": {f"c={k[0]},d={k[1]}": v for k, v in sorted(sig.items())}}


def main() -> int:
    T0 = time.time()
    print("=" * 92)
    print(" ISOSPIN PARITY, CONTROLLED AT FIXED n — what this instrument can still answer")
    print("=" * 92)
    print(f" q0 = {mp.nstr(Q0, 20)} (experimental proton anchor)")
    Q, QR = _wenzl_constants(Q0)
    entire = abs(QR - Q ** 2) < mp.mpf("1e-40")
    print(f" live Q^r = {mp.nstr(QR, 18)}   Q^2 = {mp.nstr(Q ** 2, 18)}   equal: {entire}")
    print(" => convention D: the Wenzl level is the constant 2, Q^r = Q^2 is entire, so")
    print(f"    there is no pole. C's q* = {mp.nstr(Q_STAR_C, 12)} is an ordinary point here,")
    print("    and the old 'real-level branch' / 'diagnostic ray' split does not exist.")

    # ── 0. the exact cost law (convention-independent) ─────────────────────
    print("\n" + "─" * 92)
    print(" 0. COST LAW  Sum_{lam|-n} dim^2 = n!   (a hard bound from an identity)")
    print("─" * 92)
    base = sum(_f_lambda(l) ** 2 for l in partitions_of(12) if len(l) >= 3)
    cost = {}
    for n in (6, 9, 12, 15, 18, 21):
        # Sum dim^2 and n! are EXACT INTEGERS -- keep them so. float(21!) discards
        # precision for nothing, and the raw-float64 ratchet is right to refuse it.
        # The ratio and the projection are mpf, carried from the exact integers.
        sdim = sum(_f_lambda(l) ** 2 for l in partitions_of(n) if len(l) >= 3)
        nfact = math.factorial(n)
        ratio = mp.mpf(sdim) / mp.mpf(base)
        secs = mp.mpf(str(SEC_PER_POINT_N12_MEASURED)) * ratio
        cost[str(n)] = {"sum_dim_squared_l_ge_3": int(sdim),
                        "n_factorial": int(nfact),
                        "cost_ratio_vs_n12": mp.nstr(ratio, 12),
                        "projected_sec_per_grid_point": mp.nstr(secs, 12)}
        yrs = secs / mp.mpf("3.15576e7")
        print(f"   n={n:2d}  Sum dim^2={mp.nstr(mp.mpf(sdim), 6):>12}  n!={mp.nstr(mp.mpf(nfact), 6):>12}  "
              f"x n12={mp.nstr(ratio, 4):>10}  => {mp.nstr(secs, 4)} s/pt"
              + (f" = {mp.nstr(yrs, 3)} yr" if yrs > 1 else ""))
    print(f"   baseline: {SEC_PER_POINT_N12_MEASURED} s/pt at n=12, MEASURED here")
    print("   (the previous table hardcoded 32.0 s/pt and understated every row by ~1.7x)")
    print("   => 6Li (n=18) and 7Li (n=21) are out of reach whatever the convention.")

    # ── 1. the confound (convention-independent) ───────────────────────────
    print("\n" + "─" * 92)
    print(" 1. WHY THE A-LADDER CANNOT DECIDE IT — isospin and n are confounded there")
    print("─" * 92)
    ladder = []
    for nm, Z, N in (("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
                     ("6Li", 3, 3), ("7Li", 3, 4)):
        even = (Z + N) % 2 == 0
        ladder.append({"iso": nm, "Z": Z, "N": N, "A": Z + N, "n": 3 * (Z + N),
                       "isospin_class": "Z=N" if Z == N else "Z!=N", "A_even": even})
        print(f"   {nm:5s} (Z,N)=({Z},{N})  A={Z+N}  n={3*(Z+N):2d}  "
              f"{'Z=N ' if Z == N else 'Z!=N'}  A {'even' if even else 'odd '}")
    confound = all((r["isospin_class"] == "Z=N") == r["A_even"] for r in ladder)
    print(f"   => Z=N <=> A even holds across all six: {confound}. Adding isotopes preserves it.")

    # ── 2. the controlled test at n=6 — 0.6s, and it cannot discriminate ───
    print("\n" + "─" * 92)
    print(" 2. CONTROLLED at FIXED n=6 — only (Z,N) varies. Is there any signal to compare?")
    print("─" * 92)
    QS = [mp.mpf("1.001"), mp.mpf("1.05"), Q0, mp.mpf("1.2"), Q_STAR_C, mp.mpf("2.0")]
    print(f"   {'case':>6} {'Z,N':>7} {'class':>6} " +
          " ".join(f"{('F(%.4g)' % float(q)):>13}" for q in QS))
    results, all_below_floor = {}, True
    for nm, Z, N, cls in CASES_N6:
        vals = [F_iso(Z, N, q) for q in QS]
        mx = max(abs(v) for v in vals)
        if mx >= F_NULL_TOL:
            all_below_floor = False
        results[nm] = {
            "Z": Z, "N": N, "isospin_class": cls, "n_strands": 3 * (Z + N),
            "F_by_q": {mp.nstr(q, 8): mp.nstr(v, 12) for q, v in zip(QS, vals)},
            "max_abs_F": mp.nstr(mx, 12),
            "below_null_tolerance": bool(mx < F_NULL_TOL),
            "word": word_composition(Z, N, Q0),
        }
        print(f"   {nm:>6} {f'({Z},{N})':>7} {cls:>6} " +
              " ".join(f"{float(v):>13.5e}" for v in vals))
    print(f"\n   every |F| below the null tolerance {mp.nstr(F_NULL_TOL, 3)}: {all_below_floor}")
    print("   The object is a STRUCTURAL ZERO for every (Z,N): F_iso sums only l(lam) >= 3,")
    print("   and convention D gives y_lam = 0 there for all n (schurPrincipal_eq_zero_iff).")
    print("   So the control returns the same answer for every isospin class — no signal.")

    # ── 2b. why a crossing scan over this is actively misleading ───────────
    print("\n" + "─" * 92)
    print(" 2b. THE TRAP: the residual round-off is (Z,N)-DEPENDENT and not stable in q")
    print("─" * 92)
    order_rows = []
    for q in (mp.mpf("1.2"), mp.mpf("2.0")):
        ordering = sorted(((abs(F_iso(Z, N, q)), nm) for nm, Z, N, _ in CASES_N6),
                          reverse=True)
        names = [nm for _, nm in ordering]
        order_rows.append({"q": mp.nstr(q, 8), "descending_by_abs_F": names})
        print(f"   q={float(q):.3f}: |F| descending = {' > '.join(names)}")
    unstable = order_rows[0]["descending_by_abs_F"] != order_rows[-1]["descending_by_abs_F"]
    print(f"   ordering changes between these q: {unstable}")
    print("   This probe's own design makes the braid word the ONLY thing that varies, so")
    print("   the NOISE is exactly what varies with isospin. A bisect-on-sign-change over")
    print("   it yields isospin-correlated 'crossings' that are pure artifact — which the")
    print("   old verdict (predicted == observed over crosses_below_q0) would have reported")
    print("   as a surviving pattern. A good control over a null object manufactures the")
    print("   very correlation it was built to test.")

    # ── 3. the n=12 leg: not run, and not needed ───────────────────────────
    print("\n" + "─" * 92)
    print(" 3. THE n=12 LEG IS NOT RUN — and does not need to be")
    print("─" * 92)
    n12_sec = mp.mpf(str(SEC_PER_POINT_N12_MEASURED)) * 26 * len(CASES_N12)
    print(f"   measured {SEC_PER_POINT_N12_MEASURED} s for ONE grid point (4He at q0);")
    print(f"   the old 26-point x {len(CASES_N12)}-case sweep is ~{mp.nstr(n12_sec/60, 3)} min.")
    print("   That is why the pre-2026-08-25 version never reached its own w.save(). Its")
    print("   answer is already known without that leg: the vanishing")
    print("   is proved for ALL n, so no amount of compute returns anything but zero.")
    for n in (6, 12):
        parts = partitions_of(n)
        ge3 = [l for l in parts if len(l) >= 3]
        print(f"   n={n:>3}: {len(ge3)} of {len(parts)} partitions have l>=3 — all weight-zero under D")

    print("\n" + "=" * 92)
    print(" The isospin question is NOT answered, and NOT refuted. This instrument cannot")
    print(" address it: its discriminating object carries no weight in the canonical")
    print(" convention. A probe that could must be built on an object D does not annihilate.")
    print("=" * 92)
    print(f" TOTAL WALL {time.time()-T0:.1f}s")

    w = WitnessBuilder("threerow-isospin-parity", engine="mpmath50+f64-seminormal-sparse",
                       output_dir=OUTDIR)
    w.add_assertion("wenzl_level_is_constant_two", 1 if entire else 0, 1)
    w.add_assertion("controlled_object_is_structural_zero", 1 if all_below_floor else 0, 1)
    w.add_assertion("residual_ordering_is_unstable_in_q", 1 if unstable else 0, 1)
    w.add_assertion("a_ladder_confound_holds", 1 if confound else 0, 1)
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("wenzl_level_r", "2 (convention D)")
    w.add_parameter("q_star_conventionC_pole", mp.nstr(Q_STAR_C, 30))
    w.add_parameter("null_tolerance", mp.nstr(F_NULL_TOL, 6))
    w.add_parameter("sec_per_grid_point_n12_measured", str(SEC_PER_POINT_N12_MEASURED))
    w.add_parameter("chi_precision", "f64 Hoefsmit seminormal (sparse kernel)")
    w.add_data("cost_law_sum_dim_squared_equals_n_factorial", cost)
    w.add_data("a_ladder_confound", ladder)
    w.add_data("controlled_results_n6", results)
    w.add_data("residual_ordering_by_q", order_rows)
    w.add_data("n12_leg_not_run", {
        "reason": "answer is proved for all n; the sweep is ~%s min and returns zero"
                  % mp.nstr(n12_sec / 60, 4),
        "measured_sec_per_grid_point": str(SEC_PER_POINT_N12_MEASURED),
        "projected_sweep_sec": mp.nstr(n12_sec, 12),
        "cases": [c[0] for c in CASES_N12],
    })
    w.add_caveat(
        "THIS PROBE CANNOT ANSWER ITS OWN QUESTION UNDER CONVENTION D. F_iso sums only "
        "l(lam) >= 3, where y_lam = 0 for all n (schurPrincipal_eq_zero_iff, "
        "wenzlLevel_conventionD). The controlled test returns the same answer for every "
        "isospin class because it returns nothing at all. The isospin question is neither "
        "answered nor refuted here — scope-(a), about this instrument."
    )
    w.add_caveat(
        "DO NOT RE-ENABLE A CROSSING SCAN ON THIS OBJECT. The residual is round-off, it is "
        "(Z,N)-dependent because the braid word is by design the only varying input, and "
        "its ordering is not stable in q. A bisect-on-sign-change produces isospin-"
        "correlated crossings that are artifact, and the previous verdict logic would have "
        "reported them as a surviving pattern."
    )
    w.add_caveat(
        "pp(2,0), nn(0,2), 4Li(3,1), 4H(1,3) are COMBINATORIAL PROBES of the braid word, "
        "NOT bound nuclides — the diproton/dineutron are unbound and 4H/4Li are unbound "
        "resonances. They are used only because atom_braid_word_3A(Z,N) is defined for any "
        "(Z,N). No physical prediction is made about them and AME is never consulted."
    )
    w.add_caveat(
        "THE CONFOUND AND THE COST LAW ARE CONVENTION-INDEPENDENT AND SURVIVE. In "
        "{D,T,3He,4He,6Li,7Li} isospin and strand count move together (Z=N <=> A even), so "
        "the A-ladder cannot separate them however many isotopes are added; and "
        "Sum_lam dim^2 = n! puts 6Li/7Li out of reach by orders of magnitude. Both stand "
        "whatever happens to the sign question."
    )
    w.save()
    print(f"witness -> {OUTDIR}/threerow-isospin-parity.witness.json")
    return 0 if (entire and all_below_floor and confound) else 1


if __name__ == "__main__":
    raise SystemExit(main())
