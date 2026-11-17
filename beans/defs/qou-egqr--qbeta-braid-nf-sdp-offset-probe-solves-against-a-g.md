---
# qou-egqr
title: qbeta_braid_nf_sdp_offset_probe solves against a Gram that is singular under convention D
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:29:16Z
updated_at: 2026-10-12T17:40:00Z
parent: qou-cdx1
---

Parent: qou-cdx1. Split out of qou-cds2, which migrated pyhecke's mpmath path to
convention D and exposed this as the one real downstream consequence.

## The measurement

`computations/probes/qbeta_braid_nf_sdp_offset_probe.py` asserts
`G1_solve_consistent`: that `G x* = nf` holds to `1e-40`, solving against the
50-dps Gram from `gram.gram_matrix_mp()`.

Under convention C, G was invertible on the full NF basis and the probe met that
bound. Under D the Markov-Gram form on that basis is **singular** — corank 1 —
and the residuals become:

    muon (4_1)     2.127e-10
    proton (B_3)   1.313e-10

The solve did not fail. It **lost thirty orders of magnitude of precision**,
which is the fingerprint of the null direction, and the 1e-40 gate correctly
catches it. The probe exits 1 and says so.

## The repair is named, and it is the one the float64 side already took

Quotient by the radical — `QOU/QBeta/GramSignature.lean`. The float64 path did
exactly this in `6086572c4`: `G_INV` was deleted rather than renamed, and the
inverse is now taken on `H_3/rad`.

## Why it was NOT done in qou-cds2

Moving the probe from solving on the full NF basis to solving on `H_3/rad`
changes what it measures: `x*` is unique only modulo the radical, so the
"offset from the symmetric point" the probe reports becomes an offset in the
quotient. That is a decision about what the probe means, not a library
migration, and folding it into one would have hidden a science change inside a
convention change.

## State

Its witness is committed WITH the failure recorded. That is deliberate: a
witness claiming 1e-40 consistency the code no longer produces would be the
stale-artifact defect (detector-blindness taxonomy row 10). The red is honest
and should stay until the quotient repair lands.

Note the probe's own docstring already anticipated the precision it was relying
on: "the float64 version of this gate could only ask for 1e-6". At 1e-6 this
failure would have been invisible.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

`qbeta_braid_nf_sdp_offset_probe` solves against a Gram that is singular under
D. The registry records this as the one real downstream consequence of
migrating pyhecke's mpmath path. Live; the probe's own guard refuses rather
than publishing laundered numbers, which is correct behaviour and not a fix.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-12 re-measured against `main` `021543d83c8` — the named repair is REFUTED, and my own 2026-10-10 triage missed it

**My `LIVE` verdict above is half right and its reasoning is stale.** It is
right that the guard is "correct behaviour and not a fix". It is wrong about
what the fix would be, and so wrong about what this bean is waiting for.

### 1. The probe no longer loses precision — it refuses, universally

This bean records the probe exiting **1** with residuals `muon 2.127e-10` /
`proton 1.313e-10`, i.e. a 1e-40 gate catching a 30-order precision loss.
Measured live, it exits **2** before computing anything, and the refusal
carries a far stronger statement than the residuals do:

    ⟨radical, nf(β)⟩ = (−1/q)^writhe(β)   exactly

— the pairing is β's **sign-representation value**. A `zpow` of a nonzero base
never vanishes, so **no braid's normal form is orthogonal to the radical**, so
`G x = nf` is unsatisfiable for *every* braid at *every* `q ≠ 0`. Not
ill-conditioned: unsatisfiable. That is
`QOU.QBeta.signRepValue_ne_zero` in
[`RadicalPairingIsSignRep.lean`](../../folio/quantum-observable-universe/lean/QOU/QBeta/RadicalPairingIsSignRep.lean),
**sorry-free, generic `Field` per §7c** (the file's one `sorry` is the word
inside a docstring saying it is sorry-free). It is a scope-(b) structural
exclusion with its invariant named, which is what AGENTS.md's refutation rule
asks for and what the residuals could never have supplied.

Verified here independently of the thirteen-word probe the Lean cites, directly
at the two production anchors at 70 dps: `⟨rad, nf⟩ = 1` **exactly** for both,
and both are powers of `σ₁σ₂⁻¹` so both have writhe 0, giving `(−1/q)^0 = 1`.
Prediction and measurement agree exactly.

### 2. So "until the quotient repair lands" is a wait that cannot end

§State above says *"the red is honest and should stay until the quotient repair
lands"*, and §Repair defers that repair as *"a decision about what the probe
means"*. The corpus has since decided it, against. The same Lean file's
docstring:

> *"That is the fact that makes re-solving it on the quotient and reporting an
> offset angle a **category error rather than a numerical approximation**."*

Quotienting by the radical does not solve `G x = nf`; it solves
`G x = P_⊥ nf`, a different demand, having discarded a component that is
*never* zero. The offset angle you would then report is an artefact of the
projection. **This bean's named fix was refuted eight weeks before my triage
called the bean live, and the triage did not check the Lean.**

### 3. The committed witness is the frozen pre-guard record — new taxonomy row 58 (filed as 57; renumbered at merge, main took 57)

§State reasons that keeping the red avoids the stale-artifact defect (row 10).
It avoids row 10 and lands in its mirror image. What is on disk is the
**2026-08-16, pre-guard** artifact (`scriptHash d4bdd964d1d8`; the live file
hashes `0a2c46c6818f`), and it reports

    G1_solve_consistent  passed: false
    "G x* = nf to < 1e-40 for both anchors"

— the failure as a **precision-gate miss**. That is the superseded diagnosis,
and it is precisely the one that invites the quotient repair. Worse, it cannot
be corrected: the guard `return 2`s at line ~204 while `WitnessBuilder` is
constructed at ~359, so **no run of the producer can rewrite its own witness**.
`scriptHash` drift is detected correctly and AGENTS.md §4's prescribed remedy
("re-run the producer") is structurally unavailable. Filed as **row 58** of
[`the detector-blindness taxonomy`](../../docs/audits/2026-08-15-detector-blindness-taxonomy.md);
near neighbour is row 39, and it is not the same failure — there the check
calls a stale witness fresh, here the check is right and the fix does not
exist. The witness also carries **no convention stamp**, so the producer's
docstring is the only thing recording that it is C-frame.

### 4. Two docstring defects fixed in the same pass

- **A wrong number with a right "identically".** The docstring claimed *"BOTH
  anchors carry a radical component of ~47 % of their NF norm (0.47268915 for
  each, identically)."* The figure and the "identically" are correct and the
  **denominator is not**: `0.47268915119281285398` is exactly `1/‖rad‖`
  (`‖rad‖ = 2.1155552173696784523`) — the projection length onto the unit
  radical direction, identical across anchors *because* `⟨rad, nf⟩ = 1`
  exactly. The radical's share **of the NF norm** is `1/(‖rad‖·‖nf‖ )` and
  **differs**: muon `0.461823239529892831`, proton `0.472606756658436762`
  (`‖nf‖` = `1.02352829120072182` / `1.00017434057642058`). Written the old
  way it reads as a numerical coincidence between two knots; it is a
  consequence of the theorem the same paragraph goes on to cite.
- **A splice artefact.** The clause *"Homogeneity is therefore broken and the
  offset direction becomes"* had been cut from its sentence (`…not merely its
  scale.`) by the 2026-08-19 ⛔ insertion and left dangling 23 lines below at
  the end of an unrelated paragraph, where it survived four commits. Restored.

### 5. What this bean is now waiting for — and it is NOT the quotient

Still open, and genuinely so, which is why this stays `todo`:

**Re-derive the question under D.** The probe's premise ("`G` invertible, so
`x* = G⁻¹ nf` is unique and its direction is knot-dependent") is dead. Giving
this probe a falsifiable D-frame question means finding a demand that is
*satisfiable* on the rank-5 image — not projecting the unsatisfiable one. That
is new mathematics, not a migration, and it is coupled to `qou-v7qj` (whether
the radical quotient is the right repair for the D operator-selection LP; the
answer here is evidence that it is **not**, for this demand at least).

**Exit criterion, replacing §State's.** This bean closes when a D-frame demand
is derived and its probe runs, or when the owner rules the question retired. It
does **not** close on the quotient landing, and the committed red should stay —
but read with §3 in hand, because the red names the wrong failure.

## Progress Update (Round 65 — PR #8267)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8267`](https://github.com/litlfred/qou/pull/8267) (branch `feat/round65-radical-branching-bond-habiro-cusp-43c1`, Commit 1 `20143712c434683951cbe6f568953fd4a98454bc`, Commit 2 / Head `1ee46ede72413597113d706dd733554a25e327d5`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/QBeta/RadicalPairingIsSignRep.lean (`signRepValue_inv_mul_and_mul_inv`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/radical_branching_bond_habiro_cusp_probe.py` (`scriptHash: 949a90321cd5`) + `test/results/witnesses/radical-branching-bond-habiro-cusp.witness.json` (`allPassed: true`).
