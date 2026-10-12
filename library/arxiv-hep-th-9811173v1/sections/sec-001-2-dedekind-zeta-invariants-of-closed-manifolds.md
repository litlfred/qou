---
doc_id: arxiv-hep-th-9811173v1
doc_title: "arXiv:hep-th/9811173v1 19 Nov 1998"
section_id: sec-001-2-dedekind-zeta-invariants-of-closed-manifolds
section_title: "Dedekind-zeta invariants of closed manifolds"
section_number: 2
pages: 3-8
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.998
---
We have found rational Dedekind-zeta invariants for 998 manifolds in the Hodgson--Weeks census, which lists $11,031$ closed orientable manifolds, with 9,218 distinct volumes, all less than $6.5$, and with all their geodesics having lengths greater than $0.3$. These 998 manifolds have 224 distinct volumes, which are rationally related, via ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"},[\[ab\]](#ab){reference-type="ref" reference="ab"}), to 140 distinct Dedekind zeta values, each corresponding to an invariant trace field of at least one census manifold. Table 1 enumerates the fields by degree. Tables 2--12 give, for each field $K$, a generating polynomial, together with its discriminant and the rational relation of $Z_K$ to the volume of the first manifold in the census with invariant trace field $K$. The 224 distinct volumes are given in Tables 13a--f, where it can be observed that numerators and denominators of the 998 invariants are bounded by $a\le9408656$ and $b\le9$. Our methods were as follows.

## Examination of 1,200 single-complex-place fields

It became clear, from studying [@AMS:JB; @AMS:SB; @AMS:RK; @AMS:DZ], that there are unspecified rational relations of the form ([\[ab\]](#ab){reference-type="ref" reference="ab"}) between Dedekind zeta values and volumes of some, but not all, of the manifolds in the Hodgson--Weeks census. We soon found that 30 of the first 32 census manifolds have rational Dedekind-zeta invariants, with $a\le46$ and $b\le3$. The 2 exceptions are manifolds ${\rm m}003(-4,1)$ and ${\rm m}004(+7,1)$, whose invariant trace fields have 2 complex places.

The next step was to obtain systematic listings of fields with precisely one complex place. Thanks to the `numberfields` directory[^1] at the University of Bordeaux, we found files that order single-complex-place fields, for each degree $n\le7$, by the magnitudes, $-D$, of the discriminant. We selected the first 200 fields for each degree $n\in\{2,3,4,5,6,7\}$ and used the `zetak` command of Pari to compute 19 digits of the Dedekind zeta values, $\zeta_K(2)$, of these 1,200 fields. Forming $Z_K$, defined in ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}), we made $1200\times11031=13,237,200$ indiscriminate comparisons between these target fields and the census entries. This took 19 seconds on a 233MHz Pentium. We found 842 manifolds, with 175 distinct volumes, rationally related to 96 distinct Dedekind zeta values, with numerators and denominators of the rational invariants bounded by $a\le46$ and $b\le5$.

Since the census provided 17-digit volumes, the probability of any of these simple rational results being spurious is comfortably less than $10^{-12}$. Conversely, one needs only 5-digit precision for the volume to discover the rational Dedekind-zeta invariant in these 842 cases, and hence to obtain an accurate volume from ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}). Only for degrees $n\ge8$ do precision, core memory and CPUtime become issues. In the $n=12$ case of Table 12, with $|D|=12,476,239,474,594,496$, these issues require close attention.

The 96 fields that were caught by this 19-second trawl comprise all those of Tables 2 and 3 and all those above the lines drawn in Tables 4--7. Below the lines, and in Tables 8--12, we took assistance from Melbourne [@CGHN].

## Examination of 44 fields found by Snap

For the remaining $140-96=44$ results of Tables 2--12, we made reference to the impressive body of files[^2] at the University of Melbourne. These were obtained by Coulson, Goodman, Hodgson and Neumann [@CGHN] (hereafter referred to as CGHN) using 50-digit precision, in marked distinction to the 5 digits which suffice for the findings above.

CGHN make no reference to Dedekind zeta values; they do, however, find single-complex-place invariant trace fields for about 9% of the Hodgson--Weeks manifolds. The next step was to examine the overlap between our single-complex-place fields and theirs. We found that the CGHN file `closed_census_algebras` contains 95 of our 96 single-complex-place fields. The exception was the quintic field with $D=-14103$, for which our low-precision method had readily yielded the rational invariant $a/b=2$ of the manifold ${\rm s}784(+5,2)$, which was absent from the file `closed_census_algebras`, obtained by CGHN from 50-digit searches for fields of degree[^3] not exceeding 16. We then referred to the file `closed.fields`, where ${\rm s}784(+5,2)$ indeed appears, with the expected invariant trace field, $x^5-2x^4+2x^3-x^2-2x-1$.

Thus assured that all our 96 finds were genuine, we extracted all of the invariant trace fields from the CGHN files `closed_census_algebras` and `closed.fields`, and asked Pari to determine their signatures and discriminants. This revealed 44 cases beyond the ranges of our search, namely the 32 below the lines in Tables 4--7 and the 12 in Tables 8--12. Within our selected ranges, CGHN had found all and only our 96 single-complex-place fields, indicating the reliability of both their methods and ours.

The next step was obvious, yet computationally demanding: to determine rational Dedekind-zeta invariants for the manifolds associated by Snap to the remaining 44 large-discriminant single-complex-place fields. The `zetak` command of Pari was entirely adequate to complete Tables 4--7, at 19-digit precision, yielding numerators and denominators bounded by $a\le976$ and $b\le5$, for which merely 7-digit precision would have been amply sufficient. The 12 fields of Tables 8--12 presented a much tougher computational challenge.

At degree $n=8$, Pari-GP 2.0.11 began to falter, with `zetak` yielding results drastically below the requested precision (as warned in the Pari manual) or running out of memory (when allocated 100MB of core). Accordingly we devised a method based on the `dirzetak` command, which returns the multiplicities, $m_K(n)$, of the ideals of $K$ with norm $n$, up to some requested maximum, $N$, that may comfortably extend to $N=10^6$. These multiplicities are the numerators of the Dirichlet series $$\zeta_K(2)=\sum_{n>0}\frac{m_K(n)}{n^2}\label{dirz}$$ We then computed the truncated sums $S_N:=\sum_{n=1}^N m_K(n)/n^2$, and accelerated their convergence by forming $T_{N,M}:=(S_N N-S_M M)/(N-M)$, with $M\approx\frac12N$. This removes a predictable $O(1/N)$ truncation error, leaving an $O(1/N^{3/2})$ "random-walk" error. With $N\le10^6$, we were able to achieve 10-digit precision, by averaging out fluctuations in $T_{N,M}$. Even in the most demanding case of Table 12, where the rational invariant is a 7-digit integer, we were left with 3 vanishing decimal places for $a/b=9408656.000\pm0.001$.

Hence we completed the task for Hodgson--Weeks manifolds. Tables 2--12 give $140$ single-complex-place invariant trace fields of closed census manifolds, of which 96 were detected by us without reference to CGHN. The 224 distinct census volumes rationally related to the Dedekind zeta values of these fields are given in Tables 13a-f. These 224 distinct volumes correspond to 998 of the 11,031 entries of the Hodgson--Weeks census file `ClosedManifolds` available[^4] from the Geometry Center at the University of Minnesota.

## A special case: manifold ${\rm v}3066(-1,2)$

We note a peculiarity of manifold ${\rm v}3066(-1,2)$, with the same volume as ${\rm v}3066(+1,2)$. The latter has unit Dedekind-zeta invariant and hence a volume $$Z_{K_+}:=\frac{59^{3/2}}{(2\pi)^2}\,\frac{\zeta_{K_+}(2)}{2\zeta(2)}
=5.137941201873417769841348339\ldots
\label{v3066}$$ where the cubic invariant trace field of ${\rm v}3066(+1,2)$ is $$K_+:=x^3+2x-1\label{K3p}$$ with discriminant $-59$. Snap, working at 100-digit precision, gave the invariant trace field of ${\rm v}3066(-1,2)$ as a join of ([\[K3p\]](#K3p){reference-type="ref" reference="K3p"}) with ${\bf Q}(\sqrt{-59})$, generated by a root of the sextic $$K_-:=x^6-3x^5+10x^4-15x^3+21x^2-14x+4\label{K6m}$$ with discriminant $(-59)^3$ and 3 complex places. The Borel regulator [@CGHN; @NY] of ${\rm v}3066(-1,2)$ was given as $\left[Z_{K_+},-\frac12Z_{K_+},-\frac12Z_{K_+}\right]$. It thus appears that a single-complex-place invariant trace field is sufficient, yet *not* necessary, to give a rational Dedekind-zeta invariant.

## How may one *derive* the rational invariant?

Some of our results contain non-trivial factors, with 4-digit and 3-digit primes in $3\times1223=3669$ and $2^4\times3\times5\times967=232,080$, from Table 10, and $2\times3\times7\times11\times149=68,838$, from Table 11. Their origins are obscure. The duodecadic example of Table 12 entails $a/b=2^4\times23\times37\times691=9,408,656$. We note, though cannot explain, the circumstance that its largest prime factor also occurs in $\zeta(12)/\pi^{12}
=\frac{691}{638512875}$. Reverse engineering gave 50 decimal places of $$\begin{aligned}
\zeta_{K_{12}}(2)&=&
1.06095699592540035751698213238632531266926282705990
\ldots\label{50dp}\\
K_{12}&:=&
x^{12}-3x^{11}-8x^{10}+17x^9+27x^8-19x^7-50x^6
\nonumber\\&&{}
-24x^5+44x^4+37x^3-5x^2-8x-1
\label{K12}
\end{aligned}$$ from high-precision triangulation of manifold ${\rm v}2824(+4,1)$. We know of no easy way to check ([\[50dp\]](#50dp){reference-type="ref" reference="50dp"}) beyond the first 10 digits, confirmed by accelerated convergence of a million truncations of ([\[dirz\]](#dirz){reference-type="ref" reference="dirz"}).

Arguments from $K$-theory [@AMS:JB; @AMS:DZ] appear powerless to derive values for the Dedekind-zeta invariant, $a/b$, though they imply [@DZ:Invent; @DZ:JMPS; @DZ:Texel] its rationality, for every manifold whose invariant trace field has a single complex place. It thus remains a challenge to derive the simple value $a/b=4$, for the quadratic manifold ${\rm m}036(-4,3)$, with invariant trace field ${\bf Q}(\sqrt{-7})$ and volume observed, at 1800-digit precision, to coincide with $$\begin{aligned}
\frac14Z_{{\bf Q}(\sqrt{-7})}&=&
\frac74\left\{{\rm Cl}_2\left(\frac{2\pi}{7}\right)
+{\rm Cl}_2\left(\frac{4\pi}{7}\right)
-{\rm Cl}_2\left(\frac{6\pi}{7}\right)\right\}\label{Q7}\\
&=&
2.66674478344905979079671246261065004409838388855263
\ldots\label{V7}
\end{aligned}$$ whose reduction to $${\rm Cl}_2(\theta):=\sum_{n>0}\frac{\sin(n\theta)}{n^2}\label{Cl}$$ is derived in Section 4. Triangulation gives $$\begin{aligned}
{\rm vol}({\rm m}036(-4,3))&=&
2D\left(-e^{-i\theta_7}\right)
+D\left(-\mbox{$\frac12$}e^{-i\theta_7}\right)\label{T7}\\
\theta_7&:=&2\arctan\sqrt7
\end{aligned}$$ where the Bloch--Wigner dilogarithm $$D(z):=\Im{\rm Li}_2(z)+\log|z|\Im\log(1-z)
=\Im\sum_{n>0}\left(\frac{1}{n^2}-\frac{\log|z|}{n}\right)z^n
\label{BW}$$ gives the volume of an ideal tetrahedron whose essential dihedral angles are the arguments of $\{z,1/(1-z),1-1/z\}$. The 1800-digit agreement of ([\[T7\]](#T7){reference-type="ref" reference="T7"}) with ([\[Q7\]](#Q7){reference-type="ref" reference="Q7"}) is compelling evidence that, with $\theta_7:=2\arctan\sqrt7$, $$\frac32{\rm Cl}_2(\theta_7)
-\frac32{\rm Cl}_2(2\theta_7)+\frac12{\rm Cl}_2(3\theta_7)=
\frac74\left\{{\rm Cl}_2\left(\frac{2\pi}{7}\right)
+{\rm Cl}_2\left(\frac{4\pi}{7}\right)
-{\rm Cl}_2\left(\frac{6\pi}{7}\right)\right\}\label{todo}$$

An elementary proof of this remarkable relation between Clausen values has escaped both us, and also, it appears, the authors of [@AMS:JB; @AMS:SB; @AMS:RK; @AMS:DZ]. To cast it in a less classical form, we multiply ([\[todo\]](#todo){reference-type="ref" reference="todo"}) by 2, and transform to Bloch--Wigner functions, obtaining $$4\,D\left(\frac{3+i\sqrt7}{4}\right)+
2\,D\left(\frac{3+i\sqrt7}{8}\right)=
7\,D\left(2\frac{1+i\tan{\pi\over7}}
{3-\tan^2{\pi\over7}}\right)
\label{modern}$$ where the argument on the r.h.s. is a root of the totally complex sextic $$K_6:=x^6-4x^5+9x^4-8x^3+4x^2-2x+1\label{K6}$$ with discriminant $(-7)^5$. The l.h.s. of ([\[modern\]](#modern){reference-type="ref" reference="modern"}) is the volume of the cusped manifold ${\rm s}776$, which is complementary to the 3-component 6-crossing link $6^3_1$. Its triangulation immediately yields 6 ideal tetrahedra, with 2 distinct shapes in the quadratic field ${\bf Q}(\sqrt{-7})$. The challenge is to prove that by combining these 6 one forms the same volume as from the 7 congruent sextic shapes on the r.h.s. of ([\[modern\]](#modern){reference-type="ref" reference="modern"}). This is a modern version of our puzzle ([\[todo\]](#todo){reference-type="ref" reference="todo"}) in classical analysis: how may one relate Clausen values at multiples of $\theta_7:=2\arctan\sqrt7$ to Clausen values at multiples of $2\pi/7$, when there appears to be no non-trivial relation between trigonometric functions of the two sets of angles? A far greater challenge would be to derive, rather than merely measure, the integer Dedekind-zeta invariant $2^4\times23\times37\times691$ of the closed manifold ${\rm v}2824(+4,1)$.

# Cusped manifolds and join fields

Now we turn to the study of cusped manifolds, complementary to knots and links. Packaged with SnapPea [@SnapPea], there are the 4,815 orientable cusped manifolds of the Hildebrand--Weeks census [@HiW], triangulated by no more than 7 ideal tetrahedra, and 114 non-orientable manifolds, triangulated by no more than 5. Making $4929\times1200$ comparisons with the Dedekind zeta values of Section 2.1, we found 7 new single-complex-place fields, beyond those from the Hodgson--Weeks census. Then the CGHN file `cusped.fields` confirmed these finds and yielded the remaining 5 fields of Table 14, with larger discriminants. In Table 14, we give the rational Dedekind-zeta invariant of a selected cusped manifold for each of the 12 new fields.

Our tally of single-complex-place fields is now $96+44+7+5=152$. Among the $4,929$ cusped manifolds, we found 312 whose volumes are rationally related to one of the 152 Dedekind zeta values, with numerators and denominators in ([\[ab\]](#ab){reference-type="ref" reference="ab"}) bounded by $a\le2853$ and $b\le7$.

We also sought integer relations of the form $$a\,{\rm vol}({\cal M})=b_1Z_{K_1}+b_2Z_{K_2}
\label{ab12}$$ corresponding to a cusped or closed manifold ${\cal M}$ whose invariant trace field is the join of single-complex-place fields $K_1$ and $K_2$, or is a subfield of this join. Restricting $K_1$ and $K_2$ to the 152 fields of Tables 2--12 and Table 14, we found 91 census manifolds, with 26 distinct volumes, rationally related, via ([\[ab12\]](#ab12){reference-type="ref" reference="ab12"}), to pairs of Dedekind zeta values. Details of the 29 cusped and 62 closed manifolds are provided by Tables 15--18. Two of the 26 integer relations entail join fields noted in [@CGHN], namely the first in Table 16 and the second in Table 17. We used Pari's `nfisincl` command to confirm that all 6 of the quartic invariant trace fields in Table 18 are subfields of the octadic joins. In 4 of these 6 cases, distinct values of $b_1/b_2$ occur, for the same invariant trace field.

We believe that we have exhausted the 3-term relations between census volumes and pairs of the 152 target Dedekind zeta values. David Bailey's impressively efficient, arbitrary precision [@TRANSMP], implementation of PSLQ [@PSLQ] found the 91 relations in 40 minutes and then took 17 hours to exhaust the $(4815+114+11031)\times{152\choose2}=183,156,960$ indiscriminate possibilities. The PSLQ search rate was thus a healthy 3 kHz. No reduction to 3 distinct Dedekind zeta values was detected, presumably because the census volumes are kept deliberately small.

[^1]: `ftp://megrez.math.u-bordeaux.fr/pub/numberfields`

[^2]: ` http://www.ms.unimelb.edu.au/`$\,\widetilde{}\,$`snap`

[^3]: We later ran Snap at 100-digit precision, and found a group field of degree 20.

[^4]: The 1995 file ` ftp://ftp.geom.umn.edu/pub/software/snappea/tables/ClosedManifolds` contains 11,031 entries; unfortunately some of the Dehn fillings do not correspond to those packaged, internally, with SnapPea. We enlisted Snap, to check all the surgeries given in Tables 2--13.
