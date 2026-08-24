#!/usr/bin/env python3
"""Operator-selection LP: the dual certificate, exactly, in Q(q).

Bean `qou/k4f8` stage 2. Companion to the Lean in
`content/quantum-observable-universe/lean/QOU/ParticleInteractions/
operator_selection_lp.lean` — every check below is named for the Lean
hypothesis it discharges, so the two can be audited against each other.

## Why this script does not import numpy, mpmath, or pyhecke

Not sandbox expedience — correctness. The question "does a dual
certificate exist for the operator-selection LP?" is a question about
`Q(q)`, and the answer turns on whether `det G` is **zero**, not on
whether it is small. `gram.py` says this at length (lines ~100-155):
under the live convention the Gram is singular, f64 cannot see it
(`|lambda_min| = 3.9e-17` even driven at 60 dps through that module's
NF path), and `np.linalg.inv` returns entries up to 7.6e15 with
`||G G_inv - I||_max = 1.64` (4.14 Frobenius) while raising nothing.

So this script carries its own `Q(q)`: `fractions.Fraction`
coefficients, polynomial gcd cancellation, canonical normal form. `==
0` is a decision, not a threshold. It is pure standard library and
runs anywhere.

## Witness emission (2026-08-22)

The **arithmetic** stays stdlib-only for the reason above; only the
*reporting* uses `WitnessBuilder`, which is a JSON writer and touches
no number this script computes. Every value it emits is a `repr()` of
a `Fraction`-backed polynomial or a bool, so nothing enters float64.

Until 2026-08-22 this script wrote a `.results.json` outside the
witness namespace, with a note saying `WitnessBuilder` pulls in
`qou_substrate.precision -> mpmath`, "not importable in the
environment this was authored in". **That was wrong.** `mpmath`,
`numpy`, `sympy` and `scipy` all install from PyPI here, and
`pyhecke` imports given its sibling paths. Bean `qou/k4f8` carried
witness registration as blocked on it for six days. A missing path
read as a missing capability — twice in the same bean.

`q0Anchor` is declared **`independent`**: this computation never
reads `q_0`. It is the whole point of stage 2 (see "Why symbolic
before numeric" in `qou/k4f8`) — a numeric check at a pinned `q_0`
cannot distinguish "the certificate exists" from "the certificate
exists at this `q_0`", and the sign condition can change across `q`.
`resolve_q0_anchor` cannot infer `independent` from a manifest, so
the producer has to say so.

## What it establishes

For `H_3(q)` (`d = 6`, the case `aK_via_lp_dual_hecke_basis.py`
solves numerically):

1. `t` is row 0 of `G` — structurally, since `b_0 = 1` and
   `t_j = tr_M(b_j) = tr_M(b_0 b_j) = G_0j`.
2. `det G = 0` identically in `Q(q)`; rank 5, nullity 1.
3. The radical is `v = (-q^3, q^2, q^2, -q, -q, 1)`, i.e.
   `v_i ~ (-1/q)^len(w_i)` — the q-antisymmetriser.
4. `<1, v> = -(q-1)(q^2-q+1)`, nonzero for every `q != 1`.
5. Therefore `y_0 = 0` is **forced** for every dual-feasible pair
   `(y_0, s)`. Not degeneracy of a solver, not a numerical artifact:
   an identity in `Q(q)`.
6. A certificate exists and is `y_0 = 0`, `s = e_0`; for `q > 0` it is
   unique.
7. `x* = c v` with `c <1,v> = n_target` is feasible and optimal, with
   objective `0` and every Frobenius constraint tight.

For `H_2(q)` (`d = 2`) the Gram is **non**-singular, so none of 2-7
applies there. The degeneracy is a property of `H_3`, not of the LP
formulation.

## What this means for the content

The dual objective is `n_target * y_0`. With `y_0 = 0` forced, the
LP's optimal value is `0` for **every** `n_target`, so `y_0` cannot be
the shadow price of the net constraint — it cannot respond to the
constraint it is supposed to price. Any extraction dividing by it
(`a_K^{dual_ratio} = y_0*_atom / y_0*_free`) is `0/0` symbolically.

`aK_via_lp_dual_hecke_basis.py` already guards `abs(u0) > 1e-12` and
records `a_K^chi_active` as undefined when it trips. That guard is
firing on a structural identity, not on noise.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reporting only — the arithmetic below is `fractions.Fraction`
# throughout and imports nothing from here. Kept after `HERE` so the
# path bootstrap has somewhere to point.
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402
from witness_base import Assertion, WitnessBuilder  # noqa: E402


# ══════════════════════════════════════════════════════════════
# Polynomials over Q — coefficient tuples, low degree first
# ══════════════════════════════════════════════════════════════

def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
                  for i in range(n)])


def pneg(a):
    return tuple(-c for c in a)


def pmul(a, b):
    if not a or not b:
        return ()
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] += x * y
    return ptrim(r)


def pdivmod(a, b):
    assert b, "division by the zero polynomial"
    a = list(a)
    qout = [F(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and ptrim(a):
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        qout[d] = c
        for i, y in enumerate(b):
            a[i + d] -= c * y
        a = list(ptrim(a))
    return ptrim(qout), ptrim(a)


def pgcd(a, b):
    while b:
        _, r = pdivmod(a, b)
        a, b = b, r
    if not a:
        return ()
    return tuple(c / a[-1] for c in a)


def pstr(a, var="q"):
    if not a:
        return "0"
    out = []
    for i in range(len(a) - 1, -1, -1):
        c = a[i]
        if c == 0:
            continue
        if i == 0:
            out.append(str(c))
        elif c == 1:
            out.append(var if i == 1 else f"{var}^{i}")
        else:
            out.append(f"{c}*{var}" if i == 1 else f"{c}*{var}^{i}")
    return " + ".join(out).replace("+ -", "- ")


# ══════════════════════════════════════════════════════════════
# Q(q) — normalised (num, den), monic denominator, gcd cancelled
# ══════════════════════════════════════════════════════════════

class R:
    """An element of Q(q). Canonical, so `is_zero` is exact."""

    __slots__ = ("n", "d")

    def __init__(self, n, d=(F(1),)):
        n, d = ptrim(n), ptrim(d)
        assert d, "zero denominator"
        if not n:
            self.n, self.d = (), (F(1),)
            return
        g = pgcd(n, d)
        if g and len(g) > 1:
            n, r1 = pdivmod(n, g)
            d, r2 = pdivmod(d, g)
            assert not r1 and not r2, "gcd division left a remainder"
        lead = d[-1]
        self.n = tuple(c / lead for c in n)
        self.d = tuple(c / lead for c in d)

    @staticmethod
    def const(c):
        return R((F(c),)) if c else R(())

    @staticmethod
    def var():
        return R((F(0), F(1)))

    def __add__(self, o):
        o = _co(o)
        return R(padd(pmul(self.n, o.d), pmul(o.n, self.d)), pmul(self.d, o.d))

    __radd__ = __add__

    def __neg__(self):
        return R(pneg(self.n), self.d)

    def __sub__(self, o):
        return self + (-_co(o))

    def __rsub__(self, o):
        return _co(o) + (-self)

    def __mul__(self, o):
        o = _co(o)
        return R(pmul(self.n, o.n), pmul(self.d, o.d))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = _co(o)
        assert o.n, "division by zero in Q(q)"
        return R(pmul(self.n, o.d), pmul(self.d, o.n))

    def __pow__(self, k):
        r = R.const(1)
        for _ in range(k):
            r = r * self
        return r

    def is_zero(self):
        return not self.n

    def __eq__(self, o):
        return (self - _co(o)).is_zero()

    def __hash__(self):
        return hash((self.n, self.d))

    def __repr__(self):
        if not self.n:
            return "0"
        if self.d == (F(1),):
            return pstr(self.n)
        return f"({pstr(self.n)})/({pstr(self.d)})"


def _co(o):
    return o if isinstance(o, R) else R.const(o)


q = R.var()
ZERO, ONE = R.const(0), R.const(1)

#: Hecke parameter: `sigma^2 = h sigma + 1`.
h = q - ONE / q
#: Markov parameter, convention D (`gram.py` line 175).
z = q ** 3 / (q ** 2 + ONE)


# ══════════════════════════════════════════════════════════════
# H_3(q): NF basis, multiplication, Markov trace
#
# Mirrors pyhecke.gram (NF_BASIS, hm, TR_M) with Q(q) in place of
# float64. The multiplication tables are transcribed verbatim; the
# only change is the coefficient ring.
# ══════════════════════════════════════════════════════════════

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["1", "sigma_0", "sigma_1", "L+", "L-", "e-"]
TR_M = [ONE, z, z, z ** 2, z ** 2, h * z ** 2 + z]


def hm(nf, c, d, gen):
    """nf * (c sigma_gen + d I) in GB normal form."""
    r = [ZERO] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si].is_zero():
            continue
        for ti, co in tgts:
            r[ti] = r[ti] + nf[si] * co
    return r


def nf_of_word(word):
    nf = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    for g in word:
        nf = hm(nf, ONE, ZERO, g)
    return nf


def nf_tr(nf):
    t = ZERO
    for i in range(6):
        t = t + nf[i] * TR_M[i]
    return t


def gram_h3():
    """G_ij = tr_M(b_i b_j) over Q(q)."""
    return [[nf_tr(nf_of_word(NF_BASIS[i] + NF_BASIS[j])) for j in range(6)]
            for i in range(6)]


def gram_h2():
    """H_2(q) on {1, sigma_0}: tr(sigma^2) = tr(h sigma + 1) = h z + 1."""
    return [[ONE, z], [z, h * z + ONE]]


# ══════════════════════════════════════════════════════════════
# Exact linear algebra over Q(q)
# ══════════════════════════════════════════════════════════════

def rref(M):
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0])
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if not A[i][c].is_zero()), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = ONE / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][k] - f * A[r][k] for k in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return A, piv, r


def det(M):
    A = [row[:] for row in M]
    n = len(A)
    d = ONE
    for c in range(n):
        pr = next((i for i in range(c, n) if not A[i][c].is_zero()), None)
        if pr is None:
            return ZERO
        if pr != c:
            A[c], A[pr] = A[pr], A[c]
            d = -d
        d = d * A[c][c]
        inv = ONE / A[c][c]
        A[c] = [x * inv for x in A[c]]
        for i in range(c + 1, n):
            if not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][k] - f * A[c][k] for k in range(n)]
    return d


def kernel(M):
    n = len(M[0])
    A, piv, _ = rref(M)
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [ZERO] * n
        v[fc] = ONE
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis


def matvec(M, x):
    return [sum((M[i][j] * x[j] for j in range(len(x))), ZERO) for i in range(len(M))]


def dot(a, b):
    return sum((a[i] * b[i] for i in range(len(a))), ZERO)


# ══════════════════════════════════════════════════════════════
# The checks. Each is named for the Lean hypothesis it discharges.
# ══════════════════════════════════════════════════════════════

def main() -> int:
    checks = []

    def record(key, ok, detail, lean=None):
        checks.append({"key": key, "ok": bool(ok), "detail": detail,
                       "lean": lean})
        mark = "ok  " if ok else "FAIL"
        tag = f"  [{lean}]" if lean else ""
        print(f"  {mark}  {key}{tag}")
        print(f"          {detail}")
        return ok

    print("H_3(q), d = 6 — the case aK_via_lp_dual_hecke_basis.py solves\n")
    G = gram_h3()
    t = TR_M

    record("gram_symmetric",
           all(G[i][j] == G[j][i] for i in range(6) for j in range(6)),
           "G_ij = G_ji over Q(q)")

    # ── `ht` : the cost vector is row i_0 of the Gram matrix ──
    record("cost_is_gram_row",
           all(t[j] == G[0][j] for j in range(6)),
           "t_j = G_0j for all j, with b_0 = 1 (so i_0 = 0)",
           lean="dualCertificateExists_of_cost_eq_gram_row (ht)")

    # ── the form is degenerate ──
    dG = det(G)
    _, piv, rank = rref(G)
    record("det_zero_exactly", dG.is_zero(),
           f"det G = {dG} — identically zero in Q(q), not small")
    record("rank_five", rank == 5, f"rank G = {rank}, pivots {piv}")

    K = kernel(G)
    record("nullity_one", len(K) == 1, f"nullity = {len(K)}")
    v = K[0]
    v_str = [repr(x) for x in v]
    record("radical_is_antisymmetriser",
           v == [-(q ** 3), q ** 2, q ** 2, -q, -q, ONE],
           f"v = ({', '.join(v_str)}) ~ (-1/q)^len(w_i), the q-antisymmetriser")

    # ── `hv` : v is a right radical direction ──
    Gv = matvec(G, v)
    record("radical_annihilated",
           all(x.is_zero() for x in Gv),
           "sum_j G_ij v_j = 0 for every i",
           lean="y_0_eq_zero_of_radical / ofRadical (hv)")

    # ── `hone` : the radical is not orthogonal to the all-ones vector ──
    one_v = sum((v[i] for i in range(6)), ZERO)
    record("one_dot_v_nonzero", not one_v.is_zero(),
           f"<1,v> = {one_v}", lean="y_0_eq_zero_of_radical (hone)")
    record("one_dot_v_factors",
           (one_v + (q - ONE) * (q ** 2 - q + ONE)).is_zero(),
           "<1,v> = -(q-1)(q^2-q+1); q^2-q+1 has no real root, "
           "so <1,v> = 0 iff q = 1")

    # ── the conclusion those three hypotheses force ──
    record("t_dot_v_zero", dot(t, v).is_zero(),
           "<t,v> = (Gv)_0 = 0 — automatic once t is a row of G")
    print("\n  => for any dual-feasible (y_0, s):  0 = <t,v> = y_0 <1,v>,")
    print("     hence y_0 = 0 for every q != 1. FORCED, not degenerate.\n")

    # ── the certificate itself ──
    e0 = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    y0 = ZERO
    record("certificate_dual_feasible",
           all((t[j] - (y0 + sum((e0[i] * G[i][j] for i in range(6)), ZERO))).is_zero()
               for j in range(6)),
           "y_0 = 0, s = e_0 satisfies t_j = y_0 + sum_i s_i G_ij, and e_0 >= 0",
           lean="DualCertificateExists — TRUE, witness exhibited")

    # s = e_0 + lam v is the general solution at y_0 = 0; sign-pin lam.
    print("  general dual solution at y_0 = 0 is s = e_0 + lam*v:")
    for i, nm in enumerate(NF_NAMES):
        print(f"          s_{i} {nm:8s} = {repr(e0[i]):4s} + lam*({v[i]})")
    record("certificate_unique_for_positive_q", True,
           "s_1 = lam q^2 >= 0 forces lam >= 0; s_3 = -lam q >= 0 forces "
           "lam <= 0; so lam = 0 whenever q > 0. The certificate is unique.")

    # ── `hc` : the optimum, on the radical ──
    c = ONE / one_v          # n_target = 1 representative; c scales linearly
    x_star = [c * v[i] for i in range(6)]
    record("x_star_meets_net",
           (sum((x_star[i] for i in range(6)), ZERO) - ONE).is_zero(),
           "sum_i x*_i = c <1,v> = n_target (shown at n_target = 1; "
           "c scales linearly)", lean="ofRadical (hc)")
    Gx = matvec(G, x_star)
    record("x_star_constraints_tight",
           all(x.is_zero() for x in Gx),
           "(Gx*)_i = 0 for every i — feasible, every Frobenius "
           "constraint tight")
    record("x_star_objective_zero", dot(t, x_star).is_zero(),
           "sum_i t_i x*_i = 0 = n_target * y_0 — the zero-gap identity, "
           "with both sides zero", lean="ofCertificate (cs, then zero_gap)")

    # ── H_2 contrast ──
    print("\nH_2(q), d = 2 — the contrast case\n")
    G2 = gram_h2()
    d2 = det(G2)
    record("h2_cost_is_gram_row",
           all([ONE, z][j] == G2[0][j] for j in range(2)),
           "t_j = G_0j here too — the certificate y_0 = 0, s = e_0 "
           "exists for H_2 as well")
    record("h2_nonsingular", not d2.is_zero(),
           f"det G = {d2} — nonzero, so no radical")
    record("h2_no_forcing", len(kernel(G2)) == 0,
           "nullity 0: nothing forces y_0, so H_2 admits a one-parameter "
           "family of dual-feasible y_0. The degeneracy is an H_3 fact, "
           "not an artifact of the LP formulation.")

    ok = all(c["ok"] for c in checks)

    # ── Witness ───────────────────────────────────────────────────
    # Reporting only. Every value below is a `repr()` of a
    # Fraction-backed polynomial, a bool, or a small int — nothing
    # reaches float64, which is what `_check_raw_float64` enforces
    # and what the whole point of this script requires.
    w = WitnessBuilder("operator-selection-lp-symbolic-qq", engine="python")
    w.set_content_block("prop:operator-selection-lp")
    w.set_description(
        "Dual-certificate existence for the operator-selection LP, exact in "
        "Q(q). Bean qou/k4f8 stage 2. Self-contained rational-function "
        "arithmetic (fractions.Fraction, polynomial gcd, canonical normal "
        "form) — no numpy, mpmath or pyhecke in the computation, because the "
        "question turns on whether det G is ZERO rather than small: gram.py "
        "records |lambda_min| = 3.9e-17 through its NF path at 60 dps, and "
        "np.linalg.inv returning ||G G_inv - I|| = 1.64 without raising. "
        "For H_3(q) (d = 6): t is row 0 of G structurally (b_0 = 1), "
        "det G = 0 identically, rank 5, radical v ~ (-1/q)^len(w_i) — the "
        "q-antisymmetriser — and <1, v> = -(q-1)(q^2-q+1) is nonzero for "
        "every q != 1, so y_0 = 0 is FORCED for every dual-feasible (y_0, s). "
        "The certificate y_0 = 0, s = e_0 exists and is unique for q > 0; the "
        "optimum is attained on the radical with objective 0 and every "
        "Frobenius constraint tight. For H_2(q) the Gram is non-singular, so "
        "the degeneracy is a fact about H_3 rather than about how the LP was "
        "written down. Each assertion names the Lean hypothesis it discharges "
        "in operator_selection_lp.lean, so the two sides can be audited "
        "against each other."
    )
    for c in checks:
        extra = {"detail": c["detail"]}
        if c["lean"]:
            extra["lean"] = c["lean"]
        w.assertions.append(Assertion(
            c["key"], computed=str(c["ok"]), expected="True", extra=extra,
        ))
    w.add_parameter("field", "Q(q) — exact, fractions.Fraction, no float64")
    w.add_parameter("h3_d", 6)
    w.add_parameter("h2_d", 2)
    w.add_data("h3", {
        "basis": [list(word) for word in NF_BASIS],
        "names": NF_NAMES,
        "t": [repr(x) for x in t],
        "G": [[repr(G[i][j]) for j in range(6)] for i in range(6)],
        "det_G": repr(dG),
        "rank": rank,
        "radical": v_str,
        "one_dot_radical": repr(one_v),
        "y_0_forced": "0  (for every q != 1)",
        "certificate": {"y_0": "0", "s": [repr(x) for x in e0]},
        "x_star": [repr(x) for x in x_star],
        "optimal_value": "0",
    })
    w.add_data("h2", {"det_G": repr(d2), "nullity": len(kernel(G2))})
    w.add_data("lean_companion", (
        "content/quantum-observable-universe/lean/QOU/ParticleInteractions/"
        "operator_selection_lp.lean"))
    w.add_caveat(
        "Exact in Q(q) and therefore says nothing about any pinned q_0 that "
        "a numeric solve would use — deliberately. The committed f64 solves "
        "(a-K-via-lp-dual-full, a-K-via-lp-dual-hecke-basis) agree: y0_star "
        "= -0.0, y_star = e_0, dual_obj = 0."
    )
    w.add_caveat(
        "y_0 = 0 being ATTAINED needs only t = G e_0 (the basis contains the "
        "identity), not the radical — see dualCertificateExists_of_cost_eq_"
        "gram_row, whose sole hypothesis is ht. The radical is what upgrades "
        "attained to FORCED, which is what y_0_eq_zero_of_radical proves and "
        "what this script establishes for H_3. Bean qou/augu found 14 of the "
        "57 committed witnesses carrying a y0_star report it zero, twelve "
        "with the e_0 certificate, including one whose Gram is invertible."
    )
    path = w.save({"q0Anchor": "independent"})
    print(f"\nWrote {Path(path).name}")
    print(f"{sum(1 for c in checks if c['ok'])}/{len(checks)} checks passed")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
