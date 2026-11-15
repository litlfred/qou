---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-006-5-sketch-of-the-algebraic-proof-of-theorem
section_title: "Sketch of the algebraic proof of Theorem ??"
section_number: 5
pages: 13-17
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.943
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
[]{#sec:alg_proof label="sec:alg_proof"}

This proof is organized around the following key diagram: $$\label{eqn:keydiagram}
    \begin{diagram}[size=2em]
        [[S^1 \cup S^1 \cup S^1, S^3]]  & \lTo & \mathcal H(3)  \\
        \dTo^g & & \dTo_{\mathcal G} \\
        [S^1 \times S^1 \times S^1, S^2] & \lTo & \pi_1\text{Maps}(S^1\times S^1,S^2)\\
    \end{diagram}
    \tag{$*$}$$ The left half represents the geometric-topological problem we are trying to solve, and is devoid of algebraic structure. The right half represents the algebraic structures that we impose on the left half via the two horizontal maps in order to solve the problem.

In the upper left corner of [\[eqn:keydiagram\]](#eqn:keydiagram){reference-type="eqref" reference="eqn:keydiagram"} we have the set of link-homotopy classes of three-component links in the 3-sphere $S^3$, and in the lower left corner the set of homotopy classes of maps of the 3-torus to the 2-sphere. The vertical map $g$ between them assigns to the link-homotopy class of $L$ the homotopy class of its characteristic map $g_L$. Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} describes $g$ and asserts that it is one-to-one.

In the upper right corner of [\[eqn:keydiagram\]](#eqn:keydiagram){reference-type="eqref" reference="eqn:keydiagram"} we have the group $\mathcal H(3)$ of link-homotopy classes of three-component string links. A $k$-component ***string link*** consists of $k$ oriented intervals embedded disjointly in a cube, with their tails on the bottom face, their tips on the top face directly above their tails, and their interiors in the interior of the cube. The terminology was coined by Habegger and Lin [@HabeggerLin]. The product of two $k$-component string links with endpoints in a common position is given by stacking the second one on top of the first. When a string link moves by a link homotopy, each strand is allowed to cross itself, while different strands must remain disjoint, just as for links. Then the above product induces a group structure on the set $\mathcal H(k)$ of link homotopy classes of $k$-component string links.

<figure id="fig:h3_generators">
<p><embed src="FigGen.pdf" style="height:2.08333in" /> (-225,77)<span><span class="math inline"><em>P</em></span></span> (-120,77)<span><span class="math inline"><em>Q</em></span></span> (-25,77)<span><span class="math inline"><em>R</em></span></span> (-80,29)<span><span class="math inline">=</span></span> (-175,29)<span><span class="math inline">=</span></span> (-165,-15)<span><span class="math inline"><em>P</em><em>Q</em><em>P</em><sup>−1</sup><em>Q</em><sup>−1</sup> = <em>B</em></span></span> (-263,7)<span><span class="math inline"><em>P</em></span></span> (-263,22)<span><span class="math inline"><em>Q</em></span></span> (-265,37)<span><span class="math inline"><em>P</em><sup>−1</sup></span></span> (-265,52)<span><span class="math inline"><em>Q</em><sup>−1</sup></span></span></p>
<figcaption>Generators for <span class="math inline">ℋ(3)</span></figcaption>
</figure>

Following Habegger and Lin, we derive the following presentation for $\mathcal H(3)$: $$\begin{aligned}
    \mathcal H(3) \ = \ \langle P, Q, R, B \ | \ &[P,Q] = [Q,R] = [R,P] = B, \\
    &[P,B] = [Q,B] = [R,B] = 1 \rangle
    \end{aligned}$$ The string links $P$, $Q$, $R$ and $B$ are those shown in Figure [1](#fig:h3_generators){reference-type="ref" reference="fig:h3_generators"}.

Using this presentation, elements of $\mathcal H(3)$ can be written uniquely in the form $$P^pQ^qR^rB^\mu  \ , \quad \text{for} \ p,q,r,\mu\in\mathbb Z.$$ Two elements $P^pQ^qR^rB^\mu$ and $P^{p^*}Q^{q^*}R^{r^*}B^{\mu^*}$ are conjugate if and only if $p = p^*$, $q = q^*$, $r = r^*$ and $\mu \equiv \mu^*$ mod $\gcd(p,q,r)$.

A string link $S$ can be closed up to a link $\widehat{S}$ by joining the tops of the strands to their bottoms outside the cube, without introducing any more crossings. For example, the closure of the three-component string link $B$ is the Borromean rings, as shown in Figure [2](#fig:B_closure){reference-type="ref" reference="fig:B_closure"}.

<figure id="fig:B_closure">
<p><embed src="FigBR.pdf" style="height:1.25in" /> (-103,40)<span><span class="math inline">=</span></span>(-125,7)<span><span class="math inline"><em>B̂</em></span></span></p>
<figcaption>The string link <span class="math inline"><em>B</em></span> closes up to the Borromean rings <span class="math inline"><em>B̂</em></span></figcaption>
</figure>

Thus the Borromean rings, a "primitive example" in the world of links, is the closure of a string link which is itself a commutator of simpler string links.

The closing-up operation descends to link homotopy classes and provides the upper horizontal map in [\[eqn:keydiagram\]](#eqn:keydiagram){reference-type="eqref" reference="eqn:keydiagram"}. It is easily seen that the closure of the string link $P^pQ^qR^rB^\mu$ has pairwise linking numbers $p$, $q$ and $r$ and Milnor invariant $\mu\mod{\gcd(p,q,r)}$. It follows that this closing-up map is onto. Furthermore, its point inverse images are the conjugacy classes in $\mathcal H(3)$, a special circumstance for links with three components which fails for four or more components.

In the lower right corner of [\[eqn:keydiagram\]](#eqn:keydiagram){reference-type="eqref" reference="eqn:keydiagram"} we have the union of the fundamental groups of the components of the space of continuous maps of the $2$-torus to the $2$-sphere, with one group $\pi_1 \text{Maps}_p(S^1 \times S^1, S^2)$ for each choice of degree $p$ of these maps. The work of Fox [@Fox] on torus homotopy groups (the case $p = 0$), and its generalization by Larmore and Thomas [@LarmoreThomas], provides explicit presentations for these groups: $$\begin{aligned}
    \pi_1\text{Maps}_p(S^1\times S^1,S^2)\ = \ \langle U_p, V_p, W_p \ | \ &[U_p,V_p] = W_p^2\,,\,W_p^{2p} = 1, \\
    &[U_p,W_p] = [V_p,W_p] = 1 \rangle
    \end{aligned}$$

Using this presentation, elements of $\pi_1\text{Maps}_p(S^1\times S^1,S^2)$ can be written uniquely in the form $$U_p^q\, V_p^r\, W_p^\nu  \ , \quad \text{for} \ q,r,\nu\in\mathbb Z\text{ with } 0 \leq \nu < 2|p|.$$ Two elements $U_p^q \, V_p^r \, W_p^\nu$ and $U_p^{q^*} V_p^{r^*} W_p^{\nu^*}$ are conjugate if and only if $q = q^*$, $r = r^*$ and $\nu \equiv \nu^*$ mod $2\gcd(p,q,r)$.

A direct argument using framed links shows how the generators $U_p$, $V_p$ and $W_p$ of $\pi_1\text{Maps}_p(S^1\times S^1,S^2)$ can be represented by specific maps $S^1 \times S^1 \times S^1 \to S^2$, all agreeing with some fixed map of degree $p$ on $* \times S^1 \times S^1$. In addition to this common feature, the representatives for $U_p$, $V_p$, $W_p$ have degrees $q = 1, 0, 0$ on $S^1 \times * \times S^1$, degrees $r = 0, 1, 0$ on $S^1 \times S^1 \times *$, and Pontryagin invariants $\nu = 0, 0, 1$ relative to the chosen basepoint for $\pi_1\text{Maps}_p(S^1\times S^1,S^2)$.

The lower horizontal map in the key diagram takes a homotopy class of based loops in the space $\text{Maps}(S^1\times S^1,S^2)$, ignores basepoints, identifies $S^1 \times S^1$ with $* \times S^1 \times S^1$, and then regards this class as a homotopy class of maps of $S^1 \times S^1 \times S^1 \to S^2$ in the usual way. In particular, the element $U_p^q \, V_p^r \, W_p^\nu$ of $\pi_1\text{Maps}_p(S^1\times S^1,S^2)$ is taken to a map with degrees $p$, $q$ and $r$ on the $2$-dimensional coordinate subtori, and -- *this is the key observation* -- with Pontryagin invariant $\nu$ mod $2\gcd(p,q,r)$ relative to the image of the basepoint map. This lower horizontal map is onto, and point inverse images are conjugacy classes in $\pi_1 \text{Maps}_p(S^1\times S^1,S^2)$.

The final step will be to define the vertical map $\mathcal G$ on the right side of the key diagram to make the whole diagram commutative, and to be a group homomorphism, insofar as possible. The hedge "insofar as possible" refers to the fact that we have a group $\mathcal H(3)$ in the upper right corner of the diagram, but only a union of groups $\pi_1 \text{Maps}_p(S^1 \times S^1, S^2)$ in the lower right corner. We deal with this disparity by demoting $\mathcal H(3)$ to a union of groups as follows.

Let $\mathcal H_0(3)$ denote the subgroup of $\mathcal H(3)$ consisting of string links with the second and third strands unlinked, and with presentation: $$\mathcal H_0(3) = \langle Q,R,B \ | \ [Q,R] = B\,,\,[Q,B] = [R,B] = 1 \rangle.$$ Consider the left cosets $\mathcal H_p(3) = P^p \mathcal H_0(3)$ of $\mathcal H_0(3)$, and convert each of them into a subgroup isomorphic to $\mathcal H_0(3)$ by using left translation to transfer the group structure from subgroup to coset. Adopting the notations $Q_p = P^p Q$, $R_p = P^p R$ and $B_p = P^p B$ for the generators of $\mathcal H_p(3)$ in this borrowed group structure, we get the presentation $$\mathcal H_p(3) = \langle Q_p, R_p, B_p \ | \ [Q_p,R_p] = B_p\,,\,[Q_p,B_p] = [R_p,B_p] = 1 \rangle.$$

We are now ready to define the vertical map $\mathcal G$ on the right side of [\[eqn:keydiagram\]](#eqn:keydiagram){reference-type="eqref" reference="eqn:keydiagram"} so as to make the whole diagram commutative, and at the same time to be a union of homomorphisms from the groups $\mathcal H_p(3)$ to the groups $\pi_1 \text{Maps}_p(S^1 \times S^1, S^2)$.

To do this, we start with specific string links to represent the elements of $\mathcal H_p(3)$. For purposes of illustration, we choose $p = 2$, and show in Figure [3](#fig:string_closed){reference-type="ref" reference="fig:string_closed"} the string links $1_2 = P^2$, $Q_2 = P^2 Q$ and $R_2 = P^2 R$, and under them the three-component links we get by closing them up.

<figure id="fig:string_closed">
<p><embed src="FigString.pdf" style="height:2.5in" /> (-215,100)<span><span class="math inline">1<sub>2</sub></span></span> (-110,100)<span><span class="math inline"><em>Q</em><sub>2</sub></span></span> (-5,100)<span><span class="math inline"><em>R</em><sub>2</sub></span></span> (-215,-0)<span><span class="math inline">$\widehat{1_2}$</span></span> (-110,0)<span><span class="math inline">$\widehat{Q_2}$</span></span> (-5,0)<span><span class="math inline">$\widehat{R_2}$</span></span></p>
<figcaption>Closing up the generators of <span class="math inline">ℋ<sub>2</sub>(3)</span></figcaption>
</figure>

The corresponding characteristic maps from $S^1 \times S^1 \times S^1 \to S^2$ all restrict to the same map of degree $2$ on $* \times S^1 \times S^1$, and therefore all three represent elements of the fundamental group $\pi_1\text{Maps}_2(S^1 \times S^1, S^2)$ based at this map. We denote these three images by $\mathcal G_2(P^2)$, $\mathcal G_2(P^2 Q)$ and $\mathcal G_2(P^2 R)$, with the intent of forcing commutativity in the key diagram. In fact, we can do this for all the string links $P^2 Q^q R^r B^\mu$, and a simple geometric argument shows that composition in the group $\mathcal H_2(3)$ carries over in this way to multiplication in the group $\pi_1 \text{Maps}_2(S^1 \times S^1, S^2)$.

Furthermore, a direct argument using framed links shows that the elements $\mathcal G_2(P^2 Q)$ and $\mathcal G_2(P^2 R)$ may serve as the elements $U_2$ and $V_2$ in the above presentation for $\pi_1\text{Maps}_2(S^1 \times S^1, S^2)$, so that $\mathcal G_2$ takes $P^2 Q$ to $U_2$ and $P^2 R$ to $V_2$. It then follows that $\mathcal G_2$ maps $P^2 B = [P^2Q, P^2R]$ to $[U_2,V_2] = W_2^2$.

The value $p = 2$ used above was just for purposes of illustration, and the corresponding results are true for all values of $p$. Thus we have defined the vertical map $\mathcal G$ on the right side of our key diagram to be a union of homomorphisms $\mathcal G_p :  \mathcal H_p(3) \to \pi_1\text{Maps}_p(S^1\times S^1,S^2)$ making the whole diagram commutative.

Now let $L$ be any three-component link in $S^3$ with pairwise linking numbers $p$, $q$ and $r$ and Milnor invariant $\mu$. Then $L$ is link homotopic to the closure of $P^p Q^q R^r B^\mu$. By commutativity of the key diagram, the homotopy class of the characteristic map $g_L$ is the image under the lower horizontal map of the element $\mathcal G_p(P^p Q^q R^r B^\mu) = U_p^q \, V_p^r \, W_p^{2\mu}$ of $\pi_1\text{Maps}_p(S^1\times S^1,S^2)$, and therefore has Pontryagin invariant $2 \mu$, as desired.

This completes our sketch of the algebraic proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.
