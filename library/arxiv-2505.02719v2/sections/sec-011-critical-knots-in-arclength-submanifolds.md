---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-011-critical-knots-in-arclength-submanifolds
section_title: "Critical knots in arclength submanifolds"
section_number: null
pages: 23-26
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.995
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:AL-critical}
In this abstract setting we consider for $s\in (\frac{1}{2},1]$  
an arbitrary  continuously differentiable parameter-invariant
energy 
$$
\EL \colon \OL \ceq H^{1+s}_\reg(\R/\Z,\R^n)\to\R.
$$
The latter means that 
$\EL(\eta)=\EL(\eta\circ\psi)$ for any $\eta\in\OL$,
where $\psi\in H^{1+s}([0,1])$ is a
strictly increasing parameter transformation with $\psi(0)=0$ and $\psi(1)=1$,
which can be extended to all of $\R$ to satisfy $\psi(t+1)=1+\psi(t)$
for all $t\in\R$.  

One of the simplest examples of such a parameter-invariant functional is the
length $\LL \colon \OL\to\R$, which is actually a smooth submersion, since its differential
$\D\LL_\eta\colon T_\eta\OL\simeq H^{1+s}(\R/\Z,\R^n)\to T_{\LL(\eta)}\R\simeq\R$
satisfies $\D\LL_\eta(\eta)=\LL(\eta)$ for all $\eta\in\OL$ because of the 
positive
$1$-homogeneity of $\LL$ and Euler's homogeneous function 
theorem. 
Hence, by the preimage theorem \cite[Theorem 4.J]{zeidler_1993}, the set
\begin{equation}\label{eq:Omega-s}
\varOmega^{1+s}\ceq\{\g\in\OL:\LL(\g)=1\}=\LL^{-1}(1),
\end{equation}
is a smooth submanifold of $\OL$
with its tangent space given by
\begin{equation}\label{eq:TgOmega-s}
	T_\g\varOmega^{1+s}
	=
	\bigg\{
		\nu\in H^{1+s}(\R/\Z,\R^n) 
		: 
		\D\LL_\g(\nu)=\int_0^1\sdfrac{\langle\g'(u),\nu'(u)\rangle}{|\g'(u)|}\d u=0
	\bigg\}.
\end{equation}
We also consider the smooth submanifolds with a fixed point $\bz\in\R^n$:
\begin{equation}\label{eq:Omega-sz}
\varOmega^{1+s}_\bz\ceq\{\g\in\varOmega^{1+s}:\g(0)=\bz\}
\end{equation}
with tangent space
\begin{equation}\label{eq:TgOmega-sz}
T_\g\varOmega^{1+s}_\bz=\{\nu\in T_\g\varOmega^{1+s}:\nu(0)=0\}.
\end{equation}
We now relate the arclength manifolds $\NL^{1+s}$ and $\NL^{1+s}_{\bz}$ 
to $\varOmega^{1+s}$ and
$\varOmega^{1+s}_{\bz}$ via general parameter-invariant energies $\EL\in C^1(\OL)$
and their critical points under a fixed-length constraint.

Note that as before, since $ \AL^{1+s} $ and $ \AL^{1+s}_{\bz} $ are open subsets of $ \NL^{1+s} $ and $ \NL_{\bz}^{1+s} $ respectively, the results of this section hold as well for arclength parametrized knots if we choose $ \OL$ to be the open set $ H^{1+s}_{\injreg}(\R/\Z,\R^n) $. This is due to the fact that the corresponding tangent spaces coincide; see \cref{eq:tangent-space-AL,eq:tangent-space-ALz}.
Only $|\g'|=1$ will be used in the arguments of this subsection, injectivity of $\g$ does not play a r{\^o}le here.

\begin{theorem}[Arclength criticality vs. criticality under length constraint]
\label{thm:critical-points}
Let $s\in (\frac{1}{2},1]$ and $ \ML\in \{\NL^{1+s},\AL^{1+s}\} $.
If $\g\in\ML\cap H^{2+s}(\R/\Z,\R^n)$ is a critical point of the restricted
parameter-invariant energy $\widetilde{\EL}\ceq\EL|_{\ML}$, 
then $\g$ is a critical
point of $\EL-\lambda\LL$ on $\OL$ for some $\lambda\in\R$. If  
$\EL$ is 
positively $\alpha$-homogeneous for some 
$\alpha\in\R$, then
$\lambda = \alpha \, \EL(\g) = \alpha \, \widetilde{\EL}(\g)$. In particular, if $\alpha\not=0$ and
$\widetilde{\EL}(\g)\not= 0$ then $\lambda\not= 0$, whereas
if $\EL$ is scale-invariant or $\widetilde{\EL}(\g)=0$, then $\lambda=0$.
\end{theorem}

Notice that we require higher regularity of the critical point, 
which we will verify for the energies in
our applications in geometric knot theory in \cref{sec:Smoothness}. 
This higher regularity  is necessary in
the following decomposition of tangent vectors $\nu\in T_\g\varOmega^{1+s}$
into a tangential and a non-tangential part  with respect to $\g$. 
We lose one derivative of $\g$ when we split off the tangential part.
\begin{lemma}[Decomposition of tangent vectors]
\label{lem:decomposition}
For any $\g\in \NL^{1+s}\cap H^{2+s}(\R/\Z,\R^n)\subset\varOmega^{1+s}$ 
and $\nu\in T_\g\varOmega^{1+s}$ there exists
$h\in T_\g\NL^{1+s}$ and a function $\varrho\in H^{1+s}(\R/\Z)$ with $\varrho(0)=\varrho(1)=0$, such 
that 
\begin{equation}\label{eq:decomposition}
	\nu(t)=h(t) + \varrho(t) \, \g'(t)\quad\Foa t\in\R/\Z.
\end{equation}
Likewise, if $\g\in\NL^{1+s}_{\bz}\cap H^{2+s}(\R/\Z,\R^n)$ for some fixed $\bz\in\R^n$
then every $\nu\in T_\g\varOmega^{1+s}_\bz$ can be decomposed as in \cref{eq:decomposition}
where now $h\in T_\g\NL^{1+s}_\bz$.
\end{lemma}
\begin{proof}
Set $\varrho(t)\ceq\int_0^t \inner{\nu'(u),\g'(u)}_{\R^n} \dd u$, which is of class
$H^{1+s}(\R/\Z)$ due to the product rule (see, e.g., \cite[Proposition A.5]{knappmann-etal_2023}), and satisfies $\varrho(0)=0=\varrho(1)$ since $\nu\in T_\g\varOmega^{1+s}$ and
$\abs{\g'}=1$ on $\R/\Z$. The function $h\ceq\nu-\varrho\g'$ is in $H^{1+s}(\R/\Z,\R^n)$
because of our regularity assumption on $\g$ and by the product rule, and one
computes (abbreviating $\inner{\cdot,\cdot} \ceq \inner{\cdot,\cdot}_{\R^n}$)
\begin{align*}
	\inner{h',\g'} 
	&=
	\inner{\nu',\g'} -\varrho' \inner{\g',\g'}-\rho \inner{\g'',\g'}
	=
	\inner{\nu',\g'} - \inner{\nu',\g'} \inner{\g',\g'}
	=
	0,
\end{align*}
where we used the definition of $\varrho$ and the fact that $\g$ is arclength parametrized.
Therefore, $h\in T_\g\NL^{1+s}$ (see \cref{eq:tangent-space-AL}), which establishes the decomposition \cref{eq:decomposition}.

With the same Ansatz for $\varrho$ one obtains for $\g\in\NL^{1+s}_\bz$ 
and $\nu
\in T_\g\varOmega_\bz^{1+s}$ that $h(0)=\nu(0)-\varrho(0)\g'(0)=0$ so that 
$h\in T_\g\NL^{1+s}_\bz$ by means of \cref{eq:tangent-space-ALz}.
\end{proof}
With this decomposition of tangent vectors of $\varOmega^{1+s}$ and 
$\varOmega^{1+s}_\bz$ we can
now prove criticality under the fixed-length constraint.

\begin{refproof}[Proof of \cref{thm:critical-points}]
As mentioned earlier, it suffices to prove the theorem for $ \ML=\NL^{1+s} $. For arbitrary $\nu\in T_\g\varOmega^{1+s}$ we find 
according to \cref{lem:decomposition}
some $h\in T_\g\ML$ and a function $\varrho\in H^{1+s}(\R/\Z)$ with $\varrho(0)=\varrho(1)=0$ such that
\cref{eq:decomposition} holds true. Consider the family $\varphi_\tau\ceq
\Id_\R + \tau\varrho\in H^{1+s}([0,1])$ satisfying $\varphi_\tau(0)=0$ and
$\varphi_\tau(1)=1$, and 
$$
\varphi_\tau'(t)=1+\tau\varrho'(t)\ge 1 - \abs{\tau} \norm{\varrho'}_{C^0}\ge
1-\tau_0 \,C_E \norm{\varrho}_{H^{1+s}}>0\quad\Foa t\in [0,1],
$$
if $|\tau|\le\tau_0\ll 1$. Here, $C_E$ denotes the constant of the Morrey embedding
theorem \cite[Theorem A.2]{knappmann-etal_2023}. So, $\psi\ceq\varphi_\tau$ is an
admissible strictly increasing parameter transformation under which $\EL$ is assumed to be invariant, i.e.,
the function $\tau\mapsto \EL(\g\circ\varphi_\tau)$ is constant on $(-\tau_0,\tau_0)$.
With 
the additional properties 
$$
	\textstyle
	\frac{\partial}{\partial \tau}\varphi_\tau(t) |_{\tau=0}
	=
	\varrho(t)
	\quad\AND\quad
	\varphi_0(t) = t \quad\Foa t\in [0,1],
$$
we conclude
\begin{align*}
	0 &
	\textstyle
	= 
	\frac{\partial}{\partial \tau}\EL(\g\circ\varphi_\tau) \big|_{\tau=0}
	= 
	\D\EL_\g \!\pars[\big]{ \pars{\g'\circ\varphi_0} \cdot\frac{\partial}{\partial \tau}\varphi_\tau |_{\tau=0} }
	=
	\D\EL_\g(\varrho\g')
	\\
	&\overset{\cref{eq:decomposition}}{=}
	\D\EL_\g(\nu-h)
	=
	\D\EL_\g(\nu)-\D\EL_\g(h)
	=
	\D\EL_\g(\nu)-\D\widetilde{\EL}_\g(h)
	=
	\D\EL_\g(\nu)
	.
\end{align*}
Since $\nu\in T_\g\varOmega^{1+s}$ 
was arbitrary we infer from the Lagrange multiplier 
theorem (see \cite[Corollary 3.5.29]{abraham-etal_1988}) 
that there is some number $\lambda\in\R$ such that
$(\D\EL-\lambda \D\LL)_\g=0$.

For the evaluation of $\lambda$ we use that $\LL(\g)=1$,
the positive
$1$-homogeneity of $\LL$, and the positive $\alpha$-homogeneity of $\EL$ to
compute with Euler's homogeneous function theorem
$
\lambda = \lambda \, \LL(\g) = \lambda \D\LL_\g(\g) = \D\EL_\g(\g) = \alpha \, \EL(\g) =
 \alpha \, \widetilde{\EL}(\g).
$
\end{refproof}

Fixing a point $\bz\in\R^n$ adds a vectorial constant Lagrange multiplier.
\begin{corollary}[Criticality with fixed point]
\label{cor:critical-points}
Let $s\in (\frac{1}{2},1]$, $\bz\in\R^n$ and $ \ML_{\bz}\in \{\NL^{1+s}_{\bz},\AL^{1+s}_{\bz}\} $. If $\g\in\ML_{\bz}\cap
H^{2+s}(\R/\Z,\R^n)$ is a critical knot of the restricted 
parameter-invariant energy
$\widetilde{\EL}\ceq\EL|_{\ML_{\bz}}$, then $\g$ is critical for
$\EL-\lambda \, \LL- \inner{\Upsilon,P_0(\cdot)}$ for some
$\lambda\in\R$ and $\Upsilon\in\R^n$. 
If $\EL$ is 
positively $\alpha$-homogeneous for some $\alpha\in\R$,
then $\lambda + \inner{\Upsilon,\bz}=\alpha \, \widetilde{\EL}(\g).$
\end{corollary}
\begin{proof}Again we may focus on $ \ML_{\bz}=\NL^{1+s}_{\bz} $.
We can use \cref{lem:decomposition} for an arbitrary tangent vector
$\nu\in T_\g\varOmega^{1+s}_\bz$ to obtain \cref{eq:decomposition}
with a function $\varrho\in H^{1+s}(\R/\Z)$ with $\varrho(0)=\varrho(1)=0$
and tangent vector $h\in T_\g\ML_{\bz}$. Constructing a family of
admissible parameter transformations as in the previous proof we obtain
$\D\EL_\g(\nu)=0$. Observing that we can represent 
the smooth submanifold $\varOmega_\bz^{1+s}$ as
preimage as $\varOmega_\bz^{1+s}=(\LL\times P_0)^{-1}(1,\bz)$,
where $P_0$ is the point evaluation defined in \cref{eq:point-evaluation},
we can apply the
Lagrange multiplier rule
\cite[Corollary 3.5.29]{abraham-etal_1988}
to obtain some number $\lambda\in\R$ and a vector $\Upsilon\in\R^n$ such
that $\g$ is a critical point of the functional $\EL-\lambda\LL -\langle
\Upsilon,P_0(\cdot)\rangle$. 
For the relation between $\lambda$ and $\Upsilon$ we compute similarly
as in the previous proof $ \lambda + \inner{\Upsilon,\bz}
	 =
	\lambda \, \LL(\g) + \inner{\Upsilon,P_0(\g)}
	=
	\lambda \D\LL_\g(\g) + \inner{ \Upsilon,(\D P_0)_\g(\g) }
	=
	\D\EL_\g(\g)
	= 
	\alpha \, \widetilde{\EL}(\g). $
\end{proof}

If we assume  
that the energy $\EL$ is also invariant under translation, 
we do not have to deal with the  additional
Lagrange parameter $\Upsilon\in\R^n$.

\begin{lemma}\label{cor:critical-points_wo_fixed_point}
Let $ \ML=\{\NL^{1+s},\AL^{1+s}\} $ and $ \ML_{\bz}=\{\eta\in \ML:\eta(0)=\bz\} $. If the energy $\EL\in C^1(\OL)$ is invariant under translations, then 
a critical point $\gamma \in \ML_\bz$ of $\EL|_{\ML_\bz}$ is also a 
critical point of $\EL|_{\ML}$.
\end{lemma}
\begin{proof}
	Since the energy is invariant under translations we have 
\[
	\textstyle
	\D\EL_\g p
	=
	\frac{\partial}{\partial\varepsilon}
	\EL(\gamma+\varepsilon p)
	\big|_{\varepsilon=0}
	=
	0\quad\Foa p\in\R^n
	.
\]
In particular, this implies
\[
	\textstyle
	0=\D\EL_\g h(0)
	=
	\D\EL_\g h - \D\EL_\g (h-h(0))
	=
	\D\EL_\g h
	\quad
	\Foa
	h\in T_\g\ML
	,
\]
since $h-h(0)\in T_\g\ML_\bz$;  see \cref{eq:tangent-space-AL} and
\cref{eq:tangent-space-ALz}.
\end{proof}
