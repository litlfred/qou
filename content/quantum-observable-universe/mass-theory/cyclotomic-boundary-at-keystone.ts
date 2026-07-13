import { conjecture } from "../../schema/builders";

/**
 * The Habiro-tail cyclotomic boundary sits at the keystone order n=5.
 *
 * The binding q-deformation of the na-Stokes period obeys
 *   S(n) = S(n-1) + [n-1]_q S(n-2) + D(n),   S(n) = Σ_{λ⊢n} dim_q(λ),
 * and the Habiro tail D(n) is cyclotomic (a product of cyclotomic
 * polynomials, times the universal (q-1)^2 double root and a q-monomial)
 * exactly for n ≤ 5, going genuinely non-cyclotomic from n = 6.
 *
 * The new observation: n ≤ 5 is EXACTLY the framework's {calibration
 * orders c=1,2,3 → n=2,3,4} ∪ {S₅ keystone n=5}, and the mechanism ties
 * to the merged McKay 2I↔Ê₈ value map (#3685): at n=5 the four bwS0
 * conjugation classes of S₅ carry dim_q equal to the E₈ Coxeter marks
 * [1]_q, [4]_q, [5]_q, [5]_q+1, because A₅ ≅ 2I/{±1} is icosahedral and
 * 2I ↔ Ê₈. A₅ is the LAST McKay-ADE alternating group (A₄↔Ê₆, A₅↔Ê₈,
 * A₆ not binary polyhedral); at n=6 the McKay-mark structure exits
 * (only 4/11 partitions have dim_q a single [m]_q, vs 7/7 at n=5) and
 * D(6) leaves the cyclotomic (Habiro) ring — where A₆ is also the unique
 * exceptional S₆ (the only symmetric group with a nontrivial outer
 * automorphism).
 *
 * Scope-(a) correlation; causation (does the A₅→A₆ McKay exit / S₆
 * anomaly force the boundary?) is OPEN and is the formalization target.
 * The D(m) arithmetic itself is the 2026-06-28 Stages 7-9 result (cited,
 * not re-derived); the McKay value map is #3685 (cited). No fit, no
 * wiring, no closure. Magnitudes not interpreted (numerology guard).
 */
export default conjecture({
  label: "conj:cyclotomic-boundary-at-keystone",
  title:
    "The Habiro-tail cyclotomic boundary sits at the keystone order: $D(n)$ is cyclotomic $\\iff n \\leq 5$",
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
    "prop:sw-period-residue-sum",
    "prop:calibration-cohomology-alignment",
  ],
  computation: {
    engine: "python",
    script: "computations/lever1_cyclotomic_boundary_keystone_conjecture.py",
    witness: "computations/lever1-cyclotomic-boundary-keystone-conjecture.witness.json",
    status: "verified",
  },
  tags: [
    "binding",
    "habiro-tail",
    "cyclotomic",
    "keystone",
    "s5-so3",
    "mckay",
    "e8",
    "open-conjecture",
  ],
});
