#!/usr/bin/env python3
# polynomial_q_not_applicable: pure integer combinatorics on
# nucleon orderings; no q-polynomial arithmetic.
"""Canonical-braid interface composition utility.

Layer 2 of the substrate-derivation infrastructure (see
`def:canonical-braid-interface-composition`).  Provides:

  - `interface_composition(Z, N, ordering='pppnnn')` →
    `(n_pp, n_pn, n_nn)` tuple
  - `interface_composition_from_word(word)` → same tuple, derived
    from a `atom_braid_word_3A`-style word
  - `pppnnn_ordering(Z, N)` → list of 'p'/'n' strings
  - `ATOM_TABLE` → known atoms with (Z, N) tuples

Used by:
  - `probe_interface_composition_sweep.py` (Layer 3, this PR)
  - downstream Δ_coupling residual analyses

Witness: `canonical-braid-interface-composition.witness.json`
(emitted by the sweep probe, not this utility).

@module computations/interface_composition
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from typing import Iterable, Literal

Nucleon = Literal["p", "n"]


# Known atoms (Z, N).  Extended beyond the {D, T, ³He, ⁴He}
# magic-shell empirical bench to give richer (n_pp, n_pn, n_nn)
# coverage for fitting α, β, γ.
ATOM_TABLE: dict[str, tuple[int, int]] = {
    "D":   (1, 1),
    "T":   (1, 2),
    "3He": (2, 1),
    "4He": (2, 2),
    "5Li": (3, 2),
    "6He": (2, 4),
    "6Li": (3, 3),
    "6Be": (4, 2),
    "7Li": (3, 4),
    "7Be": (4, 3),
    "8Be": (4, 4),
    "8Li": (3, 5),
    "8B":  (5, 3),
    "9Be": (4, 5),
    "9B":  (5, 4),
    "10B": (5, 5),
    "12C": (6, 6),
    "14N": (7, 7),
    "16O": (8, 8),
}


def pppnnn_ordering(Z: int, N: int) -> list[Nucleon]:
    """Canonical 'all protons first, then all neutrons' ordering."""
    return ["p"] * Z + ["n"] * N


def alternating_ordering(Z: int, N: int) -> list[Nucleon]:
    """Alternating proton/neutron ordering (excess at end)."""
    pairs = min(Z, N)
    out: list[Nucleon] = []
    for _ in range(pairs):
        out.extend(["p", "n"])
    out.extend(["p"] * (Z - pairs))
    out.extend(["n"] * (N - pairs))
    return out


def interface_composition(
    Z: int, N: int, *, ordering: str = "pppnnn"
) -> tuple[int, int, int]:
    """Return `(n_pp, n_pn, n_nn)` for the given ordering.

    Ordering names:
      'pppnnn' — canonical (all protons first)
      'alternating' — proton/neutron alternation
      'custom' — pass `nucleon_list` directly (not via this signature)

    Closed-form for pppnnn:
        n_pp = max(0, Z - 1)
        n_nn = max(0, N - 1)
        n_pn = 1 if Z >= 1 and N >= 1 else 0
    """
    if ordering == "pppnnn":
        # Closed form is faster + matches the canonical convention.
        return (
            max(0, Z - 1),
            1 if (Z >= 1 and N >= 1) else 0,
            max(0, N - 1),
        )
    if ordering == "alternating":
        nucs = alternating_ordering(Z, N)
    else:
        raise ValueError(f"Unknown ordering: {ordering!r}")
    return interface_composition_from_ordering(nucs)


def interface_composition_from_ordering(
    nucleons: Iterable[Nucleon],
) -> tuple[int, int, int]:
    """Count interface types from an explicit nucleon ordering."""
    nucs = list(nucleons)
    n_pp = n_pn = n_nn = 0
    for k in range(len(nucs) - 1):
        a, b = nucs[k], nucs[k + 1]
        if a == "p" and b == "p":
            n_pp += 1
        elif a == "n" and b == "n":
            n_nn += 1
        else:
            n_pn += 1
    return (n_pp, n_pn, n_nn)


def _pn_color_weighted(h_val: float) -> float:
    """The Bring color-weighted pn interface, `-h(1 - δ/2)/2`.

    δ is DERIVED from `_li_2_q_util.flavor_split_leading`, not hardcoded, so
    this cannot drift from the word builder. On failure it returns the uniform
    average, leaving the caller's behaviour unchanged rather than silently
    admitting an unrelated value.
    """
    try:
        import mpmath as mp
        from _li_2_q_util import flavor_split_leading
        from q_parameter import Q_50_DIGIT_STR, Q_MP
        # This classifier is float BY SIGNATURE (`h_val: float`) and tags
        # letters with `abs(d - x) < 1e-9`. delta ~ 1.4e-3 shifts the pn value
        # by 7e-5, eight orders above that window, so double is ample. No
        # physical quantity is computed here -- only which of four letter
        # types a junction is.
        with mp.workdps(50):
            delta = float(flavor_split_leading(Q_MP))  # float64-ok: letter-type tag, 1e-9 window, no physics
    except Exception:
        return -h_val / 2
    return -h_val * (1 - delta / 2) / 2


def interface_composition_from_word(
    word: list[tuple[float, float, int]],
    *,
    h_val: float | None = None,
) -> tuple[int, int, int]:
    """Derive (n_pp, n_pn, n_nn) from a canonical braid word.

    Inspects the `(c, d, gen_idx)` triples at inter-nucleon
    positions `gen_idx = 3k + 2` and classifies by the d value:
      d = 0                → pp interface (σ)
      d = -h/2             → pn, UNIFORM average (Δ_I)
      d = -h(1 - δ/2)/2    → pn, BRING COLOR-WEIGHTED  ← production default
      d = -h               → nn interface (σ⁻¹)

    Both pn spellings are accepted and counted as pn. The color-weighted one
    was added 2026-09-06 (`qou-hu1f`): `atom_braid_word_3A` defaults to
    `pn_convention="bring_color_weighted"`, emitting `-h(1-δ/2)/2 =
    -0.104458…` against the uniform `-h/2 = -0.104530…`. This function
    accepted only the uniform value and so raised `Unrecognised interface d`
    on every production word. PRE-EXISTING, not a consequence of the
    intra-ordering ruling — measured failing under both orderings.

    `h_val` defaults to the canonical h = q_0 - q_0^{-1} ≈ 0.209.
    """
    if h_val is None:
        from hecke_core import h as h_module
        h_val = float(h_module)

    n_pp = n_pn = n_nn = 0
    for c, d, g in word:
        if g % 3 != 2:
            continue
        if abs(d) < 1e-9:
            n_pp += 1
        elif abs(d - (-h_val / 2)) < 1e-9:
            n_pn += 1                      # uniform average
        elif abs(d - _pn_color_weighted(h_val)) < 1e-9:
            n_pn += 1                      # Bring color-weighted (production)
        elif abs(d - (-h_val)) < 1e-9:
            n_nn += 1
        else:
            raise ValueError(
                f"Unrecognised interface d={d}; expected one of "
                f"{{0, -h/2={-h_val/2:.4f}, -h={-h_val:.4f}}}"
            )
    return (n_pp, n_pn, n_nn)


# Self-test on import — closed-form vs ordering-derived consistency.
def _selftest() -> None:
    for atom, (Z, N) in ATOM_TABLE.items():
        a = interface_composition(Z, N, ordering="pppnnn")
        b = interface_composition_from_ordering(pppnnn_ordering(Z, N))
        assert a == b, f"closed-form vs ordering mismatch for {atom}: {a} != {b}"


_selftest()


if __name__ == "__main__":
    print(f"{'atom':<6}{'(Z,N)':<8}{'n_pp':>5}{'n_pn':>5}{'n_nn':>5}"
          f"{'total':>7}")
    print("-" * 36)
    for atom, (Z, N) in ATOM_TABLE.items():
        comp = interface_composition(Z, N)
        print(f"{atom:<6}({Z},{N})    {comp[0]:>5}{comp[1]:>5}"
              f"{comp[2]:>5}{sum(comp):>7}")
