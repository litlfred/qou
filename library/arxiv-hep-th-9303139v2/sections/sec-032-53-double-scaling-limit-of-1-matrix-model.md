---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-032-53-double-scaling-limit-of-1-matrix-model
section_title: "Double-scaling limit of 1-matrix model"
section_number: 5.3
pages: 126-134
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.989
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Now we proceed to discussion of a slightly different approach to continuum
limits, which is directly adjusted to the needs of matrix models. The naive
idea \cite{mamo},\cite{FKN}
is to forget about integrability and just look at the Ward
identities (Virasoro constraints in the 1-matrix case) and take a continuum
limit of these identities. This approach makes close contact with the standard
technique of "loop equations" (Makeenko-Migdal equations \cite{MaMi})
in the theory of
matrix models, of which Virasoro and $W$-constraints are just particular
examples.\footnote{One of the puzzles in the theory of non-eigenvalue
models is to identify group-theoretical meaning of generic loop equations:
they are usually introduced as equations of motion rather than as Ward
identities (see discussion at the beginning of Section 2 above), and thus
their implications are more obscure and technical means to deal with them are
much more restricted. When group theory description will be found, it will
very soon reveal the (generalized) integrable structure of non-eigenvalue
models and it will be a big step forward in the whole theory.
}

However, carefull analysis of continuum limit of discrete Virasoro constraints
\cite{MMMM} makes it clear that the procedure is far less simple than one can
think in advance (usually derivations are not very carefull and details are
just "put under the carpet"). The crucial problem is that we want peculiar
(double scaling) rather than naive limit, and, as we mentioned in the previous
subsection, this also requires a certain reduction (elimination of the
odd-times $t_{2m+1}$).  If parity symmetry
(w.r.to the change of $H \rightarrow -H$ in the original matrix integral) is
taken into account, one
can easily throw away {\it first} derivatives w.r.to the odd-times $t_{2m+1}$,
just because
$\displaystyle{\left.\frac{\partial Z_N}{\partial t_{2m+1}}\right| _{t_{2k+1}
= 0} = 0}$, but this is no longer true as far as the {\it second} derivatives
$\displaystyle{\left.\frac{\partial^2 Z_N}{\partial t_{2m+1}\partial t_{2l-1}}
\right| _{t_{2k+1} = 0}}$ are concerned,
which appear in (the "quantum piece" of) the
Virasoro constraints (1.2). It is a highly non-trivial feature of loop
equations (having its origin in their integrable structure!), that in
continuum limit these terms can be in fact carefully eliminated.
The thing is that the second derivatives of $\log Z_N$ appear to be a {\it
local} objects, in the sense that they depend only on $Z_{\tilde N}$ with the
difference $\mid \tilde N-N\mid \leq m+l$, which does {\it not} blow up as $N
\rightarrow \infty$ in continuum limit. Moreover, the differences
$\displaystyle{\frac{\partial^2 \log Z_N}{\partial t_{2m+1}\partial t_{2l-1}} -
\frac{\partial^2 \log Z_N}{\partial t_{2m}\partial t_{2l}}}$ almost tend to
zero, leaving some simple (though vitaly important) correction to arising
continuous loop equations. This locality property allows one to
get rid of these dangerous odd-time derivatives,
substituting them just by second derivatives
w.r.to the even-times. Since such substitution is possible
only  for {\it logarithms} of $Z_N$, continuous constraints appear imposed on
the {\it square root} of original partition function (or on the
$\frac{1}{p}$-th power in the case of the $p-1$-component conformal models).
Another aspect of this trick to deal with the odd-time derivatives is that it
makes the entire derivation depending on the
fact that the theory is integrable - this is what guarantees the
above-mentioned
locality.  Since the way to reveal integrability,
by looking at the loop equations themselves is yet not very well
understood, the whole calculation becomes not quite self-contained (but of
course, if we know everything about integrable structure this is not a real
drawback, this is just a limitation of particular approach, starting from the
loop equations) . In particular, this is the only
loophole, which is still not filled in the description of continuum limit of
conformal (multi-component) matrix models, which in all other respects goes in
exactly in parallel with the 1-component (1-matrix) case.\footnote{
It transforms discrete $W$-constraints into continuum $W$-constraints, which
in their turn arise from the GKM with the appropriate potential \cite{GKM},
\cite{Mikh}. Unfortunately, since the GKM-inteprpretation of {\it discrete}
multicomponent models (like the one existing in the 1-matrix case, see s.3.8)
is yet unknown, the direct way to take their continuum limit - like the one
to be described in the next subsection for the 1-matrix case - is also yet
unavailable. For more details about conformal matrix models, their integrable
structure and continuum limits see refs.\cite{comamo}.
}

We shall now describe briefly the steps of this calculation for the 1-matrix
model, refering for all the details to refs.\cite{MMMM} and \cite{GMMMMO}.
Our previous discussion already contain motivations for the main steps, so we
do not need to go into detailed explanations. Manipulations below, involving
Kazakov variables can look a little artificial, but we repeat that they can be
interpreted as a switch from the Toda-type to KP-type hierarchies, which, as
we already saw in the previous subsection, is naturally associated with the
double-scaling continuum limit.

We start from the discrete Virasoro constraints (1.2), rewritten in terms of a
generating functional ("stress tensor" on the spectral plane):
\be
L_-(z) Z_N = 0,
\ee
where
\be L_-(z) = \sum_{n\geq -1}^{\infty} L_n z^{-n-2} = \frac{1}{2}\left(
J^2(z)\right)_-,
\ee
and
\be
\new
\begin{array}{c}
J(z) = \partial \phi(z) = \sum_{n= -\infty}^{\infty}J_n z^{-n-1}; \\
\phi(z) = \frac{1}{\sqrt{2}}\sum_{k\geq 0}t_kz^k -
\sqrt{2} \sum_{k>0} \frac{z^{-k}}{k}\frac{\partial }{\partial t_k};  \\
J_{-k} = \sqrt{2}\frac{\partial }{\partial t_k}; \ \ J_k =
\frac{1}{\sqrt{2}}kt_k, \ \ k\geq 0;  \\
\frac{\partial}{\partial t_0}Z_N = NZ_N.
\end{array}
\ee

Next, we need to reduce the original partition function:
\be
Z_N\{t\} \longrightarrow Z_N^{\rm red}\{t_{\rm even}\} \equiv
Z_N\{t_{\rm odd}=0, t_{\rm even}\}.
\ee
All odd virasoro generators $L_{2n+1}$
act trivially on $Z_N^{\rm red}$, since
$\displaystyle{\left.\frac{\partial Z_N}{\partial t_{2k+1}}\right|
_{t_{\rm odd}=0} = 0}$, and we need to consider only $L_{2n}$.
Introduce also\footnote{
Note that $\displaystyle{
\left.\phi^{\rm red}(z) \neq \phi(z) \right|_{t_{\rm odd}=0}}$ and similarly
$\displaystyle{
\left.L_{2n}^{\rm red}(z) \neq L_{2n} \right|_{t_{\rm odd}=0}}$: some factors
of $2$ in (\ref{redfields}) being responsible for this discreapancy. In fact
$L^{\rm red}$ are related to generators of the Virasoro constraints in the
{\it complex}-matrix model \cite{MMMM},
\be
Z_N^C = \int dM \exp \left(\sum_{k\geq 0}t_{2k} {\rm Tr} (MM^\dagger)^k\right)
\nn
\ee
and in continuum limit $\displaystyle{Z_N^C \sim \sqrt{Z_{2N}^{\rm red}}}$.
}
\be
\phi^{\rm red}(z) &\equiv \frac{1}{\sqrt{2}}\sum_{k\geq 0} t_{2k}z^{2k} -
\sqrt{2}\sum_{k>0} \frac{z^{-2k}}{k}\frac{\partial}{\partial
t_{2k}}; \nn \\
L^{\rm red}(z) &= \frac{1}{2}\left(\partial \phi^{\rm red}(z)\right)^2; \nn \\
L_{2n}^{\rm red} &\equiv \sum_{k>0} kt_{2k}\frac{\partial}{\partial t_{2k+2n}}
+
\sum_{k=0}^n \frac{\partial^2}{\partial t_{2k}\partial t_{2n-2k}}.
\label{redfields}
\ee

Now we have two issues to be discussed separately. The first one is the change
from $t_{2k}$ to Kazakov variables $T_{2m+1}$. The second is the difference
between constraints imposed on $Z^{\rm red}$ and $Z$.

The simplest way to {\it describe} Kazakov variables is to introduce one more
- antiperiodic - scalar field,
\be
\Phi(u) = \frac{1}{\sqrt{2}} \sum_{k\geq 0} T_{2k+1} u^{k+\frac{1}{2}}
- \sqrt{2} \sum_{k\geq 0} \frac{u^{-k-\frac{1}{2}}}{k+\frac{1}{2}}
\frac{\partial}{\partial \tilde T_{2k+1}}.
\ee
Here $\tilde T$ and $T$ are related by transfromation
\be
T_{2k+1} = \tilde T_{2k+1} + \epsilon^2 \frac{k}{k+\frac{1}{2}}\tilde
T_{2k-1} + 2\epsilon N\delta_{k,0}.
\ee
Impose now a relation:
\be
\partial\phi^{\rm red}(z) &= \frac{1}{\epsilon^2}U^{-1}
\partial\Phi(u) U; \nn \\
z^2 &= 1 + \epsilon^2 u,
\label{preKaz}
\ee
and in continuum limit $\epsilon$ is assumed to vanish.
This is a relation which maps homogeneous representations into principal, but
its invariant meaning (especially - from the point of view of conformal field
theory) does not seem to be enough understood. Anyhow, this relations
establishes a relation between $t_{\rm even}$ and $T$. Namely, comparing
the coefficients in front of the positive powers of $u$
at both sides of this equation, we get:
\be
T_{2k+1} &= \frac{1}{2}\epsilon^{2k+1}
\sum_{m\geq k}^{\infty} \frac{g_m
\Gamma(m+\frac{1}{2})}{(m-k)!\Gamma(k+\frac{3}{2})}, \ \ k\geq 0; \nn \\
g_m &= mt_{2m},\ \ m\geq 1; \ \ \ \ g_0 = 2N.
\label{Kazchava}
\ee
Inverse transformation looks like
\be
g_m = 2\sum_{k\geq m} (-)^{k-m}
\frac{T_{2k+1}\Gamma(k+\frac{3}{2})}
{\epsilon^{2k+1}(k-m)!\Gamma(m+\frac{1}{2})} .
\ee
Now,
\be
\frac{\partial}{\partial t_{2k}} =
\frac{1}{2}\sum_{m=0}^{k-1} \frac{\Gamma(k+\frac{1}{2})\epsilon^{2k+1}}
{(k-m-1)!\Gamma(m+\frac{3}{2})}\frac{\partial}{\partial\tilde T_{2m+1}},
\ee
and using this formula when comparing the negative powers of $u$ we find:
\be
U &= \exp\left(\sum_{m,n} A_{mn}\tilde T_{2m+1}\tilde T_{2n+1}\right), \nn \\
A_{mn} &= 2\frac{(-)^{m+n}}{\epsilon^{2(m+n+1)}}\cdot
\frac{\Gamma(m+\frac{3}{2})\Gamma(n+\frac{3}{2})}
{m!n!(m+n+1)(m+n+2)}.
\label{Umatrix}
\ee
The square of relation (\ref{preKaz}) is:
\be
\left(\partial\phi^{\rm red}\right)^2(z) = \frac{1}{\epsilon^4}U^{-1}
\left(\partial\Phi\right)^2(u) U,
\label{preKazVir}
\ee
or
\be
\sum_{p\geq 0}L_{2p}^{\rm red} z^{-2p-2} =
\frac{1}{\epsilon^4}U^{-1}
\left(\sum_{n\geq -1} \tilde{\cal L}_{2n} u^{-n-2}\right) U.
\ee
This equality implies that
\be
\new
\begin{array}{c}
U^{-1}\tilde{\cal L}_{2n} U = \epsilon^4 \sum_{p\geq 0}L_{2p}^{\rm red}
\oint_{\infty}\frac{u^{n+1}du}{z^{2p+2}} =  \\ =
\epsilon^{-2n} \sum_{p=0}^{n+1} (-)^{n+1-p} C^p_{n+1} L_{2p}^{\rm red},
\end{array}
\ee
since
\be
\new
\begin{array}{c}
\epsilon^4\oint_{\infty}\frac{u^{n+1}du}{z^{2p+2}} =
\oint_{\infty}\frac{u^{n+1}du}{(1+\epsilon^2 u)^{p+1}}
=  \frac{1}{\epsilon^{2n}}\frac{\Gamma(-p)}{(n+1-p)!\Gamma(-n-1)} = \nn \\ =
\frac{(-)^{n+p+1}}{\epsilon^{2n}}\frac{(n+1)!}{p!(n+1-p)!}
= \frac{(-)^{n+1-p}}{\epsilon^{2n}}C_{n+1}^p.
\end{array}
\ee
Explicit expressions for the generators $\tilde{\cal L}_{2n}$ (which are
harmonics
of the stress tensor
$\frac{1}{2}\left(\partial\Phi\right)^2(u)$ of antiperiodic field $\Phi(u)$),
are:
\be
\new
\begin{array}{c}
\tilde{\cal L}_{-2} = \sum_{k\geq 1} (k+\frac{1}{2}) T_{2k+1}
\frac{\partial}{\partial \tilde T_{2(k-1)+1}} + \frac{T_1^2}{4};  \\
\tilde{\cal L}_{0} = \sum_{k\geq 0} (k+\frac{1}{2}) T_{2k+1}
\frac{\partial}{\partial \tilde T_{2k+1}};  \\
\tilde{\cal L}_{2n} = \sum_{k\geq 0} (k+\frac{1}{2}) T_{2k+1}
\frac{\partial}{\partial \tilde T_{2(k+n)+1}} +  \\
+ \frac{1}{4}\sum_{k=0}^{n-1}
\frac{\partial^2}{\partial \tilde T_{2k+1}\partial \tilde T_{2(n-k-1)+1}} -
\frac{(-)^n}{16\epsilon^{2n}}; \ \ n>0.
\end{array}
\label{vircotil}
\ee
So far everything what was done was just change of variables and all relations
were exact for any $\epsilon$, no limits were taken.

Operators (\ref{vircotil}) are very similar to ${\cal L}_{2n}$, arising in the
"continuous Virasoro constraints" (1.3), imposed on partition function of
$X^3$-Kontsevich model. There are, however, two discreapancies.

First, $\frac{\partial}{\partial \tilde T}$ appear in (\ref{vircotil}) instead
of $\frac{\partial}{\partial T}$ in generators in (1.3). One can argue that
this difference is not really essential, since $\tilde T_{2k+1}$ and
$T_{2k+1}$ differ by terms, which are proportional to $\epsilon^2$ and thus
vanish in the continuum limit $\epsilon \rightarrow 0$.
(Note, however, that this reasoning can be applied only for every particular
constraint $\tilde{\cal L}_{2n}Z = 0$, $n \geq -1$,
not to the entire generating functional,
where different terms are summed, multiplied by different powers of
$\epsilon$.)

The second discreapancy is a litlle more serious: it is the occurence of an
extra term $\displaystyle{\frac{(-)^{n+1}}{16\epsilon^{2n}}}$ for all $n\geq
0$ (this difference is present for $n=0$ as well, because ${\cal L}_0$
contains the item $\frac{1}{16}$, which is lacking in (\ref{vircotil}).)
This extra term can not be eliminated by just taking continuum limit:
moreover, it blows up instead of vanishing when $\epsilon \rightarrow 0$.
Remarkably enough, this term disappears when we turn to consideration of
actual Virasoro constraints, not just a formal choice of time variables. It
cancels completely with the other potential source of problem for the
derivation of continuous Ward identites. We proceed now to this most
sophisticated matter in this whole subsection.

The thing is that, as we already mentioned before, the reduction of discrete
Virasoro constraint $L_{2n}Z_N = 0$ contains some non-vanishing terms with the
odd-time  derivatives:
\be
\new
\begin{array}{c}
\left(\sum_{k>0} 2kt_{2k} \frac{\partial}{\partial t_{2k+2n}} + 2
\sum_{k=0}^{n} \frac{\partial^2}{\partial t_{2k}\partial t_{2n-2k}}\right)
Z_N^{\rm red} =                                    \\ =
\left(\sum_{k=0}^{n} \frac{\partial^2}{\partial t_{2k}\partial t_{2n-2k}}
- \sum_{k=0}^{n-1} \frac{\partial^2}
{\partial t_{2k+1}\partial t_{2n-2k-1}}\right)  Z_N^{\rm red}.
\end{array}
\label{colivirder0}
\ee
We added an extra term with the second even-time derivatives to both sides of
the identity, in order to get at the r.h.s. a combination, which has a chance
to vanish in continuum limit. (This formula still needs to be corrected, see
eq.(\ref{colivirder3}) below.)

In order to find rigorous reason for elimination of the terms at the r.h.s we
need to address to explicit formulas from the last subsection of section 4
(no simpler way is known so far). The crucial formula  which we need is:
\be
\frac{\partial^2\phi_n}
{\partial t_k\partial t_l} = \frac{\partial}{\partial t_k}
\frac{\langle n \mid h^l \mid n \rangle}{\langle n \mid n \rangle}
= \left( \sum_{m>n} - \sum_{m<n}\right)
\frac{\langle n \mid h^k \mid m \rangle \langle m \mid h^l \mid n \rangle}
{\langle m \mid m \rangle\langle n \mid n \rangle},
\label{colivirder1}
\ee
and the most important feature of it is its $R$-matrix structure (the
fact that a {\it difference} occurs at the r.h.s.). This structure implies
almost complete cancellation of terms, when we sum over $n$ in order to get
$\log Z_N = \sum_{0}^{N-1} \phi_n$, leaving only a finite sum of the length
{\it independent} of N:
\be
\frac{\partial^2\log Z_N}
{\partial t_k\partial t_l} =
\sum_{0 < j < {\rm min}(k,l)} \left( \sum_{n = N-j}^{N-1}
\frac{\langle n \mid h^k \mid n+j\rangle \langle n+j \mid h^l \mid n \rangle}
{\langle n \mid n \rangle\langle n+j \mid n+j \rangle}\right).
\ee
The finite sum at the r.h.s. can be expressed in terms of $R_n =
e^{\phi_n-\phi_{n-1}}$, which are exactly the quantites to satisfy equations
of Volterra hierarchy and tending to {\it constant} (denoted by  $R_0$ in the
previous section) in continuum limit. Locality property - the finiteness of
the sum at the r.h.s in (\ref{colivirder1}) - implies that this r.h.s. tend to
a constant value as $N \rightarrow \infty$. This constant does not completely
cancels in the difference
\be
\left(\sum_{k=0}^{n} \frac{\partial^2}{\partial t_{2k}\partial t_{2n-2k}}
- \sum_{k=0}^{n-1} \frac{\partial^2}
{\partial t_{2k+1}\partial t_{2n-2k-1}}\right)  \log Z_N^{\rm red},
\label{colivirder2}
\ee
and the remaining contributions appears to be exactly what necessary to cancel
the dangerous term
$\displaystyle{\frac{(-)^{n+1}}{16\epsilon^{2n}}}$
which appeared in the difference between $\tilde{\cal L}_n$ and ${\cal L}_n$.
We refer to ref.\cite{MMMM} for more details about these cancellations, and
the only thing to discuss at the rest of this subsection is the difference
between the r.h.s. of (\ref{colivirder0}) and (\ref{colivirder2}).
In the second expression the second derivatives are taken of $\log Z$, while
they are of $z$ itself in the first one. Of course,
\be
\frac{\partial^2 \log Z_N^{\rm red}}
{\partial t_{2k+1}\partial t_{2n-2k-1}}
=   \frac{1}{Z_N^{\rm red}} \frac{\partial^2  Z_N^{\rm red}}
{\partial t_{2k+1}\partial t_{2n-2k-1}}
\nn
\ee
but this is $not$ true for even derivatives. So, identity (\ref{colivirder0})
yet needs to be transformed a little more in order to contain exactly
(\ref{colivirder1}) at its r.h.s. If this is achieved, the l.h.s. acquires
additional contribution and turns into
\be
\new
\begin{array}{c}
\sum_{k>0} 2kt_{2k} \frac{\partial Z_N^{\rm red}}{\partial t_{2k+2n}} +
\sum_{k=0}^{n} \left( 2\frac{\partial^2 Z_N^{\rm red}}
{\partial t_{2k}\partial t_{2n-2k}}
- \frac{1}{Z_N^{\rm red}}
    \frac{\partial Z_N^{\rm red}}
{\partial t_{2k}}\frac{\partial Z_N^{\rm red}}{\partial t_{2n-2k}}\right)
=  \\
= 4\sqrt{Z_N^{\rm red}} L_{2n}^{\rm red} \sqrt{Z_N^{\rm red}}.
\end{array}
\label{colivirder3}
\ee

As a result of all this reasoning we conclude that the double scaling
continuum limit of reduced 1-matrix model can be described by the following
relation:
\be
\lim_{{\rm d.s.}\ \epsilon \rightarrow 0,\ N \rightarrow\infty}
\sqrt{Z_N^{\rm red}\{t_{\rm even}\}} \ = \ U^{-1}Z_{V = \frac{X^3}{3}}\{T\},
\ee
where factor $U$ is defined in (\ref{Umatrix}),  relation between $t$ and
$T$-variables is given by (\ref{Kazchava}) and
$Z_{V = \frac{X^3}{3}}\{T\}$ is $X^3$-Kontsevich model. The motivation for
this conclusion is that both sides of the equation satisfy the same continuous
Virasoro constraints (1.3).

This whole derivation can be straightforwardly generalized to the case of
multiscaling limit in conformal matrix models and analogous relation contains
roots of the $p$-th degree, see \cite{comamo} for detailed discussion.
