**Remark (§3b-cond Lean classes for the four remaining mass-tower
open problems).**

After the α_EM derivation chain
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)
$\to$ [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
$\to$ [`conj:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition),
four structural gaps remain in the mass-tower derivation. The Lean
file [`mass-tower-open-problems-classes.lean`](mass-tower-open-problems-classes.lean)
consolidates them as typeclasses in the §3b-cond pattern, each with
a sorry-free conditional theorem reducing the conjectural form to
a class instance.

## The four classes

### 1. `Term7ShellCorrectionClass`

**Open problem.** The unified six-term mass formula under-predicts
isotope masses for $A \geq 5$ by $\sim 10\%$. Term 7
(`conj:shell-correction-term-seven`)
adds a shell correction with coefficient $\alpha_5$ currently fit to
the AME panel, not derived. The class
`Term7ShellCorrectionClass` asserts the existence of a structural
derivation from the Gröbner-Shirshov filtration spectral sequence at
height-6 partitions ($\ell = 5$).

**Conditional theorem.** `term7_structural` — given the class,
$\alpha_5$ is a categorical-derivation output, not a phenomenological
extension.

### 2. `ChiralityFactorClass`

**Open problem.** The deuterium chirality factor $a_K = 1 + h$ (with
$h = q - q^{-1}$) is recorded as a paper-empirical ansatz; a numerical
probe failed to match against eight candidate writhe-ribbon formulas.
[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
proposes a Kauffman-framing derivation. The strengthened class
`ChiralityFactorClass` axiomatises that derivation: it asserts the
existence of a function $a_K(h, w, \langle c \rangle)$ and an error term
such that $a_K = 1 + w \cdot \langle c \rangle \cdot h + O(h^2)$,
encoding the structural first-order Kauffman expansion.

**Conditional theorem.** `chirality_factor_structural` — sorry-free
reduction of the chirality ansatz to the class instance.

### 3. `ZHabiroConvergenceClass`

**Open problem.** The brane-tower per-generator volumes
$z_i = |\hat{V}_i|$ for low isotopes lie just below the
first pole of $\Phi_q$ at $z = q_0 \approx 1.11$
([`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)). Each
summand is enormous and the analytic infinite-product diverges; two
regularisations (Yekutieli finite-slice, $q$-Habiro completion) have
been documented but neither uniformly closes the gap. The strengthened
class `ZHabiroConvergenceClass` axiomatises a uniform bound on the
regularised tower sum, formally asserting $\forall z < q_0, \sum \Phi_q(z) \leq M$
for some $M < q_0$.

**Conditional theorem.** `brane_tower_finite` — given the class,
the brane-tower contribution is finite for every isotope-relevant
volume.

### 4. `AlphaOver4PiClass`

**Open problem.** The additive Bring zero-mode form gives residual
$-4.2 \times 10^{-6}$ at the $2/(3\pi)$ order; the next-order
self-energy correction $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$
brings it to $+5.7 \times 10^{-8}$
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
The coefficient $1/(4\pi)$ is currently a near-match (1.4% off) and
may refine to $1/(2\pi[2]_q)$ or another $q$-correction, but its
structural origin is conjecturally a multivariate polylogarithm
regulator on a higher Bloch group $B_n(\mathbb{C})$, $n \geq 3$
[`borel1974`, `bloch2000`]. The strengthened class `AlphaOver4PiClass`
axiomatises the higher-Bloch-group origin of the next-order
coefficient by asserting the existence of a higher Bloch group type, a
regulator, and an element mapping exactly to $\alpha/(4\pi)$.

**Conditional theorem.** `alpha_over_4pi_structural` — given the
class, the next-order coefficient is a regulator output, not an
empirical fit.

## Pattern

Each of the four classes follows the §3b-cond template established
by [`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):

1. **Carrier definition** — the target real or function (e.g.
   $\alpha_5 \in \mathbb{R}$, $a_K(h, w) \in \mathbb{R}$, the
   uniform bound $M$, $\alpha/(4\pi)$).
2. **Class** — a `Prop`-valued typeclass asserting the existence
   of the structural derivation as a single field.
3. **Conditional theorem** — sorry-free Lean theorem taking the
   class as `[Instance]` and unpacking the existential.

Closure of the four class instances is the irreducible open
content remaining in the mass-tower derivation. None requires new
mathematical machinery beyond what is documented in the cited
upstream blocks; each requires the explicit categorical /
geometric derivation written out in full.
