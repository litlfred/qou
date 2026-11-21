---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-052-125-other-examples-of-global-p-adic-uniformizati
section_title: "Other examples of global $p$-adic uniformization."
section_number: 12.5
pages: 107-110
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.816
latex_coverage_ratio: 0.965
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:7.5}

\begin{para}\label{para:7.5.1}
 Shimura's paper \cite{shimura67:_const} deals not only with quaternion algebra
 over $\Q$, but also with quaternion algebras $B/E$ over a totally real
 number field $E$. When $B$ {\it splits at a single real place,} he
 constructs curves ${\mathcal{X}^+(N)}$ and ${\mathcal{X}^\ast}$
 satisfying properties similar to (a),(b),(c) of \ref{para:7.4.2}.


 In this context, $N$ may be an arbitrary ideal of $\mathcal{O}_E$,
 $\Q(\zeta_N)$ has to be replaced by the ray class field with conductor
 $N.\infty$, and the condition $N(g)>0$ means that the reduced norm of
 $g$ is totally positive, or, what amounts to the same, is positive at
 the split real place $\infty_0$.\index{000infinity0@$\infty_0$}
 
 The novelty, however, is that these Shimura curves have {\it no
 direct interpretation} as moduli spaces for
 decorated abelian varieties, since $B$ is not in the Albert list of
 endomorphism algebras of abelian varieties when $[E:\Q]>1$.


 To overcome this problem, Shimura introduces the following remarkable
 trick. Let $K$ be a totally imaginary quadratic extension of $E$. Then
 $B^\bullet =B\otimes_E K$ is in Albert's list (we endow it with the
 involution which is the tensor product of $\ast$ on $B$ and complex
 conjugation on $K$). It turns out that the Shimura varieties of PEL
 type for abelian varieties of dimension $g=4[E:\Q]$ ($\ast$-polarized,
 with level structure) with complex multiplication by $B^\bullet$ are
 twisted forms of the same curve. The Shimura curve attached to $B$ is
 obtained by Weil descent from the Shimura curves attached to
 $B\otimes_E K$, for sufficiently many quadratic extensions $K$.
\end{para}

\begin{para}\label{para:7.5.2}
 \v{C}erednik's original $p$-adic uniformization theorem
 already applies to Shimura curves attached to quaternion algebras over
 a totally real number field $E$. His method has been further developed
 in \cite{varshavsky98:_shimur}, \cite{varshavsky98:_shimur_ii}. On the
 other hand, Drinfeld's modular 
 approach has been extended by Boutot-Zink \cite{tpuosc}, using Shimura's
 trick. Let us sketch the principle of the construction.


 Let $G$ be the multiplicative group of $B^\times$, viewed as an
 algebraic group over $\Q$. Let $\Gamma$ be a congruence subgroup of
 $G^{\mathrm{ad}}(\Q)$ (alternatively, one can consider an open compact
 subgroup 
 $C$ of $G(\A_f)$). Let us first assume that $\Gamma$ is {\it maximal at
 $p$} (alternatively $C$ is of the form $C^pC_p$ for some open compact
 subgroup $C^p$ of $G(\A_f^p)$, \cf \ref{para:7.1.2}). The (non-connected) Shimura
 curve $\Sh$ given by
 \begin{equation*}
  \Sh_\C^{\mathrm{an}}= C\backslash \bigl((\P_\C^1\setminus\P^1(\R)) \times
   G(\A_f)\bigr) /G(\Q)
 \end{equation*}
 is defined over the reflex field, which is $E$ (embedded into $\R$ via
 $\infty_0$). Over some finite abelian extension $E'/E$, it decomposes as
 a disjoint union of geometrically connected Shimura curves
 $\mathcal{X}_\Gamma$ ($\mathfrak{h}/\Gamma$ over $\C\;$; one possible
 $\Gamma$ is the image of $G(\Q)\cap C$ in $\G^{\mathrm{ad}}(\Q)$).


 Let $v=v_0$ be a {\it critical} finite place of $E$, \ie such that
 $B_v$ is a non-split quaternion algebra. Let $p$ be the residue
 characteristic of $v_0$ and let $v_1,\ldots, v_m$ be the other places
 of $E$ above $p$.


 Let $K$ be a totally imaginary quadratic extension of $E$, such that
 every place $v_i$ splits in $K$. We denote by $w_i, \ovl{w_i}$ the two
 places of $K$ above $v_i$. The quaternion algebra $B^\bullet =
 B\otimes_E K$ is ramified at $w=w_0$: $B^\bullet_w\cong B_v$.


 We fix an extension $\infty_0: K\hookrightarrow \C$ of the real
 embedding $\infty_0$ of $E$, and a double embedding $\C \hookleftarrow
 \ovl{\Q} \hookrightarrow \C_p$ whose restriction to $K$ is compatible
 with $(\infty_0,w)$. The embeddings $K \hookrightarrow \C_p$ which
 factor through some $w_i$ but not through some $\ovl{w_i}$ form a CM
 type $\Psi$: $\Psi\coprod \ovl{\Psi}=\Hom(K,\C_p)$ (identified with
 $\Hom(K,\C)$ through our chosen double embedding).
 

There is a natural $\Q$-group $G^\bullet$ such that
 $G^\bullet(\Q)=\{b\in B^\bullet| bb^\ast\in E\}$, acting on
 $V^\bullet=V\otimes_E K$. One can attach to $C$ an open compact
 subgroup $C^\bullet$ of $G^\bullet(\A_f)$, maximal at $p$, and a
 Shimura curve $\Sh^\bullet$ such that $\Sh$ is open and closed in
 $\Sh^\bullet$ (\cite[3.11]{tpuosc}). Alternatively, one can attach to
 $\Gamma$ a congruence subgroup $\Gamma^\bullet$ in $G^{\bullet ad}(\Q)$
 and a corresponding connected Shimura curve
 $\mathcal{X}_{\Gamma^\bullet}$ which is a twisted form of
 $\mathcal{X}_{\Gamma}$ (defined over some abelian extension of
 $K$). The point is that this new Shimura curve $\Sh^\bullet$ is of PEL
 type. More precisely, for $C$ small enough, it is a moduli space for
 $\ast$-polarized abelian varieties of dimension $g=4[E:\Q]$ with
 multiplication by
 $\mathcal{B}^\bullet=\mathcal{B}\otimes_{\mathcal{O}_E}\mathcal{O}_K$,
 Shimura type $\Psi$, and level structure. As in \ref{pro:7.1.5}, it
 admits a model $\Sh^\bullet$ over $\mathcal{O}_{E_v}$.


 Let $\udl{A} \rightarrow \Sh^\bullet$ be the universal abelian
scheme up to prime to $p$ isogeny.  Due to the $\mathcal{O}_K$-action,
the $p$-divisible group of $\udl{A} $ splits as $
\udl{A}[p^\infty]\cong \prod_i \Lambda_{w_i}\times \Lambda_{\ovl{w_i}}$,
where $ \Lambda_{w_i}$ and $\Lambda_{\ovl{w_i}}$ are $p$-divisible groups
of height $4[E_{v_i}:\Q_p]$ with formal multiplication by
$E_{v_i}$. Moreover, $ \Lambda_{w}= \Lambda_{w_0}$ is a special formal
$\mathcal{B}_v$-module of height $4.[E_{v}:\Q_p]$ (defined as in 
\ref{exa:4.3.4}, 
replacing $\Q_p$ by $E_v$), and $ \Lambda_{\ovl{w}}$ is the Serre dual of
$\Lambda_{w}$; the other $ \Lambda_{w_i},\;i>0,$ are etale, and the $
\Lambda_{\ovl{w_i}}$ are their respective Serre duals. Hence the Newton
polygon of the Dieudonn\'e module of $\udl{A}[p^\infty]$ has slopes
$0,\frac{1}{2},1$ (only $\frac{1}{2}$ if $m=0$).

\vspace*{2mm}

\begin{figure}[h]
 \begin{picture}(120,70)(-20,-10)
  \put(-10,0){\line(1,0){110}}
  \put(0,-10){\line(0,1){70}}
  \bezier{10}(60,15)(60,7.5)(60,0)
  \bezier{30}(90,45)(90,22.5)(90,0)
  \put(15,5){\makebox(0,0)[b]{{\tiny $0$}}}
  \put(40,15){\makebox(0,0)[c]{{\tiny $1/2$}}}
  \put(68,32){\makebox(0,0)[c]{{\tiny $1$}}}
  \thicklines
  \put(0,0){\line(1,0){30}}
  \put(30,0){\line(2,1){30}}
  \put(60,15){\line(1,1){30}}
 \end{picture}
 \caption{}
\end{figure}


Let $\mathfrak{v}$ be the discrete valuation ring
$\widehat{\Z^{\mathrm{ur}}}.\mathcal{O}_{E_v}$ as in
\ref{para:7.1.2}. The moduli problem 
for $\mathcal{B}_v$-module of height $4.[E_{v}:\Q_p]$ is representable
by the $p$-adic formal scheme $\displaystyle \coprod_\Z
\;({}_{E_v}\hat\Omega)_{\mathfrak{v}}$, where ${}_{E_v}\hat\Omega$ is
the analogue for (and over) $\mathcal{O}_{E_v}$ of the formal scheme
$\hat\Omega$, with associated analytic space
$(_{E_v}\Omega)_{\C_p}=\P^1_{\C_p}\setminus \P^1(E_v)$, \cf \ref{para:6.3.5}.
\end{para}

\begin{para}\label{para:7.5.3}
 This is the modular way taken by Boutot and Zink to reprove (and
 strengthen) \v{C}erednik's theorem.  As was remarked by
 Varshavsky \cite[3.13]{varshavsky98:_shimur_ii}, one obtains a simpler adelic
 formulation if one works with a twisted version ${}^{\mathrm{ad}}\Sh$ of $\Sh$
 (corresponding to a different normalization of $h_0$ in \ref{para:1.2.4}); this
 does not change the adelic description of the associated complex space
 \begin{equation*}
  {}^{\mathrm{ad}}\Sh_\C^{\mathrm{an}}= C\backslash
   \bigl((\P_\C^1\setminus\P^1(\R)) \times G(\A_f)\bigr)/G(\Q),
 \end{equation*}
 but makes the analogy with the following description of the associated
 $p$-adic space more striking.
 

 Let $\ovl{B}$ be the quaternion algebra over $E$ obtained from $B$ by
 interchanging the invariants at $\infty_0, v$, and let $\ovl{G}$ be the
 $\Q$-algebraic group attached to $\ovl{B}^\times$. Let us identify
 $\ovl{G}(\A^p_f)$ with $G(\A^p_f)$ via an anti-isomorphism
 $\ovl{B}\otimes_E \A^p_f \rightarrow B\otimes_E \A^p_f ,$ and set
 $\ovl{C}=GL_2(E_v)C^p$ viewed as a subgroup of $\ovl{G}(\A_f)$.  Then
 \begin{align*}
  {}^{\mathrm{ad}}\Sh_{\C_p}^{\mathrm{an}} & =C^p \backslash
  \bigl((_{E_v}\Omega)_{\C_p}\times G(\A_f^p)\bigr)/{\ovl{G}}(\Q)\\
  & =\ovl{C}\backslash \bigl((\P^1_{\C_p}\setminus\P^1(E_v))\times
  \ovl{G}(\A_f)\bigr)/{\ovl{G}}(\Q)
 \end{align*}
 where ${\ovl{G}}(\Q)$ acts on $(_{E_v}\Omega)_{\C_p}$ through
 ${\ovl{G}}^{\mathrm{ad}}(\Q_p)\cong PGL_2(E_v)$.  

 Moreover, one can drop the assumption that $C$ is maximal at $p$, on
 replacing $(_{E_v}\Omega)_{\C_p}$ by some finite etale covering as in
 \ref{para:7.4.7}. \cite[3]{tpuosc}, \cite[5]{varshavsky98:_shimur_ii}.
\end{para}

\begin{para}\label{para:7.5.4}
 Rapoport, Zink and Boutot on one hand (by modular methods \`a la
 Drinfeld), and Varshavsky on the other hand (by group-theoretic methods
 \`a la \v{C}erednik), have pointed out similar global
 $p$-adic uniformizations in much more general cases.

 Let us only mention a remarkable example: Mumford's {\it fake
 projective plane} \cite{aaswkak9pq0}. This is a smooth projective complex
 surface $S$ with the same Betti numbers as $\mathbb{P}^2$, but not
 isomorphic to $\mathbb{P}^2$. Actually, it is a surface of general
 type. Mumford's construction is of diadic nature. It is a quotient of
 the two-dimensional generalization $\Omega^{(2)}$ of $\Omega$ by an
 explicit arithmetic group. This $\Omega^{(2)}$ is the complement of the
 lines defined over $\Q_2$ in the projective plane.

 Using the last theorem of \cite{psfpg} or \cite{varshavsky98:_shimur_ii}, one can see
 that $S$ is actually a Shimura surface of PEL type, parametrizing
 polarized abelian varieties of dimension $9$, with multiplication by an
 order in a simple $\Q$-algebra $B$ of dimension $18$ with center
 $\Q(\sqrt{-7})$. The invariants of $B$ at the two primes of
 $\Q(\sqrt{-7})$ above $2$ are $1/3$ and $2/3$ (\cf a recent
 preprint by F. Kato for more detail). The associated group $G$ is a
 group of unitary similitudes of signature $(1,2)$.


 The ``diadic ball'' $\Omega^{(2)}$ (or rather its formal avatar) has an
 modular interpretation for certain $p$-divisible groups (with
 multiplication by $B_2$). These $p$-divisible groups split as a product
 of three $p$-divisible groups of slope $1/3$ and height $3$, and three
 $p$-divisible groups of slope $2/3$ and height $3$.


 The associated Gauss-Manin connection splits into six factors of rank
 $3$ (in two variables). It resembles the Appell-Lauricella connection
 studied in \cite{pdrefapdfhdpv}, \cite{calip}, \cite{fde}, but is different.
\end{para}
