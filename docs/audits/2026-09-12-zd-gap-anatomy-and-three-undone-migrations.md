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

## 6c. 🛑 §3/§5(c) RESOLVED — with a NEGATIVE. `Δ^{(n)}` is not level-independent, and the tower factor names a hidden parameter

Added 2026-09-12. §5(c) closed `qou-y3bm` leaving **one** hypothesis isolated: is
`Δ^{(n)}` level-independent? **It is not — and the corpus already said so.**
[`brane-tower-q-laplacian-decay-proof.md`](../../content/quantum-observable-universe/observations/brane-tower-q-laplacian-decay-proof.md)
Step 3 states an **equality**, not a bound:

```
|⟨e_k, Δ^{(n)} e_k⟩| = (λ_k^{(q)})^n ,      λ_k^{(q)} = [k]_q² · ℏ_q / L_q²
```

So `Δ^{(n)}` is the **n-th iterate of the q-Laplacian**. `towerSum_of_const` is a
true theorem whose hypothesis this object does not satisfy — which is exactly what
isolating the hypothesis was for.

**The true sum is geometric in `ℏ_q²·λ_k`, not `ℏ_q²`**, and it equals the
implemented `1/(1−ℏ_q²)` **iff `λ_k = 1`**. At the leading mode `[1]_q = 1`, so that
pins

```
L_q = √ℏ_q = 0.314772482985
```

Three new sorry-free theorems in
[`TowerGeometricSum.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/TowerGeometricSum.lean)
(`lean`-direct exit 0, axioms `[propext, Classical.choice, Quot.sound]`):
`towerSum_iterated`, `towerSum_iterated_eq_simple_iff`, `leadingMode_lam_eq_one_iff`.
Probe:
[`qbeta_e0_tower_lq_dependence_probe.py`](../../computations/qbeta/qbeta_e0_tower_lq_dependence_probe.py)
(6/6).

**So `qbeta_e0.tower_summed` DOES carry a hidden parameter — now named and priced.**
`L_q` is the *q-deformed filament length*, a **free geometric scale**
(`fluid-dynamics/discrete-vortex-spectrum`; the Kelvin derivation takes `L_q = L`,
the period). The factor is a one-parameter family and the implemented value selects
one member:

| `L_q` | `λ₁` | tower factor | `E₀` (MeV) | vs implemented |
|---|---|---|---|---|
| **`√ℏ_q`  — implemented** | **1.0** | **1.00991452** | **4.22748336** | — |
| `1` (Kelvin `L_q = L`, `L = 1`) | 0.09908172 | 1.00097365 | 4.19005705 | **−0.8853 %** |
| `ℏ_q` | 10.0926795 | 1.10997858 | 4.64634966 | **+9.908 %** |
| `q − 1/q` ( = `h`) | 2.26699408 | 1.02276209 | 4.28126303 | **+1.272 %** |

**The choice of `L_q` is not a detail — it IS the effect.** The widest sampled
departure is **9.908 %** against a *total* tower correction of **0.9915 %**.
Convergence is not the issue (the divergence threshold is `L_q ≤ √(ℏ_q³) =
0.0311882`, far below every plausible value); the **value** is.

**🛑 And the tempting move is forbidden.** Picking `L_q = √ℏ_q` *because it
reproduces the current `E₀`* is the selection-against-the-target the anti-fit
directive forbids, one level up from the cell-ranking case in §2. Whether
`√ℏ_q` is the right filament length is a **modelling question for the owner**.
`qbeta_e0` is untouched by this probe.

## 7. What a next agent should do, in order

1. **`qou-wfvl`** — put the element decision to the owner once #7212 lands. Highest value; subsumes the accuracy question.
2. ~~**`qou-46ys`** — migrate the binding/mass channel off convention C~~ **DONE**
   (#7235, #7236 merged). The A3 overshoot **did not survive** it, and the
   "remaining straddle" this list first named **does not exist** — see §6b. What
   replaces it: the `Vol_hyp` **mislabelling** in four producers, and the open
   modelling question of whether a Z-clustered pseudo-volume is the right
   geometric input (owner call, not a migration).
3. ~~**`qou-y3bm`** — derive the tower series~~ **DONE, then RESOLVED NEGATIVELY**
   (§5(c) then §6c). The series is derived; its one remaining hypothesis is
   **false**, and the factor instead pins `L_q = √ℏ_q` — a free scale. What
   replaces it is an **owner modelling call**, not agent work: is `√ℏ_q` the right
   q-deformed filament length? The choice moves `E₀` by up to 9.9 % against a
   0.99 % total correction.
4. **`qou-pdix`** — the `α` eigenphase carrier. This is the REAL blocker: no
   ladder can be rederived on the `z_D` base without it, so it gates item 5.
   **Attack B (the Faddeev modular double) is now pruned — see §8**, which also
   splits route 5 and hands you a two-sided bracket on the carrier's steepness.
   The live target is the step-② holonomy; measure its log-slope against 2.176
   before attempting a closed form.
5. **`qou-iagg`** — the second dashboard re-score, once a ladder exists on the
   `z_D` base. Blocked behind `qou-pdix`, and that is a genuine dependency.

**Do not** rank routes by residual to choose among them (§2 is exactly why), and **do not**
quote the 337 429× (§1).

## 8. The ladder blocker itself — attack B on `qou-pdix`, and route 5 SPLITS

§1's decomposition put **1312×** of the Q_β miss on the *missing ladder* and 257×
on the functional. The ladder cannot be rederived on the `z_D` base until
`qou-pdix` — the `α` eigenphase carrier — has one, so `qou-pdix` is the real
blocker behind item 4 of §7, and `qou-iagg` sits behind it as a genuine
dependency rather than a scheduling accident.

`qou-pdix`'s route table has one survivor, **route 5 (a transcendental
construction)**: the required phase is transcendental over `ℤ[q,q⁻¹]`, which
closes routes 2–4 in one stroke, and route 1 was already pruned numerically.
Route 5 named four candidates — *"a q-exponential, Faddeev's `Φ_q`, a
holonomy/monodromy, a matrix exponential"*. **Attack B tested the second.**

### 8.1 Two independent negatives

**B1 — inversion-as-a-bridge is EXCLUDED, scope-(b), with a proved invariant.**
The mechanism was that `Φ_b`'s modular duality `b ↦ 1/b` (with `q = exp(iπb²)`,
`q̃ = exp(iπ/b²)`) carries the fibre-level `|q| = 1` elliptic regime, where an
eigenphase is natural, over to the real `q > 1` substrate where the ladder is
evaluated. But the two regimes are cut out by

| regime | condition on `b²` |
|---|---|
| fibre / elliptic, `\|q\| = 1` | `b²` **real** (`arg b = 0`) |
| substrate, `q` real positive | `b²` **imaginary** (`arg b = π/4`) |

and `z ↦ 1/z` fixes **both** the real axis and the imaginary axis setwise. Each
locus maps into itself; neither is reachable from the other. Six sorry-free
theorems in `QOU/QBeta/ModularDoubleLocusSeparation.lean`
(`modular_cannot_bridge` and its symmetric twin being the payload;
`loci_inter_eq_zero` rules out passing through a shared point, since the loci
meet only at `b² = 0` and `FaddeevPhi.hb`'s `0 < Re b` excludes it).

**The separation is the corpus's own.** `FaddeevPhi`'s class docstring already
draws this line and records that only one side is discharged — *"on the
`Im b² > 0` substrate branch this is discharged by the modular-double product …
the `|q| = 1` fibre regime, real `b`, remains open."* Worth flagging as a trap:
`hb : 0 < b.re` reads like a mild positivity hypothesis and is in fact what keeps
the two branches apart.

**B2 — `q̃` as a carrier is pruned on the ladder's SECOND target number,
scope-(a).** This is the finding that generalises. The required phase is pinned
by two numbers, not one:

```
P(q0)       = 1.997259194490263    (± 5.7e-7 relative)
|P'/P|(q0)  = 2.176                (~4 figures)
```

`q̃ = exp(±π²/ln q)`, so `|d ln q̃/dq| = π²/(q ln²q) = 816.73` at `q₀`:

| candidate | `\|P'/P\|(q₀)` | verdict |
|---|---|---|
| `[2]_q` | 0.0937 | 23.2× too flat |
| `2 − 3h⁴` | 0.0996 | 21.8× too flat |
| `χ^(2,1)(𝓑₃)` | 0.1018 | 21.4× too flat |
| `tr M_4_1` | 1.7363 | 1.25× too flat |
| **target** | **2.176** | — |
| **`q̃` (modular dual)** | **816.73** | **375.3× too STEEP** |

**So the target is bracketed: `1.7363 < 2.176 < 816.73`.** The declared Laurent
forms are all too flat; the modular-dual scale is far too steep. Branch-independent
— the two `arg b` branches flip the sign of `ln q̃`, not the slope — so this is a
fact about the modular-dual *scale*, not a convention choice.

That bracket is **reusable**: it says the carrier's steepness is *intermediate*,
which is a positive constraint on route 5 rather than one more exclusion.

### 8.2 Route 5 splits, and `Φ_b` is NOT pruned

```
5a  modular-double / q~ family ...... PRUNED (B1 mechanism, B2 magnitude)
5b  holonomy / monodromy family ..... OPEN — unchanged, and it IS branch 3
```

Per *Before declaring "refuted"*, the scope-(b) exclusion must not over-narrow.
`Φ_b`'s `b`-shift relation `Φ(z − ib/2) = (1 + exp(2πbz))·Φ(z + ib/2)` carries no
`exp(−1/t)` non-perturbative scale at all — its prefactor is an ordinary
exponential in `z` — so B2's overshoot does not touch it. `Φ_b` stays a live
transcendental **ingredient** for 5b. What is excluded is the *inversion* as a
bridge and `q̃` as a *carrier*.

**And the obvious next move is a fit, so it is named rather than taken:** the
shift prefactor's log-slope in `q` depends on `z`, so `z` is a dial that could be
set to hit 2.176. That is selection against the target, banned outright by
§NO FITTING. `z` has to come out of the braiding.

### 8.3 The most useful output is a pointer, not a prune

Branch 3 / 5b is the Kohno–Drinfeld / KZ picture — and `qou-pdix`'s own
2026-08-22 entry already noted that **the canonical chain invokes exactly that
shape at step ②, "Yekutieli non-abelian Stokes."** With the bracket, the target
for the next agent is much narrower than "derive `α`":

- the carrier is a **holonomy** of the step-② connection — not a character value
  (excluded by rationality) and not a modular-dual scale (excluded by B1/B2);
- it must land at `P(q₀) = 1.99726` with `|P'/P| = 2.176`, i.e. **intermediate
  steepness**;
- `z`, or whatever plays its role, must be **derived** from the braiding.

**🛑 That next step, as first written here, was NOT RUNNABLE — corrected the
same day, and the correction is the finding.** This section closed with *"compute
the holonomy log-slope of the step-② non-abelian Stokes connection at `q₀`"*.
**There is no constructed step-② connection.** Verified at the Lean rather than
from the cheat sheet, whose own §2a warns that its status column was the thing
that was wrong:

- `QOU.Mass.HeckeStokes.stokes_curvature_factors` is
  `X² − (q − 1/q)X − 1 = (X − q)(X + 1/q)`, discharged by `field_simp; ring` over
  a generic field. Sound, and it is where the two Hecke eigenvalues come from —
  but it is an algebraic factorisation. No connection, no curvature form, no
  surface, no multiplicative integral.
- The curvature reading lives in a **docstring** in `NaStokesKeystone.lean`: the
  2-form is *stipulated* to be the Hecke quadratic, so imposing flatness recovers
  it tautologically. AGENTS.md *Derive-then-check* item 8 verbatim — if it is
  true by `ring`, it is notation.

So "take its holonomy" presupposes exactly step ②'s acknowledged scope-(a) gap.

### 8.4 What IS measurable, and it is flat — the `lw` period ladder

`NaStokesKeystone.lean` carries more than the stipulation: a content-bearing §3b
class whose open core is a genuine **period**, `aD(c+1) = lw c` with
`lw c = (1/(c+1))·Σ_{λ⊢c+1} dim_q V_λ`, and it states closed forms as hypotheses
to a sorry-free conditional theorem. Measured at the proton pin against the
ladder's **second** target number:

| step-② object | value | `\|d ln f/dq\|` | vs 2.176 |
|---|---|---|---|
| `lw 1 = 1` | 1 | 0 | constant |
| `lw 2 = (q+1)²/(3q)` | 1.33696562 | 0.046958636 | **46.3× too flat** |
| `lw 3 = (3q²+4+3/q²)/4` | 2.53277966 | 0.22430586 | **9.70× too flat** |
| `tauOf` | 2.64238631 | 0.11385448 | **19.1× too flat** |
| `2χ^(2,1)/[2]_q` | 1.983379502 | 0.1954502 | **11.1× too flat** |

**Per-rep normalisation does not escape it, and that is the sharpest line here.**
The corpus's standing claim is that the carrier is the per-rep q-Reeb phase
`θ_λ = arccos(χ^λ/d_λ)` and that the scalar `tr_M` *collapses* it — which
predicts the per-rep object should behave differently from the average. It does
move: dividing by `d_λ` takes the slope `0.1018 → 0.1955`, a factor 1.92. It is
still **11.1× short**. So **the collapse is not what costs the slope.**

**The value-only trap, caught explicitly.** `λ = (3)` and `λ = (1³)` have
`d_λ = 1` and `χ = 1` on the Borromean, so `2χ/d = 2` **exactly** — 0.137 % from
the target *value*, better than most of the declared basket — with slope
identically **zero**. A value-only comparison would promote them; the second
target number rejects them outright. This is why §D's two-number target matters.

**Calibrated, not self-consistent:** the probe's central-difference method
reproduces the bean's independently-recorded bare-`χ^(2,1)` entry `0.1018` as
`0.101787393` (rel 1.2e-4).

**Scope (a), and conditional.** These *declared* forms lack the steepness; no
proved invariant forbids a holonomy of a genuinely derived connection, and there
is simply none in the corpus to test. And that `lw` **is** the step-② period is
the unproved keystone class — assumed in the measurement, not shown
(*conditional-proved ≠ premise-established*).

### 8.5 The bracket is now a SPECIFICATION, not a list of exclusions

```
step-2 / Laurent family   0.047 .. 0.224      9.7x - 46x TOO FLAT
best declared basket      1.7363              1.25x too flat
TARGET                    2.176                 --
modular dual q~         816.73                375x TOO STEEP
```

Both sides are real corpus objects and the middle is empty. The flatness is not
bad luck in which forms were tried: a low-degree rational in `q` at `q₀ ≈ 1.11`
**cannot** be steep, and a non-perturbative `exp(−1/t)` **cannot** be shallow. So
the carrier must be an **intermediate transcendental** — which is what an ordered
exponential (a real holonomy) supplies and a polynomial average cannot.

**That is why the stipulated curvature is the blocker rather than a bookkeeping
complaint: 5b needs step ② CONSTRUCTED, not stipulated.** The honest next step is
therefore step ②'s own gap — a multiplicative-integral construction whose
curvature is *computed* to be `σ² − (q−q⁻¹)σ − 1`, or an honest §3b restatement
with the geometric step as hypothesis — not another candidate-form sweep.

Probe: `computations/qbeta/qbeta_pdix_step2_holonomy_slope_probe.py` (7/7).

`qou-pdix` remains **OPEN**. Attack B removed two candidate mechanisms and left
the gap where it was. PR #7252; probe
`computations/qbeta/qbeta_pdix_modular_double_locus_probe.py` (13/13).
