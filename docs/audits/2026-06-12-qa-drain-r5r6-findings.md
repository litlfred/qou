# QA agent-drain (rounds 5–6) — harvested findings & supersession audit

**Date:** 2026-06-12
**Author:** agent session (claude-code)
**Scope:** post-mortem of the corpus-wide QA agent-drain rounds 5–6 (PRs #1918, #1941),
plus a *verified* harvest of the substantive FAIL findings worth acting on.

---

## 1. Why r5/r6 are superseded (close, do not rebase)

The agent-drain rounds 5 (#1918, 519 verdict commits) and 6 (#1941, 88 verdict
commits, stacked on #1918) were opened off `main` at `e8145c2e` (2026-06-06) and
capped/continued through 2026-06-07. By 2026-06-12 they are obsolete:

| Signal | Measurement |
|---|---|
| `main` advanced since the merge-base `e8145c2e` | **933 commits** (6 days) |
| `.qa.json` files changed on `main` since merge-base | **2147** |
| r6 verdict files that **also** changed on `main` (collision set) | **88 of 88 (100 %)** |
| QA schema / criteria / checker changes on `main` | see below |

**QA infrastructure drifted** — the drain wrote against a now-outdated contract:

- `feat(qa): wall-base-ring-minimal` — **new criterion** the drain never evaluated.
- `feat(qa): section-title coherence audit` — **new criterion** the drain never evaluated.
- `feat(qa): rater-rubric QA framework` + `proof-rater write-path (--score)` (merged
  #1939) — a new **scoring** dimension the drain predates.
- `qa: persist checker metrics payload into block-qa sidecars` — **sidecar schema change**;
  the drain emitted the *old* shape.
- `merge … resolve 143 .qa.json conflicts (proof-rater graft)` — `main` already
  reconciled sidecars en masse.
- `chore(qa-sweep): refresh N sidecars after checker-version drift` — checker
  versions bumped, so drain verdicts now read as stale on arrival.

**Conclusion:** rebasing 607 hand-written verdict commits onto current `main` would
produce hundreds of conflicts and old-schema output that is **strictly inferior** to
re-running the current `qa-sweep` + `qa-agent-drain` tooling on `main`. The verdict
*sidecars* are re-derivable and not worth salvaging. **The only non-re-derivable value
is the substantive FAIL findings below.**

---

## 2. Verified findings (re-checked against current `main`, 2026-06-12)

These were flagged by drain workers and **spot-verified to still hold on current
`main`**. They are real, model-independent, and actionable.

### 2.1 — PRIORITY: likely Lean build-breaker

**`mass-theory/prop-rigid-monoidal-structural-gap-invariance.lean`** — the file
declares **`instance canonical` twice** (lines 238 and 324) and
**`theorem structural_gap_convention_independent` twice** in the same namespace, plus
several `sorry`s (lines ~204, 217, 290, 303). A duplicated `instance`/`theorem` in one
namespace is a hard Lean error (`'canonical' has already been declared`), so this file
very likely **does not compile**. Recommended fix: delete the duplicated second block
(keep one `instance canonical` + one `theorem`), preserving the §3b-cond conjectural
`sorry` that is legitimately allowed.

### 2.2 — `proof-narrative-lean-equiv`: Lean concludes `True`/repackages hypotheses while the narrative asserts a substantive claim

| Block (`.lean`) | Current Lean conclusion | Narrative claims |
|---|---|---|
| `fluid-dynamics/p4-universality` | `theorem universality_conditional … : True := trivial` | α = 4/3 critical-exponent universality |
| `fluid-dynamics/ns-singularity-descartes` | `theorem ns_singularity_descartes : True := by … trivial` (docstring admits placeholder) | NS-singularity ⇒ Descartes blow-up obstruction |
| `appendix-surreals/surreal-squeeze` | `theorem surreal_squeeze_conditional … : 0 < ε ∧ ε < 1 := ⟨h_pos, h_inf⟩` (repackages hypotheses) | δ²·ε⁻¹ > ε³ surreal squeeze |

All three use the §3b-cond conditional-class pattern (classes as `[Instance]`
hypotheses), which is sanctioned — **but the theorem *conclusion* is vacuous** (`True`
or a tautological repackaging), so the Lean does not encode the narrated result. The
fix is to make the conclusion state the actual identity/inequality (still conditional
on the classes), not `True`.

### 2.3 — Superseded by `main` (do NOT re-file)

| Block | Drain finding (2026-06-07) | Current `main` |
|---|---|---|
| `mass-theory/spectral-sequence-collapse` | "Lean only proves `e*e=e` idempotency" | **Developed**: now `class SemisimpleAlgebra`, `class WhiteheadHH` (`-- Ref:[cartan1956]`), real `innerDerivation` (`simp;ring`), `theorem spectral_sequence_collapses_to_centre`, `wedderburnWeight`/`plancherelWeight`. Finding is stale. |

---

## 3. Unverified snapshot candidates (re-check before acting)

These were flagged by drain workers at the 2026-06-06/07 snapshot but **were NOT
re-verified against current `main`** (where 933 commits — including Lean axiom→theorem
discharges and mass-theory development — may have resolved some). Treat as leads, not
facts; grep current `main` before filing.

**`proof-narrative-lean-equiv` stub candidates:** `appendix-surreals/collatz-no-cycles`
& `collatz-contact-boundary` (lean.ref → `…_conditional : True := trivial`),
`braids-and-knots/zeta8-witness-level2-su2` (`wenzl_annihilator_at_zeta8` proved `∃x,x=0`
via `⟨0,rfl⟩`), `mass-theory/terms-2-6-higher-operations` (`True := trivial`; narrative
is *explicitly* an unproven sketch, so arguably acceptable),
`mass-theory/mass-tower-coefficient-stratification` (`∃ depth, depth = stratumDepth`
skeleton), `mass-theory/q-beta-c-k-recursion-from-habiro-q-difference` (recursion
*engine* encoded, recursion *claim* unconstructed).

**`voice-statement-no-interpretation` (interpretation / exploration-log inside a
statement block, no companion `interprets:` remark):**
`mass-theory/terms-2-6-higher-operations` ("CORRECTION 1/2", "TESTED, FAILS"),
`observations/substrate-consistency-window` ("would falsify the framework"),
`mass-theory/rho-k-h3a-refinement`, `mass-theory/qbeta-c8-c10-silver-rationals`,
`mass-theory/q-beta-c3-hopf-three-fold-markov` ("formalizes the Track C direction" +
`## Status`/`## Open`), `information-theory/q-gaussian-solves-q-heat`,
`molecular-construction/co-lp-dual-binding`,
`stochastic-mechanics/joint-galois-braid-discharged`,
`fluid-dynamics/p3-blowup-yekutieli`.

**`wall-side-*` (numeric q₀≈1.11 / MeV in a generic-chapter statement, no §7c banner):**
`mass-theory/partition-sum-proton-residual` (q₀/MeV/CODATA hard-coded + `nlinarith` on
ℝ literals, no banner — flagged major).

---

## 4. Recommended forward path

1. **Close #1918 and #1941** as superseded (this audit is the record).
2. **Act on §2** (verified): fix the `prop-rigid-monoidal` duplicate-instance build
   break first; then promote the three §2.2 vacuous-conclusion theorems to state their
   actual results (still conditional on their classes).
3. **For continued QA-drain**, restart off **current `main`** with the **current**
   tooling (`qa-sweep` + `qa-agent-drain-queue` now include `wall-base-ring-minimal`,
   `section-title-coherence`, and rater `--score`) rather than the 6-day-old approach —
   and lean on `main`'s automated `qa-sweep` for the mechanical sidecar refresh, reserving
   agents for the genuinely-judgement criteria.
4. **Re-verify §3 leads** against current `main` (corpus-grep discipline) before filing
   any as open issues — several flagged blocks were developed on `main` since the snapshot.
