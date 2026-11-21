---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-027-49-on-the-theory-of-gkm
section_title: "On the theory of GKM"
section_number: 4.9
pages: 110-118
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.985
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We remind that GKM is abbreviation for the Generalized Kontsevich model,
This theory is the naturally broad collection of topics for a separate big
section in these notes. However, we decided not to include such detailed
presentation. This is because GKM theory seems too incomplete now. First, we
believe that the natural invariant formulation - of which existing matrix
integral is
only a specific realization - is still lacking. Second, GKM is not yet
generalized enough to fulfil its main purpose of incorporating infromation
about {\it all} the models of $2d$ gravity (in fact it should include even
more: the entire theory of integrable hierarchies and geometrical
quantization). Third, though the whole approach is very conceptual and deep,
many {\it proofs}, as available nowadays, are still very technical and long.
All this implies, that the proper view on the subject of GKM still needs to be
found. At the moment we could describe two complementary approaches: one,
starting from integral representations, another - from the Duistermaat-Heckman
(localization) theory and Fourier analysis on group manifolds. Though
intimately related, these two approaches are still technically different in
too many respects. The second one is more fundamental (since ordinary
integrals arise from discrete sums either in special limits or in the cases of
inifinite-dimensional algebras, and, more important, since integral
representation is only one of many possible ways to define the quantities of
interest). However, many of the most important results, obtained in the first
approach yet do not have their proper names and exact counterparts in the
second one. We believe that this whole issue will be very much clarified in
the near future and decided to postpone a detailed review till that time.
What we can not avoid in these notes, is giving at least a {\it list} of
topics,
already included in the theory of GKM, and this is the purpose of the present
subsection.

Kontsevich model with $V=\frac{X^3}{3}$ was derived by Maxim
Kontsevich \cite{Ko} from the original definition of topological $2d$ gravity,
given by E.Witten \cite{WitTG} in terms of generating functional for Chern
classes of certain bundles over Riemann surfaces. Generalization of this
reasoning (when more bundles are taken into consideration) leads to the theory
of Landau-Ginzburg Gravity (LGG), which is believed to be the same as GKM,
though not all the proofs are already avaliable.\footnote{
Intermidiate results include
the study of spherical approximation to LGG, which exhibits the structures,
peculiar for "quasiclassical integrable hierarchies" (of which Bateman
hierarchy to be briefly mentioned in section 5.2 below is an example), and
which also arise in "quasiclassical approximation" to GKM. For some results in
this direction see \cite{WittenN2},\cite{KriDu},\cite{TakTak},\cite{LP},
\cite{Krich},\cite{KhMa} and
references therein.
}

The crucial feature of non-perturbative partition functions, as we discussed at
the neginning of section 2, is their intrinsic integrability. For $2d$ gravity
this general idea acquires a very concrete formulation: partition functions
are usually just $\tau$-functions of conventional integrable hierarchies,
moreover - for LGG, associated with minimal models, these are just ordinary
multicomponent Toda hierarchies.\footnote{One can say that this is natural:
both such models and Toda hierarchies are associated with the level $k=1$
Kac-Moody algebras and corresponding simplified versions of the WZNW model.
However, too much still remains to be clarified about this "obvious"
connection.
}

M.Kontsevich found  representation for  generating
functional in the form of matrix integral, i.e. formulated a matrix model,
which later allowed to prove Witten's conjecture
that the functional is in fact a $\tau$-function.
The concept of GKM as a {\it universal} matrix model, including all the
information about generic (eigenvalue?) matrix models and thus all the models
of $2d(?)$ gravity was introduced in \cite{GKM}, and the analogue of
Kontsevich model with arbitrary potential $V(X)$, i.e. expression
\be
\new
\begin{array}{c}
\left.Z_V\{T\}\right|_{T_k = \frac{1}{k}{\rm tr}\Lambda^{-k}} =
C_V(\Lambda)^{-1}{\cal F}_V\left(V'(\Lambda)\right) \sim \\
\sim \frac{\sqrt{{\rm det} V''(\Lambda)}}
{(2\pi)^{n^2/2} e^{{\rm tr}\left(\Lambda V'(\Lambda) - V(\Lambda)\right)}}
\int_{n\times n} dX e^{- {\rm tr} V(X) + {\rm
tr} V'(\Lambda) X}
\end{array}
\label{GKoM}
\ee
was proposed as an intemediate step in this direction.\footnote{
We remind that ${\rm det} V''(\Lambda)$ is defined somewhat tricky, see s.2.5
above. The same matrix integral (\ref{GKoM}) was also considered
in refs.\cite{MaSe},\cite{Direv},\cite{Ko2},\cite{AvM}.
}
This (still restricted) version of GKM is already enough to unify all the $(p,
1)$-models of $2d$ gravity. In some sense, $(p,q)$-models with $q\neq 1$ are
also included, but in a very non-transparent way (using analytical
continuation), which does not even explicitly respect the $p \leftrightarrow
q$ symmetry. Partition function of such GKM, $Z_V\{T\}$ depends on two types
of variables: time-variables $\hat T_k$ and potential $V$. Formally these two
types of variables are absolutely different, $V$ being responsible for the
choice of particular LGG model or, what is essentially the same, of particular
reduction of Toda-lattice or KP hierarchy; while $\hat T_k$ are parameters of
the generating functional of all correlation functions in this particular
model. But of course, since we deal with exact (non-perturbative) approach,
there is almost no real difference between these types of
dependencies - on the model (vacuum state) and on the $\hat T$'s: the model
can be changed by non-infinitesimal shift of $\hat T$-variables.
Technically, in GKM this is reflected in the identity of the form
\cite{Krich}:
\be
{\cal Z}_{V_p}\{T\} = f_p(r\mid \hat T_k + r_k)\cdot
\tau\{\hat T_k + r_k\mid G_p\}
\label{Krich'}
\ee
where $r_k = \frac{p}{k(p-k)}{\rm
Res}\left(V'(\mu)\right)^{1-\frac{k}{p}}d\mu$
provide a specific parametrization of potentials $V$, which is here assumed to
be any polinomial of degree $p$, and $f_p$ is some simple function:
\be
f_p(r\mid \hat T_k + r_k) = \exp -\frac{1}{2} \sum_{i,j} A_{ij}(r)
(\hat T_i + r_i)(\hat T_j + r_j); \nn \\
A_{ij} = {\rm Res}\left(V'(\mu)\right)^{i/p}d\left(V'(\mu)\right)^{j/p} =
\frac{\partial^2\log \tau_0^{(p)}}{\partial t_i\partial t_j},
\ee
and $\tau_0^{(p)}$ is a $\tau$-function of "quasiclassical hierarchy".
What
is important, $G_p$ (which define the shape of the $\tau$-function
as function of $\hat T + r$) and  $f_p$  depend only on the degree $p$,
but not on the other details of the shape of the potential. This is a deep
formula. It accounts for two phenomena at once: First, it says that $Z$
depends on the {\it sum} of $\hat T$ and $r$.\footnote{
In Miwa parametrization
$\hat T_k = \frac{1}{k}{\rm tr}\left(V'_p(\Lambda)\right)^{-k/p}$. Throughout
these notes we used different time-variables $T_k =
\frac{1}{k}{\rm tr}\Lambda^{-k}$, which are independent of the potential $V$,
instead $V$-dependence of $Z_V$ - which we did not really study -
was rather nontrivial. If expressed in terms of $\hat T$, partition function
$\hat Z_V\{\hat T+r\} = Z_V\{T\}$ becomes almost independent of $V$: it changes
- abruptly - {\it only} when the degree $p$ of potential changes. This second
type of description is of course in better accordance with the symmetries of
particular model - which are different in different "vacua" (for different
$p$). Therefore these are  variables $\hat T + r$, rather than in
$T$ which arise naturally in Ward identites - as we saw in sections 2.5 and
2.6. $T$'s and $\hat T$'s are suited for different purposes: $T$'s are nice
when {\it universality} aspects of GKM are concerned, while $\hat T$'s arise
when specific features of particular models (orbits, vacua) are considered.
}
Second, dependence on $V$ is not {\it quite} smooth: when the degree of
potential changes, the shapes of the functions $f$ and $\tau$ also changes
abruptly. Another side of the same phenomenon is that partition function
$Z_V\{T\}$, which in principle is well defined as a matrix integral for all
choices of $V$ and $L$ (thus $\hat T$) at once, is in fact singular at some
points: there are phase transitions, manifesting the switch from one LGG model
to another. After a phase transition original integral expression becomes
sonewhat symbolical: it defines partition function only in the sense of
analytical continuation, and it is a separate problem to find an integral
representation, adequate in the new phases. In practice, what is nicely
decribed by the integral representation GKM in the form of eq.(\ref{GKoM}),
are $(p,1)$-models, with $p+1$ being just the power of potential $V(x)$. What
is not yet found, is analogous representation for $(p,q)$-models with $q\neq
1$ (it can involve multiple matrix integrals, and universal model is supposed
to be "matrix quantum mechanics in external fields").

Derivation of the crucial formula (\ref{Krich'})in any approach - starting from
GKM in the form of either LGG or matrix integrals - is still very tedious. In
matrix-model representation it relies upon identity \cite{Krich}
\be
\new
\begin{array}{c}
\frac{\partial Z_V}{\partial T_k} =
\langle {\rm tr}\Lambda^k - {\rm tr} X^k \rangle \equiv  \\
\equiv {\cal C}_V^{-1} \int \left({\rm tr}\Lambda^k - {\rm tr} X^k\right)
e^{-{\rm tr}V_p(X) +  {\rm tr}V_p'(\Lambda)X} dX \ \ \ {\rm for}\  1\leq k\leq
p,
\end{array}
\label{tkderiv}
\ee
which look trivial but are rather hard to derive. (A proof of the string
equation in GKM at the end of the previous subsection is the simplest example
of this kind of exersices.)
Certainly some simple derivation "in two lines" should exist, but it is not yet
found. Formulas of this kind are very important for all aspects of GKM theory.
Besides other things, they are just necessary to actually evaluate correlation
functions in $(p,1)$-models of $2d$ gravity, of which $Z_V\{T\}$ is a
generating functional. If instead of these "physical" questions, one asks
about integrability theory, identites of this sort also play important role.
For example, looking at (\ref{tkderiv}) for a special $k=p$ and special choice
of potential - monomial $V_p(X) = \frac{X^{p+1}}{p+1}$,- ane can note that the
r.h.s. vanishes: this is just a Ward identity, reflecting invariance under the
shift of the integration variable, $\delta X =\ const$.
This is a simplest version of a more general statement:\footnote{
This property was technically implicit in original Kontsevich's work \cite{Ko}
for $p+1=3$, where it was related with certain combinatorial identities. A
tricky proof, relying upon properties of $\tau$-functions, was given for any
$p$ in \cite{GKM}. An example of straightforward proof, again  for $p+1=3$, -
just in terms of Kontsevich matrix integrals - can be found in
ref.\cite{DFIZ}.
}
\be
{\rm if}\ V_p(X) = \frac{X^{p+1}}{p+1}, \ \ \ {\rm then} \ \ \ \
\frac{\partial Z_V}{\partial T_{pk}} = 0 \ \ {\rm for\ all\ } n\in Z_+.
\label{redcondk}
\ee
Looking from the point of view of integrable hierarchies, one immediately
recognizes (\ref{redcondk}) as an example of reduction condition
(\ref{redtotau1}). It corresponds to the so called $p$-reduction of
KP-hierarhy, of which KdV ($p=2$) and Boussinesq ($p=3$) are the most
celebrated examples. We refer to \cite{GKM} and \cite{Krich} for all details
and references, the only thing to mention here is that the slightly weaker
verison of the constraint (\ref{redcondk}),
\be
\frac{\partial Z_V}{\partial T_{pn}} = a_n = {\rm const},
\label{redcondk'}
\ee
where $a_n$ do not depend on any time variables, can be simply expressed in
Miwa parametrization: it is just the statement that $\varphi$-functions in
\be
Z_V = \frac{{\rm
det}_{\gamma\delta}\varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)}
\nn
\ee
satisfy the $p$-reduction condition:
\be
\lambda^p \varphi_\gamma(\lambda) =
\sum_{\delta = 1}^{\gamma+p}
\hat{\cal V}_{\gamma\delta}\varphi_\delta(\lambda).
\label{predcogra}
\ee
This a restrictive relation, because $\varphi$'s are infinite seria in
$1/\lambda$, while at th r.h.s. in (\ref{predcogra}) there is only a finite
number of items. In GKM it is satisfied for monomial potential


just as a corollary of Gross-Newman
equation, or  more exact, of the Ward identity for the integral
\be
\varphi_\gamma(\lambda) \sim \int x^{\gamma-1} e^{-V(x)+V'(\lambda)x} dx.
\nn
\ee
Indeed, integral does not change under the shift $\delta x = \ const$, and
this implies:
\be
\int x^{\gamma-1} \left( V'(x) - V'(\lambda) - \frac{\gamma -1}{x}\right)
e^{-V(x)+V'(\lambda)x} dx = 0,
\nn
\ee
i.e.
\be
\sum_{k=1}^{p+1} kv_k \left(\varphi_{\gamma +k-1}(\lambda) -
\lambda^{k-1}\varphi_\gamma(\lambda)\right) - (\gamma-1)\varphi_{\gamma -1} =
0.
\label{calvdef}
\ee
If only $v_{p+1}\neq 0$, this leads to an identity of the required form of
(\ref{predcogra}). This description of reduction can be modified to allow for
non-monomial potentials, making use of the concept of "equivalent
hierarchies", see \cite{Tak},\cite{Krich}: in this framework the reduction
condition is
\be
V'(\lambda)\varphi_\gamma(\lambda) = \sum_\delta
{\cal V}_{\gamma\delta}\varphi_\delta,(\lambda),
\label{redcond'}
\ee
but classes of essentially different
reductions are labeled by the degree of potential only.

As we already discussed in the previous subsection, linear constraints like
(\ref{predcogra}) are not restrictive enough to fix the shape of the
$\tau$-function (the point $G$ in the universal module space) unambigously:
string equation should be also imposed. If expressed in terms of
$\varphi$'s, string equation is just the property
(\ref{gkmKasch}):
\be
\varphi_{\gamma +1} = {\cal A}\varphi_\gamma,
\label{recondigkm}
\ee
where the Kac-Schwarz operator
\be
{\cal A} = \frac{1}{V''(\lambda)}\frac{\partial}{\partial \lambda} -
\frac{1}{2}\frac{V'''(\lambda)}{(V''(\lambda))^2} + \lambda.
\ee
It has obvious generalization of the form
\be
{\cal A}_{p,q} = \frac{\partial}{\partial V'_p( \lambda)}
- \frac{1}{2}\frac{V'''_p(\lambda)}{(V''_p(\lambda))^2} + Q'_q(\lambda),
\label{KaschopQ}
\ee
where $Q_q(\lambda)$ is a polinomial of degree $q+1$ and (\ref{recondigkm}) is
substituted be
\be
\varphi_{\gamma +q} = {\cal A}_{p,q}\varphi_\gamma.
\ee
This generalization is
naturally related to the string equation in $(p.q)$ models, see \cite{KhMa}
and references therein.
Generic $(p,q)$ LGG model can be described by a system of constraints,
\be
(\lambda^p - {\cal V}_p)\{\varphi\} = 0,  \nn \\
{\cal A}_{p,q}\{\varphi\} = 0,
\label{constrset}
\ee
where both operators ${\cal V}_p$ and ${\cal A}_{p,q}$
are not uniquely fixed by
choosing $p$ and $q$, and there is also a freedom to change variables $\lambda
\rightarrow f(\lambda)$ and make a triangular transformation of basis
$\varphi_\gamma \rightarrow \varphi_\gamma + \sum_{\delta
<\gamma}C_{\gamma\delta}\varphi_\delta$. Altogether the set of equations
(\ref{constrset}) modulo these allowed transformations is finite -
$(p-1)(q-1)$ - dimensional, this is dimension of the module space of LGG
models with given $p$ and $q$. Kontsevich integral can be now used to
establish duality transformation from $(p,q)$ to $(q,p)$ model \cite{KhMa}:
\be
Z_{V,Q}(\Lambda) =
C_{V,Q}^{-1}(\Lambda) \int_{n\times n} dX
e^{-{\rm tr}S_{V,Q}(X,\Lambda) + {\rm
tr}V'(\Lambda)Q'(X)} Z_{Q,V}(X).
\label{VQGKM}
\ee
Here
\be
S_{V,Q}(x,\lambda) = \int^x V'(y)Q''(y)dy = \int^x V'(y)dQ'(y),
\ee
As usual, $C_{V,Q}(\Lambda)$ is  the quasiclassical approximation
to the integral, and
$Z_{V,Q}(\Lambda) \equiv \frac{{\rm det}_{\gamma\delta}
\varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)}$, where $\varphi$ are
solutions to (\ref{constrset}) with ${\cal V}_p$ and ${\cal A}_{p,q}$
defined by eqs.(\ref{redcond'}) and (\ref{KaschopQ}) respectively.\footnote{
Also expression for  $r_k$-variables is now modified:
\be
r_k = \frac{p}{k(p-k)}{\rm Res} (V'_p(\mu))^{1-k/p}dQ'_p(\mu),
\nn
\ee
For monomial $V_p$ and $Q_q$  $\ r_k = -\frac{p}{p+q}\delta_{k,p+q}$.
}
This relation does {\it not} provide any
formula for $Z_{V_p,Q_q}(\Lambda)$ unless $q=1$. The case of $q=1$ is
distinguished because $Z_{Q_1,V_p}$ is trivial. Indeed, the 1-reduction
constraint $\lambda\varphi_\gamma = \varphi_{\gamma+1} + \sum_{\delta
\leq\gamma}{\cal V}_{\gamma\delta} \varphi_\delta$, implies that
${\rm det}_{\gamma\delta}\varphi_\gamma(\lambda_\delta) =
\Delta(\lambda)\prod_\delta \varphi_1(\lambda_\delta)$,
thus $Z_{Q_1,V_p} = \exp \sum_k a_kT_k$, what is essentially the same as
$Z_{Q_1,V_p} = 1$,\footnote{
Since $\varphi_1(\lambda) = 1 +\sum_{k>0}b_k\lambda^{-k}$, $\ \log
\varphi_1(\lambda) = \sum_{k>0}\frac{a_k}{k}\lambda^{-k}$, and the sum
$\sum_\delta \log\varphi_1(\lambda_\delta) =
\sum_{k>0}\frac{a_k}{k}\left(\sum_\delta \lambda_\delta^{-k}\right) =
\sum_{k>0} a_kT_k$. Addition of any {\it linear} combination of
time-variables to $\log\tau$ does not essentially change $\tau$-function.
For example,  the ordinary integrable equations
(like KdV or KP) are usually written in terms of variables like $u =
\frac{\partial^2}{\partial T_1}\log\tau$, which are {\it second} derivatives
of $\log\tau$.
}
and (\ref{VQGKM}) is just our old
formula (\ref{GKoM}) for the $(p,1)$ version of GKM.
(In fact $Q_1(X) \sim X^2$, and $Z_{Q_1,V_p}$ is
nothing but Gaussian Kontsevich model. It is trivial when the "zero-time"
$N=0$, as we assume here.) Matrix model realization of $Z_{V_p,Q_q}$ for
$q\neq 1$ is yet unknown.

This is not the only important further generalization of GKM (\ref{GKoM}).
Another one is implied by the formula
for ${\cal F}_V$ in terms of eigenvalues from the section 3.3,
\be
{\cal F}_V \sim \prod_{\gamma = 1}^n \int dx_\gamma e^{-V(x_\gamma)}
\Delta^2(x) I(x,l).
\label{KIverIZ}
\ee
As it was already mentioned in section 3.3, the Itzykson-Zuber integral
\be
I(x,l) \sim  \int [DU] e^{{\rm tr} UXU^\dagger L} \sim
\frac{{\rm det}_{\gamma\delta} e^{x_\gamma l\delta}}
{\Delta(x)\Delta(l)}
\ee
is in fact a coadjoint orbit integral and has group theoretical
interpretation: under certian conditions it turns into a character $\chi_R(g)
= {\rm Tr}_R g$ of the group $GL(n)$. Here $g \equiv e^L$ is considered as a
group element, representation $R$ is labeled by integer-valued parameters
$m_1,\ldots,m_n$ - essentially the lengths of rows in the Young diagramm.
Exact statement is:
\be
I(m,l)\cdot\frac{\Delta(l)}{\Delta(g)} = \frac{{\rm det}_{\gamma\delta}
g_\gamma^{m_\delta}}{\Delta(m)\Delta(g)} = \frac{\chi_R(g)}{d_R},
\ee
i.e. in order to get a character we should integrate over matrices $X$
with integer-valued eigenvalues.\footnote{
The ratio
\be
\frac{\Delta(l)}{\Delta(g)} = \prod_{\gamma >\delta} \frac{l_\gamma -
l_\delta}{e^{l_\gamma} - e^{l_\delta}}
\nn
\ee
is the usual correction factor, which is the price for the possibility to
reduce quantum-mechanical problem of motion on the orbit to a
{\it single} matrix integral. The full problem of
matrix quantum mechanics can and should be considered as a
multi-matrix (in fact, infinite-matrix) generalization of GKM (\ref{GKoM}),
which incorporates all the $(p,q)$ LGG models.
}
Dimension $d_R$ of representation can be also expressed in terms of
$m$-variables: $d_R = \Delta(m)$. As to the traces
${\rm tr} X^k = \sum_\gamma
x_\gamma^k \rightarrow \sum_\gamma m_\gamma^k$, which appear in the action of
GKM, they are very similar to the
$k$-th Casimir eigenvalue $C_k(R)$ (though is not exactly the same). Thus we
see that the integral in (\ref{KIverIZ})
is in fact very similar to
\be
{\cal F}_V^{qu}\{g,\bar g\} \equiv \sum_R \chi_R(\bar g)\chi_R(g)
e^{-\sum_{k=0}^{\infty}v_kC_k(R)},
\label{quanGKM}
\ee
evaluated at the point $\bar g = I$.
The only real difference is that instead of the integral we have a sum over
discrete values of $m$ (sum over all the representations, or a {\it model} of
$GL(n)$). This "discretized" (quantum?) GKM
is more general that the continuum one
which can be obtained by various limiting procedures. It is now obvious that
the theory of discretized GKM largely overlaps with that of $2d$ Yang-Mills
theory. The simplest ingredient of this theory is the classical result
\cite{chartau}, that
$GL(N)$ characters are in fact (singular) Toda-lattice and KP
$\tau$-functions. Moreover, the entire sum at the r.h.s. of (\ref{quanGKM}),
if considered as a function of $T_k = \frac{1}{k}{\rm tr} g^k$,
${\bar T}_k = \frac{1}{k}{\rm tr} \bar g^k$ is
in fact a Toda-lattice $\tau$-function. There are also features parallel to
(\ref{Krich'}).
We refer to \cite{ITEP12}
for a little more details about discretized GKM (see also
a recent paper \cite{GoNe}). This is one more very important direction of the
further investigation of GKM.
