import QOU.Mass.HyperbolicSurfaceLaw
import Mathlib.Tactic

/-!
# QOU.Mass.StokesSingularCountAffine — Euler's formula bounds the Stokes singular locus below by an affine function of `A`, so the non-abelian-Stokes surface term renormalises the volume coefficient

`QOU.Mass.HyperbolicSurfaceLaw` bridged Yekutieli's non-abelian Stokes estimate to the bulk
criterion: the estimate splits into a **good** term counted by the `4^k` kites of the tessellation
(an area count) and a **bad** term bounded by the number of **singular points** of the surface map
(`|bad| ≤ m`; `bad = ∅` if the map is linear), one dimension down. The 2026-08-30 audit reads the
surface coefficient `a_S` as proportional to that singular count for the spanning surface of the
nuclear braid closure, and bean `qou-yc1m` asks the question nobody had answered: **how does that
count scale with `A`?**

This file answers it without choosing a parametrization, because the answer does not depend on one.

## 🛑 First, a correction to the reading this file inherited — including from my own #6929

The 2026-08-30 audit, and `HyperbolicSurfaceLaw`'s header repeating it, said the bad set is
"counted by the singular points of the map defining the surface". **That is the 1-dimensional
string case** (held text, `sec-000-0-introduction.md:2280`: *"Let m be the number of singular
points of the map σ. Then |bad(k)| ≤ m."*). In the **2-dimensional** case the kite map
`τ : I² → X` is *linear by definition* (Def 4.1.1, `:3278`) and has no singular points at all;
there, Def 4.4.12 (`:3964`) makes an index **good iff the forms `α|Zᵢ` and `β|Zᵢ` are smooth**,
and Lemma 4.4.13's proof (`:3969-3976`) covers *"the singular locus of α and the singular locus of
β"* by `m` line segments `Zⱼ` and sets **`a₀ := 2m`, `a₁ := 2·Σ len(Zⱼ)`**. So:

* the bad set is the singular locus of the **connection**, not of the surface parametrization;
* `a₁` is a **length**, not a count — "`a_S ∝` a count" can only refer to `a₀`;
* **if `(α, β)` are smooth, `a₀ = a₁ = 0` on every surface at every `A`** — the Stokes route
  then supplies **no surface term of any size**. A Stokes surface term *requires a singular
  connection*, and the corpus has no `(α, β)` as forms at all (bean `qou-20bk`: *"Step 2's
  curvature is stipulated, not a form"*).

The Euler argument below is correct as mathematics; what it says about the Stokes surface term is
therefore **conditional on a hypothesis about the connection**, stated as `hsing` in the theorem
and named here so it is not mistaken for a derived fact.

## The argument, with its hypothesis in the open

Whatever kites are used, they are glued along a **cell decomposition** of the surface — `V`
vertices, `E` edges, `F` faces. Euler's formula gives, for **any** decomposition with at least one
vertex and one face,

    E = V + F − χ  ≥  2 − χ                                   (`edges_ge_two_sub_chi`)

and the canonical closure's Seifert surface has **`χ = −9A + 1`** — not measured but *computed*
from `n = 3A` disks and `12A − 1` bands, both of which the corpus derives for all `A`
(`qou-hu1f`: *"`11A + (A−1) = 12A − 1`; the fit was right and is now derived"*), so

    E  ≥  9A + 1                                              (`edges_ge_of_chi_canonical`)

**The 1-skeleton of any cell decomposition of the spanning surface grows at least linearly in
`A`.** That bound is sharp (the one-vertex polygon presentation attains it) and it generalises two
exact counts the corpus already holds — `AffineCountIsNotASurfaceTerm.crossingCount = 12A − 1` and
`TransverseSurfaceCurvature.seifertBettiOne_extensive`, which is `1 − χ` affine for all `A` — from
one decomposition to all of them. It is not a new number.

**(H1) The hypothesis:** that the singular locus of the connection forms `(α, β)` runs along the
1-skeleton of some cell decomposition of the surface, so that the bad-set constant `a₀ = 2m`
inherits the Euler bound `m ≥ E ≥ 9A + 1`. Under (H1), against the Seifert surface's own cells
`3A + (12A − 1) = 15A − 1`, the boundary/bulk ratio is bounded below by something tending to
`3/5`, never to `0`, and **the Stokes singular count is not a surface term**
(`stokes_canonical_not_surfaceTerm`): like the hyperbolic ball, it renormalises the volume
coefficient and supplies no `A^(−1/3)`.

## Scope — three tiers, kept apart

* **Proved (scope-(b), the invariant is Euler's formula):** the edge lower bound for every cell
  decomposition; that a boundary count bounded below by an affine function with positive slope,
  over a bulk count bounded above by an affine function, has a ratio that does not vanish and so
  fails `StokesSurfaceTerm`; and the instantiation at the canonical closure's counts.
* **Derived inputs, cited not measured:** `n = 3A`, `c = 12A − 1`, hence `χ = −9A + 1`, `2g = 8A`
  with `μ = A + 1`. **One trap in the corpus, recorded here:** `μ = A + 1` is carried as a
  *hypothesis* `(hmu : mu = A + 1)` in `SLq2LabelParity.lean:77` and `TorusKnotPages.lean:82`, yet
  `total_curvature_is_the_computable_half_probe.py:43` and its witness cite it as *"(exact,
  Lean-proved)"* — conditional-proved ≠ premise-established. The probe-level derivation is
  `the_canonical_closure_is_a_chain_of_torus_links_probe.py:40-55`; no Lean proves it.
* **(H1), NOT discharged and not currently dischargeable (scope-(a)):** the corpus has no
  connection forms, so nothing can be said about where they are singular. This file gives the
  criterion and the bound; it cannot supply the premise. **Two ways out, both named:** a connection
  smooth on the surface, which gives `a₀ = a₁ = 0` and *no* Stokes surface term at all; or a
  singular locus that is a proper sub-complex of *sublinear* total edge count — which Euler forbids
  for the whole 1-skeleton but not for a subset, so (H1) is genuinely where the content is.
* **The only escape from the Euler bound itself** is a spanning surface with `χ` sublinear in `A`,
  i.e. genus growing slower than `A`; none is proposed anywhere in the corpus, and for the
  canonical closure `g = 4A` is derived.
* **Not a fit.** No coefficient appears.

So the two routes the owner asked to be connected — the hyperbolic ball and the surface of kites —
end in the same place for the same structural reason, **to the extent the Stokes one is a surface
term at all**: each has a boundary that is a fixed fraction of its bulk, the ball because
`S/V ≥ 2` in `H³` (proved, unconditional), the Stokes surface because Euler pins its 1-skeleton to
`≥ 2 − χ` edges with `χ` affine (proved, conditional on (H1)).

Ground ring: `ℤ` for the counting, `ℝ` for the limit.

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/HyperbolicSurfaceLaw.lean
-- Ref: [leitner2026] docs/audits/2026-08-30-nonabelian-stokes-and-the-surface-term.md
-- Ref: [leitner2026] computations/probes/every_seifert_invariant_is_affine_probe.py (χ = −9A+1, six nuclei)
-- Ref: [yekutieli2015] A. Yekutieli, Nonabelian multiplicative integration on surfaces (Def 4.4.12, Lemma 4.4.13)
-/

namespace QOU.Mass.StokesSingularCountAffine

open Filter QOU.Mass.HyperbolicSurfaceLaw

/-! ## Euler's formula lower-bounds the cut locus -/

/-- **Any cell decomposition with a vertex and a face has at least `2 − χ` edges.** Pure Euler. -/
theorem edges_ge_two_sub_chi (V E F χ : ℤ) (hEuler : χ = V - E + F) (hV : 1 ≤ V) (hF : 1 ≤ F) :
    2 - χ ≤ E := by
  omega

/-- **At the canonical closure's `χ = −9A + 1`, every decomposition has `≥ 9A + 1` edges.** The
1-skeleton of any cell decomposition grows at least linearly in `A`. (Whether the connection's
singular locus contains it is hypothesis (H1) of the header, not a consequence.) -/
theorem edges_ge_of_chi_canonical (A V E F : ℤ) (hEuler : -9 * A + 1 = V - E + F)
    (hV : 1 ≤ V) (hF : 1 ≤ F) : 9 * A + 1 ≤ E := by
  omega

/-- Euler's formula in the form `χ = 2 − 2g − μ` for a compact orientable surface of genus `g` with
`μ` boundary components, together with the corpus's `2g = 8A`, `μ = A + 1`, reproduces
`χ = −9A + 1` — the three measured invariants are mutually consistent. -/
theorem chi_of_genus_boundary (A g μ : ℤ) (hg : 2 * g = 8 * A) (hμ : μ = A + 1) :
    2 - 2 * g - μ = -9 * A + 1 := by
  omega

/-! ## A bounded-below boundary over a bounded-above bulk is not a surface term -/

/-- **The general criterion.** If the singular count is eventually at least an affine function with
positive slope, and the cell count is eventually positive and at most an affine function, then the
ratio does not tend to `0`, so the pair is not a `StokesSurfaceTerm`. -/
theorem not_stokesSurfaceTerm_of_bounds (cells sing : ℝ → ℝ) (αc βc αs βs : ℝ)
    (hαc : 0 < αc) (hαs : 0 < αs)
    (hsing : ∀ᶠ A in atTop, αs * A + βs ≤ sing A)
    (hcells : ∀ᶠ A in atTop, 0 < cells A ∧ cells A ≤ αc * A + βc) :
    ¬ StokesSurfaceTerm cells sing := by
  rintro ⟨-, h0⟩
  -- the comparison ratio tends to αs/αc > 0
  have hnum : Tendsto (fun A : ℝ => αs + βs / A) atTop (nhds (αs + 0)) :=
    tendsto_const_nhds.add (by simpa [div_eq_mul_inv] using tendsto_inv_atTop_zero.const_mul βs)
  have hden : Tendsto (fun A : ℝ => αc + βc / A) atTop (nhds (αc + 0)) :=
    tendsto_const_nhds.add (by simpa [div_eq_mul_inv] using tendsto_inv_atTop_zero.const_mul βc)
  have hlim : Tendsto (fun A : ℝ => (αs + βs / A) / (αc + βc / A)) atTop
      (nhds ((αs + 0) / (αc + 0))) := hnum.div hden (by simpa using hαc.ne')
  have hpos : (0 : ℝ) < (αs + 0) / (αc + 0) := by simp; positivity
  -- eventually the comparison ratio exceeds half its limit ...
  have hhalf : (0 : ℝ) < (αs + 0) / (αc + 0) / 2 := by positivity
  have hlt : (αs + 0) / (αc + 0) / 2 < (αs + 0) / (αc + 0) := by linarith
  have h1 := Filter.Tendsto.eventually_const_lt hlt hlim
  -- ... and the true ratio is eventually below that half (since it tends to 0)
  have h2 : ∀ᶠ A in atTop, sing A / cells A < (αs + 0) / (αc + 0) / 2 :=
    Filter.Tendsto.eventually_lt_const hhalf h0
  -- ... but the true ratio dominates the comparison ratio for large A
  have h3 : ∀ᶠ A in atTop, (αs + βs / A) / (αc + βc / A) ≤ sing A / cells A := by
    -- `αs·A + βs ≥ 0` holds only EVENTUALLY (for A ≥ −βs/αs); the first draft asked nlinarith to
    -- prove it for every A > 0, which is false. It gets its own eventual bound here.
    filter_upwards [hsing, hcells, eventually_gt_atTop (0 : ℝ), eventually_ge_atTop (-βs / αs)]
      with A hs ⟨hc0, hc1⟩ hA hA2
    have e1 : (αs + βs / A) / (αc + βc / A) = (αs * A + βs) / (αc * A + βc) := by
      field_simp
    rw [e1]
    have hden0 : 0 < αc * A + βc := lt_of_lt_of_le hc0 hc1
    rw [div_le_div_iff₀ hden0 hc0]
    have hs0 : 0 ≤ αs * A + βs := by
      have := (div_le_iff₀ hαs).mp hA2
      linarith
    nlinarith [mul_le_mul_of_nonneg_left hc1 hs0, mul_le_mul_of_nonneg_right hs hc0.le]
  obtain ⟨A, hA1, hA2, hA3⟩ := (h1.and (h2.and h3)).exists
  linarith

/-! ## The canonical closure -/

/-- The Seifert surface's cell count for the canonical closure: `3A` disks and `12A − 1` bands. -/
noncomputable def seifertCells (A : ℝ) : ℝ := 15 * A - 1

/-- **Under (H1), the Stokes singular count of the canonical closure is not a surface term.** The
hypothesis `hsing` IS (H1): a singular count that respects Euler's bound `≥ 9A + 1` eventually.
Over the Seifert cell count `15A − 1` its ratio is bounded below by something tending to `3/5`,
so it fails `StokesSurfaceTerm`. Like the hyperbolic ball, the Stokes route then renormalises the
volume coefficient and supplies no `A^(−1/3)`. Nothing here discharges `hsing`; see the header. -/
theorem stokes_canonical_not_surfaceTerm (sing : ℝ → ℝ)
    (hsing : ∀ᶠ A in atTop, 9 * A + 1 ≤ sing A) :
    ¬ StokesSurfaceTerm seifertCells sing := by
  apply not_stokesSurfaceTerm_of_bounds seifertCells sing 15 (-1) 9 1 (by norm_num) (by norm_num) hsing
  filter_upwards [eventually_gt_atTop (1 : ℝ)] with A hA
  unfold seifertCells
  constructor <;> linarith

end QOU.Mass.StokesSingularCountAffine
