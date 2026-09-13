---
# qou-46ys
title: 'MIGRATION NOT DONE: the binding/mass channel is still convention C while the decay channel is on D'
status: completed
type: task
priority: high
created_at: 2026-09-12T19:04:20Z
updated_at: 2026-09-12T20:15:27Z
---

**What is wrong.** The owner ruled convention D canonical on 2026-08-15 and
excised C. The **decay** channel has been migrated (`z_D` now scores Q_β). The
**binding / mass** channel has not, and says so in its own source.

**Primary evidence, not inference.**
[`computations/gap_a3_overshoot_robustness_check.py`](../computations/gap_a3_overshoot_robustness_check.py)
lines 52-67, its own comments, twice:

> `TRM` is CONVENTION C. `TRM["D"] = 0.38835725751524` is the convention-C
> deuteron `|tr_M|`; under the canonical convention D the same quantity is
> [different] … Convention C was excised 2026-08-09 … **Re-deriving is
> authorial work** and is [not done here]

and at line 67: *"tr_M(β_K) from the #2635 run (`y_lambda_at` q₀ + `chi_all_lambda`)
— **CONVENTION C**"*.

**Why this is the most exposed channel, measured.** `z` is not a separate knob —
**it *is* the `y_λ`**, at step ⑥ of the canonical chain (the Frobenius pairing
`tr_M = Σ_λ y_λ χ_λ`). Binding is the *same* pairing,
`B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` over partitions of `n = 3A`, and convention D sets
`y_λ = 0` for every `ℓ(λ) ≥ 3`:

| A | n = 3A | partitions | ≤2 rows | **killed** | fraction of dim kept |
|---|---|---|---|---|---|
| 1 | 3 | 3 | 2 | 1 | 83.3 % |
| 2 | 6 | 11 | 4 | 7 | 18.3 % |
| 3 | 9 | 30 | 5 | 25 | 1.34 % |
| 4 | 12 | 77 | 7 | 70 | **0.0434 %** |
| 5 | 15 | 176 | 8 | 168 | **7.41e-6** |

At ⁴He, D keeps **7 of 77 blocks**. So the open binding-magnitude problem — the
"separate super-pairwise additive extensive object" of the `Δ_λ` gate — is being
attacked with weights that under the canonical convention are almost all zero,
while the code computing them is still on C. **No bean recorded that before this
one.** (The `Δ_λ` half is settled and unaffected:
`Δ_λ = (−1)^{n(λ)}·dim V_λ`, sorry-free, general `n`.)

**Normalisation is NOT the issue** — `Σ_λ y_λ f^λ = 1.0` exactly under D at
n = 3, 6, 9, 12 (`qbeta_zd_gap_anatomy_probe`, worst |·−1| < 1e-50). Do not spend
a session on that hypothesis; it is refuted.

**Scope of the work, and it is real.** The file itself calls re-deriving
"authorial work" — a `z`-swap is *not* valid (`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`,
sorry-free, makes the C-frame ladder and the three-row forcing mutually
exclusive). So this is a re-derivation, not a substitution.

**Two acceptable outcomes, and the cheap one is legitimate:**
1. Re-derive the binding `tr_M` under D. Large, authorial.
2. **Scope every figure the binding channel publishes as C-conditional**, the way
   the `c_k` ladder already is. Cheap, honest, and it stops the straddle being
   invisible — which is the actual present harm.

Nobody owns this. Full analysis:
`docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §4 and §5(b).


## 2026-09-12 — MIGRATED. And the A3-overshoot trend DOES NOT SURVIVE it.

**The migration was cheap, not "authorial work".** The file's own banner said
re-deriving under D is authorial and didn't do it. The convention-D values at the
proton pin were **already committed** in
`canonical-mass-table-extended.witness.json` (`q0Anchor: proton`, nine nuclides,
computed 2026-09-07). So it is a **read**, and it fixes convention *and* anchor
at once. `gap_a3_overshoot_robustness_check.py` now reads by `(Z,N)` instead of
hardcoding C literals, and `Q0` comes from the table's `q0Value`.

**Rederived independently before being trusted.** `tr_M = Σ_λ y_λ χ_λ`, and the
`χ_λ` are representation characters — **independent of the Markov parameter**, so
only `y_λ` carries the convention. (The swap *is* legitimate here, unlike the
`c_k` ladder, whose offset mixes bar-weights — so `decayLadder_zC_threeRow_ne_zero`
does not apply.) Recomputing from the committed 50-digit `χ_λ` in
`atom-chi-rust-{d,3he,4he}` against `y_λ^D = [n−2k+1]_q/[2]_q^n` (ℓ(λ) ≤ 2, else
0) reproduces the table **exactly** for all three: `0.1519683392042316` /
`0.05859625365443638` / `0.01123741765976742`. Both live `y_λ` implementations
(`y_lambda_su_n`, `regenerate_chi_atom_conventionD.y_lambda`) agree to 60 dps, so
there is no second convention-D weight in the corpus.

### The result is NEGATIVE

| | C (muon) | **D (proton)** |
|---|---|---|
| O(D) | 2.050 | **0.8021** |
| O(³He) | 2.861 | **0.8116** |
| O(⁴He) | 3.364 | **0.6829** ← *below* ³He |
| D<³He bands disjoint | True | **False** |
| ³He<⁴He bands disjoint | True | **False** |
| flatten needs | −28 % / −39 % | **−1.17 % / +17.5 %** |

- **No overshoot**: every `O < 1` — an *undershoot*.
- **The A-trend inverts** at ⁴He, so there is no monotone atom-dependence to explain.
- **Flattening needs shifts inside the ±20 % knot-ID ambiguity the file itself cites** — its own robustness criterion, failed.

**The script was printing "ROBUST" unconditionally.** Three hardcoded blocks,
including a six-line VERDICT asserting *"the overshoot is EXACT"*, *"the GROWTH
with A is robust D→³He under every error model"*, *"the atom-dependence is REAL,
not a calibration artifact"*. All were the C-frame answer and printed regardless
of the computed table. **Every conclusion is now computed**, including against the
file's own ±20 % threshold.

**🛑 SCOPE-(a), NOT (b).** One pin, one convention, one knot/Vol assignment, one
error model. It refutes the trend **as computed here**. It does **not** prove no
atom-dependence exists.

**Trap, and it cost me a wrong conclusion first:** do **not** calibrate against
`docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md`,
which records the D deuteron as `0.5751`. That was correct on 2026-08-15 and is
**stale** — the table was regenerated at the proton pin and the value moved to
`0.15197`. Calibrating against it reads as a failure of a *correct* computation.

### What this bean does NOT close — successor work

`Vol_hyp` and `B_over_me` in that file are **unchanged C-era assignments**. So the
binding channel is migrated in its `tr_M` but **not in its knot assignment**; a
D-consistent knot assignment is `qou-e5jf`'s arc. A successor bean should carry
that, plus the wider sweep: this migrated the one file that *documented* its C
dependence, and `scripts/convention-c-value-audit.py` reports 85 confirmed
convention-C bindings in `computations/` (`qou-t9r1`).

PR #7235, commit `65401dce5bd`.


## 2026-09-12 (drain) — the SECOND producer, the sign flip, and both audits. PR #7236.

Reopened-in-spirit as a drain pass; the migration proper is above.

**`gap_a3_deuteron_A_D_overshoot.py`** — the matched pair of the file migrated in
#7235, same muon `Q0`, same C `TRM`. Migrated the same way (both constants from
`canonical-mass-table-extended.witness.json`). Both files now independently give
**0.8021**, so the pair stayed matched.

**THE SUBSTANTIVE FINDING: the required `P_λ` correction FLIPS SIGN.**

| | C (muon) | **D (proton)** |
|---|---|---|
| flat baseline vs deuteron binding | **overshoots** ×2.05 | **undershoots** ×0.8021 |
| required `P_λ` | **SUPPRESS** to 48.79 % | **ENHANCE** to 124.7 % |

**Any `P_λ` search inheriting the "suppression" framing is aimed the wrong way.**
The probe now prints that in its own output rather than leaving it to be inferred.

**Three more hardcoded claims, now computed.** The script printed
unconditionally: `"OVERSHOOT factor"`; *"the bar-even `P_λ` must **SUPPRESS** the
effective trace to ~124.7 % of flat"* (suppression to 124.7 % is not
suppression); *"the flat baseline **OVERSHOOTS** … by ~0.8021×"*; and
*"consistent with **EXACTLY 2** … Reporting ≈2.05"*.

**🛑 The header's "48 %" warning is on a stale figure AND points the wrong way.**
It says substituting the live value "would **inflate** the overshoot by 48 %" —
that 48 % is the ratio to `0.5751` (the 2026-08-15 `rho-k` audit's D deuteron,
correct then, stale now). The live value is `0.15197`, so migrating **deflates by
~2.56×**.

**Both A3 audits bannered SUPERSEDED** — kept as dated records per the `4.66e6`
precedent, but their *titles* asserted the refuted conclusion (*"the cross-atom
binding-overshoot trend is REAL"*, *"it GROWS with A"*) and a cold reader took
them as live. Each now opens with the C-vs-D table, the scope-(a) marker, the
`P_λ` sign note and the stale-`0.5751` trap. The producers had been migrated
while their own authority still asserted the old conclusion — the
"fixed in one place, survives in the others" failure.

**REMAINING, and it is the successor work:** `VOL_D` / `Vol_hyp` and `B/m_e` are
still **C-era assignments**, so both files are now **D in their trace and C in
their geometry**. A D-consistent knot/volume assignment is undone —
`qou-e5jf`'s arc. Coordinated to PR #7229 (end-to-end binding), which may consume
either.


## 2026-09-12 — 🛑 the "remaining straddle" this bean named DOES NOT EXIST. Correcting myself twice.

PR #7240. Probe
[`a3_vol_is_pseudovolume_not_convention_probe.py`](../computations/probes/a3_vol_is_pseudovolume_not_convention_probe.py)
(7/7). The entry above says *"`VOL_D` / `Vol_hyp` and `B/m_e` are still C-era
assignments … D in their trace and C in their geometry."* Both halves are wrong.

**(i) `B_OVER_ME` is not an assignment.** It is `|−B/m_e|` from the AME
**experimental** binding energies — the *comparison target*: `2.224566` /
`7.718058` / `28.295673` MeV over `m_e` reproduce the literals to <2.6e-4. It
carries no convention and never did. **Calling the measured side a modelling
assumption is the wrong direction of error** in a corpus whose point is keeping
the comparison boundary clean.

**(ii) `VOL` carries no Markov parameter.** SnapPy triangulation output on a
braid closure; nothing in it touches `z`. **So this bean's migration is
COMPLETE** — `tr_M` and `Q0` were the only convention-bearing inputs.

**(iii) But `VOL` is MISLABELLED `Vol_hyp`, and the corpus said so on
2026-05-19.** Per `2026-05-19-delta-lambda-thread-closure.md`: 12.776 / 12.554
are *"Not legitimate hyperbolic volumes (degenerate tetrahedra)"*, they are
*"SnapPy's pseudo-volume sum across the degenerate triangulation"*, *"NOT a
Mostow-rigidity-protected hyperbolic invariant"*. Four live producers carry the
wrong name. Λ-vs-Cl₂ class.

**(iv) And it is a DIFFERENT OBJECT from the `Vol` the owner retired.** The
2026-08-29 ruling retires `Vol(6₂) = 4.40083251612` and rules the closure flat
(`Vol = 0`). `VOL(D) = 12.776` is neither; `12.776/4.40083 = 2.9031`, not an
integer multiple. **The ruling does not reach this input** — but reading it beside
a variable named `Vol_hyp` says it does, and **I nearly concluded that.**

**SUCCESSOR, and it is a MODELLING call for the owner, not a migration:** is a
**Z-clustered pseudo-volume of a degenerate triangulation** the right geometric
input at all? `VOL(³He) == VOL(⁴He)` exactly while `VOL(D)` differs — clustering
by `Z`, not by knot — flagged in `2026-06-05-gap-a4-L1-retrospective.md` as
*"suggesting they are not the genuine Path B Vol(K)"*, still unresolved.

**It bears on the A3 refutation:** if `VOL` is the wrong input, the refuted trend
was computed on a wrong geometry *as well as* the wrong convention — which makes
the negative about the **route**, not only the frame.

Audit doc §6b + §7 item 2 updated:
[`2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`](../docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md).
