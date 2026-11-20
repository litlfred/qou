---
# qou-z3k1
title: 'GAP: tactic-ladder oracle finds 3 vacuous decls the vacuity audit misses (+2 definitional restatements)'
status: in-progress
type: task
priority: high
tags:
    - vacuity
    - reorg-2026-10-04
    - lean
created_at: 2026-08-08T00:05:00Z
updated_at: 2026-11-20T09:10:00Z
parent: qou-6qbv
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


## 2026-09-05 — item 3 `cp_violation_spectral_form` is DRAINED

Branch `claude/gram-kappa-laundered-axiom-2026-09-05`, PR #6782. This bean's
"Not edited" note said the honest disposition is a per-item judgement; here it
is, for this one item.

**The honest form came from the block's own `.md`, not from invention.** Its
Falsifiability section says *"Amphicheiral knots must yield exactly δ_CP = 0"*,
and its body *"Amphicheiral or real-q configurations have Im(χ_λ) = 0 and
δ_CP = 0"*. That direction is **provable** from the definition — a quotient of
two reals is real — so it is now `deltaCP_eq_zero_of_real_characters`, proved,
with hypotheses verified load-bearing (without them the goal survives as
`chiAlt.im * chiSym.re / normSq − chiAlt.re * chiSym.im / normSq = 0`).

**The conjecture proper gets a §3b carrier that is not self-assuming.** It is an
IDENTIFICATION, so the physical δ_CP enters as a PARAMETER
(`CPViolationSpectralForm (physicalDeltaCP : … → ℝ)`); asserting it against
`deltaCP`, which is *defined* as that ratio, would be the §3b-cond item-5
projection this corpus keeps catching. No instance — the honest open state,
since the corpus has no independent δ_CP (`complex-chirality-rotation.lean:44`
records the numerical bound as future work).

`lean.ref` and the definition index moved to `CPViolationSpectralForm`.
Verified lean-direct exit 0, no sorry.

**Items 1, 2, 4, 5 untouched**, deliberately. Item 1 (`LevelSufficiency`) needs
the `markovTrace` definition looked at, as this bean says. Item 2
(`hadron_operations_closure`) is four conjuncts of `∀ n, ∀ h, ∃ h', h' = op n h`
and has the same "what would the honest statement be" problem as the Markov
cluster in `qou-ekga` — closure is a claim about an operation's codomain, and
asserting it needs the operation's own definition, not a restatement.

## Note for whoever picks this up: `explicit_alpha_k_h3` should NOT be drained

I had it queued as the easiest remaining item. It is not — the file itself says
so, in a header note I had not read:

> "**Known defect, not introduced here and not fixed here.** … Making it
> falsifiable needs the α_k derived from the `H_3` curvature-rank computation,
> which is not available here; it is recorded as a bean rather than papered
> over."

So it is honestly labelled, deliberately left, and blocked on a derivation that
does not exist. Restating it would be papering over exactly what that note
refuses to paper over. Leave it.


## 2026-09-05 — item 1 `LevelSufficiency`: the defect is FIXED; its successor is already queued

Checked because this bean's own note said item 1 "needs the `markovTrace`
definition looked at, not just the theorem". It has been.

**The content-block file this item names no longer exists.**
`knots-particles-confinement/level-sufficiency.lean` is gone; the block keeps
its `.ts`/`.md` and its `lean.ref` now points at
`qou:QOU.BraidKnot.LevelSufficiency` in the library tree — the §0a
"no shadowing stubs" shape.

**The definitional defect is repaired.** This bean's sharpest point was that
`markovTrace P q = markovTrace P' q := rfl` means *"`markovTrace` is
definitionally independent of its particle argument, which is a defect in the
definition, not just the theorem"*. The live definition is

```lean
class HasMarkovTrace (P : ConfinedParticle) (q : R_q) where
  value : R_q

noncomputable def markovTrace (P : ConfinedParticle) (q : R_q)
    [h : HasMarkovTrace P q] : R_q := h.value
```

so the value is now keyed on `(P, q)` through an instance and the `rfl` proof is
impossible. The hypotheses moved onto a §3b class `LevelSufficient` carrying
`trace_eq` as a field.

**Its successor is a self-assuming projection — and is ALREADY COUNTED.**

```lean
def LevelSufficiency … [hi : LevelSufficient P P' q h_unfold h_cover] :
    markovTrace P q = markovTrace P' q := hi.trace_eq
```

`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` flags it
`proof-no-self-assuming-projection` / `field-projection`, **severity critical**,
at line 112 — one of the 34 in that category. So it belongs to whoever drains
that queue, exactly as this bean ruled for `delta_max_numerical_scale`. Do not
re-work item 1. The file is also candid about it in its own docstring
("**Assumed, not derived here** — the body projects `LevelSufficient.trace_eq`").

**Two of my own errors while checking this, both worth the reader's caution.**

1. I first reported the corpus audit had **0 hits** for this declaration. It has
   one. My script queried `d['findings']`; the data lives under `d['flagged']`,
   and `.get('findings') or []` turned a wrong key into a confident zero.
2. On seeing `def` rather than `theorem` I hypothesised it escapes the detector
   as the §1a `theorem → def` disguise. **It does not** — `detectSelfAssuming`
   has an `isDefProof` arm that opts Prop-valued `def`s in (`PROP_CONCLUSION`
   includes `=`), added because "36/99 placeholder-canonical projections are
   `def`-kind". This declaration is precisely what that arm was written for.

## 2026-11-15 — PR opened for item 2 `hadron_operations_closure` (`Q-6QBV-1 = 1`)

- PR: https://github.com/litlfred/qou/pull/8001 (`claude/qou-z3k1-ajfl-z9fx-2026-11-15`, head `dc257cfe44475b4d418b26d8e48c2b5566459344`)
- Replaced the standalone `axiom Hadron : ℕ → Type` and vacuous `∃ h', h' = op n h` conjuncts in `folio/quantum-observable-universe/knots-particles-confinement/hadron-operations-closure.lean` with a concrete carrier `HadronState n` (`Hadron n`) and proved braiding involution + alternating sign flip, Hopf-linking two-sided invertibility, skein idempotence + linear mass decomposition, and fusion associativity + mass additivity sorry-free.

## W8 note 2026-11-20 (PR #8533)

`LevelSufficiency` is still a self-assuming projection on main. It cannot be fixed by a cited sorry: `markovTrace` is free `HasMarkovTrace.value` data, so `markovTrace P q = markovTrace P' q` is false for arbitrary instances. The only honest fix is to define the trace from the Hecke character tower (Jones' Markov property). Ledger verdict: genuine, disposition gap-needs-real-markov-trace.
