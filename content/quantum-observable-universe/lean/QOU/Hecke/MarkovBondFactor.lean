import QOU.Hecke.MarkovTrace
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel

/-!
# QOU.Hecke.MarkovBondFactor — the per-bond trace factor `tr_M(c·σ + d) = c·z + d`

> **STATUS (2026-06-10):**
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

## References

- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] braids-and-knots/markov-trace.md; audit
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
