---
# qou-i7ju
title: hadron-knot-table.witness.json is stale on main and its producer cannot finish
status: todo
type: task
priority: high
created_at: 2026-08-30T13:40:13Z
updated_at: 2026-09-05T06:29:13Z
---

`computations/hadron-knot-table.witness.json` disagrees with its own producer
**on `main` today**, before any pending change, and the producer cannot be
re-run to completion in an agent container.

## The pre-existing staleness — measured, and not caused by any open PR

`tr_M(protium)` computed from the current tree is **1.1463376906350053**; the
committed witness asserts **1.123183539266**. That is a 2.1 % disagreement in
a committed published number.

Verified it is not attributable to the in-flight nucleon change (PR #6214) by
computing it **with that change stashed** — identical to the digit,
`1.1463376906350053`. Protium goes through `build_atom_nf`, which that PR does
not touch. So the drift is main's, from some earlier change to the atom
builder or its cone that never regenerated this witness.

Nothing flags it: the witness-staleness machinery keys on `scriptHash` /
`scriptCommitSha`, not on whether the recorded assertions still reproduce.

## Why it cannot be fixed the ordinary way

The producer does not finish. Measured directly 2026-08-30: the three A=1
atoms (`proton`, `neutron`, `protium`) complete in **under 20 seconds**, then
**deuterium** — the first bound atom — runs indefinitely. Killed after
~3.5 minutes of silence here; AGENTS.md records a 50-minute run terminated by
its own timeout, with 16 further atoms after it.

The witness is written **once, after all 19 atoms**, so a partial run produces
nothing. Truncating the `ATOMS` list would produce a *different* witness, not a
regenerated one. Hand-editing the numbers is forbidden.

## What would actually unblock it

Three routes, in increasing order of effort:

1. **Run it where it can finish.** Nothing about the producer is wrong; it is
   simply long. An environment with hours of budget regenerates it as-is.
2. **Make the producer checkpoint** — emit or update the witness incrementally
   per atom rather than once at the end. Then a bounded run refreshes the rows
   it reached, and the wall becomes a partial-coverage question rather than an
   all-or-nothing one. This is a producer change and wants its own decision.
3. **Find the deuterium wall.** AGENTS.md's own note records that the
   `scipy.sparse` boundary once blamed for this was fixed (`da645cf0f32`,
   `46dcfc62a57`) and that what remains is cost, not a defect — `O(dim·nnz)`
   over σ's nonzeros. Whether that cost is reducible has not been looked at.

## Consequence for PR #6214

That PR adds the σ₀² gluon term and moves two more of this witness's
assertions — `tr_M(proton)` +50.00 %, `tr_M(neutron)` +57.50 %. It does **not**
create the staleness; the witness is already stale independently. Blocking a
correct, thrice-cross-checked change behind a pre-existing defect it did not
cause, and cannot fix, would be the wrong trade — but the resulting witness
carries three known-stale assertions instead of one and that must be stated
wherever it is read.


---

## UPDATE 2026-09-04 — deuterium DOES complete, and its binding has flipped sign

Independent run this session (different container, live tree, muon anchor C
`q = 1.1099785956…`). Two things this bean and AGENTS.md both record as
unmeasured are now measured, and one of them is worse than the staleness this
bean was opened for.

### 1. Deuterium completes. Both prior records say it does not.

This bean says *"deuterium — the first bound atom — runs indefinitely. Killed
after ~3.5 minutes of silence here"*; AGENTS.md records a 50-minute run killed
by its own timeout at `exit 124`. **It finished here**, producing a value. The
run was then killed at atom 4 of 19 by its own budget, not by deuterium.

So route 1 of this bean ("run it where it can finish") is better-founded than
it looked: the first bound atom is finite, and the open question is the 15
atoms above it, not whether A=2 terminates. I do NOT have deuterium's wall
time — the launch budget is not recoverable from this session — so this
establishes termination, not cost. `qou-r4w5` already has the cost diagnosis
(brute-force SYT enumeration in `_count_syts_by_12_relation`, closed form for
`chi_lambda(sigma_1)` sitting in the docstring two lines above the call).

### 2. The committed deuterium binding is sign-flipped against the live tree

| atom | committed witness | current tree | drift |
|---|---|---|---|
| proton `tr_M` | 0.419562177934 | 0.629328 | **+50.00 %** |
| neutron `tr_M` | 0.301675079767 | 0.475134 | **+57.50 %** |
| protium `tr_M` | 1.123183539266 | 1.146338 | **+2.06 %** |
| deuterium `tr_M` | 0.253377259444 | 0.404362 | **+59.59 %** |
| deuterium `B_MeV` | **+2.2213** | **−8.5281** | **sign flip, 3.84×** |

The proton and neutron figures reproduce this bean's own `+50.00 % / +57.50 %`
**exactly**, which is what confirms PR #6214's σ₀² gluon term is in the tree I
ran. Protium's +2.06 % corroborates this bean's independently-measured
`tr_M(protium) = 1.1463376906350053` — same value, different session, computed
today.

**The deuterium row is new.** Nobody had it, because nobody had got past A=2.
It matters more than the others: the committed `+2.2213 MeV` sits **0.15 %**
from the AME deuteron binding `2.2246 MeV`, and the live tree gives
`−8.5281 MeV` — wrong sign, 3.84× the magnitude.

**What is NOT claimed.** That #6214 caused the flip. Three drifts are in this
witness at once — #6214's gluon term, the pre-existing protium-class staleness
this bean opened for, and possibly the anchor — and one run separates none of
them. The scope-(a) statement is: *the current tree does not reproduce the
committed deuterium binding, and the disagreement is a sign, not a tolerance.*
Bisecting it needs a run per candidate commit at ~one bound atom each.

### 3. The anchor question is now answerable from a ruling, not a judgement

`hadron-knot-table.witness.json` is the corpus's **last remaining `Q0_FLIP`** —
it carries the retired pin A (`1.1099785955573347…`) while the live canonical
muon is C (`1.1099785956427390…`). `qou-bypn` puts this producer in group A
("via `q_parameter`; each needs a decision, not a sweep") — but `qou-bypn` is
dated 2026-08-25 and the owner's ruling of **2026-08-30** post-dates it and
supplies the decision rule: proton by default, exceptions only for (E1) an
explicit proton-vs-muon comparison or (E2) the ideal CAL-1/2/3 layer, with the
burden on the exception.

Measured against that: the producer's docstring names no pin, no comparison
and no CAL layer — it computes *"mass formulas and Q-value predictions"*, i.e.
observable evaluation — and the committed witness's `q0AnchorReason` is
**`None`**. Neither exception can be named, so under the standing ruling this
is a **proton** producer.

**Consequence for sequencing, and it is the practical point:** re-running at
muon to close the flip would spend the whole 19-atom budget producing a witness
at the anchor the ruling says is wrong, and constraint 4 (manifest and witness
land together) then requires the same run again. The flip should not be closed
before the classification is.


---

## RETRACTION 2026-09-04 — "nobody had got past A=2" is FALSE

The update immediately above says the deuterium row is *"new — nobody had it,
because nobody had got past A=2."* **That is wrong.** It is in this bean, in
`qou-bypn`, and in the body of PR #6678, which is now merged to `main`.

`qou-sv7h` got there first and went further. Two commits, both dated
2026-09-03, both **already in the tree my run used**:

- `815b2a46a0` — wires the Rust LP-accumulator kernel into
  `unified_iterative_correction` and `atom_character_raw`; `binding_energy`
  runs end to end for the first time. **deuterium `B_pred = -7.271102125 MeV`
  in 942.3 s**, wrong sign against AME `+2.224566`.
- `7b8625230c` — **tritium too**: `-7.742121347` against AME `+8.481796`.

So the corpus already had the sign, at two atoms, before my run.

**And their reading of it is better than mine.** I reported the sign. They
report the *shape*, which is the informative part: from A=2 to A=3 the
prediction moves `-7.271 → -7.742` (**6.5 %**) while experimental binding moves
`2.225 → 8.482` (**+281 %**). The accumulator is nearly **A-independent** where
real binding grows roughly linearly in A. A sign flip therefore does not supply
what is missing — whatever is missing is **extensive in A**, which lands exactly
on the standing open problem in AGENTS.md (the super-pairwise additive extensive
object the six Δ_λ ansätze failed to produce, with the pairwise cap
`exchangeDet_pow_two_le_four`). They also establish the sign was **already
negative before** their correction, so it is not "the fix broke the physics" —
the accumulator has been wrong-signed all along and nobody could see it because
the function could not complete.

What survives from my run: the four-atom `tr_M` drift table, and the
independent corroboration of this bean's `tr_M(protium) = 1.1463376906350053`.

## What the retraction UNCOVERS — a 17.3 % gap on identical code

Setting the two deuterium numbers side by side is worth more than either alone:

| run | stem | anchor | `binding_energy(1,1)` |
|---|---|---|---|
| `qou-sv7h` | standalone | **proton** (default) | **−7.271102125** |
| mine, via `hadron_knot_table` | `hadron_knot_table` | **muon** (`ideal_muon`) | **−8.5281** |

**17.3 % apart, and the code was identical.** Measured, not assumed:

- `git log 7b8625230c..6238f50999 --` over `hecke_core_legacy.py`,
  `hadron_knot_table.py`, `tools/pyhecke-native/`, `tools/hecke-engine/`,
  `tools/pyhecke/` is **empty** — no change to any part of the binding path
  between their measurement and my run-time base.
- `pyhecke_native` **0.9.0 present**, so both took the Rust kernel path, not
  the Python fallback.
- `hadron_knot_table.compute_atom` is `B = binding_energy(Z, N)` with **no
  additional terms** — we measured the same quantity.

The one difference I can name is the **anchor**: `q_parameter` resolves it from
`sys.argv[0]`'s stem, `hadron_knot_table` is listed `ideal_muon`, and any
other stem gets proton.

**If that is the cause it is a serious finding**, because the two pins differ by
**11.6 ppb** and the outputs differ by 17.3 % — an amplification of order
**1.5e7**. That would make every number out of this accumulator
anchor-dominated, and it is consistent with `qou-sv7h`'s own finding that
`hecke_core_legacy.py:1604`'s `math.log(abs(tr_run))` narrows to **float64
inside the loop**, upstream of any cast.

**NOT ESTABLISHED — this is a hypothesis with the alternatives named, not a
result.** Untested alternatives: their harness may differ from a bare
`binding_energy(1,1)` call in some way their commit does not state; and their
`B_pred` may be reported at a different point in the accumulation than
`compute_atom`'s `B`. The decisive test is one ~15-minute run of
`binding_energy(1,1)` from a non-`ideal_muon` stem: reproducing −7.2711
confirms the anchor, reproducing −8.5281 refutes it and points at the harness.
That run is in flight; **do not quote the amplification figure until it lands.**


---

## RESOLVED 2026-09-05 — the anchor hypothesis is REFUTED. It is a stale extension build.

The decisive run landed. **My hypothesis was wrong and the amplification figure
is dead — do not quote it.**

    stem = deuteron_pin_sensitivity_diag  (not in ideal_muon -> PROTON)
    q_parameter.Q       = 1.1099785827513808
    binding_energy(1,1) = -8.52811254141235
    elapsed             = 22606.7 s

Proton gives **−8.5281**, the same as my muon run via `hadron_knot_table`. So the
q0 pin does **not** move this number, the accumulator is **not**
anchor-dominated, and the "11.6 ppb in, 17.3 % out, ~1.5e7 amplification"
speculation in the previous section is **retracted in full**.

### The real cause, and the error that hid it

The runtime is the tell I should have read first: **22,606.7 s against
`qou-sv7h`'s 942.3 s for the same call — 24×.** We were not running the same
code path.

`pyhecke_native` **0.9.0 is installed and imports fine**, and I checked exactly
that and concluded the Rust kernel was in use. **The guard does not test the
module, it tests a function:**

    _HAS_LP_KERNEL = hasattr(_PHN, "lp_accumulator_step_traces_mpfr")

and that attribute is **ABSENT** from the installed 0.9.0 (58 exported names;
this is not among them). So `_HAS_LP_KERNEL` is False and both of my runs took
the **Python fallback**. *"The extension imports"* is not *"the kernel is
available"* — that is the whole error.

### Why the fallback's number should not be trusted at all

The fallback builds its matrices at line 1207 via `_build_ysn_matrices`. The
repo's own gate, `computations/audits/ysn_braid_relation_audit.py`, run today:

> the Python YSN family satisfies the QUADRATIC relation but **VIOLATES the
> BRAID relation**. It is therefore **not a representation of H_n(q)**, and
> products of these matrices are **not Markov traces of braids**. Everything
> `unified_iterative_correction` / `binding_energy` computes from them inherits
> this. The Rust `seminormal_matrices_mpfr` family satisfies all three relations
> at 50 dps and is the correct object.

So **−8.5281 is computed on matrices that are provably not a representation of
the Hecke algebra.** `qou-sv7h`'s −7.271102125 is the one computed on matrices
that are. My four-atom `tr_M` table above inherits the same defect and should be
read as fallback-path values, not as the framework's numbers.

**What survives:** the SIGN. Both paths are negative (−8.5281 and −7.2711)
against AME **+2.224566**, so "wrong-signed" does not depend on which path ran.
`qou-sv7h`'s A-independence finding is on the correct path and is untouched.

### Why the kernel gate could not catch this

`lp_accumulator_kernel_gate.py` says so itself: *"Both sides use the SAME (Rust
MPFR) seminormal matrices. That is the whole point."* It holds the matrices
fixed and verifies the **recurrence** to 7.09e-48. The 17.3 % gap is not in the
recurrence — it is in **which matrices go into it**, which that gate deliberately
does not vary. Its 7.09e-48 is correct and is not evidence about the end-to-end
number.

### The systemic problem — this is silent, and it is the corpus's default

`pyhecke-native` is **not on PyPI** (404; its wheel workflow is
`workflow_dispatch`-only with no publish step — AGENTS.md §Project structure).
The kernel *is* in the Rust source (`src/lib.rs:941`, registered at `:1957`);
only the installed 0.9.0 wheel predates it. So in a default container:

- the guard silently selects the fallback — **no error, no warning**;
- the run is **24× slower**;
- and the number it produces comes from a **non-representation** matrix family.

Anyone regenerating `hadron-knot-table.witness.json` — or any binding number —
without a locally built wheel gets that silently. That is a reproducibility
hazard for the whole binding path, not just this witness.

**Suggested guard (not applied here — it belongs to `qou-sv7h`'s arc):** when
`_HAS_LP_KERNEL` is False, `binding_energy` should say so loudly rather than
proceed, because its matrices are known-defective on that path. A `_path_bridge`
-style refusal, or at minimum a stderr warning naming
`ysn_braid_relation_audit.py`.

**Method note worth keeping:** the 24× runtime gap identified the cause; the
value gap alone did not. When two runs of one function disagree, **compare their
wall times before theorising about the physics.**


---

## CLOSED 2026-09-05 — both paths reproduced in one container; diagnosis confirmed

Rebuilt `pyhecke-native` from source (`maturin build --release`, **52 s**),
installed it, and re-ran the identical call. Exports went **58 → 59**, the one
added name being `lp_accumulator_step_traces_mpfr` — the exact function the
guard tests for.

    _HAS_LP_KERNEL = True                    <- was False before the rebuild
    q_parameter.Q  = 1.1099785827513808      <- proton, unchanged
    binding_energy(1,1) = -7.271102124876717      840.8 s

| path | `binding_energy(1,1)` | elapsed |
|---|---|---|
| kernel live (this container, after rebuild) | **−7.271102124876717** | **840.8 s** |
| `qou-sv7h` (independent, different container) | −7.271102125 | 942.3 s |
| Python fallback (this container, stale wheel) | −8.52811254141235 | 22,606.7 s |

`round(−7.271102124876717, 9) == −7.271102125` — **exact agreement with the
sibling to every digit they reported**, from a separate container and a
separately built wheel. The diagnosis is closed:

- **value gap  17.29 %** (1.2570104165 MeV absolute)
- **runtime gap 26.9×**

Both numbers are now reproduced side by side under one q₀, one commit, one
container, with the ONLY variable being whether the wheel carries the kernel.
Nothing else is left to attribute it to — not the anchor (refuted above), not
tree drift, not the harness.

**Consequences that stand:**

1. **−8.5281 and my four-atom `tr_M` table are fallback-path artefacts** —
   computed on a matrix family the repo's own audit proves is not a
   representation of H_n(q). They are not the framework's numbers. The SIGN
   survives (both paths negative against AME +2.224566), and `qou-sv7h`'s
   A-independence result is on the correct path throughout.
2. **`hadron-knot-table.witness.json` cannot be correctly regenerated in a
   default container.** The guard picks the fallback silently, so a regeneration
   attempt produces a plausible-looking witness from the wrong object. This is
   the practical blocker on this bean, and it is upstream of the `Q0_FLIP` and
   of the anchor-classification question entirely.
3. The audibility fix landed (PR #6706): a once-per-process stderr warning from
   `binding_energy` / `unified_iterative_correction`. **Not** a refusal — that
   is `qou-sv7h`'s and the owner's call.

**Prerequisite for anyone picking this up:** rebuild the wheel FIRST and assert
`_HAS_LP_KERNEL` before trusting any binding number. 52 s, against 6+ hours
spent on a number that was never the framework's.


---

## DO NOT REGENERATE — the standing instruction still holds, and I am not overriding it

I now have a working kernel in this container, which is exactly the capability
this bean's route 1 ("run it where it can finish") was waiting on. **I am
deliberately not regenerating the witness.** Two reasons from the history,
neither of them mine:

**1. The sibling's instruction is explicit and current.** `096f0d89b9` said
regeneration "must NOT proceed until step 2" (wire the correct matrices in) —
and step 2 *has* since happened, in `815b2a46a0`, so that precondition is
satisfied and it would be easy to read the gate as lifted. But the LATER commit
`7b8625230c`, written after the wiring, replaces it:

> No witness regenerated, and **hadron-knot-table.witness.json should stay
> untouched while the sign is wrong.**

The sign is still wrong at all four atoms they have measured. So the gate is not
lifted; it was re-stated on stronger grounds. Regenerating now would record
19 atoms of a quantity known to have the wrong sign, at ~840 s per bound atom
and rising as A², and it would *look* like progress.

**2. The committed witness is already invalid on three independent axes**, and
this was recorded a year of sessions ago — `da645cf0f3`, 2026-08-23:

> the existing witness is stale on three separate axes anyway (**muon q₀,
> convention C, older script**)

plus the `Q0_FLIP` on the retired pin, plus the `tr_M` drift this bean measured.
So "is it also on braid-violating matrices?" is a *fifth* axis, and I did not
establish it: the June-era source is outside this shallow clone (oldest fetched
commit 2026-08-15), and the marginal value of a fifth invalidity proof on an
already-invalid artifact is close to zero. **Recorded as unmeasured rather than
guessed** — the witness predates both the braid-relation discovery (2026-08-31)
and the convention-D ruling, so the presumption is unfavourable, but a
presumption is not a measurement.

**What "unblocked" actually means now.** This bean's route 1 was
capability-blocked; it is now *correctness*-blocked, which is a different and
better-defined state. The order is: sign first (`qou-sv7h`, and they hold it),
then anchor classification (`qou-bypn` — proton under the 2026-08-30 ruling),
then regenerate. Not the reverse. A run costing ~840 s per bound atom is cheap
compared with publishing 19 wrong-signed numbers that look freshly computed.

## UNBLOCKED 2026-09-05 (qou-0wqd / PR #6708)

The regeneration was gated on step 2 of the corrected priority in
`docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md` — "wire the
correct family in, then re-run the binding numbers". That is now measured, and
the answer is that nothing moves.

`hadron_knot_table.py` reaches `_build_ysn_matrices` only through
`binding_energy` (line 180), and `binding_energy`'s accumulator is fully served
by the Rust MPFR kernel: `uic(1,1)` is byte-identical under both matrix
families, 193 kernel calls / 193 served. Even with the kernel forced off the two
families agree to `2.0e-14`, because the consumer takes a trace and the trace is
provably blind to a braid defect.

So the witness would record the same numbers either way. Regenerating it is a
staleness question, not a correctness one.
