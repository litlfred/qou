---
# qou-8chw
title: 'DEFECT: compute_tr_m_via_branching is BAR-INVARIANT -- returns identical values at q and 1/q, disagreeing with the transfer by 387x at 1/q0'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:42:01Z
updated_at: 2026-08-24T12:16:22Z
---

MEASURED 2026-08-19. computations/canonical_tr_m_via_branching.compute_tr_m_via_branching(Z, N, q_val) returns IDENTICAL values at q and 1/q:

    q_val=None   -> 0.5750908722902753612501
    q_val=q0     -> 0.575090872290275362348
    q_val=1/q0   -> 0.575090872290275362348    <- IDENTICAL to q0
    q_val=1.5    -> 0.6872499967008388608549
    q_val=2.0    -> 0.879272760520779915328
    q_val=0.5    -> 0.879272760520779915328    <- IDENTICAL to 2.0

So q_val IS honoured in magnitude (1.5 and 2.0 differ) but the function is BAR-INVARIANT. The transfer path gives tr_M_atom(D) at 1/q0 = -0.001480853171161937, so the two disagree by 387x at the bar image while agreeing to 1.4e-4 at q0.

WHY THIS MATTERS BEYOND ITS OWN CORRECTNESS: I reached for this function as an INDEPENDENT ARBITER for the transfer value at 1/q0 (qou-r9dv) and it cannot serve -- a bar-invariant function corroborates nothing about bar. Worse, it agrees with the transfer AT q0, so a check run only at the anchor would look like confirmation.

WHICH IS RIGHT IS NOT DECIDED HERE. Evidence that the TRANSFER is right away from q0: the word demonstrably re-lifts at 1/q0 (12 of 23 deuteron letters change; flavor_split_leading is exactly bar-odd, f(1/q) = -q^2 f(q)), and the bond-product formula tr_free/tr_atom = PROD 1/(z + d_b) holds at 4.45e-31 over 16 nuclei A=2..10 using the bar image throughout. Evidence for BRANCHING at 1/q0: none found. But that is not a proof, and the branching path may be computing a deliberately bar-even object (its docstring says it returns |tr_M|, though abs alone does not explain it).

FIRST STEP: read what the function actually varies with q_val. If it is bar-even BY DESIGN, the q_val parameter should REJECT q < 1 or document the symmetry -- silently returning the q image value is the trap. If it is not by design, it is a bug in the q-threading.

Found while arbitrating qou-r9dv.


RETRACTED 2026-08-23 -- THE BAR-INVARIANCE DOES NOT REPRODUCE.

Re-measured on current main after rebasing this branch:

    q0     0.5751722439177720556      (bean recorded 0.5750908722902754)
    1/q0   0.03320366093055433826     (bean recorded the SAME as q0)
    |gap across the bar| = 0.541969

So the claim in this bean's headline is FALSE as of now. The measurement was
taken on a branch that predated main's qou-zck8 / qou-cds4, which ported the
H_6 pn A-operator extract off float64, regenerated it, and fixed its consumers
to parse the extract's decimal strings. Do not plan around the invariance.

AND THE RETRACTION IS GOOD NEWS. The value moved ONTO the transfer value:

    branching (now)  0.5751722439177720556
    transfer         0.5751722439177718708
    relative         3.2e-16

A sibling working the mass table, from the other side and knowing nothing about
this branch, landed on the same number the transfer path and the Hoefsmit /
markov-peel arbiter give. That is a FOURTH agreement on tr_M^atom(D) and it
strengthens the qou-r9dv refresh. Stated at the right precision: the branching
path's rho factor is NumPy complex, so this is agreement AT THE FLOAT64 FLOOR of
the arithmetic it uses -- not a 16-digit corroboration, and two consecutive runs
differ in the last few digits. Do not quote it as exact.

WHAT SURVIVES, and it is the part that mattered for qou-r9dv: THE COMBINER STILL
CANNOT ARBITRATE AWAY FROM q0. Three inputs carry q into the A=2 path; only two
receive q_val:

    y_lambda_at(6, q_val)                      <- q_val, and BAR-EVEN (0.0
                                                  departure at 50 dps, 11 parts)
    evaluate_word_matrix_np(mu, intra, q_val)  <- q_val
    A^lambda_{xi nu}(I)                        <- JSON LOADED FROM DISK, frozen
                                                  at the q it was generated at

For q_val != q0 the return is a HYBRID: a frozen operator at q0 contracted
against weights and blocks at q_val. Neither tr_M at q_val nor at q0. Same class
as the AGENTS.md layer-straddle rule, with q-values in place of anchors. At 1/q0
it returns +0.0332 against the transfer's -0.00148 -- it does not agree in SIGN.

The trap this bean named is therefore intact: at q_val = q0 the hybrid
degenerates to the correct value, so the function is right exactly where it is
usually tested, and it fails toward AGREEMENT with an independent path at the
anchor.

SECOND FINDING, unrelated to the bar. Of the two extracts on disk, the H_9 nn
one carries NO q0Value stamp at all -- a frozen operator that does not record
which q it was frozen at is invisible to every q0-drift check. Ten of the twelve
(n, interface) extracts are absent entirely, so the A=2 pn deuteron is the only
path this defect can currently reach; A >= 3 goes through the transfer.

THE FIX IS NOT A DOCSTRING. This bean's FIRST STEP allowed for "bar-even by
design, so document the symmetry". It is not by design and, post-qou-zck8, not
even bar-even: the operator is frozen. Honest minimum is to REJECT q_val != q0
with a clear error rather than return a number; regenerating A^lambda at
arbitrary q is the real fix and is separate, larger work. NOT done here -- I am
not touching a producer a sibling is actively regenerating without coordinating
first.

Probe: computations/branching_q_threading_probe.py -- ASSERTIONS PASS, exit 0.
Conclusions rest only on exact quantities (JSON fields, source facts) and
mpmath at 60 dps; the one float64 number is labelled as such.

STATUS: the original claim is retracted; the underlying defect is confirmed and
stays open, re-scoped to "q_val is not threaded into the A^lambda extract".


LIVE HALF CLOSED 2026-08-24 -- PR #5619, branch claude/alambda-q-threading-2026-08-24.

compute_tr_m_via_branching now REFUSES q_val off the extract's stamped anchor
instead of returning a hybrid. It compares q_val to the extract's own q0Value
and returns a clean error naming the cause and the alternative
(tr_m_atom_via_transfer.tr_m_atom_zn).

MY FIRST GATE WAS WRONG AND TESTING CAUGHT IT. Tolerance 1e-30 REFUSED
PRODUCTION'S OWN DEFAULT: the default sets q_val = float(Q_FLOAT), a float64
truncation ~1e-16 from the 50-digit stamp. 1e-12 separates cleanly (truncation
~1e-16 vs bar image ~2e-1). Verified on five values: production default OK,
50-digit q0 OK, bar image / q=1.5 / q0+1e-9 all REFUSED. Both live consumers
pass float(Q_FLOAT) and are unaffected.

THE "REAL FIX" DOES NOT EXIST, AND THE CORPUS SAID IT DID. I went looking to
build A^lambda at arbitrary q rather than merely guard, because
A_operator_extract_at_level's header says the correct non-fitted replacement is
the closed form A^lambda_{xi nu}(I) = Pi rho_lambda(I) Pi in
a_operator_categorical, "verified exact at 1e-49". BOTH HALVES OVER-READ:

  * categorical_A_interface is a `raise NotImplementedError` STUB with ZERO
    callers (only its own def and a TODO line reference it). Its docstring
    calls step 4 "the crux ~500 LOC".
  * the 1e-49 belongs to a DIFFERENT result -- the combiner identity at
    lambda |- 12 / A=4 in a_operator_recursive.py. What passes on the
    categorical route is the I = IDENTITY preflight, not the I != 1 interface
    case actually needed.

An agent reading the old wording concludes the replacement exists and needs
only wiring. It does not. Corrected in that header, and recorded in the probe
verdict so the next reader hits it before attempting to lift the refusal.

STILL OPEN in this bean: (1) implementing categorical_A_interface -- the ~500
LOC crux -- which is what would actually let A^lambda be built at arbitrary q;
(2) the H_9 nn extract carrying NO q0Value stamp at all, so no drift check can
classify it. Neither is touched here.

NOT CLAIMED: this does not adjudicate tr_M^atom(1/q0). That still rests on a
single method. The fix makes the combiner's unusability LOUD, not fixed.


RETRACTION 2026-08-24, SAME DAY: "the replacement does not exist" WAS WRONG.

I wrote, in PR #5619 and in two source comments, that A^lambda cannot currently
be built at arbitrary q because the closed-form construction
`a_operator_categorical.categorical_A_interface` is a `raise
NotImplementedError` stub with zero callers. The stub part is TRUE. The
conclusion is FALSE.

The working construction exists under a DIFFERENT NAME:

    a_operator_gauge_align.gauge_aligned_A_combiner_general(
        lam, n_inner, n_block, q_str, dps)

It takes q_str and builds the exact seminormal matrices, the class-sum isotypic
projectors, and the interface I_pn = sigma_{n_inner-1} - (h/2)*1 all AT THE
REQUESTED q. Verified by running it: 4 (xi,nu) blocks for lam=(4,2) at q_0, at
the bar image 1/q_0, and at q = 1.5 -- all fine. The closure-b design doc
(docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md)
records the deuteron categorical A as DONE, exact, 891/891 PASS at 1e-25.

HOW I GOT IT WRONG. I read the stub, saw zero callers, grepped for the 1e-49
figure, found it belonged to a different result, and concluded the replacement
was vapour. Every one of those observations was correct; the INFERENCE from
them was not. I never opened the design doc's verification plan, which says in
plain text that step 2 is done -- and the working function is two files away
under a name my greps for "categorical_A_interface" and "def categorical_A"
could not hit. A stale stub is not evidence of absence.

WHAT CHANGES:
  * The refusal guard in compute_tr_m_via_branching is now INTERIM, not
    permanent. It is still the right thing to have RIGHT NOW -- a loud refusal
    beats a silent hybrid -- but it should be lifted, not defended.
  * The remaining work is a WIRING job, not the ~500 LOC crux I claimed. Step 6
    (the operator-level V_xi (x) V_nu embedding) is what
    gauge_aligned_A_combiner_general already solved.
  * Both source comments and the PR body are corrected. A_operator_extract_at_level's
    header now carries a NAVIGATION WARNING pointing at the real function and
    away from the stale stub, since that stub is what misled me.

NEXT, CONCRETELY: replace `load_A_extract` in the A=2 path with a call to
gauge_aligned_A_combiner_general at q_val; regression-check tr_M^atom(D) at q_0
against 0.5751722439177718708 (four methods agree there); then cross-check the
bar-image value against the fine-Bratteli transfer's -0.0014808531711619370338.
If those agree, the guard comes out and qou-8chw's main finding closes -- AND
tr_M^atom(1/q_0) gains the SECOND independent method it has been missing.

The stale stub should also be deleted or made to delegate.


WIRING SCOPED 2026-08-24 (after the retraction above). Feasibility established,
integration specified, NOT implemented -- the remaining risk is gauge, and a
half-done adapter that silently moves tr_M would be worse than none.

CONVENTIONS MATCH -- checked before anything else, because a mismatch here
would make the regression test meaningless:

    builder  a_operator_gauge_align._d_pn(h) = -h(1 - avg_color_delta/2)/2
             i.e. the COLOUR-WEIGHTED p-n bridge (qou-gdtb, 3dcf933c5d)
    extract  sublemma-2-1-A-operator-extract.witness.json records
             "interface": "I = sigma_2 - h(1/2 - delta/4)"
             "interface_ctype": "averaged_weighted"
             "interface_d": -0.104458247769726289017834066290005644128

So the frozen extract was regenerated AFTER the colour-weighting change and the
two agree. Wiring the builder in is convention-consistent; it does not silently
swap a colour-blind interface for a weighted one. (Relevant because
3dcf933c5d missed two consumer sites -- one a real bug fixed on main, one filed
inert as qou-tqfm. This is not a third.)

BUILDER VERIFIED OFF-ANCHOR: gauge_aligned_A_combiner_general((4,2), 3, 3,
q_str, 50) returns 4 (xi,nu) blocks at q_0, at 1/q_0, and at q = 1.5.

INTEGRATION SPEC (the actual remaining work):

  consumer  compute_chi_lambda_via_branching reads
              extract_cache[(n, iface)]["results_per_lambda"][key]
            with key = str(list(lam)) or str(tuple(lam)) -- both conventions
            are already tried at canonical_tr_m_via_branching.py:286.
  builder   gauge_aligned_A_combiner_general(lam, 3, 3, q_str, dps) returns
            {(xi, nu): dict} for ONE lam -- so the adapter loops lam |- 6 and
            reshapes into results_per_lambda.

  THE RISK IS GAUGE, NOT PLUMBING. The closure-b design doc's own verification
  criterion says the categorical A must match the full-rank H_6 extract
  "modulo the V_xi (x) V_nu BASIS GAUGE". The builder is named
  gauge_ALIGNED_..., which suggests it already fixes a gauge -- but whether it
  is the SAME gauge the frozen extract used is unverified, and a mismatch would
  change tr_M silently while every shape check passes.

  So the first step is NOT to swap the call. It is: build A^lambda both ways at
  q_0 and compare entrywise. Only if they agree (or differ by a verified gauge
  transform) does the swap preserve meaning.

REGRESSION TARGETS for whoever does it:
    tr_M^atom(D) at q_0    0.5751722439177718708265353439861808891524943528928
                           (four independent methods agree at this value)
    tr_M^atom(D) at 1/q_0  -0.0014808531711619370338  (fine-Bratteli transfer;
                           currently SINGLE-METHOD -- this wiring is what would
                           give it a second)

Not started. The guard stays until this lands.


## 2026-08-24 — wiring landed, and it found a SECOND, larger freeze

Both q-freezes on the A=2 branching path are now fixed (`64867e938f`).

**1. A^λ (the one this branch set out to fix).** `build_A_extract_at_q`
constructs the extract at `q_val` from
`a_operator_gauge_align.gauge_aligned_A_combiner_general`. Gauge precondition
MEASURED before the swap, as I said I would: both constructions at q_0 over all
11 λ ⊢ 6 and all 35 (ξ,ν) pairs, 0 missing, worst entrywise diff **7.05e-51**.
Same gauge, no transform.

**2. h — found while checking why the fix did not close the gap.**
`per_nucleon_intra_word` built the per-nucleon word from `hecke_core.h`, a
float64 `q_0 - 1/q_0` MODULE CONSTANT, ignoring `q_val`. At the bar image the
true h is SIGN-FLIPPED, so the neutron's Hecke-negative letters `(1, -h, g)`
carried the wrong sign outright.

Against the transfer's `-0.0014808531711619370338`:

| A^λ | h | tr_M^atom(D) at 1/q_0 |
|---|---|---|
| frozen | frozen | `+0.0332037`  (21x off, wrong sign) |
| built | frozen | `+0.0331943`  (A^λ freeze is only ~3e-4) |
| built | threaded | `-0.00148039` (3.2e-4, sign agrees) |

**The freeze I chased was the small one.** A^λ moved the answer by 3e-4; h is
what inverted the sign. Both were invisible at q_0 because each degenerates to
the correct value there — the path failed TOWARD agreement with an independent
method exactly where it is tested.

## The regression target is NOT met — scope-(a), not closed

I scoped this bean as "the wiring is what would give the transfer's bar value a
second method". It gives it one **at ~3 significant figures, not 16**, and I am
recording that as a miss rather than a win.

3.2e-4 is **~10 orders above this computation's float64 floor**, so it is a real
discrepancy, not arithmetic: the `Σ_λ y_λ χ^λ` cancellation is only 2.06 orders
(max |term| 0.170 against a sum of 0.00148), putting the f64 floor on the result
at ~2.5e-14. Measured, not estimated.

**Still open:** a third q-carrying input is frozen, or the two constructions
genuinely differ off-anchor. `gauge_aligned_A_combiner_general` computes its own
`h = q - 1/q` from `q_str`, so it is not that one. Next candidates: `y_lambda_at`
at the bar image, and `_avg_color_delta()` (a module-level constant used by the
colour-weighted interface `_d_pn`).

Regressions clean: q_0 = 8.7e-17 vs the four-method target; default float64-Q
path = 3.8e-15. Precision gates: one RED (`q0-anchor flip`, 3 qbeta witnesses)
is pre-existing — identical on the stashed clean tree, none of the three touched.

The q guard survives as fallback-only, for (n_outer, interface) pairs the
builder does not cover (e.g. the still-unstamped H_9 nn extract).


## CLOSED — 2026-08-24, later the same day. Three freezes, not one.

The 3.2e-4 residual I reported above is closed. The third frozen input was
**δ, the flavour split** — one of the two candidates I named.

`_d_pn(h)` built the p-n interface shift from `_avg_color_delta()`, a LAZILY
CACHED MODULE GLOBAL evaluated once at q_0 and taking no q argument. So
`gauge_aligned_A_combiner_general(..., q_str, ...)` baked a q_0-pinned constant
into an interface it was otherwise building entirely at `q_str`.

δ **sign-flips** under q -> 1/q: `+0.0013757108070270960086` at q_0,
`-0.0016949478760214730243` at 1/q_0 — a 1.5e-3 relative move in the shift.

### The full ladder, against the transfer's `-0.0014808531711619370338`

| A^λ | h | δ | tr_M^atom(D) at 1/q_0 | rel |
|---|---|---|---|---|
| frozen | frozen | frozen | `+0.0332037` | 21x, wrong sign |
| built | frozen | frozen | `+0.0331943` | 21x |
| built | threaded | frozen | `-0.00148039` | 3.2e-4 |
| built | threaded | threaded | `-0.001480853171161933678` | **2.27e-15** |

### The bean's target is now genuinely met

`tr_M^atom(D)` at `1/q_0` has a **second independent method** at 2.27e-15 — not
the ~3 significant figures I recorded an hour ago, and not the miss I logged.
The fine-Bratteli transfer's bar value is no longer single-method.

### What the defect actually was, for the next reader

Not one bug — a **class**. Three separate q-carrying inputs on one path were
each pinned at the anchor by a different mechanism: a frozen JSON, a module
float64 constant, and a lazily-cached global. Each was individually invisible at
q_0, because each degenerates to the correct value there. The path therefore
failed TOWARD agreement with an independent method exactly where it is normally
tested. Finding one did not predict the others: I fixed A^λ expecting closure
and got 21x; fixed h expecting closure and got 3.2e-4.

`d_for_ctype`'s `delta=` docstring already described this straddle **precisely**,
for q-symbolic callers. It was reached by a numeric off-anchor caller instead —
the warning was right and the guard was simply never wired to this path.

### Scope respected

The owner-gated `_avg_color_delta()` default is UNTOUCHED (AGENTS.md §"q₀ anchor
convention"; its own "Do NOT change this default"). The fix adds an optional `q`
argument. Threading is a **provable no-op at the anchor** —
`flavor_split_leading(q_0)` and `_avg_color_delta()` measured EXACTLY equal
(diff 0.0 at 60 dps) — which is why all six call sites in the module could be
threaded without re-verifying each.

Verification: `verify_combiner_identity(dps=50)` 891/891, 0 failures, max
residual 3.07e-49 vs a 1e-25 tolerance. q_0 = 8.7e-17 vs the four-method target;
default float64-Q path 3.8e-15. Both unchanged.

**Still open (separate, unchanged):** the H_9 nn A-operator extract carries no
`q0Value` stamp, and the stale `a_operator_categorical.categorical_A_interface`
stub should be deleted or made to delegate.


## Correction to my own entry above (same day) — the H_9 stamp item was mis-scoped

I recorded "the H_9 nn A-operator extract carries no `q0Value` stamp" as an open
item under this consumer. **It is not a live risk in this consumer**, and I
should have checked the reachability before writing it down.

`compute_tr_m_via_branching` returns via the fine-Bratteli transfer for `A >= 3`
**before** the extract load, so `n` at that point is ALWAYS 6 — no H_9 entry is
reachable from that function at all. Of the 13 registered extracts, 11 are absent
from disk (they fail loudly), the H_6 pn deuteron is stamped, and only `(9,"nn")`
is unstamped and it cannot be reached.

**Re-scoped, still open:** the unstamped file IS consumed by
`sublemma_2_1_h9_tritium_verify.py` and `sublemma_2_1_h12_helium_4_framework.py`.
Whether either threads q or is anchor-only is unexamined — that is the surviving
item, against those two files.

The guard was still made fail-closed on an unstamped frozen extract (`9cec747d2e`),
now correctly labelled forward-looking hardening: it catches an n = 6 entry added
without a stamp, or the deuteron extract losing its stamp in a regeneration. A
built extract carries `built_at_q` instead and stays inert.

## Also closed: the stale stub (`8723bb4967`)

`a_operator_categorical.categorical_A_interface` no longer raises — it delegates
to `gauge_aligned_A_combiner_general` (verified: max entrywise difference **0.0**
against the combiner for λ=(4,2), (ξ,ν)=((2,1),(2,1))). Deleting it would have
left the same trap for anyone grepping the design doc's function name, so it
delegates and carries the history in its docstring. p-n at n_block=3 only;
anything else raises with a message naming the design doc.
