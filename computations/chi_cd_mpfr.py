"""chi_cd_mpfr — canonical-tier (MPFR) χ^λ for (c, d, gen) atomic words.

NO float64 on this path (owner ruling 2026-06-09: canonical = symbolic;
MPFR ≥ 50 dps is the speed fallback; f64 is preview/cross-check only).

The atomic braid word from `mass_at_3A_proper.atom_braid_word_3A` is a
list of `(c, d, gen0)` Hecke-crossing templates. `pyhecke_native`'s
canonical-tier character API (`chi_lambda_all_partitions_mpfr`) takes a
SIGNED braid word `[(sign, gen1)]` with `sign ∈ {+1, −1, 0}` (0 = the
averaged half-sum `(σ+σ⁻¹)/2 = σ − h/2`). We bridge the two by
LINEARITY of the character:

    σ        (c=1, d=0)      → +1 generator                  (1 term)
    σ⁻¹      (c=1, d=−h)     → −1 generator                  (1 term)
    averaged (c=1, d=−h/2)   → sign-0 crossing               (1 term)
    color-weighted p-n
      σ − h(½ − δ/4)·1       → [sign-0] + (h·δ/4)·1          (2 terms)

The color-weighted identity-term coefficient `h·δ/4` is rebuilt here at
full 50-dps from `flavor_split_subleading(q₀)` — the float `d` carried
by the word builder has only ~17 significant digits and would silently
cap any consumer at f64 precision otherwise.

`χ^λ(word) = Σ_terms coeff · χ^λ(braid_term)`, each term evaluated by
the native MPFR kernel and combined with `mpmath.mpf` coefficients.
"""
from __future__ import annotations

import mpmath as mp
import pyhecke_native as _pn

from q_parameter import Q_50_DIGIT_STR

_TOL = 1e-9


def to_braid_terms(
    word: list[tuple[float, float, int]], *, dps: int = 50
) -> list[tuple["mp.mpf", list[tuple[int, int]]]]:
    """Map a `(c, d, gen0)` word to `[(coeff_mpf, [(sign, gen1)])]`.

    Each `gen0` is 0-indexed (word-builder convention); the emitted
    braid words are 1-indexed (native-kernel convention). Raises on any
    crossing template that is not σ / σ⁻¹ / averaged / color-weighted-pn
    so convention drift fails loudly.
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    h_f = float(h)
    terms: list[tuple[mp.mpf, list[tuple[int, int]]]] = [(mp.mpf(1), [])]
    delta = None  # lazy — only the color-weighted branch needs it
    for c, d, g in word:
        cf, df = float(c), float(d)
        if abs(cf - 1.0) > _TOL:
            raise ValueError(
                f"chi_cd_mpfr: unsupported crossing c={c} at gen={g} "
                "(expected c=1 templates)"
            )
        if abs(df) < _TOL:
            terms = [(co, w + [(1, g + 1)]) for co, w in terms]
        elif abs(df + h_f) < _TOL:
            terms = [(co, w + [(-1, g + 1)]) for co, w in terms]
        elif abs(df + h_f / 2) < _TOL:
            terms = [(co, w + [(0, g + 1)]) for co, w in terms]
        else:
            if delta is None:
                from _li_2_q_util import flavor_split_subleading
                delta = flavor_split_subleading(q)
            expected_d = -(h * (mp.mpf("0.5") - delta / 4))
            if abs(df - float(expected_d)) > _TOL:
                raise ValueError(
                    f"chi_cd_mpfr: unrecognised crossing (c={c}, d={d}) at "
                    f"gen={g}; expected σ / σ⁻¹ / averaged / color-weighted pn"
                )
            id_coeff = h * delta / 4
            split: list[tuple[mp.mpf, list[tuple[int, int]]]] = []
            for co, w in terms:
                split.append((co, w + [(0, g + 1)]))   # sign-0 averaged branch
                split.append((co * id_coeff, w))        # identity branch
            terms = split
    return terms


def chi_all_partitions_cd_mpfr(
    n_strands: int,
    word: list[tuple[float, float, int]],
    *,
    dps: int = 50,
) -> dict[tuple[int, ...], "mp.mpf"]:
    """`{partition: χ^λ}` (mpf) at MPFR `dps` for the (c,d,gen) `word`.

    Routes through `pyhecke_native.chi_lambda_all_partitions_mpfr` (the
    canonical-tier kernel) once per linearity term and accumulates with
    mpf coefficients. Returns mpf values (caller serialises via
    `mpmath.nstr` / `str`).
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    terms = to_braid_terms(word, dps=dps)
    acc: dict[tuple[int, ...], mp.mpf] = {}
    for coeff, braid in terms:
        for shape, chi_str in _pn.chi_lambda_all_partitions_mpfr(
            n_strands, braid, Q_50_DIGIT_STR, dps
        ):
            key = tuple(shape)
            acc[key] = acc.get(key, mp.mpf(0)) + coeff * mp.mpf(chi_str)
    return acc
