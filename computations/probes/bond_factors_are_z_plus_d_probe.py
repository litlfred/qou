#!/usr/bin/env python3
"""bond_factors_are_z_plus_d_probe.py — the bond half of #6920 finding 9 was ALREADY in the corpus.

🛑 **THIS PROBE EXISTS TO CORRECT A MERGED CLAIM OF MINE.** PR #6920 finding 9 presented

    tr(atom) = ∏_nucleons a(1 + rε + qε²) · ∏_bonds (1/2)(1 + ρ_b ε + τ_b ε²)

as answering `qou-qqm4`'s goal (2), with the three bond factors "measured at `A = 3` by turning ONE
interface on". They were measured that way, and the values are right. **They are also, exactly, the
corpus's own `∏ᵢ (z + dᵢ)` — a bond model that was already recorded, with the same mechanism, before
that PR was opened.** This probe measures the identification, states what is and is not mine, and
records the correction where a reader of the compute will find it.

## What the corpus already had

`mass_at_3A_proper.atom_braid_word_3A`'s own docstring, and
`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`:

> the character ratio `R(Z,N) = tr_M(W_atom) / tr_M(W_free)` is **identical under the two orderings
> to ~1e-60** at `2H, 3H, 3He, 4He` — and equals `prod_i (z + d_i)` over the `A-1` interfaces under
> *both*. […] The reason is structural rather than numerical: the chain closure is a connected sum,
> and connected-sum multiplicativity of the Markov trace does not care how each summand's word is
> internally ordered. Reordering letters inside a block changes that block's trace; it does not
> change the interface factors.

That is the bond product, the invariance under intra-nucleon reordering, **and the mechanism**. My
"disjointness is not monotonicity" reconciliation, which #6920 called something "neither bean
states", is that paragraph in different words. A fuller probe family sits alongside it —
`the_character_ratio_derivation_path_is_the_bond_model_probe`,
`the_pn_bond_is_an_average_and_cannot_be_extremal_probe`, `pairwise_ceiling_is_overstated_probe`.

## The identification, measured

`z_D = q³/(q²+1)` expanded at `q = 1+ε` is `(1/2, 1, 1/4)`, and each interface letter carries a `d`
by kind. The canonical word's interface letters are `pp → sigma`, `pn → averaged_weighted`,
`nn → sigma_inv`, and:

    bond   #6920's "measured" factor      z + d (kind)
    pp     1/2,  1,  1/4                  1/2,  1,  1/4    (sigma)
    pn     1/2,  0,  3/4                  1/2,  0,  3/4    (averaged_weighted)
    nn     1/2, -1,  5/4                  1/2, -1,  5/4    (sigma_inv)

Coefficient for coefficient. The one-interface extraction and `z + d` are two routes to the same
three objects.

## What of finding 9 survives as new — and it is the half that turns a ratio into an absolute

The corpus's bond model is about the **RATIO** `tr(atom)/tr(free)`. A ratio cancels the free word
entirely, so it says nothing about `tr(free)` and cannot give `c₀`, `c₁`, `c₂`, which are
coefficients of the **difference** `Δ = tr(free) − tr(atom)`. What #6920 adds is the other factor:

    tr(free; Z,N) = tr(p)^Z · tr(n)^N,   with (a, r, q) = (1/2, 3/2, 23/4) proton,
                                                          (1/2, -1,  3  ) neutron

measured on single nucleons at `n = 3`. Combining the two gives the absolute closed form, and the two
constants that fall out — `(S_p, S_n) = 4(r_p, r_n)` and `(37, 20)` from `q_p, q_n` — are downstream
of the free half, so they are not re-derivations of anything. Also new: the **ε-series** form of the
bond factors (the corpus's is the ratio at `q₀`), and the `A = 5` verification.

**Corrected framing, which is what should be quoted from here on:** finding 9 is the corpus's bond
half — re-derived independently, not new — **times** a free half that is new, giving an absolute
closed form neither had alone. Not "goal (2) answered", and not a mechanism nobody had stated.

## Why this was missed, since that is the reusable part

The corpus-grep before #6920 searched `.beans/`, `content/`, `docs/`, `computations/` and the library
for the *topic* — and found `qou-kru4`, `qou-wdij`, `MonotoneWordTraceFactorizes`. It did not find
this, because the bond model lives in a **producer's docstring** and in probe filenames phrased as
what they refute (`..._moves_absolute_traces_not_the_bond_model`, `..._is_overstated`). A topic grep
for "bond product" or "factorises" does not hit either. What would have hit: grepping the **word
builder itself** — the one function every claim in this arc goes through — before claiming anything
about what its output factorises into. That is now the standing lesson: *read the docstring of the
producer your result is about.*

SCOPE — (a) scope-limited. Exact `Fraction` arithmetic; the `z` expansion is symbolic at `q = 1+ε`
and the `d` series come from the corpus's own `letter_d_series`. No `q₀` evaluated, no float, no
witness, nothing wired, no Lean.
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

# The three bond factors as PR #6920 measured them — by turning ONE interface on at A = 3 and
# dividing by the free word. Recorded here as the thing to be identified, not as an input.
MEASURED_6920 = {
    "pp": [F(1, 2), F(1), F(1, 4)],
    "pn": [F(1, 2), F(0), F(3, 4)],
    "nn": [F(1, 2), F(-1), F(5, 4)],
}

# Which interface letter kind each bond type carries on the canonical word. Asserted below against
# `atom_canonical_crossings` rather than trusted.
EXPECTED_KIND = {"pp": "sigma", "pn": "averaged_weighted", "nn": "sigma_inv"}


def z_series(K: int = 2) -> list[F]:
    """`z_D = q³/(q²+1)` at `q = 1+ε`, to order `K`. Convention D, per the 2026-08-15 ruling."""
    num = [F(1), F(3), F(3)]          # (1+ε)³ truncated
    den = [F(2), F(2), F(1)]          # (1+ε)² + 1
    r = [F(0)] * (K + 1)
    r[0] = num[0] / den[0]
    r[1] = (num[1] - r[0] * den[1]) / den[0]
    r[2] = (num[2] - r[0] * den[2] - r[1] * den[1]) / den[0]
    return r


def interface_kinds(Z: int, N: int) -> list[tuple[int, str]]:
    """The `(generator, kind)` of every interface letter (`g % 3 == 2`) of the canonical word."""
    return [(g, k) for g, k in atom_canonical_crossings(Z, N, include_inter=True) if g % 3 == 2]


def main() -> int:
    print("=" * 92)
    print("  The bond factors of #6920 finding 9 ARE the corpus's z + d — a correction")
    print("=" * 92)

    z = z_series()
    print(f"  z_D = q³/(q²+1) at q = 1+ε:  {[str(x) for x in z]}\n")

    # 1. The interface letter kinds, read off the canonical word rather than assumed.
    print("  interface letter kinds on the canonical word (g % 3 == 2):")
    observed = {}
    for label, Z, N in (("3p", 3, 0), ("3He", 2, 1), ("T", 1, 2), ("3n", 0, 3)):
        ifs = interface_kinds(Z, N)
        print(f"    {label:<5} (Z={Z},N={N})  {ifs}")
        for _, kind in ifs:
            observed.setdefault(kind, 0)
            observed[kind] += 1
    kinds_ok = set(EXPECTED_KIND.values()) <= set(observed)
    print(f"    ⇒ the three expected kinds all occur: {kinds_ok}\n")

    # 2. The identification itself.
    print(f"    {'bond':<6}{'#6920 measured':>26}{'z + d':>26}{'kind':>22}")
    ok = kinds_ok
    for bond, kind in EXPECTED_KIND.items():
        d = _D.letter_d_series(kind, 2)
        zd = [a + b for a, b in zip(z, d)]
        hit = zd == MEASURED_6920[bond]
        ok = ok and hit
        print(f"    {bond:<6}{str([str(x) for x in MEASURED_6920[bond]]):>26}"
              f"{str([str(x) for x in zd]):>26}{kind:>22}  {'ok' if hit else 'MISMATCH'}")
    print(f"    ⇒ {'3/3 — coefficient for coefficient. Two routes, one object.' if ok else 'MISMATCH — the identification is wrong; do not quote this file.'}")

    print("\n  🛑 THE CORRECTION. PR #6920 finding 9 presented the bond product as answering")
    print("  qou-qqm4's goal (2) and called its reconciliation something 'neither bean states'.")
    print("  Both overstate. `atom_braid_word_3A`'s own docstring and")
    print("  `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe` already carried")
    print("  the bond product, its invariance under intra-nucleon reordering, AND the mechanism —")
    print("  'connected-sum multiplicativity ... does not care how each summand's word is")
    print("  internally ordered'. That is 'disjointness is not monotonicity' in other words.")
    print("\n  WHAT SURVIVES AS NEW, and it is the half that turns a ratio into an absolute:")
    print("  the corpus's bond model is about the RATIO tr(atom)/tr(free), which cancels the free")
    print("  word entirely. #6920 adds tr(free) = tr(p)^Z tr(n)^N with (a,r,q) measured on single")
    print("  nucleons, and only the two together give c0, c1, c2 — coefficients of the DIFFERENCE.")
    print("  (S_p,S_n) = 4(r_p,r_n) and (37,20) from q_p,q_n are downstream of that free half.")
    print("  Also new: the eps-SERIES form of the bond factors, and the A = 5 verification.")
    print("\n  WHY IT WAS MISSED: the bond model lives in a PRODUCER'S DOCSTRING and in probe")
    print("  filenames phrased as what they refute. A topic grep does not hit either. What would")
    print("  have: reading the docstring of the word builder every claim in this arc goes through.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
