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

## Current opaque / sorry surface

| Decl | Kind | Where | Type signature | Blocks |
|------|------|-------|----------------|--------|
| `gradedMarkovTrace` | `noncomputable opaque` | `gb-residue-spectral-sum.lean:32` | `ℕ → ℝ → ℝ` | The whole GB filtration |
| `residueAtRoot` | `noncomputable opaque` | `gb-residue-spectral-sum.lean:36` | `ℕ → RootOfUnity → ℝ → ℝ` | The spectral-sum identity |
| `GBResidueSpectralSum.spectral_decomposition` | class field axiom | `gb-residue-spectral-sum.lean:55` | `mass = ‖descended‖ + Σ_ℓ Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})` | The proposition itself |
| `spectral_sum_finite` | `sorry` (`Fin levelBound` access) | `gb-residue-spectral-sum.lean:80` | `∃ N, ∀ ℓ ≥ N, residueAtRoot ℓ S.roots⟨0,_⟩ S.q = 0` | Termination |
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

1. **`gradedMarkovTrace` → `def`** (Effort: large)
   *Requires*: full formalization of the GS-filtration (`ConfinementLevel`).
   *Action*: out of scope for this PR; create a tracking issue.

2. **`residueAtRoot` → `def`** (Effort: medium-large)
   *Requires*: a small Mathlib lemma about meromorphicity of the
   quantum dilogarithm at roots of unity, then `Complex.residue`
   applied to `Φ_q · gradedMarkovTrace`.
   *Action*: write a `quantum-dilogarithm-meromorphic-at-roots.lean`
   skeleton (one definition + one `meromorphicAt` lemma + one
   `residue_eq_pow_coefficient` corollary) — block this on (1) for
   the trace half.

3. **`spectral_sum_finite` → proof** (Effort: small)
   *Requires*: the `confinement-level-unique` proposition (already
   stated, currently `sorry`).  The finiteness of the spectral sum
   then follows by transport.
   *Action*: prove `confinement-level-unique` first; then this
   becomes a one-line `simp_rw`.

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
