# The "A ≈ 4 carrier saturation crossover" — structural origin found: the carrier was never extensive (R4-b)

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FORMALIZE-FIRST derive-or-refute of the saturation datum reported by
the ⁶Li discriminator
([`2026-07-13-li6-h18-amplification-discriminator.md`](2026-07-13-li6-h18-amplification-discriminator.md) §5 item 2).
**No fit, no tuning, no wiring.**
**Probe:** [`computations/deltalambda/carrier_saturation_mechanism_probe.py`](../../computations/deltalambda/carrier_saturation_mechanism_probe.py)
(witness `carrier-saturation-mechanism.witness.json`, 9/9 assertions, wall 4.2 s — all inputs cached, no new tr_M compute).

## 1. The question as posed — and the formalize-first answer

The discriminator audit reported that the θ_λ carrier
`S(A) = Σ_λ y_λ·dim_λ·|Δθ_λ|` "grows geometrically to A = 4 then flatlines
at m_e·S ≈ 0.40–0.45 MeV", and asked which mechanism: (i) |Δθ_λ| shrinking,
(ii) Markov weight concentrating on Δθ ≈ 0 blocks, or (iii) cancellation.

The one-line structural argument (compute-author §3.3, found **before** the
per-λ numerics) dissolves the premise:

> **The carrier weights are exactly the Markov-trace normalization weights.**
> [`prop:wedderburn-trace-identity`](../../content/quantum-observable-universe/mass-theory/wedderburn-trace-identity.md)
> (corpus, Lean-backed) states `Σ_λ y_λ·d_λ = tr_M(1) = 1` with
> `d_λ = f^λ` — the same `w_λ = y_λ·dim_λ` the carrier uses. Hence
> `p_λ := y_λ·dim_λ` is a **probability distribution** over the Wedderburn
> blocks and
>
> $$S(A) \;=\; \sum_\lambda p_\lambda\,|\Delta\theta_\lambda| \;=\; \mathbb{E}_p\!\left[\,|\Delta\theta|\,\right]$$
>
> is a probability-weighted **mean** of per-block Reeb phase displacements —
> an **intensive, bounded** quantity (|Δθ_λ| ≤ π on rotation-channel
> blocks). It structurally cannot grow with A. **There is no growth to
> saturate.**

Machine check: `max |Σ p_λ − 1| = 5.3×10⁻⁵¹` across all six atoms
(D, T, ³He, ⁴He, ⁵Li, ⁶Li) from the cached 50-dps witnesses.

## 2. Premise correction — the carrier was flat the whole time (parent-table erratum)

Recomputing m_e·S(A) per-λ from the same cached witnesses the discriminator
used:

| atom | A | blocks | **m_e·S recomputed (MeV)** | R3-b table printed | E_p[\|Δθ\|] (rad) | 𝒜 = B/(m_e·S) |
|---|--:|--:|--:|--:|--:|--:|
| D | 2 | 11 | 0.3681 | 0.36 | 0.7204 | 6.043 |
| T | 3 | 30 | **0.4466** | ~~0.22~~ | 0.8740 | 18.990 |
| ³He | 3 | 30 | **0.3877** | ~~0.19~~ | 0.7587 | 19.909 |
| ⁴He | 4 | 77 | 0.4488 | 0.449 | 0.8782 | 63.051 |
| ⁵Li | 5 | 176 | 0.4078 | 0.408 | 0.7981 | 64.563 |
| ⁶Li | 6 | 385 | 0.4006 | 0.401 | 0.7840 | 79.858 |

The discriminator table's T/³He m_e·S entries (0.22 / 0.19) are **errata** —
inconsistent with that audit's own 𝒜 column (B_AME/𝒜 = 0.4466 / 0.3877,
reproduced here to 4 digits; probe assertion
`erratum_T_me_S_matches_A_column`). The 𝒜 column, the verdict, and every
downstream conclusion of R3-b are **unaffected** — only the impression of a
"geometric carrier ramp to A = 4" was an artifact of those two entries.

**Corrected datum: the carrier is FLAT across the entire range** —
m_e·S ∈ [0.368, 0.449] MeV for A = 2..6 (max/min = 1.219, non-monotonic).
It never grew geometrically; a ramp matching the 𝒜 law would have required
max/min ≥ 2.4 by A = 4.

## 3. Mechanism verdicts (per-λ decomposition, all from cached data)

| candidate mechanism | verdict | evidence |
|---|---|---|
| (i) per-block \|Δθ_λ\| collapse (atom/free convergence) | **NO** as the driver of the 𝒜 crossover | E_p[\|Δθ\|] stays order-unity (0.72–0.88 rad) at every A; no collapse at A ≥ 5. (The *unweighted* block mean does fall, 0.67 → 0.20 rad — but the weighted mean, which is what S is, does not.) |
| (ii) weight concentration on Δθ ≈ 0 blocks | **NO** | corr(p_λ, \|Δθ_λ\|) is **positive** at every A (+0.78 at T, +0.59 at ⁴He, +0.12 at ⁶Li): the Markov weight sits preferentially on *larger*-than-typical \|Δθ\| blocks — the opposite of (ii). Weighted mean > unweighted mean for all A ≥ 3. |
| (iii) cancellation | **N/A** | S sums \|Δθ\|; no signed cancellation across blocks is possible. |
| **(iv) NORMALIZATION (the actual mechanism)** | **YES — derived** | `Σ p_λ = 1` exactly (corpus proposition, machine-checked ≤ 5.3e-51): S is an intensive bounded mean. The geometric ramp and the A ≈ 4 crossover of 𝒜(A) live **entirely in the numerator B_AME**. |

**The 𝒜-step factorization** (𝒜step = Bstep / Sstep, per added nucleon)
localizes the crossover:

| step | B-step | S-step | 𝒜-step |
|---|--:|--:|--:|
| D→T | 3.813 | 1.213 | 3.143 |
| T→⁴He | 3.336 | 1.005 | 3.320 |
| ³He→⁴He | 3.666 | 1.158 | 3.167 |
| **⁴He→⁵Li** | **0.931** | 0.909 | 1.024 |
| **⁵Li→⁶Li** | **1.215** | 0.982 | 1.237 |

The ×3.2/nucleon "geometric law" of R2-d/R3-b was, at ≥ 85 % of its
magnitude, **the experimental binding curve itself** (B-steps 3.3–3.8 up to
the α particle, collapsing to 0.93–1.22 past it — the α-peak /
B/A-saturation onset), lightly modulated by an order-unity carrier. The
"crossover at A ≈ 4" is the AME curve's own alpha peak observed through a
structurally flat denominator.

### Which λ dominate

Top-5 blocks carry 67–99 % of S. The dominant contributors are the
near-three-row balanced shapes adjacent to the maximal-p_λ blocks: D
`[4,2]` (68 %); T `[6,3]`+`[7,2]`+`[6,2,1]`; ⁴He `[8,3,1]`+`[7,4,1]`+`[8,4]`;
⁵Li `[9,5,1]`+`[10,4,1]`+`[9,4,2]`; ⁶Li `[10,6,2]`+`[11,5,2]`+`[11,6,1]`.
Participation N_eff stays small (3.8–7.6 effective blocks out of up to 385):
the Markov distribution p_λ concentrates on a thin band of shapes near
λ ≈ (n·0.55, n·0.31, n·0.14), and both p and \|Δθ\| stabilize there —
the (p_λ, \|Δθ_λ\|) joint law converges up the Hecke tower
(E_p[\|Δθ\|] = 0.878 → 0.798 → 0.784 rad at A = 4, 5, 6). The
growth-channel share of S decays smoothly (0.79 → 0.22 from D to ⁶Li), so
the bounded rotation channel increasingly dominates the mean.

## 4. Corpus-structure match

- **The carrier side (flat) is the Wedderburn/Markov normalization** —
  already a corpus proposition
  ([`prop:wedderburn-trace-identity`](../../content/quantum-observable-universe/mass-theory/wedderburn-trace-identity.md)),
  not new structure. The tower-stabilization of E_p[\|Δθ\|] toward
  ≈ 0.78 rad is an empirical convergence datum (deliberately **not**
  identified with any constant — 3 tower points cannot support an
  identification; see guard notes).
- **The numerator side (the A ≈ 4 crossover in B_AME) matches the SU(4)
  supermultiplet truncation** —
  [`2026-07-12-su4-supermultiplet-alpha-cluster-truncation.md`](2026-07-12-su4-supermultiplet-alpha-cluster-truncation.md):
  the Lean-proved `C(4,n)` gate (`dim[1ⁿ] = C(4,n) = 0` for n > 4,
  Schur–Weyl-derived flavor factor) is the corpus's algebraic account of
  why the direct n-body channel closes at n = 4, forcing α-clustering and
  the B/A flattening. The crossover the discriminator measured in 𝒜(A) is
  that physics (as recorded in AME) — it was never in the θ_λ carrier.
- **Demazure / level-truncation (GAP-A-3)** is *not* needed to explain this
  datum: no per-λ truncation signature appears in the decomposition (the
  dominant-shape band moves smoothly with n; nothing switches off at
  H₁₂ → H₁₅).
- **The [3]_q! ≈ 6.1 "ceiling"** plays no role: 𝒜(D) ≈ [3]_q! remains the
  single-observable guarded datum of R2-d; the carrier itself never
  referenced it.

**Is this the framework's derivation of nuclear saturation?** Stated
carefully: **no.** What is *derived* (corpus proposition + this
decomposition) is that the normalized linear θ_λ carrier is **intensive**
— a categorical statement of the *form* "per-nucleon quantities flatten",
i.e. the carrier is structurally *compatible* with saturation-shaped
physics but cannot *produce* extensive binding at all. The actual A ≈ 4
crossover in this data path is carried by B_AME (experimental input), whose
corpus-side algebraic account is the separate SU(4) truncation line. The
sharp structural corollary is the useful output:

> **Corollary (scope-(a), for every future θ_λ closure).** Under the
> canonical Markov weighting `w_λ = y_λ·dim_λ`, the linear carrier
> `m_e·Σ w_λ|Δθ_λ| = m_e·E_p[|Δθ|]` is bounded by
> `m_e·π ≈ 1.605 MeV` (rotation channel; growth-channel share measured
> ≤ 0.79 and decaying) and empirically pinned at ≈ 0.4 MeV. **Extensivity
> must live elsewhere** — in an A-structured amplification 𝒜, in a
> non-normalized weighting, or in a different pairing — never in the
> normalized linear carrier. Ansätze of the form
> `B = m_e·𝒜·Σ y_λ dim_λ |Δθ_λ|` with scalar-or-slowly-varying 𝒜 are
> pruned as a class for large A: they force 𝒜 ∝ B_AME, i.e. they carry no
> binding information beyond the carrier's order-unity modulation.

This subsumes and explains both prior verdicts: the R2-d scalar-𝒜
refutation (a scalar times an intensive mean cannot track an extensive B)
and the R3-b geometric-law break (the "law" was B_AME's own ramp, which
ends at the α peak).

## 5. Falsifiable predictions (registered now)

1. **Carrier flatness extends:** m_e·S(A) stays in ≈ [0.35, 0.50] MeV for
   A = 8, 12 — and if the tower convergence is real, E_p[\|Δθ\|] at A = 8
   lands in 0.75–0.82 rad. No cached H₂₄/H₃₆ atom-χ witnesses exist yet
   (corpus-grepped: the largest is ⁶Li H₁₈); this is the named next
   compute (long job — tee-log discipline applies).
2. **Ceiling:** no isotope, at any A, yields m_e·S > 1.605 MeV + the
   growth-channel excess (with the growth share continuing to decay with
   n as measured 0.79 → 0.22). A single violation falsifies the
   normalization reading (or the witness pipeline).
3. **Formalizable prune (next Lean step, §3.4 pattern):** a small lemma
   `carrier_bounded : (∀ λ, |Δθ_λ| ≤ π) → Σ y_λ·d_λ = 1 → Σ y_λ·d_λ·|Δθ_λ| ≤ π`
   (finite arithmetic over the block index) turns the corollary into a
   machine-checked class-prune so the "scalar-𝒜 linear carrier" family
   cannot be silently re-proposed. The normalization premise is already
   the corpus proposition's Lean side.

## 6. Anti-fit / guard notes

- Nothing tuned, nothing wired. B_AME values appear **only** as numerators
  of reported diagnostic quotients (𝒜, B-steps).
- The convergence value E_p[\|Δθ\|] → ≈ 0.78 rad is **not** identified with
  any derived constant (π/4 = 0.785 sits nearby — flagged **as a
  numerology hazard, explicitly not claimed**: three tower points cannot
  support an identification, and no structural argument ties the
  stationary mean to π/4).
- The erratum finding (§2) does not alter any R3-b verdict; it corrects
  two table cells and the "grows geometrically then flatlines" phrasing of
  its §5 item 2 — the carrier neither grew nor crossed over.
- Scope-(a) throughout: the corollary prunes the *normalized linear
  carrier as sole mechanism*; it does not exclude θ_λ, y_λ, dim_λ, or any
  constant as ingredients of an A-structured closure.

## Provenance

Probe: [`carrier_saturation_mechanism_probe.py`](../../computations/deltalambda/carrier_saturation_mechanism_probe.py)
(9/9 assertions, wall 4.2 s, teed log `/tmp/carrier_sat.log`; witness
[`carrier-saturation-mechanism.witness.json`](../../computations/deltalambda/carrier-saturation-mechanism.witness.json)).
Cached inputs (no new tr_M compute):
`binding-reeb-phase-decomposition.witness.json`,
`chi-{deuteron,tritium,helium-3,helium-4}-h{6,9,12}-at-q0-50dps.witness.json`,
`chi-lithium-{5,6}-h{15,18}-at-q0-50dps-matrix-m.witness.json`,
`chi-helium-4-free-h12-at-q0-50dps.witness.json` (LR regression gate),
`chi-{proton,neutron}-h3-at-q0-50dps.witness.json` (LR nucleon cache).
Corpus anchors: `prop:wedderburn-trace-identity` (normalization),
[`2026-07-12-su4-supermultiplet-alpha-cluster-truncation.md`](2026-07-12-su4-supermultiplet-alpha-cluster-truncation.md)
(numerator-side A = 4 structure). Predecessors:
[`2026-07-13-theta-lambda-magnitude-derive-or-refute.md`](2026-07-13-theta-lambda-magnitude-derive-or-refute.md) (R2-d),
[`2026-07-13-li6-h18-amplification-discriminator.md`](2026-07-13-li6-h18-amplification-discriminator.md) (R3-b).
EXPLORATORY — audit + witness only; no production wiring.
