---
doc_id: arxiv-hep-th-9811173v1
doc_title: "arXiv:hep-th/9811173v1 19 Nov 1998"
section_id: sec-003-22-examination-of-44-fields-found-by-snap
section_title: "Examination of 44 fields found by Snap"
section_number: 2.2
pages: 4-7
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.994
doc_brief: "arXiv:hep-th/9811173v1 19 Nov 1998 — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to Dedekind zeta values, with coprime integers a and b giving a b vol(M) ="
---
For the remaining $140-96=44$ results of Tables 2--12, we made reference to the impressive body of files[^1] at the University of Melbourne. These were obtained by Coulson, Goodman, Hodgson and Neumann [@CGHN] (hereafter referred to as CGHN) using 50-digit precision, in marked distinction to the 5 digits which suffice for the findings above.

CGHN make no reference to Dedekind zeta values; they do, however, find single-complex-place invariant trace fields for about 9% of the Hodgson--Weeks manifolds. The next step was to examine the overlap between our single-complex-place fields and theirs. We found that the CGHN file `closed_census_algebras` contains 95 of our 96 single-complex-place fields. The exception was the quintic field with $D=-14103$, for which our low-precision method had readily yielded the rational invariant $a/b=2$ of the manifold ${\rm s}784(+5,2)$, which was absent from the file `closed_census_algebras`, obtained by CGHN from 50-digit searches for fields of degree[^2] not exceeding 16. We then referred to the file `closed.fields`, where ${\rm s}784(+5,2)$ indeed appears, with the expected invariant trace field, $x^5-2x^4+2x^3-x^2-2x-1$.

Thus assured that all our 96 finds were genuine, we extracted all of the invariant trace fields from the CGHN files `closed_census_algebras` and `closed.fields`, and asked Pari to determine their signatures and discriminants. This revealed 44 cases beyond the ranges of our search, namely the 32 below the lines in Tables 4--7 and the 12 in Tables 8--12. Within our selected ranges, CGHN had found all and only our 96 single-complex-place fields, indicating the reliability of both their methods and ours.

The next step was obvious, yet computationally demanding: to determine rational Dedekind-zeta invariants for the manifolds associated by Snap to the remaining 44 large-discriminant single-complex-place fields. The `zetak` command of Pari was entirely adequate to complete Tables 4--7, at 19-digit precision, yielding numerators and denominators bounded by $a\le976$ and $b\le5$, for which merely 7-digit precision would have been amply sufficient. The 12 fields of Tables 8--12 presented a much tougher computational challenge.

At degree $n=8$, Pari-GP 2.0.11 began to falter, with `zetak` yielding results drastically below the requested precision (as warned in the Pari manual) or running out of memory (when allocated 100MB of core). Accordingly we devised a method based on the `dirzetak` command, which returns the multiplicities, $m_K(n)$, of the ideals of $K$ with norm $n$, up to some requested maximum, $N$, that may comfortably extend to $N=10^6$. These multiplicities are the numerators of the Dirichlet series $$\zeta_K(2)=\sum_{n>0}\frac{m_K(n)}{n^2}\label{dirz}$$ We then computed the truncated sums $S_N:=\sum_{n=1}^N m_K(n)/n^2$, and accelerated their convergence by forming $T_{N,M}:=(S_N N-S_M M)/(N-M)$, with $M\approx\frac12N$. This removes a predictable $O(1/N)$ truncation error, leaving an $O(1/N^{3/2})$ "random-walk" error. With $N\le10^6$, we were able to achieve 10-digit precision, by averaging out fluctuations in $T_{N,M}$. Even in the most demanding case of Table 12, where the rational invariant is a 7-digit integer, we were left with 3 vanishing decimal places for $a/b=9408656.000\pm0.001$.

Hence we completed the task for Hodgson--Weeks manifolds. Tables 2--12 give $140$ single-complex-place invariant trace fields of closed census manifolds, of which 96 were detected by us without reference to CGHN. The 224 distinct census volumes rationally related to the Dedekind zeta values of these fields are given in Tables 13a-f. These 224 distinct volumes correspond to 998 of the 11,031 entries of the Hodgson--Weeks census file `ClosedManifolds` available[^3] from the Geometry Center at the University of Minnesota.

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

[^1]: ` http://www.ms.unimelb.edu.au/`$\,\widetilde{}\,$`snap`

[^2]: We later ran Snap at 100-digit precision, and found a group field of degree 20.

[^3]: The 1995 file ` ftp://ftp.geom.umn.edu/pub/software/snappea/tables/ClosedManifolds` contains 11,031 entries; unfortunately some of the Dehn fillings do not correspond to those packaged, internally, with SnapPea. We enlisted Snap, to check all the surgeries given in Tables 2--13.
