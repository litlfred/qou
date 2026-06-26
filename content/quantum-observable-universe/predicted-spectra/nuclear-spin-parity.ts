import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "Although consistent with standard spin-statistics, formulating the parity content strictly via SU_q(2)/tensor-product categorical rules provides a novel synthesis, embedding empirical parity constraints algebraically within the quantum observable universe without invoking ad-hoc external postulates." },
  ],
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
  lean: { ref: "qou:QOU.Archimedean.nuclear_spin_parity",
    validation: "not_checked",
  },
});
