# From-scratch derivation infrastructure

> **DEPRECATED for production (2026-05-29, #1422 decision A').** The
> scripts in this directory compute $\tau_M$ on the **single-component
> free-proton braid** — *not* the 11-crossing canonical recipe that
> production (`markov_peel`, Hoefsmit, chi-cache, Habiro) uses.  Their
> values (e.g. $\tau_M(p_{\text{free}}, q_0) \approx 1.7339$) are
> legitimate Jones–Markov traces of *their own braid choice*; they
> should **not** be compared with the production
> $\tau_M(\beta_p, q_0) \approx 1.0653$ as if they were "different
> conventions of the same braid".  Kept on disk for pedagogy /
> historical reference; **not re-pursued**.
>
> See [`docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](../../../docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md)
> §"Resolution 2026-05-29" and
> `derivation_chain.py` (escalation block, RESOLVED).

Self-contained derivation of the categorical mass formula for atoms,
without any dependencies on the existing `folio-assistant/computations/`
infrastructure.

Every step is derived from the **algebraic axioms** and traced
explicitly:

1. **Hecke energy** — `def:hecke-mass-element` via braid generators with
   quadratic relation `σ_i² = (q-q⁻¹)σ_i + 1` on top of braid relations.

2. **Cat action of C on S** — left multiplication on `H_n(q)` viewed as
   the regular representation in `Mat_{[n]_q!}(ℚ(q))`.

3. **Frobenius pairing** — `⟨x, y⟩_τ := τ(xy)` with `τ` the Markov trace
   `tr_M`, derived from the Markov axioms (cyclic + factorisation).

4. **Non-abelian Stokes** — finite-slice multiplicative integral over
   the braid word, with depth = GB filtration max-grade. Each Hecke
   relation firing is logged with the resulting filtration drop.

5. **Wedderburn decomposition** — `H_n(q) ≅ ⊕_λ M_{d_λ}(ℚ(q))`
   constructed explicitly from the central idempotents `p_λ`.

6. **Schur-Weyl** — the irrep `V_λ` constructed explicitly as a
   sub-representation of `(ℚ(q)^N)^{⊗n}` cut out by `e_λ`.

7. **Finite Jones polynomial** — `J(L) = tr_M(T_w(β_L))` where
   `tr_M(T_w) = Σ_λ y_λ χ_λ(T_w)` with `y_λ` from the Wenzl bridge.

8. **Jet order + GB filtration** — every reduction step records the
   GB grade of source and target, building the spectral filtration.

## Outputs

Each derivation emits a witness with full step-by-step trace:
- input braid word
- per-step reduction log (which relation fired, source grade, target grade)
- GB normal form
- Wedderburn block coefficients
- per-block Markov trace contribution
- final categorical mass

## Files

- `hecke_step_by_step.py` — H_n(q) implementation with traced operations
- `h3_canonical_basis.py` — H_3 canonical-basis reduction
- `wedderburn_markov.py` — Wedderburn decomposition + Markov trace at H_3
- `wenzl_y_axiomatic.py` — Wenzl y_λ via Markov axioms
- `hoefsmit_general.py` — Hoefsmit seminormal σ_i^λ for general λ ⊢ n
- `derive_he3.py` — ³He at H_3 (SDP-canonical braid)
- `derive_t_h5.py` — tritium at H_5 (SDP-canonical braid)
