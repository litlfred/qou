import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quaternion-so3-motivation",
  title: "From $\\mathrm{SU}(2)$ to quaternions via $\\mathrm{SO}(3)$",
  uses: [
    "def:su2-generators",
    "def:so3-generators",
  ],
});
