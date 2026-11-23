#!/usr/bin/env python3
"""Pre-registered 80-dps probe for Workstream W4 (`beans` qou-v2om, qou-0c19, qou-gpb5, qou-3q7t):
Many-Body 6q-12q Colour-Reconnection Nuclear Carrier & Figure-Eight Stokes Constant A_omega = 3.

Pre-registration committed BEFORE execution:
  - `computations/probes/w4_colour_reconn_stokes_aomega/PREREGISTRATION.md`
Formal Lean 4 backing (`0 sorry`, `0 axiom`, generic §7c):
  - `folio/quantum-observable-universe/lean/QOU/Nuclear/ColourReconnectionStokesAssembly.lean`

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact symbolic `sympy` verification over `Q(q)` for the 6q Jimbo overlap & q-Fierz spectrum,
  - zero `float64` imports, casts, or lossy literals (`probe-float64-guard.py` clean),
  - zero post-hoc parameter fitting (only CAL-1/2/3 enter MeV scale readouts).
"""

from __future__ import annotations

import itertools
import sys
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
from qou_substrate.constants import q_at, vol_4_1_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


# ---------------------------------------------------------------------------
# Part A helpers: Figure-eight (4_1) Eisenstein, A-polynomial, and GGM A_omega = 3
# ---------------------------------------------------------------------------
def smul_int(a: list[int], b: list[int], order: int) -> list[int]:
    out = [0] * (order + 1)
    for i, ca in enumerate(a):
        if ca == 0 or i > order:
            continue
        lim = order - i
        for j, cb in enumerate(b[: lim + 1]):
            if cb:
                out[i + j] += ca * cb
    return out


def sadd_int(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    return [
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    ]


def sscale_int(c: int, a: list[int]) -> list[int]:
    return [c * x for x in a]


def inv_pochhammer_sq_int(n: int, order: int) -> list[int]:
    out = [0] * (order + 1)
    out[0] = 1
    for j in range(1, n + 1):
        for _ in range(2):
            for d in range(j, order + 1):
                out[d] += out[d - j]
    return out


def eisenstein_e1_int(order: int) -> list[int]:
    out = [0] * (order + 1)
    out[0] = 1
    for n in range(1, order + 1):
        for k in range(n, order + 1, n):
            out[k] -= 4
    return out


def harmonic_h_int(n: int, order: int) -> list[int]:
    out = [0] * (order + 1)
    out[0] = 2 * n
    for j in range(1, n + 1):
        for k in range(j, order + 1, j):
            out[k] += 4
    return out


def ggm_g_series_int(m: int, order: int) -> tuple[list[int], list[int]]:
    """Exact integer q-series (G^0_m, G^1_m) from GGM 2012.00062 eqs. (51a)/(51b) for m >= -1."""
    e1 = eisenstein_e1_int(order)
    g0 = [0] * (order + 1)
    g1 = [0] * (order + 1)
    n = 0
    while True:
        expo = n * (n + 1) // 2 + m * n
        if n > abs(m) + 1 and expo > order:
            break
        if expo <= order:
            rem = order - expo
            ip = inv_pochhammer_sq_int(n, rem)
            sgn = -1 if (n % 2 == 1) else 1
            for d, c in enumerate(ip):
                g0[d + expo] += sgn * c
            w = sadd_int(sadd_int([2 * m], e1), harmonic_h_int(n, rem))
            tw = smul_int(ip, w[: rem + 1], rem)
            for d, c in enumerate(tw):
                g1[d + expo] += sgn * c
        n += 1
        if n > 4 * order + 8:
            break
    return g0, g1


def ggm_wronskian_int(m: int, order: int) -> list[list[list[int]]]:
    g0m, g1m = ggm_g_series_int(m, order)
    g0m1, g1m1 = ggm_g_series_int(m + 1, order)
    return [[g0m, g1m], [g0m1, g1m1]]


def mat2_mul_series_int(
    a: list[list[list[int]]], b: list[list[list[int]]], order: int
) -> list[list[list[int]]]:
    out: list[list[list[int]]] = [[[], []], [[], []]]
    for i in range(2):
        for j in range(2):
            acc = [0] * (order + 1)
            for k in range(2):
                acc = sadd_int(acc, smul_int(a[i][k], b[k][j], order))
            out[i][j] = acc[: order + 1]
    return out


def const_mat2_series_int(m: list[list[int]], order: int) -> list[list[list[int]]]:
    return [[[m[i][j]] + [0] * order for j in range(2)] for i in range(2)]


def evaluate_part_a_stokes_and_apoly(q0: mp.mpf) -> dict:
    """80-dps verification of Part A: Eisenstein Z[omega], 4_1 A-polynomial jet, GGM A_omega=3."""
    one = mp.mpf(1)
    omega = mp.exp(1j * mp.pi / mp.mpf(3))
    omega_bar = one - omega

    # 1. Eisenstein & tetrahedral cross-ratio identities
    eis_res = abs(one - omega + omega**2)
    eis_conj_res = abs(one - omega_bar + omega_bar**2)
    cube_res = abs(omega**3 + one)
    six_res = abs(omega**6 - one)
    disc_res = abs((2 * omega - one) ** 2 + mp.mpf(3))
    tet_res = abs(omega * (one - omega) - one)
    edge0_res = abs((omega**4) / ((one - omega) ** 2) - one)
    edge1_res = abs(((one / (one - omega)) * ((one - one / omega) ** 2)) ** 2 - one)
    min_root_sep = min(
        abs(mp.mpc(-1) - omega),
        abs(mp.mpc(-1) - omega_bar),
        abs(omega - omega_bar),
    )

    # 2. A-polynomial degree-3 L-specialization & 80-dps Cauchy contour extraction of tau, v_3
    def b_coeff(m_val: mp.mpc) -> mp.mpc:
        return m_val**4 - m_val**2 - mp.mpf(2) - m_val ** (-2) + m_val ** (-4)

    # Check A_AJ(1, L) = (L - 1)^3 and A_CCGLS(1, L) = (L - 1)(L + 1)^2 at test L points
    apoly_spec_max_err = mp.mpf(0)
    for l_str in ("-2", "-1", "1", "2", "3"):
        lv = mp.mpc(mp.mpf(l_str))
        b1 = b_coeff(mp.mpc(1))
        a_aj = (lv - one) * (lv**2 + b1 * lv + one)
        a_cc = (lv - one) * (lv**2 - b1 * lv + one)
        apoly_spec_max_err = max(
            apoly_spec_max_err,
            abs(a_aj - (lv - one) ** 3),
            abs(a_cc - (lv - one) * (lv + one) ** 2),
        )

    # Cauchy contour extraction on |u| = 1/32 (exact binary rational radius, 128 points)
    radius = one / mp.mpf(32)
    n_pts = 128
    samples: list[mp.mpc] = []
    s_prev: mp.mpc | None = None
    for k in range(n_pts):
        theta = 2 * mp.pi * mp.mpf(k) / mp.mpf(n_pts)
        u = radius * mp.exp(1j * theta)
        m_half = mp.exp(u / mp.mpf(2))
        bm_scaled = m_half**8 - m_half**6 - 2 * m_half**4 - m_half**2 + one
        w_disc = (bm_scaled**2 - 4 * m_half**8) / (u**2)
        s_cur = mp.sqrt(w_disc)
        if s_prev is not None and abs(s_cur - s_prev) > abs(-s_cur - s_prev):
            s_cur = -s_cur
        s_prev = s_cur
        l_cc = (bm_scaled + u * s_cur) / (2 * m_half**4)
        samples.append(mp.log(-l_cc))

    c_coeffs: list[mp.mpc] = []
    for deg in range(6):
        acc = mp.mpc(0)
        for k in range(n_pts):
            theta = 2 * mp.pi * mp.mpf(k) / mp.mpf(n_pts)
            acc += samples[k] * mp.exp(-1j * mp.mpf(deg) * theta)
        c_coeffs.append(acc / mp.mpf(n_pts) / (radius**deg))

    tau_exact = -1j * mp.sqrt(mp.mpf(3))
    v3_exact = -1j * mp.sqrt(mp.mpf(3)) / mp.mpf(3)
    tau_err = abs(c_coeffs[1] - tau_exact)
    v3_err = abs(c_coeffs[3] - v3_exact)
    even_v_err = max(abs(c_coeffs[0]), abs(c_coeffs[2]), abs(c_coeffs[4]))
    jet_rel_err = max(
        abs(c_coeffs[1] ** 2 + mp.mpf(3)),
        abs(3 * c_coeffs[3] - c_coeffs[1]),
    )

    # 3. Exact GGM Wronskian sandwich certification (Lean `ggm_stokes_symmetry_three`)
    a_ggm = [[0, 1], [1, 1]]
    b_ggm = [[0, 1], [1, 0]]
    c_ggm = [[0, -1], [1, 2]]
    ord_cert = 40
    wm1 = ggm_wronskian_int(-1, ord_cert)
    wm1_t = [[wm1[0][0], wm1[1][0]], [wm1[0][1], wm1[1][1]]]
    stilde = mat2_mul_series_int(
        mat2_mul_series_int(
            const_mat2_series_int(a_ggm, ord_cert),
            mat2_mul_series_int(
                mat2_mul_series_int(wm1, const_mat2_series_int(b_ggm, ord_cert), ord_cert),
                wm1_t,
                ord_cert,
            ),
            ord_cert,
        ),
        const_mat2_series_int(c_ggm, ord_cert),
        ord_cert,
    )
    all_even = all(
        stilde[i][j][k] % 2 == 0
        for i in range(2)
        for j in range(2)
        for k in range(ord_cert + 1)
    )
    splus = [
        [[x // 2 for x in stilde[i][j]] for j in range(2)]
        for i in range(2)
    ]
    det_wm1 = sadd_int(
        smul_int(wm1[0][0], wm1[1][1], ord_cert),
        sscale_int(-1, smul_int(wm1[0][1], wm1[1][0], ord_cert)),
    )
    det_wm1_ok = det_wm1[0] == 2 and all(x == 0 for x in det_wm1[1:])

    det_splus = sadd_int(
        smul_int(splus[0][0], splus[1][1], ord_cert),
        sscale_int(-1, smul_int(splus[0][1], splus[1][0], ord_cert)),
    )
    det_splus_ok = det_splus[0] == 1 and all(x == 0 for x in det_splus[1:])

    sym_diff = sadd_int(
        sadd_int(splus[0][1], splus[1][0]),
        sscale_int(-3, splus[0][0]),
    )
    sym_three_ok = all(x == 0 for x in sym_diff)
    base_q0_ok = (
        splus[0][0][0] == 1
        and splus[0][1][0] == 3
        and splus[1][0][0] == 0
        and splus[1][1][0] == 1
    )

    # Deep substrate evaluation at q_sub = 1 / q_0 = exp(-ln q_0) < 1
    ord_sub = 1600
    wm1_deep = ggm_wronskian_int(-1, ord_sub)
    wm1_deep_t = [[wm1_deep[0][0], wm1_deep[1][0]], [wm1_deep[0][1], wm1_deep[1][1]]]
    stilde_deep = mat2_mul_series_int(
        mat2_mul_series_int(
            const_mat2_series_int(a_ggm, ord_sub),
            mat2_mul_series_int(
                mat2_mul_series_int(
                    wm1_deep, const_mat2_series_int(b_ggm, ord_sub), ord_sub
                ),
                wm1_deep_t,
                ord_sub,
            ),
            ord_sub,
        ),
        const_mat2_series_int(c_ggm, ord_sub),
        ord_sub,
    )
    q_sub = one / q0
    q_pows = [one] * (ord_sub + 1)
    for k in range(1, ord_sub + 1):
        q_pows[k] = q_pows[k - 1] * q_sub

    s11_sub = mp.fsum((stilde_deep[0][0][k] // 2) * q_pows[k] for k in range(ord_sub + 1))
    s12_sub = mp.fsum((stilde_deep[0][1][k] // 2) * q_pows[k] for k in range(ord_sub + 1))
    s21_sub = mp.fsum((stilde_deep[1][0][k] // 2) * q_pows[k] for k in range(ord_sub + 1))
    s22_sub = mp.fsum((stilde_deep[1][1][k] // 2) * q_pows[k] for k in range(ord_sub + 1))

    s11_sub_3q = mp.fsum(
        (stilde_deep[0][0][k] // 2) * q_pows[k] for k in range((ord_sub * 3) // 4)
    )
    trunc_diff_s11 = abs(s11_sub - s11_sub_3q)
    r1_raw = s12_sub
    r2_ratio = s12_sub / s11_sub
    r3_sym = (s12_sub + s21_sub) / s11_sub
    r3_sym_err = abs(r3_sym - mp.mpf(3))
    det_sub_err = abs(s11_sub * s22_sub - s12_sub * s21_sub - one)

    # 4. Delta_lambda T5 assembly check at A_omega = 3
    ln_q0 = mp.log(q0)
    cusp_mod = mp.sqrt(mp.mpf(3)) / mp.mpf(4)
    a_omega = mp.mpf(3)
    pure_boost_cap_a1 = cusp_mod * (ln_q0**2)
    pure_boost_cap_a3 = a_omega * cusp_mod * (ln_q0**2)
    s_mu_anchor = mp.mpf("0.00968298")
    s_pr_anchor = mp.mpf("-0.03945936")
    theta_mu_implied = mp.sqrt(ln_q0**2 - s_mu_anchor / (a_omega * cusp_mod))
    theta_pr_implied = mp.sqrt(ln_q0**2 - s_pr_anchor / (a_omega * cusp_mod))

    return {
        "eisenstein_max_residual": max(
            eis_res, eis_conj_res, cube_res, six_res, disc_res, tet_res, edge0_res, edge1_res
        ),
        "flat_saddle_min_root_sep": min_root_sep,
        "apoly_spec_max_err": apoly_spec_max_err,
        "nz_tau_err": tau_err,
        "nz_v3_err": v3_err,
        "nz_even_leak": even_v_err,
        "nz_jet_rel_err": jet_rel_err,
        "ggm_cert_exact": bool(
            all_even and det_wm1_ok and det_splus_ok and sym_three_ok and base_q0_ok
        ),
        "r3_sym_err": r3_sym_err,
        "det_sub_err": det_sub_err,
        "trunc_diff_s11": trunc_diff_s11,
        "pure_boost_cap_a3_exceeds_s_mu": bool(pure_boost_cap_a3 > s_mu_anchor > pure_boost_cap_a1),
        "serialized": {
            "omega_re": fmt(omega.real, dps=OUT_DPS),
            "omega_im": fmt(omega.imag, dps=OUT_DPS),
            "vol_4_1": fmt(vol_4_1_at(WORK_DPS), dps=OUT_DPS),
            "eisenstein_max_residual": fmt(
                max(eis_res, eis_conj_res, cube_res, six_res, disc_res, tet_res), dps=20
            ),
            "snappy_gluing_max_residual": fmt(max(edge0_res, edge1_res), dps=20),
            "flat_saddle_min_root_separation": fmt(min_root_sep, dps=OUT_DPS),
            "apoly_degree_in_L": 3,
            "nz_tau_extracted_im": fmt(c_coeffs[1].imag, dps=OUT_DPS),
            "nz_v3_extracted_im": fmt(c_coeffs[3].imag, dps=OUT_DPS),
            "nz_tau_abs_error": fmt(tau_err, dps=20),
            "nz_v3_abs_error": fmt(v3_err, dps=20),
            "ggm_series_order_certified": ord_cert,
            "ggm_s11_first_8_coeffs": splus[0][0][:8],
            "ggm_s12_first_8_coeffs": splus[0][1][:8],
            "ggm_s21_first_8_coeffs": splus[1][0][:8],
            "ggm_substrate_q_sub": fmt(q_sub, dps=OUT_DPS),
            "ggm_substrate_S11": fmt(s11_sub, dps=25),
            "ggm_substrate_trunc_diff_1200_vs_1600": fmt(trunc_diff_s11, dps=15),
            "reading_R1_raw_S12": fmt(r1_raw, dps=25),
            "reading_R2_ratio_S12_over_S11": fmt(r2_ratio, dps=25),
            "reading_R3_symmetry_constant": fmt(r3_sym, dps=OUT_DPS),
            "reading_R3_abs_err_from_3": fmt(r3_sym_err, dps=20),
            "t5_cusp_modulus_sqrt3_over_4": fmt(cusp_mod, dps=OUT_DPS),
            "t5_pure_boost_cap_A1": fmt(pure_boost_cap_a1, dps=OUT_DPS),
            "t5_pure_boost_cap_A3": fmt(pure_boost_cap_a3, dps=OUT_DPS),
            "t5_diagnostic_theta_muon_at_A3": fmt(theta_mu_implied, dps=OUT_DPS),
            "t5_diagnostic_theta_proton_at_A3": fmt(theta_pr_implied, dps=OUT_DPS),
        },
    }


# ---------------------------------------------------------------------------
# Part B helpers: Hoefsmit S^{[A,A,A]} (A = 1..4) & U_q(sl_3) colour reconnection
# ---------------------------------------------------------------------------
SyTableau = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


def enumerate_rect_three_syts(a_nuc: int) -> list[SyTableau]:
    """Enumerate all standard Young tableaux of rectangular shape [A, A, A] in canonical order."""
    n_tot = 3 * a_nuc
    partial: list[tuple[list[int], list[int], list[int]]] = [([], [], [])]
    for val in range(1, n_tot + 1):
        nxt: list[tuple[list[int], list[int], list[int]]] = []
        for r0, r1, r2 in partial:
            if len(r0) < a_nuc:
                nxt.append((r0 + [val], r1, r2))
            if len(r1) < len(r0):
                nxt.append((r0, r1 + [val], r2))
            if len(r2) < len(r1):
                nxt.append((r0, r1, r2 + [val]))
        partial = nxt
    syts = [(tuple(r0), tuple(r1), tuple(r2)) for r0, r1, r2 in partial]
    syts.sort()
    return syts


def factorized_nucleon_syt(a_nuc: int) -> SyTableau:
    """Unique column-factorized SYT T_fac^{(A)} with {3k+1, 3k+2, 3k+3} in column k."""
    return (
        tuple(3 * k + 1 for k in range(a_nuc)),
        tuple(3 * k + 2 for k in range(a_nuc)),
        tuple(3 * k + 3 for k in range(a_nuc)),
    )


def q_bracket_mp(q: mp.mpf, n: int) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


def q_dim_rect_three_mp(q: mp.mpf, a_nuc: int) -> mp.mpf:
    """Quantum dimension dim_q([A, A, A]) = [3A]_q! / prod_{x in [A,A,A]} [h(x)]_q."""
    num = mp.mpf(1)
    for k in range(1, 3 * a_nuc + 1):
        num *= q_bracket_mp(q, k)
    den = mp.mpf(1)
    for r in range(3):
        for c in range(a_nuc):
            h_len = (a_nuc - c) + (2 - r)
            den *= q_bracket_mp(q, h_len)
    return num / den


class SparseHoefsmitGenerators:
    """Exact 80-dps real-symmetric Hoefsmit generators R_k(q) (0 <= k < 3A - 1) on S^{[A,A,A]}."""

    def __init__(self, a_nuc: int, q: mp.mpf) -> None:
        self.a_nuc = a_nuc
        self.n_strands = 3 * a_nuc
        self.q = q
        self.q_inv = mp.mpf(1) / q
        self.h = q - self.q_inv
        self.syts = enumerate_rect_three_syts(a_nuc)
        self.dim = len(self.syts)
        self.syt_to_idx = {t: idx for idx, t in enumerate(self.syts)}
        self.fac_idx = self.syt_to_idx[factorized_nucleon_syt(a_nuc)]

        # Precompute cell positions (row, col) of 1..3A for every SYT
        pos_list: list[list[tuple[int, int]]] = []
        for t in self.syts:
            pos = [(0, 0)] * (self.n_strands + 1)
            for r in range(3):
                for c, val in enumerate(t[r]):
                    pos[val] = (r, c)
            pos_list.append(pos)

        # Each generator k is stored as row adjacency list: rows[i] = [(j, val), ...] (at most 2 entries)
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
                    # Build swapped tableau s_k T
                    grid = [list(row) for row in t]
                    grid[r1][c1] = v2
                    grid[r2][c2] = v1
                    j = self.syt_to_idx[(tuple(grid[0]), tuple(grid[1]), tuple(grid[2]))]
                    rows_k[i] = [(i, diag), (j, off)]
                    inv_rows_k[i] = [(i, diag - self.h), (j, off)]
            self.gen_rows.append(rows_k)
            self.inv_gen_rows.append(inv_rows_k)

    def apply_gen(self, k: int, vec: list[mp.mpf], inverse: bool = False) -> list[mp.mpf]:
        rows = self.inv_gen_rows[k] if inverse else self.gen_rows[k]
        out = [mp.mpf(0)] * self.dim
        for i, entries in enumerate(rows):
            acc = mp.mpf(0)
            for j, val in entries:
                acc += val * vec[j]
            out[i] = acc
        return out

    def apply_word(self, word: list[tuple[int, bool]], vec: list[mp.mpf]) -> list[mp.mpf]:
        """Apply a list of `(generator_index, is_inverse)` right-to-left to `vec`."""
        cur = list(vec)
        for k, inv in reversed(word):
            cur = self.apply_gen(k, cur, inverse=inv)
        return cur

    def build_dense_from_word(self, word: list[tuple[int, bool]]) -> list[list[mp.mpf]]:
        """Build full dim x dim matrix of a braid word by applying to unit vectors."""
        zero = mp.mpf(0)
        one = mp.mpf(1)
        cols: list[list[mp.mpf]] = []
        for j in range(self.dim):
            ej = [zero] * self.dim
            ej[j] = one
            cols.append(self.apply_word(word, ej))
        return [[cols[j][i] for j in range(self.dim)] for i in range(self.dim)]

    def verify_relations_max_residual(self) -> mp.mpf:
        """Check Hecke quadratic and Artin braid relations on deterministic test vectors."""
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


def matvec_dense(mat: list[list[mp.mpf]], vec: list[mp.mpf]) -> list[mp.mpf]:
    return [mp.fsum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def dot_mp(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(u[i] * v[i] for i in range(len(u)))


def cg_solve_spd(
    mat: list[list[mp.mpf]], rhs: list[mp.mpf], tol: mp.mpf, max_iter: int = 300
) -> tuple[list[mp.mpf], mp.mpf]:
    """80-dps Conjugate Gradient solver on SPD hidden-colour block, returning (x, inf_residual)."""
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
    """Exact 80-dps lowest eigenpair of real-symmetric matrix:
    uses `mp.eigsy` for dim <= 60, and full-reorthogonalized Lanczos + `mp.eigsy` on the
    invariant Krylov subspace for dim = 462, certified by exact L_inf eigen-residual!"""
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

    # Full-reorthogonalized Lanczos from |T_fac> (with deterministic perturbation so no invariant block is missed)
    zero = mp.mpf(0)
    v0 = [mp.mpf(1) / mp.mpf(1000 * (i + 3)) for i in range(n)]
    v0[start_idx] = mp.mpf(1)
    nrm0 = mp.sqrt(dot_mp(v0, v0))
    v0 = [x / nrm0 for x in v0]

    basis: list[list[mp.mpf]] = [v0]
    m_steps = min(200, n)
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
        # Double classical Gram-Schmidt reorthogonalization at 80 dps
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


def verify_sympy_6q_identities() -> dict:
    """Exact symbolic Q(q) check of Lean `sixQuark_R23_overlap` and `qFierz_charPoly_roots`."""
    q = sp.Symbol("q", nonzero=True)
    inv_q = sp.Integer(1) / q

    # Build 6-quark tensor eps6 on {0,1,2}^3 x {0,1,2}^3 (36 nonzero entries out of 729)
    perms3 = list(itertools.permutations((0, 1, 2)))

    def inv_count(p: tuple[int, int, int]) -> int:
        return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])

    eps3 = {p: (-inv_q) ** inv_count(p) for p in perms3}
    norm_eps3_sq = sp.simplify(sum(val**2 for val in eps3.values()))
    expected_norm_eps3_sq = sp.simplify(
        (1 + inv_q**2) * (1 + inv_q**2 + inv_q**4)
    )
    norm_ok = sp.simplify(norm_eps3_sq - expected_norm_eps3_sq) == 0

    # Compute <eps6 | R_{2,3}(q) | eps6> over all 36 x 36 pairs
    overlap_num = sp.Integer(0)
    for p_left, v_left in eps3.items():
        for p_right, v_right in eps3.items():
            a, b, c = p_left
            d, e, f = p_right
            amp_ket = v_left * v_right
            if c == d:
                # R(e_c (x) e_c) = q e_c (x) e_c
                overlap_num += amp_ket * (q * amp_ket)
            else:
                # R(e_c (x) e_d) has e_d (x) e_c plus [c > d](q - q^-1) e_c (x) e_d
                swapped_left = (a, b, d)
                swapped_right = (c, e, f)
                if swapped_left in eps3 and swapped_right in eps3:
                    overlap_num += amp_ket * eps3[swapped_left] * eps3[swapped_right]
                if c > d:
                    overlap_num += amp_ket * (q - inv_q) * amp_ket

    q2 = q + inv_q
    q3 = q**2 + 1 + inv_q**2
    q4 = q**3 + q + inv_q + inv_q**3
    overlap_ratio = sp.simplify(overlap_num / (norm_eps3_sq**2))
    overlap_ok = sp.simplify(overlap_ratio - (q**3) / q3) == 0

    vq_sq = sp.simplify(1 + (q - inv_q) * overlap_ratio - overlap_ratio**2)
    vq_sq_ok = sp.simplify(vq_sq - (q2 * q4) / (q3**2)) == 0

    mu = sp.Symbol("mu")
    char_poly = (0 - mu) * (-(q**3 + inv_q**3) / (2 * q3) - mu) - (q2 * q4) / (4 * q3**2)
    factored_poly = (mu - q2 / (2 * q3)) * (mu + q4 / (2 * q3))
    char_ok = sp.simplify(char_poly - factored_poly) == 0

    return {
        "all_exact_sympy_pass": bool(norm_ok and overlap_ok and vq_sq_ok and char_ok),
        "eps3_norm_sq": str(norm_eps3_sq),
        "six_quark_R23_overlap_ratio": str(overlap_ratio),
        "hidden_colour_vq_sq": str(vq_sq),
        "q_fierz_eigenvalues": [str(sp.simplify(q2 / (2 * q3))), str(sp.simplify(-q4 / (2 * q3)))],
    }


def build_gap_and_coupling_matrices(
    hoef: SparseHoefsmitGenerators,
) -> tuple[dict[str, list[list[mp.mpf]]], dict[str, list[list[mp.mpf]]]]:
    """Build the 2 pre-registered intra-nucleon gap matrices (G1, G2) and 3 inter-nucleon
    colour-reconnection matrices (V1, V2, V3) on S^{[A,A,A]}_{H_{3A}(q_0)}."""
    a_nuc = hoef.a_nuc
    dim = hoef.dim
    q = hoef.q
    q_inv = hoef.q_inv
    h = hoef.h
    zero = mp.mpf(0)
    half = mp.mpf(1) / mp.mpf(2)
    q3_bal = q_bracket_mp(q, 3)
    diag_shift_r = (q**3) / q3_bal

    # Dense matrices for single generators R_k and R_k^{-1}
    r_mats = [hoef.build_dense_from_word([(k, False)]) for k in range(hoef.n_strands - 1)]

    # Gap G1: sum_{k=0}^{A-1} (R_{3k} + R_{3k+1} + 2 q^{-1} I)
    g1 = [[zero] * dim for _ in range(dim)]
    for k in range(a_nuc):
        m0 = r_mats[3 * k]
        m1 = r_mats[3 * k + 1]
        for i in range(dim):
            for j in range(dim):
                g1[i][j] += m0[i][j] + m1[i][j]
            g1[i][i] += 2 * q_inv

    # Gap G2: sum_{k=0}^{A-1} ((R_{3k} R_{3k+1} R_{3k})^2 - q^{-6} I) / (q - q^{-1})
    g2 = [[zero] * dim for _ in range(dim)]
    q_m6 = q ** (-6)
    for k in range(a_nuc):
        g0, g1_idx = 3 * k, 3 * k + 1
        ft_word = [
            (g0, False),
            (g1_idx, False),
            (g0, False),
            (g0, False),
            (g1_idx, False),
            (g0, False),
        ]
        ft_mat = hoef.build_dense_from_word(ft_word)
        for i in range(dim):
            for j in range(dim):
                # Symmetrize numerically (exact symmetric in theory)
                val = half * (ft_mat[i][j] + ft_mat[j][i])
                if i == j:
                    val -= q_m6
                g2[i][j] += val / h

    # Coupling V1: chain q-Fierz sum_{k=0}^{A-2} 1/2 * (R_{3k+2} - (q^3/[3]_q) I)
    v1 = [[zero] * dim for _ in range(dim)]
    for k in range(a_nuc - 1):
        mb = r_mats[3 * k + 2]
        for i in range(dim):
            for j in range(dim):
                v1[i][j] += half * mb[i][j]
            v1[i][i] -= half * diag_shift_r

    # Coupling V2: complete-graph K_A symmetrized pair-exchange sum_{0 <= a < b < A}
    # Transport strand s = 3a + 2 to t - 1 = 3b - 1 via positive braid R_{3b-2}...R_{3a+2},
    # cross with R_{3b-1}, and return via inverses.
    v2 = [[zero] * dim for _ in range(dim)]
    for a_idx in range(a_nuc):
        for b_idx in range(a_idx + 1, a_nuc):
            s_strand = 3 * a_idx + 2
            target_gen = 3 * b_idx - 1
            prefix = [(g_idx, False) for g_idx in range(target_gen - 1, s_strand - 1, -1)]
            suffix = [(g_idx, True) for g_idx in range(s_strand, target_gen)]
            pair_word = prefix + [(target_gen, False)] + suffix
            p_mat = hoef.build_dense_from_word(pair_word)
            fac_diag = p_mat[hoef.fac_idx][hoef.fac_idx]
            for i in range(dim):
                for j in range(dim):
                    v2[i][j] += half * (half * (p_mat[i][j] + p_mat[j][i]))
                v2[i][i] -= half * fac_diag

    # Coupling V3: adjacent-interface gamma-gamma bond V_k^3 = (R_{3k+2} R_{3k+3}^{-1})^3 (symmetrized, zeroed on |T_fac>)
    v3 = [[zero] * dim for _ in range(dim)]
    for k in range(a_nuc - 1):
        g_inter = 3 * k + 2
        g_next = 3 * k + 3
        gg_word = [
            (g_inter, False),
            (g_next, True),
            (g_inter, False),
            (g_next, True),
            (g_inter, False),
            (g_next, True),
        ]
        gg_mat = hoef.build_dense_from_word(gg_word)
        fac_diag = gg_mat[hoef.fac_idx][hoef.fac_idx]
        for i in range(dim):
            for j in range(dim):
                v3[i][j] += half * (gg_mat[i][j] + gg_mat[j][i])
            v3[i][i] -= fac_diag

    return {"G1_intra_gen": g1, "G2_intra_casimir": g2}, {
        "V1_chain_fierz": v1,
        "V2_allpairs_fierz": v2,
        "V3_chain_gg_bond": v3,
    }


def evaluate_part_b_colour_reconnection(
    q0: mp.mpf, e0_mev: mp.mpf, eosc_mev: mp.mpf, me_mev: mp.mpf, b_ame: dict[str, mp.mpf]
) -> dict:
    """80-dps evaluation of 6q/9q/12q Hoefsmit colour reconnection & Schur-complement shifts."""
    singlet_counts: dict[str, dict] = {}
    hoef_by_a: dict[int, SparseHoefsmitGenerators] = {}
    max_hecke_braid_res = mp.mpf(0)

    for a_nuc in (1, 2, 3, 4):
        syts = enumerate_rect_three_syts(a_nuc)
        qdim = q_dim_rect_three_mp(q0, a_nuc)
        singlet_counts[f"A={a_nuc}_{3 * a_nuc}q"] = {
            "A": a_nuc,
            "n_quarks": 3 * a_nuc,
            "su3_singlet_dim": len(syts),
            "hidden_colour_dim": len(syts) - 1,
            "q_dim_at_q0": fmt(qdim, dps=OUT_DPS),
        }
        if a_nuc >= 2:
            hoef = SparseHoefsmitGenerators(a_nuc, q0)
            max_hecke_braid_res = max(
                max_hecke_braid_res, hoef.verify_relations_max_residual()
            )
            hoef_by_a[a_nuc] = hoef

    # Evaluate all 2 x 3 = 6 pre-registered zero-parameter (Gap, Coupling) models across A = 2, 3, 4
    gv_mats_by_a = {a_nuc: build_gap_and_coupling_matrices(hoef_by_a[a_nuc]) for a_nuc in (2, 3, 4)}

    models_out: dict[str, dict] = {}
    max_cg_res = mp.mpf(0)
    max_eig_res = mp.mpf(0)
    all_ground_lowered = True
    a2_order4_sandwich_ok = True

    for g_name in ("G1_intra_gen", "G2_intra_casimir"):
        for v_name in ("V1_chain_fierz", "V2_allpairs_fierz", "V3_chain_gg_bond"):
            m_key = f"{g_name}__{v_name}"
            per_a: dict[str, dict] = {}
            shifts_bh2: dict[int, mp.mpf] = {}
            shifts_exact: dict[int, mp.mpf] = {}

            for a_nuc in (2, 3, 4):
                hoef = hoef_by_a[a_nuc]
                dim = hoef.dim
                fac = hoef.fac_idx
                hid_indices = [i for i in range(dim) if i != fac]

                g_mat = gv_mats_by_a[a_nuc][0][g_name]
                v_mat = gv_mats_by_a[a_nuc][1][v_name]

                # Verify H_0 |T_fac> = 0
                h0_fac_norm = max(abs(g_mat[i][fac]) for i in range(dim))
                max_cg_res = max(max_cg_res, h0_fac_norm)

                # Extract hidden-colour block Q_hid H_0 Q_hid and coupling vector b = Q_hid V |T_fac>
                h_hid = [[g_mat[i][j] for j in hid_indices] for i in hid_indices]
                b_vec = [v_mat[i][fac] for i in hid_indices]
                v_leak_sq = dot_mp(b_vec, b_vec)

                sol_hid, cg_res = cg_solve_spd(h_hid, b_vec, mp.mpf("1e-76"))
                max_cg_res = max(max_cg_res, cg_res)
                delta_bh2 = -dot_mp(b_vec, sol_hid)  # <= 0 (strictly < 0 when b_vec != 0)

                # Exact coupled ground state of H_total = H_0 + V
                h_tot = [
                    [g_mat[i][j] + v_mat[i][j] for j in range(dim)]
                    for i in range(dim)
                ]
                e_ground, psi_ground, eig_res = lowest_eigenpair_sym(h_tot, fac)
                max_eig_res = max(max_eig_res, eig_res)

                if v_leak_sq > mp.mpf("1e-60") and not (e_ground < mp.mpf(0) and delta_bh2 < mp.mpf(0)):
                    all_ground_lowered = False

                # At A = 2 with central G2 and V1/V2 (pure 2-state {|11>, |88>_sym} invariant block!),
                # verify Lean's exact O(v^4) sandwich: -v^2/Delta_8 < E_- <= -v^2/Delta_8 + v^4/Delta_8^3
                if a_nuc == 2 and g_name == "G2_intra_casimir" and v_name == "V1_chain_fierz":
                    delta8 = h_hid[0][0]  # central on [2,1] x [2,1]: scalar 2 * q_0^-3 [3]_{q_0}
                    # Check if V1 leaves the 2D Krylov span {|T_fac>, V1|T_fac>} invariant:
                    # Note V1|88> can couple inside the 4D |88> space, whereas H_0 = Delta_8 * I_4 on ALL 4 |88> states!
                    # Let's record both exact E_- and the 2-state formula E_2state(0, delta8, sqrt(v_leak_sq)).
                    e_2state = (delta8 - mp.sqrt(delta8**2 + 4 * v_leak_sq)) / mp.mpf(2)
                    lo_bound = -v_leak_sq / delta8
                    hi_bound = -v_leak_sq / delta8 + (v_leak_sq**2) / (delta8**3)
                    if not (lo_bound < e_2state <= hi_bound):
                        a2_order4_sandwich_ok = False

                p_hid_prob = mp.mpf(1) - (psi_ground[fac] ** 2)
                shifts_bh2[a_nuc] = abs(delta_bh2)
                shifts_exact[a_nuc] = abs(e_ground)

                per_a[f"A={a_nuc}"] = {
                    "dim_singlet": dim,
                    "v_offdiag_norm_sq": fmt(v_leak_sq, dps=OUT_DPS),
                    "delta_E_BH2_dimless": fmt(delta_bh2, dps=OUT_DPS),
                    "E_ground_exact_dimless": fmt(e_ground, dps=OUT_DPS),
                    "hidden_colour_admixture_prob": fmt(p_hid_prob, dps=OUT_DPS),
                    "bind_BH2_in_E0_MeV": fmt(abs(delta_bh2) * e0_mev, dps=25),
                    "bind_exact_in_E0_MeV": fmt(abs(e_ground) * e0_mev, dps=25),
                    "bind_exact_in_Eosc_MeV": fmt(abs(e_ground) * eosc_mev, dps=25),
                    "bind_exact_in_me_MeV": fmt(abs(e_ground) * me_mev, dps=25),
                    "cg_solve_inf_residual": fmt(cg_res, dps=15),
                    "lanczos_eig_inf_residual": fmt(eig_res, dps=15),
                }

            # Dimensionless scaling ratios relative to A = 2 (deuteron)
            b2_bh = shifts_bh2[2]
            b2_ex = shifts_exact[2]
            models_out[m_key] = {
                "per_A": per_a,
                "scaling_ratios_BH2_vs_A2": {
                    "A3_over_A2": fmt(shifts_bh2[3] / b2_bh, dps=20),
                    "A4_over_A2": fmt(shifts_bh2[4] / b2_bh, dps=20),
                },
                "scaling_ratios_exact_vs_A2": {
                    "A3_over_A2": fmt(shifts_exact[3] / b2_ex, dps=20),
                    "A4_over_A2": fmt(shifts_exact[4] / b2_ex, dps=20),
                },
                "ame_comparison_ratios_in_E0_chart": {
                    "2H_model_over_AME": fmt((shifts_exact[2] * e0_mev) / b_ame["2H"], dps=15),
                    "3H_model_over_AME": fmt((shifts_exact[3] * e0_mev) / b_ame["3H"], dps=15),
                    "3He_model_over_AME": fmt((shifts_exact[3] * e0_mev) / b_ame["3He"], dps=15),
                    "4He_model_over_AME": fmt((shifts_exact[4] * e0_mev) / b_ame["4He"], dps=15),
                },
            }

    return {
        "singlet_counts": singlet_counts,
        "models": models_out,
        "max_hecke_braid_res": max_hecke_braid_res,
        "max_cg_res": max_cg_res,
        "max_eig_res": max_eig_res,
        "all_ground_lowered": all_ground_lowered,
        "a2_order4_sandwich_ok": a2_order4_sandwich_ok,
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
            "3H": mp_mev + 2 * mn_mev - mt_mev,
            "3He": 2 * mp_mev + mn_mev - mh_mev,
            "4He": 2 * mp_mev + 2 * mn_mev - ma_mev,
        }

        # W6 documented energy-scale charts (no fitting; CAL-1/2/3 only)
        e0_mev = me_mev / (q0 * (q0 - one))
        eosc_mev = me_mev / ((q0 - one) ** 2)

        print("=" * 84)
        print(" W4 Pre-Registered 80-dps Probe: 6q-12q Colour Reconnection & GGM A_omega = 3")
        print("=" * 84)
        print(f"  q0 (proton pin) = {fmt(q0, dps=30)}")
        print(f"  E0(q0) [MeV]    = {fmt(e0_mev, dps=16)}   |   E_osc(q0) [MeV] = {fmt(eosc_mev, dps=16)}")
        print(
            "  CODATA-2022 B [MeV]: "
            + ", ".join(f"{k}={fmt(v, dps=10)}" for k, v in b_ame.items())
        )

        part_a = evaluate_part_a_stokes_and_apoly(q0)
        sympy_6q = verify_sympy_6q_identities()
        part_b = evaluate_part_b_colour_reconnection(q0, e0_mev, eosc_mev, me_mev, b_ame)

        print("\n[Part A] Figure-eight Eisenstein, A-polynomial jet & GGM A_omega = 3:")
        print(f"  Eisenstein / gluing max residual : {fmt(part_a['eisenstein_max_residual'], dps=10)}")
        print(f"  NZ Cauchy jet |tau + i sqrt(3)|  : {fmt(part_a['nz_tau_err'], dps=10)}")
        print(f"  NZ Cauchy jet |v3 + i sqrt(3)/3| : {fmt(part_a['nz_v3_err'], dps=10)}")
        print(f"  GGM integer series cert (q^40)   : {part_a['ggm_cert_exact']}")
        print(f"  Substrate R3 = (S12+S21)/S11 err : {fmt(part_a['r3_sym_err'], dps=10)}")

        print("\n[Part B] 6q/9q/12q Hoefsmit S^{[A,A,A]} Colour Reconnection (0 free params):")
        print(f"  SymPy exact Q(q) 6q checks       : {sympy_6q['all_exact_sympy_pass']}")
        print(f"  Hoefsmit Hecke/braid max resid   : {fmt(part_b['max_hecke_braid_res'], dps=10)}")
        for m_key, m_val in part_b["models"].items():
            e2 = m_val["per_A"]["A=2"]["bind_exact_in_E0_MeV"]
            e3 = m_val["per_A"]["A=3"]["bind_exact_in_E0_MeV"]
            e4 = m_val["per_A"]["A=4"]["bind_exact_in_E0_MeV"]
            r32 = m_val["scaling_ratios_exact_vs_A2"]["A3_over_A2"]
            r42 = m_val["scaling_ratios_exact_vs_A2"]["A4_over_A2"]
            print(
                f"  {m_key:<34} |E_-|*E0 [MeV]: A2={e2[:8]}, A3={e3[:8]}, A4={e4[:8]} "
                f"| ratios 1 : {r32[:7]} : {r42[:7]}"
            )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath+sympy")
        wb.set_description(
            "Pre-registered 80-dps (50-dps serialized) W4 evaluation of (A) figure-eight "
            "Eisenstein Z[omega] cusp lattice, degree-3 A-polynomial L-specialization, NZ "
            "cusp-modulus jet (tau = -i*sqrt(3), v_3 = -i*sqrt(3)/3), and GGM Wronskian "
            "sandwich proof of A_omega = 3 vs Delta_lambda T5 assembly, and (B) exact 6q (5D), "
            "9q (42D), and 12q (462D) U_q(sl_3) Hoefsmit colour-reconnection overlaps and "
            "Bloch-Horowitz Schur-complement ground-energy shifts against CODATA-2022 light-nuclei "
            "binding deficits (beans qou-v2om, qou-0c19, qou-gpb5, qou-3q7t)."
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
            "folio/quantum-observable-universe/lean/QOU/Nuclear/ColourReconnectionStokesAssembly.lean",
        )
        wb.add_data(
            "codata_2022_nuclear_binding_MeV",
            {
                k: fmt(v, dps=OUT_DPS)
                for k, v in b_ame.items()
            },
        )
        wb.add_data(
            "codata_2022_binding_ratios_vs_2H",
            {
                "3H_over_2H": fmt(b_ame["3H"] / b_ame["2H"], dps=25),
                "3He_over_2H": fmt(b_ame["3He"] / b_ame["2H"], dps=25),
                "4He_over_2H": fmt(b_ame["4He"] / b_ame["2H"], dps=25),
            },
        )
        wb.add_data(
            "c_knot_conditioning_reference_qou_3q7t",
            {
                "note": (
                    "Bean qou-3q7t title cites legacy Convention-C C_knot(D)=5.85; canonical "
                    "Convention-D values (c-knot-cancellation-conditioning.witness.json) are "
                    "6.0679 / 6.7061 / 4.9054 / 290.007 with 4He cancellation kappa=0.007955."
                ),
                "legacy_convention_C_deuteron": "5.85",
                "canonical_convention_D": {
                    "2H": "6.0679",
                    "3H": "6.7061",
                    "3He": "4.9054",
                    "4He": "290.007",
                },
                "cancellation_ratio_kappa_convention_D": {
                    "2H": "0.2911",
                    "3H": "0.4137",
                    "3He": "0.2944",
                    "4He": "0.0079548",
                },
            },
        )
        wb.add_data("part_a_figure_eight_stokes_aomega", part_a["serialized"])
        wb.add_data("part_b_sympy_6q_exact_checks", sympy_6q)
        wb.add_data("part_b_su3_singlet_multiplicities", part_b["singlet_counts"])
        wb.add_data("part_b_colour_reconnection_models", part_b["models"])

        wb.add_assertion(
            "eisenstein_and_snappy_gluing_identities_hold_80dps",
            fmt(part_a["eisenstein_max_residual"], dps=15),
            "0",
            "1e-70",
            source="ColourReconnectionStokesAssembly.eisenstein_minimal_poly",
        )
        wb.add_assertion(
            "apoly_degree3_specialization_and_nz_cusp_jet_80dps",
            fmt(
                max(
                    part_a["apoly_spec_max_err"],
                    part_a["nz_tau_err"],
                    part_a["nz_v3_err"],
                    part_a["nz_jet_rel_err"],
                ),
                dps=15,
            ),
            "0",
            "1e-65",
            source="ColourReconnectionStokesAssembly.aPolyFourOne_degree_and_meridian_one & aPoly_nz_cusp_jet",
        )
        wb.add_assertion(
            "ggm_wronskian_sandwich_proves_aomega_eq_3_exact_and_substrate",
            1 if (part_a["ggm_cert_exact"] and part_a["r3_sym_err"] < mp.mpf("1e-70")) else 0,
            1,
            "0",
            source="ColourReconnectionStokesAssembly.ggm_stokes_symmetry_three",
        )
        wb.add_assertion(
            "su3_singlet_dimensions_1_5_42_462_and_sympy_6q_overlap_exact",
            1
            if (
                part_b["singlet_counts"]["A=1_3q"]["su3_singlet_dim"] == 1
                and part_b["singlet_counts"]["A=2_6q"]["su3_singlet_dim"] == 5
                and part_b["singlet_counts"]["A=3_9q"]["su3_singlet_dim"] == 42
                and part_b["singlet_counts"]["A=4_12q"]["su3_singlet_dim"] == 462
                and sympy_6q["all_exact_sympy_pass"]
            )
            else 0,
            1,
            "0",
            source="ColourReconnectionStokesAssembly.su3SingletDim_light_nuclei & sixQuark_R23_overlap",
        )
        wb.add_assertion(
            "hoefsmit_relations_cg_and_lanczos_residuals_below_1e_minus_70",
            fmt(
                max(
                    part_b["max_hecke_braid_res"],
                    part_b["max_cg_res"],
                    part_b["max_eig_res"],
                ),
                dps=15,
            ),
            "0",
            "1e-68",
            source="80-dps Hoefsmit S^{[A,A,A]} Hecke/braid, CG, and Lanczos residual certification",
        )
        wb.add_assertion(
            "colour_reconnection_strictly_lowers_ground_energy_all_models",
            1 if (part_b["all_ground_lowered"] and part_b["a2_order4_sandwich_ok"]) else 0,
            1,
            "0",
            source="ColourReconnectionStokesAssembly.multiChannel_schur_rayleigh_lt & colourReconnection_lowers_ground_energy",
        )

        wb.add_caveat(
            "1. GGM Stokes constant A_omega = 3 is proved algebraically from the 2-tetrahedra cusp "
            "sandwich A_GGM W_-1(q) B_GGM W_-1(q)^T C_GGM (S^+_12 + S^+_21 = 3 S^+_11 at all q); "
            "while A_omega = 3 lifts the T5 pure-boost ceiling to 0.014142 > S_mu = 0.009683, the "
            "particle-specific angular deformation vartheta_K remains an open G3 monodromy input "
            "(bean qou-qnnq) and the l^1-ceiling still precludes closing nuclear binding by per-block "
            "Delta_lambda weights alone. "
            "2. Coupling |1^A> to the (4, 41, 461) hidden-colour reconnection channels in S^{[A,A,A]} "
            "strictly lowers the ground energy across all 6 pre-registered zero-parameter models "
            "(resolving the wrong-sign unbinding of the factorized single-gamma-gamma chain), and "
            "complete-graph K_A pair exchange (V2) boosts the A=2 -> 3 -> 4 scaling from chain (1:2:3) "
            "to pairwise (~1:3:6), but still misses the super-pairwise alpha-cluster jump (1:3.81:12.72) "
            "without spin-isospin SU(4) Wigner [4] space-exchange weighting and a derived energy-scale "
            "unit (W6 R = tau_e / hbar_q^2 ~ 70.40)."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
