import { remark } from "../../schema/builders";

export default remark({
  label: "rem:so3-generators-rotations",
  title: "The $\\mathrm{SO}(3)$ generators as rotations",
  interprets: "def:so3-generators",
  tags: ["so3", "rotation-group"],
  uses: [
    "def:so3-generators",
  ],
});
