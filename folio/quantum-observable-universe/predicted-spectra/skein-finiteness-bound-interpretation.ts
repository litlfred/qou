import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skein-finiteness-bound",
  label: "rem:skein-finiteness-bound-interpretation",
  title: "The nuclear chart lattice and particle finiteness",
  uses: [
    "prop:skein-finiteness-bound",
    "prop:beta-stability",
    "prop:shell-closure-normal-form",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Owner rulings 2026-11-21 (electron sigma_0 sigma_1 sigma_0, Hopf closure) and 2026-11-20 (up quark an unknot strand): the six embeddable torus knots are no longer said to be exactly the quarks, leptons and force carriers." },
  ],
});
