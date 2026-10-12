---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-016-6-zeroes-of-characters-of-quasi-simple-groups
section_title: "Zeroes of characters of quasi-simple groups"
section_number: 6
pages: 17-18
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.971
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#sec:rank3 label="sec:rank3"}

Together with our previous work [@LM15; @LMS13] with C. Lassueur and E. Schulte our results allow us to guarantee the existence of zeroes of characters of quasi-simple groups on $\ell$-singular elements once the $\ell$-rank is at least 3, as claimed in Theorem [\[thmA:zeroes\]](#thmA:zeroes){reference-type="ref" reference="thmA:zeroes"} which we restate:

::: thm
[]{#thm:zeroes label="thm:zeroes"} Let $\ell>2$ be a prime and $G$ a finite quasi-simple group of $\ell$-rank at least 3. Then for any non-trivial character $\chi\in{\operatorname{Irr}}(G)$ there exists an $\ell$-singular element $g\in G$ with $\chi(g)=0$, unless one of:

1.  $G$ is of Lie type in characteristic $\ell$;

2.  $\ell=5$, $G={\operatorname{L}}_5(q)$ with $5||(q-1)$ and $\chi$ is unipotent of degree $\chi(1)=q^2\Phi_5$;

3.  $\ell=5$, $G={\operatorname{U}}_5(q)$ with $5||(q+1)$ and $\chi$ is unipotent of degree $\chi(1)=q^2\Phi_{10}$; or

4.  $\ell=5$, $G=Ly$ and $\chi(1)\in\{48174,11834746\}$; or

5.  $G=E_8(q)$ with $q$ odd, $d_\ell(q) = 4$ and $\chi$ is the semisimple character with label $((0),(8))$ in the unique Lusztig-series of type $D_8$.
:::

::: proof
*Proof.* For $G$ a covering group of a sporadic simple group, an easy check of the known character tables shows that only case (4) arises. For alternating groups and their covering groups the claim is contained in the proof of [@LMS13 Prop. 4.2 and Thm. 4.5]. If $G$ is a covering group of a special linear or unitary group then [@LM15 Thm. 1.3] shows that only the cases in (1), (2) and (3) can arise.

For the remaining groups of Lie type first note that the Steinberg character vanishes on the product of any $\ell$-element with a unipotent element in its centraliser, so can be discarded from our discussion. We now first consider groups $G$ of exceptional Lie type. Since the $\ell$-rank of $G$ is at least 3, it must be of type $F_4$, $E_6,{}^2\!E_6$, $E_7$ or $E_8$. For these it is shown in the proof of [@LMS13 Thm. 6.11] that their irreducible characters $\chi$ vanish on some $\ell$-singular element unless either $\chi$ is unipotent or $\ell|(q^2+1)$ in $G=E_8(q)$ and $\chi$ lies in the Lusztig series of an isolated element with centraliser $D_8(q)$. We deal with these cases in turn.

We begin with $G=E_8(q)$. Since $G$ has $\ell$-rank at least 3 we must have $d=d_\ell(q)\in\{1,2,3,4,6\}$. First assume that $d=1$. There exist maximal tori of orders divisible by $\Phi_1\Phi_7$, $\Phi_1\Phi_9$ and $\Phi_1\Phi_{14}$, hence $G$ contains semisimple $\ell$-singular elements of order divisible by a Zsigmondy prime divisor $r$ of $\Phi_7,\Phi_9$ and $\Phi_{14}$. All non-trivial unipotent characters apart from $\phi_{8,1},\phi_{8,91}$ and the Steinberg character are of defect zero for one of these three primes, hence vanish on any $r$-singular element. For the remaining two characters, direct calculation with the character formula shows that they vanish on elements of order $\Phi_1\Phi_4$. Very similar considerations apply to the remaining cases $d\in\{2,3,4,6\}$. If $d=4$ and $\chi$ lies in the Lusztig series of an isolated element with centraliser $D_8(q)$, the same argument using Zsigmondy prime divisors of $\Phi_5$, $\Phi_8$, $\Phi_{10}$ and $\Phi_{12}$ only leaves the four characters in that series, those with label $\sys{0}{8}$ and $\sys{0 1}{1 8}$ and their duals. Three of them are zero on suitable products of an $\ell$ element with a unipotent element.

The arguments for the unipotent characters of the remaining exceptional groups are similar and easier.

Finally, let us suppose that $G$ is of classical Lie type. By Theorem [\[thm:non-unip\]](#thm:non-unip){reference-type="ref" reference="thm:non-unip"} the claim holds if $\chi$ is not unipotent. For unipotent characters $\chi$, the claim follows from Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}, since all exceptions listed there have $\ell$-rank two, including those in cases (4) and (5) with $n=3e$ respectively $n=3d$. ◻
:::

::: rem
\(a\) Let $p$ be a prime and $f\ge1$. Then $G={\operatorname{SL}}_2(p^f)$ has $p$-rank $f$, but its irreducible characters of degree $q\pm1$ do not vanish on any $p$-singular elements of $G$. Similarly, there exist such characters for ${\operatorname{SL}}_3(p^f)$, ${\operatorname{SU}}_3(p^f)$ and $^2G_3(3^{2f+1})$. This shows that Case (1) in Theorem [\[thm:zeroes\]](#thm:zeroes){reference-type="ref" reference="thm:zeroes"} is a true exception. Also, $Ly$ has characters of degrees 48174 and 11834746 which do not vanish on 5-singular elements. (It is well-known that the Lyons group behaves like a characteristic 5 group in many respects, see e.g. [@PR].) It can be checked that the unipotent characters of ${\operatorname{L}}_5(q)$ and ${\operatorname{U}}_5(q)$ listed in Cases (2) and (3) are also true exceptions.

\(b\) We expect the exceptions in Case (1) to only occur for groups of Lie type in characteristic $\ell$ of small Lie rank.

\(c\) The results of [@LMS13], [@LM15] and of the present paper show that even for $\ell$-rank 2 there exist only relatively few irreducible characters of quasi-simple groups not vanishing on some $\ell$-singular element. Nevertheless we refrain from attempting to give an explicit list in that case.
:::
