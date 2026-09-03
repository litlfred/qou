# Roast of brick 3 — the `BrunnianDeficitRecursion` Lean instance (qou-v7ro)

**Date:** 2026-08-31 · **Bean:** `qou-v7ro` · **Scope:** adversarial feasibility assessment (a
"roast"), not a coding task. Evidence-based: every claim below was grepped/read in the QOU Lean
tree this session. **Verdict up front: do NOT commit to the full brick 3 now — bank bricks 1–2,
record this roast, and if pursued, take the design fork below deliberately.**

## What brick 3 must deliver

The `BrunnianDeficitRecursion` **instance**: a Lean proof that the *actual* convention-D spin-½
Markov deficit `D_A = 1 − qtr(ρ(w_A))/[2]^A` satisfies `D_{A+1}=−h²(h²+2)D_A` ∀A. Needs: (a)
`ρ(w_n)` as a concrete operator on `V^⊗n` ∀n; (b) the μ-weighted quantum trace `qtr`; (c) identity
(I) `G_n=[2]^n(1+h²)−h²Q_n`; (d) the cap-cup reduction `Q_n=qtr_{n-2}(c·B)` + coupled c/B recursions
+ pairing + T4 → the 2-term recursion; (e) the composing induction. The recursion is already
**proved mathematically** (#6217, certified) and its field-algebra glue (e)+scalar-closure is
already Lean (#6228). So brick 3 is Lean-formal *verification of an already-proved result* — its
value is assurance, not new mathematics.

## What the QOU tree already has (the good news — more than "Mathlib has no knot theory")

| infra | file | what it gives |
|---|---|---|
| abstract TL algebra ∀n | `MathlibExt/TemperleyLiebAlgebra` | `RingQuot` of `FreeAlgebra` mod {loop `e_i²=δe_i`, adjacency `e_ie_je_i=e_i`, commuting}; universal property; `TL_{n+1}(δ)` |
| Iwahori–Hecke algebra | `MathlibExt/IwahoriHeckeAlgebra` | the Hecke algebra abstractly |
| Hecke representation | `Archimedean/HeckeRep` + `MathlibExt/MarkovTrace` | `HeckeRep n d`, `.eval : BraidWord n → Matrix (Fin d) R_t` (monoid hom), `.character w = (eval w).trace`, cyclic + conjugation invariance |
| trace multiplicativity | `MathlibExt/MarkovTraceMultiplicative` | `markovTrace_kronecker : tr(A⊗ₖB)=tr(A)tr(B)`, `trace_kronecker_pow` |
| Ocneanu trace, Markov moves | `MathlibExt/OcneanuTrace`, `MarkovMoves`, `MarkovBondRule` | the trace-tower axioms as hypotheses |
| YBE | `Braiding/r_matrix_braiding_structure` | YBE on an **abstract** `RMatrixBraidingContext` |

## The roast — five obstacles, each measured

**(R1) Wrong trace.** `HeckeRep.character` is, by its own honesty note (`MarkovTrace.lean` §Scope),
the *un-normalised, single-irrep, plain matrix trace over `R_t = ℤ[t,t⁻¹]`* — explicitly **not** the
`y_λ`-weighted Markov trace, **not** normalised (`tr_M(1)=1`), and **not** the μ-weighted quantum
trace `qtr = tr(D·X)` the deficit uses. The deficit needs the spin-½ (d=2ⁿ) rep with the
μ-weighted quantum trace normalised by `[2]^A`. The existing `markovTrace` is a different functional.

**(R2) No concrete spin-½ tensor-power representation.** `r_matrix_braiding_structure` axiomatises
the YBE on an opaque `RMatrixBraidingContext` (V3, comp, R12/R13/R23) — there is **no** concrete
`R̆ = P∘R` operator on `V^⊗n` for general `n`, and no concrete `HeckeRep` instance realising the
spin-½ rep with the actual R-matrix. Brick 1 (`TemperleyLiebSpinHalf`) built the concrete `e=q−R`
only at 2 strands (4-dim). The position-indexed `e_i`/`R_i` on `V^⊗n` (identity elsewhere) satisfying
the TL relations ∀n is the single hardest missing piece, and it is unbuilt.

**(R3) The Brunnian word tower.** `BraidWord n` is a fixed-`n` generator list. `w_n = [w_{n-1}, b_n]`
is an iterated band-commutator that grows with `n`; the family `{w_n}` plus the strand embedding
`BraidWord (n-1) ↪ BraidWord n` and the operator-level compatibility `ρ(w_{n-1}) ↦ ρ(w_{n-1})⊗1`
must be defined and proved. Doable (list + `Fin` bookkeeping) but not free.

**(R4) The substance is all new.** None of the existing infra proves identity (I), the cap-cup
reduction, the coupled c/B recursions, the pairing `=Q_{n-1}`, or `T4=h⁴[2]Q_{n-1}` at the concrete
μ-trace level. The abstract TL relations help re-express `e_i²=[2]e_i`, but the trace *identities*
that carry the proof are representation-specific and unformalised.

**(R5) Parallel-track risk + a self-correction I own.** Bricks 1–2 (`TemperleyLiebSpinHalf`,
`QuantumTraceTower`) built a **concrete `Fin 4` / `Fin n → Fin 2` μ-weighted** track that does **not**
connect to the `HeckeRep`/`MarkovTrace` track. Concretely, brick 2's `qtr_kron` **overlaps**
`MarkovTraceMultiplicative.markovTrace_kronecker` (both rest on `Matrix.trace_kronecker`; mine adds
the weight `D`, so it is a generalisation, not an exact duplicate — but I should have grepped for the
existing file *before* writing it). Continuing brick 3 forces a design choice: build on my concrete
`Fin n → Fin 2` model (self-contained, reproves some infra) **or** on `HeckeRep` (reuses cyclic/conj
lemmas, but must *add* the quantum trace + spin-½ rep + normalisation). Neither is short, and mixing
them without a bridge lemma would duplicate more.

> **R5 overlap RETIRED (2026-09-02).** `QuantumTraceTower.qtr_kron` now routes through the canonical
> plain-trace multiplicativity `QOU.MathlibExt.MarkovTraceMultiplicative.trace_kron` instead of
> re-invoking `Matrix.trace_kronecker` in parallel — so one trace-multiplicativity lemma sits under
> both the mass/binding Markov-trace compute and this weighted tower. The μ-weighted `qtr_kron` is now
> a documented specialisation of `trace_kron`, not a parallel track. (The exact name in the file is
> `trace_kron`, not `markovTrace_kronecker` — this note also corrects the identifier used above.)
> Statements unchanged; sorry-free; verified lean-direct.

## Effort + verdict

Brick 3 is a genuine multi-file, multi-session formalisation whose crux (R2) is essentially
"formalise the Temperley–Lieb / Hecke **Markov-trace representation** on tensor powers" — a project
in its own right. The abstract TL algebra existing shortens the *relations*, not the *rep + trace*.
Because the recursion is already proved and certified, brick 3 buys formal assurance, not new
results, and the anti-laundering rule forbids shortcutting it with a `sorry` instance.

**Recommendation (judgement, marked as such):**
1. **Do not open the full brick 3 now.** Bank bricks 1–2 as reusable concrete-spin-½ TL infra.
2. **This roast is the durable record** so the next agent does not rediscover R1–R5.
3. **If brick 3 is pursued**, sequence it: (3a) decide the track (my `Fin n → Fin 2` model vs
   `HeckeRep`) and, if keeping mine, add a one-line bridge `qtr_kron ⟷ markovTrace_kronecker` to
   retire the R5 overlap; (3b) the position-indexed `e_i` on `V^⊗n` + TL relations ∀n (the R2 crux);
   (3c) `ρ(w_n)` tower; (3d) identity (I) + cap-cup + induction, closing via the existing #6228 glue.
4. **The `BrunnianDeficitRecursion` instance stays unfabricated** (honest open state) meanwhile — the
   recursion is proved in math and certified; only its Lean witness is deferred.
