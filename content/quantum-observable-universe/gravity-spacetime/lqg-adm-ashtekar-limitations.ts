import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lqg-adm-ashtekar-limitations",
  title: "Limitations of the LQG comparison",
  tags: [
    "loop-quantum-gravity",
    "comparison"
  ],
  uses: [
    "rem:lqg-adm-ashtekar-comparison",
    "conj:os-reflection-positivity-from-reeb",
    "rem:yang-mills-surreal-bound"
  ]
});
