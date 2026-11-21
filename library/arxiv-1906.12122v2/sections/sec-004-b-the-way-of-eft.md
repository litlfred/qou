---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-004-b-the-way-of-eft
section_title: "B The way of EFT"
section_number: null
pages: 4-6
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.998
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsec:WayofEFT}

How does one ensure that a nuclear EFT reproduces QCD in the appropriate energy
domain?  Once degrees of freedom have been selected according to the energies
of interest, one constructs the most general Lagrangian $\mathcal{L}$ 
involving the corresponding set of fields $\{\psi\}$, which is constrained only
by the 
QCD symmetries,

\begin{equation}
 \LL = \sum_i c_i(\Mlo,\Mhi,\Lambda) \, O_i(\{\psi\}),
\label{Lexp}
\end{equation}

where the $O_i(\{\psi\})$ are operators that involve fields at the same 
spacetime point but contain an arbitrary number of derivatives, and 
$c_i(\Mlo,\Mhi,\Lambda)$ are the low-energy constants (LECs).  Here $\Lambda$
denotes an arbitrary regulator parameter with dimension of mass.  With $\LL$, or
the corresponding Hamiltonian, the propagation and interaction of the low-energy
degrees of freedom can be calculated.  The procedure might be entirely
perturbative, as represented by Feynman diagrams with a finite number 
of loops, or partially nonperturbative, as obtained by an infinite sum
of Feynman diagrams or the solution of an equivalent integral or differential
equation such as, respectively, the Lippmann-Schwinger or the Schr\"odinger 
equation.  In either case, the interactions are singular, which requires
regularization.  When the calculation can be reduced to a finite number of 
loops, dimensional regularization can be employed, which introduces a 
renormalization scale $\mu$.  However, in nuclear physics we are most often 
faced with summing an infinite number of loops with overlapping momenta
which, with present techniques, can only be made finite by the introduction,
at either interaction vertices or propagators, of a momentum-regulator function
$f(p/\Lambda)$ such that $f(0)=1$ and
{$f(x\to \infty) =0$}.  Here $p$ refers to the
momentum of a nucleon, in which case the regulator is separable, or the
transferred momentum, when the regulator is nonseparable.  We can alternatively
look at position space, where the nonseparable regulator is local (\ie, a 
function of position only) whereas the separable regulator is nonlocal.

The goal is to construct the $T$ matrix for a low-energy process
as an expansion in $Q/\Mhi<1$, schematically,

{
\begin{multline}
T(Q) = \NN \sum_{\nu= 0}^\infty \, 
 \left(\frac{Q}{\Mhi}\right)^{\!\nu} \\
 \null \times 
 F^{(\nu)}\!\left(\frac{Q}{\Mlo}, \frac{Q}{\Lambda}; 
 \gamma^{(\nu)}\!\left(\frac\Mlo\Mhi,\frac\Lambda\Mhi\right)
 \right) \,,
\label{Texp}
\end{multline}
}

where $\NN$ is a normalization factor, the $F^{(\nu)}$ are functions generated 
by the dynamics of the $\{\psi\}$, the $\gamma^{(\nu)}=\OO(1)$ are 
dimensionless combinations of the $c_i$, and $\nu$ is a counting index.
``Power counting'' is the relation between $\nu$ and the interaction label $i$ 
in Eq.~\eqref{Lexp}.  While the form of the $O_i$ in the Lagrangian~\eqref{Lexp}
depends on the choice of fields, the expansion~\eqref{Texp} must not
{\cite{Chisholm:1961tha,Kamefuchi:1961sb}}.  Likewise,
observables obtained from Eq.~(\ref{Texp}) must not depend on the arbitrary
regularization procedure---renormalization-group (RG) invariance.

Once the expansion~(\ref{Texp}) has been achieved, one can truncate the sum at 
a given $\nu=\mathcal{V}$ with a small error,

\begin{equation}
 T(Q\sim \Mlo)=T^{(\mathcal{V})}(Q,\Lambda)\left[1
 + \OO\left(\frac{Q^{{\mathcal{V}}+1}}{\Mhi^{{\mathcal{V}}+1}}\right)\right] \,.
\label{Ttrunc}
\end{equation}

Before renormalization, non-negative powers of $\Lambda$ can appear, which 
originate in the short-distance part of loops.  The uncertainty principle 
ensures that such contributions cannot be separated from that of LECs.
Renormalization is the procedure that fixes the cutoff dependence of the LECs
so that the truncated amplitude $T^{(\mathcal{V})}(Q,\Lambda)$ satisfies 
approximate RG invariance,

\begin{equation}
 \frac{\Lambda}{T^{(\mathcal{V})}(Q,\Lambda)}
 \frac{\dd T^{(\mathcal{V})}(Q,\Lambda)}{\dd\Lambda}
 =  \OO\left(\frac{Q^{{\mathcal{V}}+1}}{\Mhi^{\mathcal{V}}\Lambda}\right) \,.
\label{TRGtrunc}
\end{equation}

This condition ensures the error introduced by the arbitrary regularization 
procedure is no larger than the $Q/\Mhi$ error stemming from the neglect of
higher-order terms in Eq.~\eqref{Ttrunc}, as long as $\Lambda \simge \Mhi$.
In this ``modern view'' of renormalization, there is no need to take the 
$\Lambda \to \infty$ limit~\cite{Lepage:1989hf}.  However, while in analytical 
calculations Eq.~\eqref{TRGtrunc} can be verified explicitly, in numerical 
calculations varying the regulator parameter widely above the breakdown scale
is usually the only tool available to check RG invariance.  In contrast, 
$\Lambda < \Mhi$ generates relatively large errors from the regularization
procedure.  Failure to satisfy Eq.~\eqref{TRGtrunc} altogether means
uncontrolled sensitivity to short-distance physics: results depend on the value
of $\Lambda$ and on the choice of the regulator function $f(x)$, which acquires
the status of a physical, model-dependent ``form factor.''

After renormalization, when the contribution from momenta of the order
of the large cutoff have been removed, the dominant terms in loop integrals come
from momenta of $\OO(Q)$.  Counting powers of $Q$ in individual contributions
to Eq.~\eqref{Texp} is similar to determining the superficial degree of
divergence of diagrams.  There is, in general, also residual $\Lambda$
dependence (Eq.~\eqref{TRGtrunc}) which can be absorbed in the LECs of
higher-derivative interactions.
{Since shuffling short-range physics between loops and LECs does
not change observables, the finite part of {an} LEC is expected to be set
by the replacement $\Lambda\to \Mhi$ (see, for example,
\cite{Veltman:1980mj})\footnote{
{\textcite{Burgess:2013ara} offers a clear discussion in the specific 
context of the cosmological constant.}
}, which then places an upper bound on the order these interactions appear 
{at}.
The exception is when a symmetry suppresses the corresponding 
interaction~\cite{tHooft:1979rat}.
``Naturalness'' assumes that all terms in the effective
Lagrangian (respecting the relevant symmetries) have dimensionless 
coefficients
of $\OO(1)$ when the appropriate powers of $\Mlo$ and $\Mhi$ are factored out.
Renormalization is thus a powerful tool to estimate sizes of the 
LECs.}

This framework is a generalization of the ancient requirement of 
renormalizability by a finite set of parameters.  If 
{all interactions needed for Eq.~\eqref{TRGtrunc}
are present at each order,}
the resulting $S$ matrix incorporates the relations among QCD 
$S$-matrix elements demanded by symmetries, with no other assumption than an 
expansion in $Q/\Mhi<1$.  
Every low-energy observable depends on a finite 
number of LECs at leading order (LO), where $\mathcal{V}=0$, a few more at 
next-to-leading order (NLO), where $\mathcal{V}=1$, {\textit{etc}.}  Once 
the LECs are determined from a finite number of data, all other observables can 
be pre- or postdicted with a controlled error.  Traditionally the input data 
have been experimental, but LQCD results can now be used
instead~\cite{Barnea:2013uqa,Beane:2015yha,Kirscher:2015yda}.

One of the virtues of the model independence encoded in Eq.~\eqref{TRGtrunc}
is that it provides an {\it a priori} estimate of theoretical errors.  At the 
simplest level errors can be estimated from the higher-order terms in 
Eq.~\eqref{Ttrunc} with a guess for $\Mhi$.  A lower bound on the theoretical 
error is provided by cutoff variation from $\Mhi$ to much higher values.
The breakdown scale $\Mhi$ itself can be inferred comparing the energy 
dependence at various orders with data~\cite{Lepage:1997cs}.  Reliance on data 
can be minimized by using instead EFT results at different
cutoffs~\cite{Griesshammer:2015osb}.  Up to now both data fitting and
propagation of errors have employed standard statistical analyses previously 
used for models.  However, these methods can lead to biases because they are 
not particularly well suited to the \apriori EFT error estimates, which 
typically increase with $Q$, while experimental data are
{sometimes} more 
precise at higher $Q$.  A comprehensive theory of EFT error analysis based on 
Bayesian methods is currently being 
developed~\cite{Schindler:2008fh,Furnstahl:2014xsa,Furnstahl:2015rha,
Wesolowski:2015fqa}
with the promise of becoming the standard in the field.
