---
# 2ti7
title: Drain 382 broken content-sibling .lean orphans (compile sweep 2026-06-28)
status: in-progress
type: task
priority: normal
created_at: 2026-06-28T16:49:39Z
updated_at: 2026-06-29T22:20:45Z
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

## 2026-06-29 wave-3 swarm (9 agents × 2 files, quantum-observable-universes next 18)

Continued the same chapter (re-derived: 18 fixed by wave-2, 45 remaining). Swarmed the
next **18** (reeb/torus/q-dilogarithm/q-exponential/frobenius-hopf cluster). Outcome:
**18/18 genuinely repaired, all independently re-verified `fail=0`** (parallel sweep), 0
flagged. Quality gate clean: no `: True`/`native_decide`/trivial-field; **0 new sorries**;
**axioms scrutinised** — `categorical-reeb-unique` axiom count 3→3 (pre-existing, cited
`[witten1988]`, §3b-cond external-axiom pattern), `q-dilogarithm` 2→1 (agent *reduced*
axioms; remaining cited `[manuscript]`) — no fabricated audit-dodges. Repairs: §7c
base-ring generalisation to `[Field R]`/`[LinearOrder R][IsStrictOrderedRing R]` where the
file used division/order on `R_q` (contact-affine-chart, heisenberg-commutator); inlined
faithful sibling-structure copies for out-of-scope `extends` (reeb cluster) cited
`[kock2004]`; type-correct monoidal Frobenius law (frobenius-hopf-substrate); `HEq` for
heterogeneous equalities; conclusion restated as honest `∃`-Prop (categorical-self-duality);
dead-`ring` / `No goals` cleanups. **27/63 of the chapter now drained across waves 2+3.**

## 2026-06-29 wave-4 swarm (9 agents × 2 files, quantum-observable-universes next 18)

Re-derived (36 fixed by waves 2+3, 27 remaining); swarmed next **18** (q-differential-geometry
+ `qou-exists-axiom-*` cluster). **18/18 genuinely repaired, all independently re-verified
`fail=0`**, 0 flagged. Quality gate clean: no `: True`/`native_decide`/trivial-field; 1 new
sorry, cited `[kassel1995] §IX` (valid key); **axioms IMPROVED** — `quantum-observable-universe-exists`
2→0 (replaced both axioms with one honest cited sorry), `q-logarithm-unique` 3→3 (pre-existing),
`qou-exists-axiom-2` 1→1 (pre-existing, axiom-by-design); no fabricated axioms. Dominant fix this
wave: the recurring **R_q-vs-ℝ base-ring mismatch** — many files recast to `R_q = LaurentPolynomial ℤ`
but consumed ℝ-valued `SubstrateParameter.field` / used `q⁻¹`/order on `R_q` (no Inv/order);
rewired to ℝ (archimedean realisation per §7c) or generic `[Field R]` where appropriate, importing the
canonical library module. Also `q-logarithm-exists` replaced a vacuous `∃…,True` with honest
`Nonempty`. **45/63 of the chapter drained across waves 2+3+4 (18 remain).**

## 2026-06-29 wave-5 swarm (5 agents, quantum-observable-universes remainder)

Re-derived the live-broken set FIRST (wave-1 lesson #1): of the chapter's 63
genuine.txt orphans, a fresh parallel `lean-verify-siblings.sh` sweep found
**54 already green** (siblings + the recent `fix(pre-existing)` main commits had
drained far more than the stale "45 done / 18 remain" count implied) — only **9
still broken**. Swarmed those 9 across **5 agents** grouped by root-cause family.
Outcome: **9/9 genuinely repaired, all independently re-verified `fail=0`**, 0
flagged. Committed in 2 commits (`8592abd3` = 7 files, `7b6545bb` = final 2).

The 9 + dominant fix:
- su2-emergence, variational-equations — stranded-docstring-above-`noncomputable
  section`; missing `import QOU.QuantumObservableUniverse.Structures` (universe
  params); inlined cross-sibling `SpinDecomposition`; section balance.
- substrate-parameter-planck, substrate-radial-coordinate — `unknown tactic`.
- weight-decomposition-exists, weight-decomposition — `Function expected` /
  `invalid binder annotation` (instance-bracket on a non-class).
- spectral-chart-correspondence, substrate-self-duality — top-level `λ` /
  stranded `/--` parse breakage from a malformed preceding declaration.
- u1-equivariant-reduction — `failed to synthesize` (§7c R_q-vs-ℝ base-ring trap).

Quality gate (orchestrator): vacuity scan clean (no `: True`/`native_decide`/
fabricated-axiom/trivial-field); 0 new sorries this wave; pre-existing cited
axiom `su2_emergence` (`[lusztig1993]`/`[deligne2007]`) left intact; §7c base
ring kept (`R_q = LaurentPolynomial ℤ`, no gratuitous ℝ cast). The
`quantum-observable-universes` chapter is now **fully drained** (all 63 genuine
orphans green on this branch).

**CI note:** PR #3142 `gate` + `content-sibling-compile` failed with the Actions
**billing signature** (≤4s, `runner_id: 0` no runner, 404 logs, empty output) on
both pushed SHAs — NOT a code defect (local lean-verify exit 0 on all 9).
Documented `[skip-ci: billing; local verify exit 0]` on the PR; no retrigger
pushed (billing doesn't clear on retry).

**Lesson reconfirmed:** re-derive-first is essential — the genuine.txt list is
now badly stale (mass-theory's "72" and the other chapter counts must be
re-swept before any wave-6, not trusted).

## 2026-06-30 wave-6 (mass-theory; re-derive → 1 live-broken, fixed directly)

Re-derived FIRST: of mass-theory's 72 genuine.txt orphans, a fresh parallel
`lean-verify-siblings.sh` sweep found **71 already green** (siblings) — only
**1 still broken**: `categorical-higgs-mechanism.lean`, the exact file wave-1
deliberately left broken (earlier swarm repair reverted for §3b-tax
proof-claims-unencoded trivial carriers). 1 file ⇒ fixed directly, no swarm.

Root cause: the two sibling-class field types (`CategoricalLinkingOperation`,
`WeinbergAngleCategorical`) had their imports commented out (out-of-Lake-tree
siblings can't be imported standalone) → auto-bound implicit → "Function
expected". Fix = wave-3 inline-faithful-copy precedent: inlined both sibling
classes verbatim-faithful (instances renamed to dodge the same-namespace
`canonical` clash); the 3 genuinely-proved linking properties keep real proofs
(ring distributivity / `pow_zero` / `neg_neg`), the open markers stay honest
`True` conjecture-skeleton placeholders (§3b-tax conjecture-block carve-out) —
NOT fabricated content. fail=0, 0 sorries, 0 new axioms. Committed `f4fae7a0`.

**Two chapters now fully drained** (quantum-observable-universes 63/63 + mass-theory
72/72). The genuine.txt list (382) is wildly stale — re-derive-first remains the
single most important lesson; do NOT trust the per-chapter counts.

## 2026-06-30 wave-7 (particle-interactions; 5-agent swarm + 2 direct)

Re-derived FIRST: of particle-interactions' 37 genuine.txt orphans, 24 already
green — **13 live-broken**. 5-agent swarm (3+3+3+2+2) + merged 9 new main commits
(r13f sibling drains) mid-wave. Outcome: **13/13 repaired, all re-verified fail=0**,
quality-gated (no vacuity/native_decide/fabricated axioms; 0 new sorries except none).

Dominant fixes: docstring-above-`noncomputable section` (quark/hadron/beta cluster);
import-only honest stubs collapsing shadowing duplicates → real library decls
(confinement-level-exists → QOU.BraidKnot.ConfinementLevel, nuclear-groebner-reduction
→ QOU.Archimedean.NuclearGroebnerReduction; dropped Lean-4-removed `constant`);
faithful inline copies of out-of-scope sibling structures (AtomKnot/StableAtom/
LocalizedKnot/isIsotope); §7c archimedean restatement to ℝ where genuinely
archimedean (beta-stability/skein A^{2/3} rpow + ordering, hadron masses).

Two finished directly after the swarm's 5th agent was interrupted by a session
resume:
- atomic-braid: theorem unprovable because A/totalStrands were default-valued
  FIELDS (independent data) → made them `def`s (derived) ⇒ identity definitional.
- per-nucleon-channel-decomposition: agent's in-flight transcription asserted a
  FALSE protonChannelSum=-h/2 (coded factors sum ≈15.9 at q=2, not -0.75). Rewrote
  per the .md table — explicit rational sym/alt; std channels (quadratic Δ₃ eigendata
  from def:typed-crossing-operator, not elementary) → channel-sum identities stated
  §3b-cond CONDITIONAL on the cited std closed form, verified non-vacuously by
  field_simp;ring; added a real branchingFactorizationSigns positivity proof.

**Three chapters now fully drained** (quantum-observable-universes 63, mass-theory 72,
particle-interactions 37 stale-listed / 13 live). CI billing persists across all
SHAs (2-4s, runner_id 0, no logs) — documented; hourly self-check-in armed for recovery.

PR #3142 (waves 5+6+7) MERGED to main (merge-commit 13cd2974) — included a post-merge
fix to categorical-higgs-mechanism (a bad earlier merge had declared the inlined
classes twice; dropped the leftover opaque markers, kept the faithful inlines, fail=0).

## 2026-06-30 wave-8 (predicted-spectra + brings-surface + information-theory + observations)

Next four chapters. genuine.txt lists 95 orphans (26 + 24 + 23 + 22). Per the
re-derive-first lesson, running a fresh `lean-verify-siblings.sh` sweep over all 95
on current main FIRST to find the actually-live-broken set before any fix (prior
waves found 70-95% already drained by siblings). Branch
`claude/2ti7-orphan-drain-wave8-2026-06-30`.
