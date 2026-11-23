import QOU.Basic
import QOU.Glossary
import QOU.KnotTheory
import QOU.QuantumObservableUniverse
import QOU.PathIntegrals
import QOU.MassDerivation
import Mathlib.Data.Real.Basic
import Mathlib.Topology.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Tactic.Linarith

/-!
# QOU.MobiusEnergy — Categorical Möbius Energy and Self-Avoidance

Formalization of the categorical Möbius energy functional and the
non-self-intersection corollary from Chapter 4, §9 of the QOU manuscript.

## Structure

1. **Categorical Möbius energy** — the functional `E_cat(γ)` built from the
   Frobenius–Hopf comultiplication and q-Hodge star.
2. **Classical limit** — in the limit `q → 1`, `E_cat` recovers the classical
   Möbius energy up to topological normalisation.
3. **Non-self-intersection** — the non-cocommutativity of the Hopf structure
   at `q ≠ 1` provides an energy barrier preventing self-intersection.

## References

- [freedman1994] M. Freedman, Z.-X. He, Z. Wang, "Möbius energy of knots
  and unknots", Annals of Mathematics 139 (1994), 1–50.
- [ohara1991] J. O'Hara, "Energy of a knot", Topology 30 (1991), 241–247.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-! ## §1  Knot Embedding and Classical Möbius Energy -/

/-- A **knot embedding** `γ : S¹ → M` in the fibre of the realisation functor,
    equipped with smooth parametrisation data.

    In the categorical setting, `γ` takes values in `ω(A)` where `ω` is the
    fibre functor and `A` is the Frobenius–Hopf object. -/
structure KnotEmbedding (M : Type*) where
  /-- The parametrised curve `γ : [0, 1] → M` (periodic). -/
  curve : ℝ → M
  /-- Arc-length distance along the curve. -/
  arcLengthDist : ℝ → ℝ → ℝ
  /-- Arc-length distance is symmetric. -/
  arcLength_symm : ∀ s t, arcLengthDist s t = arcLengthDist t s
  /-- Arc-length distance is non-negative. -/
  arcLength_nonneg : ∀ s t, 0 ≤ arcLengthDist s t
  /-- **Ambient (chord) distance** `|γ(s) − γ(t)|` between the strand points at
      parameters `s` and `t`.

      Carried as a field rather than obtained from a `MetricSpace M` instance,
      matching how `arcLengthDist` is already carried: `M` is the fibre of the
      realisation functor and the rest of this file keeps it a bare `Type*`, so
      requiring a metric instance would constrain every use site for one
      definition.

      Added 2026-08-30 (bean `qou-o6ml`, route 2). Until then this structure
      carried only the *intrinsic* distance, so the Möbius/O'Hara integrand —
      which is a function of the **ambient** separation minus the intrinsic one
      — could not be written in this encoding at all, and the `ClassicalMobiusEnergy`
      docstring stated an integral none of the data here could express. -/
  ambientDist : ℝ → ℝ → ℝ
  /-- Ambient distance is symmetric. -/
  ambient_symm : ∀ s t, ambientDist s t = ambientDist t s
  /-- Ambient distance is non-negative. -/
  ambient_nonneg : ∀ s t, 0 ≤ ambientDist s t
  /-- **The chord never exceeds the arc.**  This is what makes the O'Hara
      integrand pointwise non-negative, and hence what makes
      `ClassicalMobiusEnergy.nonneg` a consequence rather than an assumption. -/
  chord_le_arc : ∀ s t, ambientDist s t ≤ arcLengthDist s t

/-- The **classical Möbius energy** of a knot embedding.

    $$E(\gamma) = \iint_{S^1 \times S^1}
      \left(\frac{1}{|\gamma(s) - \gamma(t)|^2}
        - \frac{1}{D(\gamma(s), \gamma(t))^2}\right)
      |\gamma'(s)|\,|\gamma'(t)|\,ds\,dt.$$

    Ref: [freedman1994], [ohara1991]
    LaTeX: `\label{prop:mobius-energy}` (classical part) -/
structure ClassicalMobiusEnergy where
  /-- The energy value `E(γ)`. -/
  value : ℝ
  /-- The energy is non-negative (Freedman–He–Wang). -/
  nonneg : 0 ≤ value
  /-- Whether the underlying knot is the unknot.  Carried as an opaque
      `Prop` because this structure holds no isotopy-class data; it is the
      minimum needed to *state* Freedman–He–Wang rather than assert its
      conclusion. -/
  isUnknot : Prop
  /-- The energy equals 4 if and only if the knot is the unknot
      (Freedman–He–Wang, 1994).

      **This field read `value = 4 ↔ True` until 2026-08-30.** `P ↔ True`
      is `P`, so that spelling forced `value = 4` for *every* instance —
      machine-checked, `c.unknot_iff.mpr trivial : c.value = 4` — which is
      not a weakened form of Freedman–He–Wang but the negation of its
      content: it made the classical Möbius energy blind to the knot, and
      through `CategoricalMobiusEnergy.classicalLimit` made `E_cat` blind
      too (`E_cat = 1 + const` for every knot).  It carried no `sorry`, no
      `axiom` and no tautological *conclusion*, so no vacuity detector saw
      it, and a prior audit (bean `qou-u87j`) cited its presence as
      evidence the library encoding was *stronger* than its content-block
      sibling. -/
  -- Ref: [freedman1994] https://doi.org/10.2307/2946626
  unknot_iff : value = 4 ↔ isUnknot

/-- The **O'Hara / Möbius integrand** at parameters `(s, t)`:

    $$\frac{1}{|\gamma(s) - \gamma(t)|^2} - \frac{1}{D(\gamma(s), \gamma(t))^2}.$$

    The subtracted term is the *regularisation*: the singularity of the ambient
    term as `t → s` is cancelled by the intrinsic term, which is what makes the
    double integral converge.  It is also, structurally, why this functional is
    a candidate where an unsubtracted kernel is not — see bean `qou-17mq`, whose
    O2 (neutrality) obstruction excludes pair kernels that are not zero-mean; a
    kernel whose subtraction is intrinsic is not vulnerable to that argument.

    Ref: [ohara1991], [freedman1994] -/
noncomputable def KnotEmbedding.oharaIntegrand {M : Type*} (k : KnotEmbedding M)
    (s t : ℝ) : ℝ :=
  1 / k.ambientDist s t ^ 2 - 1 / k.arcLengthDist s t ^ 2

/-- **The O'Hara integrand is pointwise non-negative** off the diagonal.

    Derived from `chord_le_arc`, not assumed.  `ClassicalMobiusEnergy.nonneg`
    below is a *field* — the positivity of the energy is carried as a hypothesis
    there because the structure has no integrand to derive it from.  This lemma
    supplies the pointwise half of that derivation: the remaining step is that
    an integral of a non-negative function is non-negative, which needs
    integration theory this file does not set up.

    The hypothesis is that the two points are distinct in the ambient space,
    which is exactly the off-diagonal condition the double integral imposes. -/
theorem KnotEmbedding.oharaIntegrand_nonneg {M : Type*} (k : KnotEmbedding M)
    (s t : ℝ) (hpos : 0 < k.ambientDist s t) :
    0 ≤ k.oharaIntegrand s t := by
  have harc : 0 < k.arcLengthDist s t := lt_of_lt_of_le hpos (k.chord_le_arc s t)
  have hsq : k.ambientDist s t ^ 2 ≤ k.arcLengthDist s t ^ 2 := by
    nlinarith [k.chord_le_arc s t, hpos.le]
  have h : 1 / k.arcLengthDist s t ^ 2 ≤ 1 / k.ambientDist s t ^ 2 :=
    one_div_le_one_div_of_le (by positivity) hsq
  simpa [KnotEmbedding.oharaIntegrand, sub_nonneg] using h

/-- The integrand is symmetric in its two parameters, inherited from the two
    distance symmetries. -/
theorem KnotEmbedding.oharaIntegrand_symm {M : Type*} (k : KnotEmbedding M)
    (s t : ℝ) : k.oharaIntegrand s t = k.oharaIntegrand t s := by
  simp [KnotEmbedding.oharaIntegrand, k.ambient_symm s t, k.arcLength_symm s t]

/-! ### The MUTUAL term — what a per-pair EM weight actually needs

`oharaIntegrand` above is the **self**-energy form: one curve, and the
subtraction is what tames the diagonal singularity as `t → s`.  Bean `qou-o6ml`
route (2) does not want that.  It wants the **mutual** energy between two
*distinct* components of a link, and that is a different and simpler object. -/

/-- The **mutual (cross) integrand** between points on two distinct components:

    $$\frac{1}{|\gamma_i(s) - \gamma_j(t)|^2}.$$

    **No subtraction.**  The subtracted term in `oharaIntegrand` is `1/D(s,t)²`
    with `D` the arc-length distance *along the curve*; for points on different
    components there is no path along the curve at all, so `D = ∞` and the term
    vanishes identically.  The mutual energy is the unsubtracted integral, and
    the regularisation question does not arise because distinct components are
    disjoint — there is no diagonal to be singular on.

    Modelled here as a bare separation function rather than through
    `KnotEmbedding`, because that structure carries a single `curve : ℝ → M` and
    **cannot express a multi-component link at all**.  That is the real gap on
    route (2), and naming it is the point of this block. -/
noncomputable def mutualIntegrand (sep : ℝ → ℝ → ℝ) (s t : ℝ) : ℝ :=
  1 / sep s t ^ 2

/-- **The mutual integrand is strictly positive** wherever the two components do
    not touch — with no hypothesis beyond that, and in particular with no
    chord-vs-arc inequality.

    Contrast `oharaIntegrand_nonneg`, which needs `chord_le_arc` and yields only
    `0 ≤`.  The mutual term is unconditionally `0 <`, which is exactly the
    property bean `qou-o6ml` route (2) asks of a per-pair weight: *nonzero for
    unlinked pairs*.  On the Borromean carrier every pairwise `lk_ij = 0`
    (axiom (A3) of `mirror_split_s3_em_functional_probe.py`), so a weight built
    from linking numbers vanishes there while this one does not. -/
theorem mutualIntegrand_pos (sep : ℝ → ℝ → ℝ) (s t : ℝ) (h : 0 < sep s t) :
    0 < mutualIntegrand sep s t := by
  unfold mutualIntegrand
  positivity

/-- The mutual integrand is the `D → ∞` limit of the O'Hara integrand, stated as
    the algebraic identity that makes the two comparable: dropping the
    subtracted term is exactly setting `1/D² = 0`. -/
theorem mutualIntegrand_eq_ohara_without_subtraction
    (sep arc : ℝ → ℝ → ℝ) (s t : ℝ) (hD : 1 / arc s t ^ 2 = 0) :
    mutualIntegrand sep s t = 1 / sep s t ^ 2 - 1 / arc s t ^ 2 := by
  rw [hD, sub_zero]; rfl

/-! ### A multi-component carrier

`mutualIntegrand` above is stated over a bare separation function because
`KnotEmbedding` carries a single `curve : ℝ → M` and cannot express a link.
This is that structure.  With it the mutual term is stated *through* the
encoding, and — the point of the exercise — its positivity needs **no side
hypothesis at all**, because disjointness is part of what it means to be a
link. -/

/-- An **`n`-component link embedding**: `n` parametrised components in `M`,
    together with the ambient separation between a point on any component and a
    point on any other.

    The separation is carried at link level rather than assembled from the
    components, because `KnotEmbedding.ambientDist` relates two points on *the
    same* curve and there is nothing in that structure relating two curves. -/
structure LinkEmbedding (M : Type*) (n : ℕ) where
  /-- The components. -/
  component : Fin n → KnotEmbedding M
  /-- Ambient distance from `component i` at parameter `s` to `component j` at
      parameter `t`. -/
  sep : Fin n → ℝ → Fin n → ℝ → ℝ
  /-- Separation is symmetric under exchanging the two (component, parameter)
      pairs. -/
  sep_symm : ∀ i s j t, sep i s j t = sep j t i s
  /-- Separation is non-negative. -/
  sep_nonneg : ∀ i s j t, 0 ≤ sep i s j t
  /-- **Distinct components never meet.**  This is what makes the configuration
      a *link* rather than a singular map, and it is exactly the hypothesis that
      makes the mutual integrand unconditionally positive below. -/
  disjoint : ∀ i j, i ≠ j → ∀ s t, 0 < sep i s j t
  /-- Restricted to one component, the link-level separation is that
      component's own ambient distance — so the two notions agree where they
      overlap rather than sitting side by side. -/
  sep_self : ∀ i s t, sep i s i t = (component i).ambientDist s t

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- The **mutual integrand** between component `i` at `s` and component `j` at
    `t`, stated through the link structure. -/
noncomputable def mutualIntegrand (L : LinkEmbedding M n) (i j : Fin n)
    (s t : ℝ) : ℝ :=
  1 / L.sep i s j t ^ 2

/-- **Unconditional positivity on distinct components.**

    The bare-function `mutualIntegrand_pos` above needs `0 < sep s t` supplied
    as a hypothesis.  Here it is discharged from `disjoint`: nothing is assumed
    beyond `i ≠ j`.  That is the whole reason to have this structure — a
    per-pair EM weight built this way is positive *because the carrier is a
    link*, not because positivity was assumed of it. -/
theorem mutualIntegrand_pos_of_ne (L : LinkEmbedding M n) {i j : Fin n}
    (hij : i ≠ j) (s t : ℝ) : 0 < L.mutualIntegrand i j s t := by
  unfold mutualIntegrand
  have := L.disjoint i j hij s t
  positivity

/-- The mutual integrand is symmetric under exchanging the two components
    together with their parameters. -/
theorem mutualIntegrand_symm (L : LinkEmbedding M n) (i j : Fin n) (s t : ℝ) :
    L.mutualIntegrand i j s t = L.mutualIntegrand j i t s := by
  unfold mutualIntegrand
  rw [L.sep_symm]

/-- The **self** integrand of one component is the O'Hara one, subtraction and
    all.  Recorded so the two halves of a link's energy — `Σᵢ self` and
    `Σ_{i<j} mutual` — are both expressible here.

    Only the summation and integration are missing, and they need measure
    theory this file does not set up. -/
noncomputable def selfIntegrand (L : LinkEmbedding M n) (i : Fin n)
    (s t : ℝ) : ℝ :=
  (L.component i).oharaIntegrand s t

/-- On one component the link-level and component-level ambient distances
    agree, so the mutual integrand restricted to `i = i` is the *unsubtracted*
    part of that component's own O'Hara integrand.

    This is the statement that the two integrands are the same object seen at
    different index pairs — the diagonal carries a subtraction, the off-diagonal
    does not. -/
theorem mutualIntegrand_self (L : LinkEmbedding M n) (i : Fin n) (s t : ℝ) :
    L.mutualIntegrand i i s t = 1 / (L.component i).ambientDist s t ^ 2 := by
  unfold mutualIntegrand
  rw [L.sep_self]

/-- **The scaling ingredient.**  Rescaling every separation by `c > 0` scales
    the mutual integrand by `c⁻²`.

    This is *not* scale-invariance of the energy — that also needs the `ds dt`
    measure to scale by `c²`, which requires the integral this file does not
    build.  It is the pointwise half, recorded so the mechanism is visible and
    the missing half is named rather than assumed. -/
theorem mutualIntegrand_smul (L L' : LinkEmbedding M n) (c : ℝ) (hc : 0 < c)
    (i j : Fin n) (s t : ℝ)
    (hscale : L'.sep i s j t = c * L.sep i s j t) :
    L'.mutualIntegrand i j s t = c⁻¹ ^ 2 * L.mutualIntegrand i j s t := by
  unfold mutualIntegrand
  rw [hscale, mul_pow]
  field_simp

/-- **`LinkEmbedding` is inhabitable**, exhibited rather than asserted.

    This file's own history is the reason to check: `NonSelfIntersection`
    carried a field asserting `∀ E₀, energy > E₀` and was therefore
    **uninhabitable for every `M`**, which made every result conditional on it
    vacuous — sorry-free, and seen by no detector. A new structure with five
    interacting fields earns the same scrutiny.

    Witness: components with all distances `0`, and a separation that is the
    component's own `ambientDist` on the diagonal and `1` off it.  Degenerate on
    purpose — the point is that the field set is *consistent*, not that this is
    a link anyone wants. -/
theorem nonempty_linkEmbedding (M : Type*) (m : M) (n : ℕ) :
    Nonempty (LinkEmbedding M n) := by
  classical
  let K : KnotEmbedding M :=
    { curve := fun _ => m
      arcLengthDist := fun _ _ => 0
      arcLength_symm := fun _ _ => rfl
      arcLength_nonneg := fun _ _ => le_refl 0
      ambientDist := fun _ _ => 0
      ambient_symm := fun _ _ => rfl
      ambient_nonneg := fun _ _ => le_refl 0
      chord_le_arc := fun _ _ => le_refl 0 }
  exact ⟨{ component := fun _ => K
           sep := fun i s j t => if i = j then (K.ambientDist s t) else 1
           sep_symm := by
             intro i s j t
             by_cases h : i = j
             · subst h; simpa using K.ambient_symm s t
             · simp [h, Ne.symm h]
           sep_nonneg := by
             intro i s j t
             by_cases h : i = j
             · subst h; simpa using K.ambient_nonneg s t
             · simp [h]
           disjoint := by
             intro i j hij s t
             simp [hij]
           sep_self := by intro i s t; simp }⟩

end LinkEmbedding

/-! ## §2  Categorical Möbius Energy -/

/-- **Categorical Möbius energy data** for a knot `γ` in a quantum observable
    universe `(C, A, ω)`.

    The energy functional is
    $$E_{\mathrm{cat}}(\gamma) = \lambda \circ \mathrm{tr}_A
      \iint_{S^1 \times S^1 \setminus \mathrm{diag}}
      (\Delta(\gamma(s)) \otimes \Delta(\gamma(t)))
      \star_q \|d\gamma/ds \wedge_q d\gamma/dt\|\,ds\,dt$$

    where `Δ` is the Hopf comultiplication, `λ` is the Frobenius form,
    and `⋆_q` is the q-Hodge star.

    LaTeX: `\label{prop:mobius-energy}` -/
structure CategoricalMobiusEnergy (M : Type*) where
  /-- The substrate parameter governing the q-deformation. -/
  sp : ArchimedeanSubstrateField M
  /-- A chosen base point for evaluating the substrate field. -/
  basepoint : M
  /-- The q-parameter value at the base point. -/
  q : ℝ := sp.field basepoint
  /-- `q > 1` (non-classical regime). -/
  q_gt_one : q > 1
  /-- The knot embedding in the fibre space. -/
  knot : KnotEmbedding M
  /-- The categorical energy value `E_cat(γ)`. -/
  energy : ℝ
  /-- The classical Möbius energy of the same knot. -/
  classicalEnergy : ClassicalMobiusEnergy
  /-- The categorical energy of the knot after applying the Möbius
      transform with parameter `g ∈ PSL(2, ℂ)` (parametrised here by a
      real coordinate on the group, acting on the `ℂP¹` fibre via the
      gauge group fixed by the categorical volume constraint). -/
  energyUnderMobius : ℝ → ℝ
  /-- **Möbius invariance**: `E_cat(γ)` is invariant under the full Möbius
      group `PSL(2, ℂ)`. Encoded as: the transformed energy equals the
      base energy for every group element `g` — the energy functional is
      constant along every Möbius orbit (categorical: invariance under
      `Aut⊗(ω)`). -/
  mobiusInvariant : ∀ g : ℝ, energyUnderMobius g = energy
  /-- **Classical limit**: as `q → 1`, the categorical energy recovers the
      classical Möbius energy up to topological normalisation.
      Encoded as: `E_cat = (1/4) · E_classical + const`. -/
  classicalLimitConst : ℝ
  classicalLimit : energy = (1 / 4) * classicalEnergy.value + classicalLimitConst

/-- The quantum Planck constant at a given substrate parameter value. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- The quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def quantumTwo (q : ℝ) : ℝ := q + q⁻¹

/-! ## §3  Möbius Energy Recovery (Proposition) -/

/-- **Proposition: Categorical recovery of Möbius energy.**

    In the classical limit `q → 1`, the categorical Möbius energy recovers
    the classical Möbius energy up to a topological normalisation:
    $$\lim_{q \to 1} E_{\mathrm{cat}}(\gamma) = \frac{1}{4} E(\gamma) + \mathrm{const}.$$

    The proof proceeds in three steps:
    1. **Gauge fixing** — the categorical volume constraint fixes `G = SU(2)`,
       ensuring `E_cat` is Möbius-invariant.
    2. **Frobenius–Hopf kernel expansion** — at `q = 1`, the comultiplication
       becomes cocommutative and the Frobenius pairing reduces to the Killing
       form, yielding the `1/r²` repulsive kernel.
    3. **Self-energy subtraction** — the diagonal regularisation matches the
       arc-length subtraction via the antipode `S`.

    Stated along the whole Möbius orbit rather than at the base energy
    alone. In that form it is **derived** from two fields — invariance
    carries the transformed energy back to `E_cat`, and the classical
    limit then applies — rather than returned verbatim.

    The base case is `cme.classicalLimit` itself, which is what this
    declaration used to restate: `theorem MobiusEnergy … :=
    cme.classicalLimit`, the structure field under a second name. Use
    the field directly when the orbit plays no part.

    LaTeX: `\label{prop:mobius-energy}` -/
theorem MobiusEnergy {M : Type*} (cme : CategoricalMobiusEnergy M) (g : ℝ) :
    cme.energyUnderMobius g
      = (1 / 4) * cme.classicalEnergy.value + cme.classicalLimitConst := by
  rw [cme.mobiusInvariant g]
  exact cme.classicalLimit

/-- The categorical Möbius energy is non-negative (inheriting from the
    classical bound and the normalisation). -/
theorem MobiusEnergy_nonneg {M : Type*} (cme : CategoricalMobiusEnergy M)
    (h_const_nonneg : 0 ≤ cme.classicalLimitConst) :
    0 ≤ cme.energy := by
  rw [cme.classicalLimit]
  have := cme.classicalEnergy.nonneg
  linarith

/-! ## §4  Non-Self-Intersection Corollary -/

/-- **q-Deformed repulsion kernel**.

    At `q ≠ 1`, the classical `1/r²` kernel is replaced by
    $$\frac{[2]_q}{r^2 - \hbarQ^2}$$
    which has a hard singularity at `r = ℏ_q`, creating an energy barrier. -/
noncomputable def qRepulsionKernel (q r : ℝ) : ℝ :=
  quantumTwo q / (r ^ 2 - hbarQ q ^ 2)

/-- At the pole itself the kernel evaluates to `0` — **Lean's `x / 0 = 0`
    junk value, not a statement about the singularity.**

    This declaration was named `qRepulsionKernel_singular` and documented as
    "the q-deformed kernel diverges at `r = ℏ_q`" while concluding `= 0`,
    proved by `div_zero`.  The name and the docstring asserted a divergence;
    the statement asserted its opposite, and the proof established only the
    division convention.  Renamed and re-documented 2026-08-30; the genuine
    divergence is `qRepulsionKernel_unbounded_near_pole` below, and it is
    that lemma — not this one — that the non-self-intersection corollary
    needs. -/
theorem qRepulsionKernel_junk_value_at_pole (q r : ℝ)
    (hr : r ^ 2 - hbarQ q ^ 2 = 0) :
    qRepulsionKernel q r = 0 := by
  unfold qRepulsionKernel
  rw [hr, div_zero]

/-- The quantum Planck constant is positive when `q > 1`. -/
theorem hbarQ_pos (q : ℝ) (hq : q > 1) : 0 < hbarQ q := by
  unfold hbarQ
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- The quantum integer `[2]_q` is positive when `q > 0`. -/
theorem quantumTwo_pos (q : ℝ) (hq : q > 0) : 0 < quantumTwo q := by
  unfold quantumTwo
  have : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

/-- **The genuine divergence.**  For `q > 1` the kernel exceeds every bound
    at radii strictly outside the exclusion radius `ℏ_q`, so it is unbounded
    as `r ↘ ℏ_q`.  This is the energy barrier the non-self-intersection
    corollary rests on; `qRepulsionKernel_junk_value_at_pole` above is not. -/
theorem qRepulsionKernel_unbounded_near_pole (q : ℝ) (hq : q > 1) (B : ℝ) :
    ∃ r : ℝ, hbarQ q < r ∧ B < qRepulsionKernel q r := by
  have hh : 0 < hbarQ q := hbarQ_pos q hq
  have hc : 0 < quantumTwo q := quantumTwo_pos q (by linarith)
  set M : ℝ := max B 1 + 1 with hM
  have hM1 : 1 < M := by
    have : (1 : ℝ) ≤ max B 1 := le_max_right _ _
    simp only [hM]; linarith
  have hMpos : 0 < M := by linarith
  have hMB : B < M := by
    have : B ≤ max B 1 := le_max_left _ _
    simp only [hM]; linarith
  set d : ℝ := quantumTwo q / M with hd
  have hdpos : 0 < d := div_pos hc hMpos
  refine ⟨Real.sqrt (hbarQ q ^ 2 + d), ?_, ?_⟩
  · have h1 : hbarQ q ^ 2 < hbarQ q ^ 2 + d := by linarith
    have h2 : Real.sqrt (hbarQ q ^ 2) < Real.sqrt (hbarQ q ^ 2 + d) :=
      Real.sqrt_lt_sqrt (sq_nonneg _) h1
    rwa [Real.sqrt_sq hh.le] at h2
  · have hsq : Real.sqrt (hbarQ q ^ 2 + d) ^ 2 = hbarQ q ^ 2 + d :=
      Real.sq_sqrt (by positivity)
    have hden : Real.sqrt (hbarQ q ^ 2 + d) ^ 2 - hbarQ q ^ 2 = d := by
      rw [hsq]; ring
    have hcancel : quantumTwo q / d = M := by
      rw [hd]; field_simp
    unfold qRepulsionKernel
    rw [hden, hcancel]
    exact hMB

/-- **Corollary: Obstruction to self-intersection.**

    For `q ≠ 1`, the non-cocommutativity of the Hopf structure provides a
    categorical obstruction to knot self-intersection: the energy diverges
    whenever two non-adjacent strands approach within distance `ℏ_q`.

    The mechanism:
    - The universal R-matrix `R ∈ U_q(su(2)) ⊗̂ U_q(su(2))` controls the
      failure of cocommutativity: `σ ∘ Δ ≠ Δ`.
    - The q-deformed commutator `[X̂, P̂]_q = iℏ_q` replaces the `1/r²`
      kernel with `[2]_q / (r² − ℏ_q²)`.
    - This kernel has a hard singularity at `r = ℏ_q`, creating an energy
      barrier of infinite height — the "quantum exclusion zone".

    Physically, the vortex filament `γ` cannot pass through itself because
    doing so would require infinite categorical energy. This is the
    knot-theoretic analogue of the Pauli exclusion principle.

    LaTeX: `\label{cor:non-self-intersection}` -/
structure NonSelfIntersection (M : Type*) where
  /-- The categorical Möbius energy data. -/
  cme : CategoricalMobiusEnergy M
  /-- **Energy barrier.**  If two *non-adjacent* strand points — at least the
      exclusion radius `ℏ_q` apart along the curve — came within `ℏ_q` of each
      other in the ambient space, the categorical energy would exceed every
      bound.  Stated as an implication, so an inhabitant is a configuration
      whose non-adjacent strands all stay *outside* `ℏ_q` — the physical content
      ("the filament cannot pass through itself"), recovered as
      `separation_ge_exclusionRadius` below.

      **The separation is the knot's own chord distance** (bean `qou-dx7g`,
      2026-11-20).  This structure used to carry a free field
      `separation : ℝ → ℝ → ℝ`, so `separation := fun _ _ => hbarQ q` made the
      antecedent false and the "exclusion" returned what was chosen.  The
      separation is now `cme.knot.ambientDist`, the chord distance
      `KnotEmbedding` has carried since 2026-08-30.

      **The non-adjacency antecedent is forced, not a weakening.**
      `KnotEmbedding.chord_le_arc` gives `ambientDist ≤ arcLengthDist`, so every
      pair less than `ℏ_q` apart along the curve is also less than `ℏ_q` apart in
      space.  Without the antecedent such neighbouring pairs would trigger the
      barrier and the structure would be uninhabitable for any embedding with
      short arcs, which is the docstring's "non-adjacent strands" made explicit.

      **This field asserted the consequent unconditionally until
      2026-08-30**, as `∀ E₀ : ℝ, ∃ ε : ℝ, ε > 0 ∧ (∀ _s _t : ℝ, cme.energy
      > E₀)`.  The two `_s _t` binders were unused, so the inner `∀` was a
      constant and the field reduced to `∀ E₀ : ℝ, cme.energy > E₀` — the
      energy exceeds every real.  Instantiating at `E₀ := cme.energy` gives
      `cme.energy > cme.energy`, so `NonSelfIntersection M` was
      **uninhabitable for every `M`** (machine-checked: `IsEmpty
      (NonSelfIntersection M)`), and every result conditional on it was
      vacuous.  The docstring's own quantifier order (`∀ ε, ∃ E₀`) was the
      reverse of the code's, and the proximity antecedent it describes was
      never written as a hypothesis at all. -/
  energyBarrier : ∀ s t : ℝ, hbarQ cme.q ≤ cme.knot.arcLengthDist s t →
    cme.knot.ambientDist s t < hbarQ cme.q → ∀ E₀ : ℝ, cme.energy > E₀

/-- The ambient separation between the strand points at parameters `s` and `t`:
    the knot's chord distance `|γ(s) − γ(t)|`.  A definition, not a field. -/
def NonSelfIntersection.separation {M : Type*} (nsi : NonSelfIntersection M) :
    ℝ → ℝ → ℝ :=
  nsi.cme.knot.ambientDist

/-- The exclusion radius: `ℏ_q = 1 − q⁻¹`, derived from the categorical
    Möbius energy data. Not a free parameter — it is always `hbarQ cme.q`. -/
noncomputable def NonSelfIntersection.exclusionRadius {M : Type*}
    (nsi : NonSelfIntersection M) : ℝ := hbarQ nsi.cme.q

/-- The exclusion radius is exactly `ℏ_q`. -/
theorem exclusionRadius_eq {M : Type*}
    (nsi : NonSelfIntersection M) :
    nsi.exclusionRadius = hbarQ nsi.cme.q := rfl

/-- The exclusion radius is positive — **derived** from `cme.q_gt_one`
    through `hbarQ_pos`, not carried.  It was a structure field
    (`exclusionRadius_pos`) until 2026-08-30; a hypothesis that follows from
    another field is an assumption wearing a theorem's name.  Matches the
    repair already made to the content-block sibling
    `climax-volume-mass/non-self-intersection-proof.lean`. -/
theorem exclusionRadius_pos {M : Type*} (nsi : NonSelfIntersection M) :
    0 < nsi.exclusionRadius :=
  hbarQ_pos nsi.cme.q nsi.cme.q_gt_one

/-- **The exclusion, derived rather than assumed.**  No two strand points of
    an inhabitant that are non-adjacent (at least `ℏ_q` apart along the curve)
    come within the exclusion radius in space: if one pair did, the barrier
    field would make the energy exceed itself. -/
theorem separation_ge_exclusionRadius {M : Type*}
    (nsi : NonSelfIntersection M) (s t : ℝ)
    (hnadj : hbarQ nsi.cme.q ≤ nsi.cme.knot.arcLengthDist s t) :
    hbarQ nsi.cme.q ≤ nsi.separation s t := by
  by_contra h
  push_neg at h
  exact absurd (nsi.energyBarrier s t hnadj h nsi.cme.energy) (lt_irrefl _)

/-- The exclusion radius vanishes in the classical limit `q → 1`. -/
theorem hbarQ_classical_limit : hbarQ 1 = 0 := by
  unfold hbarQ
  simp [inv_one]

/-- At `q > 1`, the exclusion zone has positive radius, providing
    a genuine obstruction to self-intersection. -/
theorem exclusionZone_positive (q : ℝ) (hq : q > 1) :
    0 < hbarQ q :=
  hbarQ_pos q hq

/-! ## §5  The classical-limit field constrains nothing — measured 2026-09-14

`CategoricalMobiusEnergy.classicalLimit` reads
`energy = (1/4) * classicalEnergy.value + classicalLimitConst`, which looks like
the bridge from the categorical energy to the classical one. **It is not a
constraint on that pair at all**, because `classicalLimitConst` is a *free field
of the same structure*, appearing once and linearly. Given any `energy` and any
`classicalEnergy` whatever, exactly one constant satisfies the equation — so the
field defines `classicalLimitConst` rather than relating the two energies.

The mathematical statement the docstring quotes,
`lim_{q→1} E_cat(γ) = ¼ E(γ) + const`, means a **universal** constant: the same
for every knot. Encoded **per instance**, that content is gone.

This is the same class as the incident the `ClassicalMobiusEnergy.unknot_iff`
docstring records — *"no `sorry`, no `axiom` and no tautological conclusion, so
no vacuity detector saw it"* — one field over, and it survived that repair. It
is recorded, not repaired: making the constant universal changes what the
structure asserts, which is an authoring decision for the owner, not a fix an
agent should make unasked. Bean `qou-pzsi`. -/

/-- **`classicalLimitConst` is determined by the other two fields.** -/
theorem classicalLimitConst_eq {M : Type*} (cme : CategoricalMobiusEnergy M) :
    cme.classicalLimitConst = cme.energy - (1 / 4) * cme.classicalEnergy.value := by
  have h := cme.classicalLimit
  linarith

/-- **So the classical-limit field relates the two energies not at all.** For
*any* real `e` and *any* classical energy `c`, exactly one constant makes the
equation hold. A field that can always be satisfied, whatever the quantities it
mentions, asserts nothing about them. -/
theorem classicalLimit_unconstraining (e : ℝ) (c : ClassicalMobiusEnergy) :
    ∃! k : ℝ, e = (1 / 4) * c.value + k := by
  refine ⟨e - (1 / 4) * c.value, by ring, ?_⟩
  intro k hk
  linarith

/-! ### Is a UNIVERSAL constant available?  No — measured, not assumed.

`classicalLimit_unconstraining` above shows the field constrains nothing *per
instance*.  The natural repair is to ask for **one** `k` shared by every
instance — that would be a real, falsifiable claim about the normalisation
rather than a per-instance bookkeeping slot.

**It is not available as the structure is written**, and this is a theorem
rather than a doubt.  `shiftEnergy` takes any instance to another with the
**same** `classicalEnergy` and the constant moved by an arbitrary `d`: shift
`energy` and `energyUnderMobius` together, and both `mobiusInvariant` and
`classicalLimit` survive by `ring`.  Nothing else in the structure — `sp`,
`basepoint`, `q`, `q_gt_one`, `knot` — relates `energy` to `classicalEnergy`,
so nothing obstructs the shift.

Consequence: given even ONE instance, `classicalLimitConst` is **surjective
onto ℝ** at fixed classical energy, so `∃ k, ∀ c, c.classicalLimitConst = k`
is false.  Making the constant universal is therefore **not a quantifier
change** — it requires *adding a constraint to the structure* that ties
`energy` to `classicalEnergy`, which is new mathematics and is exactly what
the framework does not currently have. -/

/-- From any instance, another with the SAME classical energy and the
constant shifted by an arbitrary `d`. -/
def shiftEnergy {M : Type*} (cme : CategoricalMobiusEnergy M) (d : ℝ) :
    CategoricalMobiusEnergy M :=
  { cme with
    energy := cme.energy + d
    energyUnderMobius := fun g => cme.energyUnderMobius g + d
    mobiusInvariant := by intro g; rw [cme.mobiusInvariant g]
    classicalLimitConst := cme.classicalLimitConst + d
    classicalLimit := by rw [cme.classicalLimit]; ring }

theorem shiftEnergy_classicalEnergy {M : Type*} (cme : CategoricalMobiusEnergy M)
    (d : ℝ) : (shiftEnergy cme d).classicalEnergy = cme.classicalEnergy := rfl

theorem shiftEnergy_const {M : Type*} (cme : CategoricalMobiusEnergy M) (d : ℝ) :
    (shiftEnergy cme d).classicalLimitConst = cme.classicalLimitConst + d := rfl

/-- **The constant is surjective onto ℝ** as soon as one instance exists —
at fixed classical energy. -/
theorem classicalLimitConst_surjective {M : Type*} (cme : CategoricalMobiusEnergy M)
    (k : ℝ) : ∃ c : CategoricalMobiusEnergy M,
      c.classicalEnergy = cme.classicalEnergy ∧ c.classicalLimitConst = k :=
  ⟨shiftEnergy cme (k - cme.classicalLimitConst), rfl, by
    rw [shiftEnergy_const]; ring⟩

/-- **No universal constant exists** for the structure as encoded. -/
theorem no_universal_classicalLimitConst {M : Type*}
    (cme : CategoricalMobiusEnergy M) :
    ¬ ∃ k : ℝ, ∀ c : CategoricalMobiusEnergy M, c.classicalLimitConst = k := by
  rintro ⟨k, hk⟩
  have h0 := hk cme
  have h1 := hk (shiftEnergy cme 1)
  rw [shiftEnergy_const] at h1
  linarith


end QOU
