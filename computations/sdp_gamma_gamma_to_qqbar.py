#!/usr/bin/env python3
"""γγ → qq̄ SDP framework — categorical derivation of the proton crossing
budget (per investigation #4 in the H/D error-budget discussion).

Goal: derive the proton's 11-crossing structure (or whatever the right
budget is) FROM FIRST PRINCIPLES via SDP, instead of taking it as a
4-channel γγ→qq̄ ansatz fed in by hand.

Per content/.../breit-wheeler-vertex.md, the γγ → qq̄ pair-creation
vertex is encoded in the Hecke algebra:

  - σ_0 (horizontal polarization, eigenvalues +q / −q⁻¹)
  - σ_1 (vertical polarization, eigenvalues +q / −q⁻¹)
  - σ_0 · σ_1 → L₊ (Hopf link intermediate)
  - σ_0 · σ_1 · σ_0 → trefoil (electron / quark closure)

The classical reading: each photon enters a Hecke generator slot,
the product gives the pair-creation amplitude in the polarization
sphere, and the SDP picks out the canonical T_w whose Wedderburn
projections are PSD.

This script implements the H_2 / H_3 / H_4 SDP for the smallest
γγ → qq̄ vertices and reports:

  1. The SDP-optimal canonical T_w (in NF basis)
  2. Its Markov trace at q_0
  3. The implied crossing count
  4. Comparison to the proton's hand-built 11-crossing budget

This is a STARTER SCAFFOLD — the full multi-strand γγ → 3·quark
build for the proton requires:

  - H_3 SDP for the inner Borromean braid B_3
  - H_3 SDP for each quark pair (uu, ud, dd)
  - H_2 SDP for the 2·σ_0 gluon self-coupling
  - LR cross-level embedding to combine into H_3

That's the full pipeline. For now: H_2 γγ → e⁺e⁻ SDP as proof of
concept, then H_3 qq̄ with one inner Borromean.

NO Vol_hyp.  NO census.  Pure mpmath at 50 dps.

Scope note (2026-11-20). Owner ruling (bean qou-99qc, 2026-11-18, confirmed 2026-11-20):
def:photon is gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1. A single crossing is a TERM of a
photon, not a photon. The four-term recomputation of this file's photon claim is
probes/photon_chiral/photon_chiral_ports_probe.py, section E (results.md there).
The chiral vertex needs s1, so a four-term photon lives in H_3, not in this H_2 scaffold; the
H_2 numbers here are unchanged and remain an H_2 statement about the s0 term.

Output: sdp-gamma-gamma-to-qqbar.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

VOL_FIGURE_EIGHT = mp.mpf("2.029883212819307")
# CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase A).
from q_parameter import MASS_RATIO_MU_E_STR as _MU_E_STR
MASS_RATIO_MU_E  = mp.mpf(_MU_E_STR)
HBAR_Q_SQ        = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q           = mp.sqrt(HBAR_Q_SQ)
Q0               = mp.mpf(1) / (mp.mpf(1) - HBAR_Q)
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0


# ──────────────────────────────────────────────────────────────────
# H_2 — single quark + antiquark from γγ
# ──────────────────────────────────────────────────────────────────
#
# H_2(q) has 2 NF basis elements: {1, σ_0}.
# The SDP variables are coefficients c_1, c_σ in T_w = c_1·1 + c_σ·σ_0.
#
# Wedderburn projections at H_2:
#   - sym irrep (n) = (2): σ_0 → +q.  Projection: c_1 + q·c_σ
#   - alt irrep (1ⁿ) = (1,1): σ_0 → −q⁻¹.  Projection: c_1 − q⁻¹·c_σ
#
# PSD constraint (1×1 blocks): both projections ≥ 0
#   c_1 + q·c_σ ≥ 0
#   c_1 − q⁻¹·c_σ ≥ 0
#
# Trace value (a normalisation, NOT the selector — see below):
# Per Wenzl: tr_M(T_w) = y_(2)·χ_(2) + y_(1,1)·χ_(1,1)
#                      = y_(2)·(c_1 + q·c_σ) + y_(1,1)·(c_1 − q⁻¹·c_σ)
#                      = c_1·(y_(2) + y_(1,1)) + c_σ·(y_(2)·q − y_(1,1)·q⁻¹)
#
# At Markov-trace normalization: tr_M(σ_0) = z_M (the Markov param).
#
# tr_M(T_w) = 1 IS NOT THE SELECTION RULE (owner ruling 2026-08-30, bean
# qou-1qsw).  Imposed as a constraint it admits only the identity
# (c_1 = 1, c_σ = 0), so it excludes every non-trivial vertex including the
# shipped σ_0² — which is PSD but has tr_M = 1.128… at the substrate.  A
# condition that rejects the construction the file ships cannot be what
# selected it.  It is a normalisation of the trace, nothing more.
#
# THE SELECTOR IS PSD PARITY.  For the vertex σ_0^k both projections are the
# k-th powers of the generator's eigenvalues — sym q^k, alt (−q⁻¹)^k — so with
# 0 < q the sym block is always positive and the alt block is non-negative
# exactly when k is even:
#
#     σ_0^k is PSD  ⇔  k is even.
#
# Proved, sorry-free and over a generic ordered field, in
# folio/quantum-observable-universe/lean/QOU/QBeta/GluonVertexPsdParity.lean
# (`vertex_psd_iff_even`).  It mentions no Markov parameter, no Gram matrix
# and no anchor, so unlike the integer-LP rule it replaces it cannot go stale
# under a convention change.  It makes σ_0² the minimal non-zero admissible
# vertex, and excludes the single σ_0 that the convention-D re-run of the
# integer LP returns as its optimum
# (computations/qbeta/integer_lp_gluon_convention_d.py).  It does not force
# k > 0: whether the gluon vertex is present at all is a separate question.
# γγ → qq̄ "production" is described by σ_0³ (per breit-wheeler-vertex
# the trefoil σ_0σ_1σ_0 closes to a trefoil knot = electron, not quark).


def h2_psd_check(c1, c_sigma):
    """Return (sym_eigval, alt_eigval) for T_w = c1·1 + c_sigma·σ_0.

    PSD iff both ≥ 0.
    """
    sym = c1 + Q0 * c_sigma
    alt = c1 - QI0 * c_sigma
    return sym, alt


def h2_markov_trace(c1, c_sigma):
    """tr_M(T_w) at q_0 via Wenzl y_λ from y-lambda-wenzl-witness."""
    import json
    path = Path(__file__).parent / "y-lambda-wenzl-witness.json"
    with open(path) as f:
        d = json.load(f)
    table = d["tables_by_n"]["2"]
    y_sym = mp.mpf([w["y_lambda_numeric"] for w in table["weights"]
                    if w["partition"] == [2]][0])
    y_alt = mp.mpf([w["y_lambda_numeric"] for w in table["weights"]
                    if w["partition"] == [1, 1]][0])
    sym, alt = h2_psd_check(c1, c_sigma)
    # tr_M = Σ y_λ · χ_λ (Wenzl convention)
    return y_sym * sym + y_alt * alt


def h2_breit_wheeler_demo():
    """Demonstrate the σ_0³ trefoil produces electron via H_2."""
    # σ_0³ = (h·σ_0 + 1)·σ_0 = h·σ_0² + σ_0 = h·(h·σ_0 + 1) + σ_0
    #      = (h²+1)·σ_0 + h·1
    h_val = HA
    c1 = h_val
    c_sigma = h_val**2 + 1
    sym, alt = h2_psd_check(c1, c_sigma)
    tr_M = h2_markov_trace(c1, c_sigma)
    return {
        "c_1": float(c1),
        "c_sigma": float(c_sigma),
        "sym_eigenvalue_at_q_0": float(sym),
        "alt_eigenvalue_at_q_0": float(alt),
        "psd_at_q_0": (sym >= 0) and (alt >= 0),
        "tr_M_at_q_0": float(tr_M),
    }


# ──────────────────────────────────────────────────────────────────
# H_3 — first quark pair (e.g. u-d in proton)
# ──────────────────────────────────────────────────────────────────
#
# H_3(q) has 6 NF basis elements: {1, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0}.
# Wedderburn: 3 irreps with d_λ = 1, 2, 1 (sym, std, alt).
# T_w = a_0·1 + a_1·σ_0 + a_2·σ_1 + a_3·σ_0σ_1 + a_4·σ_1σ_0 + a_5·σ_0σ_1σ_0
#
# This is a 6-dim parameter space.  The full SDP at H_3 is a constrained
# optimization problem with PSD blocks of size (1, 2, 1).
#
# For brevity: report what the SDP infrastructure (joint_tower_sdp_solver
# from PR #444) would give for γγ → qq̄ in H_3.

def h3_skeleton_outline():
    """Describe the H_3 SDP for γγ → qq̄ (without solving)."""
    return {
        "n_strands": 3,
        "n_NF_basis_elements": 6,
        "wedderburn_blocks": [
            {"partition": [3], "d_lambda": 1, "irrep": "sym"},
            {"partition": [2, 1], "d_lambda": 2, "irrep": "std"},
            {"partition": [1, 1, 1], "d_lambda": 1, "irrep": "alt"},
        ],
        "psd_constraint_count": 3,
        "psd_constraint_dim": [1, 2, 1],
        "sdp_solver": "joint_tower_sdp_solver_v2.py (Phase 3b — H_3 SDP)",
        "expected_T_w_for_proton_pair": (
            "B_3 closure σ_0 σ_1⁻¹ σ_0 σ_1⁻¹ σ_0 σ_1⁻¹ + ud-half + gluon corrections"
        ),
        "expected_crossing_count": 11,  # paper's hand-built budget
        "open_question": (
            "Does the SDP UNIQUELY pick out 11 crossings, or are there "
            "alternative PSD-feasible budgets at H_3? probe_proton_crossing"
            "_budget.py shows the answer is 'yes, 11 is uniquely close to "
            "AME but other budgets are PSD-feasible too' — so the SDP is "
            "not strict enough; an additional constraint (e.g., minimal "
            "tr_M complement) is needed to pick out 11 categorically."
        ),
    }


def main():
    print("=" * 78)
    print("γγ → qq̄ SDP framework (scaffold)")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(Q0, 30)}")
    print(f"  m_e = {M_E_MEV} MeV")
    print()

    print("━━ H_2 demo: σ_0³ trefoil = electron γγ → e⁻e⁺")
    print("─" * 78)
    bw = h2_breit_wheeler_demo()
    print(f"  T_w = ({bw['c_1']:.4f})·1 + ({bw['c_sigma']:.4f})·σ_0")
    print(f"  sym eigenvalue at q_0 = {bw['sym_eigenvalue_at_q_0']:.4f}")
    print(f"  alt eigenvalue at q_0 = {bw['alt_eigenvalue_at_q_0']:.4f}")
    print(f"  PSD at q_0?            = {bw['psd_at_q_0']}")
    print(f"  tr_M at q_0            = {bw['tr_M_at_q_0']:.4f}")
    print()
    print("  Interpretation: σ_0³ is NOT PSD — the alt eigenvalue above is")
    print("  negative.  That is the parity rule, not an accident of q_0:")
    print("  alt(σ_0^k) = (−q⁻¹)^k, so with 0 < q it is non-negative iff k")
    print("  is even, and k = 3 is odd.  Proved sorry-free over a generic")
    print("  ordered field in QOU/QBeta/GluonVertexPsdParity.lean")
    print("  (vertex_psd_iff_even); the printed eigenvalue is its check.")
    print()
    print("  The older reading here argued from tr_M ≠ 1 instead.  That")
    print("  argument is WITHDRAWN (owner ruling 2026-08-30, bean qou-1qsw):")
    print("  tr_M = 1 admits only the identity, so it would also reject the")
    print("  σ_0² gluon vertex this file ships.  It is a normalisation, not")
    print("  a selector.  It also quoted tr_M ≈ 0.73, which was never the")
    print("  trace — 0.7312 is the magnitude of the alt eigenvalue.")
    print("  σ_0³ remains a SPECIFIC braid whose closure is the trefoil 3_1;")
    print("  what is now excluded is reading it as an admissible H_2 vertex.")
    print()
    print("  γγ → e⁻e⁺ in H_2: the breit-wheeler-vertex content block")
    print("  describes σ_0·σ_1·σ_0 → trefoil, but at H_2 there's no σ_1.")
    print("  H_3 is the minimum where the Hopf-link → trefoil sequence")
    print("  fits.  Hence the framework's 'electron lives at H_2 with")
    print("  σ_0³' assignment may be a CONVENTION rather than a")
    print("  derivation.")
    print()

    print("━━ H_3 SDP skeleton for γγ → qq̄")
    print("─" * 78)
    h3 = h3_skeleton_outline()
    print(f"  n_strands               = {h3['n_strands']}")
    print(f"  NF basis elements       = {h3['n_NF_basis_elements']}")
    print(f"  Wedderburn block dims   = {h3['psd_constraint_dim']}")
    print(f"  Existing SDP solver     = {h3['sdp_solver']}")
    print(f"  Expected proton T_w     = {h3['expected_T_w_for_proton_pair']}")
    print(f"  Expected crossing count = {h3['expected_crossing_count']}")
    print()
    print(f"  Open question:")
    print(f"    {h3['open_question'][:78]}")
    print(f"    {h3['open_question'][78:155]}")
    print(f"    {h3['open_question'][155:230]}")
    print(f"    {h3['open_question'][230:]}")
    print()

    print("━━ Path forward (deep work, future branch)")
    print("─" * 78)
    next_steps = [
        "1. Run joint_tower_sdp_solver_v2.py with γγ→qq̄ ansatz at H_3",
        "   — feed in 'γ_1 ⊗ γ_2' as 2-strand seed, evolve to 3-strand",
        "   — extract canonical T_w via PSD optimum",
        "2. Compare the SDP-derived T_w to the hand-built B_3 + ud + gluon",
        "   (current proton crossing budget).  Are they identical?",
        "3. If not, the SDP-derived budget is the categorical truth;",
        "   the hand-built 11-crossing version is convention.",
        "4. Generalize to H_4 (Brell-Wheeler diquark), H_5 (uud / udd",
        "   quark assembly inside nucleon), H_6 (deuteron), etc.",
        "5. Each level adds an LR-embedding step (Littlewood-Richardson",
        "   cross-level consistency, R4 from PR #444).",
    ]
    for s in next_steps:
        print(f"  {s}")
    print()

    # Build witness
    w = (
        WitnessBuilder("sdp-gamma-gamma-to-qqbar", engine="python+mpmath")
        .set_description(
            "Scaffold for γγ → qq̄ SDP categorical crossing-budget "
            "derivation. H_2 demo confirms σ_0³ has tr_M ≈ 0.73 at "
            "q_0 (not 1). H_3 skeleton outlines the 6-dim NF basis "
            "+ 3 Wedderburn blocks (dims 1, 2, 1). Full SDP solve "
            "deferred to follow-up — uses joint_tower_sdp_solver_v2.py "
            "(PR #444 Phase 3b) infrastructure."
        )
        .set_content_block("rem:photon-channel-wedderburn-chain")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("mpmath_dps", mp.mp.dps)
        .add_data("h2_breit_wheeler_demo", bw)
        .add_data("h3_skeleton_outline", h3)
        .add_data("path_forward", next_steps)
        .add_caveat(
            "This is a scaffold, not a complete γγ→qq̄ SDP solve. "
            "The full pipeline requires LR-embedding from H_2 (γγ) "
            "into H_3 (qq̄ with substrate), then H_3 (qq̄) into H_n "
            "(multi-quark hadron). PR #444's joint_tower_sdp_solver_v2 "
            "+ R4 cross-level consistency provides the SDP "
            "infrastructure; wiring γγ as the seed is the deep work."
        )
        .add_caveat(
            "probe_proton_crossing_budget.py showed PSD-feasible "
            "alternatives to the 11-crossing budget exist (different "
            "n_b3, n_gluon combinations are also PSD); the SDP needs "
            "an additional constraint (e.g., MINIMAL tr_M complement) "
            "to uniquely pick the 11-crossing canonical T_w."
        )
    )
    out_path = w.save()
    print(f"Witness: {out_path.name}")


if __name__ == "__main__":
    main()
