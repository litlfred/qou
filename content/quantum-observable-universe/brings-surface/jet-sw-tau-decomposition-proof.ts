import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-sw-tau-decomposition",
  title: "Proof of the jet decomposition of the Archimedean functor",
  uses: [
    "prop:jet-sw-tau-decomposition",
    "prop:mi-sw-abelianisation",
  ],
});
