/-
QOU.Mass.ChainTripleMilnorVanishesByGcdDividesProduct — route 3's last residual closes,
and it needs no connected-sum citation: the chain triple's Magnus coefficient is the
PRODUCT of its two linking numbers, and `gcd u v ∣ u * v` always.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-2g9j`). The sibling
`OneSeparatedComponentSufficesForMilnorVanishing.lean` covers 393 of the derived
carrier's 424 triples and proves the remaining 31 are exactly the **chain**
`{i, i+1, i+2}` — one hub linked to two ends that are unlinked from each other. That
file leaves the chain open and names what would close it: *"`μ̄` of length `k` vanishes
unless all `k` indices lie in a single connected-sum summand"*, a statement no held
source in this corpus states.

**It is not needed.** The chain closes on a divisibility fact, from a much smaller
measured input.

**The measured input.** Write `u = lk(hub, x)`, `v = lk(hub, y)`, and note the third
linking number `lk(x, y) = 0` by the chain hypothesis, so
`Δ = gcd(u, v, 0) = gcd(u, v)`. On a **monotone** closure the two far components'
meridians occupy two *contiguous, non-interleaved* blocks of the hub's longitude — one
run per generator is exactly what monotone means — so the degree-2 Magnus coefficient
is a product of block sums rather than an interleaved count:

    ε_{x,y}(λ_hub) = u · v        ε_{y,x}(λ_hub) = 0

Measured on **596/596** monotone chain triples: 62 on the derived carrier (7 isotopes,
both crossing-resolution branches) and 534 from random monotone braid closures. Off
monotone it fails — 22/78 and 29/78 respectively — which is precisely where
monotonicity enters.

**The conclusion, and it is unconditional.** `gcd u v ∣ u` and `u ∣ u * v`, so
`Δ ∣ ε` whatever `u` and `v` are. Milnor's `μ̄` is defined modulo `Δ`; hence it vanishes
on every chain triple of a monotone closure. `chain_mubar_vanishes` is that step and is
the whole file.

**Why the ORDER-DEPENDENCE is not a defect but the point.** `ε_{x,y} = u·v` while
`ε_{y,x} = 0`: the raw integer depends on the index order, which looks alarming for
something called an invariant. That dependence is exactly what the mod-`Δ`
indeterminacy exists to absorb — **both** values are divisible by `Δ`
(`both_orderings_vanish`), so the invariant is well defined and zero either way. A
scan that symmetrises and happens to land on the `0` branch sees an honest integer zero
and can mistake a general mechanism for a coincidence; that happened here, and it is
recorded in the companion probe.

**What this does and does not settle.** Together with the sibling file, every triple of
the derived carrier is now covered: 393 by one separated component, 31 by this. It does
**not** prove the measured input — that a monotone closure's hub longitude splits into
two non-interleaved blocks — which is carried as a structural hypothesis in
`ChainTriple.eps_eq`, exactly as the sibling carries the split-link vanishing. It is a
far smaller and more concrete input than the connected-sum statement it replaces, and
unlike that statement it is checkable by counting: 596/596, with the off-monotone
failure as its control.

**The off-monotone control is a genuine counterexample, and it is what makes `eps_eq`
load-bearing.** Of 78 non-monotone chain triples exactly **one** has `Δ ≥ 2`, and
divisibility **fails** on it (77 of 78 divisible) — a real chain triple carrying nonzero
`μ̄`. The other 77 sit at `Δ = 1`, where `1` divides everything and the statement is
vacuous, so report the two separately or the arm reads as stronger than it is. On the
monotone side it is not vacuous: `Δ ≥ 2` on 62/62 carrier and 144/534 random chain
triples.

`without_eps_eq_the_conclusion_fails` is the Lean witness of that counterexample's
shape: with `eps` free of `u * v`, `Δ = 2` need not divide it.

SCOPE — **scope-(b)** on the chain triples, invariant cited: `gcd u v ∣ u * v`, together
with the measured block structure of a monotone closure's longitudes. It excludes the
consecutive triples as a source of a binding term.

**Deliberately not formalised**, as in the two siblings: Milnor's `μ̄` itself, the Magnus
expansion, and the block structure. What is machine-checked is the arithmetic that
converts the measured coefficient into a vanishing invariant.

Base ring: `ℤ`, genuinely — linking numbers are integers, the coefficient is an integer,
and the content is a divisibility among them.
-/
import Mathlib.Data.Int.GCD
import Mathlib.Tactic.Linarith

namespace QOU.Mass.ChainTripleMilnorVanishesByGcdDividesProduct

/-- A **chain triple** on a monotone closure: a hub linked to two ends `x, y` that are
unlinked from each other, together with the degree-2 Magnus coefficient of the hub's
longitude.

`eps_eq` is the measured structural input and the only place monotonicity enters: one
run per generator puts the two far meridians in contiguous, non-interleaved blocks of
`λ_hub`, so the coefficient is a product of block sums. Verified on 596/596 monotone
chain triples; it fails off monotone. -/
structure ChainTriple where
  /-- `lk(hub, x)` — nonzero by the chain hypothesis, though nothing below needs that -/
  u : ℤ
  /-- `lk(hub, y)` -/
  v : ℤ
  /-- the degree-2 Magnus coefficient `ε_{x,y}(λ_hub)` -/
  eps : ℤ
  /-- MEASURED (596/596 monotone): the far meridians are non-interleaved, so the
  coefficient is the product of the two linking numbers -/
  eps_eq : eps = u * v

/-- Milnor's indeterminacy for a chain triple. The third linking number vanishes by the
chain hypothesis, so `Δ = gcd(u, v, 0)` collapses to `gcd(u, v)`. -/
def delta (C : ChainTriple) : ℤ := (Int.gcd C.u C.v : ℤ)

/-- **The result, and it is the whole file.** `μ̄` is defined modulo `Δ`, and `Δ` divides
the chain triple's coefficient — so `μ̄ = 0` there.

The proof is `gcd u v ∣ u ∣ u * v`. It is unconditional in `u` and `v`: no positivity,
no primality, no bound on the linking numbers. All the content sits in `eps_eq`, which
is where monotonicity was used. -/
theorem chain_mubar_vanishes (C : ChainTriple) : delta C ∣ C.eps := by
  rw [C.eps_eq]
  exact Dvd.dvd.mul_right (Int.gcd_dvd_left C.u C.v) C.v

/-- The reverse ordering `ε_{y,x}(λ_hub)` is measured to be `0` (596/596), and `Δ`
divides that too — trivially.

Stated because the raw coefficient is order-DEPENDENT (`u·v` one way, `0` the other),
which is alarming until one notices that this is exactly what the mod-`Δ` indeterminacy
absorbs: the invariant is well defined and zero under **both** orderings, so nothing
about the vanishing depends on a convention. -/
theorem both_orderings_vanish (C : ChainTriple) (epsRev : ℤ) (hrev : epsRev = 0) :
    delta C ∣ C.eps ∧ delta C ∣ epsRev :=
  ⟨chain_mubar_vanishes C, hrev ▸ dvd_zero _⟩

/-- **Not vacuous**: an instance with `Δ ≥ 2` and a genuinely nonzero coefficient,
matching the carrier's measured values (`lk = ±2` on consecutive components, all-`σ⁻¹`
branch). Recorded so `chain_mubar_vanishes` cannot be read as holding because the
coefficient is always zero — here it is `4`, and `Δ = 2` divides it. -/
def carrierChain : ChainTriple where
  u := -2
  v := -2
  eps := 4
  eps_eq := by norm_num

theorem carrierChain_delta_eq_two : delta carrierChain = 2 := by
  simp [delta, carrierChain]

theorem carrierChain_eps_ne_zero : carrierChain.eps ≠ 0 := by decide

/-- …and the divisibility genuinely fires on it: `2 ∣ 4`. -/
theorem carrierChain_vanishes : delta carrierChain ∣ carrierChain.eps :=
  chain_mubar_vanishes carrierChain

/-- **The hypothesis is what carries the content, not the arithmetic.** With `eps` free
of `u * v` the conclusion can fail — `Δ = 2` does not divide `3`. Recorded so
`chain_mubar_vanishes` is visibly a statement about `eps_eq` rather than a triviality
that would hold for any coefficient whatsoever. -/
theorem without_eps_eq_the_conclusion_fails :
    ¬ ((Int.gcd (-2 : ℤ) (-2) : ℤ) ∣ (3 : ℤ)) := by decide

end QOU.Mass.ChainTripleMilnorVanishesByGcdDividesProduct
