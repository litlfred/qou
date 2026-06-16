# Borromean axial-coupling fix

Date: 2026-05-07

Restored `/home/runner/work/qou/qou/computations/borromean-axial-coupling.py` from `_deprecated/` and fixed the core bug.

## Bug

The deprecated script used

$$
\beta \cdot \sigma_1 \cdot \beta^{-1}.
$$

Any trace-like observable of that expression is cyclic-trivial:

$$
\mathrm{tr}(\beta \sigma_1 \beta^{-1}) = \mathrm{tr}(\sigma_1).
$$

So the old "Borromean suppression" was forced to be `1` identically.

## Fix

The restored script keeps that identity as an explicit diagnostic, then switches to the non-conjugate probe

$$
\beta \cdot \sigma_1.
$$

This is sensitive to the Borromean word and therefore no longer collapses by cyclicity.

## Current status

- cyclic diagnostic: still exactly trivial, as expected.
- direct `β·σ₁` probe: nontrivial.
- probe value: `g_A ≈ 1.3186` from `(5/3) · |tr_std(βσ₁) / tr_triv(βσ₁)|`.

This is an **audit-only probe**, not the final bound-state observable.  The principled observable should use the `G^{-1}` + LP-active-set formula rather than a raw trace ratio.
