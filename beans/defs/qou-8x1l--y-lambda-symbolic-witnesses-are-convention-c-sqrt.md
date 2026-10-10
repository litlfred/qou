---
# qou-8x1l
title: 'y_lambda symbolic witnesses are convention C (sqrt-q): blocks rho_k_h3a_refinement Schur-Weyl and 5 downstream'
status: completed
type: task
priority: normal
created_at: 2026-08-10T13:25:49Z
updated_at: 2026-08-16T02:37:59Z
---


## The finding

The structural detector (test 2: nonzero `y_λ` on a 3+-row block) calls
`float(v)` and `continue`s on `ValueError`, so a weight stored as a **sympy
expression** never reaches the comparison. Same shape of blind spot as the
decimal-fingerprint scan that reopened `qou-eea0`.

**Test 3 (landed, PR #4924 `04cbe04c`):** C is `z = 1/(q^{1/2} + q^{-1/2})`;
D is `z = q³/(q²+1)`, rational and sqrt-free. A half-integer power of `q` in a
weight expression is convention C at any `n`. No maintained list.

Two witnesses, and it is not "symbolic ⇒ suspect" — three of the five holding
symbolic weights on 3+-row blocks are clean:

| witness | expressions | producer |
|---|---|---|
| `y-lambda-symbolic-witness.json` | 20 | **unknown — orphan** |
| `y-lambda-wenzl-bridge-symbolic-witness.json` | 270 | **unknown — orphan** |

Evaluated at q₀ the wenzl-bridge one gives nonzero `y_λ` where D gives exact
zero: `(4,1,1) 0.0101`, `(3,2,1) 0.0073`, `(2,2,2) 7.73e-4`,
`(3,1,1,1) -6.85e-4`, `(1⁶) -1.24e-5`.

## Why it blocks

It is the `y_λ` source for `rho_k_h3a_refinement`, whose Schur–Weyl check

    Σ_λ y_λ χ^λ(β_D) = 0.388286424074788876711537513129
    tr_M(β_D)        = 0.388286471559408882668623506562
    |residual|       = 4.74846e-8      (1.2e-7 relative)

**fails**, and which returns `exit 2` on that failure *while writing its
witness anyway* (`return 0 if sw_match else 2`). The script states the
consequence itself: *"Δ_λ extraction below is meaningless without this
identity."*

`rho_k_h3a_refinement` is the upstream of five producers —
`rho_k_co_casimir_extended`, `rho_k_h3a_co_casimir`, `rho_k_h3a_crystal`,
`rho_k_h3a_frobenius_pairing`, `rho_k_h3a_lp_dual`.

So the producer has been reporting this the whole time in the only channel it
had, and any run classifying `exit 2` as "producer failure" files it under the
wrong heading.

## What this does NOT establish

The residual is ~1.2e-7 relative, close to the ~1e-7 signature AGENTS.md
records for an ideal/experimental **anchor straddle** (muon-built `y_λ` cache
against proton-q₀ `χ_λ`). Those are two different causes with a similar
magnitude and I have **not** separated them — convention C in the `y_λ` is
established by the sqrt signature and the nonzero ℓ≥3 weights; that it is the
*whole* residual is not. Re-deriving the `y_λ` under D and re-measuring is
what decides it.

## To close

1. Find the producer for both symbolic witnesses (currently orphans — a
   re-run of the 54 does not touch them).
2. Re-derive them under D — sqrt-free, `y_λ = 0` for `ℓ(λ) ≥ 3`.
3. Re-run `rho_k_h3a_refinement`; SW check must pass at 1e-40, exit 0.
4. Then the five downstream, in dependency order.
5. Re-measure the residual against the anchor-straddle hypothesis above and
   record which cause it was.

Blocks the `qou-eea0` convergence criterion (`--stale` empty).

## Producers identified — both are DEPRECATED, and that is the point

| witness | producer |
|---|---|
| `y-lambda-symbolic-witness.json` | `computations/_deprecated/y_lambda_symbolic.py` |
| `y-lambda-wenzl-bridge-symbolic-witness.json` | `computations/_deprecated/y_lambda_wenzl_bridge_extended.py` |

`qou-eea0` already ruled on this class:

> their producers are in `_deprecated/`. The witness outlived the script.
> These cannot be regenerated without un-deprecating, and probably should be
> **retired rather than regenerated**: a witness whose producer was
> deliberately retired is history, and history is allowed to be convention C
> provided it says so.

**That disposition does not hold for these two.** It assumed such witnesses
are no longer consumed. These are read — as live input — by six live
producers:

    delta_lambda_empirical_tabulation.py
    per_irrep_pole_atom_crystal.py
    phase5/phase1c_proton_h3_symbolic_decomposition.py
    rho_k_co_casimir_extended.py
    rho_k_h3a_refinement.py
    sigma_shell_from_beta_chain.py

(13 live files name them; the other 7 only in docstrings/comments. The six
above do `read_text`/`json.load` on them.)

So the deprecation boundary has been crossed in the direction that matters: a
**retired** producer's convention-C output is current input to live compute,
and `rho_k_h3a_refinement`'s Schur–Weyl check is the alarm that has been
going off about it.

This also means the campaign's orphan triage undercounted: "producer in
`_deprecated/` → retire" is only safe once the witness has no live readers,
and that condition was never checked.

## Revised close condition

Step 1 of the plan above is not "find the producer" — it is a decision the
owner may want to take:

1. **Un-deprecate and migrate** `y_lambda_wenzl_bridge_extended.py` to D
   (sqrt-free, `y_λ = 0` for `ℓ(λ) ≥ 3`), regenerate, or
2. **Re-point the six live readers** at a D-convention `y_λ` source that
   already exists, if one covers n = 6 symbolically, or
3. **Retire for real** — delete the witness and fix the six readers.

Not chosen here; each has a different blast radius and (1) resurrects a file
someone deliberated over retiring.

## A FOURTH class the detectors cannot see: derived-value witnesses

Migrating the `y_λ` producer to D (done, cross-validated against the Rust
engine to 1.2e-15) did **not** fix `rho_k_h3a_refinement`. The Schur–Weyl
residual got *worse*: 4.75e-8 → 0.1868.

That is informative rather than disappointing. `χ^λ` is a Hecke character —
it depends on `q` but not on `z`, so it is convention-independent. Only `y_λ`
and `tr_M` carry the convention. C's `y_λ` agreed with the stored `tr_M` to
1.2e-7; D's `y_λ` against the *same* stored `tr_M` is off by 0.19. So the
stored `tr_M` is the **C partner**, and the original 4.75e-8 was never mostly
convention — it is a separate, smaller defect (the anchor-straddle hypothesis
is still live for it).

`computations/atomic-tr-m-mpfr-50dps.witness.json` is convention C **by
construction** — its own description says `tr_M` is computed "via the Hoefsmit
+ Wenzl bridge (Σ_λ y_λ · χ_λ)", i.e. over the C weights. But it stores only
trace *values*: no partitions, no weights, no sqrt. All three detectors clear
it:

    _is_convention_c -> False     fingerprint -> False
    structural       -> False     symbolic    -> False

It is not in the work list and never was.

**The general defect:** convention propagates through the *dependency graph*,
while every detector so far is *content-based*. A witness that merely records
a number derived from convention-C inputs is undetectable from its own bytes.
The fix has to be provenance-based — taint a witness if its producer reads a
tainted witness — which the ordering graph already built for `--stale` can
supply.

## And the producer has been printing a 48% internal disagreement

Re-running `atomic_tr_m_mpfr_50dps.py` (whose bridge module
`tr_m_wenzl_bridge_mpfr.py:573` *already* reads `z = q**3/(q**2+1)`, i.e. the
code is D while the committed witness is stale C) prints, for the deuteron:

    [peel]  tr_M(q_0)   = 0.57517233101788385191979179668715365887545302563801
    |bridge - peel|     = 0.18681514229410284461801930172180759299709038862953

So its two internal paths disagree by 48%, every run, and the witness records
the bridge (C-side) one. My convention-D sum `Σ_λ y_λ^D χ^λ = 0.5750909`
lands on the **peel** side.

**Unresolved, and I am not asserting otherwise:** peel gives 0.5751723 vs my
D sum 0.5750909 — a 1.4e-4 relative gap that is far too large to be precision
and is not explained. Candidates: a different braid normalisation in the peel
path, a writhe/framing factor, or a third convention. Which of peel / bridge /
Σ y^D χ is canonical D is **not** established here.

## The D-looking `z` in the tr_M bridge is in its SELF-TEST

`tr_m_wenzl_bridge_mpfr.py:573` reads `z = q**3 / (q**2 + 1)` — convention D
— which is why I first read the module as already migrated. It is inside
`if __name__ == "__main__":`. The library function actually called by
`atomic_tr_m_mpfr_50dps.py` is `tr_M_via_wenzl_bridge_mpfr` at line 373, and
it does not use that `z`.

So the module **greps as convention D while the live path is not**. Any
text-or-grep-based convention audit clears it falsely. This is the same
lesson as the symbolic blind spot, one level further out: the detector sees
the bytes, not the execution.

Re-running the producer confirms it — the regenerated witness still records
the bridge value (0.38835718…), not peel (0.57517233…). Regeneration with
current code does **not** move this witness to D.

**Reverted my re-run.** It changed the committed deuteron value by 1.8e-4
(0.38828647 → 0.38835718) without resolving anything, and I could not state
what that shift means. A witness whose number I cannot explain should not be
committed.

## Where this leaves the chain

- `y_λ` symbolic: **migrated to D and independently validated** (Rust,
  1.2e-15). Landed.
- `tr_M`: still bridge/C-side. Its producer's two internal paths disagree by
  48% every run, and which one is canonical D is **not** established.
- `rho_k_h3a_refinement`: still exit 2. It cannot pass until the `tr_M` layer
  is decided, and that decision is above what I should take unilaterally —
  it changes the nucleon-mass inputs.

## Provenance detector built (landed) — 695 suspect, not 55

`scripts/convention-c-taint.py`. Seeds from the three content tests, then
fixpoints "a producer that reads a tainted witness emits tainted witnesses".

Three configurations, because the first two fail in opposite directions:

| edges followed | suspect | verdict |
|---|---|---|
| witness refs in the producer's own text | 272 | **misses** `atomic-tr-m` |
| + every ref in imported modules | 1964 (75%) | no signal |
| + only refs in a **read context** | **695** | catches it at depth 1 |

Import-following is required because the filename literal is usually one
module away: `atomic_tr_m_mpfr_50dps.py` names no witness at all — the
`y-lambda-mpfr-witness.json` read lives inside
`tr_m_wenzl_bridge_mpfr._load_y_lambda`.

**The selftest paid for itself immediately** by failing on a real bug rather
than on the test: `WITNESS_REF` matched `\.witness\.json`, but 13 witnesses
are named `foo-witness.json` — the `y_λ` family among them. The **harness
carried the identical regex**, so its dependency ordering has been silently
dropping exactly the edges that matter most here. Fixed in both; orphans
27 → 26, seeds 47 → 53.

Calibration: a taint is provenance-**suspect**, not proved C — a producer may
read a tainted witness and never use the affected field. It is a review queue
ordered by distance from a seed; the script exits 0 by design. The strong half
is the converse: untainted *and* failing no content test is clean on both axes.

## RESOLVED — tr_M aligned to D (owner instruction, 2026-08-10)

The chain was already wired: `y-lambda-mpfr-witness.json` declares
`source_witness = y-lambda-wenzl-bridge-symbolic-witness.json`, the file
migrated to D. Regenerating propagated D into `_load_y_lambda` and thence
into `tr_M` — the dependency order the harness computes.

**The 48% split closed to machine-exact.** Bridge vs peel on the deuteron,
which had disagreed by 0.1868 every run:

    |bridge - peel| = 3.63e-51        (and 2.29e-50, 2.16e-50 on the others)

The peel side was right. My earlier 1.4e-4 "unexplained gap vs peel" was my
own ad-hoc `Σ y^D χ`, not peel — a correction to my own prior claim.

Canonical tr_M at q₀, C → D: proton 1.06531 → 1.14576, neutron 0.92323 →
0.98774, deuteron 0.38829 → 0.57517, tritium 0.10405 → 0.22931, helium-3
0.20654 → 0.40377. Both anchor tables regenerated; convention aligned on
both **without** touching anchor selection.

## Still open, and now precisely located

1. **`rho_k_h3a_refinement` SW: 0.1868 → 8.15e-5, still failing 1e-40.**
   NOT convention. Its `y_λ` match the bridge's to **1.14e-8 = 11.4 ppb** —
   the documented μ–p straddle (it evaluates symbolic weights at the *proton*
   q₀ while the bridge defaults to the *muon*-pinned ideal table). 1e-8 cannot
   produce 1.4e-4, so by elimination the residual is in the refinement's own
   **live χ path**. Separate defect; needs its own bean.

2. **`_Y_LAMBDA_DEFAULT` points at the ideal (muon) table**, against the
   2026-08-07 proton-default directive. Deliberately so — it carries an
   explicit *"the default name stays the IDEAL (muon) one so existing
   consumers are untouched"* comment, and **13 files** read that table.
   Flipping it is a decision with a blast radius, not a fix. Owner call.

3. **Downstream regeneration.** tr_M moved +7.5% to +120% into the
   mass/binding layer. Every consumer needs re-running; the taint queue
   (`scripts/convention-c-taint.py`, 695 suspect) is how to enumerate them.

## Blast radius of the D migration: 146 producers, 188 witnesses

`.work/convention-d-blast-radius.json` (schema `convention-d-blast-radius/v1`).
Every producer that reads one of the four witnesses moved to D
(`atomic-tr-m-mpfr-50dps`, `y-lambda-mpfr`, `y-lambda-mpfr-proton`,
`y-lambda-wenzl-bridge-symbolic`), with what each reads and writes.

It is a regeneration **queue**, not a verdict — a reader may not touch the
affected field. But `tr_M` moved +7.5% to +120%, so the ones that do are
materially wrong now.

Not swept in this session: 146 producers is beyond what one session can run
(one alone, `per_irrep_pole_atom`, times out at 1800s), and #4928 owns bulk
regeneration. Handing off the list rather than starting a sweep I cannot
finish.

## A blind spot in `--stale`, found by using it on my own change

`--stale` reported the same 7 producers as before my migration — nothing new.
Correct, and useless here: it uses the **journal's** append order as its
clock, so it only sees producers run *through the harness*. I regenerated
`y_λ` and `tr_M` **by hand**, so the migration is invisible to it.

That is a real limitation of the mechanism, not of this run: any hand-run
regeneration — which is how most one-off fixes happen — leaves `--stale`
silently clean. Options are to stamp hand-runs into the journal, or to derive
staleness from witness mtime/`scriptHash` against the graph instead of from
run order. Not fixed here; recorded so the next agent does not trust a clean
`--stale` as proof of consistency.

## The 8.71e-8 residual: eight hypotheses, eight refutations, and where it points

Every component of `Σ_λ y_λ·χ^λ = tr_M` was tested individually. All pass.

| # | hypothesis | verdict |
|---|---|---|
| 1 | peel is muon-anchored | refuted — imports `Q_MP` (proton) |
| 2 | peel shares the y_λ table (self-agreement) | refuted — no table reads, symbolic recursion |
| 3 | the proton y_λ table is wrong | refuted — 2.75e-50 vs symbolic, 1.25e-15 vs Rust |
| 4 | peel is *substituted* at muon | refuted — `q60 = sp.Float(q_str,60)`, q_str proton |
| 5 | peel bakes numerics at build time | refuted — pure sympy `Add`, free symbols `{q}`, 0 decimals |
| 6 | the braid word is muon-anchored | refuted — matches `−h(proton)` to 4.57e-18 |
| 7 | the bridge's χ is cached / anchor-locked | refuted — χ tracks `q_str` (rel ~1e-7) |
| 8 | the muon table's values aren't muon | refuted — matches symbolic@muon to ~1e-50 |

### The measurement that matters

    bridge(proton y, proton χ) = 0.575172243917771870826535   = refinement's Σy·χ
    bridge(proton y, muon χ)   = 0.575172395398020063703615
    peel (proton, symbolic)    = 0.575172331017883851919791796687
    bridge(muon y,  proton χ)  = peel  to 3.63e-51

**Mixing anchors satisfies the identity exactly; matching them misses by 8.71e-8.**
Since `Σ y_λ(q)·χ^λ(β,q) = tr_M(β,q)` must hold *identically in q*, this is not
an anchor question. It says the symbolic `y_λ(q)` is not quite the Markov weight
function, off by something that cancels in that one mixed pairing.

### What this says about the convention-D migration (self-critique)

The D migration was validated three ways — Rust `trace_weights_n` at 1.2e-15,
all 3+-row weights vanishing, and both table evaluations at ~1e-50. Every one
of those tests the weights **against each other or against a shared
convention**. *None* tests the Markov identity itself, which is the property
`y_λ` actually has to satisfy.

peel is the only object in the chain that computes `tr_M` **without** going
through `Σ y·χ` — which is exactly why it is the one disagreeing.

So: the migration is verified as an **evaluation** and unverified as a
**normalisation**. The 3.63e-51 I twice cited as confirmation was measuring the
wrong property, and its exactness is a clue about `y_λ(q)`'s functional form,
not about q₀.

### Obstacle to the obvious next test

Testing the identity *identically in q* is not a substitution: the braid word's
`d` values are **numeric and pinned** (verified proton-derived). `χ^λ(β_D,q)`
therefore cannot be evaluated at an arbitrary q without **rebuilding the word
at that q**. Any "check it at a third anchor" probe must regenerate the word
first, or it silently pairs a proton-built word with foreign-q matrices — the
same class of straddle this whole bean is about.

### To close

1. Rebuild `atom_braid_word_3A(1,1)` at a third q (neither pin) and test
   `Σ y_λ(q)·χ^λ(q) − tr_M_peel(q)`. Failure there ⇒ `y_λ(q)` is wrong and the
   muon agreement is coincidence; success ⇒ the defect is anchor-specific.
2. Or reduce `Σ y_λ(q)·χ^λ(β_D,q) − tr_M_peel(q)` symbolically to a rational
   function in q and check it is identically zero. No q₀ needed; decides
   whether `r = 2` is the right Wenzl-bridge solution.

## SYMBOLIC RESULT: the D weights ARE correctly Markov-normalised

Tested the normalisation identity symbolically — no q₀, no braid word, no
second implementation to agree with:

    n=2: sum_lambda y_lambda(q)*dim(lambda) = 1
    n=3: = 1     n=4: = 1     n=5: = 1     n=6: = 1

Exact, identically in q, at every n from 2 to 6, via `cancel`/`together` on
the convention-D symbolic witness.

**This is the check the three earlier validations missed.** Rust
`trace_weights_n` (1.2e-15), the 3+-row vanishing, and the two table
evaluations (~1e-50) all compare the weights against each other or against a
shared convention. This one tests the defining property directly — and it
passes.

So the previous entry's self-critique is half retracted: the gap was real
(normalisation was untested) but the answer is clean. `z = q³/(q²+1) ⟹ r = 2`
yields correctly normalised Markov weights **as a function of q**, not merely
numbers agreeing at one pin. The convention-D migration stands.

### Consequence for the 8.71e-8

If `y_λ(q)` is correctly normalised, the residual is NOT in the weights. It
must be in `χ^λ(β_D)` or in the peel recursion on that specific braid — the
two factors this test does not touch, since it evaluates at the identity
braid where `χ^λ(1) = dim V_λ`.

`Σ y_λ·χ^λ(β) = tr_M(β)` for a general β is strictly stronger and remains
untested symbolically.

### Formalize-first (owner point, 2026-08-10)

Per AGENTS.md §Formalize-first this identity is a structural invariant and
belongs in Lean, not in a probe:

    ∑ λ ⊢ n, y_λ * dim V_λ = 1

and then the general `Σ y_λ·χ^λ(β) = tr_M(β)`. That should gate the weights,
rather than numerical agreement at a pin. That it took eight refutations to
notice the defining property was never checked is the argument for the policy.

## CLOSED — the 8.71e-8 was bookkeeping, and three claims above are wrong

`computations/markov/peel_anchor_identification_probe.py` (+ witness, 4/4
assertions). The residual is not in the weights, not in `χ^λ`, and not in the
peel recursion. It was a peel value read out of the **muon** witness and
labelled proton.

### The measurement

The peel returns an **exact integer-coefficient rational function of q** —
deg-50 numerator over `192·q²³·(q²+1)³`, zero `Float` atoms — so one
expression evaluates at both pins:

    peel(proton q₀) = 0.5751722439177718708265353439129360075256
    peel(muon   q₀) = 0.5751723310178838519197902970632253704678

Against the four numbers recorded above:

| recorded as | actually matches |
|---|---|
| `bridge(proton y, proton χ)` = 0.575172243917771870826535 | **peel(PROTON) to 5.98e-25** — every digit recorded |
| "peel (proton, symbolic)" = 0.575172331017883851919791796687 | **peel(MUON) to 2.61e-24** |

The second is verbatim the `peel_check.tr_M_at_q0_50dps` field of
`atomic-tr-m-mpfr-50dps.witness.json`, whose own `q_0_50dps` field reads
`1.109978595557334719899763`. The witness is labelled correctly; this bean
read it as proton. So the anchor-**matched** pairing satisfies the identity to
all recorded digits, and the paradox — *"mixing anchors satisfies the identity
exactly; matching them misses by 8.71e-8"* — never happened.

### Three corrections to this bean

1. **The stated obstacle is false.** *"The braid word's `d` values are numeric
   and pinned. `χ^λ(β_D,q)` therefore cannot be evaluated at an arbitrary q
   without rebuilding the word at that q."* Not for the peel path.
   `crossing_from_cd` uses the numeric `(c, d)` only to *identify* which of
   five canonical templates a crossing is — a q-independent combinatorial
   choice — and builds the element from the **symbolic** form. Even the colour
   δ goes in as `(q−1)²(1−q⁻⁴)/3`. No anchor enters `tr_M_atomic` at all; the
   caller's substitution is the only one the number ever sees.
2. **Hypothesis 1 was refuted on the wrong grounds.** *"peel is muon-anchored
   — refuted, imports `Q_MP` (proton)."* It does import `Q_MP`, for the
   `abs(df + h·(½ − δ/4)) < 1e-9` pattern-match tolerance, which selects a
   template and is discarded. The import is real; the inference from it is
   not. The peel is neither muon- nor proton-anchored — it is anchor-free.
3. **"Both anchor tables regenerated" — one was.**
   `atomic-tr-m-mpfr-50dps-proton.witness.json` was last computed 2026-08-09,
   a day *before* the migration commits `de9fd2521` / `e2295f00f`, which
   touched only its muon sibling. It still carried C (proton 1.065306,
   deuteron 0.388357). Regenerated: 1.145760 / 0.575172, with `|bridge − peel|`
   ≈ 1e-50 on proton, neutron, deuteron, tritium and helium-3. So the anchor
   the 2026-08-07 directive makes the default for all new compute was the
   stale one, for six days.

### Why it hid, and the mechanism now closed

`markov_peel.tr_M_atomic`'s docstring advertised `z = 1/(q^½ + q^{-½})` —
convention C — long after the live path moved to
`hecke_symbolic.z_markov = q³/(q²+1)`. `z` is named nowhere else in that
module, so the stale line was the only convention statement a reader would
find in the canonical peel entry point. Corrected, with what the module
actually guarantees.

Second mechanism, also closed: `WitnessBuilder.stamp_staleness_metadata` wrote
`q0Anchor` **unconditionally**, while `build()` guards it with
`if "q0Anchor" not in witness`. Two writers of one field, disagreeing. The new
probe declares `q0Anchor: "ambiguous"` — honest, since spanning both pins is
its subject — and had `"proton"` stamped over it from the running script's
manifest entry. A witness asserting a pin its contents do not carry is exactly
what the field exists to prevent. Guarded.

### A structural convention check that falls out

`(q²+1)` divides the peel's denominator once per Markov peel, because
`z = q³/(q²+1)`. Convention C's `z = 1/(√q + q^{-1/2})` cannot produce that —
it leaves half-integer powers. So *"(q²+1)³ divides the denominator"* is a
convention test on a symbolic result needing no source reading, no `z` grep,
and no anchor. Asserted by the probe.

### Still open

`Σ_λ y_λ(q)·χ^λ(β) = tr_M(β)` **identically in q** for a general β. What is
established is agreement at each of the two pins to ~1e-50, plus the
normalisation `Σ y_λ·dim V_λ = 1` symbolically at every n from 2 to 6 (and in
Lean). The general-β symbolic reduction is strictly stronger and untested —
but it is now tractable rather than blocked, since the peel side is a rational
function and correction 1 removes the reason this bean gave for not trying.
