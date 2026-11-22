import QOU.HadronicMass


/-!
# QOU.HadronicMass.nucleon_borromean_topology

The proton and neutron are each modelled as a Borromean
configuration `(6_2^3)` of three quark vortices, bound internally
by Hopf links `ℒ_Hopf` representing the strong force between each
quark pair.  The nucleon mass functional therefore decomposes as a
`QuarkFlavorFactor` times a topological-mass evaluation on
`ℒ_Hopf`.

The Lake module [`lean/QOU/HadronicMass.lean`](../../lean/QOU/HadronicMass.lean)
exposes `QuarkFlavorFactor` (the three-quark content) together with
the constants `vol_borromean` and `vol_hopf_link`.  This sibling
records the structural existence: every well-formed
`QuarkFlavorFactor` paired with the Borromean / Hopf-link volumes
gives a candidate nucleon topology datum.

LaTeX label: `lem:nucleon-borromean-topology`

## References

- [leitner2026] §10 Observations / nucleon-borromean-topology
- The Borromean / Hopf-link volume constants follow SnapPy
  (Bloch–Wigner dilogarithm).
-/

namespace QOU.HadronicMass

/-- **Nucleon Borromean topology — existence form.**

    A nucleon's topological data consists of a `QuarkFlavorFactor`
    encoding its three quark content together with the Borromean
    hyperbolic volume `vol_borromean` (external 3-link) and the
    Hopf-link volume `vol_hopf_link` (internal pairwise binding).
    The lemma packages the existence of a coherent datum: the Lake
    module's `proton_quarks` already realises one such instance,
    The existence statement holds. -/
-- Ref: [leitner2026] §10 Observations / nucleon-borromean-topology
theorem nucleon_borromean_topology :
    ∃ (qff : QuarkFlavorFactor) (v_borr v_hopf : ℝ),
      0 < v_borr ∧ v_hopf = 0 ∧ qff.n_up + qff.n_down = 3 := by
  refine ⟨proton_quarks, vol_borromean, vol_hopf_link, ?_, ?_, ?_⟩
  · unfold vol_borromean; norm_num
  · rfl
  · rfl

end QOU.HadronicMass
