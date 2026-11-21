---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-016-42-selecting-local-deformations
section_title: "Selecting local deformations"
section_number: 4.2
pages: 19-21
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.978
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#subsec:Vnonempty label="subsec:Vnonempty"}

Each choice of $\bar{s} = (s_1, \dots, s_n)$ corresponds to a local deformation with 1--form $(\omega_0)_j$ expressed in $V_j$ as in equation ([\[eqn:omega_0-S\]](#eqn:omega_0-S){reference-type="ref" reference="eqn:omega_0-S"}). In terms of the deformation, varying $\bar{s}$ varies the rates at which the cone angles are changing (instantaneously). When $\bar{s}=(1, \dots, 1)$, all cone angles are changing at the same rate. It might be convenient to let $\bar{s}=(1, \dots, 1)$, to simplify calculations. However, such a choice may not give us the bounds on $\sum b_j$ that we need.

In particular, we would like to select $\bar{s}$ such that we may use certain inequalities from [@hk:univ]. (These inequalities appear in the proof of Lemma [\[lemma:b_j-bound\]](#lemma:b_j-bound){reference-type="ref" reference="lemma:b_j-bound"} in this paper.) In order to use these inequalities, we will need to find $\bar{s}$ such that each $b_j(\bar{s}) \geq 0$.

The existence of such an $\bar{s}$ has been discovered by Hodgson and Kerckhoff, but their result is unpublished, so we include it as Lemma [\[lemma:Vnonempty\]](#lemma:Vnonempty){reference-type="ref" reference="lemma:Vnonempty"} here.

::: lemma
There is an $\bar{s}\neq 0$ for which $b_j(\bar{s})\geq 0$ for all $j=1, 2, \dots, n.$ []{#lemma:Vnonempty label="lemma:Vnonempty"}
:::

::: proof
*Proof.* It suffices, by rescaling, to restrict $\bar{s}$ to the simplex $$T=\{\bar{s}=(s_1, \dots,s_n) | \sum_j s_j = n, s_j \geq 0\}.$$

We first set up some notation.

Let the $j$-th vertex of $T$ be denoted $t_j$. So $t_j = (0, \dots,
0, n, 0, \dots, 0)$ where the single non-zero value is in the $j$-th location. Notice that at $t_j$, $b_i(t_j)\leq 0$ for all $i\neq j$. Because the sum of the $b_i$ is always strictly positive, we must have $b_j(t_j)>0$.

Let the face of $T$ opposite $t_j$ be denoted $f_j$. That is, on $f_j$ the $j$-th coordinate is always $0$. Notice that on $f_j$, $b_j
\leq 0$. We will assume that $b_j < 0$ on $f_j$. If not, consider instead level sets of $b_j$ for values $\epsilon > 0$ arbitrarily close to $0$. Below, we will be finding points where all the $b_j$ are positive. Taking a limit will at least give points where the $b_j$ are nonnegative.

We will also assume level sets $b_j=0$ intersect transversely. If not, take an arbitrarily small perturbation of the quadratic functions (keeping them quadratic).

First we note that the set where $b_j>0$ is an open neighborhood of $t_j$ in $T$. This is because on any line from $t_j$ to $f_j$, $b_j$ goes from positive to negative. Because $b_j(s)$ is quadratic in $s$, $b_j=0$ on this line in exactly one value. Thus the level set $b_j=0$ separates $t_j$ from $f_j$. It has a well--defined positive and negative side.

Now, we prove the following sublemma by induction.

::: lemma
Consider the $k-1$ simplex $S_k$ of $T$ where $s_i=0$ for all $i>k$. There exists a nonempty open set $B_k \subseteq S_k$ where $b_j>0$ for all $j\leq k$. Furthermore, the set $E_k\subseteq S_k$ where $b_j=0$ for all $j<k$ is an odd number of points, each on the boundary of $B_k$. []{#lemma:sub-vnonempty label="lemma:sub-vnonempty"}
:::

Notice that in the above statement, when $k=n$, the simplex $S_n$ is all of $T$. Then if the statement is true, $B_n$ is an open set on which all the $b_j$ are positive, so this will prove Lemma [\[lemma:Vnonempty\]](#lemma:Vnonempty){reference-type="ref" reference="lemma:Vnonempty"}.

An additional fact we will pick up from the proof is that the set $E_n$ where $b_j=0$ for $j=1, 2, \dots, n-1$ is an odd number of points. (We will use this additional fact in the proof of Lemma [\[lemma:choose-S\]](#lemma:choose-S){reference-type="ref" reference="lemma:choose-S"} below.)

::: proof
*Proof.* We first prove Lemma [\[lemma:sub-vnonempty\]](#lemma:sub-vnonempty){reference-type="ref" reference="lemma:sub-vnonempty"} when $k=2$. In this case, $S_2$ is the 1--simplex from $t_1$ to $t_2$. At $t_1$, $b_1>0$. At $t_2$, $b_1 <0$. Since $b_1$ is quadratic, somewhere on $S_2$ is a single point $e_2$ where $b_1=0$. Notice that $b_2(e_2)$ must be positive. This is because each $b_j(e_2)\leq 0$ for $j>2$ (since the corresponding coordinates $s_j$ are all zero). Since $b_1(e_2)$ is zero, and the sum $\sum b_i >0$, this forces $b_2>0$. Then in this case, $E_2$ contains the single point $e_2$. $B_2$ is nonempty, with $e_2$ on its boundary.

<figure id="fig:findv">

<figcaption>Proof of Lemma <a href="#lemma:Vnonempty" data-reference-type="ref" data-reference="lemma:Vnonempty">[lemma:Vnonempty]</a> when <span class="math inline"><em>k</em> = 3</span>.</figcaption>
</figure>

We will now prove the lemma by induction for $k+1$. For reference, an example of the case when $k+1=3$ is illustrated in Figure [1](#fig:findv){reference-type="ref" reference="fig:findv"}.

$S_{k+1}$ is the $k$ subsimplex of $T$ with vertices $t_1, t_2, \dots,
t_{k+1}$, on which $s_{k+2}= \dots = s_n=0$. It has as one boundary face the $k-1$ simplex $S_k$, on which $s_{k+1}= s_{k+2}= \dots
=s_n=0$. On any other face of $S_{k+1}$, $s_{k+2}=\dots=s_n=0$, and also $s_j=0$ for some $j<k+1$.

By induction, we are assuming that on the face $S_k$ the set $B_k$, where $b_j>0$ for all $j\leq k$ is a nonempty open set. By continuity, the set $\hat{B}_k$ in $S_{k+1}$ where the same $b_j>0$ must also be nonempty.

The set $\hat{E}_k \subset S_{k+1}$ where $b_j=0$ for $j<k$ is a $1$--manifold with boundary. A neighborhood of $E_k$ in $\hat{E}_k$ lies in the boundary of $\hat{B}_k$.

Consider $\hat{E}_k$. As a 1--manifold, it consists of closed components and arcs. The part of its boundary contained in $S_k$ is the set $E_k$, so consists of an odd number of points. Hence there must be an odd number of arc components of $\hat{E}_k$ with exactly one endpoint in $S_k$.

Consider the other boundary components of $\hat{E_k}$. They must lie on faces of $S_{k+1}$. Recall the set $\{b_j=0\}$ does not intersect any face $f_j$ where $s_j=0$. Thus the only possible additional face of intersection of $\hat{E_k}$ and $S_{k+1}$ is the face on which $s_k=s_{k+2}=\dots=s_n=0$, spanned by vertices $t_1, \dots, t_{k-1}$ and $t_{k+1}$ (note this face is in $f_k$). By induction (using the induction hypothesis with vertices renumbered), there are an odd number of intersection points of $\hat{E_k}$ on this face of $S_{k+1}$.

Thus there must be an odd number of arcs of $\hat{E_k}$ running from $S_k$ to the face $f_k$. Along any of these arcs, $b_k$ goes from positive (at a point of $E_k$ on $S_k$) to negative (since $b_k<0$ on $f_k$). Thus it must be zero at an odd number of interior points. Each of these points is in $E_{k+1}$. We may also have points of $E_{k+1}$ coming from the intersection of $\{b_k=0\}$ with closed components of $\hat{E}_k$, or with arc components of $\hat{E}_k$ with both endpoints of the arc on the same face (either $S_k$ or $f_k$). In the former case, $\{b_k=0\}$ must intersect any closed component an even number of times, and in the latter case $b_k$ has the same sign on both endpoints, so again $\{b_k=0\}$ intersects the arc an even number of times. Thus the total number of points in $E_{k+1}$ is odd.

At each point in $E_{k+1}$, we have $b_1=b_2=\dots=b_k=0$, and we have $b_{k+2}$ through $b_n$ all less than or equal to zero. Since the sum of all the $b_j$ is positive, $b_{k+1}$ must be positive. This implies $B_{k+1}$ is a nonempty open set, and the points of $E_{k+1}$ are on its boundary. ◻
:::

This completes the proof of Lemma [\[lemma:Vnonempty\]](#lemma:Vnonempty){reference-type="ref" reference="lemma:Vnonempty"}. ◻
:::

Now, as mentioned above, the choice of $\bar{s}$ is tied to the rates at which the cone angles are varying. Lemma [\[lemma:Vnonempty\]](#lemma:Vnonempty){reference-type="ref" reference="lemma:Vnonempty"} implies that a desired $\bar{s}$ exists, but gives us no further information about $\bar{s}$. In particular, some cone angle may reach $2\pi$ before the others. When this happens, the hyperbolic structure in the corresponding tube about the singular locus is nonsingular. We may thus view the deformation from this point on as a deformation on a cone manifold with one fewer component of the singular locus. We do this, obtaining deformations with fewer and fewer singular components, until each cone angle has reached $2\pi$.
