# Binding / mass workplan refresh — week review 2026-07-18 → 2026-07-24

**Tier:** coordination (no new results claimed). Owner-requested review of the ~500 main
commits and active siblings since the uploaded-papers sweep (PR #3950 / #4006), with an
updated prioritized workplan. Sources: main log clustering, the window's audit docs, the
open-PR landscape (15 PRs), and the 07-19/07-20 upload batches.

## 1. Frontier snapshot (what changed this week, per front)

| Front | Closed this week | Named open object now |
|---|---|---|
| **Δ_λ sign** | Fully proved (jet-order valuation) | — (permanent) |
| **Δ_λ magnitude** | Entire exchange-determinant-cumulant family machine-excluded (3-lemma Lean pincer); bar-odd re-search shut (ℓ¹-ceiling); cumulant→MeV map resolved as one cluster expansion (deuteron to 6 digits) | A **non-determinant graded-dimension object with two-sided correction** — `[A]_q!` escapes the det cap but overshoots +21% at A=4; Demazure damping brackets A=4 but A=3 needs amplification ("one knob cannot do both") |
| **E_unit** | Source identified: the counit, `μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.6295 MeV`, 0-param, deuteron −9.2% | Higher-order counit / NA-Stokes terms (the −9%); octahedral 4-dilogarithm route live on PR #4127 |
| **Covariance kernel (`qou-x631`)** | 4 proof routes eliminated (phases 1–2); obstruction pinned (`f^λ` outside the polynomial algebra) | Phase 3: a genuine tilted-limit-shape large-deviation bound for `T₃ ≤ 0` |
| **Keystone / C1** | `KeystoneBridgeC1Binding.lean` sorry-free: normalizer `N(n) = (n−1)!` forced; `ρ·A` scale rule an output, not a fit; C1 ≢ GGM excluded on 5 routes (invariant: isoclinicity) + Door-v ℤ/2 parity guardrail | Geometric identification C1 ↔ SW jet-prolongation symbol (scoped; the 4 new SW uploads are its reading list) |
| **α_EM** | F-construction T1–T5 + R1 closed; parameter-free target assembled | **R2 only** — loop-weight provenance; owner-ruled NOT proved; `1/(8π)` stays phase-4, do not wire |
| **Q_β value leg** | Proved measurement-limited (`no_anchor_invariant_realizes_swing` + `MeasurementLimitedFloor`); `c₄^even` exact but 830× too small; a production-wiring violation removed from `canonical_mass.py` | Walls: Pentagon/G3 = one missing Mathlib theorem (Hadamard factorization; PI-1..3 scaffolds attack it); φ_odd at ~1 sig fig, blocked on unprinted GGM data |
| **q₀ / Bring / τ** | Polarized Bring det′Δ computed (idea A1: 1.38758, blow-up killed, honest negative — q-dictionaries polarization-blind) | Same categorical wall as α_EM R2 (`TauRhoHodgeLift` inhabitation) |
| **I_𝓑₃ / 3D-index** | B1 landed: `I_𝓑₃(0) = 1+13q²−16q³−97q⁴+…`, 4/4 self-tests | The index→`F_Bor`/ρ(𝓑₃) bridge — derive, don't fit. **No sibling picked this up** |
| **L2 dashboard** | Re-certified: `beats_100x = 2/7` unchanged; the 5 misses proved measurement-limited (Q_β/m_n/Δ_pn via c₃; m_p/m_μ via q₀) | — |

## 2. Uploaded-papers ideas scoreboard (from the merged #3950 sweep)

Done: **A1** (honest negative), **A2** (hauptmodul gate, no consumer yet), **A3** (trace
prune + re-scope), **B1** (I_𝓑₃, no consumer yet), **A5/B4 partial** (vector2 pincer:
cospectrality refuted exactly, `g₅ = √5` pinned; residues below), **B5** (taken up by
siblings and effectively pruned — rotated index is bar-even anchor-smooth), **B7**
(consumed inside B1's well-definedness gate).

Unclaimed: **A4** (X₀(50)/50a Hecke gate), **A6** (S₅-invariant theta characteristic /
K_Q), **A7** (level-5 congruence functor), **B2** (angle-structure LP ↔ SDP), **B3**
(normal-surface collective term), **B6** (index convolution along cusps).

## 3. New uploads (07-19/07-20) — pre-loaded ammunition, mostly unreferenced

SW/integrable-systems cluster (Grassi–Gu–Mariño 1908.07065, Donagi 9705010,
Donagi–Markman 9408004, Braden–Marshakov 0205308) → the **C1 ↔ SW geometric leg**;
NA-Stokes cluster (Broda 0012035, Magnus-expansion phys-rep09) → the **E_unit −9%
expansion**; McPhail-Snyder–Reshetikhin 2509.02354 → fibre holonomy braiding (taken up
by PR #4127); Ramis–Sauloy–Zhang 0903.0853 + Nguyen–Tran strong-AJ → already consumed
(qlift doors; NT Lean epic).

## 4. Prioritized workplan (this session's queue)

1. **I_𝓑₃ → F_Bor bridge** (B1 follow-on, unclaimed; this session's own artifact).
   Extend the producer to per-cusp graded classes (advances B6 simultaneously);
   formalize-first: state the integer/grading invariant a *derived* bridge must satisfy
   before touching coefficients. No fitting to the 2.89% gap.
2. **E_unit higher-order counit terms** via the Broda + Magnus uploads (the −9.2%
   deuteron residual). Derive the next order along `(q−q⁻¹) = (v−v⁻¹)[2]_v`; check
   D/T/³He/⁴He forward-only. Coordinate with PR #4127 (octahedral route) — distinct
   angle: analytic Magnus order-2, not the 4-tetrahedron resummation.
3. **Vector-2 A5 residue**: extract BN12's printed anti-involution S′ data and run the
   cospectrality comparison vs the `[1⁴]` exchange matrix — kills or revives the Bring
   leg of Vector 2 for `m ∈ (0, 1/√5)`.
4. **B4 residue**: GK cyclic-dilogarithm D₅ product on the explicit 4₁ triangulation —
   the exact fibre-level 1/√5.
5. **Δ_λ magnitude two-sided search, formalize-first**: Lean-state the invariant any
   graded-dimension family must satisfy (escape det cap at A=4 AND amplify at A=3);
   enumerate only survivors (parabolic/skew quotients of `[A]_q!`). Post intent on the
   live Δ_λ sibling PRs (#4131/#4132/#4134).
6. **Covariance-kernel phase 3**: tilted-limit-shape large-deviation bound for `T₃ ≤ 0`
   (four routes already dead; the target is precise). Overlap-OK research; post intent.
7. **z-geometric C1 ↔ SW smallest sub-claim**: Newton-polygon-level yes/no between the
   C1 slope-½/theta structure and the quantum-SW-curve Stokes data (Grassi–Gu–Mariño).
8. **A2 gate consumer**: wire `t₅(τ₀) = −10` as a discrete validator on the q₀ ↦ τ
   dictionary candidates (cheap; same spirit as the A3 trace prune). Pairs with A4
   (X₀(50)/50a integer Hecke gates) if picked up.
9. **B2 dual dictionary**: GHHR Prop A.3 angle-structure LP duals ↔ the confinement-SDP
   `y_star`/`active_set` fields (structural, fit-free, lands in existing infra).

**Walls — do not attempt:** Q_β/m_n value improvements (proved measurement-limited;
c_k-tower fitting is the named forbidden move); wiring `1/(8π)` (owner ruling); bar-odd
Δ_λ sign re-searches (ℓ¹-ceiling); deriving decay from the binding kernel across parity
(Door-v guardrail).

## 5. Sibling triage flags (critical-distance duty; not verdicts)

- **PR #4136** (6Li `B_gate` via a `[10]_q/[6]_q` multiplier "found" to close a 2.6 MeV
  gap, wired into `mass_binding_dashboard.py` with baseline switched) and **PR #4135**
  (4He toroidal ratio closing a 1.7 MeV gap) both pattern-match the anti-fit rule's
  target: a post-hoc correction selected because it lands on AME, then wired. Needs
  anti-fit triage before merge: is the multiplier *derived* from a stated principle, or
  selected? (Cf. the just-removed production-wiring violation in
  `2026-07-19-qbeta-toroidal-tower-overclaim-audit.md`.)
- **PR #4132/#4131/#4134** (Δ_λ H₃-vs-H₄, q-dilog channel, deuteron B2 formula):
  open-outcome research overlapping item 5 above — coordinate, don't stand down.

## 6. Stale-bean flags (other sessions' beans — flagged here, not modified)

`qou-x631` (update to phase-3 scope), `qou-a46k` + T1–T5 children (close; superseded by
R2-only state), `qou-folk`/`qou-0rzk` (owner-gated post-R2-ruling), `kehn` (forbidden
move post-measurement-limited proof), `qou-25zr` (re-scope to the surviving `Vol`/b₄
item), `qou-f69k`/`8we6` (c₄ shown immaterial), `z2bn` (needs owner F1/F3 framing),
`ovud` (wiring risk — re-examine against the overclaim audit), `qou-zezz` (check against
the `qou-esx7` epic), `t7qv` (superseded).

## Cross-references

- Idea provenance: [`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](../audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md)
- Executions: [`2026-07-18-vector2-double-pincer-a5-b4.md`](../audits/2026-07-18-vector2-double-pincer-a5-b4.md),
  [`2026-07-18-borromean-3d-index.md`](../audits/2026-07-18-borromean-3d-index.md),
  `TrBIntegerTracePrune.lean`, `BringHauptmodulGate.lean`
- Week's key closures: `2026-07-18-deltalambda-exchange-determinant-family-nogo.md`,
  `2026-07-19-cumulant-mev-map-cluster-expansion.md`, `2026-07-19-eunit-source-is-the-counit.md`,
  `2026-07-20-keystone-bridge-c1-binding.md`, `2026-07-20-close-1ppq-attempt.md`,
  `2026-07-19-alpha-em-r2-owner-ruling.md`, `2026-07-20-doorv-guardrail.md`
- Sibling attack map: [`keystone-multivector-attack.md`](keystone-multivector-attack.md) (PR #4058)

## Addendum — coordination pass (2026-07-24, post-/coordinate)

- **Triage task resolved by sibling:** #4144 (`coordinate-delta-lambda-front`) executed the
  fit rollback — #4135/#4136 CLOSED (owner directive), cluster-A shared pre-revert base
  documented. Bean `qou-nng0` closed citing #4144.
- **W5 on hold** until #4144's convergence path for #4132/#4133/#4134/#4137 settles
  (one canonical Δ_λ PR + thin deltas); then coordinate there.
- **W7 sibling-led:** #4140 thread 2 scaffolds the C1 ↔ DM-cubic/SW route
  (`CategoricalLagrangianDMCubic.lean`; open wall `qou-jqof` = derive `q_cubic = C1`).
  Distinct-angle Newton-polygon check remains possible but post intent on #4140 first.
- **Parallel workplan:** #4146 is a second same-day refresh (α_EM B2 lead + sibling-epic
  map); cross-linked, no inconsistencies — read both.
- **In flight this session:** W1 (I_𝓑₃ → F_Bor bridge invariant), W3 (BN12 S′ spectrum),
  W4 (GK D₅ product).
