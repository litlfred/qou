import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:descartes-knot-eigenbasis",
  lean: { ref: "qou:QOU.Archimedean.descartes_knot_eigenbasis",
    validation: "not_checked",
  },
  title: "Knot eigenbasis completeness for a Descartes universe",
  tags: ["archimedean-universe", "knot-invariant", "hecke-algebra", "schur-weyl"],
  uses: [
    "cor:descartes-braid-structure",
    "thm:jones-markov-trace",
    "prop:knot-eigenbasis-complete",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/archimedean_knot_eigenbasis_probe.py",
    witness: "computations/probes/archimedean-knot-eigenbasis-probe.witness.json",
    status: "verified",
  },
});
