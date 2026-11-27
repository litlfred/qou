import { proposition } from "../../schema/builders";

/**
 * The A = 2 γγ bond on the four-strand tail, as exact identities in the
 * Markov parameter z and h = q − q⁻¹. Lean: this block's `.lean` sibling,
 * namespace `QOU.LightNucleiBond`.
 */
export default proposition({
  label: "prop:light-nuclei-a2-bond-tail",
  title: "The $A = 2$ $\\gamma\\gamma$ bond on the four-strand tail, for every Markov parameter",
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "Proved in Lean, sorry-free, over any field with 2 ≠ 0: `proton_free`, `neutron_free`, `bond_into_proton`, `bond_into_neutron`, `bond_into_proton_vanishes`, `bond_into_neutron_vanishes`, plus the evaluator lemmas `ME_eq_P` and `tail_eq_trWord`, and the reduction from the full A = 2 word to the four-strand tail (`a2_reduce`, giving `a2_bond_into_proton` and `a2_bond_into_neutron` on the Hecke tower for any first nucleon in H₃). Also proved, over any commutative ring at every z and h: `towerTr_shift_commutator`, tr(Y↑(σ₀σ₁ − σ₁σ₀)) = 0 for every Y on strands ≥ 1 (the h² step). Not formalised: the identification of the h² part of V³ − 1 with that commutator (probe `bond_structure_probe.py` (a)), and the leading-order coefficients (1 − z²)/2 and (1 − z²)/z, which are read off the identities by hand. The same identities were first measured with `computations/probes/light_nuclei_a2_a3/bond_generic_z_probe.py`. Issue #9039.",
    },
  ],
  uses: ["prop:markov-trace-recursive-reducer", "prop:markov-trace-hecke-functional"],
  cites: ["jones1987"],
  computation: {
    engine: "sympy",
    script: "computations/probes/light_nuclei_a2_a3/bond_generic_z_probe.py",
    witness: ["computations/probes/light_nuclei_a2_a3/bond-generic-z.witness.json"],
    status: "verified",
    requires: ["sympy", "python-flint"],
  },
  lean: {
    ref: "qou:QOU.LightNucleiBond.bond_into_proton",
    validation: "not_checked",
  },
  tags: ["markov-trace", "light-nuclei", "gamma-gamma-bond", "binding"],
});
