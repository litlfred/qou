# Is the Δ_λ chirality sign the ±i Stokes phase? — HONEST NEGATIVE

**Date:** 2026-08-01  **Beans:** qou-5hcf (epic qou-r2nh), qou-yju0
**Branch:** `claude/stokes-phase-sign-delta-lambda-2026-08-01`
**Lean:** [`StokesPhaseSignChirality.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/StokesPhaseSignChirality.lean) — verified sorry-free (`lean`-direct exit 0)
**Reads from:** descent+Ward scaffold PR #4525 (`StokesMatrixDescent.lean`,
`WardFiltrationCounting.lean`, its open carrier `StokesPhaseSign`); PROBE-4
overturning audit [`2026-06-23-option-e-probe4-overturning-afunction-sign.md`](2026-06-23-option-e-probe4-overturning-afunction-sign.md);
KL-positivity prune [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md).
**Status:** structural test; **no fit; nothing wired**; the Δ_λ magnitude stays open.

## Question

The descent+Ward scaffold (PR #4525) proved sorry-free that the gauge-invariant
Markov trace `tr_M(S)` forces the |Δ_λ| MAGNITUDES (`overdetermined`,
`stokes_trace_conj_invariant`) but structurally cannot see the chirality SIGN
(`chiral_sign_cancels`), relocating the entire residual Δ_λ gap to
`chiralPairs(n)` signs. Its open carrier `StokesPhaseSign` conjectured the sign
is the real shadow of the **±i Stokes discontinuity**, a sign that **flips under
the bar-involution** `q ↦ q⁻¹` (its `bar_flip` field). Does it?

## TL;DR verdict — NO. The ±i phase does not supply the sign.

The ±i imaginary discontinuity is real and provable, but it **cannot** be the
Δ_λ chirality sign, because that sign is **not bar-odd**: it does not flip on
every conjugate pair, which a bar-covariant ±i phase would force. The physical
sign is a **real π-phase** — the Lusztig a-function / b-invariant parity
`(-1)^{n(λ)} = sgn(w₀^{S_{λ'}})` (already the corpus result of the PROBE-4
overturning audit) — categorically distinct from a ±i (π/2) phase.

**The task's two named anchors (n=3: 1+/2−, n=6: 6+/5−) are the misleading
special cases.** They are the *only* `n ≤ 8` where every chiral pair flips, so a
bar-odd phase and the real sign happen to agree there. The mechanism already
breaks at **n=4** (neither chiral pair flips) — between the two anchors.

## Part 1 — the ±i imaginary discontinuity IS real (proved sorry-free)

The alien derivative `Δ_ω` across a Stokes line is the discontinuity of the
Laplace transform around the Borel singularity `ξ = A`; for a simple singularity
this is the contour residue `2πi·ρ` (`ρ` the real residue). Encoded as
`stokesDiscontinuity ρ := (2πρ : ℝ)·i`:

| Claim | Lean decl | Status |
|---|---|---|
| discontinuity is purely imaginary (`.re = 0`) | `stokesDiscontinuity_re_zero` | **proved** |
| its imaginary part is the full `2πρ` | `stokesDiscontinuity_im` | **proved** |
| nonzero residue ⇒ nonzero jump | `stokesDiscontinuity_ne_zero` | **proved** |
| it is a π/2 monodromy: square is a NEGATIVE real `−(2πρ)²` | `stokesDiscontinuity_sq` | **proved** |

So the ±i-ness is not in doubt. The `2πi` is **forced** by the monodromy (no
free parameter, no fit).

## Part 2 — but it does NOT reproduce the mixed-sign Δ_λ pattern

A ±i phase that is **bar-covariant** (`q ↦ q⁻¹` acts as complex conjugation
`i ↦ −i`) imprints a sign that must **flip on every chiral pair** — this is
precisely `StokesPhaseSign.bar_flip`. Formalized as `BarOdd s := ∀ p,
p.conjugate ≠ p → s p.conjugate = − s p`.

The physical Δ_λ sign `PartitionOf5.deltaSign` (canonical, S5SO3FiberAction.lean)
**fails** it:

- `deltaSign_not_barOdd` — **proved**. Counterexample: the chiral pair
  `(5) ↔ (1⁵)` has `deltaSign(1⁵) = +1 = deltaSign(5)` — EQUAL, not opposite. The
  bar-involution does not flip it.
- `no_imaginary_phase_sources_deltaSign` — **proved**. No bar-covariant
  imaginary phase (whose sign is `BarOdd`) can equal `deltaSign`.

### The bar-flip ladder (symbolic, `n = 2 … 8`)

`sign(λ) = (-1)^{n(λ)}`, `n(λ) = Σ_i i·λ_i`. A chiral pair `{λ, λ'}` flips iff
`n(λ)+n(λ')` is odd iff `#{parts of λ,λ' that are ≡ 2,3 (mod 4)}` is odd — a
partition invariant that is **not** "λ self-conjugate or not".

| n | #chiral pairs | pairs that FLIP | pairs that do NOT flip | sign multiset |
|---|---|---|---|---|
| 2 | 1 | 1 | 0 | 1+/1− |
| 3 | 1 | 1 | 0 | 1+/2− |
| 4 | 2 | **0** | **2** | 3+/2− |
| 5 | 3 | 1 | **2** | 5+/2− |
| 6 | 5 | 5 | 0 | 6+/5− |
| 7 | 7 | 5 | **2** | 6+/9− |
| 8 | 10 | 1 | **9** | 11+/11− |

Bar-flip (the ±i-phase signature) holds ONLY at n=2,3,6 and fails at n=4,5,7,8.
The task anchors n=3, n=6 are exactly the coincidental agreements. Explicit
non-flipping chiral pairs: n=4 `(3,1)↔(2,1,1)` both −1; n=5 `(5)↔(1⁵)` both +1,
`(3,2)↔(2,2,1)` both +1.

## Part 3 — the actual sign source: a REAL π-phase (a-function parity)

`deltaSign λ = (-1)^{n(λ)} = e^{iπ·n(λ)}` is a **π (half-turn) real monodromy**:
the Lusztig a-function / b-invariant parity, equal to the sign-representation
twist `sgn(w₀^{S_{λ'}})`. This is the corpus result of the PROBE-4 overturning
audit (2026-06-23, `PartitionOf5.deltaSign_eq_nStat_parity`). It squares to `+1`
(`chirality_sign_is_real_pi_phase`, composing the two corpus lemmas) — a π
monodromy, whereas the ±i discontinuity squares to a *negative* real (Part 1), a
π/2 monodromy. **Different monodromy orders ⇒ the ±i phase cannot be the
source.** The sign lives in the a-grading (writhe/framing channel), not in the
imaginary Stokes phase.

## Proved / open split

| Assertion | Disposition |
|---|---|
| Stokes discontinuity `2πi·ρ` is purely imaginary, nonzero, π/2 monodromy | **proved sorry-free** (`stokesDiscontinuity_*`) |
| the physical Δ_λ sign is NOT bar-odd (counterexample `(5)↔(1⁵)`) | **proved sorry-free** (`deltaSign_not_barOdd`) |
| no bar-covariant imaginary phase supplies `deltaSign` | **proved sorry-free** (`no_imaginary_phase_sources_deltaSign`) |
| the sign is the real π-phase `(-1)^{n(λ)}` (a-function parity), square +1 | **proved sorry-free** (`chirality_sign_is_real_pi_phase`, from corpus lemmas) |
| the Δ_λ MAGNITUDE `|Δ_λ| = dim` | **OPEN** — relocated to PROBE-2 / s5-so3 keystone (unchanged) |

## Scope discipline (STRICT)

This is a **scope-(b) structural exclusion** of one specific mechanism, licensed
by a **proved invariant** (bar-parity): a bar-covariant ±i Stokes phase imprints
a bar-odd sign; the target `(-1)^{n(λ)}` is provably not bar-odd (it fails to
flip on named chiral pairs); therefore that mechanism cannot source the sign.
What is excluded is *the bar-covariant ±i phase as the sign source* — **not** the
existence of the ±i discontinuity (which is proved), and **not** any role for
resurgence in the Δ_λ *magnitude*. The `StokesPhaseSign` carrier's `bar_flip`
axiom is simply **inconsistent with the physical target**; the carrier can be
retired as the sign mechanism. The a-function-parity source (corpus, PROBE-4
overturning) stands as the actual, already-identified origin.

**Anti-fit:** the ±i phase and its bar-covariance were tested as forced by the
singularity structure — never tuned to reproduce signs. The negative is honest:
the mechanism fails, and it fails at n=4, *between* the two anchors where it
superficially appeared to work.

## Cross-references

- Descent+Ward scaffold PR #4525 (`StokesMatrixDescent.lean`,
  `WardFiltrationCounting.lean` — `StokesPhaseSign`, `chiral_sign_cancels`)
- [`2026-06-23-option-e-probe4-overturning-afunction-sign.md`](2026-06-23-option-e-probe4-overturning-afunction-sign.md) — the a-function-parity sign source
- [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md) — KL-positivity prune (magnitude vs sign)
- `S5SO3FiberAction.lean` — canonical `PartitionOf5.deltaSign`, `deltaSign_eq_nStat_parity`
