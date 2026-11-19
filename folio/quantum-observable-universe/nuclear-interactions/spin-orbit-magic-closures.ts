import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spin-orbit-magic-closures",
  title:
    "Higher-$\\ell$ spin–orbit Pauli multiplicities, Mayer–Jensen magic closures, and quadratic Fermi symmetry energy",
  lean: {
    ref: "qou:QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy.mayerJensenMagic_values",
    validation: "validated",
  },
  tags: [
    "nuclear-binding",
    "magic-numbers",
    "shell-closure",
    "spin-orbit",
    "mayer-jensen",
    "symmetry-energy",
    "pauli-exclusion",
  ],
  uses: [
    "prop:demand-stability",
    "prop:nuclear-operator-regimes",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalized in `folio/quantum-observable-universe/lean/QOU/Nuclear/SpinOrbitShellClosureAndSymmetryEnergy.lean` (`sWave_recover_four_state_pauli_fiber`, `degPlus_add_degMinus`, `totalOrbitalSpinIsospinCap_eq`, `sum_oscShellDeg_mul_three`, `cumOscClosure_eq_sum`, `cumOscClosure_values`, `carbon12_and_oxygen16_shell_closures`, `mayerJensenMagic_mul_three_closed_form`, `mayerJensenMagic_values`, `mayerJensen_step_decomposition`, `unifiedNuclearMagicSeq_eq_and_doubly_magic_masses`, `pauliAsymmetryPenalty_eq_promotion_sum`, `quadratic_pauli_symmetry_energy_exact`, `quadratic_pauli_symmetry_in_N_sub_Z`, `fermi_asymmetry_promotion_nonneg`, `quadratic_pauli_symmetry_pos`) with 80-dps zero-float64 witness `computations/probes/nuclear-spin-orbit-shells-and-symmetry.witness.json`.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_spin_orbit_shells_and_symmetry_probe.py",
    witness: "computations/probes/nuclear-spin-orbit-shells-and-symmetry.witness.json",
    status: "verified",
  },
});
