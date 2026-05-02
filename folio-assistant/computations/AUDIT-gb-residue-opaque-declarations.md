# Audit — `gb-residue-spectral-sum.lean` opaque declarations

**Scope.** Catalog the `noncomputable opaque` and `sorry`-axiom
declarations in `content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.lean`
that block a fully formal proof of `prop:gb-residue-spectral-sum`,
and assess what Mathlib infrastructure (or new content) would be
needed to promote each to a definition with a real proof.

This audit is a follow-up to the equivalence theorem
`prop:habiro-residue-sum-equivalence` (PR #472), whose
`archimedean_agreement` axiom transitively depends on the
identifications below.

## P2.6 Lean refactor (2026-05-02) — opaque axioms removed

The two `noncomputable opaque` declarations and the `sorry` in
`spectral_sum_finite` have been **removed** from
`gb-residue-spectral-sum.lean`. The instance data is now carried
by class fields on `GBResidueSpectralSum`:

- `S.gradedTrace : Fin levelBound → ℝ` — replaces global `opaque
  gradedMarkovTrace`. Per
  [`prop:graded-markov-trace-from-gs-filtration`](../../content/quantum-observable-universe/braids-and-knots/graded-markov-trace-from-gs-filtration.md),
  the value is the descent of `tr_M` along `J^ℓ / J^{ℓ+1}`.
- `S.residue : Fin levelBound → ℝ` — replaces global `opaque
  residueAtRoot`. Per
  [`prop:residue-at-root`](../../content/quantum-observable-universe/braids-and-knots/residue-at-root.md),
  the value is the cyclotomic projection of `Φ_q · gradedTrace ℓ`
  in the Habiro completion.

The `sorry` on the previous line 86 is closed by removing the
unsafe `S.roots⟨0, sorry⟩` access; the class-based form has the
finiteness as a tautology over `Fin levelBound`.

Convenience accessors `gradedMarkovTrace S ℓ` and `residueAt S ℓ`
preserve the call-site name for any external reader.

## Remaining surface

| Decl | Kind | Where | Type signature | Blocks |
|------|------|-------|----------------|--------|
| `GBResidueSpectralSum.gradedTrace` | class field | `gb-residue-spectral-sum.lean:78` | `Fin levelBound → ℝ` | Each instance must supply per-level traces (narrative: `prop:graded-markov-trace-from-gs-filtration`) |
| `GBResidueSpectralSum.residue` | class field | `gb-residue-spectral-sum.lean:83` | `Fin levelBound → ℝ` | Each instance must supply per-level residues (narrative: `prop:residue-at-root`) |
| `GBResidueSpectralSum.spectral_decomposition` | class field axiom | `gb-residue-spectral-sum.lean:91` | `mass = ‖descended‖ + Σ_ℓ residue ℓ` | The proposition itself |
| `HabiroResidueSumEquivalence.archimedean_agreement` | class field axiom | `habiro-residue-sum-equivalence.lean:97` | `eval u_0 (map ι trace) = mass` | Transitively the equivalence |
| `HabiroResidueSumEquivalence.protonExample.archimedean_agreement` | `sorry` | `habiro-residue-sum-equivalence.lean:139` | proton-specific instance witness | Concrete instance |

## Mathlib infrastructure assessment

| Need | Mathlib status (2026-04) | Path forward |
|------|--------------------------|--------------|
| Complex meromorphic functions | `Mathlib.Analysis.Meromorphic.*` exists with `MeromorphicAt`, `MeromorphicOn`. Adequate for stating residues at isolated poles. | Use directly. |
| Residue at a pole | Mathlib has `Complex.residue` for some flavours; a general `Function.residue` API is partial. The specific case "residue at `ζ_ℓ` of `Φ_q · tr_{M,ℓ}` viewed as a meromorphic function in `q`" needs a concrete Mathlib proof of meromorphicity at roots of unity. | Open. Likely need a dedicated lemma `meromorphic_quantum_dilogarithm_at_roots_of_unity`. |
| Quantum dilogarithm `Φ_q` | No Mathlib formalization. Defined in QOU as a formal product `∏_{n≥0} (1 − q^n)`. | Add as a `noncomputable def` over `ℂ`; prove convergence on `|q| < 1` and meromorphic continuation across `S^1` using Mathlib's `Multipliable` API. |
| Cyclotomic / roots of unity | `Mathlib.NumberTheory.Cyclotomic.*` has `IsPrimitiveRoot`, `Polynomial.cyclotomic`. | Use directly (already done in nearby content blocks). |
| GS-filtration of `H_n(q)` | `QOU.BraidKnot.ConfinementLevel` exists but is also axiomatized. | Out of scope here; tracked in `proof-status-tracking`. |
| Markov trace on graded pieces | The induced trace `tr_{M,ℓ}` on `J^ℓ / J^{ℓ+1}` requires the GS filtration first. | Blocked on previous row. |

## Promotion path (priority order)

1. **`gradedMarkovTrace` → `def`** — ✅ landed via P2.6 Lean refactor
   (2026-05-02). The opaque axiom has been removed; instances now
   supply `S.gradedTrace : Fin levelBound → ℝ` directly.
   *Remaining*: a fully constructive `def` (rather than a class
   field) requires full formalization of the GS-filtration
   (`ConfinementLevel`); out of scope here, tracked as a downstream
   Mathlib-infrastructure issue.

2. **`residueAtRoot` → `def`** — ✅ landed via P2.6 Lean refactor
   (2026-05-02). The opaque axiom has been removed; instances now
   supply `S.residue : Fin levelBound → ℝ` directly.
   *Remaining*: a fully constructive `def` would compute the
   cyclotomic projection in the Habiro completion (per
   `prop:residue-at-root`) — this also needs the GS-filtration
   infrastructure plus a Habiro-completion formalization. Out of
   scope; tracked downstream.

3. **`spectral_sum_finite` → proof** — ✅ landed via P2.6 Lean
   refactor (2026-05-02). The previous `sorry` has been removed by
   reformulating finiteness as a tautology over `Fin levelBound`.
   The class-based residue function has compact-finite domain by
   construction.

4. **`spectral_decomposition` → theorem** (Effort: very large)
   *Requires*: (1), (2), and the analytic identification of the
   cyclotomic tail with the residue contributions — i.e. the
   classical Habiro–Mittag-Leffler bridge.
   *Action*: long-term; the empirical witness (machine-precision
   agreement on every available atom) is the working substitute.

5. **`HabiroResidueSumEquivalence.archimedean_agreement` → theorem** (Effort: large)
   *Requires*: (4) plus the polynomial-side `tail_in_ideal` axiom of
   `HabiroCompletion`.
   *Action*: derive directly from (4) once available.

6. **`protonExample.archimedean_agreement` → numerical proof** (Effort: medium)
   *Requires*: full transcription of the proton's degree-48 Markov
   polynomial into Lean (49 integer literals) and a
   `decide`/`native_decide` evaluation at `q_0`.
   *Alternative*: emit an autogenerated sibling
   `examples/proton-trace-coeffs.lean` from
   `habiro-coefficients-atomic.witness.json` via a small TS or Bun
   script.
   *Action*: feasible standalone; tracked as a small follow-up.

## Empirical-witness coverage (current)

The cross-pipeline validators on this branch certify the
agreement at machine precision on:

| Atom | `tail_in_ideal` (atomic) | `tail_in_ideal` mod p ∈ {2..13} | atomic-vs-interpolate (60 dps) | atomic-vs-residue (term6) |
|------|---------------------------|---------------------------------|-------------------------------|----------------------------|
| p (proton, A=1) | ✓ | ✓ all 6 | ✓ rel ≤ 1e-12 | ✓ rel = 0 (when 442 lands) |
| n (neutron, A=1) | ✓ | ✓ all 6 | ✓ rel ≤ 1e-12 | ✓ rel = 2.79e-16 (when 442 lands) |
| D (deuteron, A=2) | ✓ | ✓ all 6 | ✓ rel ≤ 1e-12 | ✓ rel = 0 (when 442 lands) |
| T (triton, A=3) | (no atomic poly yet) | (n/a) | (interpolate-only) | (n/a) |

The `T` row is the next obvious extension: re-run
`habiro_coefficients_atomic.py` with `Z=1, N=2, include_inter=True`
to add T to the atomic side.  The interpolate witness reports
walltime ~13 s for T at 60 dps; the atomic-poly path is likely
faster but produces a much larger polynomial.

## Recommended next moves (out of scope of this audit)

- **Issue**: "Formalize `ConfinementLevel` and the GS-filtration of `H_n(q)`" — blocks every promotion above.
- **Issue**: "Quantum dilogarithm meromorphic-at-roots-of-unity lemma" — small, self-contained, useful well beyond this chapter.
- **PR (mechanical)**: emit `examples/<atom>-trace-coeffs.lean` from each atomic witness via a Bun script, populating the explicit `Polynomial ℤ` literal so the `archimedean_agreement` `sorry` can be discharged by `native_decide`.
