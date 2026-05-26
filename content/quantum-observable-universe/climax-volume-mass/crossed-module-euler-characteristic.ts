import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossed-module-euler-characteristic",
  title: "Hecke crossed module h² trace equals $\\dim(V) \\cdot \\chi(\\Sigma_4)$",
  uses: [
    // broken-ref removed (Phase 7): def:borromean-baryon-mass-formula
    // broken-ref removed (Phase 7): prop:quaternion-from-hecke-eigenspaces
  ],
  lean: { ref: "qou:QOU.BraidKnot.CrossedModuleEulerCharacteristic" },
});
