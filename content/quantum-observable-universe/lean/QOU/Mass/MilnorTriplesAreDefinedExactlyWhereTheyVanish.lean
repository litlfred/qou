/-
QOU.Mass.MilnorTriplesAreDefinedExactlyWhereTheyVanish — on the derived carrier,
the property that makes a Milnor triple **well-defined** is the same property that
makes it **zero**.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-brng`). Milnor's
triple-linking number `μ̄(ijk)` is defined only modulo
`Δ = gcd(lk_ij, lk_jk, lk_ki)`, so it is a genuine integer exactly on triples with
`Δ = 0` — all three pairwise linking numbers vanishing. On the derived carrier
(the closure of the canonical atom braid word) the linking graph is the path `P_μ`
with `μ = A + 1`, so `Δ = 0` requires the three components to be pairwise
non-adjacent, which first happens at `A = 4`. The minimal-span family
`{i, i+2, i+4}` — `A − 3` triples, per-component multiplicity capped at 3
independent of `A` — is the only named subfamily whose count survives
`QOU.Mass.CoordinationSaturation`, against `C(A−1,3) ~ A³` for the full family.

`qou-768r` records that **no `μ̄` value has ever been computed** and that doing so
needs the Magnus expansion of a longitude in the free group. This file shows the
computation is unnecessary: on this carrier every `Δ = 0` triple has `μ̄ = 0`, and
the reason is the defining condition itself.

**The mechanism.** The closure of a *monotone* braid — one run per generator, which
the canonical atom word satisfies for every `(Z, N)` with `A = 2…24` — is a
connected sum of `(2, k)` torus links `#_g T(2, e_g)`, verified against SnapPy
`deconnect_sum` on **32/32** branches of the ²H word with zero mismatches
(`docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`). Each summand
comes from one generator `g` and so touches only the components containing strands
`g` and `g+1` — **measured: at most 2 components per generator**, on
A = 2, 4, 6, 8, 10.

A summand joining two components makes them linked. Contrapositively, components
with `lk = 0` share **no summand** — so a triple with `Δ = 0` is *separated*: no
summand of the connected sum touches two of its members. Its sublink is then
**split** — three components separated by the connected-sum spheres — and every
Milnor invariant of length ≥ 2 vanishes on a split link.

**CORRECTED 2026-09-04: this said "unlink", which over-claimed.** Sharing no summand
gives *splitness*, not triviality of the components, and I never measured the latter.
A sibling's docstring on `atom_closure_milnor_indeterminacy_probe.py` (landed on main
while this branch was open) measures the components by exact-integer Kauffman bracket
and finds every multi-strand one is a `(2, odd)`-torus **knot** — `T(2,7)` throughout
the `σ` branch, a `T(2,5)`/`T(2,3)` mix on `σ⁻¹`, for A = 2, 3, 4, 6. Only the single
1-strand component is unknotted. **The conclusion is unaffected** — splitness is
already enough, and local knotting changes no Milnor invariant — but the invariant
being cited was the wrong one, and a wrong citation is worth fixing even when the
verdict survives.

`separated_of_delta_zero` is that step, and it is the whole content. It needs no
path structure and no minimality — only that a shared summand implies nonzero
linking. The path and the min-span family enter as the *instance*: measured, **0**
generators join two members of any `{i, i+2, i+4}` triple on A = 8, 10, 12, 16, and
that measurement is **branch-independent**, since which components a generator
touches is fixed by the permutation and does not depend on how the superposition
letters resolve to crossing signs (unlike `lk` itself).

**What this is not.** It does not say Milnor invariants are useless on every
carrier — on a genuinely Brunnian link like L6a4 the summand hypothesis fails and
`μ̄₁₂₃ = 1`. It says this *particular* carrier, being a connected sum along a path,
puts "defined" and "zero" on the same condition. Nor does it touch the `Δ = 2`
triples, which touch a linked pair and retain one bit; those are **not** covered
here and are the residual.

SCOPE — **scope-(b)** on the min-span family, invariant cited: Milnor invariants of
length ≥ 2 vanish on a **split** link, together with the connected-sum decomposition
of a monotone braid closure. It excludes *this family as a source of a binding term*. It does not
refute route 3 in general, and it does not touch the `Δ = 2` one-bit triples.

**Deliberately not formalised.** Milnor's `μ̄` itself, the connected-sum
decomposition, and "invariants vanish on a split link". None is cheaply available in
this Mathlib, and asserting them as a `class` would be the
axiomatisation-is-not-a-proof pattern. They are carried as the *stated* topological
reason; what is machine-checked is the combinatorial step that converts the
defining condition into separation, plus the min-span family's non-adjacency. The
halves are kept separate on purpose, as in the sibling
`FreedmanHeGenusHandleNeedsVanishingLinking.lean`.

Base ring: `ℤ` — linking numbers are integers and the content is which ones vanish.
No ordering or ring generality is used, so per AGENTS.md §7c neither is assumed.
-/
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Linarith

namespace QOU.Mass.MilnorTriplesAreDefinedExactlyWhereTheyVanish

/-- Two components are **joined** when some summand of the connected-sum
decomposition touches both.

On the derived carrier a summand is one generator's run, so it touches only the
components containing strands `g` and `g+1` — measured at most two, on
A = 2, 4, 6, 8, 10. The single hypothesis `joins_linked` is what the topology
supplies: a shared `(2, k)` torus summand links the two components it joins. -/
structure Summands where
  /-- some summand of the connected sum touches both components -/
  joins : ℕ → ℕ → Prop
  /-- linking numbers of the closure -/
  lk : ℕ → ℕ → ℤ
  /-- sharing a summand makes two components linked -/
  joins_linked : ∀ i j, joins i j → lk i j ≠ 0

/-- **The result, and it is the whole file.** A triple on which `μ̄` is a genuine
integer — `Δ = gcd(lk_ij, lk_jk, lk_ki) = 0`, i.e. all three pairwise linking
numbers vanish — shares **no** summand between any two of its members.

Its sublink is therefore **split**, and every Milnor invariant of length ≥ 2 vanishes
on a split link — whatever the individual components are knotted as (measured: they
are `(2, odd)`-torus knots, not unknots; local knotting changes no Milnor invariant). So on this carrier the condition that makes `μ̄` *defined* is the condition
that makes it *zero*.

Needs no path structure, no minimality, and no `Δ`-arithmetic: it is exactly the
contrapositive of `joins_linked`, which is why the result is as general as the
connected-sum decomposition itself. -/
theorem separated_of_delta_zero (S : Summands) {a b c : ℕ}
    (hab : S.lk a b = 0) (hbc : S.lk b c = 0) (hca : S.lk c a = 0) :
    ¬ S.joins a b ∧ ¬ S.joins b c ∧ ¬ S.joins c a :=
  ⟨fun h => S.joins_linked a b h hab,
   fun h => S.joins_linked b c h hbc,
   fun h => S.joins_linked c a h hca⟩

/-- Adjacency on the path `P_μ` that the derived carrier's linking graph is
measured to be: `lk ≠ 0` exactly on consecutive components. -/
def Adjacent (i j : ℕ) : Prop := j = i + 1 ∨ i = j + 1

/-- `Adjacent` is a disjunction of `ℕ`-equalities, so it decides — but the `def`
opaques it to instance synthesis, which is what the witness below needs. -/
instance (i j : ℕ) : Decidable (Adjacent i j) := by
  unfold Adjacent; infer_instance

/-- **The min-span family is pairwise non-adjacent.** `{i, i+2, i+4}` is the
tightest triple with this property, which is why `qou-768r` names it: it is the
smallest family that is Milnor-*defined*, and it is the only one whose count
(`A − 3`, per-component multiplicity ≤ 3) survives `CoordinationSaturation`. -/
theorem minSpan_pairwise_not_adjacent (i : ℕ) :
    ¬ Adjacent i (i + 2) ∧ ¬ Adjacent (i + 2) (i + 4) ∧ ¬ Adjacent (i + 4) i := by
  refine ⟨?_, ?_, ?_⟩ <;> rintro (h | h) <;> omega

/-- The path carrier: `lk` vanishes off consecutive pairs. Stated as the direction
actually used — non-adjacent implies unlinked — rather than as an `iff`, so the
theorem below does not silently require more than the measurement supports. -/
structure PathCarrier extends Summands where
  /-- non-consecutive components are unlinked -/
  lk_zero_of_not_adjacent : ∀ i j, ¬ Adjacent i j → lk i j = 0

/-- **Applied to the carrier.** Every min-span triple is separated, hence carries
`μ̄ = 0`. Independently measured on the braid words themselves: **0** generators
join two members of any `{i, i+2, i+4}` triple, on A = 8, 10, 12, 16 — and that
measurement is branch-independent, since which components a generator touches is
fixed by the permutation, not by how the superposition letters resolve. -/
theorem minSpan_separated (P : PathCarrier) (i : ℕ) :
    ¬ P.joins i (i + 2) ∧ ¬ P.joins (i + 2) (i + 4) ∧ ¬ P.joins (i + 4) i := by
  obtain ⟨h1, h2, h3⟩ := minSpan_pairwise_not_adjacent i
  exact separated_of_delta_zero P.toSummands
    (P.lk_zero_of_not_adjacent _ _ h1)
    (P.lk_zero_of_not_adjacent _ _ h2)
    (P.lk_zero_of_not_adjacent _ _ h3)

/-- **The statement is not vacuous**: a configuration satisfying every hypothesis
exists, with `joins` inhabited on the consecutive pairs it is supposed to be
inhabited on. Recorded so `minSpan_separated` cannot be read as holding because
nothing can satisfy `PathCarrier`. -/
def chainCarrier : PathCarrier where
  joins i j := Adjacent i j
  lk i j := if Adjacent i j then -2 else 0
  joins_linked i j h := by simp [h]
  lk_zero_of_not_adjacent i j h := by simp [h]

/-- …and its `joins` really does hold somewhere — the consecutive pairs are joined,
so the separation result above is cutting something out rather than describing an
empty relation. -/
theorem chainCarrier_joins_consecutive (i : ℕ) : chainCarrier.joins i (i + 1) :=
  Or.inl rfl

end QOU.Mass.MilnorTriplesAreDefinedExactlyWhereTheyVanish
