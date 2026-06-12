# Fluid-dynamics proof-statement-integrity — disposition audit

**Date:** 2026-06-12
**Branch/PR:** `claude/proof-rater-integrity-fixes-2026-06-12`
**Scope:** the `proof-statement-integrity = fail` backlog surfaced by the
proof-rater baseline (#1939) and re-flagged by the qa-drain rounds
(#1918/#1941, criterion `proof-narrative-lean-equiv`).

## Why this doc exists

The integrity backlog was scoped as "replace `True`-stubs with the real
one-line statement." On inspection that premise is wrong, and the fix is
deeper. This doc records the corrected finding and the per-cluster
disposition so the work is auditable and resumable.

## Finding 1 — the flagged `.lean` is a *sibling stub*, not the canonical decl

Each content-block `<block>.lean` under `fluid-dynamics/` is a
**sibling-resolution stub** (`theorem X : True := by trivial`) whose
docstring points to the buildable declaration in the **library module**
under `content/quantum-observable-universe/lean/QOU/…`. Example:
`observability-q-independent.lean` →
`QOU/GaugeFieldFluidDynamics.lean:741`. The integrity rater scored the
stub (which is vacuously `True`), so part of the backlog is a
**measurement artifact** (the canonical decl was never read).

**Implication:** any integrity re-rating must read the *canonical*
declaration named in the stub docstring, not the stub.

## Finding 2 — the canonical decls are the *context-class projection* pattern

Reading the canonical library decls, they are not faithful encodings.
They are the **self-assuming projection** pattern: a `class XContext`
carries the claim as a *field*, and the "theorem" projects it. Example
(`QOU/FluidDynamics/q_bkm_criterion.lean`):

```lean
class QBKMContext where
  extendsSmoothly : Prop
  vorticityIntegralFinite : Prop
  claim_bkm_iff : extendsSmoothly ↔ vorticityIntegralFinite   -- the claim, as a hypothesis
theorem q_bkm_criterion [ctx : QBKMContext] :
    ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite := ctx.claim_bkm_iff
```

The predicates are **abstract opaque `Prop`s**, and the proof assumes the
conclusion. This is *not* a valid §3b-cond conditional-class result (which
must axiomatise a genuine conjecture and *derive* a conditional
consequence) — the class field **is** the conclusion. The integrity fail
is therefore **legitimate**: the Lean does not encode the `.md`'s
mathematical content.

`observability_q_independent` is the same shape: the `.md` claims
`Hom_{C_{q₁}}(1,Ad A) = Hom_{C_{q₂}}(1,Ad A)`, but the Lean concludes
`obs.hom_rank = 0 := obs.observable` with the `q₁,q₂` arguments unused.

## Finding 3 — the chapter is open-NS-problem claims typed as `proposition`

Navier–Stokes global regularity is open (a Millennium problem). The
fluid-dynamics chapter states many results about it as `proposition`s
whose `.lean` is a conjecture-class. Three are direct kind-mismatches
(`.ts` = `proposition`, `.lean` = conjecture-class):

| block (file) | label | `.lean` | genuinely conjectural? |
|---|---|---|---|
| q-aubin-lions | `prop:q-aubin-lions` | `class QAubinLions` (docstring labels it `conj:`) | yes (compactness as q→1) |
| p2-critical-exponent | `prop:critical-exponent` | `class CriticalExponent`; `uses` **`conj:regularity-breakdown`** | yes (already downstream of a conjecture) |
| p5-counterexample | `prop:ns-counterexample` | `class NSCounterexample` | yes (NS counterexample) |

Per §3b, a `proposition` may not sit downstream of a `conj:` unless it
satisfies §3b-cond. `prop:critical-exponent` already violates this
(`uses: ["…","conj:regularity-breakdown"]`).

### §3b cascade map (why this is not 3 isolated fixes)

Demoting these to `conjecture` (the honest kind, matching the `.lean`)
renames `prop:` → `conj:` and **propagates** to provable-kind users:

```
prop:ns-counterexample  ─used-by→  prop:q-aubin-lions (prop), p5 self
prop:q-aubin-lions       ─used-by→  prop:vorticity-lower-bound (prop)
prop:critical-exponent   ─used-by→  prop:p4-universality (prop)
```

So `vorticity-lower-bound`, `p4-universality` (both propositions) become
downstream of conjectures and must themselves demote or adopt §3b-cond.
Each label is additionally cross-referenced in ~12–18 `.md`/index files
(`definition-index.md`, several `appendix-surreals/*`, intra-chapter
prose) that need link updates on any rename.

## Cluster summary — 13 fluid-dynamics integrity fails

| Cluster | Count | Blocks | Disposition |
|---|---:|---|---|
| Projection of abstract `Prop`s (NS-PDE) | 9 | q-bkm-criterion, ns-obstruction-computation, ns-obstruction-tower, ns-singularity-descartes, ns-kummer-specialisation, leray-profile, p1-nonlinear-uniqueness, p1-spectral-sobolev, p4-universality | honest relabel + documented abstract-predicate caveat; real formalization is research-grade (tracked) |
| Degenerate projection w/ simple real claim | 1 | observability-q-independent | **faithfully formalizable** — state q-independence of the Hom space directly |
| Kind-mismatch (prop vs conjecture-class) | 3 | q-aubin-lions, p2-critical-exponent, p5-counterexample | demote `proposition → conjecture` (or §3b-cond), handle cascade |

The remaining 16 integrity fails (predicted-spectra 9, quantum-observable-universes 6,
mass-theory 1) showed the same family (weakened proxies, unsound
`Subsingleton` axioms over free reals, missing decls) and are triaged in a
follow-up pass.

## Finding 4 — the integrity fail is the *degenerate* sub-case of an otherwise-blessed pattern

Running the repo's own `conjectural-propagation-audit.ts` on current main is
decisive: **140 provable-kind blocks are reported "Conditional-on-class
(eligible under §3b-cond)"** — i.e. the conjecture-class pattern is the
*accepted* honest form for open-problem content, **not** a violation. A
blanket `proposition → conjecture` demotion would therefore fight the
framework and trigger a needless chapter-wide cascade.

The two criteria encode different standards, and both can hold at once:

| criterion | what it checks | verdict on these blocks |
|---|---|---|
| `conjectural-propagation` | is the conjectural cone *class-axiomatised*? | **OK** (conditional-on-class) |
| `proof-statement-integrity` | does the Lean *derive* the `.md` claim (vs assume it)? | **FAIL** (degenerate projection) |

A valid §3b-cond block axiomatises the conjecture's **hypotheses** and
*derives* the result; the integrity fail is the **degenerate** sub-case where
the class field **is** the conclusion (`claim_bkm_iff`, `obs.observable`), so
the theorem derives nothing. The fix is therefore **per-block formalization
judgment, not mechanical demotion.**

## Disposition plan (this PR) — revised after Finding 4

1. **Do NOT blanket-demote.** The conjecture-class pattern is blessed; only
   genuine kind-mismatches (`.ts` provable kind with **no** Lean theorem at
   all, only a bare conjecture-class — `q-aubin-lions`, `p2-critical-exponent`,
   `p5-counterexample`) are demotion/§3b-cond candidates, and each needs the
   owner's call on demote-to-`conjecture` vs add-a-conditional-theorem
   (both have cascade/▢propagation cost).
2. **Tractable faithful fix, no cascade:** `observability-q-independent` —
   its `.md` proof is real (the Hom space is computed in `C`, independent of
   `q`). Replace the `hom_rank : ℕ` proxy with a statement that the Hom
   object is the *same* across `q₁, q₂` and prove it; kind stays `theorem`.
   Lean-gated (verify with `lake build QOU`).
3. **Make conditional-class theorems non-degenerate where feasible:** move the
   conclusion out of the class field; have the class carry genuine hypotheses
   and the theorem derive the `.md` claim. Research-grade for the NS-PDE
   blocks (Sobolev/L^∞ infra) — tracked as a separate effort; attempt the
   most tractable as an exemplar.
4. **Honest re-rating** of blocks where (2)/(3) land: re-run the rater so
   `proof-statement-integrity` reflects the improved Lean, with written
   rationale. No vacuous "faithful" Lean is manufactured to game the score.

**Note (audit-script bug, out of scope):** `conjectural-propagation-audit.ts`
crashes while printing the *Violators* section on current main (Bun trace from
the violator `console.log`/witness-write). The conditional-on-class tally
(140) prints fine. Filed for a separate fix; does not affect this disposition.

## Fix recipe (verified on `q-bkm-criterion`, 2026-06-12)

Each NS block has up to two defects; both are mechanical once seen
(`q_bkm_criterion` done end-to-end, `lake build -R … q_bkm_criterion` exit 0):

1. **Build.** The module has no imports → `ℝ`/`ℕ` unknown → it never
   compiled (and reds `QOU.lean`, which imports it). Add the **generic**
   `import Mathlib.Algebra.Ring.Defs` (provides `CommRing`). Do **not** use
   `QOU.Shared.SobolevHkRegularity` — it transitively imports
   `Mathlib.Data.Real.Basic` (`ℝ`), violating §7c.
2. **Integrity.** The class carries the conclusion as a field
   (`claim_… : A ↔ B`) and the theorem projects it (`:= ctx.claim_…`) —
   self-assuming. Restructure: the class carries the genuine sub-hypotheses
   (e.g. the two iff directions); the theorem **derives** the headline
   (`⟨ctx.dir₁, ctx.dir₂⟩`). This is §3b-cond **condition 5** (non-degenerate).
3. **Base ring (§7c).** Generic `{R : Type*} [CommRing R]`, never `ℝ`. Drop
   archimedean setup hypotheses the statement does not use (`0 < T`, `1 < q`);
   they belong to a post-wall `ℝ`-specialisation.
4. **Verify + re-rate.** `lake build -R QOU.FluidDynamics.<module>` exit 0
   (per-module — `lake build QOU` is red on ~50 pre-existing failures and is
   not the gate), then re-rate `proof-statement-integrity` via `qa-agent-write`.

Agent guidance updated to match: CLAUDE.md §3b-cond (condition 5 + base-ring
note) and `local/lean-proof-review.md` Review Type 4.

**Env (durable this container):**
`export PATH="$HOME/.elan/toolchains/leanprover--lean4---v4.24.0/bin:$PATH"`;
do **not** set a `git url.*.insteadOf` redirect (it re-triggers a destructive
mathlib re-clone). `PosSemidefTraceZero` + `HeckeAlgebra/Formal` are confirmed
green on current main (the old-base red is gone).

## Progress ledger (2026-06-12)

| block | build | integrity | base ring | notes |
|---|---|---|---|---|
| q-bkm-criterion | ✓ exit 0 | ✓ pass | generic `CommRing` | iff derived from 2 directions |
| p4-universality | ✓ exit 0 | ✓ pass | generic types (no ring) | independence derived from factoring |
| ns-obstruction-tower | ✓ exit 0 | ✓ pass | generic `CommRing` | `res_Σ` → `res_sigma` (Σ reserved token; old file never parsed) |
| ns-singularity-descartes | ✓ exit 0 | ✓ pass | generic `CommRing` + `ℤ` | `NS_A ≠ 0` derived from `χ = −6` |
| ns-obstruction-computation | (this batch) | (this batch) | generic `CommRing` + `ℤ` | both iffs derived from 4 directions |
| ns-kummer-specialisation | (this batch) | (this batch) | `ℤ`/`ℕ` only | **(i), (ii) proved outright** — (i) contrapositive of (iii); (ii) from `χ ≠ 0` via `Int.le_of_dvd` |
| leray-profile | (this batch) | (this batch) | generic `CommRing` | stale `BigOperators.Basic` import fixed; reconstruction derived from ansatz + normalisation |
| p1-spectral-sobolev | (this batch) | (this batch) | generic `LinearOrderedField` | (a) derived from (b) + q-integer monotonicity |
| p1-nonlinear-uniqueness | (this batch) | (this batch) | `ℝ` (**§7c-justified**: `Real.exp`, Gronwall order) | (c) uniqueness derived from distance Gronwall bound |
| observability-q-independent | pending | pending | TBD (generic) | faithful fix in `GaugeFieldFluidDynamics.lean` — q-independence provable by `rfl` once the Hom-rank construction genuinely omits `q` |

**Follow-up (narrative side, §3b-cond condition 3):** several of these
blocks' `.md` files state the result unconditionally (e.g.
`q-bkm-criterion.md`); per the owner's directive the narrative should also
read "if ⟨hypotheses⟩ hold, then …" — add the conditional banner naming the
context-class hypotheses. `p4-universality.md` already has the banner; the
remaining 8 are a small `.md`-only follow-up batch.

## Coordination

- qa-drain r6 (#1941) flags several of these (`ns-singularity-descartes`,
  …) under `proof-narrative-lean-equiv` but **records verdicts only**;
  fixing the Lean statement here resolves both that and
  `proof-statement-integrity`. A note will be posted on #1941 so the
  `.qa.json` re-rating does not collide.
- No open PR is fixing fluid-dynamics statement integrity.
