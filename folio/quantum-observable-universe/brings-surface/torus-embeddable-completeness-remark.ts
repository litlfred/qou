import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:torus-embeddable-complete",
  label: "rem:torus-embeddable-completeness-remark",
  title: "Number-theoretic nature of the completeness bound",
  uses: ["prop:torus-embeddable-complete"],
});
