import QOU.Infra.Polylogarithm
import QOU.Infra.Clausen
import QOU.Infra.DirichletL
import QOU.Infra.BorelRank

/-!
# QOU axiomatic infrastructure for analytic number theory

Umbrella for the four infrastructure modules that package
mathematical objects not yet in Mathlib (polylogarithm,
Clausen function, Dirichlet L-values, Borel K-theory rank).

Each module either:
- Defines a *closed-form prediction* as a noncomputable `def`
  (lets downstream `prop:` blocks `ring`/`norm_num` against it
  with zero `sorry`), or
- Declares a *conjecture class* (the substantive content that
  identifies the closed form with the analytic object); concrete
  instances must furnish a proof using a chosen polylog
  implementation.

See AGENTS.md §3b-cond: downstream propositions using these
classes via `[Instance]` hypotheses remain *theorem-level* in
the manifest (conditional-class exception).
-/
