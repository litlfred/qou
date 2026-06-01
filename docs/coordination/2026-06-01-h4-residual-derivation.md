# h⁴-residual structural-derivation hunt — 2026-06-01

Branch: `claude/h4-residual-structural-derivation-2026-06-01`

Per PR #1617's exploration finding (commit `51b80545de`), the 54 ppb
residual on the Ocneanu `(α_em/π)/dim H_3` near-match is closed
sub-ppb by two empirical forms:

  Form A: `f = 1 + (1 - π²/80)·h⁴`            → 0.003 ppb (17,584× over baseline)
  Form B: `f = 1 + (7/8)·h⁴ + (G/(8π))·h⁶`    → 0.0008 ppb (68,576× over baseline)

Both pass below the 1 ppQ substrate target. But the constants
`80 = 2⁴·5`, `7/8`, and `G/(8π)` LACK clean structural derivation.

This branch attempts to:

1. **Cross-anchor stability test** — re-evaluate Form A/B at the
   muon-anchored q₀ (vs the proton-anchored q₀ used in #1617). True
   structural forms should be q-anchor-stable; coincidence basins
   collapse under cross-anchor variation. Pre-stated failure
   signature: works at proton-pin but fails at muon-pin → empirical
   fit.

2. **Higher-precision PSLQ** — at 100+ dps with maxcoeff up to 10⁶
   across wider substrate basis (Mahler measures, Bloch-Wigner
   dilog at substrate roots, Apéry-like constants, q-Bernoulli
   evaluations).

3. **Structural derivation attempts**:
   - `80 = 2⁴ · 5`: try to derive from 4 EM-halvings × Bring quintic
   - `7/8`: try Bring saturating-genus T_(2,7) contribution
   - `G/(8π)`: try fine-structure prefactor recurrence

4. **Two-coefficient PSLQ** — search for `f = 1 + a·h⁴ + b·h⁶` with
   small integers (a numerator, denominator) for both coefficients.

## Status

| Task | Tier | Status |
|---|---|---|
| 1. Cross-anchor stability test | TBD | pending |
| 2. Higher-precision PSLQ | TBD | pending |
| 3. Structural derivation (80, 7/8, G/(8π)) | TBD | pending |
| 4. Two-coefficient PSLQ | TBD | pending |

## Cross-references

- merged [PR #1581](https://github.com/litlfred/qou/pull/1581) (closed-route reexamination — 54 ppb baseline)
- merged [PR #1617](https://github.com/litlfred/qou/pull/1617) (closed-route follow-ups — Form A/B exploration)
- audit [`2026-06-01-closed-route-reexamination-roundup.md`](../audits/2026-06-01-closed-route-reexamination-roundup.md)
- coord [`2026-06-01-closed-route-followups.md`](./2026-06-01-closed-route-followups.md) (Form A/B detail)
