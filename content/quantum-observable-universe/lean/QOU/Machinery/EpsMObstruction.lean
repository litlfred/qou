/-
# The ε_m canonical-cocycle obstruction — Frobenius shift law and the obstruction form

Backbone for the ε_m descent programme (bean qou-y3xv; audit
`docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md`
Addenda 21–23). The compute layers measured these facts across
unramified fields of degree up to 96 and in the residue field 𝔽₂₅;
this file proves the algebra behind them once, generically, so the
probes rest on a proved backbone rather than a per-run coincidence.

Two independent pieces:

* **`frobenius_shift`** — the closed form for the shift exponent. The
  Galois generator σ = φ₅² acts on μ₂₄ₘ by ζ ↦ ζ²⁵, so an m-th root
  written as `ζ ^ e` is moved by exactly `(ζ ^ 24) ^ e`, and `ζ ^ 24`
  has order m. This is what turns a per-field measurement of the shift
  exponent into the residue-field discrete logarithm `r(w) = e(w) mod m`
  — the step that let the whole m | 24 lattice be recomputed in 𝔽₂₅.
  Stated over a generic `CommGroup` per §7c: no p-adic or archimedean
  structure enters.

* **The obstruction form `qSymbol`** — `Q([w]) = e(w)·e(1−w)` in
  `ZMod 24`, with the three facts the compute layer relies on:
  `qSymbol_rescale` (independence of the discrete-logarithm generator,
  because every unit of `ZMod 24` squares to 1), `reflection_even` (the
  reflection relation contributes an even amount), and
  `inversion_closed_form` + `inversion_even_iff` (the derived inversion
  relation's exact value `a² − 12a`, which is even **iff** a is — the
  fact that refuted an earlier parity claim of mine and confined the
  parity statement to the defining five-term relation).

`clearable_of_even` is the last logical step: an even obstruction can
always be cancelled by an even shift.

HONESTY (STRICT): sorry-free, no axioms beyond Lean's, no `native_decide`.
The `decide` uses discharge genuinely finite computations over `ZMod 24`
(the ring is `Fintype`), never a structural claim. Nothing here asserts
that ε_m *is* any particular value — that is compute, and it is not
wired.

-- Ref: [suslin1991] https://doi.org/10.1090/S0002-9947-1991-1044046-0
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Tactic.Ring

namespace QOU.Machinery.EpsMObstruction

/-! ## The Frobenius shift law -/

/-- **The shift law.** With σ acting by `g ↦ g ^ 25` (the Galois
generator φ₅² on roots of unity at the prime 5), an element written as
`ζ ^ e` is moved by exactly `(ζ ^ 24) ^ e`:

    σ(ζ ^ e) = (ζ ^ 24) ^ e * (ζ ^ e).

Generic `CommGroup`; no arithmetic hypotheses are needed, the identity
is pure exponent bookkeeping. -/
theorem frobenius_shift {G : Type*} [CommGroup G] (ζ : G) (e : ℕ) :
    (ζ ^ e) ^ 25 = (ζ ^ 24) ^ e * ζ ^ e := by
  rw [← pow_mul, ← pow_mul, ← pow_add]
  ring_nf

/-- The shift factor `ζ ^ 24` has order exactly `m` when `ζ` has order
`24 * m` — so the shift really does land in `μ_m`, which is what makes
the shift exponent well defined mod `m`. (No `m ≠ 0` hypothesis is
needed: the infinite-order case `m = 0` holds too.) -/
theorem orderOf_shift_factor {G : Type*} [CommGroup G] (ζ : G) (m : ℕ)
    (hord : orderOf ζ = 24 * m) :
    orderOf (ζ ^ 24) = m := by
  have h24 : (24 : ℕ) ∣ orderOf ζ := ⟨m, hord⟩
  rw [orderOf_pow_of_dvd (by norm_num) h24, hord]
  omega

/-! ## The obstruction form -/

/-- The obstruction contribution of one Bloch symbol `[w]`: the product
of the Teichmüller discrete logarithms of `w` and of `1 - w`, taken in
`ZMod 24` (the base Teichmüller group at the prime 5 is `μ₂₄`). -/
def qSymbol (ew e1w : ZMod 24) : ZMod 24 := ew * e1w

/-- Every unit of `ZMod 24` squares to `1` — the group of units is
elementary abelian. This is what makes `qSymbol` independent of which
generator is used for the discrete logarithm. -/
theorem unit_sq_eq_one (u v : ZMod 24) (h : u * v = 1) : u ^ 2 = 1 := by
  revert h
  revert v
  revert u
  decide

/-- **Generator independence.** Rescaling the discrete logarithm by a
unit `u` (i.e. choosing a different generator of `μ₂₄`) leaves the
obstruction form unchanged, because `u ^ 2 = 1`. -/
theorem qSymbol_rescale (u a b : ZMod 24) (hu : u ^ 2 = 1) :
    qSymbol (u * a) (u * b) = qSymbol a b := by
  unfold qSymbol
  have h : u * a * (u * b) = u ^ 2 * (a * b) := by ring
  rw [h, hu, one_mul]

/-- **The reflection relation is even.** `[x] + [1 - x]` contributes
`2 * (a * b)`, where `a = e(x)` and `b = e(1 - x)`: the two symbols
carry the same pair of logarithms in opposite order. -/
theorem reflection_even (a b : ZMod 24) :
    qSymbol a b + qSymbol b a = 2 * (a * b) := by
  unfold qSymbol
  ring

/-- **The inversion relation's closed form.** With `e(1/x) = -a` and
`e(1 - 1/x) = 12 + b - a` (the second from `1 - 1/x = -(1-x)/x` together
with `e(-1) = 12`), the pair `[x] + [1/x]` contributes exactly
`a ^ 2 - 12 * a`. -/
theorem inversion_closed_form (a b einv e1inv : ZMod 24)
    (hinv : einv = -a) (h1inv : e1inv = 12 + b - a) :
    qSymbol a b + qSymbol einv e1inv = a ^ 2 - 12 * a := by
  subst hinv
  subst h1inv
  unfold qSymbol
  ring

/-- **The inversion contribution is even exactly when `a` is.** This is
why the parity of the obstruction form is *not* preserved by the derived
inversion relation, and hence why the parity statement is confined to the
defining five-term relation: inversion holds in the Bloch group only
modulo torsion, and `ZMod 24` sees precisely that torsion. -/
theorem inversion_even_iff (a : ZMod 24) :
    (∃ k : ZMod 24, a ^ 2 - 12 * a = 2 * k) ↔ (∃ j : ZMod 24, a = 2 * j) := by
  revert a
  decide

/-- **Clearability.** An even obstruction can always be cancelled by an
even shift — the last step of the representative-change argument, which
uses only shifts realised by the defining five-term relation (all of
which are even). -/
theorem clearable_of_even (q : ZMod 24) (hq : ∃ j : ZMod 24, q = 2 * j) :
    ∃ s : ZMod 24, (∃ k : ZMod 24, s = 2 * k) ∧ q + s = 0 := by
  obtain ⟨j, rfl⟩ := hq
  exact ⟨-(2 * j), ⟨-j, by ring⟩, by ring⟩

end QOU.Machinery.EpsMObstruction
