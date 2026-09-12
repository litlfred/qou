---
# qou-za3q
title: magnus-Omega2 probes call the Plancherel weight y_lambda; 91% of their work is on shapes tr_M annihilates
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T10:49:41Z
updated_at: 2026-09-12T03:55:51Z
parent: qou-x631
---

## What is there

`deltalambda/{deuteron,triton}_magnus_omega2_sign_probe.py` and
`he4_magnus_omega2_sign_sparse_probe.py` each define

    def wedderburn_weight(shape, q):
        """y_λ = d_q(λ)² / [n]_q!  (symmetric q-integers) — same as the A=2 probe."""

and aggregate `P_total = Σ_λ y_λ · tr(ρΩ₂)` over **every** partition. Fifteen
files under `computations/` compute this same form, `substrate/hecke_core.py`
among them.

That is the **quantum Plancherel** weight. It is not the Wenzl Schur principal
specialisation the production Markov trace uses, and the two are not close:

| | (3,) | (2,1) | (1,1,1) |
|---|---:|---:|---:|
| Wenzl y_λ (production) | 0.50540423 | 0.24729789 | **0** |
| d_q²/[n]_q! (these probes) | 0.16338323 | 0.66067377 | 0.16338323 |

At H₉ the divergence is structural, not a rescaling: Plancherel's **largest**
weights sit on shapes production annihilates — (4,3,1,1) and (4,2,2,1) at
0.1463 each, (5,2,1,1) at 0.1063, (4,3,2) at 0.0910 — while the five surviving
≤2-row shapes carry 0.0000017 to 0.0065. Under the Wenzl weight those same
≥3-row shapes are all exactly 0 (row cap, level r = 2; see `qou-fq0f`).

## What I am NOT claiming

That the weight is wrong. `computations/audits/y_lambda_convention_c_fingerprint_audit.py`
already states the row-cap test and flags precisely this trap:

> AGENTS.md is explicit that the three partition-weight families y_λ / w_λ /
> w̃_λ are DISTINCT at q ≠ 1 and must never be conflated, so a hit on a field
> that is not the Wenzl y_λ is a false positive this cannot rule out by itself.

`d_q²/[n]_q!` may well be the right pairing measure for a Magnus Ω₂ sign
question, which is not a Markov trace. I cannot settle that from here.

What IS wrong regardless is the **name**: these docstrings call it `y_λ`, and
the aggregation field in the witness is `y_lambda`. That is the conflation
AGENTS.md forbids, and it is what makes the fingerprint audit unable to
discriminate — it keys on a field *named* `y_lambda`, so these probes are
permanent false-positive candidates in a corpus-wide convention scan.

## Decision needed

1. **Is the Plancherel measure intended here?** If yes, rename it — `w_planch`
   or similar — in all three probes and the twelve other call sites, so the
   corpus has one name per object and the fingerprint audit stops tripping.
   If no, these three probes' results are computed against the wrong measure.
2. **Does the sign survive either way?** Both weight families are strictly
   positive, so a conclusion that is only about the SIGN of `P_total` may be
   robust to the choice. If so, the probes' headline claim stands while the
   naming is fixed — worth checking before treating this as urgent.

## Side finding: the same 91% waste, and a classification

`he4_magnus_omega2_sign_sparse_probe` dispatches over all 77 partitions of 12
and builds `sigma_csr`/`germ_csr` for each, at dimensions to d_λ = 7700. Under
the production weight 70 of those 77 carry weight exactly zero — the same waste
`qou-fq0f` removed from the Wenzl bridge (99.5x). It cannot be removed here
until item 1 is settled: with the Plancherel weight nothing vanishes, so there
is nothing to skip.

**Classification for `qou-hu1f`:** forced to the OLD `grouped` ordering, this
probe ran 33+ CPU-minutes without completing inside a 2700 s budget — the same
outcome it has under `borromean`. It does not complete either way, so its
failure is **pre-existing, not caused by the intra-ordering ruling.** That
closes the last undecided producer from the regeneration pass.

---

## 2026-09-07 — decision 2 answered by measurement; decision 1 fixed without a breaking rename

### The sign IS robust, and that was not automatic

Re-weighted each probe's **own committed** `tr_rho_Omega2` with
`y_lambda_wenzl_bridge_numeric` — the traces are shared rather than recomputed,
so the comparison isolates the weight family exactly:

| atom | partitions | Wenzl-nonzero | P_total (Plancherel) | P_total (Wenzl) | sign |
|---|---:|---:|---:|---:|:---:|
| deuteron | 11 | 4 | −15.095 | −6.921 | both − |
| triton | 30 | 5 | −108.147 | −59.991 | both − |
| ⁴He | 77 | 7 | −57.803 | −100.827 | both − |

The bean guessed this might be trivial because "both weight families are
strictly positive". It is not — that would only settle it if the traces shared
a sign, and they do not:

    atom      tr(ρΩ₂) > 0    < 0
    deuteron        4         5
    triton         13        15
    ⁴He            26        49

So the sum is a genuine cancellation, and re-weighting redistributes mass across
terms of both signs while zeroing 7/11, 25/30 and 70/77 of them outright. The
sign was free to flip and did not.

**So the probes' headline claim stands.** This is a naming defect, not a
results defect — which is what decision 2 asked.

### Magnitude is NOT robust, and not even monotonically

−15.1 → −6.9 and −108.1 → −60.0 shrink, but ⁴He goes the other way, −57.8 →
−100.8. Any conclusion drawn from `|P_total|` rather than its sign is still
weight-family dependent, and the direction of the shift is not predictable from
the atom. Recorded as a caveat on the new witness.

### Decision 1: the conflation is fixed, the rename is not the way

A field rename would break real readers — `magnus_sign_growth_analysis.py:115`
and `l1_ceiling_d_frame_remeasure.py:157` both do `mp.mpf(r["y_lambda"])`
against these exact witnesses, and there are ~8 further consumers of the
magnus-omega2 witnesses. So instead:

- the three docstrings that *asserted* `y_λ = d_q(λ)²/[n]_q!` now name it the
  quantum Plancherel measure and state, with the measured H₃ table, that it is
  **not** the Wenzl y_λ and why the two are not a rescaling;
- each witness gains `weight_family:
  "quantum_plancherel_dq2_over_n_factorial"` plus a note. The ambiguous column
  keeps its name so nothing breaks, but the object now declares what it is, so
  a corpus scan can discriminate on the declaration instead of guessing from a
  field name.

New probe carrying the measurement:
`computations/deltalambda/magnus_omega2_weight_family_robustness_probe.py`,
1/1 assertion.

### Still open — and this is decision 1's actual question

**Whether the Plancherel measure is the RIGHT pairing for a Magnus Ω₂ sign
question is NOT settled here.** The rename makes the corpus honest about which
object is in play; it does not choose the object. What the robustness result
buys is that the choice is not urgent: no published sign conclusion moves either
way.

---

## 2026-09-07 — decision 1: full analysis, options beaned

Analysis: [`docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md`](../docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md)

Three measurements settle what the earlier notes could only frame:

1. **`tr(1)` is the decisive discriminator.** Wenzl gives exactly **1.0** at
   n = 6, 9, 12. Plancherel gives **11.139 / 184.233 / 6751.541** — it is not a
   normalised trace, and its scale drifts ~600× from A=2 to A=4. Since the
   programme's target claim is a *sign change in A*, that drift makes any
   cross-A magnitude statement meaningless under Plancherel.
2. **The divergence is structural, and quantified.** Plancherel puts 81.8 % of
   its H₆ mass on ≥3-row shapes where the Wenzl cap puts 0 %; 62.4 % of the A=2
   |contribution| comes from shapes Wenzl annihilates. Under Wenzl the whole H₆
   signal is three 2-row shapes — and the largest Wenzl weight, (6,) at 0.45,
   contributes nothing, because a commutator vanishes on a 1-dimensional block.
3. **The probes' own control cannot discriminate.** `ρ=I ⇒ tr(Ω₂)=0` holds
   *blockwise* — every per-λ control trace is exactly 0 — so it is weight-blind.
   It is evidence for cyclicity and none at all for the weight choice. Worth
   knowing, because the docstrings present it as validating the setup.

**Recommendation: option A as headline + option C as a permanent guard.**

Options beaned:

| bean | option | verdict |
|---|---|---|
| `qou-q2q7` | A — adopt Wenzl | **recommended** (headline) |
| `qou-smvw` | C — report both | **recommended** (guard) |
| `qou-94yt` | B — keep Plancherel, justify | not recommended alone |
| `qou-ia4w` | D — normalise Plancherel | not recommended |
| `qou-gba1` | E — derive the pairing | worth doing; must not block A |

Safe either way: no published conclusion moves, because the sign is robust.

---

## 2026-09-07 (later) — CORRECTION: the sign is NOT robust at A=3

The robustness result recorded above is **wrong**, and the way it was wrong is
the point.

It re-weighted each sign probe's **committed** per-λ traces without checking
whether those traces were canonical. Two of three were not: triton's witness was
**2026-09-03** and ⁴He's is **2026-09-04**, both before the 2026-09-05 ordering
ruling. So it compared two contractions of a *superseded braid word* and
reported robustness on all three atoms.

Regenerating triton on the canonical word changed **28 of its 30**
per-partition traces. The only two unmoved are `(9,)` and `(1⁹)` — the
one-dimensional blocks, where a commutator vanishes regardless of ordering.
That is the ordering signature exactly.

| atom | source | P Plancherel | P Wenzl | agree? |
|---|---|---:|---:|:---:|
| deuteron | canonical | −15.095 | −6.921 | yes |
| triton | canonical | **+2.470** | **−13.931** | **no** |
| ⁴He | pre-ruling | −57.803 | −100.827 | undetermined |

**At A=3 the two weight families give opposite signs.** So the choice is not
cosmetic — it determines a published conclusion.

### Which strengthens the recommendation rather than weakening it

The answers are not symmetric. The programme's target is negative at A=2 and
**positive at A≥3**. Plancherel gives triton `+2.470` — the wanted sign. Wenzl
gives `−13.931` — the unwanted one.

That is a finding about the physics, not a reason to prefer Plancherel. The
standing rule here is no fitting, and choosing a weight family because it yields
the desired sign is exactly that. The honest reading: **under the principled
pairing the A=2 → A=3 sign change is not yet exhibited**, and ⁴He is needed
before even that is settled.

### The guard

`magnus_omega2_weight_family_robustness_probe.py` now reads each source's
`computedAt`, records `source_pre_ruling`, and **excludes** a pre-ruling source
from the gate instead of counting it as agreement — a stale source cannot
support a verdict either way, since both arms answer the wrong question.

Downstream corrections made: the analysis doc, the published artifact, and this
bean. `qou-q2q7` and `qou-smvw` inherit the change.

### Why this surfaced at all

Only because the perf work made triton runnable. It could not finish in 2400 s
before; profiling found the probes rebuilding 56 commutators per shape where 28
suffice, and at 3.35× it completed and exposed the stale witness.

### Open

- [ ] Regenerate `he4-magnus-omega2-sign.witness.json` (source 2026-09-04) —
      until then A=4 is undetermined and no cross-A sign-change claim can be
      made under either weight.

### ⁴He regeneration — 63/77 banked, not finished

Run with `--workers 4 --checkpoint`, both of which the probe already supported
and neither of which had been used — `--workers` **defaults to 1**, which is a
large part of why A=4 had never been regenerated.

    63 of 77 partitions in 90 minutes, then the budget expired.

Progress is banked in `.he4_magnus_progress.jsonl` (gitignored, per the
convention for the sibling checkpoints), so a resume needs only the remaining
14. Those are the expensive ones: the sweep runs smallest-first, and the largest
H₁₂ blocks reach d_λ = 7700 against d_λ = 2970 at the point it stopped. Cost
goes as roughly d², so the remainder is several hours, not minutes.

**A=4 therefore remains undetermined**, and no cross-A sign-change claim can be
made under either weight family until it lands.

Two things did come out of the attempt:

- **The multiplicity fold applies here too.** The ⁴He word gives 145 adjacent
  (i<j) pairs over 14 distinct keys, of which only **10** survive with a
  nonzero net coefficient under antisymmetry. Folded. Verified by the probe's
  own `--gate` (sparse vs dense across all 30 H₉ partitions) at rel diff
  **3.06e-60** — and that gate independently reproduced the regenerated
  canonical triton datum `+2.4701927083`, sign +1, which is a second confirmation
  of the sign flip from an implementation that shares no code with the dense path.
- **The sparse probe was already ahead of the dense ones** on the thing that
  matters most: it uses far-commutativity, `[A_a, A_b] = 0` for `|a−b| ≥ 2`,
  which `deuteron`/`triton` do not. Porting that to the dense probes is likely a
  further large win and is not done.

- [ ] Resume ⁴He (14 partitions, multi-hour) and re-run the robustness probe;
      only then is A=4 in play.
- [ ] Port far-commutativity from the sparse probe to the dense deuteron/triton
      probes.

## 2026-09-08 coordination: same kernel as qou-x631, qou-k5r5, qou-o6ov, qou-omr7

Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 1 / §7.3 C2: `k5r5` (99 commits, 08-21 → 09-08) and `o6ov` (99 commits, 08-30 → 09-05) both work the odd-moment / Magnus `tr(ρ_λ Ω₂)` kernel, and before this note there were **zero** cross-citations among k5r5 / o6ov / x631 / za3q / omr7 (measured 2026-09-08 by grepping each body for the other four ids). Shared ledger: epic `qou-x631`, now parent of the other four. Roles — x631: epic, Cov_Planch(f^λ, Σc²) ≤ 0 / T₃(k) kernel; k5r5: M₁ > 0 (first odd moment), all-n proof OPEN, identity Lean-proved; o6ov: does |tr(ρ_λ Ω₂)|/dim decay in b across the ≤2-row column (open mathematics, rescoped 2026-09-05, PR #6822); za3q: Magnus-Ω₂ probes use the Plancherel weight y_λ, 91 % of their work on shapes tr_M annihilates; omr7: Magnus probes' d_q was the hook product, weight inverted (4 files, PR #6442). Statuses are unchanged by this note; a result landing on any of the five should be cited in the other four.

## MEASURED 2026-09-08/11: A=4 = +34.126027, sign +1 — no flip at the alpha particle

77/77 partitions, max dim 7700, 28661s (8.0h) on 3 workers.
  P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
  sign +1, control (rho=I) = 0.0 vanishes True, split 33+/42-, sign_flip_vs_A3 = False

Sign map: A2 = -1, A3 = +1, A4 = +1. Exactly ONE sign change in A=2,3,4 and it
sits between the deuteron and the triton, NOT at the alpha particle.

Survived four session-boundary kills via per-partition checkpointing; the two
earlier attempts that did NOT survive used setsid/nohup (qou-6cm9). The dim-7700
partition (~3h on one worker, unbankable until complete) was expected to make A=4
unreachable. It landed.

scope-(a): dimensionless SIGN datum. NOT a MeV (Δ_λ gate open), NOT a physical
binding-sign assertion (qou-v7ro/#6077 cited, not re-derived). Per-partition
sign-indefinite.


## MEASURED 2026-09-12 (PR #7197): the A=2 -> A=3 sign change is a PLANCHEREL ARTIFACT

The checklist item `[ ] Resume 4He ... and re-run the robustness probe; only
then is A=4 in play` is now discharged in full. Its first half landed in #7179;
**this is the second half**, and it is the half that carries the result.

All three sources are post-ruling (2026-09-08 / 2026-09-08 / 2026-09-11), so for
the first time nothing is excluded by the ORDERING_RULING guard.

 atom     | A | P_total Plancherel                  | sg | P_total Wenzl                 | sg | agree
----------|---|-------------------------------------|----|-------------------------------|----|------
 deuteron | 2 | -15.095241437873283771              | -1 | -6.9212506527                 | -1 | yes
 triton   | 3 | +2.470192708                        | +1 | -13.930562450                 | -1 | NO
 4He      | 4 | +34.126027285357652927              | +1 | -20.466481428076021593        | -1 | NO

**Read the sign COLUMNS:**

    Plancherel   -, +, +    one sign change, between deuteron and triton
    Wenzl        -, -, -    NO sign change anywhere in A = 2, 3, 4

So the measures do not merely disagree on a magnitude — they disagree on
**whether the programme's target phenomenon exists.** It is present only under
the measure these probes aggregate with, absent under the production weight.

### This STRENGTHENS the earlier reading rather than changing it

The 2026-09-07 correction already said, on triton alone: *"under the principled
pairing the A=2 -> A=3 sign change is not yet exhibited, and 4He is needed before
even that is settled."* 4He has now landed and it does not rescue it — Wenzl is
negative there too. The honest statement is no longer "not yet exhibited at
A=3" but **not exhibited at any of A=2,3,4.**

And Plancherel again gives the wanted sign at A=4, as it did at A=3. Preferring
it on that basis is selection against the target (AGENTS.md NO FITTING), so the
pattern of it being the convenient answer twice is a reason for more suspicion,
not less.

### Decision 1 is STILL OPEN — and this bean does NOT close

Which measure is the correct pairing for a Magnus Omega2 question is unsettled;
nothing here chooses it. What changed is that the choice is **no longer
cosmetic** — the 2026-09-07 note said "the choice is not urgent: no published
sign conclusion moves either way", and that is **now false**: at A=3 and A=4 the
conclusion moves. Options qou-q2q7 (A, Wenzl — recommended) / qou-smvw (C, report
both — recommended) / qou-94yt (B) / qou-ia4w (D) / qou-gba1 (E) are unchanged in
substance but have gained urgency.

Per AGENTS.md §13a this bean stays open: its subject is an open question about
the correct pairing, not a mechanical task.

### Two stale assertions fixed in the same PR

Both were contradicted by the witness's own data, which is the defect class this
corpus keeps hitting:

1. Caveat 2 read "Establishes only that the published SIGN does not distinguish
   the two measures" — true when only the deuteron was canonical, and the exact
   opposite of the result now sitting three fields away in the same file.
2. The docstring header/table still had 4He as pre-ruling and "undetermined".

### Verification

Witness `data` byte-identical across mpmath 1.3.0 and 1.4.1 (volatile keys
masked; full `data`+`assertions` compared, not display digits — the truncation
trap). mpmath 1.4.1 installed and re-run rather than committing the downgraded
environment record; clarabel verified genuinely unused by this producer.
`precision-gates.sh --changed` RED set byte-identical to pristine main
(stash/compare), so nothing newly red. The probe exits 1 BY DESIGN —
`sign_robust_to_weight_family` computed 0 expected 1; the failure is the result.
The 10 audit witnesses the gate run dirtied were restored, not committed.

Siblings to cite per qou-x631: qou-k5r5, qou-o6ov, qou-omr7.
