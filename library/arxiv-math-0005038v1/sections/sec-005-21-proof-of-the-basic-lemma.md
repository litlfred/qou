---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-005-21-proof-of-the-basic-lemma
section_title: "Proof of the Basic Lemma"
section_number: 2.1
pages: 4-6
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.953
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
[]{#BLEM label="BLEM"}

The problem is that one cannot necessarily define an algebraic intersection number between two properly embedded surfaces, since it might be possible to eliminate intersections by pushing them off to infinity. We overcome this problem by proving the existence of an immersed closed surface $\tilde{\Sigma}_2(F)$ which is equal to $(1-q)^2(1+qt)\tilde{\Sigma}(F)$ outside a small neighborhood of the punctures.

Let $F$ be a fork. Let the endpoints of $T(F)$ be $p_i$ and $p_j$. Let $\nu(p_i)$ and $\nu(p_j)$ be disjoint $\epsilon$-neighborhoods of $p_i$ and $p_j$ respectively such that $\nu(p_k) \cap P = \{p_k\}$ for $k=i,j$. Let $U$ be the set of $\{x,y\} \in C$ such that at least one of $x$ and $y$ lies in $\nu(p_i) \cup \nu(p_j)$. Fix a basepoint $u_0 = \{u_1,u_2\} \in U$, where $u_1 \in \nu(p_i)$ and $u_2 \in \nu(p_j)$. Let $\tilde{U}$ be the pre-image of $U$ in $\tilde{C}$. Choose a lift $\tilde{u}_0$ of $u_0$ to $\tilde{C}$. We start by analyzing $\pi_1(U,u_0)$.

<figure id="u">
<div class="picture">
<p>(280,130)(4,0)</p>
<p>(60,60) (55,125)<span><span class="math inline"><em>ν</em>(<em>p</em><sub><em>i</em></sub>)</span></span></p>
<p>(220,60) (215,125)<span><span class="math inline"><em>ν</em>(<em>p</em><sub><em>j</em></sub>)</span></span></p>
<p>(85,60)(105,40) (95,50)<span>(1,-1)<span>0</span></span> (95,50)<span><span class="math inline"><em>α</em><sub>1</sub></span></span></p>
<p>(105,40)(175,40) (140,40)<span>(1,0)<span>0</span></span> (138,33)<span><span class="math inline"><em>α</em><sub>2</sub></span></span></p>
<p>(175,40)(195,60) (185,50)<span>(1,1)<span>0</span></span> (174,52)<span><span class="math inline"><em>α</em><sub>3</sub></span></span></p>
<p>(195,60)(175,80) (185,70)<span>(-1,1)<span>0</span></span> (189,73)<span><span class="math inline"><em>β</em><sub>1</sub></span></span></p>
<p>(175,80)(105,80) (140,80)<span>(-1,0)<span>0</span></span> (140,85)<span><span class="math inline"><em>β</em><sub>2</sub></span></span></p>
<p>(105,80)(85,60) (95,70)<span>(-1,-1)<span>0</span></span> (86,75)<span><span class="math inline"><em>β</em><sub>3</sub></span></span></p>
<p>(60,60) (50,54)<span><span class="math inline"><em>p</em><sub><em>i</em></sub></span></span></p>
<p>(77,50)<span><span class="math inline"><em>u</em><sub>1</sub></span></span></p>
<p>(40,60)(40,80)(85,60) (40,60)(40,40)(85,60) (40,58)<span>(0,-1)<span>0</span></span> (30,58)<span><span class="math inline"><em>γ</em><sub>1</sub></span></span></p>
<p>(192,50)<span><span class="math inline"><em>u</em><sub>2</sub></span></span></p>
<p>(220,60) (223,56)<span><span class="math inline"><em>p</em><sub><em>j</em></sub></span></span></p>
<p>(195,60)(240,80)(240,60) (195,60)(240,40)(240,60) (240,62)<span>(0,1)<span>0</span></span> (241,58)<span><span class="math inline"><em>γ</em><sub>2</sub></span></span></p>
</div>
<figcaption>Arcs.</figcaption>
</figure>

Using the arcs shown in Figure [1](#u){reference-type="ref" reference="u"}, we define the following elements of $\pi_1(U,u_0)$. $$\begin{aligned}
a_1 &=& \{\gamma_1,u_2\},\\
a_2 &=& \{u_1,\gamma_2\},\\
b_1 &=& \{\alpha_1, \beta_1\beta_2\beta_3\}\{\alpha_2\alpha_3,u_1\},\\
b_2 &=& \{\alpha_1\alpha_2\alpha_3, \beta_1\}\{u_2,\beta_2\beta_3\}.
\end{aligned}$$ Note that $b_1$ and $b_2$ are homotopic in $C$, but not in $U$.

The following relations hold in $\pi_1(U)$. $$\begin{aligned}
\label{urel1}  {[}a_1,a_2] &=& 1,\\
\label{urel2}  {[}a_1,b_1 a_1 b_1] &=& 1,\\
\label{urel3}  {[}a_2,b_2 a_2 b_2] &=& 1.
\end{aligned}$$ The first of these is obvious. The second follows from the fact that $b_1 a_1 b_1$ is equal in $\pi_1(U)$ to $\{u_1,\delta\}$, where $\delta$ is a curve based at $u_2$ which passes counterclockwise around $p_1$ and $u_1$. The third follows by a similar argument.

We now analyze $\pi_1(\tilde{U},\tilde{u}_0)$. Let $i \colon\thinspace U \to C$ be the inclusion map and let $i_*$ be the induced map on fundamental groups. Then $\pi_1(\tilde{U})$ is the kernel of the map $\phi i_*$. We define the following elements of $\pi_1(\tilde{U},\tilde{u}_0)$. $$\begin{aligned}
a &=& a_2^{-1}a_1,\\
b &=& b_2^{-1}b_1,\\
c &=& a_1^{-1}b_1^{-1}a_1b_1,\\
d &=& a_2^{-1}b_2^{-1}a_2b_2.
\end{aligned}$$ If $x \in \pi_1(\tilde{U},\tilde{u}_0)$ and $y \in \pi_1(U,u_0)$ then the conjugate $x^y = y^{-1}xy$ is also an element of $\pi_1(\tilde{U},\tilde{u}_0)$. The following relations hold in $\pi_1(\tilde{U},\tilde{u}_0)$. $$\begin{aligned}
\label{Urel1}  a^{a_1} &=& a,\\
\label{Urel2}  c^{b_1 a_1} c &=& 1,\\
\label{Urel3}  d^{b_2 a_2} d &=& 1,\\
\label{Urel4}  dba^{b_1} &=& ab^{a_1}c.
\end{aligned}$$ To see this, rewrite these relations in terms of $a_1$, $a_2$, $b_1$ and $b_2$. The first three translate into equations ([\[urel1\]](#urel1){reference-type="ref" reference="urel1"}) to ([\[urel3\]](#urel3){reference-type="ref" reference="urel3"}). The fourth translates into a trivial identity.

If $x \in \pi_1(\tilde{U})$, let $[x]$ denote the corresponding element of $H_1(\tilde{U})$. Note that if $x \in \pi_1(\tilde{U})$ and $y \in \pi_1(U)$ then $[x^y] = \phi(y)^{-1}[x]$. The relations given in equations ([\[Urel1\]](#Urel1){reference-type="ref" reference="Urel1"}) to ([\[Urel4\]](#Urel4){reference-type="ref" reference="Urel4"}) give rise to the following relations in $H_1(\tilde{U})$. $$\begin{aligned}
\label{hrel1} (q^{-1}-1)[a] &=& 0,\\
\label{hrel2} (q^{-1}t^{-1}+1)[c] &=& 0,\\
\label{hrel3} (q^{-1}t^{-1}+1)[d] &=& 0,\\
\label{hrel4} (q^{-1}-1)[b] &=& (q^{-1}-1)[a] - [c] + [d].
\end{aligned}$$ Combining these relations, we obtain the following. $$(1-q)^2(1+qt) [b] = 0.$$

Let $[\tilde{\Sigma}(F)]$ be the element of $H_2(\tilde{C},\tilde{U})$ represented by $\tilde{\Sigma}(F)$. The long exact sequence of relative homology gives us the following exact sequence of $\Lambda$-modules $$H_2(\tilde{C}) \stackrel{j_*}{\to}
H_2(\tilde{C},\tilde{U}) \stackrel{\partial}{\to}
H_1(\tilde{U}).$$ But $\partial[\tilde{\Sigma}(F)] = [b]$. It follows that $$(1-q)^2(1+qt)[\tilde{\Sigma}(F)] = j_*[\tilde{\Sigma}_2(F)]$$ for some $[\tilde{\Sigma}_2(F)] \in H_2(\tilde{C})$ represented by some closed immersed surface $\tilde{\Sigma}_2(F)$.

Let $N$ be a noodle. Choose $\nu(p_i)$ and $\nu(p_j)$ small enough so as not to intersect $N$. Then $$(1-q)^2(1+qt) \langle N,F \rangle =
\sum_{a,b \in {\bf{Z}}}q^at^b(q^at^b\tilde{\Sigma}(N),\tilde{\Sigma}_2(F)).$$ Now $(q^at^b\tilde{\Sigma}(N),\tilde{\Sigma}_2(F))$ is the algebraic intersection number between a properly embedded surface and an immersed closed surface, so is well-defined.

Suppose $\sigma$ is an element of the kernel of the Lawrence-Krammer representation. Then $\sigma(\tilde{\Sigma}_2(F))$ and $\tilde{\Sigma}_2(F)$ represent the same element of homology, so have the same algebraic intersection with any $q^at^b\tilde{\Sigma}(N)$. Thus $\langle N,\sigma(F) \rangle = \langle N,F \rangle$.
