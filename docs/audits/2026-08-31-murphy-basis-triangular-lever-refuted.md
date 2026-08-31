# The `Triangular` lever cannot prove the Murphy basis — measured, and the route that replaces it

**Date:** 2026-08-31 · **Bean:** `qou-phir` · **Branch:** `claude/hecke-murphy-index-bridge-2026-08-31`
**Probe:** [`computations/hecke/murphy_supp_rsk_probe.py`](../../computations/hecke/murphy_supp_rsk_probe.py)
(exact integer arithmetic; permutations are tuples, Hecke coefficients are Laurent polynomials
held as `dict{exponent: int}` — no float appears anywhere in the script)

## The claim

`QOU.BraidKnot.SpechtStandardBasis.Triangular` — the corpus's linear-independence lever, a family
`v : ι → (α →₀ R)` with an injective leading map `lead`, a unit diagonal coefficient, and support
bounded above by `lead` — **cannot** be applied to the Murphy family `m_{st}` against the `T_w`
basis of `H_n(q)`. This holds for **every** linear order on `S_n` and **every** bijective leading
map, not merely for the RSK map that motivated the attempt.

This is a **scope-(b) structural exclusion** in the AGENTS.md sense. The invariant cited is the
peeling argument in §3, and the `n = 3` check is exhaustive over all six indices rather than
sampled. It excludes **this lever applied to this pair of bases**. It says nothing against the
Murphy basis, which is a theorem (Murphy 1995; Mathas, Thm 3.20), nor against `Triangular`, which
remains the proved lever the Specht standard-basis theorem runs on.

## 1. What was being attempted, and why it looked promising

The plan (bean `qou-phir`) was: index the Murphy elements by `MurphyIndex n`, use the
Robinson–Schensted bijection as `lead`, and discharge the three `Triangular` fields.

`lead_inj` came out **free**, and that part stands: `murphyIndexEquivPerm n : MurphyIndex n ≃
Equiv.Perm (Fin n)` is RSK composed with the `Nat.Partition`-Σ ↔ `YoungDiagram`-subtype index
bridge, so `lead_injective` is `Equiv.injective` with no combinatorial content
(`QOU.BraidKnot.HeckeMurphyYoung`, sorry-free). Getting one of three fields for nothing is what
made the route look cheap.

## 2. `diag_unit` fails first — RSK is not a legal leading map

`diag_unit` requires the coefficient at `lead x` to be a unit, so in particular `lead x ∈
supp (m x)`. Measured over the complete index set:

| `n` | indices | `RSK⁻¹(P=s,Q=t) ∈ supp` | `RSK⁻¹(P=t,Q=s) ∈ supp` |
|---|---|---|---|
| 3 | 6 | 1 | 3 |
| 4 | 24 | 3 | 9 |
| 5 | 120 | 11 | 23 |

The smallest witness is hand-checkable and needs no machine. At `n = 3`, `λ = (2,1)`, `s = t = t^λ`:
then `d(s) = d(t) = 1`, so

    m_{st} = x_λ = T_1 + T_{s₁},     supp = {1, s₁},

while `RSK⁻¹(s,t) = s₂ ∉ {1, s₁}`.

## 3. No leading map works at all — the peeling argument

Suppose `(≤, lead)` satisfied `Triangular`, and let `M` be the maximum of the order. For any index
`x`, `supp_le` gives `supp (m x) ≤ lead x`; so `M ∈ supp (m x)` forces `lead x = M`, and `lead` is
injective, so **`M` lies in exactly one support**. Deleting that index and `M` leaves the same
problem one size smaller. Hence a `Triangular` structure exists **iff** this peeling never stalls —
a forced, deterministic test, implemented as `peel_test`.

At `n = 3` it stalls immediately. The six supports are:

| λ | s | t | `supp (m_{st})` |
|---|---|---|---|
| (3) | `[[1,2,3]]` | `[[1,2,3]]` | `{1, s₁, s₂, s₁s₂, s₂s₁, w₀}` |
| (2,1) | `[[1,2],[3]]` | `[[1,2],[3]]` | `{1, s₁}` |
| (2,1) | `[[1,2],[3]]` | `[[1,3],[2]]` | `{s₂, s₁s₂}` |
| (2,1) | `[[1,3],[2]]` | `[[1,2],[3]]` | `{s₂, s₂s₁}` |
| (2,1) | `[[1,3],[2]]` | `[[1,3],[2]]` | `{1, s₂, w₀}` |
| (1,1,1) | `[[1],[2],[3]]` | `[[1],[2],[3]]` | `{1}` |

Every permutation lies in **at least two** of them — multiplicities `1 ↦ 4`, `s₁ ↦ 2`, `s₂ ↦ 4`,
`s₁s₂ ↦ 2`, `s₂s₁ ↦ 2`, `w₀ ↦ 2` — because `x_{(3)} = Σ_{w ∈ S₃} T_w` already has full support and
the shape-(2,1) and shape-(1,1,1) supports then double every element. So no permutation can be the
order-maximum, and no `Triangular` structure exists. The peel stalls after **0 of 6** indices at
`n = 3`, **1 of 24** at `n = 4`, **5 of 120** at `n = 5`.

## 4. The route that replaces it

Mathas does not use triangularity at all
([`library/hecke-alg/`](../../library/hecke-alg/), *Hecke algebras and Schur algebras of the
symmetric group*, Thm 3.20):

> *"Lemma 3.9 and Lemma 3.14 show that `M` spans `H`. By Theorem 1.11 we know that `H` is a free
> `R`-module of rank `n!`. However `|M| = Σ_λ |Std(λ)|²` and it is well-known that this sum is
> equal to `n!` (for example, use the Robinson–Schensted correspondence). Thus `M` is a basis of
> `H`. We call `M` the Murphy basis of `H`."*

Every ingredient but spanning is already sorry-free here, and the RSK ingredient is the very same
bijection that gave `lead_inj`:

| Mathas' ingredient | corpus declaration | status |
|---|---|---|
| `H` free of rank `n!` | `QOU.Hecke.TwBasis.finrank_eq_factorial` | sorry-free |
| `Σ_λ (f^λ)² = n!` via RSK | `HeckeMurphyYoung.murphyIndex_fintypeCard` | sorry-free (new) |
| the family `m_{st}` itself | `HeckeMurphyYoung.murphyFamily` | sorry-free (new) |
| spanning (Mathas Lemma 3.14) | — | **open — the one remaining input** |
| ⇒ basis | `HeckeMurphyYoung.murphyBasisOfSpanning` | sorry-free (new) |

`basisOfSpanning` / `murphyBasisOfSpanning` / `murphyFamily_linearIndependent` take spanning as an
explicit hypothesis and **derive** the `Module.Basis` from it together with the two counts, via
Mathlib's `basisOfTopLeSpanOfCardEqFinrank`. That is a derivation, not an assumption dressed up as
one: the hypothesis is Mathas' Lemma 3.14 and the conclusion is not among the class fields (§3b-cond
non-degeneracy). All six new declarations report `[propext, Classical.choice, Quot.sound]` under
`#print axioms` — no `sorryAx`.

## 5. What this cost, and the standing lesson

The probe took minutes and refuted a target that would otherwise have absorbed a tranche — the same
outcome as `murphy_lead_injectivity_probe.py` earlier in this arc, which refuted
`lead(λ,s,t) = d(s)⁻¹ w_λ d(t)` at the same cost. Two for two. **Probe the statement before
formalising it** when the statement is a finite claim about small `n`.

The second lesson is the corpus-grep one, now at eight instances in this arc: the SYT-type bridge
`murphyFamily` needed (`QOU.BraidKnot.toBraidKnotSYT`, reconciling the two `StandardYoungTableau`
structures) already existed in `NumSYTBridge.lean`, and Mathas' route was sitting in
`library/hecke-alg/` the whole time. Reading the source cost one grep and changed the plan.
