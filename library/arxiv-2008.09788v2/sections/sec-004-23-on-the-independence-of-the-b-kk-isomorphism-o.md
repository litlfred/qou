---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY"
section_id: sec-004-23-on-the-independence-of-the-b-kk-isomorphism-o
section_title: "On the independence of the B-KK isomorphism of infinite prime and Plotkin conjecture for symplectomorphisms"
section_number: 2.3
pages: 13-23
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
\label{indep}


\subsubsection{\bf Plotkin's problem for symplectomorphism and the Kontsevich conjecture}\label{plk}

Observe that the study of automorphisms of the group of polynomial symplectomorphisms, as well as automorphisms of the Weyl algebra (Plotkin's problem) is extremely important in course of the Kontsevich conjecture, as well as the Jacobian conjecture.



\subsubsection{\bf Ultrafilters and infinite primes}\label{uf}
Let $\mathcal{U}\subset 2^{\mathbb{N}}$ be an arbitrary non-principal ultrafilter on the set of all positive numbers (in this note $\mathbb{N}$ will almost always be regarded as the index set). Let $\mathbb{P}$ be the set of all prime numbers, and let $\mathbb{P}^{\mathbb{N}}$ denote the set of all sequences $p=(p_m)_{m\in\mathbb{N}}$ of prime numbers. We refer to a generic set $A\in \mathcal{U}$ as an index subset in situations involving the restriction $p_{|A}:A\rightarrow \mathbb{P}$. We will call a sequence $p$ of prime numbers $\mathcal{U}$-stationary if there is an index subset $A\in\mathcal{U}$ such that its image $p(A)$ consists of one point.


A sequence $p:\mathbb{N}\rightarrow\mathbb{P}$ is bounded if the image $p(\mathbb{N})$ is a finite set. Thanks to the ultrafilter finite intersection property, bounded sequences are necessarily $\mathcal{U}$-stationary.




Any non-principal ultrafilter $\mathcal{U}$ generates a congruence
\begin{equation*}
\sim_{\mathcal{U}}\subseteq \mathbb{P}^{\mathbb{N}}\times\mathbb{P}^{\mathbb{N}}
\end{equation*}
in the following way. Two sequences $p^1$ and $p^2$ are $\mathcal{U}$-congruent iff there is an index subset $A\in\mathcal{U}$ such that for all $m\in A$ the following equality holds:
\begin{equation*}
p^1_m=p^2_m.
\end{equation*}
The corresponding quotient
\begin{equation*}
{}^*\mathbb{P}\equiv \mathbb{P}^{\mathbb{N}}/\sim_{\mathcal{U}}
\end{equation*}
contains as a proper subset the set of all primes $\mathbb{P}$ (naturally identified with classes of $\mathcal{U}$-stationary sequences), as well as classes of unbounded sequences. The latter are referred to as nonstandard, or infinitely large, primes. We will use both names and normally denote such elements by $[p]$, mirroring the convention for equivalence classes. The terminology is justified, as the set of nonstandard primes is in one-to-one correspondence with the set of prime elements in the ring ${}^*\mathbb{Z}$ of nonstandard integers in the sense of Robinson \cite{R}.



Indeed, one may utilize the following construction, which was thoroughly studied\footnote{also cf. \cite{C}} in \cite{LLS}. Consider the ring $\mathbb{Z}^{\omega}=\prod_{m\in\mathbb{N}}\mathbb{Z}$ - the product of countably many copies of $\mathbb{Z}$ indexed by $\mathbb{N}$. The minimal prime ideals of $\mathbb{Z}^{\omega}$ are in bijection with the set of all ultrafilters on $\mathbb{N}$ (perhaps it is opportune to remind that the latter is precisely the Stone-Cech compactification $\beta\mathbb{N}$ of $\mathbb{N}$ as a discrete space). Explicitly, if for every $a=(a_m)\in\mathbb{Z}^{\omega}$ one defines the support complement as
\begin{equation*}
\theta(a)=\lbrace m\in\mathbb{N}\;|\;a_m=0\rbrace
\end{equation*}
and for an arbitrary ultrafilter $\mathcal{U}\in 2^{\mathbb{N}}$ sets
\begin{equation*}
(\mathcal{U})=\lbrace a\in\mathbb{Z}^{\omega}\;|\;\theta(a)\in\mathcal{U}\rbrace,
\end{equation*}
then one obtains a minimal prime ideal of $\mathbb{Z}^{\omega}$. It is easily shown that every minimal prime ideal is of such a form. Of course, the index set $\mathbb{N}$ may be replaced by any set $I$, after which one easily gets the description of minimal primes of $\mathbb{Z}^I$ (since those correspond to ultrafilters, there are exactly $2^{2^{|I|}}$ of them if $I$ is infinite and $|I|$ when $I$ is a finite set).
Note that in the case of finite index set all ultrafilters are principal, and the corresponding $(\mathcal{U})$ are of the form $\mathbb{Z}\times\cdots\times (0)\times\cdots\times\mathbb{Z}$ - a textbook example.

Similarly, one may replace each copy of $\mathbb{Z}$ by an arbitrary integral domain and repeat the construction above. If for instance all the rings in the product happen to be fields, then, since the product of any number of fields is von Neumann regular, the ideal $(\mathcal{U})$ will also be maximal.
\smallskip

The ring of nonstandard integers  may be viewed as a quotient (an ultrapower)
\begin{equation*}
\mathbb{Z}^{\omega}/(\mathcal{U})={}^*\mathbb{Z}.
\end{equation*}
The class of $\mathcal{U}$-congruent sequences $[p]$ corresponds to an element (also an equivalence class) in ${}^*\mathbb{Z}$, which may as well as $[p]$ be represented by a prime number sequence $p=(p_m)$, only in the latter case some but not too many of the primes $p_m$ may be replaced by arbitrary integers. For all intents and purposes, this difference is insignificant.

\smallskip
Also, observe that $[p]$ indeed generates a maximal prime ideal in ${}^*\mathbb{Z}$: if one for (any) $p\in [p]$ defines an ideal in $\mathbb{Z}^{\omega}$ as
\begin{equation*}
(p,\; \mathcal{U})=\lbrace a\in\mathbb{Z}^{\omega}\;|\;\lbrace m\;|\; a_m\in p_m\mathbb{Z}\rbrace\in\mathcal{U}\rbrace,
\end{equation*}
then, taking the quotient $\mathbb{Z}^{\omega}/(p,\; \mathcal{U})$ in two different ways, one arrives at an isomorphism
\begin{equation*}
{}^*\mathbb{Z}/([p])\simeq \left(\prod_{m}\mathbb{Z}_{p_m}\right)/(\mathcal{U}),
\end{equation*}
and the right-hand side is a field by the preceding remark.
\smallskip
For a fixed non-principal $\mathcal{U}$ and an infinite prime $[p]$, we will call the quotient
\begin{equation*}
\mathbb{Z}_{[p]}\equiv {}^*\mathbb{Z}/([p])
\end{equation*}
the nonstandard residue field of $[p]$. Under our assumptions this field has characteristic zero.



\medskip



\subsubsection{\bf Algebraic closure of nonstandard residue field}\label{ac}
We have seen that the objects $[p]$ - the infinite prime - behaves similarly to the usual prime number in the sense that a version of a residue field corresponding to this object may be constructed. Note that the standard residue fields are contained as a degenerate case in this construction, namely if we drop the condition of unboundedness and instead consider $\mathcal{U}$-stationary sequences, we will arrive at a residue field isomorphic to $\mathbb{Z}_{p}$, with $p$ being the image of the stationary sequence in the chosen class. The fields of the form $\mathbb{Z}_{[p]}$ are a realization of what is known as pseudofinite field, cf. \cite{BH}.

\smallskip

The nonstandard case is surely more interesting. While the algebraic closure of a standard residue field is countable, the nonstandard one itself has the cardinality of the continuum. Its algebraic closure is also of that cardinality and has characteristic zero, which implies that it is isomorphic to the field of complex numbers. We proceed by demonstrating these facts.
\smallskip

\begin{prop}
For any infinite prime $[p]$ the residue field $\mathbb{Z}_{[p]}$ has the cardinality of the continuum\footnote{There is a general statement on cardinality of ultraproduct due to Frayne, Morel, and Scott \cite{FMS}. We believe the proof of this particular instance may serve as a neat example of what we are dealing with in the present paper.}.
\end{prop}

\begin{proof}
It suffices to show there is a surjection

\begin{equation*}
h^*:\mathbb{Z}_{[p]}\rightarrow \mathfrak{P},
\end{equation*}

where $\mathfrak{P}=\lbrace 0,1\rbrace^{\omega}$ is the Cantor set given as the set of all countable strings of bits with the 2-adic metric

\begin{equation*}
d_2(x,y)=1/k,\;\;k=\min\lbrace m\;|\;x_m\neq y_m\rbrace.
\end{equation*}

The map $h^*$ is constructed as follows. If $\mathfrak{Z}\subset \mathfrak{P}$ is the subset of all strings with finite number of ones in them, and
\begin{equation*}
e:\mathbb{Z}_+\rightarrow\mathfrak{Z},\;\;e\left(\sum_{k<m}f_k2^k\right)=(f_1,\ldots,f_{m-1},0,\ldots)
\end{equation*}
is the bijection that sends a nonnegative integer to its binary decomposition, then for a class representative $a=(a_m)\in[a]\in\mathbb{Z}_{[p]}$ set $h^*(a)$ to be the (unique) ultralimit of the sequence of points $\lbrace x_m=e(a_m)\rbrace$. The correctness of this map rests on the property of the Cantor set being Hausdorff quasi-compact. Surjectivity is then established directly: consider an arbitrary $x\in\mathfrak{P}$. For each $m\in\mathbb{N}$ the set
\begin{equation*}
\mathfrak{P}_m=\lbrace e(0),e(1),\ldots,e(p_m-1)\rbrace
\end{equation*}
consists of $p_m$ distinct points. Let $x_m$ be the nearest to $x$ point from this set with respect to the 2-adic metric.
The sequence $(p_m)$ is unbounded, so that for every $m\in\mathbb{N}$ the index subset

\begin{equation*}
A_m=\lbrace k\in\mathbb{N}\;|\;p_k>2^m\rbrace
\end{equation*}
belongs to the ultrafilter $\mathcal{U}$. It is easily seen that for every $k\in A_m$ one has:

\begin{equation*}
d_2(x,x_k)<1/m
\end{equation*}
But that effectively means that the sequence $(x_m)$ has the ultralimit $x$, after which $a_m=e^{-1}(x_m)$ yields the desired preimage.
\end{proof}

As an immediate corollary of this proposition and the well-known Steinitz theorem, one has

\begin{thm}
The algebraic closure $\overline{\mathbb{Z}_{[p]}}$ of $\mathbb{Z}_{[p]}$ is isomorphic to the field of complex numbers.
\end{thm}
\smallskip

We now fix the notation for the aforementioned isomorphisms in order to employ it in the next section.

For any nonstandard prime $[p]\in {}^*\mathbb{P}$ fix an isomorphism $\alpha_{[p]}:\mathbb{C}\rightarrow \overline{\mathbb{Z}_{[p]}}$ coming from the preceding theorem. Denote by $\Theta_{[p]}:\overline{\mathbb{Z}_{[p]}}\rightarrow \overline{\mathbb{Z}_{[p]}}$ the nonstandard Frobenius automorphism - that is, a well-defined field automorphism that sends a sequence of elements to a sequence of their $p_m$-th powers:

\begin{equation*}
(x_m)\mapsto(x_m^{p_m}).
\end{equation*}

The automorphism $\Theta_{[p]}$ is identical on $\mathbb{Z}_{[p]}$; conjugated by $\alpha_{[p]}$, it yields a wild automorphism of complex numbers, as by assumption no finite power of it (as always, in the sense of index subsets $A\in\mathcal{U}$) is the identity homomorphism.

\bigskip


\subsubsection{\bf Extension of the Weyl algebra}\label{wa}
The $n$-th Weyl algebra $A_{n,\mathbb{C}}\simeq A_{n,\overline{\mathbb{Z}_{[p]}}}$ can be realized as a proper subalgebra of the following ultraproduct of algebras

\begin{equation*}
\mathcal{A}_n(\mathcal{U},[p])=\left(\prod_{m\in\mathbb{N}}A_{n,\mathbb{F}_{p_m}}\right)/\mathcal{U}.
\end{equation*}

Here for any $m$ the field $\mathbb{F}_{p_m}=\overline{\mathbb{Z}_{p_m}}$ is the algebraic closure of the residue field $\mathbb{Z}_{p_m}$. This larger algebra contains elements of the form $(\zeta^{I_m})_{m\in\mathbb{N}}$ with unbounded $|I_m|$ - something which is not present in $A_{n,\overline{\mathbb{Z}_{[p]}}}$, hence the proper embedding. Note that for the exact same reason (with degrees $|I_m|$ of differential operators having been replaced by degrees of minimal polynomials of algebraic elements) the inclusion

\begin{equation*}
\overline{\mathbb{Z}_{[p]}}\subseteq \left(\prod_{m\in\mathbb{N}}{F}_{p_m}\right)/\mathcal{U}
\end{equation*}
is also proper.
\smallskip

It turns out that, unlike its standard counterpart $A_{n,\mathbb{C}}$, the algebra $\mathcal{A}_n(\mathcal{U},[p])$ has a huge center described in this proposition:

\begin{prop}
The center of the ultraproduct of Weyl algebras over the sequence of algebraically closed fields $\lbrace \mathbb{F}_{p_m}\rbrace$ coincides with the ultraproduct of centers of $A_{n,\mathbb{F}_{p_m}}$:
\begin{equation*}
C(\mathcal{A}_n(\mathcal{U},[p]))=\left(\prod_{m}C(A_{n,\mathbb{F}_{p_m}})\right)/\mathcal{U}.
\end{equation*}
\end{prop}

The proof is elementary and is left to the reader. As in positive characteristic the center $C(A_{n,\mathbb{F}_{p}})$ is given by the polynomial algebra

\begin{equation*}
\mathbb{F}_{p}[x_1^{p},\ldots,x_n^{p},y_1^{p},\ldots,y_n^{p}]\simeq \mathbb{F}_{p}[\xi_1,\ldots,\xi_{2n}],
\end{equation*}

there is an injective $\mathbb{C}$-algebra homomorphism

\begin{equation*}
\mathbb{C}[\xi_1,\ldots\xi_{2n}]\rightarrow \left(\prod_{m}\mathbb{F}_{p_m}[\xi_1^{(m)},\ldots\xi_{2n}^{(m)}]\right)/\mathcal{U}
\end{equation*}

from the algebra of regular functions on $\mathbb{A}_{\mathbb{C}}^{2n}$ to the center of $\mathcal{A}_n(\mathcal{U},[p])$, evaluated on the generators in a straightforward way:

\begin{equation*}
\xi_i\mapsto[(\xi_i^{(m)})_{m\in\mathbb{N}}].
\end{equation*}

Just as before, this injection is proper.

Furthermore, the image of this monomorphism (the set which we will simply refer to as the polynomial algebra) may be endowed with the canonical Poisson bracket. Recall that in positive characteristic case for any $a,b\in \mathbb{Z}_p[\xi_1,\ldots,\xi_{2n}]$ one can define

\begin{equation*}
\lbrace a,b\rbrace=-\pi\left(\frac{[a_0,b_0]}{p}\right).
\end{equation*}

Here $\pi:A_{n,\mathbb{Z}}\rightarrow A_{n,\mathbb{Z}_p}$ is the modulo $p$ reduction of the Weyl algebra, and $a_0, b_0$ are arbitrary lifts of $a,b$ with respect to $\pi$. The operation is well defined, takes values in the center and satisfies the Leibnitz rule and the Jacobi identity. On the generators one has
\begin{equation*}
\lbrace \xi_i,\xi_j\rbrace=\omega_{ij}.
\end{equation*}
The Poisson bracket is trivially extended to the entire center $\mathbb{F}_{p}[\xi_1,\ldots,\xi_{2n}]$ and then to the ultraproduct of centers. Observe that the Poisson bracket of two elements of bounded degree is again of bounded degree, hence one has the bracket on the polynomial algebra.



\subsubsection{\bf Endomorphisms and symplectomorphisms}\label{es}

The point of this construction lies in the fact that thus defined Poisson structure on the (injective image of) polynomial algebra is preserved under all endomorphisms of $\mathcal{A}_n(\mathcal{U},[p])$ of bounded degree. Every endomorphism of the standard Weyl algebra is specified by an array of coefficients $(a_{i,I})$ (which form the images of the generators in the standard basis); these coefficients are algebraically dependent, but with only a finite number of bounded-order constraints. Hence the endomorphism of the standard Weyl algebra can be extended to the larger algebra $\mathcal{A}_n(\mathcal{U},[p])$. The restriction of any such obtained endomorphism on the polynomial algebra $\mathbb{C}[\xi_1,\ldots,\xi_{2n}]$ preserves the Poisson structure. In this setup the automorphisms of the Weyl algebra correspond to symplectomorphisms of $\mathbb{A}_{\mathbb{C}}^{2n}$.

\medskip

\textbf{Example}. If $x_i$ and $y_i$ are standard generators, then one may perform a linear symplectic change of variables:
\begin{eqnarray*}
f(x_i)=\sum_{j=1}^na_{ij}x_j+\sum_{j=1}^{n}a_{i,n+j}y_j,\;\;i=1,\ldots,n,\\
f(d_i)=\sum_{j=1}^na_{i+n,j}x_j+\sum_{j=1}^{n}a_{i+n,n+j}y_j,\;\; a_{ij}\in\mathbb{C}.
\end{eqnarray*}
In this case the corresponding polynomial automorphism $f^c$ of
\begin{equation*}
\mathbb{C}[\xi_1,\ldots,\xi_{2n}]\simeq\mathbb{C}[x_1^{[p]},\ldots,x_n^{[p]},y_1^{[p]},\ldots,y_n^{[p]}]
\end{equation*}
acts on the generators $\xi$ as
\begin{equation*}
f^c(\xi_i)=\sum_{j=1}^{2n}(a_{ij})^{[p]}\xi_j,
\end{equation*}
where the notation $(a_{ij})^{[p]}$ means taking the base field automorphism that is conjugate to the nonstandard Frobenius via the Steinitz isomorphism.



Let $\gamma:\mathbb{C}\rightarrow\mathbb{C}$ be an arbitrary automorphism of the field of complex numbers. Then, given an automorphism $f$ of the Weyl algebra $A_{n,\mathbb{C}}$ with coordinates $(a_{i,I})$, one can build another algebra automorphism using the map $\gamma$. Namely, the coefficients $\gamma(a_{i,I})$ define a new automorphism $\gamma_*(f)$ of the Weyl algebra, which is of the same degree as the original one. In other words, every automorphism of the base field induces a map $\gamma_*:A_{n,\mathbb{C}}\rightarrow A_{n,\mathbb{C}}$ which preserves the structure of the ind-object. It obviously is a group homomorphism.

\medskip

Now, if $P_{n,\mathbb{C}}$ denotes the commutative polynomial algebra with Poisson bracket, we may define an ind-group homomorphism $\phi:\Aut(A_{n,\mathbb{C}})\rightarrow \Aut(P_{n\mathbb{C}})$ as follows. Previously we had a morphism $f\mapsto f^c$, however as the example has shown it explicitly depends on the choice of the infinite prime $[p]$. We may eliminate this dependence by pushing the whole domain $\Aut(A_{n,\mathbb{C}})$ forward with a specific base field automorphism $\gamma$, namely $\gamma=\Theta_{[p]}^{-1}$ - the field automorphism which is Steinitz-conjugate with the inverse nonstandard Frobenius, and only then constructing the symplectomorphism $f^c_{\Theta}$ as the restriction to the (nonstandard) center. For the subgroup of tame automorphisms such as linear changes of variables this procedure has a simple meaning: just take the $[p]$-th root of all coefficients $(a_{i,I})$ first. We thus obtain a group homomorphism which preserves the filtration by degree and is in fact well-behaved with respect to the Zariski topology on $\Aut$ (indeed, the filtration $\Aut^{N}\subset \Aut^{N+1}$ is given by Zariski-closed embeddings). Formally, we have a proposition:

\begin{prop}
There is a system of morphisms
\begin{equation*}
\phi_{[p],N}:\Aut^{\leq N}(A_{n,\mathbb{C}})\rightarrow \Aut^{\leq N}(P_{n,\mathbb{C}}).
\end{equation*}
such that the following diagram commutes for all $N\leq N'$:
\begin{equation*}
\begin{tikzcd}
\Aut^{\leq N}(A_{n,\mathbb{C}}) \arrow{r}{\phi_{[p],N}} \arrow{d}{\mu_{NN'}} & \Aut^{\leq N}(P_{n,\mathbb{C}})\arrow{d}{\nu_{NN'}}\\
\Aut^{\leq N'}(A_{n,\mathbb{C}})\arrow{r}{\phi_{[p],N'}} & \Aut^{\leq N'}(P_{n,\mathbb{C}})
\end{tikzcd}
\end{equation*}



The corresponding direct limit of this system is given by $\phi_{[p]}$, which maps a Weyl algebra automorphism $f$ to a symplectomorphism $f^c_{\Theta}$.
\end{prop}
\medskip

The Belov -- Kontsevich conjecture then states:
\begin{conj}
$\phi_{[p]}$ is a group isomorphism.
\end{conj}
Injectivity may be established right away.
\begin{thm}
$\phi_{[p]}$ is an injective homomorphism.
\end{thm}
(See \cite{4} for the fairly elementary proof). 


\subsubsection{\bf On the loops related to infinite primes}\label{loops}
Let us at first assume that the Belov -- Kontsevich conjecture holds, with $\phi_{[p]}$ furnishing the isomorphism between the automorphism groups. This would be the case if all automorphisms in  $\Aut(A_{n,\mathbb{C}})$ were tame, which is unknown at the moment for $n>1$.



The main result of the paper is as follows:

\begin{thm}
If one assumes that $\phi_{[p],N}$ is surjective for any infinite prime $[p]$, then $\Phi_N$ is quasifinitedimensional and its eigenvalues are roots of unity.
\end{thm}
\smallskip

Let $[p]$ and $[p']$ be two distinct classes of $\mathcal{U}$-congruent prime number sequences - that is, two distinct infinite primes. We then have the following diagram:
\begin{equation*}
\begin{tikzcd}
\Aut(A_{n,\mathbb{C}}) \arrow{r}{\phi_{[p]}} \arrow{d}{isom} & \Aut(P_{n,\mathbb{C}})\arrow{d}{isom}\\
\Aut(A_{n,\mathbb{C}})\arrow{r}{\phi_{[p']}} & \Aut(P_{n,\mathbb{C}})
\end{tikzcd}
\end{equation*}

with all arrows being isomorphisms. Vertical isomorphisms answer to different presentations of $\mathbb{C}$ as $\overline{\mathbb{Z}_{[p]}}$ and $\overline{\mathbb{Z}_{[p']}}$. The corresponding automorphism $\mathbb{C}\rightarrow \overline{\mathbb{Z}_{[p]}}$ is denoted by $\alpha_{[p]}$ for any $[p]$.
\smallskip

The fact that all the arrows in the diagram are isomorphisms allows one instead to consider a loop of the form
\begin{equation*}
\Phi:\Aut(A_{n,\mathbb{C}})\rightarrow \Aut(A_{n,\mathbb{C}}).
\end{equation*}

Furthermore, as it was noted in the previous section, the morphism $\Phi$ belongs to \\
$\Aut(\Aut(A_{n,\mathbb{C}}))$.

We need to prove that $\Phi$ is a trivial automorphism. The first observation is as follows.

\begin{prop}
The map $\Phi$ is a morphism of algebraic varieties.
\end{prop}

\begin{proof}
Basically, this is a property of $\phi_{[p]}$ (or rather its unshifted version, $f_p\mapsto f^c_p$). More precisely, it suffices to show that, given an automorphism $f_p$ of the Weyl algebra in positive characteristic $p$ with coordinates $(a_{i,I})$, its restriction to the center (a symplectomorphism) $f^c_p$ has coordinates which are polynomials in $(a_{i,I}^p)$.

\smallskip

The switch to positive characteristic and back is performed for a fixed $f\in\Aut (A_{n,\mathbb{C}})$ on an index subset $A_f\in\mathcal{U}$.

\smallskip

Let $f$ be an automorphism of $A_{n,\mathbb{C}}$ and let $N=\Deg f$ be its degree. The automorphism $f$ is given by its coordinates $a_{i,I}\in\mathbb{C}$, $i=1,\ldots,2n$, $I=\lbrace i_1,\ldots,i_{2n}\rbrace$, obtained from the decomposition of algebra generators $\zeta_i$ in the standard basis of the free module:
\begin{equation*}
f(\zeta_i)=\sum_{i,I}a_{i,I}\zeta^I,\;\;\zeta^I=\zeta_1^{i_1}\cdots\zeta_{2n}^{i_{2n}}.
\end{equation*}

\medskip

Let $(a_{i,I,p})$ denote the class $\alpha_{[p]}(a_{i,I})$, $p=(p_m)$, and let $\lbrace R_k(a_{i,I}\;|\;i,I)=0\rbrace_{k=1,\ldots,M}$ be a finite set of algebraic constraints for coefficients $a_{i,I}$. Let us denote by $A_1,\ldots,A_M$ the index subsets from the ultrafilter $\mathcal{U}$, such that $A_k$ is precisely the subset, on whose indices the constraint $R_k$ is valid for $(a_{i,I,p})$. Take $A_f=A_1\cap\ldots\cap A_M\in\mathcal{U}$ and for $p_m$, $m\in A_f$, define an automorphism $f_{p_m}$ of the Weyl algebra in positive characteristic $A_{n,\mathbb{F}_{p_m}}$ by setting
\begin{equation*}
f_{p_m}(\zeta_i)=\sum_{i,I}a_{i,I,p_m}\zeta^I.
\end{equation*}
All of the constraints are valid on $A_f$, so that $f$ corresponds to a class $[f_p]$ modulo ultrafilter $\mathcal{U}$ of automorphisms in positive characteristic. The degree of every $f_{p_m}$ ($m\in A_f$) is obviously less than or equal to $N=\Deg f$.

\bigskip



Now consider $f\in\Aut^{\leq N}(A_{n,\mathbb{C}})$ with the index subset $A_f$ over which its defining constraints are valid. The automorphisms $f_{p_m}=f_p:A_{n,\mathbb{F}_p}\rightarrow A_{n,\mathbb{F}_p}$ defined for $m\in A_f\in\mathcal{U}$ provide arrays of coordinates $a_{i,I,p}$. Let us fix any valid $p_m=p$ denote by $\mathit{F}_{p^k}$ a finite subfield of $\mathbb{F}_p$ which contains the respective coordinates $a_{i,I,p}$ (one may take $k$ to be equal to the maximum degree of all minimal polynomials of elements $a_{i,I,p}$ which are algebraic over $\mathbb{Z}_p$).

\smallskip

Let $a_1,\ldots,a_s$ be the transcendence basis of the set of coordinates $a_{i,I,p}$ and let $t_1,\ldots,t_s$ denote $s$ independent (commuting) variables. Consider the field of rational functions:

\begin{equation*}
\mathit{F}_{p^k}(t_1,\ldots,t_s).
\end{equation*}
\medskip
The vector space
\begin{equation*}
\Der_{\mathbb{Z}_p}(\mathit{F}_{p^k}(t_1,\ldots,t_s),\mathit{F}_{p^k}(t_1,\ldots,t_s))
\end{equation*}
of all $\mathbb{Z}_p$-linear derivations of the field $\mathit{F}_{p^k}(t_1,\ldots,t_s)$ is finite-dimensional with \\$\mathbb{Z}_p$-dimension equal to $ks$; a basis of this vector space is given by elements $$\lbrace e_a\mathit{D}_{t_b}\;|\;a=1,\ldots, k,\;b=1,\ldots,s\rbrace$$ where $e_a$ are basis vectors of the $\mathbb{Z}_p$-vector space  $\mathit{F}_{p^k}$, and $\mathit{D}_{t_b}$ is the partial derivative with respect to the variable $t_b$.

\smallskip

Set $a_1,\ldots,a_s=t_1,\ldots,t_s$ (i.e. consider an $s$-parametric family of automorphisms), so that the rest of the coefficients $a_{i,I,p}$ are algebraic functions of $s$ variables $t_1,\ldots,t_s$. We need to show that the coordinates of the corresponding symplectomorphism $f_p^c$ are annihilated by all derivations $e_a\mathit{D}_{t_b}$.

Let $\delta$ denote a derivation of the Weyl algebra induced by an arbitrary basis derivation $e_a\mathit{D}_{t_b}$ of the field. For a given $i$, let us introduce the short-hand notation
\begin{equation*}
a=f_p(\zeta_i),\;\;b=\delta(a).
\end{equation*}
\medskip
We need to prove that
\begin{equation*}
\delta(f^c(\xi_i))=\delta(f_p(\zeta_i^p))=0.
\end{equation*}
In our notation $\delta(f_p(\zeta_i^p))=\delta(a^p)$, so by Leibnitz rule we have:
\begin{equation*}
\delta(f_p(\zeta_i^p))=ba^{p-1}+aba^{p-2}+\cdots+a^{p-1}b.
\end{equation*}
\smallskip

Let $\ad_x:A_{n,\mathbb{F}_p}\rightarrow A_{n,\mathbb{F}_p}$ denote a $\mathbb{Z}_p$-derivation of the Weyl algebra corresponding to the adjoint action (all Weyl algebra derivations are inner!):
\begin{equation*}
\ad_x(y)=[x,y].
\end{equation*}
We will call an element $x\in A_{n,\mathbb{F}_p}$ locally ad-nilpotent if for any $y\in A_{n,\mathbb{F}_p}$ there is an integer $D=D(y)$ such that
\begin{equation*}
\ad_x^D(y)=0.
\end{equation*}
All algebra generators $\zeta_i$ are locally ad-nilpotent. Indeed, one could take $D(y)=\Deg y + 1$ for every $\zeta_i$.

If $f$ is an automorphism of the Weyl algebra, then $f(\zeta_i)$ is also a locally ad-nilpotent element for all $i=1,\ldots,2n$. That means that for any $i=1,\ldots,2n$ there is an integer $D\geq N+1$ such that
\begin{equation*}
\ad_{f_p(\zeta_i)}^D(\delta(f_p(\zeta_i)))=\ad_{a}^D(b)=0.
\end{equation*}

\smallskip

Now, for $p\geq D+1$ the previous expression may be rewritten as
\begin{equation*}
0=\ad_{a}^{p-1}(b)=\sum_{l=0}^{p-1}(-1)^l\binom{p-1}{l}a^lba^{p-1-l}\equiv\sum_{l=0}^{p-1}a^lba^{p-1-l}\;\;(\text{mod\;} p),
\end{equation*}
and this is exactly what we wanted. \\
\smallskip

We have thus demonstrated that for an arbitrary automorphism $f_p$ of the Weyl algebra in characteristic $p$ the coordinates of the corresponding symplectomorphism $f_p^c$ are polynomial in $p$-th powers of the coordinates of $f_p$, provided that $p$ is greater than $\Deg f_p + 1$. As the sequence $(\Deg f_{p_m})$ is bounded from above by $N$ for all $m\in A_f$, we see that there is an index subset $A^*_f\in\mathcal{U}$ such that the coordinates of the symplectomorphism $f_{p_m}^c$ for $m\in A^*_f$ are polynomial in $p_m$-th powers of $a_{i,I,p_m}$. This implies that $f^c$ in characteristic zero is given by coefficients polynomial in $\alpha_{[p]}(a_{i,I})^{[p]}$ as desired.

\smallskip

It follows, after shifting by the inverse nonstandard Frobenius, that $\Phi$ is an endomorphism of the algebraic variety $\Aut (A_{n,\mathbb{C}})$.
\end{proof}

\medskip

The automorphism $\Phi$ acting on elements $f\in\Aut(A_{n,\mathbb{C}})$, takes the set of coordinates $(a_{i,I})$ and returns a set $(G_{i,I}(a_{k,K}))$ of the same size. All functions $G_{i,I}$ are algebraic by the above proposition. It is convenient to introduce a partial order on the set of coordinates. We say that $a_{i,I'}$ is higher than $a_{i,I}$ (for the same generator $i$) if $|I|<|I'|$ and we leave pairs with $i\neq j$ or with $|I|=|I'|$ unconnected. We define the dominant elements $a_{i,I}$ (or rather, dominant places $(i,I)$) to be the maximal elements with respect to this partial order, and subdominant elements to be the elements covered by maximal ones (in other words, for fixed $i$, subdominant places are the ones with $|I|=|I_{\max}|-1$).

\smallskip

The next observation follows from the fact that the morphisms in question are algebra automorphisms.

\begin{lem}
Functions $G_{i,I}$ corresponding to dominant places $(i,I)$ are identities:
\begin{equation*}
G_{i,I}(a_{k,K})=a_{i,I}.
\end{equation*}
\end{lem}
\begin{proof}
Indeed, it follows from the commutation relations that for any $i=1,\ldots,2n$ and $f_p$, $p=p_m,\; m\in A_f\in\mathcal{U}$, the highest-order term in $f_p^c(\xi_i)=f_p(\zeta_i^p)=f_p(\zeta_i)^p$ has the coefficient $a_{i,I,p}^p$. The shift by the inverse Frobenius then acts as the $p$-th root on the dominant place, so that we deduce that the latter is independent of the choice of $[p]$.
\end{proof}

\medskip

Let us now fix $N\geq 1$ and consider
\begin{equation*}
\Phi_N:\Aut^{\leq N} A_{n,\mathbb{C}}\rightarrow \Aut^{\leq N} A_{n,\mathbb{C}}
\end{equation*}
-- the restriction of $\Phi$ to the subvariety $\Aut^{\leq N} A_{n,\mathbb{C}}$, which is well defined by the above lemma. The morphism corresponds to an endomorphism of the ring of functions
\begin{equation*}
\Phi_N^*:\mathcal{O}(\Aut^{\leq N} A_{n,\mathbb{C}})\rightarrow \mathcal{O}(\Aut^{\leq N} A_{n,\mathbb{C}})
\end{equation*}

Let us take a closer look at the behavior of $\Phi_N$ (and of $\Phi^*_N$, which is essentially the same up to an inversion), specifically at how $\Phi_N$ affects one-dimensional subvarieties of automorphisms. Let $\mathcal{X}_N$ be the set of all algebraic curves of automorphisms in $\Aut^{\leq N} A_{n,\mathbb{C}}$; by virtue of Lemma 3.3 we may without loss of generality consider the subset of all curves with fixed dominant places -- we denote such a subset by $\mathcal{X}_N'$, and, for that same matter, the subsets $\mathcal{X}_N^{(k)}$ of curves with fixed places of the form $(i,I')$, which are away from a dominant place by a path of length at most $(k-1)$. In particular one has $\mathcal{X}_N'=\mathcal{X}_N^{(1)}$.

The morphism $\Phi_N$ yields a map
\begin{equation*}
\tilde{\Phi}_N:\mathcal{X}_N\rightarrow \mathcal{X}_N
\end{equation*}
and its restrictions
\begin{equation*}
\tilde{\Phi}_N^{(k)}:\mathcal{X}_N^{(k)}\rightarrow \mathcal{X}_N.
\end{equation*}
Our immediate goal is to prove that for all attainable $k$ we have
\begin{equation*}
\tilde{\Phi}_N^{(k)}:\mathcal{X}_N^{(k)}\rightarrow \mathcal{X}_N^{(k)},
\end{equation*}
i.e. the map $\Phi_N$ preserves the terms corresponding to non-trivial differential monomials.

In spite of minor abuse of language, we will call the highest non-constant terms of a curve in $\mathcal{X}_N^{(k)}$ dominant, although they cease to be so when that same curve is regarded as an element of $\mathcal{X}_N$.

Let $\mathcal{A}\in\mathcal{X}_N$ be an algebraic curve in general position. Coordinate-wise $\mathcal{A}$ answers to a set $(a_{i,I}(\tau))$ of coefficients parameterized by an indeterminate. By Lemma 3.3, $\Phi_N$ leaves the (coefficients corresponding to) dominant places of this curve unchanged, so we may well set $\mathcal{A}\in\mathcal{X}_N^{(1)}$. In fact, it is easily seen that the subdominant terms are not affected by $\Phi_N$ either, thanks to the commutation relations that define the Weyl algebra: for every $p$ participating in the ultraproduct decomposition, after one raises to the $p$-th power one should perform a reordering within the monomials -- a procedure which degrades the cardinality $|I|$ by an even number. Therefore, nothing contributes to the image of any subdominant term other than that subdominant term itself, which therefore is fixed under $\Phi_N$. We are then to consider the image

\begin{equation*}
\tilde{\Phi}_N^{(2)}(\mathcal{A})\in \mathcal{X}_N^{(2)}.
\end{equation*}

Again, given a positive characteristic $p$ within the ultraproduct decomposition, suppose the curve $\mathcal{A}$ (or rather its component answering to the chosen element $p$) has a number of poles attained on dominant\footnote{With respect to $\mathcal{X}_N^{(2)}$, i.e. the highest terms that actually change - see above where we specify this convention.} terms. Let us pick among these poles the one of the highest order $k$, and let $(i_0,I_0)$ be its place. By definition of an automorphism of Weyl algebra as a set of coefficients, the number $i_0$ does not actually carry any meaningful data, so that we are left with a pair $(k,|I_0|)$. As we can see, this pair is maximal from two different viewpoints; in fact, the pair represents a vertex of a Newton polygon taken over the appropriate field, with the discrete valuation given by $|I|$. The coordinate function $a_{i_0,I_0}$ corresponding to this pole admits a decomposition

\begin{equation*}
a_{i_0,I_0}=\frac{a_{-k}}{t^k}+\cdots,
\end{equation*}
with $t$ a local parameter. Acting upon this curve by the morphism $\Phi_N$ amounts to two steps: first, we raise everything to the $p$-th power and then assemble the components within the ultraproduct decomposition, then we take the preimage, which is essentially the same as taking the $p'$-root, with respect to a different ultraproduct decomposition. The order of the maximal pole is then multiplied by an integer during the first step and divided \emph{by the same integer} during the second one. By maximality, there are no other terms that might contribute to the resulting place in $\tilde{\Phi}_N^{(2)}(\mathcal{A})$. It therefore does not change under $\Phi_N$.

We may process the rest of the dominant (with respect to $\mathcal{X}_N^{(2)}$) terms similarly: indeed, it suffices to pick a different curve in general position. We then move down to $\mathcal{X}_N^{(k)}$ with higher $k$ and argue similarly.

\smallskip

After we have exhausted the possibilities with non-constant terms, we arrive at the conclusion that all that $\Phi_N$ does is permute the irreducible components of $\Aut^{\leq N} A_{n,\mathbb{C}}$. That in turn implies the existence of a positive integer $l$ such that

\begin{equation*}
\Phi_N^l=\text{Id}.
\end{equation*}

\medskip

In fact, the preceding argument gives us more than just the observation that $\Phi_N$ is unipotent.  Let $\Phi_{N,M}^*$ denote the linear map of finite-dimensional vector spaces obtained by restricting $\Phi_{N}^*$ to regular functions of total degree less than or equal to $M$. Then the following proposition holds.

\begin{prop}
If $\lambda$ is an eigenvalue of $\Phi_{N,M}^*$, then $\lambda^k=1$ for some integer $k$.
\end{prop}

\begin{proof}
Indeed, should there exist $\lambda_0\neq 1$, we may find an exceptional curve whose singularity changes under $\Phi_N$, note that coefficients are products of normalization coordinates.
\end{proof}














\subsubsection{\bf Discussion}\label{ds}
The investigation of decomposition of polynomial algebra-related objects into ultraproducts over the prime numbers $\mathbb{P}$ leads to a problem of independence of the choice of infinite prime. In the case of the Tsuchimoto -- Belov -- Kontsevich homomorphism the answer turns out to be affirmative, although there are other constructions, which are of algebraic or even polynomial nature but for which the independence fails. The reason for such arbitrary behavior has a lot to do with growth functions (in which case the situation is similar to the one described in\cite{17}, and in fact in\cite{5}, where one has a non-injective endomorphism $f_p:A_{n,\mathbb{F}_p}\rightarrow A_{n,\mathbb{F}_p}$, whose degree grows with $p$, which disallows for the construction of a naive counterexample to the Dixmier Conjecture in the ultralimit). It is, in our view, worthwhile to study such behavior in greater detail.
