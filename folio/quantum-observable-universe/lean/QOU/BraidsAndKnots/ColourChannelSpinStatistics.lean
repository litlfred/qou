import Mathlib.GroupTheory.Perm.Sign
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Perm
import Mathlib.Tactic.DeriveFintype

/-!
# QOU.SchurWeyl.ColourChannelSpinStatistics — which `S₃` channel colour can occupy

Bean `qou-qs4c` (epic `qou-qs0e`). Audit:
`docs/audits/2026-11-15-quark-factor-relations-and-colour-channel.md`.

## The question

A three-quark state carries an `S₃` action on its three strands, and in a tensor-factor
picture `colour ⊗ spin ⊗ flavour ⊗ space` each factor carries its own `S₃` channel
`λ ∈ {(3), (2,1), (1³)}`. Fermi statistics asks that the **product** contain the sign
representation. The question in `qou-qs4c` is whether the **colour** factor is forced into
the totally antisymmetric channel `(1³)`.

## What this file proves (pure representation theory of `S₃`, no physics input)

The three irreducible characters of `S₃ = Equiv.Perm (Fin 3)` are written from Mathlib's own
data: `sym = 1`, `anti = Equiv.Perm.sign`, and `mixed = (#fixed points) − 1` (the character of
the permutation representation minus the trivial one). `chars_orthonormal` checks that the
three are orthonormal for `⟨χ, ψ⟩ = (1/|G|) Σ_g χ(g) ψ(g)`; there are three conjugacy classes,
so they are the complete set of irreducible characters.

`signMult c s f x` is `|G|` times the multiplicity of the sign representation in
`c ⊗ s ⊗ f ⊗ x`. The theorems:

* `signMult_anti` — with colour in `(1³)` and space in `(3)`, the sign multiplicity of the
  product is `1` when the spin channel equals the flavour channel and `0` otherwise
  (`χ_{(1³)} χ_λ = χ_{λ'}` and real characters). This is the `SU(6)` `56` structure.
* `colour_channel_forced` — **only** colour `(1³)` admits a state whose spin, flavour and space
  channels are all `(3)`. With colour `(3)` or `(2,1)` the multiplicity is `0`.
* `no_groundstate_flavour_singlet` — with colour `(1³)`, space `(3)` and the spin channel in a
  level-2 channel (`(3)` or `(2,1)`, i.e. one with at most two rows), the flavour channel
  `(1³)` has multiplicity `0`.

## What it does NOT prove, so read the scope

The Lean is a statement about `S₃` characters. Reading it as "the colour channel is `(1³)`"
needs three PHYSICAL premises, none of which is in the Lean:

1. the three-quark state carries a tensor product of four `S₃` actions (colour, spin, flavour,
   space). Whether the substrate supplies a separate colour factor at all is OPEN; the Hecke
   word of a single three-strand braid carries ONE `S₃` action, not four;
2. Fermi statistics: the full product lies in the sign representation;
3. a ground state with symmetric spatial channel `(3)` and spin and flavour both `(3)` exists.
   That is the `Δ⁺⁺(1232)` (`uuu`, spin `3/2`), an EMPIRICAL input at the comparison boundary.

Given 1-3, `colour_channel_forced` settles the colour channel as `(1³)`; this is Greenberg's
1964 argument written as a finite character computation. Separately, the level-2 Wenzl weight
of `(1³)` is zero (`QOU.SchurWeyl.WenzlWeightLevelR.wenzlWeight_eq_zero_iff`, `w_μ = 0 ⟺
ℓ(μ) > r`), so a convention-D channel cannot host colour; colour needs a level `r ≥ 3` factor.

## Base ring (§7c)

Integer-valued characters over `ℤ`; no ordering, no `ℝ`.

LaTeX label: `prop:colour-channel-spin-statistics`
-/

namespace QOU.SchurWeyl.ColourChannelSpinStatistics

/-- The three `S₃` channels, labelled by partitions of `3`. -/
inductive Channel
  | sym    -- λ = (3)
  | mixed  -- λ = (2,1)
  | anti   -- λ = (1³)
  deriving DecidableEq, Fintype, Repr

open Channel

/-- Number of fixed points of a permutation of `Fin 3`. -/
def fixedPts (g : Equiv.Perm (Fin 3)) : ℤ :=
  ((Finset.univ.filter fun i : Fin 3 => g i = i).card : ℤ)

/-- The irreducible character of `S₃` labelled by a channel. -/
def chi : Channel → Equiv.Perm (Fin 3) → ℤ
  | sym,   _ => 1
  | mixed, g => fixedPts g - 1
  | anti,  g => (Equiv.Perm.sign g : ℤ)

/-- `|S₃|` times the inner product `⟨χ_a, χ_b⟩`. -/
def gram (a b : Channel) : ℤ := ∑ g : Equiv.Perm (Fin 3), chi a g * chi b g

/-- The three characters are orthonormal: `|S₃| · ⟨χ_a, χ_b⟩ = 6 δ_{ab}`. -/
theorem chars_orthonormal (a b : Channel) : gram a b = if a = b then 6 else 0 := by
  cases a <;> cases b <;> decide

/-- Dimensions (character values at the identity) are `1, 2, 1`, and `Σ dim² = |S₃|`. -/
theorem dims : chi sym 1 = 1 ∧ chi mixed 1 = 2 ∧ chi anti 1 = 1 ∧
    (chi sym 1) ^ 2 + (chi mixed 1) ^ 2 + (chi anti 1) ^ 2 = 6 := by decide

/-- `|S₃|` times the multiplicity of the sign representation in
`colour ⊗ spin ⊗ flavour ⊗ space`. -/
def signMult (c s f x : Channel) : ℤ :=
  ∑ g : Equiv.Perm (Fin 3), chi c g * chi s g * chi f g * chi x g * chi anti g

/-- Colour `(1³)`, space `(3)`: the sign multiplicity is `1` exactly when the spin channel
equals the flavour channel. -/
theorem signMult_anti (s f : Channel) :
    signMult anti s f sym = if s = f then 6 else 0 := by
  cases s <;> cases f <;> decide

/-- **Only colour `(1³)` admits spin `(3)`, flavour `(3)`, space `(3)`.** -/
theorem colour_channel_forced (c : Channel) :
    signMult c sym sym sym ≠ 0 ↔ c = anti := by
  cases c <;> decide

/-- With colour `(1³)` and space `(3)`, a spin channel in `{(3), (2,1)}` (at most two rows,
i.e. a level-2 channel) never pairs with flavour `(1³)`: no ground-state flavour singlet. -/
theorem no_groundstate_flavour_singlet (s : Channel) (hs : s ≠ anti) :
    signMult anti s anti sym = 0 := by
  cases s <;> simp_all [signMult_anti]

/-- With colour `(2,1)` (the alternative non-singlet channel), spin `(3)` and space `(3)`, the
flavour channel must be `(2,1)`; flavour `(3)` (the `Δ⁺⁺` flavour channel) is excluded. -/
theorem mixed_colour_excludes_symmetric_flavour :
    signMult mixed sym sym sym = 0 ∧ signMult mixed sym mixed sym = 6 := by
  decide

end QOU.SchurWeyl.ColourChannelSpinStatistics
