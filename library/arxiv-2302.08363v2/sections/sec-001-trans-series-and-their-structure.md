---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-001-trans-series-and-their-structure
section_title: "Trans-series and their structure"
section_number: null
pages: 2-5
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.603
latex_coverage_ratio: 0.678
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
\label{tss-sec}
In this paper we will consider trans-series involving two small parameters: a coupling 
constant $g$ and an exponentially small term of the form 

\be
y = g^{-b} \re^{-A/g}. 
\ee

These trans-series are of the form 

\be
\label{phits}
\Phi= \sum_{\ell \ge 0} y^{\ell}  \varphi_\ell (g), 
\ee

where 

\be
 \label{trans-not}
 \varphi_\ell (g)= \sum_{n \ge 0} a_{n, \ell} g^n
\ee

 are formal power series in $g$. Some of the examples we will consider 
 will be however slightly more general, including for example logarithmic terms, or involving 
 finite sums of expressions like (\ref{phits}). The series $\varphi_0(g)$ is the perturbative series, 
 and the higher order series $\varphi_\ell (g)$, with $\ell\ge 1$, 
 are non-perturbative corrections. These could be of the instanton or the renormalon type, 
and in this paper we will consider both of them. In general the coefficients $a_{n, \ell}$ for $\ell\ge 1$ are complex and they 
depend on a choice of lateral resummation (in the case of ODEs, there is a dependence on a trans-series parameter $C$, 
and different choices of resummation lead to different choices of $C$). We will specify such a choice as 
needed. 

The series $\varphi_\ell(g)$ are typically Gevrey-1, i.e. their coefficients have the factorial growth 

\be
a_{n, \ell} \sim n!, \qquad n \gg 1, 
\ee

at fixed $\ell$. This means that $\varphi_\ell(g)$ have zero radius of convergence. One way to make sense of these series is 
to use generalized or lateral Borel resummations  $s_\pm (\varphi)(g)$ (see e.g. \cite{mmbook} for an introductory 
survey of Borel resummation techniques). We will assume that these resummations exist, for sufficiently small $g$. 
The Borel resummed trans-series is then given by 

\be
\label{br-transseries}
s_\pm (\Phi)= \sum_{\ell \ge 0} y^{\ell} s_\pm (\varphi_\ell)(g). 
\ee

As we see, this object is itself an infinite sum over all exponentially small corrections. 
Even if the lateral Borel resummations exist and one can make sense in this way of the 
factorially divergent series $\varphi_\ell (g)$, the sum over the infinite number of 
non-perturbative sectors is potentially a new source of divergences. 
In the case of nonlinear ODEs, this infinite sum is known to converge provided 
${\rm Re}(g/A)$ is not too large \cite{costin}, but in general one has to address this convergence 
issue. 

We can reorganize $\Phi$ in a different way, suggested by the work of 
\cite{costin-costin} on non-linear ODEs: for each fixed power of $g$, $n$, we consider the series 

\be
\label{CGdef}
\CG_n(y)= \sum_{\ell \ge 0} a_{n, \ell} y^\ell,
\ee

so that we can write, formally, 

\be
\label{phi-y}
\Phi= \sum_{n \ge 0} g^n \CG_n (y).
\ee

We will call $\CG_n(y)$ the $n$-th partial series of the trans-series $\Phi$. 
An important result of \cite{costin-costin} is that, for non-linear ODEs, the partial series $\CG_n(y)$ are convergent, and 
they have the same radius of convergence for all $n$. Generically, we expect

\be
a_{n, \ell} \sim \ell^{-b_n} R^{-\ell}, \qquad \ell \gg 1,
\label{an-bn-R}
\ee

for fixed $n$. The common radius of convergence is $R$, while the exponents $b_n$ depend in general on $n$. 

In many situations, like the one considered in \cite{costin-costin}, 
the convergence property of the partial series is closely 
related to the convergence of the sum over exponential corrections in the Borel resummed trans-series (\ref{br-transseries}). 
Heuristically, this can be argued as follows. If $g$ is sufficiently small, we can 
approximate the lateral Borel resummations appearing in (\ref{br-transseries}) 
by uniform optimal truncations, i.e. we can truncate all factorially divergent series 
$\varphi_\ell(g)$ in (\ref{trans-not}) at the same $n=N^\star$. 
This is because all these series have the same rate of divergence. The 
resulting approximation is nothing but the sum of the first $N^\star$ functions $\CG_n(y)$, which is convergent if the 
partial series converge. 
 
Let us note that the radius $R$ signals the occurrence of a common singularity in the functions $\CG_n(y)$. One can 
ask what is the relation between the location of the singularity in the $\CG_n$s, and the location of the singularities of the 
exact function represented by the resummed trans-series $\Phi$. As explained in \cite{costin-costin}, the singularity in the $\CG_n$s gives the first term in an asymptotic approximation to the singularities of the exact function. In the case of nonlinear ODEs, one also 
has that, for a fixed $|y|<R$ in the common domain of convergence, the functions $\CG_n(y)$ grow 
factorially \cite{costin-costin}, 

\be
\label{new-fact}
\CG_n(y) \sim n!, \qquad n\gg 1. 
\ee

Therefore, the expansion (\ref{phi-y}) provides an asymptotic representation of the 
Borel-resummed trans-series for small $g$ and $|y|<R$ which is very different from the asymptotic representation 
provided by $\varphi_0(g)$. We believe that the behavior (\ref{new-fact}) also occurs in the QFT trans-series which satisfy the 
convergence property. 

In the following sections, we will consider interesting examples in QFT where the convergence property of the trans-series 
holds. 


   



\sectiono{The large \texorpdfstring{$N$}{N} sigma model, revisited} 
\label{sec-sigma}



One of the most explicit results for a trans-series expansion in QFT was obtained in \cite{beneke-braun} for the 
self-energy of the $O(N)$ non-linear sigma model, at the first non-trivial order in the $1/N$ expansion. Let us briefly review 
the result and analyze the properties of the trans-series. 

The basic field of the $O(N)$ non-linear sigma model is a scalar 
field $\boldsymbol{\sigma}: \IR^2 \rightarrow \IR^N$ satisfying the constraint

\be
\boldsymbol{\sigma}^2=1. 
\ee

The Lagrangian density is 

\be
\CL={1\over 2 g_0^2}  \partial_\mu \boldsymbol{\sigma} \cdot  \partial^\mu {\boldsymbol{\sigma}}, 
\ee

where $g_0$ is the bare coupling constant. As it is well-known, this model can be solved order by order in the $1/N$ expansion. 
In particular, one can find an explicit formula for the self-energy $\Sigma(p)$ at NLO in $1/N$. This was calculated in \cite{cr-dr} by using a convenient sharp momentum (SM) cutoff regularization, and one finds: 

\be
\Sigma(p)=p^2+ m^2 +{m^2 \over N} S\left( {p^2 \over m^2} \right) + \CO\left({1\over N^2} \right), 
\ee

Here, $m$ is the mass gap, and $S(x)$ is given by 


 \be
 \label{Sx}
 S(x)= \int_0^\infty \rd y \left(  \log\left( {\xi+ 1  \over \xi-1}  \right)\right)^{-1} \left[  {y  \xi \over {\sqrt{(1+ y +x)^2-4 x y}}} -1+
  {x+ 1 \over 2} \left( {1\over \xi}-1\right) \right]. 
  \ee
  
 In this expression we have denoted
 
 \be
 \xi ={\sqrt{1+ {4 \over y}}}. 
 \ee
 
Since $m$ is proportional to the dynamically generated scale, it is natural to introduce a renormalized 
coupling at the scale $p$, $g(p)$, by 

\be
{1\over x}={ m^2 \over p^2}= \re^{-1/g(p)}.
\ee

We expect that $S(x)$, for small $x$, is given by a perturbative series in $g(p)$, together 
with non-perturbative, exponentially small corrections. The perturbative expansion was obtained in 
\cite{cr-dr}, while the full trans-series was obtained in \cite{beneke-braun} 
in a slightly different renormalization scheme. We will now present the final result of this remarkable calculation\footnote{Some details are clarified and worked out in \cite{sss}, which extends the result of \cite{beneke-braun} to the supersymmetric non-linear sigma model. Similar results for the Gross--Neveu model are discussed in \cite{kneur}.}. 

The ingredients of the trans-series are contained in three sequences of 
functions of an auxiliary variable $t$, 
which can be regarded in fact as a Borel transform variable. The first sequence is denoted by $F_\ell(t)$, $\ell \ge 0$, 
and given explicitly by 

\be
F_\ell(t)= \sum_{j=0}^\ell 2(2t ^2 -t-j){\Gamma(2t+2j-1) \over \Gamma(2t+j+1)}{1 \over j!}\left[ {\Gamma(\ell+t-1) \over \Gamma(t+j-1) \Gamma(\ell-j+1)} \right]^2. 
\ee

It can be easily checked that the $F_\ell(t)$ are polynomials in $t$ of degree $2\ell$. One finds, for example 

\be
F_0(t)=1, \qquad F_1 (t)= t^2-1, \qquad F_2(t)= \frac{1}{4} \left(t^4+6 t^3+t^2-4 t-8\right). 
\ee

The second sequence of functions is denoted by $G_\ell(t)$, with $\ell\ge 0$, and given explicitly by 

\be
\ba
G_\ell(t)&=-F_\ell(t) (\psi(t+\ell-1)+\psi(2-t-\ell))\\
&+ \sum_{j=0}^\ell 4(2t ^2 -t-j)\psi(\ell+1-j) {\Gamma(2t+2j-1) \over \Gamma(2t+j+1)}{1 \over j!}\left[ {\Gamma(\ell+t-1) \over \Gamma(t+j-1) \Gamma(\ell-j+1)} \right]^2.
\ea
\ee

Here, $\psi(t)$ is the digamma function. The functions $G_\ell(t)$ are meromorphic and have poles at all non-negative integers and some negative integers. One finds, for example, 

\be
\ba
G_0(t)&= -2 \gamma_E - \psi(-1+t) -\psi(2-t),\\
 G_1(t)&=(t-1) \left(-2 ((\gamma_E -1) t+\gamma_E +1)-(t+1) \psi (1-t)-(t+1) \psi (t) \right), 
 \ea
\ee

where $\gamma_E$ is the Euler--Mascheroni constant. The third, and final sequence of functions, is 
denoted by $H_\ell(t)$. One has 

\be
\ba
H_0(t)&= {1\over t} -{1 \over t+1}, \\
H_1(t)&=-\frac{1}{t}+\frac{2}{t+1}-\frac{1}{t-1}, \\
H_\ell(t)&= (-1)^{\ell-1} \sum_{j=0}^{\ell-1}\left(  {(\ell-2)! \over (\ell-j-2)! j!} \right)^2 2(2 t^2+j-\ell) (2\ell-2j-2)! \prod_{a=j-\ell}^{\ell-j} (t+a)^{-1}, \qquad \ell \ge 2. 
\ea
\ee

$H_\ell(t)$ is a rational function of $t$ with poles at $t=0, \pm 1, \cdots, \pm \ell$. One has in addition the following 
property,

\be
\label{resHresG}
{\rm Res}_{t=k} H_{\ell+k}(t)= {\rm Res}_{t=k} G_{\ell}(t), \qquad k \in \IZ_{\ge 0},  
\ee

for all $\ell\ge 0$. We note that the functions $H_{0,1}(t)$ differ from the ones appearing in \cite{beneke-braun}, due to a difference 
choice of renormalization scheme. 

We have now all ingredients to construct the formal trans-series. Let us first define 

\be
r_{\ell,k} = {\rm Res}_{t=k} \, H_\ell(t)
\ee

as well as the function 

\be
\widehat G_\ell(t)= G_\ell(t) - \frac{r_{\ell,0}}{t},
\ee

which is regular at the origin, due to (\ref{resHresG}). We now define the formal series

\be
\label{sigma-trans}
\varphi_\ell(g)= F_\ell (0)+ \sum_{n\ge 1} \left( F_\ell^{(n)}(0) + \widehat G_\ell^{(n-1)}(0)  \right) g^{n}, \qquad \ell \ge 0. 
 \ee
 
 We will also need the integrals

\begin{equation}
c_\ell = -{\rm{P}} \int_0^\infty \left( H_\ell(t) -r_{\ell,0} \frac{ \re^{-t}}{t} \right) \rd t.
\end{equation}

Let us now consider the trans-series 

\be
\label{beneke-ts}
\Phi_\pm =\sum_{\ell \ge 0} (-1)^\ell \re^{-\ell/g} \left( r_{\ell,0}\log(g) + c_\ell  \pm \ri\pi \sum_{k=1}^\ell r_{\ell,k} + \varphi_\ell (g)  \right). 
\ee

This is slightly more general than the trans-series considered in (\ref{phits}) since it involves a logarithmic term. The 
main result of \cite{beneke-braun} is that the non-trivial integral (\ref{Sx}) appearing in the self-energy can be obtained 
as a lateral resummation of $\Phi_\pm$:

\begin{equation}
\label{restrans}
{1\over x} S(x) =s_\pm (\Phi_\pm)= \sum_{\ell \ge 0} (-1)^\ell \re^{-\ell/g} \left( r_{\ell,0}\log(g) + c_\ell  \pm \ri\pi \sum_{k=1}^\ell r_{\ell,k} + s_\pm (\varphi_\ell)(g) \right).
\end{equation}

Note that the constant, imaginary term of the trans-series is ambiguous and 
depends on the choice of lateral resummation, 
as expected since the work of David \cite{david2,david3}. As noted in \cite{beneke-braun}, 
the property (\ref{resHresG}) guarantees the cancellation of non-perturbative ambiguities, i.e. 
it guarantees that the two lateral resummations in (\ref{restrans}), with the correlated choice of sign in the 
imaginary piece, give the same result. 

From the above results one obtains e.g. the asymptotic behavior for the self-energy, which is given by the conventional perturbative series:

\be
\frac{1}{x}S(x) \sim \log(g) + 1 - \gamma_E -2 g +  \sum_{k \ge 1 }k! \left( \left(1+(-1)^k\right)\zeta(k+1) - 2 \right) g^{k+1}. 
\ee

This was first found in \cite{cr-dr} (the constant term of this series differs from the result quoted in \cite{beneke-braun}, 
since our functions $H_{0,1}(t)$ are different from theirs).

We can now address the main question raised in this paper. We have a family of formal series (\ref{sigma-trans}) and, in the notation of (\ref{trans-not}), their coefficients are given by 

\be
a_{0, \ell}= F_\ell (0), \qquad a_{n,\ell}= F_\ell^{(n)}(0) + G_\ell^{(n-1)}(0), \quad n \ge 1. 
\ee

We want to determine the behavior of these coefficients for large $\ell$ and fixed $n$. We find, numerically, 

\be 
\label{anl-sigma}
a_{n, \ell} \sim C_n {9^\ell \over \ell^2}, \qquad \ell \gg 1, 
\ee

where $C_n$ is an $n$-dependent constant. We have verified this behavior for 
many values of $n\le 20$, and we conjecture that this asymptotic behavior holds for 
all $n \ge 0$. This implies in particular that the series $\CG_n(y)$ are convergent and 
they have the same radius of convergence for all $n$, namely, $R=1/9$. We have also found 
numerically that $C_n \sim n!$, as one would 
expect from (\ref{new-fact}). Let us also note that the coefficients $c_{\ell}$, $r_{\ell, 0}$ 
appearing in (\ref{beneke-ts}), as well as the sum 

\be
\sum_{k=1}^\ell r_{\ell, k}
\ee

have the same asymptotic behavior for large $\ell$ as the coefficients $a_{n, \ell}$, namely $9^\ell/ \ell^2$. 
In particular, we find a singularity of 
the partial series at 

\be
\label{sing-sigma}
{m^2 \over p^2}= -{1 \over 9}. 
\ee


To illustrate the behavior (\ref{anl-sigma}), we plot in \figref{vert-series} the sequence 

\be
\label{quot-seq}
s^{(n)}_{\ell}= {a_{n,\ell } \over 9^\ell \ell^{-2}}
\ee

for $\ell=1,\cdots, 60$, and $n=1,6$, together with their Richardson transform of order $3$. It is manifest that they converge rapidly to an $n$-dependent constant. 

 \begin{figure}
\center
\includegraphics[width=0.4\textwidth]{coeff1.pdf} \qquad \qquad 
\includegraphics[width=0.4\textwidth]{coeff6.pdf} 
\caption{The sequences (\ref{quot-seq}) for $n=1$ (left) and $n=6$ (right), represented by black dots, together with their Richardson 
transforms of order $3$, represented by red dots.}
\label{vert-series}
\end{figure}

As we explained in section \ref{tss-sec}, we expect that the convergence property of 
the partial series implies the convergence of the 
full trans-series. In this example, this is realized in a simple way, and the 
common radius of convergence that we have found for the series $\CG_n(y)$ is actually the same one that was found 
in \cite{beneke-braun} for the full resummed trans-series. However, the two radius of convergence 
do not need to match, in general. The present trans-series is peculiar in this regard, related to the 
fact that the parameters $b_n$ of \eqref{an-bn-R} are in this case the same for all $n$. In the trans-series of the free energy discussed in section \ref{sec-integrable}, the $b_n$ does change with $n$, and the radius of convergence extracted from the partial series can only provide an approximation for the radius of the full trans-series.

We have verified the convergence property of partial series for the trans-series representing 
the large $N$ two-point function, but we expect this property to fail at finite $N$. The reason is the following. 
It is easy to check from the 
explicit expression for $S(x)$ that the two-point function at large $N$ has a single singularity at 
precisely the point (\ref{sing-sigma}), which is also the common location of the singularity for the 
series $\CG_n(y)$, see \figref{fig-sing1}. Physically, this represents the threshold for production of 
three particles of mass $m$, as noted in \cite{beneke-braun}, and it is 
a consequence of working at large $N$. At finite $N$ there will be infinitely many multi-particle 
thresholds, and we expect singularities at $p^2/m^2= -(2k+1)^2$, $k \in \IZ_{>0}$, as show on the right at \figref{fig-sing1}. 
As pointed out in \cite{shifman, shifman-hadrons}, this analytic structure can not be 
obtained from a convergent trans-series, and in particular from a trans-series with the 
convergent property of partial series. 
Heuristically, we expect that a trans-series with the latter property will lead to singularities 
in a bounded set of the $p^2/m^2$ plane, the farthest singularity being approximated by the common singularity of the partial series. 
This is the case for the two-point function at large $N$, but not at finite $N$. 

As an additional observation, let us mention that the trans-series (\ref{beneke-ts}) is a clear example 
in which the strong version of the resurgence program discussed in \cite{dmss} does {\it not} hold. 
According to the strong version, all the 
non-perturbative corrections appearing 
in the trans-series should be obtained from the analysis of the 
Borel singularities of the perturbative series, perhaps up to 
overall multiplicative constants. However, it is easy to see that the first 
Borel singularity of $\varphi_0(g)$ leads to a trivial trans-series, proportional to 
$\re^{-1/g}$, and can not in any way reconstruct the full $\varphi_1(g)$. This is similar to the examples 
found in \cite{dmss}, and it might be due to the fact that the trans-series 
(\ref{beneke-ts}) is obtained at a fixed order in the 
large $N$ expansion.  



 \begin{figure}
\center
\includegraphics[width=.8\textwidth]{sing2pt.pdf} 
\caption{The singularity structure of the large $N$ two point function 
is shown on the left, in the $p^2/m^2$ plane. There is a single branch cut 
singularity at $-9$, as it follows from (\ref{sing-sigma}). At finite $N$, it has 
been argued in \cite{beneke-braun} that there will be 
many singularities along the negative real axis, at positions $-(2k+1)^2$, 
$k \in \IZ_{>0}$, as shown on the figure on the right.}
\label{fig-sing1}
\end{figure}
