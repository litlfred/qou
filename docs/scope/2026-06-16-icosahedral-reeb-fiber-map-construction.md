# Scope — icosahedral A₅ Reeb fibre map: construction program for `conj:s5-so3-fiber-action`

**Date:** 2026-06-16
**Branch:** `claude/brave-hopper-ghhp9a`
**Status:** scope (multi-session, owner-gated) — NOT a probe to run blind
**Discipline:** formalize-first (the cheap combinatorial link is discharged first; the geometry is
the genuinely unbuilt object) + critical-distance (building the map ≠ closing the physics).

## Context

`conj:s5-so3-fiber-action` is the single open object the merged synthesis
([`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md))
reduces m_τ, GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K) to. Its open content is a **geometric
fibre map**: partition of 5 ↦ a specific A₅ rotation on Bring's quintic surface, compatible with
the $H_5(q)\to H_3(q)$ cross-algebra functor.

The 2026-06-13 functor-resolution doc proposed the *combinatorial* side is $\mathrm{Res}^{S_5}_{S_3}$.
Its branching backbone + the SO(3)↓A₅↪S₅ bridge are now **verified**
([`2026-06-16-s5so3-branching-backbone-verified.md`](../audits/2026-06-16-s5so3-branching-backbone-verified.md),
checker [`scripts/s5so3_branching_backbone_verify.py`](../audits/scripts/s5so3_branching_backbone_verify.py)).
The corpus also already realizes the **S₃ side geometrically** via the q-Reeb flow on the
exceptional divisor ($\mathcal{S}_p\cong\mathbb{CP}^1=S^2$, Hopf bundle $S^3\to S^2$, six $S_3$ knot
operators, $S_3$-Galois boundary monodromy;
[`exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md)).

**What is unbuilt:** that construction realizes only the cyclic $C_5$ (Lagrange-resolvent
diagonalization) on a *single*-point blow-up, and is a *3-strand* (S₃-target) construction. The
full icosahedral $A_5\cong I\subset\mathrm{SO}(3)$ action threading the Reeb flow — the actual
geometric fibre map — is not built. The classical backdrop is **Klein's icosahedral solution of the
quintic**: Bring's curve realizes the $A_5$ Galois action and $S^3/2I$ is the Poincaré homology
sphere, so the ingredients are known objects to be assembled on *this* divisor.

## Five-ingredient construction program

| # | Ingredient | Type | Status |
|---|---|---|---|
| 1 | **A₅-invariant orbit blow-up.** Blow up the icosahedral 12-vertex (or 20-/30-) A₅-orbit on the divisor sphere, NOT a single brane point — a single point's stabilizer kills most of $A_5$. The exceptional locus then carries $A_5$ as Klein's rotation action $I\subset\mathrm{SO}(3)$ on $\mathcal{S}_p\cong\mathbb{CP}^1$. | algebraic geometry | **unbuilt (crux)** |
| 2 | **2I-equivariant Reeb field.** Show the q-Reeb field $\xi_q$ ($\dot\psi=q$, `q-reeb-flow-on-coral-coords`) commutes with the binary icosahedral $2I\subset\mathrm{SU}(2)$ on the Hopf $S^3\to S^2$ (round Sasakian contact form is SU(2)-invariant ⟹ plausibly $2I$-invariant — must be proved for the q-deformed flow). | contact geometry | **unbuilt** |
| 3 | **The two bridging branchings.** $\mathrm{SO}(3)\downarrow A_5$ ($V_1\!\to\!T_1$, $V_2\!\to\!H$, $V_3\!\to\!T_2\oplus G$) and $S_5\downarrow A_5$ ($(3,1,1)\to T_1\oplus T_2$, $(3,2),(2,2,1)\to H$). | character theory | **VERIFIED** (this session) |
| 4 | **Commuting square (the functor).** A₅-equivariant Reeb operator on the ℓ-sector, restricted to the 3-tube via the **$123\!\to\!345$ embedding** (spacetime strands $\{1,2\}$ fixed — see embedding-independence note), equals the six $S_3$ knot operators with the $\mathrm{Res}^{S_5}_{S_3}$ multiplicities. | category theory | depends on 1,2 |
| 5 | **Markov-trace shift (the physics).** Evaluate the $H_3(q)$ trace shift between $E_{(3,1,1)}$ (ℓ=1) and $E_{(3,2)}$ (ℓ=2) projectors → correction factor $F(E,q_0)$ → test the 210 ppb muon gap. | compute (`pyhecke`) | depends on 4 |

## Why each ingredient is necessary (not optional)

- **1 (orbit, not point):** $A_5$ acts on Bring's $\Sigma_4$ by automorphisms, but blowing up a
  single brane point only retains that point's $A_5$-stabilizer. To keep the *full* icosahedral
  symmetry on the exceptional divisor, the blow-up center must be an $A_5$-invariant configuration —
  the icosahedron's 12-vertex / 20-face / 30-edge special orbits on $S^2$. This is the single most
  concrete "thing to build".
- **2 (equivariance):** "threading the Reeb flow with $A_5$" is meaningless unless the flow commutes
  with the group. The binary cover $2I$ acts on the total space $S^3$; equivariance of $\xi_q$ is the
  precise compatibility condition.
- **3 (bridge):** connects the geometry (spherical-harmonic level ℓ) to the combinatorics
  (already-verified $S_5\downarrow S_3$). **Discharged** — this was the cheap formalize-first step and
  it confirms the doc's bridge.
- **4 (square):** *is* the geometric realization — the conjecture asks exactly that the geometric map
  equals the combinatorial functor. The $123\!\to\!345$ embedding (not $123\!\to\!123$) is mandatory:
  the multiplicities are conjugation-invariant but the geometry is not, and the spacetime-frame
  strands must be held fixed.
- **5 (trace):** the only ingredient that touches the empirical target; everything above is
  structure.

## Risks / honest blockers (critical-distance)

- **Building 1–4 proves the geometric map EXISTS; it does NOT guarantee the physics.** The $S_3$-side
  lepton mass attempt already misses CODATA by 99% with a divergent tau
  ([`lepton-bring-surface-h3-3channel.md`](../../content/quantum-observable-universe/mass-theory/lepton-bring-surface-h3-3channel.md)),
  so a correct functor can still fail at ingredient 5.
- **C₅ → A₅ may not promote on a single divisor.** If the one-point blow-up's geometry resists the
  full icosahedral action (ingredient 1 fails), the Reeb-on-ED route describes the $S_3$ target only
  and is not the fibre map. Ingredient 1 is the go/no-go gate.
- **Multi-session, owner-gated.** Ingredients 1–2 are genuine algebraic/contact geometry, overlapping
  the merged GAP-A-4 chain. Coordinate before opening a probe branch; do not run a wide numerical
  search in place of the structural construction (formalize-first).

## Immediate next step (cheap, already done) and the gate

- ✅ **Ingredient 3** verified this session (extends the backbone checker).
- ⛔ **Gate = ingredient 1.** Before any compute, settle whether the icosahedral 12-vertex orbit
  blow-up retains $A_5$ as rotations on $\mathcal{S}_p$. This is a Klein-icosahedral / Bring-curve
  algebraic-geometry question, not a numerical probe.

## Cross-references

- [`2026-06-16-s5so3-branching-backbone-verified.md`](../audits/2026-06-16-s5so3-branching-backbone-verified.md) — backbone + bridge verification (ingredient 3)
- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](../audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md) — the candidate functor $\mathrm{Res}^{S_5}_{S_3}$
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — the synthesis (single open object)
- [`exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md) — the existing S₃-side Reeb construction
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — the keystone scaffold (open `partition_to_rotation`)
