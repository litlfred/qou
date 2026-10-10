import QOU.BraidsAndKnots.S5SO3FiberAction

/-!
# The canonical class-angle bijection: A₅ irreps → icosahedral conjugacy-class angles

The s5-so3 keystone's angle half asks for the map from the five A₅ irreps
`{A, T₁, T₂, G, H}` to the five icosahedral rotation **conjugacy-class angles**
`{0°, 72°, 120°, 144°, 180°}` (the orders of `I ⊂ SO(3)`: identity, 5-fold, 3-fold, 5-fold,
2-fold). The merged geometric build (`BringFiberActionInstance.lean`, PR #3093) discharges
`BringFiberAction.five_distinct_classes` with the **continuous Reeb phases**
`θ_λ = arccos(χ_λ(C₅)/dim_λ) ∈ {0°, 57.4°, 90°, 101.9°, 104.5°}` — distinct, but **not** the
icosahedral class angles. This file pins the **canonical class-angle bijection** and proves it is
**uniquely forced** by three structural properties of the A₅ character table.

## The A₅ character table (rows = irrep, cols = class `[e, 2A, 3A, 5A, 5B]`)

| irrep | e | 2A (180°) | 3A (120°) | 5A (72°) | 5B (144°) |
|---|---|---|---|---|---|
| `A`  | 1 | 1  | 1  | 1 | 1 |
| `T₁` | 3 | −1 | 0  | φ | −1/φ |
| `T₂` | 3 | −1 | 0  | −1/φ | φ |
| `G`  | 4 | 0  | 1  | −1 | −1 |
| `H`  | 5 | 1  | −1 | 0 | 0 |

with `φ = (1+√5)/2`, `−1/φ = (1−√5)/2`. The **zero pattern** (the only character datum used here —
no `√5`, so the determination is pure finite combinatorics): `T₁,T₂` vanish on `3A`; `G` vanishes on
`2A`; `H` vanishes on `5A` and `5B`; `A` never vanishes.

## The three properties that force the map (uniqueness)

1. **(P1) Character-nonvanishing.** An irrep is never assigned the angle of a class on which its
   character is zero (the realizing rotation must act nontrivially on the irrep). This alone cuts the
   `5! = 120` bijections to `40`.
2. **(P2) Galois 5-fold chirality.** The outer automorphism `√5 ↦ −√5` simultaneously swaps the
   chirality pair `T₁ ↔ T₂` and the two 5-cycle classes `5A ↔ 5B` (`72° ↔ 144°`). `χ_{T₁}` takes the
   golden value `φ` (the larger root) on `5A`, pinning `T₁ ↦ 5A (72°)` and its partner `T₂ ↦ 5B
   (144°)`. This is the chirality pair of the keystone five-fold `1+1+1+2 = 5`
   ([`KeystoneFiveFoldStructure.lean`](KeystoneFiveFoldStructure.lean)). Cuts `40 → 4`.
3. **(P3) Trivial-to-identity.** The trivial rep `A` maps to the identity class `e (0°)`. Cuts `4 → 1`.

The unique survivor is `A ↦ 0°, T₁ ↦ 72°, G ↦ 120°, T₂ ↦ 144°, H ↦ 180°`. The historic **G-vs-T₂
tie** is resolved structurally: `G ↦ 120°` is **forced** (after `A,T₁,T₂` are placed, `G` must avoid
`2A` where `χ_G = 0`, leaving only `3A`); `T₂ ↦ 144°` by the Galois twist. This is **not** the
SO(3)-tower appearance order (`T₂ ↦ 180°, G ↦ 144°`) — appearance order and the canonical class map
genuinely disagree, and the character table picks the latter.

## Anti-tautology

The angles here come **only** from the classical A₅ character table (zero pattern + Galois action) —
they carry **no `q₀` dependence**. The MTC weights `W_λ = d_q²/D²` (residual (i)) are the **separate**
`q₀`-Plancherel data. So this bijection is **not** a re-naming of `W_λ`: angles and weights are
independent inputs, exactly the structure a genuine geometric realization should have.

## Scope (honest)

This pins and proves-unique the **class-angle** half of the keystone (`conj:s5-so3-fiber-action`),
upgrading the Reeb-phase #3093 instance to the actual icosahedral class angles and making the
owner-gated geometric derivation **falsifiable** (any Bring-quintic automorphism derivation must
reproduce `{0,72,120,144,180}`). It does **not** close residual (i) (the `W_λ = d_q²/D²`
Plancherel/MTC obligation), and it does **not** re-derive Bring's quintic automorphism from scratch —
P1–P3 are read off the published A₅ character table.

Base ring (§7c): the determination is pure finite combinatorics over the inductive `A5Irrep` /
`IcoClass` (`decide`-verifiable); the only `ℝ` appears in the optional `BringFiberAction`-shaped
furnishing at the end, where the SO(3) rotation angle is intrinsically real.

-- Ref: [klein1888] Klein, Lectures on the Icosahedron (Bring's quintic, A₅ ≅ I).
-- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7 (A₅ character table).
-/

namespace QOU.BraidsAndKnots

/-- The five conjugacy classes of `A₅ ≅ I ⊂ SO(3)`, named by their rotation order:
    `e` (identity), `c2` (double transpositions, order 2), `c3` (3-cycles, order 3),
    `c5a`/`c5b` (the two 5-cycle classes, Galois-conjugate). -/
inductive IcoClass where
  | e | c2 | c3 | c5a | c5b
  deriving DecidableEq, Repr

/-- All five icosahedral conjugacy classes. -/
def allList : List IcoClass := [.e, .c2, .c3, .c5a, .c5b]

instance : Fintype IcoClass where
  elems := {IcoClass.e, IcoClass.c2, IcoClass.c3, IcoClass.c5a, IcoClass.c5b}
  complete := fun x => by cases x <;> decide

instance : Fintype A5Irrep where
  elems := {A5Irrep.A, A5Irrep.T₁, A5Irrep.T₂, A5Irrep.G, A5Irrep.H}
  complete := fun x => by cases x <;> decide

/-- The icosahedral rotation angle (in degrees) of each conjugacy class. -/
def IcoClass.angle : IcoClass → ℕ
  | .e => 0 | .c2 => 180 | .c3 => 120 | .c5a => 72 | .c5b => 144

/-- **The A₅ character zero pattern** (`charVanishes λ C = true ⟺ χ_λ(C) = 0`): `T₁,T₂` vanish on
    the 3-cycles `c3`; `G` vanishes on the double-transpositions `c2`; `H` vanishes on both 5-cycle
    classes `c5a, c5b`; the trivial rep `A` never vanishes. The only character datum the determination
    uses (no `√5`). -/
def charVanishes : A5Irrep → IcoClass → Bool
  | .A,  _ => false
  | .T₁, c => decide (c = .c3)
  | .T₂, c => decide (c = .c3)
  | .G,  c => decide (c = .c2)
  | .H,  c => decide (c = .c5a ∨ c = .c5b)

/-- **The canonical class map** `A₅ irrep → conjugacy class`, uniquely forced by P1+P2+P3
    (`canonical_angle_map_unique`). The `G-vs-T₂` tie is resolved: `G ↦ c3`, `T₂ ↦ c5b`. -/
def canonicalClassMap : A5Irrep → IcoClass
  | .A  => .e
  | .T₁ => .c5a
  | .G  => .c3
  | .T₂ => .c5b
  | .H  => .c2

/-- **The canonical class-angle bijection in degrees**: `A↦0, T₁↦72, G↦120, T₂↦144, H↦180`. -/
def irrepClassAngle (l : A5Irrep) : ℕ := (canonicalClassMap l).angle

/-- The five class angles, explicitly. -/
theorem irrepClassAngle_values :
    irrepClassAngle .A = 0 ∧ irrepClassAngle .T₁ = 72 ∧ irrepClassAngle .G = 120 ∧
    irrepClassAngle .T₂ = 144 ∧ irrepClassAngle .H = 180 := by decide

/-- **The canonical class map is a genuine bijection** (injective on the five-element `A5Irrep`). -/
theorem canonicalClassMap_injective : Function.Injective canonicalClassMap := by decide

/-- **The five class angles are distinct** — the substantive `five_distinct_classes` content, now with
    the actual icosahedral conjugacy-class angles `{0,72,120,144,180}` rather than the continuous Reeb
    phases of #3093. -/
theorem irrepClassAngle_injective : Function.Injective irrepClassAngle := by decide

/-- **(P1) Character-nonvanishing predicate** on a class assignment `f`. `abbrev` so that the
    `∀ l, … = false` body stays transparently `Decidable` (over `Fintype A5Irrep`) for `decide`. -/
abbrev SatisfiesNonvanishing (f : A5Irrep → IcoClass) : Prop :=
  ∀ l, charVanishes l (f l) = false

/-- The canonical map is character-nonvanishing (P1 holds). -/
theorem canonical_satisfies_nonvanishing : SatisfiesNonvanishing canonicalClassMap := by decide

/-- **Uniqueness — the three structural properties force the canonical map.** Any class assignment
    `f` that is character-nonvanishing (P1), Galois 5-fold chiral (`T₁ ↦ c5a`, `T₂ ↦ c5b`, P2),
    trivial-to-identity (`A ↦ e`, P3), and injective, equals `canonicalClassMap`. In particular the
    `G ↦ c3` / `H ↦ c2` split (the G-vs-T₂ tie) is forced: with `A, T₁, T₂` placed, `G` must avoid
    `c2` (`χ_G = 0` there, by P1) and `e, c5a, c5b` (already taken, by injectivity), leaving only `c3`;
    then `H` lands on the last free class `c2`. -/
theorem canonical_angle_map_unique
    (f : A5Irrep → IcoClass)
    (hP1 : SatisfiesNonvanishing f)
    (hT₁ : f .T₁ = .c5a) (hT₂ : f .T₂ = .c5b) (hA : f .A = .e)
    (hinj : Function.Injective f) :
    f = canonicalClassMap := by
  -- `G ↦ c3`: forced by avoiding `c2` (P1) and `e, c5a, c5b` (injectivity).
  have hG : f .G = .c3 := by
    have h2 : f .G ≠ .c2 := by
      intro h; have e1 := hP1 .G; rw [h] at e1; exact absurd e1 (by decide)
    have he : f .G ≠ .e   := fun h => absurd (hinj (h.trans hA.symm)) (by decide)
    have ha : f .G ≠ .c5a := fun h => absurd (hinj (h.trans hT₁.symm)) (by decide)
    have hb : f .G ≠ .c5b := fun h => absurd (hinj (h.trans hT₂.symm)) (by decide)
    rcases hfg : f .G with _ | _ | _ | _ | _ <;> simp_all
  -- `H ↦ c2`: the last free class after `A, T₁, T₂, G` are placed (injectivity).
  have hH : f .H = .c2 := by
    have he : f .H ≠ .e   := fun h => absurd (hinj (h.trans hA.symm)) (by decide)
    have ha : f .H ≠ .c5a := fun h => absurd (hinj (h.trans hT₁.symm)) (by decide)
    have hb : f .H ≠ .c5b := fun h => absurd (hinj (h.trans hT₂.symm)) (by decide)
    have h3 : f .H ≠ .c3  := fun h => absurd (hinj (h.trans hG.symm)) (by decide)
    rcases hfh : f .H with _ | _ | _ | _ | _ <;> simp_all
  funext l
  cases l
  · rw [hA]; rfl
  · rw [hT₁]; rfl
  · rw [hT₂]; rfl
  · rw [hG]; rfl
  · rw [hH]; rfl

/-- **The canonical class-angle map furnishes a `BringFiberAction`** whose rotation angles are the
    genuine icosahedral conjugacy-class angles. Provided as a `def` (not a global `instance`) to avoid
    clashing with the merged Reeb-phase instance `bringFiberAction_icosahedral` (#3093); the two are
    different-but-both-injective angle assignments, and this one is the geometrically canonical
    (actual-rotation-angle) realization. `five_distinct_classes` reduces to `irrepClassAngle_injective`
    through the injective `ℕ ↪ ℝ` cast. -/
noncomputable def bringFiberAction_canonicalClassAngles : BringFiberAction where
  irrepToRotation l := ⟨{ axis_x := 0, axis_y := 0, axis_z := 1, angle := (irrepClassAngle l : ℝ) }⟩
  five_distinct_classes := by
    intro a b h
    have h' : (irrepClassAngle a : ℝ) = (irrepClassAngle b : ℝ) := h
    exact irrepClassAngle_injective (Nat.cast_injective h')

end QOU.BraidsAndKnots
