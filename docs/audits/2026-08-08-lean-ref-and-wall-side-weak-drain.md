# Broken `lean.ref` taxonomy corrected, and the WEAK-33 classification validated

**Date:** 2026-08-08
**Scope:** follow-up drain on the two queues left open by #4712 and #4709.
**Beans:** `qou-z3k1` (triviality sweep), wall-side WEAK queue.

Two queues were handed over: the 34 broken `lean.ref` from #4712's corpus-wide
triviality sweep, and the 33 WEAK `wall-side-correct` blocks from #4709. This
records what draining them actually found — including a place where the
handover's own taxonomy was wrong.

## 1. The broken `lean.ref` count is 33, not 34

`skip_reasons.decl-not-found` reports **34**; the `skipped_decls` map contains
**33** distinct declarations. The gap is explained by #4712's own recorded wart:
two content blocks (`a2-from-three-strands.ts`, `q-deformation-weight-lattice.ts`)
share one `lean.ref` (`QOU.Eightfold.WeylInvarianceQDeformation`) — the probe
partitions over *blocks* but keys output by *declaration*. So 34 block-level
hits collapse to 33 declarations. Not a defect; worth stating so the next reader
does not go looking for a 34th.

## 2. "31 name a declaration that exists nowhere" is wrong

#4712's write-up classified the set as *31 absent + 3 namespace mismatches*.
Re-resolving each ref against its **referring block's own sibling** gives a
materially different — and more actionable — picture:

| class | n | what it means |
|---|---|---|
| **ref names a decl absent from its own sibling** | **22** | the block *has* a sibling `.lean` carrying real content; the ref names a module/concept name instead of a declaration |
| **no sibling `.lean` and no module at the mapped path** | **10** | genuinely unformalised |
| **true namespace mismatch** | **1** | the decl exists, in a different namespace, in the mapped module |

The 22 are the interesting class and they are *not* "exists nowhere". Examples:

| block's `lean.ref` tail | its sibling actually declares |
|---|---|
| `PolynomialBarInvolution` | `barPoly`, `barPoly_X`, `barPoly_neg_X` |
| `QMomentumProperties` | `qMomentumP`, `qMomentumP_additive` |
| `AtomicValence` | `atomicValence`, `valence_hydrogen`, `valence_carbon` |
| `ElectronShellCapacity` | `ElectronShell`, `shell1_capacity`, `shell2_capacity` |
| `DemandProfile` | `NormalForm`, `demandProfile`, `demandMagnitude` |

The pattern is uniform: the ref was written as *the name of the idea* (which is
also the module/block name) rather than the name of a declaration. The
formalisation is present. The fix per block is to pick its principal
declaration — a per-block judgement, deliberately **not** bulk-applied here.

## 3. Two of the three "namespace mismatches" were something else

#4712 listed three namespace mismatches. Only **one** is:

- `QOU.BraidKnot.QBetaCanonicalMarkovWeightsInstance.explicitInstance`
  → the module `QBetaCanonicalMarkovWeightsInstance.lean` declares it under
  `QOU.BraidKnot.CanonicalMarkovWeightsH3`. Genuine namespace mismatch. **Fixed.**

The other two are **wrong declaration names**, not namespaces:

- `QOU.BraidKnot.AtomKnot.unique` — its sibling declares
  `AtomKnot.unique_up_to_markov`. **Fixed.**
- `QOU.BraidKnot.KnotOperatorEnergy.unique` — its sibling declares
  `KnotOperatorEnergy.shadowPrice_unique`. **Fixed.**

Both were reported as resolving to `QOU.BraidKnot.ConfinementLevel.unique`, in a
completely unrelated file. That is a **last-component match on the token
`unique`** — precisely the trap #4712's own write-up warned about:

> *matching `unique` to `unique` would have made the probe silently probe a
> different theorem in an unrelated namespace, and report a confident result
> about it.*

The write-up avoided that trap in the probe and then fell into it in the
taxonomy. Recorded because it is the same failure shape as the four
tool-misreporting bugs #4712 catalogued: **a resolver that reports a confident
wrong answer rather than no answer.** A first pass of this drain reproduced the
trap a third time before the sibling files were read directly.

## 4. The WEAK-33 classification is validated — under a stricter test

#4709 classified 33 blocks as WEAK: *bare `ℝ`, no archimedean construct at all*.
Its classifier is a token regex over raw file text, which matches inside
docstrings, `--` comments and identifiers. A naive re-run appears to contradict
the classification — e.g. `derived-mass-formula-light-isotopes.lean` scores 12
"archimedean" hits.

Re-running with **block and line comments stripped** and word-boundary tokens
(`Real.sqrt|pi|exp|log|rpow|cos|sin`, `Complex.`, `∫`, `deriv`, `Tendsto`,
`NNReal`) resolves the discrepancy — the apparent hits were `Mathlib.Data.Real.Basic`
in an import and the substring `deriv` inside `derivedLightIsotopeFormula`:

> **All 33 have zero code-level archimedean constructs and zero ordering
> tactics.** The classification stands.

So the queue is real, and #4709's judgement not to bulk-acknowledge it was
correct: these are where a genuine gratuitous-`ℝ` is most likely to hide.

## 5. One WEAK block drained — a genuine §7c violation

`mass-theory/macdonald-hook-telescope.lean` was `(Q X : ℝ)` throughout while
containing **only field algebra**: a geometric ratio `((1−X)/(1−Q))^n`, a
quotient, and the hypothesis `Q ≠ 1`. No ordering, no radical, no `Real.*`.

The file diagnosed itself, and the note had gone stale:

> *"For the purposes of this stub we state the telescope as an identity in `ℝ`
> …; the full categorical statement (over `ℚ(Q, X)` …) lives in a follow-up
> file."*

Regenericised to `{R : Type*} [Field R]`, dropping `Mathlib.Data.Real.Basic`.
Same class and same fix as `hoefsmit-binding-amplitude` (#4693/#4703) — the one
genuine violation found in the previous shortlist. Verified `lean`-direct, exit 0.

Sweep: **1089/1188 → 1091/1188** (+1 from this, +1 from the `lean.ref` fix in §3
now resolving to the correct module).

**32 WEAK blocks remain unread.** They are not acknowledged and should not be
acknowledged without a read.

## 6. Noted in passing, not acted on

`macdonald_hook_telescope_witness_scope : 1 + 1 + 2 + 3 + 5 + 7 + 11 = 30 := by decide`
is an **ascribed-literal tautology** — content lives entirely in the declaration
name and docstring — i.e. exactly the class #4712's new detector was added for.
Flagged rather than edited: per AGENTS.md §1a the honest disposition (prove /
state with `sorry` + `-- Ref:` / demote) is a per-item judgement, and this one
belongs with whoever drains that category.

## Remaining

| queue | remaining |
|---|---|
| `lean.ref` — ref names a decl absent from its own sibling | 22 (pick principal decl per block) |
| `lean.ref` — no formalisation at all | 10 (formalise or demote) |
| wall-side WEAK | 32 (each needs a read) |
| wall-side MED | 65 (unchanged; per-file `[LinearOrderedField R]` call) |
