# B/A error-budget framework

**Date:** 2026-04-27
**Branch:** `claude/b-over-a-std-block-matrices` (PR #442)
**Purpose:** explicit error-bound framework for the v3 / v4 binding-energy
predictions on PR #442, structured by Gröbner–Shirshov filtration depth and
jet-order scaling.

## Context

The published QOU mass formula is two parallel legs converging at a knot's
hyperbolic volume:

| Geometric leg (top-down) | Algebraic leg (bottom-up) |
|---|---|
| (1) categorical action of **C** on 𝒮 | (A) SDP confinement at q₀ + GB-filtration + jet order |
| (2) connection ∇ via Stokes | (B) canonical Hecke element T_w |
| (3) Frobenius pairing on End(𝒮_p) | (C) Markov trace tr_M(β) = Σ_λ y_λ χ_λ(β) |
| (4) Reeb-foliation density μ on S³\K | (D) Jones polynomial J_K(q) |
| (5) Vol_hyp(K) | (E) Vol_hyp(K) (volume conjecture) |

The two legs converge at Vol_hyp via the (borrowed) volume conjecture, then
B = ρ · m_e · Vol_hyp(T_w) where ρ is a structural integer prefactor.

The PR #442 v3 evaluator (`b_over_a_evaluator_v2.py` v3 logic) implements only
a fragment of leg (E) — abelianised crossing counts (n_pp, n_nn, n_pn) reduced
to NF in H₃, then `(E₀/A) Σ_λ w_λ log|Λ_λ^free / Λ_λ^nuc|`. This is **at most**
a Vol_hyp-asymptotic approximation of the canonical formula; it omits:

- The geometric leg entirely (no Vol_hyp computation, no Stokes-derived ∇).
- The structural ρ prefactor.
- GB-filtration page identifications (Terms 4–7).
- Wigner T-pairing corrections (T = 0 pn, T = 1 same-flavour).
- Chirality factor a_K (range [0.91, 1.21] empirically).
- Frobenius co-Casimir term m_e · Σ_λ 1/dim_q(V_λ).
- Joint-tower SDP feasibility selection.

This document bounds the residual — `B/A_v3 − B/A_AME` — that arises from
those omissions, in three tiers.

## Tier 1: closed-form bounds (no compute)

### 1.1  NF term-count bound

Working in H₃, the NF basis has |NF₃| = 3! = 6 elements
{γ, σ₀, σ₁, L₊, L₋, e⁻}. Any NF-reduced element has at most 6 terms.

Working in H_n for n large (e.g. level-3 atom braid, n = 3A), the NF basis has
n! elements — factorial blow-up. Diamond-lemma reduction is exponential in
word length in the worst case. For ⁴He (3A = 12) this is 479M; for ⁴⁰Ca
(3A = 120) the basis is astronomical.

**Bound on intermediate term-count growth during build_atom(Z, N) before NF
collapse:** at most 2^L where L is the word length being reduced (each
Hecke firing σ² → hσ + 1 doubles the active-term count before the next
reduction). Word length L = Z(Z-1)/2 + N(N-1)/2 + ZN ≈ A²/2.

For ⁴He: L = 6, intermediate cap 2⁶ = 64. Tractable.
For ¹²C: L = 66, cap 2⁶⁶ ≈ 7×10¹⁹. Marginally tractable with sparse rep.
For ⁴⁰Ca: L = 980, cap 2⁹⁸⁰ ≈ 10²⁹⁵. Intractable — confirms the v4
hung process at 16+ min.

**Implication:** v3 (H₃ abelianised) is forced by tractability; the canonical
chain at level 3A requires partition-by-partition (`atom_mass_partition.py`),
which costs Σ_λ dim(λ)² · L = polynomial in p(n) · L.

### 1.2  GB-filtration page-truncation tail bound

The Markov trace decomposes as

  tr_M = Σ_{ℓ ≥ 0} π_ℓ(tr_M)

over the Gröbner–Shirshov filtration (`prop:gb-spectral-sequence`,
`prop:e-infinity-page-identifications`). Truncation at level ℓ ≤ L gives a
geometric tail.

Each page-ℓ contribution scales as h^ℓ · z^(word length), where
- h = q − q⁻¹ ≈ 0.20906 at q₀ (Hecke amplitude),
- z = 1/(√q + 1/√q) ≈ 0.49932 at q₀ (Markov parameter).

**Conjectural bound** (to be verified empirically against
[`gb-filtration-jet-order.witness.json`](../folio-assistant/computations/gb-filtration-jet-order.witness.json)):

  ∥Σ_{ℓ > L} π_ℓ tr_M∥ ≤ C · h^(L+1) · z^A

with C an O(1) constant from the GB-filtration page structure.

Concrete numbers at q₀ for L = 5 (paper truncation point):
- h⁶ = (0.20906)⁶ ≈ 8.4 × 10⁻⁵
- z^A factor: ⁴He → 0.062, ¹²C → 1.5 × 10⁻⁴, ⁴⁰Ca → 6 × 10⁻¹³

So the page-truncation tail at L = 5 is bounded above by:
- ⁴He: ~5 × 10⁻⁶ · C  (tight)
- ¹²C: ~1.3 × 10⁻⁸ · C  (very tight)
- ⁴⁰Ca: ~5 × 10⁻¹⁷ · C  (meaningless — base prediction error swamps)

**Caveat:** this bound assumes h^ℓ scaling holds page-wise. Verification
requires reading the witness explicitly; deferred to Tier 2.

### 1.3  Jet-order scaling

Per `gb_filtration_jet_tracker.py` (commit `e81e9c12` on
`claude/mass-units-bridge-followups`), each Hecke firing increments jet order
by 1. So jet order ≤ word length L = O(A²).

**Bound:** the maximum jet order reached in `build_atom(Z, N)` is at most
ZN + Z(Z-1)/2 + N(N-1)/2 = Z(Z+N) + N(N-1)/2 (each crossing contributes
≤ 1 jet). For Z = N: max jet order = A²/2.

Empirical jet-order growth from the witness (Tier 2) tightens this.

## Tier 2: empirical bounds (from witnesses)

### 2.1  GB-filtration jet-order witness

[`folio-assistant/computations/gb-filtration-jet-order.witness.json`](../folio-assistant/computations/gb-filtration-jet-order.witness.json)
(commit `e81e9c12`, watched-branch only as of 2026-04-27): three test cases
with measured jet-order growth and Hecke-firing counts during NF reduction.

**Method:** read the witness's per-test {input_word, jet_order_max,
hecke_firings, page_distribution} fields; fit a power-law c · A^k or
exponential c · r^A to the page distribution; use the fitted growth rate to
bound v3's truncation error per (Z, N) input.

Status: witness file lives on the watched branch; cherry-pick into PR #442
follow-up commit, OR wait for it to merge to main.

### 2.2  Cross-witness sanity at q₀

Sister witnesses on origin/main that may be probed:
- `qbeta-gb-filtration-residues.witness.json` — per-level Markov-trace
  decomposition for proton/neutron.
- `gb-filtration-gauge-invariance.witness.json` — stratum partition gauge
  invariance proof.

These provide page-distribution data for ⁴He / level-3 nucleons but not for
heavier isotopes.

## Tier 3: residual structure decomposition

For each predicted (Z, N), decompose the residual

  res(Z, N) := B/A_v3(Z, N) − B/A_AME(Z, N)

into the chain steps v3 omits.

### 3.1  Frobenius co-Casimir

Term: m_e · Σ_λ 1/dim_q(V_λ) per atom.

For H₃: dim_q values are 1, [2]_q, 1.

  Σ 1/dim_q ≈ 1 + 1/[2]_q + 1 ≈ 2.497 at q₀

Times m_e ≈ 0.511 MeV: this term contributes ≈ 1.27 MeV per atom (NOT
per-nucleon; divide by A).

Per-nucleon contribution: ⁴He → 0.32 MeV/A; ¹²C → 0.11 MeV/A; ⁴⁰Ca → 0.032 MeV/A.

### 3.2  Term 7 (GB-filtration ℓ=5 shell correction)

Per `35a Term 7 only with universal m_e·8G — captures 6–25% of binding
(magic ⁴He highest)` (commit on `claude/mass-units-bridge-followups`):

- ⁴He (magic, A=4): captures ~25% of binding ≈ 1.77 MeV/A.
- A ≥ 5 (non-magic): captures 6–10% ≈ 0.5–0.8 MeV/A.

This is a **lower bound** on the Term 7 magnitude. v3 omits it entirely; the
bound contributes to the residual as a multiplicative-then-additive correction.

### 3.3  Wigner T-pairing

T = 0 pairing (active when Z = N): empirically ≈ 1.5–3 MeV/A for light
Z = N nuclei (⁴He, ¹²C, ¹⁶O, ⁴⁰Ca all magic Z = N → T = 0).

T = 1 same-flavour pairing (active when |Z − N| = 0 or 2): ≈ 0.5–1 MeV/A.

v3 omits both; bound by ≤ 3 MeV/A added.

### 3.4  Chirality factor a_K

Empirically observed range:
- D (²H): a_K ≈ 1.209
- T (³H): a_K ≈ 0.956
- ³He: a_K ≈ 0.956
- ⁴He: a_K ≈ 0.914

For A ≥ 5, a_K is a fitted parameter per knot type — bound it by the
observed range [0.91, 1.21]. Multiplicative factor on the per-nucleon mass.

v3's spectral term enters this multiplication uncontrollably.

### 3.5  Combined residual budget (illustrative)

For ¹²C (Z = N = 6, A = 12):

| Source | bound (MeV/A) |
|---|---:|
| Frobenius co-Casimir | +0.11 |
| Term 7 (lower) | +0.5 |
| Wigner T = 0 | +1.5 |
| Chirality (×0.91 to ×1.21 multiplicative) | (effective ±20%) |
| GB tail at ℓ > 5 (Tier 1.2) | <10⁻⁸ (negligible) |
| **Sum (additive lower bound)** | **+2.1** |

v3 prediction for ¹²C: B/A = 4.26 MeV. AME: 7.68 MeV. Residual: −3.42 MeV.

Residual budget accounts for **+2.1 MeV** of the 3.42 MeV gap (~61%); the
remaining 1.3 MeV (~39%) is unexplained by v3-omitted-but-known terms. That
remainder is the open structural gap the paper itself acknowledges (per
`b3499347 compute(coulomb): subtraction reveals structure -- gap is NOT EM`).

## Open items / TODOs

| # | Gap | Tier | Status |
|---|---|---|---|
| 1 | Reeb-density → Vol_hyp categorical-derivation witness | (geometric leg 4→5) | open |
| 2 | Volume conjecture (Kashaev/Murakami) — bridge between legs; not derived from QOU | (legs meet) | borrowed; structural |
| 3 | Joint-tower SDP not built (only fundamental-particle SDP exists) | (algebraic leg A) | open |
| 4 | Canonical Hecke T_w explicit only for ℓ ≤ 1 (electron, p, n); ⁶Li/⁷Li (n₀ = 18, 21) not derived | (algebraic leg B) | open |
| 5 | Structural ρ prefactor — ρ ∈ {1, 2} for ℓ ≤ 2; breaks at ρ = 5 for ⁶Li/⁷Li (volume-match observation, not derived) | (final step) | open |
| 6 | `rem:yekutieli-stokes-remark` referenced but no formal block; non-abelian Stokes step (geometric leg 2) not formalised | (geometric leg 2) | open |
| 7 | Push-forward to universal cover + Reeb-vortex measure (geometric step 3 → 4) has no formal block | (geometric leg 3→4) | open |
| 8 | Term 7 shell correction (GB ℓ=5) computed for ⁴He, open for A ≥ 5 | (algebraic leg) | open |
| 9 | `prop:knot-factor-frobenius-pairing` demoted to `conj:` in Track 5 (CLAUDE.md §3b propagation); needs review whether genuinely conjectural | (geometric leg 3) | review |
| Q | Is `(E₀/A) Σ w_λ log|Λ|` formula equivalent (as Vol_hyp asymptotic) to `B = ρ · m_e · Vol_hyp`? | formula consistency | awaiting answer |

## How this doc supports PR #442

The PR is now framed as a **diagnostic**: v3 represents the abelianised-counts
H₃ ceiling. The error budget above bounds how far below the canonical chain v3
sits, and explicitly lists which omitted contributions are responsible for the
residual.

When the canonical chain is fully formalised (gaps 1–9 closed), a v5
implementation against the canonical pipeline can be benchmarked against this
budget — every additional MeV of residual reduction should correspond to one
of the chain steps reactivating.
