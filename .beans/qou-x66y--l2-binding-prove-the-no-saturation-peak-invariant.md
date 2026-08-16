---
# qou-x66y
title: 'L2 binding: prove the no-saturation-peak invariant for the additive per-bond chain (upgrade probe_collective_binding_residual''s near-proof to Lean)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T10:10:00Z
updated_at: 2026-08-11T10:10:45Z
---


## DONE (2026-08-11) — proved, and the exclusion bites

`computations/probe_collective_binding_residual.py` argued at "near-proof level"
that the additive per-bond chain has "no mechanism to produce a saturation PEAK".
That argument narrows the whole collective-binding search, but AGENTS.md
§"Before declaring refuted" allows a scope-(b) exclusion only on a **proved**
invariant. It was not proved. Now it is.

`QOU/MassTheory/ChainBindingNoSaturationPeak.lean` (sorry-free, 3 theorems):

* `chainPerNucleon_eq_hyperbola` — along any isobaric chain (`d = N − Z` fixed),
  `B_sym(A)/A = c₁ + c₂/A` **exactly**, with
  `c₁ = α(L_pp+L_nn)/2` **independent of `d`** and all the `d`-dependence in `c₂`.
  An identity, discharged by `ring`.
* `hyperbola_no_interior_max` — `c₁ + c₂/A` is monotone on `A > 0`, so never
  exceeds both neighbours.
* `chain_no_saturation_peak` — hence no saturation peak, for **any** `α`,
  per-bond constants, or isospin excess.

The `d`-independence of `c₁` is what makes it a real exclusion rather than an
artifact of looking along `N = Z`: every isobaric chain is a hyperbola with the
*same* asymptote.

### Measured, not asserted (`chain_binding_hyperbola_no_peak_probe.py`, exit 0)

* Production `B_sym` **is** the hyperbola: worst |diff| **4.44e-16** over
  2H/4He/6Li/12C/16O/24Mg/40Ca. So the theorem is about the right object, not an
  idealization of it.
* Measured `B_AME/A` peaks at **⁵⁶Fe, 8.7904 MeV** — interior, as required.
* Chain asymptote **c₁ = 2.9242 MeV/nucleon**: the chain is **3.01× low even at
  its own A→∞ limit**.

That last number sharpens the standing framing. The missing collective term is
not only responsible for the *shape* (the peak) but for ~2/3 of the *magnitude* —
the chain cannot reach the plateau even asymptotically.

### Scope

Scope-(b), narrow. Excludes additive per-bond-type sums with constants fixed
along an isobaric chain **as the source of the peak**. Does NOT exclude the chain
as an additive contribution (AGENTS.md permanence principle 1 — an inaccurate
total does not invalidate a proved per-bond factor), nor `A`-dependent per-bond
constants, nor say anything about the magnitude of the missing term. Nothing
fitted; the Δ_λ "no seventh ansatz" gate untouched.

## Step (D) scoped (2026-08-11) — and materially weakened

Measured both Plancherel expectations directly, k=3..12:

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|----|----|----|
| a/b | 4.00 | 2.20 | 2.17 | 2.21 | 2.11 | 2.07 | 2.06 | 2.07 | 2.06 | 2.04 |

with `a = w_std = 𝔼[f^{λ/(2,1)}]`, `b = 𝔼[f^{λ/(3)}]`. The ratio converges to
**2 = f^{(2,1)}/f^{(3)}**, consistent with `f^{λ/μ} ≈ f^λ·f^μ/|S₃|` for
Plancherel-typical λ.

**(D) is NOT the cheap sub-goal the script implies.** It is *false pointwise*: at
a single-row `λ = (k)`, `f^{λ/(3)} = 1` while `f^{λ/(2,1)} = 0`. So no
tableau-by-tableau argument can give it — it is genuinely measure-theoretic, and
that is exactly the Mathlib gap `LevelSelectionLogarithmic.lean` names.

**But sharp (D) is not needed.** `cube_moment_le_of_ratio_bound` (sorry-free):
for **any** `ε > 0`, `ε·b ≤ a` gives `a ≥ (ε/(2(1+ε)))·T`. Since `T` is
super-exponential by `sum_sq_pow_three_le`, so is `a` — the constant is
irrelevant to the growth conclusion. Sharp (D) is `ε = 1` giving `T/4`; `ε = 1/100`
would do just as well.

So the target for the literature is **"a ≥ εb for some explicit ε > 0"**, not
`a ≥ b`, with a measured margin of >2×.

### Literature (answering "need lit?": yes, for (D))

The regime is *fixed μ, |λ| → ∞*, which is the studied one:
- Morales–Pak–Panova, *Asymptotics of the number of standard Young tableaux of
  skew shape*, arXiv:1610.07561 — "no multiplicative formula for `f^{λ/μ}`;
  asymptotics known for few special families and **for fixed μ**".
- Morales–Pak–Panova, *Asymptotics for skew standard Young tableaux via bounds
  for characters*, arXiv:1710.05652 — character-bound route, the one that would
  give explicit constants.
- Biane / Śniady (asymptotic factorization, normalized characters) — the
  machinery behind both.

**Caveat for the Lean.** An asymptotic theorem plus a finite check (k≤12) leaves
a gap in the middle. What closes it is an *explicit-constant* bound valid for all
k ≥ some k₀ small enough to meet the finite check — which is why the
`ε`-weakening above matters: it is far easier to get a crude explicit constant
than a sharp asymptotic.

## CORRECTION (2026-08-11) — the lit recommendation was wrong; the corpus already reduced (D)

I recommended pulling Morales–Pak–Panova for step (D). **Not needed.**
`docs/audits/2026-07-18-deltalambda-D-reduction-content-covariance.md` already
reduces (D) rigorously, and more cleanly than the skew-asymptotics route:

    f^{λ/(2,1)} = (f^λ − χ₃)/3 ,   f^{λ/(3)} = (f^λ + 3χ₂ + 2χ₃)/6
    T₂ = 0 exactly (conjugation)
    (D) ⟺ 4·T₃ ≤ T₁ ⟸ T₃ ≤ 0 ⟺ Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0

via `S_k` characters + the Jucys–Murphy content formula. Every step an identity.

**Independent cross-validation.** Recomputing `ε = 2(1−c)/(1+2c)` from the
*character* route reproduces the ratios I had measured by *direct skew-tableau*
enumeration, digit for digit: 4.0000, 2.2000, 2.1702, 2.2070, 2.1115, 2.0697,
2.0649, 2.0703, 2.0578, 2.0435 (k=3..12). Two independent routes agreeing
confirms the audit's identities.

**And the covariance inequality is more than is needed.** Combining the audit's
reduction with `cube_moment_le_of_ratio_bound`: any `c < 1` with `T₃ ≤ c·T₁`
gives `ε = 2(1−c)/(1+2c) > 0`, which is all the growth conclusion consumes.
Bridge proved sorry-free as `ratio_bound_of_T3_le`.

Slack: measured `T₃/T₁` runs **−0.200 → −0.007** (k=3..12) against a requirement
of merely `< 1`. Two orders of magnitude at k=12.

**What is actually left.** The trivial character bound `|χ^λ(3-cycle)| ≤ f^λ`
already gives `T₃ ≤ T₁`; only a *quantitative* gap below 1 is missing. The
extremal shapes cannot obstruct it: `λ=(k)` and `λ=(1ᵏ)` are the only ones
attaining ratio 1 (checked: the JM formula gives exactly 1 at `λ=(k)`), and they
have `f^λ = 1`, contributing `±1` against a super-exponential `T₁`. So the
remaining step is a finite/extremal estimate, not a covariance theorem and not a
literature import.

## The explicit c < 1 (2026-08-11) — one combinatorial claim from closing (D)

`ratio_bound_of_T3_le` needs `T₃ ≤ c·T₁` with `c < 1`. The **extremal split**
supplies it, and the key realisation is that `c` may depend on `k`: `T₁` is
super-exponential, so a polynomially-decaying margin is absorbed without loss.

Only two shapes reach `r(λ) = χ^λ(3-cycle)/f^λ = 1` — the single row `(k)` and
single column `(1ᵏ)` — and **both have `f^λ = 1`**, so they contribute mass `M = 2`
against a super-exponential `T₁`. Off them, `r` is maximised at `(k−1,1)` with

    ρ = 1 − 3/(k−1)     exactly

(the `Σ_□c(□)²` gap against the single row is exactly `(k−1)² − 1`). Verified
k=4..13 in `computations/probes/wstd_extremal_split_probe.py` (exit 0), which also
cross-checks the character route against direct skew-tableau enumeration.

Lean (sorry-free): `T3_lt_of_extremal_split`, `T3_le_explicit_c` — any `ρ < 1` and
`M < T₁` give `T₃ < T₁` with explicit `c`. Chains into `ratio_bound_of_T3_le`
(`ε = 2(1−c)/(1+2c) ≍ 4/(3(k−1))`) then `cube_moment_le_of_ratio_bound`.

### The one remaining input

That `Σ_□ c(□)²` is **maximised over non-extremal shapes at `(k−1,1)`**. Verified
to k=13; **not proved**. This is a statement about content sums of partitions —
far weaker and more tractable than the covariance inequality the audit reduced
(D) to, and it needs no Plancherel measure at all.

### Chain status

| step | status |
|---|---|
| (A) branching identity | corpus, exact |
| (B) Plancherel identity, `T₂ = 0` | corpus, exact |
| (C) cube-moment bound | **Lean, sorry-free** (`sum_sq_pow_three_le`) |
| (D) transfer | reduced to `C₂`-maximality; algebra **Lean, sorry-free** |
| RSK/Burnside `Σ(f^λ)² = k!` | open (`RSKBurnsideTarget.lean`) |
| `TowerGeometricLowerBound` instance | still none |

The "multi-session Mathlib build" estimate now looks like two concrete
combinatorial lemmas, not an infrastructure programme.
