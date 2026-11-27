import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ks-finiteness-via-diamond-lemma",
  title:
    "Algebraic shortcut: Kontsevich--Soibelman's ind-constructibility from the Diamond Lemma",
  interprets: "conj:curvature-rank-gb-stratification",
  uses: [
    "conj:curvature-rank-gb-stratification",
    "unital-groebner-bases:cor:pbw",
  ],
  cites: ["kontsevich-soibelman-2008", "bergman1978", "bokut2005"],
});
