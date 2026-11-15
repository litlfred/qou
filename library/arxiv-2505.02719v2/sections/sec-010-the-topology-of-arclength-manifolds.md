---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-010-the-topology-of-arclength-manifolds
section_title: "The topology of arclength manifolds"
section_number: null
pages: 20-23
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.985
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:AL-toplogy}
Fix a point $\bz\in\R^n$ and $s\in \intervaloc{0,1}$. The Hilbert space $ \HL=H^{1+s}\left( \R/\Z,\R^n \right) $ with its inner product\footnote{For $ s=1 $ simply replace the double integral in \cref{eq:fractionalscalarproduct} by $ \left\langle \gamma'',h'' \right\rangle_{L^2}  $.}
\begin{equation}\label{eq:fractionalscalarproduct}
\begin{aligned}
	\inner{f,h}_\HL&\ceq\inner{f,h}_{H^{1+s}}=\inner{f,g}_{L^2}+\inner{f',g'}_{L^2}\\
	&+\int_{\R/\Z}\int_{\R/\Z}\frac{\inner{f(u)-f(v),h(u)-h(v)}}{
	\abs{u-v}_{\R/\Z}^{1+2s}}\d u \d v,\quad 
	\text{for $f,h \in \HL$},
\end{aligned}
\end{equation}

induces a Riemannian metric $g$ on  the arclength submanifolds
\begin{align*}
	&\NL^{1+s}_\bz\subset\NL^{1+s}\subset H^{1+s}_\reg(\R/\Z,\R^n)\subset
H^{1+s}(\R/\Z,\R^n)\,\text{ and }\\
&\AL^{1+s}_\bz\subset\AL^{1+s}\subset H^{1+s}_\injreg(\R/\Z,\R^n)\subset
H^{1+s}(\R/\Z,\R^n).
\end{align*}
More precisely, let $ \ML\in \left\{\NL^{1+s},\NL^{1+s}_{\bz},\AL^{1+s},\AL^{1+s}_{\bz}\right\} $,
$g_\g(f,h)\ceq\langle f,h\rangle_\HL$
for $\g\in\ML$ and $f,h\in T_\g\ML$. So, $\ML$ is a
smooth Riemannian submanifold of the open set $H^{1+s}_\reg(\R/\Z,\R^n) $, or $H^{1+s}_\injreg(\R/\Z,\R^n)$,
respectively; see
\cite[Theorem 3.6]{palais_1966}.
As in the abstract setting of \cref{sec:grad_flows} we have
the path metric (cf.{} \cref{eq:path-metric})
\begin{equation}\label{eq:path-metricALsz}
\dist_{\ML}(\g,\eta)\ceq\inf_{c\in \PS(\g,\eta)}\int_0^1 
\sqrt{g_{c(t)}(\dot{c}(t),\dot{c}(t))}\d t=
\inf_{c\in \PS(\g,\eta)}\int_0^1 \|\dot{c}(t)\|_\HL \d t 
\end{equation}
measuring the distance of
two curves $\g,\eta\in\ML$
in the same connected component of $\ML$, where 
\begin{equation}\label{eq:path-spaceAL}
	\PS(\g,\eta)
	\ceq
	\braces[\big]{
		c\in C^1([0,1],\ML)
		:
		c(0)=\g,c(1)=\eta
	}.
\end{equation}

To investigate the topology of $\ML$ 
more closely,
we look at a mapping that transforms an arbitrary regular closed curve $\g
\in H^{1+s}_\reg(\R/\Z,\R^n)$
into an arclength parametrized curve. The arclength $\psi_\g:
[0,1]\to [0,1]$
(rescaled to the unit interval and then extended to all of $\R$ such that 
$\psi_\g(t+1)=1+\psi_\g(t)$ for all $t\in\R$)  
is given by the strictly monotonic function 
$\psi_\g(t)\ceq\frac1{\LL(\g)}\LL(\g|_{[0,t]})$ for $t\in [0,1]$.
It has a strictly monotonic inverse
$\psi_\g^{-1}:[0,1]
\to [0,1]$.
We prove in \Cref{thm:arclength} 
in \cref{sec:arclength-reparam}
that the reparametrization and rescaling mapping
$\ARC:H^{1+s}_\reg(\R/\Z,\R^n)\to H^{1+s}_\unitspeed(\R/\Z,\R^n)$
given by
\begin{equation}\label{eq:ARC}
	\ARC(\g)
	\ceq
	\sdfrac{1}{\LL(\g)}\,\g\circ \psi_\g^{-1}\quad\Fo \g\in H^{1+s}_\reg(\R/\Z,\R^n)
\end{equation}
is continuous with respect to the $H^{1+s}$-topology for any $s\in (\frac{1}{2},1)$.
For $s=1$ this was proven by Reiter in \cite[Theorem 1.13]{reiter_2009}.
Notice that rescaling and reparametrization does not destroy the injectivity
of a curve so that we have the inclusion
$\ARC(H^{1+s}_\injreg(\R/\Z,\R^n))\subset
\AL^{1+s}$ for all $s\in (\frac{1}{2},1]$.

\begin{theorem}[Arclength manifolds are strong deformation retracts]
\label{thm:strong-deformation-ALs}
The open set\newline $H_\reg^{1+s}(\R/\Z,\R^n)\subset H^{1+s}(\R/\Z,\R^n)$ strongly
deformation retracts onto the submanifolds $\NL^{1+s}$ and 
$\NL^{1+s}_\bz$
for any $s\in (\frac{1}{2},1]$ and $\bz\in\R^n$, whereas $ H^{1+s}_{\injreg}\left( \R/\Z,\R^n \right) $ strongly deformation retracts onto $ \AL^{1+s} $ and $ \AL^{1+s}_{\bz} $. 
\end{theorem}

\begin{proof}
If $\g\in\NL^{1+s}$ then $\LL(\g)=1$ and $\psi_\g(t)=t$ for any $t\in\R$ so
that $\ARC(\g)=\g$ by definition \cref{eq:ARC}. 
Therefore, the mapping $\ARC \colon H^{1+s}_\reg(\R/\Z,\R^n)\to
H^{1+s}_\unitspeed(\R/\Z,\R^n)=\NL^{1+s}$ 
is continuous with $\ARC|_{\NL^{1+s}}=
\Id_{\NL^{1+s}}$, whence a retraction onto $\NL^{1+s}$.
For a given point $\bz\in\R^n$ we simply compose
the map $\ARC$ with the smooth
shift $\tau_\bz:H^{1+s}(\R/\Z,\R^n)\to
H^{1+s}(\R/\Z,\R^n)$ defined as $\tau_\bz(h) \ceq h+\bz-h(0)$
satisfying $\tau_\bz(\g)=\g$ for all $\g\in\AL^{1+s}_\bz$ 
so that we
obtain the retraction $\tau_\bz\circ\ARC:H^{1+s}_\injreg(\R/\Z,\R^n)
\to\NL^{1+s}_\bz$.

Now, we need to construct a homotopy between the identity map on the set
$\OL \ceq H^{1+s}_\reg(\R/\Z,\R^n)$ and the retraction onto $\NL^{1+s}$, and $\NL^{1+s}_\bz$, respectively.
Consider for any curve $\eta\in \OL$
the family of parameter transformations 
\begin{equation}\label{eq:familiy-param}
\phi_\eta(\sigma) \ceq (1-\sigma)\Id_\R+
\sigma\psi_\eta^{-1}:[0,1]\to [0,1]\quad\Fo \sigma\in [0,1],
\end{equation}
where, as before, $\psi_\eta^{-1}$ is the strictly monotonic inverse
of the rescaled arclength $\psi_\eta(t)=\frac1{\LL(\eta)}\LL(\eta|_{[0,t]})$.
As before, we may extend $\phi_\eta$ to all of $\R$ with
$\phi_\eta(t+1)=1+\phi_\eta(t)$ for all $t\in\R$.
Clearly, 
$\phi_\eta(\sigma)(0)=0$ and $\phi_\eta(\sigma)(1)=1$, and $\phi_\eta(\sigma)
(\cdot)$
is strictly
increasing for all $\sigma\in [0,1]$, since
$\phi_{\eta}(\sigma)'(t)=(1-\sigma)+\sigma (\psi_\g^{-1})'(t)>0$ for
any $t\in [0,1]$. We can interpret this family $\phi_\eta(\sigma)$ as 
a mapping $\phi_{\cdot}(\cdot):\OL\times [0,1]\to
H^{1+s}_\reg([0,1])$, which clearly is continuous on
$\OL\times [0,1]$ 
due to \Cref{cor:restriction-inverse-operator} and 
\Cref{lem:parametrization_continuous} in \cref{sec:arclength-reparam}.
Next, we modify the mapping $\ARC$ in \cref{eq:ARC} to obtain
a family of mappings $\CAPARC(\eta,\sigma)$ for $\sigma\in [0,1]$ defined as
\begin{equation}\label{eq:ARC-sigma}
\textstyle
\CAPARC(\eta,\sigma)\ceq\frac1{1+\sigma(\LL(\eta)-1)}\,\eta\circ\phi_\eta(\sigma)
\quad\Fo\eta\in \OL.
\end{equation}
\Cref{composition_continuous} in \cref{sec:arclength-reparam}
implies that the map 
$\CAPARC(\cdot,\cdot):\OL\times [0,1]\to \OL
$ is continuous. With $\phi_\eta(0)(t)=t$ for all $t\in\R$ one has $\CAPARC(\eta,0)=\eta$
for all $\eta\in \OL$, and $\CAPARC(\eta,1)\in\NL^{1+s}$ since $\phi_\eta(1)=
\psi_\eta^{-1}$ so that $\CAPARC(\eta,1)=\ARC(\eta)$ by \cref{eq:ARC}, 
and the original map
$\ARC$ was shown 
to be a retraction onto $\NL^{1+s}$.
For $\g\in\NL^{1+s}$ one has $\LL(\g)=1$ and $\psi_\g^{-1}(t)=t$ whence 
$\phi_\g(\sigma)(t)=t$ for all $t\in\R$ and $\sigma\in [0,1]$, 
and therefore 
$
\CAPARC(\g,\sigma)=\frac1{1+\sigma(1 -1)}\,\g=\g.$
Hence, $\CAPARC(\cdot,\cdot)$ is a strong deformation 
retraction of $\OL$ onto $\NL^{1+s}$.

If we fix a point $\bz\in\R^n$ to treat the arclength submanifold
$\NL^{1+s}_{\bz}$ instead of $\NL^{1+s}$, then we take 
the family of shifts $T_\bz(h,\sigma)\ceq
h+\sigma(\bz-h(0))$ for $h\in\OL$. 
Then the composition
$T_\bz(\CAPARC(\cdot,\sigma),\sigma)$ for $\sigma\in [0,1]$
yields a strong deformation retraction of $\OL$ onto $\NL^{1+s}_\bz$.
Indeed, we have
$T_\bz(h,0)=h$, 
$T_\bz(h,1)=h+\bz-h(0)$ hence $T_\bz(h,1)'=
h'$, and
$T_\bz(h,1)(0)=\bz$ for all $h\in \OL$.
So, $T_\bz(\CAPARC(\eta,0),0)=\CAPARC(\eta,0)=\eta$, and
$T_\bz(\CAPARC(\eta,1),1)=\CAPARC(\eta,1)+\bz-\CAPARC(\eta,1)(0)
\in\NL^{1+s}_\bz$ for every $\eta\in\OL$. In addition,
for $\g\in\NL^{1+s}_\bz$ we have shown above
that $T_\bz(\CAPARC(\g,\sigma),\sigma)=
T_\bz(\g,\sigma),$
which equals $\g$
since $\g(0)=\bz$.

Replacing $ \NL^{1+s} $ and $ H^{1+s}_{\reg} $ by $ \AL^{1+s} $ and $ H^{1+s}_{\injreg} $ respectively, yields the desired statement for the submanifolds of arclength parametrized knots. 
\end{proof}
\begin{remark}\label{rem:topological-justification-AL}
\cref{thm:strong-deformation-ALs} 
justifies restricting knot energies to the submanifold of arclength parametrized
curves topologically: As the knot space $H^{1+s}_\injreg(\R/\Z,\R^n)$ strongly
deformation retracts onto $\AL^{1+s}$ and also onto $\AL^{1+s}_\bz$, all
three topological spaces are homotopy equivalent and hence contain
the same topological information. 
\end{remark}
The last result of this section gives a justification from the perspective of knot theory. 
\begin{theorem}[Connected components are knot classes]
\label{thm:components-knot-classes}
Let $s\in (\frac{1}{2},1]$. If two knots $\g_0$ and $\g_1$ lie in the same
connected component of $\AL^{1+s}$ then they are $C^1$-ambiently isotopic.
If, on the other hand,
two knots $\g_0,\g_1\in\AL^{1+s}$ are $C^1$-isotopic in 
$\R^n$,
then they lie in the same connected component
of $\AL^{1+s}$.
All statements remain 
true if we replace $\AL^{1+s}$ by $\AL^{1+s}_\bz$ for some fixed point
$\bz\in\R^n$.
\end{theorem}
\begin{proof}
Fix $s\in (\frac{1}{2},1]$.
It suffices to treat $\AL \ceq \AL^{1+s}$.
If $\g_0,\g_1\in\AL$ are contained in the same connected component
of the smooth submanifold $\AL\subset\OL\ceq
H^{1+s}_\injreg(\R/\Z,\R^n)$ then there exists a path $c\in  
C^\infty([0,1],\AL)$ such that
$c(0)=\g_0$ and $c(1)=\g_1$; see, e.g., \cite[Lemma 3.1]{palais_1966}.
Set $J(t,\sigma) \ceq c(\sigma)(t)$ for $t\in\R/\Z$ and $\sigma\in [0,1]$, to
find that the curve
$J(\cdot,\sigma)\in\AL$ is a $C^1$-embedding for any $\sigma\in [0,1]$
by means of the Morrey embedding $H^{1+s}(\R/\Z,\R^n)\hookrightarrow
C^1(\R/\Z,\R^n)$; see \cite[Theorem A.2]{knappmann-etal_2023}. 
Moreover, one can show with this embedding 
that $J$ is also of class $C^1(\R/\Z\times [0,1],
\R^n)$ so that $J$ constitutes a $C^1$-isotopy with $J(\cdot,0)=\g_0$ and
$J(\cdot,1)=\g_1$. According to \cite[Theorem 1.2]{blatt_2009a} the two knots
$\g_0$ and $\g_1$ are therefore ambiently isotopic, i.e., in the same knot
class.

Let $J \in C^1(\Circle\times[0,1] ,\AmbSpace)$ be an isotopy satisfying $J(\cdot,0) = \gamma_0$ and $J(\cdot,1) = \gamma_1$. 
We consider the metric space $X \ceq C^1(\Circle,\AmbSpace)$ with the $C^1$-norm.
Define $\varGamma \in C^0([0,1],X)$ by $\varGamma(t) \ceq J(\cdot,t)$.
The set $U \ceq C^1_{\mathrm{ir}}(\Circle,\AmbSpace)$ is open in $X$,
and $\varGamma$ maps into it.
Observe that the distance function
\[
    \dist(\gamma, X \setminus U) \ceq \smash{\inf_{\eta \in X \setminus U} \|\gamma - \eta\|_{C^1}} \quad \text{ for }\gamma\in U
\]
is Lipschitz continuous.
Thus, the function $F \colon \intervalcc{0,1} \to \R$, $F(t) \ceq \dist(\varGamma(t), X \setminus U)$ is continuous. 
The interval $\intervalcc{0,1}$ is compact, so $F$ must have a minimizer $t_0 \in \intervalcc{0,1}$.
Because of $\varGamma(t_0) \in U$ and because $U$ is open, the minimum value must be positive: $2\varepsilon\ceq F(t_0) > 0$. 
Since $C^\infty(\Circle\times[0,1],\AmbSpace)$ is dense in $C^1(\Circle\times[0,1],\AmbSpace)$, there is an  $H \in C^\infty(\Circle\times[0,1],\AmbSpace)$ so that
$
    \norm{J - H}_{C^1(\Circle\times[0,1],\R^n)}
    <
    \varepsilon
$.
For the path $G$ defined by $G(t) \ceq H(t,\cdot)$ this means that
\[
\norm[\big]{ 
		t \mapsto \norm{ \varGamma(t) - G(t) }_{C^1} 
	}_{L^\infty} 
    \leq 
    \norm{J - H}_{C^1([0,1] \times \Circle,\R^n)}
    <
    \varepsilon
	.
\]
By construction, we have for every $t \in [0,1]$ that
\[
    G(t) 
	\in 
	B_\varepsilon(\varGamma(t)) \cap C^2(\Circle,\AmbSpace)
	\subset
	U \cap C^2(\Circle,\AmbSpace) 
    = C^2_{\mathrm{ir}}(\Circle,\AmbSpace)
	.
\]
Since the embedding $C^2(\Circle,\AmbSpace) \hookrightarrow H^{1+s}(\Circle,\AmbSpace)$ is linear and continuous, the path $G$ is an element of
$C^\infty([0,1],H^{1+s}_{\mathrm{ir}}(\Circle,\AmbSpace))$.
Now we define the linear homotopies
\[
    \varGamma_1(t) \ceq (1-t) \, \gamma_0 + t \, G(0)
    \quad \text{and} \quad 
    \varGamma_2(t) \ceq (1-t) \, G(1) + t \, \gamma_1
    ,
    \quad 
    \text{for $t \in [0,1]$}
    .
\]
Notice that $G(0) \in B_\varepsilon(\gamma_0)$, $G(1) \in B_\varepsilon(\gamma_1)$, that these balls contained in $ C^1_{\injreg}(\Circle,\AmbSpace) $ are convex,  and that knot classes are stable under small $ C^1 $-pertubations, see \cite{blatt_2009a}. 
Thus, we have $\varGamma_1, \varGamma_2 \in C^\infty([0,1],H^{1+s}_{\mathrm{ir}}(\Circle,\AmbSpace))$.
Concatenation of the paths $\varGamma_1$, $G$, and $\varGamma_2$ yields a continuous path from $\gamma_0$ to $\gamma_1$ in $H^{1+s}_{\mathrm{ir}}(\Circle,\AmbSpace)$.
Finally, we retract this path to a continuous path in $\mathcal{A}$, by means of \cref{thm:strong-deformation-ALs}.
\end{proof}
