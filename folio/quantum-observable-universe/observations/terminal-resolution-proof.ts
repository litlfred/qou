import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of the pair Skein nucleon identities",
  uses: [
    "lem:pair-skein-mass-formula",
  ],
});
