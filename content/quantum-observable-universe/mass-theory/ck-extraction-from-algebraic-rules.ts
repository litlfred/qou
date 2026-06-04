import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ck-extraction-from-algebraic-rules",
  interprets: "prop:q-beta-categorical-precision-ladder",
  title:
    "$c_k$ extraction from four algebraic reduction rules (Yang-Baxter, $q$-Young symmetrizers, Hecke quadratic, GB/jet) on the typed-$\\mathbf{B}_3$ word: the closed forms $c_k \\in \\{b, b^2, -2, b^2+1/2\\}$ are derivable outputs, not phenomenological identifications",
  uses: ["rem:braid-group-n-strand"],
  cites: [
    "kashiwara1990",
    "jones1985",
    "hoefsmit1974",
    "wenzl1988",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "ck-extraction",
    "algebraic-rules",
    "yang-baxter",
    "q-young-symmetrizers",
    "hecke-quadratic",
    "grobner-shirshov",
    "jet-bundle",
    "synthesis",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "**$c_4$ closed form has shifted.** The original $c_4 = b^2 + 1/2$ form below is superseded by $c_4 = c_3 \\cdot b^4 = -2 b^4$ (per the SDP-$T_\\beta$ derivation and `prop:q-beta-categorical-precision-ladder`). The $b^2 + 1/2$ shape is now attributed to $c_5$ (with sign flip: $c_5 = -(b^2 + 1/2)$). The four-rule reframing remains valid; only the per-rung closed-form column needs updating. Audit: `docs/audits/-qbeta-all-ck-categorical-extension.md`.",
    },
  ],
});
