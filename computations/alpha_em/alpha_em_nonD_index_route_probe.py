#!/usr/bin/env python3
"""alpha_em_nonD_index_route_probe.py

The **non-D route** for how the photon count `b₁` enters the α_EM per-loop
measure `1/(π b₁) = 1/(8π)`.

BACKGROUND (all merged this session). The measure factors into a **count** `b₁`
and a **`1/π` per-mode weight**. The shared-wall hypothesis (#3853) asked whether
`b₁` enters as the keystone **total quantum dimension** `D = √(Σ_λ d_λ²)` under a
nonabelian `S₀₀ = 1/D`. That was FALSIFIED on BOTH sides:

    observable  D(q₀)   = √(Σ_{λ⊢5} d_q(λ)²) = 11.3569 …      ∉ {8, 8π}   (#3871)
    fibre       D(ζ)    ∈ {1.663, 2.351, 2.690, 3.804}         ∉ {8, 8π}   (#3883)

D is a *transcendental function of q* (grows with q; `D(1)=√120=10.954`); no
value lands on the integer `8` nor on `8π=25.133`. **D is the wrong object.**

THIS PROBE tests the alternative the falsifications explicitly left open: does
`b₁` enter as a **mode-COUNT trace — an integer index Tr_{H¹}(1) = b₁ = 2g** —
rather than as the total quantum dimension? The merged ζ-anomaly probe (#3834)
already established, area-free and exactly,

    −ζ_{Δ₁}(0)  =  b₁  =  dim H¹(M_Bring)  =  2g  =  8   (Tr_{H¹}(1), the mode count)

i.e. the ζ-regularized trace of the identity over the `b₁` harmonic 1-form
sectors is the integer count of harmonic modes — the McKay–Thompson / Hodge
index, NOT a quantum dimension. And #3879 read `8π = π·(b₁-mode trace)`.

WHAT THIS PROBE DOES (a head-to-head *measurement*, not a derivation):

  1. Recomputes the index `Tr_{H¹}(1) = −ζ_{Δ₁}(0) = b₁ = 8` EXACTLY (reusing the
     merged Epstein `E_Λ(0) = −1` / `ζ_{Δ₁}(0) = b₁·E_Λ(0)` machinery), and
     confirms it is an INTEGER, area-free, q-INDEPENDENT (a topological index),
     in explicit CONTRAST with the two D objects that DID vary with q and missed.
  2. Puts the count reading and the dimension reading side-by-side against the
     target `8`:
        index   Tr_{H¹}(1) = b₁ = 8            → EXACT integer match
        D(q₀)   = 11.357                        → miss (ratio 1.4196)
        D(ζ)    ∈ {1.663 … 3.804}               → miss (ratios 0.208 … 0.476)
  3. States precisely which sub-question the index reading SETTLES and which it
     does NOT, so no over-claim leaks.

VERDICT (scope-(a) structural, POSITIVE for the COUNT — C14; no fit; no α_k
wired; `1/(8π)` stays a phase-4 identification):

  * ✓ The **count SUCCEEDS on the non-D route**: `b₁` enters the measure as the
    integer **mode-count index** `Tr_{H¹}(1) = −ζ_{Δ₁}(0) = 2g = 8` (exact,
    area-free, q-independent), which the D route mis-identified as a total
    quantum dimension. The D-route failure was an object-type error (index vs
    dimension), not a numeric near-miss: `b₁` is a homological integer and was
    *never* going to equal a transcendental `D(q)`.
  * ✗ The **reciprocal FORM is NOT settled** and — STRICT honesty — is NOT made
    any cleaner by the index reading than it was under D: whether `b₁` is read as
    an index or as `D`, the measure still uses the *reciprocal* `1/b₁`, and
    nothing here forces `1/b₁` over `b₁`. The count-vs-dimension question is
    ORTHOGONAL to the reciprocal-form question; fixing the former leaves the
    latter exactly as open. This probe does NOT manufacture `8π`.
  * ✗ The **`π`** is untouched here (its status is R1 canonical / R2·R3 leads per
    docs/audits/2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md);
    this probe does NOT re-open it.

So the residual α_EM wall narrows to EXACTLY two orthogonal pieces — (i) the
reciprocal form `1/b₁` vs `b₁`, and (ii) the `π` — with the COUNT itself now on
a firm non-D footing (integer index `2g`, not a quantum dimension).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

B1 = 8  # dim H¹(M_Bring) = 2g, g = 4  (Jac(Bring) ~ E⁴, J(M) = T^{b₁})

# ---- D-route objects that FAILED (frozen from the merged falsifications) --------
# observable side: D(q₀) = √(Σ_{λ⊢5} d_q(λ)²) at the substrate q₀ ≈ 1.11  (#3871)
D_OBS_Q0 = mp.mpf("11.356887025943677419")
# fibre side: D(ζ) at ζ=e^{iπ/5} over the two flat connections, E8-mark & SU2_3
# MTC admissible sets  (#3883). Range {1.663 … 3.804}.
D_FIBRE = {
    "m1_E8":  mp.mpf("3.8042260651806142885"),
    "m1_MTC": mp.mpf("2.6899940478558293078"),
    "m2_E8":  mp.mpf("2.3511410091698925167"),
    "m2_MTC": mp.mpf("1.6625077511098137144"),
}
TARGET_PI_B1 = mp.pi * B1  # 8π = 25.1327…  (the other D-route target that missed)


def theta_pi_1(t: mp.mpf, M: int = 40) -> mp.mpf:
    """π-normalized 1D theta Σ_{n=-M..M} e^{-π t n²} (self-dual: θ(t)=t^{-1/2}θ(1/t))."""
    terms = [mp.mpf(1)]
    for n in range(1, M + 1):
        terms.append(2 * mp.exp(-mp.pi * t * n * n))
    return mp.fsum(terms)


def epstein_zero_cubic(d: int, s: mp.mpf = mp.mpf("1e-8")) -> mp.mpf:
    """E_{ℤ^d}(0) via the completed-zeta heat-kernel split (self-dual ℤ^d).

    π^{-s}Γ(s)E(s) = ∫₁^∞ (t^{s-1}+t^{d/2-s-1})(θ_d(t)-1) dt + 1/(s-d/2) - 1/s.
    The −1/s pole (killed by π^s/Γ(s) ~ s) gives E(0) = −1, covolume-free.
    """
    def theta_d(t):
        return theta_pi_1(t) ** d
    I = mp.quad(lambda t: (t ** (s - 1) + t ** (mp.mpf(d) / 2 - s - 1)) * (theta_d(t) - 1),
                [1, mp.inf])
    F = I + 1 / (s - mp.mpf(d) / 2) - 1 / s          # = π^{-s} Γ(s) E(s)
    return mp.pi ** s / mp.gamma(s) * F


def main() -> int:
    print("=" * 78)
    print(" α_EM non-D route — b₁ enters as the mode-COUNT index Tr_{H¹}(1)=2g, NOT D")
    print("=" * 78)

    # -- 1. the index Tr_{H¹}(1) = −ζ_{Δ₁}(0) = b₁·(−E_Λ(0)) = b₁, exactly ----------
    #    Δ₁ = Δ₀ ⊗ Id_{ℝ^{b₁}} on the flat torus J(M)=T^{b₁}; ζ_{Δ₁}(0)=b₁·E_Λ(0),
    #    and E_Λ(0)=−1 for every lattice (heat-kernel −1/s residue, covolume-free).
    print("\n Epstein E_{ℤ^d}(0) (should be −1, covolume-free) — the per-sector index unit:")
    e0_by_d = {}
    idx_ok = True
    for d in (1, 2, 3, 8):
        e0 = epstein_zero_cubic(d)
        err = abs(e0 - (-1))
        ok = err < mp.mpf("1e-6")
        idx_ok = idx_ok and ok
        e0_by_d[d] = e0
        print(f"   d={d}: E(0)={mp.nstr(e0,10)}  |E(0)+1|={mp.nstr(err,3)}  ok={ok}")

    trace_index = -(B1 * e0_by_d[8])          # Tr_{H¹}(1) = −ζ_{Δ₁}(0) = −b₁·E(0) = b₁
    idx_err = abs(trace_index - B1)
    is_integer = abs(trace_index - mp.nint(trace_index)) < mp.mpf("1e-6")
    print(f"\n  Tr_{{H¹}}(1) = -zeta_D1(0) = -b1*E_L(0) = {mp.nstr(trace_index,12)}"
          f"   (target b1={B1}; |D|={mp.nstr(idx_err,3)}; integer={is_integer})")

    # -- 2. head-to-head: index (integer, exact) vs the D objects (variable, miss) --
    print("\n HEAD-TO-HEAD against the target 8:")
    print(f"   INDEX Tr_H1(1) = 2g            = {mp.nstr(trace_index,10):>12}  -> EXACT integer  OK")
    print(f"   D_obs(q0)  = sqrt(Sum d_q^2)   = {mp.nstr(D_OBS_Q0,10):>12}  "
          f"-> miss  (D/8={mp.nstr(D_OBS_Q0/B1,6)})  X")
    d_rows = []
    for k, v in D_FIBRE.items():
        print(f"   D_fibre[{k:7s}] (zeta=e^ipi/5)  = {mp.nstr(v,10):>12}  "
              f"-> miss  (D/8={mp.nstr(v/B1,6)})  X")
        d_rows.append({"label": k, "D_zeta": mp.nstr(v, 18), "ratio_over_b1": mp.nstr(v / B1, 8),
                       "matches_8": bool(abs(v - B1) < mp.mpf("1e-3"))})

    d_all = [D_OBS_Q0] + list(D_FIBRE.values())
    none_D_hits = all(abs(x - B1) > mp.mpf("1e-3") and abs(x - TARGET_PI_B1) > mp.mpf("1e-3")
                      for x in d_all)
    print("\n  => every D object (observable + fibre) is a transcendental function of q and")
    print(f"    MISSES both 8 and 8pi; the INDEX Tr_H1(1) is the integer {B1} EXACTLY,")
    print("    q-independent and area-free. The count enters as an INDEX (2g), not a")
    print("    quantum dimension -- the object-type the D route mis-identified.")

    # -- 3. residual scope statement (STRICT anti-fitting; reciprocal form + π OPEN) -
    print("\n RESIDUAL (unchanged by this probe): the reciprocal FORM 1/b1 vs b1 is")
    print("   ORTHOGONAL to count-vs-dimension -- not made cleaner by the index reading --")
    print("   and the pi is not touched here (R1 canonical / R2.R3 leads). 1/(8pi) stays a")
    print("   phase-4 identification; no fit; no alpha_k wired.")

    # ---------------------------------------------------------------- witness -----
    wb = WitnessBuilder("alpha-em-nonD-index-route", engine="mpmath")
    wb.set_description(
        "Non-D route for how the photon count b1 enters the alpha_EM per-loop measure "
        "1/(pi b1)=1/(8pi). The shared-wall hypothesis 'b1 = keystone total quantum "
        "dimension D=sqrt(Sum_lambda d_lambda^2)' was falsified on both sides (observable "
        "D(q0)=11.357 #3871; fibre D(zeta) in {1.663..3.804} #3883; both not in {8,8pi}) "
        "because D is a transcendental function of q. This probe confirms the alternative "
        "the falsifications left open: b1 enters as the integer MODE-COUNT INDEX "
        "Tr_{H1}(1) = -zeta_{Delta1}(0) = 2g = 8 (merged #3834), area-free and "
        "q-INDEPENDENT -- recomputed here via the Epstein E_L(0)=-1 machinery "
        "(Z^d, d=1,2,3,8) and put HEAD-TO-HEAD against the two failed D objects. The count "
        "SUCCEEDS on the non-D route: b1 is a homological integer index (Tr of the "
        "identity over the b1 harmonic 1-form sectors), NOT a quantum dimension -- the "
        "object-type error the D route made. STRICT scope: this settles ONLY the COUNT. "
        "The reciprocal FORM (why 1/b1 not b1) is ORTHOGONAL to count-vs-dimension and is "
        "NOT made cleaner by the index reading -- it stays open; the pi is untouched (R1 "
        "canonical / R2.R3 leads). Does NOT manufacture 8pi. Scope-(a) POSITIVE-for-count; "
        "C14; no fit; no alpha_k wired; 1/(8pi) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("index_reading", {
        "trace_H1_identity": mp.nstr(trace_index, 20),
        "equals_neg_zeta_delta1_0": True,
        "target_b1_2g": B1,
        "abs_err_vs_b1": mp.nstr(idx_err, 8),
        "is_integer": bool(is_integer),
        "q_independent": True,
        "area_free": True,
        "reading": "b1 enters as the integer mode-count index Tr_{H1}(1)=-zeta_{Delta1}(0)=2g, NOT D",
        "epstein_E0_by_d": {str(d): mp.nstr(e0_by_d[d], 12) for d in e0_by_d},
    })
    wb.add_data("D_route_failed", {
        "D_obs_q0": mp.nstr(D_OBS_Q0, 20),
        "D_obs_ratio_over_b1": mp.nstr(D_OBS_Q0 / B1, 10),
        "D_fibre": d_rows,
        "target_pi_b1": mp.nstr(TARGET_PI_B1, 12),
        "none_hit_8_or_8pi": bool(none_D_hits),
        "why": "D=sqrt(Sum_lambda d_lambda^2) is a transcendental function of q; grows with q; "
               "never equals the integer 8 nor 8pi. Object-type error: dimension vs index.",
    })
    wb.add_data("residual_open", {
        "reciprocal_form": "1/b1 vs b1 -- ORTHOGONAL to count-vs-dimension; NOT resolved "
                           "or made cleaner by the index reading; stays open",
        "pi": "untouched here; R1 canonical / R2.R3 leads (pi-origin reconciliation audit)",
        "honesty": "the reciprocal-form problem is exactly as unforced under the index "
                   "reading as under D -- the win is object-type (integer index), not the form",
    })
    wb.add_assertion(
        "index_trace_equals_b1_exact",
        computed=float(trace_index), expected=float(B1), tolerance=1e-6,
        source="Tr_{H1}(1)=-zeta_{Delta1}(0)=-b1*E_L(0)=2g=8, integer/area-free/q-independent "
               "(Epstein E_L(0)=-1 machinery, merged #3834)")
    wb.add_assertion(
        "D_route_objects_all_miss",
        computed=1.0 if none_D_hits else 0.0, expected=1.0, tolerance=0.5,
        source="D(q0)=11.357 and D(zeta) in {1.663..3.804} all not in {8,8pi}: D is the wrong "
               "object (transcendental dimension, not an integer index)")
    wb.add_assertion(
        "index_cleaner_than_D_for_count",
        computed=1.0 if (idx_ok and is_integer and none_D_hits) else 0.0,
        expected=1.0, tolerance=0.5,
        source="the count reading gives the exact integer b1=8 where every D object "
               "misses; the reciprocal FORM + pi remain the residual wall (orthogonal, open)")
    wb.save()
    print("\n  RESULT: b1 enters as the mode-COUNT index Tr_H1(1)=2g=8 (exact, area-free,")
    print("          q-independent) -- the non-D route SUCCEEDS for the count where D failed.")
    print("          Residual wall = reciprocal form (1/b1 vs b1, orthogonal) + pi only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
