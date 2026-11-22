---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-010-b2-the-chgue-limit-a0-and-factorisation
section_title: "B.2 The chGUE limit a0 and factorisation"
section_number: null
pages: 21-22
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.725
latex_coverage_ratio: 0.988
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Here we would like to perform a more detailed check. As it was shown
in \cite{ADSV} 
in the large-$N$ limit
the spectral density of the Hermitian Wilson Dirac operator behaves
like the density of a 
{\it finite} GUE-matrix of size $\nu\times\nu$ plus the microscopic
chGUE density. We therefore expect
that our general partition function will factorise in the limit
$a\to0$ into a finite GUE times a second chGUE partition function of the
remaining $2n$ eigenvalues. 

In order to show that we will first simplify ${\cal Z}_\nu^{(0)}$
further before using the de Bruijn integration theorem. Taking
eq. (\ref{Zev}) as a starting point we can use the fact that the jpdf
integrated over all variables 
is totally symmetric under exchange or relabeling of the
$d_j$ \footnote{Using this symmetry our manipulations from now on will
  not be valid 
in general for correlation functions.}.
We can split the variables into two sets, denoted by
$t_{j=1,\ldots,\nu}\equiv d_{j=1,\ldots,\nu}$, and
$s_{j=1,\ldots,2n}\equiv d_{j=\nu+1,\ldots,2n+\nu}$. If we do a Laplace
expansion of the determinant into blocks of sizes $2n\times 2n$ and
$\nu\times\nu$, we can split off a Vandermonde type determinant in the
variables $t_j$, after appropriately relabeling all other permutations:
\bea
{\cal Z}_\nu^{(0)} &\sim&
\int_{-\infty}^\infty\prod_{j=1}^{\nu}
dt_j\,\e^{-\frac{t_j^2}{4a^2}}
\Delta_{\nu}(\{t\})
\int_{-\infty}^\infty\prod_{j=1}^{2n}
ds_j\,\e^{-\frac{s_j^2}{4a^2}}\prod_{i=1}^{\nu}(s_j-t_i)
\ \Delta_{2n}(\{s\})
\label{ZprePf}\\
&&\times
\int_0^\infty\prod_{b=1}^{n} du_b
\e^{\frac{- u_b^2}{2a^2(1-a^2)}}
\left|
\begin{array}{cc}
\e^{\frac{s_1u_1}{2a^2}}\ldots
\e^{\frac{s_1u_n}{2a^2}}&\e^{-\frac{s_1u_1}{2a^2}}\ldots
\e^{-\frac{s_1u_n}{2a^2}}\\ 
\cdots          & \cdots\\
\e^{\frac{s_{2n}u_1}{2a^2}}\ldots\e^{\frac{s_{2n}u_n}{2a^2}}
&\e^{-\frac{s_{2n}u_1}{2a^2}}\ldots\e^{-\frac{s_{2n}u_n}{2a^2}}\\  
\end{array}\right|
\left|
\begin{array}{cccc}
1&{t_1}&\cdots&t_1^{\nu-1}\\
\cdots&\cdots          &\cdots& \cdots\\
1&t_{\nu}&\cdots &t_{\nu}^{\nu-1}
\end{array}\right|\!\!.\nn
\eea
We can now perform the integrations over $u_{1},\ldots,u_n$
with the help of the standard de Bruijn integral formula eq. (\ref{gendeB}).
To make it applicable we can simply multiply the weight factors into the
determinant, and we obtain the following result:
\bea
{\cal Z}_\nu^{(0)}\! &\sim&\!
\int_{-\infty}^\infty\prod_{j=1}^{\nu}
dt_j\,\e^{-\frac{t_j^2}{4a^2}}
\Delta_{\nu}(\{t\})^2\!
\int_{-\infty}^\infty\prod_{j=1}^{2n}
ds_j\,\e^{-\frac{s_j^2}{4a^2}}\prod_{i=1}^{\nu}(s_j-t_i)
\Delta_{2n}(\{s\})
\Pf_{1\leq i,j\leq 2n}\left[F(s_i-s_j)
\right]\!.\ \ \ \ \ \ \ 
\label{Zxt}
\eea
In eq. (\ref{Zxt}) we can make further use of the symmetry under
relabeling of the 
variables $s_j$ and the anti-symmetry of the Vandermonde determinant
to write the Pfaffian as the following product: 
\bea
{\cal Z}_\nu^{(0)} &\sim&
\int_{-\infty}^\infty\prod_{j=1}^{\nu}
dt_j\,\e^{-\frac{t_j^2}{4a^2}}
\Delta_{\nu}(\{t\})^2\!
\int_{-\infty}^\infty\prod_{j=1}^{2n}
ds_j\,\e^{-\frac{s_j^2}{4a^2}}\prod_{i=1}^{\nu}(s_j-t_i)
\ \Delta_{2n}(\{s\})
\prod_{k=1}^n F(s_{2k}-s_{2k-1}).\ \ \ \ \ \ 
\label{ZDevm=0}
\eea
Now consider the exponents of two consecutive variables, say $s_1$ and
$s_2$, from the Gaussian and the exponential part of $F$: 
\be
\exp\Big[{-\frac{s_1^2+s_2^2}{4a^2}}+
\frac{(s_{2}-s_{1})^2(1-a^2)}{8a^2}\Big]
=\exp\Big[-\frac{(s_1+s_2)^2}{8a^2}-\frac{(s_1-s_2)^2}{8}\Big].
\ee
In the limit $a\to0$ the first term on the right hand side will give a
delta-function, whereas the second Gaussian term remains:
\be
\lim_{a\to0}\sqrt{8a^2\pi}\exp\Big[-\frac{(s_1+s_2)^2}{8a^2}
-\frac{(s_1-s_2)^2}{8}\Big] = \delta(s_1+s_2)\ \e^{-s_1^2/2}\ .
\ee
In the same limit the error-function in eq. (\ref{Fm0}) becomes the
sign function (see e.g. \cite{PandeyMehta}), 
\be
\lim_{a\to0}\erf\Big[ (s_2-s_1)
\sqrt{\frac{(1-a^2)}{8a^2}}\Big]=\sign[s_2-s_1]\ .
\label{limerf}
\ee
We are now ready to take the limit $a\to0$ of the partition function
eq. (\ref{ZDevm=0}). We first formally
change variables $r_j=t_j/a$ 
to isolate the $a$-dependence, and then
take the limit only on the remaining $a$-dependence, that is the
variables $r_j$, 
\be
\lim_{a\to0}{\cal Z}_\nu^{(0)}
\sim\int_{-\infty}^\infty \prod_{j=1}^{\nu} dr_j \, 
\e^{-\frac{r_j^2}{4}}\Delta_{\nu}(\{ r \})^2 
\int_{-\infty}^\infty\prod_{j=1}^{n} ds_j \, 
s_j \sign[s_j] \exp\Big[{-\frac{s_j^2}{2}}\Big]
\prod_{i=1}^{\nu}(s_j^2 - a^2 r_i^2) \ 
\Delta_{n}(\{s^2\})^2.
\label{ZDeva0}
\ee
We have used the fact that for $s_{2k} \to - s_{2k-1}$ we obtain 
$\Delta_{2n}(\{s\}) \to \prod_{i=1}^n 2 s_i \ \Delta_n(\{s^2\})^2$.
The variables $r_j$ thus act as mass terms to the $s$-variables, 
but to leading order these masses can be neglected, leading to 
a complete decoupling of variables.
Our final result is thus reading
\be
\int_{-\infty}^\infty\prod_{j=1}^{\nu} dr_j \, 
\exp\Big[{-\frac{r_j^2}{4}}\Big]
\Delta_{\nu}(\{r\})^2
\int_{-\infty}^\infty\prod_{j=1}^{n}
ds_j\,|s_j|^{2\nu+1}\exp\Big[{-\frac{s_j^2}{2}}\Big]
\ \Delta_{n}(\{s^2\})^2,
\label{Zfactor}
\ee
where the $\nu$ would-be zero-eigenvalues at $a=0$ have decoupled into
a GUE of size $\nu$, 
times the standard massless chGUE with exactly $\nu$ zero eigenvalues.
However, we should remember that due to rescaling
the original variables $t_j$ are all of the order ${\cal O}(a)$.

It is clear how to this order of approximation the microscopic
spectral density would look like: it is the superposition of a
finite-$\nu$ semi-circle from the GUE and 
the Bessel spectral density with $\nu$ zero-eigenvalues from the
chGUE. This confirms the analysis of \cite{ADSV} on the level of the
partition function, to that order. 






\sect{Skew-orthogonal polynomials}\label{SOP-C}

In this appendix we compute the skew-orthogonal polynomials given in
eqs. (\ref{sOPs}) for $\nu=0$.
We first recall that the expectation value of a single characteristic
polynomial (or equivalently the $N_f=1$ partition function) gives the
even polynomials $R_{2j}$ where we follow the argument of
\cite{AKP}. This expectation value is
computed using the supersymmetric method in the next subsection
\ref{Reven}. Based on that the odd polynomials $R_{2j+1}$ then follow
as shown in \ref{Rodd}.

Starting from the quenched partition function eq. (\ref{Zjpdf}) for $\nu=0$
\be
{\cal Z}_0^{(0)}
=
\int_{-\infty}^\infty\prod_{j=1}^{2n}
ds_j w(s_j)
\ \Delta_{2n}(\{s\})\ \Pf_{1\leq i,j\leq 2n}[F(s_i-s_j)]\ ,
\ee
we can write the expectation value of a single determinant as follows:
\bea
\langle \det[z-\Dirac_5]\rangle_{2n}
&=&\frac{1}{{\cal Z}_0^{(0)}} \int_{-\infty}^\infty\prod_{j=1}^{2n}
ds_j w(s_j) (z-s_j)
\ \Delta_{2n}(\{s\})\ \Pf_{1\leq i,j\leq 2n}[F(s_i-s_j)]
\nn\\
&=&\frac{1}{{\cal Z}_0^{(0)}}
 \frac{(2n)!}{2^nn!}\int_{-\infty}^\infty\prod_{j=1}^{N}
ds_j w(s_j)
\ \Delta_{2n+1}(\{s\},z)\ \prod_{l=1}^nF(s_{2l}-s_{2l-1}).
\eea
Here we have used the fact that both the Vandermonde determinant and
the Pfaffian are antisymmetric 
in order to simplify their product (times the symmetric integral over
all eigenvalues), cf. \cite{Mehta} Appendix 25. Furthermore we have
included the determinant into a larger Vandermonde.
Writing the Vandermonde determinant in terms of even and odd monic
polynomials $\Phi_{2i}$ and $\Psi_{2i+1}$ respectively,
\be
\Delta_{2n+1}(\{s\},z)
=\det_{i=0,\ldots,n-1;j=1,\ldots,2n+1}\Big[\{\Phi_{2i}(s_j),
\Psi_{2i+1}(s_j)\}\ \Phi_{2n}(s_j) \Big]\ ,
\ee
and relabeling $z=s_{2n+1}$, we have from the generalised de Bruijn
formula (cf. \cite{AKP} eq. (4.9), or \cite{KG})
\be
\langle \det[z-\Dirac_5]\rangle_{2n}=
\frac{n!}{{\cal Z}_0^{(0)}}\ \Pf_{0\leq i,j\leq 2n}
\left[
\begin{array}{lll}
\langle \varphi_i,\varphi_j\rangle & \ldots& \varphi_0(s_{2n+1})\\
\ldots &&\cdots\\
&& \varphi_{2n}(s_{2n+1})\\
-\varphi_0(s_{2n+1})\ldots & -\varphi_{2n}(s_{2n+1})&0\\
\end{array}
\right],
\label{preskew}
\ee
for the set of all monic polynomials $\varphi_{i}=\{
\Phi_0, \Psi_1, \Phi_2, \Psi_3, \cdots, \Phi_{2 n}

\}$, with the scalar product defined in
eq. (\ref{skew}). Choosing polynomials $\varphi_j=R_j$ to satisfy the
skew-orthogonality eq. (\ref{skewdef}) we obtained the desired
relation
\be
R_{2n}(z)=\langle \det[z-\Dirac_5]\rangle_{2n}= \langle
\det[z+\Dirac_5]\rangle_{2n}\ ,
\label{Revenvev}
\ee
which obviously has parity.
