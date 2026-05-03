### Statement

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate
parameter $q$, let $\beta \in B_n$ be a braid, and let
$\rho_q = 1/\hbar_q^2$ be the substrate density
([quantum Planck constant](#def:quantum-planck-constant)).
For each non-empty $S \subseteq \{0, \dots, n-2\}$ with
$\lvert S \rvert \leq 2$, let $K_S$ be the Φ$_q$-piece of $\beta$
([Φ$_q$-piece](#def:phi-q-piece)) and let
$V_S := \prod_{i \in S}\hat{V}_i^{\mathrm{full}}$ be the per-block
spectral coordinate
([mass endomorphism tower](#prop:mass-endomorphism-tower)).

#### Algebraic-side prerequisite

The **algebraic** content of "JSJ stratification" — a partition of
the mass-tower formula into level-$|S|$ summands in
$J^{|S|}/J^{|S|+1}$ of the GS confinement filtration — is stated
in full generality by
[`prop:phi-q-tower-algebraic-stratification`](#prop:phi-q-tower-algebraic-stratification).
That proposition is **unconditional**: it lives entirely in
$H_n(R, q)$ over $\mathbb{Q}(q^{1/2})$, makes no reference to
$\tau$, hyperbolic volume, or 3-manifold pieces, and uses the
**Frobenius norm** $\|\cdot\|_F$ valued in the ground ring (not
the Archimedean absolute value).

The conjecture below — and *only* the conjecture — crosses the
Archimedean wall by identifying that algebraic stratification
with the geometric JSJ under $\tau_{\mathrm{arch}}$.

**Conjecture (Φ$_q$–JSJ archimedean bridge).** Under the archimedean
realisation $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization))
each summand of the dilogarithm form of the tower equals $\rho_q$ times
the hyperbolic volume of the corresponding Φ$_q$-piece,

$$
  \tau_{\mathrm{arch}}\!\bigl(z^{\lvert S\rvert} \cdot \Phi_q(\lvert V_S\rvert)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S),
  \qquad
  1 \leq \lvert S \rvert \leq 2,
$$

and the descended summand $\bigl\lvert\prod_i \hat{V}_i\bigr\rvert$
realises archimedeanly to the holonomy term
$\rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_\emptyset)$.
Summing over $S$ yields

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}(\varrho)\bigr)
  \;=\;
  \rho_q \cdot
  \!\!\sum_{\substack{S \subseteq \{0,\dots,n-2\} \\ 0 \leq \lvert S\rvert \leq 2}}\!\!
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S).
$$

After identifying the family $\{K_S\}_S$ (modulo
small-piece collapse) with the JSJ decomposition
$\mathrm{JSJ}(K)$ of $K = \widehat{\beta}$, the right-hand side
coincides with the JSJ piecewise sum
$\sum_{P \in \mathrm{JSJ}(K)} \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)$
that drives the canonical binding-energy pipeline.

### Why this matters (rather than deprecating Φ$_q$)

The conjecture says the **dilog form** and the **hyperbolic-volume
form** of the tower are not two competing engines: they are two
presentations of the same archimedean number, evaluated through two
different convergence schemes.

- **JSJ pipeline.** For each piece $P$, evaluate
  $\mathrm{Vol}_{\mathrm{hyp}}(P)$ numerically with SnapPy. Fast on
  finished hyperbolic atoms; opaque internally.
- **Φ$_q$ pipeline.** For each $S$, evaluate
  $\Phi_q(\lvert V_S \rvert)$ as a Laurent polynomial in $q^{1/2}$.
  Slower convergence (the Kashaev limit is logarithmic), but yields a
  closed-form, $q$-differentiable expression per generator and per
  pair.

The bridge predicts that the two engines compute the same atomic-mass
target, and explains the empirical 0.15% Φ$_q$ floor on $D$ as a
**Kashaev-convergence floor**, not a model floor. Phase 2 of the
1ppb handover (pentagon-defect expansion) is intrinsically a
Φ$_q$ computation — the pentagon identity is the Φ$_q$ five-term
relation — so the dilog form earns its keep as a *theoretical* tool
while JSJ remains the numerical workhorse.

### Conditional Lean theorem

Per `CLAUDE.md` §3b, this conjecture is downstream of
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture) and
therefore cannot be a `theorem`/`proposition` block. The
sibling `.lean` file states it as a Lean theorem **conditional on a
typeclass instance**:

```
theorem bridge {q : ℝ} [Kashaev.VolumeConjecture q]
    (β : Braid) :
    -- archimedean realisation of the dilog form
    -- equals ρ_q · Σ_S Vol(K_S)
    ...
```

The Lean theorem is fully verified modulo the `VolumeConjecture`
typeclass instance, so the only mathematical input that remains
unproved is KVC itself — exactly the same mathematical content as
the conjecture above.

### Required ingredients (to be filled in incrementally)

1. **Single-crossing case** ($\lvert S \rvert = 1$). The Kashaev limit
   of a single-crossing piece is a one-bridge knot complement; its
   hyperbolic volume realises $\Phi_q(\lvert\hat{V}_i\rvert)$. The
   single-crossing identity is the smallest non-trivial instance of
   KVC and is the base case of the bridge.

2. **Adjacent-pair case** ($\lvert S \rvert = 2$). The pair piece
   $K_{\{i, i+1\}}$ is a two-bridge knot whose hyperbolic volume
   realises $z^2 \cdot \Phi_q(\lvert\hat{V}_i \hat{V}_{i+1}\rvert)$.
   The Markov weight $z^2$ on the algebraic side reproduces the
   gluing weight on the JSJ side, governed by the
   [pentagon UV commutation](#prop:pentagon-uv-commutation) relation.

3. **Descended (level-zero) carrier.** The empty piece $K_\emptyset$
   carries the descended summand
   $\bigl\lvert\prod_i \hat{V}_i\bigr\rvert$
   ([descended-level-zero](#prop:descended-level-zero)).

4. **JSJ identification.** Modulo collapse of Seifert-fibered small
   pieces, the family $\{K_S\}$ realises $\mathrm{JSJ}(K)$ with
   weights matching $\rho_F$ on the JSJ side. This step is the
   formal bridge between the **algebraic JSJ** (the
   $J^\bullet$-graded stratification of $H_n(q)$ described in the
   *Algebraic-side statement* above) and the geometric JSJ
   decomposition of $S^3 \setminus \widehat\beta$. The
   algebraic JSJ is intrinsic to the Hecke side and is not
   derived from the geometric JSJ; the conjecture is precisely
   that $\tau_{\mathrm{arch}}$ pushes one to the other.

The first two ingredients are conditional on KVC at the per-piece
level; the third is a categorical statement
([descended-level-zero](#prop:descended-level-zero)); the fourth is
a JSJ-theoretic identification, conjectural until each
small-piece collapse is verified.

### Motivic dictionary

The bridge admits a clean motivic reading: the algebraic side
$\Phi_q(\lvert V_S\rvert)$ is a class in the quantum Bloch group
$\mathcal{B}_q$ ([quantum Bloch group](#rem:quantum-bloch-group)), the
archimedean realisation $\tau_{\mathrm{arch}}$ is the $q$-deformed
Borel/Beilinson regulator, and the right-hand side is the standard
Neumann–Zagier decomposition of the volume of $S^3 \setminus K$ along
its hyperbolic pieces [`neumann-zagier1985`, `zagier1986`]. In this
language the conjecture is the statement that

- the quantum Bloch class $[\Phi_q(\lvert V_S\rvert)]$ regulates
  archimedeanly to the volume of the corresponding Φ$_q$-piece, and
- the Φ$_q$ stratification $\{K_S\}_S$ realises the JSJ stratification
  with regulator weights matching $\rho_F$.

The $\rho_q$ prefactor on the right-hand side is the substrate-density
normalisation that converts a regulator output (a real number) into a
mass density on the brane. Phrased this way, the dilog form and the
hyperbolic-volume form are not two competing engines but two
presentations of the same regulator, evaluated through two
convergence schemes.
