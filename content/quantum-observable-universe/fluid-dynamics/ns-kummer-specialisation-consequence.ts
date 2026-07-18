import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-kummer-specialisation-consequence",
  title: "Consequence for NS regularity",
  interprets: "prop:ns-kummer-specialisation",
  uses: ["thm:qu-to-qou"],
  tags: ["kummer", "obstruction", "navier-stokes", "blowup"],
});
