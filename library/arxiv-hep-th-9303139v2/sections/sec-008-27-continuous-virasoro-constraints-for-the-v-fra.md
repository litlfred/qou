---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-008-27-continuous-virasoro-constraints-for-the-v-fra
section_title: "Continuous Virasoro constraints for the $V = \frac{X^3}{3}$ Kontsevich model"
section_number: 2.7
pages: 32-46
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.966
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
This example is a little more complicated than that in the previous
subsection, and we do not present calculations in full details (see
\cite{MMM} and \cite{GKM}). Our goal is to demonstrate that the
constraints which arise in this model,
though still form  (Borel subalgebra of) some Virasoro
algebra, are $different$  from (\ref{virdid}). From the point of view of the
CFT-formulation the relevant model is that of the $twisted$ (in this
particular case - antiperiodic) free fields. These so called "continuous
Virasoro constraints" give the simplest illustration of the difference between
discrete and continuous matrix models: this is essentially the difference
between "homogeneous" (Kac-Frenkel) and "principal" (soliton vertex operator)
representation of the level $k=1$ Kac-Moody algebra. From the point of view of
integrable hierarchies this is the difference between Toda-chain-like and
KP-like hierarchies. We shall come back to a more detailed discussion of this
difference later, when the "multi-scaling continuum limit" will be considered.

Another (historical) aspect of the same relation also deserves mentioning,
since it also illustrates the interrelation between different models.
The discrete 1-matrix model arises naturally in description of quantum $2d$
gravity as sum over 2-geometries in the formalism of random equilateral
triangulations. The model, however, decribes only lattice approximation to
$2d$ gravity and (double-scaling) coninuum limit should be taken in order to
obtain the real (continuous) theory of $2d$ gravity. This limit was originally
formulated in terms of the contraint algebra (equations of motion or "loop"
or "Schwinger-Dyson" equations - terminology is taste-dependent), leaving open
the problem of what is the form of partition function ${\cal Z}^{cont}\{T\}$
of continuous theory. Since the relevant algebra appeared to be just the WI
for  Kontsevich model (with $V(X) = \frac{X^3}{3}$), this proves that the
latter one is exactly the continuous theory of pure $2d$ gravity. At the same
time, Kontsevich model itself can be naturally introduced as a theory of
$topological$ gravity (in fact this is how the model was originally discovered
in \cite{Ko}). From this point of view the constraint algebra, to be discussed
below in this subsection, plays central role in the proof of equivalence
between pure $2d$ quantum gravity and pure topological gravity (in both cases
"pure" means that "matter" fields are not introduced).

After these introductory remarks we proceed to  calculations. Actually they
just repeat those for the Gaussian model, performed in the previous
subsection, though formulas get somewhat more complicated. This time we do not
include zero-time $N$ and just use eq.(\ref{GNe}) with $V(X) = \frac{X^3}{3}$.
Now it is also much more tricky (though possible)
to work in  matrix notations (because
fractional powers of $ L$ will be involved) and we rewrite everything in
terms of the eigenvalues of $ L$.

We substitute
\be
\new
\begin{array}{c}
{\cal C}_{\frac{X^3}{3}} = \frac{\prod_\delta
e^{\frac{2}{3}\lambda_\delta^{3/2}}}
{\sqrt{\prod_{\gamma,\delta}
              (\sqrt{\lambda_\delta} + \sqrt{\lambda_\gamma})}},  \\
\left( \frac{\partial^2}{\partial L_{tr}^2}\right)_{\gamma\gamma} =
 \frac{\partial^2}{\partial\lambda_\gamma^2} +
     \sum_{\delta\neq\gamma}\frac{1}{\lambda_\gamma-\lambda_\delta}
     \left(\frac{\partial}{\partial\lambda_\gamma}
                 - \frac{\partial}{\partial\lambda_\delta}\right)
\end{array}
\nn
\ee
and introduce a special notation for
\be
\frac{{\cal D}}{{\cal D}\lambda_\gamma} \equiv
{\cal C}_{\frac{X^3}{3}}^{-1} \frac{\partial}{\partial \lambda_\gamma}
         {\cal C}_{\frac{X^3}{3}} =
 \frac{\partial}{\partial \lambda_\gamma} + \sqrt{\lambda_\gamma} -
\frac{1}{4\lambda_\gamma}
- \frac{1}{2} \sum_{\delta\neq\gamma}\frac{1}{\sqrt{\lambda_\gamma}
(\sqrt{\lambda_\delta} +
           \sqrt{\lambda_\gamma})}. \nn
\ee
Then (\ref{GNe}) turns into
\be
\left( \left(\frac{{\cal D}}{{\cal D}\lambda_\gamma}\right)^2 +
\sum_{\delta\neq\gamma}\frac{1}{\lambda_\gamma-\lambda_\delta}
\left(\frac{{\cal D}}{{\cal D}\lambda_\gamma} - \frac{{\cal D}}{{\cal
D}\lambda_\delta}\right)
\right) {\cal Z}_{\frac{X^3}{3}}\{T\} = 0.
\label{GNX3}
\ee
Now we need explicit expression for $T$:
\be
T_k = \frac{1}{k} L^{-k},
\label{KMX3T}
\ee
and as we already know from the previous subsection we  also need
\be
r_k = - \frac{2}{3}\delta_{k,3}.
\ee
It will not be explained untill we turn to consideration of integrable
structure of Kontsevich model in the following sections,
but ${\cal Z}_{\frac{X^3}{3}}\{T\}$ is
in fact independent of all time-variables with $even$ numbers
(subscripts). Therefore we can take only $k=2a+1$ in (\ref{KMX3T}),
\be
T_{2a+1} &= \frac{1}{2a+1} \sum_\delta \lambda_\delta^{-a-\frac{1}{2}}, \nn \\
r_{2a+1} &= - \frac{2}{3}\delta_{a,1}
\ee
and
\be
\frac{\partial}{\partial \lambda_\gamma} {\cal Z}_{\frac{X^3}{3}}\{T\} &=
\sum_{a=0}^{\infty} \frac{\partial T_{2a+1}}{\partial \lambda_\gamma}
   \frac{\partial{\cal Z}}{\partial T_{2a+1}} =
  -\frac{1}{2} \sum_{a=0}^{\infty} \lambda_\gamma^{-a-\frac{3}{2}}
                 \frac{\partial{\cal Z}}{\partial T_{2a+1}}; \nn \\
\frac{\partial^2}{\partial \lambda_\gamma^2} {\cal Z}_{\frac{X^3}{3}}\{T\} &=
  \frac{1}{4}\sum_{a,b=0}^{\infty} \lambda_\gamma^{-a-b-3}
                 \frac{\partial{\cal Z}}{\partial T_{2a+1}\partial T_{2b+1}} +
   \frac{1}{2} \sum_{a=0}^{\infty} (a + \frac{3}{2})
\lambda_\gamma^{-a-\frac{5}{2}}
                 \frac{\partial{\cal Z}}{\partial T_{2a+1}}. \nn
\ee
These expressions should be now substituted into (\ref{GNX3}) and we obtain:
\be
\new
\begin{array}{c}
\frac{1}{4}\sum_{a,b=0}^{\infty} \lambda_\gamma^{-a-b-3}
                 \frac{\partial{\cal Z}}{\partial T_{2a+1}\partial T_{2b+1}} +
 \\
+ \sum_{a=0}^{\infty} \left[
\frac{1}{2} \sum_{a=0}^{\infty}
(a + \frac{3}{2})\lambda_\gamma^{-a-\frac{5}{2}} -
\frac{1}{2} \sum_{\delta\neq\gamma}\frac{1}{\lambda_\gamma-\lambda_\delta}
\left(\lambda_\gamma^{-a-\frac{3}{2}} - \lambda_\delta^{-a-\frac{3}{2}}
\right) -
\right.
 \\
\left.
- \left( \sqrt{\lambda_\gamma} - \frac{1}{4\lambda_\gamma}
- \frac{1}{2} \sum_{\delta\neq\gamma}
\frac{1}{\sqrt{\lambda_\gamma}(\sqrt{\lambda_\delta} +
           \sqrt{\lambda_\gamma})}
\right)\lambda_\gamma^{-a-\frac{3}{2}}
\right]\frac{\partial{\cal Z}}{\partial T_{2a+1}} +  \\
+ \left[\ldots\right] {\cal Z}  \ \ \
= \ \ \ \sum_{n=-1}^{\infty} \frac{1}{\lambda_\gamma^{n+2}}{\cal L}_n{\cal Z}
\end{array}
\label{vircder}
\ee
with
\be
\new
\begin{array}{c}
{\cal L}_{2n} =
\sum_{a=0}^{\infty}
    \left(a+\frac{1}{2}\right)\left(T_{2a+1}+r_{2a+1}\right) \times \\ \times
\frac{\partial}{\partial T_{2a+2n+1}} +
\frac{1}{4} \sum_{\stackrel{a+b=n-1}{a,b\geq 0}}
\frac{\partial^2}{\partial T_{2a+1}\partial T_{2b+1}}
+  \frac{1}{16}\delta_{n,0} + \frac{1}{4} T_1^2\delta_{n,-1} = \\
= \frac{1}{2}\sum_{{\rm odd}\ k=1}^{\infty}
       k(T_k+r_k)\frac{\partial}{\partial T_{k+2n}} +
 \frac{1}{4} \sum_{{\rm odd}\ k = 1}^{2n-1}
\frac{\partial^2}{\partial T_k\partial T_{2n-k}} +
  \frac{1}{16}\delta_{n,0} + \frac{1}{4} T_1^2\delta_{n,-1}.
\end{array}
\label{vircidder}
\ee
Factor $\frac{1}{2}$ in front of the first term at the r.h.s. in
(\ref{vircidder}) is important for ${\cal L}_{2n}$ to satisfy the properly
normalized Virasoro algebra:\footnote{
Therefore it could be reasonable to use a different notation: ${\cal L}_n$
instead of ${\cal L}_{2n}$. We prefer ${\cal L}_{2n}$, because it emphasises
the property of the model to be 2-reduction of KP hierarchy (to KdV), see
section 4 below.
}
\be
\phantom. [{\cal L}_{2n}, {\cal L}_{2m}] = (n-m){\cal L}_{2n+2m}.
\nn
\ee
Coefficient $\frac{1}{4}$ in front of the second term can be eliminated by
rescaling of time-variables: $T \rightarrow \frac{1}{2}T$, then the last term
turns into $\frac{1}{16}T_1^2\delta_{n,-1}$.

We shall not actually discuss evaluation of the coefficient in front of
${\cal Z}$ (with no derivatives), which is denoted by $[\ldots]$ in
(\ref{vircder}) (see \cite{MMM} and \cite{GKM}). In fact almost all the terms
in original complicated expression cancel, giving finally
\be
\left[ \ldots \right] =
\frac{1}{16\lambda_\gamma^2} + \frac{T_1^2}{4\lambda_\gamma},
\nn
\ee
and this is represented by the terms with $\delta_{n,0}$ and $\delta_{n,-1}$
in expressions (\ref{vircidder}) for the Virasoro generators ${\cal L}_{2n}$.

The term with the double $T$-derivative in (\ref{vircder}) is already of the
necessary form. Of intermidiate complexity is evaluation of the coefficient in
front of $\frac{\partial{\cal Z}}{\partial T_{2a+1}}$ in (\ref{vircder}),
which we shall briefly describe now.
First of all, rewrite this coefficient, reordering the items:
\be
\frac{1}{2}\left[ (a + \frac{3}{2})\lambda_\gamma^{-a-\frac{5}{2}} -
 \sum_{\delta\neq\gamma}\frac{1}{\lambda_\gamma-\lambda_\delta}
\left(\lambda_\gamma^{-a-\frac{3}{2}} -
\lambda_\delta^{-a-\frac{3}{2}} \right)\right] +
\nn \\
+ \left[ \frac{1}{4}\lambda_\gamma^{-a-\frac{5}{2}} +
       \frac{1}{2} \sum_{\delta\neq\gamma}
\frac{\lambda_\gamma^{-a-2}}{\sqrt{\lambda_\delta} +
           \sqrt{\lambda_\gamma}} \right]
- \lambda_\gamma^{-a-1}.
\label{vircder2}
\ee
The first two terms together are equal to the sum over $all$ $j$ (including
$j=i$):
\be
- \frac{1}{2} \sum_\delta \frac{1}{\lambda_\gamma-\lambda_\delta}
\left(\lambda_\gamma^{-a-\frac{3}{2}} - \lambda_\delta^{-a-\frac{3}{2}} \right)
 =  \frac{1}{2} \sum_\delta \frac{\lambda_\gamma^{a+\frac{3}{2}} -
             \lambda_\delta^{a+\frac{3}{2}}}{\lambda_\gamma-\lambda_\delta}
  \cdot\frac{1}{\lambda_\gamma^{a+\frac{3}{2}}\lambda_\delta^{a+\frac{3}{2}}} =
\nn \\
= \frac{1}{2\lambda_\gamma^{a+2}} \sum_\delta
\frac{\lambda_\gamma^{a+2} - \lambda_\gamma^{\frac{1}{2}}
\lambda_\delta^{a+\frac{3}{2}}}
{\lambda_\gamma-\lambda_\delta}\cdot\frac{1}{\lambda_\delta^{a+\frac{3}{2}}}.
\nn
\ee
Similarly, the next two terms can be rewritten as
\be
\frac{1}{2} \sum_\delta \frac{\lambda_\gamma^{-a-2}}{\sqrt{\lambda_\gamma} +
\sqrt{\lambda_\delta}} =
\frac{1}{2\lambda_\gamma^{a+2}}
\sum_\delta \frac{\sqrt{\lambda_\gamma} - \sqrt{\lambda_\delta}}
{\lambda_\gamma-\lambda_\delta} = \nn \\
= \frac{1}{2\lambda_\gamma^{a+2}} \sum_\delta
\frac{\lambda_\gamma^{\frac{1}{2}} \lambda_\delta^{a+\frac{3}{2}} -
\lambda_\delta^{a+2}}
{\lambda_\gamma-\lambda_\delta}\cdot\frac{1}{\lambda_\delta^{a+\frac{3}{2}}}.
\nn
\ee
The sum of these two expressions is equal to
\be
\frac{1}{2\lambda_\gamma^{a+2}} \sum_\delta
\frac{\lambda_\gamma^{a+2} - \lambda_\delta^{a+2}}
{\lambda_\gamma-\lambda_\delta}
\cdot\frac{1}{\lambda_\delta^{a+\frac{3}{2}}}.
\nn
\ee
Note that powers $a+2$ are already integer and the remaining ratio can be
represented as a sum of $a+2$ terms. Adding also the last term from the l.h.s.
of (\ref{vircder2}), we finally obtain:
\be
-\frac{1}{\lambda_\gamma^{a+1}} + \frac{1}{2} \sum_{n=-1}^a
\frac{1}{\lambda_\gamma^{n+2}}\sum_\delta
\frac{1}{\lambda_\delta^{a-n+\frac{1}{2}}} =   \nn \\ =
\frac{1}{2}\sum_{n=-1}^a \frac{1}{\lambda_\gamma^{n+2}}
(2a-2n+1)(T+r)_{2a-2n+1}
\nn
\ee
in accordance with (\ref{vircder}) and (\ref{vircidder}).



\subsection{$\tilde W$-constraints for the asymmetric 2-matrix model}

We turn now to a very different application \cite{tildeW} of the GN equation
(\ref{GNe}). Namely, we shall now consider ${\cal F}_{V,n}\{ L\}$
as a building block in construction of conventional discrete two-matrix model
\be
Z_N\{t,\bar t\} \equiv c_N^2 \int dHd\bar H
e^{\sum_k (t_k {\rm Tr}H^k + \bar t_k {\rm Tr} \bar H^k) + {\rm Tr}H\bar H} =
\nn \\
= \int d L e^{\sum_k t_k {\rm Tr} L^k}
{\cal F}_{\bar U,N}\{ L\}.
\label{2mamo}
\ee
Now $ L$ plays the role of $H$ and $\bar U(\bar H) =
\sum_k\bar t_k  \bar H^k$.

We can now use GN equation to derive a relation for $Z_N\{t,\bar t\}$.
Take (\ref{GNe}),
\be
\left(\bar U (\frac{\partial}{\partial L_{tr}}) +  L\right)
{\cal F}_{\bar U,N}\{ L\} = 0,
\label{GNe'}
\ee
multiply it by  $e^{{\rm Tr}U( L)} = e^{\sum_k t_k {\rm Tr} L^k}$
and integrate over $ L$.
In order to express this relation in terms of $t$-derivatives of $z$ it is
necessary to have some "scalar" rather than $matrix$ equations, therefore
we"ll actually need to take trace of (\ref{GNe'}). However, in order not to
loose any information, we first multiply (\ref{GNe'}) by $ L^n$ and
$then$ take the trace. In this way we obtain:
\be
\int d L e^{\sum_k t_k {\rm Tr} L^k}
{\rm Tr}  L^n
\left(\bar U (\frac{\partial}{\partial L_{tr}}) +  L\right)
{\cal F}_{\bar U}\{ L\}  = 0.
\nn
\ee
Integration by parts gives:
\be
\int d L {\cal F}_{\bar U}\{ L\}
{\rm Tr}\left(\bar U (-\frac{\partial}{\partial L_{tr}}) +  L\right)
 L^n e^{\sum_k t_k {\rm Tr} L^k}.
\label{gana1}
\ee

Now we need to introduce a new class of operators \cite{tildeW}.
Consider the action of
${\rm Tr} \frac{\partial^m}{\partial  L_{tr}^m}  L^n$
on  $e^{{\rm Tr}U( L)} = e^{\sum_k t_k {\rm Tr} L^k}$. It
gives some linear combination of terms like
\be
{\rm tr} L^{a_1} ...{\rm tr} L^{a_l} e^{{\rm tr} U( L)} =
\frac{\partial^l}{\partial t_{a_1}...\partial t_{a_l}} e^{-{\rm tr} U( L)}
\nn
\ee
i.e. we obtain a combination of differential operators with $t$-derivatives,
to be denoted $\tilde W(t)$:
\be
\tilde W_{n-m}^{(m+1)}(t)
e^{{\rm tr} U( L)} \equiv
{\rm Tr} \frac{\partial^m}{\partial  L_{tr}^m}  L^n
e^{{\rm tr} U( L)}, \ \ \ m,n \geq 0.
\label{twop}
\ee
For example,
\be
\new
\begin{array}{c}
\tilde W_n^{(1)} = \frac{\partial}{\partial t_n}, \ \ n\geq 0;  \\
\tilde W_n^{(2)} = \sum_{k=0}^{\infty} kt_k\frac{\partial}{\partial t_{k+n}} +
    \sum_{k=0}^n \frac{\partial^2}{\partial t_k\partial t_{n-k}},
\ \ n\geq -1;   \\
\tilde W_n^{(3)} = \sum_{k,l = 1}^{\infty} kt_klt_l
\frac{\partial}{\partial t_{k+l+n}}
+ \sum_{k=1}^{\infty} kt_k
  \sum_{a+b=k+n}\frac{\partial^2}{\partial t_a\partial t_b}  + \\
+ \sum_{k=1}^{\infty} kt_k
  \sum_{a+b=n+1}\frac{\partial^2}{\partial t_a\partial t_{b+k-1}}
+ \sum_{a+b+c=n} \frac{\partial^3}{\partial t_a\partial t_b\partial t_c}
+ \frac{(n+1)(n+2)}{2}\frac{\partial}{\partial t_n};
 \\
\ldots
\end{array}
\label {twopex}
\ee
Note, that while $\tilde W_n^{(1)}$ and $\tilde W_n^{(2)}$
are just the ordinary $(U(1)$-Kac Moody and Virasoro
operators respectively, the higher $\tilde
W^{(m)}$-operators do $not$ coincide with the generators of the
{\bf W}-algebras: already
\be
\tilde W_n^{(3)} \neq W^{(3)} =
\sum_{k,l = 1}^{\infty} kt_klt_l
\frac{\partial}{\partial t_{k+l+n}}
+ 2\sum_{k=1}^{\infty} kt_k
  \sum_{a+b=k+n}\frac{\partial^2}{\partial t_a\partial t_b} \nn \\
+ \frac{4}{3}
  \sum_{a+b+c=n} \frac{\partial^3}{\partial t_a\partial t_b\partial t_c}.
\nn
\ee
$\tilde W$-operators (in variance with ordinary $W$-operators) satisfy
recurrent relation:
\be
\tilde W_n^{(m+1)} = \sum_{k=1}^{\infty} kt_k\tilde W_{n+k}^{(m)} +
          \sum_{k=0}^{m+n-1} \frac{\partial}{\partial t_k}
                      \cdot \tilde W_{n-k}^{(m)}, \ \ \ n\geq -m.
\ee
Actually not too much is already known about the ${\tilde W}$ operators and
the structure of $\tilde{\bf W}$-algebras (in particular it remains unclear
whether the negative harmonics $\tilde W_n^{(m+1)}$ with $n < -m$ can be
introduced in any reasonable way), see \cite{tildeW} for some preliminary
results.

Equation (\ref{gana1}) can now be represented in terms of the $\tilde
W$-operators:
\be
\int d L {\cal F}_{\bar U}\{ L\}
\left(\sum_{k\geq 1} k\bar t_k
\left(-\frac{\partial}{\partial L_{tr}}\right)^{k-1}
+  L\right) L^n e^{{\rm Tr}U(t)} = \nn \\
= \left(\sum_{k\geq 1} (-)^{k-1}k\bar t_k \tilde W_{n+1-k}^{(k)} +
     \tilde W_{n+1}^{(1)} \right) Z_N\{t,\bar t\} = 0.
\label{gana2}
\ee
This relation is highly asymmetric in $t$ and $\bar t$, and in fact it
provides a suitable description of the WI only in the somewhat peculiar case
when potential $\bar U(\bar H)$ is a polinomial of $finite$ degree. See
refs.\cite{GaNa} and \cite{tildeW} for discussion of such asymmetric models.


\subsection{$\tilde W$-constraints for generic 2-matrix model}

When both potentials $U$ and $\bar U$ in (\ref{2mamo}) are generic formal
seria, eqs.(\ref{gana2}) represent only a one-parametric subset of the
2-parametric family of WI. Before we describe the whole set, let us emphasize
that the two-matrix model (\ref{2mamo}) is the one, where the action is $not$
of the most general form, consistent with some symmetry. Therefore it is not
covariant under arbitrary change of variables $H,\bar H \longrightarrow
f(H,\bar H), \bar f(H,\bar H)$, and our usual method of derivation of Ward
identities does not work. The reason why generic 2-matrix model with action
containing all the possible combinations ${\rm Tr} (H^{a_1}\bar H^{b_1}
H^{a_2}\bar H^{b_2} ...)$  is never considered seriously is essentially our
poor understanding of the unitary-matrix interals for "non-eigenvalue"
theories, to which class such generic model belongs.
For reasons to be explained in the next section such problems do not arise for
the models of the form (\ref{2mamo})


or (\ref{comamo"}), and this is why they attracted most attention so far.
Hopefully the problems with the unitary-matrix integrals are temporal and
this restricted class of multimatrix models will be unlarged, this should be
especially easy to do in the part of the theory dealing with constraint
algebras, but this subject is beyond the scope of the present notes.

In order to derive the complete set of WI for the model (\ref{2mamo}), we
apply the following semi-artificial trick. Note that exponential
$e^{{\rm Tr}H\bar H}$ satisfies:
\be
\left( {\rm Tr} H^n\frac{\partial^m}{\partial H^m_{tr}} -
{\rm Tr} \bar H^m \frac{\partial^n}{\partial \bar H^n_{tr}}\right)
e^{{\rm Tr} H\bar H} = 0.
\label{wt2m1}
\ee
Let us integrate this identity over $H$ and $\bar H$ with the weight
$e^{{\rm Tr}U(H) + {\rm Tr}\bar U(\bar H)}$ and then integrate by parts.
We obtain an identity:
\be
\new
\begin{array}{c}
\int dHd\bar H e^{{\rm Tr} H\bar H} \cdot \\ \cdot
\left( {\rm Tr} \left(-\frac{\partial}{\partial H_{tr}}\right)^mH^n  -
{\rm Tr} \left(-\frac{\partial}{\partial \bar H_{tr}}\right)^n\bar H^m\right)
e^{{\rm Tr}U(H) + {\rm Tr}\bar U(\bar H)} = 0,
\end{array}
\label{wt2m2}
\ee
which can be represented in terms of $\tilde W$ operators \cite{GKM}:
\footnote{Relations (\ref{wt2m1}) and thus (\ref{twid}) are in the obvious
sense associated with $\ {\rm Tr} H^n\bar H^m$. Of course there are similar
relations, in the same sense associated with any object like
${\rm Tr} (H^{a_1}\bar H^{b_1}H^{a_2}\bar H^{b_2} ...)$
and with products of such traces: it is enough to substitute all
$\bar H \rightarrow \frac{\partial}{\partial H_{tr}}$ to obtain the l.h.s. of
the equation and substitute all $H \rightarrow \frac{\partial}{\partial
\bar H_{tr}}$ to obtain its r.h.s. (one should only remember that such
substitution is possible, say in the l.h.s. if all the $\bar H$ are put
to the right of all $H$, in order to restore the matrix-product form of the
relation, one should carefully take into account all the commutators, arising
when $\frac{\partial}{\partial H_{tr}}$ is carried back to original position
of the corresponding $\bar H$).
All such relations can appear to be just implications of eq.(\ref{twid}).
}
\be
\tilde W^{(m+1)}_{n-m}(t) Z\{t,\bar t\} =
(-)^{m-n}\tilde W^{(n+1)}_{m-n}(\bar t) Z\{t,\bar t\}, \ \ {\rm for\ all}\
m,n\geq 0.
\label{twid}
\ee

This is the full(?) set of WI for the 2-matrix model.
When one of potentials (say, $U(t)$ is polinomial of finite degree, the
most of this symmetry is "spontaneously broken", the surviving part being
described by eqs.(\ref{gana2}).

Among other things eq.(\ref{twid})
reveals an amusing automorphsim of the $\tilde{\bf W}_{\infty}$
algebra:
\be
\tilde W^{(m+1)}_{n-m} \longleftrightarrow  \tilde W^{(n+1)}_{m-n}, \ \ \
m,n\geq 0,
\ee
for example, Virasoro's Borel subalgebra is formed not only by operators
$\tilde W^{(2)}_n$, but also by $\tilde W^{(n+2)}_{-n}, \ n\geq -1$
(while $U(1)$ Borel subalgebra -  not only by $\tilde W^{(1)}_n =
\frac{\partial}{\partial t_n}$, but also by $\tilde W^{(n+1)}_n, \ n\geq 0$).

One can attempt to apply the same procedure and derive $\tilde W$-identites
for the conventional $(p-1)$-matrix models with $p-1 > 2$. In principle, this
is possible, but unfortunately the arising equations neither have a nice form
nor is there many enough of them. However, for illustrational purposes we shall
scetch some relevant fromulas in the rest of this subsection.

Consider the multimatrix integral
\be
\new
\begin{array}{c}
Z  = \int dH_1...dH_{p-1} \cdot
\\
\cdot e^{{\rm Tr}U_1(H_1) + \ldots + {\rm
Tr}U_{p-1}(H_{p-1})}\ldots e^{{\rm Tr}(H_1H_2 + H_2H_3 + \ldots
+H_{p-2}H_{p-1})}
\end{array}
\label{mumamosc}
\ee
Acting on $Z$, operator
$\ \displaystyle{\tilde W^{(m+1)}_{n-m}(t^{(1)})}\ $ produces an
insertion of
$\ \displaystyle{{\rm Tr} H_1^n \stackrel{\longleftarrow}
{\left(\frac{\partial}{\partial H_{1,tr}}\right)^m}}$
at the position of $\ldots$ in (\ref{mumamosc}).
Integration by parts gives:
\be
{\rm Tr} H_1^n \stackrel{\longrightarrow}
{\left(-\frac{\partial}{\partial H_{1,tr}}\right)^m}
\longrightarrow (-)^m{\rm Tr} H_1^nH_2^m = (-)^m{\rm Tr} H_2^mH_1^n
\nn
\ee

In the case of $p-1=2$, that we discussed above, this can be rewriten as
$\displaystyle{(-)^m{\rm Tr} H_1^m \stackrel{\longrightarrow}
{\left(\frac{\partial}{\partial H_{2,tr}}\right)^n}}$  and integration
by parts gives
$\displaystyle{(-)^m{\rm Tr} H_2^m \stackrel{\longleftarrow}
{\left(-\frac{\partial}{\partial H_{2,tr}}\right)^n}}$,
what is equivalent to the action of $(-)^{m+n}\tilde W^{(n+1)}_{m-n}(t^{(2)})$
on $Z$: we reproduce equation (\ref{twid}).

However, for $p-1>2$ things are more complicated. Insertion of ${\rm Tr}
H_2^mH_1^n$ is equivalent to that of
$\displaystyle{{\rm Tr} H_2^m\left(\stackrel{\longrightarrow}
{\frac{\partial}{\partial H_{2,tr}}} - H_3\right)^n}$, which after
integration by parts and acts on $e^{U_2(H_2)}$ and gives:
\be
\new
\begin{array}{c}
{\rm Tr} H_2^m\left(-\stackrel{\longleftarrow}
{\frac{\partial}{\partial H_{2,tr}}} - H_3\right)^n \sim
\\ \sim
{\rm Tr} H_2^m\left(\sum_k kt_k^{(2)}H_2^{k-1} - H_3\right)
\left(-\stackrel{\longleftarrow}
{\frac{\partial}{\partial H_{2,tr}}} - H_3\right)^{n-1} \sim \ldots
\end{array}
\ee
Derivatives remaining at the r.h.s. should be carried through the first
bracket and than act on $e^{U_2(H_2)}$ etc. After all we get
some linear combination of terms like
${\rm Tr} H_2^{b_1}H_3^{c_1}H_2^{b_2}H_3^{c_2}\ldots $
with $t^{(2)}$-dependent coefficients.

Now, if we are dealing with the $p-1=3$-matrix model, every $H_2$
standing to the right
of all $H_3$'s can be substituted by $\frac{\partial}{\partial H_{3,tr}}$,
otherwise one should also include terms with commutators when this
$\frac{\partial}{\partial H_{3,tr}}$ is carried back to the place where
$H_2$ was standing. In this way we obtain a combination of insertions of
the form
\be
\new
\begin{array}{c}
{\rm Tr} \stackrel{\longrightarrow}
{\left(\frac{\partial}{\partial H_{3,tr}}\right)^{b_1}}H_3^{c_1}
   \stackrel{\longrightarrow}
{\left(\frac{\partial}{\partial H_{3,tr}}\right)^{b_2}}H_3^{c_2}\ldots  \sim
\\
\sim {\rm Tr} \stackrel{\longleftarrow}
{\left(-\frac{\partial}{\partial H_{3,tr}}\right)^{b_1}}H_3^{c_1}
 \stackrel{\longleftarrow}
{\left(-\frac{\partial}{\partial H_{3,tr}}\right)^{b_2}}H_3^{c_2}\ldots
\end{array}
\ee
The resulting operator can be expressed through $\tilde W(t^{(3)})$ and we
obtain an identity, saying that some algebraic combination of
$\tilde W(t^{(1)})$ and $\tilde W(t^{(3)})$ with $t^{(2)})$-dependent
coefficients annihilates the partition function.

For $p-1>3$ insertion of $H_2$ is equivalent to that of
$\frac{\partial}{\partial H_{3,tr}} - H_4$
rather than  $\frac{\partial}{\partial H_{3,tr}}$, and the
procedure should be repeated again and again.
Finaly one arrives at constraints where the
operators are algebraic combinations of
$\tilde W(t^{(1)})$ and $\tilde W(t^{(p-1)})$ with the coefficients, which
depend on $t^{(2)},\ldots,t^{(p-2)}$ (moreover these are $infinite$
seria in $\tilde W$ operators, unless all the intermediate potentials
$U_2,\ldots,U_{p-2}$ are polinomials of $finite$ degree.

This is of course not a too illuminating procedure and in fact it was never
worked through to get concrete identities in any nice form.
Instead it can serve to
illustrate the problems, peculiar for the class of conventional multimatrix
models (at least for $p-1>2$). It can also emphasize the beauty of $conformal$
multimatrix models, which have clear advantages already at the level of
Ward identites.


\subsection{$\tilde W$-operators in Kontsevich model}

After $\tilde W$-operators are introduced, we can also rewrite the GN equation
(\ref{riv1})
for Kontsevich models in terms of $\tilde W$'s. Namely, we shall prove the
following identity
\cite{tildeW}:
\be
\left(\frac{\partial}{\partial
\Lambda_{tr}}\right)^{m+1} {\cal Z}\{ T_k\} =
(\pm)^{m+1}
\sum_{l\geq 0} \Lambda^{-l-1} \tilde W_{l-m}^{(m+1)}( T)
{\cal Z}\{ T_k\},
\label{tiwko}
\ee
valid for $any$ function ${\cal Z}$ which depends on
$ T_k = \mp\frac{1}{k}{\rm tr}\Lambda^{-k},\ \ k\geq 1\ $ and
$ T_0 = \pm{\rm tr}\log \Lambda$
with $n\times n$ matrix $\Lambda$.
Application of the identity (\ref{tiwko}) is most straightforward in the
Gaussian model (\ref{gako}), e.g. for transformation of eq.
(\ref{gako3}) into eq.(\ref{gako4})
(we remind that $ L = \Lambda$ in this case).
In other cases calculations with the use of identity
(\ref{tiwko}), accounting for the quasiclassical factor
${\cal C}_V\{ L\}$ and the difference between $ L = V'(\Lambda)$ and $\Lambda$
become somewhat more involved, though still seem enough straightforward.
Also for particular potentials
$V(X)$ partition function ${\cal Z}_V\{T\}$  is actually independent of
certain (combinations of) time-variables (for example, if
$V(X) = \frac{X^{p+1}}{p+1}$ it is independent of all $T_{pk},\ k\in Z_+$),
and this is
important for appearence of the constraints in the standard from like
eqs.{\ref{vircder}), (\ref{vircidder}),
i.e. for certain $reduction$ of $\tilde W$-constraints to the ordinary
$W$-constraints. This relation between $\tilde W$- and $W$-operators deserves
further investigation.

The proof of eq.(\ref{tiwko}) is provided by the following trick. Let us make
a sort of Fourier transformation:
\be
{\cal Z}\{ T\} =
\int dH\ {\cal G}\{H\} e^{\sum_{k=0}^{\infty} T_k{\rm Tr}H^k},
\label{mafoutr}
\ee
where integral is over $N\times N$ Hermitean matrix $H$.\footnote{
Here it is for the first time that we encounter an important idea: matrix
models
- the ordinary 1-matrix model (\ref{1mamo'})
in this case - can be considered as defining integral transformations. This
view on matrix models can to large extent define their role in the future
developement of string theory.
}
Then it is clear that once the identity (\ref{tiwko}) is established for
${\cal Z}\{ T\}$ substituted by $ e^{{\rm Tr} U(H)},\ \
 U(H) = \sum_{k=0}^{\infty} T_k{\rm Tr}H^k$, with any matrix $H$,
it is valid for $any$ function ${\cal Z}\{ T\}$. The advantage of such
substitution is that we can now make use of the definition (\ref{twop})
of the $\tilde W$ operators in order to rewrite (\ref{tiwko}) in a very
explicit form:
\be
\left(\frac{\partial}{\partial \Lambda_{tr}}\right)^{m+1}
e^{{\rm Tr} U(H)} =
(\pm)^{m+1}\sum_{l \geq 0}^{\infty} \Lambda^{-l-1}
 \tilde W_{l-m}^{(m+1)}( T) e^{{\rm Tr} U(H)} = \nn \\
= (\pm)^{m+1}
\sum_{l \geq 0}^{\infty} \Lambda^{-l-1} {\rm Tr}
\left(\frac{\partial}{\partial H_{tr}}\right)^m H^l
e^{{\rm Tr} U(H)} = \nn \\
= (\pm)^{m+1}
{\rm Tr}\left(\frac{\partial}{\partial H_{tr}}\right)^m
\frac{1}{\Lambda\otimes I - I\otimes H} e^{{\rm Tr} U(H)}.
\label{tiwkoder1}
\ee
Now expression for $ T$'s in terms of $\Lambda$ should be used. Then
\be
e^{{\rm Tr} U(H)} =  Det^{\pm 1} (\Lambda\otimes I - I\otimes H)
\nn
\ee
and substituting this into (\ref{tiwkoder1}) we see that (\ref{tiwko}) is
equivalent to
\be
\left( \left(\frac{\partial}{\partial \Lambda_{tr}}\right)^{m+1} -
(\pm)^{m+1} I\cdot{\rm Tr} \left(\frac{\partial}{\partial H_{tr}}\right)^m
\cdot \frac{1}{\Lambda\otimes I - I\otimes H}
\right)\cdot \nn \\
\cdot  Det^{\pm 1} (\Lambda\otimes I - I\otimes H) = 0
\label{tiwkoder2}
\nn
\ee
Here "${\rm Tr}$" stands for the trace in the $H$-space only, while
$Det = {\rm Det}\otimes {\rm det}$ - for determinant in both $H$ and
$\Lambda$ spaces.
After one $\Lambda$-derivative is taken explicitly, we get:
\be
\left(I\otimes{\rm Tr}\right) \left( \left(\frac{\partial}{\partial
\Lambda_{tr}}\right)^m\otimes I -  I\otimes \left(\pm\frac{\partial}{\partial
H_{tr}}\right)^m
\right)
\cdot \nn \\ \cdot
\frac{Det^{\pm 1} (\Lambda\otimes I -  I\otimes H)}
{\Lambda\otimes I - I\otimes H} = 0.
\label{tiwkoder3}
\ee
This is already a matrix identity,
valid for any $\Lambda$ and $H$ of the sizes
$n\times n$ and $N\times N$ respectively. For example, if $m=0$ ($\tilde
W^{(1)}$-case), it is obviously satisfied. If both $n=N=1$, it is also
trivially true, though for different reasons for different choice of signs:
for the upper signs, the ratio at the l.h.s. is just unity and all derivatives
vansih; for the lower signs we have:
\be
\left(\frac{\partial}{\partial \lambda }\right)^m  -
\left(-\frac{\partial}{\partial h}\right)^m =
\left(\sum_{\stackrel{a+b=m-1}{a,b\geq 0}}
\left(\frac{\partial}{\partial \lambda }\right)^a
\left(-\frac{\partial}{\partial h}\right)^b \right)
\left(\frac{\partial}{\partial \lambda }  + \frac{\partial}{\partial h}\right),
\nn
\ee
and this obviously vanishes since $(\frac{\partial}{\partial \lambda } +
\frac{\partial}{\partial h})f(\lambda -h) \equiv 0$ for any $f(x)$.

If $m>0$ and $\Lambda,\ H$ are indeed {\it matrices},
direct evaluation becomes much more
sophisticated. We present the first two nontrivial examples: $m=1$ and $m=2$.
The following relartions will be usefull. Let
$Q \equiv  \frac{1}{\Lambda\otimes I - I\otimes H}$. Then
\be
Det^{\pm 1}Q \frac{\partial}{\partial \Lambda_{tr}}  Det^{\mp 1} Q =
\pm\left[(I\otimes {\rm Tr})Q\right]; \nn \\
Det^{\pm 1}Q \frac{\partial}{\partial H_{tr}}  Det^{\mp 1} Q =
\mp\left[({\rm tr}\otimes I)Q\right]; \nn \\
\left(\frac{\partial}{\partial \Lambda_{tr}}\otimes I\right) Q =
-\left[({\rm tr}\otimes I)Q\right]Q;
\nn \\
\left(I\otimes\frac{\partial}{\partial H_{tr}}\right) Q =
\left[(I\otimes {\rm Tr})Q\right]Q.
\label{tiwkoder5}
\ee

This is already enough for the proof in the case of $m=1$. Indeed:
\be
Det^{\pm 1}Q \left(\frac{\partial}{\partial \Lambda_{tr}}\otimes I \mp
    I\otimes \frac{\partial}{\partial H_{tr}}\right)Q Det^{\mp 1} Q = \nn \\
= \{-\left[({\rm tr}\otimes I)Q\right]Q
  \pm \left[(I\otimes {\rm Tr})Q\right]Q \}\mp \nn \\
\mp\{ \left[(I\otimes {\rm Tr})Q\right]Q \mp
 \left[({\rm tr}\otimes I)Q\right]Q \} = 0. \nn
\ee
The first two terms at the r.h.s. come arise from $\Lambda$-, while the
last two - from $H$-derivatives.

In the case of $m=2$ one should take derivatives once again. This is a little
more tricky, and the same compact notation are not sufficient. In addition to
(\ref{tiwkoder5}) we now need:
\be
\left(\frac{\partial}{\partial \Lambda_{tr}}\otimes I\right)
\left[({\rm tr}\otimes I)Q\right]Q =
- \left[({\rm tr}\otimes I)Q\right]^2 Q - {\cal B}.
\label{tiwkoder7}
\ee
Here
\be
\left[({\rm tr}\otimes I)Q\right]^2 =
\left[({\rm tr}\otimes I)\left[({\rm tr}\otimes I)Q\right]Q\right],
\label{tiwkoder8}
\ee
while in order to write ${\cal B}$ explicitly we need to restore matrix
indices (Greek for the $\Lambda$-sector and Latin - for the $H$ one). The
$(\alpha i,\gamma k)$-component of (\ref{tiwkoder7}) looks like:
\be
\left(\frac{\partial}{\partial \Lambda_{\beta\alpha}}\delta^{im}\right)
Q_{\delta\delta}^{mj}Q_{\beta\gamma}^{jk} =
- Q_{\delta\delta}^{ij}Q_{\beta\beta}^{jl}Q_{\alpha\gamma}^{lk} -
  Q_{\delta\beta}^{il}Q_{\alpha\delta}^{lj}Q_{\beta\gamma}^{jk}
\ee
and appearence of the second term at the r.h.s. implies, that
${\cal B}_{\alpha\gamma}^{ik} =
Q_{\delta\beta}^{il}Q_{\alpha\delta}^{lj}Q_{\beta\gamma}^{jk}$.
Further,
\be
&\left(\frac{\partial}{\partial \Lambda_{tr}}\otimes I\right)
\left[(I\otimes {\rm Tr})Q\right]Q =  \nn \\
&-\left[(I\otimes {\rm Tr})\left[({\rm tr}\otimes I)Q\right]Q\right]Q
-\left[(I\otimes {\rm Tr})\left[(I\otimes {\rm Tr})Q\right]Q\right]Q; \nn \\
&\left( I\otimes \frac{\partial}{\partial H_{tr}}\right)
\left[({\rm tr}\otimes I)Q\right]Q = \nn \\
&+ \left[({\rm tr}\otimes I)\left[(I\otimes {\rm Tr})Q\right]Q\right]Q +
  \left[(I\otimes {\rm Tr})\left[({\rm tr}\otimes I)Q\right]Q\right]Q; \nn \\
&\left( I\otimes \frac{\partial}{\partial H_{tr}}\right)
\left[(I\otimes {\rm Tr})Q\right]Q =
+ \left[(I\otimes {\rm Tr})\left[(I\otimes {\rm Tr})Q\right]Q\right]Q
+{\cal B}.
\ee
It is important that ${\cal B}$ that appears in the last relation
in the form of
${\cal B}_{\alpha\gamma}^{ik} =
Q_{\alpha\delta}^{lj}Q_{\delta\beta}^{il}Q_{\beta\gamma}^{jk}$
is exactly the same ${\cal B}$ as in eq.(\ref{tiwkoder7}).

Now we can prove (\ref{tiwkoder3}) for $m=2$:
\be
&Det^{\pm 1}Q \left(\left(\frac{\partial}{\partial
\Lambda_{tr}}\right)^2\otimes I -
I\otimes \left(\frac{\partial}{\partial H_{tr}}\right)^2\right)
Q Det^{\mp 1} Q =  \nn \\
&= \left\{
\pm\left[(I\otimes{\rm Tr})Q\right]\left(
- \left[({\rm tr}\otimes I)Q\right]Q \pm \left[(I\otimes{\rm Tr})Q\right]Q
\right) - \right. \nn \\ &\left. - \left(
- \left[({\rm tr}\otimes I)\left[({\rm tr}\otimes I)Q\right]Q\right]Q - {\cal
B}
\right) \pm \right. \nn \\ &\left. \pm \left(
- \left[(I\otimes{\rm Tr})\left[({\rm tr}\otimes I)Q\right]Q\right]Q -
  \left[({\rm tr}\otimes I)\left[(I\otimes{\rm Tr})Q\right]Q\right]Q
\right)\right\} - \nn \\
&- \left\{
\mp\left[({\rm tr}\otimes I)Q\right]\left(
\left[(I\otimes{\rm Tr})Q\right]Q \mp \left[({\rm tr}\otimes I)Q\right]Q
\right) + \right. \nn \\ &\left. + \left(
\left[(I\otimes{\rm Tr})\left[(I\otimes{\rm Tr})Q\right]Q\right]Q + {\cal B}
\right) \mp \right. \nn \\ &\left. \mp \left(
\left[({\rm tr}\otimes I)\left[(I\otimes{\rm Tr})Q\right]Q\right]Q +
\left[(I\otimes{\rm Tr})\left[({\rm tr}\otimes I)Q\right]Q\right]Q
\right)\right\}
\ee
where the terms 1,2,3,4,5,6 in the first braces cancel the terms 1,3,2,4,6,5
in the second braces and identity (\ref{tiwkoder8}) and its counterpart with
$({\rm tr}\otimes I) \rightarrow  (I\otimes {\rm Tr})$ is used.

Explicit proof of eq.(\ref{tiwkoder3}) for generic $m$ is unknown.


\













\bigskip
