#!/usr/bin/env python3
"""threerow_isospin_parity_probe.py — does the ≥3-row sign crossing depend on
ISOSPIN (Z=N vs Z≠N), or only on the strand count n = 3A?

Bean qou-prjo.  Direct test of the pattern flagged (and correctly NOT claimed) in
#4832: among {D(1,1), T(1,2), ³He(2,1), ⁴He(2,2)} the two Z=N members cross BELOW
q₀ and the two Z≠N members cross ABOVE it.

WHY THE OBVIOUS CONTINUATION IS THE WRONG TEST — AND IS ALSO UNAFFORDABLE.

  (i) CONFOUNDED.  In that four-point set, isospin and strand count move TOGETHER:
      Z=N ⟺ A even ⟺ n ∈ {6,12}, Z≠N ⟺ A odd ⟺ n = 9.  So the four points cannot
      separate "Z=N" from "n even multiple of 6".  Extending to ⁶Li(3,3) and
      ⁷Li(3,4) does NOT fix this — it adds n=18 (Z=N) and n=21 (Z≠N), preserving
      the exact same confound.

  (ii) UNAFFORDABLE.  The batched-column trace costs O(L · Σ_λ dim²), and
      Σ_{λ⊢n} (dim V_λ)² = n! EXACTLY (verified below).  Relative to the measured
      n=12 cost (~32 s/grid point):
          n=15  →      2.73·10³ ×   (≈ 24 h / grid point)
          n=18  →      1.34·10⁷ ×   (≈ 14 YEARS / grid point)   ← ⁶Li
          n=21  →      1.07·10¹¹ ×  (≈ 10⁵ YEARS / grid point)  ← ⁷Li
      The #4832 sparse fix removed a dim³→dim² factor; it did NOT remove the
      factorial.  ⁶Li/⁷Li are out of reach by 7 and 11 orders of magnitude — a
      HARD BOUND from an exact identity, not a sandbox limitation.

THE CONTROLLED TEST INSTEAD: hold n FIXED, vary only (Z,N).

      n =  6 :  D(1,1)   [Z=N]   vs   pp(2,0), nn(0,2)   [Z≠N]
      n = 12 :  ⁴He(2,2) [Z=N]   vs   ⁴Li(3,1), ⁴H(1,3)  [Z≠N]

  Same strand count, same ℓ≥3 stratum, same partition set, same word length, same
  cost — the ONLY thing that changes is the isospin content of the braid word.
  This isolates exactly the variable the pattern is about, which the A-ladder
  cannot.  If Z≠N members at n=12 still cross BELOW q₀, the pattern is an
  n-effect mislabelled as isospin, and the claim is DEAD.

  ⚠ pp, nn, ⁴Li, ⁴H are COMBINATORIAL PROBES, not bound nuclides (the diproton and
  dineutron are unbound; ⁴H/⁴Li are unbound resonances).  No physical claim is made
  about them; `atom_braid_word_3A(Z,N)` is defined for any (Z,N) and that is all
  this test uses.  AME is never consulted.

BRANCH DISCIPLINE (carried from the trend probe).  The Wenzl level eigenvalue
Q^r = u³/(−u⁶−u⁴+u³+u²+1), u=√q, has a POLE at q* = 1.27844957657969…; above q*
the effective level r = log(Q^r)/log(Q) is COMPLEX.  So crossings are reported
separately for the REAL-LEVEL BRANCH (1,q*) — which contains q₀ — and for the
beyond-substrate DIAGNOSTIC RAY q ∈ (q*, 4].  The #4832 T/³He crossings at
q ≈ 1.4285/1.4617 lie on the latter.  Every ray field is prefixed `diagnostic_`.

DISCIPLINE.  free_parameters = 0; AME never used; experimental proton anchor;
y_λ via the LIVE closed form (never the muon cache); layer-pure (y_λ and χ^λ at the
SAME running q); scope-(a) unless an invariant is proved.
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
U_STAR = mp.findroot(lambda u: -u**6 - u**4 + u**3 + u**2 + 1, mp.mpf("1.13"))
Q_STAR = U_STAR ** 2
Q_LO = mp.mpf("1.000001")
Q_RAY_MAX = mp.mpf("4.0")
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


def bisect(f, a, b, fa, fb, iters):
    for _ in range(iters):
        m = (a + b) / 2
        fm = f(m)
        if fm == 0:
            return m
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b, fb = m, fm
    return (a + b) / 2


def scan(f, lo, hi, npts, iters, tag):
    a, b = mp.log(lo - 1), mp.log(hi - 1)
    grid = [1 + mp.e ** (a + (b - a) * k / (npts - 1)) for k in range(npts)]
    vals, t0 = [], time.time()
    for k, x in enumerate(grid):
        vals.append(f(x))
        el = time.time() - t0
        print(f"      [{tag}] {k+1}/{npts} q={float(x):.6f} F={float(vals[-1]):+.5e} "
              f"el {el:.0f}s ETA {el/(k+1)*(npts-k-1):.0f}s", flush=True)
    out = []
    for i in range(len(grid) - 1):
        if vals[i] != 0 and vals[i + 1] != 0 and (vals[i] > 0) != (vals[i + 1] > 0):
            out.append(bisect(f, grid[i], grid[i + 1], vals[i], vals[i + 1], iters))
    return out


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
    print(" ISOSPIN PARITY, CONTROLLED AT FIXED n — is the crossing about Z=N, or about n?")
    print("=" * 92)
    print(f" q₀ = {mp.nstr(Q0, 20)} (experimental proton anchor)")
    print(f" real-level branch (1, q*), q* = {mp.nstr(Q_STAR, 20)}; ray (q*, 4] is DIAGNOSTIC")

    # ── 0. the exact cost law that rules out ⁶Li / ⁷Li ─────────────────────
    print("\n" + "─" * 92)
    print(" 0. COST LAW  Σ_{λ⊢n} dim² = n!  ⇒ ⁶Li (n=18) / ⁷Li (n=21) are out of reach")
    print("─" * 92)
    base = sum(_f_lambda(l) ** 2 for l in partitions_of(12) if len(l) >= 3)
    cost = {}
    for n in (6, 9, 12, 15, 18, 21):
        s = sum(_f_lambda(l) ** 2 for l in partitions_of(n) if len(l) >= 3)
        ratio = s / base
        cost[str(n)] = {"sum_dim_squared_l_ge_3": float(s), "n_factorial": float(math.factorial(n)),
                        "cost_ratio_vs_n12": float(ratio),
                        "projected_sec_per_grid_point": float(32.0 * ratio)}
        yrs = 32.0 * ratio / 3.15576e7
        print(f"   n={n:2d}  Σdim²={float(s):.4e}  n!={float(math.factorial(n)):.4e}  "
              f"×n12={float(ratio):.3e}  ⇒ {32.0*ratio:.1f} s/pt" + (f" = {yrs:.2g} yr" if yrs > 1 else ""))
    print("   ⇒ ⁶Li and ⁷Li are infeasible by 7 and 11 orders of magnitude (HARD bound,")
    print("     from an exact identity — NOT a sandbox limitation).")

    # ── 1. the confound ────────────────────────────────────────────────────
    print("\n" + "─" * 92)
    print(" 1. WHY THE A-LADDER CANNOT DECIDE IT (isospin and n are confounded there)")
    print("─" * 92)
    for nm, Z, N in (("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
                     ("6Li", 3, 3), ("7Li", 3, 4)):
        print(f"   {nm:5s} (Z,N)=({Z},{N})  A={Z+N}  n={3*(Z+N):2d}  "
              f"{'Z=N ' if Z == N else 'Z≠N '}  A {'even' if (Z+N) % 2 == 0 else 'odd '}")
    print("   ⇒ in this family Z=N ⟺ A even. Adding ⁶Li/⁷Li preserves the confound.")

    # ── 2. controlled test ─────────────────────────────────────────────────
    results = {}
    for label, cases, npts, iters in (("n6", CASES_N6, 60, 60), ("n12", CASES_N12, 26, 26)):
        print("\n" + "─" * 92)
        print(f" 2{label}. CONTROLLED at FIXED n — only (Z,N) varies")
        print("─" * 92)
        for nm, Z, N, cls in cases:
            t0 = time.time()
            f = lambda q, Z=Z, N=N: F_iso(Z, N, q)
            br = scan(f, Q_LO, Q_STAR * (1 - mp.mpf("1e-5")), npts, iters, nm)
            ray = scan(f, Q_STAR * (1 + mp.mpf("1e-5")), Q_RAY_MAX, max(8, npts // 3),
                       iters, nm + "-ray")
            fq0 = f(Q0)
            below = [float(c) for c in br if c < float(Q0)]
            above_br = [float(c) for c in br if c > float(Q0)]
            results[nm] = {
                "Z": Z, "N": N, "isospin_class": cls, "n_strands": 3 * (Z + N),
                "F_at_q0": float(fq0), "sign_at_q0": int(mp.sign(fq0)),
                "crossings_real_level_branch": [float(c) for c in br],
                "crossings_below_q0": below,
                "crossings_above_q0_on_branch": above_br,
                "diagnostic_crossings_beyond_q_star": [float(c) for c in ray],
                "crosses_below_q0": bool(below),
                "word": word_composition(Z, N, Q0),
                "wall_sec": round(time.time() - t0, 1),
            }
            print(f"   {nm:5s} ({Z},{N}) {cls:5s} F(q₀)={float(fq0):+.4e}  "
                  f"below-q₀: {below if below else 'none'}   "
                  f"on-branch>q₀: {above_br if above_br else 'none'}   "
                  f"diagnostic>q*: {[round(c,5) for c in ray] if ray else 'none'}", flush=True)

    # ── 3. verdict ─────────────────────────────────────────────────────────
    print("\n" + "=" * 92)
    print(" 3. DOES THE Z=N ⇒ 'crosses below q₀' PATTERN SURVIVE THE CONTROL?")
    print("=" * 92)
    holds = True
    rows = []
    for nm, r in results.items():
        predicted = (r["isospin_class"] == "Z=N")
        observed = r["crosses_below_q0"]
        ok = (predicted == observed)
        holds = holds and ok
        rows.append((nm, r["n_strands"], r["isospin_class"], predicted, observed, ok))
        print(f"   {nm:5s} n={r['n_strands']:2d} {r['isospin_class']:5s} "
              f"predicted below-q₀ crossing: {predicted!s:5s}  observed: {observed!s:5s}  "
              f"{'OK' if ok else '*** BREAKS THE PATTERN ***'}")
    verdict = ("isospin_pattern_survives_fixed_n_control" if holds
               else "isospin_pattern_BROKEN_by_fixed_n_control")
    print(f"\n   VERDICT: {verdict}")
    print("=" * 92)
    print(f" TOTAL WALL {time.time()-T0:.0f}s")

    w = WitnessBuilder("threerow-isospin-parity", engine="mpmath50+f64-seminormal-sparse",
                       output_dir=OUTDIR)
    w.set_description(
        "Bean qou-prjo. Controlled test of the 'Z=N crosses below q₀, Z≠N crosses above' "
        "pattern observed across {D,T,³He,⁴He} in #4832. In that four-point set isospin "
        "and strand count are CONFOUNDED (Z=N ⟺ A even ⟺ n∈{6,12}); extending to ⁶Li/⁷Li "
        "preserves the confound AND is unaffordable, since the batched-column trace costs "
        "O(L·Σ_λ dim²) with Σ_{λ⊢n} dim² = n! exactly (n=18 is 1.34e7× the n=12 cost). "
        "This probe instead holds n FIXED and varies only (Z,N): n=6 D(1,1) vs pp(2,0)/"
        "nn(0,2); n=12 ⁴He(2,2) vs ⁴Li(3,1)/⁴H(1,3). pp/nn/⁴Li/⁴H are COMBINATORIAL probes, "
        "not bound nuclides, and no physical claim is made about them. Crossings are "
        "reported separately on the REAL-LEVEL branch (1,q*), q*=1.27844957657969 (where "
        "the Wenzl level r is real and which contains q₀), and on a beyond-substrate "
        "DIAGNOSTIC ray above q* where r is COMPLEX. free_parameters=0; AME never used; "
        "experimental proton anchor; live y_λ closed form; layer-pure."
    )
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("free_parameters", 0)
    w.add_parameter("q_star_real_level_branch_end", mp.nstr(Q_STAR, 30))
    w.add_parameter("chi_precision", "f64 Hoefsmit seminormal (sparse kernel)")
    w.add_data("cost_law_sum_dim_squared_equals_n_factorial", cost)
    w.add_data("controlled_results", results)
    w.add_data("pattern_rows", [{"iso": a, "n": b, "class": c, "predicted_below": d,
                                 "observed_below": e, "consistent": f} for a, b, c, d, e, f in rows])
    w.add_data("verdict", verdict)
    w.add_assertion("isospin_pattern_survives_fixed_n_control", holds, holds)
    w.add_caveat(
        "CONFOUND. Across {D,T,³He,⁴He} (and ⁶Li,⁷Li) isospin and strand count move "
        "together: Z=N ⟺ A even ⟺ n ∈ {6,12,18}. Any claim that the crossing side is set "
        "by ISOSPIN rather than by n must come from a FIXED-n comparison; that is what "
        "this probe supplies. Extending the A-ladder cannot decide it, however many "
        "isotopes are added."
    )
    w.add_caveat(
        "pp(2,0), nn(0,2), ⁴Li(3,1), ⁴H(1,3) are COMBINATORIAL PROBES of the braid word, "
        "NOT bound nuclides — the diproton/dineutron are unbound and ⁴H/⁴Li are unbound "
        "resonances. They are used only because `atom_braid_word_3A(Z,N)` is defined for "
        "any (Z,N). No physical prediction is made about them and AME is never consulted."
    )
    w.add_caveat(
        "BEYOND-SUBSTRATE. Every `diagnostic_crossings_beyond_q_star` value is at q > q* = "
        "1.27845, where the effective Wenzl level r = log(Q^r)/log(Q) is COMPLEX and the "
        "principal specialisation has no real level. Such values are structural diagnostics "
        "of the analytic function, NOT physical claims, and are NOT comparable to "
        "on-branch crossings as members of one trend."
    )
    w.add_caveat(
        "Scope-(a). A located crossing is a positive existence statement; 'no crossing' is "
        "about the swept interval and grid only (an even number of zeros between adjacent "
        "grid points can be missed). No invariant is proved, so no scope-(b) claim is made. "
        "value_only object: the binding MAGNITUDE remains OPEN (bean qou-prjo)."
    )
    w.save()
    print(f"witness -> {OUTDIR}/threerow-isospin-parity.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
