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
    "def:hecke-mass-element",
    "prop:hecke-mass-trace",
    "def:transfer-matrix-operator",
    "rem:skein-binding-lagrangian",
  ],
  cites: [
    "jones1985",
    "kock2004",
  ],
});
