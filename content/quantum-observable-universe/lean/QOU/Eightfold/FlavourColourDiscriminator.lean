/-
# Where a flavour-versus-colour discriminator can live, and where it cannot

The chapter's open-problem item 4 ends *"Whatever separates flavour from colour
lies elsewhere"*, after recording that the two natural invariants are blind:

* the `Sym²` gate — `Sym2GateFSTrichotomy.gate_does_not_separate_two_triples`;
* the `ℤ/3` grading —
  `TrialitySelectionRule.identification_invisible_to_selection_rule`.

This file asks whether those two failures are a coincidence or a pattern, and
answers: **a pattern, and a complete one for their whole class.** Both gates read
only *object-level* data — a dimension, a Frobenius–Schur type, a triality
class — and on that data the colour triple and the flavour triple **coincide**.
So no gate of that class can separate them, and there is nothing to be gained by
looking for a third one.

`no_object_gate_separates` is therefore a **scope-(b) structural exclusion of a
class of discriminators**, with the invariant named: equal data, equal verdict.
It is not a negative result about flavour and colour — it is a positive result
about where to look next.

## Where to look next

`some_channel_gate_separates` shows the obstruction lifts the moment the gate is
allowed to read one more thing: **which Young-symmetry channel of `V ⊗ V ⊗ V`
carries the physical state.** Colour occupies the totally antisymmetric channel
(the baryon wavefunction is `ε_{abc}`); flavour occupies the symmetric channel
for the decuplet and the mixed one for the octet. These are different `S₃`
irreps, so a gate reading the channel is not blind.

The chapter already knows this, in a different place. **Open-problem items 4 and
7 are the same question**, and item 7 is the one that names the location:
*"colour antisymmetric and spin symmetric force flavour symmetric."* Item 4 says
the answer lies elsewhere; item 7 is the elsewhere.

## The circularity this does NOT escape — read before citing

Assigning colour the antisymmetric channel is an **input, not a derivation.**
Item 7 states plainly that the chapter derives neither the spin factor nor the
colour antisymmetry. So `some_channel_gate_separates` does not establish that
flavour and colour differ; it establishes that *if* the channel assignment is
supplied, a gate can see the difference — whereas no amount of object data ever
could.

The honest summary is that the discriminator is **located, not established**.
What is genuinely settled here is the negative half, and the negative half is
what redirects the search: stop looking for object invariants.
-/
import QOU.Eightfold.Sym2GateFSTrichotomy
import QOU.Eightfold.TrialitySelectionRule

namespace QOU.Eightfold.FlavourColourDiscriminator

open QOU.Eightfold.Sym2GateFSTrichotomy (FSType)
open QOU.Eightfold.TrialitySelectionRule (triality)

/-- The object-level data this chapter's gates actually read: a dimension, a
Frobenius–Schur type, and a triality class. Both the `Sym²` gate (at dimension
three, `gate_forces_complex_of_dim_three` shows its verdict is exactly the
Frobenius–Schur type) and the `ℤ/3` selection rule factor through this. -/
structure ObjectData where
  dim : ℕ
  fs : FSType
  tri : ZMod 3
  deriving DecidableEq

/-- The colour triple, as the `ℂ³` summand of `Im(𝕆) = ℝ ⊕ ℂ³`: its complex
dimension is what remains of the seven imaginary directions after the stabilised
real line is removed, halved.

`FSType.complex` is the Günaydin–Gürsey input (bean `qou-8pl3`, gap (i)) — a
citation here, not a derivation. -/
def colourTripleData : ObjectData :=
  { dim := (7 - 1) / 2, fs := .complex, tri := triality 1 0 }

/-- The flavour triple, as the `SU(3)` fundamental with Dynkin label `(1,0)`,
dimension by the Weyl formula `(a+1)(b+1)(a+b+2)/2`.

Here `FSType.complex` **is** derived: triality `1 ≠ 0`, so the fundamental is not
self-dual (`fundamental_not_selfDual`), hence complex type. -/
def flavourTripleData : ObjectData :=
  { dim := (1 + 1) * (0 + 1) * (1 + 0 + 2) / 2, fs := .complex, tri := triality 1 0 }

/-- The two triples carry **identical** object-level data. The dimensions arrive
by genuinely different routes — `(7-1)/2` from the octonion decomposition,
`2·1·3/2` from the Weyl dimension formula — and agree at 3. -/
theorem colour_eq_flavour_data : colourTripleData = flavourTripleData := by decide

/-- **The class exclusion.** A gate is a verdict-valued function of what it can
read. No gate that reads only object-level data separates the colour triple from
the flavour triple — not the two already tried, and not any third.

This is why the `Sym²` and `ℤ/3` failures were not repairable: they were not
failures of those two constructions, but of the class. -/
theorem no_object_gate_separates (gate : ObjectData → Bool) :
    gate colourTripleData = gate flavourTripleData := by
  rw [colour_eq_flavour_data]

/-- The same, for an invariant valued in an arbitrary type rather than a
two-valued verdict — nothing about the exclusion depends on the gate being a
yes/no test. -/
theorem no_object_invariant_separates {I : Type*} (inv : ObjectData → I) :
    inv colourTripleData = inv flavourTripleData := by
  rw [colour_eq_flavour_data]

/-- Dimension of the symmetric cube of a `d`-dimensional space. -/
def sym3Dim (d : ℕ) : ℕ := (d + 2).choose 3

/-- Dimension of the alternating cube of a `d`-dimensional space. -/
def alt3Dim (d : ℕ) : ℕ := d.choose 3

/-- **The next moves are already dead.** After `Sym²` fails, the natural
instinct is to try the next tensor functor — `Sym³`, or `Λ³` (whose singlet is
the colour `ε_{abc}`, which makes it look especially promising). Both dimensions
are functions of `dim V` alone, so a gate reading either is a gate reading
`ObjectData`, and `no_object_gate_separates` already covers it.

Checked concretely rather than argued: `Sym³` gives `10` for both triples and
`Λ³` gives `1` for both.

This is what makes the class exclusion worth having. It does not merely record
two past failures — it forecloses the entire "try another tensor construction on
`V`" family without running any of them. -/
theorem tensor_cube_gates_also_blind :
    sym3Dim colourTripleData.dim = sym3Dim flavourTripleData.dim
    ∧ alt3Dim colourTripleData.dim = alt3Dim flavourTripleData.dim := by
  constructor <;> decide

/-- The Young-symmetry channel of `V ⊗ V ⊗ V`, indexed by the partitions of 3 —
equivalently by the irreps of `S₃`. -/
inductive Channel3
  /-- `λ = (3)`, the trivial `S₃`-irrep: the decuplet's flavour channel. -/
  | symmetric
  /-- `λ = (2,1)`, the standard irrep: the octet's flavour channel. -/
  | mixed
  /-- `λ = (1³)`, the sign irrep: the colour channel, `ε_{abc}`. -/
  | antisymmetric
  deriving DecidableEq, Repr

/-- Colour occupies the totally antisymmetric channel: the baryon colour
wavefunction is `ε_{abc}`. **Input, not derived here** — see the header. -/
def colourChannel : Channel3 := .antisymmetric

/-- The decuplet's flavour channel is the symmetric one. -/
def flavourDecupletChannel : Channel3 := .symmetric

/-- The octet's flavour channel is the mixed one. -/
def flavourOctetChannel : Channel3 := .mixed

/-- The colour channel differs from **both** flavour channels, so the distinction
is not an artefact of which flavour multiplet is chosen. -/
theorem colourChannel_ne_flavourChannels :
    colourChannel ≠ flavourDecupletChannel ∧ colourChannel ≠ flavourOctetChannel := by
  constructor <;> decide

/-- **The obstruction lifts.** A gate allowed to read the Young-symmetry channel
in addition to the object data does separate the two — exhibited concretely, so
this is a construction and not an existence claim.

Read together with `no_object_gate_separates`: the channel is not merely *a*
place a discriminator could live, it is the first place one can live at all. -/
theorem some_channel_gate_separates :
    ∃ gate : ObjectData × Channel3 → Bool,
      gate (colourTripleData, colourChannel)
        ≠ gate (flavourTripleData, flavourDecupletChannel) := by
  refine ⟨fun p => p.2 == Channel3.antisymmetric, ?_⟩
  decide

/-- The two halves as one statement: object data is never enough, and the channel
is enough. This is the file's content in a single type. -/
theorem separation_requires_the_channel :
    (∀ gate : ObjectData → Bool, gate colourTripleData = gate flavourTripleData)
    ∧ (∃ gate : ObjectData × Channel3 → Bool,
        gate (colourTripleData, colourChannel)
          ≠ gate (flavourTripleData, flavourDecupletChannel)) :=
  ⟨no_object_gate_separates, some_channel_gate_separates⟩

end QOU.Eightfold.FlavourColourDiscriminator
