import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gram-kappa-spectral-interpretation",
  title:
    "Conjectural Plancherel form of $\\kappa$",
  interprets: "conj:gram-determinant-plancherel-ratio",
  uses: ["conj:gram-determinant-plancherel-ratio", "def:cs-gram-determinant-ratio"],
  tags: [
    "interpretation",
    "kappa",
    "plancherel",
    "numerical-evaluation",
    "no-hand-calculation",
  ],
  cites: [
    "jones1987",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/alpha_em_form_ladder_probe.py",
    witness: "computations/alpha-em-form-ladder.witness.json",
    status: "verified",
  },
});
