#!/usr/bin/env python3
"""Where does `T_w^{-1}` live in the `T`-basis?  (bean qou-phir)

Mathas' Lemma 3.9 says an `m_{st}` on a composition shape is an *R-combination*
of terms on the sorted shape.  `CompositionIdeal.exists_xComp_swap` proves the
ideal-level identity `a x_mu b = (a T_d^{-1}) x_nu (T_d b)`; turning that into
3.9 as stated means expanding `T_d^{-1}` in the `T`-basis and controlling its
support.  This probe measures that support before any of it is formalised.

  (A) length bound   -- is  supp(T_w^{-1})  inside  {v : l(v) <= l(w)} ?
  (B) Bruhat bound   -- is  supp(T_w^{-1})  inside  [e, w]  (subword criterion) ?
  (C) leading term   -- is the coefficient at `w` itself  q^{-l(w)} ?
  (D) how wide can the expansion get, against the naive 2^l(w) bound?

Conventions taken from the corpus, not from a textbook:

  * quadratic relation  sigma^2 = (q-1) sigma + q, read off
    `IwahoriHecke.sigmaInv = (1/q)(sigma - (q-1))`;
  * `TwBasis.Tw_mul_Tw : T_v * T_w = T_{w*v}` when lengths add -- the FLIPPED
    handedness forced by `orbitMap`.  So left multiplication by a generator
    acts on the RIGHT of the index:
        sigma_i * T_w = T_{w s_i}                 if l(w s_i) > l(w)
        sigma_i * T_w = q T_{w s_i} + (q-1) T_w   otherwise

THE PROBE CHECKS ITSELF FIRST.  An earlier version of this file reported that
(B) fails for exactly half the elements of S_4.  That was a bug in its own
Bruhat test (a reduced word whose orientation was never verified, and a
subword test that enumerated the wrong set), not a fact about Hecke algebras.
So before any verdict is printed, the probe asserts that

  * each reduced word multiplies back to its own permutation, and has
    length exactly l(w);
  * `T_w * T_w^{-1} = T_1` and `T_w^{-1} * T_w = T_1`, symbolically.

If the inverse were wrong those identities would fail, and no support claim
below would mean anything.

NO FLOAT64: every coefficient is a sympy rational function in `q`.
"""

from itertools import permutations
import sympy as sp

q = sp.Symbol("q")


def length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def right_mul_s(w, i):
    """w * s_i  -- s_i swaps positions i, i+1, i.e. (w s_i)(i) = w(i+1)."""
    v = list(w)
    v[i], v[i + 1] = v[i + 1], v[i]
    return tuple(v)


def word_prod(word, n):
    """s_{i_1} s_{i_2} ... s_{i_k}, built by right multiplication from the identity."""
    w = tuple(range(n))
    for i in word:
        w = right_mul_s(w, i)
    return w


def reduced_word(w):
    """A reduced word for `w`.  Bubble-sorting `w` to the identity by right
    multiplications gives  w s_{j_1} ... s_{j_m} = e,  hence
    w = s_{j_m} ... s_{j_1}: the sorting word REVERSED."""
    v = list(w)
    n = len(v)
    sorting = []
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                sorting.append(i)
                changed = True
    return list(reversed(sorting))


def sigma_mul(elt, i):
    out = {}
    for w, c in elt.items():
        ws = right_mul_s(w, i)
        if length(ws) > length(w):
            out[ws] = out.get(ws, 0) + c
        else:
            out[ws] = out.get(ws, 0) + q * c
            out[w] = out.get(w, 0) + (q - 1) * c
    return {w: sp.cancel(c) for w, c in out.items() if sp.cancel(c) != 0}


def sigma_inv_mul(elt, i):
    """sigma_i^{-1} . x  =  (1/q)(sigma_i . x - (q-1) x)."""
    out = dict(sigma_mul(elt, i))
    for w, c in elt.items():
        out[w] = out.get(w, 0) - (q - 1) * c
    return {w: sp.cancel(c / q) for w, c in out.items() if sp.cancel(c) != 0}


def mul(x, y):
    """x * y, expanding x over the basis and acting by generators."""
    total = {}
    for v, cv in x.items():
        # T_v * y : build T_v as sigma_{i_k} ... sigma_{i_1} acting on y
        acc = dict(y)
        for i in reduced_word(v):
            acc = sigma_mul(acc, i)
        for w, cw in acc.items():
            total[w] = total.get(w, 0) + cv * cw
    return {w: sp.cancel(c) for w, c in total.items() if sp.cancel(c) != 0}


def tw(w, n):
    elt = {tuple(range(n)): sp.Integer(1)}
    for i in reduced_word(w):
        elt = sigma_mul(elt, i)
    return elt


def tw_inverse(w, n):
    """T_w = sigma_{i_k}...sigma_{i_1}  =>  T_w^{-1} = sigma_{i_1}^{-1}...sigma_{i_k}^{-1}."""
    elt = {tuple(range(n)): sp.Integer(1)}
    for i in reversed(reduced_word(w)):
        elt = sigma_inv_mul(elt, i)
    return elt


def bruhat_le(u, w):
    """Subword criterion: u <= w iff some SUBWORD of a reduced word for w
    multiplies to u.  Enumerated by dynamic programming over prefixes."""
    n = len(w)
    reachable = {tuple(range(n))}
    for i in reduced_word(w):
        reachable = reachable | {right_mul_s(p, i) for p in reachable}
    return u in reachable


def main():
    print("T_w^{-1} support probe  (exact sympy over Q(q); no float anywhere)\n")

    # ---- self-checks, before any verdict -------------------------------
    print("self-check:")
    bad_word = bad_inv = checked = 0
    for n in range(2, 5):
        e = tuple(range(n))
        for w in permutations(range(n)):
            checked += 1
            rw = reduced_word(w)
            if word_prod(rw, n) != w or len(rw) != length(w):
                bad_word += 1
            inv = tw_inverse(w, n)
            if mul(tw(w, n), inv) != {e: sp.Integer(1)}:
                bad_inv += 1
            if mul(inv, tw(w, n)) != {e: sp.Integer(1)}:
                bad_inv += 1
    print(f"  reduced words correct + reduced        {checked - bad_word} / {checked}")
    print(f"  T_w * T_w^-1 = T_w^-1 * T_w = T_1      {checked - bad_inv} / {checked}")
    if bad_word or bad_inv:
        print("\n  SELF-CHECK FAILED -- no support verdict is printed.")
        return
    print("  passed; verdicts below are about the algebra, not the harness\n")

    # ---- the measurement ----------------------------------------------
    A = B = C = N = 0
    Bi = Ci = invol = 0
    widest = (0, None)
    saturating = []
    for n in range(2, 5):
        for w in permutations(range(n)):
            inv = tw_inverse(w, n)
            lw = length(w)
            N += 1
            winv = tuple(sorted(range(n), key=lambda i: w[i]))
            A += all(length(v) <= lw for v in inv)
            B += all(bruhat_le(v, w) for v in inv)
            C += sp.cancel(inv.get(w, sp.Integer(0)) - q ** (-lw)) == 0
            Bi += all(bruhat_le(v, winv) for v in inv)
            Ci += sp.cancel(inv.get(winv, sp.Integer(0)) - q ** (-lw)) == 0
            if w == winv:
                invol += 1
            if len(inv) > widest[0]:
                widest = (len(inv), (n, w, lw))
            if lw >= 2 and len(inv) == 2 ** lw:
                saturating.append((n, w, lw))

    print(f"  (A) support has length <= l(w)      {A} / {N}")
    print(f"  (B) support inside Bruhat [e, w]    {B} / {N}")
    print(f"  (C) coefficient at w is q^-l(w)     {C} / {N}")
    print(f"  (B') support inside Bruhat [e, w^-1]  {Bi} / {N}")
    print(f"  (C') coefficient at w^-1 is q^-l(w)   {Ci} / {N}")
    print(f"\n  involutions (w = w^-1) in range:      {invol} / {N}")
    print(f"\n  (D) widest expansion: {widest[0]} terms at n={widest[1][0]} "
          f"w={widest[1][1]} l={widest[1][2]}  (2^l = {2 ** widest[1][2]})")
    print(f"      elements attaining the full 2^l(w): {len(saturating)} of {N}"
          f"; max l among them = "
          f"{max((s[2] for s in saturating), default=0)}")


if __name__ == "__main__":
    main()
