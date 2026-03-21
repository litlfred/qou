import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mi-sw-abelianisation",
  title: "Abelianisation of the MI integral on exceptional divisors",
  hasProof: true,
  uses: [
    "rem:brings-smoothness",
    "def:mass-identity",
    "rem:chiral-bundles",
    "rem:weight-space-decomposition",
    "prop:jet-prolongation",
    "rem:color-tube-cubic",
  ],
});
