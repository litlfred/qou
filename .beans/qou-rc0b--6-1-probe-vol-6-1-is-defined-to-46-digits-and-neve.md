---
# qou-rc0b
title: '6_1 probe: VOL_6_1 is defined to 46 digits and never read — the strongest available anchor is unused'
status: todo
type: task
priority: normal
created_at: 2026-08-21T20:52:43Z
updated_at: 2026-08-21T20:53:18Z
---

Found while fixing a LOSSY module-const in that file during prepare-merge on
PR #5382 (bean qou-irzg). The dps fix is on #5382; **this finding is not, and
belongs to the qou-6ort arc that owns the probe.**

## The observation

`computations/qbeta/qbeta_ohtsuki_sixone_kappa_series.py:166` defines

    VOL_6_1 = mp.mpf("3.163963228883143983991757529167384812325703962")

and **nothing reads it** — not in that file, not anywhere in the tree. Every
other constant in the same block is read: `KI6C_SIGMA_BAR`/`KI6C_OMEGA_BAR` at
eight sites, `SIGMA_52`/`OMEGA_52` at four.

## Why it matters — it is the strongest anchor the probe has

Theorem 1.1 writes `⟨K⟩_N = e^{Nς} N^{3/2} ω (1 + Σκᵢℏⁱ)`, so `Re(ς)` is the
exponential growth rate, and the volume conjecture makes that `Vol(K)/2π`. The
probe's own docstring says exactly this. Measured against the committed witness:

    Re(sigma_fit)   = 0.503560387637746199120114   (.data.gate_6_1.sigma_fit)
    Vol(6_1)/(2*pi) = 0.5035603876377461977116192  (from the UNUSED constant)
    ki6c printed    = 0.5035603                    (.data.gate_6_1.sigma_ki6c)

    |fit − Vol/2π|  = 1.4e-18   <- the anchor sitting unread
    |fit − printed| = 8.8e-8    <- the anchor honesty-control #1 actually checks

**Ten orders of magnitude, and it is the more independent of the two.** The
printed ς comes from the same paper the transcription came from, so agreeing
with it tests the transcription against its own source. Vol(6₁) comes from
hyperbolic geometry — a different object entirely — so it tests the result
against something the paper could not have contaminated.

## What is actually wrong

The comparison is **performed in prose and not in code**. The docstring says
"Theorem 1.1 + the volume conjecture require `Vol(6₁)/2π = 0.50356`" — a
hand-divided 5-digit value written inline, three lines below a 46-digit
constant that could produce it. So the headline number and the constant can
drift apart independently, and no assertion in the witness compares the fitted
rate to the volume at all (the six are: two determinants, two 5₂ validations,
two 6₁ gates).

## Suggested fix (for the owning arc)

Add a seventh assertion comparing `Re(sigma_fit)` to `VOL_6_1/(2*mp.pi)`, and
derive the docstring's 0.50356 from the constant rather than restating it. That
turns honesty-control #1 from a 6-digit self-consistency check into an
18-digit independent one, at the cost of about three lines.

## Two loose threads noticed in passing, NOT chased

1. `computations/lambda_scale_rd4_k_p_search.py:57` carries its own
   `VOL_6_1 = mp.mpf("3.16396322648")`. That disagrees with the 46-digit value
   at the **10th digit** (…22648 vs …22888). One of the two is wrong; the
   46-digit one matches `sigma_fit` to 1.4e-18, so the short one is the
   suspect. Not verified further.
2. The docstring's `## OUTCOME 2026-08-19: the gate FAILED` section says
   "No κ is reported" and cites a converged rate of ≈0.5715 (13.5 % off),
   but the committed witness shows all six assertions **passing** and
   `sigma_fit` landing on the volume. The later `SECOND PASS` section appears
   to have resolved it. Worth checking whether the OUTCOME section is now
   stale prose describing a superseded state.

## Note on the dps fix in #5382

The truncation I repaired there (46 digits built at the default dps 15, a
4.16e-17 relative loss) **changed no published number**, precisely because this
constant is unread. That was verified before the fix, not assumed.
