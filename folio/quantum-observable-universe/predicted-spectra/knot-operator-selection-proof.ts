import { proof } from "../../schema/builders";

export default proof({
  label: "prf:knot-operator-selection",
  title: "Proof of knot operator selection",
  uses: ["prop:knot-operator-selection"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**🟧 OWNER RULING 2026-09-15 settles the symbol: `tr(id_A)` is the quantum dimension `dim_q(A)`, the Euler characteristic of an object IN THE QOU CATEGORY — so it is q-DEPENDENT.** **This block's reading is the one the owner selected.** `[2]_q = q + q^-1 = 2.0108968667` at the proton `q_0` is `dim_q` of the fundamental `V_1`, and under the ruling that IS the categorical Euler characteristic. Nothing here changes; the note is recorded so a reader meeting `-6` or `2` elsewhere knows those are topological Euler characteristics of a state bundle, a different object. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean formalisation of the Convention-D Markov Gram radical on H_3 (det G = 0 on H_n with the (1^3) block as radical, non-degenerate on H_n / rad tr_M ≅ TL_n): `lean/QOU/QBeta/MarkovGramDegenerate.lean`.",
    },
  ],
});
