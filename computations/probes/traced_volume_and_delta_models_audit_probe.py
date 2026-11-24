#!/usr/bin/env python3
"""80-dps algebraic & substrate diagnostic for beans qou-jwl8 and qou-bg3w.

1. Part A (`qou-jwl8` — `QOU/BraidsAndKnots/TracedVolumeVsHalfTwist.lean`):
   - Symbolic `sympy` verification over `Q(q, z)` of:
     * `tr_M(P_3(a,b,c)) - tr_M(Delta_3(a,b,c)) = (b - c) * (z^2 - h*z - 1)`;
     * `z_D^2 - (q - q^-1)*z_D - 1 = -(q^4 + q^2 + 1) / (q^2 + 1)^2`;
     * `tr_M(P_4(0)) - tr_M(Delta_4) = -h * z * (z^2 - h*z - 1)`.
   - 80-dps normal-form Markov trace audit at `q_0` (`q0Anchor = "proton"`),
     `z_D = q_0^3 / (q_0^2 + 1)`, across all `2^A` binary orderings for
     `A = 3` (`4/8` differ, `o_0 == o_1` iff equal), `A = 4` (`14/16` differ,
     including uniform `pppp`), and `A = 5` (`32/32` differ).

2. Part B (`qou-bg3w` — live & historical `Delta = NF(n) - NF(p)` naming inventory):
   - Evaluates at 80-dps proton `q_0` (and exact rational `q = 111/100` to
     verify the `1.66e-4` `_Q_FRAC` shift from `b607c7ad351`) all six
     nucleon-word `Delta` constructions referenced across the corpus:
     (M1) `Delta_S` (1-/2-crossing short model: `net = h^2/2 - h`,
          `tr_M^z = h^2/2 - h*z`, `chi_{(2,1)} = 0`, `(D1)` affine in `z`);
     (M2) `nuc9_interleaved` (`V^3 * quark_pairs`, 9 crossings, pre-`qou-1qsw`);
     (M3) `nuc11_interleaved` (`build_nucleon_nf_mp` == `build_atom_nf_exact@q0`,
          `V^3 * quark_pairs * sigma_0^2`, 11 interleaved crossings);
     (M4) `nuc11_grouped` (`grouped_word_from_chains(nucleon_gen_chains)`,
          11 generator-bucketed crossings `g_0` then `g_1`);
     (M5) `categorical_Lminus` (`V^3 * quark_pairs * (sigma_1 * sigma_0)`,
          11 crossings with `L_-`, excluded scope-(b) on octic Sturm count 0);
     (M6) `gg_V3_canonical` (`2026-11-20..22` ruled `gamma-gamma` core `V^3`,
          6 crossings for both `p` and `n`, so `Delta_{V^3} = 0` on the bare
          word while `Q_beta` comes from the `T_3` weight-space split).
   - Verifies that `pyhecke.atom.build_nucleon_nf_mp` and `nucleon_gen_chains`
     now emit the SAME crossing count (`11 == 11` post-`qou-1qsw`), and differ
     in `H_3(q_0)` (`net = -0.2271597118` vs `-0.2331977113`) strictly from
     generator bucketing (`(sigma_0 sigma_1^-1)^3` vs `sigma_0^3 sigma_1^-3`).
"""

from __future__ import annotations

import itertools
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "tools" / "pyhecke" / "python",
    _ROOT / "computations" / "substrate",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


def _swap(p: tuple[int, ...], i: int) -> tuple[int, ...]:
    lst = list(p)
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return tuple(lst)


def _inv_count(p: tuple[int, ...]) -> int:
    return sum(
        1
        for i in range(len(p))
        for j in range(i + 1, len(p))
        if p[i] > p[j]
    )


def _rmul_gen(x: dict[tuple[int, ...], mp.mpf], i: int, h: mp.mpf) -> dict[tuple[int, ...], mp.mpf]:
    """Right-multiply `x` in `H_n(q)` by `T_{s_i}` (`T_{s_i}^2 = h T_{s_i} + 1`)."""
    out: dict[tuple[int, ...], mp.mpf] = {}
    zero = mp.mpf(0)
    for w, c in x.items():
        ws = _swap(w, i)
        if _inv_count(ws) > _inv_count(w):
            out[ws] = out.get(ws, zero) + c
        else:
            out[w] = out.get(w, zero) + h * c
            out[ws] = out.get(ws, zero) + c
    return out


def _rmul_shifted(
    x: dict[tuple[int, ...], mp.mpf], i: int, d: mp.mpf, h: mp.mpf
) -> dict[tuple[int, ...], mp.mpf]:
    """Right-multiply `x` in `H_n(q)` by `T_{s_i} + d`."""
    zero = mp.mpf(0)
    y = _rmul_gen(x, i, h)
    if d == zero:
        return y
    keys = set(x) | set(y)
    return {k: y.get(k, zero) + d * x.get(k, zero) for k in keys}


def _reduced_word(w: tuple[int, ...]) -> list[int]:
    word: list[int] = []
    cur = w
    while _inv_count(cur) > 0:
        for i in range(len(cur) - 1):
            if cur[i] > cur[i + 1]:
                word.append(i)
                cur = _swap(cur, i)
                break
    return list(reversed(word))


def _make_markov_tracer(h: mp.mpf, z: mp.mpf):
    """Exact recursive Ocneanu Markov trace on the `S_n` Kazhdan-Lusztig/T_w basis."""
    memo: dict[tuple[int, ...], mp.mpf] = {}
    one = mp.mpf(1)

    def tr_basis(w: tuple[int, ...]) -> mp.mpf:
        n = len(w)
        if n <= 1:
            return one
        if w in memo:
            return memo[w]
        if w[-1] == n - 1:
            val = tr_basis(w[:-1])
        else:
            rw = _reduced_word(w)
            # In S_n, any coset representative w with w(n-1) < n-1 has a reduced
            # word containing s_{n-2} = n-2 at most once (ascending tail coset).
            # Build via coset decomposition w = u * s_{n-2} * s_{n-3} ... s_k
            # where k = w.index(n - 1), u in S_{n-1}.
            k = w.index(n - 1)
            # Right-multiply w by s_k * s_{k+1} * ... * s_{n-2} to move n-1 to the end:
            u = w
            for j in range(k, n - 1):
                u = _swap(u, j)
            # Then T_w = T_u * T_{s_{n-2}} * T_{s_{n-3}} * ... * T_{s_k} since lengths add!
            # By Markov + trace cyclicity on H_{n-1}:
            # tr_n(T_u * T_{n-2} * R) = z * tr_{n-1}(R * T_u) where u, R in H_{n-1}.
            u_sub = u[:-1]
            elem: dict[tuple[int, ...], mp.mpf] = {tuple(range(n - 1)): one}
            for j in range(n - 2 - 1, k - 1, -1):
                elem = _rmul_gen(elem, j, h)
            for gen_i in _reduced_word(u_sub):
                elem = _rmul_gen(elem, gen_i, h)
            val = z * sum(c * tr_basis(v) for v, c in elem.items())
        memo[w] = val
        return val

    def tr_elem(x: dict[tuple[int, ...], mp.mpf]) -> mp.mpf:
        return sum(c * tr_basis(w) for w, c in x.items())

    return tr_elem


def _h3_delta_metrics_sym():
    """Exact symbolic `Q(q, z)` analysis of all six `Delta = NF(n) - NF(p)` models."""
    q, z = sp.symbols("q z")
    h = q - sp.Integer(1) / q

    # H_3 basis indexed by S_3 permutations
    id3 = (0, 1, 2)
    s0 = (1, 0, 2)
    s1 = (0, 2, 1)
    s01 = (1, 2, 0)
    s10 = (2, 0, 1)
    s010 = (2, 1, 0)
    basis = (id3, s0, s1, s01, s10, s010)

    def rmul_sym(x: dict[tuple[int, ...], sp.Expr], g: int, d: sp.Expr) -> dict[tuple[int, ...], sp.Expr]:
        out: dict[tuple[int, ...], sp.Expr] = {}
        for w, c in x.items():
            ws = _swap(w, g)
            if _inv_count(ws) > _inv_count(w):
                out[ws] = out.get(ws, sp.Integer(0)) + c
            else:
                out[w] = out.get(w, sp.Integer(0)) + h * c
                out[ws] = out.get(ws, sp.Integer(0)) + c
            if d != 0:
                out[w] = out.get(w, sp.Integer(0)) + d * c
        return {k: sp.expand(v) for k, v in out.items() if sp.simplify(v) != 0}

    def eval_word(letters: list[tuple[int, sp.Expr]]) -> dict[tuple[int, ...], sp.Expr]:
        x: dict[tuple[int, ...], sp.Expr] = {id3: sp.Integer(1)}
        for g, d in letters:
            x = rmul_sym(x, g, d)
        return x

    def diff_nf(
        wn: dict[tuple[int, ...], sp.Expr], wp: dict[tuple[int, ...], sp.Expr]
    ) -> dict[tuple[int, ...], sp.Expr]:
        return {
            b: sp.simplify(wn.get(b, sp.Integer(0)) - wp.get(b, sp.Integer(0)))
            for b in basis
        }

    tr_weights = {
        id3: sp.Integer(1),
        s0: z,
        s1: z,
        s01: z ** 2,
        s10: z ** 2,
        s010: z * (h * z + sp.Integer(1)),
    }
    # Irreducible character chi_{(2,1)} on H_3(q):
    # chi(1)=2, chi(T_0)=chi(T_1)=h, chi(T_0 T_1)=chi(T_1 T_0)=-1, chi(T_0 T_1 T_0)=0.
    chi21_weights = {
        id3: sp.Integer(2),
        s0: h,
        s1: h,
        s01: sp.Integer(-1),
        s10: sp.Integer(-1),
        s010: sp.Integer(0),
    }

    def net_sym(dvec: dict[tuple[int, ...], sp.Expr]) -> sp.Expr:
        return sp.simplify(sum(dvec.values()))

    def tr_sym(dvec: dict[tuple[int, ...], sp.Expr]) -> sp.Expr:
        return sp.expand(sum(dvec[b] * tr_weights[b] for b in basis))

    def chi21_sym(dvec: dict[tuple[int, ...], sp.Expr]) -> sp.Expr:
        return sp.simplify(sum(dvec[b] * chi21_weights[b] for b in basis))

    d_map = {
        ("u", "u"): sp.Integer(0),
        ("d", "d"): -h,
        ("u", "d"): -h / sp.Integer(2),
        ("d", "u"): -h / sp.Integer(2),
    }

    def quark_letters(quarks: tuple[str, str, str]) -> list[tuple[int, sp.Expr]]:
        return [
            (0, d_map[(quarks[0], quarks[1])]),
            (0, d_map[(quarks[0], quarks[2])]),
            (1, d_map[(quarks[1], quarks[2])]),
        ]

    v3_letters = [(0, sp.Integer(0)), (1, -h)] * 3

    # M1: Delta_S — short 1-/2-crossing model:
    # proton single ud crossing (sigma_0 - h/2) vs neutron (sigma_0 - h/2)(sigma_1 - h)
    # Wait: verify exact short model `net = h^2/2 - h`, `tr_M = h^2/2 - h*z`, `chi_21 = 0`:
    # In H_3, p_S = (sigma_0 - h/2)*(sigma_1), n_S = (sigma_0 - h/2)*(sigma_1 - h) ->
    # n_S - p_S = -h * (sigma_0 - h/2) = -h * sigma_0 + h^2 / 2!
    # Check: net(-h*sigma_0 + h^2/2) = h^2/2 - h; tr_M = h^2/2 - h*z;
    # Wait: chi_21(-h*sigma_0 + h^2/2) = -h^2 + h^2 = 0 IDENTICALLY!!
    p_short = eval_word([(0, -h / sp.Integer(2)), (1, sp.Integer(0))])
    n_short = eval_word([(0, -h / sp.Integer(2)), (1, -h)])
    m1_delta = diff_nf(n_short, p_short)

    # M2: nuc9_interleaved — V^3 * quark_pairs (9 crossings)
    p_nuc9 = eval_word(v3_letters + quark_letters(("u", "u", "d")))
    n_nuc9 = eval_word(v3_letters + quark_letters(("u", "d", "d")))
    m2_delta = diff_nf(n_nuc9, p_nuc9)

    # M3: nuc11_interleaved — V^3 * quark_pairs * sigma_0^2 (11 crossings, build_nucleon_nf_mp)
    gluon_s0_sq = [(0, sp.Integer(0)), (0, sp.Integer(0))]
    p_nuc11_int = eval_word(v3_letters + quark_letters(("u", "u", "d")) + gluon_s0_sq)
    n_nuc11_int = eval_word(v3_letters + quark_letters(("u", "d", "d")) + gluon_s0_sq)
    m3_delta = diff_nf(n_nuc11_int, p_nuc11_int)

    # M4: nuc11_grouped — all g_0 letters then all g_1 letters (nucleon_gen_chains)
    def grouped_letters(quarks: tuple[str, str, str]) -> list[tuple[int, sp.Expr]]:
        ql = quark_letters(quarks)
        g0 = [(0, sp.Integer(0))] * 3 + [x for x in ql if x[0] == 0] + gluon_s0_sq
        g1 = [(1, -h)] * 3 + [x for x in ql if x[0] == 1]
        return g0 + g1

    p_nuc11_grp = eval_word(grouped_letters(("u", "u", "d")))
    n_nuc11_grp = eval_word(grouped_letters(("u", "d", "d")))
    m4_delta = diff_nf(n_nuc11_grp, p_nuc11_grp)

    # M5: categorical_Lminus — V^3 * quark_pairs * (sigma_1 * sigma_0) (11 crossings)
    gluon_lminus = [(1, sp.Integer(0)), (0, sp.Integer(0))]
    p_cat_lm = eval_word(v3_letters + quark_letters(("u", "u", "d")) + gluon_lminus)
    n_cat_lm = eval_word(v3_letters + quark_letters(("u", "d", "d")) + gluon_lminus)
    m5_delta = diff_nf(n_cat_lm, p_cat_lm)

    # M6: gg_V3_canonical — 2026-11-20..22 ruled V^3 = (sigma_0 sigma_1^-1)^3 for both p and n
    p_v3 = eval_word(v3_letters)
    n_v3 = eval_word(v3_letters)
    m6_delta = diff_nf(n_v3, p_v3)

    models = [
        ("M1_Delta_S_short_1_2_crossings", 2, "short_factorized", m1_delta, "unscored_history_cell"),
        ("M2_nuc9_interleaved_pre_1qsw", 9, "interleaved", m2_delta, "retired_pre_2026_08_30"),
        ("M3_nuc11_interleaved_build_nucleon_nf_mp", 11, "interleaved", m3_delta, "unscored_history_gluon_open"),
        ("M4_nuc11_grouped_nucleon_gen_chains", 11, "gen_grouped", m4_delta, "legacy_marshalled_frame"),
        ("M5_categorical_Lminus_11_crossings", 11, "interleaved_Lminus", m5_delta, "excluded_scope_b_Lpm_retired"),
        ("M6_gg_V3_ruled_canonical_core", 6, "borromean_V3", m6_delta, "canonical_2026_11_20_bare_word_zero_split_on_T3"),
    ]

    out = []
    for name, n_cross, order_kind, dvec, status in models:
        net_e = net_sym(dvec)
        tr_e = tr_sym(dvec)
        poly_z = sp.Poly(tr_e, z)
        z2_coeff = sp.simplify(poly_z.nth(2))
        chi21_e = chi21_sym(dvec)
        out.append((name, n_cross, order_kind, status, net_e, tr_e, z2_coeff, chi21_e))
    return q, z, h, out


def main() -> int:
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        q0 = mp.mpf(q_at(WORK_DPS))
        h0 = q0 - one / q0
        z_d = (q0 ** 3) / (q0 ** 2 + one)

        # ── Part A: Symbolic & 80-dps verification of qou-jwl8 ───────────────
        qs, zs, as_, bs, cs = sp.symbols("q z a b c")
        hs = qs - sp.Integer(1) / qs
        tr_h2_ab = (as_ + bs + hs) * zs + (sp.Integer(1) + as_ * bs)
        tr_h2_ac = (as_ + cs + hs) * zs + (sp.Integer(1) + as_ * cs)
        tr_p3 = tr_h2_ab * (zs + cs)
        tr_d3 = (zs + bs) * tr_h2_ac
        sym_a3_err = sp.simplify(
            (tr_p3 - tr_d3) - (bs - cs) * (zs ** 2 - hs * zs - sp.Integer(1))
        )

        zd_s = qs ** 3 / (qs ** 2 + sp.Integer(1))
        sym_quad_zd_err = sp.simplify(
            (zd_s ** 2 - hs * zd_s - sp.Integer(1))
            + (qs ** 4 + qs ** 2 + sp.Integer(1)) / (qs ** 2 + sp.Integer(1)) ** 2
        )

        tr_p4_unif = ((hs ** 2 + sp.Integer(1)) * zs + hs) * (hs * zs + sp.Integer(1)) * zs
        tr_d4_unif = (zs ** 2) * ((hs ** 3 + sp.Integer(2) * hs) * zs + hs ** 2 + sp.Integer(1))
        sym_a4_unif_err = sp.simplify(
            (tr_p4_unif - tr_d4_unif) + hs * zs * (zs ** 2 - hs * zs - sp.Integer(1))
        )

        tracer = _make_markov_tracer(h0, z_d)

        def pair_shift(t1: int, t2: int) -> mp.mpf:
            if t1 == 1 and t2 == 1:
                return mp.mpf(0)
            if t1 == 0 and t2 == 0:
                return -h0
            return -h0 / two

        def eval_traced_volume_product(ordering: tuple[int, ...]) -> mp.mpf:
            prod = one
            n_strands = len(ordering)
            for i in range(n_strands - 1):
                a_acc, b_acc = mp.mpf(0), one
                for j in range(i + 1, n_strands):
                    d_ij = pair_shift(ordering[i], ordering[j])
                    a_acc, b_acc = a_acc * (h0 + d_ij) + b_acc, a_acc + b_acc * d_ij
                prod *= z_d * a_acc + b_acc
            return prod

        def eval_half_twist_trace(ordering: tuple[int, ...]) -> mp.mpf:
            n_strands = len(ordering)
            elem: dict[tuple[int, ...], mp.mpf] = {tuple(range(n_strands)): one}
            pos = list(range(n_strands))
            word_gens = [i for k in range(1, n_strands) for i in range(k - 1, -1, -1)]
            for i in word_gens:
                s_left, s_right = pos[i], pos[i + 1]
                d_val = pair_shift(ordering[s_left], ordering[s_right])
                elem = _rmul_shifted(elem, i, d_val, h0)
                pos[i], pos[i + 1] = s_right, s_left
            return tracer(elem)

        blast_summary: dict[str, dict[str, object]] = {}
        tol_zero = mp.mpf("1e-75")
        a3_iff_holds = True
        for a_num in (3, 4, 5):
            n_tot = 0
            n_diff = 0
            max_dlog = mp.mpf(0)
            agreeing_orders: list[str] = []
            for o in itertools.product((1, 0), repeat=a_num):
                n_tot += 1
                p_val = eval_traced_volume_product(o)
                b_val = eval_half_twist_trace(o)
                dlog = abs(mp.log(abs(p_val)) - mp.log(abs(b_val)))
                if dlog > tol_zero:
                    n_diff += 1
                else:
                    agreeing_orders.append("".join(str(bit) for bit in o))
                if a_num == 3:
                    expected_eq = o[0] == o[1]
                    if (dlog <= tol_zero) != expected_eq:
                        a3_iff_holds = False
                if dlog > max_dlog:
                    max_dlog = dlog
            blast_summary[f"A={a_num}"] = {
                "total_orderings": n_tot,
                "differing_orderings": n_diff,
                "agreeing_orderings": agreeing_orders,
                "max_abs_delta_log": fmt(max_dlog, dps=30),
            }

        # Direct numeric cross-check against Lean closed-form formulas:
        quad_factor_zd = z_d ** 2 - h0 * z_d - one
        quad_closed_zd = -(q0 ** 4 + q0 ** 2 + one) / ((q0 ** 2 + one) ** 2)
        quad_zd_diff = abs(quad_factor_zd - quad_closed_zd)

        p3_udd = eval_traced_volume_product((1, 0, 0))
        d3_udd = eval_half_twist_trace((1, 0, 0))
        lean_a3_udd_diff = abs((p3_udd - d3_udd) - ((-h0 / two) - (-h0)) * quad_factor_zd)

        p4_pppp = eval_traced_volume_product((1, 1, 1, 1))
        d4_pppp = eval_half_twist_trace((1, 1, 1, 1))
        lean_a4_unif_diff = abs((p4_pppp - d4_pppp) - (-h0 * z_d * quad_factor_zd))

        # ── Part B: 80-dps inventory & pyhecke cross-check for qou-bg3w ──────
        import pyhecke.atom as py_atom
        import pyhecke.gram as py_gram

        q_sym, z_sym, _h_sym, sym_models = _h3_delta_metrics_sym()
        q_frac_111 = mp.mpf(111) / mp.mpf(100)

        delta_inventory: list[dict[str, object]] = []
        d1_affine_models: list[str] = []
        m1_chi21_exact_zero = False
        m3_net_q0 = mp.mpf(0)
        m4_net_q0 = mp.mpf(0)
        m2_pin_shift = mp.mpf(0)

        for name, n_cross, order_kind, status, net_e, tr_e, z2_coeff, chi21_e in sym_models:
            f_net = sp.lambdify(q_sym, net_e, "mpmath")
            f_tr = sp.lambdify((q_sym, z_sym), tr_e, "mpmath")
            f_z2 = sp.lambdify(q_sym, z2_coeff, "mpmath")
            f_chi21 = sp.lambdify(q_sym, chi21_e, "mpmath")

            net_q0 = mp.mpf(f_net(q0))
            net_111 = mp.mpf(f_net(q_frac_111))
            tr_zd_q0 = mp.mpf(f_tr(q0, z_d))
            z2_q0 = mp.mpf(f_z2(q0))
            chi21_q0 = mp.mpf(f_chi21(q0))

            is_d1_affine = sp.simplify(z2_coeff) == 0
            if is_d1_affine:
                d1_affine_models.append(name)
            if name.startswith("M1_"):
                m1_chi21_exact_zero = sp.simplify(chi21_e) == 0
            if name.startswith("M2_"):
                m2_pin_shift = abs(net_q0 - net_111)
            if name.startswith("M3_"):
                m3_net_q0 = net_q0
            if name.startswith("M4_"):
                m4_net_q0 = net_q0

            delta_inventory.append(
                {
                    "model": name,
                    "crossings": n_cross,
                    "intra_order": order_kind,
                    "post_2026_11_22_status": status,
                    "net_at_proton_q0": fmt(net_q0, dps=OUT_DPS),
                    "net_at_q_111_100": fmt(net_111, dps=30),
                    "tr_D_at_proton_q0": fmt(tr_zd_q0, dps=OUT_DPS),
                    "chi_21_at_proton_q0": fmt(chi21_q0, dps=30),
                    "tr_z_quad_coeff_at_q0": fmt(z2_q0, dps=30),
                    "d1_affine_in_z": is_d1_affine,
                }
            )

        # Cross-check M3 & M4 directly against live `pyhecke.atom` at 80 dps.
        # `pyhecke.gram.hm_mp` reduces `T_g^2 = h T_g + 1` using `h_py = pyhecke.gram.h_mp(dps)`
        # (from the 50-digit `HA_50_DIGIT_STR`). At `q_py = (h_py + sqrt(h_py^2 + 4))/2`,
        # `q_py - q_py^-1 = h_py` to 80 dps, so both M3 and M4 agree to `< 1e-75`, while
        # `h_py` vs `h0 = q_at(80) - 1/q_at(80)` measures the 50-digit string boundary (`~4.4e-50`).
        h_py = py_gram.h_mp(WORK_DPS)
        q_py = (h_py + mp.sqrt(h_py ** 2 + mp.mpf(4))) / two
        m3_sym_expr = [row[4] for row in sym_models if row[0].startswith("M3_")][0]
        m4_sym_expr = [row[4] for row in sym_models if row[0].startswith("M4_")][0]
        m3_net_at_qpy = mp.mpf(sp.lambdify(q_sym, m3_sym_expr, "mpmath")(q_py))
        m4_net_at_qpy = mp.mpf(sp.lambdify(q_sym, m4_sym_expr, "mpmath")(q_py))

        nf_p_mp = py_atom.build_nucleon_nf_mp(["u", "u", "d"], dps=WORK_DPS)
        nf_n_mp = py_atom.build_nucleon_nf_mp(["u", "d", "d"], dps=WORK_DPS)
        pyhecke_m3_net = sum(nf_n_mp) - sum(nf_p_mp)
        m3_pyhecke_exact_diff = abs(pyhecke_m3_net - m3_net_at_qpy)
        m3_q50_vs_q80_diff = abs(pyhecke_m3_net - m3_net_q0)

        g0_p, g1_p = py_atom.nucleon_gen_chains(["u", "u", "d"], q=q_py)
        g0_n, g1_n = py_atom.nucleon_gen_chains(["u", "d", "d"], q=q_py)
        n_chains_p = len(g0_p) + len(g1_p)
        n_braid_word_p = len(py_atom.nucleon_braid_word(["u", "u", "d"], dps=WORK_DPS))

        def eval_grouped_pyhecke(g0_list, g1_list) -> list[mp.mpf]:
            nf_vec = [one] + [mp.mpf(0)] * 5
            for c_val, d_val, gen_idx in py_atom.grouped_word_from_chains(g0_list, g1_list):
                nf_vec = py_gram.hm_mp(nf_vec, mp.mpf(c_val), mp.mpf(d_val), gen_idx, WORK_DPS)
            return nf_vec

        nf_p_grp = eval_grouped_pyhecke(g0_p, g1_p)
        nf_n_grp = eval_grouped_pyhecke(g0_n, g1_n)
        pyhecke_m4_net = sum(nf_n_grp) - sum(nf_p_grp)
        m4_pyhecke_diff = abs(pyhecke_m4_net - m4_net_at_qpy)
        m3_vs_m4_gap = abs(m3_net_q0 - m4_net_q0)

        # ── Build Witness JSON ───────────────────────────────────────────────
        wb = WitnessBuilder(
            "traced-volume-and-delta-models-audit",
            engine="mpmath-80dps",
            output_dir=pathlib.Path(__file__).resolve().parent,
        )
        wb.set_description(
            "80-dps diagnostic & symbolic verification for beans qou-jwl8 "
            "(QOU/BraidsAndKnots/TracedVolumeVsHalfTwist.lean: traced_volume "
            "product P_A vs strand-tracked half-twist Delta_A across A=3,4,5) "
            "and qou-bg3w (complete 6-model nucleon-word Delta = NF(n) - NF(p) "
            "inventory at proton q_0 vs q=111/100 and live pyhecke.atom builders)."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("q0_proton", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("z_D_proton", fmt(z_d, dps=OUT_DPS))

        wb.add_data(
            "part_a_traced_volume_vs_half_twist",
            {
                "hecke_quad_factor_at_zD": fmt(quad_factor_zd, dps=OUT_DPS),
                "a3_udd_product_minus_halftwist": fmt(p3_udd - d3_udd, dps=OUT_DPS),
                "a4_uniform_product_trace": fmt(p4_pppp, dps=OUT_DPS),
                "a4_uniform_halftwist_trace": fmt(d4_pppp, dps=OUT_DPS),
                "a4_uniform_product_minus_halftwist": fmt(p4_pppp - d4_pppp, dps=OUT_DPS),
                "blast_radius_by_A": blast_summary,
            },
        )
        wb.add_data(
            "part_b_delta_nucleon_word_inventory",
            {
                "pyhecke_nucleon_braid_word_len": n_braid_word_p,
                "pyhecke_nucleon_gen_chains_len": n_chains_p,
                "m3_vs_m4_ordering_net_gap": fmt(m3_vs_m4_gap, dps=30),
                "m2_nuc9_q0_vs_111_100_pin_gap": fmt(m2_pin_shift, dps=30),
                "d1_affine_models": d1_affine_models,
                "models": delta_inventory,
            },
        )

        wb.add_assertion(
            "sym_a3_product_minus_halftwist_identity",
            int(sym_a3_err == 0),
            1,
            "0",
            source="TracedVolumeVsHalfTwist.trTracedVolumeA3_sub_trHalfTwistA3",
        )
        wb.add_assertion(
            "sym_quad_factor_at_zD_identity",
            int(sym_quad_zd_err == 0),
            1,
            "0",
            source="TracedVolumeVsHalfTwist.heckeQuadFactor_at_zD",
        )
        wb.add_assertion(
            "sym_a4_uniform_product_minus_halftwist_identity",
            int(sym_a4_unif_err == 0),
            1,
            "0",
            source="TracedVolumeVsHalfTwist.trTracedVolumeA4Uniform_sub_trHalfTwistA4Uniform",
        )
        wb.add_assertion(
            "a3_agreement_iff_o0_eq_o1_all_8_orderings",
            int(a3_iff_holds and blast_summary["A=3"]["differing_orderings"] == 4),
            1,
            "0",
            source="TracedVolumeVsHalfTwist.trTracedVolumeA3_eq_trHalfTwistA3_at_zD_iff",
        )
        wb.add_assertion(
            "a4_14_of_16_and_a5_32_of_32_orderings_differ",
            int(
                blast_summary["A=4"]["differing_orderings"] == 14
                and blast_summary["A=5"]["differing_orderings"] == 32
            ),
            1,
            "0",
            source="qou-jwl8 blast-radius enumeration A=4,5 at 80 dps",
        )
        wb.add_assertion(
            "lean_closed_forms_match_80dps_traces",
            fmt(max(quad_zd_diff, lean_a3_udd_diff, lean_a4_unif_diff), dps=15),
            "0",
            "1e-75",
            source="TracedVolumeVsHalfTwist.{heckeQuadFactor_at_zD, trTracedVolumeA4Uniform_sub_trHalfTwistA4Uniform}",
        )
        wb.add_assertion(
            "delta_S_chi21_vanishes_and_d1_affine_unique",
            int(
                m1_chi21_exact_zero
                and d1_affine_models
                == ["M1_Delta_S_short_1_2_crossings", "M6_gg_V3_ruled_canonical_core"]
            ),
            1,
            "0",
            source="qou-bg3w: chi_(2,1)(Delta_S)=0 and z^2 coeff nonzero on all 9-/11-crossing models",
        )
        wb.add_assertion(
            "pyhecke_interleaved_and_grouped_both_11_crossings_match_symbolic",
            fmt(max(m3_pyhecke_exact_diff, m4_pyhecke_diff), dps=15),
            "0",
            "1e-75",
            source="pyhecke.atom.{build_nucleon_nf_mp@Q50, grouped_word_from_chains@q0} == M3, M4 to 80 dps",
        )
        wb.add_assertion(
            "pyhecke_m3_q50_matches_80dps_q0_to_50str_precision",
            fmt(m3_q50_vs_q80_diff, dps=15),
            "0",
            "1e-48",
            source="build_nucleon_nf_mp (Q_50_DIGIT_STR) vs M3(q_at(80)) 50-digit string boundary",
        )
        wb.add_assertion(
            "pyhecke_both_builders_have_11_crossings_post_1qsw_and_differ_by_ordering",
            int(n_braid_word_p == 11 and n_chains_p == 11 and m3_vs_m4_gap > mp.mpf("0.006")),
            1,
            "0",
            source="qou-bg3w: post-qou-1qsw both builders emit 11 crossings; gap 0.006038 is intra-order",
        )

        wb.add_caveat(
            "1. Scope (a) definitional & naming audit only: selects neither P_A nor Delta_A as "
            "the nuclear operator (an open owner question on qou-jwl8, alongside the 2026-11-21 "
            "rulings superseding single-crossing interface letters in favour of ruled gamma-gamma "
            "bonds). "
            "2. On qou-bg3w, post-2026-11-20..22 owner rulings fix the scored Q_beta base to the "
            "gamma-gamma V^3 T_3 weight-space split (0.3254 MeV), relax R3 p-n colour weighting to "
            "a working conjecture, and keep step-4 gluon choices open; Models M1-M5 remain "
            "documented historical/comparison cells."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"A=3 differing: {blast_summary['A=3']['differing_orderings']}/8")
        print(f"A=4 differing: {blast_summary['A=4']['differing_orderings']}/16")
        print(f"A=5 differing: {blast_summary['A=5']['differing_orderings']}/32")
        print(f"M3 (build_nucleon_nf_mp) net(Delta) = {fmt(m3_net_q0, dps=20)}")
        print(f"M4 (nucleon_gen_chains)  net(Delta) = {fmt(m4_net_q0, dps=20)}")
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
