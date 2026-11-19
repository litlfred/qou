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
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement previously said $F_{\\mathrm{Pauli}}$ vanishes for bosonic braids and is a unit for fully fermionic ones. Both blocks are one-dimensional, so the character ratio is $(-1)^w q^{-2w}$ ($w$ = writhe): always a unit, never zero (this matches `computations/probes/pauli_factor_wedderburn_probe.py`). The vanishing Pauli factor used in `computations/spectral_decomposition_qvalue_d.py` is a different object, $|\\mathrm{tr}_M(e_{(1^3)} T_\\beta e_{(1^3)})| / |\\mathrm{tr}_M(T_\\beta)|$, which is identically zero under convention D because $y_{(1^3)} = 0$, for every braid. Neither object has the bosonic/fermionic behaviour that was claimed.",
    },
  ],
});
