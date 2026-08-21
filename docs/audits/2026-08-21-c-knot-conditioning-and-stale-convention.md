# The `C_knot` deficit: the recorded figures are convention-C-stale, the reported spread is measured in an ill-conditioned coordinate, and the named "surviving direction" is already closed

**Date:** 2026-08-21 · **Branch:** `claude/cknot-deuteron-deficit-2026-08-21` · **PR:** #5406
· **Bean:** `qou-3q7t` · **Axis:** Δ_λ / `C_knot` magnitude
· **Tier:** scope-(a) throughout — a correction to the *interpretation* of a recorded measurement,
plus two currency corrections. **No closure. No fit. Nothing wired. Δ_λ magnitude stays OPEN.**

## 0. BLUF

Three findings, none of which derives the magnitude, all of which change what the next agent should
spend a session on.

1. **The figures recorded for this bean are convention-C-stale.** `qou-3q7t` and
   [`2026-08-02-c-knot-nonuniversal-pinned-weight.md`](2026-08-02-c-knot-nonuniversal-pinned-weight.md)
   both carry `C_knot = 5.85 / 4.44 / 3.29 / 9.31`, spread `2.83×`. The producer moved to canonical
   convention D on 2026-08-11 (`70d1ade383`, `qou-4jut`); the committed witness reads
   `6.0679 / 6.7061 / 4.9054 / 290.007`, spread `59.12×`. The verdicts survive; the magnitudes do not.
2. **The `59.12×` is dominated by one ill-conditioned denominator, and so was the `2.83×`.** The master
   sum is alternating; `κ(⁴He) = |S|/Σ_λ|t_λ| = 0.0080`, a `126×` near-cancellation whose largest single
   block term is `52×` the whole signed sum. Re-expressed per block the same information gives spread
   `2.05×`. Formalized sorry-free.
3. **The one "surviving direction" the bean names is already closed, by a probe that landed the same
   day.** The bean says the per-vertex q-Reeb eigenphase "remains the one non-circular opening".
   [`2026-08-02-qreeb-eigenphase-compactness.md`](2026-08-02-qreeb-eigenphase-compactness.md)
   (`qou-0g4z`) shows every rotational block is **compact**, so the eigenphase channel is bounded and
   cannot supply an absolute scale — scope-(a), with a structural reason rather than a failed search.

## 1. Convention-C staleness (finding 1)

| K | H_n | `\|S(K)\|` conv-C | `\|S(K)\|` conv-D | `C_knot` conv-C | `C_knot` conv-D | move in `\|S\|` |
|---|---|---|---|---|---|---|
| D | 6 | 0.7438 | 0.71745 | 5.853 | **6.0679** | 3.5% |
| T | 9 | 3.7349 | 2.47514 | 4.444 | **6.7061** | 34% |
| ³He | 9 | 4.5883 | 3.07899 | 3.292 | **4.9054** | 33% |
| ⁴He | 12 | 5.9456 | **0.19094** | 9.313 | **290.007** | **96.8%** |
| | | | | spread **2.83×** | spread **59.12×** | |

Mirror ratio `C_knot(T)/C_knot(³He)`: `1.35 → 1.3671`. Corrected in this PR: the audit doc (banner,
C-era table kept legible and marked), the bean body, and the header docstring of
[`CKnotNonUniversal.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/CKnotNonUniversal.lean),
which still quoted the C figures while the file's own constants and its refresh note below them were
already convention D — the header contradicted the file. **The bean's own TITLE still names `5.85`.**

## 2. The spread is measured in an ill-conditioned coordinate (finding 2)

`S(K) = Σ_λ t_λ`, `t_λ = y_λ·χ^λ(β_K)·(−1)^{n(λ)}·f^λ`, is **alternating**, so `|S|` can sit far below
the scale of its own summands. Define the **cancellation ratio**

    κ(K) = |S(K)| / Σ_λ|t_λ(K)| ∈ [0,1].

| K | n | #λ | `S` (signed) | `Σ\|t_λ\|` | `κ` | `1/κ` | `max\|t_λ\|/\|S\|` | at λ | `C_knot` |
|---|---|---|---|---|---|---|---|---|---|
| D | 6 | 11 | −0.71744534 | 2.4646 | 0.29110 | 3.44 | 1.77 | (5,1) | 6.0679 |
| T | 9 | 30 | −2.4751404 | 5.9823 | 0.41374 | 2.42 | 1.51 | (6,3) | 6.7061 |
| ³He | 9 | 30 | −3.0789913 | 10.459 | 0.29438 | 3.40 | 1.91 | (6,3) | 4.9054 |
| ⁴He | 12 | 77 | **−0.19093767** | 24.003 | **0.0079548** | **125.71** | **52.05** | (8,4) | 290.007 |

`κ` is exactly the reciprocal condition number of `|S|` under per-block **relative** perturbation.
Both halves are proved sorry-free in
[`CKnotCancellationConditioning.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/CKnotCancellationConditioning.lean)
(general `Finset`, no substrate input, no `q₀`, no experimental number):

| lemma | content |
|---|---|
| `perturbed_sum_dist_le` | `‖δ‖_∞ ≤ ε ⇒ \|Σ t(1+δ) − Σ t\| ≤ ε·Σ\|t\|`, i.e. a relative move of up to `ε/κ` |
| `exists_annihilating_perturbation` | **sharp**: `δ_i = −(S/T)·sign(t_i)` has sup-norm exactly `κ` and sends the sum to `0` |
| `he4_cancellation_below_one_percent` | `κ(⁴He) < 1/100` |
| `mirror_pair_well_conditioned` | `κ(T) > 1/4` **and** `κ(³He) > 1/4` |
| `he4_conditioning_regime_differs` | `κ(T), κ(³He) > 25·κ(⁴He)` |

Sharpness is the part that matters. When `κ` is small `C_knot` is not merely *imprecise* — a per-block
relative correction of size `κ` sends `|S|` to zero and `C_knot` to `+∞`, and a slightly larger one
flips the sign of `S`. So `C_knot(⁴He) = 290.007`, sitting at `κ < 1%`, carries essentially no
information about the size of the missing per-block structure, and it is what produces the headline
`59.12×`.

Two corroborations, neither re-derived here:

- [`threerow_4he_completion_probe.py`](../../computations/deltalambda/threerow_4he_completion_probe.py)
  (`qou-prjo`) records `4He_sign_at_qlo = +1`, `4He_sign_at_q0 = −1` for the ℓ(λ)≥3 stratum of the same
  object. A sign change is a zero, hence `κ = 0` somewhere on the physical interval; the small `κ`
  measured here at `q₀` is the full-sum shadow of that crossing.
- Historical: the `96.8%` move of `|S(⁴He)|` under the C→D migration is what a `~24%` per-term
  perturbation *must* do at `1/κ ≈ 126`. The same-sized perturbation moved the well-conditioned
  `T`/`³He` by `34%`/`33%`. **No ⁴He-specific mechanism is needed to explain the outlier.**

### 2a. The well-posed coordinate — and exactly how far it can be pushed

`δ_min^∞(K) = |B_AME(K)/m_e − S(K)| / Σ_λ|t_λ|` is the **minimum sup-norm relative per-block
correction** `{δ_λ}` for which `Σ_λ t_λ(1+δ_λ)` reaches the experimental target.

| K | `δ_min^∞` | `δ_min^2` |
|---|---|---|
| D | 1.4753 | 2.4354 |
| T | 2.3609 | 3.5645 |
| ³He | 1.1497 | 1.8365 |
| ⁴He | 2.2990 | 4.1690 |

`spread(δ_min^∞) = 2.05×` against `spread(C_knot) = 59.12×`.

**Three caveats, all of which cut against reading too much into the 2.05×:**

1. **It does not rescue universality, and "coordinate artifact" cuts both ways.** If the `59.12×` is a
   coordinate artifact then so was the `2.83×` the earlier audit called non-universal. Neither number
   should be read as *the* variation of the per-knot deficit. The per-knot non-universality itself
   stands — it rests on the mirror pair (§2b), not on either spread figure.
2. **`δ_min` is a LOWER BOUND, and a loose one.** It is attained by a perturbation pointing exactly
   along `sgn(t_λ)` — maximally efficient, and free to differ arbitrarily between isotopes. A physical
   `Δ_λ` constrained to be *the same function of λ* across isotopes must be larger. Equal `δ_min` does
   **not** mean equal correction **direction**, so `2.05×` is not evidence that the four isotopes want
   the same correction.
3. **No A-trend should be read off four points.** `1.475 / 2.361 / 1.150 / 2.299` for `A = 2/3/3/4` is
   not monotone and is a lower bound, not a measurement.

What survives all three: **the missing per-block magnitude is an order-unity relative correction to
each block term, uniformly across the four isotopes.** "Derive `C_knot ≈ 6`" and "derive
`C_knot ≈ 290`" are the same size of problem in per-block coordinates. Reading `59.12×` as "⁴He is
qualitatively harder" is reading a coordinate artifact.

### 2b. What is deliberately NOT weakened

`mirror_pair_well_conditioned` is the defensive lemma. The scope-(b) exclusion
`CKnotNonUniversal.no_level_only_closure` uses exactly the `T`/`³He` pair, and **both** of those points
sit at `κ > 1/4` — within a factor 4 of a perfectly conditioned sum. The ill-conditioning is localised
on `⁴He`; the mirror exclusion is untouched, and so is `no_writhe_only_framing`, whose D/T leg is also
well conditioned.

## 3. The named "surviving direction" is already closed (finding 3)

`qou-3q7t` and the 2026-08-02 audit both end by naming the per-vertex seminormal eigenphase / q-Reeb
`Δθ_λ` (E₀-options Candidate #1) as "the one non-circular opening", closing only *differences* to date.
**That is superseded.** [`qreeb_eigenphase_compactness_probe.py`](../../computations/deltalambda/qreeb_eigenphase_compactness_probe.py)
(`qou-0g4z`, audit [`2026-08-02-qreeb-eigenphase-compactness.md`](2026-08-02-qreeb-eigenphase-compactness.md),
0-fit, `reads_B_AME: false`) measured `|χ_λ/f^λ|` block by block and found:

> In **every** binding knot the only block with `|χ/d| > 1` is the **trivial 1-dimensional
> representation** `(n)` — dim `1`, character `q^w`, a pure writhe scaling with no mixing and hence no
> rotation angle at all. **Every** genuinely-rotational block (dim ≥ 2, where `θ_λ = arccos(χ_λ/f^λ)`
> is defined) is compact. The eigenphase content is therefore bounded, and the sole unbounded channel
> is `q^w`, which is already a summand of the master formula.

So the difference-only behaviour has a **structural reason** — boundedness — not merely a failed
search: a bounded channel cannot supply an unbounded absolute scale. That is scope-(a) for the
eigenphase construction (the cited fact is a *measurement* of compactness across D/T/³He plus
`QReebEigenphaseCompact.no_rotation_angle_of_boost`, not a proof for all knots), and it does not
exclude the magnitude in general.

**One thing this audit adds to that.** The blocks that actually dominate the master sum are the
**compact** ones, in every isotope: `max|t_λ|` sits at `(5,1)`, `(6,3)`, `(6,3)`, `(8,4)` — all
two-row, all dim ≥ 2, never the trivial rep. So the near-cancellation of §2 is a compact-block
phenomenon, and the one unbounded channel contributes a minority share. The two results therefore
point the same way rather than merely coexisting: the sum is dominated by exactly the blocks the
compactness argument bounds.

**Scope note.** `qou-0g4z` covers D, T, ³He. ⁴He was falsified separately —
[`2026-06-24-he4-qreeb-phase-falsification.md`](2026-06-24-he4-qreeb-phase-falsification.md).

## 4. What is actually left, and what additional structure would be needed

- **The value is proved; the magnitude is not.** `Δ_λ = (−1)^{n(λ)}·dim V_λ` is sorry-free general-n
  (`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`). Nothing here touches it. What is open is
  the many-body binding **magnitude**.
- **Per-block weights are excluded as a class, and this audit is consistent with that.** Six ansätze
  failed; AGENTS.md records the structural reason — no per-block weight converts an intensive quantity
  into an extensive one (pairwise cap `QOU.MassTheory.exchangeDet_pow_two_le_four`). §2a's measurement
  agrees: the required correction is order-unity, i.e. **not** a refinement of the existing block
  weights but a comparably-sized separate object.
- **The eigenphase opening is closed for absolute magnitude** (§3), on boundedness grounds.
- **So the honest remaining shape** is the one AGENTS.md already names and this audit does not improve
  on: a separate, super-pairwise, **additive extensive** term. Two things would move it, neither
  attempted here — (i) the GAP-A-1 route (fix the binding operator `K(𝔥) ∈ H_{3A}(q₀)` by substrate-only
  SDP and read its block content directly, bypassing any `χ^λ → M_λ` rule; E₀-options Candidate #2,
  multi-week), or (ii) an absolute per-block energy normalization, which is a **new substrate axiom** —
  the E₀-options audit already flags that if every candidate collapses to difference-only, Subgoal-1 is
  unreachable without one. Finding 3 is one more collapse of exactly that kind.
- **A methodological consequence.** Any future cross-isotope diagnostic on this axis should report `κ`
  alongside the ratio. A spread computed across points of wildly differing `κ` compares one
  ill-conditioned measurement against three well-conditioned ones, and the resulting number is not a
  property of the physics.

## 5. Anti-fit ledger

| statement | status |
|---|---|
| recorded `C_knot` figures are convention-C; convention-D values differ | **measured, 0-fit** (committed witness) |
| `κ(⁴He) < 1/100`; `max\|t_λ\| = 52×\|S\|` | **measured, 0-fit** + **Lean sorry-free** |
| `1/κ` is the condition number; the bound is sharp | **Lean sorry-free**, general `Finset` |
| mirror pair well conditioned (`κ > 1/4`), exclusion untouched | **Lean sorry-free** |
| dominant block is compact (dim ≥ 2) in all four isotopes | **measured, 0-fit** |
| eigenphase route bounded ⇒ difference-only | **prior result** (`qou-0g4z`), cited not re-derived |
| `δ_min^∞` order-unity, spread `2.05×` | **measured**; a LOWER BOUND, explicitly not a derived `Δ_λ` |
| per-knot Δ_λ **magnitude** | **OPEN** (`qou-3q7t`) |

`y_λ` recomputed from the Wenzl closed form (`Σ y_λ f^λ = 1` asserted); `χ^λ` from the committed
interface-inclusive Rust Hoefsmit caches; convention **D**, **experimental proton pin**
(`q_parameter.Q`), no layer straddle; exact mpmath at 50 dps, no `float` anywhere in the arithmetic.
`B_AME` enters **only** through the diagnostic ratios `C_knot` and `δ_min` and is **never inverted
into a canonical weight** (owner directive: *"Δ_λ from inverted CODATA = NOT ALLOWED"*).
`free_parameters = 0`; `audit_only`; **nothing wired**. No ansatz for the magnitude is proposed here —
`κ` and `δ_min` are diagnostics of the *existing* formula, so there is no seventh ansatz.

**Refs:** producer
[`c_knot_cancellation_conditioning_probe.py`](../../computations/deltalambda/c_knot_cancellation_conditioning_probe.py)
+ witness; Lean
[`CKnotCancellationConditioning.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/CKnotCancellationConditioning.lean);
companions `qou-4jut` (convention refresh), `qou-prjo` (⁴He sign crossing), `qou-0g4z` (eigenphase
compactness).
