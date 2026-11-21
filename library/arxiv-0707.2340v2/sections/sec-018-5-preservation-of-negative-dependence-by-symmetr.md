---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-018-5-preservation-of-negative-dependence-by-symmetr
section_title: "Preservation of Negative Dependence by Symmetric Exclusion Processes"
section_number: 5
pages: 31-33
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.819
latex_coverage_ratio: 0.983
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{n-s6}

In this section we study some consequences of the results in \S 
\ref{s-stable} for symmetric exclusion processes and provide an answer to
the problem of finding a natural negative dependence 
property that is preserved by such evolutions (Problem~\ref{p-see}).

Let us first describe these processes in more detail. A configuration of 
particles on a countable set $S$ is a point
$\eta$ on the Boolean lattice $2^S$, which we identify with $\{0,1\}^S$, so 
$\eta(i)=1$ means that site $i$ is occupied, while $\eta(i)=0$ means that it 
is vacant. One is given a non-negative symmetric kernel 
$Q=(q_{i,j})_{i,j\in S}$ satisfying
\begin{equation}\label{eq-1-l}
\sup_i\sum_jq_{i,j}<\infty.
\end{equation}
The corresponding exclusion process $\eta_t$ is the Markov process on 
$\{0,1\}^{S}$ in which
$\eta\rightarrow \tau_{i,j}(\eta)$ at rate $q_{i,j}$, where $\tau_{i,j}$ 
is the transposition
that interchanges the coordinates $\eta(i)$ and $\eta(j)$. Note that if
$\eta(i)=\eta(j)$ (i.e., the two sites are both occupied or both empty), 
this transposition has no effect,
while if $\eta(i)\neq\eta(j)$, the transposition has the effect of moving the
particle from
the occupied site to the vacant site. In the language of semigroups and 
generators, the
semigroup $T(t)$ on $C(\{0,1\}^S)$ defined by 
$T(t)F(\eta)=E^{\eta}F(\eta_t)$ has generator
$$\mathcal{L}F(\eta)=\frac 12\sum_{i,j}q_{i,j}[F(\tau_{i,j}(\eta))-F(\eta)]$$
for functions $F$ that depend on finitely many coordinates. Condition 
\eqref{eq-1-l} guarantees
that the process is well defined and uniquely determined by $Q$.

One can give a more probabilistic description of the symmetric exclusion 
process in
terms of Poisson processes.
Recall that a Poisson process $N(t)$ with rate $\lambda>0$ is a random 
increasing step
function with jumps of size one, in which the times between jumps are 
independent
exponentially
distributed random variables $\tau_k$ with parameter $\lambda$:
$P(\tau_k>t)=e^{-\lambda t}$.
Now take a collection $N_{i,j}(t)$ of independent Poisson processes indexed by
unordered pairs $i,j$ --
$N_{i,j}(t)$ with rate $q_{i,j}$ -- and apply the transposition 
$\tau_{i,j}$ to
$\eta$ at the jump times of
$N_{i,j}(t)$. We will denote probabilities for the process with initial
configuration $\eta$ by $P^{\eta}$.

Negative correlation inequalities have played an important role in the
development of the theory of symmetric exclusion processes. For example,
Proposition 1.7 of \cite[Chap.~VIII]{L0} implies that
\begin{equation}\label{eq-2-l}
P^{\eta}(\eta_t\equiv 1 \text{ on } A)\leq\prod_{i\in
A}P^{\eta}(\eta_t(i)=1),\quad A\subseteq S.
\end{equation}
This inequality was used in an essential way in the characterization of 
stationary distributions
of the process, see Theorem 1.44 in {\em op.~cit} and the end of
this section. Inequality 
\eqref{eq-2-l} was generalized by Andjel in \cite{An} to
\begin{equation}\label{eq-3-l}
\begin{split}
&P^{\eta}(\eta_t\equiv 1\text{ on }A\cup B)\leq P^{\eta}(\eta_t\equiv 1
\text{ on
}A)P^{\eta}(\eta_t\equiv
1\text{ on } B),\\ 
&A,B\subseteq S,\, A\cap B=\emptyset,
\end{split}
\end{equation}
and used to prove an ergodic theorem. For further applications of correlation
inequalities in this
setting, see the references and discussion in \cite{L2}.

In that paper, one of us conjectured that the distribution of $\eta_t$ at 
time $t$ with deterministic initial configuration
$\eta$ is negatively associated. Even the special case
\begin{equation}\label{eq-4-l}
\begin{split}
&P^{\eta}(\eta_t\equiv 1\text{ on }A,\eta_t\equiv 0\text{ on }B)\geq
P^{\eta}(\eta_t\equiv 1\text{ on
}A)P^{\eta}(\eta_t\equiv 0\text{ on } B),\\ 
&A,B\subseteq S,\,A\cap B=\emptyset
\end{split}
\end{equation}
remained open (note that in \eqref{eq-4-l}, one of the events is increasing
while the other is decreasing). 
Surprisingly, despite the similarity between \eqref{eq-3-l} and 
\eqref{eq-4-l}, 
neither the proof of \eqref{eq-3-l} in \cite{An}, nor a somewhat
different one given in \cite{L2}, extends to prove \eqref{eq-4-l}. 
We are now able to prove this conjecture, see Theorem~\ref{th-Lig} below. 
The latter is actually a consequence of a yet stronger property for finite
 symmetric exclusion processes that we will now establish.

\begin{proposition}\label{prop-lig}
Suppose that $S$ is finite and the initial distribution
$\eta_0$ 
of a symmetric exclusion process on $\{0,1\}^S$ is strongly Rayleigh.
Then so is the distribution of $\eta_t$ for all $t> 0$.
\end{proposition}

\begin{proof}  
First, we observe that it suffices to prove the statement in case
$q_{i,j}\neq 0$ for only one
pair $i,j$.  To see this, suppose $T_1(t)$ and $T_2(t)$ are semigroups for 
finite state Markov chains
on the same state space with generators $\mathcal{L}_1$ and $\mathcal{L}_2$ 
respectively, and let $T(t)$ be the semigroup
with generator $\mathcal{L}_1+\mathcal{L}_2$. The Trotter product formula 
(see \cite[p.~33]{EK}) gives
$$T(t)=\lim_{n\rightarrow\infty}\big[T_1(t/n)T_2(t/n)\big]^n.$$
It follows that if a closed set of probability measures $\mathcal{M}$ on 
the state space has the property 
that $\mu\in \mathcal{M}$ implies $\mu T_i(t)\in \mathcal{M}$ for $i=1,2$ 
and $t>0$, then 
$\mu\in\mathcal{M}$ implies $\mu T(t)\in \mathcal{M}$ for $t>0$.
Now write the generator of the symmetric exclusion process as the following 
sum, corresponding to transitions at individual pairs of sites:
$$\mathcal{L}=\sum_{i,j}\mathcal{L}_{i,j},$$
where
$$\mathcal{L}_{i,j}F(\eta)=\frac 12q_{i,j}[F(\tau_{i,j}(\eta))-F(\eta)].$$
Repeated application of the preceding observation with $\mathcal{M}=$ the 
set of probability measures on
$\{0,1\}^S$ with stable generating polynomials, implies that the statement of 
the proposition
is correct for the process with generator $\mathcal{L}$ if it is correct for 
the process with generator $\mathcal{L}_{i,j}$ for each $i,j$. 

In the case of a single non-zero $q_{i,j}$, the generating
polynomial of the distribution of $\eta_t$ is given by $\alpha
f(z)+(1-\alpha)f(\tau_{i,j}(z))$, where
$\alpha=f(N_{i,j}(t)\text{ is even})$ and $f$ is the generating polynomial
for the initial distribution. Therefore, the result follows from 
Theorem~\ref{asym}.
\end{proof}

Recall from \S \ref{s240} that if $S$ is a 
countably infinite set, a probability measure on
$\{0,1\}^S$ is strongly
Rayleigh if every projection onto a finite subset of $S$ is strongly Rayleigh. 
Note that this property is preserved by weak convergence of measures. 

\begin{theorem}\label{th-Lig}
Suppose that $S$ is countable and the initial distribution $\eta_0$ of a 
symmetric exclusion process 
on $\{0,1\}^S$ is strongly Rayleigh. Then the distribution of $\eta_t$ is 
strongly Rayleigh, and hence CNA+, for all $t>0$.
\end{theorem}

\begin{proof} 
Since stability (the strongly Rayleigh property) implies
negative association by Theorem~\ref{stab-NA}, the result follows from 
Proposition~\ref{prop-lig} when $S$ is finite. 
For general $S$, approximate the exclusion process on $S$ by processes on 
finite subsets $S_n$ of
$S$ that increase to $S$, by taking the transposition rates for the process 
on $S_n$ to be $q_{i,j}$ if
$i,j\in S_n$ and zero otherwise. By the Trotter-Kurtz semigroup convergence 
theorem (see \cite[p.~28]{EK}), the
processes on $S_n$ converge to the process on $S$, so the result holds on 
$S$ as well. (See \cite[\S I.3]{L0} for details.) 
\end{proof}

\begin{remark}\label{prod-meas}
In particular, Theorem \ref{th-Lig} proves Conjecture \ref{con-lig} and shows 
that its conclusion remains valid if the initial configuration is a 
product measure (since any such measure is obviously strongly Rayleigh, 
cf.~Definition \ref{d-prod-m} and \S \ref{s240}).
\end{remark}

We conclude this section with an application of Theorem~\ref{th-Lig} 
to the extremal stationary
distributions for an irreducible
symmetric exclusion process. Theorem~1.44 of \cite[Chap.~VIII]{L0} states
that these
are exactly $\{\mu_{\alpha}:\alpha\in \mathcal{H}\}$, where 
\begin{itemize}
\item[(a)] $\mathcal{H}=\left\{\alpha:S\rightarrow [0,1] : 
\sum_jq_{i,j}[\alpha(j)-\alpha(i)]=0\text{ for each }i\right\}$ are the
harmonic functions for $Q$ with values in $[0,1]$, and 
\item[(b)] $\mu_{\alpha}=\lim_{t\rightarrow\infty}\nu_{\alpha}T(t)$, 
where $\nu_{\alpha}$ is the product measure on $\{0,1\}^S$ satisfying 
$$\nu_{\alpha}\{\eta:\eta\equiv 1\text{ on }A\}=\prod_{i\in A}\alpha(i),\quad
A\subseteq S.$$
\end{itemize} 
Very little is known about $\mu_{\alpha}$ other than 
\begin{itemize}
\item[(I)] 
$\mu_{\alpha}=\nu_{\alpha}$ if and only if $\alpha$ is constant, and 
\item[(II)] 
$\mu_{\alpha}\{\eta:\eta(i)=1\}=\alpha(i)$ for each $i\in S$. 
\end{itemize}
As a consequence of Theorem~\ref{th-Lig}, we can now add
\begin{itemize}
\item[(III)] 
$\mu_{\alpha}$ is negatively associated for each $\alpha\in\mathcal{H}$. 
\end{itemize}

\begin{remark}\label{r-lig-21}
If $q_{i,j}>0$ for all $i,j$, then as we noted in \S \ref{ss-ex-case} 
the limiting distribution of $\eta_t$ as
$t\to\infty$ is the symmetrization of the initial distribution. In 
\S \ref{s-countex} we construct examples of measures in $\fP_{n}$, 
$n\ge 20$, that are CNA+ but do
not have ULC rank sequences. By Theorem~\ref{pro-w} in \S \ref{ss-ex-case}, 
these counterexamples
to Conjectures~\ref{c-p}--\ref{cna-ulc} show that none of 
the properties NLC, h-NLC, Rayleigh/h-NLC+, CNA, CNA+ is preserved by the
symmetrization procedure \eqref{sym}, and by \cite[Theorem 3.2]{L2}, the same
can be said about the NA property. Therefore, the analog of 
Proposition~\ref{prop-lig} fails for all the aforementioned properties.
\end{remark}

\begin{remark}\label{r-lig-2}
The analog of Theorem~\ref{th-Lig} for asymmetric exclusion processes is 
false. A simple example is
obtained by taking $S=\{1,2\}$ in which only transitions from state 1 to 
state  2 are allowed. If the initial
distribution gives probability $\frac 14$ to each of the configurations in
$\{0,1\}^S$, then
the limiting distribution as $t\to\infty$ is given by 
$\mu(\{11\})=\mu(\{00\})=\frac14$,
$\mu(\{10\})=0$, and $\mu(\{01\})=\frac 12$. This measure is not NA.
\end{remark}
