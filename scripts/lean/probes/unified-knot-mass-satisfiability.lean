/-!
# Probe: is `QOU.BraidKnot.UnifiedKnotMass` satisfiable by the physics it names?

**Result: no.** Two of the three mass terms are pinned to zero by the class's
own fields, and `trivial_vortex_vacuum_mass`'s hypotheses are contradictory.

`content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean`
declares three stubs and a class over them:

```lean
def descendedMarkov (q : ℝ) (_braid : Unit) : ℝ := 0 * q
def braneTower      (q : ℝ) (_braid : Unit) : ℝ := 0 * q

class UnifiedKnotMass where
  ...
  unified_identity  : total_mass = descended + tower + frobenius_correction
  descended_is_markov : descended = |descendedMarkov q braid|
  tower_is_phi_q_sum  : tower     = braneTower q braid
```

The stubs are disclosed ("Concrete model: each component returns 0; the genuine
constructions live downstream in dedicated files"), and no instance of the class
is ever constructed -- both good. The defect is narrower and is not a stub
problem: the class **fields point at the stubs**, not at the downstream
constructions they name. `descended_is_markov` does not say "descended is
whatever `prop:categorical-mass-markov` yields"; it says `descended =
|0 * q|`. So the antecedent `U : UnifiedKnotMass` is one that no intended model
can satisfy, and every `(U : UnifiedKnotMass)` theorem in the file is
conditional on it.

`trivial_vortex_vacuum_mass` then adds `h_desc : U.descended = 1` ("the
descended trace evaluates to 1 -- the trace of the identity element of
`H_n(q)`"), which contradicts the class. Its conclusion follows from `False`.

To run (needs Mathlib oleans; see AGENTS.md line 3715 for the cache restore):

    cp content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean /tmp/p.lean
    sed -n '/^-- ==== PROBE/,$p' scripts/lean/probes/unified-knot-mass-satisfiability.lean >> /tmp/p.lean
    LP=""; for d in .lake/packages/*/.lake/build/lib/lean; do LP="$LP$PWD/$d:"; done
    LEAN_PATH="$LP" lean /tmp/p.lean          # exit 0 = every claim below holds

Verified exit 0 on lean-v4.24.0, 2026-08-27. Bean qou-0avp.
-/

-- ==== PROBE BODY (appended to the source file by the recipe above) ====
namespace QOU.BraidKnot

-- The class field pins `descended` to the stub, which is identically 0.
theorem probe_descended_forced_zero (U : UnifiedKnotMass) : U.descended = 0 := by
  rw [U.descended_is_markov, descendedMarkov]; simp

theorem probe_tower_forced_zero (U : UnifiedKnotMass) : U.tower = 0 := by
  rw [U.tower_is_phi_q_sum, braneTower]; simp

-- Therefore the hypotheses of `trivial_vortex_vacuum_mass` are CONTRADICTORY:
-- `h_desc : U.descended = 1` together with the class gives `(0 : ℝ) = 1`.
theorem probe_trivial_vortex_hypotheses_absurd
    (U : UnifiedKnotMass) (h_desc : U.descended = 1) : False := by
  have h0 : U.descended = 0 := probe_descended_forced_zero U
  rw [h0] at h_desc
  exact absurd h_desc (by norm_num)

-- And so the "theorem" holds vacuously: anything follows.
theorem probe_vacuous (U : UnifiedKnotMass) (h_desc : U.descended = 1) :
    U.total_mass = 12345 :=
  absurd h_desc (by rw [probe_descended_forced_zero U]; norm_num)

end QOU.BraidKnot
