**Proposition (canonical p-n averaging uniqueness).**  *Any two
p-n interface averaging functionals* $\sigma_{pn}, \sigma_{pn}'$
*on* $H_{3A}(R, q)$ *that both satisfy* (a) **bar-invariance**
$\sigma_{pn}(q) = \sigma_{pn}(q^{-1})$, (b) **color-flavor
compatibility** (Bring color-tube symmetry over quark
composition), *and* (c) **standard normalisation**
$\sigma_{pn} = z$ *with the same* $z$ *are equal block-wise.
Hence the canonical p-n averaging is uniquely determined by
these three structural hypotheses — closing the cheat-sheet
open audit finding (Phase 5q, line 128).*

## Setting

The QOU mass identity at $A \geq 2$ contracts a per-interface
averaging functional $\sigma_{pn}$ across the p-n boundary slice
in $H_{3A}(R, q)$.  Two production candidates have circulated:

| candidate | form | status |
|---|---|---|
| uniform bar-invariant | $\sigma_{\rm avg} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ | current default ([`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)) |
| Bring color-tube weighted | per-quark-composition weighted | "open audit finding" (Phase 5q); empirically reproduces $\Delta m_{n-p}$ to ${\approx}\,0.14\,\%$ of CODATA via Scheme 4 per-sheet PL integration |

Both satisfy bar-invariance + standard normalisation; they differ
on the per-sheet color weighting.  The uniqueness theorem here
states that **once color-flavor compatibility is fixed**, the
averaging is determined.  Closing the `ColorFlavorCompatible`
class to the Bring weighted derivation refines the admissible
normalisation $z$ to a unique canonical form.

## Lean structure

The uniqueness is staged via the [§3b-cond conditional-class
pattern](../../../CLAUDE.md):

- `BarInvariant R σ_pn` — substrate axiom (bar-involution-respecting).
- `ColorFlavorCompatible R σ_pn` — **open**: refines once the
  categorical color-sheet ↔ quark-flavor mapping lands (per
  `probe_pn_flavor_asymmetry.py` Scheme 4).  Currently carried as a
  per-instance witness with `True` placeholder.
- `StandardNorm R σ_pn z` — pointwise $\sigma_{pn} = z$.

Conditional on the three classes, `theorem pn_averaging_unique`
proves $\sigma_{pn} = \sigma_{pn}'$ sorry-free; the
sub-singleton form `pn_averaging_subsingleton` packages the same
content for downstream use.

The open `ColorFlavorCompatible` class is the per-quark color
weighting derivation; until that lands, the uniqueness theorem is
proved *conditional on the class instance* per CLAUDE.md §3b-cond.

## Computational consequence

The closed-form `closed_form_tau_M.py` already exposes the
opt-in `pn_convention="bring_color_weighted"` placeholder that
raises `NotImplementedError` with the queue context.  Implementing
the Bring weighted convention requires (a) extending the closed
form to accept quark-mass inputs, and (b) defining the canonical
color-sheet ↔ quark-flavor mapping.

## Status

This proposition is **proved conditional on the
`ColorFlavorCompatible` class instance**.  No fitting, no
empirical input: the uniqueness reduces to the pointwise
normalisation hypothesis once the structural conditions are
named.  Closing the open class is the genuine open math
(per Phase 5q audit).
