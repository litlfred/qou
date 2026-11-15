---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-005-24-haar-distributed-unitary-random-matrices-and
section_title: "Haar distributed unitary random matrices and the Weingarten function"
section_number: 2.4
pages: 6-7
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.981
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
In the following we will be interested in the asymptotics of special
matrix integrals over the group $\UU(N)$ of unitary $N\times
N$-matrices. We always equip the compact group $\UU(N)$ with its
Haar probability measure and accordingly distributed random matrices
we shall call \emph{Haar distributed unitary random matrices}. Thus
the expectation $\EE$ over this ensemble is given by integrating
with respect to the Haar measure.

The expectation of products of entries of Haar distributed unitary
random matrices can be described in terms of a special function on
the permutation group. Since such considerations go back to
Weingarten \cite{W}, Collins \cite{Col} calls this function the
Weingarten function and denotes it by $\Wg$. We will follow his
notation. In the following we just recall the relevant information
about this Weingarten function, for more details we refer to
\cite{Col,CS,X}.

We use the following definition of the Weingarten function. For
$\pi\in S_n$ and $N\geq n$ we put
$$\Wg(N,\pi)=
\EE \big(U_{11}\cdots
U_{nn}\overline{U}_{1\pi(1)}\cdots\overline{U}_{n\pi(n)}\big),
$$ where
$U=(U_{ij})_{i,j=1}^N$ is an $N\times N$ Haar distributed unitary
random matrix. Sometimes we will suppress the dependence on $N$ and
just write $\Wg(\pi)$. This $\Wg(N,\pi)$ depends on $\pi$ only
through its conjugacy class. General matrix integrals over the
unitary groups can be calculated as follows:
\begin{multline}
\EE\big(U_{i'_1j'_1}\cdots U_{i'_nj'_n}\overline U_{i_1j_1}
\cdots\overline U_{i_nj_n}\big) \\
= \sum_{\alpha,\beta\in S_n}
\delta_{i_1i'_{\alpha(1)}}\cdots \delta_{i_ni'_{\alpha(n)}}
\delta_{j_1j'_{\beta(1)}}\cdots\delta_{j_nj'_{\beta(n)}}
\Wg(\beta\alpha^{-1}).
\end{multline}

The Weingarten function is a quite complicated object, and its full
understanding is at the basis of questions around Itzykson-Zuber
integrals. For our purposes, only the behaviour of leading orders in
$N$ of $\Wg(N,\pi)$ is important. One knows (see, e.g.,
\cite{Col,CS}) that the leading order in $1/N$ is given by
$\vert\pi\vert+n$ and increases in steps of 2.

Let us use the following notation for the first two orders ($\pi\in
S(n)$):
$$\Wg(N,\pi)=\mu(\pi)N^{-(\vert \pi\vert +n)}+\phi(\pi)
N^{-(\vert\pi\vert+n+2)}+O\bigl(N^{-(\vert\pi\vert+n+4)}\bigr).$$

One knows that $\mu$ is multiplicative with respect to the cycle
decomposition, i.e.,
$$\mu(\pi_1\times\pi_2)=\mu(\pi_1)\cdot\mu(\pi_2).$$
The important part of the second order information is
contained in the leading order of
$\Wg(\pi_1\times\pi_2)-\Wg(\pi_1)\Wg(\pi_2)$, which is given by
$\mu_2(\pi_1,\pi_2) N^{-(|\pi_1| + |\pi_2| + m + n +2)}$ for
$\pi_1 \in S_m$ and $\pi_2 \in S_n$ and where
$$\mu_2(\pi_1,\pi_2):=
\phi (\pi_1\times\pi_2)-\mu(\pi_1)\phi(\pi_2)-
\phi(\pi_1)\mu(\pi_2).$$ Note that we have
$$\mu_2(\pi_1,\pi_2)=\mu_2(\pi_2,\pi_1).$$

Collins \cite{Col} has general counting formulas for the calculation
of $\mu$ and $\mu_2$ (and also higher order analogues); however, a
conceptual explanation of $\mu_2$ seems still to be missing. $\mu$
is the M\"obius function of the lattice of non-crossing
partitions (thus determined by Catalan numbers), and this fact
is quite well understood by the relation between $\mu$ and
asymptotic freeness of unitary random matrices. In a similar
way, one should get a conceptual understanding of $\mu_2$ by
the relation with second order freeness. In the present paper
we will not pursue further this direction, but we will come
back to it in forthcoming investigations. Here we will not
rely on the concrete values of
$\mu$ or $\mu_2$, but will only use the  basic
properties mentioned above.
