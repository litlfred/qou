import Mathlib.Tactic
import QOU.Observations.AlgebraicCausalActionStructure

/-!
# QOU.Observations.MuArchContinuumLimit

Conjectural Archimedean lift `μ_arch` carrying the pre-Archimedean
algebraic causal-action structure of
`QOU.Observations.AlgebraicCausalActionStructure` to a Finster
causal fermion system ([finster2021], [finster2024]).

The conjecture is encoded as a typeclass with four fields, one per
clause of the narrative statement:

1. Operator-algebra limit (`A_q ↪ F ⊂ L(H)`),
2. Measure convergence (`w̃_λ → ρ` weakly),
3. Trace ↔ causal action (`tr_M(x·y) → ∫∫ L dρ dρ`),
4. Active set ↔ `supp(ρ)`.

Instances of the class are the conjectural input; the only `sorry`
in the entire downstream chain lives in the (currently unmade)
instance. Downstream lemmas that depend on `μ_arch` are stated with
`[MuArchContinuumLimit ...]` as an explicit class hypothesis,
following the conditional-class pattern (CLAUDE.md §3b-cond).

## References

- [finster2021] F. Finster, N. Kamran, M. Oppio, *The linear
  dynamics of wave functions in causal fermion systems*, J. Diff.
  Eq. 293 (2021) 115-187. https://doi.org/10.1016/j.jde.2021.05.025
- [finster2024] F. Finster, J. Kleiner, C. F. Paganini, *Causal
  fermion systems as an effective collapse theory*, J. Phys. A 57
  (2024) 395303. https://doi.org/10.1088/1751-8121/ad7655
- [kerov1981] S. V. Kerov, A. M. Vershik, *Asymptotic theory of
  the characters of a symmetric group*, Funct. Anal. Appl. 15
  (1981) 246-255.
- [biane1998] P. Biane, *Representations of symmetric groups and
  free probability*, Adv. Math. 138 (1998) 126-181.
- [feray2010] V. Féray, P.-L. Méliot, *Asymptotics of q-Plancherel
  measures*, Prob. Theory Related Fields 152 (2012) 589-624.
-/

namespace QOU.Observations.MuArchContinuumLimit

universe u v

/-- **Conjecture (μ_arch continuum limit).**

Encodes the four clauses of
`conj:mu-arch-continuum-limit` (observations chapter):

1. `operatorAlgebraLimit` — `A_q` embeds into a limiting operator
   algebra `F` on a Hilbert space `H` under joint Faddeev scaling.
2. `measureConvergence` — `w̃_λ` pushes forward to a Borel measure
   `ρ` on `F`; the convergence is weak.
3. `traceCausalAction` — for fixed-degree `x, y`, the Markov-trace
   identity converges to the Finster causal-action integral.
4. `activeSetIsSupport` — LP active sets converge to `supp(ρ)`.

The class is purely propositional; concrete witnesses require
analytic input (Kerov-Vershik / Féray-Méliot, free probability,
LP stability under scaling) that is not yet available in Mathlib. -/
class MuArchContinuumLimit : Prop where
  /-- Clause 1: operator-algebra embedding under joint Faddeev
      scaling. -/
  operatorAlgebraLimit : Prop
  /-- Clause 2: weak convergence of the q-Plancherel measure to a
      Finster universal measure on the limit operator algebra. -/
  measureConvergence : Prop
  /-- Clause 3: convergence of the Markov-trace identity to the
      Finster causal-action integral. -/
  traceCausalAction : Prop
  /-- Clause 4: LP active sets push forward to the support of the
      limit measure. -/
  activeSetIsSupport : Prop

end QOU.Observations.MuArchContinuumLimit
