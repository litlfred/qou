import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:noble-gas-characterization",
  lean: { ref: "qou:QOU.Descartes.noble_gas_characterization", validation: "not_started" },
  title:
    "Noble gas characterization: full shell as full curls",
  tags: [
    "noble-gas",
    "electron-shell",
    "hopf-link",
    "sub-link",
    "trefoil",
    "closed-shell",
    "curl",
    "helium",
    "neon",
    "argon",
  ],
  uses: ["rem:helium-hopf-diagram"],
});
