---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-006-7-boundary-concentration-phenomena
section_title: "Boundary concentration phenomena"
section_number: 7
pages: 30-35
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 0.942
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Boundary concentration phenomena}



\subsection{Critical scale orders}\label{sec:Sequences of model spaces}

We first state the following assertion concerning the critical scale order of sequences of hemispheres (cf. Proposition \ref{prop:ball distribution laws}, Subsection 1.1 in \cite{GM}, Corollary 2.22 in \cite{Sh}, Theorem 8.1.1 and Corollary 8.5.7 in \cite{Sh1}):
\begin{thm}\label{thm:sequence of hemisphere}
For $\kappa>0$,
and for every $\eta \in (0,1]$
we have
\begin{equation}\label{eq:sequence of hemisphere}
\lim_{n\to \infty}\OI(B^{n}_{\kappa/n,0};-\eta)= \PI(G_{\kappa,0};1-\eta),
\end{equation}
where $G_{\kappa,0}$ is the half-Gaussian-model-space defined as $(\ref{eq:Gaussian model space})$,
and the right hand side of $(\ref{eq:sequence of hemisphere})$ is the partial inscribed radius of $G_{\kappa,0}$ defined as $(\ref{eq:partial inscribed radius})$.
In particular,
for a sequence $\{\kappa_{n}\}$ of $\kappa_{n}>0$,
the sequence $\{B^{n}_{\kappa_{n},0}\}$ is a boundary concentration family if and only if $n\,\kappa_{n}\to \infty$.
\end{thm}
\begin{proof}
Let us regard the $n$-dimensional standard sphere $M^{n}_{n/\kappa}$ with constant curvature $n/\kappa$ as an mm-space defined as (\ref{eq:normalized metric measure space with boundary}) (see Remark \ref{rem:mm-spaces}).
We observe that
$M^{n}_{n/\kappa}$ is the double of the hemisphere $B^{n}_{\kappa/n,0}$.
Based on Lemma \ref{lem:observable and separation on model} and this geometric observation,
we obtain
\begin{equation*}
\OI(B^{n}_{\kappa/n,0};-\eta)= \DS(B^{n}_{\kappa/n,0};\eta)=\frac{1}{2}\SE(M^{n}_{\kappa/n};\eta/2,\eta/2),
\end{equation*}
where $\SE(M^{n}_{\kappa/n};\eta/2,\eta/2)$ is the $(\eta/2,\eta/2)$-separation distance of $M^{n}_{\kappa/n}$ defined as (\ref{eq:Gromov separation distance}) (see Remark \ref{rem:Gromov separation distance}).
It is well-known that
the right hand side tends to $r>0$ determined by
\begin{equation*}
\frac{1-\eta}{2}=\frac{\int^{r}_{0}\,e^{-\frac{\kappa}{2}\,t^{2}}\,    dt}{\int^{\infty}_{-\infty}\,e^{-\frac{\kappa}{2}\,t^{2}}\,    dt}
\end{equation*}
as $n\to \infty$ (see e.g., Theorem 2.1 and Lemma 2.3 in \cite{Sh}).
We see that $r$ is equal to $\PI(G_{\kappa,0};1-\eta)$,
and hence (\ref{eq:sequence of hemisphere}).

For a metric measure space with boundary $X=(X,d_{X},\mu_{X})$,
\begin{equation}\label{eq:scaling formula}
\OI(cX;-\eta)=c \OI(X;-\eta)
\end{equation}
for every $c>0$,
where we set $cX:=(X,c d_{X},\mu_{X})$ (cf. Proposition 2.19 in \cite{Sh}).
Therefore,
by (\ref{eq:sequence of hemisphere}) and $B^{n}_{\kappa_{n},0}=\sqrt{\kappa\,(n\,\kappa_{n})^{-1}} \,B^{n}_{\kappa/n,0}$,
we arrive at the desired conclusion.
\end{proof}

We next investigate sequences of Euclidean balls.
\begin{thm}\label{thm:sequence of Euclidean ball}
For $\lambda>0$,
and for every $\eta \in (0,1]$
we have
\begin{equation}\label{eq:sequence of Euclidean ball}
\lim_{n\to \infty}\OI(B^{n}_{0,\lambda/n};-\eta)= \PI(E_{\lambda};1-\eta)=\frac{1}{\lambda}\log \frac{1}{\eta},
\end{equation}
where $E_{\lambda}$ is the exponential-model-space defined as $(\ref{eq:exponential model space})$.
In particular,
for a sequence $\{\lambda_{n}\}$ of $\lambda_{n}>0$,
the sequence $\{B^{n}_{0,\lambda_{n}}\}$ is a boundary concentration family if and only if $n\,\lambda_{n}\to \infty$.
\end{thm}
\begin{proof}
By $s_{0,\lambda/n}(t)=1-\lambda\,n^{-1}\,t$,
we have $v_{n,0,\lambda/n}(r)=(1-\lambda\,n^{-1}\,r)^{n}$,
where $v_{n,0,\lambda}$ is defined as (\ref{eq:ball function}).
Lemma \ref{lem:observable and separation on model} implies that
\begin{equation*}
\OI(B^{n}_{0,\lambda/n};-\eta)=\frac{n}{\lambda}\,(1-\eta^{\frac{1}{n}})\to \frac{1}{\lambda}\log \frac{1}{\eta}
\end{equation*}
as $n\to \infty$.
On the other hand,
$\PI(E_{\lambda};1-\eta)$ is equal to a positive number $r>0$ determined as $1-\eta=\int^{r}_{0}\,\lambda\,e^{-\lambda\,t}\,dt$;
in particular,
$\PI(E_{\lambda};1-\eta)=\lambda^{-1} \log \eta^{-1}$.
This proves the equalities (\ref{eq:sequence of Euclidean ball}).
Due to $B^{n}_{0,\lambda_{n}}=\lambda\,(n\,\lambda_{n})^{-1} \,B^{n}_{0,\lambda/n}$ and (\ref{eq:scaling formula}),
we complete the proof.
\end{proof}

We also provide the following result for warped-product-model-spaces:
\begin{thm}\label{thm:warped product model Levy family}
For $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
and for every $\eta \in (0,1]$
\begin{equation*}\label{eq:warped product Levy family}
\lim_{n\to \infty}\OI(M^{n}_{\kappa/n^{2},\lambda/n};-\eta)= \PI(E_{\lambda};1-\eta)=\frac{1}{\lambda}\log \frac{1}{\eta}.
\end{equation*}
Moreover,
for a sequence $\{\kappa_{n}\}$ of $\kappa_{n}<0$,
and for a sequence $\{\lambda_{n}\}$ of $\lambda_{n}=\sqrt{\vert \kappa_{n} \vert}$,
the sequence $\{M^{n}_{\kappa_{n},\lambda_{n}}\}$ is a boundary concentration family if and only if we have $n\,\lambda_{n}\to \infty$ as $n\to \infty$.
\end{thm}
\begin{proof}
Lemma \ref{lem:observable and separation on model} yields
\begin{equation*}
\OI(M^{n}_{\kappa/n^{2},\lambda/n};-\eta)=\frac{n}{(n-1)\lambda}\,\log \frac{1}{\eta} \to \frac{1}{\lambda}\log \frac{1}{\eta}
\end{equation*}
as $n\to \infty$.
The second equality of (\ref{eq:sequence of Euclidean ball}) tells us the desired equalities.
The later assertion also immediately follows from Lemma \ref{lem:observable and separation on model}
\end{proof}

Let us give a proof of Corollary \ref{cor:ball model Levy family}.
\begin{proof}[Proof of Corollary \ref{cor:ball model Levy family}]
Let $\kappa$ and $\lambda$ satisfy the convex-ball-condition.
We will prove that
$\{\ball\}$ is a boundary concentration family.

We first consider the case of $\kappa>0$.
In this case,
we have $\lambda \geq 0$.
Due to Theorem \ref{thm:main theorem},
we have $\OI(\ball;-\eta) \leq \OI(B^{n}_{\kappa,0};-\eta)$.
Furthermore,
Theorem \ref{thm:sequence of hemisphere} tells us that
$\{B^{n}_{\kappa,0}\}$ is a boundary concentration family.
Hence,
$\{\ball\}$ is also a boundary concentration family.

When $\kappa=0$,
the desired statement follows from Theorem \ref{thm:sequence of Euclidean ball}.

In the case of $\kappa<0$,
it holds that $\lambda>\sqrt{\vert \kappa \vert}$.
In virtue of Theorem \ref{thm:main theorem} and Lemma \ref{lem:observable and separation on model},
we obtain
\begin{equation*}
\OI(\ball;-\eta) \leq \OI\bigl(M^{n}_{\kappa,\sqrt{ \vert \kappa \vert}};-\eta\bigl) = \frac{1}{(n-1)\sqrt{ \vert \kappa \vert}}\,\log \frac{1}{\eta};
\end{equation*}
in particular,
$\OI(\ball;-\eta)\to 0$ as $n\to \infty$.
Thus,
we complete the proof of Corollary \ref{cor:ball model Levy family}.
\end{proof}



\subsection{Positive dimensional cases}\label{sec:Positive dimensional cases}
In this subsection,
we summarize corollaries of Theorem \ref{thm:weighted main theorem}.
Hereafter,
let $\{(M_{n},f_{n})\}$ be a sequence of metric measure spaces with compact boundary defined as $(\ref{eq:weighted Riemannian manifold})$.
We denote by $\dim M_{n}$ the dimension of $M_{n}$.
Theorem \ref{thm:weighted main theorem} together with Theorems \ref{thm:sequence of hemisphere}, \ref{thm:sequence of Euclidean ball}, \ref{thm:warped product model Levy family} and Corollary \ref{cor:ball model Levy family} leads us to the following:
\begin{cor}\label{cor:hemisphere corollary}
Let $\{N_{n}\}$ be a sequence of integers with $N_{n} \geq \dim M_{n}$,
and let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}>0$.
Assume $\ric^{N_{n}}_{f_{n},\partial M_{n}^{\perp}}\geq (N_{n}-1)\kappa_{n}$ and $H_{f_{n},\bm_{n}}\geq 0$ for each $n$.
If $N_{n}\,\kappa_{n}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}
Let $\{N_{n}\}$ be a sequence of integers with $N_{n} \geq \dim M_{n}$,
and let $\{\lambda_{n}\}$ be a sequence of $\lambda_{n}>0$.
We assume $\ric^{N_{n}}_{f_{n},\partial M_{n}^{\perp}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq (N_{n}-1)\lambda_{n}$ for each $n$.
If $N_{n}\,\lambda_{n}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}\label{cor:finite dimensional corollary}
Let $\{N_{n}\}$ be a sequence of integers with $N_{n} \geq \dim M_{n}$,
and let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}<0$.
For each $n$,
we put $\lambda_{n}:=\sqrt{\vert \kappa_{n} \vert}$.
We assume $\ric^{N_{n}}_{f_{n},\partial M_{n}^{\perp}}\geq (N_{n}-1)\kappa_{n}$ and $H_{f_{n},\bm_{n}}\geq (N_{n}-1)\lambda_{n}$.
If $N_{n}\,\lambda_{n}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}
Let $\{N_{n}\}$ be a sequence of integers with $N_{n} \geq \dim M_{n}$.
Assume $\ric^{N_{n}}_{f_{n},\partial M_{n}^{\perp}}\geq (N_{n}-1)\kappa$ and $H_{f_{n},\bm_{n}}\geq (N_{n}-1)\lambda$ for each $n$.
We also assume that
one of the following holds:
\begin{enumerate}
\item $\kappa$ and $\lambda$ satisfy the convex-ball-condition;
\item $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
\end{enumerate}
If $N_{n}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

Now,
we will present a concrete example concerning these corollaries, especially Corollary \ref{cor:finite dimensional corollary}:
\begin{ex}\label{ex:finite dimensional example}
Let $\{N_{n}\}$ be a sequence of integers with $N_{n} \geq n$,
and let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}<0$.
For each $n$,
put $\lambda_{n}:=\sqrt{\vert \kappa_{n} \vert}$.
Define a sequence $\{(\widetilde{M}_{n},\widetilde{f}_{n})\}$ of metric measure spaces with boundary as
\begin{align*}
\widetilde{M}_{n}&:=([0,\infty) \times \mathbb{S}^{n-1},dt^{2}+e^{-2\lambda_{n} t}\,ds_{n-1}^{2}),\\
\widetilde{f}_{n}&:=(N_{n}-n)\,\lambda_{n}\,\rho_{\partial \widetilde{M}_{n}}-\log\,\bigl( (N_{n}-1)\,\lambda_{n}\, (\vol_{\mathbb{S}^{n-1}} (\mathbb{S}^{n-1}))^{-1}\bigl).
\end{align*}
Then the sequence $\{(\widetilde{M}_{n},\widetilde{f}_{n})\}$ is a boundary concentration family if and only if we have $N_{n}\,\lambda_{n} \to \infty$.

Computing the curvatures of $\widetilde{M}_{n}$,
we see the following (cf. calculations in the proof of Lemma 3.1 in \cite{S1}):
For all $z\in \partial \widetilde{M}_{n}$ and $t>0$,
\begin{equation*}
\ric^{N_{n}}_{\widetilde{f}_{n}}(\gamma'_{z}(t))=(N_{n}-1)\kappa_{n}, \quad H_{\widetilde{f}_{n},z}=(N_{n}-1)\lambda_{n}.
\end{equation*}
Moreover,
$\theta_{\widetilde{f}_{n}}(t,z)=e^{-\widetilde{f}_{n}(z)}\,s^{N_{n}-1}_{\kappa_{n},\lambda_{n}}(t)$,
where $\theta_{\widetilde{f}_{n}}(t,z)$ is defined as (\ref{eq:volume element}).
This yields $m_{\widetilde{M}_{n},\widetilde{f}_{n}}(\widetilde{M}_{n})=1$.
Furthermore,
$\DS(  (\widetilde{M}_{n},\widetilde{f}_{n});\eta )$ is equal to $r_{n}>0$ determined by
\begin{equation*}
\vol_{\mathbb{S}^{n-1}} (\mathbb{S}^{n-1})\,\int^{\infty}_{r_{n}}\,\theta_{\widetilde{f}_{n}}(t,z)\,dt=\eta;
\end{equation*}
in particular,
from Proposition \ref{prop:Kazukawa}
we deduce
\begin{equation*}
\OI((\widetilde{M}_{n},\widetilde{f}_{n});-\eta)=\DS(  (\widetilde{M}_{n},\widetilde{f}_{n});\eta )=\frac{1}{(N_{n}-1)\lambda_{n}}\,\log\frac{1}{\eta}.
\end{equation*}
We conclude the desired statement.
\end{ex}



\subsection{One dimensional cases}\label{sec:One dimensional cases}
We next summarize corollaries of Theorem \ref{thm:twisted weighted main theorem}.
Throughout this subsection,
we always assume $\dim M_{n}=n$.
Similarly to the above subsection,
one can verify the following assertions by using Theorem \ref{thm:twisted weighted main theorem}:

\begin{cor}
Let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}>0$,
and let $\{\delta_{n}\}$ be a sequence of $\delta_{n}\in \mathbb{R}$.
Let us assume $\ric^{1}_{f_{n},\partial M_{n}^{\perp}}\geq (n-1)\kappa_{n}\,e^{\frac{-4f_{n}}{n-1}}$ and $H_{f_{n},\bm_{n}}\geq 0$ for each $n$.
Suppose additionally that
$f_{n}\leq (n-1)\delta_{n}$.
If $n\,\kappa_{n}\,e^{-4\delta_{n}}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}
Let $\{\lambda_{n}\}$ be a sequence of $\lambda_{n}>0$,
and let $\{\delta_{n}\}$ be a sequence of $\delta_{n}\in \mathbb{R}$.
Let us assume $\ric^{1}_{f_{n},\partial M_{n}^{\perp}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq (n-1)\lambda_{n}\,e^{\frac{-2f_{n}}{n-1}}$ for each $n$.
Suppose additionally that
$f_{n}\leq (n-1)\delta_{n}$.
If $n\,\lambda_{n}\,e^{-2\delta_{n}}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}\label{cor:one dimensional corollary}
Let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}<0$,
and let $\{\delta_{n}\}$ be a sequence of $\delta_{n}\in \mathbb{R}$.
For each $n$,
put $\lambda_{n}:=\sqrt{\vert \kappa_{n} \vert}$.
Assume $\ric^{1}_{f_{n},\partial M_{n}^{\perp}}\geq (n-1)\kappa_{n}\,e^{\frac{-4f_{n}}{n-1}}$ and $H_{f_{n},\bm_{n}}\geq (n-1)\lambda_{n}\,e^{\frac{-2f_{n}}{n-1}}$.
Suppose additionally that
$f_{n}\leq (n-1)\delta_{n}$.
If $n\,\lambda_{n}\,e^{-2\delta_{n}}\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

\begin{cor}
We assume $\ric^{1}_{f_{n},\partial M_{n}^{\perp}}\geq (n-1)\kappa\,e^{\frac{-4f_{n}}{n-1}}$ and $H_{f_{n},\bm_{n}}\geq (n-1)\lambda\,e^{\frac{-2f_{n}}{n-1}}$ for each $n$.
Suppose additionally that
$f_{n}\leq (n-1)\delta$ for some $\delta \in \mathbb{R}$.
We also assume that
one of the following holds:
\begin{enumerate}
\item $\kappa$ and $\lambda$ satisfy the convex-ball-condition;
\item $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
\end{enumerate}
Then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{cor}

Let us construct a concrete example for the above corollaries:
\begin{ex}\label{ex:one dimensional example}
Let $\{\kappa_{n}\}$ be a sequence of $\kappa_{n}<0$,
and let $\{\delta_{n}\}$ be a sequence of $\delta_{n}\in \mathbb{R}$.
For each $n$,
we put $\lambda_{n}:=\sqrt{\vert \kappa_{n} \vert}$.
Let us denote by $(    \mathbb{S}^{n-1}_{\kappa_{n},\lambda_{n},\delta_{n}}, ds^{2}_{n-1,\kappa_{n},\lambda_{n},\delta_{n}})$ the $(n-1)$-dimensional sphere with volume
\begin{equation*}
e^{-C_{n}}  \left(\int^{\infty}_{1}\exp\left(-\frac{(n-1)\,\lambda_{n}\,e^{-2\delta_{n}}}{2}t^{2}\right)dt \right)^{-1},
\end{equation*}
where $C_{n}:=2^{-1}\,(n-1)\,(\lambda_{n}\,e^{-2\delta_{n}}-2\,\delta_{n})$.
We define a sequence $\{(\widetilde{M}_{n},\widetilde{f}_{n})\}$ of metric measure spaces with boundary as
\begin{align*}
\widetilde{M}_{n}&:=\bigl([0,\infty) \times \mathbb{S}^{n-1}_{\kappa_{n},\lambda_{n},\delta_{n}}, \,dt^{2}+\mathcal{H}^{2}_{\kappa_{n},\lambda_{n},\delta_{n}}(t)\,ds^{2}_{n-1,\kappa_{n},\lambda_{n},\delta_{n}}\bigl),\\
\widetilde{f}_{n}&:=-\frac{n-1}{2} \log\, \bigl(\rho_{\partial \widetilde{M}_{n}}+1\bigl)+(n-1)\delta_{n},
\end{align*}
where
\begin{equation*}
\mathcal{H}_{\kappa_{n},\lambda_{n},\delta_{n}}(t):=\frac{1}{\sqrt{t+1}} \,\exp \left(-\frac{\lambda_{n}\,e^{-2\delta_{n}}}{2}\bigl((t+1)^{2}-1\bigl) \right).
\end{equation*}
If $n\,\lambda_{n}\,e^{-2\delta_{n}}\to \infty$,
then $\{(\widetilde{M}_{n},\widetilde{f}_{n})\}$ is a boundary concentration family.

We derive this statement from Corollary \ref{cor:one dimensional corollary}.
We rewrite $\widetilde{M}_{n}$ as
\begin{equation*}
\widetilde{M}_{n}=\bigl([0,\infty) \times \mathbb{S}^{n-1}_{\kappa_{n},\lambda_{n},\delta_{n}},\, dt^{2}+F^{2}_{\kappa_{n},\lambda_{n},z}(t)\,ds^{2}_{n-1,\kappa_{n},\lambda_{n},\delta_{n}}\bigl),
\end{equation*}
where for each $z\in \partial \widetilde{M}_{n}$,
\begin{align*}
s_{\widetilde{f}_{n},z}(t)&:=\int^{t}_{0}\,  e^{\frac{-2\widetilde{f}_{n}(\gamma_{z}(a))}{n-1}}\,da,\\
F_{\kappa_{n},\lambda_{n},z}(t)&:= \exp \left(  \frac{\widetilde{f}_{n}(\gamma_{z}(t))-\widetilde{f}_{n}(z)}{n-1}  \right)\,s_{\kappa_{n},\lambda_{n}}(s_{\widetilde{f}_{n},z}(t)).
\end{align*}
From this expression,
one can compute the curvatures of $\widetilde{M}_{n}$ as follows (cf. calculations in the proof of Lemmas 3.5, 5.2 and 7.1 in \cite{S2}):
For all $z\in \partial \widetilde{M}_{n}$ and $t>0$
we have
\begin{equation*}
\ric^{1}_{\widetilde{f}_{n}}(\gamma'_{z}(t))=(n-1)\kappa_{n}\,e^{\frac{-4\widetilde{f}_{n}(\gamma_{z}(t))}{n-1}},\quad H_{\widetilde{f}_{n},z}=(n-1)\lambda_{n}\,e^{\frac{-2\widetilde{f}_{n}(z)}{n-1}}.
\end{equation*}
Moreover,
$\theta_{\widetilde{f}_{n}}(t,z)=e^{-\widetilde{f}_{n}(z)}\,s^{n-1}_{\kappa_{n},\lambda_{n}}(s_{\widetilde{f}_{n},z}(t))$,
and hence
\begin{equation*}
\theta_{\widetilde{f}_{n}}(t,z)=e^{C_{n}}\,\exp \left(-\frac{(n-1)\,\lambda_{n}\,e^{-2\delta_{n}}}{2}(t+1)^{2}\right);
\end{equation*}
in particular,
we see $m_{\widetilde{M}_{n},\widetilde{f}_{n}}(\widetilde{M}_{n})=1$.
Since $\widetilde{f}_{n}\leq (n-1)\delta_{n}$,
Corollary \ref{cor:one dimensional corollary} leads us to the desired conclusion.
\end{ex}
