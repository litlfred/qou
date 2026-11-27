#!/usr/bin/env python3
"""qcd_spin_factor_probe -- a spin factor separate from colour (beans qou-ni4b, qou-bwwr; #9058).

Pre-registration: PREREGISTRATION-spin-factor.md (commit 2abaa8ed425, pushed before this file).
Constructions P1-P3 and the P3 acceptance test are fixed there. Every member is reported.

Exact arithmetic only: sympy over Q(p, r, q), Python Fraction, and an integer Laurent-polynomial
class. No float64 anywhere (no float(), no math / statistics over floats).
Output: qcd_spin_factor_probe.out.json next to this file.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

q, p, r = sp.symbols("q p r", positive=True)
HERE = Path(__file__).resolve().parent
OUT: dict = {"checks": [], "P1": {}, "P2": {}, "P3": {}}


def check(name, ok, detail="", posthoc=False):
    OUT["checks"].append({"name": name, "pass": bool(ok), "detail": str(detail),
                          "posthoc": posthoc})
    print(f"[{'PASS' if ok else 'FAIL'}]{' (post-hoc)' if posthoc else ''} {name}  {detail}")
    return bool(ok)


# =============================================================================================
# P1 -- exhaustive strand-wise colour x spin Hecke class, via seminormal irreps of H_3
# =============================================================================================
def hecke_irreps(t):
    """Seminormal Hecke generators (T1, T2) of H_3(t), (T - t)(T + t^-1) = 0, keyed by shape."""
    T2 = sp.Matrix([[-1 / (t * (t**2 + 1)), 1],
                    [(t**4 + t**2 + 1) / (t**2 + 1)**2, t**3 / (t**2 + 1)]])
    return {
        (3,): (sp.Matrix([[t]]), sp.Matrix([[t]])),
        (2, 1): (sp.diag(t, -1 / t), T2),
        (1, 1, 1): (sp.Matrix([[-1 / t]]), sp.Matrix([[-1 / t]])),
    }


def verify_irreps(t):
    ok = True
    for lam, (A, B) in hecke_irreps(t).items():
        n = A.shape[0]
        I = sp.eye(n)
        for T in (A, B):
            ok &= sp.simplify((T - t * I) * (T + I / t)) == sp.zeros(n)
        ok &= sp.simplify(A * B * A - B * A * B) == sp.zeros(n)
    return ok


def projectors(T, t):
    n = T.shape[0]
    I = sp.eye(n)
    return {"S": (T + I / t) / (t + 1 / t), "A": (t * I - T) / (t + 1 / t)}


LABELS = ("S", "A")
EIG = {"+": q, "-": -1 / q}


def assignments():
    """All 16 maps (a, b) -> eigenvalue sign."""
    keys = [(a, b) for a in LABELS for b in LABELS]
    for signs in itertools.product("+-", repeat=4):
        yield dict(zip(keys, signs))


def classify(assign):
    s = assign
    transported = (s[("S", "S")] == s[("A", "A")] and s[("S", "A")] == s[("A", "S")]
                   and s[("S", "S")] != s[("S", "A")])
    colour_fixed = s[("S", "S")] == s[("A", "S")] and s[("S", "A")] == s[("A", "A")]
    spin_fixed = s[("S", "S")] == s[("S", "A")] and s[("A", "S")] == s[("A", "A")]
    if transported:
        return "transported"
    if colour_fixed and spin_fixed:
        return "scalar"
    if colour_fixed:
        return "colour-fixed (K0-type: R = 1_c (x) X_s)"
    if spin_fixed:
        return "spin-fixed (R = X_c (x) 1_s)"
    return "mixed"


def braid_numerators(assign, pc, rs, N):
    """Numerators of sigma1 sigma2 sigma1 - sigma2 sigma1 sigma2 over all irrep pairs."""
    cir = hecke_irreps(pc)
    sir = hecke_irreps(rs)
    nums = set()
    for lam, (C1, C2) in cir.items():
        if len(lam) > N:
            continue
        PC = [projectors(C1, pc), projectors(C2, pc)]
        for mu, (S1, S2) in sir.items():
            if len(mu) > 2:
                continue
            PS = [projectors(S1, rs), projectors(S2, rs)]
            R = []
            for i in range(2):
                M = sp.zeros(C1.shape[0] * S1.shape[0])
                for (a, b), sg in assign.items():
                    M += EIG[sg] * sp.kronecker_product(PC[i][a], PS[i][b])
                R.append(M)
            res = R[0] * R[1] * R[0] - R[1] * R[0] * R[1]
            for e in res:
                e = sp.cancel(sp.together(e))
                if e != 0:
                    num, _ = sp.fraction(e)
                    nums.add(sp.factor(sp.expand(num)))
    return sorted(nums, key=sp.default_sort_key)


def run_P1():
    check("P1 seminormal H_3 irreps satisfy Hecke + braid (symbolic t)", verify_irreps(q))
    rows = []
    for N in (2, 3, 4):
        for assign in assignments():
            kind = classify(assign)
            tag = "".join(assign[(a, b)] for a in LABELS for b in LABELS)
            for (pc, rs, pr_label) in ((sp.Integer(1), sp.Integer(1), "p=r=1"),
                                       (sp.Integer(1), r, "p=1, r sym"),
                                       (p, sp.Integer(1), "p sym, r=1"),
                                       (p, r, "p, r sym")):
                nums = braid_numerators(assign, pc, rs, N)
                if not nums:
                    gb = ["0"]
                    generic = True
                else:
                    # lex with p > r > q, so the GB meets Q[q] in the elimination ideal.
                    # The pre-registration fixed "lex Groebner basis in (p, r, q)" but not the
                    # variable order; "braids at generic q" is decided HERE as: no GB element
                    # lies in Q[q] alone (p, r may be tied to q, e.g. r = q). The first run
                    # used order (q, p, r) and wrongly read every non-empty GB as "not
                    # generic"; corrected post-hoc, see RESULT.md.
                    gens = [v for v in (p, r, q) if any(v in e.free_symbols for e in nums)]
                    G = sp.groebner(nums, *gens, order="lex")
                    gb = [str(sp.factor(g)) for g in G.exprs]
                    elim_q = [g for g in G.exprs if g.free_symbols <= {q}]
                    generic = not elim_q
                rows.append({"N": N, "lambda_SS,SA,AS,AA": tag, "kind": kind,
                             "params": pr_label, "braid_generic": generic,
                             "groebner_lex": gb})
    OUT["P1"]["rows"] = rows
    # ---- parameter-tie test (post-hoc refinement of "braids at generic q", see RESULT.md):
    # for (p, r) in T x T, T = {1, -1, q, -q, 1/q, -1/q}, does the residual vanish
    # identically in q?  Also flag cyclotomic factors in p or r alone (roots of unity,
    # e.g. p^2 +- p + 1 = 0, i.e. [3]_{+-p} = 0: a non-semisimple colour parameter).
    T = [sp.Integer(1), sp.Integer(-1), q, -q, 1 / q, -1 / q]
    ties = []
    for N in (2, 3, 4):
        for assign in assignments():
            tag = "".join(assign[(a, b)] for a in LABELS for b in LABELS)
            nums = braid_numerators(assign, p, r, N)
            ok_ties = []
            for pv in T:
                for rv in T:
                    if all(sp.simplify(e.subs({p: pv, r: rv})) == 0 for e in nums):
                        ok_ties.append(f"(p,r)=({pv},{rv})")
            ties.append({"N": N, "lambda_SS,SA,AS,AA": tag, "kind": classify(assign),
                         "ties_braiding_identically_in_q": ok_ties})
    OUT["P1"]["tie_test"] = ties
    # summaries
    for N in (2, 3, 4):
        tr = [x for x in rows if x["N"] == N and x["kind"] == "transported"]
        check(f"P1 N={N}: no transported member braids at generic q (all 2x4 param cases)",
              all(not x["braid_generic"] for x in tr),
              "; ".join(f"{x['lambda_SS,SA,AS,AA']}[{x['params']}] GB={x['groebner_lex']}"
                        for x in tr))
        gen = sorted({(x["lambda_SS,SA,AS,AA"], x["kind"], x["params"])
                      for x in rows if x["N"] == N and x["braid_generic"]})
        OUT["P1"][f"generic_braiders_N{N}"] = gen
        # Pre-registered prediction, as written, FAILS once p, r are left free: mixed members
        # have components of the Groebner variety with q generic (p or r a root of unity at
        # N=3, 4; a tie [2]_q = [2]_p [2]_r at N=2). Kept as a recorded FAIL.
        check(f"P1 N={N}: every member braiding at generic q (p, r free) is colour-fixed, "
              "spin-fixed or scalar [pre-registered prediction]",
              all(k[1] != "transported" and k[1] != "mixed" for k in gen),
              f"{len(gen)} (assignment, param) cases; mixed: "
              + str([k for k in gen if k[1] == "mixed"]))
        tt = [x for x in OUT["P1"]["tie_test"] if x["N"] == N]
        okt = all((not x["ties_braiding_identically_in_q"]) == (x["kind"] in ("transported", "mixed"))
                  for x in tt)
        check(f"P1 N={N}: with (p,r) tied to q in {{+-1, +-q, +-1/q}}: transported and mixed members "
              "braid for NO tie; colour-fixed, spin-fixed and scalar members braid for some tie",
              okt, [(x["lambda_SS,SA,AS,AA"], x["ties_braiding_identically_in_q"]) for x in tt
                    if x["kind"] != "scalar"], posthoc=True)
    # N-independence for N >= 3
    def sig(N):
        return sorted((x["lambda_SS,SA,AS,AA"], x["params"], tuple(x["groebner_lex"]))
                      for x in rows if x["N"] == N)
    check("P1 N=3 and N=4 give identical Groebner bases (same irreps occur)", sig(3) == sig(4))


# ---------------------------------------------------------------- explicit cross-check (Fraction)
def jimbo_cols(d, t):
    """Jimbo R-check of U_t(gl_d) on C^d (x) C^d as {(i,j): {(k,l): coef}}, Fraction t."""
    cols = {}
    for i in range(d):
        for j in range(d):
            if i == j:
                cols[(i, j)] = {(i, i): t}
            elif i < j:
                cols[(i, j)] = {(j, i): Fraction(1)}
            else:
                cols[(i, j)] = {(j, i): Fraction(1), (i, j): t - 1 / t}
    return cols


def apply_cols(cols, vec):
    out = {}
    for k, c in vec.items():
        for k2, c2 in cols[k].items():
            out[k2] = out.get(k2, 0) + c * c2
    return {k: v for k, v in out.items() if v != 0}


def proj_cols(d, t, kind):
    R = jimbo_cols(d, t)
    cols = {}
    for key in R:
        v = {}
        Rv = R[key]
        if kind == "S":   # (R + 1/t)/(t + 1/t)
            for k, c in Rv.items():
                v[k] = v.get(k, 0) + c
            v[key] = v.get(key, 0) + 1 / t
        else:             # (t - R)/(t + 1/t)
            v[key] = v.get(key, 0) + t
            for k, c in Rv.items():
                v[k] = v.get(k, 0) - c
        cols[key] = {k: c / (t + 1 / t) for k, c in v.items() if c != 0}
    return cols


def strand_R(N, pc, rs, qq, assign):
    """R on W (x) W, W = C^N (x) C^2; basis ((c1,s1),(c2,s2))."""
    PC = {k: proj_cols(N, pc, k) for k in LABELS}
    PS = {k: proj_cols(2, rs, k) for k in LABELS}
    eig = {"+": qq, "-": -1 / qq}
    cols = {}
    for c1, s1, c2, s2 in itertools.product(range(N), range(2), range(N), range(2)):
        out = {}
        for (a, b), sg in assign.items():
            for (d1, d2), cc in PC[a][(c1, c2)].items():
                for (t1, t2), cs in PS[b][(s1, s2)].items():
                    key = ((d1, t1), (d2, t2))
                    out[key] = out.get(key, 0) + eig[sg] * cc * cs
        cols[((c1, s1), (c2, s2))] = {k: v for k, v in out.items() if v != 0}
    return cols


def braid_residual_explicit(N, pc, rs, qq, assign):
    R = strand_R(N, pc, rs, qq, assign)
    W = list(itertools.product(range(N), range(2)))

    def act(i, vec):
        out = {}
        for key, c in vec.items():
            pair = (key[i], key[i + 1])
            for (x, y), c2 in R[pair].items():
                k2 = key[:i] + (x, y) + key[i + 2:]
                out[k2] = out.get(k2, 0) + c * c2
        return {k: v for k, v in out.items() if v != 0}

    maxres = 0
    for b in itertools.product(W, repeat=3):
        v = {b: Fraction(1)}
        lhs = act(0, act(1, act(0, v)))
        rhs = act(1, act(0, act(1, v)))
        for k in set(lhs) | set(rhs):
            d = lhs.get(k, 0) - rhs.get(k, 0)
            if d != 0:
                maxres = max(maxres, abs(d))
    return maxres


def irrep_residual_zero(assign, pc, rs, qq, N):
    nums = braid_numerators(assign, p, r, N)
    subs = {p: pc, r: rs, q: qq}
    return all(sp.Rational(e.subs(subs)) == 0 for e in nums)


def run_P1_crosscheck():
    pts = [(Fraction(2), Fraction(3), Fraction(5)), (Fraction(1), Fraction(1), Fraction(1)),
           (Fraction(3, 2), Fraction(3, 2), Fraction(3, 2))]
    members = {"transported ++ (q,-q^-1,-q^-1,q)": dict(zip(
                   [(a, b) for a in LABELS for b in LABELS], "+--+")),
               "colour-fixed (q,-q^-1,q,-q^-1)": dict(zip(
                   [(a, b) for a in LABELS for b in LABELS], "+-+-")),
               "mixed (q,q,q,-q^-1)": dict(zip(
                   [(a, b) for a in LABELS for b in LABELS], "+++-"))}
    log = []
    allok = True
    for name, assign in members.items():
        for (pc, rs, qq) in pts:
            ex = braid_residual_explicit(3, pc, rs, qq, assign)
            ir = irrep_residual_zero(assign, sp.Rational(pc.numerator, pc.denominator),
                                     sp.Rational(rs.numerator, rs.denominator),
                                     sp.Rational(qq.numerator, qq.denominator), 3)
            agree = (ex == 0) == ir
            allok &= agree
            log.append(f"{name} @(p,r,q)=({pc},{rs},{qq}): explicit max|res|={ex}, "
                       f"irrep zero={ir}")
    OUT["P1"]["explicit_crosscheck"] = log
    check("P1 explicit 216-dim Fraction residual agrees with irrep result (3 members x 3 points)",
          allok, " | ".join(log))


# =============================================================================================
# P2 -- derived spin-only twist (Laurent-polynomial exact arithmetic, integer coefficients)
# =============================================================================================
class L:
    """Integer Laurent polynomial in q: dict exponent -> int."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k: v for k, v in (c or {}).items() if v != 0}

    @staticmethod
    def mono(e, k=1):
        return L({e: k})

    def __add__(self, o):
        d = dict(self.c)
        for k, v in o.c.items():
            d[k] = d.get(k, 0) + v
        return L(d)

    def __neg__(self):
        return L({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        d = {}
        for a, x in self.c.items():
            for b, y in o.c.items():
                d[a + b] = d.get(a + b, 0) + x * y
        return L(d)

    def iszero(self):
        return not self.c

    def sym(self):
        return sum(v * q**k for k, v in self.c.items())


ONE = L.mono(0)


class Op:
    """Sparse operator: col basis-tuple -> {row: L}."""

    def __init__(self, cols):
        self.cols = cols

    def __mul__(self, o):  # self * o  (apply o first)
        cols = {}
        for k, col in o.cols.items():
            out = {}
            for k2, c in col.items():
                for k3, c3 in self.cols[k2].items():
                    out[k3] = out.get(k3, L()) + c * c3
            cols[k] = {kk: v for kk, v in out.items() if not v.iszero()}
        return Op(cols)

    def __add__(self, o):
        cols = {}
        for k in self.cols:
            d = dict(self.cols[k])
            for k2, v in o.cols[k].items():
                d[k2] = d.get(k2, L()) + v
            cols[k] = {kk: v for kk, v in d.items() if not v.iszero()}
        return Op(cols)

    def scale(self, s):
        return Op({k: {k2: v * s for k2, v in col.items()} for k, col in self.cols.items()})

    def iszero(self):
        return all(not col for col in self.cols.values())

    def eq(self, o):
        return (self + o.scale(-ONE)).iszero()

    @staticmethod
    def identity(basis):
        return Op({b: {b: ONE} for b in basis})


def jimbo_local(d):
    """Jimbo R-check on C^d (x) C^d with Laurent entries (generic q)."""
    cols = {}
    h = L({1: 1, -1: -1})
    for i in range(d):
        for j in range(d):
            if i == j:
                cols[(i, j)] = {(i, i): L.mono(1)}
            elif i < j:
                cols[(i, j)] = {(j, i): ONE}
            else:
                cols[(i, j)] = {(j, i): ONE, (i, j): h}
    return cols


def swap_local(d):
    return {(i, j): {(j, i): ONE} for i in range(d) for j in range(d)}


def id_local(d):
    return {(i, j): {(i, j): ONE} for i in range(d) for j in range(d)}


def tensor_local(A, B):
    """Local 2-site op on (C^a (x) C^b) per site: strand state = (x, y)."""
    cols = {}
    for (x1, x2), ca in A.items():
        for (y1, y2), cb in B.items():
            out = {}
            for (u1, u2), va in ca.items():
                for (w1, w2), vb in cb.items():
                    key = ((u1, w1), (u2, w2))
                    out[key] = out.get(key, L()) + va * vb
            cols[((x1, y1), (x2, y2))] = {k: v for k, v in out.items() if not v.iszero()}
    return cols


def chain_gen(local, states, n, i):
    basis = list(itertools.product(states, repeat=n))
    cols = {}
    for b in basis:
        out = {}
        for (x, y), c in local[(b[i], b[i + 1])].items():
            k = b[:i] + (x, y) + b[i + 2:]
            out[k] = out.get(k, L()) + c
        cols[b] = {k: v for k, v in out.items() if not v.iszero()}
    return Op(cols), basis


def full_twist(local, states, n):
    gens = [chain_gen(local, states, n, i)[0] for i in range(n - 1)]
    basis = list(itertools.product(states, repeat=n))
    word = Op.identity(basis)
    for _ in range(n):
        for g in gens:
            word = g * word
    return word, basis


def content_sum(shape):
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


def two_row_shapes(n):
    return [(n - j, j) if j else (n,) for j in range(0, n // 2 + 1)]


def hook_f(shape):
    n = sum(shape)
    cols = [sum(1 for rr in shape if rr > j) for j in range(shape[0])]
    prod = 1
    for i, row in enumerate(shape):
        for j in range(row):
            prod *= (row - j - 1) + (cols[j] - i - 1) + 1
    f = 1
    for k in range(2, n + 1):
        f *= k
    return f // prod


def run_P2():
    s_states = [0, 1]
    # combined per-strand states (spin, isospin)
    cs = list(itertools.product(range(2), range(2)))
    RS = jimbo_local(2)
    cons = {"D (Deligne R_s(q) x P_I)": tensor_local(RS, swap_local(2)),
            "F (K0-type R_s(q) x 1_I)": tensor_local(RS, id_local(2)),
            "Y (symmetric R_s(q) x R_I(q))": tensor_local(RS, RS)}
    res = {}
    for name, loc in cons.items():
        g1, basis = chain_gen(loc, cs, 3, 0)
        g2, _ = chain_gen(loc, cs, 3, 1)
        braid = (g1 * g2 * g1).eq(g2 * g1 * g2)
        Id = Op.identity(basis)
        hecke = ((g1 + Id.scale(L.mono(1)).scale(-ONE)) *
                 (g1 + Id.scale(L.mono(-1)))).iszero()
        g1sq = g1 * g1
        quart = ((g1sq + Id.scale(-L.mono(2))) * (g1sq + Id.scale(-L.mono(-2)))).iszero()
        tw = {}
        for n in (3, 4):
            D, bas = full_twist(loc, cs, n)
            Ds, bs = full_twist(RS, s_states, n)
            # Delta^2_s (x) 1_I  and  Delta^2_s (x) Delta^2_I as ops on combined basis
            DI, bi = full_twist(RS, s_states, n)

            def lift(spin_op, iso_op):
                cols = {}
                for b in bas:
                    sk = tuple(x[0] for x in b)
                    ik = tuple(x[1] for x in b)
                    out = {}
                    for s2, cs_ in spin_op.cols[sk].items():
                        for i2, ci in iso_op.cols[ik].items():
                            k = tuple(zip(s2, i2))
                            out[k] = out.get(k, L()) + cs_ * ci
                    cols[b] = {k: v for k, v in out.items() if not v.iszero()}
                return Op(cols)

            IdI = Op.identity(list(itertools.product(s_states, repeat=n)))
            tw[n] = {"Delta2 = Delta2_s (x) 1_I": D.eq(lift(Ds, IdI)),
                     "Delta2 = Delta2_s (x) Delta2_I": D.eq(lift(Ds, DI))}
        res[name] = {"braid": braid, "hecke_q": hecke, "quartic (T^2-q^2)(T^2-q^-2)=0": quart,
                     "full_twist": {str(k): v for k, v in tw.items()}}
    OUT["P2"]["constructions"] = res
    check("P2 D, F, Y all satisfy the braid relation on 3 strands",
          all(v["braid"] for v in res.values()))
    check("P2 D (Deligne, isospin transported classically) is NOT Hecke; satisfies "
          "(T^2-q^2)(T^2-q^-2)=0", (not res["D (Deligne R_s(q) x P_I)"]["hecke_q"]) and
          res["D (Deligne R_s(q) x P_I)"]["quartic (T^2-q^2)(T^2-q^-2)=0"])
    check("P2 F (K0-type) is Hecke", res["F (K0-type R_s(q) x 1_I)"]["hecke_q"])
    check("P2 Y (symmetric) is NOT Hecke", not res["Y (symmetric R_s(q) x R_I(q))"]["hecke_q"])
    for nm in ("D (Deligne R_s(q) x P_I)", "F (K0-type R_s(q) x 1_I)"):
        check(f"P2 {nm}: full twist = Delta2_s (x) 1_I at n=3,4 (theta_I = 1 derived)",
              all(res[nm]["full_twist"][k]["Delta2 = Delta2_s (x) 1_I"] for k in ("3", "4")))
    nm = "Y (symmetric R_s(q) x R_I(q))"
    check(f"P2 {nm}: full twist = Delta2_s (x) Delta2_I, not Delta2_s (x) 1_I (n=3,4)",
          all(res[nm]["full_twist"][k]["Delta2 = Delta2_s (x) Delta2_I"] and
              not res[nm]["full_twist"][k]["Delta2 = Delta2_s (x) 1_I"] for k in ("3", "4")))

    # ------ Delta^2_s spectrum on (C^2)^{(x)n}: q^{2c(lambda)} via minimal polynomial + weights
    spec = {}
    allmin = True
    allwt = True
    for n in range(2, 7):
        D, bas = full_twist(RS, s_states, n)
        Id = Op.identity(bas)
        shapes = two_row_shapes(n)
        prod = Id
        for lam in shapes:
            prod = (D + Id.scale(-L.mono(2 * content_sum(lam)))) * prod
        allmin &= prod.iszero()
        # weight-space traces: weight k = number of 1's
        for k in range(0, n // 2 + 1):
            tr = L()
            for b in bas:
                if sum(b) == k:
                    tr = tr + D.cols[b].get(b, L())
            pred = L()
            for j in range(0, k + 1):
                lam = (n - j, j) if j else (n,)
                pred = pred + L.mono(2 * content_sum(lam), hook_f(lam))
            allwt &= (tr - pred).iszero()
        spec[n] = {str(lam): f"q^{2 * content_sum(lam)}" for lam in shapes}
    OUT["P2"]["Delta2_spin_spectrum"] = spec
    check("P2 Delta2_s on (C^2)^{(x)n}, n=2..6: min poly prod_lambda (Delta2 - q^{2c(lambda)}) = 0",
          allmin)
    check("P2 weight-space traces of Delta2_s match sum f^lambda q^{2c(lambda)} (n=2..6)", allwt)

    # ------ deuteron / singlet split with the full twist as theta
    c42, c33 = content_sum((4, 2)), content_sum((3, 3))
    th = {lam: q**(2 * content_sum(lam)) for lam in ((4, 2), (3, 3))}
    split = {
        "D": sp.factor(th[(4, 2)] * 1 - th[(3, 3)] * 1),
        "F": sp.factor(th[(4, 2)] * 1 - th[(3, 3)] * 1),
        "Y": sp.factor(th[(4, 2)] * th[(3, 3)] - th[(3, 3)] * th[(4, 2)]),
    }
    OUT["P2"]["deuteron_minus_singlet_twist_factor"] = {k: str(v) for k, v in split.items()}
    check("P2 content sums c(4,2)=5, c(3,3)=3 (agrees with Lean contentSum_four_two/_three_three)",
          c42 == 5 and c33 == 3)
    check("P2 split factor s*i' - s'*i: D, F give q^10 - q^6; Y gives 0",
          sp.expand(split["D"] - (q**10 - q**6)) == 0 and split["Y"] == 0, split)

    # ------ untwisted trace asymmetry: q-trace on spin vs ordinary trace on classical isospin
    n = 6
    D, bas = full_twist(RS, s_states, n)
    Id = Op.identity(bas)
    shapes = two_row_shapes(n)
    qtr = {}
    for lam in shapes:
        num = Id
        den = sp.Integer(1)
        for mu in shapes:
            if mu == lam:
                continue
            num = (D + Id.scale(-L.mono(2 * content_sum(mu)))) * num
            den *= q**(2 * content_sum(lam)) - q**(2 * content_sum(mu))
        trK = L()
        trP = L()
        for b in bas:
            dg = num.cols[b].get(b, L())
            w = (n - sum(b)) - sum(b)   # K = diag(q, q^-1) per strand
            trK = trK + dg * L.mono(w)
            trP = trP + dg
        qtr[lam] = (sp.factor(sp.cancel(trK.sym() / den)), sp.cancel(trP.sym() / den))
    ok_tr = True
    for lam in shapes:
        S2 = lam[0] - (lam[1] if len(lam) > 1 else 0)   # 2S
        qdim = sum(q**(S2 - 2 * m) for m in range(S2 + 1))
        ok_tr &= sp.simplify(qtr[lam][0] - hook_f(lam) * qdim) == 0
        ok_tr &= sp.simplify(qtr[lam][1] - hook_f(lam) * (S2 + 1)) == 0
    OUT["P2"]["isotypic_traces_n6"] = {str(k): {"q_trace": str(v[0]), "trace": str(v[1])}
                                       for k, v in qtr.items()}
    check("P2 n=6 isotypic traces: Tr(K P_lambda) = f^lambda [2S+1]_q, Tr P_lambda = f^lambda (2S+1)",
          ok_tr)
    deut = qtr[(4, 2)][0] * qtr[(3, 3)][1]
    sing = qtr[(3, 3)][0] * qtr[(4, 2)][1]
    diff = sp.factor(sp.simplify(deut - sing))
    OUT["P2"]["untwisted_trace_split_qtrace_spin_classical_iso"] = str(diff)
    check("P2 untwisted split (q-trace spin, classical-trace isospin) = 45 (q - q^-1)^2",
          sp.simplify(diff - 45 * (q - 1 / q)**2) == 0, diff)


# =============================================================================================
# P3 -- chromomagnetic background: covariance and the (2s)^2 - 1/3 acceptance test
# =============================================================================================
def run_P3_covariance():
    N = 3
    a1, a2 = sp.symbols("a1 a2")
    avec = [a1, a2, -a1 - a2]
    lam = {("S", "S"): sp.Symbol("l_SS"), ("S", "A"): sp.Symbol("l_SA"),
           ("A", "S"): sp.Symbol("l_AS"), ("A", "A"): sp.Symbol("l_AA")}

    def proj_sym(d, t, kind):
        R = sp.zeros(d * d)
        for i in range(d):
            for j in range(d):
                col = i * d + j
                if i == j:
                    R[col, col] = t
                elif i < j:
                    R[j * d + i, col] = 1
                else:
                    R[j * d + i, col] = 1
                    R[col, col] = t - 1 / t
        I = sp.eye(d * d)
        return (R + I / t) / (t + 1 / t) if kind == "S" else (t * I - R) / (t + 1 / t)

    out = {}
    for label, pc, rs in (("p=r=1", 1, 1), ("p, r sym", p, r), ("p=1, r sym", 1, r),
                          ("p sym, r=1", p, 1)):
        PC = {k: proj_sym(N, sp.sympify(pc), k) for k in LABELS}
        PS = {k: proj_sym(2, sp.sympify(rs), k) for k in LABELS}
        # basis ordering of W(x)W = ((c1,s1),(c2,s2)); build via index map
        idx = {}
        for c1, s1, c2, s2 in itertools.product(range(N), range(2), range(N), range(2)):
            idx[(c1, s1, c2, s2)] = len(idx)
        dim = len(idx)
        Rm = sp.zeros(dim)
        for (c1, s1, c2, s2), col in idx.items():
            for (d1, s1b, d2, s2b), row in idx.items():
                v = 0
                for (a, b), l in lam.items():
                    v += l * PC[a][d1 * N + d2, c1 * N + c2] * PS[b][s1b * 2 + s2b, s1 * 2 + s2]
                Rm[row, col] = sp.simplify(v)
        sz = [1, -1]

        def Hdiag(kind):
            vals = []
            for (c1, s1, c2, s2) in idx:
                if kind == "chromo":
                    vals.append(avec[c1] * sz[s1] + avec[c2] * sz[s2])
                elif kind == "charge":
                    vals.append(avec[c1] + avec[c2])
                else:
                    vals.append(sz[s1] + sz[s2])
            return vals

        conds = {}
        for kind in ("chromo", "charge", "zeeman"):
            Hv = Hdiag(kind)
            eqs = set()
            for row in range(dim):
                for col in range(dim):
                    e = Rm[row, col]
                    if e != 0 and sp.expand(Hv[row] - Hv[col]) != 0:
                        eqs.add(sp.factor(sp.cancel(e)))
            sol = sp.solve(list(eqs), list(lam.values()), dict=True) if eqs else [{}]
            conds[kind] = {"n_equations": len(eqs),
                           "solution": [{str(k): str(v) for k, v in s.items()} for s in sol]}
        out[label] = conds
    OUT["P3"]["covariance"] = out
    for kind in ("charge", "zeeman"):
        check(f"P3(i) {kind} background commutes with every member (all param cases)",
              all(out[k][kind]["n_equations"] == 0 for k in out))
    def same(sol, pairs):
        # sympy may solve for either member of a pair; compare as substitutions
        L4 = {sp.Symbol(n) for n in ("l_SS", "l_SA", "l_AS", "l_AA")}
        sub = {sp.Symbol(k): sp.sympify(v) for k, v in sol.items()}
        return all(sp.simplify(sp.Symbol(a).subs(sub) - sp.Symbol(b).subs(sub)) == 0
                   for a, b in pairs)
    cl = out["p=r=1"]["chromo"]["solution"]
    check("P3(i) p=r=1: chromomagnetic covariance <=> l_SS = l_AA and l_SA = l_AS (R in span{1,P})",
          len(cl) == 1 and len(cl[0]) == 2 and same(cl[0], [("l_SS", "l_AA"), ("l_SA", "l_AS")]),
          cl)
    for k in ("p, r sym", "p=1, r sym", "p sym, r=1"):
        sol = out[k]["chromo"]["solution"]
        # Pre-registered wording was "nothing at generic p or r"; the identity always commutes,
        # so the precise statement checked is: only scalar multiples of 1 (all l_ab equal).
        check(f"P3(i) {k}: chromomagnetic covariance forces R = l*1 (all l_ab equal)",
              len(sol) == 1 and len(sol[0]) == 3 and
              same(sol[0], [("l_SS", "l_AA"), ("l_SA", "l_AA"), ("l_AS", "l_AA")]), sol)


def run_P3_susceptibility():
    """Classical point p = r = q = 1: per-state susceptibilities of S_n-isotypic channels."""
    directions = {2: [[1, -1]], 3: [[1, -1, 0], [1, 1, -2]], 4: [[1, -1, 0, 0], [1, 1, -1, -1],
                                                               [1, 1, 1, -3]]}
    sz = [1, -1]
    results = {}
    kappa_all = {}
    dir_ok = True
    for N, dirs in directions.items():
        W = list(itertools.product(range(N), range(2)))
        for n in (1, 2, 3):
            perms = list(itertools.permutations(range(n)))

            def sign(pm):
                s = 1
                for i in range(n):
                    for j in range(i + 1, n):
                        if pm[i] > pm[j]:
                            s = -s
                return s

            fact = len(perms)
            chans = {"Sym^n W": {pm: Fraction(1, fact) for pm in perms}}
            if n >= 2:
                chans["Lambda^n W"] = {pm: Fraction(sign(pm), fact) for pm in perms}
            if n == 3:
                mixed = {}
                for pm in perms:
                    mixed[pm] = (Fraction(1 if pm == (0, 1, 2) else 0)
                                 - chans["Sym^n W"][pm] - chans["Lambda^n W"][pm])
                chans["(2,1)-isotypic"] = mixed
            per_dir = []
            for a in dirs:
                b_unit = {}
                for kind in ("chromo", "charge", "zeeman"):
                    # single strand normaliser: (1/dimW) * sum_w b(w)^2
                    tot = Fraction(0)
                    for (c, s) in W:
                        bw = (a[c] * sz[s] if kind == "chromo" else a[c] if kind == "charge"
                              else sz[s])
                        tot += Fraction(bw * bw)
                    b_unit[kind] = tot / len(W)
                row = {}
                for cname, X in chans.items():
                    trX = Fraction(0)
                    sums = {k: Fraction(0) for k in b_unit}
                    for x in itertools.product(W, repeat=n):
                        diag = Fraction(0)
                        for pm, c in X.items():
                            if all(x[pm[i]] == x[i] for i in range(n)):
                                diag += c
                        if diag == 0:
                            continue
                        trX += diag
                        Bc = sum(a[w[0]] * sz[w[1]] for w in x)
                        B0 = sum(a[w[0]] for w in x)
                        Bs = sum(sz[w[1]] for w in x)
                        sums["chromo"] += diag * Bc * Bc
                        sums["charge"] += diag * B0 * B0
                        sums["zeeman"] += diag * Bs * Bs
                    chi = {k: (sums[k] / trX) / b_unit[k] for k in sums}
                    kap = chi["chromo"] / chi["charge"] - chi["zeeman"]
                    row[cname] = {"dim": str(trX), "chi_chromo": str(chi["chromo"]),
                                  "chi_charge": str(chi["charge"]),
                                  "chi_zeeman": str(chi["zeeman"]), "kappa": str(kap)}
                per_dir.append(row)
            if len(per_dir) > 1:
                dir_ok &= all(pd == per_dir[0] for pd in per_dir)
            results[f"N={N}, n={n}"] = per_dir[0]
            for cname, v in per_dir[0].items():
                kappa_all.setdefault((n, cname), {})[N] = v["kappa"]
    OUT["P3"]["susceptibility_q1"] = results
    OUT["P3"]["kappa_by_channel"] = {f"n={k[0]} {k[1]}": v for k, v in kappa_all.items()}
    check("P3(ii) susceptibilities independent of the Cartan direction (N=3,4)", dir_ok)
    check("P3(ii) n=1: kappa = 0 for every N (factorisation)",
          all(v == "0" for v in kappa_all[(1, "Sym^n W")].values()))
    hits = []
    for key, byN in kappa_all.items():
        vals = set(byN.values())
        nindep = len(vals) == 1
        val = next(iter(vals))
        inset = val in {"-1/3", "1/3", "-1/12", "1/12", "-2/3", "2/3"}
        if nindep and inset:
            hits.append((key, val))
    OUT["P3"]["acceptance_clause2_candidates"] = [f"{k}: {v}" for k, v in hits]
    check("P3 acceptance clause (2): no channel has an N-independent kappa in the pre-listed set "
          "(prediction MISS)", not hits, hits)
    strong = [h for h in hits if h[1] == "-1/3"]
    check("P3 STRONG: no N-independent kappa = -1/3", not strong, strong)
    # post-hoc observations (not pre-registered)
    eq = all(v["chi_chromo"] == v["chi_charge"] == v["chi_zeeman"]
             for res in results.values() for v in res.values())
    check("P3(ii) chi_chromo = chi_charge = chi_zeeman in every S_n channel at q=1, so "
          "kappa = 1 - chi_zeeman", eq, posthoc=True)
    Nn = sp.Symbol("N")
    form = {("Sym^n W"): -(2 * Nn + 3) / (2 * Nn + 1), ("Lambda^n W"): -(2 * Nn - 3) / (2 * Nn - 1)}
    okf = all(sp.Rational(kappa_all[(2, c)][Nv]) == f.subs(Nn, Nv)
              for c, f in form.items() for Nv in (2, 3, 4))
    check("P3(ii) n=2 closed forms kappa(Sym^2W) = -(2N+3)/(2N+1), kappa(Lambda^2W) = "
          "-(2N-3)/(2N-1); the -1/3 of Lambda^2W at N=2 is N-dependent", okf, posthoc=True)


def main():
    run_P1()
    run_P1_crosscheck()
    run_P2()
    run_P3_covariance()
    run_P3_susceptibility()
    npass = sum(c["pass"] for c in OUT["checks"])
    OUT["summary"] = f"{npass}/{len(OUT['checks'])} checks pass"
    print(OUT["summary"])
    (HERE / "qcd_spin_factor_probe.out.json").write_text(
        json.dumps(OUT, indent=1, ensure_ascii=False, default=str) + "\n")


if __name__ == "__main__":
    main()
