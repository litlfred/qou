---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-006-energies-on-submanifolds-of-hilbert-spaces
section_title: "Energies on submanifolds of Hilbert spaces"
section_number: null
pages: 8-12
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:energies-hilbert}
In this section we provide sufficient criteria on the energy and on the underlying
spaces guaranteeing the validity of the Palais--Smale condition (PS). 
Throughout this section we use the following notation:
We let $\HL$ be a Hilbert space and $\BL$ be a Banach space such that there is a compact embedding $\iota_{\BL} \colon \HL \embeds \BL$.
We suppose that $\EL \colon \OL \to \R$ is an energy functional of class $C^1$
on an open subset $\OL \subset \HL$.
Moreover, we suppose that $\ML \subset \OL$ is a $C^1$-submanifold without boundary.
Summarized, we have the following setup:
\begin{enumerate}
	\Item[(E)]\label{condE}
	{\sc (Embedding)}
	$\ML\subset \OL\subset \HL \xhookrightarrow{\iota_\BL} \BL$ and $\iota_\BL$ is compact.
\end{enumerate}
Since $\ML \subset \HL$ is a $C^1$-submanifold, the tangent bundle $T \ML \subset \ML \times \HL$ is splitting, see \cite[Chapter III]{lang_2002}. More precisely, there is a continuous map $\pr^{\ML} \colon \ML \to \BoundedLinOps(\HL)$ such that for each $x \in \ML$ the operator $\pr^{\ML}_x \ceq \pr^{\ML}(x)$ is a continuous linear projector onto $T_x \ML$. Note that we do \emph{not} mean $\pr^{\ML}_x$ to be the orthonormal projector with respect to the inner product on $\HL$.

Our aim is to find sufficient criteria for the \PaSma-condition of $\widetilde{\EL} \ceq \EL|_{\ML}$.
To this end, we make further assumptions.
This will be eased by introducing the following notion:
We say that a subset $\ControlledSet \subset \ML$ is \emph{\Econtrolled{\EL}} if and only if $\ControlledSet \subset \HL$ is bounded and if $\EL$ is bounded on $\ControlledSet$.
Here are our assumptions:
\begin{enumerate}
	\Item[\rm (P)]\label{condP}
	{\sc (Projector)}
	The map $\pr^{\ML}$ is bounded on \Econtrolled{\EL} subsets of $\ML$.
	\Item[\rm (B)]\label{condB}
	{\sc (Boundedness)}
	Every  \PaSma-sequence for $\widetilde{\EL} = \EL|_{\ML}$ is bounded.
	\Item[\rm (L)]\label{condL}
	{\sc (Limit in $\ML$)}
	Every convergent \PaSma-sequence of $\widetilde{\EL}$ has its limit point in $\ML$.
	\Item[\rm (S)]\label{condS}
	{\sc (Splitting)}
	There are 
	a scalar function $\mu \colon \ML \to \intervaloo{0,\infty}$,
	a continuous bilinear form $\QL \colon \HL \times \HL \to \R$,
	and 
	a map $\RL \colon \ML \to \BL^*$
	such that the differential $\D\EL$ splits as follows:
	\[
		\D\EL_x h = \mu(x) \, \QL(x,h) + \RL_x \, \iota_\BL \, h 
		\quad 
		\text{for all $x \in \ML$ and all $h \in\HL$.}
	\]
	Moreover, we assume the following:
	\begin{itemize}
	\Item[\rm (S1)]\label{condS1}
	For every \Econtrolled{\EL} subset $\ControlledSet \subset \ML$ there are $0 < m \leq M < \infty$ such that 
	\[
		m \leq \mu(x) \leq M \quad \text{for all $x\in\ControlledSet$.}
	\]
	
	\Item[\rm (S2)]\label{condS2}
		$\QL$ is coercive, i.e., there is $c > 0$ such that 
	\[
		\QL(h,h) \ge c \norm{h}_\HL^2
		\quad 
		\text{for all $h \in \HL$.}
	\]
	
	\Item[\rm (S3)]\label{condS3}
	$\RL$ is bounded on \Econtrolled{\EL} subsets of $\ML$.
	\end{itemize}

	\Item[\rm (D)]\label{condD}
	{\sc (Differential in non-tangential directions)}
	There is a map $\SL \colon \ML \to \BL^*$ such that 
	\[
		\D{\EL}_x \pars{\Id_\HL-\pr_x^\ML} \, h = \SL_x \, \iota_\BL \, h
		\quad 
		\text{for all $x \in \ML$ and all $h \in \HL$}, 
	\]
	and $\SL$ is bounded on \Econtrolled{\EL} subsets of $ \ML $.
\end{enumerate}

Condition \ref{condS3} is an abstract way of saying $\RL_x$ is of ``lower order'' and thus of less importance compared to $\QL(x,\cdot)$.
Likewise, \ref{condD} states that $\D \EL_x h$ is of ``lower order'' if $h$ is transversal to $T_x \ML$ in the sense that $h$ lies in the range of the $\pars{\Id_\HL-\pr_x^\ML}$.

\begin{theorem}[\PaSma-condition for $\widetilde{\EL}=\EL|_\ML$]
\label{thm:PS-abstract}
Under the conditions \ref{condE}, \ref{condP}, \ref{condB}, \ref{condL}, \ref{condS}, and \ref{condD} above, 
the restricted
energy $\widetilde{\EL}=\EL|_\ML$ satisfies the \PaSma-condition.
\end{theorem}

\begin{proof}
	Let $(x_k)_k\subset\ML$ be a \PaSma-sequence for $\widetilde{\EL}$.
	By condition \ref{condB}, $\ControlledSet \ceq \braces{x_k}_{k \in \N}$ is a bounded subset of $ \HL $. So,
	passing over to a subsequence, we may therefore assume that $(x_{k})_{k \in \N}$ is a weakly convergent \PaSma-sequence. 
	We are going to prove that $(x_{k})_{k \in \N}$ must also be strongly convergent in $\HL$ to a point $x_\infty$;
	because condition \ref{condL} then implies that $x_\infty$ lies in $\ML$, which proves the theorem.

	To show that $(x_{k})_{k \in \N}$ is strongly convergent, we use an argument inspired by the proof of \cite[Lemma 2.1]{cerami-etal_1984}.
	Note that $\ControlledSet \ceq \braces{x_k : k \in \N}$ is \Econtrolled{\EL} by definition of a \PaSma-sequence. 

	Let $0 < m \leq M < 0$ be the constants from \ref{condS1}, and let $c > 0$ be the coercivity constant from \ref{condS2}.
	For $h_k \ceq x_k - x_\infty$ we get
	\begin{equation}
		c \, m \norm{h_k}_\HL^2
		\leq 
		\mu(x_k) \, Q(h_k,h_k)
		=
		\mu(x_k) \, Q(x_k,h_k) - \mu(x_k) \, Q(x_\infty,h_k)
		.
		\label{eq:ExploitingCoercivity}
	\end{equation}
	From \ref{condS} and \ref{condD}, we obtain
	\[
		\mu(x_k) \, Q(x_k,h_k)
		=
		\D \EL_{x_k} \pr^\ML_{x_k} h_k
		+
		\SL_{x_k} \, \iota_\BL \, h_k
		-
		\RL_{x_k} \, \iota_\BL \, h_k
		.
	\]
	The triangle inequality and condition \ref{condS1} lead to
	\begin{align*}
		c \, m \norm{h_{k}}_\HL^2
		&\leq
		\abs{\D \EL_{x_k} \pr^\ML_{x_k} h_k}
		+
		\pars[\big]{
			\norm{\SL_{x_k}}_{\BL^*}
			+
			\norm{\RL_{x_k}}_{\BL^*} 
		} \norm{\iota_{\BL}h_k}_{\BL}
		+
		M \abs{Q(x_\infty,h_k)}
		.
	\end{align*}
	Because $\VL$ is \Econtrolled{\EL},
	conditions \ref{condD}, and \ref{condS3} imply that 
	\[
		C_\SL \ceq \sup_{k \in \N} \norm{\SL_{x_k}}_{\BL^*} < \infty 
		,
		\qand 
		C_\RL \ceq \sup_{k \in \N} \norm{\RL_{x_k}}_{\BL^*} < \infty 
		.
	\]
	Thus, we obtain
	\begin{equation}
		\label{eq:StruweTrick1}
		c \, m \norm{h_{k}}_\HL^2
		\leq
		\abs{\D \EL_{x_k} \pr^\ML_{x_k} h_k}
		+
		\pars[\big]{ C_\SL + C_\RL }
		\norm{\iota_\BL \, h_k}_{\BL}
		+
		M \abs{Q(x_\infty,h_k)}
		.
	\end{equation}
	The bilinear form $Q$ is continuous, and we have weak convergence $h_k \rightharpoonup 0$ in~$\HL$.
	Hence, the third summand $M\abs{Q(x_\infty,h_k)}$ in \cref{eq:StruweTrick1} converges to $0$ as $k \to \infty$.
	The operator $\iota_\BL$ is compact and $h_k$ converges weakly to $0$ in~$\HL$. 
	Hence, $\iota_\BL \, h_k$ converges strongly to~$0$ in~$\BL$.
	Thus, also the second summand in \cref{eq:StruweTrick1} converges to~$0$.
	Finally, we have to discuss the first summand in \cref{eq:StruweTrick1}.
	By definition of the dual norm and the operator norm $\norm{\pr^\ML_{x_k}}_{\LL(\HL)}$, we have
	\[
		\abs{\D \EL_{x_k} \pr^\ML_{x_k} h_k}
		=
		\abs{\D \widetilde{\EL}_{x_k} \pr^\ML_{x_k} h_k}
		\leq
		\norm{\D \widetilde{\EL}_{x_k}}_{(T_{x_k}\ML)^*}
		\norm{\pr^\ML_{x_k}}_{\LL(\HL)}
		\norm{h_k}_{\HL}
		.
	\]	
	Because $(x_k)_{k \in \N}$ is a \PaSma-sequence for $\widetilde{\EL}$, we have $\norm{\D \widetilde{\EL}_{x_k}}_{(T_{x_k} \ML)^*} \to 0$ as $k \to \infty$. 
	Since $\VL$ is \Econtrolled{\EL} and because of \ref{condP},
	we have $\sup_{k \in \N} \norm{\pr^\ML_{x_k}}_{\LL(\HL)} < \infty$. In addition, the weakly convergent sequence $ (h_k)_{k} $ is bounded.
	This shows that also the first summand in \cref{eq:StruweTrick1} converges to $0$. Since $c \, m > 0$, we infer that $h_k \to 0$ strongly in $\HL$, thus $x_k \to x_\infty$ as $k \to \infty$.
\end{proof}

If $\ML= \OL \subset \HL$,
then assumptions \ref{condP}, and \ref{condD} are automatically satisfied, and we obtain a result similar in flavor to \cite[Chapter~II, Proposition 2.2]{struwe_2008a}. 
(Note that the Lax--Milgram theorem implies that coercivity of $\QL$ means that the operator $\HL \to \HL^*$, $x \mapsto \QL(x,\cdot)$ is continuously invertible.)

\begin{corollary}[\PaSma-condition for $\EL$ on $\OL$]
\label{cor:PS-open-set}
Let $\ML=\OL \subset \HL$ be an open set and let $\EL\in C^1(\OL)$. 
Suppose that \ref{condE}, \ref{condB}, \ref{condL},  and  \ref{condS} are satisfied.
Then $\EL$ satisfies the \PaSma-condition.
\end{corollary}

In view of applications in geometric knot theory we consider linear 
combinations of a non-negative energy functional with lower order
terms. 
For this, we extend the abstract setting \ref{condE} by another Banach space $\CL$, into which the Hilbert space $\HL$ embeds compactly, i.e., there is a compact linear embedding $\iota_\CL \colon \HL \to \CL$.
Moreover, we complement condition \ref{condP} on the projection $\pr_x^\ML \colon \HL\to T_x\ML$
by the following condition:

\begin{enumerate}
	\Item[\rm (P*)]\label{condP*}
	There is an operator-valued map $\Pr \colon \ML \to \BoundedLinOps(\CL)$
	such that 
	\[
		\iota_\CL \, \pr^{\ML}_x = \PR_x \, \iota_\CL
		\quad 
		\text{for all $x \in \ML$,}
	\]
	and the map $\Pr$ is bounded on \Econtrolled{\EL} subsets of $\ML$.
\end{enumerate}

In addition to the original energy $\EL\in C^1(\OL)$ with its restriction $\widetilde{\EL}=\EL|_\ML$ to the submanifold $\ML\subset\OL\subset\HL \embeds \BL$, 
we
consider another functional $\FL \in C^1(\UL)$ on an open subset $\UL\subset\CL$ with $\iota_\CL(\OL)\subset\UL$.
For some fixed $\theta>0$ we investigate the  \emph{total energy} $\TL \ceq \EL + \theta \pars{\FL \circ \iota_\CL} \in C^1(\OL)$. 
Note that, in general, a \PaSma-sequence  for the restriction $\widetilde{\TL} \ceq \TL|_\ML$, need not be a \PaSma-sequence for the individual
functionals $\widetilde{\EL}$ or $\widetilde{\FL} \ceq (\FL \circ \iota_\CL) |_\ML$, even if
both functionals are non-negative, since their differentials
may not tend to zero. To formulate a clear-cut result,
we replace assumptions \ref{condL} and
\ref{condB} by the following separate  
assumptions on the energies: 
\begin{enumerate}
	\Item[\rm (B*)]\label{condB*}
	For every $K \in \R$ the sublevel set $\braces[\big]{ x \in \ML : \EL(x) \leq K}$ of $\widetilde{\EL} = \EL_\ML$ is bounded in $\HL$.
	\Item[\rm (L*)]\label{condL*}
	Whenever a sequence $(x_k)_k\subset\ML$ is weakly convergent in $\HL$ to some point $x_\infty$ and $ \sup_{k\in\N}\FL(x_k)<\infty $,
	then $x_\infty \in \ML$.	
\end{enumerate}

\begin{corollary}[(PS)-condition for the total energy $\widetilde{\TL}=\TL|_\ML$]
\label{cor:PS-total-energy}
	Let $\iota_\CL \colon \HL \embeds \CL$ be a compact embedding.
	Let $\OL \subset \HL$ and $\UL \subset \CL$ be open subsets such that $\iota_\CL(\OL) \subset \UL$, and let $\EL \in C^1(\OL)$ and $\FL \in C^1(\UL)$ be bounded from below on $\ML$.
	Suppose that conditions \ref{condE},
	\ref{condP}, \ref{condP*},
	\ref{condB*}, \ref{condS}, \ref{condD},
	and \ref{condL*} are satisfied.
	Then for every $\theta>0$ the restriction  $\widetilde{\TL}=\TL|_\ML$ of the total energy $\TL = \EL + \theta \pars{\FL\circ\iota_\CL}$
	satisfies the \PaSma-condition.
\end{corollary}

\begin{proof}
	By adding suitable constants, we may assume that $\widetilde{\EL} \geq 0$ and $\widetilde{\FL} \geq 0$.
	Let $(x_k)_k\subset\ML$ be a \PaSma-sequence for $\widetilde{\TL}$.
	By definition, there is a $K \in \R$ such that $\widetilde{\TL}(x_k) \leq K$ for all $k \in \N$.
	Now $\widetilde{\FL} \geq 0$ implies
	\begin{equation}
		\label{eq:energy-bound}
		\EL(x_k)
		=
		\widetilde{\EL}(x_k)
		\le
		\widetilde{\EL}(x_k) + \theta \, \widetilde{\FL}(x_k)=\widetilde{\TL}(x_k)\le K\quad\Foa k\in\N
		.
	\end{equation}
	By \ref{condB*}, $(x_k)_{k \in \N}$ is bounded in $\HL$. Hence, it contains a weakly convergent subsequence with limit point $x_\infty \in \HL$. 
	As in the proof of \cref{thm:PS-abstract}, we pass over to this subsequence and denote it by $(x_k)_{k \in \N}$. 
	And as in that proof, we aim to show that the $x_k$ converge strongly to $x_\infty$ in $\HL$.
	Once this is established, condition \ref{condL*} implies $x_\infty \in \ML$
	since $(x_{k})_{k \in \N}$ is bounded under~$\FL$;
	this follows from $\widetilde{\EL} \geq 0$:
	\begin{equation*}
		\FL(x_k)
		=
		\widetilde{\FL}(x_k)
		\le
		\tfrac{1}{\theta}
		\pars[\big]{ \widetilde{\EL}(x_k) + \theta \, \widetilde{\FL}(x_k)}
		=
		\tfrac{1}{\theta} \, \widetilde{\TL}(x_k)
		\le 
		\tfrac{K}{\theta}
		\quad\Foa k\in\N.
	\end{equation*}
	To show strong convergence of $(x_k)_{k \in \N}$, we first recall from \cref{eq:energy-bound} that $\ControlledSet \ceq \braces{x_k}_{k \in \N}$  is \Econtrolled{\EL}.
	Precisely as in the proof of \cref{thm:PS-abstract}, we derive inequality \cref{eq:StruweTrick1} for $h_k \ceq x_k - x_\infty$ and show that the second and third summand in \cref{eq:StruweTrick1} converge to~$0$. Alas, we need a new argument for showing that the first summand $\abs{\D \EL_{x_k} \pr^\ML_{x_k} h_k}$ converges to~$0$ as $ k\to \infty $.
	This time, we decompose it and use condition \ref{condP*} as follows:
	\[
		\D \EL_{x_k} \pr^\ML_{x_k} h_k
		=
		\D \TL_{x_k} \pr^\ML_{x_k} h_k
		-
		\theta \, \D \FL_{x_k} \, \iota_\CL \, \pr^\ML_{x_k} h_k
		=
		\D \widetilde{\TL}_{x_k} \pr^\ML_{x_k} h_k
		-
		\theta \, \D \FL_{(\iota_\CL x_k)} \, \PR_{x_k}\, \iota_\CL \,h_k
		.
	\]
	This leads us to
	\[
		\abs{\D \EL_{x_k} \pr^\ML_{x_k} h_k}
		\leq 
		\norm{\D \widetilde{\TL}_{x_k}}_{(T_{x_k}\ML)^*}
		\norm{\pr_{x_k}^\ML}_{\LL(\HL)}
		\norm{h_k}_{\HL}
		+
		\theta \norm{\D \FL_{(\iota_\CL x_k)}}_{\CL^*}
		\norm{\PR_{x_k}}_{\LL(\CL)}
		\norm{\iota_\CL \,h_k}_{\CL}
		.
	\]
	Since $\iota_\CL$ is compact, we have $\iota_\CL \, x_k \to \iota_\CL \, x_\infty$ as $k \to \infty$. 
	By condition~\ref{condL*}, we have $x_\infty \in \ML \subset \OL$
	and $\iota_\CL x_\infty \in \iota_\CL(\OL) \subset \UL$.
	Since $x \mapsto \D \FL_x$ is continuous on $ \UL $, and by condition~\ref{condP}, and because of $\iota_\CL \, x_k \to \iota_\CL \, x_\infty$, we have
	\[
		\smash{\sup_{k \in \N}} \norm{\D \FL_{(\iota_\CL x_k)}} < \infty
		,
		\quad 
		\sup_{k \in \N} \norm{\pr_{x_k}^{\ML}}  < \infty
		,
		\qand 
		\smash{\lim_{k \to \N}} \norm{\iota_\CL \, h_k}_{\CL} = 0
		.
	\]
	The sequence $(x_k)_{k\in\N}$ is a \PaSma-sequence for $\smash{\widetilde{\TL}}$, and because of \ref{condP*}, and $h_k \rightharpoonup 0$, we have 
	\[
		\smash{\lim_{k \to \infty}}
		\norm{\D \widetilde{\TL}_{x_k}}_{(T_{x_k}\ML)^*}
		=
		0
		,
		\quad 
		\sup_{k \in \N} \norm{\PR_{x_k}}_{\LL(\CL)}  < \infty
		,
		\qand
		\smash{\sup_{k \in \N}} \norm{h_k}_{\HL}  < \infty
		.
	\]
	All this together implies that $\smash{\abs{\D \widetilde{\EL}_{x_k} \pr^\ML_{x_k} h_k}} \to 0$ as $k \to \infty$, which completes the proof.
\end{proof}
