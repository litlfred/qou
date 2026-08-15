---
# qou-kc21im
title: 'GAP: is KC21''s "structural parity is convention-immune" VERIFIED or asserted? c_3(q) is DEFINED BY the C-frame extractor'
status: todo
type: task
priority: high
created_at: 2026-08-15T15:05:00Z
updated_at: 2026-08-15T15:05:00Z
---

## The question

PR #5107 (merged 2026-08-15) audited the c_3 refutation chain against the
C→D trace-convention change and correctly split the findings:

- **value layer → C-conditional** (c_3 ≈ −2.07 under C, ≈ −974 under D;
  (H1), `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S`, the D-ladder constants, and
  even the "canonical" c_2 = −1 are all C-frame statements);
- **structural layer → claimed convention-IMMUNE.** The registry note added
  to KC21 (§9g) says: *"the structural parity statement (`S(−ε) = −S(ε)`)
  and the `1/u³` result are convention-immune"*.

**This bean asks whether that second claim was verified or asserted.**

## Why it is not obvious

The bar-parity argument is a statement about the **function** `c_3(q)` (and
its odd part `S`): with `q = q₀ + iε`, `S(−ε) = −S(ε)`. But `c_3(q)` is not a
convention-free object — it is *defined by* the extractor, whose N=1 rung
consumes the convention-C Markov parameter (`α = (z−1)h/2`,
`qbeta_utils.py:124-125`). Under D the extractor returns a numerically and
structurally different function (c_3 ≈ −974; rung convergence 58× → 1.12×).
The parity of function `f_C` does not transfer to function `f_D` merely
because both are called "c_3".

Compare the neighbouring, *checked* immunity claims from the same audit —
the anchor-swing mechanism and the entropy bound were shown immune **because
their inputs (`u`, `Q_A`, σ) are z-free**. The parity claim has no analogous
z-free-input demonstration on record; `S = h·D(ũ)` runs through the ladder
that #5107 itself marks C-conditional in the same registry sentence.

## What would settle it

1. **Re-derive the parity under D.** Extract `c_3^D(q)` with the D parameter
   and test `S^D(−ε) = −S^D(ε)` symbolically (sympy exact / mpmath 60 dps,
   proton pin) — the same shape of test #5107 ran for the swing ratio.
2. **Or exhibit the z-free reduction.** If the parity follows from
   `fig8Trace_im_odd` + `fig8Trace_im_real_zero` (both proved-lean) with no
   z-bearing input in between, write that dependency chain out explicitly;
   that *is* the immunity proof and the claim stands as stated.
3. Update KC21's §9g note to the tiered outcome (`verified-immune` /
   `C-conditional`) in the `.md` **and** the JSON twin; run
   `kernel_constraints_registry_validate.py` (R6 now guards twin drift).

## Interaction with the new `disputed` registration

Bean `qou-b3nk` (PR #5111) proves the decay ladder's `z_C` fails the
**full-bar condition** `bar(z) = z − h` away from `q² = 1` (`z_C` is
bar-EVEN; `z_D` satisfies it). So the C-frame trace does **not** commute with
the full bar involution. That does not by itself invalidate fibre-variable
parity bookkeeping (`ZBarParity`'s z-alone exclusion is pure algebra in `q`
and survives), **but it removes the obvious reason to expect trace-derived
quantities to carry clean bar parity** — which is precisely what `S`'s
odd-part claim asserts. The two questions should be answered together.

## Discipline

Not a refutation — scope-(a) at most until tested. Per §"Defined residual ≠
derived decomposition": `S` is a residual of a C-frame extraction, so its
parity is a property of that extraction until shown otherwise. Do not flip
any registry tier on assertion in either direction; the honest interim label
is "immunity claimed, not yet audited".

Raised by the session that ran the #5107 redirect, on reading the audit's own
logic back against the sentence it added to KC21.
