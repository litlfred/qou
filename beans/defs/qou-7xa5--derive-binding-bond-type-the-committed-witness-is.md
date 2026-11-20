---
# qou-7xa5
title: 'derive-binding-bond-type: the committed witness is a green PASS for a REFUTED law, and its numbers no longer reproduce (7.515 -> 1.795, ordering flipped)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-26T12:21:32Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Found 2026-09-26 while closing out `qou-udeg` (float64 upstream of a discrete
decision). `computations/derive_binding_bond_type.py` was the one candidate from
that arc I had NOT dismissed, because its T-vs-3He verdict is a float64-decided
ordering recorded as a bool. **The float64 concern is benign. Two larger defects
sit next to it.**

## 0. The float64 concern that brought me here: BENIGN, measured

The bond counts collapse the discriminator. T = (Z=1,N=2) gives
`(n_pp,n_pn,n_nn) = (0,2,1)`; 3He = (Z=2,N=1) gives `(1,2,0)`. The `n_pn = 2`
term is common, so

    B_T - B_3He  ==  B_nn - B_pp

Measured on a fresh run: `0.5635676573955835 - 0.6421150754085667 = -0.0785` MeV.
A separation of ~8e-2 is fourteen orders above the binary64 floor, so the
`float(Bk)` casts at lines 91 / 98 cannot flip the ordering. **Not a defect.
Do not "fix" the casts on precision grounds** — they are display/serialization
of a quantity whose decision margin is 1e13 x the arithmetic noise.

## 1. DEFECT A (the big one): the producer implements the REFUTED Delta-tr law

`bond_binding` (line 56-72) returns

    E0 * (tr_f - tr_a)          # Delta_tr, with E0 = m_e/(q0(q0-1))

where `tr_f` / `tr_a` come straight out of `binding_canonical.binding_canonical`.
That module's own banner, lines 4-5:

    "SUPERSEDED LAW - this module's `B_MeV` is `Q_beta . Delta_tr`, and that law
     is REFUTED. It is kept for provenance and comparison; do not quote `B_MeV`"

and `f7851e7fc5`'s message states the scope precisely: *"Only `Delta_tr =
tr_free - tr_atom` scales with them, and that is the REFUTED law this file is
marked 'do not quote' for."*

**Be precise about what is and is not claimed here.** This producer does NOT
quote `B_MeV` — it takes the raw traces and builds Delta_tr itself with `E0`
in place of `Q_beta`. So it evades the letter of the banner while implementing
the same refuted SHAPE. The live law is the log-RATIO

    B = E_0 * log(tr_free / tr_atom)

implemented in `computations/binding_log_free_energy.py`, and independently
visible in `binding_single_pipeline_comparison._bond_type_L` (bean `qou-7i9u`),
which computes `log(tf/ta)`.

The witness on `main` therefore records `allPassed: true` for a *discriminator
computed under a refuted law*. A reader grepping for a green bond-type result
finds one.

## 2. DEFECT B: the committed witness is STALE, and its verdict INVERTS

`computations/derive-binding-bond-type.witness.json` on `main`:

    computedAt        2026-06-22T04:26:20Z
    scriptHash        7359da319a6e
    scriptCommitSha   9e5351788e68
    allPassed         true
    B_T = 7.515056318972376   B_3He = 7.361247627849864   -> ordering MATCHES

Fresh run, this container, 2026-09-26:

    scriptHash        f9ce3deb4636          <- self-stale, real producer edit
    allPassed         FALSE
    B_T = 1.7946369645162918  B_3He = 1.873184382529275   -> ordering MISMATCH

    B_pp  2.3785162259 -> 0.6421150754
    B_pn  2.4913657010 -> 0.6155346536
    B_nn  2.5323249170 -> 0.5635676574

That is a ~4x move AND a **flipped bond ordering** (pp<pn<nn became pp>pn>nn).
No precision or environment change can flip an ordering; this is structural.

## 3. WHAT MOVED IT: import-cone drift, and it is already-known drift

`git diff 9e5351788e68 b4789d6023 -- derive_binding_bond_type.py` is hygiene
only and CANNOT produce 4x:

  - `from q_parameter import Q as Q0` -> `Q_MP as Q0`   (mpf pin; ~1e-16)
  - AME literals -> `codata_constants.AME_B_*_MEV_VALIDATION` (last-digit only:
    8.4818 -> 8.4817962, 28.29566 -> 28.2956624)

So `git diff <producer>` — the check AGENTS.md tells you to run — says
"cosmetic" and is WRONG here. This is textbook **import-cone drift**
(`qou-e9pp`), in the very module AGENTS.md uses as its worked example.

The mover is `computations/mass_at_3A_proper.py`, which supplies
`atom_braid_word_3A` — the word `binding_canonical` traces. Four commits since
the witness was computed, all in September, and two name the cause outright:

    9cefcf6cf0  2026-09-13  retract(qou-5c64, qou-gjkv): "the C->D component is
                            measurably zero" is FALSE -- the p-p bond IS z, and
                            its residual is z_D/z_C
    99e2ddc1d9  2026-09-13  correct(qou-5c64): "grouped reproduces ANY
                            pre-2026-09-05 number" is measurably too strong --
                            it misses 2026-06-15 by 1.151x / 1.481x

A **convention C->D move on the p-p bond** is exactly the kind of change that
re-orders pp vs nn, and a sibling has ALREADY MEASURED that pre-2026-09-05
numbers do not reproduce. This witness is 2026-06-22. So this is not a new
drift class — it is a known one with an un-swept consumer.

`binding_canonical.py` itself changed only by COMMENT in that window
(`f7851e7fc5`, "DECLARED, not switched", verified a no-op: word byte-identical,
`tau_p = 1.145759692457300869689` unchanged). Do not blame it.

## 4. DEFECT C (minor, display): the ordering line hardcodes its own `<`

Line 81-82:

    print(f"  ordering: B_pp={float(B['pp']):.4f} < B_pn={float(B['pn']):.4f} "
          f"< B_nn={float(B['nn']):.4f}\n")

Live output: `ordering: B_pp=0.6421 < B_pn=0.6155 < B_nn=0.5636` — values that
are DECREASING under asserted `<`. **Frame this honestly: the line was CORRECT
when written** (June: 2.379 < 2.491 < 2.532) and was falsified by the cone move
in defect 3. It is still a defect — a comparison operator should be computed,
not typed — and it is the same class AGENTS.md records for
`qbeta_ck_truncation_order_analysis.py` (hardcoded prose disagreeing with its
own computed table), but it is a stale assertion, not an author's error.

## 5. DISPOSITION — nothing changed, deliberately

The regenerated witness was **reverted**; the tree is clean. Regenerating a
derived artifact that belongs to someone else's arc (`qou-5c64` / `qou-gjkv` /
`qou-t29k`) is NOT covered by either exemption of the 2026-09-07
ASK-THE-OWNER directive, and a witness whose verdict flips `passed: true ->
false` is precisely the kind that wants framing rather than a quiet push.

**Do NOT simply re-run and commit.** Committing the fresh run would replace a
green PASS with a red FAIL for a discriminator that, per defect 1, is computed
under a refuted law — i.e. it would publish a red number that nobody should be
reading in the first place. The three routes, for whoever picks this up:

  (a) **Re-run and commit the red.** Cheapest (the producer is ~20 ms). Makes
      the corpus honest about the drift. Cost: publishes a red assertion for a
      refuted law, which invites someone to "fix" the law to make it green —
      exactly the fitting the 2026-09-05 directive forbids.
  (b) **Retire the producer to the log-ratio law.** Replace `E0*(tr_f-tr_a)`
      with `E0*log(tr_f/tr_a)` per `binding_log_free_energy.py`. This is the
      mathematically right move and is NOT mine to make: it changes what the
      producer claims, and the bond-type T-vs-3He discriminator under the log
      law has not been measured. Needs its own arc.
  (c) **Mark the producer superseded**, as `binding_canonical` already is, and
      leave the witness as the dated provenance record it is. Cheapest honest
      option; loses nothing, because nothing should be quoting Delta_tr.

**My judgement (not a finding): (c), then (b) as a separate arc.** (a) is the
worst of the three — it spends a commit making a refuted quantity's failure
official. Owner call.

## 6. BLAST RADIUS

Measured: no `content/`, `docs/audits/` or `.beans/` file names
`bond_type_reproduces_T_He3_ordering` or "bond-type discriminator", so the
green verdict is not cited anywhere. The exposure is a future reader grepping
witnesses for a passing bond-type result. Related: `qou-7i9u` (float64 in
`_bond_type_L`, the log-law sibling), `qou-e9pp` (import-cone drift class),
`qou-5c64` / `qou-gjkv` (the C->D p-p bond move that caused this),
`qou-udeg` (the float64-upstream-of-discrete arc this came out of).


## 2026-09-27 — ROUTE (c) TAKEN: marked SUPERSEDED. Stays in-progress (rule 13a).

Owner instruction "resolve issues". Of the three routes framed — (a) re-run and
commit the red, (b) migrate to the log-ratio law, (c) mark superseded — **(c)**,
mirroring the banner `binding_canonical.py` already carries for the same law class.

**TWO INDEPENDENT GROUNDS**, either sufficient, both checkable against a corpus
artifact without re-running anything:

1. **The FUNCTIONAL.** `B_xy = E_0·(tr_M_free − tr_M_atom)` is a constant times
   Δtr — the class `binding_canonical.B_MeV` is already marked REFUTED for:
   `tr_M` is multiplicative along the chain, binding is extensive, and
   `Δtr/tr_free = 1 − exp(−S)` is within 7.7e-4 of 1 by A = 11, above which Δtr
   does not mis-scale the binding, it does not *contain* it.

2. **The BOND COMPOSITION.** `C(Z,2) + Z·N + C(N,2) = C(A,2)` — the complete
   graph. `QOU.Mass.CoordinationSaturation.complete_graph_no_saturation`
   (verified present: 4 theorems, **0 sorries**) proves `ε·C(A,2)/A` exceeds
   every bound, so no `B/A` plateau exists and observed saturation refutes it
   structurally, not merely at ⁴He.

   **SCOPED:** that Lean is stated for a UNIFORM `ε` and this module has three
   bond energies. The extension is a one-line monotonicity argument and it is
   MINE, not the theorem's — with all three positive (measured 0.6421 / 0.6155 /
   0.5636), `B(A) ≥ min·C(A,2)`, so the theorem applies at `ε = min`. Do not
   restate this as though the Lean covered three types directly. The
   replacement's composition is a CHAIN (`(Z−1), 1, (N−1)`; `A−1` bonds, bounded
   degree), which matters as much as the `log` does.

**DRIFT RE-MEASURED, and the headline assertion has FLIPPED.** Committed witness
`computedAt` 2026-06-22, `allPassed: true`; fresh run reports FAILURES, and the
module's whole purpose — the T-vs-³He discriminator — goes MATCHES → **MISMATCH**:

    B_pp 2.3785 -> 0.6421    D   +12.0% -> -72.3%
    B_pn 2.4914 -> 0.6155    T   -11.4% -> -78.8%
    B_nn 2.5323 -> 0.5636    3He  -4.6% -> -75.7%
                             4He -47.4% -> -87.0%

Bigger than the "4×" I reported earlier from a partial read.

**NO REGENERATED WITNESS COMMITTED.** Ran it twice to measure, reverted both
times. Publishing a red for a law already known wrong is noise, not a finding.

**Also fixed (exemption 2, not tidying):** the `ordering:` line hardcoded `<`
between all three bonds — true when written (2.379 < 2.491 < 2.532), false now
(0.642 > 0.616 > 0.564). The producer printed a false statement one line below
the numbers refuting it. Operators now derived, comparing mpf not display floats.
Print-only, so no witness field moves.

**NOT fixed:** the witness's 17 raw float64 fields (the run's own ratchet warns).
Serializing them correctly only takes effect by regenerating the witness, which
the paragraph above forbids. Recorded in the banner instead.

**Scope (a), not (b):** bond-TYPE decomposition is NOT excluded as an ingredient —
the three derived sub-braid traces are the same objects the log-ratio law
consumes. What is excluded is `constant × Δtr` summed over the complete graph.

**STILL OPEN — route (b)** (port the bond-type decomposition onto the log-ratio
law) is a separate arc and has not been taken. Bean stays in-progress.

Commit `7df1e2f5f5`.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8296, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
