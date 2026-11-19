import { example } from "../../schema/builders";

export default example({
  label: "ex:birthday-grading-substrate",
  title:
    "Birthday of the aether parameters $c_q$, $\\hbar_q$, $d_H(q)$ at $q = 1 + \\varepsilon$",
  interprets: "def:birthday-grading",
  tags: [
    "surreal-numbers",
    "birthday",
    "substrate",
    "infinitesimal",
  ],
  uses: [
    "def:birthday-grading",
  ],
});
