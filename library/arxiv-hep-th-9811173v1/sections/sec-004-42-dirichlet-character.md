---
doc_id: arxiv-hep-th-9811173v1
doc_title: "arXiv:hep-th/9811173v1 19 Nov 1998"
section_id: sec-004-42-dirichlet-character
section_title: "Dirichlet character"
section_number: 4.2
pages: 9-13
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.992
---
The simplest example of a number field with a single complex place is an imaginary-quadratic field ${\bf Q}(\sqrt{-d})$, where $d$ is a square-free positive integer. When $d\equiv3$ (mod 4), the discriminant is $D=-d$; otherwise it is $D=-4d$.

It is proven in [@Berndt] that $$\frac{\zeta_K(2)}{\zeta(2)}=\sum_{n>0}\frac{\chi_K(n)}{n^2}\label{chi}$$ where $\chi_K$ is the real Dirichlet character of the group of units of the field ${\bf Z}/|D|$ and $D$ is the discriminant of the imaginary-quadratic field $K$. The Dirichlet character is related to the Jacobi (or Kronecker) symbol by $$\chi_K(n)=\left(\frac{D}{n}\right)\label{Jacobi}$$ which vanishes if ${\rm gcd}(D,n)>1$. When $D$ is odd, one may use the alternative form $\left(\frac{n}{|D|}\right)$.

Using ([\[chi\]](#chi){reference-type="ref" reference="chi"}) in ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}), at $n=2$, one happily disposes of powers of $\pi$. We dispose of $\sqrt{-D}$, by using the imaginary-quadratic result [@Berndt] $$\sum_{n>0}\frac{\chi_K(n)}{n^2}=
\frac{1}{\sqrt{-D}}\sum_{-D>k>0}\chi_K(k)
{\rm Cl}_2\left(\frac{2\pi k}{|D|}\right)\label{chik}$$ which yields a finite sum over the elements of the group of units. Finally, we dispose of a factor 2, via the reflection relations $\chi_K(k)=-\chi_K(|D|-k)$ and ${\rm Cl}_2(\theta)=-{\rm Cl}_2(2\pi-\theta)$, to obtain the readily computable result $$Z_K=Z_{|D|}:=D\sum_{-D>2k>0}\left(\frac{D}{k}\right)
{\rm Cl}_2\left(\frac{2\pi k}{D}\right)\label{ZKq}$$ with the magnitude of the discriminant identifying the imaginary-quadratic field.

Thanks to David Bailey [@TRANSMP], it is now a routine matter to evaluate ([\[ZKq\]](#ZKq){reference-type="ref" reference="ZKq"}) to high precision[^1], using [@Lewin] $$\frac{{\rm Cl}_2(\theta)}{\theta}
=1-\df12\log(\theta^2) +\sum_{n=1}^\infty\frac{\zeta(2n)}{2n^2+n}
\left(\frac{\theta}{2\pi}\right)^{2n}
\label{cl2}$$ which converges faster than $1/9^n$, for $\theta\in[0,2\pi/3]$. An angle in $[2\pi/3,\pi]$ may be transformed to a pair in $[0,2\pi/3]$, by rearrangement of the duplication formula $$\df12{\rm Cl}_2(2\theta)={\rm Cl}_2(\theta)-{\rm Cl}_2(\pi-\theta)
\label{dub}$$ Rather than compute $\zeta(2n)/(2\pi)^{2n}
=\frac12|B_{2n}|/(2n)!$ recursively, from the Bernoulli numbers, we used a FFT program written by David Bailey to evaluate $\{\zeta(2n)\mid 0\le n<2^{m}\}$, in one fell swoop, by a multi-dimensional generalization of Newton's method. With $m=11$, the initial outlay, to tabulate 2048 coefficients to 1800 digits, was 8 minutes; then 1800 good digits of any Clausen value in $\{{\rm Cl}_2(\theta)\mid 0<\theta<2\pi/3\}$ are obtainable in less than 2 seconds on a 533MHz machine. Low-precision results for $Z_{|D|}$ are given in Table 19.

It follows from ([\[ZKq\]](#ZKq){reference-type="ref" reference="ZKq"}) that every discovery of a rational Dedekind-zeta invariant for a quadratic link gives a relation between a set of Clausen values at angles whose tangents involve $\sqrt d$, and a set of Clausen values at angles which are multiples of $2\pi/|D|$. We have already seen this, rather strikingly, in the case $-D=d=7$ of ([\[todo\]](#todo){reference-type="ref" reference="todo"}), where the hyperbolic 6-crossing 3-component link[^2] $6^3_1$ mediates between Clausen values, and hence the Bloch--Wigner dilogarithms of ([\[modern\]](#modern){reference-type="ref" reference="modern"}), with very different types of argument on the left and right.

We now address the question: which links have volumes that link Clausen values?

## Figure-8 knot at $D=-3$

The first case, at $D=-3$, is elementary. The unique[^3] arithmetic knot is the figure-8 knot of Fig. 3. Its volume is the first entry of Table 19. It links Clausen values at $2\arctan\sqrt3$ and $2\pi/3$. This relation clearly poses no analytical puzzle, since the angles are identical.

## Whitehead link at $D=-4$

Just as the simplest hyperbolic knot, $4_1$, gave the answer at $D=-3$, so the simplest hyperbolic 2-component link, namely the Whitehead link $5^2_1$ of Fig. 4, gives the answer at $D=-4$. Its volume is the second entry of Table 19. It links Clausen values at $2\arctan\sqrt1$ and $2\pi/4$, which are again identical.

## Link $6^3_1$ at $D=-7$

The Dedekind-zeta invariant of the link $6^3_1$, illustrated in Fig. 5, is measured to be $2$, corresponding to $$2\left\{3{\rm Cl}_2(\theta_7)
-3{\rm Cl}_2(2\theta_7)+{\rm Cl}_2(3\theta_7)\right\}=Z_7=
7\left\{{\rm Cl}_2\left(\frac{2\pi}{7}\right)
+{\rm Cl}_2\left(\frac{4\pi}{7}\right)
-{\rm Cl}_2\left(\frac{6\pi}{7}\right)\right\}\label{d7}$$ with $\theta_7:=2\arctan\sqrt7$. At 1800-digit precision, PSLQ finds this to be the sole integer relation between the 6 Clausen values. The combination on the left is selected by hyperbolic geometry; that on the right by the Dirichlet character. Thus the rational Dedekind-zeta invariant of link $6^3_1$ encodes a highly non-trivial analytical relation between Clausen values. A derivation of $a/b=2$ would prove ([\[d7\]](#d7){reference-type="ref" reference="d7"}). Conversely, a proof of ([\[d7\]](#d7){reference-type="ref" reference="d7"}) would derive $a/b=2$. Where may one find *any* such proof?

## Link $9^2_{40}$ at $D=-8$

As exemplar of the next non-trivial relation between Clausen values, we select the 9-crossing 2-component link $9_{40}^2:=(\sigma_1^2\sigma_2^{-1})^3$ of Fig. 6. Its Dedekind-zeta invariant is observed to be unity, which implies that its volume is equal to each side of $$\df12\left\{27{\rm Cl}_2(\theta_2)-9{\rm Cl}_2(2\theta_2)
+{\rm Cl}_2(3\theta_2)\right\}
=Z_8=8\left\{{\rm Cl}_2\left(\frac{2\pi}{8}\right)
+{\rm Cl}_2\left(\frac{6\pi}{8}\right)\right\}
\label{d8}$$ with $\theta_2:=2\arctan\sqrt2$. As in the case of ([\[d7\]](#d7){reference-type="ref" reference="d7"}), a proof is lacking.

## A 12-crossing 4-component link at $D=-11$

In [@CGHN] it was noted that neither the closed nor the cusped census entails the field ${\bf Q}(\sqrt{-11})$. In [@9806174] it was observed that the 12-crossing 4-component link of Fig. 7, with braid word $(\sigma_1^{}\sigma_2^{-2}\sigma_3^{}\sigma_2^{-2})^2$, entails this field. Its Dedekind-zeta invariant is observed to be unity, corresponding to the relation $$15{\rm Cl}_2(\theta_{11})-10{\rm Cl}_2(2\theta_{11})
+{\rm Cl}_2(5\theta_{11})=Z_{11}=11\sum_{k=1}^5\left(\frac{k}{11}\right)
{\rm Cl}_2\left(\frac{2\pi k}{11}\right)
\label{d11}$$ where $\theta_{11}:=2\arctan\sqrt{11}$ and $\left(\frac{k}{11}\right)$ is the Jacobi (or Legendre) symbol for the Dirichlet character. Again, we lack a proof.

## A 12-crossing 3-component link at $D=-15$

The next case likewise comes from [@9806174]. The 12-crossing 3-component link of Fig. 8, with braid word $(\sigma_1^2\sigma_2^{-2})^3$, has Dedekind-zeta invariant empirically equal to 2, at 1800-digit precision. This corresponds to the relation $$24{\rm Cl}_2(\theta_{5,3})-12{\rm Cl}_2(2\theta_{5,3})
-8{\rm Cl}_2(3\theta_{5,3})
+6{\rm Cl}_2(4\theta_{5,3})=Z_{15}
=15\sum_{k=1}^7\left(\frac{k}{15}\right)
{\rm Cl}_2\left(\frac{2\pi k}{15}\right)
\label{d15}$$ with $\theta_{5,3}:=2\arctan\sqrt{5/3}$. Again, where is the proof?

## A self-dual platonic link at $D=-20$

The reader might now expect us to consider the case $D=-19$. For reasons that will be given in Section 5, we skip to $D=-20$, where we were rewarded by the splendidly symmetric alternating platonic link drawn in Fig. 1. Its Dedekind-zeta invariant was measured to be unity. This innocent-sounding statement translates to our 5th unproven relation $$36{\rm Cl}_2(\theta_5)-30{\rm Cl}_2(2\theta_5)
+4{\rm Cl}_2(3\theta_5)+3{\rm Cl}_2(4\theta_5)=Z_{20}
=20\sum_{k\in\{1,3,7,9\}}{\rm Cl}_2\left(\frac{2\pi k}{20}\right)
\label{d20}$$ with $\theta_5:=2\arctan\sqrt5$. Between these 8 Clausen values, PSLQ found no other relation.

We found that, far from complicating the result, the 4 Clausen values on the left simplify the 54 Bloch--Wigner values of the triangulation in ${\bf Q}(\sqrt{-5})$. There is, of course, an infinity of rewritings of ([\[d20\]](#d20){reference-type="ref" reference="d20"}), obtained by adding, on the left, combinations of Bloch--Wigner values that algebraically [@AMS:SB] sum to zero, by virtue of special cases of the classical [@Lewin] 2-variable 5-dilogarithm relation of Abel, which is easily proved by differentiation. Here, as elsewhere, we expose the classical analysis that remains to be done.

## A 48-crossing daisy-chain link at $D=-24$

The attentive reader will now expect us to skip the case $D=-23$ and jump to the 8th underlining in ([\[iq\]](#iq){reference-type="ref" reference="iq"}), at $D=-24$. This is precisely what we did, though the character of the result was not what we first supposed. It seemed to us that the hallmark of past success, in finding links that link Clausen values, was to achieve the largest possible symmetry group. What, we asked ourselves, could pack a better symmetry-to-crossing ratio than the remaining 4 platonic alternating links?

Let us denote the tetrahedral link of Fig. 1 by $T:=24^{10}_{\rm tet}$. The 4 non-self-dual alternating platonic links have components that mimic the vertices and edges of the cube $C:=48^{20}_{\rm cub}$, octahedron $O:=48^{18}_{\rm oct}$, dodecahedron $D:=120^{50}_{\rm dod}$, and icosahedron $I:=120^{42}_{\rm ico}$, where, for example, the last has 120 alternating crossings of its 42-components, which mimic the 12 vertices and 30 edges of the perfect solid with 20 faces. These links are highly symmetrical, yet none of their 4 volumes yielded the sought-for rational relation to a quadratic Dedekind zeta value. Later, we show that they are quartic links.

Instead, we found an answer to our 8th question by a more child-like construction: a non-alternating daisy chain. By a daisy chain we mean a link each of whose components has 2 crossings with a neighbour on one side, and 2 crossings with a neighbour on the other, with the whole forming a circle, as in Fig. 2. By a non-alternating daisy chain, we mean one in which the 4 crossings of each component occur in an order over-over-under-under, while still linking with neighbours. A little doodling should convince the reader that non-alternating daisy-chain links must have an even number of components.

A delightful feature of Jeff Weeks' program SnapPea [@SnapPea] is that it enables one to draw such chains quickly, and then ask whether the resultant non-alternating link has quadratic shapes in its triangulation. Using A.C. Manoharan's port of SnapPea to Windows95[^4], we inferred, from instances with up to 96 crossings, that the non-alternating daisy-chain link with $2n\ge6$ components, and hence $4n\ge12$ crossings, has hyperbolic volume $$V_{2n}=8nD\left(i\tan\frac{(n-2)\pi}{4n}\right)\label{daisy}$$ The first 4 hyperbolic non-alternating daisy chains yield results with $-D\in\{3,4,8,20\}$: $$\begin{aligned}
V_6&=&4Z_4\label{dc6}\\
V_8&=&2Z_8\label{dc8}\\
V_{10}&=&\df12Z_{20}+V_6\label{dc10}\\
V_{12}&=&20Z_3\label{dc12}
\end{aligned}$$ Then nothing interesting happens until we reach 24 components, with 48 crossings, where $$V_{24}=Z_{24}+V_{8}\label{dc24}$$ hits the target, at $D=-24$.

SnapPea illustrates this nicely. Drawing daisy chains with 6, 8, 10, 12, 24 components, and inspecting the triangulations, one detects the square roots of 1, 2, 5, 3, 6. The last, illustrated in Fig. 2, delivers a result for $Z_{24}=V_{24}-V_{8}$, namely $$60{\rm Cl}_2(\theta_{3,2})-18{\rm Cl}_2(2\theta_{3,2})
-4{\rm Cl}_2(3\theta_{3,2})+3{\rm Cl}_2(4\theta_{3,2})=Z_{24}
=24\sum_{k\in\{1,5,7,11\}}{\rm Cl}_2\left(\frac{2\pi k}{24}\right)
\label{d24}$$ with $\theta_{3,2}:=2\arctan\sqrt{3/2}$. So, for the 6th time, we have a relation that is as easy to check numerically as it appears hard to derive.

[^1]: ` http://science.nas.nasa.gov/Groups/AAA/db.webpage/mpdist/mpdist.html`

[^2]: We use the notation of [@Rolfsen], whose appendix give drawings of links up to 9 crossings.

[^3]: See Helaman Ferguson's sculpture at ` http://www.mtholyoke.edu/acad/math/ma/sculpture.htm`

[^4]: ` http://home.att.net/`$\,\widetilde{}\,$`Manoharan/SnapPea/snappea.html`
