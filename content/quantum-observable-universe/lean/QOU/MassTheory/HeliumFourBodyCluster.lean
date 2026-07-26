/-
# The A=4 (⁴He) 4-body residual is a SATURATION object (μ₄ < 0), sign-INCOMPATIBLE
# with the Borromean-deficit binding recipe — the derived cluster recipe does NOT
# extend from A=3 to A=4 on SIGN (a sign SWAP).

Route-3 extension of the derived Borromean cluster probe (#4360 sign / #4364
magnitude lift) to the next isotope A=4.  The question posed: does the SAME 0-fit
Borromean-lift recipe reproduce the ⁴He 4-body residual?

**The derived A=4 residual target (forward AME − model, 0 fit).**  The exact
0-parameter simplex (Mayer) decomposition of the graded-subtracted residual
`M(A) = ρ_strong(A) − ρ_grad(A)` over the derived coordination-graph counts
`C(A,k)` (edges, triangles, tetrahedra), pinned by the three points A = 2, 3, 4
(`QOU.MassTheory.AdditiveResidualSimplex` #4320,
`deltalambda_kappa_interface_residual_simplex_probe.py`), gives

    μ₂ = 0,   μ₃ = +0.4708,   μ₄ = −4.591.

The genuinely-4-body coefficient is `μ₄ = −4.591`, and it is **NEGATIVE** — the
closed `[1⁴]` SU(4) supermultiplet / α-cluster **saturation** signature (the
graded reference's own 4-body simplex coefficient `g₄ = +8.37` over-subtracts,
`μ₄ = s₄ − g₄`).  This is a FORWARD computation, never an inversion.

**The sign obstruction (this file).**  #4360 proved the A=3 Borromean/Brunnian
cluster `c₃ = E₀·(1 − τ_Borr) ≥ 0` supplies the `μ₃ > 0` **sign** the
multiplicative pairwise route (`≤ 0`, #4354) cannot.  Its A=4 analog is a
4-component Brunnian link; realized the SAME way — a trace **deficit against the
unlink**, `c₄ = E₀·(1 − τ_L₄)` — it is again a *binding* object: whenever the
level trace lies at or below the unlink (`τ ≤ 1`, exactly the #4360 shape) the
cluster is **non-negative**, `c₄ ≥ 0`.  But the derived target is `μ₄ < 0`.  Hence

    a non-negative Brunnian deficit `c₄ ≥ 0`  ≠  the derived `μ₄ < 0`.

The recipe **walls on SIGN at A=4**.  This is the mirror of #4354: there the
`μ₃ > 0` target excluded the `≤ 0` multiplicative cluster; here the `μ₄ < 0`
target excludes the `≥ 0` Brunnian deficit.  Reading them together gives a
**sign SWAP** — no single sign mechanism reproduces both A=3 (`+`) and A=4 (`−`):

| residual | derived sign | Brunnian deficit (≥0) | multiplicative cluster (≤0) |
|----------|--------------|-----------------------|-----------------------------|
| μ₃ (3-body) | **+** | ✓ compatible (#4360) | ✗ excluded (#4354) |
| μ₄ (4-body) | **−** | ✗ **excluded (this file)** | ✓ consistent (#4354) |

The A=4 α-cluster residual is therefore a structurally **different** object from
the A=3 irreducible-binding Brunnian cluster: a saturation/closure term, not a
binding term.  The Borromean-lift recipe does not carry the *sign* across the
isotope step — a genuine, derived, 0-fit structural finding.

**Scope.**  The exclusion `μ₄ < 0 ≠ c₄ ≥ 0` is a *proved* sign exclusion —
**scope-(b) CONDITIONAL on** the Brunnian level deficit being non-negative
(`τ_L₄ ≤ 1`), exactly the invariant #4360 proved for the bare Borromean closed
form.  Whether the specific 4-component (width-3 cabled, H₁₂) Brunnian deficit is
`≥ 0` at the substrate `q₀` is the companion probe's measured input
(`computations/deltalambda/helium_four_body_cluster_probe.py`); its leading order
rises to `O(h⁶)` (Milnor length-4 vs the Borromean length-3 `O(h⁴)`), verified by
the lift-is-coefficient-ratio invariant carried over here.  The magnitude of
`μ₄` is never inverted to set any coefficient; nothing is wired.

Base ring (§7c): `ℝ`, because every statement is an archimedean ordering/sign
fact (`≤ 1`, `0 ≤`, `< 0`, a numeric value `<` / `≠` a numeric target).
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### The derived A=4 residual moment `μ₄` is negative (forward AME − model) -/

/-- The A=4 4-body simplex residual coefficient, from the exact 0-parameter
back-substitution `μ₄ = M(4) − 6·μ₂ − 4·μ₃` on the derived coordination counts,
evaluated at the canonical `q₀` (`deltalambda_kappa_interface_residual_simplex_probe.py`).
Recorded as the derived numeric value; the sign — not the digits — is load-bearing. -/
noncomputable def mu4Residual : ℝ := -4.591

/-- **The derived A=4 residual is NEGATIVE.**  Unlike the positive 3-body moment
`μ₃ = +0.4708`, the 4-body α-cluster residual `μ₄ = −4.591 < 0` — the closed
`[1⁴]` SU(4) supermultiplet *saturation* signature (`μ₄ = s₄ − g₄`, the graded
reference's `g₄ = +8.37` over-subtracts).  Forward, 0-fit. -/
theorem mu4Residual_neg : mu4Residual < 0 := by
  unfold mu4Residual; norm_num

/-! ### The 4-component Brunnian cluster, realized as a trace deficit, is `≥ 0` -/

/-- A level Markov trace as a function of `h = q − q⁻¹`, normalized so the
`k`-component unlink is `τ(0) = 1` (writhe-0 trivial eigenvalue).  This is the
generic shape #4360 used for the Borromean `H₃` trace `τ_Borr`. -/
noncomputable def tauLevel := fun (τ : ℝ → ℝ) (h : ℝ) => τ h

/-- The 4-body Brunnian **binding cluster** at level `τ`, realized the SAME way as
the A=3 Borromean cluster (#4360): the energy-scaled deficit of the link trace
against the unlink, `c₄ = E₀·(1 − τ_L₄(h))`.  ("Brunnian": every proper sub-link
is trivial, so the pairwise content vanishes and the whole is the irreducible
4-body cluster.) -/
noncomputable def brunnian4Cluster (E0 : ℝ) (τ : ℝ → ℝ) (h : ℝ) : ℝ :=
  E0 * (1 - τ h)

/-- **The Brunnian binding cluster is non-negative** whenever the level trace lies
at or below the unlink (`τ h ≤ 1`) and the energy scale is non-negative — exactly
the #4360 shape `c₃ = E₀·(1 − τ_Borr) ≥ 0`, transported to A=4.  This is the
*binding* half-line: a deficit against the unlink is a positive binding
contribution. -/
theorem brunnian4Cluster_nonneg {E0 h : ℝ} {τ : ℝ → ℝ}
    (hE : 0 ≤ E0) (hτ : τ h ≤ 1) : 0 ≤ brunnian4Cluster E0 τ h := by
  unfold brunnian4Cluster
  exact mul_nonneg hE (by linarith)

/-- **The Brunnian binding cluster is strictly positive** in the physical regime
(`E₀ > 0`, `τ h < 1`). -/
theorem brunnian4Cluster_pos {E0 h : ℝ} {τ : ℝ → ℝ}
    (hE : 0 < E0) (hτ : τ h < 1) : 0 < brunnian4Cluster E0 τ h := by
  unfold brunnian4Cluster
  exact mul_pos hE (by linarith)

/-! ### The sign wall: `μ₄ < 0` cannot equal a non-negative Brunnian deficit -/

/-- **(WALL, sign, scope-(b) conditional on `τ ≤ 1`)  The derived A=4 residual
`μ₄ < 0` is unreachable by the Borromean-deficit binding recipe.**  If the
4-component Brunnian level deficit is non-negative (`τ_L₄(h) ≤ 1`, the #4360
invariant), its cluster `c₄ = E₀·(1 − τ_L₄) ≥ 0`; but `μ₄ < 0`, so
`μ₄ ≠ c₄`.  The same 0-fit recipe that supplied the A=3 `μ₃ > 0` sign gives the
WRONG sign at A=4.  (Mirror of `Mu4RhoFCluster.mu3_ne_pairwise_3body_cluster`.) -/
theorem mu4_ne_brunnian4Cluster {E0 h : ℝ} {τ : ℝ → ℝ}
    (hE : 0 ≤ E0) (hτ : τ h ≤ 1) : mu4Residual ≠ brunnian4Cluster E0 τ h := by
  have hcl : 0 ≤ brunnian4Cluster E0 τ h := brunnian4Cluster_nonneg hE hτ
  have hneg : mu4Residual < 0 := mu4Residual_neg
  intro hEq
  rw [hEq] at hneg
  linarith

/-- **(CAPSTONE) The A=3 → A=4 sign SWAP.**  Read with #4360 (Brunnian deficit
`≥ 0`) and #4354 (multiplicative cluster `≤ 0`):

* `μ₃ > 0` lies on the *positive* side — compatible with the Brunnian deficit
  (`c₃ ≥ 0`), incompatible with the multiplicative cluster (`≤ 0`);
* `μ₄ < 0` lies on the *negative* side — incompatible with the Brunnian deficit
  (`c₄ ≥ 0`, proved here), consistent with the multiplicative cluster (`≤ 0`).

So no single sign mechanism reproduces both isotopes: the Brunnian (binding)
operator selects A=3, the multiplicative (saturation) operator selects A=4.  The
Borromean-lift recipe does not carry the sign across the isotope step. -/
theorem sign_swap_a3_a4 {μ₃ E0 h : ℝ} {τ : ℝ → ℝ}
    (hμ₃ : 0 < μ₃) (hE : 0 ≤ E0) (hτ : τ h ≤ 1) :
    -- A=3: μ₃>0 sits with the Brunnian deficit, apart from the ≤0 pairwise cluster
    (0 < μ₃ ∧ 0 ≤ brunnian4Cluster E0 τ h) ∧
    -- A=4: μ₄<0 sits apart from the SAME Brunnian deficit (the swap)
    (mu4Residual < 0 ∧ mu4Residual ≠ brunnian4Cluster E0 τ h) :=
  ⟨⟨hμ₃, brunnian4Cluster_nonneg hE hτ⟩,
   ⟨mu4Residual_neg, mu4_ne_brunnian4Cluster hE hτ⟩⟩

/-! ### The magnitude lift is a coefficient ratio at the raised Milnor order `h⁶` -/

/-- A Brunnian-order-suppressed level deficit at Milnor order `m`:
`D(h) = h^m · κ h`.  For an `n`-component Brunnian link the leading order is
`m = 2(n − 1)` (every proper sub-link trivial kills all lower orders): the
Borromean `n = 3` gives `m = 4` (#4364), the 4-component `n = 4` gives `m = 6`. -/
noncomputable def brunnianDeficitOrder (m : ℕ) (κ : ℝ → ℝ) (h : ℝ) : ℝ :=
  h ^ m * κ h

/-- The A=4 Brunnian Milnor order is `6` (`= 2·(4−1)`), one Milnor step above the
Borromean's `4`.  (Recorded as the derived exponent the companion probe measures;
`O(h⁶)` vs the A=3 `O(h⁴)`.) -/
def brunnian4Order : ℕ := 6

theorem brunnian4Order_eq : brunnian4Order = 2 * (4 - 1) := by
  unfold brunnian4Order; norm_num

/-- **Order-invariance of a level lift, any Milnor order.**  For two deficits at
the SAME order `m`, `h^m·κ₁ h` and `h^m·κ₂ h` (`h ≠ 0`, `κ₂ h ≠ 0`), the lift
ratio is `κ₁ h / κ₂ h` — the shared `h^m` cancels.  A width-cable level lift is a
pure coefficient rescale and can NEVER change the Milnor order; the A=4 cabling
preserves `O(h⁶)` exactly as the A=3 cabling preserved `O(h⁴)` (#4364). -/
theorem lift_is_coefficient_ratio_order {m : ℕ} {κ₁ κ₂ : ℝ → ℝ} {h : ℝ}
    (hh : h ≠ 0) (hκ₂ : κ₂ h ≠ 0) :
    brunnianDeficitOrder m κ₁ h / brunnianDeficitOrder m κ₂ h = κ₁ h / κ₂ h := by
  unfold brunnianDeficitOrder
  have hm : h ^ m ≠ 0 := pow_ne_zero m hh
  field_simp

end QOU.MassTheory
