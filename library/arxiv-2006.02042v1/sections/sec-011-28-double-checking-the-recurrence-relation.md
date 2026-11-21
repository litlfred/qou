---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-011-28-double-checking-the-recurrence-relation
section_title: "Double-checking the recurrence relation"
section_number: 2.8
pages: 9-10
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.906
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
Following \cite{CM}, for $Q\in \BC[t,M,x]$ we define $\left\langle  Q\right\rangle: \BZ \rightarrow \mathcal{R}=\BC[t^{\pm 1}]$ by
$$\left\langle Q \right\rangle(n):= [n]\sum^{n-1}_{k=0}P(t,t^{2n},t^{4k})\prod^{k}_{l=1}(t^{4n}+t^{-4n}-t^{4l}-t^{-4l})$$
for $n\geq 1$, and $\left\langle Q \right\rangle(-n)=-\left\langle Q \right\rangle(n)$ for $n\leq 0$.
It is known that the colored Jones polynomial of the figure eight knot is $J_E = \la 1 \ra$. 

For $Q, R\in \BC[t,M,x]$, we write $Q\equiv R$ if $Q-R\in \BC[t,M]$. Then we have the following.
\begin{lemma}\label{ALemma}
\begin{eqnarray*}
L\left\langle 1\right\rangle &\equiv& \left( t^{-2}M^{-4}-t^{-2}M^{-2}-t^2 \right)\left\langle 1\right\rangle 
+ \left( t^6M^2-t^2M^{-2} \right)\left\langle x\right\rangle,\\
L^2\left\langle 1\right\rangle &\equiv&
\big\{ 
t^{-12}M^{-8} 
- \left(t^{-12} + t^{-8}\right)M^{-6} 
- t^{12}M^4 - (t^{-4}+1)M^{-4}\\
&&  \qquad \qquad \,\,\, + \, \left(t^{-4} + 1\right)M^{-2} +t^8 + t^4 +1
\big\} \left\langle 1\right\rangle \\
&&  + \, \big \{
t^{16}M^6 - t^{-8}M^{-6} - t^{12}M^{4} + t^{-4}M^{-4} 
- \left(t^{12}+t^8+t^4 \right)M^2 \\
&&  \qquad \qquad \,\, + \,\left(t^4 + t^{-4} + 1\right)M^{-2}
\big \}\left\langle x\right\rangle, \\
L^{-1}\left\langle 1\right\rangle &\equiv&
\left( t^{-2}M^4 - t^{-2}M^2 -t^{2}\right)\left\langle 1\right\rangle
+\left(t^6M^{-2} - t^2 M^2 \right)\left\langle x\right\rangle, \\
L^{-2}\left\langle 1\right\rangle &\equiv&
\big\{
t^{-12}M^8 - \left(t^{-12} + t^{-8} \right)M^6 - t^{12}M^{-4} - \left(t^{-4} + 1\right)M^4\\
&& \qquad \qquad  + \,(t^{-4}+1)M^2 + t^{8} + t^4 +1
\big\}\left\langle 1\right\rangle\\
&& + \,  \big\{
t^{16}M^{-6} - t^{-8}M^6 - t^{12}M^{-4} + t^{-4}M^{4} - \left(t^{12}+t^8+t^4\right)M^{-2}\\
&& \qquad \qquad \,\,\,\,\, + \,\left(t^4+t^{-4}+1\right)M^{2}
\big\}\left\langle x\right\rangle.
\end{eqnarray*}
\end{lemma}
\begin{proof}
From \cite[Proposition 4.5]{CM} we have 
\begin{eqnarray*}
L\left\langle 1\right\rangle &\equiv& \left( t^{-2}M^{-4}-t^{-2}M^{-2}-t^2 \right)\left\langle 1\right\rangle 
+ \left( t^6M^2-t^2M^{-2} \right)\left\langle x\right\rangle, \\
L\la x \ra &\equiv& (t^{-2}M^{-2}-t^2M^2)\la 1 \ra +(t^6M^4-t^2M^2-t^2)\la x \ra.
\end{eqnarray*}
By a direct calculation, using the fact that $L^2\la 1 \ra=L(L\la 1 \ra)$ and the above formulas, we obtain the formula for $L^2\la 1 \ra$. The proofs for $L^{-1}\left\langle 1\right\rangle$ and $L^{-2}\left\langle 1\right\rangle$ are similar. 
\end{proof}

Using Lemma \ref{ALemma} and a direct calculation we see that
$$
(L^2 + L^{-2} + p_1(t,M)L + p_{-1}(t,M)L^{-1} +p_0(t,M)) \la 1 \ra \equiv 0.
$$
This means that $PJ_E\in \mathcal{R}[M^{\pm 1}]$.
