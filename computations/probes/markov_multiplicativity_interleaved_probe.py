#!/usr/bin/env python3
"""
Probe — the Markov trace really is multiplicative over generators, so no pair term.

qou-ls86's last named lead: the Coulomb deficit is that `Q*h` is LINEAR in charge
where electrostatic energy is QUADRATIC, and a `Q^2`-like term cannot live at one
bond (a single interface generates only the 2-dimensional `span{1, sigma}`, since
`sigma^2 = h sigma + 1`). The hope was that it lives at MULTI-BOND level, where
distinct bonds' crossings can pair. That is also the one place the many-body
collective term could come from. This probe tests it.

## A circular test, avoided

The obvious test — feed a multi-bond word to `pyhecke.trace.markov_trace_at_q`
and see whether the trace factorises — is **circular**. Reading the source:

    tr_M = 1.0
    for gen in range(n_strands - 1):
        ...                    # Hecke-reduce WITHIN this generator only
        Vs = z_mark * a + b
        tr_M *= Vs             # <-- multiplicativity is ASSUMED here

The production trace is *implemented as* a bare product over generators, and its
docstring says so ("Only the descended term = Pi V_i"). All three entry points —
`markov_trace_at_q`, `markov_trace_symbolic_eval`, `tr_M_at_q0_via_crt` — carry
the same "descended" wording. So testing factorisation against them measures the
implementation, not the algebra. (This is the same shape as the circular CHECK-1
in `chain_binding_hyperbola_no_peak_probe.py`, which compared a closed form
against itself.)

## The independent route

`pyhecke.trace.nf_tr` evaluates the Markov trace against the Groebner-Shirshov
normal-form basis of `H_3`,

    NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
             =  1,  sigma0, sigma1, sigma0 sigma1, sigma1 sigma0, sigma0 sigma1 sigma0

as `nf_tr(nf) = sum_i nf[i] * TR_M[i]` — a genuine linear functional on the
algebra, not a per-generator product. The basis contains the **interleaved** word
`(0,1,0)`, which is exactly the case a product formula cannot see: the product
formula depends only on the per-generator *multiset*, so it must give the same
answer for `sigma0 sigma1 sigma0` and for `sigma0^2 sigma1`.

## Result — they agree IDENTICALLY, and the float64 test that first "showed" it
## was vacuous

**RETRACTED METHOD (2026-08-18, owner directive).** The first revision of this
probe evaluated `nf_tr` against `pyhecke.trace.TR_M`, which is a **float64**
table, and reported

    interleaved - product = 7.4e-17   ->  "the product formula is EXACT"

That is not a result. Agreement at `1e-16` is the **floor of float64
arithmetic**, obtained no matter what is true, so the test could not have
distinguished the hypotheses. It was recorded as a "scope limit" and shipped —
which is exactly the move the NO-FLOAT64 directive forbids (AGENTS.md,
"PROBES ARE NOT EXEMPT").

**The conclusion survives, by exact algebra rather than by measurement.** On
`H_3`, from the Markov trace's defining properties — normalisation `tr(1)=1`,
the Markov property `tr(x sigma_last) = z tr(x)`, cyclicity, and the Hecke
relation `sigma^2 = h sigma + 1` — with no numbers at all:

    tr(s0)        = z
    tr(s0 s1)     = z * tr(s0) = z^2            [Markov property]
    tr(s0 s1 s0)  = tr(s0^2 s1)                 [cyclicity]
                  = h tr(s0 s1) + tr(s1)        [Hecke relation]
                  = h z^2 + z
    product formula:  (z h + 1) * z = h z^2 + z

    interleaved - product = 0,  identically in (q, z, h)

Not "agrees to 1e-16" — **equal as rational functions**.

## Why this SHARPENS the n = 3 caveat rather than removing it

The exact derivation shows *why* it works: cyclicity moves the trailing `s0` to
the front, where the Hecke relation collapses `s0^2` back into `span{1, s0}`. So
the single interleaved word of `H_3` is reducible to a sequential one **by
cyclicity alone**. That is a property of `H_3` being small — its NF basis has
exactly one interleaved word, and it happens to be a cyclic rotation of a
sequential one.

For larger `n` there are interleaved words with no such rotation (e.g.
`s0 s1 s0 s2 s1`), and nothing here says the product formula survives them. The
general-`n` question is **open**, and this probe is evidence only at `n = 3`.

NO WITNESS: an exact symbolic identity in `sympy` over the rational function
field; no floating-point arithmetic anywhere.

Bean qou-ls86; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import sympy as sp


def main() -> int:
    # EXACT throughout: symbols over the rational function field, no floats.
    z, h = sp.symbols("z h")

    # Markov trace on H_3 from its defining properties:
    #   tr(1) = 1 ; tr(x sigma_last) = z tr(x) ; cyclicity ; sigma^2 = h sigma + 1
    tr_1 = sp.Integer(1)
    tr_s0 = z
    tr_s1 = z
    tr_s0s1 = sp.expand(z * tr_s0)              # Markov property, x = s0 in H_2
    tr_s1s0 = tr_s0s1                           # cyclicity
    # interleaved: cyclicity rotates the trailing s0 forward, Hecke collapses s0^2
    tr_s0s1s0 = sp.expand(h * tr_s0s1 + tr_s1)
    product_formula = sp.expand((z * h + 1) * z)

    print("Is the Markov trace multiplicative over generators? EXACT check.\n")
    print("  The production trace ASSUMES it (`tr_M *= Vs` per generator), so testing")
    print("  factorisation against markov_trace_at_q would be CIRCULAR.")
    print("  And evaluating nf_tr against pyhecke.trace.TR_M would be VACUOUS —")
    print("  TR_M is float64, so any such test agrees to ~1e-16 regardless of truth.")
    print("  Both routes rejected; this derives the traces symbolically instead.\n")

    print("  Markov trace on H_3, exact in (z, h):\n")
    print(f"    tr(1)          = {tr_1}")
    print(f"    tr(s0)         = {tr_s0}")
    print(f"    tr(s0 s1)      = {tr_s0s1}          [Markov property]")
    print(f"    tr(s1 s0)      = {tr_s1s0}          [cyclicity]")
    print(f"    tr(s0 s1 s0)   = {tr_s0s1s0}   <-- INTERLEAVED")
    print(f"    (z h + 1) * z  = {product_formula}   <-- PRODUCT FORMULA\n")

    delta = sp.simplify(tr_s0s1s0 - product_formula)
    print(f"  interleaved - product = {delta}")
    print("  -> EQUAL AS RATIONAL FUNCTIONS, identically in (q, z, h).")
    print("     Not 'agrees to 1e-16' — there is no numeric comparison here.\n")

    print("## Derivation, in full\n")
    print("    tr(s0 s1 s0) = tr(s0^2 s1)          cyclicity")
    print("                 = h tr(s0 s1) + tr(s1) Hecke: s0^2 = h s0 + 1")
    print("                 = h z^2 + z            Markov property")
    print("    (z h + 1) z  = h z^2 + z\n")

    print("## Consequence\n")
    print("  log tr is strictly additive over generators on H_3, so NO term quadratic")
    print("  in crossings across distinct bonds exists there. The trace does not")
    print("  couple distinct bonds. The last named lead for both the Coulomb")
    print("  order-deficit and the many-body collective term is closed at n = 3.\n")

    print("## Why this SHARPENS the n = 3 caveat\n")
    print("  The derivation shows WHY it works: cyclicity rotates the trailing s0")
    print("  forward, where the Hecke relation collapses s0^2 into span{1, s0}. So")
    print("  H_3's single interleaved word is a cyclic rotation of a sequential one.")
    print("  That is a property of H_3 being small. For larger n there are interleaved")
    print("  words with no such rotation (e.g. s0 s1 s0 s2 s1), and nothing here says")
    print("  the product formula survives them. General n is OPEN.\n")
    print("(no witness by design — an exact symbolic identity, no floating point.)")

    assert delta == 0, "the identity must hold exactly, not approximately"
    assert isinstance(tr_s0s1s0, sp.Expr), "traces must stay symbolic"
    return 0


if __name__ == "__main__":
    sys.exit(main())
