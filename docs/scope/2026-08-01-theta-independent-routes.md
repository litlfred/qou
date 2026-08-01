# Independent ϑ routes: the Rademacher symbol is out, and the arc has an A-free target

**Date:** 2026-08-01 · **Axis:** ϑ_K gap (`qou-qnnq`) · **Beans:** `qou-rdmr`, `qou-offl`
**Tier:** scope-(a) refutation + a derived falsifiable constraint. Nothing wired; nothing fitted.

Follows [`2026-08-01-t4-anchor-circularity.md`](2026-08-01-t4-anchor-circularity.md),
which established that `A_ω` and `ϑ_K` are **one** degree of freedom and that the
arc therefore needs a leg that determines ϑ *without* `A_ω`.

## 1. The Rademacher symbol vanishes on both anchors

Ghys ("Knots and dynamics", ICM 2006) identifies `B₃ ≅ π₁(T¹M)` for the modular
orbifold; a conjugacy class in `PSL(2,ℤ)` gives a modular knot whose linking
number with the trefoil is the **Rademacher function** `Φ`. `qou-rdmr` proposed
`Φ` as the word → winding map, and its input — the braid word — is genuinely
independent of `A_ω`, so it was a legitimate candidate for an independent leg.

**The binary precondition passes.** Per
[`qbeta_t3_multiknot_binding_probe.py`](../../computations/qbeta/qbeta_t3_multiknot_binding_probe.py)
the corpus assigns `electron → 3₁`, `muon → 4₁`, `proton → 𝔹₃` (Borromean). The
two channel anchors are therefore two *different* braid words, so a word → number
map is not excluded on its face. (The `qou-rdmr` bean text attributing both
anchors to 4₁ is wrong and is corrected in the bean.)

**But `Φ` is blind to the family.** Both canonical words are `(σ₁σ₂⁻¹)ⁿ` — 4₁ at
`n = 2`, 𝔹₃ at `n = 3`. Under `σ₁ ↦ R`, `σ₂ ↦ L⁻¹` the image is `(RL)ⁿ`, an
RL-*balanced* word, and the Rademacher function of a word in `R, L` is
`Φ = Σaᵢ − Σbᵢ`. Hence `Φ((RL)ⁿ) = n − n = 0` for every `n`.

[`qbeta_rdmr_rademacher_winding_probe.py`](../../computations/probes/qbeta_rdmr_rademacher_winding_probe.py)
confirms this three independent ways — the Dedekind-sum formula in exact
`Fraction` arithmetic, the RL-word count, and homogeneity `Φ(Aⁿ) = n·Φ(A)`:

| knot | n | SL(2,ℤ) image | trace | Φ |
|---|---|---|---|---|
| 4₁ (muon) | 2 | `((5,3),(3,2))` | 7 | **0** |
| 𝔹₃ (proton) | 3 | `((13,8),(8,5))` | 18 | **0** |

So `Φ` predicts `ϑ = 0` for both, and — the decisive point — it cannot even
**distinguish** the two anchors, which is the minimum any word → ϑ map must do.

**Scope is (a), not (b).** This refutes the Rademacher *symbol* as the ϑ source.
It does **not** refute the Ghys word → winding programme: a different
quasimorphism, or the full linking datum rather than its Rademacher shadow,
remains open. The braid word does carry independent information — the
precondition passed — `Φ` is simply not the functional that extracts it.

**Method note.** The gate earned its keep. The first run bound `σ₂⁻¹` to `L⁻¹`
rather than `L` (i.e. to `σ₂`), sending `σ₁σ₂⁻¹` to `((0,1),(−1,1))` instead of
`RL` and producing a spurious `Φ = −2` for 4₁. The two cross-checks contradicted
it and the gate assertion failed. A single-method computation would have
reported that `−2` as a signal.

## 2. The chain does carry one falsifiable, A-free statement

The circularity note left the arc looking contentless. It is underdetermined,
but underdetermined is not contentless. Eliminating `A_ω` between the two anchor
equations of `S_K = A_ω·κ·(ln²q₀ − ϑ_K²)` leaves a relation with no free
parameter:

> **(∗)** `(ln²q₀ − ϑ_μ²) / (ln²q₀ − ϑ_p²)  =  S_μ / S_p  ≡  r`

`r = −0.2453912076` is built from the two **measured** `S` values alone — it
contains neither `A_ω` nor `q₀`. Solved for the proton coordinate,
`ϑ_p² = L − (L − ϑ_μ²)/r` with `L = ln²q₀`.

This is the arc's actual target, and it changes what an independent route has
to do:

1. **A route supplying both ϑ values is testable with no conditioning
   inherited** — on the curve or off it, `A_ω` never enters.
2. **A route that lands on the curve *determines* `A_ω`** via
   `A_ω = S_μ/(κ(L − ϑ_μ²))`. That would be this arc's first genuine
   determination rather than a literature import.

[`qbeta_qnnq_afree_theta_constraint_probe.py`](../../computations/probes/qbeta_qnnq_afree_theta_constraint_probe.py)
derives the curve, passes the C0 control (the T4 pair lies on it, residual
1.3 × 10⁻⁸, limited by the 8-digit ϑ values — it must, by construction), and
tabulates the one-parameter family:

| A | ϑ_μ | ϑ_p | ϑ_p/ϑ_μ |
|---|---|---|---|
| 2.10 | 0.016737 | 0.233072 | 13.93 |
| 3.00 | 0.058946 | 0.203235 | 3.448 |
| 10.00 | 0.093233 | 0.141568 | 1.518 |

Every row satisfies both anchors **exactly**. Nothing in the T4 chain picks a
row — that is the one degree of freedom, made concrete. The only internal
constraint remains the one-sided `A ≥ A_crit = 2.046` (2.054 on the canonical
`q₀` grid), from `ϑ_μ` reality.

### 2.1 This upgrades the rdmr refutation to A-free

`qou-rdmr` predicts `ϑ_μ = ϑ_p = 0`. At `ϑ_μ = 0` the curve **forces**
`ϑ_p = 0.23551`, not 0. So the Rademacher symbol is off the curve and is refuted
**without assuming `A_ω = 3`** — §1's verdict no longer rests on
`A_ω`-conditioned targets.

### 2.2 A q₀ discrepancy worth fixing separately

[`qbeta_t4_stokes3_crux_probe.py`](../../computations/qbeta/qbeta_t4_stokes3_crux_probe.py)
hardcodes `q₀ = 1.11020` ("from NZ probe: u_test = 0.209") against the canonical
substrate `q₀ ≈ 1.1099786`. `r` is `q₀`-free so (∗) is unaffected, but the curve
is not: `L` and `A_crit` shift in the fourth digit. Both grids are reported in
the witness. Not corrected here — it belongs with the T4 probe's other
hardcoded-literal issues already flagged `genuine` in the circular-anchor ledger.

## 3. What this means for `qou-offl` (cone-manifold / generalized Dehn filling)

`qou-offl` is now the arc's live independent leg, and (∗) gives it a **well-posed
acceptance test** it did not have before:

> Produce ϑ for **both** 4₁ and 𝔹₃ from cone-manifold geometry alone — no `A_ω`,
> no T4 inversion — and check the pair against (∗). Landing on it determines
> `A_ω`; missing it refutes the route at scope (a).

### 3.1 A whole shape of candidate is already ruled out

Before running any geometry — formalize-first, narrow the search — the counting
settles which *shapes* of cone-manifold answer can be tested at all. Two
equations, three unknowns: **one** extra scalar closes the system exactly, with
zero residual and nothing left to check; **two** over-determine it by one and
leave a residual that can fail.

So a route that supplies a **ratio** `ϑ_p/ϑ_μ` from some geometric quantity is
**unfalsifiable by construction**.
[`qbeta_offl_ratio_candidates_unfalsifiable_probe.py`](../../computations/probes/qbeta_offl_ratio_candidates_unfalsifiable_probe.py)
makes that concrete rather than merely asserting it: `ρ(A) = ϑ_p/ϑ_μ` is
monotone decreasing, running from ≈ 598 as `A → A_crit⁺` down to 1.005 at
`A = 1000` — a **bijection** from `A ∈ (A_crit, ∞)` onto `ρ ∈ (1, ∞)`. Every
ratio above 1 is attained by exactly one `A`. No ratio candidate can therefore
be refuted; it can only *name* an `A`. (Inversion round-trip verified exact,
10⁻⁶⁹ relative.)

The practical damage is worse than the formal point. Plausible parameter-free
geometric ratios **cluster**:

| candidate ratio | ρ | A it forces |
|---|---|---|
| Vol(𝔹₃)/Vol(4₁) | 3.6099 | 2.909 |
| 2√3 (\|cusp modulus\| of 4₁) | 3.4641 | 2.990 |
| cusp count 3/1 | 3.0 | 3.344 |
| √(Vol ratio) | 1.8999 | 6.025 |
| crossing number 6/4 | 1.5 | 10.35 |
| \|disc\| 4/3 | 1.3333 | 15.40 |

Three of six land in `A ∈ [2.5, 4]`. That is not a menu to pick from — it is
the warning. The whole range `A ∈ [2.5, 4]` is a mere ~2× band in `ρ`,
`[2.513, 4.887]`, so a ratio landing "near 3" is close to guaranteed and is
weak evidence **even when the quantity was fixed in advance**. Anyone reaching
for the 2√3 row because it forces `A = 2.990` should read this paragraph again.

### 3.2 The two hazards that remain

- **Re-parameterization.** If the geometric ϑ carries its own free
  normalization constant, the route has moved the degree of freedom rather than
  removing it. The test is immune *only* if the normalization is fixed before
  the comparison. State it up front, as `qou-rdmr` did.
- **Single-anchor fitting.** Any route can hit *one* ϑ by choosing its
  normalization. (∗) is a genuine test precisely because it constrains the
  **pair**.

**Net requirement for `qou-offl`:** supply **both** ϑ values **absolutely**,
from a normalization fixed in advance. The derivation itself is open; what this
note contributes is the target, the shape constraint, and the hazards.

## Cross-references

- Beans: `qou-qnnq` (the gap), `qou-rdmr` (refuted at scope (a)), `qou-offl` (live).
- [`2026-08-01-t4-anchor-circularity.md`](2026-08-01-t4-anchor-circularity.md) — the one-degree-of-freedom finding this builds on.
- [`2026-08-01-aomega-three-test-illposed.md`](2026-08-01-aomega-three-test-illposed.md) — why the `A_ω = 3` side has no cheap well-posed test either.
- AGENTS.md §"Before declaring refuted" (the (a)/(b) discipline); §anti-fit.
