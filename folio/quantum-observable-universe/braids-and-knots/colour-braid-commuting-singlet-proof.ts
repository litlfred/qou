import { proof } from "../../schema/builders";

export default proof({
  label: "prf:colour-braid-commuting-singlet",
  title: "Proof that a braid-commuting map keeps the singlet line",
  uses: ["prop:colour-braid-commuting-singlet", "prop:colour-singlet-flavour-generator", "prop:colour-relabel-singlet"],
});
