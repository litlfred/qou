import QOU.Hecke.MarkovTrace
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel

/-!
# QOU.Hecke.MarkovBondFactor — the per-bond trace factor `tr_M(c·σ + d) = c·z + d`

> **STATUS (2026-09-13) — both theorems machine-verified in this file, against
> its real import cone.** Superseding the 2026-06-10 note below:
> `lean -DautoImplicit=false -s 65536 QOU/Hecke/MarkovBondFactor.lean` is
> **exit 0 in 2.8 s**, and `#print axioms` on **both** `trace_bond_crossing`
> and `trace_bond_pair_factorizes` gives `[propext, Classical.choice,
> Quot.sound]` — no `sorry`, no `sorryAx`.
>
> Two claims in the old note were true when written and are now stale.
> `trace_bond_pair_factorizes` was recorded as *"drafted; its `ring`/`abel` step
> is not yet machine-confirmed — the restored Mathlib cache is missing
> `Mathlib.Tactic.Ring`/`Abel`"*: the cache carries them now and the step
> elaborates. And `trace_bond_crossing` was verified *"standalone … with a
> minimal stand-in class"*; it is now verified against the real
> `MarkovTrace`/`HeckeAlgebra` classes of this file, which is the stronger
> check. (The old note's `[propext, Quot.sound]` reflects the stand-in harness;
> the real cone adds `Classical.choice`.)
>
> **Still true:** the module is **standalone — imported by nobody** (grep over
> `content/**/*.lean`: zero `import QOU.Hecke.MarkovBondFactor`). Whether to
> re-wire it into the `QOU.Hecke` aggregator is a build-graph decision and is
> deliberately **not** taken here.
>
> Original note, kept for the record:
> - `trace_bond_crossing` (the per-bond factor `tr_M(c·σ+d) = c·z+d`) is
>   **MACHINE-VERIFIED** — its proof logic was elaborated standalone against
>   Mathlib on lean v4.24.0 with a minimal stand-in class carrying the same
>   `MarkovTrace` fields; `#print axioms` = `[propext, Quot.sound]` only
>   (no `sorry`, no `sorryAx`). The per-bond Markov factor is a proven theorem.
> - `trace_bond_pair_factorizes` (two-bond) proof is drafted; its `ring`/`abel`
>   step is **not yet** machine-confirmed — the sandbox's restored Mathlib
>   cache is missing `Mathlib.Tactic.Ring`/`Abel` and a full rebuild timed out.
> - Module kept **standalone (NOT imported by the `QOU.Hecke` aggregator)** so
>   no proof error can break the QOU package build. A full in-repo `lake build`
>   is currently blocked by an UNRELATED upstream failure in
>   `QOU.Hecke.Generators` (a restored-cache / Mathlib-consistency artifact, not
>   this module). Re-wire into `QOU/Hecke.lean` once `lake build QOU` is green.
>   See `docs/audits/2026-06-10-binding-bond-graph-compute-audit-and-derivation.md` §7.

An inter-nucleon bond in the atom braid is a bridge crossing
`c • σ_i + d • 1` (p-p: `(1, 0)`; n-n: `(1, −h)`; p-n: `(1, −h(½−δ/4))`).
Its Markov-trace value is the *conditional expectation* of the crossing:

  `tr_M(c • σ_i + d • 1) = c · z + d`        (one bond)

and for two bridge crossings at generators `i < j` the trace
*factorizes over bonds*:

  `tr_M((c₁ • σ_i + d₁) · (c₂ • σ_j + d₂)) = (c₁·z + d₁) · (c₂·z + d₂)`

This is the fibre-level (generic `CommRing R`, formal `q` — per
AGENTS.md §7c no archimedean structure) backbone of the per-bond
binding factor `f_bond(q) = c·z + d` derived on the compute side:
`f_pp = z`, `f_nn = z − h`, `f_pn = z − h(½ − δ/4)`, validated against
the measured `tr_atom/tr_free` to 1.1e-15 on D/T/³He/⁴He.  See
`docs/audits/2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`
and the depth-1 `Z_q` heat-kernel framing (the bridge is the depth-1
link kernel on the Wedderburn eigenbasis).

Both lemmas are sorry-free consequences of the `MarkovTrace` class
fields (`trace_gen`, `trace_prod_gen`, `normalised`, linearity).  The
general `A`-bond factorization `tr_M(∏_k (c_k • σ_{i_k} + d_k)) =
∏_k (c_k·z + d_k)` for pairwise-distant generators needs the
cross-level Markov axiom (or a word-induction principle) that the
class does not yet carry — same gap documented at
`markov_trace_unique`; the pair case below is the `A = 3` (two-bond)
instance and the compute witness covers the general case numerically.

**Status of the general case (2026-09-07, bean `qou-gr3t`).** The gap named above is now a
*named hypothesis with a counter-model*: `QOU.Hecke.MarkovInteriorBond.InteriorMarkov` states the
interior-generator Markov property (`tr(a·σ_g·b) = z·tr(a·b)` for `a` below and `b` above the
bond), `tr_bondWord_of_interiorMarkov` proves the general-`A` bond product from it for arbitrary
(non-monotone) block words, `interiorMarkov_ascending` proves it unconditionally in the monotone
case, and `not_interiorMarkov_cmTower` exhibits a `MarkovTower` satisfying every field and
violating it — so the property is independent of the abstract tower axioms.

**PROVED for the Hecke tower (2026-09-13, PR #7265 + #7337).** The clause that stood here —
*"is a theorem of the Hecke tower (quadratic + braid + word-spanning), still to be proved there"* —
named the right target and is now out of date on its own conclusion.
`QOU.Hecke.InteriorMarkovOfBraidedTower.interiorMarkov_of_braided` discharges `InteriorMarkov` on
**every** `BraidedTower` (the three Iwahori–Hecke relations: quadratic, far-commutation, braid),
through `HeckeSandwichReduces.disjointBlock_of_braided`; composing with
`tr_bondWord_of_interiorMarkov` gives the general-`A` bond product unconditionally there, and
`QOU.Hecke.PureBondChainProduct.tr_pureBondChain_of_braided` states it in the bare-product shape
this docstring quotes. Both sorry-free.

**Three limits, or this gets over-quoted.** (i) The coefficient is `1`: the proved shape is
`∏_k (z + d_k)`, not `∏_k (c_k·z + d_k)`, because `c • σ + d` factors only over a field — no
restriction on the corpus, since all three bond types listed above carry `c = 1`. (ii) It is proved
in a **different class**. `MarkovTrace n q A` below is fixed-level and single-algebra with no
filtration, so it cannot state "`a` below the bond, `b` above it" — which is exactly what "the class
does not yet carry" recorded, and remains true of *this* class; the proof lives in the tower
vocabulary and transporting it here is a separate bridge. (iii) A braided tower is not yet the
**production** trace: the Ocneanu trace of `H_n(q)` at `z = q³/(q²+1)` is proved unique as a
`HeckeCoset.MarkovTraceFamily` and is not packaged as an `OcneanuTrace.MarkovTrace` (bean
`qou-gr3t`, remaining item).

The `n = 9` exact identity (`route_c_step3_bond_factorisation_exact_probe.py`, 76/76) remains the
independent scope-(b) evidence at fixed `A`, on the canonical non-monotone word.

## References

- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] braids-and-knots/markov-trace.md; audit
  `2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`
-/

namespace QOU.Hecke

universe u

namespace MarkovTrace

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]

/-- **Per-bond trace factor (one bond).**  The Markov trace of a bridge
crossing `c • σ_i + d • 1` is its conditional expectation
`c · z + d` — the fibre-level form of the per-bond binding factor
`f_bond(q)`:  `f_pp = z` (`(c,d) = (1,0)`), `f_nn = z − h`
(`(1, −h)`), `f_pn = z − h(½ − δ/4)`. -/
theorem trace_bond_crossing (i : Generator n) (c d : R) :
    MT.trace (c • HA.embed i + d • (1 : A)) = c * MT.z_param + d := by
  rw [map_add, map_smul, map_smul, MT.trace_gen, MT.normalised,
    smul_eq_mul, smul_eq_mul, mul_one]

/-- **Two-bond factorization.**  For bridge crossings at generators
`i < j` the Markov trace factorizes over the bonds:
`tr_M((c₁σ_i + d₁)(c₂σ_j + d₂)) = (c₁z + d₁)(c₂z + d₂)`.
This is the `A = 3` (two-bond chain) instance of
`tr_atom = tr_free · ∏ f_bond`; uses `trace_prod_gen`
(`tr_M(σ_iσ_j) = z²`, two Markov peels). -/
theorem trace_bond_pair_factorizes (i j : Generator n)
    (h : i.idx.val < j.idx.val) (c₁ d₁ c₂ d₂ : R) :
    MT.trace ((c₁ • HA.embed i + d₁ • (1 : A)) *
              (c₂ • HA.embed j + d₂ • (1 : A)))
      = (c₁ * MT.z_param + d₁) * (c₂ * MT.z_param + d₂) := by
  have expand : (c₁ • HA.embed i + d₁ • (1 : A)) *
                (c₂ • HA.embed j + d₂ • (1 : A))
      = (c₁ * c₂) • (HA.embed i * HA.embed j)
        + ((c₁ * d₂) • HA.embed i
        + ((d₁ * c₂) • HA.embed j + (d₁ * d₂) • (1 : A))) := by
    simp only [add_mul, mul_add, smul_mul_smul_comm, mul_one, one_mul]
    abel
  rw [expand, map_add, map_add, map_add, map_smul, map_smul, map_smul,
    map_smul, MT.trace_prod_gen i j h, MT.trace_gen, MT.trace_gen,
    MT.normalised, smul_eq_mul, smul_eq_mul, smul_eq_mul, smul_eq_mul,
    mul_one]
  ring

end MarkovTrace

end QOU.Hecke
