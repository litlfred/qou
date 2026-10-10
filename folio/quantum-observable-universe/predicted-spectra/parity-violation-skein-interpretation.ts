import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:parity-violation-skein",
  label: "rem:parity-violation-skein-interpretation",
  title: "Physical interpretation: maximal parity violation and CP",
  uses: ["prop:parity-violation-skein", "def:beta-decay-skein"],
});
