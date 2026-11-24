#!/usr/bin/env python3
"""Pre-registered 80-dps probe for Closing Open Gap 1 (Option 1A):
4He 12-Quark Pauli Antisymmetrizer & Wigner SU(4) Spin-Isospin Chromomagnetic Binding.

Pre-registration committed & pushed BEFORE execution:
  - `computations/probes/gap1_4he_wigner_pauli_12q/PREREGISTRATION.md`
Formal Lean 4 backing (`0 sorry`, `0` custom `axiom`s, generic §7c + `_real` bridge):
  - `folio/quantum-observable-universe/lean/QOU/Nuclear/TwelveQuarkWignerPauliBinding.lean`

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact rational `sympy` verification over `Q` for microscopic 6q Pauli/CMI/Harvey identities,
  - zero `float64` imports, casts, or lossy literals (`probe-float64-guard.py` clean),
  - zero post-hoc parameter fitting (`NO FITTING, EXCEPT CAL-1/2/3`).
"""

from __future__ import annotations

import itertools
import json
import sys
from collections import deque
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

Tableau = tuple[tuple[int, ...], ...]


# ---------------------------------------------------------------------------
# Part A1: Exact Young-diagram combinatorics, SU(4)_{sigma tau} & shell closure
# ---------------------------------------------------------------------------
def enumerate_syts(shape: tuple[int, ...]) -> list[Tableau]:
    """Deterministically enumerate all standard Young tableaux of `shape` (1-indexed entries)."""
    n_total = sum(shape)
    n_rows = len(shape)
    results: list[Tableau] = []
    partial: list[list[int]] = [[] for _ in range(n_rows)]

    def backtrack(val: int) -> None:
        if val > n_total:
            results.append(tuple(tuple(row) for row in partial))
            return
        for r in range(n_rows):
            if len(partial[r]) < shape[r] and (r == 0 or len(partial[r]) < len(partial[r - 1])):
                partial[r].append(val)
                backtrack(val + 1)
                partial[r].pop()

    backtrack(1)
    results.sort()
    return results


def transpose_tableau(t: Tableau) -> Tableau:
    """Transpose an r x c rectangular standard Young tableau into c x r."""
    n_rows = len(t)
    n_cols = len(t[0])
    return tuple(tuple(t[r][c] for r in range(n_rows)) for c in range(n_cols))


def factorized_col_syt(a_nuc: int) -> Tableau:
    """Unique column-factorized colour SYT T_fac^{col} of [A, A, A] ({3k+1, 3k+2, 3k+3} in col k)."""
    return (
        tuple(3 * k + 1 for k in range(a_nuc)),
        tuple(3 * k + 2 for k in range(a_nuc)),
        tuple(3 * k + 3 for k in range(a_nuc)),
    )


def hook_prod_shape(shape: tuple[int, ...]) -> int:
    """Exact integer product of hook lengths across all cells of `shape`."""
    prod = 1
    for i, row_len in enumerate(shape):
        for j in range(row_len):
            arm = row_len - j - 1
            leg = sum(1 for i2 in range(i + 1, len(shape)) if shape[i2] > j)
            prod *= arm + leg + 1
    return prod


def su4_weyl_dim_col_three(a_nuc: int) -> tuple[int, int, int]:
    """Exact integer (numerator, hook_prod, weyl_dim) of V^{SU(4)}_{[3^A]}."""
    shape = (3,) * a_nuc
    num = 1
    for i in range(a_nuc):
        for j in range(3):
            num *= 4 + j - i
    hp = hook_prod_shape(shape)
    assert num % hp == 0
    return num, hp, num // hp


def content_sum_shape(shape: tuple[int, ...]) -> int:
    return sum(j - i for i, row_len in enumerate(shape) for j in range(row_len))


def int_factorial(n: int) -> int:
    acc = 1
    for k in range(2, n + 1):
        acc *= k
    return acc


def int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return int_factorial(n) // (int_factorial(k) * int_factorial(n - k))


def evaluate_part_a1_combinatorics() -> dict:
    """Verify conjugate pairing, hook equality, SU(4) dimensions, and A=5 shell closure."""
    by_a: dict[str, dict] = {}
    all_ok = True
    expected_su3 = {1: 1, 2: 5, 3: 42, 4: 462, 5: 6006}
    expected_su4 = {1: 20, 2: 50, 3: 20, 4: 1, 5: 0}
    expected_ext = {1: 4, 2: 6, 3: 4, 4: 1, 5: 0}

    for a_nuc in (1, 2, 3, 4, 5):
        rect = (a_nuc, a_nuc, a_nuc)
        col3 = (3,) * a_nuc
        hp_rect = hook_prod_shape(rect)
        hp_col3 = hook_prod_shape(col3)
        cat_ok = 2 * hp_rect == (
            int_factorial(a_nuc) * int_factorial(a_nuc + 1) * int_factorial(a_nuc + 2)
        )
        specht_rect = int_factorial(3 * a_nuc) // hp_rect
        specht_col3 = int_factorial(3 * a_nuc) // hp_col3
        su4_num, _, su4_dim = su4_weyl_dim_col_three(a_nuc)
        nuc_ext = int_comb(4, a_nuc)
        kap_col3 = content_sum_shape(col3)
        kap_rect = content_sum_shape(rect)
        cas8_su4 = 8 * kap_col3 + 3 * a_nuc * (16 - 3 * a_nuc)

        if a_nuc <= 4:
            syts_r = enumerate_syts(rect)
            syts_c = enumerate_syts(col3)
            c_set = set(syts_c)
            bij_ok = (
                len(syts_r) == specht_rect
                and len(syts_c) == specht_col3
                and all(transpose_tableau(t) in c_set for t in syts_r)
            )
        else:
            bij_ok = True

        row_ok = (
            hp_rect == hp_col3
            and cat_ok
            and specht_rect == expected_su3[a_nuc]
            and su4_dim == expected_su4[a_nuc]
            and nuc_ext == expected_ext[a_nuc]
            and kap_col3 + kap_rect == 0
            and bij_ok
        )
        if not row_ok:
            all_ok = False

        by_a[f"A={a_nuc}"] = {
            "n_quarks": 3 * a_nuc,
            "specht_dim_colour_and_spin_isospin": specht_rect,
            "hidden_channel_dim": specht_rect - 1,
            "su4_weyl_dim_colThree": su4_dim,
            "su4_content_numerator": su4_num,
            "nucleon_exterior_dim_choose_4_A": nuc_ext,
            "content_sum_colThree": kap_col3,
            "content_sum_rectThree": kap_rect,
            "eight_times_C2_SU4_colThree": cas8_su4,
            "pauli_hidden_fraction_rational": f"{specht_rect - 1}/{specht_rect}",
        }

    return {"all_combinatorics_pass": all_ok, "by_A": by_a}


# ---------------------------------------------------------------------------
# Part A2: Exact SymPy rational microscopic 6q Pauli, CMI & Harvey verification
# ---------------------------------------------------------------------------
QuarkState = tuple[int, int, int]  # (colour in 0..2, spin in {0=up,1=dn}, iso in {0=u,1=d})
BaryonVec = dict[tuple[QuarkState, ...], sp.Rational]


def _add_term(vec: BaryonVec, key: tuple[QuarkState, ...], coeff: sp.Rational) -> None:
    if coeff == 0:
        return
    nxt = vec.get(key, sp.Rational(0)) + coeff
    if nxt == 0:
        vec.pop(key, None)
    else:
        vec[key] = nxt


def _dot_q(u: BaryonVec, v: BaryonVec) -> sp.Rational:
    if len(u) > len(v):
        u, v = v, u
    acc = sp.Rational(0)
    for k, val in u.items():
        vk = v.get(k)
        if vk is not None:
            acc += val * vk
    return acc


def _build_nucleon_states_3q() -> dict[str, BaryonVec]:
    """Construct exact S_3-antisymmetric 3q states |p_up>, |p_dn>, |n_up>, |n_dn> over Q."""
    # Spin-isospin symmetric seed for (Sz=+1/2, Tz=+1/2): perms of ((0,0), (0,0), (1,1))
    st_seed: dict[tuple[tuple[int, int], ...], sp.Rational] = {
        ((0, 0), (0, 0), (1, 1)): sp.Rational(1),
        ((0, 0), (1, 1), (0, 0)): sp.Rational(1),
        ((1, 1), (0, 0), (0, 0)): sp.Rational(1),
    }
    # Apply (P_01^sigma + P_02^sigma + P_12^sigma - 3 I) to kill S = 3/2 (Delta^+) and keep S = 1/2
    st_pup: dict[tuple[tuple[int, int], ...], sp.Rational] = {}
    for cfg, val in st_seed.items():
        st_pup[cfg] = st_pup.get(cfg, sp.Rational(0)) - sp.Rational(3) * val
        for i, j in ((0, 1), (0, 2), (1, 2)):
            lst = list(cfg)
            lst[i] = (cfg[j][0], cfg[i][1])
            lst[j] = (cfg[i][0], cfg[j][1])
            t_sw = tuple(lst)
            st_pup[t_sw] = st_pup.get(t_sw, sp.Rational(0)) + val
    st_pup = {k: v for k, v in st_pup.items() if v != 0}

    # Combine with colour Levi-Civita eps_{c0, c1, c2}
    perms3 = list(itertools.permutations((0, 1, 2)))
    p_up: BaryonVec = {}
    for c_perm in perms3:
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if c_perm[i] > c_perm[j])
        sgn = sp.Rational(-1 if (inv % 2) else 1)
        for st_cfg, val in st_pup.items():
            full_key = tuple((c_perm[m], st_cfg[m][0], st_cfg[m][1]) for m in range(3))
            _add_term(p_up, full_key, sgn * val)

    def lower_spin(v: BaryonVec) -> BaryonVec:
        out: BaryonVec = {}
        for k, val in v.items():
            for m in range(3):
                if k[m][1] == 0:
                    lst = list(k)
                    lst[m] = (k[m][0], 1, k[m][2])
                    _add_term(out, tuple(lst), val)
        return out

    def lower_iso(v: BaryonVec) -> BaryonVec:
        out: BaryonVec = {}
        for k, val in v.items():
            for m in range(3):
                if k[m][2] == 0:
                    lst = list(k)
                    lst[m] = (k[m][0], k[m][1], 1)
                    _add_term(out, tuple(lst), val)
        return out

    p_dn = lower_spin(p_up)
    n_up = lower_iso(p_up)
    n_dn = lower_spin(n_up)
    return {"p_up": p_up, "p_dn": p_dn, "n_up": n_up, "n_dn": n_dn}


def _tensor_product_3q(u: BaryonVec, v: BaryonVec, scale: sp.Rational) -> BaryonVec:
    out: BaryonVec = {}
    for ku, vu in u.items():
        for kv, vv in v.items():
            _add_term(out, ku + kv, scale * vu * vv)
    return out


def _apply_cmi_vec(v: BaryonVec, n_quarks: int) -> BaryonVec:
    """Apply exact microscopic CMI operator -sum_{i<j} (2 P_ij^col - 2/3)(2 P_ij^sig - 1)."""
    out: BaryonVec = {}
    two_thirds = sp.Rational(2, 3)
    four_thirds = sp.Rational(4, 3)
    for cfg, amp in v.items():
        for i in range(n_quarks):
            for j in range(i + 1, n_quarks):
                # -(2 P_c - 2/3)(2 P_s - 1) = -4 P_c P_s + 2 P_c + (4/3) P_s - 2/3
                _add_term(out, cfg, -two_thirds * amp)
                # P_s
                lst_s = list(cfg)
                lst_s[i] = (cfg[i][0], cfg[j][1], cfg[i][2])
                lst_s[j] = (cfg[j][0], cfg[i][1], cfg[j][2])
                _add_term(out, tuple(lst_s), four_thirds * amp)
                # P_c
                lst_c = list(cfg)
                lst_c[i] = (cfg[j][0], cfg[i][1], cfg[i][2])
                lst_c[j] = (cfg[i][0], cfg[j][1], cfg[j][2])
                _add_term(out, tuple(lst_c), sp.Rational(2) * amp)
                # P_c P_s
                lst_cs = list(cfg)
                lst_cs[i] = (cfg[j][0], cfg[j][1], cfg[i][2])
                lst_cs[j] = (cfg[i][0], cfg[i][1], cfg[j][2])
                _add_term(out, tuple(lst_cs), sp.Rational(-4) * amp)
    return out


def _antisymmetrize_6q_from_3x3(v_clus: BaryonVec) -> BaryonVec:
    """Apply A_6 = (1/20) sum_{left coset reps pi of S_6 / (S_3 x S_3)} sgn(pi) P_pi to an
    (S_3 x S_3)-antisymmetric 6-quark state, using true left action new_cfg[pi(m)] = cfg[m]."""
    coset_reps: list[tuple[tuple[int, ...], sp.Rational]] = []
    for left_set in itertools.combinations(range(6), 3):
        right_set = tuple(idx for idx in range(6) if idx not in left_set)
        perm = left_set + right_set
        inv_perm = [0] * 6
        for m, pm in enumerate(perm):
            inv_perm[pm] = m
        inv = sum(1 for a in range(6) for b in range(a + 1, 6) if perm[a] > perm[b])
        sgn = sp.Rational(-1 if (inv % 2) else 1)
        coset_reps.append((tuple(inv_perm), sgn))

    inv20 = sp.Rational(1, 20)
    out: BaryonVec = {}
    for cfg, amp in v_clus.items():
        for inv_p, sgn in coset_reps:
            new_cfg = tuple(cfg[inv_p[m]] for m in range(6))
            _add_term(out, new_cfg, inv20 * sgn * amp)
    return out


def verify_sympy_6q_microscopic() -> dict:
    """Exact rational verification of CMI eigenvalues, Pauli norm 1/9, and Harvey (1/9, 4/45, 4/5)."""
    nucs = _build_nucleon_states_3q()
    p_up = nucs["p_up"]
    p_dn = nucs["p_dn"]
    n_up = nucs["n_up"]
    n_dn = nucs["n_dn"]

    # Check single-nucleon CMI = -8
    cmi_p = _apply_cmi_vec(p_up, 3)
    norm_p = _dot_q(p_up, p_up)
    cmi_nucleon_val = _dot_q(p_up, cmi_p) / norm_p
    cmi_nucleon_eig_ok = all(
        cmi_p.get(k, sp.Rational(0)) == sp.Rational(-8) * v for k, v in p_up.items()
    )

    # Build 2-nucleon S=1, Sz=1, T=0 (deuteron) cluster state: |p_up>|n_up> - |n_up>|p_up>
    nn_10 = _tensor_product_3q(p_up, n_up, sp.Rational(1))
    for k, v in _tensor_product_3q(n_up, p_up, sp.Rational(-1)).items():
        _add_term(nn_10, k, v)
    norm_nn10 = _dot_q(nn_10, nn_10)

    # Check single-crossing expectations <NN | P_23^col | NN> = 1/3 and <NN | P_23^{st} | NN> = -1/27
    p23_col_nn: BaryonVec = {}
    p23_st_nn: BaryonVec = {}
    for cfg, amp in nn_10.items():
        lc = list(cfg)
        lc[2] = (cfg[3][0], cfg[2][1], cfg[2][2])
        lc[3] = (cfg[2][0], cfg[3][1], cfg[3][2])
        _add_term(p23_col_nn, tuple(lc), amp)

        lst = list(cfg)
        lst[2] = (cfg[2][0], cfg[3][1], cfg[3][2])
        lst[3] = (cfg[3][0], cfg[2][1], cfg[2][2])
        _add_term(p23_st_nn, tuple(lst), amp)

    exp_p23_col = _dot_q(nn_10, p23_col_nn) / norm_nn10
    exp_p23_st = _dot_q(nn_10, p23_st_nn) / norm_nn10

    # Apply 6q Pauli antisymmetrizer A_6 to |NN_(1,0)>
    psi_6q_10 = _antisymmetrize_6q_from_3x3(nn_10)
    norm_psi10 = _dot_q(psi_6q_10, psi_6q_10)
    pauli_norm_ratio_10 = _dot_q(nn_10, psi_6q_10) / norm_nn10  # <NN | A_6 | NN> / <NN | NN>
    # Since A_6 is an orthogonal projector (A_6^2 = A_6, A_6^T = A_6), <Psi|Psi>/<NN|NN> = <NN|A_6|NN>/<NN|NN>
    proj_idem_ok = (norm_psi10 / norm_nn10) == pauli_norm_ratio_10

    # Probability of |NN> inside normalized |Psi_{(0s)^6}>: |<NN|Psi>|^2 / (<NN|NN><Psi|Psi>)
    prob_nn = (_dot_q(nn_10, psi_6q_10) ** 2) / (norm_nn10 * norm_psi10)

    # Project |Psi_{(0s)^6}> onto colour-singlet x colour-singlet P_{1_c x 1_c}
    # On 3q colour space, P_{1_c} = (1/6) sum_{pi in S_3} sgn(pi) P_pi^col
    perms3 = list(itertools.permutations((0, 1, 2)))
    perms3_sgn = [
        (
            p,
            sp.Rational(
                -1 if (sum(1 for a in range(3) for b in range(a + 1, 3) if p[a] > p[b]) % 2) else 1
            ),
        )
        for p in perms3
    ]
    inv36 = sp.Rational(1, 36)
    psi_col_11: BaryonVec = {}
    for cfg, amp in psi_6q_10.items():
        # Filter quickly: both {0,1,2} and {3,4,5} must contain all 3 colours {0,1,2}!
        if {cfg[0][0], cfg[1][0], cfg[2][0]} != {0, 1, 2}:
            continue
        if {cfg[3][0], cfg[4][0], cfg[5][0]} != {0, 1, 2}:
            continue
        for pL, sL in perms3_sgn:
            for pR, sR in perms3_sgn:
                nc = (
                    (cfg[pL[0]][0], cfg[0][1], cfg[0][2]),
                    (cfg[pL[1]][0], cfg[1][1], cfg[1][2]),
                    (cfg[pL[2]][0], cfg[2][1], cfg[2][2]),
                    (cfg[3 + pR[0]][0], cfg[3][1], cfg[3][2]),
                    (cfg[3 + pR[1]][0], cfg[4][1], cfg[4][2]),
                    (cfg[3 + pR[2]][0], cfg[5][1], cfg[5][2]),
                )
                _add_term(psi_col_11, nc, inv36 * sL * sR * amp)

    prob_col_11 = _dot_q(psi_col_11, psi_col_11) / norm_psi10
    prob_dd = prob_col_11 - prob_nn
    prob_hid_88 = sp.Rational(1) - prob_col_11

    # Microscopic CMI eigenvalue on |Psi_{(0s)^6}(S=1, T=0)>
    cmi_psi10 = _apply_cmi_vec(psi_6q_10, 6)
    cmi_10_val = _dot_q(psi_6q_10, cmi_psi10) / norm_psi10
    cmi_10_eig_ok = all(
        cmi_psi10.get(k, sp.Rational(0)) == sp.Rational(8, 3) * v for k, v in psi_6q_10.items()
    )

    # Also build 2-nucleon S=0, T=1, Tz=1 (pp spin-singlet: |p_up>|p_dn> - |p_dn>|p_up>)
    nn_01 = _tensor_product_3q(p_up, p_dn, sp.Rational(1))
    for k, v in _tensor_product_3q(p_dn, p_up, sp.Rational(-1)).items():
        _add_term(nn_01, k, v)
    psi_6q_01 = _antisymmetrize_6q_from_3x3(nn_01)
    norm_psi01 = _dot_q(psi_6q_01, psi_6q_01)
    cmi_psi01 = _apply_cmi_vec(psi_6q_01, 6)
    cmi_01_val = _dot_q(psi_6q_01, cmi_psi01) / norm_psi01
    cmi_01_eig_ok = all(
        cmi_psi01.get(k, sp.Rational(0)) == sp.Rational(8) * v for k, v in psi_6q_01.items()
    )

    # Closed-form CMI checks across N, Delta, 6q, 9q, 12q
    def cmi_closed(n_q: int, kap: int, s_cas: sp.Rational, t_cas: sp.Rational) -> sp.Rational:
        return (
            sp.Rational(n_q * (n_q - 5) - 2 * kap)
            + sp.Rational(4, 3) * s_cas
            + sp.Rational(4) * t_cas
        )

    closed_vals = {
        "N_3q": str(cmi_closed(3, 3, sp.Rational(3, 4), sp.Rational(3, 4))),
        "Delta_3q": str(cmi_closed(3, 3, sp.Rational(15, 4), sp.Rational(15, 4))),
        "6q_deuteron_S1_T0": str(cmi_closed(6, 3, sp.Rational(2), sp.Rational(0))),
        "6q_dinucleon_S0_T1": str(cmi_closed(6, 3, sp.Rational(0), sp.Rational(2))),
        "9q_triton_helion_S1half_T1half": str(
            cmi_closed(9, 0, sp.Rational(3, 4), sp.Rational(3, 4))
        ),
        "12q_alpha_S0_T0": str(cmi_closed(12, -6, sp.Rational(0), sp.Rational(0))),
    }

    all_ok = bool(
        cmi_nucleon_val == sp.Rational(-8)
        and cmi_nucleon_eig_ok
        and exp_p23_col == sp.Rational(1, 3)
        and exp_p23_st == sp.Rational(-1, 27)
        and pauli_norm_ratio_10 == sp.Rational(1, 9)
        and proj_idem_ok
        and prob_nn == sp.Rational(1, 9)
        and prob_dd == sp.Rational(4, 45)
        and prob_hid_88 == sp.Rational(4, 5)
        and cmi_10_val == sp.Rational(8, 3)
        and cmi_10_eig_ok
        and cmi_01_val == sp.Rational(8)
        and cmi_01_eig_ok
    )

    return {
        "all_exact_sympy_microscopic_pass": all_ok,
        "single_nucleon_cmi": str(cmi_nucleon_val),
        "nn_P23_col_expectation": str(exp_p23_col),
        "nn_P23_spin_isospin_expectation": str(exp_p23_st),
        "pauli_antisymmetrizer_norm_6q": str(pauli_norm_ratio_10),
        "harvey_6q_probabilities": {
            "P_NN": str(prob_nn),
            "P_DeltaDelta": str(prob_dd),
            "P_hidden_88": str(prob_hid_88),
            "P_colour_singlet_sum": str(prob_col_11),
        },
        "microscopic_6q_cmi_eigenvalues": {
            "S1_T0_deuteron_bag": str(cmi_10_val),
            "S1_T0_repulsive_core_vs_2N": str(cmi_10_val - sp.Rational(-16)),
            "S0_T1_dinucleon_bag": str(cmi_01_val),
            "S0_T1_repulsive_core_vs_2N": str(cmi_01_val - sp.Rational(-16)),
            "dinucleon_minus_deuteron_core_excess": str(cmi_01_val - cmi_10_val),
        },
        "closed_form_cmi_spectrum_3q_to_12q": closed_vals,
    }


# ---------------------------------------------------------------------------
# Part A3 & Part B: 80-dps Hoefsmit S^{[A,A,A]} & S^{[3^A]} and Models M0..M5
# ---------------------------------------------------------------------------
def q_bracket_mp(q: mp.mpf, n: int) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


class GeneralSparseHoefsmit:
    """Exact 80-dps real-symmetric Hoefsmit generators R_k(q) on S^{shape} for arbitrary shape."""

    def __init__(self, shape: tuple[int, ...], q: mp.mpf, syts_override: list[Tableau] | None = None) -> None:
        self.shape = shape
        self.n_rows = len(shape)
        self.n_strands = sum(shape)
        self.q = q
        self.q_inv = mp.mpf(1) / q
        self.h = q - self.q_inv
        self.syts = syts_override if syts_override is not None else enumerate_syts(shape)
        self.dim = len(self.syts)
        self.syt_to_idx = {t: idx for idx, t in enumerate(self.syts)}

        pos_list: list[list[tuple[int, int]]] = []
        for t in self.syts:
            pos = [(0, 0)] * (self.n_strands + 1)
            for r in range(self.n_rows):
                for c, val in enumerate(t[r]):
                    pos[val] = (r, c)
            pos_list.append(pos)

        self.gen_rows: list[list[list[tuple[int, mp.mpf]]]] = []
        self.inv_gen_rows: list[list[list[tuple[int, mp.mpf]]]] = []
        one = mp.mpf(1)

        for k in range(self.n_strands - 1):
            v1, v2 = k + 1, k + 2
            rows_k: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(self.dim)]
            inv_rows_k: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(self.dim)]
            for i, t in enumerate(self.syts):
                r1, c1 = pos_list[i][v1]
                r2, c2 = pos_list[i][v2]
                if r1 == r2:
                    rows_k[i] = [(i, q)]
                    inv_rows_k[i] = [(i, self.q_inv)]
                elif c1 == c2:
                    rows_k[i] = [(i, -self.q_inv)]
                    inv_rows_k[i] = [(i, -q)]
                else:
                    d_ax = (c2 - r2) - (c1 - r1)
                    abs_d = abs(d_ax)
                    qd = q_bracket_mp(q, abs_d)
                    diag = self.h / (one - q ** (-2 * d_ax))
                    off = mp.sqrt(q_bracket_mp(q, abs_d - 1) * q_bracket_mp(q, abs_d + 1)) / qd
                    grid = [list(row) for row in t]
                    grid[r1][c1] = v2
                    grid[r2][c2] = v1
                    t_sw = tuple(tuple(row) for row in grid)
                    j = self.syt_to_idx[t_sw]
                    rows_k[i] = [(i, diag), (j, off)]
                    inv_rows_k[i] = [(i, diag - self.h), (j, off)]
            self.gen_rows.append(rows_k)
            self.inv_gen_rows.append(inv_rows_k)

    def apply_gen(self, k: int, vec: list[mp.mpf], inverse: bool = False) -> list[mp.mpf]:
        rows = self.inv_gen_rows[k] if inverse else self.gen_rows[k]
        zero = mp.mpf(0)
        out = [zero] * self.dim
        for i, entries in enumerate(rows):
            acc = zero
            for j, val in entries:
                vj = vec[j]
                if vj != zero:
                    acc += val * vj
            out[i] = acc
        return out

    def apply_word(self, word: list[tuple[int, bool]], vec: list[mp.mpf]) -> list[mp.mpf]:
        cur = list(vec)
        for k, inv in reversed(word):
            cur = self.apply_gen(k, cur, inverse=inv)
        return cur

    def build_dense_from_word(self, word: list[tuple[int, bool]]) -> list[list[mp.mpf]]:
        zero = mp.mpf(0)
        one = mp.mpf(1)
        cols: list[list[mp.mpf]] = []
        for j in range(self.dim):
            ej = [zero] * self.dim
            ej[j] = one
            cols.append(self.apply_word(word, ej))
        return [[cols[j][i] for j in range(self.dim)] for i in range(self.dim)]

    def conjugate_dense_by_gen(
        self, mat: list[list[mp.mpf]], k: int, left_inv: bool, right_inv: bool
    ) -> list[list[mp.mpf]]:
        """Compute L_k @ mat @ R_k in O(dim^2) exploiting symmetry and <=2 nonzeros/row."""
        rows_l = self.inv_gen_rows[k] if left_inv else self.gen_rows[k]
        rows_r = self.inv_gen_rows[k] if right_inv else self.gen_rows[k]
        zero = mp.mpf(0)
        dim = self.dim
        tmp = [[zero] * dim for _ in range(dim)]
        for i, entries_l in enumerate(rows_l):
            row_out = tmp[i]
            for p_idx, vl in entries_l:
                mp_row = mat[p_idx]
                for j in range(dim):
                    row_out[j] += vl * mp_row[j]
        out = [[zero] * dim for _ in range(dim)]
        for i in range(dim):
            ti = tmp[i]
            oi = out[i]
            for j, entries_r in enumerate(rows_r):
                acc = zero
                for m_idx, vr in entries_r:
                    acc += ti[m_idx] * vr
                oi[j] = acc
        return out

    def verify_relations_max_residual(self) -> mp.mpf:
        max_res = mp.mpf(0)
        probe = [mp.mpf(1) / mp.mpf(i + 2) for i in range(self.dim)]
        for k in range(self.n_strands - 1):
            rk = self.apply_gen(k, probe)
            rk2 = self.apply_gen(k, rk)
            for i in range(self.dim):
                max_res = max(max_res, abs(rk2[i] - self.h * rk[i] - probe[i]))
        for k in range(self.n_strands - 2):
            lhs = self.apply_word([(k, False), (k + 1, False), (k, False)], probe)
            rhs = self.apply_word([(k + 1, False), (k, False), (k + 1, False)], probe)
            for i in range(self.dim):
                max_res = max(max_res, abs(lhs[i] - rhs[i]))
        return max_res


def compute_yamanouchi_signs(hoef: GeneralSparseHoefsmit, start_idx: int) -> tuple[list[int], bool]:
    """Compute exact Yamanouchi signs eta(T) in {+1, -1} by BFS over Hoefsmit swap edges."""
    signs = [0] * hoef.dim
    signs[start_idx] = 1
    queue: deque[int] = deque([start_idx])
    consistent = True
    while queue:
        u = queue.popleft()
        for k in range(hoef.n_strands - 1):
            for v, _ in hoef.gen_rows[k][u]:
                if v == u:
                    continue
                if signs[v] == 0:
                    signs[v] = -signs[u]
                    queue.append(v)
                elif signs[v] != -signs[u]:
                    consistent = False
    if any(s == 0 for s in signs):
        consistent = False
    return signs, consistent


def braid_transposition_word(s: int, t: int) -> list[tuple[int, bool]]:
    """True positive-braid-conjugated transposition B_{s, t} = R_s^{-1}...R_{t-2}^{-1} R_{t-1} R_{t-2}...R_s
    for 0 <= s < t (applied right-to-left by `apply_word`)."""
    assert 0 <= s < t
    left_undo = [(g_idx, True) for g_idx in range(s, t - 1)]
    right_transport = [(g_idx, False) for g_idx in range(t - 2, s - 1, -1)]
    return left_undo + [(t - 1, False)] + right_transport


def w4_legacy_buggy_word(a_idx: int, b_idx: int) -> list[tuple[int, bool]]:
    """Exact reproduction of W4 (`#9221`) `V2_allpairs_fierz` word for regression audit."""
    s_strand = 3 * a_idx + 2
    target_gen = 3 * b_idx - 1
    prefix = [(g_idx, False) for g_idx in range(target_gen - 1, s_strand - 1, -1)]
    suffix = [(g_idx, True) for g_idx in range(s_strand, target_gen)]
    return prefix + [(target_gen, False)] + suffix


def pauli_proj_from_col_mat(mat_col: list[list[mp.mpf]], h: mp.mpf) -> list[list[mp.mpf]]:
    """Compute M_{ij} = X_{ij} (X - h I)_{ji} = -Pi_D (X (x) Y) Pi_D from Lean's
    `hecke_conjugate_duality_and_pauli_invariance`."""
    dim = len(mat_col)
    out = [[mp.mpf(0)] * dim for _ in range(dim)]
    for i in range(dim):
        xi = mat_col[i]
        oi = out[i]
        for j in range(dim):
            x_inv_ji = mat_col[j][i] - (h if i == j else mp.mpf(0))
            oi[j] = xi[j] * x_inv_ji
    return out


def matvec_dense(mat: list[list[mp.mpf]], vec: list[mp.mpf]) -> list[mp.mpf]:
    return [mp.fsum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def dot_mp(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(u[i] * v[i] for i in range(len(u)))


def cg_solve_spd(
    mat: list[list[mp.mpf]], rhs: list[mp.mpf], tol: mp.mpf, max_iter: int = 350
) -> tuple[list[mp.mpf], mp.mpf]:
    n = len(rhs)
    zero = mp.mpf(0)
    x = [zero] * n
    r = list(rhs)
    p = list(r)
    rs_old = dot_mp(r, r)
    if rs_old == zero:
        return x, zero
    for _ in range(max_iter):
        ap = matvec_dense(mat, p)
        pap = dot_mp(p, ap)
        alpha = rs_old / pap
        for i in range(n):
            x[i] += alpha * p[i]
            r[i] -= alpha * ap[i]
        rs_new = dot_mp(r, r)
        if mp.sqrt(rs_new) < tol:
            break
        beta = rs_new / rs_old
        for i in range(n):
            p[i] = r[i] + beta * p[i]
        rs_old = rs_new
    ax = matvec_dense(mat, x)
    inf_res = max(abs(ax[i] - rhs[i]) for i in range(n))
    return x, inf_res


def lowest_eigenpair_sym(
    mat: list[list[mp.mpf]], start_idx: int
) -> tuple[mp.mpf, list[mp.mpf], mp.mpf]:
    n = len(mat)
    if n <= 60:
        m_mp = mp.matrix(mat)
        evals, evecs = mp.eigsy(m_mp)
        min_idx = min(range(n), key=lambda idx: evals[idx])
        lam = evals[min_idx]
        vec = [evecs[i, min_idx] for i in range(n)]
        mv = matvec_dense(mat, vec)
        res = max(abs(mv[i] - lam * vec[i]) for i in range(n))
        return lam, vec, res

    zero = mp.mpf(0)
    v0 = [mp.mpf(1) / mp.mpf(1000 * (i + 3)) for i in range(n)]
    v0[start_idx] = mp.mpf(1)
    nrm0 = mp.sqrt(dot_mp(v0, v0))
    v0 = [x / nrm0 for x in v0]

    basis: list[list[mp.mpf]] = [v0]
    m_steps = min(220, n)
    alphas: list[mp.mpf] = []
    betas: list[mp.mpf] = []

    for step in range(m_steps):
        w = matvec_dense(mat, basis[step])
        if step > 0:
            b_prev = betas[step - 1]
            prev_vec = basis[step - 1]
            for i in range(n):
                w[i] -= b_prev * prev_vec[i]
        a_cur = dot_mp(basis[step], w)
        alphas.append(a_cur)
        for i in range(n):
            w[i] -= a_cur * basis[step][i]
        for _ in range(2):
            for qv in basis:
                ov = dot_mp(qv, w)
                for i in range(n):
                    w[i] -= ov * qv[i]
        b_next = mp.sqrt(dot_mp(w, w))
        if b_next < mp.mpf("1e-72"):
            break
        if step + 1 < m_steps:
            betas.append(b_next)
            basis.append([x / b_next for x in w])

    k_dim = len(alphas)
    tri = mp.matrix(k_dim, k_dim)
    for i in range(k_dim):
        tri[i, i] = alphas[i]
        if i < len(betas) and i + 1 < k_dim:
            tri[i, i + 1] = betas[i]
            tri[i + 1, i] = betas[i]
    t_evals, t_evecs = mp.eigsy(tri)
    min_idx = min(range(k_dim), key=lambda idx: t_evals[idx])
    lam = t_evals[min_idx]
    vec = [zero] * n
    for s_idx in range(k_dim):
        coeff = t_evecs[s_idx, min_idx]
        bs = basis[s_idx]
        for i in range(n):
            vec[i] += coeff * bs[i]
    vn = mp.sqrt(dot_mp(vec, vec))
    vec = [x / vn for x in vec]
    mv = matvec_dense(mat, vec)
    res = max(abs(mv[i] - lam * vec[i]) for i in range(n))
    return lam, vec, res


def evaluate_models_and_duality(
    q0: mp.mpf, e0_mev: mp.mpf, eosc_mev: mp.mpf, me_mev: mp.mpf, b_ame: dict[str, mp.mpf]
) -> dict:
    """Certify 80-dps Hoefsmit conjugate duality across A=2,3,4 and evaluate Models M0..M5."""
    zero = mp.mpf(0)
    one = mp.mpf(1)
    half = one / mp.mpf(2)
    h = q0 - one / q0

    max_hecke_res = zero
    max_duality_gen_res = zero
    max_duality_braid_res = zero
    max_pauli_rowsum_res = zero
    max_conj_shortcut_res = zero
    all_signs_consistent = True

    # Per-A precomputed structures
    model_mats_by_a: dict[int, dict[str, tuple[list[list[mp.mpf]], list[list[mp.mpf]]]]] = {}
    fac_idx_by_a: dict[int, int] = {}
    dim_by_a: dict[int, int] = {}
    a2_full_tensor_audit: dict[str, str] = {}

    for a_nuc in (2, 3, 4):
        syts_col = enumerate_syts((a_nuc, a_nuc, a_nuc))
        # Order spin-isospin SYTs in exact bijection T_i' = transpose(T_i) so index i matches i!
        syts_st = [transpose_tableau(t) for t in syts_col]
        hoef_col = GeneralSparseHoefsmit((a_nuc, a_nuc, a_nuc), q0, syts_override=syts_col)
        hoef_st = GeneralSparseHoefsmit((3,) * a_nuc, q0, syts_override=syts_st)

        dim = hoef_col.dim
        fac = hoef_col.syt_to_idx[factorized_col_syt(a_nuc)]
        fac_idx_by_a[a_nuc] = fac
        dim_by_a[a_nuc] = dim

        max_hecke_res = max(max_hecke_res, hoef_col.verify_relations_max_residual())
        max_hecke_res = max(max_hecke_res, hoef_st.verify_relations_max_residual())

        eta, sgn_ok = compute_yamanouchi_signs(hoef_col, fac)
        if not sgn_ok:
            all_signs_consistent = False

        # Certify R_k^{[3^A]} == -D_eta (R_k^{[A,A,A]})^{-1} D_eta across all generators
        for k in range(hoef_col.n_strands - 1):
            for i in range(dim):
                dict_col_inv = dict(hoef_col.inv_gen_rows[k][i])
                dict_st = dict(hoef_st.gen_rows[k][i])
                for j in set(dict_col_inv.keys()) | set(dict_st.keys()):
                    val_st = dict_st.get(j, zero)
                    val_dual = -mp.mpf(eta[i] * eta[j]) * dict_col_inv.get(j, zero)
                    max_duality_gen_res = max(max_duality_gen_res, abs(val_st - val_dual))

        # Build intra-cluster Casimir gaps G2_col on S^{[A,A,A]} and G2_st on S^{[3^A]}
        g2_col = [[zero] * dim for _ in range(dim)]
        g2_st = [[zero] * dim for _ in range(dim)]
        q_m6 = q0 ** (-6)
        q_p6 = q0**6
        for c_idx in range(a_nuc):
            g0, g1_i = 3 * c_idx, 3 * c_idx + 1
            ft_word = [
                (g0, False),
                (g1_i, False),
                (g0, False),
                (g0, False),
                (g1_i, False),
                (g0, False),
            ]
            ft_col = hoef_col.build_dense_from_word(ft_word)
            # By conjugate duality, full twist (6 positive crossings, even!) on S^{[3^A]} is
            # D_eta ((ft_col)^{-1})^T D_eta! At A=2,3 also build directly on hoef_st to certify!
            if a_nuc <= 3:
                ft_st = hoef_st.build_dense_from_word(ft_word)
            else:
                inv_ft_word = [
                    (g0, True),
                    (g1_i, True),
                    (g0, True),
                    (g0, True),
                    (g1_i, True),
                    (g0, True),
                ]
                ft_col_inv = hoef_col.build_dense_from_word(inv_ft_word)
                ft_st = [
                    [mp.mpf(eta[i] * eta[j]) * ft_col_inv[j][i] for j in range(dim)]
                    for i in range(dim)
                ]
            for i in range(dim):
                for j in range(dim):
                    vc = half * (ft_col[i][j] + ft_col[j][i])
                    vs = half * (ft_st[i][j] + ft_st[j][i])
                    if i == j:
                        vc -= q_m6
                        vs = q_p6 - vs
                    else:
                        vs = -vs
                    g2_col[i][j] += vc / h
                    g2_st[i][j] += vs / h

        g2_barsym = [
            [half * (g2_col[i][j] + g2_st[i][j]) for j in range(dim)] for i in range(dim)
        ]
        g2_sum = [[g2_col[i][j] + g2_st[i][j] for j in range(dim)] for i in range(dim)]

        # Interaction matrices across nucleon pairs 0 <= a < b < A
        v_m0_buggy = [[zero] * dim for _ in range(dim)]
        v_m1_true_ka = [[zero] * dim for _ in range(dim)]
        v_pauli_ka = [[zero] * dim for _ in range(dim)]
        v_pauli_all9_nc = [[zero] * dim for _ in range(dim)]
        v_pauli_all9_avg = [[zero] * dim for _ in range(dim)]

        inv_2nc = one / mp.mpf(6)
        inv_2nc2 = one / mp.mpf(18)

        # Save A=2,3 single-interface matrices for unprojected W_A(q_0) orthogonality & 25x25 audit
        b23_col_a2: list[list[mp.mpf]] = []
        b23_st_a2: list[list[mp.mpf]] = []
        w3_pair_tensors: list[list[list[mp.mpf]]] = []

        for a_idx in range(a_nuc):
            for b_idx in range(a_idx + 1, a_nuc):
                # Legacy W4 word for M0 baseline reproduction
                w_leg = w4_legacy_buggy_word(a_idx, b_idx)
                m_leg = hoef_col.build_dense_from_word(w_leg)
                d_leg = m_leg[fac][fac]
                for i in range(dim):
                    for j in range(dim):
                        # Match exact line 781-782 of w4_colour_reconn_stokes_aomega_probe.py
                        v_m0_buggy[i][j] += half * (half * (m_leg[i][j] + m_leg[j][i]))
                    v_m0_buggy[i][i] -= half * d_leg

                # True K_A interface transposition B_{3a+2, 3b}
                s_base = 3 * a_idx + 2
                t_base = 3 * b_idx
                w_base = braid_transposition_word(s_base, t_base)
                b_base_col = hoef_col.build_dense_from_word(w_base)

                # Certify conjugate braid duality & row-sum = 1 on B_{3a+2, 3b}
                if a_nuc <= 3:
                    b_base_st = hoef_st.build_dense_from_word(w_base)
                    if a_nuc == 2:
                        b23_col_a2 = b_base_col
                        b23_st_a2 = b_base_st
                    if a_nuc == 3:
                        # Symmetrized off-diagonal excitation tensor V_{ab} |Phi_fac> in R^{42 x 42}
                        t_mat = [[zero] * dim for _ in range(dim)]
                        for i1 in range(dim):
                            u1 = half * (b_base_col[i1][fac] + b_base_col[fac][i1])
                            v1_c = b_base_col[i1][fac]
                            v1_r = b_base_col[fac][i1]
                            for i2 in range(dim):
                                val_t = half * (
                                    v1_c * b_base_st[i2][fac] + v1_r * b_base_st[fac][i2]
                                )
                                if i1 == fac and i2 == fac:
                                    val_t = zero
                                t_mat[i1][i2] = half * val_t
                                _ = u1
                        w3_pair_tensors.append(t_mat)
                    for i in range(dim):
                        for j in range(dim):
                            x_inv_ji = b_base_col[j][i] - (h if i == j else zero)
                            dual_ij = -mp.mpf(eta[i] * eta[j]) * x_inv_ji
                            max_duality_braid_res = max(
                                max_duality_braid_res, abs(b_base_st[i][j] - dual_ij)
                            )

                d_col_base = b_base_col[fac][fac]
                for i in range(dim):
                    for j in range(dim):
                        v_m1_true_ka[i][j] += half * (
                            half * (b_base_col[i][j] + b_base_col[j][i])
                        )
                    v_m1_true_ka[i][i] -= half * d_col_base

                p_base = pauli_proj_from_col_mat(b_base_col, h)
                for i in range(dim):
                    rsum = mp.fsum(p_base[i])
                    max_pauli_rowsum_res = max(max_pauli_rowsum_res, abs(rsum - one))
                    # Symmetry residual check
                    for j in range(i + 1, dim):
                        max_pauli_rowsum_res = max(
                            max_pauli_rowsum_res, abs(p_base[i][j] - p_base[j][i])
                        )

                # Note: M = -Pi_D (B_col (x) B_st) Pi_D, so -(1/2)(B_col (x) B_st - d_fac) = +(1/2)(M - M_fac_fac I)?
                # CAREFUL WITH SIGN! Let's check sign on |Psi_Pauli>!
                # Recall (B_col (x) B_st) |Psi_Pauli> = -|Psi_Pauli>, so M |Psi_Pauli> = +|Psi_Pauli> (+1)!
                # On |Phi_fac>, M_{fac, fac} = +1/[3]_q^2 (~ +1/9), and for T != T_fac, M_{fac, s_k T_fac} = +beta^2 (~ +8/9).
                # Attraction toward |Psi_Pauli> (+1 > +1/9) is -1/2 * (M - M_{fac,fac} I) = +1/2 * (B_col (x) B_st - B_fac I)!
                # Wait: in Rayleigh-Ritz from |Phi_fac>, off-diagonal sign (+/-) SQUARES in v^2, while the HIDDEN DIAGONAL
                # must be ATTRACTIVE (-4/9 < 0 on Case 1/2 where M_{TT} = +1 > +1/9), which is -(1/2) * (M - M_{fac,fac} I)!!
                # Let's check: -(1/2) * (+1 - 1/9) = -4/9 < 0! YES! M = -Pi_D (B_col (x) B_st) Pi_D ALREADY absorbed one minus sign,
                # so -(1/2)(M - M_{fac,fac} I) = +(1/2) Pi_D (B_col (x) B_st + M_{fac,fac} I) Pi_D has diagonal -4/9 < 0 on |Psi_Pauli>!
                d_pauli_base = p_base[fac][fac]
                for i in range(dim):
                    for j in range(dim):
                        v_pauli_ka[i][j] -= half * p_base[i][j]
                    v_pauli_ka[i][i] += half * d_pauli_base

                # Build all 9 quark pairs (s in {3a, 3a+1, 3a+2}, t in {3b, 3b+1, 3b+2}) via exact sparse conjugation:
                # B_{s-1, t} = R_{s-1}^{-1} B_{s, t} R_{s-1}
                # B_{s, t+1} = R_t B_{s, t} R_t^{-1}
                b_s_t0: dict[int, list[list[mp.mpf]]] = {s_base: b_base_col}
                b_s_t0[s_base - 1] = hoef_col.conjugate_dense_by_gen(
                    b_s_t0[s_base], s_base - 1, left_inv=True, right_inv=False
                )
                b_s_t0[s_base - 2] = hoef_col.conjugate_dense_by_gen(
                    b_s_t0[s_base - 1], s_base - 2, left_inv=True, right_inv=False
                )

                for s_cur in (3 * a_idx, 3 * a_idx + 1, 3 * a_idx + 2):
                    cur_mat = b_s_t0[s_cur]
                    for dt in (0, 1, 2):
                        t_cur = t_base + dt
                        if dt > 0:
                            cur_mat = hoef_col.conjugate_dense_by_gen(
                                cur_mat, t_cur - 1, left_inv=False, right_inv=True
                            )
                        if a_nuc == 2:
                            ref_mat = hoef_col.build_dense_from_word(
                                braid_transposition_word(s_cur, t_cur)
                            )
                            for i_chk in range(dim):
                                for j_chk in range(dim):
                                    max_conj_shortcut_res = max(
                                        max_conj_shortcut_res,
                                        abs(cur_mat[i_chk][j_chk] - ref_mat[i_chk][j_chk]),
                                    )
                        p_st = pauli_proj_from_col_mat(cur_mat, h)
                        d_st = p_st[fac][fac]
                        for i in range(dim):
                            for j in range(dim):
                                v_pauli_all9_nc[i][j] -= inv_2nc * p_st[i][j]
                                v_pauli_all9_avg[i][j] -= inv_2nc2 * p_st[i][j]
                            v_pauli_all9_nc[i][i] += inv_2nc * d_st
                            v_pauli_all9_avg[i][i] += inv_2nc2 * d_st

        # At A = 2, run exact unprojected 25 x 25 full-tensor W_2(q_0) = S^{[2,2,2]} (x) S^{[3,3]} audit
        if a_nuc == 2:
            dim2 = dim * dim  # 25
            h_full_25 = [[zero] * dim2 for _ in range(dim2)]
            fac25 = fac * dim + fac
            d25 = -b23_col_a2[fac][fac] * b23_st_a2[fac][fac]  # +1/[3]_q^2
            for i1 in range(dim):
                for i2 in range(dim):
                    r25 = i1 * dim + i2
                    for j1 in range(dim):
                        for j2 in range(dim):
                            c25 = j1 * dim + j2
                            val = zero
                            if i2 == j2:
                                val += half * g2_col[i1][j1]
                            if i1 == j1:
                                val += half * g2_st[i2][j2]
                            # +1/2 * (B_col (x) B_st + d25 I) matches -(1/2)(M - M_fac I) on D_Pauli!
                            val += half * b23_col_a2[i1][j1] * b23_st_a2[i2][j2]
                            if r25 == c25:
                                val += half * d25
                            h_full_25[r25][c25] = val
            e25, psi25, res25 = lowest_eigenpair_sym(h_full_25, fac25)
            hid25 = [idx for idx in range(dim2) if idx != fac25]
            h_hid25 = [[h_full_25[r_i][c_i] for c_i in hid25] for r_i in hid25]
            b_vec25 = [h_full_25[r_i][fac25] for r_i in hid25]
            sol25, _ = cg_solve_spd(h_hid25, b_vec25, mp.mpf("1e-76"))
            bh2_25 = -dot_mp(b_vec25, sol25)
            d_pauli_weight = mp.fsum(psi25[idx * dim + idx] ** 2 for idx in range(dim))
            a2_full_tensor_audit = {
                "dim_W2": str(dim2),
                "v_offdiag_norm_sq_W2": fmt(dot_mp(b_vec25, b_vec25), dps=OUT_DPS),
                "delta_E_BH2_W2_dimless": fmt(bh2_25, dps=OUT_DPS),
                "bind_BH2_W2_in_Eosc_MeV": fmt(abs(bh2_25) * eosc_mev, dps=25),
                "bind_BH2_W3_exact_3x_MeV": fmt(mp.mpf(3) * abs(bh2_25) * eosc_mev, dps=25),
                "bind_BH2_W4_exact_6x_MeV": fmt(mp.mpf(6) * abs(bh2_25) * eosc_mev, dps=25),
                "E_ground_W2_dimless": fmt(e25, dps=OUT_DPS),
                "bind_W2_in_Eosc_MeV": fmt(abs(e25) * eosc_mev, dps=25),
                "D_Pauli_subspace_probability": fmt(d_pauli_weight, dps=OUT_DPS),
                "off_D_Pauli_leakage_probability": fmt(one - d_pauli_weight, dps=OUT_DPS),
                "eig_residual_25x25": fmt(res25, dps=15),
            }

        if a_nuc == 3 and len(w3_pair_tensors) == 3:
            norms_w3 = [
                mp.fsum(t[i1][i2] ** 2 for i1 in range(dim) for i2 in range(dim))
                for t in w3_pair_tensors
            ]
            overlaps_w3 = [
                abs(
                    mp.fsum(
                        w3_pair_tensors[p1][i1][i2] * w3_pair_tensors[p2][i1][i2]
                        for i1 in range(dim)
                        for i2 in range(dim)
                    )
                )
                for p1 in range(3)
                for p2 in range(p1 + 1, 3)
            ]
            a2_full_tensor_audit["W3_pair_norm_spread_max_diff"] = fmt(
                max(abs(norms_w3[1] - norms_w3[0]), abs(norms_w3[2] - norms_w3[0])), dps=20
            )
            a2_full_tensor_audit["W3_pair_orthogonality_max_inner_prod"] = fmt(
                max(overlaps_w3), dps=20
            )

        model_mats_by_a[a_nuc] = {
            "M0_w4_baseline_colour_V2": (g2_col, v_m0_buggy),
            "M1_colour_only_true_KA_fierz": (g2_col, v_m1_true_ka),
            "M2_pauli_conjugate_KA_G2col": (g2_col, v_pauli_ka),
            "M3_pauli_conjugate_KA_G2barsym": (g2_barsym, v_pauli_ka),
            "M4_pauli_all9_baryon_norm_G2sum": (g2_sum, v_pauli_all9_nc),
            "M5_pauli_all9_pair_avg_G2barsym": (g2_barsym, v_pauli_all9_avg),
        }

    models_out: dict[str, dict] = {}
    max_cg_res = zero
    max_eig_res = zero
    all_models_bind = True

    model_names = (
        "M0_w4_baseline_colour_V2",
        "M1_colour_only_true_KA_fierz",
        "M2_pauli_conjugate_KA_G2col",
        "M3_pauli_conjugate_KA_G2barsym",
        "M4_pauli_all9_baryon_norm_G2sum",
        "M5_pauli_all9_pair_avg_G2barsym",
    )

    for m_name in model_names:
        per_a: dict[str, dict] = {}
        shifts_bh2: dict[int, mp.mpf] = {}
        shifts_ex: dict[int, mp.mpf] = {}

        for a_nuc in (2, 3, 4):
            dim = dim_by_a[a_nuc]
            fac = fac_idx_by_a[a_nuc]
            hid_indices = [i for i in range(dim) if i != fac]
            g_mat, v_mat = model_mats_by_a[a_nuc][m_name]

            h0_fac_err = max(abs(g_mat[i][fac]) for i in range(dim))
            max_cg_res = max(max_cg_res, h0_fac_err)

            h_hid = [[g_mat[i][j] for j in hid_indices] for i in hid_indices]
            b_vec = [v_mat[i][fac] for i in hid_indices]
            v_leak_sq = dot_mp(b_vec, b_vec)

            sol_hid, cg_res = cg_solve_spd(h_hid, b_vec, mp.mpf("1e-76"))
            max_cg_res = max(max_cg_res, cg_res)
            delta_bh2 = -dot_mp(b_vec, sol_hid)

            h_tot = [[g_mat[i][j] + v_mat[i][j] for j in range(dim)] for i in range(dim)]
            e_ground, psi_ground, eig_res = lowest_eigenpair_sym(h_tot, fac)
            max_eig_res = max(max_eig_res, eig_res)

            if not (e_ground < zero and delta_bh2 < zero):
                all_models_bind = False

            p_hid_prob = one - (psi_ground[fac] ** 2)
            shifts_bh2[a_nuc] = abs(delta_bh2)
            shifts_ex[a_nuc] = abs(e_ground)

            per_a[f"A={a_nuc}"] = {
                "dim_carrier": dim,
                "v_offdiag_norm_sq": fmt(v_leak_sq, dps=OUT_DPS),
                "delta_E_BH2_dimless": fmt(delta_bh2, dps=OUT_DPS),
                "E_ground_exact_dimless": fmt(e_ground, dps=OUT_DPS),
                "hidden_channel_admixture_prob": fmt(p_hid_prob, dps=OUT_DPS),
                "bind_BH2_in_Eosc_MeV": fmt(abs(delta_bh2) * eosc_mev, dps=25),
                "bind_exact_in_Eosc_MeV": fmt(abs(e_ground) * eosc_mev, dps=25),
                "bind_exact_in_E0_MeV": fmt(abs(e_ground) * e0_mev, dps=25),
                "bind_exact_in_me_MeV": fmt(abs(e_ground) * me_mev, dps=25),
                "cg_solve_inf_residual": fmt(cg_res, dps=15),
                "lanczos_eig_inf_residual": fmt(eig_res, dps=15),
            }

        b2_bh = shifts_bh2[2]
        b2_ex = shifts_ex[2]
        models_out[m_name] = {
            "per_A": per_a,
            "scaling_ratios_BH2_vs_A2": {
                "A3_over_A2": fmt(shifts_bh2[3] / b2_bh, dps=25),
                "A4_over_A2": fmt(shifts_bh2[4] / b2_bh, dps=25),
            },
            "scaling_ratios_exact_vs_A2": {
                "A3_over_A2": fmt(shifts_ex[3] / b2_ex, dps=25),
                "A4_over_A2": fmt(shifts_ex[4] / b2_ex, dps=25),
            },
            "ame_comparison_in_Eosc_chart": {
                "2H_MeV": fmt(shifts_ex[2] * eosc_mev, dps=20),
                "2H_rel_diff_pct": fmt(
                    mp.mpf(100) * ((shifts_ex[2] * eosc_mev) - b_ame["2H"]) / b_ame["2H"], dps=12
                ),
                "3H_MeV": fmt(shifts_ex[3] * eosc_mev, dps=20),
                "3H_rel_diff_pct": fmt(
                    mp.mpf(100) * ((shifts_ex[3] * eosc_mev) - b_ame["3H"]) / b_ame["3H"], dps=12
                ),
                "3He_MeV": fmt(shifts_ex[3] * eosc_mev, dps=20),
                "3He_rel_diff_pct": fmt(
                    mp.mpf(100) * ((shifts_ex[3] * eosc_mev) - b_ame["3He"]) / b_ame["3He"],
                    dps=12,
                ),
                "4He_MeV": fmt(shifts_ex[4] * eosc_mev, dps=20),
                "4He_rel_diff_pct": fmt(
                    mp.mpf(100) * ((shifts_ex[4] * eosc_mev) - b_ame["4He"]) / b_ame["4He"],
                    dps=12,
                ),
            },
        }

    return {
        "models": models_out,
        "a2_full_tensor_W2_audit": a2_full_tensor_audit,
        "all_signs_consistent": all_signs_consistent,
        "all_models_bind": all_models_bind,
        "max_hecke_res": max_hecke_res,
        "max_duality_gen_res": max_duality_gen_res,
        "max_duality_braid_res": max_duality_braid_res,
        "max_pauli_rowsum_res": max_pauli_rowsum_res,
        "max_conj_shortcut_res": max_conj_shortcut_res,
        "max_cg_res": max_cg_res,
        "max_eig_res": max_eig_res,
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        one = mp.mpf(1)
        me_mev = mp.mpf(codata("electron mass energy equivalent in MeV").value_str)
        mp_mev = mp.mpf(codata("proton mass energy equivalent in MeV").value_str)
        mn_mev = mp.mpf(codata("neutron mass energy equivalent in MeV").value_str)
        md_mev = mp.mpf(codata("deuteron mass energy equivalent in MeV").value_str)
        mt_mev = mp.mpf(codata("triton mass energy equivalent in MeV").value_str)
        mh_mev = mp.mpf(codata("helion mass energy equivalent in MeV").value_str)
        ma_mev = mp.mpf(codata("alpha particle mass energy equivalent in MeV").value_str)

        b_ame = {
            "2H": mp_mev + mn_mev - md_mev,
            "3H": mp_mev + mp.mpf(2) * mn_mev - mt_mev,
            "3He": mp.mpf(2) * mp_mev + mn_mev - mh_mev,
            "4He": mp.mpf(2) * mp_mev + mp.mpf(2) * mn_mev - ma_mev,
        }

        e0_mev = me_mev / (q0 * (q0 - one))
        eosc_mev = me_mev / ((q0 - one) ** 2)

        print("=" * 92)
        print(" Gap 1 (Option 1A) Pre-Registered 80-dps Probe: 4He 12q Wigner SU(4) Pauli Binding")
        print("=" * 92)
        print(f"  q0 (proton pin) = {fmt(q0, dps=30)}")
        print(
            f"  E0(q0) [MeV]    = {fmt(e0_mev, dps=16)}   |   E_osc(q0) [MeV] = {fmt(eosc_mev, dps=16)}"
        )
        print(
            "  CODATA-2022 B [MeV]: "
            + ", ".join(f"{k}={fmt(v, dps=10)}" for k, v in b_ame.items())
        )

        part_a1 = evaluate_part_a1_combinatorics()
        part_a2 = verify_sympy_6q_microscopic()
        part_b = evaluate_models_and_duality(q0, e0_mev, eosc_mev, me_mev, b_ame)

        print("\n[Part A1 & A2] Exact Combinatorics, SU(4) Shell Closure & Microscopic 6q SymPy:")
        print(f"  Combinatorics & A=5 closure pass : {part_a1['all_combinatorics_pass']}")
        print(f"  Microscopic 6q CMI/Pauli/Harvey  : {part_a2['all_exact_sympy_microscopic_pass']}")
        print(
            f"  Hoefsmit q0 conjugate duality    : "
            f"gen={fmt(part_b['max_duality_gen_res'], dps=10)}, "
            f"braid={fmt(part_b['max_duality_braid_res'], dps=10)}, "
            f"rowsum={fmt(part_b['max_pauli_rowsum_res'], dps=10)}"
        )
        print(
            f"  A=2 unprojected 25x25 W_2 check  : "
            f"B={part_b['a2_full_tensor_W2_audit']['bind_W2_in_Eosc_MeV'][:10]} MeV, "
            f"P(D_Pauli)={part_b['a2_full_tensor_W2_audit']['D_Pauli_subspace_probability'][:12]}"
        )

        print("\n[Part B] Pre-Registered 0-Parameter Models (E_osc chart [MeV] & exact ratios):")
        for m_key, m_val in part_b["models"].items():
            b2 = m_val["per_A"]["A=2"]["bind_exact_in_Eosc_MeV"]
            b3 = m_val["per_A"]["A=3"]["bind_exact_in_Eosc_MeV"]
            b4 = m_val["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"]
            r32 = m_val["scaling_ratios_exact_vs_A2"]["A3_over_A2"]
            r42 = m_val["scaling_ratios_exact_vs_A2"]["A4_over_A2"]
            d4 = m_val["ame_comparison_in_Eosc_chart"]["4He_rel_diff_pct"]
            print(
                f"  {m_key:<34} 2H={b2[:8]}, A3={b3[:8]}, 4He={b4[:9]} ({d4[:7]}%) "
                f"| 1 : {r32[:7]} : {r42[:8]}"
            )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath+sympy")
        wb.set_description(
            "Pre-registered 80-dps (50-dps serialized) evaluation closing Open Gap 1 (Option 1A): "
            "conjugate Young-diagram pairing [A,A,A]' = [3^A], Wigner SU(4)_{sigma tau} "
            "multiplicity (20, 50, 20, 1, 0) & 12-quark Pauli 1s-shell closure at A >= 5, "
            "microscopic 6q chromomagnetic O_CM & Matveev-Sorba/Harvey (1/9, 4/45, 4/5) "
            "verification over Q, q_0-deformed Hoefsmit conjugate duality, and 6 zero-parameter "
            "colour-spin-isospin Hamiltonians (M0-M5) across 2H, 3H/3He, and 4He."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("E0_MeV", fmt(e0_mev, dps=OUT_DPS))
        wb.add_parameter("E_osc_MeV", fmt(eosc_mev, dps=OUT_DPS))
        wb.add_parameter("m_e_MeV", fmt(me_mev, dps=OUT_DPS))
        wb.add_parameter("free_parameters", 0)

        wb.add_data(
            "lean_module",
            "folio/quantum-observable-universe/lean/QOU/Nuclear/TwelveQuarkWignerPauliBinding.lean",
        )
        wb.add_data(
            "preregistration",
            "computations/probes/gap1_4he_wigner_pauli_12q/PREREGISTRATION.md",
        )
        wb.add_data(
            "codata_2022_nuclear_binding_MeV",
            {k: fmt(v, dps=OUT_DPS) for k, v in b_ame.items()},
        )
        wb.add_data(
            "codata_2022_binding_ratios_vs_2H",
            {
                "3H_over_2H": fmt(b_ame["3H"] / b_ame["2H"], dps=25),
                "3He_over_2H": fmt(b_ame["3He"] / b_ame["2H"], dps=25),
                "4He_over_2H": fmt(b_ame["4He"] / b_ame["2H"], dps=25),
            },
        )
        wb.add_data("part_a1_combinatorics_and_shell_closure", part_a1)
        wb.add_data("part_a2_sympy_6q_microscopic_cmi_and_pauli", part_a2)
        wb.add_data("part_a3_hoefsmit_conjugate_duality_residuals", {
            "all_yamanouchi_signs_consistent": part_b["all_signs_consistent"],
            "max_hecke_braid_residual": fmt(part_b["max_hecke_res"], dps=20),
            "max_generator_conjugate_duality_residual": fmt(part_b["max_duality_gen_res"], dps=20),
            "max_braid_transposition_duality_residual": fmt(
                part_b["max_duality_braid_res"], dps=20
            ),
            "max_pauli_proj_rowsum_and_sym_residual": fmt(part_b["max_pauli_rowsum_res"], dps=20),
            "max_sparse_conjugation_shortcut_residual": fmt(
                part_b["max_conj_shortcut_res"], dps=20
            ),
        })
        wb.add_data("part_b_a2_full_tensor_W2_audit", part_b["a2_full_tensor_W2_audit"])
        wb.add_data("part_b_models_M0_to_M5", part_b["models"])

        wb.add_assertion(
            "su4_weyl_dims_20_50_20_1_0_and_a5_pauli_shell_closure_exact",
            1 if part_a1["all_combinatorics_pass"] else 0,
            1,
            "0",
            source="TwelveQuarkWignerPauliBinding.conjugate_rectThree_eq_colThree & su4WeylDim_light_nuclei_and_shell_closure",
        )
        wb.add_assertion(
            "microscopic_6q_cmi_pauli_norm_1_over_9_and_harvey_weights_exact",
            1 if part_a2["all_exact_sympy_microscopic_pass"] else 0,
            1,
            "0",
            source="TwelveQuarkWignerPauliBinding.pauli_cmi_operator_identity & cmi_spectrum_and_pauli_norm",
        )
        wb.add_assertion(
            "hoefsmit_q0_conjugate_duality_and_pauli_rowsum_1_below_1e_minus_74",
            fmt(
                max(
                    part_b["max_hecke_res"],
                    part_b["max_duality_gen_res"],
                    part_b["max_duality_braid_res"],
                    part_b["max_pauli_rowsum_res"],
                    part_b["max_conj_shortcut_res"],
                ),
                dps=15,
            ),
            "0",
            "1e-74",
            source="TwelveQuarkWignerPauliBinding.hecke_conjugate_duality_and_pauli_invariance",
        )
        wb.add_assertion(
            "cg_and_lanczos_eigen_residuals_below_1e_minus_70",
            fmt(max(part_b["max_cg_res"], part_b["max_eig_res"]), dps=15),
            "0",
            "1e-70",
            source="80-dps Hoefsmit CG and full-reorthogonalized Lanczos certification across A=2,3,4",
        )
        m0_4he = mp.mpf(
            part_b["models"]["M0_w4_baseline_colour_V2"]["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"]
        )
        _w4_wit = json.loads(
            (
                _ROOT
                / "computations"
                / "probes"
                / "w4_colour_reconn_stokes_aomega"
                / "w4_colour_reconn_stokes_aomega_probe.witness.json"
            ).read_text(encoding="utf-8")
        )
        w4_ref = mp.mpf(
            _w4_wit["data"]["part_b_colour_reconnection_models"][
                "G2_intra_casimir__V2_allpairs_fierz"
            ]["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"]
        )
        wb.add_assertion(
            "m0_reproduces_w4_baseline_4he_14p4877_mev_exact",
            fmt(abs(m0_4he - w4_ref), dps=15),
            "0",
            "1e-20",
            source="Exact regression reproduction of #9221 G2_intra_casimir__V2_allpairs_fierz",
        )
        bh32_m1 = mp.mpf(
            part_b["models"]["M1_colour_only_true_KA_fierz"]["scaling_ratios_BH2_vs_A2"][
                "A3_over_A2"
            ]
        )
        bh42_m1 = mp.mpf(
            part_b["models"]["M1_colour_only_true_KA_fierz"]["scaling_ratios_BH2_vs_A2"][
                "A4_over_A2"
            ]
        )
        r42_m1 = mp.mpf(
            part_b["models"]["M1_colour_only_true_KA_fierz"]["scaling_ratios_exact_vs_A2"][
                "A4_over_A2"
            ]
        )
        wb.add_assertion(
            "all_models_strictly_bind_and_true_ka_achieves_exact_1_3_6_bh2_and_gt6_exact",
            1
            if (
                part_b["all_signs_consistent"]
                and part_b["all_models_bind"]
                and abs(bh32_m1 - mp.mpf(3)) < mp.mpf("1e-20")
                and abs(bh42_m1 - mp.mpf(6)) < mp.mpf("1e-20")
                and r42_m1 > mp.mpf(6)
            )
            else 0,
            1,
            "0",
            source="TwelveQuarkWignerPauliBinding.pauli_collective_schur_superradiance & ColourReconnectionStokesAssembly.multiChannel_schur_rayleigh_lt",
        )

        wb.add_caveat(
            "1. All 6 pre-registered Hamiltonians (M0-M5) have zero tunable or per-isotope "
            "parameters (CAL-1/2/3 only: proton-pinned q_0 and electron mass m_e in the documented "
            "E_osc(q_0) = m_e / (q_0 - 1)^2 and E_0(q_0) = m_e / (q_0(q_0 - 1)) charts). "
            "2. Strong-sector models M0-M5 are strictly SU(2)_tau isospin-symmetric, so 3H and 3He "
            "receive identical strong binding before electromagnetic pp Coulomb + (m_n - m_p) "
            "core-breaking (~0.764 MeV empirical splitting). "
            "3. Short-range (0s)^{3A} single-bag collapse is proved repulsive under O_CM (+56/3, "
            "+64, +128 for A=2,3,4), confirming that physical light-nuclei binding arises via "
            "virtual Bloch-Horowitz tunnelling from the factorized A-nucleon cluster channel into "
            "Pauli-conjugate [A,A,A] (x) [3^A] hidden-colour-spin-isospin channels rather than "
            "static 12-quark bag collapse."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
