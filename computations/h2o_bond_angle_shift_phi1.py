#!/usr/bin/env python3
"""
H₂O bond-angle shift from the Markov TRACE (not |Φ₁|).

Content block: prop:h2o-bond-angle-shift
    E(θ) = a(θ−θ₀)² + b·θ,   θ_min = θ₀ − b/(2a),
    θ₀ = arccos(−1/3) ≈ 109.47° (tetrahedral; def:tetrahedral-hbond-directions).

WHY THIS REDO (owner correction, 2026-06-09)
--------------------------------------------
The earlier probe scored each sub-braid by Φ₁ = Σ_gen log|v| — an
ABSOLUTE-VALUE, per-generator sum. That makes Φ₁ a *generator-count*
functional: the 4-strand bonding pair accrues more log|v| terms than the
3-strand lone pair, so |w_bond| > |w_lone| — the WRONG sign for VSEPR
(lone pairs must repel MORE than bond pairs), and the downstream
repulsion map then OPENED the angle (~140°, a +35 % miss).

The owner's fix: do NOT use |v|; use the (checked) Markov trace tr_M,
"so additional structure is not lost." tr_M is the LINEAR functional
    tr_M(x) = Σ_i nf(x)_i · TR_M_i        (pyhecke.gram; TR_M is the
              Markov–Ocneanu–Wenzl weight vector on the H₃(q) NF basis)
— NOT a magnitude. It keeps the sign and the q-commutator structure that
|·| discards.

THE STRUCTURAL RESULT  (Tier 1 — q-exact SIGN)
----------------------------------------------
Two canonical substrate elements (NOT fitted choices):
  • lone pair = intra-block electron pair  e⁻ = σ₀σ₁σ₀
        (the canonical electron-pair element, gram.NF_BASIS[5] = "e⁻"),
        tr_M(e⁻) = h·z² + z.
  • bond pair = cross-block O–H σ-bond = the bonding generator σ
        (water .lean: "bonding (cross-block) generators … = the O–H
        σ-bonds"),  tr_M(σ) = z.
Hence
    Δtr := tr_M(lone) − tr_M(bond) = h·z²  >  0     for every q > 1
           (h = q − q⁻¹ > 0,  z = 1/(q^{½}+q^{−½}) > 0).
A positive lone-pair trace excess ⇒ b > 0 ⇒ θ_min < θ₀: the angle
NARROWS below tetrahedral. CORRECT SIGN — the opposite of the |v| probe.

The entire effect is the h·z² term: precisely the structure |·| throws
away. It is the q-commutator weight of σ₀² = h·σ₀ + 1 carried by the
intra-block pair e⁻ and absent from the bare cross-block crossing σ.
That is the "additional structure" the owner flagged.

MAGNITUDE  (Tier 2 — order-of-magnitude only, NOT fitted)
---------------------------------------------------------
Fractional lone-pair trace excess:  Δtr / tr_M(bond) = h·z² / z = h·z.
At q₀ this is ≈ 0.104 (10.4 %).  The observed fractional angular shift is
(109.47 − 104.5)/109.47 ≈ 0.045 (4.5 %).  Same sign, same order of
magnitude.  Converting the trace excess into the energy coefficient b,
and then into degrees, needs the angular stiffness a (the curvature of
the tetrahedral well) — which is GEOMETRIC, not a trace output. So the
exact 4.97° is deliberately NOT claimed here; that would be a fit
(cf. CLAUDE.md "do not fit a seventh ansatz" / formalize-first). This
probe delivers the q-exact SIGN and the order of magnitude, and isolates
a (well stiffness) as the one remaining geometric input.
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[1]  # …/computations → repo root
for _p in (str(_HERE),
           str(_ROOT / "tools" / "pyhecke" / "python"),
           str(_ROOT / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401  — substrate modules live in substrate/
from pyhecke.gram import z, nf_of_word, nf_tr        # the checked trace
from q_parameter import Q as q0, Q_INV as qi, HA as h  # h = q − q⁻¹
from witness_base import WitnessBuilder
from experimental_constants import (
    ANGLE_H2O_HOH_DEG, ANGLE_H2O_TETRAHEDRAL_DEG,  # comparison targets only
)

TOL = 1e-12

# Canonical substrate elements (NOT fits — both are named substrate objects):
LONE_WORD = (0, 1, 0)   # e⁻ = σ₀σ₁σ₀, intra-block electron pair (gram.NF_BASIS[5])
BOND_WORD = (0,)        # σ, cross-block O–H bonding generator (water.lean)


def main() -> None:
    print("=" * 70)
    print("H₂O BOND-ANGLE SHIFT FROM THE MARKOV TRACE (not |Φ₁|)")
    print("=" * 70)
    print(f"q₀ = {q0:.10f}   z = {z:.10f}   h = {h:.10f}")
    print()

    tr_lone = float(nf_tr(nf_of_word(LONE_WORD)))   # h z² + z
    tr_bond = float(nf_tr(nf_of_word(BOND_WORD)))   # z
    delta_tr = tr_lone - tr_bond                    # h z² (lone-pair excess)
    closed_form = float(h * z ** 2)                 # predicted Δtr
    frac_excess = delta_tr / tr_bond                # h z

    theta0 = ANGLE_H2O_TETRAHEDRAL_DEG
    theta_obs = ANGLE_H2O_HOH_DEG
    frac_shift_obs = (theta0 - theta_obs) / theta0

    print(f"  tr_M(lone = e⁻ = σ₀σ₁σ₀) = {tr_lone:.10f}   (= h z² + z)")
    print(f"  tr_M(bond = σ, O–H)      = {tr_bond:.10f}   (= z)")
    print(f"  Δtr = tr_M(lone) − tr_M(bond) = {delta_tr:.10f}")
    print(f"      closed form  h z²         = {closed_form:.10f}   "
          f"(match: {abs(delta_tr - closed_form) < TOL})")
    print()
    print(f"  SIGN: Δtr {'>' if delta_tr > 0 else '≤'} 0  ⇒  b "
          f"{'>' if delta_tr > 0 else '≤'} 0  ⇒  θ_min "
          f"{'<' if delta_tr > 0 else '≥'} θ₀  (angle "
          f"{'NARROWS' if delta_tr > 0 else 'does NOT narrow'})")
    print(f"  observed: θ₀={theta0:.2f}° → θ_obs={theta_obs:.1f}°  (narrows ✓)")
    print()
    print(f"  MAGNITUDE (order-of-magnitude, not fitted):")
    print(f"    fractional trace excess  h z = {frac_excess:.4f}  ({100*frac_excess:.1f} %)")
    print(f"    observed angular shift       = {frac_shift_obs:.4f}  ({100*frac_shift_obs:.1f} %)")
    print(f"    → same sign, same order of magnitude; exact ° needs the")
    print(f"      geometric stiffness a (NOT a trace output) — left open.")
    print()

    sign_ok = delta_tr > 0
    closed_ok = abs(delta_tr - closed_form) < TOL

    w = WitnessBuilder("h2o-bond-angle-shift-phi1", engine="python")
    w.set_description(
        "H₂O H–O–H angle shift via the Markov trace tr_M (owner correction: "
        "use the checked trace, not |Φ₁|, so the q-commutator structure is "
        "kept). Lone pair = intra-block electron pair e⁻ = σ₀σ₁σ₀ "
        "(tr_M = h z² + z); bond pair = cross-block O–H σ generator "
        "(tr_M = z). Δtr = h z² > 0 is the lone-pair trace excess that drives "
        "b > 0 ⇒ θ_min < θ₀ (angle narrows below tetrahedral). q-exact SIGN; "
        "magnitude left to the geometric angular stiffness a (not fitted)."
    )
    w.set_content_block("prop:h2o-bond-angle-shift")
    w.add_parameter("q", float(q0))
    w.add_parameter("z", float(z))
    w.add_parameter("h", float(h))
    w.add_data("tr_M_lone_pair_e_minus", tr_lone)
    w.add_data("tr_M_bond_pair_sigma", tr_bond)
    w.add_data("delta_tr_lone_minus_bond", delta_tr)
    w.add_data("delta_tr_closed_form_h_z2", closed_form)
    w.add_data("fractional_trace_excess_hz", frac_excess)
    w.add_data("observed_theta0_deg", theta0)
    w.add_data("observed_theta_hoh_deg", theta_obs)
    w.add_data("observed_fractional_angular_shift", frac_shift_obs)
    w.add_assertion(
        "lone-pair trace exceeds bond-pair trace (Δtr > 0 ⇒ angle narrows)",
        computed=bool(sign_ok),
        expected=True,
        source="tr_M(e⁻) − tr_M(σ) = h z² > 0 for q > 1; correct VSEPR sign "
               "(reverses the |Φ₁| generator-count probe, which gave bond>lone)",
    )
    w.add_assertion(
        "Δtr equals the q-exact closed form h·z²",
        computed=bool(closed_ok),
        expected=True,
        source="tr_M(e⁻)=h z²+z, tr_M(σ)=z; the excess is exactly the σ₀²="
               "h σ₀+1 commutator weight that |·| discards",
    )
    w.add_data(
        "finding",
        "Switching the molecular sub-braid score from Φ₁=Σ log|v| to the "
        "Markov trace tr_M reverses the sign error of the prior H₂O probe. "
        "|v| is a generator-count sum (4-strand bond pair > 3-strand lone "
        "pair → wrong sign → angle opened ~140°); tr_M keeps the h z² "
        "commutator weight of the intra-block electron pair e⁻, giving "
        "tr_M(lone) − tr_M(bond) = h z² > 0 → b > 0 → θ_min < θ₀ (narrows, "
        "correct). q-exact sign + right order of magnitude (h z ≈ 10.4 % vs "
        "observed 4.5 %). The exact degrees need the geometric angular "
        "stiffness a; deliberately not fitted (formalize-first).",
    )
    w.save()
    print("Done. Witness saved (h2o-bond-angle-shift-phi1).")


if __name__ == "__main__":
    main()
