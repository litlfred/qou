import { prose } from "../../schema/builders";

export default prose({ label: "sec:mobius-energy-intro",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): In the classical limit $q \\to 1$, the Frobenius pairing degenerates onto the $\\mathrm{SU}(2)$ Killing form with a repulsive $1/r^2$ kernel ([Lemma](#lem:mobius-energy-frobenius-kernel)), recovering the Freedman–He–Wang Möbius energy up to a topological constant ([Proposition](#prop:mobius-energy)). Away from the symmetric point ($q \\neq 1$), non-cocommutativity of the Hopf coproduct regularizes the short-distance singularity at the scale $\\hbar_q = 1 - q^{-1}$ ([Lemma](#lem:nsi-q-deformed-kernel)), obstructing self-intersection of distinct strand segments inside the fibre $\\tau(A)$ ([Corollary](#cor:non-self-intersection))." },
  ],
});
