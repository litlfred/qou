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
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): the restricted axiom set (stripping, stability and cyclicity on words of H_n, plus the Hecke quadratic, braid and far-commutation relations) is the one the Lean formalisation uses." },
    { kind: "status", date: "2026-11-21", body: "The general disjoint-product law is now proved from the restricted axioms (Lean `QOU.BraidKnot.markovTrace_disjointProduct`, sorry-free, axioms propext/Classical.choice/Quot.sound). The proof is Ocneanu's reduction, `HeckeRel.reduce`: a function on positive words that satisfies the in-context Hecke, braid and far-commutation relations and vanishes on words using the top generator at most once vanishes everywhere. The Lean form has the two clusters sharing one strand (connected sum); the split case in the statement additionally needs shift invariance of the trace, which is not formalised. Thread N2 Lean foundations." },
    { kind: "status", date: "2026-11-21", body: "`lean.ref` now points at `markovTrace_disjointProduct` in this block's own `.lean` sibling. It used to point at the library item `QOU.BraidKnot.markovTraceRecursiveReducer`, which only returned a class field that already contained the whole claim (termination, correctness and the product law). That file is removed. What Lean covers here: the disjoint-product law, proved. Not covered: termination of the actual reducer (the `_terminates` lemma is satisfied by a constant tracer and says nothing about `markov_trace_recursive.py`), the `O(ℓ(β)·n!)` bound, and correctness of its output. Bean qou-tmmt." },
  ],
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
    // markov-trace-axiomatic-multi-atom.witness.json was declared here too,
    // and disagreed with the one above by 17%.  It is the output of a
    // DIFFERENT script (markov_trace_axiomatic_multi_atom.py, not this
    // block's declared `script`), it has not been regenerated since the
    // Markov parameter moved to z = q^3/(q^2+1), and its own
    // `convention_status` field reads DEPRECATED_NON_CANONICAL — "DO NOT use
    // for mass predictions".  A block citing a witness that disowns itself
    // is how the convention-C values reached this proposition's table.
    // Dropped as backing; the file stays in the tree as a record.
    witness: [
      "computations/markov/markov-trace-recursive.witness.json",
    ],
    status: "verified",
    requires: ["sympy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.markovTrace_disjointProduct",
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
