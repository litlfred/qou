# Pre-registration — is the light-isotope binding residual CLUSTER structure rather than body order?

**Date:** 2026-08-26 · **Bean:** `qou-52x7` (parent epic `qou-v2om`) · **PR:** [#5812](https://github.com/litlfred/qou/pull/5812)
**Status when committed: NO NUMBERS HAVE BEEN COMPUTED FOR THIS FRONT.** This file is
committed *before* the probe is written or run. The verdict is reported against the
criteria below whatever it turns out to be, including a boring one, and including
"clustering does not explain it".

## Why a pre-registration

Cluster counts are a small-integer family (`n_α`, cluster multiplicity, bond counts
between clusters) fitted against ~6 light isotopes. Something will fit. AGENTS.md names
the hazard directly — passing a fit off as a derivation — and the α-cluster axis is
already the corpus's most fit-prone area (§7 of the motivating audit records a
numerology signature there: two unrelated constructs both landing near 8 MeV/nucleon).
This document fixes, in advance: the quantity, the corpus source, a numeric support
criterion, a numeric refutation criterion, **the integer number of cluster-assignment
schemes that will be tried**, and the degrees of freedom that disqualify a result.
Trying more schemes afterwards and reporting the best is precisely the fraud this
guards against.

## The observation that motivates it (existing corpus data, quoted not recomputed)

From §5 of
[`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md),
against the complete-graph pairwise maximum
`B_allpairs = α[C(Z,2)L_pp + Z·N·L_pn + C(N,2)L_nn]` (the edge set `K_A`, the **maximum**):

| iso | `B_AME / B_allpairs` |
|---|---|
| ³H | 0.945 |
| ⁴He | **1.647** |
| ⁶Li | 0.743 |
| ⁷Li | 0.639 |

The pairwise family is **too weak at A = 4** and **too strong at A = 3, 6, 7**. That is
not a scale error — a scale error is monotone. §4 of the same audit corroborates from
the other side: against the 2.95 MeV/nucleon plateau (12 ≤ A ≤ 90), ⁴He reads **+10.5 %**
and ⁶Li/⁹Be read **−25 %**, which that audit already calls "the α-cluster signature".

## The hypotheses under test — TWO, kept separate

A per-block model over `A` nucleons cannot know that ⁶Li is "α + d" rather than six
equivalent nucleons. Two distinct readings follow, and conflating them would be the
arity conflation AGENTS.md §"Grep the claim SHAPE" warns about:

- **H_all** — cluster substructure explains **the** residual, i.e. the whole
  non-monotone pattern above, in both directions.
- **H_partial** — cluster substructure explains only the **A ≥ 6 over-binding** of the
  pairwise family (⁶Li 0.743, ⁷Li 0.639 → ≈ 1), leaving the ⁴He deficit to a different
  object.

Both are tested; they are reported separately and may receive different verdicts.

### Scope of the class being tested — stated so the verdict cannot be over-read

The class is **cluster structure implemented as an edge-set restriction on the existing
pairwise family**: same derived `α`, same derived `L_pp / L_pn / L_nn`, only the set of
bonds changes according to a cluster decomposition. **Nothing here bears on cluster
structure implemented as a NEW many-body term** (an irreducibly ≥ 3-body α term, an
SU(4) `[1⁴]` volume term, a connected-sum volume additivity rule). That is a different
hypothesis with a different arity and is explicitly **not** under test.

## (a) Exact quantity computed, and from which corpus source

- **`B_AME(Z, A)`** — total nuclear binding in MeV from
  `computations/substrate/codata_constants.py::ame_binding_mev(Z, A)`, the public
  accessor for the vendored AME2020 publication table. Returns `mp.mpf`. No hand-typed
  literals.
- **`α = E₀ = m_e / (q₀(q₀ − 1))`** — formed in `mpmath.mpf` at ≥ 60 dps from
  `q_parameter.Q_50_DIGIT_STR` (proton pin, per the 2026-08-07/2026-08-15 R2 owner
  directive) and the CODATA `m_e` accessor.
- **`L_pp, L_pn, L_nn`** — the production per-bond suppressions, **convention D**,
  colour-weighted, writhe-normalised, reproducing the formula in
  `computations/mass_binding_dashboard.py::_bond_type_L` **at `mpf` precision**:
  `z = q₀³/(q₀²+1)`, `h = q₀ − 1/q₀`, `d_pn = −h(½ − δ/4)` via
  `_li_2_q_util.flavor_split_leading`, `L = −ln(z + d) − (Δe/2)·ln(1 − h)`.
  **Note, recorded in advance:** the production accessor `_bond_type_L` returns
  **`float`** (it casts at the return), so it cannot be called directly under the
  NO-FLOAT64 discipline. The probe re-forms the identical expression in `mpf` and
  cross-checks against the production floats **only to the float64 limit**, which will
  be reported as such and never as "exact".
- **Model binding for an edge set `E`:** `B_E = α · Σ_{(i,j) ∈ E} L_{type(i,j)}`, with
  bond type from the species of the two endpoints. Identical rule to `B_allpairs`; only
  `E` changes.

**Isotope set, fixed now (6 nuclides, `(Z, N)`):**

    ²H (1,1)   ³H (1,2)   ³He (2,1)   ⁴He (2,2)   ⁶Li (3,3)   ⁷Li (3,4)

## (a-bis) Pre-registered structural claim — falsifiable, and it is the main deliverable

Asserted **before** any number is computed, and put at risk:

> **S-C1 (subgraph monotonicity).** Every cluster-assignment scheme implemented as an
> edge-set restriction yields `E ⊆ K_A`. If the three derived per-bond energies
> `αL_pp, αL_pn, αL_nn` are all **strictly positive**, then `B_E ≤ B_{K_A}` for every
> such `E`, hence `r_E = B_AME/B_E ≥ r_{K_A}` **pointwise**. Three consequences:
>
> - **(i)** For a nucleus that is a **single cluster** under the scheme, `E = K_A`
>   exactly, so `r` is **unchanged**. Under the maximal-α scheme ²H = d, ³H = t,
>   ³He = h and ⁴He = α are all single clusters — so clustering is a **no-op on four of
>   the six** isotopes, and in particular **cannot move ⁴He's 1.647 at all**.
> - **(ii)** Clustering can only **raise** `r`. ⁶Li (0.743) and ⁷Li (0.639) can rise
>   toward 1; ⁴He (1.647), already above 1 and immovable, cannot fall.
> - **(iii)** Therefore the ⁴He super-pairwise excess — **the larger half of the
>   anomaly**, and the half already given a scope-(b) exclusion in §5 of the motivating
>   audit via the exact `K_A` Laplacian spectrum — is **invariant under the entire
>   cluster-edge-set class.** H_all is refuted by S-C1 alone, with no fit.
>
> **S-C1 is falsified if** any of `αL_pp, αL_pn, αL_nn` is ≤ 0 (edge removal could then
> raise `B`), **or** if any computed `r` for a single-cluster nucleus differs from its
> `K_A` value, **or** if some declared scheme leaves ⁴He non-single-cluster and moves
> its ratio. If S-C1 is falsified it is retracted in the report.

S-C1 makes the numerical step a **confirmation rather than a search**, which is the
point. The sign of `L` is an empirical input to it and is checked, not assumed.

## (b) What COUNTS AS SUPPORT — fixed numeric criteria

**H_all is supported only if** some declared (scheme, edge-rule) pair brings **all six**
isotopes to `|r − 1| ≤ 0.10` with **zero** new constants. (Under S-C1 this is expected
impossible; it is stated so S-C1 is genuinely at risk.)

**H_partial is supported only if both hold:**

- **S-i.** For at least one declared (scheme, edge-rule) pair, **both** ⁶Li and ⁷Li
  satisfy `|r − 1| ≤ 0.10`, with **zero** new fitted constants — same `α`, same `L`.
- **S-ii.** That same pair does **not** degrade the other four: `max |r − 1|` over
  {²H, ³H, ³He, ⁴He} does not increase relative to the `K_A` baseline.

## (c) What REFUTES it — fixed numeric criteria

- **R-i.** **No** declared pair brings both ⁶Li and ⁷Li within `|r − 1| ≤ 0.25`.
  Refutes H_partial.
- **R-ii.** ⁴He's `r` is unchanged across **every** declared pair. Refutes **H_all**
  regardless of what happens at ⁶Li/⁷Li — a class that provably cannot touch the
  largest deviation does not explain the residual.
- **R-iii.** A declared scheme requires `B_E` **below** the linear-chain edge set
  (`A − 1` bonds, the corpus's `B_sym` minimum) to reach `r ≈ 1`. The cluster edge set
  must lie **between** chain and complete graph to be a cluster statement at all; if
  unity needs less than a spanning connected graph, the agreement is edge-count
  arithmetic, not clustering.

Each fires independently and each is reported separately.

## (d) Total number of cluster-assignment schemes tried — **TWO**. Edge-set rules — **TWO**. Total evaluations — **FOUR**.

Fixed now. No third scheme, no third edge rule, no fifth evaluation. Any later
exploration is a **new** pre-registration, reported as such.

**Cluster-assignment schemes (2):**

| # | scheme | ²H | ³H | ³He | ⁴He | ⁶Li | ⁷Li |
|---|---|---|---|---|---|---|---|
| **C1** | maximal-α (standard cluster model) | d | t | h | α | α + d | α + t |
| **C2** | α-plus-free-nucleons (only a *filled* `[1⁴]` is a cluster) | p + n | p + n + n | p + p + n | α | α + p + n | α + p + n + n |

**Edge-set rules (2):**

| # | rule | edges |
|---|---|---|
| **E1** | intra-cluster only (the additivity lower bound) | complete graph inside each cluster; **no** inter-cluster edge |
| **E2** | intra + one inter-cluster bond per cluster pair | E1 plus `C(k,2)` bonds, `k` = cluster count |

**Bond typing, fixed now.** Intra-cluster edges are typed by endpoint species exactly as
in `B_allpairs`: a cluster with `z` protons and `n` neutrons contributes
`C(z,2)` pp + `z·n` pn + `C(n,2)` nn. **Inter-cluster edges in E2 are assigned the type
that MAXIMISES `B`** — whichever of `L_pp, L_pn, L_nn` is largest, determined from the
computed values, not chosen per isotope. This is deliberately the **most favourable
possible** inter-cluster assignment, so a refutation under E2 is a refutation under
*every* inter-cluster bond assignment.

No optimiser, no seed, no tolerance to tune: all four evaluations are closed-form sums
over enumerated edges, in `mpmath.mpf` at ≥ 60 dps end to end.

## (e) What is explicitly NOT support

Stated in advance so it cannot be argued afterwards:

1. **A per-isotope free constant is NOT support.** Any `c_i` varying with `(Z, A)` makes
   the model a reparametrisation of the data and carries zero information. If a
   per-isotope constant is needed, that is a **refutation**, reported as one.
2. **A global rescale of `α` is NOT support.** `α` is derived
   (`m_e/(q₀(q₀−1))`, proton pin). Refitting it is a CAL-4 violation, and by S-C1 it
   cannot fix a non-monotone ratio anyway — a global scale moves every `r` by the same
   factor and cannot reverse an ordering.
3. **A free choice of cluster decomposition per isotope is NOT support** — it is
   unfalsifiable. With the decomposition free one may always choose the edge count that
   reproduces the target, and "clustering" then constrains nothing. Only the two schemes
   fixed above make H a claim at all.
4. **Adding a new many-body term is NOT support for THIS hypothesis.** It is the other
   hypothesis (already open in the corpus; see prior work below) and will not be
   presented as a cluster-edge-set result.
5. **Matching ⁴He alone is NOT support.** One number is not a test. Nor is matching
   ⁶Li alone.
6. **A good fit obtained after ⁸Be, ⁹Be, ¹²C, ¹⁶O are added is NOT support.** The
   isotope set is fixed above at six. Extending it is a new pre-registration.
7. **"Suggestive" is not support**, and neither is a second construct landing near the
   same value — that is the numerology signature already recorded at §7 of the
   motivating audit.

## Prior work found by corpus-grep, run BEFORE this file was written

The connected-sum / cluster route is **not new to this corpus**, and this front is
therefore largely a *re-scoping and structural* exercise, not a discovery one. Grep run
across `docs/audits/`, `docs/coordination/`, `content/`, `computations/` for
`connected sum` / `satellite` / `alpha[- ]cluster` / `clustering`:

- [`computations/deltalambda/alpha_cluster_volume_additivity_probe.py`](../../computations/deltalambda/alpha_cluster_volume_additivity_probe.py)
  + [witness](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json) —
  reads the A ≥ 5 link as a **connected sum / split union** of A ≤ 4 cluster units and
  uses **additivity of hyperbolic volume** under both. Zero-fit. ⁸Be validates to
  **+0.16 %**. This is exactly the "connected-sum / satellite decomposition of the braid
  closure" the front asks about, and it already exists.
- [`2026-07-13-inter-cluster-bond-term-derive-or-refute.md`](2026-07-13-inter-cluster-bond-term-derive-or-refute.md)
  — the deficit `B_AME − B_add` characterised; **three** pre-registered zero-freedom
  bond hypotheses (cluster-spin `j`, fixed deuteron-channel `j = 3`, strand-count `j`)
  all **NEGATIVE**. Structural finding retained: the deficit is **~linear in
  light-cluster nucleon count** (0.78 MeV/nucleon, max dev 5.8 %, 3 points, guarded)
  and is **not** a function of bond spin.
- [`2026-08-02-alpha-cluster-su4-extensive-term.md`](2026-08-02-alpha-cluster-su4-extensive-term.md)
  — the proved SU(4) gate `dim[1^A] = C(4,A)`
  (`QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff`) gives the **categorical origin
  of α-clustering** (no `[1⁵]` ⇒ A > 4 must break into α's). `B/n_α` has CV **0.053**
  vs `B/A`'s 0.148. The audit is explicit that the **structure** is motivated and the
  **magnitude** (~29.8 MeV/α) is **empirical, not derived**, and refuses the `8G·k`
  scale-setting as numerology.
- Content blocks `mass-theory/alpha-cluster-activation-gate` and
  `mass-theory/alpha-cluster-model-g-closure`;
  [`2026-07-13-alpha-activation-brunnian-derive-or-refute.md`](2026-07-13-alpha-activation-brunnian-derive-or-refute.md).

**Nothing is newly declared open by this front.** The cluster axis is already open in
the corpus at the *magnitude* leg; this pre-registration adds only the edge-set reading
and the S-C1 structural question, neither of which appears above.

## Prior expectations, recorded so they cannot be revised

- **S-C1 is expected to hold**, and therefore **H_all is expected REFUTED with no fit**,
  by R-ii. That is the anticipated headline.
- **H_partial is expected to be, at best, partially supported.** Removing edges raises
  ⁶Li/⁷Li from 0.743/0.639, but `K_A` over-counts badly at A = 6,7 (15 and 21 pairs)
  while E1 under C1 gives only `C(4,2) + C(2,2) = 6 + 1 = 7` and
  `C(4,2) + C(3,2) = 6 + 3 = 9` — a factor 2.1–2.3 reduction in edge count against a
  needed factor of 1.35–1.56. **E1 is expected to OVERSHOOT** (r > 1), and E2 to land
  nearer. If both overshoot and undershoot without bracketing, R-i fires.
- The sign fact from the sibling front is recorded so it is not re-derived: the residual
  `R(²H) = −0.61` MeV is the **only negative** one, so **any non-negative correction
  fails at ²H** (`2026-08-26-faddeev-niemi-qh34-verdict.md` §S2). Under C1, ²H is a
  single cluster, so the cluster-edge-set class **cannot** address it either — the same
  no-op as ⁴He, in the opposite direction. Bean `qou-39bx` (a sibling) holds the
  deuteron; nothing here duplicates it.

## Reporting commitment

The report states the verdict against (b)/(c) verbatim, per hypothesis, names the scope
**(a)** or **(b)** per AGENTS.md and cites the invariant if **(b)**, and says plainly if
the honest answer is "clustering does not explain it". No float64 anywhere; no agreement
reported as "exact" or "to N digits"; `mpmath.mpf` end to end. Every one of the four
declared evaluations is reported, including the boring and the failing ones.
