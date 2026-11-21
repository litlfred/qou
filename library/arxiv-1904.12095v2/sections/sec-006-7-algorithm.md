---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-006-7-algorithm
section_title: "Algorithm"
section_number: 7
pages: 15-20
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.963
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:algo label="sec:algo"}

## Overview

Let $\mathcal{T}$ be an oriented, finite 3-dimensional triangulation. Let $o=V(\mathcal{T})$ be the number of vertices and index the edges $E(\mathcal{T})=\{e_1,\dots,e_m\}$. Assume we are given floating-point approximations for the edge parameters $\nu_{e_1},\dots,\nu_{e_m}$ such that the $\Theta_{e_1}, \dots, \Theta_{e_m}$ are approximately $2\pi$ (e.g, using the program Orb [@orb] based on the methods described in [@heardThesis Section 2.2]).

We will either fail in one of the steps or obtain intervals $\underline{\overline{\nu_{e_1}}},\dots,\underline{\overline{\nu_{e_m}}}$ guaranteed to contain values for $\nu_{e_1},\dots,\nu_{e_m}$ yielding a hyperbolic structure on $\mathcal{T}$ as follows:

1.  []{#step:submatrix label="step:submatrix"} Find a subsystem of equations of full rank:\
    Since the given approximations for the edge parameters are close to a hyperbolic structure, evaluating the Jacobian $$\label{eqn:jacobian}
    M=\left(\frac{\partial \Theta_{e_j}}{\partial \nu_{e_i}}\right)_{i=1,\dots,m;j=1,\dots,m}$$ gives a matrix close to a singular matrix that we expect to have rank $m-3o$ (see Conjecture [\[conjecture:main\]](#conjecture:main){reference-type="ref" reference="conjecture:main"}). Pick a suitable set of $m-3o$ rows and columns such that the resulting submatrix of $M$ has full rank.\
    This corresponds to picking two partitions of the edges of $\mathcal{T}$ $$\begin{aligned}
    E(\mathcal{T})=E^\sim \cup E^=&\mbox{with}& E^\sim=\{e^\sim_1,\dots,e^\sim_{3o}\},~E^= = \{e^=_1,\dots,e^=_{m-3o}\}\\
    E(\mathcal{T})=E^\mathrm{fixed} \cup E^\mathrm{var}& \mbox{with}& E^\mathrm{fixed} = \{e^{\mathrm{fixed}}_1,\dots,e^{\mathrm{fixed}}_{3o}\}, ~E^\mathrm{var} = \{e^{\mathrm{var}}_1,\dots,e^{\mathrm{var}}_{m-3o}\}
    \end{aligned}$$ such that $$M'=\left(\frac{\partial \Theta_{e^=_j}}{\partial \nu_{e^\mathrm{var}_i}}\right)_{i=1,\dots,m-3o;j=1,\dots,m-3o}$$ has full rank near the given values. Keep the values of $\nu_{e^\mathrm{fixed}_i}$ fixed from now on.

2.  []{#step:intervalNewton label="step:intervalNewton"} Find an interval solution to the above subsystem of equations:\
    Using interval Newton method or Krawczyk test, find large enough intervals $$\underline{\overline{\nu_{e^\mathrm{var}_1}}},\dots,\underline{\overline{\nu_{e^\mathrm{var}_{m-3o}}}}$$ for the edges in $E^\mathrm{var}$ such that they contain a point where $\Theta_{e^=_j}=2\pi$ for every $e^=_j\in E^=$. To have intervals $\underline{\overline{\nu_{e_1}}},\dots,\underline{\overline{\nu_{e_m}}}$ for all edges of the triangulation, simply use the interval $[\nu_{e^\mathrm{fixed}_i},\nu_{e^\mathrm{fixed}_i}]$ containing only the fixed value $\nu_{e^\mathrm{fixed}_i}$ for each remaining edge $e^\mathrm{fixed}_i\in E^\mathrm{fixed}$.

3.  []{#step:validGram label="step:validGram"} Ensure solutions are valid for a simplex:\
    Using the intervals for each edge, use interval arithmetic to verify the conditions of Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"} for each simplex $\Delta$.

4.  []{#step:approxEdgeEqn label="step:approxEdgeEqn"} Ensure that the remaining edge equations are "approximately" fulfilled:\
    Use these intervals to compute intervals $\underline{\overline{\Theta_{e^\sim_1}}},\dots,\underline{\overline{\Theta_{e^\sim_{3o}}}}$ for the sums of dihedral angles adjacent to an edge in $E^\sim$ to ensure that $2\pi \in \underline{\overline{\Theta_{e^\sim_j}}}$ for every such edge.

5.  []{#step:avoidGimbal label="step:avoidGimbal"} Ensure that the remaining edge equations are fulfilled exactly:\
    Find a gimbal loop $\Gamma_1,\dots,\Gamma_o$ for each vertex and consider the resulting gimbal function $g$. Ensure that $K=\underline{\overline{\Theta_{e^\sim_1}}}\times\cdots\times\underline{\overline{\Theta_{e^\sim_{3o}}}}$ avoids gimbal lock for the intervals computed in the previous step using interval arithmetics.

## Computing the Jacobian

Note that the formulas given in [@heardThesis Lemma 2.5] for the derivatives $\partial\theta_{ij}/\partial{v_{mn}}$ (where $v_{mn}=v_{nm}$) run into a division by zero when $\theta_{ij}=\pi/2$. To obtain formulas avoiding this problem, we take the total derivative of Equation [\[eqn:dihedral\]](#eqn:dihedral){reference-type="ref" reference="eqn:dihedral"} $$\frac{\partial\theta_{ij}}{\partial{v_{mn}}}
=\frac{-1}{\sqrt{c_{ii}c_{jj}-c_{ij}^2}} \left(\frac{\partial c_{ij}}{\partial v_{mn}} - \frac{c_{ij}}{2 c_{ii}}\cdot \frac{\partial c_{ii}}{\partial v_{mn}} - \frac{c_{ij}}{2c_{jj}}\cdot \frac{\partial c_{jj}}{\partial v_{mn}}\right)$$ and note that each $\partial c_{kl}/\partial v_{mn}=(-1)^{k+l} \partial (\det G_{kl}) / \partial v_{mn}$ is, up to sign, the sum of at most two cofactors of $G_{kl}$, namely, the ones corresponding to the $2\times 2$-matrices that can be obtained by deleting from $G_{kl}$ the row and column corresponding to row $m$ or $n$ and column $n$, respectively, $m$ of $G$.

Using this, we can compute the Jacobian $M$ in [\[eqn:jacobian\]](#eqn:jacobian){reference-type="eqref" reference="eqn:jacobian"} using floating point (in Step [\[step:submatrix\]](#step:submatrix){reference-type="ref" reference="step:submatrix"}), respectively, interval arithmetics (in Step [\[step:intervalNewton\]](#step:intervalNewton){reference-type="ref" reference="step:intervalNewton"}) avoiding the need for automatic differentiation.

## Step [\[step:submatrix\]](#step:submatrix){reference-type="ref" reference="step:submatrix"}: Finding a submatrix of full rank

This step is necessary since interval methods (e.g., interval Newton method or Krawczyk test) only work for systems with invertible Jacobian. To obtain a subsystem of full rank, we apply the following algorithm to $M$ with $h=m-3o$:

::: center
:::

::: remark
Note that the algorithm has the following stability properties:

1.  We obtain the same set of rows and columns of $M$ when permuting the rows or columns of the input matrix $M$, i.e., the result is obtained by applying the same permutation to $R$, respectively, $C$ --- unless there are ties in Step [\[substep:maxEntry\]](#substep:maxEntry){reference-type="ref" reference="substep:maxEntry"}.

2.  Transposing $M$ results in interchanging $R$ and $C$.
:::

::: remark
This algorithm is a simplified version of $LDU$-factorization with full pivoting, i.e., a decomposition $M=PLDUP'$ where $P$ and $P'$ are permutation matrices, $L$ and $U$ unit-lower, respectively, unit-upper triangular matrices and $D$ a diagonal matrix.
:::

## Step [\[step:intervalNewton\]](#step:intervalNewton){reference-type="ref" reference="step:intervalNewton"}

This step is a straightforward application of the interval Newton method or Krawczyk test to the equations $\Theta_{e^=_j}-2\pi = 0$ in variables $\nu_{e^\mathrm{var}_i}$ (keeping $\nu_{e^\mathrm{fixed}_i}$ fixed). Note that even for high precision solutions, computing the approximate inverse in the Krawczyk test using IEEE754 double-precision floating point numbers is usually sufficient.

If we are interested in increasing the precision of the solution, we can optionally perform the ordinary Newton method to the subsystem from Step [\[step:submatrix\]](#step:submatrix){reference-type="ref" reference="step:submatrix"} before Step [\[step:intervalNewton\]](#step:intervalNewton){reference-type="ref" reference="step:intervalNewton"}.

## Steps [\[step:validGram\]](#step:validGram){reference-type="ref" reference="step:validGram"} and [\[step:approxEdgeEqn\]](#step:approxEdgeEqn){reference-type="ref" reference="step:approxEdgeEqn"}

These conditions are straightforward to check with interval arithmetics given the comment about the Budan-Fourier theorem in Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"}.

## Step [\[step:avoidGimbal\]](#step:avoidGimbal){reference-type="ref" reference="step:avoidGimbal"}: Finding gimbal loops

We need to pick a gimbal loop $\Gamma_k$ in each "vertex link" $(L_k,L^=_k)$. Note that this complex consists of the small hexagons (with alternating $\beta$- and $\gamma$-edges) of the doubly-truncated simplices (see Figure [\[fig:DoublyTruncated\]](#fig:DoublyTruncated){reference-type="ref" reference="fig:DoublyTruncated"}) and polygons coming from the ends of the prisms (see Figure [\[fig:Prism\]](#fig:Prism){reference-type="ref" reference="fig:Prism"} and [\[fig:gimbalLoopsInTriangulation\]](#fig:gimbalLoopsInTriangulation){reference-type="ref" reference="fig:gimbalLoopsInTriangulation"}). For a vertex $v_k$, pick a hexagon in $L^=_k$, mark it as "used" and starting with its boundary (oriented such that it traverses a $\gamma^{\sigma(0)\sigma(1)\sigma(2)}$ with $\sigma\in A_4$), expand this edge-loop until it touches each boundary component of $L^=_k$ as follows: pick a $\beta$-edge of the edge-loop that is adjacent to an unused hexagon $H$ and replace the $\beta$-edge by the five other edges of $H$, marking $H$ as "used" (see Figure [1](#fig:findingAGimbalLoop){reference-type="ref" reference="fig:findingAGimbalLoop"}). It is faster to exhaust all $\beta$-edges of one hexagon first in breadth-first search manner (vs depth-first search) before moving on to the next hexagon.

<figure id="fig:findingAGimbalLoop">
<div class="center">

</div>
<figcaption>Procedure to find a gimbal loop <span class="math inline"><em>Γ</em></span>.</figcaption>
</figure>

## Step [\[step:avoidGimbal\]](#step:avoidGimbal){reference-type="ref" reference="step:avoidGimbal"}: Computing the gimbal function's derivative

We then need to compute $[Dg(K)]$ which boils down to computing the derivatives $\partial m_{\Gamma_k}/\partial T_i$ of the gimbal matrices $m_{\Gamma_k}$ associated to the gimbal loops $\Gamma_k$. Focusing on one $i$ and $k$, note that $m_{\Gamma_k}$ is given by an alternating product the form $$\prod\nolimits_1 \cdot R_{T_i}\cdot \prod\nolimits_2  \cdot R_{T_i} \cdot \prod\nolimits_3 \cdot R_{T_i} \cdots \prod\nolimits_q$$ where $\prod\nolimits_k$ stands for a product of $\beta$- and $\gamma$-matrices and rotations $R_{T_{i'}}$ with $i'\not=i$ ($q$ is actually at most three since an edge of $\mathcal{T}$ has two ends which might or might not end in the same vertex). We can then compute the derivative as $$\begin{aligned}
\frac{\partial m_{\Gamma_k}}{\partial T_i} &=& \phantom{+} \prod\nolimits_1 \cdot R'_{T_i}\cdot \prod\nolimits_2  \cdot R_{T_i} \cdot \prod\nolimits_3 \cdots R_{T_i} \cdot \prod\nolimits_q\\
 & & + ~ \cdots \\
 & & +\prod\nolimits_1 \cdot R_{T_i}\cdot \prod\nolimits_2  \cdot R_{T_i} \cdot \prod\nolimits_3 \cdots R'_{T_i} \cdot \prod\nolimits_q \quad \mbox{where}~
R'_\omega = \left(\begin{array}{ccc} -\sin\omega & -\cos\omega & \\ \phantom{-}\cos\omega & -\sin\omega & \\ & & 0\end{array}\right).
\end{aligned}$$

We need to evaluate this using the intervals from Step [\[step:intervalNewton\]](#step:intervalNewton){reference-type="ref" reference="step:intervalNewton"} for the $\beta$- and $\gamma$-matrices and the intervals $\underline{\overline{\Theta_{e^\sim_1}}},\dots,\underline{\overline{\Theta_{e^\sim_{3o}}}}$ from Step [\[step:approxEdgeEqn\]](#step:approxEdgeEqn){reference-type="ref" reference="step:approxEdgeEqn"} for $R'_{T_i}$ and all the $R_{T_j}$.

## Step [\[step:avoidGimbal\]](#step:avoidGimbal){reference-type="ref" reference="step:avoidGimbal"}: Verifying invertibility

To show that a square matrix $m$ with real interval entries is invertible (in the sense used in Definition [\[def:gimbalLockAvoided\]](#def:gimbalLockAvoided){reference-type="ref" reference="def:gimbalLockAvoided"} and [\[def:trigGimbalFunction\]](#def:trigGimbalFunction){reference-type="ref" reference="def:trigGimbalFunction"}), we can find an approximate inverse $n$ (usually IEEE754-double precision is sufficient) and verify that each entry of $mn-\mathrm{Id}$ has absolute value strictly less than $1/r^2$ where $r$ is the number of rows.
