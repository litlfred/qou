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
    {
      kind: "note",
      body: "Computational provenance: the_canonical_closure_is_a_chain_of_torus_links_probe.py, the_curvature_floor_is_sharp_probe.py.",
    },
  ],
});
