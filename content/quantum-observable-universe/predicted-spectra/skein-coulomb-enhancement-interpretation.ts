import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skein-coulomb-enhancement",
  label: "rem:skein-coulomb-enhancement-interpretation",
  title: "Magnitude, transition classes, and what the QOU predicts",
  uses: [
    "prop:skein-coulomb-enhancement",
    "prop:hadron-half-life",
    "def:electron-knot",
  ],
});
