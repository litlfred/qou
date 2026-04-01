import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-instanton",
  label: "rem:instanton-on-shell",
  title: "On-shell simplification: instanton backgrounds",
  tags: ["instanton", "on-shell", "topological", "bogomolny"],
  uses: [
    "def:categorical-lagrangian",
    "prop:categorical-self-duality",
  ],
});
