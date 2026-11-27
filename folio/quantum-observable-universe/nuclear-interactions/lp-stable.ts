import { definition } from "../../schema/builders";

export default definition({
  label: "def:lp-stable",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs \u2014 real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here." },
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.LPStable", validation: "not_checked" },
  title: "LP-stable element of $H_3(q)$",
  tags: [
    "lp-stability",
    "gram-matrix",
    "confinement",
    "hecke-algebra",
  ],
  uses: [],
});
