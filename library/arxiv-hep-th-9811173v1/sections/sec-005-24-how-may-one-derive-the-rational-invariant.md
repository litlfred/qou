---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-005-24-how-may-one-derive-the-rational-invariant
section_title: "How may one derive/ the rational invariant?"
section_number: 2.4
pages: 6-7
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
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
