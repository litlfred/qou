#!/usr/bin/env python3
"""Independent derivation of the Whitehead-link adjoint Reidemeister torsion
|tau_adjoint(L5a1)| from the ideal-triangulation Neumann-Zagier data, closing the
gap qou-pn5j and upgrading c_sigma = 2^{-3/4} from IDENTIFICATION to DERIVATION.

Route 1 of bean qou-pn5j (Dimofte-Garoufalidis 1-loop = adjoint torsion).  The
1-loop invariant is the determinant of the gluing-equation Jacobian w.r.t.
log-shapes, on N equations = (N - #cusps independent edge equations) + (one
meridian per cusp):

    J_{k,j} = A_{k,j} - B_{k,j} * z_j/(1 - z_j),

where SnapPy's rect gluing equation k is   prod_i z_i^{A_i} (1 - z_i)^{B_i} = c_k,
so  d/d(log z_j) [ A log z + B log(1-z) ] = A - B * z/(1-z).

|tau| = |det J|  (validated: NO 1/2 factor and NO flattening monomial are needed
for the MODULUS, because the calibration below reproduces the known figure-eight
value |tau(4_1)| = sqrt(3) exactly).

CALIBRATION (non-circular): the SAME det(J) construction is run on 4_1, whose
adjoint torsion |tau| = sqrt(3) is classically known (trace field Q(sqrt(-3)),
c_sigma(4_1) = 3^{-1/4}).  Matching it pins the formula/normalization; L5a1 is
then a genuine prediction, NOT a fit of c_sigma.

RESULT (corrects the earlier qou-k00d inference).  The independent 1-loop
computation gives  |tau(L5a1)| = 4 sqrt(2) = 2^{5/2}  (det J = 4(1+i), a clean
Gaussian integer) -- i.e. a FACTOR OF 2 LARGER than the |tau| = 2 sqrt(2) that
the bare knot template c_sigma = |tau|^{-1/2} would infer from c_sigma = 2^{-3/4}.
The resolution is a per-cusp normalization: for a c-cusp link,

    c_sigma = 2^{(c-1)/2} * |tau_meridian|^{-1/2}

    - 4_1  (c=1):  2^0     * (sqrt 3)^{-1/2}   = 3^{-1/4}          (matches)
    - L5a1 (c=2):  2^{1/2} * (2^{5/2})^{-1/2}  = 2^{1/2-5/4} = 2^{-3/4}  (matches)

So c_sigma = 2^{-3/4} is DERIVED, via the geometrically-computed torsion
|tau| = 2^{5/2} plus the sqrt(2) two-cusp factor -- NOT via the (incorrect)
tau = 2 sqrt(2) inference.  The extra factor 2^{(c-1)/2} is consistent with the
two known cases (c = 1, 2); its general-c form is a smaller open sub-item (it
matches the standard per-cusp Gaussian-integration factor in the GGMW/Ohtsuki
saddle asymptotic).

⚠ REFUTED 2026-08-07 (PR #4691, bean qou-fl4t).  |det J| as computed here is
NOT a topological invariant: retriangulating the same manifold gives 8 distinct
values for 5_2 (a ONE-cusped knot), 17 for 6_2, 6 for L5a1, 7 for L6a4.  The
calibration on 4_1 cannot detect this — 4_1 has two tetrahedra, the one class
with no room to vary under Pachner moves.

The ambiguity group has since been identified (one_loop_ambiguity_group_probe.py):
it is the UNIT GROUP OF THE TRACE FIELD — sqrt(2) for L5a1/L6a4, sqrt(plastic)
for 5_2 (disc(x^3-x-1) = -23, the 5_2 trace field, ~30 digits).  That is exactly
where the dropped DG flattening monomial prod z''^f'' z'^f' lives, confirming the
diagnosis.  So the per-cusp factor 2^{(c-1)/2} below is not merely unproved, it
is UNIDENTIFIABLE: no universal constant absorbs a manifold-dependent unit group.

c_sigma = 2^{-3/4} therefore reverts to IDENTIFICATION (bean qou-pn5j, reopened).
[RESOLVED 2026-08-08: back to DERIVATION, but NOT by this file's route -- see
docs/audits/2026-08-08-c-sigma-derivation-status.md. The per-cusp factor below
does not exist; the derivation runs through the triangulation-invariant
computations/one_loop_torsion.py and carries the prefactor form as its one
stated assumption.]
Its NUMERICAL VALUE is unaffected — whitehead_c_sigma_hiprec.py pins it to ~20
digits independently, with no SnapPy and no det J.  Repair = restore the
flattening + the 1/2, then re-run the invariance probe.

⚠⚠ SUPERSEDED 2026-08-08 — THE PER-CUSP FACTOR DISSOLVES ENTIRELY.
(probes/one_loop_c_sigma_percusp_dissolution_probe.py; audit
docs/audits/2026-08-08-per-cusp-factor-dissolves.md)

The repair is done: `computations/one_loop_torsion.py` now computes the
triangulation-invariant DG invariant at ANY cusp number, giving
|tau(4_1)| = sqrt(3)/2, |tau(L5a1)| = sqrt(2), |tau(L6a4)| = 8 — NOT the
sqrt(3), 2^{5/2}, 64 computed here.  Against those,

    k_c := c_sigma * |tau_DG|^{1/2}   is the SAME constant 2^{-1/2}
    at c = 1 and c = 2, to 17 digits.

A per-cusp factor would require k to move by sqrt(2) between them; the measured
ratio is 0.999999999999999995.  So the correct law has NO per-cusp factor:

    c_sigma = 2^{-1/2} |tau_DG|^{-1/2}

and calibrating it on 4_1 ALONE predicts c_sigma(L5a1) = 2^{-3/4} to 17 digits
with nothing adjustable.

WHY THE FIT ABOVE LOOKED LIKE IT WORKED.  On the DEFAULT triangulations of 4_1,
L5a1 and L6a4 — and not in general — |tau_old| = 2^c |tau_DG|.  Substituting,
2^{(c-1)/2} |tau_old|^{-1/2} = 2^{-1/2} |tau_DG|^{-1/2} identically.  The
"standard per-cusp Gaussian-integration factor" claimed above was exactly the
c-dependence needed to undo that 2^c.  It is a reparametrization, and the 2^c
relation fails on 8 of the 13 manifolds tested — including 5_2, 6_2 and 7_4 at
c = 1, where there is no per-cusp factor to blame.

Audit-only; the derived tau is NOT wired to any production dashboard.
-- Ref: Dimofte-Garoufalidis, "The quantum content of the gluing equations",
        Geom. Topol. 17 (2013) 1253-1315 (1-loop invariant).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
if str(HERE / "substrate") not in sys.path:
    sys.path.insert(0, str(HERE / "substrate"))

from _precision import set_compute_dps, fmt  # noqa: E402

# Precision must be raised BEFORE any module-scope mpf constants:
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps(max(mp.mp.dps, 80))


def _rank_independent_rows(rows):
    """Greedily select a maximal set of C-linearly-independent row indices."""
    basis = []          # reduced echelon vectors
    chosen = []
    for idx, row in enumerate(rows):
        v = list(row)
        for b_idx, b in basis:
            piv = next(i for i, x in enumerate(b) if abs(x) > mp.mpf(10) ** -20)
            if abs(v[piv]) > mp.mpf(10) ** -20:
                f = v[piv] / b[piv]
                v = [vi - f * bi for vi, bi in zip(v, b)]
        if any(abs(x) > mp.mpf(10) ** -20 for x in v):
            basis.append((idx, v))
            chosen.append(idx)
    return chosen


def one_loop_torsion(name: str):
    """|det J| for manifold `name`, using indep. edges + one meridian per cusp."""
    import snappy
    M = snappy.Manifold(name)
    N = M.num_tetrahedra()
    ncusps = M.num_cusps()
    # High-precision shape read (bean qou-t0rf).  `complex(s)` is float64, so
    # the previous `mp.mpc(complex(s))` capped this computation near 16 digits
    # regardless of `mp.mp.dps`, and made its own 4_1 values wobble at digit 16
    # across runs.  Both halves are needed: asking SnapPy for `bits_prec` is
    # useless if the value is then routed through a double.
    _bits = int(mp.mp.dps * 3.3219) + 16
    z = [mp.mpc(mp.mpf(str(s.real()).replace(' ', '')), mp.mpf(str(s.imag()).replace(' ', '')))
         for s in M.tetrahedra_shapes('rect', bits_prec=_bits)]
    t = [z[j] / (1 - z[j]) for j in range(N)]           # z_j/(1-z_j)

    ge = M.gluing_equations('rect')                     # list of (A, B, c)
    nedges = len(ge) - 2 * ncusps                       # edges, then (mer,long)*cusps

    def jac_row(A, B):
        return [A[j] - B[j] * t[j] for j in range(N)]

    edge_rows = [jac_row(A, B) for (A, B, c) in ge[:nedges]]
    # one meridian per cusp: rect order is [mer, long] per cusp after the edges
    merid_rows = [jac_row(*ge[nedges + 2 * i][:2]) for i in range(ncusps)]

    indep = _rank_independent_rows(edge_rows)[: N - ncusps]
    J_rows = [edge_rows[i] for i in indep] + merid_rows
    J = mp.matrix(J_rows)
    det = mp.det(J)
    return abs(det), det, z


def _eval_fox_word(gens: dict, word: list) -> tuple[mp.matrix, list[int]]:
    """Evaluate a group-ring word under Φ = φ ⊗ Ad_{ρ^{-1}} in Mat_3(C)."""
    M = mp.eye(3)
    t_pow = [0, 0]
    for g, p, te in word:
        M = M * gens[(g, p)]
        t_pow[0] += te[0]
        t_pow[1] += te[1]
    return M, t_pow


def _extract_laurent_poly_from_fox(eval_P_fn, degree_cap: int) -> list[mp.mpc]:
    """Recover exact coefficients c_0..c_{degree_cap} of P(t) = ∑_{k=0}^D c_k t^k
    at 80 dps by Cauchy DFT on the circle |t| = 2 (away from the pole t = 1).
    """
    M_pts = max(16, 2 * (degree_cap + 1))
    r0 = mp.mpf(2)
    two_pi_i = 2j * mp.pi
    samples = []
    for m in range(M_pts):
        tm = r0 * mp.exp(two_pi_i * mp.mpf(m) / mp.mpf(M_pts))
        samples.append(eval_P_fn(tm))
    coeffs: list[mp.mpc] = []
    for k in range(degree_cap + 1):
        acc = mp.mpc(0)
        for m in range(M_pts):
            phase = mp.exp(-two_pi_i * mp.mpf(k * m) / mp.mpf(M_pts))
            acc += samples[m] * phase
        coeffs.append((acc / mp.mpf(M_pts)) / (r0 ** k))
    return coeffs


def _synthetic_div_by_t_minus_1(coeffs: list[mp.mpc], times: int) -> tuple[list[mp.mpc], mp.mpf]:
    """Divide ∑_{k=0}^D c_k t^k by (t - 1)^`times`; return quotient coeffs & max remainder."""
    cur = list(coeffs)
    max_rem = mp.mpf(0)
    # Descending Horner division: cur_desc[0] t^D + ... + cur_desc[D]
    for _ in range(times):
        desc = list(reversed(cur))
        q_desc = [desc[0]]
        for c in desc[1:]:
            q_desc.append(q_desc[-1] + c)
        rem = abs(q_desc.pop())
        if rem > max_rem:
            max_rem = rem
        cur = list(reversed(q_desc))
    return cur, max_rem


def dubois_yamaguchi_wirtinger_cross_check() -> dict:
    """Triangulation-independent 80-dps calculation of |τ_adjoint| for 4_1 (b=1)
    and Whitehead link L5a1 (b=2) via Dubois–Yamaguchi [dubois-yamaguchi2012]
    (arXiv:0906.1500v4) §4.1–4.2 Fox differential calculus, §6 Theorem 5 eq. (15)
    derivative formula, §6.3 eq. (29), and §8 Theorem 14 eq. (32) reciprocality
    (bean qou-1el8).
    """
    saved_dps = max(int(mp.mp.dps), 80)
    from one_loop_torsion import one_loop
    set_compute_dps(saved_dps)
    import snappy

    # ── 1. Figure-eight knot 4_1 (b = 1, §4.1 eqs. (31)–(103)) ───────────────
    # Complete hyperbolic holonomy lift: s = 1, u^2 + u + 1 = 0 => u = exp(2πi/3).
    u = mp.exp(2j * mp.pi / mp.mpf(3))
    Ax = mp.matrix([[1, 2, -1], [0, 1, -1], [0, 0, 1]])
    Ay = mp.matrix([[1, 0, 0], [-u, 1, 0], [-(u ** 2), 2 * u, 1]])
    gens41 = {("x", 1): Ax, ("x", -1): Ax ** -1, ("y", 1): Ay, ("y", -1): Ay ** -1}

    rel41 = [
        ("x", -1, [-1, 0]), ("y", 1, [1, 0]), ("x", 1, [1, 0]), ("y", -1, [-1, 0]),
        ("x", 1, [1, 0]), ("y", 1, [1, 0]), ("x", -1, [-1, 0]), ("y", -1, [-1, 0]),
        ("x", 1, [1, 0]), ("y", -1, [-1, 0]),
    ]
    M_rel41, _ = _eval_fox_word(gens41, rel41)
    rel41_err = mp.norm(M_rel41 - mp.eye(3))

    # Fox derivative ∂r/∂y = x^{-1} - x^{-1}yxy^{-1} + x^{-1}yxy^{-1}x - yx^{-1} - 1
    fox_terms_41 = [
        (+1, [("x", -1, [-1, 0])]),
        (-1, [("x", -1, [-1, 0]), ("y", 1, [1, 0]), ("x", 1, [1, 0]), ("y", -1, [-1, 0])]),
        (+1, [("x", -1, [-1, 0]), ("y", 1, [1, 0]), ("x", 1, [1, 0]), ("y", -1, [-1, 0]), ("x", 1, [1, 0])]),
        (-1, [("y", 1, [1, 0]), ("x", -1, [-1, 0])]),
        (-1, []),
    ]

    def eval_P41(t_val):
        # P_{4_1}(t) := t^3 * det Φ(∂r/∂y) / det Φ(x - 1)
        Num = mp.zeros(3, 3)
        for sgn, w in fox_terms_41:
            Mw, tp = _eval_fox_word(gens41, w)
            Num += sgn * (t_val ** tp[0]) * Mw
        Den = t_val * Ax - mp.eye(3)
        return (t_val ** 3) * (mp.det(Num) / mp.det(Den))

    coeffs_41 = _extract_laurent_poly_from_fox(eval_P41, degree_cap=4)
    # Closed form §4.1 eq. (102) at I_x = 2: (t - 1)(t^2 - 5t + 1) = -1 + 6t - 6t^2 + t^3
    exact_coeffs_41 = [mp.mpc(-1), mp.mpc(6), mp.mpc(-6), mp.mpc(1), mp.mpc(0)]
    poly_41_coeff_err = max(abs(a - b) for a, b in zip(coeffs_41, exact_coeffs_41))

    # Theorem 5 eq. (15) (b = 1, a_1 = 1): lim_{t->1} Δ(t)/(t - 1) = (-1)^1 T_λ(4_1)
    # Note Δ(t) = t^{-3} P_{4_1}(t), and t^{-3}|_{t=1} = 1.
    q_41, rem_41 = _synthetic_div_by_t_minus_1(coeffs_41[:4], times=1)
    T_lambda_41 = -sum(q_41)  # (-1)^1 factor from eq. (15)
    abs_T_lambda_41 = abs(T_lambda_41)

    # Theorem 14 eq. (33) bar-involution parity (b = 1 => odd: Δ(t^{-1}) = -t^3 Δ(t) for Δ = t^{-3}(t-1)(t^2-5t+1))
    t_probe = mp.mpf("1.37")
    delta_41_t = eval_P41(t_probe) / (t_probe ** 3)
    delta_41_inv = eval_P41(1 / t_probe) * (t_probe ** 3)
    recip_41_err = abs(delta_41_inv - (-(t_probe ** 3) * delta_41_t))

    # Porti §5.1 change-of-curve from longitude λ to meridian μ via cusp shape |s(4_1)| = 2√3:
    hp41 = snappy.ManifoldHP("4_1")
    s41_list = [mp.mpc(mp.mpf(str(x.real).replace(" ", "")), mp.mpf(str(x.imag).replace(" ", "")))
                for x in hp41.cusp_info("shape")]
    cusp_mod_41 = abs(s41_list[0])
    abs_T_mu_41_dy = abs_T_lambda_41 / cusp_mod_41
    abs_tau_dg_41 = abs(one_loop(snappy.Manifold("4_1"), [0]))
    set_compute_dps(saved_dps)

    # ── 2. Whitehead link L5a1 (b = 2, §4.2 eqs. (83)–(144) & §6.3 eq. (29)) ─
    # Complete hyperbolic holonomy lift: x = 2, y = 2, v = 1 + i (α = β = 1, γ = -1 + i).
    gamma_w = mp.mpc(-1, 1)
    Aa = mp.matrix([[1, 2, -1], [0, 1, -1], [0, 0, 1]])
    Ab = mp.matrix([[1, 0, 0], [gamma_w, 1, 0], [-(gamma_w ** 2), -2 * gamma_w, 1]])
    gensW = {("a", 1): Aa, ("a", -1): Aa ** -1, ("b", 1): Ab, ("b", -1): Ab ** -1}

    w_word = [
        ("b", 1, [0, 1]), ("a", 1, [1, 0]), ("b", -1, [0, -1]),
        ("a", -1, [-1, 0]), ("b", -1, [0, -1]), ("a", 1, [1, 0]), ("b", 1, [0, 1]),
    ]
    w_inv = [(g, -p, [-e for e in te]) for (g, p, te) in reversed(w_word)]
    relW = [("a", 1, [1, 0])] + w_word + [("a", -1, [-1, 0])] + w_inv
    M_relW, _ = _eval_fox_word(gensW, relW)
    relW_err = mp.norm(M_relW - mp.eye(3))

    # Full unreduced Fox derivative ∂(awa^{-1}w^{-1})/∂b = (a - 1)(1 - bab^{-1} - bab^{-1}a^{-1}b^{-1} + bab^{-1}a^{-1}b^{-1}a)
    # Evaluate det Φ(∂r/∂b) / det Φ(a - 1) directly from the full 8-term Fox sum on diagonal φ_{(1,1)} (t_1 = t_2 = t):
    factor_terms_W = [
        (+1, []),
        (-1, [("b", 1, [0, 1]), ("a", 1, [1, 0]), ("b", -1, [0, -1])]),
        (-1, [("b", 1, [0, 1]), ("a", 1, [1, 0]), ("b", -1, [0, -1]), ("a", -1, [-1, 0]), ("b", -1, [0, -1])]),
        (+1, [("b", 1, [0, 1]), ("a", 1, [1, 0]), ("b", -1, [0, -1]), ("a", -1, [-1, 0]), ("b", -1, [0, -1]), ("a", 1, [1, 0])]),
    ]
    full_fox_W = []
    for sgn, w in factor_terms_W:
        full_fox_W.append((+sgn, [("a", 1, [1, 0])] + w))
        full_fox_W.append((-sgn, w))

    def eval_PW_diag(t_val):
        # P_{L5a1}(t) := t^3 * det Φ(∂r/∂b)(t, t) / det Φ(a - 1)(t)
        Num = mp.zeros(3, 3)
        for sgn, w in full_fox_W:
            Mw, tp = _eval_fox_word(gensW, w)
            Num += sgn * (t_val ** (tp[0] + tp[1])) * Mw
        Den = t_val * Aa - mp.eye(3)
        return (t_val ** 3) * (mp.det(Num) / mp.det(Den))

    coeffs_W = _extract_laurent_poly_from_fox(eval_PW_diag, degree_cap=6)

    # Check §6.3 eq. (27): P_W(t) = (t - 1)^2 (-2xyv t^2 + (x^2 + y^2) t(t + 1)^2 - (t + 1)^4)
    t_check = mp.mpf("1.31")
    v_hol = mp.mpc(1, 1)
    closed_PW = ((t_check - 1) ** 2) * (
        -8 * v_hol * (t_check ** 2) + 8 * t_check * ((t_check + 1) ** 2) - ((t_check + 1) ** 4)
    )
    fox_PW_err = abs(eval_PW_diag(t_check) - closed_PW)

    # Theorem 5 eq. (15) (b = 2, a_1 = a_2 = 1): lim_{t->1} Δ(t, t)/(t - 1)^2 = (-1)^2 T_λ(L5a1)
    q_W, rem_W = _synthetic_div_by_t_minus_1(coeffs_W, times=2)
    T_lambda_W = sum(q_W)  # (-1)^2 = +1, t^{-3}|_{t=1} = 1
    abs_T_lambda_W = abs(T_lambda_W)

    # Theorem 14 eq. (32) bar-involution parity (b = 2 => even: Δ(t^{-1}, t^{-1}) = +Δ(t, t) up to t^k; here k = 0!)
    delta_W_t = eval_PW_diag(t_probe) / (t_probe ** 3)
    delta_W_inv = eval_PW_diag(1 / t_probe) * (t_probe ** 3)
    recip_W_err = abs(delta_W_inv - delta_W_t)

    # Porti §5.1 per-cusp change-of-curve from multi-longitude λ = (λ_1, λ_2) to multi-meridian μ = (μ_1, μ_2):
    hpW = snappy.ManifoldHP("L5a1")
    sW_list = [mp.mpc(mp.mpf(str(x.real).replace(" ", "")), mp.mpf(str(x.imag).replace(" ", "")))
               for x in hpW.cusp_info("shape")]
    cusp_mod_prod_W = abs(sW_list[0]) * abs(sW_list[1])
    abs_T_mu_W_dy = abs_T_lambda_W / cusp_mod_prod_W
    abs_tau_dg_W = abs(one_loop(snappy.Manifold("L5a1"), [0, 0]))
    set_compute_dps(saved_dps)

    # Honest comparison against BOTH the superseded unflattened corpus values (√3 and 2^{5/2})
    # AND the triangulation-invariant DG values (√3/2 and √2):
    sqrt3 = mp.sqrt(3)
    sqrt3_over_2 = sqrt3 / 2
    two_pow_5_2 = 4 * mp.sqrt(2)
    sqrt2 = mp.sqrt(2)

    ratio_old_to_dy_41 = sqrt3 / abs_T_mu_41_dy          # = 2 = 2^1
    ratio_old_to_dy_W = two_pow_5_2 / abs_T_mu_W_dy      # = 4 = 2^2

    # Universal b-independent c_σ law: k := c_σ * |T_μ|^{1/2} calibrated on 4_1 (c_σ(4_1) = 3^{-1/4}):
    k_41 = mp.power(3, mp.mpf(-1) / 4) * mp.sqrt(abs_T_mu_41_dy)   # = 2^{-1/2}
    csig_W_universal = k_41 / mp.sqrt(abs_T_mu_W_dy)               # = 2^{-3/4} with NO per-cusp factor!
    csig_W_target = mp.power(2, mp.mpf(-3) / 4)

    tol = mp.mpf("1e-55")
    assertions = [
        {
            "name": "dy2012_4_1_wirtinger_relator_vanishes_80dps",
            "computed": fmt(rel41_err),
            "expected": "0",
            "tolerance": "1e-70",
            "passed": bool(rel41_err < mp.mpf("1e-70")),
        },
        {
            "name": "dy2012_4_1_fox_poly_matches_eq102_80dps",
            "computed": fmt(poly_41_coeff_err),
            "expected": "0",
            "tolerance": "1e-65",
            "passed": bool(poly_41_coeff_err < mp.mpf("1e-65") and rem_41 < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_4_1_thm5_longitude_torsion_equals_3",
            "computed": fmt(abs_T_lambda_41),
            "expected": fmt(mp.mpf(3)),
            "tolerance": "1e-65",
            "passed": bool(abs(abs_T_lambda_41 - 3) < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_4_1_meridian_torsion_equals_sqrt3_over_2_matches_dg",
            "computed": fmt(abs_T_mu_41_dy),
            "expected": fmt(sqrt3_over_2),
            "tolerance": "1e-55",
            "passed": bool(abs(abs_T_mu_41_dy - sqrt3_over_2) < tol and abs(abs_T_mu_41_dy - abs_tau_dg_41) < tol),
        },
        {
            "name": "dy2012_4_1_thm14_bar_reciprocality_odd_b1",
            "computed": fmt(recip_41_err),
            "expected": "0",
            "tolerance": "1e-65",
            "passed": bool(recip_41_err < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_L5a1_wirtinger_relator_vanishes_80dps",
            "computed": fmt(relW_err),
            "expected": "0",
            "tolerance": "1e-70",
            "passed": bool(relW_err < mp.mpf("1e-70")),
        },
        {
            "name": "dy2012_L5a1_fox_poly_matches_eq27_80dps",
            "computed": fmt(fox_PW_err),
            "expected": "0",
            "tolerance": "1e-65",
            "passed": bool(fox_PW_err < mp.mpf("1e-65") and rem_W < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_L5a1_thm5_multilongitude_torsion_equals_8sqrt2_eq29",
            "computed": fmt(abs_T_lambda_W),
            "expected": fmt(8 * sqrt2),
            "tolerance": "1e-65",
            "passed": bool(abs(abs_T_lambda_W - 8 * sqrt2) < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_L5a1_multimeridian_torsion_equals_sqrt2_matches_dg",
            "computed": fmt(abs_T_mu_W_dy),
            "expected": fmt(sqrt2),
            "tolerance": "1e-55",
            "passed": bool(abs(abs_T_mu_W_dy - sqrt2) < tol and abs(abs_T_mu_W_dy - abs_tau_dg_W) < tol),
        },
        {
            "name": "dy2012_L5a1_thm14_bar_reciprocality_even_b2",
            "computed": fmt(recip_W_err),
            "expected": "0",
            "tolerance": "1e-65",
            "passed": bool(recip_W_err < mp.mpf("1e-65")),
        },
        {
            "name": "dy2012_universal_no_percusp_law_predicts_c_sigma_2_pow_minus_3_4",
            "computed": fmt(csig_W_universal),
            "expected": fmt(csig_W_target),
            "tolerance": "1e-55",
            "passed": bool(abs(csig_W_universal - csig_W_target) < tol),
        },
    ]

    report = {
        "source": "[dubois-yamaguchi2012] arXiv:0906.1500v4, §4.1–4.2, §6 Theorem 5 eq. (15), §6.3 eq. (29), §8 Theorem 14 eq. (32)",
        "compute_dps": int(mp.mp.dps),
        "figure_eight_4_1": {
            "num_boundary_tori_b": 1,
            "wirtinger_relator_norm_err": fmt(rel41_err),
            "thm5_longitude_torsion_abs": fmt(abs_T_lambda_41),
            "cusp_shape_modulus": fmt(cusp_mod_41),
            "meridian_torsion_dy_abs": fmt(abs_T_mu_41_dy),
            "meridian_torsion_dg_abs": fmt(abs_tau_dg_41),
            "superseded_detJ_sqrt3": fmt(sqrt3),
            "ratio_superseded_detJ_to_dy_meridian": fmt(ratio_old_to_dy_41),
            "thm14_bar_parity_sign": -1,
            "thm14_reciprocality_abs_err": fmt(recip_41_err),
        },
        "whitehead_link_L5a1": {
            "num_boundary_tori_b": 2,
            "wirtinger_relator_norm_err": fmt(relW_err),
            "thm5_multilongitude_torsion_re": fmt(T_lambda_W.real),
            "thm5_multilongitude_torsion_im": fmt(T_lambda_W.imag),
            "thm5_multilongitude_torsion_abs": fmt(abs_T_lambda_W),
            "cusp_shape_modulus_product": fmt(cusp_mod_prod_W),
            "multimeridian_torsion_dy_abs": fmt(abs_T_mu_W_dy),
            "multimeridian_torsion_dg_abs": fmt(abs_tau_dg_W),
            "superseded_detJ_2_pow_5_2": fmt(two_pow_5_2),
            "ratio_superseded_detJ_to_dy_multimeridian": fmt(ratio_old_to_dy_W),
            "thm14_bar_parity_sign": 1,
            "thm14_reciprocality_abs_err": fmt(recip_W_err),
        },
        "adjudication_qou_1el8": {
            "per_cusp_factor_2_pow_c_minus_1_over_2": "REFUTED — unflattened |det J| carried a triangulation-specific 2^b factor (2 at b=1 giving sqrt(3) vs sqrt(3)/2; 4 at b=2 giving 2^{5/2} vs sqrt(2)).",
            "universal_b_independent_law": "c_sigma = 2^{-1/2} * |T_mu|^{-1/2}",
            "calibrated_prefactor_k_from_4_1": fmt(k_41),
            "predicted_c_sigma_L5a1": fmt(csig_W_universal),
            "target_2_pow_minus_3_4": fmt(csig_W_target),
            "abs_diff": fmt(abs(csig_W_universal - csig_W_target)),
        },
    }
    return report, assertions


if __name__ == "__main__":
    mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else max(mp.mp.dps, 80)

    print(f"1-loop adjoint torsion from NZ data — mpmath dps={mp.mp.dps}\n")

    # --- calibration on the figure-eight (|tau| = sqrt(3) known) ---
    tau41, det41, _ = one_loop_torsion('4_1')
    sqrt3 = mp.sqrt(3)
    rel41 = abs(tau41 - sqrt3) / sqrt3
    dig41 = int(-mp.log10(rel41)) if rel41 > 0 else 999
    print("CALIBRATION  4_1:")
    print(f"  |det J|      = {mp.nstr(tau41, 25)}")
    print(f"  sqrt(3)      = {mp.nstr(sqrt3, 25)}")
    print(f"  match: ~{dig41} digits   ({'OK' if dig41 >= 12 else 'FAIL'})\n")

    # --- prediction for the Whitehead link ---
    tauW, detW, zW = one_loop_torsion('L5a1')
    import snappy
    ncW = snappy.Manifold('L5a1').num_cusps()
    target = 4 * mp.sqrt(2)                              # 2^{5/2} (DERIVED torsion)
    relW = abs(tauW - target) / target
    digW = int(-mp.log10(relW)) if relW > 0 else 999
    # colored-Jones prefactor via the per-cusp normalization c_sigma = 2^{(c-1)/2}|tau|^{-1/2}
    csig = mp.power(2, (ncW - 1) / mp.mpf(2)) * tauW ** (mp.mpf(-1) / 2)
    csig_target = mp.power(2, mp.mpf(-3) / 4)
    rel_cs = abs(csig - csig_target) / csig_target
    dig_cs = int(-mp.log10(rel_cs)) if rel_cs > 0 else 999
    print("PREDICTION  L5a1 (Whitehead):")
    print(f"  shapes z     = {[mp.nstr(s, 6) for s in zW]}")
    print(f"  det J        = {mp.nstr(detW, 20)}   (= 4(1+i))")
    print(f"  |tau| = |det J| = {mp.nstr(tauW, 25)}")
    print(f"  4*sqrt(2)=2^5/2 = {mp.nstr(target, 25)}")
    print(f"  match: ~{digW} digits   ({'DERIVED' if digW >= 12 else 'NO MATCH'})")
    print(f"\n  c_sigma = 2^((c-1)/2)|tau|^(-1/2), c={ncW}:")
    print(f"    derived  = {mp.nstr(csig, 20)}")
    print(f"    2^(-3/4) = {mp.nstr(csig_target, 20)}   (match ~{dig_cs} digits)")

    # --- 3-cusp cross-check: Borromean rings L6a4 (corpus: W1 probe, PR #4238) ---
    # |det J_NZ(L6a4)| = 64 is ALREADY in the corpus
    # (computations/probes/borromean_nz_adjoint_torsion.py, 2026-07-25); this
    # reproduces it independently and tests the per-cusp factor at c=3.
    tauB, detB, zB = one_loop_torsion('L6a4')
    ncB = snappy.Manifold('L6a4').num_cusps()
    tauB_target = mp.mpf(64)                             # 2^6
    # Guard on the RELATIVE ERROR, not on tauB. Once the shape read stopped
    # losing precision to SnapPy's spaced exponents this hit 64 exactly, and
    # `tauB > 0` let log10(0) = -inf through into int() — a crash on success.
    relB = abs(tauB - tauB_target) / tauB_target
    digB = int(-mp.log10(relB)) if relB > 0 else 999
    # unified relation  exp(2 c0) = 2^{c-1}/|det J|  =>  c0 = (1/2) log(2^{c-1}/|det|)
    c0B_pred = mp.log(mp.power(2, ncB - 1) / tauB) / 2
    c0B_measured = mp.mpf("-1.3828105122579213")         # W1 Jones-side, NMAX=56 (borromean-jones-1loop-torsion.witness.json)
    csigB = mp.power(2, (ncB - 1) / mp.mpf(2)) * tauB ** (mp.mpf(-1) / 2)
    print(f"\n  CROSS-CHECK  L6a4 (Borromean, c={ncB}) — corpus |det|=64 (W1/#4238):")
    print(f"    |tau| = {mp.nstr(tauB, 18)}  (target 2^6=64; ~{digB} digits)")
    print(f"    c_sigma = 2^((c-1)/2)|tau|^-1/2 = {mp.nstr(csigB, 12)} (= 1/4)")
    print(f"    c0 predicted (unified law) = {mp.nstr(c0B_pred, 8)}")
    print(f"    c0 measured  (W1 Jones)    = {mp.nstr(c0B_measured, 8)}"
          f"   -> {mp.nstr(abs(c0B_pred-c0B_measured)/abs(c0B_measured)*100, 3)}% "
          f"(fit err; W1 p=1.4993 vs 3/2)")

    ok = dig41 >= 12 and digW >= 12 and dig_cs >= 12 and digB >= 12
    print("\n  ARITHMETIC:", "internally consistent at this precision."
          if ok else "not clean at this precision; inspect formula/curve choice.")
    print("  VERDICT: SUPERSEDED. The numbers above reproduce, but |det J| is not a")
    print("  topological invariant (PR #4691) and the per-cusp factor does not exist")
    print("  (probes/one_loop_c_sigma_percusp_dissolution_probe.py). The invariant")
    print("  values are |tau(4_1)|=sqrt(3)/2, |tau(L5a1)|=sqrt(2), |tau(L6a4)|=8, from")
    print("  computations/one_loop_torsion.py; the law is c_sigma = 2^{-1/2}|tau|^{-1/2}.")
    print("  c_sigma = 2^{-3/4} IS derived, but by that route, not this one --")
    print("  docs/audits/2026-08-08-c-sigma-derivation-status.md.")

    dy_report, dy_assertions = dubois_yamaguchi_wirtinger_cross_check()
    dy_all_passed = all(a["passed"] for a in dy_assertions)
    print("\n  DUBOIS–YAMAGUCHI (0906.1500v4) WIRTINGER FOX-DERIVATIVE CROSS-CHECK (qou-1el8):")
    print(f"    4_1  (b=1): |T_λ| = {dy_report['figure_eight_4_1']['thm5_longitude_torsion_abs']}, "
          f"|T_μ| = {dy_report['figure_eight_4_1']['meridian_torsion_dy_abs']} (= sqrt(3)/2; old |det J|/2)")
    print(f"    L5a1 (b=2): |T_λ| = {dy_report['whitehead_link_L5a1']['thm5_multilongitude_torsion_abs']} (= 8*sqrt(2)), "
          f"|T_μ| = {dy_report['whitehead_link_L5a1']['multimeridian_torsion_dy_abs']} (= sqrt(2); old |det J|/4)")
    print(f"    Universal b-independent c_σ(L5a1) = {dy_report['adjudication_qou_1el8']['predicted_c_sigma_L5a1']} "
          f"(diff vs 2^(-3/4): {dy_report['adjudication_qou_1el8']['abs_diff']})")

    wit = {
        "q0Anchor": "independent",
        "q0AnchorReason": "Pure hyperbolic 3-manifold Reidemeister torsion and Wirtinger Fox-calculus twisted Alexander derivative on 4_1, L5a1, and L6a4; q_0 does not enter.",
        "superseded": "2026-08-08: |det J| here is not a topological invariant (PR #4691) and the per-cusp factor 2^{(c-1)/2} does not exist. Invariant values: |tau(4_1)|=sqrt(3)/2, |tau(L5a1)|=sqrt(2), |tau(L6a4)|=8 via computations/one_loop_torsion.py and confirmed triangulation-independently at 80 dps via Dubois-Yamaguchi [dubois-yamaguchi2012] Theorem 5 eq. (15) Fox derivative on Wirtinger presentations (qou-1el8); law is c_sigma = 2^{-1/2}|tau_DG|^{-1/2}. c_sigma=2^{-3/4} is DERIVED by that b-independent route (docs/audits/2026-08-08-c-sigma-derivation-status.md). Legacy |det J| fields below are retained for history alongside dubois_yamaguchi_2012_wirtinger_cross_check.",
        "description": "[SUPERSEDED |det J| + ADJUDICATED via dubois-yamaguchi2012] Triangulation-independent Wirtinger Fox-calculus derivative (Dubois-Yamaguchi 2012 Thm 5 eq. 15) gives |T_lambda(4_1)|=3 => |T_mu(4_1)|=sqrt(3)/2 and |T_lambda(L5a1)|=8sqrt(2) => |T_mu(L5a1)|=sqrt(2), confirming that unflattened |det J| carried a 2^b factor (sqrt(3) and 2^{5/2}) and deriving c_sigma(L5a1)=2^{-3/4} from 4_1 with NO per-cusp factor.",
        "computation": "whitehead_c_sigma_torsion", "audit_only": True,
        "dps": int(mp.mp.dps),
        "assertions": dy_assertions,
        "allPassed": bool(ok and dy_all_passed),
        "method": "1-loop invariant det(J) [legacy] cross-checked against triangulation-independent Wirtinger Fox-calculus derivative lim_{t->1} Delta(t)/(t-1)^b = (-1)^b T_lambda (Dubois-Yamaguchi 2012 Thm 5 eq. 15)",
        "calib_4_1": {"det_abs": fmt(tau41), "sqrt3": fmt(sqrt3),
                       "match_digits": dig41},
        "whitehead_L5a1": {"num_cusps": ncW, "det": f"({fmt(detW.real)} + {fmt(detW.imag)}j)",
                            "tau_abs": fmt(tauW),
                            "target_2_pow_5_2": fmt(target),
                            "match_digits": digW},
        "c_sigma_relation": "c_sigma = 2^{-1/2} * |T_mu|^{-1/2} (b-independent; legacy 2^{(c-1)/2}|det J|^{-1/2} cancelled a triangulation-specific 2^c factor)",
        "c_sigma_derived": fmt(csig),
        "c_sigma_target_2_pow_minus_3_4": fmt(csig_target),
        "c_sigma_match_digits": dig_cs,
        "borromean_L6a4_crosscheck": {
            "num_cusps": ncB, "tau_abs": fmt(tauB), "target_2_pow_6": "64",
            "match_digits": digB,
            "corpus_source": "computations/probes/borromean_nz_adjoint_torsion.py (W1, PR #4238, 2026-07-25) already has |det|=64; reproduced here independently",
            "c_sigma_derived": fmt(csigB),
            "c0_predicted_unified_law": fmt(c0B_pred),
            "c0_measured_W1_jones": "-1.3828105122579213",
            "note": "Legacy unflattened |det J|=64 = 2^3 * 8 vs invariant |tau_DG(L6a4)|=8; universal b-independent law gives c_sigma = 2^{-1/2} * 8^{-1/2} = 1/4 => c0 = -1/2 ln 16 = -1.3863 vs W1 Jones-side -1.3828."},
        "dubois_yamaguchi_2012_wirtinger_cross_check": dy_report,
        "corrects_prior_inference": "qou-k00d/PR#4571 recorded tau=2sqrt(2); unflattened 1-loop gave |det J|=4sqrt(2)=2^{5/2}; Dubois-Yamaguchi 2012 Thm 5 eq. (15) + Porti cusp-shape change-of-curve pins triangulation-invariant |T_mu(4_1)|=sqrt(3)/2 and |T_mu(L5a1)|=sqrt(2), deriving c_sigma(L5a1)=2^{-3/4} with zero per-cusp factor.",
        "cusp_factor_status": "REFUTED & DISSOLVED (qou-fl4t, qou-1el8): Dubois-Yamaguchi 2012 Theorem 5 eq. (15) holds for all b >= 1 without any b-dependent prefactor and matches one_loop_torsion.py at both b=1 (4_1) and b=2 (L5a1) to 80 dps.",
        "derivation_complete": bool(ok and dy_all_passed),
        "reference": "Dubois-Yamaguchi, arXiv:0906.1500v4 [dubois-yamaguchi2012]; Dimofte-Garoufalidis, Geom. Topol. 17 (2013) 1253; Porti (1997) adjoint torsion",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c-sigma-torsion.witness.json"
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    wit.setdefault("engine", "mpmath")
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine="mpmath", q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n  Witness: {out}")
    sys.exit(0 if (ok and dy_all_passed) else 1)
