import { remark } from "../../schema/builders";

/**
 * Research-notes remark: candidate closed forms for the
 * A-scaling of the LP-dual binding-energy shadow price y_0*(A, T_3).
 *
 * Empirical data (witness alpha-5-lp-dual-crystal, 2-row stratum,
 * ℓ=5):
 *
 *   q     D(A=2,|T_3|=0)   T,³He(A=3,|T_3|=1/2)   ratio T/D
 *   1.110     10.3125            570.68              55.34
 *   1.050      7.6912            247.93              32.24
 *   1.001      6.0301            127.69              21.18
 *
 * The ratio T/D depends on q non-trivially.  As q → 1⁺ the ratio
 * shrinks toward ~21; as q grows toward q_0 ≈ 1.11 it grows
 * toward ~55.  This is incompatible with a SIMPLE separable form
 *
 *   y_0*(A, |T_3|) ≟ g(q) · h(A, |T_3|)
 *
 * because the q-dependence of g(q) would have to multiply BOTH
 * D and T by the same factor — but the ratio changes with q.
 *
 * Better candidates (research directions):
 *
 *   (a) Partition-of-unity decomposition.  Write
 *       y_0*(A, |T_3|) = Σ_λ a_λ(A, |T_3|) · b_λ(q)
 *       summed over the active set (LP-dual support).  At q_0
 *       the active set is 3/4 for D and 4/5 for T,³He.  The
 *       q-dependent ratios then come from re-weighting the LP
 *       constraints differently across A's at different q.
 *
 *   (b) Wedderburn-block-resolved form.  Write
 *       y_0*(A, |T_3|) = Σ_{λ ∈ active(A,|T_3|)} u_λ*(A, |T_3|, q)
 *       where each u_λ* depends on the per-block Frobenius
 *       pairing (y_λ · χ^λ(β_K)).  The mirror-pair invariance
 *       T = ³He follows because their active sets are
 *       λ-conjugate under the Hopf antipode.
 *
 *   (c) q → 1 limit (classical Specht).  At q = 1 the q-numbers
 *       reduce to ordinary integers; the LP-dual y_0* should
 *       reduce to a Specht-dim-weighted sum that recovers the
 *       *classical* BW coefficients α_k.  Empirically the
 *       q → 1.001 numbers (D=6.03, T=127.69) suggest such a
 *       limit exists but with a non-trivial T/D ratio.
 *
 *   (d) Crystal limit q → 0.  This is the genuine Kashiwara
 *       crystal limit (NOT q → 1).  In that limit JM
 *       eigenvalues become integer content multiplicities; the
 *       LP becomes integer-programming over a Kashiwara crystal
 *       graph.  The probe sweeps q → 1⁺ but does NOT approach
 *       q → 0; that needs separate compute.  Open follow-up.
 *
 *   (e) Demazure sub-crystal selector.  PR #619 found that the
 *       categorical rule for λ*(Z, N) is "max y_λ · |χ^λ|" — not
 *       a pure structural property of λ.  This selector picks
 *       out a Demazure sub-crystal of the canonical basis.  The
 *       LP-dual u_λ* may decompose along Demazure components,
 *       yielding y_0*(A, |T_3|) as a sum of crystal-graph
 *       weights.
 *
 * Witness-able next probes:
 *   - q-sweep at q ∈ {q_0/2, q_0/4, …} to approach Kashiwara
 *     crystal q → 0 from above.
 *   - ⁴He at A=4, |T_3|=0 (n=12 sympy, slow).  Hypothesis:
 *     y_0*(⁴He) sits on the same |T_3|=0 branch as D (i.e.
 *     y_0*(⁴He)/y_0*(D) is q-rational, not isospin-asymmetric).
 *   - Compute the LP-dual on the SINGLE (3,3,1,1,1)-stratum
 *     (Demazure-sliced 2-row) to test (e).
 *
 * No closed form is asserted as proved.  This is a research-
 * notes remark consolidating the empirical structure and the
 * non-trivial q-dependence — to be cleared up by the next
 * round of probes.
 */
export default remark({
  label: "rem:lp-dual-scaling-conjecture",
  interprets: "prop:spin-involution-lp-dual-invariance",
  title:
    "Candidate closed forms for $y_0^*(A, |T_3|)$ — A-scaling research notes",
  uses: [
    "prop:spin-involution-lp-dual-invariance",
  ],
  tags: [
    "lp-duality",
    "shadow-price",
    "closed-form",
    "research-notes",
    "kashiwara-crystal",
    "demazure-subcrystal",
    "open-question",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/alpha/alpha_5_lp_dual_crystal.py",
    witness: "computations/alpha/alpha-5-lp-dual-crystal.witness.json",
    status: "verified",
  },
});
