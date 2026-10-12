---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-018-61-two-commuting-complex-structures-on-o
section_title: "Two commuting complex structures on O"
section_number: 6.1
pages: 21-22
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
---
We have already introduced the complex structures $J,\tilde{J}$ on ${\mathbb O},\tilde{{\mathbb O}}$ in sections [\[sec:spin7\]](#sec:spin7){reference-type="ref" reference="sec:spin7"}, [\[sec:spin43\]](#sec:spin43){reference-type="ref" reference="sec:spin43"}. They extend to two commuting complex structures on ${\mathbb O}\times \tilde{{\mathbb O}}$.

Let us describe the commutant of $J,\tilde{J}$ acting on ${\mathbb O}\times \tilde{{\mathbb O}}$ in ${\mathfrak so}(11,3)$. A part of the commutant lives in ${\mathfrak so}(7)\oplus{\mathfrak so}(4,3)$ subalgebra. This is the already described ${\mathfrak so}(6)\subset{\mathfrak so}(7)$ and ${\mathfrak so}(3)\oplus {\mathfrak so}(1,3)\subset{\mathfrak so}(4,3)$. But there are more transformations in the commutant. Indeed, it is easy to see that the generators $E^4\otimes \tilde{E}^i, i=1,2,3$ commute with both $J=E^4$ and $\tilde{J}=-\tilde{E}^1\tilde{E}^2\tilde{E}^3$. These 3 additional generator extend ${\mathfrak so}(3)$ into ${\mathfrak so}(4)$ rotating the directions $e^4, e^{\tilde{1}}, e^{\tilde{2}}, e^{\tilde{3}}$.

All in all, we see that the commutant of $J,\tilde{J}$ in ${\rm Spin}(11,3)$ is $$\begin{aligned}
G_{J,\tilde{J}} = {\rm SU}(4)\times{\rm SU}(2)_L\times {\rm SU}(2)_R \times {\rm Spin}(1,3),
\end{aligned}$$ i.e., the product of the Pati-Salam and Lorentz groups. We are not careful here about the possible discrete subgroups that are in the kernel of the embedding of this direct product into ${\rm Spin}(11,3)$, as this is of no interest to us in the present paper.

An even more interesting case is that of the commutant of $J'=R_u$ and $\tilde{J}$. The complex structure $J'$ breaks ${\rm SU}(4)$ to ${\rm SU}(3)\times {\rm U}(1)_{B-L}$. Thus, we get $$\begin{aligned}
\label{LR-Lorentz}
G_{J',\tilde{J}} = {\rm SU}(3)\times{\rm U}(1)_{B-L}\times {\rm SU}(2)_L\times {\rm SU}(2)_R \times {\rm Spin}(1,3),
\end{aligned}$$ which is the product of the left/right symmetric ([\[GLR\]](#GLR){reference-type="ref" reference="GLR"}) and Lorentz groups.

## Identification with particles

The complex structure $J$ splits ${\mathbb O}$ into its $(1,0),(0,1)$ subspaces, each of them being a copy of ${\mathbb C}^4$. Moreover, there is a preferred copy of ${\mathbb C}$, arising as the one spanned by ${\mathbb I}, u \in {\mathbb O}$. This is where leptons will live. Similarly, the complex structure $\tilde{J}$ splits $\tilde{{\mathbb O}}$ into its $(1,0), (0,1)$ subspaces. We know that each of these describes Lorentz 2-component spinors of the same chirality. As in all GUT discussions, we can concentrate on only one of these spaces, thus describing the particle content using Lorentz spinors of the same chirality.

Putting all of this together, we see that ${\mathbb O}\times\tilde{{\mathbb O}}$ splits as $$\begin{aligned}
\label{S-split}
{\mathbb O}\times\tilde{{\mathbb O}} = L \oplus Q \oplus \bar{L} \oplus \bar{Q}.
\end{aligned}$$ The first two terms here are in the $(1,0)$ subspace of $J$, the second two are in the $(0,1)$ eigenspace. Each of these spaces is also a fundamental representation of ${\rm SU}(2)\subset{\rm Spin}(4,3)$, and a Lorentz spinor. Concentrating on the $(1,0)$ eigenspace of $\tilde{J}$ selects 2-component Lorentz spinors of the same chirality. Thus, the projection of every term in ([\[S-split\]](#S-split){reference-type="ref" reference="S-split"}) onto the $(1,0)$ eigenspace of $\tilde{J}$ gives a fundamental representation of ${\rm SU}(2)$ that is also a 2-component Lorentz spinor.

It is clear that the $Q,\bar{Q}$ factors in ([\[S-split\]](#S-split){reference-type="ref" reference="S-split"}) transform as the fundamental and anti-fundamental representation of ${\rm SU}(3)\subset{\rm Spin}(6)\subset{\rm Spin}(7)$, and that all factors in ([\[S-split\]](#S-split){reference-type="ref" reference="S-split"}) are charged with respect to the ${\rm U}(1)_{B-L}$, with the assignment of charges being as in ([\[charges\]](#charges){reference-type="ref" reference="charges"}). It remains to understand the transformation properties of the factors with respect to ${\rm SU}(2)_L\times{\rm SU}(2)_R$.

The general element of the Lie algebra ${\mathfrak so}(4)$ is given by $$\begin{aligned}
 \frac{1}{2} a^i \epsilon^{ijk} \tilde{E}^j\tilde{E}^k + b^i E^4 \otimes \tilde{E}^i.
\end{aligned}$$ This splits into two commuting ${\mathfrak su}(2)$ subalgebras as $$\begin{aligned}
\frac{1}{2}(a^i -b^i) \left( \frac{1}{2}  \epsilon^{ijk} \tilde{E}^j\tilde{E}^k - E^4 \otimes \tilde{E}^i  \right) 
+\frac{1}{2}(a^i +b^i) \left( \frac{1}{2}  \epsilon^{ijk} \tilde{E}^j\tilde{E}^k + E^4 \otimes \tilde{E}^i  \right) .
\end{aligned}$$ Let us name the first of these two factors as ${\mathfrak su}(2)_L$, and the second as ${\mathfrak su}(2)_R$. On the $(1,0)$ eigenspace of $\tilde{J}=-\tilde{E}^1\tilde{E}^2\tilde{E}^3$ we have $\tilde{E}^1\tilde{E}^2={\rm i\,}\tilde{E}^3$, and so on this subspace the splitting into the two ${\mathfrak su}(2)$ factors becomes $$\begin{aligned}
\frac{1}{2}(a^i -b^i) \left( {\rm i\,}\tilde{E}^i- E^4 \otimes \tilde{E}^i  \right) 
+\frac{1}{2}(a^i +b^i) \left( {\rm i\,}\tilde{E}^i+ E^4 \otimes \tilde{E}^i  \right) .
\end{aligned}$$ Note that the signs in brackets are reversed onto the $(0,1)$ subspace of $\tilde{J}$. It is now clear that the two eigenspaces of $J=E^4$ transform as $(2,1)$ and $(1,2)$ representations of ${\rm SU}(2)_L\times{\rm SU}(2)_R$. Indeed, on the $(1,0)$ eigenspace of $J$ we can replace $E^4$ by its eigenvalue $-{\rm i\,}$. This makes it clear that this subspace is a singlet with respect to ${\rm SU}(2)_R$. Similarly, the operator $E^4$ has eigenvalue $+{\rm i\,}$ on the $(0,1)$ eigenspace, which makes it clear that it is a singlet with respect to ${\rm SU}(2)_L$. All in all, we get precisely the assignment of representations as in ([\[charges\]](#charges){reference-type="ref" reference="charges"}).

It remains to understand the assignment of particles into doublets of the two different ${\rm SU}(2)$. The choice of such assignment for the sector that transforms as the doublet of ${\rm SU}(2)_L$ is a convention. And so we name the components of doublets of ${\rm SU}(2)_L$ as in ([\[fermions\]](#fermions){reference-type="ref" reference="fermions"}). These transform as 2-component columns $\chi_L\to U_L \chi_L, U_L\in{\rm SU}(2)_L$. The correct assignment for the right doublets can only be motivated by the Dirac mass terms that couple the left and right sectors. The choices made in ([\[Phi\]](#Phi){reference-type="ref" reference="Phi"}), ([\[Phi-Y\]](#Phi-Y){reference-type="ref" reference="Phi-Y"}) motivate the assignments as in ([\[fermions\]](#fermions){reference-type="ref" reference="fermions"}).
