"""Formal-q Markov trace on the H_3(q) NF basis — symbolic over ℚ(s).

Spec Step 2 (`docs/scope/2026-06-04-fibre-composite4-implementation-spec.md`).
The float / Fraction Markov trace in `gram.py` evaluates at a fixed
numeric q (the substrate q₀, or the 111/100 rational model). This module
carries q **symbolically** so the trace can later be evaluated at any
point — in particular at **roots of unity** (Step 3), which the fibre /
Habiro analysis of the Q_β c_3 residue A needs.

## Why the variable is s = q^½, not q

The Markov weight `z = 1/(q^½ + q^−½)` is *not* a Laurent polynomial in
q (or in s): in `s = q^½` it is the rational function `z = s/(s²+1)`.
So the natural coefficient ring is **ℚ(s)** (rational functions in s),
not Laurent polynomials. We therefore use sympy with the symbol `s`;
`q = s²`, `h = q − q⁻¹ = s² − s⁻²` (Laurent in s), `z = 1/(s + s⁻¹)`.

## Optional dependency

This module requires `sympy`. It is imported lazily by the pyhecke
package (`pyhecke/__init__.py` PEP-562 loader), so importing pyhecke
itself does not require sympy — only `import pyhecke.trace_formal` does.

## Public API

    s, q_of_s, h_formal, z_formal      — the symbolic atoms
    TR_M_formal()                      — symbolic Markov weights (6-vector)
    nf_of_word_formal(word)            — NF 6-vector of a braid word
    nf_tr_formal(nf)                   — symbolic Markov trace of an NF vector
    markov_trace_combo_formal(terms)   — tr_M(Σ cᵢ σ_{wᵢ}), simplified
    specialize(expr, s_value)          — substitute s and simplify/evalf
    eval_at_root_of_unity(expr, N, k)  — q = exp(2πik/N) → s = exp(πik/N)
"""
from __future__ import annotations

import sympy as sp

# s = q^{1/2}.  Declared positive so sympy keeps real-axis simplifications
# clean; root-of-unity evaluation substitutes a complex value explicitly.
s = sp.symbols("s", positive=True)
q_of_s = s ** 2
h_formal = q_of_s - 1 / q_of_s          # = s² − s⁻²  (Laurent in s)
z_formal = 1 / (s + 1 / s)              # = s/(s²+1)  (rational in s)


def TR_M_formal() -> list[sp.Expr]:
    """Symbolic Markov-Ocneanu-Wenzl weights on the NF basis
    [γ, σ₀, σ₁, L₊, L₋, e⁻] — mirrors `gram.TR_M` with z, h symbolic.
    tr_M(e⁻) = h·z² + z (the 2026-05-19 fix, not z³)."""
    z, h = z_formal, h_formal
    return [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]


# NF multiplication by σ_gen (c=1, d=0) — symbolic mirror of gram.hm.
def _hm_formal(nf: list[sp.Expr], gen: int) -> list[sp.Expr]:
    h = h_formal
    r = [sp.Integer(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, sp.Integer(1))]),
            (1, [(1, h), (0, sp.Integer(1))]),
            (2, [(3, sp.Integer(1))]),
            (3, [(3, h), (2, sp.Integer(1))]),
            (4, [(5, sp.Integer(1))]),
            (5, [(5, h), (4, sp.Integer(1))]),
        ]
    else:
        tables = [
            (0, [(2, sp.Integer(1))]),
            (1, [(4, sp.Integer(1))]),
            (2, [(2, h), (0, sp.Integer(1))]),
            (3, [(5, sp.Integer(1))]),
            (4, [(4, h), (1, sp.Integer(1))]),
            (5, [(5, h), (3, sp.Integer(1))]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return [sp.expand(x) for x in r]


def nf_of_word_formal(word) -> list[sp.Expr]:
    """Symbolic NF 6-vector of a braid word (tuple of 0/1 generators)."""
    nf = [sp.Integer(1), sp.Integer(0), sp.Integer(0),
          sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    for g in word:
        nf = _hm_formal(nf, g)
    return nf


def nf_tr_formal(nf: list[sp.Expr]) -> sp.Expr:
    """Symbolic Markov trace of an NF 6-vector (dot with TR_M_formal)."""
    weights = TR_M_formal()
    return sp.simplify(sum(nf[i] * weights[i] for i in range(6)))


def markov_trace_combo_formal(terms) -> sp.Expr:
    """Symbolic tr_M(Σ cᵢ·σ_{wᵢ}) over ℚ(s).

    `terms` is an iterable of `(coeff, word)`; coeffs may be ints,
    Fractions, or sympy expressions. Returns a simplified rational
    function in `s`."""
    acc = [sp.Integer(0)] * 6
    for c, word in terms:
        cf = sp.nsimplify(c) if not isinstance(c, sp.Basic) else c
        nfw = nf_of_word_formal(word)
        for i in range(6):
            acc[i] += cf * nfw[i]
    return nf_tr_formal(acc)


def specialize(expr: sp.Expr, s_value, *, dps: int = 50):
    """Substitute a numeric value for s and evaluate to `dps` digits.

    `s_value` may be real or complex; returns a sympy Float/complex."""
    return sp.N(expr.subs(s, sp.sympify(s_value)), dps)


def eval_at_root_of_unity(expr: sp.Expr, N: int, k: int = 1, *, dps: int = 50):
    """Evaluate `expr` at q = exp(2πik/N), i.e. s = q^½ = exp(πik/N).

    Returns a (generally complex) sympy number at `dps` digits. This is
    the Step-3 hook: a Habiro element is the *family* of these values
    over all roots of unity, not any single one."""
    s_val = sp.exp(sp.I * sp.pi * sp.Rational(k, N))
    return sp.N(expr.subs(s, s_val), dps)
