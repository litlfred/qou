---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-011-7-examples-via-maximaminima
section_title: "Examples via maxima/minima"
section_number: 7
pages: 21-26
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.974
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:bracket label="sec:bracket"}

The Kauffman bracket polynomial [@K&P] for knots up to regular isotopy is defined by the skein relation in Figure [1](#skeinbracket){reference-type="ref" reference="skeinbracket"}. The bracket value for the unknot diagram with no crossing is set to be $1$. In this section we examine invariants defined from YB $2$-cocycles and the bracket following the definition in Section [\[sec:cupcap\]](#sec:cupcap){reference-type="ref" reference="sec:cupcap"}. In this section we assume that $\mathbb k$ contains $\sqrt{-1}$ and an invertible element $A$ that serves as a variable in the Kauffman bracket.

<figure id="skeinbracket">
<div class="center">
<img src="skeinbracket" style="width:2.4in" />
</div>
<figcaption></figcaption>
</figure>

Let $\cup$ and $\cap$ be pairing used in the bracket skein relation defined in [@K&P] for basis elements $e_1$, $e_2$ of $V={\mathbb k}^{\otimes 2}$ by $\cup(e_i\otimes e_i)=0$ for $i=1,2$ and $$\cup(e_1 \otimes e_2)=\sqrt{-1} A , \quad \cup(e_2 \otimes e_1)=- \sqrt{-1} A^{-1} .$$ The copairing is defined by $$\cap (1)=\sqrt{-1} A e_1 \otimes e_2 - \sqrt{-1} A^{-1} e_2 \otimes e_1.$$ It is known [@K&P] that these satisfy the switchback, passcup, and passcap identities. The pairing is represented by a cup (a local minimum of a diagram), and the copairing is represented by a cap (a local maximum of a diagram) in Figure [1](#skeinbracket){reference-type="ref" reference="skeinbracket"}. As a first approach we examine the case where the pairing and copairing are not deformed, so that $\bar \cup = 0 = \bar \cap$.

<figure id="cocyskein">
<div class="center">
<img src="cocyskein" style="width:3.7in" />
</div>
<figcaption></figcaption>
</figure>

Diagrammatic convention for a $2$-cocycles for $\phi_1$ and $\hat \phi_1$ are depicted in Figure [3](#cocyskein1){reference-type="ref" reference="cocyskein1"}, where a double circles represents $\phi$ and a double circles with shaded inner circle represents $\hat \phi$. Let $B, \bar B, C, \bar C \in \mathbb k$. We set $\phi= B \mathbb 1 + \bar B \cap \cup$ and $\hat \phi= C  \cap \cup + \bar C \mathbb 1$ as in Figure [3](#cocyskein1){reference-type="ref" reference="cocyskein1"} and examine this case. Thus with the above $\phi$, $\hat \phi$ and undeformed $\cup$ and $\cap$, our set up is $\tilde R = R + \hbar \phi$ and $\tilde R^{-1} = R^{-1} + \hbar \hat \phi$ modulo $\hbar^2$ as described in the preceding section.

In Figure [3](#cocyskein1){reference-type="ref" reference="cocyskein1"} and later figures, the square bracket indicates that the cocycle skein relations are to be applied locally, and the bracket on the right-hand side indicates that the bracket skein relations are to be applied to other parts of a given diagram. For simplicity, we drop brackets when the stages of computations are understood.

<figure id="cocyskein1">
<div class="center">
<img src="cocyskein1" style="width:4.2in" />
</div>
<figcaption></figcaption>
</figure>

::: lemma
[]{#lem:B=C label="lem:B=C"} The operators $\tilde R = R + \hbar \phi$ and $\tilde R^{-1} = R^{-1} + \hbar \hat \phi$ satisfy the passcup and passcap identities if and only if $B=C$ and $\bar B = \bar C$.
:::

::: proof
*Proof.* A diagrammatic proof is presented in Figure [4](#passcupcap){reference-type="ref" reference="passcupcap"} for all identities involved. The identities are (1)=(2), (3)=(4), (5)=(6) and (7)=(8). One obtains the stated conditions from these diagrams. This argument is similar to the bracket case. ◻
:::

<figure id="passcupcap">
<div class="center">
<img src="passcupcap" style="width:6.5in" />
</div>
<figcaption></figcaption>
</figure>

From here on we assume the conditions $B=C$ and $\bar B = \bar C$ in Lemma [\[lem:B=C\]](#lem:B=C){reference-type="ref" reference="lem:B=C"}.

::: lemma
[]{#lem:inverse label="lem:inverse"} Under the condition $B=C$ and $\bar B = \bar C$, the operators $\tilde R = R + \hbar \phi$ and $\tilde R^{-1} = R^{-1} + \hbar \hat \phi$ are inverses to each other if and only if $\bar B = - A^{-2} B$ and $2(A^4 -1) B=0$.
:::

::: proof
*Proof.* One of the conditions for the two operators to be inverses to each other is computed under the skein relation in Figure [5](#inverse0){reference-type="ref" reference="inverse0"}. One of the $\hbar$-degree one part of the inverse conditions is depicted in Figure [6](#inverse1){reference-type="ref" reference="inverse1"} in the left-hand side. In the first line in the right-hand side, the defining relations of $\phi$ and $\hat \phi$ are are applied. In the second and the third lines, the bracket skein relation is applied. By collecting terms for each of $\mathbb 1$ and $\cap \cup$, we obtain $$\begin{aligned}
A^{-1} B + A \bar C &=& 0 , \\
AB+A^{-1} \bar C - A^3 \bar B - A^{-3} C &=& 0 .
\end{aligned}$$ By substituting $B=C$ and $\bar B = \bar C$ we obtain the stated result. ◻
:::

<figure id="inverse0">
<div class="center">
<img src="inverse0" style="width:3.2in" />
</div>
<figcaption></figcaption>
</figure>

<figure id="inverse1">
<div class="center">
<img src="inverse1" style="width:3in" />
</div>
<figcaption></figcaption>
</figure>

::: lemma
[]{#lem:YB2cocy label="lem:YB2cocy"} The operators $\tilde R$ and $\tilde R^{-1}$ are YBOs. Equivalently, $\phi$ and $\hat \phi$ are YB $2$-cocycles.
:::

::: proof
*Proof.* The left-hand side of Figure [7](#YBcocy){reference-type="ref" reference="YBcocy"} is the first term of the YB 2-cocycle condition in Figure [\[YBd2\]](#YBd2){reference-type="ref" reference="YBd2"}. In the top line of the right-hand side of Figure [7](#YBcocy){reference-type="ref" reference="YBcocy"} shows the expansion of crossings according to the bracket skein relation. In the second line, the skein relation for the YB 2-cocycle $\phi$ is applied. This computation is carried out for all the eight terms of the 2-cocycle condition in Figure [\[YBd2\]](#YBd2){reference-type="ref" reference="YBd2"}, and set equal to zero. The expressions is written in like terms with respect to the basis elements of the Temperley-Lieb algebra (e.g. [@K&P]) as depicted in Figure [8](#basis){reference-type="ref" reference="basis"}, and the coefficient of each basis element is set equal to zero. The coefficients of the elements (A), (D) and (E) cancel. Those for (B) and (C) each gives the identical condition $2(A^4-1)B = 0$, which is among the hypotheses for the choice of $A$ and $B$. The case for $\tilde R^{-1}$ is the same due to the symmetry in the definitions. ◻
:::

<figure id="YBcocy">
<div class="center">
<img src="YBcocy" style="width:6.2in" />
</div>
<figcaption></figcaption>
</figure>

<figure id="basis">
<div class="center">
<img src="basis" style="width:2.5in" />
</div>
<figcaption></figcaption>
</figure>

::: proposition
[]{#prop:allrelations label="prop:allrelations"} Let $\mathbb k$ be a unital ring that contains an invertible $A$ and $B,\bar B, C, \bar C$. The YBOs $\tilde R$ and $\tilde R^{-1}$, together with undeformed $\tilde \cup = \cup$ and $\tilde \cap=\cap$ define a quantum cocycle knot invariant up to regular isotopy if the following hold: $$B=C,  \quad \bar B = \bar C, 
\quad \bar B = - A^{-2} B, \quad 2(A^4 -1) B=0.$$
:::

::: proof
*Proof.* This follows from Lemma [\[lem:B=C\]](#lem:B=C){reference-type="ref" reference="lem:B=C"}, Lemma [\[lem:inverse\]](#lem:inverse){reference-type="ref" reference="lem:inverse"} and Lemma [\[lem:YB2cocy\]](#lem:YB2cocy){reference-type="ref" reference="lem:YB2cocy"}. ◻
:::

<figure id="writhe">
<div class="center">
<img src="writhe" style="width:3in" />
</div>
<figcaption></figcaption>
</figure>

::: definition
We normalize the regular isotopy invariant defined in Proposition [\[prop:allrelations\]](#prop:allrelations){reference-type="ref" reference="prop:allrelations"} by dividing it by the value $\delta=- A^2 - A^{-2}$ of the unknot $\begin{tikzpicture}
                                    \draw (0,0) circle (0.1cm);
                            \end{tikzpicture}$, and denote the normalized regular isotopy invariant by $\Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)}(K)$. Therefore, we have that $\Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)}(\begin{tikzpicture}
                            \draw (0,0) circle (0.1cm);
                            \end{tikzpicture}) = 1$.
:::

The supersctript M stands for maxima/minima. We note that since $\tilde \cup$ and $\tilde \cap$ are undeformed, the value of $\begin{tikzpicture}
                            \draw (0,0) circle (0.1cm);
                            \end{tikzpicture}$ does not contain any terms in $\hbar$, and therefore no new restrictions on $A$ and $B$ are added, as the invertibility of the normalizing factor does not depend on the deformation coefficients.

We examine the effect of writhe to normalize the regular isotopy invariant to obtain an isotopy invariant for oriented knot diagrams, as in the case of the bracket polynomial. Let $D$ be an oriented diagram.

It has been assumed in this section that knots are unoriented. To make a normalization by writhe, from here on we pick and fix an orientation. In Figure [9](#writhe){reference-type="ref" reference="writhe"} left-hand side, two types of small kinks are depicted. For the top figure, either choice of orientation gives a positive crossing for oriented diagrams, and a negative crossing for the bottom figure.

::: lemma
Let $D$ be a diagram of an oriented knot obtained from $D'$ by type I Reidemeister move of removing a small kink as in Figure [9](#writhe){reference-type="ref" reference="writhe"} top (resp. bottom) left. Set $$\begin{aligned}
w_+:= - A^{3} -  \hbar B A^{-2} (A^{4} + 2 ) , 
  & \ {\rm and} \  & 
w_- := - A^{-3} + \hbar B (A^{-4} + 2 )  .
\end{aligned}$$ Then we have, respectively, $\Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)} (D') =  w_+ \Psi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)} (D)$ and $\Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)}(D') =  w_- \Psi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)} (D).$
:::

::: proof
*Proof.* Diagrammatic computations are shown in Figure [9](#writhe){reference-type="ref" reference="writhe"} top and bottom right, respectively. ◻
:::

We note that the above two coefficients should yield $1$ when multiplied, and indeed we find $$\begin{aligned}
w_+ \cdot w_- &=& [ - A^{3} -  \hbar B A^{-2} (A^{4} + 2 ) ]    [ - A^{-3} + \hbar B (A^{-4} + 2 ) ]  \\
&=& 
1 -  \hbar B ( A^3 ( (A^{-4} + 2 )  - A^{-3} A^{-2} (A^{4} + 2 ) ) \\
&=& 
1 - \hbar B [ 2 A^{-5}  ( A^8 - 1 ) ] , 
\end{aligned}$$ modulo $\hbar^2$, and $2   ( A^8 - 1 ) B$ is divisible by $2(A^4 -1)B$, one of the equalities in Lemma [\[prop:allrelations\]](#prop:allrelations){reference-type="ref" reference="prop:allrelations"}, as expected. Hence we treat that $w_+$ and $w_-$ are inverses each other in $\mathbb k$.

By the writhe normalization argument, we obtain the following.

::: theorem
[]{#thm:bracket label="thm:bracket"} Let $D$ be an oriented knot diagram with the number of positive (resp. negative) crossings $p(D)$ (resp. $n(D)$). Then $$\Phi^{\rm W}_{(\tilde R, \tilde \cup, \tilde \cap)}  (D) = w_+^{-p(D)} w_-^{-n(D)} \Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)} (D)$$ is independent of choice of $D$ and indeed is an invariant up to isotopy, thus denoted by $\Phi^{\rm W}_{(\tilde R, \tilde \cup, \tilde \cap)}  (K)$ and simply $\Phi^{\rm W} (K)$.
:::

The superscript W stands for writhe-normalized. We also use the notation $\Phi^{\rm W} (K)=\Phi^{{\rm W} 0} (K) + \hbar  \Phi^{{\rm W} 1} (K)$. Since $w_+$ and $w_-$ are inverses of each other, we can also write the prefix powers to be $w_-^{p(D)} w_+^{n(D)}$.

::: lemma
[]{#lem:Tm label="lem:Tm"} Let $T_m$ be a $(2,m)$ torus knot or knot for positive integers $m$, as depicted in Figure [\[Tm\]](#Tm){reference-type="ref" reference="Tm"}. Then we have $\Phi^{\rm M} (T_1)= w_+$, $\Phi ^{\rm W}(T_1)=1$ and $$\begin{aligned}
 \Phi^{\rm M} (T_{m+1} ) &=&   (A + \hbar B ) \Phi^{\rm M} (T_m ) + (A^{-1} - \hbar A^2 B)  w_+^{m} , \label{eq:Tmbracket} \\
 \Phi^{\rm W} (T_{m+1}) &=&   (A + \hbar B )  w_-  \Phi^{\rm W}(T_m) +  (A^{-1} - \hbar A^2 B) w_- . \label{eq:TmJones}
\end{aligned}$$
:::

::: proof
*Proof.* Equation [\[eq:Tmbracket\]](#eq:Tmbracket){reference-type="eqref" reference="eq:Tmbracket"} follows from the definitions and the deformed bracket skein. Since $$\Phi^{\rm W} (T_m)=w_+^{-m}\Phi^{\rm M}(T_m)=w_-^m \Phi^{\rm M}(T_m),$$ by multiplying both sides by $w_-^{m+1}$, we obtain Equation [\[eq:TmJones\]](#eq:TmJones){reference-type="eqref" reference="eq:TmJones"}. ◻
:::

::: example
[]{#ex:Tmbracket label="ex:Tmbracket"}

Let $T_m$ be a $(2,m)$ torus knot or knot as depicted in Figure [\[Tm\]](#Tm){reference-type="ref" reference="Tm"}. If $m-1$ appears we retain it to be positive. Note that all crossings are positive. By using Equation [\[eq:TmJones\]](#eq:TmJones){reference-type="eqref" reference="eq:TmJones"}, we obtain $$\begin{aligned}
  \Phi^{\rm W}(T_2) &=&[  (A  + A^{-1}) + \hbar(B + A^2 B) ]  w_- \\
  &=& [ ( A  + A^{-1}) + \hbar (B - A^2B) ] [ - A^{-3} + \hbar B (A^{-4} + 2 ) ]  \\
  &=& -A^{-3}(A  + A^{-1}) + \hbar  B(A^{-5} + 3A^{-1} + 2A). 
\end{aligned}$$

By Proposition [\[prop:allrelations\]](#prop:allrelations){reference-type="ref" reference="prop:allrelations"}, the coefficient of $\hbar$ is considered modulo $2(A^4-1)$. This is satisfied with $A=\sqrt{-1}$. In the coefficient of $\hbar B$, $$A^{-5} + 3A^{-1} + 2A = - 2 \sqrt{-1}.$$ Thus $\Phi^{{\rm W} 1} (T_2)$ is nontrivial.
:::

::: proposition
For $A=\sqrt{-1}$, we have $\Phi^{{\rm W}} (T_m) = (2-m) +  \sqrt{-1} (m-1)  (8 - m)  \hbar  B$ $$\begin{aligned}
                \Phi^{{\rm W}} (T_m) &=& 
                \begin{cases}
                            0 - m\sqrt{-1}B\hbar \ \ \ \ \hspace{10mm} {\rm for}\ m\geq 0\  {\rm even}\\
                            \frac{1}{2} - (m-2)\sqrt{-1}B \hbar\ \  \ \ {\rm for}\  m\geq 0\ {\rm odd}
                \end{cases}.
        
\end{aligned}$$
:::

::: proof
*Proof.* From Example [\[ex:Tmbracket\]](#ex:Tmbracket){reference-type="ref" reference="ex:Tmbracket"}, we use the evaluation $A=\sqrt{-1}$. In this case the recursive formula of Lemma [\[lem:Tm\]](#lem:Tm){reference-type="ref" reference="lem:Tm"} becomes $$\Phi^{\rm W} (T_{m+1})_{A=\sqrt{-1}}  = ( \sqrt{-1}+ \hbar B )   w_-  \Phi^{\rm W}(T_m)_{A=\sqrt{-1}} +  ( - \sqrt{-1} +   \hbar B) w_- ,$$ where $w_- := - A^{-3} + \hbar B (A^{-4} + 2 )  = - \sqrt{-1} + 3 \hbar  B$. Hence by simplifying the notation $\varphi_m:=  \Phi^{\rm W}(T_m)_{A=\sqrt{-1}}$, we obtain $$\begin{aligned}
            \varphi_{m+1} 
            &=&
            (\sqrt{-1} + \hbar B)(\sqrt{-1}+3\hbar B)\varphi_m + (-\sqrt{-1} + \hbar B)(\sqrt{-1}+3\hbar B)\\
            &=&
            (-1+4\sqrt{-1}B\hbar)\varphi_m + (1-2\sqrt{-1}B\hbar ). 
        
\end{aligned}$$

Set $\varphi_m=a_m + \hbar B b_m$. Then we obtain $$\begin{aligned}
            a_{m+1} + \hbar B b_{m+1} &=&  (-1+4\sqrt{-1}B\hbar) (a_m + \hbar B b_m) + (1-2\sqrt{-1}B\hbar )\\
            &=& (-a_m +1) + \hbar B (4 \sqrt{-1} a_m - b_m - 2 \sqrt{-1} ),
        
\end{aligned}$$ so that $$\begin{cases} a_{m+1} = -a_m +1 , \\
        b_{m+1} = 4 \sqrt{-1} a_m - b_m - 2 \sqrt{-1} , 
        \end{cases}$$ and $a_1=1$, $b_1=0$. It follows that $a_m=0$ for $m$ even, and $a_m = 1$ for $m$ odd, while $b_m = -2m\sqrt{-1}$ for $m$ even, and $b_m = -2(m-2)\sqrt{-1}$ for $m$ odd. The normalizing factor is $\delta = -A^2-A^{-2} = 2$, and dividing $a_m$ and $b_m$ by $2$ we obtain the result. ◻
:::

::: corollary
There exist infinitely many knots and links with nontrivial, and distinct, infinitesimal part $\Phi^{{\rm W} 1}$ of the quantum cocycle invariant $\Phi^{{\rm W}}$.
:::
