import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-frobenius-traces",
  title: "Frobenius traces of Cremona $50\\mathrm{a}1$ and strict Hasse inequality for $7 \\le p \\le 41$",
  lean: {
    ref: "qou:QOU.BringsSurface.BringFrobeniusTraces.bring_hasse_table",
    validation: "leanok",
  },
  uses: [
    "def:local-q-zeta-function",
    "thm:hasse-weil-bound",
  ],
  tags: ["frobenius", "hasse-weil", "elliptic-curve", "brings-surface"],
});
