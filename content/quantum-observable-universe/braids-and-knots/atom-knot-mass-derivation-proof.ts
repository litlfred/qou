import { proof } from "../../schema/builders";

export default proof({
  label: "prf:atom-knot-mass-derivation",
  title:
    "Proof of the end-to-end mass derivation $B = \\rho \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$",
  uses: [
    "prop:atom-knot-mass-derivation",
    "def:quantum-observable-universe",
    "def:rigid-monoidal-category",
    "rem:adjoint-trace",
    "def:confined-particle",
    "prop:confinement-sdp",
    "prop:wedderburn-trace-identity",
    "thm:jones-markov-trace",
    "prop:archimedean-realization-functor",
  ],
});
