---
doc_id: arxiv-math-0505056v2
doc_title: "Matrix factorizations and link homology II"
section_id: sec-000-matrix-factorizations-with-a-parameter
section_title: "Matrix factorizations with a parameter"
section_number: null
pages: 1-12
source_pdf: 0505056v2.pdf
source_sha256: 1b6580406c3d35b5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.988
doc_brief: "Matrix factorizations and link homology II — To a presentation of an oriented link as the closure of a braid we assign a complex of bigraded vector spaces."
---
[]{#section-one label="section-one"}

In the paper \[KR\] we constructed, for each $n>0,$ a bigraded cohomology theory of links in $\R^3$ whose Euler characteristic is a certain one-variable specialization $(q^n,q)$ of the HOMFLYPT polynomial \[HOMFLY\], \[PT\]. The $n=0$ specialization is the Alexander polynomial, equal to the Euler characteristic of the knot homology theory discovered by Ozsváth, Rasmussen and Szabó \[OS\], \[R1\]. The approach in \[KR\] fails for $n=0,$ assigning trivial groups to any link.

In this sequel to \[KR\] we assume that the reader is familiar with that paper. Recall that our construction of link cohomology was based on matrix factorizations with potentials being sums and differences of $x^{n+1},$ for various $x.$ When $n=0,$ the category of matrix factorizations (up to chain homotopies) with the potential $\sum \pm x_i$ is trivial. Looking for a remedy, let us add a formal variable $a$ and change the potential from $x$ to $ax.$

Take an oriented arc $c$ as in figure [1](#arc){reference-type="ref" reference="arc"}, label its ends $x_1$ and $x_2,$ and assign the potential $ax_1 - ax_2$ to the arc. Let $R=\Q[a,x_1,x_2]$ and define $C_c$ as the factorization $$R \stackrel{a}{\lra} R \xrightarrow{x_1 -x_2} R.$$ We have $d^2= ax_1 - ax_2$ and view $C_c$ as an object of the homotopy category of matrix factorizations with the potential $a(x_1-x_2).$

<figure id="arc">

<figcaption>An arc</figcaption>
</figure>

Make $R$ bigraded by setting $$\label{degrees}\deg(a) = (2,0), \hspace{0.3in} \deg(x_i)=(0,2).$$ This implies $\deg(d^2) = (2,2)$ and we select the bigrading of the middle $R$ in the factorization so that $\deg(d)= (1,1)$: $$\label{arcfact} 
  R \stackrel{a}{\lra} R\{-1,1\} \stackrel{x_1 -x_2}{\lra} R,$$ where the bidegree shift by $(n_1,n_2)$ is denoted $\{n_1,n_2\}.$

<figure id="xonefour">

<figcaption>Wide edge <span class="math inline"><em>t</em></span></figcaption>
</figure>

Next, given a wide edge $t$ as in figure [2](#xonefour){reference-type="ref" reference="xonefour"}, assign variables $x_1,x_2,x_3,x_4$ to the edges next to it. We can write $$ax_1 + ax_2 - ax_3 -ax_4 = a(x_1+x_2-x_3-x_4) + 0 (x_1 x_2-x_3x_4).$$ Define $C_t$ as the tensor product (over $R$) of factorizations $$R \stackrel{a}{\lra} R\{-1,1\} \xrightarrow{x_1+x_2-x_3-x_4} R$$ and $$R\stackrel{0}{\lra} R\{-1,3\} \xrightarrow{x_1 x_2 - x_3 x_4} R$$ where $R= \Q[a,x_1,x_2,x_3,x_4].$

Throughout the paper we work with matrix factorizations with potentials $w=a \sum_i \epsilon_i x_i$ where $i$ ranges over some finite set $I$ of integers and $\epsilon_i\in \{1,-1\}$ are \"orientations\" of $x_i.$ The category $mf_w$ has objects $(M,d)$ where $M=M^0\oplus M^1$ and $M^0,M^1$ are free bigraded $R$-modules (possibly of infinite rank), while $d$ is a generalized differential $$M^0 \stackrel{d}{\lra} M^1 \stackrel{d}{\lra} M^0$$ of bidegree $(1,1)$ and subject to $d^2=w.$ Here $R$ is the ring of polynomials in $a$ and $x_i$'s with rational coefficients. The bidegrees are given by formula ([\[degrees\]](#degrees){reference-type="ref" reference="degrees"}). Morphisms in $mf_w$ are bidegree-preserving maps of $R$-modules $M^0\to N^0,$ $M^1\to N^1$ that commute with $d.$

We found it useful to visualize a matrix factorization as above by decomposing $$M^0={\mathop{\oplus}\limits_{k,l}} M^0_{k,l}, \hspace{0.2in} 
 M^1={\mathop{\oplus}\limits_{k,l}} M^1_{k,l},$$ as direct sums of vector spaces, one for each bidegree $(k,l),$ and placing them in the nodes of a coordinate lattice, see figure [3](#lattice){reference-type="ref" reference="lattice"}. Diagonal arrows denote the differential, horizontal arrows show multiplication by $a$ and vertical arrows--multiplications by $x_i.$

<figure id="lattice">

<figcaption>Lattice of factorization <span class="math inline"><em>M</em></span></figcaption>
</figure>

The category $hmf_w$ of matrix factorizations up to chain homotopies has the same objects as $mf_w$ and the $\Q$-vector space of morphisms from $M$ to $N$ is the quotient of the space of morphisms in $mf_w$ by null-homotopic morphisms (the homotopy maps must have bidegree $(-1,-1)$).

If the index set $I$ is empty, then $R=\Q[a]$ and $mf_w$ is equivalent to the category of complexes of free graded $\Q[a]$-modules.

<figure id="diagbound">

<figcaption>Graph <span class="math inline"><em>Γ</em>,</span> an example</figcaption>
</figure>

In general, given a planar marked graph $\Gamma$ (as described in \[KR, Introduction\]), possibly with boundary points, we assign to it a matrix factorization $C(\Gamma)$ which is the tensor product of $C_c,$ over all arcs $c$ in $\Gamma,$ and $C_t,$ over all wide edges $t$ in $\Gamma.$ For instance, for the graph in figure [4](#diagbound){reference-type="ref" reference="diagbound"}, $$C(\Gamma) = C_{t_1} \otimes C_{t_2} \otimes C_{c_1} \otimes C_{c_2}$$ where $c_1,c_2$ are the arcs of $\Gamma$ with endpoints labelled $x_3,x_5$ and $x_7,x_6,$ respectively. The tensor product is taken over suitable polynomial rings $\Q[a,x_i]$ so that $C(\Gamma)$ is a finite rank free $\Q[a,x_1, \dots, x_9]$-module. The potential $$w=a(x_1 + x_2 - x_7 - x_4 - x_8 -x_9)$$ and we view $C(\Gamma)$ as an object of $mf_w$ (or $hmf_w$) with the ground ring $R$ the polynomial ring $\Q[a,x_1,x_2,x_4,x_7,x_8,x_9]$ in $a$ and external (or boundary) variables. The other variables $x_3,x_5,x_6$ are \"internal\". Notice that $C(\Gamma)$ has infinite rank as an $R$-module.

When $\Gamma$ has no boundary points, $w=0$ and $C(\Gamma)$ becomes a 2-periodic complex $$C^0(\Gamma) \stackrel{d}{\lra} C^1(\Gamma) \stackrel{d}{\lra} C^0(\Gamma)$$ of bigraded $\Q[a]$-modules. Its cohomology, denoted $H(\Gamma),$ is a bigraded $\Q[a]$-module.

If $\Gamma$ is a single circle with one mark (glue together the endpoints of the arc in the figure [1](#arc){reference-type="ref" reference="arc"} and place a mark there), the complex is $$\Q[a, x_1] \stackrel{a}{\lra}\Q[a,x_1]\{-1,1\} \stackrel{0}{\lra} \Q[a,x_1]$$ (since now $x_2=x_1$), and $H(\Gamma)\cong \Q[x_1]\{-1,1\}.$

<figure id="pair2">

<figcaption>Graphs <span class="math inline"><em>Γ</em><sup>0</sup></span> and <span class="math inline"><em>Γ</em><sup>1</sup></span></figcaption>
</figure>

Consider the diagrams $\Gamma^0, \Gamma^1$ in figure [5](#pair2){reference-type="ref" reference="pair2"}. Factorization $C(\Gamma^0)$ is the tensor product of $$R \stackrel{a}{\lra} R\{-1,1\} \xrightarrow{x_1-x_4} R$$ and $$R \stackrel{a}{\lra} R\{-1,1\} \xrightarrow{x_2-x_3} R,$$ where $R=\Q[a,x_1,x_2,x_3,x_4].$ In the product basis, $C(\Gamma^0)$ has the form $$\begin{array}{l}R \\  \oplus \\ R\{-2,2\}\end{array}
  \stackrel{P_0}{\lra}
  \begin{array}{l} R\{-1,1\} \\ \oplus \\ R\{-1,1\}  \end{array}
  \stackrel{P_1}{\lra} 
  \begin{array}{l}R \\ \oplus \\ R\{-2,2\}\end{array}$$ with $$P_0=\left(\begin{array}{cc} a  & x_3-x_2 \\
      a   & x_1-x_4 \end{array} \right), \hspace{0.2in}
P_1=\left(\begin{array}{cc} x_1-x_4  & x_2-x_3 \\
      -a  & a \end{array} \right).$$

Likewise, $C(\Gamma^1)$ has the presentation $$\begin{array}{l}R \\ \oplus \\ R\{-2,4\}\end{array}
  \stackrel{Q_0}{\lra}
  \begin{array}{l} R\{-1,1\} \\ \oplus \\ R\{-1,3\}  \end{array}
  \stackrel{Q_1}{\lra} 
  \begin{array}{l}R \\ \oplus \\ R\{-2,4\}\end{array}$$ with $$Q_0=\left(\begin{array}{cc} a  & x_3x_4-x_1x_2 \\
      0   & x_1+x_2-x_3-x_4 \end{array} \right), \hspace{0.2in}
Q_1=\left(\begin{array}{cc} x_1+x_2-x_3-x_4  & x_1x_2-x_3x_4 \\
      0  & a \end{array} \right).$$ A map between $C(\Gamma^0)$ and $C(\Gamma^1)$ can be described by a pair of $2\times 2$ matrices with coefficients in $R$ that specify the images of the basis vectors of $C^i(\Gamma^0)$ in $C^i(\Gamma^1)$ for $i=0,1.$

Let $\chi_0: C(\Gamma^0) \lra C(\Gamma^1)$ be given by the pair of matrices $$\label{chinull} 
U_0^0=\left(\begin{array}{cc} x_4-x_2  &  0  \\
      0   &  1  \end{array} \right), \hspace{0.2in}
U_0^1=\left(\begin{array}{cc} x_4  &  -x_2 \\
      -1  & 1 \end{array} \right).$$ Our bases in $C(\Gamma^0)$ and $C(\Gamma^1)$ are homogeneous with respect to the bigrading of $R.$ It's easy to see that $\chi_0$ is a homogeneous map of bidegree $(0,2).$

Next, define $\chi_1: C(\Gamma^1) \lra C(\Gamma^0)$ by the pair of matrices $$\label{chione} 
U_1^0=\left(\begin{array}{cc} 1  &  0  \\
      0   &  x_4-x_2  \end{array} \right), \hspace{0.2in}
U_1^1=\left(\begin{array}{cc} 1  &  x_2 \\
      1  & x_4 \end{array} \right).$$ The map $\chi_1$ is bidegree-preserving.

Given a plane diagram $D$ of a tangle, place at least one mark on each internal edge of the diagram (an edge disjoint from the boundary of $D$), and label the marks and boundary points by $x_1, \dots, x_m.$ To each crossing $p$ of the diagram assign the complex $C_p$ of matrix factorizations as follows. Up to shifts, the complex is the cone of the map $\chi_0$ or $\chi_1,$ depending on whether the crossing is positive or negative. The shifts are explained in figure [6](#cones){reference-type="ref" reference="cones"}.

<figure id="cones">

<figcaption>Complex assigned to a crossing</figcaption>
</figure>

Thus, if the crossing is positive, $$C_p = \hspace{0.3in} 0 \lra C(\Gamma^0)\{0,2\} \stackrel{\chi_0}{\lra} 
 C(\Gamma^1) \lra 0 ,$$ with $C(\Gamma^1)$ positioned in cohomological degree $0.$ The shift $\{0,2\}$ makes the differential preserve the bidegree. If the crossing is negative, $$C_p = \hspace{0.3in} 0 \lra C(\Gamma^0)\{0,-2\} \stackrel{\chi_0}{\lra} 
 C(\Gamma^1)\{0,-2\} \lra 0 ,$$ with $C(\Gamma^0)$ in cohomological degree $0.$ The overall bigrading shift by $\{0,-2\}$ is here for the normalization of the Reidemeister move IIa (see later).

Define $C(D)$ as the tensor product of $C_p,$ over all crossings $p$ of $D,$ and $C_c,$ over all arcs $c.$ It's a complex built out of matrix factorizations $C(\Gamma),$ over all resolutions $\Gamma$ of $D.$ The differential $\partial$ preserves the bigrading of each term $C^j(D).$ We view $C(D)$ as an object of the category $K(hmf_w).$ The latter is the category whose objects are complexes of objects in $hmf_w$ and whose morphisms are homomorphism of complexes modulo null-homotopic morphisms.

Now we specialize to the case when $D$ is a link diagram (has empty boundary). Then each term $C^j(D)$ in the complex $C(D)$ is an object of the homotopy category of bigraded free $\Q[a]$-modules. We'll see that $C^j(D),$ for any diagram $D,$ decomposes as a direct sum of contractible pieces $$0 \lra \Q[a] \stackrel{1}{\lra} \Q[a] \lra 0$$ and the cohomology $H(C^j(D)),$ which we denote $CH^j(D).$ Moreover, $a$ acts trivially on $CH^j(D),$ so we can ignore the $\Q[a]$-module structure and think of it as a bigraded $\Q$-vector space, $$CH^j(D) = {\mathop{\oplus}\limits_{k,l}} CH^j_{k,l}(D).$$ The bigrading descends from the bigrading on matrix factorizations $C(\Gamma).$

Thus, to $D$ we assign the complex $CH(D)$ of bigraded $\Q$-vector spaces $$\dots \stackrel{\partial}{\lra}  
  CH^j(D)  \stackrel{\partial}{\lra} CH^{j+1}(D) \stackrel{\partial}{\lra} \dots$$ As a $\Q$-vector space, $CH(D)$ is the direct sum of cohomology groups $H(\Gamma)$ of complexes $C(\Gamma),$ over all resolutions of $D.$

The cohomology $H(D) = H(CH(D),\partial)$ of the above complex is triply-graded, $$H(D) = {\mathop{\oplus}\limits_{j,k,l}} H^j_{k,l}(D).$$

Of course, for the whole construction to be interesting, $H(D)$ should not depend on the choice of $D,$ given $L.$

::: prop
[]{#prop-mark label="prop-mark"} Let $D$ be a marked tangle diagram. Then $C(D)$, as an object of $K(hmf_w),$ does not depend on the number of markings on each edge of $D.$
:::

Proposition [\[prop-mark\]](#prop-mark){reference-type="ref" reference="prop-mark"} is proved in the next section.

Next we run into an obstacle: things seem to work well only if we restrict to diagrams $D$ that come from braids. Let's say that $D$ is a braid diagram if $D$ depicts the link $L$ as the closure of a clockwise oriented braid, see figure [7](#braid){reference-type="ref" reference="braid"}. We denote the braid by $D$ as well.

<figure id="braid">

<figcaption>A braid diagram</figcaption>
</figure>

To justify the introduction of braid diagrams, partition the Reidemeister moves of links into types I, II, III in the usual way and then separate II into two subtypes, IIa and IIb, depending on orientations, see figure [8](#reid){reference-type="ref" reference="reid"}. We only consider the type III move with the orientations pointing in the same direction.

<figure id="reid">

<figcaption>Reidemeister moves</figcaption>
</figure>

::: prop
If diagrams $D_1, D_2$ are related by a Reidemeister move of type I, IIa or III, the complexes $C(D_1)$ and $C(D_2)$ are isomorphic as objects of the category $K(hmf_w),$ up to an overall shift in the triple grading.
:::

For a proof see Section [\[sec-proofs\]](#sec-proofs){reference-type="ref" reference="sec-proofs"}.

It seems likely to us that $C(D_1)$ and $C(D_2)$ are not isomorphic (up to a shift) if $D_1, D_2$ are the two tangles in the IIb move in figure [8](#reid){reference-type="ref" reference="reid"}, although we did not prove this. To avoid the IIb move, we restrict our consideration to braid diagrams. Closures of braid diagrams $D_1, D_2$ are isotopic as oriented links iff $D_1, D_2$ are related by a chain of Markov moves. A Markov move is one of the following:

\(a\) conjugation $DD' \leftrightarrow D'D,$

\(b\) transformations in the braid group: $$\begin{aligned}
D\sigma_j \sigma_i & \leftrightarrow & D \sigma_i \sigma_j \hspace{0.1in} \mathrm{if} 
 \hspace{0.1in} |i-j|>1, \\ 
D & \leftrightarrow & D \sigma_i \sigma_i^{-1},  \\
D & \leftrightarrow & D \sigma_i^{-1} \sigma_i,  \\
D \sigma_i \sigma_{i+1}\sigma_i & \leftrightarrow & D \sigma_{i+1}
  \sigma_{i} \sigma_{i+1} .
\end{aligned}$$

\(c\) transformations $D \leftrightarrow D \sigma_n^{\pm 1},$ for a braid $D$ with $n$ strands.

Notice that we never see the Reidemeister move IIb when dealing with braid diagrams. The propositions stated earlier imply:

::: theorem
Given two braid diagrams $D_1,D_2$ of an oriented link $L,$ the cohomology groups $H(D_1)$ and $H(D_2)$ are isomorphic as triply-graded vector spaces, up to an overall shift in the grading.
:::

To describe the Euler characteristic of $H(D),$ we consider the function $F$ from braid diagrams to the ring of rational functions in $q$ and $t$ that is uniquely determined by the following properties:

-   $F(D_1)=F(D_2)$ if $D_1,D_2$ are conjugate braid presentations (see Markov move (a) above),

-   $F(D_1)=F(D_2)$ if $D_1,D_2$ are related by a braid presentation move (Markov moves (b) above),

-   $F(D \sigma_n) = F(D),$ for a braid $D$ with $n$ strands,

-   $F(D\sigma_n^{-1})= - t^{-1}q^{-1} F(D),$ for a braid $D$ with $n$ strands,

-   For any braid diagram $D$ there is a skein relation $$q^{-1} F(D \sigma_i) - q F(D \sigma_i^{-1})= (q-q^{-1})
     F(D),$$

-   If $D$ is the one-strand diagram of the unknot, $F(D)=\frac{t^{-1}}{q^{-1}-q}.$

To see that $F$ is simply a version of the HOMFLYPT polynomial, let $\alpha= - t^{-1}q^{-1}$ and consider $$\widetilde{F}(D) = \sqrt{\alpha}^{|D|_+ - |D|_-  - s(D)+1}  F(D)$$ where $|D|_+,$ respectively $|D|_-,$ is the number of positive, respectively negative, crossings of $D,$ while $s(D)$ is the number of strands of $D.$ Our conventions are explained in figure [9](#conv){reference-type="ref" reference="conv"}.

<figure id="conv">

<figcaption>Positive and negative crossings and braid generators</figcaption>
</figure>

Then $\widetilde{F}(D)$ is invariant under all Markov moves of braids and satisfies the HOMFLYPT skein relation $$\label{homfly-rel}
 q \sqrt{\alpha}\hspace{0.05in} \widetilde{F}(D\sigma_i^{-1}) - 
 (q \sqrt{\alpha})^{-1} \widetilde{F}(D\sigma_i) = (q-q^{-1}) \widetilde{F}(D).$$ Thus, $\widetilde{F}(D)$ equals the HOMFLYPT polynomial of the link $L,$ normalized so that $$\widetilde{F}(\mathrm{unknot})= \frac{\alpha }{1-q^{-2}}.$$

::: theorem
[]{#sec-thm label="sec-thm"} For any braid diagram $D$ the Euler characteristic $\langle D \rangle$ of $H(D)$ equals $F(D).$
:::

The Euler characteristic $$\label{euler-char} 
  \langle D \rangle \define \sum_{j,k,l}(-1)^j t^k q^l \dim_{\Q} 
 H^j_{k,l}(D)$$ is a power series in $q$ with coefficients in $\Z[t,t^{-1}].$ The theorem claims that each vector space $H^j_{k,l}(D)$ is finite dimensional and the sum above is a rational function of $t$ and $q$ equal to $F(D).$ See the end of Section [\[sec-proofs\]](#sec-proofs){reference-type="ref" reference="sec-proofs"} for a proof.

Specializing to $q\sqrt{\alpha}=1$ in the equation ([\[homfly-rel\]](#homfly-rel){reference-type="ref" reference="homfly-rel"}) nets us the Alexander polynomial. In terms of $t$ and $q,$ we are imposing the relation $t=-q.$ Homologically, $t,$ $q$ and the minus sign correspond to the three grading directions. Hence, suitably collapsing the tri-grading to a bigrading we get a categorification of the Alexander polynomial.

Sergei Gukov, Albert Schwarz and Cumrun Vafa recently conjectured \[GSV\] that there exist integer-valued link invariants $D_{Q,s,r}$ depending on three integer parameters $Q,s,r,$ that can be used to determine ranks of sl(n) link homology groups as well as the coefficients of the HOMFLYPT polynomial of a link. These invariants should come from the physical theory of the BPS states and should be related to ranks of cohomology groups of suitable moduli spaces. It would be interesting to try relating $D_{Q,s,r}$ to the dimensions of cohomology groups $H^j_{k,l}.$ Our normalization of the HOMFLYPT polynomial is similar to the one in \[GSV\], both having $q-q^{-1}$ as the denominator of the unknot invariant.

On the other hand, it's been independently suggested by several people, including Oleg Viro \[V\], that there should exist a triply-graded link homology theory with the HOMFLYPT polynomial as the Euler characteristic. The current paper resulted from our search for such a theory and for a combinatorial categorification of the Alexander polynomial.

Triply-graded cohomology theories had previously appeared in the work of Asaeda, Przytycki and Sikora \[APS\] on categorification of invariants of links in I-bundles over surfaces, and in Audoux and Fiedler \[AF\], who introduced a refined Jones polynomial and its categorification, which are only invariant under braid-like isotopies. Restriction to braid-like isotopies appears in our construction as well, but we don't know how our invariant relates to those of \[APS\] and \[AF\].

To conclude this section, we mention several modifications, potential generalizations and illnesses of the homology theory $H.$

-   It's not natural that we have to restrict to braid diagrams to get a link invariant. In another sign of disfunctionality, the theory does not extend to all cobordisms. For instance, the cohomology groups of the unknot do not have a Frobenius algebra structure over the cohomology ring of the empty link (it's convenient to define the latter ring to be $\Q[a]$), preventing us from extending the theory even to unknotted cobordisms between unlinks.

-   Any field $k$ can be used instead of $\Q.$ More generally, we can work over $\Z,$ so that the invariant of a closed planar graph $\Gamma$ is a complex of graded free abelian groups, up to chain homotopy equivalence, and the invariant of a link is a complex of complexes as above, up to chain homotopy equivalence. Taking the homology $H(\Gamma,\Z)$ of each resolution of $D$ and forming a complex out of them produces a complex $CH(D,\Z)$ from a diagram $D.$ We then specialize to braid diagrams and take the cohomology of $CH(D,\Z).$ The resulting groups $H(D,\Z)$ are triply-graded and, up to isomorphism, do not depend on the choice of braid diagram $D,$ given $L.$

-   In Section [\[sec-proofs\]](#sec-proofs){reference-type="ref" reference="sec-proofs"} we rewrite the factorizations $C(\Gamma^0), 
    C(\Gamma^1)$ and the maps $\chi_0,$ $\chi_1$ in the form that depends only on $a$ and the differences $x_i-x_j$ of the variables $x_i.$ This allows us to pass from the ring $R=\Q[a,x_1, \dots, x_m]$ to the smaller ring $\overline{R}=\Q[a,x_2-x_1, \dots, x_m-x_1].$ The definition of cohomology and the proof of its invariance work over $\overline{R}$ as well, leading to *reduced* cohomology groups $\overline{H}(D),$ with the property $H(D)= \overline{H}(D)\otimes_{\Q} \Q[x].$ In the reduced theory the unknot has one-dimensional cohomology groups.

-   $sl(n)$ link homology theory (see \[KR\]) utilized the potential $x^{n+1}.$ Soon afterwards Gornik \[G\] studied a deformation of that theory with the potential $x^{n+1}-(n+1)\beta^n x.$ In the $n=2$ case the deformation was found earlier by Lee \[L\] and used by Rasmussen in his combinatorial proof of the Milnor conjecture \[R2\]. The definitions in \[KR\] can be generalized to the potential $x^{n+1}+a_n x^n + \dots + a_1 x$ where $a_1, \dots, a_n$ are formal variables. We hope that this generalization will be invariant under the Reidemeister moves and will turn out to be the \"$sl(n)$-equivariant\" version of $sl(n)$ link homology. The invariant of the empty link should be the ring of polynomials in $a_1, \dots, a_n,$ and naturally isomorphic to the $U(n)$-equivariant cohomology ring of the point. The invariant of the unknot should be the quotient of the polynomial ring $\Q[x,a_1, \dots, a_n]$ by the relation $x^{n+1}+a_n x^n + \dots + a_1 x=0,$ isomorphic to the $U(n)$-equivariant cohomology ring of $\mathbb{CP}^n.$ A certain version of Bar-Natan link homology \[BN\], \[K\] should correspond to the potential $x^3+ a x.$

-   For a common generalization of the $U(n)$-equivariant link homology and the theory described here one could try the potential $a_{n+1}x^{n+1}+a_n x^n + \dots + a_1 x$ with all $a$'s being formal variables. Factorizations $C(\Gamma^0), C(\Gamma^1),$ the maps $\chi_0, \chi_1$ and the complex $C(D)$ can be defined for this potential as well, but we don't know whether this theory will be invariant under the Reidemeister-Markov moves of braid diagrams.
