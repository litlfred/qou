# Audit: ξ_2 reconciliation — retract the "ξ_2 = 0" closure to OPEN

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Supersedes.** [`2026-05-31-casimir-xi-2-equals-zero.md`](2026-05-31-casimir-xi-2-equals-zero.md)
**Witness.** [`casimir-xi-2-dig-deeper.witness.json`](../../computations/casimir-xi-2-dig-deeper.witness.json)
**Result.** **ξ_2 is OPEN, gated on the N_⊙ construction (sub-problem 1).** The
"ξ_k = 0 because Casimir isn't Hecke" closure is **retracted** — it is the third
reversal of a flip-flop and contradicts the conjecture block's own framing.

## The flip-flop this audit closes

The ξ_2 substrate-correction coefficient reversed sign-of-claim three times
inside PR #1540:

| # | Commit | Claim | Argument |
|---|---|---|---|
| 1 | `b1f467f5c` | `ξ_k = 0` | ε ∝ ℏ_q² calibration cancels q |
| 2 | `ac3fae543` | `ξ_odd = 0` only; `ξ_{even≥2}` **OPEN** | bar-symmetry kills only odd ranks; retract #1 as overreach |
| 3 | `665aa7eb1` | `ξ_k = 0` (again) | "Casimir doesn't go through Hecke at any order" |

This is exactly the wire/un-wire flip-flop pattern that AGENTS.md flags for the
Q_β `c_k` saga. Per the repo's anti-flip-flop discipline, the correct response is
not a fourth claim but a **structural settlement** of why the coefficient keeps
flipping.

## The contradiction step 3 introduced

The step-3 closure ([`casimir-xi-2-equals-zero.md`](2026-05-31-casimir-xi-2-equals-zero.md))
asserts:

> "The Casimir effect derivation in QOU is purely geometric — it does not use the
> Hecke-algebra structure of QOU at any order. … Casimir doesn't go through Hecke
> at any order. No q-deformation."

But the conjecture block
([`casimir-epsilon-vacuum.md`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md))
frames the very same quantity *through* Hecke:

- `N_⊙ = −(π²/720)·(A/d³)·ℏ²_q·ℏc·ε⁻¹` — carries the substrate-Planck `ℏ²_q`;
- the `ℏ²_q` is "forced by dimensional consistency with the Hoefsmit normalisation
  `Geom_ε(L) = Vol(L)/ℏ²_q · linking_weight(L)`";
- **sub-problem 3**: *"The QOU analogue would be a Hecke-trace identity … derivable
  from the Markov-trace structure on H_n(q) at the plate-boundary representation."*

The closure and the conjecture cannot both be right: one says Casimir never touches
Hecke, the other says the prefactor *is* a Markov trace on `H_n(q)`.

## What the dig-deeper probe actually shows

`casimir_xi_2_dig_deeper.py` evaluates the two canonical trace functionals on the
Wenzl `y_λ(q)` weights at substrate. The value of ξ_2 is **entirely determined by
which functional N_⊙'s mode-count is** — i.e. by the (unconstructed) N_⊙ object.

### Reading 1 — normalized Markov trace of the identity

$$
\mathrm{tr}_M(1)\big|_{H_n} \;=\; \sum_{\lambda \vdash n} y_\lambda(q)\,\dim V_\lambda \;\equiv\; 1
\qquad \text{for ALL } q.
$$

Verified across `q ∈ {1.05, q_0, 1.3, 1.7, 2.0}`: deviation from 1 is `2.7×10⁻⁵¹`
(machine zero). This is just the **Wenzl normalization** — the normalized trace of
the identity is always 1.

→ ξ_k = 0 under this reading, **but tautologically**. It carries no Casimir-specific
content: *any* normalized trace of *any* identity is 1.

### Reading 2 — unnormalized weight sum

$$
\sum_{\lambda \vdash n} y_\lambda(q)
$$

is q-dependent, and its **relative h²-coefficient grows with n** (number of
strands / modes):

| n | rel. h²-coef of Σ y_λ |
|---|---|
| 2 | 0.00 |
| 3 | −0.94 |
| 4 | −2.23 |
| 5 | −3.79 |
| 6 | −5.51 |
| 7 | −7.20 |

A divergent, n-dependent ξ_2 is **physically inadmissible** for a single observable.
So the naive "prefactor = Markov trace on `H_n(q)`" route (sub-problem 3) does **not**
yield a finite ξ_2 without ζ-regularization across the mode tower — and ζ-regularization
is precisely the q-independent step (standard analytic continuation, no q-deformation).

### The earlier survey numbers are not reproducible

The 5-source survey reported `tr_M(1)` ≈ 0.9946, 0.9839, 0.9680, 0.7510 (n=2..5).
These match **neither** canonical functional (Σ y_λ·dim ≡ 1; Σ y_λ = 0.72, 0.51, 0.31…).
Internally they fit `−0.123·C(n,2)` for n=2,3,4 (coef/C(n,2) = −0.124, −0.123, −0.122),
with n=5 (−0.57) an outlier breaking the fit. A closure should not be anchored on
numbers that cannot be reproduced from canonical primitives.

## Why step 1 was also not a derivation

[`casimir_beta_2_derivation.py`](../../computations/casimir_beta_2_derivation.py)
imposes the calibration `ε = ε_0·ℏ_q²` *by hand* so the `1/ℏ_q²` in `Geom_ε` cancels.
That is circular: the calibration is chosen to produce the cancellation. It is an
assumption about N_⊙, not a derivation of ξ_2.

## The honest invariant

| Coefficient | Status | Source |
|---|---|---|
| `ξ_0` | **= 1, derived** | rank-0 / tree-level mode count |
| `ξ_odd` | **= 0, derived** | bar-symmetry (q ↦ q⁻¹) projects away odd ranks |
| `ξ_{even ≥ 2}` | **OPEN** | gated on the N_⊙ construction (sub-problem 1) |

"ξ_2 = 0" is defensible **only** as the content-free Reading 1 (normalized trace of
identity ≡ 1). The moment N_⊙ carries any Casimir-specific, unnormalized mode
weighting, q-dependence returns. Until N_⊙ is constructed and its trace functional
fixed, ξ_2 cannot be derived — in either direction.

## Action taken

1. `casimir_xi_2_dig_deeper.py` + witness added (this audit's evidence base).
2. [`casimir-xi-2-equals-zero.md`](2026-05-31-casimir-xi-2-equals-zero.md) marked
   **SUPERSEDED** with a banner pointing here.
3. Conjecture block status unchanged — it already reads **Open** and frames
   sub-problems 1–3 as open; the closure audit doc was the overreach, not the block.

## What WOULD settle ξ_2 (unchanged from the survey)

A construction of `N_⊙(A,d)` that maps each plate mode to a specific Wedderburn block
of a specific `H_n(q)`, fixing the trace functional. Whether the resulting ζ-regularized
mode sum is q-independent (→ ξ_2 = 0) or retains an h² correction (→ ξ_2 ≠ 0) is then a
computation, not a choice. This is sub-problem 1, and it remains open.
