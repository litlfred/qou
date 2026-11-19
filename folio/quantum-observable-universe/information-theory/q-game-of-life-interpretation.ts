import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-game-of-life",
  label: "rem:q-game-of-life-interpretation",
  title: "Deterministic cellular-automaton models of Peña et al. and 't Hooft",
  uses: ["prop:q-game-of-life"],
  cites: ["pena2022", "thooft2016"],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/toffoli_qand_convention_d_derivation.py",
    witness: ["computations/probes/toffoli-qand-convention-d-derivation.witness.json"],
    status: "verified",
  },
});
