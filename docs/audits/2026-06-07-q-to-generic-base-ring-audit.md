# ℚ → generic base-ring generalization audit (QOU Lean)

**Date:** 2026-06-07
**Branch / PR:** `claude/eager-darwin-PqAjM` (PR #1974)
**Trigger:** Owner request — "restate `chi21_borromean_qform` over `q : Rˣ`
(Laurent units) instead of ℚ … do this for as many Lean progs w/ ℚ as
possible. maybe need an audit param … 'over a field' or so."

## Mechanism — reuse the canonical `wall-base-ring-minimal` criterion

The "audit param 'over a field'" the owner asked for **already exists** as a
first-class QA criterion: [`wall-base-ring-minimal`](../../content/pipeline/qa-criteria-registry.ts)
(checker `checkBaseRingMinimal` in
[`content/pipeline/qa-checkers-voice.ts`](../../content/pipeline/qa-checkers-voice.ts),
landed on `main` in `d7f3e4a9`, concurrent with this PR). It is the
algebraic-side companion to `wall-side-correct` (§7c) and flags, per block:

* algebraic-side Lean (no archimedean ℝ markers) carrying **`[Field R]` /
  `ℚ` / `DivisionRing` / `field_simp`**, or a ring-element **`⁻¹`** — as a
  candidate for a division-free restatement over `ℤ[q, q⁻¹]`
  (`LaurentPolynomial ℤ`) / `CommRing`;
* it deliberately treats a **Units coercion `↑q⁻¹`** (over a `CommRing`,
  `q : Rˣ`) as the *target* pattern — i.e. the fixed form, not a hit.

Run it via the standard QA sweep (warn-only, advisory):

```
bun run content/pipeline/qa-sweep.ts <block-path> --only wall-base-ring-minimal
```

This audit deliberately adds **no** standalone scanner (§2a reuse
discipline — a second Python re-implementation of the same heuristic would
only drift from `checkBaseRingMinimal`). The mechanism is the canonical
criterion; this doc supplies the part the automated WARN cannot — the
**per-candidate human adjudication** ("is a field essential, or is this a
Laurent identity?").

## Adjudication (the value the WARN defers to a human)

Scanning the 42 ℚ-typed QOU Lean declarations, classified by what the body
actually uses:

| Class | Trigger | Verdict |
|-------|---------|---------|
| ring | only `+ − * ^` | generalize → `{R} [CommRing R]` |
| field | *variable* division `1/q`, no ordering / `Real.*` / numeric literal | candidate → `[Field R]` or `(q : Rˣ)` |
| numeric | concrete rational literal `p/q` (e.g. `17/4`, `−3/4`) | **keep ℚ** — a *value*, not an identity |
| archimedean | `Real.*`, ordering `≤ < ≥ >`, `sqrt`, `rpow`, transcendence, CODATA decimal | **keep ℝ/ℚ** |

Counts: **1 ring · 15 field · 15 numeric (keep) · 11 archimedean (keep)**.

### Acted on

- **`chi21_borromean_qform`** (`BorromeanChiPerRep.lean`) — the form
  `wall-base-ring-minimal` explicitly names as the WARN this PR fixes. The
  genuinely fibre-level forms now live over `{R} [CommRing R]`:
  - `chi21_borromean (h : R)` — the `R[h]` character `2 − 3h⁴ − h⁶`
    (+ `chi21_borromean_even`);
  - **`chi21_borromean_qform_unit (q : Rˣ)`** — the q-rational form
    `num(q)·(q⁻¹)⁶` over a **unit** of any `CommRing`, reaching
    `LaurentPolynomial ℤ` (`q = T`, **not** a field element), with bridges
    `chi21_borromean_qform_unit_eq_poly` and `…_bar_invariant`;
  - **`TUnit : (LaurentPolynomial ℤ)ˣ`** (`q = T`, inverse `T(-1)`) +
    `chi21_borromean_qform_unit_laurent` — a concrete `ℤ[q, q⁻¹]` witness
    that the `Rˣ` layer is **not vacuous over a non-field**.

  The pre-existing `[Field R]` `chi21_borromean_qform`/`hform` API is **kept**
  (consumed by `Machinery/DerivedCharacterCatalogue.lean`); the `Rˣ` form is
  added alongside as the strictly-more-general companion.

### Reviewed — intentionally kept (NOT actionable)

The remaining `field` rows are not clean wins:

| Decl(s) | File | Why kept |
|---------|------|----------|
| `trM_borromean`, `Q_borromean`, `…_isTrace`, `…_bar_invariant` | `BorromeanMarkovTrace.lean` | **Deliberate** ℚ-shadow: the `R[h]` core (`IsBorromeanMarkovTrace`, `borromean_markov_trace_closed_form_mul`) is already generic; only the genuine quotient + positivity stay over ℚ. |
| `chi21_borromean_qform`, `…_hform`, `…_eq_hform`, `…_hform_bar_invariant` | `BorromeanChiPerRep.lean` | Field/division shadow over `[Field R]`; consumed by `DerivedCharacterCatalogue`. The fibre content is the `R[h]` + `Rˣ` forms above. |
| `qbeta_c3_squared`, `qbeta_c3_cubed`, `qbeta_c10_at_silver` | `QBetaCnAtSilver.lean` | Values **at the silver ratio** — ℚ-specific (variable bound to a fixed algebraic number). |
| `halfSymTotalDim`, `halfSymTrivialS3`, `effectiveCellCount` | `S4S3HalfSymmetricProjection.lean` | Specific S₄/S₃ dimension-count ratios. |
| `gonshor` | `SignSequence.lean` | Surreal sign-sequence construction. |

The 15 `numeric` (Plancherel weights, silver-ratio `c_k`) and 11
`archimedean` (CODATA, positivity, Hoefsmit dyadics) rows are correct ℚ/ℝ
specialisations.

## Finding

Beyond the `chi21_borromean_qform` Laurent-unit restatement (the exact case
`wall-base-ring-minimal` flags), QOU's Lean corpus has **no further clean
ℚ → generic wins**: the ℚ uses are overwhelmingly intentional archimedean
shadows already split from a generic `R[h]` core, or genuinely ℚ-specific
numeric facts. The automated wall remains armed in the pipeline for new Lean.

## Limitation (input to the wall)

The wall's `[Field R]`/`⁻¹` markers flag *variable division* but cannot tell
whether the divided variable is bound to a concrete algebraic number
downstream (the `*_at_silver` / `halfSym*` cases) — those are the `numeric`
class here and need the one-line human verdict the wall already requests
("adjudicate: is a field essential, or is this a Laurent identity?").
