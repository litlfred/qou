import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-binding-amplitude",
  title:
    "Hoefsmit binding amplitude $b^2 = [3]_q / [2]_q^2$",
  lean: { ref: "qou:QOU.BraidsAndKnots.hoefsmit_b_sq_eq_q3_over_q2sq" },
  uses: ["prop:frobenius-lepton-meson-bridge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling states the identity in terms of $[2]_q$ alone and needs only $[2]_q \\neq 0$." },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Base ring minimised (AGENTS.md §7c).** The Lean sibling moved from " +
        "`[Field R]` + `field_simp` to a generic `[CommRing R]` with the " +
        "modulus carried as a unit `q : Units R`, so `↑q⁻¹` is a `Units` coercion " +
        "rather than a ring inverse; `[2]_q² = h² + 4` and `[3]_q = [2]_q² − 1` " +
        "are each one `linear_combination` against `↑q · ↑q⁻¹ = 1`. The " +
        "amplitude identity is now stated division-free as " +
        "`binding_amplitude_iff`: `b²·[2]_q² = [3]_q ↔ (1 − b²)·[2]_q² = 1`, " +
        "an equivalence over any commutative ring with **no** non-vanishing " +
        "hypotheses — the R[h] multiplicative form of `b² = [3]_q/[2]_q²` and " +
        "`1 − b² = 1/[2]_q²`. Note this file never needed ℝ: the Hoefsmit " +
        "square root is already avoided by carrying `b` through its defining " +
        "quadratic, so it is a substrate-side block, not an archimedean one. " +
        "A field survives only in the `RatioForm` section holding the two " +
        "quotient presentations quoted in the `.md`; " +
        "`hoefsmit_b_sq_eq_q3_over_q2sq` keeps its exact previous statement " +
        "there.",
    },
  ],
  cites: [
    "wenzl1988c",
  ],
  tags: [
    "hoefsmit",
    "binding-amplitude",
    "meson",
    "pion-decay",
    "q-integer",
    "lepton-meson-bridge",
  ],
});
