import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wigner-axiom",
  title: "The Wigner axiom: a one-dimensional classical-limit obstruction",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.WignerAxiom",
    validation: "stub",
  },
  uses: [
    "def:classical-limit-obstruction",
    "lem:brings-euler-characteristic",
  ],
  cites: ["wigner1960", "weibel1994", "brown-zhang-2008", "hadfield-krahmer-2005"],
  tags: ["conjecture", "primary-conjecture", "classical-limit", "obstruction", "millennium-problem", "wigner"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Owner instruction 2026-09-15: 'if need an axiom for millennium problems, call it the Wigner Axiom and cite 1959 paper'. Primary conjecture per AGENTS.md §3b-tax (its Lean class binds no other conjecture class); content-bearing fields; NO instance is supplied. What it replaces: the former part (a) of `thm:qou-obstruction-reduction`, which claimed `dim HH^2(U_q, Ad) = 1` as a theorem by an argument that stated Van den Bergh duality untwisted and cohomology-to-dual-cohomology (Brown–Zhang's form is cohomology-to-homology with the Nakayama twist), conflated `HH^1` with `HH^2`, and is contradicted at `q = 1` by Whitehead's lemma. The equivariance argument fixing the target of clause (W2) is `QOU.Brings.S5Char.hochschild_invariants_of_base` (sorry-free).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; the reduction itself ([obstruction reduction](#thm:qou-obstruction-reduction)) is then a theorem" },
  ],
});
