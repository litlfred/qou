---
# t7qv
title: Mass/binding gap review + θ_λ via Reeb/na-Stokes jet-filtration (+ 4 gaps)
status: in-progress
type: milestone
priority: high
created_at: 2026-07-03T19:40:00Z
updated_at: 2026-07-03T20:10:00Z
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
