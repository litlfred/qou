---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-020-51-tropical-polygons
section_title: "Tropical polygons"
section_number: 5.1
pages: 54-58
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.971
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:tropical-polygons label="sec:tropical-polygons"}

Let $\nabla$ denote the canonical torsion-free flat connection on $B$ associated to the affine structure. The following definitions are due to Abouzaid [@abouzaid-msri-dec09].

::: definition
[]{#def:tropical-disk label="def:tropical-disk"} Let $B$ be a two-dimensional singular affine manifold with focus-focus singularities, and let $x \in B$ be a non-singular point. Let $\Gamma$ be a tree all of whose edges are finite. Label one univalent vertex $p_{\text{out}}$, and denote the other univalent vertices by $p_1,\dots,p_r$. A *tropical disk* in $B$ ending at $x$ is a balanced tropical embedding $v : \Gamma \to B$, satisfying the following conditions.

1.  $v(p_{\text{out}}) = x$,

2.  For $i = 1,\dots,r$, $v(p_i)$ is a singular point of the affine structure, and $v$ maps the (unique) edge incident to $p_i$ into a monodromy-invariant line of the singularity.
:::

In the case at hand, there is only one singularity, so the only such tropical disks are line segments emanating from the singular point in the monodromy-invariant direction. If there were more singularities with intersecting monodromy-invariant lines, we could obtain more complicated tropical disks.

::: definition
[]{#def:tropical-polygon label="def:tropical-polygon"} Let $q_0, q_1, \dots, q_k$ be points of $B$, with $q_j \in
  B(\frac{1}{d_j}\Z)$. Let $\Gamma$ be a metric ribbon tree with $k+1$ infinite edges. One infinite edge, the *root*, is labeled with $q_0$ and it is the output. The other $k$ infinite edges, the *leaves*, are labeled with $q_1,\dots,q_k$ in counterclockwise order and these are the inputs. Assign to the region between $q_j$ and $q_{j+1}$ the weight $\sum_{i=1}^jd_i$, and give the region between $q_0$ and $q_1$ weight $0$. Orient the tree upward from the root, so that each edge has a "left" and a "right" side coming from the ribbon structure. To each edge $e$, assign a weight $w'_e$ given by the weight on the left side of $e$ minus the weight on the right side of $e$. Define a corrected weight $w_e$ by $$\begin{split}
      w_e = 0 & \text{ if $w'_e < 0$ and $e$ contains a leaf}\\
      w_e = 0 & \text{ if $w'_e > 0$ and $e$ contains the root}\\
      w_e = w'_e &\text{ otherwise}
    \end{split}$$ Then a *tropical polygon* modeled on $\Gamma$ is a map $u:
  \Gamma \to B$ such that:

1.  $u$ converges on the root edge to $q_0$ and on the $j$-th leaf edge to $q_j$;

2.  on the edge $e$, the tangent vector $\dot{u}_e$ to the component $u_e$ satisfies $$\nabla_{\dot{u}_e} \dot{u}_e = w_e \dot{u}_e$$ and $\dot{u}_e$ converges to $0$ on the infinite ends of the root and leaf edges; this differential equation only holds outside a finite set of points where tropical disks are attached;

3.  there exists a finite collection of tropical disks $v_1,\dots,v_N$ such that the union $u \cup \{v_1,\dots,v_N\}$ is balanced; the balancing condition at a vertex $x$ is the vanishing of the sum of the derivative vectors $\dot{u}_e$ of the various components of $u$ incident at $x$ and the integral tangent vectors to $v_i$ at $x$, oriented toward the vertex.
:::

The heuristic motivation for these definitions is that, if we consider a deformation of complex structures in which the torus fibers collapse, we expect that a family of honest holomorphic polygons will likewise collapse onto a piecewise linear complex in $B$. We further expect that two types of local limiting behavior can occur. Some parts of the curve may limit to surfaces that fiber over straight lines in $B$ intersecting the torus fibers in paths joining two Lagrangian sections, while other parts may limit to surfaces that fiber over straight lines in $B$ intersecting the torus fibers in circles. The latter are what become the tropical disks, while the former become the rest of the tropical polygon. The balancing condition comes from the necessity that these parts can be connected up to form a topological polygon with boundary on the Lagrangian sections. See also [@d-branes-book Ch. 8].

To unpack this definition, let us restate it in the simplest case, which is that of tropical triangles (this mainly simplifies the issues regarding weights):

::: proposition
[]{#prop:tropical-triangles label="prop:tropical-triangles"} Let $q_1 \in B(\frac{1}{n}\Z)$ and $q_2 \in B(\frac{1}{m}\Z)$, with $n > 0$ and $m > 0$. Let $q_0 \in B(\frac{1}{n+m}\Z)$. Let $\Gamma$ be the ribbon tree with one vertex and three infinite edges. Then a tropical triangle modeled on $\Gamma$ consists of three maps $u_0: [0,\infty) \to B$, $u_1: (-\infty,0] \to B$, $u_2:
  (-\infty,0] \to B$ such that

1.  $u_0 \equiv q_0$ is a constant map;

2.  $u_1(0) = u_2(0) = q_0$;

3.  $u_1(-\infty) = q_1$, $u_2(-\infty) = q_2$;

4.  We have $\nabla_{\dot{u}_1} \dot{u}_1 =
        n\dot{u}_1$ and $\nabla_{\dot{u}_2} \dot{u}_2 = m\dot{u}_2$, outside of a finite set of points where tropical disks are attached;

5.  there exists a finite collection of tropical disks $v_1,\dots,v_N$ such that the balancing condition holds.
:::

We can also unpack the equation $\nabla_{\dot{u}} \dot{u} =
n\dot{u}$. The key outcome of the following Lemmas is the insight that the tangent vector $\dot{u}$ increases by $n$ times the distance the path $u$ travels. Recall that a path $\gamma$ is called a geodesic for a connection $\nabla$ if $\nabla_{\dot{\gamma}} \dot{\gamma} = 0$.

::: lemma
Let $\gamma: [0,1] \to B$ be a geodesic for $\nabla$. Define $u :
  (-\infty,0] \to B$ by $u(t) = \gamma(\exp(nt))$. Then at the point $x = \gamma(s)$, we have $\dot{u} = ns\dot{\gamma}$, and $\nabla_{\dot{u}} \dot{u} = n\dot{u}$.
:::

::: proof
*Proof.* We set $s = \exp(nt)$. The equation $\dot{u} = ns\dot{\gamma}$ is just the chain rule (note that $\dot{u} = du/dt$ while $\dot{\gamma} =
  d\gamma/ds$). We have $$\nabla_{\dot{\gamma}} \dot{u} = \nabla_{\dot{\gamma}} (ns\dot{\gamma}) = n\dot{\gamma}
    + ns\nabla_{\dot{\gamma}}\dot{\gamma} = n\dot{\gamma}$$ since $\gamma$ is a geodesic. Multiplying this equation by $ns$, and using the fact that $\nabla$ is tensorial in its subscript, we obtain $\nabla_{\dot{u}} \dot{u} = n\dot{u}$. ◻
:::

::: lemma
[]{#lem:differences label="lem:differences"} Let $u: [a,b] \to B$ solve $\nabla_{\dot{u}}\dot{u} =
  n\dot{u}$. Then if we patch together affine charts along $u$ to embed a neighborhood of $u$ into $\R^n$, we have $$\dot{u}(b) - \dot{u}(a) = n(u(b)-u(a))$$ where we use the affine structure of $\R^n$ to take differences of points and vectors at different points.
:::

::: proof
*Proof.* Define $\gamma: [\exp(na),\exp(nb)] \to B$ by $\gamma(s) = u((\log
  s)/n)$, so that $\gamma$ is a geodesic. We can embed a neighborhood of $\gamma$ into $\R^n$ by patching together affine coordinate charts along $\gamma$. Using addition in this embedding, we can write $\gamma(s) = \gamma(\exp(na)) + (s-\exp(na))\dot{\gamma}$. We have $\dot{u}(\log(s)/n) = ns\dot{\gamma}(s)$, and $$\dot{u}(b) - \dot{u}(a) =n(\exp(nb)-\exp(na))\dot{\gamma} =
    n(\gamma(\exp(nb)) - \gamma(\exp(na))) = n(u(b)-u(a))$$ ◻
:::

One more thing to note regarding these tangent vectors $\dot{u}$ is how they represent homology classes on the torus fibers of the fibration over $B$.

When considering a tropical curve $C^\trop$ corresponding to a closed holomorphic curve $C$, each edge of the tropical curve carries an integral tangent vector, which morally represents the class $[C\cap
T^2_b] \in H_1(T^2_b;\Z)$ that measures how the holomorphic curve intersects the torus fiber $T^2_b = \pi^{-1}(b)$. Because the curve is closed, this class is locally constant along each edge of $C^\trop$.

When considering a tropical curve $C^\trop$ representing a holomorphic curve $C$ with boundary on Lagrangian sections $L(i),L(j)$, the intersection of $C$ with $T^2_b$ would morally be a path on $T^2_b$ from $L(i)_b$ to $L(j)_b$, where $L(i)_b$ is intersection of $T^2_b$ and $L(i)$. Let $A(L(i)_b,L(j)_b) \subset
H_1(T^2_b,\{L(i)_b,L(j)_b\};\Z)$ be the subset consisting of such cycles, which could also be described as the preimage of $L(j)_b -
L(i)_b \in H_0(\{L(i)_b,L(j)_b\};\Z)$ under the boundary homomorphism. Hence $A(L(i)_b,L(j)_b)$ is a torsor for the kernel of that homomorphism, which is $H_1(T^2_b;\Z)$. Using the group structure on $T^2_b$, we can identify $A(L(i)_b,L(j)_b)$ with the coset $$+ H_1(T^2_b;\Z) \subset H_1(T^2_b;\R)$$ On the other hand, there is an isomorphism $(T_bB)_\R \cong
H_1(T^2_b;\R)$. Hence the class of $[C\cap T^2_b]$ can be regarded as a tangent vector to the base, which is in general real and varies along the tropical curve as $L(i)$ and $L(j)$ move relative to one another. The tangent vector $\dot{u}$ to the tropical curve is this class.

The balancing condition at a vertex $b$ of the tropical polygon amounts to requiring that the three paths $L(i)_b\to L(j)_b$, $L(j)_b
\to L(k)_b$ and $L(k)_b\to L(i)_b$ form a contractible loop. At a point where a tropical disk is attached, the path $L(i)_b \to L(j)_b$ changes discontinuously by a loop in the homology class in $H_1(T^2_b;\Z)$ corresponding to the integer tangent vector to the tropical disk.

The last thing to describe for tropical polygons is their multiplicities. There is a multiplicity coming from the different ways to attach a disk $v$ to the tropical polygon. If one incoming edge of the polygon has tangent vector $\dot{u}_e$ corresponding to a path $\gamma_1: L(i)_b \to L(j)_b$ on $T^2_b$, and the disk has tangent vector $w$ corresponding to a loop $\gamma_2$ on $T^2_b$, there are $|\gamma_1.\gamma_2| = |\det(\dot{u}_e, w)|$ points where the disk can be attached, assuming this determinant is an integer (as it is in the special case below). Otherwise, one must look carefully at exactly where on the torus the paths $\gamma_1$ and $\gamma_2$ are located.

For a tropical disk $v$, we also expect the Gross--Siebert theory to associate a multiplicity $m(v)$. Morally speaking, this number should be a virtual count of holomorphic disks corresponding to $v$, and it should possible to extract this from the "structure" on the affine base in the sense of [@gs-affine-complex]. In the case at hand, where the base has just a single focus-focus singularity, all of these factors are expect to be one for simple disks, and zero for multiply covered disks [@abouzaid-comm]. In the rest of this section, we adopt this as an ansatz. Modulo this ansatz, we show in Proposition [\[prop:tropical-our-case\]](#prop:tropical-our-case){reference-type="ref" reference="prop:tropical-our-case"} that the tropical curve counts agree with the holomorphic curve counts computed in Section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}. From a certain point of view, this may be regarded as evidence for the ansatz itself, since tropical curve invariants are intentionally designed to correspond to holomorphic curve invariants, and we have computed the latter.

In summary, the multiplicity of a tropical polygon will have both the Gross--Siebert factors $m(v)$ counting how many holomorphic disks are in each class, as well as simpler factors counting how many ways these classes of disks can be attached.

::: remark
After this paper was originally written, an exposition of the closely related idea of *jagged paths* appeared [@gs-theta Definition 3.2]. In that paper, the various multiplicities are packaged in a different way, but it turns out the that tropical curve counts defined there also agree, in the case of $(\CP^2,D)$, with the holomorphic curve counts computed in Section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}. The multiplicities we seek are packaged into certain series $f_{\mathfrak{d}} = 1 + \sum_p c_pz^p$ where $\mathfrak{d}$ runs over certain distinguished rays and lines in $B$. See [@gs-theta §3] for more explanation. In our case, there are two such rays emanating from the singularity of the affine structure in the monodromy invariant directions. Our ansatz is equivalent to the fact that the corresponding series reduce, in appropriate choices of coordinates, to $1 + z$ and $1+w$ respectively. The salient feature is that these series have a linear term with coefficient $1$ and no higher degree terms.
:::
