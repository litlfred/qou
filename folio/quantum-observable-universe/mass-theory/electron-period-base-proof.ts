import { proof } from "../../schema/builders";

export default proof({
  label: "prf:electron-period-base",
  title: "Proof that the electron period is the n=0 base",
  uses: ["prop:electron-period-base", "prop:jet-sw-tau-decomposition"],
});
