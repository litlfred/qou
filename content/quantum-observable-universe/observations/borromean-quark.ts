import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-quark",
  title:
    "Quarks as Borromean-linked unknots in the exceptional divisor",
  lean: {
    ref: "qou:QOU.Archimedean.BorromeanQuark",
    validation: "not_checked",
  },
  tags: [
    "borromean",
    "quark",
    "unknot",
    "neutrino",
    "color-confinement",
    "exceptional-divisor",
    "hyperbolic-volume",
  ],
  uses: [
    "def:neutrino-knot",
    "def:observable-mtc",
    "prop:bn-mtc-action",
    // NOTE: `prop:ns-obstruction-tower` is INTENTIONALLY OMITTED here.
    // PR #1076 added it to document the narrative bridge to the
    // fluid-dynamics NS-obstruction tower, but it cascaded the 5-
    // conjecture NS web into every quark/electron-using block's
    // transitive cone, bloating §3b-cond audit gaps 9 → 22. The
    // bridge is preserved as a markdown cross-reference in
    // intro-ns-obstruction-tower-mtc.md (text-level, not in the
    // manifest dependency graph). Adding it back here requires
    // either teaching the audit not to propagate via conjectures,
    // or banner+class-hyp on the ~13 affected props.
  ],
});
