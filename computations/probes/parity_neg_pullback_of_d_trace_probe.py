"""qou-hlxp: what the letter maps do to the convention-D Markov trace.

Exact symbolic computation over Q(q) (sympy); no floats anywhere.

The three letter maps of `QOU/QuarkState/HelicityCommonSource.lean` are not
K-linear self-maps of H_n(q) (except flip), but each one IS a K-linear algebra
isomorphism H_n(q) -> H_n(q^-1), where H_n(q^-1) is presented on generators t_i
with t_i^2 = -h t_i + 1 (h = q - q^-1):

    neg  : s_i |-> -t_i
    flip : s_i |-> t_i^-1 = t_i + h
    swap : s_i |-> -s_i^-1 = h - s_i   (an automorphism of H_n(q) itself)

Each check verifies the image letter satisfies x^2 = h x + 1 in H_n(q^-1).

Question: pull the convention-D Ocneanu trace of H_n(q^-1) (parameter
z_D(q^-1)) back along each map. Is the result the convention-D trace of
H_n(q) (parameter z_D(q) = q^3/(q^2+1))? If not, which Markov trace is it?

Method: H_n as the Iwahori-Hecke algebra on S_n in the T_w basis; the Ocneanu
trace is built from its defining recursion; the pulled-back functional is
evaluated on every T_w and compared against Ocneanu traces of H_n(q).
"""
from __future__ import annotations

import itertools
import json
import pathlib
import sys

import sympy as sp

q = sp.symbols("q", positive=True)


def perm_mul(a, b):
    # (a*b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(len(a)))


def simple(n, i):
    p = list(range(n))
    p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def length(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])


class Hecke:
    """H_n with generators s_i, s_i^2 = hh s_i + 1, basis T_w."""

    def __init__(self, n, hh):
        self.n, self.hh = n, hh
        self.elems = list(itertools.permutations(range(n)))

    def mul_gen_left(self, i, vec):
        s = simple(self.n, i)
        out = {}
        for w, c in vec.items():
            sw = perm_mul(s, w)
            if length(sw) > length(w):
                out[sw] = out.get(sw, 0) + c
            else:
                out[sw] = out.get(sw, 0) + c
                out[w] = out.get(w, 0) + self.hh * c
        return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}

    def mul(self, a, b):
        # a * b with a given as a vector; expand a's T_w as products of generators
        out = {}
        for w, c in a.items():
            word = reduced_word(w)
            v = dict(b)
            for i in reversed(word):
                v = self.mul_gen_left(i, v)
            for k, val in v.items():
                out[k] = out.get(k, 0) + c * val
        return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}

    def gen(self, i):
        return {simple(self.n, i): sp.Integer(1)}

    def one(self):
        return {tuple(range(self.n)): sp.Integer(1)}


def reduced_word(w):
    w = list(w)
    word = []
    # bubble sort: w = s_{i1} ... s_{ik}
    n = len(w)
    p = list(w)
    res = []
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                res.append(i)
                changed = True
    # p = w * s_{res[0]} * ... ; so w = s_{res[-1]} ... s_{res[0]} composed appropriately
    word = list(reversed(res))
    # verify
    t = tuple(range(n))
    for i in word:
        t = perm_mul(t, simple(n, i))
    assert t == tuple(w), (w, word, t)
    return word


def ocneanu(H, z):
    """Ocneanu trace on H_n with tr(1)=1, tr(x s_{k} y) = z tr(xy), x,y in H_k."""
    cache = {}

    def tr_vec(vec):
        return sp.simplify(sum(c * tr_basis(w) for w, c in vec.items()))

    def tr_basis(w):
        if w in cache:
            return cache[w]
        n = len(w)
        m = max([i for i in range(n) if w[i] != i], default=-1)
        if m == -1:
            val = sp.Integer(1)
        else:
            # top moved point m: write T_w = T_x s_{m-1} ... ; use reduced word and
            # Markov recursion on the largest generator index appearing once.
            word = reduced_word(w)
            top = max(word)
            if word.count(top) == 1:
                k = word.index(top)
                # T_w = T_x s_top T_y with x, y words in the lower generators;
                # tr = z * tr(T_x T_y), the product taken IN THE ALGEBRA (the
                # concatenated word need not be reduced).
                v = H.one()
                for i in word[:k] + word[k + 1:]:
                    v = H.mul(v, H.gen(i))
                val = z * tr_vec(v)
            else:
                raise RuntimeError("non-unique top in reduced word: %s" % (word,))
        cache[w] = sp.simplify(val)
        return cache[w]

    return tr_vec, tr_basis


def reduced_word_top_once(w):
    return reduced_word(w)


def pullback(Hq, Hqi, image_letter, tr_qi):
    """phi: H(q) -> H(q^-1), s_i |-> image_letter(i); returns w |-> tr_qi(phi(T_w))."""
    vals = {}
    for w in Hq.elems:
        v = Hqi.one()
        for i in reduced_word(w):
            v = Hqi.mul(v, image_letter(i))
        vals[w] = tr_qi(v)
    return vals


def main():
    h = q - 1 / q
    zD = q**3 / (q**2 + 1)
    zD_inv = zD.subs(q, 1 / q)
    results = {}
    ok = True
    for n in (2, 3, 4):
        Hq = Hecke(n, h)
        Hqi = Hecke(n, -h)
        trq_vec, trq = ocneanu(Hq, zD)
        trqi_vec, _ = ocneanu(Hqi, zD_inv)
        maps = {
            "neg": lambda i: {k: -c for k, c in Hqi.gen(i).items()},
            "flip": lambda i: {**Hqi.gen(i), tuple(range(n)): h},
        }
        targets = {"neg": (Hqi, trqi_vec), "flip": (Hqi, trqi_vec),
                   "swap": (Hq, trq_vec)}
        maps["swap"] = lambda i: {**{k: -c for k, c in Hq.gen(i).items()}, tuple(range(n)): h}
        row = {}
        for name, img in maps.items():
            Ht, trt = targets[name]
            # check image letter satisfies x^2 = h x + 1 in the target algebra
            x = img(0)
            lhs = Ht.mul(x, x)
            rhs = {k: h * c for k, c in x.items()}
            rhs[tuple(range(n))] = rhs.get(tuple(range(n)), 0) + 1
            diff = {k: sp.simplify(lhs.get(k, 0) - rhs.get(k, 0)) for k in set(lhs) | set(rhs)}
            assert all(v == 0 for v in diff.values()), (name, diff)
            pb = pullback(Hq, Ht, img, trt)
            z_pb = sp.simplify(pb[simple(n, 0)])
            # is pb the Ocneanu trace of H(q) with parameter z_pb?
            _, tr_zpb = ocneanu(Hq, z_pb)
            is_ocneanu = all(sp.simplify(pb[w] - tr_zpb(w)) == 0 for w in Hq.elems)
            equals_D = all(sp.simplify(pb[w] - trq(w)) == 0 for w in Hq.elems)
            row[name] = {
                "z_pullback": str(sp.factor(z_pb)),
                "pullback_is_markov_trace": is_ocneanu,
                "pullback_equals_convention_D": equals_D,
            }
            ok = ok and is_ocneanu
        results[n] = row
        print(n, json.dumps(row, ensure_ascii=False))
    # expected closed forms
    zT = sp.simplify(-q**-3 / (q**-2 + 1))  # z_D at q -> -q^-1 (transpose convention)
    checks = {
        "flip_pullback_is_D": all(results[n]["flip"]["pullback_equals_convention_D"] for n in results),
        "neg_pullback_not_D": not any(results[n]["neg"]["pullback_equals_convention_D"] for n in results),
        "swap_pullback_not_D": not any(results[n]["swap"]["pullback_equals_convention_D"] for n in results),
        "neg_z_is_zD_at_minus_q_inv": sp.simplify(sp.sympify(results[3]["neg"]["z_pullback"].replace("^", "**"), locals={"q": q}) - zD.subs(q, -1 / q)) == 0,
        "all_pullbacks_markov": ok,
    }
    # Support: the D trace kills the q-antisymmetriser of H_3; the pulled-back
    # trace z_T = z_D(-1/q) kills the q-symmetriser instead (the transpose).
    H3 = Hecke(3, h)
    zT = zD.subs(q, -1 / q)
    trD3, _ = ocneanu(H3, zD)
    trT3, _ = ocneanu(H3, zT)
    sym = {w: q ** length(w) for w in H3.elems}
    alt = {w: (-1 / q) ** length(w) for w in H3.elems}
    checks["D_kills_antisymmetriser_n3"] = sp.simplify(trD3(alt)) == 0
    checks["D_keeps_symmetriser_n3"] = sp.simplify(trD3(sym)) != 0
    checks["pullback_kills_symmetriser_n3"] = sp.simplify(trT3(sym)) == 0
    checks["pullback_keeps_antisymmetriser_n3"] = sp.simplify(trT3(alt)) != 0
    print(json.dumps(checks))
    out = pathlib.Path(__file__).with_suffix("").name.replace("_probe", "").replace("_", "-") + ".witness.json"
    pathlib.Path(__file__).with_name(out).write_text(
        json.dumps({"description": __doc__.strip().splitlines()[0], "results": {str(k): v for k, v in results.items()},
                    "checks": checks, "exact": True,
                    "q0Anchor": "independent",
                    "q0AnchorReason": "exact symbolic computation over Q(q) in sympy; q stays a "
                                      "symbol and no q0 pin is ever read"}, indent=2, ensure_ascii=False) + "\n")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
