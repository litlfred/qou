import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean conjunct (ii) used to return the Hurwitz hypothesis unchanged; it now derives $|\\mathrm{Aut}| \\le 252$ at $g = 4$. The phrase \"maximal genus consistent with the Hurwitz bound\" is withdrawn: the bound holds for every $g \\ge 2$ (round-trip audit pass 2, C16)." },
  ],
  label: "prop:genus-maximal-descent",
  lean: { ref: "qou:QOU.Archimedean.genus_maximal_descent",
    validation: "not_checked",
  },
  title: "Genus of the one-complex-dimensional descent",
  tags: ["archimedean-universe", "genus", "riemann-roch"],
  uses: [
    "def:archimedean-condition",
  ],
  proofs: ["prf:genus-maximal-descent"],
});
