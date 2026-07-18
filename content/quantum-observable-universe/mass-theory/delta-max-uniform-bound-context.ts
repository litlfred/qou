import { remark } from "../../schema/builders";

export default remark({
  label: "rem:delta-max-uniform-bound-context",
  title: "Framework context for the uniform tail bound",
  interprets: "prop:delta-max-uniform-bound",
  tags: ["jet-tower", "phi-q", "tail-bound", "convergence"],
  uses: ["prop:delta-max-uniform-bound"],
});
