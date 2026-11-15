---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-001-knot-invariants-knot-homologies-and-lmov-conject
section_title: "Knot invariants, knot homologies, and LMOV conjecture"
section_number: null
pages: 2-3
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.959
doc_brief: "BPS states, knots and quivers — 7 sections: Front matter; BPS states, knots and quivers; Knot invariants, knot homologies"
---
Ever since its birth knot theory attracted attention of physicists, and various knot invariants turned out to have physical interpretation.

In particular various knot polynomials have been reinterpreted as expectation values in Chern-Simons theory in [@Witten_Jones], and subsequently they were expressed in terms of topological string theory amplitudes [@Witten:1992fb]. In [@OoguriV] the topological string setup was related to M-theory and it was argued, that colored HOMFLY-PT polynomials are encoded in LMOV invariants, which count bound states of open M2-branes with M5-branes. In this work we show, among others, how -- so far conjectural -- integrality of these invariants can be proven.

Furthermore, more recently homological knot invariants, such as Khovanov homology and its more involved cousins [@Khovanov; @KhR1; @KhR2], have been also realized in brane systems in string theory, also revealing yet to be proved new properties of those invariants [@GSV; @DGR; @Gukov:2011ry]. In what follows we show that certain information about homological knot invariants is also encoded in quiver moduli spaces.

Let us introduce first the generating function of $S^r$-colored HOMFLY-PT polynomials, which will be the main object of the subsequent analysis, as well as corresponding LMOV invariants. To start with consider the Ooguri-Vafa generating function [@OoguriV; @Labastida:2000zp; @Labastida:2000yw; @Labastida:2001ts] $$Z(U,V) = \sum_R  \textrm{Tr}_R U \, \textrm{Tr}_R V = \exp\Big(  \sum_{n=1}^{\infty} \frac{1}{n} \textrm{Tr} U^n \textrm{Tr} V^n \Big),   \label{ZUV}$$ where $U=P\,\exp\oint_K A$ is the holonomy of $U(N)$ Chern-Simons gauge field along a knot $K$, $V$ plays a role of a source, and the sum runs over all representations $R$, i.e. all two-dimensional partitions. The LMOV conjecture states that the expectation value of ([\[ZUV\]](#ZUV){reference-type="ref" reference="ZUV"}) takes form $$\begin{aligned}
\big\langle Z(U,V) \big\rangle &= \sum_R \overline{P}_{R}(a,q) \textrm{Tr}_R V  = \nonumber \\
&= \exp \Big(  \sum_{n=1}^\infty \sum_R \frac{1}{n} f_{R}(a^n,q^n) \textrm{Tr}_R V^n  \Big),    \label{ZUVvev}
\end{aligned}$$ where the expectation value of the holonomy is identified with the unreduced HOMFLY-PT polynomial of a knot $K$, $\langle \textrm{Tr}_R U \rangle = \overline{P}_{R}(a,q)=P_R^{\bf 0_1} P_R(a,q)$ (where $P_R^{\bf 0_1}$ is the unknot factor), and the functions $$f_{R}(a,q) = \sum_{i,j} \frac{N_{R,i,j} a^i q^j}{q-q^{-1}}  \label{fR}$$ encode conjecturally integer LMOV (or Ooguri-Vafa) invariants $N_{R,i,j}$, counting bound states of M2-branes ending on M5-branes. These functions take form of universal polynomials in colored HOMFLY-PT polynomials.

In what follows we consider one-dimensional source $V=x$. In this case $\textrm{Tr}_R V \neq 0$ only for symmetric representations $R=S^r$, so that $\textrm{Tr}_{S^r}(x) = x^r$. Let us denote $P(x)=\langle Z(U,x) \rangle$, and let $\overline{P}_{r}(a,q)$ denote the $S^r$-colored HOMFLY-PT polynomial of $K$, so that ([\[ZUVvev\]](#ZUVvev){reference-type="ref" reference="ZUVvev"}) takes form $$P(x) = \sum_{r=0}^\infty \overline{P}_{r}(a,q) x^r =   
e^{\sum_{r,n\geq 1} \frac{1}{n} f_{r}(a^n,q^n)x^{n r}}.
\label{Pz2}$$

In this case $f_r(a,q)\equiv f_{S^r}(a,q) = \sum_{i,j} \frac{N_{r,i,j} a^i q^j}{q-q^{-1}}$, for $N_{r,i,j}\equiv N_{S^r,i,j}$, are polynomials in $\overline{P}_{d_1}(a^{d_2},q^{d_2})$ for some $d_1$ and $d_2$ (such that $d_1 d_2\leq r$), e.g. $f_1(a,q) = \overline{P}_1(a,q)$, $$f_2(a,q) =  \overline{P}_2(a,q) - \frac{1}{2} \overline{P}_1(a,q)^2 -\frac{1}{2}  \overline{P}_1(a^2,q^2),$$ etc. It follows that ([\[Pz2\]](#Pz2){reference-type="ref" reference="Pz2"}) can be rewritten in product form $$P(x) = \prod_{r\geq 1;i,j;k\geq 0} \Big(1 - x^r a^i q^{j+2k+1} \Big)^{N_{r,i,j}} .
\label{Pr-LMOV}$$ Integrality of BPS degeneracies $N_{r,i,j}$ encoded in this product is one important outcome of our work.

Another outcome of our work is a surprising relation of colored HOMFLY-PT polynomials, or their generating function ([\[Pz2\]](#Pz2){reference-type="ref" reference="Pz2"}), to superpolynomials, i.e. the Poincaré polynomials of the uncolored HOMFLY-PT homologies of knots [@DGR]. More generally, one can consider colored HOMFLY-PT homology $\mathcal{H}^{S^r}_{i,j,k}$ that has not been defined rigorously by mathematicians, however its conjectural (reduced) colored superpolynomial $$P_r (a,q,t) = \sum_{i,j,k} \, a^i q^j t^k \, \dim \mathcal{H}^{S^r}_{i,j,k}   \label{P_r-aqt}$$ can be very effectively computed for various families of knots, using the formalism of differentials [@DGR; @Rasmussen-differentials; @Gukov:2011ry; @Gukov:2015gmm]. Note that generalizations of the LMOV conjecture to the case of superpolynomials have been considered in [@Garoufalidis:2015ewa; @Kameyama:2017ryw].

For example, for trefoil knot $3_1$, eq. ([\[P_r-aqt\]](#P_r-aqt){reference-type="ref" reference="P_r-aqt"}) takes form [@FGSS] $$P_r(a,q,t)=  \frac{a^{2r}}{q^{2r}}\sum_{k=0}^r {r \brack k} q^{2k(r+1)} t^{2k} \prod_{i=1}^k  (1+a^2q^{2(i-2)}t), \label{Pr-31}$$ where ${r \brack k} = \frac{(q^2;q^2)_r}{(q^2;q^2)_k(q^2;q^2)_{r-k}}$, and the $q$-Pochhammer symbol is defined as $(z;q)_n=\prod_{i=0}^{n-1} (1-zq^i)$. For $t=-1$ ([\[Pr-31\]](#Pr-31){reference-type="ref" reference="Pr-31"}) specializes to the reduced colored HOMFLY-PT polynomial, while in the uncolored ($r=1$) case it reduces to $$P_1(a,q,t) = \frac{a^2}{q^2} + a^2 q^2 t^2 + a^4 t^3.   \label{P1-31}$$ The monomials in this expression correspond to generators of the HOMFLY-PT homology, and powers of $t$ in each monomial -- in this example taking values $(0,2,3)$ -- are referred to as homological degrees.
