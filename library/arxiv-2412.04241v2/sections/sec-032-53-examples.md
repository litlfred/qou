---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-032-53-examples
section_title: "Examples"
section_number: 5.3
pages: 65-68
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.951
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.examples2}

We now explore how the approach described in last two subsections works for some
different ground rings. We will illustrate how one can test whether a Galois
invariant function near roots of unity is actually an element of a Habiro ring.

\begin{example}
Recall the Kashaev invariant of the trefoil from equation~\eqref{eq:KZ}
(often called the Kontsevich-Zagier series). We can compute the first few terms
in the expansions at $\z_1,\z_2,\z_3,\z_4$ (with $q=\z_m(1-u)$)
\be
\begin{aligned}
F_{3_1,1}(u)
&\=
1 + u + 2u^2 + 5u^3+\mathrm{O}(u^4)\,,\\
F_{3_1,2}(u)
&\=
3 + 11u+\mathrm{O}(u^2)\,,\\
F_{3_1,3}(u)
&\=
5-\z_3+\mathrm{O}(u)\,,\\
F_{3_1,4}(u)
&\=
8-3\z_4+\mathrm{O}(u)\,.
\end{aligned}
\ee
These give rise to the vector
\be
\begin{small}
\begin{aligned}
&(&\gamma_{1,1,0}&\;|&
\gamma_{2,1,0}&\;&
\gamma_{1,2,0}&\;|&
\gamma_{3,1,0}&\;&
\gamma_{3,1,1}&\;&
\gamma_{1,3,0}&\;|&
\gamma_{4,1,0}&\;&
\gamma_{4,1,1}&\;&
\gamma_{2,2,0}&\;&
\gamma_{1,4,0}\;&)\,\phantom{,,_{2_{2_{2_{2_{2}}}}}}\\
\=\;&(&1 &\;|& 3 &\;& 1 &\;|& 5 &\;& -1 &\;& 2 &\;|
& 8 &\;& -3 &\;& 11 &\;& 5\;&)\,,\phantom{,_{2_{2_{2_{2_{2}}}}}}
\end{aligned}
\end{small}
\ee
which when multiplied by $\bM_5^{-1}$ gives the expected
\be
\begin{small}
\begin{aligned}
&(&a_{1,0}&\;|&
a_{2,0}&\;&
a_{2,1}&\;|&
a_{3,0}&\;&
a_{3,1}&\;&
a_{3,2}&\;|&
a_{4,0}&\;&
a_{4,1}&\;&
a_{4,2}&\;&
a_{4,3}&)\,\phantom{.,_{2_{2_{2_{2_{2}}}}}}\\
\=&(&1 &\;|& 1 &\;& 0 &\;|& 1 &\;& 0 &\;& 0 &\;|
& 1 &\;& 0 &\;& 0 &\;& 0&)\,.\phantom{,_{2_{2_{2_{2_{2}}}}}}
\end{aligned}
\end{small}
\ee
To see just how delicate the property of being in the Habiro ring is, notice
that simply changing the number $\gamma_{1,1,0}$ from $1$ to $2$ by would give
the sequence
\be
\begin{small}
\begin{aligned}
&\Big(\!\!\!\!&2 \;&\;\Big|& \frac{3}{4} &\;
& \frac{1}{4}\; &\;\Big|& \frac{65}{72} &\;& \frac{-1}{72}
&\;& \frac{17}{72}\; &\;\Big|& \frac{275}{288} &\;& \frac{-7}{144} &\;& \frac{1}{32}
&\;& \frac{17}{72}\;&\Big)\,,
\end{aligned}
\end{small}
\ee
where the integrality has been completely ruined.
\end{example}

\begin{example}
In this example we will see what the introduction of denominators does to the
Habiro ring. The Habiro function $F(q)\in\HH_\BQ$ whose image under $\iota$ is the
collection of (constant) power series
\be
F(\z_m(1-u)) \=
\bigg\{
\begin{array}{cl}
1 & \text{if }m\text{ is odd}\,,\\
0 & \text{if }m\text{ is even}\,
\end{array}
\ee
does not belong to $\HH_{\BZ}$, but is an element of $\HH_{\BZ[1/2]}$. Indeed, it
can be written
\be
F(q)\=1
+\frac{1}{4}(-1+q)\,(q;q)_1
+\frac{1}{8}(1-q+q^2)\,(q;q)_2
+\frac{1}{32}(-5+2q+q^2+4q^3)\,(q;q)_3+\cdots\,.
\ee
Similarly, the element $G(q)=F(q^2)-F(q)$, whose image under $\iota$ is the
collection of (constant) power series
\be
G(\z_m(1-u)) \=
\bigg\{
\begin{array}{cl}
1 & \text{if }m\;\equiv\;2\pmod{4}\\
0 & \text{otherwise}\,,
\end{array}
\ee
is also an element of $\HH_{\BZ[1/2]}$, and can be written
\be
G(q) \=
\frac{1}{4}(1-q)\,(q;q)_1
+\frac{1}{8}(-1+q-q^2)\,(q;q)_2
+\frac{1}{32}(1-2q+3q^2-4q^3)\,(q;q)_3+\cdots\,.
\ee
\end{example}

\begin{example}
Our final example is an element of the Habiro ring of the ring of integers,
with $1/23$ adjoined, of the field
$\mathbb{K}=\BQ(\alpha)/(\alpha^3-\alpha^2+1)$, the cubic field of discriminant
$-23$, associated to the Kashaev invariant of the knot $5_2$.
We define a collection of series $(\Psi_{5_2,m})_{m\geq1}$ using the residue formulas
given in Section~\ref{sub.sym}. Specifically, we define
\be
\Psi_{5_2,m}(u)
\;:=\;
\Res{w^m=z}J_{5_2}(1,w,\z_m(1-u))\frac{dw}{w}\,,
\ee
where
\be
J_{5_2}(t,w,q)
\;:=\;
\sum_{k=0}^{\infty}
\frac{q^{k(k+1)}\thinspace w^{2k}}{(qw;q)_{k}^3}t^k
\ee
and set $z=1-\alpha^2$ so that $z^2(1-z)^{-3}=1$.
The collection $\Psi_{5_2,m}$ is related to the symmetrised series
$\Phitof^{(5_2)}(q)\thinspace\Phitof^{(5_2)}(q^{-1})$ discussed in
Section~\ref{sub.52-237}. For example, equation~\eqref{eq:52sym} is equal to
$(3\alpha-2)\Psi_{5_2,1}(-x)$.
One can compute the first few coordinates via the expansions
\be
\begin{aligned}
\Psi_{5_2,1}(u)
&\=
\frac{1}{23}(-9\alpha^2 + 3\alpha + 2)
+ \frac{1}{23^4}(444\alpha^2 + 3417\alpha - 1287)u^2\\
&\qquad\qquad + \frac{1}{23^4}(444\alpha^2 + 3417\alpha - 1287)u^3
+ \mathrm{O}(u^4)\,,\\
\Psi_{5_2,2}(u)
&\=\frac{1}{23}(-43\alpha^2 + 22\alpha + 7) + \mathrm{O}(u^2)\,,\\
\Psi_{5_2,3}(u)
&\=\frac{1}{23}(-111\alpha^2 + 60\alpha + 17) + \mathrm{O}(u)\,,\\
\Psi_{5_2,4}(u)
&\=\frac{1}{23}(-242\alpha^2 + 119\alpha + 41) + \mathrm{O}(u)\,,
\end{aligned}
\ee
giving rise to the vector
\be
\left(
\begin{array}{c}
\gamma_{1,1,0}\\
\hline
\gamma_{2,1,0}\\
\gamma_{1,2,0}\\
\hline
\gamma_{3,1,0}\\
\gamma_{3,1,1}\\
\gamma_{1,3,0}\\
\hline
\gamma_{4,1,0}\\
\gamma_{4,1,1}\\
\gamma_{2,2,0}\\
\gamma_{1,4,0}\\
\end{array}
\right)
\=
\left(
\begin{array}{c}
  {}_{\phantom{2_{2_{2_{2_2}}}}}\tfrac{1}{23}(-9\alpha^2 + 3\alpha
  + 2)_{\phantom{2_{2_{2_{2_2}}}}} \\
 \hline
 {}^{\phantom{2^{2^2}}}\tfrac{1}{23}(-43\alpha^2 + 22\alpha
 + 7)^{\phantom{2^{2^2}}}\\
 0 \\
 \hline
 {}^{\phantom{2^{2^2}}}\tfrac{1}{23}(-111\alpha^2 + 60\alpha
 + 17)^{\phantom{2^{2^2}}}\\
 0\\
 {}_{\phantom{2_{2_{2_{2_2}}}}}\tfrac{1}{23^4}(444\alpha^2 + 3417\alpha
 - 1287)_{\phantom{2_{2_{2_{2_2}}}}} \\
 \hline
 {}^{\phantom{2^{2^2}}}\tfrac{1}{23}(-242\alpha^2
 + 119\alpha + 41)^{\phantom{2^{2^2}}}\\
 0\\
 0\\
 \tfrac{1}{23^4}(444\alpha^2 + 3417\alpha - 1287)
\end{array}
\right)\,.
\ee
(That the coordinates here are in $\BK$ as opposed to $\BK[\z_m]$ is because
$\phi(m)\leq 2$ for $m<5$ and $\Psi_{5_2}$ is a symmetrisation; in general, the
coordinates are in $\BK[\z_m+\z_m^{-1}]$.)
This vector when multiplied by $\bM_{5}^{-1}$ gives the vector
\be
\renewcommand\arraystretch{1.3}
\left(
\begin{array}{c}
  {}_{\phantom{2_{2_{2_{2_2}}}}}\tfrac{1}{23}(-9\alpha^2
  + 3\alpha + 2){}_{\phantom{2_{2_{2_{2_2}}}}}\\
 \hline
 \tfrac{1}{92}(-34\alpha^2 + 19\alpha + 5)\\
 {}_{\phantom{2_{2_{2_{2_2}}}}}\tfrac{1}{92}(34\alpha^2
 - 19\alpha - 5){}_{\phantom{2_{2_{2_{2_2}}}}}\\
 \hline
 \tfrac{1}{6716184}(-5376038\alpha^2 + 3018917\alpha + 785707)\\
 \tfrac{1}{6716184}(2070166\alpha^2 - 1142197\alpha - 309323)\\
 {}_{\phantom{2_{2_{2_{2_2}}}}}\tfrac{1}{6716184}(4552234\alpha^2
 - 2529235\alpha - 674333){}_{\phantom{2_{2_{2_{2_2}}}}} \\
 \hline
 \tfrac{1}{26864736}(-22020494\alpha^2 + 10246115\alpha + 3924793)\\
 \tfrac{1}{13432368}(-5376038\alpha^2 + 3018917\alpha + 785707)\\
 \tfrac{1}{8954912}(10100386\alpha^2 - 4938301\alpha - 1720695)\\
 \tfrac{1}{6716184}(4552234\alpha^2 - 2529235\alpha - 674333)
\end{array}
\right)\,,
\ee
which has denominator $26864736=2^5\cdot3\cdot23^4$. If we instead apply the
correct Frobenius automorphism and then multiply by $\bM_{5}^{-1}$ we find
\be
\begin{aligned}
\left(
\begin{array}{c}
\gamma_{1,1,0}\\
\hline
\varphi_2(\gamma_{2,1,0})\\
\gamma_{1,2,0}\\
\hline
\varphi_3(\gamma_{3,1,0})\\
\varphi_3(\gamma_{3,1,1})\\
\gamma_{1,3,0}\\
\hline
\varphi_4(\gamma_{4,1,0})\\
\varphi_4(\gamma_{4,1,1})\\
\varphi_2(\gamma_{2,2,0})\\
\gamma_{1,4,0}\\
\end{array}
\right)
&\=
\frac{1}{23^4}\left(
\begin{array}{c}
 225\alpha^2 + 213\alpha + 142\\
 241\alpha^2 + 113\alpha + 74\\
 0\\
 279\alpha^2 + 132\alpha + 151\\
 0\\
 156\alpha^2 + 249\alpha + 153\\
 161\alpha^2 + 115\alpha + 4\\
 0\\
 0\\
 156\alpha^2 + 249\alpha + 153
\end{array}
\right)\pmod{288}\,,\\
\left(
\begin{array}{c}
a_{1,0}\\
\hline
a_{2,0}\\
a_{2,1}\\
\hline
a_{3,0}\\
a_{3,1}\\
a_{3,2}\\
\hline
a_{4,0}\\
a_{4,1}\\
a_{4,2}\\
a_{4,3}\\
\end{array}
\right)
&\=
\frac{1}{23^4}
\left(
\begin{array}{c}
 225\alpha^2 + 213\alpha + 142\pmod{288}\\
 4\alpha^2 + 47\alpha + 55\pmod{72}\\
 68\alpha^2 + 25\alpha + 17\pmod{72}\\
 0\pmod{4}\\
 2\alpha^2 + 2\alpha \pmod{4}\\
 2\alpha^2 + 3\alpha + 1\pmod{4}\\
 0\pmod{1}\\
 0\pmod{1}\\
 0\pmod{1}\\
 0\pmod{1}
\end{array}
\right)\,,
\end{aligned}
\ee
where now everything is integral away from the prime $23$.
\end{example}
