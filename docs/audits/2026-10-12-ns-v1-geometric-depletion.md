# NS vector 1: geometric depletion of vortex stretching, mapped onto the QOU chain

**Date:** 2026-10-12 (finished 2026-10-13)
**Bean:** `qou-fm7s` (parent `qou-vo9t`)
**Branch:** `ns-v1`, based on `claude/bold-gates-00l1bl` at `fff8e49a6`
**Setting:** unforced 3D incompressible Navier–Stokes ($f \equiv 0$), smooth data, on $\mathbb R^3$ or $\mathbb T^3$. This is the setting stated in `fluid-dynamics/ns-obstruction.md:15`.
**Background:** `2026-10-12-ns-rescue-reformulations.md` (cited as **[R]**) and `2026-10-12-ns-chain-after-item3-retraction.md`.

Tags: **[S]** standard literature; **[D]** derived here; **[L]** Lean, sorry-free; **[A]** asserted in the corpus without derivation; **[O]** open.

---

## 0. Verdict

1. **Lean [L].** The pointwise algebra that makes aligned vorticity kill stretching is now proved, sorry-free, in `QOU/FluidDynamics/GeometricDepletion.lean`. No PDE statement is formalized. No axiom or carrier is introduced.
2. **Mapping: no QOU quantity is the Constantin–Fefferman hypothesis.** The nearest corpus object is the plane field $\ker\varTheta$. Under the only reading in which it can be related to vorticity, $\ker\varTheta = \xi^\perp$, its Levi data is a single scalar $\xi\cdot\operatorname{curl}\xi$. That is one component of $\nabla\xi$. The Constantin–Fefferman condition is a bound on all of $\nabla\xi$.
3. **The chain's non-degenerate ⇒ singular branch is refuted under that reading [D].** A Beltrami flow on $\mathbb T^3$ is contact everywhere, has a constant Levi scalar, satisfies Constantin–Fefferman trivially, and is a global smooth unforced NS solution (§3.4).
4. **One true conditional statement survives, and it is a necessary condition on the corpus's counterexample (§3.5).** If the corpus's blowup object were a smooth NS solution, its vorticity *line field* would have to lose ½-Hölder coherence in the high-vorticity region. The corpus's anti-parallel-pair argument never addresses filament bending, and a straight anti-parallel pair is excluded twice over.

---

## 1. Literature (all **not held** in `library/`)

Corpus-grep, all six paths. Path 0 (`corpus_search`) is unavailable: the `paper-assistant` server failed to connect. So the absences below are lexical.

- Constantin, Fefferman, depletion, *vorticity direction* and *da Veiga / Berselli* were grepped over `folio/`, `docs/audits/`, `computations/`, `beans/defs/`, `library/INDEX.md`, `library/*/sections` and `library/*/ocr`.
- No held source. The hits were unrelated namesakes (Constantin Teleman, Constantin Arcuş), Fefferman in CR geometry, and the one-line Clay framing in `ns-obstruction.md:15`.
- No corpus block defines the direction field $\xi = \omega/|\omega|$.

**[S1] Constantin–Fefferman.** P. Constantin, C. Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, Indiana Univ. Math. J. **42** (1993) 775–789.

- Statement: let $u$ be a smooth solution on $[0,T)$. Suppose there are $\Omega,\rho>0$ such that, whenever $|\omega(x,t)|>\Omega$ and $|\omega(y,t)|>\Omega$, the angle $\varphi$ between $\xi(x,t)$ and $\xi(y,t)$ satisfies $|\sin\varphi| \le |x-y|/\rho$. Then the solution does not blow up at $T$.
- Only the **line field** $[\xi]$ enters, through $|\sin\varphi|$.
- Bibliographic data and the qualitative statement were confirmed by web search via secondary sources (Beirão da Veiga's papers; Springer s10473-020-0606-7). The exact hypothesis form above is quoted from the standard secondary literature. The primary text was not read.

**[S2] Beirão da Veiga–Berselli.** H. Beirão da Veiga, L. C. Berselli, *On the regularizing effect of the vorticity direction in incompressible viscous flows*, Differential Integral Equations **15**(3) (2002) 345–356.

- They improve the Lipschitz condition to $|\sin\varphi| \le C|x-y|^{1/2}$ in the same region.
- Later surveys by Beirão da Veiga call $\beta = 1/2$ the best Hölder exponent to date.
- Confirmed by web search. The primary theorem statement was not read.

**[S3] Constantin.** P. Constantin, *Geometric statistics in turbulence*, SIAM Review **36** (1994) 73–98.

- The stretching rate $\alpha = \xi\cdot S\xi$ has the singular-integral representation
  $$\alpha(x) = \tfrac{3}{4\pi}\,\mathrm{P.V.}\!\int D(\hat y,\xi(x),\xi(x+y))\,|\omega(x+y)|\,\frac{dy}{|y|^3},\qquad D(e_1,e_2,e_3) = (e_1\cdot e_3)\det(e_1,e_2,e_3).$$
- Publication data are confirmed (paywalled). The kernel formula is as given in the brief and the secondary literature (Dascaliuc–Grujić arXiv:1205.7080 restates it). **It was not checked against the primary text.**
- Nothing in the Lean depends on this formula: the Lean is about $D$ as a function.

Recommended follow-up, unclaimed: ingest [S1]–[S3] into `library/` and register `references.ts` keys before any content block cites them.

---

## 2. Lean results [L]

The file is `folio/quantum-observable-universe/lean/QOU/FluidDynamics/GeometricDepletion.lean`, in namespace `QOU.FluidDynamics.GeometricDepletion`. Vectors are `Fin 3 → R` with Mathlib's `crossProduct` and `⬝ᵥ`. In the table, $|v|^2$ means $v\cdot v$.

| declaration | statement | ring |
|---|---|---|
| `triple_eq_det` | `triple e₁ e₂ e₃ = det ![e₁,e₂,e₃]` | `CommRing` |
| `depletionKernel_self` | $D(e_1,e_2,e_2)=0$ | `CommRing` |
| `depletionKernel_neg_self` | $D(e_1,e_2,-e_2)=0$ | `CommRing` |
| `depletionKernel_neg_third` | $D(e_1,e_2,-e_3)=D(e_1,e_2,e_3)$ | `CommRing` |
| `depletionKernel_neg_neg` | $D(e_1,-e_2,-e_3)=-D(e_1,e_2,e_3)$ | `CommRing` |
| `triple_sub_second` | $\det(e_1,e_2,e_3)=\det(e_1,e_2,e_3-e_2)$ | `CommRing` |
| `cross_dot_self` | Lagrange: $\lvert b\times c\rvert^2=\lvert b\rvert^2\lvert c\rvert^2-(b\cdot c)^2$ | `CommRing` |
| `dot_sq_le` | Cauchy–Schwarz | ordered field |
| `triple_sq_le_sub` | $\det^2 \le \lvert e_1\rvert^2\lvert e_2\rvert^2\lvert e_3-e_2\rvert^2$ (Hadamard with the shift) | ordered field |
| `depletionKernel_sq_le` | $D^2 \le \lvert e_1\rvert^4\lvert e_2\rvert^2\lvert e_3\rvert^2\lvert e_3-e_2\rvert^2$ | ordered field |
| `depletionKernel_sq_le_cross_unit` | for unit $e_1,e_3$: $D^2\le\lvert e_2\times e_3\rvert^2$ ($=\sin^2\varphi$ when $e_2$ is unit too) | ordered field |
| `depletionKernel_sq_le_unit_sub` / `_add` | for unit vectors: $D^2\le\lvert e_3\mp e_2\rvert^2$ | ordered field |
| `abs_depletionKernel_le_unit` | $\lvert D\rvert\le\min(\lVert e_3-e_2\rVert,\lVert e_3+e_2\rVert)$, Euclidean norm | `ℝ` |
| `depletionKernel_witness` | $D((1,1,1),(1,0,0),(0,1,0))=1$, so $D\not\equiv0$ | `ℝ` |

**Verification.**
- `lean`-direct with `-DautoImplicit=false -s 65536` against the private olean tree `olean-v1`: **exit 0**, no warnings.
- `#print axioms` on all 11 headline theorems gives `[propext, Classical.choice, Quot.sound]`.
- A grep for `sorry`, `axiom`, `native_decide` and `: True` returns nothing.
- `lake build` was not run.

**Correction to the brief [L].** The brief anticipated a "sign-flip symmetry". The correct statements are:
- $D$ is **even in $e_3$ alone.** The kernel sees only the line through $\xi(x+y)$, which matches the $|\sin\varphi|$ form of [S1].
- $D$ is **odd under a global flip** $(e_2,e_3)\mapsto(-e_2,-e_3)$. This is consistent with $u\mapsto-u$ reversing $S$ and therefore $\alpha$.

**Why the sharp form matters.** `depletionKernel_sq_le_cross_unit` bounds the kernel by $|\xi(x)\times\xi(x+y)| = |\sin\varphi|$. That is exactly the quantity [S1] controls. The Lipschitz hypothesis $|\sin\varphi|\le |y|/\rho$ thus turns the $|y|^{-3}$ kernel into one that is integrable near the origin. This is the pointwise mechanism, and it is now machine-checked. The PDE argument built on it (Biot–Savart, energy estimates) is not.

---

## 3. Mapping onto the corpus

### 3.1 Candidate objects

- **Direction field $\xi$.** Undefined in the corpus (§1).
- **Contact plane field $\ker\varTheta$.** `core-levi-form.md` places the vortex filament $\varrho$ on $(\mathcal S,\varTheta)$, with its normal plane $N_p\varrho\subset\ker\varTheta_p$.
- **Reeb field.** In [R] §4 this is the fibre generator $V$ of $M = UT(\Sigma_4)$, a Beltrami field.

### 3.2 What the corpus forces, and where [D]

A contact structure needs dimension $\ge 3$, and [R] §1a shows $\mathcal S$ cannot be a surface here.

On a contact 3-manifold, $N_p\varrho$ and $\ker\varTheta_p$ are both 2-planes, so the inclusion is an equality. If $\varrho$ is a vortex line (tangent $\xi$), then $\ker\varTheta_p = \xi(p)^\perp$.

**This holds only on the filament $\varrho$.** [S1] needs a hypothesis on the whole open region $\{|\omega|>\Omega\}$. Nothing in the corpus fixes $\varTheta$ off $\varrho$, and nothing relates it to $\omega$ there.

### 3.3 The Levi data is one scalar [D]

Suppose we grant $\varTheta = f\,\xi^\flat$ (with $f\neq0$) on a region. Then on $\ker\varTheta$:
$$d\varTheta|_{\ker\varTheta} = f\,(\xi\cdot\operatorname{curl}\xi)\,\mathrm{vol}_{\ker\varTheta},$$
because $df\wedge\xi^\flat$ vanishes on $\ker\xi^\flat$.

- **There is one Levi number, not two.** A real 2-plane field in dimension 3 has complex rank 1, and its Levi form is $1\times1$. This agrees with `2026-09-04-contact-distribution-complex-rank-and-dimension-seven.md`, which records `cr_dim = 1` and $\Lambda^2_{\mathbb C}H = 0$.
- So the eigenvalue pair $(\lambda_\parallel,\lambda_\perp)$ and $\mathrm{cond}(\mathcal L_\varTheta|_{N_p})$ of `core-levi-form.md` are **undefined in dimension 3.** They need complex rank $\ge 2$, i.e. real dimension $\ge 5$, where $N_p\varrho$ can no longer be a filament's whole normal plane.
- This is a third dimension conflict, in addition to [R] §1a. It is recorded here and not repaired: content edits are out of scope and need the owner.

### 3.4 Neither Levi branch is the CF hypothesis, and the non-degenerate ⇒ singular branch is false [D]

**[S1] gives an upper bound on the Levi scalar, never a lower one.** For a unit field, $\partial_v\xi\perp\xi$ and $|\xi\times\partial_v\xi| = |\partial_v\xi|$. Hence $|\sin\varphi|\le|x-y|/\rho$ gives $|\partial_v\xi|\le 1/\rho$ for unit $v$, and so $|\xi\cdot\operatorname{curl}\xi|\le C/\rho$.

- CF therefore **implies** a bound on the Levi scalar.
- Neither branch of the Levi dichotomy implies CF:
  - non-degeneracy, $\xi\cdot\operatorname{curl}\xi \neq 0$, is a lower bound;
  - degeneracy, $\xi\cdot\operatorname{curl}\xi = 0$ (local integrability of $\xi^\perp$), is one vanishing component.
- Neither says anything about the other components of $\nabla\xi$.

**Counterexample to "contact non-degenerate along the vortex ⇒ singular".** This is the corpus's branch (A) in `levi-degeneracy-conjecture.md` and `core-levi-interpretation.md:13`. On $\mathbb T^3$ (period $2\pi$ in $z$), take
$$u(x,t) = e^{-\nu t}(\sin z,\ \cos z,\ 0).$$

- Then $\operatorname{curl}u = u$, so $\omega = u$ and $\xi = (\sin z,\cos z,0)$.
- $(u\cdot\nabla)u = u_z\,\partial_z u = 0$, so with $p\equiv0$ this is an exact global smooth solution of unforced NS.
- $\xi\cdot\operatorname{curl}\xi = 1$ everywhere, so $\ker\xi^\flat$ is a contact structure on all of $\mathbb T^3$, with a constant, non-degenerate Levi scalar.
- $\xi$ is smooth with $|\nabla\xi| = 1$, so [S1] holds with $\rho = 1$.

Under the reading $\ker\varTheta=\xi^\perp$, the implication is false by explicit counterexample. This is scope (b), with the counterexample as the invariant. It is the $\mathbb T^3$ twin of [R] §4: the model's own Reeb field is Beltrami, and $e^{-\nu t}V$ is global.

**Scope of the refutation.** It refutes the *implication* under this identification. It does not refute any reading the corpus has not stated.

### 3.5 The one true conditional statement [D, from S1/S2]

**Proposition.** Let $u$ be a smooth solution of unforced NS on $[0,T^*)$ on $\mathbb R^3$ or $\mathbb T^3$, in the class of [S2]. Suppose it blows up at $T^*$, for example because $\int_0^{T^*}\lVert\omega\rVert_\infty = \infty$, the form asserted in `vorticity-lower-bound.md` (c). Then for every $\Omega>0$ and $C>0$ there are $t<T^*$ and $x,y$ with $|\omega(x,t)|,|\omega(y,t)|>\Omega$ and $|\sin\varphi|>C|x-y|^{1/2}$. The Lipschitz statement of [S1] follows a fortiori.

**Proof.** The contrapositive of [S2].

**What it says about the corpus.**

- **The hypothesis is not established.** `vorticity-lower-bound.md` concerns the weak limit $v^*$ as $q\to1$. The corpus does not show that $v^*$ is a smooth solution on $[0,T^*)$ [O], so the Proposition applies to the corpus's object only conditionally.
- **The counterexample needs filament bending, and the corpus never argues for it.** The full corpus argument (`vorticity-lower-bound-argument.md`, five lines) is the anti-parallel Biot–Savart ODE. It never mentions filament bending, curvature or the direction field.
  - For a *straight* anti-parallel pair the line field $[\xi]$ is constant, so [S1] holds trivially and no blowup occurs.
  - That flow is also two-dimensional, so it is globally regular by Ladyzhenskaya's theorem [S, not held].
  - Across the pair $\xi(x+y)\approx-\xi(x)$, which is exactly where `depletionKernel_neg_self` makes the partner's contribution vanish to first order in the angle.
- So any realization of `conj:ns-counterexample` must make the filaments bend or twist without bound inside the high-vorticity region. The corpus currently supplies no mechanism for that.

**This is a necessary condition, not a QOU result.** No QOU quantity enters its hypothesis. That is why §0 says no QOU quantity *is* the CF hypothesis.

---

## 4. Recommended next step

1. **Owner decision (not taken here): what $\varTheta$ is off the filament.**
   - **What it means:** `core-levi-form` would define $\varTheta$ on a 3D region as $f\,\xi^\flat$, or say it is the Boothby–Wang form of [R].
   - **What it costs:** one content block plus its `.lean` sibling.
   - **What it risks:** under $f\xi^\flat$, §3.3 makes $\mathrm{cond}$ undefined and §3.4 refutes branch (A). Under Boothby–Wang, $\varTheta$ is unrelated to any NS solution.
   - **What it commits to:** either reading removes the two-eigenvalue claim.
   - **Default if nothing is decided:** the blocks stay as they are, with the dimension and branch defects of [R] §1 unscoped.
2. **Cheapest research step (my judgement): a filament-curvature probe for `vorticity-lower-bound-argument`.** Ask whether the q-NS pair dynamics generates unbounded curvature at scale $\sqrt{T^*-t}$. Without that, §3.5 shows the argument cannot produce a smooth-solution blowup. A negative answer would be a scope-(a) result worth recording.
3. **Ingest [S1]–[S3]** into `library/` and register `references.ts` keys.

The Lean file is standalone library Lean: it has no content block, and nothing imports it yet.
