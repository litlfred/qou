# α_EM two-loop coefficient: the skein gives `−h²·H`, and no ζ(3) (2026-11-27)

Bean `qou-l4t2` (parent `qou-3l2l`; swarm epic `qou-s028`). Mathematics only: no
measured value enters any statement below. Lean:
[`QOU/MassTheory/EmVertexPairScalarChain.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmVertexPairScalarChain.lean)
(lean-direct exit 0; axioms `propext`, `Quot.sound`, `Classical.choice` only; no `sorry`).

## Question

The bean asks for the order-`α²` coefficient of `1/α_EM` in closed form, in
Bloch-`B₃` / `ζ(3)` terms. The 2026-11-22 review left one pure-math core that is
workable under `qou-aemx` (canonical form open): *for each labelled arm, decide
whether its second-order coefficient lies in the ℚ-span of `{1, π², π² log 2, ζ(3)}`*.
This note answers that for the part of the Form B arm that comes from the vertex
algebra.

## Result

Convention D fixes every Hecke generator by `σ² = hσ + 1`, `h = q − q⁻¹`.

1. **The skein is a scalar** (`skein_scalar`). `σ − σ⁻¹ = h·1` in any algebra over the
   coefficient ring, noncommutative included. This was known in the commutative
   setting (`hecke_skein_bar_contraction`); the new statement holds for any
   generator `σᵢ` of `H_n`, whatever strand pair it acts on.
2. **Every chirality-summed vertex pair is `−h²`** (`vertexPair_eq_neg_hsq`). The
   four-history sum `Σ (−ε₁ε₂) x^{ε₁} y^{ε₂}` equals `−(x − x⁻¹)(y − y⁻¹)` as a pure
   ring identity (`four_topology_eq_neg_skein_product`), so at any two generators it
   is `−h²`. The same-position and cross-position identities of
   `EmFermionLoopFourTopology` are the cases `y = x` and `y = σ'`.
3. **Chains and moments** (`vertexPair_chain`, `moment_vertexPair_chain`). A product
   of `k` vertex pairs, at any positions, is `(−h²)^k`. Under any linear moment `m`
   with `m(1) = 1` its moment is `(−h²)^k`; the tadpole `m(σ)` and every other moment
   drop out.
4. **Two-loop coefficient** (`skeinChain_two_loop_coeff`,
   `formB_is_skein_two_loop`). In `Π(α) = Hα(1 + N₁(−h²)α + N₂h⁴α² + …)` the `α²`
   coefficient is `−N₁h²H`. With `N₁ = 1` this is exactly Form B's `−Hh²`.

**Consequence.** Every coefficient the chirality-summed Hecke skein contributes lies
in `ℤ[h]·H = ℤ[q, q⁻¹]·[2]_q/(8π)`. A trilogarithm value `ζ(3) − Li₃(q⁻²)` cannot
come from the vertex algebra. So, for Form B, the extra term `c₂` of the
pre-registration (`computations/alpha/alpha_em_two_loop_bloch_schwinger_preregistration.md`)
is **zero from the algebra**: the derived two-loop slot is Form B's own `−Hh²`.

Scope (per AGENTS.md §"Before declaring refuted"): this is a **structural exclusion
of ζ(3) from the vertex algebra only**, cited invariant `skein_scalar`. It does *not*
exclude a `B₃` term from a two-loop **measure** (a period integral on Bring's
surface), which the corpus does not define. Candidate `C1` stays a labelled
pre-registered arm; it is not derived by this note and not refuted by it.

## What is still open (each a choice, not derived here)

- **`N₁`, the number of two-loop placements.** Same-position and cross-position
  pairs each give `−h²`. Form B uses `N₁ = 1`. If both placements count, `N₁ = 2`
  (and QED's two-loop vacuum polarization has three diagrams). The algebra does not
  fix `N₁`; a diagram count on the `EmFermionLoop` would.
- **Vertex normalization (`§3b-cond`).** `S = σ − σ⁻¹` gives `−h²`; `S/2` gives
  `−h²/4`. Unchanged by this note.
- **A two-loop measure.** Form B carries one `1/(8π)` at both orders. A second loop
  with its own period would be the only place for a weight-3 value.

## Comparison (prose only; not in any proof)

From the 2026-11-24 witness, `C0` (`c₂ = 0`, i.e. this derived value) and `C1`
(Bloch-`B₃`) differ by 0.34 ppb in `1/α`. The 2026-11-27 κ audit records that the
proton/muon pin tension (`qou-2002`) moves every arm by about 80 ppb, so no
α_EM residual below about 80 ppb is meaningful yet. The two arms cannot be told
apart by comparison today, and `qou-aemx` forbids choosing by residual anyway.
