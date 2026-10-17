---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL +"
section_id: sec-002-21-mellin-transform
section_title: "Mellin transform"
section_number: 2.1
pages: 8-13
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.925
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL + — We give complete detail of the description of the GNS representation of the quantum plane A and its dual ˆ A as"
---
\label{sec:Pre:Mellin}
In this subsection, let us recall the Mellin transform of a function and its properties. 

\begin{Thm}Let $f(x)$ be a continuous function on the half line $0<x<\oo$. Then its Mellin transform is defined by
\Eq{\phi(s):=(\cM f)(s)=\int_0^\oo x^{s-1} f(x)dx,} whenever the
integration is absolutely convergent for $a<Re(s)<b$. By the Mellin
inversion theorem, $f(x)$ is recovered from $\phi(s)$ by
\Eq{f(x):=(\cM\inv\phi)(x)=\frac{1}{2\pi}\int_{c-i\oo}^{c+i\oo}x^{-s}\phi(s)ds,}
where $c\in\R$ is any values in between $a$ and $b$.
\end{Thm}

We have the following analyticity theorem \cite{PK}:
\begin{Thm}\label{MTpole}
(Strip of analyticity) If $f(x)$ is a locally integrable function on $(0,\oo)$ such that it has decay property:
\Eq{\label{growth}f(x)=\left\{\begin{array}{cc}O(x^{-a-\e})&x\to 0^+\\O(x^{-b+\e})&x\to +\oo \end{array}\right.} 
for every $\e>0$ and some $a<b$, then the Mellin transform defines an analytic function $(\cM f)(s)$ in the strip
$$a<Re(s)<b.$$

(Analytic continuation) Assume $f(x)$ behaves algebraically for $x\to 0^+$, i.e. 
\Eq{f(x)\sim \sum_{k=0}^\oo A_k x^{a_k},} 
where $Re(a_k)$ increases monotonically to $\oo$ as $k\to\oo$. Then the Mellin transform $(\cM f)(s)$ can be
analytically continued into $Re(s)\leq a=-Re(a_0)$ as a meromorphic function with simple poles at the points $s=-a_k$
with residue $A_k$.

A similar analytic property holds for the continuation to the right half plane.

(Growth) If $f(x)$ is a holomorphic function of the complex variable $x$ in the sector $-\a<\arg x<\b$ where
$0<\a,\b\leq \pi$, and satisfies the growth property \eqref{growth} uniformly in any sector interior to the above
sector, then $(\cM f)(s)$ has exponential decay in $a<Re(s)<b$ with
\Eq{(\cM f)(s)=\left\{\begin{array}{cc}O(e^{-(\b-\e)t})&t\to+\oo\\O(e^{(\a-\e)t})&t\to -\oo \end{array}\right.} 
for any $\e>0$ uniformly in any strip interior to $a<Re(s)<b$, where $s=\s+it$.

(Parseval's Formula) 
\Eq{\int_0^\oo f(x)g(x)x^{z-1}dx =\frac{1}{2\pi i}\int_{c-i\oo}^{c+i\oo} (\cM f)(s)(\cM g)(z-s)ds,} 
where $Re(s)=c$ lies in the common strip for $\cM f$ and $\cM g$. In
particular we have 
\Eq{\int_0^\oo |f(x)|^2 dx =\frac{1}{2\pi}\int_{-\oo}^\oo |(\cM f)(\frac{1}{2}+it)|^2dt.}
\end{Thm}




\subsection{Weight and multiplier algebra of a $C^*$-algebra}\label{sec:pre:C*}
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




\subsection{GNS representation and Tomita-Takesaki's theory}\label{sec:pre:GNS}
Let us recall the main objects in the study of GNS representation of a $C^*$-algebra (see e.g. \cite{KV1}).

\begin{Def} A Gelfand-Naimark-Segal (GNS) representation of a $C^*$-algebra $\cA$ with a weight $\phi$ is a triple
$$(\cH, \pi, \L),$$
where $\cH$ is a Hilbert space, $\L:\cA\to\cH$ is a linear map, and $\pi:\cA\to\cB(\cH)$ is a representation of $\cA$ on $\cH$ such that $\L(\cN)$ is dense in $\cH$, and
\begin{eqnarray}
\pi(a)\L(b)&=&\L(ab) \tab\forall a\in\cA,b\in \cN,\\
\<\L(a),\L(b)\>&=&\phi(b^*a)\tab\forall a,b\in\cN,
\end{eqnarray}
where $\cN=\{a\in\cA: \phi(a^*a)<\oo\}$.
\end{Def}

The Tomita-Takesaki's Theory \cite{Ta,T} provides a detailed description of the GNS-construction in the von Neumann algebraic setting:
\begin{Def} Giving a weight $\phi$ that determines the Hilbert space structure by the GNS construction, the operator
\Eq{\label{T}T: x\to x^*} is closable and has a polar decomposition as 
\Eq{T=J\DD^{\frac{1}{2}},}
where $J$ is called the modular conjugation, and $\DD$ is called the modular operator.
\end{Def}

A very important property of $J$ is the following
\begin{Thm}[Murray-von Neumann]\label{MvN} Let $M$ be the completion of $\cA\sub \cB(\cH)$ in the weak operator topology as a von Neumann algebra. Then considering $M\sub \cB(\cH)$, we have
\Eq{JM J=M',}
where $M'$ is the commutant of $M$.
\end{Thm}

\begin{Def} For $x\in\cA$, the operator
\Eq{\s_t^{\phi}(x) := \DD^{it}x\DD^{-it}} is called the modular automorphism group.

We have $\phi(a^*b) = \phi(b\s_0^\phi(a^*))$

\end{Def}

On the Hopf * algebra level, we have the following properties:

\begin{Prop}
The antipode $S$ has a polar decomposition \Eq{S=\t_{-i/2}\circ R,}
where $\t_{-i/2}$ denotes the analytic generator of $(\t_t)_{t\in\R}$, called the \emph{scaling group}, which is a group of automorphisms of $M$, and $R$, called the \emph{unitary antipode}, is an anti-automorphism of $M$. 

We have $R^2=1$ and $S^2=\t_{-i}$.

\end{Prop}

Finally some properties concerning the left and right invariant Haar functional:
\begin{Prop}
The left invariant Haar functional $\phi$ and right invariant Haar functional $\psi$ are related by $\psi=\phi \circ R$.

We have \Eq{\phi\circ\t_t=\nu^{-t}\phi,\tab \psi\circ\s_t^{\phi}=\nu^{-t}\psi,}where $\nu>0$ is called the scaling constant.

Furthermore there exists an element $\d\in \cA$ such that $$\s_t^\phi(\d)=\nu^t\d,$$ where $\d\in \cA$ is called the modular element.
\end{Prop}

\begin{Prop} \label{GNSright}The map $\L_R: \cA\to \cH$ defined by
\Eq{\L_R(a):=\L_L(a\d^{-\frac{1}{2}}),} gives the GNS representation of $\cA$ with the right Haar functional on the same space $\cH$, where $\d$ is the modular element defined above.
\end{Prop}
