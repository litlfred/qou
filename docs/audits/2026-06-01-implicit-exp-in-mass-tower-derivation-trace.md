# Implicit exp / exp_q in the mass-tower derivation — trace (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/hoefsmit-chi-lambda-q-evaluator-2026-06-01, PR #1630)
**Status:** DERIVATION TRACE — identifies where exp / exp_q / Φ_q appear in
the canonical chain, flags candidate gaps where a linear approximation
might lose exp structure. NO closure attempt, NO candidate-fishing.

## User-raised question (2026-06-01)

> "is the swing/oscillation due to missing cosh_q / sinh_q?"
>
> Clarification: "I meant more to go back to the derivation of the mass
> tower formula and the definitions based on non-abelian Stokes ... try
> to derive ... see where it comes out. With archimedean we are doing
> exp / exp_q somewhere ... trace it back/forwards"
>
> Further: "may be implicit (like doing the integral is essentially exp)"

## TL;DR

**Yes — exp IS implicit in the mass-tower formula via the quantum dilogarithm
Φ_q.** Per `per-braid-mass-tower.md`:

```
m(W) = |tr_M(W)| + Σ_n [ Σ Φ_q(|tr_M(ξ)|) + z² Σ Φ_q(|tr_M(ξξ')|) ]
```

`Φ_q` is the **Faddeev quantum dilogarithm**, which is the archimedean
realization of `exp(Li_2^q(...))` — literally an exponential at the categorical
level.

This trace identifies four candidate sites where the exp/Li_2^q structure
could be losing fidelity to the categorical chain in the current c_k
expansion of Q_β. Each is documented as a research direction, not a
candidate to wire.

## Derivation chain — where exp/exp_q/Φ_q appear

Per CLAUDE.md §Canonical derivation chain:

```
substrate q_0 → 𝐂 categorical action → Yekutieli non-abelian Stokes → 𝐇_n(q) Hecke
             → Wedderburn decomposition → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
             → confinement SDP → canonical T_w → Archimedean functor at q_0
             → MeV observables
```

### Site 1: Yekutieli non-abelian Stokes — implicit path-ordered exp

Per `yekutieli-stokes-remark.md`: the non-abelian Stokes theorem
(Yekutieli 2015) requires `c_1(Ad(A)) = c_2(Ad(A)) = 0` for the
non-abelian surface integral to be well-defined.

**Mathematical content**: the non-abelian surface integral of a flat
connection `A` is essentially a path-ordered exponential `P·exp(∫_S A)`
mapped to the Hecke algebra. The flatness conditions ensure path-
independence; the categorical volume `ε` is the well-defined result.

**Where exp is hidden**: the categorical volume `ε` is the BOUNDARY
VALUE of the path-ordered exp. When mapped via Wedderburn → Frobenius
pairing → tr_M, the exp structure becomes the χ_λ(W) characters — but
each χ_λ(W) is itself the trace of an ordered product of σ_i matrices,
which is the finite-dim representation of a path-ordered exp.

### Site 2: Φ_q (Faddeev quantum dilogarithm) in mass-tower formula

Per `per-braid-mass-tower.md`:

```
m(W) = |tr_M(W)| + Σ_n [ Σ_ξ Φ_q(|tr_M(ξ)|) + z² Σ_{ξ,ξ'} Φ_q(|tr_M(ξ·ξ')|) ]
```

**Φ_q is literally an exp**: per `_phi_q_util.py` docstring:

```
Φ_q(z) = ∏_{k≥1} (1 − q^{-k}·z)^{-1}
```

Taking logs:

```
log Φ_q(z) = -Σ_k log(1 - q^{-k}·z) = Σ_k Σ_n (q^{-k}·z)^n / n
           = Σ_n z^n · (1/n) · Σ_k q^{-k·n}
           = Σ_n z^n / (n · (q^n - 1))     [for |q| > 1]
           = -Σ_n z^n · q^n / (n · [n]_q)   [in [n]_q form, |q| > 1]
```

So **`log Φ_q(z) = -Li_2^q(-z·q)/q` or similar**, depending on sign conventions.
And `Φ_q(z) = exp(some Li_2^q-like function)`.

**Φ_q is the post-τ archimedean evaluation of `exp(Li_2^q(...))`** — the
user's intuition tracks exactly.

### Site 3: Q_β Taylor expansion — where the exp structure might LOSE fidelity

The Q_β ladder is currently expanded as:

```
Q_β(q) = Q_base · Π_{k≥2} (1 + c_k · u^k)
```

where `u = b·ℏ_q²` is small at q_0. Each factor `(1 + c_k · u^k)` is a
LINEAR expansion in `u^k` — NOT an exp.

**If the underlying mass-tower formula is actually structured as**:

```
Q_β(q) = Q_base · exp(Σ_k c̃_k · u^k)
```

then `Π (1 + c_k u^k)` is the LEADING-ORDER Taylor expansion of the exp,
losing higher-order cross-terms like `c̃_2 · c̃_3 · u^5`.

**Numerical test**: at q_proton, u = b·ℏ_q² ≈ 8.5 × 10⁻³. The exp vs `1+x`
difference is `x²/2 + x³/6 + ... ≈ x²/2 ≈ 3.6 × 10⁻⁵`.

For the c_3 deviation (-0.0693 in units of u^3 ≈ 6.1 × 10⁻⁷ at q_proton):

```
deviation in absolute units: -0.0693 · u^3 ≈ -4.2 × 10⁻⁸
(x²/2 of u): ≈ 3.6 × 10⁻⁵
```

The c_3 deviation magnitude (-0.0693 in units of u^3 = -4.2e-8 absolute)
is **~10⁻³ smaller** than the exp-vs-linear difference at u^2 order
(3.6e-5 absolute). So the linear-expansion-of-exp hypothesis is
inconsistent with the c_3 deviation at u^3 order — the exp/linear
difference is dominated by u^2 effects, not u^3.

**Verdict for Site 3:** even if the framework is doing linear-of-exp
somewhere, the c_3-level deviation (-0.0693) at u^3 is NOT explained
by it. The dominant exp-linearization error is at u^2 order, which
goes into c_2 — and c_2 = -1 IS the empirically observed Taylor-exact
value. So if c_2 is correct, the exp linearization isn't broken at
that level.

### Site 4: Markov trace per-block χ_λ(W) — Hoefsmit seminormal vs symbolic

Per `qbeta-per-block-paper-closed-forms.witness.json` (PR #1620 / #1630
context), the per-block character χ_λ(W) IS the trace of a product of
σ_i matrices in the Hoefsmit seminormal form. The σ_i matrices satisfy
the Hecke relation `(σ_i - q)(σ_i + q⁻¹) = 0`, whose eigenvalues are
q and -q⁻¹.

**The "exp" here**: a product `σ_1 σ_2 ... σ_n` of Hecke generators can
be re-expressed via the **Burau/Lawrence-Krammer or Wenzl** formulas,
which involve q-deformed exponentials of nilpotent matrices.

**If the framework's per-block χ_λ uses the standard Hoefsmit form** (which
it does, per `tools/pyhecke/python/pyhecke/syt_prefix_cache.py`), this
IS the correct categorical evaluation — no exp linearization.

So Site 4 is CORRECTLY handled. No gap.

## Where the actual gap might be

Taking sites 1-4 together:

- Site 1 (non-abelian Stokes) → correctly mapped to Hecke via Wedderburn
- Site 2 (Φ_q) → correctly used in mass-tower; Φ_q IS the exp
- Site 3 (Q_β linear-of-exp) → ruled out by u^2 vs u^3 magnitude analysis
- Site 4 (Hoefsmit χ_λ) → correctly handled

**Implication**: the c_3 near-match deviation is NOT a linear-of-exp
artefact at any of the four documented sites. The "implicit exp"
hypothesis (user-raised 2026-06-01) is structurally plausible but
doesn't explain the specific c_3 magnitude.

**The remaining open hypothesis**: the gap may live in HOW Φ_q is
specifically composed with tr_M in the mass-tower formula. Per
`per-braid-mass-tower.md`, the formula uses `Φ_q(|tr_M(ξ)|)` — i.e.,
Φ_q evaluated at the MODULUS of the Markov trace. This modulus operation
could lose phase information from the fibre Im(tr_M) (per PR #1616
fibre/observable framing). If tr_M(ξ) has a fibre Im part that gets
discarded by the |...| operation, the residual would show up at the
Φ_q evaluation level — a u^3+ effect in the c_k expansion.

**Connection to PR #1626 + #1630 finding**: the cross-anchor test
showed that the c_3 empirical "swing" is NOT structural q-dependence
at the 1e-8 anchor proximity. The "missing exp" might explain the
near-match magnitude (-0.07) but only if it operates at a Q_β-pipeline
level that the cross-anchor test doesn't probe.

## What this trace does NOT do

- ❌ Does NOT propose a c_k closure formula based on an exp/Li_2^q expansion
- ❌ Does NOT modify production wiring
- ❌ Does NOT support the "missing cosh_q/sinh_q" hypothesis (PR #1630 §
  scan found NO clean match among 16 cosh_q/sinh_q candidates)

## What it DOES add

- A documented trace of where exp/exp_q/Φ_q appear in the chain
- An explicit analysis ruling out u^2-vs-u^3 magnitude mismatch for the
  linear-of-exp hypothesis at Site 3
- A documented OPEN hypothesis: `|tr_M(ξ)|` modulus might be discarding
  fibre Im content (connects to PR #1616 framing)

## Anti-pattern guard

Per CLAUDE.md no-7th-ansatz discipline:

- ❌ DO NOT propose `Q_β = exp(Σ c̃_k u^k)` formula and re-fit c̃_k
  numerically — that's the 8th-ansatz trap
- ❌ DO NOT search for the "missing Φ_q correction" by candidate-
  matching c_3 ≈ -0.0693
- ❌ DO NOT promote the |tr_M| → exp(tr_M complex) hypothesis without
  a categorical derivation of where the complex tr_M comes from
- ✓ DO investigate the structural question of whether the mass-tower
  formula should be using `tr_M(ξ)` directly vs `|tr_M(ξ)|` (with phase),
  per the fibre/observable framing

## Files

- `docs/audits/2026-06-01-implicit-exp-in-mass-tower-derivation-trace.md` (this file)

## Cross-refs

- `content/quantum-observable-universe/quantum-observable-universes/yekutieli-stokes-remark.md` — non-abelian Stokes derivation
- `content/quantum-observable-universe/mass-theory/per-braid-mass-tower.md` — mass-tower formula with Φ_q
- `content/quantum-observable-universe/information-theory/q-exponential-taylor.md` — q-exponential definition
- `computations/_phi_q_util.py` — Φ_q archimedean util (post-τ)
- `computations/_li_2_q_util.py` — Li_2^q util (pre-τ, binding context)
- PR #1616 — Im(q) fibre/observable framing in CLAUDE.md
- PR #1620 — Hecke-natural form for sym(Δtr_M)
- PR #1626 — complex c_3 fibre diagnostic
- PR #1630 — Li_2^q × spectral cross-anchor completion + cosh_q/sinh_q scan
