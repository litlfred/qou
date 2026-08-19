# S1 — Deriving the Q_β ladder in convention D

**Date:** 2026-08-16
**Branch:** `claude/s1-derive-d-ladder-2026-08-16` (PR #5187)
**Status:** ⚠️ **HEADLINE RETRACTED 2026-08-16** — the claim that convention
D has a negative Wedderburn weight and fails positivity is **withdrawn**;
it rested on a false identification (`1/2 − z` is not `y_(2,1)`). D is
positive semidefinite, signature `(5,0,1)`. What survives is a scope-(a)
negative — the C ladder's phase formula does not transport to D by
parameter substitution — plus three `z`-free findings and a named wall.
The Lean is sound and sorry-free throughout; only the interpretation was
wrong. No D-frame `c_k` is derived, and none is claimed. **Read the
Summary box first.**

Owner instruction: *"derive D ladder"*, following the 2026-08-15 ruling
that convention D (`z_D = q³/(q²+1)`) is canonical and C
(`z_C = √q/(1+q)`) is excised for the registered channels.

---

## Summary

> ### 🛑 HEADLINE RETRACTED 2026-08-16 — convention D does **not** fail positivity
>
> **This document's original headline claim is withdrawn.** It asserted that
> `1/2 − z` is the standard-block Wedderburn weight `y_(2,1)`, that this
> weight is strictly negative at `z_D`, and therefore that the D-frame phase
> has **no positive-trace reading**. The identification is false and the
> conclusion **inverts**.
>
> **What is actually true**, established by S2
> ([PR #5185](https://github.com/litlfred/qou/pull/5185), audit
> [§3bis](2026-08-16-s2-gram-radical-independent-revalidation.md)) and cited
> here rather than re-derived: solving the corpus's own three defining
> conditions for the `H₃(q)` Markov weights at `z = z_D` gives
>
> | λ | rows | `y_λ` under D | sign for `q > 1` |
> |---|---|---|---|
> | `(3)` | 1 | `(q⁴+1)/(q²+1)²` | **positive** |
> | `(2,1)` | 2 | `q²/(q²+1)²` | **positive** |
> | `(1³)` | 3 | `0` | identically zero |
>
> — **positive semidefinite, signature `(5, 0, 1)`**. The surviving weights
> are both strictly positive and the single dead weight is *exactly zero,
> not negative*. That is what a Temperley–Lieb trace should look like, so
> the weight structure under D **confirms** the TL identification instead of
> arguing against it.
>
> **Why the original claim was wrong — the durable lesson.** The vector
> `(z, 1/2 − z, z)` satisfies **only** the normalisation condition of
> `CanonicalMarkovWeightsH3`; it **fails** the other two defining
> conditions. So it is not a weight vector of `H₃(q)` at all, and
> `1/2 − z_D` is simply not `y_(2,1)`. At `q ≈ 1.11` the two differ in sign
> as well as magnitude — `1/2 − z_D ≈ −0.1127` versus the actual
> `y_(2,1) ≈ +0.2473`.
>
> This is a **symbol-collision / claim-shape failure**, precisely the class
> AGENTS.md §"Grep the claim SHAPE, not only the topic" exists to catch: *a
> formula was given the name of an object whose defining conditions it does
> not satisfy.* Grepping the topic (`y_(2,1)`, Markov weights,
> `CanonicalMarkovWeightsH3`) returned plenty and looked like corroboration.
> The step that was skipped is the one that mattered — checking whether
> **this expression** satisfies the **defining conditions** of the object
> whose name it was given. No amount of topic-grep would have caught it.
>
> **The Lean theorem stands and is untouched.** `1/2 − z_D < 0` for `q > 1`
> is true, sorry-free, and was never in question. Only the *interpretation*
> was wrong. The declaration has been **renamed** — `threeRowMiddleWeight`
> → `ladderPhaseCoeff`, and correspondingly
> `threeRowMiddleWeight_neg_at_zD` → `ladderPhaseCoeff_neg_at_zD` — so the
> name describes what it actually proves (the sign of an affine phase
> coefficient) rather than a Wedderburn weight it is not.
>
> **Scope reclassified (b) → (a).** The original scope-(b) *structural
> exclusion* of convention D is withdrawn: the invariant it cited — a
> negative Wedderburn weight — does not exist. What survives is a
> scope-(a) scope-limited negative about the *transport of one ansatz's
> phase formula*, below.
>
> Superseded text is retained in marked boxes rather than deleted, per
> AGENTS.md §"Before declaring refuted": the numerical results stand; only
> the identification and its scope were wrong.

### What survives

**The C ladder's phase formula does not transport to D by substituting the
parameter** — a scope-**(a)** result about the ansatz, carrying no claim
about either trace's positivity.

The ladder's phase is affine in the coefficient `1/2 − z`:
`α = (z−1)h/2 = −h/4 − (h/2)·(1/2 − z)`, pure algebra. That coefficient is
**positive at `z_C` and negative at `z_D`, for every `q > 1`** (sorry-free),
so the two conventions place the ansatz's phase on opposite sides of
`z = 1/2`. The `−974.43` obtained by substituting `z_D` remains meaningless
— but because the substitution transports a formula out of the frame it was
derived in, **not** because any weight goes negative.

Three further findings are unaffected by the retraction — all concern the
`z`-free part of the ladder and sharpen what it *is* in **both** frames:

- `c₂ = −1` is **convention-immune**, not "a C-frame statement".
- `c₃` is **not an independent rung** in either frame.
- The ladder **terminates at `k = 3` by construction**; `c₄…c₇` are
  identically zero.

§6b's three algebraic identities (`z_D = q²/[2]_q`, `z_C = 1/[2]_{√q}`,
`δ − 2 = (q/b)·u`) are likewise unaffected, and §6c's status for the TL
identification is unchanged: a **hypothesis under test**, not a result.

Evidence: [`qbeta_d_frame_ladder_structure_probe.py`](../../computations/qbeta/qbeta_d_frame_ladder_structure_probe.py)
(20/20 assertions, 60 dps, proton pin — A7 relabelled to `κ(z) = 1/2 − z`
and **A7r** added as a retraction guard) and
[`DecayLadderConventionDPositivity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DecayLadderConventionDPositivity.lean)
(sorry-free, `lean`-direct exit 0, `#print axioms` clean on all ten
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

## 4. The sign of the ladder's affine phase coefficient

> ### 🛑 RETRACTED — this section originally read the sign below as a Wedderburn-weight positivity failure
>
> **The superseded claim, retained verbatim** (AGENTS.md §"Before declaring
> refuted" — re-scope, do not delete):
>
> > Because `y_(2,1) = 1/2 − z`, the phase is affine in the standard-block
> > weight: `α = −h/4 − (h/2)·y_(2,1)`. … **Scope-(b) structural
> > exclusion**: the invariant is a proved sign condition, and the excluded
> > object is named precisely — the three-row weight instance `(z, 1/2−z, z)`
> > evaluated at `z_D`. A Markov trace with a strictly negative Wedderburn
> > weight is not a positive trace, so the ladder's `α` formula has no
> > positive-trace reading at `z_D` …
> >
> > | | three-row instance (the ladder's `α`) | two-row forcing (the mass channel) |
> > |---|---|---|
> > | **convention C** | admits (`y_(2,1) > 0`) | **excludes** (`y_(1³) ≠ 0`) |
> > | **convention D** | **excludes** (`y_(2,1) < 0`) | admits |
>
> **`1/2 − z` is not `y_(2,1)`.** The vector `(z, 1/2 − z, z)` satisfies
> only the normalisation condition of `CanonicalMarkovWeightsH3` and fails
> the other two, so it is not a weight vector of `H₃(q)`. The actual
> convention-D weights are `y_(3) = (q⁴+1)/(q²+1)²`,
> `y_(2,1) = q²/(q²+1)²`, `y_(1³) = 0` — **positive semidefinite, signature
> `(5, 0, 1)`** (S2, [PR #5185](https://github.com/litlfred/qou/pull/5185)
> [§3bis](2026-08-16-s2-gram-radical-independent-revalidation.md); cited,
> not re-derived). At `q ≈ 1.11`, `1/2 − z_D ≈ −0.1127` while the actual
> `y_(2,1) ≈ +0.2473`.
>
> So **the "excludes (`y_(2,1) < 0`)" cell of that table is wrong**, and
> with it the whole D column's positivity reading. Convention D does not
> fail positivity; its weight structure is exactly what a Temperley–Lieb
> trace should look like, which **supports** the TL identification rather
> than arguing against it. The scope-(b) structural exclusion is
> **withdrawn** — the invariant it cited does not exist.
>
> **Class of error:** symbol collision — a formula given the name of an
> object whose defining conditions it does not satisfy. See the Summary box.

**What the Lean actually proves**, unchanged and correct. The ladder's
phase is affine in the coefficient `κ(z) := 1/2 − z`:

$$
\alpha \;=\; \frac{(z-1)h}{2} \;=\; -\frac{h}{4} \;-\; \frac{h}{2}\,\kappa(z),
$$

pure algebra (probe A7). The two conventions place `κ` on opposite sides of
zero:

**Theorem** (`QOU.QBeta.zD_gt_half`, sorry-free). For every `q > 1`,
`z_D(q) = q³/(q²+1) > 1/2`.

*Proof.* `2q³ − q² − 1 = (q−1)(2q² + q + 1)`, and `2q² + q + 1 > 0` for all
real `q`. ∎

**Corollary** (`ladderPhaseCoeff_neg_at_zD`, sorry-free). For every
`q > 1`, `κ(z_D) = 1/2 − z_D(q) < 0`.

**Mirror** (`zC_lt_half`, `ladderPhaseCoeff_pos_at_zC`, sorry-free). For
every `q > 1`, `z_C(q) = √q/(1+q) < 1/2` — with `s = √q`, this is
`0 < (s−1)²` — hence `κ(z_C) > 0`.

**Capstone** (`ladderPhaseCoeff_sign_separates_zC_zD`). The two conventions
sit on opposite sides of `z = 1/2` at every substrate value.

At the proton pin: `κ = +0.000680` at `z_C`, `−0.112688` at `z_D`.

> **The sign of `κ` carries no trace-positivity content.** It is a threshold
> crossing of an affine coefficient in one ansatz. Nothing about the
> positivity of any Markov trace follows from it, in either direction.
> Machine-guarded as probe assertion **A7r**.

### What this excludes, and what it does not

**Scope-(a) scope-limited negative** per AGENTS.md §"Before declaring
refuted" (downgraded from the withdrawn scope-(b) above). What is excluded
is the **transport** of the C ladder's phase formula into D by substituting
the parameter: `α = (z−1)h/2` was derived in the C frame, and `κ` changes
sign between the frames, so the substitution carries the formula outside
the regime it was derived in. That is why the resulting `−974.43` is
meaningless.

It does **not** exclude convention D — for the decay channel or at all.
That channel is registered `disputed` (§9g) and stays so, on other grounds.
It does not exclude a D-frame ladder; it says only that one is not obtained
by parameter substitution.

### Relation to the existing exclusion

`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free, pre-existing)
proves that at `z_C` the sign-block weight `y_(1³)` is nonzero, so C is
incompatible with the two-row cap that forces D in the mass channel. With
the retraction above, that result now reads **alongside** S2's rather than
against it: under D the same `y_(1³)` is exactly zero, so the two-row cap
is satisfied and the D weights are positive semidefinite. Both point the
same way — toward D and toward the TL identification.

The earlier two-column table claiming the ladder's `α` "excludes D" on
positivity grounds is withdrawn (see the box). The surviving asymmetry is
narrower and is not about positivity: the ansatz's phase formula was
derived in the C frame and does not transport.

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

**The wall has moved, and it is narrower than this section originally
claimed.** The D-frame weight vector is **no longer open** — S2 computed it
(Summary box; cited, not re-derived), and it is positive semidefinite with
`y_(1³) = 0`, so the two-row cap is satisfied automatically rather than
needing to be imposed.

What is open is the **phase**: the relation `α = −h/4 − (h/2)·y_(2,1)` was
read off the bogus instance `(z, 1/2−z, z)`, so there is **no established
relation between the ladder's `α` and the actual Wedderburn weights in
either frame**. The affine-in-`y_(2,1)` story was an artefact of the wrong
instance, and removing it leaves the ansatz's phase without a derivation
from weights at all. That — not the weight vector — is the wall.

> ### 🛑 DOUBLY SUPERSEDED — first box's *conclusion* survives, its *reason* does not
>
> **The original §6 proposed this repair**, retained verbatim (AGENTS.md
> §"Before declaring refuted"):
>
> > 1. The two-row forcing sets `y_(1³) = 0`, so the weight vector is **not**
> >    `(z, 1/2−z, z)` and the affine relation `α = −h/4 − (h/2)y_(2,1)` —
> >    which was derived *from* that instance — no longer follows.
>
> **The first correction pass then argued** (also retained, also wrong):
>
> > - `(2,1)` is a **two-row** partition, so it **survives** the TL quotient.
> > - But `threeRowMiddleWeight_neg_at_zD` proves `y_(2,1) = 1/2 − z_D < 0`
> >   for **every** `q > 1`.
> > - A positive trace factoring through `TL_3` requires `y_(2,1) ≥ 0`.
> > - The negative weight therefore sits on a **surviving** block … hence the
> >   weights **must be recomputed inside `TL_3`, where the normalisation
> >   differs.**
>
> **That reasoning is void**, because its second bullet is the retracted
> identification: `1/2 − z_D` is not `y_(2,1)`, so there is no negative
> weight on a surviving block and no contradiction to resolve. The first and
> third bullets are correct and stand.
>
> **Nor is its conclusion established.** The weights do **not** need to be
> recomputed "inside `TL_3` where the normalisation differs" — S2 obtained
> them by solving the `H₃(q)` conditions **at `z = z_D` directly**, and
> `y_(1³) = 0` falls out. No separate `TL_3` normalisation was required.
>
> **What survives from both boxes** is the original item 1's inference, on
> its own terms: the D-frame vector is not `(z, 1/2−z, z)` with the third
> entry zeroed, and the affine relation `α = −h/4 − (h/2)y_(2,1)` does not
> transport. That was right for a simpler reason than either box gave — the
> vector was never a weight vector in the first place.
>
> Correction of record:
> [PR #5187 comment](https://github.com/litlfred/qou/pull/5187#issuecomment-5305314459),
> [PR #5185 comment](https://github.com/litlfred/qou/pull/5185#issuecomment-5305313383);
> retraction landed on this branch 2026-08-16.

### 6a. What remains of the wall

1. ~~Which partitions survive at `q₀` is plausibly a **cell-module
   reducibility** question at a non-generic parameter.~~ **Answered, and
   the framing was wrong.** S2 measured the degeneration to be **generic in
   `q`** — `det G ≡ 0` identically over ℚ(q), corank unchanged across 12
   rational `q` — so no cell module is degenerating and no re-pin can move
   it. The surviving partitions under D are `(3)` and `(2,1)`, with
   `y_(1³) = 0` identically. See their audit §3.
2. ~~The weight vector must be **recomputed in the quotient**, not restricted
   from `H_3`.~~ **No longer open.** S2 obtained the D-frame weights by
   solving the `H₃(q)` defining conditions at `z = z_D` directly (Summary
   box). What remains open is the **phase**: with the affine-in-`y_(2,1)`
   relation retracted, there is no derivation of the ladder's `α` from the
   actual weights in *either* frame. Until there is, there is no D-frame
   `α`, and extracting a `c₃` beforehand would still be another inversion of
   experimental `Q_β`.
3. The published treatment of Markov-trace weights as a function of the
   trace parameter is Orellana, *Weights of Markov Traces on Hecke
   Algebras* (arXiv:math/9806163, `library/arxiv-math-9806163v1/9806163v1.pdf`). **Glyph-collision
   warning:** that paper's "type D" is the Coxeter type `D_n`, which is
   **not** this repo's "convention D". The two are unrelated; the paper's
   type-A reduction is the relevant part.

### 6b. Three exact algebraic facts — machine-verified

These were hand-derived when the originating worktree was unavailable and
are now **verified numerically** (mpmath, 60 dps, proton pin
`q₀ = 1.1099785827513808…` read from `qou_substrate.constants.Q_50_DIGIT_STR`;
`z_C`, `z_D`, `b`, `u` imported verbatim from
`qbeta_d_frame_ladder_structure_probe.py`). All three are **identities**, so
they hold at every `q`, not just the pin — each closes to `< 1e-60`, i.e. to
working precision.

| # | claim | value at `q₀` | residual |
|---|---|---|---|
| 1 | `z_D = q²/[2]_q`, `[2]_q = q + q⁻¹` | `0.612688037146465251…` | `7.8e-62` |
| 2 | `z_C = 1/[2]_{√q}` | `0.499320334183694452…` | `7.8e-62` |
| 3 | `δ − 2 = (q/b)·u` | `0.0108968667071 = 1.27939023435 × 0.00851723455016` | `6.3e-62` |

Reproducible as assertions **A8** of
[`qbeta_d_frame_ladder_structure_probe.py`](../../computations/qbeta/qbeta_d_frame_ladder_structure_probe.py)
(20/20, exit 0). The residuals above were obtained twice — once by a
standalone check and once inside the probe — by two independent
implementations that agree to the digit.

Each is a one-line rearrangement, which is why the residuals are at
round-off:

- **(1)** `[2]_q = (q²+1)/q`, so `q²/[2]_q = q³/(q²+1) = z_D`. Now also
  **Lean-proved** over a generic field — `QOU.QBeta.zD_eq_qsq_div_bracketTwo`
  (§7c-compliant: no ordering, no `Real.sqrt`), with the `ℝ`
  specialisation `zD_eq_qsq_div_bracketTwo_real`.
- **(2)** with `s = √q`, `1 + q = s·[2]_s`, so `z_C = √q/(1+q) = 1/[2]_s`.
  Not stated generically — `Real.sqrt` puts it on the archimedean side of
  the §7c wall.
- **(3)** `δ − 2 = (q−1)²/q` and `u = b·ℏ_q² = b(q−1)²/q²`, so the ratio is
  exactly `q/b`.

**What they mean, and what they do not.** `δ = [2]_q` is the Temperley–Lieb
loop parameter, so (1) says `z_D` is `q²` over that loop parameter — a
TL-shaped object, reached from the *ladder* side rather than from the Gram
side. (3) says a TL-organised expansion in `δ−2` is a **rescaling** of the
ladder's `u`-expansion by the constant `q/b`, not a new series. (2) notes
that C is `[2]`-flavoured too, but at `√q` rather than `q`.

**These are observations about shape, not evidence of a mechanism.** A
number being expressible in TL notation does not make the trace factor
through TL — see §6c.

*Correction to the source comments:* they quote `q²/[2]_q = 0.6126878…`.
That digit string is a transcription slip; the verified value is
`0.6126880371464652…`, identical to `z_D` as the identity requires. The
`z_C` and `δ−2` figures quoted there reproduce exactly.

### 6c. The TL identification is a HYPOTHESIS UNDER TEST

The sibling's D-frame Markov–Gram coranks at `n = 3, 4, 5` are `1, 10, 78`,
matching `n! − Catalan(n)` = `dim ker(H_n(q) ↠ TL_n(q))` — arithmetic
re-checked here (`6−5=1`, `24−14=10`, `120−42=78`). If it holds, the radical
is the Temperley–Lieb ideal and the degeneration is **generic in `q`**, not
special-parameter reducibility. It would also *derive* the two-row forcing
that the corpus currently posits, since `TL_3` annihilates exactly `(1³)`.

**Three points fitting a formula is suggestive, not proved.** This is
recorded as an open hypothesis and **nothing is built on it**. The
measurement is the sibling's and was not re-derived here.

- **Discriminator:** `n = 6`, where `720 − 132 = 588`.
- **Cheapest confirming test:** does the sibling's `n = 3` radical land on
  the `(1³)` block *specifically*? That distinguishes "the radical **is**
  the TL ideal" from "some other 1-dimensional radical". Asked on #5185.

**Bearing of the retraction on this hypothesis: it strengthens it.** The
weight structure S2 measured under D — `y_(3), y_(2,1) > 0` and
`y_(1³) = 0` exactly, signature `(5,0,1)` — is what a Temperley–Lieb trace
looks like: positive on the `≤ 2`-row blocks, zero on the rest. The
retracted claim pointed the other way, so removing it removes an apparent
counter-indication.

**It is still not a proof.** The corank data remains three points fitting
`n! − Catalan(n)`, and a positive semidefinite weight vector with the right
zero is *consistent with* the TL identification without establishing it.
`n = 6` (`588`) is still the discriminator, and the block-identity question
above is still the cheap test. Nothing is built on it.

**Scope of the correction in the box above:** scope-**(a)**, a
scope-limited negative. What is excluded is the *transport* of the C
ladder's phase formula into D by parameter substitution. It does **not**
exclude convention D, nor a D-frame ladder, nor the TL route.

Tracked as a bean — text in §8.

---

## 7. Tiering — every coefficient named in this document

| quantity | frame | tier | basis |
|---|---|---|---|
| `c₂ = −1` | both (immune) | **proved** (`ring` identity), *identification of the N=2 factor is `asserted`* | `q-beta-c-2-eq-neg-one-structural.lean` |
| `z_D > 1/2`, so `κ = 1/2 − z_D < 0`, ∀ `q>1` | D | **proved** (sorry-free) | `DecayLadderConventionDPositivity.lean` |
| `z_C < 1/2`, so `κ = 1/2 − z_C > 0`, ∀ `q>1` | C | **proved** (sorry-free) | same |
| ~~`κ` *is* the Wedderburn weight `y_(2,1)`~~ | — | **RETRACTED** — false; `(z,1/2−z,z)` fails 2 of 3 defining conditions | Summary box; S2 [#5185 §3bis](2026-08-16-s2-gram-radical-independent-revalidation.md) |
| D-frame weights `y_(3),y_(2,1) > 0`, `y_(1³) = 0`; signature `(5,0,1)` | D | **measured** (exact, S2's symbolic solve) — **cited, not re-derived** | S2 [#5185 §3bis](2026-08-16-s2-gram-radical-independent-revalidation.md); guarded here as probe A7r |
| `z_D = q²/[2]_q` | D | **proved** (sorry-free, generic `[Field R]`) | `zD_eq_qsq_div_bracketTwo`; numerics §6b, `7.8e-62` |
| `z_C = 1/[2]_{√q}` | C | **symbolic-exact** | §6b, `7.8e-62` (archimedean — not stated generically) |
| `δ − 2 = (q/b)·u` | both | **symbolic-exact** | §6b, `6.3e-62` |
| radical `=` TL ideal (coranks `n!−C_n`) | D | **HYPOTHESIS under test** | 3 points only; `n=6` is the discriminator — §6c |
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

> **GAP: derive the Q_β ladder phase `α` from the actual Wedderburn
> weights — in either frame.**
>
> The ladder's phase was believed to be `α = −h/4 − (h/2)·y_(2,1)`, an
> affine functional of the standard-block weight of the "three-row instance"
> `y = (z, 1/2−z, z)`. **That instance is not a weight vector of `H₃(q)`** —
> it satisfies only the normalisation condition and fails the other two — so
> the affine relation is retracted and **there is now no derivation of `α`
> from weights in either frame**. That is the gap.
>
> The D-frame weight vector itself is **not** the gap: S2 (PR #5185, audit
> §3bis) solved the `H₃(q)` conditions at `z = z_D` and obtained
> `y_(3) = (q⁴+1)/(q²+1)²`, `y_(2,1) = q²/(q²+1)²`, `y_(1³) = 0` —
> positive semidefinite, signature `(5,0,1)`, with the two-row cap satisfied
> automatically.
>
> *Attempted:* re-extraction of `c₃` under D (gives `−974.43`; meaningless,
> because it transports a C-frame phase formula by parameter substitution).
> Genericity check on `z` (the `z` reproducing `Q_β` is `z* ≈ 0.499104`,
> neither `z_C` at 2.1σ nor `z_D` at 1121σ).
>
> *⚠️ RETRACTED — do not revive either of these (see §4, §6).* Two earlier
> versions of this bean are wrong and are recorded so a later agent does not
> re-derive them:
> 1. *"`y_(2,1) = 1/2 − z_D < 0`, so D is not a positive trace."* **False
>    premise.** `1/2 − z` is not `y_(2,1)`; the actual `y_(2,1)` under D is
>    `q²/(q²+1)² > 0`. **Convention D does not fail positivity.**
> 2. *"The weights must be recomputed inside `TL_3`, where the normalisation
>    differs."* **Not established** — and unnecessary. S2 got them from the
>    `H₃(q)` conditions at `z_D` directly.
>
> The Lean is sound throughout; only the reading of it was wrong. The
> declaration is now named `ladderPhaseCoeff_neg_at_zD` — it proves
> `1/2 − z_D < 0`, a statement about an affine phase coefficient with **no**
> trace-positivity content.
>
> *Next honest step:* start from S2's D-frame weights (above) and ask
> whether the ladder ansatz's phase `α = (z−1)h/2` can be derived from them
> at all — via Orellana's type-A weight formula (arXiv:math/9806163,
> `library/arxiv-math-9806163v1/9806163v1.pdf`), noting its "type D" is the Coxeter type `D_n`
> and unrelated to convention D. If no such derivation exists, the honest
> conclusion is that the ansatz's `z`-dependence is not weight-derived in
> *either* frame — which would also explain why `z*` matches neither `z_C`
> nor `z_D`. Do **not** extract a `c₃` before that — it would be another
> inversion of experimental `Q_β`.
>
> *Open hypothesis, not an input yet:* the sibling's coranks `1, 10, 78` at
> `n = 3, 4, 5` match `n! − Catalan(n)`, suggesting the radical is the TL
> ideal. The `(5,0,1)` signature is consistent with it and removes an
> apparent counter-indication, but three points are suggestive, not proved;
> `n = 6` (`588`) is the discriminator, and the cheap confirming test is
> whether the `n = 3` radical lands on `(1³)` specifically. Do not build on
> it before then.
>
> *Verified algebra available to the next agent (§6b):* `z_D = q²/[2]_q`
> (also Lean-proved generically, `QOU.QBeta.zD_eq_qsq_div_bracketTwo`),
> `z_C = 1/[2]_{√q}`, and `δ − 2 = (q/b)·u` — so a TL expansion in `δ−2` is
> a rescaling of the `u`-expansion by `q/b`, not a new series.
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

### Correction pass (2026-08-16, same session)

The §6/§8 correction was written after the originating worktree was lost to
disk cleanup; the algebra had been hand-derived and posted to the PRs to
survive. This pass **re-verified it on a machine** before writing it down:

- **Numerics:** all three §6b identities re-derived at 60 dps against the
  proton pin, using `z_C`/`z_D`/`b`/`u` imported verbatim from the branch
  probe rather than re-implemented. Residuals `7.8e-62`, `7.8e-62`,
  `6.3e-62`. One transcription slip in the source comments corrected
  (`q²/[2]_q` was quoted as `0.6126878…`; it is `0.6126880371464652…`).
  The `n! − Catalan(n)` arithmetic was re-checked for `n = 3,4,5,6`.
- **Lean:** re-verified `lean`-direct against the pre-existing restored
  olean cache (6990 Mathlib oleans, used **read-only** — no `lake build`,
  no second restore), exit 0. `#print axioms` on all seven declarations
  reports only `propext`, `Classical.choice`, `Quot.sound` — no `sorryAx`.
- **Added:** `zD_eq_qsq_div_bracketTwo` (generic `[Field R]`, §7c) and its
  `ℝ` specialisation, both discharged by `field_simp` alone.
- **Not re-derived:** the sibling's Gram/corank measurement (`1, 10, 78`).
  That remains their result and is cited, not reproduced.

### Retraction pass (2026-08-16, same session)

The headline claim was withdrawn after S2 (PR #5185 §3bis) showed the
`y_(2,1)` identification is false. See the Summary box for the full
statement; recorded here is what was changed and re-verified.

- **Retracted:** that `1/2 − z` is the Wedderburn weight `y_(2,1)`, that
  the weight is negative at `z_D`, and that convention D therefore has no
  positive-trace reading. **Convention D does not fail positivity** — its
  `H₃(q)` weights are positive semidefinite, signature `(5,0,1)`.
  Scope reclassified **(b) → (a)**.
- **Not retracted:** every numerical and Lean result. `1/2 − z_D < 0` for
  `q > 1` is true and sorry-free; the §6b identities, the `c₂`/`c₃`/`c₄…c₇`
  findings, and the genericity table are untouched.
- **Lean renamed** so the names describe what is proved:
  `threeRowMiddleWeight` → `ladderPhaseCoeff`,
  `threeRowMiddleWeight_neg_at_zD` → `ladderPhaseCoeff_neg_at_zD`,
  `threeRowMiddleWeight_pos_at_zC` → `ladderPhaseCoeff_pos_at_zC`,
  `threeRow_positivity_separates_zC_zD` →
  `ladderPhaseCoeff_sign_separates_zC_zD`. Statements and proof terms are
  byte-for-byte unchanged apart from the identifiers.
- **Re-verified after the rename:** `lean`-direct exit 0 against the
  pre-existing restored olean cache (6990 Mathlib oleans, **read-only** — no
  `lake build`, no second restore; count unchanged before and after).
  `#print axioms` on **all ten** declarations reports only `propext`,
  `Classical.choice`, `Quot.sound` — no `sorryAx`. Zero occurrences of
  `sorry` in the file.
- **Probe:** A7 relabelled from `y_(2,1)` to `κ(z) = 1/2 − z` (the
  arithmetic was always right; only the name was wrong), and **A7r** added
  as a retraction guard — it evaluates S2's closed forms at `q₀`, asserts
  the D weights are positive semidefinite, and asserts
  `κ(z_D) < 0 < y_(2,1)`, so the conflation cannot silently return.
  **18/18 → 20/20**, exit 0.
- **Cited, not re-derived:** S2's symbolic solve of the three defining
  conditions. A7r evaluates their published closed forms as a guard; it
  does not reproduce the solve.
- **Audit witnesses not committed.** Running the precision gate regenerates
  three tree-wide audit witnesses (`q0-anchor-consistency`,
  `witness-float64-padding`, `witness-raw-float64--docs-audits-scripts`)
  whose committed counts are stale for reasons unrelated to this branch —
  the offenders live in `computations/_deprecated/`. They were **reverted
  rather than committed**, as on the previous pass (bean `qou-pgdw`).
