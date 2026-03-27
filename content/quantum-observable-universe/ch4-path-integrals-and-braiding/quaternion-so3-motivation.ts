import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:su2-generators",
  label: "rem:quaternion-so3-motivation",
  title: "From $\\mathrm{SU}(2)$ to quaternions via $\\mathrm{SO}(3)$",
  uses: [
    "rem:brings-qou-4tuple",
    "def:su2-generators",
    "def:so3-generators",
  ],
});
