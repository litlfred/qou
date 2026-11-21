---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.967
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Borel transform [@Borel] is an important tool in the study of non-perturbative phenomena. It is used to extract information from divergent series which typically arise in perturbative expansions. Non-perturbative partition functions depend on extra parameters, like the choice of integration contour, this dependence seems to disappear in perturbative expansion, but is in fact traded for divergence of the series. New parameters appear as an ambiguity in the Borel transform. All this is well seen already in the simplest example of the exponential Borel transform $$\begin{aligned}
\sum_r   r!\cdot q^r  =
 \int_0^\infty \sum_r (qx)^r e^{-x} dx = \int_0^\infty \frac{e^{-x} dx }{1-qx}
 \label{factorialelimination}
\end{aligned}$$ Now, it is clear that the r.h.s. depends on the integration contour, and there is an ambiguity $$\begin{aligned}
\oint_{x=q^{-1}} \frac{e^{-x} dx }{1-qx} = \frac{2\pi i}{q} e^{-{1/q}}
\end{aligned}$$ so that the sum of divergent series is defined modulo this "instantonic\" term.

This standard argument, lying in the base of entire \"resurgence theory\" [@resurgence] is, however, technically based on exponential functions, and their Gamma and, more general, hypergeometric generalizations. They have, of course, a straightforward $q$ ("quantum\") and $t$ deformations [@GR; @Mac1; @Koor], but this is not the only important direction to look at. In modern integrability theory [@UFN3], which is a crucially important part of non-perturbative physics, an important role is played by *combinatorial* generalizations of the factorial, like the quantity $d_R$, which extends the factorial from integers to partitions (Young diagrams). It seems important to look at the versions of Borel transform that deal with such additional combinatorial structure, hence, the name combinatorial Borel transform. Surprisingly or not, exponentials still show up in the combinatorial Borel transforms, through Cauchy identities [@Mac], thus most probably this is not the last step. However, it can prove sufficient for the needs of integrability theory, at least.

As to possible techniques which could provide a route to the combinatorial Borel transforms, in [@2212.04859] it was suggested to consider an interpolation between two different kinds of sums over all Young diagrams $$\begin{aligned}
\sum_R q^{|R|} = \prod_{k=1}\frac{1}{1-q^k}
\label{gendia}
\end{aligned}$$ and $$\begin{aligned}
\sum_R q^{|R|} S_R\{p\}S_R\{\bar p\} = \exp\left(\sum_k \frac{q^kp_k\bar p_k}{k}\right)
\label{Cauchy}
\end{aligned}$$ by taking a specially adjusted average of the Schur functions over the power sums $p_k$. The emphasis, however, can be put not so much on averaging, but on coexistence of generating functions differing by the non-trivial combinatorial weights $d_R$. It is a common place to consider such families differing by the number of factorials in the weights: these are just related by the standard exponential Borel transform. It is an interesting direction to study a more tricky combinatorial difference. The goal of the present paper is to exploit this idea and extend it further in various directions.

<figure>
<div class="picture">
<p>(300,100)(-50,-70) (0,0)<span><span class="math inline">∑<sub><em>r</em></sub><em>a</em><sub><em>r</em></sub><em>q</em><sup><em>r</em></sup></span></span> (14,-10)<span>(0,-1)<span>25</span></span> (-25,-25) (18,-35)<span>(0,1)<span>25</span></span> (24,-21) (22,-31)<span><span class="math inline">$\left&lt;q^r\right&gt;=q^r \frac{a_r}{b_r}$</span> </span> (0,-50)<span><span class="math inline">∑<sub><em>r</em></sub><em>b</em><sub><em>r</em></sub><em>q</em><sup><em>r</em></sup></span></span></p>
<p>(60,0)<span><span class="math inline">=</span></span></p>
<p>(60,-50)<span><span class="math inline">=</span></span></p>
<p>(45,-60)<span><span class="math inline">$S_r\{0\}=\frac{b_r}{c_r}$</span></span></p>
<p>(105,0)<span><span class="math inline">∑<sub><em>r</em></sub><em>a</em><sub><em>r</em></sub><em>q</em><sup><em>r</em></sup></span></span> (100,-50)<span><span class="math inline">$\underline{\sum_r c_r q^r S_r\{\bar p\}}$</span></span> (120,-37)<span>(0,1)<span>26</span></span> (125,-25)<span><span class="math inline">$\left&lt;S_r\{\bar p\}\right&gt;_{\bar p} =\frac{a_r}{c_r}$</span></span></p>
<p>(185,5)<span>(1,0)<span>40</span></span> (185,8)<span>(1,0)<span>40</span></span> (185,-45)<span>(1,0)<span>40</span></span> (185,-48)<span>(1,0)<span>40</span></span> (295,-25)<span>(0,1)<span>15</span></span> (299,-10)<span>(0,-1)<span>17</span></span> (260,-22) (307,-22)<span><span class="math inline">$\left&lt;S_R\{\bar p\}\right&gt;_{\bar p} = \frac{a_R}{c_R}$</span></span></p>
<p>(250, 0)<span><span class="math inline">∑<sub><em>R</em></sub><em>a</em><sub><em>R</em></sub><em>q</em><sup>|<em>R</em>|</sup><em>S</em><sub><em>R</em></sub>{<em>p</em>} = <em>F</em>{<em>p</em>}</span></span> (250,-50)<span><span class="math inline">$\boxed{\sum_R c_R q^{|R|} S_R\{p\} S_R\{\bar p\}}$</span></span></p>
<p>(175,20)</p>
</div>
<figcaption>A picture, illustrating the concept of the <span><em>combinatorial Borel transform</em></span> (CBT) of the series. First, we introduce into the original series an auxiliary function <span class="math inline"><em>S</em><sub><em>r</em></sub>{<em>p̄</em>}</span> such that its average over <span class="math inline"><em>p̄</em></span> with an appropriate measure can change the coefficients in a desired way: say, <span class="math inline"><em>a</em><sub><em>r</em></sub> = <em>r</em>! → <em>b</em><sub><em>r</em></sub> = 1</span> in (<a href="#factorialelimination" data-reference-type="ref" data-reference="factorialelimination">[factorialelimination]</a>) or, more general, <span class="math inline"><em>a</em><sub><em>r</em></sub> = <em>d</em><sub><em>r</em></sub><sup><em>m</em></sup> = (<em>r</em>!)<sup>−<em>m</em></sup> → <em>b</em><sub><em>r</em></sub> = <em>a</em><sub><em>r</em></sub><em>d</em><sub><em>r</em></sub> = <em>d</em><sub><em>r</em></sub><sup><em>m</em> + 1</sup> = (<em>r</em>!)<sup>−<em>m</em> − 1</sup></span>. For traditional applications, the main point is that the underlined sum can converge better than the original one in the left upper corner due to <span class="math inline">$S_r\{0\} = \frac{b_r}{c_r} \sim \frac{1}{r!}$</span>, but for us this is just one application of many. Then, we extend the summation domain <span class="math inline">{<em>r</em>} → {<em>R</em>}</span> and introduce an additional auxiliary function <span class="math inline"><em>S</em><sub><em>R</em></sub>{<em>p</em>}</span> so that the sum in the box is easily calculated, for instance, with the help of the Cauchy identity. As an additional bonus, this converts the Cauchy relations into ineteresting formulas for the series <span class="math inline"><em>F</em>{<em>p</em>}</span> at the right upper corner, which can <span><em>a priori</em></span> look non-trivial, but are actually the <span class="math inline"><em>p̄</em></span> averages of simple identities. Technically, what we do is a substitution of the Gamma-function average <span class="math inline">⟨<em>q</em><sup><em>r</em></sup>⟩ → <em>q</em><sup><em>r</em></sup><em>Γ</em>(<em>r</em>+1) = <em>r</em>! ⋅ <em>q</em><sup><em>r</em></sup></span> which inverts the left vertical arrow in the usual Borel transform, by a smoother and richer Gaussian average, at the price of extending the sum over integers <span class="math inline"><em>r</em></span> to that over all integer partitions (Young diagrams) <span class="math inline"><em>R</em></span>. Such generalization is not unique, which opens a way to obtain a whole class of formulas by slight changes of the Gaussian measure. </figcaption>
</figure>

The paper is organized as follows. In section 2, we explain the basic of our approach, and demonstrate how the averaging method works for evaluating sums. In section 3, we extend the method to reproduce multiple combinatorial sums. In section 4, we discuss evaluating bilinear averages in parallel with the property of strong superintegrability in matrix models. Section 5 contains short notes on relations of the sums considered in the paper with the Ramanujan sums. At last, section 6 discusses the cases when the sums are divergent, while section 7 contains some concluding remarks.

#### Notation.

We use the notation $S_R\{p_k\}$ for the Schur functions, which are symmetric functions of $x_i$, and are graded polynomials of power sums $p_k:=\sum_ix_i^k$. They are labeled by partitions, or, equivalently, by Young diagrams $R$ with $l_R$ parts: $R_1\ge R_2\ge\ldots\ge R_{l_R}$. The corresponding skew Schur functions labeled by two partitions $R$ and $Q\in R$ are denoted as $S_{R/Q}\{p_k\}$, while the Macdonald polynomials are denoted through $M_R\{p_k\}$. We also denote $R^\vee$ the conjugate partition (Young diagram).

Our main quantity in this paper is $d_R$, $$\begin{aligned}
d_R = \frac{\prod_{i<j}^{l_R} \left(R_i -i - R_j+j\right)}
{\prod_{i=1}^{l_R} \left(l_R +R_i-i   \right)!}
\end{aligned}$$ which is equal to $S_R\{\delta_{k,1}\}$ in terms of Schur functions, and is equal to ${\rm dim}_R/|R|!$, where ${\rm dim}_R$ is the dimension of representation $R$ of the symmetric group ${\cal S}_{|R|}$. $|R|=\sum_i^{l_R}R_i$ is here the size of partition $R$ with $l_R$ parts.

The theory of symmetric functions can be found in [@Mac], and the theory of symmetric groups, in [@Fulton].

We also use notation $\sum_R$ for the sum over all partitions $R$ including the empty set, while $\sum_{R\vdash m}$ means summing over all partitions of integer $m$.
