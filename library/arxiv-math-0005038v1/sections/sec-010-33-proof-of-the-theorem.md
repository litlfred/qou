---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-010-33-proof-of-the-theorem
section_title: "Proof of the Theorem"
section_number: 3.3
pages: 9-10
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.819
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
In this subsection we use the Basic Lemma and the Key Lemma to prove that the Lawrence-Krammer representation is faithful. The following lemma will be useful.

::: lem
[]{#digon label="digon"} Let $\alpha$ and $\beta$ be simple closed curves in $D \setminus P$ which intersect transversely at finitely many points. The following are equivalent.

-   $\alpha$ is isotopic relative to $\partial D \cup P$ to a simple closed curve which intersects $\beta$ at fewer points,

-   $\alpha$ and $\beta$ cobound a "digon", that is, an embedded disc in $D \setminus P$ whose boundary consists of one subarc of $\alpha$ and one subarc of $\beta$.
:::

A proof can be found in [@paris-rolfsen Proposition 3.7], or [@flp Proposition 3.10].

Suppose $\sigma \in {\mathcal{H}}(D,P)$ is a homomorphism representing an element of the kernel of the Lawrence-Krammer representation. We will show that $\sigma$ is isotopic relative to $\partial D \cup P$ to the identity map.

Take $D$ to be the unit disc centered at the origin in the complex plane, and take $p_1,\dots,p_n$ to be real numbers satisfying $-1 < p_1 < \dots < p_n < 1$. For $i = 1,\dots,n-1$, let $E_i$ be the horizontal edge from $p_i$ to $p_{i+1}$. For $i = 1,\dots,n$, let $N_i$ be the noodle which winds around $p_i$ and no other punctures, intersecting the real axis twice.

<figure id="stdnoodle">
<div class="picture">
<p>(120,130)(0,-10)</p>
<p>(60,60)</p>
<p>(50,1)(74,73)(83,70) (70,1)(92,67)(83,70)</p>
<p>(45,-10)<span><span class="math inline"><em>d</em><sub>1</sub></span></span> (65,-10)<span><span class="math inline"><em>d</em><sub>2</sub></span></span></p>
<p>(20,60) (40,60) (60,60) (80,60) (100,60)</p>
<p>(20,60)(40,60)</p>
</div>
<figcaption>The edge <span class="math inline"><em>E</em><sub>1</sub></span> and the noodle <span class="math inline"><em>N</em><sub>4</sub></span></figcaption>
</figure>

See Figure [1](#stdnoodle){reference-type="ref" reference="stdnoodle"}.

Let $F$ be a fork such that $T(F) = E_1$. Then $\langle N_3,F \rangle = 0$. By the Basic Lemma, $\langle N_3,\sigma(F) \rangle = 0$. By the Key Lemma, it follows that $\sigma(E_1)$ is isotopic relative to $\partial D \cup P$ to an arc which is disjoint from $N_3$. By composing $\sigma$ with an element of ${\mathcal{I}}(D,P)$ if necessary, we can assume that $\sigma(E_1)$ is disjoint from $N_3$.

Similarly, $\sigma(E_1)$ can be isotoped so as to be disjoint from $N_4$. By Lemma [\[digon\]](#digon){reference-type="ref" reference="digon"}, this isotopy can be performed by a sequence of moves which consist of eliminating digons, and hence do not introduce any new intersections with $N_3$. Thus we can assume that $\sigma(E_1)$ is disjoint from both $N_3$ and $N_4$.

Continuing in this way, we can assume that $\sigma(E_1)$ is disjoint from $N_i$ for all $i = 3,\dots,n$. By applying one final isotopy relative to $\partial D \cup P$, we can assume that $\sigma(E_1) = E_1$. Note that we have not yet eliminated the possibility that $\sigma$ reverses the orientation of $E_1$.

We can repeat the above procedure to isotope $\sigma(E_2)$ to $E_2$ while leaving $E_1$ fixed. Continuing in this way, we can assume that $\sigma(E_i) = E_i$ for all $i = 1,\dots,n-1$. It follows that $\sigma$ must be isotopic relative to $\partial D \cup P$ to $(\Delta^2)^k$ for some $k \in {\bf{Z}}$, where $\Delta^2$ is a Dehn twist about the boundary of a collar neighborhood of $\partial D$. However, the induced action of $\Delta^2$ on $H_2(\tilde{C})$ is simply multiplication by $q^{2n}t^2$. Since $\sigma$ acts trivially on $H_1(\tilde{C})$ we have that $k=0$, so $\sigma$ represents the trivial braid.
