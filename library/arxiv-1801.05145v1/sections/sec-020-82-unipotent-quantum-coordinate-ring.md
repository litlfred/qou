---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-020-82-unipotent-quantum-coordinate-ring
section_title: "Unipotent quantum coordinate ring"
section_number: 8.2
pages: 58-60
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.92
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\label{subsec:unipotent}
Let us endow $U_q^+(\g) \tens U_q^+(\g)$ with the algebra structure defined by
$$(x_1 \tens x_2) \cdot (y_1 \tens y_2) = q^{-(\wt(x_2),\wt(y_1))}(x_1y_1 \tens x_2y_2).$$
Let $\Delta_\n$ be the algebra homomorphism $U_q^+(\g) \to U_q^+(\g)
\tens U_q^+(\g)$ given by
$$ \Delta_\n(e_i) = e_i \tens 1 + 1 \tens e_i.$$

Set
$$ A_q(\n) = \soplus_{\beta \in  \rl^-} A_q(\n)_\beta \quad \text{ where } A_q(\n)_\beta \seteq (U^+_q(\g)_{-\beta})^*.$$

Defining the bilinear form $\langle \ \cdot \ , \ \cdot \ \rangle\cl
(A_q(\n) \tens A_q(\n)) \times (U^+_q(\g) \tens U^+_q(\g))  \to \Q(q)$ by
$$ \langle \psi \tens \theta, x \tens y \rangle =\theta(x) \psi(y),$$
we  get an algebra structure on $A_q(\n)$  given by
$$(\psi \cdot \theta)(x) = \langle \psi \tens \theta, \Delta_\n(x) \rangle
= \theta(x_{(1)})\psi(x_{(2)})$$
where $\Delta_\n(x)=x_{(1)} \tens x_{(2)}$.

Since $U_q^+(\g)$ has a $U_q^+(\g)$-bimodule structure, so does
$A_q(\n)$.

We define the $\A$-form of $\An$ by
\eqn
&&\An_\A=\set{\psi\in\An}{\psi\bl\Up_\A\br\subset\A},
\eneqn
 and define the bar-involution $-$ on $\An$ by

$$\ol{\psi}(x)=\ol{\psi(\ol{x})} \quad\text{for $\psi\in\An$ and $x\in\Up$.}
$$

Note that the bar-involution is not a ring homomorphism but it satisfies
\eqn
&&\ol{\psi\;\theta\;}=q^{(\wt(\psi),\wt(\theta))}\;\ol{\theta}\;\ol{\psi}\quad
\text{for any $\psi$, $\theta\in\An$.}
\eneqn

For $i\in I$, we denote by $e_i^*$ the right action of
$e_i$ on $\An$.

\begin{lemma} For $u,v \in A_q(\n)$, we have  $q$-boson relations
\begin{align*}
e_i(uv) = (e_iu)v + q^{(\alpha_i,\wt(u))} u (e_iv) \  \text{ and }
 \ e_i^*(uv) = u(e_i^*v) + q^{(\alpha_i,\wt(v))} (e_i^*u)v.
\end{align*}
\end{lemma}

\begin{proof}
$$
\lan e_i(uv), x\ra=\lan uv, xe_i\ra= \lan u\tens v,\; \Delta_\n(xe_i)\ra.$$
If we set $\Delta_\n x=x_{(1)}\tens x_{(2)}$,
then we have
$$\Delta_\n(xe_i)=(x_{(1)}\tens x_{(2)})(e_i\tens 1+1\tens e_i)
=q^{-(\alpha_i,\wt(x_{(2)}))}(x_{(1)}e_i)\tens x_{(2)}+x_{(1)}\tens (x_{(2)}e_i).$$
Hence, we have
\begin{align*}
&\lan u\tens v,\; \Delta_\n(xe_i)\ra
=q^{-(\alpha_i,\wt(x_{(2)}))}u(x_{(2)})v(x_{(1)}e_i)+u(x_{(2)}e_i)v(x_{(1)})\\
&\hspace{5ex}=q^{(\alpha_i,\wt(u))}u(x_{(2)})\cdot (e_iv)(x_{(1)})+(e_iu)(x_{(2)})
\cdot v(x_{(1)})\\
&\hspace{5ex}=\lan q^{(\alpha_i,\wt(u))}u\tens(e_iv)+(e_iu)\tens v,\,\Delta_\n x\ra.
\end{align*}
The second  identity follows in a similar way.
\end{proof}

We define the map $\iota \cl  U_q^-(\g) \to A_q(\n)$ by
$$  \langle \iota(u),x \rangle = (u,\vph(x)) \quad \text{ for any } u \in U_q^-(\g) \text{ and } x \in U_q^+(\g).$$
 Since $(\ ,\ )$ is a non-degenerate bilinear form on $\Um$,
$\iota$ is injective.
The relation $$\langle \iota(e_i'u), x \rangle = (e_i'u,\vph(x)) =
(u,f_i \vph(x)) =(u, \vph(xe_i))=\lan \iota(u),x e_i \ran = \langle e_i \iota(u),x
\rangle,$$ implies that
\eqn \iota(e_i'u) = e_i \iota(u).
\eneqn


\begin{lemma} $\iota$ is an algebra isomorphism.
\end{lemma}

\begin{proof}
The map $\iota$ is an algebra homomorphism because $e_i'$ and $e_i$
both satisfy the same $q$-boson relation.
\end{proof}

Hence, the algebra $A_q(\n)$ has an upper crystal basis $(L^\up(A_q(\n)),B(A_q(\n)))$ such that
$B(A_q(\n)) \simeq B(\infty)$. Furthermore, $A_q(\n)$ has an upper global basis $$\B^\up(A_q(\n))=\{ G^\up(b) \}_{ \ b \in B(A_q(\n))}$$
induced by the balanced triple
$\bl \Q\tens\An_\A,\,L^\up(A_q(\n)),\,\overline{L^\up(A_q(\n))}\br$
 (see \eqref{eq:Bup}).

There exists an injective map
\eqn &&\oi_\lambda\cl  B(\lambda)\to B(\infty)
\eneqn
induced by the $\Up$-linear homomorphism
$\iota_\la\cl V(\lambda)\to A_q(\n)$ given by
$$v\longmapsto \big ( \Up \ni a\mapsto (av,u_\lambda)\big).$$
 The map $\oi_\lambda$   commutes with $\te_i$.
We have
$$
G^\low_\lambda(b)=G^\low(\oi_\lambda(b))u_\lambda
 \quad\text{and}\quad
\iota_\la G_\la^\up(b)=G^\up(\oi_\la(b))\quad\text{for any $b\in B(\lambda)$.}$$

\begin{remark}
Note that the multiplication on $\An$ given in \cite{GLS} is different from ours.
Indeed, by denoting
the product of $\psi$ and $\phi$  in \cite[\S4.2]{GLS} by $\psi \cdot \phi$,
 for $x \in U_q^+(\g)$,  we have
\eqn
(\psi \cdot \phi) (x) = \psi(x^{(1)}) \phi(x^{(2)}),
\eneqn
where $\Delta_+(x)=x^{(1)}q^{h_{(1)}} \otimes x^{(2)}q^{h_{(2)}}$  for $x^{(1)}, x^{(2)} \in U_q^{+}(\g),  \ h_{(1)}, h_{(2)} \in \wl^\vee$.
By Lemma \ref{lem:Deltan} below, we have
\eqn
(\psi \cdot \phi) (x) &&= \psi\bl q^{(\wt(x_{(1)}),\wt(x_{(2)}))} (x_{(2)}) \br \phi \bl x_{(1)} \br \\
&&=q^{(\wt(x_{(1)},\wt(x_{(2)}))} \psi(x_{(2)}) \phi(x_{(1)})
= q^{(\wt(\psi),\wt(\phi))} (\psi \phi)(x)
\eneqn
for $x \in U_q^+(\g)$, where $\Delta_\n(x)=x_{(1)} \tens x_{(2)}$.
In particular, we have a $\Q(q)$-algebra isomorphism
from $(\An, \cdot)$ to $\An$ given by
\eq \label{eq:isoAqn}
 x \mapsto q^{-\frac{1}{2}(\beta, \beta)} x \quad \ \text{for} \ x \in \An_{\beta}.
\eneq
Note also that
the bar-involution $-$ is a ring anti-isomorphism
between $\An$ and $(\An, \cdot)$.
\end{remark}
