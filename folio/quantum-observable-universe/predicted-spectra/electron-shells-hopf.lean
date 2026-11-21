/-!
# Electron shells as closed sub-Hopf links (conjectural)

Class-axiomatized stub for `conj:electron-shells-hopf`: the
electron-cloud structure of a neutral atom — shell capacities
2, 8, 18, 32, … = 2n² — arises from the closed sub-Hopf-link
factorization of the multi-electron chain (each electron the word
σ₀σ₁σ₀ ∈ B₃, closure: the Hopf link). A maximal
closed sub-Hopf link at linking level `n` admits exactly `2n²`
electrons; the noble gases are the atoms whose electron cloud
is a union of such closed sub-links.

-- Ref: [leitner2026]
Per `AGENTS.md §3b-cond`, opaque Props + class fields + sorry
instance per claim. Algebraic tier only — the numerical
photon-energy and selection-rule matches belong to a future
Archimedean tier (per gemini review on #721).

## References

- `[leitner2026]` `conj:electron-shells-hopf`
- `[leitner2026]` `prop:torus-hopf-stability`
-/

namespace QOU.ElectronShellsHopf

/-- **Shell-capacity claim**: the maximal closed sub-Hopf link
    at linking level `n` consists of exactly `2n²` electrons. -/
opaque ShellCapacity2nSquaredHolds : Prop

/-- **Noble-gas closure claim**: atoms whose electron cloud is a
    union of closed sub-Hopf links are exactly the noble gases
    (He, Ne, Ar, Kr, Xe, Rn, Og). -/
opaque NobleGasClosureHolds : Prop

/-- **Electron-shells-Hopf conjecture** (class-axiomatized per §3b-cond). -/
class ElectronShellsHopf : Prop where
  shell_capacity : ShellCapacity2nSquaredHolds
  noble_gas_closure : NobleGasClosureHolds

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance electron_shells_hopf_conjecture : ElectronShellsHopf where
--     axiom electron_shells_hopf_shell_capacity : ShellCapacity2nSquaredHolds
--     axiom electron_shells_hopf_noble_gas_closure : NobleGasClosureHolds
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[ElectronShellsHopf]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[ElectronShellsHopf]` as an explicit hypothesis.

end QOU.ElectronShellsHopf
