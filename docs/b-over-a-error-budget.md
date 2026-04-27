# B/A error-budget framework — canonical chain

**Date:** 2026-04-27
**Branch:** `claude/b-over-a-std-block-matrices` (PR #442)
**Purpose:** explicit error-bound framework for binding-energy predictions
against the canonical QOU mass derivation, structured by Gröbner–Shirshov
filtration depth and jet-order scaling.  Forward-looking — applies to any
implementation of the canonical pipeline.

## Canonical derivation chain

Per watched-branch commit `7588970f` (*phase 0 (revised): mass derivation
pre/post-Archimedean — Yekutieli + GB SS collapse*), the canonical mass
identity is a **single finite-categorical pipeline**:

  **B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0**

Everything pre-Archimedean lives in **ℚ(q)**, exact and finite.  Volume
conjecture is post-Archimedean naming, not part of the derivation.  The
geometric leg (Reeb-density / Mostow / Gromov / Vol_hyp) is explicitly
**not part of QOU derivation**.  The GB spectral sequence **collapses at
E_2** for semisimple H_n(q) at generic q.

| Step | Where in the pipeline |
|---|---|
| (1) Categorical action of **C** on 𝒮 | input |
| (2) Yekutieli at finite slice (= Hecke quadratic relation σ²=hσ+1 as curvature 2-form at adjacent slices) | structural correspondence; no analytic content |
| (3) Joint-tower confinement SDP at q_0 with GB filtration + jet-order tracking | yields canonical T_w ∈ H_{n_0}(q_0) in GB-NF |
| (4) Wedderburn decomposition H_n(q) ≅ ⊕_λ M_{d_λ}(ℚ(q)) | semisimple at generic q; GB SS collapses at E_2 |
| (5) Markov trace tr_M(T_w) = Σ_λ y_λ(q) χ_λ(T_w) | Wenzl-bridge y_λ + q-Murnaghan–Nakayama χ_λ |
| (6) Categorical mass invariant M(𝔥) = ρ · tr_M(T_w) ∈ ℚ(q) | ρ structural integer (multiplicity in SDP solution) |
| (7) Archimedean realization functor at q = q_0, multiply by m_e | gives B(𝔥) ∈ ℝ (MeV) |

Reference blocks: [`prop:atom-knot-mass-derivation`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md), [`prop:joint-tower-sdp-confinement`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md) (commits `7588970f`, `fdc51078`).

## Tier 1: closed-form bounds (no compute)

### 1.1  NF term-count bound

Working in H_n with n large, the NF basis has n! elements (factorial
blow-up).  Diamond-lemma reduction is exponential in word length in the
worst case.

For an A-nucleon braid built constructively (not partition-by-partition),
intermediate term-count growth before NF collapse is bounded above by 2^L
where L is the word length.  L scales as A² for atomic braids, so:

| A | L ≈ A² | 2^L cap |
|---:|---:|---|
| 4 (⁴He) | 6 | 64 (tractable) |
| 12 (¹²C) | 66 | 7×10¹⁹ (marginal) |
| 40 (⁴⁰Ca) | 980 | 10²⁹⁵ (intractable) |

**Implication for any v5 implementation:** the constructive `build_atom`
path is intractable beyond ⁴He.  v5 must use partition-by-partition
Markov trace
([`atom_mass_partition.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/atom_mass_partition.py)),
which costs Σ_λ dim(λ)² · L = polynomial in p(n) · L.

### 1.2  GB-filtration page-truncation bound (mostly trivial after E_2 collapse)

The Gröbner–Shirshov spectral sequence on H_n(q) **collapses at E_2** for
semisimple q (per [`prop:spectral-sequence-collapse`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md)).
This means d_r = 0 for r ≥ 3 and the E_∞-page identifies with the
Wedderburn decomposition.

**Tight bound:** Markov trace truncation after E_2 page is **exact** —
no truncation error from page level.  The previous "page-tail bound
C·h^(L+1)·z^A" was conjectural and is now superseded by the collapse:
the only truncation needed is convergence of the per-partition Markov
trace at finite slice depth (Yekutieli finite-slice property), which is
also exact in ℚ(q).

### 1.3  Jet-order scaling

Per [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py)
(commit `e81e9c12` on watched branch), each Hecke firing increments jet
order by 1.  Maximum jet order in `build_atom(Z, N)` ≤ Z(Z+N) +
N(N-1)/2 = O(A²).

The jet order is the **temporal slice-traversal order** in the
Yekutieli finite-slice picture; it does not directly affect numerical
accuracy but bounds the certificate complexity needed to record the
SDP solution.

## Tier 2: empirical bounds (from witnesses)

### 2.1  GB-filtration jet-order witness

[`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json)
(commit `e81e9c12`, watched-branch only as of 2026-04-27): three test cases
with measured jet-order growth and Hecke-firing counts during NF reduction.

Use to verify Tier 1.3 jet-order growth empirically per (Z, N).

### 2.2  Cross-witness sanity at q_0

- [`qbeta-gb-filtration-residues.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/) — per-level Markov-trace decomposition for proton/neutron.
- [`gb-filtration-gauge-invariance.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/) — stratum partition gauge invariance proof.

Provide page-distribution and gauge-invariance data for level-3 nucleons.

### 2.3  Wenzl-bridge y_λ witness (canonical input)

[`y-lambda-wenzl-witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y-lambda-wenzl-witness.json) — y_λ values at 100 dps for n = 2..12.
Cross-checked against MPFR linear-system witness in
[`y-lambda-wenzl-vs-mpfr-cross-check.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y-lambda-wenzl-vs-mpfr-cross-check.json) (max |Δ| ≤ 5 × 10⁻⁵¹).

These are the canonical y_λ inputs to step (5) of the chain.

## Tier 3: residual structure decomposition (post-realization)

For each predicted (Z, N), decompose the residual

  res(Z, N) := B/A_predicted(Z, N) − B/A_AME(Z, N)

into the canonical chain steps.  Under the canonical formula
`B = m_e · ρ · tr_M(T_w)`, the residual has limited structural sources:

### 3.1  ρ structural prefactor uncertainty

ρ ∈ ℤ_{>0} is determined structurally by the SDP solution multiplicity in
the Wedderburn decomposition.

For ℓ ≤ 1 (electron, p, n): ρ = 1 directly.
For ℓ ≥ 2 (atoms): ρ depends on the joint-tower SDP feasibility.
  Per the watched branch, ρ ∈ {1, 2} for ℓ ≤ 2; **ρ = 5 for ⁶Li / ⁷Li
  is a volume-match observation, not derived** ([GAP 5](#open-items)).

A predictor that gets ρ wrong scales B(𝔥) by an integer factor — the
residual is multiplicative, not additive.

### 3.2  T_w accuracy (canonical Hecke element)

For ℓ ≤ 1 (electron, p, n): T_w explicit and verified.
For ℓ ≥ 2 (⁶Li / ⁷Li and beyond): **T_w not yet derived** ([GAP 4](#open-items)).

Without explicit T_w, the entire chain (5)–(7) cannot run for these atoms.

### 3.3  Wenzl-bridge y_λ + q-MN χ_λ accuracy

Both are computed in ℚ(q) symbolically (or at high MPFR dps).  Validation
suite ([y_lambda_symbolic_validate.py](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y_lambda_symbolic_validate.py))
confirms agreement to ≤ 10⁻³⁰ at 50 dps for n = 2..12 across 5 q-probes.

**Bound:** at 50 dps MPFR, the per-step error in step (5) is ≤ 10⁻⁴⁰.

### 3.4  Archimedean realization q = q_0

The substrate parameter q_0 is calibrated against CODATA m_e and is
treated as exact in the symbolic chain.  Realization error ≤ 10⁻⁵⁰ at
50 dps.

### 3.5  Combined error budget

Under the canonical formula and assuming all three open gaps (3, 4, 5)
close cleanly:

| Source | Bound on B(𝔥) error |
|---|---|
| Tier 1.1 NF tractability | O(0) for partition-by-partition path |
| Tier 1.2 GB page truncation (after E_2 collapse) | 0 |
| Tier 1.3 jet-order scaling | structural complexity, no numerical impact |
| Tier 3.1 ρ uncertainty | multiplicative integer factor |
| Tier 3.2 T_w accuracy (ℓ ≥ 2) | infinite (no T_w → no prediction) |
| Tier 3.3 y_λ / χ_λ at 50 dps | ≤ 10⁻⁴⁰ |
| Tier 3.4 Archimedean q_0 | ≤ 10⁻⁵⁰ |

**Headline:** for ℓ ≤ 1 atoms with explicit T_w and ρ, the canonical
chain delivers B(𝔥) at MPFR precision (50 dps).  For ℓ ≥ 2 the
prediction depends on closing GAPS 3, 4, 5.

## Open items / TODOs

Three gaps remain open (block v5 implementation against canonical chain):

| # | Gap | Status |
|---|---|---|
| 3 | Joint-tower SDP solver implementation | **partially closed by `fdc51078`** (`phase 2: design spec`); concrete solver still pending. |
| 4 | Canonical T_w explicit for ℓ ≥ 2 (⁶Li, ⁷Li, ...) | **OPEN** — without T_w, chain (5)–(7) cannot run. |
| 5 | Structural ρ prefactor derivation for ℓ ≥ 2 | **OPEN** — ρ = 1 for ℓ ≤ 1 direct; ρ = 5 for ⁶Li/⁷Li volume-match observation, not derived. |

Six gaps from the earlier two-leg framing are **closed** by `7588970f`
(volume conjecture, Reeb-density, Mostow/Gromov, Vol_hyp not part of QOU
derivation; GB SS collapse at E_2).  See PR #442 body for the full
status table.

## Note on superseded artifacts

This PR (#442) originally contained:

- `content/quantum-observable-universe/braids-and-knots/b-over-a-spectral-decomposition.{md,ts,lean}`
- `folio-assistant/computations/b_over_a_evaluator_v2.py`
- `folio-assistant/computations/b-over-a-witness-v2.json`

implementing a Plancherel-weighted log-of-Markov-trace-ratio formula
`(E_0/A) Σ_λ w_λ log|Λ_λ^free / Λ_λ^nuc|`.  Per `7588970f`, this is
**NOT the canonical formula**; the canonical is `B = m_e · ρ · tr_M(T_w)`.

Those artifacts are deleted from the branch (preserved in git history).
This document remains as the forward-looking error-bound framework for
v5 work against the canonical chain.

## Appendix A: structural hypotheses for GAPs 4 and 5

The watched branch `claude/mass-units-bridge-followups` (commit
`7fbbec14`, witness `joint-tower-sdp-h6-h9.witness.json`) provides three
explicit principled-derivation atoms with `(A, n_0, knot, ρ)`:

| atom | A | n_0 = 3A | knot | strands | word_len | binding | ρ | B_AME (MeV) |
|---|---:|---:|---|---:|---:|---|---:|---:|
| deuteron | 2 | 6 | 6_2 | 3 | 6 | L_H (Hopf) | 1 | 2.2246 |
| tritium | 3 | 9 | 8_11 | 5 | 14 | T_3 trefoil-like | 2 | 8.4818 |
| ³He | 3 | 9 | L6a4 | 3 | 6 | L6a4 (link) | 2 | 7.718 |

Volume-match-only observations (deprecated methodology, not principled):
⁶Li ρ = 5, ⁷Li ρ = 5 (per `li-atom-knot-search.witness.json`).

### Hypothesis A.1: ρ = A − 1 (primary)

Direct fit to the 3 explicit data points:

| atom | A | A − 1 | observed ρ | match |
|---|---:|---:|---:|:---:|
| deuteron | 2 | 1 | 1 | ✓ |
| tritium | 3 | 2 | 2 | ✓ |
| ³He | 3 | 2 | 2 | ✓ |

**Predictions** (testable once watched branch lands principled
derivations):

| atom | A | predicted ρ | volume-match observed | hypothesis verdict |
|---|---:|---:|---:|---|
| ⁴He | 4 | **3** | (none yet) | open |
| ⁶Li | 6 | **5** | 5 | **agrees** with deprecated obs |
| ⁷Li | 7 | **6** | 5 | **disagrees** with deprecated obs |

If hypothesis A.1 holds for ⁶Li, the agreement with the volume-match ρ
is a quantitative consistency check.  The disagreement at ⁷Li would
suggest either:

- (a) the volume-match observation for ⁷Li was incorrect (the
  watched branch has commit `f970e86f deprecate volume-match atom-knot
  search; quarantine ⁶Li/⁷Li`, supporting (a)); or
- (b) ρ = A − 1 fails at ⁷Li due to a shell-closure correction (⁷Li has
  one nucleon outside the K-shell magic 4); a corrected rule of the form
  `ρ = A − 1 − δ_shell` with `δ_shell ∈ {0, 1}` could fit both ⁶Li and ⁷Li
  if `δ_shell = 1` for nuclei with 1 valence nucleon outside a magic core.

**Status:** A.1 is a 3-data-point hypothesis with one principled
prediction (⁴He = 3) and one structural-consistency check (⁶Li = 5
matches the deprecated volume-match).  Cannot be falsified or confirmed
without watched-branch principled derivations for ⁴He, ⁶Li.

### Hypothesis A.2: T_w recursive cluster decomposition (GAP 4)

The pattern `n_0 = 3A` reflects the level-3 atomic braid: each nucleon
contributes 3 quark strands, so an A-nucleon atom lives in H_{3A}.

For light atoms the constituent decomposition tracks observable cluster
structure:

- D = p + n (one binding link, Hopf)
- T = p + 2n (one binding knot, 8_11; 5-strand braid suggests a 3-2 cluster split)
- ³He = 2p + n (one binding link, L6a4)
- ⁴He: predict α-particle structure, knot/link on H_12, possibly two
  Hopf-Hopf bindings (4-cluster)
- ⁶Li: in nuclear physics ⁶Li ≈ α + D cluster.  Hypothesise
  T_w(⁶Li) = LR_embed_{12 → 18}(T_w(⁴He)) ·
            (binding_crossing on cluster boundary) ·
            T_w(D) lifted to H_18
- ⁷Li ≈ α + T cluster: T_w(⁷Li) = LR_embed_{12 → 21}(T_w(⁴He)) ·
            (binding) · T_w(T) lifted to H_21
- ⁸Be ≈ α + α: T_w(⁸Be) = LR_embed(T_w(⁴He)) ⊗ LR_embed(T_w(⁴He)) +
            interaction.  Note: ⁸Be is unstable in nature, which would
            be predicted by the SDP infeasibility at the
            cluster-double-α configuration.

The Littlewood–Richardson cross-level embedding infrastructure landed
in the watched branch's commit `96ce5607` (`R4: cross-level embedding
consistency via Littlewood-Richardson`) provides the embedding rule
needed to run this recursion.

**Status:** A.2 is a structural sketch, not a derivation.  Validation
requires the watched branch to (i) derive ⁴He principled T_w, (ii) run
LR_embed_{12 → 18} ∘ T_w(⁴He) and check whether the result + binding
yields the SDP-feasible T_w(⁶Li) at the right ρ.

### What this appendix contributes

It does not close GAPs 4 or 5.  It provides:

- A concrete falsifiable hypothesis (`ρ = A − 1`) that fits all known
  principled data and matches the deprecated ⁶Li volume-match
  observation.
- A structural sketch (LR-embedding cluster decomposition) for the
  recursive T_w construction, consistent with the watched branch's
  R4 infrastructure.
- A specific prediction at ⁴He (`ρ = 3`) that can be tested as soon
  as the next phase lands on the watched branch.

If A.1 and A.2 hold up, GAPs 4 and 5 reduce to "implement the
recursion at the new infrastructure level."  If they fail at ⁴He, the
hypothesis space narrows substantially.
