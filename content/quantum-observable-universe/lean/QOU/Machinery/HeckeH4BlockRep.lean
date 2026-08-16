import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4BlockRep — the three matrix blocks of H₄(q)

Wenzl-bridge **A2-s2** (bean `qou-xzaq`, approach `qou-pk7l`, milestone
`qou-lv5t`): the Hoefsmit seminormal matrix data for the three
higher-dimensional Wedderburn blocks of the rank-4 Iwahori–Hecke algebra
$H_4(q)$ — partitions $(2,2)$ (2-dimensional), $(3,1)$ (3-dimensional)
and $(2,1,1)$ (3-dimensional).  Together with the two characters
$\chi_+ : \sigma_i \mapsto q$ (partition $(4)$) and
$\chi_- : \sigma_i \mapsto -q^{-1}$ (partition $(1^4)$) these are the
block *data* of $H_4(q) \cong K \times K \times M_2 \times M_3 \times M_3$.

Convention: Hecke quadratic $S^2 = (q - q^{-1})\,S + 1$, eigenvalues
$q$ and $-q^{-1}$; each $2\times 2$ mixing block is b-normalized
($b$-entry $= 1$, $\det = -1$, trace $= q - q^{-1}$), the
`HeckeH3BlockRep.S1` pattern.  Two mixing blocks occur:

* the **axial-distance $-2$** block — *identical* to
  `QOU.Machinery.H3.S1` (`HeckeH3BlockRep`), it is the $\sigma_1$-edge
  mixing block of all three partitions here; genericity denominator
  $q^2 + 1$;
* the **axial-distance $-3$** block — the $\sigma_2$-edge of $(3,1)$
  and $(2,1,1)$, with $a = -1/(q(q^4+q^2+1))$,
  $c = (q^2+1)^2(q^4+1)/(q^4+q^2+1)^2$, $d = q^5/(q^4+q^2+1)$; this is
  where the $[4]$-type factor $q^4 + 1$ enters the rank-4 picture
  (matching its appearance in the determinant of the 24×24 coordinate
  matrix).

For each block we prove, as sorry-free matrix identities: the Hecke
quadratic for $S_0, S_1, S_2$, both adjacent braid relations
$S_0 S_1 S_0 = S_1 S_0 S_1$ and $S_1 S_2 S_1 = S_2 S_1 S_2$, and the
far commutation $S_0 S_2 = S_2 S_0$.

Data provenance: derived and verified symbolically (sympy, exact over
$\mathbb{Q}(q)$) in `computations/h4_wedderburn/` (`derive.py` →
`hecke-h4-wedderburn-seminormal.data.json`; human summary
`docs/audits/2026-07-19-h4-wedderburn-seminormal-data.md`).  Every
matrix entry below is transcribed from that data file.

Base ring (§7c): generic `[Field R]` — inverses are genuinely used; no
archimedean construct.  Genericity hypotheses as needed per theorem:
`q ≠ 0`, `q ^ 2 + 1 ≠ 0`, `q ^ 4 + q ^ 2 + 1 ≠ 0`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001
-/

namespace QOU.Machinery.H4

variable {R : Type*} [Field R]

/-! ## Partition (2,2) — 2-dimensional block

Tableaux order `[12|34], [13|24]`. -/

/-- $(2,2)$ block, $S_0 = \mathrm{diag}(q, -q^{-1})$. -/
noncomputable def S0_22 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  Matrix.of ![![q, 0], ![0, -q⁻¹]]

/-- $(2,2)$ block, $S_1$ — the axial-distance $-2$ mixing block,
    *identical* to `QOU.Machinery.H3.S1` (`HeckeH3BlockRep`). -/
noncomputable def S1_22 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  Matrix.of ![![-(1 / (q * (q ^ 2 + 1))), 1],
              ![(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]]

/-- $(2,2)$ block, $S_2 = \mathrm{diag}(q, -q^{-1}) = S_0$. -/
noncomputable def S2_22 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  Matrix.of ![![q, 0], ![0, -q⁻¹]]

/-- $(2,2)$: $S_0$ satisfies the Hecke quadratic (sorry-free). -/
theorem S0_22_hecke (q : R) (hq : q ≠ 0) :
    S0_22 q * S0_22 q = (q - q⁻¹) • S0_22 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_22, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- $(2,2)$: $S_1$ satisfies the Hecke quadratic (sorry-free). -/
theorem S1_22_hecke (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S1_22 q * S1_22 q = (q - q⁻¹) • S1_22 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_22, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- $(2,2)$: $S_2$ satisfies the Hecke quadratic (sorry-free). -/
theorem S2_22_hecke (q : R) (hq : q ≠ 0) :
    S2_22 q * S2_22 q = (q - q⁻¹) • S2_22 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S2_22, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- $(2,2)$: braid relation $S_0 S_1 S_0 = S_1 S_0 S_1$ (sorry-free). -/
theorem S0_S1_braid_22 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S0_22 q * S1_22 q * S0_22 q = S1_22 q * S0_22 q * S1_22 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_22, S1_22, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- $(2,2)$: braid relation $S_1 S_2 S_1 = S_2 S_1 S_2$ (sorry-free). -/
theorem S1_S2_braid_22 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S1_22 q * S2_22 q * S1_22 q = S2_22 q * S1_22 q * S2_22 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_22, S2_22, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- $(2,2)$: far commutation $S_0 S_2 = S_2 S_0$ (trivial here — both
    diagonal; sorry-free). -/
theorem S0_S2_comm_22 (q : R) :
    S0_22 q * S2_22 q = S2_22 q * S0_22 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_22, S2_22, Matrix.mul_apply, Fin.sum_univ_two]

/-! ## Partition (3,1) — 3-dimensional block

Tableaux order `[123|4], [124|3], [134|2]`. -/

/-- $(3,1)$ block, $S_0 = \mathrm{diag}(q, q, -q^{-1})$. -/
noncomputable def S0_31 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![q, 0, 0], ![0, q, 0], ![0, 0, -q⁻¹]]

/-- $(3,1)$ block, $S_1 = (q) \oplus$ [axial-distance $-2$ mixing block
    on rows 2–3] — the mixing block is `HeckeH3BlockRep.S1`. -/
noncomputable def S1_31 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![q, 0, 0],
              ![0, -(1 / (q * (q ^ 2 + 1))), 1],
              ![0, (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]]

/-- $(3,1)$ block, $S_2 =$ [axial-distance $-3$ mixing block on rows
    1–2] $\oplus (q)$ — the $c$-entry carries the $[4]$-type factor
    $q^4 + 1$. -/
noncomputable def S2_31 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![-(1 / (q * (q ^ 4 + q ^ 2 + 1))), 1, 0],
              ![(q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2,
                q ^ 5 / (q ^ 4 + q ^ 2 + 1), 0],
              ![0, 0, q]]

/-- $(3,1)$: $S_0$ satisfies the Hecke quadratic (sorry-free). -/
theorem S0_31_hecke (q : R) (hq : q ≠ 0) :
    S0_31 q * S0_31 q = (q - q⁻¹) • S0_31 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(3,1)$: $S_1$ satisfies the Hecke quadratic (sorry-free). -/
theorem S1_31_hecke (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S1_31 q * S1_31 q = (q - q⁻¹) • S1_31 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(3,1)$: $S_2$ satisfies the Hecke quadratic (sorry-free). -/
theorem S2_31_hecke (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    S2_31 q * S2_31 q = (q - q⁻¹) • S2_31 q + 1 := by
  -- `field_simp` internally regroups `q^4 + q^2 + 1` as `q^2*(q^2+1) + 1`;
  -- supply the nonzero fact in that exact shape so its discharger fires.
  have h3c : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := fun h => h3 (by linear_combination h)
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S2_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(3,1)$: braid relation $S_0 S_1 S_0 = S_1 S_0 S_1$ (sorry-free). -/
theorem S0_S1_braid_31 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S0_31 q * S1_31 q * S0_31 q = S1_31 q * S0_31 q * S1_31 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_31, S1_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(3,1)$: braid relation $S_1 S_2 S_1 = S_2 S_1 S_2$ (sorry-free) —
    the cross-edge identity mixing the $d=-2$ and $d=-3$ blocks. -/
theorem S1_S2_braid_31 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    S1_31 q * S2_31 q * S1_31 q = S2_31 q * S1_31 q * S2_31 q := by
  -- see `S2_31_hecke` for why the regrouped nonzero fact is needed
  have h3c : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := fun h => h3 (by linear_combination h)
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_31, S2_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(3,1)$: far commutation $S_0 S_2 = S_2 S_0$ ($S_0$ is scalar $q$
    on the rows the $S_2$ mixing block occupies; sorry-free). -/
theorem S0_S2_comm_31 (q : R) :
    S0_31 q * S2_31 q = S2_31 q * S0_31 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_31, S2_31, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try ring

/-! ## Partition (2,1,1) — 3-dimensional block (mirror of (3,1))

Tableaux order `[12|3|4], [13|2|4], [14|2|3]`. -/

/-- $(2,1,1)$ block, $S_0 = \mathrm{diag}(q, -q^{-1}, -q^{-1})$. -/
noncomputable def S0_211 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![q, 0, 0], ![0, -q⁻¹, 0], ![0, 0, -q⁻¹]]

/-- $(2,1,1)$ block, $S_1 =$ [axial-distance $-2$ mixing block on rows
    1–2] $\oplus (-q^{-1})$ — the mixing block is `HeckeH3BlockRep.S1`. -/
noncomputable def S1_211 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![-(1 / (q * (q ^ 2 + 1))), 1, 0],
              ![(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1), 0],
              ![0, 0, -q⁻¹]]

/-- $(2,1,1)$ block, $S_2 = (-q^{-1}) \oplus$ [axial-distance $-3$
    mixing block on rows 2–3] — the $c$-entry carries the $[4]$-type
    factor $q^4 + 1$. -/
noncomputable def S2_211 (q : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![-q⁻¹, 0, 0],
              ![0, -(1 / (q * (q ^ 4 + q ^ 2 + 1))), 1],
              ![0, (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2,
                q ^ 5 / (q ^ 4 + q ^ 2 + 1)]]

/-- $(2,1,1)$: $S_0$ satisfies the Hecke quadratic (sorry-free). -/
theorem S0_211_hecke (q : R) (hq : q ≠ 0) :
    S0_211 q * S0_211 q = (q - q⁻¹) • S0_211 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(2,1,1)$: $S_1$ satisfies the Hecke quadratic (sorry-free). -/
theorem S1_211_hecke (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S1_211 q * S1_211 q = (q - q⁻¹) • S1_211 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(2,1,1)$: $S_2$ satisfies the Hecke quadratic (sorry-free). -/
theorem S2_211_hecke (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    S2_211 q * S2_211 q = (q - q⁻¹) • S2_211 q + 1 := by
  -- see `S2_31_hecke` for why the regrouped nonzero fact is needed
  have h3c : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := fun h => h3 (by linear_combination h)
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S2_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(2,1,1)$: braid relation $S_0 S_1 S_0 = S_1 S_0 S_1$ (sorry-free). -/
theorem S0_S1_braid_211 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S0_211 q * S1_211 q * S0_211 q = S1_211 q * S0_211 q * S1_211 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_211, S1_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(2,1,1)$: braid relation $S_1 S_2 S_1 = S_2 S_1 S_2$ (sorry-free) —
    the cross-edge identity mixing the $d=-2$ and $d=-3$ blocks. -/
theorem S1_S2_braid_211 (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    S1_211 q * S2_211 q * S1_211 q = S2_211 q * S1_211 q * S2_211 q := by
  -- see `S2_31_hecke` for why the regrouped nonzero fact is needed
  have h3c : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := fun h => h3 (by linear_combination h)
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1_211, S2_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try field_simp
  all_goals try ring

/-- $(2,1,1)$: far commutation $S_0 S_2 = S_2 S_0$ ($S_0$ is scalar
    $-q^{-1}$ on the rows the $S_2$ mixing block occupies; sorry-free). -/
theorem S0_S2_comm_211 (q : R) :
    S0_211 q * S2_211 q = S2_211 q * S0_211 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0_211, S2_211, Matrix.mul_apply, Fin.sum_univ_three]
  all_goals try ring

end QOU.Machinery.H4
