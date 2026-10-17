---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-015-44-2-bundles-with-connections
section_title: "2-Bundles with Connections"
section_number: 4.4
pages: 41-46
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.973
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec4_4}

Apart from the equivalence between transport functors and principal $G$-bundles with connection (Theorem \ref{th2}), our paper \cite{schreiber3} also contains an analogous equivalence for vector bundles with connection. It has
 an immediate generalization to 2-vector bundles with many applications, on which we shall give a brief outlook. 

Suppose $2\mathrm{Vect}$ is  some 2-category of 2-vector spaces. Given a 2-group $\mathfrak{G}$, a
representation of $\mathfrak{G}$ on such a 2-vector space is a 2-functor
\begin{equation*}
  \rho : \mathcal{B}\mathfrak{G} \to 2\mathrm{Vect}\text{.}
\end{equation*}
A \emph{2-vector bundle with connection} and structure 2-group $\mathfrak{G}$  is nothing but a  transport 2-functor
$
  \mathrm{tra} : \mathcal{P}_2(X) \to 2\mathrm{Vect}
$
with $\mathcal{B}\mathfrak{G}$-structure.
Important classes of 2-vector bundles are line 2-bundles and string bundles.



\subsubsection{Models for 2-Vector Spaces}




Depending on the precise application there is some flexibility in
what one may want to understand under a 2-vector space. Usually
 2-vector spaces are abelian module
categories over a given monoidal category. For $k$ a field, two important classes of examples are the following.
First, let  $\widehat{k}$ be
the discrete monoidal category over $k$. Then, $2\mathrm{Vect}$ is 2-category of module categories over $\widehat{k}$. This is 
equivalent to the 2-category of categories internal to $k$-vector spaces. These
\emph{Baez-Crans 2-vector spaces} \cite{baez7} are appropriate for the discussion of Lie 2-algebras.

The second model for $2\mathrm{Vect}$ is the 2-category of module categories over the monoidal category $\mathrm{Vect}(k)$ of $k$-vector spaces,
\begin{equation*}
2\mathrm{Vect} := \mathrm{Vect}(k)\text{-}\mathrm{Mod}\text{.}
\end{equation*}
In its totality this is rather unwieldy, but it contains two important  sub-2-categories: the 2-category $\mathrm{KV}(k)$ of \emph{Kapranov-Voevodsky 2-vector spaces} \cite{kapranov1} and the 2-category $\mathrm{Bimod}(k)$, whose objects are $k$-algebras, whose 1-morphisms are bimodules over these algebras and whose 2-morphisms are bimodule homomorphisms \cite{shulman1}. Indeed, there is an  inclusion 2-functor
\begin{equation*}
\iota: \mathrm{Bimod}(k) \hookrightarrow \mathrm{Vect}(k)\text{-}\mathrm{Mod}
\end{equation*}
that sends a $k$-algebra $A$ to the category $A\text{-}\mathrm{Mod}$ of ordinary (say, right) $A$-modules. This is a module category over $\mathrm{Vect}(k)$ by tensoring a right module from the left by a vector space. A 1-morphism, an $A$-$B$-bimodule $N$, is sent to the functor that tensores a right $A$-module  from the right by $N$, yielding a right $B$-module. A bimodule morphism induces evidently a natural transformation of these functors. 


If one restricts the 2-functor $\iota$ to the full sub-2-category formed by
those algebras that are direct sums  $A = k^{\oplus n}$ of the ground
field algebra, the 2-vector spaces in the image of $\iota$ are of the form $\mathrm{Vect}(k)^n$, i.e. tuples of vector spaces. The 1-morphisms in the image are $(m\times n)$-matrices whose entries are $k$-vector spaces. These form  the 2-category of Kapranov-Voevodsky 2-vector spaces \cite{kapranov1}.


\subsubsection{The canonical Representation of a 2-Group}

Every automorphism 2-group $\mathrm{AUT}(H)$ of a Lie group $H$ has a
canonical representation on 2-vector spaces, namely
\begin{equation}
\label{30}
\alxydim{}{\mathcal{B}\mathrm{AUT}(H) \ar[r]^-{A} & \mathrm{Bimod}(k) \ar[r]^-{\iota} & \mathrm{Vect}(k)\text{-}\mathrm{Mod}\text{,}}
\end{equation}
where the  2-functor $A$ is defined similar as the one we have used for the non-abelian bundle gerbes in \erf{48}. It sends the single object to $k$ regarded as a $k$-algebra, it sends a 1-morphism $\varphi\in \mathrm{Aut}(H)$ to the bimodule $_{\varphi}k$ in the notation of Section \ref{sec4_3_2}, and it sends a 2-morphism $(\varphi,h):\varphi\Rightarrow  c_h \circ \varphi$ to the multiplication with $h$ from the left. 

Now let $\mathfrak{G}$ be any smooth Lie 2-group corresponding to a smooth crossed module $(G,H,t,\alpha)$. We have a canonical 2-functor
\begin{equation}
\label{39}
\mathcal{B}\mathfrak{G} \to \mathcal{B}\mathrm{AUT}(H)\quad:\quad \bigon{\ast}{\ast}{g}{g'}{h}\mapsto \bigon{\ast}{\ast}{\alpha_g}{\alpha_{g'}}{h}
\end{equation}
whose composition with \erf{30} gives a representation of $\mathfrak{G}$, that we call the \emph{canonical $k$-representation}.

\begin{example} 
\label{ex1}
A very simple but useful example is the canonical $\C$-representation of
$\mathcal{B}\C^{\times}$.
In this case the composition \erf{30} is the 2-functor
\begin{equation*}
\rho\quad:\quad \mathcal{BB}\C^{\times} \to \mathrm{Vect}(\C)\text{-}\mathrm{Mod}\quad:\quad \bigon{\ast}{\ast}{\id}{\id}{z} \mapsto \bigon{\mathrm{Vect}(\C)}{\mathrm{Vect}(\C)}{- \otimes \C}{-\otimes \C}{- \cdot z}
\end{equation*}
for all $z \in \C^{\times}$. Notice that $\mathrm{Vect}(\mathbb{C})$ is the canonical
1-dimensional 2-vector space over $\C$ in the same sense in that $\mathbb{C}$ is
the canonical 1-dimensional complex 1-vector space. Therefore, transport 2-functors
\begin{equation*}
\mathrm{tra}:\mathcal{P}_2(M) \to \mathrm{Vect}(\C)\text{-}\mathrm{Mod}
\end{equation*}
with $\mathcal{BB}\C^{\times}$-structure  deserve to be addressed as
\emph{line 2-bundles with connection}. Two remarks:
\begin{enumerate}
\item 
Going through the discussion of abelian bundle gerbes with connection in Section \ref{sec3_2} it is easy to see  that line 2-bundles with connection are equivalent to bundle gerbes with connection defined via line bundles instead of circle bundles.
\item
The fibre $\mathrm{tra}(x)$ of a line 2-bundle $\mathrm{tra}$ at a point $x$ is an algebra which is Morita equivalent to the ground field $\C$. These are exactly the finite rank operators on a separable Hilbert space. Thus, line 2-bundles with connection are a form of bundles of finite rank operators with connection, this is the point of view taken in \cite{bouwknegt1}.
\end{enumerate}
\end{example}
 
The  2-functor $A:\mathcal{B}\mathrm{AUT}(H) \to \mathrm{Bimod}(k)$ we have used above can be deformed to a 2-functor $A^{\rho}$ using an ordinary representation $\rho: \mathcal{B}H \to \mathrm{Vect}(k)$ of $H$. It sends the object of $\mathcal{B}\mathrm{AUT}(H)$ to the algebra $A^{\rho}(\ast)$ which is the vector space generated from all the linear maps $\rho(h)$. A 1-morphism $\varphi\in\mathrm{Aut}(H)$ is again sent to the bimodule $_{\varphi}A^{\rho}(\ast)$, and the 2-morphisms as before to left multiplications. The original 2-functor is reproduced by $A=A^{\mathrm{triv}_{k}}$ from the trivial representation of $H$ on $k$.



\begin{example}
For $G$ a compact simple and simply-connected Lie group, we consider the level $k$ central extension $H_k:=\hat\Omega_k G$ of the group of based loops in $G$. For a positive energy representation $\rho: \mathcal{B}\hat\Omega_k G \to \mathrm{Vect}(k)$ the algebra $A^{\rho}(\ast)$ turns out to be a von Neumann-algebra while the bimodules $_{\varphi}A^{\rho}(\ast)$ are Hilbert bimodules. In this infinite-dimensional case we have to make the composition of 1-morphisms more precise: here we take not the algebraic tensor product of these Hilbert bimodules but the  Connes fusion tensor product
\cite{stolz1}. Connes fusion product still respects the composition: for $A$ a von Neumann algebra
and ${}_\varphi A$ the bimodule structure on it induced from twisting the left action by an algebra
automorphism $\varphi$, we have
\begin{equation*}
  {}_\varphi A \otimes {}_{\varphi'}A \simeq {}_{\varphi' \circ \varphi} A
\end{equation*}
under the Connes fusion tensor product. Now let $\mathfrak{G}=\mathrm{String}_k(G)$ be the string 2-group defined from the  crossed module $\hat\Omega_k G \to P _0G$ of Fr�chet Lie groups \cite{baez9}. Together with the projection 2-functor \erf{39} we obtain an induced representation
\begin{equation*}
i:\mathcal{B}\mathrm{String}_k(G) \to \mathrm{Bimod}_{\mathrm{CF}}(k)
\end{equation*}
The fibres of a transport 2-functor 
\begin{equation}
\mathrm{tra}: \mathcal{P}_2(M) \to \mathrm{Bimod}_{\mathrm{CF}}(k)
\label{38}
\end{equation}
with $\mathcal{B}\mathrm{String}_k(G)$-structure are hence von Neumann algebras, and its parallel transport along a path is a Hilbert bimodule for these fibres. 
In conjunction with the result \cite{baez8,baas2}
that $\mathrm{String}_k(G)$-2-bundles have the same classification as
ordinary fibre bundles whose structure group is the topological
String group, this says that transport 2-functors \erf{38} have to be addressed as \emph{String 2-bundles with connection}, see \cite{stolz1}.
\end{example}


\subsubsection{Twisted Vector Bundles}



Vector bundles over $M$ twisted by a class $\xi\in H^3(M,\Z)$ are the same thing as gerbe modules for a bundle gerbe $\mathcal{G}$ whose Dixmier-Douady class is $\xi$ \cite{bouwknegt1}. These modules are in turn nothing else but certain (generalized) 1-morphisms in the 2-category of bundle gerbes $\mathfrak{BGrb}(M)$ \cite{waldorf1}. The same is true for connections on twisted vector bundles. More precisely, a twisted vector bundle with connection is the same as a 1-morphism
\begin{equation*}
\mathcal{E}:\mathcal{G} \to \mathcal{I}_{\rho}
\end{equation*}
from the bundle gerbe $\mathcal{G}$ with connection to the trivial bundle gerbe $\mathcal{I}$ equipped with the connection 2-form $\rho \in \Omega^2(M)$. 

Now let 
\begin{equation*}
\mathrm{tra}:\mathcal{P}_2(M) \to \mathrm{Vect}(\C)\text{-}\mathrm{Mod}
\end{equation*}
be a transport 2-functor which plays the role of the bundle gerbe $\mathcal{G}$, but we allow an arbitrary structure 2-group $\mathfrak{G}$ and any representation $\rho:\mathcal{B}\mathfrak{G} \to \mathrm{Vect}(\C)\text{-}\mathrm{Mod}$. Let $\mathrm{tra}^{\infty}: \mathcal{P}_2(M) \to \mathcal{B}\mathfrak{G}$ be a smooth 2-functor which plays the role of the trivial bundle gerbe. We shall now consider transport transformations
\begin{equation*}
A:\mathrm{tra} \to \mathrm{tra}^{\infty}_{\rho}\text{.}
\end{equation*} 
Let $\pi:Y \to M$ be a surjective submersion for which $\mathrm{tra}$ admits a local trivialization with smooth descent data $(\mathrm{triv},g,\psi,f)$. The descent data of $\mathrm{tra}^{\infty}$ is of course $(\pi^{*}\mathrm{tra}^{\infty},\id,\id,\id)$. Now the transport transformation $A$ has the following descent data: the first part is a \pt\ $h: \mathrm{triv} \to \pi^{*}\mathrm{tra}^{\infty}$ whose associated functor $\holo(h): \mathcal{P}_1(Y) \to \Lambda_{\rho}(\mathrm{Vect}(\C)\text{-}\mathrm{Mod})$ is a transport functor with $\Lambda \mathcal{B}\mathfrak{G}$-structure. The second part is a modification $\varepsilon: \pi_2^{*}h \circ g \Rightarrow \id \circ \pi_1^{*}h$ whose associated natural transformation
\begin{equation*}
\holo(\varepsilon): \pi_2^{*}\holo(h) \otimes \holo(g) \to \pi_1^{*}\holo(h)
\end{equation*}
is a morphism of transport functors over $Y^{[2]}$. According to the coherence conditions on descent 1-morphisms, it fits into the commutative diagram
\begin{equation}
\label{62}
\alxydim{@C=2cm}{\pi_3^{*}\holo(h) \otimes \pi_{23}^{*}\holo(g) \otimes \pi_{12}^{*}\holo(g) \ar[r]^-{\pi_{23}^{*}\holo(\varepsilon) \otimes \id} \ar[d]_{\id\otimes \holo(f)} & \pi_2^{*}\holo(h) \otimes \pi_{12}^{*}\holo(g) \ar[d]^{\pi_{12}^{*}\holo(\varepsilon)} \\ \pi_{3}^{*}\holo(h) \otimes \pi_{13}^{*}\holo(g) \ar[r]_{\pi_{13}^{*}\holo(\varepsilon)} & \pi_1^{*}\holo(h)}
\end{equation}
of morphisms of transport functors over $Y^{[3]}$ and satisfies $\Delta^{*}\holo(\varepsilon) \circ \holo(\psi) =\id$. The transport functor 
\begin{equation*}
\holo(h): \mathcal{P}_1(Y) \to \Lambda_{\rho}(\mathrm{Vect}(\C)\text{-}\mathrm{Mod})
\end{equation*}
together with the natural transformation $\holo(\varepsilon)$ is the general version of a vector bundle with connection twisted by a transport 2-functor $\mathrm{tra}$. According to Sections \ref{sec4_1} and \ref{sec3_3}, the twists can thus be Breen-Messing gerbes or non-abelian bundle gerbes with connection. 



Depending on the choice of the representation $\rho$, our twisted vector bundles can be translated into more familiar language. Let us demonstrate this in the  case of Example \ref{ex1}, in which the twist is a line 2-bundle with connection, i.e. a transport 2-functor
\begin{equation*}
\mathrm{tra}: \mathcal{P}_2(M) \to \mathrm{Vect}(\C)\text{-}\mathrm{Mod}
\end{equation*}  
with $\mathcal{BB}\C^{\times}$-structure. In order to obtain the usual twisted vector bundles, we restrict the target 2-category to $\mathcal{B}\mathrm{Vect}(\C)$, the monoidal category of complex vector spaces considered as a 2-category.  The following Lie category $\mathrm{Gl}$ is appropriate: its objects are the natural numbers $\N$, and it has only morphisms between equal numbers, namely all matrices $\mathrm{Gl}_n(\C)$. The composition is the product of matrices. The Lie category $\mathrm{Gl}$ is strictly monoidal: the tensor product of two objects $m,n\in\N$ is the product $nm\in\N$, and the one of two matrices $A\in\mathrm{Gl}(m)$ and $B\in\mathrm{Gl}(n)$ is the ordinary tensor product $A\otimes B\in \mathrm{Gl}(m\times n)$. In fact, $\mathrm{Gl}$ carries a second monoidal structure coming from the sum of natural numbers and the direct sum of matrices, so that $\mathrm{Gl}$ is actually a \emph{bipermutative category}, see Example 3.1 of \cite{baas1}. 


Notice that we have a canonical inclusion functor 
$\iota: \mathcal{B}\C^{\times} \hookrightarrow \mathrm{Gl}$,
which induces another inclusion
\begin{equation*}
\iota_{*}:\transport{}{2}{\mathcal{BB}\C^{\times}}{\mathcal{B}\mathrm{Vect}(\C)} \to \transport{}{2}{\mathcal{B}\mathrm{Gl}}{\mathcal{B}\mathrm{Vect}(\C)}
\end{equation*}
of line 2-bundles with connection into more general vector 2-bundles with connection. Here we have used the representation
\begin{equation*}
\rho: \mathcal{B}\mathrm{Gl} \to \mathcal{B}\mathrm{Vect}
\end{equation*} 
obtained as a generalization of Example \ref{ex1} from $\C^{\times}=\mathrm{Gl}_1(\C)$ to $\mathrm{Gl}_n(\C)$ for all $n\in \N$. The composition $\rho \circ \iota$ reproduces the representation of Example \ref{ex1}. 


Using the above inclusion, the given transport 2-functor $\mathrm{tra}$ induces a transport 2-functor $\iota_{*}\circ \mathrm{tra}: \mathcal{P}_2(M) \to \mathcal{B}\mathrm{Vect}(\C)$ with $\mathcal{B}\mathrm{Gl}$-structure, and one can study transport transformations
\begin{equation*}
A:\mathrm{tra} \to \mathrm{tra}^{\infty}_{\rho}
\end{equation*} 
in that greater 2-category $\transport{}{2}{\mathcal{B}\mathrm{Gl}}{\mathcal{B}\mathrm{Vect}(\C)}$. Along the lines of the general procedure described above, we have transport functors $\holo(g)$ and $\holo(h)$ coming from the descent data of $\mathrm{tra}$ and $A$, respectively. In the present particular situation, the first one takes values in the category $\Lambda_{\rho\circ\iota}\mathcal{B}\mathrm{Vect}_1(\C)$ whose objects are one-dimensional complex vector spaces and whose morphisms from $V$ to $W$ are invertible linear maps $f: W \otimes \C \to \C \otimes V$. Similar to Lemma \ref{lem6}, this category is equivalent to the category $\mathrm{Vect}_1(\C)$ of one dimensional complex vector spaces itself. Thus, the transport functor $\holo(g)$ with $\mathcal{B}\C^{\times}$-structure is a complex line bundle $L$ with connection over $Y^{[2]}$. The second transport functor, $\holo(h)$, takes values in the category $\Lambda_{\rho\circ\iota}\mathcal{B}\mathrm{Vect}(\C)$. This category is equivalent to the category $\mathrm{Vect}(\C)$ itself. It has $\Lambda_{\iota}\mathcal{B}\mathrm{Gl}$-structure, which is equivalent to $\mathrm{Gl}$. Thus, $\holo(h)$ is a transport functor with values in $\mathrm{Vect}(\C)$ and $\mathrm{Gl}$-structure. It thus corresponds to a finite rank vector bundle $E$ over $Y$ with connection. 

Since all identifications we have made so far a functorial, the morphisms $\holo(f)$ and $\holo(\varepsilon)$ of transport functors induce morphisms of vector bundles that preserve the connections, namely an associative morphism
\begin{equation*}
\mu: \pi_{23}^{*}L \otimes \pi_{12}^{*}L \to \pi_{13}^{*}L
\end{equation*}
of line bundles over $Y^{[2]}$, and a morphism
\begin{equation*}
\varrho: \pi_2^{*}E \otimes L \to \pi_1^{*}E
\end{equation*}
of vector bundles over $Y$ which satisfies a compatibility condition corresponding to \erf{62}. This reproduces the definition of a twisted vector bundle with connection \cite{bouwknegt1}.
We remark that the 2-form $\rho$ that corresponds to the smooth 2-functor $\mathrm{tra}^{\infty}_{\rho}$ which was the target of the transport transformation $A$ we have considered, is related to the curvature of the connection on the vector bundle $E$: it requires that
\begin{equation*}
\mathrm{curv}(E) = I_n \cdot (\mathrm{curv}(L) - \pi^{*}\rho)\text{,}
\end{equation*}
where $I_n$ is the identity matrix and $n$ is the rank of $E$. This condition can be derived similar to Lemma \ref{lem8}.

\setsecnumdepth{3}
