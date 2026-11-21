The Dimofte–Gaiotto–Gukov 3d–3d correspondence maps a hyperbolic 3-manifold $M^3$ to a 3d $\mathcal{N}{=}2$ gauge theory $T[M^3]$. The partition function $Z_{T[M^3]}(q)$ on a squashed 3-sphere $S^3_b$ equals the state-integral invariant of $M^3$ constructed from the quantum dilogarithm $\Phi_q$. Applied to the Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$, the 3d–3d theory $T[\mathbf{S}^3 \setminus \mathcal{B}_3]$ yields a partition function whose $h^4$ coefficient matches the framework's Markov-trace coefficient $h^4 = -3/4$.

## Significance

The 3d–3d correspondence gives the framework a **gauge-theory
realisation** of every hyperbolic-3-manifold mass formula.
Concretely, the Borromean coefficient $h^4 = -3/4$ is expected to
reappear as the four-loop perturbative contribution to
$Z_{T[\mathcal{B}_3]}$, and the framework's **dimensionless** Borromean
dressing as the value of that partition function at $q_0$:

| Framework side | 3d gauge theory side |
|----------------|----------------------|
| $\mathcal{B}_3$ (Borromean rings complement) | $T[\mathcal{B}_3]$ — a 3d $\mathcal{N}{=}2$ theory |
| the dimensionless Borromean dressing $F_{\mathcal{B}} = \lvert\mathrm{tr}_M(\beta_{\mathcal{B}})\rvert\,[3]_q!/q^3$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
| $h^4 = -3/4$ Markov-trace coefficient | 4-loop perturbative contribution to $Z_{T[\mathcal{B}_3]}$ |

The middle row is not $m_p \leftrightarrow Z_{T[\mathcal{B}_3]}(q_0)$,
an **absolute** proton mass in MeV as the value of the partition function.
That form is excluded for two independent reasons. The framework the framework no longer claims, targets, or scores an absolute
nucleon mass as a prediction: absolute mass is $\mathfrak{m}_e$ times a
dimensionless ratio, and $\mathfrak{m}_e$ is the calibration that fixes the MeV
scale, so the MeV figure carries no content beyond the ratio. Independently of
that, a partition function is a **dimensionless** number, so setting it
equal to a quantity carried in MeV was never dimensionally coherent.

**What is not settled, and is not settled here:** *which* dimensionless
Borromean quantity the correspondence should be tested against. $F_{\mathcal{B}}$
is the natural candidate because it is the dimensionless factor that dresses the
muon anchor in the canonical nucleon relation, but no normalisation of
$Z_{T[\mathcal{B}_3]}$ has been matched to it. The row above states the
comparison the correspondence *ought* to make, not one that has been made — the
$h^4$ row remains the block's only quantitatively pinned claim.

This is **mirror symmetry** in the sense that the framework's mass
formula and a quantum-field-theory partition function on a curved
spacetime are two computations of the same hyperbolic invariant.

## Structural position

- **GB filtration.** None: the duality is at the partition-function
  / observable level, not at a specific Hecke-element level.
- **Jet order.** All orders: the partition function has a full $q$ /
  perturbative expansion, and the $h^4$ coefficient corresponds to a
  specific perturbative order in the gauge theory.
- **Bar-symmetry.** Depends on the gauge theory side; for
  $\mathcal{N}{=}2$ theories with a real-mass parameter, the
  bar-symmetry corresponds to the parity-reversal of the squashed
  3-sphere $S^3_b \to S^3_{1/b}$.

## Which theory the DGG construction produces (literature)

The construction cited in Open Question 1 does not by itself produce the theory the dictionary above assumes. For a knot complement $N$ the theory $T^{DGG}[N]$ built from an ideal triangulation has as its vacua only a subset of the irreducible flat $SL(2,\mathbb{C})$ connections on $N$, because a triangulation captures only part of the character variety; it therefore describes a subsector of the six-dimensional theory $T^{6d}[N]$, not all of it, and generically carries only a $U(1)$ flavour symmetry where $T^{6d}$ carries $su(2)$ \cite[\S2.3]{arxiv-1803.04009v2}. The same source gives a topological criterion for when that $U(1)$ enhances to $SU(2)$ or $SO(3)$ \cite[\S3]{arxiv-1803.04009v2}, and identifies the field-theoretic operation that corresponds to Dehn filling, which builds theories for closed $3$-manifolds \cite[\S4.1]{arxiv-1803.04009v2}. All three statements are made for a $3$-manifold with a single torus boundary. The Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$ has three cusps, so whether the criterion or the filling operation transfers to it has not been checked, and the equality of partition functions stated at the top of this block should be read as holding at most for the subsector that $T^{DGG}$ realises.

## Open questions

1. Identify the 3d $\mathcal{N}{=}2$ theory $T[\mathcal{B}_3]$
   explicitly (Dimofte–Gaiotto–Gukov 2014 provides the construction).
   The DGG theory realises only part of the flat $SL(2,\mathbb{C})$
   connections as vacua, and the closing (Dehn-filling) operation on it is
   identified in \cite{arxiv-1803.04009v2} (§2.3, §4.1); both are stated for a
   single torus boundary, while $\mathcal{B}_3$ has three cusps.
2. Cross-check the $h^4 = -3/4$ coefficient as a 4-loop contribution
   in $T[\mathcal{B}_3]$ partition function.
3. Closing the conjecture remains distant: the QFT-side
   formalisation it would require has not been developed.

## Cross-references

- [Borromean rings represent a non-trivial element of $K_3(\mathbb{C})$ / Bloch group with regulator $r_2 = 8G$](../mass-theory/borromean-bloch-group-element.md)
  — K-theoretic regulator parallel
- [Kashaev volume conjecture](../mass-theory/kashaev-volume-conjecture.md)
  — Volume Conjecture is the leading-order 3d–3d statement
- [Dimofte–Gaiotto–Gukov 2014; Terashima–Yamazaki 2011]
