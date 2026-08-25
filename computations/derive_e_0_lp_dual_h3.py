#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation script — solves the
# operator-selection LP at H_3 on the real Hecke Gram + Markov-trace
# data; emits y_0^* as the LP-dual derivation of E_0.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

LP-dual audit at H_3 — y_0^* shadow price is NOT E_0_MeV (negative finding).

Per `prop:operator-selection-lp` / `prop:confinement-lp` strong duality:

    Σ_i t_i x_i^*  =  n_target · y_0^*

The dual variable y_0^* on the net constraint is the marginal
*categorical action* per unit target net. The hypothesis under
test (Workplan 2 Phase 2+ candidate D): is y_0^* · m_e the
structurally-derived E_0 in MeV?

**RESULT: NO.** This script wires the real H_3(q) Gram matrix +
Markov-trace cost vector through the canonical operator-selection LP
(clarabel-MPFR; was scipy.linprog until 2026-08-23) (loaded from
[`gram-matrix-dual.witness.json`](gram-matrix-dual.witness.json),
no fitting). The findings:

  1. For n_target = 1 (proton), the LP minimum over the cone
     x_i ≥ 0 picks x^* = (0,…,0,1) — pure e^- (trefoil 3_1)
     channel — with primal_obj = t_{e^-} = 0.1245 and
     y_0^* = 0.1245. So y_0^* · m_e ≈ 0.064 MeV, NOT the
     4.186 MeV of convention A.

  2. With the unboundedness x_i ≥ -M, the LP slides to a
     signed-coefficient mixed solution with primal_obj ≈ 0
     and y_0^* ≈ 0 — the action is unbounded below.

  3. Neither matches the `prop:confinement-lp` claim that x^* =
     NF(B_3) ≈ (+0.998, -0.010, +0.009, +0.046, -0.044, 0)
     with tr_M(B_3) ≈ 0.999. Verifying the Frobenius positivity
     at the claimed B_3 vector: G[1]·B_3 ≈ +0.509 (NOT tight)
     and G[4]·B_3 also nonzero — so my Gram + B_3 are
     inconsistent with the prop's "active set {σ_0, L_-}" claim.
     Likely cause: a normalization mismatch between
     `gram-matrix-dual.witness.json` and the prop's Gram, OR
     the prop is informal at the level of the worked example
     (the LP optimum is genuinely the cheapest channel, not
     the named B_3 operator).

**Interpretation.** y_0^* is *dimensionless* in cat-units; the
MeV scale comes from OUTSIDE the LP (convention A:
E_0 = m_e c_q^2 ℏ_q = 4.186 MeV per `energy-scale-planck.md`).
The LP-dual is a structural DECOMPOSITION tool — it identifies
which channels are active (y_i^* > 0) and confirms strong
duality — but it does NOT derive E_0 in MeV. The "convention D"
slot in `E_0_CONVENTIONS` should be downgraded from "STRUCTURAL
ANSWER" to "structural decomposition; consumes convention A's
E_0 as the MeV scale".

**No fitting** — all inputs (t_i, G_ij, n_target choices) are
loaded from substrate witnesses; the LP is solved by scipy
the canonical LP with no parameter tuning; the negative finding is honest
exposure.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV  # noqa: E402  (CAL-1)
from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import (  # noqa: E402
    provenance as _provenance,
    solve_operator_selection_lp as _canonical_lp,
)

GRAM_WITNESS = _pb.witness_path("gram-matrix-dual.witness.json", HERE)
# `beta-decay-energy-scale.witness.json` was moved to `_deprecated/` while NINE
# live scripts still read it (this one, `derived_masses`, `meson_mass_from_hecke`,
# `derivation_chain`, `q_beta_predicted`, `derive_m_e_hecke_path_a`, two probes,
# and an audit). The deprecation criteria in `_deprecated/README.md` require
# that nothing live consume the witness, so that move was out of policy — and
# it is the same situation the README already documents for
# `hecke_core_legacy.py`, which was moved BACK OUT for exactly this reason.
#
# `_path_bridge.witness_path` now falls back to `_deprecated/` as a LAST
# resort, so this resolves without a local workaround. Verified 2026-08-23:
# the live and deprecated copies' `nucleon_nf` payloads are identical, so the
# fallback changes no number — it only lets this script run at all. Without it
# the producer could not execute, which is why its witness sat frozen at
# 2026-05-11 carrying a maximally-violated duality certificate for three
# months. Bean `qou/ftuv`.
BETA_DECAY_WITNESS = _pb.witness_path("beta-decay-energy-scale.witness.json", HERE)
OUT = _pb.witness_path("e-0-lp-dual-h3.witness.json", HERE)


def load_h3_data():
    """Load 6-element H_3 NF basis: Markov traces + Gram matrix."""
    with GRAM_WITNESS.open() as fh:
        d = json.load(fh)
    basis_labels = list(d["markov_trace_basis"].keys())
    t = np.array([d["markov_trace_basis"][k] for k in basis_labels], dtype=float)
    G = np.array(d["gram_matrix"], dtype=float)
    assert G.shape == (6, 6), f"expected 6x6 Gram, got {G.shape}"
    return basis_labels, t, G


def load_proton_neutron_nets():
    """Load proton/neutron net values + β-decay Δ(net) from β-decay witness."""
    with BETA_DECAY_WITNESS.open() as fh:
        d = json.load(fh)
    return {
        "proton": d["nucleon_nf"]["proton_net"],
        "neutron": d["nucleon_nf"]["neutron_net"],
        "delta_net": abs(d["hecke_nf_differences"]["delta_net"]),
    }


def solve_operator_selection_lp(t, G, n_target, M_bound=1e3, cone=False):
    """Solve the H_3 operator-selection LP and return primal + dual.

    Primal:
        min   t^T x
        s.t.  Σ x_i = n_target           (eq; dual var y_0)
              G x ≥ 0                     (ineq; dual vars y_i ≥ 0)
              x_i ≥ -M   (or x_i ≥ 0 when `cone`)

    **REWRITTEN 2026-08-23 (bean `qou/ftuv`) to delegate to the canonical
    solver.** This function used to be a local `scipy.optimize.linprog`
    reimplementation carrying the *same name* as
    `pyhecke.lp_dual_solver.solve_operator_selection_lp` — so a reader, or a
    grep-based audit looking for producers on the canonical path, would find
    this and conclude the canonical solver was in use. It was not.

    The reimplementation also had a SIGN ERROR. It took
    ``y_0_star = -eq_marg[0]`` where the canonical solver takes
    ``+eq_marginals[0]``, and in `cone` mode that flipped the shadow price:

        local      primal_obj +0.3753866308623884   y_0_star -0.3753866308623884
                   dual_obj   -0.3753866308623884   duality_gap 0.7507732617247768
        canonical  primal_obj +0.3753866308623884   y_0_star +0.3753866308623884
                   dual_obj   +0.3753866308623884   duality_gap 0.0

    Its own strong-duality check therefore reported a gap equal to TWICE the
    objective — maximally violated — and it recorded that instead of failing.
    Every `results_per_target_cone` entry in the committed witness carries
    `y_0_star = -0.12449094312996863` with `duality_gap ≈ 2 × primal_obj`, in
    a witness whose entire purpose is the LP-dual certificate, and the file
    emits no assertion that would have caught it. `E_0` is derived downstream
    as `y_0_star · m_e`, so the sign flip propagated into an energy.

    Both modes are expressible by the canonical solver, which is why the
    reimplementation was never needed:

        cone=False  →  M_bound = M_bound   (x_i ≥ -M, the prop's form)
        cone=True   →  M_bound = 0.0       (x_i ≥ 0)

    The return shape is kept verbatim so callers are unaffected, including the
    `y_0_star` spelling (the canonical dataclass uses `y0_star`).
    """
    res = _canonical_lp(
        np.asarray(t, dtype=float),
        np.asarray(G, dtype=float),
        float(n_target),
        M_bound=0.0 if cone else float(M_bound),
        # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
        # whether the Rust binary happens to be built.
        backend="clarabel",
    )
    if not res.feasible:
        return {"feasible": False, "status": "infeasible"}

    x_star = np.asarray(res.x_star, dtype=float)
    out = {
        "feasible": True,
        "x_star": [float(v) for v in x_star.tolist()],
        "y_0_star": float(res.y0_star),
        "y_star": [float(v) for v in res.y_star],
        "active_set": list(res.active_set),
        "primal_obj": float(res.primal_obj),
        "dual_obj": float(res.dual_obj),
        "duality_gap": float(res.duality_gap),
        "Gx_at_optimum": [float(v) for v in (np.asarray(G, float) @ x_star).tolist()],
        "n_target": float(n_target),
    }
    # Solver provenance and the full-precision decimals behind the f64 above.
    prov = dict(_provenance(res))
    if "y0_star_str" in prov:
        prov["y_0_star_str"] = prov.pop("y0_star_str")   # match the local spelling
    out.update(prov)
    return out


def main() -> int:
    print("=" * 80)
    print(" LP-dual derivation of E_0 at H_3 (convention D)")
    print("=" * 80)

    basis, t, G = load_h3_data()
    nets = load_proton_neutron_nets()

    print(f"\n  Basis (6 NF): {basis}")
    print(f"  Markov traces t_i = {t.round(6).tolist()}")
    print(f"  Net values (substrate): proton {nets['proton']:.6f}, "
          f"neutron {nets['neutron']:.6f}, |Δ(net)| {nets['delta_net']:.6f}")
    print()

    targets = {
        "proton_net": float(nets["proton"]),
        "neutron_net": float(nets["neutron"]),
        "delta_net_transition": float(nets["delta_net"]),
        "unit_target": 1.0,
    }

    print(f"  {'target name':<22} {'n_target':>10} {'y_0^* (cat)':>14} {'E_0_LP MeV':>14} {'vs A (4.186)':>14} {'active set':<20}")
    print("  " + "─" * 100)

    m_e_f = float(M_E_MEV)
    e0_A = m_e_f / 1.10998 / (1.10998 - 1)
    results = {"signed": {}, "cone": {}}
    for mode_name, cone_flag in [("signed (prop: x_i ≥ -M)", False), ("cone (x_i ≥ 0)", True)]:
        print(f"\n  ── {mode_name} ──")
        print(f"  {'target name':<22} {'n_target':>10} {'y_0^* (cat)':>14} {'E_0_LP MeV':>14} {'vs A (4.186)':>14} {'active set':<20}")
        print("  " + "─" * 100)
        for name, n_t in targets.items():
            r = solve_operator_selection_lp(t, G, n_t, cone=cone_flag)
            key = "cone" if cone_flag else "signed"
            if not r.get("feasible"):
                print(f"  {name:<22}: INFEASIBLE — {r.get('status')}")
                results[key][name] = r
                continue
            y0 = float(r["y_0_star"])
            e0_lp_mev = y0 * m_e_f
            ratio_to_a = e0_lp_mev / e0_A
            active = [basis[i] for i in r["active_set"]]
            print(f"  {name:<22} {n_t:>10.6f} {y0:>+14.6f} {e0_lp_mev:>+14.6f} {ratio_to_a:>+14.4f} {str(active):<20}")
            results[key][name] = r

    # Also try the SDP (PSD) variant if available
    print()
    print("  ──── β-decay Q_β prediction via LP-dual E_0 (cone mode, x ≥ 0) ────")
    delta_net = float(nets["delta_net"])
    codata = 0.78233341
    for name, r in results["cone"].items():
        if not r.get("feasible"):
            continue
        e0_mev = float(r["y_0_star"]) * m_e_f
        q_beta = delta_net * e0_mev
        err_kev = (q_beta - codata) * 1000
        print(f"  {name:<22}: E_0_LP = {e0_mev:+.6f} MeV → Q_β = {q_beta:.6f} MeV (err {err_kev:+.2f} keV)")

    print()
    print("  Convention A reference: E_0 = m_e/(q_0(q_0-1)) ≈ 4.186 MeV")
    print("  Convention A Q_β:       Q_β = |Δ(net)|·E_0 ≈ 0.7836 MeV (err +1.31 keV)")

    out = {
        "computation": "e-0-lp-dual-h3",
        "description": (
            "LP-dual derivation of E_0 at H_3 via the operator-"
            "selection LP per prop:operator-selection-lp. Solves "
            "min Σ t_i x_i s.t. Σx=n_target, Gx≥0 on the real H_3 "
            "Gram + Markov-trace data from gram-matrix-dual.witness."
            "json (no fitting). Reports y_0^* for four substrate-"
            "derived n_target choices: proton net, neutron net, "
            "β-decay transition Δ(net), and unit target. Compares "
            "E_0_LP_dual = y_0^* · m_e against convention A's "
            "single-tick m_e/(q(q-1)) ≈ 4.186 MeV."
        ),
        "auditOnly": "docs/audits/2026-05-10-hbar-q-scaling-audit.md",
        "no_fitting_assertion": (
            "All inputs (t_i, G_ij, n_target choices) loaded from "
            "substrate witnesses; LP solved by the canonical "
            "`solve_operator_selection_lp` on the clarabel-MPFR backend "
            "(was scipy linprog, with a sign error on y_0_star — bean qou/ftuv) with "
            "no parameter tuning; y_0^* read directly from the "
            "dual marginal of the equality constraint."
        ),
        "parameters": {
            "basis": basis,
            "t_markov_traces": t.tolist(),
            "n_target_choices": targets,
            "m_e_MeV": float(M_E_MEV),
        },
        "data": {
            "results_per_target_signed": results["signed"],
            "results_per_target_cone": results["cone"],
            "convention_A_E0_MeV": float(M_E_MEV) / 1.10998 / (1.10998 - 1),
            "convention_A_Q_beta_MeV_single_wrap": 0.7836458,
            "codata_Q_beta_MeV": 0.78233341,
            "negative_finding": (
                "Signed-cone LP (per prop's x_i ≥ -M): y_0^* = 0, "
                "primal slides to 0 — LP unbounded below in cost. "
                "Positive-cone LP (x_i ≥ 0): LP picks cheapest "
                "channel x^* = (0,…,1) with y_0^* ≈ 0.124 — NOT "
                "the B_3 normal form. In either case, y_0^* · m_e "
                "is far from convention A's 4.186 MeV. The LP-dual "
                "does NOT derive E_0 in MeV; it gives a "
                "dimensionless action shadow price. MeV scale "
                "comes from CAL-1 (m_e) + structural choice "
                "(convention A's single-tick m_e c_q^2 ℏ_q)."
            ),
        },
    }
    # Migrated to WitnessBuilder.wrap_legacy (#637 deferred Tier-2,
    # adopted in PR #639). Preserves on-disk layout bit-for-bit
    # while adding scriptHash / scriptCommitSha / computedAt /
    # durationMs staleness metadata required by `run_pipeline.py`.
    builder = WitnessBuilder.wrap_legacy(
        "e-0-lp-dual-h3", out, script_path=__file__, engine="scipy"
    )
    saved = builder.save()
    print(f"\n  Wrote {saved.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
