---
doc_id: arxiv-1205.4619v1
doc_title: "Quaternion-Octonion Unitary Symmetries and Analogous Casimir Operators"
section_id: sec-004-5-generators-and-casimir-invariants
section_title: "Generators and Casimir Invariants"
section_number: 5
pages: 9-11
source_pdf: 1205.4619v1.pdf
source_sha256: 8c76e30a52dca571
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.95
doc_brief: "Quaternion-Octonion Unitary Symmetries and Analogous Casimir Operators — An attempt has been made to investigate the global SU(2) and SU(3) unitary ﬂavor symmetries systematically in terms of"
---
A very useful concept in group representation theory is that of Casimir
operators \cite{key-16,key- 29} although there is no general agreement
\cite{key-15} on a unique definition of Casimir operator\cite{key-8,key-9}.
Nonetheless, there exists a set of invariant matrices \cite{key-15}
which can be constructed from the contractions of the generators of
a Lie group. Such invariant matrices are called the Casimir operators
\cite{key-15,key- 29} and hence commute with all the generators of
a Lie group. A familiar example, from ordinary quantum mechanics,
is the Casimir operator $\hat{L}^{2}$ for the rotation group. It
commutes with the three generators $\overrightarrow{L}$ of the rotation
group and its eigenvalues $l(l+1)\hslash^{2}$ label the 'simplest'
states of particles with angular momentum. Hence, a Casimir operator
is a nonlinear function of the generators that commutes with all of
the generators of the group. The adjoint representation of the algebra
is given by the structure constants , which are always real i.e. 

\begin{align}
\left[\widehat{X}_{A}\,,\widehat{X}_{B}\right]=i & f_{ABC}\,\widehat{X}_{C};\nonumber \\
\left[\widehat{X}_{A}\,,\left[\widehat{X}_{B}\,,\widehat{X}_{C}\right]\right]=if_{BCD}\left[\widehat{X}_{A}\,,\widehat{X}_{D}\right] & =-f_{BCD}f_{ADE}\widehat{X}_{E}.\label{eq:45}
\end{align}
If there are $N$ generators, then we get a $N\times N$ matrix representation
in the adjoint representation. From the Jacobi identity,

\begin{align}
\left[\widehat{X}_{A}\,,\left[\widehat{X}_{B}\,,\widehat{X}_{C}\right]\right]+\left[\widehat{X}_{B}\,,\left[\widehat{X}_{C}\,,\widehat{X}_{A}\right]\right]+\left[\widehat{X}_{C}\,,\left[\widehat{X}_{A}\,,\widehat{X}_{B}\right]\right] & =0;\label{eq:46}
\end{align}
we get the similar relation for the structure constants i.e. $f_{BCD}f_{ADE}+f_{ABD}f_{CDE}+f_{CAD}f_{BDE}=0.$
The states of the adjoint representation correspond to the generators
$|\widehat{X}_{a}>$. We may now consider the simple Lie-algebras
whose generators satisfy the commutation relation

\begin{align}
\left[\mathbb{\mathbb{T}}^{a},\mathbb{\mathbb{T}}^{b}\right]= & \sum_{k}f^{abc}\mathbb{\mathbb{T}}^{c};\label{eq:47}
\end{align}
where we use Hermitian generators $\mathbb{\mathbb{T}}^{a}$ in order
to choose the Killing form \cite{key-16} proportional to $\delta^{ab}$i.e.

\begin{align}
Trace\,\mathbb{\mathbb{T}}^{a}\mathbb{\mathbb{T}}^{b} & \propto\delta^{ab};\label{eq:48}
\end{align}
with a positive and representation dependent proportionality constant
that can be fixed from the choice of the group. With this convention
the structure constants $f^{abc}$ are real and completely anti-symmetric
and the generators of the adjoint representation are related \cite{key-16}
to the structure constants

\begin{align}
\left(\mathbb{\mathbb{T}}_{A}\right)_{bc}^{a}= & -i\, f^{abc}.\label{eq:49}
\end{align}
From the commutation relations (\ref{eq:45}), one can write the anti-symmetric
structure constant as

\begin{align}
f^{abc}= & -\frac{i}{\hat{C}}\,\, Trace\left[\left[\mathbb{\mathbb{T}}^{a},\mathbb{\mathbb{T}}^{b}\right]\mathbb{\mathbb{T}}^{c}\right];\label{eq:50}
\end{align}
where the generators $\mathbb{\mathbb{T}}^{a}$ act on $N\times N$
matrices of a semi simple Lie (Special Unitary $SU(N)$) group of
$N^{2}-1$ generators under the condition $Trace\,\mathbb{\mathbb{T}}^{a}=0$
and $\hat{C}$ is Casimir operator. So, the adjoint representation
of the group plays an important role to examine the Casimir operators
due to the equation (\ref{eq:47}). Hence, the commutation relation
(\ref{eq:46}) does not really diminish the number of generators of
the adjoint representation. Rather, it is a different way of writing
the Jacobi identity \cite{key-16}. Casimir operator for corresponding
group, every expression $\hat{C}$ in the $\mathbb{\mathbb{T}}^{a}$'s
commutes with all the basis elements of the algebra i.e. $\left[\hat{C},\mathbb{\mathbb{T}}^{a}\right]=0.$
In general,$\hat{C}$ does not belong to the algebra as it is not
linear in $\mathbb{\mathbb{T}}^{a}.$ The number of generators required
to give a complete set of Casimir invariants is equal to the rank
of the group. Casimir operators are used to label irreducible representations
of the Lie algebra. The utility of Casimir operators arises from the
fact that all states in a given representation assume the same value
for a Casimir operator. This is because the states in a given representation
are connected by the action of the generators of the Lie algebra and
such generators commute with the Casimir operators. This property
may then be used to label representations in terms of the values of
the Casimir operators.
