import { proof } from "../../schema/builders";

export default proof({
  label: "prf:emergence-to-quantum-flat",
  title: "Proof of From Tannakian emergence to 2-group quantum flatness",
  uses: ["prop:emergence-to-quantum-flat"],
  cites: ["baez2004", "baez-schreiber2007"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-t3ox: clarified the scope of INN(G_q) uniqueness under the Baez-Lauda crossed-module equivalence (`baez2004`) and Baez-Schreiber fake-curvature condition (`baez-schreiber2007` §4). Infinitesimally, F_A = d(partial)(B) plus simplicity B^- = 0 gives F_A^- = 0 for any crossed module partial : H -> G_q whose Lie-algebra differential d(partial) is an isomorphism (including discrete central extensions with ker(partial) != 1); strict 2-group uniqueness of INN(G_q) holds precisely when global group-level faithfulness ker(partial) = 1 and surjectivity coker(partial) = 1 are imposed alongside d(partial) = id.",
    },
  ],
});
