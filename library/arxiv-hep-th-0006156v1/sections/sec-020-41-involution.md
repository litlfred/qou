---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-020-41-involution
section_title: "Involution"
section_number: 4.1
pages: 11-12
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
The formal quantization of section [\[sec:fquant\]](#sec:fquant){reference-type="ref" reference="sec:fquant"} can be put in the usual framework of quantum mechanics if we assume that both the formal parameter $q$ and the generators $\chi$ are exponentials $$q=e^{\pi i\tau}\qquad\qquad
\chi_j=e^{-2\pi\sqrt\tau\varphi_j},$$ and the new generators $\varphi_j$ have the commutation relations $$[\varphi_{2n\pm1},\varphi_{2n}]=-\tfrac{I}
{2\pi i}\qquad\qquad[\varphi_j,\varphi_i]=0 \mbox{ if
  }|j-i|\not\equiv1\pmod{N}$$ independent of $\tau$, and so could be taken as selfadjoint operators $$\varphi_j^\dagger=\varphi_j^{} .$$ The rest depends on $\tau$ of course. If the established formula $$c=1+6(\tau+\tfrac1{\displaystyle\tau}+2)$$ (relating the coupling constant of the continuous Liouville field theory to the central charge of the corresponding representation of the Virasoro algebra) has something to do with our lattice theory, then three cases have to be considered: a) $c\leq1\leftrightarrow\tau<0$; b) $c\geq25\leftrightarrow\tau>0$; and c) $1\leq c\leq25\leftrightarrow|\tau|=1$. The first two, although lead to pretty normal reality conditions $\chi_j^\dagger=\chi_j^{-1}$ and $\chi_j^\dagger=\chi_j^{}$ respectively, also put $q$ on the unit circle, which is the last thing we want right now. That leaves c).

## Change of function $\epsilon$ 

So, $|\tau|=1$, also, since $c$ does not distinguish between $\tau$ and $1/\tau$, let for definiteness $\Im\tau>0$. Following [@faddeev95], consider the function $$\label{eq:fofz}
f(z)=e_{\sqrt\tau}(iz/\sqrt\tau
)=\frac{(-e^{2\pi i(z+\frac\tau2)};
  e^{2\pi i\tau})_\infty} {(-e^{\frac{2\pi i}\tau(z-\frac12)};
  e^{-\frac{2\pi i}\tau})_\infty} \; ,$$ which uses our former favourite $\epsilon$ as the numerator but divides it by itself but with suitably altered arguments. In Appendix we collect some of the properties of this function. Here we remark in particular that $f(z)$ satisfies the same functional equation $$\label{fe}
   \frac{f(z+\frac\tau2)}{f(z-\frac\tau2)}
   =\frac1{1+e^{2\pi i\tau z}}$$ as $\epsilon(e^{2\pi iz})$ did, but this time we also have $$|f(z)|=1$$ on the line $z=\tau\bar{z}$, simply because the numerator and denominator of $f$ are complex conjugate of each other on that line. There is an easy profit to be had from that.
