# CODATA registry vintage straddle — the m_p L2 "437× miss" is bookkeeping

**Date:** 2026-08-09
**Bean:** `qou-2an8` (the check it asked for), session `qou-ltmt`
**PR:** [#4860](https://github.com/litlfred/qou/pull/4860)
**Probe:** [`computations/codata_registry_triangulation_probe.py`](../../computations/codata_registry_triangulation_probe.py)
**Witness:** `computations/codata-registry-triangulation.witness.json` (audit-only, 3 assertions, all pass)

## Summary

The largest single entry on the L2 100× fail list — `m_p` at **+1.351 ppb,
a 437× miss** — carries **no physical content**. It is the arithmetic
inconsistency between two CODATA registries of different vintages, reported
as though it were a prediction error.

Bean `qou-2an8` raised exactly this possibility and, correctly, declined to
assert it:

> "the documented de-fitted m_p round-trip miss is +1.35 ppb and the CODATA
> 2018→2022 proton shift is also +1.35 ppb; whether these are the same
> number is a check to run, not a conclusion."

This audit runs the check. They are the same number.

## Method — internal triangulation, no external lookup

The corpus stores an algebraically over-determined triple; any two members
fix the third. All three are labelled "CODATA 2022":

| quantity | in-repo source | value |
|---|---|---|
| `m_e` | `codata_2022_source.M_E_MEV` | 0.51099895069 MeV |
| `m_p/m_e` | `qou_substrate.constants.MASS_RATIO_P_E` — the q₀ pin anchor | 1836.152673426 |
| `m_p` | `codata_2022_source.M_P_MEV` — the L2 comparison target | 938.27208816 MeV |

A same-edition triple is consistent by construction, so the residual is a
self-contained integrity test. No published table needs to be consulted, and
none is: every number here is read from repo sources at run time, never
re-typed as a literal.

## Leg 1 — the proton triple is inconsistent

```
m_e · (m_p/m_e)   =  938.27208942732424736394 MeV
m_p registry      =  938.27208816            MeV
residual          =  +1.3507 ppb
```

**The bar is the printed granularity, not the quoted σ.** Within a single
CODATA adjustment these three are not independent measurements — they are one
global least-squares output, and the MeV-valued `m_p` is derived downstream of
`m_e` and the ratio. A same-edition triple therefore agrees to the round-off
of its last printed digit: `m_p` is stored to 11 significant figures, i.e.
0.0107 ppb.

> residual = **127× the last printed digit.** Rounding cannot produce this.

*Recorded but not used as the test:* against the combined measurement σ
(0.430 ppb) the residual is only **3.14 σ** — suggestive, not decisive. An
earlier draft of this probe asserted a >10 σ threshold; that was wrong and was
corrected. The granularity argument is the sound one and is the one the
witness asserts.

## Leg 2 — an independent observable picks the stale member

`m_n = m_p + m_e + Q_β` must reproduce the separately-stored CODATA **direct**
neutron (`M_N_MEV_CODATA_DIRECT` = 939.56542194). Feeding the same β-decay
Q-value with each candidate proton:

| proton used | neutron | residual | in σ |
|---|---|---|---|
| stored `M_P_MEV` | 939.56542052069 | −1.511 ppb | 2.96 σ |
| `m_e · (m_p/m_e)` | 939.56542178801 | **−0.162 ppb** | **0.32 σ** |

The ratio-consistent proton lands inside 1 σ of an observable it was not
built from; the stored proton misses by ~3 σ. The stored `m_p` is the stale
member.

This is corroborated by the module's own contents: `codata_2022_source` holds
the genuine 2022 electron mass (…069, not the 2018 …000) and the genuine 2022
direct neutron — but a 2018 proton. One vendored snapshot, mixed vintage.

## Leg 3 — the muon leg is non-discriminating

Reported for completeness only. The muon triple's residual is 1.410 ppb
against a combined σ of 31.1 ppb — the uncertainty is **23× the effect under
test**, so the leg can neither confirm nor exclude. An earlier draft used it to
"localise the defect to the proton"; that was an overclaim and was removed. It
supports no conclusion in this audit.

## Leg 4 — where the artifact does *not* reach: the μ–p tension

`m_μ` is the single largest L2 miss (963.6×). If the vintage straddle
explained that too, this would be a far bigger finding — so it was tested
explicitly rather than left implied. It does not:

| muon–electron ratio used | m_μ miss |
|---|---|
| 206.7682830 (as stored, 2018) | 963.6× |
| 206.7682827 (2022) | **970.2×** |

Correcting the vintage makes `m_μ` **worse**. Recorded as measured: a
correction that degrades an observable is reported, not suppressed. The μ–p
substrate tension is genuine physics and this finding does not touch it.

## Leg 5 — the stale proton reaches Q_β's *target*, but Q_β's miss survives

Q_β is one of the two genuine L2 levers (see the companion finding below), so
its comparison target had to get the same treatment. The corpus holds **two**
experimental determinations: `Q_BETA_MEV_AME` (AME2020 direct) and
`m_n(direct) − m_p − m_e`. The second is built on the stale proton.

| disagreement between the two determinations | ppb | σ |
|---|---|---|
| using `M_P_MEV` as stored | 1814.2 | 2.33 σ |
| using `M_P_MEV_RATIO_CONSISTENT` | **194.3** | 0.249 σ |

The stale proton explains **89.3%** of the disagreement — the two
determinations then agree comfortably.

Prediction scored against each target:

| target | miss |
|---|---|
| AME2020 | 164.0× |
| via consistent m_p | 139.1× |
| via **stale** m_p | 68.7× ← the trap |

**Q_β's miss is genuine** against every legitimate target (139–164×, both ≫
100×) — unlike m_p, the artifact does not dissolve it. But an unwary
comparison against the stale-derived target reads 68.7×, ~2.4× too
optimistic. This is the second place the same stale literal produced a
misleading accuracy number.

## What was fixed in the registry, and what deliberately was not

`physics.nist.gov` is egress-blocked from the authoring sandbox, so the true
CODATA-2022 proton digits could not be verified. That constrains the fix:

**Fixed** (provable from repo contents alone):
- `M_P_MEV`'s docstring no longer claims "CODATA-2022". It carries the
  inconsistency proof and the neutron-leg identification.
- `M_N_MEV_AME_DERIVED`'s docstring records that its ~1.5 ppb disagreement
  with the direct neutron is explained by the stale proton it is built from,
  and that it is **not** an independent neutron measurement.
- Added `M_P_MEV_RATIO_CONSISTENT` (+ error), explicitly **derived**.
- Added `MASS_RATIO_P_E` as a **re-export sourced** from `qou_substrate` —
  not a copy. A local literal would have made the module a fourth registry
  for the same quantity, i.e. the defect class itself. Fail-soft so a missing
  `qou_substrate` cannot break 234 importers to serve a diagnostic.
- Added `triple_consistency_ppb()` / `assert_triple_consistent()` — a
  regression guard against a defect no precision audit can catch: exactly
  representable, correctly typed, precise to 11 figures, wrong edition. It
  asserts against a known-residual ceiling rather than zero, so it is not a
  guard that is expected to fail.

**Not fixed:** the literal itself. Writing a *derived* number into a file
whose stated purpose is to vendor NIST quotes would reintroduce exactly the
provenance defect being documented. The swap stays open on bean `qou-if87`,
gated on a verified quote. **No value changed; zero blast radius.**

## Why the dashboard row is exactly this residual

`q₀` is Newton-solved so that the substrate identity reproduces
`MASS_RATIO_P_E` exactly:

$$
m_p/m_e \;=\; 2\,\frac{\mathrm{Vol}(4_1)}{\hbar_q^2}\,F_{\mathrm{Bor}}(q_0) \;-\; 12
$$

so the producer's prediction is *identically* `m_p_pred = m_e · MASS_RATIO_P_E`.
Its "error" against `M_P_MEV` is therefore, by construction, the leg-1
residual:

```
dashboard m_p err  =  1.351      ppb   (miss factor 437.0×)
leg-1 residual     =  1.3507001  ppb
|difference|       =  0.0003     ppb
```

The agreement is limited by the dashboard's own 4-significant-figure
serialization of `err_ppb`, not by physics. There is no room left for a
physical contribution.

## Consequence for L2 — a phantom removed, no count inflated

**`m_p` does not become "MET".** Under the proton pin `m_p` *is* the anchor,
so a clean round-trip is a calibration tautology — precisely the trap
[`AGENTS.md` §"q₀ anchor convention" rule 1](../../AGENTS.md) already guards
against for `m_μ` under the muon pin. The honest disposition is that the row
should not be **scored** in either direction; it is an anchor round-trip
diagnostic. The count does **not** rise to 3/7 on the strength of this.

For the two rows that inherit the stale target, scoring against a
self-consistent registry gives (audit-only projection; the dashboard is
unmodified):

| observable | err (was) | miss (was) | verdict |
|---|---|---|---|
| `m_n` | 0.903 ppb (2.414) | **176.7×** (420.1) | still FAIL — genuine |
| `Δ_pn` | 655.9 ppb (773.9) | **151.3×** (163.3) | still FAIL — genuine |

Both improve materially yet remain genuine failures, driven by the real Q_β
residual. Nothing is laundered into a pass.

**Net effect on the frontier.** After removing the artifact, every surviving
nucleon-side L2 miss traces to two levers already on the board — the Q_β /
Habiro closure (bean `kehn`) and the μ–p substrate tension. The 437× `m_p`
entry was never a lever, and work aimed at "closing the m_p gap" was aimed at
a bookkeeping error.

## Scope

Scope-**(a)**, in the sense of `AGENTS.md` §"Before declaring refuted":
this shows that *the m_p row as currently computed* measures registry
inconsistency. It makes no claim about the substrate identity's accuracy —
that question is simply not tested by a round-trip of its own anchor, which is
the point.

## Companion finding — the 5 L2 failures are 2 independent ones

Probe: [`computations/l2_row_independence_probe.py`](../../computations/l2_row_independence_probe.py),
witness `l2-row-independence.witness.json`.

Removing the `m_p` artifact prompted the obvious next question: are the
remaining rows independent? Three of the five are not. The identities hold on
**both** the prediction side and the target side:

```
Delta_pn  ==  Q_beta + m_e             pred resid  2.0e-12 MeV   target resid -6.9e-10 MeV
m_n       ==  m_p + Q_beta + m_e       pred resid  3.2e-11 MeV   target resid -6.9e-10 MeV
```

(Residuals are the rounding of the dashboard's own ~12-significant-figure
serialized strings, not physics.)

The target side is dependent because `M_N_MEV_AME_DERIVED` is *constructed*
as `M_P_MEV + M_E_MEV + Q_BETA_MEV_AME` — the neutron value the dashboard
scores against is built from the proton registry and the AME β-decay
Q-value, not measured independently of them.

| row | status |
|---|---|
| `m_p` | **artifact** — pin-anchor round-trip vs a stale registry |
| `m_n` | **redundant** — `m_p + Q_β + m_e` on both sides |
| `Δ_pn` | **redundant** — `Q_β + m_e` on both sides |
| `Q_β` | **independent failure** — lever: Habiro closure (bean `kehn`) |
| `m_μ` | **independent failure** — lever: μ–p substrate tension |

**Five reported failures are two independent ones.** L2 planning that reads
the list as five fronts over-counts the work and mis-ranks it.

*Not claimed:* that the dependent rows are wrong to publish (m_n in MeV is a
useful number — it is just not an independent test), nor that Q_β and m_μ are
the only *possible* failures — only the only independent ones among the rows
currently scored. `M_N_MEV_CODATA_DIRECT` **is** an independent neutron
value; it is simply not what this dashboard scores against.

## Blast radius of the follow-up fix (scoping datum, not a defect count)

Correcting `M_P_MEV` is a one-line edit with a long tail. Counting references
under `computations/`, `tools/`, `qou-mass/` (excluding `_deprecated/`):

| | count |
|---|---|
| files referencing `M_P_MEV` / `M_P_MEV_VALIDATION` | **234** |
| of those, files that construct a `WitnessBuilder` | **175** |

**Read this as scope, not as 175 wrong numbers.** Most consume the value as a
*validation comparison target*, where a 1.35 ppb shift is far below what the
consumer resolves; a few may consume it as an *input*, which the
three-calibration discipline forbids independently of vintage. The point is
only that the fix regenerates a large committed-witness surface and therefore
needs its own scoped, owner-gated branch with a long-compute plan — it is not
an idle-drain item.

## Follow-ups (deliberately not in PR #4860)

1. Correct `codata_2022_source.M_P_MEV` to the 2022 value and re-score the
   dashboard. Touches committed witnesses ⇒ its own scoped branch.
2. Re-classify the `m_p` dashboard row as an anchor round-trip diagnostic,
   mirroring the existing `m_μ` treatment.
3. Triangulate `Q_BETA_MEV_AME` and `M_MU_OVER_M_E` once a 2022 snapshot
   lands — `M_MU_OVER_M_E` = 206.7682830 is on the same suspicion list, though
   leg 3 shows the muon registry is too coarse to settle it internally.
4. `MASS_RATIO_P_E_ERR` = 1.1e-7 is the 2018 uncertainty even though the value
   is 2022; it inflates `Q_ERR` and every downstream error bar slightly.

## Cross-references

- Bean `qou-2an8` (this check), `kehn` (Q_β lever), `tnjb` (q₀ anchor hygiene)
- [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md)
  — where the +1.35 ppb de-fitted round-trip was first documented, as a
  theory residual. This audit reclassifies that number.
- [`docs/precision-goals.md`](../precision-goals.md) — the L1/L2 legs
