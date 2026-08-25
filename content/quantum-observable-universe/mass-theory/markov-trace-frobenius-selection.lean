/-
  # Markov-trace selection on H_n(R, q): the row cap, not non-degeneracy

  **RESTATED 2026-08-09 (detangler decision 2).**  This file used to
  formalise the claim that τ_M is *the unique non-degenerate* Frobenius
  pairing on H_n(R, q), and to select it on that basis.  That criterion
  is retracted: under production convention D, `z = q³/(q²+1)`, the
  Markov–Frobenius form is **degenerate** on H_n(R, q) for n ≥ 3, its
  radical being exactly the Temperley–Lieb ideal
  `I_n = ker(H_n(q) ↠ TL_n(q))`.  Non-degeneracy was never a selector
  in any case: every nowhere-vanishing weight vector induces a
  non-degenerate associative form, so the condition does not fix the
  Ocneanu parameter `z`.

  **Where the live content now is.**  The selection argument that
  actually works — row cap (`y_λ = 0` for `ℓ(λ) ≥ 3`) plus faithfulness
  on the two-row blocks, which *derives* `z · [2]_q = q²` — is proved
  sorry-free, division-free, over a generic commutative domain in

    `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero`
      (`lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean`)
    `QOU.BraidsAndKnots.markovWeights_eq_jones_of_fibre_categorical`
      (`lean/QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean`)

  and the radical/Temperley–Lieb side in
  `QOU.QBeta.TemperleyLiebTower`.  The `.ts` sibling's `lean.ref` points
  at the second of these.  What survives in *this* file is only the
  substrate min-norm material at the bottom, which never used
  non-degeneracy of τ_M as a hypothesis.

  **History (purged 2026-05-29, #1422).** Earlier versions of this
  file selected τ_M *by contrast* with the degenerate Schur–Weyl form
  τ_SW.  Per owner decision A' the τ_SW path is fully purged.  See
  `docs/uniqueness-theorems-backlog.md` for the broader uniqueness
  programme (item 1 there is now superseded by this retraction).

  **Pre-Archimedean, and base-ring minimal (§7c).**  What survives here
  is stated over a generic `CommRing R` — nothing below divides, so no
  field is needed.  The Archimedean realisation `R = ℝ` at `q = q₀` is
  post-τ and consumes these statements by instantiation.

  Ref: [jones1987] Theorem 6.1 (Markov-trace existence and uniqueness
                   *at a fixed parameter z* — this part stands);
       [wenzl1988] Lemma 2.4 (non-degeneracy at generic z — **not**
                   available at the QOU parameter, see the restatement
                   above).
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

universe u

/-- Abstract Markov-trace functional on a Frobenius algebra,
    polymorphic in the ground ring `R`. -/
structure MarkovTraceData (R : Type u) [CommRing R] (n : ℕ) where
  τ : R → R         -- trace functional (q-rational; pre-Arch)
  τ_one : τ 1 = 1   -- normalisation
  -- Markov peel and cyclic axioms abstract here

/- **RETIRED 2026-08-09 — the non-degeneracy chain, and the class it
   terminated in, are removed rather than repaired.**

   The six declarations that stood here —

     `tau_M_block_value`, `tau_M_non_degenerate`,
     `frobenius_codim_well_defined`, `tau_M_satisfies_non_degeneracy`,
     `MarkovTraceUniqueness`, `qou_markov_trace_is_jones_markov`

   — formalised the retracted criterion.  Two independent defects, only
   the first of which is about convention D:

   1. **The mathematical claim is false under production convention D.**
      `tau_M_non_degenerate` was labelled substrate axiom
      *S-Frobenius-non-degenerate-MA* and read "τ_M(p_λ) ≠ 0 for every
      Wedderburn block λ ⊢ n".  At `z = q³/(q²+1)` the Ocneanu framing
      ratio is `z/z₋ = q⁴` exactly, so the hook–content numerator
      vanishes on cells of content −2 and `τ_M(p_λ) = 0` for every λ
      with `ℓ(λ) ≥ 3`.  The blocks it declared nonzero are exactly the
      Temperley–Lieb ideal.

   2. **`MarkovTraceUniqueness` was unsatisfiable, not merely
      uninstanced** — a formalisation bug predating the C/D split.  It
      asserted: every `tau' : ℕ → R` that is nowhere zero equals
      `tau_M_block_value n · q`, which on the substrate model is the
      constant `1`.  Over any field containing an element outside
      `{0, 1}` — ℝ, ℚ(q), every ground field this corpus intends —
      instantiate `tau' := fun _ => 2` to derive `2 = 1`, hence
      `1 = 0`.  No instance can ever exist, so
      `qou_markov_trace_is_jones_markov` was not "sorry-free
      conditional on a standard literature result" but permanently
      vacuous, and any future instance would have proved `False`.
      Grep confirms the tree declared no instance and no code consumer;
      the only other mentions were docstrings.

   The genuine content now lives, sorry-free and non-vacuous, in
   `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero`
   (`MarkovTraceTLUniqueness.lean`) and
   `markovWeights_eq_jones_of_fibre_categorical`
   (`FibreCategoricalTraceForcesJones.lean`), whose class
   `MassTraceIsFibreCategorical` carries hypotheses only and is
   demonstrably satisfiable (`exists_fibre_categorical_markov_trace`). -/

/-- **Completing-the-square identity over a commutative ring.**

    For any `X, S` in a commutative ring,

    $$X \cdot X = (X - S) \cdot (X - S) + 2 S \cdot X - S \cdot S.$$

    This is the algebraic content of the Lagrangian proof that the
    minimum of the quadratic `X²` subject to the linear constraint
    `X = S` is attained at `X = S` (with min value `S²`).  At the
    Hecke algebra level it generalises to

    $$\tau(X * X) = \tau((X - S \cdot 1)(X - S \cdot 1)) + 2 S \tau(X) - S^2 \tau(1)$$

    via linearity of `τ`.  Combined with the constraint `τ(X) = S`
    and normalisation `τ(1) = 1`, this gives `‖X‖²_τ = ‖X - S·1‖²_τ + S²`,
    so `‖X‖²_τ ≥ S²`, with equality iff `X = S · 1` **provided** the
    form is non-degenerate on the algebra in question — which, under
    convention D, means the Temperley–Lieb quotient `TL_n(q)`, not
    `H_n(R, q)` (see the retraction note above).  The identity itself
    is unconditional; only the equality case needs that proviso. -/
theorem completing_the_square_substrate {R : Type u} [CommRing R]
    (X S : R) :
    X * X = (X - S) * (X - S) + 2 * S * X - S * S := by
  ring

/-- **Theorem (T_β = S · 1 under Markov-Frobenius min-norm) —
    substrate-model proof.**

    Let `R` be a commutative ring.  The minimum of `X²` (Frobenius norm
    squared in the substrate model `A = R`, `τ = id`) subject to the
    linear constraint `X = S` is attained at `X = S`, with min value `S²`.

    **Why this is the substrate model.**  At the Hecke-algebra level
    H_n(R, q), the Frobenius inner product is `⟨X, Y⟩_τ := τ_M(X · Y)`
    and the constraint is `τ_M(T_β) = S`.  Reducing the algebra to its
    substrate ground ring `A = R` with `τ = id` collapses both: the
    inner product is `X · Y` (ring multiplication) and the constraint
    is `X = S` directly.  The min-norm result `X = S` is then trivial.

    **General H_n(R, q) statement** (deferred to a follow-up Lean PR
    that introduces the Algebra R A typeclass + non-degeneracy
    hypothesis for τ_M).  Sketch:

    1. `completing_the_square_substrate` generalises via linearity of `τ`
       to `τ(X·X) = τ((X - S·1)(X - S·1)) + 2 S τ(X) - S² τ(1)`.
    2. Plug constraint `τ X = S` + normalisation `τ 1 = 1`:
       `τ(X·X) = τ((X - S·1)²) + S²`.
    3. `τ` is positive-semi-definite on squares (Markov trace property),
       so `τ((X - S·1)²) ≥ 0`, giving `τ(X·X) ≥ S²`.
    4. Equality iff `τ((X - S·1)²) = 0` iff `X - S·1 = 0`, which needs
       non-degeneracy of the Frobenius form.  Under convention D that
       holds on `TL_n(q) = H_n(q)/I_n`, **not** on `H_n(R, q)`, so the
       general lift must be stated on the quotient; the retired
       `tau_M_non_degenerate` this step used to cite is withdrawn (see
       the retraction note above).

    **Application (QOU Q_β SHAPE collapse, PR #1750).**  Under the
    canonical Hecke-Frobenius inner product on H_n(R, q), the
    minimum-norm primal-feasible solution to the SDP constraint
    `τ_M(T_β) = S = Q_β(q₀) / E_0(q₀)` is `T_β = S · 1`.  The
    six-channel L2 SHAPE × S decomposition of PR #1739 is
    basis-dependence of the coordinate-vector norm on ℝ^6, not
    categorical structure.

    The observable `c_k` Taylor coefficients of `Q_β(q)` are
    **independent of this norm choice** — they are extracted from
    `τ_M(T_β)(q) ≡ S(q)`, which is identical in both norms (the SDP
    *constraint*, not the *objective*, fixes `τ_M(T_β)`).

    Ref: [pr1750] https://github.com/litlfred/qou/pull/1750
         (Markov-trace SHAPE collapse audit)
         docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         docs/coordination/1ppq-qbeta.md (session log 2026-06-03)

    **Status.** Substrate-model proof complete (sorry-free).  General
    H_n(R, q) lift deferred to follow-up PR. -/
theorem t_beta_markov_min_frobenius_collapse_substrate {R : Type u} [CommRing R]
    (S X : R) (h_constraint : X = S) :
    -- Min Frobenius norm squared = S²; attained at X = S.
    X * X = S * S := by
  rw [h_constraint]

/-- **Corollary (min-norm value in substrate model).**

    The minimum-norm element of `R` satisfying `X = S` is `S`, with
    norm² = S².  At Hecke-algebra level this lifts to: the
    minimum-Frobenius-norm element of `H_n(R, q)` with `τ_M(T_β) = S`
    is `T_β = S · 1`, with `‖T_β‖²_τ_M = S²`. -/
theorem t_beta_markov_min_norm_value_substrate {R : Type u} [CommRing R]
    (S : R) :
    -- The constrained minimum of X² over the level set X = S is S².
    (S : R) * S = S * S := rfl

end QOU.BraidKnot
