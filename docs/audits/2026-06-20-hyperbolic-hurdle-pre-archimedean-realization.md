# The "Hyperbolic Hurdle" dialog — pre-archimedean realization assessment

**Date:** 2026-06-20
**Branch:** `claude/nifty-hopper-2yt8sx`
**Trigger:** External pitch ("the Hyperbolic Hurdle") proposing three strategies
to handle products of *shifted hyperbolic functions* — (①) confocal
elliptic–hyperbolic (prolate-spheroidal) coordinates to decouple a two-center
$\mathrm{sech}(x{+}c)\,\mathrm{sech}(x{-}c)$ integral; (②) the substitution
$u=\tanh(x/a)$ mapping the Pöschl–Teller $\mathrm{sech}^2$ Schrödinger ODE to
the Associated Legendre equation; (③) replacing the shifted product by an
**addition / linearization theorem over an orthogonal-polynomial basis**
(Jacobi / Legendre $P_\lambda^\mu$). Owner steer: assess the **algebraic /
pre-archimedean realization** — does any of this live *below* the
substrate→archimedean wall, or only above it?
**Audience:** anyone weighing whether the dialog content should land in the
paper, the Lean formalization, or the compute pipeline; anyone working the
per-isotope binding combiner (Subgoal-1 / GAP-A-3) or the generation tower.
**Bottom-line up front:** Strategies ① and ② are intrinsically **archimedean**
— continuum coordinate $x\in\mathbb{R}$, a real $\mathrm{sech}^2$ potential, a
real ODE — and they solve a hurdle **QOU does not have** (there is no continuum
two-center sech integrand at the substrate). They have **no pre-archimedean
realization**. Strategy ③ **does** have one, and it is **already built**: it is
the Hecke branching trace decomposition
[`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md),
with Littlewood–Richardson fusion coefficients
[`prop:lr-coefficient-hecke`](../../content/quantum-observable-universe/mass-theory/lr-coefficient-hecke.md)
and the Wenzl-A-operator payload
[`def:wenzl-A-operator`](../../content/quantum-observable-universe/mass-theory/wenzl-A-operator.md),
assembled up the Borromean tower by
[`prop:operator-valued-combiner-convergence`](../../content/quantum-observable-universe/mass-theory/operator-valued-combiner-convergence.md).
The pitch is therefore **conceptual confirmation of an existing mechanism**, not
new leverage. The one genuinely open frontier it correctly points at is **not**
the addition theorem (which exists) but the **operator-valued / geometric
payload** that the fusion rule weights — open in two places (the universal
A-operator at $\mathbf{H}_{9+}$, and the S₅↔SO(3) fibre map). This mirrors the
[KLR-dialog assessment](2026-05-30-klr-dialog-assessment.md): textbook-correct
machinery, but the load-bearing claim does not survive contact with the
framework as new content.

---

## 1. The substrate→archimedean sort

| Strategy | Native level | Pre-archimedean realization in QOU? |
|---|---|---|
| **① Confocal elliptic–hyperbolic coords** (decouple a two-center $\mathrm{sech}(x{\pm}c)$ integral) | archimedean — continuum $x\in\mathbb{R}^3$, real measure | **None.** No continuum two-center sech integrand exists below the wall. |
| **② $u=\tanh(x/a)$ → $\mathrm{sech}^2$ Pöschl–Teller ODE → Associated Legendre** | archimedean — real ODE, $V_0\,\mathrm{sech}^2$ potential | **None as written** — a bare real-coordinate change with no $q$-deformation. |
| **③ Addition / linearization theorem over an orthogonal basis** ($P_\lambda^\mu$, Jacobi) | archimedean *as written* | **Yes — and it is the framework's core machinery (§3–§4).** |

### 1.1 Why ① and ② have no pre-archimedean shadow

The "hyperbolic" content of QOU is **not** a $\mathrm{sech}(x\pm c)$ product over
a continuous spatial coordinate. It is two distinct, unrelated objects:

1. **Hyperbolic volume** of a knot/link complement — a *discrete*
   Lobachevsky / Bloch–Wigner sum $\mathrm{Vol}(K)=\sum_i \Lambda(\theta_i)$ over
   ideal tetrahedra. A number (archimedean), assembled combinatorially, not an
   integral of a sech potential.
2. **The Coulomb/strong ratio** $\tanh(\ln q)=\dfrac{q-q^{-1}}{q+q^{-1}}
   =\dfrac{q^2-1}{q^2+1}$ — already a $q$-rational
   ([`coulomb-strong-ratio-q-rational`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-strong-ratio-q-rational.md)).

QOU's *only* use of $\tanh$ is item 2, where an archimedean transcendental
$\tanh(\ln q)$ **collapses to a $q$-rational**. That collapse is exactly what
"pre-archimedean realization" means — and strategy ②'s $\tanh$ exhibits none
(it is a real coordinate change, no $q$-shadow). Strategy ① separates an
integrand that does not exist below the wall.

> **Failure-mode warning (recurrent).** Wiring ①/② into the hyperbolic-*volume*
> compute repeats the dilog re-pitch failure documented in the
> [KLR-dialog assessment §"Trefoil is not hyperbolic"](2026-05-30-klr-dialog-assessment.md):
> $\mathrm{Vol}$ is a discrete dilog sum, torus/Seifert knots — including the
> electron trefoil $T_{2,3}$ — give $D(z)=0$, and there is no sech integrand to
> separate. Do not re-derive this analysis on a new sech/Pöschl–Teller re-pitch.

---

## 2. ③ below the wall — the dictionary

| Pitch (archimedean strategy ③) | QOU pre-archimedean realization |
|---|---|
| shifted two-center product $f_A(x)\,f_B(x)$ | character $\chi^\lambda(\beta_1\cdot I\cdot\beta_2)$ of a braid glued across the interface $I=\sigma_{n_1}$ |
| orthogonal basis $\{P_\lambda^\mu\}$ | irreducible Hecke characters $\{\chi^\lambda\}$ (orthogonal under the Markov/Frobenius pairing) |
| addition theorem $P_\lambda(\tanh(x{-}c))=\sum_k C_k(c)\,P_\lambda^k$ | restriction $V_\lambda\!\downarrow_{\mathbf{H}_{n_1}\otimes\mathbf{H}_{n_2}}=\bigoplus_{\mu,\nu} c^\lambda_{\mu\nu}\,V_\mu\boxtimes V_\nu$ |
| expansion coefficients $C_k(c)$ | LR fusion coefficients $c^\lambda_{\mu\nu}\in\mathbb{Z}_{\ge0}$ **+** operator payload $A^\lambda_{\mu\nu}(I)$ |
| $q\to1$ classical limit | symmetric-group LR / Clebsch–Gordan rule = the actual Jacobi/Legendre linearization the pitch names (zonal spherical functions) |

The $q$-orthogonal-polynomial bridge the pitch is groping toward is the
**Koornwinder / Macdonald–Askey–Wilson** family; `koornwinder1990` is already in
`references.bib`, and CLAUDE.md §7b already lists "non-symmetric Macdonald
evaluation under the Observation Frame ($\tau$)" as authoring guidance.

---

## 3. The pre-archimedean addition theorem (concretely)

$$
\chi^\lambda(\beta_1\cdot I\cdot\beta_2)
  = \sum_{\mu\vdash n_1,\;\nu\vdash n_2}
    c^\lambda_{\mu\nu}\;
    \mathrm{Tr}\!\bigl(A^\lambda_{\mu\nu}(I)\,
                       (\rho_\mu(\beta_1)\otimes\rho_\nu(\beta_2))\bigr)
$$

This is the "single-center summation" strategy ③ chases: the LHS is a genuinely
entangled two-center object (braids on *both* sides of the interface
$I=\sigma_{n_1}$ for the inclusion $\mathbf{H}_{n_1}(q)\otimes\mathbf{H}_{n_2}(q)
\hookrightarrow\mathbf{H}_{n_1+n_2}(q)$); the RHS is a finite sum over the
orthogonal character basis with integer fusion weights — **no continuum
integral, no shifted-sech product.**

| Object | Block | Status |
|---|---|---|
| the addition theorem | [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md) | class-axiomatised (§3b), Lean-verified modulo instance (Wenzl 1988 + Halverson–Ram 1998 + Hoefsmit 1974) |
| fusion coefficients $c^\lambda_{\mu\nu}$ | [`prop:lr-coefficient-hecke`](../../content/quantum-observable-universe/mass-theory/lr-coefficient-hecke.md) | **concretely computed** (`computations/substrate/lr_coefficients.py`; tables `3⊗3→6`, `3⊗6→9`, `6⊗6→12`) |
| operator payload $A^\lambda_{\mu\nu}(I)$ | [`def:wenzl-A-operator`](../../content/quantum-observable-universe/mass-theory/wenzl-A-operator.md) | full-rank at $\mathbf{H}_6$; **least-squares (open) at $\mathbf{H}_{9+}$** (`computations/a_operator/A_operator_extract_at_level.py`) |

---

## 4. The Borromean tower instantiation

- One nucleon $=$ **3 strands** (Bring color tube; proton $=\mathcal{B}_3$). So a
  two-nucleon interface is $\mathbf{H}_3\otimes\mathbf{H}_3\hookrightarrow
  \mathbf{H}_6$, $I=\sigma_3$ — **the deuteron is the two-center base case.**
- Tower: peel one nucleon ($+3$ strands) at a time, interfaces at
  $n_k=3(A-k+1)$. The combiner **telescopes**:

$$
\mathrm{cv}(A{+}1)=w(A)\,\mathrm{cv}(A)
\quad\Longrightarrow\quad
\mathrm{cv}(2{+}m)=\Bigl(\textstyle\prod_{j=0}^{m-1}w(2{+}j)\Bigr)\mathrm{cv}(2).
$$

That is
[`prop:operator-valued-combiner-convergence`](../../content/quantum-observable-universe/mass-theory/operator-valued-combiner-convergence.md):
the addition theorem applied recursively **is** "express the multi-center
product as accumulated single-center sums," bottoming out at the deuteron
($\mathbf{H}_6$). The recursion is realised in
`computations/canonical_tr_m_via_branching.py` and Lean-verified (by `Nat.rec`)
modulo the `[WenzlAOperator R q]` instance.

---

## 5. Solid vs. open (the honest part)

- ✅ **Pre-archimedean & proved-modulo-infra.** The branching identity, the LR
  coefficients, and the telescoping recursion are class-axiomatised (§3b-cond)
  and Lean-verified modulo the class instance. LR numbers are integer and
  concretely tabulated.
- ✅ **Exact at the two-center base case.** The $\mathbf{H}_6$ A-operator extract
  is full-rank; branching agrees with the direct Markov trace to **0.72 ppb**
  (Phase A baseline).
- ⚠️ **The real gap is the operator payload, not the addition theorem.** The
  *universal* $A^\lambda_{\mu\nu}(I)$ at $\mathbf{H}_{9+}$ (3+ nucleons) is a
  least-squares fit over an inner-test family, not closed form — that missing
  operator is
  [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/particle-interactions/crystal-graph-realization.md)
  via `prop:crystal-r-matrix-sub-lemma`. Production sidesteps it by delegating
  $A\ge3$ to the direct Hoefsmit kernel $\mathrm{tr}_M=\sum_\lambda
  y_\lambda\chi^\lambda$, so higher rungs are *validated* but not yet *derived*
  through the theorem.
- ⚠️ **Binding $\Delta_\lambda$ is a separate gate.** The theorem delivers
  $\chi^\lambda$ (→ mass / $\mathrm{tr}_M$); per-isotope binding
  $B=m_e\sum_\lambda y_\lambda\chi^\lambda\Delta_\lambda$ still needs the
  per-partition $\Delta_\lambda$, which remains open (six ansätze failed; **no
  7th fit** per the CLAUDE.md Δ_λ gate).

---

## 6. Connection to the live GAP-A-3 / s5-so3 keystone

The pitch's ③ lens localizes the open problem to the **operator-valued /
geometric payload** of a Hecke branching — and the same shape appears at a
*second*, currently-active frontier. Recent `origin/main` commit `035aa52e`
(2026-06-16, "m_τ Path A + GAP-A-3 binding both reduce to s5-so3 keystone")
ties two programs to one open conjecture:

| Frontier | Hecke branching | Fusion combinatorics (known) | Open payload |
|---|---|---|---|
| **Nucleon tower / mass** | $\mathbf{H}_{n_1}\otimes\mathbf{H}_{n_2}\hookrightarrow\mathbf{H}_{n_1+n_2}$ | LR coefficients $c^\lambda_{\mu\nu}$ | universal $A^\lambda_{\mu\nu}(I)$ at $\mathbf{H}_{9+}$ — `conj:crystal-graph-realization` |
| **Generation + binding $P_\lambda$** | $\mathbf{H}_5\to\mathbf{H}_3$ restriction | $S_5\!\downarrow\!S_3$ multiplicities (e.g. the $(2,1)$ irrep appears with multiplicity **exactly 2** in both electron $\ell{=}1$ block $(3,1,1)$ and muon $\ell{=}2$ block $(3,2)$) | the partition→rotation map — `conj:s5-so3-fiber-action` |

The second frontier is the **s5-so3 keystone**: the geometric fibre map
$S_5\supset A_5\cong I\subset SO(3)$ realizing each partition-of-5 as an
icosahedral rotation on Bring's quintic surface, formalized (on `main`) as the
open classes
[`BringFiberAction`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
(field `partition_to_rotation : PartitionOf5 → IcosahedralRotation`) and
[`GenerationBranchingFunctor`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean)
(field `project : H5 → H3`). The binding side enters via the two-layer GAP-A-3
factorization $\Delta_\lambda(K)=A(K)\cdot P_\lambda(K)$, where $A(K)$ is
Phase-4-derived and $P_\lambda(K)$ — the per-partition deviation from the flat
($\mathrm{mass}/\mathrm{trace}$) distribution — reduces to this same fibre map.

**The unifying observation (the actual payoff of the ③ lens).** In *both*
frontiers the combinatorial fusion rule (LR coefficients / restriction
multiplicities) is **known and integer**; what is open is the operator-valued
or geometric payload the rule weights. Strategy ③'s "addition theorem over an
orthogonal basis" is thus the right *shape*, realized twice, and it correctly
relocates the open problem from the *coefficients* (closed) to the *payload*
(open).

> **Critical-distance caveat (do not overstate).** This is **not** "s5-so3
> closes binding." Per commit `035aa52e` §4, the identity
> $\chi^{(1,1,1)}(\beta_{\mathrm{Bor}})=1$ is **necessary, not sufficient**; the
> full Wedderburn correction $F(E_{(3,2)},q_0)$ requires the *open* functor. The
> partition→rotation map is unconstructed; $\Delta_\lambda$ stays gated, with
> $P_\lambda\equiv1$ the free baseline candidate channels must beat. Adjacent
> landmines to avoid: $(1+q)/2$ is **refuted** (sign-flipped at canonical $q_0$,
> PR #1707 — do not re-chase); the generation structure is **icosahedral
> $\ell$-degree branching**, not a Koide $\mathbb{Z}/3$ democracy (Koide is a
> CAL-4 import, commit `afc820dc`); and the $c_k$ ladder is **q-holonomic**
> (argument recurrence), not a C-finite order recurrence (commit `8ec801b1`).

---

## 7. Recommendation

1. **Do not add ①/② to the paper, Lean, or compute.** No pre-archimedean
   content; wrong object; re-derives a known dead end if pointed at the volume
   compute.
2. **③ requires no new content.** It is
   `prop:hecke-branching-trace-decomposition` +
   `prop:operator-valued-combiner-convergence`, already on disk. The pitch's
   value is confirming the *shape* of the open frontier — an addition theorem
   over the Hecke-character basis — and localizing the gap to the payload.
3. **The productive frontier is the operator/geometric payload**, in two linked
   places: the universal A-operator at $\mathbf{H}_{9+}$
   (`conj:crystal-graph-realization`) and the s5-so3 partition→rotation map
   (`conj:s5-so3-fiber-action`), joined to GAP-A-3's two-layer
   $\Delta_\lambda=A(K)\cdot P_\lambda(K)$ per the
   [Δ_λ gating context](2026-05-18-delta-lambda-gating-context.md). **No 7th
   $\Delta_\lambda$ ansatz.**

---

## 8. Cross-references

- [KLR / crystal-bases dialog assessment](2026-05-30-klr-dialog-assessment.md)
  — the precedent: textbook-correct re-pitch, 0/6 load-bearing claims survive.
- [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md)
  — the pre-archimedean addition theorem.
- [`prop:lr-coefficient-hecke`](../../content/quantum-observable-universe/mass-theory/lr-coefficient-hecke.md)
  — the fusion coefficients.
- [`def:wenzl-A-operator`](../../content/quantum-observable-universe/mass-theory/wenzl-A-operator.md)
  — the operator payload (open at $\mathbf{H}_{9+}$).
- [`prop:operator-valued-combiner-convergence`](../../content/quantum-observable-universe/mass-theory/operator-valued-combiner-convergence.md)
  — the Borromean-tower telescoping recursion.
- [`coulomb-strong-ratio-q-rational`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-strong-ratio-q-rational.md)
  — the model pre-archimedean collapse $\tanh(\ln q)=(q^2-1)/(q^2+1)$.
- [Δ_λ gating context](2026-05-18-delta-lambda-gating-context.md) — six failed
  ansätze; the Δ_λ gate; GAP-A-3 / GAP-A-4 directions.
- [m_avg Subgoal-1 operator-combiner scope](../coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md)
  — the +2.89% closure path the combiner serves.
- `S5SO3FiberAction.lean`, `GapA4MuonBranching.lean` (on `main`) — the s5-so3
  keystone classes (commit `035aa52e`).
- CLAUDE.md §7b (symmetric-crystal / Macdonald authoring guidance), §7c (base
  ring), §3b-cond (conditional-class formalization).
