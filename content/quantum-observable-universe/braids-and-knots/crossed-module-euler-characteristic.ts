import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossed-module-euler-characteristic",
  title: "Hecke crossed module h² trace equals $\\dim(V) \\cdot \\chi(\\Sigma_4)$",
  uses: [
    "def:borromean-baryon-mass-formula",
    "prop:quaternion-from-hecke-eigenspaces",
  ],
  lean: { ref: "qou:QOU.BraidKnot.CrossedModuleEulerCharacteristic" },
});
