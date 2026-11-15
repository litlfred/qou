---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-008-25-translation-functors
section_title: "Translation functors"
section_number: 2.5
pages: 14-17
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.975
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-translation}
Fix $\lambda\in\mathcal A_0$ and 
$\mu\in\bar{\mathcal{A}}_0-\mathcal A_0$. Set $\nu=|\lambda-\mu|$ 
(in fact, $\nu=|\lambda_i-\mu_i|$ for all 
$i\in\bN$ and $\nu$ will stay in $\bar{\mathcal{A}}_0$). 
Recall that there is a unique simple 
$\Uq$-module $\Ln{\nu}\cong\Tn{\nu}$.
Denote by $p_{\lambda}\colon\T\to\T_{\lambda}$ the 
\textit{projection onto the block} $\T_{\lambda}$ functor. Similarly for $\mu$.



\begin{defn}(\textbf{Onto and out of the wall})\label{defn-onout}
Given $\lambda$ and $\mu$, we define 
two functors via
\[
\mathcal T_{\lambda}^{\mu}\colon\T_{\lambda}\to\T_{\mu},\;M\mapsto p_{\mu}(M\otimes_{\bC}\Tn{\nu}),\quad\quad\mathcal T^{\lambda}_{\mu}\colon\T_{\mu}\to\T_{\lambda},\;M\mapsto p_{\lambda}(M\otimes_{\bC}\Tn{\nu}).
\]
We call them \textit{translation onto} the $\mu$-wall $\mathcal T_{\lambda}^{\mu}$ and 
\textit{translation out of} the $\mu$-wall $\mathcal T^{\lambda}_{\mu}$.
\end{defn}




\begin{defn}(\textbf{Through the wall})\label{defn-trans}
Define $\Theta_s^{\lambda}=\mathcal T^{\lambda}_{-1}\circ \mathcal T_{\lambda}^{-1}$ and $\Theta_t^{\lambda}=\mathcal T^{\lambda}_{l-1}\circ \mathcal T_{\lambda}^{l-1}$. We 
call them \textit{translation through the wall functors}.
\end{defn}



If it is clear which $\lambda$ we are using we, abusing notation, denote them by $\Theta_s,\Theta_t$.



\begin{prop}\label{prop-functors}
For all $i\in\bN$ we have 
the following.
\begin{itemize}
\item[(a)] The functors 
$\mathcal T_{\lambda}^{\mu}$ and $\mathcal T^{\lambda}_{\mu}$ are well-defined (their definition gives $\Uq$-tilting modules in the right blocks), 
adjoints (left and right) and 
exact. Thus, $\Theta^{\lambda}_s$ and 
$\Theta^{\lambda}_t$ are exact and self-adjoint.
\item[(b)] We have (recalling that $\Ln{\mu_i}\cong\Tn{\mu_i}$)
\[
\mathcal T_{\lambda}^{\mu}(\Tn{\lambda_i})\cong\begin{cases}\Tn{\mu_{i-1}}\oplus\Tn{\mu_{i+1}},  & \text{if }\mu_i>\lambda_i,\\
  \Tn{\mu_i}\oplus\Tn{\mu_i},  & \text{if }\mu_i<\lambda_i,\end{cases}\quad
\mathcal T^{\lambda}_{\mu}(\Tn{\mu_i})\cong\begin{cases}\Tn{\lambda_{i+1}},  & \text{if }\mu_i>\lambda_i,\\
 \Tn{\lambda_{i}},  & \text{if }\mu_i<\lambda_i.\end{cases}
\]
\item[(c)] The dead-end relations $\Theta^{\lambda}_s(\Tn{\lambda_0})\cong0$, $\Theta^{\lambda}_s(\Tn{\lambda_1})\cong\Tn{\lambda_2}$, and $\Theta^{\lambda}_t(\Tn{\lambda_0})\cong\Tn{\lambda_1}$. Moreover, we have
\[
\Theta^{\lambda}_{s\text{ or }t}(\Tn{\lambda_i})\cong\begin{cases}\Tn{\lambda_{i-1}}\oplus\Tn{\lambda_{i+1}} ,  & \text{if }i>1\text{ is odd for }s\text{ and even for }t,\\
  \Tn{\lambda_{i}}\oplus\Tn{\lambda_{i}} ,  & \text{if }i>0\text{ is odd for }t\text{ and even for }s.\end{cases}
\]
\end{itemize}
Here we set $\Tn{-1}=\Tn{\lambda_{-1}}=\Tn{\mu_{-1}}=0$.\makeqed
\end{prop}


Note that biadjoint functors have in 
addition some other nice properties, see e.g.~\cite[Section~2]{kh5}. Moreover, 
in the 
case $\mu=-1$ we have $\mu_i>\lambda_i$ 
iff $i$ is odd whereas in the case $\mu=l-1$ 
we have $\mu_i>\lambda_i$ iff $i$ is even as 
a look at~\eqref{eq-alcove} should convince the reader.



\begin{proof}
\textbf{(a).} The functors are well-defined by 
(c) of Proposition~\ref{prop-basicp} and
part (b) of Lemma~\ref{lem-tiltcat}, i.e. tensor products of tiltings are tiltings. 
The other statements can be verified as in the 
case of category $\mathcal O$, i.e. we can adopt~\cite[Sections~7.1 and~7.2]{hum} without difficulties. 




\textbf{(b).} Use 
Propositions~\ref{prop-weyl} 
and~\ref{prop-tilt}, Corollary~\ref{cor-weyl} and Theorem~\ref{thm-link}.



\textbf{(c).} This is just a direct application of the finer list of 
statements given in (b).
\end{proof}



We use the convention that 
$\Theta^{\lambda}_{k-tst}$ denotes an 
\textit{alternating} composition of length 
$k$ of translation through the wall functors starting with 
$\Theta^{\lambda}_{t}$. Likewise for $\Theta^{\lambda}_{k-sts}$.
Using (c) of Proposition~\ref{prop-functors}, we get the following.


\begin{cor}(\textbf{Combinatorics of the translation 
through the wall functors})\label{cor-theta}
We have:
\begin{itemize}
\item[(a)] $\Theta_s^{\lambda}\circ\Theta_s^{\lambda}\cong \Theta_s^{\lambda}\oplus \Theta_s^{\lambda}$ and $\Theta_t^{\lambda}\circ\Theta_t^{\lambda}\cong \Theta_t^{\lambda}\oplus \Theta_t^{\lambda}$ as functors.
\item[(b)] We have for $i\in\bN$ even respectively odd, 
that (with $k\geq 0$ terms $\Theta^{\lambda}_{t\text{ or }s}$) 
there exist multiplicities $m_j\in\bN$ (that can be zero) such that
\begin{gather*}
\Theta^{\lambda}_{k-tst}\Tn{\lambda_i}=(\Theta^{\lambda}_{s\text{ or }t}\circ\dots\Theta^{\lambda}_t\circ\Theta^{\lambda}_s\circ\Theta^{\lambda}_t)\Tn{\lambda_i}\cong \Tn{\lambda_{i+k}}\oplus \bigoplus_{j<i+k}\Tn{\lambda_{j}}^{\oplus m_j},
\\
\Theta^{\lambda}_{k-tst}\Tn{\lambda_i}=(\Theta^{\lambda}_{s\text{ or }t}\circ\dots\Theta^{\lambda}_t\circ\Theta^{\lambda}_s\circ\Theta^{\lambda}_t)\Tn{\lambda_i}\cong \Tn{\lambda_{i-1+k}}^{\oplus 2}\oplus \bigoplus_{j<i-1+k}\Tn{\lambda_{j}}^{\oplus m_j}.
\end{gather*}
Similarly for $i\in\bN$ odd respectively even and $\Theta^{\lambda}_{k-sts}$.\makeqed
\end{itemize}
\end{cor}

\begin{proof}
Clear from Proposition~\ref{prop-functors}.
\end{proof}

Define the following functors:
\begin{gather*}
\begin{aligned}
\mathcal T^{\mu,i}_{\lambda}=p_{\bbi}\circ\mathcal T^{\mu}_{\lambda},
\quad\quad&
\mathcal T_{\mu}^{\lambda,i}(\Tn{\mu_j})=\begin{cases}
\delta_{i,j}\Tn{\lambda_{i}},&\text{if }\mu=-1, i\text{ even},\\
\delta_{i,j}\Tn{\lambda_{i}},&\text{if }\mu=l-1, i\text{ odd},
\end{cases}
\\
\Theta_{s\text{ or }t}^{\lambda,i}&=\begin{cases}p_{\bbi}\circ\Theta^{\lambda}_{s}, &\text{if }i\text{ is even},\\
p_{\bbi}\circ\Theta^{\lambda}_{t}, &\text{if }i\text{ is odd}.
\end{cases}
\end{aligned}
\end{gather*}
Here $p_{\bbi}$ denotes the projection to the $\Tn{\bbi}$-part.

\begin{defn}\label{defn-tiltcatendo}
Given a $\Uq$-tilting module $T$, denote by 
$\mathcal F_{T}$ any functor $\mathcal F_{T}\cong \cdot\otimes_{\bC}T$.
A functor $\mathcal F\colon\T\to\T$ is called 
\textit{projective} if it is a direct summand 
of functors of the form $\mathcal F_{T}$.
We denote by $\Endo(\T)$ the \textit{category 
of projective endofunctors} $\mathcal F\colon\T\to\T$ 
whose morphisms $\Hom_{\Endo(\T)}(\mathcal F,\mathcal F^{\prime})$ 
are natural transformations $\eta\colon\mathcal F\to\mathcal F^{\prime}$. 
Moreover, we denote by $\Endo(\T_{\lambda})$ the \textit{category 
of projective endofunctors} $\mathcal F\colon\T_{\lambda}\to\T_{\lambda}$ 
that can be obtained via compositions and countable direct sums 
of functors of the form $\Theta_{s\text{ or }t}^{\lambda,i}$. Similarly for walls $\mu$. 
Here we count the empty sum as the identity functor. 
\end{defn}


It follows from Lemma~\ref{lem-profunc} below that these are actually categories. 
Moreover, by construction, the translation through the wall functors 
$\Theta_s^{\lambda}$ or $\Theta_t^{\lambda}$ are objects in $\Endo(\T_{\lambda})$, 
since
\begin{equation}\label{eq-projectivefunc}
\Theta_s^{\lambda}=\!\!\bigoplus_{i\in\bZ_{\geq 1}}\!\!\Theta_s^{\lambda,2i},\quad\quad\Theta_t^{\lambda}=\!\!\bigoplus_{i\in\bZ_{\geq 0}}\!\!\Theta_s^{\lambda,2i+1},
\end{equation}
as follows by Proposition~\ref{prop-functors}. Similarly,
\begin{equation}\label{eq-projectivefunc2}
\mathcal T_{\lambda}^{\mu}=\!\!\bigoplus_{i\in\bZ_{\geq 0}}\!\!\mathcal T_{\lambda}^{\mu,i},\quad\quad \mathcal T_{\mu}^{\lambda}=\begin{cases}\bigoplus_{i\in\bZ_{\geq 0}}\!\!\mathcal T_{\mu}^{\lambda,2i}, &\text{if }\mu=-1,\\
\bigoplus_{i\in\bZ_{\geq 0}}\!\!\mathcal T_{\mu}^{\lambda,2i+1}, &\text{if }\mu=l-1.\end{cases}
\end{equation}

\newpage

\begin{lem}\label{lem-profunc}
$\Endo(\T), \Endo(\T_{\lambda}), \Endo(\T_{\mu})$ are additive 
categories of exact functors.\makeqed
\end{lem}



\begin{proof}
That $\Endo(\T)$ is closed under composition 
follows from part (b) of Lemma~\ref{lem-tiltcat}, 
and the identity functor is projective because 
of $\mathrm{id}\cong\cdot\otimes_{\bC} \Tn 0$. Hence, $\Endo(\T)$ is a category.
That $\Endo(\T)$ is preserved under finite 
direct sums (showing that the category is 
additive) follows from part (a) of Lemma~\ref{lem-tiltcat}. 
The statement for the $\lambda$ and $\mu$ 
versions follow by construction.
Last, that functors in 
$\Endo(\T)$ are exact follows because tensoring over a 
field always respects exact sequences. 
Likewise for the $\lambda$ and $\mu$ versions which come 
from projections of such functors.
\end{proof}



The following lemma 
is true in more generality (see for example~\cite[Chapter~4, Section~6]{ass}), 
but we restrict to our case here. Recall that a 
functor between additive categories 
$\mathcal F\colon\mathcal C\to\mathcal D$ is 
called \textit{indecomposable} if any 
decomposition $\mathcal F\cong\mathcal F_1\oplus\mathcal F_2$ 
implies that $\mathcal F_1\cong 0$ or $\mathcal F_2\cong 0$.
Moreover, we call a category \textit{infinite} Krull-Schmidt 
if each object can be uniquely decomposed (up to permutation) 
into a countably infinite direct sum of indecomposable objects.



\begin{lem}\label{lem-profuncinde}
A functor $\mathcal F\cong \cdot\otimes_{\bC} T$ is 
indecomposable iff $T$ is an indecomposable 
$\Uq$-module. Thus, $\Endo(\T)$ is Krull-Schmidt. In contrast, the $\lambda$ and 
$\mu$ versions are infinite Krull-Schmidt.\makeqed
\end{lem}



\begin{proof}
Assume that $T$ decomposes 
into $T_1\oplus T_2$. Then $\mathcal{F}\cong (\cdot\otimes_{\bC}T_1)\oplus (\cdot\otimes_{\bC}T_2)$.
On the other hand, by Yoneda 
and the tensor-hom adjunction, 
the $T$ representing $\mathcal F$ is 
uniquely determined up to isomorphism. 
Thus, a decomposition of $\mathcal F$ 
induces a decomposition of $T$. This 
implies, by using 
part (a) of Lemma~\ref{lem-tiltcat}, that $\Endo(\T)$ is Krull-Schmidt.

The statement for the $\lambda$ and $\mu$ 
versions follow again by construction.
\end{proof}





\begin{prop}\label{prop-profunc}
The functors $\mathcal T^{\mu,i}_{\lambda}$, $\mathcal T_{\mu}^{\lambda,i}$ and 
$\Theta^{\lambda,i}_{s\text{ or }t}$ are 
all indecomposable.
\end{prop}



\begin{proof}
Any non-trivial decomposition 
$\Theta^{\lambda,i}_{s\text{ or }t}=F_1\oplus F_2$ 
gives rise to a non-trivial idempotent 
$\eta\in\Endo(\Theta^{\lambda,i}_{s\text{ or }t})$. 
By using Proposition~\ref{prop-functors} together 
with Corollary~\ref{cor-homspaces} we see that 
such a natural transformation can not exist 
(most of the $\Uq$-intertwiners are nilpotent). 
Let us illustrate this in an explicit calculation for $\Theta^{\lambda,i}_t$ 
with $i\neq 0$.
Applying $\Theta^{\lambda,i}_t$ on the sequence
\begin{equation}\label{eq-inde}
\xy
\xymatrix{
 \Tn{\bbid}
\ar@<2pt>[r]^/0.25cm/{u_{i-1}} & \Tn{\bbi}\ar@<2pt>[l]^/-0.25cm/{d_{i}}\ar@<2pt>[r]^/-0.25cm/{u_i} 
& \Tn{\bbiu}\ar@<2pt>[l]^/0.25cm/{d_{i+1}}
}
\endxy
\end{equation}
gives us (with bottom and top row given by applying 
$\Theta^{\lambda,i}_t$ to~\eqref{eq-inde})
\begin{gather}\label{eq-inde2}
\begin{aligned}
\xy
\xymatrix{
\Tn{\bbi}\ar@<2pt>[r]^/-1.0em/{\begin{pmatrix} 0\\ 1 \end{pmatrix}}
\ar@{<->}[dd]|{\eta_{\Tn{\bbid}}}
&
\Tn{\bbi}\oplus\Tn{\bbi}\ar@<2pt>[r]^/0.9em/{\begin{pmatrix} 1 & 0\end{pmatrix}}
\ar@<2pt>[l]^/0.9em/{\begin{pmatrix} 1 & 0 \end{pmatrix}}
\ar@{<->}[dd]|{\eta_{\Tn{\bbi}}}
&
\Tn{\bbi}\ar@<2pt>[l]^/-0.9em/{\begin{pmatrix} 0 \\ 1 \end{pmatrix}}
\ar@{<->}[dd]|{\eta_{\Tn{\bbiu}}}\\
& & &\\
\Tn{\bbi}\ar@<2pt>[r]^/-1.0em/{\begin{pmatrix} 0\\ 1 \end{pmatrix}}
&
\Tn{\bbi}\oplus\Tn{\bbi}\ar@<2pt>[r]^/0.9em/{\begin{pmatrix} 1 & 0\end{pmatrix}}
\ar@<2pt>[l]^/0.9em/{\begin{pmatrix} 1 & 0 \end{pmatrix}}
&
\Tn{\bbi}.\ar@<2pt>[l]^/-0.9em/{\begin{pmatrix} 0 \\ 1 \end{pmatrix}}
}
\endxy
\end{aligned}
\end{gather}
Here we used Proposition~\ref{prop-functors} to calculate 
$\Theta^{\lambda,i}_t(\Tn{i})$, while the images of the 
$\Uq$-intertwiners can be calculated as in Example~\ref{ex-howtofunctor}. 
Note that $\eta$ above is assumed to be a natural transformation, i.e. 
all squares in~\eqref{eq-inde2} commute.
Now, under the assumption that $\eta$ is an idempotent, we have $\eta_{\Tn{\bbid}}$ 
equals $0$ or $1$ because of Corollary~\ref{cor-homspaces}. 
In the first case we obtain that all others components 
of $\eta$ are zero as well, while in the second case we obtain 
that all others components 
of $\eta$ are the identity as well 
(both follow via direct computation using Corollary~\ref{cor-homspaces}, the assumption 
that all components of $\eta$ are idempotents 
and the commutativity of all squares in~\eqref{eq-inde2}). 
The same arguments and calculations show the 
claim for the functors $\Theta^{\lambda,i}_s$ 
and $\mathcal T_{\lambda}^{\mu,i}$ 
(except that our job is even easier for the latter since all 
involved tiltings are simple). 
The claim for the functor $\mathcal T^{\lambda,i}_{\mu}$ is left to the reader.
This shows 
the statement.
\end{proof}

\begin{rem}\label{rem-projective}
The category $\Endo(\T_{\lambda})$ is the Karoubi envelope 
(in the sense of Definition~\ref{defn-karoubi}) of the 
category $\Endo_{\Theta}(\T_{\lambda})$ generated 
(via direct sums and compositions) by the 
translation through the wall functors $\Theta^{\lambda}_{s\text{ or }t}$. 
This follows from~\eqref{eq-projectivefunc} and Proposition~\ref{prop-profunc}. 
We call $\Endo(\T_{\lambda})$ the category of projective endofunctors 
although it would be historical more accurate to call 
$\Endo_{\Theta}(\T_{\lambda})$ the category of projective endofunctors. 
This convention is due to the fact that, in contrast to the case of category $\mathcal O$ 
(see e.g.~\cite{bg}), our buildings blocks are the 
various $\Theta^{\lambda,i}_{s\text{ or }t}$ 
and not the functors $\Theta^{\lambda}_{s\text{ or }t}$ themselves.
\end{rem}
