import Mathlib.Tactic

/-!
# QOU.Conjectures.MagicNumbersBring — magic numbers as S₅-stable lattice ranks

Conjectural axiomatisation of `conj:magic-numbers-bring`
(`folio/quantum-observable-universe/observations/magic-numbers-bring.md`).

The seven observed nuclear magic numbers
`𝔐 = {2, 8, 20, 28, 50, 82, 126}` are the ranks of seven distinguished
`S₅`-stable, `τ̂`-stable period sub-lattices of (powers of) the integer
homology `H₁(𝓑, ℤ)` of Bring's genus-4 curve.  The conjecture asserts a
**rank-preserving bijection** between the magic-number set and a family
of such lattices: for each magic `n` there is a lattice `L n` whose
`ℤ`-rank is exactly `n`.

The conjecture itself is encoded as a `class` (AGENTS.md §3b / §3b-tax);
its field carries the genuine rank-equality content, not a bare `True`.
An unproved primary conjecture is honestly represented by a
content-bearing class with **no instance** (the open state); the Phase-2
period-lattice computation that would provide an instance is deferred
(workplan P1.4).

LaTeX label: `conj:magic-numbers-bring`

## References

- [leitner2026] §"Magic numbers from Bring's surface"
- [klein1888] Klein, classification of S₅-stable sub-lattices on Bring's curve
-/

namespace QOU.Conjectures

/-- The seven observed nuclear magic numbers `{2, 8, 20, 28, 50, 82, 126}`. -/
def magicNumbers : List ℕ := [2, 8, 20, 28, 50, 82, 126]

/-- **Conjecture class** (`conj:magic-numbers-bring`).

An instance asserts a rank-`n` integer lattice `magicLattice n` (a
distinguished `S₅`-stable, `τ̂`-stable period sub-lattice of a power of
`H₁(𝓑, ℤ)`) for every magic number `n ∈ magicNumbers`, whose `ℤ`-rank
**equals** `n`.

The field `rank_eq_magic` carries the conjecture's genuine content — the
rank-preserving bijection between magic numbers and the distinguished
lattices — rather than a bare `True`.  This is a **primary** conjecture
(its signature takes no other conjecture class as a hypothesis). -/
class MagicNumbersBring where
  /-- The distinguished `S₅`-stable, `τ̂`-stable period sub-lattice
      attached to a magic number, presented by its `ℤ`-rank. -/
  magicLattice : ℕ → ℕ
  /-- **Conjectural rank identity.**  For every magic number `n`, the
      attached distinguished lattice has `ℤ`-rank exactly `n` — the
      rank-preserving bijection `𝔐 ↔ {Lₙ}`. -/
  rank_eq_magic : ∀ n ∈ magicNumbers, magicLattice n = n

-- No instance: this is an OPEN primary conjecture (AGENTS.md §3b-tax).
-- The identity model (`magicLattice n := n`) discharges `rank_eq_magic`
-- by `rfl` for ANY set of naturals — it constructs no actual
-- S₅-stable period sub-lattice of Bring's curve, so it captures none of
-- the conjecture's content.  The Phase-2 period-lattice computation
-- that would supply a genuine instance is deferred (workplan P1.4).

end QOU.Conjectures
