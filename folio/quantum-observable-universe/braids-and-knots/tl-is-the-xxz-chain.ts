import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tl-is-the-xxz-chain",
  title:
    "The production trace computes in the algebra of a one-dimensional spin chain",
  interprets: "prop:substrate-massive-regime",
  uses: ["prop:substrate-massive-regime", "def:two-row-stratum"],
  cites: ["jones1985", "jimbo1986"],
  computation: {
    script: "computations/onedim/tl_is_the_xxz_chain_probe.py",
    engine: "python+mpmath",
    status: "verified",
  },
  tags: [
    "temperley-lieb",
    "spatially-one-dimensional",
    "spin-chain",
    "convention-d",
    "bethe-string",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The matrix identity above is verified numerically at both documented substrate anchors, to the precision of the computation, rather than formalised; the proposition's Lean covers the scalar identities on which it rests, not the assembly. The coefficient of the boundary term was initially transcribed with the wrong sign, and the discrepancy was resolved by solving for the coefficients from the matrix entries; the witness script records this, and the coefficients should not be restored to a remembered form without re-running it." },
  ],
});
