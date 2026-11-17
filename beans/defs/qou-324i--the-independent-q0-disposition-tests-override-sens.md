---
# qou-324i
title: The `independent` q0 disposition tests override-sensitivity, not q0-independence — 7 false positives
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T20:27:28Z
updated_at: 2026-11-17T08:04:32Z
parent: qou-cdx1
---

Found on `qou-1c4y` / PR #5464 while re-measuring after #5457 merged (`238fc79f6e`).
Sibling territory: bean `qou-o922`, PR #5477.

## The test and what it actually measures

A producer is dispositioned `q0Anchor: independent` when its output is
**byte-identical under `QOU_Q0_ANCHOR=muon` vs `=proton`**, taken as proof that
it never reads q₀.

That environment variable only reaches q₀ resolution that goes **through
`q_parameter`**. So the test measures *override-sensitivity*, and
override-sensitivity coincides with q₀-independence **only when q₀ arrives via
`q_parameter`**. Two paths defeat it:

1. **A hardcoded q₀ literal.** An env var cannot change a string constant.
2. **A direct read of `q-pinning-50-digit.witness.json`.** Never consults
   `q_parameter`, so the override is not in the path.

Both produce byte-identical output under either anchor **while being
hard-pinned to muon.**

## Measured (post-#5457, on main)

    37   witnesses stamped q0Anchor: independent
     9   still carry muon digits in the file
     6   producer has a HARDCODED muon q0 literal
     1   producer reads the pinning witness directly
     2   neither — value inherited from an upstream input

So **7 of 9 are provably not q₀-independent.** Worked example —
`qbeta/qbeta_c3_rung_structure_analysis.py:74`:

```python
Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"   # muon
...
q0_mp = mp.mpf(Q0_MP_PIN)          # "Numerical check at q_0"
```

Its witness records `q_0 = 1.1099785955573347198997` under the primary pin key
while asserting `independent`. The label says the producer does not use q₀; the
data block says it evaluated at the muon one.

The six hardcoded: `markov_identity_symbolic_probe`,
`probe_he4_magic_baryeven_prune`, `qbeta_c3_rung_structure_analysis`,
`qbeta_habiro_f_from_shape_collapse`, `qbeta_rung1_div25_framing_squared_test`,
`z2bn_tau_derivation_probe`. Direct-read: `lambda_scale_substrate_probe`.
Inherited: `chirality_topology_binding_probe`, `fitted_labelled_canonical_audit`.

## Scope — what is NOT claimed

- **The drain is good work and the `save()` carry-forward fix is correct.** This
  is a blind spot in one criterion, not a reason to revert anything.
- **28 of the 37 `independent` labels are untouched** by this — they carry no
  muon digits and nothing here disputes them.
- **A hardcoded literal is not automatically wrong.** A probe may legitimately
  pin a specific q₀ for a stability check. The defect is the **label**: calling
  it `independent` records the opposite of what the producer does, and hides it
  from every subsequent pin audit.

## Suggested strengthening

Make the disposition require BOTH the env-override invariance **and** a source
check: no q₀-shaped literal (`1.10997858` / `1.10997859`), and no direct read of
the pinning witness. My `computations/audits/q0_hardcoded_pin_audit.py` already
does the literal half (strips comments/docstrings via `tokenize`), and
`q0_muon_population_partition.py` on #5464 does the direct-read half.


## ANSWERED (2026-08-23) — it IS the Markov parameter, measured

I recorded above that I would not claim `load_q_50dps`'s z is *the* Markov
parameter without a corpus read or an owner call. Measurement settles it.

The defining Markov property `tr_M(T_w) = z^{ℓ(w)}` was tested against both
conventions at the proton pin:

    max|tr_M - z_D^l| = 2.5391265e-50    (holds, to the arithmetic floor)
    max|tr_M - z_C^l| = 0.12606583       (fails)

and `tr_M(T_1) = 0.61268803714647 = z_D` exactly. Corroborated by naming: of
the 24 callers that bind the z return, `pentagon_reduction_li2q.py` calls it
`z_markov` and `e0_lambda_composite.py` calls it `ZMARK`.

So `load_q_50dps` returns **z_C in the Markov role**, under a canonical-D
regime, with 24 consumers. The convention-C detector misses it because it is a
**tuple-element return** — the blind spot this bean records.

Full diagnosis in `qou-rh31`. Fix belongs with the convention-D tranche
(`qou-cds1`/`qou-cds2`), not a q₀-pin PR; and some consumers may use the z in a
pair-weight role (`compute_t2_t3_from_vols`: `T3 = z²·Σ_{i<j}`) rather than the
Markov role, so a per-consumer read is still required before changing it.


## 🛑 CORRECTION + the real cause (2026-08-23): it is `mpf(1)`, not the tuple return

I wrote above — and told #5514 — that the convention-C detector misses
`load_q_50dps` **because it is a tuple-element return**. That is **wrong**.
The site is an ordinary assignment (`z = mpf(1)/...`), and the scan already
covers assignments named `z`. Retracted.

**The real cause is the numerator.** `is_c_form` accepted only a bare literal:

    1 / (mp.sqrt(q0) + mp.sqrt(qi))        -> True
    1.0 / (mp.sqrt(q) + mp.sqrt(qi))       -> True
    mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))    -> FALSE
    mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv)) -> FALSE

**And `mpf(1)` is how the corpus is REQUIRED to write it.** The NO-FLOAT64
discipline mandates carrying `mpmath.mpf` rather than a bare Python literal.
So **complying with the precision rule made a site invisible to the convention
rule** — one house rule blinding another. That is a much better taxonomy entry
than the one I first gave.

## Measured

Fix is a 20-line `_is_unit_numerator()` predicate, used by `is_c_form` and
`is_c_form_reciprocal`. Selftest **53/53** (3 new `mpf(1)` fixtures).

    ACTIONABLE convention-C sites:  1  ->  31

Enumerated all 43 scan rows by hand: every one is
`1/(sqrt(q) + sqrt(q_inv))` or `1/(sqrt(q) + 1/sqrt(q))` — convention C
exactly — and the `DELIB` rows are correctly excluded as labelled comparisons
(`z_C`, `zC`, `z_c`). **No false positives found.** Several are named outright:
`Z_MARK`, `z_mark`, `z_markov`, `z_m`.

So the corpus believed it had **one** actionable C site and has **31**.

Note the standing AGENTS.md posture was already right about this and should
stay: *"treat the remaining C surface as UNMEASURED rather than clear."* A
clean detector run was never evidence the surface was clear, and this is the
fourth spelling found by a detector written to catch the previous blind spot.


## ADJUDICATED 2026-08-28 — PR #5895, on main at cdbdc84af1

This bean's thesis is CONFIRMED, on a live file, and its numbers have moved.

**The worked confirmation.** `probes/lambda_scale_substrate_probe` reads
`q-pinning-50-digit.witness.json` DIRECTLY. Re-running the flip experiment its
own `q0AnchorReason` cites as proof reports `clean` -- while the producer is
hard-pinned to muon, and `q0_anchor_manifest.json` says `ideal_muon`. That is
this bean's defeater #2, live, with the false negative it predicts. Relabelled
`muon`.

**The numbers have moved since 2026-08-23; do not quote the old table.** This
bean recorded 6 producers with a HARDCODED muon literal. Measured today through
`_source_normalise.code_only`, four of those six (`probe_he4_magic_baryeven_prune`,
`qbeta_c3_rung_structure_analysis`, `qbeta_habiro_f_from_shape_collapse`,
`qbeta_rung1_div25_framing_squared_test`) carry NO q0 literal in code -- they
import `Q_50_DIGIT_STR` from `q_parameter`. Main moved, not my edits: I had
changed nothing when I measured. The live count is 2 flip-blind
(`markov_identity_symbolic_probe`, literals; `lambda_scale_substrate_probe`,
pin-witness) after carving out auditor-marked producers.

**A THIRD defeater, which this bean did not have.** A q0-bearing name imported
from a PEER PRODUCER. The override resolves in the peer, at the peer's layer.
This is the inheritance path `qou-1c4y` records as "an unaudited inheritance
path ... worth its own pass; not attempted here" -- it is now audited.

**AND ITS FALSE POSITIVE, which is the reason the guard exists.**
`hoefsmit_symbolic.Q` is `sp.symbols('q', positive=True)`. A peer-import scan
keyed on the NAME indicts `chi_content_eigenbasis_probe` and
`eigenbasis_structural_lemmas_probe`, whose dispositions are CORRECT -- the flip
confirms both `clean` independently. I had these two on a suspect list before
reading line 57 of the module they import from. Symbolic-RHS guard + `--selftest`
pinning both directions now in `q0_independence_checker`.

**The strengthening this bean asked for is implemented**: `--flip-validity`
reports, per `independent` witness, whether the override can see its q0 at all,
names which defeater applies (the repair differs for each), and flags the case
where the witness's own reason CITES the flip while being blind to it.

Scope note: the source check is now available but is NOT yet a required half of
the disposition anywhere, because nothing invokes `q0_independence_checker` at
all -- `scripts/staleness-gates.sh` runs `anchor_flip_straddle_audit`, not this.
Wiring it is the remaining work on this bean.

---

## RE-MEASURED 2026-08-28 — narrowed, NOT closed

Detector half is **done** (`_is_unit_numerator` on main, PR #5494). The **primary**
claim — that `independent` tests *override-sensitivity* rather than
q₀-independence — is **still live**:

    witnesses stamped independent : 53   (was 37 on 2026-08-23)
      ... still carrying muon digits:  4   (was 9)

`fitted_labelled_canonical_audit`, `hardcoded_q0_literal_families_audit`,
`lambda_scale_substrate_probe`, `markov_identity_symbolic_probe`.

**Caveat:** `hardcoded_q0_literal_families_audit` is an audit whose SUBJECT is
hardcoded q₀ literals, so it legitimately contains them — very likely a false
positive of this test. Actionable is **≤ 3** until each is read individually. A
count from a detector is a hypothesis until one of its members has been opened by
hand; that is the lesson this arc kept re-learning.

Remaining work: require the env-invariance **and** a source check (no q₀-shaped
literal, no direct pinning-witness read). Both halves exist as scripts —
`q0_hardcoded_pin_audit.py` and `q0_muon_population_partition.py`.


## Re-measured 2026-09-06 — and the excursion turned up something bigger than the bean

Found by `scripts/bean-staleness-triage.py` (6th of 284 artifact beans).

### The bean's own numbers, re-measured

| | bean (post-#5457) | measured 2026-09-06 |
|---|---|---|
| witnesses stamped `q0Anchor: independent` | 37 | **149** |
| of those, still carrying muon digits | 9 | **7** |
| producers with a hardcoded muon literal | 6 | **1** (see below) |

**Do not read "7 carry muon digits" as 7 false positives.** Four of the seven
are audits *whose subject matter is q₀ literals* —
`q0-value-drift-audit`, `witness-float64-padding-audit`,
`hardcoded-q0-literal-families`, `fitted-labelled-canonical-audit`. Containing
the digits is correct for them; they report on files that have them. That is
this bean's own confusion one level up: a string match on a witness cannot
separate *pinned to muon* from *reporting about muon pins*.

Of the remaining three, two (`qbeta-ck-basis-constrained-pslq`,
`substrate/knot-volumes`) have producers that do **not** pin muon at all — the
witness mentions it for another reason. So the "hardcoded muon literal" class
is down to **one** site.

### That one site is a deliberate sample point, not a pin

`computations/markov/markov_identity_symbolic_probe.py:204` evaluates a
**symbolic residual** at five points — `proton_q0`, `muon_q0`, `1.3`, `0.7`,
`2` — to check it is identically zero. Two of the five are not anchors at all.
So `independent` is the **correct** disposition here and this is not a false
positive. Only the *label* was wrong: the literal is the **retired**
self-certified pin (`1.109978595557334…`), retired 2026-08-22.

### 🛑 My first fix was itself a defect, and a ratchet caught it

I re-pointed the literal to a 28-digit truncation of the live CODATA-2022 pin.
The precision gates then showed a gate red that had **not** been red in either
of my two earlier full runs: `witness-value copy ratchet`. Established by
stash-test, not assumed:

    with my change:     indexed 227038   NARROW 270
    without my change:  indexed 227034   NARROW 269

and the 28-digit string appeared in **exactly two places, both introduced by
that edit** — the producer and its witness. That is ≤3 ⇒ NARROW, *"a computed
value typed in, not read"*. The 16-digit canonical prefix, by contrast, is in
**150** witnesses (SHARED). So typing any truncation of a canonical constant
that is not already in the tree manufactures a fresh copy-defect.

**Corrected by fixing the LABEL instead** — `muon_q0` →
`muon_q0_RETIRED_PIN`, value untouched, no numeric literal introduced. NARROW
back to **269**. Only the label was ever wrong.

### 🔴 The real find: this witness's `peel` values are ~2× stale

Regenerating it moved numbers at sample points **that did not change**:

| q | committed | recomputed |
|---|---|---|
| `proton_q0` | 1.1457596924573008697 | **0.62932840220292191817** |
| `1.3` | 3.3688168001572002037 | **1.277736943233662226** |
| `0.7` | −4.7449410256554617359 | **−0.3531913855255301353** |
| `2` | 116.33458984375 | **51.77927734375** |

**This is not my edit.** A label rename cannot change `peel` at `q = 2`, and
`peel` is computed *before* the sample loop, so the list cannot reach it. The
committed witness records values the current code does not reproduce — import-
cone drift, the class AGENTS.md says actually bites.

**The verdict is robust; the intermediates are not.** The assertion
(*identity holds identically in q*, 2/2 atoms) passes either way, because the
residual is identically zero regardless of `peel`'s normalisation.

**The regenerated witness is deliberately NOT committed.** A ~2× move in
recorded numbers does not land undiagnosed. Whoever picks this up needs to
identify which upstream changed — note the run costs ~9 min (the deuteron
bridge alone is 520 s).

## a3-magnitude drained (2026-09-05, session fervent-noether) — a PROTON-pinned false-`independent` this bean's muon-digit scan could not see

While fixing qou-v6wz (the qbeta-ck-basis-constrained-pslq false-`independent`), I re-scanned for the same audit-escape class. Found `a3_magnitude_berezinian_crossterm_probe` stamped `q0Anchor: independent` (boilerplate reason 'no q0-dependent field') with the exact fvk-selection/qou-zk51 comment '# no q0 in this producer's cone; stamp provenance only.' + `q0_anchor=False`.

CONFIRMED genuine by the anchor-diff (QOU_Q0_ANCHOR=muon vs =proton): 24 substantive fields move — inputs.q0/h/hbar_q and every results.natural_readings_scatter[*].correction/rho/abs_err_vs_rstar — at the ~1e-8 mu-p-tension level. It reads the anchor via Q_50_DIGIT_STR (env-sensitive through q_parameter), so the flip-test IS valid here (defeaters #1/#2 don't apply) and the movement proves override-sensitivity + q0-dependence.

WHY THIS BEAN'S SCAN MISSED IT: its still-carrying-muon-digits filter keyed on MUON literals. a3-magnitude is PROTON-pinned (stem not in ideal_muon => Q_50_DIGIT_STR resolves to proton), so it carries PROTON digits and escaped the muon-digit sweep — a genuine sub-case of the false-`independent` class this bean owns: proton-pinned false-independents, not just muon ones.

FIX (rides on PR #6824 with qou-v6wz): q0_anchor=False -> q0_anchor=None (resolve). It reads ONE pin (proton default), so `proton` is correct (NOT `comparison` — unlike fvk-selection which reads both). Now stamps q0Anchor:proton + q0Value; q0_anchor_consistency_audit does NOT flag it as a flip; witness numbers byte-identical (default was already proton). Stale comment corrected.

SEPARATE, NOT FIXED: a3-magnitude computes in float64 (Q0 = float(Q_50_DIGIT_STR), all scatter values ~16-digit) — a NO-FLOAT64 concern needing an mpmath refactor, out of scope for a stamp fix. Its q0-dependence at ~1e-8 is above the float64 floor so the anchor-diff is real, not noise. Worth its own bean.

STILL SUSPECT, unmeasurable here: `toffoli-lp-stability` — same boilerplate-independent + carries q0 in a scan[9].q + constants.q0_physical, but its producer exits non-zero (both pins) in this container, so I could not anchor-diff it. Needs a run in a working env before verdict.

## toffoli-lp-stability drained (2026-09-07, session fervent-noether) — the suspect from the a3-magnitude pass, CONFIRMED

The 'STILL SUSPECT, unmeasurable here' item from the a3-magnitude section is resolved. toffoli-lp-stability's producer needs numpy (via pyhecke.gram), absent in the prior container; installed it and ran the anchor-diff.

CONFIRMED genuine (QOU_Q0_ANCHOR=muon vs =proton): 49 substantive fields move — constants.q0_physical and the entire gram_matrix_at_q0 — at the ~1e-8 mu-p level. Stamped q0Anchor:independent (boilerplate reason) with the same copy-paste '# no q0 in this producer's cone' comment + q0_anchor=False. Third instance of the false-`independent` class (after qbeta-ck-basis-constrained-pslq / qou-v6wz and a3-magnitude).

DISTINCT AXIS from qou-3j5m. Commit 9ea4f724d4 (qou-3j5m, 2026-08-30) migrated toffoli's convention C->D straddle (gram/toffoli_diagonal/q_and_amplitude) and found 'the stability claim does not survive'. It did NOT touch the q0-anchor stamp — orthogonal. My fix is the stamp only; the C->D migration is theirs and untouched.

FIX: q0_anchor=False -> q0_anchor=None (resolve). Reads ONE pin (Q_50_DIGIT_STR -> proton default), so `proton` is correct (not `comparison`). Now stamps q0Anchor:proton + q0Value; q0_anchor_consistency_audit does NOT flag it; gram numbers byte-identical (default was already proton, only the producer's own timestamp/git_sha bumped). Stale comment corrected.

RUNNING TALLY of the false-`independent` drain from this session: qbeta-ck-basis-constrained-pslq (ambiguous, reads both), a3-magnitude (proton), toffoli-lp-stability (proton). All three were the identical copy-paste stamp block.

## Tractable 'visible-q0-value' set exhausted; the rest is this bean's detector territory (2026-09-07, session fervent-noether)

After draining qbeta-ck-basis-constrained-pslq / a3-magnitude / toffoli-lp-stability, the set of witnesses stamped q0Anchor:independent AND carrying a visible q0 fingerprint is down to 10, and 9 are known-FP-or-tracked:
  - 5 AUDITS whose subject IS q0 literals (fitted-labelled-canonical, hardcoded-q0-literal-families, undeclared-muon-pin-flip-risk, q0-value-drift-audit, witness-float64-padding-audit) — legitimately independent.
  - 2 qbeta (habiro-f-from-shape-collapse, rung1-div25) — qou-o922 PROVED-independent.
  - markov-identity-symbolic — resolved by the 2026-09-06 sibling pass above (symbolic residual at 5 sample points; independent is correct; only the retired-pin LABEL was fixed).
  - substrate/knot-volumes — hyperbolic volumes, q0-independent geometry; carries q0 for context.

The 10th, deltalambda/s5so3-geometric-wlambda-a4-helium (NEW, landed in the interim 1289 commits), is INDETERMINATE by anchor-diff and is THIS BEAN'S detector territory, not a bounded fix: boilerplate reason + parameters.q0 = the PROTON value, but the anchor-diff shows 0 substantive fields move — AND even parameters.q0 does not change muon vs proton, so the QOU_Q0_ANCHOR override does NOT reach its q0 (a hardcoded literal or an import path). That is exactly defeater #1/#2: a byte-identical flip does NOT prove independence when the override is not in the path. Needs q0_independence_checker --flip-validity (which names the defeater), not an anchor-diff. Handed here.

CHEAP PRE-FILTER for the systematic sweep: all 3 genuine drains carried the identical copy-paste stamp block — the comment '# no q0 in this producer's cone; stamp provenance only.' + q0_anchor=False. That signature spans 372 producers (grep), MOST legitimately independent (the q0_anchor=False branch exists for the ~196/287 that never reach q0, qou-iph3). It is not a defect list — but it is a cheap first sieve: intersect it with 'producer actually reads q0 / witness carries a load-bearing q0 field' before spending an anchor-diff. The mechanical 372-producer sweep is this bean's single-owner drain; not overlapping it.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Same: the `independent` q0 disposition classifier is pin-axis. Keep open, re-
home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## RETRACTION, same session — this bean was CORRECTLY parented and my verdict above was wrong (bean `qou-am5t`)

The 2026-10-10 verdict above says **REPARENT**, on the reasoning that this is the
q0/colour axis rather than the convention axis and therefore the wrong milestone.
**That reasoning is wrong, and `qou-cdx1`'s own title says so**:

> `MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)`

Its body states the three rulings explicitly — **R1** convention D canonical / C
excised, **R2** proton pin canonical, **R3** `bring_color_weighted` canonical.
So the milestone is a THREE-RULING milestone, not a C-excision milestone, and a
q0-pin bean (R2) or a colour-weight bean (R3) sits under it by design.

My §9 paragraph calling the shared milestone an artefact of the two rulings
"landing in the same message" had it backwards: they share a milestone because
the milestone was scoped to cover all three, deliberately.

**This bean stays under `qou-cdx1`. It is not re-parented, and the REPARENT
verdict above is withdrawn.** Everything else in that verdict — that it is live
and worth doing — stands.

Third correction of this session, and the same class each time: a claim about a
bean made without reading that bean's own primary text closely enough. The first
was `qou-m7py` (called satisfied off one grepped line), the second was the
66-unscoped paper classifier.

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)
