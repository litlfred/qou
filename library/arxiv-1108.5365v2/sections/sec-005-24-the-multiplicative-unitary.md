---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-005-24-the-multiplicative-unitary
section_title: "The multiplicative unitary"
section_number: 2.4
pages: 13-15
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.983
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:pre:mu}
Multiplicative unitaries are fundamental to the theory of quantum groups in the setting of $C^*$-algebras and von Neumann algebras, and to generalization of Pontryagin duality. In particular, a multiplicative unitary encodes all the structure maps of a quantum group and its dual. A very good exposition is given in \cite{T}.

First let us define the leg notation.
\begin{Def}Let $\cH$ be a Hilbert space and $W\in \cB(\cH\ox\cH)$ be a bounded operator. Then we define
$W_{ij}\in\cB(\cH^{\ox k})$ by letting $W$ acts on the factors at the position $i,j$. In particular, the operators
 $W_{12},W_{23},W_{13}\in \cB(\cH\ox\cH\ox\cH)$ are given by the formulas
\Eq{T_{12}:=T\ox Id_H,\tab T_{23}:=Id_H\ox T,}
\Eq{T_{13}:=\S_{12}T_{23}\S_{12}=\S_{23}T_{12}\S_{23},}
where $\S\in\cB(\cH\ox\cH)$ denotes the flip $f\ox g\mapsto g\ox f$.
\end{Def}

\begin{Def} Let $\cH$ be a Hilbert space. A unitary operator $W\in \cB(\cH\ox \cH)$ is called a multiplicative unitary if it satisfies the pentagon equation
\Eq{W_{23}W_{12}=W_{12}W_{13}W_{23},}
where the leg notation is used.
\end{Def}

Given a GNS representation $(\cH,\pi, \L)$ of a locally compact quantum group $\cA$, we can define a unitary operator \Eq{\label{WW}W^*(\L(a)\ox \L(b)) = (\L\ox \L)(\D(b)(a\ox 1)).}

It is known that $W$ is a multiplicative unitary \cite[Thm 3.16, Thm 3.18]{KV1}, and the coproduct on $\cA$ defining it can be recovered from $W$:
\begin{Prop} Let $x\in\cA \inj \cB(\cH)$ as operator. Then 
\Eq{W^*(1\ox x)W = \D(x)} as operators on $\cH\ox \cH$.
\end{Prop}
\begin{proof} For $x, f,g\in \cA$, we have $x\cdot \L(f)=\L(xf)$, hence
\begin{eqnarray*}
W^*((1\ox x)\cdot (\L(f)\ox \L(g)))&=&W^* (\L(f)\ox \L(xg))\\
&=&(\L\ox \L)(\D(xg)(f\ox 1))\\
&=&(\L\ox \L)(\D(x)\D(g)(f\ox 1))\\
&=&\D(x)\cdot (\L\ox \L)(\D(g)(f\ox 1))\\
&=&\D(x)W^*(f\ox g).
\end{eqnarray*}
\end{proof}

As a motivation, let us consider an example involving classical group:
\begin{Ex}\cite[Ex 7.1.4]{T}\cite{W} Let $G$ be a locally compact group with right Haar measure $\l$. Then the operator 
\Eq{(W f)(x,y):=f(xy,y)}
is a multiplicative unitary in $\cB(L^2(G,\l)\ox L^2(G,\l))=\cB(L^2(G\x G,\l\x\l))$. The pentagon equation for $W$ is equivalent to the associativity of the multiplication in $G$. Indeed, for $f\in L^2(G\x G\x G, \l \x \l \x \l)\simeq L^2(G,\l)^{\ox 3}$ and $x,y,z\in G$, we have
\begin{eqnarray*}
(W_{23}W_{12}f)(x,y,z)&=&f(x(yz),yz,z),\\
(W_{12}W_{13}W_{23}f)(x,y,z)&=&f((xy)z,yz,z).
\end{eqnarray*}
\end{Ex}

An important property of $W$ is that it encodes the information of the dual quantum group $\hat{\cA}$. By definition, $\hat{\cA}$ is the closure of the linear span of \Eq{\{(\w\ox 1)W: \w\in \cB(\cH)^*\}\sub\cB(\cH),} and we actually have 
\Eq{W\in M(\cA\ox \hat{\cA}),} where $M$ stands for the multiplier algebra.

Similarly, the multiplicative unitary for the dual $\hat{\cA}$ is given by $\hat{W}:=W_{21}^*$, hence it is known from the Pontryagin duality that $\hat{W}\in M(\hat{\cA}\ox \cA)$ as well. From the pentagon equation, we then obtain:

\begin{Cor}\label{DWW}
As an element $W\in M(\cA\ox \hat{\cA})$, together with the pentagon equation, we have 
\Eq{\label{DW}(\D\ox 1)W=W_{13}W_{23},}
\Eq{(1\ox \hat{\D})W=W_{13}W_{12}.}
\end{Cor}

Finally let us define the notion of ``manageability" introduced by Woronowicz \cite{W, WZ} that describes a class of well-behaved multiplicative unitary. It is shown that any manageable multiplicative unitary gives rise to a quantum group on the $C^*$-algebraic level.
\begin{Def}\label{manageable}
A multiplicative unitary $W$ is manageable if there exists a positive self-adjoint operator $Q$ acting on $\cH$ and a unitary operator $\til[W]$ acting on $\over[\cH]\ox \cH$ such that $\ker(Q)=\{0\}$,
\Eq{(Q\ox Q)W = W(Q\ox Q),} 
and
\Eq{\<x\ox u, W(z\ox y)\>_{\cH\ox \cH} = (\over[z]\ox Qu, \til[W](\over[x]\ox Q\inv y)\>_{\over[\cH]\ox \cH}}
for any $x,z\in \cH, y\in D(Q\inv), u\in D(Q)$.
\end{Def}
Here $\over[\cH]$ denote the complex conjugate of $\cH$, so that the map $x\in \cH \to \over[x]\in \over[\cH]$ is an anti-unitary map. The inner product on $\over[\cH]$ is given by $\<\over[x],\over[y]\>_{\over[\cH]}:=\<y,x\>_\cH$.
