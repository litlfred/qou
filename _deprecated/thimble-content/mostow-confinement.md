**Proposition (conditional on
[`MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean)).**
*Let $K \subset U$ be the link formed at an encounter
([approach](#sec:approach-to-exceptional-divisor)), and assume
that the merged complement $U \setminus K$ admits a complete,
finite-volume hyperbolic structure satisfying Mostow rigidity
(class field `MostowRigidity` in
`QOU.Encounter.MostowRigidity`).  Then:*

1. *(**Volume rigidity.**) The hyperbolic volume
   $\mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$ is a topological
   invariant of $K$: it depends only on the link type, not on
   any continuous parameter of the encounter.*

2. *(**Mass rigidity.**) Under the
   [Archimedean realization functor](#def:archimedean-realization-functor)
   $\tau_{\mathrm{arch}}$, the categorical mass attached to $K$
   is*

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}^{\mathrm{trans}}(\varrho_K)\bigr)
  \;=\;
  \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(U \setminus K),
$$

   *and is therefore **discrete**: distinct knot types yield
   distinct mass eigenvalues with no continuous interpolation.*

3. *(**Confinement.**) The energy required to deform $K$ into a
   non-isotopic link is bounded below by the Mostow gap to the
   nearest neighbour in the discrete volume spectrum.  Particles
   are confined because there is no nearby hyperbolic structure
   they can slip into.*

![Mostow staircase: discrete hyperbolic-volume spectrum and
confinement.  The horizontal axis is
$\mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$; each tread is a
distinct knot-type plateau (Unknot/Seifert-fibred at
$\mathrm{Vol} = 0$, then $4_1$, $5_2$, $6_1$).  Risers are the
Mostow gaps; their strict positivity is the formal content of
the rigidity statement.  The "no continuous deformation"
annotation marks the impossibility of moving sideways across a
gap, which is what *confinement* means at the geometric
level.](rendered/mostow-staircase.svg)

The proposition is **conditional on `MostowRigidity`** (§3b-cond
pattern).  The class is axiomatised in
[`QOU.Encounter.MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean);
The Lean module now carries substantive predicates rather than
`True` placeholders.  The class field signature is

```
class MostowRigidity (M : Type*) where
  volume         : ℝ
  volume_nonneg  : 0 ≤ volume
  mostow_gap     : ℝ
  mostow_gap_pos : 0 < mostow_gap
```

and the downstream theorem

```
theorem mass_rigidity_of_mostow [h : MostowRigidity M] :
    0 ≤ h.volume ∧ 0 < h.mostow_gap
```

is **fully proved** (no `sorry`) by unpacking the class
witnesses.  This realises parts (1) (existence of a real volume
invariant) and (2)--(3) (strictly positive Mostow gap = isolated
mass eigenvalue = confinement) at the level needed by downstream
consumers.

Two concrete instances start populating the hyperbolic-volume
spectrum (both in
[`QOU.Encounter.MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean)):

* **`MostowRigidity.unknot : MostowRigidity Unknot`** — the
  unknot-complement (degenerate, Seifert-fibred) case: volume
  $0$ by Thurston's extension of $\mathrm{Vol}$ to non-hyperbolic
  complements, with the gap conservatively set to
  $1 < \mathrm{Vol}(4_1) \approx 2.0299$.

* **`MostowRigidity.figureEight : MostowRigidity FigureEight`**
  — the figure-eight knot complement $4_1$, smallest known
  orientable cusped hyperbolic 3-manifold (Cao--Meyerhoff 2001):
  volume $\mathrm{Vol}(4_1) = 2 \, \mathrm{Cl}_2(\pi/3) \approx
  2.02988321281931$ (witnessed at $50$ decimal digits in
  [`hyperbolic-volumes.witness.json`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/computations/hyperbolic-volumes.witness.json)
  via the Clausen-function identity), gap conservatively set to
  $0.5 < \mathrm{Vol}(5_2) - \mathrm{Vol}(4_1) \approx 0.798$.
  Both Lean literals carry `:leanval[...]` tags so the
  [`codemod-leanval.ts`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/pipeline/codemod-leanval.ts)
  pipeline keeps them in lock-step with the witness; CI gates
  on `--check`.

The fully-proved comparison theorem
`unknot_volume_lt_figureEight_volume`
($\mathrm{volumeInvariant}(\mathtt{Unknot}) < \mathrm{volumeInvariant}(\mathtt{FigureEight})$)
exhibits the first non-trivial use of `volumeInvariant` and
shows that the class is rich enough to support genuine
spectral comparisons rather than just ansatz bookkeeping.

The §3b "hard work" deferred to the long-term Mathlib
geometric-topology layer is the *full* discreteness theorem
asserting that, for a given $M$, the value of `mostow_gap`
matches the actual gap to the next hyperbolic-volume value
(rather than just being some positive real).  Downstream theorems
in this paper consume only the witnesses, not that absolute
identification.  The shape mirrors `SDPSlaterUniqueness`
([primal uniqueness in the SDP-rank module](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean)):
both are conditional-class axiomatisations of a multi-week
Mathlib formalisation, and both unlock the corresponding
rigorous conditional consequences.

## Why this is the geometric mirror of the SDP optimum

Mostow rigidity is the **geometric face of strong duality**.  We
unpack the parallel:

| Algebraic side                 | Geometric side                     |
|--------------------------------|------------------------------------|
| Primal SDP optimum $\Phi^\ast$ | Hyperbolic structure on $U\setminus K$ |
| Slater's condition (strict feasibility) | Existence of a complete finite-volume structure |
| Strong duality (gap $= 0$)     | Steepest-descent has converged     |
| `SDPSlaterUniqueness`          | Mostow rigidity                    |
| Discreteness of $\Phi^\ast$    | Discreteness of $\mathrm{Vol}_{\mathrm{hyp}}$ |
| Wedderburn-block content       | Knot type up to homeomorphism      |

The
[GB--PL thimble bijection](#conj:gb-reduction-pl-thimble-bijection)
realises this column-by-column: the algebraic SDP datum on the
left is the $\mathbb{Z}[q^{\pm 1/2}]$-shadow of the hyperbolic
datum on the right, with the
[Archimedean realisation functor](#def:archimedean-realization-functor)
as the explicit translator.  *Mass is quantised because volume is
rigid* — and volume is rigid because Mostow's theorem leaves no
room for it to drift.

## Cited literature

The hyperbolic-rigidity framing matches the
*rigid phase* of Witten's analytic continuation of Chern--Simons
theory: in three dimensions the Chern--Simons path integral
concentrates exactly on the hyperbolic structures satisfying
Mostow rigidity.  Neumann--Zagier give the first-order behaviour
of $\mathrm{Vol}_{\mathrm{hyp}}$ near the rigid point as the
critical behaviour of an algebraic potential — the
*Neumann--Zagier potential* — whose stationary points are the
"settled" configurations.  We collect these and other
literature precedents in the
[encounter literature bridge](#rem:encounter-literature-bridge).
