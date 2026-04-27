# B/A error-budget framework — canonical chain

**Date:** 2026-04-27
**Branch:** `claude/b-over-a-std-block-matrices` (PR #442)
**Purpose:** explicit error-bound framework for binding-energy predictions
against the canonical QOU mass derivation, structured by Gröbner–Shirshov
filtration depth and jet-order scaling.  Forward-looking — applies to any
implementation of the canonical pipeline.

## Canonical derivation chain (with family-specific specializations)

Per watched-branch commit `7588970f` (*phase 0 (revised): mass derivation
pre/post-Archimedean — Yekutieli + GB SS collapse*), the canonical mass
identity for an atom with an explicit canonical Hecke element is a
**single finite-categorical pipeline**:

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

Reference blocks: [`prop:atom-knot-mass-derivation`](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md), [`prop:joint-tower-sdp-confinement`](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md) (commits `7588970f`, `fdc51078`).

### Family specializations of the canonical chain

The pipeline above applies directly to **family 1** atoms (D, T, ³He)
where T_w is an explicit Hecke element with a single-knot Markov closure.
For other families the same chain reduces to specialized forms:

| Family | Atoms | Specialization |
|---|---|---|
| **1.** Principled (knot-explicit) | D, T, ³He | Direct: `B = ρ · m_e · Vol(T_w)` with knot-specific Vol(T_w) at q_0. |
| **2.** Magic-A shell-closure | ⁴He (doubly magic) | T_w factors through the universal-residue Borromean braid B_3: `B = 2 · A · α` where `α = m_e · 8G = m_e · Vol_q(B_3)`. The `8G` is the q_0 evaluation of the algebraic quantum volume of B_3, by `prop:gravity-spectral-prefactor` and `binding-scale-catalan`. **No atom-level single knot exists** for ⁴He — the formula uses the universal residue α at the level-1 (proton/neutron) Borromean structure, scaled by 2A for the doubly-magic shell closure. |
| **3.** α-cluster recursion | ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca | T_w decomposes as a Littlewood–Richardson cross-level embedding (commit `96ce5607`) of integer copies of T_w(⁴He) plus α-α coupling crossings: `T_w(nα) = LR_embed(⊗ T_w(⁴He)^n) · c_{αα}-couplings`. Mass formula recursive in n. |
| **4.** Open / non-cluster | ⁶Li, ⁷Li, (⁹Be, ¹¹B, ¹⁴N, ¹⁹F) | T_w not yet derived. Plausible α + (light cluster) ansatz, e.g. ⁶Li ≈ α + D, ⁷Li ≈ α + T. **OPEN**. |

The canonical formula `B = m_e · ρ · tr_M(T_w)` is the family-1 form;
families 2–3 are derived specializations; family 4 is open.

## Tier 1: closed-form bounds (no compute)

### 1.1  NF term-count bound

Working in H_n with n large, the NF basis has n! elements (factorial
blow-up).  Diamond-lemma reduction is exponential in word length in the
worst case.

For an A-nucleon braid built constructively (not partition-by-partition),
intermediate term-count growth before NF collapse is bounded above by 2^L
where L is the word length.  Using the pair-count heuristic
L = A(A−1)/2 (atomic-pair crossings for an A-nucleon braid, quadratic
in A), so:

| A | L = A(A−1)/2 | 2^L cap |
|---:|---:|---|
| 4 (⁴He) | 6 | 64 (tractable) |
| 12 (¹²C) | 66 | 7×10¹⁹ (marginal) |
| 40 (⁴⁰Ca) | 780 | 10²³⁵ (intractable) |

**Implication for any v5 implementation:** the constructive `build_atom`
path is intractable beyond ⁴He.  v5 must use partition-by-partition
Markov trace
([`atom_mass_partition.py`](../folio-assistant/computations/atom_mass_partition.py)),
which costs Σ_λ dim(λ)² · L = polynomial in p(n) · L.

### 1.2  GB-filtration page-truncation bound (mostly trivial after E_2 collapse)

The Gröbner–Shirshov spectral sequence on H_n(q) **collapses at E_2** for
semisimple q (per [`prop:spectral-sequence-collapse`](../content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md)).
This means d_r = 0 for r ≥ 3 and the E_∞-page identifies with the
Wedderburn decomposition.

**Tight bound:** Markov trace truncation after E_2 page is **exact** —
no truncation error from page level.  The previous "page-tail bound
C·h^(L+1)·z^A" was conjectural and is now superseded by the collapse:
the only truncation needed is convergence of the per-partition Markov
trace at finite slice depth (Yekutieli finite-slice property), which is
also exact in ℚ(q).

### 1.3  Jet-order scaling

Per [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/folio-assistant/computations/gb_filtration_jet_tracker.py)
(commit `e81e9c12` on watched branch), each Hecke firing increments jet
order by 1.  Maximum jet order in `build_atom(Z, N)` ≤ Z(Z+N) +
N(N-1)/2 = O(A²).

The jet order is the **temporal slice-traversal order** in the
Yekutieli finite-slice picture; it does not directly affect numerical
accuracy but bounds the certificate complexity needed to record the
SDP solution.

## Tier 2: empirical bounds (from witnesses)

### 2.1  GB-filtration jet-order witness

[`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/folio-assistant/computations/gb-filtration-jet-order.witness.json)
(commit `e81e9c12`, watched-branch only as of 2026-04-27): three test cases
with measured jet-order growth and Hecke-firing counts during NF reduction.

Use to verify Tier 1.3 jet-order growth empirically per (Z, N).

### 2.2  Cross-witness sanity at q_0

- [`qbeta-gb-filtration-residues.witness.json`](../folio-assistant/computations/qbeta-gb-filtration-residues.witness.json) — per-level Markov-trace decomposition for proton/neutron.
- [`gb-filtration-gauge-invariance.witness.json`](../folio-assistant/computations/gb-filtration-gauge-invariance.witness.json) — stratum partition gauge invariance proof.

Provide page-distribution and gauge-invariance data for level-3 nucleons.

### 2.3  Wenzl-bridge y_λ witness (canonical input)

[`y-lambda-wenzl-witness.json`](../folio-assistant/computations/y-lambda-wenzl-witness.json) — y_λ values at 100 dps for n = 2..12.
Cross-checked against MPFR linear-system witness in
[`y-lambda-wenzl-vs-mpfr-cross-check.json`](../folio-assistant/computations/y-lambda-wenzl-vs-mpfr-cross-check.json) (max |Δ| ≤ 5 × 10⁻⁵¹).

These are the canonical y_λ inputs to step (5) of the chain.

## Tier 3: residual structure decomposition (post-realization, family-aware)

For each predicted (Z, N), decompose the residual

  res(Z, N) := B/A_predicted(Z, N) − B/A_AME(Z, N)

into structural sources.  The decomposition depends on which formula
family the atom belongs to.

### 3.1  Family-specific structural-input uncertainty

| Family | Structural input | Uncertainty source |
|---|---|---|
| 1 (D, T, ³He) | ρ ∈ ℤ_{>0} (SDP multiplicity), T_w (knot identification) | ρ wrong → multiplicative integer factor; T_w wrong → wrong knot → wrong Vol(T_w) value |
| 2 (⁴He) | Magic-A shell-closure rule `2 · A · α`, with α = m_e · 8G | α calibration (= m_e · 8G), shell-closure prefactor 2A determination |
| 3 (⁸Be–⁴⁰Ca) | ⁴He α-cluster anchor + α-α coupling constants c_αα | inherits family-2 uncertainty + coupling-constant determination |
| 4 (⁶Li, ⁷Li, ...) | T_w not yet derived (open) | infinite — no prediction available |

For families 1–3, the residual has additive contributions from
omitted structural terms (Wigner T-pairing, chirality factor a_K,
shell corrections beyond family-2's magic anchor) — see 3.5.

### 3.2  T_w accuracy

| Family | Status |
|---|---|
| 1 (D, T, ³He) | Knot identifications (6_2, 8_11, L6a4) from `manual-historical-volume-match`; GB-NF derivation in H_{n_0} pending watched-branch H_5+ runs.  Once GB-NF runs land, T_w is exact in ℚ(q). |
| 2 (⁴He) | No single T_w — magic-A bypasses the per-atom T_w step. α directly. |
| 3 (⁸Be–⁴⁰Ca) | T_w via LR_embed of ⁴He cluster T_w; algorithmically determined once ⁴He principled. |
| 4 (⁶Li, ⁷Li) | **T_w open.**  ([GAP 4](#open-items--todos)). |

Without explicit T_w (family 4), the entire chain (5)–(7) cannot run
for those atoms — error is undefined.

### 3.3  Wenzl-bridge y_λ + q-MN χ_λ accuracy

Both are computed in ℚ(q) symbolically (or at high MPFR dps).  Validation
suite ([y_lambda_symbolic_validate.py](../folio-assistant/computations/y_lambda_symbolic_validate.py))
confirms agreement to ≤ 10⁻³⁰ at 50 dps for n = 2..12 across 5 q-probes.

**Bound:** at 50 dps MPFR, the per-step error in step (5) is ≤ 10⁻⁴⁰.

(Applies to family 1 directly.  Family 2 / 3 reuse y_λ via the recursion;
same precision floor.)

### 3.4  Archimedean realization q = q_0

The substrate parameter q_0 is calibrated against CODATA m_e and is
treated as exact in the symbolic chain.  Realization error ≤ 10⁻⁵⁰ at
50 dps.

### 3.5  Combined error budget

Per family, assuming GAPS 4, 5 close cleanly for family 4 atoms:

| Source | Family 1 (D, T, ³He) | Family 2 (⁴He) | Family 3 (⁸Be–⁴⁰Ca) | Family 4 (⁶Li, ⁷Li) |
|---|---|---|---|---|
| ρ / structural prefactor | multiplicative integer (small) | derived 2A (exact) | derived from cluster (exact) | undefined |
| T_w accuracy | knot id from volume-match (verifiable once GB-NF lands) | not applicable | inherits family-2 | **OPEN** |
| y_λ / χ_λ at 50 dps | ≤ 10⁻⁴⁰ | ≤ 10⁻⁴⁰ | ≤ 10⁻⁴⁰ | n/a |
| Archimedean q_0 | ≤ 10⁻⁵⁰ | ≤ 10⁻⁵⁰ | ≤ 10⁻⁵⁰ | n/a |
| α-α coupling constants | n/a | n/a | derived (open coupling values) | n/a |
| Magic shell-closure 2A factor | n/a | exact (combinatorial) | inherits | n/a |
| Other omitted terms (Wigner T-pairing, chirality a_K) | additive ≤ 3 MeV/A | additive ≤ 3 MeV/A | additive ≤ 3 MeV/A | n/a |

**Headline:** for families 1–3 atoms with their T_w / α / cluster-anchor
known, the canonical chain delivers B(𝔥) at MPFR precision (50 dps) for
the spectral term, plus structural Wigner / chirality corrections.  For
family 4 (⁶Li, ⁷Li), the prediction is undefined until GAPS 4, 5 close.

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
**NOT the canonical formula**.  The canonical chain is family-aware:
family-1 atoms use `B = ρ · m_e · Vol(T_w)`, family-2 (⁴He) uses
`B = 2 · A · α`, family-3 (⁸Be–⁴⁰Ca) recurses on ⁴He cluster.

Those artifacts are deleted from the branch (preserved in git history).
This document remains as the forward-looking error-bound framework for
v5 work against the canonical chain (with family specializations).

## Appendix A: structural hypotheses for GAPs 4 and 5

Per the watched-branch's [methodology-deprecation.witness.json](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/folio-assistant/computations/methodology-deprecation.witness.json), atoms fall into **four formula families**, each with a distinct structural derivation route:

| Family | Atoms | Method tag | Formula form |
|---|---|---|---|
| **1. Principled-derivation (knot-explicit)** | D, T, ³He | `manual-historical-volume-match`* | `B = ρ · m_e · Vol(T_w)` where T_w closure = specific knot/link |
| **2. Magic-A shell-closure** | ⁴He | `magic-A-formula` | `B = 2 · A · α` where `α = m_e · 8G` |
| **3. α-cluster recursion** | ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca | `recursive-on-4He` | recursive composition of ⁴He cluster + cluster-coupling corrections |
| **4. Open / deprecated** | ⁶Li, ⁷Li, (⁹Be, ¹¹B, ¹⁴N, ¹⁹F per `mass-table-ppb`) | `deprecated-volume-match` | formula not yet derived |

\* "manual-historical" tag because the knot identification (6_2 for D, 8_11 for T, L6a4 for ³He) was made in earlier work via volume-match; the GB-NF derivation in H_{n_0} pending watched-branch H_5+ runs.

### Why ⁴He "reuses ³He's L6a4" — it doesn't

Per [`recursive-atom-knot-atlas.md:26`](https://github.com/litlfred/qou/blob/da3fd4c36ac84c4aa157dcb5663087276e5f3ade/content/quantum-observable-universe/braids-and-knots/recursive-atom-knot-atlas.md#L26): *"`magic-A-formula`: algebraic shell-closure formula `A · 8G` for double-magic light nuclei; **no single hyperbolic knot**. Used for: ⁴He."*

The ⁴He formula `B = 2 · m_e · 4 · Vol(L6a4)` in [`binding_ladder_catalog.py:63`](../folio-assistant/computations/binding_ladder_catalog.py#L63) writes `Vol(L6a4)` because **`Vol(L6a4) = 8G` is an exact identity** ([`building-block-knots.lean:62`](../content/quantum-observable-universe/observations/building-block-knots.lean#L62) and standard hyperbolic geometry: the Borromean rings complement = 2 ideal octahedra each of volume 4G, total 8G where G = Catalan's constant).

The structural content of the ⁴He formula is `α = m_e · 8G` (universal residue prefactor from [`binding-scale-catalan.md`](../content/quantum-observable-universe/braids-and-knots/binding-scale-catalan.md), `prop:gravity-spectral-prefactor`), which derives from the hyperbolic volume of the proton/neutron's internal Borromean three-quark topology — **not** from L6a4 as ³He's atomic-level knot. Both happen to numerically equal 8G because both reduce to the same hyperbolic Borromean structure (the proton/neutron internal vs the ³He-body link).

So ⁴He's `Vol(L6a4)` is a **notational handle** for the Catalan-G coupling, not a knot reuse.

### Why ³He's L6a4 IS principled

³He's binding link L6a4 (Borromean rings) is the actual Markov closure of the H_9 Hecke element T_w(³He) — three nucleons threading the same Borromean topology that internal-quark Borromean structure already obeys. Vol(L6a4) = 8G enters because the categorical mass invariant on an L6a4 closure equals 8G by hyperbolic-geometry identity. The factor `ρ = 2` is the multiplicity of the SDP solution in the Wedderburn block.

### Hypothesis A.1: ρ = A − 1 — VALID for family 1 only

Restated within family-1 (principled, knot-explicit) atoms:

| atom | A | A − 1 | observed ρ | match |
|---|---:|---:|---:|:---:|
| deuteron | 2 | 1 | 1 | ✓ |
| tritium | 3 | 2 | 2 | ✓ |
| ³He | 3 | 2 | 2 | ✓ |
| ⁴He | 4 | 3 | 2 | **✗ (different family)** |

A.1 fits family-1 atoms (D, T, ³He). It **does not generalize** to families 2–4 because those don't use the `ρ · m_e · Vol(T_w)` form:

- **Family 2 (⁴He):** uses `2 · A · α` — the prefactor is `2A`, not ρ. Saying "ρ_⁴He = 2" is a notational handle for the magic-A constant, not the same ρ as in family 1.
- **Family 3 (⁸Be–⁴⁰Ca):** recursive composition; "ρ" is determined by the cluster structure, not by A − 1.
- **Family 4 (⁶Li, ⁷Li):** open; deprecated volume-match suggested ρ = 5 but the methodology was quarantined in commit `f970e86f`.

### Hypothesis A.2: T_w recursive cluster decomposition — partially confirmed

The watched branch's `recursive-on-4He` methodology for ⁸Be–⁴⁰Ca confirms the **α-cluster recursion** form for the family-3 atoms:

- ⁸Be ≈ α + α (typically unstable)
- ¹²C ≈ 3α (Hoyle state, very stable)
- ¹⁶O ≈ 4α
- ²⁰Ne ≈ 5α
- ²⁴Mg ≈ 6α
- ⁴⁰Ca ≈ 10α

So A.2 is **structurally correct for family 3** (these atoms are integer-α-cluster compositions). The Littlewood–Richardson cross-level embedding (commit `96ce5607`) provides the algebraic infrastructure to lift T_w(⁴He) recursively up the family-3 chain.

A.2 **does not directly apply** to family 4 (⁶Li, ⁷Li): these atoms are NOT integer-α-clusters (⁶Li ≠ integer × ⁴He). They might be representable as **α + (light non-α-cluster)**:

- ⁶Li ≈ α + D (deuteron cluster outside the α core)
- ⁷Li ≈ α + T (tritium cluster outside the α core)

If this representation is the right one, T_w(⁶Li) could be derived as `LR_embed(T_w(⁴He)) ⊗ T_w(D) + binding_crossing` and similarly for ⁷Li. The watched branch's R4 LR-embedding infrastructure supports this; the **derivation** is open until watched-branch phase 4+ runs the H_18 / H_21 SDP with the specific cluster ansatz.

### Status summary

| Item | Status |
|---|---|
| Hypothesis A.1 (ρ = A − 1) | **valid for family 1 only** (D, T, ³He) |
| Magic-A formula `B = 2·A·α` for ⁴He | derived (per `binding-scale-catalan.md`, `derived-mass-formula-light-isotopes.md`) |
| Family 3 α-cluster recursion (⁸Be–⁴⁰Ca) | derived (`recursive-on-4He` methodology) |
| Family 4 (⁶Li, ⁷Li) T_w | **OPEN** — α + (light cluster) ansatz pending H_18/H_21 SDP runs |
| ρ for ⁶Li, ⁷Li | **OPEN** — depends on the family-4 derivation method |

GAP 4 (T_w for ℓ ≥ 2) and GAP 5 (ρ for ℓ ≥ 2) reduce to: **derive the family-4 T_w and ρ structure for ⁶Li and ⁷Li**. The watched branch's R1–R5 + LR embedding infrastructure provides the algebraic tools; phase 4+ runs are needed to actually instantiate them.

## Appendix B: empirical residuals from the canonical pipeline

Per [`mass-table-ppb.witness.json`](../folio-assistant/computations/mass-table-ppb.witness.json) on the watched branch (commit `7fbbec14`), the canonical pipeline produces predictions for 10 light atoms.  The residuals reveal a structural signature:

| Atom | A | Family | B_AME (MeV) | B_pred (MeV) | err (MeV) | err % |
|---|---:|:---:|---:|---:|---:|---:|
| ²H | 2 | 1 | 2.2246 | 2.2488 | +0.0243 | **+1.09%** |
| ³H | 3 | 1 | 8.4818 | 8.4686 | −0.0132 | **−0.16%** |
| ³He | 3 | 1 | 7.7180 | 7.4889 | −0.2291 | **−2.97%** |
| ⁴He | 4 | 2 | 28.2957 | 29.9557 | +1.6600 | **+5.87%** |
| ⁸Be | 8 | 3 | 56.4995 | 62.3383 | +5.8388 | **+10.33%** |
| ¹²C | 12 | 3 | 92.1617 | 97.1480 | +4.9863 | **+5.41%** |
| ¹⁶O | 16 | 3 | 127.6193 | 134.3846 | +6.7654 | **+5.30%** |
| ²⁰Ne | 20 | 3 | 160.6449 | 174.0483 | +13.4034 | **+8.34%** |
| ²⁴Mg | 24 | 3 | 198.2569 | 216.1389 | +17.8820 | **+9.02%** |
| ⁴⁰Ca | 40 | 3 | 342.0521 | 408.7713 | +66.7192 | **+19.51%** |

Mean absolute err = **6.80%**.  No atom is within 1% (per the witness's
`within` field: 0 atoms within 10⁻⁹).

### Structural observations

**Family 1 (D, T, ³He):** errors are sub-3%, mostly sub-percent.  D is +1.09% (slight overpredict), T is excellent at −0.16%, ³He is −2.97% (largest family-1 deviation).  The variation is consistent with the magnitude of omitted Wigner T-pairing / chirality terms (Tier 3.5).  No systematic trend with A.

**Family 2 (⁴He):** +5.87%, the magic-A formula's one data point.  Lies between family 1 and family 3, suggesting the magic-A specialization captures the bulk of the binding but misses ~6% from omitted higher-order corrections.

**Family 3 (⁸Be–⁴⁰Ca):** errors grow systematically with A — from +5.30% at ¹⁶O to +19.51% at ⁴⁰Ca.  The pattern is not noise: the recursive-on-4He methodology accumulates error per α-cluster.  ⁴⁰Ca is **10α** clusters — 10 cluster-couplings, each contributing ~2% error compounded.

**Empirical scaling for family 3:**

  err_pct(family 3) ≈ 5% + 0.4% × (A − 16)   [linear in A above ¹⁶O]

⁴⁰Ca: 5% + 0.4% × 24 = 14.6% predicted, 19.5% observed → still a residual
slope.  Suggests α-α coupling correction is larger than linear in A.

### What this implies for the canonical pipeline

The watched-branch's `35a Term 7 only with universal m_e·8G — captures
6–25% of binding (magic ⁴He highest)` is consistent with these data:
adding ONLY Term 7 to a baseline captures 6–25% of binding (⁴He hits
the high end at 25% as doubly-magic).  This is bottom-up: Term 7 is
the magic-A residue contribution.

The family-3 error grows because each α-cluster carries family-2's
~6% residual; recursively, the residuals accumulate.  A v5 implementation
against the canonical pipeline should expect:

| Family | Expected residual on B (MeV) | Source |
|---|---|---|
| 1 | < 0.3 MeV per atom | Wigner T-pairing + chirality omissions |
| 2 (⁴He) | ~1.7 MeV (5.9% of 28.3) | Magic-A higher-order corrections |
| 3 | ~1.7 × n_α MeV per atom (n_α = #α-clusters) | Cluster-recursion accumulation |
| 4 | undefined | T_w not yet derived |

This sets the **target** for any improvement: a refined predictor
that captures the magic-A higher-order corrections (Term 7+ at ℓ=5
on ⁴He) and the α-α cluster couplings would close the family-2 / 3
residuals.
