import { remark } from "../../schema/builders";

export default remark({
  label: "rem:instanton-on-shell",
  title: "On-shell simplification: instanton backgrounds",
  tags: ["instanton", "on-shell", "topological", "bogomolny"],
  uses: [
    "def:categorical-instanton",
    "def:categorical-lagrangian",
    "prop:categorical-self-duality",
  ],
});
