---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-008-32-finite-quantum-spaces
section_title: "Finite quantum spaces"
section_number: 3.2
pages: 12-15
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.984
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
The notion of finite-dimensional Euclidean (or formally real) Jordan algebra was introduced and analyzed in [@jor-vn-wig:1934] under the name $r$-number algebra in order to formalize the properties of the observables of finite quantum systems. A minimal set of requirement for the observables of a finite quantum system is that it is a finite-dimensional real vector space $J$ such that one can consistently define powers of any element and that if a sum of squares of elements vanishes it implies that each of these elements vanishes. Given the square $x\mapsto x^2$, one defines a symmetric bilinear product on $J$ by setting $x\cdot y=1/2((x+y)^2-x^2-y^2)$ for $x,y\in J$.

So let $J$ be a finite-dimensional real vector space endowed with a symmetric bilinear product $$(x,y) \mapsto x.y = y.x
\label{prodcom}$$ for $x,y\in J$ and assume that the following condition is satisfied $$\sum_{i\in I} (x_i)^2=0 \Rightarrow x_i=0,\>\> \forall i\in I
\label{formre}$$ for any finite family $(x_i)_{\in I}$ in $J$, where $(x)^2=x.x$ for $x\in J$. The above condition for the product is refered to as *formal reality condition*. One has the following result [@jor-vn-wig:1934].

::: theorem
[]{#POJO label="POJO"} Let $J$ be as above and define $x^n\in J$ for $x\in J$ and $n\in \mathbb N^+$ by induction on $n$ as $x^1=x$ and $x^{n+1}=x.x^n$.\
Then the following conditions $\mathrm{(i)}$ and $\mathrm{(ii)}$ are equivalent :\
$\mathrm{(i)}\>\>\>  x^r.x^s=x^{r+s},\>\>  \text{for any}\>\> x\in J$ and $r,s\in \mathbb N^+$\
$\mathrm{(ii)}\>\>\> (x^2.y).x=x^2.(y.x),\>\> \text{for any}\>\>  x,y\in J$
:::

A finite-dimensional real commutative algebra satisfying ([\[formre\]](#formre){reference-type="ref" reference="formre"}) and the equivalent conditions (i) and (ii) of the theorem is referred to as a finite-dimensional *Euclidean* (or *formally real*) *Jordan algebra*, [@ber:2000], [@mcc:2004], [@ior:2009].\
Condition (i) of Theorem [\[POJO\]](#POJO){reference-type="ref" reference="POJO"} is referred to as *power associativity* while Condition (ii) is referred to as the *Jordan identity*. It is well known and easy to show that the Jordan identity implies the power associativity but it is a very nontrivial result that in the above context the power associativity combined with the formal reality condition imply the Jordan identity [@jor-vn-wig:1934]. One can find in [@alb:1950] other natural conditions on commutative power-associative algebras leading to the Jordan identity.\
It is worth noticing that Condition (3.2) and Condition (i) of Theorem 1 (i.e. power associativity) are exactly the conditions needed to have spectral resolutions of the elements of $J$. Indeed a finite-dimensional Euclidean Jordan algebra $J$ has a unit $\mbox{\rm 1\hspace {-.6em} l}\in J$ such that $\mbox{\rm 1\hspace {-.6em} l}. x=x$ for any $x\in J$ and any $x\in J$ has a *finite spectral resolution* $$x=\sum_{r\in I_x}\lambda_r e_r
\label{sprx}$$ where $I_x$ is a finite set, $\lambda_r\in \mathbb R$ and $e^2_r=e_r\in J$ for any $r\in I_x$, $e_r . e_s=0$ for $r,s\in I_x$ with $r\not=s$ and $$\mbox{\rm 1\hspace {-.6em} l}=\sum_{r\in I_x}e_r
\label{spr1x}$$ i.e. $(e_r)$ is a finite family of orthogonal idempotents in $J$ the sum of which is the unit $\mbox{\rm 1\hspace {-.6em} l}\in J$. Furthermore the number of elements of $I_x$, $\text{card}(I_x)$, is bounded by a finite number which only depends on $J$ that is one has $\sup_{x\in J}(\text{card}(I_x))<\infty$.\
This means that one can set $$x^0=\mbox{\rm 1\hspace {-.6em} l}
\label{x01}$$ and that $$P\mapsto P(x)=\sum_r P(\lambda_r)e_r
\label{fcalc}$$ defines a homomorphism of unital algebras from the algebra $\mathbb R[X]$ of real polynomials into $J$ for any $x\in J$.\
These finite-dimensional Euclidean Jordan algebras were classified in [@jor-vn-wig:1934] where the following theorem is proved.

::: theorem
[]{#ClassF label="ClassF"} Any finite-dimensional Euclidean Jordan algebra is a direct sum of a finite number of simple ideals. A finite-dimensional simple Euclidean Jordan algebra is isomorphic to one of $$\begin{array}{l}
\mathbb R\ \mathrm{and}\ \ JSpin_{n+2} =\mathbb R\mbox{\rm 1\hspace {-.6em} l}\oplus \mathbb R^{n+2},\\
\\
J^1_{n+3} = {\cal H}_{n+3}(\mathbb R),
J^2_{n+3} = {\cal H}_{n+3}(\mathbb C),\\
\\
J^4_{n+3} = {\cal H}_{n+3}(\mathbb H),\ \mathrm{with}\ n\in \mathbb N\\
\\
\mathrm{and}\ J^8_3 = {\cal H}_3(\mathbb O).
\end{array}$$
:::

In the above statement $JSpin_{n+1}=\mathbb R\mbox{\rm 1\hspace {-.6em} l}\oplus \mathbb R^{n+1}$ is endowed with the product $$(r\mbox{\rm 1\hspace {-.6em} l}\oplus v). (r'\mbox{\rm 1\hspace {-.6em} l}\oplus v')=(rr'+\langle v,v'\rangle)\mbox{\rm 1\hspace {-.6em} l}\oplus (rv'+r'v)$$ where $\langle,\rangle$ is the scalar product of the Euclidean space $\mathbb R^{n+1}$ and, for any involutive algebra ${\cal A}$, ${\cal H}_n({\cal A})$ denotes the space of hermitian $n\times n$-matrices with entries in ${\cal A}$ endowed with the product $$A. B = \frac{1}{2} (AB+BA)
\label{anticom}$$ where $(A,B)\mapsto AB$ is the product in $M_n({\cal A})$.\
The absence of $JSpin_{1}$ in the above list comes from the fact that $JSpin_{1}$ is not simple but is isomorphic to the commutative associative algebra $\mathbb R\oplus \mathbb R$ of the real functions on a two-points set. Furthermore, notice that one has the following coincidence $$\begin{array}{l}
{\cal H}_1(\mathbb R)={\cal H}_1(\mathbb C)={\cal H}_1(\mathbb H)={\cal H}_1(\mathbb O)=\mathbb R,\\
{\cal H}_2(\mathbb R)=JSpin_2,\ {\cal H}_2(\mathbb C)=JSpin_3, {\cal H}_2(\mathbb H)=JSpin_5,\\
{\cal H}_2(\mathbb O)=JSpin_9
\end{array}$$ and that the ${\cal H}_n(\mathbb O)$ are not Jordan algebras for $n\geq 4$.\
In each finite-dimensional simple Euclidean Jordan algebra $J$, its unit $\mbox{\rm 1\hspace {-.6em} l}$ admits a decomposition $$\mbox{\rm 1\hspace {-.6em} l}= \sum^{c(J)}_{i=1} e_i$$ with $e_i. e_j=0$ for $i\not= j$ (orthogonality) where the $e_i$ are primitive idempotents. The number $c(J)$ does only depend on $J$ and is refered to as the *capacity* (or the *degree*) of $J$. One has $c(\mathbb R)=1$, $c(JSpin_{n+2})=2$, $c(J^1_3)=c(J^2_3)=c(J^4_3)=c(J^8_3)=3$ and $c(J^1_n)=c(J^2_n)=c(J^4_n)=n$ for $n\geq 4$.\
Note the obvious fact that a finite-dimensional Euclidean Jordan algebra $J$ which is associative is the algebra of real functions on a finite space $K$ which can be identified to the set of *characters* of $J$, that is the set of homomorphisms $$\chi : J\rightarrow \mathbb R$$ of unital algebras. More generally, it will be convenient in the following to consider that a finite-dimensional Euclidean Jordan algebra $J$ is the algebra of "*real function*\" on some associated "*finite quantum space*\" (a dual object). This is justified by the above spectral properties as well as by the fact that $J$ is the set of observable of a finite quantum system (see below). Indeed the pure states on $J$ are the primitive idempotents in $J$ and the transition probabilities between two states are the appropriate traces of the corresponding product of idempotents.\
Recall finally that a *Jordan algebra* over a commutative field $\mathbb K$ is a $\mathbb K$-vector space endowed with a symmetric bilinear product $(x,y)\mapsto x. y$ satisfying Property (ii) of Theorem [\[POJO\]](#POJO){reference-type="ref" reference="POJO"}. For infinite-dimensional real Jordan algebras, there are various generalizations of the formal reality condition ([\[formre\]](#formre){reference-type="ref" reference="formre"}). In this frame there are (bounded) generalizations of Theorem [\[POJO\]](#POJO){reference-type="ref" reference="POJO"}, see [@ioc-lou:1985] for the $JB$-algebra version and [@vn:1936] for a weak version.
