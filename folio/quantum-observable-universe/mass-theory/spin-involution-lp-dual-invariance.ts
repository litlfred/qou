import { proposition } from "../../schema/builders";

/**
 * Generic spin / duality / LP-dual invariance.
 *
 * MATHEMATICAL DEFINITION OF SPIN.
 *
 *   A *spin involution* on a Frobenius algebra (A, τ) over a
 *   commutative ring R is an R-linear involutive map σ: A → A
 *   such that:
 *     (i)   σ ∘ σ = id (involution),
 *     (ii)  σ(ab) = σ(b) σ(a) for all a, b ∈ A
 *           (anti-multiplicative; *-anti-homomorphism),
 *     (iii) τ ∘ σ = τ (the trace is σ-invariant).
 *
 *   The Z/2 grading of A by σ-eigenvalue ±1 is the *spin
 *   grading*; the two-element group ⟨σ⟩ is the *spin group*.
 *   A σ-eigenvector with eigenvalue +1 is called *self-conjugate*
 *   or a *spin singlet*.
 *
 * QOU INSTANCE.
 *
 *   For A = H_n(R, q) (Iwahori–Hecke algebra) and τ = Markov
 *   trace, the Hopf antipode S satisfies (i)–(iii) and is the
 *   QOU spin involution.  S acts on Wedderburn blocks as
 *   V_λ ↔ V_{λ^T} (transpose partition).  The σ-fixed
 *   elements are isospin singlets; σ-doublets {λ, λ^T} with
 *   λ ≠ λ^T are isospin pairs.  T_3 = (signature under σ)/2.
 *
 *   Under S, the per-atom canonical braid recipe satisfies
 *   S(β_K(Z, N)) ~ β_K(N, Z) (Markov-conjugate), so the QOU
 *   spin involution implements the Z ↔ N swap on atomic
 *   braids — in physics, exactly the isospin involution
 *   acting on nucleons (proton ↔ neutron).
 *
 * THE THEOREM.
 *
 *   Let (A, τ) be a Frobenius algebra with spin involution σ.
 *   Let c ∈ A be σ-invariant: σ(c) = c.  Let Σ be a σ-stable
 *   set of channels (Wedderburn idempotent labels).  Then for
 *   every input element β ∈ A, the optimal LP-dual variable
 *   y_0*(β) of the operator-selection LP
 *
 *     min  τ(c · x)
 *     s.t. τ(1 · x)        = n_target(β),
 *          τ(π_λ · x) ≥ 0  ∀ λ ∈ Σ
 *
 *   is invariant under σ:
 *
 *     y_0*(σ(β)*) = y_0*(β),   given n_target(σ(β)*) = n_target(β).
 *
 *   In particular, β and σ(β) (and any pair Markov-conjugate
 *   to σ(β)) produce the same shadow price.
 *
 * COROLLARY (QOU isospin invariance).
 *
 *   For mirror nuclei (β_K(Z, N), β_K(N, Z)) — Markov-conjugate
 *   under the QOU spin involution S — the LP-dual binding-
 *   energy shadow price is exactly equal:
 *
 *     y_0*(Z, N) = y_0*(N, Z).
 *
 *   This is the rigorous version of the empirical finding
 *   y_0*(T) = y_0*(³He) tabulated in
 *   `rem:lp-dual-isospin-invariance`.
 *
 * The proof is short (5 steps); see the .md.  Lean stub
 * formalises the generic spin-involution framework + the
 * σ-invariance argument.
 */
export default proposition({
  label: "prop:spin-involution-lp-dual-invariance",
  title:
    "Spin involutions on Frobenius algebras leave the LP-dual shadow price invariant: $\\sigma(c) = c \\Rightarrow y_0^*(\\sigma(\\beta)^*) = y_0^*(\\beta)$",
  lean: {
    ref: "qou:QOU.BraidKnot.SpinInvolutionLPDualInvariance",
    validation: "not_checked",
  },
  uses: ["prop:jucys-murphy-central-elements-qou", "def:spin-involution"],
  cites: ["kassel1995", "murphy1992"],
  tags: [
    "lp-duality",
    "spin-involution",
    "isospin-invariance",
    "frobenius-algebra",
    "hopf-antipode",
    "shadow-price",
    "structural-theorem",
    "generic-framework",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body: "Conclusion corrected on owner ruling: the LP is related to the LP for $\\sigma(\\beta)^*$, not $\\sigma(\\beta)$, because anti-multiplicativity gives $\\sigma(\\beta^*\\beta) = \\sigma(\\beta)\\sigma(\\beta)^*$. The hypotheses that $\\sigma$ commutes with $*$ and that $n_{\\mathrm{target}}$ agrees on $\\beta$ and $\\sigma(\\beta)^*$ are now stated. The Lean sibling proves Steps 1 and 3 only.",
    },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The QOU-instance corollary (mirror nuclei have equal LP-dual shadow prices) is withdrawn as unproved. Its proof assumed the Markov trace is invariant under the antipode $\\sigma_i \\mapsto \\sigma_i^{-1}$; under convention D, $\\tau(\\sigma_i) = q^3/(q^2+1)$ and $\\tau(\\sigma_i^{-1}) = 1/(q(q^2+1))$ (0.6127 vs 0.4036 at $q_0$), so the hypothesis $\\tau\\circ\\sigma = \\tau$ fails. The equality $y_0^*(T) = y_0^*({}^3\\mathrm{He})$ recorded in the witness is therefore unexplained by this proposition. The pair-knot corollary's conclusion still holds, by shift-invariance of the trace rather than by $S$. The generic theorem is unaffected.",
    },
  ],
});
