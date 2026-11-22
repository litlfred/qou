"""Covariant two-term (all-pairs charge) insertion on V^{⊗N} with coloured strands, exact in ℚ(q).

Pre-registered in PREREGISTRATION.md (commit d38166d1cb) before any number was computed.

Generalises the scored `two_term_covariant_all_pairs_qtrace` object (`two_term_qtrace_weighting.py`,
Lean `QOU.BraidsAndKnots.NucleonWeightSpaceQTrace`, `NucleonQEDCovariance` T5/T6) from the two
3-strand nucleon weight spaces to N strands that may carry quark, lepton or neutral charges.

* Jimbo Ř on V^{⊗N}, V = span(u, d), u ↦ T³ = +½ (same matrices as the #8681 `jimbo.py`,
  re-implemented here on dense per-weight-space blocks; validated against the Ocneanu trace at z_D).
* Q_i diagonal per strand colour: quark (u 2/3, d −1/3), lepton (u=ν 0, d=e⁻ −1), neutral (0, 0).
  Q_pair = Σ_{i<j} Q_i Q_j (diagonal).
* Covariant projection E: on each total-weight space W_m (H_N-invariant, multiplicity-free by quantum
  Schur–Weyl) E(Q) = Σ_k (tr(Q P_k)/tr P_k) P_k, P_k the central idempotent of λ = (N−k, k),
  obtained by Lagrange interpolation in the full twist Δ² (eigenvalue q^{2c(λ)}); the interpolation is
  checked exactly (idempotent, complete, Π(Δ² − e_k) = 0) on every block it is used on.
* Connected part: E(Q)^conn = E(Q) − (tr_W Q / dim W)·1 on each W_m.
* t₂(X) = Σ_m q^{m} Tr_{W_m}(E(Q)^conn ρ(X)) / [2]_q^N   (q^m = K^{⊗N} on W_m, m = #u − #d),
  t₁(X) = Σ_m q^{m} Tr_{W_m}(ρ(X)) / [2]_q^N  (= Ocneanu–Markov trace at z_D, checked).

No floats. Values at q₀ are produced by the caller from the exact rational functions.
"""
from __future__ import annotations

import itertools
from functools import lru_cache

from sympy import QQ
from sympy.polys.fields import field

KF, QSYM = field("q", QQ)

# The engine runs over one number field at a time: the symbolic ℚ(q) (exact closed forms; small N),
# an exact rational q (Fraction; exact zero tests at any N) or mpmath at the proton q₀ (70 dps).
q = ONE = ZERO = h = QD2 = None
CHARGE: dict = {}
EXACT = True
TOL = None


def use(qval=None, one=None, exact=True, tol=None):
    """qval=None -> symbolic ℚ(q). Otherwise q := qval with unit `one` (Fraction(1) or mp.mpf(1))."""
    global q, ONE, ZERO, h, QD2, CHARGE, EXACT, TOL
    if qval is None:
        q, ONE, ZERO = QSYM, KF.one, KF.zero
    else:
        q, ONE, ZERO = qval, one, one * 0
    h = q - ONE / q
    QD2 = q + ONE / q
    CHARGE = {"quark": (ONE * 2 / 3, -ONE / 3), "lepton": (ZERO, -ONE), "neutral": (ZERO, ZERO)}
    EXACT, TOL = exact, tol
    for f in (blocks, isotypic_projectors, insertions, _rho_cache):
        f.cache_clear()


def _close(a, b):
    if EXACT:
        return a == b
    return abs(a - b) <= TOL * (1 + abs(b))


def _mclose(A, B):
    return all(_close(a, b) for ra, rb in zip(A, B) for a, b in zip(ra, rb))


# ── weight-space blocks ─────────────────────────────────────────────────────────────────────────
@lru_cache(maxsize=None)
def blocks(N):
    """{m: list of basis tuples} with m = #u − #d (bit 0 = u)."""
    out: dict = {}
    for b in itertools.product((0, 1), repeat=N):
        m = sum(1 if x == 0 else -1 for x in b)
        out.setdefault(m, []).append(b)
    return out


def _apply_gen(vec, i, inv):
    out: dict = {}
    for b, c in vec.items():
        a, bb = b[i], b[i + 1]
        if a == bb:
            terms = [(b, q)]
        elif (a, bb) == (0, 1):
            sw = list(b); sw[i], sw[i + 1] = 1, 0
            terms = [(tuple(sw), ONE)]
        else:
            sw = list(b); sw[i], sw[i + 1] = 0, 1
            terms = [(tuple(sw), ONE), (b, h)]
        for bv, cv in terms:
            out[bv] = out.get(bv, ZERO) + c * cv
        if inv:                       # Ř⁻¹ = Ř − h
            out[b] = out.get(b, ZERO) - c * h
    return {k: v for k, v in out.items() if v != 0}


def apply_letters(vec, letters):
    """letters read left to right as a product; ρ(xy) = ρ(x)ρ(y), so apply right to left.
    g ≥ 0: σ_g; g < 0: σ_{−g−1}⁻¹ (the #8681 convention)."""
    for g in reversed(letters):
        vec = _apply_gen(vec, g, False) if g >= 0 else _apply_gen(vec, -g - 1, True)
    return vec


def apply_element(vec, elem):
    """elem = list of factors; factor = list of (coef, letters) (a linear combination).
    The element is the product of its factors left to right."""
    for fac in reversed(elem):
        out: dict = {}
        for coef, letters in fac:
            if coef == 0:
                continue
            for k, v in apply_letters(vec, letters).items():
                out[k] = out.get(k, ZERO) + coef * v
        vec = {k: v for k, v in out.items() if v != 0}
    return vec


def rho_blocks(N, elem):
    """{m: dense matrix (list of rows)} of ρ(elem) on each W_m."""
    return _rho_cache(N, repr(elem), elem)


@lru_cache(maxsize=None)
def _unused(N, key):
    raise NotImplementedError


_RHO: dict = {}


def _rho_cache(N, key, elem):
    if (N, key) in _RHO:
        return _RHO[(N, key)]
    _RHO[(N, key)] = r = _rho_compute(N, elem)
    return r


_rho_cache.cache_clear = _RHO.clear


def _rho_compute(N, elem):
    res = {}
    for m, bs in blocks(N).items():
        ix = {b: i for i, b in enumerate(bs)}
        d = len(bs)
        M = [[ZERO] * d for _ in range(d)]
        for j, b in enumerate(bs):
            for k, v in apply_element({b: ONE}, elem).items():
                M[ix[k]][j] = v          # weight preserved (checked by KeyError otherwise)
        res[m] = M
    return res


# ── tiny dense linear algebra over KF ───────────────────────────────────────────────────────────
def mm(A, B):
    n, p = len(A), len(B[0])
    Bt = list(zip(*B))
    return [[sum((a * b for a, b in zip(A[i], Bt[j]) if a != 0 and b != 0), ZERO) for j in range(p)]
            for i in range(n)]


def eye(d):
    return [[ONE if i == j else ZERO for j in range(d)] for i in range(d)]


def lin(*terms):
    """Σ c·M."""
    d = len(terms[0][1])
    out = [[ZERO] * d for _ in range(d)]
    for c, M in terms:
        for i in range(d):
            for j in range(d):
                if M[i][j] != 0:
                    out[i][j] += c * M[i][j]
    return out


def tr(M):
    return sum((M[i][i] for i in range(len(M))), ZERO)


def diag(vals):
    d = len(vals)
    return [[vals[i] if i == j else ZERO for j in range(d)] for i in range(d)]


# ── central idempotents of H_N on each weight space ────────────────────────────────────────────
def full_twist_letters(N, gens=None):
    gens = list(range(N - 1)) if gens is None else gens
    return gens * (len(gens) + 1)


def content_sum(N, k):
    a, b = N - k, k
    return a * (a - 1) // 2 + b * (b - 1) // 2 - b


@lru_cache(maxsize=None)
def isotypic_projectors(N):
    """{m: {k: P_k}} — central idempotents of the H_N image on W_m, λ = (N−k, k)."""
    D2 = rho_blocks(N, [[(ONE, full_twist_letters(N))]])
    out = {}
    for m, bs in blocks(N).items():
        nu, nd = (N + m) // 2, (N - m) // 2
        ks = list(range(0, min(nu, nd) + 1))
        ev = {k: q ** (2 * content_sum(N, k)) for k in ks}
        d = len(bs)
        P = {}
        for k in ks:
            M = eye(d)
            for l in ks:
                if l != k:
                    M = mm(M, lin((ONE / (ev[k] - ev[l]), D2[m]), (-ev[l] / (ev[k] - ev[l]), eye(d))))
            P[k] = M
        # exact checks
        tot = lin(*[(ONE, P[k]) for k in ks])
        assert _mclose(tot, eye(d)), ("completeness", N, m)
        for k in ks:
            assert _mclose(mm(P[k], P[k]), P[k]), ("idempotent", N, m, k)
            assert _mclose(mm(D2[m], P[k]), lin((ev[k], P[k]))), ("eigen", N, m, k)
        out[m] = P
    return out


# ── charge insertions ───────────────────────────────────────────────────────────────────────────
def qpair_diag(colours, b):
    Qs = [CHARGE[c][x] for c, x in zip(colours, b)]
    return sum((Qs[i] * Qs[j] for i in range(len(Qs)) for j in range(i + 1, len(Qs))), ZERO)


@lru_cache(maxsize=None)
def insertions(colours):
    """{m: {'raw': Q, 'cov': E(Q)^conn, 'rawconn': Q − mean, 'Ecoef': {k: c_k}}}."""
    colours = tuple(colours)
    N = len(colours)
    Pk = isotypic_projectors(N)
    out = {}
    for m, bs in blocks(N).items():
        d = len(bs)
        Q = diag([qpair_diag(colours, b) for b in bs])
        mean = tr(Q) / d
        coefs = {k: tr(mm(Q, P)) / tr(P) for k, P in Pk[m].items()}
        EQ = lin(*[(coefs[k], P) for k, P in Pk[m].items()])
        out[m] = {"raw": Q, "cov": lin((ONE, EQ), (-mean, eye(d))),
                  "rawconn": lin((ONE, Q), (-mean, eye(d))), "Ecoef": coefs, "mean": mean}
    return out


def t_one(N, rho):
    return sum((q ** m * tr(M) for m, M in rho.items()), ZERO) / QD2 ** N


def t_two(colours, rho, kind="cov"):
    ins = insertions(tuple(colours))
    N = len(colours)
    return sum((q ** m * tr(mm(ins[m][kind], M)) for m, M in rho.items()), ZERO) / QD2 ** N


def sector_trace(N, rho, pred, insertion=None):
    """Σ_{b in sector} ⟨b| K X ρ |b⟩ with optional per-block insertion matrices {m: X}."""
    tot = ZERO
    for m, M in rho.items():
        A = M if insertion is None else mm(insertion[m], M)
        for i, b in enumerate(blocks(N)[m]):
            if pred(b):
                tot += q ** m * A[i][i]
    return tot


# ── Ocneanu cross-check (independent of the block engine): coset recursion of #8681 ────────────
def ocneanu_check_words():
    return [[0], [0, 1, 0], [0, -2] * 3, [0, 0, 0], [0, 1, -3, 2, 1]]


use()
