import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:alpha-k-derivation-procedure",
  label: "rem:alpha-k-derivation-procedure-proof-sketch",
  title: "Proof sketch: alpha k derivation procedure",
  uses: ["conj:alpha-k-derivation-procedure"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): For exact rational forms, replace numeric `numpy.linalg.solve` with\n`sympy` over a symbolic $q$." },
  ],
});
