import { remark } from "../../schema/builders";

export default remark({
  label: "rem:b1-current-status",
  title:
    "Canonical B1 current-status synthesis — what is theorem, what is open, after eleven rounds",
  interprets: "conj:gb-depth-period-correspondence",
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:b1-soft-sharpness-theorem",
    "prop:depth-2-identification-bloch-suslin",
    "prop:b1-figure-8-row-theorem",
    "prop:b1-torus-knot-rows-theorem",
    "prop:b1-hyperbolic-rows-theorem",
    "prop:hecke-baer-star-generic",
    "prop:two-filtration-bridge-small-cases",
    "prop:joint-galois-braid-discharged",
    "prop:bring-trilog-imaginary-tate-rational",
    "prop:cl3-zeta5-orbit-sum-identity",
    "rem:jones-faithfulness-crossing-8",
    "conj:qou-infra-discharges-goncharov-zeta5",
    "conj:cl3-zeta5-geometric-realization",
  ],
  cites: [
    "murakami-murakami2001",
    "bloch2000",
    "suslin1991",
    "kashaev1997",
    "thurston1978",
  ],
  tags: [
    "B1-status",
    "synthesis",
    "current-status",
    "theorem-vs-open",
    "graded-mikusinski",
    "exposition",
  ],
});
