import QOU.BraidKnot.JucysMurphy

/-!
# OV base seminormal vector — the polytabloid JM computation (toward `seminormalVector_base_exists`)

The single remaining `sorry` in the Okounkov–Vershik seminormal cone,
`seminormalVector_base_exists` ([`JucysMurphy.lean`]), reduces (numerically confirmed,
[audit 2026-07-19](../../../../docs/audits/2026-07-19-ov-base-vector-column-superstandard-verification.md))
to the eigen-equation on the **column-superstandard** polytabloid:

  `X_s · e_{T₀} = content(cell of s) · e_{T₀}`.

This file builds that computation from the sorry-free Specht foundation. First brick:
the **reduction** of the abstract JM action `(rep μ).asAlgebraHom (jucysMurphy n s)`
applied to a polytabloid into the concrete signed-cell polytabloid sum
`∑_{j<s} e_{(j\,s)·t}` — general in the tableau `t`, from
`Representation.asAlgebraHom_single` + `rep_polytabloid`.

-- Ref: [vershik-kerov1977] (Young's seminormal form)
-/

namespace QOU.BraidKnot.OVBaseSeminormalVector

open Specht QOU.BraidKnot.JucysMurphy

variable {k : Type} [CommRing k] {μ : YoungDiagram}

/-- **JM action on a polytabloid = a polytabloid sum.** The Jucys–Murphy element
    `X_s = ∑_{j<s} (j\,s)` acts on the polytabloid `e_t` by
    `∑_{j<s} e_{(j\,s)·t}` — each transposition permutes the polytabloid
    (`rep_polytabloid`), and `asAlgebraHom` sends the `single` sum to the
    endomorphism sum. General in `t`; the eigen-equation is what this sum collapses
    to for the column-superstandard `T₀`. -/
theorem jm_smul_polytabloid (s : Fin (Specht.nOf μ)) (t : Specht.Tableau μ) :
    (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s)
        (Specht.polytabloid (k := k) t)
      = ∑ j ∈ Finset.univ.filter (fun j : Fin (Specht.nOf μ) => j.val < s.val),
          Specht.polytabloid (k := k) ((Equiv.swap j s) • t) := by
  unfold jucysMurphy
  rw [map_sum, LinearMap.sum_apply]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [Representation.asAlgebraHom_single, one_smul,
    QOU.BraidKnot.JucysMurphy.rep_polytabloid]

/-! ## Brick 2 — column antisymmetry of the polytabloid -/

/-- **Column antisymmetry.** For `σ` in the column stabilizer of `t`, permuting the
    columns signs the polytabloid: `rep σ (e_t) = sgn(σ) · e_t`. Reindex the
    column-stabilizer sum by left-multiplication by `σ` (a bijection of `colStab t`,
    as `σ ∈ colStab t`); `sgn(σ·π) = sgn(σ)·sgn(π)` and `sgn(σ)² = 1` collapse the
    signs. -/
theorem rep_colStab_polytabloid (t : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab t) :
    Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign σ : ℤ) • Specht.polytabloid (k := k) t := by
  classical
  rw [Specht.polytabloid, map_sum, Finset.smul_sum]
  refine Fintype.sum_equiv (Equiv.mulLeft (⟨σ, hσ⟩ : Specht.colStab t)) _ _ (fun π => ?_)
  rw [map_zsmul, Specht.Mtab.rep_of]
  show (Equiv.Perm.sign (π : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
        • Specht.Mtab.of (k := k) (σ • (π : Equiv.Perm (Fin (Specht.nOf μ))) • t)
      = (Equiv.Perm.sign σ : ℤ)
        • ((Equiv.Perm.sign (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))))  : ℤ)
            • Specht.Mtab.of (k := k) ((σ * (π : Equiv.Perm (Fin (Specht.nOf μ)))) • t))
  have hw : (σ * (π : Equiv.Perm (Fin (Specht.nOf μ)))) • t
      = σ • (π : Equiv.Perm (Fin (Specht.nOf μ))) • t := mul_smul _ _ _
  rw [hw, ← mul_smul (Equiv.Perm.sign σ : ℤ)
        (Equiv.Perm.sign (σ * (π : Equiv.Perm (Fin (Specht.nOf μ)))) : ℤ),
      map_mul, Units.val_mul, ← mul_assoc, ← Units.val_mul, Int.units_mul_self,
      Units.val_one, one_mul]

/-- **A same-column transposition negates the polytabloid.** If the transposition
    `swap j s` lies in the column stabilizer of `t` (i.e. `j, s` are in the same
    column), then `e_{(j\,s)·t} = − e_t` — the sign of a transposition. -/
theorem polytabloid_swap_colStab (t : Specht.Tableau μ) {j s : Fin (Specht.nOf μ)}
    (hjs : j ≠ s) (hmem : Equiv.swap j s ∈ Specht.colStab t) :
    Specht.polytabloid (k := k) ((Equiv.swap j s) • t)
      = - Specht.polytabloid (k := k) t := by
  rw [← QOU.BraidKnot.JucysMurphy.rep_polytabloid, rep_colStab_polytabloid t hmem,
    Equiv.Perm.sign_swap hjs]
  simp

/-- **C-antisymmetry sum collapse (the coset-inner-sum).** For any finite set `H`
    of permutations all lying in the column stabilizer of `t`, the signed
    representation sum collapses to `|H| · e_t`: each term is
    `sgn(σ) · (sgn(σ) · e_t) = sgn(σ)² · e_t = e_t` by brick 2
    (`rep_colStab_polytabloid`) and `sgn(σ)² = 1`. This is the inner sum over a
    full-column subgroup `S_C ⊆ colStab t` in the coset decomposition of the
    single-column Garnir relation (brick 3b): it turns `∑_{π ∈ S_C} sgn(π)·π·e_t`
    into `|C|! · e_t`. Collision-independent — pure column antisymmetry. -/
theorem colStab_subset_sum_rep_polytabloid (t : Specht.Tableau μ)
    (H : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hH : ∀ σ ∈ H, σ ∈ Specht.colStab t) :
    ∑ σ ∈ H, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
      = H.card • Specht.polytabloid (k := k) t := by
  classical
  rw [← Finset.sum_const]
  refine Finset.sum_congr rfl (fun σ hσ => ?_)
  rw [rep_colStab_polytabloid t (hH σ hσ), smul_smul, ← Units.val_mul,
    Int.units_mul_self, Units.val_one, one_smul]

/-- **The outer star-sum evaluation.** The signed transposition sum over the
    `|C|+1` coset representatives `{(x\,s) : x ∈ {s} ∪ C}` (with `(s\,s) = 1`)
    evaluates to `e_t − ∑_{j∈C} e_{(j\,s)·t}`: the `x = s` term contributes `+e_t`
    (identity), and each `x = j ∈ C` term contributes `−e_{(j\,s)·t}`
    (`sgn(swap j s) = −1`, `rep_polytabloid`). This is the RHS of the single-column
    Garnir cancellation `0 = |C|!·(e_t − ∑_{j∈C} e_{(j\,s)·t})`; collision-independent. -/
theorem starSum_rep_polytabloid (t : Specht.Tableau μ)
    (C : Finset (Fin (Specht.nOf μ))) (s : Fin (Specht.nOf μ)) (hs : s ∉ C) :
    ∑ x ∈ insert s C, (Equiv.Perm.sign (Equiv.swap x s) : ℤ) •
        Specht.Mtab.rep (k := k) μ (Equiv.swap x s) (Specht.polytabloid (k := k) t)
      = Specht.polytabloid (k := k) t
        - ∑ j ∈ C, Specht.polytabloid (k := k) ((Equiv.swap j s) • t) := by
  classical
  rw [Finset.sum_insert hs]
  have hid : (Equiv.Perm.sign (Equiv.swap s s) : ℤ) •
      Specht.Mtab.rep (k := k) μ (Equiv.swap s s) (Specht.polytabloid (k := k) t)
      = Specht.polytabloid (k := k) t := by
    rw [Equiv.swap_self]
    show (Equiv.Perm.sign (1 : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) •
        Specht.Mtab.rep (k := k) μ 1 (Specht.polytabloid (k := k) t) = _
    simp
  rw [hid]
  have hC : ∑ j ∈ C, (Equiv.Perm.sign (Equiv.swap j s) : ℤ) •
        Specht.Mtab.rep (k := k) μ (Equiv.swap j s) (Specht.polytabloid (k := k) t)
      = - ∑ j ∈ C, Specht.polytabloid (k := k) ((Equiv.swap j s) • t) := by
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl (fun j hj => ?_)
    have hjs : j ≠ s := fun h => hs (h ▸ hj)
    rw [Equiv.Perm.sign_swap hjs, QOU.BraidKnot.JucysMurphy.rep_polytabloid]
    simp
  rw [hC, ← sub_eq_add_neg]

open scoped Classical in
/-- The subgroup `S_D` of permutations fixing every label **outside** `D`
    (realised as a `Finset`), used as `S_C` and `S_{C∪{s}}` in the single-column
    Garnir coset decomposition. -/
def permFixingOutside (D : Finset (Fin (Specht.nOf μ))) :
    Finset (Equiv.Perm (Fin (Specht.nOf μ))) :=
  Finset.univ.filter (fun σ => ∀ l, l ∉ D → σ l = l)

open scoped Classical in
theorem mem_permFixingOutside {D : Finset (Fin (Specht.nOf μ))}
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} :
    σ ∈ permFixingOutside (μ := μ) D ↔ ∀ l, l ∉ D → σ l = l := by
  rw [permFixingOutside, Finset.mem_filter]
  exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩

/-- **The full-group single-column Garnir sum = `|S_C| · (e_t − ∑ e_{(j\,s)·t})`
    (sorry-free, collision-independent).** For a label set `C` lying in one column of
    `t` (hypothesis `hCcol`: every permutation supported on `C` preserves columns) and
    a label `s ∉ C`, the signed representation sum over the **full** group `S_{C∪{s}}`
    factors as `|S_C|` copies of the outer star-sum. Route: reindex `S_{C∪{s}}` by the
    bijection `(x, π) ↦ (x\,s)·π` onto `(C∪{s}) × S_C`, collapse the inner `S_C`-sum
    to `|S_C|·e_t` by column antisymmetry (`colStab_subset_sum_rep_polytabloid`), and
    recognise the outer sum via `starSum_rep_polytabloid`. Combined with the
    (collision-dependent) full-group **annihilation** `= 0` and `|S_C| = |C|! ≠ 0`,
    this yields the single-column relation `∑_{j∈C} e_{(j\,s)·t} = e_t`. -/
theorem colGarnir_fullgroup_sum (t : Specht.Tableau μ)
    (C : Finset (Fin (Specht.nOf μ))) (s : Fin (Specht.nOf μ)) (hs : s ∉ C)
    (hCcol : ∀ π ∈ permFixingOutside (μ := μ) C, π ∈ Specht.colStab t) :
    ∑ σ ∈ permFixingOutside (μ := μ) (insert s C), (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
      = (permFixingOutside (μ := μ) C).card •
          (Specht.polytabloid (k := k) t
            - ∑ j ∈ C, Specht.polytabloid (k := k) ((Equiv.swap j s) • t)) := by
  classical
  set SC := permFixingOutside (μ := μ) C with hSC
  set SCs := permFixingOutside (μ := μ) (insert s C) with hSCs
  -- membership helper: any σ ∈ SCs maps s into `insert s C`
  have hs_mem : ∀ σ ∈ SCs, σ s ∈ insert s C := by
    intro σ hσ
    by_contra hc
    have h1 : σ (σ s) = σ s := (mem_permFixingOutside (μ := μ)).mp hσ (σ s) hc
    have h2 : σ s = s := by have := congrArg σ.symm h1; simpa using this
    rw [h2] at hc
    exact hc (Finset.mem_insert_self s C)
  -- the reindexing bijection `(x, π) ↦ (x s)·π`, inverse `σ ↦ (σ s, (σ s, s)·σ)`
  have stepA : ∑ σ ∈ SCs, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
      = ∑ p ∈ (insert s C) ×ˢ SC, (Equiv.Perm.sign (Equiv.swap p.1 s * p.2) : ℤ) •
          Specht.Mtab.rep (k := k) μ (Equiv.swap p.1 s * p.2)
            (Specht.polytabloid (k := k) t) := by
    refine Finset.sum_nbij' (fun σ => (σ s, Equiv.swap (σ s) s * σ))
      (fun p => Equiv.swap p.1 s * p.2) ?_ ?_ ?_ ?_ ?_
    · -- hi : image lands in the product
      intro σ hσ
      rw [Finset.mem_product]
      refine ⟨hs_mem σ hσ, ?_⟩
      rw [hSC, mem_permFixingOutside (μ := μ)]
      intro l hl
      rcases eq_or_ne l s with rfl | hls
      · rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left]
      · have hlins : l ∉ insert s C := by
          rw [Finset.mem_insert]; push_neg; exact ⟨hls, hl⟩
        rw [Equiv.Perm.mul_apply, (mem_permFixingOutside (μ := μ)).mp hσ l hlins,
          Equiv.swap_apply_of_ne_of_ne
            (fun h => hlins (by rw [h]; exact hs_mem σ hσ)) hls]
    · -- hj : the product image lands back in SCs
      intro p hp
      rw [Finset.mem_product] at hp
      rw [hSCs, mem_permFixingOutside (μ := μ)]
      intro l hl
      have hlC : l ∉ C := fun h => hl (Finset.mem_insert_of_mem h)
      have hls : l ≠ s := fun h => hl (h ▸ Finset.mem_insert_self s C)
      have hlp1 : l ≠ p.1 := fun h => hl (h ▸ hp.1)
      rw [Equiv.Perm.mul_apply, (mem_permFixingOutside (μ := μ)).mp hp.2 l hlC,
        Equiv.swap_apply_of_ne_of_ne hlp1 hls]
    · -- left_inv
      intro σ _
      show Equiv.swap (σ s) s * (Equiv.swap (σ s) s * σ) = σ
      rw [← mul_assoc, Equiv.swap_mul_self, one_mul]
    · -- right_inv
      intro p hp
      rw [Finset.mem_product] at hp
      have hp2s : p.2 s = s := (mem_permFixingOutside (μ := μ)).mp hp.2 s hs
      have hfst : (Equiv.swap p.1 s * p.2) s = p.1 := by
        rw [Equiv.Perm.mul_apply, hp2s, Equiv.swap_apply_right]
      apply Prod.ext
      · exact hfst
      · show Equiv.swap ((Equiv.swap p.1 s * p.2) s) s * (Equiv.swap p.1 s * p.2) = p.2
        rw [hfst, ← mul_assoc, Equiv.swap_mul_self, one_mul]
    · -- h : summand agreement under the bijection
      intro σ _
      show (Equiv.Perm.sign σ : ℤ) •
          Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
        = (Equiv.Perm.sign (Equiv.swap (σ s) s * (Equiv.swap (σ s) s * σ)) : ℤ) •
          Specht.Mtab.rep (k := k) μ (Equiv.swap (σ s) s * (Equiv.swap (σ s) s * σ))
            (Specht.polytabloid (k := k) t)
      rw [show Equiv.swap (σ s) s * (Equiv.swap (σ s) s * σ) = σ from by
        rw [← mul_assoc, Equiv.swap_mul_self, one_mul]]
  rw [stepA, Finset.sum_product' (insert s C) SC
      (fun a b => (Equiv.Perm.sign (Equiv.swap a s * b) : ℤ) •
        Specht.Mtab.rep (k := k) μ (Equiv.swap a s * b) (Specht.polytabloid (k := k) t))]
  -- inner sum over `S_C` collapses to `|S_C|·e_t` (column antisymmetry)
  have inner : ∀ x, ∑ π ∈ SC, (Equiv.Perm.sign (Equiv.swap x s * π) : ℤ) •
        Specht.Mtab.rep (k := k) μ (Equiv.swap x s * π) (Specht.polytabloid (k := k) t)
      = SC.card • ((Equiv.Perm.sign (Equiv.swap x s) : ℤ) •
          Specht.Mtab.rep (k := k) μ (Equiv.swap x s) (Specht.polytabloid (k := k) t)) := by
    intro x
    have hpull : ∑ π ∈ SC, (Equiv.Perm.sign (Equiv.swap x s * π) : ℤ) •
          Specht.Mtab.rep (k := k) μ (Equiv.swap x s * π) (Specht.polytabloid (k := k) t)
        = (Equiv.Perm.sign (Equiv.swap x s) : ℤ) •
            Specht.Mtab.rep (k := k) μ (Equiv.swap x s)
              (∑ π ∈ SC, (Equiv.Perm.sign π : ℤ) •
                Specht.Mtab.rep (k := k) μ π (Specht.polytabloid (k := k) t)) := by
      rw [map_sum, Finset.smul_sum]
      refine Finset.sum_congr rfl (fun π _ => ?_)
      simp only [map_mul, Module.End.mul_apply, map_zsmul, Units.val_mul, mul_smul]
    rw [hpull, colStab_subset_sum_rep_polytabloid t SC hCcol, map_nsmul, smul_comm]
  rw [Finset.sum_congr rfl (fun x _ => inner x), ← Finset.smul_sum,
    starSum_rep_polytabloid t C s hs]

/-! ## Brick 3a — the same-column contribution of the JM sum

Splitting the reduction sum `Σ_{j<s} e_{(j s)·t}` (brick 1) by whether `swap j s`
lies in the column stabilizer: the **same-column** part evaluates outright to
`(count) · (−e_t)` via brick 2, isolating the **off-column** (Garnir) part as the
sole remaining debt toward the eigen-equation. -/

/-- **Same-column contribution.** The same-column part of the JM polytabloid sum
    (`j < s` with `swap j s ∈ colStab t`) is `(count) · (−e_t)` — each term is
    `−e_t` by `polytabloid_swap_colStab`. -/
theorem sameColumn_sum_polytabloid (s : Fin (Specht.nOf μ)) (t : Specht.Tableau μ) :
    ∑ j ∈ Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        j.val < s.val ∧ Equiv.swap j s ∈ Specht.colStab t),
          Specht.polytabloid (k := k) ((Equiv.swap j s) • t)
      = (Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
          j.val < s.val ∧ Equiv.swap j s ∈ Specht.colStab t)).card
            • (- Specht.polytabloid (k := k) t) := by
  classical
  rw [← Finset.sum_const]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [Finset.mem_filter] at hj
  obtain ⟨_, hlt, hmem⟩ := hj
  exact polytabloid_swap_colStab t (ne_of_lt (Fin.lt_def.mpr hlt)) hmem

/-- **The JM sum, split by column** (brick 1 + brick 3a). The JM action on `e_t`
    is `(same-column count) · (−e_t)` plus the **off-column** sum
    `Σ_{j<s, swap j s ∉ colStab t} e_{(j s)·t}`. This isolates the off-column
    (Garnir) part as the sole remaining piece of the eigen-equation. -/
theorem jm_polytabloid_split (s : Fin (Specht.nOf μ)) (t : Specht.Tableau μ) :
    (Specht.Mtab.rep (k := k) μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s)
        (Specht.polytabloid (k := k) t)
      = (Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
            j.val < s.val ∧ Equiv.swap j s ∈ Specht.colStab t)).card
            • (- Specht.polytabloid (k := k) t)
        + ∑ j ∈ Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
            j.val < s.val ∧ Equiv.swap j s ∉ Specht.colStab t),
              Specht.polytabloid (k := k) ((Equiv.swap j s) • t) := by
  classical
  rw [jm_smul_polytabloid,
    ← Finset.sum_filter_add_sum_filter_not
        (Finset.univ.filter (fun j : Fin (Specht.nOf μ) => j.val < s.val))
        (fun j => Equiv.swap j s ∈ Specht.colStab t)]
  simp only [Finset.filter_filter]
  rw [sameColumn_sum_polytabloid]

end QOU.BraidKnot.OVBaseSeminormalVector
