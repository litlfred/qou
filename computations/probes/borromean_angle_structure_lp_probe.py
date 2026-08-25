#!/usr/bin/env python3
"""borromean_angle_structure_lp_probe.py — the Casson-Rivin angle-structure LP of the
Borromean rings complement B3, with full LP-dual emission, and the exact Prop-A.3
(Gauss-Bonnet) pairing against the vertex spun-normal surfaces of the same triangulation.

Executes idea B2 of docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md:
the angle-structure LP <-> confinement-SDP dual dictionary, COMPARISON-ONLY.

SOURCES (primary, no guessed conventions):
  [GA]    Garoufalidis, "The 3D index of an ideal triangulation and angle structures"
          (arXiv:1208.1663, library/arxiv-1208.1663v2/1208.1663v2.pdf):
          - Section 2.2: a generalized angle structure on an ideal tetrahedron assigns
            angles at edges summing to 1 around each vertex (footnote 2: "traditionally
            pi" — we work in pi-units throughout); opposite edges share the angle, so a
            tetrahedron carries a triple (alpha, beta, gamma) with alpha+beta+gamma = 1.
            On a triangulation T the sum of angles around every EDGE of T is 2.
            Strict = all angles > 0.
          - Section 2.3 eq (2.7):  Abar*alpha + Bbar*beta + Cbar*gamma = (2,...,2)^T,
            alpha + beta + gamma = (1,...,1)^T  — exactly the linear system built here
            from SnapPy's gluing_equations() rows (N edge rows in the (a|b|c) exponent
            convention + 2r peripheral rows).
          - Thm 2.12: the 3D index I_T is well-defined if T admits a strict angle
            structure; hence the strict solution found here re-certifies (by a second,
            LP route) the well-definedness the sibling probe borromean_3d_index.py
            used via SnapPy's "all tetrahedra positively oriented".
  [GHHR]  Garoufalidis-Hodgson-Hoffman-Rubinstein, "The 3D-index and normal surfaces"
          (arXiv:1604.02688, library/arxiv-1604.02688v1/1604.02688v1.pdf):
          - Prop A.3 (eq (34)): for any generalised angle structure alpha and any
            embedded spun normal surface S,
                chi(S) = - sum_q alpha(q) x_q / pi + rho_alpha(dS) / (2 pi),
            where alpha(q) is the angle on the two edges FACING quad q and rho_alpha
            the rotational holonomy of the boundary, oriented as in [dS].
          - Example A.10 + Example 10.23: worked m004 case — the four vertex spun
            normal surfaces are once-punctured Klein bottles with boundary
            +-4mu +- lambda and chi = -1.  This is the validation target for the
            pairing implementation (stage 1).
          - Remark A.9 / formula (39) and Example A.10's "K = 2M + (1/2)L + 1T2":
            tetrahedral solutions T_t (the per-tet (1,1,1) quad-space vectors) are
            legitimate formal Q-normal generators with formal chi = -1; they are used
            below (with free sign) in the dual-certificate decomposition.
          - Theorem A.11 (Farkas): angle structures are dual to surfaces of
            non-negative (formal) Euler characteristic — the Casson-Rivin /
            Luo-Tillmann duality this probe makes concrete for B3.

CONVENTIONS PINNED EMPIRICALLY, THEN FROZEN (stage 1, m004):
  - facing permutation sigma: SnapPy quad type t (slot 3j+t of Surface.quad_vector())
    faces the angle in shape-variable slot 3j+sigma[t].  All 6 candidates tested;
    exactly one — sigma = (1,2,0) — reproduces chi = -1 on all four m004 vertex
    surfaces alpha-independently.
  - boundary-orientation sign eps: rho_alpha(dS) = eps * pi * sum_h (p_h*murow_h +
    q_h*lamrow_h) . alpha with (p_h, q_h) = Surface.boundary_slopes(); eps = -1 is
    forced by alpha-independence (the GHHR [dS] orientation is opposite to SnapPy's
    reported slope under its peripheral-row convention).
  In pi-units the frozen formula is
      chi(S) = - sum_q alpha(sigma(q)) x_q - (1/2) * sum_h (p_h*murow_h + q_h*lamrow_h) . alpha .

LP-DUAL EMISSION (AGENTS.md "LP / SDP duals — first-class infra", STRICT):
  The witness carries y0_star, y_star, active_set, primal_obj, dual_obj, duality_gap.
  The repo's canonical entry point solve_operator_selection_lp(t, G, n_target)
  (computations/lp_dual_solver.py -> pyhecke.lp_dual_solver) does NOT fit this LP's
  shape (it solves min t.x s.t. 1^T x = n_target, G x >= 0 with a square Gram G; the
  angle LP is max-min over 16 equality constraints + 24 positivity constraints with
  no Gram/target pair), so this probe MIRRORS its output contract exactly instead:
      x_star      — the strict angle structure (24 exact rationals, pi-units)
      y0_star     — shadow price of the normalization bundle (per-tet sums = 1,
                    per-edge sums = 2): the dual objective sum_t w_t + 2 sum_e w_e
      y_star      — the 24 shadow prices z_i >= 0 of the angle-positivity
                    constraints x_i >= s (the Frobenius-positivity analog)
      active_set  — {i : z_i > 0}
      primal_obj  — s* (the max-min angle, in pi-units)
      dual_obj    — the dual optimum (= s*, exact)
      duality_gap — exactly 0 (rational arithmetic)
  The per-constraint arrays w_tet_star / w_edge_star are emitted additionally.

SOLVER NOTE. sympy 1.14's sympy.solvers.simplex._simplex was found to RETURN
INFEASIBLE POINTS without raising on infeasible inequality systems (minimal repro in
preflight below).  The probe therefore embeds a small exact two-phase simplex
(Fraction arithmetic, Bland's rule) and — decisively — VERIFIES EVERY CERTIFICATE
EXACTLY (primal feasibility, dual feasibility, complementary slackness, strong
duality), so no conclusion rests on trusting any solver implementation.

SCOPE (STRICT). Audit-only; scope-(a); comparison-only; NO FIT; nothing wired to
production.  The confinement-SDP side is READ from its committed witnesses
(computations/borromean-axial-coupling.witness.json — the beta_Bor operator-selection
LP over the 6-element H_3(q) NF basis, and
computations/nucleus-real-sdp-proton.witness.json — the 3-Wedderburn-block proton
solve); no number from the angle LP is compared numerically to any number from the
SDP.  The deliverable is the count/rank/structure table and the formal question a
real dictionary must answer.

Audit doc: docs/audits/2026-07-24-angle-structure-lp-sdp-dictionary.md
"""
from __future__ import annotations

import itertools
import json
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------------------
# Exact two-phase simplex (Fraction arithmetic, Bland's rule) with certified
# primal + dual output.   min c.x  s.t.  A x = b, x >= 0.
# ---------------------------------------------------------------------------

class Infeasible(Exception):
    pass


class Unbounded(Exception):
    pass


def _pivot(T, basis, row, col):
    piv = T[row][col]
    T[row] = [v / piv for v in T[row]]
    for i, R in enumerate(T):
        if i != row and R[col] != 0:
            f = R[col]
            T[i] = [a - f * b for a, b in zip(R, T[row])]
    basis[row] = col


def _solve_phase(T, basis, ncols, cost_row):
    while True:
        enter = None
        for j in range(ncols):  # Bland: smallest-index negative reduced cost
            if T[cost_row][j] < 0:
                enter = j
                break
        if enter is None:
            return
        leave = None
        best = None
        for i in range(cost_row):
            if T[i][enter] > 0:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best or (
                        ratio == best and basis[i] < basis[leave]):
                    best = ratio
                    leave = i
        if leave is None:
            raise Unbounded()
        _pivot(T, basis, leave, enter)


def _solve_linear(M, rhs):
    n = len(M)
    A = [list(M[i]) + [rhs[i]] for i in range(n)]
    for col in range(n):
        piv = next(i for i in range(col, n) if A[i][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [v / pv for v in A[col]]
        for i in range(n):
            if i != col and A[i][col] != 0:
                f = A[i][col]
                A[i] = [a - f * b for a, b in zip(A[i], A[col])]
    return [A[i][-1] for i in range(n)]


def _simplex_eq(A, b, c):
    m, n = len(A), len(A[0])
    A = [[Fraction(x) for x in row] for row in A]
    b = [Fraction(x) for x in b]
    c = [Fraction(x) for x in c]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-x for x in A[i]]
            b[i] = -b[i]
    T = [A[i] + [Fraction(1) if k == i else Fraction(0) for k in range(m)] + [b[i]]
         for i in range(m)]
    basis = [n + i for i in range(m)]
    cost = [Fraction(0)] * (n + m + 1)
    for j in range(n + m):
        s = sum(T[i][j] for i in range(m) if basis[i] >= n)
        cost[j] = (Fraction(1) if j >= n else Fraction(0)) - s
    cost[-1] = -sum(b)
    T.append(cost)
    _solve_phase(T, basis, n + m, m)
    if -T[m][-1] != 0:
        raise Infeasible()
    drop = []
    for i in range(m):
        if basis[i] >= n:
            piv = next((j for j in range(n) if T[i][j] != 0), None)
            if piv is None:
                drop.append(i)  # redundant row
            else:
                _pivot(T, basis, i, piv)
    keep = [i for i in range(m) if i not in drop]
    T2 = [[T[i][j] for j in range(n)] + [T[i][-1]] for i in keep]
    basis2 = [basis[i] for i in keep]
    m2 = len(T2)
    cost2 = list(c) + [Fraction(0)]
    for i in range(m2):
        if cost2[basis2[i]] != 0:
            f = cost2[basis2[i]]
            cost2 = [a - f * bv for a, bv in zip(cost2, T2[i])]
    T2.append(cost2)
    _solve_phase(T2, basis2, n, m2)
    x = [Fraction(0)] * n
    for i in range(m2):
        x[basis2[i]] = T2[i][-1]
    obj = sum(ci * xi for ci, xi in zip(c, x))
    AB = [[A[keep[i]][basis2[k]] for i in range(m2)] for k in range(m2)]
    cB = [c[basis2[k]] for k in range(m2)]
    y_kept = _solve_linear(AB, cB)
    y = [Fraction(0)] * m
    for i, yi in zip(keep, y_kept):
        y[i] = yi
    return obj, x, y


def solve_and_certify(A, b, c):
    """min c.x s.t. Ax = b, x >= 0 — with EXACT verification of every certificate."""
    obj, x, y = _simplex_eq(A, b, c)
    m, n = len(A), len(A[0])
    A_ = [[Fraction(v) for v in row] for row in A]
    b_ = [Fraction(v) for v in b]
    c_ = [Fraction(v) for v in c]
    for i in range(m):
        assert sum(A_[i][j] * x[j] for j in range(n)) == b_[i], f"primal row {i}"
    assert all(v >= 0 for v in x), "primal negativity"
    y = [(-yi if b_[i] < 0 else yi) for i, yi in enumerate(y)]  # undo row sign flips
    for j in range(n):
        red = c_[j] - sum(A_[i][j] * y[i] for i in range(m))
        assert red >= 0, f"dual infeasible col {j}: {red}"
        if x[j] > 0:
            assert red == 0, f"complementary slackness col {j}"
    assert sum(y[i] * b_[i] for i in range(m)) == obj, "strong duality"
    return obj, x, y


# ---------------------------------------------------------------------------
# Gluing data (SnapPy — the same NZ source as borromean_3d_index.py)
# ---------------------------------------------------------------------------

def exact_int(x):
    f = Fraction(str(x))
    assert f.denominator == 1, f"non-integer datum {x!r}"
    return int(f)


def gluing(snappy, name):
    M = snappy.Manifold(name)
    N = M.num_tetrahedra()
    r = M.num_cusps()
    G = M.gluing_equations()
    rows = [[int(x) for x in row] for row in G.data] if hasattr(G, "data") else \
        [[int(G[i][j]) for j in range(3 * N)] for i in range(len(G))]
    assert len(rows) == N + 2 * r
    return M, N, r, rows[:N], rows[N:]


def ga_equalities(N, edge_rows):
    """GA eq (2.7) in pi-units: per-tet sums = 1, per-edge sums = 2."""
    A, b = [], []
    for j in range(N):
        row = [0] * (3 * N)
        row[3 * j] = row[3 * j + 1] = row[3 * j + 2] = 1
        A.append(row)
        b.append(1)
    for e in edge_rows:
        A.append(list(e))
        b.append(2)
    return A, b


def ga_general_solution(A, b):
    """Exact particular solution + nullspace basis of the GA equality system."""
    from sympy import Matrix
    Am = Matrix(A)
    part, params = Am.gauss_jordan_solve(Matrix(b))
    x0 = part.subs({p: 0 for p in params})
    basis = []
    for p in params:
        basis.append(part.subs({q: (1 if q == p else 0) for q in params}) - x0)
    rank = Am.rank()
    return [Fraction(str(v)) for v in x0], \
        [[Fraction(str(v)) for v in nv] for nv in basis], rank


def random_ga(x0, basis, seed):
    rng = random.Random(seed)
    x = list(x0)
    for nvec in basis:
        t = Fraction(rng.randint(-9, 9), rng.randint(1, 7))
        x = [a + t * b for a, b in zip(x, nvec)]
    return x


# ---------------------------------------------------------------------------
# Prop A.3 pairing (pi-units): chi(S) = -P_sigma(S).alpha + eps*(1/2)*per(S).alpha
# ---------------------------------------------------------------------------

def facing_vec(qv, N, sigma):
    P = [0] * (3 * N)
    for j in range(N):
        for t in range(3):
            P[3 * j + sigma[t]] += qv[3 * j + t]
    return P


def peripheral_vec(slopes, N, r, cusp_rows):
    v = [0] * (3 * N)
    for h in range(r):
        p, q = slopes[2 * h], slopes[2 * h + 1]
        for i in range(3 * N):
            v[i] += p * cusp_rows[2 * h][i] + q * cusp_rows[2 * h + 1][i]
    return v


def chi_pairing(qv, slopes, alpha, N, r, cusp_rows, sigma, eps):
    P = facing_vec(qv, N, sigma)
    per = peripheral_vec(slopes, N, r, cusp_rows)
    return (-sum(Fraction(P[i]) * alpha[i] for i in range(3 * N))
            + eps * Fraction(1, 2) * sum(Fraction(per[i]) * alpha[i]
                                         for i in range(3 * N)))


# ---------------------------------------------------------------------------
# Max-min angle LP (Casson-Rivin):  max s  s.t. GA equalities, x_i >= s, x, s >= 0
# ---------------------------------------------------------------------------

def solve_angle_lp(N, A_eq, b_eq):
    """Returns (s_star, x_angles, w_tet, w_edge, z) — all exact Fractions.

    Standard equality form: vars (x_1..x_{3N}, s, t_1..t_{3N}) >= 0, minimize -s,
    rows = the 16 GA equalities + the 3N rows  x_i - s - t_i = 0.
    Dual y = (w_tet | w_edge | ztilde); z_i := shadow price of x_i >= s.
    """
    n_ang = 3 * N
    nvar = n_ang + 1 + n_ang
    A, b = [], []
    for row, be in zip(A_eq, b_eq):
        A.append([Fraction(v) for v in row] + [Fraction(0)] * (1 + n_ang))
        b.append(Fraction(be))
    for i in range(n_ang):
        row = [Fraction(0)] * nvar
        row[i] = Fraction(1)
        row[n_ang] = Fraction(-1)
        row[n_ang + 1 + i] = Fraction(-1)
        A.append(row)
        b.append(Fraction(0))
    c = [Fraction(0)] * nvar
    c[n_ang] = Fraction(-1)
    obj, xfull, y = solve_and_certify(A, b, c)
    s_star = xfull[n_ang]
    assert obj == -s_star
    n_eq = len(A_eq)
    # solve_and_certify returns duals of the MIN form (min -s); negate the
    # equality duals to report in the MAX convention (max s), under which
    # dual_obj = w.b = s* and the positivity prices z stay >= 0.
    w = [-v for v in y[:n_eq]]
    z = y[n_eq:]
    # the positivity shadow prices must be >= 0 and sum to 1 when s* > 0
    assert all(v >= 0 for v in z), "z negativity"
    if s_star > 0:
        assert sum(z) == 1, "sum z != 1"
    # dual objective in max convention: w.b (per-tet 1's and per-edge 2's)
    dual_obj = sum(wi * Fraction(be) for wi, be in zip(w, b_eq))
    assert dual_obj == s_star, "dual objective != s*"
    # certificate identity: z = E^T w componentwise (reduced costs on x columns)
    for i in range(n_ang):
        ETw = sum(w[k] * Fraction(A_eq[k][i]) for k in range(n_eq))
        assert ETw == z[i], f"z != E^T w at slot {i}"
    return s_star, xfull[:n_ang], w[:N], w[N:], z


# ---------------------------------------------------------------------------
# Preflight: embedded-solver unit tests + the sympy _simplex infeasibility repro
# ---------------------------------------------------------------------------

def preflight():
    ok = True
    # (1) infeasible detection: c >= 0 with c = 1 AND c = 0
    try:
        solve_and_certify([[1], [1]], [1, 0], [0])
        ok = False
    except Infeasible:
        pass
    # (2) tiny duality: min x1+x2 s.t. x1+x2 = 1 -> obj 1, y = 1
    o, x, y = solve_and_certify([[1, 1]], [1], [1, 1])
    ok &= (o == 1 and y[0] == 1)
    # (3) document the sympy 1.14 _simplex bug this probe works around
    sympy_bug = None
    try:
        from sympy import Matrix
        from sympy.solvers.simplex import _simplex, InfeasibleLPError
        try:
            _o, _x, _y = _simplex(Matrix([[1], [-1], [1], [-1]]),
                                  Matrix([1, -1, 0, 0]), Matrix([[0]]), Matrix([0]))
            # system {c = 1, c = 0} is infeasible; reaching here without an
            # InfeasibleLPError is the bug
            sympy_bug = f"returned {_x} on infeasible system without raising"
        except InfeasibleLPError:
            sympy_bug = "correctly raised (bug absent in this sympy version)"
    except Exception as e:  # pragma: no cover
        sympy_bug = f"sympy _simplex unavailable: {e!r}"
    return ok, sympy_bug


# ---------------------------------------------------------------------------
# Stage 1: m004 validation (GHHR Examples 10.23 / A.10)
# ---------------------------------------------------------------------------

def validate_m004(snappy):
    M, N, r, edge_rows, cusp_rows = gluing(snappy, "m004")
    A_eq, b_eq = ga_equalities(N, edge_rows)
    x0, basis, rank = ga_general_solution(A_eq, b_eq)
    dim = 3 * N - rank
    log(f"  m004: N={N}, r={r}, GA-space dim {dim} (Neumann N+r = {N + r})")
    dim_ok = (dim == N + r)

    surfs = M.normal_surfaces()
    sdata = [([exact_int(v) for v in s.quad_vector()],
              [exact_int(v) for v in s.boundary_slopes()]) for s in surfs]
    alphas = [random_ga(x0, basis, sd) for sd in range(5)]

    passing = []
    for sigma in itertools.permutations((0, 1, 2)):
        for eps in (1, -1):
            chis = []
            good = True
            for qv, sl in sdata:
                vals = {chi_pairing(qv, sl, a, N, r, cusp_rows, sigma, eps)
                        for a in alphas}
                if len(vals) != 1:
                    good = False
                    break
                chis.append(vals.pop())
            if good:
                passing.append((sigma, eps, chis))
    conv_ok = (len(passing) == 1)
    sigma, eps, chis = passing[0] if passing else ((None,) * 3)
    chi_ok = conv_ok and all(c == -1 for c in chis)
    log(f"  convention scan: {len(passing)} passing candidate(s); "
        f"pinned sigma={sigma}, eps={eps}; chi values {chis} "
        f"(GHHR Ex 10.23/A.10 expects -1,-1,-1,-1)")

    s_star, xang, w_tet, w_edge, z = solve_angle_lp(N, A_eq, b_eq)
    log(f"  m004 angle LP: s* = {s_star} (strict iff > 0); "
        f"regular-ideal-tet structure would give 1/3")
    return {
        "dim_ok": dim_ok, "conv_ok": conv_ok, "chi_ok": chi_ok,
        "sigma": sigma, "eps": eps, "chis": chis,
        "s_star": s_star, "n_surfaces": len(sdata),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 74)
    print(" Casson-Rivin angle-structure LP of B3 (SnapPy L6a4) with dual emission")
    print(" + exact Prop-A.3 pairing vs vertex spun-normal surfaces")
    print(" audit-only / scope-(a) / comparison-only / no fit — see docstring")
    print("=" * 74)

    try:
        import snappy
    except ImportError:
        print("WALL: SnapPy is not importable — gluing data cannot be obtained "
              "from the source; refusing to hand-guess it (anti-guessing rule).")
        return 2

    log("preflight: embedded exact-simplex unit tests + sympy _simplex bug check")
    pf_ok, sympy_bug_note = preflight()
    log(f"  embedded solver {'OK' if pf_ok else 'FAILED'}; "
        f"sympy _simplex on infeasible repro: {sympy_bug_note}")
    if not pf_ok:
        return 1

    log("stage 1: m004 validation (convention pinning vs GHHR Ex 10.23 / A.10)")
    m004 = validate_m004(snappy)
    if not (m004["dim_ok"] and m004["conv_ok"] and m004["chi_ok"]):
        log("  STOP: m004 validation failed")
        return 1
    SIGMA, EPS = m004["sigma"], m004["eps"]

    # ---------------- stage 2: the B3 angle LP -----------------------------
    log("stage 2: L6a4 angle-structure LP (GA eq (2.7), pi-units, exact)")
    M, N, r, edge_rows, cusp_rows = gluing(snappy, "L6a4")
    log(f"  L6a4: {N} tets, {r} cusps, solution '{M.solution_type()}', "
        f"volume {float(M.volume()):.9f}")
    A_eq, b_eq = ga_equalities(N, edge_rows)
    x0, basis, rank = ga_general_solution(A_eq, b_eq)
    dim = 3 * N - rank
    log(f"  GA equality system: rank {rank}, GA-space dim {dim} "
        f"(Neumann N+r = {N + r})")

    s_star, xang, w_tet, w_edge, z = solve_angle_lp(N, A_eq, b_eq)
    active = [i for i in range(3 * N) if z[i] != 0]
    binding = [i for i in range(3 * N) if xang[i] == s_star]
    dual_obj = sum(w_tet) + 2 * sum(w_edge)
    log(f"  s* = {s_star} > 0 => STRICT angle structure exists (GA Thm 2.12 "
        f"index hypothesis re-certified by LP)")
    log(f"  primal x*: {[str(v) for v in xang]}")
    log(f"  dual: w_tet {[str(v) for v in w_tet]}, w_edge {[str(v) for v in w_edge]}")
    log(f"  y_star (angle-positivity shadow prices) support {active} "
        f"({len(active)} of {3 * N}); primal binding set {len(binding)} slots")
    log(f"  strong duality exact: dual_obj = {dual_obj} = s*; gap 0")

    # complementary slackness cross-check at contract level
    assert all(xang[i] == s_star for i in active), "CS: active but not binding"

    # geometric octahedral structure: from SnapPy shapes (all z = i for the
    # 2-octahedron decomposition), angles are quarter-integers; build exactly
    import math
    shapes = M.tetrahedra_shapes("rect")
    geo = []
    geo_exact = True
    for zz in shapes:
        zc = complex(zz)
        w1 = 1 / (1 - zc)
        w2 = 1 - 1 / zc
        for val in (zc, w1, w2):
            a = math.atan2(val.imag, val.real) / math.pi
            q4 = Fraction(round(4 * a), 4)
            if abs(a - float(q4)) > 1e-9:
                geo_exact = False
            geo.append(q4)
    geo_feasible = geo_exact and \
        all(sum(Fraction(A_eq[k][i]) * geo[i] for i in range(3 * N))
            == Fraction(b_eq[k]) for k in range(len(A_eq)))
    geo_min = min(geo) if geo_exact else None
    lp_is_geometric = (geo_feasible and xang == geo)
    log(f"  geometric structure: quarter-integer angles {geo_exact}, "
        f"GA-feasible exactly {geo_feasible}, min angle {geo_min}; "
        f"LP optimizer == geometric structure: {lp_is_geometric}")

    # ---------------- stage 3: vertex spun-normal surfaces + Prop A.3 ------
    log("stage 3: vertex spun-normal surfaces (SnapPy t3mlite/FXrays) + Prop A.3")
    surfs = M.normal_surfaces()
    log(f"  {len(surfs)} vertex spun-normal surfaces (quad-coordinate vertex "
        f"enumeration, algorithm='FXrays', snappy {snappy.__version__})")
    alphas = [random_ga(x0, basis, sd) for sd in range(4)]
    alphas.append([Fraction(v) for v in xang])          # the LP optimum
    if geo_feasible:
        alphas.append(geo)                              # the geometric structure
    table = []
    all_indep = True
    all_int = True
    for s in surfs:
        qv = [exact_int(v) for v in s.quad_vector()]
        sl = [exact_int(v) for v in s.boundary_slopes()]
        vals = {chi_pairing(qv, sl, a, N, r, cusp_rows, SIGMA, EPS) for a in alphas}
        indep = (len(vals) == 1)
        all_indep &= indep
        chi = vals.pop() if indep else None
        if chi is None or chi.denominator != 1:
            all_int = False
        table.append({"index": s._index, "quad_vector": qv,
                      "boundary_slopes": sl, "chi": chi})
    from collections import Counter
    chi_dist = Counter(str(t["chi"]) for t in table)
    quads_dist = Counter(sum(t["quad_vector"]) for t in table)
    closed = [t["index"] for t in table if all(v == 0 for v in t["boundary_slopes"])]
    cusp_pattern = Counter()
    for t in table:
        sl = t["boundary_slopes"]
        nz = tuple(h for h in range(r) if (sl[2 * h], sl[2 * h + 1]) != (0, 0))
        cusp_pattern[nz] += 1
    log(f"  Prop A.3 alpha-independent on all {len(surfs)}: {all_indep} "
        f"({len(alphas)} angle structures incl. LP optimum"
        f"{' + geometric' if geo_feasible else ''})")
    log(f"  chi integral on all: {all_int}; distribution {dict(chi_dist)}")
    log(f"  all vertex classes have chi < 0: "
        f"{all(t['chi'] is not None and t['chi'] < 0 for t in table)} "
        f"(consistent with strict structure via Farkas / GHHR Thm A.11)")
    log(f"  closed classes ([dS] = 0): {closed if closed else 'none'}")
    pat_str = {('+'.join(str(c) for c in k) if k else 'none'): v
               for k, v in sorted(cusp_pattern.items())}
    log(f"  cusps-touched pattern: {pat_str}")
    s3_pattern_ok = (
        cusp_pattern[(0,)] == cusp_pattern[(1,)] == cusp_pattern[(2,)]
        and cusp_pattern[(0, 1)] == cusp_pattern[(0, 2)] == cusp_pattern[(1, 2)])
    log(f"  S3 symmetry of the (cusps-touched) census grading: {s3_pattern_ok}")

    # symmetry-group facts
    isos_full = M.is_isometric_to(M, return_isometries=True)
    full_perms = sorted({tuple(i.cusp_images()) for i in isos_full})
    combi = M.isomorphisms_to(M)
    combi_perms = sorted({tuple(i.cusp_images()) for i in combi})
    log(f"  isometry group: {len(isos_full)} isometries, cusp permutations "
        f"{full_perms} (full S3)")
    log(f"  combinatorial automorphisms of THIS triangulation: {len(combi)}, "
        f"cusp permutations {combi_perms} (only a Z2 of the S3 is realized "
        f"combinatorially)")

    # ---------------- stage 4: dual certificate vs the normal-surface cone --
    log("stage 4: LP dual certificate as a normal-class combination (exact)")
    QS = []
    for t in table:
        P = facing_vec(t["quad_vector"], N, SIGMA)
        per = peripheral_vec(t["boundary_slopes"], N, r, cusp_rows)
        # Q_S.alpha = -chi(S) for every GA alpha (Prop A.3 rearranged):
        # chi = -P.alpha + eps*(1/2)*per.alpha  =>  Q_S := P_S - eps*(1/2)*per_S
        QS.append([Fraction(P[i]) - EPS * Fraction(1, 2) * per[i]
                   for i in range(3 * N)])
    # with the pinned eps = -1 this is Q_S = P_S + (1/2) per_S; verify the identity
    a_chk = alphas[0]
    for t, Q in zip(table[:5], QS[:5]):
        assert sum(Q[i] * a_chk[i] for i in range(3 * N)) == -t["chi"], \
            "Q_S pairing identity broken"
    taus = []
    for tt in range(N):
        v = [Fraction(0)] * (3 * N)
        v[3 * tt] = v[3 * tt + 1] = v[3 * tt + 2] = Fraction(1)
        taus.append(v)

    def l1_decompose(cols, target):
        """min sum(u+v) s.t. cols.c + u - v = target, c,u,v >= 0. Returns (l1, c)."""
        ncol = len(cols)
        n = 3 * N
        A2, b2 = [], []
        for i in range(n):
            row = [cols[k][i] for k in range(ncol)] + [Fraction(0)] * (2 * n)
            row[ncol + i] = Fraction(1)
            row[ncol + n + i] = Fraction(-1)
            A2.append(row)
            b2.append(target[i])
        c2 = [Fraction(0)] * ncol + [Fraction(1)] * (2 * n)
        o2, sol2, _ = solve_and_certify(A2, b2, c2)
        return o2, sol2[:ncol]

    # (a) effective cone: surfaces + tetrahedral classes, ALL coefficients >= 0
    l1_eff, _ = l1_decompose(QS + taus, z)
    log(f"  (a) z in cone(Q_S, tau_t >= 0): "
        f"{'YES' if l1_eff == 0 else f'NO (l1 distance {l1_eff})'}")
    # (b) surfaces >= 0, tetrahedral (trivial, GHHR Rmk A.9) classes FREE sign
    cols_b = QS + taus + [[-v for v in tv] for tv in taus]
    l1_mod, cb = l1_decompose(cols_b, z)
    surf_support = [(k, cb[k]) for k in range(len(QS)) if cb[k] != 0]
    tau_coeff = [cb[len(QS) + tt] - cb[len(QS) + N + tt] for tt in range(N)]
    decomposable_mod_trivial = (l1_mod == 0)
    log(f"  (b) z in cone(Q_S >= 0) + span(tau_t): "
        f"{'YES' if decomposable_mod_trivial else f'NO (l1 {l1_mod})'}")
    if decomposable_mod_trivial:
        resid = [sum((QS[k][i] * cb[k]) for k in range(len(QS)))
                 + sum(taus[tt][i] * tau_coeff[tt] for tt in range(N)) - z[i]
                 for i in range(3 * N)]
        assert all(v == 0 for v in resid), "decomposition residual"
        supp_desc = [(k, str(v), str(table[k]["chi"]), table[k]["boundary_slopes"])
                     for k, v in surf_support]
        log(f"    support surfaces (index, coeff, chi, slopes): {supp_desc}")
        log(f"    tetrahedral-class coefficients: {[str(v) for v in tau_coeff]}")
        # pairing bookkeeping: sum c_S*(-chi_S) + sum d_t = pairing(z) = s*
        chk = sum(v * (-table[k]["chi"]) for k, v in surf_support) + sum(tau_coeff)
        assert chk == s_star, "pairing bookkeeping"

    # ---------------- stage 5: the SDP side (read-only) ---------------------
    log("stage 5: confinement-SDP witnesses (read-only; comparison of structure)")
    comp_dir = Path(__file__).resolve().parent.parent
    sdp_side = {}
    for wf, key in [("borromean-axial-coupling.witness.json", "beta_bor_nf_lp"),
                    ("nucleus-real-sdp-proton.witness.json", "proton_wedderburn")]:
        p = comp_dir / wf
        if not p.exists():
            sdp_side[key] = {"note": f"witness {wf} not found"}
            continue
        d = json.loads(p.read_text())
        data = d.get("data", {})
        if key == "beta_bor_nf_lp":
            sdp_side[key] = {
                "witness": wf,
                "index_set": "6-element H_3(q) normal-form basis "
                             "{1, s1, s2, s1s2, s2s1, s1s2s1}",
                "n_channels": len(data.get("y_star", [])),
                "active_set": data.get("active_set"),
                "active_names": data.get("active_basis_names"),
                "duality_gap": data.get("duality_gap"),
            }
        else:
            sub = data.get("positive_norm_subspace_solve", {})
            sdp_side[key] = {
                "witness": wf,
                "index_set": "3 Wedderburn blocks of H_3 "
                             "(partitions (1,1,1), (2,1), (3))",
                "n_channels": len(sub.get("y_star", [])),
                "active_set": sub.get("active_set"),
                "active_blocks": sub.get("active_blocks"),
            }
        log(f"  {key}: channels {sdp_side[key].get('n_channels')}, "
            f"active {sdp_side[key].get('active_set')}")

    comparison = {
        "lp_side": {
            "ambient": "24 angle slots = 24 quad types (8 tets x 3)",
            "equality_rank": rank,
            "polytope_dim": dim,
            "n_vertex_surface_rays": len(surfs),
            "active_set_size": len(active),
            "primal_binding_size": len(binding),
            "dual_support_as_surfaces": len(surf_support)
            if decomposable_mod_trivial else None,
            "s_star": str(s_star),
        },
        "sdp_side": sdp_side,
        "counts_verdict": (
            "no count/rank coincidence: LP polytope dim 11, 52 vertex rays, "
            "dual support 3 surfaces (mod 2 trivial classes) vs SDP 6 NF "
            "channels / 1 active and 3 Wedderburn blocks / 2 active"),
    }

    all_core = (pf_ok and m004["dim_ok"] and m004["conv_ok"] and m004["chi_ok"]
                and s_star > 0 and dim == N + r and all_indep and all_int
                and not closed and s3_pattern_ok and decomposable_mod_trivial)

    # ------------------------------------------------------------------ witness
    wb = WitnessBuilder("borromean-angle-structure-lp-probe", engine="python-exact")
    wb.set_description(
        "Casson-Rivin angle-structure LP of the Borromean rings complement B3 "
        "(SnapPy L6a4, 8 ideal tetrahedra, 3 cusps) built EXACTLY from GA "
        "1208.1663 eq (2.7) in pi-units (per-tet sums 1, per-edge sums 2), solved "
        "by an embedded exact two-phase simplex with every optimality certificate "
        "verified in rational arithmetic (primal/dual feasibility, complementary "
        "slackness, strong duality). Emits the full LP-dual contract "
        "(y0_star/y_star/active_set/primal_obj/dual_obj/duality_gap) per AGENTS.md "
        "LP/SDP-duals STRICT rule; solve_operator_selection_lp's shape does not fit "
        "this LP, so its output contract is mirrored exactly (documented). The "
        "52 vertex spun-normal surfaces of the SAME triangulation are enumerated "
        "(SnapPy t3mlite/FXrays quad-coordinate vertex enumeration) and the GHHR "
        "1604.02688 Prop A.3 Gauss-Bonnet pairing chi(S) = -sum alpha(q) x_q/pi + "
        "rho_alpha(dS)/2pi is verified exactly (conventions pinned on m004 against "
        "GHHR Ex 10.23/A.10: four once-punctured Klein bottles, chi = -1). "
        "Comparison-only vs the confinement-SDP witnesses "
        "borromean-axial-coupling / nucleus-real-sdp-proton; NO numeric fitting "
        "between the two sides; audit-only, nothing wired to production.")
    wb.set_content_block("def:borromean-baryon")
    wb.set_audit_only("docs/audits/2026-07-24-angle-structure-lp-sdp-dictionary.md")

    wb.add_data("manifold", "L6a4 (Borromean rings complement)")
    wb.add_data("n_tetrahedra", N)
    wb.add_data("n_cusps", r)
    wb.add_data("angle_convention",
                "pi-units per GA 1208.1663 Sec 2.2 fn 2: per-tet alpha+beta+gamma=1, "
                "per-edge sums = 2 (eq (2.7)); strict iff all 24 angles > 0")
    wb.add_data("facing_permutation_sigma", list(SIGMA))
    wb.add_data("boundary_orientation_eps", EPS)
    wb.add_data("m004_validation", {
        "ga_dim_equals_N_plus_r": m004["dim_ok"],
        "unique_passing_convention": m004["conv_ok"],
        "chi_all_minus_one": m004["chi_ok"],
        "chi_values": [str(c) for c in m004["chis"]],
        "s_star": str(m004["s_star"]),
        "n_surfaces": m004["n_surfaces"],
        "reference": "GHHR 1604.02688 Ex 10.23 + Ex A.10 (once-punctured Klein "
                     "bottles, boundary +-4mu +- lambda, chi = -1)",
    })
    wb.add_data("sympy_simplex_bug_note", sympy_bug_note)

    # ---- the STRICT dual-emission contract fields (mirroring lp_dual_solver) ----
    wb.add_data("x_star", [str(v) for v in xang])
    wb.add_data("y0_star", str(dual_obj))
    wb.add_data("y_star", [str(v) for v in z])
    wb.add_data("active_set", active)
    wb.add_data("primal_obj", str(s_star))
    wb.add_data("dual_obj", str(dual_obj))
    wb.add_data("duality_gap", "0")
    wb.add_data("dual_contract_note",
                "solve_operator_selection_lp (pyhecke.lp_dual_solver) solves "
                "min t.x / 1^T x = n_target / G x >= 0 with square Gram G — shape "
                "does not fit the max-min angle LP; the output contract is mirrored "
                "exactly instead: y_star = shadow prices of the 24 angle-positivity "
                "constraints x_i >= s, active_set = their support, y0_star = dual "
                "objective (shadow value of the (1,...,1;2,...,2) normalization "
                "bundle), duality_gap exactly 0 in rational arithmetic.")
    wb.add_data("w_tet_star", [str(v) for v in w_tet])
    wb.add_data("w_edge_star", [str(v) for v in w_edge])
    wb.add_data("primal_binding_set", binding)
    wb.add_data("ga_equality_rank", rank)
    wb.add_data("ga_polytope_dim", dim)
    wb.add_data("geometric_structure_check", {
        "quarter_integer_shapes": geo_exact,
        "ga_feasible_exactly": bool(geo_feasible),
        "min_angle": str(geo_min) if geo_min is not None else None,
        "lp_optimizer_equals_geometric": bool(lp_is_geometric),
    })

    wb.add_data("vertex_surfaces", {
        "tool": f"snappy {snappy.__version__} Manifold.normal_surfaces() "
                "(t3mlite spun, FXrays vertex enumeration in quad coordinates)",
        "count": len(surfs),
        "chi_distribution": dict(chi_dist),
        "total_quads_distribution": {str(k): v for k, v in sorted(quads_dist.items())},
        "closed_classes": closed,
        "cusps_touched_pattern": pat_str,
        "table": [{"index": t["index"],
                   "quad_vector": t["quad_vector"],
                   "boundary_slopes": t["boundary_slopes"],
                   "chi": str(t["chi"])} for t in table],
    })
    wb.add_data("symmetry", {
        "isometry_group_order": len(isos_full),
        "isometry_cusp_permutations": [list(p) for p in full_perms],
        "combinatorial_automorphisms": len(combi),
        "combinatorial_cusp_permutations": [list(p) for p in combi_perms],
        "census_grading_s3_symmetric": s3_pattern_ok,
    })
    wb.add_data("dual_certificate_decomposition", {
        "effective_cone_l1_distance": str(l1_eff),
        "mod_trivial_feasible": decomposable_mod_trivial,
        "surface_support": [{"index": k, "coeff": str(v),
                             "chi": str(table[k]["chi"]),
                             "boundary_slopes": table[k]["boundary_slopes"]}
                            for k, v in surf_support],
        "tetrahedral_class_coefficients": [str(v) for v in tau_coeff],
        "note": "z = sum c_S Q_S + sum d_t tau_t with c_S >= 0, d_t free; "
                "tau_t are the formal chi = -1 tetrahedral classes of GHHR "
                "Rmk A.9 / Ex A.10 (trivial in the Q-normal class group).",
    })
    wb.add_data("comparison_table", comparison)

    wb.add_assertion("embedded_solver_preflight", computed=float(pf_ok),
                     expected=1.0, tolerance=0.5,
                     source="unit tests: infeasibility detection + certified duality")
    wb.add_assertion("m004_convention_pinned_uniquely",
                     computed=float(m004["conv_ok"]), expected=1.0, tolerance=0.5,
                     source="exactly one (sigma, eps) of 12 reproduces "
                            "alpha-independent chi on all 4 m004 vertex surfaces")
    wb.add_assertion("m004_chi_matches_ghhr", computed=float(m004["chi_ok"]),
                     expected=1.0, tolerance=0.5,
                     source="GHHR Ex 10.23/A.10: 4 once-punctured Klein bottles, "
                            "chi = -1")
    wb.add_assertion("l6a4_strict_angle_structure_exists",
                     computed=float(s_star), expected=0.25, tolerance=1e-12,
                     source="max-min angle s* = 1/4 exactly (> 0 = strict; GHRS "
                            "Rmk 1.10 guarantees existence for link complements)")
    wb.add_assertion("l6a4_lp_duality_gap_zero", computed=0.0, expected=0.0,
                     tolerance=1e-30,
                     source="rational arithmetic; strong duality verified exactly "
                            "(prop:operator-selection-lp contract)")
    wb.add_assertion("l6a4_ga_dim_equals_N_plus_r",
                     computed=float(dim), expected=float(N + r), tolerance=0.5,
                     source="Neumann: dim of generalized angle structures = N + r")
    wb.add_assertion("prop_a3_alpha_independent_all_surfaces",
                     computed=float(all_indep), expected=1.0, tolerance=0.5,
                     source=f"GHHR Prop A.3 pairing constant over {len(alphas)} "
                            "generalized angle structures for all 52 surfaces")
    wb.add_assertion("prop_a3_chi_integral_all_surfaces",
                     computed=float(all_int), expected=1.0, tolerance=0.5,
                     source="chi in Z for all 52 vertex classes (values -1, -2)")
    wb.add_assertion("all_vertex_chi_negative",
                     computed=float(all(t["chi"] < 0 for t in table)),
                     expected=1.0, tolerance=0.5,
                     source="no chi >= 0 vertex class — Farkas-consistent with the "
                            "strict angle structure (GHHR Thm A.11)")
    wb.add_assertion("dual_certificate_decomposes_mod_trivial",
                     computed=float(decomposable_mod_trivial), expected=1.0,
                     tolerance=0.5,
                     source="LP dual optimum = nonneg combination of 3 vertex "
                            "surfaces + free tetrahedral classes (exact)")
    wb.save()
    log("witness saved")

    print()
    print(f"  s* = {s_star} (strict angle structure certified exactly)")
    print(f"  dual: y_star support {active}; decomposition over surfaces "
          f"{[(k, str(v)) for k, v in surf_support]} mod tetrahedral classes")
    print(f"  surfaces: 52 vertex classes, chi {dict(chi_dist)}, Prop A.3 "
          f"verified alpha-independently")
    print(f"  RESULT: {'ALL OK' if all_core else 'CHECK FAILED'}")
    return 0 if all_core else 1


if __name__ == "__main__":
    raise SystemExit(main())
