import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**ENACTED 2026-09-15 (owner selection A).** The condition is now stated as `g(M_0) = 4`, equivalently `chi_eu(M_0) = -6`, about the base curve. The former wording `chi(A) = tr(id_A) = -6 in R` and the sentence \"the class `[A] in K_0(C)` has rank -6\" are withdrawn: under the ruling `tr(id_A) = dim_q(A)` the rank of `[A]` is a (regularised) quantum dimension, which is `0` for `A = O_q(SU(2))`, so that sentence was false. `K_0(C)` itself is now defined in `def:grothendieck-group-of-a-qou`. The Lean sibling keeps its `eulerChar = -6` field as the value of `chi_eu(M_0)`.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:archimedean-condition",
  lean: { ref: "qou:QOU.ArchimedeanCondition", validation: "not_checked" },
  title: "Descartes condition",
  tags: ["archimedean-universe", "euler-characteristic"],
  // rem:three-euler-characteristics dropped from uses[] 2026-11-20 (bean
  // qou-tm3c, owner rule "cut edges the text does not use"). The text links it
  // only to say which Euler characteristic chi_eu(M_0) is meant (the
  // topological one of a curve); the link stays in the .md. Through that
  // remark's mention of conj:wigner-axiom, this one edge put 92 provable
  // blocks downstream of the Wigner axiom, thm:descartes among them.
  uses: ["thm:qu-to-qou"],
});
