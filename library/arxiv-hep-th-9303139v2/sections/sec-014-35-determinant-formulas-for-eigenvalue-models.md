---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-014-35-determinant-formulas-for-eigenvalue-models
section_title: "Determinant formulas for eigenvalue models"
section_number: 3.5
pages: 53-59
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.956
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We are now prepared to make the crucial step towards understanding of
mathematical structure behind eigenvalue models, which distinguishes their
partition functions in the entire variety of arbitrary $N$-fold integrals.
This structure expresses itself in the form of determinantal formulas, which
we are now going to discuss. In the next section 4 these formulas will be
identified as examples of $\tau$-functions of KP and Toda hierarchies.

Looking at the relevant
integrals (\ref{1mamoev}), (\ref{mumamoev}) one can notice that
integrals over different eigenvalues with non-trivial measures which depend
on the shape of potentials $U$ or $V$, are almost separated, the only
"interaction" between different eigenvalues being defined by $universal$
(potential-independent) quantities, made from the Van-der-Monde determinants.
This feature is intimately related both to its origin (decoupling of angular
variables in original matrix integral) and to its most important implication
(integrability). The main property of the Van-der-Monde determinant is that it
is at the same time a $Pfaffian$ (and it is in this quality that it arises
from matrix integrals) and a $determinant$ (and this is the feature that
implies integrability):
\be
\prod_{i>j}(h_i-h_j) = \Delta(h) = {\rm det}_{ij}h_i^{j-1}.
\label{vdmd}
\ee
We already used this property above, when going from eq.(\ref{KIev}) to
eq.(\ref{KIev'}), which as we shall see later is the crucial step in the proof
of integrability of Kontsevich model. In that case determinantal formula
(\ref{KIev'}) for partition function was trivial to derive, because the
integrand was $linear$ in Van-der-Monde determinants. Now we turn to slightly
more complicated situations, involving products of Van-der-Monde determinants.

Consider an eigenvalue model of the form:
\be
Z_N = \frac{1}{N!} \prod_{k=1}^N \int d\mu_{h_k,\bar h_k} \Delta(h)\Delta(\bar
h),
\label{meas1}
\ee
to be refered to as "scalar-product" model.
All conventional multimatrix models (\ref{mumamo'}) belong to this class.
In the case of the 1-matrix model (\ref{1mamoev})
\be
d\mu_{h,\bar h} = dhd\bar h e^{U(h)}\delta(h-\bar h),
\ee
while for conventional multimatrix models
(\ref{mumamoev})
\be
d\mu_{h^{(1)}, h^{(p-1)}} = dh^{(1)}dh^{(p-1)}\prod_{\alpha=2}^{p-2}
\int dh^{(\alpha)} \prod_{\alpha =1}^{p-1} e^{U_{\alpha}(h^{(\alpha)})}
\prod_{\alpha = 1}^{p-2} e^{h^{(\alpha)}h^{(\alpha+1)}}
\label{measmumamo}
\ee
If $d\mu_{h,\bar h} =\delta(h-\bar h)d\bar h d\mu_h$ we call this measure
local. The  main feature of local measure is that operator of multiplication
by $H$ (or any function of $h$) is Hermitean. Thus measure is local in the
1-matrix model, but is non-local for all $p-1>1$.
In the latter case the measure is defined to depend only on $h = h^{(1)}$ and
$\bar h = h^{(p-1)}$, all other
$h^{(\alpha)},\ \alpha = 2\ldots p-2$ being integrated out, what makes
the "interaction" between $h$ and $\bar h$ more complicated than just
$\delta(h-\bar h)$ in the one-matrix ($p=2$) and $e^{h\bar h}$ in the
two-matrix ($p=3$) cases. In no sense the set of particular formulas
(\ref{measmumamo}) for $p>3$ is distinguished among other scalar-product
models,
and from now on we shall not consider conventional multimatrix models with
$p-1 > 2$ as a separate class of theories.

Eqs.(\ref{meas1}) and (\ref{vdmd}) imply together that
\be
Z_N = \frac{1}{N!} \prod_{k=1}^N \int d\mu_{h_k,\bar h_k}
 {\rm Det}_{ik} h_k^{i-1} {\rm Det}_{jk} \bar h_k^{j-1} =   \nn \\
= {\rm Det}_{ij} \int d\mu_{h,\bar h} h^{i-1}\bar h^{j-1} =
      {\rm Det}_{ij} \langle h^{i-1} \mid  \bar h^{j-1} \rangle,
\label{dimamodet}
\ee
where an obvious notation is introduced for the scalar product
\be
\langle f(h)\mid g(\bar h)\rangle \equiv \int d\mu_{h,\bar h} f(h)g(\bar h).
\nn
\ee

We can now be a little more specific and introduce time-variables $t_k$ and
$\bar t_k$ so, that
\be
d\mu_{h,\bar h} = e^{U(h)+\bar U(\bar h)}{d\hat\mu}_{h,\bar h}, \nn \\
U(h) = \sum_{k=-\infty}^{\infty} t_kh^k, \ \
\bar U(\bar h) = \sum_{k=-\infty}^{\infty}
\bar t_k\bar h^k,
\label{tbartmeas}
\ee
and $\hat{d\mu}_{h,\bar h}$ is already independent of $h$ and $\bar h$. If we
now denote ${\cal H}^f(t,\bar t) \equiv \langle 1\mid 1\rangle$, then
\be
{\cal H}^f_{ij} \equiv \langle h^{i}\mid \bar h^{j} \rangle
= \frac{\partial^2}{\partial t_{i}\partial \bar t_{j}}{\cal H}^f(t,\bar t) =
\nn \\ \stackrel{{\rm if}\ i,j\geq 0}{=}
\left(\frac{\partial}{\partial t_1}\right)^{i}
\left(\frac{\partial}{\partial\bar t_1}\right)^{j}{\cal H}^f(t,\bar t),
\label{todamatr}
\ee
and
\be
Z_N = {\rm Det}_N {\cal H}^f_{ij},
\label{todarepr}
\ee
where $\ {\rm Det}_N$ stands for determinant of the $N\times N$ matrix ${\cal
H}_{i-1,j-1}$ (which is defined itself for {\it any} integers $i,j$)
with $i,j = 0,\ldots, N-1$.
Characteristic property of ${\cal H}_{ij}^f$ is its
peculiar time-dependence:
\be
\frac{{\cal H}^f_{ij}}{\partial t_k} = {\cal H}^f_{i+k,j}; \ \ \
\frac{{\cal H}^f_{ij}}{\partial \bar t_k} = {\cal H}^f_{i,j+k}.
\ee

Eq.(\ref{todarepr}) provides the determinantal formula for all scalar-product
models. The case of the local measure - for  1-matrix
model - is a little special. In this case $U(h)$ contains the whole
information about the measure: $d\mu_{h,\bar h} = \delta(h-\bar h)d\mu_h,\
d\mu_h = e^{U(h)}dh$, and there is no $\bar U(\bar h)$ (or $\bar t$ simply
coincide with $t$). Then (\ref{todarepr}) is still valid, but
\be
{\cal H}^f_{ij} = \left.\langle h^{i}\mid \bar h^{j} \rangle\right|
_{d\mu_{h,\bar h}}
= \left.\langle h^{i+j} \rangle\right|_{d\mu_h} =
\frac{\partial}{\partial t_{i+j}}{\cal H}^f(t) = \nn \\
\stackrel{{\rm if}\ i,j\geq 0}{=}
\left(\frac{\partial}{\partial t_1}\right)^{i+j}{\cal H}^f(t).
\label{todachainmatr}
\ee
The same formula (\ref{todachainmatr}) can be also derived as a limit of
eq.(\ref{KIev'}) for Kontsevich integral. Indeed,
\be


Z_N\{t\} = c_N\int_{N\times N}dH e^{{\rm Tr}U(H)} =
\lim_{ L \rightarrow 0} {\cal F}_{U,N}\{ L\} =
\nn \\
= \lim_{\{ l_j\}\rightarrow 0}
 \frac{{\rm Det}_{ij}\hat\varphi_i^{\{U\}}( l_j)}{\Delta( l)} =
{\rm Det}_{ij}\frac{\partial^{j-1}\hat\varphi_i^{\{U\}}( l_j)}
{\partial l^{j-1}}(0) = {\rm Det}_{ij} {\cal H}^f_{i-1,j-1},

\ee
where this time
\be
{\cal H}^f_{i-1,j-1} \stackrel{i,j>0}{=}
\frac{\partial^{j-1}\hat\varphi_i^{\{U\}}( l_j)}
{\partial l^{j-1}}( l =0) \stackrel{(\ref{KIev'})}{=}
\left(\frac{\partial}{\partial  l}\right)^{i+j-2} \hat\Phi^{\{U\}}
\mid_{ l = 0}.
\ee
Now we note, that the action of $\frac{\partial}{\partial  l}$ on
$\hat\Phi^{\{U\}}( l) = \int dx e^{U(x) +  l x}$ is equivalent to
that of $\left( \frac{\partial}{\partial t_1}\right)$, since this is no
longer a matrix integral, and thus
\be
{\cal H}^f_{ij} =  \left( \frac{\partial}{\partial t_1}\right)^{i+j}
\hat\Phi^{\{U\}}(0),
\label{todachainmatr1}
\ee
i.e. ${\cal H}^f(t) = \hat\Phi^{\{U\}}(0)$.

$Conformal$ multimatrix models were introduced in section 2.3 above just
as eigenvalue models. For the $A_{p-1}$ series partition functions are defined
to be
\be
\new
\begin{array}{c}
Z_{N_1\ldots N_{p-1}}^{A_{p-1}}\{t^{(1)} \ldots t^{(p-1)}\} =   \\
= \prod_{\alpha =1}^{p-1} c_{N_\alpha}\int_{N_\alpha\times N_\alpha}
dH^{(\alpha)} e^{{\rm Tr}U_\alpha(H^{(\alpha)})} \cdot \\ \cdot
\prod_{\alpha =1}^{p-2} {\rm Det}
\left( H^{(\alpha)}\otimes I - I\otimes H^{(\alpha +1)}\right) =  \\
= \prod_{\alpha = 1}^{p-1} \frac{1}{N_\alpha !}\prod_{i=1}^{N_\alpha}
\int dh_i^{(\alpha)} e^{U_\alpha (h_i^{(\alpha)})} \Delta^2(h^{(\alpha)})
\prod_{\alpha = 1}^{p-2} \prod_{i,k}

(h_i^{(\alpha)} - h_k^{(\alpha +1)}).
\label{comamoap}
\end{array}
\ee
This expression does not have a form of eq.(\ref{meas1}), thus conformal
matrix models for $p-1>1$ are not of the "scalar-product" type. We
shall sometimes call them $(p-1)$-component models, because they are related
to the multi-component integrable hierarchies.
The simplest way to proceed with their investigation is
to use the same trick with Kontsevich integral, which was just applied in the
1-matrix case.

Let us start from a very general $(p-1)$-component model:
\be
Z = \prod_{\alpha = 1}^{p-1} \int_{N_\alpha\times N_\alpha}
dH^{(\alpha)} e^{{\rm Tr} U_\alpha (H^{(\alpha)})}
K(H^{(1)}\ldots H^{(p-1)}).
\label{mucomammo}
\ee
It can be also represented in terms of Kontsevich integrals:
\be
Z = \left.K\left(\frac{\partial}{\partial L^{(1)}_{tr}},\ldots,
\frac{\partial}{\partial L^{(p-1)}_{tr}}\right)
\prod_{\alpha = 1}^{p-1} {\cal F}_{U_\alpha,
N_\alpha}\{ L^{(\alpha)}\}\right|_{ L^{(\alpha)} = 0}.
\label{mucomamo1}
\ee
This representation is not very usefull, since the limit $ L \rightarrow
0$ is not easy to take, unless $K$ is a polinomial in the eigenvalues of all
its arguments. However, this is exactly the case for our confromal models
(\ref{comamoap}). Indeed,
\be
K^{A_{p-1}} = \prod_{\alpha =1}^{p-2} {\rm Det}
\left(\frac{\partial}{\partial  L^{(\alpha)}_{tr}}\otimes I -
      I \otimes \frac{\partial}{\partial  L^{(\alpha+1)}_{tr}}\right).
\ee
Still this is not very convenient, because representation (\ref{KIev'}) for
${\cal F}$ contain $\Delta( L)$ in denominator, which are not very
pleasant to differentiate. Simplification can be achieved if instead we
rewrite the original expression at the r.h.s. of (\ref{comamoap}) as follows:
\be
&Z_{N_1\ldots N_{p-1}}^{A_{p-1}}\{t^{(1)} \ldots t^{(p-1)}\} =
\nn \\ &=



\Delta\left(\frac{\partial}{\partial l^{(1)}} \right)

\prod_{\alpha =1}^{p-2}
\Delta\left(\frac{\partial}{\partial l^{(\alpha)}},
\frac{\partial}{\partial l^{(\alpha+1)}} \right)
\Delta\left(\frac{\partial}{\partial l^{(p-1)}} \right)
\times \nn \\ &\times
\left.
\prod_{\alpha =1}^{p-1}\left( \frac{1}{N_\alpha !}\prod_{i=1}^{N_\alpha}\int
dh_i^{(\alpha)}
e^{U_\alpha (h_i^{(\alpha)})+ l_i^{(\alpha)}h_i^{(\alpha)}}

\right)\right|_{ l^{(\alpha)} = 0}
\label{mucomamo2}
\ee
where
$\Delta(h,h') \equiv \prod_{i>j}^N(h_i-h_j)\prod_{k>l}^{N'}(h'_k-h'_l)
\prod_{i=1}^N\prod_{k=1}^{N'}(h'_k-h_i)$.




This formula already takes the specific form of $K$ into account.
The product of integrals in brackets at the r.h.s. of (\ref{mucomamo2})
is equal (for every fixed $\alpha$) to
\be



\frac{1}{N_\alpha !}


\prod_{j=1}^{N_\alpha}\hat\Phi^{\{U_\alpha\}}( l_j^{(\alpha)})
\ee
(compare with eq.(\ref{todachainmatr1})).



In order to simplify the notation we shall further denote
$\hat\Phi^{\{U_\alpha\}}( l) \equiv \int dx e^{U_\alpha(x)+ l x}$
through $\hat\Phi_\alpha( l)$, and
$\left(\frac{\partial}{\partial t_1^{(\alpha)}}\right)^k
\hat\Phi^{\{U_\alpha\}}( l^{(\alpha)}) =
\left(\frac{\partial}{\partial  l^{(\alpha)}}\right)^k
\hat\Phi^{\{U_\alpha\}}( l^{(\alpha)})$ - through
$\partial^k \hat\Phi_\alpha( l)$. Thus
\be
&Z_{N_1\ldots N_{p-1}}^{A_{p-1}}\{t^{(1)} \ldots t^{(p-1)}\} =

\nn \\
&= \Delta\left(\frac{\partial}{\partial l^{(1)}} \right)

\prod_{\alpha =1}^{p-2}
\Delta\left(\frac{\partial}{\partial l^{(\alpha)}},
\frac{\partial}{\partial l^{(\alpha+1)}} \right)
\Delta\left(\frac{\partial}{\partial l^{(p-1)}} \right)
\times \nn \\ &\times \left.
\prod_{\alpha =1}^{p-1}\left(   \frac{1}{N_\alpha !} \prod_{j=1}^{N_\alpha}
\hat\Phi_\alpha( l_j^{(\alpha)})\right) \right|_{ l^{(\alpha)} = 0}.
\label{mucomamo4}

\ee
If $p-1=1$, differential operator is just a square of determinant
$\Delta(\partial/\partial l)$ and we can use the relation
\be
\Delta^2(h) &= \sum_P {\rm Det}_{ij} h_{P(j)}^{i+j-2} =
\nn \\
&= \sum_P {\rm Det}
\left[
{\begin{array}{ccrc}
1           &h_{P(2)}   &h^2_{P(3)}\ldots &h^{N_1-1}_{P(N_1)}    \\
h_{P(1)}    &h^2_{P(2)} &h^3_{P(3)}\ldots &h^{N_1}_{P(N_1)}    \\
h_{P(1)}^2  &h^3_{P(2)} &h^4_{P(3)}\ldots &h^{N_1+1}_{P(N_1)}    \\
            &           &\ldots           &                      \\
h_{P(1)}^{N_1-1}  &h_{P(2)}^{N_1} &h_{P(3)}^{N_1+1}\ldots
&h^{2N_1-2}_{P(N_1)}
\end{array}}
\right]
\label{detform1}
\ee
where the sum is over all the $N!$ permutations $P$ of $N$ elements
$1\ldots N$, in order to conclude that (\ref{mucomamo4}) reproduces
our old formula (\ref{todarepr}), (\ref{todachainmatr1}):
$Z_N = {\rm Det}_{ij} \partial^{i+j-2}\hat\Phi$.

For $p-1=2$ we need to use a more complicated analogue of
(\ref{detform1}):
\be
&\Delta(h)\Delta(h,h')\Delta(h') =



\label{detform2} \\
&= \sum_P\sum_{P'}{\rm Det}\left[
{\begin{array}{crccrc}
1           &h_{P(2)}

\ldots &h^{N_1-1}_{P(N_1)}   &1  &\bar h_{\bar P(2)}

\ldots &\bar h^{N_2-1}_{\bar P(N_2)} \\
h_{P(1)}    &h^2_{P(2)}

\ldots &h^{N_1}_{P(N_1)}  &\bar h_{\bar P(1)}  & \bar h_{\bar P(2)}^2

\ldots &\bar h^{N_2}_{\bar P(N_2)} \\
h_{P(1)}^2  &h^3_{P(2)}

\ldots &h^{N_1+1}_{P(N_1)}  &\bar h_{\bar P(1)}^2 &\bar h_{\bar P(2)}^3

\ldots &\bar h^{N_2+1}_{\bar P(N_2)}  \\
            &    &     \ldots &  & &                     \\
h_{P(1)}^{{\cal N}_1-1}  &h_{P(2)}^{{\cal N}_1}

\ldots &h^{{\cal N}+N_1-2}_{P(N_1)}
&\bar h_{\bar P(1)}^{{\cal N}_2-1}  &\bar h_{\bar P(2)}^{{\cal N}_2}

\ldots &\bar h^{{\cal N}+N_2-2}_{P(N_2)}
\end{array}}
\right]

\nn
\ee
where ${\cal N} = \sum_{\alpha =1}^{p-1} N_\alpha$. Making use of this
formula, we conclude that the r.h.s. of (\ref{mucomamo4}) for $p-1=2$ is also
representable in the form of determinant:
\be
{\rm Det}
 \left[
\begin{array}{crccrc}
\hat\Phi &\partial\hat\Phi \ldots &\partial^{N_1-1}\hat\Phi
  &\hat{\bar\Phi} &\partial\hat{\bar\Phi} \ldots
&\partial^{N_2-1}\hat{\bar\Phi} \\

\partial\hat\Phi &\partial^2\hat\Phi \ldots &\partial^{N_1}\hat\Phi
  &\partial\hat{\bar\Phi} &\partial^2\hat{\bar\Phi} \ldots
&\partial^{N_2}\hat{\bar\Phi}
\\

  &         & \ldots  & &    &                        \\
\partial^{{\cal N}-1}\hat\Phi &\partial^{\cal N}\hat\Phi \ldots
&\partial^{{\cal N}+N_1-2}\hat\Phi
  &\partial^{{\cal N}-1}\hat{\bar\Phi} &\partial^{\cal N}\hat{\bar\Phi} \ldots
&\partial^{{\cal N}+N_2-2}\hat{\bar\Phi}

\end{array}
\right]
\nn
\ee
here $\hat\Phi = \hat\Phi_1,\ \hat{\bar\Phi} = \hat\Phi_2$
and all arguments $ l^{(\alpha)} = 0$.
It is especially easy to check formula (\ref{detform2})
in the simplest case of $N_1=N_2=1$. Then it just says that
$\bar h - h = {\rm Det}\left[\begin{array}{cc}
1&1 \\ h&\bar h \end{array}\right]$.
Analogues expressions for $p-1>2$ are more involved, they are no longer just
determinants: this is obvious already
from consideration of the simplest case of $N_1=\ldots=N_{p-1}=1$,
the product $\prod_{\alpha=1}^{p-2}(h^{(\alpha)} - h^{(\alpha+1)})$
is no longer determinant of any nice matrix.
