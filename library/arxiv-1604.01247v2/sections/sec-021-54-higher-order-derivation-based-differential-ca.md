---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-021-54-higher-order-derivation-based-differential-ca
section_title: "Higher order derivation-based differential calculi"
section_number: 5.4
pages: 27-28
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.97
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Let $J$ be a unital Jordan algebra with center $Z(J)$ and let $\Omega^n_{{\mbox{\tiny Der}}}(J)$ be the $J$-module of all $n$-$Z(J)$-linear antisymmetric mappings of ${\mbox{Der}}(J)$ into $J$, that is $\omega\in \Omega^n_{{\mbox{\tiny Der}}}(J)$ is a $Z(J)$-linear mapping $$\omega:\wedge^n_{Z(J)} {\mbox{Der}}(J)\rightarrow J$$ of the n-th exterior power over $Z(J)$ of the $Z(J)$-module ${\mbox{Der}}(J)$ into $J$ as a $Z(J)$-module. Then $\Omega_{{\mbox{\tiny Der}}}(J)=\oplus_{n\geq 0} \ \Omega^n_{{\mbox{\tiny Der}}}(J)$ is canonically a differential graded Jordan algebra with differential given by the Chevalley-Eilenberg formula $$\begin{array}{ll}
d\omega(X_0,\cdots,X_n) & =  \sum_{0\leq k\leq n} (-1)^k X_k\  \omega(X_0,\stackrel{k\atop \vee}{\cdots},X_n) \\
&+ \sum_{0\leq r<s\leq n}(-1)^{r+s}\ \omega([X_r,X_s],X_0,\stackrel{r\atop \vee}{\cdots} \stackrel{s\atop \vee}{\cdots},X_n)
\end{array}
\label{C-E}$$ for $\omega\in \Omega^n_{{\mbox{\tiny Der}}}(J)$ and $X_p\in {\mbox{Der}}(J)$. Thus $\Omega_{{\mbox{\tiny Der}}}(J)$ is a differential calculus over $J$ which will be referred as the *derivation-based differential calculus* over $J$.\
If $J$ is a finite-dimensional simple Euclidean Jordan algebra, (i.e. one of the list of Theorem 2), one has

$$\Omega_{{\mbox{\tiny Der}}}(J)=J\otimes \wedge {\mbox{Der}}(J)^\ast
\label{omegaJ}$$ where $\wedge{\mbox{Der}}(J)^\ast$ is the exterior algebra of the dual of the finite-dimensional real Lie algebra ${\mbox{Der}}(J)$. In the case where $J$ is the exceptional Jordan algebra $J^8_3$, this differential calculus is characterized by the following universal property.

::: proposition
[]{#dex label="dex"} Any homomorphism $\varphi$ of unital Jordan algebra of $J^8_3$ into the Jordan subalgebra $\Omega^0$ of a unital differential graded Jordan algebra $\Omega=\oplus \Omega^n$ has a unique extension $\tilde\varphi:\Omega_{{\mbox{\tiny Der}}}(J^8_3)\rightarrow \Omega$ as a homomorphism of differential graded Jordan algebras.
:::

(sketch of). By using the fact that the $J^8_3$-modules are of the form $J^8_3\otimes {\cal E}$ for some vector spaces ${\cal E}$ and the definition of the $\mathbb N$-graded Jordan superalgebras, Formulae ([\[grcom\]](#grcom){reference-type="ref" reference="grcom"}) and ([\[grJ\]](#grJ){reference-type="ref" reference="grJ"}), it follows that any unital differential graded Jordan algebra $\Omega=\oplus \Omega^n$ which contains $J^8_3$ as unital Jordan subalgebra of $\Omega^0$ is as algebra of the form $$\Omega=J^8_3\otimes \Omega_{(0)}$$ where $\Omega_{(0)}=\oplus \Omega^n_{(0)}$ is an associative graded-commutative algebra (this generalizes a classical result in the non graded case). The proof follows then from Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"}, from $d^2=0$ with the graded Leibniz rule for $d$ and from the simplicity of $J^8_3$. $\square$\
A more detailed proof will appear in a forthcoming paper.\
. Notice that as Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"}, Proposition [\[dex\]](#dex){reference-type="ref" reference="dex"} is very specific to the exceptional Jordan algebra $J^8_3$.\
As a consequence all differential calculus over $J^8_3$ which are generated as differential graded Jordan algebra by $J^8_3$ are quotients of $\Omega_{\mbox{\tiny Der}}(J^8_3)$, in particular among these, one has all the differential graded Jordan algebras of the form

$$\Omega=J^8_3\otimes \wedge {\mathfrak g}^\ast
 \label{diffexc}$$ where ${\mathfrak g}$ is a Lie subalgebra of ${\mbox{Der}}(J^8_3)=\frak f_4$, the differential being the Chevalley-Eilenberg differential (${\mathfrak g}$ acting by derivations on $J^8_3$).
