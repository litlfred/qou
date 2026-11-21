---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-018-53-ribbon-knots-and-doubly-slice-knots
section_title: "Ribbon knots and doubly slice knots"
section_number: 5.3
pages: 16-17
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.99
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:ds}


A knot $K$ is called \emph{homotopy ribbon} if there exists a slice disk $D$ such that
$\pi_1(N_K)\to \pi_1(D^4\setminus \nu D)$ is surjective. Note that if a knot is ribbon, then it is also homotopy ribbon.
It is an open conjecture whether every knot that is slice is also homotopy ribbon.

Let $K\subset S^3$ be a knot. Recall that there exists a non--singular hermitian pairing
\[ \lambda:H_1(N_K;\mathbb{Z}[t^{\pm 1}])\times H_1(N_K;\mathbb{Z}[t^{\pm 1}])\to \mathbb{Q}(t)/\mathbb{Z}[t^{\pm 1}] \] which is referred to as the \emph{Blanchfield pairing}.
We say that $M\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])$ is a \mbox{metabolizer} for the Blanchfield pairing if $M=M^{\perp}$, i.e. if $M$ satisfies
\[ M=\{ x\in H_1(N_K;\mathbb{Z}[t^{\pm 1}]) \, |\, \lambda(x,y)=0 \in \mathbb{Q}(t)/\mathbb{Z}[t^{\pm 1}] \mbox{ for all }y\in M\}.\]
If $K$ is slice, then there exists a metabolizer for the Blanchfield pairing.
Also recall from the previous section that for any $k$ there exists a canonical isomorphism $H_1(N_K;\mathbb{Z}[t^{\pm 1}])/(t^k-1)=H_1(L_k;\mathbb{Z})$.
If $M$ is a metabolizer for the Blanchfield pairing, then for any $k$ we have that $M/(t^k-1)\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])/(t^k-1)=H_1(L_k;\mathbb{Z})$
is a metabolizer for the linking form $\lambda_k$.
We refer to \cite{Bl57}, \cite{Ke75}, \cite[Section~7]{Go78}, \cite{Let00} and \cite[Section~2.3]{Fr04} for more information.


The proof of Theorem \ref{thm:slice}  can now be modified along well established lines (cf. e.g. \cite[Theorem~8.3]{Fr04}) to prove the following theorem:

\begin{theorem}\label{thm:ribbon}
Let $K\subset S^3$ be a ribbon knot, then there exists a metabolizer $M\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])$ for the Blanchfield pairing $\lambda$
such that for any $k$ and any non--trivial character $\chi:H_1(L_{k};\mathbb{Z})\to S^1$ of prime power vanishing on $M/(t^k-1)$ we have
\[ \Delta_{N_K}^{\alpha(k,\chi)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_q])[t^{\pm 1}]=\mathbb{Q}(\zeta_q)[t^{\pm 1}]$.
\end{theorem}

Using \cite[Proposition~4.6]{Fr04}  one can show that if a knot $K$ satisfies the ribbon obstruction of Theorem \ref{thm:ribbon}, then it also satisfies the
sliceness obstruction given by Theorem \ref{thm:slicetensor}.


A knot $K\subset S^3$ is called \emph{doubly slice} if there exists an unknotted locally flat
two--sphere $S
\subset S^4$ such that
$S\cap S^3=K$.
Note that a doubly slice knot is in particular slice.






The ordinary Alexander polynomial does not contain enough information to distinguish between slice and doubly slice knots.
On the other hand twisted Alexander polynomials can detect the difference.
The following theorem is well--known to the experts. It can be proved using the above ideas
of Kirk and Livingston combined with the results of Gilmer and Livingston \cite{GL83} (cf. also \cite[Section~8.2]{Fr04}).
Note that many of the ideas already go back to the original paper by Sumners \cite{Sum71}.

\begin{theorem} \label{thm:doublyslice}
Let $K$ be a doubly slice knot. Then for any prime power $k$ there exist
two metabolizers $M_1$ and $M_2$ of $\lambda_k$ with $M_1\cap M_2=\{0\}$
such that for any odd prime power $n$ and any  character $\chi:H_1(L_k;\mathbb{Z})\to \mathbb{Z}/n\to S^1$ which vanishes either on $M_1$ or on $M_2$
we have
\[ \Delta_{N_K}^{\alpha(k,\chi)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_n])[t^{\pm 1}]$.
\end{theorem}

It is also possible to state and prove an analogue of Theorem \ref{thm:slicetensor} for doubly slice knots.
