import Mathlib.Tactic

/-!
# Mirror-Bar Bond Cancellation and Two-Row Cap Violation Ratio (`qou-kgsx`, `qou-lr57`)

This module formalizes two algebraic identities in the nuclear binding sector:

1. **Nucleus-Independent Mirror-Bar Bond Cancellation (`qou-kgsx`)**:
   On an $A$-nucleon chain with $Z - 1$ proton-proton bonds (weight $z$), $N - 1$
   neutron-neutron bonds (weight $\bar{z}$), and one mixed proton-neutron interface
   (weight $z + d$), the bond-product factor $z^{Z-1} \bar{z}^{N-1} (z + d)$ and its
   mirror-bar image $\bar{z}^{N-1} z^{Z-1} (\bar{z} + \bar{d})$ have quotient
   $(\bar{z} + \bar{d}) / (z + d)$, completely independent of $Z$ and $N$.
   Similarly, the monomial exponent $a(Z, N) = 6 + 2(N - Z) - (Z + N - 1) = 7 - 3Z + N$
   and bond count $b(Z, N) = Z + N - 1$ satisfy the universal identity
   $a(Z, N) + a(N, Z) + 2 b(Z, N) = 12$ for all $Z, N$.

2. **Two-Row Cap Decomposition and Violation Share (`qou-lr57`)**:
   Writing a partition-summed trace as $T_{\mathrm{all}} = T_{\le 2} + T_{> 2}$, a table
   satisfying the two-row cap ($T_{> 2} = 0$) has $T_{\mathrm{all}} = T_{\le 2}$, whereas
   any table with $T_{> 2} \neq 0$ has relative excess
   $(T_{\mathrm{all}} - T_{\le 2}) / T_{\mathrm{all}} = T_{> 2} / T_{\mathrm{all}} =
   1 - T_{\le 2} / T_{\mathrm{all}}$.
-/

namespace QOU.MassTheory.MirrorBarCancellationAndTwoRowCapRatio

/-- Bond-chain weight product $z^{z_p} \bar{z}^{n_m} (z + d)$ with $z_p$ proton-proton
bonds, $n_m$ neutron-neutron bonds, and one mixed interface $z + d$. -/
noncomputable def bondChainProduct (z zbar d : ℝ) (zp nm : ℕ) : ℝ :=
  z ^ zp * zbar ^ nm * (z + d)

/-- Mirror-bar image $\bar{z}^{n_m} z^{z_p} (\bar{z} + \bar{d})$ after swapping
species counts $(z_p \leftrightarrow n_m)$ and applying bar conjugation
$(z \leftrightarrow \bar{z}, d \leftrightarrow \bar{d})$. -/
noncomputable def mirrorBarChainProduct (z zbar d dbar : ℝ) (zp nm : ℕ) : ℝ :=
  zbar ^ nm * z ^ zp * (zbar + dbar)

/-- For all bond counts $z_p, n_m \in \mathbb{N}$ and non-zero weights $z, \bar{z}, z + d$,
the mirror-bar quotient equals $(\bar{z} + \bar{d}) / (z + d)$, independent of $z_p$ and $n_m$. -/
theorem mirrorBar_quotient_independent_of_counts (z zbar d dbar : ℝ) (zp nm : ℕ)
    (hz : z ≠ 0) (hzbar : zbar ≠ 0) (hzd : z + d ≠ 0) :
    mirrorBarChainProduct z zbar d dbar zp nm / bondChainProduct z zbar d zp nm =
      (zbar + dbar) / (z + d) := by
  unfold mirrorBarChainProduct bondChainProduct
  have hzp : z ^ zp ≠ 0 := pow_ne_zero zp hz
  have hnm : zbar ^ nm ≠ 0 := pow_ne_zero nm hzbar
  have h_comm : zbar ^ nm * z ^ zp * (zbar + dbar) =
      (z ^ zp * zbar ^ nm) * (zbar + dbar) := by
    ring
  rw [h_comm]
  exact mul_div_mul_left (zbar + dbar) (z + d) (mul_ne_zero hzp hnm)

/-- Monomial exponent $a(Z, N) = 6 + 2(N - Z) - (Z + N - 1)$. -/
def monomialExpA (Z N : ℤ) : ℤ :=
  6 + 2 * (N - Z) - (Z + N - 1)

/-- Bond-count exponent $b(Z, N) = Z + N - 1$. -/
def bondCountExpB (Z N : ℤ) : ℤ :=
  Z + N - 1

/-- For all $Z, N \in \mathbb{Z}$, $a(Z, N) = 7 - 3Z + N$ and the mirror-crossed
exponent sum $a(Z, N) + a(N, Z) + 2 b(Z, N)$ equals $12$ identically. -/
theorem mirror_exponent_sum_eq_twelve (Z N : ℤ) :
    monomialExpA Z N = 7 - 3 * Z + N ∧
      monomialExpA Z N + monomialExpA N Z + 2 * bondCountExpB Z N = 12 := by
  unfold monomialExpA bondCountExpB
  have h_a : 6 + 2 * (N - Z) - (Z + N - 1) = 7 - 3 * Z + N := by
    ring
  have h_sum : (6 + 2 * (N - Z) - (Z + N - 1)) +
      (6 + 2 * (Z - N) - (N + Z - 1)) + 2 * (Z + N - 1) = 12 := by
    ring
  exact ⟨h_a, h_sum⟩

/-- Total partition-weighted sum decomposed into $\ell(\lambda) \le 2$ and
$\ell(\lambda) > 2$ sectors. -/
noncomputable def totalPartitionSum (t_le2 t_gt2 : ℝ) : ℝ :=
  t_le2 + t_gt2

/-- When the $>2$-row contribution $t_{>2}$ is non-zero and $t_{\le 2} + t_{>2} \neq 0$,
the total sum differs from the two-row sum and the relative $>2$-row share equals
$1 - t_{\le 2} / (t_{\le 2} + t_{>2})$. -/
theorem twoRowCap_violation_share_identity (t_le2 t_gt2 : ℝ)
    (h_tot : totalPartitionSum t_le2 t_gt2 ≠ 0) (h_gt2 : t_gt2 ≠ 0) :
    totalPartitionSum t_le2 t_gt2 ≠ t_le2 ∧
      t_gt2 / totalPartitionSum t_le2 t_gt2 =
        1 - t_le2 / totalPartitionSum t_le2 t_gt2 := by
  unfold totalPartitionSum at *
  have h_ne : t_le2 + t_gt2 ≠ t_le2 := by
    intro h_eq
    have h_zero : t_gt2 = 0 := by linarith
    exact h_gt2 h_zero
  have h_share : t_gt2 / (t_le2 + t_gt2) = 1 - t_le2 / (t_le2 + t_gt2) := by
    field_simp [h_tot]
    ring
  exact ⟨h_ne, h_share⟩

end QOU.MassTheory.MirrorBarCancellationAndTwoRowCapRatio
