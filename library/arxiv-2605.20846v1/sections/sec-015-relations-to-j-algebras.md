---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-015-relations-to-j-algebras
section_title: "Relations to J-Algebras"
section_number: null
pages: 74-78
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.984
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:Jalg}

\begin{defn} \label{defn:Trace of Surgery}
(Trace of Surgery) Let $M$ be an oriented $n$-manifold and $0\leq k\leq n$. Let $\phi : S^{k-1} \times D^{n-k} \hookrightarrow M$ be an embedding along which a $k$-handle is attached. The resulting manifold is \[
M' = M \cup_{\phi } (D^k \times D^{n-k})
.\]
The \textit{trace} of this handle attachment is the $(n+1)$-dimensional cobordism $W$ from $M$ to $M'$ obtained by attaching a $k$-handle to $M \times [0,1]$ along $M\times \left\{ 1 \right\} $: \[
W = (M \times [0,1]) \cup_{\phi } (D^k \times D^{n-k+1})
.\]
Its incoming boundary is $M \times \left\{ 0 \right\} $ and the outgoing boundary is the manifold $M'$.
\end{defn}

Recall \cite{juhasz2018defining}'s assignment of a $J$-algebra associated to a 3-dimensional oriented TFT $Z: \operatorname{Cob}(3) \to \text{Vect}_k$ \footnote{Note Juhasz's original paper the unusual convention is to denote by $\operatorname{Cob}(n)$ the category of $n$-manifolds and bordisms. We will not adopt this convention.} is denoted $J(Z)$ which consists of the following data 

\begin{enumerate}
\item $A_g = Z(\Sigma_g)$ is the vector space associated to the genus $g$ surface $\Sigma_g$ under $Z$, for all $g\geq 0$
\item linear maps $\alpha_g: A_g \to A_{g-1} $, which we call ``genus reduction maps.'' \\
This is the $Z$-image of trace of the attachment of a 2-handle around a hole, which eliminates it.
\item linear maps $\delta _{j, g-j}: A_g \to A_j \otimes A_{g-j}$, which we call ``splitting maps.'' \\
This is the $Z$-image of the trace of the splitting of $\Sigma_g $ into $\Sigma_j \amalg \Sigma_{g-j}$.
\item linear maps  $\mu _{i,j} : A_i \otimes A_j \to A_{i+j}$, which we call ``merging maps.''\\
This is the $Z$-image of the trace of the merging of $\Sigma_i \amalg \Sigma_j $ into $\Sigma_{i+j}$.
\item linear maps $\omega_g : A_g \to A_{g+1}$, which we call ``genus creation maps.'' \\
This is the $Z$-image of the trace of the attachment of a $1$-handle.
\item The linear map $tr: A_0 \to k$, which we call the ``trace map.'' \\
This is $Z(D^3)$, where $D^3 : S^2 \to \emptyset$.
\item The linear map $1: k \to A_0$, which we call the ``unit map.''\\
This is $Z(D^3)$, where $D^3 : \emptyset \to S^2 $
\item involutions $*_g: A_g \to A_g$
\item representations $\rho _g : MCG(\Sigma_g) \to \operatorname{Aut}(A_g) $.
\end{enumerate}

8 and 9 come from the following construction: First note that $MCG(\Sigma_g)$ here means $\operatorname{Diff}^+(\Sigma_g ) / \operatorname{Diff}^+_0(\Sigma_g )  $, namely isotopy classes of orientation preserving diffeomorphisms. The representations send a particular orientation-preserving diffeomorphism $d\in \operatorname{Diff}^+(\Sigma_g ) $ to $Z(Cyl(d))$ where $Cyl(d)$ is the mapping cylinder. In particular, there is a specific order $2$ diffeomorphism giving rise to the involutions $*_g$-- this is defined to be the diffeomorphism which sends the $\Sigma_g$ in its standard embedding in $\mathbb{R}^3$ to itself after performing a $\pi $-rotation about the $z$-axis.

The genus creation/reduction maps, and the splitting/merging maps are the images of the trace of elementary surgeries on surfaces. 

These data, along with appropriate compatibility conditions, fit into an algebraic structure named ``J-Algebras.'' A theorem by \cite{juhasz2018defining} is that these data completely determine the 3-dimensional TFT $Z$. In fact, the statement is stronger:

\begin{thm} \label{thm:Jalg=3dTFT}
[Juhasz] The assignment $Z \mapsto J(Z)$ is an equivalence between the symmetric monoidal category of 3-dimensional TFTs and $\textbf{J-Alg}$.
\end{thm}

Here the category $\textbf{J-Alg}$ is the category whose objects are $J$-algebras and whose morphisms are \textit{J-algebra homomorphisms}. We refer the reader to the original article for the precise definition of such morphisms.

Our goal for this section is to briefly analyse where $P$ and $L$ algebras fit inside a $J$-algebra.

The following data of the $J$-algebra associated with a TFT $Z$ that directly involves the genus $0$ piece:

\begin{enumerate}
\item $A_0 = Z(S^2)$ is the vector space associated to the two-sphere.
\item linear maps $\alpha_1: A_1 \to A_{0} $,

\item linear maps $\delta _{0, g}: A_g \to A_0 \otimes A_{g}$,

\item linear maps  $\mu _{g,0} : A_g \otimes A_0 \to A_{g}$, 

\item linear maps $\omega_0 : A_0 \to A_{1}$, 

\item The linear map $tr: A_0 \to k$, 

\item The linear map $1: k \to A_0$, 

\item involutions $*_0: A_0 \to A_0$
\item representations $\rho _0 : MCG(S^2) \to \operatorname{Aut}(A_0) $.
\end{enumerate}

Note that 8 and 9 are actually both trivial for the following reason: $MCG$ here means isotopy classes of orientation preserving diffeomorphisms, so $MCG(S^2)= \left\{ [id_{S^2}] \right\} $ is the group of one element. Therefore $\rho_0$ maps $[id_{S^2}]$ trivially to the identity of $A_0$. The diffeomorphism of $S^2$ defined by rotation about the $z$-axis by $\pi $ is therefore also isotopic to the identity, hence passing through $Z$ gives the identity on $A_0$. By definition this is the involution $*_g$. Therefore we see that 8 and 9 contains no information.

Furthermore, we see that 6 and 7 agree with the unit and trace maps of $A_0$ as a commutative Frobenius algebra. In the case $g=0$, $\delta_{0,g} = m^\vee $ and $\mu_{g,0} = m$ recovers the co/multiplication maps.

Therefore, the non-trivial information associated to the commutative Frobenius algebra $A_0$ is the following:
\begin{enumerate}
\setcounter{enumi}{1}
\item the genus reduction map $\alpha_1: A_1 \to A_0 $ 
\item the splitting maps $\delta_{0,g}: A_g \to A_0 \otimes A_g$, $g>0$
\item the merging maps $\mu_{g,0}: A_g \otimes A_0 \to A_g$, $g>0$
\item the genus creation map $\omega_0 : A_0 \to A_1$.
\end{enumerate}



Even though the four classes of maps above are the only maps in the data of $J$-algebras that directly involves $A_0 $, they do not generate all relevant maps. For example, they do not generate prime endomorphisms $e_p : A_0 \to A_0$ where $p$ is irreducible.

\begin{thm} \label{thm:JgivesPL}
The degree $0$ part of every $J$-algebra is a $P / L$-algebra. Namely, every $J$-algebra induces a $P/L$-algebra. 
\end{thm}

\begin{proof}
By theorem \ref{thm:Jalg=3dTFT}, for any $J$-algebra $J$ there exists a 3-dimensional oriented TFT $Z: \operatorname{Cob}(3)\to \operatorname{Vect}_k$ such that $J(Z) = J$, where $J(Z)$ consists of the data 1-9 along with compatibility conditions. By theorem \ref{thm:3dTFTgivesPLmonoid}, every 3-dimensional TFT $Z$ determines a $P /L$ algebra $Z(S^2)$.
\end{proof}

This is an extremely unsatisfying proof. We will present a more geometric construction that illustrates precisely \textit{how} the data of a $J$-algebra determines, for example, the prime units. For this, we will need Heegaard Splitting.

\begin{thm} \label{thm:HeegaardSplitting}
[Heegaard] Let $M$ be a connected closed oriented $3 $-manifold. Then there exists two handle bodies $M_1 , M_2 $ of genus $g$ and an orientation-reversing diffeomorphism $f: \partial M_1 \to \partial M_2 $ such that \[
M \cong M_1 \cup_f M_2 
.\]
\end{thm}

\begin{rmk}
The Heegaard genus $g(M)$ is defined as the minimal genus of all possible Heegaard splitting of $M$. In fact \cite{martelli2016introduction}, only $S^3$ (and those $M$ diffeomorphic to it) has $g=0$, and only lens spaces (other than $S^3$) or $S^2 \times S^1$ has $g=1$. All other 3-manifolds have $g\geq 2$.
\end{rmk}

Since $M_1 $ is evidently diffeomorphic to $M_1 \cup_{\partial M_1 } \partial M_1 \times [0,1]$, we may write \[
M \cong M_1 \cup_{\partial M_1 } \partial M_1 \times [0,1] \cup_f M_2 
.\]
and after factoring through diffeomorphisms $\phi_{1,2}: \Sigma_g \to \partial M_{1,2} $, \[
M \cong M_1 \cup_{\phi_1 ^{-1}} Cyl(h) \cup_{\phi_2 } M_2 
.\]
where $h =\phi_2 ^{-1} \circ f\circ \phi_1 : \Sigma_g \to \Sigma_g $ is orientation preserving.

Therefore we have the following variant of the Heegaard splitting:

\begin{thm}
Let $M$ be a connected closed oriented $3 $-manifold. Then there exists two handle bodies $M_1 , M_2 $ of genus $g$ and $h \in \operatorname{Diff}^+(\Sigma_g ) $ such that \[
M \cong M_1 \cup_{\phi_1 ^{-1}} Cyl(h) \cup_{\phi_2 } M_2 
.\]
where $Cyl(h) = (\Sigma_g \times [0,1] \amalg \Sigma_g) / (x,1) \sim h(x)$ is the mapping cylinder of $h$, $\phi_{1}: \Sigma_g \to \partial M_{1}$ is an orientation-preserving diffeomorphism, and $\phi_{2}: \Sigma_g \to \partial M_{2}$ is an orientation-reversing diffeomorphism.
\end{thm}

and the boundary variant:

\begin{thm} \label{thm:Heegaardvarpar}
Let $M$ be a connected closed oriented $3 $-manifold with boundary $\partial M \cong \amalg^{a+b} S^2$. Then there exists two connected oriented 3-manifolds $M_1 , M_2 $ with boundaries $\partial M_1 = \amalg^a S^2 \amalg \Sigma^1$ and $\partial M_2 = \amalg^b S^2 \amalg \Sigma^2$, where $\Sigma^{1,2}$ are of of genus $g$, and $h \in \operatorname{Diff}^+(\Sigma_g ) $ such that \[
M \cong M_1 \cup_{\phi_1 ^{-1}} Cyl(h) \cup_{\phi_2 } M_2 
.\]
where $Cyl(h) = (\Sigma_g \times [0,1] \amalg \Sigma_g) / (x,1) \sim h(x)$ is the mapping cylinder of $h$, $\phi_{1}: \Sigma_g \to \Sigma^1$ is an orientation-preserving diffeomorphism, and $\phi_{2}: \Sigma_g \to \Sigma^2$ is an orientation-reversing diffeomorphism.
\end{thm}

\begin{prop} \label{prop:JtoLmaps}
Given any $A= \oplus_{i\geq 0 } A_i$ an $J$-algebra over $k$, and any irreducible oriented $3$-manifold $P$, let $1_P: k \to A_0$ and $e_P : A_0  \to A_0$ be a prime unit and a prime endomorphism of the $L$-algebra $A_0 $. Then there exists $h \in MCG(\Sigma_g)$ for some $g$ such that \[
1_P = \alpha_1 \circ \alpha_2 \dots \circ \alpha _g \circ \rho_g(h) \circ \omega_{g-1} \circ \omega _{g-2} \circ \dots \circ \omega_0 \circ 1
.\]
and that \[
e_P = \alpha_1 \circ \alpha_2 \dots \circ \alpha _g \circ \rho_g(h) \circ \omega_{g-1} \circ \omega _{g-2} \circ \dots \circ \omega_0
.\]
Namely, $1_P: k \to A_0$ is the composition \[
k \overset{1}{\to } A_0 \overset{\omega _0}{\to } A_1 \overset{\omega _1}{\to } \dots \overset{\omega _{g-1}}{\to }A_g \overset{\rho _g(h)}{\to } A_g \overset{\alpha _g}{\to } A_{g-1} \overset{\alpha_{g-1}}{\to } \dots \overset{\alpha _2}{\to } A_1 \overset{\alpha_1 }{\to }A_0 
.\]
and $e_P: A_0 \to A_0 $ is the composition \[
A_0 \overset{\omega _0}{\to } A_1 \overset{\omega _1}{\to } \dots \overset{\omega _{g-1}}{\to }A_g \overset{\rho _g(h)}{\to } A_g \overset{\alpha _g}{\to } A_{g-1} \overset{\alpha_{g-1}}{\to } \dots \overset{\alpha _2}{\to } A_1 \overset{\alpha_1 }{\to }A_0 
.\]
\end{prop}

\begin{proof}
Applying theorem \ref{thm:Heegaardvarpar} to $P\setminus D^3$ in the case $(a,b)=(0,1)$, there exists a genus $g$ handle body $M_1 $ and a connected closed oriented $3$-manifold $M_2 $ with boundary $S^2 \amalg \Sigma_g$ and  $h\in \operatorname{Diff}^+(\Sigma_g ) $ such that \[
P\setminus D^3 \cong M_1 \cup Cyl(h) \cup M_2 
.\]
Recall that any handle body of genus $g$ can be obtained, by definition, by attaching $g$-many 1-handles to a $0$-handle. Hence in the case $(a,b)=(0,1)$, we learn that $P$ is built by first attaching $g$-many 1-handles to a $0$-handle, which results in $M_1 $.  Then we glue on a mapping cylinder $Cyl(h)$. Then we attach $g$-many $2$-handles, which form $M_2 $. We stop short of attaching the final $3$-handle, which would had result in a closed manifold.

Passing through the TFT $Z$ corresponding to the $J$-algebra $A$, and noting that $\omega _i$ is the image of the trace of $1$-handle attachments while $\alpha_i$ is the image of the trace of $2$-handle attachments, we obtain the desired composition for $1_P$.

Doing the same to $P\setminus (D^3 \sqcup D^3)$ in the case $(a,b)=(1,1)$, we obtain the desired composition for $e_P$.
\end{proof}
