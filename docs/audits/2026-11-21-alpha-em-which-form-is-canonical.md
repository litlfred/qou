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

**Resolved by two labelled arms (owner card choice, 2026-11-21).** The α_em row
of `per-observable-100x-status.witness.json` now carries `arms` with each form
scored the same way: `cs_tower` 467.6 ppb (3.052e5× miss), `additive_A_c0`
0.9937 ppb (648.4×), `additive_B_c1` 0.3652 ppb (238.3×). It also records
`consumer_arm: cs_tower` and `canonical_form: OPEN (qou-aemx)`. The headline
`pred_MeV` stays the B arm only for existing readers, and every arm misses the
100× target, so the scoreable count (1 / 6) does not depend on the headline.
No other number in the witness moved.

## 8. Proved after the review (owner picked items 1, 2, 3)

All lean-direct exit 0, no warnings, axioms `propext, Classical.choice, Quot.sound`.

1. **`[10]_q` from the actual `H₃(q)` representations** —
   `QOU/AlphaEM/T35TenLinchpinFromH3.lean`. Explicit 2-dimensional representation
   checked against the Hecke and braid relations; the characters of `(σ₁σ₂)⁵` are
   `q¹⁰`, `−1` and `q⁻¹⁰` (`hook_trace_T35`: the hook value is `−1` for every `q`).
   `t35_weights_unique`: a weighted sum equals `q¹⁰ − q⁻¹⁰ = (q − q⁻¹)[10]_q` for all
   nonzero rational `q` iff the weights are `(1, 0, −1)`. Convention-D weights (zero
   on `(1,1,1)`) cannot produce it. Still open: why the photon carries `(1, 0, −1)`.
   PR #8177 proves the weight equivalence only for abstract integer characters.
2. **`κ(1) = 1`** (`kappa_one`): the `q`-Gram matrix of `meson_em_sinh_closed_form`
   reduces to the classical one at `q = 1`, and `det G_cl = π⁴·45375/72900 ≠ 0`.
3. **Forms A and B define a unique small coupling**
   (`isFormB_existsUnique_small`): for `T > 0`, `q > 0` and `2·c·h² ≤ T + 2/(3π)`,
   exactly one `α ∈ (0, 1/(T + 2/(3π))]`; any other positive root has `c·h²·α > 1`
   (`formB_large_root`).

## 9. Why the photon carries `(1, 0, −1)`: two findings and one negative (owner picked items 1 and 2)

The open question from §8 item 1 is where the Markov weights `(1, 0, −1)` on the
blocks `(3), (2,1), (1³)` of `H₃(q)` come from. Two Lean results and one exact probe.

**Finding A, the chiral vertex is invisible to the supertrace**
(`QOU/AlphaEM/PhotonBlockCharacters.lean`, `photon_supertrace`). With the ruled
photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`, `σ₀σ₁⁻¹` acts as `1` on both
one-dimensional blocks, so `χ_(3)(γ) − χ_(1³)(γ) = (φ₀ + φ₁)·[2]_q` with no `φ₀₁`.

**Finding B, γ's own characters are proportional to `(1, 0, −1)` only without
the chiral vertex** (`photon_chars_supertrace_iff`). For `q ≠ 0` and
`q² + 1 + q⁻² ≠ 0`: `χ_(3) + χ_(1³) = 0` and `χ_(2,1) = 0` iff `φ₀₁ = 0` and
`(φ₀ + φ₁)(q − q⁻¹) = −2`. So the photon, read as a functional through its own
characters, does not supply the weights while it carries its fourth term. Scope (a).

**Negative, the `U_q(gl(1|1))` supertrace** (exact probe
`computations/alpha_em/photon_gl11_supertrace_weights_probe.py`, 8/8). Hecke, braid
and the Markov twist `μ = 1` check. The full supertrace on `V^{⊗3}` vanishes on all
of `H₃(q)`. The cut supertrace (one strand open) has weights
`q²/[3]_q · (1, −1, 1)`, the Alexander normalisation, and gives
`q²/[3]_q (q¹⁰ + 1 + q⁻¹⁰)` on `(σ₁σ₂)⁵`, not `(q − q⁻¹)[10]_q`. Scope (a): this
representation alone. The sign alternates on the hook, so it does not zero `(2,1)`.

Lean: lean-direct exit 0, axioms `propext, Classical.choice, Quot.sound`. Still open:
a construction that zeros the hook block and gives the two one-dimensional blocks
opposite signs.

## 10. The Young projector trace (owner picked option 3, 2026-11-22)

`τ = χ_(3) − χ_(1³)` has weights `(1, 0, −1)` by definition. The question is whether
anything natural produces it. Three results, the probe now 13/13:

1. **`τ` is not a Markov trace.** `τ(1) = 0` but `τ(σ₂) = [2]_q`, so no `z` gives
   `τ(xσ₂) = z·τ(x)` on `H₂`. It cannot come from the usual normalised link trace.
2. **`τ` is the `gl(1|1)` supertrace on the two extremal sectors.** `Ř` preserves
   the number `k` of odd tensor factors in `V^{⊗3}`. The supertrace of sector `k` has
   weights `(1,0,0)`, `(−1,−1,0)`, `(0,1,1)`, `(0,0,−1)` for `k = 0, 1, 2, 3`. So the
   all-even plus all-odd sectors give exactly `τ`, and the mixed sectors give `−τ`,
   which is why the full supertrace is zero (§9).
3. **No single super vector space gives `τ`**
   (`QOU/AlphaEM/YoungTraceNoSuperDimension.lean`,
   `no_superdim_gives_young_trace`, lean-direct exit 0, standard axioms). At `q = 1`
   the Schur-functor dimensions `d(d+1)(d+2)/6`, `d(d−1)(d+1)/3`, `d(d−1)(d−2)/6`
   are never `c·(1, 0, −1)` with `c ≠ 0`.

Still open: why the photon would select the extremal sectors. Nothing above ties the
two; Finding A (§9) only shows that `τ(γ) = (φ₀ + φ₁)[2]_q`.

## 11. Can the photon select the extremal sectors? (owner picked option 3, 2026-11-22)

No element of `H₃(q)` can, the photon included. Exact probe, now 18/18.

- The ordinary trace of each sector gives its block multiplicities: `k = 0` is `(3)`,
  `k = 1` is `(3) ⊕ (2,1)`, `k = 2` is `(2,1) ⊕ (1³)`, `k = 3` is `(1³)`.
- `Ř` preserves `k`, so every element of `H₃(q)` maps each sector to itself.
- The two mixed sectors together contain all three blocks. For `[2]_q[3]_q ≠ 0`,
  `H₃(q)` is semisimple (`M₁ ⊕ M₂ ⊕ M₁`), so an element that acts by zero on the
  mixed sectors is zero. No nonzero `x ∈ H₃(q)` keeps the extremal sectors and
  removes the mixed ones.

So `τ(x) = str(P_ext · x)`, where `P_ext` projects onto the weights `(3,0)` and
`(0,3)`. `P_ext` is a Cartan element of `U_q(gl(1|1))`: it commutes with `H₃(q)`
and sits on the other side of Schur–Weyl duality. Whatever selects the `(1,0,−1)`
weights has to come from the gauge (gl(1|1)) side, not from the braid word or the
photon element. Scope (b) for "an element of `H₃(q)` does the selecting", with the
invariant being faithfulness of the mixed sectors. The semisimplicity step is quoted
here, not proved in Lean.

Coordination: the norm-one photon work (PR #8981, `PhotonBarClosure.lean`) was
asked whether its block norms fix the sign-block to trivial-block ratio at `−1`.

## 12. Which gl(1|1) Cartan insertions give `(1, 0, −1)` (owner picked options 2 and 1, 2026-11-22)

Let `H = E₁₁ − E₂₂` act on `V^{⊗3}`; it equals `3 − 2k` on the sector with `k` odd
factors. Insert a diagonal `f(H)` into the supertrace. Exact probe, now 21/21:

- The block weights of `x ↦ str(f(H)·x)` are exactly
  `(f(3) − f(1), f(−1) − f(1), f(−1) − f(−3))`.
- So they are proportional to `(1, 0, −1)` iff `f(1) = f(−1)` and `f(3) = f(−3)`,
  that is `f` is even under `H ↦ −H` (equivalently `K ↦ K⁻¹`, `K = q^H`), with
  `f(3) ≠ f(1)`.
- `K` alone fails (nonzero hook weight). `K + K⁻¹` gives `[2]_q h² · (1, 0, −1)`;
  `K² + K⁻²` and `H²` also give the direction.

What this settles: the direction `(1, 0, −1)` is forced by one structural condition,
evenness of the Cartan insertion under `K ↦ K⁻¹`. What it does not settle: the
overall scale `f(3) − f(1)`, which differs between `K + K⁻¹`, `K² + K⁻²` and `H²`.
Choosing among them by the α_em value would be selection against the target. The
link to the photon, and whether `K ↦ K⁻¹` is the bar involution on the gauge side,
is still open; the norm-one photon thread (PR #8981) has been asked about it.
No Lean change: the criterion is linear algebra on the sector weights, which are
computed exactly in the probe, not formalised.

## 13. Is the Cartan insertion derivable? (owner, 2026-11-22: work the options)

**The direction, yes, from one symmetry. The reason for that symmetry and the sign, no.**

1. **`(1, 0, −1)` is the same thing as oddness under `ι : σᵢ ↦ −σᵢ⁻¹`.**
   `QOU/AlphaEM/IotaOddTrace.lean`, `iota_odd_iff` (lean-direct exit 0, axioms
   `propext, Classical.choice, Quot.sound`): for `q ≠ 0`, `q² + 1 + q⁻² ≠ 0` and
   characteristic 0, a block functional satisfies `τ(ι x) = −τ(x)` on every word iff
   its weights are `w₃·(1, 0, −1)`. `ι` swaps the trivial and sign blocks;
   `trace_iota_hook` shows it keeps the hook character, via an explicit intertwiner
   `P` with `det P = q² + 1 + q⁻²`.
2. **On the gl(1|1) side `ι` is the parity swap.** The trace of `ρ(ιx)` on sector `k`
   equals that of `ρ(x)` on sector `3 − k`. Because 3 is odd, the supertrace sign
   flips under this swap, so an insertion `f(H)` that is even under `H ↦ −H`
   (`K ↦ K⁻¹`) gives an `ι`-odd functional. This is why §12's condition appears.
3. **Scale, up to sign.** Among even insertions, the idempotent ones with nonzero
   weights are `P_ext` (weights `(1, 0, −1)`) and `1 − P_ext` (`(−1, 0, 1)`).
   `P_ext = (c − c(1))/(c(3) − c(1))` with `c = K + K⁻¹`. Asking for a projection fixes
   the scale; the sign (keep the extremal sectors or the mixed ones) stays a choice.
4. **Casimir route: excluded.** A central element of `U_q(gl(1|1))` acts on `V^{⊗3}`
   by a `U`-endomorphism, hence by an element of `H₃(q)` (Schur–Weyl double
   centraliser, Mitsuhashi; quoted, not proved here). The full supertrace vanishes on
   all of `H₃(q)` (§9), so any central insertion gives zero. Scope (b), invariant: the
   vanishing full supertrace. Only a non-central (torus) insertion can work.

Probe `photon_gl11_supertrace_weights_probe.py` now 26/26 (`ι` Hecke and braid
relations, the sector swap, `P_ext` as a polynomial in `K + K⁻¹`).

Still open, and not derived: why the α_em functional should be `ι`-odd, and the sign.
`ι` sends the chiral vertex `σ₀σ₁⁻¹` to `σ₀⁻¹σ₁`; the ruled photon is not `ι`-invariant.

## 14. Is mass the real part and α_em the imaginary part? (owner, 2026-11-22)

**Partly. The α_em functional is a definite piece of the Markov trace, and it is a
writhe (framing) phase. That mass is the other piece is not shown.**

1. **The Markov trace splits by `ι : σᵢ ↦ −σᵢ⁻¹`.** Under convention D the weights
   are `y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²`, `y₁₁₁ = 0`. The `ι`-odd part of
   `tr_M` is `(y₃ − y₁₁₁)/2 · τ = (y₃/2)·τ`, with `τ = χ_(3) − χ_(1³)` the α_em
   functional of §10. So the α_em functional is already inside the canonical trace,
   with its scale fixed by `z_D`. (Probe, exact, 10 words.)
2. **`τ` reads only the exponent sum `e` (the writhe):** `τ(w) = q^e − (−q⁻¹)^e`.
   Under `q ↦ q⁻¹` it is even for odd `e` and odd for even `e`
   (`QOU.AlphaEM.TauExp.tau_eq`, `tau_bar`, sorry-free, generic field).
3. **Electron `σ₀σ₁σ₀`:** `e = 3`, `τ = q³ + q⁻³` (bar-even). Linchpin `(σ₁σ₂)⁵`:
   `e = 10`, `τ = q¹⁰ − q⁻¹⁰` (bar-odd).
4. **Where real and imaginary appear.** On the unit circle `q = e^{iθ}`, the two
   one-dimensional blocks give `q^e` and `(−q⁻¹)^e = (−1)^e q̄^e`. So
   `χ_(3) ± χ_(1³)` are `2 Re q^e` and `2i Im q^e`, and which is which is swapped by
   the parity of `e`. This is the sense in which braid words intertwine the two
   parts: the word decides it through its writhe. At real `q₀` (`Im q₀ = 0`) there
   is no phase, so this is a fibre-level statement, not an observable one.
5. **Relation to the corpus.** `rem:mass-modulus-em-phase-color-grading` reads EM as
   the framing phase `arg tr_M`, picked up as the ribbon twist `q^{2w c(λ)}` of writhe
   `w`. Items 2 and 4 agree with that: `τ` sees the word only through its writhe.
   That remark reads mass as the modulus (polar). `conj:binding-qbeta-complex-volume`
   and `conj:complex-mass-constituent-functional` read additive Re/Im splits instead.
   This section supports none of the three over the others: it locates the α_em
   functional as the `ι`-odd part, and says nothing yet about where mass sits.

**Not shown:** that mass is the `ι`-even part; why α_em should be `ι`-odd; the sign.

## 15. The electron and α_em, and the three follow-ups (owner, 2026-11-22: "do all three")

Weights are convention D, `y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²`, `y₁₁₁ = 0`.
`τ = χ_(3) − χ_(1³)` is the α_em functional; the `ι`-odd part of `tr_M` is `(y₃/2)·τ` (§14).

1. **The electron word is one phase on one block.** In the hook representation
   `σ₀σ₁σ₀` has trace `0` (`QOU.AlphaEM.ElectronWord.electron_hook_trace`, sorry-free).
   So for any weights its block trace is `w₃q³ + w₁₁₁(−q⁻¹)³`
   (`electron_block_trace`), and under convention D
   `tr_M(σ₀σ₁σ₀) = y₃·q³`. Polar form: modulus `y₃`, phase `q³`, the exponent being
   the writhe `3`.
2. **Its α_em part and its other part.** `tr_M(e) = y₃(q³+q⁻³)/2 + y₃(q³−q⁻³)/2`. The
   first summand is the `ι`-odd (α_em) part, the second the `ι`-even part. With
   `q = e^λ` they are `y₃ cosh 3λ` and `y₃ sinh 3λ`. On `|q| = 1` (`y₃` is real there)
   they are `y₃ cos 3θ` (real) and `i y₃ sin 3θ` (imaginary). So **for the electron the
   α_em part is the real part**, not the imaginary one. For the linchpin `(σ₁σ₂)⁵`
   (writhe 10) the α_em part is imaginary. At `q = 1`, `tr_M(e) = 1/2` and all of it
   is the α_em part.
3. **Option 1, the mass formula.** The canonical nucleon mass uses
   `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³` with `β_Bor = (σ₀σ₁⁻¹)³`, and the muon anchor uses
   the volume of the figure-eight knot, whose braid word `(σ₀σ₁⁻¹)²` we test. Both words
   have writhe `0`, so `τ` vanishes on them for every
   `q` (`borromean_tau`, `figureEight_tau`): their `tr_M` is entirely `ι`-even. So the
   mass formula does read only the `ι`-even part, **but only because its words have
   writhe 0**. That is not a selection rule: it says nothing about a word of nonzero
   writhe, the electron included.
4. **Option 2, `q = 1`.** `τ(w)(1) = 1 − (−1)^e`: zero on even writhe, `2` on odd. The
   only `ι`-odd object in α_em, `τ(T35) = (q − q⁻¹)[10]_q`, vanishes at `q = 1`; the
   coupling `α = q⁻¹/([9]_q[10]_q)` survives there only after dividing by `h`. The
   n − p term `−m_e/720` (n–p thread, PR #8804, `PREREGISTRATION-em-term.md`) is
   `α(1)·S` with `S = QPair·hol`, `hol = V³` of writhe 0, and the adopted quark charges.
   So it is not an `ι`-odd trace effect: the `ι` split does not explain why that term
   survives `q = 1`. (Scope (a).)

**Not shown:** that mass is the `ι`-even part as a principle; any link between the
electron's writhe 3 and the linchpin's 10; why α_em is `ι`-odd; the sign.

## 16. The photon on the electron, and T(3,5) as the electron cubed (2026-11-22)

Lean: `QOU/AlphaEM/PhotonElectronTrace.lean` (sorry-free, standard axioms only).
Probe: `computations/alpha_em/photon_gl11_supertrace_weights_probe.py`, 40/40.

**Photon.** `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`. The trace is linear, so each term is read
by its writhe. The chiral vertex `σ₀σ₁⁻¹` has writhe 0, and `τ` vanishes on it
(`chiralVertex_tau`). Each single letter gives `τ = q + q⁻¹` (`letter_tau`). The ι-odd
part of the convention-D trace of `γ` is therefore
`(φ₀ + φ₁)(q⁴+1) / (2q(q²+1))`, which is `(φ₀ + φ₁)/2` at `q = 1`.

**Photon on the electron.** `γ·e` has terms of writhe 3, 4, 4, 3. At `q = 1`, `τ` is
`1 − (−1)^e`, so the writhe-4 terms drop and the ι-odd part is `(1 + φ₀₁)/2`. On the
electron, only the chiral vertex carries `α_em` at `q = 1`. The single letters, which
carry it on the bare photon, do not.

**Writhe 3 and writhe 10.** The braid identity `(σ₀σ₁)⁵ = Δ²·Δ·σ₁` with `Δ = σ₀σ₁σ₀`
(the electron word) and `Δ² = (σ₀σ₁)³` (the full twist) gives

    T(3,5) = electron³ · σ₁.

Lean proves it on all three blocks of `H₃(q)`: on the hook block (`t35_hook`) and on the two
one-dimensional blocks (`t35_sym_alt`). Since `H₃(q)` is semisimple at generic `q`, the
identity therefore holds in `H₃(q)`. The full twist acts as `1` on the hook block
(`electron_sq_hook`). The test was registered before it was run: among
`electron^k · (photon term)` for `k ≤ 4`, writhe 10 occurs only as `electron³·σ₀` and
`electron³·σ₁`. These two have the same trace.

**What this shows, and what it does not.**

- It shows that the `[10]_q` linchpin word is reachable from the electron word and one
  photon letter. It is the `φ₁` term (or the `φ₀` term) of `γ·e³`.
- It does not show why the electron enters cubed, or why `α_em` should read this term.
  It also fixes no value, and nothing in it was chosen against a target.
- At `q = 1` the writhe is 10, which is even, so `τ(T35) = 0`. The linchpin's content is
  off `q = 1`, which matches §15: on `|q| = 1` its α_em part is imaginary.

## 17. Why the cube? The torus family T(3, 3m+2) (2026-11-22)

Lean: `QOU/AlphaEM/TorusFamilyTrace.lean` (sorry-free, standard axioms only). Probe 43/43.

- `(σ₀σ₁)²` is literally the list `electron ++ [σ₁]` (`trefoil_eq_electron_letter`). Its
  closure is a knot, the trefoil `T(3,2)`. The electron word alone closes to a 2-component
  link, since its permutation is a transposition. So one photon letter turns the electron's
  Hopf-link closure into a trefoil, which is the backup electron of the owner ruling.
- With `m` full twists, `Δ² = electron²` gives `(σ₀σ₁)^(3m+2) = electron^(2m+1)·σ₁`. This is
  `T(3, 3m+2)`, of writhe `6m + 4`. `m = 1` is the `T(3,5)` linchpin.
- Full twists act as `1` on the hook block (`hookWord_fullTwists`). So the hook trace is `−1`
  for every `m` (`torusWord_hook_trace`), and `τ = q^(6m+4) − q^-(6m+4)` (`torusWord_tau`).
  The trace of `T(3,5)` is `y₃q¹⁰ − y₂₁`. Unlike the electron's trace, this is not a single phase.
- At `q = 1` the ι-odd part of `γ·electron³` is `(1 + φ₀₁)/2`. That is the same value as for
  `γ·electron`, because the extra full twist is invisible there.

**Answer to "why k = 3".** The braid group does not force it. Every odd power
`electron^(2m+1)·σ₁` is a 3-strand torus knot, and `k = 3` is `m = 1`: one full twist on
top of the trefoil. In this algebra the family members differ only in which power of `q`
`τ` reads. So choosing `m = 1` needs a reason from outside, which is the `[10]_q` value
itself. Using that value to choose `m` would be selection against the target. Scope (a):
nothing here excludes a reason for `m = 1` that comes from somewhere else.

## 18. What picks one full twist: the Bring genus bound (2026-11-22)

**Correction to §16–§17: prior work I missed.** `QOU/BraidKnot/WeakVertexElectronFactor.lean`
(on main, 2026-11-21) already proves `(σ₀σ₁)⁵ = e⁻ · (e⁻ · (σ₀σ₁)²)` and
`e⁻ · e⁻ = (σ₀σ₁)³` in the braid group `B₃` itself (`weakVertex_eq_electron_mul`,
`electron_sq_eq`). That is stronger than the block-level `t35_hook` / `t35_sym_alt` of #9017,
which were derived again without citing it. There it is the `3 + 7` crossing split of the
β-decay weak vertex. The block-level lemmas remain correct and are consistent with it.
Neither result moves any number.

**Corpus search.** §1 of this audit already says the 9 and the 10 of `q·[9]_q·[10]_q` "come
from the two genus-4 torus knots `T(2,9)` and `T(3,5)` on Bring's surface". The genus rule
`g(K) ≤ 4 = g(Σ₄)` is `rem:bring-embeddable-knots`, and the generator set is
`prop:torus-knot-generators` (`brings-surface/torus-knot-generators.lean`). The
electroweak blocks call `{T(2,9), T(3,5)}` the *saturating* carriers: the only coprime
solutions of `(p−1)(q−1) = 8`.

**Applied to the electron family** (`QOU/AlphaEM/TorusFamilyGenus.lean`, sorry-free):

- `T(3, 3m+2) = e^(2m+1)·σ₁` has genus `3m + 1`. The Bring bound allows `m ∈ {0, 1}`
  (trefoil, `T(3,5)`), and genus 4 holds only at `m = 1`.
- The backup-electron family `T(2, 2m+1) = σ₀^(2m+1)` has genus `m`, and genus 4 holds only
  at `m = 4`, which is `T(2,9)`.

So the one full twist is the genus-saturation rule the corpus already uses for both factors
of the tree term. It is not chosen from the α_em value.

**Status of that rule, stated plainly.** The genus bound is a `remark`, and its
exhaustiveness is marked open (`rem:knot-exhaustiveness`). "Saturating" is stated as a
selection mechanism inside conjecture-level electroweak blocks; it is not proved. So `m = 1`
rests on an adopted rule, not on a theorem. Two further limits: the photon letter could
enter at another position, and in `B₂` any odd power of `σ₀` is "electron-built", so the
backup family is a weak statement.

## 19. Can "saturation" (genus exactly 4) be derived? Not as an identification of curves (2026-11-22)

**What the corpus actually says.** `rem:torus-knot-generators-interpretation` uses
"saturation" descriptively: `T(2,9)` "at genus 4 exactly saturates Bring's surface", and
"new particle types would require composite construction". That is the bound being met,
not a rule that selects the genus-4 member. The selective use ("the saturation mechanism
that forces `{T(2,9), T(3,5)}`") appears only in the conjecture-level electroweak blocks.
The same remark also names `T(2,3)` as the electron and calls `T(2,9)` "symmetry-broken".
That predates the 2026-11-21 owner ruling (electron = `σ₀σ₁σ₀` with Hopf closure, trefoil as
backup). It is recorded here and not edited, since that is an owner call.

**One natural derivation route, tested.** The route: the saturating knots are singled out
because their fibre *is* Bring's curve. `T(3,5)` and `T(2,9)` are the links of `y³ = x⁵` and
`y² = x⁹`. Their Milnor fibres compactify to the smooth genus-4 curves `y³ = x⁵ + 1` and
`y² = x⁹ + 1`, which carry automorphisms of order 15 and 9 (standard, cited). The corpus
records `Aut(Σ₄) ≅ S₅`. `QOU/AlphaEM/SaturationNotBringFibre.lean` (sorry-free, by cycle
types) proves that `S₅` has no element of order 9 or 15. So neither curve is Bring's curve,
and the genus-4 match is topological only.

**Scope (a).** This rules out *that* identification, under the standard algebraic structure
on the Milnor fibre. It does not rule out a different reason for the genus-4 member, for
example a topological embedding of the fibre surface into `Σ₄`, or an `S₅`-equivariance
argument. The saturation rule stays adopted, not derived.

## 20. The topological route: no S₅-equivariant embedding of a genus-4 fibre surface (2026-11-22)

**Question (pre-registered before any proof was attempted).** §19 left open whether the
genus-4 members `T(3,5)` and `T(2,9)` could be tied to Bring's surface `Σ₄` topologically
rather than as curves. Two readings were tested, and the outcome of each was written down
as "embeds", "does not embed" or "undecided" before starting:

1. *Subsurface reading.* The fibre surface `F` (genus 4, one boundary circle) sits in `Σ₄`
   as an `S₅`-invariant subsurface.
2. *Mapping-class reading.* The monodromy `h` of the fibration (order 15 for `T(3,5)`,
   order 18 for `T(2,9)`, after capping the boundary) lies in a finite group of mapping
   classes of the closed genus-4 surface together with an `S₅`, for example commuting with
   it or normalising it.

**Result: neither reading holds. Both are scope-(b) exclusions with named invariants.**

*Reading 1.* A genus-4 one-boundary subsurface `F ⊂ Σ₄` has complement a closed disk `D`.
If `S₅` preserved `F` it would preserve `D`. The `S₅` action is holomorphic, so it is
faithful on `D` (an automorphism that is the identity on an open set is the identity). A
finite group of homeomorphisms of a closed disk is conjugate to a subgroup of `O(2)`
(Kerékjártó; Eilenberg), so it fixes a point `p`. The stabiliser of `p` in a holomorphic
action acts faithfully on the tangent line, hence is cyclic. That would make `S₅` cyclic,
and `perm5_not_isCyclic` proves it is not. The argument uses only the genus and the single
boundary circle, so it excludes `T(3,5)` and `T(2,9)` alike.

*Reading 2.* By Nielsen realisation (Kerckhoff 1983, cited as [Ker] in the held source
`library/bn/`), a finite group of mapping classes of the closed genus-4 surface acts by
conformal automorphisms of some complex structure. The largest conformal automorphism group
in genus 4 has order 120 and belongs to Bring's surface (`library/210811825v1/`, appendix
E; `def:brings-surface`). If `h` normalises or commutes with an `S₅`, the group they
generate is finite (a finite-order element normalising a finite group), contains `S₅`, and
has order at most 120. `no_overgroup_of_perm5` proves such a group has no element of order
15 or 18. So `h` cannot be there.

**Lean.** Appended to `QOU/AlphaEM/SaturationNotBringFibre.lean`, lean-direct exit 0,
`#print axioms` free of `sorryAx`:

| Declaration | Statement |
|---|---|
| `perm5_not_isCyclic` | `S₅` is not cyclic |
| `perm5_no_order_18` | `S₅` has no element of order 18 |
| `no_overgroup_of_perm5` | a finite group of order ≤ 120 containing `S₅` has no element of order 15 or 18 |

The topological inputs (disk actions are linear, cyclic point stabilisers, Nielsen
realisation, the genus-4 bound 120) are cited, not formalised.

**What this does and does not say.** Every route tried so far fails to tie the genus-4
member to `Σ₄` beyond the number 4: not as a curve (§19), not as an invariant subsurface,
not through its monodromy. So the selection of exactly one full twist (`T(3,5)`, genus 4)
rests on the Bring bound `g ≤ 4` plus the adopted saturation rule, and saturation is still
not derived. This does not touch the bound `g ≤ 4` itself, which only needs a topological
embedding without equivariance, and that always exists for `g ≤ 4`.

**A discrepancy with the corpus, flagged and not changed.** `prop:s5-equivariant-torus-knots`
and audit `2026-06-02-lepton-t2n-torus-tower.md` §2 call `T(2,n)` `S₅`-equivariant when
`ℤ_n ↪ S₅`. The monodromy of `T(2,n)` has order `2n`, not `n`. Under a monodromy-order
criterion the verdicts change: `T(2,3)` (order 6) passes, `T(2,5)` (order 10) fails. Which
cyclic group the corpus criterion means is an owner question. Nothing here edits that block.

## 21. Both equivariance tests stated (owner card, 2026-11-22)

Following the owner's choice on the discrepancy flagged in §20, `prop:s5-equivariant-torus-knots`
now states both tests. The ℤₙ test (`S₅` has an element of order `n`) holds for `n ∈ {3, 5}`;
the monodromy test (order `2n`, i.e. `ℤ₂ × ℤₙ`) holds only for `n = 3`. New sorry-free Lean in
`observations/s5-equivariant-torus-knots.lean`, proved from cycle types rather than from the
hand-entered order table: `s5_order_dvd_sixty`, `s5_five_dvd_order`, `s5_has_order_iff`,
`s5_has_order_two_mul_iff`. No other block was changed; blocks citing the proposition keep the
ℤₙ reading unless they say otherwise.
