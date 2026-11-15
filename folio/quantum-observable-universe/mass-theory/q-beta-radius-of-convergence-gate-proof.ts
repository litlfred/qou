import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-radius-of-convergence-gate-evidence",
  title:
    "Evidence for the $\\mathfrak{Q}_\\beta$ radius-of-convergence conjecture from the $c_2, \\ldots, c_{10}$ window",
  interprets: "conj:q-beta-radius-of-convergence-gate",
  uses: [
    "conj:q-beta-radius-of-convergence-gate",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
});
