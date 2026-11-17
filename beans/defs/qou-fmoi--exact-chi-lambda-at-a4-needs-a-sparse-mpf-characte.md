---
# qou-fmoi
title: Exact chi_lambda at A=4 needs a sparse-mpf character product (dense mpmath is ~571 h)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T09:11:25Z
updated_at: 2026-10-10T07:25:44Z
parent: qou-v2om
---


## The incompatibility

`su4_1111_markov_trace_probe` (PROBE 2b, the genuine Schur-Weyl [1⁴] A=4
object) has been dead on `main` with

    ValueError: scipy.sparse does not support dtype object

Not a scipy bug and not a probe bug in isolation — the two halves disagree
about precision:

- `mass_at_3A_proper.atom_braid_word_3A` carries **exact `mpf`** offsets by
  default (`allow_float64=False`, an explicit precision gate). Measured on the
  A=4 word: **25 of 47** crossings carry an `mpf` — 22 `(int, mpf)`, 3
  `(mpf, mpf)`.
- `mass_at_3A_proper.chi_lambda_of_word` builds the product in **scipy sparse**
  and returns `float(...)`. It is a float64 routine by construction.

So a precision upgrade upstream silently killed a downstream consumer. Same
mechanism as the mpf-f-string class in `qou-geqa`, one layer up: there the
`TypeError` was in formatting, here it is in the linear algebra.

## Why the obvious fixes do not work

**`float(c)`** makes it exit 0 in 0.01 s and emit entirely plausible numbers.
Banned — AGENTS.md §"PROBES ARE NOT EXEMPT" names "note it as a limitation and
ship" as the wrong move, and this probe's own verdict discipline turns on
whether a scale-free ratio lands at ×2.093.

**`hoefsmit_mpmath.chi_lambda_of_word_mp`** is the correct exact route — dense
mpmath, same accumulation order, already in the corpus. It is unaffordable
here, measured rather than estimated:

| irrep | dim | exact χ cost |
|---|---|---|
| (6,6) — smallest of ten | 132 | **65.7 s** (measured) |
| (5,3,3,1) — largest | 4158 | **~571 h** (cubic scaling) |

One irrep of ten, for one isotope.

## What the conditioning measurement does and does not say

At dim=132, against the 50-dps exact reference, the float64 character agrees to
**15 digits** (rel. err 1.7e-16) — so this word is well conditioned and float64
loses nothing to cancellation *there*.

Two things that is not. It is not permission to ship float64. And it is not a
statement about dim=4158, where the 47-factor product is far denser and was not
tested — testing it requires the exact value, which is the thing that costs
571 h.

## The actual route

Neither cast nor dense mpmath. The seminormal σ_i carry **at most 2 nonzeros
per row** (1×1 and 2×2 blocks), so:

1. **Sparse mpf product** — dict-of-rows, cost bounded by `nnz` per step rather
   than `dim³`; or
2. **Trace-only row propagation** — `tr(ΠM) = Σ_i e_iᵀ (ΠM) e_i`, propagating one
   sparse row vector through the 47 factors. Rough order: 47 × dim × 2 mpf ops
   per row × dim rows ≈ 5e8 for dim=4158 — hours, not centuries, and exact.

Both stay in exact arithmetic. Either would also unblock any other A≥4 consumer
of the exact word, so this is infrastructure rather than a one-probe fix.

## Interim state (this branch)

The probe now **refuses explicitly** rather than dying inside scipy: a guard
`ExactCharacterInfeasible` naming the dim, the cost, the required fix and the
rule. It exits non-zero — correctly, in the same category as
`low_isotope_mass_table` and `qbeta_braid_nf_sdp_offset_probe`. The A=4 [1⁴]
question stays **unanswered**, which is the honest state; it was not previously
answered either, only opaque.

## 2026-08-24 — route VALIDATED, and two of my own numbers corrected

Prototyped the trace-only sparse product and ran it against the dense routine.
**It works, and the gap is three orders of magnitude.**

### Measured, at the canonical working precision (dps = 70)

```
dim=132  word=47 factors
  dense   chi = 20.472734309881024467    81.2 s
  sparse  chi = 20.472734309881024467     1.0 s     (80.8x)
  relative difference  7.077e-71
```

`7e-71` at a 70-digit working precision is **exact agreement to the arithmetic**
— the two routes compute the same number, which is what makes the timing
meaningful.

Extrapolating quadratically over the ten irreps (132, 165, 462, 891, 1408,
1485, 1650, 2376, 2673, 4158):

| route | all ten irreps |
|---|---|
| dense mpmath | **~1135 h** |
| trace-only sparse, nnz/row = 1 | **~36 min** |
| trace-only sparse, nnz/row = 2 | **~73 min** |

The dim=132 irrep's `sigma_0` is diagonal (1.00 nonzero/row); larger irreps
carry 2×2 blocks, so the honest figure is the second row. **Call it an hour.**
The A=4 [1⁴] object is a lunch break, not a decade.

### Method

`tr(Π M_k) = Σ_i e_iᵀ (Π M_k) e_i`. Propagate one row vector through the 47
factors as a dict of nonzeros — `v ← c·(v·σ_g) + d·v` — and read component `i`.
The product is never materialised, so cost is `dim² · |word| · nnz_per_row`
rather than `dim³ · |word|`. Accumulation order matches
`chi_lambda_of_word_mp` (left-to-right), which is why the values agree exactly
rather than merely closely.

### CORRECTION 1 — the dense cost was understated

This bean said 65.7 s at dim=132 ⇒ ~571 h at dim=4158. Both figures were
measured at **`mp.dps = 15`**, mpmath's default. `_precision`'s own docstring
warns about exactly this: *"IMPORTING THIS MODULE DOES NOT SET mp.dps … the
number reads as measured while carrying ~15 significant digits."* Neither
`su4_1111_markov_trace_probe` nor `hoefsmit_mpmath` raises it, so a harness that
omits `set_compute_dps()` silently benchmarks float64-grade arithmetic. At the
real dps=70 it is **81.2 s ⇒ ~705 h**.

### CORRECTION 2 — the conditioning claim is RETRACTED

This bean, the probe docstring and PR #5615 all said:

> at dim=132, against the 50-dps exact reference, the float64 character agrees
> to **15 digits** — so this word is well conditioned and float64 loses nothing
> to cancellation *there*.

**That is void.** Both sides of the comparison were at dps=15, so the agreement
was the **floor of the arithmetic on both sides** and carried no information
about the mathematics. It is precisely the invalid form AGENTS.md names —
*"agreement at 1e-16 in float64 is the floor of the arithmetic, not evidence
about the mathematics"* — committed in the same PR that quotes the rule.

**There is currently no evidence about conditioning here, in either direction.**
Do not cite it. Now that the sparse route is cheap, the question is answerable
for real: run sparse-exact against float64 at several dims and see whether the
agreement degrades with size.

### Still to do

Implementation is unchanged in shape but now has a measured target: placement
(alongside `chi_lambda_of_word_mp` in `hoefsmit_mpmath`), tests against the
dense routine at small dims, and a decision about whether `su4`'s guard lifts
or the probe routes to the new function. The prototype lives in this session's
scratchpad; it is ~30 lines.

## 2026-08-24, later — the retracted conditioning question, now actually answered

The retraction above said *"there is currently no evidence here about
conditioning, in either direction."* With the sparse route validated, getting
that evidence costs about a minute, so here it is — float64 against the sparse
exact route at dps=70 (itself cross-validated against dense mpmath to 7e-71):

| shape | dim | float64 rel. error | digits |
|---|---:|---:|---:|
| (6,6) | 132 | 2.779e-16 | 15 |
| (9,1,1,1) | 165 | 4.073e-16 | 15 |
| (3,3,3,3) | 462 | 5.715e-17 | 16 |
| (8,3,1) | 891 | 2.999e-15 | 14 |

**float64 holds 14–16 digits across a 6.7× range of dim, degrading mildly.**
Extrapolating to dim=4158 (another 4.7×) suggests ~13 digits — **not measured
there**, and the largest irrep is exactly where a 47-factor product is densest.

### Why this is worth recording rather than quietly dropping

**The retracted claim was approximately right and entirely unsupported.** It
said "15 digits"; the truth is 14–16. Had I not re-measured, I would have
carried a correct-looking number whose evidence was worthless — and would have
had no way to know the difference. Being close to the truth is not the same as
having evidence for it, and the repair is to get the evidence, not to keep the
guess because it turned out fine.

### What it licenses — narrower than it looks

It says the **character product** is well conditioned. It does **not** say the
probe may use float64:

- The `su4` verdict also depends on the `y_λ` Wenzl weights and the ratios
  built from them; none of that is measured here.
- AGENTS.md's rule is about **carriage through the analysis**, not the accuracy
  of one number. A probe conclusion gets written into beans, audit docs and
  content blocks where nothing re-derives it.
- dim=4158 is untested, and it is the case that matters.

So the guard stays, and the sparse implementation remains the right fix. What
changed is that we now know float64 was not *silently* wrong here — which is
useful for triaging the OTHER float64-into-sparse sites (`qou-q7lf`,
`hecke_core_legacy`), where the same question will come up and can now be asked
the same cheap way.

## Correction: the engine has 14 candidate consumers, not zero

I said on merging #5648 that "nothing currently needs it, since the case I built
it for prunes to one cheap irrep". That was measured only against `su4`.

Measured properly — producers that call `chi_lambda_of_word` **and** build their
word with `atom_braid_word_3A`, which carries exact `mpf` offsets:

    binding_rotation_phase_lead          phase3_deuteron_tritium_h_expansion
    wedderburn_jones_markov              ocneanu_weights
    tr_m_q_hecke_seminormal              h6_deuteron_free_word_chi_lambda_probe
    su4_1111_markov_trace_probe          trace_convention_reconciliation
    he3_tritium_cosh_asymmetry_diagnosis term5_v2_chirality
    hoefsmit_mpmath                      canonical_brane_tower
    binding_per_bond_decomposition       mass_at_3A_proper

**14 producers are on the silent-coercion path** after `qou-qrsp` made
`chi_lambda_of_word` coerce its word coefficients to `float` at the contract.

### What that does and does not establish

It establishes the *set*, not the *need*. `qou-qrsp` measured the coercion at
half an ulp per coefficient, and for `su4` the verdict was unaffected — all four
metrics agreed with the exact route to ~16 digits. Whether any of the other 13
has a conclusion sensitive to that loss is **unmeasured**, and the su4 result is
mild evidence they do not.

The cheap check now exists for each: run the caller against
`chi_lambda_of_word_sparse_mp` and compare. That is what settled it for `su4`,
and it is a per-caller question rather than a corpus sweep.


## 2026-08-24 — the engine HAS a consumer, and the corpus already named the blocker it retires

**CORRECTION FIRST.** On merging #5648 I said "nothing currently needs the
engine", then corrected that to "14 producers on the silent-coercion path". BOTH
figures were loose: they counted files that merely MENTION `chi_lambda_of_word`
and `atom_braid_word_3A`, which sweeps in the engine module itself, its own test,
and docstring text. Measured by the definition that matters — who IMPORTS the
float64 kernel:

    8 importers of `mass_at_3A_proper.chi_lambda_of_word`
      -2 already handled (the sparse test; `su4_1111_markov_trace_probe`, migrated)
    = 6 remaining consumers, all with live call sites, 5 of which WRITE A WITNESS

Do not quote 14 or 19.

### The case does not rest on a verdict flip, and should not be argued that way

`mass_at_3A_proper.py:561` is `def chi_lambda_of_word(...) -> float`, and its own
docstring is explicit: *"This is a float64 kernel, and the return annotation is
the contract ... no caller has ever received more than 53 bits from here."* So
five committed witnesses carry numbers from a float64 kernel. Under the STRICT
NO-FLOAT64 rule that is a defect on its own terms — "note it as a limitation and
ship" is banned, and a float64 result "resolves to ~1e-16 no matter what is
true". Whether any of the six has a VERDICT that turns on the extra bits is still
UNMEASURED, and I am not claiming it does.

### The corpus had already written down the blocker the engine removes

Same docstring, closing line: *"at A = 4 the largest irrep is f^λ = 4158, i.e.
~7.2e10 mpf operations per matrix multiply, so that route is not a drop-in for
the A ≥ 4 producers."*

That is exactly the wall `chi_lambda_of_word_sparse_mp` goes around. Hoefsmit
seminormal matrices carry ≤2 nonzeros per row, so propagating one sparse row
through the word costs O(dim²·|word|·nnz) instead of O(dim³·|word|) — the
measured 82–223× — and the stated reason the exact route "is not a drop-in" no
longer holds. The justification for the engine was sitting in the very function
it replaces.

### Next honest step

Migrate the five witness-writing consumers, cheapest dim first, and diff each
witness. That measurement is what would decide whether any verdict moves; until
it is run, the claim is "removes a float64 kernel from five witnesses", not
"changes a result".


## 2026-08-24 (later) — MEASURED: the float64 kernel gives ~14 digits, not 16, and TWO of my own claims above are corrected

### Correction 1: it is FOUR producers, not five, and one is already exact

I wrote "6 remaining consumers, 5 of which write a witness". Reading the CALL
SITES rather than the import list:

    h6_deuteron_free_word_chi_lambda_probe  ALREADY EXACT -- it computes with
      chi_lambda_of_word_mp (lines 122-124) and calls the float64 kernel at 127
      only as a CROSS-CHECK (`chi_b64`). Not a defect. Remove it from the list.

So: **5 files use the float64 route exclusively, 4 of which write a witness** --
`native_5_strand_baryon`, `phase3_deuteron_tritium_h_expansion`,
`rho_k_h3a_gg_trajectory`, `tr_m_q_hecke_seminormal` (witness-writing), plus
`canonical_brane_tower` (no witness).

**An import is a proxy, not a verdict.** I inferred float64 payloads from an
import list without reading what the call site did with the result -- the same
shape as "a non-zero exit is not a defect" and "a source-text grep is not the
answer", which this bean's own notes already warn about. Third time.

### Correction 2: for `tr_m_q_hecke_seminormal` this is not a kernel swap

That producer is float64 END TO END, not merely through the character:
`q_val: float = Q_0_FLOAT` is its q0, and every emitted field is `float(...)`
(`y_at_q0`, `chi_q_at_q0`, `contribution`). Migrating it means carrying q as
`mpf` from `Q_50_DIGIT_STR`, taking y_lambda exact, and serializing via
`_precision.fmt` -- a producer rewrite whose numbers move, not a one-line
substitution. Budget it accordingly.

### The measurement: ~14 good digits, and the loss GROWS with word length

`computations/probes/chi_lambda_float64_precision_loss_probe.py` (new, committed,
writes no witness). Proton pin, exact side at dps 70:

    deuteron  A=2, |word| = 23   worst rel gap 5.36e-15   24.1x the ulp floor
    helium-3  A=3, |word| = 35   worst rel gap 8.17e-15   36.8x the ulp floor

"float64, therefore ~1e-16" was the assumption I would otherwise have shipped.
1e-16 is the FLOOR, not a measurement -- a character is a trace of a PRODUCT over
the whole word, so rounding accumulates with length and the (c, d) coefficients
alternate in sign. 23 ops -> 35 ops moved the loss 24x -> 37x, so A >= 4 is worse
again.

### Why the number decides something

The L1 goal is internal cross-method agreement <= 1 ppQ = 1e-15. **Every gap
measured is larger than that.** So a quantity computed through this kernel
cannot meet L1 -- arithmetically, not as a matter of taste about float64. Any
producer reporting more than ~14 significant digits from it, or claiming
agreement "to 1 ppQ", is reporting its own rounding.

That is the consumer case for the engine, and it does not depend on a verdict
flipping. Whether any of the four CONCLUSIONS changes is still unmeasured; at 14
digits, a probe reporting 4 significant figures is unaffected and should be left
alone.


## 2026-08-24 (later still) — the consumers PUBLISH past the ceiling, which is what scopes the migration

The 14-digit ceiling alone does not establish that anything is wrong: a witness
storing SIX significant digits is untouched by a 14-digit kernel. So I measured
what the four float64-only producers actually publish, over their committed
witnesses:

    native-5-strand-baryon        n= 25  max 18 digits    68% carry > 14
    rho-k-h3a-gg-trajectory       n=106  max 17 digits    83% carry > 14
    tr-m-q-hecke-seminormal       n= 65  max 18 digits    93% carry > 14
    phase3-deuteron-tritium-...          no bare floats in data

**Three of the four publish three to four digits of their own rounding, stored
as data.** Digits past the 14th are not determined by the computation that
produced them.

That makes the migration a CORRECTNESS fix for those three rather than hygiene,
and it also bounds it: `phase3_deuteron_tritium_h_expansion` publishes no bare
floats and is the cheapest to leave alone. Census wired into the probe
(`consumer_census()`), so it is re-runnable rather than a number in a bean.

### What this does NOT establish

It does not show a CONCLUSION moves. A trajectory reported at `.6g` in the
console is unaffected whatever the stored JSON carries; the defect is in what is
published, not necessarily in what was argued from. Keep those separate.

### Migration shape, from reading the three

- `rho_k_h3a_gg_trajectory` is MOSTLY exact already -- `Q_MP`, `mp.mpf` for
  `y_at_q0`/`dim_q_at_q0`, and most `float()` is inside f-strings (display,
  permitted). The genuine leaks are four: the word coefficients
  (`float(c), float(d)`, l.127/129), the stored character (`float(chi)`, l.148),
  `build_seminormal_matrices(..., q=float(Q_MP))` (l.216) and
  `y_lambda_at(n, q_val=float(Q_MP))` (l.212). The LP input `float(abs(target))`
  (l.325) is a legitimate solver boundary -- Clarabel takes float.
- `tr_m_q_hecke_seminormal` is float64 end to end (`q_val: float = Q_0_FLOAT`);
  a rewrite, not a swap.
- `native_5_strand_baryon` not yet read.

None of the four uses `_precision.fmt` for serialization -- that is the other
half of the fix, and is what stops 18 digits being written in the first place.


### Cross-check against the raw-float64 ratchet — and a miscount of mine, caught before it shipped

All three float64-publishing consumers are already on the drain list in
`computations/raw-float64-baseline.json`, with raw-float64 field counts:

    native-5-strand-baryon        25
    rho-k-h3a-gg-trajectory       84
    tr-m-q-hecke-seminormal       65
    phase3-deuteron-tritium-...   NOT baselined

**I nearly wrote "3 of the 6 baseline entries are these consumers."** That was
wrong: the file's top level has six KEYS (`note`, `enforced_rule`,
`drain_owner`, `files_count`, `fields_count`, `files`) and the real count is
`files_count: 1410`. I counted the wrapper, not the contents. Being in a
1410-file baseline is unremarkable and is NOT corroboration -- the opposite of
the striking coincidence I was about to report. Same error class as everything
else in this bean: a proxy read as the answer.

What IS real: the ONE consumer my census found clean (no bare floats in data) is
the ONE not baselined. Two methods, same negative, on the same single file.

So the migration is a DRAIN, not a new finding -- AGENTS.md's "baselines drain,
never grow" already owns these three. What the census adds is the REASON they
should drain ahead of the other 1407: they do not merely carry raw float64, they
publish 3-4 digits of rounding as data, and the kernel feeding them is measured
at ~14 digits. That is a stronger argument than "raw float64 present".


### CORRECTION — it is FOUR of four, and the "clean" one escaped through a shared blind spot

The census above walked BARE FLOATS and reported `phase3_deuteron_tritium_h_expansion`
as carrying none, i.e. clean. **It is not clean.** It stores its values as
STRINGS -- `"12.7030229395046"`, fifteen significant digits -- which is what
`_precision.fmt` emits. Re-measured counting string-serialized numbers too:

    native-5-strand-baryon        n= 28  max 18 digits    71% carry > 14
    rho-k-h3a-gg-trajectory       n=136  max 17 digits    82% carry > 14
    tr-m-q-hecke-seminormal       n= 70  max 18 digits    87% carry > 14
    phase3-deuteron-tritium-...   n=  6  max 15 digits   100% carry > 14

All four publish digits their own computation does not determine.

**And the corroboration I reported one entry above is WITHDRAWN.** I wrote:
"the one consumer the census found clean is the one NOT baselined. Two methods,
same negative, same single file." That is not two methods -- the raw-float64
ratchet keys on the same REPRESENTATION my walker did, so both are blind to a
string. They agreed because they share the blind spot, not because they
independently confirmed anything.

**Two detectors agreeing is not corroboration when they key on the same thing.**
That belongs in the detector-blindness taxonomy
(`docs/audits/2026-08-15-detector-blindness-taxonomy.md`), which already records
that four of its thirteen blind spellings were found BY detectors written to
catch the previous blind spot. This is a fifth, and it was caught only because I
re-verified a negative by a different method before merging -- the negative is
the result nobody re-checks.

## 2026-10-10 — second consumer hits the same wall

`computations/brane_tower_isospin_diagnosis.py`, ported in issue litlfred/qou#7552 to `per_generator_V_hat_3A` with `QOU_H3A_MPF=1`, computes proton through helium-3 at mpf and fails at helium-4: `syt_prefix_cache` hands an object-dtype matrix to `scipy.sparse` (ValueError, mass_at_3A_proper.py:431 -> syt_prefix_cache.py:199). The witness records helium-4 as not computed rather than falling back to float64. Carrier for the port: `qou-g16t`.
