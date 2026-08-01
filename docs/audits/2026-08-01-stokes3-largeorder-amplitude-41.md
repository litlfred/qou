# A_ω = 3: the resurgent large-order route — does the 4₁ κ-tower amplitude reproduce the GGM integer Stokes constant?

**Date:** 2026-08-01 · **Bean:** `qou-fgte` (T4: Stokes-3 identification) ·
**Branch:** `claude/stokes3-identification-aomega-2026-08-01` ·
**Tier:** numerical (large-order asymptotics; exact-κ-validated low orders) ·
**Discipline:** scope-(a); no fit; no c_k wired; A_ω=3 stays the GGM-algebraic result — here CROSS-CHECKED, not re-derived.

**Probe:** [`qbeta_stokes3_largeorder_amplitude_probe.py`](../../computations/qbeta/qbeta_stokes3_largeorder_amplitude_probe.py)
· witness [`qbeta-stokes3-largeorder-amplitude.witness.json`](../../computations/qbeta/qbeta-stokes3-largeorder-amplitude.witness.json).

## 0. Two objects, both called "A_ω" — do not conflate (framing correction)

Per [`2026-07-18-g3-stokes-keystone-evidence-base.md` §0](2026-07-18-g3-stokes-keystone-evidence-base.md):

| object | what it is | value | source |
|---|---|---|---|
| **instanton ACTION** `A` | Borel-plane singularity **location** (denominator of the factorial growth) | `ι = Vol(4₁)/π ≈ 0.646` (complex ±𝔙) | GGM eq 46; corpus #3692/#3819; measured |
| **Stokes CONSTANT** `A_ω` | **amplitude** of that singularity (numerator) | **integer 3** | GGM state-integral / 3d-index — **exact, algebraic** ([`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py), `S⁺(q→0)=[[1,3],[0,1]]`) |

The exact **3** is already established algebraically. What was still open (bean
`qou-fgte`): the **resurgence large-order route** — does the geometric-connection
perturbative κ-tower's own factorial growth independently reproduce the amplitude
`2πC_n → 3`? The 2026-07-07 audit extracted the **action** (denominator) to 6
orders; it never extracted the **amplitude** (Stokes constant / numerator).

## 1. Method

_[results section filled after the compute run — see §2]_

## 2. Results

_[to be filled]_

## 3. Verdict

_[to be filled]_

## Cross-references

- Algebraic A_ω=3: [`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py)
- Action (complex ±𝔙, preliminary): [`2026-07-07-fmap-resurgence-action-and-pion-knot.md`](2026-07-07-fmap-resurgence-action-and-pion-knot.md)
- κ-tower exact closed forms: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md)
- Framing (even/odd A_ω, keystone): [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
- Per-winding Stokes family: [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md)
