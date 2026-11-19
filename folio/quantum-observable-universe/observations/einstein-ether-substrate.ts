import { remark } from "../../schema/builders";

export default remark({
  label: "rem:einstein-ether-substrate",
  title: "Einstein's ether and the categorical substrate",
  // The remark is a historical interpretation of the substrate's *cohomological*
  // fixing — "q_0 is fixed ... by the cohomological structure of H^1(Bring) = 2W"
  // is the claim that carries the Einstein analogy, and that claim is
  // prop:calibration-cohomology-alignment. Demoting to `prose` was the other
  // option, but the remark does lean on a provable statement, so `interprets`
  // is the honest disposition (AGENTS.md §3a).
  interprets: "prop:calibration-cohomology-alignment",
  uses: ["def:categorical-action", "prop:calibration-cohomology-alignment"],
  cites: ["einstein1920"],
  tags: ["substrate", "einstein", "ether", "categorical", "foundations"],
});
