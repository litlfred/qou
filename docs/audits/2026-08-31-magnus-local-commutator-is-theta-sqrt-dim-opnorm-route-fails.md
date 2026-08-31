# The local commutator is Θ(√dim): the operator-norm route to o(dim) cannot work — the decay is a cancellation (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** research the remaining word-piece and local-commutator norm bounds.
**Scope:** scope-(a) negative for one proof route; no MeV, no fit, nothing wired.
**Probe:** [`magnus_local_commutator_norm_probe.py`](../../computations/deltalambda/magnus_local_commutator_norm_probe.py)
**Refines:** #6339 (which localized the bound to `‖⁅ρ,A_a⁆‖_F = o(√dim)` and proposed the
operator-norm telescoping route).

## The route under test

#6339's Leibniz telescoping (Lean `commutator_mul_left`) gives, with `ρ = ∏σ_{g_i}`:
```
‖⁅ρ,A_a⁆‖_F ≤ Σ_{|g_i−a|≤1} ‖σ_{<i}‖_op · ‖⁅σ_{g_i},A_a⁆‖_F · ‖σ_{>i}‖_op.
```
The proposed route: `‖σ_k‖_op = q` (constant), O(1) crossings near `a`, so
`‖⁅ρ,A_a⁆‖_F ≤ C·max_g‖⁅σ_g,A_a⁆‖_F` with `C` dim-independent — and if the **local**
commutator `‖⁅σ_g,A_a⁆‖_F = o(√dim)`, the whole `o(dim)` follows with no cancellation.
**This probe tests that "if".**

## Two controls (both settled)

- **`σ_k` is symmetric with eigenvalues `{q, −q⁻¹}`** — verified exactly (`‖σ_0−σ_0ᵀ‖=0`,
  `eig(2×2 block) = {q,−1/q}` to err 0). So `‖σ_k‖_op = q` **exactly**, a dim-independent
  constant, and the word-piece operator-norm factors are `≤ q^{L−1}` = constant. **This half
  of the route is sound.**
- **Correction (a control caught my error):** `⁅σ_a, A_a⁆ ≠ 0` — the germ does **not**
  commute with its own generator (measured `‖⁅σ_a,A_a⁆‖_F ≈ 0.95`). Reason: `A_a = q·∂σ_a·σ_a⁻¹`
  is built from `σ_a` *and its derivative*, and the seminormal block `B(q)` does not commute
  with `∂B` (its eigenvectors rotate with `q`). So the near-`a` telescoping terms are
  `g ∈ {a−1, a, a+1}` (three), not two. This does not change the O(1) count.

## The decisive measurement: the local commutator is Θ(√dim)

`max_{a, g∈{a−1,a,a+1}} ‖⁅σ_g,A_a⁆‖_F / √dim`, at the max-dim partition of each `b`
(exact mpf, all partitions — no `ρ`, so cheap):

| b | A=2 (dim) | A=3 (dim) |
|---|---|---|
| 1 | 1.16 (5) | 0.97 (8) |
| 2 | 1.42 (10) | 1.27 (28) |
| 3 | 1.53 (16) | 1.40 (105) |
| 4 | 1.45 (9) | 1.48 (189) |
| 5 | — | 1.50 (216) |
| 6 | — | 1.51 (168) |
| 7 | — | 1.37 (48) |

**It does not decay — it rises and plateaus at ≈1.5.** So `‖⁅σ_g,A_a⁆‖_F = Θ(√dim)` with a
stable constant ≈1.5 (across A=2, A=3; A=4 extends the range to dim≈7700). The local
commutator is **genuinely `√dim`-sized**, *not* `o(√dim)`.

## Consequence: the operator-norm route cannot reach o(dim)

With every factor pinned:
```
|tr(ρ_λ O)| ≤ ‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F ≤ [C·Θ(√dim)]·[Θ(√dim)] = O(dim).
```
The submultiplicative (operator-norm) telescoping **can only give O(dim)** — it cannot see the
measured `o(dim)`. Since the measured decay *is* real (#6331/#6339: raw `|t|` grows ≤15% as
fast as dim), the `o(dim)` is a **cancellation** that the norm bounds discard — at two places:

1. **Word-piece cancellation.** Each telescoping term `σ_{<i}·⁅σ_{g_i},A_a⁆·σ_{>i}` has
   Frobenius norm `Θ(√dim)` (local `Θ(√dim)` times constant op-norms), and there are O(1) of
   them — so the *triangle-inequality* bound on `‖⁅ρ,A_a⁆‖_F` is `Θ(√dim)`. Yet `‖⁅ρ,A_a⁆‖_F/√dim`
   was **measured to decrease with b** (#6339). That decrease is therefore a cancellation
   *among the telescoping terms* — the word-piece dressing rotates the local commutators so
   they partially cancel — not a per-term norm effect.
2. **Trace (Cauchy–Schwarz) slack**, on top of (1), wherever `|t| ≪ ‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F`.

## Honest scope (this is a route-negative, not a theorem-negative)

- **`o(dim)` is NOT refuted** — it is measured true. What is refuted (scope-(a), with the
  measured invariant `‖⁅σ_g,A_a⁆‖_F = Θ(√dim)`) is that a **naive operator-norm /
  submultiplicative bound** on the telescoping can prove it. It cannot: the bound is `O(dim)`.
- **The reduced object of #6339 (`‖⁅ρ,A_a⁆‖_F = o(√dim)`) is still the right target** and is
  still (measured) plausibly true — but it is itself a **cancellation** among `Θ(√dim)` terms,
  *not* something a local norm bound yields. #6339's proposal to close it by bounding the local
  pieces is what this note closes.
- **A proof must track signs / phase, not norms** — i.e. the cumulant / connected-diagram
  cancellation, which is exactly where the whole arc began (`tr(Ω₂)=0`). The single-window
  reduction (#6311) and the `‖[ρ,A_a]‖_F` localization (#6339) stand; what is now clear is that
  the surviving route is *inherently* a cancellation argument, and the operator-norm shortcut
  is a dead end.

## Bottom line

The word-piece operator norms are the *easy* half (`‖σ_k‖_op = q` exactly), but the **local
commutator is Θ(√dim)** (measured, plateau ≈1.5), so the operator-norm/submultiplicative route
gives only `O(dim)` and **cannot prove `o(dim)`**. The measured `o(dim)` is a genuine
cancellation — among the telescoping terms and/or in the trace — which redirects the proof back
to the sign-tracking cumulant/connected-diagram route and rules out the norm shortcut. This is
the honest research outcome: a hopeful route closed, and the reason it closes measured exactly.
