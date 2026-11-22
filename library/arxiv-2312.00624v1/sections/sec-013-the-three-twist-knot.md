---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-013-the-three-twist-knot
section_title: "The three-twist knot"
section_number: null
pages: 26-29
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.987
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: 52 label="sec: 52"} The state integral of the three-twist knot $\chi_{{\bf{5}}_2}(u;\hbar)$ can be expressed explicitly as [@bdp; @dimofte-levelk; @ggm2]

$$\label{chi52}
 \begin{aligned}
 \chi_{{\bf{5}}_2}(u;\hbar)=&{\rm e}^{-\frac{\pi{\rm i}}{12}-\frac{5\pi{\rm i}}{3}c_{\mathsf{b}}^2}\Big(
    {\rm e}^{\pi{\rm i}(-2u^2-4c_{\mathsf{b}}u)}
     {\cal H}({\rm e}^{2 \pi {\mathsf{b}}u},{\rm e}^{4 \pi {\mathsf{b}}u},{\rm e}^{4 \pi {\mathsf{b}}u}, ;q)
     {\cal H}({\rm e}^{2 \pi {\mathsf{b}}^{-1} u},{\rm e}^{4 \pi {\mathsf{b}}^{-1} u},{\rm e}^{4 \pi {\mathsf{b}}^{-1} u};{\tilde{q}}^{-1})\\
      &+{\rm e}^{\pi{\rm i}(-2u^2+4c_{\mathsf{b}}u)}
     {\cal H}({\rm e}^{-2 \pi {\mathsf{b}}u},{\rm e}^{-4 \pi {\mathsf{b}}u},{\rm e}^{-4 \pi {\mathsf{b}}u};q)
     {\cal H}({\rm e}^{-2 \pi {\mathsf{b}}^{-1} u},{\rm e}^{-4 \pi {\mathsf{b}}^{-1} u},{\rm e}^{-4 \pi {\mathsf{b}}^{-1} u};{\tilde{q}}^{-1}) \\
     &+{\cal H}({\rm e}^{2 \pi {\mathsf{b}}u},{\rm e}^{-2 \pi {\mathsf{b}}u},1;q)
     {\cal H}({\rm e}^{2 \pi {\mathsf{b}}^{-1} u},{\rm e}^{-2 \pi {\mathsf{b}}^{-1} u},1;{\tilde{q}}^{-1})
      \Big) \, ,
\end{aligned}$$

where $c_{{\mathsf{b}}}= {\rm i}({\mathsf{b}}+ {\mathsf{b}}^{-1})/2$ and the $q$-special function ${\cal H}(x,y,z;q)$ is defined by[^1]

$${\cal H}(x,y,z;q) = (x q;q)_\infty (y q;q)_\infty \sum_{n=0}^\infty \frac{q^{n(n+1)} z^n}{(q;q)_n (x q;q)_n (y q;q)_n} \, ,$$

while $(x q;q)_\infty$ and $(x q;q)_n$ denote the quantum dilogarithm and the $q$-shifted factorial, respectively. See Appendix [\[app: faddeev\]](#app: faddeev){reference-type="ref" reference="app: faddeev"} for their definitions. As for the case of the figure-eight knot in Section [\[sec: 41\]](#sec: 41){reference-type="ref" reference="sec: 41"}, using Eq. [\[chi52\]](#chi52){reference-type="eqref" reference="chi52"}, we can identify

$$\begin{align}
  \phi^{(\rm{geom}), \rm{WKB}}(X;q)& =  \log {\cal H}(X,X^2,X^2;q) \, , \label{phi52geom} \\
  \phi^{(\rm{conj}), \rm{WKB}}(X;q) &=  \log {\cal H}(X^{-1},X^{-2},X^{-2};q) \, , \label{phi52conj} \\
  \phi^{(\rm{self}), \rm{WKB}}(X;q) &=  \log {\cal H}(X,X^{-1},1;q) \, , \label{phi52self}
\end{align}$$ together with $C_{\rm{geom}} = C_{\rm{conj}} = C_{\rm{self}} = {\rm e}^{\frac{3 \pi {\rm i}}{4}}$ and $$\begin{align}
  {{\rm i}s^{(\rm{geom})}_0(x) \over \hbar}+ s^{(\rm{geom})}_1(x) + {{\rm i}s^{(\rm{geom})}_0(x_D) \over \hbar_D} + s^{(\rm{geom})}_1(x_D) 
  &= {x^2 \over{\rm i}\hbar} + {2 \pi x \over\hbar} + x +{5 \pi^2 {\rm i}\over 6 \hbar} + {5 {\rm i}\hbar \over 24} \, , \label{s01geom52}\\
  {{\rm i}s^{(\rm{conj})}_0(x) \over \hbar} + s^{(\rm{conj})}_1(x) + {{\rm i}s^{(\rm{conj})}_0(x_D) \over \hbar_D} + s^{(\rm{conj})}_1(x_D) 
  &= {x^2 \over {\rm i}\hbar} - { 2 \pi x \over\hbar}- x + {5 \pi^2 {\rm i}\over 6 \hbar} + {5 {\rm i}\hbar \over 24} \, , \label{s01conj52}\\
  {{\rm i}s^{(\rm{self})}_0(x) \over \hbar} + s^{(\rm{self})}_1(x) + {{\rm i}s^{(\rm{self})}_0(x_D) \over \hbar_D} + s^{(\rm{self})}_1(x_D) 
  &= {5 \pi^2 {\rm i}\over 6 \hbar} + {5 {\rm i}\hbar \over 24} \, .\label{s01self52}
\end{align}$$ Indeed, the three terms in the RHS of Eq. [\[chi52\]](#chi52){reference-type="eqref" reference="chi52"} capture the contributions to the exact partition function coming from the geometric, conjugate, and self-conjugate branches, respectively. These are the only three non-abelian branches of the $\bm{5}_2$-knot, as described in Example [\[52example\]](#52example){reference-type="ref" reference="52example"}. Moreover, as before, we solve Eqs. [\[s01geom52\]](#s01geom52){reference-type="eqref" reference="s01geom52"}, [\[s01conj52\]](#s01conj52){reference-type="eqref" reference="s01conj52"}, and [\[s01self52\]](#s01self52){reference-type="eqref" reference="s01self52"} order by order in $x$ and $\hbar$ and obtain that $$\begin{align}
  s^{(\rm{geom})}_0(x) &= \frac{5 \pi^2}{6} - \frac{x^2}{2} \, , \quad s^{(\rm{geom})}_1(x) = x \, , \label{s01geom52-new}\\
  s^{(\rm{conj})}_0(x) &= \frac{5 \pi^2}{6} - \frac{x^2}{2} \, , \quad s^{(\rm{conj})}_1(x) = -x \, , \label{s01conj52-new}\\
  s^{(\rm{self})}_0(x) &= \frac{5 \pi^2}{6} \, , \quad s^{(\rm{self})}_1(x) = 0 \, . \label{s01self52-new}
\end{align}$$ In this way, we have fully determined the perturbative wave functions $\chi^{(\alpha), \rm{WKB}}(u;\hbar)$ of the three-twist knot in the resummed form of Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}. As before, we verify successfully that they are annihilated by the $\hat A$-operator in Eq. [\[52Ahat\]](#52Ahat){reference-type="eqref" reference="52Ahat"}, as expected.

Let us now test the integrality conjecture in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"} for all three non-abelian branches. Expanding the RHS of Eqs. [\[phi52geom\]](#phi52geom){reference-type="eqref" reference="phi52geom"}, [\[phi52conj\]](#phi52conj){reference-type="eqref" reference="phi52conj"}, and [\[phi52self\]](#phi52self){reference-type="eqref" reference="phi52self"} gives $$\begin{align}
  \phi^{(\rm{geom}), \rm{WKB}}(X;q)& = \sum_{k \ge 1} \frac{q^k (X^k+X^{2k})}{k(q^k-1)} + \log \left(\sum_{n \ge 0} \frac{q^{n(n+1)} X^{2n}}{\prod_{i=1}^n (1-q^i) (1-q^i X)(1-q^i X^2)} \right)  \, , \label{phi52geom-exp}\\
  \phi^{(\rm{conj}), \rm{WKB}}(X;q) &=  \sum_{k \ge 1} \frac{q^k (X^{-k}+X^{-2k})}{k(q^k-1)} + \log \left(\sum_{n \ge 0} \frac{q^{n(n+1)} X^{n}}{\prod_{i=1}^n (1-q^i) (X-q^i)(X^2-q^i)} \right)  \, , \label{phi52conj-exp}\\
  \phi^{(\rm{self}), \rm{WKB}}(X;q) &=  \sum_{k \ge 1} \frac{q^k (X^k+X^{-k})}{k(q^k-1)} + \log \left(\sum_{n \ge 0} \frac{q^{n(n+1)} X^{n}}{\prod_{i=1}^n (1-q^i) (1-q^i X)(X-q^i)} \right)  \, . \label{phi52self-exp}
\end{align}$$

Both terms on the RHS of Eq. [\[phi52geom-exp\]](#phi52geom-exp){reference-type="eqref" reference="phi52geom-exp"} for the geometric branch contribute with positive powers of $X$. For the conjugate branch, we note that the negative powers of $X$ arise entirely from the first term on the RHS of Eq. [\[phi52conj-exp\]](#phi52conj-exp){reference-type="eqref" reference="phi52conj-exp"}, while a factor of $q^{\sigma_{{\rm conj}, n}}$ with $$\label{sigma52}
\sigma_{{\rm conj}, n} = \left\lfloor \frac{n^2}{4} \right\rfloor \, , \quad n \in {\mathbb Z}_{>0} \, ,$$ appears in the denominator of the power series in $X$ obtained by expanding the second term. Let us stress that this negative power of $q$ arises from the factors[^2] $\prod_{i=1}^n(X-q^i)^{-1}(X^2-q^i)^{-1}$ in the summand inside the logarithm, and it is absent from both the $X^{-1}$-series for the conjugate branch and the $X$-series for the geometric branch. Finally, in the case of the self-conjugate branch, the first term on the RHS of Eq. [\[phi52self-exp\]](#phi52self-exp){reference-type="eqref" reference="phi52self-exp"} supplies both positive and negative powers of $X$, while the second term only adds to the $X$-series after expansion. Here, a more complicated factor of $q^{\sigma_{{\rm self}, n}}$ with $$\label{sigma52self}
\sigma_{{\rm self}, n} = \left\lfloor \frac{1}{24} \left(P \left(\left\lfloor \frac{2 (n+2)}{3} 
\right\rfloor \right)^2-1 \right) \right\rfloor \, , \quad n \in {\mathbb Z}_{>0} \, ,$$ where $P(n)$ denotes the $n$-th prime number, occurs in the denominator of the power series in $X$ after summing up the contribution from the expansion of the second term on the RHS of Eq. [\[phi52self-exp\]](#phi52self-exp){reference-type="eqref" reference="phi52self-exp"}. This originates from the factors $\prod_{i=1}^n(X-q^i)^{-1}$ in the summand inside the logarithm.

As we have done for the $\bm{4}_1$-knot, after extracting the coefficients $a^{(\alpha)}_{\pm n}(q)$, $n \in {\mathbb Z}_{>0}$, from the series for $\phi^{(\alpha), \rm{WKB}}(X;q)$, we obtain the functions $D_{\pm s}^{(\alpha)}(q)$, $s \in {\mathbb Z}_{>0}$, by applying the formulae in Eqs. [\[Dtilde1\]](#Dtilde1){reference-type="eqref" reference="Dtilde1"}, [\[Dtilde2\]](#Dtilde2){reference-type="eqref" reference="Dtilde2"}. Again, these are non-trivial polynomials with integer coefficients. In particular, the first few of them are $$\begin{aligned}
D^{({\rm geom})}_1(q) &= q \, , \quad D^{({\rm geom})}_2(q) = -q(-1 + q) \, , \quad D^{({\rm geom})}_3(q) = D^{({\rm geom})}_4(q)=-q^3 \, , \\
D^{({\rm geom})}_5(q) &= q^4 (-1 + q^2) \, , \quad D^{({\rm geom})}_6(q) = q^4 (-1 + 2 q^2 + q^4) \, , \\
D^{({\rm geom})}_7(q) &= q^5 (-1 + q (1 + q)^2) \, , 
\end{aligned}$$ for the geometric solution, $$\begin{aligned}
D^{({\rm conj})}_1(q) &= D^{({\rm conj})}_2(q) = -1 \, , \quad D^{({\rm conj})}_3(q) = -2 - q \, , \quad D^{({\rm conj})}_4(q)=-(1 + q) (1 + 2 q) \, , \\
D^{({\rm conj})}_5(q) &= -2 - 2 q - 7 q^2 - 4 q^3 - q^4 \, , \\
D^{({\rm conj})}_6(q) &= -(1 + q) (1 + 2 q + 3 q^2 + 6 q^3 + 7 q^4 + 2 q^5) \, \\
D^{({\rm conj})}_7(q) &= -2 - 2 q - 8 q^2 - 11 q^3 - 20 q^4 - 23 q^5 - 32 q^6 - 19 q^7 - 6 q^8 - q^9 \, , 
 \end{aligned}$$ for its conjugate, and $$\begin{aligned}
D^{({\rm self})}_1(q) =& 2 q \, , \quad D^{({\rm self})}_2(q) = 1 + q^2 \, , \quad D^{({\rm self})}_3(q) =1 + q^2 + 2 q^4 \, , \\
D^{({\rm self})}_4(q) =&-1 - q + q^2 + 2 q^4 + 3 q^6 + q^7 \, , \\
D^{({\rm self})}_5(q) =& -1 + q - q^2 + 2 q^3 + 4 q^5 + q^6 + 6 q^7 + 2 q^8 + 2 q^9 \, , \\
D^{({\rm self})}_6(q) =&  -1 - q^2 - 2 q^4 + 2 q^5 - 2 q^6 + 4 q^7 + q^8 + 8 q^9 + 4 q^{10} \\
& + 11 q^{11} + 7 q^{12} + 5 q^{13} + 3 q^{14} + q^{15} \, , \\
D^{({\rm self})}_7(q) =& -1 - q^3 - 2 q^5 + q^6 - 4 q^7 + 4 q^8 - 3 q^9 + 9 q^{10} + 4 q^{11} + 18 q^{12} \\
&+ 12 q^{13} + 27 q^{14} + 18 q^{15} + 17 q^{16} + 10 q^{17} + 8 q^{18} + 
 2 q^{19} + 2 q^{20} \, ,
\end{aligned}$$ for the self-conjugate one. Trivially, we have that $$\begin{aligned}
D^{({\rm conj})}_{-1}(q) = D^{({\rm conj})}_{-2}(q) &= q \, , \quad D^{({\rm conj})}_{-s}(q) = 0 \quad s \ge 3 \, , \\
D^{({\rm self})}_{-1}(q) &= q \, , \quad D^{({\rm self})}_{-s}(q) = 0 \quad s \ge 2 \, .
\end{aligned}$$ We have verified numerically that the polynomials $D_{\pm s}(q)$ have integer coefficients up to $s=20$ for all three branches. We then compute the integers $c_{\pm s}$, $s \in {\mathbb Z}_{>0}$, using Eqs. [\[cs-sequenceP\]](#cs-sequenceP){reference-type="eqref" reference="cs-sequenceP"}, [\[cs-sequenceM\]](#cs-sequenceM){reference-type="eqref" reference="cs-sequenceM"}, which give

$$\begin{align}
\{ c^{(\rm{geom})}_s\}_{s \in {\mathbb Z}_{>0}}=&\{ 1, 1, -8, -15, 1, 64, 148, 49, -575, -1599, -1088, 5088,  \dots \} \, , \label{cs52geom} \\
\{ c^{(\rm{conj})}_s\}_{s \in {\mathbb Z}_{>0}}=& (-1) \{ 1, 5, 28, 101, 401, 1544, 6077, 24101, 96418, 388205, 1571307, 6387608, \dots \} \, , \label{cs52conj}\\
\{ c^{(\rm{self})}_s\}_{s \in {\mathbb Z}_{>0}}=& \{ 2, 10, 38, 122, 402, 1486, 5931, 24058, 96995, 389810, 1572397, 6382526 \dots \} \, , \label{cs52self}
\end{align}$$

while $c^{(\rm{conj})}_{-s} = [s]_2+ 5 [s+1]_2$, where $[s]_2$ denotes the remainder of the division of $s$ by $2$, and $c^{(\rm{self})}_{-s} = 1$ for all $s \in {\mathbb Z}_{>0}$. We observe that the above sequences of integers satisfy the relation $$\label{cs-rel52}
c^{(\rm{geom})}_s + c^{(\rm{conj})}_s + c^{(\rm{self})}_s = c^{(\rm{conj})}_{-s} + c^{(\rm{self})}_{-s} \, , \quad s \in {\mathbb Z}_{>0} \, .$$ which corresponds to the analogous formula in Eq. [\[cs-rel41\]](#cs-rel41){reference-type="eqref" reference="cs-rel41"} for the figure-eight knot. Note that, in both our examples, the sum of the integer sequences $\{c_s\}$ over all branches equals the sum of the integer sequences $\{c_{-s}\}$, which is a periodic function of $s \in {\mathbb Z}_{>0}$. Again, the alternative computational approach of Appendix [\[app: rational2\]](#app: rational2){reference-type="ref" reference="app: rational2"} agrees with the above results.

Let us now go back to the quantum $A$-polynomial for the $\bm{5}_2$-knot written in Eq. [\[52Ahat\]](#52Ahat){reference-type="eqref" reference="52Ahat"}. The corresponding $q$-difference equation in the form of Eq. [\[AJ-eq\]](#AJ-eq){reference-type="eqref" reference="AJ-eq"} is of third order. Precisely, we have $$\label{Ahat-52}
\hat{A}_{\bm{5}_2}(\hat{P}, \hat{X}, q) \chi^{(\alpha), \rm{WKB}}(u; \hbar) = 0 \, ,$$ where $\chi^{(\alpha), \rm{WKB}}(u; \hbar)$ is the resummed perturbative wave function in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"} associated with the branch $\alpha$. In the rational case of $q= {\rm e}^{2 \pi {\rm i}{P \over Q}}$ with $P, Q \in {\mathbb Z}_{>0}$ coprime, Eq. [\[Ahat-52\]](#Ahat-52){reference-type="eqref" reference="Ahat-52"} can be solved in closed form by directly applying the results of Section [\[sec: 3rd-order\]](#sec: 3rd-order){reference-type="ref" reference="sec: 3rd-order"}. As for the $\bm{4}_1$-knot, let us consider the case $\alpha = \rm{geom}$ and drop the label to simplify our notation. After appropriately accounting for the exponential prefactor containing the functions $s_{0,1}(x)$ in Eq. [\[s01geom52-new\]](#s01geom52-new){reference-type="eqref" reference="s01geom52-new"}, the $q$-difference equation above assumes the form in Eq. [\[Psi-eq3\]](#Psi-eq3){reference-type="eqref" reference="Psi-eq3"} with the identifications $$\label{coeffs-qdiff52}
 \begin{aligned}
  A(X)= q^{-2} X^{-2} \frac{C_2(X,q)}{C_3(X,q)} \, , \quad B(X)= q^{-2} X^{-4} \frac{C_1(X,q)}{C_3(X,q)} \, , \quad C(X) = X^{-6} \frac{C_0(X,q)}{C_3(X,q)} \, ,
  \end{aligned}$$

where $C_0,C_1,C_2,C_3$ are the coefficient functions defined in Eq. [\[52xC\]](#52xC){reference-type="eqref" reference="52xC"}. Substituting the expressions in Eq. [\[coeffs-qdiff52\]](#coeffs-qdiff52){reference-type="eqref" reference="coeffs-qdiff52"} into Eq. [\[matrix3\]](#matrix3){reference-type="eqref" reference="matrix3"} and computing the matrix ${\cal M}_Q(X)$, we can then derive explicit formulae for $\Pi \upsilon$ and $\upsilon_0$ from Eqs. [\[Pi3\]](#Pi3){reference-type="eqref" reference="Pi3"}, [\[u03\]](#u03){reference-type="eqref" reference="u03"}. We stress that the ambiguity in the definition of $\Theta_2$ is resolved by requiring Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"} to be satisfied with $\alpha=\text{geom}$, which implies the choice $m=2$. Plugging these into Eq. [\[dict-end\]](#dict-end){reference-type="eqref" reference="dict-end"}, we find the functions $\Upsilon (X)$ and $\varphi_Q(X)$ for the geometric branch of the three-twist knot. We can easily use the resulting explicit expression for $\varphi_Q(X)$ to numerically evaluate the integer constants $c_s$, $s \in {\mathbb Z}_{>0}$, for the geometric branch by applying Eq. [\[varphiQ-cs\]](#varphiQ-cs){reference-type="eqref" reference="varphiQ-cs"} for any choice of $P, Q \in {\mathbb Z}_{>0}$ coprime, thus producing a third independent computation which is in perfect agreement with the previous two. The same discussion can be applied to the conjugate and self-conjugate branches of the $\bm{5}_2$-knot, in which case the appropriate functions $s_{0,1}(x)$ are written in Eqs. [\[s01conj52-new\]](#s01conj52-new){reference-type="eqref" reference="s01conj52-new"}, [\[s01self52-new\]](#s01self52-new){reference-type="eqref" reference="s01self52-new"} and the ambiguity in the choice of $m$ in Eq. [\[theta2-m\]](#theta2-m){reference-type="eqref" reference="theta2-m"} is fixed by imposing the condition in Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"} with $\alpha = \text{conj}, \text{self}$, yielding $m=1$ and $m=0$, respectively. Again, the corresponding integer constants $c_{\pm s}$, $s \in {\mathbb Z}_{>0}$, for the conjugate and self-conjugate branches match our previous results.

[^1]: ${\cal H}(x,y;q)$ is closely related to the $q$-hypergeometric function.

[^2]: Note that there are twice as many contributing factors of $q^{-1}$ here compared to the conjugate branch of the figure-eight knot, in agreement with the observed formulae for the functions $\sigma_{{\rm conj}, n}$ in Eqs. [\[sigma41\]](#sigma41){reference-type="eqref" reference="sigma41"}, [\[sigma52\]](#sigma52){reference-type="eqref" reference="sigma52"}.
