#!/usr/bin/env python3
"""Exact symbolic-in-q Hecke characters — the implementation behind
`hecke_characters.chi_lambda_braid(..., precision="symbolic_q")`.

WHAT THIS IS. `hecke_characters` builds seminormal representation matrices and
traces a braid word through them. Its float64 builder and its mpmath twin
(`build_seminormal_matrices_mp`) both need a NUMERICAL q. This module is the
third builder: sympy over Q(q), with q a free symbol, so the character comes
back as a rational function rather than a number.

That closes the "F3" branch, which the entry point had carried as a raised
NotImplementedError:

    "symbolic-in-q character evaluation is deferred to F3 (Murnaghan-Nakayama /
     Ram-Wenzl recursion in Rust). For now use precision='mpfr_50dps'."

The deferral named Murnaghan-Nakayama, and an MN engine does now exist
(`computations/qbeta/qbeta_hecke_mn_character_engine_probe.py`) -- but MN gives
characters on the STANDARD elements T_{gamma_mu} only, and a Hecke character is
NOT a class function on braid words. The corpus's own numbers make that
concrete: chi^(2,1)(s1 s2 s1) = 0 while chi^(2,1)(s1) = q - 1/q, though both
words are transpositions. So MN cannot serve this entry point, and the
seminormal route is the one that can. The MN engine remains valuable as an
independent check, and the two agree symbolically on every standard element for
n = 2..5.

THE CONSTRUCTION, and the one place it departs from its numerical twin.
`build_seminormal_matrices_mp` sets the off-diagonal pair of each 2x2 block to
b = sqrt(|a a' + 1|), which is irrational in q and cannot be simplified in
Q(q). This module uses the SIMILAR rational form

    M[i,j] = a a' + 1,   M[j,i] = 1

which is conjugate to (b, b) by diag(..., b, ...). Conjugation preserves the
trace, so every character is identical; only the basis differs. That is checked
against the mp builder at 50 dps rather than asserted -- see
`computations/qbeta/qbeta_hecke_symbolic_seminormal_probe.py`.

ARITHMETIC. Exact throughout. No float appears anywhere in this module, and
`q` is never given a value; callers wanting a number substitute one themselves,
where the loss is visible.
"""

from __future__ import annotations

from functools import lru_cache

import sympy as sp

#: The Hecke parameter, as a free positive symbol. Callers comparing against a
#: witness should `subs(q, ...)` explicitly rather than expecting a value here.
q = sp.Symbol("q", positive=True)

#: h = q - 1/q, the corpus's Hecke deformation parameter (sigma^2 = h sigma + 1).
h = q - 1 / q

Partition = tuple[int, ...]


@lru_cache(maxsize=None)
def syts_and_contents(shape: Partition):
    """Standard Young tableaux of `shape` as {entry: cell}, plus cell contents.

    Mirrors the data shape of `hecke_characters.standard_young_tableaux` so the
    two builders index tableaux the same way.
    """
    cells = [(i, j) for i, row in enumerate(shape) for j in range(row)]
    contents = {(i, j): j - i for (i, j) in cells}
    n = sum(shape)
    out: list[dict[int, tuple[int, int]]] = []

    def grow(k: int, rowlen: list[int], acc: dict) -> None:
        if k > n:
            out.append(dict(acc))
            return
        for i in range(len(shape)):
            j = rowlen[i]
            if j >= shape[i]:
                continue
            if i > 0 and rowlen[i - 1] <= j:
                continue                     # the cell above must be filled first
            rowlen[i] += 1
            acc[k] = (i, j)
            grow(k + 1, rowlen, acc)
            del acc[k]
            rowlen[i] -= 1

    grow(1, [0] * len(shape), {})
    return tuple(out), contents


@lru_cache(maxsize=None)
def seminormal(shape: Partition) -> tuple[sp.Matrix, ...]:
    """sigma_1 .. sigma_{n-1} in the seminormal basis, exact over Q(q)."""
    syts, contents = syts_and_contents(shape)
    dim = len(syts)
    if dim == 0:
        return ()
    index = {tuple(sorted(t.items())): i for i, t in enumerate(syts)}
    n = sum(shape)
    mats: list[sp.Matrix] = []

    for k in range(1, n):
        M = sp.zeros(dim, dim)
        done: set[int] = set()
        for i in range(dim):
            if i in done:
                continue
            cell_k, cell_k1 = syts[i][k], syts[i][k + 1]
            rho = contents[cell_k1] - contents[cell_k]
            a = sp.simplify(h / (1 - q ** (-2 * rho)))
            a_prime = sp.simplify(h / (1 - q ** (2 * rho)))

            swapped = dict(syts[i])
            swapped[k], swapped[k + 1] = cell_k1, cell_k
            j = index.get(tuple(sorted(swapped.items())))
            if j == i:
                j = None

            if j is None:
                # k and k+1 in the same row or column: sigma acts by a scalar.
                M[i, i] = a
                done.add(i)
            else:
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = sp.simplify(a * a_prime + 1)   # = b^2
                M[j, i] = sp.Integer(1)
                done.update((i, j))
        mats.append(sp.simplify(M))
    return tuple(mats)


def _normalize_word(word):
    """Accept both word shapes in use in this repo, and reject anything else.

    Two forms are live:

      SIGNED   [(sign, gen_1based), ...]        -- `chi_lambda_braid`'s form,
                                                  sign in {+1, -1, '+', '-'}
      TYPED    [(c, d, gen_0based), ...]        -- `chi_all_lambda`'s form, a
                                                  crossing being the ALGEBRA
                                                  element c*sigma_g + d

    Returns the typed form `(c, d, gen_0based)`, since sigma^-1 = sigma - h
    makes SIGNED a special case of TYPED: (1, 0) and (1, -h).

    Guessing between them by length alone would be a silent-misread hazard, so
    the arity is required to be uniform and anything else raises.
    """
    if not word:
        return []
    arities = {len(item) for item in word}
    if arities == {2}:
        out = []
        for sign, gen in word:
            positive = sign in ('+', 1, True)
            out.append((sp.Integer(1),
                        sp.Integer(0) if positive else -h,
                        int(gen) - 1))
        return out
    if arities == {3}:
        return [(sp.sympify(c), sp.sympify(d), int(g)) for c, d, g in word]
    raise ValueError(
        "braid word must be uniformly [(sign, gen_1based), ...] or "
        f"[(c, d, gen_0based), ...]; got item arities {sorted(arities)}"
    )


def word_matrix(shape: Partition, word) -> sp.Matrix:
    """Matrix of a braid word in the irrep `shape`, exact over Q(q)."""
    mats = seminormal(tuple(shape))
    if not mats:
        raise ValueError(f"no standard tableaux for shape {shape}")
    dim = mats[0].shape[0]
    out = sp.eye(dim)
    for c, d, g in _normalize_word(word):
        if not 0 <= g < len(mats):
            raise ValueError(
                f"generator index {g} out of range for shape {shape} "
                f"({len(mats)} generators)")
        out = out * (c * mats[g] + d * sp.eye(dim))
    return out


def chi_lambda_braid_symbolic(shape, word) -> sp.Expr:
    """`chi_lambda(beta)` as an exact element of Q(q).

    The return is a sympy expression in the module-level symbol `q`, not a
    number and not a string: substituting a value is the caller's decision and
    belongs where the precision loss is visible.
    """
    return sp.cancel(sp.together(sp.expand(sp.trace(word_matrix(tuple(shape), word)))))


__all__ = [
    "q", "h", "syts_and_contents", "seminormal",
    "word_matrix", "chi_lambda_braid_symbolic",
]
