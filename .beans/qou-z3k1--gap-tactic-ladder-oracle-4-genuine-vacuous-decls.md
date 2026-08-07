---
# qou-z3k1
title: 'GAP: tactic-ladder oracle finds 4 vacuous decls no static detector catches (+2 definitional restatements)'
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

Checked all six against `docs/audits/2026-08-07-lean-vacuous-existential-audit.json`
on main (the sibling 17-item audit, 4 drained as of 402240a1b6): **none of the
six appear in it**. The grep hits under `docs/audits/` were all
`lean-atlas-deps.json`, which mechanically indexes every declaration and carries
no verdict. So these extend that audit rather than duplicate it — coordinate
with whoever owns it before draining.

## GENUINE — assert nothing

1. `delta_max_numerical_scale` — `lean/QOU/Appendix/DeltaMaxNumericalScale.lean:9`

       theorem delta_max_numerical_scale [ctx : DeltaMaxNumericalScaleContext] :
           (1 : ℝ) = 1 := ctx.holds

   Conclusion is literally `1 = 1`. Banned twice over: AGENTS.md §Strict Lean
   Discipline item 5 (tautological conclusion) and §3b-cond item 5 (the class is
   consumed as a bare projection, so the theorem derives nothing). Named as if it
   establishes a numerical scale for Δ_max.

2. `LevelSufficiency` — `knots-particles-confinement/level-sufficiency.lean:72`

       theorem LevelSufficiency (P P' : ConfinedParticleTy) (q : ℝ)
           (_h_unfold : unfolds P P') (_h_cover : kMax P q ≤ coarseStrands P) :
           markovTrace P q = markovTrace P' q := rfl

   Both hypotheses `_`-prefixed (unused) and the proof is `rfl`, so the claim
   holds for ANY two particles — the covering condition is decoration. Worth more
   than a restatement: it means `markovTrace` is definitionally independent of
   its particle argument, which is a defect in the definition, not just the
   theorem.

3. `hadron_operations_closure` — `knots-particles-confinement/hadron-operations-closure.lean:35`

   Four conjuncts of the form `∀ n, ∀ h : Hadron n, ∃ h' : Hadron n, h' = op n h`.
   Vacuously true for any total function (take `h' := op n h`). Asserts nothing
   about closure beyond well-typedness.

4. `cp_violation_spectral_form` — `observations/cp-violation-spectral-form.lean:48`

       ∃ δ : ℝ, δ = (W.chiAlt / W.chiSym).im := ⟨(W.chiAlt / W.chiSym).im, rfl⟩

   "There exists a real equal to this real."

Items 3–4 are the vacuous-existential class of the sibling audit; items 1–2 are
not (1 is a tautology, 2 is an unused-hypothesis `rfl`).

## DEFINITIONAL RESTATEMENT — `rfl` + unused hypothesis, restates its own `def`

5. `strangelet_double_beta` — `observations/strangelet-double-beta.lean:65` —
   `unfold double_beta_rate; rfl`, with `(hq : 1 < q)` unused.
6. `borel_partial` — `lean/QOU/AppendixSurreals/BorelPartialResolution.lean:19` —
   `rfl`, with `(_ : 2 ≤ n)` unused.

Per AGENTS.md §Strict Lean Discipline item 8 these are notation, not theorems,
and should be `def`/`abbrev` or dropped.

## Scope

Scope-**(a)** per AGENTS.md §"Before declaring refuted": the *Lean* for these six
carries no content. NOT a claim the underlying mathematics is wrong.

## Not edited

No declaration touched. Restating a theorem changes what the corpus claims and
the honest disposition (prove / state with `sorry` + `-- Ref:` / demote to
`conjecture`, per §1a) is a per-item judgement. `LevelSufficiency` in particular
needs the `markovTrace` definition looked at, not just the theorem.

## Provenance / caveat

From a PARTIAL sweep — 251 of ~1189 blocks (21%) at time of filing, 18 closed
hits, of which 6 reproduce `qou-q407` verdicts and 10 were newly read. At the
observed ~13% close rate the full corpus should yield 100–150 candidates; most
will be legit (concrete `decide`/`omega`/`simp` where content lives in the
definitions — 4 of the first 6 were). Sweep resumable via
`--shard I/N --checkpoint N --resume`, shards under `/tmp/triv/`.

## Follow-up

Wire a `proof-self-assuming` / `proof-unused-hypothesis-rfl` criterion into
`content/pipeline/lean-vacuity-axiom-audit.ts` so this class joins the
review-ledger workflow instead of depending on an expensive probe run
(`qou-q407` follow-up 1 covers the syntactic half).
