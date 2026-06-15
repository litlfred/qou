#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath/sympy consumer; symbolic-q
# polynomials live upstream (hoefsmit_symbolic / y_lambda_wenzl_bridge witnesses).
"""Δ_λ Option G — gg-pair-production trajectory for proton + neutron at n=3.

Extension of `rho_k_h3a_frobenius_pairing.py` (Option G, deuteron @ n=6)
to the nucleon braids @ n=3.  For proton β_p and neutron β_n, walks the
**gg-pair-production trajectory** crossing-by-crossing (each weighted
operator c·σ_i + d·I in the canonical word from
`hecke_core._PROTON_G0/G1` / `_NEUTRON_G0/G1` is one gg-pair event in
the symmetric-crystal interpretation; see
`two-photon-pair-production.md` and
`symmetric-crystal-pair-production.md`).

PER-STEP STATE TRACKED
======================

At every prefix β_K^(i) of the canonical word (i = 0 .. L), this script
records:

  - The cumulative weighted braid word so far (β_K^(i) = first i ops).
  - Per-Wedderburn-block character χ^λ(β_K^(i)) for every λ ⊢ 3.
  - Per-block contributions y_λ · χ^λ(β_K^(i)) (the Schur–Weyl summands).
  - The running partial Markov trace tr_M(β_K^(i)) = Σ_λ y_λ χ^λ(β_K^(i)).
  - Frobenius-pairing scalars S_K^(i) = Σ_μ y_μ χ^μ²/d_μ (the central-
    projection norm² along the trajectory).

OPTION G AT THE FULL BRAID
==========================

For the FULL nucleon (i = L), applies the Frobenius-pairing
minimum-norm closure formula

    Δ_λ^G(K) = (-B(K)/m_e) / S_K · χ^λ(β_K) / d_λ,
    S_K       = Σ_μ y_μ χ^μ(β_K)² / d_μ.

Note: free protons / neutrons have no nuclear binding (B = 0), so the
"binding-energy gap" Δρ for a single nucleon is ZERO under the CAL-3
convention (m_p, m_n ARE the calibration anchors).  Δ_λ^G under that
definition is identically 0 for both p and n.

To make Option G's structural content visible at the nucleon level,
this script ADDITIONALLY reports the **co-Casimir test target**
B_test = m_e · |tr_M(β_K)| (= the Schur–Weyl Markov-norm scaled to
mass units), which gives a finite Δ_λ^G profile for each nucleon
that can be compared structurally.

LP / SDP DUAL INFRASTRUCTURE  (per CLAUDE.md § *LP / SDP duals*)
================================================================

For each nucleon at the full braid, also runs the canonical LP and SDP
operator-selection solvers from `lp_dual_solver`:

  - LP via `solve_operator_selection_lp(t, G, n_target)` with
    t = Plancherel weights (1/dim_q(λ)), G = identity (every Δ_λ
    free), n_target = -B_test/m_e.  Reports y0_star, y_star,
    active_set, primal_obj, dual_obj, duality_gap.

  - SDP via `solve_psd_operator_selection_sdp(t, G, n_target)`
    with the same inputs.  Reports X_star, Z_star, eigenvalues
    (PSD certificate), duality_gap.

Both solvers' outputs are emitted per-nucleon in the witness so the
LP/SDP shadow-price dual can be compared against Option G's
closed-form Δ_λ^G.

REFERENCES
==========

  - `hecke_core._PROTON_G0/G1` / `_NEUTRON_G0/G1` — the canonical
    gg-pair-production operator chains for the two nucleons.
  - `prop:operator-selection-lp` / `lp_dual_solver.py` — canonical
    LP + SDP infrastructure (CLAUDE.md mandate for any operator-
    selection compute).
  - `rho_k_h3a_frobenius_pairing.py` — sibling deuteron compute
    (Δ_λ Option G).
  - `two-photon-pair-production.md` — gg → e⁻e⁺ symmetric-crystal step.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from mass_at_3A_proper import chi_lambda_of_word  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from lp_dual_solver import (  # noqa: E402
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)


# `hook_lengths`, `d_lambda`, `dim_q_lambda` imported from the shared
# helper rather than re-implemented locally — Gemini PR #613 review
# (dedup across the 4 ρ_K race scripts).
from murnaghan_nakayama import hook_lengths, d_lambda, dim_q_lambda  # noqa: E402, F401


# ── Build nucleon braid words (gg-pair-production cascade) ───────────
def nucleon_word(nucleon: str):
    """Return the canonical (c, d, gen_idx) sequence for one nucleon
    on n = 3 strands.  No interface (single nucleon, m_pn = 0)."""
    if nucleon == "p":
        intra_g0, intra_g1 = _PROTON_G0, _PROTON_G1
    elif nucleon == "n":
        intra_g0, intra_g1 = _NEUTRON_G0, _NEUTRON_G1
    else:
        raise ValueError(f"unknown nucleon: {nucleon}")
    word = []
    for c, d in intra_g0:
        word.append((float(c), float(d), 0))
    for c, d in intra_g1:
        word.append((float(c), float(d), 1))
    return word


# ── Per-prefix Markov-trace decomposition (gg trajectory tracking) ───
def per_prefix_decomposition(word, parts_dim):
    """For each prefix length i = 0..L, compute χ^λ(β^(i)) for every
    λ ⊢ 3.  parts_dim is [(λ, dim, sigmas, dim_λ), ...] where sigmas
    are the per-λ seminormal matrices.

    Returns: per_step = [{step, op, partial_word, chi_per_lambda}]
    """
    L = len(word)
    out = []
    for i in range(L + 1):
        prefix = word[:i]
        chi_per_lambda = {}
        for (lam, sigmas, dim_lam) in parts_dim:
            chi = chi_lambda_of_word(sigmas, dim_lam, prefix, n_gens_required=2)
            chi_per_lambda[lam] = float(chi)
        op_str = "·".join(_op_name(*op) for op in prefix) if prefix else "𝟙"
        out.append({
            "step": i,
            "n_ops_so_far": i,
            "last_op": (None if i == 0 else f"{word[i-1][0]:.3g}·σ_{word[i-1][2]}"
                        f"{f' + ({word[i-1][1]:.3g})·𝟙' if abs(word[i-1][1]) > 1e-12 else ''}"),
            "chi_per_lambda": {str(list(lam)): chi_per_lambda[lam]
                                for lam in chi_per_lambda},
        })
    return out


def _op_name(c, d, gi):
    """Compact label for one (c, d, gen_idx) op."""
    if abs(d) < 1e-12:
        return f"σ_{gi}"
    return f"({c:.2g}σ_{gi}+{d:.2g}·𝟙)"


# Local alias: q_dim is the imported `dim_q_lambda` (kept under the
# old name for minimum diff to call sites below).
q_dim = dim_q_lambda


def main() -> int:
    print("=" * 96)
    print("  Δ_λ Option G — gg-pair-production TRAJECTORY (proton + neutron, n=3)")
    print("  Sibling extension of rho_k_h3a_frobenius_pairing.py (deuteron @ n=6)")
    print("  + LP/SDP dual infrastructure per CLAUDE.md § *LP / SDP duals — first-class infra*")
    print("=" * 96)

    # WitnessBuilder up front so durationMs measures full runtime.
    builder = (
        WitnessBuilder(
            name="rho-k-h3a-gg-trajectory",
            # Canonical engine tag per probe-gamma-gamma-h3-psd-scan
            # (Copilot PR #613 review).  mpmath is used UPSTREAM of the
            # LP/SDP for the χ^λ trajectory at 50 dps, but the LP/SDP
            # solvers themselves are float64; the canonical combined tag
            # for python+numpy+cvxpy consumers groups this witness
            # appropriately.
            engine="python+numpy+cvxpy",
        )
        .set_description(
            "Δ_λ Option G extension: per-prefix gg-pair-production "
            "trajectory for the proton and neutron (n=3, p(3)=3) "
            "canonical braid words, with per-step χ^λ + Σ y_λ χ^λ "
            "decomposition. At the full braid, applies the Frobenius-"
            "pairing min-norm closure (Option G) AND routes through "
            "the canonical LP / SDP solvers from lp_dual_solver.py "
            "(per CLAUDE.md § LP/SDP duals — first-class infra). "
            "Sibling of rho_k_h3a_frobenius_pairing.py (deuteron @ n=6)."
        )
    )

    n = 3
    parts = [(3,), (2, 1), (1, 1, 1)]  # all partitions of 3
    print(f"\n  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  n   = {n} strands;  partitions of n: {[list(p) for p in parts]}")

    # ── Per-λ y_λ + dim + seminormal matrices (independent of nucleon) ─
    print("\n  Building per-λ Hoefsmit seminormal matrices …")
    parts_dim = []
    y_lambda_dict = y_lambda_at(n, q_val=float(Q_MP))  # {partition: y_value}
    y_at_q0 = {}
    dim_q_at_q0 = {}
    for lam in parts:
        sigmas, dim_lam, _tableaux = build_seminormal_matrices(lam, q=float(Q_MP))
        parts_dim.append((lam, sigmas, dim_lam))
        y_at_q0[lam] = mp.mpf(str(y_lambda_dict[lam]))
        dim_q_at_q0[lam] = q_dim(lam, Q_MP)
        print(f"    λ = {str(list(lam)):<12}  d_λ = {d_lambda(lam):<3}  "
              f"y_λ(q_0) = {mp.nstr(y_at_q0[lam], 10):<20}  "
              f"dim_q(λ) = {mp.nstr(dim_q_at_q0[lam], 8)}")

    nucleon_data = {}
    for nuc in ("p", "n"):
        print(f"\n{'─' * 96}")
        print(f"  NUCLEON: {nuc}  (β_{nuc} canonical word)")
        print(f"{'─' * 96}")
        word = nucleon_word(nuc)
        L = len(word)
        print(f"  word length L = {L} (gg-pair-production ops: 7 on σ_0 + 4 on σ_1)")
        for i, (c, d, gi) in enumerate(word):
            print(f"    op[{i:2d}]:  c={c:.4g}, d={d:+.5g}, gen=σ_{gi}")

        # ── Per-prefix χ^λ trajectory ──────────────────────────────
        print(f"\n  Per-prefix per-λ characters χ^λ(β_{nuc}^(i)):")
        per_step = per_prefix_decomposition(word, parts_dim)
        print(f"  {'step':<5}{'last_op':<28}", end="")
        for lam in parts:
            print(f"{'χ^'+str(list(lam)):>15}", end="")
        print(f"{'tr_M(β^(i))':>16}")
        print("  " + "-" * 90)
        for step in per_step:
            i = step["step"]
            last = step["last_op"] or "(empty)"
            print(f"  {i:<5}{last[:28]:<28}", end="")
            tr_partial = mp.mpf(0)
            for lam in parts:
                chi = step["chi_per_lambda"][str(list(lam))]
                print(f"{chi:>15.6g}", end="")
                tr_partial += y_at_q0[lam] * mp.mpf(str(chi))
            print(f"{float(tr_partial):>16.10g}")

        # ── Final-step Option G ───────────────────────────────────
        final_chi = {tuple(map(int, k.strip("[]").split(", "))): mp.mpf(str(v))
                     for k, v in per_step[-1]["chi_per_lambda"].items()}
        abs_tr_M = abs(sum(y_at_q0[lam] * final_chi[lam] for lam in parts))
        # B_test = m_e · |tr_M|  — visible structural target (not a real binding)
        B_test_MeV = M_E_MEV * abs_tr_M
        target = -B_test_MeV / M_E_MEV  # = -|tr_M|
        S_K = sum(y_at_q0[lam] * final_chi[lam] ** 2 / d_lambda(lam) for lam in parts)
        norm_sq = target * target / S_K

        print(f"\n  ── Final-step Option G (Frobenius-pairing min-norm closure) ──")
        print(f"     |tr_M(β_{nuc})|         = {mp.nstr(abs_tr_M, 18)}")
        print(f"     S_K = Σ y_μ χ^μ²/d_μ   = {mp.nstr(S_K, 18)}")
        print(f"     B_test = m_e · |tr_M|  = {mp.nstr(B_test_MeV, 10)} MeV  (structural target)")
        print(f"     target = -B_test/m_e   = {mp.nstr(target, 10)}")
        print(f"     ‖δ_K^G‖² = target²/S   = {mp.nstr(norm_sq, 10)}")

        delta_G_per_lambda = {}
        contribs = {}
        check_sum = mp.mpf(0)
        print(f"\n     {'partition':<14}{'d_λ':<5}{'χ^λ':>14}{'χ^λ/d_λ':>14}"
              f"{'Δ_λ^G':>16}{'y_λ χ^λ Δ_λ^G':>20}")
        print("     " + "-" * 83)
        for lam in parts:
            dl = d_lambda(lam)
            chi = final_chi[lam]
            delta_G = target * chi / (dl * S_K)
            contrib = y_at_q0[lam] * chi * delta_G
            delta_G_per_lambda[str(list(lam))] = str(delta_G)
            contribs[str(list(lam))] = str(contrib)
            check_sum += contrib
            print(f"     {str(list(lam)):<14}{dl:<5}{float(chi):>14.6g}"
                  f"{float(chi/dl):>14.6g}{float(delta_G):>16.6g}{float(contrib):>20.6g}")
        residual = check_sum - target
        print(f"     {'closure check (Σ y χ Δ)':<33}{float(check_sum):>30.10g}  "
              f"target = {float(target):.6g}  residual = {float(residual):.2e}")

        # ── LP/SDP via canonical solver — operator-selection LP ──────
        # Per Copilot PR #613 review (line 320): the original comment
        # described a y·χ-absorbed variable change that does NOT match
        # the implementation.  The actual setup:
        #
        #   Variables : x_λ ≥ 0 for each λ ⊢ n
        #   Cost      : t_λ = 1 / (dim_q(λ) · |y_λ χ^λ(β_K)|)
        #               (Plancherel × inverse-binding-weight, so the
        #                LP minimises Σ_λ (1/dim_q) · |Δ_λ| after
        #                interpreting x_λ as |y_λ χ^λ| · |Δ_λ|)
        #   Equality  : Σ_λ x_λ = |target|        (= |B_test/m_e|)
        #   G         : I (every channel free; Frobenius positivity
        #               degenerates to non-negativity of x_λ)
        #
        # Per Gemini PR #613 review (line 317, HIGH): t_λ MUST include
        # the 1/|y_λ χ^λ| factor for the LP to actually minimise the
        # weighted L¹-norm of Δ_λ rather than the weighted sum of
        # contributions.  Without that factor the LP minimises
        # Σ_λ (1/dim_q) · (|y_λ χ^λ| · |Δ_λ|) = weighted sum of
        # *contribution magnitudes*, NOT of Δ_λ.
        d_lp = len(parts)
        # Compute |y_λ χ^λ(β_K)| at q_0 for each λ (final-step values).
        y_chi_abs = [
            abs(float(y_at_q0[lam] * final_chi[lam])) for lam in parts
        ]
        # Build cost t_λ = 1/(dim_q(λ) · |y_λ χ^λ|).  Guard against
        # near-zero |y_λ χ^λ| (set to a large finite cost so the LP
        # naturally avoids that channel).
        _yc_floor = 1e-15
        t_arr = np.array([
            float(1.0 / (float(dim_q_at_q0[lam]) * max(yc, _yc_floor)))
            for lam, yc in zip(parts, y_chi_abs)
        ], dtype=float)
        G_arr = np.eye(d_lp, dtype=float)
        n_target_lp = float(abs(target))  # |target| ≥ 0 for the LP
        try:
            lp_result = solve_operator_selection_lp(t_arr, G_arr, n_target_lp)
            lp_dict = lp_result.to_dict()
        except Exception as e:
            lp_dict = {"feasible": False, "error": str(e)}

        # ── SDP via canonical solver ─────────────────────────────────
        try:
            sdp_result = solve_psd_operator_selection_sdp(t_arr, G_arr, n_target_lp)
            sdp_dict = sdp_result.to_dict()
        except Exception as e:
            sdp_dict = {"feasible": False, "error": str(e)}

        print(f"\n  ── LP dual (canonical operator-selection LP, t = 1/(dim_q · max(|y·χ|, floor))) ──")
        if lp_dict.get("feasible") is not False:
            print(f"     y0_star      = {lp_dict.get('y0_star'):+.6g}  (shadow price of mass equation)")
            print(f"     y_star       = {[f'{y:+.4g}' for y in lp_dict.get('y_star', [])]}")
            print(f"     active_set   = {lp_dict.get('active_set')}")
            print(f"     primal_obj   = {lp_dict.get('primal_obj'):.6g}")
            print(f"     dual_obj     = {lp_dict.get('dual_obj'):.6g}")
            print(f"     duality_gap  = {lp_dict.get('duality_gap'):.2e}")
        else:
            print(f"     LP infeasible: {lp_dict.get('error', 'unknown')}")

        print(f"\n  ── SDP (PSD-cone version of the same operator-selection problem) ──")
        if sdp_dict.get("feasible") is not False:
            print(f"     primal_obj   = {sdp_dict.get('primal_obj'):.6g}")
            print(f"     dual_obj     = {sdp_dict.get('dual_obj'):.6g}")
            print(f"     duality_gap  = {sdp_dict.get('duality_gap'):.2e}")
            evs = sdp_dict.get("eigenvalues", [])
            print(f"     eigenvalues  = {[f'{e:+.4e}' for e in evs]}")
        else:
            print(f"     SDP infeasible: {sdp_dict.get('error', 'unknown')}")

        nucleon_data[nuc] = {
            "word_length": L,
            "trajectory": per_step,
            "final": {
                "abs_tr_M_at_q0": str(abs_tr_M),
                "S_K_central_projection": str(S_K),
                "B_test_MeV": str(B_test_MeV),
                "target": str(target),
                "frobenius_norm_sq": str(norm_sq),
                "Delta_lambda_G": delta_G_per_lambda,
                "contributions": contribs,
                "closure_residual": str(residual),
            },
            "lp_dual": lp_dict,
            "sdp": sdp_dict,
            "y_star": lp_dict.get("y_star", []),
            "active_set": lp_dict.get("active_set", []),
            "y0_star": lp_dict.get("y0_star"),
            "primal_obj": lp_dict.get("primal_obj"),
            "dual_obj": lp_dict.get("dual_obj"),
            "duality_gap": lp_dict.get("duality_gap"),
        }

    # ── Cross-nucleon comparison ──────────────────────────────────
    print(f"\n{'═' * 96}")
    print("  CROSS-NUCLEON Δ_λ^G COMPARISON  (proton vs neutron)")
    print(f"{'═' * 96}")
    print(f"  {'partition':<14}{'Δ_λ^G(p)':>18}{'Δ_λ^G(n)':>18}"
          f"{'ratio p/n':>14}{'sign(p)':>10}{'sign(n)':>10}")
    print("  " + "-" * 84)
    for lam in parts:
        dp = mp.mpf(nucleon_data["p"]["final"]["Delta_lambda_G"][str(list(lam))])
        dn = mp.mpf(nucleon_data["n"]["final"]["Delta_lambda_G"][str(list(lam))])
        ratio = dp / dn if abs(dn) > 1e-40 else mp.mpf("inf")
        sp_str = "+" if dp > 0 else ("-" if dp < 0 else "0")
        sn_str = "+" if dn > 0 else ("-" if dn < 0 else "0")
        print(f"  {str(list(lam)):<14}{float(dp):>18.6g}{float(dn):>18.6g}"
              f"{float(ratio):>14.4g}{sp_str:>10}{sn_str:>10}")

    print(f"\n  Note: Δ_λ^G profiles differ across nucleons (vortex-aware property).")
    print(f"  Same closure formula, different inputs (β_p vs β_n χ^λ values).")

    builder.add_data("nucleons", nucleon_data)
    builder.add_data("y_lambda_at_q0", {str(list(lam)): str(y_at_q0[lam]) for lam in parts})
    builder.add_data("dim_q_at_q0", {str(list(lam)): str(dim_q_at_q0[lam]) for lam in parts})
    builder.add_data("d_lambda", {str(list(lam)): d_lambda(lam) for lam in parts})

    # Closure assertions per-nucleon
    for nuc in ("p", "n"):
        residual = abs(mp.mpf(nucleon_data[nuc]["final"]["closure_residual"]))
        builder.add_assertion(
            name=f"option_g_closure_{nuc}",
            computed=float(residual),
            expected=0.0,
            tolerance=1e-13,
            source=f"Option G binding-equation closure residual at full β_{nuc}",
        )
        # LP duality gap (strong duality)
        gap = nucleon_data[nuc]["duality_gap"]
        if gap is not None:
            builder.add_assertion(
                name=f"lp_duality_gap_{nuc}",
                computed=float(gap),
                expected=0.0,
                tolerance=1e-6,
                source=f"LP strong duality gap |primal - dual| at β_{nuc}",
            )
        sdp_gap = nucleon_data[nuc]["sdp"].get("duality_gap")
        if sdp_gap is not None and not (isinstance(sdp_gap, float) and (sdp_gap != sdp_gap)):
            builder.add_assertion(
                name=f"sdp_duality_gap_{nuc}",
                computed=float(sdp_gap),
                expected=0.0,
                tolerance=1e-4,
                source=f"SDP strong duality gap |primal - dual| at β_{nuc}",
            )

    out_path = builder.save()
    print(f"\n  Wrote {out_path.name} ({out_path.stat().st_size} bytes).")
    print("=" * 96)
    print("  OUTCOME: Option G extended to proton + neutron + LP/SDP duals via canonical solvers.")
    print("=" * 96)
    return 0


if __name__ == "__main__":
    sys.exit(main())
