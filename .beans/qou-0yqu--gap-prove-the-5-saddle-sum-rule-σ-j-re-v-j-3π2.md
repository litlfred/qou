---
# qou-0yqu
title: 'GAP: prove the 5₂ saddle sum rule Σ_j Re V_j = -3π²/2'
status: todo
type: task
created_at: 2026-08-03T14:28:26Z
updated_at: 2026-08-03T14:28:26Z
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
`uploads/2304.12545v1.pdf`, `uploads/fulltext.pdf`; commit `3a551a05`).

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
