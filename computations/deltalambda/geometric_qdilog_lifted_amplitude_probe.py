#!/usr/bin/env python3
"""The geometric quantum-dilog amplitude for the deuteron `r`: the ONE principled evaluation of the
FULL McPhail-Snyder–Reshetikhin lifted dilogarithm `L(ζ⁰,ζ¹)` on the pinned trefoil shape — fixing
the prior frontier probe's `Li₂`-only omission — plus the pinch-degeneracy structural finding.
Forward, single evaluation, **no scan, no fit** (§2e).

CHAIN (read first):
  * #4345 (merged): the trefoil crossing octahedral tetrahedron shape from the pinned boundary rep is
    exactly z' = −h² (cross-ratio of the fixed points of ρ(u), ρ(v)).
  * #4339 (merged): g₂_leading = 1 exact (real coloring); r = g₂ − 1 = +0.87% is the shapes→amplitude
    nonlinearity. g₂ = (bar-even deuteron/E_unit binding gap)/h² ≈ 1.00865 is a MEASURED ratio
    (labelled "NEAR-MATCH — underived" throughout the corpus), not a fit and not back-solved.
  * The frontier note (#4347) evaluated the BARE Li₂ once (Li₂(z')/z' = 0.9893, nonlinearity −1.07%)
    and stopped at the wall. This probe does the NEXT principled step: the FULL lifted dilog.

THE PRINCIPLED OBJECT (no menu — MSR fixes it uniquely). MSR (2509.02354) eq (A.15): the correct
per-tetrahedron amplitude is the *lifted* dilogarithm — the complex Chern-Simons invariant of the
flattened ideal tetrahedron —
    L(ζ⁰,ζ¹) = Li₂(e^{2πiζ⁰})/(2πi) + πi ζ⁰ζ¹ + ζ⁰ log(1 − e^{2πiζ⁰}),
with the flattening fixed by (A.8): e^{2πiζ⁰} = z, e^{−2πiζ¹} = 1 − z. NOT the bare Li₂ the prior
probe used. The corpus (`g2_leading_exact...`) established g₂ is carried by the REAL (bar-even) face,
so the principled scalar is Re L — no choice.

RESULT 1 — exact closed form (verified to 30 dps). On the eigenspace shape z = −h² the flattening is
    ζ⁰ = ½ − i·ln(h)/π   (Re ζ⁰ = ½ EXACTLY — reconciles the corpus's two trefoil frames z=½ and −h²),
    ζ¹ = i·ln(1+h²)/(2π),
and the real part of the full lifted dilog collapses to
    Re L(ζ⁰,ζ¹) = ¼ ln(1 + h²) = ¼(h² − h⁴/2 + h⁶/3 − …).
Normalising to the derived leading coefficient 1 (g₂_leading = 1):
    g₂_candidate = Re L / (h²/4) = ln(1+h²)/h² = 1 − h²/2 + h⁴/3 − …  ≈ 0.9788   ⇒   r ≈ −2.12%.

RESULT 2 — REFUTATION (scope-(a)). Target r = +0.87% (g₂ = 1.00865). The full lifted dilog gives
r ≈ −2.12%: WRONG SIGN and ~2.4× the magnitude. Fixing the prior Li₂-only omission moved the answer
FURTHER from target (−1.07% → −2.12%), not closer. So the eigenspace-shape lifted-dilog route, alone,
does NOT reproduce r. This constrains magnitudes/combinations, not ingredients (scope-(a), not (b)).

RESULT 3 — STRUCTURAL (Lean-proved, `PinchedOctahedronDegenerate.lean`). The deuteron σ₁³ = trefoil
is a torus knot ⇒ its crossings are PINCHED (§5.2, Def 5.3: incoming over/under eigenspaces coincide).
At the standard pinched log-coloring (§5.2 eq 5.7) ALL FOUR MSR shape-logs ζ⁰_{r,t,l,b} = 0
identically, so the octahedral e₂ = Σ_{i<j} ζ⁰_i ζ⁰_j = 0. The "four-shape octahedron" has NO
four-distinct-shape content at the pinched trefoil (the four ideal tetrahedra collapse to z=1). Hence
g₂ is NOT the naive octahedral e₂ of the MSR shape-logs (that is 0 in the limit that applies), and the
−h² is the *eigenspace cross-ratio* — a different invariant from the four ζ⁰_j.

THE SHARPENED WALL (honest). The genuine MSR regular part (Garoufalidis-Kashaev eq A.17) carries the
torsion factor D(ζ) = ∏_{k=1}^{N-1}(1−ω^{ζ+k})^{k/N}, which lives at q = ω a root of unity (N→∞) —
the FIBRE regime — whereas g₂ is evaluated at the real substrate q₀ (the ARCHIMEDEAN regime). Closing
r rigorously needs the fibre→archimedean (τ-functor) transfer of the pinched regular part, not a
further evaluation at real q₀. Per §2e, scanning dilog forms/shapes to hit +0.87% is refused.

EXPLORATORY — audit + witness only. scope-(a); nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
Q0_STR = "1.10997859555733471"   # muon-canonical (computations/ layer)
TWO_PI_I = 2 * mp.pi * mp.mpc(0, 1)


def lifted_L(z: mp.mpc) -> mp.mpc:
    """MSR eq (A.15): the lifted dilogarithm L(ζ⁰,ζ¹) with the standard flattening from (A.8),
    principal branches (Im log ∈ (−π,π])."""
    z0 = mp.log(z) / TWO_PI_I                 # e^{2πiζ⁰} = z
    z1 = -mp.log(1 - z) / TWO_PI_I            # e^{−2πiζ¹} = 1 − z
    return mp.polylog(2, z) / TWO_PI_I + mp.pi * mp.mpc(0, 1) * z0 * z1 + z0 * mp.log(1 - z)


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    h = q0 - 1 / q0
    z = -h ** 2

    # --- RESULT 1: full lifted dilog + exact closed form Re L = ¼ ln(1+h²) ---
    L = lifted_L(z)
    ReL_closed = mp.log(1 + h ** 2) / 4
    closed_form_ok = abs(L.real - ReL_closed) < mp.mpf("1e-30")
    z0 = mp.log(z) / TWO_PI_I
    re_zeta0_is_half = abs(z0.real - mp.mpf("0.5")) < mp.mpf("1e-40")

    g2_candidate = mp.log(1 + h ** 2) / h ** 2        # = Re L / (h²/4)
    r_candidate = g2_candidate - 1
    r_target = mp.mpf("0.00865")

    # symbolic confirmation of the closed form: Re L = ¼ ln(1+h²) as a power series
    hs = sp.symbols("h", positive=True)
    zs = -hs ** 2
    Li2s = sum(zs ** n / sp.Integer(n) ** 2 for n in range(1, 8))
    z0s = (sp.log(hs ** 2) + sp.I * sp.pi) / (2 * sp.pi * sp.I)
    z1s = -sp.log(1 + hs ** 2) / (2 * sp.pi * sp.I)
    Ls = Li2s / (2 * sp.pi * sp.I) + sp.pi * sp.I * z0s * z1s + z0s * sp.log(1 - zs)
    ReLs = sp.series(sp.re(Ls), hs, 0, 9).removeO()
    matches_quarter_ln = sp.simplify(ReLs - sp.series(sp.log(1 + hs ** 2) / 4, hs, 0, 9).removeO()) == 0

    # --- RESULT 3: pinch degeneracy — all four ζ⁰_j = 0 at the standard pinch ⇒ e₂ = 0 ---
    b1, b2, b1p, b2p, mu1, mu2, eps, bb = sp.symbols("b1 b2 b1p b2p mu1 mu2 eps bb")
    z0map = {
        "r": eps * (b2p - b1),
        "t": eps * (b2 - b1 - mu1),
        "l": eps * (b2 - b1p + mu2 - mu1),
        "b": eps * (b2p - b1p + mu2),
    }
    pinch = {b1: bb, b2: bb + mu1, b1p: bb + mu2, b2p: bb}          # §5.2 eq 5.7
    z0_pinched = {k: sp.simplify(v.subs(pinch)) for k, v in z0map.items()}
    Z = list(z0_pinched.values())
    e2_pinched = sp.simplify(sum(Z[i] * Z[j] for i in range(4) for j in range(i + 1, 4)))
    all_zero = all(v == 0 for v in Z)

    result = {
        "R1_full_lifted_dilog_closed_form": {
            "amplitude": "MSR eq (A.15) L(ζ⁰,ζ¹) = Li₂(z)/(2πi) + πi ζ⁰ζ¹ + ζ⁰ log(1−z), flattening (A.8)",
            "shape": "z = −h² (eigenspace cross-ratio, #4345)",
            "Re_zeta0_eq_half": bool(re_zeta0_is_half),
            "note_frames": "Re ζ⁰ = ½ EXACTLY — reconciles the corpus's two trefoil frames (z=½ and −h²)",
            "Re_L_numeric": mp.nstr(L.real, 15),
            "Re_L_closed_form": "¼ ln(1+h²) = " + mp.nstr(ReL_closed, 15),
            "closed_form_verified_30dps": bool(closed_form_ok),
            "closed_form_verified_symbolic": bool(matches_quarter_ln),
            "Im_L_branch_dependent": mp.nstr(L.imag, 8) + " (carries ln h — flattening-branch ambiguity)",
        },
        "R2_refutation_scope_a": {
            "g2_candidate": mp.nstr(g2_candidate, 12) + "  (= ln(1+h²)/h², normalised to g₂_leading=1)",
            "r_candidate": mp.nstr(r_candidate, 8),
            "r_target": mp.nstr(r_target, 8),
            "verdict": "WRONG SIGN and ~2.4× magnitude (got −2.12%, target +0.87%). The full lifted "
                       "dilog (correct amplitude) is FURTHER from target than the bare Li₂ (−1.07%). "
                       "The eigenspace-shape lifted-dilog route, ALONE, does not reproduce r.",
            "scope": "(a) scope-limited negative — constrains magnitudes/combinations, NOT ingredients. "
                     "No proved invariant excludes the lifted dilog from a closure; this is not (b).",
            "no_scan": "one principled evaluation; dilog forms/shapes NOT scanned to hit +0.87% (§2e).",
        },
        "R3_pinch_degeneracy": {
            "standard_pinch_zeta0": {k: str(v) for k, v in z0_pinched.items()},
            "all_four_vanish": bool(all_zero),
            "octahedral_e2_at_pinch": str(e2_pinched),
            "lean": "QOU/MassTheory/PinchedOctahedronDegenerate.lean (e2_pinch, sorry-free)",
            "meaning": "deuteron σ₁³ = trefoil (torus knot) ⇒ crossings PINCHED (§5.2 Def 5.3); at the "
                       "standard pinch (eq 5.7) all four MSR shape-logs = 0, so the octahedral e₂ = 0. "
                       "The 'four-shape octahedron' has NO four-distinct-shape content at the pinched "
                       "trefoil; g₂ is NOT the naive octahedral e₂ of the ζ⁰_j. The −h² is the "
                       "eigenspace cross-ratio, a different invariant.",
        },
        "sharpened_wall": {
            "torsion_factor": "the genuine MSR regular part (Garoufalidis-Kashaev A.17) carries "
                              "D(ζ)=∏_{k=1}^{N-1}(1−ω^{ζ+k})^{k/N}, a q=root-of-unity (N→∞) object",
            "regime_gap": "D(ζ) lives in the FIBRE (root of unity); g₂ is at the real substrate q₀ "
                          "(ARCHIMEDEAN). Closing r needs the fibre→archimedean (τ) transfer of the "
                          "pinched regular part — NOT a further real-q₀ evaluation.",
            "scope": "scope-(a): sharpens the frontier (#4347) from 'compute the 4-shape octahedron' "
                     "to 'the 4-shape object degenerates at the pinch; the real object is the pinched "
                     "regular part in the root-of-unity regime, needing the τ transfer'.",
        },
    }

    payload = {
        "computation": "geometric-qdilog-lifted-amplitude",
        "description": ("The ONE principled evaluation of the FULL McPhail-Snyder–Reshetikhin lifted "
                        "dilogarithm L(ζ⁰,ζ¹) (2509.02354 eq A.15, the flattened-tetrahedron complex "
                        "Chern-Simons invariant) on the pinned trefoil eigenspace shape z=−h² — fixing "
                        "the prior frontier probe's Li₂-only omission. RESULT: Re L = ¼ ln(1+h²) "
                        "exactly (verified 30 dps + symbolic; Re ζ⁰=½ reconciles the corpus's z=½ and "
                        "−h² frames); normalised g₂ = ln(1+h²)/h² ≈ 0.9788 ⇒ r ≈ −2.12%, WRONG SIGN and "
                        "~2.4× vs the measured +0.87% — the correct amplitude is FURTHER from target "
                        "than the bare Li₂ (−1.07%). REFUTES the eigenspace-shape lifted-dilog route "
                        "(scope-(a), not (b)). STRUCTURAL (Lean-proved): at the standard pinch all four "
                        "MSR shape-logs = 0, so the octahedral e₂ = 0 — the four-shape octahedron "
                        "degenerates at the pinched trefoil; the −h² is the eigenspace cross-ratio, not "
                        "an MSR shape. Sharpened wall: the genuine regular part (D(ζ) torsion) is a "
                        "root-of-unity object; closing r needs the fibre→archimedean τ transfer. "
                        "scope-(a), audit-only, nothing wired; no scan (§2e)."),
        "audit_only": True,
        "tier": "one principled full-amplitude evaluation (exact closed form) + Lean-proved structural "
                "degeneracy + sharpened wall; no fit, no scan",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the exact residual r = g₂ − 1",
            "paper": "library/arxiv-2509.02354v2/2509.02354v2.pdf eq (A.15) lifted dilog, (A.17) regular part, §5.2 pinch",
            "lean": "QOU/MassTheory/PinchedOctahedronDegenerate.lean (e2_pinch)",
            "builds_on": "#4345 (shape −h² from rep), #4339 (g₂_leading=1), #4347 (frontier: bare Li₂)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
            "no_scan": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "geometric-qdilog-lifted-amplitude", payload,
        script_path=__file__, engine="mpmath+sympy", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("ReL_closed_form_quarter_ln", computed=str(bool(closed_form_ok)), expected="True")
    wb.add_assertion("Re_zeta0_is_half", computed=str(bool(re_zeta0_is_half)), expected="True")
    wb.add_assertion("pinch_e2_zero", computed=str(e2_pinched), expected="0")
    out = wb.save(extra={"auditOnly": True})

    print("=== Geometric quantum-dilog lifted amplitude for the deuteron r ===")
    print(f"R1  full lifted dilog on z=−h²:  Re L = {mp.nstr(L.real,12)}  =  ¼ln(1+h²) "
          f"[closed form verified: {closed_form_ok} / symbolic: {matches_quarter_ln}]")
    print(f"    Re ζ⁰ = ½ exactly: {re_zeta0_is_half}  (reconciles the z=½ and −h² frames)")
    print(f"R2  g₂_candidate = ln(1+h²)/h² = {mp.nstr(g2_candidate,10)}  ⇒  r = {mp.nstr(r_candidate,6)} "
          f"(target +{mp.nstr(r_target,4)})")
    print(f"    REFUTED (scope-a): wrong sign & ~2.4× magnitude; correct amplitude is FURTHER from "
          f"target than the bare Li₂ (−1.07%). No scan (§2e).")
    print(f"R3  standard-pinch ζ⁰_j = {[str(v) for v in Z]}  (all zero: {all_zero})  ⇒  octahedral "
          f"e₂ = {e2_pinched}")
    print(f"    ⇒ the four-shape octahedron DEGENERATES at the pinched trefoil (Lean: e2_pinch). g₂ is "
          f"NOT the naive octahedral e₂; −h² is the eigenspace cross-ratio.")
    print("WALL (sharpened): the genuine regular part (D(ζ) torsion) is a root-of-unity object; "
          "closing r needs the fibre→archimedean τ transfer, not a further real-q₀ evaluation.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
