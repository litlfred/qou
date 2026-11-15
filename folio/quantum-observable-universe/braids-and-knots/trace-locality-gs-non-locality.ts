import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:trace-locality-meets-gs-non-locality",
  label: "rem:trace-locality-gs-non-locality",
  title: "Gröbner–Shirshov reduction is non-local",
  tags: ["locality", "grobner-shirshov", "interpretation"],
  uses: ["prop:trace-locality-meets-gs-non-locality"],
});
