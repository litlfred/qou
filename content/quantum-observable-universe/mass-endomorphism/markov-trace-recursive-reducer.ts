import { proposition } from "../../schema/builders";

/**
 * Existence and termination of a recursive symbolic Markov-trace
 * reducer for arbitrary words in $H_n(q)$, building on the
 * Hecke-quadratic + Markov-axiom + cyclic-trace data.
 *
 * The algorithm:
 *
 *   1. Expand the input braid word β ∈ B_n into the canonical
 *      Hecke basis {T_w : w ∈ S_n} via iterated Hecke quadratic.
 *      (`gb_filtration_jet_tracker.HeckeElement`).
 *   2. For each basis element T_w, compute tr_M(T_w) by recursion
 *      on the Coxeter length ℓ(w):
 *      • base case: ℓ(w) = 0 ⇒ tr_M = 1.
 *      • if w doesn't use σ_{n-2} (the highest generator of H_n),
 *        truncate to S_{n-1} and recurse with smaller ambient
 *        algebra.
 *      • otherwise, find a rightmost occurrence of σ_{n-2} in a
 *        canonical reduced word, cyclically rotate, drop σ_{n-2}
 *        via the Markov axiom (gaining a factor of z), and reduce
 *        the rotated remainder back into the H_n basis. Each strip
 *        decreases ℓ(w) by exactly 1, so termination is guaranteed.
 *   3. Sum c_w · tr_M(T_w) over the basis expansion.
 *
 * Memoisation on `(perm, n)` makes repeated atom evaluations
 * fast: the basis of S_n has finitely many elements, each computed
 * once per ambient n.
 *
 * Establishes the **disjoint-product property** for tr_M on
 * commuting clusters in H_n: if α uses only generators σ_{i<k} and
 * β uses only σ_{j>k+1} (separated by an unused generator slot),
 * then tr_M(α ⊗ β) = tr_M(α) · tr_M(β). Verified empirically on the
 * deuteron's H_6 disjoint cluster σ₁⁷σ₂⁴ ⊕ σ₄⁶σ₅⁴σ₄⁻¹.
 */
export default proposition({
  label: "prop:markov-trace-recursive-reducer",
  title:
    "Existence of a recursive symbolic Markov-trace reducer for $H_n(q)$ with disjoint-product property",
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
  ],
  cites: ["jones1987", "kassel1995", "wenzl1988"],
  computation: {
    engine: "sympy",
    script:
      "computations/markov/markov_trace_recursive.py",
    witness: [
      "computations/markov/markov-trace-recursive.witness.json",
      "computations/markov/markov-trace-axiomatic-multi-atom.witness.json",
    ],
    status: "verified",
    requires: ["sympy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.markovTraceRecursiveReducer",
    validation: "not_checked",
  },
  tags: [
    "markov-trace",
    "axiomatic-reduction",
    "recursive-algorithm",
    "disjoint-product",
    "memoisation",
    "termination",
  ],
});
