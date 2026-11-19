import { example } from "../../schema/builders";

/**
 * The six-term Gröbner–Shirshov normal form of the nucleon Hecke
 * element and its net evaluated at the substrate parameter q_0.
 */
export default example({
  label: "ex:nucleon-hecke-element-normal-form",
  title: "Six-term normal form and net of the nucleon",
  interprets: "def:nucleon-hecke-element",
  uses: ["def:nucleon-hecke-element"],
  tags: [
    "nucleon",
    "normal-form",
    "hecke-algebra",
    "net",
    "witness",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: breit-wheeler-nucleon-nf.witness.json.",
    },
  ],
});
