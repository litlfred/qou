import { proof } from "../../schema/builders";

export default proof({
  label: "prf:alpha-k-derivation-procedure",
  title: "Proof of alpha k derivation procedure",
  uses: ["prop:alpha-k-derivation-procedure"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): For exact rational forms, replace numeric `numpy.linalg.solve` with `sympy` over a symbolic $q$." },
  ],
});
