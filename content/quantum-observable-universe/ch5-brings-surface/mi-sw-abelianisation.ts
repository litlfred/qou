import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mi-sw-abelianisation",
  lean: {
    decl: "QOU.Brings.mi_sw_abelianisation",
    validation: "not_checked",
  },
  title: "Abelianisation of the MI integral on exceptional divisors",
  uses: [
    "rem:brings-smoothness",
    "def:mass-identity",
    "rem:weight-space-decomposition",
    "rem:color-tube-cubic",
  ],
  proofs: ["prf:mi-sw-abelianisation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mi-sw-abelianisation-0.svg", blockIndex: 0, hash: "14223e481516" },
  ],

});
