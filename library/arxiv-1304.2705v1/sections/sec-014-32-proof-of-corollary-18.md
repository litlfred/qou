---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-014-32-proof-of-corollary-18
section_title: "Proof of Corollary 1.8"
section_number: 3.2
pages: 14-15
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.867
latex_coverage_ratio: 0.824
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integrals of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topology can be written"
---
\lbl{sub.cor52}

Assume now that $(A,B)=(2,3)$. Then,
\begin{align*}
\frac{1}{(b(1-e^{b^{-1}w}))^3} &= -\frac{1}{w^3} +\frac{3b^{-1}}{2w^2} 
-\frac{b^{-2}}{w} 
+O(1)
\\
\left( \phi_m(b w) \right)^3 &=
1-3 E^{(m)}_1(q) \, b w + \frac{3}{2} \left(3 E^{(m)2}_1(q) -
E^{(m)}_2(q)\right) \, b^2 w^2 + O(w^3) \\
(\ti \phi_n(b^{-1} w))^3 &= 
1+3 \ti E^{(n)}_1(\tq) \, b^{-1} w
+ \frac{3}{2} \left(3 \ti E^{(n)2}_1(\tq) +
\ti E^{(n)}_2(\tq)\right) \, b^{-2} w^2 + O(w^3)
\\
e^{\frac{2}{4 \pi i} w^2 + 2 w (b (m+1/2) + b^{-1} (n+1/2))} &=
1+\left((1+2m)b  +(1 + 2 n) b^{-1}\right) w + \\
& \left(1 + \frac{b^2+b^{-2}}{2} +\frac{1}{2 \pi i} + 2 b^2 m^2 + 2 b^{-2} n^2
+ 4 m n \right. \\
& \left. + 2(1+b^2) m + 2(1+b^{-2}) n \right) w^2 + O(w^3) 
\end{align*}
If $R=\Res_{w=0}(F_{2,3,m,n}(w))$, then
{\small
\begin{align*}
R_{m,n} &= -\frac{b^2}{2} \left(
1 + 4 m + 4 m^2   - 6 E^{(m)}_1(q) - 12 m  E^{(m)}_1(q) + 9 E^{(m)2}_1(q) - 3 
E^{(m)}_2(q) \right)
\\
& - \frac{1}{2 \pi i} +  \frac{1}{2}
\left(1 + 2 m - 3 E^{(m)}_1(q)\right)\left(1 + 2 n -6 E^{(n)}_1(\tq)\right) 
\\
& + \frac{b^{-2}}{2} \left( - n - n^2 -6 E^{(0)}_2(\tq) + 3 E^{(n)}_1(\tq) 
+6 n E^{(n)}_1(\tq) - 9 E^{(n)2}_1(\tq) + 3 E^{(n)}_2(\tq) \right) \,,
\end{align*}
}
This proves part (a) of Corollary \ref{cor.52}. Part (b) follows from
Equation \eqref{eq.FABrec} for $(A,B)=(2,3)$ and $(A,B)=(1,3)$.
Note that Theorem \ref{thm.1} states that
\begin{align}
\lbl{eq.52R}
\calI_{2,3}(q)& = 
-e^{\frac{3 \pi i}{4}} \la P_{2,3} (F \ti F) \ra
\end{align}
where 
\begin{align*}
P_{2,3} &= -\frac{b^2}{2} 
\left( 
1+4 \d+4 \d^2-6 \d_1-12 \d \d_1+9 \d_1^2-3 \ti\d_2
\right)
\\
& + \frac{1}{2} 
\left( 
1+2 \d+\frac{i}{\pi} +2 \ti\d+4 \d \ti\d-3 \d_1-6 \ti\d \d_1
-6 e_2(\tq)-6 \ti\d_1-12 \d \ti\d_1+18 \d_1 \ti\d_1
\right)
\\
& + \frac{b^{-2}}{2}
\left( 
-\ti\d-\ti\d^2+3 \ti\d_1+6 \ti\d \ti\d_1-9 \ti\d_1^2+3 \ti\d_2
\right) \,.
\end{align*}
