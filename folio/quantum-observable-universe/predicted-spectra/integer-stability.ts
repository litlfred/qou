import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:integer-stability",
  title:
    "Integer stability: the valley of stability as a Diophantine constraint",
  tags: [
    "stability",
    "diophantine",
    "integer",
    "valley-of-stability",
    "coulomb",
    "magic-numbers",
  ],
  lean: { ref: "qou:QOU.Archimedean.integer_stability",
    validation: "not_checked",
  },
  uses: ["def:stable-nucleus", "prop:beta-stability"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "caveat",
      date: "2026-10-11",
      body: "Normalisation reconciled 2026-10-11 (owner picks 1+2, bean `qou-opjb`). Minimising $a_C p^2/A^{1/3} + a_A(A-2p)^2/A$ in $p$ gives $p^* = A/(2 + cA^{2/3})$ with $c = a_C/(2a_A)$, the form of `prop:beta-stability`. Three blocks had disagreed: `prop:integer-stability` wrote the quadratic with $a_A$ where $4a_A$ belongs (so $p^* = A/(2 + 4cA^{2/3})$) and $a_C = (q-q^{-1})\\lambda_C$, which applies $(q-q^{-1})$ twice; `rem:diophantine-valley` wrote $t^3 = 2p(1 + ct^2)$, i.e. $2c$ in place of $c$; and `rem:elliptic-stability-locus` inherited the doubled form. All three now follow `prop:beta-stability`.",
    },
  ],
});
