---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.991
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
\subsection{Background}\label{ss:Backgroud}
The Murnaghan--Nakayama rule \cite{Mur,Nak1,Nak2} serves as a combinatorial algorithm for calculating the irreducible characters of symmetric groups $\mathfrak{S}_n$. The Iwahori--Hecke algebra $\mathscr{H}_{n}(q)$ in type $A$, which is the $q$-deformation of $\mathfrak{S}_n$, is a unital associative algebra over the field of rational functions $\mathbb{C}(q)$. Ram \cite{Ram} used the quantum Schur--Weyl duality \cite{Jim} to establish a Frobenius-type character formula for $\mathscr{H}_{n}(q)$, linking it to one-row Hall-Littlewood functions and Schur symmetric functions (see also \cite{KV, KW}). He also introduced the $q$-Murnaghan--Nakayama rule, an iterative combinatorial method for computing irreducible characters using smaller partitions. An alternative approach was explored in \cite{Pfe1}. Recent work \cite{JL1} employed the vertex operator realization of Schur functions to revisit the $q$-Murnaghan--Nakayama rule.

This approach has led to the
formulation of a Murnaghan--Nakayama rule for the Hecke--Clifford algebra \cite{JL2}, utilizing the vertex operator realization of Schur $Q$-functions. 

At the end of \cite{Pfe2}, Pfeiffer noted the potential for deriving irreducible character formulas for the cyclotomic Hecke algebra $\mathscr{H}_{m,n}(q,\bm{u})$ over some specific elements, yet evidence was lacking to show that these character values could yield a complete character table. This raises the question of which elements can determine the characters and how to derive the character values for others. In 1998, inspired by Greene's derivation of the Murnaghan--Nakayama formula via Young’s seminormal representations \cite{Gre}, Halverson and Ram \cite{HR} established an analogue of the Murnaghan--Nakayama rule for $\mathscr{H}_{m,n}(q,\bm{u})$, focusing on certain ``standard elements". They claimed, without proof, that these values would completely determine the characters. Subsequently, a result by Mak \cite{Mak} confirms that the characters of $\mathscr{H}_{m,n}(q,\bm{u})$ can be determined by the values of the ``standard elements" through a highly complicated process.

In 2000, Shoji \cite{Sho} utilized Schur--Weyl reciprocity between $\mathscr{H}_{m,n}(q,\bm{u})$ and a Levi subalgebra of the quantized enveloping algebra $\mathscr{U}_{q}(gl_m)$ \cite{SS} to provide a Frobenius-type formula for the characters of $\mathscr{H}_{m,n}(q,\bm{u})$. He introduced a new presentation and standard elements for $\mathscr{H}_{m,n}(q,\bm{u})$, proving that the characters are completely determined by their values on these elements \cite[Proposition 7.5]{Sho}, addressing Pfeiffer's earlier question. In contrast to the ``standard elements'' mentioned above, Shoji's version of ``standard elements'' has simpler forms.

In 2013, Regev \cite{Reg} obtained an 
elegant formula, now usually referred to as the Regev formula, for the characters of super representations of the symmetric group. This result was derived through the super analogue of the classical Schur--Weyl duality (sometimes called the Schur-Sergeev duality), combined with the combinatorial theory of Lie superalgebras, which was initially developed by Sergeev \cite{Ser84} and later expanded in detail by Berele and Regev \cite{BR}. Taylor \cite{Tay} provided a new proof of Regev's work by utilizing the Murnaghan--Nakayama formula for the skew characters of symmetric groups. Building on Taylor’s work, Zhao \cite{Zhao3} extended the (quantum) Regev formula to the Iwahori--Hecke algebra of type $A$ by employing the corresponding Murnaghan--Nakayama rule for skew characters. An alternative proof of the quantum Regev formula was recently presented in \cite{JL1} using the vertex operator realization of Schur functions. 


In \cite{LP}, L\"ubeck and Prasad established a character identity that connects the irreducible character values of the Weyl group $\mathscr{W}_{2,n}$ to those of the symmetric group $\mathfrak{S}_{2n}$ using the Frobenius character formula for symmetric groups. Subsequently, Adin and Roichman \cite{AR} provided a combinatorial proof of this identity and extended it to the setting of wreath products. We collectively refer to these results as the L\"ubeck--Prasad--Adin--Roichman formula.

The second orthogonality relation for the irreducible characters of a finite group plays a crucial role in computing these characters. The second orthogonality relation for the irreducible characters of a split semisimple algebra also makes sense. An explicit form of the second orthogonality relation for the irreducible characters of the Brauer algebra was given in \cite{Ram97}. The $q$-analogue of the second orthogonality relation for the Hecke algebra of type $A$ formulated in terms of the bitrace was determined in \cite{HLR, JL1}. 
A spin analogue of the bitrace was recently developed for the Hecke--Clifford algebra in \cite{JL2}.


\subsection{Aims}

While the earlier Murnaghan--Nakayama-type formulas of Halverson--Ram are fundamental, they are not fully suited to our present purposes. In particular, Halverson and Ram computed characters only on certain ``standard elements'' and did not prove in that paper that these values determine the full character table (although they indicated a method for doing so later). Moreover, their approach relies on explicit seminormal/Hoefsmit-type representations together with double-centralizer (Clifford-theoretic) arguments and a bitrace reduction. This framework is structurally powerful, but less convenient for the Frobenius-formula-based combinatorial recursions and applications that we pursue here. Mak later resolved the determinacy issue from a structural viewpoint via a reducibility theorem for trace functions on Ariki--Koike algebras, but this is of a different nature and does not directly provide an explicit iterative combinatorial character formula. By contrast, Shoji's Frobenius-type formula and his choice of standard elements offer a natural starting point for such a development.

This paper has two main goals. First, we formulate a Murnaghan--Nakayama rule for the cyclotomic Hecke algebra based on Shoji's Frobenius-type formula, together with an effective operational procedure for computing character values. Compared with earlier formulations, our rule has a more canonical form and specializes uniformly to several known formulas, including those for the complex reflection group of type $G(m,1,n)$ and the Iwahori--Hecke algebras of types $A$ and $B$. In addition, combined with Shoji's result \cite[Proposition 7.5]{Sho}, it provides a simpler route to the complete character table of $\mathscr{H}_{m,n}(q,\bm{u})$. Second, in a dual framework based on the vertex-operator realization of Schur functions, we derive an iterative formula on upper multipartitions, which may be viewed as a dual Murnaghan--Nakayama rule for the cyclotomic Hecke algebra.

Our second aim is to demonstrate the scope of these rules through several applications. We obtain a Regev-type formula for the cyclotomic Hecke algebra, establish a L\"ubeck--Prasad--Adin--Roichman-type formula that computes character values via partitions rather than multipartitions, and introduce the notion of multiple bitrace together with a general combinatorial formula. These applications illustrate the practical strength of the new Murnaghan--Nakayama rule and do not seem to be readily accessible from the earlier formulas. They also extend the corresponding formulas discussed in Subsection \ref{ss:Backgroud}.


\subsection{Main results} 
We now summarize the main results of the paper. In the Hecke algebra of type $A$, the Murnaghan--Nakayama rule is naturally expressed in terms of generalized ribbons. In the cyclotomic setting, the corresponding combinatorial objects become {\em generalized multi-ribbons}, namely $m$-tuples of generalized ribbons. When $m=1$, the cyclotomic Hecke algebra reduces to the Hecke algebra of type $A$, and generalized multi-ribbons reduce exactly to generalized ribbons. In this sense, our construction is a genuine extension of the type $A$ picture.

More broadly, our result fits into a unified pattern relating character formulas, symmetric functions, and skew-diagram combinatorics. Table \ref{t:M-N} summarizes Murnaghan--Nakayama rules for several algebras. The present work completes the last line of the table and simultaneously generalizes the cases of the symmetric group, Hecke algebras of types $A$ and $B$, and the complex reflection group $\mathscr{W}_{m,n}$.

\begin{table}
    \centering  
    \renewcommand{\arraystretch}{2}
{\small\begin{tabularx}{\textwidth}{>{\centering\arraybackslash}X>{\centering\arraybackslash}X>{\centering\arraybackslash}X}
\toprule
 \bf{Algebras} & \bf{Symmetric functions} & \bf{Skew diagrams} \\ \midrule
symmetric group $\mathfrak{S}_n$ & Schur function $s_{\la}$ & ribbon \\ \midrule
Hecke algebra (type $A$) $\mathscr{H}_n$ & Schur function $s_{\la}$ & generalized ribbon \\ \midrule
Hecke algebra (type $B$) $\mathscr{B}_n$ & double Schur function $s_{(\la,\mu)}$ & double generalized ribbon \\ \midrule
Sergeev algebra $\mathscr{C}_n\rtimes \mathfrak{S}_n$ & Schur $Q$-function $Q_{\la}$ & double strip \\ \midrule
Hecke--Clifford algebra $\mathscr{C}_n\rtimes \mathscr{H}_n$ & Schur $Q$-function $Q_{\la}$ & generalized double strip \\ \midrule
complex reflection group $\mathscr{W}_{m,n}$ & multi-Schur function $s_{\bm{\la}}$ & multi-ribbon \\ \midrule
{\em cyclotomic Hecke algebra} $\mathscr{H}_{m,n}(q,\bm{u})$ & {\em multi-Schur function} $s_{\bm{\la}}$ & {\em generalized multi-ribbon} \\ \bottomrule
\end{tabularx}}
\caption{Murnaghan--Nakayama rules for various algebras}\label{t:M-N}
\end{table}

Our first main result is a recursive Murnaghan--Nakayama rule for irreducible characters of the cyclotomic Hecke algebra, formulated directly on Shoji's standard elements.

\medskip
\begin{mainthm}[Corollary \ref{t:m-n2}]\label{t:A}
    Let $\bm{\la}$ and $\bm{\mu}$ be two multipartitions of $n$, and let $\chi_{\bm{\mu}}^{\bm{\la}}$ be the value of the irreducible character indexed by $\bm{\la}$ at the standard element $g(\bm{\mu})$. Then
\begin{align}
\chi_{\bm{\mu}}^{\bm{\la}}=\sum_{\bm{\nu}}\frac{q^{\mu^{(r)}_j}}{q-q^{-1}}\wt(\bm{\la/\nu};q^{-2},\bm{u},r)\chi^{\bm{\nu}}_{\bm{\mu}\setminus \mu^{(r)}_j},
\end{align}
where the sum runs over all multipartitions $\bm{\nu}\subset \bm{\la}$ such that $\bm{\la/\nu}$ is a $\mu^{(r)}_j$-generalized multi-ribbon. Here $\bm{\mu}\setminus \mu^{(r)}_j$ is obtained from $\bm{\mu}$ by deleting the $j$-th row of the $r$-th partition, and $\wt(\bm{\la/\nu};q^{-2},\bm{u},r)$ is the explicit weight defined in \eqref{e:defwt}.
\end{mainthm}


\medskip

Iterating Theorem \ref{t:A} yields a tableau-type expansion formula: the character value $\chi_{\bm{\mu}}^{\bm{\la}}$ can be written as a weighted sum over generalized multi-ribbon tableaux of shape $\bm{\la}$ and content $\bm{\mu}$ (Corollary \ref{t:m-n3}). This provides a fully combinatorial global formula, complementing the recursive version above.

In addition to the above (``lowering'') recursion, we establish a dual iterative formula in the opposite direction (Corollary \ref{c:dualMN2}), derived from the vertex operator realization of Schur functions. This dual formula expresses a character as a linear combination of characters indexed by multipartitions with strictly smaller upper data, and therefore gives a complementary computational mechanism to the Murnaghan--Nakayama rule.

We next turn to applications. The first application is a Regev-type formula for the permutation super representation of $\mathscr{H}_{m,n}(q,\bm{u})$.

\medskip
\begin{mainthm}[Theorem \ref{t:Regev}]\label{t:B}
    Let $\bm{\mu}$ be a $m$-multipartition of $n$. Then the value of the character of the permutation super representation on the standard element $g(\bm{\mu})$ is given by
\begin{align}\label{e:D}
\begin{split}
    &\chi^{\bm{u},q}_{\bm{k}|\bm{l};n}(g(\bm{\mu}))\\
=&q^{n-l(\bm{\mu})}\prod_{r=1}^m\prod_{j=1}^{l(\mu^{(r)})}\sum_{(\bm{\alpha};\bm{\beta})\in \mathfrak{C}(\mu^{(r)}_j;\bm{k}\mid\bm{l})} \bm{u}^r_{\overrightarrow{l}(\bm{\alpha};\bm{\beta})}(1-q^{-2})^{l(\balp;\bbeta)-1}(-q^{-2})^{|\bbeta|-l(\bbeta)}\prod_{i=1}^m\binom{k_i}{l(\alpha^{(i)})}\binom{l_i}{l(\beta^{(i)})}.
\end{split}
\end{align}
Here $\mathfrak{C}(\mu^{(r)}_j;\bm{k}\mid\bm{l})$ is defined in Sec. \ref{s:Regev}, $\overrightarrow{l}(\bm{\alpha};\bm{\beta}):=\max\{1\leq i\leq m\mid l(\alpha^{(i)})+l(\beta^{(i)})>0\}$, and $l(\balp;\bbeta):=l(\balp)+l(\bbeta)$.
\end{mainthm}
\medskip

A special case of Theorem \ref{t:B} yields a hook-sum formula (Cor. \ref{t:special-hook}) for irreducible characters indexed by multipartitions all of whose components are hooks. We also provide an alternative proof of this formula in Appendix \ref{app}.

Our second application is a cyclotomic Hecke algebra analogue of the L\"ubeck--Prasad--Adin--Roichman formula. It expresses irreducible characters indexed by multipartitions in terms of data attached to the corresponding partition with empty $m$-core.

\medskip
\begin{mainthm}[Theorem \ref{t:AR}]\label{t:C}
    Let $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ and $\bmu\in \mathcal{P}_{n,m}$, and let $\la$ be the unique partition with empty $m$-core and $m$-quotient $\bla$. Then
\begin{align}\label{e:E}
    \chi^{\bla}_{\bmu}=q^{n-l(\bmu)}\sum_{r=1}^m\sum_{\btau\in\mathcal{P}_m(\mu^{(r)})}\eta^{\la}_{\btau;r},
\end{align}
where $\eta^{\la}_{\btau;r}$ is the partition-based quantity introduced in Definition \ref{d:eta'}.
\end{mainthm}
\medskip

Under the specialization $\bm{u}=\bm{\zeta}=(1,\zeta,\zeta^2,\cdots,\zeta^{m-1})$, $q=1$, and $\bmu=(\varnothing,\cdots,\varnothing,\mu)$, Theorem E specializes to the Adin-Roichman formula for the complex reflection group $\mathscr{W}_{m,n}$.

Finally, we introduce the notion of {\em multiple bitrace} for $\mathscr{H}_{m,n}(q,\bm{u})$ and derive an explicit combinatorial formula. This may be viewed as a cyclotomic analogue of the bitrace formulas known in types $A$ and related settings.

\medskip
\begin{mainthm}[Theorem \ref{t:mbtr}]\label{t:D}
    Let $\bm{\mu}$ and $\bm{\nu}$ be two multipartitions of $n$. Then
\begin{align}\label{e:F}
        \mbtr(\bm{\mu},\bm{\nu})=\frac{q^{2n}}{(q-q^{-1})^{l(\bm{\mu})+l(\bm{\nu})}}\sum_{\bm{M},\bm{N},\bm{A}}\bm{u}_{\bm{M}}\bm{u}_{\bm{N}}\prod_{i=1}^m\wt_{q^{-2}}(A^{(i)}),
\end{align}
where the sum runs over pairs of $m$-multimatrices $(\bm{M},\bm{N})$ and $m$-tuples of matrices $\bm{A}$ satisfying the conditions stated in Theorem \ref{t:mbtr}. Here $\bm{u}_{\bm{M}}$ and $\wt_q(A^{(i)})$ are the corresponding weight polynomials attached to $\bm{M}$ and $A^{(i)}$, respectively.
\end{mainthm}
\medskip

By specialization, the left-hand side and right-hand side of \eqref{e:F} reduce to $\sum_{\bm{\la}\in \mathcal{P}_{n,m}}\phi^{\bm{\la}}_{\bm{\mu}}\overline{\phi^{\bm{\la}}_{\bm{\nu}}}$ and $\delta_{\bmu,\bm{\nu}}m^{l(\bmu)}\prod_{i=1}^m z_{\mu^{(i)}}$, respectively, and thus Theorem F recovers the second orthogonality relation for irreducible characters of $\mathscr{W}_{m,n}$:
\begin{align}
    \sum_{\bm{\la}\in \mathcal{P}_{n,m}}\phi^{\bm{\la}}_{\bm{\mu}}\overline{\phi^{\bm{\la}}_{\bm{\nu}}}=
    \begin{cases}
      m^{l(\bmu)}\prod\limits_{i=1}^m z_{\mu^{(i)}}, &\text{if $\bmu=\bm{\nu}$},\\
      0, &\text{otherwise},
    \end{cases}
\end{align}
where $z_{\lambda}:=\prod_{i\geq 1}i^{m_i(\lambda)}m_i(\lambda)!$ for a partition $\lambda$.





\subsection{Organization} 
The layout of this paper is as follows. In the next section, we will briefly review key terminologies related to multipartitions and symmetric functions indexed by multipartitions, along with a recapitulation of Shoji's Frobenius formula. In Sec. \ref{s:M-N}, we will present our Murnaghan--Nakayama rule, accompanied by several straightforward examples. Sec. \ref{s:special} focuses on three special cases of the Murnaghan--Nakayama rule, demonstrating how our rule recovers existing formulas for the complex reflection group of type $G(m, 1, n)$, as well as for Hecke algebras of type $A$ and type $B$. In Sec. \ref{s:OV}, we provide an alternative computational formula (dual Murnaghan--Nakayama rule) for the irreducible characters in a dual picture, utilizing the vertex operator realization of Schur functions. In Sec. \ref{s:Regev}, we present the first application of our Murnaghan--Nakayama rule: the Regev formula for the cyclotomic Hecke algebra. We extend the work of L\"ubeck--Prasad--Adin--Roichman to the setting of the cyclotomic Hecke algebra in Sec. \ref{s:LPAR}. Sec. \ref{s:mbtr} concentrates on the multiple bitrace of irreducible characters, followed by the presentation of a combinatorial formula for it. In Appendix \ref{app:sagecode}, we show how to use the Sagemath program \cite{Sage} to compute the irreducible character tables $(\chi^{\bm\la}_{\bm\mu})_{\bla,\bmu\in\mathcal P_{n,m}}$ via our Murnaghan--Nakayama rule.
