import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:braid-fluid",
  title: "Braid--fluid correspondence: from categorical braiding to vortex dynamics",
  uses: [
    // Yang-Baxter, invoked to enforce Reidemeister III so three-vortex
    // braiding is path-independent.
    "prop:r-matrix-braiding-structure",
    "rem:madelung-fluid",
    "sec:webster-inner-product",
    // J_L(q), which this block reads as the topological helicity.
    "thm:jones-markov-trace",
    // The closure that turns the tangle's word into J_L.
    "prop:closure-unseen-subword",
  ],
  cites: [
    "moffatt1969",
    "birman-williams1983",
    "ghys2007",
    "garside1969",
    "dehornoy2015",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "**Hydrodynamic helicity, template reduction, and Garside stepping provenance.** (1) Moffatt (1969, \u00a72--3, eq. (3.6)) proves that for thin knotted/linked vortex filaments in inviscid barotropic flow, $H = \\int v \\cdot \\omega\\,dV = \\sum_{i,j} \\alpha_{ij}\\,\\kappa_i \\kappa_j$ reduces to Gauss linking numbers weighted by circulations, which vanishes on unlinked knots with zero framing and cannot separate chiral mirrors or distinct unframed knot types of equal writhe; the Markov trace $J_L(q)$ refines $H$ at higher Vassiliev orders. (2) Birman and Williams (1983, \u00a72--4) and Ghys (2007, \u00a73.1--3.5) establish that periodic orbits of three-dimensional hyperbolic/Anosov flows (including geodesic flow on $\\mathrm{UT}(\\mathrm{PSL}_2(\\mathbb{Z})\\backslash\\mathbb{H})$) collapse onto branched $2$-manifold templates carrying positive-braid words. (3) Garside (1969, \u00a72, Theorem 4) and Dehornoy, Digne, Godelle, Krammer, and Michel (2015, Ch. II, Proposition 4.8) supply the canonical positive-monoid greedy normal form $\\Delta^k s_1 \\cdots s_r$ for stepping along template words. **Claim boundary:** template reduction applies to periodic orbits of hyperbolic/template-admitting $3$-flows, not arbitrary viscous time-evolutions with vortex reconnection.",
    },
  ],
  tags: ["braid-group", "fluid-dynamics", "arnold", "vortex", "correspondence"],
});
