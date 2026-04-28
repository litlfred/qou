import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-reeb",
  label: "rem:lepton-discrepancies",
  title: "Electron--muon discrepancies",
  uses: [
    "def:substrate-parameter",
    "rem:symmetry-preserving-leptons",
  ],
  tags: ["lepton", "anomaly", "observation"],
});
