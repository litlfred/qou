import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.EWHiggsTorusLinkTriplet — the electroweak identification conjecture lattice

The physical identification `W↔T(2,4)`, `Z↔T(2,6)`, `H↔T(2,8)` is **not**
one monolithic conjecture. It decomposes into an honest §3b conjecture
lattice (primary/dependent per §3b-tax, dependency threaded through
`[instance]` binders) sitting on top of a **provable** genus / enumeration /
far-commuting / bar-parity core.

LaTeX label (of the top node): `conj:electroweak-higgs-torus-link-triplet`.

## The lattice (narrowed 2026-07-05)

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| `EWSelectionPrinciple` | primary   | — | **physics postulate only**: EW carriers *are* the sub-saturating even-twist links (`0 < g < 4`) |
| `EWSectorEnumeration`  | dependent | C1 | those carriers are exactly `{T(2,4),T(2,6),T(2,8)}` |
| `EWSectorAssignment`   | primary   | — | **the single sector postulate** replacing charge+spin: `H` singlet (`A₊`), `W±,Z` doublets (`A₋`) |
| `EWHiggsTorusLinkTriplet` | dependent | C1, sector | the full identification |

**What is now PROVED (no longer conjectural).**

* The **enumeration / far-commuting minimality** — that three pairwise
  far-commuting even-twist generators fit minimally in `B₆` at `(1,3,5)` and
  that the sub-saturating window is exactly `{T(2,4),T(2,6),T(2,8)}` — is
  `thm:ew-triplet-far-commuting-minimal` + `prop:electroweak-triplet-bring-embedding`
  (both sorry-free). So `EWSelectionPrinciple` carries **only** the physics
  selection postulate (EW sector ↔ this proved set), *not* the enumeration.
* **Charge and spin** are `thm:ew-triplet-charge-spin-from-involution`
  (sorry-free, conditional on the sector postulate): via the spin involution
  of `def:spin-involution`, `H ∈ A₊ ⇒` scalar+neutral, `W± ∈ A₋ ⇒` vector
  `T₃=±1`, `Z ∈ A₋` vector neutral via Weinberg mixing. The **former C3
  (charge) and C4 (spin) — previously two independent open primary
  conjectures — are now proved consequences** of the single sector postulate
  `EWSectorAssignment`. They are removed from the lattice as independent nodes.

The irreducible residual is therefore just **C1 (selection)** — strongly
grounded in the corpus genus-4 saturation story — and the **sector
assignment** (which link sits in which `σ`-sector), together with the bare
particle-label map. Charge and spin no longer appear as open gaps.

`sorry`-free: this file declares only conjecture **classes** (no `instance`
fabricated to "close" them) plus the `crossings` data; there are no `sorry`s
and no vacuous `: True` bodies.

## References

- [leitner2026] particle-interactions/electroweak-higgs-torus-link-triplet
- `thm:ew-triplet-far-commuting-minimal` (far-commuting minimality + enumeration, proved)
- `prop:electroweak-triplet-bring-embedding` (genus/embedding core, proved)
- `thm:ew-triplet-charge-spin-from-involution` (charge+spin from the sector postulate, proved)
- `def:spin-involution` (the `σ` spin grading `A = A₊ ⊕ A₋`)
-/

namespace QOU.ParticleInteractions

/-! ## The conjecture lattice (formal §3b classes)

The Seifert genus of `T(2, 2k)` is `k - 1` and `g(Σ₄) = 4`; both are
Lean-proved in `prop:electroweak-triplet-bring-embedding`, and the
far-commuting `n = 6` minimality in `thm:ew-triplet-far-commuting-minimal`.
Here the raw `k - 1` / `4` is used inline so this file stays self-contained. -/

/-- **C1 (PRIMARY) — electroweak selection postulate.**

    The electroweak carrier sector consists of the *nontrivial, strictly
    sub-saturating* even-twist 2-component torus links: those with Seifert
    genus `g` in the window `0 < g < 4 = g(Σ₄)`, the sub-saturating complement
    of the genus-4-**saturating** carriers `{T(2,9), T(3,5)}` (corpus:
    `genus-filtration-ideal`).

    **This class now carries ONLY the physics selection postulate** — the
    claim that the electroweak sector *is* realised by this window. The
    *enumeration* of the window (that it is exactly `{T(2,4),T(2,6),T(2,8)}`,
    `k ∈ {2,3,4}`) and the far-commuting minimality are no longer part of this
    conjecture: they are the proved `thm:ew-triplet-far-commuting-minimal` and
    `prop:electroweak-triplet-bring-embedding`. The field carries the window
    membership as a parameter-quantified predicate, not the conclusion. -/
-- @conjecture: primary
class EWSelectionPrinciple where
  /-- Carrier predicate on the twist parameter `k` of `T(2, 2k)`. -/
  isCarrier : ℕ → Prop
  /-- Every carrier link is nontrivial (`genus = k-1 > 0`) and strictly
      below the genus-4 saturation (`genus < 4`). -/
  subSaturating : ∀ k, isCarrier k → 0 < k - 1 ∧ k - 1 < 4
  /-- The window is realised (non-vacuous): the `k = 2` (`W±`) link is a
      carrier. -/
  carrier_realised : isCarrier 2

/-- **C2 (DEPENDENT on C1) — sector enumeration.**

    Given the selection postulate, the electroweak carriers are exactly
    `k ∈ {2, 3, 4}`. The forward inclusion `carrier ⊆ {2,3,4}` follows from
    C1's window bound (proved as `ew_enumeration` /
    `sub_saturating_enumeration`); the conjectural content here is only the
    *reverse* inclusion — that all three are realised as carriers. -/
-- @conjecture: dependent (on EWSelectionPrinciple)
class EWSectorEnumeration [EWSelectionPrinciple] where
  /-- The carrier set is exactly `{2, 3, 4}`. -/
  carriers_eq : ∀ k, EWSelectionPrinciple.isCarrier k ↔ (k = 2 ∨ k = 3 ∨ k = 4)

/-- **C-sector (PRIMARY) — the single sector-assignment postulate.**

    This class **replaces the former C3 (charge) and C4 (spin) primary
    conjectures**. It is the one residual physics input beyond selection: the
    assignment of each carrier to a `σ`-spin-involution sector
    (`def:spin-involution`) — the spin-singlet `A₊` (bar-even, neutral) or the
    spin-doublet `A₋` (bar-odd, charged). Once this assignment is fixed, charge
    and spin are **derived**, not postulated: this is the sorry-free
    `thm:ew-triplet-charge-spin-from-involution`
    (`H ∈ A₊ ⇒` scalar+neutral; `W± ∈ A₋ ⇒` vector, `T₃=±1`; `Z ∈ A₋` vector,
    neutral via Weinberg mixing).

    Twist convention: `k = 2 ↔ W`, `k = 3 ↔ Z`, `k = 4 ↔ H`.

    **The `t3Label` field is a FREE LABEL, not forced (honest, 2026-07-05).**
    Which of the two *vector* slots (`k = 2 ↔ σ₁⁴` or `k = 3 ↔ σ₃⁶`) hosts the
    *charged* carrier `W±` (`|t₃| = 1`) versus the neutral `Z` (`t₃ = 0`) is
    **not** fixed by any proved crossing→charge principle. The corpus
    crossing→charge map `def:coulomb-charge` (`Q = ½·writhe`) evaluated on the
    all-positive braid `σ₁^{2k}` gives `Q(T(2,2k)) = k > 0` for *every* carrier,
    so it makes all three charged and cannot select the neutral slot; the
    `writhe → Y` map is falsified, and the one map that survives that audit,
    `writhe → I₃` (`2·I₃ = writhe`), *also* fails here — on the all-positive
    carriers it gives `2·I₃ = 2k`, nonzero on both vector slots, so it too
    yields no neutral slot (`writheI3_does_not_select_neutral_slot` in
    `thm:ew-triplet-charge-spin-from-involution`;
    `2026-06-02-u1-hypercharge-assignment.md`).
    The assignment `t3Label 2 = 1` (`W` at the lower crossing `σ₁⁴`) below is the
    paper's *choice*, consistent with the mass ordering `4 < 6 < 8` (necessary,
    not sufficient); its underdetermination is proved as `which_slot_is_W_free`
    in `thm:ew-triplet-charge-spin-from-involution`. What *would* force it is a
    genuine crossing/linking → `T₃` map singling out the `Z` slot — an open
    input the framework does not yet supply. -/
-- @conjecture: primary
class EWSectorAssignment where
  /-- Spin sector of the carrier of twist `k`: `true` = singlet (`A₊`),
      `false` = doublet (`A₋`). -/
  isSinglet : ℕ → Bool
  /-- `H` (`k = 4`) is the bar-even self-dual singlet. -/
  higgs_singlet : isSinglet 4 = true
  /-- `W` (`k = 2`) is a bar-odd doublet. -/
  w_doublet : isSinglet 2 = false
  /-- `Z` (`k = 3`) is a bar-odd doublet (neutral via mixing, not via `A₊`). -/
  z_doublet : isSinglet 3 = false
  /-- Doubled isospin `2·T₃` label of the carrier of twist `k`. This is the
      **free label** (see the class docstring): no proved crossing→charge
      principle forces which vector slot is charged. -/
  t3Label : ℕ → ℤ
  /-- `W` (`k = 2`) is the charged member — the paper's free choice of the
      charged vector slot (mirror `t3Label 3 = 1` is equally admissible). -/
  w_charged : t3Label 2 = 1
  /-- `Z` (`k = 3`) is neutral — via the Weinberg `(W³, B) → (Z, γ)` mixing, not
      via bar-even membership. -/
  z_neutral : t3Label 3 = 0
  /-- `H` (`k = 4`) is the neutral singlet. -/
  higgs_neutral : t3Label 4 = 0

/-- **C_top (DEPENDENT on C1, C-sector) — the full electroweak identification.**

    `W ↔ T(2,4)`, `Z ↔ T(2,6)`, `H ↔ T(2,8)`: crossings `(4, 6, 8)`, with the
    spin sectors supplied by the (open) sector postulate `EWSectorAssignment`.
    Charge and spin themselves are *not* carried here as conjectural fields —
    they are the proved `thm:ew-triplet-charge-spin-from-involution`. This top
    node rests on the conjectural selection principle (C1) and the sector
    postulate, so it is a *dependent* conjecture, honestly carrying both as
    `[instance]` binders. -/
-- @conjecture: dependent (on EWSelectionPrinciple, EWSectorAssignment)
class EWHiggsTorusLinkTriplet
    [EWSelectionPrinciple] [EWSectorAssignment] where
  /-- Crossing counts of the `(W, Z, H)` carrier links. -/
  crossings : Fin 3 → ℕ
  /-- The identification: crossings `(4, 6, 8)`, with sectors `W, Z` doublets
      and `H` singlet supplied by `EWSectorAssignment` (whence, via
      `thm:ew-triplet-charge-spin-from-involution`, spins `(1,1,0)` and charges
      `(±1, 0, 0)`). -/
  identification :
    crossings 0 = 4 ∧ crossings 1 = 6 ∧ crossings 2 = 8 ∧
    EWSectorAssignment.isSinglet 2 = false ∧
    EWSectorAssignment.isSinglet 3 = false ∧
    EWSectorAssignment.isSinglet 4 = true

end QOU.ParticleInteractions
