import { prose } from "../../schema/builders";

export default prose({
  label: "sec:thurston-relaxation",
  uses: [
    "conj:algebraic-geometric-dilog-equivalence",
    "def:archimedean-realization-functor",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): This identification is asserted, not established: no block states it and no witness checks it, and clause (1) of the [algebraic--geometric dilogarithm conjecture](#conj:algebraic-geometric-dilog-equivalence) rests on it, so it carries that conjecture's tier." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): These roots are in bijection with the $n$ ideal tetrahedra of a hyperbolic triangulation of the $\\Phi_q$-piece $K_S$, the root of index $k$ labelling the tetrahedron whose shape parameter it seeds ([pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)(1))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The [Archimedean realization functor](#def:archimedean-realization-functor) acts as the explicit translator between the algebraic and geometric solvers." },
  ],
});
