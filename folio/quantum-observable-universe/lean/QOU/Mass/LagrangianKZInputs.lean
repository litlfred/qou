import QOU.Mass.LagrangianKZIdentification

/-!
# Bridge A, step A2 — deriving the inputs left open in `LagrangianKZIdentification`

Audit `docs/audits/2026-11-15-bridge-a2-lagrangian-kz.md`, §"What is left as genuine new input".
That note left three inputs between the corpus and the KZ connection:

1. Reeb invariance of `∇`, `L_ξ ∇ = 0`;
2. regular residues at triple collisions, for `n ≥ 4`;
3. permutation symmetry of the `n`-body sector.

## Part I — permutation symmetry is the descent to unordered configurations (input 3)

P1 of the audit note makes the braiding of `C` a local system on the **unordered** configuration
space `Conf_n / S_n`, because `B_n = π₁(Conf_n / S_n)`. Pulled back to `Conf_n`, with tensor
factor `k` sitting at point `z_k`, that descent datum is: relabelling the points by `σ` acts on the
fibre `V^{⊗n}` by the strand permutation `P_σ`. For the connection form this is the equivariance

  `ω(σ·z)(σ·u) = P_σ ω(z)(u) P_σ⁻¹`,   `(σ·z)_{σ a} = z_a`.

Nothing else is assumed. We prove:

* `arnoldForm_relabel`: relabelling the points of an Arnold-class form relabels its residues.
* `residue_covariant`: equivariance forces `M_{σa,σb} = P_σ M_{ab} P_σ⁻¹` for every `a ≠ b`.
* `swap_covariant`: the transposition residues `P_{(ij)}` are themselves covariant.
* `residue_uniform`: if **one** pair residue is `α + β P_{(i₀ j₀)}` (this is what `schurWeyl_two`
  gives for one pair), then **every** pair residue is `α + β P_{(ij)}` with the same `α, β`.
* `arnoldForm_eq_abelian_add_kz`: so the whole form is `α·(abelian form) + KZ(ℏ = β, Ω = P)`.

So input 3 is not a new physical assumption. It is the statement that the `n`-body sector is built
from the braiding of `C`, which P1 already uses. The only convention is the labelling "factor `k`
at point `z_k`".

## Part II — Reeb and translation invariance are a gauge choice (input 1)

`affineNormalize z k = (z_k − z_0)/(z_1 − z_0)` is invariant under every dilation and translation
(`affineNormalize_affine`). A function is invariant under both iff it factors through
`affineNormalize` (`affineInvariant_iff`). This is the algebraic half of the product decomposition
`Conf_n ≅ ℂ × ℂ^× × M_{0,n+1}`, `z ↦ (z_0, z_1 − z_0, affineNormalize z)`.

The decomposition is what turns input 1 from an axiom into a gauge choice. The translation factor
`ℂ` is contractible. The Euler loop on the `ℂ^×` factor is the full twist `Δ²`, which is central in
`B_n`. So a local system on `Conf_n` is the pull-back of one on `M_{0,n+1}` together with one central
automorphism, and a connection `ω_M + B·dt/t` (`ω_M` pulled back from `M_{0,n+1}`, `B` a parallel
logarithm of the twist) represents it. That representative is dilation and translation
invariant. The written argument is in the audit note; the Lean here is the invariance lemma.

What is **not** shown: that this representative still has logarithmic poles along all diagonals
(Saito's condition (a) of the audit note). `B` is a parallel section of a regular-singular
connection, so it has moderate growth, but its pole order along the boundary of `M_{0,n+1}` is not
controlled here.

## Part III — triple collisions (input 2)

Only the rank-one case is settled, in the written note (closed logarithmic 1-forms on the braid
arrangement, Brieskorn). The matrix case for `n ≥ 4` stays open. Nothing in this file is about it.

Base ring §7c: any field (Part II), any infinite field (Part I).

-- Ref: [arnold1969] Arnold, The cohomology ring of the colored braid group, Mat. Zametki 5.
-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987), §1.1.
-- Ref: [deligne1970] Deligne, Équations différentielles à points singuliers réguliers, LNM 163.
-/

namespace QOU.Mass.LagrangianKZ

open Equiv

section Permutation

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- **Relabelling.** Moving the point labelled `a` to label `σ a` (`(σ·z)_{σ a} = z_a`) turns the
Arnold-class form with residues `M` into the one with residues `M_{σa,σb}`. -/
theorem arnoldForm_relabel (σ : Perm (Fin n)) (M : Fin n → Fin n → A) (z u : Fin n → K) :
    arnoldForm M (z ∘ σ.symm) (u ∘ σ.symm) = arnoldForm (fun a b => M (σ a) (σ b)) z u := by
  unfold arnoldForm arnoldCoeff
  rw [← Equiv.sum_comp σ]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [← Equiv.sum_comp σ]
  simp only [Function.comp_apply, Equiv.symm_apply_apply]

/-- **Equivariance forces covariant residues.** If relabelling the points by `σ` acts on the form
by conjugation with `g σ`, then `M_{σa,σb} = g_σ M_{ab} g_σ⁻¹` for every `a ≠ b`. -/
theorem residue_covariant [Infinite K] (g : Perm (Fin n) →* Aˣ) (M : Fin n → Fin n → A)
    (heq : ∀ σ : Perm (Fin n), ∀ z : Fin n → K, Function.Injective z → ∀ u,
      arnoldForm M (z ∘ σ.symm) (u ∘ σ.symm) = (g σ : A) * arnoldForm M z u * ↑(g σ)⁻¹)
    (σ : Perm (Fin n)) : ∀ a b, a ≠ b → M (σ a) (σ b) = (g σ : A) * M a b * ↑(g σ)⁻¹ := by
  have h := (const_gauge_iff (K := K) (g σ) M (fun a b => M (σ a) (σ b))).mp
    (fun z hz u => by rw [← heq σ z hz u, arnoldForm_relabel])
  exact h

/-- The strand-transposition residues are covariant: `g_σ P_{(ij)} g_σ⁻¹ = P_{(σi σj)}`. -/
theorem swap_covariant (g : Perm (Fin n) →* Aˣ) (σ : Perm (Fin n)) (i j : Fin n) :
    (g σ : A) * (g (swap i j) : A) * ↑(g σ)⁻¹ = (g (swap (σ i) (σ j)) : A) := by
  rw [swap_apply_apply, map_mul, map_mul, map_inv]
  simp [Units.val_mul, mul_assoc]

/-- A permutation sending a given ordered pair of distinct labels to another. -/
theorem exists_perm_pair {i₀ j₀ i j : Fin n} (h₀ : i₀ ≠ j₀) (h : i ≠ j) :
    ∃ σ : Perm (Fin n), σ i₀ = i ∧ σ j₀ = j := by
  refine ⟨swap (swap i₀ i j₀) j * swap i₀ i, ?_, ?_⟩
  · have hne : i ≠ swap i₀ i j₀ := by
      intro he
      have : swap i₀ i i = swap i₀ i (swap i₀ i j₀) := congrArg (swap i₀ i) he
      rw [swap_apply_right, swap_apply_self] at this
      exact h₀ this
    simp only [Perm.coe_mul, Function.comp_apply, swap_apply_left]
    exact swap_apply_of_ne_of_ne hne h
  · simp [Perm.coe_mul, Function.comp_apply, swap_apply_left]

/-- **One pair fixes all pairs.** With covariant residues, if one pair residue is
`α + β P_{(i₀ j₀)}`, then every pair residue is `α + β P_{(ij)}` with the same `α, β`. -/
theorem residue_uniform (g : Perm (Fin n) →* Aˣ) (M : Fin n → Fin n → A)
    (hcov : ∀ σ : Perm (Fin n), ∀ a b, a ≠ b → M (σ a) (σ b) = (g σ : A) * M a b * ↑(g σ)⁻¹)
    {i₀ j₀ : Fin n} (h₀ : i₀ ≠ j₀) (α β : K)
    (hpair : M i₀ j₀ = α • (1 : A) + β • (g (swap i₀ j₀) : A)) :
    ∀ i j, i ≠ j → M i j = α • (1 : A) + β • (g (swap i j) : A) := by
  intro i j hij
  obtain ⟨σ, hi, hj⟩ := exists_perm_pair h₀ hij
  have := hcov σ i₀ j₀ h₀
  rw [hi, hj, hpair] at this
  rw [this, mul_add, add_mul, mul_smul_comm, smul_mul_assoc, mul_smul_comm, smul_mul_assoc,
    swap_covariant, ← hi, ← hj, mul_one, Units.mul_inv]

/-- **The form, assembled.** Equivariance plus one Schur–Weyl pair residue writes the whole
Arnold-class form as an abelian part plus the KZ form with `ℏ = β` and `Ω_{ij} = P_{(ij)}`. -/
theorem arnoldForm_eq_abelian_add_kz [Infinite K] (g : Perm (Fin n) →* Aˣ)
    (M : Fin n → Fin n → A)
    (heq : ∀ σ : Perm (Fin n), ∀ z : Fin n → K, Function.Injective z → ∀ u,
      arnoldForm M (z ∘ σ.symm) (u ∘ σ.symm) = (g σ : A) * arnoldForm M z u * ↑(g σ)⁻¹)
    {i₀ j₀ : Fin n} (h₀ : i₀ ≠ j₀) (α β : K)
    (hpair : M i₀ j₀ = α • (1 : A) + β • (g (swap i₀ j₀) : A)) (z u : Fin n → K) :
    arnoldForm M z u =
      α • arnoldForm (fun _ _ => (1 : A)) z u + kzForm β (fun i j => (g (swap i j) : A)) z u := by
  rw [← arnoldForm_split]
  exact arnoldForm_congr_offDiag
    (residue_uniform g M (residue_covariant g M heq) h₀ α β hpair) z u

end Permutation

section Affine

variable {K : Type*} [Field K] {n : ℕ}

/-- Affine normal form of a configuration: move `z_0` to `0` and `z_1` to `1`. -/
def affineNormalize (z : Fin (n + 2) → K) (k : Fin (n + 2)) : K :=
  (z k - z 0) / (z 1 - z 0)

/-- The normal form is invariant under every dilation `c ≠ 0` and every translation `b`. -/
theorem affineNormalize_affine (z : Fin (n + 2) → K) {c : K} (hc : c ≠ 0) (b : K) :
    affineNormalize (fun k => c * z k + b) = affineNormalize z := by
  funext k
  unfold affineNormalize
  have h1 : c * z k + b - (c * z 0 + b) = c * (z k - z 0) := by ring
  have h2 : c * z 1 + b - (c * z 0 + b) = c * (z 1 - z 0) := by ring
  rw [h1, h2, mul_div_mul_left _ _ hc]

/-- On configurations with `z_0 ≠ z_1`, the normal form is reached by an affine map. -/
theorem affineNormalize_eq_affine (z : Fin (n + 2) → K) (_h : z 1 ≠ z 0) :
    affineNormalize z = fun k => (z 1 - z 0)⁻¹ * z k + (-(z 1 - z 0)⁻¹ * z 0) := by
  funext k
  unfold affineNormalize
  rw [div_eq_inv_mul]
  ring

/-- **Invariance is factoring through the normal form.** A function on configurations with
`z_0 ≠ z_1` is invariant under all dilations and translations iff it only depends on
`affineNormalize z`. -/
theorem affineInvariant_iff {X : Type*} (f : (Fin (n + 2) → K) → X) :
    (∀ z : Fin (n + 2) → K, z 1 ≠ z 0 → ∀ c : K, c ≠ 0 → ∀ b : K,
        f (fun k => c * z k + b) = f z) ↔
      ∀ z : Fin (n + 2) → K, z 1 ≠ z 0 → f z = f (affineNormalize z) := by
  constructor
  · intro h z hz
    rw [affineNormalize_eq_affine z hz]
    exact (h z hz _ (inv_ne_zero (sub_ne_zero.mpr hz)) _).symm
  · intro h z hz c hc b
    have hz' : c * z 1 + b ≠ c * z 0 + b := by
      intro he; exact hz (mul_left_cancel₀ hc (add_right_cancel he))
    rw [h _ hz', h z hz, affineNormalize_affine z hc b]

end Affine

/-! ## Part IV — a colliding cluster acts as one object (input 2, the monoidal side)

Let a cluster `S` of points collide: `z_p = c + ε w_p` for `p ∈ S`, the other points fixed, and
move along the collision direction `u = w` on `S`, `0` elsewhere. Then
`ε · ω_M(z)(u) = ½ Σ_{p ≠ q ∈ S} M_{pq} + ε · (terms regular at ε = 0)`
(`cluster_residue`). So on the blow-up of the collision locus the exceptional divisor carries the
residue `Σ_{p<q ∈ S} M_{pq}`, the pair residues of the cluster added up, and the pairs that leave
the cluster contribute nothing singular. With `M_{pq} = Ω_{pq}` this is the Casimir of the cluster
viewed as one object `V_{p₁} ⊗ … ⊗ V_{p_k}`, minus the Casimirs of its factors: the monoidal
structure, read off at the collision. -/

section Cluster

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- The configuration where the cluster `S` sits at `c + ε w` and the others stay at `z`. -/
def clusterConfig (S : Finset (Fin n)) (c ε : K) (w z : Fin n → K) : Fin n → K :=
  fun p => if p ∈ S then c + ε * w p else z p

/-- The collision direction: `w` on the cluster, `0` outside. -/
def clusterDir (S : Finset (Fin n)) (w : Fin n → K) : Fin n → K :=
  fun p => if p ∈ S then w p else 0

/-- **Residue of a colliding cluster.** For symmetric residues, distinct positions `w` inside the
cluster and `ε ≠ 0`, the form along the collision direction is `ε⁻¹` times half the sum of the
cluster's pair residues, plus a term that stays regular as `ε → 0` whenever `c` differs from
every outside point. -/
theorem cluster_residue (h2 : (2 : K) ≠ 0) {M : Fin n → Fin n → A} (hM : ∀ i j, M i j = M j i)
    (S : Finset (Fin n)) {c ε : K} (hε : ε ≠ 0) {w : Fin n → K}
    (hw : ∀ p ∈ S, ∀ q ∈ S, p ≠ q → w p ≠ w q) (z : Fin n → K) :
    ε • arnoldForm M (clusterConfig S c ε w z) (clusterDir S w) =
      (2 : K)⁻¹ • ∑ p ∈ S, ∑ q ∈ S, (if p = q then (0 : A) else M p q) +
      ε • ∑ p ∈ S, ∑ q ∈ Finset.univ \ S,
        (w p * (c + ε * w p - z q)⁻¹) • M p q := by
  classical
  -- restrict the outer sum to the cluster
  have hout : arnoldForm M (clusterConfig S c ε w z) (clusterDir S w) =
      ∑ p ∈ S, w p • arnoldCoeff M (clusterConfig S c ε w z) p := by
    unfold arnoldForm
    rw [← Finset.sum_subset (Finset.subset_univ S) (fun p _ hp => by
      simp [clusterDir, hp])]
    exact Finset.sum_congr rfl fun p hp => by simp [clusterDir, hp]
  -- split each coefficient into inside and outside partners
  have hsplit : ∀ p ∈ S, arnoldCoeff M (clusterConfig S c ε w z) p =
      ∑ q ∈ S, (ε * (w p - w q))⁻¹ • M p q +
        ∑ q ∈ Finset.univ \ S, (c + ε * w p - z q)⁻¹ • M p q := by
    intro p hp
    unfold arnoldCoeff
    rw [← Finset.sum_sdiff (Finset.subset_univ S), add_comm]
    congr 1
    · refine Finset.sum_congr rfl fun q hq => ?_
      simp only [clusterConfig, if_pos hp, if_pos hq]
      congr 1; ring_nf
    · refine Finset.sum_congr rfl fun q hq => ?_
      have hq' : q ∉ S := (Finset.mem_sdiff.mp hq).2
      simp only [clusterConfig, if_pos hp, if_neg hq']
  -- the inside part: Σ w_p/(w_p − w_q) M_pq = ½ Σ_{p≠q} M_pq
  have hin : ∑ p ∈ S, ∑ q ∈ S, (w p / (w p - w q)) • M p q =
      (2 : K)⁻¹ • ∑ p ∈ S, ∑ q ∈ S, (if p = q then (0 : A) else M p q) := by
    have hswap : ∑ p ∈ S, ∑ q ∈ S, (w q / (w p - w q)) • M p q =
        -∑ p ∈ S, ∑ q ∈ S, (w p / (w p - w q)) • M p q := by
      rw [Finset.sum_comm, ← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun p _ => ?_
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun q _ => ?_
      rw [hM q p, ← neg_sub (w p) (w q), div_neg, neg_smul]
    have hone : ∑ p ∈ S, ∑ q ∈ S, ((w p - w q) / (w p - w q)) • M p q =
        ∑ p ∈ S, ∑ q ∈ S, (if p = q then (0 : A) else M p q) := by
      refine Finset.sum_congr rfl fun p hp => Finset.sum_congr rfl fun q hq => ?_
      by_cases hpq : p = q
      · subst hpq; simp
      · rw [if_neg hpq, div_self (sub_ne_zero.mpr (hw p hp q hq hpq)), one_smul]
    have hdiff : ∑ p ∈ S, ∑ q ∈ S, ((w p - w q) / (w p - w q)) • M p q =
        ∑ p ∈ S, ∑ q ∈ S, (w p / (w p - w q)) • M p q -
          ∑ p ∈ S, ∑ q ∈ S, (w q / (w p - w q)) • M p q := by
      rw [← Finset.sum_sub_distrib]; refine Finset.sum_congr rfl fun p _ => ?_
      rw [← Finset.sum_sub_distrib]; refine Finset.sum_congr rfl fun q _ => ?_
      rw [sub_div, sub_smul]
    rw [hswap, sub_neg_eq_add, ← two_smul K] at hdiff
    rw [← hone, hdiff, smul_smul, inv_mul_cancel₀ h2, one_smul]
  rw [hout, Finset.smul_sum, ← hin, Finset.smul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun p hp => ?_
  rw [hsplit p hp, smul_add, smul_add, Finset.smul_sum, Finset.smul_sum, Finset.smul_sum,
    Finset.smul_sum, Finset.smul_sum]
  congr 1
  · refine Finset.sum_congr rfl fun q _ => ?_
    rw [smul_smul, smul_smul, mul_inv, div_eq_mul_inv]
    by_cases hpq : w p - w q = 0
    · simp [hpq]
    · field_simp
  · refine Finset.sum_congr rfl fun q _ => ?_
    rw [smul_smul, smul_smul, smul_smul]; ring_nf

end Cluster

end QOU.Mass.LagrangianKZ
