A strict $2$-group is equivalently a *crossed module*: a
group homomorphism $\partial \colon H \to G$ together with an
action of $G$ on $H$ satisfying the Peiffer identity. The
associated exact sequence

```tex
\begin{equation}\label{eq:crossed-module-ses}
\begin{tikzcd}[column sep=2em]
  1 \ar[r]
  & \ker\partial \ar[r]
  & H \ar[r, "\partial"]
  & G \ar[r]
  & \mathrm{coker}\partial \ar[r]
  & 1
\end{tikzcd}
\end{equation}
```

encodes the $2$-group as a homotopy type with
$\pi_0 = \mathrm{coker}\partial$ and
$\pi_1 = \ker\partial$.

The *inner-automorphism $2$-group*
$\mathrm{INN}(G) = (G \xrightarrow{\mathrm{id}} G)$
has $\ker\partial = 1$ and $\mathrm{coker}\partial = 1$, so it is
connected and connected as a $2$-group. A $2$-connection for
$\mathrm{INN}(G)$ on a principal $2$-bundle over $M$ consists of a
$\mathfrak{g}$-valued $1$-form $A$ and a $\mathfrak{g}$-valued
$2$-form $B$, subject to the *:refterm[quantum flatness]{#quantum-flatness}* condition

$F_A =  B.$

In the QOU setting, $G = \mathrm{SU}(2)$ and the Levi distribution
$H = \ker\varTheta$ has $\dim_{\mathbb{R}} H = 4$, so the Hodge
decomposition $\Lambda^2 H^* = \Lambda^+\!H^* \oplus \Lambda^-\!H^*$
is available. Imposing the *simplicity constraint*

$B  \in  \Gamma\!\bigl(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)\bigr)$

\--- that is, requiring the $2$-form datum to be self-dual ---
and combining with :refterm[quantum flatness]{#quantum-flatness} gives
the commutative diagram

```tex
\begin{equation}\label{eq:2group-instanton}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^1(M,\mathfrak{g})
    \ar[r, "d_A"]
  & \Omega^2(M,\mathfrak{g})
    \ar[r, "\pi^+"]
  & \Omega^{2,+}(M,\mathfrak{g})
  \\
  & F_A \ar[u, "=B"]
    \ar[r, equal]
  & F_A^+ \ar[u, "\text{simplicity}"']
\end{tikzcd}
\end{equation}
```

The :refterm[quantum flatness]{#quantum-flatness} condition $F_A = B$ combined with the simplicity
constraint $B = F_A^+$ forces $F_A = F_A^+$, hence $F_A^- = 0$.
This is precisely the instanton equation
$F_A|_H = {*_H}F_A|_H$
of [instanton](#def:instanton). Thus, the self-dual formulation
used throughout this paper is a special case of $2$-group gauge theory
for $\mathrm{INN}(\mathrm{SU}(2))$ subject to a simplicity constraint
on the $2$-form datum.

This perspective clarifies the relationship between the instanton
condition in Chapter 1 and the higher-categorical structures of later
chapters: the parallel-transport $2$-functor of the
$\mathrm{INN}(\mathrm{SU}(2))$ $2$-bundle assigns to paths in $M$
not only group elements in $\mathrm{SU}(2)$ but $2$-morphisms
encoding the self-dual curvature, with the simplicity constraint
selecting the physical (instanton) sector.
