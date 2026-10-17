---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model"
section_id: sec-008-expansion-at-the-center
section_title: "Expansion at the center"
section_number: null
pages: 15-17
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.99
doc_brief: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model — 18 sections: Front matter; Introduction; The extended Skyrme-Faddeev model"
---
To obtain a solution for the radial function $f(r)$, we assume it can be expressed as a power series expansion around the center, $r=0$: $$f(r)=\sum_{k=0}^{\infty}a_k r^k.\label{expansion-center}$$ By substituting this series into the field equation [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} and expanding the equation into a power series in $r$, we can solve for the coefficients, $a_k$. This is achieved by setting each coefficient of the resulting series to zero, which allows us to determine the unique values of the $a_k$ coefficients that satisfy the field equation. For our calculations, we will focus on the first few coefficients, $a_k$, as they determine the leading behavior of the radial function near the center. The values of these coefficients are heavily dependent on the number $l$, which determines the number of scalar fields, $N=2l+1$.

### Q-ball case: $N=1$, $(l=0)$

Unlike the $CP^N$ model, which lacks quartic terms, the ESF model yields more than one solution for the coefficients $a_k$. Upon substituting the power series expansion from Equation [\[expansion-center\]](#expansion-center){reference-type="eqref" reference="expansion-center"} into the radial equation [\[radialeq\]](#radialeq){reference-type="eqref" reference="radialeq"} and expanding the resulting expression in powers of $r$, we obtain: $$-\frac{l(l+1)}{r^2}a_0-\frac{l(l+1)-2}{r}a_1+{\cal O}(1)=0.\label{eq:expansion}$$ The singular terms, which are proportional to $r^{-2}$ and $r^{-1}$, must be eliminated to ensure a finite solution. This is achieved by an appropriate selection of the coefficients $a_0$ and $a_1$.

The first case, $l=0$, represents a direct generalization of previously studied Q-ball solutions (corresponding to the $N=1$ case). In this instance, the constraint requires that the coefficient $a_1$ vanishes ($a_1=0$), while $a_0$ remains a free constant determined by the initial conditions at the center. Consequently, the radial function $f(r)$ near the center, $r=0$, behaves like a parabola, and the second coefficient, $a_2$, is determined by the following complex expression: $$\begin{aligned}
a_2&=\frac{\left(1+a_0^2\right){}^{7/2} \tilde\mu ^2-8  \omega ^2 a_0
   \left(1-a_0^2\right) \left(1+a_0^2\right)^2-8 \kappa  \omega ^4 \left(\beta  e^2+2 \gamma  e^2\right)a_0^3 \left(1-a_0^2\right) }{48 \left(1+a_0^2\right) \Big((1+a_0^2)^2+\kappa  \omega ^2 \left(\beta 
   e^2-4\right)a_0^2\Big)}.\label{CP1_a2}
\end{aligned}$$ The terms containing the coefficient $\kappa$ explicitly represent the modifications to the central behavior that arise from the presence of quartic terms within the model's Lagrangian.

There is a second solution that exhibits a linear behavior near the origin, as determined by the coefficient $a_1$: $$a_1=\pm\sqrt{\frac{\left(1+a_0^2\right){}^2+\kappa  \omega ^2 \left(\beta  e^2-4\right)a_0^2 }{\kappa  \left(\beta  e^2+2 \gamma  e^2\right)}}\label{CP1_a1}$$ This solution is mathematically valid only when $\kappa\neq 0$ and $\beta  e^2+2 \gamma  e^2\neq 0$. This latter constraint implies that the energy density, as defined in Equation [\[H1b\]](#H1b){reference-type="eqref" reference="H1b"}, includes a term of the form $\sim\frac{3\omega^4 f^2-f'^4}{(1+f^2)^4}$ which is not guaranteed to be positive definite. It is crucial to note that the mere existence of a series expansion does not guarantee that the resulting numerical solution to the field equations will possess the desired physical properties (such as finiteness or non-negative energy). Therefore, a full numerical solution of the radial equation is required for verification.

### Q-ball case: $N=3$, $(l=1)$

For Q-balls with $l=1$ (corresponding to $N=3$), the coefficient $a_0$ must be zero, while $a_1$ is a free constant. The coefficient $a_2$ is determined by the following expression: $$a_2=\frac{\widetilde\mu ^2}{32 \Big(1+\kappa  \left(2-5 \beta  e^2-6 \gamma  e^2\right)a_1^2 \Big)}\label{CP3a2}$$ The explicit dependence of $a_2$ on $a_1$ arises exclusively from the quartic terms present in the model's Lagrangian. A detailed analysis of these specific types of solutions is presented in the forthcoming section.

### Q-shell case: $N=5,7,9,\ldots$, $(l=2,3,4,\ldots)$

Assuming $\text{sgn}(f)=+1$ and substituting the power series expansion [\[expansion-center\]](#expansion-center){reference-type="eqref" reference="expansion-center"} with the boundary conditions $a_0=a_1=0$ (consistent with $N \ge 3$ solutions) into the radial equation [\[radialeq\]](#radialeq){reference-type="eqref" reference="radialeq"}, we obtain the following expansion around $r=0$: $$\begin{aligned}
&-\Big(a_2 \left(l^2+l-6\right)+\frac{\tilde\mu ^2}{8}\Big)+(l-3)(l+4)a_3 r+\Big(\omega^2a_2+(l-4)(l+5)a_4\Big)r^2+\\
&+\Big(\omega^2a_3+(l-5)(l+6)a_5\Big)r^3+{\cal O}(r^4)=0.
\end{aligned}$$ To satisfy this equation, every coefficient must vanish. When $l=2$ (i.e., $N=5$), the constant term simplifies to $-\frac{\tilde{\mu}^2}{8}$, which cannot be canceled (since $\tilde{\mu} \ne 0$). Thus, the radial equation cannot be satisfied for $l=2$. Furthermore, for values of $l$ greater than or equal to $2$, the equation for the $r^0$ coefficient yields $a_2 = -\frac{\tilde{\mu}^2}{8(l^2+l-6)}$. Since $l^2+l-6 > 0$ for $l \ge 2$, $a_2$ must be negative. This implies that $f(r)$ would be negative in the immediate vicinity of $r=0$, which contradicts our initial assumption that $f(r) \ge 0$. Consequently, it is not possible to obtain a regular radial function as a power series near $r=0$ for $l \ge 2$, meaning the model does not possess regular Q-ball solutions for these higher field numbers.

An alternative solution structure exists by considering a vacuum core, where the field $f=0$ within the sphere $r \le R_{\text{in}}$. This leads to Q-shell solutions. The expansion near this internal radius, $R_{\text{in}}$, is essentially identical to the expansion performed near the external compacton radius, $R_{\text{out}}$, since the function is approaching zero quadratically. Therefore, we assume the series expansion: $$f(r)=c_2(r-R_{\rm in})^2+c_3(r-R_{\rm in})^3+\ldots$$ Substituting this into the field equation yields the relationship $c_k=(-1)^k b_k$, where $b_k$ are the coefficients defined previously in Equations [\[eq:b2\]](#eq:b2){reference-type="eqref" reference="eq:b2"}-[\[eq:b4\]](#eq:b4){reference-type="eqref" reference="eq:b4"}, but with $R_{\text{out}}$ formally replaced by $R_{\text{in}}$.
