# The hook column of the gauge-invariant curvature has a reduced-Burau closed form, all orders (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** "merge and go" — continue the qou-o6ov frontier after #6445.
**Scope:** scope-(a); one exact positive (a derived closed form, verified to the dps floor); no MeV, no fit, nothing wired.
**Probe:** [`magnus_gauge_hook_closed_form_probe.py`](../../computations/deltalambda/magnus_gauge_hook_closed_form_probe.py)
**Follows:** #6445 (the projector curvature `Ω₂^P` is a genuine Hecke element, gauge-invariant) and #6430 (hooks = q-exterior powers of the reduced Burau, with the exact word-length twist).

## Why this is now reachable

#6430 reduced the **plain hook character** to the `(n−1)`-dim reduced Burau `ρ^V`:
`tr_{(k,1^{n-k})}(ρ) = q^{L(1−j)}·e_j(eig ρ^V)`, `j = n−k`, `L = |ρ|`. It could **not** be extended to
the germ `Ω₂`, because the germ is a rep-specific log-derivative and the exterior-power functor is
germ-naturality-limited (#6432, #6434). #6445 replaced the germ by the projector curvature
`Ω₂^P = (4/[2]_q²)·Σ_a[σ_a,σ_{a+1}]`, a **genuine algebra element** — so the #6430 handle now
applies to the *curvature*, not just the character.

## The closed form (derived)

On a hook `(k,1^{n-k}) = Λ^j(V)`, `Λ^j` is a tensor functor (`Λ^j(A)Λ^j(B) = Λ^j(AB)`) and
`tr_{Λ^j V}(Λ^j M) = e_j(eig M|_V)`. With `ρ ↦ Λ^j(W)`, `W = ρ^V`, and `Ω₂^P` built from the σ's,
each commutator term `ρσ_aσ_{a+1}` is itself a **word** of length `L+2`, so #6430's exact identity
applies to it term by term:

```
tr_{(k,1^{n-k})}(ρ·Ω₂^P)
  = (4/[2]_q²) · q^{(L+2)(1−j)} · Σ_a [ e_j(eig(W·σ^V_a·σ^V_{a+1})) − e_j(eig(W·σ^V_{a+1}·σ^V_a)) ],   j = n−k
```

The twist `q^{(L+2)(1−j)}` is common to both commutator terms (same length) and factors out of the
sum. The result is a closed form **in the `(n−1)`-dim reduced Burau alone** — no seminormal germ,
no per-irrep block structure, valid for **all orders `n`**.

**The endpoint-zero is manifest in the formula.** `j=0`: `e_0 ≡ 1`, every bracket is `1−1 = 0`
(trivial rep). `j=n−1`: `e_{n-1} = det`, and `det(Wσ_aσ_{a+1}) = det(Wσ_{a+1}σ_a)` since dets
commute, so every bracket vanishes (sign rep). The two exact zeros of the arc drop out of the
algebra with no trace-orthogonality argument.

## Verified (A=2, n=6, exact mpf at 140 dps)

| k | hook | j | direct `tr(ρΩ₂^P)` | closed form (Burau) | error |
|---|---|---|---|---|---|
| 6 | (6) | 0 | 0 | 0 | 0 (abs) |
| 5 | (5,1) | 1 | −40.5793016691 | −40.5793016691 | 2.1e-140 (rel) |
| 4 | (4,1,1) | 2 | −38.7822485845 | −38.7822485845 | 1.2e-139 (rel) |
| 3 | (3,1³) | 3 | −4.1907573068 | −4.1907573068 | 1.9e-139 (rel) |
| 2 | (2,1⁴) | 4 | 1.47629892958 | 1.47629892958 | 2.6e-139 (rel) |
| 1 | (1⁶) | 5 | 0 | 7.7e-141 | 7.7e-141 (abs) |

**Every hook matches to the dps floor** (worst 2.6e-139). This is an exact identity, not an
approximation — the residual is eigenvalue-solver noise at 140 digits.

## The trap I fell into, recorded for the next agent

The first pass **omitted the word-length twist** and matched only at `j=0, 1` and the two
endpoints — while failing the interior by factors of 12–2500. That pattern is diagnostic and worth
knowing: `j=1` has twist `q^0 = 1`, and both endpoints vanish regardless of twist, so *those four
rows can never detect a missing twist*. An agent seeing "endpoints + `j=1` pass, interior fails"
should suspect the `q^{len·(1−j)}` factor before suspecting the reduction. The reduction was right;
the length of the inserted word (`L+2`, not `L`) is what carries the twist.

A second, smaller trap: the sign rep's direct trace is **exactly** `0`, so a relative-error verdict
over a `1e-80` regulariser turns dps-floor noise (`7.7e-141`) into a spurious `7.7e-61` "miss". Score
exactly-zero endpoints by absolute error.

## Consequence for the arc

This is the **second exact reduction** in the arc and the first one that reaches the *curvature*
rather than the character. Combined with #6445:

- The **hook column** of the gauge-invariant row-decay is now an explicit `(n−1)`-dim
  reduced-Burau elementary-symmetric formula, all orders. Its `b`-decay (`b = n−λ_1 = j` for a hook)
  is the decay of `q^{(L+2)(1−j)}·[e_j(…) − e_j(…)]` in `j` — a question about the reduced-Burau
  spectrum of the atom word, which is a far smaller object than the seminormal tower.
- The **two-row column** of `Ω₂^P` is already carried exactly by the 2-dim `U_q(sl₂)` R-matrix
  (#6445's gauge-invariance test *is* that reduction, to 1e-140). So for the gauge-invariant object
  **both** the hook and two-row columns now have small-object handles — the exact situation the germ
  could never reach.
- What remains open for a general-`n` **proof** of the row-decay of `Ω₂^P`: (i) bound the hook
  formula in `j` from the Burau spectrum; (ii) the non-hook, non-two-row shapes.

## Honest limits

- **Verified at `n=6`; the derivation is general in `n`.** The closed form rests on two exact
  facts — `Λ^j` is a tensor functor, and #6430's twisted hook identity holds for every word — both
  general. The numerical check is a consistency test at one `n`, not the proof; a Lean statement of
  the identity is the natural next formalize-first step (it is a one-line consequence of #6430's
  identity applied at length `L+2`).
- **Hooks only.** This is the hook column. It says nothing new about non-hook shapes beyond what
  #6445 already established for two-rows.
- **Nothing wired.** No witness, no consumer, no number changed.

## Bottom line

Because `Ω₂^P` is an algebra element, the #6430 exterior-power handle extends from the plain
character to the **curvature**: the hook column of the gauge-invariant row-decay is
`(4/[2]_q²)·q^{(L+2)(1−j)}·Σ_a[e_j(eig Wσ_aσ_{a+1}) − e_j(eig Wσ_{a+1}σ_a)]` in the `(n−1)`-dim reduced
Burau, verified to the dps floor on every hook at `n=6`, with the endpoint-zeros manifest. The
hook and two-row columns of the gauge-invariant decay both now reduce to small objects — the
first time any column of the *decay* (not the character) has done so.
