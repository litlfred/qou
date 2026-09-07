#!/usr/bin/env python3
"""atom_bond_product_closed_form_probe.py — c₀, c₁ AND c₂ in closed form. (qou-qqm4)

## The result

The atom word is a **chain**: `A` nucleon blocks on disjoint strand triples, joined by `A − 1`
single interface letters at generators `3k + 2`. Its normalised Markov trace is the corresponding
**product over nucleons and bonds**:

    tr(atom; ordering)  =  ∏_nucleons  a·(1 + r ε + q ε²)   ·   ∏_bonds  (1/2)·(1 + ρ_b ε + τ_b ε²)

Every factor is **measured on a smaller object**, never fitted:

    proton    a = 1/2   r = 3/2   q = 23/4          measured at n = 3 (one nucleon, free word)
    neutron   a = 1/2   r = −1    q = 3
    bond pp   (1/2)·(1,  2,  1/2)                   measured at A = 3 by turning ONE interface on
    bond pn   (1/2)·(1,  0,  3/2)                   (`m_pp` / `m_pn` / `m_nn` select which)
    bond nn   (1/2)·(1, −2,  5/2)

and with `Δtr = tr(free) − tr(atom)`, `c₀ = [ε⁰]`, `c₁ = [ε¹]`, `c₂ = [ε¹]+[ε²]`, this reproduces
**every recorded value on 9 words, `A = 2…5`** — `pp, pn, nn, 3p, T, ³He, 3n, ⁴He, ⁵He`.

**This is `qou-qqm4`'s goal (2).** `c₂` has a closed form; it just is not a form in `(Z, N)` alone,
which is why the `(u, D)` leave-one-out (`c2_pairwise_shape_holdout_probe`) had to miss. It is a
form in the **ordering** — a product over nucleons and adjacent pairs.

## Why this is not a fit

Five measured series predict twenty-seven numbers (9 words × 3 orders), with **no free parameter at
any step**. Two further points on how the inputs were obtained:

- The bond factors were extracted from **one-interface** words at `A = 3`, and every prediction here
  is for a **multi-interface** word. So even T and ³He — the words the extraction used — are
  non-trivial tests of the *product*, not restatements of their own data.
- `A = 2` (three words), `A = 4` and `A = 5` contributed **nothing** to any input and are held out
  outright. `⁵He` in particular (`n = 15`, `2¹⁵` basis states, 49 min) was computed for an unrelated
  question — the `k(A)` refutation — before this form existed.

The three bond factors also fall into an obvious pattern, `ρ_b = p_b − n_b` and `τ_b = 1/2 + n_b`
(counting protons and neutrons in the bond, `p_b + n_b = 2`). That is a *description* of three
measured values, carrying one spare degree of freedom, and it is **not** what the closed form above
uses — the form uses the measured factors themselves, so nothing here rests on the pattern being
right. It is reported because it is the shape a derivation would have to produce.

## What each earlier finding becomes

- `c₀ = 2^(−A) − 2^(1−2A)` is the `ε⁰` part: `∏ a = 2^(−A)` over nucleons times `2^(−(A−1))` over
  bonds. The interfaces act **multiplicatively** (each halves the leading term), which is why the
  `Δ` of one interface is *not* additive over interfaces — measured, and it had to be.
- `(S_p, S_n) = (6, −4)`, `c₁`'s only ordering-dependent input, is `4·(r_p, r_n)`.
- `(37, 20)` from the free word's second order falls out of `q_p, q_n`.
- The `|S| = 2` pair classes (`c2_pair_class_decomposition_probe`) are the second-order terms of this
  product: `intra` from a single nucleon's `q`, `cross` from two nucleons' `r`, `n-if` from one
  nucleon and one bond, `if-if` from two bonds — which is why `if-if` counts *pairs of like
  interfaces* and so cannot be affine in `I_pp − I_nn`.

## 🛑 Scope — what is NOT established

1. **Sorted orderings only *here* — but the unsorted case has since been tested, and it passed.**
   Every word in *this* file is `p…p n…n`, because `atom_canonical_crossings` took `(Z, N)` and
   nothing else. That is no longer the only word the corpus can build:
   `atom_word_explicit_ordering_probe` adds `ordering=` to the canonical builder (default unchanged,
   asserted identical on 14/14 words with `A ≤ 4`) and runs `pnp` at `A = 3`. Result: **6/6** —
   `c₀ = 3/32`, `c₁ = 3/16`, `c₂ = 177/128`, each predicted by the product from factors measured on
   *other* words, and `pnp ≠ ppn` so the check is not satisfied by a constant.

   That also settles the corollary this note flagged as an assumption. `pnp`'s two bonds are `(p,n)`
   and `(n,p)`, so the code's treatment of the mixed bond as **orientation-independent** is now a
   measurement rather than an untested convenience — at `A = 3`, orders ≤ 2. One ordering at one `A`
   is not "all orderings"; it is the first evidence of any kind, where before there was none.
2. **Orders 0, 1, 2 only**, and `A ≤ 5`.
3. **Not proved — and the corpus already holds the neighbouring theorem, which I first claimed it
   did not.** An earlier version of this file said "neither the free-word factorisation nor the bond
   product has a Lean statement". That is **wrong**:
   `QOU/MathlibExt/MonotoneWordTraceFactorizes.lean` (sorry-free, `lean`-direct exit 0, bean
   `qou-kru4`) proves `tr_stabWord_eq_prod_tr` — a **monotone** word's trace is `∏ tr(letter)`. I
   asserted an absence without grepping for it, in a session whose whole subject is that failure.

   **But it is a different statement, and the difference is the point.** That theorem factorises
   over **letters** of an *ascending* word, and the canonical word is **not ascending**: one
   nucleon's generator sequence is `[0,1,0,1,0,1,0,0,1,0,0]` against the grouped
   `[0,0,0,0,0,0,0,1,1,1,1]`. The corpus records that too, in bean `qou-wdij` (with the same two
   sequences), together with the fallout — the monotone transfer refuses on `main`, and the
   general-word kernel that replaced it **loses the `O(A)` scaling** (`A = 4` takes 621 s, a ~1700×
   jump). So letter-level factorisation is genuinely dead under owner ruling `qou-hu1f`.

   What survives is **block-and-bond** factorisation, and it survives for a different reason:
   nucleons act on **disjoint strand triples**, which is insensitive to how their internal letters
   are ordered. Disjointness is not monotonicity. That is why this file's product holds on exactly
   the word whose letter-level product the ruling destroyed — and it is the reconciliation between
   this result and `qou-kru4` / `qou-wdij`, neither of which states it.

   The *disjoint-block trace law* has no Lean statement — checked, not assumed:
   `QOU/MathlibExt/BraidJuxtapositionMonoid.lean` proves the juxtaposition **monoid** and the
   commutation of disjoint blocks, but no trace-multiplicativity over them. That, plus the bond
   factor's stabilisation, is the formalize-first follow-on.
4. **`q₀` never enters.** These are ε-series coefficients, exact rationals. Nothing here is evaluated
   at any anchor and nothing is wired to a witness or a content block.

SCOPE — (a) scope-limited. Exact `Fraction` arithmetic throughout; no float, no `q`, no witness.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

import canonical_braid_crossings as _CBC  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

_ORIG = _CBC.atom_canonical_crossings

# Recorded exact values, canonical word. c₁ from PR #6920's closed form (44/44); c₂ from the exact
# ε-series and reproduced independently by [◇]. ⁵He is from the A=5 run (49 min) — recomputing it
# on every invocation is not reasonable, so it is a target here and `--verify-live` re-measures the
# cheap ones. If any of these ever disagree with a fresh run, the TARGET is what to re-derive.
C1 = {"pp": F(1, 8), "pn": F(1, 16), "nn": F(0), "3p": F(19, 64), "T": F(1, 64),
      "3He": F(1, 8), "3n": F(-5, 32), "4He": F(7, 128), "5He": F(1, 256)}
C2 = {"pp": F(33, 32), "pn": F(25, 32), "nn": F(1, 16), "3p": F(117, 64), "T": F(99, 128),
      "3He": F(157, 128), "3n": F(5, 16), "4He": F(439, 512), "5He": F(1001, 2048)}
ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "3p": (3, 0), "T": (1, 2), "3He": (2, 1),
      "3n": (0, 3), "4He": (2, 2), "5He": (2, 3)}
# Cheap enough to re-measure under --verify-live (n ≤ 9).
LIVE_OK = ("pp", "pn", "nn", "3p", "T", "3He", "3n")


def mul(a, b):
    """Truncated product of two order-2 series."""
    return [a[0] * b[0], a[0] * b[1] + a[1] * b[0],
            a[0] * b[2] + a[1] * b[1] + a[2] * b[0]]


def div(a, b):
    """a/b as a truncated order-2 series; b[0] must be non-zero."""
    r0 = a[0] / b[0]
    r1 = (a[1] - r0 * b[1]) / b[0]
    r2 = (a[2] - r0 * b[2] - r1 * b[1]) / b[0]
    return [r0, r1, r2]


def _series(Z, N, *, inter, **mk):
    """Order-2 ε-series of the normalised trace, with the given interface multiplicities."""
    if mk:
        _CBC.atom_canonical_crossings = (
            lambda z, n, **kw: _ORIG(z, n, **{**kw, **mk}))
        _D.atom_canonical_crossings = _CBC.atom_canonical_crossings
    try:
        c, _ = _D.trace_expansion(Z, N, inter, 2)
    finally:
        _CBC.atom_canonical_crossings = _ORIG
        _D.atom_canonical_crossings = _ORIG
    return list(c)


def measure_inputs(log=print):
    """The five input series. Each is measured on a SMALLER object than anything predicted."""
    nuc = {}
    for key, Z, N in (("p", 1, 0), ("n", 0, 1)):
        c = _series(Z, N, inter=False)
        nuc[key] = c
        log(f"    nucleon {key}:  a = {c[0]}   r = {c[1]/c[0]}   q = {c[2]/c[0]}"
            f"   (measured at n = 3, one nucleon, free word)")

    # Bond factors: take a two-nucleon-plus word, turn exactly ONE interface on, divide by the
    # free word. T = p n n has bonds (pn, nn); ³He = p p n has bonds (pp, pn). Extracting from
    # ONE-interface words makes every multi-interface prediction below a real test of the product.
    bond = {}
    for word_Z, word_N, which, mk in (
        (2, 1, "pp", dict(m_pp=1, m_pn=0, m_nn=0)),
        (1, 2, "pn", dict(m_pp=0, m_pn=1, m_nn=0)),
        (1, 2, "nn", dict(m_pp=0, m_pn=0, m_nn=1)),
    ):
        free = _series(word_Z, word_N, inter=True, m_pp=0, m_pn=0, m_nn=0)
        one = _series(word_Z, word_N, inter=True, **mk)
        R = div(one, free)
        bond[which] = R
        log(f"    bond {which}:  {[str(x) for x in R]}"
            f"   = (1/2)·(1, {R[1]/R[0]}, {R[2]/R[0]})"
            f"   (measured at A = 3, ONE interface on)")
    return nuc, bond


def predict(Z, N, nuc, bond):
    """Predicted (free, atom) order-2 series for the sorted ordering `p…p n…n`."""
    free = [F(1), F(0), F(0)]
    for _ in range(Z):
        free = mul(free, nuc["p"])
    for _ in range(N):
        free = mul(free, nuc["n"])
    atom = list(free)
    order = ["p"] * Z + ["n"] * N
    for x, y in zip(order, order[1:]):
        # A mixed bond keys to "pn" whichever way round it sits. In a SORTED ordering only the
        # (p, n) orientation ever occurs, so treating (n, p) as the same factor is an untested
        # assumption, not a measurement — see the scope note. It is inert here and would matter
        # the moment an unsorted ordering is attempted.
        key = "pp" if x == y == "p" else "nn" if x == y == "n" else "pn"
        atom = mul(atom, bond[key])
    return free, atom


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-live", action="store_true",
                    help="also re-measure the n ≤ 9 targets instead of trusting the table (~2 min)")
    args = ap.parse_args()
    t0 = time.time()

    print("=" * 96)
    print("  c₀, c₁ AND c₂ in closed form: the atom word is a product over nucleons and BONDS")
    print("=" * 96)
    print("  tr(atom) = ∏_nucleons a(1 + rε + qε²) · ∏_bonds (1/2)(1 + ρ_b ε + τ_b ε²)")
    print("  Every factor is measured on a SMALLER object. No free parameter at any step.\n")

    print("  INPUTS (5 series):")
    nuc, bond = measure_inputs(log=lambda s: print(s))
    print(f"    [{time.time()-t0:5.1f}s]\n")

    print(f"  {'case':<6}{'(Z,N)':>8}{'c₀ pred':>12}{'c₀ exact':>12}"
          f"{'c₁ pred':>12}{'c₁ rec':>12}{'c₂ pred':>13}{'c₂ rec':>13}")
    ok = True
    for nm, (Z, N) in ZN.items():
        A = Z + N
        free, atom = predict(Z, N, nuc, bond)
        d = [f - a for f, a in zip(free, atom)]
        c0p, c1p, c2p = d[0], d[1], d[1] + d[2]
        c0e = F(1, 2) ** A - 2 * F(1, 2) ** (2 * A)     # the derived floor
        good = (c0p == c0e and c1p == C1[nm] and c2p == C2[nm])
        ok = ok and good
        print(f"  {nm:<6}{f'({Z},{N})':>8}{str(c0p):>12}{str(c0e):>12}"
              f"{str(c1p):>12}{str(C1[nm]):>12}{str(c2p):>13}{str(C2[nm]):>13}"
              f"  {'ok' if good else 'FAIL'}")
    print(f"  ⇒ {f'{len(ZN)}/{len(ZN)} — c₀, c₁ and c₂ all reproduced, A = 2…5.' if ok else 'FAIL — the bond product does NOT hold; do not quote this file.'}")

    live = True
    if args.verify_live:
        print(f"\n  --verify-live: re-measuring the n ≤ 9 targets rather than trusting the table")
        for nm in LIVE_OK:
            Z, N = ZN[nm]
            f_ = _series(Z, N, inter=False)
            a_ = _series(Z, N, inter=True)
            d = [x - y for x, y in zip(f_, a_)]
            hit = (d[1] == C1[nm] and d[1] + d[2] == C2[nm])
            live = live and hit
            print(f"    {nm:<6} c₁ {str(d[1]):>10} vs {str(C1[nm]):>10}   "
                  f"c₂ {str(d[1]+d[2]):>12} vs {str(C2[nm]):>12}   {'ok' if hit else 'TABLE IS STALE'}"
                  f"   [{time.time()-t0:5.1f}s]")
        print(f"    ⇒ {'the recorded table matches a fresh run.' if live else 'THE TABLE IS STALE — re-derive it before quoting anything above.'}")

    print("\n  The bond factors fall into a pattern — ρ_b = p_b − n_b, τ_b = 1/2 + n_b — which is a")
    print("  DESCRIPTION of three measured values with one spare dof, and is NOT what the form above")
    print("  uses: that uses the measured factors themselves. Reported because it is the shape a")
    print("  derivation would have to produce.")
    print("\n  🛑 SCOPE. (1) SORTED orderings only — every word here is p…p n…n, because the canonical")
    print("  construction takes (Z, N). The bond product is STATED for an arbitrary ordering and is")
    print("  UNTESTED on one; `pnp` is the discriminating case and needs the canonical construction")
    print("  extended, not a hand-built word. (2) Orders 0,1,2 and A ≤ 5 only. (3) NOT PROVED, and")
    print("  the corpus DOES hold the neighbouring theorem — MonotoneWordTraceFactorizes (qou-kru4),")
    print("  which an earlier version of this file wrongly said did not exist. That one factorises")
    print("  over LETTERS of an ASCENDING word; the canonical word is not ascending (qou-wdij), so")
    print("  letter-level factorisation really is dead under the ruling. THIS product is over BLOCKS")
    print("  and BONDS and survives for a different reason — disjoint strand triples, insensitive to")
    print("  internal letter order. Disjointness is not monotonicity, and that is the reconciliation")
    print("  neither of those beans states. The disjoint-block trace law itself has no Lean statement")
    print("  (checked: BraidJuxtapositionMonoid proves the monoid and the commutation of disjoint")
    print("  blocks, not trace-multiplicativity over them). (4) No q₀ enters")
    print("  anywhere: these are exact rational ε-coefficients, wired to nothing.")
    print(f"\n  ({time.time()-t0:.1f}s)")
    return 0 if (ok and live) else 1


if __name__ == "__main__":
    sys.exit(main())
