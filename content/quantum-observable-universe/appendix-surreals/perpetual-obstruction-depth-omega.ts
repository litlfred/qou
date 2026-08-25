import { remark } from "../../schema/builders";

export default remark({
  label: "rem:perpetual-obstruction-depth-omega",
  title: "The perpetual obstruction as a single surreal grade",
  interprets: "thm:motivic-perpetual-obstruction",
  uses: [
    "thm:motivic-perpetual-obstruction",
    "def:surreal-blowup-calculus",
    "rem:conway-normal-form",
    "prop:cs-evaluation-faithfulness",
  ],
});
