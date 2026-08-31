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

---

## The positive sector breaks the degeneracy — 2026-08-31. The demand finally selects.

**Owner steer:** *"we can restrict away from negative because that is backwards
in computational time. We only want positive. negative is for entanglement (on
the full tower)."* Corpus framing, `jet_history_retention_probe.py` §Q3:
negatives enter only via `T_i⁻¹ = T_i − A`, so *"'negative = entanglement' is a
statement about NEGATIVE CROSSINGS (chirality)"*.

Probe `computations/probes/positive_sector_operator_selection_probe.py`
(5 assertions). **This resolves the obstruction the entry above established.**

There, `b₁ = 1` ⟹ `t = G e₁` ⟹ row 1 of `Gx ≥ u` *is* the objective, always
binding, dual always `e₁`, no demand could select. **Positivity breaks exactly
that** — with `x ≥ 0` the optimum can no longer reach the row-1 bound:

| nucleus | objective | row-1 bound `u₁` | `obj > u₁` |
|---|---|---|---|
| D | 0.429886 | 0.299015 | yes |
| T | 0.266264 | 0.142072 | yes |
| ³He | 0.298365 | 0.188179 | yes |
| ⁴He | 0.184802 | 0.089410 | yes |

so row 1 stops being binding and the program becomes a genuine **covering LP** —
`t = TR_M^{⊗A}` and `G` are both entrywise positive.

**The net constraint has to go, and the corpus already says why.** With
`1ᵀx = n_target` retained the positive sector is **infeasible** at every `A`.
Dropping it is justified, not convenient: `prop:operator-selection-lp` proves
`y₀* = 0` identically, so it carries no shadow price. It is exactly the
informationless constraint that blocks the positive sector.

    min t·x   s.t.   G x ≥ u_demand,   x ≥ 0

### It selects

| nucleus | A | dim | objective | \|support\| |
|---|---|---|---|---|
| D | 2 | 36 | 0.429886496 | 6 |
| T | 3 | 216 | 0.266264217 | 6 |
| ³He | 3 | 216 | 0.298365497 | 9 |
| ⁴He | 4 | 1296 | 0.184802398 | 24 |

**`T` and `³He` get different supports** — the separation Gap #2 needs, and the
first route in this line of work to produce it. All four objectives distinct.

**The optimal support lands on a sub-alphabet**, uniformly across all four:
only `σ₁`, `L₊`, `L₋` appear as tensor factors; `γ`, `σ₀`, `e⁻` never do. An
output of the program, not an input.

### ⚠ Tension flagged, not resolved

`x_free` is itself **not** in the positive sector — 108 of 216 coordinates
negative at `A = 3`, because the nucleon NF carries `σ₁⁻¹` letters. So positivity
is imposed on the *solution* while the *demand* `u = G x_free` comes from an
object that violates it. Either the constituent product legitimately carries
entanglement content and the program covers it, or **the nucleon should be
rebuilt in the positive sector** — which would move every number above. The
result depends on which.

### Next

My judgement, in order:

1. **Resolve the tension** — decide whether `build_atom_nf`'s nucleon belongs in
   the positive sector. This is the load-bearing question: every number above
   moves if it does, and it is a modelling decision rather than a computation.
2. **Test stability of the support under `q`.** The selection is only meaningful
   if the support is a structural feature and not a vertex that flips near `q₀`.
   Cheap, and it is the obvious way this result could be an artifact.
3. Only then ask whether the selected operator *is* `K`. Nothing so far shows it
   is — no `B_AME` enters anywhere in this route, which is the point, but it also
   means nothing yet ties the selection to binding.

---

## `x_free` settled, and the separation is structural in `q` — 2026-08-31

**Owner ruling on `x_free`.** Its 108-of-216 negative coordinates at `A = 3` are
**correct, not a defect**: `x_free` is the tensor product of the individual
nucleon NFs with **no inter-nucleon crossings** — the *free constituents* of the
atom, not a bound configuration — and the constituents are not asked to be in a
stable configuration. Positivity belongs to the **solution** only; the program
asks for the cheapest forward-time operator that *covers* an unbound,
entanglement-carrying constituent product. The tension flagged in the entry above
is resolved in favour of the construction as it stands. **No nucleon rebuild
needed** — this removes item 1 from that entry's next-list.

**`q`-stability** (probe `positive_sector_q_stability_probe.py`, 4 assertions).
`gram_matrix_mp`'s `q` override exists for exactly this test. Swept
`q = 1.02 … 1.50` at `A = 3`, rebuilding *everything* per `q` — Gram, Markov cost
`TR_M(q) = [1, z, z, z², z², hz²+z]`, and both nucleon NFs via `_hm_mp`. Nothing
carried from `q₀`.

| claim | strength |
|---|---|
| **`T` ≠ `³He` separation** | **fully robust** — different supports at all 13 `q` values, 1.02–1.50 |
| **sub-alphabet `{σ₁, L₊, L₋}`** | stable on `q ∈ [1.02, 1.26]`; breaks at 1.28 (`γ`, `σ₀`, `e⁻` enter). `q₀ = 1.10998` well inside |
| **degeneracy-breaking `obj > u₁`** | holds to ≈ 1.30, fails by 1.35 |
| **support SIZE** | **NOT robust** |

**A correction to my own previous entry.** The "6 and 9" support sizes are
**vertex counts that move with `q`**, not structural facts: `|supp T|` takes
`{4,5,6,7,8,9,12}` and `|supp He3|` takes `{5,7,8,9,10,11,12,13}` across the
sweep, with no monotone pattern. Do not quote them as invariants. What is
invariant is **that** the two differ, and **which letters** the support uses —
not how many words.

### Next

With `x_free` settled and stability measured, the remaining item from the
previous entry is the substantive one, and it is now the only one:

**Does the selected operator have anything to do with `K`?** Nothing so far ties
it to binding — no `B_AME` enters this route anywhere, which is what makes it
clean, but it also means the selection is currently a structural fact about the
Hecke data and not yet a physical claim. My judgement on how to attack it: the
sub-alphabet `{σ₁, L₊, L₋}` is the sharpest handle, because it is a *derived*
restriction on which operators can appear and it is `q`-stable. Ask what
`{σ₁, L₊, L₋}` means as a binding operator — `L₊`/`L₋` are the Hopf-link
elements of the NF basis — before asking whether the numbers match anything.

---

## Does the selected operator relate to `K`? No — structurally. 2026-08-31

Probe `computations/probes/k_versus_selected_operator_probe.py` (4 assertions).
Answered formally, with **no physical input anywhere**.

**`K` is exactly computable.** In the `H_3`-local model, with `P` the product of
the `A` nucleon NFs (no inter-nucleon crossings), `atom` the same with them, and
`M_P` left-multiplication by `P`: `K = M_P⁻¹ · atom`, and `M_P` is invertible at
every `A` tested. Electrons excluded (EM channel). **It validates itself at
`A = 2`**: `build_atom_nf` applies exactly one inter-nucleon letter after both
nucleon blocks, so `K` must be that letter — and the solve returns
`K(²H) = σ₀ + D_PN·1` to `1e-12`.

**`K` is never in the positive sector, and the interval is exact.** `K(²H)`'s
only negative coefficient is `γ`, and it **is** `D_PN`. So positivity of `K`
reduces to the sign of `D_PN`, settled in closed form — numerator factors as

    (q − 1)(q + 1)(q⁶ − 2q⁵ − 5q⁴ − q² + 2q − 1)

and the sextic has **exactly one real root above 1**,
`q_c = 3.458099300032797192042069`. So `D_PN < 0` **precisely on `1 < q < q_c`**,
which contains `q₀` by a factor of ~3.12 (`q₀/q_c = 0.32098`) and covers the
entire range swept in the stability probe.

> **Correction to my own first draft:** I wrote *"`D_PN < 0` for all `q > 1`"*.
> **False** — `q_c` is why. The correct statement is the interval.

At `A ≥ 3`, `K` has 3–4 negative components at `q₀` (D 1, T 3, ³He 3, ⁴He 3,
⁶Li 4).

**So the answer is no.** The LP's feasible set is `{x ≥ 0}`; `K` is not in it —
not "does not happen to be", **cannot be**. Nor is `x*` a rescaling: at `A = 2`
their shared support is `{γ, σ₀}` with ratios `−9.640158` and `0.290774`.

### The structural reading

`K` and `x*` are **complementary, not competing**, and the corpus's own
vocabulary says why. Negatives enter only via `T_i⁻¹ = T_i − A`
(`jet_history_retention_probe` §Q3) — the inverse-crossing sector. `K` is
*defined* as the free-to-bound map and on `1 < q < q_c` necessarily carries that
content; `x*` is *defined* by excluding it. The LP was never going to return `K`.
They answer different questions: `x*` is the cheapest forward-time operator whose
Frobenius profile covers the free constituent product; `K` is the actual map and
lives partly in the reverse-time sector.

**The `T`/`³He` separation `x*` produces stands as a structural fact about the
Hecke data — it is simply not a fact about `K`.**

### ⚠ Interpretation, explicitly not derived

The entire negative content of `K(²H)` is `D_PN`, the `p`-`n` interface offset —
and the deuteron is the `p`-`n` bound system. Nothing derives that
correspondence and no physical quantity enters the computation. Recorded so a
later reader finds it labelled rather than rediscovering it as a lead.

### Next

The `t7qv` line as posed is now answered end to end, so the choice is the owner's.
Three things are open, in my order:

1. **`q_c = 3.4580993…` is an unexplained structural constant.** It is the sign
   boundary of the entanglement content of the deuteron binding operator, it
   comes out of a sextic with small integer coefficients, and nothing in the
   corpus references it. Cheapest to look at and most likely to be real.
2. **Wire or discard the positive-sector LP.** It is a working `(Z,N)`-sensitive
   selector sitting outside production; leaving it unwired indefinitely is how
   the corpus accumulated the routes this whole arc has been auditing.
3. Audit consumers of `nf_channel_exact`, now known callable and wrong.

---

## All three follow-ups closed — 2026-08-31

### (1) `q_c` is explained, and my "unexplained constant" label is WITHDRAWN

Probe `qc_is_the_convexity_boundary_probe.py` (5 assertions, all exact/sympy).

Exactly `D_PN = −h(2 − δ)/4` (residual identically 0), so for `q > 1` where
`h > 0`, `D_PN < 0 ⟺ δ < 2` — and **the sextic in the `D_PN` numerator IS the
equation `δ = 2` rearranged**, verified identical symbolically.

`δ = 2` is where the colour-weighted `p`-`n` interface

    σ − h(½ − δ/4)·1  =  (½ + δ/4)·σ + (½ − δ/4)·σ⁻¹     [weights sum to 1]

has `σ⁻¹` weight **exactly zero** — it degenerates to a **pure `σ`**. Beyond
`q_c` the weight is negative and it stops being a convex combination.

| regime | `σ⁻¹` weight | `D_PN` |
|---|---|---|
| `1 < q < q_c` | > 0, convex average | < 0 |
| `q = q_c` | 0, pure `σ` | 0 |
| `q > q_c` | < 0, not a convex combination | > 0 |

So the earlier result — `K(²H)` outside the positive sector exactly on
`1 < q < q_c` — is a **tautology**: the binding operator carries inverse-crossing
content exactly while the `p`-`n` interface contains an inverse crossing. Right
outcome for something that looked mysterious.

At `q₀`: `δ = 0.0013757`, weights `0.500344 / 0.499656` — within **0.07 %** of
the symmetric average, three orders of magnitude below the boundary value 2.

What genuinely survives, and it is small: the sextic is **irreducible over ℚ**,
so `q_c` is algebraic of degree exactly 6; and nothing in the corpus records it.
Note it is a property of `PN_CONVENTION = "bring_color_weighted"` — under
`strict_averaged` the weights are ½/½ at every `q` and no boundary exists.

### (3) `nf_channel_exact` — audited, **zero consumers**

Every reference outside my own probes is namespace plumbing: import lists in
`pyhecke/__init__.py`, `hecke_core.py`, `hecke_core_legacy.py`,
`qou_mass/_internal/hecke_core.py`, plus `atom.py`'s own `__all__`. **No call
site anywhere.** Consistent with it having been dead code behind the `NameError`.
Nothing to repair beyond the flag already in `atom.py`; no downstream numbers are
affected.

### (2) The positive-sector LP — **probe only, deliberately**

The hazard you named is the *ambiguity*, not the un-wiredness, so the disposition
is now recorded in the probe itself rather than left floating.

- **Not `K`** — it lies outside the positive sector on `1 < q < q_c`, so this LP
  cannot return it. Complementary, not competing.
- **Not production** — `nucleus_real_sdp` runs a different program (per-block on
  the `H_{3A}` centre, diagonal Gram, net constraint retained). Neither is a
  drop-in for the other.
- **Not consumed** — no content block, derivation or witness reads its support
  or objective.

**Recommendation: do not wire, do not discard.** Wiring now adds a production
dependency with no consumer — the same accumulation problem pointing the other
way. It becomes right when something downstream actually needs a
`(Z,N)`-sensitive selector. That condition is written into the probe so the
decision is on the record.

### State of `t7qv`

The `K`-via-knot-convolution line is answered end to end and every follow-up it
generated is closed. Remaining open items on this bean are the older ones
(`A ≥ 5` geometric saturation; the octahedral arrangement), untouched by this arc.

---

## `A ≥ 5` saturation and the octahedral arrangement — 2026-08-31

Probe `computations/probes/geometric_saturation_and_labelling_probe.py`
(4 assertions). The two linked items split into questions with **different**
answers. `_deltahedron` in `gap2_irreducible_triple_bracket_probe` is hardcoded
as a *"3-D packing fact"* — asserted, not derived. Now derived.

### Derived

**1. The saturation law is Euler's formula.** All-triangular faces ⟹ `2E = 3F`,
so `V − E + F = 2` gives `E = 3V − 6`, no packing input. Every hardcoded count
**is** `3A − 6`:

| A | \|E\| hardcoded | `3A−6` | `C(A,2)` | saturates |
|---|---|---|---|---|
| 4 | 6 | 6 | 6 | no (complete) |
| 5 | 9 | 9 | 10 | yes |
| 6 | 12 | 12 | 15 | yes |
| 7 | 15 | 15 | 21 | yes |

**2. The `A ≤ 4` / `A ≥ 5` crossover is a quadratic root.**

    3A − 6 = A(A−1)/2  ⟺  A² − 7A + 12 = 0  ⟺  (A−3)(A−4) = 0

Simplex and deltahedron agree **exactly at `A = 3, 4`**, strictly apart for
`A ≥ 5`. The boundary stated as a modelling choice is a root pair.

**3. The octahedron is forced at `A = 6`.** `E = 12` on 6 vertices forces degree
sum 24, i.e. 4-regularity — and there are **15 labelled but exactly one
isomorphism class** of 4-regular graph on 6 vertices, which is the corpus's.
(Complement of a 4-regular graph on 6 vertices is a perfect matching; all such
are isomorphic.) **"Deriving the octahedral arrangement" is done.**

### Not derived — and worse than this bean recorded

The arrangement fixes the *graph*, not which vertices are protons. `⁶Li`'s 20
labellings fall into two classes:

| class | count | B | vs AME |
|---|---|---|---|
| `(8,8,0)` | 12 (60 %) | 41.590 | **+29.99 %** |
| `(6,6,0)` | 8 (40 %) | 31.193 | **−2.50 %** |

reproducing this bean's two figures exactly. **The obvious extremal principle —
a bound state maximises its binding contacts — selects `(8,8,0)`, the +29.99 %
one.** So the favourable −2.50 % is the *minimum*-mixed class: a pick **against**
the only principle available, not merely a member-pick. That is stronger than
what this bean said, and it **closes "derive the arrangement" as a route to
rescuing −2.50 %**.

Geometrically the min-mixed class is protons on one face, neutrons on the
opposite — maximal *like*-clustering. Whether that is motivated is a modelling
question; it is certainly not a binding-maximisation.

Scale elsewhere: `⁷Li` spans `M₂ = 7…10` across its 35 labellings — a 43 %
spread in the leading term with nothing choosing.

### Scope

§§1–3 are conditional on the **convex-deltahedron** hypothesis — the corpus's
modelling choice, not derived. Two cited consequences (Freudenthal–van der
Waerden): convex deltahedra exist only for `A ∈ {4,5,6,7,8,9,10,12}`, so there is
**no `A = 11` member** and the model has a hole no labelling argument can fill;
and max-contact packings and convex deltahedra are not the same family above
`A = 9`, so the terms should not be used interchangeably there. Within
`4 ≤ A ≤ 7`, where the corpus uses it, they agree.

### Next

The honest state of this bean's `A ≥ 5` line: the geometry is settled, and the
remaining freedom is entirely in the **labelling**, where the only available
principle points away from the favourable number. My judgement on what is worth
doing, and it is short:

1. **Retire the `−2.50 %` figure** wherever it is quoted, or re-label it as
   min-mixed-selected. It now has a specific defect — chosen against the only
   extremal principle — rather than a vague one.
2. If the labelling is to be derived, it needs a principle *other* than contact
   maximisation. Isospin/Pauli like-clustering is the obvious candidate and would
   select the favourable class, but nothing in the corpus currently supplies it,
   and inventing it to reach a known number is the failure mode this arc has been
   auditing throughout.

## 2026-08-31 — the silver coincidence is real, and it is the Plancherel functional

Owner: *"this is VERY old and needs re-examination, it is pre convention D"*
and *"isn't the LP dual shadow realizable as a representation?"* Both land.
`computations/probes/metallic_silver_coincidence_weighting_probe.py`, 6/6.

**My earlier negative was about the wrong object and I withdraw its framing.**

1. **PR #1999's `metallic_q_illustration.py` fails three checks under D.**
   Stale `q_0` (`1.1099785955541805` vs `1.1099785827513808`, off `1.3e-8`);
   `chi^(2,1)(sigma_1 sigma_2) = h^2-1` is wrong — convention D gives the
   constant `-1`, verified against the explicit 2x2 rep at four `q`; and it
   plots bare `chi^lambda` while its docstring claims weighted
   `y_lambda chi^lambda`. Its own `h^2-1` flips sign at `h = 1`, the golden
   rung, contradicting its own "no sign flips at metallic ratios". The
   corroboration `metallic_ladder_regime_test_probe.py` drew from it is
   **withdrawn**; that probe's own measurements stand.

2. **Under D only two blocks are live.** `y_alt = 0` identically. In `h`:
   `y_sym = (h^2+2)/(h^2+4)`, `y_std = 1/(h^2+4) = 1/[2]_q^2`, exact.

3. **THE RESULT.** Under the q-Plancherel weighting
   `W_lambda = d_q^2 / sum d_q^2`,

       T(sigma) = (h/2) * T(gamma)      identically, at every strand count n,

   from three facts the corpus already holds: `W_lambda = W_lambda'` (hook
   multisets are transpose-invariant; checked n=2..5), the transpose-pair
   character sum `chi^lambda(sigma) + chi^lambda'(sigma) = dim(lambda) h`
   (`GaloisPairCharacterSum` in `MetallicLPIdentities.lean`), and
   `chi^lambda(gamma) = dim(lambda)`. Hence `T(gamma) = T(sigma)` iff `h = 2`
   iff `q = delta_silver`, **for every n**.

   That **generalises the sorry-free Lean `silver_lp_coincidence` (PR #2047)**
   from `n = 2` to all `n`. Its cost vector `(2(q+1/q), q^2-q^-2)` is exactly
   `2[2]_q * (T(gamma), T(sigma))`, so the theorem is that identity's `n = 2`
   instance. Verified outright at n=2 and n=3; the n=3 coincidence polynomial
   factors as `(q^2-2q-1)(q^4+3q^2+1)` — the silver minimal polynomial appears
   as an explicit factor.

4. **Which answers the owner's second point.** `T(sigma) = (h/2) T(gamma)` is
   one identity that is simultaneously an optimisation fact (two LP cost
   coefficients coincide) and a representation fact (the transpose-pair
   character sum). My split between a "representation-theoretic regime" and
   "an optimisation one" is **withdrawn** — the dual *is* the representation.

5. **Why my H_3/H_9 sweep saw nothing.** Convention D's Markov trace is not
   Plancherel-weighted: `T(sigma)/T(gamma) = z = q^2/[2]_q`, not `h/2`. Its
   coincidence moves off silver to the **supergolden ratio** `q^3 = q^2+1`,
   `q = 1.4655712318767680`, `h = 0.783243`; the only other Markov locus is
   `q^5+q^4-2q^2-q-1 = 0`, `q = 1.2414315`, `h = 0.435910`. Neither metallic.
   So the ladder is a feature of the Plancherel functional, and a metallic
   result cannot be moved into the atom LP without first settling which
   functional the physics extremises. **That is now the open question.**

6. **What IS refuted.** `SDPDegeneracyDetectsMetallic`'s `S(n) ⊆ {delta_1..
   delta_n}` fails at n=3 in both weightings: Plancherel `S(3)` also contains
   `q = 2.8022805603737193` (`h = 2.44543`, between silver and bronze); Markov
   `S(3)` is the two non-metallic roots above. Silver being *in* `S(n)` is now
   a theorem; `S(n)` being *inside* the ladder is false. The conjecture should
   be weakened to the direction that holds.

## 2026-08-31 — lead: the atom LP is an n-fold integer program

From the owner's paper drop (`5bbd4b33`), triaged not yet built. De Loera,
Hemmecke, Onn, Weismantel, **N-Fold Integer Programming** (`math/0605242`).
An *n-fold IP* has constraint matrix `A^(n) = (1_n ⊗ I_q) ⊕ (I_n ⊗ A)`: `n`
independent copies of a fixed block `A x_k = b_k`, coupled by one global row
block `sum_k x_k = b_0`. Their words: the programs are almost separable, *"the
constraint sum x_k = b_0 **binds** these programs together."*

That is the atom, exactly: `x_k` = nucleon `k`'s NF occupation (`q = 6`), `A
x_k = b_k` the per-nucleon Hecke constraint, `sum_k x_k = b_0` the atom's
conserved totals (baryon number, charge, closure arity `c_atom = 2A - #odd`).
Two consequences worth testing:

- **The cost becomes additive.** `sum_k c_k x_k`, not `t^{⊗A} · x`. Binding is
  then `[sum_k min per-nucleon] - [min of the coupled program]` — the duality
  gap contributed by the coupling block alone, a difference of two comparable
  quantities in the same units. Our current Kronecker formulation takes a
  difference of two products, which is where the `4He` L2 miss (8 meV wanted
  out of 28.3 MeV, `2.5e9x` — bean `qou-1nvh`) plausibly gets destroyed.
- **Theorem 1.1: poly-time in `n` for fixed `A`.** The `6^A` blowup goes away,
  so heavy `A` becomes computable; and their Graver bases *stabilise* in `n`,
  giving an `n`-independent set of augmentation directions — which is a direct
  handle on the selection question `t = G e_1` left open.

Runners-up from the same drop, not ingested: Bödi–Herr–Joswig *Algorithms for
Highly Symmetric Linear and Integer Programs* (`1012.4941`) — reduce a
symmetric LP via linear representations of the symmetry group, i.e. onto
isotypic components; and van der Hulst, *Folding Mixed-Integer LPs and
Reflection Symmetries* (`2603.12136`). Also `2203.06568` (SDP bounds via a
split Terwilliger algebra) as a method template for block-diagonalising an SDP
by a centraliser algebra's Wedderburn decomposition.

## 2026-08-31 — the atom LP as an n-fold IP: binding is the aggregation gap, and it is ZERO at q_0

`computations/probes/nfold_ip_coupling_duality_gap_probe.py`, 6/6.

**The reformulation, and it is clean.** Take the corpus's own positive-sector
LP unchanged, `phi(v) = min{t.x : Gx >= Gv, x >= 0}`. Then

    free(Z,N) = Z phi(v_p) + N phi(v_n)     -- n separate local blocks
    atom(Z,N) = min{sum_k t.x_k : sum_k G x_k >= sum_k G v_k, x >= 0}
                                            -- the SAME constraints aggregated
    E_bind    = free - atom

Aggregation is a relaxation, so `E_bind >= 0` **structurally** — `x_p + x_n` is
aggregate-feasible with cost exactly `free`, which is the whole proof of the
sign. Mass defect out of a relaxation, nothing fitted.

**Two wins.** (1) The `6^A` blowup collapses: substituting `X = sum_k x_k` the
atom program is a single **6-variable** LP, `atom = phi(Z v_p + N v_n)`, with
all `A`-dependence in the RHS. Checked against the explicit `6A`-variable block
LP at A = 2,3,4, agreeing to 1e-12. (2) Binding becomes the **cone-crossing
defect** of the LP value function: `phi` is positively homogeneous and convex
hence subadditive, so `E_bind` is exactly its failure to be additive — zero iff
`v_p` and `v_n` lie in one linearity cone. "What binds a nucleus" becomes a
finite decidable question.

**The answer at q_0 is zero.** Supports are `(2,3,4)` for p and `(2,3)` for n —
**nested**, so one cone, `phi` linear along the ray. `E_bind = 0` to machine
epsilon for 2H, 3H, 3He, 4He, 6Li, 12C, 16O and pure-species systems; largest
residual 5.3e-15 on values of order 10. An exact algebraic zero, not a small
binding. **This route does not repair the 4He L2 miss (`qou-1nvh`).**

**But the mechanism is real and windowed.** Sweeping h from 0.05 to 4.2 the gap
is zero everywhere except `h in (0.47718474189158, 0.56984029056366)`, i.e.
`q in (1.26666, 1.32472)`, peak 0.0687 at h = 0.534. q_0 has h = 0.20906,
**56.2% below the lower edge**. Verified not to be a solver artefact: three LP
methods agree to 0, both separate problems carry valid dual certificates
(`y >= 0`, `G^T y <= t`, strong duality), and an explicit cheaper feasible
aggregate point is exhibited (2.1021 vs 2.1717).

**Inside the window the law is exact:** `E_bind = min(Z,N) * kappa` over
`0 <= Z,N <= 4`, with kappa = 0.069590 (Z >= N) or 0.070191 (Z < N), a 0.86%
split; and `E_bind = 0` identically whenever Z = 0 or N = 0. So **no binding
without both species** — no dineutron, no diproton — structurally, not fitted.
Since `min(Z,N) = (A - |N-Z|)/2` this is a volume term and an asymmetry term
locked at coefficient ratio 1. It is **not** the SEMF, whose asymmetry term
goes as `(N-Z)^2/A` with an independent coefficient; the agreement is
qualitative only.

**What it leaves open, and it is the same thing twice now.** The n-fold form
requires an ADDITIVE cost `sum_k t.x_k` where the corpus's atom construction
uses the multiplicative `t^(x)A . x`. Different functionals, not two spellings
— the trace *is* multiplicative on disjoint blocks, but `log(t.x)` is not
linear in x, so no change of variables converts one program into the other.
Together with the previous turn's finding that the metallic structure lives in
the Plancherel weighting and not the Markov one, **"which functional is the
physics supposed to extremise" is now blocking from two independent
directions.** That is the next thing to settle.

**Boundary of what was built:** this is the LP relaxation. `scipy.linprog`
throughout, continuous. The n-fold *aggregation* is fully exercised, but
Theorem 1.1's actual content — poly-time solvability of the INTEGER program via
Graver-basis stabilisation — is not built. The relaxation collapsing to 6
variables makes it trivially tractable, so the whole complexity question lives
in the integrality that is missing.

## 2026-08-31 — LEAD: n-fold IP and the q-P != NP work

Requested connection between the above and
`content/quantum-observable-universe/appendix-surreals/p-vs-np-surreal-bound.md`
(+ `p-vs-np-conjecture.ts`). Recorded as a lead; nothing built.

That bound argues: a q-substrate computation accesses the Reeb-period budget
`Omega_q ~ eps^-1`, a classical step the mass-gap budget `Delta_q ~ eps^3`;
classical simulation of a q-algorithm needs `2^n delta_n^2 Omega_q` against a
budget `2^n Delta_q`, so `ordw = 1 > -3` and the simulation exceeds budget by a
full omega-order; `P != NP` then follows under the standard-part map,
**conditional** on non-compressibility of `BQP_q -> P` as `eps -> 0`.

Three points of contact, in increasing order of how much they'd actually cost
to test:

1. **N-fold IP is a rare variable-dimension IP that is in P.** General IP is
   NP-hard; IP in *fixed* dimension is in P (Lenstra). N-fold IP is neither —
   dimension `nq` is variable — yet poly-time, and the tractability comes from
   the **block structure**, not from small dimension. So if the atom program is
   genuinely n-fold, computing nuclear binding is in **P in the nucleon count**.

2. **Which is a scope statement about the squeeze, either way.** The surreal
   bound is about problems where a q-substrate buys a `2^n` Reeb speed-up that
   the standard part destroys. If binding is an n-fold IP it needs no
   exponential budget at all, so it is *not* an instance where the squeeze
   applies — the substrate's own dynamics would not exhibit the hardness the
   conjecture trades on. Either that scope limit should be stated in
   `p-vs-np-conjecture.ts`, or the atom program is NOT genuinely n-fold, and
   then the exponential is real and "binding is NP-hard to compute" becomes a
   positive, falsifiable prediction. Both branches are worth having written
   down; right now neither is.

3. **The sharpest technical link: Graver stabilisation <-> tower stabilisation.**
   De Loera et al. prove the Graver basis of `A^(n)` stabilises in `n` (their
   Section 4, citing [13,19]) — the augmentation directions become
   `n`-independent past a threshold. The corpus's Hecke tower has its own
   stabilisation: `h3a_frobenius_gram_offdiagonal_probe` verified the Markov
   trace is multiplicative on disjoint strand blocks, so `G^(A) = G^(x)A` and
   `t^(A) = t^(x)A` exactly. **Conjecture worth opening:** the Graver basis of
   the atom program stabilises *because* the trace factorises on blocks — i.e.
   the augmentation directions are the tower-stable objects the corpus already
   has. If that holds, the substrate's algebraic structure is precisely what
   puts its own dynamics in P, and the `eps^-1` Reeb budget is not needed for
   them. Testable at small A by computing the Graver basis directly (4ti2 /
   `zsolve`), which is also exactly the missing integer half of the probe above
   — so points 1-3 and the probe's own gap close with the same piece of work.

## 2026-08-31 — SETTLED: the substrate extremises the Markov trace; the zero is critical

`computations/probes/which_functional_the_substrate_extremises_probe.py`, 6/6.

**Axis 1 settled three ways over — Markov, not Plancherel.** Three properties
the corpus already *demands* each reject the q-Plancherel weighting:

1. **Not a Markov trace.** `tr(x.T_n)/tr(x)` is `h/2` on gamma but
   `-2q^3/(q^6+2q^4-2q^2-1)` on `s0` — not even constant, so no Markov
   parameter exists. Markov gives `z` on both. The Markov property is what
   makes the trace a link invariant and what the whole closure/arity apparatus
   rests on (`c_free = 2A`, `c_atom = A+1`, Lean `ClassicalTraceFloor`).
2. **Does not annihilate the q-antisymmetriser.** `W_alt = q^2/D != 0` against
   `y_alt = 0`. Convention D's defining fact is the singular Gram whose radical
   IS the antisymmetriser; a Plancherel Gram is nonsingular, i.e. a different
   cone from the one every SDP here is posed over.
3. **Not multiplicative on disjoint strand blocks.** Re-running
   `h3a_frobenius_gram_offdiagonal_probe`'s own H_6 test with Plancherel
   weights: **36 of 36 pairs fail**, worst rel err 10.9. Not a normalisation —
   `gamma(x)gamma`, `gamma(x)s0`, `s0(x)gamma` all miss by +4.0346 but `s0(x)s0`
   misses by **-2.0556, sign flipped**. This is the property that gives
   `t^(A) = t^(x)A`, i.e. the entire atom construction.

**Consequence: the metallic ladder is retired as a physical mechanism.** The
silver coincidence and the Lean `silver_lp_coincidence` it generalises stay true
theorems — about a functional that is not a link invariant, has the wrong cone,
and cannot build an atom. A re-scoping, not a refutation; if a legitimate role
for Plancherel ever appears, the metallic results return with it.

**Axis 2 was never a fork, and I withdraw last turn's "blocking from two
directions".** Additive and multiplicative give *exactly* the same answer: zero.
Verified at full `6^A` with no collapse — 36, 216, 216, 1296 variables for 2H,
3H, 3He, 4He — max |gap| 2.2e-16. The tensor of the per-nucleon optima is
already globally optimal for the coupled program.

**The mechanism, and it is one fact.** At q_0 the dual optimum is **rank one and
shared by both nucleons**: `y*_p = y*_n = 0.54312042 e_2`, a single active row
(index 2, `sigma_1`). So `phi(v) = 0.54312042 (Gv)_2` is **exactly linear in v**
— residual exactly 0.0 on `v_p`, `v_n`, `v_p+v_n`, `2v_p+2v_n`. A linear value
function is exactly additive, so the gap vanishes identically for every (Z,N)
and either cost convention. This subsumes the "nested supports" observation of
the previous turn and is `t = G e_1` biting again: `y = e_1` is dual-feasible
with all six dual constraints tight, a maximally degenerate vertex.

**And the zero is CRITICAL, not structural.** The geometry is perfectly capable
of binding: **86 of 300** random nonnegative costs open a strictly positive gap
(worst 1.65%). What is special is the Markov cost. Along directions that do
open a gap, `gap/eps` is **constant over six decades** (1e-1..1e-6; constants
0.0309, 0.0289, 0.0174, each flat to < 5e-8), so the gap grows exactly linearly
from zero: **the Markov cost lies ON the boundary of the no-gap region**, and
since only 5 of 24 directions cross, the boundary is a face rather than a point.

**Self-correction.** A first pass detected gap-opening with `abs(gap) > 1e-9`
and reported a knife-edge radius of 3e-8. Those were *negative* gaps —
structurally impossible, since aggregation is a relaxation — i.e. solver noise.
Every measurement in the committed probe is sign-aware with a relative
threshold, zero spurious negatives are observed, and the boundary claim rests
on the linear scaling rather than on any radius.

**What this does to 1PPQ.** The question is no longer "which functional". It is
**why the substrate sits exactly on that critical face**, and whether physical
binding is the linear response `C.eps` to whatever breaks the degeneracy — with
`C ~ 0.017-0.031` already measured. That is the next thing to build.

## 2026-08-31 — the question dissolves: binding is a p/n dual-vertex hysteresis

`computations/probes/binding_window_is_a_dual_vertex_hysteresis_probe.py`, 6/6.

**I withdraw my own framing.** I asked "why does the substrate sit exactly on
that critical face". That conflated two boundaries, and separated they answer
themselves.

**Cost space: the face is occupied at EVERY q, by an identity.** The dual vertex
`lam e_2` has `lam = min_i t_i/G[i,2]`, and that argmin is **3-fold tied** on
`{s1, L+, L-}`. The `2<->3` leg is the identity

    G[3,2] = z * G[2,2]        residual 1.2e-31 at 40 dps, four values of q

which is just the Markov property `tr(x T_n) = z tr(x)` written in the Gram; the
`3<->4` leg is the `L+/L-` symmetry. Sweeping h from 0.05 to 2.5 the argmin set
is `{2,3,4}` at every point, inside the binding window and out. **So there is no
fine-tuning of q_0 in it at all** — the substrate lies on that face for the same
reason the trace is a link invariant.

**q space: what actually controls binding is a hysteresis.** Two competing dual
vertices: `e_0` (all six dual rows tight — this is what `t = G e_1` supplies)
and `lam e_2` (three tight rows, the Markov tie). Each nucleon switches from
`lam e_2` to `e_0` at its **own** h:

    proton  at h = 0.47718474189158
    neutron at h = 0.56984033

and the binding window is **exactly** the interval between — matching to 4e-15
and 4.4e-8 the window edges bisected independently *from the gap itself* in
`nfold_ip_coupling_duality_gap_probe`. Two different computations (dual support
here, primal gap there) landing on the same two numbers. Verified at 7 sampled
h: **the gap is nonzero exactly when the two nucleons do not share a vertex.**

**One sentence: binding is the split between the proton's and the neutron's
dual-vertex transition points.**

**q_0 is nowhere near it.** `h(q_0) = 0.20906` against the first transition at
`0.47718` — factor **2.283**. Margins by which each nucleon prefers `lam e_2`:
proton `+0.0647 (+9.33%)`, neutron `+0.1442 (+23.29%)`. Both comfortably
positive, proton nearer (which is why it switches first). The zero is robust,
not marginal.

**Correction carried into the earlier probes.** `t = G e_1` is **neither
necessary nor sufficient** for the no-gap property, so my reading of it as the
blanket obstruction was too strong. Rows 1, 3, 5 of G used as costs open gaps
(9.5e-3, 2.1e-2, 5.2e-3), and **150 of 150** random costs `G w`, `w >= 0`, open
gaps. Its real role is narrower: it supplies `e_0` as the second, maximally
degenerate dual vertex. `which_functional_the_substrate_extremises_probe.py` has
been amended with a pointer.

**Where this leaves 1PPQ.** The zero at q_0 is now fully explained and robust:
not fine-tuning, not a cost artefact, not repairable by nudging q. Binding needs
the two nucleons to straddle a transition, and at q_0 they sit on the same side
by 9% and 23%. Since the transition points are properties of `v_p` and `v_n` —
of the **nucleon chains**, not of q — the problem relocates cleanly: either
something must separate the proton and neutron objectives far more than the
present flavour split does, or the binding constraint is not in
`{Gx >= Gv, x >= 0}` at all. Both are well-posed; neither is a search over cost
functionals, and that search is now closed.
