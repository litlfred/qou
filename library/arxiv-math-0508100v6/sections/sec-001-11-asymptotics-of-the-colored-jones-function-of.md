---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-001-11-asymptotics-of-the-colored-jones-function-of
section_title: "Asymptotics of the colored Jones function of a knot"
section_number: 1.1
pages: 2-4
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.954
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.asymptotics}

To a knot $K$ in 3-space, one can associate a sequence of Laurent polynomials
$$
J_{K,n}(q) \in \BZ[q^{\pm 1}]
$$
for $n \in \BN=\{1,2,3,\dots\}$. $J_{K,1}(q)=1$ and
$J_{K,2}(q)$ is the famous {\em
Jones polynomial} of $K$ introduced by Jones in \cite{J}, and
$J_{K,n}(q)$ are roughly speaking the Jones polynomials of
$(n-1)$-parallels of the knot. More precisely, $J_{K,n}(q)$ is the
{\em quantum group} invariant of $K$ using the $n$-dimensional
irreducible $\mathfrak{sl}_2(\BC)$ representation, normalized by
$J_{\text{unknot},n}(q)=1$ for all $n$; see \cite{RT,Tu}. The
sequence $\{J_{K,n}(q)\}_n$ is often called the {\em
colored Jones function} of the knot $K$.

The paper is concerned with the asymptotic growth of the colored Jones
function. More precisely, fix a knot $K$ and consider the sequence
of holomorphic functions:

\begin{equation*}
 f_{K,n}:\BC \longto \BC, \quad
f_{K,n}(z):=J_{K,n}(e^{z/n})
\end{equation*}
for $n \in \BN$. In other words, we are evaluating the $n$-th polynomial
$J_{K,n}(q)$ at a complex $n$-th root of $e^{z}$.
We will be concerned with strong and weak
convergence of the sequence $f_{K,n}$, for $n \in \BN$. Let us
explain what we mean by that. Fix an open subset $U$ of $\BC$
containing 0.

\begin{definition}
\lbl{def.strongweak} {\rm(a)} A sequence of holomorphic functions
$f_n: U \longto \BC$ {\em strongly converges in $U$} to a
holomorphic function $f: U \longto \BC$ (and write
$\slim_{n\to\infty} f_n(z)=f(z)$) if $f_n(z)$ converges to $f(z)$
uniformly   on any compact subset
of $U$. \\
{\rm(b)} A sequence of holomorphic functions $f_n: U \longto \BC$
{\em weakly converges} to a holomorphic function $f: U \longto \BC$
(and write $\wlim_{n\to\infty} f_n(z)=f(z)$) if the Taylor series of
$f_n(z)$ at $z=0$ coefficient-wise converges to the Taylor series of
$f(z)$. In other words, for every $k \geq 0$, we have:
$$
\lim_{n\to\infty} \frac{d^k f_n}{dz^k}\Big|_{z=0}
= \frac{d^k f}{dz^k}\Big|_{z=0}.
$$
\end{definition}

It is easy to see that strong convergence of holomorphic functions
implies weak convergence. The converse is not true (see however, Lemma
\ref{lem.complex} below).

The Melvin-Morton-Rozansky (MMR, in short) Conjecture, which was
settled by Bar-Natan and the first author in \cite{B-NG}, compares
the function $f_{K,n}$ of a knot $K$ with the {\em Alexander
polynomial} $\D_K$ of $K$, normalized by $\D_K(t^{-1})= \D_K(t)$ and
$\D_K(1)=1$.


\begin{theorem}{\rm (The MMR conjecture)}
\lbl{thm.MMR}\cite{B-NG}
For every knot $K$ we have
\begin{equation*}
\wlim_{n \to \infty} \,\, f_{K,n}(z) = \frac{1}{\D_K(e^{z})} .
\end{equation*}
\end{theorem}

Our sample result is the following  analytic form of the MMR
Conjecture, which has application in the Generalized Volume
Conjecture.

\begin{theorem}
\lbl{thm.11} {\rm (Proof in Section \ref{sub.complex})}
For every knot $K$ there exists an open neighborhood
$U_K$ of $0 \in \BC$ such that in $U_K$, we have
\begin{equation*}
\slim_{n\to\infty} f_{K,n}(z)=\frac{1}{\D_K(e^{z})}.
\end{equation*}
\end{theorem}

Given Theorem \ref{thm.11} one may ask for a full asymptotic
expansion of  $f_{K,n}(z)$ in terms of powers of $1/n$. In order to
formulate our results, let us introduce the notion of strong and
weak asymptotic expansions.

\begin{definition}
\lbl{def.ass} Fix an open set $U$ of $\BC$, and holomorphic
functions $f_n:U \longto \BC$ and $R_n: U \longto \BC$.
\newline
\rm{(a)} We will say
that the sequence $f_n$ is {\em strongly asymptotic in $U$} to the
series $ \sum_{k=0}^\infty R_k(z) \left(\frac{z}{n}\right)^k $, and
write
\begin{equation}
\lbl{eq.defstrongass}
f_n(z) \sim^s_{n \to \infty}
\sum_{k=0}^\infty
R_k(z) \left(\frac{z}{n}\right)^k
\end{equation}
if for every $N \geq 0$ we have:
\begin{equation}
\lbl{eq.assstrong}
\slim_{n\to\infty}
\left( \frac{n}{z} \right)^{N} \left(
f_n(z)-\sum_{k=0}^{N-1}
R_k(z) \left(\frac{z}{n}\right)^k
\right)=R_{N}(z).
\end{equation}
\rm{(b)}
Likewise, we will say
that the sequence $f_n$ is {\em weakly asymptotic in $U$} to the
series $ \sum_{k=0}^\infty R_k(z) \left(\frac{z}{n}\right)^k $, and
write
\begin{equation}
\lbl{eq.defweakass}
f_n(z) \sim^w_{n \to \infty}
\sum_{k=0}^\infty
R_k(z) \left(\frac{z}{n}\right)^k
\end{equation}
if for every $N \geq 0$ we have:
\begin{equation}
\lbl{eq.assweak}
\wlim_{n\to\infty}
\left( \frac{n}{z} \right)^{N} \left(
f_n(z)-\sum_{k=0}^{N-1}
R_k(z) \left(\frac{z}{n}\right)^k
\right)=R_{N}(z).
\end{equation}
\end{definition}

Usually, sequences of holomorphic functions $f_n(z)$ do not have
asymptotic expansions (or even a limit, as $n \to \infty$). However,
sequences that appear in perturbative expansions of {\em Quantum
Field Theory} are generally expected to have asymptotic expansions.
In fact asymptotic expansions are generally easier to define (via
{\em Feynman diagram} techniques) than the partition functions
$f_{K,n}(z)$ themselves. Even when the partition functions can be
defined, the asymptotic expansions is a numerically useful way to
approximate them.



In \cite{Ro1},
Rozansky discovered that the sequence $f_{K,n}(z)$ has a weak asymptotic
expansion, where the terms are rational functions in the variable $e^z$.
More precisely, Rozansky proved the following result.

\begin{theorem}
\lbl{thm.Zrat}\cite{Ro1}
For every knot $K$ there exists a sequence  $P_{K,k}(q) \in \BQ[q^{\pm 1}]$
of Laurent polynomials with $P_{K,0}(q)=1$ such that
\begin{equation}
\lbl{eq.Zrat}
f_{K,n}(z) \sim_{n \to \infty}^w
\sum_{k=0}^\infty
\frac{P_{K,k}(e^{z})}{\D_K(e^{z})^{2k+1}} \left(\frac{z}{n}\right)^k .
\end{equation}
\end{theorem}

A different proof, valid for all simple Lie groups, was given in \cite{Ga1},
using work of \cite{GK}. Our result is strong version of Theorem
\ref{thm.Zrat}.

\begin{theorem}
\lbl{thm.1} {\rm (Proof in Section \ref{sub.thm1proof})}
For every knot $K$ there exists an open neighborhood
$\tilde U_K$ of $0 \in \BC$ such that in $ \tilde U_K$, we have
\begin{equation}
\lbl{eq.thm1}
f_{K,n}(z) \sim_{n \to \infty}^s \sum_{k=0}^\infty
\frac{P_{K,k}(e^{z})}{\D_K(e^{z})^{2k+1}}
\left(\frac{z}{n}\right)^k.
\end{equation}
\end{theorem}
