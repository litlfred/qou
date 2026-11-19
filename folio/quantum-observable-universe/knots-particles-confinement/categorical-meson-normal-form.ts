import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-meson-normal-form",
  title: "Normal form and particle content of the meson",
  interprets: "def:categorical-meson",
  tags: ["meson", "normal-form"],
  uses: [
    "def:categorical-meson",
    "def:hadron",
  ],
});
