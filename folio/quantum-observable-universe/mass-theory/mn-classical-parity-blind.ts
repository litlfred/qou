import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:schur-weyl-mass-decomposition",
  label: "rem:mn-classical-parity-blind",
  title:
    "Classical Murnaghan–Nakayama characters are parity-blind: proton ≡ neutron at $q = 1$",
  tags: [
    "murnaghan-nakayama",
    "classical-limit",
    "character",
    "q-deformation",
    "proton-neutron",
    "parity",
  ],
  uses: ["prop:schur-weyl-mass-decomposition"],
});
