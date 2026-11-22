---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-017-53-transitions-between-representation
section_title: "Transitions between representation"
section_number: 5.3
pages: 15-16
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.991
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The transition between any pair of representations 
$\pi_{\si_1}$  and $\pi_{\si_2}$
can be represented as
an integral transformation of the form
\begin{equation}\label{duality}
\psi_{\si_1}(l_{\si_1})\,=\,\int dl_{\si_2}\;A^{\si_1\si_2}_L(l_{\si_1},
l_{\si_2})
\,\psi_{\si_2}(l_{\si_2})\,.
\end{equation}
The relations
\begin{equation}\label{duality'}
\begin{aligned}
& \big(\pi_s(\sk_t)\psi_{s}\big)(l_{s})\,=\,4\pi b^2
  \int dl_{t}\;A^{st}_L(l_{s},l_{t})
\,\frac{1}{\textup{i}}\frac{\pa}{\pa l_t}\psi_{t}(l_{t})\,,\\
& 4\pi b^2\frac{1}{\textup{i}}\frac{\pa}{\pa l_s}
\psi_{s}(l_{s})\,=\,\int dl_{t}\;A^{st}_L(l_{s},
l_{t})
\,\big(\pi_t(\sk_s)\psi_{t}\big)(l_{t})\,,
\end{aligned}
\end{equation}
describing
the quantum change of Darboux coordinates
are direct consequences. 



It is important to note that the problem to  find the 
proper quantum representation of the generators
$\pi_\si(\CL_{\si'})$ is essentially equivalent to the problem
to find the kernels $A^{\si_1\si_2}_L(l_{\si_1},
l_{\si_2})$ in \rf{duality}.
Indeed, the requirement that
$\pi_\si(\CL_\si)\equiv 2\cosh(\sll_\si)/2$ implies
difference equations for the kernel $A^{\si_1\si_2}_L(l_{\si_1},
l_{\si_2})$ such as
\begin{equation}\label{Loopduality}
\pi_{\si_1}(\CL_{\si_2})\cdot A^{\si_1\si_2}_L(l_{\si_1},
l_{\si_2})\,=\,2\cosh(l_{\si_2}/2)\,
A^{\si_1\si_2}_L(l_{\si_1},l_{\si_2})\,.
\end{equation}
The difference operator on the left is of course understood
to act on the variable $l_{\si_1}$ only. 
Under certain natural conditions one may
show that the difference equations \rf{Loopduality} 
determine the
kernels $A^{\si_1\si_2}_L(l_{\si_1},l_{\si_2})$
uniquely. Conversely, knowing $A^{\si_1\si_2}_L(l_{\si_1},l_{\si_2})$,
one may show \cite{TV} that it satisfies relations of the 
form \rf{Loopduality}, and thereby deduce the explicit form of 
$\pi_{\si_1}(\CL_{\si_2})$. 

Considering the generalization to Riemann spheres $C_{0,n}$ 
with more than 
four holes it is natural to demand that the full theory can be 
built in a uniform manner
from the local pieces associated to the four-holed spheres 
that appear in a pants decomposition of $C_{0,n}$. This leads to 
severe restrictions on the kernels $A^{st}_L(l_{s},l_{t})$ 
known as the pentagon- and hexagon equations \cite{T05}. We claim 
that the resulting constraints determine $A^{st}_L(l_{s},l_{t})$ 
essentially uniquely up to changes of the normalization associated to 
pairs of pants.

Solutions of these conditions are clearly given by 
the b-$6j$-symbols. It is important to note, however, that a
change of normalization of the form \rf{norm} will be equivalent to
a gauge transformation \rf{gauge}. This means that 
different normalizations of the b-$6j$ symbols are 
in one-to-one correspondence with choices of Darboux-coordinates 
$(l_\si',k_\si')$
obtained from $(l_\si,k_\si)$ by  
canonical transformations of the form $l_\si'=l_\si$, 
$k_\si'=k_\si+f(l_\si)$. Only a very particular normalization
for the b-$6j$ symbols can correspond to the quantization of 
the Fenchel-Nielsen coordinates.
