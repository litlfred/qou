---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-012-33-itzykson-zuber-and-kontsevich-integrals
section_title: "Itzykson-Zuber and Kontsevich integrals"
section_number: 3.3
pages: 49-52
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.94
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Let us proceed now to Kontsevich integral,
\be
{\cal F}_{V,n}\{ L\} =
\int_{n\times n} dX e^{- {\rm tr} V(X) + {\rm tr} L X}.
\label{KI'}
\ee
We shall see shortly that it in fact depends only on the eigenvalues of the
matrix $ L$ (this fact was already used in the previous section),
however, this time somewhat more sophisticated unitary matrix integrals will
be involved.

Substitute $X = U_X^{\dagger}D_XU_X;  \ \  L = U_{ L}^{\dagger}
D_{ L}U_{ L}$ in (\ref{KI'}) and denote
$U \equiv U_XU_{ L}^{\dagger}$. Then
\be
&{\cal F}_{V,n}\{ L\} = \nn \\
&= \prod_{i=1}^n \int dx_i e^{-V(x_i)}
\Delta^2(x)
\int_{n\times n} \frac{[dU]}{[dU_{Cartan}]}
\exp\left({\sum_{\gamma,\delta =1}^n x_\gamma l_\delta\mid
U_{\gamma\delta}\mid^2} \right).
\label{KI'2}
\ee
In order to proceed further we need to evaluate the integral over unitary
matrices, which appeared at the r.h.s.

This integral can actually be represented in two different ways:
\be
I_n\{X, L\} \equiv  \int_{n\times n} \frac{[dU]}{[dU_{Cartan}]}
e^{{\rm tr} XU L U^{\dagger}} =
\label{IZa} \\
=  \int_{n\times n} \frac{[dU]}{[dU_{Cartan}]}
e^{\sum_{\gamma,\delta =1}^n x_\gamma l_\delta\mid U_{\gamma\delta}\mid^2}
\label{IZb}
\ee
(the U's in the two integrals are related by the transformation
$U \longrightarrow U_XUU_{ L}^{\dagger}$ and Haar measure is both left
and right invariant).
Formula (\ref{IZa}) implies that $I_n\{X, L\}$ satisfies a set of simple
equations \cite{Migeq}:
\be
\left( {\rm tr} \left(\frac{\partial}{\partial X_{tr}}\right)^k -
       {\rm tr}  L^k \right) I_n\{X, L\} = 0, \ \ k\geq 0, \nn\\
\left( {\rm tr} \left(\frac{\partial}{\partial  L_{tr}}\right)^k -
       {\rm tr} X^k \right) I_n\{X, L\} = 0, \ \ k\geq 0,
\label{Migeq}
\ee
which by themselves are not very restrictive. However, another formula,
(\ref{IZb}), implies that $I_n\{X, L\}$ in fact depends only on the
eigenvalues of $X$ and $ L$, and for $such$ $I_n\{X, L\} =
\hat I\{x_\gamma, l_\delta\}$ eqs.(\ref{Migeq}) become very restrictive
\footnote{When acting on $\hat I$, which depends only on eigenvalues,  matrix
derivatives turn into:
\be
{\rm tr} \frac{\partial}{\partial X_{tr}} \hat I &=
   \sum_\gamma \frac{\partial}{\partial x_\gamma} \hat I; \nn \\
{\rm tr} \frac{\partial^2}{\partial X_{tr}^2} \hat I &=
   \sum_\gamma \frac{\partial^2}{\partial x_\gamma^2} \hat I  +
\sum_{\gamma\neq\delta} \frac{1}{x_\gamma-x_\delta}
\left(\frac{\partial}{\partial x_\gamma} -
\frac{\partial}{\partial x_\delta}\right) \hat I;
\nn
\ee
etc.
} and allow to
determine $\hat I\{x_\gamma, l_\delta\}$
unambigously (at least if $\hat I\{x_\gamma, l_\delta\}$
is expandable in a formal power seria in $x_\gamma$ and $ l_\delta$).
The final solution is
\be
I_n\{X, L\} = \frac{(2\pi)^{\frac{n(n-1)}{2}}}{n!}
\frac{{\rm det}_{\gamma\delta}
   e^{x_\gamma l_\delta}}{\Delta(x)\Delta( l)}.
\label{IZ}
\ee
Normalization constant can be defined by taking $ L = 0$, when
\be
I_n\{X,L=0\} =
\frac{{\rm Vol}_{U(n)}}{({\rm Vol}_{U(1)})^n} =
\frac{(2\pi)^{\frac{n(n-1)}{2}}}{\prod_{k=1}^n k!},
\nn
\ee
and using the fact that
\be
\left.\frac{{\rm det}_{\gamma\delta} f_\gamma(l_\delta)}{\Delta(l)}\right|
_{\{l_\delta = 0\}} =
\left(\prod_{k=0}^{n-1}\frac{1}{k!} \right) {\rm det}_{\gamma\delta}
\partial^{\delta-1}f_\gamma(0).
\nn
\ee

Eq.(\ref{IZ}) is usually refered to as the Itzykson-Zuber formula
\cite{IZ}. In mathematical literature it was earlier derived by
Kharish-Chandra \cite{KhCh}, and in fact the integral (\ref{IZa} is the basic
example of the coadjoint orbit integrals \cite{STS}-\cite{AS}, which can be
exactly evaluated with the help of the Duistermaat-Heckmann theorem \cite{DH},
\cite{NiDH},\cite{Wit2YM},\cite{NT}.
This calculation is the simplest example of the very
important technique of $exact$ evaluation of $non-Gaussian$ unitary-matrix
integrals, which is now doing its first steps (see \cite{KMSW1}-\cite{Shata})
and will be discussed at the end of these notes.

Now we turn back to the eigenvalue formulation of the GKM. Substitution of
(\ref{IZ}) into (\ref{KI'2}) gives:
\be
{\cal F}_{V,n}\{ L\} = \frac{(2\pi)^{\frac{n(n-1)}{2}}}{\Delta( l)}
\prod_{\delta=1}^n \int dx_\delta e^{-V(x_\delta)} \Delta(x)
\frac{1}{n!} {\rm det}_{\gamma\delta} e^{x_\gamma l_\delta} = \nn \\
= \frac{(2\pi)^{\frac{n(n-1)}{2}}}{\Delta( l)}
\prod_{\delta =1}^n \int dx_\delta e^{-V(x_\delta) + x_\delta l_\delta}
\Delta(x),
\label{KIev}
\ee
where we used antisymmetry of $\Delta(x)$ under permutations of $x_\gamma$'s in
order to change $\frac{1}{n!} {\rm det}_{\gamma\delta}
e^{x_\gamma l_\delta}$ for
$e^{\sum_\delta x_\delta l_\delta}$
under the sign of the $x_\delta$ integration.

We can now use the fact that $\Delta(x) = {\rm
det}_{\gamma\delta}x_\delta^{\gamma -1}$ in order to
rewrite the r.h.s. of (\ref{KIev}):
\be
{\cal F}_{V,n}\{ L\} = (2\pi)^{\frac{n(n-1)}{2}}\frac{{\rm det}_{\gamma\delta}
\hat\varphi_\gamma( l_\delta)}{\Delta( l)},
\label{KIev'}
\ee
where
\be
\hat\varphi_\gamma( l) \equiv \int dx x^{\gamma -1}e^{-V(x)+ l x},
\ \ \ \gamma\geq 1.
\label{hatvarphi}
\ee
These functions $\hat\varphi( l)$ satisfy a simple recurrent relation:
\be
\hat\varphi_\gamma = \frac{\partial\hat\varphi_{\gamma -1}}{\partial  l} =
\left(\frac{\partial}{\partial  l}\right)^{\gamma -1}\hat\Phi
\label{preKasch}
\ee
with
\be
\hat\Phi( l)\equiv \hat\varphi_1( l) =
\int dx e^{-V(x)+ l x}.
\label{preKasch'}
\ee

Note also that if the "zero-time" $N$ is introduced (see subsection 2.6 above
and \cite{Toda}), then
\be
{\cal F}_{V,n}\{N\mid L\} \equiv {\cal F}_{V(X)-N\log X,n}\{ L\} =
(2\pi)^{\frac{n(n-1)}{2}}\frac{{\rm det}_{\gamma\delta}
\hat\varphi_{\gamma +N}( l_\delta)}{\Delta( l)}
\label{KIev'N}
\ee
with just the $same$ $\hat\varphi_\gamma( l)$ and
$\gamma,\delta = 1\ldots n$.
If we divide by the  quasiclassical factor
${\cal C}_V\{\Lambda \}({\rm det} \Lambda )^N,\
 L = V'(\Lambda )$, in order to transform Kontsevich integral into Kontsevich
model (see section 2.5), we get:
\be
{\cal Z}_V\{N,T\} = \frac{1}{({\rm det} \Lambda )^N}\cdot\frac{{\rm
det}_{\gamma\delta} \varphi_{\gamma +N}(\lambda _\delta)}{\Delta(\lambda )}.
\label{KIev"N}
\ee
The role of ${\cal C}_V\{\Lambda \}$ is to convert $\hat\varphi( l)$ into
the properly normalized expansions in the negative iteger powers of $\lambda $:
\be
\varphi_\gamma(\lambda )  =
\frac{e^{-\lambda V'(\lambda )+V(\lambda )}\sqrt{V''(\lambda )}}{\sqrt{2\pi}}
\hat\varphi_\gamma(V'(\lambda )) =
\lambda ^{\gamma -1}(1 + {\cal O}(\lambda ^{-1})),
\label{varphiko}
\ee
and to change $\Delta( l) = \Delta(V'(\lambda ))$ in the denominator of
(\ref{KIev'N}) for  $\Delta(\lambda )$ in (\ref{KIev"N}).
Instead of the simple recurrent relations (\ref{preKasch}) for $\hat\varphi$
the normalized functions $\varphi$ satisfy:
\be
\varphi_\gamma(\lambda ) = {\cal A}\varphi_{\gamma -1}(\lambda ) =
{\cal A}^{\gamma -1}\Phi(\lambda ),
\label{Kasch}
\ee
where $\Phi(\lambda ) = \varphi_1(\lambda )$ and operator
\be
{\cal A} = \frac{1}{V''(\lambda )}\cdot\frac{\partial}{\partial \lambda }
-\frac{1}{2}\frac{V'''(\lambda )}{(V''(\lambda ))^2} + \lambda
\label{Kaschop}
\ee
now depends on the potential $V(x)$.
