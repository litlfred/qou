---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-006-17-homological-mirror-symmetry
section_title: "Homological Mirror Symmetry"
section_number: 1.7
pages: 6-7
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.987
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
[]{#Sec:HMS label="Sec:HMS"}

The proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} involves establishing Fukaya category analogues of three well-known results concerning derived categories of sheaves.

-   (Bondal-Orlov) The derived category of sheaves on the intersection of two even-dimensional quadrics has a semi-orthogonal decomposition in which one factor is the derived category of sheaves on an underlying hyperelliptic curve [@BondalOrlov].

-   (Kapranov) The derived category of sheaves on an even-dimensional quadric has a semi-orthogonal decomposition in which one factor is the derived category of sheaves on a pair of points [@Kapranov].

-   (Bondal-Orlov) If $X \rightarrow Y$ is the blow-up along a smooth centre $B\subset Y$ of codimension at least 2, the derived category of sheaves on $B$ embeds in the derived category of sheaves on $X$ [@BondalOrlov].

Obviously, Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} is exactly the symplectic analogue of the first of these results. Our proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} relates both categories appearing in its statement with the Fukaya category of the *relative quadric* $Z$, given by blowing up ${\mathbb P}^{2g+1}$ along $Q_0\cap Q_1$. We construct equivalences with quasi-isomorphic images $$D^{\pi}\EuScript{F}(\Sigma_g) \ \hookrightarrow \ D^{\pi}\EuScript{F}(Z) \ \hookleftarrow  \ D^{\pi}\EuScript{F}(Q_0\cap Q_1;0).$$ Although it occupies only a small part of the final proof, the geometric heart of $\hookrightarrow$ and arguably of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} is Section [\[Section:Quadric\]](#Section:Quadric){reference-type="ref" reference="Section:Quadric"}, which gives a derived equivalence between the nilpotent summand of the Fukaya category of a quadric $Q \subset {\mathbb P}^{2g+1}$ and the Fukaya category of a pair of points $S^0$. This is precisely the symplectic analogue of Kapranov's theorem. From that perspective, a hyperelliptic curve and the total space of the associated pencil of quadrics behave, categorically, like fibrations with the same fibre and monodromy. To pass between $D^{\pi}\EuScript{F}(Z)$ and $D^{\pi} \EuScript{F}(Q_0 \cap Q_1)$ involves relating the derived Fukaya category of a base locus and of a blow-up, akin to the second mentioned theorem of Bondal-Orlov (in this case, however, the symplectic story is carried out in more restricted circumstances, for blow-ups of codimension two complete intersections satisfying a raft of convenient hypotheses). In light of these analogies, one is led to compare the chains of spaces $$\label{Eqn:Kuznetsov}
\begin{array}{ccccccc} 
\emptyset & \subset & 2 \ \textrm{points} & \subset & \Sigma_g & \subset & X \\
\updownarrow &  &\updownarrow & &\updownarrow & & \updownarrow \\ 
{\mathbb P}^{2g+1} & \supset & Q & \supset & Q_0\cap Q_1 & \supset & X^{\vee} 
\end{array}$$ where the top line corresponds to double branched covers of projective space of dimensions $d=-1,0,1,2$ over divisors of degree $2g+2$, and the lower line the base locus of a $d$-dimensional family of quadrics in ${\mathbb P}^{2g+1}$. There are equivalences between the Fukaya category of a space in the top line, and the nilpotent summand of the Fukaya category of the space below it, in each of the first 3 columns, mirror to a small part of Kuznetsov's "homological projective duality\" [@Kuznetsov]. The situation in the final column is less clear. For instance, when $g=2$, both $X$ and $X^{\vee}$ are $K3$ surfaces, but in general they don't have equivalent derived categories of coherent sheaves unless one introduces a twist by a class in the Brauer group. It would be interesting to know whether this has any symplectic analogue. The hypersurface of degenerate quadrics is singular in codimension 3, so technical difficulties arise in pushing this any further.

Given the proposed Landau-Ginzburg mirror $w:Y_{Q_0 \cap Q_1} \rightarrow {\mathbb C}$ of $Q_0 \cap Q_1$ [@Katzarkov; @Przyj], and the proofs by Seidel and Efimov of mirror symmetry for curves of genus $\geq 2$, [@Seidel:HMSgenus2; @Efimov], Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} essentially proves one direction of Homological Mirror Symmetry for the Fano variety which is the complete intersection of two quadrics: $$D^{\pi}\EuScript{F}(Q_0 \cap Q_1;0) \ \simeq \ D^b_{sing}(Y_{Q_0 \cap Q_1},w|_{\text{open subset}})$$ (restricting $w$ throws out certain "massive modes\"). In particular, this gives the first proof of HMS for a moduli space of bundles on a curve of higher genus.

::: Remark
Homological Mirror Symmetry typically relates symplectic and algebraic geometry. The relation of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} to HMS is roughly as follows. The mirror of a Fano variety $X$ is a Landau-Ginzburg model $w: Y \rightarrow {\mathbb C}$; blowing up the Fano $X' \rightarrow X$ is expected to introduce new singular fibres $Y \subset Y' \stackrel{w'}{\rightarrow} {\mathbb C}$ into the LG-model. Blow-ups induce semi-orthogonal decompositions of the derived category $D^b(X') = \langle D^b(X), \mathcal{C}\rangle$, hence corresponding semi-orthogonal decompositions relating the Fukaya-Seidel categories of the mirrors. On the other hand, the new singular fibre of $(Y',w')$ leads to a new summand to its derived category of singularities, which should correspond to a new summand in the Fukaya category of $X'$ (and perhaps some bulk deformation of the summands coming from $X$). For more on the mirror symmetric background and motivation for Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"}, see [@KKOY].
:::
