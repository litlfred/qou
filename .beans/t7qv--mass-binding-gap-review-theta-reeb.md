---
# t7qv
title: Mass/binding gap review + θ_λ via Reeb/na-Stokes jet-filtration (+ 4 gaps)
status: in-progress
type: milestone
priority: high
created_at: 2026-07-03T19:40:00Z
updated_at: 2026-07-11T22:05:00Z
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

## 2026-08-31 — magnitude gate RESTATED, and `M_n(K)` corrected

Probes: `computations/probes/alpha_residual_gb_jet_bodyorder_probe.py` (bean
`qou-o1dh`) and `computations/probes/mixed_cluster_count_probe.py` (4 assertions
each). Audit: `docs/audits/2026-08-31-alpha-residual-gb-jet-bodyorder.md`.

### 1. The gate's target is misstated by ~4×

This bean's magnitude gate is aimed at the "**irreducible 4-body α-unit
(~16–21 MeV ⁴He residual)**". That figure is a **pairwise-chain residual** — what
the `(A−1)`-bond sum fails to reach — which lumps together every body order ≥ 3
*and* credits `pp`/`nn` bonds at ~2.4–2.5 MeV each.

**Nature binds neither.** The deuteron is the only bound two-nucleon system
(`³S₁`, 2.2246 MeV); `pp` and `nn` sit in the `¹S₀` channel by Pauli and are
unbound virtual states (`a_pp ≈ −17.3 fm`, `a_nn ≈ −18.7 fm`, vs
`a_np(¹S₀) ≈ −23.7 fm`).

With `b₂(pn) = 2.2246`, `b₂(pp) = b₂(nn) = 0`, the Ursell–Mayer expansion of ⁴He
from AME2020 alone is

| order | MeV | share |
|---|---|---|
| 2-body | 8.8983 | 31.45 % |
| **3-body** | **14.6032** | **51.61 %** |
| 4-body — the genuine α unit | **4.7942** | 16.94 % |

**Three-body dominates four-body by 3.05×.** So the gate should target
**≈ 4.8 MeV**, and most of what it has been chasing is a *three-body* object.
That matches standard nuclear physics — chiral-EFT 3N forces are essential at
`A = 3,4`, genuine 4N forces are small.

### 2. `M_n(K)` must count MIXED clusters only

The 2026-07-11 frontier update takes `M_n` from the max-contact packing, with
`A ≤ 4` simplex `= C(A,n)`. That over-counts: a cluster binds only if it has at
least one proton **and** at least one neutron, since `pp`, `nn`, `ppp` and `nnn`
are all unbound. So

    M_n(Z,N) = C(A,n) − C(Z,n) − C(N,n)          (= Z·N at n = 2)

Unfitted — forced by `(Z,N)` and by which channels bind. At `A ≤ 4` the simplex
is complete, so there is **no arrangement freedom** and nothing is chosen.

With the single deuteron anchor `E = B(D)`, `B(K) = E·Σ M_n·a_D^{(n)}`:

| | `M_n` mixed | `C(A,n)` err | **mixed err** |
|---|---|---|---|
| ³H | `[2, 1]` | +13.75 % | **−12.48 %** |
| ³He | `[2, 1]` | +25.00 % | **−3.82 %** |
| ⁴He | `[4, 4, 1]` | +9.13 % | **−6.59 %** |
| worst | | 25.00 % | **12.48 %** |

**The worst error halves.** And the sign structure flips coherently: `C(A,n)`
over-counts uniformly, mixed-only under-counts uniformly. An over-count that
becomes an under-count on removing *exactly* the unbound channels is what a real
correction looks like — the three-isotope sign agreement carries more than the
magnitude.

For scale in this same lane: the pairwise chain gives ⁴He at −76 %, the jet tower
at unit weight −91 %.

### 3. It does NOT rescue `A ≥ 5` — Part 5's refutation stands

At ⁶Li: `C(A,n)` gives **+772.9 %**, mixed-only **+712.6 %**. Removing the
pure-flavour clusters takes out ~8 % of the excess and nothing more. **The
flavour correction is necessary and not sufficient**, and the `A ≥ 5` fix is
Part 13's geometric saturation — flavour does not touch it. Part 5 and Part 13
are one open item seen from two sides.

### 4. ⚠ The geometric route is NOT yet fit-free

Taking the contact graph seriously, `M_n` = number of `n`-cliques. Six
close-packed spheres in an octahedral arrangement give `K_{2,2,2}`: 12 edges, 8
triangles, **0 four-cliques** — the cap kills every `n ≥ 4` term outright, which
is Part 13 made concrete. That collapses the divergence.

But the 3p3n **arrangement** on those six sites is a free choice:

| `M_2`, `M_3` | B (MeV) | err | labelings |
|---|---|---|---|
| 6, 6 | 31.193 | **−2.50 %** | 8 of 20 |
| 8, 8 | 41.590 | +29.99 % | 12 of 20 |

against `B(⁶Li) = 31.994`. **A 32.5-point spread, and the favourable member is
the *minority* labeling.** Nothing derives the arrangement, so `−2.50 %` is a
member-pick — the failure mode this corpus has withdrawn three times this
session. Recorded because the number is attractive enough to be dangerous:
**anyone carrying it forward must derive the arrangement first.**

### What this does and does not close

- **Advances** the open `θ_λ w_n(K) derive-or-refute` item: one factor of `M_n`
  is now derived rather than assumed, and the `A ≤ 4` error halves.
- **Does not close** it: the `A ≥ 5` behaviour is untouched, and the geometric
  arrangement is undetermined.
- **Restates** the magnitude gate's target from ~21 MeV to ≈ 4.8 MeV, and
  reassigns the bulk to three-body — which changes what `Gap #2` (3-body /
  whole-A link-volume) is for. That gap is no longer a side item; on this
  accounting it is where the majority of the binding lives.

### Also worth flagging

`derive_binding_chain_cooperative`'s `pp`/`nn` per-bond constants (2.38/2.49/2.53
signed, 2.91/3.89/5.18 log) have no empirical counterpart. That is a modelling
choice and deserves a note wherever those constants are quoted.

---

## Gap #2 (3-body link-volume) — worked 2026-08-31. The substrate fixes the arity, and it refutes the assignment.

Probe `computations/probes/link_assignment_census_selectivity_probe.py`
(5 assertions). Prior work first, because I initially presented part of this as
new and it is not: `docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`
(`qou-8ms1`) already established that `6_2`/`8_11`/`L6a4` are an **admitted
fit** and measured the census degeneracy. Re-measured here only as a guard.

**What is new** answers that audit's own named next step — *derive a complexity
bound on `K` from the substrate with no reference to `B_AME`, then ask whether
the volume match is unique inside that class*.

The invariant is the closure's **component count**. The canonical word's letters
are `c·σ_g + d·1`, and `σ_g`, `σ_g⁻¹` project to the *same* transposition, so
the permutation — hence the cycle count — is identical on every branch and under
every sign convention. Measured exact over `0 ≤ Z,N ≤ 5`, both `pn_convention`s,
nine bond multiplicities:

    c_free = 2A                                  23/23 exact
    c_atom = 2A − #(odd-multiplicity bonds)     414/414 exact   ⇒ A+1 at unit mult.

A bond merges only when its crossing count is odd. This **corroborates
`QOU.MassTheory.ClassicalTraceFloor` (`qou-zrx2`, sorry-free) by an independent
route** — that file derives `cAtom = A+1` combinatorially; here both counts fall
out of the actual word's permutation.

**All four registry entries fail it:** `6_2` 1 vs 3, Hopf 2 vs 3, `8_11` 1 vs 4,
`L6a4` 3 vs 4. The `2H` rows reproduce the audit's scope-(b) finding; **`3H` and
`3He` are new** — the audit reached only `A = 2`. The objection is uniform, not a
deuteron peculiarity.

**Intersected with the volume window the class is EMPTY:**

| atom | in volume window | with `A+1` cusps |
|---|---|---|
| ²H | 799 | **0** |
| ³H | 1,102 | **0** |
| ³He | 26,843 | 29 |

So the derived restriction exists and leaves nothing standing at `A = 2, 3`. At
³He the best survivor `L14n62525` (+0.598 %) beats `L6a4` (−2.969 %) fivefold —
**not proposed as a replacement**, only evidence the incumbent is not best in its
own class.

Component count is *necessary*, so emptiness refutes while a survivor is only a
candidate; and the arity counts are upper bounds (the census is not exhausted by
link exteriors), so the emptiness strengthens.

### What this means for Gap #2 as a target

The 3-body link-volume route needs a **4-component** link for both ³H and ³He,
not `8_11` (a knot) and not `L6a4` (3 components). And since the two isotopes
have the same derived arity, no volume assignment distinguishable at the
`A + 1` level can supply the ³H–³He split — which
`binding_color_vs_charge_tn3he.py` independently shows is Coulomb, not strong.

### Next

Not a better census pick. The open item is what the owner named: **`K` should be
an SDP solution via knot convolution**, i.e. an *objective* over Gröbner–Shirshov
normal forms, taking no `B_AME` input, with the `A+1` arity as a hard constraint.
The convolution `K_word = atom_word ++ cp_inv_word` is already in
`binding_k_solver.py`; what is missing is the minimisation and the finitude bound
`conj-canonical-knot-id-sdp.md` lists as open.
