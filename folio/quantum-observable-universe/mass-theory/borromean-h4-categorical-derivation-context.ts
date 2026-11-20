import { remark } from "../../schema/builders";

export default remark({
  label: "rem:borromean-h4-categorical-derivation-context",
  title: "Wider-framework connection and significance of the Borromean h^4 factorisation",
  interprets: "prop:borromean-h4-categorical-derivation",
  tags: ["borromean", "markov-trace", "wenzl-weights", "h4"],
  uses: ["prop:borromean-h4-categorical-derivation"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):   relation $q\\sigma^2 = (q^2 − 1)\\sigma + q$, formalised\n  in `QOU.Hecke.SpectralProjector` (`eminus_idem`,\n  `eplus_eminus_orthogonal`, `eplus_add_eminus = 1`).\n  Closed-form trace computation on $V^{\\otimes 3}$ can be done via\n  the Cayley–Hamilton block reduction\n  `QOU.Braiding.HeckeGenPolyReduction.hecke_gen_poly_reduction`.\n\ncomputation; both are now valid Lean entry points to the same\n`χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶` identity." },
  ],
});
