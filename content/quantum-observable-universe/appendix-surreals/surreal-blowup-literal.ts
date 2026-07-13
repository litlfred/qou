import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-blowup-literal",
  title: "Every step of the surreal blow-up is a literal surreal object",
  interprets: "def:surreal-blowup-calculus",
  tags: [
    "surreal-numbers",
    "renormalisation",
    "blow-up",
    "standard-part",
  ],
  uses: [
    "def:surreal-blowup-calculus",
  ],
});
