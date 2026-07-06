import { definition } from "../../schema/builders";

export default definition({
  label: "def:spin-involution",
  title: "Spin involution on a Frobenius $*$-algebra",
  lean: {
    ref: "qou:QOU.BraidKnot.SpinInvolution",
    validation: "not_checked",
  },
  uses: [],
  cites: ["kassel1995"],
  tags: [
    "spin-involution",
    "frobenius-algebra",
    "isospin",
    "spin-grading",
    "hopf-antipode",
  ],
});
