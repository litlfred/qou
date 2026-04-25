import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shell-correction-term-seven",
  title: "Shell-correction seventh term from GB-filtration level 5",
  uses: [
    "thm:knot-mass-formula-unified",
    "prop:e-infinity-page-identifications",
    "def:confinement-level",
    "prop:three-parameters-wedderburn",
    "prop:gb-residue-spectral-sum",
    "prop:bw-coefficient-shadow-price",
    "prop:wigner-2-coefficient",
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
