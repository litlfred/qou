import QOU.IwahoriHecke.QTraceCyclic

/-!
# The Markov peel, and why the physical weight is forced

`QOU.IwahoriHecke.QTraceCyclic` made the site-weighted trace `tr_w` a genuine trace —
cyclic, hence invariant under conjugation, which is **Markov move I**. What a Markov trace
needs beyond that is **move II**, the *peel*:

    tr(ι(x) · σ_n) = z · tr(x)   for x in the smaller algebra,

relating the trace on `H_{n+1}(q)` to the one on `H_n(q)`. This file proves it, and computes
`z`.

## The tower

Two maps, one on each side of the action:

* `tower` — the algebra map `H_{m+1}(q) → H_{m+2}(q)`, `σ_a ↦ σ_{a.castSucc}`. The only input
  is `coxA_castSucc`, that the type-`A` Coxeter matrix restricts along `castSucc`.
* `extendSiteHom` — the matrix-level counterpart `End(V^{⊗(m+1)}) → End(V^{⊗(m+2)})`,
  `X ↦ X ⊗ 1`, built as `idTensorHom` reindexed along `Fin.snocEquiv`. It is an algebra map
  because both factors are.

`heckeActionN_tower` says the square commutes, by `hom_ext_sigma` — the two composites agree
on generators because `extendSite_strandBraid` does.

## The peel, and the weight it forces

The computation is `trace_peel`. Writing `P u v := ∑ₜ w t · Ř_{(u,t),(v,t)}` for the weighted
partial trace of the braiding over the new site, the whole content is:

* `P` is **diagonal** — `Ř`'s swap entry needs `u = t` and `t = v` at once, so it never
  survives the partial trace;
* if `P` is the scalar `z`, the peel holds with that `z` (`trace_peel`, `qTrace_peel`).

The interesting direction is the converse, and it is what makes the corpus's choice of weight
non-arbitrary:

> **`peel_forces_physical_weight`** — if the peel holds at all, then `w 1 = q² · w 0`. With
> the normalisation `w 0 = 1` that is `w = (1, q²)` on the nose, and then `z = q³`.

So the weight `K = diag(1, q²)` that `QOU.MassTheory.WeightedPermutationCharacter` and the
rest of the corpus use is **not a convention chosen to make things work** — it is the unique
weight (up to overall scale) for which the braiding admits a Markov peel at all, and `q³` is
not fitted either: it is `w 1 · q`, forced by the same two equations.

## 🛑 What this is still not

A Markov trace in the sense the Jones polynomial consumes also wants **normalisation**
`tr(1) = 1`; `qTrace_one` gives `(1 + q²)^{m+1}`, so the normalised functional is
`tr_w / (1 + q²)^{m+1}` and the corresponding `z` acquires the same factor. That rescaling is
not done here. Nor is the link invariant: `QOU.IwahoriHecke.MarkovTrace.markovTrace` is still
`noncomputable opaque`, and nothing here constructs it.

-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials
-- Ref: [jimbo1986]; [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.MarkovPeel

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.QuantumTrace
open QOU.MathlibExt.SkeinRelation QOU.MathlibExt.IwahoriHecke
open Finset

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-! ## Splitting off the last site -/

/-- Splitting a state of `V^{⊗(m+2)}` into its last site and the first `m+1`. -/
def lastSplit (m : ℕ) : Fin 2 × (Fin (m + 1) → Fin 2) ≃ (Fin (m + 2) → Fin 2) :=
  Fin.snocEquiv (fun _ : Fin (m + 2) => Fin 2)

/-- **The site extension** `X ↦ X ⊗ 1`: act by `X` on the first `m+1` sites, do nothing to
the new one. An algebra map, because `idTensorHom` and reindexing both are. -/
noncomputable def extendSiteHom :
    Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R
      →ₐ[R] Matrix (Fin (m + 2) → Fin 2) (Fin (m + 2) → Fin 2) R :=
  (Matrix.reindexAlgEquiv R R (lastSplit m)).toAlgHom.comp
    (idTensorHom (R := R) (σ := Fin 2) (ρ := Fin (m + 1) → Fin 2))

theorem extendSiteHom_apply (X : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R)
    (a b : Fin (m + 2) → Fin 2) :
    extendSiteHom (R := R) (m := m) X a b
      = (if a (Fin.last (m + 1)) = b (Fin.last (m + 1)) then 1 else 0)
        * X (fun k => a k.castSucc) (fun k => b k.castSucc) := by
  simp only [extendSiteHom, AlgHom.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe,
    Matrix.reindexAlgEquiv_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    idTensorHom_apply, idTensor_apply]
  rfl

/-! ## The algebra tower -/

/-- The type-`A` Coxeter matrix restricts along `castSucc`: strands `0 … m−1` of `H_{m+2}(q)`
carry the same Coxeter data they had in `H_{m+1}(q)`. -/
theorem coxA_castSucc (a b : Fin m) :
    coxA (m + 1) a.castSucc b.castSucc = coxA m a b := by
  unfold coxA
  simp [Fin.ext_iff]

/-- **The tower map** `H_{m+1}(q) → H_{m+2}(q)`, adding a strand on the right. -/
noncomputable def tower (hqi : q * qi = 1) :
    QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q →ₐ[R]
      QOU.IwahoriHecke.Balanced.BalancedHecke (coxA (m + 1)) q :=
  QOU.IwahoriHecke.Balanced.liftBalanced hqi
    (fun a => QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi a.castSucc)
    (fun _ => QOU.IwahoriHecke.Balanced.isHeckeGenerator_sigma hqi _)
    (fun a b => by
      rw [← coxA_castSucc a b, ← coxA_castSucc b a]
      exact QOU.IwahoriHecke.Balanced.sigma_braid coxA_symm a.castSucc b.castSucc)
    coxA_symm

@[simp] theorem tower_sigma (hqi : q * qi = 1) (a : Fin m) :
    tower q qi hqi (QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a)
      = QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi a.castSucc :=
  QOU.IwahoriHecke.Balanced.liftBalanced_sigma hqi _ _ _ coxA_symm a

/-- The site extension of a strand braiding is the corresponding strand braiding one level
up. This is the one place the `Fin` arithmetic of the tower is done. -/
theorem extendSite_strandBraid (a : Fin m) :
    extendSiteHom (R := R) (m := m) (strandBraid q qi a)
      = strandBraid q qi (a.castSucc : Fin (m + 1)) := by
  classical
  have ha : (a : ℕ) < m := a.isLt
  have hs : ((a.succ).castSucc : Fin (m + 2)) = (a.castSucc : Fin (m + 1)).succ := by
    simp
  ext u v
  simp only [extendSiteHom_apply, strandBraid, braidAt, embedPair_apply, hs]
  by_cases hall : ∀ k : Fin (m + 2), k ≠ ((a.castSucc : Fin (m + 1)).castSucc) →
      k ≠ ((a.castSucc : Fin (m + 1)).succ) → u k = v k
  · have hne : ∀ i : Fin (m + 1), (i.castSucc : Fin (m + 2)) ≠ Fin.last (m + 1) :=
      fun i => (Fin.castSucc_lt_last i).ne
    have hL : u (Fin.last (m + 1)) = v (Fin.last (m + 1)) := by
      refine hall _ (fun hc => hne _ hc.symm) (fun hc => hne a.succ ?_)
      rw [hs]; exact hc.symm
    have hI : ∀ k : Fin (m + 1), k ≠ a.castSucc → k ≠ a.succ →
        u k.castSucc = v k.castSucc := by
      intro k h1 h2
      exact hall _ (fun hc => h1 (Fin.castSucc_injective _ hc))
        (fun hc => h2 (Fin.castSucc_injective _ (hc.trans hs.symm)))
    rw [if_pos hall, if_pos hI, if_pos hL, one_mul]
  · rw [if_neg hall]
    push_neg at hall
    obtain ⟨k, hk1, hk2, hk3⟩ := hall
    revert hk1 hk2 hk3
    induction k using Fin.lastCases with
    | last => intro _ _ h; rw [if_neg h, zero_mul]
    | cast k' =>
      intro h1 h2 h3
      have hno : ¬ (∀ kk : Fin (m + 1), kk ≠ a.castSucc → kk ≠ a.succ →
          u kk.castSucc = v kk.castSucc) := fun hI =>
        h3 (hI k' (fun hc => h1 (by rw [hc])) (fun hc => h2 (by rw [hc, hs])))
      rw [if_neg hno, mul_zero]

/-- **The tower square commutes**: acting after adding a strand is extending the action. -/
theorem heckeActionN_tower (hqi : q * qi = 1)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    heckeActionN q qi hqi (tower q qi hqi x)
      = extendSiteHom (heckeActionN q qi hqi x) := by
  have hcomp : (heckeActionN q qi hqi).comp (tower q qi hqi)
      = (extendSiteHom (R := R) (m := m)).comp (heckeActionN q qi hqi) :=
    QOU.IwahoriHecke.Balanced.hom_ext_sigma hqi _ _ (fun a => by
      rw [AlgHom.comp_apply, AlgHom.comp_apply, tower_sigma, heckeActionN_sigma,
        heckeActionN_sigma, extendSite_strandBraid])
  simpa using DFunLike.congr_fun hcomp x

/-! ## The braiding's weighted partial trace over the new site -/

/-- The diagonal entries of `Ř`. -/
theorem rCheck_diag_apply (u t : Fin 2) :
    rCheck q qi (u, t) (u, t) = if u = t then q else if u < t then q - qi else 0 := by
  rw [rCheck_apply, if_pos rfl]

private theorem rc_00 : rCheck q qi ((0 : Fin 2), (0 : Fin 2)) (0, 0) = q := by
  rw [rCheck_diag_apply, if_pos rfl]

private theorem rc_01 : rCheck q qi ((0 : Fin 2), (1 : Fin 2)) (0, 1) = q - qi := by
  rw [rCheck_diag_apply, if_neg (by decide), if_pos (by decide)]

private theorem rc_10 : rCheck q qi ((1 : Fin 2), (0 : Fin 2)) (1, 0) = 0 := by
  rw [rCheck_diag_apply, if_neg (by decide), if_neg (by decide)]

private theorem rc_11 : rCheck q qi ((1 : Fin 2), (1 : Fin 2)) (1, 1) = q := by
  rw [rCheck_diag_apply, if_pos rfl]

/-- **The peel scalar exists exactly at the physical weight.**

If the weighted partial trace of `Ř` over the new site is the *same* scalar `z` whichever
value the surviving site carries — which is precisely what a peel `tr(xσ) = z·tr(x)` needs —
then `w 0 · q = w 1 · qi`, i.e. `w 1 = q² · w 0`, and `z = w 1 · q`.

So the corpus's weight `K = diag(1, q²)` is forced by the peel, not chosen for it. -/
theorem peel_forces_physical_weight (w : Fin 2 → R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = z) :
    w 0 * q = w 1 * qi ∧ z = w 1 * q := by
  have e0 := hP 0
  have e1 := hP 1
  rw [Fin.sum_univ_two, rc_00, rc_01] at e0
  rw [Fin.sum_univ_two, rc_10, rc_11, mul_zero, zero_add] at e1
  exact ⟨by linear_combination e0 - e1, e1.symm⟩

/-- With the scale fixed by `w 0 = 1`, the forced weight is `(1, q²)` and the forced peel
scalar is `q³`. -/
theorem peel_weight_eq (hqi : q * qi = 1) (w : Fin 2 → R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = z)
    (h0 : w 0 = 1) : w 1 = q ^ 2 ∧ z = q ^ 3 := by
  obtain ⟨hw, hz⟩ := peel_forces_physical_weight q qi w z hP
  rw [h0, one_mul] at hw
  have h1 : w 1 = q ^ 2 := by linear_combination (-q) * hw - w 1 * hqi
  exact ⟨h1, by rw [hz, h1]; ring⟩

/-- The converse: at `w = (1, q²)` the partial trace really is the scalar `q³`. -/
theorem peel_scalar_of_physical (hqi : q * qi = 1) (w : Fin 2 → R)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) (u : Fin 2) :
    (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = q ^ 3 := by
  rcases (by decide : ∀ u : Fin 2, u = 0 ∨ u = 1) u with rfl | rfl
  · rw [Fin.sum_univ_two, rc_00, rc_01, h0, h1]
    linear_combination (-q) * hqi
  · rw [Fin.sum_univ_two, rc_10, rc_11, h0, h1]
    ring

/-! ## The peel -/

/-- The site index braided against the new one, and the new site itself. -/
private theorem last_succ_eq : ((Fin.last m).succ : Fin (m + 2)) = Fin.last (m + 1) := by
  simp

/-- **The diagonal of `(X ⊗ 1) · Ř` collapses to one term.**

The two supports intersect tightly: `X ⊗ 1` forces the new site to be preserved, and `Ř`
forces every site but the two it acts on to be preserved, leaving only site `m` free — and
`Ř`'s swap entry cannot fire there because it would need that free value to equal both of the
others. So only the diagonal survives. -/
theorem extendSite_mul_lastBraid_diag
    (X : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) (u : Fin (m + 2) → Fin 2) :
    (extendSiteHom (R := R) X * strandBraid q qi (Fin.last m)) u u
      = X (fun k => u k.castSucc) (fun k => u k.castSucc)
        * rCheck q qi (u ((Fin.last m).castSucc), u (Fin.last (m + 1)))
            (u ((Fin.last m).castSucc), u (Fin.last (m + 1))) := by
  classical
  rw [Matrix.mul_apply, Finset.sum_eq_single u]
  · rw [extendSiteHom_apply, if_pos rfl, one_mul, strandBraid, braidAt, embedPair_apply,
      if_pos (fun _ _ _ => rfl), last_succ_eq]
  · intro c _ hcu
    rw [extendSiteHom_apply, strandBraid, braidAt, embedPair_apply, last_succ_eq]
    by_cases hoff : ∀ k : Fin (m + 2), k ≠ (Fin.last m).castSucc → k ≠ Fin.last (m + 1) →
        c k = u k
    · by_cases hlast : u (Fin.last (m + 1)) = c (Fin.last (m + 1))
      · -- `c` agrees with `u` off site `m`; the swap entry cannot fire, so `Ř` vanishes
        have hci : c ((Fin.last m).castSucc) ≠ u ((Fin.last m).castSucc) := by
          intro hc
          refine hcu (funext fun k => ?_)
          by_cases hk : k = (Fin.last m).castSucc
          · rw [hk, hc]
          · by_cases hk' : k = Fin.last (m + 1)
            · rw [hk', hlast]
            · exact hoff k hk hk'
        have hz : rCheck q qi (c ((Fin.last m).castSucc), c (Fin.last (m + 1)))
            (u ((Fin.last m).castSucc), u (Fin.last (m + 1))) = 0 := by
          rw [rCheck_apply, if_neg, if_neg]
          · intro hc
            have h1 : c ((Fin.last m).castSucc) = u (Fin.last (m + 1)) :=
              congrArg Prod.fst hc
            have h2 : c (Fin.last (m + 1)) = u ((Fin.last m).castSucc) :=
              congrArg Prod.snd hc
            exact hci (by rw [h1, hlast, h2])
          · intro hc
            exact hci (congrArg Prod.fst hc)
        rw [if_pos hoff, hz, mul_zero]
      · rw [if_neg hlast, zero_mul, zero_mul]
    · rw [if_neg hoff, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ u) h

/-- Rewriting a weighted trace as a sum over basis states. -/
theorem trace_siteWeight_mul {n : ℕ} (w : Fin 2 → R)
    (M : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) :
    Matrix.trace (siteWeight w * M) = ∑ a : Fin n → Fin 2, (∏ k, w (a k)) * M a a := by
  rw [Matrix.trace]
  exact Finset.sum_congr rfl (fun a _ => by
    rw [Matrix.diag_apply, siteWeight, Matrix.diagonal_mul])

/-- **The peel, at matrix level.** -/
theorem trace_peel (w : Fin 2 → R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = z)
    (X : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) :
    Matrix.trace (siteWeight (n := m + 2) w
        * (extendSiteHom X * strandBraid q qi (Fin.last m)))
      = z * Matrix.trace (siteWeight (n := m + 1) w * X) := by
  classical
  have hsplit : ∀ F : (Fin (m + 2) → Fin 2) → R,
      (∑ a : Fin (m + 2) → Fin 2, F a)
        = ∑ a' : Fin (m + 1) → Fin 2, ∑ t : Fin 2, F (lastSplit m (t, a')) := by
    intro F
    rw [← Equiv.sum_comp (lastSplit m) F, Fintype.sum_prod_type, Finset.sum_comm]
  rw [trace_siteWeight_mul, trace_siteWeight_mul, Finset.mul_sum]
  simp only [extendSite_mul_lastBraid_diag]
  rw [hsplit]
  refine Finset.sum_congr rfl (fun a' _ => ?_)
  have hcs : ∀ (t : Fin 2) (k : Fin (m + 1)), lastSplit m (t, a') k.castSucc = a' k := by
    intro t k; simp [lastSplit]
  have hlst : ∀ t : Fin 2, lastSplit m (t, a') (Fin.last (m + 1)) = t := by
    intro t; simp [lastSplit]
  have hprod : ∀ t : Fin 2, (∏ k : Fin (m + 2), w (lastSplit m (t, a') k))
      = (∏ k : Fin (m + 1), w (a' k)) * w t := by
    intro t
    rw [Fin.prod_univ_castSucc]
    congr 1
    · exact Finset.prod_congr rfl (fun k _ => by rw [hcs t k])
    · rw [hlst t]
  have hstep : ∀ t : Fin 2,
      (∏ k : Fin (m + 2), w (lastSplit m (t, a') k))
        * (X (fun k => lastSplit m (t, a') k.castSucc)
              (fun k => lastSplit m (t, a') k.castSucc)
          * rCheck q qi (lastSplit m (t, a') ((Fin.last m).castSucc),
              lastSplit m (t, a') (Fin.last (m + 1)))
            (lastSplit m (t, a') ((Fin.last m).castSucc),
              lastSplit m (t, a') (Fin.last (m + 1))))
      = (w t * rCheck q qi (a' (Fin.last m), t) (a' (Fin.last m), t))
          * ((∏ k : Fin (m + 1), w (a' k)) * X a' a') := by
    intro t
    have hfun : (fun k => lastSplit m (t, a') k.castSucc) = a' := funext (fun k => hcs t k)
    rw [hprod t, hfun, hcs t (Fin.last m), hlst t]
    ring
  refine (Finset.sum_congr rfl (fun t _ => hstep t)).trans ?_
  rw [← Finset.sum_mul, hP]

/-- **The peel, at algebra level.** `tr_w(ι(x) · σ_last) = z · tr_w(x)` — Markov move II,
conditional on the weight admitting a peel scalar at all. -/
theorem qTrace_peel (hqi : q * qi = 1) (w : Fin 2 → R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = z)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    qTrace q qi (m := m + 1) hqi w
        (tower q qi hqi x * QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi (Fin.last m))
      = z * qTrace q qi (m := m) hqi w x := by
  rw [qTrace, map_mul, heckeActionN_tower, heckeActionN_sigma, trace_peel q qi w z hP, qTrace]

/-- **The peel at the physical weight**, with its forced scalar: `z = q³`. -/
theorem qTrace_peel_physical (hqi : q * qi = 1) (w : Fin 2 → R)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    qTrace q qi (m := m + 1) hqi w
        (tower q qi hqi x * QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi (Fin.last m))
      = q ^ 3 * qTrace q qi (m := m) hqi w x :=
  qTrace_peel q qi hqi w (q ^ 3) (peel_scalar_of_physical q qi hqi w h0 h1) x

end QOU.IwahoriHecke.MarkovPeel
