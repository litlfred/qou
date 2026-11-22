---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-001-2-warmup-quantization-of-ht2
section_title: "Warmup: quantization of H(T2)"
section_number: 2
pages: 4-8
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.997
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:quant}

To get a feel for the structure of complex Chern-Simons theory, we begin with a (seemingly) elementary exercise: the quantization of the phase space that $SL(2,\BC)$ Chern-Simons theory attaches to a two-torus.

First, some generalities. As discussed in \cite{DIWitten-cx}, the action of complex Chern-Simons theory on a Euclidean three-manifold $M$ takes the form

\DIbe I_{k,s} = \tfrac12(k+is)S_{CS}(\CalA) + \tfrac12(k-is)S_{CS}(\ol\CalA)\,, \label{DI.action} \DIee

where $S_{CS} = \frac{1}{4\pi}\int_M \text{Tr}\big(\CalA\wedge\CalA+\frac23\CalA\wedge\CalA\wedge\CalA\big)$ is the usual Chern-Simons functional. Here $\CalA$ is a connection on an $SL(2,\BC)$ bundle over $M$, and $\ol \CalA$ is its complex conjugate. The group $SL(2,\BC)$ contains $SU(2)$ as its maximal compact subgroup (in fact, as a complex manifold, $SL(2,\BC)\simeq T^*SU(2)$), and on a compact 3-manifold $M$ there can be large gauge transformations $g:M\to SL(2,\BC)$ that wrap nontrivially around the compact $SU(2)$. The path-integral integration measure $\exp(i I_{k,s})$ is invariant under large gauge transformations on a closed $M$ so long as $k\in \BZ$. On the other hand, the coupling constant $s$ is unconstrained.

For a unitary theory --- which in Euclidean space means that partition functions are conjugated under orientation reversal --- the action must be real, which forces $s$ to be real. We will assume this to be true in the quantization below, though eventually in partition functions we will find that we can analytically continue $s$ in a straightforward manner. There also exist exotic unitarity structures with $s$ imaginary \cite{DIWitten-cx}, which will lead to slightly different Hilbert spaces.


As an aside, in the relation to 3d Euclidean gravity with a negative cosmological constant, one identifies the Hermitian and anti-Hermitian parts of $\CalA = w+ie$ as a vielbein $(e)$ and a spin connection $(w)$. The part of the action $I_{k,s}$ proportional to $s$ becomes the usual Einstein-Hilbert action, while the part proportional to $k$ is a gravitational Chern-Simons term \cite{DIWitten-gravCS}. The classical solutions of Chern-Simons theory on a three-maniofld $M$ are flat $SL(2,\BC)$ connections, which become identified with (possibly degenerate) metrics of constant negative curvature, \DIie\ hyperbolic metrics, in 3d gravity.



Geometric quantization of complex Chern-Simons theory on a general surface $\Sigma$ was first discussed in \cite{DIWitten-cx} and recently revisited in \cite{DIAG-HW}, using a holomorphic polarization. A more modern perspective on quantization, based on the topological A-model, appears in \cite{DIDGLZ}, following \cite{DIGW-branes} (see also \cite{DImirrorbranes}). In the case of $\Sigma=T^2$, we can take a more pedestrian approach, following \cite{DID-levelk, DIAK-complexCS}.

The Hilbert space that Chern-Simons theory assigns to any surface $\Sigma$ is a quantization of the classical phase space

\DIbe \CalP[\Sigma] = \CalM_{\rm flat}(SL(2,\BC),\Sigma) \simeq {\rm Hom}(\pi_1(\Sigma),SL(2,\BC))\,. \label{DI.PS} \DIee

This is the space of complex flat connections on $\Sigma$ (modulo gauge transformations), or equivalently, the space of representations of the fundamental group of $\Sigma$ in $SL(2,\BC)$. The space $\CalP[\Sigma]$ is a finite-dimensional complex symplectic variety, possibly singular, equipped with the Atiyah-Bott holomorphic symplectic form

\DIbe \Omega = \int_\Sigma \delta \CalA \wedge \delta \CalA\,. \label{DI.AB} \DIee

Of course, the actual symplectic form we use for quantization should be real; the Chern-Simons action \eqref{DI.action} tells us to take

\DIbe \omega_{k,s} = \frac{k+is}{4\pi}\,\Omega + \frac{k-is}{4\pi}\, \ol\Omega = \frac{k}{2\pi}\text{Re}\,\Omega - \frac{s}{2\pi}\text{Im}\,\Omega\,. \DIee


Famously, the space $\CalP[\Sigma]$ is hyperk\"ahler. It admits an entire $\cp^1$ of complex structures, one of which is singled out in the description \eqref{DI.PS} as a space of complex flat connections. The other complex structures can be made manifest by rewriting $\CalP[\Sigma]$ as Hitchin's moduli space $\CalP[\Sigma]\simeq \CalM_{\rm Hit}(SU(2),\Sigma)$ associated to the compact group $SU(2)$ \cite{DIHitchin-SD}. Similarly, the space $\CalP[\Sigma]$ admits a $\cp^1$ of real symplectic forms, spanned by the hyperk\"ahler triplet $(\omega_I,\omega_J,\omega_K)$, where $\omega_I=\text{Re}\,\Omega$ and $\omega_J = \text{Im}\,\Omega$ above. The third form $\omega_J$ is a K\"ahler form in our chosen complex structure. Notably, $\frac{1}{4\pi^2}\omega_I$ represents a nontrivial \emph{integral} cohomology class in $H^2(\CalP[\Sigma],\BZ)$, while $\omega_J,\omega_K$ are cohomologically trivial. This provides another explanation for the quantization of the level $k$: in geometric quantization, one requires $\omega_{k,s}$ to be the first Chern class of a line bundle, which can only happen if it has integral periods, whence $k\in \BZ$, but $s$ is unconstrained.



Now let us specialize to $\Sigma=T^2$. Flat connections on a torus are determined by the holonomies $\rho_A,\rho_B$ along the $A$ and $B$ cycles, up to $SL(2,\BC)$ conjugation. Since the fundamental group $\pi_1(T^2)=\BZ^2$ is abelian, the holonomies commute and can be simultaneously diagonalized.

\footnote{More precisely: the holonomies can simultaneously be put in Jordan normal form.} 

Letting $x,y$ denote their eigenvalues, we find

\DIbe \CalP[T^2] = (\BC^*\times \BC^*)/\BZ_2 \simeq \{(x,y)\in (\BC^*)^2\}/\raisebox{-.1cm}{$(x,y)\sim (x^{-1},y^{-1})$}\,.\DIee

The $\BZ_2$ action here is just that of the Weyl group, acting as residual gauge transformations.
The holomorphic symplectic form is

\DIbe \Omega = 2\,\frac{dy}{y}\wedge \frac{dx}{x}\,,\DIee

reflecting the nontrivial intersection of A and B cycles on $T^2$, whence

\DIbe \omega_{k,s} = \frac{k}{\pi}(d\log |y|\wedge d\log |x| - d\arg y\wedge d \arg x) -\frac{s}{\pi}(d\log|y|\wedge d\arg x +d\arg y\wedge d\log |x|)\,. \DIee

As anticipated, the period of $\frac{1}{2\pi}\omega_{k,s}$ on the compact $(S^1\times S^1)/\BZ_2$ cycle in $\CalP[T^2]$ is equal to $k$, and is properly quantized.

In order to diagonalize the real symplectic form $\omega_{k,s}$, we define $b$ to be the complex number with $\text{Re}(b)>0$ and

\DIbe b^2 = \frac{k-is}{k+is}\,, \label{DI.defb}\DIee

and make a change of variables

\footnote{The new variables absorb some powers of the coupling constants $k,b$, which obfuscates the effect of the classical limit $k\to\infty$, \DIeg\ in \eqref{DI.nmcomm}. It is important to keep in mind that the natural functions on the phase space are still $x,\bar x,y,\bar y$.} 

from $(x,y)\in (\BC^*)^2$ to $(\mu,\nu;m,n)\in \BR^2\times (\BR/2k\BZ)^2$\,:

\DIbe \label{DI.defxy}
 \begin{array}{ll} x = \exp \frac{i\pi }{k}\big(-ib\mu-m\big)\,,\qquad & \bar x =  \exp \frac{i\pi }{k}\big(-ib^{-1}\mu+m\big)\,, \\[.1cm]
y = \exp \frac{i\pi }{k}\big(-ib\nu-n\big)\,,\qquad & \bar y =  \exp \frac{i\pi }{k}\big(-ib^{-1}\nu+n\big)\,.\end{array}
\DIee

Notice that if $s$ is real then $|b|=1$, so $(x,y)$ and $(\bar x,\bar y)$ are complex conjugates, as written. Then the symplectic form collapses to

\DIbe \omega_{k,s} = \frac{\pi}{k} d\nu\wedge d\mu - \frac{\pi}{k}dn\wedge dm\,.\DIee


We proceed to quantize the space as if it were just $\BC^*\times\BC^*$, and restore Weyl invariance later.
The functions $\nu,\mu$ and $n,m$ can simply be quantized to operators with canonical commutation relations

\DIbe -[\bm \nu,\bm \mu] = [\mb n,\mb m] = \frac{k}{i \pi}\,. \label{DI.nmcomm} \DIee

Of course, since $m$ is periodic the spectrum of $\mb n$ is quantized, and vice versa; altogether, both the eigenvalues of both $\mb m$ and $\mb n$ must belong to $\BZ/(2k\BZ)$. The well-defined operators are actually quantizations $\mb x,\bar{\mb x},\mb y,\bar{\mb y}$ of the $\BC^*$-valued functions in \eqref{DI.defxy}, with  $\mb x = \exp \frac{i\pi }{k}\big(-ib\bm\mu-\mb m\big)$, etc. For these we find

\DIbe \mb y \mb x  = q^{\frac12} \mb x\mb y\,,\quad \bar{\mb y}\bar{\mb x}=\tilde q^{\frac12}\bar{\mb x}\bar{\mb y}\,;\qquad \mb x\bar{\mb y} = \bar{\mb y}{\mb x}\,,\quad  \mb y\bar{\mb x} = \bar{\mb x}{\mb y}\,, \label{DI.qtorus} \DIee

with

\DIbe q^{\frac12} := \exp \frac{2\pi i}{k+is} = \exp{\tfrac{i\pi}{k}(b^2+1)}\,,\qquad \tilde q^{\frac12} := \exp \frac{2\pi i}{k-is} = \exp{\tfrac{i\pi}{k}(b^{-2}+1)}\,. \label{DI.qq} \DIee

Thus, abstractly, we see that the quantized operator algebra consists of two independent Weyl algebras (or ``quantum torus'' algebras), one in $\mb x,\mb y$ and one in $\bar{\mb x},\bar{\mb y}$.

There are many equivalent ways to represent the operator algebra on a Hilbert space $\CalH[T^2]$. The simplest is to take

\DIbe \CalH[T^2]_{k,s} = L^2(\BR)\otimes \BC^{2|k|} \simeq \{f(\mu,m)\} \label{DI.Hks} \DIee

to consist of functions of a real variable $\mu$ and an integer $m\in \BZ/(2k\BZ)$. Equivalently, we may take functions of $x$ and $\bar x$. Formally, in geometric quantization, this corresponds to choosing a particular ``real'' polarization --- taking sections of a line bundle $\CalL\to\CalP[\Sigma]$ with $c_1(\CalL)=\omega_{k,s}$ that are covariantly constant with respect to $\nu$ and $n$. The operators $\mb x,\bar{\mb x}$ act on $f(\mu,m)$ as multiplication by $x,\bar x$, while $\mb y,\bar{\mb y}$ are shifts

\DIbe \mb y\,f(\mu,m) = f(\mu+ib,m-1)\,,\qquad \bar{\mb y}\,f(\mu,m) = f(\mu+ib^{-1},m+1)\,.\DIee


To restore Weyl-invariance, we restrict to the $\BZ_2$-invariant part of the Hilbert space, \DIie\ functions that are even

\DIbe f(\mu,m) = f(-\mu,-m)\,. \label{DI.Weyl} \DIee

Correspondingly, we should restrict to a subalgebra of the operator algebra that is invariant under $(\mb x,\bar{\mb x},\mb y,\bar{\mb y})\to(\mb x^{-1},\bar{\mb x}^{-1},\mb y^{-1},\bar{\mb y}^{-1})$. This subalgebra is generated by operators $\mb X=\mb x+\mb x^{-1}$, $\mb Y=\mb y+ \mb y^{-1}$, and $\mb T=\mb{xy} + \mb x^{-1} \mb y^{-1}$ (and their conjugates), which obey

\DIbe \mb X^2 + \mb Y^2 + q^{-\frac12}\mb T^2 = \mb X\mb T\mb Y +2(1+q^{-1})\,. \DIee


When $k=0$, complex Chern-Simons theory still make sense (as long as $s\neq 0$), but the above quantization procedure requires a slight modification \cite{DIDGG-index}. The change of variables \eqref{DI.defxy} does not make sense, and is not necessary, since $\omega_{k=0,s}$ is already diagonalized. Indeed, $\omega_{k=0,s}$ is the canonical symplectic form on $\BC^*\times \BC^*$ when viewed as the cotangent bundle $T^*(S^1\times S^1)$. We expect quantization to produce $\CalH[T^2]_{0,s} = L^2(\BZ\times \BZ)$. To see it, simply write $(x,y)=(e^{\frac{\pi}{s}m+i\theta}, e^{\frac\pi s n+i\phi})$. The symplectic form becomes

\DIbe \omega_{k=0,s} = - dn\wedge d\theta + dm\wedge d\phi\,. \DIee

These canonically-conjugate functions are quantized to operators with $[\bm \theta,\mb n]= - [\bm \phi,\mb m]=i$.
Since $\theta,\phi$ are periodic with period $2\pi$, the eigenvalues of $\mb m,\mb n$ must be integers. We can represent the operator algebra (say) on functions $f(m,n)$ of two integers, such that

\DIbe \label{DI.index-fmn}
 \begin{array}{ll}   \mb x\, f(m,n) = q^{\frac m4} f(m,n-1)\,,\quad &\bar{\mb x}\,f(m,n) = \tilde q^{-\frac m4} f(m,n+1)\,, \\[.1cm]
 \mb y\, f(m,n) = q^{\frac n4} f(m+1,n)\,,\quad &\bar{\mb y}\,f(m,n) = \tilde q^{-\frac n4} f(m-1,n)\,, \end{array}\DIee

where now \eqref{DI.qq} reduces to

\DIbe q^{\frac14} = \tilde q^{-\frac 14} := \exp \frac \pi s\,. \label{DI.qq-index} \DIee

With these new definitions of $q$ and $\tilde q$, the operators satisfy the standard quantum-torus relations \eqref{DI.qtorus}. Alternatively, and equivalently, we may take the Hilbert space to contain functions $g(m,\zeta)$ of an integer $m$ and a phase $\zeta=e^{i\theta}$, with

\DIbe \label{DI.index-fmz}
\begin{array}{ll}   \mb x\, g(m,\zeta) = q^{\frac m4}\zeta\, g(m,\zeta)\,,\quad &\bar{\mb x}\,g(m,\zeta) = \tilde q^{-\frac m4}\zeta^{-1} \,g(m,\zeta)\,. \\[.1cm]
 \mb y\, g(m,\zeta) = q^{\frac n4}\, g(m+1,q^{\frac14}\zeta)\,,\quad &\bar{\mb y}\,g(m,\zeta) = \tilde q^{-\frac n4} \,g(m-1,\tilde q^{-\frac n4} \zeta)\,. \end{array}\DIee

Again, we impose Weyl-invariance at the end by restricting to even functions $f(m,n)=f(-m,-n)$ or $g(m,\zeta)=g(-m,\zeta^{-1})$.
