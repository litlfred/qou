import { definition } from "../../schema/builders";

export default definition({
  label: "def:strong-multiplicativity",
  renamedFrom: ["thm:strong-multiplicativity"],
  title: "Strong multiplicativity",
  lean: { ref: "fred2005:Fred2005.StrongMult.IsStronglyMultiplicative",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body: "Rewritten to the source. Until 2026-11-21 this block was `thm:strong-multiplicativity`, stating $\\Delta(xy) = \\Delta(x)\\Delta(y)$ and attributing a preservation result to \"[fred2005, Thm 4.12]\". arXiv:math/0602138 has no Theorem 4.12; strong multiplicativity is Def. 1.11, a condition on the comultiplication of the splay algebra relative to the Poisson bracket, and Prop. 1.13 is its consequence. The condition is formalised as `Fred2005.StrongMult.IsStronglyMultiplicative μ Δ π` (an equation of linear maps over a noncommutative $R$-algebra), where `μ` is the ordered product of $S = \\otimes A_i$ transported to $T$, not $T$'s own product (QA 2026-11-21), with Remark 1.12 as `prim_of_isStronglyMultiplicative`: for a bracket vanishing against the unit, $\\Delta$ sends the bracket of two primitives to a primitive. Prop. 1.13 is not formalised.",
    },
  ],
  tags: ["strong-multiplicativity", "comultiplication", "poisson"],
  uses: ["def:skewed-poisson-structure"],
  cites: ["leitner2006"],
});
