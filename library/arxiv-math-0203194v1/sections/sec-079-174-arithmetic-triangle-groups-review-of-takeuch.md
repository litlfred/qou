---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-079-174-arithmetic-triangle-groups-review-of-takeuch
section_title: "Arithmetic triangle groups. Review of Takeuchi's list."
section_number: 17.4
pages: 186-188
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.983
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::5.4}

\begin{para}\label{para::5.4.1} (Cocompact) arithmetic triangle groups
 are hyperbolic triangle groups which are {\it commensurable with the
 unit groups of quaternion algebras $B$ over number fields}.

 In order to make this definition more precise, let us first place
 ourselves in greater generality. Let $E$ be a number field, and let $B$
 be a quaternion algebra over $E$. Let $V$ be a finite set of places of
 $E$ containing the places at infinity and at least one place (possibly
 infinite) where $B$ is unramified. Let us define
 \begin{equation*}
  G_{(V)} = \prod \,B_v^\times/E_v^\times = \prod \, PGL_2(E_v)
 \end{equation*} where the product runs over all places $v\in V$ which
 are unramified for
 $B$. Let $\mathcal{O}_{E}(V)$ be the ring of so-called $V$-integers of
 $E$ (elements which are integers at the places not in $V$),
 let $\mathcal{B}(V)$ be a maximal $\mathcal{O}_{E}(V)$-order in
 $B$, and let $PSL_1(\mathcal{B}(V))$ be the image in $G_{(V)}$ of the
 group of elements of $\mathcal{B}(V)$ of reduced norm $1$. 
 This is a cocompact discrete subgroup of $ G_{(V)}$, but the projection
 of $PSL_1(\mathcal{B}(V))$ in any proper factor of 
 $G_{(V)}$ is dense \cite[IV.1.1]{adadq}. 

 Any subgroup of $G_{(V)}$ which is commensurable to
 $PSL_1(\mathcal{B}(V))$ is called an {\it arithmetic subgroup of $G_{(V)}$}. 

 \noindent In particular, arithmetic subgroups of $PGL_2(\R)$ are
 subgroups which are commensurable with the unit groups
 $PSL_1(\mathcal{B})$ of quaternion algebras over {\it totally real}
 number fields $E$, which are {\it split at exactly one place at
 infinity $\infty_0$} (and one can take $V=\{\infty_0\}$).
\end{para}

\begin{para}\label{para::5.4.2} The complete list of cocompact
 arithmetic triangle groups (there are $76$ such groups, up to
 permutation of $e_0,e_1,e_\infty$), and of the corresponding quaternion
 algebras, has been established by K. Takeuchi; moreover, he has shown
 that two arithmetic triangle groups are commensurable with each other
 if and only if they come from the same quaternion algebra. Here is the
 list \cite[Table 1]{ccoatg}:

\renewcommand{\arraystretch}{1.5}
\begin{longtable}{lcp{0.63\textwidth}}
 $E$ & $\mathrm{disc}(B)$ & $ (e_0,e_1,e_\infty)\text{ up to permutation}$ \\
 \hline
 $\Q$ & $2.3$ & $(2,4,6)\, (2,6,6)\, (3,4,4)\, (3,6,6)$ \\
 $\Q(\sqrt 2)$ & $v_2$ &
 $(2,3,8)\, (2,4,8)\, (2,6,8)\, (2,8,8)\, (3,3,4)\, (3,8,8)\,$ 
 $(4,4,4)\, (4,6,6)\, (4,8,8)$ \\
 $\Q(\sqrt 3)$ & $v_2$ &
 $(2,3,12)\, (2,6,12)\, (3,3,6)\, (3,4,12)\, (3,12,12)\, (6,6,6)\,$ \\
 $\Q(\sqrt 3)$ & $v_3$ & $(2,4,12)\, (2,12,12)\, (4,4,6)\, (6,12,12)\,$ \\
 $\Q(\sqrt 5)$ & $v_2$ & $(2,4,5)\, (2,4,10)\, (2,5,5)\, (2,10,10)\,
 (4,4,5)\, (5,10,10)$ \\
 $\Q(\sqrt 5)$ & $v_3$ & $(2,5,6)\, (3,5,5)$ \\
 $\Q(\sqrt 5)$ & $v_5$ & $(2,3,10)\, (2,5,10)\, (3,3,5)\, (5,5,5)$ \\
 $\Q(\sqrt 6)$ & $v_2$ & $(3,4,6)$ \\
 $\Q(\cos \pi/7)$ & $1$ &
 $(2,3,7)\, (2,3,14)\, (2,4,7)\, (2,7,7)\, (2,7,14)\, (3,3,7)\,$ 
 $(7,7,7)$ \\ 
 $\Q(\cos \pi/9)$ & $1$ & $(2,3,9)\, (2,3,18)\, (2,9,18)\, (3,3,9)\,
 (3,6,18)\, (9,9,9)$ \\
 $\Q(\cos \pi/9)$ & $v_2.v_3$ &
 $(2,4,18)\, (2,18,18)\, (4,4,9)\, (9,18,18)$ \\
 $\Q(\cos \pi/8)$ & $v_2$ &
 $(2,3,16)\, (2,8,16)\, (3,3,8)\, (4,16,16)\, (8,8,8)$ \\
 $\Q(\cos \pi/10)$ & $v_2$ & $(2,5,20)\, (5,5,10)$ \\
 $\Q(\cos \pi/12)$ & $v_2$ & 
 $(2,3,24)\, (2,12,24)\, (3,3,12)\, (3,8,24)\, (6,24,24)\,$ $(12,12,12)$ \\
 $\Q(\cos \pi/15)$ & $v_3$ & $(2,5,30)\, (5,5,15)$ \\
 $\Q(\cos \pi/15)$ & $v_5$ &
 $(2,3,30)\, (2,15,30)\, (3,3,15)\, (3,10,30)\, (15,15,15)$ \\
 $\Q(\sqrt 2, \sqrt 5)$ & $v_2$ & $(2,5,8)\, (4,5,5)$ \\
 $\Q(\cos \pi/11)$ & $1$ & $(2,3,11).$\\

\end{longtable}

\medskip\noindent ($v_p$ denotes the unique place of $E$ above
 $p$. Notice that all fields 
 $E$ appearing in this table are Galois --- even abelian --- over $\Q$).
\end{para}

\begin{para}\label{para::5.4.3} We do not know whether all arithmetic
 triangle groups are 
 congruent subgroups (actually, unit groups of quaternion algebras seem
 to be unsolved hard cases of the congruence subgroup problem, \cf 
 \cite{rapinchuk92:_congr}). Nevertheless, in each commensurability
 class of arithmetic 
 triangle groups, there is a (unique) triangle group of the form
 \begin{equation*} \Gamma^\ast= \{g\in B^\times\mid 
 g\mathcal{B}=\mathcal{B}g, \Nr(g)>0\}: \end{equation*} this is the one
 which appears first in the each of the above rows, \cf
 \cite[Table 3]{ccoatg}. The corresponding Schwarz orbifolds are Shimura
 orbifolds $\mathcal{X}^\ast$. More generally, any Schwarz orbifold whose
 orbifold fundamental group is a congruence group, is a Shimura orbifold.
\end{para}
