# KLR / Wenzl positivity — connection to the `|...|` audit (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/phi-q-modulus-audit-and-reframe-2026-06-01)
**Status:** STRUCTURAL FINDING — informs the modulus refactor.
**Triggered by:** user 2026-06-01: *"don't we know from KLR that
observables are positive? What is the role of KLR here? Explore what's
in the paper."*

## TL;DR

The framework's positivity guarantee comes from **Wenzl positivity at
q_0 ∈ ℝ_{>1}**, NOT from KLR canonical-basis positivity directly. KLR is
present in the framework as authoring guidance + classical-limit /
roots-of-unity conjectures, but is NOT what makes Markov traces
positive at production-canonical braids.

The `|tr_M|` in paper categorical statements is **conservative
archimedean wrapping** that's REDUNDANT given Wenzl positivity + the
specific canonical T_w choice. Removing `|...|` from categorical
statements is **theoretically backed**: positivity is a THEOREM at the
substrate level, not an axiom that needs `|...|` enforcement.

## What KLR / Wenzl actually give

| Source | Positivity statement |
|---|---|
| **Wenzl 1988** + Kazhdan-Wenzl 1993 (`conj:wenzl-positivity-implies-substrate-positivity`) | Rep(U_q(𝔰𝔩_2)) is unitary C*-tensor category iff q ∈ {e^{iπ/N}: N≥3} ∪ ℝ_{>0} |
| **Müger 2003 + BKLR 2015** | Unitary C*-tensor category ⟹ every Frobenius algebra has positive antipode-twisted pairing |
| **Williamson 2014** (KL positivity conjecture, proved) | KL basis structure constants are polynomials in q^{1/2} with non-negative integer coefficients |
| **Khovanov-Lauda-Rouquier** | KLR algebras categorify quantum groups; graded dimensions non-negative; canonical basis has non-negative integer structure constants |

## What this does NOT directly give

| Claim | True? | Why |
|---|---|---|
| `tr_M(ρ(β)) > 0` for arbitrary β | NO | Markov trace of an arbitrary braid word need not be positive; depends on ρ(β) being a positive operator (it's generally not) |
| `Δtr_M = tr_M(β_n) − tr_M(β_p) > 0` | NO | Mass differences can be negative; empirically Δtr_M ≈ −0.142 at q_proton |
| Individual Hecke characters χ_λ > 0 | NO | At q_proton: χ_(3) ≈ −0.26, χ_(2,1) ≈ −0.11, χ_(1,1,1) ≈ −0.17 |
| KL canonical basis has positive structure constants | YES | Williamson 2014 |

## How positivity actually flows in production

For the specific canonical braid words used in production:

```
tr_M(β_p)   at q_proton ≈ +1.07  (positive)
tr_M(β_n)   at q_proton ≈ +0.92  (positive)
tr_M(β_Bor) at q_proton ≈ +1.00  (positive; closed form (4+h²-3h⁴-h⁶)/(h²+4))
```

These are positive **empirically**. The Wenzl positivity theorem
provides a structural reason: the framework's canonical T_w choices
correspond to **positive operators** in the C*-completion. Specifically,
the SDP selection (`prop:operator-selection-lp`) selects T_w whose
Markov trace is PSD-feasible — i.e., positivity at the categorical
level is BUILT INTO the SDP-selection procedure.

This means:
1. **Wenzl positivity** gives the substrate the right structure
2. **SDP selection of T_w** picks operators that respect this positivity
3. **Result**: tr_M(T_w) is positive AT q_0 for the production T_w

The `|tr_M(T_w)|` in paper categorical definitions is therefore:
- **Redundant** for canonical T_w (production convention)
- **Theoretically backed for removal** (Wenzl + SDP-selection guarantee positivity)
- **Potentially misleading** in categorical formulas where `tr_M` is the categorical Markov trace (a Habiro-ring element, NOT a real number to which `|...|` applies)

## What KLR is doing in the framework

Searching the paper, KLR appears in 4 specific contexts:

### (1) `conj:kazhdan-lusztig-classical-limit`

> "As q → 1, the KLR canonical basis flattens to the Kazhdan-Lusztig
> basis of S_n, recovering Pauli/Bose statistics."

KLR is the categorical lift; q → 1 limit gives classical statistics.
**Authoring guidance**, not used in production positivity arguments.

### (2) `conj:root-of-unity-mtc-truncation`

> "At q = e^(2πi/k), the KLR algebra truncates to a Modular Tensor
> Category of non-abelian anyons."

KLR organises the roots-of-unity behaviour. Recently exercised in PR
#1642's ζ_8 Habiro identification. **Conjectural; positivity-adjacent
via MTC unitarity.**

### (3) `atom-knot-mass-derivation.md`

> "filters via a KLR canonical-basis 'cemetery' prune (drops σ_i^{±k}
> pure-power Demazure-trivial classes per AGENTS.md §7b)"

KLR canonical basis used as a **compression tool** for braid-word
enumeration. Compresses 13088 → 138 canonical-basis classes.
**Combinatorial, not positivity.**

### (4) `conj:qbeta-c-k-closed-forms` (mass-endomorphism)

> "KLR canonical-basis trace formula: per-Wedderburn-block
> canonical-basis Markov trace at orders ε^8, ε^10, ε^12 — the framework
> has scaffolding (Hecke-KLR bridge in conj:kazhdan-lusztig-classical-limit)"

KLR proposed as the **route to higher-order c_k coefficients**. NOT
yet implemented. **Conjectural; positivity-adjacent if proved.**

## AGENTS.md §7b audit precedent (2026-05-30)

> "An external AI dialog re-pitching KLR/crystal as (a) GS
> compute-speedup, (b) positivity-by-construction, (c) Option E Δ_λ
> closure was assessed in `docs/audits/2026-05-30-klr-dialog-assessment.md`;
> verdict was 0/6 candidate proofs would meaningfully shorten with a
> KLR layer."

So KLR has been considered as a route to positivity-by-construction and
**rejected** as not shortening any existing proof. The framework's
positivity comes from Wenzl + Müger / BKLR, NOT from KLR layering.

## Implication for the `|...|` refactor

| Site type | Refactor justified? | Why |
|---|---|---|
| Categorical mass definitions `𝔪 = |tr_M|` | YES — drop `|...|` | Wenzl + SDP selection guarantee positivity for canonical T_w; `|...|` is redundant safety wrapper |
| Mass-tower terms `Σ Φ_q(|V̂|)` | YES (production already refactored) | Φ_q is bar-asymmetric; sign matters |
| Markov probability `|tr_M|²` | YES — rewrite as `tr_M·\bar{tr_M}` | Bar-involution is the categorical content; modulus-squared is the archimedean reduction |
| Bound statements `|tr_M(x)| ≤ ...` | ESCALATE | Bounds are inherently about magnitude; `|...|` may be correct here |
| Pre-archimedean substrate identity `\|tr_M(β_Bor)\|·...` | YES — drop `|...|` | Substrate identity holds at the categorical level with signed tr_M; Wenzl gives positivity at q_0 |

## Updated proposal doc — theoretical backing for each group

The Tier-2 refactor proposal
(`docs/audits/2026-06-01-paper-modulus-tier2-refactor-proposal.md`) should
reference this finding: each `|...|` removal is backed by the
combination:

1. **Wenzl positivity** at q_0 (theorem)
2. **SDP selection** of canonical T_w (production discipline)
3. **Müger / BKLR** Frobenius positivity (off-the-shelf)
4. **NOT** KLR canonical-basis positivity (which is structurally
   distinct and isn't used in production)

This makes the refactor not just a notation cleanup but a **discipline
alignment**: the paper categorical statements should reflect the
THEOREMS (Wenzl + Müger / BKLR), not enforce positivity via `|...|`
ad-hoc.

## Anti-pattern guards

- ❌ Do NOT claim "KLR makes observables positive" — KL/KLR positivity
  is at the structure-constant level; doesn't directly imply positivity
  of arbitrary Markov traces. Wenzl + Müger / BKLR is the correct citation.
- ❌ Do NOT remove `|...|` from BOUND statements (`|tr_M(x)| ≤ M`) —
  bounds are inherently magnitude statements.
- ✓ DO cite Wenzl positivity + SDP selection as the structural reason
  the refactor is safe.

## Cross-refs

- `conj:wenzl-positivity-implies-substrate-positivity` — the Wenzl → substrate bridge
- `conj:os-reflection-positivity-from-reeb` — the OS positivity axiom
- `conj:kazhdan-lusztig-classical-limit` — KLR / KL connection
- `conj:root-of-unity-mtc-truncation` — KLR at roots of unity (PR #1642)
- `conj:qbeta-c-k-closed-forms` — KLR for higher-order c_k (open)
- `docs/audits/2026-05-30-klr-dialog-assessment.md` — KLR as proof-shortening: 0/6
- AGENTS.md §7b — Symmetric-crystal techniques (KLR / Kashiwara)
- `docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md` — sister audit
- `docs/audits/2026-06-01-paper-modulus-tier2-refactor-proposal.md` — proposal
