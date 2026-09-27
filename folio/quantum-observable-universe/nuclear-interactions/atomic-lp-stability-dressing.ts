import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:atomic-lp-stability",
  label: "rem:atomic-lp-stability-dressing",
  title: "Borromean dressing and composite-nucleus stabilisation",
  tags: ["lp-stability", "borromean", "atomic-braid", "confinement"],
  uses: ["prop:atomic-lp-stability", "def:atomic-braid"],
});
