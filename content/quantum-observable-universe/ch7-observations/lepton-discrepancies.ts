import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-reeb",
  label: "rem:lepton-discrepancies",
  title: "Electron--muon discrepancies",
  uses: ["def:substrate-parameter", "def:categorical-reeb"],
  tags: ["lepton", "anomaly", "observation"],
});
