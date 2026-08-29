import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic

/-!
# QOU.Eightfold.Sym2GateComplexType — the parity invariant is a SELF-DUAL theorem

Companion to `QOU.Eightfold.Sym2GateMultiplicity`, whose §"Why the count has no
cross terms" states the boundary this file proves:

> Over a group with a non-self-dual irrep the cross terms would have to be
> carried, and the parity conclusion would not follow.

That is a prose caveat in a file whose whole point is that prose caveats about
scope should be theorems.  Here it is one.

## Why it matters for the chapter

`Sym2GateMultiplicity.dimOfMult_ne_three_of_gate` proves that no
three-dimensional object of the single-fibre `SU(2)` category passes the `Sym²`
gate.  It is easy to over-read that as *"the gate excludes dimension 3"* — and
the eightfold chapter needs a three-dimensional object, so the difference is the
whole question.

It does not.  The proof runs through `even_dimOfMult_of_gate`, and **that**
runs through self-duality: every `SU(2)` irrep satisfies `V^* ≅ V`, so the
cross terms `V_i ⊗ V_j` (`i ≠ j`) contribute no singlet, the count reduces to
the two self-pairing terms, and the survivors are forced to be distinct
even-dimensional irreps.  Drop self-duality and the argument has no purchase:
a **complex-type** irrep (`FS = 0`, `X ≇ X̄`) pairs to a singlet only against
its conjugate, so a lone `X` — conjugate *absent* from the object — passes the
gate at **any** dimension, odd included.

`complex_three_passes_gate` below is that object at dimension exactly `3`.

So the `SU(3)` fundamental is not an exception the gate tolerates; it lives in
a sector the parity theorem never covered.  This is the same distinction
`AGENTS.md` §"Before declaring 'refuted'" draws between a scope-(a) and a
scope-(b) claim, applied to the corpus's own invariant: `even_dimOfMult_of_gate`
is scope-(b) **within the self-dual sector** and says nothing outside it.

## What is proved

* `crossSingletCount_eq_zero_iff` — the complex-sector gate: the cross terms
  vanish exactly when no irrep appears together with its conjugate.
* `ComplexTypeOn` / `complexType_gate_iff_no_conjugate_pair` — the hypothesis
  that makes the count a gate, carried explicitly, and the gate's reading under
  it: never an irrep together with its conjugate.
* `conjugate_pair_fails_gate` — the failure mode of the complex sector, and
  `witness_fails_once_conjugate_present`, the same object failing once the
  conjugate is added.
* `complex_three_passes_gate` + `complex_three_dim` — the witness: an object of
  **odd** dimension `3` that passes.
* `parity_invariant_fails_in_complex_sector` — the two combined, as the scope
  statement: `Sym2GateMultiplicity.even_dimOfMult_of_gate` has no analogue here.

## Scope — what this does NOT do

It does **not** exhibit the `SU(3)` fundamental, does not formalise `SU(3)`,
and does not prove `Sym²(𝟑) = 𝟔` is irreducible.  Mathlib has no `SU(3)`
representation type and that remains the gap recorded in `qou-8fl1` (T2-hard).

What it settles is the *shape* of the question, which was the thing at risk of
being got wrong: whether the corpus's parity exclusion is evidence against a
three-dimensional flavour fundamental.  It is not — the exclusion is a theorem
about self-dual fibres, and it is silent, not negative, on the complex-type
sector.  A reader who took `dimOfMult_ne_three_of_gate` as a general bar on
dimension 3 would be drawing a scope-(b) conclusion from a scope-(a) result.

The model here is the standard cross-term count, cited not derived, exactly as
in the companion file: `dim Hom(1, V_i ⊗ V_j) = [V_j ≅ V_i^*]`.

## Base ring (§7c)

Pure combinatorics over `ℕ`.  No ring, no ordering, no archimedean content.

-- Ref: [fulton-harris1991] §11 (Frobenius–Schur indicator; the three types
-- real / complex / quaternionic, and `dim Hom(1, V ⊗ W) = [W ≅ V^*]`).
-/

namespace QOU.Eightfold.Sym2GateComplexType

open Finset

/-! ## 1. Data for a category whose irreps need not be self-dual

`S` indexes the irreps occurring in `W`, `m` their multiplicities, `d` their
dimensions — left free rather than fixed to `2j + 1`, since outside `SU(2)`
there is no such formula — and `dual i` names the index of `V_i^*`. -/

/-- `dim W = Σ_i m_i · d_i`. -/
def dimOfMultGen (S : Finset ℕ) (m d : ℕ → ℕ) : ℕ := ∑ i ∈ S, m i * d i

/-- The cross-term singlet count **on the complex sector**.  `V_i ⊗ V_j`
contains a singlet exactly when `V_j ≅ V_i^*`, so the `V_i` isotypic component
pairs against the `V_{dual i}` one to contribute `m_i · m_{dual i}`.

Summed over `i ∈ S` this counts each conjugate pair from **both ends**, so it is
a count of *ordered* singlet-producing pairings — twice the unordered number.
Only its **vanishing** is used below, and that is unaffected; the factor is
recorded rather than quietly divided out.

**Scope, and it is not cosmetic.**  This is the complete singlet count only when
every occurring irrep is of **complex type** (`ComplexTypeOn` below): then
`Sym²(V_i)` carries no singlet of its own and the cross terms are all there is.
On a **self-dual** irrep it is simply the wrong quantity — the true contribution
is `C(m+1, 2)` (orthogonal) or `C(m, 2)` (symplectic), per
`Sym2GateMultiplicity.sym2SingletCount`, and the symplectic case differs from
`m²` exactly where it matters: at `m = 1` the binomial vanishes and `m²` does
not.  Reading `m_i · m_{dual i}` as a singlet count at `dual i = i` would
contradict `Sym2GateMultiplicity.fundamental_passes_gate`, in which the
self-dual 2-dimensional fibre is present and **passes**.  Hence the
`ComplexTypeOn` hypothesis is carried explicitly wherever the count is read as
a gate. -/
def crossSingletCount (S : Finset ℕ) (m dual : ℕ → ℕ) : ℕ :=
  ∑ i ∈ S, m i * m (dual i)

/-! ## 2. The complex-sector gate -/

/-- **The gate in the complex sector.**  The cross terms vanish exactly when no
irrep occurs together with its conjugate. -/
theorem crossSingletCount_eq_zero_iff (S : Finset ℕ) (m dual : ℕ → ℕ) :
    crossSingletCount S m dual = 0 ↔ ∀ i ∈ S, m i = 0 ∨ m (dual i) = 0 := by
  unfold crossSingletCount
  rw [Finset.sum_eq_zero_iff]
  exact forall₂_congr fun i _ => Nat.mul_eq_zero

/-- **Complex type on `S`**: no occurring irrep is its own dual.  This is the
`FS = 0` hypothesis, and it is what licenses reading `crossSingletCount` as the
singlet count at all — see the scope paragraph on the definition. -/
def ComplexTypeOn (S : Finset ℕ) (dual : ℕ → ℕ) : Prop := ∀ i ∈ S, dual i ≠ i

/-- On the complex sector the gate has a **conjugate-avoidance** reading: it
passes exactly when the object never contains an irrep together with its
conjugate.

**The hypothesis is not used in the proof, and that is the point.**  The
equivalence is pure arithmetic — it holds for any `dual` whatever, which is why
it is discharged by `crossSingletCount_eq_zero_iff` alone.  What `ComplexTypeOn`
buys is not the *equivalence* but the right to call the left-hand side a
**singlet count**: off the complex sector `crossSingletCount` is not the singlet
count at all (see the scope paragraph on the definition), so the equivalence
would be a true statement about the wrong quantity.  Carrying the hypothesis
forces call sites to declare the sector rather than inherit the reading
silently.  Named accordingly — the interpretation, not the arithmetic, is what
is conditional. -/
theorem complexType_gate_iff_no_conjugate_pair {S : Finset ℕ} {m dual : ℕ → ℕ}
    (_h : ComplexTypeOn S dual) :
    crossSingletCount S m dual = 0 ↔ ∀ i ∈ S, m i = 0 ∨ m (dual i) = 0 :=
  crossSingletCount_eq_zero_iff S m dual

/-- Within the complex sector, an irrep **and** its conjugate both present is
exactly what fails the gate.  (Contrast the self-dual sector, where the
restrictive mechanism is instead the binomial self-pairing of
`Sym2GateMultiplicity` — a different quantity, and one that lets a symplectic
irrep through at multiplicity one.) -/
theorem conjugate_pair_fails_gate {S : Finset ℕ} {m dual : ℕ → ℕ} {i : ℕ}
    (hi : i ∈ S) (hpos : 0 < m i) (hdual : 0 < m (dual i)) :
    crossSingletCount S m dual ≠ 0 := by
  intro h
  rcases (crossSingletCount_eq_zero_iff S m dual).mp h i hi with h0 | h0 <;> omega

/-! ## 3. The witness: an odd-dimensional object that passes

Index `0` carries a complex-type irrep of dimension `3`; its conjugate is index
`1`, which is **absent** from the object (`m 1 = 0`). -/

/-- Multiplicity: one copy of irrep `0`, nothing else. -/
def wMult : ℕ → ℕ := fun i => if i = 0 then 1 else 0

/-- Dimensions: irrep `0` (and its conjugate `1`) are three-dimensional. -/
def wDim : ℕ → ℕ := fun _ => 3

/-- Conjugation: `0 ↔ 1`, a genuine involution with **no fixed point** among
the two indices — this is what `FS = 0`, complex type, means. -/
def wDual : ℕ → ℕ := fun i => if i = 0 then 1 else if i = 1 then 0 else i

theorem wDual_involutive_on_pair : wDual (wDual 0) = 0 ∧ wDual (wDual 1) = 1 := by
  decide

/-- The conjugate is genuinely a **different** irrep — the complex-type
hypothesis, stated rather than assumed silently. -/
theorem wDual_zero_ne_self : wDual 0 ≠ 0 := by decide

/-- The object has dimension `3`. -/
theorem complex_three_dim : dimOfMultGen {0} wMult wDim = 3 := by decide

/-- **The witness.**  It passes the gate: the only occurring irrep is `0`, whose
conjugate `1` has multiplicity `0`, so no cross term survives — and `Sym²` of a
complex-type irrep contains no singlet of its own. -/
theorem complex_three_passes_gate : crossSingletCount {0} wMult wDual = 0 := by
  decide

/-- **The scope statement.**  There is an object that passes the `Sym²` gate and
has **odd** dimension.  So `Sym2GateMultiplicity.even_dimOfMult_of_gate` — "a
passing object has even dimension" — has no analogue once irreps are allowed to
be non-self-dual, and `dimOfMult_ne_three_of_gate` must be read as a theorem
about the self-dual sector, not as a bar on dimension `3`. -/
theorem wComplexType : ComplexTypeOn {0} wDual := by
  intro i hi
  rw [Finset.mem_singleton] at hi
  subst hi
  decide

theorem parity_invariant_fails_in_complex_sector :
    ∃ (S : Finset ℕ) (m d dual : ℕ → ℕ),
      ComplexTypeOn S dual ∧
      crossSingletCount S m dual = 0 ∧ Odd (dimOfMultGen S m d) :=
  ⟨{0}, wMult, wDim, wDual, wComplexType, complex_three_passes_gate, by
    rw [complex_three_dim]; decide⟩

/-- The contrast that isolates the cause.  Keep the object and add its
conjugate, and it fails.  So what the witness above relies on is not the
dimension and not the multiplicity, but the **absence of the conjugate** — the
freedom a self-dual category does not have, since there the conjugate is always
present whenever the irrep is. -/
theorem witness_fails_once_conjugate_present :
    crossSingletCount {0, 1} (fun _ => 1) wDual ≠ 0 :=
  conjugate_pair_fails_gate (i := 0) (by decide) (by decide) (by decide)

end QOU.Eightfold.Sym2GateComplexType
