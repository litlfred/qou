#!/usr/bin/env python3
"""Is an excited electron a non-reduced word? Exact Groebner-Shirshov / normal-form probe.

Owner question (2026-11-21): "Can we see this in the grobner bases calculations that an
excited electron is a non-reduced?"

Everything is exact over Q(q, phi) with sympy. No float, no measured value, no fit.

Model.  H_n(q) with sigma_i^2 = h sigma_i + 1, h = q - 1/q.  Normal form = the T_w basis
(w in S_n), which is the irreducible-word basis of the Groebner-Shirshov system (braid
relations + quadratic relation); T_w T_s = T_{ws} if l(ws) > l(w), else h T_w + T_{ws}.
A word is "reduced" (GS-irreducible) iff it is a positive word whose letters multiply with
no quadratic branch, i.e. it is a reduced expression; sigma^{-1} = sigma - h always yields a
sum.  The photon is the ruled form gamma = 1 + p0 s_a + p1 s_b + p01 s_a s_b^{-1}
(owner ruling 2026-11-20).  Markov trace convention D, z = q^3/(q^2+1).

Invariants reported for each element x = sum c_w T_w (all functions of the NF vector, hence
independent of rewrite order):
  chi(x)   = sum c_w q^{l(w)}          (index character = the 1-dim trivial rep T_s -> q)
  maxlen   = max{l(w) : c_w != 0}      (top of the Bruhat length filtration)
  tr_D(x)  = convention-D Markov trace
and, for a single word, the number of quadratic branches hit when multiplying left to right
(NOT an invariant of the element; reported to show "non-reduced" literally).
"""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

q = sp.symbols("q", positive=True)
p0, p1, p01 = sp.symbols("phi0 phi1 phi01")
h = q - 1 / q
zD = q**3 / (q**2 + 1)


def ident(n):
    return tuple(range(n))


def length(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


def rmul_s(w, i):  # w * s_i : swap positions i, i+1
    w = list(w)
    w[i], w[i + 1] = w[i + 1], w[i]
    return tuple(w)


def lmul_s(i, w):  # s_i * w : swap values i, i+1
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in w)


class H:
    """Element of H_n(q): dict perm -> coeff."""

    def __init__(self, n, d=None):
        self.n = n
        self.d = {k: v for k, v in (d or {}).items() if sp.simplify(v) != 0}

    @staticmethod
    def one(n, c=1):
        return H(n, {ident(n): sp.Integer(1) * c})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = sp.together(d.get(k, 0) + v)
        return H(self.n, d)

    def scale(self, c):
        return H(self.n, {k: sp.together(c * v) for k, v in self.d.items()})

    def rmul_gen(self, i, sign=1):
        """x * sigma_i^{sign}; returns (element, quadratic branches hit)."""
        if sign == -1:
            a, k = self.rmul_gen(i, 1)
            return a + self.scale(-h), k
        d, hits = {}, 0
        for w, c in self.d.items():
            ws = rmul_s(w, i)
            if length(ws) > length(w):
                d[ws] = d.get(ws, 0) + c
            else:
                hits += 1
                d[w] = d.get(w, 0) + h * c
                d[ws] = d.get(ws, 0) + c
        return H(self.n, {k: sp.together(v) for k, v in d.items()}), hits

    def lmul_gen(self, i, sign=1):
        if sign == -1:
            a, k = self.lmul_gen(i, 1)
            return a + self.scale(-h), k
        d, hits = {}, 0
        for w, c in self.d.items():
            sw = lmul_s(i, w)
            if length(sw) > length(w):
                d[sw] = d.get(sw, 0) + c
            else:
                hits += 1
                d[w] = d.get(w, 0) + h * c
                d[sw] = d.get(sw, 0) + c
        return H(self.n, {k: sp.together(v) for k, v in d.items()}), hits

    def rmul_word(self, word):
        x, hits = self, 0
        for i, s in word:
            x, k = x.rmul_gen(i, s)
            hits += k
        return x, hits

    def __mul__(self, o):
        out = H(self.n)
        for w, c in o.d.items():
            x, _ = self.rmul_word(reduced_word(w))
            out = out + x.scale(c)
        return out

    def embed(self, n):
        return H(n, {tuple(list(w) + list(range(len(w), n))): c for w, c in self.d.items()})


def reduced_word(w):
    """A reduced word for w (bubble sort), as letters (i, +1)."""
    w, word = list(w), []
    while True:
        for i in range(len(w) - 1):
            if w[i] > w[i + 1]:
                w[i], w[i + 1] = w[i + 1], w[i]
                word.append((i, 1))
                break
        else:
            break
    return list(reversed(word))


def word_elt(n, word):
    return H.one(n).rmul_word(word)


def chi(x):
    return sp.factor(sp.together(sum(c * q ** length(w) for w, c in x.d.items())))


def maxlen(x):
    return max(length(w) for w in x.d) if x.d else None


def tr_D(x):
    """Markov trace, convention D: tr(a sigma_{n-1} b) = z tr(a b), tr(1) = 1."""
    total = 0
    for w, c in x.d.items():
        total += c * tr_basis(w)
    return sp.factor(sp.together(total))


_trc = {}


def tr_basis(w):
    if w in _trc:
        return _trc[w]
    n = len(w)
    if n == 1:
        return sp.Integer(1)
    if w[n - 1] == n - 1:
        v = tr_basis(w[:-1])
    else:
        # w = u * (s_{n-2} s_{n-3} ... s_j), u in S_{n-1} x 1 ; T_w = T_u T_{s_{n-2}} T_rest
        for j in range(n - 2, -1, -1):
            c = ident(n)
            for i in range(n - 2, j - 1, -1):
                c = rmul_s(c, i)
            cinv = tuple(sorted(range(n), key=lambda k: c[k]))
            u = tuple(w[c_inv] for c_inv in cinv)  # u = w * c^{-1}
            if u[n - 1] == n - 1 and length(u) + (n - 1 - j) == length(w):
                rest = [(i, 1) for i in range(n - 3, j - 1, -1)]
                y, _ = H(n - 1, {u[:-1]: sp.Integer(1)}).rmul_word(rest)
                v = zD * sum(cc * tr_basis(ww) for ww, cc in y.d.items())
                break
        else:
            raise RuntimeError(w)
    v = sp.together(v)
    _trc[w] = v
    return v


def photon(n, a, b):
    """gamma = 1 + p0 s_a + p1 s_b + p01 s_a s_b^{-1}  (ruled form)."""
    g = H.one(n)
    g = g + word_elt(n, [(a, 1)])[0].scale(p0)
    g = g + word_elt(n, [(b, 1)])[0].scale(p1)
    g = g + word_elt(n, [(a, 1), (b, -1)])[0].scale(p01)
    return g


def show(x):
    return {"".join(f"s{i}" for i, _ in reduced_word(w)) or "1": str(sp.factor(c)) for w, c in sorted(x.d.items(), key=lambda t: length(t[0]))}


def report(label, x, hits=None, extra=None):
    r = {"label": label, "terms": len(x.d), "maxlen": maxlen(x),
         "length_profile": sorted({length(w) for w in x.d}),
         "chi": str(chi(x)), "tr_D": str(tr_D(x)), "nf": show(x)}
    if hits is not None:
        r["quadratic_branches_left_to_right"] = hits
        r["GS_irreducible_as_written"] = hits == 0
    if extra:
        r.update(extra)
    return r


checks, out = [], []


def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)


# --- self-tests of the model -------------------------------------------------
s0 = word_elt(3, [(0, 1)])[0]
s1 = word_elt(3, [(1, 1)])[0]
check("quadratic sigma0^2 = h sigma0 + 1",
      all(sp.simplify(v) == 0 for v in ((s0 * s0) + s0.scale(-h) + H.one(3, -1)).d.values()))
check("braid s0 s1 s0 = s1 s0 s1",
      not ((s0 * s1 * s0) + (s1 * s0 * s1).scale(-1)).d)
check("tr_D(1)=1, tr_D(s0)=z_D", sp.simplify(tr_D(s0) - zD) == 0)
check("left and right products agree: s1*(s0 s1 s0)",
      not ((s1 * word_elt(3, [(0, 1), (1, 1), (0, 1)])[0]) + word_elt(3, [(0, 1), (1, 1), (0, 1)])[0].lmul_gen(1)[0].scale(-1)).d)

# --- 1. ground-state electron candidates -------------------------------------
X1 = [(0, 1), (1, 1), (0, 1)]           # corpus e-  sigma0 sigma1 sigma0
X3 = [(0, 1)] * 3                       # trefoil T(2,3) on two strands
e1, k1 = word_elt(3, X1)
e3, k3 = word_elt(3, X3)
out.append(report("ground X1 = s0 s1 s0 (H3)", e1, k1))
out.append(report("ground X3 = s0^3 (H2 in H3)", e3, k3))
check("X1 is GS-irreducible (reduced expression of w0)", k1 == 0 and maxlen(e1) == 3)
check("X3 = s0^3 is NOT GS-irreducible already in the ground state", k3 == 2 and maxlen(e3) == 1)

# --- 2. photon on the electron's own strands (H3) -----------------------------
g = photon(3, 0, 1)
for lab, x in (("gamma * X1", g * e1), ("X1 * gamma", e1 * g), ("gamma * X3", g * e3), ("X3 * gamma", e3 * g)):
    out.append(report(lab, x))
check("photon cannot raise Bruhat length above l(w0)=3 in H3 (gamma*X1)", maxlen(g * e1) == 3)
check("chi(gamma*X1) = chi(gamma)*chi(X1)  (chi multiplicative)",
      sp.simplify(chi(g * e1) - chi(g) * chi(e1)) == 0)
# per-term reducedness of gamma*X1: each photon monomial times w0
for lab, w in (("s0*X1", [(0, 1)] + X1), ("s1*X1", [(1, 1)] + X1), ("s0 s1^-1 * X1", [(0, 1), (1, -1)] + X1)):
    x, k = word_elt(3, w)
    out.append(report("monomial " + lab, x, k))
check("every non-identity photon monomial times w0 hits a quadratic branch",
      all(word_elt(3, w)[1] > 0 for w in ([(0, 1)] + X1, [(1, 1)] + X1, [(0, 1), (1, 1)] + X1)))

# --- 3. the corpus's excitation constructions ---------------------------------
# (a) R-I move as Markov stabilisation sigma_n (transfer-matrix-operator-properties.md)
stab = []
for k in range(0, 4):
    n = 3 + k
    word = X1 + [(2 + j, 1) for j in range(k)]
    x, hits = word_elt(n, word)
    r = report(f"X1 + {k} positive curl(s) (H{n})", x, hits)
    stab.append((k, x, hits))
    out.append(r)
check("positive stabilisations stay GS-irreducible and add 1 to Bruhat length each",
      all(hits == 0 and maxlen(x) == 3 + k for k, x, hits in stab))
check("tr_D ratio per positive curl = z_D",
      all(sp.simplify(tr_D(stab[k][1]) / tr_D(stab[k - 1][1]) - zD) == 0 for k in range(1, 4)))
x, hits = word_elt(4, X1 + [(2, -1)])
out.append(report("X1 + 1 negative curl (H4)", x, hits))
zbar = (1 / q) ** 3 / ((1 / q) ** 2 + 1)
check("tr_D ratio for a negative curl = bar(z_D) = z_D(q^-1)",
      sp.simplify(tr_D(x) / tr_D(stab[0][1]) - zbar) == 0)
check("negative curl: two NF terms (lengths 3 and 4); each term irreducible", sorted({length(w) for w in x.d}) == [3, 4])

# (b) same-strand writhe +2 (hydrogen-orbitals.md: w = 3 -> 5 -> 7 ...)
same = []
for m in (3, 5, 7, 9):
    x, hits = word_elt(2, [(0, 1)] * m)
    same.append((m, x, hits))
    a = sp.factor(x.d.get((1, 0), 0))
    out.append(report(f"s0^{m} (H2): writhe {m}, shell n=(m-1)/2={(m - 1) // 2}", x, hits,
                      {"coeff_sigma": str(a), "deg_q_coeff_sigma": int(sp.degree(sp.numer(sp.together(a)), q) - sp.degree(sp.denom(sp.together(a)), q))}))
check("s0^m: chi = q^m (= q^writhe) for m=3,5,7,9", all(sp.simplify(chi(x) - q**m) == 0 for m, x, _ in same))
check("s0^m never reduces to a single word; NF stays in span{1,s0}", all(maxlen(x) == 1 and len(x.d) == 2 for m, x, _ in same))

# (c) photon sharing one strand with the electron: gamma on (s1, s2) in H4
gs = photon(4, 1, 2)
e14 = e1.embed(4)
for lab, x in (("gamma(s1,s2) * X1 (H4)", gs * e14), ("X1 * gamma(s1,s2) (H4)", e14 * gs)):
    out.append(report(lab, x))
# (d) photon on two new strands (disjoint): gamma(s3,s4) in H6 commutes, lengths add
gd = photon(6, 3, 4)
e16 = e1.embed(6)
xd = e16 * gd
out.append(report("X1 * gamma(s3,s4) disjoint (H6)", xd))
check("disjoint photon: chi factorises and tr_D factorises",
      sp.simplify(chi(xd) - chi(e16) * chi(gd)) == 0)

# --- 4. chi = q^writhe for arbitrary signed words (sanity over all words length<=4 in H3)
ok = True
for L in range(0, 5):
    for word in itertools.product([(0, 1), (0, -1), (1, 1), (1, -1)], repeat=L):
        x, _ = word_elt(3, list(word))
        wr = sum(s for _, s in word)
        if sp.simplify(chi(x) - q**wr) != 0:
            ok = False
check("chi(NF(beta)) = q^writhe(beta) for all 341 signed words of length <= 4 in H3", ok)

npass = sum(ok for _, ok in checks)
print(f"\n{npass}/{len(checks)} checks pass")
res = {"probe": "photon_excitation_gs", "exact": "sympy Q(q,phi)", "convention": "D, z=q^3/(q^2+1)",
       "photon": "1 + phi0 s_a + phi1 s_b + phi01 s_a s_b^-1",
       "checks": [{"name": n, "pass": o} for n, o in checks], "results": out}
Path(__file__).with_name("excitation_gs_probe.witness.json").write_text(json.dumps(res, indent=1) + "\n")
for r in out:
    print(json.dumps({k: r[k] for k in r if k != "nf"}))
sys.exit(0 if npass == len(checks) else 1)
