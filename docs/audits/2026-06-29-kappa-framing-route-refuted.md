# `κ` is NOT a Markov framing exponent — formalize-first prune (2026-06-29)

**Branch:** `claude/kappa-framing-derivation-2026-06-29`. Owner opened the gated
`κ` derivation under STRICT constraints: **only CAL-1/2/3 (experimental ideal),
NO fitting**, `κ` an *output* not an input. **Discipline:** formalize-first
(prune the route before any numerics); the test is "residual isovector `b → 0`",
**never** "`b = −√3`" (that would reproduce the error). **Result: the
framing-exponent route is refuted.** `κ` is not a normalization constant.

## The hypothesis (and why it was plausible)

The synthesis (#3114) found the residual `log_{q₀}Δ_λ` has a **constant**
isovector coefficient `b ≈ −1.747` (A=6–12), with `κ = b/4 ≈ −0.437` the
per-writhe coefficient. Proposed route: the writhe `σ−σ⁻¹` enters the binding
only through a Jones–Markov **framing factor** `(framing)^{−writhe}`, so `κ`
would be that framing exponent — a categorical constant derivable from the Hecke
`σ` eigenvalues `q, −q⁻¹`, no fit.

## The structural fact that refutes it

The canonical binding is `B_pred = E₀·(tr_M(W_free) − tr_M(W_atom))` with the
Jones–Markov trace `tr_M` (`computations/markov/markov_trace_canonical.py`,
`z = 1/(q^{1/2}+q^{-1/2})`). Crucially, the atom braid word is fed to `tr_M` as a
product of **Hecke elements** `c·σ_g + d·I`, with the crossing type carried
**entirely by `d`**:

| crossing | `(c, d)` | reason |
|---|---|---|
| `σ` (positive) | `(1, 0)` | the generator |
| `σ⁻¹` (negative) | `(1, −h)` | `σ⁻¹ = σ − h` (Hecke relation `σ² = hσ + 1`) |
| color-averaged p-n | `(1, −h(½−δ/4))` | bar-symmetric |

So the writhe (the `σ` vs `σ⁻¹` asymmetry) is **already inside the Hecke
element**, and `tr_M` evaluates its trace **exactly in `q`**. There is **no
separate framing normalization applied** (grep: no `framing`/`writhe`/
`reidemeister` term in the trace or binding code), and **none is missing** — the
regular-isotopy `tr_M` of the explicit `(c,d)` element already carries the full
writhe-dependence. There is no free framing exponent to identify with `κ`.

**Empirical confirmation.** If `tr_M` were writhe-blind (so the writhe lived only
in a missing framing factor), `B_pred` would be the same for a mirror pair at
fixed `A`. It is not: `B_pred(³He) = 0.6581 ≠ B_pred(³H) = 0.6290` — `tr_M`
already produces a `T₃`-dependent prediction. The residual `b` is the **mismatch
between that exact categorical isovector content and the physical one**, not an
un-applied normalization.

## Verdict (scope-(a), cited)

- **The framing-exponent route for `κ` is REFUTED.** Structural invariant: the
  canonical `tr_M` is an *exact* trace of the explicit `c·σ + d·I` element, with
  the writhe fully encoded in `d = −h`; there is no normalization degree of
  freedom. `κ` is therefore **not** a Markov framing constant (and the `√3/4` /
  `7/16` coincidences remain numerology, doubly so now — they would tune a
  non-existent knob).
- **What `b ≈ −1.747` actually is:** a *completeness gap* of the model
  `B_pred = E₀·(tr_M_free − tr_M_atom)` — its isovector (charge-asymmetry)
  content is exactly computed but **physically incomplete**. Closing it is the
  full **Δ_λ closure** (augment the categorical model so its exact isovector
  output matches physics), which the corpus gates as research-grade and which
  **cannot** be done by tuning a framing exponent or fitting `b` (CAL-1/2/3 only,
  no fit).

## Consequence

`κ` is **not derivable as a framing/normalization shortcut** — that route is
closed. A legitimate derivation requires a *structurally augmented* categorical
binding model whose exact trace already yields the right isovector content (then
`b → 0`, no residual to "explain"). **No fit; no CAL-4; not wired.**

## The live route — Bring surface + chirality (owner-directed)

Framing is refuted, but the residual's isovector part is exactly **chiral**
content, and the corpus already homes it (corpus-grep, not a new construction):

- **`QOU.WedderburnMass.chirality_residue_mass_term`** decomposes the categorical
  mass per GB-filtration stratum as `mass_stratum s = mass_achiral s +
  mass_chiral s` — an **achiral (mirror-symmetric) + chiral (residue)** split.
  This **is** the binding residual's bar-even/bar-odd (isoscalar/isovector)
  split: `a(A)` is the achiral part, and the **writhe `b·T₃` term IS the
  `mass_chiral` residue.** The IMME parity algebra (#3104 `imme_mirror_diff`) is
  the mirror-involution shadow of this achiral/chiral decomposition.
- **`brings-surface/archimedean-chirality.md`** gives chirality its categorical
  origin: the **Reeb involution `ξ ↦ −ξ`** on the CR manifold, with chirality the
  `±`-eigenspaces (fermions sign-definite, bosons chirality-blind). The bar-odd
  writhe is precisely the Reeb-odd content.
- **The Bring surface supplies the chiral datum:** the A₅ **Galois `√5 ↦ −√5`
  twist** (`KeystoneFiveFoldStructure`, `IcosahedralCharacterGoldenRatio`,
  `KeystoneCanonicalAngleMap`) — the framework's "5-fold chirality" swapping the
  `T₁ ↔ T₂` irreps — is the categorical chirality the Reeb residue evaluates.

**Reframed `κ` (derive-or-refute, no fit).** `κ` is the **chiral-residue
coefficient** of `mass_chiral` — the per-writhe weight of the Reeb-odd /
Bring-A₅-chiral part of the binding. It is therefore the *binding-side* of the
**keystone residual-(i)** program (the `W_λ` Plancherel/Verlinde-measure work,
active on `main`: `BWVacuumRowIsHecke`, the Verlinde S-matrix reduction), seen
through the Reeb-chirality / Galois-`√5` lens rather than framing. The test
stays **`residual b → 0`** once the chiral residue is correctly derived from the
Bring A₅ datum — **never** `b = −√3` (that reproduces the error and tunes a
chiral knob to data, which the gate forbids).

**Status.** Route reclassified: framing **out**, Bring-A₅-chirality / `mass_chiral`
**in** — and it is the *same* gated keystone derivation, not a separable
shortcut. Next concrete step (gated, no fit): express the binding's `mass_chiral`
residue through the Bring A₅ Galois-chirality datum and test whether it drives
the isovector residual to zero. **No fit; CAL-1/2/3 only; not wired.**
