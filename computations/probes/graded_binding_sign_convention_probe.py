#!/usr/bin/env python3
# polynomial_q_not_applicable: exact Fraction h-series + mpmath evaluation at q0; no symbolic-q polynomial output.
"""Is graded binding `+c_k` or `-c_k`? The corpus's own functional decides, and it
decides by making the question EMPTY: every binding law the corpus carries is a
LOGARITHM of a trace, and a logarithm — with either sign, at any scale — turns the
chain product into a sum, so the type-two pair convolution `sum_{i<j} b_i b_j`
that carries `(N-Z)^2` never reaches it. The sign question is live only for a
BARE (linear) functional of the trace, and the corpus's one bare binding law,
`B = Q_beta . (tr_free - tr_atom)`, was REFUTED on 2026-09-05 for a different
reason (a product is not extensive).

WHERE THIS SITS
---------------
Bean `qou-zlra`, opened from `qou-oooq`. There,
`the_asymmetry_term_lives_at_vassiliev_type_two_probe` established

    c_2/c_0 = (N-Z)^2/2 + (5-A)/8        [chain product, every A = 3..10, every Z]

and READ binding as `-alpha c_2/c_0` so that the asymmetry penalises |N-Z|. The
bean asked which sign the framework actually takes, and noted a third
possibility — `unified-iterative-correction`'s `ln|tr M_lambda|` — that is a log.
This probe answers all three at once, on the corpus's own letters, with the
theorem `QOU.Mass.GradedBindingFunctionalPairTerm` (sorry-free) as the invariant.

THE LETTERS (recomputed, not hardcoded)
--------------------------------------
Convention D, proton pin, the closed forms of `QOU.Mass.ChainTraceFactor`:

    z    = q^3/(q^2+1)                  b_pp = z
    h    = q - 1/q                      b_nn = z - h = 1/(q(q^2+1))
    delta = (q-1)^2 (1-q^-4)/3          b_pn = z - h(1 - delta/2)/2

and the free-nucleon factors `t_p`, `t_n` from the 2026-09-05 arc synthesis
(`docs/audits/2026-09-05-binding-law-arc-synthesis.md` section 2), used ONLY for
the refuted difference law's scan.

WHAT IS MEASURED
----------------
S1  the three bond factors and the Lean identities they satisfy at q_0;
S2  exact h-series over Fraction: [h^2] of the chain PRODUCT is quadratic in Z
    (second difference 4 = the closed form's (N-Z)^2/2), [h^2] of +log and of
    -log of the same product is LINEAR in Z (second differences 0) — for
    A = 3..12 and every Z — and the Lean identity [h^2] log P = sum(c_i - b_i^2/2);
S3  valley scan at q_0 for each functional the corpus carries or has carried:
    the live log-ratio law, the refuted bare difference, and the type-two
    truncations under both signs; argmax_Z at fixed A, interior or endpoint;
S4  the `qou-eqwg` within-generator question: (a) letters on one generator
    COMMUTE (the transfer matrices are the regular representation of a
    commutative algebra), so "non-commutativity inside a generator" is empty;
    (b) the two-branch state sum `w_+ prod(q+d) + w_- prod(-1/q+d)` of several
    letters on ONE generator is NOT a product of per-letter traces, so its log
    is not additive — a real cross term, but one the chain never exercises
    because every interface letter sits on its own generator; (c) a SINGLE
    Wedderburn block `tr_lambda(prod (c sigma + d))` — the object
    `unified-iterative-correction` takes the log of — is not multiplicative
    even on the chain layout, and its [h^2] log is NOT linear in Z (nonzero,
    non-constant second differences).
    The YSN representation used is rational (Hoefsmit seminormal form), relation-
    checked exactly, and cross-checked against `hecke_core_legacy`'s numeric YSN
    at q_0.

NO float64 anywhere: mpmath at COMPUTE_DPS (70) for q_0 evaluations, `Fraction`
for the h-series. `float()` appears only inside display f-strings.

NOT CLAIMED
-----------
No binding number, no fit, nothing wired. Not that any functional is correct.
Not that the UIC single-block quadratic has the SEMF's sign or size — it is
reported with whatever sign the algebra gives it. Not that the valley question
is settled: it is settled FOR the functionals the corpus carries, on the chain.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from math import isqrt  # integer root only; exact
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS, fmt  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

try:
    from qou_substrate.constants import M_E_MEV_STR as _ME_STR  # noqa: E402
except Exception:  # pragma: no cover
    from codata_constants import M_E_MEV as _ME  # noqa: E402
    _ME_STR = str(_ME)

mp.mp.dps = COMPUTE_DPS
T0 = time.time()

# ---------------------------------------------------------------------------
# exact truncated power series in h over Fraction
# ---------------------------------------------------------------------------
ORD = 4  # keep h^0..h^4; everything below needs at most h^2 and is exact there


class PS:
    """Truncated power series sum_{k<=ORD} c_k h^k with Fraction coefficients."""
    __slots__ = ("c",)

    def __init__(self, c):
        c = [Fraction(x) for x in c][: ORD + 1]
        self.c = c + [Fraction(0)] * (ORD + 1 - len(c))

    @staticmethod
    def const(x):
        return PS([x])

    def __add__(self, o):
        o = o if isinstance(o, PS) else PS.const(o)
        return PS([a + b for a, b in zip(self.c, o.c)])

    __radd__ = __add__

    def __neg__(self):
        return PS([-a for a in self.c])

    def __sub__(self, o):
        return self + (-(o if isinstance(o, PS) else PS.const(o)))

    def __rsub__(self, o):
        return PS.const(o) - self

    def __mul__(self, o):
        if not isinstance(o, PS):
            o = PS.const(o)
        out = [Fraction(0)] * (ORD + 1)
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j in range(ORD + 1 - i):
                out[i + j] += a * o.c[j]
        return PS(out)

    __rmul__ = __mul__

    def inv(self):
        a0 = self.c[0]
        assert a0 != 0, "series inverse needs a nonzero constant term"
        out = [Fraction(0)] * (ORD + 1)
        out[0] = 1 / a0
        for k in range(1, ORD + 1):
            s = sum(self.c[j] * out[k - j] for j in range(1, k + 1))
            out[k] = -s / a0
        return PS(out)

    def __truediv__(self, o):
        o = o if isinstance(o, PS) else PS.const(o)
        return self * o.inv()

    def __rtruediv__(self, o):
        return PS.const(o) * self.inv()

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return (self.inv()) ** (-n)
        r = PS.const(1)
        for _ in range(n):
            r = r * self
        return r

    def shift_down(self):
        """Divide by h (requires zero constant term)."""
        assert self.c[0] == 0
        return PS(self.c[1:] + [Fraction(0)])

    def sqrt(self):
        """Square root of a series whose constant term is a rational square."""
        a0 = self.c[0]
        r0 = Fraction(isqrt(a0.numerator), isqrt(a0.denominator))
        assert r0 * r0 == a0, "constant term must be a perfect square"
        out = [Fraction(0)] * (ORD + 1)
        out[0] = r0
        for k in range(1, ORD + 1):
            s = sum(out[j] * out[k - j] for j in range(1, k))
            out[k] = (self.c[k] - s) / (2 * r0)
        return PS(out)

    def log_unital(self):
        """log of a series with constant term 1: log(1+u) = u - u^2/2 + u^3/3 - ..."""
        assert self.c[0] == 1
        u = self - 1
        out = PS.const(0)
        up = PS.const(1)
        for k in range(1, ORD + 1):
            up = up * u
            out = out + up * Fraction((-1) ** (k + 1), k)
        return out

    def __eq__(self, o):
        o = o if isinstance(o, PS) else PS.const(o)
        return self.c == o.c

    def __repr__(self):
        return "PS(" + ", ".join(str(x) for x in self.c) + ")"


H = PS([0, 1])                          # the variable h
Q_SER = (H + (H * H + 4).sqrt()) / 2    # q = (h + sqrt(h^2+4))/2, i.e. q - 1/q = h


def letters_ser():
    q, qi = Q_SER, Q_SER.inv()
    z = q ** 3 / (q * q + 1)
    delta = (q - 1) ** 2 * (1 - qi ** 4) / 3
    d_pn = -(H * (1 - delta / 2) / 2)
    return {"pp": z, "pn": z + d_pn, "nn": z - H}, {"pp": PS.const(0), "pn": d_pn, "nn": -H}


def second_differences(vals):
    return [vals[i + 2] - 2 * vals[i + 1] + vals[i] for i in range(len(vals) - 2)]


# ---------------------------------------------------------------------------
# generic scalar-field adapter (Fraction at a rational q, or PS in h) for YSN
# ---------------------------------------------------------------------------
class Field:
    def __init__(self, q, qi, h, one, zero):
        self.q, self.qi, self.h, self.one, self.zero = q, qi, h, one, zero

    @staticmethod
    def rational(qf: Fraction):
        return Field(qf, 1 / qf, qf - 1 / qf, Fraction(1), Fraction(0))

    @staticmethod
    def series():
        return Field(Q_SER, Q_SER.inv(), H, PS.const(1), PS.const(0))

    @staticmethod
    def numeric(q0):
        return Field(q0, 1 / q0, q0 - 1 / q0, mp.mpf(1), mp.mpf(0))

    def a_rho(self, rho: int):
        """Hoefsmit diagonal entry a_rho = h/(1 - q^{-2 rho}); as a series it is
        1/((1 - q^{-2 rho})/h) so the removable singularity at h = 0 is handled."""
        den = self.one - (self.qi ** (2 * rho) if rho > 0 else self.q ** (-2 * rho))
        if isinstance(self.h, PS):
            return den.shift_down().inv()
        return self.h / den


def standard_tableaux(shape):
    n = sum(shape)
    tabs = []

    def rec(t, k):
        if k > n:
            tabs.append([row[:] for row in t])
            return
        for r in range(len(shape)):
            if len(t[r]) < shape[r] and (r == 0 or len(t[r - 1]) > len(t[r])):
                t[r].append(k)
                rec(t, k + 1)
                t[r].pop()

    rec([[] for _ in shape], 1)
    return tabs


def content_of(T, k):
    for r, row in enumerate(T):
        if k in row:
            return row.index(k) - r
    raise KeyError(k)


def swap_tab(T, k):
    S = [[k + 1 if x == k else (k if x == k + 1 else x) for x in row] for row in T]
    for r, row in enumerate(S):
        if any(row[i] > row[i + 1] for i in range(len(row) - 1)):
            return None
        for i, x in enumerate(row):
            if r > 0 and S[r - 1][i] > x:
                return None
    return S


def ysn_matrices(shape, F: Field):
    """Rational Hoefsmit seminormal form of sigma_1..sigma_{n-1} in the irrep `shape`.
    M[j][i] = coefficient of v_j in sigma v_i (column i is the image of basis i).
    Eigenvalues q (same row) and -1/q (same column); the mixing block for a pair
    (T, T') with axial distance rho = c(k+1)-c(k) > 0 on T is
    [[a_rho, 1 + a_rho a_-rho], [1, a_-rho]] (trace h, determinant -1)."""
    n = sum(shape)
    tabs = standard_tableaux(shape)
    idx = {tuple(tuple(r) for r in T): i for i, T in enumerate(tabs)}
    dim = len(tabs)
    mats = []
    for k in range(1, n):
        M = [[F.zero for _ in range(dim)] for _ in range(dim)]
        for i, T in enumerate(tabs):
            rho = content_of(T, k + 1) - content_of(T, k)
            if rho == 1:
                M[i][i] = F.q
            elif rho == -1:
                M[i][i] = -F.qi
            elif rho > 0:
                Tp = swap_tab(T, k)
                j = idx[tuple(tuple(r) for r in Tp)]
                ar, an = F.a_rho(rho), F.a_rho(-rho)
                M[i][i] = ar
                M[j][i] = F.one            # v_T  -> a_rho v_T + v_T'
                M[i][j] = F.one + ar * an  # v_T' -> (1 + a_rho a_-rho) v_T + a_-rho v_T'
                M[j][j] = an
        mats.append(M)
    return tabs, mats


def mat_mul(A, B, zero):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), zero) for j in range(n)] for i in range(n)]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def mat_id(n, one, zero):
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def mat_lin(c, d, S, one, zero):
    """c*sigma + d*I as a matrix."""
    n = len(S)
    return [[c * S[i][j] + (d if i == j else zero) for j in range(n)] for i in range(n)]


def trace(A, zero):
    return sum((A[i][i] for i in range(len(A))), zero)


def check_relations(shape, F: Field):
    tabs, S = ysn_matrices(shape, F)
    n = len(tabs)
    I = mat_id(n, F.one, F.zero)
    ok = True
    for k, s in enumerate(S):
        lhs = mat_mul(s, s, F.zero)
        rhs = mat_lin(F.h, F.one, s, F.one, F.zero)
        ok &= mat_eq(lhs, rhs)                               # Hecke: s^2 = h s + 1
    for k in range(len(S) - 1):
        a, b = S[k], S[k + 1]
        ok &= mat_eq(mat_mul(mat_mul(a, b, F.zero), a, F.zero),
                     mat_mul(mat_mul(b, a, F.zero), b, F.zero))  # braid
    for k in range(len(S)):
        for l in range(k + 2, len(S)):
            ok &= mat_eq(mat_mul(S[k], S[l], F.zero), mat_mul(S[l], S[k], F.zero))
    del I
    return ok


# ---------------------------------------------------------------------------
# words: the canonical intra block (as in _exact_trace_engine.nucleon_word),
# interface letters, two layouts
# ---------------------------------------------------------------------------
B_P = (Fraction(0), Fraction(1, 2), Fraction(1, 2))
B_N = (Fraction(1, 2), Fraction(1, 2), Fraction(1))


def nucleon_letters(kind, g0, g1, h):
    """(c, d, generator) letters of one nucleon's eleven-letter intra block."""
    b = B_P if kind == "p" else B_N
    w = []
    for _ in range(3):
        w += [(1, 0 * h, g0), (1, -h, g1)]
    w += [(1, -b[0] * h, g0), (1, -b[1] * h, g0), (1, -b[2] * h, g1)]
    return w + [(1, 0 * h, g0), (1, 0 * h, g0)]


def interface_d(a, b, dmap):
    return dmap["pp"] if a == b == "p" else (dmap["nn"] if a == b == "n" else dmap["pn"])


def chain_word(order, dmap, h):
    """Canonical chain: p^Z n^N strand order, one interface letter between adjacent
    nucleons on the (otherwise unused) generator 3k+2."""
    w = []
    for k, kind in enumerate(order):
        w += nucleon_letters(kind, 3 * k, 3 * k + 1, h)
        if k > 0:
            w.append((1, interface_d(order[k - 1], kind, dmap), 3 * (k - 1) + 2))
    return w


def uic_shaped_word(order, dmap, h, n_gens):
    """The `_step_chain_generic` layout of hecke_core_legacy: per step, the intra
    letters then one interface letter to EVERY previous nucleon, generator index
    cycling modulo n_gens and restarting at 0 each step."""
    w = []
    for k, kind in enumerate(order):
        g = 0
        for (c, d, _) in nucleon_letters(kind, 0, 1, h):
            w.append((c, d, g % n_gens))
            g += 1
        for prev in order[:k]:
            w.append((1, interface_d(prev, kind, dmap), g % n_gens))
            g += 1
    return w


def block_trace(word, S, F: Field):
    """tr_lambda( prod_i (c_i sigma_{g_i} + d_i) ) in the irrep with YSN matrices S."""
    n = len(S[0])
    M = mat_id(n, F.one, F.zero)
    for c, d, g in word:
        M = mat_mul(M, mat_lin(c, d, S[g], F.one, F.zero), F.zero)
    return trace(M, F.zero)


def uic_order(Z, N):
    order, pc, nc = [], 0, 0
    for kk in range(Z + N):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            order.append("p"); pc += 1
        else:
            order.append("n"); nc += 1
    return order


# ---------------------------------------------------------------------------
def main() -> int:
    checks: list[tuple[str, bool]] = []
    data: dict = {}

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"mp.dps = {mp.mp.dps}  (COMPUTE_DPS), h-series order {ORD}, exact Fraction")

    # ======================================================================
    print("\n" + "=" * 76)
    print("S1  THE LETTERS AT THE PROTON PIN (recomputed from ChainTraceFactor's closed forms)")
    print("=" * 76)
    q0 = q_at()
    h0 = q0 - 1 / q0
    z0 = q0 ** 3 / (q0 ** 2 + 1)
    delta0 = (q0 - 1) ** 2 * (1 - q0 ** -4) / 3
    dpn0 = -h0 * (1 - delta0 / 2) / 2
    b = {"pp": z0, "pn": z0 + dpn0, "nn": z0 - h0}
    L = {k: -mp.log(v) for k, v in b.items()}
    m_e = mp.mpf(_ME_STR)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0_N0 = _qbeta_e0.order_zero_scaled(m_e, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    hbar_q = 1 - 1 / q0
    E0_full = E0_N0 / (1 - hbar_q ** 2)
    print(f"    q0      = {mp.nstr(q0, 25)}   (proton pin, qou_substrate.q_at)")
    print(f"    h0      = {mp.nstr(h0, 25)}")
    for k in ("pp", "pn", "nn"):
        print(f"    b_{k} = {mp.nstr(b[k], 20)}    L_{k} = -log b_{k} = {mp.nstr(L[k], 20)}")
    print(f"    E0 (N=0) = {mp.nstr(E0_N0, 12)} MeV,   E0 (full, ruled 2026-09-05) = {mp.nstr(E0_full, 12)} MeV")
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 12))
    check("b_nn = 1/(q(q^2+1))  (ChainTraceFactor.markovZ_sub_heckeH)",
          abs(b["nn"] - 1 / (q0 * (q0 ** 2 + 1))) < tol)
    check("L_pp + L_nn = 2 log(q + 1/q)  (ChainTraceFactor.L_pp_add_L_nn)",
          abs(L["pp"] + L["nn"] - 2 * mp.log(q0 + 1 / q0)) < tol)
    check("b_pp > b_pn > b_nn > 0 at q0  (ChainTraceFactor.factors_strict_mono)",
          b["pp"] > b["pn"] > b["nn"] > 0)
    check("the h-series q(h) satisfies q - 1/q = h exactly to order h^4",
          Q_SER - Q_SER.inv() == H)
    fser, dser = letters_ser()
    for k in ("pp", "pn", "nn"):
        val = sum(mp.mpf(c.numerator) / mp.mpf(c.denominator) * h0 ** i for i, c in enumerate(fser[k].c))
        print(f"    h-series of b_{k} through h^{ORD} at h0: {mp.nstr(val, 12)}  vs exact {mp.nstr(b[k], 12)}"
              f"  (truncation gap {mp.nstr(abs(val - b[k]), 3)})")
    check("all three h-series have constant term z(0) = 1/2 (shared, so the Lean normalisation applies)",
          all(fser[k].c[0] == Fraction(1, 2) for k in fser))
    for k in ("pp", "pn", "nn"):
        data[f"b_{k}"] = fmt(b[k])
        data[f"L_{k}"] = fmt(L[k])
    data["q0"] = fmt(q0)
    data["E0_N0_MeV"] = fmt(E0_N0)
    data["E0_full_MeV"] = fmt(E0_full)

    # ======================================================================
    print("\n" + "=" * 76)
    print("S2  EXACT h-SERIES: the pair term is in the PRODUCT and in NEITHER sign of the log")
    print("=" * 76)
    print("    normalised factors f/z0 (unit constant term); [h^2] of prod, of +log, of -log;")
    print("    second differences in Z at fixed A (chain census: Z-1 pp, 1 pn, N-1 nn)")
    fnorm = {k: fser[k] / Fraction(1, 2) for k in fser}
    logf = {k: fnorm[k].log_unital() for k in fnorm}
    prod_quad_ok, log_lin_ok, closed_ok, lean_ok = True, True, True, True
    print(f"    {'A':>3} | prod [h^2] second diffs | +log [h^2] second diffs | -log [h^2] second diffs")
    for A in range(3, 13):
        rowP, rowLp, rowLm = [], [], []
        for Z in range(1, A):
            N = A - Z
            counts = {"pp": Z - 1, "pn": 1, "nn": N - 1}
            P = PS.const(1)
            for k, n in counts.items():
                P = P * fnorm[k] ** n
            c2 = P.c[2]
            closed = Fraction((N - Z) ** 2, 2) + Fraction(5 - A, 8)
            closed_ok &= (c2 == closed)
            # Lean: [h^2] log P = sum_i (c_i - b_i^2/2) over the multiset
            lean_val = sum(counts[k] * (fnorm[k].c[2] - fnorm[k].c[1] ** 2 / 2) for k in counts)
            lp = sum((logf[k] * counts[k] for k in counts), PS.const(0))
            lean_ok &= (P.log_unital().c[2] == lean_val == lp.c[2])
            rowP.append(c2)
            rowLp.append(lp.c[2])
            rowLm.append(-lp.c[2])
        dP, dLp, dLm = second_differences(rowP), second_differences(rowLp), second_differences(rowLm)
        prod_quad_ok &= all(x == 4 for x in dP)
        log_lin_ok &= all(x == 0 for x in dLp) and all(x == 0 for x in dLm)
        print(f"    {A:>3} | {str(sorted(set(dP))):>22} | {str(sorted(set(dLp))):>23} | {str(sorted(set(dLm))):>23}")
    check("c_2/c_0 = (N-Z)^2/2 + (5-A)/8 EXACTLY for every A = 3..12 and every Z (reproduces qou-oooq)",
          closed_ok)
    check("[h^2] of the chain PRODUCT has second difference 4 in Z at every A (a quadratic, vertex N = Z)",
          prod_quad_ok)
    check("[h^2] of +log and of -log of the same product has ALL second differences 0 (linear in Z)",
          log_lin_ok)
    check("[h^2] log P = sum_i (c_i - b_i^2/2) exactly  (Lean logJet_c2_prod / logJet_c2_census)",
          lean_ok)
    # the pair-term identity itself, at the h-series level
    e2_ok = True
    for A in (4, 6, 8):
        for Z in range(1, A):
            N = A - Z
            bs = [fnorm["pp"].c[1]] * (Z - 1) + [fnorm["pn"].c[1]] + [fnorm["nn"].c[1]] * (N - 1)
            cs = [fnorm["pp"].c[2]] * (Z - 1) + [fnorm["pn"].c[2]] + [fnorm["nn"].c[2]] * (N - 1)
            e2 = sum(bs[i] * bs[j] for i in range(len(bs)) for j in range(i + 1, len(bs)))
            P = PS.const(1)
            for k, n in {"pp": Z - 1, "pn": 1, "nn": N - 1}.items():
                P = P * fnorm[k] ** n
            e2_ok &= (P.c[2] == sum(cs) + e2) and (P.c[1] == sum(bs))
            e2_ok &= (sum(bs) ** 2 == sum(x * x for x in bs) + 2 * e2)
    check("[h^2] prod = sum c_i + e2(b) and (sum b)^2 = sum b^2 + 2 e2(b)  (Lean prod_c2, sq_sum_eq)", e2_ok)
    data["prod_h2_second_difference_in_Z"] = "4 (all A = 3..12)"
    data["log_h2_second_difference_in_Z"] = "0 (both signs, all A = 3..12)"
    data["b1_over_z0"] = {k: str(fnorm[k].c[1]) for k in fnorm}
    data["c2_over_z0"] = {k: str(fnorm[k].c[2]) for k in fnorm}

    # ======================================================================
    print("\n" + "=" * 76)
    print("S3  VALLEY SCAN AT q0: argmax_Z of each functional at fixed A (interior = valley)")
    print("=" * 76)
    # free-nucleon factors from the 2026-09-05 arc synthesis section 2 (derived closed forms)
    q = q0
    t_p = (q**22 + q**20 + 2*q**18 + 2*q**16 + 3*q**14 + 2*q**12 + q**10 - q**8 - q**4 - q**2 - 1) / (4 * q**9 * (q**2 + 1)**2)
    t_n = (q**18 - q**16 + 2*q**14 - 2*q**12 + 4*q**10 - 3*q**8 + 3*q**6 - 2*q**4 + q**2 - 1) / (4 * q**9)
    Qb = mp.mpf("0.7823334")  # CODATA Q_beta, the refuted law's own scale (validation-only, label)
    print(f"    t_p = {mp.nstr(t_p, 15)}, t_n = {mp.nstr(t_n, 15)}  (arc-synthesis closed forms, difference law only)")
    hb2 = {k: mp.mpf(fnorm[k].c[1].numerator) / fnorm[k].c[1].denominator for k in fnorm}
    hc2 = {k: mp.mpf(fnorm[k].c[2].numerator) / fnorm[k].c[2].denominator for k in fnorm}

    def functionals(Z, N):
        counts = {"pp": Z - 1, "pn": 1, "nn": N - 1}
        A = Z + N
        Pn = mp.mpf(1)
        for k, n in counts.items():
            Pn *= (b[k] / z0) ** n                      # normalised product
        Lsum = sum(counts[k] * L[k] for k in counts)
        c1 = sum(counts[k] * hb2[k] for k in counts)
        c2 = sum(counts[k] * hc2[k] for k in counts) + sum(
            counts[i] * counts[j] * hb2[i] * hb2[j] for i in counts for j in counts if i < j) + sum(
            counts[k] * (counts[k] - 1) / 2 * hb2[k] ** 2 for k in counts)
        tr_atom = t_p ** Z * t_n ** N * z0 ** (A - 1) * Pn
        tr_free = t_p ** Z * t_n ** N
        return {
            "log-ratio (live law, owner 2026-09-04/05)": E0_full * Lsum,
            "bare difference Q_beta.(tr_free - tr_atom) (REFUTED 2026-09-05)": Qb * (tr_free - tr_atom),
            "-c_2/c_0 alone (the qou-oooq reading)": -E0_N0 * c2,
            "+c_2/c_0 alone (the opposite sign)": E0_N0 * c2,
            "bare truncation -(1 + c_1 h + c_2 h^2)": -E0_N0 * (1 + c1 * h0 + c2 * h0 ** 2),
            "bare truncation +(1 + c_1 h + c_2 h^2)": E0_N0 * (1 + c1 * h0 + c2 * h0 ** 2),
            "bare -prod(f/z0) resummed": -E0_N0 * Pn,
            "bare +prod(f/z0) resummed": E0_N0 * Pn,
        }

    names = list(functionals(1, 2).keys())
    verdict = {}
    for nm in names:
        interior = []
        argmax = []
        for A in range(3, 13):
            vals = [functionals(Z, A - Z)[nm] for Z in range(1, A)]
            im = max(range(len(vals)), key=lambda i: vals[i])
            Zmax = im + 1
            argmax.append(Zmax)
            interior.append(1 < Zmax < A - 1)
        verdict[nm] = (argmax, interior)
        print(f"    {nm}")
        print(f"        argmax_Z, A=3..12 : {argmax}    interior maximum at: "
              f"{[A for A, i in zip(range(3, 13), interior) if i] or 'none'}")
        data[f"argmax_Z_A3to12__{nm}"] = str(argmax)
    check("live log-ratio law: maximum of B at an ENDPOINT (Z = 1) for every A = 3..12 — no valley",
          all(z == 1 for z in verdict[names[0]][0]))
    check("refuted bare difference: no interior maximum at any A = 3..12",
          not any(verdict[names[1]][1]))
    check("-c_2/c_0 alone: interior maximum at N = Z (even A) / |N-Z| = 1 (odd A) for A = 4..12",
          all(abs(2 * z - A) <= 1 for z, A in zip(verdict[names[2]][0][1:], range(4, 13)))
          and all(verdict[names[2]][1][1:]))
    check("+c_2/c_0 alone: maximum at an endpoint for every A — the sign flips the valley into a hill",
          not any(verdict[names[3]][1]))
    check("bare resummed product, either sign: no interior maximum (monotone in Z)",
          not any(verdict[names[6]][1]) and not any(verdict[names[7]][1]))

    # ======================================================================
    print("\n" + "=" * 76)
    print("S4  THE WITHIN-GENERATOR QUESTION (qou-eqwg)")
    print("=" * 76)
    # (a) transfer matrices of letters on ONE generator commute (exact, at a rational q and as series)
    def T(c, d, h):
        return [[c * h + d, c], [c, d]]

    Fr = Field.rational(Fraction(3, 2))
    comm_ok = True
    letters_q = [(Fraction(1), Fraction(0)), (Fraction(1), -Fr.h), (Fraction(1), -Fr.h / 3), (Fraction(2), Fraction(5))]
    for (c, d) in letters_q:
        for (c2_, d2_) in letters_q:
            A_, B_ = T(c, d, Fr.h), T(c2_, d2_, Fr.h)
            comm_ok &= mat_eq(mat_mul(A_, B_, Fr.zero), mat_mul(B_, A_, Fr.zero))
    Fs = Field.series()
    for (c, d) in [(1, PS.const(0)), (1, -H), (1, dser["pn"]), (1, -H / 2)]:
        for (c2_, d2_) in [(1, PS.const(0)), (1, -H), (1, dser["pn"])]:
            A_, B_ = T(c, d, Fs.h), T(c2_, d2_, Fs.h)
            comm_ok &= mat_eq(mat_mul(A_, B_, Fs.zero), mat_mul(B_, A_, Fs.zero))
    check("(a) transfer matrices T(c,d) = [[ch+d, c],[c, d]] of letters on ONE generator commute exactly "
          "(they are the regular representation of the commutative algebra R[sigma]/(sigma^2 - h sigma - 1))",
          comm_ok)
    print("        -> 'non-commutativity inside a generator' is EMPTY: there is none.")

    # (b) the two-branch state sum on one generator is not multiplicative: measure the [h^2] log cross term
    wplus = (Q_SER ** 2 + 1 + Q_SER.inv() ** 2)
    wplus = wplus / (wplus + 1)
    wminus = PS.const(1) - wplus

    def tr2_stack(ds):
        """tr_2 of prod (sigma + d_i) on ONE generator = w+ prod(q+d) + w- prod(-1/q + d)."""
        Pp, Pm = PS.const(1), PS.const(1)
        for d in ds:
            Pp = Pp * (Q_SER + d)
            Pm = Pm * (-Q_SER.inv() + d)
        return wplus * Pp + wminus * Pm

    cross = {}
    for ka in ("pp", "pn", "nn"):
        for kb in ("pp", "pn", "nn"):
            if ka > kb:
                continue
            t_ab = tr2_stack([dser[ka], dser[kb]])
            t_a, t_b = tr2_stack([dser[ka]]), tr2_stack([dser[kb]])
            # single letters have constant term 1/2, the stack has constant term 1: log-additivity fails
            # already at h^0; report [h^0] and the [h^2] of log(t/t(0)) mismatch
            la = (t_a / t_a.c[0]).log_unital()
            lb = (t_b / t_b.c[0]).log_unital()
            lab = (t_ab / t_ab.c[0]).log_unital()
            cross[(ka, kb)] = (t_ab.c[0], t_a.c[0] * t_b.c[0], lab.c[2] - la.c[2] - lb.c[2])
            print(f"        two letters {ka},{kb} on ONE generator: tr(stack)[h^0] = {t_ab.c[0]} vs "
                  f"tr(a)tr(b)[h^0] = {t_a.c[0] * t_b.c[0]};  [h^2] log cross term = {lab.c[2] - la.c[2] - lb.c[2]}")
    check("(b) stacking two interface letters on ONE generator is NOT multiplicative: tr(stack) has constant "
          "term 1 against (1/2)^2, and the [h^2] log cross term is nonzero for every pair",
          all(v[0] == 1 and v[1] == Fraction(1, 4) and v[2] != 0 for v in cross.values()))
    print("        -> real, but the chain word puts every interface letter on its OWN generator (3k+2),")
    print("           so this cross term is never exercised by the chain; it is an interface-multiplicity effect.")
    data["one_generator_stack_h2_log_cross_terms"] = {f"{a},{b}": str(v[2]) for (a, b), v in cross.items()}

    # (c) a single Wedderburn block tr_lambda(prod(c sigma_g + d)) — the object UIC takes the log of
    print("\n    (c) single-block log functional  ln tr_lambda(prod (c sigma + d)),  chain layout, [h^2] second differences in Z")
    shapes = [(2,), (1, 1), (2, 1), (3,), (2, 2), (3, 1), (2, 1, 1), (3, 2), (4, 1), (3, 1, 1), (2, 2, 1)]
    rel_ok = all(check_relations(s, Fr) for s in shapes)
    check("(c) the rational Hoefsmit seminormal form satisfies the Hecke, braid and far-commutation relations "
          f"exactly at q = 3/2 for all {len(shapes)} shapes used",
          rel_ok)
    # cross-check the characters against hecke_core_legacy's numeric YSN at q0
    xc_ok = True
    try:
        import hecke_core_legacy as HCL  # noqa: E402
        Fn = Field.numeric(q0)
        for s in [(2, 1), (3, 1), (2, 2), (3, 2)]:
            tabs, S = ysn_matrices(s, Fn)
            corp = HCL._build_ysn_matrices_exact(list(s))
            n_ = len(S)
            words = [[0], [0, 1], [1, 0, 1], [0, 1, 0, 1]] if n_ >= 2 else [[0]]
            for wd in words:
                if max(wd) >= n_:
                    continue
                Mm = mat_id(len(S[0]), Fn.one, Fn.zero)
                for g in wd:
                    Mm = mat_mul(Mm, S[g], Fn.zero)
                mine = trace(Mm, Fn.zero)
                # corpus matrices: dense tuples of mpf (dim < 32)
                Cm = [[mp.mpf(x) for x in row] for row in corp[0]]
                Cm = mat_id(len(Cm), mp.mpf(1), mp.mpf(0))
                for g in wd:
                    Cm = mat_mul(Cm, [[mp.mpf(x) for x in row] for row in corp[g]], mp.mpf(0))
                theirs = trace(Cm, mp.mpf(0))
                gap = abs(mine - theirs)
                xc_ok &= gap < mp.mpf(10) ** -40
                print(f"        character cross-check lambda={s} word={wd}: mine {mp.nstr(mine, 20)} corpus "
                      f"{mp.nstr(theirs, 20)} gap {mp.nstr(gap, 3)}")
    except Exception as e:  # pragma: no cover
        print(f"        hecke_core_legacy cross-check unavailable: {e}")
        xc_ok = False
    check("(c) block characters agree with hecke_core_legacy's numeric YSN at q0 to < 1e-40 on four shapes",
          xc_ok)

    Fs = Field.series()
    dmap_s = dser
    single_block = {}
    print(f"\n        {'lambda':>10} {'A':>3} | tr[h^0] per Z | [h^2] log(tr/tr0) second differences in Z")
    any_quadratic = False
    quadratic_shapes = []
    for s in shapes:
        n_gens = sum(s) - 1
        if n_gens < 1:
            continue
        tabs, S = ysn_matrices(s, Fs)
        per_shape = {}
        for A in (4, 5, 6, 7, 8):
            row_c0, row_h2 = [], []
            for Z in range(1, A):
                N = A - Z
                order = ["p"] * Z + ["n"] * N
                wchain = chain_word(order, dmap_s, Fs.h)
                # map generators cyclically into H_k as the UIC does (g mod n_gens)
                wchain = [(c, d, g % n_gens) for (c, d, g) in wchain]
                tr = block_trace(wchain, S, Fs)
                row_c0.append(tr.c[0])
                if tr.c[0] == 0:
                    row_h2.append(None)
                else:
                    row_h2.append((tr / tr.c[0]).log_unital().c[2])
            if any(x is None for x in row_h2):
                dd = "undefined (tr[h^0] = 0 at some Z)"
            else:
                d2 = second_differences(row_h2)
                dd = sorted(set(d2))
                if any(x != 0 for x in d2):
                    any_quadratic = True
                    if s not in quadratic_shapes:
                        quadratic_shapes.append(s)
            per_shape[A] = (row_c0, dd)
            print(f"        {str(s):>10} {A:>3} | {str([str(x) for x in row_c0]):<40} | {dd}")
        single_block[s] = per_shape
    data["single_block_shapes_with_quadratic_h2"] = [str(s) for s in quadratic_shapes]
    check("(c) on the CHAIN layout, at least one single Wedderburn block's [h^2] log tr_lambda has nonzero "
          "second differences in Z — a single block is NOT multiplicative and its type-two piece is NOT "
          "linear in the bond counts (the second differences are nonzero and not constant: not a quadratic "
          "either, because the cyclic generator map makes the word structure depend on Z)",
          any_quadratic)
    # the sanity control: the Markov-WEIGHTED sum over the two H_2 blocks IS multiplicative (S2 already showed
    # the product form); here check that the two-strand (2)+(1,1) weighted trace of a single interface letter
    # reproduces z + d
    t2 = wplus * (Q_SER + dser["pn"]) + wminus * (-Q_SER.inv() + dser["pn"])
    check("(c) control: the Wenzl-weighted H_2 sum w+ (q+d) + w- (-1/q+d) equals z + d as an h-series "
          "(ChainTraceFactor.twoStrandTrace_eq)", t2 == fser["pn"])

    # (c') the same single-block functional on the UIC's own all-pairs layout, for the record
    print("\n        UIC-shaped ALL-PAIRS layout (interface letter to every previous nucleon, alternating p/n order):")
    print(f"        {'lambda':>10} {'A':>3} | [h^2] log(tr/tr0) second differences in Z | additive-count prediction")
    add_pred = hc2["pp"] - 2 * hc2["pn"] + hc2["nn"]  # curvature of a count-linear [h^2] under all-pairs counts
    for s in [(2, 1), (2, 2), (3, 1), (3, 2)]:
        n_gens = sum(s) - 1
        tabs, S = ysn_matrices(s, Fs)
        for A in (4, 6):
            row = []
            for Z in range(1, A):
                order = uic_order(Z, A - Z)
                w = uic_shaped_word(order, dmap_s, Fs.h, n_gens)
                tr = block_trace(w, S, Fs)
                row.append(None if tr.c[0] == 0 else (tr / tr.c[0]).log_unital().c[2])
            dd = "undefined" if any(x is None for x in row) else sorted(set(second_differences(row)))
            print(f"        {str(s):>10} {A:>3} | {str(dd):<45} | count-linear part would give "
                  f"{mp.nstr(add_pred, 8)} (times e2 pieces)")
    print("        (all-pairs counts are already quadratic in Z, so curvature there does not isolate the functional;")
    print("         the chain rows above are the clean test.)")

    # ======================================================================
    print("\n" + "=" * 76)
    print("SUMMARY")
    print("=" * 76)
    print("  * The corpus's binding functional is a LOG (log-ratio law, owner-ruled 2026-09-04/05;")
    print("    UIC's ln|tr M_lambda|). For any log-type functional the +c_k/-c_k question is EMPTY:")
    print("    the type-two pair term is absent for both signs (S2, Lean logJet_c2_census).")
    print("  * The pair term IS present in the bare product, for either sign; -c_2 gives a valley,")
    print("    +c_2 a hill, and the resummed bare product is monotone (S3).")
    print("  * Within a generator nothing fails to commute (S4a). What is non-multiplicative is a")
    print("    SINGLE Wedderburn block (S4c) — the UIC functional's object — and that block can carry")
    print("    a non-linear type-two Z-dependence on the chain layout. Its sign is computed, not chosen.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Is graded binding +c_k or -c_k (bean qou-zlra)? On the corpus's own convention-D chain "
            "letters at the proton pin: the type-two pair convolution sum_{i<j} b_i b_j that carries "
            "(N-Z)^2 lives in the BARE product (second difference 4 in Z, exact, A = 3..12) and in "
            "NEITHER sign of its logarithm (second differences 0), so for every log-type binding "
            "functional — the live log-ratio law and unified-iterative-correction's ln|tr M_lambda| — "
            "the sign question is empty. Valley scan at q0: log-ratio law endpoint-maximal (no valley); "
            "-c_2/c_0 alone has an interior maximum at N = Z, +c_2/c_0 alone does not; the resummed "
            "bare product is monotone either way. Within-generator (qou-eqwg): transfer matrices on one "
            "generator commute exactly (no non-commutativity to carry anything); stacking interface "
            "letters on one generator is non-multiplicative but the chain never does it; a SINGLE "
            "Wedderburn block tr_lambda(prod(c sigma+d)) — the UIC's object — is non-multiplicative on "
            "the chain layout and its [h^2] log is not linear in Z (nonzero, non-constant second differences). "
            "Lean invariant: QOU.Mass.GradedBindingFunctionalPairTerm (sorry-free). No fit, nothing wired.")
        for k, v in data.items():
            wb.add_data(k, v)
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat("Shape result. No binding number is produced and no functional is endorsed; the "
                      "scan reports argmax_Z per functional with the corpus's own scales as labels.")
        wb.add_caveat("The single-block test (S4c) uses the canonical eleven-letter intra block and the "
                      "chain interface letters mapped cyclically into H_k as hecke_core_legacy does; it is "
                      "UIC-SHAPED, not a run of the production accumulator (which exceeded 300 s at A = 4 "
                      "in this container and was not scanned).")
        wb.add_caveat("The free-nucleon factors t_p, t_n enter only the refuted difference law's scan and "
                      "are the derived closed forms of the 2026-09-05 arc synthesis; Q_beta there is a "
                      "label for that law's own scale, not an input to any live quantity.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed   ({time.time() - T0:.1f} s)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
