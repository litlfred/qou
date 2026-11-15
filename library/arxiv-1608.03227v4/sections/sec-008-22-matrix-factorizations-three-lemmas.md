---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-008-22-matrix-factorizations-three-lemmas
section_title: "Matrix factorizations: three lemmas"
section_number: 2.2
pages: 8-11
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.958
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In this subsection we fix notations for matrix factorizations and remind some basic facts about them. In particular we prove three lemmas that we will use in the main body of the paper. These lemmas essentially contain all facts about matrix factorizations that are used here. For more thorough review of the theory of matrix factorization the reader could consult the beautiful original paper [@E] or later surveys in [@D].

Given an affine variety $\mathcal{Z}$ and a function $F$ on it we define [@E] the homotopy category $\SymbolPrint{\MFs}(\mathcal{Z},F)$ of matrix factorizations whose objects are complexes of $\CC[\calZ]$-modules $M=M_{odd}\oplus M_{even}$ equipped with the differential $$D\in \yHom_{\CC[\calZ]}(M_{odd},M_{even})\oplus  \yHom_{\CC[\calZ]}(M_{even},M_{odd})$$ such that $D^2=F$.

Thus $\MFs(\mathcal{Z},F)$ is a triangulated category as explained in subsection 3.1 of [@Or].

If $\calZ$ is a variety with $G$-action and $F$ is a $G$-invariant function then we define the category of strongly equivariant matrix factorizations $\SymbolPrint{\MFs^{str}_G}(\mathcal{Z},F)$ as the category of matrix factorizations with extra condition that $D$ is a $G$-equivariant matrix. Unfortunately, this definition is too restrictive and we use a slightly more sophisticated definition for the category of equivariant matrix factorization. We postpone the details of our definition till the next section where we define matrix factorizations that are equivariant up to homotopy. However, the naive equivariant matrix factorization as above are objects in our category.

Let us discuss some specific types of matrix factorizations that will be used in our paper. Suppose $C_\bullet=[C_0\to C_1\to\dots \to C_n]$ is the complex of $\CC[\calZ]$-modules. Then we construct a matrix factorization $\SymbolPrint{[C_\bullet]_{per}}\in \MFs(\calZ,0)$ by setting $M=C_{odd}\oplus C_{even}$, $C_{even}:=\oplus_{i\in 2\mathbb{Z} } C_i, C_{odd}= \oplus_{i\in 1+2\mathbb{Z} } C_i$ and the differential is induced from the complex $C_\bullet$.

Another type of matrix factorization appearing in our work is obtained by \"doubling\" the differential $d^+$ of an ordinary complex $(C_\bullet,d^+)$. Indeed, let us denote by $\MFs^\ell(\calZ,F)$ the set of the following complexes: $$C_\bullet=\oplus_{i=0}^\ell C_i,\quad
d^+_i: C_i\to C_{i-1},\quad
d^-_i:C_i\to C_{>i},\quad (\sum_i d_i^-+d_i^+)^2=F\cdot \mathrm{Id}.$$

The complex $C_\bullet$ with only the positive differentials $d^+_i$ is called the positive part of the complex. There is a folding map $\SymbolPrint{\MFs^{\ell}}(\calZ,F)\to \MFs(\calZ,F)$ that associates to $(C_\bullet,d^\pm_\bullet)$ a two-periodic complex $[C_\bullet,d^\pm_\bullet]_{per}$. The matrix factorizations of the above type occur very naturally in a geometric setting as explained in the lemma below. The notations for the morphisms are as follows: $\Hom ^{k}(C_\bullet,C_\bullet)=\oplus_{m} \yHom(C_m,C_{m-k})$ is notations for the maps of $\CC[\calZ]$-modules and $\Hom _{d_+}^{k}(C_\bullet,C_\bullet)$ is the subspace of maps from $\yHom^k(C_\bullet,C_\bullet)$ that commute with the differential $d^+$.

::: lemma
[]{#lem: ext MF label="lem: ext MF"} Let $(C_\bullet,d_\bullet^+)$ be the complex $$C_0\xleftarrow{d_1^+}C_1\xleftarrow{d_2^+}\dots\xleftarrow{d_\ell^+} C_\ell$$ of $\CC[\calZ]$ modules and $F\in \CC[\calZ]$ such that

1.  Elements of $\Hom _{d_+}^{<0}(C_\bullet,C_\bullet)$ are homotopic to $0$

2.  The element $F\in    \Hom _{d_+}^{0}(C_\bullet,C_\bullet)$ is homotopic to $0$.

Then the complex $(C_\bullet,d_\bullet^+)$ can be extended to $(C_\bullet,d^\pm_\bullet)\in \MFs^{\ell}(\calZ,F)$.
:::

::: proof
*Proof.* By assumption of the lemma, the endomorphism $F\cdot \mathrm{Id}$ of $(C_\bullet,d_\bullet^+)$ is homotopic to $0$. This means that there exist morphisms of $\CC[\calZ]$ modules $h^{(-1)}_i: C_i\to C_{i+1}$ such that $F=h^{(-1)}_i\circ d_{i+1}^++d_i^+\circ h^{(-1)}_{i-1}$. Then a new differential $D^{(-1)}:=d^++h^{(-1)}$ satisfies the relation $$\left(D^{(-1)}\right)^2-F =(h^{(-1)})^2\in \yHom^{\leq-2}(C_\bullet,C_\bullet).$$

Thus $D^{(-1)}$ provides a base

of induction for the proof of existence $h^{(-2i-1)}\in \yHom^{-2i-1}(C_\bullet,C_\bullet)$, $i\ge 0$ such that

1.  $[h^{(-1)},d^+]_+=F$

2.  $[h^{(-2i-1)},d^+]_+=\sum_{j=0}^{i-1} h^{(-2j-1)} h^{(-2i+2j+1)}$, $i>0$

were we used the notation $[a,b]_+=ab+ba$.

Indeed, suppose we constructed $h^{(-2i-1)}$ for all $i<j$. Define $D^{(-2j+1)}=d^++\sum_{k=0}^{j-1} h^{(-1-2k)}$, then the inductive assumption implies: $$\label{eq: D2}
\left( D^{(-2j+1)}\right)^2-F-R^{(-2j)}\in \yHom^{<-2j}(C_\bullet,C_\bullet),\quad R^{(-2j)}=\sum_{k=0}^{j-1} h^{(-2k-1)} h^{(-2j+1+2k)}$$ On the other hand, a direct computation using the inductive assumptions and the fact that $F$ commutes with all $h^{(2i-1)}$ and $d^+$ implies $$\label{eq: com d+}
 [d^+,R^{(-2j)}]=0.$$ In more details, let us introduce notation $R^{(<-2j)}:=(D^{(-2j-1)})^2-F-R^{(-2j)}$ then $$\begin{gathered}
0=[D^{(-2j-1)}, (D^{(2j-1)})^2]=[d^+ +\sum_i h^{(-2i-1)}, F+R^{(-2j)}+R^{(<-2j)}]\\=[d^+,R^{(-2j)}]+[d_++\sum_i h^{(-2i-1)},R^{(<-2j)}]+[\sum_i h^{(-2j-1)},R^{(-2j)}+R^{(-2j-1)}].
\end{gathered}$$ The first term in the last sum is from $\Hom ^{-2j+1}(C_\bullet,C_\bullet)$, on the other hand the last two are from $\Hom ^{<-2j+1}(C_\bullet,C_\bullet)$ thus ([\[eq: com d+\]](#eq: com d+){reference-type="ref" reference="eq: com d+"}) follows.

Thus $R^{(-2j)}$ is the morphism of the complex $(C_\bullet,d^+)$ of degree $-2j$, that is, an element of $\Hom _{d_+}^{-2j}(C_\bullet,C_\bullet)$. The assumption of our lemma implies that such morphism is homotopic to zero and the homotopy morphism $h^{(-2j-1)}\in  \Hom ^{-2j-1}(C_\bullet,C_\bullet)$ provides the induction step since $[h^{(-2j-1)},d^+]_+=R^{(-2j)}$.

Thus by setting $d_i^-=\sum_i h^{(-2i-1)}$ we obtain the desired extension because of ([\[eq: D2\]](#eq: D2){reference-type="ref" reference="eq: D2"}). ◻
:::

The extension described in Lemma [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} is unique up to a natural equivalence relation. First, let us fix notations: the space of morphisms $\Hom _{d^{\pm}}(A,B)$, $A,B\in \MFs^{\ell}(\calZ,F)$ consists of $\CC[\calZ]$-module homomorphism that (super-)commute with the differentials $d_\bullet^\pm$. This space is $\mathbb{Z}$-graded with $\Hom _{d^{\pm}}^i(A,B)$ consisting of morphisms $h_k: A_k\to A_{k+i}$.

::: lemma
[]{#lem: ext uniq label="lem: ext uniq"} Let $A=(C_\bullet,d^\pm_\bullet), B=(C_\bullet,\tilde{d}^\pm_\bullet)\in \MFs^{\ell}(\calZ,F)$ such that

1.  $(\tilde{C},\tilde{d}^+_\bullet)=(C_\bullet,d^+_\bullet)$

2.  Elements of $\Hom _{d_+}^{<0}(C_\bullet,C_\bullet)$ are homotopic to $0$

3.  The element $F\in    \Hom _{d_+}^{0}(C_\bullet,C_\bullet)$ is homotopic to $0$.

Then there is $\Psi=\sum_{i\le 0}\Psi_i$, $\Psi_i\in \Hom^{i}(A,B)$ such that $\Psi_0=\mathrm{Id}$ and $$\Psi\circ (d^++d^-)\circ \Psi^{-1}=(\tilde{d}^++\tilde{d}^-).$$
:::

::: proof
*Proof.* For brevity let us denote by $C^+$ the complex $(C_\bullet,d^+_\bullet)$, respectively we use notation $\Hom _{d_+}(C^+,C^+)$ for the morphisms that respect the differential $d^+$ and $\Hom(C,C)$ for the morphisms of complexes simply as modules. In particular in these notations we have $$D=d^++d^-,\quad  \tilde{D}=d^++\tilde{d}^-\in \Hom^{1}(C,C)\oplus \Hom^{\le -1}(C,C).$$

We claim that there is sequence of morphisms $\Psi^{(k)}\in \Hom^{\le 0}(C,C)$, $k=0,1,2,\dots$ such that

1.  $\Psi^{(k)}_0=\mathrm{Id}$,

2.  $D^{(k)}-\tilde{D}\in \Hom^{-k-1}(C,C)$,

where $D^{(k)}=\Psi^{(k)}\circ D\circ (\Psi^{(k)})^{-1}$.

Indeed, for $k=0$ we can set $\Psi^{(0)}=\mathrm{Id}$. For the step of induction we assume the existence of $\Psi^{(k-1)}$, then the leading term $\Delta=(D^{(k-1)}-\tilde{D})_{-k}\in  \Hom ^{-k}(C,C)$ is actually an element of $\Hom _{d_+}^{-k}(C^+,C^+)$ as could be seen from degree $-k+1$ part of the equation $$(D^{(k-1)})^2-D^2=0.$$

On the other hand the second assumption of the Lemma implies that all elements of $\Hom _{d_+}^{-k}(C^+,C^+)$ are homotopic to $0$ and hence there is $h\in Hom^{-k-1}(C,C)$ such that $[h,d^+]=\Delta$. Hence the element $\Psi^{(k)}:=(1+h)\circ \Psi^{(k-1)}$ satisfies the condition of our induction statement.

Finally, since the complex $C$ is bounded see that the morphism $\Psi^{(\ell)}$ has the desired properties and our proof is complete. ◻
:::

The last lemma is very elementary but it is responsible for appearance of the Hilbert scheme of points on the plane in our construction of the knot homology.

::: lemma
[]{#lem: crit label="lem: crit"} Let $Z$ be smooth and affine. The elements of the ideal $\calI_{crit}$ generated by the partial derivatives of the potential $F$ act by zero homotopies on the elements of $\MFs(\calZ,F)$
:::

::: proof
*Proof.* Let $z$ be a local coordinate on $\calZ$ and $D$ is the differential from some matrix factorization with the potential $F$. Then we have $$\frac{\partial F}{\partial z}=\frac{\partial D}{\partial z}\circ D+ D\circ \frac{\partial D}{\partial z}.$$ Hence $\frac{\partial D}{\partial z}$ is the map that provides a homotopy of $\frac{\partial F}{\partial z}$ to $0$. ◻
:::
