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
    "prop:beta-stability",
    "prop:color-elliptic",
    "prop:descartes-elliptic-curve",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (proved in Lean, `no_affine_match`)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The obstruction is proved in the Lean sibling." },
    {
      kind: "caveat",
      date: "2026-10-11",
      body: "Normalisation reconciled 2026-10-11 (owner picks 1+2, bean `qou-opjb`). Minimising $a_C p^2/A^{1/3} + a_A(A-2p)^2/A$ in $p$ gives $p^* = A/(2 + cA^{2/3})$ with $c = a_C/(2a_A)$, the form of `prop:beta-stability`. Three blocks had disagreed: `prop:integer-stability` wrote the quadratic with $a_A$ where $4a_A$ belongs (so $p^* = A/(2 + 4cA^{2/3})$) and $a_C = (q-q^{-1})\\lambda_C$, which applies $(q-q^{-1})$ twice; `rem:diophantine-valley` wrote $t^3 = 2p(1 + ct^2)$, i.e. $2c$ in place of $c$; and `rem:elliptic-stability-locus` inherited the doubled form. All three now follow `prop:beta-stability`. In this block every $2c$ became $c$, and the coefficient match now lands at $p \\approx 736.8$. Owner pick 2026-10-11: the conjecture now states $z(p) = -(cp+1)$, the value the coefficient match actually gives (the former $-1/(cp)$ had no derivation). The unused Möbius substitution $t = \\alpha X + \\beta$ was removed; the table now records that under $X = t$ only the quadratic coefficient agrees, the linear one never does, and the constant term agrees only at $p \\approx 736.8$. Upstream fixes in the same pass: item 2 cited the color-tube cubic, but the matching uses the color elliptic cubic (C), so it now cites (C); the Descartes curve discriminant was printed as $-(4a^3+27b^2) \\approx -18.95$, 16 times small, and is now the standard $-16(4a^3+27b^2) \\approx -303.17$ (recomputed at the proton $q_0$; $j \\approx 129.86$ unchanged, bean `qou-3nva`). The 'shares its algebraic origin (exact)' bullet contradicted the 'unproven' paragraph and was replaced by the measured coefficient statement.",
    },
    {
      kind: "note",
      date: "2026-10-11",
      body: "(D) is now derived, not stated: equal energy of the even-even nucleus $(p, A)$ and the odd-odd nucleus $(p+1, A)$, from the `prop:integer-stability` energy and pairing $\\mp\\lambda_P/A^{1/2}$. It gives the stability cubic in $\\bar p = p + 1/2$ with right-hand coefficient $\\lambda_P/(2a_A)$; the previous $2\\lambda_P/a_A$ was 4 times too large, the same $a_A$-for-$4a_A$ slip. Checked with sympy (bean `qou-opjb`).",
    },
    {
      kind: "note",
      date: "2026-10-11",
      body: "Affine obstruction added (owner picks 2+1). The invariant $J = 4P^3/(4P^3+27Q^2)$ of the depressed cubic is unchanged by $X \\mapsto \\alpha X + \\beta$; it is positive for (C) at every real $z$ and negative for (S) at every real $p \\neq 0$, $c > 0$. Lean: `QOU.EllipticStabilityLocus.no_affine_match` (sorry-free, axioms propext/Classical.choice/Quot.sound). The 'up to Möbius' wording was dropped as vacuous; the conjecture's item 2 now rests on the isogeny alone, and the conjecture stays open (bean `qou-opjb`).",
    },
  ],
});
