---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-010-42-unitary-normalization
section_title: "Unitary normalization"
section_number: 4.2
pages: 11-12
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.979
---
The expressions \rf{s-channel} and \rf{t-channel} strongly suggest to 
redefine the conformal blocks by absorbing the three-point functions
$C(\al_3,\al_2,\al_1)$ into the definition, 
\begin{equation}\label{Blnorm}\begin{aligned}
\CG_{\al_s}^{(s)}(A|Z):= 
\big(C(\al_4,\al_3,\al_s)C(Q-\al_s,\al_2,\al_1)\big)^{\frac{1}{2}}
\CF_{\al_s}^{(s)}(A|Z)\,,\\
\CG_{\al_t}^{(t)}(A|Z):= 
\big(C(\al_4,\al_t,\al_1)C(Q-\al_t,\al_3,\al_2)\big)^{\frac{1}{2}}
\CF_{\al_t}^{(t)}(A|Z)\,.
\end{aligned}
\end{equation}
This corresponds to normalizing the conformal blocks associated to the
three-punctured sphere in such a way that their scalar product is
always unity. This normalization may be called the unitary
normalization. We then have
\begin{align}
& \left\langle\, V_{\al_4}(z_4,\bz_4) V_{\al_3}(z_3,\bz_3)
V_{\al_2}(z_2,\bz_2)V_{\al_1}(z_1,\bz_1)\,\right\rangle
=\\ 
&\qquad
=\int_{\frac{Q}{2}+\textup{i}\BR}d\al_s\;
\CG_{\al_s}^{(s)}(A|Z)\CG_{\al_s}^{(s)}(A|\bar{Z})
=\int_{\frac{Q}{2}+\textup{i}\BR}d\al_t\;
\CG_{\al_t}^{(t)}(A|Z)\CG_{\al_t}^{(t)}(A|\bar{Z})\,,
\notag\end{align}
the second equation being a consequence of the unitarity of the 
change of basis
\begin{equation}\label{fusionL}
\CG_{\al_s}^{(s)}(A|Z)\,=\,\int_{{Q/2}+\textup{i}\BR} d\al_t\;
G_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,
\CG_{\al_t}^{(t)}(A|Z)\,.
\end{equation}
The normalized fusion coefficients $G_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]$ 
are related to the $F_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]$ as
\begin{equation}\label{GvsF}
G_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,=\,
\textstyle{ \sqrt{
\frac{C(\al_4,\al_3,\al_s)C(Q-\al_s,\al_2,\al_1)}
{C(\al_4,\al_t,\al_1)C(Q-\al_t,\al_3,\al_2)}}}\,
F_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,.
\end{equation}
The fusion coefficients $G_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]$ 
have a simple expression in terms of the b-$6j$ symbols,
\begin{equation} \label{eq2}
G_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,=\,
\left({M(\al_t)}{M(\al_s)}\right)^{\frac{1}{2}}
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\al_4}\,{}^{\al_s}_{\al_t}\big\}_b^{}
\,.


\end{equation}
Indeed, formula \rf{eq2} is a straightforward consequence of
equations \rf{GvsF}, \rf{FvsRW} and \rf{norm} above.


\subsection{6j symbols of ${\rm Diff}(S^1)$}

It is known that Liouville theory is deeply related to the 
representation theory of the group ${\rm Diff}(S^1)$ of diffeomorphisms
of the unit circle \cite{T08}. The operator product expansion from conformal 
field theory leads to the definition of a suitable generalization of 
the tensor product operation for representations of infinite-dimensional
groups like ${\rm Diff}(S^1)$. One may therefore 
interpret the chiral vertex-operators
from conformal field theory as analogs of the Clebsch-Gordan
maps, and the fusion coefficients as analog of $6j$-symbols 
\cite{MS,Teschner:2001rv,T08}. 

A similar issue arises here as pointed out above in our discussion 
of the modular double: To find particularly natural normalization
conditions. The normalization defined in \rf{Blnorm} above, while
being
natural from the physical point of view,
is not a direct counterpart of the normalization condition
used to define the $6j$ symbols of the modular double above.
Such a normalization condition can naturally be defined by 
requiring invariance under the Weyl-reflections $\al_i\ra Q-\al_i$.
Due to the factors $\Upsilon(2\al_i)$ 
in the definition of $C(\al_3,\al_2,\al_1)$, 
the  symmetry under  $\al_i\ra Q-\al_i$
is spoiled by the change of normalization  
\rf{Blnorm}.

However, it is easy to restore this symmetry by replacing the
normalization factor $C(\al_3,\al_2,\al_1)$ entering the
definition \rf{Blnorm} by 
\begin{align}
D(\al_1 &,\al_2,\al_3)  = \frac{|\Ga_b(2\al_1)\Ga_b(2\al_2)\Ga_b(2\al_3)|^{-2}}
{\Upsilon(2\al_1)\Upsilon(2\al_2)\Upsilon(2\al_3)}C(\al_3,\al_2,\al_1)\,.
\notag\end{align}
Replacing $C$ by $D$ in \rf{Blnorm} leads to the definition
of normalized conformal blocks $\CK_{\al_s}^{(s)}(A|Z)$
and $\CK_{\al_t}^{(t)}(A|Z)$ which can be interpreted as analogs of 
invariants in tensor products of four representations of
${\rm Diff}(S^1)$. The kernel appearing in the relation  
\begin{equation}
\CK_{\al_s}^{(s)}(A|Z)\,=\,\int_{{Q/2}+\textup{i}\BR} d\mu(\al_t)\;
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\al_4}\,
{}^{\al_s}_{\al_t}\big\}_{\rm Diff(S^1)}^{}
\CK_{\al_t}^{(t)}(A|Z)\,.
\end{equation}
is naturally interpreted as an analog of
the $6j$ symbols for ${\rm Diff}(S^1)$. It coincides exactly with the
b-$6j$ symbols, 
\begin{equation} \label{eq3}
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\al_4}\,
{}^{\al_s}_{\al_t}\big\}_{\rm Diff(S^1)}^{}
\,=\,
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\al_4}\,{}^{\al_s}_{\al_t}\big\}_b^{}
\,.
\end{equation}
as can easily be checked by straightforward calculations.
