# q-NS Part A: the enstrophy order parameter cannot diverge inside the formalised q-NS context

Date: 2026-11-27. Bean `qou-innq` (wall, Part A). Lean:
`folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_enstrophy_order_parameter.lean`
(sorry-free; no empirical value in any proof). Owner rule (2026-11-27): only what is
formalised in QOU is used; no OpenAI-announced NS work.

## Statement under test

`conj:regularity-breakdown`, Part A: for suitable data,
`Ω(q) = sup_{t≥0} Σ_k [k]_q² |v̂_k(t)|² → +∞` as `q → 1⁺`. Until now Part A had no Lean
statement (`RegularityBreakdown` encodes Part B only).

## Result

The model is `QNsWellposednessContext`, the corpus's formalisation of
`thm:q-ns-wellposedness`, de-vacuified on 2026-11-23. Part A is settled for both layer
readings of "suitable data" (`def:qns-unit-layers`):

| Reading | Verdict | Lean |
|---|---|---|
| Data fixed in the **substrate** layer (amplitudes `a_k` independent of `q`) | **False.** `Ω(q)` is bounded on `(1, q₀]` whenever it is finite at one `q₀ > 1`. | `partA_fails_for_q_independent_data`, `omega_not_tendsto_atTop` |
| Data fixed in the **physical** layer | **True for a trivial reason.** `Ω_sub = Ω_phys/(q−1)²` diverges with `α = 2` from the unit conversion alone. | `physical_layer_conversion_diverges` |
| Data allowed to depend on `q` freely | **Empty.** Every nonnegative function of `q` is `Ω(q)` for some datum. | `omega_realises_any` |

The proof has three parts.

1. **Algebra (any ordered field).** `[n]_q = U_{n−1}((q+q⁻¹)/2)`, a Chebyshev
   polynomial (`qIntBal_eq_chebU`). For `s ≥ 2` the sequence `U` is nonnegative and
   nondecreasing in both `n` and `s`, and `q ↦ q + q⁻¹` is nondecreasing on `q ≥ 1`.
   So `[n]_q` is nondecreasing in `q` on `q > 1` (`qIntBal_mono`). The proof uses only
   induction and ring identities.
2. **The supremum over `t` is attained at `t = 0`.** The context's field
   `modal_inequality` gives `|v̂_k(t)| ≤ |v̂_k(0)| e^{−ν_q[k]_q² t}`
   (`q_ns_spectral_decay`, already proved). So the enstrophy never exceeds its initial
   value (`q_ns_enstrophy_isGreatest`), and `Ω(q) = Σ_k [k]_q² a_k²`.
3. **Monotone in `q`.** By step 1, `Ω(q) ≤ Ω(q₀)` for `1 < q ≤ q₀` (`omega_mono`).

**Non-vacuity.** `stokesContext` fills every field of the context, for every `q > 1`
and any amplitudes, using the linear Stokes flow `v̂_k(t) = a_k e^{−ν_q[k]_q² t}`.
`partA_fails_stokes` applies the negative result to that family. For the datum `δ_{k,1}`,
`Ω ≡ 1` (`omega_delta_one`).

## Scope (AGENTS.md (a)/(b))

This is a **(b) structural exclusion relative to `QNsWellposednessContext`**. The proved
invariant is the field `modal_inequality` together with `qIntBal_mono`. It is **not** an
exclusion for any q-NS dynamics with nonlinear mode transfer.

## Diagnosis

The real content is the diagnosis. `modal_inequality`, `d/dt|v̂_k| ≤ −ν_q[k]_q²|v̂_k|`, is
the modal law of the **linear** Stokes equation. Navier–Stokes nonlinearity moves energy
between modes (triads), so no single mode's amplitude is monotone in general. The
following all need that transfer:

- Part A itself;
- its heuristics, "loss of UV regularisation" and "the cascade becomes continuous";
- the numerically measured substrate-layer tail pile-up in `def:qns-unit-layers`. That
  measurement is empirical and is cited here only as a signal, never in a proof.

The context therefore does not distinguish Stokes from Navier–Stokes. Property 3 of
`thm:q-ns-wellposedness` (per-mode exponential decay) is the clause that makes Part A
false. As a claim about the nonlinear q-NS flow, it is itself an overstatement.

## Consequences and owner decisions

Part A as currently written cannot be both nontrivial and consistent with property 3 of
`thm:q-ns-wellposedness`. The owner's options are:

1. **Weaken property 3** to what the energy balance actually gives: total energy decay,
   with modal transfer allowed (a triad term in the modal law). Part A stays open in the
   substrate layer as a genuine Euler-endpoint enstrophy-growth question.
2. **Keep property 3 and withdraw Part A**, or restate it as a theorem in its negated,
   substrate-layer form.
3. **Restate Part A in the physical layer.** It is then a unit artifact (`α = 2`) and
   should be recorded as one, not as a conjecture.

Recommendation (judgement): option 1. Property 3 is the anomalous clause, and option 1
keeps the question Carl wants open.
