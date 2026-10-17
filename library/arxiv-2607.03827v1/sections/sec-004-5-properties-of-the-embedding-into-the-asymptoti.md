---
doc_id: arxiv-2607.03827v1
doc_title: "Affine cellular algebras and asymptotic algebras"
section_id: sec-004-5-properties-of-the-embedding-into-the-asymptoti
section_title: "Properties of the embedding into the asymptotic algebra"
section_number: 5
pages: 17-22
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.953
doc_brief: "Affine cellular algebras and asymptotic algebras — The theory of affine cellular algebras A is extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between"
---
In this section we will provide further information related with the embedding
into the asymptotic algebra by considering the restriction functor associated to the
embedding $A\to \asym$. Moreover we will derive a geometric property of
the embedding. This enhances in particular Theorems \ref{TheoremB} and
\ref{TheoremC}.

Throughout this section, $A$ is an affine cellular algebra with cell chain $\{J_i : 1\leq i \leq n\}$ as in  (\ref{notation:cellchain}) and cell data $(B_i,\sigma_i,\Delta_i, \psi^{(i)}, \alpha_i)$ as in (\ref{notation:celldata}), with $d_i=\rank_{B_i}(\Delta_i)$, such that no determinant $\det(\psi^{(i)})$ is a zero-divisor in $B_i$ and such that the embedding $\Theta: A \to \asym$ into its asymptotic algebra $\asym=\asym_n \times \cdots \times \asym_1$, with $\asym_k=M_{d_k}(B_k)$, is given by (\ref{notation:embedding}), i.e. $\Theta(a)=(\Theta_n(a),\ldots, \Theta_1(a))$, for all $a\in A$. Then, for $a\in J_k'$, we have $\Theta_k =  \alpha_k(\overline{a})\psi^{(k)}$, where $\overline{a}=a+J_{k-1}$. The embedding $\Theta$ induces a restriction functor $$F: \asym\mathrm{-Mod} \to A\mathrm{-Mod},$$ where for $X\in \asym\mathrm{-Mod}$ the additive group $X$ becomes a left $A$-module $F(X)$ by letting
\begin{equation}\label{eq:def-module-structure}
 a\cdot x := \Theta(a)x, \qquad \forall a\in A, \: x\in X.
\end{equation}
All components $\asym_k = M_{d_k}(B_k)$ are unital algebras, with identity $\mathbf{I}_{d_k}$. The identity element of $\asym$ is $\left(\mathbf{I}_{d_n},\ldots, \mathbf{I}_{d_1}\right)$. We will identify elements $a\in \asym_k$ with the element $a\mathbf{I}_{d_k} = (0,\cdots, a, \cdots, 0) \in \asym$ and any left $\asym$-module $X$ decomposes into $X=X_n\times \cdots \times X_1$, where $X_k = \asym \mathbf{I}_{d_k} X =  \asym_k X$ is a left $\asym_k$-module. Hence, any element of $X$ can be uniquely written as $x=(x_n,\ldots, x_1)$ with $x_i\in X_i$ and the $A$-action of $a\in A$ on $x\in F(X)$ is given by $a\cdot x = \Theta(a)x = (\Theta_n(a) x_n, \ldots, \Theta_1(a)x_1)$. Moreover, for $\asym$-modules $X$ and $Y$, 
$\Hom_{\asym}(X,Y) = \prod_{k=1}^n \Hom_{\asym_k}(X_k,Y_k).$ 
Recall that by definition of an affine cellular algebra $A=\bigoplus_{i=1}^n J'_i$ as $k$-module, where $J_i = \bigoplus_{j\leq i} J'_j$.


\begin{lemma}\label{lem:idempotent} 
Let $1\leq k ,l \leq n$ and assume that $J_k/J_{k-1}$ is idempotent. The following statements hold for an $\asym_k$-module $X$ and an $\asym_l$-module $Y$.
\begin{enumerate}
    \item $J'_k\cdot X = X$.
    \item $\Hom_A(F(X),F(Y))=0$, if $k<l$.
    \item $\Hom_A(F(X),F(Y))=\Hom_{\asym}(X,Y)$, if $k=l$.
\end{enumerate}
\end{lemma}

\begin{proof}
Note, that the $A$-action on $X$ is completely determined by $\Theta_k$, i.e. $a\cdot x = \Theta(a)x = \Theta_k(a)x$, for any $a\in A$ and $x\in X$, because $\asym_iX=0$, for $i\neq k$.
Moreover, since $J_k/J_{k-1}$ is idempotent, $\asym_k\psi^{(k)}\asym_k=\asym_k$ holds.

(1) Using (\ref{eq:image-theta-k}), we have  $J_k' \cdot X= \Theta_k(J_k')\asym_k X =\asym_k\psi^{(k)}\asym_kX = \asym_k X = X.$

(2) Let $f:F(X)\to F(Y)$ be $A$-linear. By (1) and $\Theta_l(J'_k)=0$, for $l>k$:
$$f(X)=f(J'_k\cdot X)=J'_k\cdot f(X) \subseteq J'_k\cdot Y = \Theta_l(J'_k)Y=0.$$

(3) We always have $\Hom_{\asym}(X,Y)\subseteq \Hom_{A}(F(X),F(Y))$. Assume $k=l$ and let $f:F(X)\to F(Y)$ be  $A$-linear. We need to show that $f$ is $\asym$-linear. 
Since $\alpha_k(J_k/J_{k-1})=\asym_k$, for any $y \in \asym_k$, there exists $\tilde{y}\in J_k'$ such that
$\Theta_k(\tilde{y}) = \alpha_k(\overline{\tilde{y}})\psi^{(k)}=y\psi^{(k)}.$ In particular, $a(\tilde{y}\cdot z) = ay\psi^{(k)}z = \widetilde{ay}\cdot z$, for any $a,y,z\in \asym_k$.
Furthermore, since $\asym_k\psi^{(k)}\asym_k = \asym_k$, there exist elements $y_i, z_i\in \asym_k$, such that 
\begin{equation} \mathbf{I}_{d_k} 
    = \sum_{i=1}^t y_i \psi^{(k)} z_i
        =  \sum_{i=1}^t \tilde{y_i}\cdot z_i.\end{equation}

Thus, any element $a\in \asym_k$ can be written as $a=\sum_{i=1}^t \widetilde{ay_i}\cdot z_i$. Then, for $x\in X$:
\begin{eqnarray*}
    f(ax)
    = f\left(\sum_{i=1}^t \widetilde{ay_i} \cdot z_ix\right)
    = \sum_{i=1}^t \widetilde{ay_i} \cdot f ( z_ix )
    = \sum_{i=1}^t a \tilde{y_i}\cdot f ( z_ix )
    = a f\left(\sum_{i=1}^t \tilde{y_i}\cdot z_ix \right) = af(x).
\end{eqnarray*}
Hence $f$ is $\asym_k$-linear and also $\asym$-linear, since $\asym_i X = 0$, for $i\neq k$.
\end{proof}


A module is said to be {\em torsionless} provided it can be embedded into a projective (free) module. 

\begin{lemma}\label{lem:torsionless} Let  $1\leq l < k \leq m$,  $X$ a  $\asym_k$-module and $Y$ a torsionless $\asym_l$-module.  If $\det(\psi^{(l)})$ is a not a zero-divisor in $B_l$, then  $\Hom_A(F(X),F(Y))=0$. \end{lemma}

\begin{proof}
Since $\det(\psi^{(l)})$ is a not a zero-divisor in $B_l$, $\Ann_{P}(\psi^{(l)})=0$, for any free $\asym_l$-module $P=\asym_l^{(I)}$. In particular, 
$\Ann_{Y}(\psi^{(l)})=0$, for any torsionless $\asym_l$-module $Y$.

Let $f\in \Hom_A(F(X),F(Y))$. Then $\psi^{(l)} f(X) \subseteq  J_l' \cdot f(X) = f(J'_l\cdot X) = f(\Theta_k(J_l')X) = 0$, since  $\Theta_k(J_l')=0$ as $l<k$.  Thus, $f(X)\subseteq \Ann_Y(\psi^{(l)})=0$ and $f=0$.
\end{proof}


Let $\cT(\asym)$ denote the class of torsionless left $\asym$-modules. The restriction
functor $F:\cT(\asym) \to A\mathrm{-Mod}$ is fully faithful on this subcategory.

\begin{theorem}[Theorem \ref{TheoremB}] \label{TheoremBtext}
  Let $A$ be an affine cellular algebra with an affine cell chain such that
  all occurring affine cell ideals are idempotent and no determinant of their
  respective swich matrix is a zero-divisor.
  Then the embedding
  $\Theta: A \to \asym$ induces a fully faithful restriction functor
  $F: \cT(\asym) \to A\mathrm{-Mod}$, between torsionless $\asym$-modules and
  $A$-modules.
\end{theorem} 
\begin{proof}
  Let $X=\prod_{i=1}^n X_i$ and $Y=\prod_{i=1}^n Y_i$ be any torsionless
  $\asym$-modules. 
  As  $J_k/J_{k-1}$ is idempotent, $\Hom_A(F(X_k),F(Y_l)) = 0$ for
  all $k<l$, by Lemma \ref{lem:idempotent}.
By Lemma \ref{lem:torsionless}, $\Hom_A(F(X_k),F(Y_l)) = 0$ for $k>l$. Furthermore, $\Hom_A(F(X_k),F(Y_k) = \Hom_{\asym}(X_k,Y_k)$, for all $k$, by Lemma \ref{lem:idempotent}. Therefore,
$$\Hom_A(F(X),F(Y)) = \bigoplus_{k,l=1}^n \Hom_A(F(X_k),F(Y_l)) = \bigoplus_{k=1}^n \Hom_{\asym}(X_k,Y_k) = \Hom_{\asym}(X,Y).$$
\end{proof}









In the second part of this section we will compare the primitive spectrum of an affine cellular algebra with the primitive spectrum of its asymptotic algebra.
In \cite{BN} Baum and Nistor determined the periodic cyclic homology of the Iwahori-Hecke algebra $H_q$ at a proper root of unity $q$.  Their method is based on a general result, which states that a map called \emph{weakly spectrum preserving morphism} of finite type algebras induces an isomorphism in periodic cyclic homology. Furthermore, they showed that Lusztig's embedding $\phi_q: H_q \to J$, of the Iwahori–Hecke algebra $H_q$ into Lusztig's asymptotic algebra $J$ is weakly spectrum preserving. Here we will show that the embedding of an affine cellular algebra into its asymptotic algebra is weakly spectrum preserving if and only if all affine cell ideals appearing in the affine cell chain of the algebra are idempotent ideals (not necessarily generated by idempotent elements).

Let $R$ be a ring and denote by $\Prim(R)$ the set of (left) primitive ideals of $R$, where an ideal $P$ is called left primitive if it is the annihilator of a simple left $R$-module. Over a not necessarily unital ring $R$, a module $V$ is said to be simple if $R V\neq 0$ and $R v=V$ for all  $v\in V\backslash\{0\}$.


\begin{definition}[\cite{BN}]
  A $k$-algebra homomorphism  $\Theta:R\to S$ between two (not necessarily unital) $k$-algebras $R$ and $S$ is called \emph{spectrum preserving} if for any
  $P\in \Prim(S)$, $\Theta^{-1}(P)$ is contained in a unique primitive ideal of $R$ and the resulting map $\Theta^*: \Prim(S)\to \Prim(R)$ is a bijection.
\end{definition}

Given $B$ an affine commutative $k$-algebra, $n\geq 1$ and $\psi\in M_n(B)$, we denote, as above, the swich algebra $(M_n(B),\psi)$ by $\widetilde{M_n(B)}$. The map
$$ \varphi: \widetilde{M_n(B)} \to M_n(B), \qquad x\mapsto \varphi(x)=x\psi$$ is a  homomorphism of (not necessarily unital) $k$-algebras. We will examine, when $\varphi$ is spectrum preserving. A description of simple $\widetilde{M_n(B)}$-modules in terms of the simple $M_n(B)$-modules has been obtained in \cite[Theorem 3.10]{KXaffine} and will allow us to obtain the following correspondence between the primitive spectra of the two rings under the hypothesis that $\widetilde{M_n(B)}$ is idempotent. The correspondence from \cite{KXaffine} is revised in the proof of the following proposition for the sake of completeness.

Note that by \cite[Proposition 3.8]{KXaffine},
any left $M_n(B)$-module $V$ carries a natural structure of left
$\widetilde{M_n(B)}$-module, by defining 
$$ \tilde{a}\cdot v :=  \varphi(a)v = a\psi v, \qquad \forall \tilde{a}\in \widetilde{M_n(B)}, \: v\in V.$$
We denote this left $\widetilde{M_n(B)}$-module structure on $V$ by $V_\varphi$.


\newcommand{\tR}{?}


\begin{proposition} \label{primitives} Let $B$ be an affine $k$ algebra, $\psi\in M_n(B)$ and $\widetilde{M_n(B)}=(M_n(B), \psi)$. Assume $\widetilde{M_n(B)}$ is idempotent. There is a one-to-one correspondence between the primitive spectrum of $M_n(B)$ and the one of $\widetilde{M_n(B)}$ given by
$$\begin{array}{ccc}
\varphi^* : \Prim(M_n(B)) & \longrightarrow & \Prim(\widetilde{M_n(B)})\\[0.3cm]
P & \to & \{X\in M_n(B) : \psi X \psi \in P\}
\end{array}$$
\end{proposition}

\begin{proof}
Let $P\in \Prim(M_n(B))$. Then $P$ is a maximal ideal of $M_n(B)$ and $P=M_n(\mathfrak{m})$ for some ${\mathfrak m}$ a maximal ideal of $B$.

Let $V$ be a simple $M_n(B)$-module such that $P=\ann_{M_n(B)}(V)$. As above,
$V_{\varphi}$ is a $\widetilde{M_n(B)}$-module.


Note that $\ann_{V_{\varphi}}( \mathbf{I}_n)=\ann_V(\psi)$ is an $\widetilde{M_n(B)}$-submodule of $V_{\varphi}$ and consider $V_{\varphi}/ \ann_{V_{\varphi}}( \mathbf{I}_n )$. If $V_{\varphi}= \ann_{V_{\varphi}}(\mathbf{I}_n)$, then $\psi V=0$. As $\widetilde{M_n(B)}$ is idempotent, $M_n(B)\psi M_n(B)=M_n(B)$. As $V$ is a simple $M_n(B)$-module, it would follow that $V=M_n(B)V=M_n(B)\psi V=0$, a contradiction. Therefore $V_{\varphi}\neq \ann_{V_{\varphi}}(\mathbf{I}_n)$. Also $\widetilde{M_n(B)}( V_{\varphi}/ \ann_{V_{\varphi}}(\mathbf{I}_n))\neq 0$. Now take $W$ an $\widetilde{M_n(B)}$-submodule of $V_{\varphi}$ properly containing $\ann_{V_{\varphi}}(\mathbf{I}_n)$ and $w\in W\backslash \ann_{V_{\varphi}}(\mathbf{I}_n).$ We have that $M_n(B)\psi w\neq 0$ is a $M_n(B)$-submodule of $V$, hence $M_n(B)\psi w=V$ and $V_{\varphi}=V=M_n(B)\psi w=\widetilde{M_n(B)} \cdot w\subseteq W$. Hence 
$$V_{\varphi}/ \ann_{V_{\varphi}}(\mathbf{I}_n)$$
is a simple $\widetilde{M_n(B)}$-module and  
\begin{eqnarray*}\ann_{\widetilde{M_n(B)}}\left(V_{\varphi}/ \ann_{V_{\varphi}}(\mathbf{I}_n)\right)
&=&\{X\in M_n(B): X\psi v\in \ann_{V_{\varphi}}(\mathbf{I}_n),  \forall v\in V\}\\
&=&\{X\in M_n(B): \psi X\psi v=0, \forall v\in V\}.\end{eqnarray*}
Therefore 
\begin{equation}\label{UFF}
\ann_{\widetilde{M_n(B)}}\left(V_{\varphi}/ \ann_{V_{\varphi}}(\mathbf{I}_n)\right)= \{X\in M_n(B) : \psi X \psi \in P\}
\end{equation}
is a primitive ideal of $\widetilde{M_n(B)}$.





Let $Q\in \Prim(\widetilde{M_n(B)}$ and $E$ a simple left $\widetilde{M_n(B)}$-module such that $Q=\ann_{\widetilde{M_n(B)}}(E)$.  Consider the left $\widetilde{M_n(B)}$-module structure $M_n(B)_\varphi$ on $M_n(B)$. As $E$ is simple, $E=\widetilde{M_n(B)} e$ for any $e\in E\backslash\{0\}$. As in \cite[Proposition 3.10]{KXaffine} consider $q:M_n(B)_\varphi \rightarrow E$ such that $q(r)=\tilde{r}e$. Recall, that the product in $\widetilde{M_n(B)}$ is defined as $\tilde{a}\tilde{b}=\widetilde{a\psi b}$, for any $\tilde{a}, \tilde{b}\in \widetilde{M_n(B)}$. 
Given $\tilde{a}\in \widetilde{M_n(B)}, b\in M_n(B)$
$$\tilde{a}q(b)=\tilde{a}(\tilde{b}e)=(\tilde{a}\tilde{b})e=(\widetilde{a\psi b}) e=q(a\psi b)=q(\tilde{a}\cdot b).$$
So $q$ is a $\widetilde{M_n(B)}$-epimorphism and as $E$ is simple, $\Ker{q}$ is a maximal $\widetilde{M_n(B)}$-submodule of ${M_n(B)}_\varphi$. Let $Z$ be the centre of $M_n(B)$ and consider $Z\Ker{q}$ that contains $\Ker{q}$. Note that 
$$\tilde{a}\cdot (zx)=a\psi zx=z(\tilde{a}\cdot x)\in Z \Ker{q}, \qquad \forall a\in M_n(B), z\in Z, x\in \Ker{q}.$$
Hence $Z\Ker{q}$ is an $\widetilde{M_n(B)}$-submodule of $M_n(B)_\varphi$ that contains the maximal submodule $\Ker{q}$. Thus $\Ker{q}=Z\Ker{q}$ or $Z\Ker{q}=M_n(B)$. Assume  $Z\Ker{q}=M_n(B)$, then
$$E = q(M_n(B)) = q(\widetilde{M_n(B)}\cdot M_n(B))=q(M_n(B)\psi Z\Ker{q})=\widetilde{M_n(B)Z}q(\Ker{q})=0$$
a contradiction. Therefore,  $\Ker{q}=Z\Ker{q}$ and $\Ker{q}$ is a $Z$-module, as well as $E\cong M_n(B)/\Ker{q}$. As a $Z$-module, $E$ is  finitely generated and for every $\mathfrak{m}\in \MaxSpec(Z)$, $\mathfrak{m}E$ is an $\widetilde{M_n(B)}$-module, so $\mathfrak{m}E=0$ or $\mathfrak{m}E=E$.
If  $\mathfrak{m}E=E$ for all $\mathfrak{m}\in \MaxSpec(Z)$ using localisation and Nakayama's Lemma, we would have $E=0$ \cite[Proposition 3.8]{Atiyah}. Hence there is $\mathfrak{m}$, a maximal ideal of $Z=Z(M_n(B))\cong B$, such that $\mathfrak{m}E=0$. Thus $M_n(\mathfrak{m})\subseteq \Ker{q}$ and $q$ induces a $Z$-epimorphism $q':M_n(B)/M_n(\mathfrak{m}) \longrightarrow E$. Also $q'$ is a $\widetilde{M_n(B)}$-homomorphism from $(M_n(B)/M_n(\mathfrak{m}))_{\varphi}$ to $E$. Note that $\mathfrak{m}$ under the above conditions is unique.

As an $M_n(B)$-module, $M_n(B)/M_n(\mathfrak{m})\cong V_1\oplus\cdots\oplus V_n$  a direct sum of copies of a simple $M_n(B)$-modules with annihilator $M_n(\mathfrak{m})$. Since $q'\neq 0$, there is $i\in\{1,\ldots, n\}$ such that $q'(V_i)\neq 0$. For such an $i$, $\Ker{q'|_{(V_i)_{\varphi}}}=\ann_{(V_i)_{\varphi}}(\mathbf{I}_n)$, indeed if $x\in \Ker{q'}\cap (V_i)_{\varphi}$ and $\psi x\neq 0$, $M_n(B)\psi x=V_i$, for $V_i$ is a simple $M_n(B)$-module, and so $\widetilde{M_n(B)} x=(V_i)_{\varphi}$ and $q'((V_i)_{\varphi}) = q'(\widetilde{M_n(B)} x)=\widetilde{M_n(B)} q'(x)=0$, a contradiction. Thus $\Ker{q'}\cap V_i \subseteq \ann_{(V_i)_{\varphi}}(\mathbf{I}_n)$. If $x\in V_i$ is such that $\psi x=0$ then $\widetilde{M_n(B)} q'(x)=q'(\widetilde{M_n(B)} x)=q'(M_n(B)\psi x)=0$. Since $E$ is a simple $\widetilde{M_n(B)}$-module, if $q(x)\neq 0$,  $\widetilde{M_n(B)} q(x)$ would be $E$, hence $x\in \Ker{q'}$. It follows that, as an $\widetilde{M_n(B)}$-module, $E$ is isomorphic to $(V_i)_{\varphi}/ \ann_{(V_i)_{\varphi}}(\mathbf{I}_n)$, so by (\ref{UFF})
$$Q=\ann_{\widetilde{M_n(B)}}(E)=\ann_{\widetilde{M_n(B)}}((V_i)_{\varphi}/ \ann_{(V_i)_{\varphi}}(\mathbf{I}_n))=\{X\in M_n(B): \psi X\psi \in M_n(\mathfrak{m})\}.$$

Let $P_1, P_2$ be distinct elements of $\Prim(M_n(B))$. Since $P_1, P_2$ are maximal ideals, $P_1+P_2=M_n(B)$. As $P_1\subseteq \varphi^*(P_1)$ and $P_2\subseteq \varphi^*(P_2)$, if $\varphi^*(P_1) = \varphi^*(P_2)$, $M_n(B)=P_1+P_2\subseteq \varphi^*(P_1)$ and $\psi M_n(B) \psi \subseteq P_1$. By hypothesis $\widetilde{M_n(B)}$ is idempotent, so $M_n(B)\psi M_n(B)=M_n(B)$  and 
$M_n(B)=M_n(B)\psi M_n(B)\psi M_n(B)\subseteq P_1$ a contradiction, so $\varphi^*$ is injective.
\end{proof}


\begin{proposition}\label{prop:weakly}
The ring homomorphism $\varphi:\widetilde{M_n(B)}\to M_n(B)$ is spectrum preserving if and only if $\widetilde{M_n(B)}$ is idempotent.
 \end{proposition}

 \begin{proof}
Assume first that $\widetilde{M_n(B)}$ is not idempotent. It follows by \cite[Proposition 2.5(6)]{CKLS} that there is a maximal ideal $\mathfrak{m}$ of $B$ containing the ideal generated by all entries of $\psi$. Considering $M_n(\mathfrak{m})$, maximal ideal of $M_n(B)$, hence primitive, it follows that $\varphi(\widetilde{M_n(B)}) = M_n(B)\psi \subseteq M_n(\mathfrak{m})$, or in other words, $\varphi^{-1}(M_n(\mathfrak{m}))=\widetilde{M_n(B)}$. Thus, $\varphi^{-1}(M_n(\mathfrak{m}))$  is not contained in any primitive ideal of $\widetilde{M_n(B)}$ and $\varphi$ cannot be spectrum preserving, proving the only if part of the statement.

Assume now that $\widetilde{M_n(B)}$ is idempotent, take $P\in \Prim(M_n(B))$ and consider the bijection $\varphi^*$ between $\Prim(M_n(B))$ and $\Prim(\widetilde{M_n(B)})$, as in Proposition \ref{primitives}. By definition
$$P\subseteq \varphi^{-1}(P)=\{ X\in M_n(B) : X\psi \subseteq P\}\subseteq \varphi^*(P).$$
We need to show that $\varphi^*(P)$ is the unique primitive ideal containing $\varphi^{-1}(P)$. Suppose there exists a primitive ideal $Q\in \Prim(\widetilde{M_n(B)})$, such that $\varphi^{-1}(P)\subseteq Q$. By Proposition \ref{primitives}, $Q=\varphi^*(P_1)$, for some $P_1\in \Prim(M_n(B))$. In particular, $P_1\subseteq \varphi^{-1}(P_1) \subseteq Q$. Hence,  $P+P_1 \subseteq \varphi^{-1}(P) + \varphi^{-1}(P_1) \subseteq Q$. If $P\neq P_1$, then as both are maximal ideals, $P+P_1=M_n(B)$ and hence $Q=M_n(B)$, which is a contradiction. Thus  $\varphi^*(P)$ is the only primitive ideal that contains $\varphi^{-1}(P)$.
\end{proof}

\begin{definition}[\cite{BN}]
A morphism $\Theta: R\to S$ of $k$-algebras is called \emph{weakly spectrum preserving} if, and only if, there exist increasing filtrations
$0 = J_0 \subset J_1 \subset \cdots \subset J_n = R$ and 
$0 = I_0 \subset I_1\subset \cdots \subset I_n = S$ 
of two-sided ideals such that $\Theta(J_i)\subseteq I_i$ and the induced morphisms $J_i/J_{i-1} \to I_i/I_{i-1}$ are spectrum preserving.     
\end{definition}

Let $A$ be an affine cellular algebra $A$ with cell chain $0=J_0 \subset J_1 \subset \cdots \subset J_n=A$, such that each affine cell ideal $J_k/J_{k-1}$ has cell datum $(B_k, \sigma_k, \Delta_k,  \psi^{(k)},\alpha_k)$, i.e. $J_k/J_{k-1}\cong \Delta_k \otimes_{B_k}  \Delta_k' \cong \left( M_{d_k}(B_k), \psi^{(k)} \right)$ as $A$-bimodules, where $d_k=\rank_{B_k}(\Delta_k)$. Let $I_k = \asym_n \times   \cdots \times \asym_k$. Suppose no determinant $\det(\psi^{(k)})$ is a zero-divisor, then by Theorem \ref{TheoremAtext}, $\Theta$ is an embedding of $A$ into its asymptotic algebra $\asym = M_{d_n}(B_n)\times \cdots \times M_{d_1}(B_1)$. 
Using Proposition \ref{prop:weakly} we conclude
\begin{theorem}[Theorem \ref{TheoremC}] \label{TheoremCtext}
 Let $A$ be an affine cellular algebra with no determinant $\det(\psi^{(i)})$ being a zero-divisor. Then the embedding $\Theta:A\to \asym$ is weakly spectrum preserving if and only if all affine cell ideals $J_i/J_{i-1}$ are idempotent.
 \end{theorem}

 Now, \cite[Theorem 9]{BN} implies invariance of periodic cyclic homology
 under a general assumption in \cite{BN}. 
 
\begin{corollary}\label{pch}
  Let $A$ be an affine cellular algebra with no determinant $\det(\psi^{(i)})$
  being a zero-divisor and all $J_i/J_{i-1}$ being idempotent.
  If  $A$ is
  a finitely generated algebra over an affine $\mathbb{C}$-algebra, then the
  embedding $\Theta$ induces
 an isomorphism of periodic cyclic homology. 
\end{corollary}

In \cite{BN}, algebras with these properties are called finite type
algebras. Iwahori-Hecke algebras satisfy this conditions, and in \cite{BN}
the periodic cyclic homology of Iwahori Hecke algebras with parameter
not being zero and not a proper root of unity is determined by
using the embedding $\Theta$ into the asymptotic algebra and its property
of being weakly spectrum preserving. Cellular structures are not used in
\cite{BN}. Corollary \ref{pch} also applies to Brauer algebras and more
generally diagram algebras that are cellular in the sense of
\cite{GrahamLehrer} over an affine ground ring that is a $\mathbb{C}$-algebra.
