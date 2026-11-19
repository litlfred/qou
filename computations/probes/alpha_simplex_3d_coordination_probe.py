#!/usr/bin/env python3
"""alpha_simplex_3d_coordination_probe.py — 80-dps First-Principles 3D Simplicial
Nuclear Coordination & GPMT Cumulant Probe (Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/AlphaSimplexCoordinationDerivation.lean`
  (`namespace QOU.Nuclear.AlphaSimplexCoordinationDerivation`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (zero float64 intermediates, zero `math` module
imports, zero tuned parameters) the first-principles 3D tetrahedral (alpha-simplex)
simplicial coordination complexes derived in `AlphaSimplexCoordinationDerivation.lean`,
side-by-side against the existing 1D linear chain (`E = A - 1`) and the legacy
all-pairs Borromean tower (`E_pair = C(A, 2)`).

Every input comes exclusively from the three substrate calibrations:
  * CAL-1: electron mass `m_e` (`codata_constants.M_E_MEV`),
  * CAL-2: proton-pinned quantum parameter `q_0` (`q_parameter.Q_50_DIGIT_STR`),
           yielding bare level-0 scale `E_0 = m_e / (q_0 (q_0 - 1))`, Convention-D root
           `z_D = q_0^3 / (q_0^2 + 1)`, Borromean H_3 trace
           `tau_Bor = (4 + h^2 - 3 h^4 - h^6) / (h^2 + 4)`, and the parameter-free
           H_3 / H_4 GPMT modified-dimension cumulants `mu3GPMT_H4(q_0) > 0` and
           `mu4GPMT_H4(q_0) < 0` (`H4GPMTModifiedDimensionCumulants.lean`),
  * CAL-3: pion Compton length `lambda_bar_pi = hbar*c / m_pi` entering the
           parameter-free Coulomb repulsion `E_C(Z, A)` (`coulomb_energy.py`)
           with derived `alpha_EM(q_0)`.

EXPLICIT MODEL-BOUNDARY & GATE DISCLOSURES
------------------------------------------
1. **Zero-Liquid-Drop Simplicial Strong Core vs CAL-3 Coulomb Subtraction**:
   The strong simplicial functional `B_simp(K_A) = f_1 b_2 + f_2 w_3 + f_3 w_4`
   formalized in `AlphaSimplexCoordinationDerivation.lean` has ZERO liquid-drop
   or Euclidean sphere-packing assumptions (derived purely from 4-state spin-isospin
   Pauli exclusion `pauli_clique_card_le_four`, `pauli_k4_balanced_isospin`, and
   inductive tetrahedral face-gluing). When comparing total net binding against
   Coulomb-inclusive AME2020 data (`B_net = B_simp - E_C`), the additive electromagnetic
   subtraction `coulomb_energy_mev(Z, A)` (`computations/coulomb_energy.py`) uses
   the corpus's existing CAL-3 uniform-sphere radius law `R(A) = lambda_bar_pi * A^{1/3}`
   (documented as conditional in `coulomb_energy.py:124-147`). In mirror-nucleus
   differences (`simplicial_mirror_split_pure_coulomb`), the strong simplicial core
   cancels identically without touching `E_C`.
2. **Achiral `gg` Interface Bond Gate (`conj:s5-so3-fiber-action`)**:
   `b2_log_gg = E_0 * ln(1 / (z_D - h/2))` evaluates the Markov trace of the achiral
   symmetrized crossing `(T_i + T_i^{-1})/2 = T_i - (h/2)*1` (`gg_production_bond_probe.py`).
   Rewiring production to this charge-symmetric color-tube bond is gated on the
   keystone conjecture `conj:s5-so3-fiber-action` (`coulomb_energy.py:66-68`). All
   three parameter-free bond channels (`b2_log_D`, `b2_Bor_D`, `b2_log_gg`) are
   evaluated side-by-side without post-hoc selection.
3. **Both Pauli-Legal Excess-Nucleon Simplicial Attachment Regimes**:
   By `pauli_k4_balanced_isospin`, every s-wave `K_4` tetrahedron has exact `(2p, 2n)`
   composition (`card_p = 2, card_n = 2`), so once the `A_core = 2 * min(Z, N)` core
   is formed, the `D = |N - Z|` excess majority-species nucleons can form `0` new
   s-wave `K_4` tetrahedra (`f_3 = f_3(A_core)`). By `pauli_same_isospin_card_le_two`,
   mono-isospin `(n,n,n)` triangles are forbidden, leaving two Pauli-legal excess
   attachments formalized in `AlphaSimplexCoordinationDerivation.lean`:
   - **Regime A (`pauliBridge`, degree-1 peripheral bridge)**: each excess nucleon
     adds `+1` edge, `0` triangles, `0` tetrahedra (symmetry deficit
     `(2*b_2 + 3*w_3 + w_4)*|N - Z|`),
   - **Regime B (`pauliTriangle`, maximal Pauli-legal degree-2 mixed-isospin `(p,n,n)` triangle)**:
     each excess nucleon attaches to a `(p, n)` core edge, adding `+2` edges, `+1`
     mixed-isospin `(p, n_up, n_down)` triangle, and `0` tetrahedra (symmetry deficit
     `(b_2 + 2*w_3 + w_4)*|N - Z|`). Both satisfy `chi = 1` (`eulerChar_pauliExcess_both_eq_one`)
     and are reported side-by-side.
4. **Bare Level-0 Scale `E_0^{(0)}` vs Tower-Resummed `E_0^{(inf)}`**:
   All primary binding columns use the bare level-0 scale
   `E_0^{(0)} = m_e / (q_0 (q_0 - 1))` (matching `borromean_binding_recompute.py`
   and `mass_binding_dashboard.py`). The exact brane-tower geometric resummation
   factor `1 / (1 - hbar_q^2)` (`hbar_q = (q_0 - 1) / q_0 = 1 - q_0^{-1}`) and
   `E_0^{(inf)} = E_0^{(0)} / (1 - hbar_q^2) = m_e q_0 / ((q_0 - 1)(2 q_0 - 1))`
   are recorded in the witness metadata.

AME2020 binding energies (`codata_constants.ame_binding_mev`) are read strictly as
a downstream validation target (`delta_MeV = B_pred - B_AME`, `err_ppQ = delta_MeV / B_AME`,
`err_sigma = delta_MeV / sigma_AME`) and NEVER enter any predicted formula.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from _li_2_q_util import li_2_q  # noqa: E402
from codata_constants import M_E_MEV, _ame_entry, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ── Pure-integer binomial coefficient (no `import math`) ─────────────────────
def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    num = 1
    for i in range(1, k_use + 1):
        num = (num * (n - k_use + i)) // i
    return num


# ── Exact simplicial f-vectors matching AlphaSimplexCoordinationDerivation.lean ──
def f0_simplex(A: int) -> int:
    return A


def f1_simplex(A: int) -> int:
    if A <= 1:
        return 0
    if A == 2:
        return 1
    return 3 * A - 6


def f2_simplex(A: int) -> int:
    if A <= 2:
        return 0
    return 3 * A - 8


def f3_simplex(A: int) -> int:
    if A <= 3:
        return 0
    return A - 3


def intra_alpha_edges(A: int) -> int:
    return 6 * (A // 4) + _int_comb(A % 4, 2)


def intra_alpha_triangles(A: int) -> int:
    return 4 * (A // 4) + _int_comb(A % 4, 3)


def intra_alpha_tetrahedra(A: int) -> int:
    return A // 4


def cluster_node_count(A: int) -> int:
    return (A // 4) + (0 if (A % 4 == 0) else 1)


def inter_cluster_edges(A: int) -> int:
    return f1_simplex(cluster_node_count(A))


def total_alpha_cluster_edges(A: int) -> int:
    return intra_alpha_edges(A) + inter_cluster_edges(A)


def pauli_bridge_f_vector(Z: int, N: int) -> tuple[int, int, int]:
    """Regime A (`pauliBridgeF1..F3` in AlphaSimplexCoordinationDerivation.lean):
    Balanced core A_core = 2 * min(Z, N) forms K_{A_core}; each of the D = |N - Z|
    excess majority nucleons attaches by a degree-1 peripheral bond (+1 edge,
    0 triangles, 0 tetrahedra). At A <= 3, returns the full K_A simplex f-vector."""
    A = Z + N
    if A <= 3:
        return f1_simplex(A), f2_simplex(A), f3_simplex(A)
    m_min = Z if Z <= N else N
    a_core = 2 * m_min
    d_excess = A - a_core
    if a_core == 0:
        return 0, 0, 0
    return (
        f1_simplex(a_core) + d_excess,
        f2_simplex(a_core),
        f3_simplex(a_core),
    )


def pauli_triangle_f_vector(Z: int, N: int) -> tuple[int, int, int]:
    """Regime B (`pauliTriangleF1..F3` in AlphaSimplexCoordinationDerivation.lean):
    Maximal Pauli-legal excess attachment. By `pauli_k4_balanced_isospin`, excess
    single-species nucleons cannot form K_4 tetrahedra (+0 tetrahedra), but by
    `pauli_same_isospin_card_le_two` they CAN form mixed-isospin (p, n_up, n_down)
    K_3 triangles (+2 edges, +1 triangle, 0 tetrahedra per excess nucleon)."""
    A = Z + N
    if A <= 3:
        return f1_simplex(A), f2_simplex(A), f3_simplex(A)
    m_min = Z if Z <= N else N
    a_core = 2 * m_min
    d_excess = A - a_core
    if a_core == 0:
        return 0, 0, 0
    return (
        f1_simplex(a_core) + 2 * d_excess,
        f2_simplex(a_core) + d_excess,
        f3_simplex(a_core),
    )


# ── 15 Benchmark Nuclei from 2H to 238U ──────────────────────────────────────
BENCHMARK_NUCLEI: list[tuple[str, int, int]] = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("24Mg", 12, 12),
    ("40Ca", 20, 20),
    ("56Fe", 26, 30),
    ("120Sn", 50, 70),
    ("197Au", 79, 118),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]


def _ame_sigma_total_mev(Z: int, A: int) -> mp.mpf:
    with mp.workdps(max(80, mp.mp.dps)):
        entry = _ame_entry(Z, A)
        unc_kev = entry.get("binding_energy_per_A_unc_keV")
        if unc_kev is None:
            return mp.mpf(0)
        return mp.mpf(repr(unc_kev)) * mp.mpf(A) / mp.mpf(1000)


def _derive_substrate_constants() -> dict[str, mp.mpf]:
    with mp.workdps(80):
        q = mp.mpf(str(Q_50_DIGIT_STR))
        qi = mp.mpf(1) / q
        h = q - qi
        hbar_q = (q - mp.mpf(1)) / q
        tower_resum_factor = mp.mpf(1) / (mp.mpf(1) - hbar_q ** 2)
        me = mp.mpf(str(M_E_MEV))
        e0 = me / (q * (q - mp.mpf(1)))
        e0_inf = e0 * tower_resum_factor
        z_d = (q ** 3) / (q ** 2 + mp.mpf(1))
        z_gg = z_d - h / mp.mpf(2)
        z_nn_chiral = z_d - h
        tau_bor = (mp.mpf(4) + h ** 2 - mp.mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mp.mpf(4))

        # 2-body single-bond energies (MeV) — three parameter-free channels:
        # (1) Convention-D log-trace bond: E_0 * ln(1 / z_D)
        b2_log_d = e0 * mp.log(mp.mpf(1) / z_d)
        # (2) Flavor-blind gg color-average log-trace bond: E_0 * ln(1 / (z_D - h/2))
        b2_log_gg = e0 * mp.log(mp.mpf(1) / z_gg)
        # (3) Borromean H_3 single-bond energy (level-0 + Li_2^q pair at A=2):
        g_tau2 = -li_2_q(-(tau_bor * tau_bor), q, qi)
        g_tau2_zd = -li_2_q(-(tau_bor * tau_bor * z_d), q, qi)
        g_tau2_znn = -li_2_q(-(tau_bor * tau_bor * z_nn_chiral), q, qi)
        b2_bor_pair_only = e0 * (z_d ** 2) * (g_tau2 - g_tau2_zd)
        b2_bor_d = e0 * ((tau_bor ** 2) * (mp.mpf(1) - z_d)) + b2_bor_pair_only

        # GPMT H_3 / H_4 modified quantum dimensions and Mayer cumulants (dimensionless & MeV):
        # From GPMTThreeRowCumulantBridge.lean & H4GPMTModifiedDimensionCumulants.lean
        q2_1 = q ** 2 + mp.mpf(1)
        q4_1 = q ** 4 + mp.mpf(1)
        q4_2_1 = q ** 4 + q ** 2 + mp.mpf(1)
        h4_mod_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_mod_denom

        mu2_gpmt = mp.mpf(0)
        mu3_gpmt = -d_mod_111
        s_row3_h4_4 = -mp.mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mp.mpf(4) * mu3_gpmt
        mu4_gpmt_h3 = mp.mpf(2) * d_mod_111

        w3_gpmt_mev = e0 * mu3_gpmt
        w4_gpmt_h4_mev = e0 * mu4_gpmt_h4
        w4_gpmt_h3_mev = e0 * mu4_gpmt_h3

        return {
            "q0": q,
            "qi": qi,
            "h": h,
            "hbar_q": hbar_q,
            "tower_resum_factor_inv_one_minus_hbar_q_sq": tower_resum_factor,
            "m_e_MeV": me,
            "E0_bare_level0_MeV": e0,
            "E0_tower_resummed_MeV": e0_inf,
            "E0_MeV": e0,
            "z_D": z_d,
            "z_gg": z_gg,
            "z_nn_chiral": z_nn_chiral,
            "tau_Bor": tau_bor,
            "g_tau2": g_tau2,
            "g_tau2_zD": g_tau2_zd,
            "g_tau2_znn": g_tau2_znn,
            "b2_log_D_MeV": b2_log_d,
            "b2_log_gg_MeV": b2_log_gg,
            "b2_Bor_D_MeV": b2_bor_d,
            "b2_Bor_pair_step_MeV": b2_bor_pair_only,
            "dMod111": d_mod_111,
            "dMod211": d_mod_211,
            "dMod1111": d_mod_1111,
            "mu2GPMT_H4": mu2_gpmt,
            "mu3GPMT_H4": mu3_gpmt,
            "sRow3GPMT_H4_four": s_row3_h4_4,
            "mu4GPMT_H4": mu4_gpmt_h4,
            "mu4GPMT_H3": mu4_gpmt_h3,
            "w3_GPMT_MeV": w3_gpmt_mev,
            "w4_GPMT_H4_MeV": w4_gpmt_h4_mev,
            "w4_GPMT_H3_MeV": w4_gpmt_h3_mev,
            "vol_coeff_3tree_logD_GPMT_MeV": mp.mpf(3) * b2_log_d + mp.mpf(3) * w3_gpmt_mev + w4_gpmt_h4_mev,
            "bdry_deficit_3tree_logD_GPMT_MeV": mp.mpf(6) * b2_log_d + mp.mpf(8) * w3_gpmt_mev + mp.mpf(3) * w4_gpmt_h4_mev,
            "vol_coeff_3tree_BorD_GPMT_MeV": mp.mpf(3) * b2_bor_d + mp.mpf(3) * w3_gpmt_mev + w4_gpmt_h4_mev,
            "bdry_deficit_3tree_BorD_GPMT_MeV": mp.mpf(6) * b2_bor_d + mp.mpf(8) * w3_gpmt_mev + mp.mpf(3) * w4_gpmt_h4_mev,
            "vol_coeff_3tree_logGG_GPMT_MeV": mp.mpf(3) * b2_log_gg + mp.mpf(3) * w3_gpmt_mev + w4_gpmt_h4_mev,
            "bdry_deficit_3tree_logGG_GPMT_MeV": mp.mpf(6) * b2_log_gg + mp.mpf(8) * w3_gpmt_mev + mp.mpf(3) * w4_gpmt_h4_mev,
            "pauli_bridge_deficit_per_excess_logGG_MeV": mp.mpf(2) * b2_log_gg + mp.mpf(3) * w3_gpmt_mev + w4_gpmt_h4_mev,
            "pauli_triangle_deficit_per_excess_logGG_MeV": b2_log_gg + mp.mpf(2) * w3_gpmt_mev + w4_gpmt_h4_mev,
        }


def _simplicial_energy(b2: mp.mpf, w3: mp.mpf, w4: mp.mpf, f1: int, f2: int, f3: int) -> mp.mpf:
    return mp.mpf(f1) * b2 + mp.mpf(f2) * w3 + mp.mpf(f3) * w4


def _borromean_graph_energy(c: dict[str, mp.mpf], A: int, f1: int, f2: int, f3: int) -> mp.mpf:
    """Consistent O(A) Borromean trace + Li_2^q tower on a graph with `f1` charge-symmetric
    Convention-D edges (`f = z_D`), plus GPMT 3-body face and 4-body cell cumulants."""
    e0 = c["E0_MeV"]
    tau = c["tau_Bor"]
    z_d = c["z_D"]
    tr_free = tau ** A
    tr_atom = tr_free * (z_d ** f1)
    b_can0 = e0 * (tr_free - tr_atom)
    b_pair = mp.mpf(f1) * c["b2_Bor_pair_step_MeV"]
    b_gpmt = mp.mpf(f2) * c["w3_GPMT_MeV"] + mp.mpf(f3) * c["w4_GPMT_H4_MeV"]
    return b_can0 + b_pair + b_gpmt


def _legacy_borromean_allpairs_chiral(c: dict[str, mp.mpf], Z: int, N: int) -> mp.mpf:
    """Legacy `borromean_binding_recompute.py` formula: (A-1) bonds in level-0,
    all-pairs C(A,2) in Li_2^q, and chiral f_nn = z_D - h (no Coulomb)."""
    A = Z + N
    e0 = c["E0_MeV"]
    tau = c["tau_Bor"]
    z_d = c["z_D"]
    z_nn = c["z_nn_chiral"]
    n_pp = max(Z - 1, 0)
    n_pn = 1 if (Z > 0 and N > 0) else 0
    n_nn = max(N - 1, 0)
    ratio = (z_d ** n_pp) * (z_d ** n_pn) * (z_nn ** n_nn)
    tr_free = tau ** A
    dtr = tr_free - tr_free * ratio
    pair_zd = (_int_comb(Z, 2) + Z * N) * (c["g_tau2"] - c["g_tau2_zD"])
    pair_znn = _int_comb(N, 2) * (c["g_tau2"] - c["g_tau2_znn"])
    return e0 * (dtr + (z_d ** 2) * (pair_zd + pair_znn))


def _err_metrics(b_pred: mp.mpf, b_ame: mp.mpf, sigma_ame: mp.mpf) -> dict[str, str]:
    delta = b_pred - b_ame
    ppq = delta / b_ame
    err_sig = (delta / sigma_ame) if sigma_ame > mp.mpf(0) else mp.mpf(0)
    return {
        "B_pred_MeV": fmt(b_pred),
        "delta_MeV": fmt(delta),
        "err_ppQ": fmt(ppq),
        "err_pct": fmt(ppq * mp.mpf(100)),
        "err_sigma": fmt(err_sig),
    }


def main() -> int:
    set_compute_dps(80)
    c = _derive_substrate_constants()

    wb = WitnessBuilder("alpha-simplex-3d-coordination", engine="mpmath")
    wb.set_description(
        "80-dps first-principles evaluation of 3D tetrahedral (alpha-simplex) nuclear "
        "coordination complexes (stacked 3-simplex 3-tree K_A, Pauli degree-1 bridge "
        "3-tree, Pauli maximal degree-2 mixed-isospin triangle 3-tree, and hierarchical "
        "alpha-cluster complex C_A) with H_3/H_4 GPMT modified-dimension cumulants and "
        "CAL-3 Coulomb repulsion across 15 benchmark nuclei (2H to 238U). "
        "Zero free parameters, zero fitting, zero float64 intermediates."
    )

    wb.add_data(
        "model_boundary_disclosures",
        {
            "strong_simplicial_core": (
                "Derived purely from 4-state spin-isospin Pauli exclusion "
                "(pauli_clique_card_le_four, pauli_k4_balanced_isospin) and inductive "
                "3-simplex face-gluing in AlphaSimplexCoordinationDerivation.lean; "
                "ZERO liquid-drop or Euclidean sphere-packing assumptions."
            ),
            "coulomb_subtraction_scope": (
                "Additive electrostatic term E_C(Z, A) imported from computations/coulomb_energy.py "
                "(CAL-3 pion Compton length lambda_bar_pi = hbar*c/m_pi with derived alpha_EM(q_0) "
                "and uniform-sphere A^{1/3} radius scaling, documented as conditional in "
                "coulomb_energy.py:124-147). In mirror-pair differences "
                "(simplicial_mirror_split_pure_coulomb), the strong simplicial energy cancels "
                "identically."
            ),
            "achiral_gg_interface_gate": (
                "b2_log_gg = E_0 * ln(1 / (z_D - h/2)) evaluates the Markov trace of the "
                "achiral crossing (T_i + T_i^{-1})/2 = T_i - (h/2)*1; promotion to the "
                "canonical charge-symmetric production bond is gated on conj:s5-so3-fiber-action "
                "(coulomb_energy.py:66-68). All three parameter-free bond channels "
                "(b2_log_D, b2_Bor_D, b2_log_gg) are reported side-by-side."
            ),
            "pauli_excess_attachment_regimes": (
                "By pauli_k4_balanced_isospin, excess single-species nucleons D = |N - Z| "
                "cannot form s-wave K_4 tetrahedra (+0 tetrahedra). Both Pauli-legal excess "
                "attachment regimes formalized in AlphaSimplexCoordinationDerivation.lean are "
                "reported side-by-side: Regime A (pauliBridge, degree-1 peripheral bond: +D edges, "
                "0 triangles, 0 tetrahedra) and Regime B (pauliTriangle, maximal degree-2 "
                "mixed-isospin (p,n,n) triangle: +2D edges, +D triangles, 0 tetrahedra)."
            ),
            "scale_E0_convention": (
                "Primary columns use bare level-0 scale E_0^{(0)} = m_e / (q_0*(q_0 - 1)) = "
                + fmt(c["E0_bare_level0_MeV"])
                + " MeV; tower-resummed E_0^{(inf)} = E_0^{(0)} / (1 - hbar_q^2) = "
                + fmt(c["E0_tower_resummed_MeV"])
                + " MeV (factor "
                + fmt(c["tower_resum_factor_inv_one_minus_hbar_q_sq"])
                + ") is recorded in derived_substrate_constants."
            ),
        },
    )

    wb.add_data(
        "derived_substrate_constants",
        {k: fmt(v) for k, v in c.items()},
    )

    rows_data: list[dict[str, object]] = []

    print("==================================================================================================================================")
    print("  80-dps 3D Tetrahedral alpha-Simplex Nuclear Coordination Probe (Zero Fitting, Zero Float64)")
    print("==================================================================================================================================")
    print("  Derived 2-body bond energies (MeV):")
    print("    b2_log_D  = E0 * ln(1/z_D)         = " + mp.nstr(c["b2_log_D_MeV"], 12) + " MeV")
    print("    b2_Bor_D  = E0 * (dtr_2 + z_D^2*g) = " + mp.nstr(c["b2_Bor_D_MeV"], 12) + " MeV")
    print("    b2_log_gg = E0 * ln(1/(z_D - h/2)) = " + mp.nstr(c["b2_log_gg_MeV"], 12) + " MeV")
    print("  Derived H_3 / H_4 GPMT higher-body cumulants (MeV):")
    print("    w3_GPMT    = E0 * mu3GPMT_H4(q0)   = +" + mp.nstr(c["w3_GPMT_MeV"], 12) + " MeV  (triangle attraction)")
    print("    w4_GPMT_H4 = E0 * mu4GPMT_H4(q0)   = " + mp.nstr(c["w4_GPMT_H4_MeV"], 12) + " MeV  (tetrahedron saturation)")
    print("    4*w3 + w4  = E0 * sRow3GPMT_H4(4)  = +" + mp.nstr(mp.mpf(4) * c["w3_GPMT_MeV"] + c["w4_GPMT_H4_MeV"], 12) + " MeV  (net K_4 >=3-body)")
    print("    3*w3 + w4  (3-tree >=3-body/A)     = +" + mp.nstr(mp.mpf(3) * c["w3_GPMT_MeV"] + c["w4_GPMT_H4_MeV"], 12) + " MeV/nucleon")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    hdr = (
        f"{'Nucl':<6} {'Z':>3} {'N':>3} {'A':>3} | "
        f"{'f1_ch':>5} {'f1_3t':>5} {'f1_P1':>5} {'f1_P2':>5} | "
        f"{'B_AME':>10} {'B_oldBor':>10} {'B_1D_log':>10} {'B_3t_logD':>10} "
        f"{'B_3t_P1gg':>10} {'B_3t_P2gg':>10} {'B_3t_gg':>10}"
    )
    print(hdr)
    print("-" * len(hdr))

    for name, Z, N in BENCHMARK_NUCLEI:
        A = Z + N
        b_ame = ame_binding_mev(Z, A)
        sigma_ame = _ame_sigma_total_mev(Z, A)
        e_c = coulomb_energy_mev(Z, A)

        # Topological simplex counts
        f1_ch = A - 1
        f1_3t, f2_3t, f3_3t = f1_simplex(A), f2_simplex(A), f3_simplex(A)
        f1_cl, f2_cl, f3_cl = (
            total_alpha_cluster_edges(A),
            intra_alpha_triangles(A),
            intra_alpha_tetrahedra(A),
        )
        f1_p1, f2_p1, f3_p1 = pauli_bridge_f_vector(Z, N)
        f1_p2, f2_p2, f3_p2 = pauli_triangle_f_vector(Z, N)

        # 0. Legacy all-pairs chiral Borromean tower (O(A^2) blowup baseline)
        b_legacy_bor = _legacy_borromean_allpairs_chiral(c, Z, N)

        # 1. 1D Linear Chain (f1 = A - 1, f2 = 0, f3 = 0) with charge-symmetric z_D - E_C
        b_1d_log_d = mp.mpf(f1_ch) * c["b2_log_D_MeV"] - e_c
        b_1d_bor_d = _borromean_graph_energy(c, A, f1_ch, 0, 0) - e_c

        # 2. Hierarchical alpha-Cluster Complex C_A (respecting Pauli bipyramid isolation) - E_C
        b_acl_log_d = _simplicial_energy(
            c["b2_log_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_cl, f2_cl, f3_cl
        ) - e_c
        b_acl_bor_d = _simplicial_energy(
            c["b2_Bor_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_cl, f2_cl, f3_cl
        ) - e_c
        b_acl_log_gg = _simplicial_energy(
            c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_cl, f2_cl, f3_cl
        ) - e_c

        # 3. Stacked 3-Simplex Complex (3-Tree K_A: f1 = 3A-6, f2 = 3A-8, f3 = A-3) - E_C
        b_3t_log_d = _simplicial_energy(
            c["b2_log_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_3t, f2_3t, f3_3t
        ) - e_c
        b_3t_bor_graph = _borromean_graph_energy(c, A, f1_3t, f2_3t, f3_3t) - e_c
        b_3t_bor_add = _simplicial_energy(
            c["b2_Bor_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_3t, f2_3t, f3_3t
        ) - e_c
        b_3t_log_gg = _simplicial_energy(
            c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_3t, f2_3t, f3_3t
        ) - e_c

        # 4A. Pauli Regime A (pauliBridge, degree-1 peripheral excess edges) - E_C
        b_3t_p1_log_d = _simplicial_energy(
            c["b2_log_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p1, f2_p1, f3_p1
        ) - e_c
        b_3t_p1_bor_d = _simplicial_energy(
            c["b2_Bor_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p1, f2_p1, f3_p1
        ) - e_c
        b_3t_p1_log_gg = _simplicial_energy(
            c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p1, f2_p1, f3_p1
        ) - e_c

        # 4B. Pauli Regime B (pauliTriangle, maximal Pauli-legal degree-2 mixed-isospin (p,n,n) triangles) - E_C
        b_3t_p2_log_d = _simplicial_energy(
            c["b2_log_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p2, f2_p2, f3_p2
        ) - e_c
        b_3t_p2_bor_d = _simplicial_energy(
            c["b2_Bor_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p2, f2_p2, f3_p2
        ) - e_c
        b_3t_p2_log_gg = _simplicial_energy(
            c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"], f1_p2, f2_p2, f3_p2
        ) - e_c

        print(
            f"{name:<6} {Z:>3} {N:>3} {A:>3} | "
            f"{f1_ch:>5} {f1_3t:>5} {f1_p1:>5} {f1_p2:>5} | "
            f"{mp.nstr(b_ame, 7):>10} {mp.nstr(b_legacy_bor, 7):>10} "
            f"{mp.nstr(b_1d_log_d, 7):>10} {mp.nstr(b_3t_log_d, 7):>10} "
            f"{mp.nstr(b_3t_p1_log_gg, 7):>10} {mp.nstr(b_3t_p2_log_gg, 7):>10} "
            f"{mp.nstr(b_3t_log_gg, 7):>10}"
        )

        rows_data.append({
            "nuclide": name,
            "Z": Z,
            "N": N,
            "A": A,
            "B_AME_MeV": fmt(b_ame),
            "sigma_AME_MeV": fmt(sigma_ame),
            "E_C_MeV": fmt(e_c),
            "f_vectors": {
                "chain_1D": {"f0": A, "f1": f1_ch, "f2": 0, "f3": 0},
                "complete_graph_KA": {
                    "f0": A,
                    "f1": _int_comb(A, 2),
                    "f2": _int_comb(A, 3),
                    "f3": _int_comb(A, 4),
                },
                "alpha_cluster_CA": {
                    "f0": A,
                    "f1": f1_cl,
                    "f1_intra": intra_alpha_edges(A),
                    "f1_inter": inter_cluster_edges(A),
                    "f2": f2_cl,
                    "f3": f3_cl,
                },
                "stacked_3tree_KA": {
                    "f0": A,
                    "f1": f1_3t,
                    "f2": f2_3t,
                    "f2_boundary": (2 * A - 4) if A >= 4 else 0,
                    "f2_interior": (A - 4) if A >= 4 else 0,
                    "f3": f3_3t,
                    "euler_char": A - f1_3t + f2_3t - f3_3t,
                },
                "pauli_bridge_degree1_3tree": {
                    "f0": A,
                    "A_core": 2 * (Z if Z <= N else N),
                    "N_excess": abs(N - Z),
                    "f1": f1_p1,
                    "f2": f2_p1,
                    "f3": f3_p1,
                    "euler_char": A - f1_p1 + f2_p1 - f3_p1,
                },
                "pauli_triangle_degree2_3tree": {
                    "f0": A,
                    "A_core": 2 * (Z if Z <= N else N),
                    "N_excess": abs(N - Z),
                    "f1": f1_p2,
                    "f2": f2_p2,
                    "f3": f3_p2,
                    "euler_char": A - f1_p2 + f2_p2 - f3_p2,
                },
            },
            "branches": {
                "legacy_borromean_allpairs_chiral": _err_metrics(b_legacy_bor, b_ame, sigma_ame),
                "chain_1D_logD": _err_metrics(b_1d_log_d, b_ame, sigma_ame),
                "chain_1D_BorD": _err_metrics(b_1d_bor_d, b_ame, sigma_ame),
                "alpha_cluster_logD_GPMT": _err_metrics(b_acl_log_d, b_ame, sigma_ame),
                "alpha_cluster_BorD_GPMT": _err_metrics(b_acl_bor_d, b_ame, sigma_ame),
                "alpha_cluster_logGG_GPMT": _err_metrics(b_acl_log_gg, b_ame, sigma_ame),
                "stacked_3tree_logD_GPMT": _err_metrics(b_3t_log_d, b_ame, sigma_ame),
                "stacked_3tree_BorGraph_GPMT": _err_metrics(b_3t_bor_graph, b_ame, sigma_ame),
                "stacked_3tree_BorAdd_GPMT": _err_metrics(b_3t_bor_add, b_ame, sigma_ame),
                "stacked_3tree_logGG_GPMT": _err_metrics(b_3t_log_gg, b_ame, sigma_ame),
                "pauli_bridge_3tree_logD_GPMT": _err_metrics(b_3t_p1_log_d, b_ame, sigma_ame),
                "pauli_bridge_3tree_BorD_GPMT": _err_metrics(b_3t_p1_bor_d, b_ame, sigma_ame),
                "pauli_bridge_3tree_logGG_GPMT": _err_metrics(b_3t_p1_log_gg, b_ame, sigma_ame),
                "pauli_triangle_3tree_logD_GPMT": _err_metrics(b_3t_p2_log_d, b_ame, sigma_ame),
                "pauli_triangle_3tree_BorD_GPMT": _err_metrics(b_3t_p2_bor_d, b_ame, sigma_ame),
                "pauli_triangle_3tree_logGG_GPMT": _err_metrics(b_3t_p2_log_gg, b_ame, sigma_ame),
            },
        })

    wb.add_data("benchmark_nuclei", rows_data)

    # Structural assertions corresponding to the Lean 4 theorems in AlphaSimplexCoordinationDerivation.lean
    euler_all_one = all(
        (f0_simplex(Z_i + N_i) - f1_simplex(Z_i + N_i) + f2_simplex(Z_i + N_i) - f3_simplex(Z_i + N_i) == 1)
        for _, Z_i, N_i in BENCHMARK_NUCLEI
    )
    wb.add_assertion(
        name="stacked_3simplex_euler_characteristic_is_one",
        computed="1" if euler_all_one else "0",
        expected="1",
        tolerance="0",
    )

    euler_pauli_both_one = all(
        (
            (Z_i + N_i) - pauli_bridge_f_vector(Z_i, N_i)[0]
            + pauli_bridge_f_vector(Z_i, N_i)[1] - pauli_bridge_f_vector(Z_i, N_i)[2] == 1
        )
        and (
            (Z_i + N_i) - pauli_triangle_f_vector(Z_i, N_i)[0]
            + pauli_triangle_f_vector(Z_i, N_i)[1] - pauli_triangle_f_vector(Z_i, N_i)[2] == 1
        )
        for _, Z_i, N_i in BENCHMARK_NUCLEI
    )
    wb.add_assertion(
        name="pauli_bridge_and_triangle_excess_euler_characteristic_is_one",
        computed="1" if euler_pauli_both_one else "0",
        expected="1",
        tolerance="0",
    )

    wb.add_assertion(
        name="gpmt_h4_cumulant_sign_window_mu3_pos_mu4_neg",
        computed="1" if (c["mu3GPMT_H4"] > mp.mpf(0) and c["mu4GPMT_H4"] < mp.mpf(0)) else "0",
        expected="1",
        tolerance="0",
    )

    # Verify linear extensivity identity on 56Fe (A = 56 >= 3)
    a_fe = 56
    lhs_fe = _simplicial_energy(
        c["b2_log_D_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"],
        f1_simplex(a_fe), f2_simplex(a_fe), f3_simplex(a_fe),
    )
    rhs_fe = (
        c["vol_coeff_3tree_logD_GPMT_MeV"] * mp.mpf(a_fe)
        - c["bdry_deficit_3tree_logD_GPMT_MeV"]
    )
    wb.add_assertion(
        name="stacked_3simplex_affine_linear_extensivity_identity_exact",
        computed=fmt(abs(lhs_fe - rhs_fe)),
        expected="0",
        tolerance="1e-70",
    )

    # Verify Lean theorem `pauliExcess_symmetry_deficits_eq` on 208Pb (Z=82, N=126, D=44)
    z_pb, n_pb = 82, 126
    a_pb = z_pb + n_pb
    d_pb = n_pb - z_pb
    f1_pb_full, f2_pb_full, f3_pb_full = f1_simplex(a_pb), f2_simplex(a_pb), f3_simplex(a_pb)
    f1_pb_p1, f2_pb_p1, f3_pb_p1 = pauli_bridge_f_vector(z_pb, n_pb)
    f1_pb_p2, f2_pb_p2, f3_pb_p2 = pauli_triangle_f_vector(z_pb, n_pb)
    e_full_pb = _simplicial_energy(
        c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"],
        f1_pb_full, f2_pb_full, f3_pb_full,
    )
    e_p1_pb = _simplicial_energy(
        c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"],
        f1_pb_p1, f2_pb_p1, f3_pb_p1,
    )
    e_p2_pb = _simplicial_energy(
        c["b2_log_gg_MeV"], c["w3_GPMT_MeV"], c["w4_GPMT_H4_MeV"],
        f1_pb_p2, f2_pb_p2, f3_pb_p2,
    )
    def_p1_err = abs((e_full_pb - e_p1_pb) - c["pauli_bridge_deficit_per_excess_logGG_MeV"] * mp.mpf(d_pb))
    def_p2_err = abs((e_full_pb - e_p2_pb) - c["pauli_triangle_deficit_per_excess_logGG_MeV"] * mp.mpf(d_pb))
    wb.add_assertion(
        name="pauli_excess_symmetry_deficits_theorem_exact_on_208Pb",
        computed=fmt(def_p1_err + def_p2_err),
        expected="0",
        tolerance="1e-70",
    )

    out_path = wb.save()
    print("\n  Saved 80-dps witness -> " + str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
