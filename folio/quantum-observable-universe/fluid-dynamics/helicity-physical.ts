import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:helicity-conservation",
  label: "rem:helicity-physical",
  title: "Helicity as quantised topological charge",
  uses: ["prop:helicity-conservation", "rem:trefoil-vortex-chirality-flip"],
  cites: ["enciso2017", "khesin2003"],
  tags: ["helicity", "topological-charge", "quantisation"],
});
