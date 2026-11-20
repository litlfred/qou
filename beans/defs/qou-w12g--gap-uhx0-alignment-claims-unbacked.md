---
# qou-w12g
title: 'GAP: epic qou-uhx0 completion claims (qou-2och, qou-lm62) are not backed by artifacts on main'
status: todo
type: task
priority: high
created_at: 2026-11-20T09:00:00Z
updated_at: 2026-11-20T16:10:00Z
parent: qou-uhx0
---

Found by W12 (session_01VQDpPfS7H7LVPj21tEhkK3) while auditing epic `qou-uhx0`, `main` 917b69399.

1. `qou-2och` (status completed) names `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` (872 lines), an 80-dps probe, and an alpha_crit = q_0 result. None exist; `alpha_crit` occurs nowhere in `folio/`.
2. `qou-lm62` (status completed) claims a 71-entry glossary with 0 Lean refs and a Z = 1..118 table. The tree has 32 glossary blocks, 8 with `lean:` refs; no 118-row table found.
3. `qou-blf1` had the same pattern (resolution naming a nonexistent file); fixed by PR #8537.

Open, and what would close it:
- H_3(q) / n = 4 Bokut-Shiao GS confluence for the nuclear Hecke reduction: existing related Lean is `UGB/GrobnerShirshov/HeckeGS.lean`, `HeckeCompletion.lean`, `LocalConfluenceRefutation.lean`, `QOU/TransferMatrices/GSNormalForm.lean`, `QOU/Archimedean/NuclearGroebnerReduction.lean`. Nobody has checked what they already prove against the 2och statement; that comparison is the first step.
- alpha_crit = q_0: anything that derives q_0 is forever gated (owner 2026-08-02). A statement that only *evaluates* a threshold at the CAL-2 pin is not gated, but its exact content was never written down. Needs an owner-scoped statement before anyone works it.
- The GPMT radical separation part of 2och: no artifact found; unscoped.
- Whether 2och / lm62 should be set back from `completed`: owner decision (asked on #8526).

## Step 1 done (W12, 2026-11-20): what the corpus already has for the qou-2och GS claims
- **n = 4 Bokut–Shiao overlap**: settled. `UGB/GrobnerShirshov/HeckeGS.lean` refutes that {Hecke, Yang–Baxter, far-comm} is a GS basis (`NotAGSBasis.hecke_not_gs_basis_four`); `HeckeCompletion.lean` (bean qou-auq3) adds the Bokut–Shiao family and proves `heckeCompleted_isGrobnerShirshovBasis` for every n, axiom-free.
- **Unique normal forms**: hold modulo the Diamond-Lemma axioms. As of PR #8582 (bean qou-2q7r) `reduction_well_founded` is a theorem; the one remaining axiom is `local_confluence` (CompositionLemma.lean:83, Bergman §3 Thm 1.2, needs unit lc). Discharging it is the real open GS item.
- **Block-ordered nuclear Hecke-only reduction**: `QOU/TransferMatrices/GSNormalForm.lean` proves the block step and the irreducibility of chain monomials; its own "Honest scope" lists three missing pieces (no H_A(q) construction, no confluence, no global block-locality induction). Open.
- **Content defect found**: `nuclear-interactions/nuclear-groebner-reduction.md` states that G = {Hecke, Yang–Baxter, far-comm} IS the GS basis of H_A(q) with unique normal form. That is false for A ≥ 4 by the sorry-free refutation above; the correct G is the Bokut–Shiao completion. Raised as `[W12 ask]` on #8526 (content edit to a proposition statement).
- alpha_crit = q_0 and GPMT radical: still no artifact; unscoped.

## Same pattern in other beans (measured 2026-11-20)
Beans set to completed by the local commits e223ed1 / 4fcd2cb / 89bb5e0 on `cat/cat-harness/beans` (2026-11-19, `litlfred@fenugreek.home`) whose named Lean/probe/witness files are absent from main and every branch and PR: qou-2och, qou-7ypv, qou-bgq9, qou-iw1d, qou-l4t2, qou-ozdk, qou-qssg, qou-qvpl (work existed on PR #8149, closed unmerged), qou-txc1, qou-y7ek, qou-ys29 (also #8149), qou-7vhp (partial: `roundtrip-blind-packets.ts` absent), qou-rgj8 (one file). qou-2och and qou-lm62 reopened on owner instruction; the rest left as they are pending the owner.
