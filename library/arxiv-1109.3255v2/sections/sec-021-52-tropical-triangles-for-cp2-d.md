---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-021-52-tropical-triangles-for-cp2-d
section_title: "Tropical triangles for (CP2, D)"
section_number: 5.2
pages: 58-60
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.957
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:tropical-our-case label="sec:tropical-our-case"}

We now write out explicitly the tropical curves contributing to the triangle products in the case of $(\CP^2, D)$. Let us use coordinates $(\eta,\xi)$ where the point $q_{a,i} \in B(\frac{1}{n}\Z)$ has coordinates $(a/n,-i/n)$

There is one family of simple tropical disks that emanate from the singularity on the $\eta = 0$ line in the vertical direction. Their primitive tangent vectors are $\pm (0,1)$.

Figure [1](#fig:tropical-triangle){reference-type="ref" reference="fig:tropical-triangle"} shows the the tropical triangle representing the contribution of $y^2p$ to the product of $x^2$ and $z^2$. This triangle has multiplicity $2$. The singularity of the affine structure is placed so as to emphasize the tropical disk ending at the singularity.

![A tropical triangle. The dotted line extending up from the singular point is a tropical disk.](tropical-triangle){#fig:tropical-triangle width="3in"}

::: proposition
[]{#prop:tropical-our-case label="prop:tropical-our-case"} Let $n > 0$ and $m > 0$, and take $q_{a,i}\in B(\frac{1}{n}\Z)$, $q_{b,j} \in B(\frac{1}{m}\Z)$, and $q_{a+b,h} \in
  B(\frac{1}{n+m}\Z)$.

Suppose $a$ and $b$ have different signs, and let $k =
  \min(|a|,|b|)$, and $h = i+j+s$. If $0 \leq s \leq k$, there is one tropical triangle connecting these three points. It is balanced after the addition of either $s$ or $k-s$ tropical disks, depending on the position of the singularity. The multiplicity of this curve is $\binom{k}{s}$. If $s$ does not lie in this range, there is no triangle.

Suppose that $a$ and $b$ have the same sign. Then unless $h = i+j$ there is no triangle, and when $h = i+j$ there is exactly one, which is represented geometrically by the line segment joining $q_{a,i}$ and $q_{b,j}$.
:::

::: proof
*Proof.* When $a$ and $b$ have the same sign the tropical triangle can have no tropical disks attached to it. Therefore the tropical triangle is simply a line segment which passes through the three points, and this only exists if $q_{a+b,h}$ lies on the line between $q_{a,i}$ and $q_{b,j}$.

As for when $a$ and $b$ have different signs, let us consider the case $a \leq 0$, $b \geq 0$, $a+b \geq 0$, and hence $k = -a$. The other cases are related to this by obvious reflections and re-namings.

By Proposition [\[prop:tropical-triangles\]](#prop:tropical-triangles){reference-type="ref" reference="prop:tropical-triangles"}, a tropical triangle consists essentially of two maps $u_1, u_2: (-\infty,0]\to B$, together with some copies of the tropical disk and their multiples.

-   The leg $u_2$ of the tree connecting $q_{b,j}$ to $q_{a+b,h}$ cannot have any tropical disks attached, since both endpoints lie on the same side of the line $\eta = 0$. We can apply Lemma [\[lem:differences\]](#lem:differences){reference-type="ref" reference="lem:differences"} to obtain the tangent vector $\dot{u}_2$ at $q_{a+b,h}$ as $m$ times the difference between the endpoints, or $$\dot{u}_2(q_{a+b,h}) = m(q_{a+b,h}-q_{b,j}) = \left(\frac{ma-nb}{n+m}, \frac{-(mi-nj+ms)}{n+m}\right)$$

-   The leg $u_1$ of the tree connecting $q_{a,i}$ to $q_{a+b,h}$ crosses the line $\eta = 0$ at some point $x$, where tropical disks can be attached. It may bend there, and continue on to $q_{a+b,h}$, where the balancing condition $\dot{u}_1 + \dot{u}_2 =
      0$ must hold. This shows that the portion of $u_1$ connecting $x$ to $q_{a+b,h}$ must be parallel to $u_2$. Hence $x$ must be on the line joining $q_{b,j}$ and $q_{a+b,h}$. We obtain the position of $x$: $$x:   (\eta,\xi) = (0,(-aj+bi+bs)/(ma-nb))$$

-   By Lemma [\[lem:differences\]](#lem:differences){reference-type="ref" reference="lem:differences"} at $x$ the tangent vector $\dot{u}_1$ is given by $n$ times the difference of the endpoints $x$ and $q_{a,i}$: $$\dot{u}_1(x)_L = n(x - q_{a,i}) = (-a,[a(mi-nj)+nbs]/(ma-nb))$$ we use the subscript $L$ to denote this is the tangent vector coming from the left.

-   If the singularity of the affine structure occurs below the point $x$, then tropical disks are line segments going up from the singularity to $x$ in the direction $(0,1)$. Adding the vector $(0,s)$ to $\dot{u}_1(x)_L$, we obtain $\dot{u}_1(x)_R$, the tangent vector from the right, $$\dot{u}_1(x)_R = \dot{u}_1(x)_L + (0,s) = (-a, a(mi-nj+ms)/(ma-nb))$$ which is parallel to $\dot{u}_2(q_{a+b,h})$, as it must be. This shows that we must attach a collection of tropical disks whose total weight is $s$.

-   If the singularity of the affine structure occurs above $x$, then tropical disks are line segments going down from the singularity to $x$ in the direction $(0,-1)$, but there is also the monodromy to be taken into account. First we must act on $\dot{u}_1(x)_L$ by the monodromy $M=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ to get $$M\dot{u}_1(x)_L = (-a,[a(mi-nj)+nbs]/(ma-nb) - a)$$ Adding the vector $(0,-(k-s))$ to this, with $k = -a$, gives the same result as before for $\dot{u}_1(x)_R$. However, in this case we are attaching a collection of disks with total weight $(k-s)$.

-   The leg $u_1$ propagates in the direction $\dot{u}_1(x)_R$ from $x$ to $q_{a+b,h}$. As it does so, the tangent vector $\dot{u}_1$ increases by $\Delta = n(q_{a+b,h} - x)$, which is parallel to $\dot{u}_1(x)_R$. By comparing affine lengths of the segment of $u_1$ from $q_{a,i}$ to $x$ and the segment of $u_1$ from $x$ to $q_{a+b,h}$, we have the proportion $$\dot{u}_1(x)_R:\Delta = [-a/n] : [(a+b)/(n+m)]$$ and $$(\dot{u}_1(x)_R + \Delta):\dot{u}_1(x)_R = [(a+b)/(n+m) - a/n]:[-a/n] = [-(ma-nb)/(n+m)]:[-a]$$ Thus $$\dot{u}_1(q_{a+b,h}) =
        \left(-\frac{ma-nb}{n+m},\frac{mi-nj+ms}{n+m}\right) = -\dot{u}_2(q_{a+b,h})$$ Verifying the balancing condition at $q_{a+b,h}$.

Now that we know which tropical curves contribute, we must compute their multiplicities. The tropical curve constructed above uses the tropical disk $s$ or $(k-s)$ times. This means that either we attach a single simple disk $s$ times, or we attach some multiple covers of the disk in some fashion as to achieve a total multiplicity of $s$. By our ansatz, only the simple disks contribute, and each with multiplicity one.

Attaching simple disks does introduce a multiplicity, since there are multiple places to attach this disk. In fact, we have $\det(\dot{u}_1(x)_L,(0,1)) = -a = k$, so there are a total of $k$ places for disks to be attached. Thus we get the multiplicity $\binom{k}{s}$ or $\binom{k}{k-s}$, which are equal and give the desired result. ◻
:::

::: remark
The fact that the multiplicities $\binom{k}{s}$ and $\binom{k}{k-s}$ are equal is an illustration of the general phenomenon that the exact position of the singularity along its invariant line does not matter for tropical curve counts.
:::
