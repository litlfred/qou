# Model-G spectator constant `b` vs Q_β — numerology check (scope-(a) negative)

**Date:** 2026-07-18 · **Branch:** `claude/h4-exponents-value-screen-96501m` ·
**Scope:** (a); a tempting near-match tested against the numerology guard and
**refuted** as a fit-mean coincidence; nothing wired; no tier change. Recorded
so the coincidence is not mistaken for a derivation later.

## The tempting near-match

Model G ([consolidated record](2026-07-14-model-g-consolidated-record.md)) carries
an **empirical** light-spectator channel constant `b = 0.78192 MeV/nucleon`
(calibrated on the three one-bond composites ⁶Li, ⁷Li, ⁹Be). The canonical
neutron β-decay Q-value is `Q_β = 0.78233341 MeV` (CODATA). These agree to

```
b / Q_β − 1 = −0.053 %   (530 ppm)
```

A 0.05 % match is tempting: it would *derive* a fitted Model-G constant from the
canonical CAL-2 weak-sector scale (the spectator nucleon binding through the same
bar-odd weak channel that governs β-decay), removing a fit.

## The guard — per-composite decomposition dissolves it

`b` is not a single measured quantity; it is the **mean** of three independent
one-bond determinations. Backing `b` out of each composite separately
(`deficit = b · A_light · m`; α, d, t, n at AME values):

| composite | decomposition | `b = deficit/(A_light·m)` | vs Q_β(CODATA) |
|---|---|--:|--:|
| ⁶Li | α + d | 0.73688 | **−5.81 %** |
| ⁷Li | α + t | 0.82254 | **+5.14 %** |
| ⁹Be | 2α + n | 0.78635 | +0.51 % |
| **mean** | — | **0.78192** | **−0.05 %** |

The per-composite `b` **scatters by ±5.5 %** — a hundred times the 0.05 %
mean-match. ⁶Li wants 0.737, ⁷Li wants 0.823; neither is within 5 % of Q_β. Only
the *average* lands on Q_β, and the average of three values spread over ±5.5 %
coinciding with any fixed target near 0.78 MeV is **exactly what chance
produces** — 0.78 MeV is a generic light-nucleus per-nucleon binding scale.

**Verdict (scope-(a)):** `b ≈ Q_β` is a **fit-mean coincidence, not a structural
identification.** A genuine `b = Q_β` would require each composite to return
≈ 0.782 (a per-bond structural equality); instead the spread (±5.5 %) swamps the
match. No categorical mechanism connecting the spectator channel to the weak
sector is supplied or implied. Do not wire, and do not record `b = Q_β` as
derived.

## Why record a negative

Per the anti-numerology / "before declaring refuted" disciplines: this near-match
is the kind a later agent (or an outside reader) would re-discover and be tempted
to launder into a derivation. Recording the per-composite scatter forecloses that.
The honest Model-G status is unchanged: `b` remains **empirical** (the audit's own
tier), and the mixed-multibond miss remains the open shared/sub-additive-channel
problem (#3808 rounds 8–11), which a derived — not fitted — invariant must close.

## Provenance

Vendored AME2020 (`qou-mass/.../ame2020.json` via
`codata_constants._ame_binding_mev`); `b = 0.78192` from the committed
[`inter-cluster-bond-term`](../../computations/deltalambda/inter-cluster-bond-term.witness.json)
/ [Model-G record](2026-07-14-model-g-consolidated-record.md); `Q_β` CODATA from
the corpus q-β witnesses. mpmath 30-dps; exact rational binding differences.
