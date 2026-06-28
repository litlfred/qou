import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skein-finiteness-bound",
  label: "rem:skein-finiteness-bound-interpretation",
  title: "The nuclear chart lattice and particle finiteness",
  uses: [
    "prop:skein-finiteness-bound",
    "prop:beta-stability",
    "prop:shell-closure-normal-form",
  ],
});
