---
doc_id: arxiv-0807.2679v1
doc_title: "A cabling formula for the colored Jones polynomial"
section_id: sec-001-proof-of-the-cabling-formula
section_title: "Proof of the cabling formula"
section_number: null
pages: 4-10
source_pdf: 0807.2679v1.pdf
source_sha256: 69ef10f8e70fc6f6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.992
doc_brief: "A cabling formula for the colored Jones polynomial — We prove an explicit cabling formula for the colored Jones polynomial."
---
Let us fix a banded link $L$ with $c$ components $L_1,\hdots, L_c$. Choosing a component $L_i$ of $L$ and opening it up we can write $L$ as the closure of a banded $(1,1)$-tangle $T_i$. Define $T_{i;s}$ to be the banded $(s,s)$-tangle obtained from $T_i$ by replacing the opened component $L_i$ of $T_i$ by $s$ parallel bands. In terms of these tangles the $(i;r,s)$-cabling of $L$ is equal to the closure of the composition $T_{i;s} \circ B_s^r$, see also figure 1.

Note that the link $L_{i;s}^r$ has $c+g-1$ components, where $g = \mathrm{gcd}(r,s)$, since the component $L_i$ of $L$ is replaced by the $g$-component torus link that is the closure of $B^r_s$. If we number the strands of the braid $B^r_s$ starting at $0$ then two strands are in the same component of the closure if and only if their numbers are congruent modulo $g$. Therefore each component of the closed braid consists of $p = s/g$ strands. Let us suppose that our link $L_{i;s}^r$ is colored by the integers $(M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_{c})$, where the vector $\mathbf{N} = (N_0,\hdots,N_{g-1})$ represents the new colors used to color the components of the torus link that replaces the component $L_i$.

We denote the the $N$-dimensional irreducible representation of quantum $sl_2$ by $V_N$. Using the above coloring, the torus braid corresponds to a morphism from $V = \bigotimes_{k=0}^{s-1} V_{N_{k\ \mathrm{mod}g}}$ to itself. In terms of these morphisms we can now state that the unnormalized $(M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_c)$-colored Jones polynomial of the $(i;r,s)$-cabling of $L$ (abbreviated by $J$) is the following quantum trace:

$$\label{Jonesquantumtrace}J = J_{M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_c}(L^r_{i;s}) = \mathrm{Tr}_q (B_s^r \circ T_{i;s},V)$$

The first step in calculating this trace is to expand it using the isotypical decomposition of the tensor product as quantum $sl_2$ representations:

$$\label{Isodec}V=\bigotimes_{k=0}^{s-1} V_{N_{k\ \mathrm{mod} g}} \cong \bigoplus_{j=1}^{p|\mathbf{N}|-s+1} \mathrm{Hom}(V_j,V) \otimes V_j$$

The range of the summation is calculated by the Clebsch-Gordan rule [@Procesi]. The isomorphism maps $(\alpha_j\otimes v)$ on the right to $\alpha_j(v)$ and $B^r_s \circ T_{i;s}$ acts on $\mathrm{Hom}(V_j,V)$ only, while quantum $sl_2$ acts on the $V_j$ only. We can therefore expand the quantum trace in [\[Jonesquantumtrace\]](#Jonesquantumtrace){reference-type="eqref" reference="Jonesquantumtrace"} as follows: $$\label{Isotrace}J = \mathrm{Tr}_q(B^r_s \circ T_{i;s},V) = \sum_j \mathrm{Tr}(B^r_s \circ T_{i;s},\mathrm{Hom}(V_j,V))\mathrm{Tr}_q(\mathrm{Id},V_j)$$ We know that $\mathrm{Tr}_q(\mathrm{Id},V_j) = [j] = (q^{j/2}-q^{-j/2})/(q^{1/2}-q^{-1/2})$. To calculate the other traces we study how $B^r_s \circ T_{i;s}$ acts on an element $\alpha \in \mathrm{Hom}(V_j,V)$. The action is by composition so first we look at $T_{i;s} \circ \alpha$, the action of $T_{i;s}$. According to the graphical calculus [@Turaev] the colored tangle $T_{i;s}$ represents the same map as the $(1,1)$-tangle $T_i$ colored with $V$. Furthermore we can depict $\alpha$ as a coupon connecting the top of a vertical strand colored $V_j$ to the lower end of $T_i$ (this end is colored $V$), see figure 2.

Now we can slide the coupon $\alpha$ up along the $(1,1)$-tangle $T_{i}$. We obtain $\alpha$ on top of $T_i$, where $T_i$ is now colored with $V_j$. Since $V_j$ is irreducible, the operator represented by $T_i$ is multiplication by a scalar. By closing $T_i$ one sees that this scalar is exactly $[j]^{-1}J_{M_1,\hdots,M_{i-1},j,\hdots,M_c}(L)$. We conclude that $T_{i;s} \circ \alpha = [j]^{-1}J_{M_1,\hdots,M_{i-1},j,\hdots,M_c}(L)\alpha$.

<figure>
<div class="center">
<embed src="Slide.eps" />
</div>
<figcaption>Sliding the coupon <span class="math inline"><em>α</em></span> up through the tangle <span class="math inline"><em>T</em><sub><em>i</em>; <em>s</em></sub></span>.</figcaption>
</figure>

The above argument shows that $B^r_s \circ T_{i;s} \circ \alpha = [j]^{-1}J_{M_1,\hdots,M_{i-1},j,\hdots,M_c}(L) B^r_s \circ \alpha$. Therefore equation [\[Isotrace\]](#Isotrace){reference-type="eqref" reference="Isotrace"} becomes: $$\label{JIs} J = \sum_{j=1}^{p|\mathbf{N}|-s+1}\mathrm{Tr}(B^r_s,\mathrm{Hom}(V_j,V))J_{M_1,\hdots,M_{i-1},j,\hdots,M_c}(L)$$

Note that an equation such as [\[JIs\]](#JIs){reference-type="eqref" reference="JIs"} remains valid when one replaces $B^r_s$ by any braid $B$. Such a satellite formula also appears in [@MortonStrickland].

We now concentrate on calculating the trace $\mathrm{Tr}(B_s^r,\mathrm{Hom}(V_j,V))$. Note that $(B_s^r)^s = ((\sigma_1\cdots \sigma_{s-1})^s)^r$ is a central element of the braid group. The element $C = (\sigma_1\cdots \sigma_{s-1})^s$ can also be thought of as a curl in $s$ parallel strands (hence the extra curls in the definition of $B^r_s$), so it acts on $\alpha$ as $C\circ \alpha = q^{\frac{j^2-1}{4}}\alpha$. If we set $D = q^{-\frac{r}{s}\frac{j^2-1}{4}}B^r_s$, then $D^s$ acts as the identity on $\mathrm{Hom}(V_j,V)$. An argument by Jones and Rosso [@JonesRosso] shows that its trace does not depend on $q$. For the record we express the trace we were looking for in terms of $D$: $$\label{BD}\mathrm{Tr}(B^r_s,\mathrm{Hom}(V_j,V)) = q^{\frac{r}{s}\frac{j^2-1}{4}}\mathrm{Tr}(D,\mathrm{Hom}(V_j,V))$$ Since the trace of $D$ does not depend on $q$ we can calculate it at $q = 1$. In this case $B^r_s = D$ equals the permutation $(\sigma_1\cdots \sigma_{s-1})^r$ and the representation $V$ can be viewed as an $SL(2)$ representation. By collecting common factors in the tensor product we see that $V \cong \bigotimes_{k=0}^{g-1} V_{N_k}^{\otimes p}$, where $p = s/g$. Note that our permutation $D$ acts on $V$ by permuting the factors inside each tensor power. More precisely $D = c_0\cdots c_{g-1}$ where the $c_k$ are disjoint $p$-cycles and $c_k$ permutes the factors of $V_{N_k}^{\otimes p}$. We can therefore interpret $D$ as an element of the Cartesian product $S_p^g$.

One can view each of the tensor powers $V_{N_k}^{\otimes p}$ as a $S_p \times GL(V_{N_k})$ representation, where $S_p$ acts by permuting the tensor factors and $GL(V_{N_k})$ acts diagonally. By Schur-Weyl duality [@Procesi] this space allows a simultaneous decomposition into irreducibles:

$$V_{N_k}^{\otimes p} \cong \bigoplus_{\lambda_k \vdash p}E_{\lambda_k}\otimes W_{\lambda_k}$$ Here $E_{\lambda_k}$ is an irreducible $S_p$ representation and $W_{\lambda_k}$ is an irreducible $GL(V_{N_k})$ representation and the sum is over all partitions of length no more than $N_k$. Taking the tensor product over all such powers and rearranging the factors gives the following decomposition of $V$ as an $S_p^g\times GL(V_{N_0})\times \cdots \times GL(V_{N_{g-1}})$ representation.

$$V \cong \bigoplus_{\lambda_{0}\hdots \lambda_{g-1} \vdash p}E_{\lambda_{0}}\otimes \cdots \otimes E_{\lambda_{g-1}}\otimes  W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}}$$

The $GL(V_{N_0})\times \cdots \times GL(V_{N_{g-1}})$ representation $W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}}$ is in a natural way also an $SL(2)$-representation. We can therefore decompose it into irreducible $SL(2)$-representation as follows:

$$W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}} \cong \bigoplus_{j}\mathrm{Hom}(V_j,W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}})\otimes V_j$$

Hence we find the following decomposition of $V$:

$$V \cong \bigoplus_{j}\left(\bigoplus_{\lambda_0\hdots \lambda_{g-1} \vdash p}E_{\lambda_0}\otimes \cdots \otimes E_{\lambda_{g-1}}\otimes  \mathrm{Hom}(V_j,W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}})\right)\otimes V_j$$

Note that we only allow $\lambda_k$ to have length $\leq N_k$. Comparing this decomposition with the isotypical decomposition [\[Isodec\]](#Isodec){reference-type="eqref" reference="Isodec"} for $q = 1$ we see that:

$$\label{Homdec}\mathrm{Hom}(V_j,V) \cong \bigoplus_{\lambda_0\hdots \lambda_{g-1} \vdash p}E_{\lambda_0}\otimes \cdots \otimes E_{\lambda_{g-1}}\otimes  \mathrm{Hom}(V_j,W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}})$$

The action of $D$ on this space is only on the $E_{\lambda_k}$. As above we write $D  = c_0\cdots c_{g-1}$ as a product of disjoint $p$-cycles and we note that the cycle $c_k$ acts in $E_{\lambda_k}$. If we define $R_{j,\lambda_0\hdots,\lambda_{g-1}}=\mathrm{dim}(\mathrm{Hom}(V_j,W_{\lambda_0}\otimes \cdots \otimes W_{\lambda_{g-1}}))$ and denote all $c_k$ by $c$ we have the following expression for the trace: $$\label{TrD}\mathrm{Tr}(D,\mathrm{Hom}(V_j,V)) =  \sum_{\lambda_0,\hdots \lambda_{g-1} \vdash p} \chi_{\lambda_0}(c)\cdots\chi_{\lambda_{g-1}}(c)\ R_{j,\lambda_0\hdots,\lambda_{g-1}}$$

Here $\chi_{\lambda}$ is the character of the symmetric group $S_p$. To calculate these traces we note that the dimensions $R_{j,\lambda_1\hdots,\lambda_g}$ are encoded in the following product expansion of Schur functions [@Macdonald]: $$\label{GenSchur}\prod_{k=0}^{g-1} s_{\lambda_k}(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1}) = \sum_{\mu \vdash p|\mathbf{N}|-s}R_{\mu_1-\mu_2+1,\lambda_0\hdots,\lambda_{g-1}}s_{\mu}(t,t^{-1})$$

The above condition on the direct sum in [\[Homdec\]](#Homdec){reference-type="eqref" reference="Homdec"} that the length of $\lambda_k$ is no more than $N_k$ is now incorporated into the Schur functions, because an $N$-variable Schur function $s_{\lambda}$ is nonzero only if $\lambda$ has no more than $N$ parts.

As a quick check that the above formula [\[GenSchur\]](#GenSchur){reference-type="eqref" reference="GenSchur"} includes all the dimensions $R$, note that $\lambda_k \vdash p$ and so the highest degree term of $s_{\lambda}(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1})$ is $t^{p N_k-p}$, hence $\mu \vdash p|\mathbf{N}|-s$ because the highest degree term of $s_{\mu}(t,t^{-1})$ is $t^{\mu_1}$. Note also that only length-two partitions $\mu$ contribute to the sum because the Schur functions $s_{\mu}$ have only two variables. In case $\mu = (\mu_1 \mu_2)$ we have $s_{\mu}(x,y) = \frac{x^{\mu_1+1}y^{\mu_2}-x^{\mu_2}y^{\mu_1+1}}{x-y}$ and $s_{\mu}(t,t^{-1}) = \frac{t^{\mu_1+1-\mu_2}-t^{-(\mu_1+1-\mu_2)}}{t-t^{-1}}$. The range of the summation in [\[GenSchur\]](#GenSchur){reference-type="eqref" reference="GenSchur"} therefore agrees exactly with the range of $j$ in the decomposition of the tensor product [\[Isodec\]](#Isodec){reference-type="eqref" reference="Isodec"}. From now on we will parametrize this range by two part partitions $\mu \vdash p|\mathbf{N}|-s$ and set $V_\mu = V_j$, where $j = \mu_1-\mu_2+1$.

Using the product of Schur functions in [\[GenSchur\]](#GenSchur){reference-type="eqref" reference="GenSchur"} as a generating function for the dimensions $R$ we can compute $\mathrm{Tr}(D,\mathrm{Hom}(V_{\mu},V))$ simultaneously for all $\mu$. First we sum the right hand side and the left hand side of equation [\[GenSchur\]](#GenSchur){reference-type="eqref" reference="GenSchur"} with the characters as in the sum in [\[TrD\]](#TrD){reference-type="eqref" reference="TrD"}:

$$\label{GenR}\sum_{\mu \vdash |\mathbf{N}|-s}\left(\sum_{\lambda_0,\hdots \lambda_{g-1} \vdash p} \chi_{\lambda_0}(c)\cdots\chi_{\lambda_{g-1}}(c)R_{\mu,\lambda_0\hdots,\lambda_{g-1}}\right)s_{\mu}(t,t^{-1}) =$$ $$\sum_{\lambda_0,\hdots\lambda_{g-1} \vdash p} \chi_{\lambda_0}(c)\cdots \chi_{\lambda_{g-1}}(c)\prod_{k=0}^{g-1} s_{\lambda_k}(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1}) =$$ $$\prod_{k=0}^{g-1} \sum_{\lambda_k\vdash p}\chi_{\lambda_k}(c)s_{\lambda_k}(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1}) =$$ $$\label{PowProd}\prod_{k=0}^{g-1}p_p(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1})$$

In the last line we used the expansion of the power sum function $p_p$ in terms of Schur functions [@Macdonald] p.114. We can use the notion of plethysm [@Macdonald] p.138 to write the power sums in terms of the complete symmetric functions $h$ as follows: $$p_p(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1}) = (p_p \circ h_{N_k-1})(t,t^{-1}) = h_{N_k-1}(t^p,t^{-p})$$

As with partitions we define $h_{\mathbf{N}-1} = \prod_{k=0}^{g-1}h_{N_k-1}$ so that we can write the above product [\[PowProd\]](#PowProd){reference-type="eqref" reference="PowProd"} as:

$$\label{HAnswer}\prod_{k=0}^{g-1}p_p(t^{N_k-1},t^{N_k-3},...,t^{-N_k+1})=h_{\mathbf{N}-1}(t^p,t^{-p})$$

Comparing equations [\[GenR\]](#GenR){reference-type="eqref" reference="GenR"} and [\[HAnswer\]](#HAnswer){reference-type="eqref" reference="HAnswer"} we see that to compute the traces in [\[TrD\]](#TrD){reference-type="eqref" reference="TrD"} we need to express $h_{\mathbf{N}-1}(t^p,t^{-p})$ in terms of the $s_{\mu}(t,t^{-1})$. The coefficients in this expansion will be our traces.

First we consider the case where $p=1$. Since we have $s = g$ there are $\left\lfloor (|\mathbf{N}|-g)/2\right\rfloor+1$ two part partitions $\mu \vdash |\mathbf{N}|-s$, that we will number by the half integers $w = (\mu_1-\mu_2)/2$. Since $h_{\mathbf{N}-1}(t,t^{-1})$ is a product of geometric series we can use the notation defined in the introduction to write: $h_{\mathbf{N}-1}(t,t^{-1}) =$ $$\label{P1geval}\sum_{w=(|\mathbf{N}|-g)/2-\left\lfloor (|\mathbf{N}|-g)/2\right\rfloor}^{(|\mathbf{N}|-g)/2}\left({g \choose w}_{\mathbf{N}}- {g \choose w+1}_{\mathbf{N}}\right)\frac{t^{2w+1}-t^{-2w-1}}{t-t^{-1}}$$

The above equation settles the case $p=1$ since the Schur functions are exactly the geometric series in the two variable case. We will come back to the $p=1$ case after we have found the coefficients for $p>1$. We will then show that these cases can be unified into a single cabling formula for the colored Jones polynomial.

From now on let's assume that $p\geq 2$. We will carry out the expansion of $h_{\mathbf{N}-1}(t^p,t^{-p})$ into two variable Schur functions in a little more generality by setting $x_1 = t$ and $x_2 = t^{-1}$. As a first step consider the following fundamental identity [@Macdonald] p.62 relating the complete symmetric functions to the Schur functions:

$$\label{FundId} \sum_{\lambda}h_{\lambda}(x)m_{\lambda}(y) = \prod_{i,j}(1-x_iy_j)^{-1}  = \sum_{\lambda}s_{\lambda}(x)s_{\lambda}(y)$$

Here $m_{\lambda}(y)$ is the monomial symmetric function and $x = (x_1,x_2,\hdots)$ and the sums range over all partitions $\lambda$. The first part of the identity [\[FundId\]](#FundId){reference-type="eqref" reference="FundId"} implies that $h_{\mathbf{N}-1}(x_1^p,x_2^p)$ is the coefficient of $\mathbf{y}^{p(\mathbf{N}-1)} = y_0^{p (N_0-1)}\cdots y_{g-1}^{p (N_{g-1}-1)}$ in the expansion of the product $\prod_{k=0}^{g-1}(1-x_1^py_k^p)^{-1}(1-x_2^py_k^p)^{-1}$. Factoring we can also write this product as $\prod_{k=0}^{g-1}\prod_{u=0}^{p-1}(1-x_1\omega^u y_k)^{-1}(1-x_2\omega^u y_k)^{-1}$, where $\omega = \exp(2\pi i/p)$. Using the second half of the identity [\[FundId\]](#FundId){reference-type="eqref" reference="FundId"} we can expand the same product into two variable Schur functions: $$\prod_{k=0}^{g-1}\prod_{u=0}^{p-1}(1-x_1\omega^u y_k)^{-1}(1-x_2\omega^u y_k)^{-1} = \sum_{\mu}s_{\mu}(y_0,\omega y_0,\hdots,\omega^{p-1} y_{g-1})s_{\mu}(x_1,x_2)$$

Taking the coefficient of $\mathbf{y}^{p(\mathbf{N}-1)}$ on the left gives $h_{\mathbf{N}-1}(x_1^p,x_2^p)$ back, while the coefficient of $\mathbf{y}^{p(\mathbf{N}-1)}$ on the right hand side is $\sum_\mu K_{\mu}s_{\mu}(x_1,x_2)$, where $K_\mu$ is the coefficient of $\mathbf{y}^{p(\mathbf{N}-1)}$ in $s_{\mu}(y_0,\omega y_0,\hdots,\omega^{p-1} y_{g-1})$. It follows that the trace we wanted to calculate is equal to this coefficient: $\mathrm{Tr}(D,\mathrm{Hom}(V_{\mu},V)) =  K_{\mu}$.

We proceed with the calculation of $K_{\mu}$. By [@Macdonald] p.72 we can expand the Schur function $s_{\mu}(y_0,\omega y_0,\hdots,\omega^{p-1} y_{g-1})$ in terms of skew Schur functions making it possible to extract the powers of $y_j$. $$s_{\mu}(y_0,\omega y_0,\hdots,\omega^{p-1} y_{g-1}) = \sum \prod_{j = 0}^{g-1} y_j^{|\nu^{(j)}-\nu^{(j-1)}|}s_{\nu^{(j)}/\nu^{(j-1)}}(1,\omega,\hdots,\omega^{p-1})$$

The sum ranges over all sequences of partitions $0 = \nu^{(0)}\subset \nu^{(1)} \hdots \subset \nu^{(g)} = \mu$. Only the sequences of partitions satisfying $|\nu^{(j)}-\nu^{(j-1)}| = p(N_j-1)$ contribute to the coefficient of $\mathbf{y}^{p(\mathbf{N}-1)}$ in this sum. The contribution of such a sequence is $\prod_{j = 0}^{g-1} s_{\nu^{(j)}/\nu^{(j-1)}}(1,\omega,\hdots,\omega^{p-1})$. In the cases we are interested in $\mu$ has length $2$ and it follows from [@Macdonald] p.91 that this contribution is zero unless $\nu^{(j)}$ can be obtained from $\nu^{(j-1)}$ by attaching $N_j-1$ border strips of length $p$. A set theoretical difference between two nested partitions is called a border strip of length $p$ if it is connected, does not contain any $2\times 2$ squares and has $p$ elements. If this is the case for all $j$, then the contribution is $\sigma_p(\mu) = (-1)^{r_2}$, where $0\leq r_2<p$ is the residue of $\mu_2$ modulo $p$.

The above argument shows that $K_{\mu} = \sigma_p(\mu)|K_{\mu}|$, and that $|K_{\mu}|$ is the number of sequences of partitions $0 = \nu^{(0)}\subset \nu^{(1)} \hdots \subset \nu^{(g)} = \mu$ satisfying the condition that $\nu^{(j)}$ is obtained from $\nu^{(j-1)}$ by attaching $N_j-1$ border strips of length $p$.

To count the number of such sequences we first look a all ways of constructing two part partitions by attaching length $p$-border strips, starting with the empty partition. One notices that the lower leftmost corner of a new border strip can be attached at exactly two places: either the end of the first row or the end of the second row. It follows that we can list all possibilities in a Pascal-like triangle, see figure 3.

<figure>
<div class="center">
<embed src="Pascal2.eps" />
</div>
<figcaption>The Pascal-like triangle of all two part partitions that can be glued from <span class="math inline">5</span> or less border strips of length <span class="math inline"><em>p</em> = 4</span>.</figcaption>
</figure>

The $k$-th row of our Pascal triangle contains $k+1$ partitions that we index by the half integers $\frac{-k}{2},\frac{-k}{2}+1,\hdots,\frac{k}{2}$. The triangle is ordered such that if $\mu$ has index $w(\mu) = w$ then $\mu_1-\mu_2+1 = \mathrm{sgn}(w)(2wp+1)$ and $\mathrm{sgn}(w) = \sigma_p(\mu)$, provided that we agree that $\mathrm{sgn}(0)=1$.

Interpreting $|K_{\mu}|$ in terms of the Pascal triangle we see that $|K_{\mu}|$ is equal to the number of ways to move from the (empty) top of the triangle to $\mu \vdash p|\mathbf{N}|-s$ in $g$ steps of length ${N_k}-1$, for $k = 0\hdots,g-1$. A step of length $A$ can go in $A+1$ directions that are conveniently indexed by $\frac{-A}{2},\frac{-A}{2}+1,\hdots,\frac{A}{2}$. The sum of these indices must be the index of $\mu$, that is $w$. Therefore the number of ways is exactly the coefficient of $x^w$ in the product $\prod_{k=0}^{g-1}(x^{-\frac{N_k-1}{2}}+x^{-\frac{N_k-1}{2}+1}+\hdots+x^{\frac{N_k-1}{2}})$. Using the notation defined in the introduction we see that $|K_{\mu}| = {g \choose w}_{\mathbf{N}}$ and so $K_{\mu} = \mathrm{sgn}(w){g \choose w}_{\mathbf{N}}$.

We can now summarize the calculation of $J = J_{M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_c}(L^r_{i;s})$ as follows. First we expressed it in equation [\[JIs\]](#JIs){reference-type="eqref" reference="JIs"} as a sum over the colors $j$ of a trace times the colored Jones of the uncabled link. In [\[BD\]](#BD){reference-type="eqref" reference="BD"} the dependence on $q$ was extracted and finally the rest of the trace was shown to be given by the coefficients in equation [\[P1geval\]](#P1geval){reference-type="eqref" reference="P1geval"} for $p=1$ and by $K_\mu$ for $p\geq 2$. Along the we changed the sum over colors into a sum over two part partitions $\mu$, via $j = \mu_1-\mu_2+1$. We just saw that we can enumerate the $\mu$ for which $K_\mu$ is nonzero by the half integers $w$. Combining all this we find for $p\geq 2$: $J_{M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_c}(L^r_{i;s})=$ $$\sum_{w=-(|\mathbf{N}|-g)/2}^{(|\mathbf{N}|-g)/2}q^{\frac{rwp(wp+1)}{s}}\mathrm{sgn}(w){g \choose w}_{\mathbf{N}}J_{M_1,\hdots,M_{i-1},|2wp+1|,\hdots,M_c}(L)$$

Remarkably this formula is also valid for $p=1$. In this case the non-negative $w$ run through all partitions and both $w$ and $-(w+1)$ contribute to the same term $J_{M_1,\hdots,M_{i-1},|2w+1|,\hdots,M_c}(L)$, thus producing the coefficients found in [\[P1geval\]](#P1geval){reference-type="eqref" reference="P1geval"}.

Finally the convention $J_{M_1,\hdots,M_{i-1},-k,\hdots,M_c} = -J_{M_1,\hdots,M_{i-1},k,\hdots,M_c}$ allows us to incorporate the sign into the colored Jones polynomial because $\mathrm{sgn}(w) = \mathrm{sgn}(2wp+1)$. Noting that $p = s/g$ the proof of theorem 1 is complete.
