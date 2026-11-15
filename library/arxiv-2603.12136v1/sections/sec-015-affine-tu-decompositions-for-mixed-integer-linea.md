---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-015-affine-tu-decompositions-for-mixed-integer-linea
section_title: "Affine TU decompositions for mixed-integer linear programs"
section_number: null
pages: 44-45
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.967
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
We consider a mixed-integer linear program with variables $(x,y,z,\omega) \in \Z^{W^1} \times \Z^{W^2} \times \R^{W^3} \times \M^{W^4_I}$, where $W^4_I\subseteq W^4$ are the integer variables in $W^4$. We use $W_I = W^1 \cup W^2 \cup W^4_I$ to denote the integer variables and $W = W^1\cup W^2 \cup W^3 \cup W^4$ to denote all variables. The linear relaxation of the integer program is of the form: $$\begin{aligned}
    P \coloneqq \{A x + B y + C z = b,~ D x + E y + F \omega = g,~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \},
\end{aligned}$$ where $A \in \Z^{m_1\times W^1}$, $B\in \Z^{m_1\times W^2}$, $C\in \Z^{m_1\times W^3}$, $b\in \Z^{m_1}$, $D\in \Q^{m_2\times W^1}$, $E\in \Q^{m_2\times W^2}$, $F\in \Q^{m_2\times W^4}$ and $\ell \leq u$ hold, where $\ell$ and $u$ are rational vectors where we consider infinite entries to be integral. Any MILP can be brought into this form if we allow $m_1=0$ and $m_2=0$ to hold.

::: theorem
[]{#thm_atu_milp_integral label="thm_atu_milp_integral"} Suppose that for $k \leq |W^2|$, there exist matrices $S \in \Z^{m_1\times W^2}$, $U\in \Z^{m_1 \times k}$, $T\in \Z^{k \times W^2}$ and $R\in \Q^{m_2\times k}$ such that $B= S + U T$, $E=RT$ and $\begin{bmatrix}
    S & C\\
    T & \zerovec
\end{bmatrix}$ is totally unimodular and that $\ell,u \in \M^{W_I \cup W^3}$ holds. Then, for any $d = (d_{W^1}, d_T, d_{W^4_I}) \in \Z^{W^1} \times \Z^{k} \times \Z^{W^4_I}$, the affine fiber $H_d \coloneqq \{(x,y,z,\omega) \in P \mid x = d_{W^1},~ T y = d_T, ~\omega_{W^4_I} = d_{W^4_I} \}$ satisfies $$H_d = \mathrm{conv}(H_d \cap \M^{W_I}) = \mathrm{conv}(H_d \cap \M^{W_I \cup W^3}) \text{ and }$$ $$\mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P\cap\M^{W_I\cup W^3})  = \mathrm{conv}(\{(x,y,z,\omega)\in P \mid x\in \Z^{W^1},~T y \in \Z^k,~ \omega \in \M^{W^4_I} \})$$ holds.
:::

::: proof
*Proof.* We consider the affine fiber $H_d$ for any fixed $d\in \Z^{W^1} \times \Z^{k} \times \Z^{W^4_I}$ and rewrite it by substituting $B = S + U T$ and $D = R T$.

$$\begin{aligned}
      H_d \coloneqq& 
      \begin{aligned}[t]
          \{(x,y,z,\omega) \in \R^W \mid&~ A x + B y + C z = b,~ D x + E y + F \omega = g,~  x = d_{W^1},~ T y = d_T, \\&
       ~\omega_{W^4_I} = d_{W^4_I},~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \}
      \end{aligned}\\
      =& 
      \begin{aligned}[t]
          \{(x,y,z,\omega) \in \R^W \mid~&  x = d_{W^1},~ Sy + C z = b - A d_{W^1} - U d_{T},~ T y = d_T, \\
      &F \omega = g - D d_{W^1} - R d_T,~\omega_{W^4_I} = d_{W^4_I},~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \} 
      \end{aligned}\\
      = & \begin{aligned}[t]
      & \{x \in \R^{W^1} \mid x = d_{W^1}, ~\ell_{W^1} \leq x \leq u_{W^1} \} \times \\
      & \{\omega \in \R^{W^4} \mid F \omega = g - D d_{W^1} - R d_T, ~\omega_{W^4_I} = d_{W^4_I},~\ell_{W^4} \leq~ \omega \leq u_{W^4}\} \times \\
      &\{(y,z) \in \R^{W^2 \cup W^3} \mid Sy + C z = b - A d_{W^1} - U d_{T},~ T y = d_T, \ell_{W^2\cup W^3} \leq \transpose{\begin{bmatrix}
        y &
        z 
    \end{bmatrix}} \leq u_{W^2\cup W^3}\}
      \end{aligned}\\
    \coloneqq& H^{x}_d \times H^{\omega}_d \times H^{y,z}_d
    
\end{aligned}$$

In the third step, we use that $H_d$ can be rewritten as the Cartesian product of the three polyhedra $H^x_d \subseteq \R^{W^1}$, $H^{y,z}_d \subseteq \R^{W^2\cup W^3}$ and $H^\omega_d \subseteq \R^{W^4}$. Then since $\begin{bmatrix}
        S & C \\
        T & \zerovec
    \end{bmatrix}$ is totally unimodular and $\begin{bmatrix}
        b - A d_{W^1} - U d_{T} \\
        d_T
    \end{bmatrix}$ is integral by integrality of $b$, $U$, $A$ and $d$, and $\ell_{W^2\cup W^3}$ and $u_{W^2\cup W^3}$ are integral, $H^{y,z}_d$ is an integral polyhedron by Hoffman and Kruskal's theorem [@HoffmanK56]. Thus, we have $H^{y,z}_d = \mathrm{conv}(H^{y,z}_d \cap \Z^{W^2 \cup W^3}) = \mathrm{conv}(H^{y,z}_d \cap (\Z^{W^2} \times \R^{W^3}))$, where the last equality follows since $H^{y,z}_d \cap \Z^{W^2 \cup W^3} \subseteq H^{y,z}_d \cap (\Z^{W^2} \times \R^{W^3}) \subseteq H^{y,z}_d$ holds. This implies that $H_d = \mathrm{conv}(H_d \cap \M^{W_I}) = \mathrm{conv}(H_d \cap \M^{W_I \cup W^3})$ holds.

Then, note that $C$ is totally unimodular since it is a submatrix of $\begin{bmatrix}
        S & C \\
        T & \zerovec
    \end{bmatrix}$. Since $A$, $B$ and $b$ are integral and the variable bounds $\ell_{W^3}$ and $u_{W^3}$ of $z$ are integral we have by that the equation $\mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P \cap \M^{W_I \cup W^3})$ holds by [@VanDerHulst2025 Theorem 3]. Finally, using $\widehat{T} = \begin{bmatrix}
        I_{W^1} & \zerovec & \zerovec\\
        \zerovec & T & \zerovec \\
        \zerovec & \zerovec & I_{W^3_I}
    \end{bmatrix}$ as the matrix in [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref" reference="thm_affine_fiber_integral"} and the fact that $H_d = \mathrm{conv}(H_d \cap \M^{W_I})$ holds, we derive that $\mathrm{conv}(P \cap \M^{W_I})) = \mathrm{conv}(\{(x,y,z,\omega)\in P \mid x\in \Z^{W^1},~T y \in \Z^k,~ \omega \in \M^{W^4_I} \})$ holds. ◻
:::

There are a few key differences between [\[thm_atu_ilp_integral\]](#thm_atu_ilp_integral){reference-type="ref" reference="thm_atu_ilp_integral"} and [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} that make the latter more convenient to use. First of all, we do not require integrality of all of the right-hand sides, and we only need to construct an affine TU decomposition of a block in the constraint matrix rather than the complete matrix. Additionally, the $E=RT$ condition in [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} is new. This condition broadens the scope of the theorem, as otherwise, $D=\zerovec$ would have to hold to guarantee implied integrality in the affine fiber $H_d$ in the proof. Furthermore, during the detection we infer implied integrality for the continuous variables and have $\mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P\cap \M^{W_I\cup W^3})$.\
can be used directly to show that the condition [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref" reference="thm_milp_folding"} holds. For integer variables $W_I\subseteq W$ and an equitable partition $(\MP,\MQ)$ such that either $Q\cap W_I = \emptyset$ or $Q\subseteq W_I$ holds, let $\MQ^2 = \{Q \in \MQ_I \mid |Q| > 1\}$ and let $W^2 = W_B \cup \bigcup_{Q\in \MQ^2} Q$. Then, if the conditions of [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} hold for $T=(\transpose{\Pi_\MQ} \Lambda)_{\MQ',\star}$ for some subset $\MQ'\subseteq \MQ^2$, this directly shows condition [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref" reference="thm_milp_folding"} by using [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"}, and [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"} shows that we can recover integral solutions for the original model.
