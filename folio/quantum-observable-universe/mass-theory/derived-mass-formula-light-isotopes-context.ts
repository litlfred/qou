import { remark } from "../../schema/builders";

export default remark({
  label: "rem:derived-mass-formula-light-isotopes-context",
  title:
    "Scorecard, p-n splitting, and binding under-prediction for the derived mass formula",
  interprets: "prop:derived-mass-formula-light-isotopes",
  tags: ["mass-formula", "light-isotopes", "binding", "codata"],
  uses: ["prop:derived-mass-formula-light-isotopes"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness (legacy CODATA-2018 muon pin): derived-only-formula.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_borromean_verification_50dps.py",
    witness: "computations/m-p-borromean-verification-50dps.witness.json",
    status: "verified",
  },
});
