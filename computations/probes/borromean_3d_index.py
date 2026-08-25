#!/usr/bin/env python3
"""borromean_3d_index.py — the GGM/GHHR 3D-index of the Borromean rings complement.

Executes idea B1 of docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md:
I_B3, the 3D-index of the Borromean rings complement (SnapPy `L6a4`, the nucleon
carrier B3 of the QOU framework), assembled on the triality-validated tetrahedron
index machinery of figure_eight_3d_index.py (#3868 / #3805 thread).

SOURCES (primary, no guessed gluing data):
  [GHHR]  Garoufalidis-Hodgson-Hoffman-Rubinstein, "The 3D-index and normal
          surfaces" (arXiv:1604.02688, library/arxiv-1604.02688v1/1604.02688v1.pdf), Section 4:
          for an ideal triangulation T with n tetrahedra and r cusps,

              I_T([gamma])(q) = sum_{k in Z^{n-r}} q^{sum_i k_i}
                                prod_{j=1}^{n} J_D(a_j(k,gamma), b_j(k,gamma), c_j(k,gamma)),

          where the per-tetrahedron charge triples (a_j, b_j, c_j) are the entries of
          the linear combination  sum_i k_i E_i + sum_h (p_h M_h + q_h L_h)  of the
          rows of the gluing matrix (E_i = edge rows; M_h, L_h = meridian/longitude
          rows of cusp h; gamma = sum_h p_h mu_h + q_h lam_h), and the r edge weights
          set to zero must be chosen per [GHRS].  The gluing matrix "is also given by
          the gluing_equations() function in SnapPy" (GHHR Section 3.1).
  [GHRS]  Garoufalidis-Hodgson-Rubinstein-Segerman, "1-efficient triangulations and
          the index of a cusped hyperbolic 3-manifold" (arXiv:1303.5278,
          library/arxiv-1303.5278v1/1303.5278v1.pdf):
          - Section 4.5 eq (17) + Section 4.6 Thm 4.3 / Rmk 4.4 / Rmk 4.6: the r
            EXCLUDED edges must leave the remaining n-r edge rows an INTEGER BASIS
            of the integer row space Lambda of the Neumann-Zagier matrix (A|B);
            existence via a maximal tree with 1- or 3-cycle in the edge-cusp graph;
            the index is independent of which valid choice is made (Rmk 4.6).
            This probe enforces the integer-basis condition directly by integer
            linear algebra (solve each excluded row as an integer combination of
            the kept rows) rather than hand-picking edges.
          - Thm 1.1 (well-defined iff index structure; 2-3 move invariance),
            Thm 1.2 (index structure iff 1-efficient), Thm 1.5 + Rmk 1.6 (a strict
            angle structure => 1-efficient), Rmk 1.10 (all link complements in S^3
            admit a strict-angle-structure triangulation), Thm 1.8 (topological
            invariant on X^EP).  SnapPy reports the L6a4 triangulation as
            "all tetrahedra positively oriented" — the arguments of the geometric
            shapes give a strict angle structure, so the index is well-defined.

MACHINERY REUSE. The Q = q^{1/2} series kernel (dict-based _mul/_inv/_qpoch), the
tetrahedron index I_D and the symmetric index J_D below are adapted from
computations/probes/figure_eight_3d_index.py (the 4_1 probe validated against GHHR
Example 4.1 to q^10), generalized only by (a) an explicit per-call series cap
instead of the fixed HI, and (b) a correct termination bound for the I_D loop.
J_D's S_3-invariant reduction (min-shift + first-zero removal) is exactly the
triality pinned in docs/audits/2026-07-18-tetrahedron-index-triality-pin.md.

VALIDATION LADDER (this probe, in order — each gates the next):
  1. m004 (figure-eight) general-machinery check: rebuild the index from SnapPy's
     OWN gluing_equations() rows for m004 (which differ from GHHR's Ex 4.1 table in
     quad and peripheral conventions) with the general n,r code, and match
     figure_eight_3d_index.index(x,y) exactly to q^10 on 4 peripheral classes.
  2. I_B3(0,0,0): exact integer q-series via the Z^5 lattice sum (n=8, r=3) with
     the per-summand min-degree bound  D(k) = 2*sum(k) + sum_j nu_j(k)  (exact:
     leading coefficients of J_D are +-1), enumerated over l-infinity shells with
     a 3-consecutive-empty-shell stopping rule.
  3. Self-tests: (i) genuine power series (no negative q-powers; GHHR Cor 10.21);
     (ii) constant term 1; (iii) S_3 cusp-permutation symmetry of I_B3(b) on
     nonzero peripheral orbits; (iv) triangulation independence under SnapPy
     randomized retriangulation (2-3 moves; GHRS Thm 1.1(b)) when a positively
     oriented retriangulation is found.

SCOPE (STRICT). Audit-only; scope-(a); comparison-only; NO FIT; nothing wired to
production.  The deliverable is the invariant, its graded structure, and the
self-test results.  Deliberately NO comparison to F_Bor, tr_M, rho(B3), or any
mass/binding observable in this probe — a canonical bridge from index coefficients
to the QOU density objects does not exist yet and must be derived, not fitted
(AGENTS.md anti-laundering + formalize-first).
"""
from __future__ import annotations

import itertools
import sys
import time
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------------------
# Q = q^{1/2} power-series kernel (dicts power -> integer coefficient).
# Adapted from computations/probes/figure_eight_3d_index.py (validated vs GHHR
# Ex 4.1); generalized with an explicit cap argument.
# ---------------------------------------------------------------------------

def _mul(a, b, cap):
    r = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            p = pa + pb
            if p <= cap:
                r[p] = r.get(p, 0) + ca * cb
    return {p: c for p, c in r.items() if c}


def _inv(a, cap):
    # constant term of a must be 1 (true for the (q;q)_n products used here)
    r = {0: 1}
    for p in range(1, cap + 1):
        r[p] = -sum(a.get(k, 0) * r.get(p - k, 0) for k in range(1, p + 1))
    return r


@lru_cache(maxsize=None)
def _qpoch(n, cap):
    """(q;q)_n as a Q-series dict (tuple-frozen for caching)."""
    r = {0: 1}
    for j in range(1, n + 1):
        r = _mul(r, {0: 1, 2 * j: -1}, cap)
    return tuple(sorted(r.items()))


@lru_cache(maxsize=None)
def _inv_qpoch_product(n, n_plus_e, cap):
    """1/((q)_n (q)_{n+e}) to depth cap."""
    return tuple(sorted(_inv(
        _mul(dict(_qpoch(n, cap)), dict(_qpoch(n_plus_e, cap)), cap), cap).items()))


@lru_cache(maxsize=None)
def I_D(m, e, cap):
    """Tetrahedron index I_Delta(m,e)(q) as a Q-dict, coefficients to Q^cap.

    Only called with m <= 0 here (J_D's reduction guarantees it), where the
    exponent expo(n) = n(n+1) - (2n+e)m is monotone increasing in n, so the
    loop terminates exactly when expo > cap.
    """
    assert m <= 0, "I_D called with m > 0 — J_D reduction should prevent this"
    lo = max(0, -e)
    tot = {}
    n = lo
    while True:
        expo = n * (n + 1) - (2 * n + e) * m
        if expo > cap:
            break
        for p, c in _inv_qpoch_product(n, n + e, cap - expo):
            pp = p + expo
            if pp <= cap:
                tot[pp] = tot.get(pp, 0) + ((-1) ** n) * c
        n += 1
    return {p: c for p, c in tot.items() if c}


def J_D(a, b, c, cap):
    """Symmetric tetrahedron index J_Delta(a,b,c) (GHHR eq 4/6) to Q^cap.

    Reduction (from figure_eight_3d_index.py): shift by m = min(a,b,c) using
    J_D(a+s,b+s,c+s) = (-q^{1/2})^{-s} J_D(a,b,c), then drop the first zero of
    the shifted triple and use J_D(A,B,0) = I_D(-A,B) (eq 6).  The remaining
    zero-position cases reduce to the same I_D call via the S_3 triality pinned
    in the 2026-07-18 triality audit (cyclic (-q^{1/2})^m + reflection
    I_D(m,e) = I_D(-e,-m)); J_D is fully S_3-symmetric (checked numerically in
    preflight below).
    """
    m = min(a, b, c)
    sh = [a - m, b - m, c - m]
    sh.remove(0)
    A, B = sh  # both >= 0
    base = I_D(-A, B, cap + m)  # output degree p - m <= cap  =>  p <= cap + m
    sign = -1 if (m % 2) else 1  # sign of (-q^{1/2})^{-m}
    out = {}
    for p, cc in base.items():
        pp = p - m
        if pp <= cap:
            out[pp] = out.get(pp, 0) + sign * cc
    return {p: cc for p, cc in out.items() if cc}


def nu_Q(a, b, c):
    """Exact minimum Q-degree of J_D(a,b,c): A*B - m with m = min, {A,B} the
    two largest min-shifted entries (leading coefficient is +-1, never 0)."""
    m = min(a, b, c)
    s = sorted((a - m, b - m, c - m))
    return s[1] * s[2] - m


# ---------------------------------------------------------------------------
# General GHHR Section-4 index from SnapPy gluing data
# ---------------------------------------------------------------------------

class IndexTriangulation:
    """GHHR eq (15)/(16) machinery for a SnapPy manifold.

    Holds the (n+2r) x 3n gluing matrix, selects the r excluded edges by the
    GHRS Section 4.6 integer-basis condition, and evaluates I_T(b) for
    b = (p_1, q_1, ..., p_r, q_r) in H_1(dM; Z) = Z^{2r}.
    """

    def __init__(self, manifold):
        self.M = manifold
        self.n = manifold.num_tetrahedra()
        self.r = manifold.num_cusps()
        G = manifold.gluing_equations()  # rows: n edges, then (mu, lam) per cusp
        rows = [[int(x) for x in row] for row in G.data] if hasattr(G, "data") else \
               [[int(G[i, j]) for j in range(3 * self.n)] for i in range(G.nrows())]
        assert len(rows) == self.n + 2 * self.r
        self.edge_rows = rows[: self.n]
        self.cusp_rows = rows[self.n:]  # 2r rows: mu_1, lam_1, mu_2, lam_2, ...
        self.basic_edges = self._choose_basic_edges()

    # -- GHRS Section 4.6: integer-basis edge selection ---------------------
    def _nz_rows(self):
        """Neumann-Zagier (A|B) reduction of the edge rows: (a-c | b-c)."""
        out = []
        for row in self.edge_rows:
            a = row[0::3]
            b = row[1::3]
            c = row[2::3]
            out.append([ai - ci for ai, ci in zip(a, c)] +
                       [bi - ci for bi, ci in zip(b, c)])
        return out

    def _choose_basic_edges(self):
        """First (lexicographic) set of n-r edges whose NZ rows form an
        integer basis of the row lattice Lambda (GHRS Thm 4.3 / Rmk 4.6)."""
        from sympy import Matrix
        nz = self._nz_rows()
        full = Matrix(nz)
        # sanity: sum over h of C_h E_i = 0 implies sum of ALL rows = 0
        # (each column of the incidence matrix C sums to 2)
        colsums = [sum(nz[i][j] for i in range(self.n)) for j in range(2 * self.n)]
        assert colsums == [0] * (2 * self.n), \
            "NZ edge rows do not sum to zero — reduction convention broken"
        rank = full.rank()
        assert rank == self.n - self.r, f"NZ rank {rank} != n-r = {self.n - self.r}"
        for excl in itertools.combinations(range(self.n), self.r):
            kept = [i for i in range(self.n) if i not in excl]
            A = Matrix([nz[i] for i in kept])
            if A.rank() != self.n - self.r:
                continue
            ok = True
            for s in excl:
                v = Matrix(nz[s])
                try:
                    sol, params = A.T.gauss_jordan_solve(v)
                except ValueError:
                    ok = False
                    break
                if len(params) or any(x.q != 1 for x in sol):
                    ok = False
                    break
            if ok:
                return kept
        raise RuntimeError("no integer-basis edge subset found (GHRS Thm 4.3 "
                           "guarantees one exists — check gluing data)")

    # -- charge assignment and lattice sum ----------------------------------
    def _charges(self, kvec, b):
        """Per-tetrahedron (a_j, b_j, c_j) for full edge-weight vector kvec
        (length n) and peripheral class b (length 2r)."""
        n = self.n
        tot = [0] * (3 * n)
        for i, ki in enumerate(kvec):
            if ki:
                row = self.edge_rows[i]
                for j in range(3 * n):
                    tot[j] += ki * row[j]
        for l, bl in enumerate(b):
            if bl:
                row = self.cusp_rows[l]
                for j in range(3 * n):
                    tot[j] += bl * row[j]
        return [(tot[3 * j], tot[3 * j + 1], tot[3 * j + 2]) for j in range(n)]

    def summand_min_degree(self, kvec, b):
        """Exact min Q-degree of the summand at kvec: 2*sum(k) + sum_j nu_j."""
        return 2 * sum(kvec) + sum(nu_Q(*t) for t in self._charges(kvec, b))

    def admissible_lattice(self, b, hi, empty_shells_to_stop=3, rmax=40):
        """Enumerate k in the basic-edge sublattice with min degree <= hi.

        Vectorized (numpy) shells in l-infinity norm; stop after
        `empty_shells_to_stop` consecutive shells contribute nothing (the
        index-structure convergence theorem [GHRS Thm 1.2] makes the min
        degree proper — empirically Dmin(shell R) = 2R for L6a4, LINEAR in
        the l-infinity radius, so shells stay populated up to R ~ hi/2 and
        pure-Python enumeration is infeasible).  Returns
        (list of full k-vectors, stop radius).
        """
        import numpy as np
        dim = len(self.basic_edges)
        Eb = np.array([self.edge_rows[i] for i in self.basic_edges])  # dim x 3n
        P = np.zeros(3 * self.n, dtype=np.int64)
        for l, bl in enumerate(b):
            if bl:
                P += bl * np.array(self.cusp_rows[l])
        adm = []
        empty_run = 0
        R = 0
        while R <= rmax:
            box = np.array(list(itertools.product(range(-R, R + 1), repeat=dim)),
                           dtype=np.int64)
            if R:
                box = box[np.abs(box).max(axis=1) == R]
            C3 = (box @ Eb + P).reshape(len(box), self.n, 3)
            m = C3.min(axis=2)
            sh = np.sort(C3 - m[:, :, None], axis=2)
            nu = sh[:, :, 1] * sh[:, :, 2] - m
            D = 2 * box.sum(axis=1) + nu.sum(axis=1)
            good = box[D <= hi]
            for kk in good:
                kvec = [0] * self.n
                for pos, ki in zip(self.basic_edges, kk):
                    kvec[pos] = int(ki)
                adm.append(kvec)
            empty_run = 0 if len(good) else empty_run + 1
            if empty_run >= empty_shells_to_stop:
                break
            R += 1
        else:
            raise RuntimeError(f"lattice enumeration hit rmax={rmax}")
        return adm, R

    def index(self, b, qmax, progress_every=200):
        """I_T(b)(q) as an exact Q-dict, coefficients through q^qmax."""
        hi = 2 * qmax
        adm, rstop = self.admissible_lattice(b, hi)
        log(f"    lattice: {len(adm)} admissible vectors (stop radius {rstop}) "
            f"for b={tuple(b)} to q^{qmax}")
        tot = {}
        for idx, kvec in enumerate(adm):
            if progress_every and idx and idx % progress_every == 0:
                el = time.time() - T0
                log(f"    summand {idx}/{len(adm)} (elapsed {el:.0f}s, "
                    f"ETA +{el / idx * (len(adm) - idx):.0f}s)")
            charges = self._charges(kvec, b)
            shift = 2 * sum(kvec)  # q^{sum k_i} = Q^{2 sum k_i}
            cap = hi - shift
            nus = [nu_Q(*t) for t in charges]
            rest = sum(nus)  # min degree of the factors not yet multiplied
            done = 0         # min degree of the running product
            prod = {0: 1}
            for t, nu in zip(charges, nus):
                rest -= nu
                # terms of the running product above cap - rest cannot reach
                # total degree <= cap once the remaining factors' min degrees
                # are added; the factor itself is only needed to depth
                # cap - rest - done
                fac = J_D(*t, cap - rest - done)
                prod = _mul(prod, fac, cap - rest)
                done += nu
                if not prod:
                    break
            for p, cc in prod.items():
                pp = p + shift
                if pp <= hi:
                    tot[pp] = tot.get(pp, 0) + cc
        return {p: c for p, c in tot.items() if c}


def qcoeffs(d, nq):
    """Integer q-coefficients [q^0 ... q^{nq-1}] from a Q-dict."""
    return [d.get(2 * j, 0) for j in range(nq)]


def half_odd_part(d):
    """Any odd-Q (half-integer q) terms present?  (Expected none for integral b.)"""
    return {p: c for p, c in d.items() if p % 2}


def neg_part(d):
    return {p: c for p, c in d.items() if p < 0}


# ---------------------------------------------------------------------------
# Preflight: numeric identities on the series kernel itself
# ---------------------------------------------------------------------------

def preflight():
    """(1) reflection triality I_D(m,e) = I_D(-e,-m) on m<=0 pairs;
    (2) full S_3 invariance of J_D; (3) eq-6 leading term q^{AB/2}."""
    cap = 16
    ok = True
    for (m, e) in [(0, 0), (0, 2), (-1, 1), (-2, 3), (-3, 0), (-2, -1)]:
        if -e > 0 or m > 0:
            continue
        ok &= I_D(m, e, cap) == I_D(-e, -m, cap)
    for (a, b, c) in [(0, 1, 2), (2, 1, 0), (1, 3, 2), (-1, 2, 4), (-2, -1, 3),
                      (0, 0, 3), (2, 2, 2), (-3, 1, 1)]:
        ref = J_D(a, b, c, cap)
        for perm in itertools.permutations((a, b, c)):
            ok &= J_D(*perm, cap) == ref
    for (A, B) in [(1, 1), (2, 1), (3, 2)]:
        s = I_D(-A, B, cap)
        ok &= min(s) == A * B and s[min(s)] == 1
    return ok


# ---------------------------------------------------------------------------
# Stage 1: m004 general-machinery validation against the dedicated 4_1 probe
# ---------------------------------------------------------------------------

def validate_m004(snappy):
    import figure_eight_3d_index as fig8
    M = snappy.Manifold("m004")
    tri = IndexTriangulation(M)
    log(f"  m004: n={tri.n}, r={tri.r}, basic edges {tri.basic_edges}, "
        f"solution '{M.solution_type()}'")
    targets = {(0, 0): None, (0, 1): None, (2, 0): None, (1, 0): None}
    mapping = {}
    all_ok = True
    for (x, y) in targets:
        ref = qcoeffs(fig8.index(x, y), 11)
        got = None
        for (sx, sy) in itertools.product((1, -1), repeat=2):
            cand = qcoeffs(tri.index((sx * x, sy * y), 10, progress_every=0), 11)
            if cand == ref:
                got = (sx, sy)
                break
        mapping[(x, y)] = got
        ok = got is not None
        all_ok &= ok
        log(f"  m004 class (x,y)=({x},{y}): general machinery "
            f"{'MATCHES fig8 probe to q^10 (sign map ' + str(got) + ')' if ok else 'MISMATCH'}")
    return all_ok, mapping


# ---------------------------------------------------------------------------
# Stage 2+3: the Borromean index
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 74)
    print(" GHHR 3D-index of the Borromean rings complement (SnapPy L6a4)")
    print(" audit-only / scope-(a) / comparison-only / no fit — see docstring")
    print("=" * 74)

    try:
        import snappy
    except ImportError:
        print("WALL: SnapPy is not importable — gluing data cannot be obtained "
              "from the source; refusing to hand-guess it (anti-guessing rule). "
              "Install snappy and re-run.")
        return 2

    log("preflight: I_D reflection + J_D S_3 invariance + eq-6 leading term")
    pf = preflight()
    log(f"  preflight {'OK' if pf else 'FAILED'}")
    if not pf:
        return 1

    log("stage 1: m004 general-machinery validation (SnapPy NZ rows, general code)")
    m004_ok, m004_map = validate_m004(snappy)
    if not m004_ok:
        log("  STOP: general machinery does not reproduce the validated 4_1 index")
        return 1

    log("stage 2: Borromean rings complement L6a4")
    M = snappy.Manifold("L6a4")
    vol = float(M.volume())
    log(f"  L6a4: {M.num_tetrahedra()} tets, {M.num_cusps()} cusps, "
        f"solution '{M.solution_type()}', volume {vol:.9f} "
        f"(2 x octahedron = 7.327724753)")
    pos_oriented = M.solution_type() == "all tetrahedra positively oriented"
    tri = IndexTriangulation(M)
    log(f"  basic edges (GHRS 4.6 integer-basis choice): {tri.basic_edges} "
        f"(excluded: {[i for i in range(tri.n) if i not in tri.basic_edges]})")

    QMAX_MAIN = 10
    QMAX_SYM = 6

    log(f"  computing I_B3(0) to q^{QMAX_MAIN} (Z^{len(tri.basic_edges)} lattice sum)")
    I0 = tri.index((0, 0, 0, 0, 0, 0), QMAX_MAIN)
    c0 = qcoeffs(I0, QMAX_MAIN + 1)
    log(f"  I_B3(0) = {c0}")
    odd0 = half_odd_part(I0)
    neg0 = neg_part(I0)

    # self-test (i): genuine power series
    t1 = not neg0
    # self-test (ii): constant term 1
    t2 = c0[0] == 1 if c0 else False
    log(f"  self-test (i) no negative q-powers: {t1}"
        + ("" if t1 else f"  neg: {neg0}"))
    log(f"  self-test (ii) constant term 1: {t2}")
    log(f"  half-integer-power terms (expected none for integral b): "
        f"{odd0 if odd0 else 'none'}")

    # self-test (iii): S_3 cusp-permutation symmetry on nonzero orbits
    log(f"stage 3: S_3 cusp-permutation symmetry (to q^{QMAX_SYM}) — 2 orbits")
    orbits = {
        "mu_h": [(1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)],
        "mu_h+lam_h": [(1, 1, 0, 0, 0, 0), (0, 0, 1, 1, 0, 0), (0, 0, 0, 0, 1, 1)],
    }
    t3 = True
    orbit_series = {}
    orbit_notes = {}
    for name, obs in orbits.items():
        series = [tri.index(b, QMAX_SYM) for b in obs]
        coefs = [qcoeffs(s, QMAX_SYM + 1) for s in series]
        odd = [sorted(half_odd_part(s).items()) for s in series]
        direct = all(s == series[0] for s in series[1:])
        note = "direct"
        if not direct:
            # cusp curves may differ by orientation between SnapPy framings;
            # I(b) with a per-cusp sign flip is the same class under the
            # symmetry that reverses that component — try sign variants
            flipped_ok = True
            for b in obs[1:]:
                variants = []
                for sgn in itertools.product((1, -1), repeat=3):
                    bb = tuple(sgn[h // 2] * v for h, v in enumerate(b))
                    variants.append(tri.index(bb, QMAX_SYM))
                flipped_ok &= any(v == series[0] for v in variants)
            direct = flipped_ok
            note = "up to per-cusp orientation flip" if flipped_ok else "FAILED"
        t3 &= direct
        orbit_series[name] = coefs[0]
        orbit_notes[name] = note
        log(f"  orbit {name}: coeffs {coefs[0]}"
            + (f" (odd-Q part {odd[0]})" if odd[0] else "")
            + f" — S_3 {'symmetric (' + note + ')' if direct else 'BROKEN'}")

    # self-test (iv, optional): 2-3-move independence via retriangulation
    log("stage 4 (optional): retriangulation independence (GHRS Thm 1.1(b))")
    t4 = None
    t4_note = "skipped (no positively oriented retriangulation found)"
    for attempt in range(6):
        M2 = M.copy()
        M2.randomize()
        if M2.solution_type() != "all tetrahedra positively oriented":
            continue
        tri2 = IndexTriangulation(M2)
        log(f"  retriangulation: {tri2.n} tets (attempt {attempt}), computing to q^{QMAX_SYM}")
        I0b = tri2.index((0,) * (2 * tri2.r), QMAX_SYM)
        t4 = qcoeffs(I0b, QMAX_SYM + 1) == c0[: QMAX_SYM + 1]
        t4_note = (f"{tri2.n}-tet retriangulation, I(0) to q^{QMAX_SYM} "
                   f"{'matches' if t4 else 'MISMATCH'}")
        break
    log(f"  {t4_note}")

    all_core = t1 and t2 and t3 and m004_ok and pf and pos_oriented

    # ------------------------------------------------------------------ witness
    wb = WitnessBuilder("borromean-3d-index", engine="python-exact")
    wb.set_description(
        "GHHR 3D-index of the Borromean rings complement B3 (SnapPy L6a4, 8 ideal "
        "tetrahedra, 3 cusps, positively oriented => strict angle structure => "
        "1-efficient => index well-defined; GHRS 1303.5278 Thm 1.5/1.2/1.1, Rmk 1.10). "
        "General GHHR 1604.02688 Section-4 gluing formula: I_T(b) = sum over the Z^5 "
        "basic-edge sublattice (GHRS 4.6 integer-basis choice, machine-verified) of "
        "q^{sum k} times the product of 8 symmetric tetrahedron indices J_D with "
        "charges linear in (k, b). Machinery validated by rebuilding the 4_1 index "
        "from SnapPy m004 NZ data and matching the Ex-4.1-validated probe to q^10. "
        "Audit-only; scope-(a); comparison-only; NO comparison to F_Bor / masses in "
        "this probe (no canonical index->rho bridge is derived; none is fitted).")
    wb.set_content_block("def:borromean-baryon")
    wb.set_audit_only("docs/audits/2026-07-18-borromean-3d-index.md")
    wb.add_data("manifold", "L6a4 (Borromean rings complement)")
    wb.add_data("n_tetrahedra", tri.n)
    wb.add_data("n_cusps", tri.r)
    wb.add_data("volume", vol)
    wb.add_data("solution_type", M.solution_type())
    wb.add_data("basic_edges", list(tri.basic_edges))
    wb.add_data("I_B3_0_q0_qN", c0)
    wb.add_data("I_B3_0_max_order", QMAX_MAIN)
    for name, coefs in orbit_series.items():
        wb.add_data(f"I_B3_{name.replace('+', '_plus_')}_q0_q{QMAX_SYM}", coefs)
        wb.add_data(f"S3_orbit_{name.replace('+', '_plus_')}_note", orbit_notes[name])
    wb.add_data("m004_general_machinery_sign_map",
                {str(k): str(v) for k, v in m004_map.items()})
    wb.add_data("formula",
                "I_T(b) = sum_{k in Z^{n-r}} q^{sum_i k_i} prod_j J_D(charges_j(k,b))"
                "  (GHHR 1604.02688 eq 15/16; GHRS 1303.5278 eq 17 + Thm 4.3)")
    wb.add_assertion("m004_general_machinery_matches_validated_probe",
                     computed=float(m004_ok), expected=1.0, tolerance=0.5,
                     source="4 peripheral classes of m004 from SnapPy NZ rows match "
                            "figure_eight_3d_index.py (GHHR Ex 4.1) to q^10")
    wb.add_assertion("index_is_power_series", computed=float(t1), expected=1.0,
                     tolerance=0.5, source="no negative q-powers (GHHR Cor 10.21)")
    wb.add_assertion("constant_term_is_one", computed=float(t2), expected=1.0,
                     tolerance=0.5, source="I_B3(0)(0) = 1")
    wb.add_assertion("s3_cusp_permutation_symmetry", computed=float(t3), expected=1.0,
                     tolerance=0.5,
                     source=f"I_B3(b) invariant under permuting the three cusp Z^2 "
                            f"blocks on 2 nonzero orbits to q^{QMAX_SYM}")
    if t4 is not None:
        wb.add_assertion("retriangulation_independence", computed=float(t4),
                         expected=1.0, tolerance=0.5, source=t4_note)
    wb.save()
    log("witness saved")

    print()
    print(f"  I_B3(0) = {c0}  (exact integers, q^0..q^{QMAX_MAIN})")
    print(f"  self-tests: (i) power series {t1}; (ii) const 1 {t2}; "
          f"(iii) S_3 {t3}; (iv) retriangulation "
          f"{t4 if t4 is not None else 'skipped'}")
    print(f"  RESULT: {'ALL OK' if all_core else 'CHECK FAILED'}")
    return 0 if all_core else 1


if __name__ == "__main__":
    raise SystemExit(main())
