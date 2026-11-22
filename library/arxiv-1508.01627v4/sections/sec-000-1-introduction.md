---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.868
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#sec:intro label="sec:intro"} The classical Murnaghan--Nakayama rule provides an efficient recursive method to compute the values of irreducible characters of symmetric groups. This method can be adapted to the finite general linear and unitary groups, where it then allows to compute values of unipotent characters not on arbitrary but just on regular semisimple elements, see [@LM15 Prop. 3.3]. This adaptation uses the fact that the unipotent characters of general linear groups coincide with Lusztig's so-called almost characters and then applies the Murnaghan--Nakayama rule for the symmetric group.

In the present paper, we derive a Murnaghan--Nakayama rule for the values of unipotent characters of the finite classical groups on regular semisimple elements, see Theorem [\[thm:MN\]](#thm:MN){reference-type="ref" reference="thm:MN"}. Our approach here is not via a corresponding formula for the underlying Weyl group (of type $B_n$ or $D_n$), since for classical groups Lusztig's Fourier transform is non-trivial and thus the relation between almost characters and unipotent characters becomes quite tricky. Instead we combine Asai's result expressing the decomposition of Lusztig induction in terms of hooks and cohooks of symbols and which already has a Murnaghan--Nakayama like form, with Lusztig's character formula.

As a first application we derive a vanishing result for irreducible characters of quasi-simple groups on $\ell$-singular elements:

::: thmA
[]{#thmA:zeroes label="thmA:zeroes"} Let $\ell>2$ be a prime and $G$ a finite quasi-simple group of $\ell$-rank at least 3. Then for any non-trivial character $\chi\in{\operatorname{Irr}}(G)$ there exists an $\ell$-singular element $g\in G$ with $\chi(g)=0$, unless either $G$ is of Lie type in characteristic $\ell$, or $\ell=5$ and one of:

1.  $G={\operatorname{L}}_5(q)$ with $5||(q-1)$ and $\chi$ is unipotent of degree $\chi(1)=q^2\Phi_5$;

2.  $G={\operatorname{U}}_5(q)$ with $5||(q+1)$ and $\chi$ is unipotent of degree $\chi(1)=q^2\Phi_{10}$;

3.  $G=Ly$ and $\chi(1)\in\{48174,11834746\}$; or

4.  $G=E_8(q)$ with $q$ odd, $d_\ell(q) = 4$ and $\chi$ one character in the Lusztig-series of type $D_8$.
:::

The second main ingredient in the proof, apart from our Murnaghan--Nakayama formula, is a result asserting the existence of $\ell$-singular regular semisimple elements in classical groups of Lie type (see Lemma [\[lem:regelts\]](#lem:regelts){reference-type="ref" reference="lem:regelts"}) which may be of independent interest.

We then apply this vanishing result in order to classify simple endotrivial modules over fields $k$ of positive characteristic $\ell$ for finite classical groups.

::: thmA
[]{#thmA:endoclass label="thmA:endoclass"} Let $G$ be a finite quasi-simple group of classical Lie type $B_n,C_n,D_n$ or ${}^2\!D_n$ with non-cyclic Sylow $\ell$-subgroup. Then there exists a non-trivial simple endotrivial $kG$-module $V$ if and only if $G={\operatorname{Sp}}_8(2)$, $k$ has characteristic $\ell=5$, and $\dim(V)=51$.
:::

Our approach relies on the fact, proven in [@LMS13 Thm. 1.3] that any endotrivial module is liftable to a characteristic 0 representation, which can then be studied by ordinary character theory. In particular, its character cannot vanish on any $\ell$-singular element, and this latter condition can be checked with the previous Murnaghan--Nakayama formula.

As a further application we give a (partial) answer to a question of Koshitani, Külshammer and Sambale [@KKS], which is then used in [@LM15] to settle this question completely:

::: thmA
[]{#thmA:PIMs label="thmA:PIMs"} Let $G$ be a finite simple group of classical Lie type $B_n,C_n,D_n$ or ${}^2\!D_n$. Let $\ell>2$ be a prime for which Sylow $\ell$-subgroups of $G$ are non-cyclic. Then the $\ell$-modular projective cover of the trivial character of $G$ has at least three ordinary constituents.

In particular the first Cartan invariant of $G$ satisfies $c_{11}\ge3$.
:::

Our paper is organised as follows. In Section [\[sec:maxtor\]](#sec:maxtor){reference-type="ref" reference="sec:maxtor"} we prove the existence of regular semisimple elements in suitable maximal tori of groups of classical type and determine possible overgroups of collections of maximal tori. Section [\[sec:MNrule\]](#sec:MNrule){reference-type="ref" reference="sec:MNrule"} contains the proof of the Murnaghan--Nakayama rule, see Theorem [\[thm:MN\]](#thm:MN){reference-type="ref" reference="thm:MN"}. We apply this in Section [\[sec:vanish\]](#sec:vanish){reference-type="ref" reference="sec:vanish"} to prove a vanishing result on $\ell$-singular elements, see Theorems [\[thm:non-unip\]](#thm:non-unip){reference-type="ref" reference="thm:non-unip"} and [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}. In Section [\[sec:endotriv\]](#sec:endotriv){reference-type="ref" reference="sec:endotriv"} we show Theorem [\[thmA:endoclass\]](#thmA:endoclass){reference-type="ref" reference="thmA:endoclass"} classifying simple endotrivial modules for classical groups. In Section [\[sec:rank3\]](#sec:rank3){reference-type="ref" reference="sec:rank3"} we collect the previous results to prove the vanishing result in Theorem [\[thmA:zeroes\]](#thmA:zeroes){reference-type="ref" reference="thmA:zeroes"}. Finally, in Section [\[thm:cartan\]](#thm:cartan){reference-type="ref" reference="thm:cartan"} we show the application to the proof of Theorem [\[thmA:PIMs\]](#thmA:PIMs){reference-type="ref" reference="thmA:PIMs"}.

**Acknowledgement:** We thank Andrew Mathas for useful explanations concerning the notation and results of [@JM00]. We also thank the anonymous referee for his helpful comments.
