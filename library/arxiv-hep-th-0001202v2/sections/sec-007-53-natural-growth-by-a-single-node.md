---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-007-53-natural-growth-by-a-single-node
section_title: "Natural growth by a single node"
section_number: 5.3
pages: 13-14
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 1.0
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
There is a clear candidate for the second operator: the natural growth operator $N$, which appends a single node in all possible ways, and hence obeys a Leibniz rule.

The commutators of $N$ with $B_\pm$ are easily found, since we need only consider what is happening at the root. Defining the operator $L$ by $L(X):=l_1X$, we obtain $$\begin{aligned}
\left[N,\,B_+\right]&=&B_+\circ L\,,\label{np}\\
\left[B_-,\,N\right]&=&L\circ B_-\,,\label{nm}\\
\left[N,\,C\right]&=&[N,B_+]\circ B_--B_+\circ[B_-,N]=0\,.\label{nc}
\end{aligned}$$ The natural growth operator is a wonderful thing: it commutes with $B_+\circ B_-$, the operator that makes the Hopf algebra so structured; hence it preserves the kernel of $B_-$; like $B_-$, it acts as a derivative; like $B_+$, it adds a node and increases the degree of primitivity; finally, it identifies the unique [@CK] noncocommutative Hopf subalgebra ${\cal H}_{\rm CM}$, with linear basis $\delta_{n}:=N^{n-1}(l_1)$.

Constructing $N(p_4)$ and $N(p_4^\prime)$, we verified that they are in the kernel of $U_2$ and the range of $U_1$. It might thus appear that some linear combination of them with $B_+(p_4)$, $B_+(p_4^\prime)$ and the product terms $\{p_1p_4,p_1p_4^\prime,
p_2p_3\}$ solves the problem of constructing $W(p_2,p_3)$. Remarkably, this turns out not to be the case. Rather, we find that application of $$S_1:=N+(B_+-L)\circ Y
\label{S1}$$ to a 1-primitive gives a 1-primitive of higher weight. Here $Y$ is the grading operator, which multiplies each tree by its weight and operates on products by a Leibniz rule. Thus $N(p_4)$ and $N(p_4^\prime)$ are linear combinations of $\{B_+(p_4),B_+(p_4^\prime),p_1p_4,p_1p_4^\prime\}$ and 1-primitives. Instead of constructing the missing weight-5 nonproduct 2-primitive, we discovered how to generate all the 1-primitives with weight $n\le5$. We have $L(e)=p_1=l_1$, at $n=1$; $S_1(p_1)=2p_2$, at $n=2$; $S_1(p_2)=3p_3$, at $n=3$. At $n=4$, we obtain $S_1(p_3)=4p_4-p_4^\prime$, to which we adjoin $p_4$, from the ladder construction ([\[pl\]](#pl){reference-type="ref" reference="pl"}) of sect. 3. Then we obtain the 1-primitives at $n=5$ as $p_5$, $S_1(p_4)$ and $S_1^2(p_3)$.

We then found a generalization of ([\[S1\]](#S1){reference-type="ref" reference="S1"}), which solves the problem of constructing $W(p_2,p_3)$. Operating on a weight-$n$ 1-primitive with $$S_k:=\left(S_1-\frac{k-1}{2}(B_+-L)\right)\circ N^{k-1}
\label{Sk}$$ we create a $k$-primitive of weight $n+k$. In particular, $$W(p_2,p_3)=\frac{8S_2(p_3)-7N\circ S_1(p_3)}{12}-p_2p_3
\label{W23}$$ completes the construction of weight-5 2-primitives. More generally, we found that $$\begin{aligned}
W(p_2,X_n)&=&\frac{2O_2(X_n)}{n(n+1)}-p_2X_n\label{W2n}\\
O_2&:=&S_2\circ(Y+{\rm id})-N\circ S_1\circ(Y+\dfrac12{\rm id})\label{O2}
\end{aligned}$$ gives $U_1\circ W(p_2,X_n)=p_2\otimes X_n-X_n\otimes p_2$, where $X_n$ is a 1-primitive with weight $n$. We remark that ([\[W2n\]](#W2n){reference-type="ref" reference="W2n"}) lies in the kernel of $C$, for all $n>1$.

However, it is not yet clear how to generalize this construction to obtain, for example, $W(p_3,p_4)$ and $W(p_3,p_4^\prime)$ at weight $n=7$. They key to this issue is an extension[^1] of the concept of natural growth.

[^1]: Our extension of natural growth allows a suitable extension of the Lie algebra dual to ${\cal H}_R$, as was observed by Alain Connes. This will be presented in a sequel to [@DR2].
