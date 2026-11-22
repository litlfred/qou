---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-006-25-towards-a-theory-of-negative-dependence-probl
section_title: "Towards a Theory of Negative Dependence: Problems and Solutions"
section_number: 2.5
pages: 11-13
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.983
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s24}

A series of problems and conjectures was proposed by several authors as 
natural steps toward building as general a theory of negative dependence as 
possible. In \cite[\S III]{P} Pemantle pointed out that although
they are desirable, the many negative dependence properties listed in 
\S \ref{s21} might not be mutually satisfiable, and he suggested a problem that
may be formulated as follows.

\begin{problem}\label{pem-prob}
Find a natural and useful class of ``negatively dependent measures''.
\end{problem}

Note that there may well exist several such classes, if indeed any, 
depending on the
applications that one has in mind. We show that the class of strongly Rayleigh 
measures introduced in \S \ref{s23} enjoys all the negative dependence 
properties defined in \S \ref{s21} as well as other properties, which 
provides an answer to Problem~\ref{pem-prob}. 

The problem of describing natural
negative dependence properties that are preserved by symmetric exclusion 
evolutions has 
attracted some attention in the theory of 
interacting particle systems
and Markov processes \cite{L0,L00,L2}, see Problem~\ref{p-see} in 
\S \ref{ss-ex-case} and the discussion therein. In particular, the 
following conjecture
was implicitly made in \cite[p.~1374]{P} and \cite[p.~551]{L2}. 

\begin{conjecture}\label{con-lig}
If the initial configuration of a symmetric exclusion process
is non-random/deterministic, then the distribution at time $t$ is NA for 
all $t>0$.
\end{conjecture}

In \S \ref{n-s6} we prove a stronger form of this conjecture using the 
results on strongly Rayleigh measures obtained in \S \ref{s-stable}.

There are several conjectures, first published in \cite{P} 
but apparently 
of obscure folklore origin (cf.~\cite{W}), stating that various negative
dependent properties give rise to ULC rank sequences. The strongest form
of these is contained in the first part of Conjecture 4 in Pemantle's paper 
\cite{P} (see also \cite[Conjecture 3.9]{W}) and reads as follows.

\begin{conjecture}\label{c-p}
If $\mu\in\fP_n$ is $\NA$ then it is $\ULC$.
\end{conjecture}

Inspired by Conjecture~\ref{c-p} 
and motivated by Mason's long-standing
conjecture in enumerative graph/matroid theory \cite{Mason}, Wagner made the 
following conjecture in \cite[Conjecture 3.4]{W} and baptized it 
``The Big Conjecture'' since -- if true -- it would prove the validity of 
Mason's conjecture for a large class of matroids.  

\begin{conjecture}\label{big}
Any Rayleigh measure $\mu\in\fP_n$ is $\ULC$.
\end{conjecture}

Since we now know that the Rayleigh and h-NLC+ properties are equivalent 
(Proposition~\ref{p-r-h}), 
Conjecture~\ref{big} is actually already contained in the second part
of Conjecture 4 in Pemantle's paper \cite{P}. The weakest form of the latter 
conjecture is the one stated below.

\begin{conjecture}\label{cna-ulc}
If $\mu\in\fP_n$ is $\CNA+$ then it is $\ULC$.
\end{conjecture}

In \S \ref{s-countex} we construct examples of measures in $\fP_n$ for any
$n\ge 20$ that disprove all these three conjectures (for the strongest
of these, namely Conjecture~\ref{c-p}, we can actually find
counterexamples already in $\fP_3$ and $\fP_4$, see Remark~\ref{r-strong-NA}).
In fact, our examples 
show that the strongest negative association property (CNA+) 
need not even give rise to an SLC rank sequence 
(Definition~\ref{d-ulc}), thus invalidating a still weaker version of 
Conjecture~\ref{cna-ulc}. Moreover, these same examples show that
neither the PHR property (Definition~\ref{phr}) nor
indeed any of the properties weaker than strongly Rayleigh implies the 
ULC property, and also that Conjecture~\ref{cna-ulc} fails even under extra 
assumptions like those suggested in \cite[Problem 6]{BBCV}. This confirms 
once again the delicate nature of negative dependence.

The FKG theorem \cite{FKG} is a powerful tool that allows one to establish 
(global) positive correlation inequalities and limit theorems from a 
local (usually easier to check) condition, namely the positive lattice 
condition PLC. By contrast, there is as yet no general and practical 
local-to-global device for negative dependence/association. 
The NLC property is not closed under 
projections and implies neither the NA nor the (weaker) p-NC property, so the
negative version of the FKG theorem fails. As a potential remedy to this
situation, in \cite[Conjecture~2]{P} Pemantle
conjectured that the implications 
CNA $\Rightarrow$ h-NLC and CNA+ $\Rightarrow$ Rayleigh/h-NLC+ 
(established in \cite{P}, cf.~Remark~\ref{r-cn-hn}) are actually equivalences:

\begin{conjecture}\label{con-cna-R}
h-NLC $\,\Rightarrow$ CNA and Rayleigh/h-NLC+ $\Rightarrow$ CNA+. 
\end{conjecture}

We prove Conjecture~\ref{con-cna-R} 
for almost symmetric measures (cf.~Definition~\ref{d-exc}). 
Since PHR measures are CNA+  
(Theorem~\ref{PHR-NA}), we are naturally
led to consider the following related problem. 

\begin{problem}\label{prob-phr-cna}
Is PHR $=$ Rayleigh/h-NLC+?
\end{problem}

Note that if true, this would prove the second part of 
Conjecture~\ref{con-cna-R}. 
In \S \ref{s-countex} we show that the answer to 
Problem~\ref{prob-phr-cna} is negative, and that in fact the class of 
PHR measures 
is strictly contained in the class of CNA+ measures. The question 
whether Conjecture~\ref{con-cna-R} is true in full generality 
therefore remains open.

We summarize the implications between the various notions of 
negative dependence discussed so far in Fig.~\ref{fig} below. 
Compared with
the one in \cite[\S II.B]{P}, this diagram contains five extra 
classes -- three ``old'' (ULC, p-NC, NLC) and two ``new'' 
(strongly Rayleigh, PHR) -- and disregards the classes called 
JNRD, JNRD+ in \cite{P}.

\begin{figure}[!htb]
\xymatrix{
& & & \text{ULC} & {\text{{\normalsize Strongly}}\atop 
\text{{\normalsize Rayleigh}}}\ar@{>}[l]\ar@{>}[d] & \\
& & & & \text{PHR}\ar@{>}[d] & \\
& & & & \text{CNA+}\ar@{>}[d]\ar@{>}[r] & {\text{{\normalsize Rayleigh}}\atop 
\text{{\normalsize (h-NLC+)}}}\ar@{>}[d] \\
& & & & \text{CNA}\ar@{>}[d]\ar@{>}[r] & \text{h-NLC}\ar@{>}[ddl]\ar@{>}[d] \\
& & & & \text{NA}\ar@{>}[d] & \text{NLC} \\
& & & & \text{p-NC} & }
\caption{Subordination relations between negative dependence properties.}
\label{fig}
\end{figure}

As we already noted, the above examples and those
in the next sections show that the 
left horizontal, down left, and all vertical implications 
in Fig.~\ref{fig} are strict, while the question whether the right horizontal
implications are also strict is open (cf.~Conjecture~\ref{con-cna-R}). Note
also that there is no arrow pointing towards ULC from anything ``below'' 
strongly Rayleigh.

In \cite[\S I.B \& \S III.C]{P} it was pointed out that the notions of 
stochastic domination and truncation are also 
useful when studying (positive or) negative dependence.

\begin{definition}\label{d-stoc}
If $\mu,\nu\in\fP_n$ are such that $\mu(\cA)\ge \nu(\cA)$ for any
increasing event $\cA$ on $2^{[n]}$ one says that $\mu$ 
{\em stochastically dominates} $\nu$, written $\mu\suc \nu$ or $\nu\pc \mu$.
\end{definition}

\begin{definition}\label{d-trunc}
Let $\mu\in\fP_n$ and $1\le p\le q\le n$. The 
{\em truncation}
of $\mu$ to $[p,q]$ is the conditional measure 
$$\mu_{p,q}:=\left(\mu\,\bigg|\,p\le \sum_{i=1}^{n}X_i\le q\right)
\in\fP_n,$$
which is well defined provided that 
$\mu\left(\left\{S\in 2^{[n]}:p\le |S|\le q\right\}\right)\neq 0$. 
The generating polynomial of $\mu_{p,q}$ is thus given by
$$g_{\mu_{p,q}}(z_1,\ldots,z_n)
=\frac{g_{p,q}(z_1,\ldots,z_n)}
{g_{p,q}(1,\ldots,1)}\in\PP_n,$$
where $g_{p,q}(z)=\sum_{p\le |S|\le q}a_Sz^S$ and 
$\sum_{S\subseteq [n]}a_{S}z^S=g_{\mu}(z)$.
\end{definition}

For simplicity, we let $\mu_k=\mu_{k,k}$, $0\le k\le n$.
In \cite{J-DP,P} and references therein it has been discussed whether 
truncations of measures are operations that preserve negative dependence
properties. Question 10 of \cite{P} asks the following.

\begin{problem}\label{p-stoc-d}
Under what hypotheses on $\mu$ can one prove that $\mu_k\pc \mu_{k+1}$?
\end{problem}

Moreover, the next conjecture was made in \cite[Conjecture 8]{P}.

\begin{conjecture}\label{st}
Suppose that  $\mu$ is $\CNA+$ and that  
$$\mu(\{S \in 2^{[n]} : |S|=k\})\mu(\{S \in 2^{[n]} : |S|=k+1\})>0.$$ 
Then $\mu_k \pc \mu_{k+1}$. 
\end{conjecture}

To underline the relevance of these questions, in \cite[\S III.C]{P}
Pemantle argued that a combination of positive answers to
Problem~\ref{p-stoc-d} and Conjecture~\ref{st} (for Rayleigh 
measures) would imply Conjecture~\ref{con-cna-R}. In
\S \ref{ss-trunc} we give an answer to Problem~\ref{p-stoc-d} and prove that
its conclusion (hence also that of Conjecture~\ref{st}) 
holds for strongly Rayleigh measures, while in \S \ref{s-countex} we disprove
Conjecture~\ref{st} in its full generality.
