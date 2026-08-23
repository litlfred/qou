---
# qou-60r9
title: The branch adds 6 recorded assertion failures and the ratchet that sees them is advisory
status: todo
type: task
priority: normal
created_at: 2026-08-23T22:19:32Z
updated_at: 2026-08-23T23:52:00Z
---

`witness_failed_assertion_audit.py` is registered **advisory** in
`precision-gates.sh:145`, so nothing blocks on it. Measured 2026-08-23:

    origin/main                    28 NEW + 1 GROWN   (--strict exits 1)
    claude/mass-table-...-triage    34 NEW + 1 GROWN   (--strict exits 1)

Diffing the two NEW sets: **the branch adds exactly 6 and clears 0.** All six
landed in `93e24e23d` and are honest results of regenerating witnesses that had
gone stale — the corpus ceasing to lie, not breaking. That is precisely why they
must be RESOLVED and not baselined: the ratchet's own output says *"a witness
may not be committed with a recorded assertion failure. Fix the producer, the
tolerance, or the schema misuse — do NOT add it to the baseline."*

Each is a domain call. None should be closed by widening a tolerance without a
stated reason.

---

## 1. `m-p-substrate-identity-50dps` — the load-bearing one

    m_n_matches_codata_within_10ppb
      computed  501.43180043143343 ppb     expected 0.0     tolerance 10.0

The neutron mass from the parameter-free Kashiwara b² Q_β (n → p + e + ν̄)
misses CODATA by **50x its tolerance**.

Already bisected in `93e24e23d`: re-running at `QOU_COMPUTE_DPS` = 50, 60 and 70
gives 501.43180043143343 at every one, so precision is exonerated. The producer
is untouched by this branch and uses no native code. The witness was last
regenerated 2026-08-08 and its inputs were corrected AFTER: `codata_constants.py`
on 08-19 ("the canonical binding reference was hand-typed and 7 of 11 were
wrong") and `experimental_constants.py` on 08-22. **The old 2.4 ppb agreement was
computed against wrong hand-typed constants.**

So the question is not "why did this break" — it is whether the identity holds at
all once the constants are right. That is the single most consequential open
number on this branch.

## 2. `snappy-census-volume-verification` — comparing volumes against non-volumes

Six failures, all stage 2. **Stage 1 is perfect**: the producer's own SnapPy
volumes match the census to between 1e-50 and 1e-65, and snappy 3.3.2 IS
installed, so this is not a missing-dependency artifact.

Stage 2 compares `per-atom-hyperbolic-volume.witness.json` against the same
census values and gets absdiffs of 7.3051, 7.447, 5.5763, 11.027. Reading that
upstream witness explains why:

    Vol_p   =  0.02263780480881132     tag: principled-derivation
    Vol_n   = -0.11929656567536379     tag: principled-derivation
    Vol_D   = -1.1754776225650418      tag: manual-historical-volume-match
    Vol_T   = -2.7409598694596227
    Vol_3He = -1.9635842533032033
    Vol_4He = -3.529066500197784       tag: magic-A-formula

**Negative "volumes."** A hyperbolic volume cannot be negative. That witness no
longer holds hyperbolic volumes; it holds some derived or shifted quantity under
the same key names (`computedAt` 2026-08-16, producer
`per_atom_hyperbolic_volume_witness.py`).

So the audit is not failing — it is correctly reporting that its stage-2
comparison has become meaningless. Either the per-atom producer changed what it
emits without renaming the keys, or the values are wrong. Whichever it is, an
audit named *census volume verification* comparing census volumes to
non-volumes is the defect, and renaming or re-scoping stage 2 is part of the
fix.

## 3. `bond-edge-set-selection`

    he4_requires_more_than_complete_graph
      computed 1.647   expected 1.2   tolerance 0.05

L_required/L_complete for ⁴He. The assertion's own source text says "≈ 1.20 > 1:
even the complete graph under-binds". The direction of the claim still HOLDS
(1.647 > 1, more so than before); it is the hardcoded 1.20 that has moved. Likely
the cheapest of the six — the expected value looks like a frozen measurement, the
same defect class as the convention-C literal fixed in `9a5d18462`. Check whether
1.20 was ever derived or just recorded.

## 4. `rho-k-h3a-co-casimir-perknot-rerun`

    sum_density_independent_matches_parent        computed 0   expected 1   tol 0
    codata_residual_reproduces_minus_2p30_MeV     computed -2.35144747043267
                                                  expected -2.2986427  tol 1e-4

The second is a 0.053 MeV miss on a 1e-4 tolerance, against a target named for
its own value (`minus_2p30`). Same shape as #3: an expected number frozen from a
past run. The first is a structural mismatch and is the more informative of the
two — a density-independent sum no longer matching its parent.

## 5. `qbeta-kc19-phib-departure-bridge`

    anchors_reproduced_vs_saddle_witness   computed 0.0  expected 1.0  tol 0.5
    source: S(anchor) from c3_target_at matches the committed saddle witness
            S_target to 1e-6

A cross-witness agreement check that no longer agrees. Note the committed saddle
witness is one side of it, so this may be upstream staleness rather than a
computation change — check the saddle witness's `computedAt` against the q0
re-pin dates before touching the producer.

## 6. `qbeta-sym-part-hecke-natural-form`

    three_hecke_natural_forms_all_match_upstream_sym
      computed 0.0   expected 1.0   tolerance 0.0
      source: Exact algebraic identity verified via sympy after q->t^2 substitution

An EXACT algebraic identity, tolerance 0, now false. Exact identities do not fail
for numerical reasons, so this is either a genuine algebra change upstream or a
substitution that stopped applying. Given the 2026-08-09 convention C → D
excision moved every `y_lambda_at` consumer, check that first — it is the same
root cause that rotted the frozen constant in `qbeta_jacobi_anger_tower_general`
(fixed in 9a5d18462) and it lives in the same directory.

---

## The gate half

`precision-gates.sh:118` states the flip-to-blocking condition: *"FLIP TO
BLOCKING WHEN THE NEW-OFFENDER COUNT REACHES 0 — i.e. when a plain run reports
no witness outside the baseline."*

That cannot be met from this branch alone: **28 of the 34 are already on
`origin/main`**, so draining the branch's 6 leaves the gate red for reasons this
branch did not cause. Two separable pieces of work, and only the first belongs
here:

  1. THIS BRANCH: resolve the 6 above. Then the branch adds nothing to the
     count, which is the standard the other gates in this family are held to.
  2. SEPARATELY: drain main's 28 (bean `qou-ad4t` is the existing triage), then
     flip to blocking.

Until then this remains the one gate family where a PASS -> FAIL can land with
every blocking gate green — which is the complaint `qou-a31p` was opened for.


---

## Two more, both bisected (2026-08-23). Branch total 8, one resolved.

### 7. `cyclic-intertwiner-verify` — PROMOTED TO ITS OWN BEAN, **qou-w701**

Not bookkeeping. `3dcf933c5` (2026-08-10) rewrote five `a_operator_gauge_align`
interface constructions from colour-blind `-h/2` to `-h(1-δ/2)/2` and DEFERRED
re-verifying the 1.5e-49 reconstruction figure, writing "expectation is not
measurement". The measurement has now been taken and the expectation is
refuted: h6 residual **6.7123064e-49 -> 0.0011504265**, 46 orders of magnitude,
identical at `QOU_COMPUTE_DPS` 50/60/70 so precision is exonerated. The same
commit predicted the failure scale ("~1e-4 scale of the colour weighting"), and
1.15e-3 is that scale. One leg of the pairing is still colour-blind.

Nothing in the staleness family could have caught it: the producer's own hash
barely moved (only `set_compute_dps()`), and the drift axis does not follow
IMPORTS. It took running the thing.

### 8. `alpha-em-b2-canonical-scale-ratio` — stale pass, plus pre-existing schema misuse

Two separate things, and only one is a change.

**Schema misuse, PRE-EXISTING.** `K3_markov_canonical_pins_computed` has
`computed` = a vector of three numbers against `expected` = the prose string
"three declared intrinsic candidates". At HEAD (computedAt 2026-07-25) it was
already that string, with `passed: true`. So `passed` has never been a function
of `computed` vs `expected` — the producer sets it from its own verdict logic
and the two fields are decorative. Not introduced by any regeneration.

**Stale pass.** One number in the vector moved, the first pin only:

    HEAD  y_(4,1)(q0) = 0.10937853185894286   (~ 7/64 = 0.109375)
    NOW   y_(4,1)(q0) = 0.12498539716794711   (~ 1/8  = 0.125)
    the other two pins are byte-identical

and the new value arrives certified by the producer's own output: "with
tr(1)=1 certified: sum_lam y_lam*f^lam = 1 to 5.0e-31". The old one predates
that certification. Cause is the same convention C -> D migration as #6:
`c8b99ecb5` (2026-08-10, "the nuclear layer's root cache was serving
convention C past its own gate") and `36844baad` (2026-08-09, "wire the
symbolic convention-D solver"). A C-era 7/64 was being served past its gate; D
gives 1/8 and satisfies the trace normalisation.

### Running tally

    main                          28 NEW + 1 GROWN
    branch, this session's start  34 NEW
      -1  qbeta-sym-part-hecke-natural-form   RESOLVED in cffc1265f — the exact
          identity was re-indexed by convention D, not refuted; six sympy
          identities verify to 0 and the C forms are retained under their own
          assertion against the recorded C-era sym
      +2  the two above
    branch now                    35 NEW

**The C -> D migration is now the single largest cause on this list** — #6, #8
and the `qbeta_jacobi_anger_tower_general` frozen constant fixed in 9a5d18462
all trace to it, each a downstream artifact that was never regenerated after
the 2026-08-09 owner ruling. Anything on this list that touches `y_lambda_at`,
`gram.TR_M` or a `habiro-coefficients-atomic` descendant should be checked
against that ruling BEFORE it is treated as a defect.


---

## Three more (2026-08-23, later). Branch total 10; the ledger below is current.

### 9. `atomic-tr-m-helium4-canonical` :: `abs_tau_4he_positive` — stale pass, C→D

    HEAD (computedAt 2026-05-25)  computed 0.1538719675410952  exp 0.15 tol 0.1  PASS
    NOW                           computed 0.4185152019887448  exp 0.15 tol 0.1  FAIL

A tr_M witness, so the C→D pre-check applies and clears it: the recorded pass
is from 2026-05-25, two and a half months before the 2026-08-09 ruling, and
its producer has not been touched since 08-02. Nothing about the producer moved
the number; the tr_M underneath it did.

### 10 + 11. `borromean-axial-coupling` :: `g_A`, `lp_duality_gap_zero` — PROMOTED TO **qou-g8bk**

Not a numeric regression: a q₀ re-anchoring. At HEAD the witness declared
`q0Anchor: "muon"` while computing at the PROTON value (1.1099785827513808 in
its own `char_on_basis[1]`); the regeneration is the first time its numbers and
its declared pin agree. Bean tnjb's exact hazard, caught on the correcting
side.

But the corrected result does not stand up: at the declared muon anchor the
operator-selection LP DEGENERATES — `x_star[0]` sits at exactly −1,000,000, the
box bound, and the duality gap is 0.0209 against 1e-10. So g_A = 1.0 was
obtained at the wrong anchor and 0.58 is not a result either. Owner decision
required; see qou-g8bk.

## Ledger

    main                                      28 NEW + 1 GROWN
    branch at session start                   34 NEW
      -1  qbeta-sym-part-hecke-natural-form   RESOLVED (cffc1265f)
      +2  cyclic-intertwiner (-> qou-w701), alpha-em-b2
      +3  atomic-tr-m-helium4, borromean x2 (-> qou-g8bk)
    branch now                                38 NEW

Causes, for whoever drains this:

    convention C -> D migration    4   (#6 resolved, #8, #9, + the frozen
                                        constant fixed in 9a5d18462)
    q0 anchor correction           2   (#10, #11 — same root, one producer)
    deferred verification failed   1   (#7, qou-w701 — a real open defect)
    frozen expected value          2   (#3 bond-edge-set, #4 rho-k-h3a)
    schema misuse, pre-existing    1   (#8's vector-vs-prose assertion)
    genuinely open science         2   (#1 m_n at 501 ppb, #2 snappy stage 2)

**The C→D migration remains the single largest cause.** Anything on this list
touching `y_lambda_at`, `gram.TR_M` or a `habiro-coefficients-atomic`
descendant should be checked against the 2026-08-09 ruling BEFORE it is treated
as a defect. Note `gram.TR_M` has **~70 live importers**, not zero — an earlier
count of "all under `_deprecated/`" came from a `head -12` on a sorted grep and
was wrong.


---

## Batch-1 drain results (2026-08-23, final). Six more, five of them textbook stale passes.

### 12–15. `binding-depth-stratified-*` ×4 — the AME correction landing on the deuteron

    data_loaded   2.22456607 -> 2.2245662   tol 1e-10
    source        "AME 2020 deuteron binding"

All four computed **2026-06-22**, two months before the 2026-08-19 correction
whose own message says the canonical binding reference was *"hand-typed and 7
of 11 were wrong"*. This is that correction reaching the deuteron. The cleanest
instance of the class on this list.

### 16. `mass-from-q-symbolic` ×2 — a 4-month-stale witness with an anchor question under it

    HEAD computedAt 2026-04-14

    ℏ_q² = Vol(4_1)/(m_μ/m_e)                 0.00981718851347867 -> 0.009817186454275078
    m_μ/m_e from Vol(4_1)/ℏ_q² (self-consist) 206.768283          -> 206.7683263706738

HEAD's 206.768283 IS the CODATA muon/electron ratio; the new value misses it by
~4.4e-5 (2.1e-7 relative). Note the same witness records
`q₀ = 1/(1 - ℏ_q) = 1.1099785827513808` — the **proton** pin. If ℏ_q is now
derived at the proton anchor while the assertion compares against the
muon-defined ratio, this is the qou-g8bk story again in a second producer.
Worth checking against `q0_anchor_manifest.json` before treating it as
anything else.

Attribution unresolved: the witness was rewritten at 22:40:23 and its producer
appears in no run log I or the drain agent kept. Recorded here so it is not
lost.

## Ledger

    main                                       28 NEW + 1 GROWN
    branch at session start                    34 NEW
      -1  qbeta-sym-part-hecke-natural-form    RESOLVED (cffc1265f)
      +2  cyclic-intertwiner (qou-w701), alpha-em-b2
      +3  atomic-tr-m-helium4, borromean x2 (qou-g8bk)
      +5  binding-depth-stratified x4, mass-from-q-symbolic (x2 assertions)
    branch now                                 43 NEW

## Causes, updated

    convention C -> D migration       4   (one resolved)
    q0 anchor correction              2-4 (borromean x2 confirmed;
                                           mass-from-q-symbolic x2 suspected)
    stale input correction (CODATA/AME) 5  (binding-depth x4, and m_n at 501 ppb
                                            is the same correction's largest hit)
    deferred verification failed       1   (qou-w701 — a REAL open defect)
    frozen expected value              2
    schema misuse, pre-existing        1
    genuinely open science             2

**Only ONE of the 15 diagnosed is a live defect** (qou-w701). Everything else
is the corpus ceasing to lie: a stale witness meeting corrected inputs, a
convention ruling, or an anchor being applied for the first time. That is worth
stating plainly, because a ratchet counting 43 reads like 43 regressions.


---

## Two RESOLVED, and the C→D count reaches eight downstreams

### `tau_L4_matches_independent_f64_measurement` — RESOLVED (bf3c70c8c)

Reported as a fresh flip during the drain:

    HEAD (computedAt 2026-08-01)  computed 1.000145897598652  expected 1.000145898  PASS
    broken                        computed 1.0001284313359748 expected 1.000145898  FAIL

Off by 1.75e-5 against a 5e-08 tolerance — 350x — and stable to every digit at
`QOU_COMPUTE_DPS` 50/60/70, so precision was never in it.

Cause: `a4_brunnian_deficit_closed_form.py:402` held `measured = 1.000145898`,
a 10-digit copy of `tau_L4` from `a4-h12-brunnian-deficit-measure.witness.json`.
`36844baad` (2026-08-09) wired the convention-D solver into the pipeline; the
literal came from the C-era measurement.

**Re-running the measurement probe under D settles it:**

    measured    tau_L4 = 1.0001284313359779421818005266796628820822874564922
    closed form        = 1.0001284313359748

~14 significant digits, a difference of ~3.1e-15 against a 5e-08 tolerance.
**The identity was never refuted; only the copy was stale.** Fixed the same way
as the qbeta constant: the producer now READS the measurement witness instead
of freezing a copy of it.

Worth recording why the measurement witness had gone two weeks without a
regeneration: it records its producer under a `producer` key rather than
`scriptFile`, so it is one of the **22 UNRESOLVABLE** witnesses — nothing can
map it back to a producer, and it has therefore never appeared as stale. Its
producer exists and runs in 163 s. That is bean qou-nb4s's cost in miniature.

### `cyclic-intertwiner-verify` — RESOLVED (a819eb1ab), see qou-w701

The one live defect. A sixth p-n interface construction, colour-blind, in the
verifier rather than in `a_operator_gauge_align`. h6 residual
0.0011504265 → 6.7076893e-49.

### Also accepted, not flips: three more C→D nucleus atoms (f6f629021)

`nucleus_real_sdp --atom {deuteron,he4,tritium}`, each emptying
`negative_norm_blocks` and `sign_flip_conjugate_pairs` to `[]` as tr_M moves —
the same signature as he3. Sixth, seventh and eighth C→D downstreams.

## Ledger

    branch NEW at its peak                     43
      -1  qbeta-sym-part-hecke-natural-form    (cffc1265f)
      -1  cyclic-intertwiner-verify            (a819eb1ab — the live defect)
      -1  tau_L4_matches_independent...        (bf3c70c8c)
    branch now                                 40

## Causes — final tally of the 17 diagnosed

    convention C -> D                  7   (3 now RESOLVED)
    stale CODATA/AME input             5
    q0 anchor correction             2-4
    frozen expected value              2   (both were C->D literals; counted once above)
    schema misuse, pre-existing        1
    genuinely open science             2
    LIVE DEFECT                        1   (RESOLVED)

**The C→D migration of 2026-08-09 is the single largest cause on this branch,
and every instance is the same shape: a downstream artifact — a witness, a
frozen literal, or one leg of a paired computation — that was never
regenerated after the ruling.** Anything remaining on this list that touches
`y_lambda_at`, `gram.TR_M`, or a `habiro-coefficients-atomic` descendant
should be checked against it BEFORE being treated as a defect. `gram.TR_M`
has ~70 live importers.
