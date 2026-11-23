import { prose } from "../../schema/builders";

export default prose({
  label: "sec:strangelet-intro",
  uses: ["rem:golden-ratio-degeneration"],
  meta: { position: "opening" },
  cites: [
    "alford1999",
    "witten1984",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: each quark carries the crossings of its lepton partner (5 for $\\mathfrak{s}$, 3 for $\\mathfrak{d}$). Under the ruling both $\\mathfrak{d}$ and $\\mathfrak{s}$ are single negative crossing letters $\\sigma_i^{-1}$ in $\\mathcal{B}_3$ (dictionary Table 4), so the $4/3$ pairing factor, the neutrality claim and the factor-93 Jones cost comparison need re-scoping. Still valid: the Jones polynomials of $T_{2,3}^{\\sigma}$ and $T_{2,5}^{\\sigma}$ themselves, and Stages 1–3 insofar as they do not use the 5-versus-3 count." },
  ],
});
