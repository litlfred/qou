import { remark } from "../../schema/builders";

export default remark({
  label: "rem:perpetual-obstruction-depth-omega",
  title: "The perpetual obstruction as a single surreal grade",
  interprets: "conj:motivic-perpetual-obstruction",
  uses: [
    "conj:motivic-perpetual-obstruction",
    "def:surreal-blowup-calculus",
    "rem:conway-normal-form",
    "prop:cs-evaluation-faithfulness",
  ],
});
