import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:euler-char-stability",
  title: "Stability of the categorical trace and of the base Euler characteristic",
  tags: ["euler-characteristic", "brane-tower", "frobenius-trace"],
  lean: { ref: "qou:QOU.Torsion.euler_char_constant",
    validation: "not_checked",
  },
  uses: ["def:quantum-characteristic-classes", "rem:three-euler-characteristics"],
  proofs: ["prf:euler-char-stability", "prf:euler-char-stability-C"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**RESTATED 2026-09-15.** The previous statement identified the categorical trace `tr(id_{A_n})` with the topological Euler characteristic of the total space `S_n`. Its own archimedean proof computed `chi(S_{n+1}) = chi(S_n) * chi(S^2) = 2 chi(S_n)` and then asserted stability anyway, switching to the base `M_0` in its last sentence. The statement now separates the two stable quantities — the categorical trace (a quantum dimension, q-dependent) and `chi_eu(M_0)` — and records that the total space's Euler characteristic doubles. The Lean carrier `QOU.Torsion.euler_char_constant` proves abstract stability from a `stable` field and is unaffected. Analysis: `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §4.",
    },
  ],
});
