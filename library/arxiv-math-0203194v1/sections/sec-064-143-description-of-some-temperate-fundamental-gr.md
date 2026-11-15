---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-064-143-description-of-some-temperate-fundamental-gr
section_title: "Description of some temperate fundamental groups."
section_number: 14.3
pages: 139-145
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.976
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::2.3}

 In this subsection, we assume that $K$ is {\it
 algebraically closed of characteristic $0$} (typically $K=\C_p$).

\begin{para}\label{para::2.3.1} It follows from \ref{pro::2.1.5}
 (together with \ref{para::1.4.1}) 
 that $\P^1$ and $\A^1$ have trivial temperate fundamental
 groups\footnote{in contrast, recall that $\A^1$ has non-trivial
 locally-algebraic fundamental group, and that $\P^1$ has trivial
 locally-algebraic fundamental group but non-trivial \'etale fundamental
 group.}.

Let us next examine $\G_m=\P^1\setminus\{0,\infty\}$. We have
$\pi_1^{\mathrm{top}}(\G_m,1)=0$; on the other hand, any connected finite
\'etale covering is Kummer $\G_m\to \G_m,\; x\mapsto x^n$. It follows that
\begin{equation*}
\pi_1^{\mathrm{temp}}(\G_m,1)=\pi_1^{\mathrm{alg}}(\G_m,1)=\widehat{\Z}(1):=
 \underset{n}{\limproj}\,\mu_n \cong \widehat{\Z}=\prod_\ell \Z_\ell.
\end{equation*}

\noindent Similarly, $\displaystyle\pi_1^{\mathrm{temp}}(\G_m^n,1)\cong
 \widehat{\Z}^n$. 
\end{para}

\begin{para}\label{para::2.3.2} {\it Elliptic curves.} Let us first consider
 the case of an {\it elliptic curve with good reduction} $S\;$ (so that
 $\pi_1^{\mathrm{top}}(S,1)=\{1\}$).  Then any finite
 \'etale covering is given by an isogeny
 $S'\to S$ and $S'$ has good reduction. Hence any temperate covering is
 an isogeny, and 
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(S,1)=\pi_1^{\mathrm{alg}}(S,1)\cong \widehat{\Z}\times
   \widehat{\Z}.
 \end{equation*} 
 Let now $S=\G_m/q^\Z$ be instead a {\it Tate elliptic curve}. Then the
 homomorphisms 
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(\G_m,1)\to \pi_1^{\mathrm{temp}}(S,1)\to q^\Z
 =\pi_1^{\mathrm{top}}(S,1)  
 \end{equation*}
 actually give rise to a canonical exact sequence
 (\ref{cor::1.4.12}. (b) may be applied here)
 \begin{equation*}
  1\to \widehat{\Z}(1)\to  \pi_1^{\mathrm{temp}}(S,1)\to  \Z \to 1,
\end{equation*}
 and since $ \pi_1^{\mathrm{temp}}(S,1)\subset
 \pi_1^{\mathrm{alg}}(S,1)\cong \widehat{\Z}\times \widehat{\Z}$ is
 abelian, to a non-canonical isomorphism 
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(S,1)\cong \widehat{\Z}\times \Z.
 \end{equation*} 
 This is the simplest manifestation of the lacunary character of
 temperate fundamental groups.

 \medskip\noindent (The case of a Tate curve deprived from its origin is
 more difficult).
\end{para}

\begin{para}
 \label{para::2.3.3} {\it Mumford curves.} Let now $S$ be a Mumford
 curve of genus $g>1$:

 \noindent $S=\Omega/\Gamma,\;
 \;\Omega\cong \tilde S,\;$ and $\pi_1^{\mathrm{top}}(S,s)\cong \Gamma$,
 a Schottky group, free on $g$ generators.

 \noindent We have homomorphisms 
 \begin{equation*}
 \pi_1^{\mathrm{temp}}(\Omega,\bar{\tilde s})\to
  \pi_1^{\mathrm{temp}}(S,\ovl{s})\to  \pi_1^{\mathrm{top}}(S,s)
 \end{equation*}
 which give rise to an exact sequence  
 \begin{equation*}
 1\to H \to \pi_1^{\mathrm{temp}}(S,\ovl{s})\to 
 \pi_1^{\mathrm{top}}(S,s) \to 1 
 \end{equation*}
 with $H:= \Im(\pi_1^{\mathrm{temp}}(\Omega,\bar{\tilde
 s})\to \pi_1^{\mathrm{temp}}(S,\ovl{s}))^-\subset
 \pi_1^{\mathrm{temp}}(S,\ovl{s}) $. As an abstract group,
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is thus the semidirect product
 $H.\Gamma$.
 
 \noindent Passing to the profinite completion, we get an exact sequence
 \begin{equation*}
  \widehat{H} \to \pi_1^{\mathrm{alg}}(S,\ovl{s})\to 
 \widehat{\Gamma} \to 1, 
 \end{equation*}
 and the homomorphism
 $\pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})\to
 \pi_1^{\mathrm{alg}}(S,\ovl{s})$ factors through 
 $\widehat{H}$. 

 \medskip This homomorphism is very far from being injective. The point
 is that the \'etale covering of $S$ obtained from an arbitrary finite
 Galois \'etale covering $\Omega'\to \Omega$ is not Galois (or, what
 amounts to the same by \ref{thm::2.1.8}, not temperate). The finite
 Galois \'etale coverings $\Omega'\to \Omega$ which give rise to a
 Galois covering of $S$ are called ``equivariant'' in \cite[1.3]{ecoamc}; 
 by \ref{thm::2.1.8}, they 
 correspond to a topological Galois covering of some Galois \'etale
 covering $S'\to S$.

 Moreover, there are examples \cite[2.7]{ecoamc} (one may choose for $\Omega$
 the Drinfeld half-plane) where the degrees of $\Omega'/
 \Omega$ and $S'/ S$ coincide, but $\Omega'$ is not the universal
 topological covering of $S'$ ; it follows that $\Omega'$ 
 is not simply-connected (in fact, its topological fundamental group is
 free of infinite type), and that the injection 
 $\pi_1^{\mathrm{temp}}(\Omega,\bar{\tilde s})\to
 \pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})$ {\it is not a bijection in
 general}.

 Let us return to the non-injectivity of
 $\pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})\to
 \pi_1^{\mathrm{alg}}(S,\ovl{s})$. Actually, the 
 following stronger result holds: {\it $\pi_1^{\mathrm{alg}}(S,\ovl{s})$
 is metrizable, while $\pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})$ is 
 not}.  

 \noindent Recall that a profinite group is metrizable if and only if the
 set of its open subgroups is countable, 
 \cf \cite[1.3]{serre94:_cohom}. This is the case for
 $\pi_1^{\mathrm{alg}}(S,\ovl{s})$, which is even topologically finitely
 generated, but 
 not for $\pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})$. In fact, one can
 show that for any 
 $n\geq 1$, the set of open subgroups $H\subset
 \pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})$ endowed with an isomorphism
 $\pi_1^{\mathrm{alg}}(\Omega,\bar{\tilde s})/H\to \Z/n\Z$ is already
 uncountable. Indeed, this set may be identified with
 $\mathcal{O}(\Omega)^\times/(\mathcal{O}(\Omega)^\times)^n$, or else
 with the set of $\Z/n\Z$-valued 
 currents\footnote{\ie $\Z/n\Z$-valued functions on the edges of the
 tree, such that the sum of its values at the edges starting from an 
 arbitrary vertex is zero.} on the tree associated to
 $\Omega$ (\cf \cite[I.8.9, V.2.3]{garea}). Since $g\geq 2$, this 
 tree has infinitely many vertices connected to more than 
 two edges, and it follows that the $\Z/n\Z$-valued currents do not form
 a countable set.  

 A similar picture holds for Mumford curves deprived from a
 finite set of points.
\end{para}

\begin{para}\label{para::2.3.4} {\it Affinoid curves with good reduction.} In
 this case, one has 
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(S,\ovl{s})=\pi_1^{\mathrm{alg}}(S,\ovl{s}) .
 \end{equation*} 
 We may assume that $s$ is the maximal point of $S$ corresponding to the
 sup-norm. The assertion then follows from De Jong's observation 
 \cite[7.5]{efgonas} that the map
 $\pi^{\mathrm{et}}_1(s,\ovl{s})=\pi^{\mathrm{alg}}_1(s,\ovl{s})\to
 \pi^{\mathrm{alg}}_1(S,\ovl{s})$ is already surjective. We shall only
 need the case of the closed unit disk. The proof goes 
 as follows (assuming that $S\subset \P^1$ as in {\it loc.~cit.}).

 One has to show that any finite \'etale covering $f:\;S'\to S$ of
 degree $n$ such that $S'_s= \{t_1,\ldots, t_n\}$ splits.  The
 assumption implies that $f$ is a local isomorphism around each $t_i$
 (\cf \ref{para::1.2.1}). Hence one can find an affinoid neighborhood $V$ of $s$ such
 that $S'_{| V}= W_1\coprod \ldots \coprod W_n$, and $W_i\cong
 V$. Because $V$ contains the maximal point $s$ which is the boundary of
 $S$ in $\P^1$ (in the sense of \cite[3.1]{staagonf}, we get an admissible
 covering (for the Grothendieck topology) of $\P^1= S \cup
 (\P^1\setminus(S\setminus V))$ by closed analytic subdomains. One then
 glues $S'$ and $n$ copies of $\P^1\setminus(S\setminus V)$ together via
 the isomorphisms $W_i\to V$ in order to get a finite \'etale covering of
 $\P^1$ which restricts to $S'$ over $S$. Such a covering is trivial.
 
 \medskip Concerning the algebraic fundamental group of the closed unit
 disk over $\C_p$, one has the following result, 
 essentially due to M. Raynaud (not used in the sequel):
\end{para}

\begin{thm}\label{thm::2.3.5} $\quad$ A finite group is a quotient of the
 profinite group $\;$ 
 $\pi_1^{\mathrm{alg}}\bigl(\matheur{D}_{\C_p}(0,1^+),0\bigr)$
 if and only if it is generated by its $p$-Sylow subgroups.
\end{thm}

 The necessity of the condition means that any finite Galois
 \'etale covering of $\matheur{D}_{\C_p}(0,1^+)$ of order prime to $p$
 is trivial, which is proven in \cite[6.3.3]{ecfnas} and
 \cite[2.11]{repfapf}.  The 
 converse is much harder and follows from Raynaud's solution of the
 Abhyankar conjecture on finite \'etale coverings of $\A^1_{\ovl{\F}_p}$,
 \cf \cite{rdldaecpecd}. Of course, we may replace $0$ by any geometric
point or tangential base-point (\cf \ref{pro::2.2.3}).

\medskip The standard example of a non-trivial finite Galois \'etale
 covering of $\matheur{D}(0,1^+)$ is the Artin-Schreier covering
 $\matheur{D}(0,1^+) \xrightarrow{z\mapsto z^p-z} \matheur{D}(0,1^+)$
 (with group $\Z/p$); it splits on any smaller concentric disk.
 A less standard 
 example, with non-solvable Galois group $A_5$, is given by $\matheur{D}(1,1^+)
 \setminus \matheur{D}(0,1^-) \xrightarrow{z\mapsto z^3-z^{-2}}
 \matheur{D}(0,1^+)$ for $p=3$.
 
\begin{para}\label{para::2.3.6} {\it Punctured disks.} Let us fix $r\in  {|
 K^\times|}$, and set $\; \matheur{D}_r=\matheur{D}_K(0,r^+),\;\;
 \matheur{D}_r^\ast=D_r\setminus \{0\}$.  We let $\ovl{s}$ be any
 geometric point or tangential base-point of $\matheur{D}^\ast$.
\end{para}

\begin{pro}\label{pro::2.3.7} There are canonical isomorphisms 
\begin{equation*}
\pi_1^{\mathrm{temp}}(\matheur{D}_r^\ast,\ovl{s})=
 \pi_1^{\mathrm{alg}}(\matheur{D}_r^\ast,\ovl{s})=
 \pi_1^{\mathrm{alg}}(\matheur{D}_r,\ovl{s})\times \widehat{\Z}(1).
\end{equation*}
\end{pro}

\begin{proof}
 By homothety, we may assume that $r=1$ (and drop the index
 $r$). These canonical isomorphisms are induced by the 
 obvious fully faithful functors (\cf \ref{cor::1.4.8}):
 \begin{equation*}
 \Cov^{\mathrm{kum}}_{\matheur{D}^\ast} \hookrightarrow
 \Cov^{\mathrm{alg}}_{\matheur{D}^\ast},\;\; 
 \Cov^{\mathrm{alg}}_{\matheur{D}} \hookrightarrow 
 \Cov^{\mathrm{alg}}_{\matheur{D}^\ast}\hookrightarrow
 \Cov^{\mathrm{temp}}_{\matheur{D}^\ast} 
 \end{equation*}
 where $\Cov^{\mathrm{kum}}_{\matheur{D}^\ast}$ denotes the category of
 finite disjoint unions of Kummer coverings of $\matheur{D}^\ast$; it is
 stable under taking connected 
 components, fiber products (the fiber product of a Kummer covering of
 degree $m$ and a Kummer covering of degree $n$ is a finite disjoint
 union of Kummer coverings of degree $\mathrm{lcm}(m,n)$) and quotients. The
 fundamental group $\pi_1^{\mathrm{kum}}(\matheur{D}^\ast,\ovl{s})$ is
 clearly $\Z(1)$.

 Assume for a while that $s$ is the maximal point of $\matheur{D}$ (the
 statement does not depend on the choice of $s$). Then as we have seen in
 \ref{para::2.3.4}, 
 the homomorphism $\pi_1^{\mathrm{temp}}(s,\ovl{s})\to
 \pi_1^{\mathrm{alg}}(\matheur{D},\ovl{s})$ is surjective. Since it
 factors through 
 $\pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s})$, it follows that
 $\pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s})\to\pi_1^{\mathrm{temp}}
 (\matheur{D},\ovl{s}) 
 = \pi_1^{\mathrm{alg}}(\matheur{D} ,\ovl{s})$ is surjective.
 
 Let us now take for $s$ a tangential base-point at $0$. Let us consider 
 the maps $\matheur{D}_r\to \matheur{D}$ (for $r\in {|K^\times|},\;r<1$) 
 and the corresponding homomorphism (\cf \ref{para::1.4.10}):
 \begin{equation*}
 \pi_1^{\mathrm{temp}}(\matheur{D}_r^\ast,\ovl{s})\to
 \pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s}).
 \end{equation*}
 It follows from \ref{lem::2.1.11} that 
 \begin{equation*}
 \underset{r\to 0}\limproj\,
  \Im(\pi_1^{\mathrm{temp}}(\matheur{D}_r^\ast,\ovl{s})\to
  \pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s})) = \Z(1),
 \end{equation*}
 the composition 

 \begin{equation*}
 \Z(1)\to \pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s})\to\Z(1)
 \end{equation*}
 being identity. It remains to show that the sequence 

 \begin{equation*}
 1\to \Z(1)\to \pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s}) \to
 \pi_1^{\mathrm{temp}}(\matheur{D} ,\ovl{s})=
 \pi_1^{\mathrm{alg}}(\matheur{D} ,\ovl{s})\to 1 
 \end{equation*}
 is exact. The problem is only in the middle; since
 $\pi_1^{\mathrm{temp}}(\matheur{D}^\ast,\ovl{s})$ is a pro-discrete group, it
 amounts to the following fact, which is a very special case of
 \ref{lem::2.1.11}: a 
 temperate Galois covering of $\matheur{D}^\ast$ extends to
 $\matheur{D}$ if and only if its 
 restriction to a sufficiently small punctured disk centered at $0$ splits.
\end{proof}

\medskip
On the other hand, the consideration of the logarithmic \'etale covering
restricted to a punctured disk centered at infinity shows that
$\pi_1^{\mathrm{loc.alg}}(\matheur{D}_r^\ast,\ovl{s})\neq
\pi_1^{\mathrm{alg}}(\matheur{D}_r^\ast,\ovl{s})$, and {\it a fortiori},
\begin{equation*}
 \pi_1^{\mathrm{et}}(\matheur{D}_r^\ast,\ovl{s})\neq
 \pi_1^{\mathrm{temp}}(\matheur{D}_r^\ast,\ovl{s}).
\end{equation*}
  
\begin{para}\label{para::2.3.8} {\it $\A^1$ minus a few points.}
 Let $S=\A^1\setminus\{\zeta_1,\ldots,\zeta_m\}$. For any $i=1,\ldots,
 m$, let $\vec t_i$ be a tangential base-point at $\zeta_i$, and let
 $\alpha_i$ be a temperate path from $\vec t_i$ to a fixed geometric
 point $\ovl{s} $ (or tangential base-point) of $ S$. Then we have a
 canonical homomorphism corresponding to Kummer coverings induced by
 $z-\zeta_i\mapsto (z-\zeta_i)^n$ (\cf \ref{para::2.3.6})

 \begin{equation*}
  \widehat{\Z}(1)\hookrightarrow \pi_1^{\mathrm{temp}}(S,\vec
  t_i)\to\widehat{\Z}(1)
 \end{equation*}
 whose composition is identity. 
 By composition with $\mathrm{ad}(\alpha_i)$, we get a monomorphism 
 \begin{equation*}
  \widehat{\Z}(1)\hookrightarrow \pi_1^{\mathrm{temp}}(S,\ovl{s}) 
 \end{equation*}
 which depends of course on $\alpha_i$.  Let us denote by $\gamma_i$ the
 image in $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ of a topological generator
 of $\widehat{\Z}(1)\cong \widehat{\Z}$. The `local monodromies' $\gamma_i$ are
 not at all canonical, but the {\it smallest closed normal subgroup}
 $\an{\gamma_i}^-$ of $\pi_1^{\mathrm{temp}}(S,\ovl{s}) $ which contains
 them is independent of all choices. In fact we have\footnote{this is
 the correct version of cor. 5.3 in \cite{poaptg}, which was wrongly
 stated.}: 
\end{para}

\begin{pro}\label{pro::2.3.9}
 $\an{\gamma_i}^-=
 \pi_1^{\mathrm{temp}}(\A^1\setminus\{\zeta_1,\ldots, \zeta_m\},\ovl{s})$.
\end{pro}

\begin{proof}
 This amounts to saying that a temperate (Galois, if one wishes)
 covering splits if its restriction to sufficiently small punctured disks
 around any of the $\zeta_i$ splits. But the latter condition implies
 that the covering extends to a temperate covering of $\A^1$ 
 (\cf \ref{thm::2.1.10}), which automatically splits (\cf \ref{para::2.3.1}).
\end{proof}

\medskip By analogy with the complex situation, \ref{pro::2.3.9}
suggests two questions:

\begin{que}\label{que::2.3.10} Is it possible to choose the $\gamma_i$'s
 in such a way that they are topological generators of
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ ? 
\end{que}

Following the above construction, one can introduce also introduce a
local monodromy $\gamma_\infty$ at $\infty$. 

\begin{que}\label{que::2.3.11} Is it possible to choose the $\gamma_i$'s
 and $\gamma_\infty$ in such a way that their product (in suitable
 order) is identity?
\end{que}

We do not know the answer to \ref{que::2.3.10}, but shall answer 
\ref{que::2.3.11} in \ref{sec::6}, when we have more tools at disposal.

For $m\geq 2$, $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is indeed a rather
complicated topological group, far from being discrete and from being compact:

\begin{pro}\label{pro::2.3.12} For $m\geq 2$,
 $\pi_1^{\mathrm{temp}}(\A^1\setminus\{\zeta_1,\ldots,
 \zeta_m\},\ovl{s}) $ is not locally compact.
\end{pro}

\begin{proof}
 Assume that $\pi_1^{\mathrm{temp}}(S,\ovl{s}) $ is
 locally compact. Then because $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is a
 prodiscrete group, there would exist a {\it compact} (necessarily
 totally discontinuous, hence profinite) open normal subgroup $H$. Let
 $S'\to S$ be the corresponding Galois temperate covering with group
 $G=\pi_1^{\mathrm{temp}}(S,\ovl{s})/H$. Up to replacing $H$ by a small
 subgroup, we may and shall assume that $S'=\tilde T$ is the topological
 universal covering of a finite Galois \'etale covering $T$ of $S$. Via
 \ref{pro::2.1.7}, we then have an exact sequence
 \begin{equation*}
 1\to H\to \pi_1^{\mathrm{temp}}(T,\ovl{t})\to \pi_1^{\mathrm{top}}(T,
 \ovl{t} )\to 1. 
 \end{equation*}
 Let $T'$ be any finite \'etale covering of $T$. Then the universal
 topological covering $\tilde T'$ is a temperate covering of $T$ which
 dominates $S'=\tilde T$. Due to the compactness of $H$, the map $\tilde 
 T' \to \tilde T$ must be finite. 

 We now choose $T'$ in order to contradict this property. Let $\ovl{X}$
 be a projective smooth analytic curve over $K$ such that $\rk
 \pi_1^{\mathrm{top}}(\ovl{X}) > \rk \pi_1^{\mathrm{top}}(T)$. Assume
 that $\ovl{X}$ is endowed with a finite morphism to $\P^1$ which is
 unramified above $S$ (since $m\geq 2$, this just amounts to saying that
 $\ovl{X}$ is defined over $\ovl{\Q}$, according to a well-known theorem
 of Belyi). We set $X=\ovl{X}\times_{\P^1} S \subset \ovl{X}$, and choose
 for $T'$ a connected component of $ X\times_S T$. Note that since $T$ is
 Galois over $S$, $T'$ is Galois over $X$. Let $Y$ be a connected
 component of $X\times_S \tilde T$ lying above $X$. Then $\tilde T' $ is
 a topological covering of $Y$, and is finite over $Y$ (if and) only if 
 it coincides with $Y$.  We then have a commutative square of Galois 
 temperate coverings
 \begin{equation*}
  \begin{matrix}
   && Y = \tilde T'&&\\
   &\swarrow &&\searrow &\\
   \tilde X &&&& T' \\
   &\searrow &&
   \swarrow &\\
   &&X&&
  \end{matrix}
 \end{equation*}
 Now $\Aut_X Y$ admits the free group $\Aut_{T'} Y$ as a normal subgroup
 of finite index, and admits the free group $\Aut_X \tilde X$ as a
 quotient. Since $\rank \Aut_{T'} Y \leq \rank \pi_1^{\mathrm{top}}(T)<
 \rank \pi_1^{\mathrm{top}}(\ovl{X})=\rank\,\pi_1^{\mathrm{top}}(X)$, this is
 impossible. Therefore $\pi_1^{\mathrm{temp}}(S) $ is not locally compact.  
\end{proof}

 \medskip\noindent {\it Remark.} In \cite{andre:_une_gal}, temperate fundamental
 groups of algebraic $p$-adic manifolds will be used to give a geometric 
 description of the local Galois group $\Gal(\ovl{\Q}_p/\Q_p)$. 
 
\newpage
