import { remark } from "../../schema/builders";

export default remark({
  label: "rem:torus-knot-prime-powers",
  title: "Prime-power structure of $T_{3,p^k}$ generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "torus-knot",
    "prime-power",
    "genus",
    "mass-hierarchy",
    "trefoil",
    "top-quark",
    "self-intersection",
  ],
  uses: ["rem:unmapped-torus-knots"],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the trefoil's membership of both the $m = 2$ (leptonic) and $m = 3$ (quark) families was read as the reason one knot type encodes the electron and the up quark ('common seed'). Still valid: the knot-theoretic facts ($T_{3,2} = T_{2,3}$, the Mersenne genus tower, embeddability on Bring's surface). Needs re-scoping: what the $m = 3$ family assigns to the quark sector, since a quark is now an unknot strand rather than a member of a torus-knot family." },
  ],
});
