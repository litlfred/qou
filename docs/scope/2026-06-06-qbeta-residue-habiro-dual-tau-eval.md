# Q_β residue-A: the bar-ODD Habiro dual of α_EM + the τ-eval map (KLR tranche 1)

**Status:** first focused tranche of the owner-authorized KLR/crystal residue-A program ([`2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md)). Addresses **sub-goal #1 (pin the archimedean evaluation map / Habiro element structure)** by constructing the residue element's parity + pole structure as the explicit dual of α_EM. Lean-formalised (sorry-free); no `c_3` claim; nothing wired.
**Owner direction:** 2026-06-06 — "pick up KLR".
**Disciplines:** *corpus-grep* (the dual was already described in the α_EM block), *formalize-first* (structural Lean statement before any numerical search), *fibre-vs-observable* kept distinct, *no 7th fit*.

---

## 1. The corpus-grep find that pins the structure

The α_EM block [`alpha-em-habiro-bar-involution`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md) already states the duality (its §Significance):

> α_EM `H = [2]_q·(1 − h²α)` is **bar-EVEN** (fixed by `q ↦ q⁻¹`) with a modular
> **zero at ζ₄** (`H(ζ₄) = 0`). "This is the same sector that the analogous Q_β
> scaling map must occupy … the Q_β analogue — whose trace difference is *not* a
> bar fixed point — required a separate cancellation analysis", and `H(ζ₄) = 0`
> is "the exact structural dual of the Q_β Habiro element's modular **pole** at ζ₄."

Two results from this session independently pin the Q_β residue to the
**bar-ANTIsymmetric** sector — i.e. it is bar-ODD, the complement of α_EM:

| route | finding | PR |
|---|---|---|
| c_k-recursion kernel | leading coeff `a_1 = −c_3 = √2·Φ₂` is **bar-odd** | #1900 |
| on-main `α_eff` | `α_eff = (z−1)·h/2`, `h = q−q⁻¹` ⇒ **bar-odd** | #1907 |

So the residue-A element is structurally fixed (not guessed): **bar-ODD, with a
ζ₄ pole, the dual of the bar-EVEN, ζ₄-zero α_EM element.**

## 2. The construction (Lean-formalised, sorry-free)

[`QBetaResidueHabiroDual.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaResidueHabiroDual.lean),
namespace `QOU.BraidKnot.QBetaResidueDual`, generic `CommRing` with `q`/`qi`
independent (bar = swap):

| object | definition | parity / locus |
|---|---|---|
| `bracketTwo` | `[2]_q = q + qi` | bar-EVEN; zero at `qi = −q` (ζ₄) |
| `heckeDiff` | `h = q − qi` | bar-ODD |
| `residueNum` | `N = h·(1 − h²α)` | bar-ODD (the dual of α_EM's `[2]_q·(1−h²α)`) |
| `F` (not a def) | `F = N / [2]_q` | bar-ODD; **pole at ζ₄** |

Sorry-free lemmas:
- `bracketTwo_bar_even`, `heckeDiff_bar_odd` — the two generators' parities.
- `residueNum_bar_odd` — `N(q⁻¹) = −N(q)` (the structural complement of α_EM's
  `alphaEmHabiro_bar_invariant`).
- `bracketTwo_zero_at_zeta4` — `[2]_q(q, −q) = 0` (= α_EM's ζ₄ zero, since `[2]_q`
  is α_EM's factor).
- `residueNum_at_zeta4` — `N(q, −q) = 2q(1 − 4q²α) ≠ 0` (generic) ⇒ `F = N/[2]_q`
  has a **pole** at α_EM's zero.
- `residue_pole_dual_to_alphaEm_zero` — the two faces of the same `[2]_q` factor
  packaged: zero (bar-even/α_EM) ↔ pole (bar-odd/Q_β).

## 3. What this buys the KLR program + what is still open

**Buys:** the residue element's *parity and pole locus* are now a theorem, not a
hypothesis — pruning the fibre-element search to **bar-odd elements singular at
ζ₄**. Two independent session routes plus the α_EM duality all agree, so this is
a firm structural anchor for sub-goals #2–#3.

**Still open (the genuine frontier):**
- **τ-eval (sub-goal #1, remainder):** the archimedean map `τ : Habiro(ℤ) → ℝ`
  that sends `F` to the *real* `c_3` at each `q₀` — the `(1 − h²α)` correction's
  `α` and the overall normalisation are not fixed by parity alone.
- **residue magnitude (sub-goal #2):** whether `A ≈ 1.804e-15` matches the
  `τ`-image of this `F` at the proton-pinned `q₀`.
- **crystal-component selection (sub-goal #3 / GAP-A-3).**

The `c_3` *value* stays uncomputed and unwired; this tranche fixes only the
algebraic sector the kernel must live in. Δ_λ gate held; no fit.

## 4. References
- α_EM dual partner: [`alpha-em-habiro-bar-involution`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md) (PR #1511).
- bar-odd kernel parity / `α_eff`: PR #1900, PR #1907 (merged); [`docs/scope/2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md`](2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md).
- KLR program master scope: [`2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md).
- Markov-trace machinery (τ substrate): [`MarkovTraceOnHecke.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean) (PR #1811).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
