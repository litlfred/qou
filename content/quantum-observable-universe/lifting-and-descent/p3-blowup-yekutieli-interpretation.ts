import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:blowup-yekutieli",
  label: "rem:p3-blowup-yekutieli-interpretation",
  title:
    "Regularity as lifting, local-cohomology origin, and topological selection of the blowup obstruction",
  uses: [
    "prop:blowup-yekutieli",
    "thm:q-ns-wellposedness",
    "def:local-cohomology-group",
    "prop:descent-condition",
    "rem:vortex-reconnection",
  ],
});
