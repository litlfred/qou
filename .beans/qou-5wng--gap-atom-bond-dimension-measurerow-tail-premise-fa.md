---
# qou-5wng
title: 'GAP: atom_bond_dimension_measure.row_tail — premise false under D, float64 q0 cast, and it never ran'
status: completed
type: task
priority: normal
created_at: 2026-08-29T21:47:28Z
updated_at: 2026-08-30T03:17:59Z
---

FOUND 2026-08-29 via the witnessless-consumer list added to
`computations/audits/ylambda_threerow_frame_audit.py` on this branch. This file
emits no witness, so layers 2 (numeric) and 3 (dating) were both blind to it —
it is the seventh instance of the convention-D annihilated-stratum class, and
the first one that list caught.

## Three defects in one function, and the third explains the other two

`row_tail()` in `computations/atom_bond_dimension_measure.py`:

**1. Its stated premise is false under convention D.** The docstring opened
*"y_λ is the Wenzl PRINCIPAL Schur specialization (canonical Jones–Markov trace,
NONZERO FOR ALL λ)"*. Under D the Wenzl level is `r = 2`, so `y_λ = 0` exactly
for every partition with ≥3 rows. Measured at the proton pin: `max|y_λ|` over
the ℓ≥3 stratum is **0.0** at n=6 and n=9, against 0.115 and 0.0221 over all λ.

**2. `float(Q0)` fed a float64 into a computation.** Line 76 read
`y = y_lambda_at(n, float(Q0))` — the cast drops the 50-digit pin at digit 17
(`1.1099785827513808` against `1.109978582751380807591669…`). Not a display; the
value goes straight into the weight computation. NO-FLOAT64 applies to probes
exactly as to producers.

**3. IT NEVER RAN.** `y_lambda_at` is imported **nowhere** in the module — not at
module scope, not locally. `row_tail()` raised
`NameError: name 'y_lambda_at' is not defined` at its first atom, on every
invocation of `main()`. Note this is a genuine defect and not one of this
corpus's designed refusals: no guard the import cone defines raises `NameError`.

Defect 3 is why 1 and 2 survived the convention-D migration. A function that
always crashes is never read for its numbers, so nobody re-checked its claims.

## What the numbers actually are

Repaired (import added, `Q_MP` instead of `float(Q0)`), run end to end, exit 0:

    ROW-TAIL (>r-row contribution to |tr_M|, dps=40):
      atom     <=2 miss    <=3 miss    <=4 miss   free <=3 miss
      D      0.000e+00   0.000e+00   0.000e+00    0.000e+00
      3He    0.000e+00   0.000e+00   0.000e+00    0.000e+00
      4He    0.000e+00   0.000e+00   0.000e+00    0.000e+00

Identical at float64 and at 50 dps, so exact rather than a precision artifact.
The docstring claimed **0.2–3.4 %, growing with A**.

## The two claims, scoped separately — they do NOT fare the same

* *"the ≤3-row SU_q(3) restriction is a DIFFERENT trace, a 0.2–3.4 % error
  growing with A, invalid at the 1-ppQ floor"* — those figures are
  convention C and are kept in the file labelled as such. Under D the ≤2-row
  truncation is already exact, so **this measurement supports no error and no
  invalidity verdict**. The verdict may hold on other grounds; it does not
  follow from here. Scope (a).
* *"the free reference also carries >3-row content (≥ the atom's), refuting
  'binding lives in >3-row sectors'"* — the **conclusion survives** and is
  stronger under D (those sectors carry no weight at all), but the **evidence
  is now false**: neither atom nor free reference carries any >3-row content,
  so "≥ the atom's" compares two zeros. Do not cite this function as the
  measurement behind that refutation.

## Blast radius — measured, and it is one file

`structural()` and `numerical()` do **not** call `y_lambda_at` (one counts
Bratteli support, the other counts nonzero χ^λ), so the headline verdict
`χ_eff(k) = p(3k)` / the p(3A) wall is intrinsic is **unaffected**, and
`docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md` does not
carry the row-tail figures (checked). A corpus grep for the distinctive
phrasing and for `0.2–3.4` finds no other carrier.

## Done on this branch (PR #6033)

Import added; `float(Q0)` → `Q_MP`; docstring rewritten to state the D
measurement, keep the C figures labelled as convention C, and re-scope both
claims; `main()`'s summary lines corrected. Runs end to end, exit 0.

## Still open

Whether the *conclusion* "the ≤3-row SU_q(3) restriction is invalid at the
1-ppQ floor" is true on other grounds. This file no longer supports it, and I
have not looked for another support. That is the honest residue.


## Second instance from the same blind-spot list: threerow_sign_crossing_decomp.py

`computations/deltalambda/threerow_sign_crossing_decomp.py` asked *"which ≥3-row
partitions drive the deuteron sign crossing of
`F_D(q) = Σ_{λ⊢6,ℓ≥3} y_λ·χ^λ·Δ_λ`"* and sorted its rows by `|term|` to name the
dominant block. Under D that sum is identically zero, so the question has no
answer and the ranking was ordering round-off.

Measured 2026-08-29 at 70 dps, deuteron:

    lambda                Delta_l   term(q_lo)      term(q0)
    (3, 2, 1)                  16          0.0    2.16210e-71
    (4, 1, 1)                 -10          0.0   -5.14025e-72
    (3, 1, 1, 1)               10          0.0   -1.02723e-72
    ... all seven between 1e-71 and 1e-75, q_lo column exactly 0.0
    noise floor = 1.15324e-63   terms above it: 0 of 7

`(3,2,1)` printed at the top of the old ranking and reads as a structural
finding. It is cancellation residue.

**The parent was already repaired; this file was not, and the reason is the
blind spot.** `threerow_sign_crossing_probe.py` emits a witness whose committed
2026-08-25 run carries the PASSING assertion
`three_row_object_is_structural_zero`. So the parent knows. The companion emits
no witness, so layers 2 and 3 could not reach it and the repair stopped at the
file they could see. Same `mu3_door_budget` failure mode (PR #4673), one file
over.

**Repaired**, not deleted: noise floor scaled to `max|y_λ|` over ALL λ (scaling
to the ℓ≥3 entries would measure the residue against itself), fixed partition
ordering so no "dominant block" can be read off, per-λ values kept as evidence
OF the cancellation, and a non-zero exit if anything ever clears the floor —
that would mean the structural zero had stopped holding, which should not be
silent. Negative control: spiking one ℓ≥3 weight to 0.01 marks it `ABOVE`, names
`(4,1,1)`, and returns 1.


## Third file: markov_trace_gibbs_dynamics_probe.py — CORRECT as committed, latently fragile

Flagged with the `mu3_door_budget` signature (a `y < 0` filter plus row-hits).
It is **not** that failure mode. The file is convention-D-aware — it states that
the vanishing blocks are the ≥3-row ones under the level-2 Wenzl restriction,
uses `negs` to report that NONE are negative, and cross-checks
`ℓ(λ)≥3 ⟺ y_λ = 0`. Its verdict is properly scope-(b) with the invariant named
(a Gibbs state of a finite Hamiltonian is faithful; this one annihilates 7 of 11
blocks at n=6). Green as committed, and correct.

**But it tested for the zero with `== 0`, and it is green by accident of
spelling.** Measured at n=6, ambient dps 70, varying ONLY how q₀ is written:

    mpf(str(Q50)) inside workdps(60)   ->  0.0          <- what the file does
    float64 round-trip                 ->  0.0
    full-precision Q_MP                ->  1.09e-72
    mpf(Q50) at ambient dps            ->  2.19e-72

Under either of the last two, `== 0` gives:

    spelling                zeros(==0)  zeros(floor)  misfiled(==0)  misfiled(floor)  spurious E
    mpf(str(Q50))@dps60          7           7              0               0             0
    full-precision Q_MP          0           7              7               0             3
    mpf(Q50)@ambient             0           7              7               0             4

    correct answers:             7                          0                             0

So: `zeros` collapses 7 → 0; `misfiled` reports **NO** — a false alarm that the
vanishing blocks are not the ≥3-row ones, i.e. the file contradicting its own
correct thesis; and the `yl > 0` loop fires on 3–4 annihilated blocks, printing
`E_λ = -E₀ log(1e-72) ≈ 3000 MeV` as an energy level for a block carrying no
weight. A nuclear-scale number manufactured from round-off, in a probe whose
entire subject is which blocks carry weight.

Fixed with the same noise floor used elsewhere in the arc
(`max|y_λ| over ALL λ × 10^-(dps-8)`), applied to all three tests. Output is
byte-identical under the file's own spelling — same counts, same energies, same
verdict — and now correct (7 / 0 / 0) under all three spellings.

NOT a live wrong number: nothing committed was wrong. This is a latent failure
mode removed.


## Fourth and fifth: a RED GATE on main, and a stale rationale in 11 live files

### q0_anchor_gate_test.py was FAILING on main, and its message accused a Lean declaration

Its check 3 compared `mp.sign(y_λ)` across the two anchors over ALL partitions
and reported:

    FAIL: sign(y_λ) now differs between anchors — QOU.MassTheory.
          YLambdaSignThreshold.wenzl_sign is anchor-dependent after all

Measured at n=9: **all 25 disagreements are exactly the ℓ≥3 partitions, and in
every one BOTH values are below the noise floor** — proton residues of 1e-73 to
1e-147 against a muon leg of exactly 0.0. The 5 two-row blocks, the ones
carrying weight, agree. So it was reading `sign()` of cancellation dust and
reporting a refutation of a proved statement.

The underlying fact is convention D's: `r = 2` so `y_λ = 0` for `ℓ(λ) > 2`, and
that vanishing is a polynomial identity reached by CANCELLATION at finite
precision — whether the residue lands on 0.0 or 1e-75 depends on how q₀ is
spelled, so the two legs differ in their dust and nothing else. Related and
already adjudicated: `qou-ulxr` found the threshold lands exactly ON the content
lattice under D, so `wenzl_sign`'s `hnd` hypothesis fails and the parity there
is UNDEFINED, not merely zero — one more reason not to read a sign off it.

Fixed: signs compared only above the floor, annihilated stratum reported
separately. Gate now exits 0. Negative control: flipping a two-row weight's sign
at one anchor fails check 3 and NAMES the block — `[(9,)]` — with a message
distinguishing it from the annihilated stratum.

**Checks 1 and 2 also carried stale messages** ("served the muon cache",
"the cache must still be reachable"). There is no cache: the gated load moved
into the dead `_y_lambda_at_convention_C_HISTORICAL` and the live body computes
from whatever q it is handed. They are now correctly described as a
cross-implementation agreement test — still what would catch a re-introduced
cache, but not the cache-gating test they claimed.

### The stale rationale is in 11 live files

`two_row_support_recount.py` justified avoiding `y_lambda_at` as "(it serves a
muon-built cache when handed q_parameter.Q)". That is doubly stale: no cache,
and the cache FILE was itself re-derived to convention D and re-pinned to
PROTON in the same 2026-08-09 cascade. Measured, pairing the muon-cache phrase
with `y_lambda_at` within a 9-line window, excluding three sibling-agent
worktrees:

    computations/audits/q0_producer_pin_classifier.py
    computations/chi_dual_path_xref_audit.py
    computations/deltalambda/l1_ceiling_d_frame_remeasure.py
    computations/deltalambda/mu3_anchor_consistency_probe.py     <- legitimate: the historical incident
    computations/deltalambda/two_row_support_recount.py          <- fixed
    computations/probe_1b_li6_orthogonality.py
    computations/probes/binding_production_route_C_vs_D_probe.py
    computations/probes/binding_sum_C_vs_D_per_isotope_probe.py
    computations/q0_anchor_gate_test.py                          <- fixed
    computations/qbeta/qbeta_ladder_phase_from_wedderburn_weights.py
    computations/tr_m_wenzl_bridge_mpfr.py

Not swept here — the two in my audit scope are fixed and the rest are a bounded
follow-up. It matters because AGENTS.md warns specifically against acting on
that wording: promoting `y_lambda_at` to a muon identifier once reclassified
**56 clean producers**. Note `mu3_anchor_consistency_probe.py` is describing the
real 11.54 ppb straddle incident and its reference is legitimate history, not a
stale rationale — do not "fix" it.


## The stale-rationale count was MINE and it was wrong: 4 carriers, not 11

I reported "the same stale rationale is carried by 10 other live files". Reading
all of them in context, that number counts **retractions and history as
carriers** — the exact over-count the `_c_level_is_prose_only` work in this same
arc exists to prevent. A grep cannot tell a file stating a claim from a file
quoting it to kill it.

Measured, 11 live files pairing the muon-cache phrase with `y_lambda_at`:

**Already CORRECT — they quote the claim in order to retract it (2):**
  * `computations/audits/q0_producer_pin_classifier.py` — "THAT IS OUT OF DATE",
    then quotes the live body.
  * `computations/tr_m_wenzl_bridge_mpfr.py` — "CORRECTED 2026-08-23: THE CITED
    MECHANISM IS DEAD, THE GUARD IS NOT ... Verified by reading both bodies, not
    inferred."

**Legitimate history (1):**
  * `computations/deltalambda/mu3_anchor_consistency_probe.py` — describing the
    real 11.54 ppb straddle incident. Not to be "fixed".

**Genuine carriers, stating it as current behaviour (4) — FIXED here:**
  * `computations/chi_dual_path_xref_audit.py`
  * `computations/probe_1b_li6_orthogonality.py`
  * `computations/probes/binding_sum_C_vs_D_per_isotope_probe.py`
  * `computations/qbeta/qbeta_ladder_phase_from_wedderburn_weights.py`

**Mild, left alone (2):** `binding_production_route_C_vs_D_probe.py` and
`l1_ceiling_d_frame_remeasure.py` each state their OWN behaviour ("no muon-built
cache is read / consulted") and merely list `y_lambda_at` among things they do
not call. True as written; the stale claim is implied, not asserted. Editing
them would be churn.

**Plus the 2 fixed earlier** (`two_row_support_recount.py`,
`q0_anchor_gate_test.py`), so 6 corrected in total.

Note the prior art: `tr_m_wenzl_bridge_mpfr.py`'s correction cites "#5324, which
is auditing the same stale claim where it also appears in AGENTS.md" — and
AGENTS.md HAS been corrected (the `qou-c1ya`/`qou-vu19` note). So the doc side
was already done; what remained was this call-site residue.


## A NEW blind spot, one character wide — and I measured it wrong first

`computations/audits/witness_filename_blindspot_audit.py` (new). Every
witness-consuming tool here globs `*.witness.json`: the raw-float64 ratchet,
`witness_staleness_triage.py`, the q0-anchor classifier and ratchet, and layers 2
and 3 of the y_λ frame audit. A file carrying full witness provenance but named
`foo-witness.json` — hyphen, not dot — is invisible to all of them.

Measured against `origin/main`: **7 tracked files**, and **5 are the `y-lambda-*`
family** — the very subject of the audit that could not see them.

**The payoff question, answered, and it is mostly reassuring.** All five carry
**convention-D** values where a fingerprint is detectable. No C-frame
contamination is hiding here. One carries a declaration its own fields refute:

    y-lambda-wenzl-bridge-numeric-witness.json
      q0Anchor:       "independent"
      q0AnchorReason: "no q0-dependent field in this witness"
      /q0:            1.10997859555418051695830018898879867637876138498395

A `/q0` VALUE field, not a mention in a description — established by walking the
JSON and reporting the path, since "the token appears" and "the value is used"
are different claims. And **which** muon value matters: `…55541805…` is the
CODATA-2018 lepton-tower derivation, NOT the frozen canonical pin
`1.1099785955573347…`. AGENTS.md records three values all called "the muon q₀",
diverging at the 13th digit; calling this "the muon pin" would be the exact error
that section exists to prevent.

**I MEASURED IT WRONG FIRST, and the error is the one AGENTS.md names twice.**
The audit's first run reported **8**. The extra file was my own doing: running
`l1_ceiling_d_frame_remeasure.py` minutes earlier had ADDED provenance stamps to
`l1-ceiling-d-frame-remeasure.json`, which on `origin/main` carries **none**.
That file is not an invisible witness at all — it is unstamped output that
becomes stamped the moment anyone re-runs its producer. Measuring a corpus
property against a tree your own commands have mutated gives you a fact about
your session. AGENTS.md records this costing two retracted witness-staleness
rates (39 % and 73 %); this is a third. The audit now baselines from
`origin/main` by default and warns loudly under `--worktree`.

**Not fixed, deliberately.** Re-stamping is a producer-side declaration, which
per `qou-x5mi` costs a full re-run and inherits every environment difference —
four producers there did not reproduce their committed values under a changed
mpmath. Renaming is worse: any consumer reading the path breaks silently. The
audit reports; the fix is a scoped change.

## The ℓ¹ ceiling: 59 % is stale, the correction was measured, downstream was not updated

Re-ran `l1_ceiling_d_frame_remeasure.py`. Live D-frame ceilings at the proton
pin: D 0.5661, T 0.3604, ³He 0.6925, ⁴He 0.4335 — **worst case 69.2 %**, against
C's 0.516 / 0.358 / 0.592 / 0.406 whose worst is the **59 %** five docs still
quote. `docs/audits/2026-08-16-su-r-level-tower-gap-map.md:310` already recorded
`59 % → 69.2 %, still < 1 | measured | done; downstream artifacts need updating`
— and they were not.

Still-quoting: `2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md`,
`2026-08-07-two-row-projection-is-the-pairwise-cap.md`,
`2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md`
(×4), `2026-07-19-delta-lambda-barodd-sector-already-pruned.md`.

**Not swept**, per the `qou-3nva` precedent that dated audit docs are historical
records. The conclusion is unaffected either way — every D ceiling is still < 1,
so no reweighting of the N=2 partition sum reaches the target. Note the D ceiling
is LOOSER than C (`D_tighter_than_C_everywhere: false`), which is the direction
that makes the surviving conclusion meaningful.

Also corrected `l1_ceiling_d_frame_remeasure.py`'s own premise: it says the
committed ceiling witness is `q0Anchor: muon`, 2026-07-17. It is **proton,
2026-08-21** — and the script's own run confirms it (`committed y_lambda
reproduced by live D: True`).
