import { prose } from "../../schema/builders";

export default prose({
  label: "prose:definition-index",
  // No label here: the enclosing section already uses `sec:definition-index`.
  meta: { position: "opening", indexType: "definitions" },
});
