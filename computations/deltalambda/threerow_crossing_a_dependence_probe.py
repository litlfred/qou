#!/usr/bin/env python3
"""threerow_crossing_a_dependence_probe.py — is the deuteron ≥3-row sign crossing
SPECIAL to n=6, or is the crossing q A-DEPENDENT (drifting past q₀ for n≥9)?

UNIT 2 follow-up to #4829 (bean qou-prjo).

#4829 established, for `F_K(q) = Σ_{λ⊢3A, ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ`:

  * D   (n=6):  F(q→1⁺) = +8.05e-5 → F(q₀) = −0.1950,  CROSSES at q ≈ 1.05365
  * T   (n=9):  F(q→1⁺) = −4.06e-4 → F(q₀) = −2.318,   "no crossing"
  * ³He (n=9):  F(q→1⁺) = −4.06e-4 → F(q₀) = −2.806,   "no crossing"

but only swept `q ∈ (1, q₀]`.  A "no crossing on (1,q₀]" is a scope-(a) negative
about **an interval**, not about the object: the crossing may simply lie at
q > q₀.  THOSE ARE VERY DIFFERENT STRUCTURAL STATEMENTS:

  * crossing ABSENT at n=9      ⇒ the deuteron flip is SPECIAL (an n=6 accident)
  * crossing PRESENT at q > q₀  ⇒ the crossing q is A-DEPENDENT and DRIFTS, and
                                  the substrate q₀ sits BELOW the n=9 crossing —
                                  i.e. q₀ is positioned between the n=6 and the
                                  n=9 crossing.  The deuteron is then not special;
                                  it is the only light isotope whose crossing has
                                  already been passed at q₀.

This probe distinguishes them by sweeping a **DIAGNOSTIC RAY q > q₀**.

  ⚠ BEYOND-SUBSTRATE DIAGNOSTIC — NOT A PHYSICAL CLAIM.  The substrate modulus is
  q₀ ≈ 1.10998 (experimental proton anchor).  Values of F_K at q > q₀ are NOT
  predictions of anything physical; the ray exists purely to determine whether the
  analytic function F_K has a zero above q₀ (structure of the object) rather than
  no zero at all.  Every witness field on the ray is prefixed `diagnostic_`.

Also reported (the structural cause, mirroring #4829 §2 at n=9):
  * per-λ decomposition of F at several q on and above the ray,
  * the running DOMINANT ℓ≥3 partition (which block sets the sign),
  * the |Δ_λ| ordering of the ℓ≥3 stratum of 9 vs of 6.

DISCIPLINE.  0 free parameters; AME never used.  q₀ = experimental proton anchor
(`q_parameter.Q`); y_λ via the LIVE closed form `y_lambda_at_q0_mpmath` (NOT the
muon-serving `wedderburn_jones_markov.y_lambda_at` cache — AGENTS.md straddle
hazard).  Layer-pure: both y_λ(q) and χ^λ(β;q) are evaluated at the SAME running q.
χ^λ is f64 (pure-Python Hoefsmit seminormal; no mpfr kernel in this sandbox) —
decisive for a SIGN question away from a crossing, where |F| = O(1)–O(10¹).
Scope-(a)/(b) honest: a located crossing is a POSITIVE existence statement
(bracketed sign change + continuity); "no crossing on interval I" is scope-(a).
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),                 # computations/
    str(Path(__file__).resolve().parent.parent / "substrate"),   # q_parameter, _precision
    str(Path(__file__).resolve().parent.parent / "hecke"),       # hecke_characters
]
import _path_bridge  # noqa: F401,E402

import time  # noqa: E402
import mpmath as mp  # noqa: E402

from threerow_sign_crossing_probe import (  # noqa: E402
    chi_atom, delta_lambda, F_iso, G_char_free, bisect_cross, Q0, Q_LO, ZN,
    F64_SIG_DIGITS, fmt_f64_limited,
)
from schur_principal_mpmath import y_lambda_at_q0_mpmath, partitions_of  # noqa: E402
from _precision import set_compute_dps, str_at_true_precision  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

# Diagnostic ray: q₀ → Q_RAY_MAX.  BEYOND-SUBSTRATE, structural diagnostic only.
Q_RAY_MAX = mp.mpf("4.0")
RAY_NPTS = 25


def ray_grid(lo: mp.mpf, hi: mp.mpf, npts: int) -> list[mp.mpf]:
    """Geometric grid in (q−1) from lo to hi."""
    a, b = mp.log(lo - 1), mp.log(hi - 1)
    return [1 + mp.e ** (a + (b - a) * k / (npts - 1)) for k in range(npts)]


def scan_crossings(f, grid: list[mp.mpf]) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """Evaluate f on grid; bisect every bracketed sign change. Returns (qs, vals).

    `qs` stays mpf. It used to be `float(...)`, which put the physical/diagnostic
    split (`q <= q₀`) on the f64 side of a comparison against a 50-dps q₀ — a
    classification decided at 1e-17 when the located crossing is itself only
    f64-resolved. Serialization happens at the witness sink, not here.
    """
    vals = [f(q) for q in grid]
    qs = []
    for i in range(len(grid) - 1):
        a, b = vals[i], vals[i + 1]
        if a != 0 and b != 0 and (a > 0) != (b > 0):
            qs.append(bisect_cross(f, grid[i], grid[i + 1], a, b, iters=40))
    return qs, vals


def dominant_partition(Z: int, N: int, q: mp.mpf, min_rows: int = 3):
    """Return (λ*, term*, total, rows) — the ℓ≥3 partition with the largest |term| at q."""
    n = 3 * (Z + N)
    y = y_lambda_at_q0_mpmath(n, q)
    rows = []
    tot = mp.mpf(0)
    for lam in partitions_of(n):
        if len(lam) < min_rows:
            continue
        t = y[lam] * chi_atom(lam, Z, N, q) * delta_lambda(lam)
        tot += t
        rows.append((lam, delta_lambda(lam), t))
    rows.sort(key=lambda r: -abs(r[2]))
    return rows[0][0], rows[0][2], tot, rows


def main() -> int:
    print("=" * 88)
    print(" UNIT 2 — is the ≥3-row sign crossing SPECIAL to the deuteron (n=6),")
    print(" or A-DEPENDENT with the n=9 crossing lying ABOVE the substrate q₀?")
    print("=" * 88)
    print(f" q₀ (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")
    print(f" diagnostic ray q ∈ (1, {mp.nstr(Q_RAY_MAX, 4)}]  — BEYOND-SUBSTRATE for q > q₀,")
    print(" structural diagnostic ONLY, not a physical claim.")

    # ── 0. |Δ_λ| ordering of the ℓ≥3 stratum: n=6 vs n=9 ───────────────────
    print("\n" + "─" * 88)
    print(" 0.  ℓ≥3 stratum |Δ_λ| ordering  (Δ_λ = (−1)^{n(λ)}·dim V_λ, PROVED value-only)")
    print("─" * 88)
    strata = {}
    for n in (6, 9):
        rows = sorted(((lam, delta_lambda(lam)) for lam in partitions_of(n)
                       if len(lam) >= 3), key=lambda r: -abs(r[1]))
        strata[str(n)] = {
            "count_l_ge_3": len(rows),
            "max_abs_delta": int(abs(rows[0][1])),
            "top5": [{"partition": list(l), "delta": int(d)} for l, d in rows[:5]],
            # is the TOP |Δ| unique, or a ± cancelling pair of equal magnitude?
            "top_abs_multiplicity": sum(1 for _, d in rows if abs(d) == abs(rows[0][1])),
            "top_is_signed_cancelling_pair": bool(
                sum(1 for _, d in rows if abs(d) == abs(rows[0][1])) == 2
                and rows[0][1] == -rows[1][1]
            ),
        }
        print(f"  n={n}: {len(rows)} partitions, max|Δ|={abs(rows[0][1])}, top:")
        for l, d in rows[:5]:
            print(f"      {str(l):22s} Δ={d:+6d}")
        print(f"      top-|Δ| multiplicity = {strata[str(n)]['top_abs_multiplicity']}"
              f"   signed-cancelling-pair = {strata[str(n)]['top_is_signed_cancelling_pair']}")

    # ── 1. the diagnostic ray, per isotope ─────────────────────────────────
    print("\n" + "─" * 88)
    print(" 1.  F_K(q) on the diagnostic ray  (q > q₀ is BEYOND-SUBSTRATE diagnostic)")
    print("─" * 88)
    grid = ray_grid(Q_LO, Q_RAY_MAX, RAY_NPTS)
    iso = {}
    iso_mpf = {}          # the mpf crossings, kept out of the witness dict
    for name in ("D", "T", "3He"):
        Z, N = ZN[name]
        n = 3 * (Z + N)
        f = lambda q, Z=Z, N=N: F_iso(Z, N, q)
        t0 = time.time()
        qs, vals = scan_crossings(f, grid)
        below = [q for q in qs if q <= Q0]          # mpf vs mpf, not f64 vs 50-dps
        above = [q for q in qs if q > Q0]
        f_q0 = f(Q0)
        iso_mpf[name] = {"first_above": above[0] if above else None}
        iso[name] = {
            "n_strands": n,
            "F_at_qlo": fmt_f64_limited(vals[0]),
            "F_at_q0": fmt_f64_limited(f_q0),
            "sign_qlo": int(mp.sign(vals[0])),
            "sign_q0": int(mp.sign(f_q0)),
            "crossings_below_or_at_q0": [fmt_f64_limited(q) for q in below],
            "diagnostic_crossings_above_q0": [fmt_f64_limited(q) for q in above],
            "diagnostic_first_crossing_above_q0":
                fmt_f64_limited(above[0]) if above else None,
            "diagnostic_ray_max_q": str_at_true_precision(Q_RAY_MAX),
            "diagnostic_n_crossings_on_ray": len(qs),
        }
        print(f"\n  {name:4s} n={n:2d}  F(q_lo)={float(vals[0]):+.5e}  F(q₀)={float(f_q0):+.5e}"
              f"   ({time.time()-t0:.0f}s)")
        print(f"        crossings ≤ q₀ (PHYSICAL INTERVAL): "
              f"{[float(q) for q in below] if below else 'none'}")
        print(f"        crossings > q₀ (DIAGNOSTIC ONLY)  : "
              f"{[f'{float(q):.6f}' for q in above] if above else 'none'}")

    # ── 2. what happens at the n=9 crossing: which block overtakes? ────────
    print("\n" + "─" * 88)
    print(" 2.  per-λ decomposition at n=9 — which ℓ≥3 block sets the sign, and where")
    print("     does the dominant block change?  (mirrors #4829 §2 at n=6)")
    print("─" * 88)
    decomp = {}
    for name in ("T", "3He"):
        Z, N = ZN[name]
        qc = iso_mpf[name]["first_above"]     # the mpf, not the serialized string
        # sample: q→1⁺, q₀, and (if a diagnostic crossing exists) either side of it
        samples = [("q_lo", Q_LO), ("q0", Q0)]
        if qc is not None:
            samples += [("diag_below_cross", qc * mp.mpf("0.97")),
                        ("diag_above_cross", qc * mp.mpf("1.03"))]
        rec = {}
        print(f"\n  --- {name} (n=9) ---")
        for tag, q in samples:
            lam_star, t_star, tot, rows = dominant_partition(Z, N, q)
            rec[tag] = {
                "q": str_at_true_precision(q),
                "dominant_partition": list(lam_star),
                "dominant_delta": int(delta_lambda(lam_star)),
                "dominant_term": fmt_f64_limited(t_star),
                "total": fmt_f64_limited(tot),
                "top4": [{"partition": list(l), "delta": int(d),
                          "term": fmt_f64_limited(t)}
                         for l, d, t in rows[:4]],
                "beyond_substrate": bool(q > Q0),
            }
            flag = "  [DIAGNOSTIC q>q₀]" if q > Q0 else ""
            print(f"    {tag:18s} q={float(q):.6f}  total={float(tot):+.5e}"
                  f"  dominant={str(lam_star)} (Δ={delta_lambda(lam_star):+d},"
                  f" term={float(t_star):+.4e}){flag}")
            for l, d, t in rows[:4]:
                print(f"        {str(l):22s} Δ={d:+6d}  term={float(t):+.5e}")
        decomp[name] = rec

    # ── 3. character-free companion on the ray (n=6,9,12) ──────────────────
    print("\n" + "─" * 88)
    print(" 3.  character-free companion G(q)=Σ_{ℓ≥3} y_λ(q)·Δ_λ on the ray (full mpmath)")
    print("─" * 88)
    cf = {}
    for n in (6, 9, 12):
        f = lambda q, n=n: G_char_free(n, q)
        qs, vals = scan_crossings(f, grid)
        below = [q for q in qs if q <= Q0]
        above = [q for q in qs if q > Q0]
        # G is character-free: no χ kernel, so these keep their full 50 dps.
        cf[str(n)] = {
            "G_at_qlo": str_at_true_precision(vals[0]),
            "G_at_q0": str_at_true_precision(f(Q0)),
            "crossings_below_or_at_q0": [str_at_true_precision(q) for q in below],
            "diagnostic_crossings_above_q0": [str_at_true_precision(q) for q in above],
        }
        print(f"  n={n:2d}  G(q_lo)={float(vals[0]):+.4e}  G(q₀)={float(f(Q0)):+.4e}"
              f"   ≤q₀: {[float(q) for q in below] if below else 'none'}"
              f"   >q₀ (diag): "
              f"{[f'{float(q):.5f}' for q in above] if above else 'none'}")

    # ── STRUCTURAL-ZERO GUARD, which must run BEFORE the verdict ───────────
    #
    # The verdict below branches on (a) a crossing existing on the diagnostic
    # ray and (b) none existing on the physical interval. NOTHING in it checks
    # whether F is nonzero at all — so an F that is IDENTICALLY ZERO lands in
    # the `A_DEPENDENT_crossing_above_q0` branch by construction, the moment
    # round-off changes sign anywhere on the ray.
    #
    # That is what the committed 2026-08-25 witness recorded, and it was wrong
    # three ways at once:
    #
    #   * it asserts "the n=9 crossing EXISTS" while its own fields read
    #     F_at_qlo = F_at_q0 = 0.0 and sign = 0 for D, T and 3He alike;
    #   * it says "q0 sits between the n=6 and n=9 crossings" while its own
    #     `crossings_below_or_at_q0` is [] for every isotope — there is no n=6
    #     crossing on the physical interval to sit above;
    #   * it says A-DEPENDENT while its own numbers give D, T and 3He the
    #     IDENTICAL first crossing, 1.5378214048144982, to 17 digits — and the
    #     character-free companion G finds the same value at n = 6, 9 AND 12.
    #     A location identical across three braid words, three n, and two
    #     different objects is not a property of any of them.
    #
    # Measured 2026-08-29 at 70 dps: max|y_lambda| over the ell>=3 stratum is
    # BELOW the noise floor at every q on the ray, including at all three
    # "located crossings" --
    #
    #     q                     max|y| ell>=3      floor
    #     1.0001                0.0                1.09e-63
    #     1.1099785827513808    0.0                1.15e-63
    #     1.5378214048144982    1.34e-72           2.08e-63
    #     2.2810884055126934    9.77e-73           4.31e-63
    #     4.0                   2.63e-74           7.41e-63
    #
    # -- nine orders below. Under convention D the Wenzl level is r = 2, so
    # y_lambda = 0 for ell(lambda) > 2 IDENTICALLY IN q; the ray does not escape
    # it. The located crossings are sign changes of cancellation residue.
    #
    # The C-frame result this probe followed up (#4829: crossing at q ~ 1.05365,
    # F(q0) = -0.1950) is NOT refuted. It was a real convention-C measurement and
    # is out of frame, not wrong. What went wrong is that the convention-D
    # regeneration updated the MEASUREMENTS and left the VERDICT.
    _zero_q = [Q_LO, Q0, mp.mpf("1.5378214048144982"), Q_RAY_MAX]
    _above_floor = []
    for _q in _zero_q:
        _y = y_lambda_at_q0_mpmath(6, _q)
        _all = max(abs(mp.mpf(v)) for v in _y.values())
        _ge3 = max((abs(mp.mpf(v)) for l, v in _y.items() if len(l) >= 3),
                   default=mp.mpf(0))
        if _ge3 >= _all * mp.mpf(10) ** (-(mp.mp.dps - 8)):
            _above_floor.append(_q)
    structural_zero = not _above_floor

    # ── verdict ────────────────────────────────────────────────────────────
    n9_above = [name for name in ("T", "3He")
                if iso[name]["diagnostic_first_crossing_above_q0"] is not None]
    n9_below = [name for name in ("T", "3He") if iso[name]["crossings_below_or_at_q0"]]
    if structural_zero:
        verdict = "structural_zero_no_crossing_exists"
        vtext = ("STRUCTURAL ZERO under convention D. F_K(q) = 0 identically — the "
                 "Wenzl level is r = 2, so y_lambda = 0 for ell(lambda) > 2 at EVERY "
                 "q, on the ray as well as on the physical interval. The question "
                 "'is the crossing A-dependent' has no answer because there is no "
                 "crossing: every located q is a sign change of cancellation "
                 "residue, which is why all three isotopes and both objects share "
                 "the same locations. The #4829 convention-C result is out of "
                 "frame, not refuted.")
    elif n9_above and not n9_below:
        verdict = "A_DEPENDENT_crossing_above_q0"
        vtext = ("A-DEPENDENT. The n=9 crossing EXISTS but lies ABOVE q₀ — the "
                 "deuteron is NOT special; q₀ sits between the n=6 and n=9 crossings.")
    elif not n9_above and not n9_below:
        verdict = "no_n9_crossing_on_diagnostic_ray"
        vtext = ("No n=9 crossing found anywhere on the diagnostic ray — the deuteron "
                 "crossing looks SPECIAL to n=6 (scope-(a): this ray only).")
    else:
        verdict = "mixed"
        vtext = "Mixed: see per-isotope rows."
    print("\n" + "=" * 88)
    print(f" VERDICT: {verdict}")
    print(f"   {vtext}")
    _dcross = iso['D']['crossings_below_or_at_q0']
    print(f"   crossing q:  D (n=6) = {_dcross if _dcross else 'NONE'}  [≤ q₀, PHYSICAL]")
    for name in ("T", "3He"):
        print(f"                {name} (n=9) = "
              f"{iso[name]['diagnostic_first_crossing_above_q0']}  [> q₀, DIAGNOSTIC]")
    print("=" * 88)

    # ── witness ────────────────────────────────────────────────────────────
    w = WitnessBuilder("threerow-crossing-a-dependence", engine="mpmath+f64-seminormal",
                       output_dir=Path(__file__).resolve().parent)
    w.set_description(
        "UNIT 2 of bean qou-prjo follow-up to #4829. Determines whether the deuteron "
        "≥3-row sign crossing of F_K(q)=Σ_{λ⊢3A,ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ is "
        "SPECIAL to n=6 or A-DEPENDENT with the n=9 crossing lying ABOVE the substrate "
        "q₀. Sweeps a DIAGNOSTIC RAY q ∈ (1, 4.0]; every q > q₀ field is prefixed "
        "'diagnostic_' and is a STRUCTURAL diagnostic of the analytic object, NOT a "
        "physical claim (the substrate modulus is q₀ ≈ 1.10998, experimental proton "
        "anchor). Δ_λ=(−1)^{n(λ)}·dim (PROVED value-only); y_λ via live "
        "schur_principal_mpmath (proton anchor, NOT the muon cache); χ^λ via the "
        "q-running color-weighted nuclide braid + f64 Hoefsmit seminormal. Layer-pure. "
        "0 free parameters; AME not used."
    )
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.Q); live closed-form y_λ")
    w.add_parameter("q_lo_combinatorial_surrogate", mp.nstr(Q_LO, 12))
    w.add_parameter("diagnostic_ray_max_q", mp.nstr(Q_RAY_MAX, 6))
    w.add_parameter("diagnostic_ray_npts", RAY_NPTS)
    w.add_parameter("free_parameters", 0)
    w.add_parameter("chi_precision", "f64 Hoefsmit seminormal (no mpfr kernel in sandbox)")
    w.add_data("delta_stratum_ordering", strata)
    w.add_data("isotopes", iso)
    w.add_data("n9_per_partition_decomposition", decomp)
    w.add_data("character_free_companion", cf)
    w.add_data("verdict", verdict)
    w.add_data("verdict_text", vtext)
    w.add_data("structural_zero_under_convention_D", structural_zero)
    w.add_data("q_above_floor_on_ray", [mp.nstr(q, 20) for q in _above_floor])

    # THE ASSERTION THIS WITNESS DID NOT HAVE.
    #
    # The committed 2026-08-25 run carried ZERO assertions and `allPassed: true`,
    # so nothing could contradict a verdict its own data refuted. The invariant
    # is simple and is the one that failed: a verdict may claim a crossing EXISTS
    # only if the object is nonzero somewhere. Under a structural zero, the only
    # admissible verdict is the structural-zero one.
    _claims_crossing = verdict in ("A_DEPENDENT_crossing_above_q0", "mixed")
    _consistent = not (structural_zero and _claims_crossing)
    w.add_assertion("verdict_does_not_claim_a_crossing_in_a_vanishing_object",
                    mp.mpf(1) if _consistent else mp.mpf(0), mp.mpf(1),
                    tolerance=mp.mpf("0.5"),
                    source="a located crossing is an existence claim; an object below "
                           "the noise floor at every sampled q supports none")

    # A-INDEPENDENCE, recorded because it is the tell that the located crossings
    # are not isotope properties: D, T and 3He share their first diagnostic
    # crossing to full printed precision, and the character-free companion finds
    # the same value at n = 6, 9 and 12. Three braid words, three n, two objects.
    _firsts = {k: iso[k]["diagnostic_first_crossing_above_q0"] for k in iso}
    _vals = [v for v in _firsts.values() if v is not None]
    w.add_data("diagnostic_first_crossing_by_isotope", _firsts)
    w.add_data("diagnostic_first_crossing_is_isotope_INDEPENDENT",
               bool(_vals) and len(set(_vals)) == 1)
    # These six were add_assertion(name, X, X) under a comment calling them
    # "Falsifiable assertions". They were the opposite: computed and expected were the
    # SAME expression, so each was `x == x` -- tautologically true and unable to fail.
    # The sibling threerow_sign_crossing_probe carried the identical pattern and passed
    # while its measured sign inverted from +/-1 to 0 across the convention change.
    # A sign is a MEASUREMENT; it is recorded here, which is what add_data is for.
    # Bean qou-ploj.
    for name in ("D", "T", "3He"):
        w.add_data(f"{name}_sign_at_q0_measured", iso[name]["sign_q0"])
        w.add_data(f"{name}_sign_at_qlo_measured", iso[name]["sign_qlo"])
    w.add_caveat(
        "BEYOND-SUBSTRATE DIAGNOSTIC. Every 'diagnostic_' field reports F_K at q > q₀. "
        "The substrate modulus is q₀ ≈ 1.10998 (experimental proton anchor); q > q₀ is "
        "NOT a physical regime and no value on the ray is a prediction. The ray exists "
        "solely to distinguish 'the object has no zero' from 'the zero is above q₀', "
        "which are different structural statements about the same analytic function."
    )
    w.add_caveat(
        "χ^λ(β_K;q) is f64-precision (pure-Python Hoefsmit seminormal; no mpfr Rust "
        "kernel in this sandbox — disk quota, documented, not a proof gap). y_λ(q) is "
        "full 50-dps mpmath. Decisive for a SIGN question away from a crossing "
        "(|F| = O(1)–O(10¹) at the sampled points); a located crossing q carries only "
        "f64 resolution."
    )
    w.add_caveat(
        "value_only object: F_K is NOT a binding energy (Δ_λ is value-only). This probe "
        "tests only the SIGN structure of the ≥3-row trace weighting. The extensive "
        "super-pairwise magnitude term remains OPEN (bean qou-prjo)."
    )
    w.add_caveat(
        "Scope: a LOCATED crossing is a positive existence statement (bracketed sign "
        "change of a continuous function). 'No crossing' statements are scope-(a) — "
        "about the swept interval only — never scope-(b); no invariant is proved to "
        "forbid a zero anywhere."
    )
    w.save()
    print("\nwitness -> threerow-crossing-a-dependence.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
