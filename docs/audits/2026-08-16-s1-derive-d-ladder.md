# S1 — Deriving the Q_β ladder in convention D

**Date:** 2026-08-16
**Branch:** `claude/s1-derive-d-ladder-2026-08-16` (PR #5187)
**Status:** RESULT — a structural exclusion, sorry-free in Lean, plus a
named wall. No D-frame `c_k` is derived, and none is claimed.

Owner instruction: *"derive D ladder"*, following the 2026-08-15 ruling
that convention D (`z_D = q³/(q²+1)`) is canonical and C
(`z_C = √q/(1+q)`) is excised for the registered channels.

---

## Summary

**The D ladder does not exist in the shape the C ladder has, and the
reason is structural rather than numerical.**

The ladder's phase `α = (z−1)h/2` is an affine functional of a single
Wedderburn weight — the standard-block weight `y_(2,1) = 1/2 − z` of the
explicit three-row instance `y = (z, 1/2−z, z)`. At `z_D` that weight is
**strictly negative for every `q > 1`**, so the phase has no positive-trace
reading anywhere in the substrate regime. Substituting `z_D` into
`α = (z−1)h/2` evaluates the three-row instance outside its positivity
domain; that is why the resulting numbers are meaningless, and it is a
sharper statement than "the rungs stop shrinking".

Three further findings fell out, all of which sharpen what the ladder *is*
in **both** frames:

- `c₂ = −1` is **convention-immune**, not "a C-frame statement".
- `c₃` is **not an independent rung** in either frame.
- The ladder **terminates at `k = 3` by construction**; `c₄…c₇` are
  identically zero.

Evidence: [`qbeta_d_frame_ladder_structure_probe.py`](../../computations/qbeta/qbeta_d_frame_ladder_structure_probe.py)
(15/15 assertions, 60 dps, proton pin) and
[`DecayLadderConventionDPositivity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DecayLadderConventionDPositivity.lean)
(sorry-free, `lean`-direct exit 0, `#print axioms` clean on all five
declarations).

---

## 1. Where a convention enters the ladder — exactly one scalar

The ladder is

$$
Q_\beta(q) \;=\; Q_A(q)\cdot\cos\!\bigl(\alpha(q) - u/2\bigr)\cdot
\prod_{k\ge 2}\bigl(1 + c_k u^k\bigr),
\qquad \alpha = \tfrac{(z-1)h}{2},\quad u = b\,\hbar_q^2 .
$$

Every other ingredient is **z-free**: `Q_A = |q²−2q−1|(q+1)/(2q³)`,
`h = q − q⁻¹`, `ℏ_q = (q−1)/q`, `b = √((h²+3)/(h²+4))`, `u`, and the N=2
factor `1 − b²ℏ_q⁴`. So the entire convention dependence of the Q_β ladder
is the one scalar `α` inside one cosine (probe A1).

Two consequences follow immediately.

### 1a. `c₂ = −1` is convention-IMMUNE — registry §9g row 3 is wrong about this

The Lean proof of `c₂ = −1`
([`q-beta-c-2-eq-neg-one-structural.lean`](../../content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.md))
is the `ring` identity `1 − b²ℏ⁴ = 1 − (b·ℏ²)²`. It never mentions `z`.
The coefficient is therefore the same in both frames.

Registry [§9g](../coordination/ck-dk-canonical-registry.md) row 3 reads
*"`c₂ = −1` (proved Taylor-exact) is a C-frame statement"*. That is not
right as stated. What is C-frame is the **empirical agreement** between the
`−1` and the fitted `c₂^emp` — which is `−1.0176` in C and `−9.299` in D.
The coefficient carries no convention; the agreement does. The row should
be corrected to say so.

Separately, and independently of the convention question: the Lean theorem
is a **renaming**, not a derivation. `1 − b²ℏ⁴ = 1 − (bℏ²)²` is true by
`ring` for any `b`, `ℏ`. The substantive claim — that the N=2 correction
factor *is* `1 − b²ℏ_q⁴` — is asserted in the file's docstring and proved
nowhere. Per AGENTS.md §"Derive-then-check standard" item 8, a proposition
provable without using any hypothesis about the objects is notation, not a
theorem. **Tier: the identity is `proved`; the identification of the N=2
factor is `asserted`.** This is not a defect introduced by the convention
change and it is not this branch's to fix, but it should not be cited as
"`c₂` is derived" without the qualifier.

### 1b. The C→D shift is the cosine substitution and nothing else

`Δc₃ = c₃^D − c₃^C = −972.3625…` is reproduced to `2.3e-58` relative by the
exact substitution `cos A_C → cos A_D` alone (probe A6). There is no second
mechanism in the frame change. (First-order perturbation is *not* adequate
here — `ΔA/A ≈ 21%` — and gives 11.7% error; the exact form is required.)

---

## 2. `c₃` is not an independent rung, in either frame

In [`qbeta_utils.c3_target_at`](../../computations/qbeta/qbeta_utils.py) and
[`qbeta_ck_cache.py`](../../computations/qbeta/qbeta_ck_cache.py), `c₂` is
**hardcoded to `−1`** inside the `c₃` extraction:

```
Q_N2 = Q_N1 · (1 + c₂ u²),  c₂ = −1
c₃   = (Q_codata / Q_N2 − 1) / u³
```

Writing `c₂^emp := (Q_exp/Q_N1 − 1)/u²` for the coefficient the N=1 residual
actually implies, the two are related by an exact closed form:

$$
c_3 \;=\; \frac{c_2^{\mathrm{emp}} + 1}{u\,(1 - u^2)} .
$$

Verified to `2.1e-56` (C) and `4.2e-59` (D) relative — probe A3. So `c₃`
carries no information beyond *how far the imposed `−1` sits from the fitted
`c₂^emp`*, divided by `u`.

The advertised "58× per-rung gain" is therefore not a convergence
measurement. The N2/N1 ratio is identically

$$
\frac{|c_3 u^3|}{|c_2^{\mathrm{emp}} u^2|}
= \frac{|c_2^{\mathrm{emp}} + 1|}{|c_2^{\mathrm{emp}}|}\cdot\frac{1}{1-u^2},
$$

which is `0.0173` in C and `0.8925` in D (probe A3, both confirmed against
the registry's quoted `0.017` and `0.89`). Both numbers are restatements of
one fitted quantity. **The C ladder does not converge faster than the D
ladder; the imposed `−1` is simply a better fit in C.**

## 3. The ladder terminates at `k = 3` by construction

The extraction loop sets `Q_next = Q_prev·(1 + c_k u^k)` with
`c_k = (Q_exp/Q_prev − 1)/u^k`, so `Q_next = Q_exp` **exactly**, and the
`k = 4` residual is zero to the last bit (probe A4, both frames,
`|Q_N3/Q_exp − 1| = 0.0` at 60 dps). The loop then breaks on its
`EPS_RESIDUAL` guard.

There are no `c₄…c₇` rungs. Whatever produced the "N=4 → N=5
non-monotonicity" cited in
[the canonical framing doc](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
as *"the experimental signature"* was a different computation — that doc's
Rule-2 per-rung table lists **structural candidate** values (`c₃·b⁴`,
`c₃²·3 + b`), not extracted ones. The distinction matters: the truncation
-order framing (Rule 1, `N ≥ log₁₀(1/ε)/2.07 − 1`) describes a series with
independent coefficients, and the implemented object has exactly one free
number past `c₂`.

---

## 4. The structural result — positivity separates C from D

Because `y_(2,1) = 1/2 − z`, the phase is affine in the standard-block
weight:

$$
\alpha \;=\; -\frac{h}{4} \;-\; \frac{h}{2}\,y_{(2,1)} .
$$

(Verified exactly, probe A7.) So "what ladder does D support?" is the
question "what is `y_(2,1)` at `z_D`?".

**Theorem** (`QOU.QBeta.zD_gt_half`, sorry-free). For every `q > 1`,
`z_D(q) = q³/(q²+1) > 1/2`.

*Proof.* `2q³ − q² − 1 = (q−1)(2q² + q + 1)`, and `2q² + q + 1 > 0` for all
real `q`. ∎

**Corollary** (`threeRowMiddleWeight_neg_at_zD`, sorry-free). For every
`q > 1`, `y_(2,1) = 1/2 − z_D(q) < 0`.

**Mirror** (`zC_lt_half`, `threeRowMiddleWeight_pos_at_zC`, sorry-free).
For every `q > 1`, `z_C(q) = √q/(1+q) < 1/2` — with `s = √q`, this is
`0 < (s−1)²` — hence `y_(2,1) > 0` at `z_C`.

**Capstone** (`threeRow_positivity_separates_zC_zD`). The two conventions
sit on opposite sides of the positivity boundary at every substrate value.

At the proton pin: `y_(2,1) = +0.000680` at `z_C`, `−0.112688` at `z_D`.

### What this excludes, and what it does not

**Scope-(b) structural exclusion** per AGENTS.md §"Before declaring
refuted": the invariant is a proved sign condition, and the excluded object
is named precisely — **the three-row weight instance `(z, 1/2−z, z)`
evaluated at `z_D`**. A Markov trace with a strictly negative Wedderburn
weight is not a positive trace, so the ladder's `α` formula has no
positive-trace reading at `z_D`, on the whole regime `q > 1` and not merely
at the pin.

It does **not** exclude convention D for the decay channel. That channel is
registered `disputed` (§9g) and stays so. What is excluded is the
*transport* of the C ladder's phase formula into D — which is exactly the
move the task brief identified as meaningless, now with a reason.

### Relation to the existing exclusion

`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free, pre-existing)
proves the mirror obstruction: at `z_C` the sign-block weight `y_(1³)` is
nonzero, so C is incompatible with the two-row cap that forces D in the
mass channel. Together:

| | three-row instance (the ladder's `α`) | two-row forcing (the mass channel) |
|---|---|---|
| **convention C** | admits (`y_(2,1) > 0`) | **excludes** (`y_(1³) ≠ 0`) |
| **convention D** | **excludes** (`y_(2,1) < 0`) | admits |

The ladder's phase belongs to the three-row row of that table. So there is
no D ladder of this shape, and the two exclusions are not in tension — they
are the same fact seen from two sides.

---

## 5. Genericity — is C's agreement forced, or merely in range?

AGENTS.md §"Defined residual ≠ derived decomposition" check 2. Solving the
N=2 model for the `z*` that reproduces `Q_exp` exactly (a **1-parameter
fit**, labelled as such) gives `z* = 0.499104480…`. Against a `1σ`
experimental window of half-width `1.01e-4` in `z`:

| | value | `|z − z*|` | in units of the 1σ window |
|---|---|---|---|
| `z*` (fitted) | 0.4991044802 | — | — |
| `z_C` | 0.4993203342 | 2.16e-4 | **2.13** |
| `z_D` | 0.6126880371 | 1.14e-1 | **1121** |

So `z_C` is a **2.1σ near-match, not an identity** — it does not reproduce
`Q_β`, it comes within about two experimental error bars of doing so. And
`z_D` is 1121σ away, a 526× discrimination.

**This is not an argument that C is right.** Reading it that way is the
flip-flop failure mode the
[canonical framing doc](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
was written to stop. What the table licenses is narrower: *if* the ladder
ansatz `Q_A·cos((z−1)h/2 − u/2)·(1−u²)` is the right shape, then the decay
channel's Markov parameter is `z*`, which is **neither** `z_C` **nor**
`z_D`. Combined with §4 — the ansatz's weight instance is not positive at
`z_D` — the more economical reading is that the ansatz's `z`-dependence is
itself the thing that does not survive into D.

---

## 6. The wall, stated exactly

To derive a genuine D-frame ladder one must derive the D-frame **two-row**
weight vector `(y_(3), y_(2,1), 0)` and recompute `α` from it, rather than
substituting `z_D` into a three-row formula. That is open. Specifically:

1. The two-row forcing sets `y_(1³) = 0`, so the weight vector is **not**
   `(z, 1/2−z, z)` and the affine relation `α = −h/4 − (h/2)y_(2,1)` — which
   was derived *from* that instance — no longer follows.
2. Which partitions survive at `q₀` is plausibly a **cell-module
   reducibility** question at a non-generic parameter. That is precisely
   what the S2 agent (`claude/s2-gram-radical-quotient-2026-08-16`, PR
   #5185) is measuring. Their result is an input here.
3. The published treatment of Markov-trace weights as a function of the
   trace parameter is Orellana, *Weights of Markov Traces on Hecke
   Algebras* (arXiv:math/9806163, `uploads/9806163v1.pdf`). **Glyph-collision
   warning:** that paper's "type D" is the Coxeter type `D_n`, which is
   **not** this repo's "convention D". The two are unrelated; the paper's
   type-A reduction is the relevant part.

Tracked as a bean — text in §8.

---

## 7. Tiering — every coefficient named in this document

| quantity | frame | tier | basis |
|---|---|---|---|
| `c₂ = −1` | both (immune) | **proved** (`ring` identity), *identification of the N=2 factor is `asserted`* | `q-beta-c-2-eq-neg-one-structural.lean` |
| `z_D > 1/2`, `y_(2,1) < 0` at `z_D`, ∀ `q>1` | D | **proved** (sorry-free) | `DecayLadderConventionDPositivity.lean` |
| `z_C < 1/2`, `y_(2,1) > 0` at `z_C`, ∀ `q>1` | C | **proved** (sorry-free) | same |
| `c₃ = (c₂^emp+1)/(u(1−u²))` | both | **symbolic-exact** | probe A3, `2e-56` |
| `Δc₃` = cos-substitution | C→D | **symbolic-exact** | probe A6, `2e-58` |
| `c₄…c₇ ≡ 0` | both | **symbolic-exact** | probe A4, exact zero |
| `c₂^emp = −1.0176` | C | **fitted** | inversion of experimental `Q_β` |
| `c₂^emp = −9.2989` | D | **fitted** | inversion of experimental `Q_β` |
| `c₃ = −2.06934` | C | **fitted** | inversion of experimental `Q_β` |
| `c₃ = −974.432` | D | **fitted** | inversion of experimental `Q_β` |
| `z* = 0.4991045` | — | **fitted** | 1-parameter solve against `Q_β` |
| the D-frame two-row `α` | D | **OPEN** | §6 |

Nothing in the `fitted` rows is derived, and none of it is presented as a
D-frame result.

---

## 8. Bean text (for the owner to mint — no ID hand-assigned)

> **GAP: derive the convention-D two-row Markov weight vector and the
> ladder phase α it induces.**
>
> The Q_β ladder's phase is `α = (z−1)h/2 = −h/4 − (h/2)·y_(2,1)`, an
> affine functional of the standard-block weight of the *three-row*
> instance `y = (z, 1/2−z, z)`. `QOU.QBeta.threeRowMiddleWeight_neg_at_zD`
> (sorry-free, PR #5187) proves `y_(2,1) < 0` at `z_D` for every `q > 1`,
> so that instance is not a positive trace anywhere in the substrate regime
> and the phase formula cannot be transported C→D. Under the two-row cap
> that forces D, `y_(1³) = 0` and the weight vector is `(y_(3), y_(2,1), 0)`
> — which α has never been computed for.
>
> *Attempted:* re-extraction of `c₃` under D (gives `−974.43`; meaningless,
> and now explained: it evaluates the three-row instance outside its
> positivity domain). Genericity check on `z` (the `z` reproducing `Q_β` is
> `z* ≈ 0.499104`, neither `z_C` at 2.1σ nor `z_D` at 1121σ).
>
> *Why it stalled:* deriving the two-row weight vector needs to know which
> partitions survive at `q₀` under D — plausibly a cell-module
> reducibility question at a non-generic parameter, which is S2's front
> (PR #5185).
>
> *Next honest step:* take S2's Gram-radical result; if a cell module is
> reducible at `q₀`, read off the surviving partitions, build the two-row
> weight vector from Orellana's type-A weight formula
> (arXiv:math/9806163, `uploads/9806163v1.pdf`), recompute `α`, and only
> then ask what `c_k` the resulting series has. Do **not** extract a `c₃`
> before that — it would be another inversion of experimental `Q_β`.
>
> *Also queued from this branch:* correct registry §9g row 3 ("`c₂ = −1` is
> a C-frame statement" → the coefficient is convention-immune; the
> *empirical agreement* is what is C-frame), and record that `c₃` is
> algebraically dependent on `c₂^emp` so the quoted rung ratios are
> restatements rather than convergence measurements.

---

## Provenance

- **Pin:** proton / experimental, `q₀ ≈ 1.1099785827513808`, read from the
  package constant `qou_substrate.constants.Q_50_DIGIT_STR`. No muon-built
  cache is read; `wedderburn_jones_markov.y_lambda_at` is not called.
- **Precision:** 60 dps mpmath throughout; no float64 enters any reported
  number.
- **Lean verification:** `lean`-direct against the pre-existing restored
  olean cache, exit 0, `#print axioms` showing only `propext`,
  `Classical.choice`, `Quot.sound` on all five declarations. **No olean
  restore was performed** — the disk had 371 MB free at the time (the
  8 GB floor for a restore was not met, so the existing cache was used
  read-only instead).
- **Cross-validation:** the probe independently reproduces registry §9g's
  quoted `c₃^C = −2.06934258`, `c₃^D = −974.43`, `c₂^emp` `−1.0176` /
  `−9.299`, and rung ratios `0.017` / `0.89`.
