import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pauli-factor-wedderburn",
  title:
    "Pauli factor $F_{\\mathrm{Pauli}}$ is the alt/sym Wedderburn-block trace ratio",
  lean: {
    ref: "qou:QOU.BraidKnot.pauli_factor_wedderburn",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-categorical",
    "rem:gram-matrix-spectral-connection",
  ],
  tags: [
    "pauli-factor",
    "wedderburn",
    "alternating-block",
    "symmetric-block",
    "trace-ratio",
    "fermion-statistics",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/pauli_factor_wedderburn_probe.py",
    witness: "computations/probes/pauli-factor-wedderburn-probe.witness.json",
    status: "verified",
  },
});
