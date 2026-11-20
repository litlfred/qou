---
# qou-4paj
title: 'FALSE AXIOMS: the two nucleon-mass axioms assert propositions whose negations are provable'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-04T02:40:09Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-wp3h
---

Kernel-verified 2026-09-04 on `origin/main`. Not a gap and not an over-claim:
two `axiom` declarations assert propositions whose **negations are provable**
from definitions in the same file, so each file is inconsistent.

```lean
-- folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.lean
noncomputable def q₀ : ℝ := 1.10998
noncomputable def proton_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  vol_borromean / hbar_q ^ 2

axiom proton_mass_from_substrate_axiom : |proton_mass q₀ - 938.272| < 1
```

`proton_mass q₀ = 746.400676451`, so `|746.40 − 938.272| = 191.87`, not `< 1`.
`norm_num [abs_lt]` proves the negation after unfolding; `lean`-direct exit 0.
Neutron identical: `746.505` against an asserted `939.565`, negation likewise
kernel-proved.

**Not a wrong constant.** ~192 MeV, ~20 %. Correcting `vol_borromean` is not the
fix: `Vol(𝓑₃)/ℏ_q²` as an *absolute* nucleon mass is the shape AGENTS.md marks
🛑 (owner ruling 2026-06-24 — "NOT the canonical ABSOLUTE nucleon mass"), and
the 2026-08-11 ruling excised absolute mass as a prediction altogether. Neither
file contains `m_e`, so it is not even dimensionally the
`m_e·Vol(K)·ρ(K)/ℏ_q²` shape it resembles. Both files predate both rulings.

**Blast radius: none beyond the two files.** Neither theorem has a consumer
anywhere in `content/`. Both are content-block siblings — what a `lean.ref`
resolves to *first* under §0a — outside the Lake globs, and CI is
`workflow_dispatch`-only, so nothing has ever compiled them. That is why two
false axioms could sit here.

**DELIBERATELY NOT FIXED — this needs the author.** Deleting the axioms breaks
the theorems; "correcting" the constants would enshrine a construction two owner
rulings retired; and deciding what `def:categorical-proton`'s formalisation
should say *now that absolute mass is excised* is an authoring judgement about
the paper's physics, not a repair.

Three dispositions, for whoever picks this up:

1. **Retire the Lean.** Drop `proton_mass` / `neutron_mass` and their axioms
   entirely; the blocks keep their prose. Consistent with the 2026-08-11
   excision, loses nothing that is currently used, and is the smallest change.
2. **Restate as a ratio.** The excision keeps *ratios* in scope. `m_n/m_p` or
   `Δ_pn` from the same skein asymmetry would be a real claim the framework is
   allowed to make. Note `neutron_proton_splitting` in the neutron file already
   states `Δ = ½(q − q⁻¹)`, which at `q₀` is `0.0955`, against the physical
   1.293 MeV — so that leg needs its own check before being leaned on.
3. **Keep as an explicitly-labelled historical artefact**, with the axioms
   removed so the files are consistent and the prose marked superseded.

My judgement, offered as judgement: **(1)**. The construction is retired by
ruling, nothing consumes it, and (2) is new work that should be its own bean
rather than a rescue of this one.

Full write-up with the reproduction snippet:
[`docs/audits/2026-09-04-two-false-nucleon-mass-axioms.md`](../docs/audits/2026-09-04-two-false-nucleon-mass-axioms.md).

Found by fixing an unrelated scope bug: the audit walked only the Lake library
tree, so 944 content-block siblings and 148 of the corpus's 182 axioms were
invisible. Nothing was looking for false axioms.

## Progress Update (2026-11-16 — Round 47, PR #8147)

- Removed both inconsistent `axiom` declarations (`proton_mass_from_substrate_axiom` and `neutron_mass_from_substrate_axiom`) in PR `litlfred/qou#8147` (commit `94984f6696056c5cbe6d700149fbb37894d29ad5`):
  1. `folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.lean`: replaced `proton_mass_from_substrate_axiom` with sorry-free theorems `proton_mass_from_substrate : proton_mass q₀ = 7.32772475341775 / (1 - q₀⁻¹) ^ 2` (`rfl`) and `bare_borromean_carrier_not_938 : ¬ (|proton_mass q₀ - 938.272| < 1)` (`by unfold proton_mass q₀; norm_num [abs_lt]`), documenting the 2026-06-24 and 2026-08-11 owner rulings.
  2. `folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron.lean`: replaced `neutron_mass_from_substrate_axiom` with sorry-free theorems `neutron_mass_from_substrate : neutron_mass q₀ = 7.32772475341775 / (1 - q₀⁻¹) ^ 2 + (1 / 2) * (q₀ - q₀⁻¹)` (`rfl`) and `bare_neutron_carrier_not_939 : ¬ (|neutron_mass q₀ - 939.565| < 1)` (`by unfold neutron_mass q₀; norm_num [abs_lt]`).
  3. Updated `docs/audits/2026-09-04-two-false-nucleon-mass-axioms.md` with the resolution record.
- Kept at `status: in-progress` pending PR #8147 merge and owner verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8147, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
