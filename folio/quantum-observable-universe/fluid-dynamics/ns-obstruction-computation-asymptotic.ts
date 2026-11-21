import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-obstruction-computation-asymptotic",
  title: "Formal asymptotic content of the jet divergence",
  interprets: "prop:ns-obstruction-computation",
  uses: [
    "def:surreal-blowup-calculus",
    "def:standard-part-functor",
    "rem:conway-normal-form",
    "rem:body-asymptotics-catalog",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The complete recursive jet tower establishes the [surreal blow-up calculus](#def:surreal-blowup-calculus), while the exact $q \\to 1$ classical-limit extraction requires the [standard-part map](#def:standard-part-functor). See also [Big-O via $\\ordw$](#rem:conway-normal-form) alongside the [body asymptotics catalog](#rem:body-asymptotics-catalog)." },
  ],
  tags: ["navier-stokes", "asymptotics", "surreal", "blowup"],
});
