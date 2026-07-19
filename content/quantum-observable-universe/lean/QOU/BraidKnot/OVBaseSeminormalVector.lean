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
