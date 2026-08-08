---
# qou-joo5
title: '14 sorry warnings: 2 open problems, 12 blocked on absent Mathlib theory'
status: todo
type: task
priority: normal
created_at: 2026-08-08T06:55:56Z
updated_at: 2026-08-08T06:55:56Z
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
