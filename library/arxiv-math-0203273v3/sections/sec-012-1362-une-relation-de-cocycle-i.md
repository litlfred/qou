---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-012-1362-une-relation-de-cocycle-i
section_title: "Une relation de cocycle, I"
section_number: 13.6.2
pages: 70-70
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.969
---
Supposons $r\ge
1$ et trouvée une famille $u_A^{(r)}$ vérifiant la condition (ii) du lemme [\[l4\]](#l4){reference-type="ref" reference="l4"}. Quitte à remplacer $s$ par $s_r$, on peut supposer $s_r=s$, $u^{(r)}=1$. On a donc $\tilde s_{A,B}\in 1+{\mathcal{R}}(A\bullet B)^r$ pour tout couple d'objets $(A,B)$. Posons $n_{A,B}=1_{A\bullet 
B}-\tilde
s_{A,B}\in{\mathcal{R}}(A\bullet B)^r$. La relation [\[coh1\]](#coh1){reference-type="eqref" reference="coh1"} se réécrit alors $$\begin{gathered}
(1_{A\bullet B\bullet 
C}-n_{A\bullet B,C})\circ ((1_{A\bullet
B}-n_{A,B})\bullet 
1_C)\\
=(1_{A\bullet B\bullet C}-n_{A,B\bullet C})\circ 
((1_A\bullet
(1_{B\bullet 
C}-n_{B,C}))
\end{gathered}$$ d'où $$\label{coc1}
n_{A\bullet B,C}+n_{A,B}\bullet 1_C\equiv n_{A,B\bullet C} 
+1_A\bullet
n_{B,C}\pmod{{\mathcal{R}}(A\bullet B\bullet 
C)^{r+1}}.$$

Nous cherchons une famille $(u_A^{(r+1)})_{A\in {\mathcal{A}}}$ vérifiant:

::: thlist
$u_A^{(r+1)}\equiv 1\pmod{{\mathcal{R}}(A)^r}$ pour tout $A\in{\mathcal{A}}$.

$u_{A\bullet B}^{(r+1)}\circ\tilde s_{A,B}\circ
(u_A^{(r+1)}\bullet 
u_B^{(r+1)})^{-1}\in 1+{\mathcal{R}}(A\bullet B)^{r+1}$ pour tout couple d'objets $(A,B)$.
:::

Supposons le problème résolu et posons $m_A=1_A-u_A^{(r+1)}\in
{\mathcal{R}}(A)^r$. On a alors l'identité $$\begin{gathered}
(1_{A\bullet B}-m_{A\bullet B})\circ 
(1_{A\bullet
B}-n_{A,B})\circ ((1_A-m_A)\bullet 
(1_B-m_B))^{-1}\\
\equiv 1\pmod{{\mathcal{R}}(A\bullet 
B)^{r+1}}
\end{gathered}$$ soit encore $$\label{cob1}
n_{A,B}\equiv m_A\bullet 1_B 
+1_A\bullet m_B -m_{A\bullet
B}\pmod{{\mathcal{R}}(A\bullet 
B)^{r+1}}.$$

Réciproquement, l'existence d'une famille $(m_A)$ vérifiant la congruence [\[cob1\]](#cob1){reference-type="eqref" reference="cob1"} est clairement équivalenteà l'existence d'une famille $(u_A^{(r+1)})$ comme ci-dessus.
