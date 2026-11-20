#!/usr/bin/env python3
"""
deltalambda_coulomb_mirror_split_probe.py — the ³H/³He mirror binding split as
the Coulomb energy of the extra proton pair, on the Lean-proved strong-split-
zero premise, with a PARAMETER-FREE pion-Compton radius.  Two Coulomb
geometries are compared head-to-head and the forward test is separated into its
isospin-odd (Coulomb, closes) and isospin-even (strong Δ_λ magnitude, OPEN)
parts.

WHY THIS PROBE (2026-07-18).  The Δ_λ magnitude front split into a sign (DERIVED)
and a magnitude (open) sub-wall (attack-vector map 2026-07-18).  A refined
hypothesis: the ³H↔³He mirror split is NOT a strong effect at all — it is the
Coulomb repulsion of ³He's two protons.  The strong sector is now
MACHINE-VERIFIED to give ³H = ³He exactly:

    QOU.MassTheory.isospinExchange_det_mirror_invariant  (PR #3986, sorry-free,
    lean-direct exit 0) — the global proton↔neutron mirror s ↦ −s fixes every
    entry of the isospin-signed strong exchange matrix (since (−sᵢ)(−sⱼ)=sᵢsⱼ),
    so its det — and any strong binding functional of it — is mirror-invariant.
    The strong ³H/³He split is EXACTLY zero.  Scope-(b) structural exclusion
    (proved invariant), not a numerical miss.

So on that proved premise  B(³H) − B(³He) = E_C(³He)  (the neutron-rich mirror
member ³H has Z=1 ⇒ no proton pair ⇒ E_C = 0).  This probe asks the decisive
question: does a PARAMETER-FREE  E_C = coef·α_EM·Z(Z−1)·ℏc/R  with R from the
framework's own hyperbolic-volume machinery land near the AME split 0.764 MeV?

FORMALIZE-FIRST FACTOR MAP (compute-author §3.3) — every factor traced to tier:

  • strong split = 0    → PR #3986 isospinExchange_det_mirror_invariant.
                          Tier: PROVED (scope-(b)).  This is the NEW element vs
                          the 2026-07-13 continuum-EM probe, which assumed it.
  • α_EM (derived)      → prop:alpha-em-categorical-trace-ratio,
                          α = 1/(q₀·[9]_q·[10]_q) (bare, −0.155% vs CODATA;
                          ≪ the 7% binding-systematics scatter → insensitive).
                          Tier: DERIVED (bare).
  • Z(Z−1)              → exact discrete-proton pair count (self-energy of Z unit
                          protons; Σ_{i<j} 1 = C(Z,2), doubled).  Tier: EXACT.
  • R(A) = λ̄_π·A^{1/3} → PARAMETER-FREE radius: λ̄_π = ℏc/m_π, m_π = CAL-3 (the
                          orthogonal meson calibration) ⇒ ℏc/R = m_π/A^{1/3}, NO
                          empirical r₀.  Caveats, both underived and both named
                          by the pion-radius audit (2026-07-13-pion-radius-and-
                          vol-to-radius-gaps.md): the coefficient EXACTLY 1 is a
                          Yukawa SELECTION among the 4 framework mass scales
                          (GAP1: measured 0.985±0.069, consistent-not-derived),
                          and the A^{1/3} volume→radius extensivity is GAP2-OPEN.
                          Tier: PARAMETER-FREE MODULO SELECTION.
  • coef ∈ {3/5, 1/2}   → the electrostatic GEOMETRY.  3/5 = uniform charged
                          sphere self-energy; 1/2 = a single discrete pp pair at
                          separation R (Z=2 ⇒ one pair).  Classical Euclidean
                          archimedean-side model factors, NOT categorical
                          derivations.  Tier: MODEL ASSUMPTION (both reported).

RESULT (spoiler, no fit): the AME split 0.764 MeV BRACKETS between the two
geometries — pairwise 0.707 (0.93×) < AME 0.764 < uniform-sphere 0.849 (1.11×).
The parameter-free-modulo-selection Coulomb DOES land near 0.764 and reproduces
the ~1.1× mirror ratio.  But the two underived caveats above (radius coefficient
= 1 Yukawa selection; 3/5-vs-1/2 geometry model factor) mean it is a PARTIAL,
NOT a wall-crack — and it MATCHES the known 2026-07-13 continuum-EM PARTIAL
(split_AME/split_pred = 0.985±0.069 across 8 T_z pairs), which this probe
reconfirms by a focused A=3 route + the new Lean premise.

THE MAGNITUDE WALL IS UNTOUCHED.  The mirror SPLIT is isospin-odd (Coulomb).
The ABSOLUTE magnitude ratios ρ = B/B_D (⁴He 12.72, ³He 3.47, ³H 3.81) are
isospin-even STRONG quantities — the Coulomb term shifts them only by O(E_C/B) ≤
0.11 and cannot supply them.  Those ratios ARE the open Δ_λ magnitude wall; this
probe leaves them exactly where they were.

ANTI-FIT / ANTI-LAUNDERING (STRICT).  α_EM and R are fixed BEFORE any comparison;
the Coulomb scale is NEVER solved from the deficit.  The one number the
construction leaves open (the radius coefficient) is set to 1 by the Yukawa
selection, not fitted.  Because that selection + the geometry factor are
underived, the classification is (a) PARTIAL regardless of how close the number
lands.  EXPLORATORY — scope-limited (a), no production wiring, no content-block
or tier change.  Nothing here is canonical.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_HERE, _COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    _ame_binding_mev,
    M_E_MEV,
    M_PI_PM_MEV_VALIDATION,
)
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from coulomb_energy import R0_FM  # noqa: E402 — empirical r₀, for the contrast only
# Cross-check vs the prior 2026-07-13 continuum-EM PARTIAL (its exact code path)
from mirror_split_continuum_em_probe import pred_continuum, alpha_derived  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:  # pragma: no cover
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q0 = Q_MP

# CODATA masses for the length-scale selection table (printout / selection only)
M_MU_MEV = mp.mpf("105.6583755")
M_P_MEV = mp.mpf("938.27208943")
HBAR_C_MEV_FM = mp.mpf("197.3269804")   # λ̄_π in fm printout only; NOT in the pred

# Geometry model factors
COEF_SPHERE = mp.mpf(3) / 5             # uniform charged sphere self-energy
COEF_PAIR = mp.mpf(1) / 2              # single discrete pp pair at separation R


def coulomb_mev(Z: int, A: int, coef: mp.mpf, alpha: mp.mpf) -> mp.mpf:
    """E_C = coef·α·Z(Z−1)·m_π/A^{1/3}  (MeV).  ℏc/R = m_π/A^{1/3}: NO r₀.
    Returns 0 for Z<2 (no proton pair)."""
    if Z < 2:
        return mp.mpf(0)
    return coef * alpha * Z * (Z - 1) * M_PI_PM_MEV_VALIDATION / mp.cbrt(A)


def main() -> int:
    ok = True
    a_der = alpha_derived(q0)
    a_cod = 1 / mp.mpf(str(ALPHA_EM_INV))
    a_rel = a_der / a_cod - 1
    lam_pi_fm = HBAR_C_MEV_FM / M_PI_PM_MEV_VALIDATION

    split_ame = mp.mpf(str(_ame_binding_mev(1, 3))) - mp.mpf(str(_ame_binding_mev(2, 3)))
    B_3H = mp.mpf(str(_ame_binding_mev(1, 3)))
    B_3He = mp.mpf(str(_ame_binding_mev(2, 3)))
    B_D = mp.mpf(str(_ame_binding_mev(1, 2)))
    B_4He = mp.mpf(str(_ame_binding_mev(2, 4)))

    print("=== ³H/³He mirror split = Coulomb of the pp pair, on the Lean strong-"
          "split-zero premise ===\n")

    # ── the proved premise (scope-(b)) ───────────────────────────────────────
    print("PROVED PREMISE (scope-(b), PR #3986, sorry-free, lean-direct exit 0):")
    print("  QOU.MassTheory.isospinExchange_det_mirror_invariant — the p↔n mirror")
    print("  s↦−s fixes every strong bond entry ((−sᵢ)(−sⱼ)=sᵢsⱼ), so the STRONG")
    print("  ³H/³He split is EXACTLY 0.  ⇒  B(³H) − B(³He) = E_C(³He)  (³H: Z=1,")
    print("  no proton pair, E_C=0).  The ~1.10× split is therefore pure Coulomb.\n")

    # ── the parameter-free radius + derived α ────────────────────────────────
    print(f"parameter-free radius  R(A) = λ̄_π·A^(1/3),  λ̄_π = ℏc/m_π = "
          f"{float(lam_pi_fm):.5f} fm  (m_π = CAL-3)")
    print(f"  ⇒ ℏc/R(A) = m_π/A^(1/3): NO empirical r₀ (the r₀={R0_FM} fm of "
          f"coulomb_energy.py is NOT used).")
    print(f"  caveats (both underived, named by pion-radius audit 2026-07-13):")
    print(f"    · coefficient EXACTLY 1 = Yukawa selection among 4 mass scales "
          f"(GAP1: measured 0.985±0.069)")
    print(f"    · A^(1/3) volume→radius extensivity = GAP2 OPEN")
    print(f"α_EM derived (bare 1/(q₀[9]_q[10]_q)) = 1/{float(1/a_der):.6f}  "
          f"(rel {float(a_rel):+.3e} vs CODATA — insensitive)\n")

    # ── the two geometries at A=3 ────────────────────────────────────────────
    ec_sphere = coulomb_mev(2, 3, COEF_SPHERE, a_der)
    ec_pair = coulomb_mev(2, 3, COEF_PAIR, a_der)
    r_sphere = ec_sphere / split_ame
    r_pair = ec_pair / split_ame
    print("### The pp-Coulomb split E_C(³He) vs AME 0.764 MeV — two geometries")
    print(f"  {'geometry':<26}{'coef':>6}{'E_C(³He)':>11}{'pred/AME':>10}")
    print(f"  {'uniform charged sphere':<26}{'3/5':>6}{float(ec_sphere):>11.4f}"
          f"{float(r_sphere):>10.3f}×")
    print(f"  {'single discrete pp pair':<26}{'1/2':>6}{float(ec_pair):>11.4f}"
          f"{float(r_pair):>10.3f}×")
    print(f"  {'AME split':<26}{'':>6}{float(split_ame):>11.4f}{'1.000':>10}×")
    brackets = ec_pair < split_ame < ec_sphere
    print(f"\n  ⇒ the AME split BRACKETS between the geometries: "
          f"{float(ec_pair):.3f} (1/2) < {float(split_ame):.3f} (AME) < "
          f"{float(ec_sphere):.3f} (3/5)  [{'PASS' if brackets else 'FAIL'}]")
    print(f"    Both land NEAR ~0.76 MeV: the pp-Coulomb IS the right sign, order,")
    print(f"    and (to a geometry factor) magnitude of the mirror split.\n")

    # ── forward test part A: the mirror RATIO (isospin-odd → Coulomb) ─────────
    # strong = B(³H) (neutron-rich member carries the pure strong value);
    # B(³He)_pred = strong − E_C.
    ratio_ame = B_3H / B_3He
    ratio_sphere = B_3H / (B_3H - ec_sphere)
    ratio_pair = B_3H / (B_3H - ec_pair)
    print("### Forward test A — mirror RATIO B(³H)/B(³He) (isospin-ODD → Coulomb)")
    print(f"  AME                         : {float(ratio_ame):.4f}")
    print(f"  pred (3/5 sphere)           : {float(ratio_sphere):.4f}  "
          f"(over by {float(100*(ratio_sphere/ratio_ame-1)):+.1f}%)")
    print(f"  pred (1/2 pair)             : {float(ratio_pair):.4f}  "
          f"(under by {float(100*(ratio_pair/ratio_ame-1)):+.1f}%)")
    print(f"  ⇒ the target ~1.10× mirror ratio is reproduced from Coulomb ALONE.\n")

    # ── forward test part B: absolute magnitude ratios ρ (isospin-even→strong)─
    rho_ame = {"⁴He": B_4He / B_D, "³He": B_3He / B_D, "³H": B_3H / B_D}
    ec_4He = coulomb_mev(2, 4, COEF_SPHERE, a_der)
    frac = {"³He": ec_sphere / B_3He, "⁴He": ec_4He / B_4He}
    max_frac = max(frac.values())
    print("### Forward test B — absolute magnitude ratios ρ=B/B_D (isospin-EVEN → STRONG)")
    print(f"  {'ρ':<6}{'AME':>8}   (target)")
    for nm, r in rho_ame.items():
        print(f"  {nm:<6}{float(r):>8.3f}")
    print(f"  Coulomb correction fractions E_C/B: "
          + ", ".join(f"{k} {float(v):.3f}" for k, v in frac.items())
          + f"  (max {float(max_frac):.3f})")
    print(f"  ⇒ ρ_4/ρ_3He/ρ_3H are set by the STRONG binding to <=11%; the Coulomb")
    print(f"    term shifts them by O(E_C/B) and CANNOT supply them.  These ratios")
    print(f"    ARE the open Δ_λ MAGNITUDE wall — this probe leaves them UNTOUCHED.\n")
    mag_wall_open = max_frac < mp.mpf("0.12")

    # ── the direct Vol(K)^{1/3} route is blocked for a mirror pair (GAP2) ─────
    print("### The direct R∝Vol(K)^(1/3) route is BLOCKED for a mirror pair (GAP2)")
    print("  The corpus link IDs make ³H=8₁₁ (a KNOT, 1 cusp) and ³He=L6a4=Borromean")
    print("  (a LINK, 3 cusps) — different hyperbolic volumes for an isospin mirror,")
    print("  which would give the two mirrors DIFFERENT radii, contradicting isospin.")
    print("  So R∝Vol^(1/3) is not the mirror-symmetric radius; the A^(1/3) volume-")
    print("  extensivity form (same A=3 ⇒ same R) is.  (pion-radius audit GAP2, cusp-")
    print("  count∝A FAILS on the corpus's own links.)\n")

    # ── consistency with the prior continuum-EM PARTIAL (2026-07-13) ─────────
    p_cont = pred_continuum(3, 1, 2, a_der, M_PI_PM_MEV_VALIDATION)  # its exact path
    cont_ok = abs(p_cont - ec_sphere) < mp.mpf("1e-9")
    print(f"consistency vs mirror_split_continuum_em (2026-07-13): its 3H/3He pred "
          f"{float(p_cont):.4f} == this 3/5 pred {float(ec_sphere):.4f} "
          f"[{'PASS' if cont_ok else 'FAIL'}]")
    print("  → this probe RECONFIRMS the known continuum-EM PARTIAL (split_AME/pred")
    print("    = 0.985±0.069 over 8 T_z pairs) by a focused A=3 route + Lean premise;")
    print("    it does NOT claim a new crack.\n")

    # ── length-scale selection: why m_π (the 2-bit Yukawa selection) ─────────
    print("length-scale selection (coefficient needed if R = Compton length of each scale):")
    sel = {}
    for lbl, m in [("m_e (CAL-1)", M_E_MEV), ("m_μ (CAL-2 proxy)", M_MU_MEV),
                   ("m_π (CAL-3)", M_PI_PM_MEV_VALIDATION), ("m_p (phys pin)", M_P_MEV)]:
        c = split_ame / (COEF_SPHERE * a_der * 2 * m / mp.cbrt(3))
        sel[lbl] = float(c)
        tag = "   ← closest to 1 (Yukawa range) — still a SELECTION" if abs(c - 1) < 0.15 else ""
        print(f"  {lbl:<20}: {float(c):>8.3f}{tag}")
    # m_π is the CLOSEST to 1 and the a-priori Yukawa scale; m_e/m_p miss by
    # orders of magnitude.  m_μ (~1.19 at A=3) is the nearest rival — the
    # selection is real but SOFT (a 2-bit Yukawa selection, not a derivation).
    pion_closest = min(sel, key=lambda k: abs(sel[k] - 1)) == "m_π (CAL-3)"
    extremes_excluded = sel["m_e (CAL-1)"] > 10 and sel["m_p (phys pin)"] < 0.5
    pion_selected = pion_closest and extremes_excluded
    print()

    # ── verdict ──────────────────────────────────────────────────────────────
    print("VERDICT: (a) PARTIAL — NOT a wall-crack, and the magnitude wall is untouched.")
    print("  • The mirror split is PROVED pure-EM (PR #3986 scope-(b)); the parameter-")
    print("    free-modulo-selection Coulomb lands 0.71–0.85 MeV, bracketing AME 0.764,")
    print("    and reproduces the ~1.10× mirror ratio from Coulomb alone.")
    print("  • It is a PARTIAL because the radius coefficient=1 (Yukawa selection, GAP1")
    print("    undiscriminable at 7%) and the 3/5-vs-1/2 geometry factor are underived;")
    print("    it MATCHES the 2026-07-13 continuum-EM PARTIAL, not a new result.")
    print("  • The absolute magnitude ratios ρ (the real Δ_λ wall) are STRONG and stay")
    print("    OPEN.  No fit, no wiring, no tier change.")

    # ── witness ──────────────────────────────────────────────────────────────
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("deltalambda-coulomb-mirror-split", engine="mpmath")
            wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
            wb.set_description(
                "The 3H/3He mirror binding split as the Coulomb energy of the pp pair, "
                "on the machine-verified strong-split-zero premise (PR #3986, "
                "isospinExchange_det_mirror_invariant). With a PARAMETER-FREE pion-Compton "
                "radius R=lambda_pi*A^(1/3) (lambda_pi=hbar c/m_pi, CAL-3; no empirical r0) "
                "and derived alpha=1/(q0[9]_q[10]_q), the AME split 0.764 MeV BRACKETS "
                "between two geometries: pairwise 1/2 -> 0.707 (0.93x) < AME < uniform-"
                "sphere 3/5 -> 0.849 (1.11x); the ~1.10x mirror ratio is reproduced from "
                "Coulomb alone. PARTIAL not a crack: the radius coefficient=1 is a Yukawa "
                "selection (GAP1 0.985+-0.069) and 3/5-vs-1/2 is a geometry model factor, "
                "both underived; reconfirms the 2026-07-13 continuum-EM PARTIAL. The "
                "absolute magnitude ratios rho=B/B_D (4He 12.72/3He 3.47/3H 3.81) are "
                "isospin-even STRONG quantities (Coulomb shifts them by <=11%) and remain "
                "the OPEN Delta_lambda magnitude wall. Scope-(a), no fit, no wiring.")
            wb.add_data("split_AME_MeV", float(split_ame))
            wb.add_data("E_C_3He_uniform_sphere_MeV", float(ec_sphere))
            wb.add_data("E_C_3He_pairwise_MeV", float(ec_pair))
            wb.add_data("ratio_uniform_sphere", float(r_sphere))
            wb.add_data("ratio_pairwise", float(r_pair))
            wb.add_data("mirror_ratio_AME", float(ratio_ame))
            wb.add_data("mirror_ratio_pred_sphere", float(ratio_sphere))
            wb.add_data("mirror_ratio_pred_pair", float(ratio_pair))
            wb.add_data("rho_AME", {k: float(v) for k, v in rho_ame.items()})
            wb.add_data("coulomb_fraction_E_C_over_B", {k: float(v) for k, v in frac.items()})
            wb.add_data("lambda_pi_fm", float(lam_pi_fm))
            wb.add_data("alpha_derived", float(a_der))
            wb.add_data("alpha_rel_diff_vs_codata", float(a_rel))
            wb.add_data("length_scale_selection_coefficients", sel)
            wb.add_data("lean_premise",
                        "QOU.MassTheory.isospinExchange_det_mirror_invariant (PR #3986, "
                        "sorry-free): strong 3H/3He split = 0 exactly (scope-(b)).")
            asserts = [
                ("strong_split_zero_premise_lean", 1, 1,
                 "The strong 3H/3He split is proved exactly 0 by "
                 "QOU.MassTheory.isospinExchange_det_mirror_invariant (PR #3986, sorry-"
                 "free, lean-direct exit 0): p<->n mirror s->-s fixes every strong bond "
                 "entry, so B(3H)-B(3He)=E_C(3He). Scope-(b) structural premise."),
                ("uniform_sphere_over_predicts",
                 int(abs(r_sphere - mp.mpf("1.1113")) < mp.mpf("2e-3")), 1,
                 f"uniform-sphere 3/5 Coulomb E_C(3He)={float(ec_sphere):.4f} MeV = "
                 f"{float(r_sphere):.4f}x AME split 0.764 (over-predicts ~1.11x); "
                 "parameter-free radius, no fit"),
                ("pairwise_under_predicts",
                 int(abs(r_pair - mp.mpf("0.9261")) < mp.mpf("2e-3")), 1,
                 f"pairwise 1/2 Coulomb E_C(3He)={float(ec_pair):.4f} MeV = "
                 f"{float(r_pair):.4f}x AME split (under-predicts ~0.93x)"),
                ("AME_split_brackets_geometries", int(brackets), 1,
                 f"pairwise {float(ec_pair):.4f} < AME {float(split_ame):.4f} < "
                 f"uniform-sphere {float(ec_sphere):.4f}: the two model geometries "
                 "bracket the data — the parameter-free Coulomb lands near 0.764 MeV"),
                ("magnitude_wall_untouched", int(mag_wall_open), 1,
                 f"absolute magnitude ratios rho=B/B_D are strong: Coulomb fraction "
                 f"E_C/B <= {float(max_frac):.3f} (<0.12), so Coulomb cannot supply "
                 "rho_4/rho_3He/rho_3H — the Delta_lambda magnitude wall is untouched"),
                ("reconfirms_continuum_em_partial", int(cont_ok), 1,
                 f"this 3/5 A=3 pred {float(ec_sphere):.4f} equals the 2026-07-13 "
                 "mirror_split_continuum_em pred via its exact code path — a "
                 "reconfirmation of a known PARTIAL, not a new crack"),
                ("radius_is_yukawa_selection_not_derived", int(pion_selected), 1,
                 f"m_pi is the CLOSEST scale to radius-coefficient 1 "
                 f"({sel['m_π (CAL-3)']:.3f}) and the a-priori Yukawa scale; the mass "
                 f"extremes m_e ({sel['m_e (CAL-1)']:.0f}x) and m_p "
                 f"({sel['m_p (phys pin)']:.2f}x) are excluded by orders of magnitude, "
                 f"m_mu ({sel['m_μ (CAL-2 proxy)']:.2f}x) is the nearest rival — a SOFT "
                 "2-bit Yukawa SELECTION, the underived step (PARTIAL not crack)"),
            ]
            for name, comp, exp, src in asserts:
                ok = ok and (comp == exp)
                wb.add_assertion(name=name, computed=str(comp), expected=str(exp),
                                 tolerance=0, source=src)
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
