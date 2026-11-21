---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-001-2-q-deformed-plancherel-growth
section_title: "q-deformed Plancherel growth"
section_number: 2
pages: 4-7
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.957
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
\label{sec:qplancherel}

The Plancherel growth of Young diagrams has been a topic of intense study over many years. In order to explain the growth process, let $\lambda_k$ denote a Young diagram with $k$ boxes. Consider two Young diagrams $\lambda_k$ and $\lambda_{k+1}$ such that $\lambda_{k+1}$ is obtained from $\lambda_k$ by adding one box. One can associate a transition probability
\begin{equation}
\label{ptransition}
p_{\text{tran}}(\lambda_k;\lambda_{k+1})=\frac{1}{k+1}\frac{\dim \lambda_{k+1}}{\dim \lambda_k}
\end{equation}
if $\lambda_{k+1}$ is obtained from $\lambda_{k}$ by adding one box, and zero otherwise. Here, $\text{dim}\lambda_k$ denotes the dimension of the representation of symmetric group $S_k$ corresponding to Young diagram $\lambda_k$ and is given by
\begin{equation}
\label{eq:Frob-HL-formula}
\dim \lambda_k= \frac{k!} {\prod_{u\in \lambda_k}h(u)} =  \frac{k!}{\prod_i h_i!} \prod_{i<j}(h_i-h_j) .
\end{equation}
We denote the total number of boxes in a Young diagram by $l(\lambda)$ and the number of boxes in $i^{th}$ row by $\{\lambda_i\}_{i=1,..,l(\lambda)}$ such that $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_{l{(\lambda)}} \geq 0$. The hook number for a given $\lambda_i$ is given by

\ben
h_i=\lambda_i +l(\lambda)-i .
\een

They satisfy the constraint
\ben\label{eq:hiconst}
h_1>h_2> \cdots > h_{l(\lambda)} >0 .
\een
The expression \eqref{eq:Frob-HL-formula} is known as the \emph{hook length formula} \cite{fulton1991representation}. For a growth process governed by (\ref{ptransition}), one can calculate the probability to find a Young diagram $\lambda_k$ at the $k^{th}$ level, starting from a diagram with zero box. See \cite{Chattopadhyay:2019pkl} for details. It turns out to be the well known \emph{Plancherel probability} and is given by
\be
\label{pmeasure}
\mathcal{P}(\lambda_k)=\frac{(\text{dim}\lambda_k)^2}{k!}.
\ee

A natural $q$-deformation of the Plancherel growth process has been studied in \cite{Kerov1993AQO, Strahov07, 2010arXiv1001.2180F}. It follows from the representation theory of Iwahori-Hecke algebras. The transition probability of going from $\lambda_k$ to $\lambda_{k+1}$ is given by
\be
\label{q-transition}
p_{\text{tran}}^q(\lambda_k;\lambda_{k+1})=q^{b(\lambda_{k+1})-b(\lambda_k)}\frac{{\prod_{u \in \lambda_k}[h(u)]}}{{\prod_{u \in \lambda_{k+1}}[h(u)]}}
\ee
where $0<q<1$ is the deformation parameter. The constant $b$ is given by
\ben
b(\lambda) = \sum_{i=1}^{l(\lambda)}(i-1) \lambda_i
\een
and
\begin{equation}
\label{eq:boxidentity}
\frac{1}{\prod_{u \in \lambda_k}[h(u)]}=\frac{\prod_{i<j }[h_i-h_j]}{\prod_{i} [h_i]!}.
\end{equation}
The square bracket in the above expression represents the $q$-analogue of a positive integer defined as
\be\label{box-defn}
[x]=1-q^x 
\ee
and

\begin{equation}
[x]!=[x][x-1] \cdots [2][1].
\end{equation}

The probability measure associated to a Young diagram $\lambda_k$ growing according to (\ref{q-transition}) is given by
\be
\label{eq:Strahov-qPlancherel}
\mathcal{P}_q(\lambda_k)=(1-q)^k \dim \lambda_k \frac{q^{b(\lambda_k)}}{\prod_{u \in \lambda_k}[h(u)]} .
\ee
This is the $q$-deformed Plancherel measure considered in \cite{Strahov07, 2010arXiv1001.2180F}. Using $\lim_{q \to 1}\frac{[x]}{1-q}=x$, we see that
\begin{equation}
\label{eq:q-deformed-limit}
\lim_{q \to 1} \mathcal{P}_q(\lambda_k)=\mathcal{P}(\lambda_k) .
\end{equation}
Thus, in the limit $q\rightarrow 1$, the $q$-deformed measure reduces to the Plancherel measure.

Strahov in \cite{Strahov07} gave a differential model for the $q$-deformed Plancherel growth process (\ref{q-transition}). He introduced a function $v_k(u)$ which describes the profile of a rotated  Young diagram as shown in fig.(\ref{rotated_YD}).
\begin{figure}[h]
	\begin{center}
		\includegraphics[scale=0.16]{RotatedYT.pdf}
		\caption{A typical Young diagrams written in the Russian convention.}
		\label{rotated_YD}
	\end{center}
\end{figure}
As the number of boxes becomes very large, Strahov defined a rescaled function
\be
\hat{v}_k(u)=\frac{v(u\sqrt{k})}{\sqrt{k}}
\ee
such that the area under the curve is finite. The boundary of Young diagram becomes smooth under scaling. He also introduced a \qd $R$ function associated with $\hat v_k$, given by
\be
R_{\hat{v}}(x;q)=\frac{1-q}{1-q^x}\text{exp}\left[-\ln q^{-1}\int \frac{d\sigma(u)}{1-q^{x-u}}\right]
\ee
where $\sigma(u)=\frac{1}{2}(\hat{v}(u)-|u|)$ is defined as the charge of a diagram \cite{Kerov1}. It was shown that the dynamical equation governing the growth of Young diagrams equipped with $q$-deformed Plancherel measure is given in terms of the $R$-function as
	\begin{equation}
	\label{q-burgers}
	\frac{\partial R_{\hat{v} (.,t;q)}(x;q)}{\partial x} + \frac{(1-q)}{\ln q^{-1}}R^{-1}_{\hat{v} (.,t;q)}(x;q)\frac{\partial R_{\hat{v} (.,t;q)}(x;q)}{\partial t} = 0.
	\end{equation}
This is a $q$-analogue of the automodel equation. It can be expressed in different equivalent forms in terms of various other quantities associated to Young diagrams \cite{Strahov07}. 

There exists another interesting class of \qq analog of Plancherel measure studied in \cite{Eynard:2008mt} for which

\begin{equation}\label{eq:qmeasure2}
 	\mathcal{P}_q(\lambda_k)= \left(\frac{\text{dim}_q\lambda_k}{k!}\right)^2 = k! \frac{(1-q)^{2k}\ q^{2b(\lambda_k)}}{\prod_{u \in \lambda_k} [h(u)]^2} =k!(1-q)^{2k}q^{2b(\lambda_k)}\frac{\prod_{1\leq i<j \leq N}[h_i-h_j]^2}{\prod_{i=1}^N ([h_i]!)^2}.  
\end{equation}

Such a measure plays an important role in the context of topological string theory partition function on certain Calabi-Yau threefolds and Gromov-Witten invariants of $\mathbb{P}^1$ \cite{Caporaso:2006gk, Nekrasov:2003rj, Nekrasov:2002qd, Marino:2006hs, okounkov2006uses}. Unlike (\ref{eq:Strahov-qPlancherel}), here the probability is proportional to the square of \qq dimension. This simplifies the large $N$ analysis to a great extent. The saddle point equation can be solved exactly in terms of the deformation parameter $q$. We observe that the behaviour of the automodel diagrams is qualitatively the same in both cases. 
Therefore, we mainly focus on the growth process governed by (\ref{eq:qmeasure2}) and write a $q$-analogue of the automodel equation in terms of \emph{Young diagram density}. For completeness, we also discuss the growth process under (\ref{eq:Strahov-qPlancherel}). However, in this case we are only able to provide the correction to automodel diagrams for the values of $q$ close to $1$.
