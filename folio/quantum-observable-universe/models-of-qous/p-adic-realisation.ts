import { example } from "../../schema/builders";

export default example({
  interprets: "def:substrate-parameter",
  label: "ex:p-adic-realisation",
  title: "$\\mathbb{Q}_\\pp$ realisation",
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-21", body: "The bullet on Frobenius integrability said a $p$-adic instanton connection is integrable if and only if its $F$-crystal is unit-root. No source in the corpus or library states this, and it conflicts with the standard picture: every crystal's connection is integrable, while unit-root is the stronger condition matching $\\mathbb{Z}_p$-representations (André, *Period mappings and differential equations*, the section on crystals and connections, library `arxiv-math-0203194v1`). Rewritten to that." },
  ],
  cites: ["andre-baldassarri2002"],
  uses: [
    "ex:irreducible-connection",
    "rem:q-torsion-existence",
  ],
});
