import { definition } from "../../schema/builders";

/**
 * Top-channel decoration of a positive torus knot on its braid index:
 *
 *   δ_q^top(T_{m,p}) := q^w − q^{−w},   w = (m−1)p,   m ≤ p,
 *
 * the bar-odd part of the trivial-representation eigenvalue q^w of the
 * braid (σ₁⋯σ_{m−1})^p. This is the rule the producer
 * computations/rosso_jones_three_strand_delta_q.py uses; it was not
 * stated as a definition anywhere in the paper before (owner ruling
 * 2026-11-15, option A).
 */
export default definition({
  label: "def:torus-knot-top-channel-decoration",
  title:
    "Top-channel decoration $\\delta^{\\mathrm{top}}_q(T_{m,p}) = q^{w} - q^{-w}$ of a torus knot",
  uses: ["def:delta-q-decoration"],
  defines: ["torus-knot-top-channel-decoration"],
  lean: { ref: "qou:QOU.TorusKnotTopChannel.topChannelDecoration" },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/rosso_jones_three_strand_delta_q.py",
    witness: ["computations/rosso-jones-three-strand-delta-q.witness.json"],
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body:
        "**Why this block exists.** `prop:alpha-em-categorical-trace-ratio` needs $\\delta_q(T_{3,5}) = h[10]_q$. " +
        "Its derivation said this comes from summing the characters over $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$, but that sum is " +
        "$q^{10} - 1 + q^{-10}$, because $\\chi_{(2,1)}((\\sigma_1\\sigma_2)^5) = -1$. The value $h[10]_q$ comes only from the " +
        "top-channel bar-odd rule of the producer, which `def:delta-q-decoration` (a tuple of characters) does not state. " +
        "The owner ruled on 2026-11-15 (option A) that the rule be stated as its own definition. The new symbol " +
        "$\\delta^{\\mathrm{top}}_q$ avoids reusing $\\delta_q$ for two objects. No computed value changes.",
    },
  ],
  tags: ["delta-q", "torus-knot", "writhe", "bar-involution", "alpha-em", "pre-archimedean"],
});
