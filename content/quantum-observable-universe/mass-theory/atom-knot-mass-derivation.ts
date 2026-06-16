import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-mass-derivation",
  title:
    "End-to-end derivation of atomic binding energies $B = \\nu_{\\mathrm{SDP}} \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$ from the categorical action",
  lean: {
    ref: "qou:QOU.BraidKnot.atom_knot_mass_derivation",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:recursive-atom-knot-atlas",
  ],
  tags: [
    "mass-derivation",
    "two-leg",
    "geometric-leg",
    "algebraic-leg",
    "stokes",
    "frobenius-pairing",
    "reeb-density",
    "wedderburn",
    "hecke-trace",
    "gb-filtration",
    "jet-order",
    "volume-conjecture",
    "principled-pipeline",
    "algorithm",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/d_from_scratch.py",
    witness: [
      "computations/d-from-scratch.witness.json",
      "computations/unified-low-isotope-predictor.witness.json",
    ],
    status: "not_run",
  },
});
