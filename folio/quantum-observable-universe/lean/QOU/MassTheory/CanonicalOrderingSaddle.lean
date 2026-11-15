import QOU.MassTheory.NucleonOrderingSymmetry
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.List.Perm.Basic
import Mathlib.Data.List.Count
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.MassTheory.CanonicalOrderingSaddle

**The canonical nucleon arrangement `p…pn…n` is a SADDLE of the production
interface product — so no extremal principle selects it.**

Bean `qou-48is` (spun out of `qou-prjo` by PR #4850 §7). Companion to
[`NucleonOrderingSymmetry`](NucleonOrderingSymmetry.lean), which proves the
prior half: the corpus's orbit identity ranges over `S_Z × S_N`, under which the
braid word is *literally fixed*, so it licenses nothing about the cross-species
arrangement.

## The object

The production `A ≥ 3` binding chain
(`mass_table_comprehensive` → `binding_canonical(use_closed_form=True)` →
`closed_form_tau_M` → `closed_form_ratio`) multiplies one factor per adjacent
nucleon pair — `f_pp` at a p-p boundary, `f_nn` at an n-n boundary, `f_pn` at a
mixed one — over a **hardcoded** ordering `["p"] * Z + ["n"] * N`. `ifaceProd`
below is exactly that product, with the ordering supplied as a parameter.

## What is proved

* `ifaceProd_eq_of_ifaces_perm` — the product is a function of the interface
  **multiset** alone. (This is the true premise of the "the multiset is the
  physical datum" resolution.)
* `ifaces_not_determined_by_species_counts` — but the multiset is **not** an
  invariant of the isotope: two arrangements of the same `(Z, N)` realise
  different multisets. So that resolution re-coordinatises the freedom rather
  than removing it.
* `ifaceProd_deuteron_ordering_independent` — the deuteron is the null control:
  its two arrangements share one interface, so `A = 2` is exactly
  ordering-independent. The freedom switches on at `A ≥ 3`.
* `canonical_saddle` / `canonical_not_extremal` — **the main result.** If
  `f_pn < f_pp` and `f_nn < f_pn` (both hold at the substrate anchor: measured
  `f_pp = 0.4993…`, `f_pn = 0.3948…`, `f_nn = 0.2903…`), then among the
  arrangements of *two protons and two neutrons* one lies strictly **below** the
  canonical `ppnn` and another strictly **above** it. The canonical arrangement
  is therefore neither a maximum nor a minimum — it is a saddle, and no
  extremising principle can pick it out.

## What is NOT proved — read before citing

* **`sorry-free ≠ derived`.** Nothing here derives a magnitude: no binding
  energy, no `Δ_λ`, no `tr_M` value, and no comparison to AME. The content is
  the *shape* of the ordering dependence, not any number.
* **This does not show the arrangement is undeterminable.** It refutes the
  extremal-principle route and the multiset-invariance route. A selection rule
  of a different kind — a confinement/SDP argument, a Markov-move or normal-form
  argument, a coordination-graph constraint — is untouched. Scope-(a) for that
  broader claim; only `canonical_saddle` itself is a scope-(b) exclusion, and it
  excludes exactly one thing: *extremality*.
* **The two inequalities are HYPOTHESES, not corpus facts imported into Lean.**
  `canonical_saddle` proves an implication. Its antecedent is verified
  numerically at the experimental proton anchor by
  `computations/probes/canonical_ordering_dof_probe.py`; cite the two together,
  and cite this theorem as the conditional it is.

**Base ring (§7c).** `ifaceProd` and the multiset lemmas are over a generic
`[CommMonoid R]` — no ring, no `ℝ`. Only `canonical_saddle` needs an order, and
it takes the weakest generic form (`[CommRing R] [LinearOrder R]
[IsStrictOrderedRing R]`) rather than specialising to `ℝ`.

## References
- Ref: [leitner2026] `docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md`
- Ref: [leitner2026] `docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md` §7
-/

namespace QOU.MassTheory.NucleonOrdering

open Species Iface

/-! ## 1. The production interface product -/

/-- The per-interface product of `closed_form_tau_M.closed_form_ratio`, with the
arrangement supplied instead of hardcoded: one factor `f` per adjacent pair,
indexed by that pair's interface type. -/
def ifaceProd {R : Type*} [CommMonoid R] (f : Iface → R) (ss : List Species) : R :=
  ((ifaces ss).map f).prod

/-- **The product is a function of the interface multiset alone.** Rearranging
the interface list — by any permutation whatever — leaves the product fixed.

This is the exact premise of the "the physical datum is the multiset, so the
ordering is a redundant labelling" resolution. It is true. §2 shows why it is
not enough. -/
theorem ifaceProd_eq_of_ifaces_perm {R : Type*} [CommMonoid R] (f : Iface → R)
    {ss tt : List Species} (h : (ifaces ss).Perm (ifaces tt)) :
    ifaceProd f ss = ifaceProd f tt :=
  (h.map f).prod_eq

/-! ## 2. The multiset is not an invariant of the isotope -/

/-- Two arrangements of **two protons and two neutrons** — the same isotope — with
different interface multisets: `ppnn ↦ [pp, pn, nn]` carries a `pp` interface,
`pnnp ↦ [pn, nn, pn]` carries none.

So "the observable depends only on the interface multiset" does **not** make the
observable a function of `(Z, N)`. The freedom is merely re-coordinatised: from
*which arrangement* to *which multiset*. -/
theorem ifaces_not_determined_by_species_counts :
    ([Species.p, Species.p, Species.n, Species.n] : List Species).count Species.p
        = ([Species.p, Species.n, Species.n, Species.p] : List Species).count Species.p
      ∧ ([Species.p, Species.p, Species.n, Species.n] : List Species).count Species.n
        = ([Species.p, Species.n, Species.n, Species.p] : List Species).count Species.n
      ∧ (ifaces [Species.p, Species.p, Species.n, Species.n]).count Iface.pp
        ≠ (ifaces [Species.p, Species.n, Species.n, Species.p]).count Iface.pp := by
  decide

/-- Hence the two interface lists are not even permutations of one another: the
`ifaceProd` values are genuinely allowed to differ, and §3 shows they do. -/
theorem ifaces_ppnn_not_perm_ifaces_pnnp :
    ¬ (ifaces [Species.p, Species.p, Species.n, Species.n]).Perm
        (ifaces [Species.p, Species.n, Species.n, Species.p]) := by
  intro h
  exact ifaces_not_determined_by_species_counts.2.2 (h.count_eq Iface.pp)

/-- **Null control.** The deuteron's two arrangements have the *same* single
interface, so the product is invariant — exactly, for every `f`. The ordering
freedom does not exist at `A = 2`; it switches on at `A ≥ 3` with both species
present. -/
theorem ifaceProd_deuteron_ordering_independent {R : Type*} [CommMonoid R]
    (f : Iface → R) :
    ifaceProd f [Species.p, Species.n] = ifaceProd f [Species.n, Species.p] := by
  simp [ifaceProd, ifaces, iface]

/-! ## 3. The canonical arrangement is a saddle -/

section Ordered

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The canonical arrangement is strictly interior.**

Fix two protons and two neutrons. If the mixed factor is smaller than the p-p
one and larger than the n-n one — `f_nn < f_pn < f_pp`, which is what the
substrate anchor delivers — then

* `pnnp` (which trades the canonical `pp` interface for a second `pn`) sits
  strictly **below** the canonical `ppnn`, and
* `nppn` (which trades the canonical `nn` interface for a second `pn`) sits
  strictly **above** it.

The two trades push in opposite directions precisely because `f_pn` lies
*between* `f_pp` and `f_nn`. The canonical arrangement is therefore a saddle of
the arrangement-indexed product, not an extremum of it. -/
theorem canonical_saddle (f : Iface → R)
    (hpp : 0 < f Iface.pp) (hnn : 0 < f Iface.nn) (hpn : 0 < f Iface.pn)
    (hlo : f Iface.pn < f Iface.pp) (hhi : f Iface.nn < f Iface.pn) :
    ifaceProd f [Species.p, Species.n, Species.n, Species.p]
        < ifaceProd f [Species.p, Species.p, Species.n, Species.n]
      ∧ ifaceProd f [Species.p, Species.p, Species.n, Species.n]
        < ifaceProd f [Species.n, Species.p, Species.p, Species.n] := by
  have e_can : ifaceProd f [Species.p, Species.p, Species.n, Species.n]
      = f Iface.pp * (f Iface.pn * f Iface.nn) := by
    simp [ifaceProd, ifaces, iface]
  have e_lo : ifaceProd f [Species.p, Species.n, Species.n, Species.p]
      = f Iface.pn * (f Iface.nn * f Iface.pn) := by
    simp [ifaceProd, ifaces, iface]
  have e_hi : ifaceProd f [Species.n, Species.p, Species.p, Species.n]
      = f Iface.pn * (f Iface.pp * f Iface.pn) := by
    simp [ifaceProd, ifaces, iface]
  rw [e_can, e_lo, e_hi]
  constructor
  · nlinarith [mul_pos hpn hnn, mul_pos hpp hpn]
  · nlinarith [mul_pos hpp hpn, mul_pos hpn hnn]

/-- **No extremal principle selects the canonical arrangement.**

Restated as the claim it is used for: within the *same isotope* — the same
multiset of nucleon species, so the same `(Z, N)` — there is an arrangement
strictly below the canonical one and an arrangement strictly above it. Hence the
canonical arrangement is neither the minimiser nor the maximiser of the
production interface product, and a variational selection rule of either sign
cannot pick it out.

Scope-(b) exclusion, and it excludes exactly one candidate: *extremality*. It
says nothing about selection rules of other kinds. -/
theorem canonical_not_extremal (f : Iface → R)
    (hpp : 0 < f Iface.pp) (hnn : 0 < f Iface.nn) (hpn : 0 < f Iface.pn)
    (hlo : f Iface.pn < f Iface.pp) (hhi : f Iface.nn < f Iface.pn) :
    (∃ ss : List Species, ss.Perm [Species.p, Species.p, Species.n, Species.n]
        ∧ ifaceProd f ss < ifaceProd f [Species.p, Species.p, Species.n, Species.n])
      ∧ (∃ ss : List Species, ss.Perm [Species.p, Species.p, Species.n, Species.n]
        ∧ ifaceProd f [Species.p, Species.p, Species.n, Species.n] < ifaceProd f ss) := by
  obtain ⟨hbelow, habove⟩ := canonical_saddle f hpp hnn hpn hlo hhi
  refine ⟨⟨[Species.p, Species.n, Species.n, Species.p], ?_, hbelow⟩,
          ⟨[Species.n, Species.p, Species.p, Species.n], ?_, habove⟩⟩
  · decide
  · decide

end Ordered

end QOU.MassTheory.NucleonOrdering
