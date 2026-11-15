import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:p-vs-np-boundary",
  label: "rem:p-vs-np-boundary-interpretation",
  title:
    "Geometric meaning of the boundary dichotomy and the three equivalent criteria",
  uses: [
    "conj:p-vs-np-boundary",
    "def:skein-resolution-obstruction",
    "prop:p-bandwidth-bound",
    "conj:quantum-computational-universality",
  ],
});
