/-!
# Chain Mirror Splitting and Charge Symmetry (`qou-6k8b`)

This module formalizes the exact algebraic laws governing mirror-nucleus pair-binding
splitting in the nearest-neighbour chain decomposition (`qou-6k8b`):

1. **Chain pair-binding decomposition (`chainBinding`):**
   For a nuclide `(Z, N)` with `Z >= 1` and `N >= 1`, the nearest-neighbour chain model
   decomposes the pair-layer binding energy into `(Z - 1)` proton-proton bonds `Bpp`,
   one cross-chain bond `Bpn`, and `(N - 1)` neutron-neutron bonds `Bnn`:
   `chainBinding(Bpp, Bpn, Bnn, Z, N) = (Z - 1) * Bpp + Bpn + (N - 1) * Bnn`.

2. **Exact mirror pair-binding difference (`mirror_pair_binding_diff_equals_like_bond_diff`):**
   Between mirror nuclides `(Z, N)` and `(N, Z)`, the cross-bond `Bpn` cancels identically,
   leaving the exact linear relation:
   `chainBinding(Bpp, Bpn, Bnn, Z, N) - chainBinding(Bpp, Bpn, Bnn, N, Z) = (N - Z) * (Bnn - Bpp)`.

3. **A = 3 mirror splitting and charge symmetry (`a3_mirror_splitting_vanishes_iff_charge_symmetric_like_bonds`):**
   Specializing to the `A = 3` mirror pair `3H = (Z=1, N=2)` and `3He = (Z=2, N=1)`,
   the chain pair-binding difference equals `Bnn - Bpp` and vanishes if and only if
   like-nucleon bonds satisfy charge symmetry (`Bnn = Bpp`).

4. **Sign-pattern dichotomy in determinant-form mirror splitting (`det_form_mirror_splitting_sign_pattern`):**
   In the sign-weighted determinant bond model `B_ab = s_ab * K` with common positive
   prefactor `K`, opposite signs `s_nn = 1, s_pp = -1` double the like-bond scale (`2 * K`),
   whereas matching signs (`s_nn = s_pp = 1` or `s_nn = s_pp = -1`) yield exact charge
   symmetry (`0`) prior to electromagnetic and quark-mass corrections.
-/

namespace QOU.MassTheory.ChainMirrorSplittingChargeSymmetry

/-- Nearest-neighbour chain pair-binding energy `(Z - 1) * Bpp + Bpn + (N - 1) * Bnn`. -/
def chainBinding (Bpp Bpn Bnn Z N : Int) : Int :=
  (Z - 1) * Bpp + Bpn + (N - 1) * Bnn

/-- Mirror pair-binding difference between `(Z, N)` and `(N, Z)`. -/
def mirrorChainDiff (Bpp Bpn Bnn Z N : Int) : Int :=
  chainBinding Bpp Bpn Bnn Z N - chainBinding Bpp Bpn Bnn N Z

/-- Sign-weighted determinant mirror splitting `(s_nn - s_pp) * K`. -/
def detMirrorSplit (s_nn s_pp K : Int) : Int :=
  (s_nn - s_pp) * K

/-- Between mirror nuclides `(Z, N)` and `(N, Z)`, the cross-bond `Bpn` cancels
    identically and the pair-binding difference equals `(N - Z) * (Bnn - Bpp)`
    only when evaluated on the mirror pair `(Z, N)` vs `(N, Z)` (`qou-6k8b`). -/
theorem mirror_pair_binding_diff_equals_like_bond_diff
    (Bpp Bpn Bnn Z N : Int) :
    mirrorChainDiff Bpp Bpn Bnn Z N = (N - Z) * (Bnn - Bpp) ∧
    mirrorChainDiff Bpp Bpn Bnn Z Z = 0 := by
  have hdiff : mirrorChainDiff Bpp Bpn Bnn Z N =
      ((Z - 1) * Bpp + Bpn + (N - 1) * Bnn) - ((N - 1) * Bpp + Bpn + (Z - 1) * Bnn) := by
    unfold mirrorChainDiff chainBinding
    rfl
  have hbpn : ((Z - 1) * Bpp + Bpn + (N - 1) * Bnn) - ((N - 1) * Bpp + Bpn + (Z - 1) * Bnn) =
      (N - Z) * Bnn - (N - Z) * Bpp := by
    have h1 : (Z - 1) * Bpp - (N - 1) * Bpp = -((N - Z) * Bpp) := by
      have hsub : (Z - 1) - (N - 1) = -(N - Z) := by omega
      calc
        (Z - 1) * Bpp - (N - 1) * Bpp = ((Z - 1) - (N - 1)) * Bpp := by
          rw [← Int.sub_mul]
        _ = (-(N - Z)) * Bpp := by rw [hsub]
        _ = -((N - Z) * Bpp) := by rw [Int.neg_mul]
    have h2 : (N - 1) * Bnn - (Z - 1) * Bnn = (N - Z) * Bnn := by
      have hsub : (N - 1) - (Z - 1) = N - Z := by omega
      calc
        (N - 1) * Bnn - (Z - 1) * Bnn = ((N - 1) - (Z - 1)) * Bnn := by
          rw [← Int.sub_mul]
        _ = (N - Z) * Bnn := by rw [hsub]
    omega
  have hfactor : (N - Z) * Bnn - (N - Z) * Bpp = (N - Z) * (Bnn - Bpp) := by
    rw [Int.mul_sub]
  have hself : mirrorChainDiff Bpp Bpn Bnn Z Z = 0 := by
    unfold mirrorChainDiff
    omega
  exact ⟨by omega, hself⟩

/-- For the `A = 3` mirror pair `3H = (Z=1, N=2)` and `3He = (Z=2, N=1)`,
    the chain pair-binding difference equals `Bnn - Bpp` and vanishes if and only if
    like-nucleon bonds are charge-symmetric (`Bnn = Bpp`) (`qou-6k8b`). -/
theorem a3_mirror_splitting_vanishes_iff_charge_symmetric_like_bonds
    (Bpp Bpn Bnn : Int) :
    mirrorChainDiff Bpp Bpn Bnn 1 2 = Bnn - Bpp ∧
    (mirrorChainDiff Bpp Bpn Bnn 1 2 = 0 ↔ Bnn = Bpp) := by
  have h3h : chainBinding Bpp Bpn Bnn 1 2 = Bpn + Bnn := by
    unfold chainBinding
    omega
  have h3he : chainBinding Bpp Bpn Bnn 2 1 = Bpp + Bpn := by
    unfold chainBinding
    omega
  have hdiff : mirrorChainDiff Bpp Bpn Bnn 1 2 = Bnn - Bpp := by
    unfold mirrorChainDiff
    omega
  have hiff : mirrorChainDiff Bpp Bpn Bnn 1 2 = 0 ↔ Bnn = Bpp := by
    rw [hdiff]
    omega
  exact ⟨hdiff, hiff⟩

/-- In the determinant bond model `B_ab = s_ab * K`, opposite like-bond signs
    `(s_nn = 1, s_pp = -1)` produce `2 * K` splitting whereas matching signs
    `(1, 1)` or `(-1, -1)` produce zero splitting (`qou-6k8b`). -/
theorem det_form_mirror_splitting_sign_pattern (K : Int) :
    detMirrorSplit 1 (-1) K = 2 * K ∧
    detMirrorSplit 1 1 K = 0 ∧
    detMirrorSplit (-1) (-1) K = 0 ∧
    (K > 0 → detMirrorSplit 1 (-1) K > detMirrorSplit 1 1 K) := by
  have hopp : detMirrorSplit 1 (-1) K = 2 * K := by
    unfold detMirrorSplit
    omega
  have hpos_same : detMirrorSplit 1 1 K = 0 := by
    unfold detMirrorSplit
    omega
  have hneg_same : detMirrorSplit (-1) (-1) K = 0 := by
    unfold detMirrorSplit
    omega
  have hgt : K > 0 → detMirrorSplit 1 (-1) K > detMirrorSplit 1 1 K := by
    intro hK
    rw [hopp, hpos_same]
    omega
  exact ⟨hopp, hpos_same, hneg_same, hgt⟩

end QOU.MassTheory.ChainMirrorSplittingChargeSymmetry
