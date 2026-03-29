import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-spin-parity",
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
  lean: {
    decl: "QOU.Descartes.nuclear_spin_parity",
    validation: "not_checked",
  },
  uses: [
    "def:stable-nucleus",
    "prop:fermion-boson-knot-link",
  ],
});
