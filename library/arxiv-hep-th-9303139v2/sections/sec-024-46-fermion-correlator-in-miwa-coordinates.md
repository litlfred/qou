---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-024-46-fermion-correlator-in-miwa-coordinates
section_title: "Fermion correlator in Miwa coordinates"
section_number: 4.6
pages: 92-99
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.977
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Let us now return to original correlator (\ref{pretaf}) and
discuss in a little more details the implications of bosonization
identity (\ref{bosid}). In order not to write down integrals of $J$, we
introduce scalar field:\footnote{
One can consider $\phi $ as introduced for simplicity of notation,
but it should be kept in mind that the scalar-field
representation is in fact more fundamental for {\it generic} $\tau$-functions,
not related to the level $k=1$ Kac-Moody algebras (this phenomenon is well
known in conformal filed theory, see \cite{GMMOS} for more details).
}
\be
\phi(z) = \sum_{\stackrel{k\neq 0}{k\in Z-0}}\frac{J_{-k}}{k}z^k
+ \phi_0 + J_0\log z,
\ee
such that $\partial\phi(z) = J(z)$. Then (\ref{bosid}) states that:
\be
:\psi( \lambda)\tilde\psi(\tilde \lambda):\ = \
:e^{\phi(\tilde \lambda)-\phi( \lambda)}:
\label{bosid'}
\ee
"Normal ordering" here means nothing more but the requirement to neglect all
mutual contractions (or correlators) of operators in between $:\ \ :$ when
Wick theorem is applied to evaluate corrletion functions.
One can also get rid of the normal ordering sign at the l.h.s. of
(\ref{bosid'}), then
\be
\psi( \lambda)\tilde\psi(\tilde \lambda) = \
:e^{\phi(\tilde \lambda)}:\  :e^{-\phi( \lambda)}:
\label{bosid"'}
\ee
In distinguished coordinates on a sphere, when the free field propagator is
just $\log( z-\tilde z)$, one also has:
\be
\psi( z)\tilde\psi(\tilde z) =
\frac{1}{ z-\tilde z}\ :\psi( z)\tilde\psi(\tilde z):
\nn
\ee


Our task now is to express operators $e^H$ and $e^{\bar H}$ through the field
$\phi$. This is simple:
\be
H = \oint_0 U( z)J( z) = \oint_0 U( z)\partial\phi( z) =
- \oint_0 \phi( z)\partial U( z).
\ee
Here as usual $U( z) = \sum_{k>0} t_k z^k$ and integral is around
$ z = 0$. This is very similar to generic linear functional of
$\phi_-(\lambda) \equiv -\sum_{k>0}\frac{1}{k}J_k\lambda^{-k}$,
\be
H = \int \phi_-(\lambda)f(\lambda) d\lambda,
\label{hamneg}
\ee
one should only require that\footnote{
As it is usual nowadays, a factor of $2\pi i$ is assumed to be included into
the definition of contour integral $\oint$.
}
\be
\partial U( z) = \int \frac{f(\lambda)}{ z - \lambda}d\lambda,
\nn
\ee
i.e.
\be
U( z) = \int\log\left(1-\frac{ z}{\lambda}\right) f(\lambda)d\lambda.
\ee
In terms of time-variables this means that
\be
t_k = -\frac{1}{k}\int \lambda^{-k}f(\lambda)d\lambda.
\label{miwatransint}
\ee
Here we required that $U( z = 0) = 0$, sometimes it can be more natural
to introduce also
\be
t_0 = \int \log \lambda\ f(\lambda)d\lambda.
\ee
This change from the time-variables to "time density" $f(\lambda)$ is known as
Miwa
transformation. In order to establish relation with fermionic representation
and also with matrix models we shall need it in "discretized" form:
\be
t_k &= \frac{\xi}{k}\left(\sum_{\gamma} \lambda_\gamma^{-k} -
\sum_\gamma \tilde \lambda_\gamma^{-k} \right), \nn \\
t_0 &= -\xi\left(\sum_\gamma \log \lambda_\gamma  - \sum_\gamma\log \tilde
\lambda_\gamma\right).
\label{miwatrans}
\ee
We changed integral over $\lambda$ for a discrete sum
(i.e. the density function $f(\lambda)$ is
a combination of $\delta$-functions, picked at some points
$\lambda_\gamma,\ \tilde \lambda_\gamma$. This is
of course just another basis in the space of the linear functionals, but the
change from one basis to another one is highly non-trivial. The thing is, that
we selected the basis where amplitudes of different $\delta$-functions are the
{\it same}: parameter $\xi$ in (\ref{miwatrans}) is {\it independent} of
$\gamma$. Thus the real parameters are just positions of the points
$\lambda_\gamma, \ \tilde \lambda_\gamma$,
while the amplitude is defined by the density
of these points in the integration (summation) domain. This domain does
not need to be {\it a priori} specified:
it can be real line, any other contour or - better -
some  Riemann surface.)
Parameter $\xi$ is also unnecessary to introduce, because basises with
different $\xi$ are essentially equivalent. We shall soon put it equal to {\it
one}, but not before Miwa transformation will be discussed in a little more
detail.

Our next steps will be as follows.
Substitution of (\ref{hamneg}) into (\ref{miwatrans}), gives:
\be
H = -\xi\sum_\gamma \phi_-(\lambda_\gamma) +
\xi\sum_\gamma\phi_-(\tilde\lambda_\gamma).
\ee
In fact, what we need is not operator $H$ itself, but the state which is
created when $e^H$ acts on the vacuum state $\langle N\mid$. Then, since
$\langle N\mid J_m = 0$ for $m<0$, $\langle N\mid e^{-\xi\phi_-(\lambda)}$ is
essentially equivalent to $\langle N\mid e^{-\xi\phi(\lambda)}$ with
$\phi_-(\lambda)$ substituted by entire $\phi(\lambda)$. If $\xi = 1 $,
$e^{-\phi(\lambda)}$ can be further changed for $\psi(\lambda)$ and we
obtain an expression for the correlator (\ref{pretaf}) an expression where
$e^H$ is substituted by a product of operators $\psi(\lambda_\gamma)$. The
same is of course true for $e^{\bar H}$. Then Wick therem can be applied and a
new type of determinant formulas arises like, for example,
\be
\tau \sim \frac{\Delta(\lambda,
\tilde\lambda)}{\Delta^2(\lambda)\Delta^2(\tilde\lambda)}
{\rm det}_{\gamma\delta} \langle N\mid \psi(\lambda_\gamma)
\tilde\psi(\tilde\lambda_\delta)\ G \ \mid N\rangle
\ee
It can be also obtained directly from (\ref{pretafdet}), (\ref{Hmatrcor}) and
(\ref{HversTlm}) by Miwa transformation.
The rest of this subsection describes this derivation in somewhat more
details.

The first task is to substitute $\phi_-$ by $\phi$. For this purpose we
introduce operator
\be
\sum_{k=-\infty}^{\infty} t_kJ_k = H_+ + H_-,
\ee
where $H_+ = \sum_{k>0} t_kJ_k$ is just our old $H$, $H_- = \sum_{k\geq 0}
t_{-k}J_k$, and "negative times" $t_{-k}$ are defined by "analytical
continuation" of the same formulas (\ref{miwatransint}) and (\ref{miwatrans}):
\be
t_{-k} = \frac{1}{k} \int \lambda^k f(\lambda)d\lambda =
-\frac{\xi}{k} \left(\sum_\gamma \lambda_\gamma^k - \sum_\gamma
\tilde\lambda^k_\gamma \right).
\ee
Then
\be
\sum_{k=-\infty}^{\infty} t_kJ_k = H_+ + H_- =
-\xi\left(\sum_\gamma \phi(\lambda_\gamma) - \sum_\gamma
\phi(\tilde\lambda_\gamma) \right).
\label{miwadetder1}
\ee
Further,
\be
e^{H_+ + H_-} = e^{-\frac{1}{2}s(t)} e^{H_+}e^{H_-} =
      e^{\frac{1}{2}s(t)} e^{H_-}e^{H_+},
\ee
where
\be
\new
\begin{array}{c}
s(t) \equiv \sum_{k>0} kt_kt_{-k} =
-\xi^2 \sum_{k>0}\frac{1}{k} \left(\sum_\gamma
\left(\lambda_\gamma^{-k} - \tilde\lambda_\gamma^{-k}\right)
\sum_\delta \left(\lambda_\delta^k - \tilde\lambda_\delta^k \right)\right) = \\
= \xi^2 \log \left(\left. \prod_{\gamma,\delta}\right.^\prime\
\frac{(1-\frac{\lambda_\delta}{\lambda_\gamma})
(1-\frac{\tilde\lambda_\delta}{\tilde\lambda_\gamma})}
{(1-\frac{\tilde\lambda_\delta}{\lambda_\gamma})
(1-\frac{\lambda_\delta}{\tilde\lambda_\gamma})}\right) \ + \ {\rm const},
\end{array}
\ee
where prime means that the terms with $\gamma = \delta$ are excluded from the
product in the numerator and accounted for in the infinite "constant", added
at the r.h.s. In other words,
\be
e^{\frac{1}{2}s(t)} &= {\rm const}\cdot
\left(
\frac{\prod_{\gamma > \delta} (\lambda_\gamma - \lambda_\delta)
(\tilde\lambda_\gamma - \tilde\lambda_\delta)}
{\prod_\gamma \prod_\delta (\lambda_\gamma - \tilde\lambda_\delta)}
\right)^{\xi^2} =  \nn \\ &=
{\rm const}\cdot
\left(
\frac{\Delta^2(\lambda) \Delta^2(\tilde\lambda)}{\Delta(\lambda,
\tilde\lambda)}
\right)^{\xi^2}.
\label{miwadetder2}
\ee
Since $\ \langle N\mid J_m = 0\ $  for all $m<0$, we have
$\langle N\mid e^{H_-} = \langle N\mid$, and therefore
\be
\langle N\mid e^H \equiv \langle N\mid e^{H_+} =
\langle N\mid e^{H_-}e^{H_+} =

e^{-\frac{1}{2}s(t)}\langle N\mid e^{H_+ + H_-}.
\ee
{}From eq.(\ref{miwadetder1}),
\be
e^{H_+ + H_-} = {\rm const}\cdot \prod_\gamma \ :e^{-\xi\phi(\lambda_\gamma)}:
\ :e^{\xi\phi(\tilde\lambda_\gamma)}:
\ee
where "const" is exactly the same as in (\ref{miwadetder2}).
If $\xi = 1$, eq.(\ref{bosid"'}) can be used to write:\footnote{
The choice of $\xi$ can be dictated by particular purposes. Here we impose the
requirement on Miwa transform to represent $e^H = e^{H_{Cartan}}$ as a product
of dimension-1/2 operators - this is
most natural from the point of view of Hirota equations and simplifies the
relation with integrable hierarchies. However, in section 2.7 and 2.8 we used
another requirement (and there $\xi = \frac{1}{\sqrt{2}}$ rather than $\xi =
1$). There the 1-matrix model was considered, which is characterized by
especially simple form of the $full$ hamiltonian (product of dimension-zero
operators), and it was more  important to adjust
operators, which arise from $e^{H_{Cartan}}$ after Miwa transform to have
simple correlators with $e^{A\psi\tilde\psi}$. When analyzing the 1-matrix
model from this point of view one should also keep in mind that it was
actually represented in s.2.3 in terms of {\it two} complex fermions.
Screening charges are $Q^{(+)} = \oint e^{\sqrt{2}\phi} =
\oint\tilde\psi_1\psi_2 = \oint e^{\phi_1-\phi_2},\ \
Q^{(-)} = \oint e^{-\sqrt{2}\phi} = \oint\tilde\psi_2\psi_1 =
\oint e^{\phi_2 - \phi_1}$, while $\phi = \frac{1}{\sqrt{2}}(\phi_1 - \phi_2)$.
The Hamiltonian is $H_{Cartan} = \frac{1}{\sqrt{2}}\sum_k t_kJ_k =
\frac{1}{2} \sum_k t_k(J_k^1 - J_k^2)$, and Miwa transformation generators
insertions of operators $\chi_1\tilde\chi_2$, where
$\chi_1$ and $\tilde\chi_2$
have dimension 1/8 (rather than 1/2 as in the one (complex)-fermion system,
considered in $this$ section).
}
\be
\langle N\mid e^H \ = \
\frac{\Delta(\lambda,\tilde\lambda)}
{\Delta^2(\lambda) \Delta^2(\tilde\lambda)}
\langle N \mid \prod_\gamma \psi(\lambda_\gamma)
\prod_\gamma \tilde\psi(\tilde\lambda_\gamma)
\ee
Similarly,
\be
e^{\bar H} \mid N \rangle =
\prod_\delta \psi(\bar\lambda_\delta)
\prod_\delta \tilde\psi(\tilde{\bar\lambda}_\delta)
\mid N \rangle
\frac{\Delta(\bar\lambda,\tilde{\bar\lambda})}
{\Delta^2(\bar\lambda) \Delta^2(\tilde{\bar\lambda})},
\ee
where
\be
\bar t_k = - \frac{1}{k} \sum_\delta \left(\bar\lambda_\delta^k -
                  \tilde{\bar\lambda}_\delta^k\right)
\ee
and we used the fact that $J_m \mid N \rangle = 0 $ for all $m>0$.
Finaly,
\be
\new
\begin{array}{c}
\tau_N\{t, \bar t \mid G\} =
\langle N \mid e^H \ G \ e^{\bar H} \mid N \rangle =
\frac{\Delta(\lambda,\tilde\lambda)}
{\Delta^2(\lambda) \Delta^2(\tilde\lambda)}
\frac{\Delta(\bar\lambda,\tilde{\bar\lambda})}
{\Delta^2(\bar\lambda) \Delta^2(\tilde{\bar\lambda})}
\cdot   \\ \cdot
\langle N \mid  \prod_\gamma \psi(\lambda_\gamma)
\prod_\gamma \tilde\psi(\tilde\lambda_\gamma)\ G\
\prod_\delta \psi(\bar\lambda_\delta)
\prod_\delta \tilde\psi(\tilde{\bar\lambda}_\delta)
\mid N \rangle .
\end{array}
\label{tautodamiwdet}
\ee
Singularities at the coinciding points are completely eliminated from this
expression, since poles and zeroes of the correlator are canceled by those
coming from the Van-der-Monde determinants.

Let us now put $N=0$ and define normalized $\tau$-function
\be
\hat \tau_0\{t,\bar t \mid G\} \equiv
\frac{\tau_0\{t,\bar t\mid G\}}{\tau_0\{0,0\mid G\}},
\ee
i.e. divide r.h.s. of (\ref{tautodamiwdet}) by $\langle 0 \mid  G  \mid
0 \rangle$.
Wick theorem now allows to rewrite the correlator at the r.h.s.
as a determinant of the block matrix:
\be
\new
{\rm det}\left(\begin{array}{cc}
\frac{\langle 0 \mid \psi(\lambda_\gamma)
\tilde\psi(\tilde\lambda_\delta)\ G \
\mid 0 \rangle}{\langle 0 \mid \ G \ \mid 0 \rangle}
  & \frac{\langle 0 \mid \psi(\lambda_\gamma)\ G \
\tilde\psi(\tilde{\bar\lambda}_\delta) \mid 0 \rangle}{\langle 0 \mid \ G \
\mid 0 \rangle} \\
-\frac{\langle 0 \mid \tilde\psi(\tilde\lambda_\delta)\ G \
\psi(\bar\lambda_\gamma) \mid 0 \rangle}{\langle 0 \mid \ G \ \mid 0 \rangle}
  & \frac{\langle 0 \mid \ G\ \psi(\bar\lambda_\gamma)
\tilde\psi(\tilde{\bar\lambda}_\delta) \mid 0 \rangle}{\langle 0 \mid \ G \
\mid 0 \rangle}
\end{array} \right)
\label{blockform}
\ee

Special choices of points $\lambda_\gamma, \ldots,
\tilde{\bar\lambda}_\delta$ can lead to simpler formulas.
If $\tilde{\bar\lambda}_\gamma \rightarrow {\bar\lambda}_\gamma$, so that
$\bar t_k \rightarrow 0$, the matrix elements at the right lower block in
(\ref{blockform}) blow up, so that the off-diagonal blocks can be neglected.
Then
\be
\new
\begin{array}{c}
\tau_0\{t,\bar t \mid G\} \rightarrow \tau^{KP}\{t \mid G\} =
\frac{\langle 0 \mid e^H \ G \ \mid 0 \rangle}{\langle 0 \mid \ G \ \mid 0
\rangle} =   \\
= \frac{\Delta(\lambda,\tilde\lambda)}
{\Delta^2(\lambda) \Delta^2(\tilde\lambda)}
{\rm det}_{\gamma\delta} \frac{\langle 0 \mid   \psi(\lambda_\gamma)
\tilde\psi(\tilde\lambda_\delta)\ G\ \mid 0 \rangle}{\langle 0 \mid \ G \ \mid
0 \rangle} .
\end{array}
\label{kpdetrep}
\ee
This function no longer depends on $\bar t$-times and  is
just a KP $\tau$-function.

Matrix element
\be
\varphi(\lambda,\tilde\lambda) = \frac{\langle 0 \mid \psi(\lambda)\tilde\psi(
\tilde\lambda)\  G\ \mid 0 \rangle}{\langle 0 \mid G \mid 0 \rangle}
\ee
is singular, when $\lambda \rightarrow \tilde\lambda$:
$\varphi(\lambda,\tilde\lambda) \rightarrow \frac{1}{\lambda - \tilde\lambda}$.
If now in (\ref{kpdetrep}) all $\tilde\lambda \rightarrow \infty$,
\be
\tau^{KP}\{t \mid G\} =
\frac{{\rm
det}_{\gamma\delta}\varphi_\delta(\lambda_\gamma)}{\Delta(\lambda)},
\label{KPdetmain}
\ee
where
\be
\varphi_\delta(\lambda) \equiv \langle 0 \mid \psi(\lambda)
\left(\partial^{\delta-1}\tilde\psi\right)(\infty)\
G \ \mid 0 \rangle \sim \lambda^{\delta
-1} \left(1 + {\cal O}\left(\frac{1}{\lambda}\right)\right).
\ee
This is the main determinant representation of KP $\tau$-function in Miwa
parametrization.

Starting from representation (\ref{KPdetmain}) one can restore the
corresponding matrix ${\cal H}^{KP}_{ij}$ in eq.(\ref{addkptau1}) \cite{Toda}:
\be
{\cal H}^{KP}_{ij}\{t\} = \oint z^i\varphi_{-j}(z) e^{\sum_k t_kz^k} dz,
\label{addkptau3}
\ee
i.e.
\be
T_{lj}^{KP} = \oint z^l\varphi_{-j}(z).
\ee
Then obviously $\displaystyle{\frac{\partial {\cal H}^{KP}_{ij}}{\partial t_k}
= {\cal H}^{KP}_{i+k,j}}$. Now we need to prove that the $\tau$-function is
given at once by $\frac{{\rm det}\
\varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)}$ and ${\rm Det} {\cal
H}^{KP}_{ij}\{t\}$. In order to compare these two expressions one should take
$t_k = \frac{1}{k}\sum_\gamma^n \lambda_\gamma^{-k}$, so that
\be
\exp\left({\sum_{k>0} t_kz^k}\right) = \prod_{\gamma =1}^n
\frac{\lambda_\gamma}{\lambda_\gamma - z} =
\left(\prod_\gamma^n \lambda_\gamma\right)
\sum_\gamma \frac{(-)^\gamma}{z-\lambda_\gamma}
\frac{\Delta_\gamma(\lambda)}{\Delta(\lambda)},
\ee
where
\be
\Delta_\gamma(\lambda) = \prod_{\stackrel{\alpha>\beta}{\alpha,\beta\neq
\gamma}}(\lambda_\alpha - \lambda_\beta) =
\frac{\Delta(\lambda)}{\prod_{\alpha\neq \gamma}(\lambda_\alpha -
\lambda_\gamma)},
\ee
and
\be
\left.{\cal H}^{KP}_{ij}\right|_
{t_k = \frac{1}{k}\sum_\gamma^n \lambda_\gamma^{-k}} =
\left(\prod_\gamma^n \lambda_\gamma\right)
\sum_\gamma \frac{(-)^{\gamma+1}\Delta_\gamma(\lambda)}{\Delta(\lambda)}
\lambda_\gamma^i\varphi_{-j}(\lambda_\gamma).
\label{derivkpvertod1}
\ee
As far as $n$ is kept finite, determinant of the infinite-size matrix
(\ref{derivkpvertod1}),
$\displaystyle{\left.{\rm Det}_{i,j<0}{\cal H}^{KP}_{ij}\right|_{t_k =
\frac{1}{k}\sum_\gamma^n \lambda_\gamma^{-k}} = 0}$
since it is obvious from (\ref{derivkpvertod1}) that
the rank of the matrix is equal to $n$. Therefore let us consider the maximal
non-vanishing determinant,
\be
\new
\begin{array}{c}
\left.{\rm Det}_{-n\leq i,j<0}{\cal H}^{KP}_{ij}\right|_{t_k =
\frac{1}{k}\sum_\gamma^n \lambda_\gamma^{-k}} = \\ =
\left(\prod_\gamma^n \lambda_\gamma\right)^n
{\rm det}_{i\gamma} \left(
\frac{(-)^{\gamma+1}\Delta_\gamma(\lambda)}{\lambda_\gamma^i\Delta(\lambda)}
\right)
\cdot {\rm det}_{\gamma j}\varphi_{j}(\lambda_\gamma)
=  \\ =
\frac{{\rm det}_{\gamma j}\varphi_{j}(\lambda_\gamma)}{\Delta(\lambda)}.
\end{array}
\label{derivkpvertod2}
\ee
We used here the fact that determinant of a matrix is a product of
determinants and reversed the signs of $i$ and $j$. Also used were some simple
relations:
\be
\new
\begin{array}{lc}
&\prod_{\gamma=1}^n \frac{\Delta_\gamma(\lambda)}{\Delta(\lambda)} =
\frac{1}{\Delta^2(\lambda)}, \nn \\
&{\rm det}_{i\gamma}\frac{1}{\lambda_\gamma^i} = \left(\prod_\gamma^n
\lambda_\gamma\right)^{-1}\Delta(1/\lambda), \\
&\Delta(1/\lambda)  = \prod_{\alpha>\beta}\left(\frac{1}{\lambda_\alpha} -
\frac{1}{\lambda_\beta}\right) = (-)^{n(n-1)/2} \Delta(\lambda)
\left(\prod_\gamma^n\lambda_\gamma\right)^{-(n-1)},  \\
{\rm thus}& \\
&\left(\prod_\gamma^n\lambda_\gamma\right)(-)^{n(n-1)/2}
\prod_{\gamma=1}^n \frac{\Delta_\gamma(\lambda)}{\Delta(\lambda)}
{\rm det}_{i\gamma}\frac{1}{\lambda_\gamma^i} = \frac{1}{\Delta(\lambda)}.
\end{array}
\ee
Since (\ref{derivkpvertod2}) is true for any $n$, one can claim that in the
limit $n \rightarrow \infty$ we recover the statement, that
$\tau^{KP}\{t\} = {\rm Det}_{i,j<0} {\cal H}_{ij}^{KP}$ with
${\cal H}_{ij}^{KP}$ given by eq.(\ref{derivkpvertod1}) (that formula does
not refer directly to Miwa parametrization and is defined for any $t$ and any
$j<0$ and $i$). This relation between $\varphi_\gamma$'s and ${\cal
H}_{ij}^{KP}$ can now be used to introduce negative times $\bar t_k$ according
to the rule (\ref{addkptau2}). Especially simple is the prescription for
zero-time: ${\cal H}_{ij} \rightarrow {\cal H}_{i+N,j+N}$, when expressed in
terms of $\varphi$ just implies that
\be
\frac{{\rm det}\ \varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)} \rightarrow
\frac{{\rm det}\ \varphi_{\gamma +N}(\lambda_\delta)}
{({\rm det}\Lambda)^N\Delta(\lambda)}.
\ee
Generalizations of  (\ref{addkptau3}), like
\be
{\cal H}_{ij}\{t,\bar t\} = \oint \oint z^i\bar z^j
\langle 0 \mid \psi(z) \ G\ \tilde\psi(\bar z)\mid 0 \rangle
e^{\sum_{k} (t_kz^k + \bar t_k\bar z^k)} dzd\bar z,
\ee
also can be considered.
