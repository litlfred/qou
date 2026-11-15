---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-001-2-fricke-klein-example
section_title: "Fricke-Klein example"
section_number: 2
pages: 3-8
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.982
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
## Equations

This example was essentially worked out in [@fricke1965vorlesungen]. Let $k=4$, $n=2$. Let $a_1,\ldots,a_4\in\mathbb C\setminus\{-2,2\}$. Let us try to parameterize all $4$-tuples of $2\times 2$ matrices $M_1, M_2, M_3, M_4\in \mathrm{GL}_2(\mathbb{C})$, up to conjugation, satisfying $$\prod_{i=1}^4 M_i = I_2, \quad \det M_i = 1, \quad \mathop{\mathrm{tr}}M_i=a_i.$$ Let $x=\mathop{\mathrm{tr}}(M_1 M_2)$, $y=\mathop{\mathrm{tr}}(M_1 M_3)$, $z=\mathop{\mathrm{tr}}(M_2 M_3)$. The following code computes the ideal of relations between $x,y,z$:

            R.<m111,m112,m121,a1,m211,m212,m221,a2,m311,m312,m321,a3,x,y,z,a4>=QQ[]
            M1=matrix(2,2,[m111,m112,m121,a1-m111])
            M2=matrix(2,2,[m211,m212,m221,a2-m211])
            M3=matrix(2,2,[m311,m312,m321,a3-m311])
            eqns=[M1.det()-1,M2.det()-1,M3.det()-1,(M1*M2*M3).trace()-a4,(M1*M2).trace()-x, \
            (M1*M3).trace()-y,(M2*M3).trace()-z]
            J=R.ideal(eqns)
            J.elimination_ideal([m111,m112,m121,m211,m212,m221,m311,m312,m321])

The output is

                Ideal (a1*a2*a3*a4 - a1*a2*x - a1*a3*y - a2*a3*z + x*y*z - a3*x*a4 - a2*y*a4 - a1*z*a4
                + a1^2 + a2^2 + a3^2 + x^2 + y^2 + z^2 + a4^2 - 4) of Multivariate Polynomial Ring in 
                m111, m112, m121, a1, m211, m212, m221, a2, m311, m312, m321, a3, x, y, z, a4 over 
                Rational Field  

So for each $4$-tuple of matrices satisfying the conditions, the corresponding $x, y, z\in\mathbb C$ as above produce a solution to the so called *Markov equation* with parameters $a_1, a_2, a_3, a_4$: $$\begin{gathered}
\label{eq:markov}
        xyz + x^2 + y^2 + z^2 - (a_1 a_2 + a_3 a_4) x - (a_1 a_3 + a_2 a_4) y - (a_1 a_4 + a_2 a_3) z \\
        + a_1 a_2 a_3 a_4 + a_1^2 + a_2^2 + a_3^2 + a_4^2 - 4=0.
    
\end{gathered}$$

Conversely, suppose $x, y, z\in\mathbb C$ is a solution to the Markov equation. Let us see that for generically chosen values $a_1, a_2, a_3, a_4$ we can always uniquely recover the tuple of matrices, up to conjugation.

First, we observe that knowing the traces $x, y, z, a_1, a_2, a_3, a_4$ we can compute the trace of an arbitrary product of matrices $M_1,\ldots,M_4$ and their inverses. Indeed, given such a product, we first replace any occurrence of $M_4$ by $M_3^{-1} M_2^{-1} M_1^{-1}$. Then using $$A^{-1} = \mathop{\mathrm{tr}}(A) I_2 - A \qquad (A\in \mathop{\mathrm{SL}}_2(\mathbb C))$$ we can reduce to the situation when no inverses appear. So we have an arbitrary product of $M_1, M_2, M_3$. Using $$BA = \mathop{\mathrm{tr}}(BA) I_2 - A^{-1} B^{-1} \qquad (A,B\in \mathop{\mathrm{SL}}_2(\mathbb C))$$ and getting rid of the inverses we rearrange terms modulo products of shorter length until we get to a linear combination of $I_2$, $M_1$, $M_2$, $M_3$, $M_1 M_2$, $M_1 M_3$, $M_2 M_3$, $M_1 M_2 M_3=M_4^{-1}$, all of whose traces are explicitly computed in terms of $x, y, z$ and the parameters.

Knowing the traces of arbitrary products lets us find out if any $4$ products form a basis of the space of $2\times 2$ matrices. Indeed, because the trace pairing is non-degenerate, matrices $A_1,\ldots,A_{n^2}$ form a basis of the space of $n\times n$ matrices if and only if the $n^2 \times n^2$ matrix of traces $\mathop{\mathrm{tr}}(A_i A_j)$ is non-degenerate.

Suppose products of $M_1,\ldots,M_4$ do span the space of matrices, i.e. the monodromy representation is irreducible, and we choose a basis $A_1, \ldots, A_4$. Knowing the traces allows us to express any other product as a linear combination of $A_1,\ldots, A_4$. In particular we recover the ring structure on the $4$-dimensional space of linear combinations of $A_1,\ldots,A_4$ and any monodromy representation provides an isomorphism of this ring with the matrix ring. Any other monodromy representation with the same traces would produce an automorphism of the matrix ring. All automorphisms of the matrix ring are inner, i.e. related by a change of basis transformation, and so we conclude that the monodromy representations with the same traces are equivalent.

This was under the assumption that the monodromy representation is irreducible. If it is not, then in some basis the matrices $M_1,\ldots,M_4$ are upper triangular. In this situation we cannot determine the matrices only from the trace information. Denoting the top-left diagonal entry of $M_i$ by $\lambda_i$ we must have $\prod_{i=1}^4 \lambda_i=1$. On the other hand, $\lambda_i$ is a root of the polynomial $t^2 - a_i t + 1$ which has $2$ roots. So this kind of situation is possible only for special values of the parameters $a_1, a_2, a_3, a_4$.

More precisely, we call $a_1, a_2, a_3, a_4$ *generic* if none of the 16 products of the roots of $t^2 - a_i t + 1$ (we pick one root from each quadratic equation) equals $1$. We have seen, that if the parameters are generic then all monodromy representations are irreducible and in one-to-one correspondence with the solutions of the Markov equation.

## Geometry of the Markov cubic

In algebraic geometry, given an algebraic variety $X$, i.e. a set of solutions to a system of polynomial equations, we are usually interested in its cohomology ring $H^*(X,\mathbb C)$. Hodge theory extended by Deligne to non-compact and singular spaces [@deligne1971theorie; @deligne1974theorie] endows the cohomology with *mixed Hodge structure*. Structure constants of the ring typically encode interesting enumerative information. Sometimes the cohomology ring as a ring itself can be an interesting object of study, perhaps making a connection with a ring constructed in some other way in a completely different field of mathematics.

Although the ring structure in the Fricke-Klein situation turns out to be trivial, the cohomology already has a non-trivial mixed Hodge structure. We explain how to compute it.

<figure id="fig:triangle">

<figcaption><span id="fig:triangle" label="fig:triangle"></span>Markov’s cubic as the complement of a triangle in the projective plane blown up at six points</figcaption>
</figure>

Assuming the parameters $a_1,a_2,a_3,a_4\in \mathbb C\setminus\{-2,2\}$ are generic, the cubic $X$ given by the Markov equation [\[eq:markov\]](#eq:markov){reference-type="eqref" reference="eq:markov"} is nonsingular. Let $\overline{X}\subset \mathbb C\mathbb P^3$ be the solution set of the homogenization of [\[eq:markov\]](#eq:markov){reference-type="eqref" reference="eq:markov"}. Its affine part is $X\subset \overline{X}$, and the complement $\overline{X}\setminus X$ is given in $\mathbb C\mathbb P^2$ as the solution set of the homogeneous equation $xyz=0$, thus it is a union of three lines forming a triangle. Denote this triangle by $\Delta$. We refer to Figure [1](#fig:triangle){reference-type="ref" reference="fig:triangle"}. It is straightforward to check that homogenization of any cubic of the form $$xyz + x^2 + y^2 + z^2 + \text{lower degree terms}$$ does not have any singularities at infinity. So $\overline{X}$ is a smooth cubic surface, and therefore can be obtained as a blowup of $\mathbb C\mathbb P^2$ at $6$ points (for background see [@hartshorne1977algebraic]). The cubic $\overline{X}$, as any other smooth cubic surface contains $27$ projective lines. Three of them form $\Delta$. The intersection graph of the $27$ lines is well-known and one can see that for any triangle one can choose $6$ lines which do not intersect pairwise and do not contain any of the lines of the triangle. Each side of the triangle intersects $2$ of the $6$ lines. Blowing down these $6$ lines we obtain a map $\overline{X}\to \mathbb C\mathbb P^2$. The $3$ lines of $\Delta$ are isomorphically mapped to $3$ lines on $\mathbb C\mathbb P^2$. Choosing coordinates appropriately, one can assume that $f(\Delta)$ is the complement of $\mathbb C^*\times\mathbb C^*\subset \mathbb C\mathbb P^2$. So we have $$U = f^{-1}(\mathbb C^*\times\mathbb C^*) = \mathbb C^*\times\mathbb C^* \subset X,$$ an open subset, and the complement $X\setminus U$ is a disjoint union of $6$ copies of $\mathbb C$: $$X = \mathbb C^*\times\mathbb C^* \sqcup \underbrace{\mathbb C\sqcup \cdots \sqcup \mathbb C}_{\text{$6$ copies}}.$$ The $6$ copies of $\mathbb C$ are divided into $3$ pairs according to which of the three lines of $\Delta$ they intersect.

## Cohomology

With this picture in mind, we have several ways to compute the cohomology. All cohomology groups we consider have complex coefficients. From the relative cohomology sequence for the pair $\mathbb C^*\times\mathbb C^* = U\subset X$ we obtain an exact sequence $$0\to H^1(X) \to H^1(U) \to H^2(X,U) \to H^2(X) \to H^2(U) \to 0.$$ Since both $\mathbb C$ and $X$ are non-singular, by excision we have that the only non-vanishing relative cohomology group is $H^2(X, U)\cong \mathbb C^6$. So the remaining part of the long exact sequence vanishes, except for the isomorphism $H^0(X)\cong H^0(U)\cong \mathbb C$. The map $\mathbb C^2 = H^1(U) \to H^2(X,U)=\mathbb C^6$ is dual to the map $H_2(X,U) \to H_1(U)$. Here a point class on $\mathbb C$ corresponds to a disc class in $H_2(X,U)$ whose boundary is a $1$-cycle in $U$ which gets contractible in $U\cup \mathbb C$. From the picture we see that all $1$-cycles become contractible, so the map $H_2(X,U) \to H_1(U)$ is surjective, the dual map is injective and we have $H^1(X)=0$, $H^2(X)$ is an extension of $H^2(U)=\mathbb C$ by $H^2(X,U)/H^1(U)\cong\mathbb C^4$.

This is reflected by the weight filtration on $H^2(X)$. The cohomology $H^2(X,U)/H^1(U)\subset H^2(X)$ as a mixed Hodge structure is pure of weight $2$, while $H^2(U)$ has weight $4$. Thus we have $W_2 = H^2(X,U)/H^1(U)\subset H^2(X)$ with $\dim W_2=4$, $W_3=W_2$, and $W_4 = H^2(X)$ with $\dim W_4/W_2 = 1$.

Another way to compute the cohomology is to use the compactification. Let us denote $X_0=\overline{X}$, $X_1 = X_0\setminus \mathbb C\mathbb P^1$, $X_2=X_0\setminus (\mathbb C\mathbb P^1 \cup \mathbb C\mathbb P^1)$, $X_3=X_0\setminus \Delta$, so that we pass from $X_i$ to $X_{i+1}$ by removing a line. This leads to exact sequences for each $i$: $$0\to H^1(X_{i+1})\to H^2(X_i, X_{i+1}) \to H^2(X_i)\to H^2(X_{i+1}) \to H^3(X_i,X_{i+1}) \to 0$$ $$0\to H^3(X_{i+1}) \to H^4(X_i,X_{i+1}) \to H^4(X_i)\to H^4(X_{i+1}) \to 0,$$ as we will see that the even cohomologies of $X_i$ vanish at each step. At each step we will use that $H^k(X_i, X_{i+1})=H^{k-2}(X_i\setminus X_{i+1})$ by excision, which is non-zero only for $k=0,1,2$. Initially we have $H^0(X_0)=\mathbb C$, $H^2(X_0)=\mathbb C^7$ (represented by $7$ algebraic cycles: the line in $\mathbb C\mathbb P^2$ and the $6$ exceptional curves), $H^4(X_0)=\mathbb C$, all other cohomologies vanish.

For $i=0$ we have $X_0\setminus X_1=\mathbb C\mathbb P^1$, which has $H^0=\mathbb C$ and $H^2=\mathbb C$. These coincide with $H^2(X_0,X_1)$ and $H^4(X_0,X_1)$ respectively and we see that in $H^2(X_1)$ and in $H^4(X_1)$ we have one less dimension than in $H^2(X_0)$, respectively $H^4(X_0)$. So $H^4(X_1)=0$, $H^2(X_1)=\mathbb C^6$.

For $i=1$ we have $X_1\setminus X_2 = \mathbb C$, which only has $H^0=\mathbb C$. So we have that $X_2$ has one dimension less in $H^2(X_2)$, nothing else changes: $H^2(X_1)=\mathbb C^5$.

Finally, for $i=2$ we have $X_2\setminus X_3 = \mathbb C^*$, which has $H^0=\mathbb C$ and $H^1=\mathbb C$, contributing to $H^2(X_2,X_3)$ and $H^3(X_2, X_3)$ correspondingly. Thus two things happen. First, only $4$ dimensions from $H^2(X_2)$ out of $5$ contribute to $H^2(X_3)$. On the other hand, one extra dimension comes from $H^3(X_3,X_2)$. The net total is $H^2(X_3)=\mathbb C^5$, as in $X_2$, but the nature of the $5$ dimensions is different, and correspondingly the weights are different. The $4$ dimensions coming from $H^2(X_2)$ have weight $2$, and this is reflected by the fact that they are represented by algebraic cycles. The remaining class has weight $4$ as it comes from $H^3(X_3,X_2)$. The weight of $H^1(\mathbb C^*)$ is $2$, but it gets increased by $2$ when we pass to $H^3(X_3,X_2)$.

These findings can be summarized in the table on Figure [2](#fig:cohomology){reference-type="ref" reference="fig:cohomology"}.

<figure id="fig:cohomology">
<table>
<thead>
<tr class="header">
<th style="text-align: center;"><span class="math inline"><em>H</em><sup>*</sup></span></th>
<th style="text-align: center;"><span class="math inline"><em>W</em><sub><em>i</em></sub><em>H</em><sup><em>i</em></sup></span></th>
<th style="text-align: center;"><span class="math inline"><em>W</em><sub><em>i</em> + 2</sub><em>H</em><sup><em>i</em></sup>/<em>W</em><sub><em>i</em></sub><em>H</em><sup><em>i</em></sup></span></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><em>H</em><sup>2</sup></span></td>
<td style="text-align: center;"><span class="math inline">ℂ<sup>4</sup> = ⟨<em>c</em><sub>1</sub>(<em>L</em><sub><em>i</em></sub>) | <em>i</em> = 1, 2, 3, 4⟩</span></td>
<td style="text-align: center;"><span class="math inline">ℂ = ⟨<em>ω</em> = symplectic form⟩</span></td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><em>H</em><sup>0</sup></span></td>
<td style="text-align: center;"><span class="math inline">ℂ = ⟨1⟩</span></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>
<figcaption><span id="fig:cohomology" label="fig:cohomology"></span>Cohomology of the Markov cubic</figcaption>
</figure>

The $4$ algebraic classes in $H^2(X)$ can be represented by characteristic classes of line bundles. The extra class can be represented by an explicit holomorphic symplectic form as explained below. Using the natural coordinates on $\mathbb C^*\times \mathbb C^*$, the form is written as $$\omega = \frac{dx}x \wedge \frac{dy} y,$$ and one can verify that the form extends to the whole of $X$.

## Mixed Hodge Polynomial {#ssec:mixed hodge polynomial}

From Figure [2](#fig:cohomology){reference-type="ref" reference="fig:cohomology"} we obtain that the Poincaré polynomial of $X$ is $1 + 5 q^2$ and the mixed Hodge polynomial is $P(q,t) = 1 + 4 q^2 t^2 + q^2 t^4$. We prefer to consider a slightly different version of the mixed Hodge polynomial, without losing any information. Let

$$\mathrm{MH}(X; q,t) := q^{\frac12 \dim_\mathbb CX} P(X;q^{-\frac12} t^{-\frac12}, t^{\frac12}).$$ For instance, in our running example we obtain $$\mathrm{MH}(X; q,t) = q + t + 4.$$

We should also compare our calculations with the number of points on our variety over $\mathbb F_q$. Assuming all the lines are defined over the base field, we see that the first computation produces $$(q-1)^2 + 6 q  = q^2 + 4 q + 1.$$ The second computation produces $$q^2 + 7q + 1 - (q+1) - q - (q-1) = q^2 + 4 q + 1.$$ In each case, one can track how the different powers of $q$ contribute to the cohomology so that $q^2$ corresponds to $H^0$ and $4q + 1$ corresponds to $H^2$.

In any case, for a general algebraic variety $X$, if the number of points is a polynomial of $q$, we have $$\label{eq:Fq points and mixed Hodge}
        |X(\mathbb{F}_q)| = q^{\dim_\mathbb CX} P(X;-1,q^{-\frac12}) = q^{\frac12 \dim_\mathbb CX} \mathrm{MH}(X;q,q^{-1}),$$ assuming $\mathrm{MH}$ is indeed a polynomial in $q$, $t$, which means that all the weights are even and the cohomology is concentrated in even degrees.
