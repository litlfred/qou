import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:yekutieli-triple",
  label: "rem:yekutieli-triple-remark",
  title: "Functoriality and archimedean reading of the lifting triple",
  uses: ["def:yekutieli-triple", "prop:jet-prolongation", "lem:descent"],
});
