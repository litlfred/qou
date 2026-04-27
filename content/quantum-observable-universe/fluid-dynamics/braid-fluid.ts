import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:braid-fluid",
  title: "Braid--fluid correspondence: from categorical braiding to vortex dynamics",
  uses: [
    "rem:madelung-fluid",
    "sec:webster-inner-product",
  ],
  tags: ["braid-group", "fluid-dynamics", "arnold", "vortex", "correspondence"],
});
