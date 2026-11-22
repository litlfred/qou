---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.97
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
An easy way to produce a knot is to tie a piece of string and glue the ends together. This motivates the mathematical definition of a knot as a continuous embedding of a circle into three-dimensional Euclidean space. Depending on the initial knotting, different knot types arise. We say that two knots are of the same knot class if there exists an ambient isotopy \cite[p.~4f.]{Cromwell:2004} that deforms one knot to the other avoiding any sort of self-intersections or ``cutting and glueing'' phenomena. 
In the following we aim to investigate the regularity of optimal shapes for knots within their knot classes. 

Lead by the question of determining optimal representatives for given polygonal knot classes, Fukuhara \cite{Fukuhara:1988:EnergyKnot} introduced the idea to apply some sort of self-repelling potentials to given knots and follow their gradient flow towards the local minimizer. Based on that concept, O'Hara later established the notion of knot energies by defining them as real-valued functionals on the space of knots that are bounded from below and self-repulsive, i.e.~the energy blows up on a sequence of knots that converges to a curve with self-intersections \cite{OHara:2003:EnergyKnotsConformGeom}.

O'Hara was also the first to suggest such a potential knot energy for actual knots \cite{OHara:1991:EnergyKnot}, motivated from the electrostatic potential energy, in particular the self-avoidance effects described by Coulomb's law. Later, this energy was named Möbius energy due to its invariance with respect to Möbius transformations shown by Freedman, He and Wang \cite{Freedmanetal:1994:MoebiusEnergy}. 

Motivated by applications to molecular biology, Gonzalez and Maddocks elaborated a completely different approach to define knot energies in search of a new notion for thickness of knots \cite{GonzalesMaddocks:1999:GlobalCurvature}.
For any continuous, closed, and rectifiable curve $\gamma:\R/\Z \rightarrow \R^3$, where $\R /\Z \cong S^1$ denotes the circle of length 1, they characterized the thickness of  $\gamma$  by
\begin{align*}
\Delta (\gamma) = \inf_{x,y,z\in \gamma } R(x,y,z) ,
\end{align*}
where $R(x,y,z)$ stands for unique circumcircle radius of three points $x,y,z\in \R^n$ given by 
\begin{align*}
R(x,y,z) = \frac{|y-z|\, |y-x| \, |z-x|}{2 |(y-x)\wedge (z-x)|} = \frac{|y-z|}{2 \sin \measuredangle (y-x,z-x)}.
\end{align*}
Observe that $\Delta(\gamma) = 0$ if $\gamma$ intersects itself. Therefore, the quotient  $\mathcal{L}(\gamma) / \Delta(\gamma)$ of length $\mathcal{L}(\gamma)$ over thickness $\Delta(\gamma)$ called \emph{ropelength} serves as a starting point for new self-repelling potential energies.
We remark that thickness is related to the
local radius of curvature since the circumcircle of three points $x,y,z$ on a sufficiently regular curve $\gamma$ converges to the osculating circle at $x$ for $y$ and $z$ converging to $ x$ on $\gamma$. The radius of the osculating circle at $x$ on $\gamma$  is the inverse of the local curvature. 

The ropelength imposes technical challenges as it consists of operators that are hard to differentiate. These drawbacks can be softened as suggested in \cite{GonzalesMaddocks:1999:GlobalCurvature} by exchanging point-wise maximization with integration, which leads to various \emph{integral Menger\footnote{Named after the Austrian-American mathematician Karl Menger (1902-1985) who used the radius of circumscribed circles on a curve to generalize the concept of curvature to metric spaces \cite{Menger:1930:UntersuchungenUeberAllgemeineMetrik}} curvature energies}
such as
\begin{align}\label{def:intMengcurv}
\mathcal{M}^{p}(\gamma) =   \iiint_{(\R/\Z)^3} \frac{|\gamma'(r)| \, |\gamma'(s)| \, |\gamma'(t)|}{R(\gamma(r),\gamma(s), \gamma(t))^p} \d r \d s\d t.
\end{align}
for any $p>0$. Note that for curves parametrized by arc-length $\lim_{p\rightarrow \infty} \mathcal{M}_p^{1/p} (\gamma) = \frac{1}{\Delta(\gamma)}$. Other variants between ropelength and $\mathcal M^p$ can be found in \cite{GonzalesMaddocks:1999:GlobalCurvature}.

For $p>3$, these functionals are indeed knot energies according to O'Hara's definition, as Strzelecki, Szumańska and von der Mosel showed in \cite{StrzeleckiSzumanskavonderMosel:2013:KnotEnergiesInvolvMengCurv}. Furthermore, they proved a geometric Morrey-Sobolev imbedding in three dimensions, in particular that finite energy of an arc-length parametrized curve implies $C^{1,1-\frac 3p}$-regularity and its image is $C^1$-diffeomorphic to the circle \cite{StrzeleckiSzumanskavonderMosel:2010:RegularizingandselfavoidanceeffectsofintegralMengercurvature}. Blatt completed the characterization of energy spaces in \cite{Blatt:2013:NoteMenger}. Generalizations of the integral Menger curvature to higher-dimensional objects can be found for example in \cite{StrzeleckivonderMosel:2009:IntegralMengercurvatureforsurfaces,BlattKolasinski:2012:SharpboundednessandregularizingeffectsoftheintegralMengercurvatureforsubmanifolds, Kolasinski:2014:GeometricSobolevlikeembeddingusinghighdimensionalMengerlikecurvature}.
For further information on the integral Menger curvature energies  we refer the reader for example to the survey paper \cite{StrzekeckivonderMosel:2013:MengerSurvey}.
 
In order to tackle the main question of the present paper, the regularity of optimal shapes for knots, we first need to choose a suitable knot energy and then conduct regularity studies on its stationary points. 
Now if we chose for this purpose the integral Menger curvature energies $\mathcal{M}^p$, $p>3$, we would arrive at nonlinear, non-local and degenerate Euler-Lagrange operators. A formula for the first variation can be found in \cite{Hermes:2012:Menger} and for its second and third variation in \cite{Knappmann:2020:Menger}. Hence, to produce non-degenerate energies from the integral Menger curvature energies given in \eqref{def:intMengcurv}, Blatt and Reiter \cite{BlattReiter:2015:Menger} suggested to generalize $\mathcal{M}^p$ to

\begin{align}\label{def:GenIntMengCurv}
\textnormal{intM}^{(p,q)}(\gamma) =   \iiint_{(\R/\Z)^3} \frac{|\gamma'(u_1)| \, |\gamma'(u_2)| \, |\gamma'(u_3)|}{R^{(p,q)}(\gamma(u_1),\gamma(u_2), \gamma(u_3))} \d u_1 \d u_2 \d u_3, 
\end{align}
where they decoupled the circumcircle radius to
\begin{align*}
R^{(p,q)}(x,y,z) = \frac{(|y-z|\, |y-x| \, |z-x|)^p}{|(y-x)\wedge (z-x)|^q} = \frac{|y-z|^p |y-x|^{p-q} |z-x|^{p-q}}{ \sin \measuredangle (y-x,z-x)^q}
\end{align*} 
for any $p,q>0$. Observe that $\mathcal{M}^{p}(\gamma) = 2^p \textnormal{intM}^{(p,p)}(\gamma) $. According to \cite{BlattReiter:2015:Menger}, these energies are well-defined knot energies for $p\geq \tfrac 23 q + 1$ and give finite energy values on closed curves for $p< q + \tfrac 23$.  Moreover, minimizers exist within every knot class for $p\in (\tfrac 23 q +1,q+\tfrac 23)$ and $q>1$. 

For  the particular case $q=2$ and therefore $p\in (\tfrac 73, \tfrac 83)$, the generalized integral Menger curvature energies in \eqref{def:GenIntMengCurv} indeed lead to non-degenerate Euler-Lagrange equations, for which Blatt and Reiter proved the following regularity result by a combination of potential estimates and Sobolev-embeddings.


\begin{theorem}\label{thm:smooth}\cite[Theorem~4]{BlattReiter:2015:Menger}
	For $p\in (\tfrac 73, \tfrac 83)$, let $\gamma :\R/\Z\rightarrow \R^n$ be a simple curve in $W^{\frac 32 p -2,2}(\R/\Z,\R^n)$ parametrized by arc-length. 
	If $\gamma$ is a stationary point of the generalized integral Menger curvature  $\Mpz$ 
	with respect to fixed length,
	then $\gamma\in C^\infty(\R/\Z,\R^n)$. 
\end{theorem}

Furthermore, Blatt and Reiter characterized $C^1$-curves of finite generalized integral Menger curvature energy by curves in the fractional Sobolev space $W^{\frac {3p-2}{q} -1,q}(\R /\Z,\R^n)$ \cite[Theorem~1]{BlattReiter:2015:Menger}.
This result, combined with \thref{thm:smooth}, raises the question whether stationary points of finite generalized integral Menger curvature energies are not only smooth but also analytic. 

For the Möbius energy the statement was elaborated by \cite{BlattVorderobermeier:2019:CriticalMoebius} based on the corresponding smoothness result established by \cite{BlattReiterSchikorra:2016:CriticalPointsOfMoebiusEnergyAreSmooth}.  The same holds for a non-degenerate range of O'Hara's energies as shown in \cite{Vorderobermeier:2019:CriticalOHara} based on \cite{BlattReiter:2013:StationaryPointsOfOHarasKnotEnergies}. Hence it seems reasonable that it is possible to transfer the techniques to the non-degenerate range of energies $\Mpz$ for $p\in(\tfrac 73,\tfrac 83)$.


The main method used in these papers to show analyticity is based on the method of majorants, motivated by the proof of Cauchy-Kovalevsky's theorem \cite{Kovalevskaya:1875:ZurTheoriederpartiellenDifferentialgleichungen}, see also \cite[pp.~17--33]{Cauchy:1882:OEuvrescompletesdAugustinCauchy}. For applying this technique, it is necessary to establish a recursive estimate for derivatives of critical curves.
It turns out that in such estimates, there appears 
a fractional derivative of the product of two functions, which subsequently leads to a fractional Leibniz rule. Unfortunately, in contrast to the bilinear Hilbert transform in \cite{BlattVorderobermeier:2019:CriticalMoebius} and fractional Leibniz rule in \cite{Vorderobermeier:2019:CriticalOHara}, in our case this recursive estimate does not produce a sufficient difference in the order of differentiability, which is why we repeat it to obtain a difference of order $1$. 
This repetition seems to lead to Gevrey regularity of order $2$ for critical curves, which is weaker than analyticity, cf. \cite[Definiton 4.1.19]{KrantzParks:2002:Aprimerofrealanalyticfunctions} or \cite[Chapter~1.4]{Rodino:1993:LinearPartialDiffOperatorInGevreySpaces},
but we are able to confirm the analyticity in the affirmative:

\begin{theorem}\label{thm:main}
	For $p\in (\tfrac 73, \tfrac 83)$, let $\gamma :\R/\Z\rightarrow \R^n$ be a simple curve in $C^\infty(\R/\Z,\R^n)$ parametrized by arc-length. 
	If $\gamma$ is a critical point of the generalized integral Menger curvature  $\Mpz$ 
	with respect to fixed length,
	then the curve $\gamma$ is analytic. 
\end{theorem}

A closer look at the proof of the main theorem reveals that smoothness of $\gamma$ is actually not needed. It suffices to assume that $\norm[H^{\frac 5 2}]{\gamma^{(i)}}$ is finite for $i \in \set{0,1,2}$, i.e. $\gamma \in H^{4 + \frac 1 2}(\R/\Z,\R^n)$. All additional regularity is obtained by an inductive argument.

However, by the characterization of the energy spaces in \cite[Theorem~1]{BlattReiter:2015:Menger} and the regularity result \thref{thm:smooth}, finite energy $\Mpz$ of a critical point implies its smoothness already. We conclude:

\begin{corollary}\label{cor:main}
	Let  $\gamma :\R/\Z\rightarrow \R^n$ be a simple curve in $C^1(\R/\Z,\R^n)$ parametrized by arc-length  with $\Mpz (\gamma) < \infty$ for $p\in(\tfrac 73, \tfrac 83)$.
	If $\gamma$ is a critical point of $\Mpz$ with respect to fixed length, then the curve $\gamma$ is analytic.
\end{corollary}

One should be able to drop the $C^1$-assumption in the previous result by obtaining sufficient initial regularity via techniques that proved to be successful in showing a geometric Morrey-Sobolev imbedding for $\mathcal{M}^p$ with $p>3$, cf.~\cite[Theorem~1.2]{StrzeleckiSzumanskavonderMosel:2010:RegularizingandselfavoidanceeffectsofintegralMengercurvature}.

Further analyticity and Gevrey regularity results in the context of non-local differential equations can be found for example in \cite{DallAcquaEtAl:2012,DallAcquaEtAl:2014,AlbaneseEtAl:2015:GevreyRegularityForIntDiffOp,Blatt:2020:AnalyticityIntegroDiffOp,Blatt:2020:AnalyticityNonlinerEllipticPDE}.


\subsection{Exposé of the present work}
As stated above, the central idea of our proof is the same as in the one for the Cauchy-Kovalevsky theorem and goes as follows.
A curve $\gamma \in C^\infty(\R/\Z,\R^n)$ is analytic if and only if we have constants $C>0$ and $r>0$ such that for all $l \in \N_0$
\[
	 \norm[L^\infty]{\gamma^{(l)}} \le C \frac {l!} {r^l}.
\]
Suppose we had a recursive estimate
\[
	\norm[L^\infty]{\gamma^{(l+1)}} \le \Phi(l;\norm[L^\infty]{\gamma},\ldots,\norm[L^\infty]{\gamma^{(l)}})
\]
and an analytic function $c:(-\epsilon, \epsilon) \to \R$ with
\[
	c^{(l+1)}(0) = \Phi(l;c(0),\ldots,c^{(l)}(0)) \text{ and } c(0) \ge \norm[L^\infty]{\gamma}.
\]
Then, by induction,
\[
	\begin{split}
		0 \le \norm[L^\infty]{\gamma^{(l+1)}} \le \Phi(l+1;c(0),\ldots,c^{(l)}(0)) = c^{(l+1)}(0) \le C \frac {(l+1)!} {r^{l+1}}
	\end{split}
\]
for all $l \in \N$ and so, $\gamma$ is analytic.

The largest part is devoted to obtaining the required recursive estimate.
In Section \ref{sec:Decomposition}, we review a decomposition of the first variation of $\Mpz$ given in \cite[Section~4]{BlattReiter:2015:Menger} into a highest- and lower-order terms called $\Qpt$ and $\Rpt$.
In a critical point, $\Qpt$ is equal to $-\Rpt$ and we may use the regularity gap between those to establish the recursive estimate.
To that end, Section \ref{sec:EstimateMainTerm} yields an estimate of $\partial^{l+3} \gamma$ by $\partial^l\Qpt(\gamma)$.
In Section \ref{sec:RemainderTermNonCritical} we bound $\partial^l \Rpt(\gamma)$ by $\partial^{l+2} \gamma$ via a fractional Leibniz rule.
Looking at the norms involved, it turns out that these estimates combined only lead to a regularity gain strictly between $\frac 1 2$ and $1$ which is not enough for the recursive estimate, so in Subsection \ref{subsec:RecursiveEstimate}, we iterate the above once more using the fact that $\gamma$ is a critical point.
The remainder of Section \ref{sec:MainProof} is dedicated to finding the analytic majorant $c$ which fulfils the same recursive estimate with equality.
Finally, Section \ref{sec:Consequences} discusses a few simple consequences of the analyticity of critical points, not only for $\Mpz$, in geometric knot theory.

We expect that our approach extends to functionals whose first variation admits a decomposition with properties similar to those of $\Qpt$ and $\Rpt$.
A probably valid generalization would be to assume only an arbitrarily small gain in regularity, see page \pageref{rem:smallerRegularityGain}.




\subsection{Notation}\label{subsec:Notation}
In the following we give a short introduction to the fractional Sobolev spaces we are using in this paper. First, we present a continuation of the usual periodic Sobolev spaces of integer order $W^{k,p}(\R/\Z, \R^n)$ to Sobolev–Slobodeckij spaces $W^{k+s,p}(\R/\Z, \R^n)$ for $0<s <1$. The latter are defined by
\[
	W^{k+s,p}(\R/\Z, \R^n) := \{ f\in W^{k,p}(\R/\Z, \R^n) \ | \ [f^{(k)}]_{W^{s,p}(\R/\Z, \R^n)} < \infty \}
\]
equipped with the norm 
\[
	\|f\|_{W^{k+s,p}(\R/\Z, \R^n)} := \|f\|_W^{k,p}(\R/\Z, \R^n) + [f^{(k)}]_{W^{s,p}(\R/\Z, \R^n)},
\]
where 
\[
	[f^{(k)}]_{W^{s,p}(\R/\Z, \R^n)} := \Big(\int_{\R/\Z} \int_{-1/2}^{1/2} \frac{|f^{(k)}(x) - f^{(k)}(y)|^p}{|x-y|^{1+ps}} \d x \d y \Big)^{\frac 1p}
\]
is the so-called Gagliardo seminorm of $k$-th derivative of $f$. 

Second, we consider Bessel potential spaces of order $s \geq 0$ on the circle $\R/\Z$ that are given by 
\begin{align*}
H^s(\R/\Z, \C^n) := \{f\in L^2 (\R/\Z, \C^n) \ | \ \| f \|_{H^s}:= \| f \|_{H^s(\R/\Z,\C^n)} := \sqrt{(f,f)_{H^s}} < \infty  \},
\end{align*}
equipped with the inner product  
\begin{align*}
(f,g)_{H^s} := (f,g)_{H^s(\R/\Z,\C^n)} := \sum_{k\in\Z} (1+k^2)^s \langle \widehat{f}(k), \widehat{g}(k) \rangle_{\C^n}.
\end{align*}
Here, $\hat f(k) = \int_0^1 e^{-2 \pi i k x} f(x) \d x$ is the $k$-th Fourier coefficient of $f$.
For any integer $k\geq 0$, the introduced space $H^k$ coincides with the classical Sobolev space $W^{k,2}$  and their norms $\|\cdot\|_{H^k}$ and $\|f\|_{W^{k,2}}:= (\sum_{\nu=0}^{k} \|f^{(\nu)}\|^2_{L^2})^{\frac{1}{2}}$ are equivalent (cf.~\cite[Lem.~1.2]{Reiter:2012:RepulsiveKnotEnergies} or \cite[7.62]{AdamsFournier:2003:SobolevSpaces}).
Moreover, Bessel potential spaces coincide with Sobolev–Slobodeckij spaces in the case of $p=2$, in particular, they have equivalent norms
as stated in \cite[Proposition~3.4]{DiNezzaetal:2012:HitchhikersGuide} for spaces on the domain $\R^d$. The proof can be modified to fit our situation.
It can be shown that $H^s(\R/\Z,\R^n)\subseteq H^t(\R/ \Z,\R^n)$ for any $0 \leq t<s$ (cf.~\cite[Chapter~4,~Proposition~3.4]{Taylor:1996:PartialDifferentialEquationsa}) as well as $H^s(\R/\Z,\R^n) \subseteq C(\R/\Z,\R^n)$ for any $s> \frac{1}{2}$ (cf.~\cite[Chapter~4,~Proposition 3.3]{Taylor:1996:PartialDifferentialEquationsa}).

Furthermore, $H^m$ satisfies the Banach algebra property for any $m\geq \frac 12$, i.e. there exists a positive constant $C = C(m)$ such that 
\begin{align}\label{prop:Banachalgebra}
\|fg\|_{H^m} \leq C \|f\|_{H^m} \|g\|_{H^m}
\end{align}
for all $f,g \in H^m(\R/\Z,\R)$  (cf.~\cite[Theor.~4.39]{AdamsFournier:2003:SobolevSpaces}).

For further information on fractional Sobolev spaces, we refer the reader for instance to \cite{AdamsFournier:2003:SobolevSpaces,DiNezzaetal:2012:HitchhikersGuide,RunstSickel:1996:SobolevSpacesOfFractionalOrder, Triebel:2010:TheoryOfFunctionSpaces}.


    


\newcommand{\G}[1][p]{\ensuremath{\mathcal G^{(#1)}}}
\newcommand{\T}[3][\g]{\triangle_{#2,#3}{#1}}
\newcommand{\g}{\gamma}
\newcommand{\dg}{{\gamma}'}
\newcommand{\br}[1]{\ensuremath{\left(#1\right)}}
\newcommand{\Wia}[1][(3p-2)/q-1,q]{\ensuremath{W_{\mathrm{ia}}^{#1}}}
\newcommand{\s}{\ensuremath{\sigma}}
\newcommand{\gp}{g^{p}}
\newcommand{\W}[1][(3p-2)/q-1,q]{\ensuremath{W^{\scriptstyle #1}}}
