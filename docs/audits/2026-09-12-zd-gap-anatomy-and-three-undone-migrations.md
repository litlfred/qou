# The z_D Q_β gap: anatomy, and three migrations the 2026-09-08 ruling did not get

**Date** 2026-09-12 · **Beans** `qou-99qc` (parent), `qou-iagg`, `qou-46ys`, `qou-y3bm`, `qou-wfvl`
**Probes** [`qbeta_zd_gap_anatomy_probe.py`](../../computations/qbeta/qbeta_zd_gap_anatomy_probe.py) (9/9),
[`qbeta_zd_rescore_price_probe.py`](../../computations/qbeta/qbeta_zd_rescore_price_probe.py) (8/8)
**PR** #7221

## Read this first if you are picking this up cold

The owner ruled on 2026-09-08 that `ε` in `Q_β = |ε(Δ)|·E₀` is the **Markov trace at
`z_D = q³/(q²+1)`** (convention D, the two-row truncation — D7). On 2026-09-12 the owner
authorised re-scoring the L2 dashboard rows `Q_β` / `m_n` / `Δ_pn` onto that base, which
degraded them by ~5–7 orders of magnitude. The owner then asked the load-bearing question:
*is that real, or did some other migration not happen?*

**Both.** The gap is structural and honest; **and** three migrations are outstanding, one of
them large. This document is the answer, with the measurements.

## 1. The headline number was quoted against the wrong baseline — including by me

The re-score PR's own table put **1279 ppb** beside **4.316e+8 ppb**, an apparent 337 429×.
That comparison is forbidden by the corpus's own admissibility note (*"🛑 COMPARE BASE TO
BASE, and do not relate either to the 1279 ppb scored here"*) and I made it anyway. It is
two factors:

| factor | what it is |
|---|---|
| **1312×** | the **missing `c_k` ladder** — `z = 1` base 1 678 440 ppb → `z = 1` published 1279 ppb |
| **257×** | the **functional** — `z = 1` base 1 678 440 ppb → `z_D` base 4.3157e+8 ppb |

So **most of the degradation is "no ladder has been derived on an admissible base yet"**
(`qou-cds1`, blocked on the phase `qou-pdix`), not convention D. Base to base, D costs 257×.
Never quote the 337 429×.

## 2. The gap is structural, not a botched substitution

`tr^z(Δ_S)` rewrites **exactly** — verified to 1e-60 against the 2026-08-29 audit's affine form:

```
tr^z(Δ_S) = h²/2 − z·h          h = q − 1/q = 0.2090603
h²/2 = 0.0218531                z·h at z_D = 0.1280870
```

The `z` term dominates the `z`-independent term by **5.86×**, so `Q_β` is nearly
**proportional to `z`**. Inverting for CODATA:

| | `z` | distance from `z*` |
|---|---|---|
| **`z*` reproducing CODATA** | **0.99850030** | — |
| `z = 1` — the published cell | 1.0 | **0.15 %** · **INADMISSIBLE** |
| `z = q` (augmentation) | 1.10998 | +11.17 % |
| **`z_D` (ruled)** | 0.61269 | **−38.64 %** |

**The published 0.168 % was reachable only within 0.15 % of `z = 1`**, the coordinate sum,
which `ConventionDAdmissibleRoots.lean` (sorry-free) excludes. So the old agreement was a
property of an inadmissible functional, not of the framework — and with *this element* no
admissible `z` can reproduce CODATA. That is the bean's already-measured *"20 required
levels, **zero** within 1e-3 of an admissible one."*

**Scope-(a), not (b):** this excludes `Δ_S` **paired with an admissible functional**. It
excludes neither convention D nor the framework.

## 3. The missing-normalisation hypothesis is REFUTED

The leading alternative was that the normalised trace carries a `z`-dependent factor that
was not migrated, making `|tr^z(Δ)|·E₀` with fixed `E₀` an apples-to-oranges comparison.
Measured: under D, `y_λ = [n−2k+1]_q / [2]_q^n` for `ℓ(λ) ≤ 2` and `0` for `ℓ(λ) ≥ 3`, and

```
Σ_λ y_λ · f^λ  =  1.0   exactly, at n = 3, 6, 9, 12   (worst |·−1| < 1e-50)
```

so `tr(1) = 1` in both conventions and there is no hidden normalisation. Recorded because
it is the hypothesis a next agent will reach for first.

## 4. Where the convention enters BINDING — and this is the part nobody has propagated

`z` is not a separate knob. **It *is* the `y_λ`**, at step ⑥ of the canonical chain:

```
substrate q₀ → 𝐂 categorical action → Yekutieli Stokes → 𝐇_n(q) Hecke
  → Wedderburn (partitions λ ⊢ n)
  → ⑥ Frobenius pairing  tr_M = Σ_λ y_λ χ_λ      ← THE CONVENTION LIVES HERE
  → confinement SDP → canonical T_w → Archimedean functor at q₀ → MeV
```

Binding is the **same pairing**: `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` over partitions of
`n = 3A`. So D's two-row truncation lands directly on it:

| A | n = 3A | partitions | ≤2 rows | **killed** | fraction of dimension kept |
|---|---|---|---|---|---|
| 1 | 3 | 3 | 2 | 1 | 83.3 % |
| 2 | 6 | 11 | 4 | 7 | 18.3 % |
| 3 | 9 | 30 | 5 | 25 | 1.34 % |
| 4 | 12 | 77 | 7 | 70 | **0.0434 %** |
| 5 | 15 | 176 | 8 | 168 | **7.41e-6** |

At ⁴He convention D keeps **7 of 77 blocks and 0.043 % of the Wedderburn dimension**. The
`Δ_λ` half is settled (`Δ_λ = (−1)^{n(λ)}·dim V_λ`, sorry-free, general `n`); it is the
`y_λ` half the ruling moves. **The open binding-magnitude problem — the "separate
super-pairwise additive extensive object" — is being attacked with weights that under D are
almost all zero, and no bean recorded that before this one.**

## 5. The three undone migrations

### (a) The ELEMENT is census-derived, and the owner's own ruling forbids that — `qou-wfvl`

`Δ_S` is the short-NF element. **The same day** as the `ε` ruling, the owner ruled
(`qou-ales`, 2026-09-08) that *"All selection of great words should be done through gamma
gamma production and the semi-definite product solutions at q₀. Shouldn't use census."*
The functional was migrated; the element it acts on was not. PR #7212 (open) shows the
γγ-selected nucleon word gives **−17.496 %** — **2.5× better than `Δ_S`'s −43.157 %, and
derived rather than selected.** The four candidates at level 2 = `z_D`:

| candidate Δ | level-2 residual | provenance |
|---|---|---|
| `delta_S` short NF | −43.157 % | NF/census · **what the dashboard scores** |
| nuc9 `build_nucleon_nf` | −30.936 % | census |
| **nuc11 interleaved** | **−17.496 %** | **γγ-selected (#7212)** |
| nuc11 gen-grouped | −15.451 % | census, γγ-excluded |

**This is the largest outstanding item and it subsumes the `Q_β` accuracy question.** It is
an owner decision because changing the scored element is neither a precision increase nor
corpus-derived while #7212 is open.

### (b) The BINDING/MASS channel is still convention C — `qou-46ys`

[`gap_a3_overshoot_robustness_check.py`](../../computations/gap_a3_overshoot_robustness_check.py)
says so in its own comments, twice: *"`TRM` is CONVENTION C … under the canonical convention
D the same quantity is [different] … Re-deriving is authorial work."* So **the decay channel
is on D and the binding channel is on C** — a live straddle across the ruling, in the
channel §4 shows is the most exposed to it. Nobody owns this.

### (c) `E₀` had two live forms — **unified 2026-09-12 on owner instruction**

| form | value | where |
|---|---|---|
| order-zero `m_e/(q(q−1))` | 4.18598136 MeV | most call sites, incl. the dashboard |
| tower-summed `… /(1−ℏ_q²)` | 4.22748336 MeV | `qbeta_bar_branch_refuted_probe.py:88`, *"tower-summed, as ruled"* |

Ratio **1.00991452 (+0.9915 %)**, with no signal at either call site. Unified in
[`qbeta_e0.py`](../../computations/qbeta/qbeta_e0.py); **tower-summed is canonical** per the
2026-09-03 full-tower ruling, and the dashboard now routes through it (rows became
4.259e+8 / 3.547e+5 / 2.576e+8 ppb).

**🛑 The tower SERIES is not derived.** That the tower sum is `Σ_{k≥0} ℏ_q^{2k} = 1/(1−ℏ_q²)`
is taken from that one precedent. I did not find a derivation and did not construct one —
inventing it would be laundering. Canonical **by ruling**, open **by proof**: `qou-y3bm`.

## 6. A guard that fired, and the lesson in it

Routing the dashboard onto the tower `E₀` **silently reverted the whole `Q_β` row to the
retired `z = 1` cell.** Cause: the re-score calibrates against the probe witness's recorded
`−43.157175 %`, which was computed at **order-zero** `E₀`, so the +0.99 % shift broke the
comparison, `calibrated` went `False`, and the producer correctly published the old row
rather than a number it could not verify.

The guard did its job. **The calibration was asking the wrong question** — it conflated
"is my trace right?" with "which `E₀` is canonical?". Fixed by calibrating the trace at the
`E₀` the recorded cell used, then publishing at the canonical `E₀`: one check per claim.
Worth internalising, because the failure mode is a *silent revert*, not an error.

## 6b. 🛑 CORRECTION to §5(b)'s "remaining straddle" — it does not exist, and the real defect is different

Added 2026-09-12, after the migration landed. Reporting the binding migration I
wrote that *"`Vol_hyp` and `B/m_e` remain C-era assignments, so the files are D in
their trace and C in their geometry"*. **Both halves are wrong.** Probe:
[`a3_vol_is_pseudovolume_not_convention_probe.py`](../../computations/probes/a3_vol_is_pseudovolume_not_convention_probe.py)
(7/7), witness `a3-vol-is-pseudovolume-not-convention.witness.json`.

**(i) `B_OVER_ME` is not an assignment at all.** It is `|−B/m_e|` from the AME
**experimental** binding energies — the *comparison target*:

| | `B_exp` (MeV) | `B_exp/m_e` | literal in producer | rel |
|---|---|---|---|---|
| D | 2.224566 | 4.35336706 | 4.353 | 8.4e-5 |
| ³He | 7.718058 | 15.1038627 | 15.10 | 2.6e-4 |
| ⁴He | 28.295673 | 55.3732507 | 55.37 | 5.9e-5 |

It carries no convention and never did. In a corpus whose whole point is keeping
the comparison boundary clean, **calling the measured side a modelling assumption
is the wrong direction of error.**

**(ii) `VOL` carries no Markov parameter either.** It is a SnapPy triangulation
output on a braid closure; nothing in its derivation touches `z`. So **the binding
channel's convention migration is COMPLETE** — `tr_M` and `Q0` were the only
convention-bearing inputs and both are migrated. There is no "D in the trace, C in
the geometry".

**(iii) But `VOL` is MISLABELLED, and the corpus said so on 2026-05-19.** Four live
producers call it `Vol_hyp` / `VOL_HYP`
(`gap_a3_overshoot_robustness_check.py`, `gap_a3_deuteron_A_D_overshoot.py`,
`probes/gap_a3_plambda_bar_even_admissibility_probe.py`,
`probes/gap_a4_cross_isotope_residual_probe.py`). But
[`2026-05-19-delta-lambda-thread-closure.md`](2026-05-19-delta-lambda-thread-closure.md)
says of 12.776 / 12.554, verbatim:

> **Not legitimate hyperbolic volumes** (degenerate tetrahedra) … SnapPy's
> **pseudo-volume** sum across the degenerate triangulation … a combinatorial-braid
> invariant of the **simplification path**, NOT a Mostow-rigidity-protected
> hyperbolic invariant.

Same defect class as the **Λ-vs-Cl₂** trap this document's parent AGENTS.md records:
right number, wrong name, and **the wrong name invites the wrong inference.**

**(iv) And it is a DIFFERENT OBJECT from the `Vol` the owner retired.** The
2026-08-29 ruling retires `Vol(6₂) = 4.40083251612` (the census-assigned Bloch leg)
and rules the deuteron knot flat (`Vol = 0`). `VOL(D) = 12.776` is neither, and
`12.776 / 4.40083 = 2.9031` is not an integer multiple. **So that ruling does not
reach this input** — but an agent reading *"the deuteron binding is NOT a
hyperbolic-volume term"* beside a variable named `Vol_hyp` will conclude it does.
**I nearly did**, and stopping that inference is why this section exists.

**What is therefore still open, and it is NOT a convention question:** whether a
**Z-clustered pseudo-volume of a degenerate triangulation** is the right geometric
input at all. `VOL(³He) == VOL(⁴He)` exactly while `VOL(D)` differs — clustering by
`Z`, not by knot — which
[`2026-06-05-gap-a4-L1-retrospective.md`](2026-06-05-gap-a4-L1-retrospective.md)
already flagged as *"suggesting they're not the genuine Path B `Vol(K)`"*. That is
a **modelling question for the owner**, not a migration.

## 7. What a next agent should do, in order

1. **`qou-wfvl`** — put the element decision to the owner once #7212 lands. Highest value; subsumes the accuracy question.
2. ~~**`qou-46ys`** — migrate the binding/mass channel off convention C~~ **DONE**
   (#7235, #7236 merged). The A3 overshoot **did not survive** it, and the
   "remaining straddle" this list first named **does not exist** — see §6b. What
   replaces it: the `Vol_hyp` **mislabelling** in four producers, and the open
   modelling question of whether a Z-clustered pseudo-volume is the right
   geometric input (owner call, not a migration).
3. **`qou-y3bm`** — derive the tower series, or record that it is assumed wherever `E₀` is quoted.
4. **`qou-iagg`** — the second dashboard re-score, once a ladder exists on the `z_D` base.

**Do not** rank routes by residual to choose among them (§2 is exactly why), and **do not**
quote the 337 429× (§1).
