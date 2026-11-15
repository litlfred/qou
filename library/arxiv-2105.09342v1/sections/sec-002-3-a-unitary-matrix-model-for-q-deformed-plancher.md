---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-002-3-a-unitary-matrix-model-for-q-deformed-plancher
section_title: "A unitary matrix model for q-deformed Plancherel growth"
section_number: 3
pages: 7-10
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.985
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
The growth of Young diagrams can be compared with the growth of a two-dimensional crystal as shown in figure \ref{rotated_YD}. We consider every box as a unit falling from sky under gravity. There is a boundary given by the two lines passing through the origin with slope $\pm1$. Since the gravity is working downward it is easy to understand that the boxes will arrange themselves following the rules of a rotated Young diagrams. One can study a controlled growth process by assigning a probability to each diagram in this process. Following \cite{Eynard:2008mt, Chattopadhyay:2019pkl}, we can define a grand canonical ensemble of Young diagrams

\ben
\mathcal{E} = \bigcup_{k=0}^\infty \mathcal{Y}_k
\een

where $\mathcal{Y}_k$ is a set of Young diagrams with $k$ boxes. Next, assigning a probability for every diagram in the ensemble we write a grand canonical partition function for the $q$-deformed growth process as
\begin{equation}
\label{q-partition}
Z_q=\sum_{k=0}^{\infty}\sum_{\lambda_k} t^k \mathcal{P}_q(\lambda_k)\delta(k-|\lambda_k|)
\end{equation}
where $t>0$ is called \emph{fugacity}. In the above expression, $\mathcal{P}_q(\lambda_k)$ denotes the $q$-deformed Plancherel measure for a Young diagram $\lambda_k$ discussed in section \ref{sec:qplancherel}.

In order to study the above partition function in the large $k$ limit, we regularise the sum by imposing a cut-off on the Young diagrams in the summation over $\lambda_k$ in (\ref{q-partition}).  We introduce a large positive integer $N$ and constrain the Young diagrams in the ensemble to have no more than $N$ rows. This regularisation gives us a handle on the partition function to carry out a saddle point analysis of the problem. Later we show that the asymptotic behaviour of this regularised partition function can be captured by a unitary matrix model where $N$ plays the role of the rank of the unitary group.

The partition function \eqref{q-partition} for measure \eqref{eq:qmeasure2} is given by

\begin{equation}\label{eq:qdeformedgrowthpf2}
	\mathcal{Z}_q=\sum_{k=1}^{\infty}\sum_{\lambda_k}t^k \mathcal{P}_q(\lambda_k)=\sum_{k=1}^{\infty}\sum_{\lambda_k}t^k k! \frac{(1-q)^{2k}\ q^{2b(\lambda_k)}}{\prod_{u \in \lambda_k} [h(u)]^2}.
\end{equation}

It was observed in \cite{Chattopadhyay:2019pkl} that the ordinary Plancherel growth model is equivalent to $U(N)$ GWW model after restricting the Young diagrams to have maximum $N$ number of rows. The no-gap phase of GWW model describes the automodel class of Kerov. The limit shape corresponds to the GWW transition point. In this section, we first study the partition function (\ref{eq:qdeformedgrowthpf2}) in the large $N$ limit. The partition function admits two possible phases depending the value of the parameter  $t$ for a given $q$. The weak coupling phase of this theory captures the \qd growth of Young diagrams. Using the connection between UMM and 2D droplets we show that there exists an equivalent $U(N)$ UMM for the partition function (\ref{eq:qdeformedgrowthpf2}) whose no-gap phase captures the growth of Young diagrams under \qd Plancherel measure. Like GWW, this matrix model also admits a third order phase transition. This is a \qd analogue of GWW phase transition.

Using the definitions of \qq deformation (\ref{box-defn}), one can write the partition function as

\begin{equation}\label{eq:pfkind2}
	\begin{aligned}
	\mathcal{Z}_q & = \sum_{k=1}^{\infty}\sum_{\lambda_k}\exp \left[k \ln t + k \ln k-k+2k \ln (1-q)  + \sum_{i \neq j}\ln |q^{h_j}-q^{h_i}|\right. \\
	& \hspace{6cm} \left. - 2\sum_{i=1}^N \sum_{j=1}^{h_i}\ln (1-q^j)\right]
	\end{aligned}
\end{equation}

where we have dropped a constant term which makes no contribution to the saddle point equation.\\
In order to go to the continuum limit, we first re-define the parameter $q$,

\ben
q=e^{-g_s}
\een

and take the following double scaling limit
\begin{equation}\label{eq:doublescalling}
N \to \infty\ , \qquad g_s \to 0\ , \quad \mbox{such that}\ \lambda =N g_s\ \text{is finite.} 
\end{equation}
We also scale the variables and the summation appropriately with a factor of $N$ as follows
\begin{equation}
x=\frac{i}{N} , \quad  h(x) = \frac{h_i}{N}\quad \tand \quad \sum_{i=1}^{N} = N\int_0^1 dx.
\end{equation}
In the large $N$ limit, the total number of boxes scales as
\begin{equation}
k=\sum_{i=1}^N h_i -\frac{N(N-1)}{2} \xrightarrow[\text{limit}]{\text{large}\ N}N^2\int_0^1 dx\ h(x) -\frac{N^2}{2} \equiv N^2k'
\end{equation}
where
\begin{equation}
\int_0^1 dx\ h(x)=k'+\frac{1}{2}
\end{equation}
is an $O(1)$ quantity.\\
The partition function \eqref{eq:pfkind2} in the double-scaling limit can be written as

\begin{equation}
\cZ_q =\int [Dh]\, e^{S_{eff}},   
\end{equation}
where $S_{eff}$ is given by
\begin{equation}
	\begin{aligned}
	S_{eff}[h(x)]&=N^2 \left[k' \ln (N^2 t (1-q)^2 k')-k'+\int_0^1 dx \Xint-_0^1 dy \ln |e^{-\lambda h(x)}-e^{-\lambda h(y)}|\right.\\
	&\hspace*{7cm}\left. -2\int_0^1 dx \Xint-_0^{h(x)}dy \ln (1-e^{-\lambda y}) \right]
	\end{aligned}
\end{equation}

Varying the effective action with respect to $h(x)$, we get the saddle-point equation, which in terms of Young diagram density 
\ben
u(h)=-\frac{\partial x}{\partial h}
\een
is given by

\be
\label{eq:saddle_eynard}
\Xint-_{h_L}^{h_U} dh' u(h')\frac{e^{-\lambda h}}{e^{-\lambda h}-e^{-\lambda h'}}=-\frac{1}{\lambda} \log\left[\frac{1-e^{-\lambda h}}{\lambda\xi}\right]
\ee

with
\ben
\xi^2 = t \ k'.
\een
$u(h)$ has support between $h_L$ and $h_U$. From the monotonicity of $h_i$ (\ref{eq:hiconst}), it follows that the Young diagram density satisfies an upper bound
\ben
u(h) \leq 1.
\een
Therefore, one has to solve the above saddle-point equation in the presence of this constraint.\\
To solve the integral equation \eqref{eq:saddle_eynard}, we define new variables
\be\label{eq:hwrelation}
w = \frac{1-e^{-\lambda h}}{\lambda}
\ee
such that $u(w)= \frac{dh}{dw}u(h)$. 
In terms of these variables, the saddle point equation reduces to

\be
\label{eq:saddle_w}
\Xint-_{w_L}^{w_U} dw' \frac{u(w')}{w-w'} = \frac{1}{(1-\lambda w)} \log \frac{w}{\xi}
\ee

where $w_L=\frac{1-e^{-\lambda h_L}}{\lambda}$ and $w_U=\frac{1-e^{-\lambda h_U}}{\lambda}$ correspond to the end points of the support of $u(w)$.

Since the Young diagram density, $u(h)$ and hence $u(w)$ have an upper cap, we can classify solutions of (\ref{eq:saddle_w}) in two different classes. In the first class, the Young diagram density saturates the upper cap whereas in the second class, it does not. The solution class 1 captures the asymptotic growth of Young diagrams.
