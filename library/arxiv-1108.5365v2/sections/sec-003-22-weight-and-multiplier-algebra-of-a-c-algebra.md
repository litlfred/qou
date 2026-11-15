---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-003-22-weight-and-multiplier-algebra-of-a-c-algebra
section_title: "Weight and multiplier algebra of a C*-algebra"
section_number: 2.2
pages: 10-11
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:pre:C*}
In this subsection, we recall the definition of weights on a $C^*$-algebra, and the language of multiplier algebra. Most of the notions are adopted from \cite{KV1,T}. Let $\cA$ be a $C^*$-algebra and $\cA^+$ its positive self-adjoint elements.
\begin{Def} A weight on a $C^*$-algebra $\cA$ is a function $\phi: \cA^+\to [0,\oo]$ such that
\begin{eqnarray}
\phi(x+y)&=&\phi(x)+\phi(y),\\
\phi(rx)&=&r\phi(x),
\end{eqnarray}
for $x,y\in \cA^+, r\in \R_{>0}$.
\end{Def}
\begin{Def} Given a weight $\phi$ on $\cA$, we define
\begin{eqnarray}
\cM_{\phi}^+&=&\{a\in \cA^+: \phi(a)<\oo\},\\
\cN_{\phi}&=&\{a\in \cA: \phi(a^*a)<\oo\},\\
\cM_{\phi}&=&\mbox{span}\{y^*x: x,y\in \cN_{\phi}\}.
\end{eqnarray}
Then it is known that $\cM_{\phi}^+=\cM_{\phi}\cap \cA^+$, and that $\phi$ extends uniquely to a map $\cM_{\phi}\to \C$.
A weight is called faithful iff $\phi(a)=0\=> a=0$ for every $a\in \cA^+$.
\end{Def}

Next we recall a useful notion of a multiplier algebra. Let $\cB(\cH)$ be the algebra of bounded linear operators on a Hilbert space $\cH$.

\begin{Def}If $\cA\sub \cB(\cH)$ as operators, then the multiplier algebra $M(\cA)$ of $\cA$ is the $C^*$-algebra of operators
\Eq{M(\cA)=\{b\in \cB(\cH): b\cA \sub \cA, \cA b\sub \cA\}.}
In particular, $\cA$ is an ideal of $M(\cA)$.
\end{Def}
\begin{Ex} Important examples include
\Eq{M(\cK(\cH))=\cB(\cH),}
where $\cK(\cH)$ are compact operators on $\cH$, and
\Eq{M(C_0(X))=C_b(X),}
where $X$ is a locally compact Hausdorff space, $C_0(X)$ is the algebra of $\C$-valued functions on $X$ vanishing at infinity equipped with the sup-norm, and $C_b(X)$ is the $C^*$-algebra of all bounded continuous functions on $X$.
\end{Ex}

\begin{Prop}
Let $\cA$ and $\cB$ be $C^*$-algebras. A homomorphism $\phi:\cA\to M(\cB)$ is called non-degenerate if the linear span of $\phi(\cA)\cB$ and of $\cB\phi(\cA)$ are both equal to $\cB$. Then $\phi$ extends uniquely to a homomorphism $M(\cA)\to M(\cB)$. In particular, by taking $\cB=\C$, every weight $\w$ on $\cA$ has a unique extension to $M(\cA)$.
\end{Prop}

Using the notion of a multiplier algebra, the concept of a multiplier Hopf algebra is introduced in \cite{VD} (see also \cite{T}). In particular, the coproduct $\D$ of $\cA$ will be a non-degenerate homomorphism $\D:\cA\to M(\cA\ox \cA)$. The coassociativity is well-defined from the proposition above.

Given a multiplier Hopf * algebra $\cA$ with coproduct $\D$, we can define left and right invariance of a functional.
\begin{Def}\label{leftinv} A linear functional $h$ on $\cA$ is called a left invariant Haar functional if it satisfies
\Eq{(1\ox h)(\D x) = h(x)\cdot 1_{M(\cA)},}
where $1_{M(\cA)}$ is the unital element in $M(\cA)$. 

Similarly, a right invariant Haar functional satisfies
\Eq{(h\ox 1)(\D x)=h(x)\cdot 1_{M(\cA)}.}
\end{Def}
