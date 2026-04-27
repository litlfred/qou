import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-mass-derivation",
  title:
    "End-to-end derivation of atomic binding energies $B = \\rho \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$ from the categorical action",
  lean: {
    ref: "qou:QOU.BraidKnot.atom_knot_mass_derivation",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:rigid-monoidal-category",
    "def:adjoint-trace",
    "def:confined-particle",
    "prop:confinement-sdp",
    "prop:wedderburn-trace-identity",
    "thm:jones-markov-trace",
    "prop:alpha-k-derivation-procedure",
    "prop:recursive-atom-knot-atlas",
    "prop:archimedean-realization-functor",
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
});
