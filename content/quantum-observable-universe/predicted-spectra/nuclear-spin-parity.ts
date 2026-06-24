import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-spin-parity",
  proofs: ["prf:nuclear-spin-parity"],
  title:
    "Nuclear spin is integral for even $A$ and half-integral for odd $A$",
  tags: [
    "nuclear-spin",
    "angular-momentum",
    "fermion",
    "boson",
    "braid-group",
    "su-q-2",
    "nitrogen-14",
    "statistics",
  ],
  lean: { ref: "qou:QOU.Archimedean.nuclear_spin_parity",
    validation: "not_checked",
  },
});
