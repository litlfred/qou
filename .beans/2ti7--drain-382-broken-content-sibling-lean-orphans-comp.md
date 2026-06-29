---
# 2ti7
title: Drain 382 broken content-sibling .lean orphans (compile sweep 2026-06-28)
status: todo
type: task
created_at: 2026-06-28T16:49:39Z
updated_at: 2026-06-29T13:00:00Z
---


## Context

Surfaced by the 2026-06-28 content-sibling compile sweep (PR #2974).
382 of 926 content-block `.lean` siblings (outside the `lean/` library
tree) genuinely fail `lean`-direct on `main` — pre-existing breakage
that escaped CI because these files are outside the `lake build QOU`
target.

- **Findings doc:** `docs/audits/2026-06-28-content-sibling-compile-sweep.md`
- **Genuine list (382, `file ||| first-error`):**
  `docs/audits/2026-06-28-content-sibling-compile-sweep.genuine.txt`
- **CI now prevents new drift** via `lean-content-siblings.yml` +
  `scripts/lean-verify-siblings.sh` (diff-scoped; the 382 are not
  retroactively blocked).

## Attack order
1. Shared `unexpected token 'section'; expected 'lemma'` template family
   first (one fix → many files).
2. Densest chapters: `mass-theory` (72) + `quantum-observable-universes`
   (63) = 135/382.
3. Elaboration-error tail (`failed to synthesize`, `Function expected`,
   `unknown tactic`, …) per-file.

Verify a fix with: `scripts/lean-verify-siblings.sh <file.lean>` (exit 0).

## 2026-06-28 finding — the `noncomputable section` family is NOT a mechanical drain (refuted)

Tested the leading hypothesis ("one template fix → many files green"). The
77 files with `unexpected token 'section'; expected 'lemma'` share a uniform
*parse* bug — a doc-comment stranded directly above `noncomputable section`
(the docstring can't attach to a `section`). The mechanical fix (move
`noncomputable section` above the docstring) clears the parse error AND the
cascade IR errors — **but greens 0/77 files.** Every file has deeper genuine
errors underneath:

- 18 `failed to synthesize` (missing instances — real API gaps)
- 21 deeper `unexpected token` (more parse breakage further down)
- 10 `Unexpected name … after end` (unclosed `noncomputable section` vs
  `end QOU` — a second structural bug, also uniform-ish)
- 6 `Function expected`, 5 `unsolved goals`, 3 `sorryAx is not a structure`,
  division on `R_q = LaurentPolynomial ℤ` (not a field → `q⁻¹`, `/(q−q⁻¹)`
  don't typecheck), type mismatches, universe errors.

**Conclusion:** these are genuinely incomplete formalizations, not a
cosmetic template defect. Draining them requires per-file Lean work and, in
many cases, a math-design decision (e.g. represent `q⁻¹` over the fraction
field of `R_q`, or `sorry`+`-- Ref:` the unproved parts) — which likely
wants author intent (repair vs honest-stub vs delete). The mechanical
`fix_ncs.py` transform is preserved in the session scratchpad but was NOT
committed (greened nothing). Next attempt should treat these per-cluster
with formalizer-level effort, not a sweep.

## 2026-06-28 finding #2 — dominant root cause: `R_q`-used-as-a-field (89/382)

Drained the **braids-and-knots** cluster (15 files) on branch
`claude/lean-orphan-drain-2026-06-28` (PR #2996). Outcome: **2 quick wins**
(`su2-basis`, `so3-generators` — section/`noncomputable`/codomain-ℚ fixes,
committed green) and **13 deep** files that the mechanical fixes do NOT green.

The 13 deep files share one systematic blocker, and a corpus grep confirms it
is the largest identifiable cause across the whole sweep:

- **89 of 382 genuine orphans** declare `abbrev R_q := LaurentPolynomial ℤ`
  (a `CommRing`) yet use **field/order ops over it** — `q⁻¹` (needs `Inv`),
  `/2` / `/(q−q⁻¹)` (needs division), `≤`/`<`/`positivity` (needs an order).
  None exist on `LaurentPolynomial ℤ`. The files were authored as if the
  ground ring were `ℚ(q)` / `ℝ`.

This is a **ground-ring decision**, not a mechanical fix (per §7c base-ring
convention the R_q-formal vs ℝ-archimedean distinction is load-bearing).
Options:
- (A) fraction field `RatFunc ℚ` — fixes `q⁻¹`, `/n`; ordering still absent.
- (B) archimedean `ℝ` — fixes all three but collapses the substrate/archimedean
  wall (§7c violation unless the quantity is genuinely archimedean).
- (C) per-file triage — q-independent rationals → `ℚ` (the su2-basis fix),
  archimedean numerics → `ℝ` (post-wall), formal q-algebra → keep `R_q` with
  `q_inv_param` for `q⁻¹` and no division/order. Most correct, slowest.

**Recommendation: (C), per-file** — it is the only option consistent with the
repo's base-ring discipline. su2-basis is the worked exemplar (Killing form is
q-independent rational → codomain `ℚ`). Needs author sign-off before a wide
pass since it touches ~89 files and makes per-quantity math judgments.

## 2026-06-29 wave-1 swarm (6 agents × 3 files, mass-theory first 18; olean cache restored)

Multi-agent swarm over 18 mass-theory orphans, each agent verifying with
`lean-verify-siblings.sh`. Outcome: **16/18 already-green** (sibling drains had
already fixed them since 2026-06-28 — the genuine.txt list is now VERY stale),
**1 genuine repair**, **1 rejected on quality review**:
- ✅ `crystal-r-matrix-sub-lemma.lean` — REPAIRED + committed. Removed a vacuous
  `hA.identity_holds ∨ True` theorem + empty `identity_holds : Prop` carrier;
  added the real §3b-cond `CrystalGraphRealization` class (content-bearing field
  `crystal_realises : ∀ T i, raising i (nodeOf T) = none`). lean-verify fail=0.
- ❌ `categorical-higgs-mechanism.lean` — agent's repair REVERTED (not committed).
  It greened the file but via UNDER-SPECIFIED carriers: `linkingAdditive : ∀ k₁ k₂
  : ℤ, k₁+k₂=k₂+k₁` is integer commutativity (docstring claims linking-additivity
  `Lk(k₁+k₂)=Lk(k₁)+Lk(k₂)`) → §3b-tax `proof-claims-unencoded`; `mixingNormalised
  : ∃ c s, c²+s²=1` trivially (1,0). Left broken for a proper author/formalizer
  repair (the missing classes must encode REAL content).

**Process lessons for the next wave:** (1) RE-DERIVE the broken set from CURRENT
main before swarming — 16/18 were already green, so most of the ~500k swarm tokens
confirmed sibling work; a fresh `lean-verify-siblings.sh` sweep over the chapter
first would target only live breakage. (2) Swarm output MUST be quality-gated by
the orchestrator (the §3b-tax vacuity check caught the categorical-higgs
trivial-field repair the per-file verifier passed — compile-green ≠ honest-content).

## 2026-06-29 wave-2 swarm (9 agents × 2 files, quantum-observable-universes; live-set re-derived)

Applied wave-1 lesson #1: re-derived the live broken set first (git filter — 0 of the
chapter's 63 orphans were modified on main since 2026-06-28 ⇒ all still broken;
spot-verified). Swarmed the first **18**. Outcome: **18/18 genuinely repaired, all
independently re-verified `fail=0`** (parallel `lean-verify-siblings.sh` sweep), 0
flagged — 100% yield (vs wave-1's 1/18 live). All committed. Quality gate (orchestrator):
vacuity scan clean (no `: True`/`native_decide`/fabricated-axiom/trivial-field); 2 new
sorries both cited (`[kassel1995]`, valid `references.ts` keys); diff-wide grep clean.
Highlights: `braiding-induced-ordering` (real `WellFounded` proof via `Subrelation.wf`,
no sorry); `categorical-coordinate-ring` REPLACED a fabricated `axiom …_universal_axiom`
audit-dodge with the real theorem + one honest cited sorry; the rest were import-scoping /
`noncomputable section`-docstring / `end`-balance / type-correct-composite repairs with
content preserved. **Re-derive-first works** — wave-3 should continue per-chapter the same way.
