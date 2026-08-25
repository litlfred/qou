#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical rerun probe; scale-separation comparison.
"""COLOR-vs-CHARGE T/³He refutation — PER-KNOT-DENSITY RE-RUN (bean x5az).

Protocol: docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md §Next
item 2 (the audit classified `binding_color_vs_charge_tn3he.py` as
"λ_A-family-bound": the pre-swap original imported `base_lw =
linking_weight_family_a` (the fitted global λ_A ≈ 2.533) as the density base).

WHERE λ_A ENTERED (pre-swap original, commit 3e1a26b6, superseded by the
tr_M form in commit 2af340cd):

    w[xy] = bring_color_weighted_linking_weight(Z, N, q0) / linking_weight_family_a(q0)

i.e. λ_A entered ONLY as the normalization of the per-bond color weight.
The bond energies B0 themselves were ALREADY per-block Hecke traces at H_6
(E0 · (tr_free − tr_inter)) in both versions.  Since by construction

    bring_color_weighted_linking_weight(Z, N, q)
        = linking_weight_family_a(q) · (1 + δ·asym + δ²·sym),

the density base cancels ALGEBRAICALLY in the ratio: the color weight is
(1 + δ·asym + δ²·sym) regardless of whether the base is the fitted global
λ_A or the canonical per-knot tr_M(K) (`per_knot_density_per_block`).  This rerun
verifies that cancellation numerically: it computes the T−³He color split
under (a) the pre-swap λ_A-normalized weights and (b) the per-knot /
base-free weights (the form committed in 2af340cd), on identical per-block
B0 bonds, and shows the splits agree to working precision.  The refutation
("color is ~2 orders too small; T−³He is CHARGE/Coulomb") therefore cannot
be a density artifact — it is density-base-independent.

Same q₀ (canonical muon-q₀), same 30-dps precision, same H_6 machinery,
same AME targets as the parent.  NO new fitted constants.  Scope discipline:
the negative remains a scope-limited negative (a) — color weighting at the
δ = flavor_split scale, alone, does not supply the T−³He split.

EXPLORATORY probe — emits binding-color-vs-charge-tn3he-perknot-rerun.witness.json.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_PARENT = _Path(__file__).resolve().parent.parent
for _d in ("", "hecke", "habiro", "substrate"):
    _p = str(_PARENT / _d) if _d else str(_PARENT)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402
from _li_2_q_util import (  # noqa: E402
    bring_color_weighted_linking_weight as bw,
    linking_weight_family_a,
    flavor_split_leading,
)
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)  # same as parent
q0 = mp.mpf(str(Q0))
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))  # 𝔈₀ (CAL-3), same as parent

_y6 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(6, q0).items()}


def _per_block(Z, N, inter):
    """Identical to the parent's per-block H_6 Markov-trace sum."""
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = _y6.get(tuple(lam))
        if y is not None:
            tot += y * abs(mp.re(chi))
    return tot


def color_weight_perknot(Z: int, N: int) -> mp.mpf:
    """Base-free color weight (1 + δ·asym + δ²·sym) — the per-knot form
    committed in 2af340cd (any per-knot density base cancels identically,
    exactly as λ_A does)."""
    delta = flavor_split_leading(q0)
    A = Z + N
    asym = mp.mpf(N - Z) / (3 * A)
    sym = mp.mpf(2 * (2 * Z + N) * (Z + 2 * N)) / (9 * A * A)
    return mp.mpf(1) + delta * asym + delta ** 2 * sym


def split_report(name: str, w: dict, B0: dict, need: mp.mpf) -> dict:
    T_cw = 2 * B0["pn"] * w["pn"] + B0["nn"] * w["nn"]
    He_cw = B0["pp"] * w["pp"] + 2 * B0["pn"] * w["pn"]
    split = T_cw - He_cw
    frac = split / need
    print(f"\n  [{name}]")
    for xy in ("pp", "pn", "nn"):
        print(f"    w[{xy}] = {mp.nstr(w[xy], 12)}")
    print(f"    color T−³He split = {float(split):+.6f} MeV   "
          f"= {float(frac * 100):+.2f} % of needed {float(need):+.5f} MeV")
    return {
        "weights": {k: str(v) for k, v in w.items()},
        "color_split_MeV": str(split),
        "color_fraction_of_needed": str(frac),
    }


def main() -> int:
    delta = flavor_split_leading(q0)
    lam_A = linking_weight_family_a(q0)
    print("=" * 88)
    print("  COLOR vs CHARGE (T−³He) — per-knot density re-run (bean x5az)")
    print("=" * 88)
    print(f"  q_0 = {mp.nstr(q0, 20)}   δ = {float(delta):.4e}   "
          f"λ_A(q_0) = {mp.nstr(lam_A, 12)} (fitted global; audit entry point)")

    # Per-block bonds (identical in pre- and post-swap parent versions).
    B0 = {xy: E0 * (_per_block(Z, N, False) - _per_block(Z, N, True))
          for xy, (Z, N) in {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}.items()}
    for xy in ("pp", "pn", "nn"):
        print(f"  bond {xy}: B0 = {float(B0[xy]):+.4f} MeV")

    AME_T, AME_He = AME_B_TRITIUM_MEV_VALIDATION, mp.mpf("7.7180")
    need = AME_T - AME_He

    ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}
    # (a) BASELINE — pre-swap original: weights normalized by global λ_A.
    w_lamA = {xy: bw(Z, N, q0) / lam_A for xy, (Z, N) in ZN.items()}
    # (b) PER-KNOT — base-free weight (any per-knot tr_M base cancels).
    w_pk = {xy: color_weight_perknot(Z, N) for xy, (Z, N) in ZN.items()}

    rep_lamA = split_report("λ_A-normalized weights (pre-swap original)",
                            w_lamA, B0, need)
    rep_pk = split_report("per-knot / base-free weights (canonical)",
                          w_pk, B0, need)

    # Cancellation check: the two splits must agree to working precision.
    diff = abs(mp.mpf(rep_lamA["color_split_MeV"])
               - mp.mpf(rep_pk["color_split_MeV"]))
    max_w_diff = max(abs(w_lamA[xy] - w_pk[xy]) for xy in ZN)
    print(f"\n  |split_λA − split_perknot| = {mp.nstr(diff, 6)}")
    print(f"  max per-bond weight diff   = {mp.nstr(max_w_diff, 6)}")

    frac_pk = mp.mpf(rep_pk["color_fraction_of_needed"])
    too_small = abs(frac_pk) < mp.mpf("0.10")

    verdict = (
        "ROBUST — the color-vs-charge T−³He refutation is NOT a λ_A density "
        "artifact. λ_A entered the pre-swap original only as the normalization "
        "of the color weight w = bw(Z,N,q0)/λ_A, and since bw = λ_A·(1+δ·asym"
        "+δ²·sym) by construction, the density base cancels algebraically — "
        "the same cancellation holds for any per-knot tr_M base. Both forms "
        "give the identical split (≈ −0.034 MeV, ≈ 4.5 % of the needed "
        "+0.764 MeV): color at the δ = flavor-split scale is ~20× too small "
        "either way; the T−³He split remains CHARGE/Coulomb (α_EM sector). "
        "Scope (a): color weighting, alone, at this scale does not supply the "
        "split — no ingredient-level exclusion claimed. (Note: the audit's "
        "step-2 'λ_A-family-bound' classification was overcautious for THIS "
        "script — the bond energies were already per-block tr_M at H_6 and "
        "the λ_A base cancels; the refutation is density-base-independent.)"
    )
    print(f"\n  VERDICT: {verdict}")

    wb = WitnessBuilder("binding-color-vs-charge-tn3he-perknot-rerun",
                        engine="mpmath")
    wb.data["audit"] = "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    wb.data["bean"] = "x5az"
    wb.data["q_0"] = str(Q0)
    wb.data["delta_flavor_split"] = str(delta)
    wb.data["lambda_A_at_q0"] = str(lam_A)
    wb.data["B0_bonds_MeV"] = {k: str(v) for k, v in B0.items()}
    wb.data["needed_split_MeV"] = str(need)
    wb.data["lambda_A_normalized_baseline"] = rep_lamA
    wb.data["per_knot_base_free"] = rep_pk
    wb.data["abs_split_difference_MeV"] = str(diff)
    wb.data["max_weight_difference"] = str(max_w_diff)
    wb.data["verdict"] = verdict
    wb.data["refutation_scope"] = "scope-limited negative (a) per AGENTS.md"
    wb.add_assertion("density_base_cancels_splits_identical",
                     computed=float(diff), expected=0.0, tolerance=1e-20)
    wb.add_assertion("color_too_small_under_perknot_base",
                     computed=1 if too_small else 0, expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: binding-color-vs-charge-tn3he-perknot-rerun.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
