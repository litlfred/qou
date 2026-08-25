import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wigner-su4-from-spin-isospin",
  title:
    "Wigner $\\mathrm{SU}(4) = \\mathrm{SU}(2)_S \\times \\mathrm{SU}(2)_I$ as the categorical source for nuclear-shell binding",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin",
    validation: "not_checked",
  },
  uses: [
    "conj:isospin-from-canonical-bowtie",
    "conj:spin-from-so3-fiber",
  ],
  cites: [
    "wigner1937",
    "elliott1958",
    "kashiwara1991",
    "khovanovlauda2009",
  ],
  tags: [
    "wigner-su4",
    "duality-d11",
    "spin-isospin",
    "nuclear-shell",
    "l3-binding",
    "magic-shell",
    "cluster-b-closure",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
