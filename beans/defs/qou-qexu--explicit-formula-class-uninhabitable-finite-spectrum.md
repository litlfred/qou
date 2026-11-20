---
# qou-qexu
title: 'q-RH: QExplicitFormula is uninhabitable — proved for empty spectrum, general case open'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:30:00Z
updated_at: 2026-10-04T15:11:05Z
parent: qou-4fqg
---

`QExplicitFormula` (`q-geometric-langlands/explicit-formula.lean`) formalises
the q-explicit formula with the spectral side as a **finite** `List
ReebEigenvalue`. In that form it holds for **no** datum with an empty spectrum,
whatever its ideals, `Ω_q` and `q > 1`. Proved:
`not_qExplicitFormula_of_nil_spectrum`, `#print axioms` clean.

## Why the question got asked at all

`not_qExplicitFormula_empty` (already in the file) refutes exactly **one**
datum. That is weaker than it looks: a class refuted on one instance can still
be satisfiable on another, and a conditional theorem over it is only worthless
if **no** instance exists. Satisfiability is a separate question from
refutability-on-an-instance and has to be asked separately.

This is the same lesson as the `HasReebSpectralCoords` case on this branch, in
the negative direction — *"exhibit a witness of the thing the conditional
theorems actually depend on"*, and when you cannot, find out whether one can
exist. The sibling's `HasQPlancherelCLT` finding is the third instance in a
week.

## The mechanism

- `ψ_q(X)` sums over a **finite** `List MaxIdeal`, terms switched on and off by
  `N(𝔪) ≤ X`, never grown ⇒ bounded uniformly in `X` (`qChebyshev_abs_le`).
- `−½·ln_q(1 − X^{−2})` **→ +∞ as X → 1⁺** (`tail_term_unbounded`).

A bounded function cannot equal an unbounded one.

`tail_term_unbounded` is constructive, not a limit: `X := 1/√(1−ε)` makes
`1 − X^{−2} = ε` exactly, so `ε ≤ q^{−2B}` forces the term above `B`; capping
`ε ≤ 1/2` keeps `X ≤ √2`, which is what bounds the other side's `X` term.

## This is a formalisation defect, NOT a refutation of the mathematics

The classical explicit formula carries the *same* `−½log(1−x^{−2})` term and is
true. There the spectral sum runs over **infinitely many** zeros and converges
only conditionally: that term is the closed form of the trivial-zero series, and
its blow-up near `x = 1` is cancelled by the divergence of the non-trivial-zero
sum. A finite `List` cannot reproduce that cancellation.

**So a faithful carrier needs the spectral side to be an infinite sum with a
specified summation order.** That is the repair, and it is not cosmetic — the
summation order is part of the classical statement.

## What is still open (the reason this bean is in-progress, not completed)

The **general finite-spectrum** case: for a datum with a *nonempty* finite
spectrum, the same argument should apply, because on `X ∈ (1, √2]` the spectral
sum is a finite sum of terms `‖(X:ℂ)^ρ‖ = X^{Re ρ}` divided by fixed brackets,
hence bounded by a constant of the datum. Not proved here.

What it needs, concretely:

1. `‖(X:ℂ)^ρ‖ = X^{Re ρ}` for real `X > 0`. **This branch already has that
   lemma** — `abs_cpow_ofReal_eq_rpow_re` in `spectral-half-line.lean` — but it
   is a **content-block sibling**, outside the package globs, so
   `explicit-formula.lean` cannot import it (§0a). Same structural obstruction
   as `qou-sibdup`. Either move it to a library module (as `WeilZeta.lean` and
   `ReebSpectrum.lean` were) or re-prove it locally.
2. A per-element bound `X^{Re ρ} ≤ max 1 (√2 ^ Re ρ)` on `X ∈ (1, √2]`.
3. The list-sum bound, in the shape of `qChebyshev_abs_le`'s induction.

Estimated ~40 lines. Nothing in it looks hard; it was left because the
empty-spectrum result already establishes the defect and names the repair.

**Note the `qInteger` zero case** when doing it: `[ρ]_q = 0` at `ρ = 0`, and
Lean's `x/0 = 0`, so such a term contributes `0`. That helps rather than
hurts — but a proof that assumes `[ρ]_q ≠ 0` will not go through.

## Blast radius: none in Lean, two remarks in content

Zero Lean consumers of `explicit_formula` or `QExplicitFormula` outside the file.
Two content blocks cite `conj:explicit-formula` in `uses[]` —
`rem:yekutieli-quantum-li` and `rem:unitary-stability` — and both are `remark`s,
which make no logical claim, so nothing downstream is built on the refuted form.

---

## CLOSED 2026-08-30 — the general case is proved; the class is uninhabitable, full stop

`not_qExplicitFormula (D : QZetaDatum) : ¬ QExplicitFormula D`. No hypothesis on
the spectrum, the ideals, `Ω_q` or `q`. `#print axioms`
`[propext, Classical.choice, Quot.sound]`; file `lean`-direct exit 0.

Two supporting results, same argument as the empty-spectrum case plus the bound
that was missing:

- `spectral_term_norm_le` — each term is `≤ √2^{|Re ρ|} / ‖[ρ]_q‖` on
  `X ∈ (1, √2]`. Crude by design: it needs to be `X`-independent, not sharp.
- `spectralSum_norm_le` — the list sum, by the same induction as
  `qChebyshev_abs_le`.

**The blocker this bean named dissolved rather than being worked around.** It
said the proof needs `‖(X:ℂ)^ρ‖ = X^{Re ρ}`, that `spectral-half-line.lean`
already has it as `abs_cpow_ofReal_eq_rpow_re`, that §0a forbids importing it,
and that the fix is to lift it to a library module — the `qou-sibdup` remedy.

**Mathlib already had it**: `Complex.norm_cpow_eq_rpow_re_of_pos`. So no library
module was needed and no new duplication was created. The corollary is worse for
the corpus than it is good for this bean: **`abs_cpow_ofReal_eq_rpow_re` was a
twelve-line hand-rolled reproof of a Mathlib lemma**, and I had proposed
promoting it to a shared module. It is now a one-line wrapper around the Mathlib
result, with its six call sites untouched.

That is the prepare-merge §2a reuse question — *"did upstream introduce
something this branch is reinventing?"* — which I had been applying to `main`'s
new content and not to Mathlib. **Check Mathlib before lifting anything.**

**The `[ρ]_q = 0` case needed no special handling**, as the bean warned it
would: at `ρ = 0` the bracket vanishes, Lean's `x / 0 = 0` makes the term `0`,
and the bound covers it. A proof assuming `[ρ]_q ≠ 0` would have been both
unnecessary and false. The subsumption test includes `⟨0⟩` in the spectrum for
exactly this reason.

**Verified to subsume, not assumed to**: `not_qExplicitFormula` re-derives both
earlier refutations (`not_qExplicitFormula_empty`, and
`not_qExplicitFormula_of_nil_spectrum` with its hypothesis unused — Lean's
unused-variable warning is the proof it is not needed), and additionally kills a
datum with a **nonempty** spectrum `[⟨½ + i⟩, ⟨0⟩]` that neither could touch.

Both earlier theorems are kept, with docstrings now saying they are subsumed:
the empty-spectrum proof is the argument minus the spectral bound, which is
where it is easiest to read, and the single-datum counterexample still guards
the withdrawn axiom against reinstatement.

**Unchanged: this refutes the formalisation, not the mathematics.** The repair
is still an infinite sum with a specified summation order.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — w16: the ordered-infinite-spectrum carrier, and what it forces (PR #8535)

Added the repair this bean names, in `q-geometric-langlands/explicit-formula.lean`:
`QZetaDatumSeq` (spectrum `ℕ → ReebEigenvalue`, order part of the data) and
`class QExplicitFormulaSeq` (partial spectral sides converge to `ψ_q(X)` for every
`X > 1`). **No instance** — open, §3b.

Proved, sorry-free (`[propext, Classical.choice, Quot.sound]`, lean-direct exit 0):
- `partialSpectral_unbounded` — conditional on the class, the ordered partial spectral
  sums are unbounded on `(1, √2]`;
- `not_qExplicitFormulaSeq_of_bounded` — uniformly bounded partial sums exclude a datum;
- `not_qExplicitFormulaSeq_of_summable` — a summable majorant `√2^{|Re ρ_n|}/‖[ρ_n]_q‖`
  excludes it. So conditional, order-dependent convergence near `X = 1` is **forced**.

Still open: whether `QExplicitFormulaSeq` has any instance (needs the Mellin/contour
route the docstring names). Bean stays open.
