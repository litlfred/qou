# Covariance-kernel proof epic (qou-x631) — Phase 1: two proof routes eliminated

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-covariance-epic-phase1-2026-07-18` ·
**Tier:** epic setup + route-elimination (exact) · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`. **Follows:** #3998.

## The epic

Prove the sole open input of the Δ_λ super-exponential growth bound (#3939, via the #3959
reduction):

> **`cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0`**  (equivalently `T₃ ≤ 0`,
> `Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0`, `Cov_Planch(f^λ, R₄) ≤ 0`).

Already merged (#3998): verified `k ≤ 40`; the free-cumulant framing `Σ̂₃ = R₄ + R₂`,
`E_Planch[R₄] = −k`; the sorry-free Lean reduction `D_of_T3_nonpos` (so the whole chain from the
kernel to the growth bound is Lean-proved modulo this kernel); and a faithful, positive-controlled
Lean statement `covariance_kernel_conjecture`. This is a genuine multi-session problem, tracked as
epic `qou-x631`. **This note is Phase 1: eliminate proof routes** so the effort is not wasted.

## Route 1 — holonomic recurrence (inductive proof). **RULED OUT.**

If `cov(k)` satisfied a linear recurrence with polynomial coefficients (P-recursive / holonomic),
an induction on `k` might prove the sign. It does **not**: an exact nullspace search finds **no**
such recurrence up to order 4, degree 5 over `k = 3..28`. Consistent with `Σ(f^λ)³` being
non-holonomic (`Σ(f^λ)^m` for `m ≥ 3` is conjecturally non-holonomic). So a recurrence-induction
proof is unavailable.

## Route 2 — β-monotonicity of the dimension-biased content-spread. **RULED OUT.**

Let `E_β[C₂] = Σ_λ (f^λ)^β C₂(λ) / Σ_λ (f^λ)^β` (dimension-biased content-spread; `E_2 = C(k,2)`
exactly, Plancherel). The kernel is the **β:2→3** step `E_2 ≥ E_3`. If `E_β[C₂]` were monotone
decreasing in `β` for *all* β, the kernel would be one instance of a clean master inequality
(`dE_β/dβ = Cov_β(C₂, ln f^λ) ≤ 0`), potentially provable by an FKG / rearrangement argument on the
hook lengths.

It is **not** monotone. `E_β[C₂]` decreases `2→3→4` but **increases** `4→5`:

| k | E₂=C(k,2) | E₃ | E₄ | E₅ |
|---|---|---|---|---|
| 4 | 6.000 | 5.750 | **5.7333** | **5.7846** ↑ |
| 8 | 28.000 | 26.728 | **26.3863** | **26.3979** ↑ |

So the kernel `E_2 ≥ E_3` (verified all `k ≤ 18`) is a **special** β=2→3 fact, **not** part of a
monotone family. A monotone-in-β proof cannot work.

## Net + Phase-2 target

The kernel is **non-P-recursive** and **not extendable to β-monotonicity** — a special, analytic
`β = 2 → 3` statement. The remaining route is **Śniady's genus expansion** of the joint character
cumulants (or a bespoke 2→3 argument). The core obstruction, now sharply identified:

> `f^λ = χ^λ(e)` is the **exponentially large dimension**, *not* a bounded character ratio, so it
> lies outside the algebra of polynomial functions on Young diagrams. Standard Kerov-CLT / Ivanov–
> Olshanski machinery (which controls the `Σ̂_μ` character ratios) does **not** directly apply to
> the `(f^λ)³`-weighted average. The genus expansion must be applied to the *dimension-cubed-biased*
> measure `(f^λ)³/Z`.

Phase 2 (future session) attacks this via the RSK form `T₃ = Σ_{w∈S_k} χ^{sh(w)}(3-cycle)` and
Śniady's genus expansion of `E[χ(3-cycle)]` under the biased measure.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase1.py`](../../computations/deltalambda/wlambda_covariance_epic_phase1.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase1.witness.json`

## Cross-references

- The kernel + framing + Lean infra: [`2026-07-18-deltalambda-covariance-kernel-frontier.md`](2026-07-18-deltalambda-covariance-kernel-frontier.md) (#3998)
- The reduction to the kernel: [`2026-07-18-deltalambda-D-reduction-content-covariance.md`](2026-07-18-deltalambda-D-reduction-content-covariance.md) (#3959)
- Literature: Śniady (PTRF 2006, arXiv:math/0305423), Biane (Adv. Math. 1998), Morales–Pak–Panova (arXiv:1610.07561)
