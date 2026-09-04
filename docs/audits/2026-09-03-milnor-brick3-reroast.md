# Re-roast of brick 3 — has the landed two-row / Schur–Weyl / Burau machinery filled the gap? (qou-v7ro)

**Date:** 2026-09-03 · **Bean:** `qou-v7ro` · **Scope:** re-run the 2026-08-31 brick-3 feasibility
roast (`docs/audits/2026-08-31-milnor-brick3-roast.md`) against the Lean machinery that has since
landed on `main`. Evidence-based: every claim was grepped/read in the QOU Lean tree this session.
**Verdict up front: DEFER still stands — the R2 crux (a concrete, evaluable `ρ(w_n)` on `V^{⊗n}`
with the μ-weighted quantum trace) is NOT filled — but the residual gap is now sharply smaller and a
new, lighter route exists. Recorded so the next agent inherits the sharpened target, not the whole
of R2.**

## Why re-roast now

The original roast (2026-08-31) named five obstacles R1–R5 and recommended banking bricks 1–2 and
deferring the full `BrunnianDeficitRecursion` instance. Since then, machinery landed on `main` that
plausibly touches the crux: `TwoRowStratum`, `TwoRowCapDerived`, `MagnusHookExteriorPower`,
`MarkovWeightValueTransport`, and the R5 consolidation (`qtr_kron → trace_kron`, #6425). The
question this doc answers precisely: **do those files now supply the three things brick 3 needs —
(a) the concrete `ρ(w_n)` operator on `V^{⊗n}`, (b) the μ-weighted quantum trace, (c) the cap-cup
at position `n−1` — closing R2?**

## What the three brick-3 obligations are (restated)

1. **(a) concrete `ρ(w_n)`** — the Brunnian word `w_n = [w_{n-1}, b_n]` as an actual matrix/operator
   on `V^{⊗n}` (V = ℂ², so dim `2^n`), evaluable ∀n, with the strand embedding
   `ρ(w_{n-1}) ↦ ρ(w_{n-1}) ⊗ 1`.
2. **(b) μ-weighted quantum trace** — `qtr D X = tr(D·X)` normalised by `[2]^n`, the functional the
   deficit `D_A = 1 − qtr(ρ(w_A))/[2]^A` is built from.
3. **(c) cap-cup at `n−1`** — the `μ⁻¹` contraction `ptr_{μ⁻¹}(e) = 1` at position `n−1` that drives
   the `Q_n = qtr_{n-2}(c·B)` reduction.

## What landed, measured file by file

| file (on `main`) | what it actually provides | fills which obligation? |
|---|---|---|
| `BraidKnot/TwoRowStratum.lean` | the **statement** `H_n(q) ↠ End_{SU(2)}(V^{⊗n})`, V = ℂ² Schur–Weyl; predicate `IsTwoRow`. Its own docstring: *"pre-Archimedean STUB, polymorphic in the partition representation, no commitment to a Mathlib Partition API."* | **(a) NO** — it is a surjection *statement*, not a concrete operator. No evaluable matrix. |
| `MassTheory/TwoRowCapDerived.lean` | convention D = Wenzl level 2; ≥3-row weights vanish exactly (`massWeight_eq_zero_of_three_rows_of_wenzl`, `traceSum_eq_twoRow_of_wenzl`). | **partial (the cap's *target*)** — shrinks what must be traced to ≤2-row characters, but does not build (a)/(b)/(c). |
| `MassTheory/QuantumTraceTower.lean` (bricks 2 + R5) | `qtr_kron` (multiplicativity, now via canonical `trace_kron`), `qtrDiag_one` (`[2]^n` tower). | **(b) partial** — the *dimension-general* qtr facts exist; the *rep-specific* trace identities do not. |
| `MassTheory/TemperleyLiebSpinHalf.lean` (brick 1) | concrete 2-strand TL: `eTL_mul_eTL`, `ptr_muInv_eTL`(=1), `ptr_mu_eTL`, `band_mul_bandInv`. | **(c) at n = 2 only** — the position-indexed `e_{n-1}` on `V^{⊗n}` ∀n is still unbuilt. |
| `MassTheory/MagnusHookExteriorPower.lean` | esymm generating-function CORE (`prod_one_add_mul_eq_sum_esymm`). Own scope note: *"the seminormal Hecke construction, the specific word ρ, and the q-twist are outside Mathlib … numerically established, not formalizable here."* | **(a) NO** — explicitly disclaims the concrete word rep. |
| `Archimedean/MarkovWeightValueTransport.lean` | H₂ Jones–Markov weight VALUES (`y₂ 1 = 3/4`, `y₁₁ 1 = 1/4`), T4-scoped. | **no** — H₂-specific values, not a tensor-power rep. |

**Decisive negative evidence (R2).** A grep of `content/**/BraidKnot/*.lean` and
`content/**/MassTheory/*.lean` for a **concrete reduced-Burau matrix definition** and a **concrete
two-row → 2-dim sl₂ evaluable representation** returned **empty**. The corpus's own scope notes
(`MagnusHookExteriorPower`, `TwoRowStratum`) state the concrete word rep is "outside Mathlib /
numerical". So obligation (a) — the single hardest missing piece the original roast identified — is
**still unfilled**. DEFER stands.

## What genuinely changed (the landscape did shift)

The re-roast is not a null result. Three things are now true that were not on 2026-08-31:

1. **The target shrank to ≤2-row characters.** `TwoRowCapDerived` proves convention D = Wenzl
   level 2 with exact ≥3-row vanishing. So brick 3 no longer needs the full `2^n`-dim `V^{⊗n}`
   character — only the ≤2-row part survives the trace, and two-row characters reduce to the 2-dim
   sl₂ rep (the object `qou-o6ov` has been mapping: `tr_{(k,1^{n-k})}(ρ) = q^{L(1-j)} e_j`, the
   elementary-symmetric generating function, Lean sorry-free).
2. **A lighter route exists.** Instead of building the concrete `2^n`-dim `ρ(w_n)` on `V^{⊗n}`
   (obligation (a) as originally scoped), the ≤2-row cap + the landed esymm generating function
   (`MagnusHookExteriorPower.prod_one_add_mul_eq_sum_esymm`) + the reduced-Burau exterior-power
   character columns give the surviving character **without** the full tensor-power operator. This
   trades "build a `2^n` matrix ∀n" for "derive the Brunnian word's two-row/reduced-Burau spectrum
   ∀n" — a strictly smaller object.
3. **R5 is retired** (#6425): `qtr_kron` routes through the canonical `trace_kron`, so the weighted
   tower and the mass/binding Markov-trace compute share one multiplicativity lemma. The design-fork
   worry in the original R5 (two disconnected tracks) is resolved on the (b) side.

## The sharpened residual gap

The original roast's R2 was "formalise the Temperley–Lieb / Hecke Markov-trace representation on
tensor powers" — a project in its own right. The residual gap is now:

> **Lean-derive the Brunnian word `w_n`'s two-row / reduced-Burau character (its surviving spectrum)
> ∀n**, then feed it through the landed esymm generating function and the ≤2-row cap to reconstruct
> `Q_n`, closing the recursion via the existing `DeficitRecursionReduction` (#6228) glue.

This is smaller than "all of R2" because (1) the cap removes the ≥3-row bulk, (2) the trace
multiplicativity and `[2]^n` tower already exist (bricks 2 + R5), and (3) the esymm generating
function is landed. What remains genuinely new: the position-indexed `e_{n-1}` on the *reduced*
(≤2-row) space ∀n, and the specific Brunnian-word spectrum recursion — both still real work, neither
free.

## Verdict + recommendation (judgement, marked as such)

1. **DEFER stands.** Obligation (a) — a concrete, evaluable `ρ(w_n)` (or its reduced-space
   surrogate) ∀n — is NOT supplied by any landed file; the corpus's own scope notes disclaim it.
   The `BrunnianDeficitRecursion` instance stays **unfabricated** (honest open state) — the recursion
   is proved in math (#6217) and certified; only its Lean witness is deferred.
2. **But re-scope the residual to the smaller route.** If brick 3 is pursued, take the
   reduced-Burau / esymm route (avoid the `2^n` `V^{⊗n}` operator), not the original full
   tensor-power build. The `qou-o6ov` two-row character machinery is the natural upstream.
3. **This doc is the durable record** so the next agent inherits the *sharpened* gap and the lighter
   route, not the original whole-of-R2 framing.
4. **No new Lean was written for this re-roast** — it is an assessment. Nothing to verify; nothing
   fabricated.
