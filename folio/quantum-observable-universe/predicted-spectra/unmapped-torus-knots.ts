import { remark } from "../../schema/builders";

export default remark({
  label: "rem:unmapped-torus-knots",
  title: "Unmapped genus-$4$ torus knot generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "torus-knot",
    "genus-4",
    "saturating",
    "unmapped",
    "strong-force",
    "weak-force",
  ],
  uses: [
    "prop:torus-embeddable-complete",
    "rem:knot-formula-table",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the genus-1 to genus-3 torus knots were assigned to quarks as well as leptons. Still valid: the genus bookkeeping and the count of unused genus-4 generators, now read as the lepton sector plus the quarks' lepton partners. Needs re-scoping: the sentence 'Standard Model fermions exhaust at genus 3', since quarks (unknot strands) carry genus 0." },
  ],
});
