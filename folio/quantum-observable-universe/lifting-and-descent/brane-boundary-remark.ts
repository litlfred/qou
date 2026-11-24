import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:brane-boundary",
  label: "rem:brane-boundary-remark",
  title: "Archimedean locus of the brane boundary",
  uses: ["def:brane-boundary", "lem:descent"],
});
