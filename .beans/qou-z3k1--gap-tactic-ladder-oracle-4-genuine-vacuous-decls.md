---
# qou-z3k1
title: 'GAP: tactic-ladder oracle finds 3 vacuous decls the vacuity audit misses (+2 definitional restatements)'
status: todo
type: task
priority: high
tags:
    - lean
    - vacuity
created_at: 2026-08-08T00:05:00Z
updated_at: 2026-08-08T00:05:00Z
---

Four provable declarations assert nothing about the objects they name, and two
more merely restate their own `def`. None has a `sorry`, an `axiom`, or a `True`
conclusion; all type-check and always will.

Found by pointing the folio-assistant triviality probe (cheapest-first tactic
ladder) at the corpus after the LEAN_PATH fix in litlfred/folio-assistant#69.
This is a DIFFERENT shape from `qou-q407` (`(h : P) : P := h`) — the static
detector `scripts/lean-self-assuming-audit.py` does not and cannot catch these,
because the vacuity is semantic rather than syntactic.

## Corpus-grep (AGENTS.md "Before declaring open")

**Two passes, and the first was not enough — recorded because the gap is the
reusable lesson.**

Pass 1 (audit *docs*): checked all six against
`docs/audits/2026-08-07-lean-vacuous-existential-audit.json` on main (the sibling
17-item audit, 4 drained as of 402240a1b6) — none present. The other
`docs/audits/` hits were all `lean-atlas-deps.json`, which mechanically indexes
every declaration and carries no verdict.

Pass 2 (live *detector*): ran
`bun run content/pipeline/lean-vacuity-axiom-audit.ts content` — 120 defects, 81
exempt. **This retracted one of the six.** Grepping audit prose is not the same
as running the gate; a detector can already cover a case that no audit doc
mentions. Run the checker, not just `grep`.

### RETRACTED — already a counted defect

`delta_max_numerical_scale` (`lean/QOU/Appendix/DeltaMaxNumericalScale.lean:9`)
is **already flagged critical and NOT exempt** by
`proof-no-self-assuming-projection` / `field-projection`, at exactly the line
reported. It is a re-discovery, not a finding. It remains a real defect —
`theorem … [ctx : DeltaMaxNumericalScaleContext] : (1 : ℝ) = 1 := ctx.holds`,
banned by both §Strict Lean Discipline item 5 and §3b-cond item 5 — but it is
already in the queue and belongs to whoever drains that category.

## GENUINE — assert nothing, and the audit does not flag them

1. `LevelSufficiency` — `knots-particles-confinement/level-sufficiency.lean:72`

   **Name-collision caveat (checked).** The audit *does* flag a
   `LevelSufficiency` — but a DIFFERENT declaration: a `def` in the library tree
   at `lean/QOU/BraidKnot/LevelSufficiency.lean:104`, and flagged **exempt**
   ("canonical §3b placeholder projection"). The content-block file
   `knots-particles-confinement/level-sufficiency.lean` is **not flagged at
   all**. Two objects sharing a glyph, per the registry §2 rule that attributes
   do not transfer across overloaded symbols — do not let the exempt library
   `def` launder the unflagged content-block `theorem`.

       theorem LevelSufficiency (P P' : ConfinedParticleTy) (q : ℝ)
           (_h_unfold : unfolds P P') (_h_cover : kMax P q ≤ coarseStrands P) :
           markovTrace P q = markovTrace P' q := rfl

   Both hypotheses `_`-prefixed (unused) and the proof is `rfl`, so the claim
   holds for ANY two particles — the covering condition is decoration. Worth more
   than a restatement: it means `markovTrace` is definitionally independent of
   its particle argument, which is a defect in the definition, not just the
   theorem.

2. `hadron_operations_closure` — `knots-particles-confinement/hadron-operations-closure.lean:35`

   Four conjuncts of the form `∀ n, ∀ h : Hadron n, ∃ h' : Hadron n, h' = op n h`.
   Vacuously true for any total function (take `h' := op n h`). Asserts nothing
   about closure beyond well-typedness.

3. `cp_violation_spectral_form` — `observations/cp-violation-spectral-form.lean:48`

       ∃ δ : ℝ, δ = (W.chiAlt / W.chiSym).im := ⟨(W.chiAlt / W.chiSym).im, rfl⟩

   "There exists a real equal to this real."

Items 2–3 are the vacuous-existential class of the sibling audit; item 1 is not
(it is an unused-hypothesis `rfl`).

All three verified absent from the live detector by FILE path, not by name
substring — `hadron-operations-closure`, `cp-violation-spectral-form` and
`level-sufficiency` are each `NOT FLAGGED`.

## DEFINITIONAL RESTATEMENT — `rfl` + unused hypothesis, restates its own `def`

4. `strangelet_double_beta` — `observations/strangelet-double-beta.lean:65` —
   `unfold double_beta_rate; rfl`, with `(hq : 1 < q)` unused.
5. `borel_partial` — `lean/QOU/AppendixSurreals/BorelPartialResolution.lean:19` —
   `rfl`, with `(_ : 2 ≤ n)` unused.

Both verified `NOT FLAGGED` by file path.

Per AGENTS.md §Strict Lean Discipline item 8 these are notation, not theorems,
and should be `def`/`abbrev` or dropped.

## Scope

Scope-**(a)** per AGENTS.md §"Before declaring refuted": the *Lean* for these
five carries no content. NOT a claim the underlying mathematics is wrong.

## Why the ladder oracle still earns its cost

The retraction narrows the claim but does not void it. Of six candidates, one
was already gated and five were not — and the five are invisible to the static
detectors *by construction*: `proof-no-self-assuming-projection` matches bodies
shaped like `ctx.field`, so an unused-hypothesis `rfl` (item 1), a vacuous
existential discharged by `⟨x, rfl⟩` (items 2–3), and a `def`-restating `rfl`
(items 4–5) cannot match it however the regexes are tuned. Semantic vacuity
needs an oracle that runs the elaborator.

## Not edited

No declaration touched. Restating a theorem changes what the corpus claims and
the honest disposition (prove / state with `sorry` + `-- Ref:` / demote to
`conjecture`, per §1a) is a per-item judgement. `LevelSufficiency` in particular
needs the `markovTrace` definition looked at, not just the theorem.

## Sweep COMPLETE (2026-08-08) — full results

802 probed, **74 closed (9%)**, 133 skipped. Full write-up:
`docs/audits/2026-08-08-triviality-sweep-corpus-wide.md`.

Headline additions beyond the five above:

- **12 vacuous existentials** (`∃ x, x = e := ⟨e, rfl⟩`), of which **8 are NOT**
  in main's `2026-08-07-lean-vacuous-existential-audit` — mass_tower_coefficient_stratification,
  habiro_integral, residue_isRingHom_of_residueAtRoot, hadron_operations_closure,
  pauli_factor_wedderburn, explicit_alpha_k_h3, optimal_nf_is_standard_basis,
  cp_violation_spectral_form. The other 4 ARE in it — independent confirmation,
  no action. Coordinate with that audit's owner before draining.
- **2 quantified tautologies** — `orbit_sum_general`, `closed_form_holds`
  (`∀ n, 2 ≤ n → f n = f n := rfl`). Now statically caught.
- **34 broken `lean.ref`** — 31 naming a declaration that exists nowhere, plus
  3 NAMESPACE MISMATCHES where the name exists in a different namespace
  (`QOU.BraidKnot.AtomKnot.unique` vs declared `ConfinementLevel.unique`).

Static coverage now catches 8 of the 74; the rest need the elaborating oracle.

Two detector gaps closed from these findings: `proof-no-unused-hypothesis-rfl`
(15 hits) and ascribed-literal tautologies (12 hits — `colour_sector_count :
(3 : ℕ) = 3 := rfl` and friends, numeric claims whose content lives only in the
declaration name).

## Follow-up

Wire a `proof-self-assuming` / `proof-unused-hypothesis-rfl` criterion into
`content/pipeline/lean-vacuity-axiom-audit.ts` so this class joins the
review-ledger workflow instead of depending on an expensive probe run
(`qou-q407` follow-up 1 covers the syntactic half).
