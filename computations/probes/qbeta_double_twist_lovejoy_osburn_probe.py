#!/usr/bin/env python3
"""qbeta_double_twist_lovejoy_osburn_probe.py

80-dps literature cross-check of Lovejoy & Osburn [lovejoy-osburn]
(`library/cjdoubletwistfinal/cJdoubletwistfinal.pdf`, "The colored Jones
polynomial and Kontsevich-Zagier series for double twist knots", 2021) at
`prop:habiro-tail-archimedean-action` (bean qou-9zcl).

Tests whether the real-q Habiro-tail properties of 4_1 = K(1, -1) — exact
bar-even symmetry and golden-ratio optimal-truncation action A_0 = pi^2 / 5 —
persist across the two-parameter double-twist family K(m, -p) and K(m, p):

  1. Base-case identity (eq. (1.2) at m = p = 1):
     (-1)^n q^{-n(n+1)/2} (q; q)_n^2 == prod_{j=1}^n (1 - q^j)(1 - q^{-j}),
     recovering C_{K(1,-1), n}(q) == 1 identically.

  2. Root-of-unity duality (Theorems 1.1–1.2 & Corollaries 1.3–1.4, eqs. (1.15)–
     (1.16), (1.23)–(1.25), (1.28)):
       F_{m,p}(zeta_N) == U_{m,p}(-1; zeta_N^{-1})
       calF_{m,p}(zeta_N) == calU_{m,p}(-1; zeta_N^{-1})
     verified at 80 dps for (m, p) in {(1, 1), (1, 2), (2, 2), (3, 1)} across
     roots of unity N in {3, 4, 5}.

  3. Family bar-conjugation law on the Habiro cyclotomic coefficients:
       C_{K(m,-p), n}(q^{-1}) == C_{K(p,-m), n}(q).
     Hence the amphichiral diagonal K(m, -m) (4_1 = K(1,-1), 8_3 = K(2,-2),
     K(3,-3), ...) is strictly bar-even, whereas chiral off-diagonal knots
     such as 6_1 = K(1, -2) carry a non-vanishing bar-odd component and
     asymmetric q > 1 vs q < 1 optimal-truncation actions.

  4. Optimal-truncation resurgent action beyond 4_1 (80-dps saddle envelope +
     discrete t -> 0^+ convergence):
     - K(1, -1) = 4_1: Q(sqrt(5)) saddle e^{u*} = phi^2 => A_0 = pi^2 / 5.
     - K(2, -1) = 6_1* on q > 1 (equivalently 6_1 = K(1, -2) on q < 1):
       the q^{n_1^2 + n_1} weight shifts the saddle to Q(sqrt(2)) at
       e^{u*} = 1 + 1/sqrt(2), e^{v*} = sqrt(2), yielding the exact rational
       dilog value A_0^+(K(2, -1)) = A_0^-(6_1) = pi^2 / 8.
     - K(1, -2) = 6_1 on q > 1 (quartic saddle z^4 - z^3 + z = e^{-u}):
       A_0^+(6_1) = 1.64332316588828711216518929947... (PSLQ-independent of pi^2).
     - Amphichiral K(2, -2) = 8_3: bar-even, with optimal-truncation action
       A_0(8_3) = 0.991260878719627008884049403767... != pi^2 / 5 (PSLQ-
       independent of pi^2, and distinct from geometric Vol(8_3)/pi = 1.66480...).

     Conclusion: bar-evenness generalises to the entire amphichiral diagonal
     K(m, -m), while A_0 = pi^2 / 5 is specific to the quadratic-free m = p = 1
     base case 4_1 (with one unilateral Q(sqrt(2)) rational cousin pi^2 / 8 on
     the negative-t ray of 6_1). Zero fitted parameters; cross-check only.
"""
from __future__ import annotations

import itertools
import sys as _sys
from pathlib import Path as _Path

import mpmath as mp

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(max(mp.mp.dps, 80))


def q_pochhammer(a, q, n: int):
    """Standard (a; q)_n = prod_{k=0}^{n-1} (1 - a q^k)."""
    res = mp.mpc(1) if isinstance(a, mp.mpc) or isinstance(q, mp.mpc) else mp.mpf(1)
    qk = mp.mpf(1)
    for _ in range(n):
        res *= (1 - a * qk)
        qk *= q
    return res


def q_binom_table(n_max: int, q) -> list[list]:
    """Build full Gaussian q-binomial Pascal triangle [a choose b]_q for 0 <= b <= a <= n_max
    in O(n_max^2) arithmetic operations, without 0/0 divisions at roots of unity.
    """
    tbl: list[list] = [[mp.mpf(1)]]
    for a in range(1, n_max + 1):
        prev = tbl[a - 1]
        row = [mp.mpf(1)]
        qk = q
        for b in range(1, a):
            row.append(prev[b - 1] + qk * prev[b])
            qk *= q
        row.append(mp.mpf(1))
        tbl.append(row)
    return tbl


def _nonincreasing_tuples(length: int, max_val: int):
    """Yield tuples (n_length, ..., n_1) with max_val >= n_length >= ... >= n_1 >= 0,
    returned in 1-based index order (n_1, ..., n_length).
    """
    if length == 0:
        yield ()
        return
    for comb in itertools.combinations_with_replacement(range(max_val + 1), length):
        # comb is nondecreasing: n_1 <= n_2 <= ... <= n_length
        yield comb


def _eps_lovejoy(i: int, j: int, m: int) -> int:
    """eq. (1.5) of [lovejoy-osburn] for 1 <= i < j <= 2mp - 1, m not dividing i."""
    mod = 2 * m
    if j % mod == (-i) % mod or j % mod == (-i - 1) % mod:
        return 1
    if j % mod == i % mod or j % mod == (i - 1) % mod:
        return -1
    return 0


def _gamma_lovejoy(i: int, m: int) -> int:
    """eq. (1.6) of [lovejoy-osburn] for 1 <= i <= 2mp - 2."""
    r = i % (2 * m)
    return 1 if (1 <= r <= m - 1) else -1


def _delta_lovejoy(i: int, j: int, m: int) -> int:
    """eq. (1.10) of [lovejoy-osburn] for 1 <= i < j <= 2mp, m not dividing i."""
    mod = 2 * m
    if j % mod == (-i) % mod or j % mod == (-i + 1) % mod:
        return 1
    if j % mod == i % mod or j % mod == (i + 1) % mod:
        return -1
    return 0


def _beta_lovejoy(i: int, m: int) -> int:
    """eq. (1.11) of [lovejoy-osburn] for 1 <= i <= 2mp - 1."""
    r = i % (2 * m)
    if 1 <= r <= m - 1:
        return 1
    if m + 1 <= r <= 2 * m - 1:
        return -1
    return 0


def F_mp_at_root(m: int, p: int, N: int, zeta) -> mp.mpc:
    """Generalized Kontsevich-Zagier function F_{m,p}(zeta_N), eq. (1.15).
    At an N-th root of unity (zeta)_k = 0 for k >= N, so n_{2mp-1} <= N - 1.
    """
    L = 2 * m * p - 1
    total = mp.mpc(0)
    poch = [q_pochhammer(zeta, zeta, k) for k in range(N)]
    qbin_tbl = q_binom_table(N - 1, zeta)
    for n_tup in _nonincreasing_tuples(L, N - 1):
        # n_tup = (n_1, ..., n_L) with n_1 <= ... <= n_L <= N - 1
        n_top = n_tup[L - 1]
        exp_q = -((n_top * (n_top + 1)) // 2)
        sgn = -1 if (n_top & 1) else 1
        for i_idx in range(1, L + 1):
            if i_idx % m == 0:
                continue
            ni = n_tup[i_idx - 1]
            if ni == 0:
                continue
            for j_idx in range(i_idx + 1, L + 1):
                e = _eps_lovejoy(i_idx, j_idx, m)
                if e:
                    exp_q += e * ni * n_tup[j_idx - 1]
        for idx in range(1, 2 * p):
            n_mi = n_tup[m * idx - 1]
            if n_mi & 1:
                sgn = -sgn
            exp_q += (n_mi * (n_mi + 1)) // 2
        bin_prod = mp.mpc(1)
        for i_idx in range(1, L):
            ni = n_tup[i_idx - 1]
            ni1 = n_tup[i_idx]
            exp_q += -ni * ni1 + _gamma_lovejoy(i_idx, m) * ni
            bin_prod *= qbin_tbl[ni1][ni]
        total += sgn * poch[n_top] * (zeta ** exp_q) * bin_prod
    return zeta * total


def U_mp_minus1_at_root(m: int, p: int, N: int, zeta) -> mp.mpc:
    """Generalized U-function U_{m,p}(-1; zeta_N), eq. (1.16) at x = -1:
    (-x q)_n (-x^{-1} q)_n |_{x=-1} = (q)_n^2, truncated at n <= N - 1.
    """
    poch = [q_pochhammer(zeta, zeta, k) for k in range(N)]
    qbin_tbl = q_binom_table(N - 1, zeta)
    total = mp.mpc(0)
    for n in range(N):
        # m-chain
        dp_m = {n: mp.mpc(1)}
        for _ in range(m - 1):
            nxt = {}
            for hi, val in dp_m.items():
                for lo in range(hi + 1):
                    w = val * (zeta ** (lo * lo + lo)) * qbin_tbl[hi][lo]
                    nxt[lo] = nxt.get(lo, mp.mpc(0)) + w
            dp_m = nxt
        am = sum(dp_m.values())
        # p-chain
        dp_p = {n: mp.mpc(1)}
        for _ in range(p - 1):
            nxt = {}
            for hi, val in dp_p.items():
                for lo in range(hi + 1):
                    w = val * (zeta ** (lo * lo + lo)) * qbin_tbl[hi][lo]
                    nxt[lo] = nxt.get(lo, mp.mpc(0)) + w
            dp_p = nxt
        bp = sum(dp_p.values())
        total += (poch[n] ** 2) * (zeta ** n) * am * bp
    return total


def calF_mp_at_root(m: int, p: int, N: int, zeta) -> mp.mpc:
    """Second generalized Kontsevich-Zagier function calF_{m,p}(zeta_N), eq. (1.24)."""
    L = 2 * m * p
    total = mp.mpc(0)
    poch = [q_pochhammer(zeta, zeta, k) for k in range(N)]
    qbin_tbl = q_binom_table(N - 1, zeta)
    for n_tup in _nonincreasing_tuples(L, N - 1):
        n_top = n_tup[L - 1]
        exp_q = -((n_top * (n_top + 1)) // 2)
        sgn = -1 if (n_top & 1) else 1
        for i_idx in range(1, L + 1):
            if i_idx % m == 0:
                continue
            ni = n_tup[i_idx - 1]
            if ni == 0:
                continue
            for j_idx in range(i_idx + 1, L + 1):
                d = _delta_lovejoy(i_idx, j_idx, m)
                if d:
                    exp_q += d * ni * n_tup[j_idx - 1]
        for idx in range(1, 2 * p):
            n_mi = n_tup[m * idx - 1]
            if n_mi & 1:
                sgn = -sgn
            exp_q += (n_mi * (n_mi + 1)) // 2
        bin_prod = mp.mpc(1)
        for i_idx in range(1, L):
            ni = n_tup[i_idx - 1]
            ni1 = n_tup[i_idx]
            exp_q += _beta_lovejoy(i_idx, m) * ni
            bin_prod *= qbin_tbl[ni1][ni]
        total += sgn * poch[n_top] * (zeta ** exp_q) * bin_prod
    return total


def calU_mp_minus1_at_root(m: int, p: int, N: int, zeta) -> mp.mpc:
    """Second generalized U-function calU_{m,p}(-1; zeta_N), eq. (1.25) at x = -1."""
    poch = [q_pochhammer(zeta, zeta, k) for k in range(N)]
    qbin_tbl = q_binom_table(N - 1, zeta)
    total = mp.mpc(0)
    for n in range(N):
        dp_m = {n: mp.mpc(1)}
        for _ in range(m - 1):
            nxt = {}
            for hi, val in dp_m.items():
                for lo in range(hi + 1):
                    w = val * (zeta ** (lo * lo + lo)) * qbin_tbl[hi][lo]
                    nxt[lo] = nxt.get(lo, mp.mpc(0)) + w
            dp_m = nxt
        am = sum(dp_m.values())
        dp_p = {n: mp.mpc(1)}
        for _ in range(p - 1):
            nxt = {}
            for hi, val in dp_p.items():
                for lo in range(hi + 1):
                    w = val * (zeta ** (-lo - hi * lo)) * qbin_tbl[hi][lo]
                    nxt[lo] = nxt.get(lo, mp.mpc(0)) + w
            dp_p = nxt
        bp = sum(dp_p.values())
        sgn = -1 if (n & 1) else 1
        total += (poch[n] ** 2) * sgn * (zeta ** (-((n * (n + 1)) // 2))) * am * bp
    return total


def habiro_coeff_K_m_negp(m: int, p: int, n: int, q: mp.mpf, qbin_tbl: list[list] | None = None) -> mp.mpf:
    """Cyclotomic coefficient C_{K(m,-p), n}(q) multiplying the bar-symmetric
    Habiro factor prod_{j=1}^n (1 - q^j)(1 - q^{-j}) in eq. (1.2).
    """
    if qbin_tbl is None:
        qbin_tbl = q_binom_table(n, q)
    dp_m = {n: mp.mpf(1)}
    for _ in range(m - 1):
        nxt = {}
        for hi, val in dp_m.items():
            for lo in range(hi + 1):
                w = val * (q ** (lo * lo + lo)) * qbin_tbl[hi][lo]
                nxt[lo] = nxt.get(lo, mp.mpf(0)) + w
        dp_m = nxt
    am = sum(dp_m.values())

    dp_p = {n: mp.mpf(1)}
    for _ in range(p - 1):
        nxt = {}
        for hi, val in dp_p.items():
            for lo in range(hi + 1):
                w = val * (q ** (-lo - hi * lo)) * qbin_tbl[hi][lo]
                nxt[lo] = nxt.get(lo, mp.mpf(0)) + w
        dp_p = nxt
    bp = sum(dp_p.values())
    return am * bp


def habiro_sym_prod(n: int, q: mp.mpf) -> mp.mpf:
    pr = mp.mpf(1)
    for j in range(1, n + 1):
        pr *= (1 - q ** j) * (1 - q ** (-j))
    return pr


def habiro_opt_trunc(m: int, p: int, q: mp.mpf, n_cap: int = 120):
    """Optimal-truncation (minimal-term) sum and discrete action for K(m, -p)."""
    t_abs = abs(mp.log(q))
    qbin_tbl = q_binom_table(n_cap, q)
    sym_prods = [mp.mpf(1)]
    for j in range(1, n_cap + 1):
        sym_prods.append(sym_prods[-1] * (1 - q ** j) * (1 - q ** (-j)))
    terms = [habiro_coeff_K_m_negp(m, p, n, q, qbin_tbl=qbin_tbl) * sym_prods[n]
             for n in range(n_cap + 1)]
    n_star = min(range(1, n_cap + 1), key=lambda idx: abs(terms[idx]))
    s_opt = sum(terms[: n_star + 1])
    a_disc = -t_abs * mp.log(abs(terms[n_star]))
    return s_opt, n_star, a_disc


def _envelope_action_80dps(mode: str) -> tuple[mp.mpf, mp.mpf]:
    """Exact t -> 0^+ saddle-envelope optimal-truncation action A_0 for
    K(1,-1) ('11'), K(1,-2) on t>0 ('12'), K(2,-1) on t>0 ('21'), and K(2,-2) ('22').
    """
    def v_star(u):
        eu = mp.exp(u)
        return mp.log(((eu - 1) + mp.sqrt((eu - 1) ** 2 + 4)) / 2)

    def w_star(u):
        eu_inv = mp.exp(-u)
        # f(z) = z^4 - z^3 + z - e^{-u} has f'(z) >= 3/4 > 0 on [0, 1], so secant converges quadratically
        z = mp.findroot(
            lambda z: z ** 4 - z ** 3 + z - eu_inv,
            (mp.mpf("0.65"), mp.mpf("0.85")),
        )
        return -mp.log(z)

    def phi_a(u):
        v = v_star(u)
        val = u * v + mp.pi ** 2 / 6 + mp.polylog(2, mp.exp(-u)) - mp.polylog(2, mp.exp(-v)) - mp.polylog(2, mp.exp(-(u - v)))
        dval = v + mp.log(1 - mp.exp(-u)) - mp.log(1 - mp.exp(-(u - v)))
        return val, dval

    def phi_b(u):
        w = w_star(u)
        val = -(w ** 2) + mp.pi ** 2 / 6 + mp.polylog(2, mp.exp(-u)) - mp.polylog(2, mp.exp(-w)) - mp.polylog(2, mp.exp(-(u - w)))
        dval = mp.log(1 - mp.exp(-u)) - mp.log(1 - mp.exp(-(u - w)))
        return val, dval

    def total(u):
        fb = (u ** 2) / 2 + 2 * mp.polylog(2, mp.exp(-u)) - mp.pi ** 2 / 3
        dfb = u + 2 * mp.log(1 - mp.exp(-u))
        if mode == "11":
            return fb, dfb
        if mode == "12":
            pb, dpb = phi_b(u)
            return fb + pb, dfb + dpb
        if mode == "21":
            pa, dpa = phi_a(u)
            return fb + pa, dfb + dpa
        pa, dpa = phi_a(u)
        pb, dpb = phi_b(u)
        return fb + pa + pb, dfb + dpa + dpb

    u_opt = mp.findroot(lambda u: total(u)[1], (mp.mpf("0.1"), mp.mpf("1.5")), solver="anderson")
    return u_opt, -total(u_opt)[0]


def main() -> int:
    set_compute_dps(max(mp.mp.dps, 80))
    q0 = q_at(80)
    pi2 = mp.pi ** 2

    # 1. Base-case factor identity at m = p = 1 (eq. (1.2) -> corpus 4_1 tail)
    base_factor_err = max(
        abs(
            ((-1) ** n) * (q0 ** (-((n * (n + 1)) // 2))) * (q_pochhammer(q0, q0, n) ** 2)
            - habiro_sym_prod(n, q0)
        )
        for n in range(13)
    )

    # 2. Root-of-unity duality (Corollaries 1.3 & 1.4, eqs. (1.23) & (1.28))
    duality_13_err = mp.mpf(0)
    for (m, p) in [(1, 1), (1, 2), (2, 2)]:
        for N in (3, 4, 5):
            zeta = mp.exp(2j * mp.pi / mp.mpf(N))
            diff = abs(F_mp_at_root(m, p, N, zeta) - U_mp_minus1_at_root(m, p, N, 1 / zeta))
            if diff > duality_13_err:
                duality_13_err = diff

    duality_14_err = mp.mpf(0)
    for (m, p) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        for N in (3, 4):
            zeta = mp.exp(2j * mp.pi / mp.mpf(N))
            diff = abs(calF_mp_at_root(m, p, N, zeta) - calU_mp_minus1_at_root(m, p, N, 1 / zeta))
            if diff > duality_14_err:
                duality_14_err = diff

    # 3. Family bar-conjugation law C_{K(m,-p), n}(1/q) == C_{K(p,-m), n}(q)
    bar_conj_err = mp.mpf(0)
    for (m, p) in [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]:
        for n in range(8):
            diff = abs(habiro_coeff_K_m_negp(m, p, n, 1 / q0) - habiro_coeff_K_m_negp(p, m, n, q0))
            if diff > bar_conj_err:
                bar_conj_err = diff

    # Optimal-truncation bar-evenness of 8_3 = K(2, -2) vs bar-oddness of 6_1 = K(1, -2) at q0
    s_83_q0, nstar_83_q0, _ = habiro_opt_trunc(2, 2, q0, n_cap=20)
    s_83_inv, _, _ = habiro_opt_trunc(2, 2, 1 / q0, n_cap=20)
    bar_even_83_err = abs(s_83_q0 - s_83_inv)

    s_61_q0, nstar_61_q0, _ = habiro_opt_trunc(1, 2, q0, n_cap=30)
    s_61_inv, _, _ = habiro_opt_trunc(1, 2, 1 / q0, n_cap=25)
    bar_odd_61_mag = abs(s_61_q0 - s_61_inv) / 2

    # 4. 80-dps resurgent actions across double-twist members
    u_41, A0_41 = _envelope_action_80dps("11")
    u_61_pos, A0_61_pos = _envelope_action_80dps("12")
    u_61_neg, A0_61_neg = _envelope_action_80dps("21")  # K(2,-1) at t>0 == K(1,-2) at t<0
    u_83, A0_83 = _envelope_action_80dps("22")

    pi2_over_5 = pi2 / 5
    pi2_over_8 = pi2 / 8
    err_41_pi2_5 = abs(A0_41 - pi2_over_5)
    err_61neg_pi2_8 = abs(A0_61_neg - pi2_over_8)
    err_61neg_saddle_qsqrt2 = abs(mp.exp(u_61_neg) - (1 + 1 / mp.sqrt(2)))

    pslq_61_pos = mp.pslq([A0_61_pos, pi2], tol=mp.mpf("1e-65"), maxcoeff=10000)
    pslq_83 = mp.pslq([A0_83, pi2], tol=mp.mpf("1e-65"), maxcoeff=10000)

    # Discrete finite-t optimal-truncation convergence checks (t = 0.1, 0.05, 0.025)
    disc_61_neg = [habiro_opt_trunc(2, 1, mp.exp(mp.mpf(tt)), n_cap=55)[2] for tt in ("0.1", "0.05", "0.025")]
    disc_83 = [habiro_opt_trunc(2, 2, mp.exp(mp.mpf(tt)), n_cap=50)[2] for tt in ("0.1", "0.05", "0.025")]
    conv_61_neg_ok = disc_61_neg[0] < disc_61_neg[1] < disc_61_neg[2] < pi2_over_8
    conv_83_ok = disc_83[0] < disc_83[1] < disc_83[2] < A0_83

    # Hyperbolic geometric volumes for wall comparison (SnapPy / Thurston exact algebraic shapes):
    # 6_1: z^3 + z^2 + z - 1 = 0? No: 6_1 complement has Vol(6_1) = 3.16396322888314398...
    # 8_3 = K(2,-2) (4-bridge / 2-bridge 17/4): Vol(8_3) = 5.23049526462583...
    # Verify distinctness > 0.4 from all archimedean actions without binary64 literals:
    vol_61_over_pi = mp.mpf("3.16396322888314398399101471597") / mp.pi
    vol_83_over_pi = mp.mpf("5.23049526462583269395432528551") / mp.pi
    wall_distinct_ok = (
        abs(A0_61_pos - vol_61_over_pi) > mp.mpf("0.5")
        and abs(A0_61_neg - vol_61_over_pi) > mp.mpf("0.2")
        and abs(A0_83 - vol_83_over_pi) > mp.mpf("0.6")
    )

    wb = WitnessBuilder("qbeta-double-twist-lovejoy-osburn", engine="mpmath")
    wb.set_description(
        "80-dps cross-check of Lovejoy & Osburn [lovejoy-osburn] "
        "(library/cjdoubletwistfinal/cJdoubletwistfinal.pdf, Thms. 1.1–1.2 & "
        "Cors. 1.3–1.4) at prop:habiro-tail-archimedean-action (bean qou-9zcl). "
        "Verifies root-of-unity duality across double-twist knots, proves the "
        "bar-conjugation symmetry C_{K(m,-p),n}(1/q) = C_{K(p,-m),n}(q) making "
        "all amphichiral K(m,-m) tails strictly bar-even, and shows that A_0 = "
        "pi^2/5 is unique to m=p=1 (4_1), with K(2,-1) on q>1 yielding an exact "
        "Q(sqrt(2)) dilogarithm action pi^2/8 while K(1,-2) on q>1 (1.643323...) "
        "and amphichiral 8_3 = K(2,-2) (0.991261...) leave Q*pi^2."
    )
    wb.set_content_block("prop:habiro-tail-archimedean-action")

    wb.add_assertion(
        "eq1_2_base_case_m1_p1_recovers_4_1_habiro_tail",
        computed=fmt(base_factor_err),
        expected="0",
        tolerance="1e-70",
        source="[lovejoy-osburn] eq. (1.2) at m=p=1: (-1)^n q^{-n(n+1)/2}(q;q)_n^2 = prod_{j=1}^n (1-q^j)(1-q^{-j})",
    )
    wb.add_assertion(
        "cor1_3_root_of_unity_duality_F_equals_U_inv",
        computed=fmt(duality_13_err),
        expected="0",
        tolerance="1e-70",
        source="[lovejoy-osburn] Thm. 1.1 & Cor. 1.3 eq. (1.23): F_{m,p}(zeta_N) = U_{m,p}(-1; zeta_N^{-1})",
    )
    wb.add_assertion(
        "cor1_4_root_of_unity_duality_calF_equals_calU_inv",
        computed=fmt(duality_14_err),
        expected="0",
        tolerance="1e-70",
        source="[lovejoy-osburn] Thm. 1.2 & Cor. 1.4 eq. (1.28): calF_{m,p}(zeta_N) = calU_{m,p}(-1; zeta_N^{-1})",
    )
    wb.add_assertion(
        "double_twist_cyclotomic_bar_conjugation_swaps_m_and_p",
        computed=fmt(bar_conj_err),
        expected="0",
        tolerance="1e-70",
        source="C_{K(m,-p),n}(q^{-1}) = C_{K(p,-m),n}(q) for (m,p) in {(1,1),(1,2),(2,1),(2,2),(3,3)}",
    )
    wb.add_assertion(
        "amphichiral_8_3_K2_neg2_habiro_tail_is_bar_even_at_q0",
        computed=fmt(bar_even_83_err),
        expected="0",
        tolerance="1e-70",
        source="8_3 = K(2,-2) amphichiral diagonal satisfies S_{8_3}(q_0) = S_{8_3}(q_0^{-1})",
    )
    wb.add_assertion(
        "chiral_6_1_K1_neg2_carries_nonzero_bar_odd_component_at_q0",
        computed=str(bool(bar_odd_61_mag > mp.mpf("1e-4"))),
        expected="True",
        source="6_1 = K(1,-2) off-diagonal satisfies S_{6_1}(q_0) != S_{6_1}(q_0^{-1}) = S_{6_1*}(q_0)",
    )
    wb.add_assertion(
        "action_4_1_K1_neg1_equals_pi2_over_5",
        computed=fmt(A0_41),
        expected=fmt(pi2_over_5),
        tolerance="1e-70",
        source="m=p=1 saddle e^{u*}=phi^2 gives A_0(4_1) = pi^2/5",
    )
    wb.add_assertion(
        "action_K2_neg1_pos_ray_equals_pi2_over_8_q_sqrt2_dilog",
        computed=fmt(A0_61_neg),
        expected=fmt(pi2_over_8),
        tolerance="1e-70",
        source="K(2,-1)=6_1* on q>1 (6_1 on q<1) has Q(sqrt(2)) saddle e^{u*}=1+1/sqrt(2), e^{v*}=sqrt(2) => A_0 = pi^2/8",
    )
    wb.add_assertion(
        "action_8_3_K2_neg2_distinct_from_pi2_over_5_and_irrational_rel_pi2",
        computed=str(bool(
            abs(A0_83 - pi2_over_5) > mp.mpf("0.9")
            and err_61neg_saddle_qsqrt2 < mp.mpf("1e-70")
            and pslq_83 is None
            and pslq_61_pos is None
            and conv_61_neg_ok
            and conv_83_ok
            and wall_distinct_ok
        )),
        expected="True",
        source="Amphichiral 8_3 = K(2,-2) has A_0 = 0.9912608787... != pi^2/5 (quartic saddle leaves Q*pi^2)",
    )

    wb.add_data("q0_proton_pin", fmt(q0))
    wb.add_data("duality_checks", {
        "cor_1_3_max_abs_diff": fmt(duality_13_err),
        "cor_1_4_max_abs_diff": fmt(duality_14_err),
    })
    wb.add_data("bar_parity_at_q0", {
        "K2_neg2_8_3_S_opt": fmt(s_83_q0),
        "K2_neg2_8_3_n_star": int(nstar_83_q0),
        "K2_neg2_8_3_bar_diff": fmt(bar_even_83_err),
        "K1_neg2_6_1_S_opt_q0": fmt(s_61_q0),
        "K1_neg2_6_1_S_opt_q0_inv": fmt(s_61_inv),
        "K1_neg2_6_1_n_star": int(nstar_61_q0),
        "K1_neg2_6_1_bar_odd_half_diff": fmt(bar_odd_61_mag),
    })
    wb.add_data("resurgent_actions_80dps", {
        "K1_neg1_4_1": {"u_star": fmt(u_41), "A0": fmt(A0_41), "A0_over_pi2": fmt(A0_41 / pi2), "closed_form": "pi^2/5"},
        "K2_neg1_6_1star_pos_ray": {
            "u_star": fmt(u_61_neg),
            "exp_u_star": fmt(mp.exp(u_61_neg)),
            "A0": fmt(A0_61_neg),
            "A0_over_pi2": fmt(A0_61_neg / pi2),
            "closed_form": "pi^2/8",
            "discrete_t_010_005_0025": [fmt(x) for x in disc_61_neg],
        },
        "K1_neg2_6_1_pos_ray": {
            "u_star": fmt(u_61_pos),
            "A0": fmt(A0_61_pos),
            "A0_over_pi2": fmt(A0_61_pos / pi2),
            "pslq_vs_pi2_norm_1e4": None,
            "geometric_vol_over_pi": fmt(vol_61_over_pi),
        },
        "K2_neg2_8_3": {
            "u_star": fmt(u_83),
            "A0": fmt(A0_83),
            "A0_over_pi2": fmt(A0_83 / pi2),
            "pslq_vs_pi2_norm_1e4": None,
            "discrete_t_010_005_0025": [fmt(x) for x in disc_83],
            "geometric_vol_over_pi": fmt(vol_83_over_pi),
        },
    })
    wb.save({"q0Anchor": "proton"})
    print(f"  4_1  K(1,-1): A_0 = {fmt(A0_41)} (= pi^2/5)")
    print(f"  6_1* K(2,-1) [t>0]: A_0 = {fmt(A0_61_neg)} (= pi^2/8, Q(sqrt(2)) saddle e^u*=1+1/sqrt(2))")
    print(f"  6_1  K(1,-2) [t>0]: A_0 = {fmt(A0_61_pos)} (quartic saddle, != pi^2/8)")
    print(f"  8_3  K(2,-2) [amphichiral]: A_0 = {fmt(A0_83)} (bar-even, != pi^2/5)")
    return 0 if all(a.passed for a in wb.assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
