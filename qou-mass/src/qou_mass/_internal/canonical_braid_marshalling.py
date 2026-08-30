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

## Audit (Phase 5q, 2026-05-20): averaging convention

The "averaged" form (c=1, d=-h/2) represents the UNIFORM bar-invariant
projection σ_avg = (σ + σ^{-1})/2 = σ - h/2·I.  This is the convention
the canonical builder `mass_at_3A_proper.atom_braid_word_3A` produces
for p-n boundaries.  Per `prop:averaging-resonance-rule`, this is the
categorically-defined "averaged" Hecke generator.

The owner's intuition (recorded in `probe_pn_flavor_asymmetry.py` and
`probe_per_sheet_flavor_nonin.py`) is that the canonical p-n averaging
should be **Bring color-tube weighted** — i.e. account for the 3 quark
color sheets per nucleon (uud vs udd) rather than treating p-n as
flavor-symmetric.  Empirically the sum-weighted scheme reproduces
Δm_{n-p} to ~0.14% of CODATA (`probe_pn_flavor_asymmetry.py` Scheme 4).

**At the marshalling level here** (H_n algebraic, no quark-mass info),
the current convention is preserved.  See `closed_form_tau_M.py` for
the open `pn_convention="bring_color_weighted"` placeholder and the
queued research item.

  Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l)
  Ref: prop:interface-knot-markov-z.md (Phase 5c.1 — z, z-h convention)
  Ref: prop:averaging-resonance-rule.md (categorical σ_avg = σ - h/2)
  Ref: probe_pn_flavor_asymmetry.py (Bring color-tube weighted averaging probe)
  Ref: docs/canonical-derivation-cheat-sheet.md (audit finding)
"""
from __future__ import annotations

from typing import Iterable, List, Tuple

from canonical_braid_crossings import _avg_color_delta  # color-weighted averaged d



def _pn_delta():
    """Colour-weighting delta for the p-n interface (qou-gdtb)."""
    from canonical_braid_crossings import _avg_color_delta
    return _avg_color_delta()

def marshal_to_chi_lambda_braid(
    word_tuples: Iterable[Tuple[float, float, int]],
    h_val: float,
    *,
    eps: float = 1e-10,
) -> List[Tuple[int, int]]:
    """Marshal `[(c, d, gen_0idx), ...]` → `[(sign, gen_1idx), ...]`.

    For `hecke_characters.chi_lambda_braid` (f64 fast path + mpfr path).

    Conventions per PR #819 + Phase 5c.1:
      - sigma             → sign=+1 (positive σ)
      - sigma_inv         → sign=-1 (negative σ⁻¹, Hecke skein)
      - averaged          → sign=+1 (averaged → σ convention)
      - averaged_weighted → sign=+1 (same channel; see below)

    ⚠ This is **`chi_lambda_braid`'s** sign convention, in which averaged
    maps to `+1`. It is NOT the `{-1, 0, +1}` wire encoding of
    `canonical_braid_crossings.sign_for_ctype`, where averaged maps to `0`.
    Two different targets, deliberately not merged -- unifying them would
    silently change this path's numbers.

    Both averaged interfaces land in the σ channel: this marshaller emits
    signs and drops `d` entirely, so it cannot carry the p-n colour
    weighting `-h(1/2 - δ/4)` either way. Lossy, but equally lossy for both
    variants, which is why the collapse is correct *here* and was a defect
    in `marshal_to_symbolic_braid`, whose label feeds `d_for_ctype`.

    Args:
        word_tuples: iterable of (c, d, gen_0idx) triples
        h_val: substrate value of h = q - q⁻¹ used to BUILD the word
          (typically `float(Q_F64 - 1/Q_F64)` from `q_parameter`)
        eps: unused; retained for signature compatibility. Classification
          tolerances now live in `classify_crossing`, so the two marshallers
          cannot drift apart on tolerance the way they did on vocabulary.

    Returns:
        list of (sign, gen_1based) pairs suitable for chi_lambda_braid
    """
    from canonical_braid_crossings import classify_crossing
    # Explicit and total over CTYPES: a new ctype must be given a sign here
    # rather than falling through to a default. The private classifier this
    # replaces is how `averaged_weighted` went missing (qou-8zjd).
    _CHI_SIGN = {
        "sigma": 1, "sigma_inv": -1, "averaged": 1, "averaged_weighted": 1,
    }
    out: List[Tuple[int, int]] = []
    for c, d, gen in word_tuples:
        ctx = f"marshal_to_chi_lambda_braid gen={gen}"
        ctype = classify_crossing(float(c), float(d), h_val, context=ctx)
        if ctype not in _CHI_SIGN:
            raise ValueError(
                f"ctype {ctype!r} has no chi_lambda_braid sign convention; "
                f"add it to _CHI_SIGN in canonical_braid_marshalling"
            )
        out.append((_CHI_SIGN[ctype], gen + 1))
    return out


def marshal_to_symbolic_braid(
    word_tuples: Iterable[Tuple[float, float, int]],
    h_val: float,
    *,
    eps: float = 1e-10,
) -> List[Tuple[int, str]]:
    """Marshal `[(c, d, gen_0idx), ...]` → `[(gen_0idx, cross_type), ...]`.

    For `hecke_character_symbolic.q_character_on_braid_word`.

    `cross_type ∈ canonical_braid_crossings.CTYPES` -- the *full* vocabulary,
    including `averaged_weighted`. This used to be a private classifier that
    collapsed the colour-weighted p-n interface onto `"averaged"`; because
    the consumer resolves the label through `d_for_ctype`, that substituted
    `-h/2` for `-h(1/2 - δ/4)` and discarded the proton-neutron colour
    asymmetry at 6.88e-4 on one crossing in 23 (qou-gdtb, qou-8zjd).
    Classification is now delegated, so there is one vocabulary.

    Args:
        word_tuples: iterable of (c, d, gen_0idx) triples
        h_val: substrate value of h = q - q⁻¹ used to BUILD the word
        eps: unused; retained for signature compatibility. Tolerances live
          in `classify_crossing`.

    Returns:
        list of (gen_0idx, cross_type) pairs suitable for
        q_character_on_braid_word
    """
    from canonical_braid_crossings import classify_crossing
    out: List[Tuple[int, str]] = []
    for c, d, gen in word_tuples:
        ctx = f"marshal_to_symbolic_braid gen={gen}"
        out.append((gen, classify_crossing(
            float(c), float(d), h_val, context=ctx,
        )))
    return out
