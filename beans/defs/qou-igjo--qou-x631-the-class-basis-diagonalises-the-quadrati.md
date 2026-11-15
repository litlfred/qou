---
# qou-igjo
title: 'qou-x631: the class basis diagonalises the quadratic twist — the conjecture is one Fourier coefficient of f^lam'
status: completed
type: task
priority: normal
created_at: 2026-09-07T08:40:49Z
updated_at: 2026-09-07T09:35:26Z
---

Branch `claude/q407-self-assuming-projections-2026-08-21`.
Probe: `computations/qbeta/qbeta_covariance_kernel_class_basis_probe.py` (18 assertions, all pass).

## The answer to "is there a quadratic twist?" — yes, and it is *diagonal*

For \mu |- k with class size |C_mu|, set `e_mu(lam) := sqrt(|C_mu|) chi^lam(mu)/f^lam`.
Column orthogonality says exactly that **{e_mu} is an orthonormal basis of
L^2(Plancherel_k)** — and the count is right on the nose, #classes = p(k) = dim,
so it is a basis, not just an orthonormal system. `e_{1^k} = 1`, so every other
mode has mean zero.

The omega involution lam |-> lam' acts on it **one sign at a time**:

    e_mu(lam') = sgn(mu) e_mu(lam).

The quadratic twist is not an extra symmetry beside the Frobenius pairing — it is
**diagonalised by the pairing's own basis**, eigenvalue sgn(mu). Verified exactly
(integers) for 3 <= k <= 9.

## What that collapses

- `Sigma_p` is the single mode `mu = (p,1^{k-p})` rescaled, `|C_mu| = (k)_p/p`, so
  `Var_P(Sigma_p) = p(k)_p` and `E_P[Sigma_p Sigma_q] = 0` are **one line of
  Parseval** — `qou-ml0m` derived both directly; they are corollaries.
- Expanding the omega-even observable f^lam: `a_mu = sqrt(|C_mu|) S_mu/k!` with
  `S_mu = SUM_lam (f^lam)^2 chi^lam(mu)`. **The conjecture T_3(k) <= 0 is the
  statement that ONE named Fourier coefficient of f^lam is non-positive**, and
  the 3-cycle mode is a top-4 mode by mass for every 3 <= k <= 14 — a leading
  term, not a tail.

Four exact identities, all verified to k = 14:
(A) `S_mu = 0` on every odd class [twist]; (B) `S_{1^k} = M(k) = SUM (f^lam)^3`;
(C) `SUM_mu |C_mu| S_mu = k!`; (D) Parseval `SUM_mu |C_mu| S_mu^2 = k! SUM (f^lam)^4`.

## A route closed

(B)+(C) give `SUM_{mu != 1^k} |C_mu| S_mu = k! − M(k) < 0`, which invites the
guess `S_mu <= 0` for all mu != 1^k — a strengthening that would contain the
conjecture. **FALSE**: `S_{(4,2,1^{k-6})} > 0` for every 7 <= k <= 14, and it is
the largest positive coefficient in each. The conjecture needs the 3-cycle class
specifically; no blanket sign is available.

## Two self-corrections

1. **`c_p = -1/(p+1)` is NOT falsified — I called it too early.** Reading the
   table at k <= 28 I recorded it as refuted because c_5 sat near -0.075 and c_7
   was *positive*. Extending to k = 52: c_7 turns negative by k = 48, and c_5
   climbs monotonically to 62% of -1/6 with residual ~k^{-0.64} (95% would need
   k ~ 10^3). Verdict: **untestable for p >= 5 in reachable k, and consistent
   with every datum**. The earlier call was an artifact of the k-range.
2. **g'(0) is not monotone and it crosses -1/4** — a correction to merged
   `qou-f4ye`, landed there and in the tempering probe. See that bean.

Also exact: `c_p = 0` for **even p**, decided on integers (0 violations, k=4..12).
Not subsumed by orthogonality, which needs both arguments to be characters — and
log f is not one.


**Landed** `565e51c07b` on `claude/q407-self-assuming-projections-2026-08-21`.
18 assertions, all pass. Precision gates: baseline (HEAD~1) RED on 12 gates; this
commit RED on the same 12 **minus `raw-float64 ratchet`**, which this change turns
green by draining both witnesses (98 -> 0 new, 25 -> 0 tempering). Verified by
running `scripts/precision-gates.sh` in a detached worktree at the parent commit,
so 'pre-existing' is measured rather than assumed.
