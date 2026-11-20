---
# qou-ng7j
title: Detector is blind to non-y_lambda convention-C quantities (tr_M, z); Schur-Weyl is the real per-weight test
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T18:42:38Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---


## The question this answers

From `qou-y6h7`: *is the `1e-40` shadow-price identity supposed to hold under
convention D at all, given it was established under C where every channel is
live?*

**Yes — it is not a convention-C artifact, it is the definition.**
`rho_k_h3a_lp_dual.py:340` computes

```python
sw_err = abs(sw_sum - tr_M)        # sw_sum = Σ_λ y_λ(q₀) · χ^λ(β_D)
```

which is the Schur–Weyl / Frobenius identity `tr = Σ_λ y_λ χ^λ`. That identity
is exactly *what makes* `y_λ` the Wedderburn weights of the trace. It has to
hold for whichever weights are correct, under any convention.

## So why does it fail under D — and it is not (yet) the weights

`tr_M` comes from `load_deuteron_tr_M()`
(`rho_k_h3a_refinement.py:276`), which reads
**`atomic-tr-m-mpfr-50dps.witness.json`**. The Markov trace is
convention-dependent — it is the trace with parameter `z` — so under D it must
be recomputed at `z_D = q³/(q²+1)`. It has not been:

- last touched by an unrelated commit; **never regenerated** in PR #4928;
- producer `atomic_tr_m_mpfr_50dps.py` exists, so it is regenerable;
- **it is not in the convention-C work list at all**.

Both sides of the identity are therefore in different conventions, and it must
fail. That is diagnostic of a stale `tr_M`, not of the identity being C-specific.
It does not exonerate the shipped weights either — the identity simply cannot be
used as a test of them until both sides are the same convention.

## The blind spot, which is the real finding

`_is_convention_c` fires on (a) known convention-C decimals, or (b) a nonzero
`y_λ` on a three-or-more-row partition. **Both tests key on `y_λ` tables.** A
convention-C quantity that is not a `y_λ` table is invisible:

| quantity | convention-dependent? | detector sees it? |
|---|---|---|
| `y_λ` table, numeric | yes | yes (structural) |
| `y_λ` table, symbolic strings | yes | only after the PR #4928 fix |
| `tr_M(β)` — trace at parameter `z` | **yes** | **no** |
| `z` itself | **yes** | only if it happens to match a listed decimal |
| anything derived from these (ρ, Δρ, binding, mass) | **yes** | **no** |

This is the same shape as the symbolic-root miss: the detector finds convention
C only where it takes the one syntactic form it was taught. So **"47 witnesses
still convention C" is an undercount of unknown size**, and the campaign cannot
be called complete on that number.

## What to do

1. **Regenerate `atomic-tr-m-mpfr-50dps` under `z_D`** and check whether
   `atomic_tr_m_mpfr_50dps.py` computes the trace from a `z` at all, or inherits
   it from a witness — if the latter, follow it up the chain as was done for
   `y-lambda-wenzl-bridge-symbolic`.
2. **Re-run `rho_k_h3a_lp_dual` afterwards.** If `sw_err` returns below `1e-40`,
   that is a *strong per-weight confirmation* of the shipped convention-D
   weights — far stronger than `tr(1) = 1`, which is one scalar per `n` and
   cannot separate individual weights (`qou-smtg` item 4 asks for exactly this
   kind of check).
   If it does **not** return, the weights are implicated and `qou-smtg` becomes
   urgent rather than tidy-up.
3. **Extend the detector** to trace/scalar quantities, or accept and document
   that the work list bounds only the `y_λ` layer.

## Close condition

`atomic-tr-m` regenerated under D; `rho_k_h3a_lp_dual` exits 0 with `sw_err`
below tolerance, or the failure is traced to a named cause; and the detector
either covers non-`y_λ` convention-C quantities or says in its docstring that it
does not.

## Chain traced to the end — and the fix is already written

`atomic_tr_m_mpfr_50dps.py` has two paths, and they differ in convention status:

**The symbolic / legacy path is ALREADY convention D.** It calls
`tr_M_element(elem, n, Z_SYMB, H_SYMB)` from
`computations/markov/markov_trace_canonical.py`, and
`hecke/hecke_symbolic.py:56` reads

```python
z_markov = q**3 / (q**2 + 1)             # convention D
```

so `Z_SYMB` is not an independent symbol — it is the convention-D expression in
`q`. (Recorded because it looks alarming at first glance:
`atomic_tr_m_mpfr_50dps.py:344` substitutes `q60` for **every** free symbol,
which would set `z := q₀` — the *trivial* branch — if `z` were free. It is not;
`free_symbols` is `{q}`. No defect there.)

**The primary path is not.** For the deuteron the published `tr_M` comes from
`_bridge_tr_M`, the Hoefsmit + Wenzl bridge, which is
`tr_M(W) = Σ_λ y_λ(q) · χ_λ(W)` reading **`y-lambda-mpfr-witness.json`** — the
**muon/ideal** table. That table is *still convention C*, because
`regenerate_y_lambda_mpfr.py` defaulted to `--anchor proton` and refreshed only
the proton cache (fixed in PR #4928, **not yet re-run**).

So the Schur–Weyl failure is fully explained without implicating the shipped
weights: `rho_k_h3a_lp_dual` forms `Σ_λ y_λ χ^λ` from the migrated table and
compares it against a `tr_M` built from the un-migrated muon one. Two
conventions, one identity.

### Consequence for the test's value

Because the primary `tr_M` is *itself* `Σ_λ y_λ χ_λ`, once both sides read the
same table the check is **near-tautological** on that path and confirms little.
The check that would actually confirm the weights is the **symbolic/legacy**
path, which computes the Markov trace directly from the braid word at
`z_markov` and never touches `y_λ`. That is the independent comparison, and it
is already convention D — so it is available as soon as the muon table is.

### Next action, concretely

1. Re-run `regenerate_y_lambda_mpfr.py` (now defaults to `--anchor both`).
2. Re-run `atomic_tr_m_mpfr_50dps.py`.
3. Re-run `rho_k_h3a_lp_dual.py`; compare `sw_err` against the **symbolic**
   `tr_M`, not the bridge one, for an independent verdict on the weights.

## Second producer-level `z` site — `binding_k_enumerator.py:150`

```python
def stabilization_factor_z(q: float = Q0) -> float:
    """z = 1/(q^{1/2} + q^{-1/2}) — the Jones–Markov stabilization factor."""
    return 1.0 / (q ** 0.5 + q ** (-0.5))
```

Convention C, hardcoded, in a producer — and invisible to
`convention-c-producer-audit.py` for the same reason `regenerate_y_lambda_mpfr`'s
`z` was: **the audit keys on `y_lambda`, not on `z`.** That is now two confirmed
producer-level `z` sites found only by reading code, which is the strongest
evidence yet that "the producer layer is fully convention D, 178 actionable → 0"
is measuring a narrower thing than its name suggests.

**But do not "fix" this one blind.** Its only use is line 351:

```python
historical_markov_at_braid * (z ** (n_0 - n_braid))
```

and `historical_markov_at_braid` is exactly the *preserved historical field*
`qou-eea0` already documented in this witness (alongside
`stabilization_z: 0.4993203341836945`). Scaling a historical convention-C value
by the convention-C stabilization factor may be precisely correct — history is
allowed to stay convention C provided it says so.

What **is** wrong regardless of that:

* the docstring states `z = 1/(q^{1/2} + q^{-1/2})` as *the* Jones–Markov
  stabilization factor, flatly, as general fact — under convention D it is
  `z_D = q³/(q²+1)`;
* the function name `stabilization_factor_z` is generic, so any future caller
  wanting "the" stabilization factor silently gets convention C.

Minimum repair: rename to `stabilization_factor_z_conventionC` (or add an
explicit `convention` argument) and make the docstring say the value is
convention C, retained for the historical comparison. That keeps the number and
removes the trap.

### This does NOT explain the timeout

`binding_k_enumerator` ran 616 s pre-migration and now exceeds 3600 s, and that
is still unexplained. The `z` above is a single scalar multiply and cannot cost
time. The likelier candidate is the PSD admissibility filter — `psd =
K_eval["alpha_gap"] <= 1e-6` (line 403) over the `L` enumeration (line 218) — no
longer pruning as hard once the convention-D weights put exact zeros into the
matrices, so more candidates survive to the expensive `eigvalsh` stage. That is
a hypothesis from reading, **not** a measurement; it needs the producer run with
timing instrumentation to confirm or kill.

## 2026-09-15 — CLOSED for tr_M. The blind spot is now covered, and it found one.

Owner directive "excise convention C". This bean named the gap on 2026-08-10
and nothing had actioned it: `_is_convention_c` keys on `y_λ` tables, so a
convention-C `tr_M(β)` was invisible. It is not any more.

### The mechanism, and why it needed no production change

`tr_M_via_wenzl_bridge_mpfr` takes a `y_lambda_path`, not a `z` — the
convention enters through the WEIGHTS. And `mass_at_3A_proper.jones_wenzl_weight`
already takes `z` as a parameter. Since `χ^λ(W)` is convention-INDEPENDENT,

    tr_M^C(W) = Σ_λ ω_λ(q, z_C) · χ^λ(W),   z_C = 1/(√q + 1/√q)

is computable live. Validated by reproducing D through the same path:
re-weighting at `z_D` gives `0.15196833920423160759266569775107` against the
bridge's own `0.151968339204231607592665697751` — every digit. `z_C` then gives
the convention-C canonical deuteron `0.064431075366695342301985361229836`.
`z_C = 0.499320334184` matches the value `qou-98g5` states for convention C.

**So no `Z_MARKOV` parameterisation was needed.** I had proposed that as the
route and it was the wrong one — the weight function was already parameterised.

### A SECOND structural reason for the blindness, not in the original list

The bridge evaluates `χ` only where `y_λ` is nonzero, and under D the Wenzl row
cap zeroes every partition with more than two rows — at the deuteron it
evaluates **4 of 11**. Under C every channel is live: measured, **7 of 7**
three-or-more-row partitions carry nonzero weight. So a C trace needs exactly
the `χ` the D pipeline discards, and no amount of re-reading a D breakdown
recovers it. The audit now computes the full table via
`chi_general_word.chi_all_lambda_any` (0.1 s at n = 9).

### Measured

    fingerprints  32 -> 64   (+ 2 trace conventions C/D)
    witness files 33 -> 41
    ACTIONABLE    11 -> 12   (17 before the deliberate triage)
    deliberate     3 ->  8

Twelve convention-C hits. Eight are the five `*-c-vs-d-*` probes whose SUBJECT
is the convention gap — registered in `DELIBERATE`, listed **explicitly rather
than by a shared-stem regex**, because `qou-4bq3` records a DELIBERATE regex
over-blocking 8 of 24 B3 verdicts.

### The one net finding, verified

`computations/qbeta/qbeta-habiro-phase5q-dn-refactorize.witness.json`
(2026-08-10), classified `neither: hardcodes, or computes inline`:

    tr_M_p_q0            1.0653061442544502   <- convention-C proton
    tr_M_n_q0            0.9232332299116376   <- convention-C neutron
    z_q0                 0.6126880371464652   <- z_D
    tr_M_D_q0_witness    0.3882864240747888   <- convention-C DEUTERON
    tr_M_D_q0_phase5q    0.6025946342765165
    ratio_phase5q_over_witness  1.5519333072547734

Corroborated against `qou-mass/CHANGELOG.md`'s convention-C column: proton
`1.06530622859239`, neutron `0.92323329716958`, deuteron `0.38828647154771` —
all matching to the q₀-pin digit. Detector says C+grouped; the changelog agrees
independently.

**The sharp part: a field named `tr_M_D_q0_witness` holds a convention-C
value**, in a file that records `z_q0` as the D parameter. Its headline
`ratio_phase5q_over_witness` is that field's denominator.

NOT claimed: that the ratio is meaningless. `tr_M_D_q0_phase5q = 0.6025946` is
none of the known D deuteron values (canonical 0.151968…, grouped colour-
weighted 0.575172…, grouped colour-blind 0.575090…), so it is some other
object and the numerator needs reading before anyone says what the ratio
compares. Recorded as a finding for the excision campaign, not fixed here.

### Still open on this bean

`z` itself and derived quantities (ρ, Δρ, binding, mass) remain uncovered — the
original table's other rows. `tr_M` is the one closed here.

## 2026-09-15 (same session) — the `z` row is closed too

`z` was the table's other tractable row: "detector sees it? **only if it happens
to match a listed decimal**" — it never did. The existing
`y_lambda_convention_c_fingerprint_audit` says outright in its own docstring
that its test "needs no source, **no `z` grep**, and no anchor", so nothing
covered it.

z_C is one number per pin, so it costs two fingerprints:

    proton     z_C = 0.49932033418369445241   (z_D = 0.61268803714646525160)
    muon-live  z_C = 0.49932033403256001689   (z_D = 0.61268805063827241522)

The proton value matches the figure `qou-98g5` states for convention C, whose
subject is the corpus conflating it with `1/δ = 0.497290545`. Those differ in
the third decimal, so at this audit's 15-digit threshold the conflation is not
a detector hazard — worth saying, since the bean makes it sound like one.

### Measured before building, at three thresholds

    min sig digits   hits   C-labelled files   UNLABELLED files
             8        100          44                 20
            12         98          43                 19
            15         82          41                 11

The 8-digit row is below this corpus's coincidence floor (the audit's own
docstring puts 9-11 figures at 2.7 %), and it shows: at 8 digits a
`tr_M_p2_JW_sym` field looked like a stray hit. At 21 digits it is not a
coincidence at all — for a 2-strand element `tr_M(σ) = z` by definition, so
that field IS z, and it is the C one. Reading the near-miss correctly required
the strict threshold, not looser matching.

### The discriminator, and why it is a PATH and not a registry

41 of the 52 carriers name the convention in the JSON path itself —
`/conventions/C_sqrt_q_over_q_plus_1`, `/parameters/z_C_for_comparison`,
`/data/conventions/C/z_at_q0`. That is the author declaring what the field
holds, and it is a better discriminator here than the `DELIBERATE` registry:
`qou-ztee` records that this family has "no way to mark a deliberate
comparison" and a registry does not scale to 41 entries, while `qou-4bq3`
records a DELIBERATE stem regex over-blocking 8 of 24 verdicts. A path label is
narrower than either — it exempts the one FIELD the author labelled, not the
whole file.

### Result

    fingerprints  64 -> 66      witness files 41 -> 51
    ACTIONABLE    12 -> 20      z hits surfaced: 16

The 41 self-declaring files auto-exclude; the residue lands in plain fields —
`/z`, `/parameters/z`, `/parameters/w_bond_tr_M`, `/data/markov_parameters/z_M_v1`,
`/verification/tr_M(σ_1)`. That last one is the sharpest: `tr_M(σ_1)` is z by
definition, so a verification block is verifying against the C parameter.

Not a registered gate and it exits 0 by design, so nothing turns red on this.

### What remains on this bean

Only the last row: derived quantities (ρ, Δρ, binding, mass). Those are the hard
case and `qou-u5z0` already warns a C dependency "can survive as a derived
IDENTITY — invisible to every detector". `tr_M` and `z` were tractable because
each has a value you can compute and match; a derived identity has neither.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

The detector is blind to non-`y_lambda` convention-C quantities (`tr_M`, `z`
as recorded values). Live, and corroborated today: the value audit catches `z`
BINDINGS; a recorded `tr_M` is a number, not a binding.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10: the field exists on 1.3 % of witnesses, in 23 spellings — and its one consumer could not parse 10 of 11 D-stamps

Measured on `main` `ac111c1814` while re-reading `qou-5h5x`, whose done-when #1
is *"`markov_convention` provenance on every witness a producer writes (turns
the lower bound into a total)"* and names this bean as the owner.

**Coverage.** All **3510** non-`_deprecated` `computations/**/*.witness.json`:

    declaring markov_convention anywhere : 44  (1.3 %)

**And a second defect this bean does not name: the field is free text.** 23
distinct spellings for **4** states —

| state | n | spellings include |
|---|---:|---|
| D | 11 | `D`, `D canonical`, `D (N = 2)`, `D (z = q^3/(q^2+1))`, `D  (z = q^3/(q^2+1))` *(double space)*, `D — the ruled functional, z_D = q^3/(q^2+1)` |
| C | 1 | `C` |
| both compared | 3 | `both (C and D compared)`, `both, compared — D canonical` |
| no `z` enters | 8 | `not applicable`, `n/a (counit only)`, `convention-free — no z is specialised` |

Only **13 of 44** stamps are a bare `"D"`.

### Why that matters more than the coverage number

`qou-5h5x` asks this field to *"turn the lower bound into a total"*. **A
free-text field cannot**, and the proof is its one live consumer.
`computations/per_observable_100x_status.py` — the L2 dashboard AGENTS.md
directs readers to quote — compared the stamp character-for-character:

    matched = str(conv).strip().upper() == CANONICAL_MARKOV_CONVENTION   # "D"

**10 of the 11 spellings that MEAN convention D classified as `INHERITED_C`:** a
correctly-stamped *canonical* artifact reported as carrying the *excised*
convention, on the headline dashboard, in the dangerous direction.

It has produced no wrong verdict to date **only** because the cache it reads
carries the bare `"C"`, which the old check happened to get right. That is
taxonomy row 34 exactly — *zero hits is not the same as verified sound*: the
check had never met a non-bare spelling, so the defect was latent. The moment
`qou-cds1` lands and `qbeta-ck-cache.witness.json` is re-stamped with anything
longer than one character, the dashboard calls the ruled result convention C.

### Fixed at the consumer; the producer side is what remains

`_normalise_markov_convention` maps a stamp to `D` / `C` / `both` / `n/a`, with
`MARKOV_CONVENTION_SPELLINGS` holding all 23 measured spellings as fixtures
(23 rows, **0 FAIL**). **Deliberately conservative** — an unrecognised spelling
returns `"unparsed"`, never `D` and never `C`, so a new spelling fails loudly
rather than being absorbed into either verdict, and `"unparsed"` is documented
as *not a clearance*. Producer re-run: every number byte-identical, one new
payload field `cache_convention_normalised`, live verdict correctly unchanged.

**What this bean still owns**, now in the right order:

1. **A controlled vocabulary first, coverage second.** Stamping 3466 more
   witnesses in free text would multiply the parsing problem by 80. The
   normaliser's four states are a de-facto vocabulary; promoting them to the
   witness schema (`witness-schema`, under `schemas/witness-schema/`) is the
   structural fix, and `WitnessBuilder` is where it would be enforced.
2. **Then coverage** — and note `qou-3ral`'s finding applies: `WitnessBuilder`
   has **three** write paths into the anchor vocabulary, and a guard installed
   on one of them is not installed. Any convention-stamp enforcement has the
   same shape and the same trap.
3. **The blindness this bean is actually titled for is untouched**: a bare
   `tr_M` or `z` value still looks identical under either convention, and only
   producer provenance fixes it. Nothing above changes that.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8378, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-15: "excise(qou-ng7j): the z row closes too — 16 convention-C z values in unlabelled fields"). The work may be partly or fully done. Read the bean before you close it.
