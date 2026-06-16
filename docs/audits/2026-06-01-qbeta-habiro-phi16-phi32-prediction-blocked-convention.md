# Φ_16/Φ_32 prediction test — BLOCKED on convention mismatch (2026-06-01)

> Attempted to test the falsifiable strand-doubling predictions from
> [the Φ_8 categorical-interpretation audit](2026-06-01-qbeta-habiro-phi8-interpretation.md):
> (³He − D) should carry `Φ_16 = u^8 + 1`, (⁴He − ³He) should carry
> `Φ_32 = u^16 + 1`.
>
> **Test could not run.** Investigation surfaced a convention mismatch
> between two compute pipelines that BOTH claim to produce
> "atomic tr_M values". The Φ_8² factorization was found using one
> convention; the canonical Phase 5q closed form uses another.
> Resolving the mismatch is a prerequisite to the prediction test.

## TL;DR

| Compute pipeline | Deuteron `tr_M(D)` at q₀ | Convention |
|---|---|---|
| `habiro-coefficients-atomic.witness.json` (source of Φ_8² finding) | **0.3883** | `include_inter=True` canonical word marshalling |
| Phase 5q closed form (`compute_tau_M_nucleon_H3`) | **0.7281** | `chi_lambda_braid` marshalling, `include_inter=False` |
| Phase 5q closed form for ³He | 0.4437 | `tau_p² · tau_n · z(q)²` (2 positive interfaces) |
| Phase 5q closed form for ⁴He | 0.1539 | `tau_p² · tau_n² · z(q)² · (z−h)(q)` (2 positive + 1 negative) |

**The deuteron values differ by a factor of ~2 (0.3883 vs 0.7281).** These
are not the same object under the same normalization — they're different
quantities computed by different methods.

## Why this matters for the Φ_8² interpretation

The Φ_8² factorization in (D − n) — and consequently the strand-doubling
categorical-interpretation chain `Φ_8(u) = Φ_4(u²)` proposed in
[the Φ_8 audit](2026-06-01-qbeta-habiro-phi8-interpretation.md) — was
derived from the Habiro-witness convention (`include_inter=True`,
0.3883). If the canonical Phase 5q convention (0.7281) gives a
DIFFERENT factorization for (D − n), then:

- **Φ_8² may be convention-dependent**, not a categorical feature of
  the deuteron itself.
- The falsifiable predictions for (³He − D) and (⁴He − ³He) would
  need to be re-derived in the canonical convention before testing.

OR — if both conventions give the SAME Φ_8² factorization on (D − n),
then the structural interpretation IS convention-independent, and the
prediction test can proceed.

**Either outcome is informative. Neither has been verified yet.**

## What the agent did establish

1. **The Phase 5q closed forms for D, ³He, ⁴He exist** and use:
   - `tr_M(D, q) = τ_p · τ_n · z(q)`
   - `tr_M(³He, q) = τ_p² · τ_n · z(q)²`
   - `tr_M(⁴He, q) = τ_p² · τ_n² · z(q)² · (z − h)(q)`

   With τ_p, τ_n as the canonical single-nucleon Markov-trace
   eigenvalues (different from the `include_inter=True` p/n values
   in the Habiro witness).

2. **The Habiro-witness convention differs from Phase 5q at the
   first opportunity** (the deuteron), so any extraction of ³He/⁴He
   Habiro coefficients in either convention must be done from
   scratch in that convention — they can't be cross-mapped trivially.

3. **The strand-doubling prediction depends on the convention**:
   if Φ_8² is convention-dependent, then Φ_16 / Φ_32 may not appear
   in the canonical Phase 5q ³He / ⁴He factorizations at all.

## What's blocked

- Testing the Φ_16 / Φ_32 / Φ_{2^{k+1}} predictions.
- Verifying the strand-doubling categorical interpretation as
  structural rather than convention-dependent.

## What's NOT blocked

- The empirical Φ_8² factorization on (D − n) in the Habiro-witness
  convention IS real (the [factorization audit](2026-05-31-qbeta-habiro-cross-pair-quick-dp.md)
  produced this directly from the witness data). The structural
  interpretation `Φ_8(u) = Φ_4(u²)` is also a real algebraic identity.
- The cyclotomic-prefactor framework (single-nucleon Φ_4, isospin-doublet
  Φ_1·Φ_2, atomic-step Φ_{2^{k+1}}) remains a viable categorical hypothesis,
  pending the canonical-convention check.

## Next-action — resolve the convention before testing

Two complementary next steps, in priority order:

1. **Canonical-convention re-factorization on (D − n).** Recompute
   the Σ_m Δa_m·(u;u)_m sum using Phase 5q tr_M values for proton,
   neutron, deuteron. Check whether Φ_8² appears, doesn't appear,
   or is replaced by a different cyclotomic factor.
   - If **YES Φ_8² appears in both conventions**: the strand-doubling
     interpretation is convention-independent → proceed to test
     Φ_16/Φ_32 in either convention.
   - If **NO Φ_8² in canonical convention**: the strand-doubling
     interpretation is specific to the Habiro-witness convention.
     Need to identify what categorical structure each convention
     reflects, and which one is the canonical Q_β framework input.

2. **Generate canonical Phase 5q Habiro coefficients for ³He, ⁴He.**
   Once the convention question is settled, generate the integer
   Habiro coefficients for ³He and ⁴He via the same closed-form
   `tr_M = τ_p^a · τ_n^b · z^c · ...` structure, sequential polynomial
   division.

## Cross-references

- Φ_8 audit (subject of this test): [`2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md)
- Cross-pair audit (source of Φ_8²): [`2026-05-31-qbeta-habiro-cross-pair-quick-dp.md`](2026-05-31-qbeta-habiro-cross-pair-quick-dp.md)
- Parent factorization (source of Φ_1·Φ_2 + P_8): [`2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Phase 5q canonical pipeline: `compute_tau_M_nucleon_H3` (in `computations/`); search for definitions.
- Habiro-witness convention: [`habiro-coefficients-atomic.witness.json`](../../computations/habiro/habiro-coefficients-atomic.witness.json) (uses `include_inter=True`)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) PROBE NEW

## Discipline note

Per CLAUDE.md flip-flop history: "every flip used a fresh canonical-
looking formula and matched it numerically near the substrate q_0".
The Φ_8² finding was a structural (not numerical) match, but its
convention-dependence raises the same risk. **Do not promote the
strand-doubling chain to a derivation** until the canonical-convention
re-factorization confirms Φ_8² survives.
