import Mathlib.Tactic

/-!
# QOU.Molecular.ElectronShellCapacity

**Canonical declaration** for content block at
[`quantum-observable-universe/molecular-construction/electron-shell-braid-capacity.ts`](quantum-observable-universe/molecular-construction/electron-shell-braid-capacity.ts).

Formalises the manuscript **definition**: in the atomic braid `𝒜(Z, N)`
each electron is a trefoil `T_{2,3}` Hopf-linked to the nuclear core; a
*bonding site* is a position an electron may occupy, and the *shell
capacity* at a level is the number of such sites, fixed by the electron
arrangement that minimises the Faddeev functional `Φ₁`. The structure
below bundles exactly that data (§7c: `Φ₁` is the archimedean
specialisation over `ℝ`; the combinatorial counts stay in `ℕ`).
-/

namespace QOU.Molecular

/-- Shell-capacity data for an atomic braid `𝒜(Z, N)`.

    A `definition` carrier: it names the constructions the manuscript
    definition introduces (bonding-site counts, the `Φ₁` contribution per
    shell, the shell capacity) together with the two properties the
    definition asserts — capacity *is* the bonding-site count, and shells
    fill in order of increasing `Φ₁`. -/
structure ElectronShellCapacity where
  /-- Electron (equivalently proton) count `Z`. -/
  Z : ℕ
  /-- Neutron count `N`. -/
  N : ℕ
  /-- Number of bonding sites available at shell level `n`. -/
  bondingSites : ℕ → ℕ
  /-- Faddeev `Φ₁` contribution of an electron placed at shell level `n`. -/
  phi1 : ℕ → ℝ
  /-- Shell capacity at level `n`. -/
  shellCapacity : ℕ → ℕ
  /-- Definitional identity: the capacity at a level is its bonding-site
      count (manuscript: "the shell capacity … is the number of bonding
      sites available at each shell level"). -/
  capacity_eq_bondingSites : ∀ n, shellCapacity n = bondingSites n
  /-- Shells fill in order of increasing `Φ₁` contribution (manuscript:
      "an atom … fills shells in order of increasing `Φ₁` contribution"). -/
  fillOrderMonotone : Monotone phi1

-- Ref: [manuscript] quantum-observable-universe/molecular-construction/electron-shell-braid-capacity.ts

/-- Total electron capacity over shell levels `0, …, L-1`: the number of
    bonding sites the atom offers up to level `L`. -/
def ElectronShellCapacity.capacityUpTo (A : ElectronShellCapacity) (L : ℕ) : ℕ :=
  (Finset.range L).sum A.shellCapacity

/-- The capacity count is carried by the definitional identity: summing
    `shellCapacity` over the shell levels equals summing `bondingSites`. -/
theorem ElectronShellCapacity.capacityUpTo_eq_bondingSites
    (A : ElectronShellCapacity) (L : ℕ) :
    A.capacityUpTo L = (Finset.range L).sum A.bondingSites := by
  unfold ElectronShellCapacity.capacityUpTo
  exact Finset.sum_congr rfl (fun n _ => A.capacity_eq_bondingSites n)

end QOU.Molecular
