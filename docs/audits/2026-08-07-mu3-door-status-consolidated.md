# The μ₃ sign door — consolidated status (2026-08-07)

**Scope.** Single record of where the μ₃ three-body cluster sign door stands, consolidating
results that are currently scattered across PRs [#4404], [#4617], [#4651], [#4657], [#4662].
Written because the arc had reached the point where "what is actually still open" could no
longer be answered without reading five PR bodies in order.

**Bottom line.** The door is closed against a large, precisely-delimited class of operators —
and the one surviving escape has been identified, given a governing rule, and had that rule
proved. It is **not** closed in general, and this document says exactly where the remaining
freedom lives.

---

## 1. What the door is

`Mu3ClusterModularity` ([#4404]) reframed the open μ₃ question as an exact equivalence.
With `c₃ = −E₀·Δ²g` and

    Δ²g = g_ab − g_a − g_b + g_∅

the positive residual moment is reachable **iff** the joint block-trace is strictly
**submodular**:

    μ₃ > 0  ⟺  Δ²g < 0                        (`cluster_pos_iff_submodular`)

This is the whole content of the door. Everything below is about which operators can supply
`Δ²g < 0`.

## 2. What is closed

### 2.1 The per-block multiplicatively-damped class — pair term ([#4651])

If each Wedderburn block is damped multiplicatively by the two bonds, that block's own second
difference is

    Δ² = +c(1−r_a)(1−r_b) ≥ 0                 (`multiplicative_second_diff`)

and `Δ²` is **linear over blocks** (`secondDiff_sum`), so the total is non-negative. Hence a
submodular total *forces* a block with its own `Δ²_λ < 0`
(`submodular_needs_interfering_block`).

In damping coordinates the criterion is sharp: a block is submodular **iff** its joint damping
factor falls strictly below the **Fréchet–Hoeffding lower bound**,

    r_ab < r_a + r_b − 1                      (`block_submodular_iff_below_frechet`)

which is *strictly stronger* than merely beating multiplicative damping, since
`r_a + r_b − 1 ≤ r_a·r_b` for `r ∈ [0,1]` (`frechet_le_multiplicative`). An interfering block
must damp **more**, not less.

> **Direction note.** An earlier framing of this result described interfering blocks as damping
> "sub-multiplicatively — joint effect weaker than the product". That is backwards, and the
> formalization is what caught it: submodular ⟺ `r_ab < r_a + r_b − 1 ≤ r_a·r_b`, i.e. strictly
> *more* damping. Recorded here so the wrong direction does not get re-derived.

### 2.2 The same class under the GAP-7 slot correction ([#4657])

GAP-7 (`UrsellSlotAlignment.triangle_moment_decomp`) established that `μₖ` is indexed by
*particle* count while `Δᵐg` is indexed by *bond* count, so the triangle's correct assembly is

    μ₃-slot = ∑_{pairs} Δ²g + Δ³g

This is **not** a formality, because the third difference of a multiplicative block carries the
**opposite sign**:

    Δ³ = −c(1−r_a)(1−r_b)(1−r_c) ≤ 0          (`thirdDiff_multiplicative`)

so the triple term pushes *toward* the door. It never wins:

    ∑Δ² + Δ³ = c(uv + uw + vw − uvw) ≥ 0      (`slot_nonneg_multiplicative`)

by factoring as `uv(1−w) + uw + vw`, with `u,v,w = 1−r ∈ [0,1]`. GAP-7 had *measured* that the
correction "roughly doubles the magnitude but preserves the sign" on two isotopes; this proves
sign-preservation for the whole class.

### 2.3 A=2 ([#4617], parallel route)

The door is identically **vacuous** at A=2 — there is no third bond, so the construction has no
content there. Independent route, consistent with the above.

## 3. What is measured, not proved

The per-block Fréchet probe ([#4657], `mu3_frechet_perblock_probe.py`) runs the §2.1 criterion
on the operator [#4404] measured — the adjacent H₉ `|χ|` joint-trace — for both A=3 isotopes.
Gates: linearity `Σ_λΔ²_λ = Δ²g`, factorisation `Δ²_λ = y_λ·Δ²|χ|_λ`, and the committed
baseline `c₃ = −1.7688 (T) / −1.4054 (³He)` vs `−1.769 / −1.405`. All pass.

**Fréchet-violating blocks exist and are named** — the interfering block whose existence
`submodular_needs_interfering_block` requires is realised in this operator's own spectrum:

| isotope | violating λ | Fréchet slack |
|---|---|---|
| T | (3,2,2,1,1) | −7.75e-2 |
| T | (3,2,1,1,1,1) | −6.15e-2 |
| T | (3,2,2,2) | −4.61e-2 |
| ³He | (8,1) | −3.28e-2 |
| ³He | (2,2,2,1,1,1) | −1.30e-2 |
| ³He | (2,2,2,2,1) | −4.84e-3 |

**The violator sets differ between the two isotopes.** This is an honest negative on the "one
universal interfering family" hypothesis — whatever produces these blocks is isotope-dependent.
The **total** still sums supermodular in both cases, so this does not by itself open the door.

## 4. What is open — and what now governs it

### 4.1 The mixed-sign-weight escape

`Mu3SlotExclusion.reweight_cannot_open_door` proves that a non-negative re-weighting of
Fréchet-obeying blocks stays supermodular. **Its hypothesis `w_λ ≥ 0` is false on the physical
spectrum**: the Jones–Markov weights are sign-indefinite for `n ≥ 4`
([`2026-05-19-weight-factor-audit.md`] §W3), and at `n = 9, q₀` exactly **10 of 30 are
negative**. So that lemma does not foreclose the "change the Wedderburn weights" escape for the
actual trace.

The honest replacement is the exhaustive classification
(`Mu3SlotExclusion.door_mechanism_dichotomy`): a block pushes the total submodular in exactly
one of two ways —

| mechanism | reading |
|---|---|
| `w_λ > 0` and `Δ²\|χ\|_λ < 0` | a genuine **Fréchet–Hoeffding violation** (the geometry is submodular) |
| `w_λ < 0` and `Δ²\|χ\|_λ > 0` | a **negative Wedderburn weight** on supermodular geometry — no Fréchet violation at all |

and **the second dominates at A=3**: 7 (T) / 9 (³He) of the submodular pushes are bookkeeping
sign, not geometry. Conflating the two reports a sign convention as a geometric fact.

### 4.2 The governing sign is now a proved rule ([#4662])

A mechanism whose governing sign has no rule has no budget. §W3's "sign-indefinite for n ≥ 4"
is now upgraded to a combinatorial statement, proved sorry-free from the Wenzl principal
specialisation. For `q > 1` (so `Q = q² > 1`):

* every hook `h(x) ≥ 1` ⟹ every denominator factor `1 − Q^{h(x)}` is negative ⟹ the
  denominator contributes the fixed sign `(−1)^{|λ|}`, depending on the **cell count alone**;
* a numerator factor is negative exactly when `Q^r·Q^{c(x)} > 1`, i.e. exactly **above** the
  content threshold `c* = −log_Q(Q^r)`.

Writing `P(λ)` for the count of cells *below* the threshold, these merge to

    sign(s_λ) = (−1)^{P(λ)}                   (`YLambdaSignThreshold.wenzl_sign`)

At q₀ the cut is `c* = −2.5995`, so `P(λ)` counts cells of content `≤ −3` — which require
**≥ 4 rows**. Hence every `λ` with `ℓ(λ) ≤ 3` carries a positive weight
(`shallow_of_no_deep_cells`).

> **The invariant is depth, not part-count.** The measured n=9 split looks like `ℓ`-parity with
> `ℓ=2` as an exception, and that reading is wrong: `(8,1)` has `ℓ=2` but *zero* deep cells, so
> it is positive; `(5,2,1,1)` has `ℓ=4` and exactly one deep cell, so it is negative. The proof
> supplied the correct invariant; the numerics alone suggested the wrong one.

Machine-verified on **all 270 partitions for n = 2..12**, smallest threshold margin `8.0e-2`
against a `1e-12` degeneracy guard.

### 4.3 The residual holes

1. **`sign(Z)` is not derived.** `y_λ = s_λ/Z`, so §4.2 pins `sign(y_λ)` only up to one global
   sign per `n`. The probe *verifies* `sign(Z) = +1` for n = 2..12; nothing proves it.
2. **The quantitative budget is not closed.** At n=9, q₀ the negative-weight mass is small:
   `Σ|y_λ^-| = 4.21e-4` against `Σ y_λ^+ = 3.22e-2` (**1.31 %**), and the largest negative
   weight is **52.5×** smaller than the largest positive. The total sits at `Δ²g = +0.4225` (T)
   with the negative-weight blocks supplying ≈ `−0.011`, so the route needs roughly **40×**
   more than it currently delivers. This is **not an exclusion** — the door depends on
   `y_λ·Δ²|χ|_λ` products and the geometry factor ranges over five orders of magnitude
   (`3.6e-4` to `8.4e+1`). It is a *named target*.
3. **Class membership is not established.** §2 excludes the per-block multiplicatively-damped
   class. Nothing shows the H₉ `|χ|` joint traces lie in it — §3 shows some blocks do not.

## 5. Scope discipline

Per AGENTS.md §"Before declaring refuted / ruled out / dead end":

* **§2.1, §2.2 are scope-(b) structural exclusions** — each cites a proved invariant
  (non-negativity of `Δ²`, resp. of `∑Δ² + Δ³`, on the stated class). They exclude an
  *operator class*, not an *ingredient*.
* **§3 is a scope-(a) scope-limited negative** — "the violator sets differ between isotopes"
  constrains this operator at these two isotopes; it does not exclude a universal interfering
  family in general.
* **§4 is open, not refuted.** The mixed-sign escape is live. The 40× figure is a budget, not a
  bound — writing it up as an exclusion would be exactly the over-narrowing the discipline
  guards against.

Nothing in this arc is fitted and nothing is wired to production. No `Δ_λ` closure is claimed;
no `μ₃` value is fitted.

## 6. Artifacts

| PR | contribution |
|---|---|
| [#4404] | `Mu3ClusterModularity` — the door *is* (sub/super)-modularity |
| [#4617] | A=2 vacuity (parallel route) |
| [#4651] | `Mu3BlockwiseExclusion` — pair-term exclusion + the Fréchet threshold |
| [#4657] | `Mu3SlotExclusion` — survives the GAP-7 slot correction; per-block Fréchet probe; the mixed-sign correction |
| [#4662] | `YLambdaSignThreshold` — `sign(y_λ)` proved to be a content-threshold parity |

Lean: `QOU/MassTheory/{Mu3ClusterModularity, Mu3BlockwiseExclusion, Mu3SlotExclusion,
YLambdaSignThreshold}.lean` — all sorry-free.
Compute: `computations/deltalambda/{mu3_frechet_perblock_probe,
ylambda_sign_content_threshold_probe}.py` + witnesses.

[#4404]: https://github.com/litlfred/qou/pull/4404
[#4617]: https://github.com/litlfred/qou/pull/4617
[#4651]: https://github.com/litlfred/qou/pull/4651
[#4657]: https://github.com/litlfred/qou/pull/4657
[#4662]: https://github.com/litlfred/qou/pull/4662
[`2026-05-19-weight-factor-audit.md`]: 2026-05-19-weight-factor-audit.md
