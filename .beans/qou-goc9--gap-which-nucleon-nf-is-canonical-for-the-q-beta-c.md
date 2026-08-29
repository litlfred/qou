---
# qou-goc9
title: 'GAP: which nucleon NF is canonical for the Q_beta counit chain? single-wrap vs typed 6-term differ by 0.579%, 3.6x the phase'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T00:54:05Z
updated_at: 2026-08-28T19:11:15Z
---

Surfaced from `qou-pdix` (PR #5448). Probe:
`computations/qbeta/qbeta_nf_single_wrap_vs_typed_probe.py` (8/8, exact Q(h)
symbolic, validated against the live PROTON_NF/NEUTRON_NF to float64 eps).

## The two objects

| NF | (n-p) support | deg_z E | |eps(n-p)| |
|---|---|---|---|
| single-wrap | {gamma, sigma_0, sigma_1} = crossing-nos {0,1} | 1 | 0.187207 |
| typed 6-term (live `build_nucleon_nf`) | all six = crossing-nos {0,1,2,3} | 3 | 0.188291 |

Both numbers are the ones `docs/audits/2026-05-11-q-beta-residual-decomposition.md`
§1 already quotes (0.18721 / 0.18829), and their ratio is that audit's
**1.00579** "basis-change typed-vs-single-wrap" factor — recomputed here from
scratch rather than transcribed.

## Why it gates

- `docs/audits/2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md`, the Lean
  `epsNP`/`trMNP` defs, and `CrossingWeightAffine.evalMap` all encode the
  **single-wrap** vector. Every affineness / abelian-period conclusion built on
  `evalMap` is scoped to that object and is FALSE for the typed one.
- The live mass compute (`PROTON_NF`, `NEUTRON_NF`) uses the **typed** one.
- The ladder's N=1 factor is a **0.160%** correction; the ambiguity between the
  two NFs is **0.579%** — 3.6x larger. So the phase cannot be derived at all
  until the NF is settled: settling it moves the target by more than the target.

## What would close it

A derivation (not a preference) of which NF the Q_beta counit chain must use —
i.e. why the transition amplitude pairs against a single-wrap rather than a
typed-crossings normal form, or vice versa. The 2026-05-11 audit leaves the
1.00579 as a factor still to be EXPLAINED (it pairs it with the N=0 brane-tower
1.00168 to make the full 1.00744), so the corpus has not chosen.

Scope-(a) throughout: nothing is refuted, neither NF is declared canonical.


## 2026-08-28 — the question is REFRAMED by qou-avt5, and the fork is asymmetric

Corpus-grep (the STRICT checklist) found `qou-avt5` — COMPLETED, and it changes
what this bean is asking.

`qbeta_single_wrap_element_cannot_exist_probe.py` proves scope-(b): NO difference
of typed-crossing words has counit `epsNPq = h(h-2)/2`. Route: eps of any typed
word is `q^m([2]_q/2)^c`; `epsNPq` carries `(q^2-2q-1)` so it vanishes at the
silver ratio; absolute norms in Z[sqrt2] force the difference identically zero
there, which epsNPq is not. Verified here 10/10.

**So goc9's original framing was subtly wrong.** I asked "which of two valid NFs
is canonical". It is not a choice between two admissible objects: the corpus's
DESCRIPTION of Delta (a typed-crossing word difference) and its ASSERTED value
(epsNPq) are mutually inconsistent. qou-avt5 states the fork — prose wrong, or
value wrong — and explicitly declines to adjudicate.

## Independent convergence

My 0.579% gap between the single-wrap and typed counits (PR #5448) is the
NUMERICAL shadow of their STRUCTURAL exclusion. Two routes, same fact, neither
derived from the other.

## New datum, and the limit of it

eps(typed n-p) = 86 at h = 2, where epsNPq = 0. So the live construction SURVIVES
the invariant that kills the asserted value: the horns are not symmetric.
Probe: computations/qbeta/qbeta_counit_silver_ratio_adjudication_probe.py (7/7),
PR #5893.

Necessary, NOT sufficient — this does not prove epsNPq wrong and does not select
horn (b). BEAN STAYS OPEN.

What it buys: horn (a) is now falsifiable. If epsNPq is retained, the real Delta
must have a counit vanishing at h = 2 while not being a typed-word difference.

Also worth recording: h = q - 1/q is EXACTLY 2 at the silver ratio, so epsNPq
vanishes there because it is built with a root at h = 2. The content is the norm
argument; the constant is a red herring.

NEXT: the fork needs the owner of the counit block, or a derivation of epsNPq
from something. Its current status is a bare Lean `def` with no theorem.


## Cross-reference the four-path grep should have found (2026-08-28)

This bean did not cite
[`docs/audits/2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md`](../docs/audits/2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md)
(beans `qou-cds1`, `qou-99qc`, `qou-879g`, `qou-xzrj`, `qou-phlk`; PRs #5858
merged, #5864). Grepped 2026-08-28: zero mentions of it here. That audit lands
**upstream** of the question this bean asks, and may moot it.

**This bean asks:** which nucleon NF — single-wrap 3-term or typed 6-term —
is canonical *for feeding the counit* `epsNPq`.

**That audit asks whether `epsNPq` is the right functional at all**, and answers
no, on three independent counts, each a separate exact-symbolic probe:

- `epsNPq` is the **coordinate sum** `sigma -> 1`, not the augmentation
  `sigma -> q` the corpus calls it (`qbeta_epsnpq_functional_mismatch_probe`,
  7/7).
- The `net` functional is **not a trace** — 8 of 36 ordered basis pairs fail
  cyclicity (`qbeta_net_trace_invariance_probe`, 25/25). A counit into a
  commutative ring is automatically a class function, so this alone shows the
  "counit" label is structural, not cosmetic.
- It does **not descend** to the Temperley-Lieb quotient that convention D's own
  GNS proof (`prf:algebraic-gns-embedding`) places the theory in
  (`qbeta_which_algebra_the_decay_channel_lives_in_probe`, 11/11).

Sorry-free Lean alongside: `QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`
(`sigma -> 1` multiplicative forces `h = 0`).

The complete admissible set is **two** functionals, and they bracket the
measured Q-value from +12.470% (`z = q`, where the Markov trace *is* the
augmentation) and -43.157% (`z = z_D`). `epsNPq` is `tr_M` at `z = 1` — the
trivial loop value, which `qbeta-counit-closed-form.md` itself says "is never
attained on the substrate". **So the +0.168% agreement with CODATA is delivered
entirely by an evaluation inadmissible on both counts.**

### Why this bears on THIS bean specifically

The gating argument here is that the NF ambiguity (0.579%) is 3.6x the ladder's
N=1 phase (0.160%), so the phase cannot be derived until the NF is settled. If
the functional those NFs feed is itself excluded, then **choosing between two
NFs to feed it is moot** and this bean is asking a downstream question. That is
a re-scope, not a closure — recorded, not acted on.

**Not claimed:** that the audit closes this bean, or that Q_beta's number is
wrong. That audit is explicit that it is **scope-(a) throughout**: it establishes
which functional the ansatz evaluates and what the permitted replacements give;
it does not prove the number wrong. It also names the trap in the obvious next
move — the two admissible values bracket the target, so some convex combination
reproduces CODATA exactly, which is **one parameter against one anchor**,
numerology rather than derivation. Any weight must be derived from the
representation.

Also note both admissible replacements are **far** worse against CODATA than the
inadmissible evaluation. That is a reason to take the exclusion seriously as a
statement about the framework, not a reason to keep `epsNPq`.


## RE-SCOPED 2026-08-28 — this bean sits behind qou-99qc, and my own probe is retracted

**Re-scope.** This bean asks which nucleon NF is canonical *for feeding*
`epsNPq`. Two beans sit upstream of that and should be read first:

- **`qou-99qc`** (todo) — *"OWNER CALL: Delta prose vs epsNPq"*. The live owner
  decision. Its 2026-08-26 entry establishes that the fork's premise does not
  hold as originally stated, and narrows option (1) by closing the
  colour-weighted carve-out (15/15 probe).
- **`qou-xzrj`** (todo) — *"the 7.67% trace-invisible remainder of epsNPq (step
  8)"*. The step-8 postulate already has a carrier; do not open another.

If the functional is excluded, choosing between two NFs to feed it is a
downstream question. This bean is not closed by that — it is queued behind it.

## RETRACTION of my own contribution (PR #5893, merged 4135ad98e2)

`qbeta_counit_silver_ratio_adjudication_probe.py` concluded that the qou-avt6
fork is **asymmetric** — `epsNPq` excluded by avt6's invariant, the live typed
value not. **That conclusion does not hold**, and `qou-99qc` had recorded why on
2026-08-26, two days earlier.

avt6's invariant (`counit of a typed-crossing word is q^m([2]_q/2)^c`) governs
the **multiplicative** counit — the augmentation `sigma -> q`, evaluated as a
PRODUCT of per-letter counits, which is legitimate only for an algebra map.
`epsNPq` is a value of the **coordinate sum** `sigma -> 1`, which is not an
algebra map unless `h = 0` (`QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`,
sorry-free). The probe's own `eps_typed` is a coordinate sum too — literally
`sum(a - b)` over the NF coordinates. **So the invariant applies to neither
object the probe compares**, and no admissibility verdict follows for either.

This is the `da-arity-conflation` class AGENTS.md names: a theorem quoted past
the scope its type fixes.

**What survives**: the step-3 re-derivation of the typed coordinate sum from
current source (hash-pinned `gram.hm`, `atom.build_nucleon_nf`), the step-4
provenance check that it IS the live `PROTON_NF`/`NEUTRON_NF`, and the
arithmetic `86 != 0`. Those are reusable. Corrected in place rather than
reverted, so the re-derivation stays available and the reasoning error stays on
the record.

**Method failure worth keeping.** The four-path corpus-grep reached `qou-avt5`,
`qou-avt6` and the audit docs, and still missed the bean that had disposed of
the question. `.beans/` is not under `docs/`, `content/`, `computations/` or
`library/` — it is **path 6**, added 2026-08-26 for exactly this, and the entry
that would have stopped this was in a bean body and nowhere else.
