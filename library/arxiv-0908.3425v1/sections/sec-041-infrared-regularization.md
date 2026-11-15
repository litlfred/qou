---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-041-infrared-regularization
section_title: "Infrared regularization"
section_number: null
pages: 60-62
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.984
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
Let us now turn to a *formal* definition of the infrared singular and regular parts for arbitrary $p^2$ [@Becher:1999he] which makes use of the Feynman parametrization of Eq. ([\[4:3:2:HPmMn\]](#4:3:2:HPmMn){reference-type="ref" reference="4:3:2:HPmMn"}). Introducing the dimensionless variables $$\label{4:3:3:alphaomegadef}
\alpha=\frac{M}{m}={\cal O}(q),\quad \Omega=\frac{p^2-m^2-M^2}{2m M}={\cal O}(q^0),$$ we rewrite $A(z)$ as $$A(z)=m^2[z^2-2\alpha\Omega z(1-z)+\alpha^2(1-z)^2]\equiv m^2 C(z),$$ so that $H$ is now given by $$\label{4:3:3:defh2}
H(p^2,m^2,M^2;n)=\kappa(m;n) \int_0^1 \mbox{d}z
[C(z)-i0^+]^{\frac{n}{2}-2},$$ where $$\label{4:3:3:kappan}
\kappa(m;n)
=\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}}m^{n-4}.$$ The infrared singularity originates from small values of $z$, where the function $C(z)$ goes to zero as $M\to 0$. In order to isolate the divergent part one scales the integration variable $z\equiv \alpha x$ so that the upper limit $z=1$ in Eq. ([\[4:3:3:defh2\]](#4:3:3:defh2){reference-type="ref" reference="4:3:3:defh2"}) corresponds to $x=1/\alpha\to
\infty$ as $M\to 0$. An integral $I$ having the same infrared singularity as $H$ is then defined which is identical to $H$ except that the upper limit is replaced by $\infty$: $$\label{4:3:3:Idef}
I\equiv\kappa(m;n)\int_0^\infty \mbox{d}z[C(z)-i0^+]^{\frac{n}{2}-2}
=\kappa(m;n) \alpha^{n-3}\int_0^\infty \mbox{d}x[D(x)-i0^+]^{\frac{n}{2}-2},$$ where $$D(x)=1-2\Omega x+x^2+2\alpha x(\Omega x-1)+\alpha^2 x^2.$$ (The pion mass $M$ is not sent to zero.) Accordingly, the regular part of $H$ is defined as $$\label{4:3:3:Rdef}
R\equiv-\kappa (m;n)\int_1^\infty \mbox{d}z [C(z)-i0^+]^{\frac{n}{2}-2},$$ so that $$\label{4:3:3:hir}
H=I+R.$$ Let us verify that the definitions of Eqs. ([\[4:3:3:Idef\]](#4:3:3:Idef){reference-type="ref" reference="4:3:3:Idef"}) and ([\[4:3:3:Rdef\]](#4:3:3:Rdef){reference-type="ref" reference="4:3:3:Rdef"}) indeed reproduce the behavior of Eq. ([\[4:3:2:defhthr\]](#4:3:2:defhthr){reference-type="ref" reference="4:3:2:defhthr"}). To that end we make use of $\Omega_{\rm thr}=1$, yielding $$\label{4:3:3:ithr1}
I_{\rm thr}=\kappa(m;n)\alpha^{n-3}\int_0^\infty \mbox{d}x
\left\{[(1+\alpha)x-1]^2-i0^+
\right\}^{\frac{n}{2}-2},$$ which converges for $n<3$. In order to continue the integral to $n>3$, write [@Becher:1999he] $$\begin{aligned}
\left\{[(1+\alpha)x-1]^2-i0^+\right\}^{\frac{n}{2}-2}=
\frac{(1+\alpha)x-1}{(1+\alpha)(n-4)}\frac{\mbox{d}}{\mbox{d}x}
\left\{[(1+\alpha)x-1]^2-i0^+\right\}^{\frac{n}{2}-2},
\end{aligned}$$ and make use of a partial integration $$\begin{aligned}
\lefteqn{\int_0^\infty \mbox{d}x
\left\{[(1+\alpha)x-1]^2-i0^+\right\}^{\frac{n}{2}-2}
=}\\
&&\left[\frac{(1+\alpha)x-1}{(1+\alpha)(n-4)}
\left\{[(1+\alpha)x-1]^2-i0^+\right\}^{\frac{n}{2}-2}
\right]_0^\infty-\frac{1}{n-4}
\int_0^\infty \mbox{d}x \left\{[(1+\alpha)x-1]^2-i0^+\right\}^{\frac{n}{2}-2}.
\end{aligned}$$ For $n<3$, the first expression vanishes at the upper limit and, at the lower limit, yields $1/[(1+\alpha)(n-4)]$. Bringing the second expression to the left-hand side, we may then continue the integral analytically as $$\label{5:6:intanc}
\int_0^\infty \mbox{d}x\left\{[(1+\alpha)x-1]^2-i0^+
\right\}^{\frac{n}{2}-2}=\frac{1}{(n-3)(1+\alpha)},$$ so that we obtain for $I_{\rm thr}$ $$\label{4:3:3:ithr}
I_{\rm thr}=\kappa(m;n)\alpha^{n-3}\frac{1}{(n-3)(1+\alpha)}
=
\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}(n-3)}
\frac{M^{n-3}}{m+M},$$ which agrees with the infrared singular part $I$ of Eq. ([\[4:3:2:defhthr\]](#4:3:2:defhthr){reference-type="ref" reference="4:3:2:defhthr"}).

The threshold value of the regular part of Eq. ([\[4:3:3:Rdef\]](#4:3:3:Rdef){reference-type="ref" reference="4:3:3:Rdef"}) is obtained by analytic continuation from $n<3$ to $n>3$: $$\begin{aligned}
\label{4:3:3:Rthr}
 R_{\rm thr}&=&-\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}}
\int_1^\infty \mbox{d}z [z(m+M)-M_\pi]^{n-4}\nonumber\\
&=& -\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}}
\frac{1}{(n-3)(m+M)}(\infty^{n-3}-m^{n-3})\nonumber\\
&\stackrel{\mbox{$n<3$}}{=}&\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}(n-3)}
\frac{m^{n-3}}{m+M},
\end{aligned}$$ which is indeed the regular part $R$ of Eq. ([\[4:3:2:defhthr\]](#4:3:2:defhthr){reference-type="ref" reference="4:3:2:defhthr"}).

What distinguishes $I$ from $R$ is that, for non-integer values of $n$, the chiral expansion of $I$ gives rise to non-integer powers of ${\cal O}(q)$, whereas the regular part $R$ may be expanded in an ordinary Taylor series. For the threshold integral, this can nicely be seen by expanding $I_{\rm thr}$ and $R_{\rm thr}$ in the pion mass counting as ${\cal O}(q)$. On the other hand, it is the regular part which does not satisfy the counting rules. The basic idea of the infrared renormalization consists of replacing the general integral $H$ of Eq. ([\[4:3:2:HPmMn\]](#4:3:2:HPmMn){reference-type="ref" reference="4:3:2:HPmMn"}) by its infrared singular part $I$, defined in Eq. ([\[4:3:3:Idef\]](#4:3:3:Idef){reference-type="ref" reference="4:3:3:Idef"}), and dropping the regular part $R$, defined in Eq. ([\[4:3:3:Rdef\]](#4:3:3:Rdef){reference-type="ref" reference="4:3:3:Rdef"}). In the low-energy region $H$ and $I$ have the same analytic properties whereas the contribution of $R$, which is of the type of an infinite series in the momenta, can be included by adjusting the coefficients of the most general effective Lagrangian. This is the infrared renormalization condition.

As discussed in detail in Ref. [@Becher:1999he], the method can be generalized to an arbitrary one-loop graph (see also Ref. [@Semke:2005sn]). It is first argued that tensor integrals involving an expression of the type $k^{\mu_1}\cdots k^{\mu_2}$ in the numerator may always be reduced to scalar loop integrals of the form $$-i\int\frac{\mbox{d}^n k}{(2\pi)^n}\frac{1}{a_1\cdots a_m}\frac{1}{b_1\cdots b_n},$$ where $a_i=(q_i+k)^2-M^2+i0^+$ and $b_i=(p_i-k)^2-m^2+i0^+$ are inverse meson and nucleon propagators, respectively. Here, the $q_i$ refer to four-momenta of ${\cal O}(q)$ and the $p_i$ are four-momenta which are not far off the nucleon mass shell, i.e., $p_i^2=m^2+{\cal O}(q)$. Using the Feynman parametrization, all pion propagators and all nucleon propagators are separately combined, and the result is written in such a way that it is obtained by applying $(m-1)$ and $(n-1)$ partial derivatives with respect to $M^2$ and $m^2$, respectively, to a master formula. A simple illustration is given by $$\frac{1}{a_1 a_2}=\int_0^1 \mbox{d}z \frac{1}{[a_1 z+a_2(1-z)]^2}
=\frac{\partial}{\partial M^2}\int_0^1 \mbox{d}z \frac{1}{a_1 z+a_2 (1-z)},$$ where $a_i=(q_i+k)^2-M^2+i0^+$. Of course, the expressions become more complicated for larger numbers of propagators. The relevant property of the above procedure is that the result of combining the meson propagators is of the type $1/A$ with $A=(k+q)^2-M^2+i0^+$, where $q$ is a linear combination of the $m$ momenta $q_i$, with an analogous expression $1/B$ for the nucleon propagators. Finally, the expression $$-i\int\frac{\mbox{d}^n k}{(2\pi)^n}\frac{1}{AB}$$ may then be treated in complete analogy to $H$ of Eq. ([\[4:3:2:Hdef\]](#4:3:2:Hdef){reference-type="ref" reference="4:3:2:Hdef"}), i.e., the denominators are combined as in Eq. ([\[4:3:2:feynmanparh\]](#4:3:2:feynmanparh){reference-type="ref" reference="4:3:2:feynmanparh"}), and the infrared singular and regular pieces are identified by writing $\int_0^1 \mbox{d}z\cdots
= \int_0^\infty \mbox{d}z \cdots-\int_1^\infty \mbox{d}z \cdots$.
