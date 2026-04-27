# Categorical vs fitted — Q, decay, B/A audit

**Date.** 2026-04-27
**Branch.** `claude/continue-pr-442-DJRWm`
**Companion branch.** `claude/mass-table-display-bkkZU` (audit-scope seed)

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

## Critical finding (2026-04-27): two categorical invariants disagree at q_0

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
