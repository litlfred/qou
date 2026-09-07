---
# qou-vilx
title: 'qou-x631: the Kerov-expansion question is orthogonal to the conjecture (one coefficient); FSD and ICV both die at k=18 and k=26'
status: completed
type: task
priority: normal
created_at: 2026-09-07T11:16:19Z
updated_at: 2026-09-07T11:43:09Z
---

Probe: `computations/qbeta/qbeta_covariance_kernel_kerov_mode_probe.py`, 10 assertions.

## First: my own #7051 claim was under-evidenced

I recorded that expanding `ln f` in the Kerov modes *"will not terminate"*, on the
evidence that the **single-cycle** modes' share of `Var_P(ln f)` falls 20.8% -> 12.4%.
That does not follow: `{Sigma_p}` generate the shifted-symmetric algebra
**multiplicatively**, so a small linear span of single cycles says nothing about
low-**degree** polynomials in them. Expanding in the full class basis, by
d = number of nontrivial cycles (Parseval exact, 1.000000000, at every k):

| k | d=1 | **d=2** | d=3 | d<=2 |
|---|---|---|---|---|
| 8 | 24.4% | **66.1%** | 1.9% | 90.5% |
| 12 | 20.8% | **56.4%** | 12.9% | 77.2% |
| 16 | 19.4% | **50.0%** | 13.3% | 69.4% |

**The mass is at d=2, which I never looked at.** The conclusion survives — d<=2
falls 90.5% -> 69.4%, no fixed degree holds — but on evidence I had not taken.

## And then the conclusion is beside the point

`|C_{(3,1^{k-3})}| = (k)_3/3`, so `Sigma_3 = (k)_3/sqrt(|C_3|) * e_3` is **one**
orthonormal basis vector. Hence `Cov_P(ln f, Sigma_3)` is a single Fourier
coefficient, and every d>=2 mode — the 50–66% of the mass — is **orthogonal to it
and contributes nothing**. Whether the expansion terminates has no bearing on the
conjecture. *"Can ln f be expanded in Kerov modes?"* was the wrong question.

## The cleanest form of the conjecture found so far

    G(s) := SUM_lam (f^lam)^{1+s} chi^lam(3-cyc)

`G(0) = 0` **exactly** (column orthogonality) and `G(1) = T_3(k)` is the conjecture.
No partition function, no tilted measure, no covariance — every earlier
formulation (`E_Q`, `Cov_beta`) carries a normaliser Z that this one does not.
The tempering family of `qou-f4ye` is `s = beta - 2`.

Splitting by the sign of the character, with `W := SUM_{chi>0} f|chi| =
SUM_{chi<0} f|chi|` (exact integer equality — that IS `G(0)=0`) and
`nu_pm(lam) ∝ f^lam |chi^lam(3)|`:

    G(s) = W * ( E_{nu+}[f^s] - E_{nu-}[f^s] )

so the conjecture reads: **partitions whose 3-cycle character is negative carry
the larger dimensions.**

## Two routes tested and ELIMINATED

1. **First-order stochastic dominance** of `nu-` over `nu+` in `f^lam` — would give
   `G(s) <= 0` for all `s >= 0`.
2. **Increasing-concave (second-order) dominance** — strictly weaker, and exactly
   matched to the exponents that matter, since `x^s` is increasing concave on
   `s in (0,1)`. The FSD failure did not settle it a priori.

Exact on Fractions over `10 <= k <= 32`: at every k the survival functions do not
cross at all (sign pattern `[-1]`, `nu+` uniformly below) **except k = 18 and
k = 26**, where **both** fail, by 0.0161 and 0.0011. Not a near-miss to patch: false
at recurring k with a shrinking gap. The conjecture itself still holds at both
(checked exactly), so the orders are strictly stronger than needed and strictly
false. Recorded because they hold at 21 of 23 values and look compelling.



### Follow-up `qou-dnev`: the eliminated orders were the wrong KIND of tool

FSD and ICV fail here by 0.0161 and 0.0011. Measured in `qou-dnev`: the quantity
actually wanted, `A/B`, sits at ~0.59 against a threshold of 1 — **~40% slack,
uniformly over 6 <= k <= 34** — and the cancellation ratio `R ≈ 4` is flat in k.
So both were tight pointwise conditions on whole distributions applied to a slack
aggregate inequality, which is why a vanishing local defect killed them while the
conjecture stood. A lossy bound suffices; exact matching is not needed.
