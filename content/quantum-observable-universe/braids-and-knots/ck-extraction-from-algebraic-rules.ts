import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ck-extraction-from-algebraic-rules",
  interprets: "prop:q-beta-categorical-precision-ladder",
  title:
    "$c_k$ extraction from four algebraic reduction rules (Yang-Baxter, $q$-Young symmetrizers, Hecke quadratic, GB/jet) on the typed-$\\mathbf{B}_3$ word: the closed forms $c_k \\in \\{b, b^2, -2, b^2+1/2\\}$ are derivable outputs, not phenomenological identifications",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:q-beta-c3-hopf-three-fold-markov",
    "rem:typed-b3-sub-braid-extraction",
    "rem:markov-axioms-primitive",
    "rem:braid-group-n-strand",
  ],
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
});
