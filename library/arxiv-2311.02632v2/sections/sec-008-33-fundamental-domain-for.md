---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-008-33-fundamental-domain-for
section_title: "Fundamental domain for"
section_number: 3.3
pages: 12-19
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.972
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
It is worth noting that the motivation behind adopting the above action of $\Del$ is that it provides the classical tessellation of a fundamental domain, given as a regular 14-gon inside $\disk$, for the Klein quartic. This is illustrated in Figure [1](#fig:237_klein){reference-type="ref" reference="fig:237_klein"}.

![Tessellation of a fundamental domain for the Klein quartic](237_klein.png){#fig:237_klein width="50%"}

The main goal of this subsection is to determine an explicit fundamental domain for $\Gamma$. To achieve this, we will employ Poincaré's polyhedron theorem as presented by Maskit [@maskit1971]. Recall that a closed set $D$ is called a *fundamental domain* for a Fuchsian group $G$ if:

1.  No two distinct points of the interior of $D$ are equivalent under $G$, and

2.  Every point in $\disk$ is equivalent under $G$ to some point of $D$.

For an element $g = \pm \pmat{a}{b}{c}{d} \in \PSU(1,1)$ with $c \neq 0$, the *isometric circle* $I(g)$ of $g$ is defined by: $$I(g) = \{z \in \mathbb{C} : |cz + d| = 1\}.
\label{eq:isometric_circle}$$ As a Euclidean circle, its center is given by $-d / c$ and it has a radius of $1 / |c|$. On $I(g)$, $g$ acts as a Euclidean isometry. For $z\in \disk$, we have $$z\in I(g) \iff \distD(z, 0) = \distD(z, g^{-1} 0).
\label{eq:isometric_dist}$$ Furthermore, this defines a geodesic in $\disk$. This can be seen by considering the triangle with vertices at the center of $\disk$, the center of $I(g)$, and the intersection point of $I(g)$ with the unit circle. It turns out to be a right triangle. For further details on isometric circles, refer to [@MR0698777 Sections 4.1 and 7.36].

The *exterior* of $I(g)$, denoted by $\ext(I(g))$, is the subset of $\disk$ given by: $$\ext(I(g)) = \{z \in \disk : |cz + d| > 1\}.$$

::: lemma
Two isometric circles $I(\gamma_i)$ and $I(\gamma_j)$ with $i\neq j$ have a non-empty intersection within the unit disk $\disk$ if and only if $j = i\pm 1 \mod 42$, and each intersection consists of a single point.
:::

::: proof
*Proof.* By utilizing [\[eq:matrixA\]](#eq:matrixA){reference-type="eqref" reference="eq:matrixA"} and [\[eq:matrixB\]](#eq:matrixB){reference-type="eqref" reference="eq:matrixB"}, we derive an exact matrix expression for each $\gamma_i$. Applying [\[eq:isometric_circle\]](#eq:isometric_circle){reference-type="eqref" reference="eq:isometric_circle"}, we can algebraically determine the intersection of two distinct isometric circles, $I(\gamma_i)$ and $I(\gamma_j)$, within the unit disk $\disk$. Hence, this computation is straightforward and exact.

Whenever there is a non-empty intersection of $I(\gamma_i)$ and $I(\gamma_j)$ within the unit disk, it must consist of just one point. If two such isometric circles intersect at multiple points, then they must be identical as they are also geodesics in $\disk$. ◻
:::

A visual representation of the isometric circles, $I(\gamma_i)$, can be found in Figure [2](#fig:iso_circles){reference-type="ref" reference="fig:iso_circles"}.

![Isometric circles of $\gamma_i$](iso_circles.png){#fig:iso_circles width="90%"}

For each $i=1,\dots, 42$, let $v_i\in \disk$ be the unique point of the intersection $I(\gamma_i)\cap I(\gamma_{i-1})$, where we set $I(\gamma_{0}) = I(\gamma_{42})$ as before.

We define a compact subset $\F$ of the unit disk $\disk$ as the region bounded by the isometric circles $I(\gamma_i)$ for $1 \leq i \leq 42$: $$\F = \text{closure of }\bigcap_{1\leq i\leq 42} \ext(I(\gamma_i)).
\label{eq:Fdef}$$ Then $\F$ is a hyperbolic polygon with 42 sides with vertices $v_i, \, 1 \leq i \leq 42$. We denote the geodesic segment connecting $v_i$ and $v_{i+1}$ by $s_i$, hence a subset of $I(\gamma_i)$, and call it a *side* of $\F$. For a visual representation of $\F$, $s_i$ and $v_i$, refer to Figure [3](#fig:fricke_domain){reference-type="ref" reference="fig:fricke_domain"}.

![Hyperbolic polygon $\F$ and its vertices $\{v_i\}$](fricke_fundamental_domain.png){#fig:fricke_domain width="90%"}

We now consider a symmetry property of $\F$. It is evident that $b$, as defined in [\[eq:matrixB\]](#eq:matrixB){reference-type="eqref" reference="eq:matrixB"}, acts as a rotation around the origin by an angle of $2\pi/7$. We can express [\[eq:gamma_recursive\]](#eq:gamma_recursive){reference-type="eqref" reference="eq:gamma_recursive"} as $\gamma_{i} = b\gamma_{i-6}b^{-1}, \, i\in \Z$. Using the invariance property of isometric circles, $$I(hgh^{-1}) = h(I(g)),\, g,h \in \PSU(1,1),$$ we can establish the following:

::: prop
[]{#prop:Fsym label="prop:Fsym"} The polygon $\F$ is invariant under the action of the cyclic group of rotations generated by $b$.
:::

From , we have $$v_{j} = e^{2\pi \i /7}v_{j-6}.$$ Table [1](#tab:vcoor){reference-type="ref" reference="tab:vcoor"} provides the explicit coordinates of the points $v_j = x_j+  y_j\i$ for $1\leq j \leq 6$.

::: {#tab:vcoor}
   Coordinate   Numerical value  Minimal polynomial
  ------------ ----------------- ---------------------------------------------------------------------------------------------
     $x_1$         $-0.9809$     $-7 - 336 x^2 - 3584 x^4 + 4096 x^6$
     $y_1$         $-0.0246$     $-1 + 1648 x^2 + 5632 x^4 + 4096 x^6$
     $x_2$         $-0.9263$     $1 + 335 x^2 + 19055 x^4 + 96809 x^6 - 8896 x^8 - 376832 x^{10} + 262144 x^{12}$
     $y_2$         $-0.1277$     $49 - 5047 x^2 + 113631 x^4 + 688415 x^6 + 1331008 x^8 + 1032192 x^{10} + 262144 x^{12}$
     $x_3$         $-0.8900$     $28561 + 148889 x^2 + 119344 x^4 - 382383 x^6 - 445248 x^8 + 253952 x^{10} + 262144 x^{12}$
     $y_3$         $-0.2869$     $49 - 441 x^2 - 5096 x^4 + 20447 x^6 + 192192 x^8 + 401408 x^{10} + 262144 x^{12}$
     $x_4$         $-0.8944$     $-1183 - 2576 x^2 + 1792 x^4 + 4096 x^6$
     $y_4$         $-0.4034$     $-1 - 144 x^2 + 256 x^4 + 4096 x^6$
     $x_5$         $-0.7792$     $28561 + 116948 x^2 - 80583 x^4 - 471535 x^6 - 110144 x^8 + 454656 x^{10} + 262144 x^{12}$
     $y_5$         $-0.5170$     $49 + 980 x^2 + 3185 x^4 - 26593 x^6 - 78400 x^8 + 200704 x^{10} + 262144 x^{12}$
     $x_6$         $-0.6774$     $28561 + 51883 x^2 - 195334 x^4 - 389551 x^6 + 226304 x^8 + 684032 x^{10} + 262144 x^{12}$
     $y_6$         $-0.6446$     $49 + 1421 x^2 + 7938 x^4 - 4641 x^6 - 89600 x^8 - 28672 x^{10} + 262144 x^{12}$

  : Coordinates for $v_j = x_j+  y_j \i,\, 1 \leq j \leq 6$
:::

For every side $s$ of $\F$, there exists a corresponding side $s'$ and an isometry $A(s,s')\in \Gamma$ such that $A(s,s')$ maps side $s$ onto side $s'$, $(s')' = s$ and $A(s', s) = (A(s, s'))^{-1}$. These pairs of sides $(s,s')$ can be easily determined using [\[eq:sidepairings\]](#eq:sidepairings){reference-type="eqref" reference="eq:sidepairings"}. For example, $A(s_1,s_{33}) = \gamma_1$ and $A(s_{33},s_1)=\gamma_{33}$. Such a collection $\Phi=\{A(s,s')\}$ of isometries is called a *side-paring* of $\F$.

Now we introduce the notion of *cycle* of vertices following [@maskit1971]. Let $z_1$ be some vertex, say, $v_i$ of $\F$. There are two sides of $\F$, namely, $s_{i-1}$ and $s_i$ which meet at $z_1$. We choose one of these, denoting it as $t_1$. There is a corresponding side $t_1'$ and an isometry $A_1 = A(t_1,t_1')$. The next vertex, $z_2$, is defined as the image of $z_1$ under the action of $A_1$, i.e., $z_2 = A_1(z_1)$. There is a unique other side $t_2$, i.e., $t_2\neq t_1'$ which has $z_2$ as one of its endpoint. There is a corresponding side $t_2'$ and a generator $A_2 = A(t_2, t_2')$. We can continue this process iteratively: $z_3 = A_2(z_2)$ and let $s_3$ be the unique other side which has $z_3$ as an endpoint, and so on. This procedure generates sequences: $\{z_n\}$ for vertices, $\{(t_n, t_n')\}$ for pairs of sides, and $\{A_n\}$ for $\Phi$. We define the *period* as the smallest positive integer $m$ for which all three sequences are periodic with period $m$. Then the ordered list of vertices $(z_1, \ldots, z_m)$ is called a cycle of vertices.

We can find cycles starting from a given vertex by following the definition. For example, consider a cycle that starts with the vertex $z_1: =  v_{2}$. This vertex is the intersection point of sides $s_1$ and $s_2$. By setting $t_1: = s_1$, we find $t_1' = s_{33}$ and $A_1 = A(s_1, s_{33})=\gamma_1$. With these choices, we can determine the subsequent terms in the following way:

-   $z_2 = A_1(z_1) = v_{33}$, and $A_2 = A(s_{32}, s_{11}) = \gamma_{32}$.

-   $z_3 = A_2(z_2) = v_{11}$, and $A_3 = A(s_{10}, s_{24}) = \gamma_{10}$.

-   $z_4 = A_3(z_3) = v_{24}$, and $A_4 = A(s_{23}, s_{2}) = \gamma_{23}$.

-   $z_5 = A_4(z_4) = v_{2}$, and $A_5 = A(s_{1}, s_{33}) = \gamma_{1}$

After this point, the cycle becomes periodic. In this specific example, we have a cycle with a period of 4.

There exist cycles of both period 4 and period 14 within the vertices of $\F$. These vertices can be grouped into 8 distinct sets, with each set containing members that belong to a specific cycle. Here is the list of all cycles, where each pair of adjacent vertices in a cycle is connected an arrow, and each arrow is labeled with the corresponding side-pairing transformation. We will begin with the cycles having a period of 4, listed as follows: $$\begin{aligned}
{6}
v_{2}
& \xrightarrow{\gamma_{1}} v_{33}
& \xrightarrow{\gamma_{32}} v_{11}
& \xrightarrow{\gamma_{10}} v_{24}
& \xrightarrow{\gamma_{23}} v_{2},\qquad  &&
v_{2}
& \xleftarrow{\gamma_{33}} v_{33}
& \xleftarrow{\gamma_{11}} v_{11}
& \xleftarrow{\gamma_{24}} v_{24}
& \xleftarrow{\gamma_{2}} v_{2}, \notag \\
v_{3}
& \xrightarrow{\gamma_{3}} v_{14}
& \xrightarrow{\gamma_{14}} v_{36}
& \xrightarrow{\gamma_{36}} v_{23}
& \xrightarrow{\gamma_{23}} v_{3},\qquad &&
v_{3}
& \xleftarrow{\gamma_{13}} v_{14}
& \xleftarrow{\gamma_{35}} v_{36}
& \xleftarrow{\gamma_{22}} v_{23}
& \xleftarrow{\gamma_{2}} v_{3},\notag \\
v_{5}
& \xrightarrow{\gamma_{5}} v_{27}
& \xrightarrow{\gamma_{27}} v_{38}
& \xrightarrow{\gamma_{38}} v_{18}
& \xrightarrow{\gamma_{18}} v_{5},\qquad &&
v_{5}
& \xleftarrow{\gamma_{26}} v_{27}
& \xleftarrow{\gamma_{37}} v_{38}
& \xleftarrow{\gamma_{17}} v_{18}
& \xleftarrow{\gamma_{4}} v_{5}, \notag \\
v_{6}
& \xrightarrow{\gamma_{6}} v_{35}
& \xrightarrow{\gamma_{35}} v_{15}
& \xrightarrow{\gamma_{15}} v_{26}
& \xrightarrow{\gamma_{26}} v_{6},\qquad &&
v_{6}
& \xleftarrow{\gamma_{34}} v_{35}
& \xleftarrow{\gamma_{14}} v_{15}
& \xleftarrow{\gamma_{25}} v_{26}
& \xleftarrow{\gamma_{5}} v_{6}, \notag \\
v_{8}
& \xrightarrow{\gamma_{8}} v_{30}
& \xrightarrow{\gamma_{30}} v_{17}
& \xrightarrow{\gamma_{17}} v_{39}
& \xrightarrow{\gamma_{39}} v_{8},\qquad &&
v_{8}
& \xleftarrow{\gamma_{29}} v_{30}
& \xleftarrow{\gamma_{16}} v_{17}
& \xleftarrow{\gamma_{38}} v_{39}
& \xleftarrow{\gamma_{7}} v_{8}, \notag \\
v_{9}
& \xrightarrow{\gamma_{8}} v_{29}
& \xrightarrow{\gamma_{28}} v_{42}
& \xrightarrow{\gamma_{41}} v_{20}
& \xrightarrow{\gamma_{19}} v_{9},\qquad &&
v_{9}
& \xleftarrow{\gamma_{29}} v_{29}
& \xleftarrow{\gamma_{42}} v_{42}
& \xleftarrow{\gamma_{20}} v_{20}
& \xleftarrow{\gamma_{9}} v_{9}, \notag \\
v_{12}
& \xrightarrow{\gamma_{11}} v_{32}
& \xrightarrow{\gamma_{31}} v_{21}
& \xrightarrow{\gamma_{20}} v_{41}
& \xrightarrow{\gamma_{40}} v_{12},\qquad &&
v_{12}
& \xleftarrow{\gamma_{32}} v_{32}
& \xleftarrow{\gamma_{21}} v_{21}
& \xleftarrow{\gamma_{41}} v_{41}
& \xleftarrow{\gamma_{12}} v_{12}.
\label{eq:vertex_cycle1}
\end{aligned}$$

Here is the list of cycles with a period of 14: $$\begin{aligned}
{2}
v_{1} & \xrightarrow{\gamma_{42}} v_{28} \xrightarrow{\gamma_{27}} v_{37} \xrightarrow{\gamma_{36}} v_{22} \xrightarrow{\gamma_{21}} v_{31} \xrightarrow{\gamma_{30}} v_{16} \xrightarrow{\gamma_{15}} v_{25} \xrightarrow{\gamma_{24}} v_{10} \notag \\
&
\xrightarrow{\gamma_{9}} v_{19}
\xrightarrow{\gamma_{18}} v_{4}
\xrightarrow{\gamma_{3}} v_{13}
\xrightarrow{\gamma_{12}} v_{40} \xrightarrow{\gamma_{39}} v_{7}
\xrightarrow{\gamma_{6}} v_{34}
\xrightarrow{\gamma_{33}} v_{1}, \notag \\
v_{1} &
\xleftarrow{\gamma_{28}} v_{28} 
\xleftarrow{\gamma_{37}} v_{37}
\xleftarrow{\gamma_{22}} v_{22} 
\xleftarrow{\gamma_{31}} v_{31}
\xleftarrow{\gamma_{16}} v_{16}
\xleftarrow{\gamma_{25}} v_{25}
\xleftarrow{\gamma_{10}} v_{10} \notag\\
&
\xleftarrow{\gamma_{19}} v_{19}
\xleftarrow{\gamma_{4}} v_{4} 
\xleftarrow{\gamma_{13}} v_{13}
\xleftarrow{\gamma_{40}} v_{40}
\xleftarrow{\gamma_{7}} v_{7}
\xleftarrow{\gamma_{34}} v_{34}
\xleftarrow{\gamma_{1}} v_{1}.
\label{eq:vertex_cycle2}
\end{aligned}$$

For each vertex $v_i$, suppose that two sides $s_{i-1}$ and $s_{i}$ make an angle $\alpha(v_i)$ at $v_i$ measured from inside the polygon. Using the algebraic coordinates for $v_i$ provided in Table [1](#tab:vcoor){reference-type="ref" reference="tab:vcoor"} and applying formula [\[eq:hyperbolic_cosine\]](#eq:hyperbolic_cosine){reference-type="eqref" reference="eq:hyperbolic_cosine"}, we can compute $\cos(\alpha(v_i))$. It turns out that $\cos(\alpha(v_i))$ is an algebraic number. Due to the symmetry of $\F$, as explained in , we only need to calculate $\alpha(v_i)$ for $1\leq i \leq 6$. The precise values for these angles are presented in Table [2](#tab:vertex_angle){reference-type="ref" reference="tab:vertex_angle"}.

::: {#tab:vertex_angle}
   $i$   Minimal polynomial of $\cos(\alpha(v_i)))$   Numerical value of $\alpha(v_i)/\pi$
  ----- -------------------------------------------- --------------------------------------
    1                 $1-4x-4x^2+8x^3$                              0.142857
    2             $-1+56x^2-336x^4+448x^6$                          0.545452
    3             $-1+56x^2-336x^4+448x^6$                          0.545452
    4                 $1-4x-4x^2+8x^3$                              0.142857
    5             $-1+56x^2-336x^4+448x^6$                          0.454548
    6             $-1+56x^2-336x^4+448x^6$                          0.454548

  : Angles at vertices of $\F$
:::

::: lemma
[]{#lemma:cycle_angle_sum label="lemma:cycle_angle_sum"} For every cycle $(z_1,\dots, z_m)$ of vertices of $\F$, the sum of angles is $2\pi$: $$\sum_{i=1}^{m}\alpha(z_i) = 2\pi.$$
:::

::: proof
*Proof.* Note that if $i\equiv j \mod 6$, then $\alpha(v_i) = \alpha(v_{j})$. Let us establish the proof by considering different cases.

For a cycle $(z_1,z_2,z_3,z_4)$ of period 4 as given in [\[eq:vertex_cycle1\]](#eq:vertex_cycle1){reference-type="eqref" reference="eq:vertex_cycle1"}, we have: $$\sum_{i=1}^{4}\alpha(z_i) = 
\alpha(v_2)+\alpha(v_3)+\alpha(v_5)+\alpha(v_6)
=2(\alpha(v_2)+\alpha(v_5))
=2\pi.$$ And for a cycle $(z_1,\dots,z_{14})$ of period 14 in [\[eq:vertex_cycle2\]](#eq:vertex_cycle2){reference-type="eqref" reference="eq:vertex_cycle2"}, we have: $$\sum_{i=1}^{14}\alpha(z_i) = 
7(\alpha(v_1)+\alpha(v_4))
=2\pi.$$ ◻
:::

::: thm
[]{#thm:fund label="thm:fund"} The polygon $\F$ is a fundamental domain for $\Gamma$.
:::

::: proof
*Proof.* Let us employ Poincaré's theorem as presented in [@maskit1971]: if for every cycle $(z_1,\dots, z_m)$, there is an integer $\nu$ for which $$\sum_{i=1}^{m}\alpha(z_i) = \frac{2\pi}{\nu},$$ then $\F$ is a fundamental domain for the group generated by side-pairing $\Phi$, which is nothing but $\Gamma$.

This reduces our task to calculating the angle sum for every cycle. The theorem is thus deduced from Lemma  [\[lemma:cycle_angle_sum\]](#lemma:cycle_angle_sum){reference-type="ref" reference="lemma:cycle_angle_sum"}. ◻
:::

::: prop
[]{#prop:gammaindex label="prop:gammaindex"} The index $[\Delp:\Gamma]$ is 504.
:::

::: proof
*Proof.* From Table [2](#tab:vertex_angle){reference-type="ref" reference="tab:vertex_angle"}, we have $$\sum_{i=1}^{42}\alpha(z_i) = 7(2+2/7)\pi = 16\pi.$$ This implies that the area of $\F$ is $24\pi$. Therefore, $[\Delp:\Gamma]=504$, given that the fundamental domain of $\Delp$ has area $\pi/21$, which is twice the area of the fundamental triangle for $\Del$ illustrated in Figure [\[fig:237_tri\]](#fig:237_tri){reference-type="ref" reference="fig:237_tri"}. ◻
:::

::: cor
The group $\Gamma$ is the normal subgroup of $\Delp$ generated by $\gamma_{15}$.
:::

::: proof
*Proof.* Let $\Gamma'$ be the normal subgroup of $\Delp$ with index 504, which was considered in Subsection [\[subsec:hurwitzsurfaces\]](#subsec:hurwitzsurfaces){reference-type="ref" reference="subsec:hurwitzsurfaces"}. It is the normal subgroup of $\Delp$ generated by: $$\begin{aligned}
\gamma & = (a^{-1}b^3a^{-1}ba^{-1}b^3)^2 \notag \\
& = (s_2s_3s_2s_1s_2s_1s_2s_1s_2s_3s_2s_1s_2s_3s_2s_1s_2s_1s_2s_1)^2 \notag \\
&= s_2s_3s_2s_1s_2s_1s_2s_1s_3s_2s_1s_2s_1s_3s_2s_1s_2s_1s_2s_3s_2s_1s_2s_1s_2s_1s_3s_2s_1s_2s_1s_3s_2s_1s_2s_1 \notag \\
&= \gamma_{15}. \label{eq:gamma15}
\end{aligned}$$ Thus, we have $\Gamma' \subseteq \Gamma$. Considering both subgroups have the same index, we deduce $\Gamma' = \Gamma$. ◻
:::

Recall that for $w\in \disk$ with trivial stabilizer in $\Gamma$, the *Dirichlet domain* centered at $w\in \disk$ is defined by $$D(w)=\{z \in \disk: \distD(z, w) \leq \distD(z, g w) \text { for all } g \in \Gamma\} .$$ It is well-known that $D(w)$ is a fundamental domain for $\Gamma$; see, for example, [@MR0698777 Section 9.4]. From [\[eq:isometric_dist\]](#eq:isometric_dist){reference-type="eqref" reference="eq:isometric_dist"}, the domain $D(0)$ can be described as the closure in $\disk$ of $$\bigcap_{g \in \Gamma \backslash\{1\}} \ext(I(g)).$$

::: thm
[]{#thm:dirichlet label="thm:dirichlet"} The polygon $\F$ is the Dirichlet domain centered at $0$.
:::

::: proof
*Proof.* Referring to [\[eq:Fdef\]](#eq:Fdef){reference-type="eqref" reference="eq:Fdef"}, one can clearly see that $D(0)$ is a subset of $\F$. It is sufficient to verify that every interior point of $\F$ lies within $D(0)$. Then, considering that both sets are closed, it implies that the two sets are the same.

Let $z\in \F\backslash D(0)$ be an interior point of $\F$. Given that $D(0)$ is a fundamental domain for $\Gamma$, there exists a transformation $\gamma\in \Gamma$ such that $\gamma z\in D(0)\subseteq \F$. Consequently, both $z$ and $\gamma z$ reside in $\F$, which implies that they are boundary points of $\F$. From this, we conclude that $D(0)$ and $\F$ are indeed identical. ◻
:::
