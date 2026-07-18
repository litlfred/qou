# Δ_λ closure: attack-vector map after the 2026-07-18 two-front session

**Date:** 2026-07-18 · **Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` ·
**Tier:** coordination / survey (scope-(a); no fit; nothing wired). Consolidates
the "review all new math for attack vectors" sweep against everything that
landed on `main` and in active siblings since the six-ansatz gate ruling.

## 0. Standing state of the gate

Six closure ansätze — Frobenius co-Casimir, Demazure-fibre, LP-Plancherel,
LP-Frobenius, crystal-graph, augmented Markov — all failed on the deuteron
(ruling 2026-05-19 / 2026-06-02, `docs/coordination/option-e.md`;
`docs/audits/2026-05-18-delta-lambda-gating-context.md`). The anti-fit rule
("no seventh **fit-based** ansatz") stands. The **direction/scope** narrowing
was lifted 2026-07-13 (owner general reversal,
`docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md`): any **derivation**
route is now in scope for all agents. A Δ_λ obtained by inverting the AME
anchors remains a **fit** — may be labelled, may not be wired as canonical.

## 1. What is newly settled since the six-ansatz ruling

The two-front 2026-07-18 session split `Δ_λ = sign · magnitude` and resolved
each front to a different depth.

### 1a. Sign front — DERIVED (not the open crux)

The chirality sign is `sgn(w_0^{S_{λ'}})` and is reproduced by the **principal
grading jet-order** valuation, not by any KL-weight sum:

- `n(λ) = min maj(SYT(λ))` (minimal major index over standard Young tableaux),
  `sign(λ) = (−1)^{n(λ)}` at the fourth root of unity `ζ₄`
  (`deltalambda_grho_jet_order_derivation_probe.py`; Lean
  `PrincipalGradingJetOrder.lean`, sorry-free
  `zeta4_eval_principalGrading` / `deltaSign_eq_one_iff_even`).
- The carrier `g_ρ` is the **content grading / pivotal twist**, and is
  **not** the Nakayama automorphism — refuted 12/12 (#3931,
  `NakayamaGradingObstruction.lean`, hand-audited): INV-1
  commutative ⇒ symmetric ⇒ ν = id; INV-2 semisimple ⇒ ν = id.
- The KL-weight sub-path (PROBE-4) stays **structurally pruned** by
  KL-positivity vs the mixed-sign target (Lean-proved
  `PartitionOf5.deltaSign_mixed`, PR #2416;
  `docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`).

**Consequence:** the sign is a solved, permanent contribution. The open wall
is entirely the **magnitude**.

### 1b. Magnitude front — STRUCTURE derived, one scalar open

The many-body magnitude has a derived *shape* with a single undetermined
scalar (#3924, `b4_slater_antisymmetrizer_exchange_sign.py`):

- Slater antisymmetrizer trace `(1/A!)·Σ_σ sgn(σ)·4^{c(σ)} = C(4, A)` — the
  `⁴He`-locality / occupation combinatorics; rank profile `{1,4,6,4,1,0,0,0}`.
- Cumulant `b₄ = −ln det(I + G)`, `det = (1 − 5m²)(1 − m²)`, spectrum
  `{±√5, ±1}`; positivity ceiling `m < 1/√5`.
- The magnitude wall is now **one real scalar** `m ∈ (0, 1/√5)`, not a
  per-partition table — a genuine narrowing of the search.

## 2. New proved prunes (structural exclusions, scope-(b), with cited invariant)

Three ingredients are now **structurally excluded** from a magnitude closure,
each with a proved invariant (not a scope-(a) numerical miss):

1. **pn-sign blindness.** The single-trace magnitude `= dim(λ)` and the
   `C(4,A)` occupation combinatorics are **isospin-blind** — they carry no
   proton/neutron label. Any magnitude built from them alone cannot reproduce
   a p/n-dependent split; the `³H`/`³He` mirror pair is the witness (see §3).
   *Invariant:* the antisymmetrizer trace depends on `A = Z + N` only, not on
   `(Z, N)` separately.
2. **y_λ-suppression.** The Frobenius weights `y_λ` in `Σ_λ y_λ χ^λ Δ_λ`
   suppress high-partition contributions; a closure whose magnitude grows with
   `dim(λ)` is fighting the weight. *Invariant:* the Plancherel/Frobenius
   pairing normalization (LP-Plancherel / LP-Frobenius ansätze already
   excluded on this ground).
3. **q-dim hidden DOF.** Using `d_q(λ)` (quantum dimension) in place of
   `dim(λ)` reintroduces a `q`-dependent free parameter — the total quantum
   dimension `D` route that was falsified on **both** the α_EM shared-wall
   sides (`D(q₀) = 11.357`, fibre `D(ζ) ∈ {1.66…3.80}`; #3871 / #3883). Any
   magnitude closure that leans on `d_q` inherits that same hidden DOF and
   must be treated as a fit until `q` is fixed independently.

## 3. The #3943 collective-residual finding (honest negative)

The per-pair bond-magnitude forward test (#3943,
`deltalambda_perpair_bond_magnitude_derive_probe.py`,
`B = m_e·Σ_n M_n(A)·Vol_n(K)`, `M_n = (n−1)`) is an **honest negative**
(scope-(a)):

- `z_naive = 0.499` is **excluded** — lands beyond the positivity ceiling
  (`det < 0`, i.e. `m > 1/√5`).
- `g_reeb = 0.44673` is physical (`< 1/√5`) but yields **no** single
  parameter-free `m` matching all four light isotopes simultaneously.
- The `³H`/`³He` mirror split is the sharp diagnostic: the determinant
  route predicts a `2.25×` split where the data shows a `1.22×` deficit.
  The residual is therefore **collective / non-additive** — a genuine
  many-body term, not a mis-set per-pair constant.

**Reading:** a purely **additive per-pair** magnitude cannot close the gap.
This does not exclude the per-pair *factor* (permanence principle: a proved
per-bond piece stays valid); it measures the size of the missing **collective**
term. Phrased as scope-(a): "the additive per-pair construction, alone, does
not reproduce the four-isotope magnitudes."

## 4. Ranked attack vectors now open

| # | Vector | New handle | Why now | Risk |
|---|--------|-----------|---------|------|
| 1 | **Per-pair hyperbolic volume on the `[1⁴]` complete graph** | `Vol_n(K)` on the `K₄` coordination graph, not a scalar bond | #3924 gives the `C(4,A)` locality; the missing collective term is a graph (not pair) object | med |
| 2 | **Icosahedral `1/√5` from the Σ(2,3,5) S-matrix** | the `[1⁴]` spectrum ceiling `1/√5` **exactly** matches the keystone vacuum row `(2/√5)(sin π/5, sin 2π/5)` | the `√5` bridge is a *proved* coincidence, not a fit — ties the magnitude scalar `m` to the icosahedral S-matrix already in the corpus | **high value** |
| 3 | **Bar-even-symmetrized b₄ cumulant** | symmetrize `b₄ = −ln det(I+G)` under the bar involution before evaluating | isolates the bar-even (mass) part from the bar-odd (decay) part — the same split that resolved c₃ | med |
| 4 | **Reeb marginal-stability** | `g_reeb = 0.44673` as a *collective* (not per-pair) input | #3943 showed it is physical but not additively sufficient — retry as a graph-level marginal-stability condition | low |
| 5 | **Resurgence / SDP lower bound** | bound `m` from below via the confinement SDP dual | orthogonal check; would bracket `m ∈ (m_SDP, 1/√5)` | low |

**Vector 2 is the highest-value lead.** The `[1⁴]` determinant spectrum
`{±√5, ±1}` gives a positivity ceiling `m < 1/√5` that coincides **exactly**
with the vacuum row of the Σ(2,3,5) (binary-icosahedral) S-matrix already used
in the keystone construction — `(2/√5)(sin π/5, sin 2π/5)`. That is a proved
algebraic coincidence, not a numerical near-match: if the magnitude scalar `m`
is pinned to that S-matrix entry, it is a **derivation**, not a fit. This is
the first vector that connects the magnitude wall to an object the corpus
already derives independently.

## 5. What stays closed

- The **six original ansätze** — no re-open; the anti-fit rule catches a
  seventh fit-based ansatz.
- **KL-weight PROBE-4** — Lean-proved structural prune (mixed-sign vs
  KL-positivity), stays pruned.
- The **q-dim / total-quantum-dimension `D` route** — falsified on both α_EM
  shared-wall sides; inherits the hidden-`q` DOF.
- **Additive per-pair magnitude** — #3943 honest negative; retry only at the
  **graph / collective** level (Vectors 1, 4).

## Cross-references

- Gate ruling + reversal: `docs/coordination/option-e.md`;
  `docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md`;
  `docs/audits/2026-05-18-delta-lambda-gating-context.md`
- Sign front: `deltalambda_grho_jet_order_derivation_probe.py`;
  `PrincipalGradingJetOrder.lean`; #3931 `NakayamaGradingObstruction.lean`
- Magnitude structure: #3924 `b4_slater_antisymmetrizer_exchange_sign.py`
- Forward test (honest negative): #3943
  `deltalambda_perpair_bond_magnitude_derive_probe.py`
- PROBE-4 prune: `docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`;
  Lean `PartitionOf5.deltaSign_mixed` (PR #2416)
- Shared-wall `D` falsification: #3871 (observable), #3883 (fibre)
