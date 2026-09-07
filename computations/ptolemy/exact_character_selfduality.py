"""Decide self-duality of a boundary-unipotent PGL(3,C) representation DIRECTLY, by
exact character arithmetic in the Ptolemy number field K = Q[T]/(f).

WHY THIS EXISTS.  PR #6815 concluded complex type for the L6a4 obstruction-class-1
representations via the OBSTRUCTION ARGUMENT -- duality negates the obstruction class,
isomorphism preserves it, so 2*sigma = 0 forces sigma = 0 in Z/3.  Its two topological
inputs are carried as GGZ HYPOTHESES, not proofs.  A character computation needs
neither.  Agreement corroborates those hypotheses on this manifold; disagreement means
one of the two routes is wrong, which is worth more than either.

PGL, NOT SL -- and getting this wrong would invalidate the whole test.  A non-trivial
obstruction class is exactly the statement that the representation does NOT lift to
SL(3,C), so the matrix returned for a generator is defined only up to a scalar and
chi(g) is not by itself an invariant.  Under a rescaling M -> mu*M:

    chi(g) -> mu*chi(g)        det(g) -> mu^3*det(g)        so chi^3/det is INVARIANT.

Self-duality means A*M(g)*A^-1 = lambda(g)*M(g)^{-T} for scalars lambda(g); taking
determinants gives lambda(g)^3 = det(g)^2, and taking traces gives
chi(g) = lambda(g)*chi(g^-1).  Cubing and dividing:

    chi(g)^3 / det(g)  ==  chi(g^-1)^3 / det(g^-1)          for every g, if self-dual.

So a single word with chi(w)^3/det(w) != chi(w^-1)^3/det(w^-1) is a SOUND certificate
of complex type.  The bare comparison chi(w) == chi(w^-1) is reported too because it is
what one wants to look at, but it is NOT PGL-invariant and is never the verdict.  The
determinants are printed rather than assumed to be 1.

THE GENERATORS ARE THE WRONG SAMPLE, and on this manifold they are wrong in the
direction that looks like a result.  Every generator of L6a4 class 1 PASSES the
invariant test: chi(b) = chi(b^-1) = 3 and chi(c) = chi(c^-1) = 3 because b and c are
boundary-unipotent, while chi(a)/chi(a^-1) is EXACTLY a primitive cube root of unity --
K contains zeta_3, since f factors over Q(sqrt(-3)) -- so chi(a)^3 = chi(a^-1)^3.  That
is precisely the value a projective self-duality would produce, so a generators-only
test reports "no witness", which reads as evidence FOR self-duality.  Nor does twisting
help: eps(a) = zeta_3, eps(b) = eps(c) = 1 is a genuine homomorphism to mu_3 (a has
exponent sum 0 in both relators), and the twisted lift has inverse-invariant character
on all three generators.  The obstruction appears at WORD LENGTH 2 -- `ac` -- and 3504
words of length <= 5 witness it.  Hence the verdict is taken from a word SWEEP, never
from the generators.

The test is FIELD-THEORETIC, not numerical.  Everything is an element of K, compared by
equality.  No complex embedding is chosen, so "how close to real" never arises and no
tolerance is involved anywhere.

NO FLOAT64: Fraction and K only (see numberfield.py for why not sympy expressions --
the sympy version ran 17 minutes on one matrix product without emitting a line).
"""
import itertools
import json
import pathlib
import sys
from fractions import Fraction

import snappy
import sympy as sp
from snappy.ptolemy.coordinates import PtolemyCoordinates

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from numberfield import NumberField          # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent


class Elt:
    """K element with operator overloads, so snappy's matrix code works unchanged."""
    __slots__ = ('v', 'K')

    def __init__(self, K, v):
        self.K, self.v = K, v

    def _c(self, o):
        return o if isinstance(o, Elt) else Elt(self.K, self.K.const(o))

    def __add__(self, o):
        return Elt(self.K, self.K.add(self.v, self._c(o).v))
    __radd__ = __add__

    def __sub__(self, o):
        return Elt(self.K, self.K.sub(self.v, self._c(o).v))

    def __rsub__(self, o):
        return Elt(self.K, self.K.sub(self._c(o).v, self.v))

    def __mul__(self, o):
        return Elt(self.K, self.K.mul(self.v, self._c(o).v))
    __rmul__ = __mul__

    def __truediv__(self, o):
        return Elt(self.K, self.K.div(self.v, self._c(o).v))

    def __rtruediv__(self, o):
        return Elt(self.K, self.K.div(self._c(o).v, self.v))

    def __neg__(self):
        return Elt(self.K, self.K.neg(self.v))

    def __pow__(self, n):
        # snappy's variable_dict raises coordinates to integer powers.
        if not isinstance(n, int):
            return NotImplemented
        if n < 0:
            return Elt(self.K, self.K.inv(self.v)) ** (-n)
        r, b = Elt(self.K, self.K.one()), self
        while n:
            if n & 1:
                r = r * b
            b, n = b * b, n >> 1
        return r

    def __eq__(self, o):
        return self.K.eq(self.v, self._c(o).v)

    def __hash__(self):
        return hash(self.v)

    def __repr__(self):
        terms = [f"{c}" if k == 0 else (f"{c}*T" if k == 1 else f"{c}*T^{k}")
                 for k, c in enumerate(self.v) if c != 0]
        return " + ".join(terms) if terms else "0"


def _frac(c):
    """sympy Rational -> Fraction.

    NOT via nsimplify: it is a *search* for a closed form and will happily turn an
    exact rational into radicals.  Asked for 4423.../600362847 it returned
    -25000*2**(68/113)*3**(47/113)*5**(71/113)*7**(64/113)/600362847, which is not the
    same number and is not even rational.  Take the numerator and denominator.
    """
    r = sp.Rational(c)
    return Fraction(int(sp.numer(r)), int(sp.denom(r)))


def poly_to_elt(K, expr, gen):
    p = sp.Poly(sp.expand(expr), gen)
    return Elt(K, K.from_poly_coeffs([_frac(c) for c in reversed(p.all_coeffs())]))


def trace(K, M):
    acc = Elt(K, K.zero())
    for i in range(3):
        acc = acc + M[i][i]
    return acc


def det3(K, M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
    kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    MAXLEN = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    d = json.loads((HERE / f'{name}-c{kcls}-ptolemy-in-K.json').read_text())
    gen = sp.Symbol('t')
    fe = sp.sympify(d['field']['min_poly'])
    fp = sp.Poly(sp.expand(fe), gen)
    K = NumberField([_frac(c) for c in reversed(fp.all_coeffs())])
    print(f"{name} c{kcls}: K = Q[T]/({fe}), degree {K.deg}")

    pt = {k: poly_to_elt(K, sp.sympify(v), gen) for k, v in d['ptolemy'].items()}
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    dd = dict(pt)
    dd['1'] = Elt(K, K.one())
    C = PtolemyCoordinates(
        dd, is_numerical=False,
        py_eval_section=eval(V.py_eval_section()),
        manifold_thunk=lambda: M,
        non_trivial_generalized_obstruction_class=(kcls != 0))
    # evaluate_word reads words in the UNSIMPLIFIED presentation unless a group is
    # passed.  M.fundamental_group() returns the SIMPLIFIED one by default, so calling
    # evaluate_word(g) on its generators silently evaluates the wrong words -- it
    # returns matrices, they are in SL(3), their traces look like characters, and the
    # only thing that gives it away is that the relators do not map to scalars.
    G = M.fundamental_group()
    gens = G.generators()
    print(f"  generators (simplified presentation): {gens}", flush=True)

    # GATE.  rho is a PGL(3,C) representation only if every relator maps to a SCALAR
    # matrix.  Check before reading a single character off these matrices.
    for r in G.relators():
        R = C.evaluate_word(r, G)
        off = [(i, j) for i in range(3) for j in range(3)
               if i != j and not (R[i][j] == 0)]
        diag_equal = (R[0][0] == R[1][1]) and (R[1][1] == R[2][2])
        if off or not diag_equal:
            print(f"  RELATOR GATE FAILED on {r}: "
                  f"{'non-zero off-diagonal ' + str(off) if off else ''}"
                  f"{'' if diag_equal else ' unequal diagonal'}")
            print("  These matrices are NOT a representation.  Nothing downstream of"
                  " them means anything.")
            return 1
        print(f"  relator {r} -> scalar {R[0][0]}", flush=True)

    rows, witnesses = [], []
    for g in gens:
        Mg, Mi = C.evaluate_word(g, G), C.evaluate_word(g.upper(), G)
        tr, tri = trace(K, Mg), trace(K, Mi)
        dg, di = det3(K, Mg), det3(K, Mi)
        inv_g = (tr * tr * tr) / dg
        inv_i = (tri * tri * tri) / di
        same = (inv_g == inv_i)
        if not same:
            witnesses.append(g)
        rows.append({"generator": g, "chi": repr(tr), "chi_inv": repr(tri),
                     "det": repr(dg), "det_inv": repr(di),
                     "chi_eq_chi_inv": bool(tr == tri),
                     "pgl_invariant_equal": bool(same)})
        print(f"\n  g = {g}")
        print(f"    chi(g)        = {tr}")
        print(f"    chi(g^-1)     = {tri}")
        print(f"    det(g)        = {dg}")
        print(f"    det(g^-1)     = {di}")
        print(f"    chi == chi_inv                  : {tr == tri}   (NOT PGL-invariant)")
        print(f"    chi^3/det == chi_inv^3/det_inv  : {same}   <- the verdict test",
              flush=True)

    print(f"\n  generators alone: {len(witnesses)} witness(es)"
          + ("" if witnesses else "  -- inconclusive, see the docstring; sweeping words"))

    # THE SWEEP.  Reduced words up to MAXLEN in the generators and their inverses.
    letters = [g for g in gens] + [g.upper() for g in gens]
    one = Elt(K, K.one())
    seen, hits, ratio_classes = set(), [], {}
    for L in range(1, MAXLEN + 1):
        for tup in itertools.product(letters, repeat=L):
            w = ''.join(tup)
            if any(w[i].swapcase() == w[i + 1] for i in range(len(w) - 1)):
                continue        # not reduced
            if w in seen:
                continue
            seen.add(w)
            wi = ''.join(ch.swapcase() for ch in reversed(w))
            Mw, Mi = C.evaluate_word(w, G), C.evaluate_word(wi, G)
            tr, tri = trace(K, Mw), trace(K, Mi)
            dw, di = det3(K, Mw), det3(K, Mi)
            if ((tr * tr * tr) / dw) == ((tri * tri * tri) / di):
                if tri != 0 and not (tr == tri):
                    r = tr / tri
                    key = ("1" if r == one else
                           "primitive cube root of unity" if (r * r + r + one) == 0
                           else "OTHER -- unexpected, investigate")
                    ratio_classes[key] = ratio_classes.get(key, 0) + 1
                continue
            hits.append({"word": w, "chi": repr(tr), "chi_inv": repr(tri)})
        print(f"    length <= {L}: {len(seen)} reduced words, {len(hits)} PGL witnesses"
              f"; chi != chi_inv ratio classes {ratio_classes}", flush=True)

    verdict = ("COMPLEX TYPE (not self-dual)" if hits
               else f"no complex-type witness among reduced words of length <= {MAXLEN}")
    print(f"\n  VERDICT: {verdict}")
    if hits:
        print(f"    shortest witness: {hits[0]['word']}  ({len(hits)} in total)")
        print("    This uses NEITHER GGZ hypothesis -- it is independent corroboration"
              " of the\n    obstruction argument, not a restatement of it.")
    else:
        print("    NOT a proof of self-duality: a finite word sample cannot establish"
              " one.\n    Self-duality needs a conjugating matrix.")

    out = HERE / f'{name}-c{kcls}-character-selfduality.json'
    out.write_text(json.dumps({
        "manifold": name, "obstruction_class": kcls, "field": d["field"],
        "generators": gens, "rows": rows,
        "generator_witnesses": witnesses,
        "sweep": {"max_length": MAXLEN, "reduced_words": len(seen),
                  "pgl_witnesses": len(hits),
                  "shortest_witness": hits[0] if hits else None,
                  "ratio_classes_where_invariant_holds": ratio_classes},
        "verdict": verdict,
        "invariant": "chi(w)^3/det(w) vs chi(w^-1)^3/det(w^-1); PGL-scale-invariant",
    }, indent=2) + "\n")
    print(f"  wrote {out.name}")
    return 0 if hits else 2


if __name__ == '__main__':
    sys.exit(main())
