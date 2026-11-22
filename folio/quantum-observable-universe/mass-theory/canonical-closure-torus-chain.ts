import { proposition } from "../../schema/builders";

/**
 * The canonical atomic word, once its averaged letters are resolved to a
 * crossing sign, is a chain form — each generator once, in order, as a single
 * power — so its closure is a linear connected sum of (2, odd)-torus knots
 * with one unknot, of bridge number exactly 2A+1, and Milnor's infimum of
 * total curvature over its isotopy class is 2π(2A+1).
 *
 * Exponent bookkeeping and the Seifert-form algebra are in
 * `lean/QOU/Mass/TorusKnotPages.lean` (sorry-free). The two topological
 * facts — composite closed braids, and removing a T(2,±1) band — and Milnor's
 * theorem are classical and cited; the chain form itself is verified exactly
 * for A ≤ 12 by `the_canonical_closure_is_a_chain_of_torus_links_probe.py`.
 */
export default proposition({
  label: "prop:canonical-closure-torus-chain",
  title:
    "The canonical closure is a chain of $(2,\\mathrm{odd})$-torus knots: bridge number $2A+1$ and total curvature $2\\pi(2A+1)$",
  lean: {
    ref: "qou:QOU.Mass.TorusKnotPages.curvature_floor",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "def:atomic-braid",
    "def:canonical-braid-interface-composition",
  ],
  cites: ["milnor1950", "birman1974"],
  tags: [
    "mass-theory",
    "knot-theory",
    "torus-knots",
    "bridge-number",
    "total-curvature",
    "fary-milnor",
    "lean-formalised",
    "draft",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## What is formalised, what is checked, what is cited\n\n`QOU.Mass.TorusKnotPages` carries the algebra: the Seifert form\nof $T(2,n)$ is unimodular for every odd $n$; the continuant of $V - X V^{\\mathsf T}$\nsatisfies $(X+1) D_{2g} = X^{2g+1} + 1$, so the Alexander polynomial is\n$(X^n+1)/(X+1)$ and divides $X^{2n}-1$; the floor $2A+1 \\le b \\le 3A$ is\nbookkeeping from $\\mu = A+1$ and $A$ knotted components.\nThe chain form and its exponents are verified exactly for $A \\le 12$, and the\nsymbolic predictions -- components, knot types, linking, and that $W'_A$ closes\nto the same link (Jones polynomial and per-component Jones) -- for $A \\le 4$,\nby `the_canonical_closure_is_a_chain_of_torus_links_probe.py`; the\ncomputational instance at $A \\le 6$ via Reidemeister simplification and\nVogel's algorithm is `the_curvature_floor_is_sharp_probe.py`. Not formalised:\nthe two topological facts above, Milnor's theorem, and the identification of\nthe components from their Jones polynomials." },
  ],
});
