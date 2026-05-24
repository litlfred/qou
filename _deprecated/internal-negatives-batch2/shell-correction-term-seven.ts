import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shell-correction-term-seven",
  title: "Shell-correction seventh term from GB-filtration level 5",
  lean: {
    ref: "qou:QOU.WedderburnMass.ShellCorrectionTermSeven",
    validation: "not_checked",
  },
  uses: [
    "prop:e-infinity-page-identifications",
    "prop:content-scaling-correspondence",
  ],
  tags: [
    "shell-correction",
    "gb-filtration",
    "nuclear-binding",
    "term-7",
    "magic-numbers",
    "shadow-price",
    "bw-polynomial",
  ],
  cites: ["mayer1949", "mayer1955"],
});
