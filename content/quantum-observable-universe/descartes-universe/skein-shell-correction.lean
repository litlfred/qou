/-!
# Shell corrections from Skein polynomial factorization (conjectural)

Class-axiomatised stub for `conj:skein-shell-correction`: shell
corrections to the nuclear binding energy arise from the
Skein-polynomial factorization of the multi-nucleon link into
closed sub-links (one per closed shell).

Per `CLAUDE.md §3b-cond`, opaque Prop + class field + sorry
instance. Algebraic tier only — the numerical match to observed
shell-correction energies belongs to a future Archimedean tier
(per gemini review on #721).

## References

- `[manuscript]` `conj:skein-shell-correction`
- `[manuscript]` `conj:elliptic-stability-locus`
-/

namespace QOU.SkeinShellCorrection

/-- **Algebraic claim**: the Skein polynomial of the multi-nucleon
    link factorises into a product of closed-sub-link factors,
    one per closed shell; each factor contributes a structurally-
    identified shell-correction term. -/
opaque SkeinFactorisationStructuralHolds : Prop

/-- **Skein-shell-correction conjecture** (class-axiomatised per §3b-cond). -/
class SkeinShellCorrection : Prop where
  skein_factorisation_structural : SkeinFactorisationStructuralHolds

-- Ref: [manuscript] conj:skein-shell-correction
instance skein_shell_correction_conjecture : SkeinShellCorrection where
  skein_factorisation_structural := sorry

end QOU.SkeinShellCorrection
