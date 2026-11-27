import { remark } from "../../schema/builders";

export default remark({
  label: "rem:transfer-matrix-operator-properties",
  interprets: "def:transfer-matrix-operator",
  title:
    "Action on the GS ideal, operator algebra, interaction catalogue, and composition rules",
  tags: [
    "transfer-matrix",
    "operator",
    "hecke-algebra",
    "groebner",
    "hadron",
    "knot",
    "crossing",
    "universal",
    "interaction",
  ],
  uses: [
    "def:transfer-matrix-operator",
    "prop:beta-decay-transfer-matrix",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the nuclear rows of the interaction catalogue gave each quark the knot $T_{2,3}$ or $T_{2,3}^{\\sigma}$, under the lead sentence that the interaction type is set by the strands' knot types. Still valid: the assignment $\\mathfrak{u}\\mathfrak{u} \\mapsto T_{pp}$, $\\mathfrak{d}\\mathfrak{d} \\mapsto T_{nn}$, $\\mathfrak{u}\\mathfrak{d} \\mapsto T_{\\mathrm{mix}}$, which depends only on crossing orientation. Needs re-scoping: the lead sentence (for quarks the type is set by crossing orientation), and the physical readings 'proton-proton repulsion' / 'proton-neutron binding', which were argued from the trefoil pair." },
  ],
});
