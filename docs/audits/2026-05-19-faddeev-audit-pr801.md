# Faddeev Φ_q audit on PR #801

**Date**: 2026-05-19
**Question**: Are any of PR #801's scripts using Faddeev Φ_q (which gives the
−737 MeV mirror-nucleus pathology per `prop:mass-endomorphism-tower` SUPERSEDED banner)?

## Audit result on PR #801 scripts (11 scripts, all clean)

| script | uses Li_2^q | calls Φ_q | imports _phi_q_util |
|---|:-:|:-:|:-:|
| `binding_via_interface_knot.py` | ✓ | — | — |
| `binding_block_multiplicative.py` | ✓ | — | — |
| `binding_depth_stratified.py` | — | — | — |
| `binding_depth_stratified_rust.py` | — | — | — |
| `binding_depth_stratified_lr.py` | — | — | — |
| `binding_depth_stratified_knot_weighted.py` | — | — | — |
| `binding_depth_stratified_selfconj.py` | — | — | — |
| `compute_atom_chi_rust.py` | — | — | — |
| `log_delta_categorical_derivation.py` | — | — | — |
| `log_delta_full_mass_subtract.py` | — | — | — |
| `log_delta_per_depth_binding.py` | — | — | — |

ALL 11 scripts on PR #801 are clean of Faddeev. The two that use a q-dilog
(`binding_via_interface_knot.py`, `binding_block_multiplicative.py`) use
**symmetric `li_2_q`** via `_li_2_q_util.py`. The depth-stratified variants
use direct `log|χ · dim_q|` without q-dilog calls. The Rust kernel wrapper
uses Hoefsmit seminormal character (no q-dilog).

## Upstream / downstream of Faddeev (broader repo state)

**Upstream (defines Faddeev)**:
- `_phi_q_util.py` (Faddeev infrastructure)
- `mass_endomorphism.py:Phi_q` (legacy mass-tower form, gives m_p/m_e ≈ 1870)

**Downstream (consumes Faddeev)**: 46 scripts including:
- `paper_six_term_isotope_sweep.py`, `mass_formula_6term*.py` — production mass-table chain
- `canonical_tower.py`, `canonical_plus_multibrane.py` — canonical-derivation
- `adjacent_vs_full_probe.py`, `brane_tower_*.py` — probe scripts
- `derived_masses.py`, `hydrogen_step_by_step.py`, etc.

## Conclusion for PR #801

**PR #801 is clean.** No Faddeev usage in my work. Already aligned with the
SUPERSEDED banner direction.

## Scope-out: broader Faddeev deprecation

Replacing Faddeev → symmetric Li_2^q in the 46 downstream scripts is a
substantial audit (would change m_p/m_e prediction in `mass_endomorphism.py`
and propagate through downstream mass-table outputs). This is tracked as a
**separate audit branch** (`claude/faddeev-deprecation-sweep`), out of scope
for PR #801.

The structural rationale for full deprecation:
- Faddeev Φ_q has convergence radius |z| < q ≈ 1.11 → diverges for atomic
  pair products in H_{3A>3}
- Faddeev gives −737 MeV mirror-nucleus pathology on ³He
- Symmetric Li_2^q has wider convergence and avoids the pathology

Estimated scope: ~200 lines across 46 scripts + verification of m_p/m_e under
symmetric Li_2^q (may shift from 1870 to a different number; numerical
not structural concern).
