---
doc_id: arxiv-2004.04939v1
doc_title: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF"
section_id: sec-004-5-conjectures
section_title: "Conjectures"
section_number: 5
pages: 8-9
source_pdf: 2004.04939v1.pdf
source_sha256: 59a06f9f7d97cad2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.861
doc_brief: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF — Let g0 be a simple Lie algebra of type ADE and let U ′ q(g) be the corre- sponding untwisted quantum aﬃne algebra."
---
Let $\uqpg$ be an arbitrary quantum affine algebra.
We say that a real simple module $L$ in $\catC^0_\g$ is a {\em root module} if
$\de(\dual^kM,M)=\delta(k=\pm1)$ for any $k$.

\Conj
For any root module $L\in\catC^0_\g$, there exists a monoidal autofunctor
$\Refl_L$ of $\cat$ which satisfies the following conditions:
\bna
\item $\Refl_L$ satisfies similar properties in
Theorem~\ref{thm:S_i(X)} and Theorem~\ref{thm: reflection by root modules}.
\item {\rm(Braid relation)}
For root modules $L$ and $L'$,
\be[{\rm(1)}]
\item 
if $\de(\dual^kL,L')=0$ for any $k\in \Z$, then
$$\Refl_L\circ\Refl_{L'}\simeq\Refl_{L'}\circ\Refl_{L},$$
\item
if $\de(\dual^kL,L')=\delta(k=0)$ for any $k\in \Z$, then
$$\Refl_L\circ\Refl_{L'}\circ\Refl_L\simeq\Refl_{L'}\circ\Refl_{L}\circ\Refl_{L'}.$$
\ee
\item 
Let $Q$ be a Q-data, and $L\seteq\F_Q(L(i))$.
Then the automorphism of $\Kt(\g)$ induced by $\Refl_L$ coincides with
$\brd_i$, i.e.,
the following diagram commutes:
$$\xymatrix{
\KT(\g_0)\ar[r]^\sim_{\iota_Q}\ar[d]_{\brd_i}&\Kt(\g)\ar[d]_{\Refl_L}\\
\KT(\g_0)\ar[r]^\sim_{\iota_Q}&\Kt(\g).
}$$
\ee
\enconj
