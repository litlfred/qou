/-!
# Shell corrections from Skein polynomial factorization (conjectural)

Class-axiomatized stub for `conj:skein-shell-correction`: shell
corrections to the nuclear binding energy arise from the
Skein-polynomial factorization of the multi-nucleon link into
closed sub-links (one per closed shell).

-- Ref: [leitner2026]
Per `AGENTS.md §3b-cond`, opaque Prop + class field + sorry
instance. Algebraic tier only — the numerical match to observed
shell-correction energies belongs to a future Archimedean tier
(per gemini review on #721).

## References

- `[leitner2026]` `conj:skein-shell-correction`
- `[leitner2026]` `rem:elliptic-stability-locus`
-/

namespace QOU.SkeinShellCorrection

/-- **Algebraic claim**: the Skein polynomial of the multi-nucleon
    link factorizes into a product of closed-sub-link factors,
    one per closed shell; each factor contributes a structurally-
    identified shell-correction term. -/
opaque SkeinFactorizationStructuralHolds : Prop

/-- **Skein-shell-correction conjecture** (class-axiomatized per §3b-cond). -/
class SkeinShellCorrection : Prop where
  skein_factorization_structural : SkeinFactorizationStructuralHolds

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance skein_shell_correction_conjecture : SkeinShellCorrection where
--     axiom skein_shell_correction_skein_factorization_structural : SkeinFactorizationStructuralHolds
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[SkeinShellCorrection]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[SkeinShellCorrection]` as an explicit hypothesis.

end QOU.SkeinShellCorrection
