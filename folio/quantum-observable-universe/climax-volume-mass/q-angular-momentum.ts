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
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
