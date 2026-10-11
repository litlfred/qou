import { remark } from "../../schema/builders";

export default remark({
  label: "rem:elliptic-stability-locus",
  interprets: "prop:integer-stability",
  title:
    "The nuclear degeneracy locus is an elliptic curve over the Bring's surface",
  lean: {
    ref: "qou:QOU.EllipticStabilityLocus.EllipticStabilityLocus",
    validation: "not_checked",
  },
  tags: [
    "elliptic-curve",
    "stability",
    "diophantine",
    "color-fibration",
    "coulomb",
    "pairing",
    "bring-surface",
  ],
  uses: [
    "prop:integer-stability",
    "def:color-tube-fibers",
    "prop:neutron-prediction-comparison",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-11",
      body: "Normalisation reconciled 2026-10-11 (owner picks 1+2, bean `qou-opjb`). Minimising $a_C p^2/A^{1/3} + a_A(A-2p)^2/A$ in $p$ gives $p^* = A/(2 + cA^{2/3})$ with $c = a_C/(2a_A)$, the form of `prop:beta-stability`. Three blocks had disagreed: `prop:integer-stability` wrote the quadratic with $a_A$ where $4a_A$ belongs (so $p^* = A/(2 + 4cA^{2/3})$) and $a_C = (q-q^{-1})\\lambda_C$, which applies $(q-q^{-1})$ twice; `rem:diophantine-valley` wrote $t^3 = 2p(1 + ct^2)$, i.e. $2c$ in place of $c$; and `rem:elliptic-stability-locus` inherited the doubled form. All three now follow `prop:beta-stability`. In this block every $2c$ became $c$, and the coefficient match now lands at $p \\approx 736.8$. Still not derived here: the conjecture's $z(p) = -1/(cp)$ differs from the match condition $z = -(cp+1)$; the pairing coefficient $2\\lambda_P/a_A$ in (D) is untraced; and the Möbius substitution $t = \\alpha X + \\beta$ is stated but not used in the matching.",
    },
  ],
});
