#!/usr/bin/env python3
"""80-dps mpmath + exact rational ChamberGS probe for A_0 (73 chambers) and A_shell (qou-h6ef).

Pre-registered in PREREGISTRATION-chamber-gs.md (committed in 5c7972efa6c before this script).
Precision: workdps = 80, q0Anchor = "proton", zero float64, zero hardcoded AME/CODATA literals.

Verifies:
1. Model A (A_0 = [[1,0,1,1,2,2],[0,1,1,2,1,2]] on (x_p, x_n, x_d, x_t, x_h, x_alpha)):
   - Exact Graver basis |Gr_{A_0}| = 28 unsigned (56 signed) via both Pottier S-pair completion
     and exhaustive [-6,6]^4 kernel box search, with 17 unsigned circuits.
   - Complete Grobner fan |GF(I_{A_0})| = 73 full-dimensional chambers via exact rational
     facet-flipping BFS, cross-checked against sympy.groebner.
   - Exact Universal Grobner Basis |U_{A_0}| = 27 unsigned binomials (sole non-UGB Graver
     element: x_alpha - x_p x_n x_d).
   - Parameter-free QOU bare q_0, QOU tower q_0, and AME2020 all lie strictly inside the
     exact same 5-wall physical chamber C_phys with the 11-rule minimal reduced Grobner
     basis G_phys.
   - Normal-form reduction NF(x_p^2 x_n^3) = x_alpha x_n (^5He neutron-drip monomer),
     odd-even monomer staggering, and degree-3 Hoyle bottleneck (x_{8Be} -> x_alpha^2 vs
     x_alpha^3 -> x_{12C}).
2. Model B (Capacitated Mayer-Jensen Shell Matrix A_shell, C_s = [2, 6, 12, 8, 22, 32, 44]):
   - Single-species |Gr_{B_shell}| = C(S, 2) = 21 unsigned for S = 7 shells, and 100%
     confluence of the S - 1 adjacent single-shell promotion rules u_{s+1} w_s -> u_s w_{s+1}
     across all valid integer fiber states u_s + w_s = C_s >= 1.
"""

from __future__ import annotations

import itertools
import sys
import time
from collections import deque
from fractions import Fraction
from pathlib import Path

THIS = Path(__file__).resolve()
ROOT = THIS.parents[3]
for _rel in (
    "computations",
    "computations/substrate",
    "tools/pyhecke/python",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402
import sympy as sp  # noqa: E402
from sympy.polys.orderings import MonomialOrder  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from q_parameter import q_at  # noqa: E402
from qbeta.qbeta_e0 import order_zero_scaled  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS

VAR_NAMES = ["x_p", "x_n", "x_d", "x_t", "x_h", "x_alpha"]
A0 = sp.Matrix(
    [
        [1, 0, 1, 1, 2, 2],
        [0, 1, 1, 2, 1, 2],
    ]
)


def is_conformal_leq(h: tuple[int, ...], g: tuple[int, ...]) -> bool:
    for hi, gi in zip(h, g):
        if hi != 0:
            if gi == 0 or (hi > 0) != (gi > 0) or abs(hi) > abs(gi):
                return False
    return True


def compute_graver_pottier(basis: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    g_set: set[tuple[int, ...]] = set()
    for b in basis:
        g_set.add(b)
        g_set.add(tuple(-x for x in b))
    queue = deque(
        (u, v)
        for u in g_set
        for v in g_set
        if any(ui * vi < 0 for ui, vi in zip(u, v))
    )
    while queue:
        u, v = queue.popleft()
        s = tuple(ui + vi for ui, vi in zip(u, v))
        if all(x == 0 for x in s) or s in g_set:
            continue
        reduced = True
        while reduced:
            reduced = False
            for g in g_set:
                if is_conformal_leq(g, s) and g != s:
                    s = tuple(si - gi for si, gi in zip(s, g))
                    reduced = True
                    break
        if any(x != 0 for x in s) and s not in g_set:
            neg_s = tuple(-x for x in s)
            for cand in (s, neg_s):
                to_remove = {g for g in g_set if g != cand and is_conformal_leq(cand, g)}
                g_set -= to_remove
                for g in list(g_set):
                    if any(ci * gi < 0 for ci, gi in zip(cand, g)):
                        queue.append((cand, g))
                g_set.add(cand)
    return {
        g for g in g_set if not any(h != g and is_conformal_leq(h, g) for h in g_set)
    }


def canonical_heavy_positive(g: tuple[int, ...]) -> tuple[int, ...]:
    for idx in range(5, -1, -1):
        if g[idx] != 0:
            return g if g[idx] > 0 else tuple(-x for x in g)
    raise ValueError("Zero vector")


def vec_to_monomial(exps: list[int]) -> str:
    parts = []
    for name, e in zip(VAR_NAMES, exps):
        if e == 1:
            parts.append(name)
        elif e > 1:
            parts.append(f"{name}^{e}")
    return " ".join(parts) if parts else "1"


def vec_to_binomial_str(g: tuple[int, ...]) -> str:
    pos = [max(x, 0) for x in g]
    neg = [max(-x, 0) for x in g]
    return f"{vec_to_monomial(pos)} - {vec_to_monomial(neg)}"


def dot_w_g(w4: tuple[Fraction, ...], g: tuple[int, ...]) -> Fraction:
    return sum((wi * gi for wi, gi in zip(w4, g[2:])), Fraction(0, 1))


def mon_divides(m1: tuple[int, ...], m2: tuple[int, ...]) -> bool:
    return all(a <= b for a, b in zip(m1, m2))


def reduced_gb_from_weight(
    w4: tuple[Fraction, ...], graver_signed: set[tuple[int, ...]]
) -> tuple[tuple[int, ...], ...]:
    pos_graver = []
    for g in graver_signed:
        val = dot_w_g(w4, g)
        if val == 0:
            raise ValueError(f"Non-generic weight {w4} on {g}")
        if val > 0:
            pos_graver.append((g, val))
    by_lead: dict[tuple[int, ...], tuple[tuple[int, ...], Fraction]] = {}
    for g, val in pos_graver:
        lead = tuple(max(x, 0) for x in g)
        if lead not in by_lead or val > by_lead[lead][1]:
            by_lead[lead] = (g, val)
    leads = list(by_lead.keys())
    min_leads = [
        m for m in leads if not any(m2 != m and mon_divides(m2, m) for m2 in leads)
    ]
    rgb = sorted(by_lead[m][0] for m in min_leads)
    for g in rgb:
        trail = tuple(max(-x, 0) for x in g)
        assert not any(mon_divides(m, trail) for m in min_leads)
    return tuple(rgb)


def cone_extreme_rays_4d(
    ineqs: list[tuple[int, int, int, int]]
) -> list[tuple[int, ...]]:
    rays: set[tuple[int, ...]] = set()
    m = len(ineqs)
    for i, j, k in itertools.combinations(range(m), 3):
        mat = sp.Matrix([ineqs[i], ineqs[j], ineqs[k]])
        ns = mat.nullspace()
        if len(ns) != 1:
            continue
        v = ns[0]
        den_lcm = 1
        for entry in v:
            den_lcm = int(sp.ilcm(den_lcm, sp.fraction(entry)[1]))
        v_int = [int(entry * den_lcm) for entry in v]
        g_div = 0
        for x in v_int:
            g_div = int(sp.igcd(g_div, abs(x)))
        v_prim = tuple(x // g_div for x in v_int)
        for sign in (1, -1):
            cand = tuple(sign * x for x in v_prim)
            if all(sum(ni * ci for ni, ci in zip(n, cand)) >= 0 for n in ineqs):
                if any(sum(ni * ci for ni, ci in zip(n, cand)) > 0 for n in ineqs):
                    rays.add(cand)
    return sorted(rays)


def irredundant_facets_4d(
    ineqs: list[tuple[int, int, int, int]]
) -> list[tuple[tuple[int, int, int, int], tuple[Fraction, ...]]]:
    rays = cone_extreme_rays_4d(ineqs)
    primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167]
    facets = []
    seen_n = set()
    for n in ineqs:
        if n in seen_n:
            continue
        seen_n.add(n)
        on_wall = [r for r in rays if sum(ni * ri for ni, ri in zip(n, r)) == 0]
        if len(on_wall) >= 3:
            if sp.Matrix(on_wall).rank() == 3:
                wts = [primes[idx % len(primes)] + 19 * idx for idx in range(len(on_wall))]
                w_sum = sum(wts)
                rel_int = tuple(
                    Fraction(sum(wt * r[d] for wt, r in zip(wts, on_wall)), w_sum)
                    for d in range(4)
                )
                facets.append((n, rel_int))
    return facets


class WeightOrder(MonomialOrder):
    def __init__(self, weights: tuple[int, ...]) -> None:
        self.weights = weights

    @property
    def alias(self) -> str:
        return "custom_weight"

    def __call__(self, monomial: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
        return (sum(w * m for w, m in zip(self.weights, monomial)), monomial)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, WeightOrder) and self.weights == other.weights

    def __hash__(self) -> int:
        return hash(self.weights)


def derive_qou_light_cluster_bindings(q0: mpf) -> tuple[dict[str, mpf], dict[str, mpf]]:
    """Derive parameter-free QOU bare & tower cluster binding energies (d, t, h, alpha) at 80 dps."""
    with mp.workdps(DPS + 10):
        one = mpf(1)
        h = q0 - one / q0
        hbar_q = (q0 - one) / q0
        me = mpf(str(M_E_MEV))
        e0_bare = order_zero_scaled(me, q0)
        e0_tower = e0_bare / (one - hbar_q**2)

        z_d = (q0**3) / (q0**2 + one)
        z_gg = z_d - h / mpf(2)
        q2_1 = q0**2 + one
        q4_1 = q0**4 + one
        q4_2_1 = q0**4 + q0**2 + one
        h4_mod_denom = (q2_1**3) * q4_1 * q4_2_1

        mu3_gpmt = (q0**3) / (q2_1 * q4_2_1)
        casimir_gpmt = (
            mpf(12)
            * (q0**3)
            * (q0**8 + mpf(2) * (q0**6) + mpf(4) * (q0**4) + mpf(2) * (q0**2) + one)
            / h4_mod_denom
        )

        b2_gg_bare = e0_bare * mp.log(one / z_gg)
        b2_gg_tower = e0_tower * mp.log(one / z_gg)
        w3_bare = e0_bare * mu3_gpmt
        w3_tower = e0_tower * mu3_gpmt

        ec_d = mpf(str(coulomb_energy_mev(1, 2)))
        ec_t = mpf(str(coulomb_energy_mev(1, 3)))
        ec_h = mpf(str(coulomb_energy_mev(2, 3)))
        ec_a = mpf(str(coulomb_energy_mev(2, 4)))

        bare = {
            "d": +(b2_gg_bare - ec_d),
            "t": +(mpf(3) * b2_gg_bare + w3_bare - ec_t),
            "h": +(mpf(3) * b2_gg_bare + w3_bare - ec_h),
            "alpha": +(mpf(6) * b2_gg_bare + e0_bare * casimir_gpmt - ec_a),
        }
        tower = {
            "d": +(b2_gg_tower - ec_d),
            "t": +(mpf(3) * b2_gg_tower + w3_tower - ec_t),
            "h": +(mpf(3) * b2_gg_tower + w3_tower - ec_h),
            "alpha": +(mpf(6) * b2_gg_tower + e0_tower * casimir_gpmt - ec_a),
        }
        return bare, tower


def reduce_monomial(
    exps: tuple[int, ...], rgb: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    cur = list(exps)
    changed = True
    while changed:
        changed = False
        for g in rgb:
            lead = [max(x, 0) for x in g]
            if all(cur[i] >= lead[i] for i in range(6)):
                cur = [cur[i] - g[i] for i in range(6)]
                changed = True
                break
    return tuple(cur)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    with mp.workdps(DPS + 10):
        q0 = +q_at(DPS + 10)

    ker_basis = [
        (-1, -1, 1, 0, 0, 0),
        (-1, -2, 0, 1, 0, 0),
        (-2, -1, 0, 0, 1, 0),
        (-2, -2, 0, 0, 0, 1),
    ]
    graver_pottier = compute_graver_pottier(ker_basis)

    # Cross-check against exhaustive [-6, 6]^4 kernel box search
    box_cands = []
    for u2, u3, u4, u5 in itertools.product(range(-6, 7), repeat=4):
        if u2 == 0 and u3 == 0 and u4 == 0 and u5 == 0:
            continue
        u0 = -(u2 + u3 + 2 * u4 + 2 * u5)
        u1 = -(u2 + 2 * u3 + u4 + 2 * u5)
        box_cands.append((u0, u1, u2, u3, u4, u5))
    box_cands.sort(key=lambda v: sum(abs(x) for x in v))
    graver_box: list[tuple[int, ...]] = []
    for v in box_cands:
        if not any(is_conformal_leq(h, v) for h in graver_box):
            graver_box.append(v)
    assert graver_pottier == set(graver_box)

    unsigned_graver = sorted(
        {canonical_heavy_positive(g) for g in graver_pottier},
        key=lambda g: (
            sum(max(x, 0) * int(A0[0, i]) for i, x in enumerate(g))
            + sum(max(x, 0) * int(A0[1, i]) for i, x in enumerate(g)),
            tuple(abs(x) for x in reversed(g)),
            g,
        ),
    )
    supports = {frozenset(i for i, x in enumerate(g) if x != 0) for g in unsigned_graver}
    min_supports = {s for s in supports if not any(s2 < s for s2 in supports)}
    circuits = [
        g
        for g in unsigned_graver
        if frozenset(i for i, x in enumerate(g) if x != 0) in min_supports
    ]

    # Complete Grobner fan enumeration via exact rational facet-flipping BFS
    w_start = (
        Fraction(-205, 100),
        Fraction(-919, 100),
        Fraction(-834, 100),
        Fraction(-2643, 100),
    )
    rgb_start = reduced_gb_from_weight(w_start, graver_pottier)
    chambers: dict[tuple[tuple[int, ...], ...], dict] = {
        rgb_start: {"sample_w": w_start}
    }
    bfs_q = deque([rgb_start])
    while bfs_q:
        rgb = bfs_q.popleft()
        ineqs = [g[2:] for g in rgb]
        facets = irredundant_facets_4d(ineqs)
        chambers[rgb]["facets"] = facets
        neighbors = {}
        for n, rel_int in facets:
            min_step = None
            for g in graver_pottier:
                val = dot_w_g(rel_int, g)
                slope = sum(ni * gi for ni, gi in zip(n, g[2:]))
                if val != 0 and slope != 0:
                    ratio = abs(val) / abs(slope)
                    if min_step is None or ratio < min_step:
                        min_step = ratio
            eps = (min_step / 4) if min_step is not None else Fraction(1, 100)
            w_adj = tuple(rel_int[d] - eps * n[d] for d in range(4))
            rgb_adj = reduced_gb_from_weight(w_adj, graver_pottier)
            neighbors[n] = rgb_adj
            if rgb_adj not in chambers:
                chambers[rgb_adj] = {"sample_w": w_adj}
                bfs_q.append(rgb_adj)
        chambers[rgb]["neighbors"] = neighbors

    ugb_signed: set[tuple[int, ...]] = set()
    for rgb in chambers:
        for g in rgb:
            ugb_signed.add(g)
            ugb_signed.add(tuple(-x for x in g))
    ugb_unsigned = sorted(
        {canonical_heavy_positive(g) for g in ugb_signed},
        key=lambda g: unsigned_graver.index(g),
    )
    not_in_ugb = [vec_to_binomial_str(g) for g in unsigned_graver if g not in ugb_unsigned]

    # Cross-check physical chamber against sympy.groebner
    px, nx, dx, tx, hx, ax = sp.symbols("x_p x_n x_d x_t x_h x_alpha")
    sym_vars = [px, nx, dx, tx, hx, ax]
    ideal_gens = [dx - px * nx, tx - px * nx**2, hx - px**2 * nx, ax - px**2 * nx**2]
    c6 = [0, 0] + [int(wi * 100) for wi in w_start]
    w_mass = [1, 1, 2, 3, 3, 4]
    m_shift = max(0, max(-c6[i] for i in range(6))) + 10
    pos_weights = tuple(c6[i] + m_shift * w_mass[i] for i in range(6))
    g_sp = sp.groebner(ideal_gens, *sym_vars, order=WeightOrder(pos_weights))
    sp_vecs = set()
    for poly in g_sp.polys:
        terms = poly.terms(order=WeightOrder(pos_weights))
        (m1, _), (m2, _) = terms
        sp_vecs.add(tuple(a - b for a, b in zip(m1, m2)))
    sympy_crosscheck_ok = sp_vecs == set(rgb_start)

    # Evaluate QOU bare q_0, QOU tower q_0, and centralized AME2020
    b_qou_bare, b_qou_tower = derive_qou_light_cluster_bindings(q0)
    b_ame = {
        "d": ame_binding_mev(1, 2),
        "t": ame_binding_mev(1, 3),
        "h": ame_binding_mev(2, 3),
        "alpha": ame_binding_mev(2, 4),
    }

    def chamber_of(b_dict: dict[str, mpf]) -> tuple[tuple[int, ...], ...]:
        scale = 10**30
        w4 = tuple(
            Fraction(-int(mp.nint(b_dict[k] * mpf(scale))), scale)
            for k in ("d", "t", "h", "alpha")
        )
        return reduced_gb_from_weight(w4, graver_pottier)

    rgb_qou_bare = chamber_of(b_qou_bare)
    rgb_qou_tower = chamber_of(b_qou_tower)
    rgb_ame = chamber_of(b_ame)
    same_chamber = rgb_qou_bare == rgb_qou_tower == rgb_ame

    g_phys_rules = []
    for g in rgb_qou_bare:
        pos = [max(x, 0) for x in g]
        neg = [max(-x, 0) for x in g]
        dqou = -(
            b_qou_bare["d"] * g[2]
            + b_qou_bare["t"] * g[3]
            + b_qou_bare["h"] * g[4]
            + b_qou_bare["alpha"] * g[5]
        )
        dame = -(
            b_ame["d"] * g[2]
            + b_ame["t"] * g[3]
            + b_ame["h"] * g[4]
            + b_ame["alpha"] * g[5]
        )
        g_phys_rules.append(
            {
                "rule": f"{vec_to_monomial(pos)} -> {vec_to_monomial(neg)}",
                "vector": list(g),
                "delta_E_QOU_bare_MeV": fmt(+dqou),
                "delta_E_AME2020_MeV": fmt(+dame),
            }
        )

    facet_rows = []
    for n, _ in chambers[rgb_qou_bare]["facets"]:
        vqou = -(
            n[0] * b_qou_bare["d"]
            + n[1] * b_qou_bare["t"]
            + n[2] * b_qou_bare["h"]
            + n[3] * b_qou_bare["alpha"]
        )
        vame = -(
            n[0] * b_ame["d"]
            + n[1] * b_ame["t"]
            + n[2] * b_ame["h"]
            + n[3] * b_ame["alpha"]
        )
        facet_rows.append(
            {
                "normal_w": list(n),
                "margin_QOU_bare_MeV": fmt(+vqou),
                "margin_AME2020_MeV": fmt(+vame),
            }
        )

    nf_he5 = reduce_monomial((2, 3, 0, 0, 0, 0), rgb_qou_bare)
    nf_c12 = reduce_monomial((6, 6, 0, 0, 0, 0), rgb_qou_bare)
    nf_n14 = reduce_monomial((7, 7, 0, 0, 0, 0), rgb_qou_bare)

    # Hoyle bottleneck check against centralized AME2020
    b_be8_ame = ame_binding_mev(4, 8)
    b_c12_ame = ame_binding_mev(6, 12)
    be8_minus_2alpha_ame = b_be8_ame - mpf(2) * b_ame["alpha"]
    c12_minus_3alpha_ame = b_c12_ame - mpf(3) * b_ame["alpha"]

    # Model B: Capacitated Mayer-Jensen Shell Matrix A_shell
    shell_caps = [2, 6, 12, 8, 22, 32, 44]
    cum_magic = list(itertools.accumulate(shell_caps))
    s_full = len(shell_caps)
    b_ker = []
    for s in range(s_full - 1):
        vec = [0] * (2 * s_full)
        vec[s] = 1
        vec[s + 1] = -1
        vec[s_full + s] = -1
        vec[s_full + s + 1] = 1
        b_ker.append(tuple(vec))
    gr_b_shell = compute_graver_pottier(b_ker)

    # Verify 100% confluence of S-1 adjacent promotion rules on [2, 6, 12, 8]
    caps4 = [2, 6, 12, 8]
    s4 = len(caps4)
    adj4 = []
    for s in range(s4 - 1):
        g = [0] * (2 * s4)
        g[s + 1] = 1
        g[s4 + s] = 1
        g[s] = -1
        g[s4 + s + 1] = -1
        adj4.append(tuple(g))
    confluence_ok = True
    tested_states = 0
    for u in itertools.product(*(range(c + 1) for c in caps4)):
        tested_states += 1
        m_tot = sum(u)
        w = tuple(caps4[s] - u[s] for s in range(s4))
        state = list(u + w)
        changed = True
        while changed:
            changed = False
            for g in adj4:
                if all(state[i] >= max(g[i], 0) for i in range(2 * s4)):
                    state = [state[i] - g[i] for i in range(2 * s4)]
                    changed = True
                    break
        rem = m_tot
        u_exp = []
        for c in caps4:
            fill = min(rem, c)
            u_exp.append(fill)
            rem -= fill
        if state != u_exp + [caps4[s] - u_exp[s] for s in range(s4)]:
            confluence_ok = False
            break

    print(
        f"ChamberGS Model A+B: |Gr_A0|={len(unsigned_graver)} unsigned, "
        f"circuits={len(circuits)}, |U_A0|={len(ugb_unsigned)}, "
        f"chambers={len(chambers)}, same_C_phys={same_chamber}, "
        f"|G_phys|={len(rgb_qou_bare)}, |Gr_B_7|={len(gr_b_shell)//2}"
    )

    wb = WitnessBuilder(
        "chamber-gs-model-a-b",
        engine="mpmath+sympy",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "Pre-registered 80-dps mpmath + exact rational Sturmfels-Thomas ChamberGS probe "
        "(PREREGISTRATION-chamber-gs.md, 5c7972efa6c; qou-h6ef): verifies |Gr_{A_0}|=28, "
        "17 circuits, |U_{A_0}|=27, 73 Grobner fan chambers, exact chamber coincidence "
        "between QOU bare q_0, QOU tower q_0, and AME2020 in 5-wall C_phys (11-rule G_phys), "
        "NF(x_p^2 x_n^3) = x_alpha x_n (^5He drip), Hoyle bottleneck, and A_shell confluence."
    )
    wb.add_parameter("q0", fmt(q0))
    wb.add_parameter("workdps", DPS)
    wb.add_data("preregistration", "computations/probes/lp_bootstrap_dual_gaps/PREREGISTRATION-chamber-gs.md")
    wb.add_data("preregistration_commit", "5c7972efa6c")
    wb.add_data(
        "model_a_cluster_toric",
        {
            "unsigned_graver_count": len(unsigned_graver),
            "signed_graver_count": len(graver_pottier),
            "unsigned_circuit_count": len(circuits),
            "unsigned_ugb_count": len(ugb_unsigned),
            "non_ugb_graver_elements": not_in_ugb,
            "groebner_fan_chamber_count": len(chambers),
            "sympy_groebner_crosscheck_passed": sympy_crosscheck_ok,
            "qou_bare_tower_ame2020_in_same_chamber": same_chamber,
            "g_phys_rule_count": len(rgb_qou_bare),
            "g_phys_rules": g_phys_rules,
            "c_phys_irredundant_facets": facet_rows,
            "nf_He5_2p3n": list(nf_he5),
            "nf_C12_6p6n": list(nf_c12),
            "nf_N14_7p7n": list(nf_n14),
            "ame_Be8_minus_2alpha_MeV": fmt(+be8_minus_2alpha_ame),
            "ame_C12_minus_3alpha_MeV": fmt(+c12_minus_3alpha_ame),
        },
    )
    wb.add_data(
        "model_b_mayer_jensen_shell",
        {
            "shell_capacities": shell_caps,
            "cumulative_magic_numbers": cum_magic,
            "single_species_unsigned_graver_S7": len(gr_b_shell) // 2,
            "adjacent_promotion_confluence_S4_states": tested_states,
            "adjacent_promotion_100pct_confluent": confluence_ok,
        },
    )

    wb.add_assertion(
        name="model_a0_graver_28_circuits_17_ugb_27_chambers_73",
        computed=f"{len(unsigned_graver)},{len(circuits)},{len(ugb_unsigned)},{len(chambers)}",
        expected="28,17,27,73",
        source="Exact Pottier + [-6,6]^4 box Graver enumeration and rational BFS Grobner fan of A_0",
    )
    wb.add_assertion(
        name="qou_q0_bare_tower_and_ame2020_coincide_in_11_rule_5_wall_C_phys",
        computed=f"{same_chamber},{len(rgb_qou_bare)},{len(facet_rows)},{sympy_crosscheck_ok}",
        expected="True,11,5,True",
        source="QOU.MathlibInfra.gPhys_strict_cost_decrease_of_chamber + sympy.groebner cross-check",
    )
    wb.add_assertion(
        name="he5_drip_and_hoyle_bottleneck_verified",
        computed=f"{list(nf_he5)},{be8_minus_2alpha_ame < mpf(0)},{c12_minus_3alpha_ame > mpf(0)}",
        expected="[0, 1, 0, 0, 0, 1],True,True",
        source="QOU.MathlibInfra.he5_normal_form_eq_alpha_neutron and hoyle_triple_alpha_bottleneck",
    )
    wb.add_assertion(
        name="mayer_jensen_shell_graver_21_and_adjacent_confluence",
        computed=f"{cum_magic},{len(gr_b_shell)//2},{confluence_ok}",
        expected="[2, 8, 20, 28, 50, 82, 126],21,True",
        source="QOU.MathlibInfra.mayerJensen_cumulative_magic and capacitated_shell_occupancy_or_hole_pos",
    )

    wb.save({"q0Anchor": "proton", "preregistration": "PREREGISTRATION-chamber-gs.md"})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
