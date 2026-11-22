/-!
# Shell threading energy from Skein smoothing (conjectural)

Class-axiomatised stub for `conj:shell-threading-energy`: the
shell energy scale `λ_shell` equals the crossing energy of the
Skein smoothing `L_0` at the beta-decay vertex — the threading
link that interpolates between the parent `N(Z, N)` and daughter
`N(p+1, n-1)` nuclear configurations.

-- Ref: [leitner2026]
Per `AGENTS.md §3b-cond`, opaque Prop + class field + sorry
instance.

The numerical claim (Skein-smoothing identification reproduces
the observed shell-correction energies within experimental
precision) belongs to a future Archimedean evaluation tier and
is intentionally NOT in this pre-Archimedean class — per gemini
review on #721, algebraic identities must be separated from
their numerical counterparts.

## References

- `[leitner2026]` `conj:shell-threading-energy`
- `[leitner2026]` `conj:skein-shell-correction`
- `[leitner2026]` `def:molecular-hopf-ring`
- `[leitner2026]` `ex:half-life-shell-worked`
-/

namespace QOU.ShellThreadingEnergy

/-- **Sub-claim (Skein-smoothing identification)**: the (specific)
    shell energy scale `λ_shell` equals the crossing energy of
    `L_0`, the Skein smoothing at the beta-decay vertex. The
    Prop is parameterless because the claim is about the
    canonical scale, not a universally-quantified family. -/
opaque ShellEnergyEqualsSmoothingEnergyHolds : Prop

/-- **Shell-threading-energy conjecture** (class-axiomatised per §3b-cond). -/
class ShellThreadingEnergy : Prop where
  smoothing_identification : ShellEnergyEqualsSmoothingEnergyHolds

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance shell_threading_energy_conjecture : ShellThreadingEnergy where
--     axiom shell_threading_energy_smoothing_identification : ShellEnergyEqualsSmoothingEnergyHolds
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[ShellThreadingEnergy]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[ShellThreadingEnergy]` as an explicit hypothesis.

end QOU.ShellThreadingEnergy
