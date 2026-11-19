#!/usr/bin/env python3
"""Per-Z shard producer for the recursive atom-knot atlas.

Extends `canonical_mass_table_extended.py` with full AME 2020
coverage. For every (Z, N) in AME 2020 (3558 nuclides), emits a
per-element shard `canonical-isotope-witness-Z<NN>.witness.json`
containing AME reference values + layered framework predictions
(where any layer has coverage).

Layers (per `docs/coordination/show-mass-sweep-table.md`):

  L1 — canonical |tr_M(β_atom, q_0)| via `markov_peel + mpmath`.
       Reachable for A ≤ 6 today (n_strands ≤ 18); ⁶Li ≈ 17 min
       wall, anything heavier requires the Rust path. We **reuse**
       existing canonical-mass-table-extended values rather than
       recompute.
  L2 — α-cluster recursion `B(nα) = n·B(⁴He) + C(n,2)·c_αα` via
       `alpha_cluster_recursion.py`. Covers Z = N, A = 4n: ⁴He,
       ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca.
  L3 — paper-six-term sweep (off by default; future extension).
  L4 — composite mass M(A, Z) = N·m_n + Z·m_p − B(A, Z) using
       Borromean nucleon masses + any-layer B.
  L5 — Q-values Q_β(A, Z) = M(A, Z) − M(A, Z+1) − m_e from
       adjacent-row L4 (future extension).

This script is intentionally a **read-many, compute-little**
orchestrator. The L1 / L2 predictions live in their producer
witnesses; canonical_isotope_witness assembles them by Z and adds
AME reference values + L4 composite + provenance.

CLI:
    python3 canonical_isotope_witness.py             # Z=0..20 default
    python3 canonical_isotope_witness.py --max-z 30  # Z=0..30
    python3 canonical_isotope_witness.py --z 1,2     # just H + He shards

Per repo-owner directive 2026-05-19: "expand to make sure all
isotopes. keep recursive knot atlas an integral part of mass /
beta / Q / binding pipeline." Plus user decisions (per
`/coordinate` AskUserQuestion 2026-05-19): AME 2020 data source,
per-Z shards, atlas per-Z sections.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.witness import load_and_hash_upstream  # noqa: E402
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_at,
    q_two_term_borromean_at,
    vol_4_1_at,
)
from codata_constants import U_MEV, M_E_MEV  # noqa: E402 — u→MeV factor (bean 46ke)
from canonical_mass import (  # noqa: E402
    e0_hadronic_tower_mev,
    gpmt_three_row_cumulants,
    neutron_mass_two_term_mev,
    np_qed_splitting_borromean_conn_mev,
    nucleon_mass_mev,
    proton_qed_self_energy_borromean_mev,
)
from coulomb_energy import (  # noqa: E402
    HBAR_C_MEV_FM,
    UNIFORM_SPHERE_FACTOR,
    alpha_em_hbar_c_mev_fm,
    nuclear_radius_fm,
)
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

# Raise precision before anything is built. U_MEV and M_E_MEV arrive from the
# registry as ~70-digit mpf and were being cast back down with float() at four
# sites; that discarded registry precision for no reason.
set_compute_dps(80)
mp.mp.dps = 80

_KILO = mp.mpf(10) ** 3
_MEGA = mp.mpf(10) ** 6
_HUNDRED = mp.mpf(100)


def _as_mpf(x):
    """Exact mpf from a JSON number, string, or mpf. None passes through.

    `mp.mpf(str(x))` and NOT `mp.mpf(x)`. The AME table stores decimal
    literals that json parses to float64, and `mpf(<float>)` would capture the
    binary tail instead of the decimal the file states: mpf(8071.31806) is
    8071.3180599999996048, while mpf(str(8071.31806)) is 8071.31806 exactly.
    Python's str() of a float is the shortest round-tripping repr, so this
    recovers the literal rather than inventing digits. That distinction is
    what `mpf_float_source_audit.py` exists to enforce.
    """
    if x is None:
        return None
    try:
        return x if isinstance(x, mp.mpf) else mp.mpf(str(x))
    except (TypeError, ValueError):
        return None


def _e(x):
    """Serialize a numeric field: full-precision string, or None."""
    return None if x is None else fmt(x)


# Zero-parameter magic-A binding B = 2·m_e·A·(8G)·ρ_F (Catalan's G; NO fit, NO
# AME) — used to DERIVE the ⁴He α-cluster anchor rather than feed AME back.
# magic_A_formula lives in computations/ (already on sys.path via HERE above +
# the _path_bridge); no extra path mutation needed.
from magic_A_formula import magic_A_binding  # noqa: E402


# ── Data loaders ──────────────────────────────────────────────────

def load_ame2020() -> dict:
    """Load the parsed AME 2020 reference data (data/ame2020.json)."""
    path = HERE / "data" / "ame2020.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found — run vendor_ame2020.py first."
        )
    return json.loads(path.read_text())


def load_layer1() -> dict:
    """Load the L1 canonical |tr_M| witness for p..⁶Li reuse."""
    path = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


def load_layer2() -> dict:
    """Load the L2 α-cluster recursion witness."""
    path = _pb.witness_path("alpha-cluster-recursion.witness.json", HERE / "alpha")
    return json.loads(path.read_text()) if path.exists() else {}


def load_layer3() -> dict:
    """Load the L3 low-isotope binding sweep (partial-shell)."""
    path = _pb.witness_path("low-isotope-binding-sweep.witness.json", HERE / "sweeps")
    return json.loads(path.read_text()) if path.exists() else {}


def load_borromean() -> dict:
    """Load m_p, m_n, m_μ from the Borromean tower witness."""
    path = _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


# ── Borromean nucleon-mass extraction ─────────────────────────────

def borromean_m_p_m_n(borromean: dict) -> tuple[mp.mpf | None, mp.mpf | None]:
    """Return 50-dps mpmath (m_p_pred_MeV, m_n_pred_MeV) from canonical_mass."""
    try:
        return nucleon_mass_mev("p"), nucleon_mass_mev("n")
    except Exception as e:
        print(f"Warning: could not load canonical_mass: {e}")
        return None, None


# ── Wave-2 Precomputation: Corrected Photon, Two-Term Lagrangian,
#    Exact 4x4 Hankel Plancherel Z_{3A}^{(4)}, & 3D Alpha-Simplex ──


def _solve_bring_schwinger_form_b_inv(q: mp.mpf) -> mp.mpf:
    """1-loop Form-B Bring–Schwinger cubic root alpha_EM^{-1}(q) at 85-dps mpmath:
      -H * h^2 * alpha^3 + H * alpha^2 + T * alpha - 1 = 0,
      T = q * [9]_q * [10]_q + 2 / (3 * pi),  H = [2]_q / (8 * pi),  h = q - 1/q.
    """
    with mp.workdps(95):
        one = mp.mpf(1)
        h = q - one / q
        h2 = h**2
        q2 = q + one / q
        q9 = (q**9 - q ** (-9)) / h
        q10 = (q**10 - q ** (-10)) / h
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = q2 / (mp.mpf(8) * mp.pi)
        a = (-t_term + mp.sqrt(t_term * t_term + mp.mpf(4) * h_term)) / (
            mp.mpf(2) * h_term
        )
        for _ in range(35):
            fa = -h_term * h2 * (a**3) + h_term * (a**2) + t_term * a - one
            dfa = -mp.mpf(3) * h_term * h2 * (a**2) + mp.mpf(2) * h_term * a + t_term
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf("1e-82"):
                break
        return +(one / a)


def _f1_simplex(A: int) -> int:
    if A <= 1:
        return 0
    if A == 2:
        return 1
    return 3 * A - 6


def _f2_simplex(A: int) -> int:
    if A <= 2:
        return 0
    return 3 * A - 8


def _f3_simplex(A: int) -> int:
    if A <= 3:
        return 0
    return A - 3


def _pauli_triangle_f_vector(Z: int, N: int) -> tuple[int, int, int]:
    """Maximal Pauli-legal excess attachment (`AlphaSimplexCoordinationDerivation.lean`)."""
    A = Z + N
    if A <= 3:
        return _f1_simplex(A), _f2_simplex(A), _f3_simplex(A)
    m_min = Z if Z <= N else N
    a_core = 2 * m_min
    d_excess = A - a_core
    if a_core == 0:
        return 0, 0, 0
    return (
        _f1_simplex(a_core) + 2 * d_excess,
        _f2_simplex(a_core) + d_excess,
        _f3_simplex(a_core),
    )


def _ground_state_su4_partition_fast(Z: int, N: int) -> tuple[int, ...]:
    """Exact O(1) ground-state <=4-row SU(4) spin-isospin partition of 3A."""
    Nu = 2 * Z + N
    Nd = Z + 2 * N
    pts = [(Nu + 1) // 2, Nu // 2, (Nd + 1) // 2, Nd // 2]
    return tuple(x for x in sorted(pts, reverse=True) if x > 0)


def _frobenius_W_lambda(
    lam: tuple[int, ...], q_int_tbl: list[mp.mpf], q_fact_tbl: list[mp.mpf]
) -> mp.mpf:
    """Exact W_lambda(q) = [n]_q! / prod [h]_q^2 via Frobenius shifted parts for l(lam) <= 4."""
    n = sum(lam)
    padded = list(lam) + [0] * (4 - len(lam))
    l1, l2, l3, l4 = padded[0] + 3, padded[1] + 2, padded[2] + 1, padded[3]
    vand = (
        q_int_tbl[l1 - l2]
        * q_int_tbl[l1 - l3]
        * q_int_tbl[l1 - l4]
        * q_int_tbl[l2 - l3]
        * q_int_tbl[l2 - l4]
        * q_int_tbl[l3 - l4]
    )
    den = q_fact_tbl[l1] * q_fact_tbl[l2] * q_fact_tbl[l3] * q_fact_tbl[l4]
    return q_fact_tbl[n] * (vand / den) ** 2


class _Hankel4RowPlancherelEvaluator:
    """Exact O(N^2) Andréief / Cauchy-Binet 4x4 Hankel evaluator for Z_n^{(4)}(q)."""

    def __init__(self, n_max: int, q: mp.mpf, q_fact_tbl: list[mp.mpf]) -> None:
        self.n_max = n_max
        self.N_max = n_max + 6
        self.q = q
        self.h = q - mp.mpf(1) / q
        self.q_fact_tbl = q_fact_tbl

        N = self.N_max
        one = mp.mpf(1)
        inv_fact_sq = [one / (q_fact_tbl[l] ** 2) for l in range(N + 1)]
        F: list[list[mp.mpf]] = [[mp.mpf(0)] * (N + 1) for _ in range(7)]
        for m in range(7):
            alpha = 2 * m - 6
            q_alpha = q**alpha
            p = one
            Fm = F[m]
            for l in range(N + 1):
                Fm[l] = p * inv_fact_sq[l]
                p *= q_alpha

        self.pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        self.comp = {
            (0, 1): (2, 3),
            (0, 2): (1, 3),
            (0, 3): (1, 2),
            (1, 2): (0, 3),
            (1, 3): (0, 2),
            (2, 3): (0, 1),
        }
        self.signs = {
            (0, 1): 1,
            (0, 2): -1,
            (0, 3): 1,
            (1, 2): 1,
            (1, 3): -1,
            (2, 3): 1,
        }

        needed: set[tuple[int, int]] = set()
        for a, b in self.pairs:
            for r, s in [(a, b + 1), (b, a + 1), (a + 2, b + 3), (b + 2, a + 3)]:
                needed.add((min(r, s), max(r, s)))

        # At q ~ 1.11, |i - j| > 140 is suppressed by q^{-9800} < 10^{-440} (exact 0 at 85 dps).
        band = 140
        self.prods: dict[tuple[int, int], list[mp.mpf]] = {}
        for r, s in sorted(needed):
            A_arr = F[r]
            B_arr = F[s]
            out = [mp.mpf(0)] * (N + 1)
            for i in range(N + 1):
                ai = A_arr[i]
                j_lo = max(0, i - band)
                j_hi = min(N - i, i + band)
                for j in range(j_lo, j_hi + 1):
                    out[i + j] += ai * B_arr[j]
            self.prods[(r, s)] = out

    def eval_Z4(self, n: int) -> mp.mpf:
        N = n + 6
        coeff_N = mp.mpf(0)
        for a, b in self.pairs:
            c, d = self.comp[(a, b)]
            sgn = self.signs[(a, b)]
            p01_pos = self.prods[(min(a, b + 1), max(a, b + 1))]
            p01_neg = self.prods[(min(b, a + 1), max(b, a + 1))]
            p23_pos = self.prods[(min(c + 2, d + 3), max(c + 2, d + 3))]
            p23_neg = self.prods[(min(d + 2, c + 3), max(d + 2, c + 3))]
            dot = mp.mpf(0)
            for k in range(N + 1):
                dot += (p01_pos[k] - p01_neg[k]) * (p23_pos[N - k] - p23_neg[N - k])
            if sgn == 1:
                coeff_N += dot
            else:
                coeff_N -= dot
        return self.q_fact_tbl[n] * coeff_N / (self.h**12)


def _precompute_wave2_tables(ame_entries: list[dict], z_max_needed: int = 118) -> dict[str, Any]:
    """Precompute once across all nuclides at 85-dps mpmath:
      - 1-term proton pin q_0 and 2-term Borromean proton pin q_2t
      - Form-B Bring–Schwinger cubic alpha_EM^{-1}(q_0) and alpha_EM^{-1}(q_2t)
      - Two-Term Categorical Lagrangian nucleon constituents (M = M_QCD + M_QED at q_2t)
      - Exact 4x4 Hankel Plancherel Z_{3A}^{(4)}(q_2t) for A = 1..A_max
      - 3D alpha-simplex bond & GPMT cumulant constants at bare E_0 and E_0^tower
      - q-CLT standard-channel bond logarithms for A > 40
    """
    from channel_binding import E0 as _cb_E0, bond_channels as _cb_bond_channels

    with mp.workdps(85):
        one = mp.mpf(1)
        m_e = mp.mpf(str(M_E_MEV))
        q0 = q_at(85)
        q2t = q_two_term_borromean_at(85, k_weighted=False)
        vol41 = vol_4_1_at(85)

        alpha_inv_b_q0 = _solve_bring_schwinger_form_b_inv(q0)
        alpha_inv_b_q2t = _solve_bring_schwinger_form_b_inv(q2t)
        alpha_hbar_c_1t = mp.mpf(str(alpha_em_hbar_c_mev_fm(q=q0)))
        alpha_hbar_c_b_q2t = mp.mpf(str(HBAR_C_MEV_FM)) / alpha_inv_b_q2t

        # Bare-Z hydrogenic shell binding at Form-B Bring–Schwinger alpha_EM(q_2t)
        ry_b_q2t_mev = m_e / (mp.mpf(2) * (alpha_inv_b_q2t**2))
        e_el_by_z: dict[int, mp.mpf] = {0: mp.mpf(0)}
        for z_val in range(1, max(z_max_needed, 118) + 1):
            tot_e, n_sh, rem = mp.mpf(0), 1, z_val
            while rem > 0:
                occ = min(2 * n_sh * n_sh, rem)
                tot_e += mp.mpf(occ * z_val * z_val) * ry_b_q2t_mev / mp.mpf(n_sh * n_sh)
                rem -= occ
                n_sh += 1
            e_el_by_z[z_val] = tot_e

        # Two-Term Categorical Lagrangian Trace M = M_QCD + M_QED at q_2t
        h_2t = q2t - one / q2t
        hbar_2t = (q2t - one) / q2t
        tr_bor_2t = abs(
            (mp.mpf(4) + h_2t**2 - mp.mpf(3) * h_2t**4 - h_2t**6)
            / (h_2t**2 + mp.mpf(4))
        )
        qf3_2t = (q2t**2 + one + q2t ** (-2)) * (q2t + one / q2t)
        f_bor_2t = tr_bor_2t * qf3_2t / (q2t**3)
        mp_qcd_q2t = m_e * (mp.mpf(2) * (vol41 / (hbar_2t**2)) * f_bor_2t - mp.mpf(12))
        mp_qed_q2t = mp.mpf(str(proton_qed_self_energy_borromean_mev(k_weighted=False, q=q2t)))
        mp_2t = mp_qcd_q2t + mp_qed_q2t
        dm_np_qed_q2t = mp.mpf(str(np_qed_splitting_borromean_conn_mev(weighting="plain", q=q2t)))
        mn_2t = mp.mpf(str(neutron_mass_two_term_mev(weighting="plain", q=q2t)))

        e0_bare_q0 = m_e / (q0 * (q0 - one))
        e0_tower_q0 = mp.mpf(str(e0_hadronic_tower_mev(q=q0)))
        e0_bare_q2t = m_e / (q2t * (q2t - one))
        e0_tower_q2t = mp.mpf(str(e0_hadronic_tower_mev(q=q2t)))
        tower_factor_q2t = e0_tower_q2t / e0_bare_q2t

        z_d_q2t = (q2t**3) / (q2t**2 + one)
        z_gg_q2t = z_d_q2t - h_2t / mp.mpf(2)
        b2_log_d_bare = e0_bare_q2t * mp.log(one / z_d_q2t)
        b2_log_gg_bare = e0_bare_q2t * mp.log(one / z_gg_q2t)

        gpmt_q2t = gpmt_three_row_cumulants(q=q2t)
        mu3_q2t = mp.mpf(str(gpmt_q2t["mu3GPMT"]))
        mu4_h4_q2t = mp.mpf(str(gpmt_q2t["mu4GPMT_H4"]))
        w3_gpmt_bare = e0_bare_q2t * mu3_q2t
        w4_gpmt_h4_bare = e0_bare_q2t * mu4_h4_q2t

        # Precompute [k]_q, [k]_q!, and 4x4 Hankel Z_{3A}^{(4)}(q_2t) for A = 1..A_max
        a_max = max((int(e["A"]) for e in ame_entries), default=295)
        n_max = 3 * a_max
        tbl_len = n_max + 8
        q_int_2t = [mp.mpf(0)] * (tbl_len + 1)
        q_fact_2t = [one] * (tbl_len + 1)
        for k in range(1, tbl_len + 1):
            qk = (q2t**k - q2t ** (-k)) / h_2t
            q_int_2t[k] = qk
            q_fact_2t[k] = q_fact_2t[k - 1] * qk

        hankel_2t = _Hankel4RowPlancherelEvaluator(n_max, q2t, q_fact_2t)
        z4_by_a: dict[int, mp.mpf] = {
            a_val: hankel_2t.eval_Z4(3 * a_val) for a_val in range(1, a_max + 1)
        }

        # Precompute nuclear radii R(A) for A = 1..A_max
        radius_by_a: dict[int, mp.mpf] = {
            a_val: mp.mpf(str(nuclear_radius_fm(a_val))) for a_val in range(1, a_max + 1)
        }

        # Precompute 80-dps q-CLT bond logs so Layer-4 A>40 runs in O(1) without float64
        e0_qclt = _cb_E0(80)
        ls_qclt = {
            b_kind: mp.log(one / _cb_bond_channels(b_kind, "numeric", 80)["std"])
            for b_kind in ("pp", "pn", "nn")
        }

        return {
            "q0": q0,
            "q2t": q2t,
            "m_e": m_e,
            "alpha_inv_b_q0": alpha_inv_b_q0,
            "alpha_inv_b_q2t": alpha_inv_b_q2t,
            "alpha_hbar_c_1t": alpha_hbar_c_1t,
            "alpha_hbar_c_b_q2t": alpha_hbar_c_b_q2t,
            "e_el_by_z": e_el_by_z,
            "mp_qcd_q2t": mp_qcd_q2t,
            "mp_qed_q2t": mp_qed_q2t,
            "mp_2t": mp_2t,
            "dm_np_qed_q2t": dm_np_qed_q2t,
            "mn_2t": mn_2t,
            "e0_bare_q0": e0_bare_q0,
            "e0_tower_q0": e0_tower_q0,
            "e0_bare_q2t": e0_bare_q2t,
            "e0_tower_q2t": e0_tower_q2t,
            "tower_factor_q2t": tower_factor_q2t,
            "b2_log_d_bare": b2_log_d_bare,
            "b2_log_gg_bare": b2_log_gg_bare,
            "w3_gpmt_bare": w3_gpmt_bare,
            "w4_gpmt_h4_bare": w4_gpmt_h4_bare,
            "q_int_2t": q_int_2t,
            "q_fact_2t": q_fact_2t,
            "z4_by_a": z4_by_a,
            "radius_by_a": radius_by_a,
            "e0_qclt": e0_qclt,
            "ls_qclt": ls_qclt,
        }


def _build_wave2_row_block(
    Z: int,
    N: int,
    A: int,
    b_ame_mev: mp.mpf | None,
    m_atom_ame_mev: mp.mpf | None,
    w2: dict[str, Any],
) -> dict[str, Any]:
    """Build per-nuclide Wave-2 `two_term_qed_and_3d_simplex` block at 80-dps mpmath."""
    lam = _ground_state_su4_partition_fast(Z, N)
    w_lam_2t = _frobenius_W_lambda(lam, w2["q_int_2t"], w2["q_fact_2t"])
    z4_3a = w2["z4_by_a"][A]
    omega_4row = w_lam_2t / z4_3a

    if Z < 2 or A < 2:
        ec_1t = mp.mpf(0)
        ec_b_q2t = mp.mpf(0)
    else:
        ustr_fac = mp.mpf(str(UNIFORM_SPHERE_FACTOR)) * mp.mpf(Z * (Z - 1)) / w2["radius_by_a"][A]
        ec_1t = ustr_fac * w2["alpha_hbar_c_1t"]
        ec_b_q2t = ustr_fac * w2["alpha_hbar_c_b_q2t"]

    f1 = _f1_simplex(A)
    f2 = _f2_simplex(A)
    f3 = _f3_simplex(A)
    f1_pt, f2_pt, f3_pt = _pauli_triangle_f_vector(Z, N)

    tf = w2["tower_factor_q2t"]
    b2_d = w2["b2_log_d_bare"]
    b2_gg = w2["b2_log_gg_bare"]
    w3 = w2["w3_gpmt_bare"]
    w4 = w2["w4_gpmt_h4_bare"]

    b_3tree_logd_bare = mp.mpf(f1) * b2_d + mp.mpf(f2) * w3 + mp.mpf(f3) * w4
    b_3tree_logd_tower = b_3tree_logd_bare * tf
    b_3tree_logd_tower_net = b_3tree_logd_tower - ec_b_q2t

    b_3tree_gg_bare = mp.mpf(f1) * b2_gg + mp.mpf(f2) * w3 + mp.mpf(f3) * w4
    b_3tree_gg_tower = b_3tree_gg_bare * tf
    b_3tree_gg_tower_net = b_3tree_gg_tower - ec_b_q2t

    b_pt_gg_tower = (mp.mpf(f1_pt) * b2_gg + mp.mpf(f2_pt) * w3 + mp.mpf(f3_pt) * w4) * tf
    b_pt_gg_tower_net = b_pt_gg_tower - ec_b_q2t

    mp_2t = w2["mp_2t"]
    mn_2t = w2["mn_2t"]
    m_e = w2["m_e"]
    e_el = w2["e_el_by_z"].get(Z, mp.mpf(0))
    qed_nucleon_shift = (
        mp.mpf(Z) * w2["mp_qed_q2t"]
        + mp.mpf(N) * (w2["mp_qed_q2t"] + w2["dm_np_qed_q2t"])
    )
    m_constit_2t = mp.mpf(Z) * mp_2t + mp.mpf(N) * mn_2t + mp.mpf(Z) * m_e - e_el
    b_simplex_used = mp.mpf(0) if A <= 1 else b_pt_gg_tower_net
    m_atom_2t_simplex = m_constit_2t - b_simplex_used

    m_atom_err_mev = (
        m_atom_2t_simplex - m_atom_ame_mev
        if m_atom_ame_mev is not None
        else None
    )
    m_atom_err_ppm = (
        m_atom_err_mev / m_atom_ame_mev * _MEGA
        if (m_atom_err_mev is not None and m_atom_ame_mev)
        else None
    )
    b_pt_err_mev = (
        b_pt_gg_tower_net - b_ame_mev
        if (A >= 2 and b_ame_mev is not None)
        else None
    )

    return {
        "q2t_pin": _e(w2["q2t"]),
        "alpha_em_inv_bring_schwinger_q2t": _e(w2["alpha_inv_b_q2t"]),
        "E_electron_bring_schwinger_q2t_MeV": _e(e_el),
        "coulomb_energy_1term_MeV": _e(ec_1t),
        "coulomb_energy_bring_schwinger_q2t_MeV": _e(ec_b_q2t),
        "qed_nucleon_shift_q2t_MeV": _e(qed_nucleon_shift),
        "M_constituent_two_term_q2t_MeV": _e(m_constit_2t),
        "su4_partition": list(lam),
        "W_lambda_unnormalized_q2t": _e(w_lam_2t),
        "Z_3A_4row_hankel_q2t": _e(z4_3a),
        "omega_lambda_normalized_4row_q2t": _e(omega_4row),
        "f_vector_3tree": [A, f1, f2, f3],
        "f_vector_pauli_triangle": [A, f1_pt, f2_pt, f3_pt],
        "B_3tree_logD_gpmt_MeV": _e(b_3tree_logd_bare),
        "B_3tree_logD_gpmt_E0tower_MeV": _e(b_3tree_logd_tower),
        "B_3tree_logD_gpmt_E0tower_net_MeV": _e(b_3tree_logd_tower_net),
        "B_3tree_gg_gpmt_MeV": _e(b_3tree_gg_bare),
        "B_3tree_gg_gpmt_E0tower_MeV": _e(b_3tree_gg_tower),
        "B_3tree_gg_gpmt_E0tower_net_MeV": _e(b_3tree_gg_tower_net),
        "B_pauli_triangle_gg_gpmt_E0tower_net_MeV": _e(b_pt_gg_tower_net),
        "B_pauli_triangle_err_MeV": _e(b_pt_err_mev),
        "M_atom_two_term_pauli_simplex_MeV": _e(m_atom_2t_simplex),
        "M_atom_two_term_err_MeV": _e(m_atom_err_mev),
        "M_atom_two_term_err_ppm": _e(m_atom_err_ppm),
    }


# ── L1 / L2 lookups ───────────────────────────────────────────────

def l1_lookup(Z: int, N: int, layer1: dict) -> dict | None:
    """Return the L1 row for (Z, N) if present in canonical-extended."""
    rows = layer1.get("data", {}).get("rows", [])
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


def l2_lookup(Z: int, N: int, layer2: dict) -> dict | None:
    """Return the L2 (α-cluster) row for (Z, N) if present.

    The alpha-cluster witness is hand-written (predates the
    WitnessBuilder convention) and stores rows at the top level,
    not under `data`. Probe both shapes.
    """
    rows = (
        layer2.get("data", {}).get("rows")
        or layer2.get("rows")
        or []
    )
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


def l3_lookup(Z: int, N: int, layer3: dict) -> dict | None:
    """Return the L3 partial-shell / census row for (Z, N).

    L3 covers odd-A and non-magic light isotopes (⁷Li, ⁹Be, ¹¹B,
    ¹⁴N, ¹⁹F, etc.) via partial-shell interpolation between
    α-cluster anchor points. Accuracy is 5–36 % (worst at half-
    filled shells); use as a fallback after L1 / L2.
    """
    rows = (
        layer3.get("data", {}).get("rows")
        or layer3.get("rows")
        or []
    )
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


# ── Row assembly ──────────────────────────────────────────────────

def assemble_row(
    ame_entry: dict, layer1: dict, layer2: dict, layer3: dict,
    m_p_borr: mp.mpf | None, m_n_borr: mp.mpf | None,
    w2: dict[str, Any],
) -> dict:
    """Compose a per-nuclide row from AME reference + L1/L2 layers."""
    Z = ame_entry["Z"]
    N = ame_entry["N"]
    A = ame_entry["A"]
    element = ame_entry["element"]

    # Reference values from AME 2020 (B in MeV, m_excess in MeV;
    # the AME file stores keV → convert).
    b_ame_keV = _as_mpf(ame_entry.get("binding_energy_total_keV"))
    b_ame_mev = b_ame_keV / _KILO if b_ame_keV is not None else None
    me_keV = _as_mpf(ame_entry.get("mass_excess_keV"))
    me_mev = me_keV / _KILO if me_keV is not None else None
    qbeta_keV = _as_mpf(ame_entry.get("beta_decay_energy_keV"))
    qbeta_mev = qbeta_keV / _KILO if qbeta_keV is not None else None
    atomic_mass_u = _as_mpf(ame_entry.get("atomic_mass_micro_u"))
    if atomic_mass_u is not None:
        atomic_mass_u = atomic_mass_u / _MEGA  # micro-u → u

    # Free nucleons (Z+N=1): mass prediction track.
    is_nucleon = (Z, N) in [(1, 0), (0, 1)]
    if is_nucleon:
        l1 = l1_lookup(Z, N, layer1)
        # `prediction_MeV_50dps` is a 50-digit string. float() on a field whose
        # NAME states its precision was the single clearest defect here.
        m_pred = (
            _as_mpf(l1.get("prediction_MeV_50dps"))
            if (l1 and l1.get("prediction_MeV_50dps")) else None
        )
        m_ref = (
            _as_mpf(l1.get("B_AME_MeV"))
            if (l1 and l1.get("B_AME_MeV") is not None) else None
        )
        m_err = m_pred - m_ref if (m_pred is not None and m_ref is not None) else None
        m_err_ppm = (m_err / m_ref * _MEGA) if (m_err is not None and m_ref) else None

        m_composite_MeV = None
        m_composite_ref_MeV = atomic_mass_u * U_MEV if atomic_mass_u is not None else None
        m_composite_err_MeV = None
        m_composite_err_ppm = None
        
        if m_p_borr is not None and m_n_borr is not None:
            m_composite_MeV = (N * _as_mpf(m_n_borr) + Z * _as_mpf(m_p_borr)
                               + Z * M_E_MEV)
            if m_composite_ref_MeV is not None:
                m_composite_err_MeV = m_composite_MeV - m_composite_ref_MeV
                m_composite_err_ppm = (m_composite_err_MeV / m_composite_ref_MeV * _MEGA) if m_composite_ref_MeV else None
                
        w2_block = _build_wave2_row_block(
            Z, N, A, b_ame_mev, m_composite_ref_MeV, w2
        )
        return {
            "Z": Z, "N": N, "A": A, "element": element,
            "prediction_type": "mass",
            "layer": "L1-borromean-via-canonical",
            "canonical_status": "borromean-tower-via-fitted-lambda",
            "prediction_MeV_50dps": (
                l1.get("prediction_MeV_50dps") if l1 else None
            ),
            "reference_MeV_50dps": _e(m_ref),
            "err_MeV": _e(m_err),
            "err_ppm": _e(m_err_ppm),
            "composite_mass": {
                "M_pred_MeV": _e(m_composite_MeV),
                "M_AME_MeV": _e(m_composite_ref_MeV),
                "err_MeV": _e(m_composite_err_MeV),
                "err_ppm": _e(m_composite_err_ppm),
                "canonical_status": "borromean-tower-via-fitted-lambda",
                "formula": "N·m_n + Z·m_p + Z·m_e − B(A,Z)",
                "m_p_source": "borromean-tower (conj:borromean-baryon-mass-formula)" if m_p_borr is not None else None,
                "B_source": "L1-borromean-via-canonical"
            },
            "two_term_qed_and_3d_simplex": w2_block,
            "ame_reference": {
                "B_AME_keV": _e(b_ame_keV),  # 0 for free nucleons
                "mass_excess_keV": _e(me_keV),
                "atomic_mass_u": _e(atomic_mass_u),
                "Q_beta_keV": _e(qbeta_keV),
            },
        }

    # Composite nuclei: binding-energy prediction (D and up).
    #
    # Selection is CANONICITY-FIRST (user directive 2026-06-02 "excise
    # all non-canonical"): production emits a binding prediction ONLY
    # from a genuinely canonical layer (the α-cluster recursion). We do
    # NOT fall through layer order L1→L2→L3 — that previously let L1's
    # empirical (knot, ρ_K) assignment mask ⁴He's α-cluster row. Any
    # non-canonical value is recorded under `excised` for the audit
    # trail, never shipped as a prediction.
    #   NB (2026-07-11, owner ruling "derive, don't anchor"): the ⁴He
    #   α-cluster cell (n_α=1,pairs=0) now ships the zero-parameter magic-A
    #   DERIVATION (≈29.96 MeV, 5.87% off AME) — not the AME anchor reflected
    #   through the identity (which gave a fake ~0.08 ppm). See the α-cluster
    #   candidate block below.
    l1 = l1_lookup(Z, N, layer1)
    l2 = l2_lookup(Z, N, layer2)
    l3 = l3_lookup(Z, N, layer3)

    # Canonical candidates: the α-cluster recursion (canonical-recursive;
    # c_αα = m_e·Vol(7²₁) is canonical). Present in L2 and/or the L3 sweep.
    canonical_candidates: list[tuple[float, str, str]] = []
    if l2 and _as_mpf(l2.get("B_pred_MeV")) is not None:
        canonical_candidates.append(
            (_as_mpf(l2["B_pred_MeV"]), "L2-alpha-cluster", "canonical-recursive")
        )
    if (l3 and str(l3.get("strategy", "")).startswith("α-cluster")
            and _as_mpf(l3.get("B_pred_MeV")) is not None):
        # DERIVE-DON'T-ANCHOR (2026-07-11, owner ruling): the α-cluster ANCHOR
        # cell — n_α=1, pairs=0 — is the trivial identity B_pred = 1·B(⁴He) +
        # 0·c_αα = B(⁴He) itself. The L3 sweep fed that ⁴He value from AME
        # (28.29566), so the row was the AME anchor reflected through the
        # identity — its ~0.08 ppm "accuracy" was an anchor tautology, and it
        # DISAGREED with the ⁴He anchor the heavier α-nuclei actually use (the
        # magic-A value, via L2). We instead ship the genuine ZERO-PARAMETER
        # magic-A derivation B(⁴He) = 2·m_e·A·(8G)·ρ_F ≈ 29.96 MeV (5.87% off
        # AME; no fit, no AME) — a real prediction, and now self-consistent
        # with the recursion anchor. Genuine recursion (n_α≥2) keeps the L3
        # value. High-accuracy (sub-%) B(⁴He) stays OPEN (needs the Δ_λ closed
        # form). NB: heavier α-nuclei are shipped by L2 (magic-A anchored), so
        # this branch ships only ⁴He in practice.
        _strat = str(l3["strategy"])
        _is_anchor_identity = ("n_α=1" in _strat and "pairs=0" in _strat)
        if _is_anchor_identity:
            _magic = magic_A_binding(Z, N)  # dict, or None if inapplicable
            # Gate the derived path on applicable==True (Copilot): only tag
            # magic-A-derived when magic-A actually applies AND yields a value.
            _applicable = bool(_magic and _magic.get("applicable"))
            _b_derived = _as_mpf(_magic.get("B_pred_MeV")) if _applicable else None
            if _b_derived is not None:
                _b_val = _b_derived
                _layer_tag = "L3-α-cluster:n_α=1,pairs=0(magic-A-derived)"
            else:
                # magic-A inapplicable — fall back to the L3 value; tag honestly.
                _b_val = _as_mpf(l3["B_pred_MeV"])
                _layer_tag = "L3-α-cluster:n_α=1,pairs=0(L3-fallback)"
        else:
            _b_val = _as_mpf(l3["B_pred_MeV"])
            _layer_tag = f"L3-{l3['strategy']}"
        canonical_candidates.append((_b_val, _layer_tag, "canonical-recursive"))

    # Layer 4 — heavy nuclei (A > 40) | Brane-tower asymptotic (q-CLT)
    if A > 40:
        # 1. Canonical macroscopic strong binding from the q-CLT colour-weighted form
        # (80-dps mpmath via precomputed standard-channel bond logarithms, zero float64)
        n_pp = Z * (Z - 1) // 2
        n_pn = Z * N
        n_nn = N * (N - 1) // 2
        tot_bonds = n_pp + n_pn + n_nn
        ls_qclt = w2["ls_qclt"]
        mean_l = (
            mp.mpf(n_pp) * ls_qclt["pp"]
            + mp.mpf(n_pn) * ls_qclt["pn"]
            + mp.mpf(n_nn) * ls_qclt["nn"]
        ) / mp.mpf(tot_bonds)
        b_strong = w2["e0_qclt"] * mp.mpf(A - 1) * mean_l

        # 2. Subtract the canonical Coulomb repulsion
        e_coulomb = (
            mp.mpf(0)
            if Z < 2
            else mp.mpf(str(UNIFORM_SPHERE_FACTOR))
            * mp.mpf(Z * (Z - 1))
            * w2["alpha_hbar_c_1t"]
            / w2["radius_by_a"][A]
        )

        l4_pred = b_strong - e_coulomb

        # HONEST SCOPE (re-scoped 2026-07-11): this is an A→∞ statistical
        # EXTRAPOLATION (q-CLT colour-weighted − Coulomb), NOT a canonical
        # closed-form derivation.  On the AME range it under-binds heavy
        # nuclei by ~72–89% (e.g. the Fe isotopes capture only ~11–28% of
        # the actual binding).  It therefore ships as an ASYMPTOTIC
        # APPROXIMATION, not "canonical-recursive".  The categorical
        # closed form for A>40 is OPEN — do not relabel this canonical.
        canonical_candidates.append(
            (l4_pred, "L4-qclt-colour-weighted", "asymptotic-approximation")
        )

    # Non-canonical candidates (recorded as excised, never shipped):
    #   • L3 census  B = ρ·Vol(census-knot), ρ hand-assigned
    #   • L3 partial-shell  linear interpolation between α anchors
    noncanonical_candidates: list[tuple[float, str, str]] = []
    if l1 and _as_mpf(l1.get("prediction_MeV_50dps")) is not None:
        noncanonical_candidates.append(
            (_as_mpf(l1["prediction_MeV_50dps"]), "L1-canonical",
             "canonical-with-empirical-assignment")
        )
    if (l3 and not str(l3.get("strategy", "")).startswith("α-cluster")
            and _as_mpf(l3.get("B_pred_MeV")) is not None):
        noncanonical_candidates.append(
            (_as_mpf(l3["B_pred_MeV"]),
             f"L3-{l3.get('strategy', 'partial-shell')}", "heuristic")
        )

    b_pred: float | None = None
    layer_used: str | None = None
    canonical_status: str = "pending"
    excised: dict | None = None
    if canonical_candidates:
        b_pred, layer_used, canonical_status = canonical_candidates[0]
    elif noncanonical_candidates:
        b_pred, layer_used, canonical_status = noncanonical_candidates[0]
        excised = {
            "excised_layer": layer_used,
            "excised_status": canonical_status,
            "excised_prediction_MeV": _e(_as_mpf(b_pred)),
            "reason": "non-canonical (heuristic / empirical-assignment)",
        }
    else:
        layer_used = "derivation-pending"
        canonical_status = "pending"

    b_pred = _as_mpf(b_pred)
    err_MeV = (b_pred - b_ame_mev) if (b_pred is not None and b_ame_mev is not None) else None
    err_pct = (err_MeV / b_ame_mev * _HUNDRED) if (err_MeV is not None and b_ame_mev) else None
    err_ppm = (err_MeV / b_ame_mev * _MEGA) if (err_MeV is not None and b_ame_mev) else None

    # L4 composite mass: M = N·m_n + Z·m_p − B
    # CANONICAL ONLY (per user directive 2026-05-19): emit only when
    # B comes from a canonical-status layer (canonical-substrate,
    # canonical-with-empirical-assignment, canonical-recursive). The
    # heuristic L3 partial-shell and the pending atoms get NO
    # composite mass — those rows surface as L?-derivation-pending in
    # the atlas.
    m_composite_MeV: float | None = None
    composite_canonical_status: str = "pending"
    if (
        m_p_borr is not None
        and m_n_borr is not None
        and b_pred is not None
        and canonical_status in (
            "canonical-substrate",
            "canonical-with-empirical-assignment",
            "canonical-recursive",
            "asymptotic-approximation",  # L4 A>40 q-CLT extrapolation (approx, not canonical)
        )
    ):
        m_composite_MeV = (N * _as_mpf(m_n_borr) + Z * _as_mpf(m_p_borr)
                           + Z * M_E_MEV - b_pred)
        composite_canonical_status = canonical_status

    # L4 reference: from AME atomic mass (× u→MeV, registry U_MEV ≈ 931.494).
    m_composite_ref_MeV = (
        atomic_mass_u * U_MEV if atomic_mass_u is not None else None
    )
    m_composite_err_MeV = (
        m_composite_MeV - m_composite_ref_MeV
        if (m_composite_MeV is not None and m_composite_ref_MeV is not None)
        else None
    )
    m_composite_err_ppm = (
        m_composite_err_MeV / m_composite_ref_MeV * _MEGA
        if (m_composite_err_MeV is not None and m_composite_ref_MeV)
        else None
    )

    w2_block = _build_wave2_row_block(
        Z, N, A, b_ame_mev, m_composite_ref_MeV, w2
    )

    return {
        "Z": Z, "N": N, "A": A, "element": element,
        "prediction_type": "binding_energy",
        "layer": layer_used or "L?-pending",
        "canonical_status": canonical_status,
        "prediction_MeV_50dps": _e(b_pred),
        "reference_MeV_50dps": _e(b_ame_mev),
        "err_MeV": _e(err_MeV),
        "err_pct": _e(err_pct),
        "err_ppm": _e(err_ppm),
        "excised": excised,
        # L4 composite mass — emitted ONLY when B is canonical
        # (canonical_status ∈ {canonical-substrate,
        # canonical-with-empirical-assignment, canonical-recursive}).
        # No AME B fallback. heuristic / pending rows get None here.
        "composite_mass": {
            "M_pred_MeV": _e(m_composite_MeV),
            "M_AME_MeV": _e(m_composite_ref_MeV),
            "err_MeV": _e(m_composite_err_MeV),
            "err_ppm": _e(m_composite_err_ppm),
            "canonical_status": composite_canonical_status,
            "formula": "N·m_n + Z·m_p − B(A,Z)",
            "m_p_source": (
                "borromean-tower (conj:borromean-baryon-mass-formula)"
                if m_p_borr is not None else None
            ),
            "B_source": layer_used,
        },
        "two_term_qed_and_3d_simplex": w2_block,
        "ame_reference": {
            "B_AME_keV": _e(b_ame_keV),
            "mass_excess_keV": _e(me_keV),
            "atomic_mass_u": _e(atomic_mass_u),
            "Q_beta_keV": _e(qbeta_keV),
            "estimated": (
                ame_entry.get("binding_energy_per_A_estimated")
                or ame_entry.get("mass_excess_estimated")
            ),
        },
    }


# ── Shard emitter ────────────────────────────────────────────────

def emit_z_shard(
    Z: int, rows: list[dict],
    upstream_records: list[dict],
    w2: dict[str, Any],
) -> Path:
    """Emit canonical-isotope-witness-Z<NN>.json for the given Z."""
    n_with_pred = sum(1 for r in rows if r.get("prediction_MeV_50dps") is not None)
    n_with_composite = sum(
        1 for r in rows
        if r.get("composite_mass", {}).get("M_pred_MeV") is not None
    )
    el = rows[0]["element"] if rows else "?"
    builder = (
        WitnessBuilder(
            f"canonical-isotope-witness-Z{Z:02d}",
            engine="python+mpmath",
        )
        .set_description(
            f"Per-Z={Z} shard of the recursive atom-knot atlas. "
            f"Element: {el}. Covers every (Z={Z}, N) in AME 2020. "
            "Each row carries: prediction_type ∈ {mass, "
            "binding_energy}; the prediction value (from L1 "
            "canonical |tr_M| via markov_peel+mpmath, OR L2 "
            "α-cluster recursion); the AME 2020 reference; "
            "err in MeV / % / ppm; L4 composite mass M = N·m_n "
            "+ Z·m_p − B (when nucleon masses + B are available); "
            "and Wave-2 Corrected Photon (Form-B Bring–Schwinger "
            "cubic alpha_EM(q_2t)), Two-Term Categorical Lagrangian "
            "Trace (M = M_QCD + M_QED at consistent q_2t), exact "
            "4x4 Hankel Plancherel Z_{3A}^{(4)}(q_2t), and 3D "
            "stacked alpha-simplex + E_0^tower binding. "
            "L1 source: canonical-mass-table-extended.witness.json; "
            "L2 source: alpha/alpha-cluster-recursion.witness.json; "
            "nucleon masses: m-p-substrate-identity-50dps.witness.json."
        )
        .add_parameter("Z", Z)
        .add_parameter("element", el)
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("q_2t_two_term_borromean", _e(w2["q2t"]))
        .add_parameter("alpha_em_inv_bring_schwinger_q2t", _e(w2["alpha_inv_b_q2t"]))
        .add_parameter("E0_bare_q2t_MeV", _e(w2["e0_bare_q2t"]))
        .add_parameter("E0_tower_q2t_MeV", _e(w2["e0_tower_q2t"]))
        .add_parameter("m_p_two_term_q2t_MeV", _e(w2["mp_2t"]))
        .add_parameter("m_n_two_term_q2t_MeV", _e(w2["mn_2t"]))
        .add_parameter("rows_total", len(rows))
        .add_parameter("rows_with_prediction", n_with_pred)
        .add_parameter("rows_with_composite_mass", n_with_composite)
        .add_data("rows", rows)
        .add_upstream_records(upstream_records)
    )
    out = builder.save({
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
    })
    wdata = json.loads(out.read_text(encoding="utf-8"))
    if isinstance(wdata.get("environment"), dict) and "clarabel" not in wdata["environment"]:
        wdata["environment"]["clarabel"] = "0.11.1"
        out.write_text(json.dumps(wdata, indent=2) + "\n", encoding="utf-8")
    return out


def emit_index(
    shards_written: list[tuple[int, Path]],
    ame_data: dict,
) -> Path:
    """Emit canonical-isotope-witness-index.json (cross-shard summary)."""
    by_z = {}
    for Z, path in shards_written:
        try:
            shard = json.loads(path.read_text())
            data = shard.get("data", {})
            by_z[Z] = {
                "shard_filename": path.name,
                "element": shard.get("parameters", {}).get("element"),
                "rows_total": shard.get("parameters", {}).get("rows_total"),
                "rows_with_prediction": shard.get("parameters", {}).get(
                    "rows_with_prediction"
                ),
                "rows_with_composite_mass": shard.get("parameters", {}).get(
                    "rows_with_composite_mass"
                ),
            }
        except (json.JSONDecodeError, OSError):
            pass

    builder = (
        WitnessBuilder(
            "canonical-isotope-witness-index", engine="python"
        )
        .set_description(
            "Cross-shard index for the per-Z canonical-isotope "
            "witness family. Each shard "
            "(canonical-isotope-witness-Z<NN>.witness.json) "
            "covers one element's isotope chain; this index "
            "aggregates the coverage map."
        )
        .add_parameter("n_shards", len(shards_written))
        .add_parameter("z_min", min(z for z, _ in shards_written) if shards_written else None)
        .add_parameter("z_max", max(z for z, _ in shards_written) if shards_written else None)
        .add_parameter("ame_source", ame_data.get("_metadata", {}).get("source"))
        .add_parameter("ame_entries", ame_data.get("_metadata", {}).get("n_entries"))
        .add_data("by_Z", by_z)
    )
    out = builder.save({
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
    })
    wdata = json.loads(out.read_text(encoding="utf-8"))
    if isinstance(wdata.get("environment"), dict) and "clarabel" not in wdata["environment"]:
        wdata["environment"]["clarabel"] = "0.11.1"
        out.write_text(json.dumps(wdata, indent=2) + "\n", encoding="utf-8")
    return out


# ── Main ──────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-z", type=int, default=20,
        help="Maximum Z to emit (default 20). Use 118 for full AME 2020."
    )
    parser.add_argument(
        "--z", default=None,
        help="Comma-separated explicit Z list (overrides --max-z)."
    )
    args = parser.parse_args(argv)

    ame = load_ame2020()
    layer1 = load_layer1()
    layer2 = load_layer2()
    layer3 = load_layer3()
    borromean = load_borromean()
    m_p_borr, m_n_borr = borromean_m_p_m_n(borromean)

    if args.z:
        z_list = [int(s.strip()) for s in args.z.split(",") if s.strip()]
    else:
        z_list = list(range(0, args.max_z + 1))

    # Bucket entries by Z.
    by_z: dict[int, list[dict]] = {z: [] for z in z_list}
    for entry in ame.get("entries", []):
        Z = entry["Z"]
        if Z in by_z:
            by_z[Z].append(entry)

    # Sort each bucket by N (rising isotope chain).
    for Z in by_z:
        by_z[Z].sort(key=lambda e: e["N"])

    print(f"  canonical_isotope_witness — Z = {z_list[0]}..{z_list[-1]}")
    print(f"  Borromean nucleon refs: m_p = {m_p_borr}, m_n = {m_n_borr}")
    print()
    print(f"  {'Z':>3}  {'element':<8}  {'rows':>5}  {'with_pred':>10}  {'with_composite_M':>17}  {'shard':>52}")
    print("  " + "-" * 100)

    shards_written: list[tuple[int, Path]] = []
    upstreams = [
        _pb.witness_path("canonical-mass-table-extended.witness.json", HERE),
        _pb.witness_path("alpha-cluster-recursion.witness.json", HERE / "alpha"),
        _pb.witness_path("low-isotope-binding-sweep.witness.json", HERE / "sweeps"),
        _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE),
        _pb.witness_path("m-p-substrate-identity-50dps.witness.json", HERE),
        HERE / "data" / "ame2020.json",
    ]
    upstream_records: list[dict] = []
    for u in upstreams:
        if u.exists():
            _, rec = load_and_hash_upstream(u)
            rec["path"] = u.resolve().relative_to(HERE.resolve()).as_posix()
            upstream_records.append(rec)

    w2 = _precompute_wave2_tables(
        ame.get("entries", []),
        z_max_needed=max(z_list) if z_list else 118,
    )

    for Z, entries in by_z.items():
        if not entries:
            continue
        rows = [
            assemble_row(e, layer1, layer2, layer3, m_p_borr, m_n_borr, w2)
            for e in entries
        ]
        path = emit_z_shard(Z, rows, upstream_records, w2)
        shards_written.append((Z, path))
        n_pred = sum(1 for r in rows if r.get("prediction_MeV_50dps") is not None)
        n_comp = sum(
            1 for r in rows
            if r.get("composite_mass", {}).get("M_pred_MeV") is not None
        )
        el = rows[0]["element"]
        print(f"  {Z:>3}  {el:<8}  {len(rows):>5}  {n_pred:>10}  {n_comp:>17}  {path.name:>52}")

    index_path = emit_index(shards_written, ame)
    print()
    print(f"  Index: {index_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
