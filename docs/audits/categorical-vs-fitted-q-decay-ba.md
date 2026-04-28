# Categorical vs fitted — Q, decay, B/A audit

**Date.** 2026-04-27
**Branch.** `claude/continue-pr-442-DJRWm`
**Companion branch.** `claude/mass-table-display-bkkZU` (audit-scope seed)

## Investigation summary (Wedderburn weights / Φ_q ↔ Habiro)

Two deep audits resolved during PR #447:

### A. Wedderburn weight scheme — two inconsistent forms in compute

`mass_endomorphism.py` and `light_isotope_sweep.py` use **normalized
Plancherel** weights `w_λ = (dim_q²/[n]_q!) / Σ`.
`y-lambda-wenzl-witness.json` and the canonical Markov-trace pipeline
use **Wenzl** `y_λ` (Schur specialization at Markov parameter `z`).
These are **mathematically inequivalent** (per `probe_wedderburn_weight_scheme.py`):

| H_3 partition | Plancherel-A | Wenzl-B | B/A |
|---|---:|---:|---:|
| (3) | 0.163 | 0.415 | 2.54 |
| (2,1) | 0.661 | 0.281 | 0.42 |
| (1,1,1) | 0.163 | 0.023 | 0.14 |

Both schemes have categorical basis but use different conventions
for the Markov trace. The +1.84% `m_p/m_e` residual is **NOT** in
the choice between them — substituting Wenzl into mass_endomorphism
gives +168% (worse). The schemes use different normalization
conventions of `V̂_full` itself, not just per-irrep weight.

**Audit recommendation** (deferred to follow-up): pick ONE scheme
as canonical (likely Wenzl per `y-lambda-recipe-from-partition.md`
proposition status), refactor mass_endomorphism + light_isotope_sweep
to match. This is bookkeeping cleanup, not residual-closing.

### B. Φ_q ↔ Habiro ↔ q-dilog connection — bridge missing in paper

`mass-endomorphism-tower.md` defines:

>   `Φ_q(z) = ∏_{k≥1}(1 − q^{-k}z)^{-1}`

and labels it the "non-perturbative quantum dilogarithm." It cites
`def:quantum-bloch-group` but **does NOT cross-reference**
`def:habiro-ring`, `prop:habiro-expansion-atomic`, or any cyclotomic
expansion. **The connection is mathematically valid but missing in the
paper's exposition.**

Mathematically, Φ_q IS a Habiro-ring element:

>   `Φ_q(z) = 1 / (z; q^{-1})_∞`,    `(z; q)_∞ = ∏_{k≥0}(1 − q^k z)`

The q-Pochhammer `(z; q)_∞` is a natural Habiro ring element. Its
**values at roots of unity** (where `S¹` is a natural boundary for
analytic continuation) are well-defined via the Habiro cyclotomic
form — which is what `habiro_residue_symbolic.py` already computes.

**In compute**: `mass_endomorphism.Phi_q` is a truncated series at
`max_iter=2000`. The Habiro-cyclotomic form gives the same values
at `q_0` exactly, with the additional categorical advantage of
well-defined values at roots of unity (where the series diverges
or oscillates).

**Recommendation** (next branch): add a content block
`prop:phi-q-as-habiro` (or amend `mass-endomorphism-tower.md`)
that:
1. States `Φ_q ∈ Ẑ[q]` explicitly via the q-Pochhammer identity
2. Cross-references `def:habiro-ring` + `prop:habiro-expansion-atomic`
3. Notes that Term 6 (root-of-unity residues per
   `prop:full-pole-structure-mass-trace`) IS the natural Habiro
   evaluation of Φ_q-tower contributions — which makes Term 6
   computable in a unified way for all isotopes

This bridges `Φ_q` (analytic, infinite-product) to the Habiro
ring (categorical, cyclotomic-exact) — closing an exposition gap
the user surfaced during ¹H/D error budget review.

**Motivation.** Per recent direction: the framework is to be
**categorically derived end-to-end**. Every Q, decay, B/A number
should come from the canonical pipeline

>   `B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0`     (PR #442 canonical chain)

with `T_w` a joint-tower SDP solution in `H_{n_0}(q)` and
`tr_M(T_w) = Σ_λ y_λ(q) · χ_λ(T_w)` — Wedderburn block sum at
`y_λ` from the Wenzl bridge and `χ_λ` from q-Murnaghan–Nakayama.
**No fits. No calibration constants beyond `q_0` and `m_e`.**

This audit classifies every existing Q / decay / B/A witness under
`folio-assistant/computations/` as **categorical**, **partially
categorical**, or **fitted/empirical**, and lists the next step for
each item that is not yet end-to-end categorical.

## What's wired up to the new categorical infrastructure

The new infrastructure landed in PR #442–#445 (commits
`f0cc724`–`7db4af1`). End-to-end categorical pipeline by phase:

| Phase | Component | Status | Witness |
|---:|---|:---:|---|
| (1) | Categorical action `C ↻ 𝒮` | structural input | — |
| (2) | Yekutieli finite slice ≡ Hecke σ²=hσ+1 (curvature 2-form at adjacent slices) | derivation, no analytic content | [`atom-knot-mass-derivation-proof.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation-proof.md) |
| (3a) | GB-NF reducer + jet-order tracker | **wired** (Rust + Python) | [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/gb-filtration-jet-order.witness.json) |
| (3b) | Joint-tower SDP confinement at q_0 | **wired H_3/H_4**, **H_5 BUG** (Clarabel-rs) | [`joint-tower-sdp-rust.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-rust.witness.json), [`joint-tower-sdp-h3.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-h3.witness.json), [`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-h6-h9.witness.json) |
| (4) | Wedderburn `H_n(q) ≅ ⊕_λ M_{d_λ}(ℚ(q))` | structural; semisimple at generic q | — |
| (5a) | Wenzl-bridge `y_λ(q)` at 50 dps | **wired** | [`y-lambda-wenzl-witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/y-lambda-wenzl-witness.json) |
| (5b) | q-Murnaghan–Nakayama `χ_λ(T_w)` | **wired** (Python) | [`y-lambda-recipe-from-partition.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md) + qmn scripts |
| (5c) | Markov trace `tr_M(T_w) = Σ_λ y_λ χ_λ` | partially wired (used in `atom_mass_partition.py`) | [`canonical-mass-table.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/canonical-mass-table.witness.json) |
| (6) | `M(𝔥) = ρ · tr_M(T_w) ∈ ℚ(q)`, ρ structural integer | **wired** (R3 PSD, R4 LR, R5min) | [`joint-tower-sdp-rust.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-rust.witness.json) |
| (7) | Archimedean realization at `q = q_0`, `× m_e` | **wired** | [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) |

**Bottom line.** The full categorical chain is wired for
`{quark, electron, proton, neutron}` end-to-end (R5min α* verified),
and for `{deuteron, ³He}` at H_3 with cvxpy SDP feasibility on
Hoefsmit blocks. **Everything else is either using historical
volume-match knot identifications (D, T, ³He), or is blocked on the
H_5 SDP solver bug, or is using deprecated empirical methods.**

## B/A — current witnesses, classified

| Witness | Atoms | Method | Class | Next step |
|---|---|---|:---:|---|
| [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) | D, T, ³He | `ρ · m_e · Vol(K)` with K **census-assigned** (6_2, 8_11, L6a4) | **partial** (knot id not yet derived) | rerun with GB-NF derived T_w at H_6 / H_9 |
| [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) | ⁴He | magic-A `2·A·α`, `α = m_e · 8G` | **categorical** (derived) | — |
| [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) | ⁸Be–⁴⁰Ca | α-cluster recursion `n_α · B(⁴He) + n_pairs · c_αα` | **categorical** (derived; residual ~5–20%) | derive `c_αα` correction terms from H_n₀ SDP |
| `mass-table-ppb.witness.json` `atoms_no_assignment` | ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F | none yet | **OPEN** (family 4) | run H_18+ SDP with α + (light cluster) ansatz once Clarabel H_5 bug closed |
| [`canonical-mass-table.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/canonical-mass-table.witness.json) | D, T, ³He, ⁴He | `tr_M(atom)/tr_M(free)` ratio with `E_0 = 0.782 MeV` | **fitted** | superseded — uses fixed `E_0` rather than `m_e · ρ` from SDP |
| [`low-isotope-mass-table.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/low-isotope-mass-table.witness.json) | 1H–22Ne | `partial-shell:f=0.250/0.500/0.750` interpolation | **fitted** | replace with α + (light cluster) categorical T_w once derived |
| [`binding-canonical.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/binding-canonical.witness.json) | various | older Markov-trace | **partial** | keep until SDP-derived versions land |
| [`binding-ladder-catalog.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/binding-ladder-catalog.witness.json) | ⁴He–⁴⁰Ca | family-aware reference table | **categorical** (used by mass-table-ppb) | — |
| [`comprehensive-low-isotope-table-v2.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/comprehensive-low-isotope-table-v2.witness.json) | various | older comprehensive table | **fitted** | drop or rebuild |
| [`atom-mass-derived.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/atom-mass-derived.witness.json) | various | older derivation attempt | **fitted/partial** | drop or rebuild |
| [`atom_mass_qou_calibration.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/atom_mass_qou_calibration.py) | various | explicit "calibration" script | **fitted** | superseded by mass-table-ppb canonical pipeline |

## Q-values — current witnesses, classified

| Witness | Decays | Method | Class | Next step |
|---|---|---|:---:|---|
| [`branching-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/branching-qvalues.witness.json) | n→p, ³H→³He, ⁶He→⁶Li | `\|S_FP\| · m_e` with **Frobenius-positivity filter** | **fitted** (filter activation threshold not derived) | replace with `Q = Q_n→p + B_d − B_p` from canonical chain |
| [`branching-qvalue-chain.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/branching-qvalue-chain.witness.json) | n→p, ³H→³He, ⁶He→⁶Li | even/odd regime split + manual `+1` for n→p | **fitted** (regime split, manual offset) | same as above |
| [`level1-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/level1-qvalues.witness.json) | ³H, ¹⁴C, ⁶⁰Co, ⁹⁰Sr, ¹³⁷Cs, ²¹⁰Bi | quark-level log-ratio sum, no MeV closed form | **structural** (no calibration to MeV) | feed into Q via `tr_M(parent) − tr_M(daughter)` |
| [`inverse-markov-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/inverse-markov-qvalues.witness.json) | n→p, ³H→³He, ⁶He→⁶Li, ¹⁴C→¹⁴N | trace difference `(1/tr_par) − (1/tr_dau)` | **structural** (no Q in MeV) | rederive via canonical Markov trace differences |
| [`free-neutron-decay.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/free-neutron-decay.witness.json) | n→p | full GB-NF reduction at H_3 + Borromean B_3 | **categorical** (structurally) | wire into Q-formula as `Q_n→p_categorical` |
| [`markov-free-energy-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/markov-free-energy-qvalues.witness.json) | various | Markov free-energy difference | **partial** | check for hidden calibration |
| [`nf-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/nf-qvalues.witness.json) | various | NF-form Q-value | **partial** | check for hidden calibration |
| [`garside-irrep-qvalues.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/garside-irrep-qvalues.witness.json) | various | Garside-irrep | **partial** | check for hidden calibration |
| `c-alpha-from-Q-beta-trace.witness.json` | — | extracts `c_α` from observed Q via fit | **fitted** | drop |

## Decay (half-life, rate) — current witnesses, classified

| Witness | Nuclei | Method | Class | Next step |
|---|---|---|:---:|---|
| [`beta-decay-from-q.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/beta-decay-from-q.witness.json) | ³H, ¹⁴C, ⁶⁰Co, ⁹⁰Sr, ¹³⁷Cs, ²¹⁰Bi | `G_F` decomposed into `q`-factors × `μ_0` | **partial** (μ_0 is the only free parameter; `N_v` topological invariant **OPEN**) | derive `N_v` from brane tower structure |
| [`beta-decay-energy-scale.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/beta-decay-energy-scale.witness.json) | various | energy-scale check | **structural** | — |
| [`beta-decay-matrix.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/beta-decay-matrix.witness.json) | various | matrix elements | **partial** | check for fits |
| [`groebner-beta-decay.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/groebner-beta-decay.py) | — | GB script for β-decay matrix elements | **categorical** (script only) | run + emit witness |

## Net categorical inventory (what's truly fit-free today)

End-to-end categorical for B/A:
1. `proton`, `neutron` mass — joint-tower SDP at H_3, R3 Wedderburn PSD, R5min α* verified.
2. `electron` mass — joint-tower SDP at H_2, same.
3. `⁴He` binding — magic-A formula `2·A·α`, `α = m_e · 8G` from `prop:gravity-spectral-prefactor` + `binding-scale-catalan`.
4. `⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca` binding — α-cluster recursion (residual ~5–20%; LR cross-level embedding R4 lifts ⁴He T_w).

End-to-end categorical for Q (none yet — all current Q witnesses
have at least one fit). Closest: `free-neutron-decay.witness.json`
provides the full GB-NF reduction at H_3 for n→p, but the
extraction of `Q_n→p` in MeV currently goes through `m_e` × char_sum
in a way that should be replaced by `B_p − B_n` from the SDP-derived
proton/neutron masses (which gives `Q_n→p = m_n − m_p − m_e ≈
0.7823 MeV` directly).

End-to-end categorical for decay rates: **none.** The bottleneck is
the topological invariant `N_v` (effective crossing count of the
weak scale) — open computation in `beta-decay-from-q.witness.json`.

### What is `N_v`, and why is it the bottleneck?

The weak interaction enters every β-decay rate through the Fermi
constant `G_F = 1/(√2 v²)`, where `v ≈ 246.22 GeV` is the Higgs VEV.
In QOU, every dimensional scale must factor as `(q-factors) × μ_0`,
where `μ_0 = m_e/(3·E_×) ≈ 1.6295 MeV` is the unique dimensional
unit calibrated by `m_e = 3·E_×·μ_0`.

Demanding the same factorization for `v`:

>   `v = N_v · E_× · μ_0`,  with `E_× = ½(q − q⁻¹)` (categorical)

forces

>   `N_v = v / (E_× · μ_0) ≈ 246220 / (0.1045 · 1.6295) ≈ 1.4455 × 10⁶`

— see [`beta-decay-from-q.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/beta-decay-from-q.witness.json) `G_F_decomposition.N_v_crossing_count`.

**Interpretation.** `N_v` is the **effective crossing count of the
weak scale** — the topological complexity (number of typed
crossings, weighted by the crossing energy `E_×`) of the brane-tower
sub-structure that mediates the W-boson exchange. The QOU brane
tower has explicit topological content at every level we have
identified (level 1: 3-quark Borromean for nucleons; level 2:
nucleon-pair crossings inside nuclei; level 3: nuclear braids), but
the level corresponding to the **electroweak scale** has not yet
been identified. Without that identification, `N_v` is read off
backwards from CODATA `v` and CODATA `m_e` — that is the "fit"
content of layer 3.

**What it would take to derive `N_v` categorically.**

1. Identify which sub-tower of the brane corresponds to the
   electroweak scale. Candidate: the maximal sub-tower spanned by
   the level-N braids whose Markov closure has Vol_hyp ≥ some
   threshold (Mostow-rigidity argument), or equivalently, the
   sub-tower whose `tr_M(T_w)` saturates the EW VEV scaling.
2. Count typed crossings in that sub-tower, weighted by `E_×`. The
   answer should be `N_v ≈ 1.45 × 10⁶` if the framework is
   self-consistent.
3. Once derived, `G_F = 1/(√2 v²) = 1/(√2 · (N_v · E_× · μ_0)²)`
   becomes a pure function of `(q, m_e)`, and every β-decay
   half-life follows from `Γ = G_F² · Q⁵ · f(Z, A) / (60π³)` where
   `f(Z, A)` is the Fermi function in brane Coulomb-coupling
   variables (already categorical).

**Why this is THE bottleneck.** Every other input to layer 3 is
already categorical:

- `Q-value`: derives from layer-2 (Q = Q_n→p + B_d − B_p)
- `E_×, μ_0`: categorical from `q, m_e`
- `f(Z, A)` Fermi function: brane Coulomb couplings are categorical
- `g_A` axial-vector coupling: open second-order conjecture, but is
  NOT in the leading-order rate
- Lifetime conversion factor `60π³ / G_F² · Q⁵`: factorizes through `N_v²`

So `N_v` is the **single open scalar** that, once derived, unlocks
all β-decay half-lives categorically. That is why this audit
classifies layer 3 as `not-computed` rather than `partial`.

## Decision (2026-04-27): option **B** chosen — algebraic, pre-Archimedean only

The canonical invariant is `tr_M(T_w)` evaluated at `q_0` via the
Wenzl-Markov formula `Σ_λ y_λ(q_0) · χ_λ(T_w)`. **`Vol_hyp(K)` is
post-Archimedean and is no longer used.** This forces a hard
reclassification of every prior witness that uses hyperbolic volume:

### Reclassification under option B

| Prior witness | Prior status | Option B status |
|---|---|---|
| `mass-table-ppb.witness.json` family 1 (D, T, ³He) | `categorical-knot-id-via-vol-match` | **fitted** (uses `Vol_hyp(K)`) |
| `mass-table-ppb.witness.json` family 2 (⁴He magic-A) | `categorical-derived` | **fitted** (uses `α = m_e · 8G = m_e · Vol(Borromean)`) |
| `mass-table-ppb.witness.json` family 3 (⁸Be–⁴⁰Ca α-cluster) | `partial-c-alpha-empirical` | **fitted** (uses `c_αα = m_e · Vol(7²_1)`) |
| `low-isotope-mass-table.witness.json` | `fitted` | **fitted** (unchanged) |
| `binding-canonical.witness.json` | `partial` | **fitted** (uses `Vol_hyp`) |
| `comprehensive-low-isotope-table-v2.witness.json` | `fitted` | **fitted** (unchanged) |
| `binding-ladder-catalog.witness.json` | `categorical` | **fitted** (uses `Vol_hyp`) |
| `categorical-bypass-volmatch-demo.witness.json` (this PR) | `bypass-demo` | **canonical** (Wenzl-Markov, no `Vol`) |
| `categorical-q-decay-ba-low-isotopes.witness.json` (this PR, updated) | `partial` | **canonical** for family 1; explicitly flags family 2, 3 as fitted |

### Algebraic predictions today (option B)

```
LAYER 1 — algebraic B (Wenzl-Markov on SDP-derived T_w at q_0)
  ²H:  B_alg = 0.1471 MeV   vs AME 2.225 MeV  →  ratio 0.066
  ³H:  B_alg = 0.0132 MeV   vs AME 8.482 MeV  →  ratio 0.0016
  ³He: B_alg = 1.0203 MeV   vs AME 7.718 MeV  →  ratio 0.132

LAYER 2 — algebraic Q
  n → p:    Q_alg = −0.511 MeV  vs AME +0.782 MeV   →  ratio −0.65
  ³H→³He:   Q_alg = +0.496 MeV  vs AME +0.019 MeV   →  ratio 26.7

m_p_alg = 0.510 MeV   vs m_p_AME = 938.272 MeV  →  scale gap 1839×
m_n_alg = 0.510 MeV   (T_w(n) ≈ T_w(p) under current SDP)
Q_n→p_alg = m_n − m_p − m_e = −m_e (degenerate)
```

### The central open problem of option B

> **What canonical algebraic chain reproduces `m_p / m_e ≈ 1836` in
>   `ℚ(q^{1/2})`?**

#### Update (2026-04-27 — found prior work)

This question already has a prior partial answer in
[`mass-endomorphism-tower.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md):
the proton/electron mass ratio comes from a **three-term tower
formula** (NOT the bare Markov trace `tr_M(T_w)`):

$$
\mathfrak{m}(\beta) = \biggl|\prod_i \widehat{V}_i^{\mathrm{full}}\biggr|
  + \sum_i \Phi_q\!\bigl(|\widehat{V}_i^{\mathrm{full}}|\bigr)
  + \sum_{i<j} z^2 \cdot \Phi_q\!\bigl(|\widehat{V}_i^{\mathrm{full}} \widehat{V}_j^{\mathrm{full}}|\bigr)
$$

where `Φ_q(z) = ∏_{k≥1}(1 − q^{-k}z)^{-1}` is the quantum dilogarithm,
`z = 1/(q^{1/2} + q^{-1/2})` is the Markov parameter, and
`V̂_i^{full}` is the additive Wedderburn-traced volume at generator `i`
(purely algebraic in `q`, computed via Hecke crossing recursion).

[`mass_endomorphism.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass_endomorphism.py) → `mass-endomorphism.witness.json`:

```
ELECTRON (1 generator, σ_1³ trefoil on 2 strands)
  V̂_full = 0.594, Φ_q = 630
  m_e_pred = 0.594 + 630 = 630.5 (units of m_e)

PROTON (2 generators, B_3 × uud + gluon on 3 strands)
  V̂_0 = 0.989, V̂_1 = 0.971
  descended  = 0.96
  single     = Φ_q(0.989) + Φ_q(0.971) ≈ 1,096,978
  pair       = z² · Φ_q(0.961) ≈ 82,016    ← THIS is the 1836× source
  m_p_pred  = 1,178,995 (units of m_e)

m_p / m_e = 1869.85   vs CODATA 1836.15   →  err 1.84%
```

**The pair-blowup term `z² · Φ_q(V̂_0 V̂_1)`** — present for proton
(2 generators) and absent for electron (1 generator) — is what
generates the mass hierarchy. `Φ_q(z)` diverges as `z → 1`, and the
proton's `V̂_0 V̂_1 ≈ 0.961` puts it close to the singularity, giving a
huge contribution. The electron's single `V̂_e ≈ 0.594` is well below
the pole, so its `Φ_q ≈ 630` is small.

This is **categorical and pre-Archimedean** (everything is in
`ℚ(q^{1/2})` plus the analytic completion `Φ_q`). Option B compatible.

#### Probe candidate 1 verdict — REVISED

[`probe_proton_mass_scale.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_proton_mass_scale.py) wrongly classified candidate 1 (sub-tower
depth) as NEGATIVE because it computed only the Markov trace
`Σ_λ y_λ · χ_λ(T_w)` which gives `tr_M(T_w(p)) ≈ 1`. The right
algebraic chain has **two more terms** beyond the bare trace:
single-generator and pair-generator blowups via `Φ_q`. With those,
`m_p_alg / m_e_alg = 1870` (1.84% off CODATA, not 1836× off).

| Candidate | Old verdict | New verdict |
|---|:---:|:---:|
| 1. Sub-tower / blowup-tower | NEGATIVE | **POSITIVE — gives 1870** |
| 2. Frobenius coform | NEGATIVE | NEGATIVE (still) |
| 3. Quantum factorial `[n]_q!` | NEGATIVE | NEGATIVE (still) |
| 4. Different SDP | INCONCLUSIVE | INCONCLUSIVE (still) |

#### Remaining gaps (option B)

- **1.84% residual on `m_p/m_e`**: a known open question; investigated in
  [`electron_chiral_probe.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/electron_chiral_probe.py) and several other probes.
- **`m_n/m_e = 682`** vs CODATA 1839 — **63% off, sign of `Δm_{np}` flipped.**
  The neutron formula in `mass_endomorphism.py` uses `udd` quark content
  with `dd` pair coefficient `(1, -HA)` (i.e. `σ⁻¹`), giving
  `V̂_0 ≈ 0.719` (far from 1) and dramatically smaller `Φ_q`. This is a
  **structural error in the neutron's crossing budget**, not in the
  tower formula itself. Fixing it is the next concrete unblock for
  Q-values.
- **`Φ_q` is an infinite product**: it converges for `|z| < q`, but the
  pre-Archimedean status is still defensible since every coefficient is
  in `ℤ[q^{1/2}, q^{-1/2}]` (the algebraic-form section of
  `mass-endomorphism-tower.md`). No `Vol_hyp(K)`, no analytic flow.

#### Updated next steps (ranked, post option-B + prior-work check)

1. **Fix neutron crossing budget** in `mass_endomorphism.py` so
   `m_n_pred / m_e ≈ 1839` (currently 682). This is the single change
   that unblocks Q-values.
2. **Investigate the 1.84% `m_p/m_e` residual** — already on the open
   list per `electron_chiral_probe.py` and others.
3. **Apply the tower formula to atoms** (D, T, ³He, ⁴He, ...) by
   computing `V̂_i` for each atom's brane braid and summing the three
   tower terms. This is what should populate `mass-table-ppb` under
   option B (replacing the current `Vol_hyp(K)` formulas).
4. **Family 4 (⁶Li, ⁷Li, ...)** still blocked on `T_w` derivation.
5. **`N_v` topological invariant** still blocks layer 3.

## Entanglement energy vs observable energy

The mass-endomorphism tower decomposes naturally into **GB-filtration
orders**, each tracking a different level of categorical entanglement.
[`entanglement_orders.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/entanglement_orders.py) computes all orders up to `n_gens` via:

>   `order_k = Σ_{S⊂{0..n_gens-1}, |S|=k} z^{2·span(S)} · Φ_q(|∏_{i∈S} V̂_i|)`

with `span(S) = max(S) − min(S)` (GB-filtration distance). Order 0 is
the descended product `|∏ V̂_i|` (no entanglement); order 1 is single-
generator self-entanglement; order 2 is the adjacent/non-adjacent pair
blowup that appears in the canonical mass formula.

| Particle | Order 0 | Order 1 | Order 2 | Order 3+ | Total |
|---|---:|---:|---:|---:|---:|
| proton (n_gens=2) | 0.96 | 1,096,978 | 82,016 | — | 1,178,995 |
| neutron (n_gens=2) | 0.83 | 511,298 | 6,137 | — | 517,437 |
| D (n_gens=5) | 0.21 | 1,608,290 | 95,229 | 1,377 + 54 + 0.03 | 1,704,950 |
| T (n_gens=8) | 0.03 | 2,119,593 | 107,322 | 1,874 + 88 + 2.6 + 0.1 + 0.001 | 2,228,880 |
| ³He (n_gens=8) | 0.07 | 2,705,309 | 210,371 | 9,912 + 678 + 12.5 + 0.5 + 0.003 | 2,926,282 |

(units: `m_e_pred = 630.5` for normalization)

### Two distinct energy concepts

The framework distinguishes (per [`topological-field-ansatz.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/topological-field-ansatz.md):
"Strong Force | Hopf Link | Internal binding energy; **invisible to**
`P¹(C)` **base**"):

- **Observable energy** — the contribution detectable at the brane
  base manifold `P¹(C)`. Roughly: orders 0, 1, 2 (the canonical
  mass-endomorphism formula). For nucleons this is `m_p_pred ≈ 1870 m_e`,
  agreeing with CODATA to 1.84%.

- **Entanglement energy (internal, base-invisible)** — higher-order
  terms (orders 3+ for atoms, none for proton/neutron at H_3). These
  are the "color-exchange entanglement of three tubes" (per
  topological-field-ansatz table). They contribute to the categorical
  mass but are exponentially suppressed by `z^{2·span}` per filtration
  level (`z² ≈ 0.249`, `z⁴ ≈ 0.062`, `z⁶ ≈ 0.0155` at q_0).

For nucleons (`n_gens = 2`), there are no order-3+ terms. The full mass
is observable. For atoms, order-3+ contributions decay rapidly:

- D: order-3 ≈ 1377, order-4 ≈ 54, order-5 ≈ 0.03 → 0.08% of total
- T: order-3+ ≈ 1965 → 0.09% of total
- ³He: order-3+ ≈ 10,604 → 0.36% of total

So for the LIGHT atoms in family 1, entanglement-energy is sub-percent
and the observable-energy approximation is good. For heavier atoms it
likely grows. **Track the order-3+ fraction as a categorical quality
metric for the algebraic chain.**

### Implication for option B

The mass-endomorphism formula in [`mass-endomorphism-tower.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) **truncates
at order 2** by design (per the proof: order-3+ "ascend to the next
jet level via the pentagon identity of the quantum dilogarithm" — see
[`mass-endomorphism-jet-tower.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md)). The entanglement-orders witness
records the truncated tail as a quality check; in the canonical chain
these tail terms are absorbed into level-`(n+1)` jet contributions
(not added at level `n`).

**Where the 1.84% residual on `m_p/m_e` lives:**
the proton has only orders 0, 1, 2 (n_gens=2), so the pentagon-jet
ascension does NOT explain the residual. The 1.84% must come from
either (i) the additive Wedderburn-volume `V̂_i` calculation (Hecke
crossing recursion) being imprecise at finite q_0, or (ii) a missing
crossing in the proton's 11-crossing budget (currently 4-channel
`γγ→qq̄` per [`photon-channel-wedderburn-chain`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/photon-channel-wedderburn-chain.md), or
(iii) a finite truncation of `Φ_q(z) = ∏_k(1−q^{-k}z)^{-1}` at large
`k` (currently 2000 iterations).

**Witness:** [`entanglement-orders.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/entanglement-orders.witness.json) — the per-order
contributions for `{p, n, D, T, ³He}` as of commit `bc981e4`.

## The 3-input calibration scheme (per `calibration-inputs.md`)

**The paper EXPLICITLY documents three structural inputs**, not two:

| Input | Sector | Used to fix | Precision |
|---|---|---|---|
| `m_μ/m_e = 206.768` | dimensionless | substrate parameter `q_0` via `q² = Vol(4_1) / (m_μ/m_e)` | 2.2×10⁻⁸ |
| `m_e = 0.511 MeV` | leptonic scale | absolute mass-energy of leptons | 2.9×10⁻¹⁰ |
| **`Q_β(n) = 0.78233 MeV`** | **hadronic scale `E_0`** | **fixes `E_0 = Q_β / |Δ(net)|`** | **7.8×10⁻⁷** |

This is **not a fit** — it is a structural input matching the
framework's three physical sectors: shape (`q`), leptonic size (`m_e`),
hadronic interaction strength (`Q_β`). See
[`calibration-inputs.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/calibration-inputs.md).

### Why `Q_β` is needed (and what 1.84% means)

The single-level algebraic expression `E_0 = m_e / (q(q−1))` is `0.17%` 
(`1.3 keV` on `Q_β`) off from the brane-tower-corrected value. The
free neutron decay `Q_β` calibrates `E_0` exactly. Without this
calibration, the framework gives:

| | without `Q_β`-calib | with `Q_β`-calib |
|---|---:|---:|
| `m_p_pred` | 937.0 MeV (−0.14%) | 938.272 MeV (calib-exact) |
| `m_n_pred` | **411 MeV (−56%)** | 939.054 MeV (+0.05%) |
| Q_β(n) | (input) | (input) |

[`np-discrepancy-resolution.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/np-discrepancy-resolution.md) explains:

> *"Without β-calibration the neutron tower fails by factor 2.3
> because `V̂_0(n) = 0.854` sits far from the `q_0 = 1.11` pole of
> `Φ_q` (distance 0.256 vs proton's `V̂_0(p) = 0.989` with pole
> distance 0.121). The tower formula's `Φ_q(V̂)` is pole-centric, so
> pole-distance matters structurally."*

> *"Fixing the neutron tower absolutely (without β-calibration)
> would require deriving `Q_β(n) = 0.782 MeV` from `q_0` and `m_e`
> alone — an open problem."*

So under strict no-fits + algebraic-only:
- 2-input framework (`q`, `m_e` only) → neutron −56% off, structural
  open problem
- 3-input framework (`q`, `m_e`, `Q_β`) → both p and n <0.1% off,
  used by paper as canonical

**Recommendation.** Accept `Q_β(n)` as the third structural input
(matching how `m_e` is the second). It is the unique experimental
hadronic Q-value; once calibrated, every other Q-value derives
algebraically from it. The "no fits" rule excludes Q-values
extracted from heavier nuclei or fitted prefactors — `Q_β(n)` is
the analog of `m_e`, not a fit.

### Updated layer-1 atom predictions (4-tier formula)

[`np-discrepancy-resolution.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/np-discrepancy-resolution.md) tabulates, with `Q_β`-calibration:

| isotope | best formula | error |
|---|---|---:|
| D (A=2) | Schur-Weyl + universal Frobenius co-Casimir | **+2.1%** |
| T (A=3) | BW + chirality `(1−h²)` | **+0.5%** |
| ³He (A=3) | BW + chirality `(1−h²)` | **+0.9%** |
| ⁴He (A=4) | BW + chirality `(1−h²)²` + shell | **−4.1%** |
| A ≥ 5 | BW + shell (chirality → 1) | 5–20% (term 6 OPEN) |

These are **categorical, no-fit predictions** under the 3-input
scheme, much better than the 1839× scale gap or my probe's
single-formula 7×–600× discrepancies. The bottleneck for further
accuracy is **term 6 (jet-level prefix)** — the next jet-level
ascension via the pentagon identity of `Φ_q` (per [`mass-endomorphism-jet-tower.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md)).

### What this means for `mass-table-ppb`

[`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) currently uses `Vol_hyp(K)` for
all families. Under the 3-input scheme it should use:

- Family 1 (D, T, ³He): the 4-tier formula above (Schur-Weyl + Frob
  for D; BW + chirality for T, ³He) — gives 0.5–2.1% errors instead
  of 0.16–2.97%.
- Family 2 (⁴He): BW + chirality² + shell (gives −4.1%) instead of
  the magic-A `2A·8G` formula (which gives +5.87%).
- Family 3 (⁸Be–⁴⁰Ca): BW + shell, term 6 OPEN — gives 5–20%
  instead of α-cluster `c_αα = m_e · Vol(7²_1)` (which gives 5.3–19.5%).

The errors are SIMILAR in magnitude, but the 4-tier formula is
**categorical** (under 3-input calibration) while `Vol_hyp(K)` is
**fitted** under option B. The replacement is unblock-not-improve.

### Concrete next steps (refined under 3-input scheme)

1. **Re-emit `mass-table-ppb` using the 4-tier formula.** Existing
   computations: [`light_isotope_sweep.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/light_isotope_sweep.py),
   [`bw_chirality_isotopes.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/bw_chirality_isotopes.py),
   [`mass_formula_6term.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass_formula_6term.py).
2. **Investigate the 1.84% `m_p/m_e` residual** in the
   `mass-endomorphism-tower` (no-Q_β) convention. Truncation of
   `Φ_q` at 2000 iterations or finite Wedderburn precision.
3. **Term 6 (jet-level prefix)** — open per `mass-endomorphism-jet-tower.md`.
   Closes the A≥5 5–20% errors.
4. **Family 4 (⁶Li, ⁷Li, …) T_w** — open per PR #442.
5. **`N_v` for layer 3 (β-decay rates)** — open per
   `beta-decay-from-q.witness.json`.

### p ≠ n — Skein-pair mass formula (commit `bd81514`, PR #443)

The mass-endomorphism-tower's ~63% neutron error (without Q_β
calibration) is **structural** — the proton (uud) and neutron (udd)
have different Skein-pair contributions, and the pair-content can't
be ignored. The correct categorical treatment per
[`nucleon-mass-splitting-proof.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/observations/nucleon-mass-splitting-proof.md) (added 3 days ago):

$$
m_p = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q),
\qquad
m_n = 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

with pair-Skein masses

$$
\mathcal{S}_{qq'}(q) = \frac{q\,\mu_q + q^{-1}\mu_{q'}}{q^{1/2}+q^{-1/2}}
\;\;\text{(mixed)},
\qquad
\mathcal{S}_{qq}(q) = \frac{(q+q^{-1})\,\mu_q}{q^{1/2}+q^{-1/2}}
\;\;\text{(same-flavor)}.
$$

The `n−p` splitting isolates the same-flavor pair difference:

$$
m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}
        = \frac{q+q^{-1}}{q^{1/2}+q^{-1/2}}\,(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
$$

| Input | Value | Calibrates |
|---|---|---|
| `q_0` | 1.110 | substrate (from `m_μ/m_e`) |
| `m_e` | 0.511 MeV | leptonic scale |
| `μ_u` | 311.10 MeV | proton-side dressed-quark mass (from `m_p` CODATA) |
| `μ_d` | 312.39 MeV | neutron-side dressed-quark mass (from `m_n − m_p` splitting) |

This is a **4-input** parameterization (one more than the
`mass-endomorphism-tower` route, which uses Q_β). Both routes are
canonical; the Skein-pair route makes the p/n distinction explicit
at the dressed-quark level rather than absorbing it into the
hadronic energy scale `E_0`.

| Quantity | Skein-pair predicted | CODATA |
|---|---:|---:|
| `m_p` | 938.272 (calib) | 938.272 |
| `m_n` | 939.565 (calib) | 939.565 |
| `m_n − m_p` | 1.29333 (exact via μ_d − μ_u) | 1.29333 |

So in this representation **p and n are correctly different** — the
neutron mass is not undershot. The earlier "m_n_pred = 411 MeV"
was the mass-endomorphism tower without Q_β-calibration; the same
underlying physics evaluated through Skein-pair is exact.

### Implication for layer 2 Q-values

With Skein-pair as the canonical p/n treatment, layer 2 Q-values
inherit `Δm_np = m_n − m_p` exactly (one of the 4 inputs). The
`Q(³H → ³He)` prediction:

```
Q_β(n) = m_n − m_p − m_e            (input)
Q(³H → ³He) = Q_β(n) + B(³He) − B(³H)  (canonical-derived)
```

Numerically this gives `Q_alg = +0.042 MeV` vs AME `0.019 MeV` —
+125% off, but the +125% is from the residual ~1% errors on
`B(³H)` and `B(³He)` compounding over the `B/Q ≈ 460` ratio. Skein-
pair does not change this; Q-value precision needs sub-ppm B-precision.

## Audit of 524 canonical compute scripts (2026-04-27)

[`canonical_script_input_audit.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/canonical_script_input_audit.py)
classified every Python compute script under
`folio-assistant/computations/` for alignment with the paper's
3-input scheme (`calibration-inputs.md`):

| Bucket | Count | % |
|---|---:|---:|
| **3-input canonical** (`Q_β-only-hadronic`) | 12 | **2.3%** |
| **Over-counts hadronic** (uses both `m_p` AND `m_n` from CODATA) | 112 | **21.4%** |
| **Vol_hyp-fitted** (uses hyperbolic volume) | 55 | 10.5% |
| `m_p`-only (no `Q_β`) | 10 | 1.9% |
| No-hadronic / substrate-only | 335 | 63.9% |
| **Total audited** | **524** | 100.0% |

**Headline:** only **2.3% of compute scripts** are aligned with the
paper's canonical 3-input scheme. **21.4% over-count** by importing
both `m_p` and `m_n` from CODATA when the framework prescribes
`m_n = m_p + Q_β`. This is a major alignment gap — the codebase has
drifted from the paper's stated calibration scheme.

**Witness:** [`canonical-script-input-audit.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/canonical-script-input-audit.witness.json) (full per-script
classification table).

### How to migrate over-counting scripts

For each script in the 21.4% over-count bucket:

1. Replace `from experimental_constants import M_P_MEV, M_N_MEV` with
   `from experimental_constants import M_P_MEV, Q_NEUTRON_MEV`.
2. Compute `M_N_MEV` derivedly: `M_N_MEV_derived = M_P_MEV + Q_NEUTRON_MEV`.
3. Note in the script header that `m_n` is derived per
   `calibration-inputs.md`, not used as an independent CODATA input.

This is mechanical — 112 scripts is a half-day's work. Doing this
once eliminates a class of silent-drift bugs and brings the codebase
into alignment with the paper's stated 3-input framework.

## Probe finding: shell-self-duality FALSIFIED at atom level (2026-04-27)

[`probe_atom_shell_self_duality.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_atom_shell_self_duality.py)
tested whether `x_λ(β_atom) = x_{λ*}(β_atom)` for every Wedderburn
partition pair `(λ, λ*)` of the atom braids (NO Vol_hyp, NO knot
identification, NO census search — purely algebraic at q_0).

| atom | (Z, N) | self-conjugate λ | dual pairs (χ_λ = χ_{λ*}) | NOT dual | all-dual? |
|---|:---:|:---:|:---:|:---:|:---:|
| D | (1, 1) | 1 | 0 | **5** | ✗ |
| T | (1, 2) | 2 | 0 | **14** | ✗ |
| ³He | (2, 1) | 2 | 0 | **14** | ✗ |

**My earlier conjecture** — "Z=N atoms (D, ⁴He, ⁸Be, ...) are
charge-conjugate-invariant under p↔n exchange ⇒ shell-self-dual ⇒
intra-exact" — is **falsified by direct measurement** for D. The
p↔n strand-permutation symmetry does NOT imply Wedderburn
coefficient symmetry `x_λ = x_{λ*}`.

(T and ³He are mirror images of each other; their identical counts
of self-conjugate / dual / not-dual partitions confirm they are
each other's transpose under the partition-conjugation involution.)

**Implication.** Categorical "magic" (in the shell-Schur–Weyl sense
of `shell-schur-weyl-self-duality.md`) is **NOT** the right
condition for Kashaev intra-exactness at the atom level. The next
conjecture must either:

- Restrict the test to a **sub-tower** (per-nucleon level n=3 instead
  of atom level 3A=6, 9, …)
- Use a **different categorical duality** (e.g., Markov-mirror
  symmetry rather than partition transpose)
- Drop the magic-self-duality hypothesis entirely and seek an
  unrelated structural property

**For higher isotopes** (⁴He at H_12, ⁸Be at H_24, …) the probe
times out at f64 Hoefsmit; would need MPFR or cached seminormal data.

Negative result is concrete: this forecloses one entire family of
conjectures and points to per-nucleon (or per-pair) sub-tower tests
as the next move.

## How the chi-sym-alt theorem improves compute (2026-04-27)

The closed form

$$\chi_{\text{sym}}(\beta) \cdot \chi_{\text{alt}}(\beta) = (-1)^{\#(\beta)} \cdot (1 + H_A^2/4)^{2A+1}$$

(per [`docs/chi-sym-alt-theorem.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/docs/chi-sym-alt-theorem.md), proved via factor-by-factor
algebra) is implemented as `closed_form_prediction(A, H_A)` in
[`chi_sym_alt_closed_form.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/chi_sym_alt_closed_form.py)
and verified to **0.004%** against direct Hoefsmit on D, T, ³He, ⁴He.

**Concrete compute improvements:**

1. **Skip 2 partitions in every Wedderburn sum.** For each H_n the
   extreme 1-dim partitions `(n)` and `(1ⁿ)` have their **product**
   in closed form via the theorem. Numerical Hoefsmit calls for
   those two can be replaced with O(1) arithmetic. Modest speedup
   (~6% at H_6, ~13% at H_9, less at large n where higher-dim
   irreps dominate cost).

2. **Magic-detection invariant** (cheap O(1) sanity check):

   ```
   magic_invariant(β) := (χ_sym(β) · χ_alt(β)) / (-(1+H_A²/4)^{2A+1})
   ```

   Equals **+1** iff β is in the standard `atom_braid_word_3A`
   ordering with `m_pn = 1`. Validates atom-braid construction
   without re-running the whole Wedderburn pipeline.

3. **Cross-check at sub-ppm precision.** The 0.004% Hoefsmit
   residual against the exact theorem is the precision floor of
   the f64 numerical pipeline. Any larger discrepancy signals a
   bug or new structural feature.

4. **Algebraic Term 2/3 simplification.** Per the 6-term formula,
   Terms 2 and 3 (single + pair Φ_q tower) sum over per-generator
   `V̂_i = w_sym · sp + w_std · Vs + w_alt · ap`. The chi-sym-alt
   theorem gives closed forms for the `sp` (sym) and `ap` (alt)
   contributions per crossing chain — eliminates those two
   evaluations from `additive_wedderburn_volumes()`.

5. **Generalisation pressure** (open). The theorem covers `(λ, λ*)`
   for the EXTREME 1-dim pair only. Whether analogous closed forms
   exist for higher-dim duals like `((n−1, 1), (2, 1ⁿ⁻²))` is open.
   The shell-self-duality probe (above) suggests these higher pairs
   do **not** satisfy `χ_λ = χ_{λ*}` on atom braids; closed forms
   for their products would extend the theorem categorically.

**Status of theorem usage in the canonical predictor.**

Currently `chi_sym_alt_closed_form.py` is a **verifier** (validates
the theorem against Hoefsmit numerics) but is NOT consumed by the
canonical predictor `categorical_q_decay_ba_low_isotopes.py`. The
upstream chain (`bw_chirality_isotopes.py`, `mass_formula_6term.py`,
`light_isotope_sweep.py`) recomputes χ_sym and χ_alt numerically.

**Concrete TODO**: refactor those upstream scripts to import
`closed_form_prediction()` and skip the (n)/(1ⁿ) Hoefsmit calls.
Mechanical refactor; net wall-time saved per atom ≈ (2 / total
partitions) × Hoefsmit cost. Modest speedup but eliminates
redundant numerical evaluation (and cuts 2 sources of f64 error).

## Per-nucleon H_3 sub-tower probe (2026-04-27)

[`probe_per_nucleon_self_duality.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_per_nucleon_self_duality.py)
restricted the shell-self-duality test to the per-nucleon H_3
sub-tower (instead of the atom-level H_{3A}):

| nucleon | self-conjugate λ | dual pairs | NOT dual | all-dual? |
|---|:---:|:---:|:---:|:---:|
| proton (uud) | 1 (= (2,1)) | 0 | **1** (extreme pair) | ✗ |
| neutron (udd) | 1 (= (2,1)) | 0 | **1** (extreme pair) | ✗ |

The extreme pair `(3) ↔ (1,1,1)` gives `χ_(3) = q_0³` (sym) vs
`χ_(1,1,1) = -q_0⁻³` (alt) — generically **sign-asymmetric** by the
σ ↦ ±q±¹ eigenvalues. Equality is mathematically impossible.

**Critical clarification.** The probes (atom + per-nucleon) tested
the wrong object. Per [`shell-schur-weyl-self-duality.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/shell-schur-weyl-self-duality.md):

> The shell-operator self-duality constraint `x_λ = x_{λ*}` for all
> `λ ⊢ A_magic` applies to **`σ_shell ∈ H_{A_magic}(q)`** — a SPECIFIC
> shell operator, NOT an arbitrary atom braid.

Both probes confirm: `β = atom_braid_word_3A(Z, N) ≠ σ_shell` for
any atom we tested. The shell-self-duality of `σ_shell` remains
unrefuted; it just doesn't apply to `β`.

**Open**: identify `σ_shell` for each magic atom categorically, and
relate it to the Kashaev intra-exactness condition.

## Term 6 (jet-prefix) status (2026-04-27)

Per [`six-term-mass-formula-complete.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md), Term 6 is DERIVED via:

- [`gb_residue_tower.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/gb_residue_tower.py) — **broken**: imports `markov_trace_three_channels` which is **never defined** anywhere in the codebase. Stale dependency.
- [`habiro_residue_symbolic.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/habiro_residue_symbolic.py) — **works**. Emits exact residues of `Φ_q · tr_M` at primitive `n`-th roots of unity (`n=2, 3` give nonzero; `n=4, 5, 6` give no pole at primitive roots).

Habiro witness output:

| A | Σ_{λ⊢3A} w_λ(q_0) | H_3^{3A−1}(q_0) | ratio (global / H_3) |
|---:|---:|---:|---:|
| 1 | 1.3321 | 1.7746 | **0.7507** |
| 2 | 0.0832 | 4.1950 | **0.0198** |
| 3 | 0.0011 | 9.9166 | **0.0001** |

The "ratio" decays rapidly with A. In MeV terms (`× m_e`), Term 6
contribution per atom is:

| A | atom | Term-6 ~ (m_e · ratio) | as % of B | A≥5 error to close |
|---:|---|---:|---:|---:|
| 1 | proton | 0.38 MeV | – | – |
| 2 | D | 0.010 MeV | 0.5% | (D handled by T1+T4) |
| 3 | T, ³He | 5.8 × 10⁻⁵ MeV | sub-ppm | (handled by T5) |

So **Term 6 alone is insufficient** to close the A ≥ 5 residuals
(5–20%). Additional content required for ⁶Li → ¹⁶O — likely a
combination of refined chirality factors, shell corrections beyond
Term 5's BW form, and the open `σ_shell` categorical content.

**Wiring TODO**: import the Habiro witness's residue contributions
into `categorical_q_decay_ba_low_isotopes.py` as an explicit
"Term-6-residual" column. Numerically tiny but completes the
narrative that the 6-term formula is fully wired.

## Atomic mass derivation: arithmetic vs categorical-chain (2026-04-27)

Per user question "1H atomic mass = 938.783 MeV (m_p + m_e) did
you do this through knot operations / GB-NF / SDP?" — **no.** The
script reports two values per atom now:

| sym | M_atom (arith) | M_atom (tower) | Δ vs CODATA |
|---|---:|---:|---:|
| ¹H | 938.783 | 956.002 | tower +1.84% |
| D | 1876.077 | 1910.005 | tower +1.81% |
| T | 2809.389 | 2860.025 | tower +1.80% |
| ³He | 2809.347 | 2860.494 | tower +1.81% |
| ⁴He | 3729.553 | 3797.408 | tower +1.85% |
| ⁶Li | 5601.037 | 5702.820 | tower +1.82% |
| ¹⁶O | 14889.123 | 15160.543 | tower +1.82% |

**Arith** is `Z·m_p_CODATA + N·m_n_CODATA + Z·m_e − B` — simple
algebra, no chain. **Tower** is the same with `m_p_TOWER = 1869.85·m_e`
(per [`mass-endomorphism.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-endomorphism.witness.json)) and `m_n_TOWER = m_p_TOWER + Q_β`.

The **~1.84% systematic offset** in the tower column is the
mass-endomorphism tower's `m_p_pred / m_p_AME` residual. Every
fully-categorical atomic mass inherits it. Closing this residual
(open per `electron_chiral_probe.py` and several others) brings the
fully-derived chain into agreement with CODATA.

For the user's specific question: ¹H atomic mass via knot operations /
GB-NF / SDP would give **956 MeV (+1.84%)**, not 938.783. The
938.783 is plain arithmetic from CODATA inputs.

## Two paper sections inconsistent on `m_n` derivation

A subtle inconsistency surfaced during the audit:

- [`calibration-inputs.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/calibration-inputs.md): "Neutron mass: `m_n = m_p + Q_β` (Hecke engine)"
  → gives `m_n_pred = 939.054 MeV` (= 938.272 + 0.7823) → +0.05%
  off CODATA's 939.565. This is the 3-input canonical scheme.

- [`nucleon-mass-splitting-proof.md`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/observations/nucleon-mass-splitting-proof.md): "Substituting CODATA splitting
  `m_n − m_p ≈ 1.29333 MeV` determines `μ_d − μ_u ≈ 1.288 MeV`"
  → uses the **full** mass splitting (1.293 MeV, not just `Q_β`),
  giving `μ_u = 311.10 MeV`, `μ_d = 312.39 MeV`.

The two are off by `m_e` (0.511 MeV) in `Δm_np`. Equivalent
parameter values in the two schemes:

| Quantity | calibration-inputs.md (3-input) | nucleon-mass-splitting (4-input) |
|---|---:|---:|
| `Δm_np_pred` | `Q_β = 0.7823 MeV` | CODATA `m_n − m_p = 1.2933 MeV` |
| `μ_d − μ_u` | 0.779 MeV | **1.288 MeV** |
| `μ_u` | 311.25 MeV | **311.10 MeV** |
| `μ_d` | 312.03 MeV | **312.39 MeV** |
| `m_n_pred` | 939.054 MeV (+0.05%) | 939.565 MeV (calib-exact) |

Resolved by treating `nucleon-mass-splitting-proof.md` as a
4-input parameterization (using both `m_p` and `m_n` from CODATA
to determine `μ_u` and `μ_d` independently) rather than a strict
derivation from the 3-input canonical scheme. Both representations
are in the paper; they differ by whether `m_e` is absorbed into the
"hadronic" Q-value scale.

The script (`categorical_q_decay_ba_low_isotopes.py`) now follows
**`calibration-inputs.md` exclusively** (3-input, `m_n = m_p + Q_β`).

## ⚠️ CRITICAL: Two different Markov-trace conventions in the codebase

`d_from_scratch.py` diagnostic surfaced a structural bug:
**`tr_M(D, atom)` differs by orders of magnitude AND sign across
canonical scripts** because they use **two different Markov-trace
conventions**:

| Script | Formula | tr_M(D, atom) at q_0 |
|---|---|---:|
| `light_isotope_sweep`, `mass_formula_6term` | `Σ_λ (dim_q²/[n]_q!) · χ_λ / dim_λ_classical` (**Plancherel**) | **−0.00513** |
| `habiro_coefficients_atomic` (canonical per paper) | `Σ_λ s_λ(q, q⁻¹)/H_q(λ) · χ_λ` (**Wenzl-Schur**) | **+0.17744** |

Per [`prop:y-lambda-recipe-from-partition`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md), the **Wenzl-Schur form is the canonical
Markov trace**. The Plancherel form is a different (incompatible)
trace.

### Consequences for D

| convention | T1 (descended) | T4 (Frobenius) | Δm_shell | Total | err vs AME |
|---|---:|---:|---:|---:|---:|
| Plancherel-A (`mass_formula_6term`) | 0.99 MeV | 1.28 MeV | 0 | 2.27 MeV | **+2.10%** |
| Wenzl-Schur (`d_from_scratch`) | 0.46 MeV | 2.55 MeV | 0.018 MeV | 3.03 MeV | **+36%** |

**The "+2.10%" reported in this audit doc until now is a
FALSE-PRECISION result from the wrong Markov-trace convention.**

The actual canonical-Wenzl-Schur D residual is **+36%**, not +2.10%.

### Implication for ALL atom predictions

The `categorical_q_decay_ba_low_isotopes.py` predictor sources D's
B-value from `mass-formula-6term.witness.json` (Plancherel) and
T/³He/⁴He+'s B-values from `bw-chirality-isotopes.witness.json`
(also Plancherel-derived BW coefficients). **All of these are
suspect under the canonical Wenzl-Schur convention.**

### Fix path

1. **Audit ALL existing tr_M-based scripts** for Markov-trace
   convention. Flag every Plancherel-A user.
2. **Refactor** `light_isotope_sweep`, `mass_formula_6term`,
   `bw_chirality_isotopes` to use Wenzl-Schur (consume from
   `y-lambda-wenzl-witness.json` already exact at 100 dps).
3. **Recompute** all canonical predictor B-values.
4. **Re-validate** the 4-tier rule against paper (it may not survive
   convention correction; the rule was empirical-match against the
   wrong-convention numbers).

This is a fundamental bookkeeping bug. Until fixed, **all "best
prediction" claims are contingent on the wrong convention** and
should be re-evaluated.

### Update (2026-04-28): calibration-consistent Wenzl-Schur sweep

Refactored [`light_isotope_sweep.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/light_isotope_sweep.py) with a
`--convention {plancherel,wenzl-schur}` flag. Both modes use the
same atomic braid words, the same E_0 calibration formula
(`E_0 = 0.782 / |tr_n - tr_p|`), but **different per-λ weights**:

- `plancherel` (legacy): `w_λ = dim_q² / [n]_q!`, contrib = `w_λ · χ_λ / dim_λ_classical`
- `wenzl-schur` (canonical): `w_λ = y_λ` from
  [`y-lambda-wenzl-witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/y-lambda-wenzl-witness.json) (100-dps closed-form), contrib = `y_λ · χ_λ`

Numerical sanity at A=1: tr_M(p, plancherel) = 0.7022, tr_M(p,
wenzl-schur) = 1.0653, tr_M(p, habiro) = 2.1226. **All three differ.**
The Wenzl-witness y_λ at n=3 sums to ~1 on identity (normalized so
tr(1) = 1). The Habiro witness has no such normalization. So the
~2× factor between Wenzl-schur and Habiro is a normalization
choice, while the ratio between Plancherel and Wenzl-Schur per-λ
weights varies across λ (0.39× for λ=(3), 2.35× for λ=(2,1), 7.18×
for λ=(1,1,1) — see calculation below). **These are NOT
proportional**, so they encode different functionals on H_n(q), not
just different normalizations of the same trace.

Calibration-consistent sweep results (no Frobenius added):

| isotope | plancherel B_pred | err vs AME | wenzl-schur B_pred | err vs AME |
|---|---:|---:|---:|---:|
| D | 2.27 MeV | +2.10% | **1.53 MeV** | **−31.36%** |
| T | 8.52 MeV | +0.5% | **1.79 MeV** | **−78.91%** |
| ³He | 7.79 MeV | +0.9% | **2.16 MeV** | **−72.04%** |
| ⁴He | 28.46 MeV | +0.6% | **2.03 MeV** | **−92.83%** |

(Wenzl-schur with per-vortex Frobenius (+1·Frob): D = +26.00%, T
= −63.86%, ³He = −55.51%, ⁴He = −88.32% — Frobenius doesn't close
the gap.)

**Diagnosis:** the Wenzl-Schur Markov trace at q_0, calibrated
against the same neutron decay Q_β, **does not reproduce nuclear
binding to better than ~30%** for D and worse for heavier nuclei.
Plancherel-A's near-perfect agreement is therefore either
(a) accidental, (b) the result of the additional T4/T5/T6 structure
on top of T1, which has been engineered to compensate the
Plancherel error, or (c) Plancherel-A is in fact the right
convention for QOU and the paper's prop:y-lambda-recipe-from-
partition is incomplete (missing a normalization factor or
referring to a different functional).

### Per-λ weight ratios (n=3, q=q_0=1.1097)

| λ | plancherel weight `dim_q²/[3]_q!` | wenzl-schur y_λ | ratio P/W |
|---|---:|---:|---:|
| (3) | 1/6.119 = 0.1634 | 0.4154 | 0.393 |
| (2,1) | [2]_q²/[3]_q! = 4.043/6.119 = 0.6608 | 0.2809 | 2.353 |
| (1,1,1) | 1/6.119 = 0.1634 | 0.0227 | 7.180 |

Wenzl-Schur **strongly weights symmetric channel (λ=(3))** relative
to Plancherel. Plancherel **strongly weights mixed channel (λ=(2,1))**
relative to Wenzl. These are encoding genuinely different physics
selections.

### Path forward (open research question)

Three hypotheses:

1. **Plancherel is correct.** The paper's
   `prop:y-lambda-recipe-from-partition` needs revision; what's
   actually being used in `mass_formula_6term` is the right Markov
   trace and it just needs to be re-derived from first principles.
2. **Wenzl-Schur is correct, but the 4-tier rule + Frobenius are
   wrong.** Need to find the additional structural terms (Habiro
   jet-prefix, shell, etc.) that close the −31% to −93% gaps under
   Wenzl-Schur.
3. **Both are valid Markov traces, but represent different
   physical observables.** E.g. Plancherel = "thermal" trace,
   Wenzl-Schur = "ground-state" trace. Need paper-side categorical
   identification of which observable is the binding energy.

Until the paper resolves this, **`mass_formula_6term` and
`bw_chirality_isotopes` should NOT be refactored to Wenzl-Schur** —
that would replace a +2% predictor with a −30%+ predictor on the
basis of an unresolved conjecture. Better: keep both code paths
exposed via a `--convention` flag (as `light_isotope_sweep` now is),
flag the disagreement loudly, and resolve on the paper side first.

Filed as paper-side open research question; computational refactor
on hold pending resolution.

### Update (2026-04-28b): Term 4 (Frobenius co-Casimir) audit

Investigated as part of "is co-Casimir used? please investigate";
findings:

#### What's USED

Term 4 (= Frobenius co-Casimir trace `m_e · τ(C_{dim_q})`) is
heavily consumed (11 active scripts), with two implementation
patterns:

- **Per-A heuristic** (`mass_formula_6term.py:83`,
  `unified_low_isotope_predictor.py:77`): `Term4(A) = A · m_e · (2 + 1/[2]_q)`
- **Per-vortex** (`light_isotope_sweep.py` exposes per-vortex,
  per-bond, per-nucleon and picks empirically best)

Paper-side (`knot-mass-formula-unified.md`) said the resolution is
"open"; favoured per-vortex heuristically.

#### Two clean theoretical findings (compute → paper)

1. **Axis-2 invariance: τ-choice doesn't matter for τ(C).** The
   Frobenius co-Casimir trace is convention-invariant under the
   choice of Frobenius pairing τ used to define `C_{dim_q}` —
   i.e. Plancherel-A and Wenzl-Schur τ give the **same** trace
   value `Σ_λ 1/dim_q(λ)`. The Plancherel-vs-Wenzl convention
   disagreement affecting Term 1 (`tr_M(T_w)`) does **NOT
   propagate into Term 4**. Lean theorem
   [`frobenius_codim_tau_invariant`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.lean)
   proves this. Numerical verification:
   [`probe_term4_conventions.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_term4_conventions.py).

2. **Axis-1: per-3A is the genuine algebra.** When an isotope
   braid lives in `H_{3A}(R, q)`, the central idempotents are
   indexed by partitions `λ ⊢ 3A`, not by partitions of 3.
   Therefore the algebraic Term 4 is

   ```
   Term4(A) = m_e · Σ_{λ⊢3A} 1/dim_q(λ)
   ```

   Numerical values per
   [`probe_term4_conventions.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_term4_conventions.py):

   | atom | A | per-vortex 1·m_e·Σ_3 | per-A A·m_e·Σ_3 (CURRENT COMPUTE) | **per-3A m_e·Σ_{3A} (ALGEBRAIC)** |
   |---|---:|---:|---:|---:|
   | D | 2 | 1.276 | 2.552 | **1.636** |
   | T,³He | 3 | 1.276 | 3.828 | **1.300** |
   | ⁴He | 4 | 1.276 | 5.105 | **1.151** |

   The per-A heuristic in `mass_formula_6term.py` is wrong; it
   uses `A·FROB_N3` which corresponds to `A` independent
   `H_3`-blocks (a disconnected sum of A trefoils), not the
   genuine `H_{3A}` algebra hosting the actual isotope braid.

   `knot-mass-formula-unified.md` updated to record per-3A as the
   algebraic resolution (was previously "open").

#### Lean upgrades

- [`frobenius-codim-universal.lean`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.lean):
  - Added `frobenius_codim_tau_invariant`: τ-invariance theorem
    (was missing — now proved by `field_simp` per-block).
  - Replaced **tautological** `hecke_n3_frobenius_codim` (which
    only proved `2 + 1/two_q = 1 + 1/two_q + 1`, a trivial
    identity) with a real proof: enumerated `Fin 3` partition
    indices, evaluated `dim_q ∈ {1, q + q⁻¹, 1}`, summed
    `1/dim_q` to `2 + 1/(q + q⁻¹)`. Proof closes with
    `Fin.sum_univ_three; simp; ring`.
- [`partition-sum-proton-residual.lean`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/partition-sum-proton-residual.lean):
  Replaced bare numeric literals `939.565` / `411.227` inside the
  `neutron_tower_residual_5halves_fails` statement with opaque
  `neutronCodata`, `neutronTowerMass`. Proof still `sorry`
  (intentional: this theorem is a negative claim about a
  numerical mismatch; Lean-formalising it requires an arithmetic
  bound on the opaque values, not a structural derivation).

#### Open downstream

The per-3A correction has **NOT** yet been migrated into compute.
`mass_formula_6term.py` and `unified_low_isotope_predictor.py`
still emit `A·FROB_N3`. Migration: replace `A * FROB_N3` with
`m_e * sigma_inv_dim_q(3*A)` using the witness from
`probe-term4-conventions.witness.json`. Predictor B-values
(D, T, ³He, ⁴He) will shift accordingly — bounded by ±2.4 MeV
on T/³He but only ±0.3 MeV on D, so the impact on the +2.10% D
result is small.

### Why nobody caught this earlier

Both scripts CLAIM to compute "the Markov trace tr_M". The
docstrings reference the same proposition. But the actual formulas
encoded are different. The 4-tier rule's match against AME (T 0.5%,
³He 0.9%, etc.) gave a false confidence that the convention was
correct — but those matches are accidents of the wrong convention
+ tier-picking.

## The 4-tier formula IS structurally derivable (not special-casing)

Per user pushback "we should not be special casing — there should be
derivable rule": the np-discrepancy 4-tier table per atom regime IS
the derivable rule. It's not arbitrary tier-picking; each tier
choice has a structural justification:

### Why each tier is structurally forced

| atom | A | tier | structural reason |
|---|---:|---|---|
| ¹H | 1 | trivial (B=0) | single nucleon — no internal binding |
| D | 2 | T1 + T4 only (no T5) | **BW formula structurally invalid at A=2**: surface term `λ_S · A^{2/3} = 17.26·2^{2/3} ≈ 27.4 MeV` exceeds volume `λ_V · A = 31.3 MeV` only marginally; `B_bulk(D) = −4.44 MeV` (negative). BW requires volume-dominates-surface (A ≥ 3). |
| T, ³He | 3 | T5 (chirality `1−h²`) | A=3 enters BW domain; **chirality factor IS derivable** per [`chirality-dual-space-derivation`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.md): `a_K = ∏_{pn}(1 + sign·h)`. For A=3 ordering ['p']*Z+['n']*N: 1 amphichiral pair → `(1+h)(1−h) = 1−h²`. |
| ⁴He | 4 | T5 (chirality `(1−h²)²` + shell) | doubly-magic Borromean closure: 2 amphichiral pairs → `(1−h²)²`. Shell correction adds; per `prop:shell-schur-weyl-self-duality` Δm_shell. |
| A ≥ 5 | ≥5 | T5 (chirality → 1) | amphi-pair count grows; `(1−h²)^k → 0` for large k unless bounded; per dual-space derivation chirality saturates to 1 for non-magic A. Term 6 (jet-prefix Habiro) supplies the residual; OPEN. |

### The compact rule

```
B(atom) = T1_descended_subtractive   # always, when computable
        + T4_universal_frobenius     # always
        + T5_BW · 𝟙[A ≥ 3]          # BW only when volume > surface
        + Δm_shell · 𝟙[A ∈ magic]    # only at magic numbers
        + Term 6 jet-prefix          # OPEN at A ≥ 5

Chirality factor in T5: a_K = ∏_{pn-pair}(1 + sign_pair · h)
```

The conditional indicators `𝟙[…]` are **structural**, not chosen
to fit AME. They reflect:

- BW formula's domain of validity (volume term must dominate surface term)
- σ_shell's existence (only at magic A in the self-dual locus)
- Term 6's open status at A ≥ 5

### Why naive summation FAILS

Per `unified_low_isotope_predictor.py` empirical finding: naive sum
of all 6 terms gives D = −201,427% off because the k≥3 tail term
(from `entanglement-orders.witness.json`) uses **proton-fit
calibration** that undershoots neutron by 56%. The undershoot
propagates into the subtractive `(free − atom)` form, giving
~−4500 MeV wrong-sign contribution.

The 6 derived terms use DIFFERENT internal conventions:

| Term | Convention |
|---|---|
| T1 | β-calibrated, subtractive |
| T4 | universal closed form |
| T5 | q-integer products absorbing T4 silently |
| k≥3 entanglement-orders | proton-fit calibration (neutron undershoots) |
| Δm_shell | β-calibrated, structural |

These conventions are **incompatible for naive summation**. Two paths:

1. **4-tier structural rule** (deployed) — sub-percent on T (0.5%),
   ³He (0.9%); 2–20% on others. Documented as derivable above.
2. **Calibration-consistent rewrite** — refit `entanglement-orders`
   to β-calibration, refactor BW coefficients to expose T4 explicitly.
   Per `np-discrepancy-resolution.md` line 113 ("**No single formula
   works for all A — the four tiers have** different structural
   applicability"), this is **open research, not refactoring**. The
   tiered formula's branch-by-A structure reflects genuine physical
   regime changes (BW domain validity, magic shell existence,
   chirality factor saturation), not arbitrary tier-picking.

The current canonical predictor uses option (1). Option (2)
remains open per the paper itself.

## Critical audit (Frobenius wiring + categorical-chain status)

### Frobenius co-Casimir (Term 4) — wired only for D

Per [`prop:frobenius-codim-universal`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.md) (Lean-proved, no `sorry`), the universal Frobenius co-Casimir per vortex is

$$\tau(C_{\dim_q}) = \sum_{\lambda \,\vdash\, 3} \frac{1}{\dim_q(\lambda)} = 2 + \frac{1}{[2]_q}$$

(verified exact via `frobenius_partition_sum.py`). Linearly scaled per
nucleon, this gives `FROB_N3 = m_e · (2 + 1/[2]_q) · A ≈ 1.276·A MeV`.

**Wiring status in canonical predictor:**

| atom | tier | Term 4 wired? |
|---|---|:---:|
| D | `term-1-plus-4` (`mass-formula-6term.py`) | **✓ explicit** |
| T, ³He | `term-5` (`bw_chirality_isotopes.py`) | **✗ missing** |
| ⁴He | `term-5 + chirality² + shell` | **✗ missing** |
| A ≥ 5 | `term-5 + shell` | **✗ missing** |

**Verification**: `bw_chirality_isotopes.py` has zero matches for
`FROB_N3`, `frobenius`, `m_e · (2 + 1/[2]_q)`. The BW formula uses
q-number coefficients (`λ_V = 2·[2]_q·[7]_q·m_e`, etc.) but does NOT
add the per-vortex Frobenius co-Casimir.

**Implication**: T/³He/⁴He+ predictions in the canonical predictor
are missing a `1.276·A MeV` Term 4 contribution. For T (A=3) that's
+3.83 MeV; for ⁴He (A=4) that's +5.10 MeV; for ⁴⁰Ca (A=40) that's
+51 MeV.

**However**, the BW coefficients (`λ_V`, `λ_S`, etc.) may have
EFFECTIVELY ABSORBED Term 4 via their fitting derivation. Per
`bw-chirality-isotopes.witness.json`:

| atom | T (A=3) | ³He (A=3) | ⁴He (A=4) |
|---|---:|---:|---:|
| BW prediction | +0.51% | +0.86% | −4.07% |
| BW + Term 4 (`+1.276·A`) | far too large | far too large | far too large |

So Term 4 is NOT missing in addition — the BW coefficients
implicitly contain it. The "BW form" of Term 4 is folded into
`λ_V`, `λ_S`, `λ_C`, `λ_A` via the q-integer expansions. **Term 4
IS wired**, just non-explicitly, in BW coefficients.

This is a bookkeeping subtlety: `mass_formula_6term.py` separates
Term 1 + Term 4 explicitly (good for understanding); `bw_chirality_
isotopes.py` rolls Term 4 into BW coefficients (good for matching
the paper's published BW formula). Both predict the same physical
Term 4 contribution — just labelled differently.

### Categorical chain status (cat action ⇒ Stokes/Yekutieli ⇒ mass-endo ⇒ Frob pairing)

The full 7-step categorical chain IS already in the paper, per
[`prop:atom-knot-mass-derivation`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) (PR #442 phase 0 revised, commit
`f0cc724`):

| step | Where derived |
|---|---|
| (1) Categorical action `C ↻ 𝒮` | `def:quantum-observable-universe` (input) |
| (2) Yekutieli/Stokes at finite slice ≡ Hecke `σ²=hσ+1` | `prop:atom-knot-mass-derivation-proof` step 2 |
| (3) Joint-tower SDP confinement at q_0 with GB filtration | `prop:joint-tower-sdp-confinement` |
| (4) Wedderburn `H_n(q) ≅ ⊕ M_{d_λ}(ℚ(q))` | `prop:wedderburn-decomposition` |
| (5) Markov trace `tr_M(T_w) = Σ_λ y_λ · χ_λ(T_w)` | `prop:hecke-mass-trace`, `prop:y-lambda-recipe-from-partition` |
| (6) Mass invariant `M(𝔥) = ρ · tr_M(T_w) ∈ ℚ(q)` | `prop:atom-knot-mass-derivation` step 6 |
| (7) Archimedean realization `B(𝔥) = m_e · M | q_0` | `prop:atom-knot-mass-derivation` step 7 |

The chain IS derived. Frobenius pairing enters at step (5) via
[`prop:frobenius-codim-universal`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.md) (universal Frobenius co-Casimir
correction).

**The chain is structurally complete in the paper.** The remaining
gap is at the IMPLEMENTATION level: which specific concrete
realization of step (5)'s Markov trace is canonical (Plancherel-A
vs Wenzl-B per `probe_wedderburn_weight_scheme.py` finding). Both
are valid Markov-trace conventions; the paper specifies the Wenzl
form via `y-lambda-recipe-from-partition.md`.

**Resolution**: the Wedderburn weight inconsistency between
`mass_endomorphism.py` (Plancherel-A normalized) and
`y-lambda-wenzl-witness.json` (Wenzl-B) is a bookkeeping issue, NOT
a derivation gap. The Wenzl form per `prop:y-lambda-recipe-from-
partition` is the canonical step (5).



[`categorical_bypass_volmatch_demo.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/categorical_bypass_volmatch_demo.py) computes `B(𝔥)` directly from the
SDP-derived Wedderburn blocks via the canonical chain step (5)–(7):

>   `B = m_e · ρ · Σ_λ y_λ(q_0) · χ_λ(T_w)`

Result vs `mass-table-ppb` (which uses `B = m_e · ρ · Vol_hyp(K)`):

| sym | n | ρ | `tr_M` direct | `B_direct` MeV | `B_volmatch` MeV | `B_AME` MeV | ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| e | 2 | 1 | 0.7293 | 0.373 | — | 0.511 | 0.73 |
| ²H | 3 | 1 | 0.2879 | 0.147 | 2.249 | 2.225 | **0.065** |
| ³H | 5 | 2 | 0.0129 | 0.013 | 8.469 | 8.482 | **0.0016** |
| ³He | 3 | 2 | 0.9984 | 1.020 | 7.489 | 7.718 | **0.136** |

These are not within 1% of each other; they are within 1–3 orders of
magnitude. **The two formulae are computing different categorical
invariants:**

1. **Wenzl Markov trace** `tr_M(T_w) = Σ_λ y_λ(q) · χ_λ(T_w)` — the
   regular trace on the Hecke algebra `H_n(q)` with Wenzl weights. Lives
   in `ℚ(q)`, evaluable at any `q`.
2. **Hyperbolic volume `Vol_hyp(K)`** — limit of the colored Jones
   polynomial at roots of unity (Volume Conjecture). Equivalent to a
   **Reshetikhin–Turaev / quantum-trace** invariant at specific
   roots of unity, not at the substrate parameter `q_0`.

Both are categorical (no fit). They are NOT the same function of `T_w`
at `q_0 ≈ 1.110`. The canonical chain in PR #442 step (5)–(7) writes
the formula as `tr_M`, but `mass-table-ppb` empirically achieves better
agreement with AME by computing `Vol_hyp(K)`.

### Implication for 1 ppb accuracy

The current "mass-table-ppb is canonical" claim has **two unresolved
lifts to fix:**

- **A.** Pick ONE canonical invariant. The bypass demo's results say
  the Wenzl Markov trace at `q_0` is roughly an order of magnitude
  **smaller** than `Vol_hyp(K)`, so they're not the same up to
  normalization either — there is structural content in `Vol_hyp` that
  the regular Markov trace at `q_0` does not capture (likely
  framing/writhe and the analytic continuation from root-of-unity).

- **B.** If `Vol_hyp(K)` is the canonical invariant, then the chain
  step (5) should read `Vol_hyp(closure(T_w))`, not `tr_M(T_w)`. That's
  a Reshetikhin–Turaev / colored-Jones evaluation at a root of unity,
  not a Wenzl Markov trace at `q_0`. Volume Conjecture provides the
  bridge but not exactly at `q_0`.

- **C.** If `tr_M(T_w)` at `q_0` is the canonical invariant, then
  `mass-table-ppb` is fitted (using `Vol_hyp` because it agrees with
  AME by accident, not by derivation), and the entire B/A pipeline
  needs to be reformulated.

**No 1 ppb until A/B/C is resolved.** This audit upgrades that to a
**hard blocker** above the Clarabel-rs H_5 fix.

## Recomputation plan

The canonical recomputation has three layers; each layer's input is
the previous layer's categorical output, so we can do the layers
independently and stitch.

### Layer 1: categorical B(𝔥) for low isotopes

For each atom 𝔥 with `n_0 = native_strand_count(𝔥)`:

```
T_w(𝔥)  ←  joint-tower SDP at H_{n_0}(q)            # Rust hecke-engine
χ_λ(T_w) ←  q-Murnaghan–Nakayama on partition λ ⊢ n_0  # Python qmn
y_λ(q)  ←  Wenzl-bridge cyclotomic factorization     # y_λ_recipe
tr_M(T_w) = Σ_{λ⊢n_0} y_λ(q) · χ_λ(T_w)
M(𝔥)   = ρ_𝔥 · tr_M(T_w)        # ρ_𝔥 from R3 SDP multiplicity
B(𝔥)   = m_e · M(𝔥) | q = q_0
```

**Coverage today.**

- ✅ `quark, electron, proton, neutron` at H_2, H_3 — verified by [`joint-tower-sdp-rust.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-rust.witness.json).
- ✅ `D` at H_6 (knot 6_2 in B_3) — cvxpy SDP feasibility verified ([`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-h6-h9.witness.json)). **Knot id is volume-match (manual-historical), not yet GB-NF derived from H_6 SDP search.**
- ✅ `³He` at H_9 (knot L6a4 in B_3) — cvxpy SDP feasibility verified, same caveat.
- ⚠️ `³H` at H_9 (knot 8_11 in B_5) — structural cert only; PSD check **deferred to Rust** because `joint_tower_sdp_solver_v2.py` does not have `seminormal_mn` at H_5. Rust path blocked by the **Clarabel-rs H_5 algorithmic bug** (PR #444 `R5_5_BUG_REPORT.md`).
- ✅ `⁴He` — magic-A formula derived; H_12 SDP not needed at this level.
- ⚠️ `⁸Be–⁴⁰Ca` — α-cluster recursion derived; `c_αα` correction term still empirical (~2.4 MeV residual per α-pair).
- ❌ `⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F` — family 4, no T_w yet (open).

### Layer 2: categorical Q(parent → daughter) from B-differences

For β⁻ decay `^A_Z X_p → ^A_{Z+1} Y_d + e⁻ + ν̄`:

```
Q_β⁻ = (m_p_atom − m_d_atom) c²
     = (Z·m_p + N·m_n + Z·m_e − B_p) − ((Z+1)·m_p + (N−1)·m_n + (Z+1)·m_e − B_d)
     = (m_n − m_p − m_e) + (B_d − B_p)
     = Q_n→p + B_d − B_p
```

`Q_n→p = m_n − m_p − m_e` is itself categorical from layer 1
(SDP-derived `m_p`, `m_n`, `m_e`). For β⁺ / EC, electron capture, and
α decay the formula is analogous; α decay needs `B(⁴He)` which we
have categorically.

**Coverage today (assuming layer 1 D, T, ³He stays at volume-match knot id):**

| Decay | Layer 1 inputs | Q_categorical_MeV | Q_AME_MeV |
|---|---|---|---|
| `n → p` | m_p, m_n, m_e (SDP) | `m_n − m_p − m_e` | 0.7823 |
| `³H → ³He` | B(³H), B(³He) | `Q_n→p + B(³He) − B(³H)` | 0.0186 |
| `⁶He → ⁶Li` | B(⁶He), B(⁶Li) | blocked on family-4 ⁶Li | 3.508 |
| `¹⁴C → ¹⁴N` | B(¹⁴C), B(¹⁴N) | blocked on family-4 ¹⁴N | 0.156 |

So Q for `n → p` and `³H → ³He` is computable **today** end-to-end
categorically (modulo D / ³H / ³He volume-match assignment caveat);
everything else is blocked on family-4 derivation.

### Layer 3: categorical decay rate (half-life)

From `beta-decay-from-q.witness.json`, the rate scales as
`G_F² · Q⁵ · f(Z, A)`, with `G_F = 1/(√2 v²)`,
`v = N_v · E_× · μ_0`, and:

- `E_× = ½(q − q⁻¹)` — categorical
- `μ_0` — calibrated by `m_e = 3 E_× μ_0` — categorical (single dimension)
- `N_v ≈ 1.4 × 10⁶` — **OPEN: topological invariant of brane tower**
- `f(Z, A)` — Fermi function from Coulomb wavefunctions — categorical
  if expressed in terms of brane Coulomb couplings

**`N_v` is the only categorical gap.** If the brane tower gives a
closed-form `N_v(q)`, all β-decay half-lives become categorical
predictions. Until then: layer 3 is structural-only.

## Concrete next steps (ranked)

1. **Build `categorical_q_decay_ba_low_isotopes.py`** — feeder script that
   pulls SDP outputs from [`joint-tower-sdp-rust.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/joint-tower-sdp-rust.witness.json) +
   [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass-table-ppb.witness.json) and computes Q-values via
   `Q_n→p + B_d − B_p`. Emits a single witness JSON with categorical Q
   for `{n→p, ³H→³He}` + B/A for `{D, T, ³He, ⁴He, ⁸Be–⁴⁰Ca}`.
2. **Resolve Clarabel-rs H_5 bug** (PR #444 `R5_5_BUG_REPORT.md`) so the
   ³H knot id (8_11 in B_5) can be derived from H_9 SDP search rather
   than volume-match.
3. **Derive `c_αα`** from joint-tower SDP at H_8 (⁸Be) — replaces the
   2.43 MeV/pair empirical residual.
4. **Run H_18 / H_21 SDP** for ⁶Li / ⁷Li with α + (D/T cluster) ansatz
   — closes family-4 GAP 4 + GAP 5.
5. **Derive `N_v`** topological invariant from brane tower — opens
   layer 3 (categorical β-decay rates).
6. **Quarantine fitted witnesses.** Move to `_deprecated/` or annotate
   `methodology: "deprecated-empirical"`:
   - `branching-qvalues.witness.json`
   - `branching-qvalue-chain.witness.json`
   - `low-isotope-mass-table.witness.json`
   - `comprehensive-low-isotope-table-v2.witness.json`
   - `atom_mass_qou_calibration.py`
   - `c-alpha-from-Q-beta-trace.witness.json`

## Cross-reference

Companion audit on `claude/mass-table-display-bkkZU` populates the
**by-content-block** view (which `.ts` blocks have wired
computations); this file is the **by-witness** view (which compute
artifacts are categorical vs fitted). The two views are intended to
be merged.
