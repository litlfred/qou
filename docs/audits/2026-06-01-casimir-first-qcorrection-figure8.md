# Audit: the first Casimir q-correction is carried by 4_1 — the substrate-defining knot

**Date.** 2026-06-01
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Builds on.** [`2026-06-01-casimir-free-field-disjoint-grounding.md`](2026-06-01-casimir-free-field-disjoint-grounding.md)
**Witness.** [`casimir-d6-qcorrection-structure.witness.json`](../../computations/casimir-d6-qcorrection-structure.witness.json)
**Result.** The leading 1/d⁴ Casimir term is q-free; the **first** q-correction
requires a hyperbolic (interacting) braided mode. The minimal such mode is the
figure-eight knot **4_1** — which is *also the knot that defines the substrate
q₀*. Its q-weight is `J_{4_1}(q) = 1 + (3/4) h² + O(h⁴)`, with the leading
coefficient **exactly 3/4**. The absolute 1/d power and magnitude remain open
(the interacting mode-sum).

## Where the leading term left off

PR #1540 + #1596 established: the leading 1/d⁴ Casimir term is the disjoint-unknot
(free-photon) mode-count — q-free, `ξ_k = 0`. q-deformation enters only when modes
**braid** (interact), i.e. degree-≥2 braid words, which by
[`lem:degree-one-braid-trivial-volume`](../../content/quantum-observable-universe/mass-theory/degree-one-braid-trivial-volume.md)
are the first that can be hyperbolic (carry nonzero Vol, hence substrate-q
dependence). This audit asks: *what is the first such correction?*

## Torus closures contribute nothing

Degree ≥ 2 is necessary for hyperbolicity but not sufficient. The minimal
degree-≥2 closures are all **torus** links/knots, with Vol = 0:

| closure | braid | crossings | Vol | hyperbolic? |
|---|---|---|---|---|
| Hopf link | σ₁² | 2 | 0 | no — torus (2,2) |
| trefoil 3_1 | σ₁³ | 3 | 0 | no — torus (2,3) |
| **figure-8 4_1** | σ₁σ₂⁻¹σ₁σ₂⁻¹ | 4 | **2.029883** | **yes — minimal hyperbolic** |
| 5_1 | σ₁⁵ | 5 | 0 | no — torus (2,5) |
| 5_2 | σ₁²σ₂σ₁⁻¹σ₂ | 5 | 2.82812 | yes |

So no q-correction arises from the 2- and 3-crossing braided modes. **The first
hyperbolic mode is the figure-eight knot 4_1** — the unique minimal-volume
hyperbolic knot, `Vol(4_1) = 2·Cl₂(π/3)`.

## The first q-correction is tied to the substrate-defining knot

4_1 is not an arbitrary choice. The substrate parameter q₀ is fixed by

$$
\frac{m_p}{m_e} = 2\,\frac{\mathrm{Vol}(4_1)}{\hbar_q^2}\,F_{\mathrm{Bor}}(q) - 12
\qquad (\texttt{qou\_substrate.constants})
$$

— the *same* `Vol(4_1) = 2·Cl₂(π/3)` that is the minimal hyperbolic volume.
Therefore the **first Casimir q-correction and the substrate parameter q₀ are
governed by one and the same hyperbolic invariant.** The interacting Casimir
correction is not an independent new scale; it is anchored to the knot that
already fixes the framework's one free parameter — a structural
self-consistency.

## The q-weight: J_{4_1}(q) = 1 + (3/4) h² + O(h⁴), exact

The substrate weight a braided mode carries is its Markov trace = Jones
polynomial. For 4_1,

$$
J_{4_1}(q) = q^{-2} - q^{-1} + 1 - q + q^{2}.
$$

In the skein variable `h = q − q⁻¹` (so `q²+q⁻² = h²+2`, `q+q⁻¹ = √(h²+4)`),

$$
J_{4_1} = (h^2+2) - \sqrt{h^2+4} + 1 = h^2 + 3 - \sqrt{h^2+4},
\qquad
\frac{dJ_{4_1}}{d(h^2)}\Big|_{h=0} = 1 - \frac{1}{2\sqrt4} = \frac34 .
$$

(The identity `J_{4_1} = h²+3−√(h²+4)` is verified to 40 digits in the witness.)
Hence

$$
\boxed{\,J_{4_1}(q) = 1 + \tfrac34\,h^2 + O(h^4)\,}
$$

— the first q-correction's relative **weight** grows as `(3/4) h²`, i.e.
`≈ 3.28 %` at q₀. The leading coefficient `3/4` is exact, not fitted.

## The 3/4 is exact algebra, not a fit — Lean-proved

To answer the "sounds like fitting" concern directly: the `3/4` is forced by an
exact field identity, formalised in
[`QOU.AppendixSurreals.FigureEightCasimirWeight`](../../content/quantum-observable-universe/lean/QOU/AppendixSurreals/FigureEightCasimirWeight.lean):

```lean
theorem jones41_three_quarters_cleared (q : ℝ) (hq : q ≠ 0) :
    (4 * (jones41 q - 1) - 3 * (q - q⁻¹) ^ 2) *
        ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹))
      = (q - q⁻¹) ^ 4 := by
  unfold jones41; field_simp; ring
```

i.e. `4(J−1) − 3h² = h⁴ / (h² + 8 + 4(q+q⁻¹))`, with the remainder denominator
proved strictly positive for `q > 0` (`jones41_remainder_denom_pos`). The proof
is `ring` after clearing `q⁻¹` — **there is no fitted constant**; `3/4` is the
unique coefficient that makes the residual `O(h⁴)`. The identity was first
checked exactly in rational arithmetic (`LHS − RHS = 0` for all test `q`), then
discharged by `field_simp; ring`.

**What is fitting-free vs. what is structural input.** The `3/4` *given* the
weight `J_{4_1}` is exact algebra (above). What is *not* algebra is the
**identification** of `J_{4_1}` as the first-correction weight — that rests on
the physical chain: Casimir = free field ⇒ leading disjoint-unknot count (q-free,
grounded in QOU's photon representation, PR #1596); first interacting correction
= first hyperbolic braided mode = `4_1`, weighted by its Markov trace. That chain
is a structural derivation, not a fit, but it is not itself a Lean theorem — it
is the modelling content the conjecture still rests on.

(Note: the same `3/4` appeared in the original ξ_2 source survey as Source A
[`linking_weight_A = 5/2 + 3h²/4`]. There it was *not applicable* to the
**leading** Casimir term, because that term is built from **disjoint** unknots
with `linking_weight = 1`. It reappears here, correctly, at the **interacting**
level — the regime where linked/hyperbolic structure, and hence the `3/4`, does
apply.)

## Honest scope — what this does and does not establish

**Established:**
1. The first q-correction exists only at the hyperbolic / interacting level
   (torus modes contribute 0).
2. It is carried by 4_1 — the substrate-defining knot.
3. Its q-weight is `J_{4_1}(q) = 1 + (3/4)h² + O(h⁴)`, exact leading 3/4.

**Not established (still open):**
- The absolute power of 1/d (the "1/d⁶" label is the standard radiative-correction
  expectation, not yet derived) and the overall magnitude. These require the
  **interacting-mode mode-sum** — the Yekutieli-homotopy lift of N_⊙ restricted
  to degree-≥2 (hyperbolic) closures, which is the same open construction flagged
  for the leading term. This audit gives the q-**weight** and the structural
  identification, **not** a numerical Casimir coefficient.

## Status delta

| Item | Before | After |
|---|---|---|
| first q-correction order | "1/d⁶, interacting modes" (asserted) | first hyperbolic mode identified = 4_1; torus modes shown to contribute 0 |
| q-weight of that correction | unknown | `J_{4_1}(q) = 1 + (3/4)h² + …`, exact leading 3/4 |
| tie to substrate | — | 4_1 = the knot defining q₀ (Vol(4_1)) — self-consistency |
| absolute 1/d coefficient | open | still open (interacting mode-sum) |

## Next

- The interacting-mode mode-sum: extend the disjoint-count construction to
  degree-≥2 closures, weighting each by `J_K(q)` and `Vol(K)`, and recover the
  power of 1/d. This is the concrete next target — and it now has a known
  leading term (4_1, weight `1 + (3/4)h²`) to anchor against.
