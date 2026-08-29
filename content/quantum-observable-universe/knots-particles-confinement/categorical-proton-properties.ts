import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-proton-properties",
  interprets: "def:categorical-proton",
  title: "Proton: NF construction, mass, charge, and computational backing",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: ["def:categorical-proton", "conj:borromean-quark"],
  cites: ["manuscript"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-29",
      body:
        "**Names a different proton stabiliser than " +
        "`rem:stable-atom-properties` does.** This block says *\"a single " +
        "Hopf link $L_- = \\sigma_1\\sigma_0$ is the minimum additional " +
        "structure capable of restoring stability\"*; " +
        "`stable-atom-properties` says the ILP *\"finds the unique integer " +
        "solution $\\sigma_0 \\to \\sigma_0$ (2 gluon crossings)\"*. Both " +
        "are two gluon crossings, so the **count** agrees while the " +
        "**operator** does not. Recorded, not adjudicated: neither block " +
        "cites a computation for its choice. Bean `qou-vtlj`; adjudication " +
        "belongs to `qou-bg3w`.",
    },
  ],
});
