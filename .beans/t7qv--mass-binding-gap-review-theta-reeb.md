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

---

## `K` as an SDP solution via knot convolution — worked 2026-08-31. There is no SDP to solve.

Owner steer: *"knots should be SDP solutions via knot convolution."* Followed to
the end. Probe `computations/probes/binding_k_convolution_sdp_probe.py`
(6 assertions). The answer is negative in a specific and useful way.

**1. The convolution leaves nothing to optimise.** `binding_k_solver.py` defines
`T_w(atom) = K · ⊗ᵢ T_w(nucleonᵢ)`, `K_word = atom_word ++ cp_inv_word`. Given
the canonical word and its `include_inter=False` restriction (which *is* the
constituent product), `K` is **determined** — every averaged letter `σ − h/2`
has eigenvalues `±(q+1/q)/2 ≠ 0`, so the constituent product is invertible and
`K = ρ(atom)·ρ(free)⁻¹` exists in every block. No free variable. The only
askable question is whether that `K` meets the constraints. It does not.

**2. Derived binding arity `c(K) = 2A+1`** (46/46 exact). No registry
`binding_link_name` has it — Hopf 2 vs 5, `8_11` 1 vs 7, `L6a4` 3 vs 7. The
separate heuristic `K_word` field: `[3,6]` (³He) matches at 7; `[3,3]` (²H)
gives 6 vs 5; `[3,4,6,7]` (³H) gives 5 vs 7. The ²H row is structural — `σ₃²` is
a **full twist**, two crossings, where the canonical `pn` bond has one, and an
even multiplicity merges nothing. Different bonds, not a near-miss.

**3. PSD-feasibility is a crossing-parity condition.** `ρ_λ(σ)` has eigenvalues
`{q₀, −1/q₀}` in every block of dim ≥ 2, so `ρ_λ(σ^k)` is PSD **iff `k` is
even**. At `H_3`: unknot +1.000 PSD, `σ` −0.901, `σ²` (Hopf) +0.812 PSD, `σ³`
(trefoil) −0.731, `σ⁴` +0.659 PSD. This explains every recorded outcome at once
and means the program **cannot select**.

**4. It rejects the corpus's own constituent.** `binding_k_solver.py` states the
nucleon trefoil is "the unique PSD-feasible canonical element" at `H_3`. It is
not PSD in either presentation, and neither is this repo's own nucleon word
(proton −0.739, neutron −0.911, PSD in 1/3 blocks). The `H_3` element that *is*
PSD-feasible is the full twist. Flagged in that file's docstring, scoped: it
contradicts a plain reading, and does not settle a narrower "R5-minimal class"
reading, which is undefined there.

**5. The determined `K` is infeasible.**

| atom | blocks | atom PSD | K PSD | worst atom | worst K |
|---|---|---|---|---|---|
| ²H | 11 | 1/11 | 1/11 | −4.210318 | −1.595181 |
| ³H | 30 | 1/30 | 2/30 | −9.531563 | −4.265691 |
| ³He | 30 | 1/30 | 2/30 | −10.040628 | −3.646531 |

**Every** surviving block is 1-dimensional — `(n)`, and `(1ⁿ)` for `K` at `A=3`.
No block of dim ≥ 2 survives, for either object, at any `A`. Exactly the parity
prediction.

### Status of `conj-canonical-knot-id-sdp`

Not merely unsupported (the 2026-08-25 finding) — **its constraint set excludes
the object the substrate produces.** Three routes now agree from different
directions: volume matching (10³–10⁴ census manifolds fit equally well), closure
arity (`c_atom = A+1`, `c(K) = 2A+1` refute every named link), PSD feasibility
(a parity filter rejecting `K`, the nucleon and the trefoil while accepting the
unknot).

Machinery validated 4/4 against `binding-link-psd-feasibility-probe.witness.json`.

### Next — and what NOT to do

**No objective is proposed, deliberately.** Inventing one that happens to admit
`6_2`/`8_11`/`L6a4` would be the same fit in a new coordinate system. A
well-posed replacement needs *both*: a constraint set the canonical word
satisfies (PSD as stated is the wrong cone — it is a parity filter), and an
objective taking no `B_AME` input. My judgement on priority: the **constraint**
half first, since a wrong cone makes any objective meaningless, and because
`ρ_λ(σ) = {q₀, −1/q₀}` suggests the natural positivity notion here is on
`σ + σ⁻¹` or on even-length subwords, not on `σ` itself. That is a guess and
should be treated as one.

---

## CORRECTION + the real mechanism — 2026-08-31. It is the LP active set at `H_{3A}`, not PSD.

**Owner correction:** *"why PSD constraints??? we have SDP constraints on the
integer LP and THAT is supposed to determine which K is active for the knot
convolution... maybe a typo somewhere got us down the wrong rabbit hole?"* —
correct, and I withdraw the previous entry's conclusion.

**The naming collision is real.** `binding_k_solver.py` and
`binding_link_psd_feasibility_probe.py` route the reader to an `H_3` **PSD
feasibility check**; the corpus's actual selection machinery is the
**operator-selection LP with duals** (`nucleus_sdp_assembly.py`,
`nucleus_real_sdp.py`) at `H_{3A}`, where the deliverable is the **active set**.
Two programs, one word. Worth renaming.

Probe `computations/probes/operator_selection_active_set_probe.py` (5 assertions).

**At `H_3` the constraint has no bite.** Frobenius positivity holds for 100 % of
alphabet words to length 6, 99.4 % at nucleon length 11. So every bound atom
`A = 1..16` is stable with the **empty word**, every row strictly slack
(`min (Gx)ᵢ = 0.40..4.44`), `y* = 0`, **active set empty** — `nuclear_ilp.py`'s
search branch is dead code. *Not* literally vacuous though (I corrected my own
first draft): the **free** product violates, first at `O16`
(`min (Gx) = −0.618`), but is slack through `A = 12`. So the emptiness is not an
artifact of `build_atom_nf` pre-applying the inter-nucleon crossings, and where
the constraint does bite it is the free product that fails and the bound atom
that passes — right sign, far too high in `A`.

**At `H_{3A}` the same program works.** Non-empty active sets, `y₀* ≠ 0`, strong
duality:

| atom | `y₀*` | active blocks |
|---|---|---|
| D | −0.014434 | 7 (plus 3 negative-norm blocks) |
| T | +0.016550 | (6,3) (7,2) (8,1) (9) |
| ³He | +0.028787 | (6,3) (7,2) (8,1) (9) |
| ⁴He | +0.003966 | 6 |

### The blocker, and it is specific

**`T` and `³He` get IDENTICAL active blocks**, differing only in the scalar
`y₀*`. So the program cannot assign them different `K` — exactly Gap #2's need,
and exactly where the census route failed too. Cause, from the witnesses' own
`note`: **Phase B color-flavor constraints (LR branching
`H_{3A} ⊃ (H_3)^Z × (H_3)^N`) are not implemented**, and
`binding_cut_entropy_derived_weightings_probe.py` records that the **LR branching
data exists only for the deuteron**. Without it the solver sees `A = 3` and
nothing else.

Same gap at the base of the γγ chain: `sdp_gamma_gamma_to_qqbar.py` lays out the
recursion (`γγ→e⁺e⁻` `H_2`, `γγ→qq̄` `H_3`, inner Borromean, quark pairs, gluon
self-coupling, *"each level adds an LR-embedding step"*) and stops at the same
step — and says of its own base rung that *"11 is uniquely close to AME but other
budgets are PSD-feasible too — so the SDP is not strict enough"*. The proton's
crossing budget is picked by closeness to AME, one level below the knots.

### Next

**Withdrawn:** my previous "no objective exists". Wrong program.
**Correct statement:** the objective and duals exist and work at `H_{3A}`; what
is missing is the **LR branching constraint** that makes the program depend on
`(Z, N)` at all. That is a specific, buildable object — cross-level LR
consistency, data currently only at `A = 2` — and it is the single highest-value
next step for `K` via knot convolution. My judgement: build it at `A = 3` first,
where `T`/`³He` give an immediate falsifiable test (the active sets must
separate), rather than at the γγ base where there is no such discriminator.

---

## Phase B LR branching — built 2026-08-31, `A`-generic. Next blocker: the diagonal Gram.

Probe `computations/probes/phase_b_lr_branching_constraint_probe.py` (7 assertions).

**Built.** Restriction along `H_{3A} ⊃ (H_3)^{⊗A}` gives
`χ^λ(x) = Σ_{μ₁..μ_A} c^λ_{μ₁..μ_A} Π χ^{μᵢ}(xᵢ)`. Each nucleon's `H_3` block
character is LR-convolved into an `H_{3A}` profile — one
`get_lr_table(3(m−1), 3)` per rung — and becomes the LP demand
`u_demand = y_λ·χ^λ_free` against the cost `t_λ = y_λ·χ^λ_atom`. Cost carries the
bound atom, demand the free constituent product, so the program would price
exactly the gap: **the knot convolution read block by block.**

Validated two independent ways, exact at `A = 2,3,4` over all 11/30/77 blocks —
the induction identity, and the restriction identity
`dim S^λ = Σ c Π dim S^μ` (which validates the *character* formula, not just the
coefficients).

### Two defects found on the way

1. **`pyhecke.atom.nf_channel_exact` raised `NameError` on every call** —
   `_TR_M_FRAC` used in the body, defined and exported by `gram`, missing only
   from `atom.py`'s import line. **Fixed.**
2. **With that fixed it is still wrong**, so it is not used. Its `χ_std` matches
   the standard-block character under *no* normalisation (`σ₀`: 0.864044 here vs
   0.209060 direct vs 0.104530 direct/dim), and its 1-dim blocks sit at
   `q = 111/100`. Defect 1 is *why* defect 2 survived — dead code is never
   compared to anything. Flagged in place, **not repaired** (the right `χ_std`
   depends on which Wedderburn convention `W_STD` pairs with — a substrate
   decision). Profiles here use direct seminormal traces. **`χ^(2,1)` is
   negative for both nucleons where that function reports +0.78/+0.66, so
   anything downstream of it needs re-checking.**

### Result, and a correction to my own first reading

The demand **is** genuinely `(Z,N)`-dependent — that part works. But the LP's
duals do not see it. `nucleus_sdp_assembly` builds a **diagonal** Gram, and the
dual constraint `y₀·1 + Gᵀy = t` never mentions `u_demand`, so with `G` diagonal
and `y₀* = 0` it forces

    y*_λ = t_λ/G_λλ = χ^λ_atom / dim S^λ

exactly — measured, and **invariant under scaling `u_demand` by 7.3×**.

I first read the differing `y*` as Phase B separating the isotopes. **Withdrawn.**
Those prices belong to the cost vector, already `(Z,N)`-dependent through
`χ_atom`. Phase B dropped into this LP adds a determined primal `x = G⁻¹u` and a
derived `n_target`, and nothing else.

### General principle for `A > 3` (as asked)

- **One new table per rung**, `get_lr_table(3(A−1), 3)`: 35 / 203 / 806 / 2659 /
  7646 entries for `A = 2..6`, 0.54 s at `A = 6`. Tractable well past where cost
  data exists; the bottleneck will be `χ^λ_atom`, not the branching.
- **The demand is a function of `(Z,N)` alone, not nucleon ordering** — verified
  to `8.9e-15` over every permutation of `ppn`, `ppnn`, `pppn`, as it must be
  (Schur multiplication commutes). Real contrast with `build_atom_nf`, which
  fixes an interleaved ordering: any surviving ordering-dependence is a property
  of the **atom word**, not of the branching.
- **`A` enters only as recursion depth.** Nothing is special to `A = 3`.
- **Caveat:** convention D's two-row cap zeroes `y_λ` outside two-row `λ`, so the
  demand (all 30 blocks at `A=3`) is projected onto a 5-block subspace before the
  LP sees it. Second place `(Z,N)` signal is lost, after the diagonal Gram.

### Next

**Build the `H_{3A}` Frobenius Gram with its off-diagonal entries.** Against a
diagonal Gram no demand can do work — `Gx = u` has a unique solution, leaving
nothing to optimise, and the dual is pinned by `t` alone. This is well-posed: the
`H_3` Gram already exists in full in `pyhecke.gram` (6×6, with its documented
radical); what is missing is the `H_{3A}` analogue. My judgement on ordering:
the Gram first, then re-run Phase B against it — the branching constraint is
already built and validated, so that step is a re-run, not new construction.
Secondary, and cheap: audit consumers of `nf_channel_exact` now that it is
callable and known wrong.

---

## The `H_{3A}` Frobenius Gram with off-diagonals — built 2026-08-31. It changes nothing, and now I know why.

Probe `computations/probes/h3a_frobenius_gram_offdiagonal_probe.py` (6 assertions).

**Two corrections, the second withdrawing my own previous diagnosis.**

**1. In the block basis, diagonality is a THEOREM.** `cost_gram_from_arrays`
builds `diag(tr_M(P_λ))` over the *central* primitive idempotents, and
`P_λ P_μ = δ P_λ`, so `tr_M(P_λ P_μ) = δ·tr_M(P_λ)` identically. Nothing was
omitted and nothing can be added there, at any `A` or `q`. Off-diagonals exist
only away from the centre — in the NF (word) basis, where the `H_3` Gram is
already richly non-diagonal (max `|off| = 1.2726`, rank 5 of 6).

**2. So the object worth building** is the Gram on the constituent subalgebra
`(H_3)^{⊗A} ⊂ H_{3A}`, dim `6^A`, whose elements are not central — and which is
where the branching lives. Markov multiplicativity on disjoint strand blocks
verified (36 pairs at `H_6`, max rel err `1.1e-8` = the f64 `y_λ` precision),
giving `G^{(A)} = G^{⊗A}`, `t^{(A)} = TR_M^{⊗A}`:

| A | dim `6^A` | rank | `5^A` | radical | max off-diag |
|---|---|---|---|---|---|
| 1 | 6 | 5 | 5 | 1 | 1.272584 |
| 2 | 36 | 25 | 25 | 11 | 1.832269 |
| 3 | 216 | 125 | 125 | 91 | 2.638104 |
| 4 | 1296 | 625 | 625 | 671 | 3.798347 |

Rank `5^A` **exactly** — the documented 1-dim `H_3` radical tensors up, so the
radical is `6^A − 5^A` (91 of 216 at `A=3`).

### And it changes nothing — the real reason

The NF basis begins with the empty word, so `b₁ = 1` and `G_{1j} = t_j`:

    t = G e₁          the cost vector IS the first row of its own constraint matrix

So row 1 of `Gx ≥ u` reads `t·x ≥ u₁` — the objective bounded by one of its own
constraints. That row is always binding, the optimum is always `u₁`, the dual is
always `e₁`. Measured invariant under: equality **and** inequality forms;
realisable, non-realisable, and kernel-direction demands; identity kept **and**
dropped; and `T` vs `³He` (identical active sets *and* duals, only the objective
differing — and that difference is just `tr_M` of the free product).

Second, independent reason for the equality form: `u = Gx ∈ range(G) = ker(G)^⊥`
(`G` symmetric), and the dual feasible set is affine with direction `ker(G)`, so
`u·y` is **constant** on it. Verified to `1.2e-15`.

### What this unifies

    b₁ = 1  ⟹  t = G e₁  ⟹  row 1 of the constraint IS the objective

  (i) optimal value ≡ 0 — documented, the `u = 0` case
  (ii) `y₀* = 0` — documented
  (iii) demand cannot select under a **diagonal** Gram — my previous turn
  (iv) demand cannot select under **any** Gram — here

**(iii) was a special case. "The blocker is the diagonal Gram" is WITHDRAWN.**
Building the off-diagonals was worth doing to settle it, but they are not what
stands between Phase B and a selection; one line of linear algebra is.

### Next

**The demand has to enter the OBJECTIVE, not the constraints.** Minimising
`‖x − x_free‖²_G` over the feasible set is a QP whose solution genuinely depends
on `x_free` — the demand selects by projection rather than by pricing, and `G`'s
`5^A`-dimensional range is exactly where such a projection lands. That is the
closest thing to what Phase B was meant to do, and `G^{(A)}` is already built for
it. My judgement: try that before anything else, because it reuses everything and
is the only route measured here that is not already excluded. Dropping `tr_M` as
the objective is the fallback; note that dropping the *identity* is not enough —
measured, the LP then goes unbounded rather than selective.
