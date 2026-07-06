"""binding_depth_stratified_derived_alpha_probe.py — falsifiability probe:
does the FRAMEWORK-DERIVED H_3 α_k assignment improve the depth-stratified
binding tower?

CONTEXT (2026-07-02 Step-9b gap survey, docs/workplans/2026-07-02-step9b-
gap-approaches.md). The production tower (binding_depth_stratified*.py)
uses the empirical assignment

    α_0 = α_1 = α_3 = 1,  α_2 = z²,  α_{k≥4} = m_e·8G
    (canonical_status = "canonical-with-empirical-assignment")

but the framework's own Markov-pairing derivation α_k = tr_M(r_k)
(prop:alpha-k-derivation-procedure; explicit-alpha-k-h3.md; machine chains
alpha-k-h3-{0..3}.derivation.json) gives at H_3:

    α_0 = 1,  α_1 = 0,  α_2 = z²,  α_3 = h·z² + z = z(1 + q^{1/2} − q^{−1/2})

i.e. the production tower silently overrides two of the four derived
values. This probe evaluates the SAME Φ_k pipeline (LR-decomposed free
chi, cached atom chi witnesses — imports binding_depth_stratified_lr)
under both assignments and reports the 4-atom ratio table + max/min
variance for each.

HYPOTHESIS CLASS (formalize-first §3.3: cheap + decisive, so run it):
H-DA: "the tower's undershoot is (partly) caused by the empirical
assignment overriding the derived α_1, α_3." Either outcome is a
permanent audit datum:
  - derived assignment improves ⇒ the empirical override was a bug;
  - derived assignment degrades ⇒ scope-limited negative — the derived
    H_3 α_k, extended by partition-depth to H_{3A} and inserted into
    the additive tower ALONE, does not close the undershoot (consistent
    with the "no A-scale slot" structural diagnosis in
    docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md).

NOTE the extension caveat: the derivation lives at H_3 (GB-filtration
depth of reduced words); reusing its values at partition-depth k of
H_{3A} is itself a hypothesis, recorded as such in the witness. The
α_{k≥4} = m_e·8G plateau is kept in both assignments (the derivation
supplies no k≥4 values).

Exploratory probe — audit-only witness, NOT wired into production.

Ref: prop:alpha-k-derivation-procedure
Ref: prop:plancherel-term-7-formulation
Ref: docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import mpmath as mp

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from q_parameter import Q as Q0
from binding_depth_stratified_lr import (
    B_AME, ZN, load_chi_dict, free_chi_for_atom, phi_k_from_dict,
)


def alpha_k_production(k: int) -> mp.mpf:
    """Production empirical assignment (binding_depth_stratified_lr.alpha_k)."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * mp.catalan


def alpha_k_derived(k: int) -> mp.mpf:
    """Framework-derived H_3 assignment α_k = tr_M(r_k) for k ≤ 3
    (explicit-alpha-k-h3.md): α_0=1, α_1=0, α_2=z², α_3=h·z²+z.
    k≥4 keeps the production m_e·8G plateau (no derived value exists)."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    h = Q0 - 1 / Q0
    if k == 0:
        return mp.mpf(1)
    if k == 1:
        return mp.mpf(0)
    if k == 2:
        return z_mark ** 2
    if k == 3:
        return h * z_mark ** 2 + z_mark
    return mp.mpf(str(M_E_MEV)) * 8 * mp.catalan


ASSIGNMENTS = {
    "production_empirical": alpha_k_production,
    "derived_h3_markov_pairing": alpha_k_derived,
}


def evaluate(alpha_fn) -> dict:
    out = {}
    for atom in ("D", "T", "3He", "4He"):
        Z, N = ZN[atom]
        n_strands, chi_atom = load_chi_dict(atom)
        chi_free = free_chi_for_atom(atom)
        chi_atom_full = {lam: chi_atom.get(lam, mp.mpf(0))
                         for lam in chi_free.keys()}
        B = mp.mpf(0)
        per_depth = {}
        for k in range(n_strands):
            delta = (phi_k_from_dict(chi_free, n_strands, k)
                     - phi_k_from_dict(chi_atom_full, n_strands, k))
            ak = alpha_fn(k)
            B += ak * delta
            if mp.fabs(delta) > mp.mpf("1e-12"):
                per_depth[k] = {"alpha_k": fmt(ak), "delta_phi": fmt(delta),
                                "contrib": fmt(ak * delta)}
        ratio = B / B_AME[atom]
        out[atom] = {
            "Z": Z, "N": N, "A": Z + N,
            "B_MeV": fmt(B), "B_AME_MeV": fmt(B_AME[atom]),
            "ratio_pred_over_AME": float(ratio),
            "per_depth": per_depth,
        }
    return out


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified-derived-alpha-probe",
                             output_dir=HERE)
    builder.set_description(
        "Falsifiability probe: depth-stratified tower under the "
        "production empirical α_k assignment (α_1=α_3=1) vs the "
        "framework-derived H_3 Markov-pairing assignment (α_1=0, "
        "α_3=h·z²+z per prop:alpha-k-derivation-procedure). Same Φ_k "
        "pipeline (LR free chi + cached atom chi). Audit-only; not "
        "wired. Extension of H_3 GB-depth values to H_{3A} "
        "partition-depth is itself a recorded hypothesis."
    )
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    h = Q0 - 1 / Q0
    builder.add_parameter("alpha_3_derived", fmt(h * z_mark ** 2 + z_mark))
    builder.add_parameter("alpha_1_derived", "0")

    summary = {}
    for name, fn in ASSIGNMENTS.items():
        res = evaluate(fn)
        ratios = [abs(r["ratio_pred_over_AME"]) for r in res.values()]
        mom = max(ratios) / min(ratios) if min(ratios) > 0 else float("inf")
        summary[name] = {
            "per_atom": res,
            "ratios": {a: r["ratio_pred_over_AME"] for a, r in res.items()},
            "max_over_min_abs": float(mom),
        }
        print(f"\n== {name} ==")
        for a, r in res.items():
            print(f"  {a:<5} B={float(mp.mpf(r['B_MeV'])):>9.4f}  "
                  f"ratio={r['ratio_pred_over_AME']:>7.4f}")
        print(f"  max/min |ratio| = {mom:.4f}")

    prod = summary["production_empirical"]
    der = summary["derived_h3_markov_pairing"]
    improved_variance = der["max_over_min_abs"] < prod["max_over_min_abs"]
    improved_closure = all(
        abs(1 - der["ratios"][a]) < abs(1 - prod["ratios"][a])
        for a in der["ratios"]
    )
    if improved_variance and improved_closure:
        verdict = ("DERIVED ASSIGNMENT IMPROVES both variance and closure — "
                   "the empirical override (α_1=α_3=1) was masking the "
                   "derived structure; escalate to production review.")
    elif improved_variance or improved_closure:
        verdict = ("MIXED — derived assignment improves "
                   + ("variance" if improved_variance else "closure")
                   + " only; scope-limited: neither assignment closes the "
                   "additive tower (consistent with the no-A-slot diagnosis).")
    else:
        verdict = ("SCOPE-LIMITED NEGATIVE — the derived H_3 α_k, extended "
                   "by partition-depth and inserted into the additive tower "
                   "alone, does not improve the undershoot. Constrains this "
                   "combination only; does NOT exclude the derived α_k as "
                   "an ingredient of a different (multiplicative / A-scaled) "
                   "assembly.")
    print(f"\nVerdict: {verdict}")

    builder.add_data("assignments", summary)
    builder.add_data("derived_improves_variance", improved_variance)
    builder.add_data("derived_improves_closure_all_atoms", improved_closure)
    builder.add_data("verdict", verdict)
    builder.add_assertion(
        "production_baseline_reproduced_D",
        computed=prod["ratios"]["D"],
        expected=0.2728,
        tolerance=0.01,
        unit="B_pred/B_AME (D)",
        source="binding-depth-stratified-rust.witness.json regen 2026-06-22",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
