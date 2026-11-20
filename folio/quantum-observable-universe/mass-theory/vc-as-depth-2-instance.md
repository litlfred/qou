**Remark (Volume Conjecture as the depth-2 instance of the GS $\leftrightarrow$
period correspondence).**

The Kashaev–Murakami–Murakami volume conjecture
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture))
admits a clean structural reading inside the graded-Mikusiński
framework
([GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence)):
*it is the depth-2 case.*

### One-line statement

$$
  \text{Volume Conjecture} \;\;\Longleftrightarrow\;\;
  \tau_{\mathrm{arch}}\!\left( G^{(2)}(\mathcal{H}_q) \right)
  \;\xrightarrow{\;\;}\;
  \mathcal{P}_2 \big/ \mathcal{P}_1
  \;=\; \{\text{hyperbolic 3-manifold volumes}\}.
$$

### Justification of the reading

The Volume Conjecture asserts that the asymptotic growth of the
coloured Jones polynomial $J_K^{(N)}(q)$ at $q = e^{2\pi i / N}$ as
$N \to \infty$ equals $\mathrm{Vol}(S^3 \setminus K)$. The
algebraic side ($J_K \in \mathbb{Z}[q^{\pm 1}]$) is field-polymorphic
and lives in the substrate. The
geometric side is a real number, transcendental in general.

In graded-Mikusiński terms:

- $J_K^{(N)}$ is built by repeated application of the depth-2
  grouplike $\mathrm{Li}_2^q$ (Faddeev–Kashaev quantum-dilogarithm
  decomposition).
- The asymptotic limit at $q = e^{2\pi i / N}$, $N \to \infty$, is
  the archimedean realization $\tau_{\mathrm{arch}}$ followed by
  std-part on the surreal envelope.
- Single-$\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral
  depth 2 $\Rightarrow$ Goncharov period-class
  $\mathcal{P}_2 / \mathcal{P}_1$ (Bloch regulator
  $K_3^{\mathrm{ind}}(\overline{\mathbb{Q}}) \otimes \mathbb{Q}
  \to \mathbb{R} / \pi^2 \mathbb{Q}$).

The Volume Conjecture is therefore not a coincidence: hyperbolic
volumes appear at depth 2 because that is structurally where the
Bloch–Wigner regulator lives. Predicted at every depth $n$ is an
analogous statement: *colored quantum invariants built from
$\mathrm{Li}_n^q$ asymptote to weight-$n$ Goncharov periods.*

### Implications of accepting the depth correspondence

The depth correspondence does **not** prove the Volume Conjecture.
What it does is reduce the conjecture to two structurally smaller
claims:

1. *Categorical Laplace transport.* Show that the asymptotic at
   roots of unity coincides with the categorical Laplace transform
   of $\Phi_q$ followed by std-part — i.e. that the limiting
   procedure is intrinsically the Mikusiński transform applied
   stratum-by-stratum. Already partially in the paper via
   [Uniqueness of the categorical Laplace transform](#prop:categorical-laplace-unique).
2. *Sharpness at depth 2.* Show that the image of $G^{(2)}$ in
   $\mathcal{P}_2 / \mathcal{P}_1$ contains the Bloch–Wigner
   regulator class of every hyperbolic knot complement. This is the
   modern formulation of Bloch's 1978 conjecture and is a known
   target in motivic cohomology.

The framework thus does not eliminate the open problem — it places
it in its correct depth-graded category, where partial results
already exist (Murakami–Murakami 2001 for the figure-8;
Garoufalidis–Lê for torus knots; many others).

### Cross-reference

For an explicit depth-2 canonical witness on the figure-8 knot
embedded in Bring's genus-4 surface, see
[Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)](#conj:bring-figure-eight-depth-2-witness).
The 50-digit value $2\,\mathrm{Cl}_2(\pi/3) \approx {{ qou.computations.hyperbolic-volumes.data.vol_4_1_decimal_50 | precision: 6 }}\ldots$
is the Bloch regulator class incarnated as a hyperbolic volume.
