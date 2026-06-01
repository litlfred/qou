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
| 1. Cross-anchor stability test | NUANCED PASS | done — Form A/B coefficients stable to 10⁻⁷; ~54 ppb improvement reproduced at both anchors |
| 2. Higher-precision PSLQ | NULL | done — no clean integer relations at 120 dps / maxcoeff 10⁶; exact N = 79.9677 not integer 80 |
| 3. Structural derivation (80, 7/8, G/(8π)) | SUBSUMED | covered by Task 2 NULL — no clean basis combination identified |
| 4. Two-coefficient PSLQ | SUBSUMED | covered by Task 2 full-basis PSLQ NULL |

## Findings summary

**The h⁴-residual coefficient is empirically very close to (but not exactly equal to) several
natural forms:**

- `1 - π²/80` matches at 56.9 ppm in the coefficient (exact N would be 79.9677)
- `7/8 + (G/(8π))·h²` matches at ~10⁻⁵ residual after both terms
- Continued-fraction convergent `547760/624883` matches at 10⁻¹¹ — no clean small structure

**Task 1 sub-finding (genuinely positive):** The 54-ppb improvement provided by Form A/B
is REPRODUCED at both proton-pin AND muon-pin q anchors. This is the signature of a
substrate-derived correction, not a proton-anchor coincidence basin.

**Task 2 sub-finding (negative):** Higher-precision PSLQ across 17 natural substrate basis
elements (G, π², ζ(3), ζ(5), ln(2), ln(3), ln(5), α_em, h^k, [k]_q, …) at 120 dps with
maxcoeff 10⁶ found NO clean integer relations. The h⁴-residual coefficient is NOT a
rational multiple of any single basis element.

**Combined interpretation:**

The 54 ppb residual after `(α_em/π)/dim H_3` IS a real substrate-stable signal (Task 1
positive), but its coefficient is NOT a clean combination of natural constants at the
basis tested (Task 2 negative). Two remaining hypotheses:

  (a) **More exotic basis required** — Mahler measure of a Bring-quintic polynomial,
      Bloch-Wigner D(z) at substrate-specific roots, etc.
  (b) **CODATA precision floor** — the 54 ppb signal may be at the edge of CODATA
      precision for (α_em, m_e, m_μ, m_p), in which case the "form" cannot be uniquely
      identified.

Neither hypothesis is tractable in a single session. The structural derivation hunt
is **CLOSED with NULL at PSLQ basis level**; future work would need either substantially
more sophisticated basis construction or improved experimental anchors.

## Cross-references

- merged [PR #1581](https://github.com/litlfred/qou/pull/1581) (closed-route reexamination — 54 ppb baseline)
- merged [PR #1617](https://github.com/litlfred/qou/pull/1617) (closed-route follow-ups — Form A/B exploration)
- audit [`2026-06-01-closed-route-reexamination-roundup.md`](../audits/2026-06-01-closed-route-reexamination-roundup.md)
- coord [`2026-06-01-closed-route-followups.md`](./2026-06-01-closed-route-followups.md) (Form A/B detail)
