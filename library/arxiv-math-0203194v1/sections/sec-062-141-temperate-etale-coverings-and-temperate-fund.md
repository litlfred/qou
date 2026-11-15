---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-062-141-temperate-etale-coverings-and-temperate-fund
section_title: "Temperate 'etale coverings and temperate fundamental groups."
section_number: 14.1
pages: 130-137
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.979
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::2.1}

\medskip In the archimedean context, the categories
$\Cov^{\mathrm{et}}_S$ and $\Cov^{\mathrm{top}}_S$ coincide; in the
non-archimedean situation, in contrast, $\Cov^{\mathrm{top}}_S$ is ``too
small'' (for instance, it consists of disjoint unions of copies of $S$
if $S$ has dimension one and tree-like reduction, \eg if $S$ is an
annulus), while  $\Cov^{\mathrm{et}}_S$ is ``too big'' (for $S=\P^1$, it
contains many non-trivial objects).

We introduce an intermediate category, which seems to be a closer
analogue of the category of unramified coverings in the 
archimedean context.
 
\begin{dfn}\label{def::2.1.1} An \'etale covering $S'\to S$ is {\rm
 temperate} if it is a quotient\footnote{in the sense of
 \ref{lem::1.2.7}.} of a 
 composite \'etale covering $T'\to T\to S$, where $T'\to T$ is a
 (possibly infinite) topological covering, and $T\to S$ is a finite
 \'etale covering.
\end{dfn}

Hence we have the commutative square 
\begin{equation*}
 \begin{matrix}
  &&T'&&\\
  & \swarrow &&\searrow &\\
  T&&&&S'\\
  &\searrow && \swarrow &\\
  &&S&&
 \end{matrix}
\end{equation*}
with $T'\in \Cov^{\mathrm{top}}_{T},\;T\in \Cov^{\mathrm{alg}}_{S},
S'\in \Cov^{\mathrm{et}}_S$. 

\medskip\noindent {\it Remark}. The notion of temperate covering is
stable under base change as in \ref{para::1.4.10}. 
 
\begin{lem}\label{lem::2.1.2} Let $T\to S$ be a finite Galois \'etale
 covering, and let $\tilde T\to T$ be the universal topological covering
 of $T$. Then the composite $\tilde T \to S$ is a Galois temperate
 covering. 
\end{lem}

\begin{proof}
 From \ref{lem::1.2.4}, we know that it is an \'etale covering, automatically
 temperate. It remains to show that it is Galois. By the universal
 property of $\tilde T$, any automorphism of $T$ lifts to $\tilde T$,
 hence there is an exact sequence of discrete groups:
 \begin{equation*}
 1\to \bigl(\pi_1^{\mathrm{top}}(T,t) \cong\bigr)\; \Aut_T \tilde T \to
 \Aut_S \tilde T \to \Aut_S\,  T\to 1. 
 \end{equation*}
 Since $\tilde T/(\Aut_T \tilde T) =T$ and $T/(\Aut_S T)=S,$ it
 follows that $ \tilde T/(\Aut_S \tilde T)=S$.
\end{proof}


We see from the lemma that in the definition of a temperate
covering, we may assume that $T'\to S$ and $T'\to T$ are Galois.  

\begin{rems}
 (i) It is {\it not true} that any quotient of a tower $T'\to T\to S$
 as in definition \ref{def::2.1.1} is again of this form. As a
 counter-example, let us consider a Tate elliptic curve $E$ over
 $K=\C_p$, and set $T= E\setminus E[2]$ (2-torsion points
 removed). Then $\tilde T $ is $\G_m^{\mathrm{an}}$ deprived from
 the countable subgroup $\pm (\sqrt q)^\Z$, and $T\cong \tilde
 T/q^\Z $. The inversion $x\mapsto 1/x$ on $\tilde T$ induces the
 inversion on $E$, and $\G_m/\{\id, \inv\}=\A^1 \;$ (via $x\mapsto
 x+1/x),\;E/\{\id,\inv\}=\P^1$. Let us consider the infinite
 temperate covering 

 \begin{equation*}
  S'=\tilde{T}/\{\id, \inv\} \to S= T/\{\id, \inv\}
   =\P^1\setminus\{0,1,\lambda,\infty\}.
 \end{equation*}
 Then $S'$ is not a topological covering of any finite \'etale
 covering $S''$ of $S$. Indeed, otherwise $\tilde T$ would be the
 universal topological covering of some connected component $T'$
 of $T\times_S S''$. The tower $\tilde T\to T' \to T$ would then
 extend to a tower of topological coverings $\G_m^{\mathrm{an}}\to
 E'\to E$, where $E'$ is another Tate curve isogenous to $E$ (we
 use the fact that the topological fundamental group of $T'$ and
 $E$ is the same). Then $S''\subset E'/\{\id, \inv\}\cong
 \P^1$. But any open subset in $\P^1_{\C_p}$ is simply-connected,
 whence $\tilde T= S''$, a contradiction.
 
 \noindent This example also shows that {\it a temperate covering may
 become a topological covering after finite \'etale base change, without
 being itself a topological covering}.

 (ii) The notion of temperate covering is not local on $S$. In fact,
 the Gross-Hopkins \'etale covering of
 $(\P^1_{\C_p})^{\mathrm{an}}$ is not temperate, although there is
 a finite open cover $(U_i)$ of $(\P^1_{\C_p})^{\mathrm{an}}$ such
 that it becomes a disjoint union of finite \'etale coverings over
 each $U_i$ (by compactness).
\end{rems}

\begin{para}\label{para::2.1.3} We denote the category of temperate
 (\'etale) coverings of $S$ by $\Cov^{\mathrm{temp}}_S$. 
 From the fact that topological and finite \'etale coverings
 respectively are stable under taking connected components and fiber
 products, it is not difficult to see that $\Cov^{\mathrm{temp}}_S$ is
 stable under taking connected components and fiber products (over
 $S$). By definition, it is stable under taking quotients. 
 
\medskip According to the results of 1.4, there is thus defined a
 separated totally discontinuous group, the {\it temperate fundamental group}
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$, which does not depend on the
 geometric point $\ovl{s}$ up to isomorphism. Moreover:
\end{para}

\begin{lem}\label{lem::2.1.4} $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is a
 pro-discrete group (hence complete, 
\cf \cite[III. 57.7]{bourbaki74:_topol}).  A basis of open neighborhoods of
$1$ is given by normal closed subgroups $H$ such that
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})/H$ is the Galois group of the
 universal topological covering of some finite \'etale Galois covering of $S$.
\end{lem}
\begin{proof}
 This follows from \ref{cor::1.4.7}. and \ref{lem::2.1.2} (connected
 temperate coverings admit a Galois closure).
\end{proof}

 \medskip 
 The inclusion $\; \Cov^{\mathrm{top}}_S \hookrightarrow
 \Cov^{\mathrm{temp}}_S$ gives rise to a {\it surjective} homomorphism 
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(S,\ovl{s}) \to \pi_1^{\mathrm{top}}(S,s) 
 \end{equation*} 
 (\cf \ref{cor::1.4.8}, taking
 into account the discreteness of $\pi_1^{\mathrm{top}}(S,s) $), which
 shows that $\pi_1^{\mathrm{temp}}(S,\ovl{s})$, although not a discrete 
 group, has many {\it infinite discrete quotients} in general; we say
 that $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is ``lacunary''.

 \medskip On the other hand, the inclusion $\; \Cov^{\mathrm{alg}}_S
 \hookrightarrow  \Cov^{\mathrm{temp}}_S$ gives rise to a 
 continuous homomorphism with dense image
 \begin{equation*}
  \pi_1^{\mathrm{temp}}(S,\ovl{s})\to \pi_1^{\mathrm{alg}}(S,\ovl{s}),
 \end{equation*}
 and $ \pi_1^{\mathrm{alg}}(S,\ovl{s}) $ may be identified with the
 profinite completion of $\pi_1^{\mathrm{temp}}(S,\ovl{s})$. This shows
 that $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is not ``too small'' (as opposed
 to $\pi_1^{\mathrm{top}}(S,s) $), and the following two propositions
 show that it is not ``too big'' as well (as opposed to
 $\pi_1^{\mathrm{et}}(S,\ovl{s}) $): 
 
\begin{pro}\label{pro::2.1.5} If $\dim\,S=1$, the homomorphism
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})\to \pi_1^{\mathrm{alg}}(S,\ovl{s}) $
 is injective. 
\end{pro}

\begin{proof}
 By \ref{lem::2.1.2} and \ref{lem::2.1.4}, it suffices to see that if
 $T\to S$ is a finite 
 Galois \'etale covering, the Galois group of the temperate covering
 $\tilde T\to S$ is residually finite. But this group contains
 $\pi_1^{\mathrm{top}}(T,t)$ as a normal subgroup of finite index. The
 point is that in dimension one, topological fundamental groups are free,
 hence residually finite.
\end{proof}

\medskip The lacunary subgroup
$\pi_1^{\mathrm{temp}}(\P^1_{\C_p}\setminus \{0,1,\infty\})$ of the
profinite free group on two generators
$\pi_1^{\mathrm{alg}}(\P^1_{\C_p}\setminus \{0,1,\infty\})$ is
especially interesting and mysterious, and will be the 
object of our investigations in later sections\footnote{recall, on the
other hand, that $\pi_1^{\mathrm{top}}(\P^1_{\C_p}\setminus
\{0,1,\infty\})$ is trivial.}.

\begin{pro}\label{pro::2.1.6} If $S$ is algebraic and $K$ of
 characteristic zero, the Galois group of any Galois temperate 
 covering of $S$ is finitely generated. Moreover, 
 if $K$ has only countably many finite 
 extensions in a fixed algebraic closure $\ovl{K}$ (\eg if $K$ is a 
 $p$-adic field), then 
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ and all its quotients by closed
 normal subgroups are `polish', \ie metrizable of countable type and
 complete.
\end{pro}

\begin{proof}
 Let us consider the first assertion. By \ref{lem::2.1.2}, it suffices to
 treat the case of the universal topological covering of a finite Galois
 \'etale covering.  By the already mentioned Gabber-L\"utkebohmert
 theorem, that finite \'etale covering is algebraic. The Galois group
 admits as a normal subgroup of finite index the topological fundamental
 group of that finite \'etale covering, which is finitely generated 
 (\cf \ref{para::1.1.2}); whence the result.

 \noindent Since $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is separated, its
 metrizability is equivalent to the existence of a countable fundamental
 system of neighborhood of $1$ \cite[IX.3.1 prop. 1]{bourbaki74:_topol}.
 By \ref{lem::2.1.4}, it 
 suffices to see that there are countably many finite \'etale coverings
 of $S$, 


 which follows, by d\'evissage, from the assumption that
 $\Gal(\ovl{K}/K)$ has countably many open subgroups, and from the
 topological finite generation of the algebraic fundamental group over
 $\ovl{K}$.
 This also shows that
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is not only a pro-discrete group
 (which already implies that it is complete), but even a countable
 inverse limit of discrete countable groups. It follows that the
 metrizable group $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ admits a 
 countable dense subset, hence its topology has a countable basis 
 \cite[IX.2.8 prop. 12]{bourbaki74:_topol}.

 \noindent It follows that any closed subgroup of
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ and any quotient of
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ by a 
 closed normal subgroup is metrizable and complete 
 \cite[IX.3.1 prop. 4]{bourbaki74:_topol}, 
 and of countable type (for a quotient: because it 
 has a countable dense subset).
\end{proof}

Notice however that the first assertion does not imply that
$\pi_1^{\mathrm{temp}}(S,\ovl{s})$ is topologically finitely generated. 
On the other hand, we shall show below that it is not locally compact in
general (\ref{pro::2.3.12}).

\begin{pro}\label{pro::2.1.7} Let $f: T\to S$ be an \'etale finite Galois
 covering of a connected $K$-manifold with group $G$, and $\ovl{t}$ be a
 geometric point of $T$. Then there is an exact sequence 
 \begin{equation*}
  1\to \pi_1^{\mathrm{temp}}(T,\ovl{t})\to
 \pi_1^{\mathrm{temp}}(S,f(\ovl{t}))\to G\to 1. 
 \end{equation*}
\end{pro}

\begin{proof}
 It is clear from the definition \ref{def::2.1.1} that any temperate covering
 of $T$ gives rise, by composition with $f$, to a 
 temperate covering of $S$. Thus the proposition follows from
 \ref{cor::1.4.12}.b.
\end{proof}

\medskip\noindent {\it Remark.} We shall see below (\ref{para::2.3.3})
that on the 
other hand, an \'etale covering of $S$ which is a finite \'etale
covering of a topological covering is not necessarily temperate.

\medskip The following result is an important criterion to recognize
topological, \resp temperate, \resp locally algebraic coverings: 

\begin{thm}\label{thm::2.1.8} Let $S'$ be a Galois \'etale covering of
 $S$ with group $G$. Then
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}

  \item if $G$ is torsion-free,
	$S'$ is a topological covering of $S$;
  \item if $G$ is virtually torsion-free, $S'$ is a temperate covering
	of $S$; more precisely, $S'$ is a topological covering of some
	finite \'etale Galois covering of $S$;
  \item assume that $S$ is countable at infinity; then $S'$ is a locally
	algebraic covering of $S$ if and only if $G$ is the union of an
	increasing sequence of finite subgroups.
 \end{enumerate}
\end{thm}

\begin{proof}
 (a) (\cf also \cite{efgonas}) Let
 $\rho:\;\pi_1^{\mathrm{et}}(S,\ovl{s}) \to G$ be the 
 continuous homomorphism corresponding $S'\to S$. Let $\ovl{t}$ 
 be another geometric point of $S$, and let $\ovl{\gamma}$ be an \'etale
 path from $\ovl{t}$ to $\ovl{s}$.  Under the composed continuous homomorphism
 \begin{equation*}
  \pi_1^{\mathrm{et}}(t,\ovl{t})\to \pi_1^{\mathrm{et}}(S,\ovl{t})
   \xrightarrow{\mathrm{ad}(\ovl{\gamma})}\pi_1^{\mathrm{et}}(S,\ovl{s})\to G  
 \end{equation*}
 the compact (profinite) group $\pi_1^{\mathrm{et}}(t,\ovl{t})\cong
 \Gal(\mathscr{H}(t)^{sep}/\mathscr{H}(t))$ is sent to 
 $1$ if $G$ is torsion-free. This means that for any $\ovl{t}'\in
 F_{\ovl{t}}(S')$,  
 $\mathscr{H}(t')=\mathscr{H}(t)$. Let $U$ be an open neighborhood of $t$
 (which we may assume to be contractible thanks to Berkovich's theorem),
 such that $S'\times_S U\cong \coprod V_j$, with $V_j$ finite \'etale
 over $U$. Since $\mathscr{H}(t')=\mathscr{H}(t)$ for any point $t'$ in
 $V_j$ above $t$, it follows from \ref{para::1.2.1} that
 $V_j$ is a topological covering of
 the contractible open set $U$, hence a disjoint union of finitely many
 copies of $U$. This holds 
 for any point $t\in S$, therefore $S'\to S$ is a topological covering. 

 (b) If $G$ is virtually torsion-free, let $N$ be a torsion-free normal
 subgroup of finite index, and let $S'\to T\to S$ 
 be the corresponding intermediate Galois covering. By $a)$, $S'\to T$ is
 a topological covering, hence $S'\to S$ is a temperate \'etale covering.

 (c) Assume that $S'$ corresponds to a principal homogeneous space under
 $G_S$, classified by an element of $\mathrm{H}^1(S,G)$. Let us write
 $S=\bigcup S_j$, with $S_j$ compact. Assume that $G=\bigcup G_k$, with
 $G_k$ finite. Then $\mathrm{H}^1(S_j,G)= \liminj \mathrm{H}^1(S_j, G_k)$, therefore the
 restriction of $S'$ to any $S_j$ is a disjoint union of finite \'etale
 coverings of $S_j$, hence 
 $S'\to S$ is locally algebraic. Conversely, if $S'\to S$ is Galois
 locally algebraic, its group $G$ is a discrete image of $\liminj
 \pi_1^{\mathrm{alg}}(S_j,\ovl{s})$, each
 $G_j:=\Im(\pi_1^{\mathrm{alg}}(S_j,\ovl{s}))$ is finite, and $G=\bigcup
 G_j$.
\end{proof}  

\begin{cor}\label{cor::2.1.9} In dimension one, $
 \pi_1^{\mathrm{temp}}(S,\ovl{s})$ is the pro-VTFD-completion of
 $\pi_1^{\mathrm{et}}(S,\ovl{s})$. 
\end{cor}

By pro-VTFD-completion of a topological group $\Gamma$, we mean the
inverse limit of its virtually torsion-free discrete quotients. This is
a filtered limit (if $\Gamma/H'$ and $\Gamma/H''$ are VTFD, so is
$\Gamma/(H'\cap H'')\;$). Pro-VTFD-completions are functorial (due to
the fact that any subgroup of a VTF group is VTF).

\begin{proof}
 By \ref{lem::2.1.2}, the coverings of the form $\tilde T\to T \to S$, with $T$
 finite \'etale Galois over $S$, are cofinal among temperate
 coverings. In dimension one, we have seen that the Galois groups of such
 Galois coverings are virtually torsion-free, whence the result (using
 \ref{para::1.3.2}).
\end{proof}

\medskip\noindent {\it Examples.} (i) It follows from \ref{cor::2.1.9}
that the logarithmic (locally algebraic) covering
\begin{equation*}
\log:\; \matheur{D}_{\C_p}(1,1^-)\longrightarrow  \A^1_{\C_p} 
\end{equation*}
of the affine line is {\it not }temperate, since its Galois group
$\Q_p/\Z_p$ has no non-trivial virtually torsion-free 
quotient. This also follows from \ref{pro::2.1.5}, since
$\pi_1^{\mathrm{alg}}(\A^1_{\C_p})=0$. 

\medskip\noindent {\it Remark.} It is easy to draw from \ref{thm::2.1.8} that a
connected \'etale covering which is both temperate 
and locally algebraic is (finite) algebraic.

\medskip \noindent (ii) It also follows from \ref{thm::2.1.8} that there is no
\'etale Galois covering of the punctured disk with Galois group
$\Z$. This fact has noteworthy consequences on the local monodromy of
$p$-adic differential equations (\cf next sections).

{\small
\medskip\noindent {\it Remark.} In \cite{poaptg}, we have limited
ourselves to temperate coverings for which the tower $T'\to T\to S$ 
occuring in definition \ref{def::2.1.1} is Galois with VTF group. The
fundamental attached to the category of such coverings is 
then the pro-VTFD-completion of $\pi_1^{\mathrm{et}}(S,\ovl{s})$. The
definition \ref{def::2.1.1} seems however more natural (and is much more 
general in higher dimension). In \cite{poaptg}, another topological
group is introduced, namely the coimage of 
$\pi_1^{\mathrm{et}}(S,\ovl{s})\to \pi_1^{\mathrm{top}}(S,\ovl{s})\times
\pi_1^{\mathrm{alg}}(S,\ovl{s})$, denoted by
$\pi_1^{\mathrm{red}}(S,\ovl{s})$. In dimension one, there is a continuous
injective homomorphism with dense image $\pi_1^{\mathrm{red}}(S,\ovl{s})\to
\pi_1^{\mathrm{temp}}(S,\ovl{s})$, but it not clear whether this is an
isomorphism (the question is the openness of 
$\pi_1^{\mathrm{et}}(S,\ovl{s})\to 
\pi_1^{\mathrm{temp}}(S,\ovl{s})$).
}

























\begin{thm}\label{thm::2.1.10} Assume that $K$ is algebraically closed
 of characteristic zero. Let $\ovl{S}$ be  
 a (paracompact strictly) {\rm normal} connected $K$-analytic space
 $\ovl{S}$, and let $Z$ be a closed analytic subset such 
 that $S:=\ovl{S}\setminus Z$ is smooth.
 Assume that for any point $s$ of $\ovl{S}$, there is a covering (in the
 sense of \ref{def::1.2.3}) from a $K$-manifold 
 onto a neighborhood $U(s)$ of $s$ which is \'etale above $U(s)\cap S$. 

 \noindent
 Then any temperate \'etale covering $S'\to S $ extends to
 a (possibly ramified) covering  
 $\ovl{S}'\to \ovl{S}$, in the sense of \ref{def::1.2.3}: any point $x$
 has an open neighborhood $U(x)$ such that $S'\times_S U(x)$ 
 is a disjoint union of finite (ramified) coverings $V_j$ of
 $U(x)$. Moreover, one may assume that the $V_j$ are normal; 
 such an extension
 $\ovl{S}'\to \ovl{S}$ is then unique. 

 Furthermore, if $Z$ has codimension $\geq 2$ and $\ovl{S}$
 is smooth, any temperate
 \'etale covering $S'\to S $ extends to a unique temperate covering
 $\ovl{S}'\to \ovl{S}$.
\end{thm}

\begin{proof}
 We start with the statement about unicity. Since it is local on
 $\ovl{S}$, it is enough to establish it in the case of finite coverings
 (by definition \ref{def::1.2.3}). Let $\ovl{S}'$ and $\ovl{S}''$ be two
 connected 
 finite coverings of $\ovl{S}$ which coincide over $S$. The diagonal
 $\Delta$ is a connected component of $S'\times_S S''$. Its closure
 $\ovl{\Delta} $ in the normalization of $\ovl{S}'\times_{\ovl{S}}
 \ovl{S}''$ is again a connected component (using \cite[3.3.16]{spasalc}).
 The projections $\ovl{\Delta} \to \ovl{S}',\;\ovl{\Delta} \to
 \ovl{S}''$ are finite, and their restrictions to $\Delta$ are
 isomorphisms; hence they are themselves isomorphisms if $\ovl{S}'$ and
 $\ovl{S}''$ are normal.

 Let us turn to the existence of the extension (with the normality
 property). By unicity, this is a local question; we may and shall
 assume that $Z$ is a hypersurface, and that 
 $\ovl{S}$ is (strictly) affinoid, and that there exists a finite
 covering $\ovl{T}\to \ovl{S}$ by a 
 rigid-analytically smooth affinoid $\ovl{T}$, which restricts to a finite
 \'etale covering $T\to S$. 

 Let us first show that any quotient of a temperate covering $S'\to S$
 which has the extension property inherits this extension property: by
 unicity, the question is again local on $\ovl{S}$; by definition of
 coverings, this reduces the question to the case when $S'\to S$ is
 finite. By glueing (\cf \cite[1.3.3]{ecfnas}), it is again enough to treat
 the affinoid (normal) case. The argument is similar to the above one
 for unicity and left to the reader.
 
 This remark allows us to assume that $S'\to S$ is a topological covering of a
 finite \'etale covering of $S$. 
 Let us first treat the case of a finite \'etale covering. In this
 case, the extension property is proved in Gabber-L\"utkebohmert 
 \cite{repfapf}.
\end{proof}

The crucial case is the case of a punctured disk $S=\matheur{D}^{\ast}$
which is worth stating separately:

\begin{lem}[Gabber, L\"utkebohmert]\label{lem::2.1.11} Any finite
 \'etale covering of $\matheur{D}^\ast$ becomes a finite disjoint union
 of Kummer coverings on a smaller concentric punctured disk.
\end{lem}
\noindent (Here the assumption that $K$ is of characteristic zero is
essential). From there, one draws the extension property, in the product
case, when $\ovl{S}$ is a polydisk and $Z$ a union of axes (\cf {\it
loc.~cit.}, 3.3). By Kiehl's theorem on the existence of tubular
neighborhoods \cite{kiehl67:_rham_kohom_mannig_koerp}, the statement
also holds if $Z$ is a strict 
normal crossing divisor in $\ovl{S}$. In the general case, one can
invoke embedded resolution for $Z$, \cf \cite{schoutens99:_embed} (note that 
\cite[\S 4]{repfapf} proposes an alternative strategy which uses embedded
resolution only in dimension $2$).
 
It remains to deal at last with the case of a topological covering
$S'\to S$.  In order to avoid problems of singularities, we consider a finite 
etale covering $T\to S$ as above, $T$ being a rigid-analytically 
smooth affinoid.  It will be more convenient to replace $S'$ by 
$S'\times_S T$ (of which $S'$ is a quotient) so that the new $S'$ is 
a topological covering of $T$ 
itself a finite \'etale covering of $S$.
By \ref{pro::1.1.3}, $S'$ extends to a topological covering $\ovl{S}'
\to\ovl{T}$, and composition with $\ovl{T}\to \ovl{S}$ provides the 
desired extension of $S'/S$ to a covering $\ovl{S}'/\ovl{S}$.
 
The last statement of the theorem follows from the Nagata-Zariski purity
theorem (which becomes easy in the case of a finite morphism of
one-dimensional affinoids).

\medskip\noindent {\it Remark.} This extension property of temperate
coverings does not hold for arbitrary \'etale coverings. 

\noindent Indeed, one can show that the logarithmic covering of the
affine line does not extend to a (ramified) covering 
of the projective line.

\medskip The previous theorem is completed by the following result,
which is proven as in the complex case \cite[exp. XII, 5.3]{sga1}:

\begin{pro}\label{pro::2.1.12} Let $\ovl{S}$ be a normal analytic space,
 and let $Z$ be a closed analytic subset such that $S:=\ovl{S}\setminus
 Z$ is dense in $\ovl{S}$. Then the functor which attaches to any finite
 normal covering of $\ovl{S}$ its restriction to $S$ is fully faithful.
\end{pro}

It follows that in \ref{thm::2.1.10}, the extension of coverings from temperate
coverings of $S$ to `normal' coverings of $\ovl{S}$ `is' a fully
faithful functor.
