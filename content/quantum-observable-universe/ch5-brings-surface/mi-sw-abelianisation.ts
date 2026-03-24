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
    "rem:chiral-bundles",
    "rem:weight-space-decomposition",
    "prop:jet-prolongation",
    "rem:color-tube-cubic",
  ],
  proofs: ["prf:mi-sw-abelianisation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mi-sw-abelianisation-0.svg", blockIndex: 0, hash: "af7757ccd6f4" },
  ],

});
