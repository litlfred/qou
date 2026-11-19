import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hochschild-homology-remark",
  title: "Traces, Kähler differentials and the two conventions for Hochschild homology",
  interprets: "def:hochschild-homology",
  uses: ["def:hochschild-homology"],
  foreshadows: ["def:chern-character"],
  tags: ["hochschild-homology", "homological-algebra", "trace", "cocenter"],
  cites: ["loday-1998", "weibel1994"],
});
