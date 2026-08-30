# Scoping Geck–Pfeiffer 7.2.6 against Mathlib — the τ-form route is a multi-session build, and it is not the reachable target

*2026-08-30. Bean `qou-0y6h`. Measured before building, per the formalize-first
discipline: state the hypothesis class, find what prunes it, and let the result
narrow the probe rather than discovering the wall halfway in.*

## The question

`qou-0y6h` names Geck–Pfeiffer Thm 7.2.6 — *every Schur element nonzero ⟹ split
semisimple* — as its remaining content. The classical route runs through the
**symmetrizing trace** `τ`: `H_n(q)` is a symmetric algebra, `τ` decomposes as
`τ = Σ_λ (1/c_λ) χ^λ`, and the `c_λ` are the Schur elements.

Is that route reachable with what Mathlib has?

## Measured: no. Every piece of the vocabulary is absent.

| GP 7.2.6 needs | Mathlib has |
|---|---|
| symmetric (Frobenius) algebra | **absent** — and see the name collision below |
| `IsFrobenius` / Frobenius form | **absent** (`grep -rln "IsFrobenius"` → nothing) |
| Schur elements | **absent** (`grep -rn "schurElement\|Schur element"` → nothing) |
| split semisimple | **absent** (`grep -rln "IsSplitSemisimple\|SplitSemisimple"` → nothing) |
| primitive central idempotents indexed by irreps | **absent** |
| characters of an algebra rep indexed by Wedderburn blocks | **wrong object** — see below |
| Artin–Wedderburn as an *iff* | **`proof_wanted`** — Mathlib's own open TODO |

### The name collision, which will mislead a grep

`Mathlib/LinearAlgebra/SymmetricAlgebra/` exists and is **not** what this needs.
Its own header: *"Given a commutative semiring `R`, and an `R`-module `M`, we
construct the symmetric algebra of `M`. This is the free commutative `R`-algebra
generated (`R`-linearly) by the module `M`."* That is `Sym(V)`, a construction on
a module. A *symmetric algebra* in the Frobenius sense — an algebra with a
symmetric non-degenerate associative form — is a different notion sharing the
name, and Mathlib does not have it.

### Character theory is about groups, not algebras

`Mathlib/RepresentationTheory/Character.lean` is characters of **finite group**
representations (`FDRep`), with orthogonality *"for irreducible representations
of a finite group over an algebraically closed field whose characteristic doesn't
divide the order of the group"*. `H_n(q)` is not a group algebra, and the
decomposition GP needs is indexed by `Partition n` — precisely the indexing
`exists_algEquiv_pi_matrix_divisionRing` does not supply.

### Artin–Wedderburn's useful direction is Mathlib's own open problem

```lean
proof_wanted isSemisimpleRing_iff_pi_matrix_divisionRing {R : Type u} [Ring R] :
    IsSemisimpleRing R ↔ ∃ (n : ℕ) (S : Fin n → Type u) (d : Fin n → ℕ) …
```

`Mathlib/RingTheory/SimpleModule/Basic.lean:464`. The existential direction
(`exists_algEquiv_pi_matrix_divisionRing`) is proved; the `iff` is not.

### `traceForm_nondegenerate` does not apply

`Mathlib/RingTheory/Trace/Basic.lean:496` proves it for a **separable field
extension** — a commutative statement. `H_n(q)` is noncommutative and this is not
about it.

## The redirect: the reachable target is not GP 7.2.6

The corpus's own `QOU.MathlibExt.RegTraceGram` route **sidesteps the entire
Frobenius/Schur vocabulary**. `isSemisimpleRing_of_regTraceGram_det_ne_zero` is
already proved and needs only

* a basis — `basisTwOfField`, landed 2026-08-30 (`9c7211676c`);
* a **determinant value** for the *regular* trace form.

No symmetrizing trace, no Schur elements, no split-semisimple, no
Artin–Wedderburn. So the reachable statement is

> `det (twGram K q n) ≠ 0` for the substrate regime,

and the `n = 2` case is **already worked in the corpus**:
`QOU.Hecke.H2TraceForm.h2_regTraceGram_det : det = [2]_q ^ 2`, sorry-free — via
`AdjoinRoot`, because there was no `T_w` basis when it was written.

The general-`n` computation now has what it needs:
`QOU.Hecke.TwBasis.σ_mul_Tw` is the full structure-constant table, so
`tr(L_{T_u})` is a finite sum of diagonal coefficients read off the *down* cases
of that table. That is arithmetic in the basis, not representation theory.

## Verdict

- **τ-form / GP 7.2.6: do not start it as a session's work.** It is a
  multi-session build that begins by adding symmetric-algebra theory to Mathlib,
  and passes through a Mathlib `proof_wanted`. Worth doing on its own merits as
  an upstream contribution; not the way to `qou-0y6h`.
- **Regular-trace determinant: open, in scope, and the hook is already built.**
  Next concrete step is `tr(L_{T_u})` from `σ_mul_Tw`, then `det(twGram)`,
  generalising `h2_regTraceGram_det` off the `AdjoinRoot` presentation and onto
  the `T_w` basis.

**Scope note.** This is a *scope-(a)* finding about the two routes, not a
*scope-(b)* exclusion of GP 7.2.6: nothing here says the theorem is false or
unreachable, only that its vocabulary is not present and the corpus has a
cheaper road to the same consumer.
