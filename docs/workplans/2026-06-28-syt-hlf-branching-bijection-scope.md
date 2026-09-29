# Scoping: closing `dimAitkenIdentity` (general-n SYT Hook-Length Formula)

**Status:** scoping only — no code committed against this plan yet.
**Owner-gate:** none required (pure combinatorics on ℕ; not a Subgoal-2 q₀-derivation).
**Tracking bean:** see `.beans/` (SYT-HLF branching bijection).
**Branch of origin:** `claude/lean-proof-sorries-lyxk3h` (PR #2984).

## The single remaining gap

[`SYTHookFormulaGeneral.dimAitkenIdentity`](../../folio/quantum-observable-universe/lean/QOU/Mathlib/SYTHookFormulaGeneral.lean)
is the only `sorry` in the SYT hook-length cone. Everything else is machine-checked:

- **hook side (i)** `prodHooks l · betaProdGap l = betaFactProd l` — sorry-free (`prodHooks_mul_betaProdGap`).
- **positivity** `0 < betaProdGap l` — sorry-free.
- **composition** `dimAitkenIdentity ⟹ numSYTenum = dimHLF` — sorry-free
  (`numSYTenum_eq_dimHLF_of_aitken`).
- **finite evidence** the *exact* identity holds for every shape with `n ≤ 6`
  (`dimAitkenIdentity_le4/_5/_6`, kernel `decide`) and `numSYTenum = dimHLF` for `n ≤ 7`
  (`SYTEnumerationN7.numSYTenum_eq_dimHLF_7`, axiom-free kernel `decide`, `[propext]` only).

The gap, in divisor-free form (`β_i = l[i] + (l.drop (i+1)).length`):

```
dimAitkenIdentity :  numSYTenum l · betaFactProd l  =  (sz l)! · betaProdGap l
                     (#SYT(λ) · ∏β_i!            =  n! · ∏_{i<j}(β_i − β_j))
```

Given the sorry-free hook side + positivity, this is **logically equivalent** to the bare HLF
`numSYTenum l = dimHLF l`. So the gap *is* the Frame–Robinson–Thrall theorem itself, no weaker.

## Why it is not a quick `decide` / Mathlib citation

- `numSYTenum` (`SYTEnumeration.lean`) is a **brute-force enumerator** (`allPerms` filtered by
  `isStdFilling`) — no branching/corner-removal lemma exists for it.
- The pinned Mathlib has **no** `#SYT` cardinality theory: no `Combinatorics.RSK`, no Specht modules,
  no Frobenius/Aitken determinant, no hook-length formula. (Verified: olean-only checkout, but the
  `Combinatorics/Young` tree carries only the `StandardYoungTableau` *structure*, no cardinality
  lemmas — consistent with the file docstrings.)

So a general proof must be built from scratch. Two routes:

### Route 1 — branching recursion (recommended; most elementary)

The classical inductive proof. Two obligations, then a strong induction on `n = sz l`.

**(B) Branching bijection for the enumerator.**
```lean
theorem numSYTenum_branching (l : List ℕ) (hl : Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = ∑ i ∈ removableCorners l, numSYTenum (decrementRow l i)
```
The cell holding the largest entry `n` sits at a removable corner; deleting it is a bijection
`SYT(λ) ≃ ⨿_corner SYT(λ⁻ᶜ)`. **This is the hard piece** — it must be proved against the brute-force
`allPerms`/`isStdFilling` model (or via the `numSYTenum = numStandardYoungTableaux` bridge, then on
Mathlib's `StandardYoungTableau`, which has no helpers either). Needs:
- `removableCorners l : Finset (Fin l.length)` — rows with `l[i] > l[i+1]` (last nonzero row always).
- `decrementRow l i` — decrement `l[i]` by 1, drop trailing zero.
- the deletion/insertion bijection on standard fillings (the genuine combinatorial content).

**(A) Algebraic recursion of the closed form.**
```lean
theorem dimHLF_branching (l : List ℕ) (hl : Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    dimHLF l = ∑ i ∈ removableCorners l, dimHLF (decrementRow l i)
```
Pure β-number algebra. With `f(λ) = n!·∏(β_i−β_j)/∏β_i!`, corner `i` sends `β_i ↦ β_i − 1`, `n ↦ n−1`,
others fixed, so
```
f(λ⁻ⁱ)/f(λ) = (β_i / n) · ∏_{j≠i} (β_i − 1 − β_j)/(β_i − β_j)
```
and the obligation is the **Lagrange/partial-fraction identity**
`Σ_i β_i ∏_{j≠i}(β_i−1−β_j)/(β_i−β_j) = n`. Provable over ℚ by Lagrange interpolation on the degree-1
polynomial `x ↦ x`; the divisor-free ℕ reformulation (to match `betaProdGap`/`betaFactProd`) is
fiddly but elementary — **no Mathlib gap**, only labor. Likely the first piece to land sorry-free.

**Composition (sorry-free given (A)+(B)).** Strong induction on `sz l`: base `n ≤ 1` is `decide`;
step rewrites both sides by their branching recursions and applies the IH to each
`decrementRow l i` (which has `sz = n−1`). The recursion terminates because `sz` strictly decreases.

> **Net-sorry discipline.** Do **not** commit (A)+(B)+composition with three open sorries — that is
> worse than the current one. Land **(A) sorry-free first** (the algebra), then the composition
> conditional on (B) only; the corpus then carries **one** sorry — the clean combinatorial bijection
> (B) — instead of the opaque determinant identity. That is the genuine narrowing. Only after (B)
> lands does `dimAitkenIdentity` become sorry-free.

### Route 2 — Frobenius determinant via `Matrix.det_vandermonde`

Mathlib **does** have `Matrix.det_vandermonde`. The Aitken determinant
`#SYT(λ) = n!·det(1/(β_i − (k−1) + j)!)` evaluates by column operations to `n!·V(β)/∏β_i!`. But
connecting `#SYT(λ)` to that determinant is itself the Jacobi–Trudi / Lindström–Gessel–Viennot content
— no lighter than (B). Not recommended as the primary route; `det_vandermonde` may still help *inside*
(A) if (A) is recast determinantally.

## Effort estimate & risks

| Piece | Est. | Risk |
|---|---|---|
| `removableCorners` / `decrementRow` defs + basic lemmas | 0.5 day | low |
| (A) `dimHLF_branching` (Lagrange identity, divisor-free) | 1–2 days | medium (ℕ bookkeeping) |
| (B) `numSYTenum_branching` (the bijection) | 3–6 days | **high** (the real content) |
| composition (strong induction) | 0.5 day | low–medium (termination plumbing) |

Total ≈ 1–2 weeks of focused Lean. (B) is the dominant risk and the reason this is a dedicated
effort, not a session task. The `decide`-verified `n ≤ 7` evidence is the regression backstop for any
partial progress.

## Recommended sequencing

1. Land `removableCorners`/`decrementRow` + their characterizing lemmas (sorry-free).
2. Land (A) `dimHLF_branching` sorry-free (algebra only; biggest tractable win).
3. State (B) with one honest `sorry` + `-- Ref: [macdonald1995] / [sagan2001]`; prove the composition
   conditional on (B). Now the corpus has **one** sorry (B), sharper than today's.
4. Attack (B): the deletion bijection on standard fillings. This is the multi-day core.
5. On (B) landing, `dimAitkenIdentity` and `numSYTenum_eq_dimHLF` go fully sorry-free; retire the
   `_of_aitken` conditional wrappers.

## Update (2026-06-29) — the manifestly-integer dimension form for general `m` (the (A) keystone)

The 2-row case of (A) closed (#3051) because `dimHLF[a,b]` has the **manifestly-integer** ballot form
`C(a+b,b) − C(a+b,b−1)` (#3044), turning the branching into Pascal's rule with no floor-division. The
analysis below was the blocker for `m ≥ 3`: a *single* binomial closed form does not exist. The
resolution (derived + computationally verified this session, `m ≤ 4`, all parts `≤ 6`) is the
**Frobenius/Aitken determinant in signed-multinomial form**:

> **`dimHLF λ  =  Σ_{σ ∈ S_m}  sgn(σ) · multinomial(n ; (λ_i − i + σ(i))_{i})`**,
>
> where each `multinomial(n; k_1,…,k_m) = n!/(k_1!⋯k_m!)` is a manifest `ℕ` (the indices sum to `n`
> since `Σ(λ_i − i + σ(i)) = Σλ_i = n`), and terms with any negative index drop out.

This is `n!·det(1/(λ_i − i + j)!)` (Aitken) with the determinant expanded over `S_m`; it specialises
**exactly** to the 2-row ballot number (`σ = id` gives `C(n,b)`, the transposition gives `−C(n,b−1)`),
and to `60 − 20 − 30 + 6 = 16` for `λ = (3,2,1)` (verified vs `#SYT`). It is the manifestly-integer
form general integrality needs — there is no entry-wise binomial determinant; integrality is *global*
(the signed sum), exactly as the 2-row difference already showed.

**Revised step 2 (general (A)) path, now unblocked conceptually:**
- 2a. Define `frobeniusDim l : ℤ := ∑_{σ : Equiv.Perm (Fin m)} sgn σ · multinomial …` (Mathlib
  `Equiv.Perm`, `Nat.multinomial`); `decide`-verify `dimHLF l = frobeniusDim l` for small `n`
  (regression backstop, sorry-free).
- 2b. Prove `dimHLF l = frobeniusDim l` in general — the hook side `prodHooks·betaProdGap =
  betaFactProd` (already sorry-free) plus `Matrix.det_vandermonde`: `frobeniusDim` is
  `n!·det((β_i)_{falling, m−j})/∏β_i!` and the falling-factorial determinant is the Vandermonde
  `∏_{i<j}(β_i−β_j) = betaProdGap`. **This is the multi-day `Matrix.det` core** (Laplace/Vandermonde).
- 2c. Branching of `frobeniusDim` via Pascal on each multinomial term (generalises the 2-row Pascal
  proof) ⇒ general (A) `dimHLF_branching`.

The formula is the durable result of this session's general-(A) grind; 2b–2c remain a dedicated
LSP-session effort (the `lake`-destructive sandbox makes `m×m` determinant proofs impractical via
recompile-iteration).
