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
| 1 | **Identify the divisor $\mathbb{CP}^1$ with Klein's icosahedral $\mathbb{P}^1$ via the spin lift.** Show the $S_5=\mathrm{Aut}(\Sigma_4)$ action restricts on $A_5$ to the **binary icosahedral $2I\subset\mathrm{SU}(2)_S$** on the spin fibre $\mathbb{C}^2_{\mathrm{spin}}$, so $\mathbb{P}(\mathbb{C}^2)=\mathbb{CP}^1$ is Klein's icosahedral line ($A_5\cong I$, Möbius rotations). | spin structure / rep theory | **SETTLED** — existence (§"Gate resolution") + identification as icosahedral $T_1$ (§"Residual-2 RESOLVED") |
| 2 | **2I-equivariant Reeb field.** Show the q-Reeb field $\xi_q$ ($\dot\psi=q$, `q-reeb-flow-on-coral-coords`) commutes with the binary icosahedral $2I\subset\mathrm{SU}(2)$ on the Hopf $S^3\to S^2$. | contact geometry | **inherits the precedent** — the existing $S_3\!\to\!\mathrm{Dic}_3$ Reeb field is already binary-equivariant; $2I$ is the analogue |
| 3 | **The two bridging branchings.** $\mathrm{SO}(3)\downarrow A_5$ ($V_1\!\to\!T_1$, $V_2\!\to\!H$, $V_3\!\to\!T_2\oplus G$) and $S_5\downarrow A_5$ ($(3,1,1)\to T_1\oplus T_2$, $(3,2),(2,2,1)\to H$). | character theory | **VERIFIED** (this session) |
| 4 | **Commuting square (the functor).** A₅-equivariant Reeb operator on the ℓ-sector, restricted to the 3-tube via the **$123\!\to\!345$ embedding** (spacetime strands $\{1,2\}$ fixed — see embedding-independence note), equals the six $S_3$ knot operators with the $\mathrm{Res}^{S_5}_{S_3}$ multiplicities. | category theory | **algebraic leg CONCRETE** (Hecke-tower Bratteli = verified branching; Wedderburn projector traces computable in pyhecke); geometric leg (Reeb = this map) stays conjectural — see §"Ingredient 4+5 close-out" |
| 5 | **Markov-trace shift (the physics).** Evaluate the $H_3(q)$ trace shift between $E_{(3,1,1)}$ (ℓ=1) and $E_{(3,2)}$ (ℓ=2) projectors → correction factor $F(E,q_0)$ → test the 210 ppb muon gap. | compute (`pyhecke`) | **REFUTED** for the named candidates — the projector correction overshoots 210 ppb by 6–8 orders (§"Ingredient 4+5 close-out") |

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

### Gate resolution (2026-06-16, second pass) — existence leg SETTLED by corpus precedent

A corpus pass on the spin structure resolves the **existence** leg and reclassifies the residual:

- **The bundle's structure group is already $\mathrm{SU}(2)$** (the spin double cover) —
  [`quaternion-so3-motivation.md`](../../content/quantum-observable-universe/braids-and-knots/quaternion-so3-motivation.md):
  $G=\mathrm{SU}(2)\cong\mathrm{Sp}(1)$, and "the $\mathrm{SO}(3)$ holonomy of the chiral sheets lifts to
  $\mathrm{Sp}(1)$ conjugation" via $\mathrm{Ad}:\mathrm{SU}(2)\twoheadrightarrow\mathrm{SO}(3)$.
- **The binary-lift principle is already in the corpus, with the $S_3$ case done explicitly** —
  [`su2-generators.md`](../../content/quantum-observable-universe/brings-surface/su2-generators.md):
  "Every finite subgroup of $\mathrm{SO}(3)$ lifts, via the double cover
  $\mathrm{SU}(2)\twoheadrightarrow\mathrm{SO}(3)$, to a binary subgroup of $\mathrm{SU}(2)$. For
  $S_3\cong D_3$ the lift is the binary dihedral $\mathrm{Dic}_3$ of order 12." So the existing $S_3$ Reeb
  construction is *already* a binary-lifted ($\mathrm{Dic}_3$) spin action.
- **$A_5\to 2I$ is the direct analogue** (verified order-doubling: $|\mathrm{Dic}_3|=2|S_3|=12$,
  $|2I|=2|A_5|=120$). The binary icosahedral lift **exists canonically** — the preimage of $A_5\cong I$ under
  the $\mathrm{SU}(2)$ structure-group cover — by the same mechanism the corpus already uses for $S_3$. The lift
  is genuinely $2I$ (not split): $A_5$ has no faithful 2-dim rep, so $I\subset\mathrm{SO}(3)$ acts on the spinor
  $\mathbb{C}^2$ only through $2I$.

**Reclassified residual (the two pieces that remain, both lighter than "build the action"):**

1. **Group extent — implemented $S_3$ (3 sheets) → full $A_5$ (5 sheets).** The existing construction realizes
   only the 3-sheet $S_3\to\mathrm{Dic}_3$; the full icosahedral $A_5$ is the even-permutation group of all 5
   Bring sheets. Extending from 3-sheet to 5-sheet **is the 5-strand extension** — ingredient 4's territory, not
   a separate spin-structure obstruction.
2. **Rep identification — is geometric $A_5$ the icosahedral $T_1$/$T_2$ rep?** $A_5$ has two faithful 3-dim real
   irreps ($T_1$, $T_2$, the enantiomorphic icosahedra). Confirm the $\mathrm{Aut}(\Sigma_4)\supset A_5$ action
   on the chiral sheets / $\mathrm{SO}(3)$ holonomy is the icosahedral 3-dim rep (consistent with ingredient 3's
   $\mathrm{SO}(3)\!\downarrow\!A_5$ picking $T_1$ at $\ell=1$). A **finite rep-identification check**, not a
   construction.

**Net:** the feared "build a $2I$-equivariant structure from scratch" (old ingredient-1 crux) is **not** the
obstruction — the $\mathrm{SU}(2)$ structure group + the standard double-cover lift supply it, with the $S_3$
precedent already coded. The real remaining work is the **5-sheet extension** (ingredient 4) and a finite
**rep-identification** (residual 2). Ingredient 2 (the $2I$-equivariant Reeb field) inherits the same precedent:
the Reeb field on the $S_3\to\mathrm{Dic}_3$ construction is already binary-equivariant, so the $2I$ case is the
analogue, not a new obstruction.

### Residual-2 RESOLVED (2026-06-16, third pass) — the geometric $A_5$ is forced to be icosahedral $T_1$

The "is the geometric $A_5$ the icosahedral $T_1$?" residual closes — it is **forced** by representation theory
(three checks in the verifier, all pass):

- **(a) Dimension forces it.** The only 3-dim irreps of $A_5$ are $T_1, T_2$. The $\mathrm{SO}(3)$-holonomy on
  the chiral sheets acts on a 3-dim real space, so its $A_5$-rep is 3-dim ⟹ $T_1$ or $T_2$. And $A_5$ is
  **simple**, so any nontrivial rep is faithful ⟹ the action is the genuine icosahedral rotation. There is no
  freedom *except* chirality.
- **(b) Chirality = the $T_1/T_2$ split.** $S_5$ **fuses** the two 5-cycle conjugacy classes that $A_5$ keeps
  separate (an odd permutation conjugates a 5-cycle to its $A_5$-non-conjugate square; verified: $A_5$ has two
  classes of 12, $S_5$ has one of 24). That fusion swaps $\chi(C_5)\leftrightarrow\chi(C_5^2)$, i.e. swaps
  $T_1\leftrightarrow T_2$. So $T_1$ and $T_2$ are the **two enantiomorphic icosahedra**, exchanged by
  $S_5\setminus A_5$ — physical **parity**. The $S_5$-stable object is $T_1\oplus T_2=(3,1,1)$.
- **(c) The rotation rep is NOT the sheet-permutation rep.** The $A_5$ permutation rep on the 5 Bring sheets is
  $A\oplus G$ (trivial + 4-dim standard), with $T_1$ multiplicity 0 (verified). So the geometric $\mathrm{SO}(3)$
  rotation ($T_1$) is a *distinct* rep from "which sheet goes where" ($G$) — the rotation is the Klein
  icosahedral action on the *spin fibre*, not the sheet shuffle.

**Structural payoff (closes the loop with §1a).** $(3,1,1)$ — which hosts *both* $T_1$ (electron, $\ell=1$) and
$T_2$ (tau's $\ell=3$ part) — is exactly the $S_5$-stable chirality-pair block. The electron and tau's $T_2$
component are **parity partners** in the same Wedderburn block; the odd-permutation (parity) operation swaps
them. Chirality is not added by hand — it is the $A_5\subset S_5$ index-2 structure.

**Remaining open (now isolated):** only the **5-sheet extension** (ingredient 4 — the commuting square, promoting
the implemented 3-sheet $S_3$ to the full 5-sheet $A_5$) and the **Markov-trace shift** (ingredient 5 — the
empirical 210 ppb). Both ingredient-1 sub-pieces (existence of the $2I$ lift; identification as icosahedral $T_1$)
are settled.

## Ingredient 4+5 close-out (2026-06-16) — algebraic leg concrete; 210 ppb mechanism REFUTED

Compute: [`scripts/s5so3_ingredient_4_5_markov_shift.py`](../audits/scripts/s5so3_ingredient_4_5_markov_shift.py)
(real `pyhecke` stack: `q0`, `q_factorial`, and the figure-eight $4_1$ Wedderburn-projector traces
`FIG8_R_311 / FIG8_R_32 / FIG8_R_41`).

**Ingredient 4 — algebraic leg is concrete.** The Hecke-tower Bratteli restriction $H_5(q)\to H_3(q)$ at
generic $q$ is box removal $=$ the verified $\mathrm{Res}^{S_5}_{S_3}$ branching; the muon block $(3,2)$ lacks
exactly the $(1,1,1)$ alt block present in the electron $(3,1,1)$. The Wedderburn projectors $E_\lambda$ and
their Markov traces are **computable** (the $4_1$ values below). What stays conjectural is only the *geometric*
leg — that the $A_5$-equivariant Reeb flow **equals** this algebra map.

**Ingredient 5 — the 210 ppb mechanism is REFUTED for the named candidates.** The bare
$m_\mu=m_e\,\mathrm{Vol}(4_1)/\hbar_q^2$ is *already* good to **209.8 ppb** ($\approx 2.1\times10^{-7}$), so the
proposed correction $\mathcal{F}(E_{(3,2)},q_0)$ must equal $1\pm 2\times10^{-7}$. Both candidates the
operator-branching doc names are $O(1)$–$O(10)$:

| Candidate $\mathcal{F}$ (doc) | value at $q_0$ | $\lvert\mathcal F-1\rvert$ | overshoot vs 210 ppb |
|---|---|---|---|
| #1 sign-block subtraction $1-W_{\mathrm{alt}}\chi^{(1,1,1)}$ ($\chi=1$ exact, $W_{\mathrm{alt}}=1/[3]_q!$) | $0.8366$ | $0.1634$ (16.3 %) | $\times\,7.8\times10^{5}$ (~5.9 orders) |
| #2 channel-trace ratio $R_{(3,2)}/R_{(3,1,1)}$ ($4_1$ traces $-0.2119/-0.01416$) | $14.97$ | $13.97$ (1397 %) | $\times\,6.7\times10^{7}$ (~7.8 orders) |

The structural identity ($\chi^{(1,1,1)}=1$ exact; $(1,1,1)$ **is** the electron–muon block) holds, but the
**magnitude** of every natural Wedderburn-projector knob is 6–8 orders too large — multiplying the bare formula
by any of them *destroys* the 210 ppb agreement rather than closing it. This **quantitatively confirms the
synthesis §4 critical-distance flag** ("χ=1 necessary, not sufficient") and the 2026-06-13 doc's own §4 ("derive
the analytic closure" — left open). The 210 ppb gap is better accounted for by the mechanical proton-anchor
re-pin lever ($\Delta q_0\times$ lever, doc §1), not a categorical projector correction.

**Net keystone status after this session:**
- ✅ Geometry (ingredients 1–3): settled — $2I$ spin lift exists, geometric $A_5$ forced to icosahedral $T_1$,
  $\mathrm{SO}(3)\!\downarrow\!A_5\!\uparrow\!S_5\!\downarrow\!S_3$ chain verified.
- ◑ Ingredient 4: algebraic leg concrete + computable; **geometric leg (Reeb = the functor) remains the open
  conjecture** — this is now the sole structural unknown.
- ❌ Ingredient 5: the **named** projector mechanism does **not** close the 210 ppb muon gap (overshoots 6–8
  orders). A correction at the $2\times10^{-7}$ scale, if one exists, is not any of the natural $H_n(q)$
  Wedderburn-projector quantities.

So `conj:s5-so3-fiber-action` is now sharply localized: the **geometric Reeb=functor identification** (ing. 4) is
the open object; the muon-mass *physics* via Wedderburn projection (ing. 5) is refuted. No fit was introduced.

## Ingredient 4 geometric leg — formalize-first scoping (2026-06-16, fourth pass)

The sole remaining structural unknown is the **geometric leg of the commuting square**: that the
$A_5$-equivariant Reeb flow on the spin-fibre $\mathbb{CP}^1$ *equals* the (now-concrete) Hecke-tower
restriction functor. Before treating this as a wide open construction, decompose it and apply the
formalize-first prune:

**The commuting square (precise).** For a braid $\beta$ routed through generation degree $\ell$:
$$
\underbrace{\text{Reeb-thread}_\ell(\beta)\big|_{\text{3-tube}}}_{\text{geometric}}
\;\overset{?}{=}\;
\underbrace{\mathrm{tr}^{H_3}_M\!\big(\mathrm{Res}^{S_5}_{S_3}\,E_{\lambda(\ell)}\,\rho_5(\beta)\big)}_{\text{algebraic}}
$$
where $\lambda(\ell)$ is the $S_5$ block of degree $\ell$ (verified bridge: $\ell{=}1\to(3,1,1)$,
$\ell{=}2\to(3,2)$) and the 3-tube is the $123\to345$ embedding.

**Decomposition into three pieces:**

1. **$S_3$ base case — ESTABLISHED.** The existing exceptional-divisor Reeb construction already threads the
   six $S_3$ braid words into six knot operators whose Markov traces are the $H_3$ Wedderburn-channel values
   (`exceptional-divisor-reeb-intro.md`; the channel-trace machinery is live — e.g. the figure-eight values
   `FIG8_R_311/R_32/R_41` used in the ingredient-5 compute). So the geometric$=$algebraic identity holds at
   the 3-strand base.
2. **Ocneanu-trace consistency — STANDARD (Jones).** The Markov trace is a consistent family on the Hecke tower
   $H_3\subset H_4\subset H_5$: $\mathrm{tr}_{n+1}|_{H_n}=\mathrm{tr}_n$ and
   $\mathrm{tr}_{n+1}(x\sigma_n)=z\,\mathrm{tr}_n(x)$ for $x\in H_n$. The Bratteli restriction is box removal
   $=$ the verified $\mathrm{Res}^{S_5}_{S_3}$ branching.
3. **$H_5$ extension — OPEN (geometric only).** A 5-strand Reeb construction on the Bring **spin** bundle whose
   Markov trace is the $H_5(q)$ Ocneanu trace, $2I$-equivariantly.

**Formalize-first prune (the narrowing).** Pieces 1+2 **pin the algebraic target of any $H_5$ extension on the
3-tube** — by Ocneanu consistency the trace of the threaded $H_5$ operator restricted to the 3-tube is *forced*
to equal the existing $H_3$ construction, and the 2-spectator-strand contribution is determined by the Markov
relations ($\mathrm{tr}(x)$ and $\mathrm{tr}(x\sigma_n)=z\,\mathrm{tr}(x)$). **Therefore the open problem is NOT
"which algebraic functor"** — that is forced to be restriction, with no free parameters — **but purely whether a
$2I$-equivariant 5-strand Reeb (geometric) realization EXISTS** matching the forced target.

Consequence for how to attack it: **do not run an algebraic search over candidate $H_5\to H_3$ functors** (the
target is rigid). The work is a *geometric existence* construction — a $2I$-equivariant contact/Sasakian
structure on the 5-strand Bring spin bundle whose Reeb flow's Markov trace is the (already-determined) $H_5$
Ocneanu trace. This is contact + spin geometry on the Bring surface, owner-gated and multi-session; it is the
genuine remaining content of `conj:s5-so3-fiber-action`. Everything algebraic/combinatorial around it
(ingredients 1–3, the algebraic leg of 4) is now settled.

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
- ✅ **Ingredients 1–3 settled; ingredient 4 algebraic leg concrete; ingredient 5 REFUTED** (§"Ingredient 4+5
  close-out"). The muon-mass physics via Wedderburn projection overshoots 210 ppb by 6–8 orders — not a fit, a
  falsification.
- ⛔ **Sole remaining structural unknown = ingredient 4 geometric leg.** Prove the $A_5$-equivariant Reeb flow on
  the spin-fibre $\mathbb{CP}^1$ **equals** the (now-concrete, computable) Hecke-tower restriction functor
  $H_5(q)\to H_3(q)$ — i.e. discharge `GenerationBranchingFunctor.project` with the *geometric* map, not just the
  algebraic target. Owner-gated, multi-session; **not** a numerical probe (ingredient 5 closed that route).

## Cross-references

- [`2026-06-16-s5so3-branching-backbone-verified.md`](../audits/2026-06-16-s5so3-branching-backbone-verified.md) — backbone + bridge verification (ingredient 3)
- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](../audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md) — the candidate functor $\mathrm{Res}^{S_5}_{S_3}$
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — the synthesis (single open object)
- [`exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md) — the existing S₃-side Reeb construction
- [`spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md) — `conj:s5-so3-fiber-action` spin SU(2)_S lift (= ingredient 1's $2I$ lift)
- [`fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) — $\Sigma_4$ is a genus-4 *curve*, Aut $=S_5$ (the dimension fact behind finding 1)
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — the keystone scaffold (open `partition_to_rotation`)
