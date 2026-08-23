---
# qou-kkja
title: 'GAP: two batch rows need a §3b-cond model class, not a revert (shell_filling_lp_strong_duality, mobius limit_to_classical)'
status: completed
type: task
priority: normal
created_at: 2026-08-21T21:16:32Z
updated_at: 2026-08-22T20:32:16Z
---

Opened by the sorry-closure honesty audit (PR #5411,
docs/audits/2026-08-21-sorry-closure-honesty-audit.md).

The audit graded 12 declarations from the 2026-08-21 batch. All 12 were
reverted, but TWO of them are not pure self-assuming projections and
deserve a better disposition than the honest `sorry` they were returned
to. Recording them so the revert is not mistaken for the final answer.

1. `QOU/Molecular/shell_filling_rule.lean :: shell_filling_lp_strong_duality`
   Verdict `genuine-composition`. The batch proof chained two fields by
   transitivity (`rw [ctx.strong_duality, ctx.dual_obj_eq]`) rather than
   projecting the conclusion. What it assumes is LP strong duality
   itself — a real, citable theorem ([bertsimas1997], ISBN
   9781886529199), not a framework-specific claim.

2. `QOU/BraidsKnots/mobius_frobenius_kernel.lean :: limit_to_classical`
   The field asserts a real `Filter.Tendsto` claim, so the class is
   content-bearing rather than empty. But paired with `K_classical_eq`
   it recomposes to exactly the conclusion, which is why it was graded
   `self-assuming-projection (2-field split)` and reverted.

WHY NOT FIXED IN #5411: the honest §3b-cond fix is a SEPARATE `extends`
model class carrying the named upstream hypothesis, with the theorem
deriving the conclusion from it. For (1) that cannot be done
file-locally — the same `ShellFillingRuleContext` also carries the two
self-assuming pairs for claims (i) and (ii), so splitting duality out
means restructuring the class. The audit brief forbids inventing a new
class to tidy a gap away, so this is queued rather than improvised.

TO RESTART COLD:
- Exemplar to copy: `QOU/FluidDynamics/q_bkm_criterion.lean` (verified,
  §3b-cond item 5 non-degenerate).
- Better in-file precedent: the `QTurbulenceCascadeModel` pattern that
  this same batch deleted and #5411 restored — one named physical
  hypothesis (Kolmogorov cutoff `q^N <= Re^(3/4)`), conclusion DERIVED by
  log algebra in `finite_cascade_depth_of_cutoff`. Read that file first.
- For (1): add `class ShellFillingLPDuality extends ShellFillingRuleContext`
  with the LP primal/dual feasibility data as fields and strong duality
  either cited or derived; name it `_of_` per Mathlib conditional-lemma
  convention. Keep claims (i) and (ii) on honest `sorry`.
- Acceptance test: the class must NOT be dischargeable by choosing values
  that make the conclusion true. If it is, it is still self-assuming.
- Note: no instance exists for ANY of the twelve context classes, so
  every downstream `[ctx]`-conditional theorem is currently vacuously
  conditional. A trivial instance would be worse (the qou-6dzi / PUnit
  defect) — do not add one to make the class look inhabited.

## DISPOSITION 2026-08-22 (both rows closed)

**Row 1 — `shell_filling_lp_strong_duality`: FIXED** (PR #5459, merged
`2d317bfcdd`). `ShellFillingLPDuality extends ShellFillingRuleContext`
carries assignment variables, per-site cost, reduced cost and a dual
optimality certificate (stationarity + complementary slackness +
primal feasibility); claim (iii) is DERIVED:

    Sum cost_i x_i = Sum (y_0 + slack_i) x_i
                   = y_0 Sum x_i + Sum slack_i x_i = y_0 Z + 0

`#print axioms` -> [propext, Quot.sound], no sorryAx. No instance
added, per the warning in this bean.

**Row 2 — `mobius_frobenius_kernel`: NO FIX AVAILABLE. Not a class-design
problem.** The current state on main is ALREADY the honest disposition:
`MobiusFrobeniusKernelContext` carries only data (`gamma`, `K_FH`), the
theorem states the real `Filter.Tendsto` claim, and the body is an
honest `sorry` + citation. `mobius_frobenius_kernel_unconstrained_false`
machine-checks that the class cannot imply it.

Why no §3b-cond class helps here, unlike row 1: in row 1 the certificate
fields (cost, slack, feasibility) are genuinely different objects from
the conclusion, so the equality is real algebra. Here the batch's two
fields were `limit_to_classical` (K_FH -> K_classical) and
`K_classical_eq` (K_classical = 1/r^2); composing them is a `rw`, so the
pair IS the conclusion split in two. That is the 2-field split the audit
already rejected, and re-introducing it under a new class name would be
the same defect with more ceremony.

The genuine hypotheses would be the reductions the manuscript names —
q-Hodge star -> classical Hodge star, and the Frobenius pairing
`int_A . mu` -> the SU(2) Killing form at q = 1. Corpus-grep 2026-08-22
finds neither formalised:

- `mobius-energy.lean :: ClassicalLimit` is about the ENERGY limit
  (`energy_cat = (1/4) energy_classical + normConst`), not the KERNEL
  limit, and carries that as a single assumed field.
- `mobius-energy-proof.lean` has `CategoricalMobiusEnergy` /
  `MobiusEnergy` on the same energy-level object.
- `KnotFactorFrobeniusPairing.lean`, `su2-basis.lean` do not supply the
  q -> 1 reduction of the pairing to the Killing form.

So row 2 is blocked on UPSTREAM FORMALISATION, which is substantial new
work, not a restructure.

ALREADY TRACKED — no new bean. `vta3` ("Derive explicit Frobenius-Hopf
kernel K_FH(q) to wire lem:mobius-energy-frobenius-kernel", 2026-07-06)
is exactly this blocker: same lemma, and it names the same two
reductions (q-Hodge star -> classical Hodge star; Frobenius pairing ->
SU(2) Killing form), ending "Do NOT fabricate". Sibling `ne0m` is the
same q-Hodge-star gap one lemma over (lem:nsi-q-deformed-kernel). The
2026-08-22 analysis above REPRODUCED vta3's conclusion independently
rather than discovering it — recorded as confirmation, not as a new
finding. Row 2 therefore needs no bean of its own; it needs vta3.

This bean is closed because its stated scope — "do these two rows need a
model class?" — is now answered: row 1 yes and done, row 2 provably no.

**Incidental finding, NOT fixed here.** `mobius-energy.lean ::
mobius_energy_nonneg` is itself a field projection —
`theorem mobius_energy_nonneg (cme) : 0 <= cme.energy_classical :=
cme.energy_classical_nonneg` — conclusion character-identical to the
`energy_classical_nonneg` field. This is the `type-matched projection`
class the vacuity audit already tracks as triage-pending. Not touched:
Mobius-energy non-negativity for embedded curves is a real theorem
(Freedman-He-Wang) and deciding between "prove it" and "keep it an
honest structural hypothesis" is a judgement call, not a mechanical fix.
