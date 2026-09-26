---
# qou-0yqu
title: 'GAP: prove the 5₂ saddle sum rule Σ_j Re V_j = -3π²/2'
status: in-progress
type: feature
priority: normal
created_at: 2026-08-03T14:28:26Z
updated_at: 2026-09-26T11:07:04Z
---


## What is open

The three 5₂ saddle values satisfy

    Σⱼ Re(Vⱼ) = −3π²/2        (SUM)

with `Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²`, `yⱼ` the roots of `y³−2y²+3y−1`,
`b = (−1,+1,+1)`. **Verified to 80 dps (residual 3.4e-80). NOT PROVED.**

Equivalently `V₃ = −2·Re(V₁) − 3π²/2`, and in `V^ext = V + π²/2` it reads
`Σⱼ Vⱼ^ext = 0` — i.e. `π²/2` is the unique *centering* shift, which is why
that convention exists at all.

## Why it matters

It is what makes the corpus's `V₃` literal unnecessary: `V₃` is determined by
`V₁`. Carrying it independently is how a wrong value (`−2.7580990292`) went
unnoticed for months.

## Established, do not redo

- **Specific to 5₂**, not branch bookkeeping: five control cubics of the same
  shape — four sharing the `Πy = 1` constraint — miss the target by 0.16 to
  2.83 while 5₂ hits to 2e-50. So it is an arithmetic property of the 5₂
  saddle cubic (Bloch-group / dilogarithm-ladder shaped).
- **Branch data is exact**: `2 log yⱼ − 3 log(1−yⱼ) = 2πi·εⱼ` with
  `ε = (+1,−1,0)`. This is where the `π²` comes from.
- **One relation is derived** (and Lean-proved, see below). Summing the
  reflection identity over the roots:

      A + B = π²/2 − (2/3)·Σ(log yⱼ)² + (2πi/3)·Σ εⱼ log yⱼ

  with `A = ΣLi₂(yⱼ)`, `B = ΣLi₂(1−yⱼ)`.

## Why it does not close

One equation, two unknowns. `A ≈ 0.9717306815`, `B ≈ 0.3514640301`, neither
with an evident closed form (`B/A = 0.36169`, `B−A = −0.62027`).

## Next honest step

The Kubert/distribution relation `Li₂(zⁿ) = n·Σ_{k<n} Li₂(ζₙᵏ z)` applied to
`Li₂(y²) = Li₂((1−y)³)` supplies the second relation, at the cost of
cube-root-of-unity arguments `ω(1−y)`. Bloch-group computation; not attempted.

## Lean status

`QOU/QBeta/FiveTwoSaddleSumRule.lean` (lean-direct exit 0, sorry-free) proves
the algebraic skeleton, the reflection reduction (with `Li` abstract, the
reflection identity as an explicit hypothesis), and the two bookkeeping
consequences.

**CORRECTION 2026-08-03.** An earlier version of this bean said only "Mathlib
has no polylogarithm". True (no `Polylog`, no `dilog`) but misleading: **QOU
has its own** — `QOU.Archimedean.LiTwo : ℝ → ℝ` with `LiTwo_reflection'`
**proved sorry-free** on `0 < x < 1`, plus the derivative infra Mathlib lacks.
That is exactly the hypothesis shape `sum_reflection_of_branch` takes, so the
abstract `Li` is instantiable today for the real root `y₃ = 0.4301597…`. It is
NOT instantiable for `y₁, y₂` (complex, `|y₁| = 1.52 > 1`) — that is the real
Lean blocker, tracked as bean `qou-ph1k` (complex `Li₂` + complex reflection). It is recorded as the content-bearing conjecture carrier
`FiveTwoSaddleSumRule` with **no instance**, and the missing input as
`FiveTwoDilogLadder`.

Formalizing the Kubert relation needs a Mathlib dilogarithm first — that is
the real blocker on the Lean side.

## Refs

- probe: `computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`
- ledger: `docs/coordination/1ppq-qbeta.md`, 2026-08-02 row
- PR #4624

## Proof attempt 2026-08-06 — NOT CLOSED. Four routes tried; results below.

### The sum rule reduces EXACTLY to one dilogarithm evaluation

Verified to 51 digits (residual 2.7e-51):

    Σⱼ Li₂(yⱼ)  =  (2·Re e₂(L) − π²/2) / 3          where Lⱼ = log yⱼ + bⱼπi

Derivation: `Σ Lⱼ = πi` (branch data) gives `Σ Lⱼ² = −π² − 2·e₂(L)`, and
substituting into (SUM) leaves exactly this. **So (SUM) is neither more nor
less than a closed-form evaluation of `A = Σ Li₂(yⱼ)`** — a dilogarithm
*ladder* at the roots of the 5₂ cubic. That is the whole problem, stated
minimally.

### Route 1 — Euler reflection: EXHAUSTED, gives no constraint on A

Summing reflection over the roots gives `A + B = π²/2 − Σ log yⱼ log(1−yⱼ)`
with `B = Σ Li₂(1−yⱼ)`. But reflection *is* the definition of `B` in terms of
`A`, so it merely eliminates `B`; it places **no** constraint on `A`.
Re-applying it to the `u = 1−y` roots returns the identical equation (since
`1−u = y`). Reflection is spent. The Lean `sum_reflection_of_branch` is this
step and cannot be pushed further.

### Route 2 — Bloch–Wigner / torsion: REFUTED as the mechanism

`Σⱼ D(yⱼ) = 0` exactly (D = Bloch–Wigner). Tempting: vanishing D suggests the
Bloch-group element is torsion, which would force `Σ L` into `(π²/6)·ℚ`.

**But it is automatic, not 5₂-specific.** `D(z̄) = −D(z)` and `D` vanishes on
reals in `(0,1)`, so *any* cubic with one real and two conjugate roots gives
`Σ D = 0`. Verified on both control cubics — both give exactly `0`. So D-
vanishing carries no 5₂ information and does **not** explain (SUM).
(Separately, `Σ Rogers L(yⱼ)/(π²/6) = 1.6885…`, not an evident rational, so
the naive torsion criterion does not apply cleanly either.)

### Route 3 — Landen: adds an unknown

`z = y/(y−1)` maps the roots exactly onto the roots of `z³ − z² + 1` (residual
0.0 at all three; `z² = 1−y` follows from `y² = (1−y)³`). Landen then relates
`A` to `Σ Li₂(zⱼ)` over a **different** algebraic set — one new unknown for one
new equation. Does not close.

### Route 4 — Kubert/distribution: CORRECTION, adds MORE unknowns than relations

An earlier revision of this bean (and of
`qbeta_5two_saddle_sum_rule_and_provenance_probe.py`) named this "the
identified route". **That was too optimistic.** Applying
`Li₂(zⁿ) = n·Σ_{k<n} Li₂(ζₙᵏ z)` to `Li₂(y²) = Li₂((1−y)³)` gives

    2[Li₂(y) + Li₂(−y)] = 3[Li₂(1−y) + Li₂(ω(1−y)) + Li₂(ω²(1−y))]

which introduces `Li₂` at `−yⱼ` and at `ω^k(1−yⱼ)` — **six** new unknown sums
for **one** new relation. It is a valid identity but nets negative. Do not
start here expecting it to close.

### Where that leaves it

(SUM) is a genuine dilogarithm-ladder evaluation at algebraic points, not
reachable by shuffling the standard transformations. Closing it needs real
Bloch-group / K-theory machinery over the 5₂ trace field, or a specific ladder
identity for this field. Still **verified to 80 dps, unproved**.

Lean status unchanged: the algebraic skeleton and the reflection reduction are
sorry-free; `hrefl` remains undischarged at the complex roots pending
`qou-gkco`. Nothing was stubbed to fake progress.

## Route 5 (2026-08-06) — RESTATEMENT: the dilogarithms cancel. START HERE.

Not a proof. But it changes what has to be proved, and it **bypasses the
complex-`Li₂` blocker** (`qou-gkco`) for this purpose.

### The chain

1. The power sums `pₙ = Σⱼ yⱼⁿ` are **integers** — `3, 2, −2, −7, −6, 7, 25,
   23, −22, …` — obeying the cubic's recurrence `pₙ = 2pₙ₋₁ − 3pₙ₋₂ + pₙ₋₃`.
2. Hence `∏ⱼ(1 − yⱼ z) = 1 − 2z + 3z² − z³` and `Σₙ pₙzⁿ/n = −log(1−2z+3z²−z³)`.
3. Therefore, exactly (residual `0.0`):

       A = Σⱼ Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³) / z  dz

   The integrand is **regular on [0,1]** — the cubic has no root there (min
   `0.615`, both endpoints `1`) — so this converges even though `|y₁| = 1.52`
   makes the defining series diverge. That divergence was the whole reason the
   complex continuation looked necessary.
4. With `y₁y₂y₃ = 1` (so `log r = −½ log y₃`) and `y₁+y₂ = 2−y₃`, the angle is
   `θ = arccos((2−y₃)√y₃/2)` and `Re e₂(L) = −3log²r + (θ−π)²`.

### The sum rule, with no dilogarithm and no complex numbers

    −∫₀¹ log(1−2z+3z²−z³)/z dz
        =  −½·log²(y₃) + (2/3)·(θ−π)² − π²/6,
      θ = arccos( (2−y₃)·√y₃ / 2 ),   y₃ = 0.430159709… the real root

Verified to `1.1e-40`. **Control**: the same expression on `y³−y²+2y−1` fails
by `0.15`, so it is specific to this cubic, not an identity of the shape.

### What this buys

* **The Lean route no longer goes through `qou-gkco`.** No complex `Li₂`, no
  analytic continuation, no branch cuts — only `intervalIntegral`, `Real.log`,
  `Real.arccos`, all in Mathlib. QOU precedent for the integral style:
  `LiTwo_eq_integral`, `integral_zero_one_eq_LiTwo` (both sorry-free).
* **It is checkable by a referee** without Bloch-group machinery.

### What it does NOT buy

It is *equivalent* to the ladder, not a solution to it — a closed-form
evaluation of this integral is itself substantial. Routes 1–4 above remain
dead. Still **verified, unproved**.

### Suggested next step

Attack the integral directly: `∫₀¹ log P(z)/z dz` for `P` an integer cubic
with no root in `[0,1]`. Either a parametrised-family/differentiation
argument, or recognise it as a known ladder for this field. Do **not** expand
`log P = Σ log(1−yⱼz)` — that just returns `−Σ Li₂(yⱼ)` and is circular.

## 2026-08-07 — THE FIELD IS disc −23. Literature target, with a caveat.

**`y³ − 2y² + 3y − 1` has discriminant `−23`** (sympy; irreducible over ℚ). So
do its reciprocal `1−2z+3z²−z³` and its Landen image `z³−z²+1` — same field, as
expected since they are related by rational maps.

`−23` is the **smallest |discriminant| among complex cubic fields**, and it is
*the* classical worked example in the dilogarithm-ladder / Zagier-conjecture
literature. This is no longer a search for an unknown identity in an unknown
field; it is a lookup in a well-trodden one.

### Where to look

- Zagier, *The Dilogarithm Function* (Bonn lecture notes) —
  https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf
- Zagier, *Polylogarithms, Dedekind Zeta Functions and the Algebraic K-Theory
  of Fields* — https://link.springer.com/content/pdf/10.1007/978-1-4612-0457-2_19.pdf
- Zagier–Gangl, *Classical and Elliptic Polylogarithms and Special Values of
  L-Series* — https://people.mpim-bonn.mpg.de/zagier/files/mpim/00-9/fulltext.pdf
- Broadhurst, *Determinations of rational Dedekind-zeta invariants of
  hyperbolic manifolds and Feynman knots and links* — https://arxiv.org/pdf/hep-th/9811173
- Neumann survey (Bloch group / CS) — https://arxiv.org/pdf/2304.12545
- Browkin–Gangl on `K₂ O_F` for this field (cited in the above).

### ⚠ THE CAVEAT — do not assume the classical results apply directly

The classical `−23` results evaluate **`ζ_F(2)` via the Bloch–Wigner `D`**,
i.e. the **imaginary / volume** side. **Our sum rule is the REAL part.**

That distinction is sharp here: `Σⱼ D(yⱼ) = 0` *automatically* for this shape
(Route 2 above — verified on control cubics too), so the Bloch–Wigner
invariant carries **no** information about our identity. The real part is the
Chern–Simons / second-regulator side, a different invariant of the same
element.

So the literature is **adjacent, not a drop-in**. The realistic direct sources
are GGM (2012.00062) / GGMW (2111.04763) themselves, which compute precisely
these `Vⱼ`, and Neumann-style CS-invariant work — not the `ζ_F(2)` ladders.

### Status

Still **verified to 80 dps, unproved**. The field identification narrows the
search enormously but did not itself close the proof.

## 2026-08-07 (b) — Broadhurst READ. The volume side is classical; ours is not.

Owner uploaded the non-paywalled sources (`uploads/9811173v1.pdf`,
`uploads/2304.12545v1.pdf`, `uploads/zagier-the-dilogarithm-function.pdf`; commit `3a551a05`).

**Broadhurst hep-th/9811173 eq (73)** states, for the D = −23 field:

    vol(σ₁σ₂³σ₁σ₂⁷) = vol(5₂) = (3/10)·vol(9₄₉) = (7/3)·vol(7₂₂)
                    = 3·Z₂₃,₃ ≈ 2.828122

i.e. `Vol(5₂) = 3·Z₂₃,₃`, three times the volume of the closed Weeks manifold
`m003(−3,1)`. Cross-checked here to **31 digits**:

    Vol(5₂)  = 2.8281220883307831628
    Vol/3    = 0.94270736277692772092
    D(y₁)    = 0.94270736277692772092      (Bloch–Wigner at our root)
    |diff|   = 2.0e-31

So **`D(y₁) = Z₂₃,₃ = Vol(5₂)/3`** — the Bloch–Wigner value at the saddle root
*is* the Dedekind zeta invariant of the field. Our roots are exactly the
classical −23 objects; the identification is not approximate.

### What this settles

**The caveat is now literature-confirmed, not merely inferred.** Broadhurst's
D = −23 result is a statement about **volume** — the Bloch–Wigner / imaginary
side. That is precisely the side Route 2 showed carries **no** information
about our sum rule (`Σⱼ D(yⱼ) = 0` automatically, control cubics included).

Broadhurst says nothing about `Σⱼ Re Vⱼ`. Neither does the ζ_F(2) ladder
literature generally: it computes the volume/regulator, not the
Chern–Simons/second-regulator combination we need.

### Practical consequence

Do **not** spend further effort mining the ζ_F(2) / Dedekind-zeta ladder
literature for this identity — it answers the sibling question. The remaining
realistic sources are **GGM (2012.00062) and GGMW (2111.04763)**, already in
`uploads/`, which compute these `Vⱼ` directly, and Chern–Simons-invariant work
in the Neumann line (`uploads/2304.12545v1.pdf`, not yet mined).

Still **verified to 80 dps, unproved.**

## 2026-08-07 — Route 5 gains a real Lean spine (4 theorems, sorry-free)

Route 5 was a restatement with no formal content behind it. It now has:

| theorem | file | what it buys |
|---|---|---|
| `prod_one_sub_mul_eq` | `QBeta/FiveTwoSumRuleIntegrand` | `∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³` (was already there) |
| `abs_log_recipCubic_le` | same | `\|log P(z)\| ≤ 4z` on `[0,1]` — the `z = 0` singularity is removable |
| `intervalIntegrable_log_recipCubic_div` | same | **the integral converges** — Route 5's RHS is a real number, not a formal expression |
| `LiTwo_eq_integral_unit` | `Archimedean/DilogReflection` | `Li₂(y) = −∫₀¹ log(1−yz)/z dz` — the argument moves from the endpoint into the integrand, which is what lets the product over roots collapse |

All axioms `[propext, Classical.choice, Quot.sound]`.

**Why this is the interesting direction.** The complex-continuation route
(`qou-gkco`) hits a hard wall at `|y₁| = 1.52`: `cLiTwo` is junk-valued outside
the closed disc, so the inversion formula is not even *stateable* for it
without redefining `Li₂` by an integral on `ℂ ∖ [1,∞)`. Route 5 sidesteps that
entirely for the **sum**: `∏ⱼ(1 − yⱼz)` is a *real* polynomial *positive on
`[0,1]`*, so `Σⱼ Li₂(yⱼ)` is one convergent real integral and no complex root
ever appears.

**The remaining gap, stated precisely.** Three things, in increasing size:

1. `Σⱼ Li₂(yⱼ) = −∫₀¹ log P(z)/z dz`. `LiTwo_eq_integral_unit` gives the `y₃`
   term; the other two need the complex `Log`. ~~The branch data `b` is the
   `2πik` correction in `log ∏ = Σ log`.~~ **REFUTED same day — see the
   correction section below.**
2. The closed-form evaluation of `−∫₀¹ log P(z)/z dz`, i.e. the sum rule.
3. Nothing here weakens the standing status: **verified to 80 dps, unproved.**
   Routes 1–4 remain dead.

## 2026-08-07 (later) — CORRECTION + what `b` actually is

Probe [`qbeta_5two_route5_branch_data_probe.py`](../computations/probes/qbeta_5two_route5_branch_data_probe.py),
witness `computations/qbeta-5two-route5-branch-data.witness.json`, 60 dps.

**Struck above (G1/G3).** My claim earlier today that `b = (−1,+1,+1)` is the
`2πik` correction in `log ∏ = Σ log` is **wrong**: G1 finds that correction is
*identically zero* (worst deviation `3.1e-61` over 40 sample points, `k = {0}`).
The conjugate pair's arguments cancel and the real root contributes a positive
real, so every principal branch is already correct. Struck rather than deleted.

**What `b` actually is (G6, exact — error `0.0`):**

> **`log yⱼ + bⱼπi = Log(−yⱼ)`, the principal branch.**

`b` is not free data and not fitted. `arg(−y) = arg y − π` in the upper
half-plane, `arg y + π` in the lower, and `= π` for positive real `y` — which
forces `(−1, +1, +1)` with **zero** remaining freedom. So

    Vⱼ = 3·Li₂(yⱼ) + Log(−yⱼ)²

and `Log(−z)²` is exactly the object appearing in the dilogarithm **inversion**
formula `Li₂(z) + Li₂(1/z) = −π²/6 − ½Log(−z)²`.

**New exact restatement (G7 + G8).** Applying inversion per root and taking real
parts, the sum rule becomes

    Σⱼ Re Li₂(yⱼ) − 2·Σⱼ Re Li₂(1/yⱼ) = −π²/2

verified to 25 digits (`0.9717306814686482591277742 − 2×2.95326644100666378427251
= −4.934802200544679309417245 = −π²/2`, difference `0.0`).

The per-root inversion rewrite fails as a *complex* identity at `y₃` (that form
needs `z ∉ [0,1]`, and `y₃ = 0.4302`), **but G8 shows the entire defect is
imaginary**: `Re Dⱼ = 0` for every root separately, with
`Im D₃ = −10.6009742…`. The sum rule uses only real parts, so the rewrite is
*derived*, not merely observed.

**Consequence for the Lean route.** What a proof needs is the **real part** of
the inversion formula on `(0,1)` — strictly weaker, and more tractable, than
the complex identity that genuinely fails there.

**Caution — the reciprocal side is not free.** `∏ⱼ(1 − z/yⱼ) = 1 − 3z + 2z² − z³`
*changes sign* on `[0,1]` (it is `−1` at `z = 1`, because `1/y₃ = 2.325 > 1`).
So the positivity argument that makes the root side a clean real integral does
**not** transfer to the reciprocal side. That sign change is where genuine
branch structure lives, and it is the honest location of the remaining
difficulty.

**Status unchanged: verified to 80 dps, unproved.** Nothing above is a proof.

## 2026-08-07 (evening) — the gap is now ONE statement

Everything else in the chain is Lean-proved, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`. Reading the sum rule as
`Σⱼ Re Vⱼ = 3·Σⱼ Re Li₂(yⱼ) + Σⱼ Re Log(−yⱼ)²`:

| piece | status | where |
|---|---|---|
| `b` is `Log(−yⱼ)`, not fitted | **proved** | `branch_shift_eq_log_neg` |
| `Σⱼ Re Log(−yⱼ)² = (3/2)log²y₃ − 2(θ−π)² − π²` | **proved** | `sum_re_log_neg_sq` |
| `∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³` | **proved** | `prod_one_sub_mul_eq` |
| `Σⱼ Re Log(1 − yⱼz) = log P(z)` on `[0,1]` | **proved** | `sum_re_log_one_sub_eq_log_recipCubic` |
| `−∫₀¹ log P(z)/z dz` converges | **proved** | `intervalIntegrable_log_recipCubic_div` |
| `Li₂(y) = −∫₀¹ log(1 − yz)/z dz`, **real** `y ∈ (0,1)` | **proved** | `LiTwo_eq_integral_unit` |
| **`Li₂(y) = −∫₀¹ Log(1 − yz)/z dz`, complex `y ∉ [1,∞)`** | **OPEN** | — |

**That last row is the whole gap.** Everything above it composes: with it, the
sum rule and Route 5's closed form
`A = −π²/6 − ½log²y₃ + (2/3)(θ−π)²` are equivalent, and the `Log²` half is
already evaluated, so the sum rule reduces to evaluating one real integral of a
cubic's logarithm.

### Why that row is the right thing to attack

For `|y| > 1` the integral **is** the analytic continuation: it converges for
every `y ∉ [1,∞)` regardless of `|y|`, unlike the series. So proving it both
defines `Li₂` past `|z| = 1` (which `qou-gkco` needs for `y₁`, `|y₁| = 1.52`)
and closes this bean. One brick, two gaps.

### Two routes, both non-trivial — neither started

1. **Termwise integration.** `−Log(1−w) = Σₙ wⁿ/n`
   (`Complex.hasSum_taylorSeries_neg_log`, `‖w‖ < 1`), so
   `−Log(1−yz)/z = Σₙ yⁿzⁿ⁻¹/n` and `∫₀¹ zⁿ⁻¹dz = 1/n` gives `Σₙ yⁿ/n²`.
   Needs a sum/integral swap. Establishes the disc case only; `|y| > 1` then
   needs a separate continuation argument.
2. **Identity theorem in `y`.** `cLiTwo` is already proved analytic on the unit
   ball (`cLiTwo_analyticOnNhd`), and the real case is already proved on
   `(0,1)` (`LiTwo_eq_integral_unit`), so the real segment is again an
   accumulation set — the same shape that worked for `cLiTwo_reflection`. The
   missing input is **analyticity of the right-hand side in the parameter `y`**,
   i.e. differentiation under the integral sign.

Route 2 reuses machinery already built on this branch and is probably shorter,
but its one missing input is not a Mathlib one-liner. **Not started; not
stubbed.**

**Status unchanged: verified to 80 dps, unproved.**

## 2026-08-07 (late) — the integral representation is proved on the disc

`QOU.MathlibExt.cLiTwo_eq_intervalIntegral`, sorry-free:

    Li₂(y) = −∫₀¹ log(1 − yz)/z dz      for ‖y‖ < 1

by termwise integration
(`intervalIntegral.hasSum_integral_of_dominated_convergence`, geometric bound
`‖y‖^(k+1)`). The indexing needed no reindexing: the `k`-th term
`y^(k+1)z^k/(k+1)` integrates to `y^(k+1)/(k+1)²`, which *is* the `k`-th term
of `cLiTwo`'s defining series, so the two `HasSum`s match on the nose.

Past the disc, `cLiTwoExt y := −∫₀¹ log(1 − yz)/z dz` is now defined and proved
to agree with `cLiTwo` on the disc (`cLiTwoExt_eq_cLiTwo`).

### ⚠ What this does NOT do — read before celebrating

**The sum rule is no closer to being proved.** Route 5 is a *restatement*, and
every brick so far makes the restatement rigorous rather than proving anything
about the number. Even with the whole chain closed, what one gets is

    Σⱼ Re Vⱼ = −3π²/2   ⟺   −∫₀¹ log P(z)/z dz = −π²/6 − ½log²y₃ + (2/3)(θ−π)²

and the right-hand side is an unevaluated real integral. **Evaluating it in
closed form is exactly as hard as it was this morning.** What the bricks bought
is real but narrower: the restatement is now a theorem rather than a numerical
observation, and `b` is demystified.

### Two links still open (neither started, nothing stubbed)

1. **`cLiTwoExt` is analytic on `ℂ ∖ [1,∞)`.** Without it, "continuation" is a
   name, not a theorem, and `cLiTwoExt(y₁)` is not yet *identified* with the
   `Li₂(y₁)` the sum rule refers to. Needs differentiation under the integral
   sign.
2. **Integrability of `z ↦ Re log(1 − yⱼz)/z` on `[0,1]`, per root.** Needed to
   split `Σⱼ Re cLiTwoExt(yⱼ)` into three integrals before applying the
   pointwise identity `sum_re_log_one_sub_eq_log_recipCubic`. Should follow the
   shape of `abs_log_recipCubic_le` — a `|log‖1 − yz‖| ≤ Cz` bound — but with
   case analysis on a general complex `y`.

**Status unchanged: verified to 80 dps, unproved.**

## 2026-08-07 (night) — Route 6 tried and REFUTED (scope-a): Zagier's enhanced dilogarithm

Owner supplied Zagier, *The Dilogarithm Function* (2007) as
`uploads/zagier-the-dilogarithm-function.pdf`. §II.1 B defines the **enhanced dilogarithm**

    D̃(ẑ) = Li₂(z) + ½·u·v    on   X̃ = {(u,v) ∈ ℂ² : eᵘ + eᵛ = 1}

with values in `ℂ/(π²/2)ℤ`, defined only on Bloch-group combinations.

**Why it looked right.** `Vⱼ = 3Li₂(yⱼ) + Log(−yⱼ)²` has exactly the
`Li₂ + (log)(log)` shape with branch data; the roots satisfy `2u = 3v + 2πik`
(`k = (1,−1,0)`, G4 of the sibling probe), which collapses `½uv` to `u²/3` plus
a branch term; and the sum rule's value `−3π²/2` is an exact multiple of the
ambiguity `π²/2`. Had it closed, the open problem would have stopped being a
transcendental evaluation and become the **vanishing of a class in
`ℝ/(π²/2)ℤ`** — a rationality statement.

**It does not close.** Probe
[`qbeta_5two_enhanced_dilog_probe.py`](../computations/probes/qbeta_5two_enhanced_dilog_probe.py),
witness `computations/qbeta-5two-enhanced-dilog.witness.json`, 50 dps:

* **G1** — no integer branch offset `(n,m) ∈ [−2,2]²` gives `Vⱼ = 3D̃`. Best
  errors `6.13, 6.13, 9.87`. MISS.
* **G4** — but the residual is *exactly* computable, not noise:

      V − 3·D̃ = πi(2b + k)·u − b²π²      (u = Log y, principal branch)

  giving `Re = π·arg(y₁) − π²` for `y₁, y₂` and `−π²` for `y₃`. Verified to
  `3.2e-50`.

* Summing and imposing the sum rule gives the **exact restatement**

      Σⱼ Re D̃(yⱼ) = π²/2 − (2/3)·π·θ,     θ = arg y₁

  verified to `5.3e-51`. **The `π·θ` term is not in `π²ℚ`**, so the sum rule
  does *not* reduce to a mod-`π²/2` rationality statement under this
  identification.

**SCOPE-(a), explicitly.** This *set-up* does not close. It does **not** exclude
an enhanced-dilogarithm formulation at a different covering point, or on a
different Bloch element — I have no invariant that forbids one, so no
scope-(b) claim is made. Note the relevant subtlety is already Lean-proved on
this branch: `d[yⱼ]` is **3-torsion**, not zero
(`QOU.QBeta.Bloch.three_smul_wedge_eq_zero`), so `Σⱼ[yⱼ]` lies in the Bloch
group only after tripling — exactly the "2- and 3-torsion issues" the
Garoufalidis–Zagier survey flags. A formulation that tracks that carefully is
the obvious next thing to try.

**Route count is now 6 tried, 6 not closing. Status unchanged: verified to
80 dps, unproved.**

## 2026-08-07T15:12Z — TAKEOVER of the stalled PR #4658. Claimed, nothing new proved.

Bean was still `status: todo` while PR #4658 (branch
`claude/fivetwo-disc-23-lit-2026-08-07`, 39 commits) carried all the work — an
unclaimed-but-active state a sibling could have collided with. Now claimed.

*Verified, not assumed, at takeover:*

* PR #4658 is `mergeable_state: clean` against `main` — the stall is **not** a
  conflict and not a failing gate. There are **zero** check runs on the head
  commit; nothing was ever red.
* The **sorry-free claim holds.** All ten `sorry` tokens across
  `FiveTwoSumRuleIntegrand.lean`, `FiveTwoSaddleSumRule.lean`,
  `ComplexDilogarithm.lean`, `BlochFiveTerm.lean` are inside docstrings
  asserting sorry-freeness; **zero** are `sorry` tactics, and there are no
  `axiom` declarations. Nothing was stubbed to fake progress.

*What did NOT change.* No new mathematics. The sum rule is **verified to 80 dps,
unproved**, exactly as the outgoing agent left it. The two open links are
untouched and unstubbed:

1. `cLiTwoExt` analytic on `ℂ ∖ [1,∞)` — needs differentiation under the
   integral sign. Plumbing: it *identifies* `cLiTwoExt(y₁)` with the sum rule's
   `Li₂(y₁)`, and closes `qou-ph1k`/`qou-gkco` too. One brick, two gaps.
2. **Evaluating `−∫₀¹ log P(z)/z dz` in closed form.** The actual hard part.
   Untouched by all eleven of the outgoing session's theorems.

*One correction carried in from #4666 (merged), which the PR body predates.*
The PR body says the Bloch–Wigner invariant "carries **no** information about
our identity". Over-stated: the *vanishing of the sum* is automatic
(`D(z̄) = −D(z)`, `D` real-vanishing), but the *individual value* is sharp and
5₂-specific — `3·D(y₊) = Vol(5₂)`, agreeing to 20 digits. The cancellation
destroys the information; it does not show there was none. The Route-2
conclusion **for the sum rule** stands unchanged; only the general clause is
wrong. Left as-is in the PR body pending owner steer on which vector to push.

**Route count still 6 tried, 6 not closing.**

### Cross-lane check at takeover — the disc −23 headline is NOT new, and the seam it exposes IS unexplored

Two findings from cross-referencing this bean against the GGM/Stokes lane of
`1ppq-qbeta.md`. Neither closes anything; the first is a correction, the second
is the first genuinely untried vector since Route 6 died.

**1. `disc = −23` was already Lean-proved on `main`, three weeks earlier.**
`QOU/QBeta/FiveTwoSaddleCurve.lean` (81 lines, sorry-free, pre-existing on
`main` — *not* introduced by #4658) contains `u0_cubic_discriminant`: the
discriminant of `y³ − 2y² + 3y − 1` is `−23`. Ledgered 2026-07-18 as part of
the GGM §6.1 5₂ port, where it arises as the `x = 1` reduction of the deformed
saddle curve `x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0`.

PR #4658 presents this as a new finding and this bean never cross-references
the file. The mathematics is right and the literature pointers are worth having;
the novelty framing is wrong. **The two lanes have been working the same cubic
without citing each other.**

**2. The untried vector: the ambiguity group is `ℂ/2π²ℤ`, not `π²/2`.**
The same 2026-07-18 entry records, for *these exact* `Vⱼ`, that **`V` is
`ℂ/2π²ℤ`-valued** — σ3-pair positions being lattice representatives. Route 6
tested Zagier's enhanced dilogarithm `D̃`, valued in `ℂ/(π²/2)ℤ`, and failed on
branch bookkeeping — a **factor-4 different modulus** from the one the corpus
has already established for the objects actually in the sum rule.

Route 6's refutation is scope-(a) and explicitly declines to exclude "a
formulation at a different covering point or Bloch element". The corpus's own
`2π²` lattice is exactly such a candidate and **was never tried** — Route 6
imported Zagier's modulus rather than using the one already documented here.
Note also `−3π²/2 = −(3/4)·2π²`, i.e. the sum-rule target is a *quarter-lattice*
point of that modulus, which is the kind of coincidence that is either the
mechanism or nothing.

**Not attempted, not stubbed, no claim made.** Recording the seam so the next
session starts here rather than re-deriving disc −23 a third time. Route count
unchanged: **6 tried, 6 not closing; status verified to 80 dps, unproved.**

## 2026-08-07 — Route 7 tried and REFUTED (scope-a): branch freedom, not the modulus

Full record in child bean **`qou-r7ml`**. Probe
`computations/probes/qbeta_5two_route7_enhanced_dilog_branch_freedom_probe.py`,
witness `qbeta-5two-route7-enhanced-dilog-branch-freedom.witness.json`, 8 gates,
60 dps, all pass.

**The hypothesis that motivated it was wrong.** The corpus's `ℂ/2π²ℤ` modulus vs
Zagier's `ℂ/(π²/2)ℤ` is **irrelevant** to this setup: the branch shift
contributes `−2π²aⱼbⱼ`, a multiple of both. The quarter-lattice coincidence
`−3π²/2 = −(3/4)·2π²` is not a mechanism. Do not re-run this hunch.

**But it exposed a real defect in Route 6's stated reason.** Route 6's witness
gate G3 evaluated `Σⱼ Re D̃` at the **principal branch only** and never varied the
branch integers *for the sum*. With `u = log y + 2πia`, `v = log(1−y) + 2πib`
there are **two** free integers per root, and the `θ` obstruction cancels iff

    3(b₁ − b₂) + 2(a₁ − a₂) = −2

Route 6's implicit `a = 0` reduces this to `3(b₁−b₂) = −2` — insoluble over `ℤ`,
which is *precisely* why it reported "no integer branch offset matches". With
`a` free it is soluble and **exact rationality IS reachable**. Route 6's
conclusion stands; its reason does not.

**Why the rationality is worthless.** Reachable set is exactly
`Σⱼ Re D̃(yⱼ)/π² ∈ 11/6 + 2ℤ` (derived and brute-forced), and **every control
cubic `y^p = (1−y)^q` lands in its own `π²ℚ` coset too** — including this bean's
named control `y³−y²+2y−1`, which *is* `y³ = (1−y)²`. Generic to the shape, not
5₂ arithmetic: **the Route-2 trap again.** Separately, neither `−1/2` (the
`V = 3·D̃` target) nor `−3/2` lies in the reachable coset.

**Route count now 7 tried, 7 not closing. Status unchanged: verified to 80 dps,
unproved.** Remaining live work is unchanged and untouched by this: `qou-clx8`
(`cLiTwoExt` analytic on `ℂ∖[1,∞)`) and the closed-form evaluation of
`−∫₀¹ log P(z)/z dz`, which is still the actual hard part.

## 2026-08-07 — Route 8: REDUCTION to a 7th-root-of-unity identity. Not a proof.

Full record in child bean **`qou-8v3k`**. Probe
`qbeta_5two_route8_envelope_deformation_cyclotomic_probe.py`, witness
`qbeta-5two-route8-envelope-deformation-cyclotomic.witness.json`, 7 gates, all pass.

**First route that moves in `x` instead of attacking at `x = 1`.**

> `Σⱼ Re Vⱼ = −3π²/2` **⟺** `Σₖ Re[Li₂(yₖ) + 2Li₂(−yₖ) + (log(−yₖ))²] = −π²/2`
> at `yₖ = −1 − 2cos(2πk/7)` — the **totally real cyclotomic field ℚ(ζ₇)⁺**, disc 49.

Mechanism, all elementary and formalizable:

1. `∂V/∂y = 0` **derives** GGM's deformed curve `xy³ −(x²+1)y² +(x²+x+1)y − x = 0`
   (already Lean-proved here as `FiveTwoSaddleCurve.lean`), so the `yⱼ(x)` are
   critical points and the envelope theorem applies.
2. Vieta: `∏ⱼ(1 − xyⱼ) = x` and `∏ⱼ(1 − yⱼ/x) = 1/x`. **This is the collapse.**
3. Envelope ⟹ `d/dx V(x,yⱼ(x)) = (1/x)log[(1−yⱼ/x)/(1−xyⱼ)]`.
4. Sum + (2) ⟹ `S'(x) = −2log x/x` ⟹ **`S(x) = S(1) − log²x`** (verified <1e-30
   on `x ∈ [0.2,5]`). Branch term `2πik log x` is purely imaginary for real
   `x > 0` — cannot touch `Re` — and on `|x|=1` is real and **measured `k = 0`**
   at eight points to `φ = π`. Hence `S(−1) = −3π²/2 + π² = −π²/2`.
5. At `x = −1`: `y³+2y²−y−1`, disc **49**, roots exactly `−1−2cos(2πk/7)`, and
   `xy = y/x = −y`.

**⚠ Does NOT close it.** `S(1)` is the constant of integration; this transports
the unknown rather than evaluating it. The cyclotomic identity is verified
numerically (residual 9.2e-41), not proved.

**Why it is still the best handle found.** Every prior route died on *real part
vs volume side*: at disc −23 the field is complex, `D ≠ 0`, and all classical
ladder results compute `ζ_F(2)` via `D`. At `x = −1` the field is **totally real
and abelian**, so `D ≡ 0` identically and Rogers sums are expected in `π²ℚ` —
Frenkel–Szenes / Y-system / Watson territory, where `−π²/2` is the natural answer.
**The obstruction that killed Routes 2, 6 and 7 is structurally absent there.**

**Route count 8 tried; 7 refuted, 1 reduction. Status: verified to 80 dps,
unproved.**

## 2026-08-07 — Route 9: the sum rule is now a RATIONALITY statement. Bloch torsion at ℚ(ζ₇)⁺.

Full record in child bean **`qou-b7cy`**. Probe
`qbeta_5two_route9_bloch_torsion_rationality_probe.py`, 6 gates, all pass.

**Route 6's stated hope is achieved, by a different mechanism.** Building on
Route 8's transport, put `w = −y = 1 + 2cos(2πk/7)`, a root of
`w³ − 2w² − w + 1`. Then `N(w) = −1`, `N(1−w) = −1`, `N(1+w) = +1` — **all three
are units** — and the ring identity

    (1 − w)²(1 + w) = 1 − w − w² + w³ = w²        [since w³ = 2w² + w − 1]

gives, for `ξ := 2[w] + [−w]`,

    δ(ξ) = w ∧ [(1−w)²(1+w)] = w ∧ w² = 0    in ∧²F* ⊗ ℚ

so **`ξ` lies in the Bloch group `B(F)`, `F = ℚ(ζ₇)⁺`**. `F` is totally real, so
`r₂ = 0` and `B(F) ⊗ ℚ = 0` by Borel: `ξ` is **torsion**, and Rogers `L` carries
Bloch torsion into `π²ℚ`. **The rationality is proved.**

Measured: `Σₖ Re[2L(wₖ) + L(−wₖ)] = π²/2` exactly (26 digits), and
`Σₖ Re V = Σₖ Re L(ξₖ) − π²`, giving `−π²/2` ✓ = Route 8's target = the sum rule.

**Open:** (i) that the rational is exactly `1/2` — verified, not derived (note
`π²/2 = 3·L(1)`); (ii) the `−π²` branch constant — a per-embedding formula
`V − L(ξ) = iπ log[(1−w)/w]` was tried and **is FALSE**, failing at two of three
embeddings; only the sum is exact. Recorded so nobody re-derives it.

The chain is now `sum rule → cyclotomic identity → L(ξ), ξ ∈ B(F) torsion →
π²ℚ → ??? = π²/2`, and **only the last arrow is open — a rational-number
question, not a transcendence question.**

**Route count 9 tried; 7 refuted, 2 reductions. Status: verified to 80 dps,
unproved.**

---

## 2026-08-08 — the cyclotomic side is CLOSED in Lean. Two links remain.

`Σₖ (2·L(wₖ) + L(−wₖ)) = π²/2` is now a **theorem** about the corpus's own
dilogarithm, not a numerical observation:

```lean
QOU/QBeta/FiveTwoAbelFiveTerm.extended_sum
  {x : ℝ} (hx : x^3 - 2x^2 - x + 1 = 0) (hlo : 1/2 < x) (hhi : x < 1) :
    (2*E (1/(1-x)) + E (-(1/(1-x)))) + (2*E x + E (-x))
      + (2*E ((x-1)/x) + E (-((x-1)/x))) = Real.pi^2/2
```

`E = extend (π²/6) rogersL`, the Rogers dilogarithm extended off `[0,1]`.
Sorry-free, `[propext, Classical.choice, Quot.sound]`, `lake build` green,
and `exists_root_in_Ioo` shows the hypothesis is satisfiable.

The chain of Lean files, bottom to top:

| file | content |
|---|---|
| `FiveTwoCyclotomicBloch` | Vieta products, `bloch_key` |
| `FiveTwoRogersReflection` | `rogersL`, reflection, **`hasDerivAt_rogersL`** |
| `FiveTwoRogersExtend` | the extension; inversion + Landen by construction |
| `FiveTwoAbelFiveTerm` | **Abel's five-term relation**, the numerators, the sum |
| `FiveTwoFiveTermArguments` | `hA/hB/hC` are five-term instances, and follow from Abel |
| `FiveTwoLevelSevenLadder` | the `(17,5,−1)` certificate |

Five beans closed by this: `qou-abel`, `qou-rhyp`, `qou-fivt`, and earlier
`qou-r7ml`, `qou-g2wr`.

### What is still missing — and it is NOT the dilogarithm any more

**The 5₂ sum rule is `Σⱼ Re Vⱼ = −3π²/2`. What is proved is `Σₖ (2L(wₖ)+L(−wₖ))
= +π²/2`.** Those are different statements, and the two links between them are
both open:

1. **`qou-trns` — the transport `x = 1 → x = −1`.** The branch integer is pinned
   by the base point; the **envelope theorem is confirmed numerically and not
   formalized**. This is the weakest link and it is analytic, not arithmetic.
2. **`qou-rstq` item 4 — `E` is not identified with `Re` of the analytic Rogers
   `L` in Lean.** Route 15 closed this **on paper** and showed it reduces to
   `Li₂` inversion and `Li₂` Landen; neither is in Mathlib, and the corpus has no
   `Li₂` off `[−1,1]` (`qou-ph1k`, `qou-gkco`, `qou-clx8`).

Link 2 matters more than it looks. `E` is *defined* piecewise, so `extended_sum`
is a theorem about a piecewise function that **provably agrees** with the Rogers
dilogarithm at every point checked and is **not proved to be it**. Anyone
quoting `extended_sum` as "the cyclotomic identity is proved" should say which
of those two they mean.

**Standing status, unchanged: the 5₂ sum rule is verified to 80 dps, unproved.**

---

## ⚠ 2026-08-08 (later) — the transport is OPEN again, and worse than recorded

`qou-trns` sub-gap 1 was marked **closed** ("`k = 0` is PINNED by the base
point"). **It is reopened.** Its step 2 — "the three branches are continuous and
never collide on the arc, `min |disc| = 0.348`" — is false.

**The discriminant vanishes on the arc**, at `θ = 137.9206708879635°`, where two
of the three `y`-branches collide exactly. `min |disc| = 0`. The `0.348` was a
**grid minimum from an ~N=360 scan**, quoted as if it were the true minimum.

Proved without numerics: `disc` is palindromic, `disc(x)/x⁴ = Q(x + 1/x)`,
`Q(u) = u⁴ − 6u³ + 7u² + 6u − 31`, and `Q(−2) = +49 > 0 > Q(−1) = −23` in
integers, so IVT gives a root with `u ∈ [−2,2]` — i.e. a point of `|x| = 1`.
`qbeta_5two_route16_discriminant_vanishes_probe.py`, 6 gates.

### The chain, corrected

| link | status |
|---|---|
| cyclotomic identity `Σₖ(2L(wₖ)+L(−wₖ)) = π²/2` | ✅ **proved in Lean**, sorry-free |
| transport `x = 1 → x = −1` | ❌ **OPEN** — branch point on the arc |
| `extend` ≡ `Re` analytic Rogers `L` in Lean | ❌ open (`qou-rstq` item 4) |

So the arithmetic half is done and **both remaining links are analytic** — one of
them harder than this bean previously recorded.

The likely repair: `Σⱼ Vⱼ` is **symmetric** in the roots, and symmetric functions
stay analytic across a branch point even though the branches do not. Rewriting
the transport symmetrically, or deforming the path off `|x| = 1` around `x₀`,
should recover it. **Neither is written, and neither is assumed.**

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the integral, examined: residues ruled out, and a caution on the disc −23 lead

Route 24, 6 gates, exit 0, 120 dps. Nothing evaluated; the difficulty is located
and one route is closed off.

### What the integral is

    I := −∫₀¹ log P(z)/z dz,   P(z) = 1 − 2z + 3z² − z³ = ∏ⱼ(1 − yⱼz)

    I = 0.97173068146864825912777416993855050011200599…

`P` is the reciprocal of the 5₂ cubic, an integer cubic, positive on `[0,1]`
(min `0.6180…`, at `z = 1`).

### Evaluating it IS the sum rule — derived here, not assumed

This bean states the equivalence; Route 24 G2 derives it independently and
checks it to 120 dps:

    3·Σⱼ Li₂(yⱼ) + Σⱼ Re log²(−yⱼ) = −3π²/2

which is `Σⱼ Re Vⱼ = −3π²/2` at `x = 1`, since `Vⱼ = 3Li₂(yⱼ) + log(−yⱼ)²` there.
So "evaluate the integral" is not a separable subproblem — it is the whole thing.

### The closed form is MINIMAL

PSLQ at 120 dps, with `L = log y₃` and `θ = arg y₁`:

    6·I = 3π² − 3L² + 4θ² − 8πθ

and **no sub-basis of `{π², L², θ²}` supports any relation at all** — all four
terms are needed. The `πL` and `θL` coefficients come out zero, so this is
exactly the `−π²/6 − ½L² + (2/3)(θ−π)²` recorded above.

### ⚠ Residues do not touch it — demonstrated, not argued

This bean warns that expanding `log P = Σ log(1−yⱼz)` is circular. The residue
route is **the same circle traversed the other way**, and G3 runs it to the end:

1. IBP: `I = ∫₀¹ log z · P′(z)/P(z) dz` — rational apart from `log z`.
2. `P′/P` is a **logarithmic derivative with simple roots**, so **every residue
   is exactly 1**. Residues carry only where the roots are; no arithmetic.
3. The transcendence is in `log z`, which is not meromorphic. Its branch cut
   contributes `∫₀¹ log z/(z−r) dz = Li₂(1/r)` at each pole.
4. Summing returns `Σⱼ Li₂(yⱼ) = I`. Circular, to 1e-51.

Worth recording as closed: contour methods relocate this difficulty, they do not
remove it.

### ⚠ CAUTION: the disc −23 literature lead may point at the wrong invariant

This bean says disc −23 is "*the* classical worked example in the
dilogarithm-ladder / Zagier-conjecture literature … a lookup in a well-trodden
one". That machinery computes `ζ_F(2)` via the **Bloch–Wigner** function `D` —
the *imaginary-part* invariant. Two measurements (G5):

* **`Σⱼ D(yⱼ) = 0` automatically here**, because `P` is real: `D(y₃) = 0` and
  `D(ȳ₁) = −D(y₁)`. It carries no information about this problem.
* **`D(y₁) = 0.9427…` is PSLQ-independent** of the whole `{π², L², θ², πθ, θL}`
  basis, while `I` lies *inside* it — and `D` enters the relation for `I` with
  coefficient **0**.

So `D` and `I` are different invariants, and the `ζ_F(2)` route governs the one
this problem does not need. Not a refutation of the literature lead, but it
means "look it up" is under-specified: what would have to be found is a
real-part ladder, not a zeta value.

### Where the attack should go instead

`∏ⱼ yⱼ = 1` **and** `∏ⱼ(1 − yⱼ) = 1`, so `y` and `1−y` are units. A complex
cubic field has unit rank `r₁ + r₂ − 1 = 1`, so `⋀²(O_F^× ⊗ ℚ)` is **zero** and
the wedge obstruction `y ∧ (1−y)` vanishes **identically** — the structural
reason a weight-2 ladder should exist here at all.

That points at explicit **five-term functional equations**, and this branch
already has `rogersL_fiveTerm` as a sorry-free Lean theorem. The level-7 ladder
was found exactly that way. Note the level-7 cubic lives in a *different* field
(disc 49, totally real), so the proved ladder cannot supply this one — but the
method transfers.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later) — the sum rule as ONE trace equal to π²/2

Route 25, 6 gates, exit 0, 120 dps. Following Route 24's own pointer at
five-term equations, this reformulates the target into the shape they act on.
**Nothing is proved.**

### The reformulation

The saddle condition `(1−y)³ = y²` is already Lean (`cubic_iff_sq_eq_cube`), so
`log(1−y) = (2/3)log y + (2πi/3)m` per embedding. Feed that into Rogers `L` and
trace over the three embeddings. At `m = −2`:

    Σ_σ [ Li₂(σy) + ½ log(σy) · log(ω_σ(1 − σy)) ]  =  π²/2

exactly — difference `0.0` at 120 dps, PSLQ `[−2, 1]`, and unique in `m` (the
trace moves by `(2/3)πθ` per step). **One equation where Route 24's `Li₂` form
needed four terms**: `π²`, `L²`, `θ²`, `πθ` all vanish into the trace.

### ⚠ What the object is, and is not

**It is not Rogers `L`.** The principal branch of `log(1−y₁)` has `m = −1`, so
legitimate branches are `m = −1 + 3k` — and `−2` is not of that form. Measured:
at `m = −2`, `exp(lg)/(1−y₁)` is a primitive **cube root of unity**, `arg = −2π/3`.

So this is Rogers `L` with `1−y` twisted by `ω`. The twist is not arbitrary —
solving `(1−y)³ = y²` for `1−y` determines it only up to a cube root of unity,
and the clean value picks one of the three. But it must be named honestly:
*"the Rogers-L trace is π²/2" would be FALSE*. With genuine Rogers `L` the trace
is `π²/2 − (2/3)πθ` (G2) — already a simplification from four terms to two, but
still θ-dependent.

### Why a trace at all — the negative result that forces it

**The identity does not split.** At the real root alone, `L(y₃)` is *not* a
rational multiple of `π²` (PSLQ to coefficient 1e10 at 120 dps finds nothing),
and `Li₂(y₃) ∉ span_ℚ{π², L²}`. So there is no root-by-root ladder; the identity
is irreducibly a sum over embeddings. `L(y₃)/π² = 0.073505600048…`, not a
low-height rational.

### What this does NOT do

G5: expanding the trace in the `{π², L², θ², πθ}` basis returns Route 24's
`6I = 3π² − 3L² + 4θ² − 8πθ` **identically**. It is a repackaging and proves
nothing. Its value is the *shape*: a single trace equal to `π²/2` is what
five-term functional equations produce, and `rogersL_fiveTerm` is already
sorry-free Lean on this branch.

### A coincidence, flagged and not claimed

`π²/2` is exactly the value of the corpus's **proved** level-7 identity
`extended_sum` (`Σₖ(2L(wₖ) + L(−wₖ)) = π²/2`). The fields differ — disc `−23`
here, disc `49` (totally real, cyclotomic) there — so it cannot be the same
identity and the proved one cannot supply this one. Recorded because a shared
constant is worth a look, not because it is evidence.

### Suggested next step

Search for an explicit ℚ-combination of five-term relations whose arguments are
built from the `yⱼ` and that reduces `Σ_σ [yⱼ]` to torsion. That is how the
level-7 numerators `(17, 5, −1)` were found on this branch, and the machinery
is already Lean-proved. The cube-root twist says the search should probably run
in the field `F(ω)`, not `F`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 40 — the distribution (Kubert) family: mapped, and bounded by a rank argument

Probe `computations/probes/qbeta_5two_route40_distribution_factors_probe.py`
(8 gates, all pass, dps 40/50/60). Lean: `FiveTwoSaddleSumRule.lean` §7d —
twelve theorems, sorry-free, `lake build` exit 0, standard axioms only.

### A retraction first — a claim drafted here and never committed

An earlier draft asserted the distribution family is **vacuous** on the Galois
sum: that `Li₂(z^n) = n·Σₖ Li₂(ζᵏz)` summed over the orbit degenerates to
`A = A`, closing Route 4 as a no-go family. **That claim is false.** Two
independent errors produced it, both now gated against:

1. The generating polynomial was built by **reversing** the coefficient list.
   For monic `R` of degree `d`, `∏(1 − Xᵢz) = z^d·R(1/z)` — the highest-first
   list read low-to-high, already in the right order. Reversing computes a
   different polynomial. G1 gates the convention *and* gates that the reversed
   one fails.
2. Granting the change of variables `u = z^n` — which **is** true, `S_n = A/n`,
   G8 — the step "so the relation says `A = A`" assumed `S_n` is one atomic new
   unknown. It is not.

### What is true: the tower is the powers of ONE generator

Let `c` be a root of `X³+X²−1` (`c = 1/ρ`, `ρ` the plastic number `ρ³=ρ+1`),
and `C_m = Σ Li₂(cᵢ^m)` over the three conjugates. Exact integer Newton
identities (G3) give

| power | minimal polynomial | role |
|---|---|---|
| `c¹` | `X³+X²−1` | `C₁` |
| `c²` | `X³−X²+2X−1` = `Q` | **`B = C₂`** |
| `c³` | `X³−2X²+3X−1` = `P` | **`A = C₃`** |
| `c⁵` | `X³−4X²+5X−1` | `C₅`, the reflection (`1−c = c⁵`) |

every discriminant `−23·square` — one cubic field throughout. So the two
sum-rule unknowns are two rungs of a single ladder, not unrelated quantities.

`X⁹−2X⁶+3X³−1` and `X⁶−X⁴+2X²−1` are both **reducible** (G4, exact):
`= (X³+X²−1)(X⁶−X⁵+X⁴−2X³+X²+1)` and `= (X³−X²+1)(X³+X²−1)`; both cubic
factors have discriminant `−23`. That reducibility is exactly what refutes the
retracted reading.

Four relations, all verified numerically (G5 at two precisions, G6):

* `C₂ + C₃ = π²/2 − Σ log y log(1−y)` — reflection at `y = c³`, since `1−c³ = c²`
* `C₁ + C₅ = ` same over the `c`-orbit — reflection at `c`, since `1−c = c⁵`
* `C₂ = 2(C₁ + D)` — duplication, `D = Σ Li₂(−cᵢ)`
* `C₃ = 3(C₁ + E)` — triplication, `E` over the sextic factor

Both reflections close with **principal** logs, no branch correction.

### The no-go, with a proof this time

Six unknowns `(C₁, C₂, C₃, C₅, D, E)`, four relations. The functional reading
off `A = C₃` lies in the row space iff stacking it leaves the rank unchanged.
**It does not: rank 4 → 5** (G7), solution family dimension 2. So distribution
plus reflection over this tower *provably* cannot determine `A`. Unlike the
retracted claim, this is a rank computation over an explicit matrix.

### What this does NOT close

The five-term relation, Landen (Route 3), and any relation using a root **not**
of the form `c^m` are all untouched. This strengthens rather than weakens the
suggested next step above — the five-term search in `F(ω)` — by removing the
distribution family from contention as a way of avoiding it. Note the search
now has a much smaller natural alphabet than "the `yⱼ`": the powers `c^m`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 41 — the five-term ladder search, and why the machinery cannot see `A`

Probe `computations/probes/qbeta_5two_route41_ladder_rank_probe.py` (5 gates,
all pass, dps 40). No Lean; nothing here is provable-and-unproved, it is a
bound on a family plus two corrections.

### Two corrections, both caught by checks rather than by review

1. **The Li₂-form five-term RHS used in the first draft is WRONG.** The
   argument set `[x, y, (1−x)/(1−xy), 1−xy, (1−y)/(1−xy)]` is right — it is the
   Rogers-L pentagon — but the identity is a statement about
   `L(z) = Li₂(z) + ½log z·log(1−z)` summing to `π²/2`, not about `Li₂` plus a
   log product. G1 gates the correct form to 40 dps **and** gates the wrong one
   failing at the same generic real points, by an amount that varies with the
   point. Caught by evaluating off the configuration it was to be used on.
2. **"`Σ_σ D(σx) = 0` is a feature of the disc −23 field" is WRONG — it is
   general.** `D(z̄) = −D(z)`, complex embeddings come in conjugate pairs, real
   embeddings give `D = 0`. True in every number field. The quartic intended as
   a *negative control* refused to be one, and that is what exposed it.

### The result

Over a set `S` of Galois orbits in `K = ℚ(c)` closed under `x ↦ 1−x` and
`x ↦ 1/x`, with **every** Euler-reflection, inversion and pentagon relation
that closes in `S`, the functional reading off `A` is not in the row space:

| `|S|` orbits | relations | rank | rank + target |
|---|---|---|---|
| 82 | 55 | 46 | 47 |
| 168 | 316 | 153 | 154 |

The gap stays exactly 1 as `S` doubles.

**And the reason, which subsumes Routes 1–5 and 40:** the Bloch-Wigner
regulator vanishes identically on a Galois sum. The invariant the whole ladder
/ Bloch-group apparatus computes is *zero here by symmetry*, so it carries no
information about `A`. Those routes were not unlucky; they were the wrong
instrument. Any future attempt that reduces to a Bloch-group computation can be
predicted to fail without running it.

### ⚠ The limit on the rank result — do not quote it without this

The rows are **Bloch-group** statements (relations modulo torsion). Turning one
into a statement about `Σ Li₂` needs the pentagon summed over the three
embeddings to have an elementary right-hand side, and G4 measures that it does
not: at `x = y = c` the sum is `8.3326…` against `3π²/2 = 14.8044…`, a gap of
`6.4718…`. The pentagon's validity region is the real one; the two complex
embeddings carry branch corrections that are **not** accounted for. So the
bound on the family is only as good as that bookkeeping, which is the obvious
next thing to do if this line is picked up again.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 42 — the volume anchor, the structural obstruction, and two corrections

Probe `computations/probes/qbeta_5two_route42_extended_bloch_anchor_probe.py`
(5 gates, all pass, dps 50). Follows Routes 40 and 41.

### The anchor: this is the 5₂ trace field, and the volume sits on these roots

    Vol(5₂) = 3·D(y₁)    y₁ the complex root of y³−2y²+3y−1
    Vol(5₂) = 6·D(c₁)    c₁ the complex root of X³+X²−1  (c = 1/ρ)

with `D` Bloch–Wigner, checked against a **published** volume so it identifies
`y₁` as the tetrahedron shape rather than restating a definition (G1). The
reference constant's ~18 digits, not the identity, bound the gate — and the test
is **relative**, since the inherited deviation scales with the ratio (the same
2.0e-18 shows as 6.0e-18 at 3 and 1.2e-17 at 6; an absolute tolerance passes one
and fails the other for no mathematical reason).

### Why every ladder route failed — measured, replacing "did not close"

`D(y₁)` alone carries the **entire** volume. Summed over the Galois orbit it
cancels **identically**: `y₂ = ȳ₁` with `D(z̄) = −D(z)`, and the real root gives
`D = 0` (G4). `D` is exactly the regulator the ordinary Bloch group computes, so
that whole apparatus evaluates to zero on a Galois-summed dilogarithm and can
carry **no** information about `A`. General, by conjugate symmetry, in every
number field. Routes 1–5, 40 and 41 were not unlucky — they could not have
closed.

And the sum rule lives entirely in what `D` discards (G3):

| | value |
|---|---|
| `Σ Re(Vⱼ)` | `−3π²/2` — the sum rule |
| `Σ Im(Vⱼ)` | `2π·log(y₃)` exactly — elementary |

Both halves elementary; the volume is absent from the Galois sum.

### ⚠ Two corrections, recorded because the wrong values were asserted first

1. **`V_j`'s branch integers are `b = (−1, +1, +1)`** — the **real** root carries
   `+1`, not `0`. Assuming `0` gives `−30.822` against a target of `−14.804`.
2. **`Σ Im(Vⱼ)` is not zero**, it is `2π·log(y₃)`. A scan over `b ∈ {−2..2}³`
   that demanded `Im = 0` therefore **rejected the correct assignment** and
   reported no solution at all. The sum rule is a statement about `Re` only.

Both are gated, including the failing assignment as a negative control.

### What this points at — and it is not another ladder

The `bⱼ` are **flattening data**. The extended Bloch group (Neumann) is built
from flattenings `(log z + p·πi, log(1−z) + q·πi)`, its regulator is the complex
volume `Vol + i·CS` rather than `Vol` alone, and the Rogers dilogarithm is well
defined on it — it retains precisely what `D` throws away. That is where a proof
should be attempted.

**Ordered next steps.**
1. Finish Route 41's gated `G4` branch bookkeeping (pentagon over the three
   embeddings missed `3π²/2` by 6.4718). Cheapest, and prerequisite — until it is
   done Route 41's rank result is a Bloch-group statement, not a `Σ Li₂` one.
2. Redo the computation in `ℬ̂(ℂ)`: show `Σ_σ [y_σ; p_σ, q_σ]` is torsion.
3. Coordinate with sibling **#4824** (`claude/extended-bloch-tetrahedron-wx3mc4`),
   already in extended-Bloch territory.

**Do not retry:** distribution (rank 4→5) or the ordinary five-term/Bloch ladder
over the `c^m` orbits (46→47, 153→154). Anything reducing to an ordinary
Bloch-group computation is blind here for the reason in G4.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
