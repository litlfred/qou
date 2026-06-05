import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-sw-tau-decomposition",
  lean: {
    ref: "qou:QOU.Brings.jet_sw_tau_decomposition",
    validation: "validated",
  },
  title: "The Seiberg–Witten differential is the jet decomposition of the Archimedean functor",
  uses: [
    "prop:mi-sw-abelianisation",
    "prop:sw-period-residue-sum",
  ],
  proofs: ["prf:jet-sw-tau-decomposition"],
});
