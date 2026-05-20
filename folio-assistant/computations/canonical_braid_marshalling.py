"""
canonical_braid_marshalling.py — shared utility for marshalling
canonical atomic-braid words to the q-character compute format.

Centralises the (c, d, gen_idx) → (sign, gen_1indexed) and
(c, d, gen_idx) → (gen_0idx, cross_type) marshalling logic that
was previously duplicated across:

  - constit_factor_varying_q_phase5k2.py
  - rho_constit_equals_tau_M_proton_phase5l.py
  - tau_M_proton_closed_form_phase5l1.py
  - delta_lambda_fr_identity_phase5c.py
  - ... (about a dozen others)

Per Gemini PR #854 review:
  "The logic for marshalling the braid word and mapping Hecke
   coefficients to generator types is duplicated across several
   scripts.  This should be centralized in a shared utility module
   to maintain consistency and reduce code duplication."

The canonical f64-word format from `atom_braid_word_3A` is a list
of `(c, d, gen_idx)` triples where:
  - (c=1, d=0)    → positive σ      ("sigma")
  - (c=1, d=-h)   → negative σ⁻¹    ("sigma_inv")   where h = q_0 - q_0⁻¹
  - (c=1, d=-h/2) → averaged σ      ("averaged")  → σ convention (PR #819)

Two consumer formats are needed:
  1. `chi_lambda_braid` expects `[(sign, gen_1based), ...]` where
     sign ∈ {+1, -1} and averaged → +1 by convention.
  2. `q_character_on_braid_word` (symbolic) expects
     `[(gen_0idx, cross_type), ...]` where cross_type is the string.

This module exports both marshalling helpers.

  Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l)
  Ref: prop:interface-knot-markov-z.md (Phase 5c.1 — z, z-h convention)
"""
from __future__ import annotations

from typing import Iterable, List, Tuple


def marshal_to_chi_lambda_braid(
    word_tuples: Iterable[Tuple[float, float, int]],
    h_val: float,
    *,
    eps: float = 1e-10,
) -> List[Tuple[int, int]]:
    """Marshal `[(c, d, gen_0idx), ...]` → `[(sign, gen_1idx), ...]`.

    For `hecke_characters.chi_lambda_braid` (f64 fast path + mpfr path).

    Conventions per PR #819 + Phase 5c.1:
      - (c=1, d=0)        → sign=+1 (positive σ)
      - (c=1, d=-h)       → sign=-1 (negative σ⁻¹, Hecke skein)
      - (c=1, d=-h/2)     → sign=+1 (averaged → σ convention)
      - other             → sign=+1 (fallback; shouldn't occur in canonical
                            braids)

    Args:
        word_tuples: iterable of (c, d, gen_0idx) triples
        h_val: substrate value of h = q - q⁻¹ used to BUILD the word
          (typically `float(Q_F64 - 1/Q_F64)` from `q_parameter`)
        eps: tolerance for matching d-coefficients

    Returns:
        list of (sign, gen_1based) pairs suitable for chi_lambda_braid
    """
    out: List[Tuple[int, int]] = []
    for c, d, gen in word_tuples:
        cf, df = float(c), float(d)
        if abs(cf - 1.0) >= eps:
            raise ValueError(f"unexpected c={cf} in canonical braid (expected c=1)")
        if abs(df) < eps:
            out.append((1, gen + 1))            # σ (positive crossing)
        elif abs(df + h_val) < eps:
            out.append((-1, gen + 1))           # σ⁻¹ (Hecke skein)
        elif abs(df + h_val / 2) < eps:
            out.append((1, gen + 1))            # averaged → σ convention
        else:
            out.append((1, gen + 1))            # fallback
    return out


def marshal_to_symbolic_braid(
    word_tuples: Iterable[Tuple[float, float, int]],
    h_val: float,
    *,
    eps: float = 1e-10,
) -> List[Tuple[int, str]]:
    """Marshal `[(c, d, gen_0idx), ...]` → `[(gen_0idx, cross_type), ...]`.

    For `hecke_character_symbolic.q_character_on_braid_word`.

    cross_type ∈ {"sigma", "sigma_inv", "averaged"}, with same convention
    as `marshal_to_chi_lambda_braid`.

    Args:
        word_tuples: iterable of (c, d, gen_0idx) triples
        h_val: substrate value of h = q - q⁻¹ used to BUILD the word
        eps: tolerance for matching d-coefficients

    Returns:
        list of (gen_0idx, cross_type) pairs suitable for
        q_character_on_braid_word
    """
    out: List[Tuple[int, str]] = []
    for c, d, gen in word_tuples:
        cf, df = float(c), float(d)
        if abs(cf - 1.0) >= eps:
            raise ValueError(f"unexpected c={cf} in canonical braid (expected c=1)")
        if abs(df) < eps:
            out.append((gen, "sigma"))
        elif abs(df + h_val) < eps:
            out.append((gen, "sigma_inv"))
        elif abs(df + h_val / 2) < eps:
            out.append((gen, "averaged"))
        else:
            out.append((gen, "sigma"))          # fallback
    return out
