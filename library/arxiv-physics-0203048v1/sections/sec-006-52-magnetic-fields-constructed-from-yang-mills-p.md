---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-006-52-magnetic-fields-constructed-from-yang-mills-p
section_title: "Magnetic fields constructed from Yang-Mills potentials"
section_number: 5.2
pages: 8-11
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.992
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
As mentioned above we now interpret the three components of the non-Abelian pure gauge Yang-Mills potential $A$ as potentials of three independent, non-vanishing magnetic fields. It is sufficient to consider only one of the three potentials $A^i$, since due to $\hat{n}^i = x^i/||\bx||$ and the cyclic symmetry of ([\[Yang-Mills-potential-components\]](#Yang-Mills-potential-components){reference-type="ref" reference="Yang-Mills-potential-components"}) in the indices $i,j,k$ all three fields can be obtained from just one field by rotations that map the $x^i$-axes on one another. From ([\[Yang-Mills-potential-components\]](#Yang-Mills-potential-components){reference-type="ref" reference="Yang-Mills-potential-components"}) we calculate the vector potential $\bA^3$ in spherical coordinates $x = r \sin\vartheta \cos\varphi$, $y = r \sin\vartheta \sin\varphi$, and $z = r \cos\vartheta$. Using unit basis vectors $\be_r,\be_\vartheta, \be_\varphi$ and fixing a value for the "coupling constant" of $q=2$, we find $$\begin{aligned}
\fl
   \bA^3 \,=\, 
   \frac{-2\pi \cos\vartheta }{(1+r^2)^{3/2}}\,\be_r \,+\,
   \frac{\sin\vartheta}{r}\sin\left(\frac{2\pi r}{\sqrt{1+r^2}}\right)\,
   \be_\vartheta
   \,-\,\frac{2 \sin\vartheta}{r}\sin^2\left( \frac{\pi r}{\sqrt{1+r^2}}\right)
   \be_\varphi. \label{Equation-Ai}
\end{aligned}$$ The corresponding magnetic field can be calculated from $\bB^3 =
 \nabla\times\bA^3$. It is easy to check that the fields $\bB^i$ are well defined and scale as $|| \bB^i(\bx) || \rightarrow  4\pi^2$ for $r\rightarrow 0$ and as $|| \bB^i(\bx) || \rightarrow  r^{-4}$ for $r\rightarrow \infty$. Hence, they have no singularity and decay sufficiently fast for large radii.

Let us note that the fields $\bB^i$ are highly symmetric and similar. Looking at the vector potential $\bA^3$ we observe that it is independent of the variable $\varphi$, therefore $\bB^3$ is invariant under rotations leaving the $x^3$-axis fixed. Since the potentials ([\[Yang-Mills-potential-components\]](#Yang-Mills-potential-components){reference-type="ref" reference="Yang-Mills-potential-components"}) are cyclic in $i,j,k$ it follows that each $\bB^i$ field is invariant under rotations about the $x^i$ axis. We have pointed out before that a rotation that maps the Euclidian basis vector field $\be_{1}$ to $\be_{2}$ also maps $\bB^1$ to $\bB^2$ etc. Furthermore, $\bB^3$ is similar to the total field $\bB = \bB^1+\bB^2+\bB^3$ in the following sense: Let $R$ be a rotation that maps the Euclidian basis vector $\be_{3}$ to the vector $\sqrt{3}\,R(\be_{3}) = \be_{1}+\be_{2}+\be_{3}$, then $\bB = \sqrt{3}\,R(\bB^3)$.

The magnetic fields $\bB^i$ are only of interest for us if their third-order invariant does not vanish. Explicitly calculating $\bA^i$ for $i=1,2,3$ we find, using the main Theorem, $$\begin{aligned}
\fl
H^{(3)}(\bB^1,\bB^2,\bB^3) 
   &= \int_0^\infty \frac{4\pi}{r^2(1+r^2)^{3/2}}
      \left(\cos(\frac{2\pi r}{\sqrt{r^2+1}})-1\right)\,dr
   = -16 \pi^2 \label{H-3-in-example}.
\end{aligned}$$ The fact that this integral is non-vanishing proves, that the constructed invariant cannot only be applied to all cases for which we where able to calculate the already existing invariant, i.e. to three mutually unlinked flux tubes, but also to examples of triples of fields not having disjunct support. It is thus a true generalization of the existing invariant known from the Massey triple product.

As we have pointed out before, $H^{(3)}$ is related to the vacuum winding number $W(g)$ of the connection $\omega=g^{-1}\d g$. We easily find (see also Frankel 1997) $$\begin{aligned}
 W(g)  &:= \nonumber
 \frac{1}{24\pi^2}\int_V tr(g^{-1} d g \wedge g^{-1} d g \wedge g^{-1} d g)\\
         &= 
   - \frac{1}{96\pi^2}\int_V\epsilon_{\indi\indj\indk}
                  A^\indi \wedge A^\indj \wedge A^\indk
  \label{H-3-and-W} \\
         &= -\frac{1}{16\pi^2} H^{(3)}(\bB^1,\bB^2,\bB^3), \nonumber 
\end{aligned}$$ where the trace term is usually referred to as the Cartan three-form on $SU(2)$.

In the general case the cross-helicities of three magnetic fields, for which we are able to find potentials such that $\nabla\cdot(\bA^i\times\bA^j)=\bB^i\cdot\bA^j-\bA^i\cdot\bB^j= 0$, do not have to vanish. In our example we can easily verify that they do vanish, i.e. $H(\bB^i,\bB^j) = 0$ for $i\ne j$. Of more interest are the three non-trivial self-helicities. If a triple of magnetic fields is derived from a Yang-Mills vacuum, ([\[dF-su2\]](#dF-su2){reference-type="ref" reference="dF-su2"}) together with $F=0$ implies $$\d A^\indi+\frac{1}{2}\,\epsilon_{\indi\indj\indk}A^\indj\wedge A^\indk = 0.$$ Using the definitions $B^\indi = \d A^\indi$ and $G^\indi = A^\indj \wedge A^\indk$ we find for $(\indi,\indj,\indk)$ cyclic $$B^\indi = -A^ \indj \wedge A^\indk = - G^\indi.$$ Thus, for $i=1,2,3$, we observe that $$H(\bB^i,\bB^i) =  \int_V \bA^i\cdot\bB^i \dxxx 
                  = -\int_V \bA^i\cdot\bG^i \dxxx = -H^{(3)}(\bB^1,\bB^2,\bB^3).$$ Therefore the self-helicities are equal to the value of the third-order invariant. This is a peculiarity of all magnetic field triples derived from an $SU(2)$ Yang-Mills vacuum.

<figure id="Figure-B3-field-lines-on-torus">
<div class="center">
<embed src="ghcmfig3.eps" />
</div>
<div class="center">
<embed src="ghcmfig4.eps" style="width:82.0%" />
</div>
<figcaption>The drawn torus is the surface at which <span class="math inline"><em>r</em>sin <em>ϑ</em><em>A</em><sub><em>φ</em></sub><sup>3</sup> =  − 1.8</span>. All field lines of <span class="math inline">$\bB^3$</span> lie on toroidal surfaces described by <span class="math inline"><em>r</em>sin <em>ϑ</em><em>A</em><sub><em>φ</em></sub><sup>3</sup> = <em>c</em><em>o</em><em>n</em><em>s</em><em>t</em></span>. Four field lines lying on this torus are drawn. <span id="Figure-B3-field-lines-on-torus" label="Figure-B3-field-lines-on-torus"></span></figcaption>
</figure>

<figure id="Figure-zero-cross-helicity">
<div class="center">
<embed src="ghcmfig5.eps" />
</div>
<div class="center">
<embed src="ghcmfig6.eps" />
</div>
<figcaption>For each field line <span class="math inline"><em>γ</em><sup>1</sup></span> and <span class="math inline"><em>γ</em><sup>3</sup></span> there exists a field line <span class="math inline"><em>γ̃</em><sup>1</sup></span> such that <span class="math inline">lk(<em>γ</em><sup>1</sup>,<em>γ</em><sup>3</sup>) + lk(<em>γ̃</em><sup>1</sup>,<em>γ</em><sup>3</sup>)</span> vanishes. <span id="Figure-zero-cross-helicity" label="Figure-zero-cross-helicity"></span></figcaption>
</figure>

In our analysis of the three example magnetic fields we now turn our attention to the topological structure of the fields and the linkage of individual field lines. Figure [\[Figure-B-1-2-3-field-lines\]](#Figure-B-1-2-3-field-lines){reference-type="ref" reference="Figure-B-1-2-3-field-lines"} and [2](#Figure-zero-cross-helicity){reference-type="ref" reference="Figure-zero-cross-helicity"} show numerically integrated field lines, where the starting points for integration are indicated by the foot points of the arrows that give the field line direction. We observe that all field lines are closed and have an elliptical shape. Figures [\[Figure-B3-field-dens-cont\]](#Figure-B3-field-dens-cont){reference-type="ref" reference="Figure-B3-field-dens-cont"} and [1](#Figure-B3-field-lines-on-torus){reference-type="ref" reference="Figure-B3-field-lines-on-torus"} visualize the toroidal structure of the individual fields at the example of $\bB^3$. Using $\bA^3 =   A^3_r\, \be_r + A^3_\vartheta\, \be_\vartheta + 
                 A^3_\varphi\, \be_\varphi$ and $\frac{\p}{\p \varphi}\bA^3=0$ it follows that $\bB^3$ can be written $$\bB^3 = \nabla\times\bA^3 = \frac{1}{r\sin\vartheta}
         \nabla(r\sin\vartheta A^3_\varphi)\times\be_\varphi
                           + B^3_\varphi\be_\varphi.$$ Therefore, the field lines of $\bB^3$ lie on $\varphi$-invariant toroidal surfaces described by $r\sin\vartheta A^3_\varphi = \mbox{const}$. Figure [\[Figure-B3-field-dens-cont\]](#Figure-B3-field-dens-cont){reference-type="ref" reference="Figure-B3-field-dens-cont"} shows the poloidal $\bB^3$-field and contour lines for three different values of $r\sin\vartheta A^3_\varphi$. A toroidal surface with $r\sin\vartheta A^3_\varphi = -1.8$ and four field lines on it is drawn in Figure [1](#Figure-B3-field-lines-on-torus){reference-type="ref" reference="Figure-B3-field-lines-on-torus"}. The central field line, sitting within all tori is characterized by $B^3_r = B^3_\vartheta = 0$. In view of the last equation, this is equivalent to $\nabla(r\sin\vartheta A^3_\varphi)=0$ which yields $r=\sqrt{1/3}$ and $\vartheta=\pi/2$. We observe that all field lines wind around the central field line exactly once. From this and the toroidal structure of $\bB^3$ we can conclude that any two arbitrary field lines $l$ and $l'$ of $\bB^3$ have a Gauß  linkage $lk(l,l')=1$.

Finally let us discuss the linking properties among field lines of different fields. To give an example, one field line of each field is plotted in Figure [\[Figure-B-1-2-3-field-lines\]](#Figure-B-1-2-3-field-lines){reference-type="ref" reference="Figure-B-1-2-3-field-lines"}. The symmetric appearance is due to the choice of symmetric starting points for the field line integration. As was stressed above, the magnetic fields $\bB^i$ can be obtained from one another by cyclic permutations of the Cartesian coordinates $x^i$. In the same way the integration starting points for the field lines $\gamma^1$, $\gamma^2$ and $\gamma^3$ where chosen to be the cyclic permuted coordinate triples $(0, 0.8, 0)$, $(0, 0, 0.8)$ and $(0.8, 0, 0)$. It is interesting that the total linkage of the set of field lines is $\text{lk}(\gamma^1,\gamma^2)+
 \text{lk}(\gamma^2,\gamma^3)+
 \text{lk}(\gamma^3,\gamma^1)=-3$. Even though we have seen that the mutual cross-helicities of all three fields vanish, their individual field lines, in general, are linked pairwise. To be more precise: If we e.g. fix one field line $\gamma^3$ of $\bB^3$, then all field lines of $\bB^1$ and $\bB^2$ are either linked with $\gamma^3$ exactly once or they intersect $\gamma^3$ twice. For reasons of symmetry, there exists for each field line $\gamma^1$ of $\bB^1$ a field line $\tilde{\gamma}^1$ of $\bB^1$, such that we find the total linkage $\text{lk}(\gamma^1,\gamma^3) + \text{lk}(\tilde{\gamma}^1,\gamma^3)=0$. Hence, the cross-helicity $H(\bB^1,\gamma^3)$ vanishes, which in turn implies $H(\bB^1, \bB^3)=0$. Figure [2](#Figure-zero-cross-helicity){reference-type="ref" reference="Figure-zero-cross-helicity"} shows such field lines $\gamma^1$, $\tilde{\gamma}^1$ and $\gamma^3$ with $(0, 0.8, 0)$, $(0, -0.8, 0)$ and $(0.8, 0, 0)$ as their respective starting points for the field line integration. Finally let us remark that in the same way as we obtained $\tilde{\gamma}^1$ we can obtain field lines $\tilde{\gamma}^2$ and $\tilde{\gamma}^3$, here with integration starting points $(0, -0.8, 0)$, $(0, 0, -0.8)$ and $(-0.8, 0, 0)$. Together, these three field lines yield a configuration complementary to the one shown in Figure [\[Figure-B-1-2-3-field-lines\]](#Figure-B-1-2-3-field-lines){reference-type="ref" reference="Figure-B-1-2-3-field-lines"}, which now has a total linkage of $+3$.
