import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-angular-momentum",
  title: "$q$-Angular momentum from the $\\mathrm{SU}_q(2)$ Casimir",
  tags: [
    "angular-momentum",
    "q-deformed",
    "su-q-2",
    "casimir",
    "spin",
    "braid",
    "jones-wenzl",
  ],
  lean: { ref: "qou:QOU.Archimedean.QAngularMomentum",
    validation: "not_checked",
  },
  uses: [
    "def:q-momentum",
    "def:q-casimir",
    "prop:nuclear-spin-parity",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The asymmetry at $q \\neq 1$ connects directly to parity violation ([parity violation](#prop:parity-violation-skein))." },
  ],
});
