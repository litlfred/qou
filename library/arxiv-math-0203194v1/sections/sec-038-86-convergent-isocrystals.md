---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-038-86-convergent-isocrystals
section_title: "Convergent isocrystals."
section_number: 8.6
pages: 84-87
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.856
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.6}     

\begin{para}\label{para:3.6.1} Let $S_0$ be a separated $k$-scheme of finite
 type, and $S_0\hookrightarrow \mathfrak{Y}$ a closed immersion into a
 flat $p$-adic formal $\mathfrak{v}$-scheme that is formally smooth in a
 neighborhood of $S_0$. Let $E$ be a vector bundle on the tube
 $]S_0[_{\mathfrak{Y}}$. An integrable connection $\nabla$ on $E$ is
 {\it convergent} if its Taylor series
 \begin{equation*}
  \epsilon(1\otimes e) =
   \sum_{n_1,\ldots,n_d\geq 0}
   \biggl(\nabla\Bigl(\frac{\partial }{\partial t_1}\Bigr)^{n_1}\ldots
   \nabla\Bigl(\frac{\partial }{\partial t_d}\Bigr)^{n_d}\biggr)(e)
   \otimes \;\prod_i\frac{\text{``$(1\otimes t_i-t_i\otimes 1)^{n_i}$''}}{n_i!}
 \end{equation*}
 is induced by an isomorphism on the tube of the
 diagonal $]S_0[_{\mathfrak{Y}\times \mathfrak{Y}}$
 \begin{equation*}
  \epsilon:\; p_2^\ast(E)\;\cong \;p_1^\ast(E)
 \end{equation*} 
 It amounts to the same to say that for any affine $U$ in $\mathfrak{Y}$
 with local coordinates
 $t_1,\ldots, t_d$, any section $e\in \Gamma(U^{\mathrm{an}},E)$ and any $\eta<1$,
 one has 
 \begin{equation*}
  \Bigl\|\nabla\Bigl(\frac{\partial }{\partial t_1}\Bigr)^{n_1}
   \ldots\nabla\Bigl(\frac{\partial }{\partial t_d}\Bigr)^{n_d}(e)\Bigr\|.
   \eta^{n_1+\ldots + n_d}\rightarrow 0
 \end{equation*}
 where $\|\;\;\|$ denotes a Banach norm on $\Gamma(U^{\mathrm{an}},E)$.

 According to Berthelot, {\it the category of vector bundles
with convergent connection depends only on $S_0$} --- even only on
$S_{0,\mathrm{red}}$ --- (up to canonical equivalence), and is functorial in
$S_0/K$; this is the category of {\it convergent isocrystals on $S_0/K$}
(or, abusively, on $S_0$).
 

Since any separated $k$-scheme locally of finite type can be locally
embedded into a $\mathfrak{X}$ as above, one can define the category of
convergent isocrystals on such a scheme by gluing \cite[2.3.2]{crecrasp}.
\end{para}

\begin{para}\label{para:3.6.2} There is a natural functor from the category
 of $F$-isocrystals on $S_0/\mathfrak{v}$ to the category of 
convergent isocrystals on $S_0/K$ \cite[2.4]{crecrasp}.  The composite of
this functor with the Dieudonn\'e functor is denoted by $\D(-)_\Q$. It
factors through a $\Q_p$-linear functor, still denoted by $\D(-)_\Q:\;$
\begin{equation*}
\Bigl\{\begin{matrix}
	\text{$p$-divisible groups over $S_0$}\\
	\text{up to isogeny}
       \end{matrix}\Bigr\}
 \longrightarrow
 \{\text{convergent isocrystals on $S_0$}\}
\end{equation*}
\end{para}

\begin{para}\label{para:3.6.3} The advantage of convergent isocrystals over
 ``crystals up to isogeny'' lies in their strong 
``continuity property'', which allows to remove the restriction $e<p$ on
ramification (as we shall do henceforth), and work conveniently with
singular schemes $S_0$ (while divided powers present certain
``pathologies'' in the singular case). In our applications, $S_0$ will
be a countable (non-disjoint) union of irreducible projective varieties,
and $\mathfrak{v}$ may be highly ramified.
\end{para}

\begin{para}\label{para:3.6.4} If $S_0$ is the reduced underlying scheme 
 ${\mathfrak{X}}_{\mathrm{red}}$ of a formal scheme $\mathfrak{X}$ as in
 \ref{para:3.5.1}, there 
 is a notion of {\it evaluation of $E$ on $\mathfrak{X}^{\mathrm{an}}$}
 \cite[2.3.2]{crecrasp}: this is a vector bundle on
 ${\mathfrak{X}}^{\mathrm{an}}$ with an integrable connection. 
 

 By functoriality of the construction, it will be enough to deal with the
 affine case ${\mathfrak{X}}=\Spf{\mathcal{A}}$ and to assume that there
 is a closed immersion $S_0=(\Spf{\mathcal{A}})_{\mathrm{red}}\hookrightarrow
 \mathfrak{Y}$ into a formally smooth $p$-adic formal
 $\mathfrak{v}$-scheme. One can construct inductively a compatible family
 of $\mathfrak{v}$-morphisms
 $\Spec(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^n)\rightarrow \mathfrak{Y}$,
 whence a $\mathfrak{v}$-morphism  $\mathfrak{X} \rightarrow
 \mathfrak{Y}$.  Let $\upsilon :\; ]S_0[_{\mathfrak{X}} 
 ={\mathfrak{X}}^{\mathrm{an}}\rightarrow\; ]S_0[_{\mathfrak{Y}}$ be the
 associated analytic map. The looked for evaluation of $E$ on
 ${\mathfrak{X}}^{\mathrm{an}}$ 
 is the pull-back by $\upsilon$ of the vector bundle with integrable
 connection on $]S_0[_{\mathfrak{Y}}$ defined by $E$.
\end{para}

\begin{para}\label{para:3.6.5} Let now $S$ be a separated scheme in
 $\Nil_\mathfrak{v}$ (it may also be viewed in  $\Nil_W$).
 Let $\mathcal{E}$ be a finite locally free $F$-crystal on $S/W$. This
 provides a vector bundle $\mathcal{E}_S$ on $S$, which 
 only depends on the inverse image $\mathcal{E}\times_W k$ of
 $\mathcal{E}$ on the $k$-scheme $S/p$ (\cf \ref{para:3.2.1}). On the other 
 hand, the convergent isocrystal $E$ on $S/p$ attached to $F$-crystal
 $\mathcal{E}\times_W k$ (\cf \ref{para:3.6.2}) depends only on
 $S_{\mathrm{red}}$.
\end{para}

\begin{para}\label{para:3.6.6} Let us apply this to Dieudonn\'e
 crystals. Let $\mathfrak{X}$ be a formal scheme as in \ref{para:3.5.1},
 and let 
 $\Lambda=\liminj \Lambda_n$ be a $p$-divisible on
 $\mathfrak{X}=\liminj {\mathfrak{X}}_n$. This gives rise to a vector bundle 
 $\displaystyle \D(\Lambda)_{\mathfrak{X}}= \liminj
 \D(\Lambda_n)_{{\mathfrak{X}}_n}$ on $\mathfrak{X}$. On the other 
 hand, we have the vector bundle $\displaystyle
 \D(\Lambda_0)_{\mathfrak{X}}=$ on $\mathfrak{X}$ and a natural
 homomorphism $\D(\Lambda_0)_{\mathfrak{X}}\rightarrow
 \D(\Lambda)_{\mathfrak{X}}$ obtained by pull-back 
 ${\mathfrak{X}}_{\mathrm{red}}={\mathfrak{X}}_0\rightarrow {\mathfrak{X}}$.


When $e\geq p$, this is not an isomorphism in general. However, {\it the
associated morphism of analytic vector bundles
$(\D(\Lambda_0)_{\mathfrak{X}})^{\mathrm{an}}\rightarrow
(\D(\Lambda)_{\mathfrak{X}})^{\mathrm{an}}$ is an isomorphism.  Moreover,
$(\D(\Lambda_0)_{\mathfrak{X}})^{\mathrm{an}}$ is the analytic vector bundle
underlying the evaluation of $\D(\Lambda_0)_\Q$ on
${\mathfrak{X}}^{\mathrm{an}}$}.


Indeed, working locally, and taking in account the very construction of
${\mathfrak{X}}^{\mathrm{an}}$, we reduce to the case when ${\mathfrak{X}}$ is
$p$-adic. Then $\mathfrak{X}/p$ is a $k$-scheme. Using the canonical
divided powers on $(p)$ and the rigidity of crystals,
$\D(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_{\mathfrak{X}}\cong
\D(\Lambda)_{\mathfrak{X}}$. It is thus enough to see that
$\D(\Lambda_0)^{\mathrm{an}}\cong\D
(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_{\mathfrak{X}}^{\mathrm{an}}$. This
follows from the fact that the convergent isocrystals $\D(\Lambda_0)_\Q$
and $\D(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_\Q$ are ``the
same'', since ${\mathfrak{X}}_0=({\mathfrak{X}}/p)_{\mathrm{red}}\;$: indeed, it
is clear that $(\D(\Lambda_0)_{\mathfrak{X}})^{\mathrm{an}}$ (\resp
$\D(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_{\mathfrak{X}}^{\mathrm{an}}$)
coincides with the evaluation of the convergent isocrystal
$\D(\Lambda_0)_\Q$ (\resp
$\D(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_\Q$) on
${\mathfrak{X}}^{\mathrm{an}}$ (\cf also \cite[6.4]{efgonas}, in a slightly less
general context).
\end{para}

\begin{para}\label{para:3.6.7} Let us draw from this two consequences:
 \begin{enumerate}
  \item taking into account the fact that the functor $\D(-)_\Q$ factors
	through the category of $p$-divisible
	groups up to isogeny, we see that if we are given a quasi-isogeny
	$\Lambda_0\rightarrow \Lambda_0'$, then there is a
	canonical isomorphism of vector bundles
	$\bigl(\D(\Lambda'_0)_{\mathfrak{X}}\bigr)^{\mathrm{an}}\rightarrow
	\bigl(\D(\Lambda)_{\mathfrak{X}}\bigr)^{\mathrm{an}}$.
  \item Through the isomorphism
	$\bigl(\D(\Lambda_0)_{\mathfrak{X}}\bigr)^{\mathrm{an}}\rightarrow
	\bigl(\D(\Lambda)_{\mathfrak{X}}\bigr)^{\mathrm{an}}$ (or equivalently,
	through the isomorphism
	$\D\bigl(\Lambda\times_{\mathfrak{X}}
	\mathfrak{X}/p\bigr)_{\mathfrak{X}}^{\mathrm{an}}
	\rightarrow
	\bigl(\D(\Lambda)_{\mathfrak{X}}\bigr)^{\mathrm{an}}$), the 
	analytic vector bundle
	$\bigl(\D(\Lambda)_{\mathfrak{X}}\bigr)^{\mathrm{an}}$ is naturally
	endowed with an integrable connection, which deserves to be
	called the {\it Gauss-Manin} connection attached to $\Lambda$.
 \end{enumerate}

 Indeed, when $\Lambda=\udl{A}[p^\infty]$ for an abelian scheme
 $\udl{A}$ over $\mathfrak{X}$,
 $(\D(\Lambda)_{\mathfrak{X}})^{\mathrm{an}}$ may then be identified
 with the De Rham cohomology bundle
 $\mathrm{H}^1_{\mathrm{DR}}(\udl{A}^{\mathrm{an}}/
 {\mathfrak{X}}^{\mathrm{an}})$
 together with its Gauss-Manin connection.  Here, one can use the
 comparison theorem between crystalline and De Rham cohomology, or the
 theory of universal vectorial extensions and Grothendieck's
 $\natural$-structures, \cf \cite{mazur74:_univer}, \cite{tddc2}.

 In the first alternative, one uses the
 divided powers on $(p)$ and construct a canonical isomorphism of vector
 bundles with connection 
 $\D(\Lambda\times_{\mathfrak{X}}\mathfrak{X}/p)_{\mathfrak{X}}\cong
 \mathrm{H}^1_{\mathrm{DR}}(\udl{A}/{\mathfrak{X}})$.


 In the second alternative, one uses Grothendieck's construction of a
 canonical connection on the universal vectorial extension $\E(\Lambda)$
 of $\Lambda^\vee$ --- \cf \ref{para:3.3.2}; the induced connection on the Lie
 algebra $\D(\Lambda)_{\mathfrak{X}}$ turns out to be the Gauss-Manin
 connection on $ \mathrm{H}^1_{\mathrm{DR}}(\udl{A}/{\mathfrak{X}})$.


 The Gauss-Manin connection is especially significant when
 ${\mathfrak{X}}^{\mathrm{an}}$ is smooth (even though $\mathfrak{X}$
 itself may not be formally smooth).

\newpage
