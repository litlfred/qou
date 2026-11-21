---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-012-the-figure-eight-knot
section_title: "The figure-eight knot"
section_number: null
pages: 23-26
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.981
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: 41 label="sec: 41"} The state integral of the figure-eight knot $\chi_{{\bf{4}}_1}(u;\hbar)$ can be expressed explicitly as [@bdp; @dimofte-levelk; @ggm2]

$$\label{chi41}
 \begin{aligned}
 \chi_{{\bf{4}}_1}(u;\hbar)={\rm e}^{-\frac{\pi{\rm i}}{12}-\frac{2\pi{\rm i}}{3}c_{\mathsf{b}}^2} \Big(
    &{\rm e}^{\pi{\rm i}(-2u^2-4c_{\mathsf{b}}u)}
     {\cal J}({\rm e}^{4\pi{\mathsf{b}}u},{\rm e}^{2\pi{\mathsf{b}}u};q)
     {\cal J}({\rm e}^{4\pi{\mathsf{b}}^{-1}u},{\rm e}^{2\pi{\mathsf{b}}^{-1} u};{\tilde{q}}^{-1})\\
     +&{\rm e}^{\pi{\rm i}(u^2-2c_{\mathsf{b}}u)}
     {\cal J}({\rm e}^{2\pi{\mathsf{b}}u},{\rm e}^{-2\pi{\mathsf{b}}u};q)
     {\cal J}({\rm e}^{2\pi{\mathsf{b}}^{-1}u},{\rm e}^{-2\pi{\mathsf{b}}^{-1} u};{\tilde{q}}^{-1})
      \Big) \, ,
\end{aligned}$$

where $c_{{\mathsf{b}}}= {\rm i}({\mathsf{b}}+ {\mathsf{b}}^{-1})/2$ and the $q$-special function ${\cal J}(x,y;q)$ is defined by[^1]

$${\cal J}(x,y;q) = (y q;q)_\infty \sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2} x^n}{(q;q)_n (y q;q)_n} \, ,$$

while $(y q;q)_\infty$ and $(y q;q)_n$ denote the quantum dilogarithm and the $q$-shifted factorial, respectively. See Appendix [\[app: faddeev\]](#app: faddeev){reference-type="ref" reference="app: faddeev"} for their definitions. By means of Eq. [\[chi41\]](#chi41){reference-type="eqref" reference="chi41"}, we can identify

$$\begin{align}
  \phi^{(\rm{geom}), \rm{WKB}}(X;q)& =  \log {\cal J}(X^2,X;q) \, , \label{phi41geom}\\
  \phi^{(\rm{conj}), \rm{WKB}}(X;q) &=  \log {\cal J}(X,X^{-1};q) \, , \label{phi41conj}
\end{align}$$ together with $C_{\rm{geom}} = C_{\rm{conj}} = {\rm e}^{\frac{\pi{\rm i}}{4}}$ and $$\begin{align}
  {{\rm i}s^{(\rm{geom})}_0(x) \over \hbar} + s^{(\rm{geom})}_1(x) + {{\rm i}s^{(\rm{geom})}_0(x_D) \over \hbar_D} + s^{(\rm{geom})}_1(x_D) &= {x^2 \over{\rm i}\hbar} + {2 \pi x \over\hbar} + x + {\pi^2 {\rm i}\over 3 \hbar} + {{\rm i}\hbar \over 12} \, , \label{s01geom41}\\
  {{\rm i}s^{(\rm{conj})}_0(x) \over \hbar} + s^{(\rm{conj})}_1(x) + {{\rm i}s^{(\rm{conj})}_0(x_D) \over \hbar_D} + s^{(\rm{conj})}_1(x_D) &=  {{\rm i}x^2 \over 2 \hbar} + { \pi x \over\hbar} + {x \over 2} + {\pi^2 {\rm i}\over 3 \hbar} + {{\rm i}\hbar \over 12} \, . \label{s01conj41}
\end{align}$$ Indeed, the two terms in the RHS of Eq. [\[chi41\]](#chi41){reference-type="eqref" reference="chi41"} represent the contributions coming from the geometric and conjugate branches, respectively. These are the only two non-abelian branches of the $\bm{4}_1$-knot, as described in Example [\[41example\]](#41example){reference-type="ref" reference="41example"}. Moreover, we solve Eqs. [\[s01geom41\]](#s01geom41){reference-type="eqref" reference="s01geom41"}, [\[s01conj41\]](#s01conj41){reference-type="eqref" reference="s01conj41"} order by order in $x$ and $\hbar$ and obtain that $$\begin{align} 
  s^{(\rm{geom})}_0(x) &= \frac{\pi^2}{3} - \frac{x^2}{2} \, , \quad s^{(\rm{geom})}_1(x) = x \, , \label{s01geom41-new} \\
  s^{(\rm{conj})}_0(x) &= \frac{\pi^2}{3} + \frac{x^2}{4} \, , \quad s^{(\rm{conj})}_1(x) = \frac{x}{2} \, . \label{s01conj41-new}
\end{align}$$ In this way, we have fully determined the perturbative wave functions $\chi^{(\alpha), \rm{WKB}}(u;\hbar)$ of the figure-eight knot in the resummed form of Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}. We verify successfully that they are annihilated by the $\hat A$-operator in Eq. [\[41Ahat\]](#41Ahat){reference-type="eqref" reference="41Ahat"}, as expected.

Let us now test the conjectural integrality structure in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"} for both the geometric and the conjugate branches. Expanding the RHS of Eqs. [\[phi41geom\]](#phi41geom){reference-type="eqref" reference="phi41geom"}, [\[phi41conj\]](#phi41conj){reference-type="eqref" reference="phi41conj"} gives $$\begin{align}
  \phi^{(\rm{geom}), \rm{WKB}}(X;q)& = \sum_{k \ge 1} \frac{q^k X^k}{k(q^k-1)} + \log \left(\sum_{n \ge 0} \frac{(-1)^n q^{n(n+1)/2} X^{2n}}{\prod_{i=1}^n (1-q^i) (1-q^i X)}  \right)  \, , \label{phi41geom-exp}\\
  \phi^{(\rm{conj}), \rm{WKB}}(X;q) &=  \sum_{k \ge 1} \frac{q^k X^{-k}}{k(q^k-1)} + \log \left(\sum_{n \ge 0}  \frac{ (-1)^n q^{n(n+1)/2} X^{2n}}{\prod_{i=1}^n (1-q^i) (X-q^i)} \right)  \, . \label{phi41conj-exp}
\end{align}$$

Let us note that both terms on the RHS of Eq. [\[phi41geom-exp\]](#phi41geom-exp){reference-type="eqref" reference="phi41geom-exp"} for the geometric branch contribute with positive powers of $X$. For the conjugate branch, we note that the negative powers of $X$ arise entirely from the first term on the RHS of Eq. [\[phi41conj-exp\]](#phi41conj-exp){reference-type="eqref" reference="phi41conj-exp"}, while a factor of $q^{\sigma_{{\rm conj}, n}}$ with $$\label{sigma41}
\sigma_{{\rm conj}, n} = \left\lfloor \frac{n^2}{8} \right\rfloor \, , \quad n \in {\mathbb Z}_{>0} \, ,$$ appears in the denominator of the power series in $X$ obtained by expanding the second term. Let us stress that this negative power of $q$ arises from the factors $\prod_{i=1}^n(X-q^i)^{-1}$ in the summand inside the logarithm, and it is absent from both the $X^{-1}$-series for the conjugate branch and the $X$-series for the geometric branch.

After extracting the coefficients $a^{(\alpha)}_{\pm n}(q)$, $n \in {\mathbb Z}_{>0}$, from the series for $\phi^{(\alpha), \rm{WKB}}(X;q)$, one can obtain the functions $D_{\pm s}^{(\alpha)}(q)$, $s \in {\mathbb Z}_{>0}$, by applying the formulae in Eqs. [\[Dtilde1\]](#Dtilde1){reference-type="eqref" reference="Dtilde1"}, [\[Dtilde2\]](#Dtilde2){reference-type="eqref" reference="Dtilde2"}. It is non-trivial that the resulting functions are polynomials with integer coefficients. In particular, the first few of them are $$\begin{aligned}
D^{({\rm geom})}_1(q) &= D^{({\rm geom})}_2(q) = q \, , \quad D^{({\rm geom})}_3(q) = q^2 \, , \quad D^{({\rm geom})}_4(q)=q^3 \, , \\
D^{({\rm geom})}_5(q) &= q^3(1+q) \, , \quad D^{({\rm geom})}_6(q) = q^4 (1 + 2 q) \, , \quad D^{({\rm geom})}_7(q) = q^4 (1 + q) (1 + q + q^2) \, , 
\end{aligned}$$ for the geometric solution, and $$\begin{aligned}
D^{({\rm conj})}_1(q) &= 0 \, , \quad D^{({\rm conj})}_2(q) = D^{({\rm conj})}_3(q) = D^{({\rm conj})}_4(q)=-1 \, , \quad D^{({\rm conj})}_5(q) &= -1-q \, , \\
 D^{({\rm conj})}_6(q) &= -2-q \, , \quad D^{({\rm conj})}_7(q) = -(1 + q) (1 + q + q^2) \, ,
\end{aligned}$$ for its conjugate. Trivially, we have that $$D^{({\rm conj})}_{-1}(q) = q \, , \quad D^{({\rm conj})}_{-s}(q) = 0 \quad s \ge 2 \, .$$ We have verified the integrality structure numerically up to $s=20$. It is then straightforward to compute the integers $c_{\pm s}$, $s \in {\mathbb Z}_{>0}$, using Eqs. [\[cs-sequenceP\]](#cs-sequenceP){reference-type="eqref" reference="cs-sequenceP"}, [\[cs-sequenceM\]](#cs-sequenceM){reference-type="eqref" reference="cs-sequenceM"}, which give

$$\begin{align}
\{ c^{(\rm{geom})}_s\}_{s \in {\mathbb Z}_{>0}}&=\{ 1, 5, 10, 21, 51, 122, 295, 725, 1792, 4455, 11133, 27930,  \dots \} \, , \label{cs41geom} \\
\{ c^{(\rm{conj})}_s\}_{s \in {\mathbb Z}_{>0}}&= (-1) \{ 0, 4, 9, 20, 50, 121, 294, 724, 1791, 4454, 11132, 27929, \dots \} \, ,  \label{cs41conj}
\end{align}$$

while $c^{(\rm{conj})}_{-s} = 1$ for all $s \in {\mathbb Z}_{>0}$. We point out that the integers in Eq. [\[cs41geom\]](#cs41geom){reference-type="eqref" reference="cs41geom"} appear to match numerically the sequence[^2]

$$\label{sequence-ex}
\sum_{k=0}^{\left\lfloor s/2 \right\rfloor} \left( {s-k \choose k} + {s-k-1 \choose k-1} \right)^2 \, , \quad s \in {\mathbb Z}_{>0} \, .$$

Moreover, we remark that the above sequences of integers satisfy $$\label{cs-rel41}
c^{(\rm{geom})}_s + c^{(\rm{conj})}_s = c^{(\rm{conj})}_{-s} \, , \quad s \in {\mathbb Z}_{>0} \, .$$ The same integer constants are obtained by implementing the alternative computational method proposed in Appendix [\[app: rational2\]](#app: rational2){reference-type="ref" reference="app: rational2"}.

Let us now go back to the quantum $A$-polynomial for the $\bm{4}_1$-knot written in Eq. [\[41Ahat\]](#41Ahat){reference-type="eqref" reference="41Ahat"}. The corresponding second-order $q$-difference equation is $$\label{Ahat-41}
\hat{A}_{\bm{4}_1}(\hat{P}, \hat{X}, q) \chi^{(\alpha), \rm{WKB}}(u; \hbar) = 0 \, ,$$ where $\chi^{(\alpha), \rm{WKB}}(u; \hbar)$ is the resummed perturbative wave function in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"} associated with the branch $\alpha$. In the rational case of $q= {\rm e}^{2 \pi {\rm i}{P \over Q}}$ with $P, Q \in {\mathbb Z}_{>0}$ coprime, Eq. [\[Ahat-41\]](#Ahat-41){reference-type="eqref" reference="Ahat-41"} can be solved in closed form by directly applying the results of Section [\[sec: 2nd-order\]](#sec: 2nd-order){reference-type="ref" reference="sec: 2nd-order"}. For simplicity, let us consider the classical solution $\alpha = \rm{geom}$ and drop the label from our notation. After suitably taking into account the exponential prefactor containing the functions $s_{0,1}(x)$ in Eq. [\[s01geom41-new\]](#s01geom41-new){reference-type="eqref" reference="s01geom41-new"}, the $q$-difference equation above assumes the form in Eq. [\[Psi-eq\]](#Psi-eq){reference-type="eqref" reference="Psi-eq"} with the identifications $$\label{coeffs-qdiff}
 \begin{aligned}
 A(X)= -q^{-2} X^{-2} {X^2-1 \over q^{-1}X^2-1} \tilde{a}(X;q) \, , \quad B(X)= q^{-2}  X^{-4} {qX^2-1 \over q^{-1}X^2-1} \, ,
  \end{aligned}$$ where we have introduced the function $$\label{atilde}
 \tilde{a}(X;q) = X^2+ X^{-2} -X-X^{-1}-q-q^{-1} \, .$$ Substituting the expressions in Eq. [\[coeffs-qdiff\]](#coeffs-qdiff){reference-type="eqref" reference="coeffs-qdiff"} into Eq. [\[matrix2\]](#matrix2){reference-type="eqref" reference="matrix2"}, we compute the matrix ${\cal M}_Q(X)$ and obtain explicit formulae for $\rm{tr} {\cal M}_Q(X)$, $\det {\cal M}_Q(X)$, and $\Delta_Q(X)$. Specifically, we find that $$\label{funct-mat41}
\begin{align}
\rm{tr} {\cal M}_Q(X) &= X^{-4 Q} \left(1- X^Q - 2 X^{2 Q} - X^{3 Q} + X^{4 Q} \right) \, , \\
\det {\cal M}_Q(X) &=X^{-4 Q} \, , \\
\Delta_Q(X) &= X^{-8 Q}\left(1-X^{2 Q}\right)^2 \left(1-2 X^{Q} -X^{2 Q}-2 X^{3 Q}+X^{4 Q}\right) \, ,
\end{align}$$ and plugging these into Eq. [\[2nd-end\]](#2nd-end){reference-type="eqref" reference="2nd-end"} with a choice of plus sign to satisfy the requirement in Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"} for $\alpha=\text{geom}$, we obtain the functions $\Upsilon (X)$ and $\varphi_Q(X)$. Observe that all functions in Eq. [\[funct-mat41\]](#funct-mat41){reference-type="eqref" reference="funct-mat41"}, and thus also $\varphi_Q(X)$, depend on $X$ through $X^Q$, as expected, and we can identify $$\begin{align}
\rm{tr} {\cal M}_Q(X) &= X^{-4 Q} T(X^Q) = X^{-2 Q} \tilde{a}(X^Q; 1) \, , \\
\Delta_Q(X) &= X^{-8 Q}\left(1-X^{2 Q}\right)^2 \Delta(X^Q) = X^{-4 Q} \left(\tilde{a}(X^Q; 1)^2 - 4 \right) \, ,
\end{align}$$ where $\tilde{a}(X; q)$ is defined in Eq. [\[atilde\]](#atilde){reference-type="eqref" reference="atilde"}, while $T(X)$ and $\Delta(X)$ are the functions introduced in Eqs. [\[classicT\]](#classicT){reference-type="eqref" reference="classicT"}, [\[classicD\]](#classicD){reference-type="eqref" reference="classicD"}, respectively, which appear in the formula for the solutions to the classical $A$-polynomial of the figure-eight knot in Eq. [\[classicP\]](#classicP){reference-type="eqref" reference="classicP"}. In particular, it follows that $$\label{8varphiQ}
\varphi_Q(X)= \frac{1}{Q} \log \left(\frac{T(X^Q) + (1-X^{2 Q})\sqrt{\Delta(X^Q)}}{2 X^{4 Q}} \right) = \frac{1}{Q} \log \left(\frac{\tilde{a}(X^Q; 1) + \sqrt{\tilde{a}(X^Q; 1)^2-4}}{2 X^{2 Q}} \right) \, ,$$ which gives us another way to numerically evaluate the integer constants $c_s$, $s \in {\mathbb Z}_{>0}$ for the geometric branch, following Eq. [\[varphiQ-cs\]](#varphiQ-cs){reference-type="eqref" reference="varphiQ-cs"} for any choice of $P, Q \in {\mathbb Z}_{>0}$ coprime, in full agreement with our previous computations. In principle, one could use the formula for $\varphi_Q(X)$ with $P=Q=1$, that is, $$\label{8varphi1}
\varphi_1(X)= \log \left( {\tilde{a}(X;1) + {\sqrt{\tilde{a}(X;1)^2- 4}} \over 2 X^2} \right) \, ,$$ to derive the conjectural expression in Eq. [\[sequence-ex\]](#sequence-ex){reference-type="eqref" reference="sequence-ex"}, but we have not attempted to do so. The same formalism can be applied to the conjugate branch of the figure-eight knot, in which case the appropriate functions $s_{0,1}(x)$ are written in Eq. [\[s01conj41-new\]](#s01conj41-new){reference-type="eqref" reference="s01conj41-new"} and the sign ambiguity in Eq. [\[2nd-end\]](#2nd-end){reference-type="eqref" reference="2nd-end"} is resolved by imposing the condition in Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"} with $\alpha = \text{conj}$, which implies a choice of minus sign. Again, the corresponding computation of the integer constants $c_{\pm s}$, $s \in {\mathbb Z}_{>0}$, for the conjugate branch agrees with the results obtained above.

[^1]: ${\cal J}(x,y;q)$ is closely related to the Hahn-Exton $q$-Bessel function [@swarttouw; @swarttouw2].

[^2]: This is the entry A$132461$ in the On-Line Encyclopedia of Integer Sequences.
