---
# t7qv
title: Mass/binding gap review + θ_λ via Reeb/na-Stokes jet-filtration (+ 4 gaps)
status: in-progress
type: milestone
priority: high
created_at: 2026-07-03T19:40:00Z
updated_at: 2026-08-31T17:09:49Z
---

Branch `claude/mass-binding-gap-review-2026-07-03`. Owner: "lots new on main +
siblings, do thorough review; how to integrate with workplan; how to close
canonical mass/binding gaps." Then steered gap #1 (θ_λ) "via Reeb based on
computational time of the knot operator" + "hyperbolic volumes via na-Stokes".
Owner said: ignore collision / duplicate ok.

## Review (3 Explore agents, 2026-07-03)

- Absolute nucleon mass SETTLED (2026-06-24, λ_A fit excised; +2.89% m_p gap
  dissolved). L2 100×: **3/7** pass (m_e, m_p anchors + m_K/m_π); fail m_μ 964×,
  m_n 181×, Q_β 160×, Δ_pn 159×. m_n+Δ_pn ride on Q_β (Path C).
- Frontier = 9b per-isotope binding Δ_λ (extensive, sign-only ℓ¹-excluded, IMME
  form). Two keystones: Q_β Habiro F(q) (unlocks 3/4), 9b per-λ weight.
- Fit-walls: no 7th Δ_λ ansatz; don't re-fit Q_β; c_k≥3 owner-gated.

## Delivered this tranche

- [x] **θ_λ gate — extensive MECHANISM implemented + confirmed** (gap #1, owner steer).
      knot-op holonomy = Yekutieli na-Stokes surface integral → SW period
      a_D^(n)=∮λ_SW^(n)=lw(n−1)=mean quantum dim (#1765), residues=per-block dim_q=θ_λ.
      Super-exponential (1,1,1.34,2.53,5.38,13.56,…) = the EXTENSIVE channel the
      intensive arccos-phase lacked. Implemented the unstaffed jet-filtration
      consumer `binding_manybody_jet_filtration.py`: unit-weight gives 4.87× ⁴He/D
      growth (vs flat phase; exp 12.72×) — mechanism present, UNDERSHOOTS. Open
      piece localized to residue weight w_n(K) (ρ·A q-difference rule R(q,x), NOT a
      fit). Audit 2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md.
- [x] **Currency fix (gap #5)**: precision-goals.md self-contradiction (2/7 TL;DR
      vs 3/7 table vs 1/6 Distinction) → reconciled to witness truth 3/7.

## Open (this tranche, queued)

- [x] **θ_λ extensive MECHANISM Lean-proved + in paper** — QOU.Mass.jetBinding_mono
      / jetBinding_lt_succ (sorry-free, lean-direct verified); block
      prop:jet-filtration-binding-extensive. Addressed all Gemini+Copilot review.
- [ ] **θ_λ w_n(K) derive-or-refute (closure — options in the audit).** RECOMMENDED:
      w_n(K) = hyperbolic link-volume of the n-body sub-cluster (literal na-Stokes;
      merges with gap #2 3-body link-volume; non-fit). Backstop: derive-or-refute the
      q-difference R(q,x) from the 6 anchors (per-isotope constant ⇒ fit ⇒ refute).
      Cherry-pick OK'd (owner 2026-07-03): pull q-Bessel R from #3265, exact-ℚ from
      #3247, per-knot VolDensity from #3205. Coordinate: intent posted #3247/#3260/#3265.
- [ ] **Gap #2: 3-body / whole-A link-volume** — enumerate ⨝_K inter-nucleon bonds,
      compute whole-A link-volume (~40% A=3 pairwise gap). Feeds the jet w_n(K).
- [ ] **Gap #3: A=3 mirror magnitude** (³H/³He; best structural 2.52%).
- [ ] **Gap #4: 9a per-knot VolDensity migration** (bean 0voz; 64/65 atom scripts
      uniform) — gated on R(K) derivation; check gate first.

## Notes

- Coordinate (per owner: duplicate ok): siblings on Q_β kernel #3265/#3242/#3258/
  #3263; Δ_λ #3247/#3205; own-theme sibling #3260 (Gram-norm probe).
- Milestone parents in corpus: zgat (9b approaches), 830y (Δ_λ-gate FOCUS), w9uk
  (currency → #3247). This bean coordinates with them, does not replace.
- CI billing-gated; Lean via lake-cache restore + lean-direct.

## Frontier update (2026-07-11, later — corpus-grep before re-probing)

The w_n(K) closure was massively advanced by siblings **today** — do NOT re-probe
the naive routes. Authoritative: [`docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`](../docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md)
(PR #3545, 13 parts) + #3534 (numerical w_n derive-or-refute) + #3548 (W_λ connected
transfer matrix) + #3549/#3551 (coordination/contact binding).

**Resolved redirect (was: "derive R(q,x) weight kernel"):**
- The weight is NOT an algebraic kernel R(q,x). Part 4 refuted the Frobenius-dual/
  na-Stokes kernel (y_λ normalize tr_M to a trace ⇒ constant ratios, can't supply the
  extensive weight). Part 5 refuted summing a_D^(n)×amplifying-weight to A
  (⁶Li +920%…¹²C +2.3e6% — super-exp period × bounded/amplifying weight can't be
  linear in A).
- **The missing piece is GEOMETRIC:** per-cluster energy = a_D^(n) (deuteron-anchored
  ≈2.22 MeV/bond); the knot topology supplies the CLUSTER COUNT M_n(K):
  M_2 = pairwise linking, M_3 = triple Milnor μ̄₁₂₃ (Part 7, validated: Hopf 1,
  Borromean μ̄=1, chain μ̄=0). Edge set = **max-contact sphere packing** (Part 13;
  A≤4 simplex = C(A,2), A≥5 saturates below). Per-bond b* = **#3548's connected tr_M
  part** = centered ghost Gram-quadratic norm (Part 12, exact identity; deuteron 0.193).
- **NOTE for future me:** the "C(A,n) body-order combinatorial weighting" (⁴He gets
  6·a_D²+4·a_D³+1·a_D⁴ ≈ 13.88× vs 12.72× exp — a tempting fit-free light-nucleus
  match) is exactly Part-13's A≤4 simplex bond-count AND the Part-5-refuted full tower;
  it overshoots catastrophically at A≥5. Verified against baseline
  binding_manybody_jet_filtration.py (unit-weight 4.87×). Do not write it up as new.

**Remaining open (both contested/gated — coordinate, don't solo):**
- b* value = H₆ seminormal-Gram build = #3548 PROBE 2 ("coordinate before solo").
- A≥5 max-contact packing geometry + cluster/halo (⁶Li=α+d, ⁹Be) deviations =
  owner-gated s5-so3 keystone territory.

Verdict: t7qv's quantitative closure is being driven by the #3534/#3545/#3548 cluster;
prop:jet-filtration-binding-extensive (qualitative) stays the proved core. This session
reviewed + recorded the frontier; did not add a colliding probe (corpus-grep discipline).

## Cross-ref: Askey/Whipple channel-rotation route also NULLs the algebraic weight (2026-07-13, PR #3749, merged)

The Whipple-rotation identification thread (channel-rotation tie of the even
(cosh/binding) and odd (sinh/Q_β) channels of 𝔙; blocks
`whipple-rotation-intertwining`, `binding-qbeta-complex-volume`) reached its
honest terminus and **independently corroborates the geometric redirect above**:

- **Third algebraic-route NULL.** The bar-even/bar-odd binding split is the most
  natural place for the Askey/Ismail–Masson channel amplitude to appear, yet the
  bare Whipple toroidal amplitude `|C(ν,μ)| = √(2/π)/Γ(ν+μ+½)` at the physical
  forced windings `(μ,ν)=(½,d−½)` does **not** reproduce the observed
  `B_even/B_odd` deuteron ratio (`whipple-observable-ratio-probe`: 51% off, no
  parameter-free `{C,1/C,amp,1/amp}` match). This is the toroidal-amplitude
  analogue of Part 4's Frobenius-dual/na-Stokes kernel refutation — a *different*
  algebraic object, same failure. Reinforces "the weight is NOT algebraic; the
  missing piece is geometric" — **do not re-probe the Askey/Whipple amplitude as
  the binding weight.**
- **Factor-2 shortcut FALSIFIED.** The tempting deuteron `2/|C| = 3.33 ≈ 3.373`
  (1.2%) is a coincidence — `B_even/B_odd = A/|C(d=A)|` fails 446%/1644% at A=3/4
  (the two N=Z cases 2H/⁴He share a fixed 3.33, a numerology artifact). Recorded
  in the witness `factor2_generalization_falsification`; do not re-chase.
- **What IS proved (permanent, per §"refuted"-scope discipline).** The even↔odd
  channel rotation `rotation_step` (sorry-free, categorical R) and the
  winding-swap reduction `channelIndexed_swaps_windings` stand — the *structural*
  tie is exact; only its bare *amplitude → MeV binding ratio* map is what NULLs.
  Consistent with your per-bond anchor `a_D ≈ 2.22 MeV = B_AME(²H)`: the deuteron
  binding is the anchor, not something the toroidal amplitude re-derives.

Net: the Askey/Whipple algebraic direction for the binding weight is **exhausted**;
t7qv's geometric M_n(K) frontier (Milnor linking + per-bond a_D) is the live route.


---

### 2026-08-31 — max-contact simplex bound Lean-proved (`w_n(K)` geometric piece)

This bean's frontier update records the `w_n(K)` closure's missing piece as
**geometric**, with the edge set a max-contact sphere packing:

> "Edge set = max-contact sphere packing (Part 13; A≤4 simplex = C(A,2),
>  A≥5 saturates below)"

and notes the tempting fit-free light-nucleus match — ⁴He weighted
`6·a_D² + 4·a_D³ + 1·a_D⁴` — is exactly that A≤4 simplex bond count, i.e.
`C(4,2), C(4,3), C(4,4)`. That was **prose, and load-bearing**. It is a theorem,
so it is now proved.

**`QOU/Mass/MaxContactSimplex.lean`**, 5 theorems, sorry-free on
`[propext, Classical.choice, Quot.sound]` (`he4_body_order` needs **no axioms**):

| theorem | statement |
|---|---|
| `inner_spokes` | the Gram entry is `c²/2` |
| `linearIndependent_spokes` | the spokes `pᵢ − p₀` are independent |
| `card_le_finrank_succ_of_equidistant` | at most `finrank + 1` pairwise-equidistant points |
| `not_five_equidistant` | **no five equal spheres are mutually tangent in 3D** |
| `he4_body_order` | `C(4,2), C(4,3), C(4,4) = 6, 4, 1` |

Equal spheres are mutually tangent iff centres are pairwise equidistant, so the
A≥5 "saturates below" is exactly the impossibility of a complete contact graph.
Proof: with `vᵢ = pᵢ − p₀` the Gram is `c²` diagonal, `c²/2` off, so
`‖Σaᵢvᵢ‖² = (c²/2)[(Σaᵢ)² + Σaᵢ²]`, vanishing only at `a = 0`.

Verified numerically first, with a firing control (a wrong off-diagonal breaks
the identity on 967/1000 random vectors).

**Not touched:** the routes this bean marks refuted (Part 4 Frobenius-dual
kernel, Part 5 amplifying-weight tower).


---

### 2026-08-31 — Gap #2: corpus-grep first, then the one piece that was closable

**What the grep found — Gap #2 has moved past this bean's July frontier, and the
direct route is blocked for a reason not recorded here.**
`2026-08-08-volume-binding-four-point-is-unrunnable.md`: the whole-A link-volume
four-point test is **data-blocked, not effort-blocked** — only 2 of the 4 targets
are usable (D has `Vol = 0`, the Hopf link not being hyperbolic; ⁴He has no
Reading-2 link). Not re-probed, per this bean's own warning. Two audits from
2026-08-30 (`coordination-saturation-formalized`,
`bonded-pair-linking-is-derived-and-not-uniform`) advanced adjacent pieces.

**What is closed.** `CoordinationSaturation.lean` refutes complete-graph
coordination by its **consequence** (`complete_graph_no_saturation`: the
`C(A,2)` model drives `B/A` past every bound), then takes bounded degree as a
modelling **assumption**. `MaxContactSimplex` proves the complete contact graph
is geometrically impossible for A ≥ 5. **The two had never been connected.**

> `no_complete_contact_of_five_le` — in 3D, no `A ≥ 5` equal spheres are all
> mutually tangent. Sorry-free.

So `C(A,2)` is not merely wrong by its predictions for heavy A; it is
geometrically **unavailable**. That is this bean's "A≥5 saturates below" as a
theorem rather than a premise, and an independent second refutation.

**What it does not supply.** `bounded_degree_saturates` needs a **degree** bound
— the 3D kissing number (12, Schütte–van der Waerden). Not proved here, and not
a modest formalisation.

**🪤 A trap, verified, recorded in the file.** The standard spherical-code
argument (`Σ⟪uᵢ,uⱼ⟫² ≥ m²/d` vs `Σ_{i≠j} ≤ m(m−1)/4`) gives `m ≤ 9` in d=3.
**False** — the icosahedral configuration realises 12. It needs
`|⟪uᵢ,uⱼ⟫| ≤ ½`, but tangency bounds the inner product only from **above**.
Measured there: inner products span `[−1, 0.4472]`, so `⟪⟫ ≤ ½` holds while
`|⟪⟫| ≤ ½` fails at the antipodal pairs; `Σ⟪⟫² = 48` exactly, meeting the
Frobenius bound `m²/d = 48` with equality and exceeding the naive ceiling 45.

**Gap #2 stays OPEN** — the link-volume half is data-blocked.
