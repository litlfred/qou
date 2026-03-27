import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:brings-surface",
  label: "rem:brings-qou-4tuple",
  title: "QOU 4-tuple for Bring's surface",
  uses: [
    "ex:c-quantum-observable-universe",
    "def:brings-surface",
    "def:substrate-parameter",
    "def:su2-generators",
    "def:so3-generators",
  ],
});
