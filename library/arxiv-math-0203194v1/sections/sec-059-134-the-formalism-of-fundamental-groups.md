---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-059-134-the-formalism-of-fundamental-groups
section_title: "The formalism of fundamental groups."
section_number: 13.4
pages: 123-129
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.979
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::1.4}  
 
\begin{para}\label{para::1.4.1} Let $\Cov^\bullet_S$ be a full
 subcategory of $\Cov^{\mathrm{et}}_S$ which is {\it stable under taking
 connected components, fiber products} (over $S$) {\it and quotients}
 (in the sense of \ref{lem::1.2.7}.). Examples:  $\Cov^{\mathrm{et}}_S$,
 $\Cov^{\mathrm{top}}_S$, $\Cov^{\mathrm{alg}}_S$.

 We denote by $F^\bullet_{S,\ovl{s}}=F^\bullet_{\ovl{s}}$ the
 restriction of $F^{\mathrm{et}}_{\ovl{s}}$ to $\Cov^\bullet_S$, and set 

 \begin{equation*}
  \pi_1^{\bullet}(S,\ovl{s}) = \Aut F^\bullet_{\ovl{s}}
 \end{equation*}
 topologized by considering as fundamental
 open neighborhoods of $1$ the stabilizers $\Stab^\bullet_{S',\ovl{s}'}$
 in $\pi_1^{\bullet}(S,\ovl{s})$ of arbitrary geometric points $\ovl{s}'$
 above $\ovl{s}$ in arbitrary \'etale coverings $S'\to S$ in
 $\Cov^\bullet_S\;$ (here we see $\pi_1^{\bullet}(S,\ovl{s})$ as acting
 on the left on   $F^\bullet_{\ovl{s}}(S')$).

 That the topology is indeed compatible with the group law is due to
 the fact that the system of subgroups $\Stab^\bullet_{S',\ovl{s}'}$ is
 stable under intersection (since $\Cov^\bullet_S$ is stable under
 taking fiber products) and under conjugation (which amounts to a change
 of $\ovl{s}'$).

 \medskip In the case $\Cov^\bullet_S = \Cov^{\mathrm{et}}_S,\;
 \pi_1^{\mathrm{et}}(S,\ovl{s})$ is the \'etale fundamental group
 introduced and studied by De Jong \cite{efgonas}.

 In the case $\Cov^\bullet_S = \Cov^{\mathrm{top}}_S,\;
 \pi_1^{\mathrm{top}}(S,\ovl{s})=\pi_1^{\mathrm{top}}(S, s)$ is (an
 incarnation of) the topological fundamental group.

 In the case $\Cov^\bullet_S = \Cov^{\mathrm{alg}}_S,\;
 \pi_1^{\mathrm{alg}}(S,\ovl{s})$ is a profinite group, which will be
 called the {\it algebraic fundamental group}. The theory is embodied in
 \cite[V]{sga1}.
 If $S$ is the analytification of an algebraic smooth
 $K$-variety $S^{\mathrm{alg}}$ and if $\mathrm{char}(K)=0$, then this
 group coincides with Grothendieck's algebraic fundamental 
 group. This follows from the {\it Gabber-L\"utkebohmert theorem},
 according to which the GAGA functor is an equivalence between the
 categories of finite \'etale coverings of $S^{\mathrm{alg}}$ and $S$
 respectively \cite{repfapf}.
\end{para}

\begin{lem}\label{lem::1.4.2} The natural continuous map 
 \begin{equation*}
  \phi: \pi_1^\bullet(S,\ovl{s})\to
  \underset{\Stab^\bullet_{S',\ovl{s}'}}{\limproj} 
  \pi_1^\bullet(S,\ovl{s})/\Stab^\bullet_{S',\ovl{s}'}
 \end{equation*}
 is a homeomorphism. In particular,
 $\pi_1^\bullet(S,\ovl{s})$ is a separated pro-discrete (hence totally
 discontinuous) topological space.
\end{lem}

\begin{proof}
 $\phi$ sends any neighborhood of $\id\in
 \pi_1^\bullet(S,\ovl{s})$ to a neighborhood of $\phi(\id)\in
 im(\phi)$. Since $\phi$ is equivariant with respect to the continuous
 action of $\pi_1^\bullet(S,\ovl{s})$ by left translation, it is open
 onto its image. Hence it suffices to show that it is bijective. Let
 $\underline{\gamma}:=(\gamma_{S',\ovl{s}'})$ be a compatible family of
 elements of $\pi_1^\bullet(S,\ovl{s})/\Stab^\bullet_{S',\ovl{s}'}$, \ie
 represent an element of $\limproj\;
 \pi_1^\bullet(S,\ovl{s})/\Stab^\bullet_{S',\ovl{s}'}$.

 \noindent For any $S'$ in $\Cov^{\bullet}_S$ and any $\ovl{s}'\in
 F^\bullet_{\ovl{s}}(S')$, $\gamma_{S',\ovl{s}'}.\ovl{s}'$ is another
 well-defined element of $F^\bullet(S')$, which we denote by
 $\gamma.\ovl{s}'$. From the compatibility of the
 $\gamma_{S',\ovl{s}'}$'s, it follows that $\gamma$ defines an
 endomorphism of the functor $F^\bullet_{\ovl{s}}$.

 On the other hand, one has a homeomorphism 
 \begin{equation*}
 \inv:\; \limproj\; \pi_1^\bullet(S,\ovl{s}) /\Stab^\bullet_{S',\ovl{s}'}
  \to \limproj\;
  \Stab^\bullet_{S',\ovl{s}'}\backslash\pi_1^\bullet(S,\ovl{s})
 \end{equation*}

 \noindent induced by $g\mapsto g^{-1}$. If we copy the construction
 $\underline{\gamma}\mapsto \gamma$ starting from
 $\inv(\underline{\gamma})$ and using right actions instead of left
 actions, the resulting endomorphism of $F^\bullet_{\ovl{s}}$ is nothing
 but the inverse of $\gamma$. Hence $\gamma$ is an element of $
 \pi_1^\bullet(S,\ovl{s})$, and it is clear that
 $\underline{\gamma}\mapsto \gamma$ is inverse to the natural map
 $\displaystyle\pi_1^\bullet(S,\ovl{s})\to \limproj\; 
 \pi_1^\bullet(S,\ovl{s})/\Stab^\bullet_{S',\ovl{s}'}$.
\end{proof}

\begin{para}\label{para::1.4.3} It is clear from the definitions that 
 $F^\bullet_{\ovl{s}}$ may be enriched to a functor
 \begin{equation*}
  \Cov^\bullet_S \longrightarrow
   \text{$\pi_1^\bullet(S,\ovl{s})$-$\Sets$},\;\;S'\mapsto
   F^\bullet_{\ovl{s}}(S')
 \end{equation*}
 where $\pi_1^\bullet(S,\ovl{s})$-$\Sets$ is the category of discrete
 sets endowed with a continuous 
 left action of $\pi_1^\bullet(S,\ovl{s})$. 
\end{para}

\begin{pro}\label{pro::1.4.4} Up to isomorphism (unique up to composition
 by inner automorphisms), $\pi_1^\bullet(S,\ovl{s})$ does not depend on
 $\ovl{s}$.
\end{pro}
\begin{proof}
 The space
 $\Isom(F^\bullet_{\ovl{s}},F^\bullet_{\ovl{t}})$, non-empty due to
 \ref{lem::1.3.3}, is formally a
 $\pi_1^{\mathrm{et}}(S,\ovl{t})-\pi_1^{\mathrm{et}}(S,\ovl{s})$-bitorsor,
 and the result follows.
\end{proof}

\begin{thm}\label{thm::1.4.5} The enriched functor $F^\bullet_{\ovl{s}}$
\begin{equation*}
 \Cov^\bullet_S \longrightarrow \text{$\pi_1^\bullet(S,\ovl{s})$-$\Sets$}
\end{equation*}
is fully faithful, and extends to an equivalence of categories  

\begin{equation*}
\{\text{disjoint unions of objects of }\Cov^\bullet_S\} \longrightarrow
\text{$\pi_1^\bullet(S,\ovl{s})$-$\Sets$}.
\end{equation*}
Connected coverings correspond to $\pi_1^\bullet(S,\ovl{s})$-orbits.
\end{thm}

\begin{proof}
 (\cf \cite[2.10]{efgonas} in the \'etale case). If
 $f:S'\to S$ is an \'etale covering in $\Cov^\bullet_S$ and
 $\ovl{s}',\;\ovl{s}''$ are elements of $F_{\ovl{s}}(S')$ in the same
 connected component of $S'$, proposition \ref{lem::1.3.3} ensures the existence of
 an \'etale path $\alpha$ from $\ovl{s}'$ to $\ovl{s}''$. Then
 $f_\ast(\alpha)\in \pi_1^{\mathrm{et}}(S,\ovl{s})$, and
 $f_\ast(\alpha).\ovl{s}'=\ovl{s}''$; of course, we may replace here
 $f_\ast(\alpha)$ by its image in $\pi_1^\bullet(S,\ovl{s})$. This shows
 that $\pi_1^\bullet(S,\ovl{s})$-orbits in $F^\bullet_{\ovl{s}}(S')$
 correspond bijectively to connected components of $S'$. In particular

 \begin{equation*}
 F^\bullet_{\ovl{s}}(S') = 
  \pi_1^\bullet(S,\ovl{s})/{\Stab^\bullet_{S',\ovl{s}'}}
 \end{equation*}
 if $S'$ is connected.

 This implies that the enriched functor $F^\bullet_{\ovl{s}}$ is fully
 faithful, because if $S'$ is connected, a morphism between \'etale
 coverings $S'\to S''$ of $S$ may be identified via its graph with a
 connected component $T$ of the \'etale covering $S'\times_S S''$ (which
 belongs to $\Cov^\bullet_S$ by assumption) such that
 $F^\bullet_{\ovl{s}}(T)\xrightarrow{\sim}
 F^\bullet_{\ovl{s}}(S')$ (this can be checked locally on $S$, and this
 reduces to a well-known fact about finite algebraic coverings).

 It remains to show that any $\pi_1^\bullet(S,\ovl{s})$-orbit comes from
 a (connected) \'etale covering. By definition, such an orbit may be
 written $ \pi_1^\bullet(S,\ovl{s})/H$, where $H$ is a subgroup
 containing the stabilizer ${\Stab^\bullet_{S',\ovl{s}'}}$ of some
 geometric point $\ovl{s}'$ above $\ovl{s}$ in some connected \'etale
 covering $S'$ of $S$. As we have seen, the connected components of
 $S'\times_S S'$ correspond bijectively to
 $\pi_1^\bullet(S,\ovl{s})$-orbits in $F^\bullet_{\ovl{s}}(S'\times_S
 S')= F^\bullet_{\ovl{s}}(S')^2.$ The union $R\subset S'\times_S S'$ of
 connected components which corresponds to the union of points
 $(\ovl{s}',\ovl{s}'.h),\;h\in H$, is an equivalence relation on $S'$
 over $S$. By lemma \ref{lem::1.2.7}, the quotient $S''=S'/R$ is an
 \'etale covering 
 of $S$ which belongs to $\Cov^\bullet_S$ by assumption. If $\ovl{s}''$
 denotes the image of $\ovl{s}'$ in $S''$, it is clear that
 $H=\Stab^\bullet_{S'',\ovl{s}''}$.
\end{proof}

\begin{para}\label{para::1.4.6} A connected \'etale covering $S'\to S$ is
 {\it Galois} if $S$ is the quotient $S'/(\Aut_S S')$; $\Aut_S S'$ is
 called the {\it Galois group} of the covering. By \cite[4.1.9]{ecfnas},
 an \'etale Galois covering of $S$ with group $G$ is the same as a
 connected principal homogeneous space under the constant 
 $S$-group $G_S$\footnote{{\it loc.~cit.}  4.1.4, which is used in the proof,
 is available since we are dealing with strictly analytic spaces, \cf
 {\it loc.~cit.} 4.1.5.}.

\noindent Through the dictionary
 of \ref{thm::1.4.5}, a Galois \'etale covering in $\Cov^{\bullet}_S$ 
 corresponds to a surjective continuous 
 homomorphism 

 \begin{equation*}
  \pi_1^\bullet(S,\ovl{s})\to G,
 \end{equation*}
 with $G$ discrete ($\cong \Aut_S S'$). In other words, a (pointed) covering
 $(S',\ovl{s}')$ in $\;\Cov^{\bullet}_S\;$ is Galois if and only if 
 ${\Stab^\bullet_{S',\ovl{s}'}}\subset
 \pi_1^\bullet(S,\ovl{s})$ is normal. 

 Example: the logarithm (\ref{exs::1.2.5}. (i)) is a Galois \'etale covering of
 $(\A^1_{\C_p})^{\mathrm{an}}$ with group $\mu_{p^\infty}\cong \Q_p/\Z_p$. 

The following is also clear:


\end{para}

\begin{cor}\label{cor::1.4.7} $\pi_1^\bullet(S,\ovl{s})$ is a
 pro-discrete group if and only if in $\Cov^\bullet_S$ any 
 connected covering is dominated by a Galois covering.
\end{cor}

\par\noindent {\it Remark}. This property holds in
$\Cov^{\mathrm{top}}_S$ and $\Cov^{\mathrm{alg}}_S$, but not in
$\Cov^{\mathrm{et}}_S$ in general. Let for instance $S=\P^1_{\C_p}$, and
let us consider the Galois covering given by the 
Gross-Hopkins period mapping (II.\ref{para:6.3.3}). According to 
\cite[7.4]{efgonas} 
(using the viewpoint sketched in II.\ref{sub:6.4}), the corresponding
discrete quotient of $\pi_1^{\mathrm{et}}(\P^1,\ovl{s})$ is the composition 

\begin{equation*}
 \pi_1^{\mathrm{et}}(\P^1,\ovl{s})\to SL_2(\Q_p) \to SL_2(\Q_p)/SL_2(\Z_p)
\end{equation*}
where the first map is a continuous surjective homomorphism,
and the quotient topology on $SL_2(\Q_p)$ is non-discrete ({\it
loc.~cit.} p. 116). Since the biggest normal subgroup of $SL_2(\Q_p)$
contained in $SL_2(\Z_p)$ is $\{\pm \id\}$, we see that its preimage in
$\pi_1^{\mathrm{et}}(\P^1,\ovl{s})$ cannot be open. Thus
$\pi_1^{\mathrm{et}}(\P^1,\ovl{s})$ is {\it not a pro-discrete group}.

\begin{cor}\label{cor::1.4.8} Let $\Cov^{\bullet\bullet}_S$ be a full
 subcategory of $\Cov^{\bullet}_S$ stable under taking connected
 components, fiber products (over $S$) and quotients. Then the
 corresponding continuous homomorphism
 $\pi_1^\bullet(S,\ovl{s})\to\pi_1^{\bullet\bullet}(S,\ovl{s})$ has
 dense image (it is neither strict\footnote{recall that a continuous
 homomorphism between topological groups is strict if the induced
 continuous bijective homomorphism between the coimage and the image is
 an isomorphism, i.e. bicontinuous; the coimage is the quotient of the
 source by the kernel, with the quotient topology.} nor surjective in
 general).  \hfill\break In particular, if
 $\;\Cov^{\mathrm{alg}}_S\subset \Cov^{\bullet}_S,\;$ then
 $\;\pi_1^{\mathrm{alg}}(S,\ovl{s})$ is the profinite
 completion\footnote{the profinite completion of a topological group is
 the inverse limit of its quotients by {\it open} normal subgroups of
 finite index.} of $\;\pi_1^\bullet(S,\ovl{s})$. 
\end{cor}

\begin{proof}
 By lemma \ref{lem::1.4.2}, it suffices to prove that for any $S'$ in
 $\Cov^{\bullet\bullet}_S$ and any $\ovl{s}'\in
 F^\bullet_{\ovl{s}}(S')=F^{\bullet\bullet}_{\ovl{s}}(S')$, the natural
 map $\pi_1^\bullet(S,\ovl{s})\to
 \pi_1^{\bullet\bullet}(S,\ovl{s})/\Stab^{\bullet\bullet}_{S',\ovl{s}'}$
 is surjective. We may replace $S'$ by the connected component of
 $s'$. According to the previous theorem,
 $\pi_1^{\bullet\bullet}(S,\ovl{s})/\Stab^{\bullet\bullet}_{S',\ovl{s}'}$
 and $\pi_1^{\bullet}(S,\ovl{s})/\Stab^{\bullet}_{S',\ovl{s}'}$ are then
 identified to
 $F^\bullet_{\ovl{s}}(S')=F^{\bullet\bullet}_{\ovl{s}}(S')$, whence the
 first assertion. The second assertion is clear, since
 $\;\pi_1^{\mathrm{alg}}(S,\ovl{s})$ is profinite.
 
 To see that the image of
 $\;\pi_1^\bullet(S,\ovl{s})\to\pi_1^{\bullet\bullet}(S,\ovl{s})$ is
 neither strict nor surjective in general, it suffices to take $S$ such that
 $\pi_1^{\mathrm{top}}(S,s)$ is infinite (\eg a Tate curve). Then
 $\pi_1^{\mathrm{et}}(S,\ovl{s})\to\pi_1^{\mathrm{alg}}(S,\ovl{s})$ is
 neither surjective nor strict. This follows from the commutative square 
 of topological groups
 \begin{equation*}
 \begin{CD}
  \pi_1^{\mathrm{et}}(S,\ovl{s}) @>>> \pi_1^{\mathrm{alg}}(S,\ovl{t})\\
  @VVV @VVV\\
  \pi_1^{\mathrm{top}}(S,s) @>>> \widehat{\pi_1^{\mathrm{top}}(S,t)}
 \end{CD}
 \end{equation*} 
 where the roof denotes the profinite completion; the coimage (\resp
 image) of the ``south-east map''
 $\pi_1^{\mathrm{top}} (S,\ovl{s}) \to  \widehat{\pi_1^{\mathrm{top}}(S,
 t)}$ is infinite discrete (\resp compact).
\end{proof}

\medskip In this context, the following general lemma is useful:

\begin{lem}\label{lem::1.4.9} Let $G, H$ be separated topological groups
 such that any neighborhood of $1$ contains an open 
 subgroup, and let $f: G\to H$ be a continuous homomorphism.
 \begin{enumerate}
  \item If the induced functor 
	$f^\ast:\,\text{$H$-$\Sets$}\to G$-$\Sets$ is essentially
	surjective, then $f$ is injective.
  \item If $f^\ast:\,H$-$\Sets \to G$-$\Sets$ is an equivalence, then $f$ is
	injective, strict and has dense image.
  \item If $f^\ast:\,H$-$\Sets\to G$-$\Sets$ is an equivalence and $G=
	\limproj G/U$ (the limit running over open subgroups of $G$),
	then $f$ is an isomorphism.
  \item If $G$ is complete and if the normal open subgroups are cofinal
	among the open subgroups $U$, then $G=\limproj G/U$.
 \end{enumerate}
\end{lem}
  
\begin{proof}
 (i) otherwise, let $g\neq 1$ be in the kernel of $f$. Because $G$ is
 separated, there exists a neighborhood $U$ of $1$ not containing $g$,
 and by hypothesis, one may assume that $U$ is an open subgroup of
 $G$. By assumption the (connected) $G$-set $G/U$ corresponds via
 $f^\ast$ to a (connected) $H$-set $X$. Since $f(g)=1$, $g$ acts 
 trivially on $f^\ast(X)$, in contradiction with the fact that $g\notin U$.

 (ii) To show that $f$ has dense image, it suffices to show that for $h\in
 H$ and any neighborhood $V$ of $1$, $f(G).h \cap V\neq \emptyset$. By
 hypothesis, one may assume that $V$ is an open 
 subgroup of $H$. Thus one has to show that $H=G.V$ for 
 any open subgroup $V$ of $H$, \ie $G$ acts transitively on $H/V$. If the
 action is not transitive, $f^{\ast}(H/V)$ can be 
 written as a disjoint union of $G$-sets, which contradicts the
 the assumption that $f^{\ast}$ is an equivalence. 

 \noindent It remains to show that $f$ is strict. But we have seen that
 $f^\ast$ induces an equivalence on transitive sets. 
 Therefore $f^{-1}$ induces a bijection between open subgroups of $H$
 and open subgroups of $G$, whence the result.

 (iii) Indeed one has a commutative diagram
 \begin{equation*}
 \begin{CD}
  G @>\subset>> H\\
  @V\wr VV @VVV \\
 \limproj G/U @>\sim>> \limproj H/V
 \end{CD}
 \end{equation*}
 and the right vertical map is injective since $H$ is separated.

 (iv) follows from \cite[III.7.2, prop. 2]{bourbaki74:_topol}.
\end{proof}

\begin{para}\label{para::1.4.10} Let $f:T\to S$ be any morphism of connected
 $K$-manifolds. We have the natural functor 

\begin{equation*}
 \Cov^{\mathrm{et}}_S\to \Cov^{\mathrm{et}}_T:\;\; S'\mapsto S'\times_S T.
\end{equation*}
Let us {\it assume} that it induces a functor 

\begin{equation*}
 f^{\bullet\ast}: \Cov^\bullet_S\to \Cov^\bullet_T.
\end{equation*}
Since
$F^\ast_{S,\ovl{s}}=F^\ast_{T,\ovl{t}}\circ f^{\bullet\ast}$ if
$\ovl{s}=f(\ovl{t})$, this gives rise to a continuous homomorphism

\begin{equation*}
f^\bullet_\ast :\pi_1^\bullet(T,\,\ovl{t})\to
 \pi_1^\bullet(S,\,\ovl{s}=f(\ovl{t})).
\end{equation*}
\end{para}

\begin{cor}\label{cor::1.4.11} $f^\bullet_\ast$ is an isomorphism of
 topological groups if and only if $f^{\bullet\ast}$ 
 is an equivalence of categories. 
\end{cor}

\begin{proof}
 If $f^\bullet_\ast$ is an isomorphism, it induces an equivalence 
 $\pi_1^\bullet(S,\,\ovl{s})$-$\Sets\cong
 \pi_1^\bullet(T,\,\ovl{t})$-$\Sets$, and it follows from \ref{thm::1.4.5} that
 $f^{\bullet\ast}$ is an equivalence of categories. The other
 implication is immediate.
\end{proof}

\begin{cor}\label{cor::1.4.12} Assume that $f$ is an \'etale covering in
 $\Cov^\bullet_S$, thus corresponding to the 
 $\pi_1^\bullet(S,\,\ovl{s})$-orbit
 $\pi_1^\bullet(S,\,\ovl{s})/\Stab^\bullet_{T,\ovl{t}}$ through the 
 dictionary of \ref{thm::1.4.5}.
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}

  \item Then $\Stab^\bullet_{T,\ovl{t}}$ is the closure of the image of
	$f^\bullet_\ast$.  In particular, if $f$ is a Galois covering,
	its Galois group is
	$\;\pi_1^\bullet(S,\,\ovl{s})/(\Im\,f^\bullet_\ast)^-$.
  \item Assume moreover that for any covering $T'\to T$ in
	$\Cov^\bullet_T$, the composition with $f$ gives rise to a
	covering $T'\to S$ in $\Cov^\bullet_S$. Then $f^\bullet_\ast$
	is open and injective (hence $\;\pi_1^\bullet(T,\,\ovl{t})$ may
	be identified with the open and closed subgroup
	$\Stab^\bullet_{T,\ovl{t}}$ of $\pi_1^\bullet(S,\,\ovl{s})$).  
 \end{enumerate}
\end{cor}
\begin{proof}
 (a) Looking at the natural identifications 
 \begin{equation*}
 \pi_1^\bullet(S,\,\ovl{s})/\Stab^\bullet_{T,\ovl{t}}\cong
 F^\bullet_{\ovl{s}}(T)\cong F^\bullet_{\ovl{t},\ovl{t}}(T\times_S \,T)
 \end{equation*}
 of $\pi_1^\bullet(S,\,\ovl{s})$-orbits. The connected component of
 $T\times_S \,T$ containing $(\ovl{t},\ovl{t})$ is the 
 diagonal $T\subset T\times_S \,T$, therefore the
 $\pi_1^\bullet(T,\,\ovl{t})$-orbit is reduced to the point
 $(\ovl{t},\ovl{t})$. This shows that $\Im f^\bullet_\ast$ lies in
 $\Stab^\bullet_{T,\ovl{t}}$.

 To show that it is dense, we have to show that for any connected $S'$ in
 $\Cov^\bullet_S$ and any geometric point $\ovl{s}'$ of $S'$ above
 $\ovl{s}$, the map $\pi_1^\bullet(T,\,\ovl{t})\to
 \pi_1^\bullet(S,\,\ovl{s})/\Stab^\bullet_{T,\ovl{t}}$ induced by
 $f^\bullet_\ast $ is surjective. This follows from \ref{thm::1.4.5} as
 in \ref{cor::1.4.8}.

 (b) Under the extra assumption, one has functors $\Cov^\bullet_T\to
 \Cov^\bullet_S\to \Cov^\bullet_T: T'/T\mapsto T'/S ;\;S'/S\mapsto
 (S'\times_S \,T)/T$.

 \noindent For any open subgroup $H\subset  \pi_1^\bullet(T,\,\ovl{t})$
 (corresponding as in \ref{thm::1.4.5} to a pointed connected covering
 $(T',\ovl{t}')\;$), $\pi_1^\bullet(T,\,\ovl{t})/H\cong
 F^\bullet_{\ovl{t}' }(T' )$ is a subset of $
 F^\bullet_{\ovl{t}',\ovl{t}}(T'\times_S\,T)\cong 
 F^\bullet_{\ovl{s}}(T')\cong
 \pi_1^\bullet(S,\,\ovl{s})/\Stab^\bullet_{T',\ovl{t}'}$.
 In other words, $f^\bullet_\ast $ induces an open injective homomorphism 
 \begin{equation*}
 \pi_1^\bullet(T,\,\ovl{t})/H \hookrightarrow
 \pi_1^\bullet(S,\,\ovl{s})/f^\bullet_\ast(H).
 \end{equation*}
 Indeed, $f^\bullet_\ast(H)=\Stab^\bullet_{T',\ovl{t}'} $ is open in
 $\pi_1^\bullet(S,\,\ovl{s}) $: such groups correspond to connected
 coverings of $S$ which dominate $T$ (\ie which factorize over $f$).
 Since such coverings are cofinal in 
 $\Cov^\bullet_S$, we can pass to the limit, using \ref{lem::1.4.2}: 

 \begin{equation*}
 \pi_1^\bullet(T,\,\ovl{t}) = \limproj \pi_1^\bullet(T,\,\ovl{t})/H
 \hookrightarrow \limproj \pi_1^\bullet(S,\,\ovl{s}) /f^\bullet_\ast(H)
 \cong \pi_1^\bullet(S,\,\ovl{s})
 \end{equation*}
 and conclude that $f^\bullet_\ast$ is an open injective homomorphism.
\end{proof}
