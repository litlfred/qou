---
# qou-58zw
title: 'Two untrustworthiness classes no existing audit covers: tolerance-below-arithmetic-floor, and producers that SHRANK'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T18:12:32Z
updated_at: 2026-08-30T21:55:16Z
---

Found 2026-08-30 answering "which probes are on float or not trustworthy". The
corpus has seven audits for this area and they are good; these two classes fall
between all of them.

## Class 1 — a tolerance BELOW the arithmetic's own floor

`computations/fr_pullback_borromean_h3a_test.py:549,554`:

    computed=float(plancherel_dev), expected=0.0, tolerance=1e-40
    computed=float(stratum_mass_dev), expected=0.0, tolerance=1e-40

`float()` resolves to ~1e-16. **The tolerance is 24 orders of magnitude below
what the arithmetic can represent.** So the assertion has exactly two possible
meanings, and neither is the one it advertises: either the cast value is
*exactly* 0.0 and the test is trivially true while measuring nothing, or it is
nonzero at ~1e-16 and the assertion must fail. It cannot ever mean "agreement
verified to 1e-40". It reads, in a witness, as a 1e-40 verification.

**Why nothing catches it.** `witness_raw_float64_audit` sees the `float()` and
flags the field. `always_vacuous_assertion_scan` looks for
`computed == expected`. Neither compares the TOLERANCE against the RESOLUTION
of the type the value is carried in — which is the actual defect, and is
mechanically checkable: flag any assertion whose `tolerance` is below ~1e-16
while its `computed` is produced by `float(...)`.

Same file, `:566`:

    computed=float(best_bor), expected=float(best_bor), tolerance=1e-12

`computed == expected` by construction; cannot fail. Its own `source` string
admits it — *"(self-consistent run)"*. `always_vacuous_assertion_scan` SHOULD
catch this shape and did not report this file; worth checking why.

## Class 2 — the producer SHRANK

`computations/probes/delta_lambda_bar_involution_probe.py` (fixed today so it
runs at all: two defects, `qou-cds2`). Its committed witness and what the
current source produces:

    keys only in the committed witness : 19
      /data/gap_decomposition/*   (formula, observed_gap, predicted_gap, miss_pct, ...)
      /data/option_E_comparison/* (verdict: "RULED OUT — wrong sign by 140x, cos=-0.51")
    keys only in a fresh run           :  2   (q0Anchor, q0Value)

`delta_star` also differs materially — `(5,1)`: -15.6949 committed vs -10.3397
fresh; `(3,2,1)` and `(4,1,1)` go to exactly 0.0.

So the committed witness records **analysis whose producing code no longer
exists**. `ghost_value_sweep` catches a producer that CHANGED (194 candidates);
nothing catches one that got SMALLER. The check is cheap: compare the key set a
producer emits against the key set its committed witness holds, and flag any
committed key the current source cannot generate.

I did NOT overwrite that witness. Doing so deletes 19 keys of recorded results
to replace them with values whose change I cannot explain.

## Bonus, from the same sweep — the float64 auditor leaks float64

`computations/audits/float64_leak_audit.py` FAILS ITS OWN ASSERTION and emits
3 raw float64 fields into its own witness (`.assertions[0].computed`,
`.expected`, `.tolerance`).

## Where the 11 `i8_violation` scripts stand

These CARRY a substrate-pure banner (they claim to be float-free) and violate
it — a claim contradicted by the code, which is the sharpest available form of
"not trustworthy". 32 violations over 11 files, worst first:

    9  fr_pullback_borromean_h3a_test.py
    4  canonical_tr_m_via_branching.py
    4  probes/markov_reduction_h3_to_h4_verify.py
    3  chi_at_q_inv_via_native_mpfr.py
    3  chi_cd_mpfr.py
    2  canonical_mass_table_extended.py
    2  normalization_reconciliation_phase5l2.py
    2  probes/he3_pairknot_composite_lp_probe.py
    1  constit_factor_residual_phase5k.py
    1  delta_lambda_categorical_verification.py
    1  substrate/whipple_rotation_involution_probe.py

**And the worst offender's witness has never been committed.** It writes
`fr-pullback-borromean-h3a-test.witness.json`; no such file exists anywhere in
the tree. Run here, it is long-compute — >10 min without reaching the end (H_12
⁴He). So the numbers behind those 1e-40 assertions have never existed, which is
worse than stale and is not what the "9 violations" count conveys on its own.


---

## Update 2026-08-30 — the detector had a false-positive class, and draining it found a live crash

### 1. I published a wrong claim about my own detector, and corrected it

In `f5aa6e5ce9` I wrote **"none of the 61 is an integer count"**. False. It came
from a grep for `float\((n_|len\(|count|num_|int\()`, which structurally cannot
match

    computed=float(result["int_burnside_sum_sq"]), expected=60.0, tolerance=1e-30

because the integer-ness lives in the **dict key**, where no pattern over the
call shape can see it. `int_burnside_sum_sq` is an integer sum of squares,
`float(60)` is exactly `60.0`, integers below 2^53 are exact in float64 — so the
comparison is exact and the tight tolerance is meaningful. Three such sites are
in `probes/gap_a4_T10_mckay_character_2I_probe.py:172,182,192`.

**The criterion was too wide.** The roundoff argument is about a RESIDUAL — a
quantity whose exact value is 0, so float64 error lives exactly where the
tolerance claims resolution. It does not bite on an exactly-representable value.
The audit now splits (`a3369e3349`):

    flagged assertions   51
      RESIDUAL (gating)  39   expected == 0
      EQUALITY (advisory) 12  expected != 0 / non-literal

The equality bucket does **not** set the exit code, because the audit cannot
decide it and guessing is the false-positive mechanism the taxonomy records. The
selftest pins all three directions, so a future narrowing cannot re-merge the
buckets silently.

### 2. The advisory bucket is NOT all false positives — 2 of 12 were real

**`atom_mass_full_hecke_qdeformed.py` — crashes on `main`.** Verified by
stashing: the pristine file exits 1 with `ZeroDivisionError`. `ya`, the
alternating-channel weight, is **exactly 0** — `y_lambda_at(3, Q)` routes to
`y_lambda_su_n(n, q, 2)`, the SU(2) specialisation, whose rank cap *is* the
two-row cap. The producer was authored under convention C, where the alt weight
was 0.0228, and its assertion **divided by it**.

| weight at q=111/100 | committed witness (C, 2026-06-22) | live (D) |
|---|---|---|
| ŷ_sym | 0.41538069634396413 | 0.5054062110 |
| ŷ_std | 0.5618691276397312 | 0.4945937890 |
| ŷ_alt | 0.022750176016304656 | **0.0 exactly** |

The alt channel is not *suppressed*, it is **absent**. Fixed in `f61deb33bf`:
the division is replaced by two assertions stating the cap itself; the
normalisation compares as mpf (under a cast the 1e-25 tolerance did no work —
any mpf residual below ~1e-16 rounds to exactly 1.0); channel traces serialize
through `_precision.fmt` (raw-float64 ratchet **51 → 0**, NEW dirty 0).

**`qbeta_wenzl_habiro_ansatz_probe.py:479`** asserted `float(target_c[2])`
against `-1.0`, where `target_c[2] = sp.Integer(-1)` is a literal assigned 211
lines earlier — an input compared to itself. Its `source` field also repeated
the "Lean-proved Taylor-exact" claim AGENTS.md corrects. Both fixed in
`d1e1f294fd`.

### 3. A 17th detector-blind spelling — a literal reaching an assertion via a LIST SLOT

`assertion_on_literal_audit` misses the Wenzl site (confirmed by running it): no
pattern over the call shape traces `target_c[2]` back to an assignment 211 lines
up. Candidate row 17 for
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`.

### 4. Free finding — a stale muon witness drained by nothing but a re-run

Regenerating the Wenzl witness moved `target_c_k["3"]`:

    committed  -2.020188128141   rel 6.0e-06 from AGENTS.md muon   c_3(mu) = -2.0202002328
    fresh      -2.069342577115   rel 2.1e-09 from AGENTS.md proton c_3(p)  = -2.0693425728

One of the ~870 muon-fingerprint witnesses, re-pinned to proton by being run.


---

## 🛑 CORRECTION 2026-08-30 (second, and it INVERTS the first)

`18c6898208`. Two corrections to this detector in one session; this one reverses
the split I recorded above. Both earlier versions were reasoned, neither
measured, and the settling measurement is four lines of mpmath.

### The fact I had not read

    # qou_substrate/witness.py:830, Assertion.passed
    return abs(float(self.computed) - float(self.expected)) <= float(self.tolerance)

**Every verdict in this corpus is a float64 subtraction.** How a producer passes
a value — `mpf`, `str`, `float` — changes what the witness *records* and never
the verdict. So "is there a `float()` cast at the call site" was never the right
question, and **dropping the cast is not the fix**.

### Measured

| | result | |
|---|---|---|
| `float(mpf("1e-45"))` | `1e-45` **exactly** | 16 sig figs at any exponent to ~1e-308 |
| `computed=1e-30, expected=0.0, tol=1e-40` | `False` | **correct**, fails as advertised |
| `computed=1e-45, expected=0.0, tol=1e-40` | `True` | **correct**, passes as advertised |
| `computed=1+1e-30, expected=1.0, tol=1e-40` | `True` | **vacuous**; would pass on a 1e-20 miss |

The defect is **catastrophic cancellation between two same-scale numbers**, so
the floor is *relative*: `2.22e-16·|expected|`. Asserting against exact zero is
the SAFE case — nothing cancels — and it is the bucket the update above gated on.

### The original bean finding is also wrong

The `fr_pullback_borromean_h3a_test.py:549,554` sites that opened this bean —
`computed=float(plancherel_dev), expected=0.0, tolerance=1e-40` — are the
`expected == 0` shape and are **fine** on this axis. `float()` of a tiny mpf
residual is lossless. Whatever else is true of that file (it carries a
substrate-pure banner and its witness has never been committed — Class 2 of this
bean, untouched), the tolerance is not the problem.

### The corrected detector

`expected != 0` **and** `tolerance < 2.22e-16·|expected|`: **19 sites, 13
files**, sorted by shortfall. It sees sites the old version excluded by rule —
worst is `probes/su4_casimir_beta_derivation_probe.py:156`, `expected="0.75"`,
`tolerance="1e-50"`, **1.7e34× below** the reachable floor; string bounds were
previously skipped as "legitimate".

`_numeric` now unwraps a literal inside a numeric constructor (`mp.mpf(1)`,
`sp.Integer(-1)`), because that is exactly the shape a first-pass fix produces —
without it the audit went quiet on the two assertions `f61deb33bf` had just
written. 19 → 21, both extras mine. Fixed to residual-against-zero.

### The call-site rule

    # vacuous however `norm` is passed
    add_assertion("normalised", computed=norm, expected=mp.mpf(1), tolerance=1e-25)
    # meaningful
    add_assertion("normalised", computed=fmt(abs(norm - 1)), expected="0", tolerance="1e-25")

### Unaffected

Everything measured rather than inferred: the `atom_mass` `ZeroDivisionError` on
main, `ŷ_alt = 0` exactly, the stale convention-C witness, the 8–90 % `tr_full`
shift (`qou-enn6`), the `qbeta_wenzl` input-compared-to-itself, and the
list-slot blindness (row 17). What does not stand is calling the 39
`expected == 0` sites a defect class.

### Still open on this bean

Class 2 (producers that SHRANK) is untouched. And the 19 corrected sites are
undrained.


---

## DRAINED 2026-08-30 — 19 → 0, and a third broken producer

`d3dca4631f`. Every site the corrected criterion flags, in two classes.

**Class A (13 sites)** — the quantity carries roundoff, so `abs(float(c) −
float(e))` cancels at `~2.22e-16·|e|` and the bound was unreachable. Fixed to
**residual against 0**. Worst and most telling: `su4_casimir_beta_derivation`
had `expected="0.75"`, `tolerance="1e-50"` — **1.7e34× below reachable** — while
the *correct* mpmath check already sat **two lines below** in its own `ok &=`
guard, and the sibling assertion directly above already used the residual
pattern. The producer was right; only the witness was vacuous.

**Class B (6 sites)** — the quantity is an exact integer (Burnside sums of
squares, dimension counts, `x/x`). `float(60)` **is** exactly `60.0`, so the
comparison was already exact and `1e-30` was decorative — a precision claim
about something with no precision. Changed to `tolerance=0` on the bare int.

### A SECOND FLOOR the criterion does not detect

Several sites serialize with `mp.nstr(x, 10)` or `(x, 12)` under a `1e-20` /
`1e-30` bound. A 10-digit string caps the comparison **before float64 enters**,
and there it is the *stricter* of the two floors. Tolerances set to what the
digits support (1e-9 on a determinant of order 10; 1e-11 on an order-1
product). **The audit should gain an nstr floor** — follow-up.

### Verified, because a fix that does not run is not a fix

- Every touched producer **re-run**. Three died on `NameError: fmt` — the
  residual form needs an import those files lacked. Caught by running, not
  reading.
- All 18 reworked assertions **PASS** in the regenerated witnesses.
- **The new shape can still FAIL**, checked at four boundary points:
  `fmt(1e-40)` vs `"0"` at 1e-50 → False; `fmt(1e-55)` → True; `fmt(1e-20)` at
  1e-30 → False; `fmt(1e-40)` → True. Correct in both directions.
- Raw-float64 ratchet: NEW dirty 1, REGRESSED 1 — the **same two** already
  established as main's. 13 producer changes added none.

### A THIRD BROKEN PRODUCER on main, not mine

`habiro/habiro_q_difference_mode_solve.py` dies with

    sympy.polys.polyerrors.PolynomialError:
    1/(2*u**4 + 2) contains an element of the set of generators

Verified by stashing: **identical failure on the pristine file**. AGENTS.md
records two genuinely-broken producers (`su4_1111_markov_trace_probe`,
`qbeta_habiro_element_probe`); this is a **third**. Its assertion is fixed here
but its witness cannot be refreshed, so that file's source moves without its
witness — recorded rather than reverted.

### Bean status

Class 1 (tolerance floor) is **drained**, after two criterion corrections.
Class 2 (producers that SHRANK) remains **untouched**.


---

## CLASS 2 CLOSED 2026-08-30 — `witness_key_orphan_audit.py` (`466aec0e5d`)

The check this bean specified — *"compare the key set a producer emits against
the key set its committed witness holds"* — is built, static (no producer runs),
and reports **3 files / 11 keys**, every one hand-verified.

### The count moved five times, and each move was a finding about the corpus

| count | what was wrong |
|---|---|
| **611 files / 6382 keys** | hand-written infra list. 20 % of the corpus — a broken detector, not a finding. Spot-checking **three** showed it was `/environment/*`, `/precisionMetadata`, `/q0Anchor`: keys the **builder** writes. Fixed by **deriving** the set from `witness.py`'s own literals; extending the hand list would have been the same defect one iteration later. |
| **14 / 84** | keys named in an **imported module**, not the producer's own file — the same import-cone blindness AGENTS.md records for witness staleness. |
| **4 / 21** | **keyword-argument keys.** `result(A_odd_...=v)` names a Python identifier and `ast.Constant(str)` never sees it. `qcollatz_backward_tree_structure_probe` was reported with three orphans sitting on **line 127 of its own file**. |
| **5 / 40** | use the witness's own **`scriptFile`** instead of guessing from the stem. This **raised** the count — two files were audited against the wrong source. |
| **3 / 11** | a key named **nowhere in `computations/`**. The class an import list cannot reach: `add_data("lp", solver.to_dict())` names `lp` and nothing beneath it. |

Measured precision before that last gate: **10 genuine against ~30 false**.

### An 18th detector-blind spelling, introduced by this audit itself

**A key written as a keyword argument.** `A_odd_preimage_positions_on_main_chain=v`
is an identifier, invisible to every string-literal scan. Candidate row 18 for
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, alongside row 17 (a
literal reaching an assertion through a list slot).

### The 11 genuine orphans

    deuteron-binding-interface-closure     C_knot_fitted_deficit, interface_amplification
    per-irrep-pole-proton-h3               full_tr_M_u_pole, per_irrep_maximizer,
                                           per_irrep_maximizer/ord_q_eq_0_negative,
                                           per_irrep_pole_orders_at_q_eq_0
    deltalambda/b1-kappa-window-extension  local_exponent_min_near, prior_reading,
                                           secant_over_new_window, windowed_exponents,
                                           parameters/track

**`C_knot_fitted_deficit` deserves its own look**: a key with *fitted* in its
name, recorded in a committed witness, whose producing code exists nowhere in
the corpus.

### A corroboration worth recording

`per_irrep_pole_deuteron_h6.py`'s **own docstring** already documents this exact
defect — *"230 deletions against 39 insertions … with no warning of any kind"* —
and names `per_irrep_pole_atom.py` as the de-facto owner of both witnesses. A
prior agent found the instance; this bean asked for the detector.

### Bean status

**Both classes now closed.** Class 1 (tolerance floor) drained 20 → 0 after two
criterion corrections plus a serialization floor. Class 2 (producers that
shrank) has a detector and 11 verified findings.

**Not done here**: draining the 11. Each is a decision about whether to
regenerate a witness (deleting recorded analysis) or restore the producing code,
and `qou-58zw` explicitly declined to overwrite one for that reason.


---

## Following the 11 — and a correction to my own framing

I wrote that `C_knot_fitted_deficit` "deserves its own look: a key with *fitted*
in its name, recorded in a committed witness, whose producing code exists
nowhere." That phrasing implies laundering. **Read, it is the opposite.**

The orphaned block's own `conclusion` field:

> **RETRACTED. NOT zero free parameters** — AME closure requires the fitted
> `C_knot = 5.852` deficit ratio. The Δ_λ gate remains open for the deuteron.
> The genuine zero-parameter deuteron closure is the scalar endomorphism
> `B = m_e·Vol(𝓑₃)·Δtr = +0.19%`, not this.

The number is recorded **as the evidence for a retraction**, and the fit is
named as a fit — the honest disposition AGENTS.md requires. Corroborated
corpus-wide: `C_knot` / `5.852086` appears in **81 files** outside witnesses,
and `docs/audits/2026-08-02-deuteron-symbolic-closed-form-trefoil-qinvariant.md`
calls it *"the fitted `C_knot`"* and a *"categorical master-formula
normalization artifact"*. Nothing is passing it off as derived.

**What IS wrong is narrower and still real:** the producer that computed the
retraction is gone, so `5.852086` cannot be re-derived. An unreproducible
retraction is much better than an unreproducible claim, and it is not nothing.

### The high-impact one is `per-irrep-pole-proton-h3`, and it converges with an independent finding

Citation surface, measured:

| witness | content/ | docs/ | beans | read by .py |
|---|---|---|---|---|
| `per-irrep-pole-proton-h3` | **2** | 4 | 2 | 2 |
| `deuteron-binding-interface-closure` | 0 | 3 | 1 | 1 |
| `deltalambda/b1-kappa-window-extension` | 0 | 0 | 1 | 1 |

The proton one is cited from reader-facing prose —
`mass-theory/per-nucleon-shift-additive-linearity-proof.md:42` links the witness
directly.

And that block's `.qa.json` sidecar **already carries a MAJOR finding on the
same two witnesses, reached from the other direction**: an agent review recorded
that the block *"reports their numbers as confirmations"* while both witnesses
are committed **failing** — proton `full_tr_M_u_pole_eq_shift_NF_proton`
`computed: 18, expected: 19, passed: false`; deuteron `computed: 38, expected:
40`. The same sidecar names `per_irrep_pole_proton_h3.py` and
`per_irrep_pole_deuteron_h6.py` as producers lost to token-substitution sweep
damage ("the canonical formalism" standing in for a script name, four sites in
one block).

**So two independent routes land on the same pair.** That review found the
*numbers* wrong; this audit found the *producing code* gone. Together they say
the failing number cannot even be re-derived — and my `scriptFile` resolution
supplies the missing third piece: the witnesses record
`scriptFile: per_irrep_pole_atom.py`, a generalised producer that took over from
both per-atom scripts.

### Still not drained, and still the author's call

Each of the 11 is a choice between regenerating a witness — which deletes
recorded analysis, including a retraction — and restoring producing code from
history. The `per_irrep_pole_*` pair is the one with a reader-facing consumer
and an existing MAJOR sidecar finding, so it is where the value is.

## 2026-09-15 — Class 3: the green is about a REFERENCE that has since moved

A third member of the same family, found while trying to answer a different
question (whether `phi_k_weight_family_discriminator`'s witness could be checked
without the matching `pyhecke_native` binary). Same shape as classes 1 and 2:
a witness records a green that no longer reproduces, no existing audit can see
it, and the check that would catch it is one line.

**The instance.** `computations/probes/phi-k-weight-family-discriminator.witness.json`
records `8/8 ok`, `computedAt 2026-09-05T06:38:03`. A fresh run on this tree is
**7/8**, and the failure is `reproduces_committed_producer_under_dq2_over_D2`:

| row | reference (read today) | this probe (fresh) | rel |
|---|---|---|---|
| no_FR | 1.54887547774 | 1.76060685111 | 0.1367 |
| 4_1 | 1.23085660637 | 2.10490813661 | 0.7101 |
| 5_2 | 1.21688276949 | 2.47527495144 | 1.034 |
| 6_1 | 1.60678321377 | 1.92396555287 | 0.1974 |

That assertion is not about this probe's own numbers. Line 542 reads
**another producer's committed witness** —
`COMPUTATIONS / "fr-pullback-k3-test.witness.json"`, field `["data"]` — and the
probe's own header (line 94) calls itself a *"READ-ONLY companion"* that
deliberately does not touch `fr_pullback_k3_test.py` because that file is owned
elsewhere. So the coupling is one-way by design and the probe has no say in when
its reference is regenerated.

**The reference was regenerated 2h16m after the green was recorded.**
`fr-pullback-k3-test.witness.json` carries `computedAt 2026-09-05T08:54:32`
against the phi-k witness's `06:38:03`. It now holds `1.5488 / 1.2308 / 1.2168 /
1.6067` — which is the **molien** row of `qou-oots`'s own record — where that
bean records the d_q²/D² row this assertion compares against as
`1.0659881 / 1.2425297 / 1.2911323 / 1.0478474`. So the reference appears to
have been regenerated under a different weight family. **Appears**, not
established: see the limitation below.

**Ruled out: the producer's own source drift.** The probe IS self-stale —
witness `scriptHash 02567f2cea25`, live source `adb0a178178a`, drifted by
`70ae502091` (*"drain(qou-psjm): route 372 AME/CODATA literals to the
registry"*), which replaced three hardcoded AME binding energies with registry
constants. That is a real substantive-looking drift and it is **not the cause**.
Measured both ways:

- the constants move by `5.84e-8` (D), `2.12e-7` (T), `1.92e-7` (³He),
  `4.10e-7` (⁴He) relative;
- checking the producer out at the pre-drain commit `53e53959d7` and re-running
  gives `2.10490760997 / 2.47527433214 / 1.92396634162` against today's
  `2.10490813661 / 2.47527495144 / 1.92396555287` — agreement to ~`2.5e-7`, the
  scale of the inputs, with **no amplification** and **no ranking change**
  (`6_1 < 4_1 < 5_2` both ways).

I first read the 20-103 % discrepancy as a ~10⁶ amplification of the AME
correction and that was wrong; the pre-drain run refutes it. Recording the
refuted reading because it is the tempting one — a self-stale `scriptHash` sat
right next to a large discrepancy and the two are unrelated.

**NOT established, and not establishable in this container.** Whether the cause
is the reference regeneration or the `pyhecke_native` rebuild. The witness
records `pyhecke_native 0.9.0 / build e3fab84c4c1df76a`; this container has the
same version at build `5df83fbc24b06f8a`, and the probe calls
`pyhecke_native.chi_lambda_braid_mpfr` (line 307) for the characters the whole
discriminator is built on. The clean separation — check the reference witness
out as it stood at the phi-k witness's own `commitSha` and re-run — is
**unavailable**: both `69f29ec5219abc5d838e85f74d33a8fa0896313b` (phi-k) and
`46bfe7fa5fc7b134698795411684dd2e61500f5b` (reference) fail `git cat-file -e`
on this shallow clone, the ~55 % `rewritten` class AGENTS.md documents. So this
entry establishes that the green is stale and that the AME drain is not why; it
does not establish which of the two remaining causes it is.

**Why nothing catches it.** `witness_dependency_drift` keys self-staleness on
the producer's own `scriptHash`, which here points at the wrong change.
`ghost_value_sweep` catches a producer whose source changed. `qou-381n`'s
screen catches a *Lean literal* citing a producer whose witness moved. None of
them look at a witness's assertions to see that they READ ANOTHER WITNESS. The
check is as cheap as the other two classes': for any producer that opens a
sibling `*.witness.json`, compare that file's `computedAt` against the
consuming witness's own `computedAt`, and flag every consumer whose reference is
newer than the green it recorded.

**Not fixed here, deliberately.** Regenerating either witness belongs to the
`qou-oots` / FR-pullback arc, not to this bean, and is outside the two
ask-first exemptions — it is neither a precision increase nor corpus-derived.
The tree was restored after both runs (`git status` clean); nothing was
committed but this note.
