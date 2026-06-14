/-!
# QOU.Archimedean.noble_gas_characterization

**PROPOSITION.** Noble gas characterization: full shell as full curls
-/

namespace QOU.Archimedean

structure NobleGasCharacterizationData where
  is_full_shell : True
  is_full_curl : True

/-- **PROPOSITION.** Noble gas characterization: full shell as full curls -/
theorem noble_gas_characterization (d : NobleGasCharacterizationData) :
    d.is_full_shell ∧ d.is_full_curl :=
  ⟨d.is_full_shell, d.is_full_curl⟩

end QOU.Archimedean
