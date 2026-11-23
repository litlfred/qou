import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-chamber-groebner-basis",
  title:
    "Physical cluster chamber, drip-line monomer reduction, and the Hoyle triple-alpha bottleneck",
  lean: {
    ref: "qou:QOU.MathlibInfra.gPhys_strict_cost_decrease_of_chamber",
    validation: "validated",
  },
  proofs: ["prf:nuclear-chamber-groebner-basis"],
  uses: [
    "prop:nuclear-groebner-reduction",
    "prop:confinement-lp",
    "def:lp-confined",
  ],
  cites: [
    "graver1975",
    "conti-traverso1991",
    "sturmfels-thomas1997",
  ],
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/lp_bootstrap_dual_gaps/chamber_gs_model_a_b_probe.py",
    witness:
      "computations/probes/lp_bootstrap_dual_gaps/chamber-gs-model-a-b.witness.json",
    status: "verified",
  },
  tags: [
    "nuclear-binding",
    "toric-ideal",
    "groebner-fan",
    "graver-basis",
    "drip-line",
    "hoyle-state",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Formalized in `folio/quantum-observable-universe/lean/QOU/MathlibInfra/NuclearChamberGS.lean` (`gPhys_in_kernel_A0`, `gPhys_strict_cost_decrease_of_chamber`, `he5_normal_form_eq_alpha_neutron`, `light_nuclide_normal_forms`, `hoyle_triple_alpha_bottleneck`, `mayerJensen_cumulative_magic`, `capacitated_shell_occupancy_or_hole_pos`) and `SymmetryReducedDualCertificate.lean` (`graver_test_set_certifies_global_ip_min`). Exhaustive 80-dps enumeration of the 28 unsigned Graver elements, 17 circuits, 27 universal Gröbner basis binomials, and 73 Gröbner fan chambers of `A_0`, together with the QOU `q_0` (bare and tower) vs AME2020 chamber coincidence check, is recorded in `computations/probes/lp_bootstrap_dual_gaps/chamber-gs-model-a-b.witness.json`.",
    },
  ],
});
