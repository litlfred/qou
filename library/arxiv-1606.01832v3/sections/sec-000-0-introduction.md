---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-4
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
toc_source: outline
text_source: latex
latex_prose_ratio: 0.755
latex_coverage_ratio: 0.946
doc_brief: "FLATNESS AND COMPLETION REVISITED — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
In this paper we continue investigating the interaction between flatness 
and adic completion for infinitely generated modules over a commutative 
ring, that we had started in \cite{Ye1}. 

Let $A$ be a commutative ring, and let $\a$ be an ideal in it. For each $k \in 
\N$ we define the quotient ring
$A_k := A / \a^{k + 1}$. 
The collection of rings $\{ A_k \}_{k \in \N}$ is an inverse system,
and the $\a$-adic completion of $A$ is the commutative ring 
$\what{A} := \lim_{\leftarrow k} \, A_k$. 
There is a canonical ring homomorphism $A \to \what{A}$. 

An {\em $\a$-adic system} of $A$-modules is an inverse system
$\{ M_k \}_{k \in \N}$, where each $M_k$ is an $A_k$-module, and the induced 
homomorphisms 
\[ A_k \ot_{A_{k + 1}} M_{k + 1} \to M_k \]
are all bijective. The {\em limit} of the system is the $A$-module 
$\what{M} := \lim_{\leftarrow k} \, M_k$.

Given an $A$-module $M$, we let 
$M_k := A_k \ot_A M$.
The collection of $A$-modules $\{ M_k \}_{k \in \N}$ is an inverse system,
that we call the {\em $\a$-adic system induced by $M$}. The limit $\what{M}$ of 
the induced system is the {\em $\a$-adic completion of $M$}.
There is a canonical $A$-module homomorphism 
$\tau_M : M \to \what{M}$, and $M$ is called {\em $\a$-adically complete} if 
$\tau_M$ is an isomorphism. (Some texts, mostly older ones, would say that $M$ 
is complete and separated.)

Our initial motivation was to prove the following theorem, that we consider 
important.

\begin{thm} \label{thm:165}
If $A$ is a noetherian commutative ring, $\a$ is an ideal in $A$, and $M$ is a 
flat $A$-module, then the $\a$-adic completion $\what{M}$ is a flat $A$-module.
\end{thm}

Of course the module $M$ has to be {\em infinitely generated} for this 
statement to be interesting.  

We were under the impression that this was an open question, solved only in 
special cases (cf.\ \cite{En}, \cite{BS},  \cite{Sct}, and
\cite[Theorems 4.2 and 3.4(2)]{Ye1}). This impression was 
based on a literature search and email correspondence with several experts. 
A few months ago we found a relatively simple proof of this result (it is now 
the proof of Theorem \ref{thm:262}(2) below). 

However, after email correspondence with a few more experts, to whom we showed 
a preliminary version of this paper, we learned that:
\begin{enumerate}
\item There is already a proof of Theorem \ref{thm:165}. It is  
\cite[Lemma 0AGW]{SP}, presumably due to de Jong, from around 2013. 

\item There is an elementary proof of Theorem \ref{thm:165}, 
indicated to us by Gabber and Ramero, along the lines of \cite[Lemma 7.1.6]{GR}.
\end{enumerate}

Thus we turned our attention to a few theorems of secondary importance, that 
are totally new, and to which our methods could be applied. This is the content 
of the present paper.

Before going on, let us make several general remarks about $\a$-adic 
completion and $\a$-torsion, that are not widely known. For an $A$-module $M$, 
let us write $\La_{\a}(M) := \what{M}$, and let $\Ga_{\a}(M)$ be the 
$\a$-torsion submodule of $M$. So $\La_{\a}$ and $\Ga_{\a}$ are $A$-linear 
functors from the category $\cat{Mod} A$ of $A$-modules to itself. 

If the ideal $\a$ is finitely generated, then for every $A$-module $M$ its 
$\a$-adic completion $\what{M}$ is $\a$-adically complete. 
Thus the functor $\La_{\a}$ is idempotent, in the sense that 
$\La_{\a} \circ \La_{\a} \cong \La_{\a}$.
There are counterexamples to this idempotence when the ideal $\a$ is not 
finitely generated. See \cite[Corollary 3.6 and Example 1.8]{Ye1}.

Even when the ring $A$ is noetherian (which of course forces the ideal $\a$ to 
be finitely generated), the functor $\La_{\a}$ is not left-exact nor 
right-exact. It is true that when $A$ is noetherian, the functor $\La_{\a}$ is 
exact when restricted to the category $\cat{Mod}_{\mrm{f}} A$ of finitely 
generated $A$-modules.

The functor $\Ga_{\a}$ is always right exact and idempotent. 

The first main result of our paper is on $\a$-adic systems. It is a vast 
generalization of the classical case, in which $A$ is noetherian and each $M_k$ 
is a finitely generated $A_k$-module. 

\begin{thm} \label{thm:180}
Let $A$ be a commutative ring, let $\a$ be a finitely generated ideal in $A$, 
and let $\{ M_k \}_{k \in \N}$ be an $\a$-adic system of 
$A$-modules, with limit $\what{M}$. Then\tup{:}
\begin{enumerate}
\item The $A$-module $\what{M}$ is $\a$-adically complete.

\item For every $k \geq 0$ the canonical homomorphism 
$A_k \ot_A \what{M} \to M_k$ is bijective.
\end{enumerate}
\end{thm}

This theorem is repeated as Theorem \ref{thm:230} in Section \ref{sec:adic-sys} 
and proved there. An immediate consequence of Theorem \ref{thm:180} is that 
when the ideal $\a$ is finitely generated, every $\a$-adic system 
$\{ M_k \}_{k \in \N}$ is induced from a module.
See Corollaries \ref{cor:333} and \ref{cor:263}.

Now we turn to flatness. 
An $A$-module $M$ is said to be {\em $\a$-adically 
flat} if \lb $\opn{Tor}^A_i(N, M) = 0$ for every $i > 0$ and every 
$\a$-torsion $A$-module $N$. Clearly flatness implies $\a$-adic flatness.  

Here is a useful characterization of $\a$-adically flat modules. 

\begin{thm} \label{thm:261}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and 
let $M$ be an $A$-module. The following conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} The $A$-module $M$ is $\a$-adically flat.

\rmitem{ii} For every $i > 0$ and $k \geq 0$ the module 
$\opn{Tor}^{A}_i(A_{k}, M)$ vanishes, and   
$A_{k} \ot_A M$ is a flat $A_k$-module.  

\rmitem{iii} For every $i > 0$ the module 
$\opn{Tor}^{A}_i(A_{0}, M)$ vanishes, and   
$A_{0} \ot_A M$ is a flat $A_0$-module. 
\end{enumerate}
\end{thm}

This is repeated as Theorem \ref{thm:168} in the body of the paper. 
Observe that there are no finiteness conditions on $A$, $\a$ or $M$. 
The result is similar to \cite[Lemma 051C]{SP} -- see Remark \ref{rem:310} 
for a comparison. The proof of Theorem \ref{thm:261} relies on some basic 
properties of the derived tensor product. 

Suppose $\bsym{a} = (a_1, \ldots, a_n)$ is a finite sequence of elements in 
$A$. The sequence $\bsym{a}$ is called {\em weakly proregular} if it satisfies 
a 
rather complicated condition, involving the Koszul complexes associated to 
powers of $\bsym{a}$. The definition is recalled in Section 
\ref{sec:WPR}. The ideal $\a$ is called weakly proregular if it is 
generated by some weakly proregular sequence. It is known that when $A$ 
is noetherian, every ideal in it is weakly proregular.
But there are fairly natural examples of weakly proregular ideals 
in non-noetherian rings (see Theorem \ref{thm:205} for such an example). 
It is now understood (see \cite{PSY1} and \cite{PSY2}) that weak proregularity 
of the ideal $\a$ is a necessary and sufficient condition for the derived 
functors $\mrm{L} \La_{\a}$ and $\mrm{R} \Ga_{\a}$ to have ``good behavior''.

As the next results show, adic flatness belongs to the ``twilight 
zone'' between the weakly proregular case and the noetherian case. 
Adic flatness comes up in the weakly proregular situation:

\begin{thm} \label{thm:280}
Let $A$ be a commutative ring, let $\a$ be a weakly proregular ideal in $A$, 
and let $M$ be an $\a$-adically flat $A$-module, with $\a$-adic completion 
$\what{M}$. Then the $A$-module $\what{M}$ is $\a$-adically flat. 
\end{thm}

But then the two notions of flatness merge in the noetherian case:

\begin{thm} \label{thm:281}
Let $A$ be a noetherian commutative ring, let $\a$ be an ideal in $A$, 
and let $\what{M}$ be an $\a$-adically flat $\a$-adically complete $A$-module. 
Then $\what{M}$ is a flat $A$-module. 
\end{thm}

Theorem \ref{thm:280} is repeated as Theorem \ref{thm:200} in the body of the 
paper. The proof uses derived categories and the MGM equivalence. 
On the other hand, Theorem \ref{thm:281} (repeated as Corollary \ref{cor:320}), 
is a consequence of item (2) of the following theorem, combined with Theorem 
\ref{thm:261}. 

An $\a$-adic system $\{ M_k \}_{k \in \N}$ is called {\em flat} if each $M_k$ 
is a flat $A_k$-module.  

\begin{thm} \label{thm:262}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and 
let $\{ M_k \}_{k \in \N}$ be a flat  $\a$-adic system, with limit 
$\what{M}$.

\begin{enumerate} 
\item If the ideal $\a$ is weakly proregular, then $\what{M}$ is an 
$\a$-adically flat $A$-module. 
\item If the ring $A$ is noetherian, then $\what{M}$ is a flat $A$-module. 
\end{enumerate}
\end{thm}

Parts (1) and (2) of the theorem are repeated as Theorems \ref{thm:290} and 
\ref{thm:295} respectively. The proofs use {\em free resolutions of 
$\a$-adic systems}, and properties of 
{\em modules of decaying functions} that were established in \cite{Ye1}.

The reader might wonder whether the distinction between flatness and 
adic flatness is genuine. The answer is that these notions are indeed distinct. 
In Theorem \ref{thm:205} we give an example of a ring $A$ and a weakly 
proregular ideal $\a \subseteq A$, such that 
the $\a$-adic completion $\what{A}$ -- which is an $\a$-adically flat 
$A$-module by Theorem \ref{thm:280} -- {\em is not flat over $A$}. 
This example is not exotic at all. The ring is 
\[ A := \K[[t_1]] \ot_{\K} \K[[t_2]] , \]
where $\K$ is a field of characteristic $0$; and the ideal is 
$\a := (t_1, t_2)$. 

In Sections \ref{sec:adic-flatness} and \ref{sec:WPR} we use {\em derived 
category} methods. All the necessary background on these methods can be found in 
the new book \cite{Ye3}. Perhaps some of the results in Section 
\ref{sec:adic-flatness} could be proved using only classical homological 
algebra (i.e.\ Ext, Tor and related spectral sequences); but even if so, the 
proofs would very likely be much longer and more difficult to understand. 
The proofs in Section \ref{sec:WPR}, that involve the MGM 
Equivalence, definitely require the use of derived categories. 

The content of this paper belongs to commutative algebra. However, it is 
expected to have applications in {\em noncommutative 
ring theory} and {\em representation theory}. Indeed, our paper \cite{Ye1} was 
written as part of our project on {\em deformation quantization}, for which we 
needed sharper results on $\a$-adically complete flat noncommutative central 
$A$-rings (and sheaves of this type). See the paper \cite{Ye2} and its 
references. 

 
\medskip \noindent
{\bf Acknowledgments}. 
Thanks to Liran Shaul, Sean Sather-Wagstaff, Asaf Yekutieli, Steven Kleiman, 
Brian Conrad, Ofer Gabber, Lorenzo Ramero, Pierre Deligne, Johan de Jong,  
Ilya Tyomkin and Leonid Positselski for helpful discussions. We also wish to 
thank the anonymous referee, for reading the paper carefully and suggesting 
several improvements.
