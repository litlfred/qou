---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-011-34-duality-for-twisted-invariants
section_title: "Duality for twisted invariants"
section_number: 3.4
pages: 9-10
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.953
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:duality}

Let   $R$ be a ring with a (possibly trivial) involution $r\mapsto \overline{r}$.
Let $F$ be a free abelian group, with its natural involution. We extend the involution on $R$ to the group ring $R[F]$ and the quotient field $Q(R[F])$ in the usual way.
We equip $R[F]^k$ with the
standard hermitian inner product $\langle v ,w \rangle=v^t\overline{w}$ (where we view elements in $R[F]^k$
as column vectors).

Let $N$ be a 3--manifold with empty or toroidal boundary
and let $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$ a representation.
We denote by  $\overline{\alpha} : \pi_1(N) \to \mbox{GL}(k,R[F])$  the representation given by
\[ \langle \alpha(g^{-1})v,w\rangle =\langle v,\overline{\alpha}(g)w\rangle \]
for all $v,w\in R[F]^k,g\in \pi_1(N)$. Put differently, for any $g\in \pi_1(N)$ we have
\[ \overline{\alpha}(g)= \overline{\left(\alpha(g)^{-1}\right)^t} \in \mbox{GL}(k,R[F]).\]
We say that a representation is \emph{unitary} if $\overline{\alpha}=\alpha$.


Note that if  $\psi:\pi_1(N)\to F$  is a non--trivial homomorphism to a free abelian group $F$
and  $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$  a representation, then
\[ \overline{\gamma \otimes \psi} = \overline{\gamma}\otimes \psi.\]

The following duality theorem can be proved using the ideas of \cite{Ki96} and \cite[Corollary~5.2]{KL99a}.

\begin{proposition}   \label{prop:dualitytau}
Let $N$ be a 3--manifold with empty or toroidal boundary and let $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$ a representation.
Then
\[ \overline{\tau(N,{\alpha})} \doteq  {\tau(N,\overline{a})}\in R[F].\]
In particular if  $\psi:\pi_1(N)\to F$  is a non--trivial homomorphism to a free abelian group $F$
and  $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$  is a unitary  representation, then $\tau(N,\gamma\otimes \psi)$ is reciprocal, i.e.
\[ \overline{\tau(N,\gamma\otimes \psi)}=\tau(N,\gamma\otimes \psi)\in R[F].\]
\end{proposition}

It is easy to see that in general the twisted Reidemeister torsion is not reciprocal if one considers representations
$\alpha$
such that  $\alpha(g)\ne \overline{\alpha(g)}$ for some $g\in \pi_1(N)$.
Hillman, Silver and Williams \cite{HSW09} give much more subtle examples which show that there also exist knots $K$
together with special linear representations such that the corresponding twisted Reidemeister torsion  is not reciprocal.

The following proposition follows from the discussion in \cite{FK06}.

\begin{proposition} \label{prop:dualitydelta}
Let $N$ be a closed 3--manifold  and let $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$ a representation with $R$  a  Noetherian UFD.
Assume that  $\Delta_{N,i}^{\alpha} \ne 0$ for all $i$. Then the following equalities hold:
\[ \overline{\Delta_{N,2}^{\alpha}}\doteq \Delta_{N,0}^{\overline{a}} \mbox{ and }  \overline{\Delta_{N}^{\alpha}}\doteq \Delta_{N}^{\overline{a}}.\]
\end{proposition}
