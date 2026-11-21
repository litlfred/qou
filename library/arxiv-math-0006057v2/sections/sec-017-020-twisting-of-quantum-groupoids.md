---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-017-020-twisting-of-quantum-groupoids
section_title: "Twisting of quantum groupoids"
section_number: 0.20
pages: 23-24
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.97
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
We describe the procedure of constructing new quantum groupoids by twisting a comultiplication. Twisting of Hopf algebroids without an antipode was developed in [@Xu] and a special case of twisting of $*$-quantum groupoids was considered in [@NV1].

::: definition
[]{#a twist label="a twist"} A *twist* for a quantum groupoid $H$ is a pair ($\Theta,\,{\bar \Theta}$), with $$\label{Theta and bTheta}
\Theta\in \Delta(1)(H\otimes_k H), \quad
{\bar \Theta}\in (H\otimes_k H)\Delta(1), \quad
\mbox { and } \quad
\Theta{\bar \Theta}= \Delta(1)$$ satisfying the following axioms : $$\begin{aligned}
(\varepsilon\otimes\mbox{id})\Theta = (\mbox{id}\otimes \varepsilon)\Theta 
&=& (\varepsilon\otimes\mbox{id}){\bar \Theta}= (\mbox{id}\otimes \varepsilon){\bar \Theta}= 1,
\label{eqn: twist eps} \\
(\Delta\otimes\mbox{id})(\Theta) (\Theta\otimes 1) &=&
(\mbox{id}\otimes \Delta)(\Theta) (1\otimes\Theta),
\label{eqn: twist ++}\\
({\bar \Theta}\otimes 1) (\Delta\otimes\mbox{id})({\bar \Theta}) &=&
(1\otimes {\bar \Theta}) (\mbox{id}\otimes \Delta)({\bar \Theta}),
\label{eqn: twist --}\\ 
(\Delta\otimes\mbox{id})({\bar \Theta}) (\mbox{id}\otimes \Delta)(\Theta)  &=&
(\Theta\otimes 1) (1\otimes {\bar \Theta}),  
\label{eqn: twist +-}\\
(\mbox{id}\otimes \Delta)({\bar \Theta}) (\Delta\otimes\mbox{id})(\Theta) &=&
(1\otimes\Theta) ({\bar \Theta}\otimes 1).
\label{eqn: twist -+}
\end{aligned}$$
:::

Note that for ordinary Hopf algebras the above notion coincides with the usual notion of twist and each of the four conditions ([\[eqn: twist ++\]](#eqn: twist ++){reference-type="ref" reference="eqn: twist ++"}) -- ([\[eqn: twist -+\]](#eqn: twist -+){reference-type="ref" reference="eqn: twist -+"}) implies the other three. But since $\Theta$ and ${\bar \Theta}$ are, in general, not invertible we need to impose all of them.

The next Proposition extends Drinfeld's twisting construction to the case of quantum groupoids.

::: proposition
[]{#twisting label="twisting"} Let ($\Theta,{\bar \Theta})$ be a twist for a quantum groupoid $H$. Then there is a quantum groupoid $H_\Theta$ having the same algebra structure and counit as $H$ with a comultiplication and antipode given by $$\Delta_\Theta(h) = {\bar \Theta}\Delta(h)\Theta, \qquad
S_\Theta(h) = v^{-1}S(h)v,
\label{eqn: theta}$$ for all $h\in H_\Theta$, where $v= m(S\otimes\mbox{id})\Theta$ is invertible in $H_\Theta$.
:::

::: proof
*Proof.* The proof is a straightforward verification, see [@EN] for details. ◻
:::

::: remark
[]{#rem: twist label="rem: twist"}

1.  One can check that the counital maps of the twisted quantum groupoid $H_\Theta$ are given by $$(\varepsilon_t)_\Theta(h) = \varepsilon(\Theta^{(1)}h)\Theta^{(2)}, \qquad
    (\varepsilon_s)_\Theta(h) = {\bar \Theta}^{(1)}  \varepsilon(h {\bar \Theta}^{(2)}).$$

2.  It is possible to generalize the above twisting construction by weakening the counit condition ([\[eqn: twist eps\]](#eqn: twist eps){reference-type="ref" reference="eqn: twist eps"}) and requiring only the existence of $u,w\in H$ such that $$\label{general eps twist}
    \varepsilon(\Theta^{(1)}w)\Theta^{(2)}= \Theta^{(1)}\varepsilon(\Theta^{(2)}w) = 1,
    \qquad
    \varepsilon(u {\bar \Theta}^{(1)}) {\bar \Theta}^{(2)}= {\bar \Theta}^{(1)}\varepsilon(u {\bar \Theta}^{(2)}) =1.$$ Then the counit of the twisted quantum groupoid $H_\Theta$ is $$\varepsilon_\Theta(h) = \varepsilon(uhw), \qquad h\in H.$$

3.  If $(\Theta,{\bar \Theta})$ is a twist for $H$ and $x\in H$ is an invertible element such that $\varepsilon_t(x)=\varepsilon_s(x)=1$ then $(\Theta^x,{\bar \Theta}^x)$, where $$\Theta^x =\Delta(x)^{-1}\Theta (x\otimes x) \quad \mbox{ and } \quad
    {\bar \Theta}^x = (x^{-1}\otimes x^{-1}){\bar \Theta}\Delta(x),$$ is also a twist for $H$. The twists $(\Theta,{\bar \Theta})$ and $(\Theta^x,{\bar \Theta}^x)$ are called *gauge equivalent* and $x$ is called a *gauge transformation*. Given such an $x$, the map $h\mapsto x^{-1}hx$ is an isomorphism between quantum groupoids $H_\Theta$ and $H_{\Theta^x}$.

4.  A twisting of a quasitriangular quantum groupoid is again quasitriangular. Namely, if $(\Theta,{\bar \Theta})$ is a twist and $({\mathcal R},{\bar {\mathcal R}})$ is a quasitriangular structure for $H$ then the quasitriangular structure for $H_\Theta$ is given by $({\bar \Theta}_{21}{\mathcal R}\Theta, {\bar \Theta}{\bar {\mathcal R}}\Theta_{21})$. The proof of this fact is exactly the same as for Hopf algebras.
:::

::: example
[]{#twisting of elementaries label="twisting of elementaries"} We will show that for every (non-commutative) separable algebra $B$ there is a family of quantum groupoid structures $H_q$ on the vector space $B^{op}\otimes B$ considered in ([@BSz2], 5.2) that can be understood in terms of twisting. Let $H=H_{1_B}$ be a quantum groupoid with the following structure operations : $$\Delta(b\otimes c) = (b\otimes e^{(1)}) \otimes (e^{(2)}\otimes c), \qquad
\varepsilon(b\otimes c) = \omega(bc), \qquad
S(b\otimes c) = c\otimes b,$$ for all $b,c\in B$, where $e =e^{(1)}\otimes e^{(2)}$ is the symmetric separability idempotent of $B$ and $\omega$ is defined by the condition $(\omega\otimes\mbox{id})e =1$. Note that $S^2=\mbox{id}$ and $H$, as an algebra, is generated by its counital subalgebras, i.e., it is dual to an *elementary* quantum groupoid of ([@NV1], 3.2).

Observe that the pair $$\Theta = (1\otimes e^{(1)}q^{-1}) \otimes (e^{(2)}\otimes 1)
\qquad
{\bar \Theta}= (1\otimes e^{(1)}) \otimes (e^{(2)}\otimes 1) = \Delta(1),$$ where $q$ is an invertible element of $B$ with $e^{(1)}q e^{(2)}=1$, satisfies ([\[eqn: twist ++\]](#eqn: twist ++){reference-type="ref" reference="eqn: twist ++"}) -- ([\[eqn: twist -+\]](#eqn: twist -+){reference-type="ref" reference="eqn: twist -+"}) and that conditions ([\[general eps twist\]](#general eps twist){reference-type="ref" reference="general eps twist"}) hold for $u=1$ and $w=q$. According to Proposition [\[twisting\]](#twisting){reference-type="ref" reference="twisting"} and Remark [\[rem: twist\]](#rem: twist){reference-type="ref" reference="rem: twist"}(b), these data define a twisting of $H$ such that the comultiplication and antipode of the twisted quantum groupoid are given by $$\Delta(b\otimes c) = (b\otimes e^{(1)}q^{-1}) \otimes (e^{(2)}\otimes c), \quad
\varepsilon(b\otimes c) = \omega(qbc),\quad
S(b\otimes c) = q^{-1}cq\otimes b,$$ for all $b,c\in B$. The target and source counital subalgebras of $H_q$ are $B^{op} \otimes 1$ and $1\otimes B$. The square of the antipode is implemented by $g_q =q\otimes q$. Since $\mbox{Ad}\,g_q$ is an invariant of $H_q$, this example shows that there can be uncountably many non-isomorphic semisimple quantum groupoids with the same underlying algebra (for noncommutative $B$).
:::
