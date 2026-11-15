---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-014-p-and-l-monoids
section_title: "P and L Monoids"
section_number: null
pages: 70-74
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.977
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:PLmonoids}
Inspired by the list of relations which define the $G_1$ and $G_2$ presentations of $\operatorname{Cob}(3)_{S^2}$, we define the following monoids in symmetric monoidal categories, in anticipation that they will come from a 3d TFT.

\begin{defn} \label{defn:Sketch, P/L monoids}
(Sketch, P/L monoids) Let $(A, 1, m, tr, m^\vee)$ be a commutative Frobenius monoid in a symmetric monoidal category $(\mathcal{C}, \otimes , 1_{\otimes })$. We say that $A$ is a P-monoid if there exist endomorphisms $e_p \in \operatorname{End}_{\mathcal{C}}(A)   $ where $p$ is a diffeomorphism class of oriented irreducible prime 3 manifolds, satisfying 
\begin{enumerate}
\item (Prime commutativity) $e_p \circ e_{p'}=e_{p'} \circ  e_p $ 
\item (Legs and waist relations) $e_p \circ m = m \circ (e_p \otimes id_A) = m\circ (id_A \otimes e_p)$
\item (Colegs and cowaist relations) $m^\vee \circ e_p = (e_p \otimes id_A) \circ m^\vee = (id_A \otimes e_p) \circ m^\vee$.
\end{enumerate}

We say that $A$ is a $L$-monoid if there exist morphisms $1_p \in \operatorname{Hom}_{\mathcal{C}}(1_ \otimes , A) $ where $p$ is a diffeomorphism class of irreducible oriented prime 3 manifolds, satisfying 
\begin{enumerate}
\item (Legs relations) $m \circ (1_p \otimes id_A) = m\circ (id_A \otimes 1_p)$.
\end{enumerate}
\end{defn}

The sketch definition has an immediate consequence:

\begin{lemma} \label{lemma:PLbijection}
There is a bijection of $P$ monoids and $L$ monoids.
\end{lemma}

\begin{proof}
Let $(A,1,m,tr, m^\vee)$ be a $P$ monoid, with $e_p$ a prime endomorphism. We may define the corresponding prime unit as $1_p = e_p \circ 1$.  

Similarly if $A$ is an $L$ monoid with $1_p$ a prime unit, we may define the corresponding prime endomorphism $e_p$ as $e_p = m \circ (1_p \otimes id_A) = m \circ (id_A \otimes 1_p)$.

It is easy to check that the proposed prime units and prime endomorphisms satisfy the desired conditions.
\end{proof}

\begin{rmk}
By essentially the same proofs of propositions \ref{waistfromCF} - \ref{colegsfromCF}, not all of the conditions above are necessary. Proposition \ref{prop:LlegsfromCF} shows that the legs relations for $A$ to be an $L$-monoid is induced by commutativity of $A$ being a commutative Frobenius algebra. Hence all commutative Frobenius monoids equipped with morphisms $1_p \in \operatorname{Hom}_{\mathcal{C}}(1_ \otimes , A) $, where $p$ is a diffeomorphism class of irreducible oriented prime 3 manifold, is an $L$-monoid. Similarly, proposition \ref{primecommfromCF}, \ref{waistfromCF}, \ref{colegsfromCF}, and \ref{cowaistfromCF} shows that prime commutativity, waist relations, colegs and cowaist relations are implied by commutative Frobenius relations and legs relations. Therefore any commutative Frobenius monoid equipped with prime endomorphisms $e_p \in \operatorname{Hom}_{\mathcal{C}}(A) $ satisfying the legs relations $m\circ (e_p \otimes id_A) = m\circ (id_A \otimes e_p)$ is a $P$-monoid.
\end{rmk}

\begin{mycom}
In light of lemma \ref{lemma:PLbijection} and the previous remark, one may wonder why there is a slight asymmetry between $P$ monoids and $L$ monoids. Both are commutative Frobenius algebras, both come equipped with maps labelled by diffeomorphism classes of oriented prime 3 manifolds, yet $P$ monoids require that the maps satisfy some relations while $L$ monoids don't. This is because for any commutative Frobenius object $X$ there is a canonical injection \[
\operatorname{Hom}_{\mathcal{C}}(1_{\otimes }, X)  \hookrightarrow \operatorname{End}_{\mathcal{C}}(X) 
.\]
sending $f: 1_ \otimes \to X$ to $m \circ (f \otimes id_X) \circ \lambda^{-1}_X : X \cong 1_{\otimes } \otimes X \to X \otimes X \to X $.

Hence, heuristically speaking, one may find that there are more endomorphisms. The legs relations say that only those induced by a prime unit are prime endomorphisms in a $P$-monoid. This is best illustrated in the following two examples.
\end{mycom}

\begin{prop}
If $(\mathcal{C}, \otimes , 1_ \otimes )$ is the category $(\textbf{Sets}, \times, \left\{ * \right\} )$, then a prime endomorphism $e_p$ of a $P$ monoid of $\mathcal{C}$ acts by multiplication by the element $1_p(*)=e_p(1_A) $, where $1_p$ is the prime unit of the corresponding $L$ monoid.
\end{prop}

\begin{proof}
Let $A$ be a $P$ monoid and $e_p:A \to A$ be a prime endomorphism. Then it satisfy the legs and waist relation $ e_p \circ m = m\circ (e_p \otimes id_A) = m\circ (id_A \otimes e_p) : A \otimes A \to A$. Meaning that \[
e_p(a \cdot b) = e_p(a) \cdot b = a\cdot e_p(b)
.\]
Let $1_A \in A$ be the multiplicative unit with respect to $m$. Then \[
e_p(a) = e_p(a \cdot 1_A) = e_p(a) \cdot 1_A = a \cdot e_p(1_A)
.\]
for all $a\in A$. Therefore $e_p$ acts by multiplication by the element $e_p(1_A)$. 

Since $1_A\in A$ is the image of the unit map $1: \left\{ * \right\} \to A$, we may identify $e_p(1_A)=e_p(1(*)) $ with the composition $e_p \circ 1$. By lemma \ref{lemma:PLbijection}, the composition $1_p = e_p \circ 1$ is the prime unit in the corresponding $L$ monoid. 
\end{proof}

\begin{rmk}
The same proof establishes that in the category $(\text{Veck}_k, \otimes , k)$ a prime endomorphism $e_p$ acts by multiplication by the element $1_p: k \to A$, or equivalently $e_p \circ 1$ where $1: k \to A$ is the unit. Note that there are more linear endomorphisms of a vector space than linear maps of the form  $k\to A$. If $A$ is finite dimensional, the former is given by $n\times n$ matrices while the latter by $n\times 1$. Hence for there to be a bijection between $P$ and $L$ monoids (algebras), it is necessary to impose the legs relations on the prime endomorphisms to rule out the endomorphisms not induced by prime units.
\end{rmk}

We are now finally ready to give the most compact definition for $P$ and $L$ monoids.

\begin{defn} \label{defn:P/L monoids}
(P/L monoids) Let $(A, 1, m, tr, m^\vee)$ be a commutative Frobenius monoid in a symmetric monoidal category $(\mathcal{C}, \otimes , 1_{\otimes })$. Then the following are equivalent,

\begin{enumerate}
\item There exist morphisms $1_p \in \operatorname{Hom}_{\mathcal{C}}(1_ \otimes , A) $, where $p$ is a diffeomorphism class of oriented irreducible prime 3 manifolds. We say $A$ is a $L$-monoid.
\item There exist endomorphisms $e_p \in \operatorname{End}_{}(A) $ that satisfies $m\circ (e_p \otimes id_A) = m\circ (id_A \otimes e_p)$, where $p$ is a diffeomorphism class of oriented irreducible prime 3 manifolds. We say $A$ is a $P$-monoid.
\end{enumerate}
The equivalence is exhibited by $1_p = e_p \circ 1$ and $e_p = m \circ (1_p \otimes id_A) = m \circ (id_A \otimes 1_p)$.
\end{defn}

Restricting ourselves to the setting of $(\text{Vect}_k, \otimes , k)$, we can say a bit more about the prime units and prime endomorphisms:

\begin{defn} \label{defn:P/L algebras}
(P/L algebras) Let $(A,1,m,tr,m^\vee)$ be a commutative Frobenius algebra over $k$. We say $A$ is a $L$ algebra if there are elements $\left\{ 1_p \in A \right\} $ for all $p$ diffeomorphism classes of oriented irreducible prime 3 manifold. Equivalently, we say $A$ is a $P$ algebra if there are linear endomorphisms $\left\{ e_p \right\} $ that acts by multiplications by the element $1_p$. The equivalence is exhibited by $1_p = e_p(1)$ and $e_p = m \circ (1_p \otimes id_A) = m\circ (id_A \otimes e_p)$.
\end{defn}

\begin{thm} \label{thm:Z(S2)isPLmonoid}
Let $Z: \operatorname{Cob}(3)_{S^2} \to \mathcal{C}$ be a symmetric monoidal functor. Then $Z(S^2) $ is a $P/L$- monoid. In the case $\mathcal{C} = \operatorname{Vect}_k$, $Z(S^2)$ is a $P/L$-algebra.
\end{thm}

\begin{proof}
By proposition \ref{prop:CFcommFrob} and corollary \ref{cor:CFonlycommFrob}, $(Z(S^2), Z(1), Z(m), Z(tr), Z(m^\vee))$ is a commutative Frobenius algebra. The prime units $1_p \in \operatorname{Hom}_{\mathcal{C}}(1_ \otimes , Z(S^2)) $ are given by $Z([p\setminus D^3])$.
\end{proof}

\begin{thm} \label{thm:3dTFTgivesPLmonoid}
Let $Z: \operatorname{Cob}(3) \to \mathcal{C}$ be an oriented 3-dimensional topological field theory. Then $Z(S^2)$ is a $P/L$-monoid. In the case $\mathcal{C} = \operatorname{Vect}_k$, $Z(S^2)$ is a $P /L$-algebra.
\end{thm}

\begin{proof}
This is a corollary to the previous theorem \ref{thm:Z(S2)isPLmonoid}: every $3$-dimensional TFT induces a symmetric monoidal functor \[
\operatorname{Cob}(3)_{S^2} \hookrightarrow \operatorname{Cob}(3) \overset{Z}{\to } \mathcal{C}
.\]
sending $S^2$ to $Z(S^2)$. Therefore the image $Z(S^2)$ is a $P/L$-monoid/algebra.
\end{proof}


\begin{mycom}
What is surprising about $P/L$ algebras and their existence through theorem \ref{thm:Z(S2)isPLmonoid} and \ref{thm:3dTFTgivesPLmonoid} is their simplicity. The only novel structures on an $L$ algebra, besides the commutative Frobenius structures, are the existence of distinguished elements $1_p$ labelled by diffeomorphism classes of oriented irreducible prime 3 manifolds. There are no relations among them. This is a feature imposed by geometry, not a bug. The only novel structures on a $P$ algebra besides the commutative Frobenius structures are the distinguished endomorphisms $e_p$. Geometry forces these to act by multiplication by $1_p$, and there are no additional relations. Hence definition \ref{defn:P/L algebras} and theorem \ref{thm:3dTFTgivesPLmonoid} together can be thought of as a statement of the ``structural collapse'' on the algebraic structures of $Z(S^2)$.
\end{mycom}

\begin{rmk}
We make the following observations. Let $Z: \operatorname{Cob}(3) \to \mathcal{C}$ be an oriented 3-dimensional topological field theory. Denote by $e_M : Z(S^2) \to Z(S^2)$ the image $Z([M \setminus (D^3 \sqcup D^3)])$ where $M$ is a closed oriented 3 manifold. Then \[
e_{M \# N} = e_M \circ e_N = e_N \circ e_M
.\]
In particular, if $P, Q$ were oriented prime 3 manifolds, we recover the commutativity of prime endomorphisms \[
e_{P \# Q} = e_P \circ e_Q = e_Q \circ e_P
.\]
This means that the assignment $M \mapsto e_M$ is a monoid map \[
(\left\{ \text{Closed oriented 3 manifolds} \right\} / \cong , \#) \to \operatorname{End}_{\mathcal{C}}(Z(S^2)) 
.\]
In particular, this map sends $S^3$ to the identity $id_{Z(S^2)}$.
\end{rmk}

\begin{eg}
For $Z: \operatorname{Cob}(3) \to \text{Vect}_k$, where $k$ is algebraically closed, since the prime endomorphisms $\left\{ e_p \right\} $ are pairwise commuting, there exists a basis on $Z(S^2)$ such that all the $e_p$ are simultaneously upper-triangular. Equivalently, there exists a flag  \[
0 = V_0 \subset  V_1 \subset  \dots \subset V_n = Z(S^2) ,\quad \dim V_i = i
.\]
such that every $e_M$ preserves every $V_i$. Since each quotient $V_i / V_{i-1}$ is one-dimensional, $e_M$ acts on the quotient by scalar multiplications. Call this scalar $\chi_i(M) \in k$. Since $e_{M\# N} = e_M \circ e_N$, their actions on the quotient $V_i / V_{i-1}$ must satisfy \[
\chi_i(M \# N) = \chi_i(M) \chi_i (N)
.\]
Therefore this ``character theory'' of closed oriented 3 manifolds is completely determined by the character theory of oriented irreducible prime 3 manifolds. 
\end{eg}

\begin{eg}
In fact, we can say more in some special cases. Consider the same setup as above. Let $\mathcal{M}$ be the set of diffeomorphism classes of oriented irreducible prime 3 manifolds. Consider  \[
A = k \left[ \left\{ e_p | p\in \mathcal{M} \right\}  \right] 
.\]
This is a commutative subalgebra of $\operatorname{End}_{\mathcal{C}}(Z(S^2)) $. Since $Z(S^2)$ is finite dimensional, so is $A$. 

If $Z(S^2)$ happens to be semisimple as an $A$-module, then $Z(S^2)$ is a direct sum of simple $A$-modules. But $A$ is commutative, so all its simple modules are one-dimensional. Therefore \[
Z(S^2) \cong \bigoplus_\lambda k_\lambda
.\]

Over any line $k_\lambda$,  every $a\in A$ acts by some scalar. Denote this scalar as $\lambda(a)$ or, if $a=e_M$ for some closed 3 manifold $M$, by $\chi_\lambda (M)$. Then we still have \[
\chi_\lambda(M \# N) = \chi_\lambda(M) \chi_\lambda(N) 
.\]

The map $a \mapsto \lambda (a)$ defines $\lambda: A \to k$ for each $\lambda$. We may group the same\footnote{We consider two lines $k_{\lambda_1 }, k_{\lambda_2 } $ the same of $\lambda_1 = \lambda_2$ as maps $A \to k$. } $k_\lambda$'s together and obtain the direct sum decomposition of $Z(S^2)$ into spaces with the same character \[
Z(S^2) = \bigoplus_ \lambda V_\lambda 
.\]
Then each $e_M$ acts by  \[
e_M |_{V_\lambda } = \chi_\lambda (M) id_{V_\lambda}
.\]
or equivalently \begin{equation} \label{eqn:e_Mact}
e_M = \sum_{\lambda}^{ } \chi_{\lambda} (M) \pi_{\lambda}
.\end{equation}
where $\pi _{\lambda}: Z(S^2) \to V_\lambda$ are the projection maps.

The prime endomorphisms are those $e_M$ where $M$ is an oriented irreducible prime 3 manifold $P$. So these act by 
\begin{equation} \label{eqn:e_Pact}
e_P = \sum_{\lambda}^{ } \chi_{\lambda} (P) \pi_{\lambda}
.\end{equation}
\end{eg}

\begin{eg}
The example above provides a simple way of computing the invariants $Z(M)$ for any closed 3 manifold $M$. Let $Z : \operatorname{Cob}(3) \to \text{Vect}_k$ where $k$ is algebraically closed. If $Z(S^2)$ is semisimple as an $A$-module where $A$ is the commutative subalgebra $A = k[\left\{ e_p | p \in \mathcal{M} \right\} ] \subset  \operatorname{End}_{\text{Vect}_k}(Z(S^2)) $, then the example above shows that $e_P$ acts by equation \ref{eqn:e_Pact}. If $1: k \to Z(S^2)$ is the unit map and $tr: Z(S^2) \to k$ the trace map, then for any closed 3 manifold $M\cong P_1 \# \dots \# P_m$, we have \[
Z(M) = tr \circ e_M \circ 1 = \sum_{\lambda}^{ } (tr \circ \pi_{\lambda} \circ 1 ) \chi_\lambda(M) =  \sum_{\lambda}^{ } (tr \circ \pi_{\lambda} \circ 1 ) \prod_{i=1}^m \chi_\lambda(P_i)
.\]
Note however that the simplicity of this formula comes at the cost of needing to compute the characters $\chi_\lambda(P_i)$ which may be equally challenging as computing $Z(M)$ via other methods.
\end{eg}
