---
# qou-u8w5
title: 'GAP: deuteron C_knot=5.853 needs eigenphase-weighted handle-commutator charge on the NON-abelian H_6 interface braid (trefoil H_2 scalar channel proved null)'
status: todo
pr: 8344
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T20:08:58Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## What was attempted (branch `claude/deuteron-symbolic-closed-form-2026-08-02`, PR #4621)

Proof-tier symbolic/exact attempt: does a closed-form 0-parameter scalar q-invariant of the σ₁³
trefoil at q₀ reproduce the deuteron `C_knot = 5.8528` (= B_D / (m_e·|S|), 0-fit, B_AME
diagnostic-only)? DERIVE-THEN-CHECK, target locked before compute.

## Why it failed (honest NEGATIVE — do not re-run the scalar scan)

- Exhaustive scan of canonical scalar q-invariants (Jones, Markov trace, quantum dims/factorials,
  torus-knot trace ratios, WRT/Verlinde, q₀ᵏ) + 2-factor composites at 50 dps: **no 0-parameter hit**
  within the exactness threshold. Nearest 0-knob = q₀¹⁷ (0.69%, ALREADY ruled-out numerology #4556 §4);
  nearest structural single `[3]_q!` (3.0%); only things within ~2.5% carry a free level knob (= fit).
- **Structural reason (Lean-proved, Mathlib-free, sorry-free):**
  `computations/deltalambda/TrefoilSurfaceStateSum.lean` — H₂(q) (2-strand Hecke, one generator σ₁) is
  **commutative** (`mul_comm`), so **every commutator vanishes** (`commutator_zero`). The trefoil
  scalar / handle-commutator channel is null *by abelianness*, independent of q₀. Independently
  confirms sibling #4619's `tr[A,B]=0` numerical null (0.136× ≠ 5.853×) by a different route.

## Surviving candidate (the missing ingredient)

An **eigenphase-weighted per-block handle-commutator charge** on the **non-abelian H₆ interface
braid** (H₆ is genuinely non-commutative ⇒ commutators are non-zero), naturally mixed-sign /
sum-to-zero — matching the PROBE-4 chirality-sign requirement that KL-positivity could not supply.
The H₂ trefoil is abelian ⇒ handles collapse; the object is NOT in the corpus.

## Framing caveat (not necessarily open physics)

Per sibling + `docs/audits/2026-07-26-g2-not-fitted-but-r-is-frame-artifact.md`: the deuteron is
separately closed to ~0.036% via fibre-level tiers, so `C_knot = 5.853` is likely a categorical
master-formula **normalization artifact**, and the honest resolution may be the fibre→archimedean
τ-transfer rather than any surface-term derivation. Weigh this before investing in the H₆-charge route.

## Next honest step

Either (a) construct the H₆-interface handle-commutator charge symbolically and check its
eigenphase-weighted trace against 5.853 (0-fit, derive-then-check), or (b) pursue the fibre→τ-transfer
normalization resolution. Do NOT re-attempt a scalar trefoil invariant — proved null.


## Progress Update (PR #8344)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`291dd36ab34a42866efb444b586e05f0b621971e` -> `38f4a86a95df28f43dea57e331b0e3b812f7f526`) in PR #8344.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8344, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
