---
# qou-4e5k
title: The paper claims three tr_M paths agree to machine epsilon; two committed witnesses disagree at 1.4e-4 on the deuteron
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T21:29:48Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

Found while regenerating the qou-mass vendor mirror (`qou-wpp2`): the mirrored
witness moved 99 lines, which sent me to compare it against its siblings.

## The published claim

`folio/quantum-observable-universe/mass-endomorphism/recomputed-low-isotope-mass-table.md:3`

  "three independent production paths to the Markov trace tr_M(B_K) at q = q_0
   **agree to machine epsilon** across the proton, neutron, deuteron, tritium,
   and 3He."

## Measured on origin/main 5b158ef06c, 2026-08-19

Two committed witnesses, both dated 2026-08-15, both declaring 50 dps, on the
same object:

    atom   atomic-tr-m-mpfr-50dps      low-isotope-mass-table      relative
    p      1.145759692457300869689     1.145759782287835504726     +7.84e-08
    n      0.987743688115809571634     0.987743756687661111334     +6.94e-08
    D      0.575172243917771870827     0.575090958682446712092     -1.41e-04

Machine epsilon at 50 dps is ~1e-50. The framework's own L1 target is 1 ppQ
(1e-15). The deuteron gap is **35 orders of magnitude** above the stated
agreement and **11 orders** above the L1 target.

## The deuteron gap is exactly the colour weighting

Feeding each witness its OWN p and n into `closed_form_tau_M(1,1,q0,tau_p,tau_n)`
so the only free variable is the p-n convention:

    atomic-tr-m-mpfr-50dps  D  ==  bring_color_weighted   to  6.0e-25   <== exact
                               vs strict_averaged             1.41e-04
                               vs chi_lambda_braid            1.71e-01

    low-isotope-mass-table  D  vs bring_color_weighted        1.41e-04
                               ==  strict_averaged      to    3.5e-09
                               vs chi_lambda_braid            1.71e-01

So `atomic-tr-m-mpfr-50dps` reproduces the canonical colour-weighted closed form
to 25 digits. The mass-table pair does not — it is 1.41e-4 away, which is the
per-bond weighted/averaged ratio (`+1.414947e-04`, independently computed) to
within 0.12%.

## The producer declares the weighting it does not appear to apply

`canonical_mass_table_extended.py` (which `low_isotope_mass_table.py` is a thin
subprocess wrapper over, so both witnesses come from it) contains **zero**
occurrences of `pn_convention`. Its own docstring says:

  "Composites (A >= 2) need the operator-valued `branching` combiner for the
   **color-weighted p-n interface** ... it linearity-splits sigma - h(1/2-d/4)*1
   into a sign-0 averaged term plus an identity term"

Declared behaviour and emitted number disagree. This is the shape the owner-ruling
audit flagged as a **convention hybrid** (`borromean_binding_recompute.py:98` --
"its own docstring DECLARES convention D ... Binding = tau(D) x bonds(C)").

Neither witness records a `pn_convention` parameter at all, so nothing downstream
can tell which frame it is reading. That is the lesson of `45789ddfa0`
(`convention_fingerprint`) unlearned one directory over.

## What I did NOT establish -- do not read past this

1. **Which one is right.** I have not shown that `closed_form_tau_M`'s
   `bring_color_weighted` and the branching combiner's weighting are the same
   object. The mass-table value is 3.5e-9 from `strict_averaged` -- close, but
   3.5e-9 is not 1e-50, so it is not simply "strict_averaged computed another
   way" either. It is near neither exactly.
2. **The free-nucleon gap has a different cause.** p and n have no p-n bond, so
   their 7.8e-8 / 6.9e-8 disagreement cannot be the colour weighting. Unexplained.
3. **Whether any cross-method check covers this pair.** If one exists and is
   green, that is a detector-blindness instance and belongs in the taxonomy.

## Where it belongs

`docs/audits/2026-08-15-detector-blindness-taxonomy.md` row 8 -- *"each entry
independently (R9) / entries disagreeing with each other"* -- names
`pyhecke.gram` as its example. This is a second instance of that class, in the
production mass table, and it reaches a published sentence.

Related: `qou-cds4` (S4, p/n convention) owns the convention question but is
scoped to `pn_convention` **assignment sites**; this producer has none, so S4's
grep does not see it.

## Next step

Decide which frame the canonical mass table should be in (S4 / ruling R3 say
`bring_color_weighted`), then either fix the producer or correct the content
block -- but **not** by relaxing the claim to fit the numbers. Whichever way it
lands, both witnesses must start recording their `pn_convention`.

## RESOLVED 2026-08-21 — the mechanism is a tolerance straddle, and the third path never ran

Chasing `binding_canonical.py` (the file `qou-cds4` says to read first) landed on
the root of this bean's finding. Recording the whole chain, including the two
places my own draft was wrong.

### The dispatch function exists TWICE, with tolerances 1000x apart

`_factor_from(c_f, d_f, g)` maps a crossing's numeric `d` to a symbolic factor.
Two copies:

    binding_canonical.py:111    tolerance 1e-6
    atom_nf_symbolic_D.py:67    tolerance 1e-3   (_D_HECKE_TOL)

Both branch on `abs(d_f + h/2) < tol` to recognise an `averaged` crossing. The
colour-weighted crossing is `d = -h(1/2 - delta/4)`, whose distance from `-h/2`
is `h*delta/4`:

    |d_weighted - d_averaged| = 7.190163e-05

**7.19e-5 sits exactly between the two tolerances.** So the same crossing is
handled two different ways by two copies of the same function:

    binding_canonical  1e-6  -> NO match -> falls through to sp.nsimplify(d)
                                            (keeps the weighting)
    atom_nf_symbolic_D 1e-3  -> MATCHES  -> rewritten as -h/2
                                            (SILENTLY DISCARDS the weighting)

Reachability confirmed, not inferred: `atom_braid_word_3A(1,1)` — the production
word builder — yields 23 crossings dispatching as
`{0: 11, -h/2: 4, -h: 7, FALLTHROUGH: 1}`. Exactly one weighted bond, the arc's
signature.

This is the `else:`-swallows-the-new-ctype shape again — the third instance after
`spectral_coordinates_all_atoms`' `else: M = np.eye(2)` (#5029) and the
`per_irrep_pole_atom` cemetery logic. Here it is worse, because the swallow is a
*tolerance*, so no `else` branch is even visibly involved.

### Measured: the four production paths, deuteron

    path                                        tr_M(D)                    weighting
    bridge (Rust/MPFR)              0.575172243917771870826535   weighted
    peel (markov_peel)              agrees with bridge to 6.1e-50   weighted
    symbolic (atom_nf_symbolic_D)   0.575090871629810316751633   BLIND
    mass table (canonical_..._ext)  0.575090958682446712091773   BLIND

    |symbolic - bridge|      = 8.14e-05      <- not machine epsilon
    |symbolic - mass table|  = 8.71e-08      <- the two blind paths do not agree either

The symbolic value is **bit-identical** to `closed_form_tau_M(..., "strict_averaged")`
computed independently, which confirms the 1e-3 tolerance is producing exactly the
colour-blind factor.

### Why nothing caught it: the third path never ran, and there is no assertion

`atomic_tr_m_mpfr_50dps.py` runs the symbolic path only under `if also_symbolic:`.
In the committed witness, `symbolic_check.abs_diff_vs_bridge` is **absent for all
five atoms** — it was never enabled. Only two paths ran, and those two are both
weighted, so they agree at ~5e-50 and the witness looks clean.

Worse, the check has **no threshold**. It computes
`diff = abs(tr_sym_mpf - tr_at_q0_mpf)`, prints it, and stores it as
`abs_diff_vs_bridge`. Nothing compares it to anything; nothing fails. So even had
it run, the 8.14e-5 would have been recorded as a field and read as a pass.

The paper's *"three independent production paths agree to machine epsilon"* is
therefore backed by a witness that ran **two**, and the third — the one that
disagrees — is disabled and unasserted.

### Two corrections to my own draft of this bean

1. **I was going to report a float64 defect. There is none.** I claimed the
   fallthrough `sp.nsimplify(d_f)` was float64-seeded. `d_f` is an `mpf` at 50 dps
   and `nsimplify` retains ~49 digits. Wrong, and caught only by running it.
2. **I predicted `atom_nf_symbolic_D`'s NF would lose its `q` dependence** via
   that fallthrough. It does not — measured, the deuteron NF has 32 terms and
   every coefficient still carries `q`. It never reaches the fallthrough at all,
   because its 1e-3 tolerance catches the crossing first. The defect is real but
   it is the opposite one: not contamination, *erasure*.

### Still open

The **8.71e-08** between the two colour-blind paths, and the **7.8e-08** between
the two witnesses on the free proton and neutron, are a second and separate
discrepancy. Free nucleons carry no p-n bond, so the weighting cannot explain
them. Unexplained, and roughly 1e7 above the L1 target on its own.

## FIXED 2026-08-21 — two root causes, both closed; the paper's claim is now true

The disagreement had **two** independent causes, one behind the other. Both are
fixed; the symbolic path now agrees with the bridge to machine epsilon, which is
what `recomputed-low-isotope-mass-table.md` claimed all along. The claim needed a
correct implementation, not a weakened wording.

    deuteron |symbolic - bridge|
      before                 8.145e-05
      after tolerance fix    7.915e-08     <- cause 1 closed, cause 2 exposed
      after delta fix        3.440e-25     <- both closed
    free nucleons after both fixes:  p 5.0e-49,  n 7.9e-49

### Cause 1 — the tolerance straddle (`atom_nf_symbolic_D.py`)

`_D_HECKE_TOL` was `1e-3`; the weighted crossing sits `7.190163e-05` from the
blind `-h/2`, so the window swallowed it. Its justifying comment claimed the
looseness absorbed "rounding of the q_0 rational" — measured, **that rounding is
exactly 0.0**: h from `_Q0_RATIONAL` and h at the 50-dps q_0 agree to the bit,
and every intra crossing lands at distance 0.0 from its target. The window bought
nothing and cost the weighting.

Fixed at `1e-9` (~7 orders of margin either side), plus an explicit branch that
matches the weighted crossing **structurally** against
`canonical_braid_crossings.d_for_ctype`, and maps it to a symbolic
`-h(1/2 - δ(q)/4)` so the NF stays a function of q. This follows the rule
`tr_m_algebraic_q.build_atom_symbolic_q` already states and this file broke: the
colour δ *"is numerically indistinguishable from -h/2, so it must be placed
structurally, not matched"*.

### Cause 2 — two definitions of δ, differing by exactly ℏ³

Closing cause 1 left 7.92e-08. Root:

    tr_m_algebraic_q.flavor_split_leading_sym(q)   = leading * (1 + hbar**3)
    _li_2_q_util.flavor_split_leading(q)           = leading
    canonical_braid_crossings._avg_color_delta()   = leading

    relative gap = 9.7270e-04 = hbar^3 exactly

and `flavor_split_leading_sym`'s docstring **claimed it matched
`_li_2_q_util.flavor_split_leading` "at any q"**. Per AGENTS.md the leading term
is proven and `(1 + ℏ³)` is the *posited* subleading correction, carried
separately as `flavor_split_subleading` — so every consumer was silently getting
the posited quantity under the proven one's name. Fixed at source: the function
now returns the leading term alone.

This was **not** confined to my call site. `tr_m_algebraic_q.build_atom_symbolic_q`
— the module's own headline export — sat 7.92e-08 from the bridge for the same
reason, and now does not.

### Why nothing caught either: three failure modes, all in one witness

`computations/tr-m-algebraic-q.witness.json`, on main since 2026-08-09:

1. **`allPassed: false`, committed and unread.** Its
   `symbolic_delta_matches_li2q` assertion recorded `computed=1.338e-06`
   against `tol=1e-12`, `passed=false` — naming cause 2 exactly, twelve days
   before I rediscovered it by hand. Spun out as **`qou-ad4t`**: 108 of 2681
   witnesses on main carry `allPassed: false`.
2. **A tolerance sized to fit the bug.** The sibling assertion
   `algebraic_q0_matches_transfer` **passed** at `6.88e-08` against `tol=1e-07`,
   with a `source` string explaining the residual as a *"~1e-8 float64-eval
   floor"*. It was cause 2, not a floor. Post-fix the value is 3.50e-15, so the
   claimed floor sat ~17 orders above the real one. Tolerance tightened to 1e-9
   and the rationalising text replaced with what actually happened.
3. **A cross-check that could not fail.** `atomic_tr_m_mpfr_50dps.py` computed
   `abs_diff_vs_bridge`, printed it, stored it as a field, and compared it to
   nothing — and sat behind `if also_symbolic:`, never enabled (the committed
   witness has no `abs_diff_vs_bridge` for any of the five atoms). Had it run
   pre-fix it would have recorded 8.14e-05 and still passed. Now carries
   `tolerance` + `passed` and prints a MISMATCH line.

### Verification

`tr_m_algebraic_q.py` re-run: both assertions pass (`3.4972e-15` vs 1e-9;
`6.5052e-19` vs 1e-12), `allPassed: true`. Environment matched to main's record
rather than downgraded — the container had mpmath 1.3.0 against the witness's
1.4.1; installed 1.4.1 (sympy 1.14 declares `mpmath<1.4`, but it imports and the
numbers are byte-identical under both, checked before trusting either) and
regenerated so provenance reads 1.4.1.

`precision-gates.sh --changed`: all blocking gates green. Vendor sync in sync
(42 modules). qou-mass 20 passed, qou-substrate 65 passed.

Pre-existing and NOT introduced here: the 19 raw-float64 fields in
`tr-m-algebraic-q.witness.json`. Main's copy has exactly 19 too. Worth a separate
fix at the producer; not folded into this one.

### Still open in this bean

Nothing from cause 1 or 2. The remaining item is the one this bean opened with
and the fixes did not touch: **`canonical_mass_table_extended.py` still emits the
colour-blind deuteron** (0.575090958682446712), and neither of its two witnesses
records a `pn_convention`. That producer computes via `Σ y_λ·χ^λ`, not through
either path fixed here. It belongs to `qou-cds4` / ruling R3, and picking its
frame is that tranche's call.

## Implementation & Witness Progress (PR #8253)
- Branch: `qou-10v9-4e5k-742w-9bei-cblw-fv0s` (`52305a7a1e7f9836f16e0d5d8d454bd72705f9b1`), PR: `litlfred/qou#8253`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/deuteron_trace_discrepancy_m1_rho_constant_sdp_zero_threshold_pn_colour_factor_and_sign_wire_loss_probe.py` -> `computations/probes/deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss.witness.json` (`allPassed: true`, `scriptHash: ece5f27ee4a5`, `scriptCommitSha: 1c76aa0739f7803dab0155515577d8888a08fc68`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8253, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
