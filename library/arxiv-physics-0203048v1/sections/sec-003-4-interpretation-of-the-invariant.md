---
doc_id: arxiv-physics-0203048v1
doc_title: "arXiv:physics/0203048v1 [physics.plasm-ph] 15 Mar 2002"
section_id: sec-003-4-interpretation-of-the-invariant
section_title: "Interpretation of the invariant"
section_number: 4
pages: 6-11
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.99
---
It is interesting to note that the new third-order invariant comes on an equal footing as the conservation of helicity, since both invariants where derived from the same identity ([\[Chern-Simons\]](#Chern-Simons){reference-type="ref" reference="Chern-Simons"}). However, contrary to the conservation of helicity, the third-order integral cannot be applied to a single magnetic field, but requires a triplet of fields. Thus we have to interpret this integral in the sense of the cross-helicity rather than the total helicity. A forthcoming paper will deal with the question of how a single magnetic field might be split into a triplet of fields with the required properties $\nabla\cdot\bG^i=0$, thereby linking the given *cross* third-order invariant and a *total* third-order invariant.

There is another way of looking at the new third-order invariant. By writing $$H^{(3)}(\bB^1,\bB^2,\bB^3) = \int_{V} \bA^1\cdot\bG_B^1
   \dxxx = H(\bB^1, \bG_B^1) \ ,$$ the integral is to be interpreted as the cross-helicity of the two divergence-free fields $\bB^1$ and $\bG_B^1$. Note that the boundary conditions for the cross-helicity, namely $\bB^1\cdot\bn=0$ and $\bG_B^1\cdot\bn=0$, are fulfilled due to condition ([\[H-3-condition-2\]](#H-3-condition-2){reference-type="ref" reference="H-3-condition-2"}) of the theorem. From this new interpretation the condition $\nabla\cdot\bG_B^1=0$ is an obvious requirement analogous to $\nabla\cdot\bB=0$. Furthermore, the symmetry of $H^{(3)}$ leads to $$H(\bB^1, \bG_B^1) = H(\bB^2, \bG_B^2) = H(\bB^3, \bG_B^3),
   \label{H-3-cross-helicity}$$ which reveals the additional conditions $\nabla\cdot\bG_B^2=0$ and $\nabla\cdot\bG_B^3=0$. Let us note that this interpretation does not simplify the direct calculation of the third-order invariant. It is still necessary to determine the fields $\bG_B^i$ which are not independent of the chosen representatives $\bA^i$.

Third-order linking integrals for magnetic fields have been constructed from the Massey triple product already by Monastyrsky and Sasorov (1987), Berger (1990) and also Ruzmaikin and Akhmetiev (1994). However, these constructions are limited to cases where the three fields are confined to three isolated and mutually unlinked flux tubes with disjunct support. It is in fact easy to see that for this special case their invariants coincide with the integral ([\[H-3-continuous-integral\]](#H-3-continuous-integral){reference-type="ref" reference="H-3-continuous-integral"}) given above. An explicit proof is given in [\[Equivalentintegrals\]](#Equivalentintegrals){reference-type="ref" reference="Equivalentintegrals"}. In particular, it is worth noting that for fields with mutually disjunct support the condition $\nabla\cdot \bG^i_B=0$ implies that the cross-helicity of all pairs of fields vanishes, i.e. their flux tubes have to be mutually unlinked.

For a set of three arbitrary magnetic fields $\nabla\cdot \bG^i_B=0$ cannot always be satisfied. To show that there are examples for which this can be satisfied, beyond the cases of three fields with mutually disjunct support, we give an explicit example in the next section.

# Example of three magnetic fields with a third-order linkage

In this section we want to give an example of three magnetic fields not confined to flux tubes, which firstly allow for one-form potentials that obey $\d(A^i \wedge A^j)=0$ and where secondly the integral invariant ([\[H-3-continuous-integral\]](#H-3-continuous-integral){reference-type="ref" reference="H-3-continuous-integral"}) yields a non-trivial result. The existence of such an example proves that the new invariant is indeed a generalization of the third-order invariant derived from a Massey triple product which was applicable merely to unlinked flux tubes. The fields we construct show an extraordinary high symmetry. For this reason they are interesting in their own right.

The idea to construct three fields $A^i$ on $\reals^4$ which obey $\d(A^i \wedge A^j)=0$ comes from Yang-Mills theory: An $SU(2)$ Yang-Mills field $$F = \d A - iq A \wedge A$$ can, in view of ([\[SU-two-AandF\]](#SU-two-AandF){reference-type="ref" reference="SU-two-AandF"}) and the identities for Pauli matrices ([\[Pauli-matrices-identities\]](#Pauli-matrices-identities){reference-type="ref" reference="Pauli-matrices-identities"}), be written as $$F^\indi = \d A^\indi + q\,\epsilon_{\indi\indj\indk}A^\indj\wedge
   A^\indk. \label{F-alpha-vanishes}$$ By taking the exterior derivative of $F$, $$\d F^\indi = q\,\epsilon_{\indi\indj\indk}\d(A^\indj\wedge A^\indk),
   \label{dF-su2}$$ we immediately observe that $\d F=0$ is a sufficient condition for all $\d(A^\indi \wedge A^\indj)$ to vanish. In the special case of a vacuum Yang-Mills field, i.e. $F=0$, the requirement $\d F=0$ is trivially fulfilled. If we now reinterpret the three components of the Yang-Mills potential as potentials of three independent magnetic fields, we have constructed an example field configuration to which the invariant ([\[H-3-continuous-integral\]](#H-3-continuous-integral){reference-type="ref" reference="H-3-continuous-integral"}) can be applied.

## Yang-Mills potentials of a vacuum field with non-vanishing winding number

An $SU(2)$ Yang-Mills vacuum field is now constructed on a time slice $\reals^3$ of $\reals^4$ using the mapping $g: \reals^3 \rightarrow SU(2)$ (see e.g. Frankel 1997, Itzykson and Zuber 1980) $$g(\bx) \,=\, \text{exp}\left[\frac{i\pi \; x^j \sigma_j}
                          {\sqrt{||\bx||^2 + \lambda^2}}\right].
                        \label{g-original}$$ Interpreted as a gauge transformation of an $SU(2)$ classical vacuum, i.e. with vanishing connection $\omega = 0$, $g(\bx)$ gives rise to the pure gauge connection $$\omega = g^{-1}(\bx)\d g(\bx),\label{pure-gauge-omega}$$ and the Yang-Mills potential one-form $A = \frac{i}{q}\omega$ reads $$A^j \sigma_j = \frac{i}{q}g^{-1}(\bx)\d g(\bx).
         \label{pure-gauge-omega-A}$$ At this point we want to remark that the vacuum winding number of $\omega$, which is defined to be the degree of the map $g$, is $W(g)=1$. An important consequence of this non-trivial winding number will be a non-trivial value of the invariant $H^{(3)}$, as can be seen in equations ([\[H-3-in-example\]](#H-3-in-example){reference-type="ref" reference="H-3-in-example"}) and ([\[H-3-and-W\]](#H-3-and-W){reference-type="ref" reference="H-3-and-W"}) below.

In order to explicitly calculate the one-form potential $A$ given by the last expression we use that $g(\bx)$, as an element of $SU(2)$, has the form $$\begin{aligned}
   g(\bx) = \exp\left(\frac{1}{2i}\sigma_j n^j \right)
          = \cos\left({\frac{f}{2}}\right) 
                  -i \sigma_j \hat{n}^j \sin\left({\frac{f}{2}}\right),
                  \label{g-in-exp-form}
\end{aligned}$$ where $\bn = f {\hat\bn}$ and where $\hat{\bn}$ is a unit vector in $\reals^3$ with coordinate components $\hat{n}^j = x^j/||\bx||$. A comparison with ([\[g-original\]](#g-original){reference-type="ref" reference="g-original"}) shows $$\begin{aligned}
   f &= - \frac{2 \pi \,||\bx||}{\sqrt{||\bx||^2 + \lambda^2}}. \label{definition-f}
\end{aligned}$$ Substituting ([\[g-in-exp-form\]](#g-in-exp-form){reference-type="ref" reference="g-in-exp-form"}) into ([\[pure-gauge-omega-A\]](#pure-gauge-omega-A){reference-type="ref" reference="pure-gauge-omega-A"}) we obtain after some calculation $$A^\indi =  \frac{1}{2q}\left[
               \hat{n}^\indi\,\d f + \d \hat{n}^\indi \,\sin{f} 
               +
               \epsilon_{\indi\indj\indk}\,\hat{n}^\indj\,\d\hat{n}^\indk 
               (\cos{f}-1)\right]. \label{Yang-Mills-potential-components}$$

## Magnetic fields constructed from Yang-Mills potentials

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
