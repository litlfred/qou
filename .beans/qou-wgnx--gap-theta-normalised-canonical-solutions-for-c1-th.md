---
# qou-wgnx
title: 'GAP: theta-normalised canonical solutions for C1 — the genuine untried route to the Stokes multipliers'
status: in-progress
type: task
priority: high
created_at: 2026-08-07T08:45:09Z
updated_at: 2026-08-07T10:04:33Z
---

Two routes are closed with NEGATIVES (steps 3 and 4): the sector data is
simply not visible in b_m asymptotics. Both tried to shortcut past building
the canonical solutions, and failed for that same underlying reason.

The untried route is the real one: construct the theta-normalised canonical
solutions in the ramified single-slope picture and read the connection
matrix off them directly.

Prerequisites ALREADY IN HAND (both algebraic, both survived):
  - B_1,2 = ±sqrt(q-1)/q from the ramified edge polynomial (bean qou-pw8l)
  - q-Gevrey order = Newton slope = 1/2, cross-checked independently

This is real work, not a refinement of steps 3-4. Level d=2 q-Borel /
theta-kernel resummation (RSZ, Asterisque 355 §3.3).

## 2026-08-07 — canonical solutions BUILT; connection matrix NOT obtained

**Done and solid.**
- Both theta-normalised canonical solutions at ∞ constructed and verified by
  substitution (residual ~1e-62 at 60 dps, z = 50/200/1000).
  `computations/qbeta/c3_w2_c1_theta_canonical.py`
- The theta-normalised series `h` is **entire in 1/z** — `|h_n|^{1/n}` falls
  monotonically to 0.128 by n=80, `h_n ~ T^n p^{-n(n-1)/2}`. So the theta
  normalisation fully absorbs the q-Gevrey divergence, and the ∞-solutions are
  genuinely analytic rather than merely asymptotic. This is what makes a
  numerical connection matrix feasible at all.
- 0-side: indicial `t² + (q−1)t + (q−1) = 0`, discriminant `(q−1)(q−5)`, so a
  conjugate pair exactly for `1 < q < 5` (substrate q₀ ≈ 1.11 is inside).
  `|t| = √(q−1) = 0.33163018974662244642` (20 digits). Series recursion
  derived; radius exactly 1. Lean: `QOU/QBeta/C1ZeroSideExponents.lean`.

**NOT obtained — and the first attempt produced a false positive.**

The bases share no domain (`g` radius 1, `h` entire in 1/z), so the 0-solutions
must be propagated outward by the functional equation
`y(p²w) = [(p²−1)y(pw) + (p²−1)y(w)]/(p⁴w²−1)`. Doing that and forming
`P = Y₀⁻¹Y_∞` gave `P(pz) = P(z)` to all printed digits — which looks like the
ellipticity check passing and is **vacuous**. The basis is degenerate:

    normalised determinant |det|/max²
      k=0   2.4e-18      k=30  2.4e-20      k=60  9.1e-22      k=98  8.5e-23

Already 1e-18 **at the matching point, before any propagation**. A
rank-collapsed matrix satisfies `P(pz) = P(z)` trivially, so the agreement
carried no information. Recorded as a negative.

**Cause.** The normalisation `e_t(z) = θ_p(z)/θ_p(z/t)` puts the two conjugate
exponents ~17 orders of magnitude apart (`col0/col1 ~ 1e17` at k=0), so the two
columns are near-parallel numerically from the start. This is a construction
problem, not only propagation loss.

**Next honest step.** A numerically stable 0-side basis. Candidates, none
tried: rescale each column by its own magnitude before forming the matrix;
backward (Miller) recurrence, which is stable in the direction the forward one
is not; or work with the solution *ratio* `y₁/y₂` and its elliptic transform
directly, avoiding the matrix inverse entirely. Until one of these lands the
Stokes multipliers stay open.

**Process note.** This is the fourth object in this arc whose name outran its
content, and the first where the agent nearly committed the error rather than
finding it — the check that caught it was looking at the *conditioning* of a
matrix whose ellipticity had already "passed".

## 2026-08-07 (later) — THE NEGATIVE ABOVE IS REFUTED; connection matrix OBTAINED

Everything under "NOT obtained" is wrong, and none of the three proposed
repairs was needed. `computations/qbeta/c3_w2_c1_connection_matrix.py`,
witness `c3-w2-c1-connection-matrix.witness.json`, 7/7 checks.

**The basis was never degenerate — it cannot be.** `p = √q` is real, so `θ_p`
has real coefficients and `θ_p(conj w) = conj θ_p(w)`. The exponents are a
conjugate pair, so for real `z`, `|e_{t₁}(z)| = |e_{t₂}(z)|` **exactly**.
Measured ratio `1.0`; max deviation `0.0`. The "~17 orders of magnitude apart"
diagnosis describes something that cannot happen. Scale-invariant conditioning
`|det|/(‖col₀‖‖col₁‖)` is **0.59 … 0.72** across the disc, not `1e-18`.

**Three premises, all wrong:**

1. *"|det|/max² ≈ 2.4e-18 means rank collapse."* `|det|/max²` is not
   conditioning — it is not invariant under rescaling one column. The
   Casoratian obeys `W(pz) = −(q−1)W(z)/(p⁴z²−1)` **exactly** (verified to
   `1e-150`), so it decays under outward propagation analytically, columns
   staying independent. The decay that looked like collapse is a theorem.
2. *"The two bases share no domain."* `h` **entire in 1/z** means `Σ hₖz^{-k}`
   converges for *every* `z ≠ 0`. With the 0-side radius 1 they overlap on the
   whole punctured disc and match directly. The propagation that lost the
   conditioning was never required.
3. *"`P(pz) = P(z)` passed, but vacuously."* It is **automatic** — for any two
   fundamental matrices, `Y₀(pz) = A(z)Y₀(z)` and `Y_∞(pz) = A(z)Y_∞(z)`, so
   `A` cancels. Never evidence, at any conditioning. Correctness check only.

Most likely origin of the original numbers: a fixed symmetric truncation of
`θ_p`. Its dominant term sits at `n* = log|w|/log p − 1/2`, already `~96` at
`|w| ~ 150`, so a window like `n ∈ [−50, 50]` misses the peak entirely. This
script uses an adaptive window centred on `n*`.

**Result.** `P = [[c₊, c₋], [conj c₊, conj c₋]]` — conjugate structure exact
(dev `0.0`), elliptic per entry `1e-27 … 1e-55`, converged in (dps, NG, NH) to
`1.4e-38`. `c₋` has **simple poles exactly at `z ∈ T·p^ℤ`** (zeros of
`θ_p(−z/T)`); `|c₋·θ_p(−z/T)| → 1.1846e-18`, finite.

**NOT claimed — flagging before it becomes the fifth instance.** `c₊` looks
constant at the substrate (`z`-spread `2.0e-27`, `arg c₊ =
1.26603946254300268722`) and I was about to call it *the connection constant*
on Liouville grounds. It is **not** an exact constant: the `z`-variation is real
and grows with `q` — `3.1e-23` at `q=1.35`, `1.2e-10` at `1.8`, `6.9e-6` at
`2.5`, `2.5e-3` at `3.4`, `0.72` at `4.8` — and is **identical across dps
140→320, NG 800→2200**, so it is not a precision artifact. "Connection constant"
is a `q → 1` statement only. The law behind it is unidentified: fitting
`ln(variation)` vs `1/log p` gives local slopes bouncing over `8.0 … 10.5`, and
the small-`q` points go non-monotonic at the numerical floor. `π² = 9.8696` (the
q-modular scale) sits in that band — **observation, not identification**.

**Stokes multipliers: STILL OPEN.** The connection matrix is a prerequisite for
them, not the same thing. That is the remaining work on this bean.

## 2026-08-07 (later still) — POLE DIVISOR pinned, symbolic + Lean; π² retired

`computations/qbeta/c3_w2_c1_pole_divisor.py`, witness
`c3-w2-c1-pole-divisor.witness.json` (3/3), Lean
`QOU/QBeta/C1ConnectionPoles.lean` (**sorry-free, machine-verified**).

**The divisor is symbolic — nothing fitted.** Every pole of `P` sits where some
`θ_p` vanishes, and `θ_p`'s zero set is a single `p`-orbit: `θ_p(w) = 0 ⟺
w ∈ −p^ℤ`. With `T = √(q−1)/q^{3/4}`:

| pole on `ℂ*/p^ℤ` | locus | source | intrinsic? |
|---|---|---|---|
| `[−1]` | `z ∈ −p^ℤ` | `θ_p(z)`, the **common** numerator of `e_t(z) = θ_p(z)/θ_p(z/t)` | **NO — normalisation artifact** |
| `[−T]` | `z ∈ −T·p^ℤ` | `θ_p(z/T₊)` | yes |
| `[+T]` | `z ∈ +T·p^ℤ` | `θ_p(−z/T)` | yes |

So `c₊` has simple poles at `[−1]`, `[−T]`; `c₋` at `[−1]`, `[+T]`. The `[−1]`
pole sits in **both** columns because it comes from the 0-side character's
common numerator — it is an artifact of that normalisation, **not** connection
data. Only `[±T]` carry it.

**Divisor proved COMPLETE by the residue theorem.** On `ℂ*/p^ℤ` the invariant
differential is `dz/z`, so residues must sum to zero — and an elliptic function
**cannot have a single simple pole** per fundamental domain, so finding one
would have proved a pole was still missing. All three poles fall in one
fundamental annulus (radii ratio `1.0181 < p = 1.0536`), and each entry's two
residues cancel with a leftover falling **exactly linearly** in `ε` (decay
factors `10.0, 10.0`) — the `O(ε)` truncation of the limit estimate. Sum is
exactly zero.

**This resolves the `c₊` puzzle from the previous entry.** Both of `c₊`'s poles
(`[−1]`, `[−T]`) lie on the **negative** real ray. The positive axis — the only
region the earlier script sampled — is maximally far from them on the torus,
so `c₊` is flat there to `1e-27`; the residual wobble is just their tail, and it
grows with `q` because the torus shortens. **The π² observation is RETIRED** —
with the mechanism in hand there is no need to posit a modular constant, and no
evidence for one. (It was recorded as "observation, not identification"; that
was the right call, and this is the follow-through.)

**Lean, `C1ConnectionPoles.lean` — machine-verified, `lean-verify` exit 0,
`#print axioms` = `[propext, Classical.choice, Quot.sound]` (no `sorryAx`):**

- `qTheta_neg_zpow_eq_zero` : `θ_P(−P^{2k}) = 0` for **all** `k ∈ ℤ` — the `⊇`
  direction of the zero locus, which is what places the poles.
- Proof is an **involution** `n ↦ 2k−1−n`: it fixes the exponent
  `−n(n+1)+2kn` (pure `ring`) and flips `(−1)ⁿ` (since `n + (2k−1−n) = 2k−1` is
  odd), so the series is its own negative. **No summability hypothesis needed** —
  `Equiv.tsum_eq` and `tsum_neg` are both unconditional in Mathlib. That is what
  made this cheap; the analytic route would have needed bilateral summability.
- Reparametrised by `p = P²` so the exponent is `−n(n+1)` with no integer
  division. Nothing mathematical turns on it.

**NOT proved in Lean, and stated in the file:** the **converse** (that `−p^ℤ`
are the *only* zeros) is the Jacobi triple product; that these zeros are poles
*of `P`* needs the analytic construction; divisor completeness needs elliptic
function theory on `ℂ*/p^ℤ`. Whether Mathlib carries JTP was **not** settled —
the environment had only a partial olean cache and no Mathlib source, so its
absence there is not evidence either way. Worth checking before anyone scopes it.

**Env note for whoever picks this up:** Lean *does* work in the web sandbox via
`scripts/lean-toolchain-cache-restore.sh` + `scripts/lean-cache-restore.sh`
(`release.lean-lang.org` and the GitHub release-asset path both 403; the vendored
`lake-cache/toolchain-v4-24-0` branch is the only route). `lean` lands in
`~/.elan/toolchains/…/bin` and is **not** put on `PATH` — export it, then
`scripts/lean-verify.sh` works.

**Stokes multipliers: STILL OPEN.** Unchanged. The divisor is now known
symbolically, which is the natural input to extracting them.

## 2026-08-07 (fourth) — the INVARIANT `χ`; `[−1]` is unremovable but invisible; Mathlib has no JTP

`computations/qbeta/c3_w2_c1_connection_invariant.py`, witness
`c3-w2-c1-connection-invariant.witness.json` (5/5).

**The basis-invariant connection datum is the cross-ratio**

    χ(z) = P₀₀ P₁₁ / (P₀₁ P₁₀)

0-side rebasing scales `P`'s **rows** by elliptic functions; ∞-side rescaling
scales its **columns**; the cross-ratio is invariant under both. On the real
axis, where `P = [[c₊, c₋], [c̄₊, c̄₋]]`,

    χ = exp(2i (arg c₊ − arg c₋)),    |χ| = 1 **exactly**

matching the phase formula to `1e-121`, elliptic to `4.8e-26`.

**`[−1]` cannot be removed — the obvious fix is impossible.** Any character
with multiplier `t` must be `e_t(z) = θ_p(cz)/θ_p(cz/t)` (the numerator has to
carry multiplier `cz`), so its zeros sit at `z ∈ −c⁻¹p^ℤ`: varying `c` **moves**
the artifact pole to `[−1/c]` but never deletes it. Worse, the rebasing ratio
`r_t = e^{(c)}_t/e^{(1)}_t` drags in a further pole at `[−t]`. So "re-normalise
the 0-side character to kill `[−1]`" does not work as stated.

**It does not need to.** `[−1]` is common to a **row** of `P`, so it appears
once in χ's numerator and once in its denominator and **cancels**. Confirmed
both ways: at the artifact pole `|P₀₀|` diverges to `1e73` while `|χ|` stays
exactly `1`; and χ is numerically **identical** across `c ∈ {1, 1.7, 0.43, 2.9}`
(dev `1e-109`). The artifact pole's location is a basis choice the invariant
does not see.

**Mathlib has NO Jacobi triple product** (source inspected at HEAD). It has
`NumberTheory/ModularForms/JacobiTheta/{OneVariable,TwoVariable,Bounds,Manifold}`
defining the *additive* `jacobiTheta₂ z τ = ∑' n : ℤ, …`, but no triple product
(the "triple product" matches are Jordan algebras, Hermitian functional
calculus, vector cross product) and **no theta zero-locus/vanishing results at
all**. So the converse of `qTheta_neg_zpow_eq_zero` cannot be closed by reuse —
it needs JTP from scratch *plus* a bridge from the additive theta to the
multiplicative `θ_p`. Recorded so it is not re-scoped as cheap.

**Stokes multipliers: STILL OPEN.** χ is the invariant they must be functions
of, not the multipliers themselves. That remains the work.

## 2026-08-07 (fifth) — JTP infrastructure: summability + functional equation, both proved

`QOU/QBeta/C1ConnectionPoles.lean` extended; `lean-verify` exit 0, all
`#print axioms` = `[propext, Classical.choice, Quot.sound]` (no `sorryAx`).

Two new sorry-free theorems, the **shared prefix of every route to the
converse**:

- `summable_qThetaTerm` — the bilateral series converges for `P > 1`, `w ≠ 0`.
  `|term n| = exp(−L n² + (M−L)n)` with `L = log P > 0`, `M = log|w|`; one
  completed square gives `−L t² + B t ≤ B²/(4L)`, so it is dominated by
  `C·e^{−|n|}` with `B = |M−L|+1`, `C = exp(B²/(4L))`. Built from
  `Summable.of_nat_of_neg` + `summable_geometric_of_lt_one` — Mathlib's own
  `jacobiTheta₂` bound is not importable here (partial olean cache).
- `qTheta_functional_equation` — `θ_P(P²w) = w·θ_P(w)`, i.e. `θ_p(pw) = wθ_p(w)`.
  Both sides are `∑ P^{−n(n−1)}wⁿ`; reindex by `Equiv.subRight 1`.
  Unconditional.

**Why these and not JTP itself.** The vanishing theorem needs neither (the
involution is unconditional), but *any* converse route needs `θ_p` to be a
genuine analytic object, and the functional equation is what forces the zero set
to be a union of `p`-orbits.

**Scoping the rest, from the Mathlib source.** Mathlib **has**
`HasProd`/`Multipliable`/`tprod` and `Analysis/Meromorphic/{Divisor,
IsolatedZeros, Order}`. It **lacks the argument principle** — which kills the
cheap route ("`θ_p` holomorphic on `ℂ*` plus `θ_p(pw) = wθ_p(w)` forces exactly
one zero per fundamental annulus; `−1` is one; done"). So the two viable routes:

  (a) prove the argument principle, then zero-count; or
  (b) prove JTP via the product side — define `∏(1−xᵐ)(1+xᵐw)(1+xᵐ⁻¹w⁻¹)`,
      show it satisfies the same functional equation, conclude the ratio is
      elliptic and bounded hence constant.

Both are substantial multi-session jobs; (b) additionally needs Liouville on
`ℂ*/p^ℤ`. **Not** a small job — do not re-scope it as one. The two lemmas above
are the shared prefix either way, and are now done.

## 2026-08-07 (sixth) — χ off-axis; TWO CORRECTIONS; precision warning

`computations/qbeta/c3_w2_c1_invariant_structure.py`, witness
`c3-w2-c1-invariant-structure.witness.json` (4/4).

**⚠ PRECISION WARNING — the sibling scripts have NO off-axis signal.** They run
at `DPS=120, NG=500, NH=60`, ample on the real axis but not off it: the ∞-side
truncation `|hₖz^{-k}| ~ |T/z|^k p^{-k(k-1)/2}` is ~`1e-48` at `|z|=0.42, k=60`,
the same size as the quantities measured there. At `z = 0.42i` those settings
report `log10|χ| = −45.80`; the **converged value is −73.4468**. The first
number is pure truncation noise, and I nearly read a divisor off it.

The diagnostic that catches it: **`P(pz) = P(z)` is an algebraic identity**
(both `Y₀`, `Y_∞` satisfy `Y(pz) = A(z)Y(z)`, so `A` cancels), so any measured
deviation is error and nothing else — a free error meter. It is `1.1` at the
coarse settings (no signal), `3.7e-66` at `DPS=200/NG=800/NH=110`, `5.9e-230`
at `DPS=300`. **Check it before believing any off-axis number.**

**CORRECTION: `|χ| = 1` on the real axis is automatic, not a finding.** The
operator has real coefficients, so conjugation swaps the two 0-side solutions
(a conjugate pair) while fixing the ∞-side ones (real), hence swaps `P`'s rows:

    χ(conj z) = 1 / conj(χ(z))          (verified to 1e-268)

On the real axis `z = conj z`, so `|χ|² = 1` identically. The earlier entry
reported `|χ| = 1` as characterising χ; it is a consequence of this symmetry.
What the real axis genuinely carries is `arg χ = 2(arg c₊ − arg c₋)`.

**Off-axis structure.** `|χ|` is independent of `|z|` (spread `3.1e-9` over a
full `p`-period at `arg = π/2`), and `log|χ|` is **exactly linear in `arg z`**
out to `arg/π ≈ 0.4`, slope `−52.3046553508` per radian —
`−2π/(log p · ln 10)` to `2.4e-65`. So χ behaves like `z^{i·2π/log p}` in that
sector. It cannot *be* that (`z^{iλ}` is not single-valued on `ℂ*`). It then
**saturates** at `−73.4468`, bend near `arg/π = 0.447` — and
`arg(−t₂)/π = 0.446975`, a **0-side exponent direction**.

Power-like behaviour in sectors, switching across rays fixed by the exponents,
is the signature of a **theta quotient**: which term dominates the θ series
changes across those rays. So χ is presumably a ratio of `θ_p`'s in the
exponents and `T`.

**NOT determined: χ's divisor, hence not its closed form.** An elliptic function
is fixed by its divisor up to a constant; the sector data constrains it but does
not supply it. That is the concrete next step, and it needs `DPS ≥ 200` throughout.

**Stokes multipliers: STILL OPEN.**
