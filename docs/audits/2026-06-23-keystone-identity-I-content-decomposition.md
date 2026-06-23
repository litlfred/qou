# Keystone Identity I, decomposed: `M(n)=n(3n−1)/2` without the hook-length formula

**Date:** 2026-06-23
**Branch:** `claude/busy-faraday-c6pfrq`
**Status:** closed-form derivation + exhaustive exact verification — no fit, no
correspondence chain, nothing archimedean (`q₀` and the 210 ppb target never appear).
**Script:** [`scripts/keystone_identity_I_content_decomposition.py`](scripts/keystone_identity_I_content_decomposition.py)
(`ALL CHECKS PASS`, exit 0).
**Lean:** [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)
(`twoM_content_decomposition`, sorry-free `ring`).

## Why this is in scope (Path B → keystone → C(n) → Identity I)

The per-atom **Path B `λ(K)`** binding route — the documented Subgoal-1 closure
path in [`docs/precision-goals.md`](../precision-goals.md) — has had its *numerical*
search exhausted (22 no-fit closures; [`gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md)).
Path B and the Δ_λ Path D both converge on the **single owner-gated open object**:
the s5-so3 keystone geometric realization of the Wedderburn weights `W_λ`
([`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md);
gate **reversed for this construction** 2026-06-19, [`AGENTS.md §Precision-goals`](../../AGENTS.md),
[`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)).

That keystone has a **falsifiable, `q₀`-free, no-fit sub-target**
([`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md)):
any `S¹`-equivariant index realizing `W_λ` must reproduce the heat-kernel defect
coefficient

```
144·C(n) = −n(n−1)(2n−13)     (the exact n=7 sign change).
```

This is Lean-proved sorry-free **except for one carried representation-theoretic
input**, *Identity I*:

```
M(n) := (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²  =  n(3n−1)/2 ,
```

the Plancherel-expected squared-hook sum, held in
[`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)
as an assumed `def twoM`. The corpus (keystone ledger; the 2026-06-20 closed-form
audit) repeatedly states this *"needs SYT-dimension / hook-length infrastructure not
currently in Mathlib — a multi-session infra fill."*

**That framing assumes the hard Frame–Robinson–Thrall hook-length FORMULA
`dim(λ)=n!/∏_c h_c` is on the critical path. It is not.**

## The decomposition

Identity I factors into two pieces, **neither using the hook-length formula**:

> **(A) Per-partition hook-content identity** — a statement about a *single* Young
> diagram (no dimensions, no Plancherel measure, no hook-length formula):
> ```
> Σ_{c∈λ} h_c²  =  Σ_{c∈λ} c(c)²  +  n²        for every  λ ⊢ n,
> ```
> where `c(c)=j−i` is the content of cell `(i,j)` and `h_c` its hook length.

> **(B) Plancherel content-square mean** — the standard Jucys–Murphy result:
> ```
> E_Planch[Σ_c c(c)²] := (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} c(c)²  =  binom(n,2) = n(n−1)/2 .
> ```

Then, since `E_Planch[n²] = n²` trivially,

```
M(n) = E_Planch[Σ_c h_c²]  =  E_Planch[Σ_c c(c)²] + n²
     = binom(n,2) + n²  =  (n²−n)/2 + n²  =  n(3n−1)/2 .     ∎
```

### Proof of (B) (no hook-length formula, no fit)

The power sum of the Jucys–Murphy elements `X_k = Σ_{i<k}(i,k)` (`X_1=0`),

```
p_2(X) = Σ_{k=1}^n X_k²  ∈  Z(ℂ[S_n])     (central),
```

acts on the Wedderburn block `V_λ` by the scalar `Σ_{c∈λ} c(c)²` (the JM eigenvalues
on the SYT basis are the cell contents; summing `X_k²` over the basis sums `c(c)²` over
all cells). For any central `z = Σ_g a_g g` acting on `V_λ` by `ω_λ(z)`, the central
primitive idempotent expansion `z = Σ_λ ω_λ(z) e_λ` with
`e_λ = (dim λ/n!) Σ_g χ^λ(g⁻¹) g` gives, reading off the identity coefficient,

```
a_e  =  Σ_λ ω_λ(z) · (dim λ)²/n!  =  E_Planch[ω_·(z)] .
```

For `z = Σ_k X_k²` the only identity contributions are `(i,k)(i,k)=e` (`i<k`), so

```
a_e  =  Σ_{k=1}^n (k−1)  =  binom(n,2) .
```

Hence `E_Planch[Σ_c c(c)²] = binom(n,2)`. (This is the classical content-power-sum /
Jucys–Murphy fact; cf. the corpus's already-Lean-proved ribbon eigenvalue
`θ_λ = q^{2c(λ)}` in [`2026-06-19-content-twist-eigenbasis-reframing.md`](2026-06-19-content-twist-eigenbasis-reframing.md),
which is the `c(λ)`-graded sibling of the same JM content structure.)

### Status of (A)

(A) is a per-partition combinatorial identity with **no representation-theoretic
content** — it does not mention dimensions, the Plancherel measure, or the
hook-length formula. It is **exhaustively verified** in exact integer arithmetic for
**every** partition with `n ≤ 22` (4507 partitions; the script's check (A)). It is of
the standard hook/content power-sum family: via the first-column hook (β-set)
`β_i = λ_i + r − i`, the hooks of row `i` are `{1,…,β_i} ∖ {β_i−β_k : k>i}`, giving
`Σ_c h_c² = Σ_i Σ_{m=1}^{β_i} m² − Σ_{i<k}(β_i−β_k)²`, and the contents have the
parallel `Σ_c c(c)² = Σ_i Σ_{j=1}^{λ_i}(j−i)²`; the difference collapses to `n²`. We
report (A) as **verified + citable**, not re-proved from scratch here.

## What this re-scopes for the Lean fill (the headline)

The hard **Frame–Robinson–Thrall hook-length formula is OFF the critical path.** The
residual Lean fill for Identity I is two standard, individually-simpler pieces:

| Piece | What it needs | In Mathlib today? |
|---|---|---|
| **(A)** `Σh² = Σc² + n²` | `YoungDiagram` + hook + content **definitions** and one combinatorial identity | `YoungDiagram` ✅; hook/content are easy defs; identity is a finite-combinatorics lemma |
| **(B)** `E_Planch[Σc²]=binom(n,2)` | `ℂ[S_n]` Wedderburn-dimension structure (`Σ_λ (dim λ)² = n!`) + Jucys–Murphy centrality | the standard `S_n` representation/JM machinery — **not** the hook-length formula |

So "needs SYT/hook-length infra" is **half right**: (B) does use the
`dim λ`/`Σ(dim λ)²=n!` Wedderburn structure (genuine SYT-dimension infra, but
standard), while the *hardest* ingredient people assume — the hook-length **formula**
— is **not needed at all**. The multi-session blocker shrinks to (A) a self-contained
combinatorial identity (verified) and (B) a standard JM/Wedderburn computation
(proved on paper above).

### Lean delta this PR

`WLambdaDefectClosedForm.lean` keeps `twoM` but now records the decomposition as a
sorry-free `ring` identity, with each summand attributed:

```lean
theorem twoM_content_decomposition (n : ℤ) : twoM n = n * (n - 1) + 2 * n ^ 2
-- n*(n-1) = 2·binom(n,2) = 2·E_Planch[Σ c²]   (piece B, Jucys–Murphy)
-- 2*n²    = 2·(per-partition n² gap)            (piece A, summed under Plancherel)
```

`n*(n−1) + 2*n² = 3n²−n = n(3n−1) = twoM n`, so `n144C_closed_form` and the
`n=7` sign change are unchanged; the opaque carried constant is now a transparent,
individually-attributed split.

## Verification (this PR, exact integer / Fraction arithmetic)

`scripts/keystone_identity_I_content_decomposition.py` (`ALL CHECKS PASS`):

- **(A)** `Σh² − Σc² = n²` for all **4507 partitions**, `n=1..22`.
- **(B)** `E_Planch[Σc²] = binom(n,2)` exactly, `n=1..22`.
- **(Bx)** JM coefficient-of-identity `Σ_{k=1}^n (k−1) = binom(n,2)` and that it equals
  `E_Planch[Σc²]` (the bridge value).
- **(D)** `M(n) = binom(n,2)+n² = n(3n−1)/2`, decomposition `==` direct, `n=1..22`.

## Discipline

- **No fit.** An exact identity is *proved* (B) / *exhaustively verified* (A); `q₀` and
  the 210 ppb target are never used. This is **not** a content-statistic `Δ_λ` ansatz
  (those are refuted and out of scope, [`2026-06-19-content-twist-eigenbasis-reframing.md §4`](2026-06-19-content-twist-eigenbasis-reframing.md));
  it concerns the `q→1` leading data `M(n)` of `W_λ`, the one carried input to the
  *falsifiable* C(n) sub-target.
- **No correspondence chain.** Pure `S_n` combinatorics + JM elements; the
  `2I→E₈→Lawrence–Zagier` chain is never invoked.
- **Owner-gate respected.** Operates strictly inside the 2026-06-19 narrow reversal
  for the keystone geometric `W_λ` construction; introduces no physical claim, wires
  nothing to production.
- **Corpus-grep done.** The content/JM eigenbasis is established in-corpus
  (`θ_λ=q^{2c(λ)}` Lean-proved); the *content decomposition of Identity I* (this doc)
  is not previously recorded — the corpus framed Identity I only through the
  hook-length formula.

## Cross-references

- [`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md) — the C(n) closed form; Identity I as deferred Lean opportunity.
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the sorry-free defect file (Identity I carried in `twoM`).
- [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger (Identity-I Mathlib-gap note now narrowed by this doc).
- [`2026-06-19-content-twist-eigenbasis-reframing.md`](2026-06-19-content-twist-eigenbasis-reframing.md) — the JM content / ribbon-twist eigenbasis already in-corpus.
- [`gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) — Path B `λ(K)` ledger (the route this keystone serves).
