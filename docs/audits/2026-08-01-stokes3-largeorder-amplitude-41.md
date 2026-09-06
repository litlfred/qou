# A_ω = 3: the resurgent large-order route — does the 4₁ κ-tower amplitude reproduce the GGM integer Stokes constant?

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-01 · **Bean:** `qou-fgte` (T4: Stokes-3 identification) ·
**Branch:** `claude/stokes3-identification-aomega-2026-08-01` ·
**Tier:** numerical (large-order asymptotics; exact-κ-validated low orders) ·
**Discipline:** scope-(a); no fit; no c_k wired; A_ω=3 stays the GGM-algebraic result — here the ACTION half is CROSS-CHECKED, the AMPLITUDE half is an honest negative.

**Probes:** [`qbeta_stokes3_largeorder_amplitude_probe.py`](../../computations/qbeta/qbeta_stokes3_largeorder_amplitude_probe.py) (κ-tower extraction)
+ [`qbeta_stokes3_largeorder_amplitude_fit.py`](../../computations/qbeta/qbeta_stokes3_largeorder_amplitude_fit.py) (refined fit)
· witnesses [`…-amplitude.witness.json`](../../computations/qbeta/qbeta-stokes3-largeorder-amplitude.witness.json), [`…-amplitude-fit.witness.json`](../../computations/qbeta/qbeta-stokes3-largeorder-amplitude-fit.witness.json).

## 0. Two objects, both called "A_ω" — do not conflate (framing correction)

Per [`2026-07-18-g3-stokes-keystone-evidence-base.md` §0](2026-07-18-g3-stokes-keystone-evidence-base.md):

| object | what it is | value | source |
|---|---|---|---|
| **instanton ACTION** `A` | Borel-plane singularity **location** (denominator of the factorial growth) | `ι = Vol(4₁)/π ≈ 0.646` | GGM eq 46; corpus #3692/#3819; measured |
| **Stokes CONSTANT** `A_ω` | **amplitude** of that singularity (numerator) | **integer 3** | GGM state-integral / 3d-index — **exact, algebraic** ([`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py), `S⁺(q→0)=[[1,3],[0,1]]`) |

The exact **3** is already established algebraically (and as the exact
q-independent symmetry constant, [`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean)).
What was still open (bean `qou-fgte`): the **resurgence large-order route** — does
the geometric-connection perturbative κ-tower's own factorial growth
independently reproduce the amplitude `2πC_n → 3`? The 2026-07-07 audit extracted
the **action** to 6 orders (finding it "complex / oscillating / preliminary"); it
never extracted the **amplitude**.

## 1. Method

The 4₁ geometric Ohtsuki κ-tower is the `1/N` expansion of the Kashaev sum
`log J_N(4₁) = 2 Σ_{j≤k} log(2 sin πj/N)` after subtracting `(3/2)log N`:
`log J_N = (Vol/2π)N + (3/2)log N + a₀ + Σ_n κ_n/N^n`. The `κ_n` are extracted by
high-precision Richardson (dps 300, **two independent N-ladders** 1200–300000 and
1600–380000, fit order 18 with **guard terms**, trust-gated by cross-fit
agreement). Then the large-order analysis:

- **action** via the ratio law `κ_{n+1}/κ_n = (n+β)/A` (ratio-slope line) and the
  Aitken-accelerated `A_n = n·κ_n/κ_{n+1} → A`, cross-checked by Borel–Padé poles;
- **amplitude** `P = κ_n·A^{n+β}/Γ(n+β)` (≈ const if single-singularity) and its
  normalization vs `3`.

**κ validation (independent re-derivation).** `κ₁…κ₄` reproduce the exact closed
forms `11√3π/108, 2π²/27, 1081√3π³/21870, 98π⁴/729` to **40+ digits**; the
cross-fit trust gate certifies **12 orders** (κ₁ to 54 digits … κ₁₂ to 13).

## 2. Results

### 2a. ACTION — clean confirmation (positive result)

| estimator | value | vs `Vol/π = 0.646132` |
|---|---|---|
| ratio-slope fit `A = 1/slope` | `0.65567` | +1.5% |
| Aitken-accelerated `A_n` | `0.644297` | **−0.28%** |
| Borel–Padé leading pole | `+0.671` (real, `arg = 0`) | +3.9% |

`A_n = n·κ_n/κ_{n+1}` rises **monotonically** `0.551 → 0.608 → … → 0.642` toward
`Vol/π`, and every Borel–Padé pole is **real positive** (`0.671, 0.793, 1.13, …`).

**This sharpens the corpus.** The leading Borel singularity is a **single, real,
positive** one at `Vol(4₁)/π` — **not** the complex conjugate pair the 6-order
2026-07-07 audit tentatively inferred. That apparent oscillation
(`0.76, 0.55, 0.61, …`) was a **two-term low-order transient**; from `n = 2`
onward the sequence is monotone. Scope-(a): the "action complex / oscillating /
preliminary" reading is **re-scoped** to "action = Vol/π, real, confirmed to
~0.3%".

### 2b. AMPLITUDE (Stokes constant) — honest negative

With `A = Vol/π` fixed and `β = 0.238` (fit), the large-order amplitude
Aitken-accelerates to

$$2\pi P \;\to\; 0.9952 \;\approx\; 1, \qquad P \to 0.1584,$$

and **no** natural normalization (`2πP`, `P`, `P·2π`, `2πP/2π`) lands within 3%
of the integer **3**. So the naive large-order route does **not** independently
reproduce the GGM `3` from 12 real `κ_n`.

This is consistent with — and independently re-derives from the perturbative side
— the standing corpus position ([`2026-07-18-g3-stokes-keystone` §2](2026-07-18-g3-stokes-keystone-evidence-base.md)):
*"the derivation route is the exact GGM state-integral / 3d-index algebra, not
float extraction from finitely many rungs."* The amplitude the large-order growth
measures is the residue of the leading Borel singularity in the cumulant
normalization; matching it to the state-integral Stokes-matrix entry `3` requires
the full GGM normalization, which finitely many `κ_n` do not supply.

## 3. Verdict

**Honest split result.**

1. **ACTION = Vol(4₁)/π: independently confirmed and sharpened** (single real
   positive Borel singularity, ~0.3%, monotone — the tentative conjugate-pair
   reading is re-scoped away, scope-(a)). A clean positive.
2. **AMPLITUDE = 3: NOT reproduced** by the naive large-order route (it gives
   `2πP ≈ 1`, O(1) but not 3). `A_ω = 3` stays the **GGM state-integral algebraic**
   value — cross-checked in *structure* (right action, right order of magnitude)
   but **not re-derived** as an integer from 12 real `κ_n`. Entropy-limited, as
   the corpus predicted.
3. **Q_β connection:** none wired. The amplitude does not land on `3` (let alone
   the `[3]_q`/`c_3` neighborhood), so there is nothing to over-claim; no `c_k`,
   no `SDeformedVolumeChannel`, no production change.

The exact `A_ω = 3` is **not** refuted — it remains the correct GGM value; what is
shown is that the *large-order amplitude route alone* does not pin it, isolating
the remaining work to the state-integral normalization.

## 4. Lean

[`Stokes3LargeOrderAmplitude.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/Stokes3LargeOrderAmplitude.lean)
(sorry-free): the extraction machinery `amplitude_extraction_single`; the
conjugate-pair envelope bound `cos_envelope` (the case the data **ruled out**);
and the open content-bearing carrier `GeometricKappaAction` (the
numerically-confirmed-but-unproved action limit `n·κ_n/κ_{n+1} → A = Vol/π`, **no
instance ⇒ open**) with the conditional consequence `action_recip_tendsto`
(inverts the action limit — a genuine derivation). The amplitude `= 3` is
**deliberately not asserted** in Lean (the probe refutes it at the naive
normalization).

## Cross-references

- Algebraic A_ω=3: [`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py); [`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean)
- Action (prior, complex/preliminary — now sharpened): [`2026-07-07-fmap-resurgence-action-and-pion-knot.md`](2026-07-07-fmap-resurgence-action-and-pion-knot.md)
- κ-tower exact closed forms: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md)
- Framing (even/odd A_ω, keystone): [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
- Per-winding Stokes family: [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md)
- κ_n ≠ c_k (perturbative, merged #4488): [`OhtsukiKappaVsCkSign.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/OhtsukiKappaVsCkSign.lean)
