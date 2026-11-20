---
# qou-7d08
title: 'Lean the Wenzl level family beyond r=2: z_C non-existence and general-r lemmas'
status: todo
type: task
priority: normal
tags:
    - wenzl-level
    - reorg-2026-10-04
    - lean
    - qbeta
    - hecke
created_at: 2026-08-16T12:55:47Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-rtxm
---

## This is the RESIDUE of PR #5229, not a duplicate of it

PR #5229 (`claude/wenzl-level-family-2026-08-16`) owns the **numerical /
symbolic / expository** side of the level-family question and states four
items: is `z_C` any level; the `z_r(q)` family for `r = 1..4`; which QOU trace
channel sits at which level; and whether "level 3 = SU(3) = colour" survives
contact with evidence (its own wording quarantines that as speculation with a
named test). As of filing it is a stub — an audit-doc plan, +20 lines, no
results — and it touches only
`docs/audits/2026-08-16-wenzl-level-family.md`.

**Do not re-run its scope here.** This bean is the part its plan does not name:
the **Lean** side, plus one obligation the algebra of PR #5230 makes precise.

## The obligation #5230 makes precise: uniqueness is not existence

PR #5230 added, unconditional and sorry-free:

- `pow_level_mul_eq_of_markovParameter : Q^r * (1 - Q + z) = z` — pure ring, no
  hypotheses at all. The inversion `Q^r = z/(1 - Q + z)`, denominator-free.
- `level_unique_of_markovParameter` — for `Q ≠ 0` and `Q` not a root of unity,
  **at most one** `r` sits at a given `z`.
- `level_eq_two_of_conventionD` — convention D's `z` pins the integer `r = 2`.

Note what `level_unique_of_markovParameter` does and does not give. It says the
level is unique **if it exists**. It says nothing about existence. So the likely
answer for `z_C` — that `Q^r = z_C/(1 - Q + z_C)` has **no** natural-number
solution `r` — is a *non-existence* statement, and it does not follow from any
lemma now in the file. It needs its own proof.

Both hypotheses are load-bearing, incidentally: at `Q = 0` the genericity
condition holds vacuously and uniqueness genuinely fails, which is why `hQ0` is
an explicit argument rather than derived.

## Tasks

- [ ] **Formalise the `z_C` verdict, whatever #5229 measures it to be.** If
      `z_C` is at no integer level, state and prove
      `¬ ∃ r : ℕ, z_C * (1 - Q^r) = Q^r * (1 - Q)` at `Q = q²`. This is a
      genuinely different shape from anything in the file — every existing
      lemma is `given r, …`. Expect it to need a growth/monotonicity argument
      in `r` at a fixed positive `q`, i.e. it will live below the
      substrate→archimedean wall (§7c) unlike the rest of the file.
- [ ] **Generalise `level_eq_two_of_conventionD` to a `level_eq_of_markovParameter`
      taking the target level as a parameter**, so `r = 1, 3, 4` are corollaries
      rather than copy-paste. The current proof is already `level_unique_…`
      plus one `field_simp; ring`; the generalisation is cheap and stops #5229's
      level family from landing as four near-identical lemmas.
- [ ] **The row cap at general `r` is already proved — wire it, do not redo it.**
      `schurPrincipal_eq_zero_iff` is stated for **all** `r`, so "level `r` caps
      at `r` rows" needs no new mathematics; the level-`r` quotient dimension
      claim is the only new part.
- [ ] **Only if #5229 finds evidence:** a Lean statement of any
      level ↔ gauge-sector correspondence. Filed here so it has a home, NOT as
      an endorsement — treat as speculation until #5229 reports, and do not
      write it into a durable artifact before then.

## Coordination

Post intent on #5229 before starting, naming this as the Lean-side split. The
natural collision is `WenzlWeightVanishing.lean`: it is the home of
`wenzlLevel_conventionD`, so if #5229 lands level-family lemmas it will want
that file too. Agree ownership first.

## Guard

Do not let a measured non-integer `r` for `z_C` be written up as "convention C
is not a Wenzl level" without the (a)/(b) scope classification of AGENTS.md
§"Before declaring refuted". A non-integer `r` from the type-A relation is a
scope-(a) negative about **that** parameterisation; it does not by itself
exclude `z_C` from being a Markov parameter of some other trace family. Only a
proved non-existence over all `r : ℕ` licenses the stronger phrasing, and even
then only for the type-A Wenzl relation as stated.

## Related

- PR #5229 — owns the numerics/audit; this bean is its Lean complement.
- PR #5230 / `docs/audits/2026-08-16-ocneanu-weight-axiomatisation.md` — the
  uniqueness lemma and the axiomatised Wenzl input.
- PR #5217 — the all-`n`, all-`r` vanishing criterion.
- `qou-25k5` (completed) — a prior convention collision where a Wenzl-Schur
  specialisation capped **columns** rather than rows. Read before assuming
  which of row/column a level caps in a given normalisation.

## 2026-11-16 — General-`r` Wenzl Level Pinning & `z_C` Non-Existence Criterion in Lean (PR #8162)
- Formalized `pow_level_mul_one_add_z_eq`, `level_eq_of_markovParameter` (general target level `r₀` parameter, specializing to `r₀ = 1, 2, 3, 4` without copy-paste), and `no_integer_wenzl_level_of_strict_bracket` / `zC_bracket_nonexistence_witness` in `folio/quantum-observable-universe/lean/QOU/Foundations/WenzlTemperleyLiebH4Keystone.lean` (wired into `QOU.lean`, 0 `sorry`, generic `CommRingOps R` per §7c).
- PR: https://github.com/litlfred/qou/pull/8162 (commit `f3dcbfe5fb51a67f3233319674c13a3791ba91d2`). Status kept `in-progress`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8162, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
