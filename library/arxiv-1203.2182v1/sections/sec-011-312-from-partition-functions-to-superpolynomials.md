---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-011-312-from-partition-functions-to-superpolynomials
section_title: "From partition functions to superpolynomials"
section_number: 3.1.2
pages: 21-26
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.986
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
As we already explained around [\[superPdef\]](#superPdef){reference-type="eqref" reference="superPdef"}, the reduced colored superpolynomial ${\cal P}^R (K; a,q,t)$ is defined as the Poincaré polynomial of the triply graded homology ${\cal H }^R_{i,j,k} (K)$ that categorifies the colored HOMFLY polynomial $P^R (K;a,q)$. Here, the word "reduced" means that the normalization is such that $P^R ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}) = 1$. Although normalization is one of the delicate points one has to worry about, luckily it will not be a major issue for us here.

Besides normalization, there are several other choices that affect the explicit form of the answer and, therefore, need to be explained, especially for comparison with other approaches. Thus, earlier we already mentioned a very important choice of framing. Another important choice is a choice of grading conventions. In order to understand its important role, let us recall that the triply-graded homology ${\cal H }^R_{i,j,k} (K)$ is related to the doubly-graded $sl(N)$ theory ${\cal H }^{sl(N), R}_{i,j} (K)$ by means of the differentials $d_N$, illustrated in Figure [\[fig:superpolunmial_hier\]](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}: $${\cal H }^{sl(N), R}_{*,*} (K) \; \cong \; \left( {\cal H }^R_{*,*,*} (K) , d_N \right) \,.
\label{specN}$$ Taking the Poincaré polynomials on both sides gives [\[superright\]](#superright){reference-type="eqref" reference="superright"}--[\[PRright\]](#PRright){reference-type="eqref" reference="PRright"}.

In order to be consistent with the specialization $a=q^N$ (also illustrated on the left side of Figure [\[fig:superpolunmial_hier\]](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}), the $q$-degree of $d_N$ should be $N$ times greater than its $a$-degree and of opposite sign. The standard convention for the homological $t$-grading of all differentials $d_N$ with $N>0$ is $-1$. Modulo trivial[^1] rescalings, such as $a \mapsto a^2$ and $q \mapsto q^2$, there are two sets of conventions consistent with these rules used in the literature: $$\begin{array}{l@{\;}|@{\;}c@{\;}|@{\;}c@{\;}c}
\multicolumn{3}{c}{\textbf{(a, q, t) grading conventions:}} \\[.1cm]
\text{differentials} & \text{conventions of } \cite{DGR,GWalcher,AS,DMMSS} & \text{conventions of } \cite{GS} \\\hline
d_{N>0} & (-2,2N,-1) & (-1,N,-1) \\
d_{N<0} & (-2,2N,2N-1) & (-1,N,-3) \\
d_{\text{colored}} & (0,2,2) & (0,1,0) \\
& (-2,0,-3) & (-1,0,-1) \\
& \vdots &
\end{array}
\label{gradingtabl}$$ Here, we mostly follow the latter conventions and occasionally, for comparison, state the results in the former conventions.

Another choice of grading conventions comes from a somewhat surprising direction. A special feature of the colored knot homology is the *mirror symmetry* conjectured in [@GS]: $${\cal H }^{R}_{i,j,*} (K) \; \simeq \; {\cal H }^{R^t}_{i,-j,*} (K) \,.
\label{mirror}$$ It relates triply-graded HOMFLY homologies colored by representations (Young diagrams) $R$ and $R^t$ related by transposition. Although this nice property is also present even in the basic uncolored case of $R = R^t = \Box$ as a generalization of the $q \leftrightarrow q^{-1}$ symmetry [@DGR], its significance is fully revealed in the colored theory with $R \ne R^t$. In particular, for our applications it means that the triply-graded homologies ${\cal H }^{S^r} (K)$ and ${\cal H }^{\Lambda^r} (K)$ are essentially the same, and so are the colored superpolynomials ${\cal P}^{S^r}$ and ${\cal P}^{\Lambda^r}$.

Put differently, the mirror symmetry [\[mirror\]](#mirror){reference-type="eqref" reference="mirror"} implies that instead of two different triply-graded homology theories ${\cal H }^{S^r} (K)$ and ${\cal H }^{\Lambda^r} (K)$ one really has only one theory, ${\cal H }^r (K)$, labeled by $r$, such that passing from $R = S^r$ to $R = \Lambda^r$ is achieved by flipping the sign of the $q$-grading accompanied by a suitable $t$-regrading. On the other hand, according to [\[specN\]](#specN){reference-type="eqref" reference="specN"} the sign of the $q$-grading is correlated with the sign of $N$ in the specialization to $sl(N)$ doubly-graded homology. Therefore, ${\cal H }^r (K)$ is related to the $sl(N)$ colored knot homology via $$\left( {\cal H }^r (K) , d_N \right) =
\begin{cases}
{\cal H }^{sl(N), S^r} (K) \,, & N>0 \\
{\cal H }^{sl(-N), \Lambda^r} (K) \,, & N<0
\end{cases}
\label{gradchoicea}$$ or $$\left( {\cal H }^r (K) , d_N \right) =
\begin{cases}
{\cal H }^{sl(N), \Lambda^r} (K) \,, & N>0 \\
{\cal H }^{sl(-N), S^r} (K) \,, & N<0
\end{cases}
\label{gradchoiceb}$$ The choice between [\[gradchoicea\]](#gradchoicea){reference-type="eqref" reference="gradchoicea"} and [\[gradchoiceb\]](#gradchoiceb){reference-type="eqref" reference="gradchoiceb"} is a matter of convention. But it is an important choice since it certainly affects the form of ${\cal H }^r (K)$ and the corresponding superpolynomial [\[superPdef\]](#superPdef){reference-type="eqref" reference="superPdef"}.

To summarize, it seems that in our class of examples we have to deal with at least two choices, between grading conventions in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} and between [\[gradchoicea\]](#gradchoicea){reference-type="eqref" reference="gradchoicea"} and [\[gradchoiceb\]](#gradchoiceb){reference-type="eqref" reference="gradchoiceb"}. A nice surprise is that these two choices are actually related [@GS]: switching from [\[gradchoicea\]](#gradchoicea){reference-type="eqref" reference="gradchoicea"} to [\[gradchoiceb\]](#gradchoiceb){reference-type="eqref" reference="gradchoiceb"} has the same effect as switching from one set of grading conventions in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} to another. In other words, to quickly go from one set of grading conventions in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} to another one can simply exchange the role of symmetric and anti-symmetric representations or, equivalently, switch the Young tableaux $R$ and its transposed $R^t$. We shall use this trick in what follows, where our default grading conventions will be that of [@GS] and [\[gradchoicea\]](#gradchoicea){reference-type="eqref" reference="gradchoicea"}.\
Keeping in mind the relations between different convention choices, now we are ready to convert [\[Braid_symmetric\]](#Braid_symmetric){reference-type="eqref" reference="Braid_symmetric"} and [\[Braid_anti-symmetric\]](#Braid_anti-symmetric){reference-type="eqref" reference="Braid_anti-symmetric"} into the colored superpolynomials ${\cal P}^{R} (T^{2,2p+1}; a,q,t)$ for symmetric and anti-symmetric representations. Starting with the symmetric representations $R = S^r$, we can use the following change of variables $$\begin{aligned}
a & = & A \left( \frac{q_1}{q_2} \right)^{3/2} \,, \nonumber \\
q & = & \frac{1}{q_2} \,, \label{GSvarchng} \\
t & = & - \sqrt{\frac{q_2}{q_1}} \,, \nonumber
\end{aligned}$$ to write the refined partition function $Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{\Lambda^r};q_1,q_2)$ in terms of $a$, $q$, and $t$. For example, from this identification one easily finds the unreduced superpolynomial $\overline{{\cal P}}^{S^r} ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)$ of the unknot, *cf.* [\[unknotMqtR\]](#unknotMqtR){reference-type="eqref" reference="unknotMqtR"}: $$\begin{aligned}
\overline{{\cal P}}^{S^r} ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)
&=& \frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{\Lambda^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)}
=M_{\Lambda^r}(q_2^{\varrho};q_1,q_2) \nonumber \\
&=& (-1)^r A^{r/2} q_2^{r/2} \frac{(A^{-1};q_2)_r}{(q_2;q_2)_r}


=(-1)^{\frac{r}{2}}a^{-\frac{r}{2}}q^{\frac{r}{2}}t^{-\frac{3r}{2}} \frac{(-at^3;q)_r}{(q;q)_r} \,.
\label{unknotsuperSr}
\end{aligned}$$ Similarly, the reduced colored superpolynomial of a more general $(2,2p+1)$ torus knot is related to the partition function $Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{\Lambda^r};q_1,q_2)$ via a refined analogue of [\[JasZZratio\]](#JasZZratio){reference-type="eqref" reference="JasZZratio"}, $${\cal P}^{S^r} (T^{2,2p+1}; a,q,t) \; = \;
\left( \frac{q_1}{q_2} \right)^{\tfrac{pr}{2}}
\frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{\Lambda^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{\Lambda^r};q_1,q_2)} \,,
\label{superPfromZZ}$$ with the same identification of the parameters [\[GSvarchng\]](#GSvarchng){reference-type="eqref" reference="GSvarchng"}. Note how the role of $R = S^r$ and $R = \Lambda^r$ is exchanged in this relation, in line with the above discussion. Explicitly, from [\[Braid_anti-symmetric\]](#Braid_anti-symmetric){reference-type="eqref" reference="Braid_anti-symmetric"} we find $$\begin{aligned}
{\cal P}^{S^r} (T^{2,2p+1}; a,q,t)&=&
\sum_{\ell=0}^r\frac{(qt^2;q)_{\ell}(-at^3;q)_{r+\ell}(-aq^{-1}t;q)_{r-\ell}(q;q)_r}
{(q;q)_{\ell}(q^2t^2;q)_{r+\ell}(q;q)_{r-\ell}(-at^3;q)_r}\frac{(1-q^{2\ell+1}t^2)}{(1-qt^2)}
\nonumber \\
&&\quad
\times (-1)^ra^{-\frac{r}{2}}q^{\frac{3r}{2}-\ell}t^{-rp-\ell+\frac{r}{2}}
\left[
(-1)^{\ell}a^{\frac{r}{2}}q^{\frac{r^2-\ell(\ell+1)}{2}}t^{\frac{3r}{2}-\ell}
\right]^{2p+1} \,.
\label{Superpolynomial_sym_refined}
\end{aligned}$$ This is one of the main results, with these choices of conventions, that we will use for testing the refined / categorified volume conjectures [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} and [\[VCparamref\]](#VCparamref){reference-type="eqref" reference="VCparamref"}.

For completeness, and to illustrate how it is done in general, we also write down the colored superpolynomial of $(2,2p+1)$ torus knots obtained from [\[Braid_symmetric\]](#Braid_symmetric){reference-type="eqref" reference="Braid_symmetric"}. In the same grading conventions as in the relation [\[superPfromZZ\]](#superPfromZZ){reference-type="eqref" reference="superPfromZZ"}, the role of symmetric and anti-symmetric representations is reversed and we obtain the $\Lambda^r$-colored superpolynomial: $${\cal P}^{\Lambda^r} (T^{2,2p+1}; a,q,t) \; = \; \left( \frac{q_2}{q_1} \right)^{\tfrac{pr}{2}}
\frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{S^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{S^r};q_1,q_2)} \,,$$ where the parameter identification is essentially the same as in [\[GSvarchng\]](#GSvarchng){reference-type="eqref" reference="GSvarchng"} with $q_1$ and $q_2$ interchanged: $$\begin{aligned}
a & = & A \sqrt{\frac{q_2}{q_1}} \,, \nonumber \\
q & = & \frac{1}{q_1} \,, \\
t & = & - \sqrt{\frac{q_1}{q_2}} \,. \nonumber
\end{aligned}$$ The exchange $q_1 \leftrightarrow q_2$ that accompanies $R \leftrightarrow R^t$ is familiar in the context of refined BPS invariants as well as in the equivariant instanton counting which, of course, are not unrelated. Hence, from the partition function $Z^{\text{ref}}_{SU(N)}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{S^r};q_1,q_2)$, we find the unreduced superpolynomial $\overline{{\cal P}}^{\Lambda^r} ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)$ of the unknot: $$\begin{aligned}
\overline{{\cal P}}^{\Lambda^r} ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)
&=& \frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{S^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)}
= M_{S^r}(q_2^{\varrho};q_1,q_2)
\nonumber \\
&=& A^{-\frac{r}{2}} q_2^{\frac{r}{2}} \frac{(A;q_1)_r}{(q_2;q_1)_r}


=(-1)^{-\frac{r}{2}}a^{\frac{r}{2}}q^{\frac{r}{2}}t^{\frac{3r}{2}}
\frac{(-a^{-1}t^{-1};q)_r}{(qt^2;q)_r} \,,
\end{aligned}$$ and the reduced colored superpolynomial of the $(2,2p+1)$ torus knot: $$\begin{aligned}
{\cal P}^{\Lambda^r} (T^{2,2p+1}; a,q,t) &=& \sum_{\ell=0}^r
\frac{(qt^2;q)_{\ell}(q;q)_r(-a^{-1}t^{-1};q)_{r+\ell}(-a^{-1}q^{-1}t^{-3};q)_{r-\ell}(qt^2;q)_r}
{(q;q)_{\ell}(qt^2;q)_r(q^2t^2;q)_{r+\ell}(q;q)_{r-\ell}(-a^{-1}t^{-1};q)_r}
\nonumber \\
&&\quad
\times \frac{(1-q^{2\ell+1}t^2)}{(1-qt^2)}a^{\frac{r}{2}}q^{\frac{3r}{2}-\ell}t^{3r-\ell}
\left[(-1)^{\ell}a^{\frac{r}{2}}q^{\frac{\ell(\ell+1)-r^2}{2}}t^{\ell}\right]^{2p+1} \,.
\label{Superpolynomial_anti-sym_refined}
\end{aligned}$$ These results agrees with the earlier calculations of the colored superpolynomials in [@GS; @Cherednik] for small values of $p$ and $r$, and provide a generalization to arbitrary $p$ and $r$.\
Finally, we complete this part by writing the same formulas for the colored superpolynomials [\[unknotsuperSr\]](#unknotsuperSr){reference-type="eqref" reference="unknotsuperSr"}--[\[Superpolynomial_anti-sym_refined\]](#Superpolynomial_anti-sym_refined){reference-type="eqref" reference="Superpolynomial_anti-sym_refined"} in a different set of grading conventions that we dub "DGR," *cf.* [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}. As we pointed out earlier, a simple way to implement this change of conventions, based on the "mirror symmetry" [\[mirror\]](#mirror){reference-type="eqref" reference="mirror"}, is to change $R \mapsto R^t$ on one side of the relations [\[unknotsuperSr\]](#unknotsuperSr){reference-type="eqref" reference="unknotsuperSr"}, [\[superPfromZZ\]](#superPfromZZ){reference-type="eqref" reference="superPfromZZ"}, *etc.* As a result, we obtain a nice relation between the $R$-colored superpolynomial of $T^{2,2p+1}$ and the refined partition function of a line operator colored by the same representation $R$ (not $R^t$ as *e.g.* in [\[superPfromZZ\]](#superPfromZZ){reference-type="eqref" reference="superPfromZZ"}): $${\cal P}^{R}_{\text{DGR}} (T^{2,2p+1}; a,q,t) \; = \; \left( \frac{q_2}{q_1} \right)^{\tfrac{pr}{2}}
\frac{Z^{\text{ref}}_{SU(N)}({\bf S}^3,T^{2,2p+1}_{R};q_1,q_2)}{Z_{SU(N)}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R};q_1,q_2)} \,,$$ where $R=S^r$ or $\Lambda^r$. Using [\[Braid_symmetric\]](#Braid_symmetric){reference-type="eqref" reference="Braid_symmetric"}--[\[Braid_anti-symmetric\]](#Braid_anti-symmetric){reference-type="eqref" reference="Braid_anti-symmetric"} and the identification of variables [@GIKV]: $$\begin{aligned}
a^2 &=& A \sqrt{\frac{q_2}{q_1}} \,, \nonumber \\
q &=& \sqrt{q_2} \,, \label{DGRvarchng} \\
t &=& - \sqrt{\frac{q_1}{q_2}} \,. \nonumber
\end{aligned}$$ we find explicit expressions for ${\cal P}^{R}_{\text{DGR}}(T^{2,2p+1})$ with $R=S^r$ and $R=\Lambda^r$: $$\begin{aligned}
{\cal P}^{S^r}_{\text{DGR}}(T^{2,2p+1}; a,q,t)
&=&\sum_{\ell=0}^r
\frac{(q^2;q^2t^2)_{\ell}(q^2t^2;q^2t^2)_r(-a^2t;q^2t^2)_{r+\ell}(-a^2q^{-2}t;q^2t^2)_{r-\ell}}
{(q^2t^2;q^2t^2)_{\ell}(-a^2t;q^2t^2)_r(q^4t^2;q^2t^2)_{r+\ell}(q^2t^2;q^2t^2)_{r-\ell}}
\nonumber \\
&\times& \frac{(1-q^{4\ell+2}t^{4\ell})}{(1-q^2)}a^{-r}q^{3r-2\ell}t^{r-\ell}
\left[ (-1)^{r-\ell}a^rq^{r^2-\ell(\ell+1)}t^{r^2-\ell^2} \right]^{2p+1}
\label{Symmetric_DGR_refined}
\end{aligned}$$ $$\begin{aligned}
{\cal P}^{\Lambda^r}_{\text{DGR}}(T^{2,2p+1};a,q,t)
&=& \sum_{\ell=0}^r
\frac{(q^2t^2;q^2)_{\ell}(-a^{-2}t^{-1};q^2)_{r+\ell}(-a^{-2}q^{-2}t^{-3};q^2)_{r-\ell}(q^2;q^2)_r}{(q^2;q^2)_{\ell}(q^4t^2;q^2)_{r+\ell}(q^2;q^2)_{r-\ell}(-a^{-2}t^{-1};q^2)_r}
\nonumber \\
&\times& \frac{(1-q^{4\ell+2}t^2)}{(1-q^2t^2)}a^r q^{3r-2\ell}t^{3r-\ell}\left[(-1)^{\ell}a^{r}q^{-r^2+\ell(\ell+1)}t^{\ell}\right]^{2p+1}
\label{Anti-Symmetric_DGR_refined}
\end{aligned}$$ as well as the unreduced superpolynomials of the unknot $\overline{{\cal P}}^{S^r}_{\text{DGR}}({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,})$: $$\overline{{\cal P}}^{S^r}_{\text{DGR}}({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)
= \frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{S^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)}
=(-1)^{\frac{r}{2}}a^{-r}q^{r}t^{-\frac{r}{2}}\frac{(-a^2t;q^2t^2)_r}{(q^2;q^2t^2)_r} \,.$$ $$\overline{{\cal P}}^{\Lambda^r}_{\text{DGR}}({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; a,q,t)
= \frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{\Lambda^r};q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)}
=(-1)^{\frac{r}{2}}a^rq^rt^{\frac{r}{2}}\frac{(-a^{-2}t^{-1};q^2)_r}{(q^2;q^2)_r} \,.$$

[^1]: Such rescalings are much more elementary choices of notation, rather than interesting choices of grading convention that affect the explicit form of the results in a more delicate way. A typical example of such harmless rescaling is a doubling of all $a$- and $q$-gradings in the last column of [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} that gives $\deg (d_{N>0}) = (-2,2N,-1)$, as in the middle column, $\deg (d_{N<0}) = (-2,2N,-3)$, *etc.*
