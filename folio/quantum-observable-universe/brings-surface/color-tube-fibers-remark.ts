import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-tube-fibers",
  label: "rem:color-tube-fibers-remark",
  title: "Color tubes as color elliptic fibers",
  uses: ["def:color-tube-fibers", "prop:color-elliptic"],
});
