import { conjecture } from "../../schema/builders";

/**
 * §3b-cond conjecture class for the proton's Borromean mass assembly.
 *
 * The class axiomatisation lives in the `qou` Lake library at
 * content/quantum-observable-universe/lean/QOU/AppendixQValues/ProtonBorromeanAssembly.lean
 * (class `ProtonBorromeanAssembly`); no sibling `.lean` here, so it does not
 * shadow the library class. The downstream `prop:proton-mass-substrate-identity`
 * takes this class as an explicit `[Instance]` hypothesis and DERIVES the
 * published flat identity from it (sorry-free modulo the class instance).
 */
export default conjecture({
  label: "conj:proton-borromean-assembly",
  title:
    "The proton's Borromean mass assembly: multiplicity $\\dim V_{(2,1)} = 2$ and binding count $|S_3| = 6$",
  lean: {
    ref: "qou:QOU.AppendixQValues.ProtonBorromeanAssembly",
  },
  uses: [
    "def:f-bor-borromean-observable",
  ],
  tags: [
    "proton",
    "borromean",
    "mass-assembly",
    "constituent-multiplicity",
    "ocneanu",
    "conditional-class",
  ],
});
