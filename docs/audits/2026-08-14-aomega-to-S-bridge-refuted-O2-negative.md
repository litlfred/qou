# The `A_ω → S` bridge is not derivable (O2 negative) — retained exploration

**Date:** 2026-08-14
**Beans:** `qou-ws1w` (O2 attempt), `qou-fddz` (O1-remove), `qou-q3np` (the prior negative), `qou-arc1` (ARC STATUS decision point)
**Probe:** [`computations/probes/aomega_o2_stokes_to_observable_mechanism.py`](../../computations/probes/aomega_o2_stokes_to_observable_mechanism.py) (self-contained, EXIT 0)
**Canonical S witness:** [`computations/qbeta/qbeta-c3-barodd-sleak.witness.json`](../../computations/qbeta/qbeta-c3-barodd-sleak.witness.json)

This document is the **retention target** for the `A_ω → S` exploration. Per the
owner directive at the `qou-arc1` decision point — *"3 go; 2 try then 1 remove
from paper if not successful — retain only in audit doc as a last-resort
exploration"* — O2 was attempted and **failed**, so the bridge is removed from the
paper content and preserved here. Nothing is lost: the full exploration, its
numbers, and the reason it fails are all recorded below.

## What the bridge claimed

That the resurgent Stokes / Donaldson–Thomas constant `A_ω = 3` (from the `4₁`
knot) connects to the bar-odd decay residuals

| | central value | = `c₃ + Vol(4₁)` |
|---|---|---|
| `S(muon)` | `+0.00968` | `−2.02020 + 2.02988` |
| `S(proton)` | `−0.03946` | `−2.06934 + 2.02988` |

with the "sign flip" `S(muon) > 0 > S(proton)` read as physical content, and the
integer `A_ω` (and its tower `3, 9, 75, 642, 5580`) somehow producing these small
signed reals.

## O2 attempt and refutation — three compounding obstructions

**(1) The individual targets are not robustly defined (decisive).** From the
canonical witness: each `S` value carries a CAL-3 propagated uncertainty of
**±1.262** — the `1/u³ ≈ 1.6×10⁶` amplification of the Q_β input error. That is
**130× the muon value** and **32× the proton value**. The witness itself asserts
the sign flip is **NOT established by the data** ("must not be cited as an
established sign flip"). The opposite-signed premise the whole bridge rests on is
unresolved.

**(2) The one resolved quantity carries no `A_ω` content.** Only the *swing*
`S(muon) − S(proton) = 0.04914` is resolved (±7.6×10⁻⁷), because the CAL-3 error
is common to both anchors and cancels. But the swing is exactly
`c₃(muon) − c₃(proton)`: `Vol(4₁)` cancels, so the only resolved quantity is the
cross-anchor `c₃` variation — no `Vol(4₁)`, no `A_ω`, no Stokes constant.

**(3) Integrality (bean `qou-q3np`, reinforced by M2).** `A_ω` and the whole
tower are integers. M2 ([`aomega_m2_bps_cohomology.py`](../../computations/probes/aomega_m2_bps_cohomology.py))
showed the closed-sector BPS spectrum is *abelian* — distinct Borel rays, trivial
Davison–Meinhardt plethystic, `dim BPS = |Ω|` — so the count is a plain integer
set, never a Poincaré polynomial. An integer cannot map to a non-integer whose
sign is not even established without free real inputs, and a map with free real
inputs hitting `0.00968` is a fit.

**The most natural framework near-match is an unfalsifiable fit.** `S ~ ℏ_q²` with
the co-occurring 4 gives `S(muon) ≈ ℏ_q² = 0.00982` (1.4% off) and
`S(proton) ≈ −4·ℏ_q² = −0.03927` (0.5% off). Both "match" — but only because
*everything* O(0.01) sits inside the ±1.262 noise band. It needs two free inputs
(`ℏ_q²` and the 4), is ~1% off, uses no Stokes integer, and is unfalsifiable. That
is the signature of a fit, not a derivation.

## Verdict

**O2 fails. There is no parameter-free `A_ω → S` map, and the target is ill-posed.**
This is sharper than the `qou-q3np` negative (no-literature + integrality): the
individual observable targets do not exist to the precision a map would predict,
and the one quantity that does (the `c₃` swing) is `A_ω`-free.

Per the directive, the bridge is **excised from the paper content** and retained
here. What stays in the paper, unaffected:

- **`A_ω = 3` as a certified conditional DT count** (`conj:stokes-dt-bps-bridge`,
  `thm:aomega-fourone-dt-count`, `prop:dt-spectrum-bar-eigenspace`) — now
  additionally *characterized* by M2 (its putative BPS realization would be abelian
  — a conditional structural statement, not a construction; A_ω=3 stays imported). It
  was already declared not-wired-downstream; that stands.
- **`S = c₃ + Vol(4₁)` as a defined residual** (the `binding-qbeta-complex-volume`
  keystone and its S-channel) — kept as a *definition* with its existing ±1.262 /
  "sign flip not established" caveats. Per the 2026-08-08 "defined residual ≠
  derived decomposition" rule, it is not a derived split and is not presented as
  one.

What is removed is only the *claimed connection between them* — that the DT
constant `A_ω` explains or produces the `S` residuals — because that connection is
what O2 could not derive and q3np found unsupported.

## The swing reframe does not rescue it either (corrected)

The one resolved quantity is the swing `S(muon) − S(proton) = 0.04915`. I initially
flagged "retarget the S-channel at the swing" as a *foreseeable* direction
(`qou-6y1p`). Corpus-grep corrected that guess. Two settled facts:

- **c₃ has no first-principles value.** The fixed theory ladder through `N=2` gives
  `Q_theory/Q_base − 1 = c₂·u²` exactly, so the `[u³]` coefficient is *identically
  0*; the ~−2 number is only the circular cal-anchored extraction
  `Q_codata/Q_base(q)` (`docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md`;
  `ck-dk-canonical-registry.md` §3 tier = empirical / circular / not-anchor-stable).
- **The swing is the `1/u³` ladder artifact**, `dc₃/dq ≈ 3.84×10⁶`
  (`computations/qbeta/qbeta-c3-swing-selfdual-pole-vs-ladder.witness.json`).

Their arithmetic consequence, confirmed in
[`computations/probes/aomega_6y1p_swing_reframe_not_tractable.py`](../../computations/probes/aomega_6y1p_swing_reframe_not_tractable.py)
(EXIT 0): **`swing = 0.04915 = (11.54 ppb μ-p substrate tension) × dc₃/dq` exactly.**
So the swing is the known μ-p tension amplified by the circular extraction — not an
independent quantity. Deriving it needs *both* a first-principles c₃ (coefficient
`≡ 0`) *and* the μ-p tension (an open ~9.5σ residual). Same wall. `qou-6y1p`
scrapped. The `S = c₃ + Vol(4₁)` *definition* still stands (it is a definition).

## Discipline

Exploratory forensics + a rigorous negative. No fit wired to production, no witness
overwrite. The O2 probe reads only the committed canonical witness and asserts its
refutation.
