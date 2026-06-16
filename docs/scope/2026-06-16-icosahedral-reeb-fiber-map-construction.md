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
| 1 | **Identify the divisor $\mathbb{CP}^1$ with Klein's icosahedral $\mathbb{P}^1$ via the spin lift.** Show the $S_5=\mathrm{Aut}(\Sigma_4)$ action restricts on $A_5$ to the **binary icosahedral $2I\subset\mathrm{SU}(2)_S$** on the spin fibre $\mathbb{C}^2_{\mathrm{spin}}$, so its projectivization $\mathbb{P}(\mathbb{C}^2)=\mathbb{CP}^1$ is Klein's icosahedral line ($A_5\cong I\subset\mathrm{PSL}_2$, Möbius rotations). See §"Ingredient 1 — findings" — the earlier "blow up the 12-vertex orbit" framing was **wrong** (gives 12 permuted lines / the E₈ tree, not one icosahedral $\mathbb{P}^1$). | spin structure / rep theory | **unbuilt (crux)** |
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

## Ingredient 1 — findings (2026-06-16): the $\mathbb{CP}^1$ is the spin fibre, action lifts to $2I$

A first pass at the gate (corpus + structural reasoning, anchored in the verifier's
INGREDIENT-1 block) sharpened ingredient 1 and **corrected two framing errors**:

1. **The $\mathbb{CP}^1$ is the spin / state-bundle fibre, NOT a blow-up of the Bring curve.**
   [`fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md)
   establishes $\Sigma_4$ is a **genus-4 curve** (complex dim 1), $\mathrm{Aut}=S_5$. You cannot get a
   $\mathbb{CP}^1$ exceptional divisor by blowing up a point on a curve ($\mathbb{P}^{1-1}=\mathbb{P}^0=$
   a point). The $\mathbb{CP}^1$ is the **state-bundle fibre** $\mathcal{S}=P\times_G\mathbb{CP}^1$
   (QOU archimedean tuple, CLAUDE.md §7) $=\mathbb{P}(\mathbb{C}^2_{\mathrm{spin}})$, on which
   $\mathrm{SU}(2)_S$ spin acts. The `exceptional-divisor-reeb-intro` "blow up a point $p\to\mathbb{CP}^1$"
   must be read as the projectivized spin fibre over $p$. This locates *where* the icosahedral $S^2$ lives.

2. **"Blow up the 12-vertex orbit" (my earlier ingredient-1 text) was geometrically wrong.** Blowing up a
   12-point $A_5$-orbit gives 12 permuted $\mathbb{P}^1$'s; resolving the quotient singularity
   $\mathbb{C}^2/2I$ gives the **E₈ tree of 8 $\mathbb{P}^1$'s** (McKay). Neither is a single
   $\mathbb{P}^1$ with icosahedral *rotation*. The correct target is **Klein's icosahedral $\mathbb{P}^1$**
   — $A_5\cong I\subset\mathrm{PSL}_2(\mathbb{C})$ acting by Möbius rotations, **intrinsic**, no orbit
   blow-up.

3. **The action must go through the BINARY icosahedral $2I$ (verified anchor).** $A_5$ has irrep dims
   $\{1,3,3,4,5\}$ ($\sum d^2=60$) — **no faithful 2-dim rep**, so $A_5$ cannot act on the spinor
   $\mathbb{C}^2$. The rotation $I\subset\mathrm{SO}(3)=\mathrm{PSU}(2)$ on $S^2=\mathbb{P}^1$ lifts to the
   **binary icosahedral $2I\subset\mathrm{SU}(2)$** (order 120, dims $\{1,2,2,3,3,4,4,5,6\}$, $\sum d^2=120$,
   the E₈ McKay irreps) on $\mathbb{C}^2$. So the icosahedral fibre action **is** the spin $\mathrm{SU}(2)_S$
   lift of [`spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md)
   — the same lift, not two. Globally $S^3/2I=$ the Poincaré homology sphere $=$ link of the E₈ singularity,
   constraining the Reeb/Hopf-bundle topology.

4. **Consistent with the standing 3-vs-5-strand caution.** `spin-from-so3-fiber.md` and the 2026-06-01
   audit already flag that the 5-strand icosahedral side and the 3-strand $H_3$ Borromean side are
   "different representation rings with no canonical map." The verified $\mathrm{Res}^{S_5}_{S_3}$ backbone
   + bridge **is** the proposed canonical map (restriction); it addresses the caution but stays a candidate
   until ingredient 4 (the commuting square) is built. No contradiction.

**Refined gate (go/no-go for ingredient 1):** does the geometric $S_5=\mathrm{Aut}(\Sigma_4)$ action **lift to
$2I\subset\mathrm{SU}(2)_S$** on the spin/state-bundle fibre over the brane point, so that $A_5\subset S_5$ acts
as $I\subset\mathrm{SO}(3)$ on the $\mathbb{CP}^1$ fibre? This is a **spin-structure / representation-lift**
question (does the automorphism lift to the binary cover on the spin bundle), not an orbit blow-up. That is the
genuinely unbuilt object.

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
- ⛔ **Gate = ingredient 1, refined.** Before any compute, settle whether the geometric
  $S_5=\mathrm{Aut}(\Sigma_4)$ action **lifts to the binary icosahedral $2I\subset\mathrm{SU}(2)_S$** on the
  spin/state-bundle $\mathbb{CP}^1$ fibre (so $A_5$ acts as $I\subset\mathrm{SO}(3)$ by Möbius rotations). This
  is a spin-structure / representation-lift question (NOT an orbit blow-up — see §"Ingredient 1 — findings");
  it coincides with the $\mathrm{SU}(2)_S$ spin lift of `spin-from-so3-fiber.md`.

## Cross-references

- [`2026-06-16-s5so3-branching-backbone-verified.md`](../audits/2026-06-16-s5so3-branching-backbone-verified.md) — backbone + bridge verification (ingredient 3)
- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](../audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md) — the candidate functor $\mathrm{Res}^{S_5}_{S_3}$
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — the synthesis (single open object)
- [`exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md) — the existing S₃-side Reeb construction
- [`spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md) — `conj:s5-so3-fiber-action` spin SU(2)_S lift (= ingredient 1's $2I$ lift)
- [`fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) — $\Sigma_4$ is a genus-4 *curve*, Aut $=S_5$ (the dimension fact behind finding 1)
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — the keystone scaffold (open `partition_to_rotation`)
