The Hopf algebra $\mathcal{O}_q(\mathrm{SU}(2))$ carries a natural
*Frobenius structure*: the Haar state
$h_q \colon \mathcal{O}_q \to \mathbb{C}$ induces a non-degenerate
pairing $\langle a, b \rangle = h_q(ab)$, making $\mathcal{O}_q$ into
a Frobenius algebra with comultiplication $\Delta_\mu$ dual to the
multiplication. This Frobenius comultiplication is compatible with the
Hopf comultiplication $\Delta_q$ of the coassociativity diagram and
satisfies the *Frobenius relation*:

```tex
\begin{equation}\label{eq:frobenius-relation-elab}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu"]
    \ar[d, "\mathrm{id} \otimes \Delta_\mu"']
  & \mathcal{O}_q
    \ar[d, "\Delta_\mu"]
  \\
  \mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu \otimes \mathrm{id}"']
  & \mathcal{O}_q \otimes \mathcal{O}_q
\end{tikzcd}
\end{equation}
```

where $\mu$ is the algebra multiplication and $\Delta_\mu$ the
Frobenius comultiplication (dual to $\mu$ under the Haar pairing).
The non-degeneracy of $h_q$ is expressed by requiring the composite

```tex
\begin{equation}\label{eq:frobenius-nondegen}
\begin{tikzcd}[column sep=3em]
  \mathcal{O}_q \otimes \mathcal{O}_q
    \ar[r, "\mu"]
  & \mathcal{O}_q
    \ar[r, "h_q"]
  & \mathbb{C}
\end{tikzcd}
\end{equation}
```

to be a perfect pairing, i.e. the induced map
$\mathcal{O}_q \to \mathcal{O}_q^*$ is an isomorphism.

This Frobenius--Hopf structure on $\mathcal{O}_q(\mathrm{SU}(2))$ is
precisely the datum required by the general
[quantum universe](#def:quantum-universe): the Haar state $h_q$ realises
the Frobenius form $\int_A \colon A \to \mathbf{1}$, and the
non-degeneracy is the $\mathbb{C}$
instance of condition (1) in
[quantum observable universe](#def:quantum-observable-universe).
In the archimedean realisation ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)),
the $4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$ and the two analytic vanishing
conditions of [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)
reduce to a triple:

1. a CR manifold $(M, \varTheta)$ of hypersurface type with
   non-degenerate Levi form;
2. a non-degenerate Frobenius--Hopf object $A$ in the monoidal
   category of vector bundles over $M$, playing the role of
   $(G, \mathcal{S})$; and
3. an instanton connection on the underlying $A$-bundle
   ([instanton](#def:instanton)).

The vanishing condition $H^0(M, \mathrm{Ad}(P)) = 0$ then follows from
the non-degeneracy of the Frobenius form $\int_A$ via the diagram

```tex
\begin{equation}\label{eq:frobenius-vanishing}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \mathrm{Ad}(A) \otimes \mathrm{Ad}(A)
    \ar[r, "\mu_{\mathrm{Ad}}"]
    \ar[d, "\text{global sections}"']
  & \mathrm{Ad}(A)
    \ar[r, "\int_{A,\mathrm{Ad}}"]
  & \mathcal{O}_M
    \ar[d, "\textstyle\int_M"]
  \\
  H^0(M,\mathrm{Ad}(A)) \otimes H^0(M,\mathrm{Ad}(A))
    \ar[rr, "\text{pairing}"']
  & & \mathbb{C}
\end{tikzcd}
\end{equation}
```

The adjoint representation $\mathrm{Ad}(A)$ inherits a non-degenerate
[Frobenius pairing](#def:frobenius-pairing) from $\int_A$; any global parallel section would
pair non-trivially with itself, contradicting the irreducibility of
the instanton connection
([irreducible connection](#lem:irreducible-connection)). Hence the Frobenius
non-degeneracy, combined with irreducibility, forces
$H^0(M, \mathrm{Ad}(A)) = 0$. The section-vanishing condition
$\Gamma_c(M, \mathcal{S}) = 0$ follows similarly from the non-existence of
$A$-equivariant sections of the associated $\mathbb{P}^1(\mathbb{C})$-bundle.

Note that the horizontal distribution $H = \ker\varTheta$ itself
*fails* to carry a Frobenius structure (as discussed in
[$q$-torsion existence](#rem:q-torsion-existence)); it is the gauge algebra, not the
distribution, that is Frobenius.
