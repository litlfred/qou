import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:mass-comparison-table",
  label: "rem:atom-mass-full-hecke",
  title: "Atomic mass of $Z = 1$--$10$ via full three-channel Hecke algebra",
  tags: [
    "mass",
    "hecke-engine",
    "three-channel",
    "symmetric",
    "alternating",
    "standard",
    "wedderburn",
    "binding-energy",
    "skein-lagrangian",
  ],
  uses: [
    "rem:mass-comparison-table",
    "rem:hecke-charge-mass-duality",
    "def:transfer-matrix-operator",
  ],
  cites: [
    "jones1985",
    "kock2004",
  ],
});
