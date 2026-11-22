---
doc_id: arxiv-1101.0956v3
doc_title: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES"
section_id: sec-007-4-exterior-differential-calculus
section_title: "Exterior differential calculus"
section_number: 4
pages: 23-36
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.993
doc_brief: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES — In this paper we present the category of generalized Lie algebroids."
---
We propose an exterior differential calculus in the general framework of generalized Lie algebroids. As any Lie algebroid can be regarded as a generalized Lie algebroid, in particular, we obtain a new point of view over the exterior differential calculus for Lie algebroids. Let $\left( \left(
F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta \right) \right)
\in \left\vert \mathbf{GLA}\right\vert$ be.

**Definition 4.1** For any $q\in \mathbb{N}$ we denote by $\left(
\Sigma _{q},\circ \right)$ the permutations group of the set $\left\{
1,2,...,q\right\} .$

**Definition 4.2** We denoted by $\Lambda ^{q}\left( F,\nu ,N\right)$ the set of $q$-linear applications $$\begin{array}{ccc}
\Gamma \left( F,\nu ,N\right) ^{q} & ^{\underrightarrow{\ \ \omega \ \ }} &
\mathcal{F}\left( N\right) \\
\left( z_{1},...,z_{q}\right) & \longmapsto & \omega \left(
z_{1},...,z_{q}\right)
\end{array}$$ such that $$\begin{array}{c}
\omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma \left( q\right)
}\right) =sgn\left( \sigma \right) \cdot \omega \left( z_{1},...,z_{q}\right)
\end{array}$$ for any $z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$ and for any $\sigma \in \Sigma _{q}$.

The elements of $\Lambda ^{q}\left( F,\nu ,N\right)$ will be called *differential forms of degree* $q$ or *differential* $q$*-forms*$.$

*Remark 4.1*** **If $\omega \in \Lambda ^{q}\left(
F,\nu ,N\right)$, then $\omega \left( z_{1},...,z,...,z,...z_{q}\right) =0.$ Therefore, if $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$, then $$\begin{array}{c}
\omega \left( z_{1},...,z_{i},...,z_{j},...z_{q}\right) =-\omega \left(
z_{1},...,z_{j},...,z_{i},...z_{q}\right) .
\end{array}$$

**Theorem 4.1** *If* $q\in N$*, then* $\left( \Lambda
^{q}\left( F,\nu ,N\right) ,+,\cdot \right)$* is a* $\mathcal{F}
\left( N\right)$*-module.*

**Definition 4.3** If $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ and $\theta \in \Lambda ^{r}\left( F,\nu ,N\right)$, then the $\left(
q+r\right)$-form $\omega \wedge \theta$ defined by $$\begin{array}{ll}
\omega \wedge \theta \left( z_{1},...,z_{q+r}\right) & =\underset{\sigma
\left( q+1\right) <...<\sigma \left( q+r\right) }{\underset{\sigma \left(
1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left( \sigma \right)
\omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma \left( q\right)
}\right) \theta \left( z_{\sigma \left( q+1\right) },...,z_{\sigma \left(
q+r\right) }\right) \vspace{3mm} \\
& \displaystyle=\frac{1}{q!r!}\underset{\sigma \in \Sigma _{q+r}}{\tsum }
sgn\left( \sigma \right) \omega \left( z_{\sigma \left( 1\right)
},...,z_{\sigma \left( q\right) }\right) \theta \left( z_{\sigma \left(
q+1\right) },...,z_{\sigma \left( q+r\right) }\right) ,
\end{array}$$ for any $z_{1},...,z_{q+r}\in \Gamma \left( F,\nu ,N\right) ,$ will be called *the exterior product of the forms* $\omega$ *and* $\theta
.$

Using the previous definition, we obtain

**Theorem 4.2** *The following affirmations hold good:*

. *If* $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ * and* $\theta \in \Lambda ^{r}\left( F,\nu ,N\right)$*, then* $$\begin{array}{c}
\omega \wedge \theta =\left( -1\right) ^{q\cdot r}\theta \wedge \omega .
\end{array}
\leqno(4.1)$$

. *For any* $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ *,* $\theta \in \Lambda ^{r}\left( F,\nu ,N\right)$* and* $\eta
\in \Lambda ^{s}\left( F,\nu ,N\right)$* we obtain* $$\begin{array}{c}
\left( \omega \wedge \theta \right) \wedge \eta =\omega \wedge \left( \theta
\wedge \eta \right) .
\end{array}
\leqno(4.2)$$

. *For any* $\omega ,\theta \in \Lambda ^{q}\left( F,\nu
,N\right)$* and* $\eta \in \Lambda ^{s}\left( F,\nu ,N\right)$ * we obtain* $$\begin{array}{c}
\left( \omega +\theta \right) \wedge \eta =\omega \wedge \eta +\theta \wedge
\eta .
\end{array}
\leqno(4.3)$$

. *For any* $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ * and* $\theta ,\eta \in \Lambda ^{s}\left( F,\nu ,N\right)$* we obtain* $$\begin{array}{c}
\omega \wedge \left( \theta +\eta \right) =\omega \wedge \theta +\omega
\wedge \eta .
\end{array}
\leqno(4.4)$$

. *For any* $f\in \mathcal{F}\left( N\right)$, $\omega \in
\Lambda ^{q}\left( F,\nu ,N\right)$ *and* $\theta \in \Lambda
^{s}\left( F,\nu ,N\right)$* we obtain* $$\begin{array}{c}
\left( f\cdot \omega \right) \wedge \theta =f\cdot \left( \omega \wedge
\theta \right) =\omega \wedge \left( f\cdot \theta \right) .
\end{array}
\leqno(4.5)$$

**Theorem 4.3** *If* $$\Lambda \left( F,\nu ,N\right) =\underset{q\geq 0}{\oplus }\Lambda
^{q}\left( F,\nu ,N\right) ,$$ *then* $$\begin{array}{c}
\left( \Lambda \left( F,\nu ,N\right) ,+,\cdot ,\wedge \right)
\end{array}$$ *is a* $\mathcal{F}\left( N\right)$*-algebra.* This algebra will be called *the exterior differential algebra of the vector bundle* $\left( F,\nu ,N\right) .$

*Remark 4.2*If $\left\{ t^{\alpha },~\alpha \in \overline{1,p}\right\}$ is the coframe associated to the frame $\left\{ t_{\alpha },~\alpha \in
\overline{1,p}\right\}$ of the vector bundle $\left( F,\nu ,N\right)$ in the vector local $\left( n+p\right)$-chart $U$, then $$\begin{array}{c}
t^{\alpha _{1}}\wedge ...\wedge t^{\alpha _{q}}\left( z_{1}^{\alpha
}t_{\alpha },...,z_{q}^{\alpha }t_{\alpha }\right) =\frac{1}{q!}\det
\left\Vert
\begin{array}{ccc}
z_{1}^{\alpha _{1}} & ... & z_{1}^{\alpha _{q}} \\
... & ... & ... \\
z_{q}^{\alpha _{1}} & ... & z_{q}^{\alpha _{q}}
\end{array}
\right\Vert ,
\end{array}$$ for any $q\in \overline{1,p}.$

*Remark 4.3*If $\left\{ t^{\alpha },~\alpha \in \overline{1,p}\right\}$ is the coframe associated to the frame $\left\{ t_{\alpha },~\alpha \in
\overline{1,p}\right\}$ of the vector bundle $\left( F,\nu ,N\right)$ in the vector local $\left( n+p\right)$-chart $U$, then, for any $q\in
\overline{1,p}$ we define $C_{p}^{q}$ exterior differential forms of the type $$\begin{array}{c}
t^{\alpha _{1}}\wedge ...\wedge t^{\alpha _{q}}
\end{array}$$ such that $1\leq \alpha _{1}<...<\alpha _{q}\leq p.$

The set $$\begin{array}{c}
\left\{ t^{\alpha _{1}}\wedge ...\wedge t^{\alpha _{q}},1\leq \alpha
_{1}<...<\alpha _{q}\leq p\right\}
\end{array}$$ is a base for the $\mathcal{F}\left( N\right)$-module $$\left( \Lambda ^{q}\left( F,\nu ,N\right) ,+,\cdot \right) .$$

Therefore, if $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$, then $$\begin{array}{c}
\omega =\omega _{\alpha _{1}...\alpha _{q}}t^{\alpha _{1}}\wedge ...\wedge
t^{\alpha _{q}}.
\end{array}$$

In particular, if $\omega$ is an exterior differential $p$-form $\omega ,$ then we can written $$\begin{array}{c}
\omega =a\cdot t^{1}\wedge ...\wedge t^{p},
\end{array}$$ where $a\in \mathcal{F}\left( N\right) .$

**Definition 4.4** If $$\begin{array}{c}
\omega =\omega _{\alpha _{1}...\alpha _{q}}t^{\alpha _{1}}\wedge ...\wedge
t^{\alpha _{q}}\in \Lambda ^{q}\left( F,\nu ,N\right)
\end{array}$$ such that $$\begin{array}{c}
\omega _{\alpha _{1}...\alpha _{q}}\in C^{r}\left( N\right) ,
\end{array}$$ for any $1\leq \alpha _{1}<...<\alpha _{q}\leq p$, then we will say that *the* $q$*-form* $\omega$* is differentiable of* $C^{r}$ *-class.*

**Definition 4.5** For any $z\in \Gamma \left( F,\nu ,N\right)$, the $\mathcal{F}\left( N\right)$-multilinear application $$\begin{array}{c}
\begin{array}{rcl}
\Lambda \left( F,\nu ,N\right) & ^{\underrightarrow{~\ \ L_{z}~\ \ }} &
\Lambda \left( F,\nu ,N\right)
\end{array}
,
\end{array}$$ defined by $$\begin{array}{c}
L_{z}\left( f\right) =\Gamma \left( Th\circ \rho ,h\circ \eta \right)
z\left( f\right) ,~\forall f\in \mathcal{F}\left( N\right)
\end{array}$$ and $$\begin{array}{cl}
L_{z}\omega \left( z_{1},...,z_{q}\right) & =\Gamma \left( Th\circ \rho
,h\circ \eta \right) z\left( \omega \left( \left( z_{1},...,z_{q}\right)
\right) \right) \\
& -\overset{q}{\underset{i=1}{\tsum }}\omega \left( \left( z_{1},...,\left[
z,z_{i}\right] _{F,h},...,z_{q}\right) \right) ,
\end{array}$$ for any $\omega \in \Lambda ^{q}\mathbf{\ }\left( F,\nu ,N\right)$ and $z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right) ,$ will be called *the covariant Lie derivative with respect to the section* $z.$

**Theorem 4.4** *If* $z\in \Gamma \left( F,\nu ,N\right) ,$ $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$* and* $\theta \in
\Lambda ^{r}\left( F,\nu ,N\right)$*, then* $$\begin{array}{c}
L_{z}\left( \omega \wedge \theta \right) =L_{z}\omega \wedge \theta +\omega
\wedge L_{z}\theta .
\end{array}
\leqno(4.6)$$

*Proof.* Let $z_{1},...,z_{q+r}\in \Gamma \left( F,\nu ,N\right)$ be arbitrary. Since $$\begin{array}{l}
L_{z}\left( \omega \wedge \theta \right) \left( z_{1},...,z_{q+r}\right)
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left( \left( \omega
\wedge \theta \right) \left( z_{1},...,z_{q+r}\right) \right) \\
-\overset{q+r}{\underset{i=1}{\tsum }}\left( \omega \wedge \theta \right)
\left( \left( z_{1},...,\left[ z,z_{i}\right] _{F,h},...,z_{q+r}\right)
\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left( \underset{\sigma
\left( q+1\right) <...<\sigma \left( q+r\right) }{\underset{\sigma \left(
1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left( \sigma \right)
\cdot \omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma \left(
q\right) }\right) \right. \\
\qquad \left. \cdot \theta \left( z_{\sigma \left( q+1\right)
},...,z_{\sigma \left( q+r\right) }\right) \right) -\overset{q+r}{\underset{
i=1}{\tsum }}\left( \omega \wedge \theta \right) \left( \left( z_{1},...,
\left[ z,z_{i}\right] _{F,h},...,z_{q+r}\right) \right) \\
=\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) \cdot \Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left(
\omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma \left( q\right)
}\right) \right) \\
\qquad \cdot \theta \left( z_{\sigma \left( q+1\right) },...,z_{\sigma
\left( q+r\right) }\right) +\underset{\sigma \left( q+1\right) <...<\sigma
\left( q+r\right) }{\underset{\sigma \left( 1\right) <...<\sigma \left(
q\right) }{\tsum }}sgn\left( \sigma \right) \cdot \omega \left( z_{\sigma
\left( 1\right) },...,z_{\sigma \left( q\right) }\right) \\
\qquad \cdot \Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left( \theta
\left( z_{\sigma \left( q+1\right) },...,z_{\sigma \left( q+r\right)
}\right) \right) -\underset{\sigma \left( q+1\right) <...<\sigma \left(
q+r\right) }{\underset{\sigma \left( 1\right) <...<\sigma \left( q\right) }{
\tsum }}sgn\left( \sigma \right) \\
\qquad \cdot \overset{q}{\underset{i=1}{\tsum }}\omega \left( z_{\sigma
\left( 1\right) },...,\left[ z,z_{\sigma \left( i\right) }\right]
_{F,h},...,z_{\sigma \left( q+r\right) }\right) \cdot \theta \left(
z_{\sigma \left( q+1\right) },...,z_{\sigma \left( q+r\right) }\right)
\end{array}$$ $$\begin{array}{l}
-\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) \overset{q+r}{\underset{i=q+1}{\tsum }}\omega \left(
z_{\sigma \left( 1\right) },...,z_{\sigma \left( q\right) }\right) \\
\qquad \cdot \theta \left( z_{\sigma \left( q+1\right) },...,\left[
z,z_{\sigma \left( i\right) }\right] _{F,h},...,z_{\sigma \left( q+r\right)
}\right) \\
=\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) L_{z}\omega \left( z_{\sigma \left( 1\right) },...,\left[
z,z_{\sigma \left( i\right) }\right] _{F,h},...,z_{\sigma \left( q+r\right)
}\right) \\
\qquad \cdot \theta \left( z_{\sigma \left( q+1\right) },...,z_{\sigma
\left( q+r\right) }\right) +\underset{\sigma \left( q+1\right) <...<\sigma
\left( q+r\right) }{\underset{\sigma \left( 1\right) <...<\sigma \left(
q\right) }{\tsum }}sgn\left( \sigma \right) \overset{q+r}{\underset{i=q+1}{
\tsum }}\omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma \left(
q\right) }\right) \\
\qquad \cdot L_{z}\theta \left( z_{\sigma \left( q+1\right) },...,\left[
z,z_{\sigma \left( i\right) }\right] _{F,h},...,z_{\sigma \left( q+r\right)
}\right) \\
=\left( L_{z}\omega \wedge \theta +\omega \wedge L_{z}\theta \right) \left(
z_{1},...,z_{q+r}\right)
\end{array}$$ it results the conclusion of the theorem. *q.e.d.*

**Definition 4.6** For any $z\in \Gamma \left( F,\nu ,N\right)$, the $\mathcal{F}\left( N\right)$-multilinear application $$\begin{array}{rcl}
\Lambda \left( F,\nu ,N\right) & ^{\underrightarrow{\ \ i_{z}\ \ }} &
\Lambda \left( F,\nu ,N\right) \\
\Lambda ^{q}\left( F,\nu ,N\right) \ni \omega & \longmapsto & i_{z}\omega
\in \Lambda ^{q-1}\left( F,\nu ,N\right) ,
\end{array}$$ where $$\begin{array}{c}
i_{z}\omega \left( z_{2},...,z_{q}\right) =\omega \left(
z,z_{2},...,z_{q}\right) ,
\end{array}$$ for any $z_{2},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$, will be called the *interior product associated to the section* $z.$

For any $f\in \mathcal{F}\left( N\right)$, we define $\ i_{z}f=0.$

*Remark 4.4*** **If $z\in \Gamma \left( F,\nu ,N\right) ,$ $\omega \in$ $\Lambda ^{p}\left( F,\nu ,N\right)$ and $U$ is an open subset of $N$ such that $z_{|U}=0$ or $\omega _{|U}=0,$ then $\left(
i_{z}\omega \right) _{|U}=0.$

**Theorem 4.5** *If* $z\in \Gamma \left( F,\nu ,N\right)$*, then for any* $\omega \in$* *$\Lambda ^{q}\left( F,\nu ,N\right)$ * and* $\theta \in$* *$\Lambda ^{r}\left( F,\nu ,N\right)$ * we obtain* $$\begin{array}{c}
i_{z}\left( \omega \wedge \theta \right) =i_{z}\omega \wedge \theta +\left(
-1\right) ^{q}\omega \wedge i_{z}\theta .
\end{array}
\leqno(4.7)$$

*Proof.* Let $z_{1},...,z_{q+r}\in \Gamma \left( F,\nu ,N\right)$ be arbitrary. We observe that $$\begin{array}{l}
i_{z_{1}}\left( \omega \wedge \theta \right) \left( z_{2},...,z_{q+r}\right)
=\left( \omega \wedge \theta \right) \left( z_{1},z_{2},...,z_{q+r}\right)
\\
=\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) \cdot \omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma
\left( q\right) }\right) \cdot \theta \left( z_{\sigma \left( q+1\right)
},...,z_{\sigma \left( q+r\right) }\right) \\
=\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{1=\sigma \left( 1\right) <\sigma \left( 2\right) <...<\sigma \left(
q\right) }{\tsum }}sgn\left( \sigma \right) \cdot \omega \left(
z_{1},z_{\sigma \left( 2\right) },...,z_{\sigma \left( q\right) }\right)
\cdot \theta \left( z_{\sigma \left( q+1\right) },...,z_{\sigma \left(
q+r\right) }\right) \\
+\underset{1=\sigma \left( q+1\right) <\sigma \left( q+2\right) <...<\sigma
\left( q+r\right) }{\underset{\sigma \left( 1\right) <...<\sigma \left(
q\right) }{\tsum }}sgn\left( \sigma \right) \cdot \omega \left( z_{\sigma
\left( 1\right) },...,z_{\sigma \left( q\right) }\right) \cdot \theta \left(
z_{1},z_{\sigma \left( q+2\right) },...,z_{\sigma \left( q+r\right) }\right)
\\
=\underset{\sigma \left( q+1\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 2\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) \cdot i_{z_{1}}\omega \left( z_{\sigma \left( 2\right)
},...,z_{\sigma \left( q\right) }\right) \cdot \theta \left( z_{\sigma
\left( q+1\right) },...,z_{\sigma \left( q+r\right) }\right) \\
+\underset{\sigma \left( q+2\right) <...<\sigma \left( q+r\right) }{\underset
{\sigma \left( 1\right) <...<\sigma \left( q\right) }{\tsum }}sgn\left(
\sigma \right) \cdot \omega \left( z_{\sigma \left( 1\right) },...,z_{\sigma
\left( q\right) }\right) \cdot i_{z_{1}}\theta \left( z_{\sigma \left(
q+2\right) },...,z_{\sigma \left( q+r\right) }\right) .
\end{array}$$

In the second sum, we have the permutation $$\sigma =\left(
\begin{array}{ccccccc}
1 & ... & q & q+1 & q+2 & ... & q+r \\
\sigma \left( 1\right) & ... & \sigma \left( q\right) & 1 & \sigma \left(
q+2\right) & ... & \sigma \left( q+r\right)
\end{array}
\right) .$$

We observe that $\sigma =\tau \circ \tau ^{\prime }$, where $$\tau =\left(
\begin{array}{ccccccc}
1 & 2 & ... & q+1 & q+2 & ... & q+r \\
1 & \sigma \left( 1\right) & ... & \sigma \left( q\right) & \sigma \left(
q+2\right) & ... & \sigma \left( q+r\right)
\end{array}
\right)$$ and $$\tau ^{\prime }=\left(
\begin{array}{cccccccc}
1 & 2 & ... & q & q+1 & q+2 & ... & q+r \\
2 & 3 & ... & q+1 & 1 & q+2 & ... & q+r
\end{array}
\right) .$$

Since $\tau \left( 2\right) <...<\tau \left( q+1\right)$ and $\tau ^{\prime
}$ has $q$ inversions, it results that $$sgn\left( \sigma \right) =\left( -1\right) ^{q}\cdot sgn\left( \tau \right) .$$

Therefore, $$\begin{array}{l}
i_{z_{1}}\left( \omega \wedge \theta \right) \left( z_{2},...,z_{q+r}\right)
=\left( i_{z_{1}}\omega \wedge \theta \right) \left( z_{2},...,z_{q+r}\right)
\\
+\left( -1\right) ^{q}\underset{\tau \left( q+2\right) <...<\tau \left(
q+r\right) }{\underset{\tau \left( 2\right) <...<\tau \left( q\right) }{
\tsum }}sgn\left( \tau \right) \cdot \omega \left( z_{\tau \left( 2\right)
},...,z_{\tau \left( q\right) }\right) \cdot i_{z_{1}}\theta \left( z_{\tau
\left( q+2\right) },...,z_{\tau \left( q+r\right) }\right) \\
=\left( i_{z_{1}}\omega \wedge \theta \right) \left(
z_{2},...,z_{q+r}\right) +\left( -1\right) ^{q}\left( \omega \wedge
i_{z_{1}}\theta \right) \left( z_{2},...,z_{q+r}\right) .
\end{array}$$

*q.e.d.*

**Theorem 4.6** *For any* $z,v\in \Gamma \left( F,\nu ,N\right)$ * we obtain* $$\begin{array}{c}
L_{v}\circ i_{z}-i_{z}\circ L_{v}=i_{\left[ z,v\right] _{F,h}}.
\end{array}
\leqno(4.8)$$

*Proof.* Let $\omega \in$* *$\Lambda ^{q}\left( F,\nu ,N\right)$ be arbitrary. Since $$\begin{array}{l}
i_{z}\left( L_{v}\omega \right) \left( z_{2},...z_{q}\right) =L_{v}\omega
\left( z,z_{2},...z_{q}\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) v\left( \omega \left(
z,z_{2},...,z_{q}\right) \right) -\omega \left( \left[ v,z\right]
_{F,h},z_{2},...,z_{q}\right) \\
-\overset{q}{\underset{i=2}{\tsum }}\omega \left( \left( z,z_{2},...,\left[
v,z_{i}\right] _{F,h},...,z_{q}\right) \right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) v\left( i_{z}\omega \left(
z_{2},...,z_{q}\right) \right) -\overset{q}{\underset{i=2}{\tsum }}
i_{z}\omega \left( z_{2},...,\left[ v,z_{i}\right] _{F,h},...,z_{q}\right)
\\
-i_{\left[ v,z\right] _{F}}\left( z_{2},...,z_{q}\right) =\left( L_{v}\left(
i_{z}\omega \right) -i_{\left[ v,z\right] _{F,h}}\right) \left(
z_{2},...,z_{q}\right) ,
\end{array}$$ for any $z_{2},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$ it result the conclusion of the theorem.*q.e.d.*

**Definition 4.7** If $f\in \mathcal{F}\left( N\right)$ and $z\in
\Gamma \left( F,\nu ,N\right) ,$ then we define ** ** $$\begin{array}{c}
d^{F}f\left( z\right) =\Gamma \left( Th\circ \rho ,h\circ \eta \right)
\left( z\right) f.
\end{array}$$

**Theorem 4.7** *The* $\mathcal{F}\left( N\right)$ *-multilinear application* $$\begin{array}{c}
\begin{array}{ccc}
\Lambda ^{q}\mathbf{\ }\left( F,\nu ,N\right) & ^{\underrightarrow{\,\
d^{F}\,\ }} & \Lambda ^{q+1}\mathbf{\ }\left( F,\nu ,N\right) \\
\omega & \longmapsto & d\omega
\end{array}
\end{array}$$ *defined by* $$\begin{array}{l}
d^{F}\omega \left( z_{0},z_{1},...,z_{q}\right) =\overset{q}{\underset{i=0}{
\tsum }}\left( -1\right) ^{i}\Gamma \left( Th\circ \rho ,h\circ \eta \right)
z_{i}\left( \omega \left( \left( z_{0},z_{1},...,\hat{z}_{i},...,z_{q}
\right) \right) \right) \\
~\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ +\underset{i<j}{\tsum }
\left( -1\right) ^{i+j}\omega \left( \left( \left[ z_{i},z_{j}\right]
_{F,h},z_{0},z_{1},...,\hat{z}_{i},...,\hat{z}_{j},...,z_{q}\right) \right) ,
\end{array}$$ *for any* $z_{0},z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right) ,$ *is unique with the following property:* $$\begin{array}{c}
L_{z}=d^{F}\circ i_{z}+i_{z}\circ d^{F},~\forall z\in \Gamma \left( F,\nu
,N\right) .
\end{array}
\leqno(4.9)$$

This $\mathcal{F}\left( N\right)$-multilinear application will be called * the exterior differentiation operator for the exterior differential algebra of the generalized Lie algebroid* $((F,\nu
,N),[,]_{F,h},(\rho ,\eta )).$

*Proof.* We verify the property $\left( 4.9\right)$ Since $$\begin{array}{l}
\left( i_{z_{0}}\circ d^{F}\right) \omega \left( z_{1},...,z_{q}\right)
=d\omega \left( z_{0},z_{1},...,z_{q}\right) \\
=\overset{q}{\underset{i=0}{\tsum }}\left( -1\right) ^{i}\Gamma \left(
Th\circ \rho ,h\circ \eta \right) z_{i}\left( \omega \left( z_{0},z_{1},...,
\hat{z}_{i},...,z_{q}\right) \right) \\
+\underset{0\leq i<j}{\tsum }\left( -1\right) ^{i+j}\omega \left( \left[
z_{i},z_{j}\right] _{F,h},z_{0},z_{1},...,\hat{z}_{i},...,\hat{z}
_{j},...,z_{q}\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z_{0}\left( \omega \left(
z_{1},...,z_{q}\right) \right) \\
+\overset{q}{\underset{i=1}{\tsum }}\left( -1\right) ^{i}\Gamma \left(
Th\circ \rho ,h\circ \eta \right) z_{i}\left( \omega \left( z_{0},z_{1},...,
\hat{z}_{i},...,z_{q}\right) \right) \\
+\underset{i=1}{\overset{q}{\tsum }}\left( -1\right) ^{i}\omega \left( \left[
z_{0},z_{i}\right] _{F,h},z_{1},...,\hat{z}_{i},...,z_{q}\right) \\
+\underset{1\leq i<j}{\tsum }\left( -1\right) ^{i+j}\omega \left( \left[
z_{i},z_{j}\right] _{F,h},z_{0},z_{1},...,\hat{z}_{i},...,\hat{z}
_{j},...,z_{q}\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z_{0}\left( \omega \left(
z_{1},...,z_{q}\right) \right) \\
-\underset{i=1}{\overset{q}{\tsum }}\omega \left( z_{1},...,\left[
z_{0},z_{i}\right] _{F,h},...,z_{q}\right) \\
-\overset{q}{\underset{i=1}{\tsum }}\left( -1\right) ^{i-1}\Gamma \left(
Th\circ \rho ,h\circ \eta \right) z_{i}\left( i_{z_{0}}\omega \left( \left(
z_{1},...,\hat{z}_{i},...,z_{q}\right) \right) \right) \\
-\underset{1\leq i<j}{\tsum }\left( -1\right) ^{i+j-2}i_{z_{0}}\omega \left(
\left( \left[ z_{i},z_{j}\right] _{F,h},z_{1},...,\hat{z}_{i},...,\hat{z}
_{j},...,z_{q}\right) \right) \\
=\left( L_{z_{0}}-d^{F}\circ i_{z_{0}}\right) \omega \left(
z_{1},...,z_{q}\right) ,
\end{array}$$ for any $z_{0},z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$ it results that the property $\left( 4.9\right)$ is satisfied.

In the following, we verify the uniqueness of the operator $d^{F}.$

Let $d^{\prime F}$ be an another exterior differentiation operator satisfying the property $\left( 4.9\right) .$

Let $S=\left\{ q\in \mathbb{N}:d^{F}\omega =d^{\prime F}\omega ,~\forall
\omega \in \Lambda ^{q}\left( F,\nu ,N\right) \right\}$ be.

Let $z\in \Gamma \left( F,\nu ,N\right)$ be arbitrary.

We observe that $\left( 4.9\right)$ is equivalent with $$\begin{array}{c}
i_{z}\circ \left( d^{F}-d^{\prime F}\right) +\left( d^{F}-d^{\prime
F}\right) \circ i_{z}=0.
\end{array}
\leqno(1)$$

Since $i_{z}f=0,$ for any $f\in \mathcal{F}\left( N\right) ,$ it results that $$\begin{array}{c}
\left( \left( d^{F}-d^{\prime F}\right) f\right) \left( z\right) =0,~\forall
f\in \mathcal{F}\left( N\right) .
\end{array}$$

Therefore, we obtain that $$\begin{array}{c}
0\in S.
\end{array}
\leqno(2)$$

In the following, we prove that $$\begin{array}{c}
q\in S\Longrightarrow q+1\in S
\end{array}
\leqno(3)$$

Let $\omega \in \Lambda ^{p+1}\left( F,\nu ,N\right)$ be arbitrary$.$ Since $i_{z}\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$, using the equality $\left( 1\right)$, it results that $$i_{z}\circ \left( d^{F}-d^{\prime F}\right) \omega =0.$$

We obtain that, $\left( \left( d^{F}-d^{\prime F}\right) \omega \right)
\left( z_{0},z_{1},...,z_{q}\right) =0,$ for any $z_{1},...,z_{q}\in \Gamma
\left( F,\nu ,N\right) .$

Therefore $d^{F}\omega =d^{\prime F}\omega ,$ namely $q+1\in S.$

Using the *Peano's Axiom* and the affirmations $\left( 2\right)$ and $\left( 3\right)$ it results that $S=\mathbb{N}.$

Therefore, the uniqueness is verified.*q.e.d.*

Note that if $\omega =\omega _{\alpha _{1}...\alpha _{q}}t^{\alpha
_{1}}\wedge ...\wedge t^{\alpha _{q}}\in \Lambda ^{q}\left( F,\nu ,N\right)$ , then $$\begin{aligned}
d^{F}\omega \left( t_{\alpha _{0}},t_{\alpha _{1}},...,t_{\alpha
_{q}}\right) &=&\overset{q}{\underset{i=0}{\tsum }}\left( -1\right)
^{i}\theta _{\alpha _{i}}^{\tilde{k}}\frac{\partial \omega _{\alpha _{0},...,
\widehat{\alpha _{i}}...\alpha _{q}}}{\partial \varkappa ^{\tilde{k}}} \\%
[1mm]
&&+\underset{i<j}{\tsum }\left( -1\right) ^{i+j}L_{\alpha _{i}\alpha
_{j}}^{\alpha }\cdot \omega _{\alpha ,\alpha _{0},...,\widehat{\alpha _{i}}
,...,\widehat{\alpha _{j}},...,\alpha _{q}}.
\end{aligned}$$

Therefore, we obtain $$\begin{array}{l}
d^{F}\omega =\left( \overset{q}{\underset{i=0}{\tsum }}\left( -1\right)
^{i}\theta _{\alpha _{i}}^{\tilde{k}}\displaystyle\frac{\partial \omega
_{\alpha _{0},...,\widehat{\alpha _{i}}...\alpha _{q}}}{\partial \varkappa ^{
\tilde{k}}}\right. \\
\left. +\underset{i<j}{\tsum }\left( -1\right) ^{i+j}L_{\alpha _{i}\alpha
_{j}}^{\alpha }\cdot \omega _{\alpha ,\alpha _{0},...,\widehat{\alpha _{i}}
,...,\widehat{\alpha _{j}},...,\alpha _{q}}\right) t^{\alpha _{0}}\wedge
t^{\alpha _{1}}\wedge ...\wedge t^{\alpha _{q}}.
\end{array}
\leqno(4.10)$$

*Remark 4.5* If $d^{F}$ is the exterior differentiation operator for the generalized Lie algebroid $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right) ,$$ $\omega \in$* *$\Lambda ^{q}\left( F,\nu ,N\right)$ and $U$ is an open subset of $N$ such that $\omega _{|U}=0,$ then $\left( d^{F}\omega
\right) _{|U}=0.$

**Theorem 4.8** *The exterior differentiation operator* $d^{F}$ * given by the previous theorem has the following properties:*

. * For any* $\omega \in$* *$\Lambda ^{q}\left(
F,\nu ,N\right)$* and* $\theta \in$* *$\Lambda ^{r}\left(
F,\nu ,N\right)$* we obtain* $$\begin{array}{c}
d^{F}\left( \omega \wedge \theta \right) =d^{F}\omega \wedge \theta +\left(
-1\right) ^{q}\omega \wedge d^{F}\theta .
\end{array}
\leqno(4.11)$$

.* For any* $z\in \Gamma \left( F,\nu ,N\right)$ we obtain $$\begin{array}{c}
L_{z}\circ d^{F}=d^{F}\circ L_{z}.
\end{array}
\leqno(4.12)$$

.* *$d^{F}\circ d^{F}=0.$

*Proof.*. Let $S=\left\{ q\in \mathbb{N}:d^{F}\left( \omega \wedge \theta \right)
=d^{F}\omega \wedge \theta +\left( -1\right) ^{q}\omega \wedge d^{F}\theta
,~\forall \omega \in \Lambda ^{q}\left( F,\nu ,N\right) \right\}$ be. Since $$\begin{array}{l}
d^{F}\left( f\wedge \theta \right) \left( z,v\right) =d^{F}\left( f\cdot
\theta \right) \left( z,v\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left( f\omega \left(
v\right) \right) -\Gamma \left( Th\circ \rho ,h\circ \eta \right) v\left(
f\omega \left( z\right) \right) -f\omega \left( \left[ z,v\right]
_{F,h}\right) \\
=\Gamma \left( Th\circ \rho ,h\circ \eta \right) z\left( f\right) \cdot
\omega \left( v\right) +f\cdot \Gamma \left( Th\circ \rho ,h\circ \eta
\right) z\left( \omega \left( v\right) \right) \\
-\Gamma \left( Th\circ \rho ,h\circ \eta \right) v\left( f\right) \cdot
\omega \left( z\right) -f\cdot \Gamma \left( Th\circ \rho ,h\circ \eta
\right) v\left( \omega \left( z\right) \right) -f\omega \left( \left[ z,v
\right] _{F,h}\right) \\
=d^{F}f\left( z\right) \cdot \omega \left( v\right) -d^{F}f\left( v\right)
\cdot \omega \left( z\right) +f\cdot d^{F}\omega \left( z,v\right) \\
=\left( d^{F}f\wedge \omega \right) \left( z,v\right) +\left( -1\right)
^{0}f\cdot d^{F}\omega \left( z,v\right) \\
=\left( d^{F}f\wedge \omega \right) \left( z,v\right) +\left( -1\right)
^{0}\left( f\wedge d^{F}\omega \right) \left( z,v\right) ,~\forall z,v\in
\Gamma \left( F,\nu ,N\right) ,
\end{array}$$ it results that $$\begin{array}{c}
0\in S.
\end{array}
\leqno(1.1)$$

In the following we prove that $$\begin{array}{c}
q\in S\Longrightarrow q+1\in S.
\end{array}
\leqno(1.2)$$

Without restricting the generality, we consider that $\theta \in \Lambda
^{r}\left( F,\nu ,N\right) .$ Since $$\begin{array}{l}
d^{F}\left( \omega \wedge \theta \right) \left(
z_{0},z_{1},...,z_{q+r}\right) =i_{z_{0}}\circ d^{F}\left( \omega \wedge
\theta \right) \left( z_{1},...,z_{q+r}\right) \\
=L_{z_{0}}\left( \omega \wedge \theta \right) \left(
z_{1},...,z_{q+r}\right) -d^{F}\circ i_{z_{0}}\left( \omega \wedge \theta
\right) \left( z_{1},...,z_{q+r}\right) \\
=\left( L_{z_{0}}\omega \wedge \theta +\omega \wedge L_{z_{0}}\theta \right)
\left( z_{1},...,z_{q+r}\right) \\
-\left[ d^{F}\circ \left( i_{z_{0}}\omega \wedge \theta +\left( -1\right)
^{q}\omega \wedge i_{z_{0}}\theta \right) \right] \left(
z_{1},...,z_{q+r}\right) \\
=\left( L_{z_{0}}\omega \wedge \theta +\omega \wedge L_{z_{0}}\theta -\left(
d^{F}\circ i_{z_{0}}\omega \right) \wedge \theta \right) \left(
z_{1},...,z_{q+r}\right) \\
-\left( \left( -1\right) ^{q-1}i_{z_{0}}\omega \wedge d^{F}\theta +\left(
-1\right) ^{q}d^{F}\omega \wedge i_{z_{0}}\theta \right) \left(
z_{1},...,z_{q+r}\right) \\
-\left( -1\right) ^{2q}\omega \wedge d^{F}\circ i_{z_{0}}\theta \left(
z_{1},...,z_{q+r}\right) \\
=\left( \left( L_{z_{0}}\omega -d^{F}\circ i_{z_{0}}\omega \right) \wedge
\theta \right) \left( z_{1},...,z_{q+r}\right) \\
+\omega \wedge \left( L_{z_{0}}\theta -d^{F}\circ i_{z_{0}}\theta \right)
\left( z_{1},...,z_{q+r}\right) \\
+\left( \left( -1\right) ^{q}i_{z_{0}}\omega \wedge d^{F}\theta -\left(
-1\right) ^{q}d^{F}\omega \wedge i_{z_{0}}\theta \right) \left(
z_{1},...,z_{q+r}\right) \\
=\left[ \left( \left( i_{z_{0}}\circ d^{F}\right) \omega \right) \wedge
\theta +\left( -1\right) ^{q+1}d^{F}\omega \wedge i_{z_{0}}\theta \right]
\left( z_{1},...,z_{q+r}\right) \\
+\left[ \omega \wedge \left( \left( i_{z_{0}}\circ d^{F}\right) \theta
\right) +\left( -1\right) ^{q}i_{z_{0}}\omega \wedge d^{F}\theta \right]
\left( z_{1},...,z_{q+r}\right) \\
=\left[ i_{z_{0}}\left( d^{F}\omega \wedge \theta \right) +\left( -1\right)
^{q}i_{z_{0}}\left( \omega \wedge d^{F}\theta \right) \right] \left(
z_{1},...,z_{q+r}\right) \\
=\left[ d^{F}\omega \wedge \theta +\left( -1\right) ^{q}\omega \wedge
d^{F}\theta \right] \left( z_{1},...,z_{q+r}\right) ,
\end{array}$$ for any $z_{0},z_{1},...,z_{q+r}\in \Gamma \left( F,\nu ,N\right)$, it results $\left( 1.2\right) .$

Using the *Peano's Axiom* and the affirmations $\left( 1.1\right)$ and $\left( 1.2\right)$ it results that $S=\mathbb{N}.$

Therefore, it results the conclusion of affirmation 1.

2\. Let $z\in \Gamma \left( F,\nu ,N\right)$ be arbitrary.

Let $S=\left\{ q\in \mathbb{N}:\left( L_{z}\circ d^{F}\right) \omega =\left(
d^{F}\circ L_{z}\right) \omega ,~\forall \omega \in \Lambda ^{q}\left( F,\nu
,N\right) \right\}$ be.

Let $f\in \mathcal{F}\left( N\right)$ be arbitrary. Since $$\begin{array}{l}
\left( d^{F}\circ L_{z}\right) f\left( v\right) =i_{v}\circ \left(
d^{F}\circ L_{z}\right) f=\left( i_{v}\circ d^{F}\right) \circ L_{z}f \\
=\left( L_{v}\circ L_{z}\right) f-\left( \left( d^{F}\circ i_{v}\right)
\circ L_{z}\right) f \\
=\left( L_{v}\circ L_{z}\right) f-L_{\left[ z,v\right] _{F,h}}f+d^{F}\circ
i_{\left[ z,v\right] _{F,h}}f-d^{F}\circ L_{z}\left( i_{v}f\right) \\
=\left( L_{v}\circ L_{z}\right) f-L_{\left[ z,v\right] _{F,h}}f+d^{F}\circ
i_{\left[ z,v\right] _{F,h}}f-0 \\
=\left( L_{v}\circ L_{z}\right) f-L_{\left[ z,v\right] _{F,h}}f+d^{F}\circ
i_{\left[ z,v\right] _{F,h}}f-L_{z}\circ d^{F}\left( i_{v}f\right) \\
=\left( L_{z}\circ i_{v}\right) \left( d^{F}f\right) -L_{\left[ z,v\right]
_{F,h}}f+d^{F}\circ i_{\left[ z,v\right] _{F,h}}f \\
=\left( i_{v}\circ L_{z}\right) \left( d^{F}f\right) +L_{\left[ z,v\right]
_{F,h}}f-L_{\left[ z,v\right] _{F,h}}f \\
=i_{v}\circ \left( L_{z}\circ d^{F}\right) f=\left( L_{z}\circ d^{F}\right)
f\left( v\right) ,~\forall v\in \Gamma \left( F,\nu ,N\right) ,
\end{array}$$ it results that $$\begin{array}{c}
0\in S.
\end{array}
\leqno(2.1)$$

In the following we prove that $$\begin{array}{c}
q\in S\Longrightarrow q+1\in S.
\end{array}
\leqno(2.2)$$

Let $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ be arbitrary. Since $$\begin{array}{l}
\left( d^{F}\circ L_{z}\right) \omega \left( z_{0},z_{1},...,z_{q}\right)
=i_{z_{0}}\circ \left( d^{F}\circ L_{z}\right) \omega \left(
z_{1},...,z_{q}\right) \vspace*{1mm} \\
=\left( i_{z_{0}}\circ d^{F}\right) \circ L_{z}\omega \left(
z_{1},...,z_{q}\right) \vspace*{1mm} \\
=\left[ \left( L_{z_{0}}\circ L_{z}\right) \omega -\left( \left( d^{F}\circ
i_{z_{0}}\right) \circ L_{z}\right) \omega \right] \left(
z_{1},...,z_{q}\right) \vspace*{1mm} \\
=\left[ \left( L_{z_{0}}\circ L_{z}\right) \omega -L_{\left[ z,z_{0}\right]
_{F,h}}\omega \right] \left( z_{1},...,z_{q}\right) \vspace*{1mm} \\
+\left[ d^{F}\circ i_{\left[ z,z_{0}\right] _{F,h}}\omega -d^{F}\circ
L_{z}\left( i_{z_{0}}\omega \right) \right] \left( z_{1},...,z_{q}\right)
\vspace*{1mm} \\
\overset{ip.}{=}\left[ \left( L_{z_{0}}\circ L_{z}\right) \omega -L_{\left[
z,z_{0}\right] _{F,h}}\omega \right] \left( z_{1},...,z_{q}\right) \vspace*{
1mm} \\
+\left[ d^{F}\circ i_{\left[ z,z_{0}\right] _{F,h}}\omega -L_{z}\circ
d^{F}\left( i_{z_{0}}\omega \right) \right] \left( z_{1},...,z_{q}\right)
\vspace*{1mm} \\
=\left[ \left( L_{z}\circ i_{z_{0}}\right) \left( d^{F}\omega \right) -L_{
\left[ z,z_{0}\right] _{F,h}}\omega +d^{F}\circ i_{\left[ z,z_{0}\right]
_{F,h}}\omega \right] \left( z_{1},...,z_{q}\right) \vspace*{1mm} \\
=\left[ \left( i_{z_{0}}\circ L_{z}\right) \left( d^{F}\omega \right) +L_{
\left[ z,z_{0}\right] _{F,h}}\omega -L_{\left[ z,z_{0}\right] _{F,h}}\omega 
\right] \left( z_{1},...,z_{q}\right) \vspace*{1mm} \\
=i_{z_{0}}\circ \left( L_{z}\circ d^{F}\right) \omega \left(
z_{1},...,z_{q}\right) \vspace*{1mm} \\
=\left( L_{z}\circ d^{F}\right) \omega \left( z_{0},z_{1},...,z_{q}\right)
,~\forall z_{0},z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right) ,
\end{array}$$ it results $\left( 2.2\right) .$

Using the *Peano's Axiom* and the affirmations $\left( 2.1\right)$ and $\left( 2.2\right)$ it results that $S=\mathbb{N}.$

Therefore, it results the conclusion of affirmation 2.

3\. It is remarked that $$\begin{array}{l}
i_{z}\circ \left( d^{F}\circ d^{F}\right) =\left( i_{z}\circ d^{F}\right)
\circ d^{F}=L_{z}\circ d^{F}-\left( d^{F}\circ i_{z}\right) \circ d^{F}
\vspace*{1mm} \\
=L_{z}\circ d^{F}-d^{F}\circ L_{z}+d^{F}\circ \left( d^{F}\circ i_{z}\right)
=\left( d^{F}\circ d^{F}\right) \circ i_{z},
\end{array}$$ for any $z\in \Gamma \left( F,\nu ,N\right) .$

Let $\omega \in \Lambda ^{q}\left( F,\nu ,N\right)$ be arbitrary. Since $$\begin{array}{l}
\left( d^{F}\circ d^{F}\right) \omega \left( z_{1},...,z_{q+2}\right)
=i_{z_{q+2}}\circ ...\circ i_{z_{1}}\circ \left( d^{F}\circ d^{F}\right)
\omega =...\vspace*{1mm} \\
=i_{z_{q+2}}\circ \left( d^{F}\circ d^{F}\right) \circ i_{z_{q+1}}\left(
\omega \left( z_{1},...,z_{q}\right) \right) \vspace*{1mm} \\
=i_{z_{q+2}}\circ \left( d^{F}\circ d^{F}\right) \left( 0\right) =0,~\forall
z_{1},...,z_{q+2}\in \Gamma \left( F,\nu ,N\right) ,
\end{array}$$ it results the conclusion of affirmation 3. *q.e.d.*

**Theorem 4.9** *If* $d^{F}$ *is the exterior differentiation operator for the exterior differential* $\mathcal{F}(N)$*-algebra* $(\Lambda (F,\nu ,N),+,\cdot ,\wedge )$, *then we obtain the structure equations of Maurer-Cartan type* $$\begin{array}{c}
d^{F}t^{\alpha }=-\displaystyle\frac{1}{2}L_{\beta \gamma }^{\alpha
}t^{\beta }\wedge t^{\gamma },~\alpha \in \overline{1,p}
\end{array}
\leqno(\mathcal{C}_{1})$$ *and * $$\begin{array}{c}
d^{F}\varkappa ^{\tilde{\imath}}=\theta _{\alpha }^{\tilde{\imath}}t^{\alpha
},~\tilde{\imath}\in \overline{1,n},
\end{array}
\leqno(\mathcal{C}_{2})$$ *where* $\left\{ t^{\alpha },\alpha \in \overline{1,p}\right\} ~$ *is the coframe of the vector bundle* $\left( F,\nu ,N\right) .$

This equations will be called *the structure equations of Maurer-Cartan type associated to the generalized Lie algebroid* $\left( \left( F,\nu
,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta \right) \right) .$

*Proof.* Let $\alpha \in \overline{1,p}$ be arbitrary. Since $$\begin{array}{c}
d^{F}t^{\alpha }\left( t_{\beta },t_{\gamma }\right) =-L_{\beta \gamma
}^{\alpha },~\forall \beta ,\gamma \in \overline{1,p}
\end{array}$$ it results that $$\begin{array}{c}
d^{F}t^{\alpha }=-\underset{\beta <\gamma }{\tsum }L_{\beta \gamma }^{\alpha
}t^{\beta }\wedge t^{\gamma }.
\end{array}
\leqno(1)$$

Since $L_{\beta \gamma }^{\alpha }=-L_{\gamma \beta }^{\alpha }$ and $t^{\beta }\wedge t^{\gamma }=-t^{\gamma }\wedge t^{\beta }$, for nay $\beta
,\gamma \in \overline{1,p},$ it results that $$\begin{array}{c}
\underset{\beta <\gamma }{\tsum }L_{\beta \gamma }^{\alpha }t^{\beta }\wedge
t^{\gamma }=\displaystyle\frac{1}{2}L_{\beta \gamma }^{\alpha }t^{\beta
}\wedge t^{\gamma }
\end{array}
\leqno(2)$$

Using the equalities $\left( 1\right)$ and $\left( 2\right)$ it results the structure equation $(\mathcal{C}_{1}).$

Let $\tilde{\imath}\in \overline{1,n}$ be arbitrarily. Since $$\begin{array}{c}
d^{F}\varkappa ^{\tilde{\imath}}\left( t_{\alpha }\right) =\theta _{\alpha
}^{\tilde{\imath}},~\forall \alpha \in \overline{1,p}
\end{array}$$ it results the structure equation $(\mathcal{C}_{2}).$*q.e.d.*

**Corollary 4.1** *If* $\left( \left( h^{\ast }F,h^{\ast }\nu
,M\right) ,\left[ ,\right] _{h^{\ast }F},\left( \overset{h^{\ast }F}{\rho }
,Id_{M}\right) \right)$ * is the pull-back Lie algebroid associated to the generalized Lie algebroid* $\left( \left( F,\nu ,N\right) ,\left[ ,
\right] _{F,h},\left( \rho ,\eta \right) \right)$ *and* $d^{h^{\ast }F}$* is the exterior differentiation operator for the exterior differential* $\mathcal{F}\left( M\right)$*-algebra* $$\left( \Lambda \left( h^{\ast }F,h^{\ast }\nu ,M\right) ,+,\cdot ,\wedge
\right),$$ * then we obtain the following structure equations of Maurer-Cartan type  * $$\begin{array}{c}
d^{h^{\ast }F}T^{\alpha }=-\displaystyle\frac{1}{2}\left( L_{\beta \gamma
}^{\alpha }\circ h\right) T^{\beta }\wedge T^{\gamma },~\alpha \in \overline{
1,p}
\end{array}
\leqno(\mathcal{C}_{1}^{\prime })$$ *and * $$\begin{array}{c}
d^{h^{\ast }F}x^{i}=\left( \rho _{\alpha }^{i}\circ h\right) T^{\alpha
},~i\in \overline{1,m}.
\end{array}
\leqno(\mathcal{C}_{2}^{\prime })$$

This equations will be called *the structure equations of Maurer-Cartan type associated to the pull-back Lie algebroid* $$\left( \left( h^{\ast }F,h^{\ast }\nu ,M\right) ,\left[ ,\right] _{h^{\ast
}F},\left( \overset{h^{\ast }F}{\rho },Id_{M}\right) \right) .$$

**Theorem 4.10 (**of Cartan type)** ***Let* $\left( E,\pi
,M\right)$* be an IDS of the generalized Lie algebroid* $\left(
\left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta \right)
\right) .$* If* $\left\{ \Theta ^{r+1},...,\Theta ^{p}\right\}$ * is a base for the* $\mathcal{F}\left( M\right)$*-submodule* $\left(
\Gamma \left( E^{0},\pi ^{0},M\right) ,+,\cdot \right)$*, then the IDS* $\left( E,\pi ,M\right)$* is involutive if and only if it exists* $$\Omega _{\beta }^{\alpha }\in \Lambda ^{1}\left( h^{\ast }F,h^{\ast }\nu
,M\right) ,~\alpha ,\beta \in \overline{r+1,p}$$ *such that* $$d^{h^{\ast }F}\Theta ^{\alpha }=\Sigma _{\beta \in \overline{r+1,p}}\Omega
_{\beta }^{\alpha }\wedge \Theta ^{\beta }\in \mathcal{I}\left( \Gamma
\left( E^{0},\pi ^{0},M\right) \right) .$$

*Proof:* Let $\left\{ S_{1},...,S_{r}\right\}$ be a base for the $\mathcal{F}\left( M\right)$-submodule $\left( \Gamma \left( E,\pi ,M\right)
,+,\cdot \right)$

Let $\left\{ S_{r+1},...,S_{p}\right\} \in \Gamma \left( h^{\ast }F,h^{\ast
}\nu ,M\right)$ such that $$\left\{ S_{1},...,S_{r},S_{r+1},...,S_{p}\right\}$$ is a base for the $\mathcal{F}\left( M\right)$-module $$\left( \Gamma \left( h^{\ast }F,h^{\ast }\nu ,M\right) ,+,\cdot \right) .$$

Let $\Theta ^{1},...,\Theta ^{r}\in \Gamma \left( \overset{\ast }{h^{\ast }F}
,\overset{\ast }{h^{\ast }\nu },M\right)$ such that $$\left\{ \Theta ^{1},...,\Theta ^{r},\Theta ^{r+1},...,\Theta ^{p}\right\}$$ is a base for the $\mathcal{F}\left( M\right)$-module $$\left( \Gamma \left( \overset{\ast }{h^{\ast }F},\overset{\ast }{h^{\ast
}\nu },M\right) ,+,\cdot \right) .$$

For any $a,b\in \overline{1,r}$ and $\alpha ,\beta \in \overline{r+1,p}$, we have the equalities: $$\begin{array}{ccc}
\Theta ^{a}\left( S_{b}\right) & = & \delta _{b}^{a} \\
\Theta ^{a}\left( S_{\beta }\right) & = & 0 \\
\Theta ^{\alpha }\left( S_{b}\right) & = & 0 \\
\Theta ^{\alpha }\left( S_{\beta }\right) & = & \delta _{\beta }^{\alpha }
\end{array}$$

We remark that the set of the $2$-forms $$\left\{ \Theta ^{a}\wedge \Theta ^{b},\Theta ^{a}\wedge \Theta ^{\beta
},\Theta ^{\alpha }\wedge \Theta ^{\beta },~a,b\in \overline{1,r}\wedge
\alpha ,\beta \in \overline{r+1,p}\right\}$$ is a base for the $\mathcal{F}\left( M\right)$-module $$\left( \Lambda ^{2}\left( h^{\ast }F,h^{\ast }\nu ,M\right) ,+,\cdot \right)
.$$

Therefore, we have $$d^{h^{\ast }F}\Theta ^{\alpha }=\Sigma _{b<c}A_{bc}^{\alpha }\Theta
^{b}\wedge \Theta ^{c}+\Sigma _{b,\gamma }B_{b\gamma }^{\alpha }\Theta
^{b}\wedge \Theta ^{\gamma }+\Sigma _{\beta <\gamma }C_{\beta \gamma
}^{\alpha }\Theta ^{\beta }\wedge \Theta ^{\gamma },\leqno\left( 1\right)$$ where, $A_{bc}^{\alpha },B_{b\gamma }^{\alpha }$ and $C_{\beta \gamma
}^{\alpha },~a,b,c\in \overline{1,r}\wedge \alpha ,\beta ,\gamma \in
\overline{r+1,p}$ are real local functions such that $A_{bc}^{\alpha
}=-A_{cb}^{\alpha }$ and $C_{\beta \gamma }^{\alpha }=-C_{\gamma \beta
}^{\alpha }.$

Using the formula $$d^{h^{\ast }F}\Theta ^{\alpha }\left( S_{b},S_{c}\right) =\Gamma \left(
\overset{h^{\ast }F}{\rho },Id_{M}\right) S_{b}\left( \Theta ^{\alpha
}\left( S_{c}\right) \right) -\Gamma \left( \overset{h^{\ast }F}{\rho }
,Id_{M}\right) S_{c}\left( \Theta ^{\alpha }\left( S_{b}\right) \right)
-\Theta ^{\alpha }\left( \left[ S_{b},S_{c}\right] _{h^{\ast }F}\right) ,
\leqno\left( 2\right)$$ we obtain that $$A_{bc}^{\alpha }=-\Theta ^{\alpha }\left( \left[ S_{b},S_{c}\right]
_{h^{\ast }F}\right) ,~\forall \left( b,c\in \overline{1,r}\wedge \alpha \in
\overline{r+1,p}\right) .\leqno\left( 3\right)$$

We admit that $\left( E,\pi ,M\right)$ is an involutive IDS of the generalized Lie algebroid $\left( \left( F,\nu ,N\right) ,\left[ ,\right]
_{F,h},\left( \rho ,\eta \right) \right) .$

As $$\left[ S_{b},S_{c}\right] _{h^{\ast }F}\in \Gamma \left( E,\pi ,M\right)
,~\forall b,c\in \overline{1,r}$$ it results that $$\Theta ^{\alpha }\left( \left[ S_{b},S_{c}\right] _{h^{\ast }F}\right)
=0,~\forall \left( b,c\in \overline{1,r}\wedge \alpha \in \overline{r+1,p}
\right) .$$

Therefore, $$A_{bc}^{\alpha }=0,~\forall \left( b,c\in \overline{1,r}\wedge \alpha \in
\overline{r+1,p}\right)$$ and we obtain $$\begin{array}{ccl}
d^{h^{\ast }F}\Theta ^{\alpha } & = & \Sigma _{b,\gamma }B_{b\gamma
}^{\alpha }\Theta ^{b}\wedge \Theta ^{\gamma }+\frac{1}{2}C_{\beta \gamma
}^{\alpha }\Theta ^{\beta }\wedge \Theta ^{\gamma } \\
& = & \left( B_{b\gamma }^{\alpha }\Theta ^{b}+\frac{1}{2}C_{\beta \gamma
}^{\alpha }\Theta ^{\beta }\right) \wedge \Theta ^{\gamma }.
\end{array}$$

As $$\Omega _{\gamma }^{\alpha }\overset{put}{=}B_{b\gamma }^{\alpha }\Theta ^{b}+
\frac{1}{2}C_{\beta \gamma }^{\alpha }\Theta ^{\beta }\in \Lambda ^{1}\left(
h^{\ast }F,h^{\ast }\nu ,M\right) ,~\forall \alpha ,\beta \in \overline{r+1,p
}$$ it results the first implication.

Conversely, we admit that it exists $$\Omega _{\beta }^{\alpha }\in \Lambda ^{1}\left( h^{\ast }F,h^{\ast }\nu
,M\right) ,~\alpha ,\beta \in \overline{r+1,p}$$ such that $$d^{h^{\ast }F}\Theta ^{\alpha }=\Sigma _{\beta \in \overline{r+1,p}}\Omega
_{\beta }^{\alpha }\wedge \Theta ^{\beta },~\forall \alpha \in \overline{
r+1,p}.\leqno\left( 4\right)$$

Using the affirmations $\left( 1\right) ,\left( 2\right)$ and $\left(
4\right)$ we obtain that $$A_{bc}^{\alpha }=0,~\forall \left( b,c\in \overline{1,r}\wedge \alpha \in
\overline{r+1,p}\right) .$$

Using the affirmation $\left( 3\right)$, we obtain $$\Theta ^{\alpha }\left( \left[ S_{b},S_{c}\right] _{h^{\ast }F}\right)
=0,~\forall \left( b,c\in \overline{1,r}\wedge \alpha \in \overline{r+1,p}
\right) .$$

Therefore, $$\left[ S_{b},S_{c}\right] _{h^{\ast }F}\in \Gamma \left( E,\pi ,M\right)
,~\forall b,c\in \overline{1,r}.$$

Using the *Proposition 3.2*, we obtain the second implication. *q.e.d.*

Let $\left( \left( F^{\prime },\nu ^{\prime },N^{\prime }\right) ,\left[ ,
\right] _{F^{\prime },h^{\prime }},\left( \rho ^{\prime },\eta ^{\prime
}\right) \right)$ be an another generalized Lie algebroid.

**Definition 4.8** For any morphism $\left( \varphi ,\varphi
_{0}\right)$ of $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ source and $$\left( \left( F^{\prime },\nu ^{\prime },N^{\prime }\right) ,\left[ ,\right]
_{F^{\prime },h^{\prime }},\left( \rho ^{\prime },\eta ^{\prime }\right)
\right)$$ target we define the application $$\begin{array}{ccc}
\Lambda ^{q}\left( F^{\prime },\nu ^{\prime },N^{\prime }\right) & ^{
\underrightarrow{\ \left( \varphi ,\varphi _{0}\right) ^{\ast }\ }} &
\Lambda ^{q}\left( F,\nu ,N\right) \\
\omega ^{\prime } & \longmapsto & \left( \varphi ,\varphi _{0}\right) ^{\ast
}\omega ^{\prime }
\end{array}
,$$ where $$\begin{array}{c}
\left( \left( \varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime }\right)
\left( z_{1},...,z_{q}\right) =\omega ^{\prime }\left( \Gamma \left( \varphi
,\varphi _{0}\right) \left( z_{1}\right) ,...,\Gamma \left( \varphi ,\varphi
_{0}\right) \left( z_{q}\right) \right) ,
\end{array}$$ for any $z_{1},...,z_{q}\in \Gamma \left( F,\nu ,N\right) .$

*Remark 4.5*** **It is remarked that the $\mathbf{B}^{\mathbf{v}}$-morphism $\left( Th\circ \rho ,h\circ \eta \right)$ is a $\mathbf{GLA}$-morphism of $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ * *source and $$\left( \left( TN,\tau _{N},N\right) ,\left[ ,\right] _{TN,Id_{N}},\left(
Id_{TN},Id_{N}\right) \right)$$ target.

Moreover, for any $\tilde{\imath}\in \overline{1,n}$, we obtain $$\begin{array}{c}
\left( Th\circ \rho ,h\circ \eta \right) ^{\ast }\left( d\varkappa ^{\tilde{
\imath}}\right) =d^{F}\varkappa ^{\tilde{\imath}},
\end{array}$$ where $d$ is the exterior differentiation operator associated to the exterior differential Lie $\mathcal{F}\left( N\right)$-algebra* * $$\begin{array}{c}
\left( \Lambda \left( TN,\tau _{N},N\right) ,+,\cdot ,\wedge \right) .
\end{array}$$

**Theorem 4.11** *If* $\left( \varphi ,\varphi _{0}\right)$ * is a morphism of* $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ * source and* $$\left( \left( F^{\prime },\nu ^{\prime },N^{\prime }\right) ,\left[ ,\right]
_{F^{\prime },h^{\prime }},\left( \rho ^{\prime },\eta ^{\prime }\right)
\right)$$ *target, then the following affirmations are satisfied:*

. *For any* $\omega ^{\prime }\in \Lambda ^{q}\left(
F^{\prime },\nu ^{\prime },N^{\prime }\right)$* and* $\theta ^{\prime
}\in \Lambda ^{r}\left( F^{\prime },\nu ^{\prime },N^{\prime }\right)$ * we obtain* $$\begin{array}{c}
\left( \varphi ,\varphi _{0}\right) ^{\ast }\left( \omega ^{\prime }\wedge
\theta ^{\prime }\right) =\left( \varphi ,\varphi _{0}\right) ^{\ast }\omega
^{\prime }\wedge \left( \varphi ,\varphi _{0}\right) ^{\ast }\theta ^{\prime
}.
\end{array}
\leqno(4.13)$$

.* For any* $z\in \Gamma \left( F,\nu ,N\right)$* and* $\omega ^{\prime }\in \Lambda ^{q}\left( F^{\prime },\nu ^{\prime
},N^{\prime }\right)$* we obtain* $$\begin{array}{c}
i_{z}\left( \left( \varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime
}\right) =\left( \varphi ,\varphi _{0}\right) ^{\ast }\left( i_{\Gamma
\left( \varphi ,\varphi _{0}\right) z}\omega ^{\prime }\right) .
\end{array}
\leqno(4.14)$$

. *If* $N=N^{\prime }$ *and* $$\left( Th\circ \rho ,h\circ \eta \right) =\left( Th^{\prime }\circ \rho
^{\prime },h^{\prime }\circ \eta ^{\prime }\right) \circ \left( \varphi
,\varphi _{0}\right) ,$$ *then we obtain* $$\begin{array}{c}
\left( \varphi ,\varphi _{0}\right) ^{\ast }\circ d^{F^{\prime }}=d^{F}\circ
\left( \varphi ,\varphi _{0}\right) ^{\ast }.
\end{array}
\leqno(4.15)$$

*Proof.* 1. Let $\omega ^{\prime }\in \Lambda ^{q}\left( F^{\prime
},\nu ^{\prime },N^{\prime }\right)$ and $\theta ^{\prime }\in \Lambda
^{r}\left( F^{\prime },\nu ^{\prime },N^{\prime }\right)$ be arbitrary. Since $$\begin{array}{l}
\displaystyle\left( \varphi ,\varphi _{0}\right) ^{\ast }\left( \omega
^{\prime }\wedge \theta ^{\prime }\right) \left( z_{1},...,z_{q+r}\right)
=\left( \omega ^{\prime }\wedge \theta ^{\prime }\right) \left( \Gamma
\left( \varphi ,\varphi _{0}\right) z_{1},...,\Gamma \left( \varphi ,\varphi
_{0}\right) z_{q+r}\right) \vspace*{1mm} \\
\qquad\displaystyle=\frac{1}{\left( q+r\right) !}\underset{\sigma \in \Sigma
_{q+r}}{\tsum }sgn\left( \sigma \right) \cdot \omega ^{\prime }\left( \Gamma
\left( \varphi ,\varphi _{0}\right) z_{1},...,\Gamma \left( \varphi ,\varphi
_{0}\right) z_{q}\right) \vspace*{1mm} \\
\hfill\cdot \theta ^{\prime }\left( \Gamma \left( \varphi ,\varphi
_{0}\right) z_{q+1},...,\Gamma \left( \varphi ,\varphi _{0}\right)
z_{q+r}\right) \vspace*{1mm} \\
\qquad\displaystyle=\frac{1}{\left( q+r\right) !}\underset{\sigma \in \Sigma
_{q+r}}{\tsum }sgn\left( \sigma \right) \cdot \left( \varphi ,\varphi
_{0}\right) ^{\ast }\omega ^{\prime }\left( z_{1},...,z_{q}\right) \left(
\varphi ,\varphi _{0}\right) ^{\ast }\theta ^{\prime }\left(
z_{q+1},...,z_{q+r}\right) \vspace*{1mm} \\
\qquad\displaystyle=\left( \left( \varphi ,\varphi _{0}\right) ^{\ast
}\omega ^{\prime }\wedge \left( \varphi ,\varphi _{0}\right) ^{\ast }\theta
^{\prime }\right) \left( z_{1},...,z_{q+r}\right) ,
\end{array}$$ for any $z_{1},...,z_{q+r}\in \Gamma \left( F,\nu ,N\right)$, it results the conclusion of affirmation 1.

2\. Let $z\in \Gamma \left( F,\nu ,N\right)$* *and* *$\omega
^{\prime }\in \Lambda ^{q}\left( F^{\prime },\nu ^{\prime },N^{\prime
}\right)$ be arbitrary. Since $$\begin{array}{ll}
i_{z}\left( \left( \varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime
}\right) \left( z_{2},...,z_{q}\right) & \displaystyle =\omega ^{\prime
}\left( \Gamma \left( \varphi ,\varphi _{0}\right) z,\Gamma \left( \varphi
,\varphi _{0}\right) z_{2},...,\Gamma \left( \varphi ,\varphi _{0}\right)
z_{q}\right) \vspace*{1mm} \\
& \displaystyle=i_{\Gamma \left( \varphi ,\varphi _{0}\right) z}\omega
^{\prime }\left( \Gamma \left( \varphi ,\varphi _{0}\right) z_{2},...,\Gamma
\left( \varphi ,\varphi _{0}\right) z_{q}\right) \vspace*{1mm} \\
& \displaystyle=\left( \varphi ,\varphi _{0}\right) ^{\ast }\left( i_{\Gamma
\left( \varphi ,\varphi _{0}\right) z}\omega ^{\prime }\right) \left(
z_{2},...,z_{q}\right) ,
\end{array}$$ for any $z_{2},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$, it results the conclusion of affirmation 2$.$

3\. Let $\omega ^{\prime }\in \Lambda ^{q}\left( F^{\prime },\nu ^{\prime
},N^{\prime }\right)$ and $z_{0},...,z_{q}\in \Gamma \left( F,\nu ,N\right)$ be arbitrary. Since $$\begin{array}{l}
\left( \left( \varphi ,\varphi _{0}\right) ^{\ast }d^{F^{\prime }}\omega
^{\prime }\right) \left( z_{0},...,z_{q}\right) =\left( d^{F^{\prime
}}\omega ^{\prime }\right) \left( \Gamma \left( \varphi ,\varphi _{0}\right)
z_{0},...,\Gamma \left( \varphi ,\varphi _{0}\right) z_{q}\right) \vspace*{
1mm} \\
=\overset{q}{\underset{i=0}{\tsum }}\left( -1\right) ^{i}\Gamma \left(
Th^{\prime }\circ \rho ^{\prime },h^{\prime }\circ \eta ^{\prime }\right)
\left( \Gamma \left( \varphi ,\varphi _{0}\right) z_{i}\right) \vspace*{1mm}
\\
\hfill \cdot \omega ^{\prime }\left( \left( \Gamma \left( \varphi ,\varphi
_{0}\right) z_{0},\Gamma \left( \varphi ,\varphi _{0}\right) z_{1},...,
\widehat{\Gamma \left( \varphi ,\varphi _{0}\right) z_{i}},...,\Gamma \left(
\varphi ,\varphi _{0}\right) z_{q}\right) \right) \vspace*{1mm} \\
+\underset{0\leq i<j}{\tsum }\left( -1\right) ^{i+j}\cdot \omega ^{\prime
}\left( \Gamma \left( \varphi ,\varphi _{0}\right) \left[ z_{i},z_{j}\right]
_{F,h},\Gamma \left( \varphi ,\varphi _{0}\right) z_{0},\Gamma \left(
\varphi ,\varphi _{0}\right) z_{1},...,\right. \vspace*{1mm} \\
\hfill \left. \cdot \widehat{\Gamma \left( \varphi ,\varphi _{0}\right) z_{i}
},...,\widehat{\Gamma \left( \varphi ,\varphi _{0}\right) z_{j}},...,\Gamma
\left( \varphi ,\varphi _{0}\right) z_{q}\right)
\end{array}$$ and $$\begin{array}{l}
d^{F}\left( \left( \varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime
}\right) \left( z_{0},...,z_{q}\right) \vspace*{1mm} \\
=\overset{q}{\underset{i=0}{\tsum }}\left( -1\right) ^{i}\Gamma \left(
Th\circ \rho ,h\circ \eta \right) \left( z_{i}\right) \cdot \left( \left(
\varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime }\right) \left(
z_{0},...,\widehat{z_{i}},...,z_{q}\right) \vspace*{1mm} \\
+\underset{0\leq i<j}{\tsum }\left( -1\right) ^{i+j}\cdot \left( \left(
\varphi ,\varphi _{0}\right) ^{\ast }\omega ^{\prime }\right) \left( \left[
z_{i},z_{j}\right] _{F,h},z_{0},...,\widehat{z_{i}},...,\widehat{z_{j}}
,...,z_{q}\right) \vspace*{1mm} \\
=\overset{q}{\underset{i=0}{\tsum }}\left( -1\right) ^{i}\Gamma \left(
Th\circ \rho ,h\circ \eta \right) \left( z_{i}\right) \cdot \omega ^{\prime
}\left( \Gamma \left( \varphi ,\varphi _{0}\right) z_{0},...,\widehat{\Gamma
\left( \varphi ,\varphi _{0}\right) z_{i}},...,\Gamma \left( \varphi
,\varphi _{0}\right) z_{q}\right) \vspace*{1mm} \\
+\underset{0\leq i<j}{\tsum }\left( -1\right) ^{i+j}\cdot \omega ^{\prime
}\left( \Gamma \left( \varphi ,\varphi _{0}\right) \left[ z_{i},z_{j}\right]
_{F,h},\Gamma \left( \varphi ,\varphi _{0}\right) z_{0},\Gamma \left(
\varphi ,\varphi _{0}\right) z_{1},...,\right. \vspace*{1mm} \\
\left. \widehat{\Gamma \left( \varphi ,\varphi _{0}\right) z_{i}},...,
\widehat{\Gamma \left( \varphi ,\varphi _{0}\right) z_{j}},...,\Gamma \left(
\varphi ,\varphi _{0}\right) z_{q}\right)
\end{array}$$ it results the conclusion of affirmation 3. *q.e.d.*

**Definition 4.9** For any $q\in \overline{1,n}$ we define $$\begin{array}{c}
\mathcal{Z}^{q}\left( F,\nu ,N\right) =\left\{ \omega \in \Lambda ^{q}\left(
F,\nu ,N\right) :d\omega =0\right\} ,
\end{array}$$ the set of *closed differential exterior* $q$*-forms* and $$\begin{array}{c}
\mathcal{B}^{q}\left( F,\nu ,N\right) =\left\{ \omega \in \Lambda ^{q}\left(
F,\nu ,N\right) :\exists \eta \in \Lambda ^{q-1}\left( F,\nu ,N\right)
~|~d\eta =\omega \right\} ,
\end{array}$$ the set of *exact differential exterior* $q$*-forms*.
