import Mathlib.Analysis.Analytic.Composition
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.Analysis.Complex.Basic
import Mathlib.GroupTheory.GroupAction.Quotient
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.GroupTheory.SpecificGroups.Cyclic
import Mathlib.LinearAlgebra.Determinant
import Mathlib.LinearAlgebra.Matrix.Charpoly.Minpoly
import Mathlib.RingTheory.Polynomial.Cyclotomic.Eval
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.RingTheory.RootsOfUnity.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Ring

/-!
# Braid-to-Homology Symplectic Representations, Cyclic Germ Stabilizers, Cellular Riemann–Hurwitz, and Bring-to-Genus-3 Degeneration Obstructions

This module formalizes four interconnected mathematical components for Bring's genus-4
curve $\Sigma_4 = \{p_1 = p_2 = p_3 = 0\} \subset \mathbb{P}^4$ (`qou-m1bg`, `qou-m3tr`,
`qou-pzsi`, `qou-8pl1`):

1. **Cyclic Point Stabilizers and $G$-Equivariant Cellular Riemann–Hurwitz (`qou-m1bg`, `qou-m3tr`):**
   - Any finite group $G$ admitting an injective group homomorphism $d_p : G \to^* K^\times$
     into the multiplicative units of a field $K$ satisfies `IsCyclic G` and admits a
     generator of order $|G|$.
   - Cartan's finite-order analytic germ rigidity over any characteristic-zero nontrivially
     normed field $\mathbb{K}$ (including $\mathbb{C}$): if an analytic map $f$ fixes $p$
     with $f'(p) = 1$ and $f^{[n]}$ agrees with $\mathrm{id}$ near $p$ ($n \ge 1$), the
     averaging map $\Phi(z) = \sum_{k=0}^{n-1} f^{[k]}(z)$ satisfies $\Phi'(p) = n \neq 0$
     and $\Phi \circ f = \Phi$ near $p$, forcing $f = \mathrm{id}$ near $p$ and on any
     preconnected open neighborhood $U \ni p$. Consequently, any finite group acting
     faithfully by analytic maps on $U$ while fixing $p$ has an injective derivative
     homomorphism $G \to^* \mathbb{K}^\times$ and is cyclic.
   - Every cyclic subgroup of $S_5 = \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,5)$ has order in
     $\{1, 2, 3, 4, 5, 6\}$, and every even cyclic subgroup ($A_5$) has order in $\{1, 2, 3, 5\}$.
   - For any finite $G$-equivariant 2-dimensional cell complex $(V, E, F)$ where $G$ acts
     freely on edges $E$ and faces $F$, orbit-stabilizer counting relates the upstairs
     Euler characteristic $|V| - |E| + |F|$ to the quotient Euler characteristic
     $|V/G| - |E/G| + |F/G|$ by both the orbit-deficit identity and the pointwise
     ramification-index identity.

2. **Integral Seifert Intersection Matrices and Braid Symplectic Representations (`qou-pzsi`):**
   - Explicit $8 \times 8$ integral Stallings Seifert matrices $S_{3,5}$ (for $(\sigma_1 \sigma_2)^5$,
     torus knot $T_{3,5}$) and $S_{2,9}$ (for $\sigma_1^9$, torus knot $T_{2,9}$), both of
     determinant $1$ (fibered knots) with unimodular skew-symmetric intersection forms
     $J = S - S^T$ ($\det J = 1$) explicitly congruent over $\mathbb{Z}$ to the standard
     genus-4 symplectic form $\Omega_8$ on $H_1(\Sigma_4; \mathbb{Z}) \cong \mathbb{Z}^8$.
   - The monodromy matrix $M_{3,5} = S_{3,5}^{-1} S_{3,5}^T$ preserves $J_{3,5}$ (conjugating
     into $\mathrm{Sp}(8, \mathbb{Z})$), has finite order $15$, and has characteristic
     polynomial equal to the 15th cyclotomic polynomial $\Phi_{15}(X)$ of degree
     $\varphi(15) = 8$, matching the level-15 isogeny class of $\mathrm{Jac}(\Sigma_4)$.
   - Eight Picard–Lefschetz symplectic transvections in $\mathrm{Sp}(8, \mathbb{Z})$ satisfy
     the Artin braid relations and far commutativity, furnishing a functorial braid-word
     evaluation into $\mathrm{Sp}(8, \mathbb{Z})$.
   - By irreducibility of $\Phi_{22}(X)$ over $\mathbb{Q}$ of degree $\varphi(22) = 10 > 8$,
     no matrix in $M_8(\mathbb{Z})$ (and hence no element of $\mathrm{Sp}(8, \mathbb{Z})$)
     annihilates $\Phi_{22}(X)$, ruling out $T_{2,11}$.

3. **Algebraic and Group-Theoretic Obstructions on Bring $\rightsquigarrow$ Genus-3 Degenerations (`qou-8pl1`):**
   - On $\{p_1(x) = 0\}$, Newton's identity yields $p_3(x) = 3 e_3(x)$ identically, so
     $p_3(x) - \tau e_3(x) = (3 - \tau) e_3(x)$ defines a constant curve for $\tau \neq 3$.
   - Any $S_5$-action with cyclic point stabilizers has minimum orbit size $\ge 20$ ($\ge 24$
     for $(2, 4, 5)$ stabilizers), and cellular Riemann–Hurwitz admits no solution at genus $3$
     for $S_5$ with cyclic stabilizers, so any degeneration to a connected genus-3 normalization
     breaks $S_5$.
   - On the quadric $\{p_1 = 0, p_2 = 0\}$, $S_4$ has no fixed point in characteristic zero.
   - For any group $G$ of order $168$ acting with $(2, 3, 7)$ point stabilizers (the Hurwitz
     action on Klein's quartic) and any subgroup $H \le G$ of order $24$ ($H \cong S_4$),
     every $H$-orbit has cardinality in $\{8, 12, 24\}$ ($\ge 8 > 2$), excluding any
     $H$-invariant 1-point or 2-point node-preimage set.
-/

namespace QOU.Brings.BraidCurveHomologyAndEquivariantHurwitz

-- ============================================================================
-- §1. Cyclic Germ Stabilizers (`qou-m1bg`) & Cellular Riemann–Hurwitz (`qou-m3tr`)
-- ============================================================================

/-- Any finite group $G$ admitting an injective multiplicative homomorphism
    $d_p : G \to^* K^\times$ into the units of a field $K$ is cyclic and possesses a
    generator whose element order equals $|G|$. -/
theorem isCyclic_and_generator_of_injective_units_hom
    {G K : Type*} [Group G] [Fintype G] [Field K]
    (d_p : G →* Kˣ) (hd : Function.Injective d_p) :
    IsCyclic G ∧ ∃ g₀ : G, orderOf g₀ = Fintype.card G := by
  let f : G →* K := (Units.coeHom K).comp d_p
  have hf : Function.Injective f := fun _ _ hab => hd (Units.ext hab)
  have hcyc : IsCyclic G := isCyclic_of_subgroup_isDomain f hf
  obtain ⟨g₀, hg₀⟩ := @IsCyclic.exists_ofOrder_eq_natCard G _ hcyc
  rw [Nat.card_eq_fintype_card] at hg₀
  exact ⟨hcyc, ⟨g₀, hg₀⟩⟩

/-- Strict differentiability with non-zero derivative $c \neq 0$ at $p$ implies local
    injectivity in a neighborhood of $(p, p)$. -/
lemma eventually_inj_of_hasStrictDerivAt {𝕜 : Type*} [NontriviallyNormedField 𝕜]
    {Φ : 𝕜 → 𝕜} {c p : 𝕜} (hΦ : HasStrictDerivAt Φ c p) (hc : c ≠ 0) :
    ∀ᶠ q : 𝕜 × 𝕜 in nhds (p, p), Φ q.1 = Φ q.2 → q.1 = q.2 := by
  have hc_pos : 0 < ‖c‖ := norm_pos_iff.mpr hc
  have hhalf : 0 < ‖c‖ / 2 := half_pos hc_pos
  have hbound := hΦ.isLittleO.bound hhalf
  filter_upwards [hbound] with q hq hEq
  have hsmul :
      (ContinuousLinearMap.smulRight (1 : 𝕜 →L[𝕜] 𝕜) c) (q.1 - q.2) = (q.1 - q.2) * c := by
    simp [ContinuousLinearMap.smulRight_apply]
  rw [hsmul, hEq, sub_self, zero_sub, norm_neg, norm_mul] at hq
  have hle : ‖q.1 - q.2‖ ≤ 0 := by nlinarith
  exact sub_eq_zero.mp (norm_le_zero_iff.mp hle)

/-- Pointwise finite sums of functions analytic at $p$ remain analytic at $p$. -/
lemma analyticAt_sum_finset {𝕜 : Type*} [NontriviallyNormedField 𝕜]
    {ι : Type*} (s : Finset ι) (F : ι → 𝕜 → 𝕜) (p : 𝕜)
    (hF : ∀ i ∈ s, AnalyticAt 𝕜 (F i) p) :
    AnalyticAt 𝕜 (fun z => ∑ i ∈ s, F i z) p := by
  classical
  induction s using Finset.induction_on with
  | empty =>
    simp only [Finset.sum_empty]
    exact analyticAt_const
  | @insert a s ha ih =>
    have ha_an : AnalyticAt 𝕜 (F a) p := hF a (Finset.mem_insert_self a s)
    have hs_an : AnalyticAt 𝕜 (fun z => ∑ i ∈ s, F i z) p :=
      ih (fun i hi => hF i (Finset.mem_insert_of_mem hi))
    have hadd := ha_an.add hs_an
    convert hadd using 1
    ext z
    exact Finset.sum_insert ha

/-- Cartan's finite-order analytic germ rigidity (`qou-m1bg`): over any characteristic-zero
    nontrivially normed field $\mathbb{K}$ (such as $\mathbb{C}$), if $f : \mathbb{K} \to \mathbb{K}$
    is analytic at $p$, fixes $p$ with $f'(p) = 1$, and satisfies $f^{[n]} =_{\mathrm{nhds}\,p} \mathrm{id}$
    for some $n \ge 1$, then $f =_{\mathrm{nhds}\,p} \mathrm{id}$. -/
theorem cartan_analytic_germ_rigidity {𝕜 : Type*} [NontriviallyNormedField 𝕜] [CharZero 𝕜]
    {f : 𝕜 → 𝕜} {p : 𝕜} {n : ℕ} (hn : 0 < n)
    (hf_an : AnalyticAt 𝕜 f p) (hfp : f p = p) (hderiv : deriv f p = 1)
    (hiter : f^[n] =ᶠ[nhds p] id) :
    f =ᶠ[nhds p] id := by
  have hf_deriv : HasDerivAt f 1 p := by
    have hd : HasDerivAt f (deriv f p) p := hf_an.hasStrictFDerivAt.hasStrictDerivAt.hasDerivAt
    rwa [hderiv] at hd
  have h_it : ∀ k : ℕ, (f^[k]) p = p ∧ AnalyticAt 𝕜 (f^[k]) p ∧ HasDerivAt (f^[k]) 1 p := by
    intro k
    induction k with
    | zero =>
      exact ⟨rfl, analyticAt_id, hasDerivAt_id p⟩
    | succ k ih =>
      rcases ih with ⟨hk_p, hk_an, hk_d⟩
      have hsucc_eq : f^[k + 1] = (f^[k]) ∘ f := Function.iterate_succ f k
      rw [hsucc_eq]
      refine ⟨by simp [Function.comp, hfp, hk_p], ?_, ?_⟩
      · exact (hfp.symm ▸ hk_an).comp hf_an
      · have hcomp := HasDerivAt.comp p (hfp.symm ▸ hk_d) hf_deriv
        simpa using hcomp
  let Φ : 𝕜 → 𝕜 := fun z => ∑ k ∈ Finset.range n, (f^[k]) z
  have hΦ_an : AnalyticAt 𝕜 Φ p :=
    analyticAt_sum_finset (Finset.range n) (fun k => f^[k]) p (fun k _ => (h_it k).2.1)
  have hΦ_deriv : HasDerivAt Φ (n : 𝕜) p := by
    have hsum := HasDerivAt.sum (u := Finset.range n) (A := fun k z => (f^[k]) z)
      (fun k _ => (h_it k).2.2)
    have hconst : (∑ _k ∈ Finset.range n, (1 : 𝕜)) = (n : 𝕜) := by
      simp [Finset.sum_const, Finset.card_range]
    rw [hconst] at hsum
    convert hsum using 1
    ext z
    simp [Φ]
  have hΦ_strict : HasStrictDerivAt Φ (n : 𝕜) p := by
    have hs : HasStrictDerivAt Φ (deriv Φ p) p := hΦ_an.hasStrictFDerivAt.hasStrictDerivAt
    rwa [hΦ_deriv.deriv] at hs
  have hn_ne : (n : 𝕜) ≠ 0 := Nat.cast_ne_zero.mpr hn.ne'
  have hinj := eventually_inj_of_hasStrictDerivAt hΦ_strict hn_ne
  have hcont_pair : ContinuousAt (fun z : 𝕜 => (f z, z)) p :=
    hf_deriv.continuousAt.prodMk continuousAt_id
  have hpair_p : (f p, p) = (p, p) := by rw [hfp]
  have hinj_z : ∀ᶠ z : 𝕜 in nhds p, Φ (f z) = Φ z → f z = z := by
    have hmem : {q : 𝕜 × 𝕜 | Φ q.1 = Φ q.2 → q.1 = q.2} ∈ nhds (f p, p) := by
      rw [hpair_p]; exact hinj
    exact hcont_pair.eventually hmem
  filter_upwards [hinj_z, hiter] with z hz_inj hz_it
  apply hz_inj
  have htele : Φ (f z) - Φ z = (f^[n]) z - z := by
    calc Φ (f z) - Φ z
        = ∑ k ∈ Finset.range n, ((f^[k]) (f z) - (f^[k]) z) := by
            simp only [Φ, ← Finset.sum_sub_distrib]
      _ = ∑ k ∈ Finset.range n, ((f^[k + 1]) z - (f^[k]) z) := by
            refine Finset.sum_congr rfl (fun k _ => ?_)
            rw [Function.iterate_succ_apply]
      _ = (f^[n]) z - (f^[0]) z := Finset.sum_range_sub (fun k => (f^[k]) z) n
      _ = (f^[n]) z - z := rfl
  have hzero : Φ (f z) - Φ z = 0 := by
    rw [htele, hz_it, id_eq, sub_self]
  exact sub_eq_zero.mp hzero

/-- Data of a finite group $G$ acting faithfully by analytic maps on a preconnected open
    neighborhood $U \subseteq \mathbb{K}$ while fixing a basepoint $p \in U$ (`qou-m1bg`). -/
structure FaithfulAnalyticPointAction (G 𝕜 : Type*) [Group G] [Fintype G]
    [NontriviallyNormedField 𝕜] [CharZero 𝕜] where
  U : Set 𝕜
  p : 𝕜
  isOpen_U : IsOpen U
  isPreconnected_U : IsPreconnected U
  mem_p : p ∈ U
  act : G → 𝕜 → 𝕜
  analytic_act : ∀ g : G, AnalyticOnNhd 𝕜 (act g) U
  mapsTo_act : ∀ g : G, Set.MapsTo (act g) U U
  fix_p : ∀ g : G, act g p = p
  act_one : ∀ z ∈ U, act 1 z = z
  act_mul : ∀ (g h : G), ∀ z ∈ U, act (g * h) z = act g (act h z)
  faithful_on_U : ∀ g : G, Set.EqOn (act g) id U → g = 1

/-- Explicit complex inhabitant of `FaithfulAnalyticPointAction`: the order-2 group
    $\mathbb{Z}^\times = \{1, -1\}$ acting on $U = \mathbb{C}$ around $p = 0$ by $z \mapsto \pm z$. -/
def complexInvolutionPointAction :
    FaithfulAnalyticPointAction ℤˣ ℂ where
  U := Set.univ
  p := 0
  isOpen_U := isOpen_univ
  isPreconnected_U := isPreconnected_univ
  mem_p := Set.mem_univ 0
  act g z := ((g : ℤ) : ℂ) * z
  analytic_act g := (analyticOnNhd_const (𝕜 := ℂ) (v := ((g : ℤ) : ℂ))).mul analyticOnNhd_id
  mapsTo_act _ _ _ := Set.mem_univ _
  fix_p _ := mul_zero _
  act_one z _ := by simp
  act_mul g h z _ := by push_cast; ring
  faithful_on_U g hg := by
    have h1 : (((g : ℤ) : ℂ) * 1) = (1 : ℂ) := hg (Set.mem_univ (1 : ℂ))
    have h1c : ((g : ℤ) : ℂ) = ((1 : ℤ) : ℂ) := by simpa using h1
    exact Units.ext (Int.cast_injective h1c)

/-- On a `FaithfulAnalyticPointAction`, iterating `act g` $k$ times at any $z \in U$ agrees
    with `act (g ^ k) z`. -/
lemma FaithfulAnalyticPointAction.iterate_eq_pow {G 𝕜 : Type*} [Group G] [Fintype G]
    [NontriviallyNormedField 𝕜] [CharZero 𝕜]
    (A : FaithfulAnalyticPointAction G 𝕜) (g : G) :
    ∀ k : ℕ, ∀ z ∈ A.U, ((A.act g)^[k]) z = A.act (g ^ k) z := by
  intro k
  induction k with
  | zero =>
    intro z hz
    simp [A.act_one z hz]
  | succ k ih =>
    intro z hz
    rw [Function.iterate_succ_apply, ih (A.act g z) (A.mapsTo_act g hz),
        ← A.act_mul (g ^ k) g z hz, pow_succ]

/-- Analytic germ stabilizer cyclicity (`qou-m1bg`): for any `FaithfulAnalyticPointAction G 𝕜`,
    the derivative map $g \mapsto (g \cdot \_)'(p)$ defines an injective group homomorphism
    $G \to^* \mathbb{K}^\times$, so `IsCyclic G` holds and $G$ admits a generator of order $|G|$. -/
theorem FaithfulAnalyticPointAction.isCyclic_and_generator {G 𝕜 : Type*} [Group G] [Fintype G]
    [NontriviallyNormedField 𝕜] [CharZero 𝕜]
    (A : FaithfulAnalyticPointAction G 𝕜) :
    (∃ d_p : G →* 𝕜ˣ,
      (∀ g : G, (d_p g : 𝕜) = deriv (A.act g) A.p) ∧ Function.Injective d_p) ∧
    IsCyclic G ∧
    ∃ g₀ : G, orderOf g₀ = Fintype.card G := by
  have h_hasDeriv : ∀ g : G, HasDerivAt (A.act g) (deriv (A.act g) A.p) A.p := fun g =>
    (A.analytic_act g A.p A.mem_p).hasStrictFDerivAt.hasStrictDerivAt.hasDerivAt
  have h_mul_deriv : ∀ g h : G, deriv (A.act (g * h)) A.p =
      deriv (A.act g) A.p * deriv (A.act h) A.p := by
    intro g h
    have hev : A.act (g * h) =ᶠ[nhds A.p] (A.act g) ∘ (A.act h) := by
      filter_upwards [A.isOpen_U.mem_nhds A.mem_p] with z hz
      exact A.act_mul g h z hz
    have hcomp : HasDerivAt ((A.act g) ∘ (A.act h))
        (deriv (A.act g) A.p * deriv (A.act h) A.p) A.p := by
      have hg_hp : HasDerivAt (A.act g) (deriv (A.act g) A.p) (A.act h A.p) := by
        rw [A.fix_p h]; exact h_hasDeriv g
      exact HasDerivAt.comp A.p hg_hp (h_hasDeriv h)
    exact (hcomp.congr_of_eventuallyEq hev).deriv
  have h_one_deriv : deriv (A.act 1) A.p = 1 := by
    have hev : A.act 1 =ᶠ[nhds A.p] id := by
      filter_upwards [A.isOpen_U.mem_nhds A.mem_p] with z hz
      exact A.act_one z hz
    exact ((hasDerivAt_id A.p).congr_of_eventuallyEq hev).deriv
  let d_p : G →* 𝕜ˣ :=
    { toFun := fun g =>
        { val := deriv (A.act g) A.p
          inv := deriv (A.act g⁻¹) A.p
          val_inv := by rw [← h_mul_deriv, mul_inv_cancel, h_one_deriv]
          inv_val := by rw [← h_mul_deriv, inv_mul_cancel, h_one_deriv] }
      map_one' := Units.ext h_one_deriv
      map_mul' := fun g h => Units.ext (h_mul_deriv g h) }
  have hd_inj : Function.Injective d_p := by
    rw [← MonoidHom.ker_eq_bot_iff, Subgroup.eq_bot_iff_forall]
    intro g hg
    have hg_deriv : deriv (A.act g) A.p = 1 := congrArg Units.val hg
    have hcard_pos : 0 < Fintype.card G := Fintype.card_pos
    have hiter_U : ∀ z ∈ A.U, ((A.act g)^[Fintype.card G]) z = z := by
      intro z hz
      rw [A.iterate_eq_pow g (Fintype.card G) z hz, pow_card_eq_one, A.act_one z hz]
    have hiter_nhds : (A.act g)^[Fintype.card G] =ᶠ[nhds A.p] id := by
      filter_upwards [A.isOpen_U.mem_nhds A.mem_p] with z hz
      exact hiter_U z hz
    have hev_id : A.act g =ᶠ[nhds A.p] id :=
      cartan_analytic_germ_rigidity hcard_pos (A.analytic_act g A.p A.mem_p)
        (A.fix_p g) hg_deriv hiter_nhds
    have heqOn_U : Set.EqOn (A.act g) id A.U :=
      AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq
        (A.analytic_act g) analyticOnNhd_id A.isPreconnected_U A.mem_p hev_id
    exact A.faithful_on_U g heqOn_U
  rcases isCyclic_and_generator_of_injective_units_hom d_p hd_inj with ⟨hcyc, hgen⟩
  exact ⟨⟨d_p, fun _ => rfl, hd_inj⟩, hcyc, hgen⟩

/-- Partition classification of cycle-type lists of sum $\le 5$ with parts $\ge 2$. -/
private lemma list_ge2_sum_le5 (L : List ℕ) (hge : ∀ x ∈ L, 2 ≤ x) (hsum : L.sum ≤ 5) :
    L.foldr Nat.lcm 1 ∈ ({1, 2, 3, 4, 5, 6} : Finset ℕ) ∧
    ((-1 : ℤ) ^ (L.sum + L.length) = 1 → L.foldr Nat.lcm 1 ∈ ({1, 2, 3, 5} : Finset ℕ)) := by
  match L with
  | [] => decide
  | [a] =>
    have ha2 : 2 ≤ a := hge a (by simp)
    have ha5 : a ≤ 5 := by simpa using hsum
    have hcases : a = 2 ∨ a = 3 ∨ a = 4 ∨ a = 5 := by omega
    rcases hcases with rfl | rfl | rfl | rfl <;> decide
  | [a, b] =>
    have ha2 : 2 ≤ a := hge a (by simp)
    have hb2 : 2 ≤ b := hge b (by simp)
    have hab5 : a + b ≤ 5 := by simpa using hsum
    have hcases : (a = 2 ∧ b = 2) ∨ (a = 2 ∧ b = 3) ∨ (a = 3 ∧ b = 2) := by omega
    rcases hcases with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ <;> decide
  | a :: b :: c :: _ =>
    exfalso
    have ha2 : 2 ≤ a := hge a (by simp)
    have hb2 : 2 ≤ b := hge b (by simp)
    have hc2 : 2 ≤ c := hge c (by simp)
    simp only [List.sum_cons] at hsum
    omega

/-- Every permutation $\sigma \in S_5 = \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,5)$ has element order
    in $\{1, 2, 3, 4, 5, 6\}$, and every even permutation ($\mathrm{sign}(\sigma) = 1$, i.e. $A_5$)
    has element order in $\{1, 2, 3, 5\}$. -/
theorem perm5_element_orders :
    (∀ σ : Equiv.Perm (Fin 5), orderOf σ ∈ ({1, 2, 3, 4, 5, 6} : Finset ℕ)) ∧
    (∀ σ : Equiv.Perm (Fin 5), Equiv.Perm.sign σ = 1 →
      orderOf σ ∈ ({1, 2, 3, 5} : Finset ℕ)) := by
  have hmain : ∀ σ : Equiv.Perm (Fin 5),
      orderOf σ ∈ ({1, 2, 3, 4, 5, 6} : Finset ℕ) ∧
      (Equiv.Perm.sign σ = 1 → orderOf σ ∈ ({1, 2, 3, 5} : Finset ℕ)) := by
    intro σ
    obtain ⟨L, hL⟩ := Quot.exists_rep σ.cycleType
    have hct : σ.cycleType = (L : Multiset ℕ) := hL.symm
    have hge : ∀ x ∈ L, 2 ≤ x := by
      intro x hx
      have hmem : x ∈ σ.cycleType := by rw [hct]; exact hx
      exact Equiv.Perm.two_le_of_mem_cycleType hmem
    have hsum : L.sum ≤ 5 := by
      have hs : σ.cycleType.sum = σ.support.card := Equiv.Perm.sum_cycleType σ
      have hcard : σ.support.card ≤ 5 := le_trans (Finset.card_le_univ _) (by decide)
      rw [hct, Multiset.sum_coe] at hs
      omega
    have hlcm : orderOf σ = L.foldr Nat.lcm 1 := by
      rw [← Equiv.Perm.lcm_cycleType σ, hct]
      rfl
    have hsign_iff : Equiv.Perm.sign σ = 1 → (-1 : ℤ) ^ (L.sum + L.length) = 1 := by
      intro hs
      have hsc := Equiv.Perm.sign_of_cycleType σ
      rw [hs, hct, Multiset.sum_coe, Multiset.coe_card] at hsc
      exact congrArg (fun u : ℤˣ => (u : ℤ)) hsc.symm
    rw [hlcm]
    rcases list_ge2_sum_le5 L hge hsum with ⟨h1, h2⟩
    exact ⟨h1, fun hs => h2 (hsign_iff hs)⟩
  exact ⟨fun σ => (hmain σ).1, fun σ hs => (hmain σ).2 hs⟩

/-- Concrete discharge of `hstabS` and `hstabA` (`qou-m1bg`): any cyclic subgroup
    $H \le \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,5)$ has cardinality in $\{1, 2, 3, 4, 5, 6\}$,
    and if $H$ consists of even permutations, its cardinality lies in $\{1, 2, 3, 5\}$. -/
theorem cyclic_subgroup_perm5_card_mem (H : Subgroup (Equiv.Perm (Fin 5))) [Fintype H]
    (hcyc : IsCyclic H) :
    Fintype.card H ∈ ({1, 2, 3, 4, 5, 6} : Finset ℕ) ∧
    ((∀ h : H, Equiv.Perm.sign (h : Equiv.Perm (Fin 5)) = 1) →
      Fintype.card H ∈ ({1, 2, 3, 5} : Finset ℕ)) := by
  obtain ⟨g₀, hg₀⟩ := @IsCyclic.exists_ofOrder_eq_natCard H _ hcyc
  rw [Nat.card_eq_fintype_card] at hg₀
  have hord_sub : orderOf (g₀ : Equiv.Perm (Fin 5)) = orderOf g₀ := Subgroup.orderOf_coe g₀
  have hcard_eq : Fintype.card H = orderOf (g₀ : Equiv.Perm (Fin 5)) := by omega
  rw [hcard_eq]
  exact ⟨perm5_element_orders.1 g₀, fun heven => perm5_element_orders.2 g₀ (heven g₀)⟩

/-- Finite $G$-equivariant 2-dimensional cell complex $(V, E, F)$ in which $G$ acts freely
    on 1-cells $E$ and 2-cells $F$ (`qou-m3tr`), so all ramification is concentrated at the
    0-cells $V$. -/
structure EquivariantCellComplex (G : Type*) [Group G] [Fintype G] where
  V : Type*
  E : Type*
  F : Type*
  [fintypeV : Fintype V]
  [fintypeE : Fintype E]
  [fintypeF : Fintype F]
  [actionV : MulAction G V]
  [actionE : MulAction G E]
  [actionF : MulAction G F]
  edgeVerts : E → V → Prop
  faceEdges : F → E → Prop
  equivariant_edgeVerts : ∀ (g : G) (e : E) (v : V), edgeVerts (g • e) (g • v) ↔ edgeVerts e v
  equivariant_faceEdges : ∀ (g : G) (f : F) (e : E), faceEdges (g • f) (g • e) ↔ faceEdges f e
  freeE : ∀ (g : G) (e : E), g • e = e → g = 1
  freeF : ∀ (g : G) (f : F), g • f = f → g = 1

attribute [instance] EquivariantCellComplex.fintypeV EquivariantCellComplex.fintypeE
  EquivariantCellComplex.fintypeF EquivariantCellComplex.actionV
  EquivariantCellComplex.actionE EquivariantCellComplex.actionF

/-- Well-definedness of quotient edge-vertex incidence on orbit sets $(E/G) \times (V/G)$. -/
def EquivariantCellComplex.quotientEdgeVerts {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) :
    Quotient (MulAction.orbitRel G C.E) → Quotient (MulAction.orbitRel G C.V) → Prop :=
  Quotient.lift₂
    (fun e v => ∃ g : G, C.edgeVerts e (g • v))
    (by
      intro e₁ v₁ e₂ v₂ he hv
      rcases he with ⟨ge, rfl⟩
      rcases hv with ⟨gv, rfl⟩
      ext
      constructor
      · rintro ⟨g, hg⟩
        refine ⟨ge⁻¹ * g * gv, ?_⟩
        have heq : g • gv • v₂ = ge • ((ge⁻¹ * g * gv) • v₂) := by
          rw [← MulAction.mul_smul, ← MulAction.mul_smul, ← mul_assoc, ← mul_assoc,
              mul_inv_cancel, one_mul]
        rw [heq] at hg
        exact (C.equivariant_edgeVerts ge e₂ _).mp hg
      · rintro ⟨g, hg⟩
        refine ⟨ge * g * gv⁻¹, ?_⟩
        have h := (C.equivariant_edgeVerts ge e₂ (g • v₂)).mpr hg
        rw [MulAction.mul_smul, MulAction.mul_smul, inv_smul_smul]
        exact h)

/-- Well-definedness of quotient face-edge incidence on orbit sets $(F/G) \times (E/G)$. -/
def EquivariantCellComplex.quotientFaceEdges {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) :
    Quotient (MulAction.orbitRel G C.F) → Quotient (MulAction.orbitRel G C.E) → Prop :=
  Quotient.lift₂
    (fun f e => ∃ g : G, C.faceEdges f (g • e))
    (by
      intro f₁ e₁ f₂ e₂ hf he
      rcases hf with ⟨gf, rfl⟩
      rcases he with ⟨ge, rfl⟩
      ext
      constructor
      · rintro ⟨g, hg⟩
        refine ⟨gf⁻¹ * g * ge, ?_⟩
        have heq : g • ge • e₂ = gf • ((gf⁻¹ * g * ge) • e₂) := by
          rw [← MulAction.mul_smul, ← MulAction.mul_smul, ← mul_assoc, ← mul_assoc,
              mul_inv_cancel, one_mul]
        rw [heq] at hg
        exact (C.equivariant_faceEdges gf f₂ _).mp hg
      · rintro ⟨g, hg⟩
        refine ⟨gf * g * ge⁻¹, ?_⟩
        have h := (C.equivariant_faceEdges gf f₂ (g • e₂)).mpr hg
        rw [MulAction.mul_smul, MulAction.mul_smul, inv_smul_smul]
        exact h)

/-- Cardinality of a $G$-orbit $o \in X / G$ measured as a fiber of the quotient projection. -/
noncomputable def orbitFiberCard {G : Type*} [Group G] (X : Type*) [MulAction G X] [Fintype X]
    (o : Quotient (MulAction.orbitRel G X)) : ℕ := by
  classical
  exact (Finset.univ.filter (fun x : X => Quotient.mk (MulAction.orbitRel G X) x = o)).card

/-- Upstairs Euler characteristic $|V| - |E| + |F|$ of an `EquivariantCellComplex`. -/
def EquivariantCellComplex.upstairsEuler {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) : ℤ :=
  (Fintype.card C.V : ℤ) - (Fintype.card C.E : ℤ) + (Fintype.card C.F : ℤ)

/-- Quotient Euler characteristic $|V/G| - |E/G| + |F/G|$ of an `EquivariantCellComplex`. -/
noncomputable def EquivariantCellComplex.quotientEuler {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) : ℤ := by
  classical
  exact (Fintype.card (Quotient (MulAction.orbitRel G C.V)) : ℤ) -
        (Fintype.card (Quotient (MulAction.orbitRel G C.E)) : ℤ) +
        (Fintype.card (Quotient (MulAction.orbitRel G C.F)) : ℤ)

section CellularRiemannHurwitz
open Classical

/-- Orbit-stabilizer relation for `orbitFiberCard`: for every $x \in X$,
    $|\mathrm{orbit}(x)| \cdot |\mathrm{Stab}_G(x)| = |G|$. -/
theorem orbitFiberCard_mul_stabilizer_eq_card_group {G : Type*} [Group G] [Fintype G]
    (X : Type*) [MulAction G X] [Fintype X] (x : X) :
    orbitFiberCard (G := G) X (Quotient.mk (MulAction.orbitRel G X) x) *
      Fintype.card (MulAction.stabilizer G x) = Fintype.card G := by
  have hfib : orbitFiberCard (G := G) X (Quotient.mk (MulAction.orbitRel G X) x) =
      Fintype.card (MulAction.orbit G x) := by
    unfold orbitFiberCard
    symm
    rw [Fintype.card_of_subtype (Finset.univ.filter (fun y : X =>
      Quotient.mk (MulAction.orbitRel G X) y = Quotient.mk (MulAction.orbitRel G X) x))]
    intro y
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Quotient.eq]
    rfl
  rw [hfib]
  exact MulAction.card_orbit_mul_card_stabilizer_eq_card_group G x

/-- Partition of a finite $G$-set $X$ into orbit fibers: $\sum_{o \in X/G} |o| = |X|$. -/
theorem sum_orbitFiberCard_eq_card {G : Type*} [Group G]
    (X : Type*) [MulAction G X] [Fintype X] :
    (∑ o : Quotient (MulAction.orbitRel G X), orbitFiberCard (G := G) X o) = Fintype.card X := by
  unfold orbitFiberCard
  have h := Finset.card_eq_sum_card_fiberwise
    (f := fun x : X => Quotient.mk (MulAction.orbitRel G X) x)
    (s := Finset.univ) (t := Finset.univ) (fun _ _ => Finset.mem_univ _)
  exact h.symm

/-- Free finite $G$-action orbit count: if $G$ acts freely on $X$, then $|X| = |G| \cdot |X/G|$. -/
theorem card_eq_card_group_mul_quotient_of_free {G : Type*} [Group G] [Fintype G]
    (X : Type*) [MulAction G X] [Fintype X]
    (hfree : ∀ g : G, ∀ x : X, g • x = x → g = 1) :
    Fintype.card X = Fintype.card G * Fintype.card (Quotient (MulAction.orbitRel G X)) := by
  have hburn := MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group G X
  have hfix : (∑ g : G, Fintype.card (MulAction.fixedBy X g)) = Fintype.card X := by
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ (1 : G))]
    have h1 : Fintype.card (MulAction.fixedBy X (1 : G)) = Fintype.card X := by
      apply Fintype.card_of_bijective (f := Subtype.val)
      refine ⟨Subtype.val_injective, fun x => ⟨⟨x, one_smul G x⟩, rfl⟩⟩
    have hrest : ∑ g ∈ Finset.univ.erase (1 : G), Fintype.card (MulAction.fixedBy X g) = 0 := by
      apply Finset.sum_eq_zero
      intro g hg
      have hg1 : g ≠ 1 := (Finset.mem_erase.mp hg).1
      rw [Fintype.card_eq_zero_iff]
      exact ⟨fun ⟨x, hx⟩ => hg1 (hfree g x hx)⟩
    rw [h1, hrest, add_zero]
  rw [hfix] at hburn
  rw [hburn, Nat.mul_comm]

/-- Double-counting / Burnside stabilizer sum: $\sum_{x \in X} |\mathrm{Stab}_G(x)| = |X/G| \cdot |G|$. -/
theorem sum_card_stabilizer_eq_card_orbits_mul_card_group {G : Type*} [Group G] [Fintype G]
    (X : Type*) [MulAction G X] [Fintype X] :
    (∑ x : X, Fintype.card (MulAction.stabilizer G x)) =
      Fintype.card (Quotient (MulAction.orbitRel G X)) * Fintype.card G := by
  have hburn := MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group G X
  have hdouble :
      (∑ x : X, Fintype.card (MulAction.stabilizer G x)) =
      (∑ g : G, Fintype.card (MulAction.fixedBy X g)) := by
    have hstab : ∀ x : X, Fintype.card (MulAction.stabilizer G x) =
        (Finset.univ.filter (fun g : G => g • x = x)).card := by
      intro x
      rw [Fintype.card_of_subtype (Finset.univ.filter (fun g : G => g • x = x))]
      intro g; simp [MulAction.mem_stabilizer_iff]
    have hfix : ∀ g : G, Fintype.card (MulAction.fixedBy X g) =
        (Finset.univ.filter (fun x : X => g • x = x)).card := by
      intro g
      rw [Fintype.card_of_subtype (Finset.univ.filter (fun x : X => g • x = x))]
      intro x; simp [MulAction.mem_fixedBy]
    simp_rw [hstab, hfix, Finset.card_filter]
    exact Finset.sum_comm
  rw [hdouble, hburn]

/-- $G$-Equivariant Cell Complex Riemann–Hurwitz in orbit-deficit form (`qou-m3tr`):
    $$|V| - |E| + |F| \;=\; |G|\,(|V/G| - |E/G| + |F/G|) \;-\; \sum_{o \in V/G} (|G| - |o|).$$ -/
theorem equivariant_cell_riemann_hurwitz_orbit_deficit {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) :
    C.upstairsEuler =
      (Fintype.card G : ℤ) * C.quotientEuler -
      ∑ o : Quotient (MulAction.orbitRel G C.V),
        ((Fintype.card G : ℤ) - (orbitFiberCard (G := G) C.V o : ℤ)) := by
  have hV_nat := sum_orbitFiberCard_eq_card (G := G) C.V
  have hE_nat := card_eq_card_group_mul_quotient_of_free (G := G) C.E C.freeE
  have hF_nat := card_eq_card_group_mul_quotient_of_free (G := G) C.F C.freeF
  have hsum_def :
      (∑ o : Quotient (MulAction.orbitRel G C.V),
        ((Fintype.card G : ℤ) - (orbitFiberCard (G := G) C.V o : ℤ))) =
      (Fintype.card (Quotient (MulAction.orbitRel G C.V)) : ℤ) * (Fintype.card G : ℤ) -
      (Fintype.card C.V : ℤ) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    have hV_int : (∑ o : Quotient (MulAction.orbitRel G C.V),
        (orbitFiberCard (G := G) C.V o : ℤ)) = (Fintype.card C.V : ℤ) := by
      exact_mod_cast hV_nat
    rw [hV_int]
  have hE_int : (Fintype.card C.E : ℤ) =
      (Fintype.card G : ℤ) * (Fintype.card (Quotient (MulAction.orbitRel G C.E)) : ℤ) := by
    exact_mod_cast hE_nat
  have hF_int : (Fintype.card C.F : ℤ) =
      (Fintype.card G : ℤ) * (Fintype.card (Quotient (MulAction.orbitRel G C.F)) : ℤ) := by
    exact_mod_cast hF_nat
  unfold EquivariantCellComplex.upstairsEuler EquivariantCellComplex.quotientEuler
  rw [hsum_def, hE_int, hF_int]
  ring

/-- Equality between the orbit-deficit sum $\sum_{o \in V/G} (|G| - |o|)$ and the pointwise
    ramification sum $\sum_{v \in V} (|\mathrm{Stab}_G(v)| - 1)$, together with the exact
    genus Riemann–Hurwitz identity $2 - 2\tilde{g} = |G|(2 - 2g) - \sum_{v \in V} (e_v - 1)$
    (`qou-m3tr`). -/
theorem equivariant_cell_riemann_hurwitz_stabilizer_and_genus {G : Type*} [Group G] [Fintype G]
    (C : EquivariantCellComplex G) :
    (∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1)) =
      (∑ o : Quotient (MulAction.orbitRel G C.V),
        ((Fintype.card G : ℤ) - (orbitFiberCard (G := G) C.V o : ℤ))) ∧
    C.upstairsEuler =
      (Fintype.card G : ℤ) * C.quotientEuler -
      ∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1) ∧
    (∀ gUp gQuot : ℤ,
      C.upstairsEuler = 2 - 2 * gUp →
      C.quotientEuler = 2 - 2 * gQuot →
      2 - 2 * gUp = (Fintype.card G : ℤ) * (2 - 2 * gQuot) -
        ∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1)) := by
  have hstab_nat := sum_card_stabilizer_eq_card_orbits_mul_card_group (G := G) C.V
  have hV_nat := sum_orbitFiberCard_eq_card (G := G) C.V
  have hram :
      (∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1)) =
      (Fintype.card (Quotient (MulAction.orbitRel G C.V)) : ℤ) * (Fintype.card G : ℤ) -
      (Fintype.card C.V : ℤ) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
    have hstab_int : (∑ v : C.V, (Fintype.card (MulAction.stabilizer G v) : ℤ)) =
        (Fintype.card (Quotient (MulAction.orbitRel G C.V)) : ℤ) * (Fintype.card G : ℤ) := by
      exact_mod_cast hstab_nat
    rw [hstab_int]
  have hdef :
      (∑ o : Quotient (MulAction.orbitRel G C.V),
        ((Fintype.card G : ℤ) - (orbitFiberCard (G := G) C.V o : ℤ))) =
      (Fintype.card (Quotient (MulAction.orbitRel G C.V)) : ℤ) * (Fintype.card G : ℤ) -
      (Fintype.card C.V : ℤ) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    have hV_int : (∑ o : Quotient (MulAction.orbitRel G C.V),
        (orbitFiberCard (G := G) C.V o : ℤ)) = (Fintype.card C.V : ℤ) := by
      exact_mod_cast hV_nat
    rw [hV_int]
  have heq_sums : (∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1)) =
      (∑ o : Quotient (MulAction.orbitRel G C.V),
        ((Fintype.card G : ℤ) - (orbitFiberCard (G := G) C.V o : ℤ))) := by
    rw [hram, hdef]
  have hrh_orb := equivariant_cell_riemann_hurwitz_orbit_deficit C
  have hrh_stab : C.upstairsEuler =
      (Fintype.card G : ℤ) * C.quotientEuler -
      ∑ v : C.V, ((Fintype.card (MulAction.stabilizer G v) : ℤ) - 1) := by
    rw [hrh_orb, heq_sums]
  refine ⟨heq_sums, hrh_stab, ?_⟩
  intro gUp gQuot hUp hQuot
  rw [← hUp, ← hQuot]
  exact hrh_stab

end CellularRiemannHurwitz

/-- Explicit concrete inhabitant of `EquivariantCellComplex (Equiv.Perm (Fin 5))` on a regular
    120-sheeted cell decomposition over a 1-vertex, 4-edge, 1-face genus-2 graph, demonstrating
    non-vacuity of `EquivariantCellComplex` for $G = S_5$ with $|V| = 120$, $|E| = 480$,
    $|F| = 120$. -/
def regularS5CellComplexInhabitant : EquivariantCellComplex (Equiv.Perm (Fin 5)) where
  V := Equiv.Perm (Fin 5)
  E := Equiv.Perm (Fin 5) × Fin 4
  F := Equiv.Perm (Fin 5)
  actionV := { smul := (· * ·), one_smul := one_mul, mul_smul := mul_assoc }
  actionE :=
    { smul := fun g p => (g * p.1, p.2)
      one_smul := fun p => Prod.ext (one_mul p.1) rfl
      mul_smul := fun g h p => Prod.ext (mul_assoc g h p.1) rfl }
  actionF := { smul := (· * ·), one_smul := one_mul, mul_smul := mul_assoc }
  edgeVerts e v := e.1 = v
  faceEdges f e := e.1 = f
  equivariant_edgeVerts g e v := by
    change g * e.1 = g * v ↔ e.1 = v
    exact mul_right_inj g
  equivariant_faceEdges g f e := by
    change g * e.1 = g * f ↔ e.1 = f
    exact mul_right_inj g
  freeE g e h := by
    have h1 : g * e.1 = e.1 := congrArg Prod.fst h
    exact mul_eq_right.mp h1
  freeF g f h := by
    change g * f = f at h
    exact mul_eq_right.mp h

-- ============================================================================
-- §2. Integral Seifert Homology & Braid Symplectic Representation (`qou-pzsi`)
-- ============================================================================

/-- Abbreviation for $8 \times 8$ integral matrices acting on $H_1(\Sigma_4; \mathbb{Z}) \cong \mathbb{Z}^8$. -/
abbrev Mat8Z := Matrix (Fin 8) (Fin 8) ℤ

/-- Standard genus-4 unimodular symplectic intersection form
    $\Omega_8 = \begin{pmatrix} 0 & I_4 \\ -I_4 & 0 \end{pmatrix}$ on $H_1(\Sigma_4; \mathbb{Z}) \cong \mathbb{Z}^8$. -/
def symplecticOmega8 : Mat8Z :=
  Matrix.of fun i j =>
    if i.val + 4 = j.val then 1 else if j.val + 4 = i.val then -1 else 0

/-- Predicate that an $8 \times 8$ integer matrix $M$ lies in the integral symplectic group
    $\mathrm{Sp}(8, \mathbb{Z}) = \{M \in M_8(\mathbb{Z}) \mid M^T \Omega_8 M = \Omega_8\}$. -/
def IsSymplectic8Z (M : Mat8Z) : Prop :=
  M.transpose * symplecticOmega8 * M = symplecticOmega8

/-- Canonical Stallings $8 \times 8$ integral Seifert matrix $S_{3,5}$ of the 3-strand torus
    braid $(\sigma_1 \sigma_2)^5 \in B_3$ (closing to $T_{3,5}$ of Seifert rank $(3-1)(5-1) = 8$). -/
def seifertT35 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 1 | 4, 4 | 5, 2 | 5, 5 | 6, 3 | 6, 6 | 7, 7 => 1
    | 1, 0 | 2, 1 | 3, 2 | 4, 0 | 5, 1 | 5, 4 | 6, 2 | 6, 5 | 7, 3 | 7, 6 => -1
    | _, _ => 0

/-- Exact integral inverse $S_{3,5}^{-1} \in \mathrm{GL}(8, \mathbb{Z})$ of `seifertT35`. -/
def seifertT35Inv : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 1, 0 | 1, 1 | 2, 0 | 2, 1 | 2, 2 | 3, 0 | 3, 1 | 3, 2 | 3, 3
    | 4, 4 | 5, 4 | 5, 5 | 6, 4 | 6, 5 | 6, 6 | 7, 0 | 7, 4 | 7, 5 | 7, 6 | 7, 7 => 1
    | 4, 1 | 5, 1 | 5, 2 | 6, 1 | 6, 2 | 6, 3 => -1
    | _, _ => 0

/-- Skew-symmetric Seifert intersection matrix $J_{3,5} = S_{3,5} - S_{3,5}^T$ on $H_1(\Sigma_{T_{3,5}}; \mathbb{Z})$. -/
def intersectionT35 : Mat8Z := seifertT35 - seifertT35.transpose

/-- Integral monodromy matrix $M_{3,5} = S_{3,5}^{-1} S_{3,5}^T$ of the fibered torus knot $T_{3,5}$. -/
def monodromyT35 : Mat8Z := seifertT35Inv * seifertT35.transpose

/-- Unimodular Darboux basis matrix $P_{3,5} \in \mathrm{GL}(8, \mathbb{Z})$ satisfying
    $P_{3,5}^T J_{3,5} P_{3,5} = \Omega_8$. -/
def darbouxP35 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 0, 1 | 0, 3 | 1, 4 | 2, 1 | 3, 3 | 3, 5 | 4, 2 | 5, 3 | 6, 6 | 6, 7 | 7, 7 => 1
    | 0, 2 | 0, 6 | 1, 2 | 2, 6 | 3, 2 | 3, 6 | 3, 7 => -1
    | _, _ => 0

/-- Exact integral inverse $P_{3,5}^{-1} \in \mathrm{GL}(8, \mathbb{Z})$ of `darbouxP35`. -/
def darbouxP35Inv : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 0, 4 | 1, 2 | 1, 6 | 2, 4 | 3, 5 | 4, 1 | 4, 4 | 5, 3 | 5, 4 | 5, 6 | 6, 6 | 7, 7 => 1
    | 0, 2 | 0, 5 | 1, 7 | 5, 5 | 6, 7 => -1
    | _, _ => 0

/-- Darboux-conjugated $T_{3,5}$ monodromy inside standard $\mathrm{Sp}(8, \mathbb{Z})$. -/
def darbouxMonodromyT35 : Mat8Z := darbouxP35Inv * monodromyT35 * darbouxP35

/-- Canonical Stallings $8 \times 8$ integral Seifert matrix $S_{2,9}$ of the 2-strand torus
    braid $\sigma_1^9 \in B_2$ (closing to $T_{2,9}$ of Seifert rank $(2-1)(9-1) = 8$). -/
def seifertT29 : Mat8Z :=
  Matrix.of fun i j =>
    if i = j then 1 else if i.val = j.val + 1 then -1 else 0

/-- Exact integral inverse $S_{2,9}^{-1} \in \mathrm{GL}(8, \mathbb{Z})$ of `seifertT29`. -/
def seifertT29Inv : Mat8Z :=
  Matrix.of fun i j => if j ≤ i then 1 else 0

/-- Skew-symmetric Seifert intersection matrix $J_{2,9} = S_{2,9} - S_{2,9}^T$. -/
def intersectionT29 : Mat8Z := seifertT29 - seifertT29.transpose

/-- Integral monodromy matrix $M_{2,9} = S_{2,9}^{-1} S_{2,9}^T$ of the fibered torus knot $T_{2,9}$. -/
def monodromyT29 : Mat8Z := seifertT29Inv * seifertT29.transpose

/-- Unimodular Darboux basis matrix $P_{2,9} \in \mathrm{GL}(8, \mathbb{Z})$ satisfying
    $P_{2,9}^T J_{2,9} P_{2,9} = \Omega_8$. -/
def darbouxP29 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 0, 1 | 0, 2 | 0, 3 => 1
    | 2, 1 | 2, 2 | 2, 3 => 1
    | 4, 2 | 4, 3 => 1
    | 6, 3 => 1
    | 1, 4 | 3, 5 | 5, 6 | 7, 7 => 1
    | _, _ => 0

/-- Exact integral inverse $P_{2,9}^{-1} \in \mathrm{GL}(8, \mathbb{Z})$ of `darbouxP29`. -/
def darbouxP29Inv : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 1, 2 | 2, 4 | 3, 6 => 1
    | 0, 2 | 1, 4 | 2, 6 => -1
    | 4, 1 | 5, 3 | 6, 5 | 7, 7 => 1
    | _, _ => 0

/-- Darboux-conjugated $T_{2,9}$ monodromy inside standard $\mathrm{Sp}(8, \mathbb{Z})$. -/
def darbouxMonodromyT29 : Mat8Z := darbouxP29Inv * monodromyT29 * darbouxP29

/-- Polymorphic determinant multiplication helper avoiding concrete `Perm (Fin 8)` unfolding. -/
private lemma det_eq_one_of_ulu {n : Type*} [Fintype n] [DecidableEq n]
    (U L UL Ω : Matrix n n ℤ)
    (hUL : U * L = UL) (hfac : UL * U = Ω.transpose)
    (hU : U.det = 1) (hL : L.det = 1) :
    Ω.det = 1 := by
  rw [← Matrix.det_transpose Ω, ← hfac, ← hUL, Matrix.det_mul, Matrix.det_mul, hU, hL]
  ring

/-- Polymorphic unimodular congruence determinant helper avoiding `Perm (Fin 8)` unfolding. -/
private lemma det_eq_one_of_cong {n : Type*} [Fintype n] [DecidableEq n]
    (P PInv J Ω : Matrix n n ℤ)
    (hP : P * PInv = 1) (hcong : P.transpose * J * P = Ω) (hΩ : Ω.det = 1) :
    J.det = 1 := by
  have h1 : P.det * PInv.det = 1 := by rw [← Matrix.det_mul, hP, Matrix.det_one]
  have hsq : P.det * P.det = 1 := by
    rcases Int.mul_eq_one_iff_eq_one_or_neg_one.mp h1 with ⟨hp, _⟩ | ⟨hp, _⟩ <;> simp [hp]
  have hc := congrArg Matrix.det hcong
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose, hΩ] at hc
  calc J.det = (P.det * P.det) * J.det := by rw [hsq, one_mul]
    _ = P.det * J.det * P.det := by ring
    _ = 1 := hc

/-- Elementary triangular factorization showing $\det(\Omega_8) = 1$ without $8!$ Laplace expansion. -/
private def omegaU8 : Mat8Z :=
  Matrix.of fun i j => if i = j then 1 else if i.val + 4 = j.val then -1 else 0

private def omegaL8 : Mat8Z :=
  Matrix.of fun i j => if i = j then 1 else if j.val + 4 = i.val then 1 else 0

private def omegaUL8 : Mat8Z :=
  Matrix.of fun i j =>
    if i.val + 4 = j.val then -1
    else if j.val + 4 = i.val then 1
    else if 4 ≤ i.val ∧ i = j then 1 else 0

theorem symplecticOmega8_det_eq_one : symplecticOmega8.det = 1 := by
  have hUL : omegaU8 * omegaL8 = omegaUL8 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hfac : omegaUL8 * omegaU8 = symplecticOmega8.transpose := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hU_tri : Matrix.BlockTriangular omegaU8 id := by
    intro i j hij
    have hlt : j.val < i.val := hij
    have hne : i ≠ j := fun h => by subst h; omega
    have hadd : ¬ (i.val + 4 = j.val) := by omega
    simp only [omegaU8, Matrix.of_apply, hne, hadd, ↓reduceIte]
  have hLT_tri : Matrix.BlockTriangular omegaL8.transpose id := by
    intro i j hij
    have hlt : j.val < i.val := hij
    have hne : j ≠ i := fun h => by subst h; omega
    have hadd : ¬ (i.val + 4 = j.val) := by omega
    simp only [omegaL8, Matrix.transpose_apply, Matrix.of_apply, hne, hadd, ↓reduceIte]
  have hU_det : omegaU8.det = 1 := by
    rw [Matrix.det_of_upperTriangular hU_tri]
    exact Finset.prod_eq_one (fun i _ => by simp [omegaU8])
  have hL_det : omegaL8.det = 1 := by
    rw [← Matrix.det_transpose omegaL8, Matrix.det_of_upperTriangular hLT_tri]
    exact Finset.prod_eq_one (fun i _ => by simp [omegaL8])
  exact det_eq_one_of_ulu omegaU8 omegaL8 omegaUL8 symplecticOmega8 hUL hfac hU_det hL_det

/-- Helper flat matrix values for shallow-depth verification of $M_{3,5}$ and $M_{2,9}$ powers. -/
private def m35Val : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 1, 0 | 2, 0 | 3, 0 | 4, 2 | 5, 3 | 7, 0 => 1
    | 0, 1 | 0, 4 | 1, 2 | 1, 5 | 2, 3 | 2, 6 | 3, 7 | 4, 1 | 5, 1 | 6, 1 | 7, 1 => -1
    | _, _ => 0

private def m35Pow3 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 3 | 2, 0 | 3, 1 | 4, 7 | 6, 4 | 7, 5 => 1
    | 0, 2 | 1, 2 | 2, 2 | 3, 2 | 4, 6 | 5, 6 | 6, 6 | 7, 6 => -1
    | _, _ => 0

private def m35Pow5 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 1, 4 | 2, 5 | 3, 6 | 4, 0 | 5, 0 | 6, 0 | 7, 0 => 1
    | 0, 7 | 1, 7 | 2, 7 | 3, 7 | 4, 1 | 4, 4 | 5, 2 | 5, 5 | 6, 3 | 6, 6 | 7, 7 => -1
    | _, _ => 0

private def m29Val : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 | 1, 0 | 2, 0 | 3, 0 | 4, 0 | 5, 0 | 6, 0 | 7, 0 => 1
    | 0, 1 | 1, 2 | 2, 3 | 3, 4 | 4, 5 | 5, 6 | 6, 7 => -1
    | _, _ => 0

private def m29Pow3 : Mat8Z :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 2 | 1, 2 | 2, 2 | 3, 2 | 4, 2 | 5, 2 | 6, 2 | 7, 2 => 1
    | 0, 3 | 1, 4 | 2, 5 | 3, 6 | 4, 7 | 6, 0 | 7, 1 => -1
    | _, _ => 0

/-- Unimodularity ($\det S = 1$, $\det(S - S^T) = 1$), symplectic preservation, and finite
    monodromy order for the $T_{3,5}$ and $T_{2,9}$ Seifert structures on $\mathbb{Z}^8$. -/
theorem seifert_t35_and_t29_unimodular_symplectic :
    seifertT35.det = 1 ∧
    seifertT29.det = 1 ∧
    intersectionT35.det = 1 ∧
    intersectionT29.det = 1 ∧
    seifertT35 * seifertT35Inv = 1 ∧
    seifertT29 * seifertT29Inv = 1 ∧
    darbouxP35.transpose * intersectionT35 * darbouxP35 = symplecticOmega8 ∧
    darbouxP29.transpose * intersectionT29 * darbouxP29 = symplecticOmega8 ∧
    monodromyT35.transpose * intersectionT35 * monodromyT35 = intersectionT35 ∧
    IsSymplectic8Z darbouxMonodromyT35 ∧
    IsSymplectic8Z darbouxMonodromyT29 ∧
    monodromyT35 ^ 15 = 1 ∧
    monodromyT29 ^ 18 = 1 := by
  have h35_tri : Matrix.BlockTriangular seifertT35.transpose id := by
    intro i j hij
    have hlt : j.val < i.val := hij
    fin_cases i <;> fin_cases j <;> (first | (dsimp only at hlt; omega) | rfl)
  have h29_tri : Matrix.BlockTriangular seifertT29.transpose id := by
    intro i j hij
    have hlt : j.val < i.val := hij
    have hne : j ≠ i := fun h => by subst h; omega
    have hsucc : ¬ (j.val = i.val + 1) := by omega
    simp only [seifertT29, Matrix.transpose_apply, Matrix.of_apply, hne, hsucc, ↓reduceIte]
  have hdet_s35 : seifertT35.det = 1 := by
    rw [← Matrix.det_transpose seifertT35, Matrix.det_of_upperTriangular h35_tri]
    exact Finset.prod_eq_one (fun i _ => by fin_cases i <;> rfl)
  have hdet_s29 : seifertT29.det = 1 := by
    rw [← Matrix.det_transpose seifertT29, Matrix.det_of_upperTriangular h29_tri]
    exact Finset.prod_eq_one (fun i _ => by simp [seifertT29])
  have hS35_inv : seifertT35 * seifertT35Inv = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hS29_inv : seifertT29 * seifertT29Inv = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hP35_inv : darbouxP35 * darbouxP35Inv = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hP35_invL : darbouxP35Inv * darbouxP35 = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hP29_inv : darbouxP29 * darbouxP29Inv = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hP29_invL : darbouxP29Inv * darbouxP29 = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hJP35 : intersectionT35 * darbouxP35 = darbouxP35Inv.transpose * symplecticOmega8 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hJP29 : intersectionT29 * darbouxP29 = darbouxP29Inv.transpose * symplecticOmega8 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hcong35 : darbouxP35.transpose * intersectionT35 * darbouxP35 = symplecticOmega8 := by
    calc darbouxP35.transpose * intersectionT35 * darbouxP35
        = darbouxP35.transpose * (intersectionT35 * darbouxP35) := Matrix.mul_assoc _ _ _
      _ = (darbouxP35Inv * darbouxP35).transpose * symplecticOmega8 := by
            rw [hJP35, ← Matrix.mul_assoc, ← Matrix.transpose_mul]
      _ = symplecticOmega8 := by rw [hP35_invL, Matrix.transpose_one, Matrix.one_mul]
  have hcong29 : darbouxP29.transpose * intersectionT29 * darbouxP29 = symplecticOmega8 := by
    calc darbouxP29.transpose * intersectionT29 * darbouxP29
        = darbouxP29.transpose * (intersectionT29 * darbouxP29) := Matrix.mul_assoc _ _ _
      _ = (darbouxP29Inv * darbouxP29).transpose * symplecticOmega8 := by
            rw [hJP29, ← Matrix.mul_assoc, ← Matrix.transpose_mul]
      _ = symplecticOmega8 := by rw [hP29_invL, Matrix.transpose_one, Matrix.one_mul]
  have hdet_j35 : intersectionT35.det = 1 :=
    det_eq_one_of_cong darbouxP35 darbouxP35Inv intersectionT35 symplecticOmega8
      hP35_inv hcong35 symplecticOmega8_det_eq_one
  have hdet_j29 : intersectionT29.det = 1 :=
    det_eq_one_of_cong darbouxP29 darbouxP29Inv intersectionT29 symplecticOmega8
      hP29_inv hcong29 symplecticOmega8_det_eq_one
  have hm35_eq : monodromyT35 = m35Val := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm29_eq : monodromyT29 = m29Val := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hseifert_symp : ∀ (S SInv : Mat8Z), S * SInv = 1 →
      (SInv * S.transpose).transpose * (S - S.transpose) * (SInv * S.transpose) =
      S - S.transpose := by
    intro S SInv hSS
    have hSST : SInv.transpose * S.transpose = 1 := by
      rw [← Matrix.transpose_mul, hSS, Matrix.transpose_one]
    rw [Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.mul_sub, Matrix.sub_mul]
    have ht1 : S * SInv.transpose * S * (SInv * S.transpose) = S := by
      calc S * SInv.transpose * S * (SInv * S.transpose)
          = S * SInv.transpose * (S * SInv) * S.transpose := by simp only [Matrix.mul_assoc]
        _ = S * (SInv.transpose * S.transpose) := by
              rw [hSS, Matrix.mul_one, Matrix.mul_assoc]
        _ = S := by rw [hSST, Matrix.mul_one]
    have ht2 : S * SInv.transpose * S.transpose * (SInv * S.transpose) = S.transpose := by
      calc S * SInv.transpose * S.transpose * (SInv * S.transpose)
          = S * (SInv.transpose * S.transpose) * (SInv * S.transpose) := by
              simp only [Matrix.mul_assoc]
        _ = (S * SInv) * S.transpose := by
              rw [hSST, Matrix.mul_one, Matrix.mul_assoc]
        _ = S.transpose := by rw [hSS, Matrix.one_mul]
    rw [ht1, ht2]
  have hsymp35 : monodromyT35.transpose * intersectionT35 * monodromyT35 = intersectionT35 :=
    hseifert_symp seifertT35 seifertT35Inv hS35_inv
  have hsymp29 : monodromyT29.transpose * intersectionT29 * monodromyT29 = intersectionT29 :=
    hseifert_symp seifertT29 seifertT29Inv hS29_inv
  have hdarb35 : IsSymplectic8Z darbouxMonodromyT35 := by
    unfold IsSymplectic8Z darbouxMonodromyT35
    have hJ : symplecticOmega8 = darbouxP35.transpose * intersectionT35 * darbouxP35 := hcong35.symm
    have hPT : darbouxP35Inv.transpose * darbouxP35.transpose = 1 := by
      rw [← Matrix.transpose_mul, hP35_inv, Matrix.transpose_one]
    calc (darbouxP35Inv * monodromyT35 * darbouxP35).transpose * symplecticOmega8 *
            (darbouxP35Inv * monodromyT35 * darbouxP35)
        = darbouxP35.transpose * monodromyT35.transpose *
            (darbouxP35Inv.transpose * darbouxP35.transpose) * intersectionT35 *
            (darbouxP35 * darbouxP35Inv) * monodromyT35 * darbouxP35 := by
          rw [hJ]
          simp only [Matrix.transpose_mul, Matrix.mul_assoc]
      _ = darbouxP35.transpose * (monodromyT35.transpose * intersectionT35 * monodromyT35) *
            darbouxP35 := by
          rw [hPT, hP35_inv]; simp only [Matrix.mul_one, Matrix.mul_assoc]
      _ = symplecticOmega8 := by rw [hsymp35, hcong35]
  have hdarb29 : IsSymplectic8Z darbouxMonodromyT29 := by
    unfold IsSymplectic8Z darbouxMonodromyT29
    have hJ : symplecticOmega8 = darbouxP29.transpose * intersectionT29 * darbouxP29 := hcong29.symm
    have hPT : darbouxP29Inv.transpose * darbouxP29.transpose = 1 := by
      rw [← Matrix.transpose_mul, hP29_inv, Matrix.transpose_one]
    calc (darbouxP29Inv * monodromyT29 * darbouxP29).transpose * symplecticOmega8 *
            (darbouxP29Inv * monodromyT29 * darbouxP29)
        = darbouxP29.transpose * monodromyT29.transpose *
            (darbouxP29Inv.transpose * darbouxP29.transpose) * intersectionT29 *
            (darbouxP29 * darbouxP29Inv) * monodromyT29 * darbouxP29 := by
          rw [hJ]
          simp only [Matrix.transpose_mul, Matrix.mul_assoc]
      _ = darbouxP29.transpose * (monodromyT29.transpose * intersectionT29 * monodromyT29) *
            darbouxP29 := by
          rw [hPT, hP29_inv]; simp only [Matrix.mul_one, Matrix.mul_assoc]
      _ = symplecticOmega8 := by rw [hsymp29, hcong29]
  have hm35_p3 : m35Val ^ 3 = m35Pow3 := by
    rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm35_p5 : m35Val ^ 5 = m35Pow5 := by
    rw [show (5 : ℕ) = 3 + 2 from rfl, pow_add, hm35_p3, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm35_15 : monodromyT35 ^ 15 = 1 := by
    rw [hm35_eq, show (15 : ℕ) = 5 * 3 from rfl, pow_mul, hm35_p5,
        show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm29_p3 : m29Val ^ 3 = m29Pow3 := by
    rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm29_p9 : m29Val ^ 9 = -1 := by
    rw [show (9 : ℕ) = 3 * 3 from rfl, pow_mul, hm29_p3,
        show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm29_18 : monodromyT29 ^ 18 = 1 := by
    rw [hm29_eq, show (18 : ℕ) = 9 * 2 from rfl, pow_mul, hm29_p9, sq, neg_mul_neg, one_mul]
  exact ⟨hdet_s35, hdet_s29, hdet_j35, hdet_j29, hS35_inv, hS29_inv,
         hcong35, hcong29, hsymp35, hdarb35, hdarb29, hm35_15, hm29_18⟩

/-- Monic polynomials over a field with one dividing the other and equal `natDegree` coincide. -/
lemma monic_eq_of_dvd_of_natDegree_eq {K : Type*} [Field K] {p q : Polynomial K}
    (hp : p.Monic) (hq : q.Monic) (hdvd : p ∣ q) (hdeg : p.natDegree = q.natDegree) :
    p = q := by
  rcases hdvd with ⟨r, rfl⟩
  have hr_ne : r ≠ 0 := right_ne_zero_of_mul hq.ne_zero
  have hdeg_mul : (p * r).natDegree = p.natDegree + r.natDegree :=
    Polynomial.natDegree_mul hp.ne_zero hr_ne
  have hr_deg : r.natDegree = 0 := by omega
  have hr_monic : r.Monic := by
    have hlc := Polynomial.leadingCoeff_mul p r
    rw [hp.leadingCoeff, one_mul, hq.leadingCoeff] at hlc
    exact hlc.symm
  have hr_one : r = 1 := Polynomial.eq_one_of_monic_natDegree_zero hr_monic hr_deg
  rw [hr_one, mul_one]

/-- A monic polynomial of positive degree dividing a monic irreducible polynomial over a field
    equals that irreducible polynomial. -/
lemma monic_eq_of_irreducible_of_dvd {K : Type*} [Field K] {p q : Polynomial K}
    (hp : p.Monic) (hdeg_pos : 0 < p.natDegree) (hq_monic : q.Monic)
    (hq_irr : Irreducible q) (hdvd : p ∣ q) :
    p = q := by
  have hp_not_unit : ¬ IsUnit p := by
    intro hu
    have h0 := Polynomial.natDegree_eq_zero_of_isUnit hu
    omega
  rcases hdvd with ⟨r, hqr⟩
  have hor := hq_irr.isUnit_or_isUnit hqr
  have hr_unit : IsUnit r := hor.resolve_left hp_not_unit
  have hr_deg : r.natDegree = 0 := Polynomial.natDegree_eq_zero_of_isUnit hr_unit
  have hr_monic : r.Monic := by
    have hlc := Polynomial.leadingCoeff_mul p r
    rw [← hqr, hp.leadingCoeff, one_mul, hq_monic.leadingCoeff] at hlc
    exact hlc.symm
  have hr_one : r = 1 := Polynomial.eq_one_of_monic_natDegree_zero hr_monic hr_deg
  rw [hqr, hr_one, mul_one]

/-- Exact characteristic polynomial of $M_{3,5}$ (`qou-pzsi`):
    `monodromyT35.charpoly` equals the 15th cyclotomic polynomial
    $\Phi_{15}(X) = X^8 - X^7 + X^5 - X^4 + X^3 - X + 1$ of degree $\varphi(15) = 8$,
    satisfying $(X^3 - 1)(X^5 - 1)\,\chi_{M_{3,5}}(X) = (X^{15} - 1)(X - 1)$. -/
theorem monodromyT35_charpoly_eq_cyclotomic_15 :
    monodromyT35.charpoly = Polynomial.cyclotomic 15 ℤ ∧
    monodromyT35.charpoly.natDegree = 8 ∧
    monodromyT35.charpoly =
      Polynomial.X ^ 8 - Polynomial.X ^ 7 + Polynomial.X ^ 5 -
      Polynomial.X ^ 4 + Polynomial.X ^ 3 - Polynomial.X + 1 ∧
    (Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1) * monodromyT35.charpoly =
      (Polynomial.X ^ 15 - 1) * (Polynomial.X - 1) := by
  let p15Z : Polynomial ℤ :=
    Polynomial.X ^ 8 - Polynomial.X ^ 7 + Polynomial.X ^ 5 -
    Polynomial.X ^ 4 + Polynomial.X ^ 3 - Polynomial.X + 1
  have hcyc15_eq : Polynomial.cyclotomic 15 ℤ = p15Z := by
    have hmul : (Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1) * p15Z =
        (Polynomial.X ^ 15 - 1) * (Polynomial.X - 1) := by ring
    have hprod15 : Polynomial.X ^ 15 - (1 : Polynomial ℤ) =
        Polynomial.cyclotomic 1 ℤ * Polynomial.cyclotomic 3 ℤ *
        Polynomial.cyclotomic 5 ℤ * Polynomial.cyclotomic 15 ℤ := by
      have hd := (Polynomial.prod_cyclotomic_eq_X_pow_sub_one (by decide : 0 < 15) ℤ).symm
      have hdiv : Nat.divisors 15 = ({1, 3, 5, 15} : Finset ℕ) := by decide
      rw [hdiv] at hd
      simpa [mul_assoc] using hd
    have hprod3 : Polynomial.X ^ 3 - (1 : Polynomial ℤ) =
        Polynomial.cyclotomic 1 ℤ * Polynomial.cyclotomic 3 ℤ := by
      have hd := (Polynomial.prod_cyclotomic_eq_X_pow_sub_one (by decide : 0 < 3) ℤ).symm
      have hdiv : Nat.divisors 3 = ({1, 3} : Finset ℕ) := by decide
      rw [hdiv] at hd; simpa using hd
    have hprod5 : Polynomial.X ^ 5 - (1 : Polynomial ℤ) =
        Polynomial.cyclotomic 1 ℤ * Polynomial.cyclotomic 5 ℤ := by
      have hd := (Polynomial.prod_cyclotomic_eq_X_pow_sub_one (by decide : 0 < 5) ℤ).symm
      have hdiv : Nat.divisors 5 = ({1, 5} : Finset ℕ) := by decide
      rw [hdiv] at hd; simpa using hd
    have hcyc1 : Polynomial.cyclotomic 1 ℤ = Polynomial.X - 1 := Polynomial.cyclotomic_one ℤ
    have hlhs : (Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1) * Polynomial.cyclotomic 15 ℤ =
        (Polynomial.X ^ 15 - 1) * (Polynomial.X - 1) := by
      rw [hprod15, hprod3, hprod5, hcyc1]; ring
    have hsub : ((Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1)) *
        (Polynomial.cyclotomic 15 ℤ - p15Z) = 0 := by
      calc ((Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1)) * (Polynomial.cyclotomic 15 ℤ - p15Z)
          = (Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1) * Polynomial.cyclotomic 15 ℤ -
            (Polynomial.X ^ 3 - 1) * (Polynomial.X ^ 5 - 1) * p15Z := by ring
        _ = 0 := by rw [hlhs, hmul, sub_self]
    have hmon3 : (Polynomial.X ^ 3 - (1 : Polynomial ℤ)).Monic :=
      Polynomial.monic_X_pow_sub_C 1 (by decide)
    have hmon5 : (Polynomial.X ^ 5 - (1 : Polynomial ℤ)).Monic :=
      Polynomial.monic_X_pow_sub_C 1 (by decide)
    have hne : (Polynomial.X ^ 3 - (1 : Polynomial ℤ)) * (Polynomial.X ^ 5 - 1) ≠ 0 :=
      (hmon3.mul hmon5).ne_zero
    exact sub_eq_zero.mp ((mul_eq_zero.mp hsub).resolve_left hne)
  have hm35_eq : monodromyT35 = m35Val := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm35_p3 : m35Val ^ 3 = m35Pow3 := by
    rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hm35_p5 : m35Val ^ 5 = m35Pow5 := by
    rw [show (5 : ℕ) = 3 + 2 from rfl, pow_add, hm35_p3, sq]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have haeval_Z : Polynomial.aeval monodromyT35 (Polynomial.cyclotomic 15 ℤ) = 0 := by
    rw [hcyc15_eq]
    simp only [p15Z, map_add, map_sub, map_pow, map_one, Polynomial.aeval_X, hm35_eq]
    have hp4 : m35Val ^ 4 = m35Pow3 * m35Val := by rw [pow_succ, hm35_p3]
    have hp7 : m35Val ^ 7 = m35Pow5 * (m35Val * m35Val) := by
      rw [show (7 : ℕ) = 5 + 2 from rfl, pow_add, hm35_p5, sq]
    have hp8 : m35Val ^ 8 = m35Pow5 * m35Pow3 := by
      calc m35Val ^ 8 = m35Val ^ (5 + 3) := rfl
        _ = m35Val ^ 5 * m35Val ^ 3 := pow_add m35Val 5 3
        _ = m35Pow5 * m35Pow3 := by rw [hm35_p5, hm35_p3]
    rw [hp8, hp7, hm35_p5, hp4, hm35_p3]
    ext r c; fin_cases r <;> fin_cases c <;> decide
  let φ : Mat8Z →+* Matrix (Fin 8) (Fin 8) ℚ := (Int.castRingHom ℚ).mapMatrix
  let MQ : Matrix (Fin 8) (Fin 8) ℚ := φ.toIntAlgHom monodromyT35
  have haeval_Q : Polynomial.aeval MQ (Polynomial.cyclotomic 15 ℚ) = 0 := by
    rw [← Polynomial.map_cyclotomic 15 (algebraMap ℤ ℚ), Polynomial.aeval_map_algebraMap ℚ MQ]
    have hcomm : Polynomial.aeval MQ (Polynomial.cyclotomic 15 ℤ) =
        φ.toIntAlgHom (Polynomial.aeval monodromyT35 (Polynomial.cyclotomic 15 ℤ)) :=
      Polynomial.aeval_algHom_apply φ.toIntAlgHom monodromyT35 (Polynomial.cyclotomic 15 ℤ)
    rw [hcomm, haeval_Z, map_zero]
  have hdvd_min : minpoly ℚ MQ ∣ Polynomial.cyclotomic 15 ℚ := minpoly.dvd ℚ MQ haeval_Q
  have hmin_eq : minpoly ℚ MQ = Polynomial.cyclotomic 15 ℚ :=
    monic_eq_of_irreducible_of_dvd
      (minpoly.monic (Matrix.isIntegral MQ))
      (minpoly.natDegree_pos (Matrix.isIntegral MQ))
      (Polynomial.cyclotomic.monic 15 ℚ)
      (Polynomial.cyclotomic.irreducible_rat (by decide))
      hdvd_min
  have hdeg_charQ : MQ.charpoly.natDegree = 8 := by
    rw [Matrix.charpoly_natDegree_eq_dim, Fintype.card_fin]
  have hdeg_15Q : (Polynomial.cyclotomic 15 ℚ).natDegree = 8 := by
    rw [Polynomial.natDegree_cyclotomic]; decide
  have hcharQ : MQ.charpoly = Polynomial.cyclotomic 15 ℚ := by
    symm
    apply monic_eq_of_dvd_of_natDegree_eq (Polynomial.cyclotomic.monic 15 ℚ)
      (Matrix.charpoly_monic MQ)
    · rw [← hmin_eq]; exact Matrix.minpoly_dvd_charpoly MQ
    · rw [hdeg_15Q, hdeg_charQ]
  have hcharZ : monodromyT35.charpoly = Polynomial.cyclotomic 15 ℤ := by
    apply Polynomial.map_injective (Int.castRingHom ℚ) Int.cast_injective
    have hmap_lhs : Polynomial.map (Int.castRingHom ℚ) monodromyT35.charpoly = MQ.charpoly :=
      (Matrix.charpoly_map monodromyT35 (Int.castRingHom ℚ)).symm
    rw [hmap_lhs, hcharQ, Polynomial.map_cyclotomic 15 (Int.castRingHom ℚ)]
  have hdegZ : monodromyT35.charpoly.natDegree = 8 := by
    rw [Matrix.charpoly_natDegree_eq_dim, Fintype.card_fin]
  refine ⟨hcharZ, hdegZ, hcharZ.trans hcyc15_eq, ?_⟩
  rw [hcharZ, hcyc15_eq]
  ring

/-- Universal non-embedding of $T_{2,11}$ monodromy in $\mathrm{Sp}(8, \mathbb{Z})$ (`qou-pzsi`):
    the 22nd cyclotomic polynomial $\Phi_{22}(X)$ has degree $\varphi(22) = 10 > 8$, and no
    $8 \times 8$ integer matrix $M \in M_8(\mathbb{Z})$ (in particular no $M \in \mathrm{Sp}(8, \mathbb{Z})$)
    satisfies $\Phi_{22}(M) = 0$. -/
theorem no_matrix8_int_annihilates_cyclotomic_22 :
    (Polynomial.cyclotomic 22 ℤ).natDegree = 10 ∧
    ∀ M : Mat8Z, Polynomial.aeval M (Polynomial.cyclotomic 22 ℤ) ≠ 0 := by
  refine ⟨by rw [Polynomial.natDegree_cyclotomic]; decide, ?_⟩
  intro M hzero
  let φ : Mat8Z →+* Matrix (Fin 8) (Fin 8) ℚ := (Int.castRingHom ℚ).mapMatrix
  let MQ : Matrix (Fin 8) (Fin 8) ℚ := φ.toIntAlgHom M
  have hzeroQ : Polynomial.aeval MQ (Polynomial.cyclotomic 22 ℚ) = 0 := by
    rw [← Polynomial.map_cyclotomic 22 (algebraMap ℤ ℚ), Polynomial.aeval_map_algebraMap ℚ MQ]
    have hcomm : Polynomial.aeval MQ (Polynomial.cyclotomic 22 ℤ) =
        φ.toIntAlgHom (Polynomial.aeval M (Polynomial.cyclotomic 22 ℤ)) :=
      Polynomial.aeval_algHom_apply φ.toIntAlgHom M (Polynomial.cyclotomic 22 ℤ)
    rw [hcomm, hzero, map_zero]
  have hdvd : minpoly ℚ MQ ∣ Polynomial.cyclotomic 22 ℚ := minpoly.dvd ℚ MQ hzeroQ
  have heq : minpoly ℚ MQ = Polynomial.cyclotomic 22 ℚ :=
    monic_eq_of_irreducible_of_dvd
      (minpoly.monic (Matrix.isIntegral MQ))
      (minpoly.natDegree_pos (Matrix.isIntegral MQ))
      (Polynomial.cyclotomic.monic 22 ℚ)
      (Polynomial.cyclotomic.irreducible_rat (by decide))
      hdvd
  have hdvd_char : minpoly ℚ MQ ∣ MQ.charpoly := Matrix.minpoly_dvd_charpoly MQ
  have hle : (minpoly ℚ MQ).natDegree ≤ MQ.charpoly.natDegree :=
    Polynomial.natDegree_le_of_dvd hdvd_char (Matrix.charpoly_monic MQ).ne_zero
  have hdeg_char : MQ.charpoly.natDegree = 8 := by
    rw [Matrix.charpoly_natDegree_eq_dim, Fintype.card_fin]
  have hdeg_22 : (Polynomial.cyclotomic 22 ℚ).natDegree = 10 := by
    rw [Polynomial.natDegree_cyclotomic]; decide
  rw [heq, hdeg_22, hdeg_char] at hle
  omega

/-- Picard–Lefschetz transvection $T_i$ ($i \in \mathrm{Fin}\,8$) along the $i$-th $A_8$ vanishing
    cycle in the `seifertT29` homology basis, together with its inverse $T_i^{-1}$. -/
def chainTransvection8 (i : Fin 8) : Mat8Z :=
  Matrix.of fun r c => (if r = c then 1 else 0) + (if r = i then intersectionT29 c i else 0)

/-- Inverse Picard–Lefschetz transvection $T_i^{-1}$ in the `seifertT29` homology basis. -/
def chainTransvection8Inv (i : Fin 8) : Mat8Z :=
  Matrix.of fun r c => (if r = c then 1 else 0) - (if r = i then intersectionT29 c i else 0)

/-- Darboux-conjugated symplectic Artin generator $\rho(\sigma_i) \in \mathrm{Sp}(8, \mathbb{Z})$
    acting directly on $(H_1(\Sigma_4; \mathbb{Z}), \Omega_8)$. -/
def darbouxBraidGen8 (i : Fin 8) : Mat8Z :=
  darbouxP29Inv * chainTransvection8 i * darbouxP29

/-- Inverse Darboux-conjugated symplectic Artin generator $\rho(\sigma_i^{-1}) \in \mathrm{Sp}(8, \mathbb{Z})$. -/
def darbouxBraidGen8Inv (i : Fin 8) : Mat8Z :=
  darbouxP29Inv * chainTransvection8Inv i * darbouxP29

/-- Functorial braid-word evaluation $\rho_8 : \mathrm{List}\,(\mathrm{Fin}\,8 \times \mathrm{Bool}) \to \mathrm{Sp}(8, \mathbb{Z})$
    mapping a signed Artin word in $\sigma_0^{\pm 1}, \dots, \sigma_7^{\pm 1}$ (`true` = $+1$,
    `false` = $-1$) to its symplectic automorphism of $H_1(\Sigma_4; \mathbb{Z}) \cong \mathbb{Z}^8$. -/
def evalBraidWordSp8Z (w : List (Fin 8 × Bool)) : Mat8Z :=
  w.foldl (fun acc ltr => acc * (if ltr.2 then darbouxBraidGen8 ltr.1 else darbouxBraidGen8Inv ltr.1)) 1

/-- Functoriality, symplectic invariance, Artin braid relations, and far commutativity
    into $\mathrm{Sp}(8, \mathbb{Z})$ for `evalBraidWordSp8Z` (`qou-pzsi`). -/
theorem braid_to_sp8z_functorial_and_artin_relations :
    (∀ i : Fin 8, IsSymplectic8Z (darbouxBraidGen8 i) ∧ IsSymplectic8Z (darbouxBraidGen8Inv i)) ∧
    (∀ i : Fin 8, darbouxBraidGen8 i * darbouxBraidGen8Inv i = 1 ∧
                  darbouxBraidGen8Inv i * darbouxBraidGen8 i = 1) ∧
    (∀ i : Fin 7,
      darbouxBraidGen8 i.castSucc * darbouxBraidGen8 i.succ * darbouxBraidGen8 i.castSucc =
      darbouxBraidGen8 i.succ * darbouxBraidGen8 i.castSucc * darbouxBraidGen8 i.succ) ∧
    (∀ i j : Fin 8, i.val + 2 ≤ j.val →
      darbouxBraidGen8 i * darbouxBraidGen8 j = darbouxBraidGen8 j * darbouxBraidGen8 i) ∧
    (∀ u v : List (Fin 8 × Bool),
      evalBraidWordSp8Z (u ++ v) = evalBraidWordSp8Z u * evalBraidWordSp8Z v) ∧
    (∀ w : List (Fin 8 × Bool), IsSymplectic8Z (evalBraidWordSp8Z w)) := by
  have hP : darbouxP29 * darbouxP29Inv = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hPL : darbouxP29Inv * darbouxP29 = 1 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hcong : darbouxP29.transpose * intersectionT29 * darbouxP29 = symplecticOmega8 := by
    ext r c; fin_cases r <;> fin_cases c <;> decide
  have hPT : darbouxP29Inv.transpose * darbouxP29.transpose = 1 := by
    rw [← Matrix.transpose_mul, hP, Matrix.transpose_one]
  have hconj_mul : ∀ A B : Mat8Z,
      (darbouxP29Inv * A * darbouxP29) * (darbouxP29Inv * B * darbouxP29) =
      darbouxP29Inv * (A * B) * darbouxP29 := by
    intro A B
    calc (darbouxP29Inv * A * darbouxP29) * (darbouxP29Inv * B * darbouxP29)
        = darbouxP29Inv * A * (darbouxP29 * darbouxP29Inv) * B * darbouxP29 := by
          simp only [Matrix.mul_assoc]
      _ = darbouxP29Inv * (A * B) * darbouxP29 := by
          rw [hP]; simp only [Matrix.mul_one, Matrix.mul_assoc]
  have hconj_symp : ∀ A : Mat8Z,
      A.transpose * intersectionT29 * A = intersectionT29 →
      IsSymplectic8Z (darbouxP29Inv * A * darbouxP29) := by
    intro A hA
    unfold IsSymplectic8Z
    calc (darbouxP29Inv * A * darbouxP29).transpose * symplecticOmega8 *
            (darbouxP29Inv * A * darbouxP29)
        = darbouxP29.transpose * A.transpose *
            (darbouxP29Inv.transpose * darbouxP29.transpose) * intersectionT29 *
            (darbouxP29 * darbouxP29Inv) * A * darbouxP29 := by
          rw [← hcong]; simp only [Matrix.transpose_mul, Matrix.mul_assoc]
      _ = darbouxP29.transpose * (A.transpose * intersectionT29 * A) * darbouxP29 := by
          rw [hPT, hP]; simp only [Matrix.mul_one, Matrix.mul_assoc]
      _ = symplecticOmega8 := by rw [hA, hcong]
  let E : Fin 8 → Mat8Z := fun i =>
    Matrix.of fun r c => if r = i then intersectionT29 c i else 0
  have hT_eq : ∀ i : Fin 8, chainTransvection8 i = 1 + E i := by
    intro i; ext r c; simp [chainTransvection8, E, Matrix.one_apply]
  have hTInv_eq : ∀ i : Fin 8, chainTransvection8Inv i = 1 - E i := by
    intro i; ext r c; simp [chainTransvection8Inv, E, Matrix.one_apply, sub_eq_add_neg]
  have hJ_skew : ∀ a b : Fin 8, intersectionT29 b a = -intersectionT29 a b := by
    intro a b; simp [intersectionT29, Matrix.transpose_apply]
  have hJ_diag : ∀ a : Fin 8, intersectionT29 a a = 0 := by
    intro a; simp [intersectionT29, Matrix.transpose_apply]
  have hE_mul : ∀ i j : Fin 8, intersectionT29 j i = 0 → E i * E j = 0 := by
    intro i j hji
    ext r c
    rw [Matrix.mul_apply, Matrix.zero_apply, Finset.sum_eq_single j]
    · simp [E, hji]
    · intro k _ hkj; simp [E, hkj]
    · intro hj_abs; exact absurd (Finset.mem_univ j) hj_abs
  have hET_J : ∀ i : Fin 8, (E i).transpose * intersectionT29 + intersectionT29 * E i = 0 := by
    intro i
    ext r c
    have h1 : ((E i).transpose * intersectionT29) r c =
        intersectionT29 r i * intersectionT29 i c := by
      rw [Matrix.mul_apply, Finset.sum_eq_single i]
      · simp [E]
      · intro k _ hki; simp [E, hki]
      · intro hi_abs; exact absurd (Finset.mem_univ i) hi_abs
    have h2 : (intersectionT29 * E i) r c =
        intersectionT29 r i * intersectionT29 c i := by
      rw [Matrix.mul_apply, Finset.sum_eq_single i]
      · simp [E]
      · intro k _ hki; simp [E, hki]
      · intro hi_abs; exact absurd (Finset.mem_univ i) hi_abs
    rw [Matrix.add_apply, Matrix.zero_apply, h1, h2, hJ_skew c i]
    ring
  have hET_J_E : ∀ i : Fin 8, (E i).transpose * intersectionT29 * E i = 0 := by
    intro i
    ext r c
    have h1 : ((E i).transpose * intersectionT29 * E i) r c =
        ((E i).transpose * intersectionT29) r i * intersectionT29 c i := by
      rw [Matrix.mul_apply, Finset.sum_eq_single i]
      · simp [E]
      · intro k _ hki; simp [E, hki]
      · intro hi_abs; exact absurd (Finset.mem_univ i) hi_abs
    have h2 : ((E i).transpose * intersectionT29) r i =
        intersectionT29 r i * intersectionT29 i i := by
      rw [Matrix.mul_apply, Finset.sum_eq_single i]
      · simp [E]
      · intro k _ hki; simp [E, hki]
      · intro hi_abs; exact absurd (Finset.mem_univ i) hi_abs
    rw [Matrix.zero_apply, h1, h2, hJ_diag i, mul_zero, zero_mul]
  have hchain_symp : ∀ i : Fin 8,
      (chainTransvection8 i).transpose * intersectionT29 * chainTransvection8 i = intersectionT29 ∧
      (chainTransvection8Inv i).transpose * intersectionT29 * chainTransvection8Inv i =
        intersectionT29 := by
    intro i
    have hsq0 := hET_J_E i
    have hlin := hET_J i
    refine ⟨?_, ?_⟩
    · rw [hT_eq i, Matrix.transpose_add, Matrix.transpose_one]
      calc (1 + (E i).transpose) * intersectionT29 * (1 + E i)
          = intersectionT29 + ((E i).transpose * intersectionT29 + intersectionT29 * E i) +
            (E i).transpose * intersectionT29 * E i := by noncomm_ring
        _ = intersectionT29 := by rw [hlin, hsq0, add_zero, add_zero]
    · rw [hTInv_eq i, Matrix.transpose_sub, Matrix.transpose_one]
      calc (1 - (E i).transpose) * intersectionT29 * (1 - E i)
          = intersectionT29 - ((E i).transpose * intersectionT29 + intersectionT29 * E i) +
            (E i).transpose * intersectionT29 * E i := by noncomm_ring
        _ = intersectionT29 := by rw [hlin, hsq0, sub_zero, add_zero]
  have hchain_inv : ∀ i : Fin 8,
      chainTransvection8 i * chainTransvection8Inv i = 1 ∧
      chainTransvection8Inv i * chainTransvection8 i = 1 := by
    intro i
    have hE2 : E i * E i = 0 := hE_mul i i (hJ_diag i)
    rw [hT_eq i, hTInv_eq i]
    refine ⟨?_, ?_⟩
    · calc (1 + E i) * (1 - E i) = 1 - E i * E i := by noncomm_ring
        _ = 1 := by rw [hE2, sub_zero]
    · calc (1 - E i) * (1 + E i) = 1 - E i * E i := by noncomm_ring
        _ = 1 := by rw [hE2, sub_zero]
  have hchain_artin : ∀ i : Fin 7,
      chainTransvection8 i.castSucc * chainTransvection8 i.succ * chainTransvection8 i.castSucc =
      chainTransvection8 i.succ * chainTransvection8 i.castSucc * chainTransvection8 i.succ := by
    intro i
    -- Note J(i, i+1) = 1 and J(i+1, i) = -1, so E_i * E_{i+1} * E_i = -E_i and E_{i+1} * E_i * E_{i+1} = -E_{i+1}!
    have hJ_adj1 : intersectionT29 i.succ i.castSucc = -1 := by
      simp only [intersectionT29, seifertT29, Matrix.sub_apply, Matrix.transpose_apply,
                 Matrix.of_apply, Fin.val_succ, Fin.coe_castSucc]
      have hne1 : i.succ ≠ i.castSucc := fun h => by
        have hv := congrArg Fin.val h; simp at hv
      have hne2 : i.castSucc ≠ i.succ := hne1.symm
      have hfalse : ¬ (i.val = i.val + 1 + 1) := by omega
      simp [hne1, hne2, hfalse]
    have hJ_adj2 : intersectionT29 i.castSucc i.succ = 1 := by
      rw [hJ_skew i.castSucc i.succ] at hJ_adj1
      linarith
    have hEi2 : E i.castSucc * E i.castSucc = 0 := hE_mul _ _ (hJ_diag _)
    have hEj2 : E i.succ * E i.succ = 0 := hE_mul _ _ (hJ_diag _)
    have hEijEi : E i.castSucc * E i.succ * E i.castSucc = -E i.castSucc := by
      ext r c
      have h1 : (E i.castSucc * E i.succ * E i.castSucc) r c =
          (E i.castSucc * E i.succ) r i.castSucc * intersectionT29 c i.castSucc := by
        rw [Matrix.mul_apply, Finset.sum_eq_single i.castSucc]
        · simp [E]
        · intro k _ hk; simp [E, hk]
        · intro h_abs; exact absurd (Finset.mem_univ _) h_abs
      have h2 : (E i.castSucc * E i.succ) r i.castSucc =
          (if r = i.castSucc then intersectionT29 i.succ i.castSucc else 0) *
          intersectionT29 i.castSucc i.succ := by
        rw [Matrix.mul_apply, Finset.sum_eq_single i.succ]
        · simp [E]
        · intro k _ hk; simp [E, hk]
        · intro h_abs; exact absurd (Finset.mem_univ _) h_abs
      rw [h1, h2, hJ_adj1, hJ_adj2]
      by_cases hr : r = i.castSucc <;> simp [E, hr]
    have hEjiEj : E i.succ * E i.castSucc * E i.succ = -E i.succ := by
      ext r c
      have h1 : (E i.succ * E i.castSucc * E i.succ) r c =
          (E i.succ * E i.castSucc) r i.succ * intersectionT29 c i.succ := by
        rw [Matrix.mul_apply, Finset.sum_eq_single i.succ]
        · simp [E]
        · intro k _ hk; simp [E, hk]
        · intro h_abs; exact absurd (Finset.mem_univ _) h_abs
      have h2 : (E i.succ * E i.castSucc) r i.succ =
          (if r = i.succ then intersectionT29 i.castSucc i.succ else 0) *
          intersectionT29 i.succ i.castSucc := by
        rw [Matrix.mul_apply, Finset.sum_eq_single i.castSucc]
        · simp [E]
        · intro k _ hk; simp [E, hk]
        · intro h_abs; exact absurd (Finset.mem_univ _) h_abs
      rw [h1, h2, hJ_adj1, hJ_adj2]
      by_cases hr : r = i.succ <;> simp [E, hr]
    rw [hT_eq i.castSucc, hT_eq i.succ]
    have hlhs : (1 + E i.castSucc) * (1 + E i.succ) * (1 + E i.castSucc) =
        1 + 2 • E i.castSucc + E i.succ + E i.castSucc * E i.succ + E i.succ * E i.castSucc +
        E i.castSucc * E i.castSucc + E i.castSucc * E i.succ * E i.castSucc := by noncomm_ring
    have hrhs : (1 + E i.succ) * (1 + E i.castSucc) * (1 + E i.succ) =
        1 + E i.castSucc + 2 • E i.succ + E i.castSucc * E i.succ + E i.succ * E i.castSucc +
        E i.succ * E i.succ + E i.succ * E i.castSucc * E i.succ := by noncomm_ring
    rw [hlhs, hrhs, hEi2, hEj2, hEijEi, hEjiEj]
    abel
  have hchain_comm : ∀ i j : Fin 8, i.val + 2 ≤ j.val →
      chainTransvection8 i * chainTransvection8 j =
      chainTransvection8 j * chainTransvection8 i := by
    intro i j hij
    have hJji : intersectionT29 j i = 0 := by
      simp only [intersectionT29, seifertT29, Matrix.sub_apply, Matrix.transpose_apply,
                 Matrix.of_apply]
      have hne1 : j ≠ i := fun h => by subst h; omega
      have hne2 : i ≠ j := hne1.symm
      have h1 : ¬ (j.val = i.val + 1) := by omega
      have h2 : ¬ (i.val = j.val + 1) := by omega
      simp [hne1, hne2, h1, h2]
    have hJij : intersectionT29 i j = 0 := by rw [hJ_skew j i, hJji, neg_zero]
    have hEij : E i * E j = 0 := hE_mul i j hJji
    have hEji : E j * E i = 0 := hE_mul j i hJij
    rw [hT_eq i, hT_eq j]
    calc (1 + E i) * (1 + E j) = 1 + E i + E j + E i * E j := by noncomm_ring
      _ = 1 + E i + E j + E j * E i := by rw [hEij, hEji]
      _ = (1 + E j) * (1 + E i) := by noncomm_ring
  have hsymp : ∀ i : Fin 8,
      IsSymplectic8Z (darbouxBraidGen8 i) ∧ IsSymplectic8Z (darbouxBraidGen8Inv i) := fun i =>
    ⟨hconj_symp _ (hchain_symp i).1, hconj_symp _ (hchain_symp i).2⟩
  have hinv : ∀ i : Fin 8,
      darbouxBraidGen8 i * darbouxBraidGen8Inv i = 1 ∧
      darbouxBraidGen8Inv i * darbouxBraidGen8 i = 1 := by
    intro i
    unfold darbouxBraidGen8 darbouxBraidGen8Inv
    rw [hconj_mul, hconj_mul, (hchain_inv i).1, (hchain_inv i).2, Matrix.mul_one, hPL]
    exact ⟨rfl, rfl⟩
  have hartin : ∀ i : Fin 7,
      darbouxBraidGen8 i.castSucc * darbouxBraidGen8 i.succ * darbouxBraidGen8 i.castSucc =
      darbouxBraidGen8 i.succ * darbouxBraidGen8 i.castSucc * darbouxBraidGen8 i.succ := by
    intro i
    unfold darbouxBraidGen8
    rw [hconj_mul, hconj_mul, hconj_mul, hconj_mul, hchain_artin i]
  have hcomm : ∀ i j : Fin 8, i.val + 2 ≤ j.val →
      darbouxBraidGen8 i * darbouxBraidGen8 j = darbouxBraidGen8 j * darbouxBraidGen8 i := by
    intro i j hij
    unfold darbouxBraidGen8
    rw [hconj_mul, hconj_mul, hchain_comm i j hij]
  have hfold : ∀ (v : List (Fin 8 × Bool)) (M : Mat8Z),
      v.foldl (fun acc ltr => acc * (if ltr.2 then darbouxBraidGen8 ltr.1 else darbouxBraidGen8Inv ltr.1)) M =
      M * evalBraidWordSp8Z v := by
    intro v
    induction v with
    | nil =>
      intro M; simp [evalBraidWordSp8Z]
    | cons ltr tl ih =>
      intro M
      simp only [List.foldl_cons, evalBraidWordSp8Z]
      rw [ih (M * _), ih (1 * _), one_mul, Matrix.mul_assoc]
  have happ : ∀ u v : List (Fin 8 × Bool),
      evalBraidWordSp8Z (u ++ v) = evalBraidWordSp8Z u * evalBraidWordSp8Z v := by
    intro u v
    unfold evalBraidWordSp8Z
    rw [List.foldl_append]
    exact hfold v _
  have hword_symp : ∀ w : List (Fin 8 × Bool), IsSymplectic8Z (evalBraidWordSp8Z w) := by
    intro w
    induction w with
    | nil =>
      unfold evalBraidWordSp8Z IsSymplectic8Z
      simp
    | cons ltr tl ih =>
      have hcons : evalBraidWordSp8Z (ltr :: tl) =
          evalBraidWordSp8Z [ltr] * evalBraidWordSp8Z tl := happ [ltr] tl
      rw [hcons]
      have hltr : IsSymplectic8Z (evalBraidWordSp8Z [ltr]) := by
        simp only [evalBraidWordSp8Z, List.foldl_cons, List.foldl_nil, one_mul]
        by_cases hb : ltr.2
        · simp only [hb, ↓reduceIte]; exact (hsymp ltr.1).1
        · simp only [hb]; exact (hsymp ltr.1).2
      unfold IsSymplectic8Z at hltr ih ⊢
      rw [Matrix.transpose_mul]
      calc (evalBraidWordSp8Z tl).transpose * (evalBraidWordSp8Z [ltr]).transpose *
            symplecticOmega8 * (evalBraidWordSp8Z [ltr] * evalBraidWordSp8Z tl)
          = (evalBraidWordSp8Z tl).transpose *
            ((evalBraidWordSp8Z [ltr]).transpose * symplecticOmega8 * evalBraidWordSp8Z [ltr]) *
            evalBraidWordSp8Z tl := by simp only [Matrix.mul_assoc]
        _ = (evalBraidWordSp8Z tl).transpose * symplecticOmega8 * evalBraidWordSp8Z tl := by
            rw [hltr]
        _ = symplecticOmega8 := ih
  exact ⟨hsymp, hinv, hartin, hcomm, happ, hword_symp⟩

-- ============================================================================
-- §3. Algebraic & Orbit Obstructions on Bring → Genus-3 Degeneration (`qou-8pl1`)
-- ============================================================================

/-- Elementary symmetric cubic $e_3(x_0, \dots, x_4) = \sum_{0 \le i < j < k \le 4} x_i x_j x_k$,
    paired with Newton power sums $p_1, p_2, p_3$ to show $S_5$-complete-intersection rigidity:
    $2(p_3 - 3 e_3) = p_1(3 p_2 - p_1^2)$ and $p_3 - 3 e_3 = p_1(p_1^2 - 3 e_2)$, so on
    $\{p_1 = 0\}$, $p_3 - \tau e_3 = (3 - \tau) e_3$ over any commutative ring. -/
theorem bring_cubic_pencil_s5_rigidity {K : Type*} [CommRing K]
    (x0 x1 x2 x3 x4 τ : K) :
    let p1 := x0 + x1 + x2 + x3 + x4
    let p2 := x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2
    let p3 := x0 ^ 3 + x1 ^ 3 + x2 ^ 3 + x3 ^ 3 + x4 ^ 3
    let e3 := x0 * x1 * x2 + x0 * x1 * x3 + x0 * x1 * x4 + x0 * x2 * x3 + x0 * x2 * x4 +
              x0 * x3 * x4 + x1 * x2 * x3 + x1 * x2 * x4 + x1 * x3 * x4 + x2 * x3 * x4
    2 * (p3 - 3 * e3) = p1 * (3 * p2 - p1 ^ 2) ∧
    (p1 = 0 → p3 - τ * e3 = (3 - τ) * e3) := by
  intro p1 p2 p3 e3
  refine ⟨by ring, ?_⟩
  intro hp1
  have hp3 : p3 = 3 * e3 + p1 * (p1 ^ 2 - 3 * (x0 * x1 + x0 * x2 + x0 * x3 + x0 * x4 +
      x1 * x2 + x1 * x3 + x1 * x4 + x2 * x3 + x2 * x4 + x3 * x4)) := by
    dsimp [p1, p3, e3]; ring
  rw [hp3, hp1, zero_mul, add_zero]
  ring

/-- Minimum $S_5$-orbit size under cyclic point stabilizers (`qou-8pl1`):
    for any action of $S_5 = \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,5)$ on a type $X$ whose point
    stabilizers are cyclic, every $S_5$-orbit has cardinality $\ge 20$; when stabilizer orders
    lie in $\{1, 2, 4, 5\}$ (the $(2, 4, 5)$ branch orders on $\Sigma_4$), every orbit has
    cardinality in $\{24, 30, 60, 120\}$ ($\ge 24$), ruling out a single $S_5$-fixed node ($k = 1$). -/
theorem s5_cyclic_stabilizer_orbit_lower_bounds (X : Type*)
    [MulAction (Equiv.Perm (Fin 5)) X] :
    (∀ x : X, [Fintype (MulAction.orbit (Equiv.Perm (Fin 5)) x)] →
      [Fintype (MulAction.stabilizer (Equiv.Perm (Fin 5)) x)] →
      IsCyclic (MulAction.stabilizer (Equiv.Perm (Fin 5)) x) →
      20 ≤ Fintype.card (MulAction.orbit (Equiv.Perm (Fin 5)) x)) ∧
    (∀ x : X, [Fintype (MulAction.orbit (Equiv.Perm (Fin 5)) x)] →
      [Fintype (MulAction.stabilizer (Equiv.Perm (Fin 5)) x)] →
      Fintype.card (MulAction.stabilizer (Equiv.Perm (Fin 5)) x) ∈ ({1, 2, 4, 5} : Finset ℕ) →
      Fintype.card (MulAction.orbit (Equiv.Perm (Fin 5)) x) ∈ ({24, 30, 60, 120} : Finset ℕ) ∧
      24 ≤ Fintype.card (MulAction.orbit (Equiv.Perm (Fin 5)) x)) := by
  have hcardS5 : Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
    rw [Fintype.card_perm, Fintype.card_fin]; decide
  refine ⟨?_, ?_⟩
  · intro x _ _ hcyc
    have hos := MulAction.card_orbit_mul_card_stabilizer_eq_card_group (Equiv.Perm (Fin 5)) x
    rw [hcardS5] at hos
    have hmem := (cyclic_subgroup_perm5_card_mem
      (MulAction.stabilizer (Equiv.Perm (Fin 5)) x) hcyc).1
    simp only [Finset.mem_insert, Finset.mem_singleton] at hmem
    rcases hmem with h | h | h | h | h | h <;> (rw [h] at hos; omega)
  · intro x _ _ hmem
    have hos := MulAction.card_orbit_mul_card_stabilizer_eq_card_group (Equiv.Perm (Fin 5)) x
    rw [hcardS5] at hos
    simp only [Finset.mem_insert, Finset.mem_singleton] at hmem ⊢
    rcases hmem with h | h | h | h <;> (rw [h] at hos; omega)

/-- Unconditional cellular Riemann–Hurwitz exclusion of genus $g = 3$ ($\chi = 2 - 2(3) = -4$)
    for $S_5 = \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,5)$ with cyclic vertex stabilizers (`qou-8pl1`):
    combining §1.1 (`cyclic_subgroup_perm5_card_mem`) and §1.2
    (`equivariant_cell_riemann_hurwitz_orbit_deficit`), no `EquivariantCellComplex` of
    `Equiv.Perm (Fin 5)` with cyclic vertex stabilizers can have upstairs Euler characteristic
    $-4$ over any quotient genus $h \in \mathbb{N}$. -/
theorem no_s5_cellular_surface_of_genus_three
    (C : EquivariantCellComplex (Equiv.Perm (Fin 5)))
    (hcyc : ∀ v : C.V, IsCyclic (MulAction.stabilizer (Equiv.Perm (Fin 5)) v))
    (h : ℕ) (hquot : C.quotientEuler = 2 - 2 * (h : ℤ)) :
    C.upstairsEuler ≠ 2 - 2 * (3 : ℤ) := by
  classical
  intro hup
  have hcardS5 : Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
    rw [Fintype.card_perm, Fintype.card_fin]; decide
  have hrh := equivariant_cell_riemann_hurwitz_orbit_deficit C
  rw [hup, hquot, hcardS5] at hrh
  let D : Quotient (MulAction.orbitRel (Equiv.Perm (Fin 5)) C.V) → ℤ :=
    fun o => (120 : ℤ) - (orbitFiberCard (G := Equiv.Perm (Fin 5)) C.V o : ℤ)
  have horb_def : ∀ o : Quotient (MulAction.orbitRel (Equiv.Perm (Fin 5)) C.V),
      D o = 0 ∨ D o = 60 ∨ D o = 80 ∨ D o = 90 ∨ D o = 96 ∨ D o = 100 := by
    intro o
    obtain ⟨v, rfl⟩ := Quotient.exists_rep o
    have hos := orbitFiberCard_mul_stabilizer_eq_card_group (G := Equiv.Perm (Fin 5)) C.V v
    rw [hcardS5] at hos
    have hmem := (cyclic_subgroup_perm5_card_mem
      (MulAction.stabilizer (Equiv.Perm (Fin 5)) v) (hcyc v)).1
    simp only [Finset.mem_insert, Finset.mem_singleton] at hmem
    dsimp only [D]
    rcases hmem with hs | hs | hs | hs | hs | hs <;> (rw [hs] at hos; omega)
  have hsum_eq : (∑ o, D o) = 244 - 240 * (h : ℤ) := by
    change (2 - 2 * (3 : ℤ)) = (120 : ℤ) * (2 - 2 * (h : ℤ)) - ∑ o, D o at hrh
    linarith
  have hnonneg : ∀ o, 0 ≤ D o := by
    intro o
    rcases horb_def o with h0 | h0 | h0 | h0 | h0 | h0 <;> omega
  have hsum_nonneg : 0 ≤ ∑ o, D o := Finset.sum_nonneg (fun o _ => hnonneg o)
  have hh_cases : h = 0 ∨ h = 1 := by omega
  rcases hh_cases with rfl | rfl
  · have hbound_mod5 : ∀ o, 96 * (D o % 5) ≤ D o := by
      intro o
      rcases horb_def o with h0 | h0 | h0 | h0 | h0 | h0 <;> omega
    have hsum_mod5_le : 96 * (∑ o, (D o % 5)) ≤ ∑ o, D o := by
      rw [Finset.mul_sum]
      exact Finset.sum_le_sum (fun o _ => hbound_mod5 o)
    have hmod_nonneg : ∀ o, 0 ≤ D o % 5 := fun o => Int.emod_nonneg _ (by decide)
    have hmod_cong : (∑ o, D o) % 5 = (∑ o, (D o % 5)) % 5 := by
      induction (Finset.univ : Finset (Quotient (MulAction.orbitRel (Equiv.Perm (Fin 5)) C.V)))
        using Finset.induction_on with
      | empty => simp
      | @insert a s ha ih =>
        rw [Finset.sum_insert ha, Finset.sum_insert ha, Int.add_emod, ih]
        omega
    have hsum_244 : (∑ o, D o) = 244 := by simpa using hsum_eq
    rw [hsum_244] at hmod_cong hsum_mod5_le
    have hsum_rem_nonneg : 0 ≤ ∑ o, (D o % 5) := Finset.sum_nonneg (fun o _ => hmod_nonneg o)
    omega
  · have hsum_4 : (∑ o, D o) = 4 := by simpa using hsum_eq
    have hall_zero : ∀ o, D o = 0 := by
      intro o
      by_contra hne
      have hge60 : 60 ≤ D o := by
        rcases horb_def o with h0 | h0 | h0 | h0 | h0 | h0 <;> omega
      have hle_sum : D o ≤ ∑ x, D x :=
        Finset.single_le_sum (fun x _ => hnonneg x) (Finset.mem_univ o)
      omega
    have hsum_0 : (∑ o, D o) = 0 := Finset.sum_eq_zero (fun o _ => hall_zero o)
    omega

/-- Absence of $S_4$-fixed points on the canonical quadric $\{p_1 = 0, p_2 = 0\}$ (`qou-8pl1`):
    over any characteristic-zero field $K$, if $x_0 = x_1 = x_2 = x_3$ and
    $p_1(x) = p_2(x) = 0$, then $x_0 = x_1 = x_2 = x_3 = x_4 = 0$. -/
theorem s4_no_fixed_point_on_bring_quadric {K : Type*} [Field K] [CharZero K]
    (x0 x1 x2 x3 x4 : K)
    (h01 : x1 = x0) (h02 : x2 = x0) (h03 : x3 = x0)
    (hp1 : x0 + x1 + x2 + x3 + x4 = 0)
    (hp2 : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 = 0) :
    x0 = 0 ∧ x1 = 0 ∧ x2 = 0 ∧ x3 = 0 ∧ x4 = 0 := by
  have hx4 : x4 = -(4 : K) * x0 := by
    rw [h01, h02, h03] at hp1; linear_combination hp1
  have h20 : (20 : K) * x0 ^ 2 = 0 := by
    rw [h01, h02, h03, hx4] at hp2; linear_combination hp2
  have h20_ne : (20 : K) ≠ 0 := by exact_mod_cast (by decide : (20 : ℕ) ≠ 0)
  have hx0_sq : x0 ^ 2 = 0 := (mul_eq_zero.mp h20).resolve_left h20_ne
  have hx0 : x0 = 0 := pow_eq_zero hx0_sq
  exact ⟨hx0, h01.trans hx0, h02.trans hx0, h03.trans hx0, by rw [hx4, hx0, mul_zero]⟩

/-- Group action modeling the $(2, 3, 7)$ Hurwitz automorphism geometry of Klein's genus-3
    quartic: a group $G$ of order $168$ acting on $X$ with all point-stabilizer orders in
    $\{1, 2, 3, 7\}$. -/
structure Hurwitz237Action (G X : Type*) [Group G] [Fintype G] [MulAction G X] where
  card_G : Fintype.card G = 168
  stabilizer_orders : ∀ x : X, [Fintype (MulAction.stabilizer G x)] →
    Fintype.card (MulAction.stabilizer G x) ∈ ({1, 2, 3, 7} : Finset ℕ)

/-- Explicit finite inhabitant of `Hurwitz237Action` on the group
    $G = \mathrm{Equiv.Perm}\,(\mathrm{Fin}\,4) \times \mathrm{Multiplicative}\,(\mathrm{ZMod}\,7)$
    of order $24 \times 7 = 168$ acting regularly on itself by left multiplication. -/
def regularHurwitz237Inhabitant :
    @Hurwitz237Action (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7))
      (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7)) _ _
      { smul := (· * ·), one_smul := one_mul, mul_smul := mul_assoc } where
  card_G := by
    rw [Fintype.card_prod, Fintype.card_perm, Fintype.card_fin,
        Fintype.card_multiplicative, ZMod.card]
    decide
  stabilizer_orders x _ := by
    letI : MulAction (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7))
        (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7)) :=
      { smul := (· * ·), one_smul := one_mul, mul_smul := mul_assoc }
    have huniq : Unique (MulAction.stabilizer
        (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7)) x) :=
      { default := ⟨1, one_mul x⟩
        uniq := fun s => Subtype.ext (mul_eq_right.mp s.2) }
    have hs1 : Fintype.card (MulAction.stabilizer
        (Equiv.Perm (Fin 4) × Multiplicative (ZMod 7)) x) = 1 :=
      @Fintype.card_unique _ huniq _
    rw [hs1]
    decide

section KleinMarkedPairObstruction
open Classical

/-- Klein quartic $S_4$-orbit lower bound and marked-pair obstruction (`qou-8pl1` / `qou-8p1b`):
    for any `Hurwitz237Action G X` ($|G| = 168$, point stabilizers of order in $\{1, 2, 3, 7\}$)
    and any subgroup $H \le G$ of order $24$ ($H \cong S_4$), every $H$-orbit on $X$ has
    cardinality in $\{8, 12, 24\}$ ($\ge 8 > 2$). Consequently, no nonempty subset $M \subseteq X$
    of cardinality $|M| \le 2$ (such as the two preimage points $\{p_+, p_-\}$ of a single
    pinched node) can be preserved setwise by $H$. -/
theorem klein_hurwitz237_s4_orbit_ge_eight_excludes_marked_pair
    {G X : Type*} [Group G] [Fintype G] [Fintype X] [MulAction G X]
    (K : Hurwitz237Action G X) (H : Subgroup G) [Fintype H] (hcardH : Fintype.card H = 24) :
    (∀ x : X,
      Fintype.card (MulAction.orbit H x) ∈ ({8, 12, 24} : Finset ℕ) ∧
      8 ≤ Fintype.card (MulAction.orbit H x)) ∧
    (∀ M : Finset X, M.Nonempty → M.card ≤ 2 →
      ¬ (∀ h : H, ∀ x ∈ M, (h : G) • x ∈ M)) := by
  have horbit : ∀ x : X,
      Fintype.card (MulAction.orbit H x) ∈ ({8, 12, 24} : Finset ℕ) ∧
      8 ≤ Fintype.card (MulAction.orbit H x) := by
    intro x
    let ι : MulAction.stabilizer H x →* MulAction.stabilizer G x :=
      { toFun := fun s => ⟨(s.1 : G), s.2⟩
        map_one' := rfl
        map_mul' := fun _ _ => rfl }
    have hι_inj : Function.Injective ι := by
      intro a b hab
      have hval : (a.1 : G) = (b.1 : G) :=
        congrArg (fun z : MulAction.stabilizer G x => z.1) hab
      exact Subtype.ext (Subtype.ext hval)
    have hdvd_nat : Nat.card (MulAction.stabilizer H x) ∣
        Nat.card (MulAction.stabilizer G x) :=
      Subgroup.card_dvd_of_injective ι hι_inj
    rw [Nat.card_eq_fintype_card, Nat.card_eq_fintype_card] at hdvd_nat
    have hmemG := K.stabilizer_orders x
    have hosH := MulAction.card_orbit_mul_card_stabilizer_eq_card_group H x
    have hs_pos : 0 < Fintype.card (MulAction.stabilizer H x) := Fintype.card_pos
    rw [hcardH] at hosH
    simp only [Finset.mem_insert, Finset.mem_singleton] at hmemG ⊢
    rcases hmemG with hs | hs | hs | hs
    · rw [hs] at hdvd_nat
      have h1 : Fintype.card (MulAction.stabilizer H x) = 1 := Nat.eq_one_of_dvd_one hdvd_nat
      rw [h1] at hosH; omega
    · rw [hs] at hdvd_nat
      have hle : Fintype.card (MulAction.stabilizer H x) ≤ 2 :=
        Nat.le_of_dvd (by decide) hdvd_nat
      have hcases : Fintype.card (MulAction.stabilizer H x) = 1 ∨
          Fintype.card (MulAction.stabilizer H x) = 2 := by omega
      rcases hcases with hc | hc <;> (rw [hc] at hosH; omega)
    · rw [hs] at hdvd_nat
      have hle : Fintype.card (MulAction.stabilizer H x) ≤ 3 :=
        Nat.le_of_dvd (by decide) hdvd_nat
      rcases hdvd_nat with ⟨k, hk⟩
      have hcases : Fintype.card (MulAction.stabilizer H x) = 1 ∨
          Fintype.card (MulAction.stabilizer H x) = 2 ∨
          Fintype.card (MulAction.stabilizer H x) = 3 := by omega
      rcases hcases with hc | hc | hc <;> (rw [hc] at hosH hk; omega)
    · rw [hs] at hdvd_nat
      have hle : Fintype.card (MulAction.stabilizer H x) ≤ 7 :=
        Nat.le_of_dvd (by decide) hdvd_nat
      rcases hdvd_nat with ⟨k, hk⟩
      have hcases : Fintype.card (MulAction.stabilizer H x) = 1 ∨
          Fintype.card (MulAction.stabilizer H x) = 2 ∨
          Fintype.card (MulAction.stabilizer H x) = 3 ∨
          Fintype.card (MulAction.stabilizer H x) = 4 ∨
          Fintype.card (MulAction.stabilizer H x) = 5 ∨
          Fintype.card (MulAction.stabilizer H x) = 6 ∨
          Fintype.card (MulAction.stabilizer H x) = 7 := by omega
      rcases hcases with hc | hc | hc | hc | hc | hc | hc <;> (rw [hc] at hosH hk; omega)
  refine ⟨horbit, ?_⟩
  intro M ⟨x₀, hx₀⟩ hM_le hinv
  have hge8 : 8 ≤ Fintype.card (MulAction.orbit H x₀) := (horbit x₀).2
  have hsub : (Finset.univ.map ⟨(Subtype.val : MulAction.orbit H x₀ → X),
      Subtype.val_injective⟩ : Finset X) ⊆ M := by
    intro y hy
    simp only [Finset.mem_map, Finset.mem_univ, Function.Embedding.coeFn_mk, true_and] at hy
    rcases hy with ⟨⟨y', ⟨h, rfl⟩⟩, rfl⟩
    exact hinv h x₀ hx₀
  have hcard_le : Fintype.card (MulAction.orbit H x₀) ≤ M.card := by
    have hmap_card : (Finset.univ.map ⟨(Subtype.val : MulAction.orbit H x₀ → X),
        Subtype.val_injective⟩).card = Fintype.card (MulAction.orbit H x₀) := by
      rw [Finset.card_map, Finset.card_univ]
    rw [← hmap_card]
    exact Finset.card_le_card hsub
  omega

end KleinMarkedPairObstruction

end QOU.Brings.BraidCurveHomologyAndEquivariantHurwitz
