# Which α_em form is canonical: what the axioms say, and what Form B rests on

Date: 2026-11-21. Bean `qou-aemx`. Branch `claude/alpha-em-canonical-form-2026-11-21`.
Requested by the owner: explain and explore QA's finding *"α_em Form B, −0.37 ppb:
the number reproduces, but it isn't derived. Forms A, B and the CS tower are all
still live … Form B also depends on three unproved classes."*

No numerical test was run for this note. Every number quoted below is carried from
[`2026-11-20-alpha-em-two-term-q0-pull.md`](2026-11-20-alpha-em-two-term-q0-pull.md)
(probe `computations/probes/alpha_em_two_term_q0_pull_probe.py`, 70 dps) and is
marked as carried. The new content is structural, and its Lean is
[`QOU/AlphaEM/FormBVersusCSTowerClassicalLimit.lean`](../../folio/quantum-observable-universe/lean/QOU/AlphaEM/FormBVersusCSTowerClassicalLimit.lean).

## 1. The forms in plain terms

All three share the tree term `T(q) = q·[9]_q·[10]_q` (≈ 136.823 at `q₀`). The 9 and
10 come from the two genus-4 torus knots `T(2,9)` and `T(3,5)` on Bring's surface.
They differ only in what they add to `T`.

| form | what it adds to `T` | its open parameter |
|---|---|---|
| **A** | `2/(3π) + α·H`, with `H = [2]_q/(8π)`, solved as a fixed point in `α` | none beyond `H` |
| **B** | `2/(3π) + α·H·(1 − c·h²·α)`, `h = q − q⁻¹`, with `c = 1` | the Schwinger coefficient `c` |
| **CS tower** | `T·c₁/(1 − c₁κ)`, `T·c₁ = π²·(98/45)·([2]_q/2)·(1 − q⁻¹)²` | the Gram ratio `κ = det G_cl/det G_q` |

- `2/(3π)` is `b₁/Area` of Bring's surface: 8 harmonic 1-forms over area `12π`.
  The value is proved (`hodgeRatio_at_g4`, `bringZeroMode_fully_tiling_derived`).
  That it is *added to `1/α`* is the model's postulate.
- A and B are **one construction at two truncations**: B keeps the next term of the
  same self-coupling. A is B with `c = 0`.
- The CS tower is **a different object**. Its correction is a pure quantum effect
  (it carries `(1 − q⁻¹)²`).

Carried numbers at the one-term proton pin: A +0.994 ppb, B −0.365 ppb, CS tower
−467.6 ppb. At the two-term pin, B is +75.97 ppb (495 σ).

## 2. Do the axioms pick one? Not as formalised, but they split on one question

Criterion used: what each form *derives* versus what it *assumes*. Agreement with
data is not used.

**New, proved in Lean (sorry-free):** the two constructions are different functions
of `q`, uniformly in every open parameter. At the classical point `q = 1`:

- `csTower_at_one`: the CS tower equals the tree `T` for **every** `κ` and every `T`.
  Its whole correction switches off.
- `formB_at_one_gt`: every positive Form-B coupling has `1/α > T + 2/(3π)` for
  **every** `c`.
- `formB_ne_csTower_at_one`: no choice of `c`, `κ` or `T` makes them agree there.
- `formA_iff_formB_at_one`: A and B coincide at `q = 1` (the Schwinger term
  multiplies `h² = 0`).

Both right-hand sides are rational in `q` with no pole at `q = 1`, so this is also
the `q → 1` limit (`csShift_tendsto_zero`). No measured value is in the file.

**What this means.** The choice between B and the CS tower is not a choice of
order, truncation or resummation. It is the answer to one structural question:

> In the classical limit `q → 1`, does the correction to the tree coupling vanish?

- **Yes** (every correction is an `ℏ_q`-effect): Form B is excluded, because it
  keeps `2/(3π) + α/(4π)` at `q = 1`. Only a CS-type tower survives.
- **No** (a topological infrared term survives classically): the CS tower cannot
  be the whole correction. Form B's own corpus already takes this side: the
  open conjecture in
  [`2026-07-18-alpha-em-perloop-measure-status-consolidation.md`](2026-07-18-alpha-em-perloop-measure-status-consolidation.md)
  states that the `q → 1` one-loop total equals `a₀·α`, `a₀ = 1/(4π)`, which is
  nonzero.

I found no corpus axiom that answers this question. Searched: the two
content blocks (`em-coupling-bring-zero-mode`, `em-coupling-chern-simons`) and the
α audits in `docs/audits/` for "q → 1" / "classical limit". The only hit is the
2026-07-18 conjecture above, which assumes the "No" side rather than deriving it.
That is an absence on those surfaces, not a proof that no such axiom exists.

## 3. Form B's "three unproved classes": two are already settled on main

QA's list is the three typeclasses named in the `em-coupling-bring-zero-mode`
block. Their state on `main` (`e914c58`):

| class | state on main | load-bearing for Form B's number? |
|---|---|---|
| `ArchimedeanLimit x` (Faddeev limit `(1−q)·log Φ_n → Li₂`) | **Proved** for every `x ∈ [0,1)`: `archimedeanLimit_zero`, `archimedeanLimit_Ioo` (`DilogPartAConvergence.lean`). Proved **false** for `x < −1` (`ArchimedeanLimitDomain.lean`). | No. Only `x ∈ (0,1)` is used, and it is closed. |
| `BlochSuslinUniqueness D` (real-slice pentagon uniqueness) | **Holds exactly when `D = 0`** (`blochSuslinUniqueness_iff`). Its hypotheses force `τ_arch = 0` on the reals (`archimedean_functor_hyps_force_zero`), so it carries nothing. The corrected complex statement is in `BlochSuslinComplex.lean`. | No. As stated it is trivially true and empty. |
| `BringZeroModeBlochClass` (an algebraic Bloch–Wigner combination equals `2/(3π)`) | **No instance, expected false.** For algebraic arguments `D` is a period, so this would make `1/π` a rational multiple of a period (Kontsevich–Zagier predicts not). The carrier knots are torus knots, so their Bloch classes have `D = 0`. Bean `qou-006b`. | No. The value `2/(3π)` is proved as `b₁/Area` without it. The theorem `bring_zero_mode_additive_form` only restates the class field. |

So the claim "Form B depends on three unproved classes" is stale for the first two
and misdirected for the third. The third is a dead route to a constant that has a
live route.

## 4. What Form B actually rests on (the real gaps)

These are the steps that are assumed, not derived:

1. **The postulate `1/α = T + b₁/Area + …`.** Why the photon's coupling gets the
   zero-mode density added. In Lean this is the field `self_consistent` of
   `UnifiedGaugeFixedPointHomologyClass` (no instance; it is the Form-B equation
   itself, with `c` as a parameter). This is the decisive gap.
2. **The `[10]_q` in the tree term** (bean `qou-15sj`). The 3-strand trace of
   `T(3,5)` collapses to `(q − q⁻¹)[10]_q` only for the character weights
   `(1, 0, −1)`; this is stated in the open PR #8177, whose Lean file
   (`QOU/AlphaEM/ChernSimonsTowerAndT35Linchpin.lean`) is **not on main**. This gap
   is shared by A, B and the CS tower.
3. **`H = [2]_q/(8π)`.** `habiroNorm_tiling_derived` proves the identity
   `[2]_q/(8π) = [2]_q/(π(2 − χ))`. That is a rewriting; which normalisation the
   loop carries is open (the "factor ½" of the 2026-07-18 consolidation).
4. **`c = 1`.** The Hecke identity `σ − σ⁻¹ = h` is exact, so `S·S̄ = −h²` is
   proved (`hecke_skein_bar_contraction`). What is not derived is that the
   two-vertex correction *is* `α·S·S̄`. The exact singlet-channel vertex moments
   (`alpha_em_rt_phase3b_exact_vertex_moments.py`) give a different value, and the
   carried CODATA-hitting coefficient is `c ≈ 0.7312`. Deriving `c` needs the
   loop expansion defined inside the model (the RT phase-2 fermion-loop program).
   Not tractable in one session.

The CS tower's gaps, for comparison: `G_q` is a parameter (bean `qou-gbsa`), and it
shares gap 2.

## 5. Two caveats on the −0.37 ppb itself (carried, not re-measured)

- It holds at the **one-term** proton pin only. At the two-term pin Form B is
  +75.97 ppb. The owner reverted the default pin to one-term on 2026-11-20
  (`per_observable_100x_status.py` note); the 2026-11-21 ruling puts the two-term
  Lagrangian trace on the scoreboard. If that ruling moves the pin, the α row
  moves with it.
- A and B straddle the target (+0.99 / −0.37 ppb) on the one parameter `c`. Any
  `c` between 0 and 1 is "in range", so the closeness of B is evidence about the
  backbone `T + 2/(3π) + α/(4π)`, not about `c = 1`.

## 6. Beans

| bean | what |
|---|---|
| `qou-aemx` | The owner decision. Narrowed here to the classical-limit question of §2. |
| `qou-006b` | `BringZeroModeBlochClass`: expected false, not load-bearing (§3). |
| `qou-15sj` | `[10]_q` linchpin, shared by all forms; PR #8177's Lean is not on main. |
| `qou-gbsa` | CS tower `G_q`. |
| `qou-q0pl` | The carried measurements. |

## 7. What the choice moves in compute (measured 2026-11-21, 60 dps)

Owner question: *"What is impact on compute for each? Mass Q_beta?"*

| quantity | reads α_em? | form used today | shift if switched to B (or A) |
|---|---|---|---|
| m_p, m_n (`canonical_mass.py`) | no | — | 0 |
| Q_β, Δ_pn, m_μ rows of `per_observable_100x_status.py` | no | — | 0 |
| m_K/m_π (`per_observable_100x_status.py`, EM term ≈ 2.0e-4 of m_K²/m_π²) | yes | CS tower (`meson_em_sinh_closed_form.alpha_em_inv_derived`) | −0.0475 ppb (B), −0.0476 ppb (A); target 263.6 ppb |
| Coulomb energies (`coulomb_energy.alpha_em_hbar_c_mev_fm`) | yes, ∝ α | CS tower | −468 ppb relative on E_C |
| Rydberg check (`atom_electron_mass.py`) | yes, ∝ α² | CS tower (`pyhecke.constants.alpha_em_inv_mp`) | residual ≈ 935 ppb → ≈ 0.7 ppb |

The m_K/m_π shifts were computed this session. The A and B α values used as
inputs are the carried one-term-pin residuals (+0.994 / −0.365 ppb vs CODATA),
not re-measured.

**Form straddle in the dashboard.** The α_em row scores **Form B**
(`alpha-em-schwinger-ladder.witness.json :: ladder_proton.form_B_alpha_inv`),
while every consumer of α (pyhecke, the meson EM term, Coulomb) uses the
**CS tower**, which `pyhecke/constants.py` labels "physical". The two differ by
≈ 467 ppb in α⁻¹. No verdict changes today, but the α row's −0.37 ppb describes
a different object from the α the rest of the dashboard consumes. Resolving it
(rescore the row, or switch the consumers) waits on `qou-aemx`.
