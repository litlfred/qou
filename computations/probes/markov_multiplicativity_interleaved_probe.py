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

## Result — they agree, so there is no cross-generator term

At the substrate anchor, with `sigma0^2 sigma1 = h*(sigma0 sigma1) + sigma1` by
the Hecke relation:

    tr_M( sigma0 sigma1 sigma0 )   INTERLEAVED   0.6911664783584446
    tr_M( sigma0^2 sigma1 )        SEQUENTIAL    0.6911664783584445
    (z*h + 1) * z                  PRODUCT       0.6911664783584445

    interleaved - product = 7.4e-17

All three coincide. The product formula is **exact** for the interleaved word, so
`log tr` is strictly additive over generators and **no term quadratic in crossings
across distinct bonds exists** at `n = 3`.

## Consequence

The last named lead for both the Coulomb order-deficit and the many-body
collective term is closed at the smallest interleaved case. A `Q^2`-like pair
energy cannot be extracted from this trace by going multi-bond, because the trace
does not couple distinct bonds at all.

## Scope — narrow, and stated as such

**Scope-(a).** Established: at `n = 3`, on the one interleaved basis word, the
product formula reproduces the independent NF-basis Markov trace. Two real
limits:

* **`n = 3` only.** `H_3` has a 6-element NF basis with exactly one interleaved
  word. Multiplicativity in general `H_n` is not established here; it is standard
  for far-apart generators (the Markov property `tr(x sigma_n) = z tr(x)` iterated
  down the tower), and this probe adds the adjacent-generator case at the smallest
  `n`.
* **float64 resolution.** `TR_M` is a float64 table, so the agreement resolves
  only to `~1e-16`. A cross term smaller than that would be invisible. Nothing
  here rules out a term at that scale — but a term at `1e-16` cannot supply a
  12.1x Coulomb shortfall.

NOT established: multiplicativity for every word in every `H_n`; that no pair
term exists anywhere in the framework. Only that this route does not supply one.

NO WITNESS: two evaluations of an existing linear functional on the NF basis;
the table reproduces it.

Bean qou-ls86; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent / "tools" / "pyhecke" / "python"))
del _Path, _bridge

import sys

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR as Q50


def main() -> int:
    mp.mp.dps = 40
    import pyhecke.gram as G
    from pyhecke.trace import nf_tr, TR_M

    q = mp.mpf(str(Q50))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)

    print("Is the Markov trace multiplicative over generators? Independent check.\n")
    print("  The production trace ASSUMES it (`tr_M *= Vs` per generator), so testing")
    print("  factorisation against markov_trace_at_q would be CIRCULAR. Using the")
    print("  Groebner-Shirshov normal-form functional nf_tr instead.\n")
    print(f"  NF basis: {G.NF_BASIS}")
    print(f"  names   : {G.NF_NAMES}\n")

    nf_inter = [0, 0, 0, 0, 0, 1]          # sigma0 sigma1 sigma0
    nf_seq = [0, 0, 1, h, 0, 0]            # sigma0^2 sigma1 = h*(s0 s1) + s1
    ti = mp.mpf(str(nf_tr(nf_inter)))
    ts = mp.mpf(str(nf_tr(nf_seq)))
    prod = (z * h + 1) * z

    print("  The product formula sees only the per-generator MULTISET, so it cannot")
    print("  distinguish these two words. The NF functional can.\n")
    print("| word                    | kind        | tr_M                |")
    print("| ----------------------- | ----------- | ------------------- |")
    print(f"| sigma0 sigma1 sigma0    | INTERLEAVED | {mp.nstr(ti, 16):<19} |")
    print(f"| sigma0^2 sigma1         | sequential  | {mp.nstr(ts, 16):<19} |")
    print(f"| (z*h + 1) * z           | PRODUCT     | {mp.nstr(prod, 16):<19} |")
    print(f"\n  interleaved - product = {mp.nstr(ti - prod, 8)}")
    print(f"  interleaved - sequential = {mp.nstr(ti - ts, 8)}\n")

    print("## Consequence\n")
    print("  All three coincide: the product formula is EXACT for the interleaved")
    print("  word, so log tr is strictly additive over generators and NO term")
    print("  quadratic in crossings across distinct bonds exists at n = 3.")
    print("  The last named lead for both the Coulomb order-deficit and the")
    print("  many-body collective term is closed at the smallest interleaved case:")
    print("  the trace does not couple distinct bonds at all.\n")
    print("## Scope — narrow, stated as such\n")
    print("  Scope-(a). n = 3 ONLY: H_3's NF basis has exactly one interleaved word.")
    print("  Multiplicativity in general H_n is not established here (it is standard")
    print("  for far-apart generators via tr(x sigma_n) = z tr(x); this adds the")
    print("  adjacent case at the smallest n).")
    print("  float64 resolution: TR_M is a float64 table, so agreement resolves only")
    print("  to ~1e-16. A cross term below that is invisible — but a 1e-16 term")
    print("  cannot supply a 12.1x Coulomb shortfall.")
    print("\n(no witness by design — two evaluations of an existing NF functional.)")

    assert abs(ti - prod) < mp.mpf("1e-14"), "interleaved must match the product formula"
    assert abs(ti - ts) < mp.mpf("1e-14"), "the two orderings must agree"
    return 0


if __name__ == "__main__":
    sys.exit(main())
