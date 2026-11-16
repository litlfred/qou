/-!
# `QOU.BringsSurface.BranchPointSixNotForced` — the branch-point count `6` is not forced

Bean `qou-qhcr`.  Companions: `QOU.BringsSurface.EulerCharacteristicSix` (the
torus-knot route to `g = 4`), `QOU.BringsSurface.CoveringDegreeRamification`
(the degree/monodromy audit of the same six branch points),
`QOU.Information.ChiMinusSix` (which carries `bringGenus = 4` as a class field).

## What this file is about

`ex:chi-minus-six-derivation` (`brings-surface/chi-minus-six-chain.md`) runs an
eight-step chain to `χ(A) = −6`.  Steps 1–4 and 6–8 are axiom consequences.
Step 5 — *"the Frobenius–Hopf structure forces the algebra to have exactly 6
branch points in its geometric descent (from the `S₃ ⊂ S₅` orbits on the 6
Weierstrass points of Bring's surface)"* — is the one step that is not, and the
block's own opening sentence says so.

This file does **not** derive the 6.  It measures how far the derived steps get,
records what the classical facts actually are, and refutes three candidate
sources for the 6 — including the finite-subgroup / ADE route, which was the
route this bean was opened to test.

Everything below is finite arithmetic over `ℕ` and `ℤ`, decidable, and stated so
that a wrong cone order, a wrong orbit size or a wrong Riemann–Hurwitz constant
makes a theorem fail rather than a docstring lie.  No `sorry`, no `axiom`, no
`native_decide`, no `ℝ` (§7c: nothing archimedean appears).

**Deliberately import-free.**  Every statement is closed arithmetic on `ℕ`/`ℤ`
and finite lists, so `decide`, `rfl` and `omega` from core suffice.  Nothing here
needs Mathlib, and not importing it keeps the module verifiable in a container
that has only a partial olean tree.

## Sources for the classical inputs (all held in `library/`)

* **60 Weierstrass points, `Aut(B) = S₅` transitive, `60 = 6 × 10`** — Braden &
  Disney-Hogg, *Bring's curve: old and new*, Prop. 3.3 and the paragraph after
  it (`library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md`),
  registered `[braden-disney-hogg-2022]`.
* **The `(2,4,5)` triangle group, `[Γ* : Γ] = |S₅| = 120`, `B = Δ/Γ` of genus 4**
  — Riera & Rodríguez, *The period matrix of Bring's curve*, §2
  (`library/pjm-v154-n1-p09-s/`), registered `[riera-rodriguez-1992]`.
* **Transitivity classification** — Laing & Singerman, *Transitivity on
  Weierstrass points*, Ann. Acad. Sci. Fenn. Math. **37** (2012), Theorem 15;
  quoted as Theorem 3.4 of `[braden-disney-hogg-2022]`
  (`.../sections/sec-006-31-weierstrass-points.md`).  Not separately held.
* **Finite subgroups of `SU(2)` / the ADE–McKay list and its cone orders** —
  classical (Klein), `[klein1888]`.
-/

namespace QOU.BringsSurface.BranchPointSixNotForced

/-! ## §1. How much of `χ(A) = −6` the derived steps actually supply

Step 3 is Riemann–Roch, `χ = 2 − 2g`.  Step 4 is obstruction non-triviality,
`g ≥ 1`.  Step 6 ("the sign is negative") adds nothing: it is already implied by
Step 4.  So Steps 1–4 and 6 together constrain `χ(A)` to the non-positive even
integers, and **Step 5 alone picks `−6` out of that infinite set**. -/

/-- Euler characteristic of a closed orientable genus-`g` surface. -/
def eulerChar (g : Nat) : Int := 2 - 2 * (g : Int)

/-- The predicate Steps 3 + 4 of the chain impose on `χ(A)`. -/
def Step34Admissible (chi : Int) : Prop := ∃ g : Nat, 1 ≤ g ∧ chi = eulerChar g

theorem neg_six_admissible : Step34Admissible (-6) := ⟨4, by omega, by decide⟩

/-- **The falsifiable half.**  `−4` is admissible for exactly the same reasons
`−6` is, so Steps 3 + 4 do not distinguish them.  If this failed, Steps 3 + 4
would already carry more than they are credited with. -/
theorem neg_four_admissible : Step34Admissible (-4) := ⟨3, by omega, by decide⟩

theorem neg_eight_admissible : Step34Admissible (-8) := ⟨5, by omega, by decide⟩

/-- **Steps 3 + 4 leave infinitely many values open.**  Every non-positive even
integer `−2n` is admissible, realised at genus `n + 1`. -/
theorem all_even_nonpos_admissible (n : Nat) : Step34Admissible (-2 * (n : Int)) :=
  ⟨n + 1, by omega, by simp only [eulerChar]; omega⟩

/-- **…and nothing else is.**  The admissible set is exactly the non-positive
even integers, so the derived steps are neither weaker nor stronger than that. -/
theorem step34_admissible_iff (chi : Int) :
    Step34Admissible chi ↔ (chi ≤ 0 ∧ ∃ k : Int, chi = 2 * k) := by
  constructor
  · rintro ⟨g, hg, rfl⟩
    refine ⟨by simp only [eulerChar]; omega, 1 - (g : Int), by simp only [eulerChar]; omega⟩
  · rintro ⟨hle, k, rfl⟩
    refine ⟨(1 - k).toNat, by omega, ?_⟩
    simp only [eulerChar]
    omega

/-! ## §2. "Six branch points" over `ℙ¹` does not fix the genus

The corpus's own six-branch-point datum is a covering of `ℙ¹`, not of a torus:
`brings-qou-4tuple.md:15` gives degree 3, `brings-is-qou-verification.md:15`
gives degree 4 with total ramification `R = 14` (see
`QOU.BringsSurface.CoveringDegreeRamification` for the audit of that
disagreement).

For a degree-`d` branched cover of `ℙ¹`, `χ(S) = 2d − R` where `R` is the
**total ramification**, not the branch-point count.  A branch point contributes
between `1` and `d − 1`, so `b` branch points give `b ≤ R ≤ b(d − 1)`.  The
branch-point count therefore pins `χ` only through `R`, and at the corpus's own
`(d, b) = (4, 6)` it leaves the whole range `genus 0 … 6` open. -/

/-- `χ` of the total space of a degree-`d` branched cover of `ℙ¹` with total
ramification `R`: Riemann–Hurwitz, `χ = d · χ(ℙ¹) − R = 2d − R`.  This is a
*definition* encoding Riemann–Hurwitz's statement; Mathlib has no
branched-covering API and nothing here proves the theorem itself. -/
def chiOverP1 (d R : Nat) : Int := 2 * (d : Int) - (R : Int)

/-- The corpus's degree-4 reading: `R = 14` is what gives `−6`. -/
theorem corpus_degree_four : chiOverP1 4 14 = -6 := by decide

/-- The corpus's degree-3 reading gives the same `χ` with a different `R`
(`R = 2g − 2 + 2d = 12`), which is why the two blocks are not numerically
inconsistent even though they describe different maps. -/
theorem corpus_degree_three : chiOverP1 3 12 = -6 := by decide

/-- **`b = 6` at degree 4 is compatible with every genus from 0 to 6.**  The
lower end is every branch point simple (`R = b = 6`), the upper end is every
branch point totally ramified (`R = b(d−1) = 18`).  So the branch-point count,
taken alone with the degree, determines nothing near `g = 4`. -/
theorem six_branch_points_degree_four_spans_genus_zero_to_six :
    chiOverP1 4 6 = eulerChar 0 ∧ chiOverP1 4 8 = eulerChar 1 ∧
    chiOverP1 4 10 = eulerChar 2 ∧ chiOverP1 4 12 = eulerChar 3 ∧
    chiOverP1 4 14 = eulerChar 4 ∧ chiOverP1 4 16 = eulerChar 5 ∧
    chiOverP1 4 18 = eulerChar 6 := by decide

/-- The ramification range a branch-point count allows: `b ≤ R ≤ b·(d−1)`. -/
def ramificationLo (b : Nat) : Nat := b
def ramificationHi (d b : Nat) : Nat := b * (d - 1)

theorem ramification_range_degree_four_six_points :
    ramificationLo 6 = 6 ∧ ramificationHi 4 6 = 18 := by decide

/-! ## §3. Where the real `6` lives, and what Step 5 says instead

Step 5 attributes the 6 to *"the `S₃ ⊂ S₅` orbits on the 6 Weierstrass points of
Bring's surface"*.  Both halves of that parenthetical are wrong against the held
source.

Bring's curve is non-hyperelliptic of genus 4, so all its Weierstrass points have
weight 1 and there are `g³ − g = 60` of them; `Aut(B) = S₅` acts **transitively**
on all 60 (`[braden-disney-hogg-2022]` Prop. 3.3).  There is therefore no set of
six Weierstrass points for an `S₃` to act on.

What the same source does record, one paragraph later, is `60 = 6 × 10`: **six**
Weierstrass points are fixed by **each of the ten transpositions** in `S₅`.  The
carrier of the 6 is an involution, not an `S₃`, and 6 is a per-involution count,
not a total.  Under that reading Step 5 becomes a coherent Riemann–Hurwitz
statement: the degree-2 quotient by a transposition has six fixed points, so its
base has genus 1 and `χ(B) = 2·χ(torus) − 6 = −6`.

That reading repairs the citation.  It does not make the step a derivation — it
still reads the 6 off Bring's curve, which the chain identifies two steps later. -/

/-- Total Weierstrass weight of a genus-`g` curve, `g³ − g`; equal to the number
of Weierstrass points exactly when every point has weight 1, which holds for
Bring's curve. -/
def weierstrassWeightTotal (g : Nat) : Nat := g ^ 3 - g

/-- **Bring's curve has 60 Weierstrass points, not 6.** -/
theorem bring_weierstrass_count : weierstrassWeightTotal 4 = 60 := by decide

theorem bring_weierstrass_count_ne_six : weierstrassWeightTotal 4 ≠ 6 := by decide

/-- Transpositions in `S₅`: `C(5,2) = 10`. -/
def s5TranspositionCount : Nat := 10

/-- **`60 = 6 × 10`** — six Weierstrass points fixed by each of the ten
transpositions (`[braden-disney-hogg-2022]`, after Prop. 3.3). -/
theorem weierstrass_split_six_by_ten :
    weierstrassWeightTotal 4 = 6 * s5TranspositionCount := by decide

/-- `χ` of a degree-`d` cover of a genus-`h` base with total ramification `R`:
`χ = d·(2 − 2h) − R`.  Generalises `chiOverP1` (`h = 0`). -/
def chiOfCover (d h R : Nat) : Int := (d : Int) * (2 - 2 * (h : Int)) - (R : Int)

theorem chiOfCover_zero_base (d R : Nat) : chiOfCover d 0 R = chiOverP1 d R := by
  simp only [chiOfCover, chiOverP1]; omega

/-- **The repaired Step 5.**  A degree-2 quotient of Bring's curve by a
transposition has six fixed points, each contributing `d − 1 = 1`, so `R = 6`;
the quotient has genus 1 and `χ(B) = 2·0 − 6 = −6`. -/
theorem bring_quotient_by_transposition : chiOfCover 2 1 6 = eulerChar 4 := by decide

/-- **Over a genus-1 base the degree drops out entirely**: `χ = −R` for every
degree.  So the repaired reading fixes the ramification at 6 and says nothing
whatever about the degree — a second place where the chain's arithmetic is
weaker than it looks. -/
theorem chi_over_torus_is_minus_ramification (d R : Nat) :
    chiOfCover d 1 R = -(R : Int) := by
  simp only [chiOfCover]; omega

/-- **`R = 6` is not forced by `χ = −6` together with `h ≥ 1`.**  Three
`(degree, base genus, ramification)` triples give `−6`, with ramification 6, 2
and 0.  The 6 arrives with the choice of base genus, not from `χ`. -/
theorem ramification_six_not_forced :
    chiOfCover 2 1 6 = -6 ∧ chiOfCover 2 2 2 = -6 ∧ chiOfCover 3 2 0 = -6 := by decide

/-! ## §4. The torus-knot route carries no genus information either

`QOU.BringsSurface.EulerCharacteristicSix` derives `g = 4`, sorry-free, from two
embeddability constraints: `T₂,₉` must embed (Seifert rank `4 ≤ g`) and `T₂,₁₁`
must not (rank `5 ≰ g`).  The arithmetic is correct and the file says outright
that "neither step is deep".

It is worth saying exactly how shallow, because the form of the constraint is
what a reader is likely to trust.  The Seifert rank of `T₂,ₛ` is `(s−1)/2`, so
for **every** target genus `g` the pair `T₂,₂g₊₁ / T₂,₂g₊₃` brackets it.  At
`g = 4` that pair is `(9, 11)` — exactly the corpus's choice.  The two
constraints therefore carry precisely the information "the genus is 4" and
nothing more; they are a restatement of the target, not an independent route to
it. -/

/-- Seifert rank of the `(2, s)` torus knot, `(2−1)(s−1)/2 = (s−1)/2`. -/
def seifertRankTwo (s : Nat) : Nat := (s - 1) / 2

theorem seifertRankTwo_nine : seifertRankTwo 9 = 4 := by decide
theorem seifertRankTwo_eleven : seifertRankTwo 11 = 5 := by decide

/-- **Every genus has a bracketing pair.**  `T₂,₂g₊₁` embeds on `Σ_g` and
`T₂,₂g₊₃` does not, for every `g`.  So the shape "one torus knot embeds, the
next does not" cannot single out `g = 4`. -/
theorem torus_knot_pair_brackets_every_genus (g : Nat) :
    seifertRankTwo (2 * g + 1) ≤ g ∧ ¬ seifertRankTwo (2 * g + 3) ≤ g := by
  constructor <;> simp only [seifertRankTwo] <;> omega

/-- The corpus's `(T₂,₉, T₂,₁₁)` is exactly the generic bracketing pair at
`g = 4`. -/
theorem corpus_pair_is_the_generic_bracket : 2 * 4 + 1 = 9 ∧ 2 * 4 + 3 = 11 := by decide

/-! ## §5. The ADE route, tested

`QOU.SU2EmergenceRankForced.su2_emergence_rank_forced` derives, from QOU axiom 5
(the categorical volume constraint `Λ²V ≅ 𝟙`) plus a dagger condition and
`det = 1`, that the fibre has rank 2 and that `G ⊆ SU(2)`.  The finite subgroups
of `SU(2)` are ADE-classified, so a natural question is whether an axiom picks
one of them and thereby produces a `6` as a group-theoretic invariant.

Three things go wrong, and the third is the informative one.

**(a) Nothing makes `G` finite.**  The conclusion of `su2_emergence_rank_forced`
is `∀ g ∈ G, g ∈ specialUnitaryGroup`, and `G` is a bare `Set`.  It is satisfied
by `G = SU(2)` itself, which is infinite; `qou-axioms-physical-reading.md` says
so in words — axiom 5 is *"the condition that makes the reconstructed gauge group
`SU(2)`"*.  The ADE list classifies **finite** subgroups, so the classification
does not apply to the object the axioms deliver.  (Not restated as a Lean theorem
here: `G = SU(2)` satisfying `g·g† = 1 ∧ det g = 1` is immediate from the
definition of `specialUnitaryGroup`, and formalising "`SU(2)` is infinite" would
add a Mathlib dependency to an otherwise import-free module without adding
information.)

**(b) Nothing picks the ADE type.**  Of the five families, exactly one is
excluded by an axiom — see §5.3 — and four survive.

**(c) Granting both, the icosahedral case does not produce a 6.**  The three
exceptional orbits of the icosahedral rotation group on `ℙ(V)` have sizes
`30, 20, 12`.  Six is an exceptional orbit size for the **tetrahedral** (`E₆`),
**octahedral** (`E₇`) and **dihedral-6** groups and is **not** one for the
icosahedral (`E₈`) group.  So an orbit-count reading of "branch points on
`ℙ(V)`" points *away* from the icosahedral case.

A Sylow reading does pick `E₈` — `A₅` has six Sylow-5 subgroups, equivalently
`|ℙ¹(𝔽₅)| = 6` — but the two readings disagree on the same group in both
directions (§5.4).  So "6" is not a function of the ADE type; it is a function of
the invariant one chooses to read, and nothing in the axioms names that
invariant.  Choosing the Sylow reading *because* it returns 6 is selection
against the target, which AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" forbids. -/

/-- The five families of finite subgroups of `SU(2)` (McKay's ADE list), named by
the rotation group they cover in `SO(3) = SU(2)/{±1}`.  `cyclic n` and
`dihedral n` carry the rotation group's parameter; `dihedral n` is intended for
`n ≥ 2` (`dihedral 1` is cyclic of order 2 and is not a separate family). -/
inductive ADEType where
  | cyclic (n : Nat)
  | dihedral (n : Nat)
  | tetrahedral
  | octahedral
  | icosahedral
deriving DecidableEq, Repr

/-- Order of the **rotation** group in `SO(3)`; the binary group in `SU(2)` has
twice this order. -/
def rotationOrder : ADEType → Nat
  | .cyclic n => n
  | .dihedral n => 2 * n
  | .tetrahedral => 12
  | .octahedral => 24
  | .icosahedral => 60

/-- Cone orders of the quotient orbifold `ℙ(V)/Ḡ`: `S²(n,n)`, `S²(2,2,n)`,
`S²(2,3,3)`, `S²(2,3,4)`, `S²(2,3,5)`. -/
def coneOrders : ADEType → List Nat
  | .cyclic n => [n, n]
  | .dihedral n => [2, 2, n]
  | .tetrahedral => [2, 3, 3]
  | .octahedral => [2, 3, 4]
  | .icosahedral => [2, 3, 5]

/-- Sizes of the exceptional orbits on `ℙ(V)`: the orbit over the cone point of
order `m` has size `|Ḡ| / m`. -/
def exceptionalOrbitSizes (t : ADEType) : List Nat :=
  (coneOrders t).map (fun m => rotationOrder t / m)

theorem orbits_tetrahedral : exceptionalOrbitSizes .tetrahedral = [6, 4, 4] := by decide
theorem orbits_octahedral : exceptionalOrbitSizes .octahedral = [12, 8, 6] := by decide
theorem orbits_icosahedral : exceptionalOrbitSizes .icosahedral = [30, 20, 12] := by decide

/-! ### §5.1 The orbit table is cross-checked, not merely asserted

Klein's relation for a finite rotation group — equivalently the orbifold Euler
characteristic of `ℙ(V)/Ḡ` being `2/|Ḡ|` — reads, after clearing denominators,

    Σᵢ (|Ḡ| − |Ḡ|/mᵢ) = 2·|Ḡ| − 2.

Each term is the number of points of `ℙ(V)` in the `i`-th exceptional orbit's
complement-within-a-generic-orbit, so the sum is a count and stays in `ℕ`.  A
wrong cone order or a wrong orbit size breaks it. -/

/-- Left-hand side of Klein's relation. -/
def kleinDefect (t : ADEType) : Nat :=
  (exceptionalOrbitSizes t).foldl (fun acc s => acc + (rotationOrder t - s)) 0

/-- **Klein's relation holds for the three exceptional families**, which
cross-checks every cone order and orbit size in `coneOrders` /
`exceptionalOrbitSizes` above. -/
theorem klein_constraint_exceptional :
    kleinDefect .tetrahedral = 2 * rotationOrder .tetrahedral - 2 ∧
    kleinDefect .octahedral = 2 * rotationOrder .octahedral - 2 ∧
    kleinDefect .icosahedral = 2 * rotationOrder .icosahedral - 2 := by decide

/-- …and for the dihedral and cyclic families at sample parameters. -/
theorem klein_constraint_dihedral_cyclic :
    kleinDefect (.dihedral 6) = 2 * rotationOrder (.dihedral 6) - 2 ∧
    kleinDefect (.cyclic 5) = 2 * rotationOrder (.cyclic 5) - 2 := by decide

/-! ### §5.2 Six is not an icosahedral orbit -/

/-- **The negative this bean was opened to test.**  Reading the branch-point
count as the size of an exceptional orbit of the ADE group on `ℙ(V)` excludes the
icosahedral case and admits the tetrahedral, octahedral and dihedral-6 cases. -/
theorem six_orbit_excludes_icosahedral :
    6 ∉ exceptionalOrbitSizes .icosahedral ∧
    6 ∈ exceptionalOrbitSizes .tetrahedral ∧
    6 ∈ exceptionalOrbitSizes .octahedral ∧
    6 ∈ exceptionalOrbitSizes (.dihedral 6) := by decide

/-- The icosahedral orbit sizes are all at least 12, so no reading that produces
a number below 12 can be an icosahedral orbit count. -/
theorem icosahedral_orbits_at_least_twelve :
    ∀ s ∈ exceptionalOrbitSizes .icosahedral, 12 ≤ s := by decide

/-! ### §5.3 What the observability axiom does prune

Axiom 3 is `Hom_𝐂(𝟙, Ad(A)) = 0`.  Read literally — the adjoint carries no
invariant vector — it excludes exactly the cyclic family: a cyclic rotation group
fixes its axis pointwise, and every other finite rotation group fixes no line.

Two cautions.  First, `qou-axioms-physical-reading.md` glosses the axiom as
eliminating *"gauge transformations that act as the identity on every
observable"*, which is the **kernel** of `Ad`, a different condition — under that
reading every binary subgroup of `SU(2)` fails, since `{±1}` is always in the
kernel.  The two readings are not interchangeable and this file does not choose
between them; it records the literal one, which is what the axiom says.  Second,
the corpus's own Lean encodes observability as an opaque `Prop` field
(`QOU.FluidDynamics.qou_ns_in_qou`), so neither reading is currently formalised
anywhere.

`adjointInvariantDim` below is a classical table, not a derivation; the content
of §5.3 is the *count of survivors*, which is four. -/

/-- `dim (Ad)^Ḡ` — the dimension of the fixed subspace of the 3-dimensional
adjoint (rotation) representation.  A cyclic rotation group fixes its axis, so 1;
every other finite rotation group fixes no line, so 0.  Classical. -/
def adjointInvariantDim : ADEType → Nat
  | .cyclic _ => 1
  | .dihedral _ => 0
  | .tetrahedral => 0
  | .octahedral => 0
  | .icosahedral => 0

/-- **Observability prunes one family and leaves four.**  Stated together with
the orbit facts so that the conjunction is not a restatement of a single table:
the family the axiom keeps and the family an orbit-reading of `6` selects are
different families. -/
theorem observability_leaves_four_families_that_disagree_about_six :
    adjointInvariantDim (.cyclic 5) ≠ 0 ∧
    adjointInvariantDim (.dihedral 6) = 0 ∧
    adjointInvariantDim .tetrahedral = 0 ∧
    adjointInvariantDim .octahedral = 0 ∧
    adjointInvariantDim .icosahedral = 0 ∧
    6 ∈ exceptionalOrbitSizes .tetrahedral ∧
    6 ∉ exceptionalOrbitSizes .icosahedral := by decide

/-! ### §5.4 The Sylow reading, and why it does not rescue the route

`A₅` has six Sylow-5 subgroups; equivalently the six points of `ℙ¹(𝔽₅)`, which is
where the exceptional embedding `A₅ ↪ A₆` comes from.  That six *does* single out
the icosahedral case among the exceptional families.

The Sylow counts are not asserted here: Sylow's theorems constrain `n_p` to
divide `|G|/p` and to be `≡ 1 (mod p)`, and that arithmetic is decidable.  It
leaves two candidates in each case, and simplicity of `A₅` (resp. the structure
of `A₄`) picks the larger — that last input is cited, not proved.

The point of this subsection is the **disagreement**: on the icosahedral group
the Sylow reading gives 6 and the orbit reading does not; on the tetrahedral
group the orbit reading gives 6 and the Sylow reading does not.  So `6` is not
determined by the ADE type.  Both readings are available for every type and
nothing in the axioms names one. -/

/-- Candidates for `n_p` allowed by Sylow's theorems: divisors `n` of `|G|/p`
with `n % p = 1`.  Decidable, and computed rather than asserted. -/
def sylowCandidates (indexBound p : Nat) : List Nat :=
  (List.range (indexBound + 1)).filter
    (fun n => n != 0 && indexBound % n == 0 && n % p == 1)

/-- **Sylow-5 in `A₅`**: `|A₅|/5 = 12`, so `n₅ ∈ {1, 6}`. -/
theorem sylow5_candidates_A5 : sylowCandidates 12 5 = [1, 6] := by decide

/-- **Sylow-3 in `A₄`** (the tetrahedral rotation group): `|A₄|/3 = 4`, so
`n₃ ∈ {1, 4}` — and **6 is not among them**, whichever way the ambiguity is
resolved. -/
theorem sylow3_candidates_A4 : sylowCandidates 4 3 = [1, 4] := by decide

theorem six_is_not_a_sylow3_count_for_A4 : 6 ∉ sylowCandidates 4 3 := by decide

/-- `n₅(A₅) = 6`: the larger of the two Sylow candidates, since `A₅` is simple
and a normal Sylow-5 would contradict that.  The simplicity input is cited
(`[klein1888]` for the icosahedral group; standard for `A₅`), not proved here. -/
def sylow5CountA5 : Nat := 6

theorem sylow5CountA5_is_a_sylow_candidate : sylow5CountA5 ∈ sylowCandidates 12 5 := by decide

/-- **The two readings of "6" disagree, in both directions.**  This is the
statement that kills the ADE route even after finiteness and the icosahedral type
are granted: the integer 6 is a property of the chosen invariant, not of the
group. -/
theorem sylow_and_orbit_readings_disagree :
    sylow5CountA5 = 6 ∧
    6 ∉ exceptionalOrbitSizes .icosahedral ∧
    6 ∈ exceptionalOrbitSizes .tetrahedral ∧
    6 ∉ sylowCandidates 4 3 := by decide

/-! ## §6. The one narrowing that is not a read-off

Everything above is negative.  The one construction found this session that
narrows `χ(A)` without naming the integer 6 is a homogeneity hypothesis plus a
classification theorem the corpus already holds.

Laing & Singerman (Ann. Acad. Sci. Fenn. Math. **37** (2012), Thm 15; quoted as
Thm 3.4 of `[braden-disney-hogg-2022]`): a Riemann surface of genus `g > 2` with
`g³ − g` Weierstrass points on which `Aut` acts **transitively** is Bring's curve
(`g = 4`), Klein's quartic (`g = 3`), or a genus-3 curve with `Aut ≅ S₄`.

The hypothesis is *"no Weierstrass point is distinguishable from any other, and
none is distinguished by weight"* — a homogeneity statement, in the same register
as the observability axiom, and not a statement about the number 6.  It narrows
`χ(A)` from the infinite set of §1 to exactly two values, `{−4, −6}`.

Separating the two then needs one further input: an automorphism of order 5.  By
Cauchy's theorem a group has an element of order 5 iff 5 divides its order, and
`5 ∣ 120` while `5 ∤ 168` and `5 ∤ 24` — so an order-5 symmetry selects Bring and
excludes both genus-3 cases.

**This is not a closure and must not be reported as one.**  It replaces one
unsourced input (the integer 6) with two structural ones (transitivity on
Weierstrass points; an order-5 automorphism), neither of which is derived from
the five QOU axioms here.  Its value is that both are group-theoretic statements
of a kind an axiom could plausibly supply, whereas "exactly six branch points" is
not. -/

/-- The genera admitted by the Laing–Singerman transitivity classification. -/
def transitivityAdmissibleGenera : List Nat := [3, 4]

/-- **Homogeneity narrows `χ(A)` to two values.**  Contrast §1, where the derived
steps leave every non-positive even integer open. -/
theorem transitivity_narrows_chi_to_two_values :
    transitivityAdmissibleGenera.map eulerChar = [-4, -6] := by decide

/-- Automorphism-group orders of the three curves in the classification:
Bring `|S₅| = 120`, Klein `|PSL(2,7)| = 168`, and the genus-3 `|S₄| = 24`. -/
def classificationAutOrders : List Nat := [120, 168, 24]

/-- **An order-5 automorphism selects Bring.**  By Cauchy, order 5 occurs iff
`5 ∣ |Aut|`; only the genus-4 case qualifies. -/
theorem order_five_selects_bring :
    120 % 5 = 0 ∧ 168 % 5 ≠ 0 ∧ 24 % 5 ≠ 0 := by decide

/-- The two inputs together give `χ = −6` — stated so the dependence is explicit:
it is a consequence of *transitivity + order 5*, not of the five axioms. -/
theorem transitivity_and_order_five_give_chi_neg_six
    (g : Nat) (hg : g ∈ transitivityAdmissibleGenera) (h5 : g = 4) :
    eulerChar g = -6 := by
  subst h5; decide

/-! ## §6.5. Hyperelliptic vs. trigonal Riemann–Hurwitz ramification at genus `g = 4`

For a degree-`d` branched cover of `ℙ¹` by a closed orientable surface of genus
`g ≥ 1`, Riemann–Hurwitz `2 − 2g = 2d − R` fixes the total ramification to
`R(d, g) = 2g − 2 + 2d`:

* **Hyperelliptic (`d = 2`, `g = 4`)**: `R(2, 4) = 10 = 2g + 2` (which is why the
  `.qa.json` note's "minimum `2g + 2 = 10` Weierstrass points" is the
  hyperelliptic branch count, not the non-hyperelliptic Weierstrass count
  `g³ − g = 60`).
* **Trigonal (`d = 3`, `g = 4`)**: `R(3, 4) = 12 = 2g + 4` (the canonical
  projection of Bring's space quintic from a line in `ℙ³`).  A simple-transposition
  (`e − 1 = 1`) 3-sheeted cover of `ℙ¹` at genus 4 therefore has `b = 12` simple
  branch points, whereas `b = 6` branch points occur iff the average ramification
  index per branch point is `R / b = 12 / 6 = 2` (total ramification `e = 3` at
  each of the 6 branch points). -/

/-- Total ramification `R(d, g) = 2g − 2 + 2d` required by Riemann–Hurwitz for a
degree-`d` cover of `ℙ¹` to have genus `g ≥ 1`. -/
def totalRamificationOverP1 (d g : Nat) : Nat := 2 * g - 2 + 2 * d

/-- `chiOverP1 d (totalRamificationOverP1 d g)` recovers `eulerChar g` for every
`g ≥ 1` and `d`. -/
theorem chiOverP1_totalRamification (d g : Nat) (hg : 1 ≤ g) :
    chiOverP1 d (totalRamificationOverP1 d g) = eulerChar g := by
  simp only [chiOverP1, totalRamificationOverP1, eulerChar]
  omega

/-- Hyperelliptic (`d = 2`) ramification at `g = 4` is `2g + 2 = 10`, not `6`. -/
theorem hyperelliptic_ramification_genus_four :
    totalRamificationOverP1 2 4 = 10 ∧ totalRamificationOverP1 2 4 ≠ 6 := by decide

/-- Trigonal (`d = 3`) ramification at `g = 4` is `2g + 4 = 12`. -/
theorem trigonal_ramification_genus_four :
    totalRamificationOverP1 3 4 = 12 := by decide

/-- For any `g ≥ 1`, a 3-sheeted simple-transposition cover (`rPerPoint = 1`) of
`ℙ¹` has `2g + 4` branch points. -/
theorem trigonal_simple_branch_count (g : Nat) (hg : 1 ≤ g) :
    totalRamificationOverP1 3 g = 2 * g + 4 := by
  simp only [totalRamificationOverP1]
  omega

/-- For a 3-sheeted cover of `ℙ¹` of genus `4` (`R = 12`), six branch points of
uniform ramification index `rPerPoint = e − 1` occur if and only if `rPerPoint = 2`
(cyclic 3-cycle monodromy `e = 3` at each of the 6 branch points). -/
theorem trigonal_genus_four_six_branch_points_iff_index_two (rPerPoint : Nat) :
    6 * rPerPoint = totalRamificationOverP1 3 4 ↔ rPerPoint = 2 := by
  simp only [totalRamificationOverP1]
  omega

/-- Across all degrees `d ≥ 2`, a uniform-ramification cover of `ℙ¹` of genus `4`
with `b = 6` branch points (`6 · rPerPoint = 2(4) − 2 + 2d = 6 + 2d`, with
`1 ≤ rPerPoint ≤ d − 1`) has `d ≡ 0 (mod 3)` and `rPerPoint = 1 + d / 3`; in
particular the unique minimal-degree solution is the trigonal triple-ramified
cover `(d, rPerPoint) = (3, 2)`. -/
theorem uniform_six_branch_points_minimal_degree_is_trigonal (d rPerPoint : Nat) :
    (2 ≤ d ∧ d ≤ 5 ∧ 1 ≤ rPerPoint ∧ rPerPoint ≤ d - 1 ∧
      6 * rPerPoint = totalRamificationOverP1 d 4) ↔
    (d = 3 ∧ rPerPoint = 2) := by
  simp only [totalRamificationOverP1]
  omega

/-! ## §7. Summary of what is and is not established here

| claim | status |
|---|---|
| Steps 3+4 constrain `χ(A)` to the non-positive even integers, and no further | proved (§1) |
| "six branch points" over `ℙ¹` at degree 4 admits genus 0–6 | proved (§2) |
| Bring's curve has 60 Weierstrass points, not 6, with `Aut` transitive | proved from `g³−g`, cited (§3) |
| Step 5's `6` is `|Fix(τ)|` for a transposition; the quotient has genus 1 | proved (§3) |
| the torus-knot pair of `EulerCharacteristicSix` brackets **every** genus | proved (§4) |
| the axioms do not make `G` finite, so ADE does not apply | argued, not formalised (§5) |
| `6` is not an exceptional orbit size of the icosahedral group | proved (§5.2) |
| observability prunes exactly the cyclic family, leaving four | table + count (§5.3) |
| the Sylow and orbit readings of `6` disagree on the same group | proved (§5.4) |
| transitivity on Weierstrass points narrows `χ` to `{−4, −6}` | cited classification (§6) |

Nothing here derives `6`.  Scope, in the sense of AGENTS.md §"Before declaring
refuted": the ADE result of §5.2 and §5.4 is a **structural exclusion** of the
specific implication *"icosahedral type ⇒ six branch points on `ℙ(V)`"* — the
invariant is the orbit-size formula `|Ḡ|/mᵢ`, and it is proved.  It is **not** a
claim that no finite-group route can produce a 6; §5.2 exhibits three types that
do.  The §4 result is likewise an exclusion of the *form* of the torus-knot
constraint, not of the constraint's conclusion. -/

end QOU.BringsSurface.BranchPointSixNotForced
