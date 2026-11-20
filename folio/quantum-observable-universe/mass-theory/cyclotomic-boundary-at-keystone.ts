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
 * The alignment: n ≤ 5 is EXACTLY the framework's {calibration orders
 * c=1,2,3 → n=2,3,4} ∪ {S₅ keystone n=5}.
 *
 * The ARITHMETIC mechanism (established): S(n)|_{q=1} = Σ_λ f^λ = I(n),
 * the involution/telephone numbers (A000085; RSK), so S(n) is the
 * q-involution / Rogers-Szegő / q-Hermite moment and D(n) is the deviation
 * of its q-lifted 3-term recurrence. Prior analysis (q-involution kernel
 * 2026-06-27 + Habiro-tail Stages 7-9, 2026-06-28) establishes the tail:
 * (q-1)^2 double root × a bar-even cofactor, cyclotomic through n=5,
 * genuinely non-cyclotomic + NON-q-HOLONOMIC from n=6. That is a property
 * of the ALTERNATING-SUM cancellation, not of any individual dim_q.
 *
 * CORRECTION (this PR): every dim_q(λ) = [n]_q!/∏[h]_q is a product of
 * cyclotomics for EVERY n, so single-[m]_q-vs-compound does NOT locate the
 * boundary (a product of several cyclotomics is still cyclotomic). The
 * McKay 2I↔Ê₈ value map (#3685) — at n=5 the four bwS0 classes carry the
 * E₈ marks [1]_q,[4]_q,[5]_q,[5]_q+1 (A₅ ≅ 2I/{±1} icosahedral, A₅ the
 * last McKay-ADE alt. group, A₆=PSL(2,9) non-McKay) — is a true rep-theory
 * COINCIDENCE OF ORDERS, but it does NOT act through cyclotomic-purity of
 * the dims and does not supply the arithmetic mechanism. (Prior wording
 * "4/11 single [m]_q vs 7/7 ⟹ leaves the ring" conflated single-[m]_q
 * with cyclotomic; corrected.)
 *
 * Scope-(a) correlation at 3 tiers (arithmetic / alignment / rep-theory);
 * causation OPEN. The n≥6 non-cyclotomicity is VERIFIED THROUGH n=11, NOT
 * proved for all n (the cofactor's non-q-holonomic degree growth is the
 * structural reason, not yet a proof). No fit, no wiring, no closure.
 * Magnitudes not interpreted (numerology guard).
 */
export default conjecture({
  label: "conj:cyclotomic-boundary-at-keystone",
  title:
    "The Habiro-tail cyclotomic boundary sits at the quintic order: $D(n)$ is cyclotomic $\\iff n \\leq 5$",
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
    "prop:sw-period-residue-sum",
    "conj:calibration-cohomology-alignment",
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
