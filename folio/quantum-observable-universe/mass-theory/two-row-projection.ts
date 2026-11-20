import { definition } from "../../schema/builders";

/**
 * Two-row projection π_{2-row} of the Hecke algebra H_n(q).
 *
 * The orthogonal projection onto the two-row Wedderburn subalgebra
 * ⊕_{λ ∈ Λ²(n)} End(V_λ), where Λ²(n) is the two-row stratum
 * (def:two-row-stratum). It is idempotent and splits the canonical
 * Markov trace as
 *
 *   tr_M = tr_M ∘ π_{2-row}  +  tr_M ∘ (id − π_{2-row}).
 *
 * Split out of def:two-row-stratum (one definiendum per block).
 * Lean: HasTwoRowProjection class in QOU.BraidKnot.TwoRowStratum.
 */
export default definition({
  label: "def:two-row-projection",
  title:
    "Two-row projection $\\pi_{\\mathrm{2-row}}$ onto the two-row Wedderburn subalgebra",
  defines: ["two-row-projection"],
  uses: ["def:two-row-stratum", "prop:wedderburn-weight-canonical"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): from [Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$)](#prop:wedderburn-weight-canonical)" },
  ],
  lean: { ref: "qou:QOU.BraidKnot.TwoRowStratum.HasTwoRowProjection" },
  tags: [
    "wedderburn-decomposition",
    "su2-schur-weyl",
    "two-row",
    "projection",
  ],
});
