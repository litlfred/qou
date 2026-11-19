import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-angular-momentum",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs\u2014real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here." },
  ],
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
});
