import { remark } from "../../schema/builders";

export default remark({
  label: "rem:regime-table",
  title: "Master regime table for the substrate parameter $q$",
  tags: [
    "regime",
    "limits",
    "summary",
    "reference",
  ],
  interprets: "def:substrate-parameter",
  uses: [
    "def:quantum-planck-constant",
    "def:information-speed-of-light",
      ],
});
