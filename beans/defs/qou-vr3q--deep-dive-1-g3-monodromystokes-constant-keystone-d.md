---
# qou-vr3q
title: 'Deep-dive 1: G3 monodromy/Stokes-constant keystone — derive A_ω (odd-face Q_β/Φ_b) as GGM 3d-index integer count'
status: todo
pr: 8277
type: task
priority: high
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T17:08:37Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-avtq
---

CORRECTED FRAMING (2026-07-18): A_ω≈3.8884 (=4√2·e^{-3/8}) is the EVEN-face, q=1 BINDING-period Stokes constant (co-equational, bar-even, binding a_D only) — NOT the odd-face keystone. Do not conflate.

G3 keystone = the bar-ODD (Q_β/Φ_b) monodromy datum z(q0)→S whose archimedean eval must reproduce S(muon)=+0.00968298, S(proton)=-0.03945936. UN-MEASURED. It is a categorical Stokes/monodromy datum (irregular q-difference connection), NOT a resummation constant.

Derivation candidate (not fit): the exact GGM 4₁ Stokes matrix integer 3 (S⁰=[[1,0],[-3,1]]), singularity at ω=Vol(4₁)/π≈0.646. computations/probes/qbeta_g3_ggm_stokes_41.py certifies det W_m=2, q-diff eq 49, eq-59a sandwich EXACT. Open 'step 3': identify that integer's substrate eval with Im 𝔙→N_odd (falsifiable). Trace-field H1 (qou-t3jv): Stokes -3 = disc(ℚ(√-3))=-3 unifying even(√3)/odd(√-3) via ℚ(ζ12) — NOT verified.

Lean scaffold ALREADY present: CyclicDilogPentagon.lean faddeevPhi_unique_of_pentagon (sorry-free), MonodromyDatumRigidity.lean monodromy_datum_rigidity (sorry-free) ⇒ A_ω carries NO fitting freedom IF pentagon holds. SINGLE open input = PentagonRigidity.uniqueUpToScalar (Faddeev-Volkov 'doubly-periodic⇒constant' Liouville step, Mathlib gap, no instance).

FORMALIZE-FIRST target: prove PentagonRigidity (Liouville step) → discharges uniqueness leg, converts G3 from 'find a function' to 'verify pentagon pins the proved inversion/unitarity/self-duality bundle'. k=21 singularity now CONFIRMED structurally unresolvable by fixed-order Borel-Leroy through k=31 (gap persists 0.172); needs Φ_b state-integral/GGM route. Full memo: docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md

---

## 2026-08-11 TAKEOVER + status refresh (this bean was stale; owner-authorised takeover of the stalled leg)

Last A_ω commit was 10 days prior (`caf115a24`); substantive work 3 weeks prior. Owner authorised takeover. On takeover the leg is verified worked to its genuine research frontier — every tractable sub-step below is ALREADY LANDED. The three claims above are superseded:

1. **Uniqueness leg CLOSED (sorry-free), NOT "single open input = PentagonRigidity Mathlib gap".** `MathlibExt/DoublyPeriodicLiouville.lean` proves the "doubly-periodic entire ⇒ constant" Liouville step from Mathlib primitives (no longer a carried hypothesis). Uniqueness is discharged sorry-free via the regularity-carrying `FaddeevPhiPhysical` (`QBeta/FaddeevPhiFullUniqueness.lean`, `faddeevPhi_uniqueUpToScalar`, class fields `hStripGrowth` + `hNF : MeromorphicNFOn`). The abstract-`FaddeevPhi`-ratio route (beans qou-cons/qou-rp5f) hit a real wall — the bare class has no regularity field (`faddeevPhi_mul_latticeIndicator` witnesses closure under pathological doubly-periodic multipliers) — and is superseded by the `FaddeevPhiPhysical` route.

2. **Trace-field H1 REFUTED, not "unverified".** Reading GGM 2012.00062 directly, the 4₁ off-diagonal DT spectrum is the PAIR {3,4} (eq 98); the co-occurring 4 has no discriminant meaning, so `Stokes -3 = disc(ℚ(√-3))` is refuted (scope-(a), `docs/audits/2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`). Do not resurrect.

3. **`A_ω=3` conditional adoption LANDED.** `mass-theory/aomega-fourone-dt-count.md` (Theorem conditional on `conj:stokes-dt-bps-bridge`); value 3 from the sorry-free decidable `QOU.QBeta.StokesQZeroDTCount` (eq-60 `S⁺(0)=[[1,3],[0,1]]`); bridge asserts no value. Passed the non-degeneracy gate on the CLOSED GPPV/GGM sector; the OPEN-HOMFLY Gukov–Stošić sector (`det(4₁)=5 ∉ {3,4}`) was correctly rejected. Symmetry-constant-vs-spectrum fork RESOLVED against a universal scalar by the 5₂ cross-knot test (`FiveTwoDTSpectrumSplit.lean`, sorry-free): 5₂ chiral, 3×3 block splits {3,4} across chirality — the real fork is which spectrum member the observable inherits via chirality.

**REMAINING OPEN PIECE — literature-open, NOT a QOU wiring gap (honest terminus).** The internal derivation of the q→0 3d-index DT count from QOU Hecke/Bring data (Wedderburn mult of H_n(q), Markov-trace, Bring embedding) reproducing S⁺(0)₁₂=3 for 4₁ AND the companion 4 / surviving the 5₂ test is an **open problem in the categorification of DT / 3d-index invariants — open in the DT/state-integral literature itself** (per `2026-08-02-aomega-internal-derivation-symmetry-constant-target.md` §B). Recomputing the q→0 index "internally" via the QOU colored Jones / state integral IS re-importing GGM, not a categorical shortcut. Until such a formula exists, `A_ω=3` is certified-as-GGM-DT-count (imported, proven-for-4₁, conditionally adopted) but NOT internally derived; claiming a closure would violate the anti-laundering rule. Consolidated frontier map: `docs/audits/2026-08-11-g3-and-qdifference-slope-frontier-consolidation.md`.

Status left `in-progress` (not `done`): the QOU-actionable content is exhausted, but the naming leg (internal derivation) is a genuine open problem — closing it is a human/owner call, not an agent's, and it awaits a literature advance in DT categorification.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open: an internal derivation of 3 is literature-open. Correct item 2: eq (98) is the 5₂ matrix, so "a 4 co-occurs for 4₁" is false. H1 is refuted only conditionally, via 9f527376. The adopted block must not say GGM proved Conj 3.

Evidence: Lean: `MathlibExt/DoublyPeriodicLiouville.lean` and `QBeta/FaddeevPhiFullUniqueness.lean` contain no `sorry`/`axiom` tokens. They are not compiled here because Mathlib oleans are absent. `StokesQZeroDTCount.lean` uses `decide` on 2×2 data. Item 2 ("H1 refuted, 4₁ spectrum {3,4} eq 98") rests on the misattribution. Item 3's adopted block overclaims Conj 3 (finding 3).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Round 55 Implementation Progress (PR #8277)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8277 (head `8f4f568482d5a937ac700b4605cc7c48271faae8`, Commit 1 `0a62bee9d3e501101e220bcafa8c3a9fee1d0d25`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/StokesMonodromyGGMSandwichAndTrivialFlatConnection.lean` (`ggm_unipotent_sandwich_invariance`, `four_one_vs_five_two_dt_spectrum_split`)
- **80-dps Witness:** `computations/probes/round55-tau-loop-markov-nucleon-stokes-monodromy.witness.json` (`scriptHash: 1de39a3b3d7c`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8277, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-07-18: "vr3q T1: hspan CLOSED — period lattice basis from b²∉ℝ (lean exit 0)"). The work may be partly or fully done. Read the bean before you close it.
