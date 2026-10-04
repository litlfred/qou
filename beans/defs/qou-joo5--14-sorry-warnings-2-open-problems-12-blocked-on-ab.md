---
# qou-joo5
title: '14 sorry warnings: 2 open problems, 12 blocked on absent Mathlib theory'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T06:55:56Z
updated_at: 2026-10-04T15:11:42Z
---

Audit of the 14 `declaration uses 'sorry'` warnings left after qou-k21h
got `lake build` green. **None is a proof gap that can be closed by
editing the file.** Each was checked against the pinned Mathlib rather
than taken on trust.

## Mathlib coverage — checked, not assumed

Grepped `.lake/packages/mathlib` at the pinned rev f897ebcf:

    hook_length / hookLength          0 files
    RSK / RobinsonSchensted           0 files
    Hadamard                          0 files
    weierstrassFactor                 0 files
    numStandardYoungTableaux          0 files
    Specht modules                    absent

So every one of these needs theory built first, not a tactic found.

## 1. Genuinely open mathematics (2) — cannot be proved by anyone

- `HyperbolicVolumeIndependence` — algebraic independence over ℚ of
  Vol(4₁), Vol(5₂), Vol(𝓑₃). The file states this outright: "the `sorry`
  represents the **open conjecture** per §3b … not a missing proof."
  Borel–Zagier circle. **Not actionable.**
- `elliptic_divisor_degree_zero` — needs the argument principle, which
  the file already identifies as "absent from Mathlib v4.24.0 (no
  elliptic-function theory, no residue theorem)". The
  boundary-cancellation half IS formalized; the analytic half is the gap.

## 2. Classical theorems, each a substantial formalization (12)

Every one carries a `-- Ref:` to a textbook result and is tracked in
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`
(P1–P5). Not oversights — deliberate, documented deferrals.

**Symmetric-group / tableau combinatorics (8)**
- `numSYT_mul_hookProduct` — Frame–Robinson–Thrall **hook-length
  formula**. Called "the genuine formalisation target of this brick".
- `sum_dimSYT_eq_involution` — RSK for involutions (Sagan §3.1).
- `branching_two_one` — branching rule (Sagan Thm 3.10.2).
- `skew_le_straight` — skew tableaux / Jacobi–Trudi (Sagan §4).
- `specht_finrank_eq_numSYT` — standard basis theorem (Sagan Thm 2.5.2).
- `specht_isSimple` — Specht simplicity in char 0.
- `spechtIso_imp_dom_both`, `specht_exhausts_irreducibles` — the
  classification.

RSK and the hook-length formula are each multi-week formalizations on
their own, and Specht module theory does not exist in Mathlib to build on.

**Complex analysis (3)**
- `norm_one_sub_weierstrassFactor_le` — the Weierstrass estimate
  `‖1 − Eₚ(z)‖ ≤ ‖z‖^{p+1}`. File: "Not elementary; deferred."
- `multipliable_canonicalProduct` — canonical product convergence.
- `hadamard_factorization` — **Hadamard's factorization theorem**.

**q-difference (1)**
- `cauchyMul_order` — the `≥` direction additionally needs a
  non-cancellation hypothesis on leading coefficients, which the file
  notes may genuinely fail in a general normed field. So the statement
  itself may need strengthening before it is provable.

## What must NOT be done

The tempting "fixes" all make things worse than an honest `sorry`:
weakening a statement until it is provable, adding an axiom, or
discharging with `native_decide`. Each converts a visible gap into
invisible false confidence. A `sorry` at least warns.

## Recommended shape of the real work

One bean per brick, sized honestly, in dependency order — the tableau
work is the load-bearing part and unblocks the most:

1. `numStandardYoungTableaux` + hook-length formula (P2)
2. RSK correspondence → involutions, branching, skew (P1/P3)
3. Specht standard basis → simplicity → classification (P4)
4. Weierstrass/Hadamard chain (independent of 1–3)

Several are plausible Mathlib contributions in their own right.

## Re-audit 2026-08-08 — the set changed; 17 now, not 14

This bean's original list is stale. `main` moved ~23.5k commits, and the
sorry set turned over: two closed (`numSYT_mul_hookProduct` via sp09,
`StandardYoungTableau` is now sorry-free), and several appeared that did
not exist when this was written.

**Current, from source (`grep -n '^\s*sorry\s*$'`):**

| classification | site |
|---|---|
| OPEN CONJECTURE | `HyperbolicVolumeIndependence:42` — algebraic independence of the three hyperbolic volumes |
| OPEN CONJECTURE | `YoungDiagramKernel:310` — `covariance_kernel_conjecture`, Biane–Śniady / Kerov-CLT; "verified k ≤ 30 computationally. Not proved." |
| declared OPEN input | `cat_descended_is_base_mass:79` — `descended_trace_is_base_trace` |
| declared OPEN input | `cat_descended_is_base_mass:89` — `base_mass_is_norm_of_base_trace` |
| deferred analytic | `QGevreyOrder:269` — `cauchyMul_order` |
| deferred analytic | `HadamardFactorization:293` — `hadamard_factorization` |
| blocked on Mathlib | `EllipticDivisorDegree:241` — needs the argument principle |
| RSK program | `YoungTableauStandard:121/129/136` — branching, skew, involutions |
| Specht program | `Specht:313/328`, `SpechtClassification:454/494`, `SpechtIrreducible:1076`, `JucysMurphy:850`, `SnWedderburnPartitionBridge:250` |

**Two of the three sorries this bean listed for HadamardFactorization are
gone** — only `hadamard_factorization` itself remains, so the Weierstrass
estimate and canonical-product convergence were closed on main. Worth
noting against `qou-v4if`, which recorded the PI-2 brick as "NOT tractable
in Mathlib v4.24.0 within reason".

**Nothing here changes the conclusion.** Every remaining site is a declared
open input, an explicit conjecture, or a cited classical theorem with no
Mathlib foundation. None is a proof gap an edit closes.

### The one entry point worth naming

`specht_form_nondegenerate` (`SpechtIrreducible:1076`) is **sp01** — the
foundation of `sp00`'s PHASE A, and the thing `specht_isSimple` waits on.
It has its own bean, `qou-0xyc`. If effort goes anywhere in the Specht
cluster, it goes there first; the other five Specht sorries are downstream
of it.

### Method note

This audit reads `^\s*sorry\s*$` from source rather than build warnings.
The earlier count came from a build log and undercounted, because a module
that fails to compile never reports its own `sorry`s — so the corpus-wide
figure was only trustworthy once the package built.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] superseded measurement: 15 real sorry terms on main in 6 files (3 content-sibling, 1 Fred2005, 2 scratch/computations) | STALLED: in-progress, last update 2026-08-08
