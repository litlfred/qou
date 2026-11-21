import { remark } from "../../schema/builders";

/**
 * Scope remark for prop:sym2-adjoint-traceless-spin-two: the spin-2 summand
 * of Sym²(V₁) is spin for the gauge group Aut⊗(τ) ≅ SU(2), not for a
 * rotation or Lorentz group of spacetime. This is why the result is not
 * stated as a proposition about gravity. The remark carries no mathematics
 * of its own; the result and its Lean reference live in the proposition.
 */
export default remark({
  label: "rem:sym2-adjoint-spin-two-gauge-not-lorentz",
  title:
    "The spin-$2$ summand of $\\mathrm{Sym}^2(V_1)$ is gauge spin, not spacetime spin",
  interprets: "prop:sym2-adjoint-traceless-spin-two",
  uses: [
    "prop:sym2-adjoint-traceless-spin-two",
    "thm:su2-emergence",
    "prop:spin-labels",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "The absence claim (no proved statement identifies $\\mathrm{Aut}^{\\otimes}(\\tau)$ with a spacetime rotation or Lorentz group) was checked by grepping the paper's `.md` blocks for rotation, Lorentz and $\\mathrm{SO}(3,1)$; the only hit relating spatial $\\mathfrak{so}(3)$ to the adjoint is the prose `sec:archimedean-preamble`.",
    },
  ],
  tags: ["spin", "gauge-group", "graviton", "symmetric-square", "scope"],
});
