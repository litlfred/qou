---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-021-334-asymptotic-behavior-in-different-grading-con
section_title: "Asymptotic behavior in different grading conventions"
section_number: 3.3.4
pages: 46-50
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.99
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
[]{#sec:saddle_DGR label="sec:saddle_DGR"}

It is instructive to study the asymptotic behavior of the colored superpolynomial and its specialization [\[Pq2special\]](#Pq2special){reference-type="eqref" reference="Pq2special"} in different grading conventions. For example, another popular set of grading conventions is the one

where differentials $d_{N<0}$ have degree $(-2,2N,2N-1)$, see [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}. One important lesson of this exercise will be the fact that the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"} has to be slightly modified depending on which grading conventions one chooses. Conceptually, and also as a simple way to remember which limit to take, one wants $$q^{\beta} t^{\gamma}  = e^{\hbar} \; \to \; 1 \,,
\label{gradreflimit}$$ where the exponents $\beta$ and $\gamma$ represent the degree[^1] of the colored differential, *cf.* [\[superright\]](#superright){reference-type="eqref" reference="superright"}, $$\deg (d_{\text{colored}}) \; = \; (0 , \beta, \gamma) \,.$$ Indeed, with the refined volume conjectures [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} and [\[VCparamref\]](#VCparamref){reference-type="eqref" reference="VCparamref"} we wish to probe the "large volume" asymptotics of the homological knot invariants $P_n (q,t)$, as $n$ goes to infinity. On the other hand, as we explained in section [\[sec:homological\]](#sec:homological){reference-type="ref" reference="sec:homological"}, the dependence of homological knot invariants on the "color" $R = S^{n-1}$ is controlled by the colored differentials which (in the basic case) change the value of $n$ by one unit, see *e.g.* [\[coloredPa\]](#coloredPa){reference-type="eqref" reference="coloredPa"}.

Therefore, in order to study the asymptotic behavior of the homological knot invariants under $n \to n+1$ for sufficiently large $n$, one needs to take a limit in which discrete values of $n$ are replaced by a continuous variable $x = e^u$ and different terms in the chain complex [\[VCsequence\]](#VCsequence){reference-type="eqref" reference="VCsequence"} are clumped together in a continuous distribution, described by $S_0 (u,t)$. Therefore, this continuous limit *is* precisely the limit in which $d_{\text{colored}}$ changes gradings by a tiny amount, *i.e.* the limit [\[gradreflimit\]](#gradreflimit){reference-type="eqref" reference="gradreflimit"}.

For example, in the grading conventions of [@DGR], the first colored differential listed in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} has $(a,q,t)$-degree $(0,2,2)$. Therefore, the right limit to take in this case is the limit [\[gradreflimit\]](#gradreflimit){reference-type="eqref" reference="gradreflimit"} with $\beta = 2$ and $\gamma=2$ or, more precisely, $$q^2 t^2 = e^{\hbar} \to 1 \,, \qquad t = \text{fixed} \,, \qquad x \equiv e^u = e^{n \hbar} = \text{fixed} \,.
\label{gradlimit}$$

In order to make this a little bit more concrete and to understand the issue better, let us illustrate how it all works in the large class of examples associated with $(2,2p+1)$ torus knots. We already computed the colored superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) for these knots in the grading conventions of [@DGR], and now to study its asymptotic behavior we will need a couple of useful identities. First, applying the Euler-Maclaurin formula [@Kirillov]: $$\begin{aligned}
\sum_{m=M}^Nf(m)&=&\int_M^Nf(t)dt+\frac{1}{2}(f(N)+f(M))
+\sum_{k=1}^{n}\frac{B_{2k}}{(2k)!}\left\{
f^{(2k-1)}(N)
\right\}
\nonumber \\
&&-\int_M^N\frac{\overline{B}_{2n}(t)}{(2n)!}f^{(2n)}(t)dt.
\end{aligned}$$ to the function $f(m)=\log\left(1-X(q^2t^2)^m\right)$, we find $$\begin{aligned}
\log(X;q^2t^2)_{\infty}=
\frac{1}{\hbar+\epsilon}{\rm Li}_2(X)+\frac{1}{2}\log(1-X)+\sum_{k=1}^{\infty}
\frac{B_{2k}}{(2k)!}\frac{U_{2k-1}(X)}{(1-X)^{2k-1}}(\hbar+\epsilon)^{2k-1}
\end{aligned}$$ where we temporarily introduced $\epsilon:=\log t$. In particular for $X=e^{\frac{s}{\hbar}}$, one finds the following expansion: $$\begin{aligned}
\log(X;q^2t^2)_{\infty} \; = \; -\frac{s}{2}\hbar^2-i\pi s\hbar+\frac{\pi^2}{3} +{\cal O}(e^{-\hbar s}) \,,
\end{aligned}$$ which we can apply to our result for the superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) or, to be more precise, to its specialization [\[Pq2special123\]](#Pq2special123){reference-type="eqref" reference="Pq2special123"} at $a = q^2$.

First, let us see what would happen if, instead of the correct limit [\[gradlimit\]](#gradlimit){reference-type="eqref" reference="gradlimit"} that comes from the gradings of colored differentials, we naively used the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"} (suitable for the homological invariants in the grading conventions of [@GS], where $\deg (d_{\text{colored}}) = (0,1,0)$). We would find that the desired specialization of the colored superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) can be approximated by an integral, much like in [\[Pn-saddle\]](#Pn-saddle){reference-type="eqref" reference="Pn-saddle"}, $${\cal P}^{S^{n-1}}_{\text{DGR}}(T^{2,2p+1};a=q^2,q,t)
\; \sim \; \int dz\; e^{\frac{1}{\hbar^2}V_{(2,2p+1)}^{\text{DGR}}(z,x;t)+{\cal O}(\hbar^{-1})} \,,$$ with a very simple potential function $V_{T^{2,2p+1}}^{\text{DGR}} (z,x;t)$: $$V_{(2,2p+1)}^{\text{DGR}}(z,x;t)
\; = \; (2p+1)\epsilon\left((\log x)^2-(\log z)^2\right) \,.$$ Clearly, the critical point of this potential is $z_0 = 1$ and, therefore, the colored superpolynomial in this grading and in the limit $\hbar\to 0$ behaves as $$\begin{aligned}
{\cal P}^{S^{n-1}}_{\text{DGR}}(T^{2,2p+1};a=q^2,q,t) \; \sim \; e^{\frac{1}{\hbar^2}V_{(2,2p+1)}^{\text{DGR}}(z_0,x;t)} \,.
\end{aligned}$$ This behavior is way too simple to learn anything non-trivial about the "large color" behavior of the colored superpolynomial and is not even in the expected form ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a), which is yet another signal that one needs to be very careful passing from one set of grading conventions to another.

Now, let us consider the asymptotic behavior of the same object in the correct limit [\[gradlimit\]](#gradlimit){reference-type="eqref" reference="gradlimit"}. Again, as in [\[Pn-saddle\]](#Pn-saddle){reference-type="eqref" reference="Pn-saddle"}, we can write $${\cal P}_{\text{DGR}}^{S^{n-1}}(T^{2,2p+1};a=q^2,q;t)
\; \sim \; \int dz\; e^{\frac{1}{\hbar} \biggl(V_{(2,2p+1)}^{\text{DGR}}(z,x,t) +{\cal O}(\hbar)\biggr)} \,,$$ with $$\begin{aligned}
&&V_{(2,2p+1)}^{\text{DGR}}(z,x;t)=
{\rm Li}_2(-t^{-1}) - {\rm Li}_2(x) + {\rm Li}_2(-xt^{-3}) +
{\rm Li}_2(xz^{-1}) - {\rm Li}_2(-xt^{-1}z^{-1})
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad\;
+ {\rm Li}_2(z) - {\rm Li}_2(zt^{-2}) - {\rm Li}_2(-x zt^{-3})
+ {\rm Li}_2(x zt^{-2})-\frac{\pi^2}{6}
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad\;
+  (2p+1)\Bigl[ (\log (-t^{-2}))\cdot(\log x) +
    \frac{(\log x)^2 - (\log z)^2}{2}-\pi i\log z\Bigr]
\nonumber \\
&& \quad\quad\quad\quad\quad\quad\quad\;
+(\log t)\cdot  (\log z) \,.
\end{aligned}$$ From this potential function, the saddle point condition ([\[saddle_point\]](#saddle_point){reference-type="ref" reference="saddle_point"}) and the first line of ([\[braid_saddle2\]](#braid_saddle2){reference-type="ref" reference="braid_saddle2"}) we find the equations for the saddle point that dominates the above integral:

$$\begin{aligned}
&&1=\frac{ (t^2 - z) z^{-1 - 2 p} (-x + z) (t^3 + x z)}{t (-1 + z) (x + t z) (t^2 - x z)},
\nonumber \\
&&y=-\frac{ t^{-1 - 4 p} (-1 + x) x^{1 + 2 p} (x + t z) (t^3 + x z)}
{(t^3 + x) (x - z) (t^2 - x z)}.
\label{Saddle_DGR2}
\end{aligned}$$ Eliminating the variable $z$, we find the refined A-polynomial $A^{\text{DGR}}_{T^{2,2p+1}} (x,y;t)$. For $p=1$, the refined A-polynomial will be described in Appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"}. For $t=-1$ we find the same behavior as in the analysis of ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) and ([\[braid_saddle2\]](#braid_saddle2){reference-type="ref" reference="braid_saddle2"}): the first equation above only specifies the value $z_0^{2p+1}=1$, and the second one reduces to ordinary unrefined $A$-polynomial equation for $T^{2,2p+1}$ knot $y+x^{2p+1}=0$.

The algebraic equations ([\[Saddle_DGR2\]](#Saddle_DGR2){reference-type="ref" reference="Saddle_DGR2"}) can be easily solved around $t=-1$: $$\begin{aligned}
z_j&=&\xi_j+\frac{\xi_j(1+\xi_j)(-2 x + \xi_j + 2 x \xi_j + x^2 \xi_j - 2 x \xi_j^2)}{(1 + 2 p) (x - \xi_j) (-1 + \xi_j) (-1 + x \xi_j)}(1+t)
\nonumber \\
&&+{\cal O}((1+t)^2),
\end{aligned}$$ with $\xi_j=e^{\frac{2\pi ij}{2p+1}}$. Plugging this solution into the second equation of ([\[Saddle_DGR2\]](#Saddle_DGR2){reference-type="ref" reference="Saddle_DGR2"}), we find the approximate solution for $y$ (as a function of $x$ and $t$): $$\begin{aligned}
y&=&-x^{2p+1}\Bigl[
1+(1+t)
(-3 x - 4 p x + 4 p x^2 + 2 \xi_j + 4 p \xi_j + x \xi_j -
 4 p x \xi_j + 4 x^2 \xi_j + 4 p x^2 \xi_j
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad
- x^3 \xi_j -
 4 p x^3 \xi_j - 3 x \xi_j^2 - 4 p x \xi_j^2 + 4 p x^2 \xi_j^2)


/(-1 + x) (x - \xi_j) (-1 + x \xi_j)
\nonumber \\
&&\quad\quad\quad\quad
+{\cal O}(1+t)^2\Bigr].
\end{aligned}$$ From ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}), one can also find the refined classical action $S_0(u,t)$: $$\begin{aligned}
S_0(u,t)&=&S_0(u)+\sum_{a=1}^{\infty}(1+t)^aS_0^{(a)}(u),
\nonumber \\
S_0(u)&=&\frac{1}{2(2p+1)}\log(-x^{2p+1})^2,
\nonumber \\
S_0^{(1)}(u)&=&\log\frac{x^{4p+2}(x-\xi_j)(1-x\xi_j)}{(1-x)^3},
\nonumber \\
S_0^{(2)}(u)&=&\frac{1}{2}S_0^{(1)}
\nonumber \\
&&
+\frac{1}{2(2p+1)(-1 + x) (x - \xi_j)^2 (-1 + x \xi_j)^2}
\nonumber \\
&&\times\bigl(
-7 x^2 - 8 p x^2 - 2 x^3 - 10 p x^3 + 9 x \xi_j + 14 p x \xi_j +
 5 x^2 \xi_j + 22 p x^2 \xi_j + 19 x^3 \xi_j
\nonumber \\
&&
+ 26 p x^3 \xi_j +
 3 x^4 \xi_j + 10 p x^4 \xi_j - 3 \xi_j^2 - 6 p \xi_j^2 -
 2 x \xi_j^2 - 12 p x \xi_j^2 - 30 x^2 \xi_j^2 - 48 p x^2 \xi_j^2
\nonumber \\
&&
-
 6 x^3 \xi_j^2 - 24 p x^3 \xi_j^2 - 13 x^4 \xi_j^2 -
 18 p x^4 \xi_j^2 + 13 x \xi_j^3 + 22 p x \xi_j^3 + x^2 \xi_j^3 +
 14 p x^2 \xi_j^3
\nonumber \\
&&
+ 23 x^3 \xi_j^3 + 34 p x^3 \xi_j^3 - x^4 \xi_j^3 +
 2 p x^4 \xi_j^3 - 11 x^2 \xi_j^4 - 16 p x^2 \xi_j^4 +
 2 x^3 \xi_j^4 - 2 p x^3 \xi_j^4
\bigr),
\nonumber
\\
&&
\end{aligned}$$ and the general form of the classical action: $$\begin{aligned}
S_0(u,t)&=&\frac{1}{2(2p+1)}\left(\log(-x^{2p+1})\right)^2-\log(-t)
 \log\left(\frac{x^{4p+2}(x-\xi_j)(1-x\xi_j)}{(1-x)^3}\right)+R(x,t).
\nonumber \\
&&
\end{aligned}$$

[^1]: For simplicity, here we assume that the $a$-degree of $d_{\text{colored}}$ is equal to zero, as for the first set of colored differentials in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}.
