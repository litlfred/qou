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
| 4 | 24 | 1 | 9 |
| 5 | 120 | 1 | 29 |

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

## 3-bis. 🛑 CORRECTION — the first version of this probe had the wrong handedness

**Recorded because the correction is the useful part.** The first run of the probe computed
`m_{st} = T_{d(s)⁻¹} · x · T_{d(t)}` with a single `d`-direction — inverting on the **left**
only. That family **is not a basis**: a rank test at a generic integer `q` puts it at 19/24
at `n = 4`. So the supports it measured were of the wrong object, and the refutation above
did not yet stand.

A sweep of all sixteen combinations (reference tableau × `d`-direction × which side is
inverted) shows exactly **four** are full rank at `n = 4`, and they are precisely the ones
that invert the two `d`-factors on **opposite** sides. Which side carries the inversion
depends on the direction of `d` itself, so Murphy's own `T_{d(s)}^* x_λ T_{d(t)}` is this
same convention read with the other `d`; **what is convention-independent is that the two
factors are inverted oppositely**. The probe now uses `m_{st} = T_{d(s)} x T_{d(t)⁻¹}` and
carries the rank sweep as a standing guard (`run_rank_guard`).

**The refutation survives the correction and gets stronger.** The `n = 3` support table in
§3 — the load-bearing hand-checkable witness — is byte-identical under both conventions;
they first differ at `n = 4`. The peel now stalls at **0 of 24** and **0 of 120** rather
than 1 and 5, and the `diag_unit` rate is *lower*, not higher. Only the three numbers
corrected above were wrong.

## 3-ter. 🛑 A SEPARATE DEFECT, in `murphyM` on `main` — it cannot be Murphy's element

The rank guard also measures an axis that has nothing to do with handedness, and here the
corpus is wrong. Murphy's `x_λ` is the sum over **one fixed** subgroup — the row stabiliser
of the reference tableau — for every pair `(s,t)` of that shape. `HeckeMurphyYoung.murphyM`
sums over `youngSubgroup n h t`, which is `Specht.rowStab t`: the **second tableau's own**
row stabiliser, a different (conjugate) subgroup for each `t`. Measured at `q = 7`, exact:

| `n` | fixed `x_λ` (Murphy) | `rowStab t` (corpus `murphyM`) |
|---|---|---|
| 3 | **6 / 6** | 5 / 6 |
| 4 | **24 / 24** | 23 / 24 (row-super ref) · 21 / 24 (col-super ref) |
| 5 | **120 / 120** | 117 / 120 (row-super ref) · 112 / 120 (col-super ref) |

Full rank in every fixed-`x_λ` cell, deficient in every `rowStab t` cell, under **both**
reference tableaux and every handedness variant tested. So:

* **The reference tableau does not matter.** Column-superstandard (`colSuperstandard`,
  which the corpus's `dOf` uses) is as good as Murphy's row-superstandard `t^λ`. That axis
  was the first thing suspected and it is a red herring.
* **The subgroup does.** A family summing over `rowStab t` can **never** span `H_n(q)`,
  so it is not the Murphy family, whatever it is called.

**Consequence for the Lean landed in this same PR.** `basisOfSpanning` is stated for an
**arbitrary** family and is unaffected — that genericity was deliberate and is what saves
the work. But `murphyBasisOfSpanning` and `murphyFamily_linearIndependent` specialise it to
`murphyFamily`, which is built on `murphyM`; both remain **true**, and both have a
hypothesis that is now measured **unsatisfiable**. That is exactly the
"conditional-proved ≠ premise-established" trap in AGENTS.md, so they are re-documented in
place rather than left to read as progress. **The fix is at `murphyM`**: sum over the
reference tableau's row stabiliser, not `t`'s. Tracked in bean `qou-phir`.

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
| the family `m_{st}` itself | `HeckeMurphyYoung.murphyFamily` | sorry-free, but **wrong family** — see §3-ter |
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

**The sharper lesson is §3-bis and §3-ter, and it is about the probe, not the target.**
A probe that measures a rich structural property of an object — supports, orders, peelings —
says nothing at all if the object is the wrong one, and it will not announce that it is
wrong: it returns a perfectly well-formed table either way. The cheap invariant that
discriminates here is a **rank test**, seconds of exact arithmetic, and it is what caught
both a wrong handedness in this probe and a wrong subgroup in `murphyM` on `main` — the
latter after the Lean built on it had already been written, verified sorry-free, committed,
and described in a PR body as Murphy's family. Sorry-free and wrong are entirely compatible.
**Before measuring a structure on a family, measure that the family is the family**; the
guard is now `run_rank_guard` in the probe.

The second lesson is the corpus-grep one, now at eight instances in this arc: the SYT-type bridge
`murphyFamily` needed (`QOU.BraidKnot.toBraidKnotSYT`, reconciling the two `StandardYoungTableau`
structures) already existed in `NumSYTBridge.lean`, and Mathas' route was sitting in
`library/hecke-alg/` the whole time. Reading the source cost one grep and changed the plan.
