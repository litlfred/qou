import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:nuclear-shell-intruder",
  label: "rem:nuclear-shell-intruder-interpretation",
  title: "Why the intruder threshold is $N = 3$",
  tags: [
    "nuclear-shell",
    "borromean",
    "intruder",
    "crossing-number",
    "spin-orbit",
  ],
  uses: ["prop:nuclear-shell-intruder", "def:borromean-baryon"],
});
