---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-018-54-quantization-of-fenchel-nielsen-coordinates
section_title: "Quantization of Fenchel-Nielsen coordinates"
section_number: 5.4
pages: 16-17
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.985
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The main observation we want to make here may be summarized in the
following two statements:

\noindent
{\it 1) The geodesic
length operators can be represented in terms of the quantized
Fenchel-Nielsen coordinates as follows:
\begin{subequations}\begin{align}
\pi_s^{\rm can}(\CL_s)\,=\,& 2\cosh(\sll_s/2)\,,\\
\pi_s^{\rm can}(\CL_t)\,=\,&\frac{1}{ 2(\cosh \sll_s - \cos 2\pi b^2)}
\Big(2\cos\pi b^2(L_2L_3+L_1L_4)+
\SL_s (L_1L_3+L_2L_4)\Big)\nonumber\\ \label{quantum't Hooft}
& \quad +  \frac{1}{\sqrt{2\sinh(\sll_{s}/2)}}
{e^{+\sk_s/2}}
\frac{\sqrt{c_{12}(\SL_s)c_{34}(\SL_s)}}{2\sinh(\sll_s/2)}
{e^{+\sk_s/2}}
\frac{1}{\sqrt{2\sinh(\sll_s/2)}}\\[-.5ex]
& \quad +  \frac{1}{\sqrt{2\sinh(\sll_s/2)}}
{e^{-\sk_s/2}}
\frac{\sqrt{c_{12}(\SL_s)c_{34}(\SL_s)}}{2\sinh(\sll_s/2)}
{e^{-\sk_s/2}}
\frac{1}{\sqrt{2\sinh(\sll_s/2)}}\,,
\notag
\end{align}
\end{subequations}
where $\SL_s=2\cosh(\sll_s/2)\equiv\pi_s(\CL_s)$ and $c_{ij}(L_s)$
was defined in \rf{cijdef}. 
The formulae defining the other representations $\pi_t$ and $\pi_u$
are obtained by simple permutations of indices.

\noindent 2)
The kernel describing the transition between representation $\pi_s$ and 
$\pi_t$ is given in terms of the b-$6j$ symbols as 
\begin{equation} \label{Avs6j}
A_L^{st}(l_s,l_t)
\,=\,
\left({{M(\al_t)}{M(\al_s)}}\right)^{\frac{1}{2}}

\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\al_4}\,{}^{\al_s}_{\al_t}\big\}_b^{}
\,\quad{\rm if}\quad \al_i=\frac{Q}{2}+\textup{i}\frac{l_i}{4\pi b}\,,
\end{equation}
for $i=1,2,3,4,s,t$. The formulae for other pairs of representations
are again found by permutations of indices.
}


The relations between Liouville theory and quantum Teichm\"uller theory
found in \cite{Teschner:2003at} allow one to 
shortcut the forthcoming self-contained derivation \cite{TV}
of the claims above.
In \cite{Teschner:2003at} it was found in particular that the conformal blocks 
$\CF_{\al_s}^{(s)}(A|Z)$ represent particular wave-functions 
in some
representation $\pi_s^{\rm Liou}$,
\begin{equation}
\psi_s(l_s)\,=\,\CF_{\al_s}^{(s)}(A|Z)\quad{\rm if}\quad
\al_s=\frac{Q}{2}+\textup{i}\frac{l_s}{4\pi b}\,.
\end{equation}
This relation fixes a specific representation $\pi_s^{\rm Liou}$.
The generator
$\CL_t$ is represented in $\pi_s^{\rm Liou}$ as in \rf{Diffop} with
coefficients $D_\ep^{\rm Liou}(l_s)$ that can be extracted from 
\cite{AGGTV,DGOT}\footnote{Our generator
$\CL_t$ corresponds to $2\cos(\pi bQ)\CL(\ga_{2,0})$ in \cite{DGOT}.}.











Redefining the conformal blocks as in \rf{Blnorm}
is equivalent
to a gauge transformation \rf{gauge}
which transforms the representation 
$\pi_s^{\rm Liou}$ to the 
representation denoted $\pi_s^{\rm can}$. 
It is straightforward to  
calculate the coefficients $D_{\ep}(l_s)$ from 
$D_\ep^{\rm Liou}(l_s)$ using \rf{Blnorm} and 
\rf{DOZZ}. A related observation was recently made in \cite{IOT}. 
The case of the one-holed torus was discussed along similar lines in 
\cite{DiGu}.

Other normalizations for the b-$6j$ symbols will 
correspond to different choices of Darboux-coordinates. In 
the normalization used in \cite{DGOT}, for example, one would find
\begin{subequations}
\begin{align}
\pi_s'(\CL_t)\,=\,&\frac{1}{ 2(\cosh \sll_s - \cos 2\pi b^2)}
\Big(2\cos\pi b^2(L_2L_3+L_1L_4)+
\SL_s (L_1L_3+L_2L_4)\Big)\nonumber\\ \label{quantum't HooftDGOT}
& +  \frac{4}{\sinh(\sll_{s}/2)}
{e^{+\sk_s'/2}}
\frac{\cosh \fr{\sll_s+l_1-l_2}{4} \cosh \fr{\sll_s+l_2-l_1}{4} 
\cosh \fr{\sll_s+l_3-l_4}{4} \cosh \fr{\sll_s+l_4-l_3}{4}}{\sinh(\sll_s/2)}
{e^{+\sk_s'/2}}
\notag \\
& +  \frac{4}{{\sinh(\sll_s/2)}}
{e^{-\sk_s'/2}}
\frac{\cosh \fr{\sll_s+l_1+l_2}{4} \cosh \fr{\sll_s-l_1-l_2}{4} 
\cosh \fr{\sll_s+l_3+l_4}{4} \cosh \fr{\sll_s-l_3-l_4}{4}}{\sinh(\sll_s/2)}
{e^{-\sk_s'/2}}
\,.
\notag
\end{align}
\end{subequations}
As the analytic properties of the coefficients $D_\ep(l_s)$ in \rf{Diffop}
are linked with the analytic properties of the kernels $A^{st}_L(l_{s},l_{t})$
via \rf{Loopduality},
it is no surprise that the kernels $A'^{st}_L(l_{s},l_{t})$ 
associated to the representation $\pi_s'$
have much better analytic properties than 
$A^{st}_L(l_{s},l_{t})$ as given by 
\rf{Avs6j}.
One may see see these analytic properties as
a profound consequence of the structure of the
moduli spaces $\CM_G(C)$ as algebraic varieties.
