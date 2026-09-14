---
# qou-vh1o
title: 'GAP: 13 self-assuming-projection candidates never reach the review ledger (derivation-pending exemption arms)'
status: completed
type: task
priority: high
created_at: 2026-09-13T19:43:07Z
updated_at: 2026-09-14T07:59:46Z
---

## The finding

`content/pipeline/lean-vacuity-axiom-audit.ts` seeds the agent-inspection review
ledger only from candidates whose `exempt_reason` matches
`LEDGER_TRACKED_EXEMPT = /triage pending/` (line ~1697; consumed at the seeding
site ~3576 and at the promotion site ~3411).

Two exemption arms emit the string **"canonical §3b placeholder projection
(tracked; derivation pending)"**. That does not match. So every candidate taking
those arms is dropped at the seeding site, never reaches an agent, and can never
be promoted back to a counted defect by a `genuine` verdict.

Measured on `origin/main` (full corpus, 3841 `.lean`): flipping the wording to
"triage pending" seeds **34** previously-invisible candidates. **21** of them are
`applied-field-projection` and are adjudicated in the PR that files this bean.
The **other 13 are this bean**, and they are pre-existing — they predate the
`applied-field-projection` pattern entirely:

- **`applied-tuple-projection` — 6**
  - `lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean:43` `acoustic_horizon_conditions`
  - `lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` `discrete_vortex_spectrum`
  - `lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` `root_of_unity_truncation`
  - `lifting-and-descent/ccg-crossed-module-structure.lean:35` `ccg_crossed_module_structure`
  - `mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:131` `qbeta_c_k_closed_forms_derived`
  - `mass-theory/crystal-basis-resolves-mass-tower-open-problems.lean:122` `crystal_basis_reduction`
- **`tuple-projection` reaching the arm as a `def` proof (`isDefProof && !nameGateMatched`) — 7**
  - `fluid-dynamics/acoustic-horizon-conditions.lean:98` `acoustic_horizon_regularity`
  - `fluid-dynamics/discrete-vortex-spectrum.lean:91` `discrete_vortex_spectrum`
  - `fluid-dynamics/root-of-unity-truncation.lean:73` `root_of_unity_truncation_conditional`
  - `fluid-dynamics/vorticity-lower-bound.lean:85` `vorticity_lower_bound_conditional`
  - `lifting-and-descent/ccg-cosimplicial-identities.lean:43` `ccg_cosimplicial_identities`
  - `mass-theory/q-beta-bar-even-kernel-typeclass.lean:123` `bar_even_kernel_implies_q_one_shadow`
  - `mass-theory/q-beta-q-eq-one-shadow-gate.lean:86` `qbeta_q_eq_one_shadow_anchors`

## Why it was left rather than absorbed

Each needs its own agent verdict (`genuine` / `legit` / `advisory`) — 13 more
file reads in a different domain (fluid dynamics, cosimplicial identities) from
the tranche that found it. Absorbing them would have tripled the PR and buried
the applied-field adjudication. AGENTS.md §"Small-moderate fixes for related
bugs ride on the active PR" — 13 adjudications is not small.

Two of the 7 `tuple-projection` entries have a **counterpart already in the
ledger** under a different declaration in the same file (e.g.
`q-beta-bar-even-kernel-typeclass.lean::bar_even_kernel_implies_direction_sanity`
is ledgered `genuine`), so the prior is that this group skews `genuine` too —
but that is a prior, not a verdict.

## What to do

1. Change the second arm's `exempt_reason` to "triage pending" (one string).
2. Run `--review-ledger` scoped to the 13 files (the scope guard added in #7332
   makes a scoped run non-destructive — verified: a 18-file run added 21 and
   removed 0).
3. Adjudicate the 13 per the rubric stated in the PR body.
4. `--check-ledger` must stay green.

## Related, NOT this bean

- **Scope leak in `seedProbeInhabitedCandidates`.** It ignores the scan scope,
  so a run scoped to 18 files reset a `proof-carrier-inhabited-by-probe` entry
  in a 19th file that was never scanned
  (`transfer-matrix-level-independence.lean::…CrystalGraphRealization`). Same
  class as the deletion-scope bug fixed in #7332, one seeder over. That entry
  was re-adjudicated in this PR rather than restored, because its file had
  genuinely changed (`70af9415e22d` → `b635d218c86a`, commit `8ea4e5479f`).
- **The committed ledger is stale by ~53 entries against a full-corpus run**:
  33 adjudications whose candidate no longer fires (spot-checked three — all
  genuinely repaired by `qou-9yt9` / `qou-ghy5`, so deletion is correct) and
  ~20 whose `.lean` changed since the verdict. `--check-ledger` reads green on
  `main` only because nobody has re-run `--review-ledger` whole-corpus. That is
  `qou-metc` item 3.


## ADJUDICATION DONE (2026-09-13, reading only — no code change)

All 13 read on `main` at the current revision. **The code change stays
blocked**: the second-arm wording edit touches lines adjacent to #7341's
split of the same `if`, and #7341 is parked on the owner. This section is the
verdict record; the ledger write lands with that PR.

### These are NOT the same defect class as the 21

The 21 were plain self-assuming projections — `theorem X : P := ctx.P_field`.
The 13 contain **four different shapes**, and only one of them is that:

**(A) Antecedent-asserting context — the sharpest, 3 of 13.** The class
carries a FREE `Prop` field, a field ASSERTING it, and the implications to
the conclusion; the theorem does modus ponens:

```lean
class AcousticHorizonConditionsContext ... where
  acoustic_horizon_formed : Prop                    -- free Prop (qou-tsnp class)
  horizon_active : acoustic_horizon_formed          -- asserts its own antecedent
  impl_transonic : acoustic_horizon_formed → mach = 1
theorem acoustic_horizon_conditions [ctx] : ctx.mach = 1 ∧ … :=
  ⟨ctx.impl_transonic ctx.horizon_active, …⟩
```

The class supplies BOTH premises, so the conclusion is assumed with two
fields of ceremony — and because the `Prop` is free, `⟨True, trivial, …⟩`
inhabits the premise. All three docstrings claim **"(§3b-conditional, fully
proved)"**, which is the second defect: §3b-cond item 5 forbids exactly this.

**(B) Conjunction-of-fields `def`, 4 of 13** — `⟨ctx.f₁, ctx.f₂, …⟩` where the
conclusion is the conjunction of the class's own fields. `P → Q → (P ∧ Q)` has
no content. Split by disclosure (below).

**(C) Accessor on an EXPLICIT structure argument, 2 of 13** — takes
`(ccg : CosimplicialCrossedGroupoid M)` as an ordinary argument, not a class
hypothesis, and projects a field any constructor must prove. That is ordinary
mathematics ("for any CCG, …") and not a self-assuming projection at all.

**(D) The correct §3b-cond pattern, 1 of 13** — the conclusion is none of the
class's fields and the premises are caller-supplied.

### Verdicts — 6 genuine / 6 advisory / 1 legit

**genuine (6)**

| decl | why |
|---|---|
| `lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean:43` `acoustic_horizon_conditions` | shape (A); docstring claims "fully proved" |
| `lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` `discrete_vortex_spectrum` | shape (A); same docstring claim |
| `lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` `root_of_unity_truncation` | shape (A); same docstring claim |
| `mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:131` `qbeta_c_k_closed_forms_derived` | **see the finding below — this is the serious one** |
| `fluid-dynamics/vorticity-lower-bound.lean:85` `vorticity_lower_bound_conditional` | shape (B), and the docstring DENIES the defect: *"it composes them; it does not assume its own conclusion"* over `⟨ctx.separation_decay, ctx.vorticity_lower, ctx.bkm_diverges⟩`, which is exactly its conclusion in three pieces |
| `fluid-dynamics/root-of-unity-truncation.lean:73` `root_of_unity_truncation_conditional` | shape (B), **the identical denial sentence verbatim** — same authoring pass |

**advisory (6)** — disclosed, declared `def`, carrier is a real hypothesis
bundle or an explicit structure; needs presentation work, not restructuring:
`fluid-dynamics/acoustic-horizon-conditions.lean:98` `acoustic_horizon_regularity`;
`fluid-dynamics/discrete-vortex-spectrum.lean:91` `discrete_vortex_spectrum`;
`mass-theory/q-beta-bar-even-kernel-typeclass.lean:123` `bar_even_kernel_implies_q_one_shadow`;
`mass-theory/q-beta-q-eq-one-shadow-gate.lean:86` `qbeta_q_eq_one_shadow_anchors`;
`lifting-and-descent/ccg-cosimplicial-identities.lean:43` `ccg_cosimplicial_identities`;
`lifting-and-descent/ccg-crossed-module-structure.lean:35` `ccg_crossed_module_structure`.

The two q-beta gate `def`s are the **exemplars** and should not be "fixed":
both say *"Assumed, not derived here"* in terms, both are `def` not `theorem`,
both classes are parametric over the caller's functions (so no global instance
can discharge them), and `q_eq_one_shadow_gate_reject_c2` derives a real
negation the class does not contain. `ccg_crossed_module_structure` is
advisory only because its conclusion `Nonempty CrossedModule` mentions neither
`ccg` nor `n` — the `∀ n` is vacuous and the statement is weaker than its
docstring.

**legit (1)** — `mass-theory/crystal-basis-resolves-mass-tower-open-problems.lean:122`
`crystal_basis_reduction`. Shape (D): the class carries `ReducesTo` implications,
the theorem applies them to caller-supplied `hCount`/`hDepth`/`hLimit`, and the
conclusion `chirality ∧ term7 ∧ zHabiro` is **no field of the class**. Its own
docstring already says so, and records that it was repaired from the bad shape
(*"the part the previous encoding — a bare `Prop` field handed back — did not
state"*). Worth citing as the reference §3b-cond encoding.

## 🛑 FINDING — a "conditional" theorem that is unconditional on FITTED values

`mass-endomorphism/conj-qbeta-c-k-closed-forms.lean`. The theorem's docstring
says the openness *"is carried by that class having no instance"*. **There is
an instance, 49 lines above it**, and it is the only one anywhere:

```lean
noncomputable instance defaultQBetaCKClosedForms : QBetaCKClosedForms where   -- line 82
  c_4 := fun q => -2 * (hoefsmitB q)^4
  …
theorem qbeta_c_k_closed_forms_derived [inst : QBetaCKClosedForms] (q : ℝ) : … -- line 131
```

Parameterless and global, so instance search resolves `[inst]` to it. The
file contradicts itself: the **class** docstring names the instance (*"The
instance `defaultQBetaCKClosedForms` axiomatises these"*) while the
**theorem** docstring 49 lines later says nothing inhabits the class.

Why it matters beyond bookkeeping: that instance's values are fitted, and the
file says so — *"whose instance values are FIT, not proved"*, with residuals
*"c_4 0.9%, c_5 2.4%, c_6 14%; c_7 signed-error +114%"*. So a §3b-cond
"conditional" result is, in practice, unconditional on a fit. That is the
shape AGENTS.md §"Axiomatization is NOT a Proof" rule 2 names, and the same
trap as `ClassicalLimitStpart`, which was demoted `instance` → `def` on
2026-08-24 for exactly this reason.

**Scope, measured, so this is not oversold:** `QBetaCKClosedForms` and
`qbeta_c_k_closed_forms_derived` are referenced by **no other file** — the
instance's reach is file-local. So nothing downstream is currently laundered;
what is wrong is the file's own self-description and the `instance`-vs-`def`
declaration. The fix is the `ClassicalLimitStpart` one: demote to `def`, and
correct the theorem docstring.

## Second finding — three propositions are formalised TWICE, and the library copy is the bad one

`acoustic-horizon-conditions`, `discrete-vortex-spectrum` and
`root-of-unity-truncation` each have a content-block sibling **and** a library
module under `lean/QOU/FluidDynamics/`. Per AGENTS.md §0a the `lean.ref`
resolves to the **sibling first**, and in all three the sibling is the better
formalisation — `acoustic_horizon_criterion_iff` is genuinely proved
(`rw [ctx.mach_def, div_eq_one_iff_eq (ne_of_gt ctx.cs_pos)]`) and
`acoustic_horizon_hawking_temperature` closes by `field_simp`, while the
library twin is shape (A).

So the three shape-(A) `genuine` verdicts sit on declarations **the blocks do
not resolve to**. Measured containment:

- the library modules are inside the Lake glob (`globs = ["QOU", "QOU.+"]`,
  `srcDir = "."` at `lean/`), so they DO compile under `lake build QOU`;
- the siblings are outside `lean/` and are not in the library, so there is no
  name collision even though `acoustic_horizon_conditions` and
  `discrete_vortex_spectrum` exist under the same name in both;
- **importers of the three library modules: 0.**

Contained, then — but a downstream library file that imports
`QOU.FluidDynamics.acoustic_horizon_conditions` gets the shape-(A) version,
not the proved one. Whether to delete the library twins or promote the
siblings into the library is an author call, not an agent call.


## LANDED 2026-09-14 — the 13 verdicts are in the ledger

Second arm's `exempt_reason` migrated "derivation pending" -> "triage pending",
the 13 seeded, and all 13 adjudicated verdicts written.

**Measured delta on the audit witness** (`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`):

| field | before | after |
|---|---|---|
| `total_defects` | 70 | **76** |
| `total_exempt` | 64 | **58** |
| `total_promoted_from_exempt` | 42 | **48** |
| `proof-no-self-assuming-projection` | 57 | **63** |

Exactly the 6 `genuine` verdicts moving from exempt to counted; the other 7
(6 `advisory` + 1 `legit`) correctly stay exempt. (`scanned_files` also moved
3846 -> 3847 — **not from this change**: the tree carries no new `.lean`
(`git status` clean apart from the three edited files), and the category delta
is exactly +6, so the extra file contributed no candidate.)

**Gates, all green on the final tree:**

- `--check-ledger` exit 0 — "all 119 candidate(s) carry a fresh agent verdict"
- `--selftest-docstring-sorry` exit 0 — 4 suppressed / 8 still flagged
- idempotence: a second `--review-ledger` run added 0, removed 0, changed 0

**Ledger:** 332 entries, 0 `needs-agent`; verdict split now
135 genuine / 133 legit / 51 advisory across all categories.

## The two findings did NOT ride this PR — they are author calls

Both are recorded above and are now tracked separately:

- **the fitted `defaultQBetaCKClosedForms` instance** — appended to `qou-hjf4`,
  which owns the global-instance-discharges-a-3b-binder class and already
  carries the `ClassicalLimitStpart` precedent this one matches.
- **the three doubly-formalised fluid-dynamics propositions** — bean `qou-klr1` (the §0a-INVERTED case: sibling proved, library twin vacuous, so a sweep written against §0a's documented direction would delete the wrong file of each pair).
