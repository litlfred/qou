<!-- FILE_START: braid-involutions-intro.md -->
The braid group carries two canonical involutions: the
twist-flip $\tau$ that swaps adjacent strands and the
$\rho$-conjugation that conjugates each generator by the
half-twist.  This section records both involutions, exhibits the
twist-flip on the trefoil holonomy, and connects the
$\rho$-conjugation to the chirality pairing developed later in
the chapter.
<!-- FILE_END: braid-involutions-intro.md -->

<!-- FILE_START: lagrange-resolvent-transform.md -->
**Proposition.**
Let $C_n$ act on a vector space $V$ of dimension $n$ with
coordinates $x_0, \ldots, x_{n-1}$, and let
$\zeta = e^{2\pi i/n}$.  The **Lagrange resolvent transform**
(discrete Fourier transform on $C_n$) is

$$
  w_k =  \frac{1}{\sqrt{n}}\sum_{j=0}^{n-1}\zeta^{kj}x_j,
  \qquad k \in \{0, \ldots, n-1\}.
$$

Then:

1. The cyclic permutation $\sigma \colon x_j \mapsto x_{j+1}$
   acts diagonally: $\sigma(w_k) = \zeta^{-k} w_k$.  The
   $C_n$ symmetry is manifest as phase rotation of the
   Fourier modes.

2. Any $C_n$-invariant polynomial constraint on the $x_j$
   transforms to a constraint on $C_n$-equivariant
   combinations of the $w_k$ (products pairing $w_k$ with
   $w_{n-k}$, i.e.\ conjugate modes).

For $n = 5$ (the case relevant to
[Bring's surface](#def:brings-surface)), the three power-sum
constraints transform to: $w_0 = 0$ (linear projection),
$w_1 w_4 + w_2 w_3 = 0$ (Hermitian quadric), and
$w_1^2 w_3 + w_4^2 w_2 + w_2^2 w_1 + w_3^2 w_4 = 0$
(symmetric cubic).

**Mathematical Novelty:** While using a Discrete Fourier Transform (DFT) to diagonalize a cyclic action is standard, the explicit $n=5$ Bring-surface formalization with the modular zeta-power reduction is a non-trivial mathematical contribution. (Note that the quadric/cubic constraint transforms mentioned in the examples are stated as part of the framework but not fully formalized).
<!-- FILE_END: lagrange-resolvent-transform.md -->

<!-- FILE_START: braid-twist-flip.md -->
Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple.
Define the two involutions

```tex
\begin{align}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_4,w_3)
    &&\text{(\textbf{twist}),}
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_4,w_3,w_2,w_1)
    &&\text{(\textbf{flip}).}
    \label{eq:braid-flip}
\end{align}
```

As $4\times 4$ permutation matrices these are

```tex
\begin{equation}\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0
  \end{pmatrix}.
\end{equation}
```

On the 4-tuple these involutions generate the Klein four-group
$V_4=\{\mathrm{id},\sigma_1,\sigma_2,\sigma_1\sigma_2\}$, with
$\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$.
<!-- FILE_END: braid-twist-flip.md -->

<!-- FILE_START: holonomy-trefoil.md -->
Given a branched cover $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$ with singular fibres
at the critical values, choose two loops
$\gamma_1,\gamma_2$ in $\mathbb{P}^1(\mathbb{C})$ encircling distinct branch
points.  Parallel-transporting the spectral modes $w_k$ around these
loops yields holonomy operators

```tex
\begin{equation}\label{eq:holonomy-generators}
  H_1=\sigma_1,\qquad H_2=\sigma_2,
\end{equation}
```

where $\sigma_1,\sigma_2$ are the braid generators.
In the $\mathrm{SU}(2)$ embedding ([SU(2) generators](#def:su2-generators)) these
become

$$
  H_1=\exp(T\varTheta e_1),\qquad H_2=\exp(T\varTheta e_2),
$$

with $T$ the geometric torsion scalar and $\varTheta$ a branch angle, so
the holonomy group is a representation of $B_3$ inside
$\mathrm{SU}(2)$.

The fundamental group of the trefoil-knot complement admits the
presentation $\langle x,y\mid xyx=yxy\rangle$, which is exactly
$B_3$.  The assignment
$x\mapsto H_1$, $y\mapsto H_2$ is therefore an isomorphism
$\pi_1(S^3\setminus K_{3,2})\xrightarrow{ \sim } \langle H_1,H_2\rangle$: the monodromy group of the branched cover
*is* the trefoil-knot group.

The composite holonomy
$H_1 H_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$ is the
$3$-cycle $\alpha$ and satisfies
$(H_1 H_2)^3=\mathrm{id}$ on $\mathrm{SO}(3)$.
<!-- FILE_END: holonomy-trefoil.md -->

<!-- FILE_START: rho-s3-holonomy-exposition.md -->
Before encountering $\rho$ in the equations that follow, it is worth
pausing to understand what this representation *does* geometrically.

The representation $\rho \colon B_3 \to \mathrm{SU}(2)$ is the exact
holonomy of the symmetric group $S_3$ acting on the branched cover
$\mathcal{S} \to \mathbb{P}^1(\mathbb{C})$. That is, $\rho$ encodes
how the spectral modes $w_k$ --- the Lagrange resolvents defined by the
discrete Fourier transform on $C_5$
([Lagrange resolvents](#prop:lagrange-resolvent-transform)) --- are
physically permuted when one transports them around the branch points of
the cover.

The chiral sheets of the geometry are defined by these spectral
coordinates: the conjugate pairs $(w_1, w_4)$ and $(w_2, w_3)$ span
two-dimensional eigenspaces of the cyclic action, and together they
tile the four non-trivial modes of the fibre into time-like and
space-like sectors. The representation $\rho$ acts on these sheets
through two elementary operations:

1. **The $\alpha$ operator (twist).**
   The generator $\sigma_1$ ([braid twist](#def:braid-twist-flip))
   swaps the two conjugate pairs: $(w_1, w_2, w_3, w_4) \mapsto (w_2, w_1, w_4, w_3)$. In the $\mathrm{SU}(2)$ embedding this is
   a rotation by $T\varTheta$ around the $e_1$ axis
   ([SU(2) generators](#def:su2-generators)). Physically, $\alpha$
   rotates the *time-like* pairs --- the modes that carry the
   dynamical phase of the Reeb flow --- while leaving the overall
   chirality unchanged.

2. **The $\beta$ operator (flip).**
   The generator $\sigma_2$ reverses the full tuple:
   $(w_1, w_2, w_3, w_4) \mapsto (w_4, w_3, w_2, w_1)$. In
   $\mathrm{SU}(2)$ this is a rotation around $e_2$, which acts as a
   *reflection of the space-like axis*. The flip exchanges the two
   chirality sectors, implementing the geometric analog of parity
   inversion.

Together, $\alpha$ and $\beta$ generate the Klein four-group $V_4$
acting on the resolvent tuple, and their composition
$\alpha\beta \colon \mathbf{w} \mapsto (w_3, w_4, w_1, w_2)$ is the
$3$-cycle whose cube returns to the identity on $\mathrm{SO}(3)$
([holonomy generators](#rem:holonomy-trefoil)). The full
$S_3$ holonomy is therefore the group generated by these rotations and
reflections of the chiral sheets.

The upshot is concrete: whenever $\rho$ appears in the braid-group
representations and knot invariants below, it is acting by *twisting
the time-like modes and reflecting the space-like axis* of the spectral
geometry. This visual anchor --- a rotation--reflection pair on the
chiral sheets --- is the physical content of the abstract topological
symmetry.
<!-- FILE_END: rho-s3-holonomy-exposition.md -->

