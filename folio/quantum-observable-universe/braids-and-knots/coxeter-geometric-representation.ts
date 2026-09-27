import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). " +
        "The $\\mathbb{R}$ here is load-bearing, not incidental: this is the Tits " +
        "geometric representation, whose bilinear form coefficient is the " +
        "*transcendental* $B(\\alpha_i,\\alpha_j) = -\\cos(\\pi/m_{ij})$ " +
        "(`bilinCoeff = -Real.cos (Real.pi / m)`), so the root space is `B →₀ ℝ`. The " +
        "proof of `reflEnd_pair_pow_eq_one` — that $(f_i f_j)^{m} = 1$ at every bond " +
        "order — is a real-trigonometric periodicity argument: the two-step recursion " +
        "`u(k+2) = 2·Real.cos φ·u(k+1) − u(k)` closed by `Real.sin_two_pi`, " +
        "`Real.sin_pos_of_pos_of_lt_pi` and the ordering facts `0 < φ < π`, `c² < 1` " +
        "(`nlinarith`). Ordering plus `Real.sin`/`Real.cos` are exactly the §7c " +
        "archimedean row, so no `CommRing` restatement of *this* argument exists " +
        "short of redoing it over a Chebyshev/real-cyclotomic ring — different " +
        "mathematics, not a de-specialisation. What does stay generic and is " +
        "deliberately kept so: the module's downstream payoffs " +
        "`braid_at_pair_unconditional` and `far_commute_at_pair_unconditional`, " +
        "which consume the $\\mathbb{R}$ faithfulness result but are stated over " +
        "`{R : Type*} [CommRing R]` on the Hecke length-rule module.",
    },
  ],
  label: "prop:coxeter-geometric-representation",
  lean: {
    ref: "qou:QOU.Machinery.CoxeterParabolic.simple_injective",
    validation: "not_checked",
  },
  title:
    "The geometric representation: simple-injectivity at every Coxeter system",
  tags: [
    "coxeter",
    "geometric-representation",
    "faithfulness",
    "chebyshev",
    "hecke-algebra",
  ],
  uses: [
    "prop:coxeter-tits-residue-collapse",
    "prop:coxeter-parabolic-transversal",
  ],
  cites: ["kassel1995", "jones1987"],
});
