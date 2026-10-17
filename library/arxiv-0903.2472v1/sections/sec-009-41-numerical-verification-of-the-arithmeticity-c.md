---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-009-41-numerical-verification-of-the-arithmeticity-c
section_title: "Numerical verification of the arithmeticity conjecture"
section_number: 4.1
pages: 44-51
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.993
---
[]{#sec:arith_example label="sec:arith_example"}

In this section, we explicitly calculate the perturbative $SL(2,{\mathbb{C}})$ invariants $S_n^{(\alpha)} (u)$ for the simplest hyperbolic knot complements and for the special value of $u=0$ (corresponding to the discrete faithful representation $\rho = {\rm geom}$). It was conjectured in [@gukov-2003] that such invariants (in fact, for arbitrary value of $u$) can be extracted from the asymptotic expansion of knot invariants computed by Chern-Simons theory with compact gauge group $G$ in the double-scaling limit [\[dslimit\]](#dslimit){reference-type="eqref" reference="dslimit"}. In the present case, $G=SU(2)$ and the relevant knot invariant is $${\cal J}(K;N) =  \frac{J_N\bigl(K;\,e^{2\pi i/N}\bigr)}{J_N\bigl({\rm unknot};\,e^{2\pi i/N}\bigr)}\,,$$ where $J_N(K;q)$ is the "$N$-colored Jones polynomial" of $K$, normalized such that $$J_N ({\rm unknot};q) = \frac{q^{N/2}-q^{-N/2}}{q^{1/2}-q^{-1/2}}$$ is the "quantum dimension" of the $N$-dimensional representation of $SU(2)$. As explained in the Introduction and then in more detail in Section [\[sec:analytic\]](#sec:analytic){reference-type="ref" reference="sec:analytic"}, the $N$-colored Jones polynomial $J_N(K;q)$ is computed by the Feynman path integral in Chern-Simons gauge theory on ${\bf S}^3$ with a Wilson loop operator, $W_R (K)$, supported on $K$ and labeled by the $N$-dimensional representation $R$ of $SU(2)$, *cf.* [\[wilsonp\]](#wilsonp){reference-type="eqref" reference="wilsonp"}. According to the Generalized Volume Conjecture [@gukov-2003], the invariant ${\cal J}(K;N)$ should have the asymptotics[^1] $$\label{JKn} {\cal J}(K;N) \;\sim\; \frac{ Z^{\text{(geom)}}(M;\,i\pi/N)}
  {Z({\bf S}^1 \times {\bf D}^2;\,i\pi/N)}\;\sim\;N^{3/2}\, \exp\left( \sum_{n=0}^\infty s_n \biggl(\frac{2\pi i}N\biggr)^{n-1} \right)$$ as $N\to\infty$, where $$\begin{aligned}
S_n^{(\rm geom)}(0) & = s_n \cdot 2^{n-1} \qquad(n \ne 1) \label{Ss} \\
S_1^{(\rm geom)}(0) & = s_1 + \frac{1}{2} \log 2 \qquad(n=1) \nonumber
\end{aligned}$$ are the perturbative $SL(2,{\mathbb{C}})$ invariants of $M = {\bf S}^3 \smallsetminus K$. (Here, we view the solid torus, ${\bf S}^1 \times {\bf D}^2$, as the complement of the unknot in the 3-sphere.) Specifically, we have $$\label{VolConj} s_0\,=\,i\,\bigl(\text{Vol}(M)\,+\,i\,{\rm CS}(M)\bigr)$$ (Volume Conjecture) and $s_1$ is the Ray-Singer torsion of $M$ twisted by a flat connection, *cf.* eq. [\[sonetorsion\]](#sonetorsion){reference-type="eqref" reference="sonetorsion"}. The arithmetic TQFT conjecture described in Section [\[sec:loops\]](#sec:loops){reference-type="ref" reference="sec:loops"} predicts that $$\label{ArithConj} s_1\;\in\;\mathbb Q\cdot\log\mathbb K\,,\quad\qquad s_n\;\in\;\mathbb K\qquad(n\ge2),$$ where $\mathbb K$ is the trace field of the knot. In this subsection, we will give numerical computations supporting this conjecture for the two simplest hyperbolic knots ${\bf 4_1}$ and ${\bf 5_2}$.

The formulas for ${\cal J}(K;N)$ in both cases are known explicitly, see *e.g.* [@kashaev-1997]. We have $$\label{Jones41} {\cal J}({\bf 4_1};N)=\sum_{m=0}^{N-1}(q)_m(q^{-1})_m\,,$$ $$\label{Jones52} {\cal J}({\bf 5_2};N) = \sum_{m=0}^{N-1}\sum_{k=0}^m q^{-(m+1)k}(q)_m^2/(q^{-1})_k\,,$$ where $q=e^{2\pi i/N}$ and $(q)_m=(1-q)\cdots(1-q^m)$ is the $q$-Pochhammer symbol as in Section [\[sec:qdilog\]](#sec:qdilog){reference-type="ref" reference="sec:qdilog"}. The first few values of these invariants are $$\label{tab:jntwoknots}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|c||c|c|c| }
\hline  $N$& ${\cal J}({\bf 4_1};N)$& ${\cal J}({\bf 5_2};N)$
\\
\hline 1  & $ 1$ & $1$
\\
\hline 2  & $5$ & $7$
\\
\hline 3  & $13$ & $18-5q$
\\
\hline 4  & $27$ & $40-23q$
\\
\hline 5  & $44-4q^2-4q^3$ & $46-55q-31q^2+q^3$
\\
\hline 6  & $89$ & $120-187q$
\\
\hline 7  & $100-14q^2-25q^3-25q^4-14q^5$ & $-154q-88q^2+47q^3+58q^4+77q^5$
\\
\hline 8  & $187-45q-45q^3$ & $-84-407q-150q^2+96q^3$
\\
\hline
\end{tabular}$$

Using formula [\[Jones41\]](#Jones41){reference-type="eqref" reference="Jones41"} for $N$ of the order of 5000 and the numerical interpolation method explained in [@zagVass] and [@GruenMor], we computed the values of $s_n$ for $0\le n\le 27$ to very high precision, finding that [\[JKn\]](#JKn){reference-type="eqref" reference="JKn"} holds with $$\label{FirstTwo} s_0 =\frac1{2\pi^2i}\,D\bigl(e^{\pi i/3}\bigr),\qquad s_1=-\frac14\,\log3\,,$$ the first in accordance with the volume conjecture and the second in accordance with the first statement of [\[ArithConj\]](#ArithConj){reference-type="eqref" reference="ArithConj"}, since $\mathbb K=\mathbb Q\bigl(\sqrt{-3}\bigr)$ in this case, and that the numbers $$\label{rational} s'_n=s_n\cdot\bigl(6\sqrt{-3}\bigr)^{n-1}\qquad(n\ge2)$$ were very close to rational numbers with relatively small and highly factored denominators: $$\label{tab:sjprime}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|c||c|c|c|c|c|c|c|c| }
\hline  $n$ & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$ & $9$
\\
\hline $s'_n$ &$\frac{11}{12}$ & 2 & $\frac{1081}{90}$ &
 98 & $\frac{110011}{105}$ & $\frac{207892}{15}$ & $\frac{32729683}{150}$ & $\frac{139418294}{35}$
\\
\hline
\end{tabular}$$ $$\label{tab:sjprimecontd}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|c||c|c|c| }
\hline  $n$ & $10$ & $\quad\dots\quad$ & $27$
\\
\hline $s'_n$ & $\frac{860118209659}{10395}$ & $\quad\dots\quad$ &
$\frac{240605060980290369529478710291172763261781986098552}{814172781296875}$
\\
\hline
\end{tabular}$$ confirming the second prediction in [\[ArithConj\]](#ArithConj){reference-type="eqref" reference="ArithConj"}. Here $D(z)$ is the Bloch-Wigner dilogarithm [\[BW\]](#BW){reference-type="eqref" reference="BW"}. (That $s_n$ is a rational multiple of $(\sqrt{-3})^{n-1}$, and not merely an element of $\mathbb Q(\sqrt{-3})$ is a consequence of [\[JKn\]](#JKn){reference-type="eqref" reference="JKn"} and the fact that ${\cal J}({\bf 4_1};N)$ is real.)

Actually, in this case one can prove the correctness of the expansion rigorously: the two formulas in [\[FirstTwo\]](#FirstTwo){reference-type="eqref" reference="FirstTwo"} were proved in [@andersen-hansen] and the rationality of the numbers $s'_n$ defined by [\[rational\]](#rational){reference-type="eqref" reference="rational"} in [@garoufalidis-costin; @garoufalidis-geronimo] and [@zagHans], and can therefore check that the numerically determined values are the true ones (see also [@zagMod] for a generalization of this analysis). In the case of ${\bf 5_2}$, such an analysis has not been done, and the numerical interpolation method is therefore needed. If we try to do this directly using eq. [\[Jones52\]](#Jones52){reference-type="eqref" reference="Jones52"}, the process is very time-consuming because, unlike the figure-8 case, there are now O($N^2$) terms. To get around this difficulty, we use the formula $$\label{idA}
\sum_{k=0}^m\frac{q^{(m+1)k}}{(q)_k}=(q)_m\,\sum_{k=0}^m\frac{q^{k^2}}{(q)_k^2}\,,$$ which is proved by observing that both sides vanish for $m=-1$ and satisfy the recursion $t_m=(1-q^m)t_{m-1}\,+\,q^{m^2}/(q)_m\,$. This proof gives a way to successively compute each $t_m$ in $\,\text O(1)\,$ steps (compute $y=q^m$ as $q$ times the previous $y$, $(q)_m$ as $1-y$ times its previous value, and then $t_m$ by the recursion) and hence to compute the whole sum in [\[Jones52\]](#Jones52){reference-type="eqref" reference="Jones52"} in only $\,\text O(N)\,$ steps. A short PARI program for this is

=cmr10 scaled

` `$\{$`f(x) = q=exp(2*Pi*I*x);y=1;p=1;s=1;t=1; `$\qquad$` for(n=1,denom(x)-1,y*=q;p*=1-y;t+=y.̂2ptn/p.̂2pt2;s+=p.̂2pt2*conj(p*t)); s`$\}$` `

 

and is very much faster than the computation based on the original formula. For instance, to compute ${\cal J}({\bf 5_2};N)$ to 200 digits for $N=100$ and $N=1000$ using [\[Jones52\]](#Jones52){reference-type="eqref" reference="Jones52"} takes 1.6 seconds and 262 seconds, respectively, whereas with the improved algorithm these times are reduced to 0.03 seconds and 0.4 seconds. The interpolation method can therefore be carried out to just as high precision as in the figure-8 case.

The results are as follows. The first coefficient is given to high precision by $$s_0=-\frac3{2\pi}\,\bigl(\text{Li}_2(\alpha)+\frac12\log(\alpha)\log(1-\alpha)\bigr)\,+\,\frac{\pi}3\,,$$ in accordance with the prediction [\[VolConj\]](#VolConj){reference-type="eqref" reference="VolConj"}, where $\,\alpha=0.87743\cdots - 0.74486\dots i\;$ is the root of $$\alpha^3-\alpha^2+1=0$$ with negative imaginary part. The next four values are (again numerically to very high precision) $$s_1=\frac14\,\log\frac{1+3\alpha}{23}\,,\qquad s_2=\frac{198\alpha^2+1452\alpha-1999}{24\cdot23^2},$$ $$s_3=\frac{465\alpha^2-465\alpha+54}{2\cdot23^3}\,,\qquad s_4=\frac{-2103302\alpha^2+55115\alpha+5481271}{240\cdot23^5}\,,$$ in accordance with the arithmeticity conjecture since $\mathbb K=\mathbb Q(\alpha)$ in this case.

These coefficients are already quite complicated, and the next values even more so. We can simplify them by making the rescaling $$s_n'=s_n\,\lambda^{n-1}$$ (*i.e.*, by expanding in powers of $2\pi i/\lambda N$ instead of $2\pi i/N$), where $$\lambda=\alpha^5(3\alpha-2)^3=\alpha^{-1}(\alpha^2-3)^3\,.$$ (This number is a generator of $\mathfrak p^3$, where $\mathfrak p =(3\alpha-2)=(\alpha^2-3)$ is the unique ramified prime ideal of $\mathbb K$, of norm 23.) We then find $$\begin{aligned}
s_2' &=& -\tfrac1{24}\,\bigl(12\,\alpha^2-19\,\alpha+86\bigr),   \\
 s_3' &=&  - \tfrac32\,\bigl(2\,\alpha^2+5\,\alpha-4\bigr),     \\
 s_4' &=&   \tfrac1{240}\,\bigl(494\,\alpha^2+12431\,\alpha+1926\bigr),     \\
 s_5' &=&   -\tfrac18\,\bigl(577\,\alpha^2-842\,\alpha+1497\bigr),     \\
 s_6' &=&  \tfrac1{10080}\,\bigl(176530333\,\alpha^2-80229954\,\alpha-18058879\bigr),      \\
 s_7' &=&  -  \tfrac1{240}\,\bigl(99281740\,\alpha^2+40494555\,\alpha+63284429\bigr), \\
 s_8' &=&  -\tfrac1{403200}\,\bigl(3270153377244\,\alpha^2-4926985303821\,\alpha-8792961648103\bigr), \\
 s_9' &=&   \tfrac1{13440}\,\bigl(9875382391800\,\alpha^2 - 939631794912\,\alpha- 7973863388897\bigr), \\
 s_{10}' &=&  - \tfrac1{15966720}\,\bigl(188477928956464660\,\alpha^2+213430022592301436\,\alpha+61086306651454303\bigr), \\
 s_{11}' &=& -\tfrac1{1209600}\,\bigl(517421716298434577\,\alpha^2-286061854126193276\,\alpha-701171308042539352\bigr),  
\end{aligned}$$ with much simpler coefficients than before, and with each denominator dividing $(n+2)!\,$. These highly nontrivial numbers give a strong experimental confirmation of the conjecture.

We observe that in both examples treated the first statement of the conjecture [\[ArithConj\]](#ArithConj){reference-type="eqref" reference="ArithConj"} can be strengthened to $$\exp(4s_1)\;\in\;\mathbb K\,.$$ It would be interesting to know if the same statement holds for all hyperbolic knot complements (or even all hyperbolic 3-manifolds). Another comment in this vein is that [\[VolConj\]](#VolConj){reference-type="eqref" reference="VolConj"} also has an arithmetic content: one knows that the right-hand side of this equation is in the image under the extended regulator map of an element in the Bloch group (or, equivalently, the third algebraic $K$-group) of the number field $\mathbb K$.

## Perturbative $SL(2,{\mathbb{C}})$ invariants for the figure-8 knot complement {#sec:figeight}

In this subsection, we explicitly calculate the perturbative $SL(2,{\mathbb{C}})$ invariants $S_n^{(\rho)}$ for the figure-8 knot complement, first via quantization of the moduli space of flat $SL(2,{\mathbb{C}})$ connections and then, independently, using the state integral model formulated in Section [\[sec:statesum\]](#sec:statesum){reference-type="ref" reference="sec:statesum"}. We find perfect agreement between the results, thus, supporting our proposal [\[statesumdef\]](#statesumdef){reference-type="eqref" reference="statesumdef"}.

Let $K$ be the figure-eight knot (shown in Figure [\[fig:knots\]](#fig:knots){reference-type="ref" reference="fig:knots"}.$a$) and let $M$ be its complement in the 3-sphere. In order to compute the perturbative invariants $S_n^{(\rho)}$ for an arbitrary $\rho:~\pi_1 (M)~\to~SL(2,{\mathbb{C}})$ we first need to review the classical geometry of $M$ in more detail and, in particular, to describe the moduli space of flat $SL(2,{\mathbb{C}})$ connections on $M$. As we already mentioned earlier, the knot group $\pi_1 (M)$ is generated by two elements, $a$ and $b$, such that $a^{-1} b a b^{-1} a = ba^{-1} ba b^{-1}$. The corresponding representation into $SL(2,{\mathbb{C}})$ is given by $$\rho (a) = \begin{pmatrix}  ~1~ & ~1~ \\ 0 & 1  \end{pmatrix}\,, \qquad
\rho (b) = \begin{pmatrix}  ~1~ & ~0~ \\ \zeta & 1  \end{pmatrix}\,,$$ where $\zeta = (-1 + \sqrt{-3})/2$ is the cube root of unity, $\zeta^3 = 1$.

The complement of the figure-eight knot can be also represented as a quotient space ${\mathbb{H}}^3/\Gamma$ [\[mquotient\]](#mquotient){reference-type="eqref" reference="mquotient"}, where the holonomy group $\Gamma$ is generated by the above two matrices. Specifically, we have $$\Gamma \cong PSL (2, {\cal O}_{\mathbb{K}})\,,$$ where ${\cal O}_{\mathbb{K}}$ is the ring of integers in the imaginary quadratic field $\mathbb{K} = \mathbb{Q} (\sqrt{-3})$.

The fundamental domain, ${\cal F}$, for $\Gamma$ is described by a geodesic pyramid in ${\mathbb{H}}^3$ with one vertex at infinity and the other four vertices at the points: $$\begin{aligned}
v_1 & = j \nonumber \\
v_2 & = \frac{1}{2} - \frac{\sqrt{3}}{6} i + \sqrt{\frac{2}{3}} j \\
v_3 & = \frac{1}{2} + \frac{\sqrt{3}}{6} i + \sqrt{\frac{2}{3}} j \nonumber \\
v_4 & = \frac{1}{\sqrt{3}} i + \sqrt{\frac{2}{3}} j\,. \nonumber
\end{aligned}$$ Explicitly, we have $${\cal F}= \{ z + x_3 j \in {\mathbb{H}}^3 ~\vert~ z \in {\cal F}_z, ~x_3^2 + |z|^2 \ge 1 \}\,,$$ where $z = x_1 + i x_2$ and $$\begin{aligned}
{\cal F}_z & = \{ z \in {\mathbb{C}}~\vert~ 0 \le {\rm Re}\,(z),~
\frac{1}{\sqrt{3}} {\rm Re}\,(z) \le {\rm Im}\,(z),~
{\rm Im}\,(z) \le \frac{1}{\sqrt{3}} (1 - {\rm Re}\,(z)) \} \nonumber \\
& \cup \{ z \in {\mathbb{C}}~\vert~ 0 \le {\rm Re}\,(z) \le \frac{1}{2},~
- \frac{1}{\sqrt{3}} {\rm Re}\,(z) \le {\rm Im}\,(z) \le \frac{1}{\sqrt{3}} {\rm Re}\,(z) \}
\end{aligned}$$ is the fundamental domain of a 2-torus with modular parameter $\tau = \zeta$. The region of large values of $x_3$ in ${\cal F}$ corresponds to the region near the cusp of the figure-eight knot complement $M$.

The standard triangulation of the figure eight knot complement comprises two ideal tetrahedra of opposite simplicial orientations, as in Figure [\[fig:tetr_momenta\]](#fig:tetr_momenta){reference-type="ref" reference="fig:tetr_momenta"}, glued together in the only nontrivial consistent manner possible, $$M = \Delta_z \cup \Delta_w\,.
\label{figeighttriang}$$ Here, $z$ and $w$ are complex numbers, representing the shapes of the ideal tetrahedra; we take $\Delta_z$ to be positively oriented and $\Delta_w$ to be negatively oriented. As explained in Section [\[sec:ideal\]](#sec:ideal){reference-type="ref" reference="sec:ideal"}, the shape parameters $z$ and $w$ must obey consistency relations, which in the case of the figure-eight knot reduce to a single algebraic relation (see *e.g.* Chapter 4 of [@thurston-1980] and Section 15 of [@neumann-2004]): $$(z-1)(w-1)=z^2w^2 \,.
\label{figeightgluing}$$ The shape parameters $z$ and $w$ are related to the $SL(2,{\mathbb{C}})$ holonomy eigenvalue, $l$, along the longitude[^2] of the knot in the following way $$\frac{z^2}{z-1} = -l\,, \qquad \frac{w^2}{w-1} = - l^{-1}\,,
\label{lholviashape}$$ which automatically solves the consistency condition [\[figeightgluing\]](#figeightgluing){reference-type="eqref" reference="figeightgluing"}. Similarly, the holonomy eigenvalue $m=e^u$ around the noncontractible meridian of the torus is given by

$$z w =m^2. \label{mholviashape}$$

Given the decomposition [\[figeighttriang\]](#figeighttriang){reference-type="eqref" reference="figeighttriang"} of the 3-manifold $M$ into two tetrahedra, we can find its volume by adding the (signed) volumes of $\Delta_z$ and $\Delta_w$, $${\mbox{Vol\,}}(M;u) = {\mbox{Vol\,}}(\Delta_z) - {\mbox{Vol\,}}(\Delta_w) = D(z)-D(w)\,,\label{figeightvol}$$ where the volume of an ideal tetrahedron is given by [\[volviad\]](#volviad){reference-type="eqref" reference="volviad"}. Similarly, following the prescription in Section [\[sec:ideal\]](#sec:ideal){reference-type="ref" reference="sec:ideal"}, the complexified volume can be given by[^3]

$$i({\mbox{Vol\,}}(M;u)+i{\rm CS}(M;u)) = L(z;0,0)-L(w;0,0)-v\bar{u}-i\pi u\,. \label{figeightcvol}$$

Notice that due to the consistency relation [\[figeightgluing\]](#figeightgluing){reference-type="eqref" reference="figeightgluing"} the total volumes [\[figeightvol\]](#figeightvol){reference-type="eqref" reference="figeightvol"}, [\[figeightcvol\]](#figeightcvol){reference-type="eqref" reference="figeightcvol"} are functions of one complex parameter, or, equivalently, a point on the zero locus of the A-polynomial, $A(l,m)=A(-e^v,e^u)=0$.

The classical A-polynomial of the figure-eight knot is $$A(l,m) = (l-1)(m^4 - (1-m^2-2m^4-m^6+m^8)l+m^4l^2)\,.$$ Observe that $A(l^{-1},m^{-1})\sim A(l,m)$ and that $A(l^{-1},m) \sim A(l,m)$, the latter reflecting the fact that the figure-eight knot is amphicheiral. The zero locus of this A-polynomial has three branches: the abelian branch $l_{{\rm abel}} = 1$ (or $v_{{\rm abel}} = -i\pi$) from the first factor, and two other branches from the second, given explicitly by $$l_{{\rm geom,conj}} (m) = \frac{1-m^{2}-2m^4-m^6+m^8}{2m^4}\pm \frac{1-m^4}{2m^2}\Delta(m)$$ or $$v_{{\rm geom,conj}} (u) = \log(-l_{{\rm geom,conj}}(e^u))\,,
\label{v41}$$ where we have defined $$\Delta(m) = i\sqrt{-m^{-4}+2m^{-2}+1+2m^2-m^4}\,.
\label{def_Delta}$$ Note that $\Delta (m)$ is an analytic function of $m=e^u$ around $u=0$, as are $l(m)$ and $v(u)$. In particular, $\Delta(1)=\sqrt{-3}$ is the generator of the trace field $\mathbb{K}=\mathbb{Q}({\rm tr\,}\Gamma)$ for the figure-eight knot.

Since there are only two non-abelian branches, they must (as indicated in Section [\[sec:symmetries\]](#sec:symmetries){reference-type="ref" reference="sec:symmetries"}) be the geometric and conjugate ones. Alternatively, eliminating shape parameters from the (geometric) eqs.[\[mholviashape\]](#mholviashape){reference-type="eqref" reference="mholviashape"} and [\[lholviashape\]](#lholviashape){reference-type="eqref" reference="lholviashape"} implies precisely that the non-abelian factor of the A-polynomial vanishes. As expected for an amphicheiral knot, due to the symmetries discussed in Section [\[sec:symmetries\]](#sec:symmetries){reference-type="eqref" reference="sec:symmetries"}, $v_{{\rm geom}}(u) = -v_{{\rm conj}}(u)$. The exact labelling of branches (geometric vs. conjugate) can be verified by computing the hyperbolic volume ${\mbox{Vol\,}}(M;u)$ of the figure-eight knot complement via an ideal triangulation, as in [\[figeightcvol\]](#figeightcvol){reference-type="eqref" reference="figeightcvol"}, and comparing the result to the integral [\[S0_integral\]](#S0_integral){reference-type="eqref" reference="S0_integral"} on the geometric branch. One obtains precisely

$$\begin{aligned}
 S_0^{(\rm geom)}(u) &= \frac{i}{2}({\mbox{Vol\,}}(M;0)+i{\rm CS}(M;0)) + \int_0^u (v_{\rm geom}(u')+i\pi)du' \notag \\
 &= \frac{1}{2}\big(\text{Li}_2(z)-\text{Li}_2(w)+\frac{1}{2}\log{z}\log(1-z)-\frac{1}{2}\log(w)\log(1-w)+uv+i\pi u\big) \notag \\
 &= \frac{i}{2}({\mbox{Vol\,}}(M;u)+i{\rm CS}(M;u))+v_{\rm geom}(u){\rm Re}\,(u)+i\pi u\,, 
\end{aligned}$$

confirming [\[S0_volume\]](#S0_volume){reference-type="eqref" reference="S0_volume"}. Note that $CS(M;u)=0$ for any imaginary $u$.

From the relation [\[lholviashape\]](#lholviashape){reference-type="eqref" reference="lholviashape"} we find that the point $(l,m)=(-1,1)$ corresponding to the complete hyperbolic structure on $M$ is characterized by the values of $z$ and $w$ which solve the equation $$z^2 - z + 1 = 0\,.$$ In order to obtain tetrahedra of positive (signed) volume, we must choose $z$ to be the root of this equation with a positive imaginary part, and $w$ its inverse: $$z = \frac{1 + i \sqrt{3}}{2}\,,\qquad  w= \frac{1 - i \sqrt{3}}{2}\,.$$ These value correspond to regular ideal tetrahedra, and maximize (respectively, minimize) the Bloch-Wigner dilogarithm function $D(z)$.

[^1]: Note that in our notations $e^{2\hbar}=q=e^{2\pi i/N}$.

[^2]: A 1-cycle on $\Sigma = T^2$ which is contractible in the knot complement $M$.

[^3]: This expression differs slightly from the one given in [@neumann-2004], because we use $2v+2\pi i$ rather than $2v$ as the logarithm of the "longitudinal" holonomy, as mentioned in Footnote [\[foot:v2pi\]](#foot:v2pi){reference-type="ref" reference="foot:v2pi"} of Section [\[sec:ideal\]](#sec:ideal){reference-type="ref" reference="sec:ideal"}.
