---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-030-verification-of-the-axioms-for-a-categorical-hol
section_title: "Verification of the axioms for a categorical holonomy"
section_number: null
pages: 34-37
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.98
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Let ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module and let ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ be the associated differential crossed module. Fix a smooth manifold $M$ with a base point $*$, a principal $G$-bundle $P$ over $M$ and an element $u\in P_*$, the fibre of $P$ over $*$. Consider a categorical connection $(\w,m)$ on $P$. Let us prove that the assignments $$[\g] \in \pi_1^1(M,*) \mapsto F^1_{(\w,u)}([\g]) \in G$$ and $$[\G] \in \P_2(M,*) \mapsto  F^2_{(\w,m,u)}([\G])  \in G \ltimes E,$$ defined in [\[dchcc\]](#dchcc){reference-type="ref" reference="dchcc"}, yield a categorical holonomy $F_{(\w,m,u)}\colon \Pc(M,*) \to \C(\Gc)$. To begin with, let us see that $F_{(\w,m,u)}$ defines a monoidal functor $\Pc_2(M,*) \to \C(\Gc)$. Here $\C(\Gc)$ is the categorical group constructed from $\Gc$; see [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}.

**Claim:** $F_{(\w,m,u)}$ is a functor.

::: Proof
Recall that the source and target maps in a category are denoted by $\sigma$ and $\tau$, respectively. Let $\G$ be a 2-path in $M$ such that $\d_l(\G),\d_r(\G)=*$. As usual put $\G(t,s)=\g_s(t); t,s \in [0,1].$ We have: $${\sigma\left (F^2_{(\w,m,u)}({[\G]})\right)=\sigma\left(g_{\g_0}^{-1},e_{{[\G]}} \right)= g_{\g_0}^{-1}={F_1\left(\sigma({[\G]})\right).}}$$ On the other hand by lemma [\[DDD\]](#DDD){reference-type="ref" reference="DDD"}: $$\tau\left (F^2_{(\w,m,u)}({[\G]})\right)=\tau\left(g_{\g_0}^{-1},e_{{[\G]}} \right)= \d(e_{{\G}}^{-1} )g_{\g_0}^{-1}= g_{\g_1}^{-1} ={F_1\left(\tau({[\G]})\right)}.$$ Therefore we can represent $F_{(\w,m,u)}$ as: $$\begin{CD} \d_u([\G]) \\ @AA [\G]A \\   \d_d([\G]) \end{CD} \in \Pc_2(M,*) \quad \longmapsto \quad \begin{CD}  g_{\g_1}^{-1}= \d(e_\G )^{-1}g_{\g_0}^{-1}\\ @AA {e_\G} A \\   g_{\g_0}^{-1} \end{CD} \in \C(\Gc) ,$$ where, as usual, $\G(t,s)=\g_s(t); s,t \in  [0,1]$.

Let $\G^1$ and $\G^2$ be 2-paths in $M$ with $\d_l(\G^1),\d_r(\G^1)=*$ and $\d_l(\G^2),\d_r(\G^2)=*$. Suppose also that $\d_u(\G^1)=\d_d(\G^2)$. For each $s,t \in [0,1]$, put $\G^1(t,s)=\g_s^1(t)$ and $\G^2(t,s)=\g_s^2(t)$. Let $\G=\G_1\circ_v \G_2$. Put $\G(t,s)=\g_s(t); s,t \in [0,1]$. Suppose $s \in [0,1/2]$. We have: $${\frac{d}{d s} e_\G(s)=e_\G(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt.}$$ By lemma [\[rescaling\]](#rescaling){reference-type="ref" reference="rescaling"}, $e_\G(1/2)=e_{\G^1}$. Let $e'_\G(s)= e_\G(1/2)^{-1} e_\G(s)$, where $s \in [1/2,1]$. Then: $${\frac{d}{d s} e'_\G(s) =e'_\G(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt.}$$ Since $e'_\G(1/2)=1_E$, it follows, by lemma [\[rescaling\]](#rescaling){reference-type="ref" reference="rescaling"}, that $e'_\G =e_{\G^2}$. Putting everything together yields $e_{\G} =e_{\G^1} e_{\G^2}$. Therefore we have: $$F^2_{(\w,m,u)}\left ( \begin{CD} \d_u([\G^2] )\\ @AA[\G^2] A\\  \d_d([\G^2])\\ @AA[\G^1] A\\ \d_d([\G^1]) \end{CD}\right)\quad =\quad  \begin{CD} F^1_{(\w,m,u)}\left (\d_u([\G^2] )\right)\\ @AAF^2_{(\w,m,u)}\big ([\G^2]\big) A\\ F^1_{(\w,m,u)}\big( {\d_u([\G^1])}\big)\\ @AAF^2_{(\w,m,u)}\big([\G^{{1}}]\big) A\\ F^1_{(\w,m,u)}\big(\d_d([\G^1])\big) \end{CD}$$ given any two elements $[\G^1]$ and $[\G^2]$ of $\P_2(M,*)$, with $\d_d(\G^2)=\d_u(\G^1).$

If we are given elements $[\G^1]$ and $[\G^2]$ of $\P_2(M,*)$, such that $\d_d([\G^2])=\d_u([\G^1]),$ then, for some representatives $\G_1^1 \in [\G^1]$ and $\G_1^2 \in [\G^2])$ we have $\d_d(\G^2_1)=\d_u(\G^1_1).$ For example, take a rank-1 homotopy $H$ connecting $\d_u(\G^1)$ with $\d_d(\G^2)$, and put $\G^1_1=\G^1 \circ_v H$ and $\G^2_1=\G^2$. Hence $F_{(\w,m,u)}\colon \Pc_2(M,*) \to \C(\Gc)$ is a functor.
:::

**Claim:** $F_{(\w,m,u)}$ is a monoidal functor.

::: Proof
Let $\G^1$ and $\G^2$ be 2-paths in $\P_2(M,*)$. Let also $\G=\G^1\circ_h \G^2$. Put $\G^1(s,t)=\g_s^1(t)$, $\G^2(s,t)=\g^2_s(t)$ and $\G(s,t)=\g_s(t)$. Here $s,t \in [0,1]$. We want to prove that $e_\G(s)=\left (g_{\g^1_0}^{-1} \tr {e_{\G^2}(s)}\right) e_{\G^1}(s)$ for any $s \in [0,1]$; see [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}. Note that this equation holds for $s=0$. Furthermore we have: $$\begin{aligned}
 \frac{d}{d s}& \left (\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s)\right) e_{\G^1}(s) \right)
\\
&=\Big (  g_{\g^1_0}^{-1} \tr \frac{d}{d s} e_{\G^2}(s)\Big) e_{\G^1}(s) +\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s)\right)  \frac{d}{d s}  e_{\G^1}(s) 
\\
 &{= \big (g_{\g^1_0}^{-1} \tr \Big (e_{\G^2}(s) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,u) } dt \Big) \Big)e_{\G^1}(s) }
\\
 &\quad \quad \quad \quad+\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s)\right) e_{\G^1}(s)  \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^1_s(t)},\t{\frac{\d}{\d s}\g^1_s(t)} \right)_{{\mathcal{H}}_\w(\g^1_s,t,u) } dt \\&=C_s+{{{D}}}_s.
\end{aligned}$$ Let us analyse each of the terms above separately: $$\begin{aligned}
C_s&=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s) \right ) \Big ( g_{\g^1_0}^{-1}\tr \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g ^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,u) } dt \Big)e_{\G^1}(s) 
\\
 &=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s) \right ) e_{\G^1}(s)\\ &\quad\quad\quad\quad\quad \Big (\big ( \d(e_{\G^1}(s))^{-1} g_{\g^1_0}^{-1} \big) \tr \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g ^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,u) } dt \Big) 
\\
&=\left (g_{\g^1_0}^{-1}\tr e_{\G^2}(s) \right)e_{\G^1}(s)\Big ( g_{\g^1_s}^{-1}  \tr \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,u) } dt \Big) .
\end{aligned}$$ Given that $m$ is $G$-equivariant, given $X,Y \in \X(M)$ we have: $$\label{Refer} 
{g^{-1}\tr m(\t{X},\t{Y})_v=m(\t{X}g,\t{Y}g)_{vg}=m(\t{X},\t{Y})_{vg}.}$$ Here $v \in P$ and $g \in G$. Therefore (recall $\g_s=\g^1_s\g^2_s$): $$\begin{aligned}
C_s&=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s) \right)e_{\G^1}(s) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,u)  g_{\g^1_s}  } dt  
\\
 &=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s) \right) e_{\G^1}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^2_s(t)},\t{\frac{\d}{\d s}\g^2_s(t)} \right)_{{\mathcal{H}}_\w(\g^2_s,t,ug_{\g^1_s}  )  } dt  
\\
 &=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s) \right) e_{\G^1}(s)\int_{1/2}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w(\g_s,t,u  )  } dt .
\end{aligned}$$ On the other hand $${{{D}}}_s=\left (g_{\g^1_0}^{-1} \tr e_{\G^2}(s)\right) e_{\G^1}(s)  \int_{0}^{1/2} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w({\g_s,t,u}) } dt.$$ Putting everything together it follows that: $$\begin{gathered}
 \frac{d}{d s} \left (\left (g_{\g^1_0}^{-1} \tr {e_{\G^2}(s)}\right) e_{\G^1}(s) \right) \\   =\left (g_{\g^1_0}^{-1} \tr e_{\G^2(s)}\right) e_{\G^1}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w({\g_s,t,u}) } dt .
\end{gathered}$$ Therefore $s \in [0,1] \mapsto \left (g_{\g^1_0}^{-1} \tr e_{\G^2(s)}\right) e_{\G^1}(s) \in E$ and $s \in [0,1] \mapsto  e_\G(s) \in E$ are both solutions of the same differential equation in $E$ and have the same initial condition.

In particular $\left (g_{\g^1_0}^{-1} \tr e_{\G^2 }\right) e_{\G^1}  = e_\G$. Therefore: $${
 F\left ( \begin{CD} \d_u([\G^1]) \\ @AA [\G^1]A \\   \d_d([\G^1]) \end{CD} \tn \begin{CD} \d_u([\G^2]) \\ @AA [\G^2]A \\   \d_d([\G ^2]) \end{CD} \right)=\begin{CD} g_{\g^1_1}^{-1} g_{\g^2_1}^{-1} \\ @AA \left (g_{\g^1_0}^{-1} \tr e_{\G^2 }\right) e_{\G^1} A \\g_{\g^1_0}^{-1}g_{\g^2_0}^{-1}  \end{CD}\quad \quad \quad \quad  =\begin{CD} F_1\big(\d_u([\G^1])\big) \\ @AA F_2([\G^1])A \\   F_1\big(\d_d([\G^1])\big) \end{CD} \quad \tn \begin{CD} F_1\big(\d_u([\G^2])\big) \\ @AA F_2\big([\G^2]\big)A \\   F_1\big(\d_d([\G^2])\big )\end{CD} \quad.}$$

We have therefore proven that $F_{(\w,m,u)}\colon \Pc_2(M,*) \to \C(\Gc)$ is a monoidal functor, and therefore a categorical group map.
:::

**Claim:** The functor $F_{(\w,m,u)}\colon \Pc_2(M,*) \to \C(\Gc)$ is smooth both on the sets $\pi_1^1(M,*)$ and $\P_2(M,*)$ of objects and morphisms of $\Pc_2(M,*)$.

::: Proof
This follows directly from the definition of $F_{(\w,m,u)}$, and from the lemma on page 74 of [@KN].
:::

The proof of theorem [\[FFF\]](#FFF){reference-type="ref" reference="FFF"} is complete.
