---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-001-2-review-1-droplet-description-of-unitary-matrix
section_title: "Review 1 : Droplet description of unitary matrix models"
section_number: 2
pages: 5-7
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.986
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:umm}

We start with a very brief discussion on droplet description of different large $N$ phases of a generic UMM. The partition function of UMM is given by,

\begin{equation}\label{eq:Zumm}
Z=\int [dU] e^{S(U)}
\end{equation}

where $[dU]$ is the Haar measure and $S(U)$ is a generic function of $N\times N$ unitary matrices $U$. The Haar measure $[dU]$ and $S(U)$ are invariant under unitary transformation. A particular class, but yet general, of unitary matrix models is given by the following action 

\ben\label{eq:partfuncplaq}
S(U)=N \sum_{n=1}^{Q}\frac{\beta_n}{n}\lb \Tr U^n +\Tr U^{\dagger n}\rb 
\een

where $Q$ is any arbitrary positive integer and $\beta_n$s are some arbitrary real parameters. This model is called the \emph{single plaquette model}. This model has applications in lattice gauge theory. Partition functions for different large $N$ Chern-Simons matter theories can also be written as a single plaquette model \cite{Chattopadhyay:2019lpr}. The large $N$ phase structure of (\ref{eq:partfuncplaq}) for $Q=2$ has been studied in \cite{zalewski,Mandal:1989ry}. A special case of single plaquette model is Gross-Witten-Wadia model \cite{gross-witten,wadia}, where $\beta_{n>1}=0$. {The GWW model is one of the exactly solvable models and it appears in many contexts in physics as well as in mathematics.}


Since both the Haar measure and the action in equation (\ref{eq:Zumm}) are invariant under unitary transformations, one can go to a diagonal basis
$$
U\ra \{e^{i \theta_1}, \cdots e^{i \theta_i}, \cdots, e^{i\theta_N}\},
$$
where $\theta_i$s are the eigenvalues of $U$. In the large $N$ limit a particular distribution of these eigenvalues on unit circle dominates the partition function. Defining a distribution function (called eigenvalue density) $\rho(\theta)$

\ben\label{eq:evdensity}
\rho(\theta) = \frac1N \sum_{i=1}^N\delta(\theta-\theta_i) = \frac{dx}{d\theta}
\een

one can show that in the large $N$ limit the eigenvalue density satisfies the saddle point equation

\ben\label{eq:evsaddle2}
\Xint- d\theta' \cot\lb \frac{\theta-\theta'}{2}\rb \rho(\theta') = \sum_n \beta_n \cos n\theta, \quad \with \quad \int d\theta \rho(\theta) = 1.
\een

This equation is obtained by extremising the effective action associated with the partition function (\ref{eq:Zumm}). For a given set of parameters $\{\beta_n\}$ one can solve this equation to find $\rho(\theta)$ corresponding to different large $N$ phases of the model under consideration. Different large $N$ phases are classified by number and positions of gaps in $\rho(\theta)$ \cite{BIPZ,zalewski,Mandal:1989ry,gross-witten,wadia} on a unit circle.

A unitary matrix model can be equivalently analysed in terms of $SU(N)$ (or $U(N)$) representations \cite{douglas2,duttagopakumar,duttadutta,Chattopadhyay}, which are expressed in terms of Young diagrams and hence the generic partition function (\ref{eq:Zumm}) can be written in Young diagram basis as well. Expanding the partition function in representation basis one finds

\ben\label{eq:pffinal2} 
\cZ=\sum_{\{h_i\}} \sum_{\vec k, \vec l}
\frac{\varepsilon(\vec \b, \vec k) \varepsilon(\vec \b, \vec
	l)}{z_{\vec k} z_{\vec l}} \chi_{\vec h}(C(\vec k)) \chi_{\vec
	h}(C(\vec l)) \quad \where, \quad \varepsilon(\vec \b, \vec k) =
\prod_{n=1}^{\infty}(N\b_{n})^{k_n}, \ \
z_{\vec k} = \prod_{n=1}^{\infty} k_{n}! n^{k_n}.
\een

Here, $\{h_1,\cdots,h_N\}$ are a set of hook numbers characterising a Young diagram, $\chi_{\vec h}(C(\vec k))$ is the character of the permutation group $S_k$ for a conjugacy class $C(\vec k)$ with $k=\sum_n n k_n$ in representation $\{h_i\}$. In the large $N$ limit the partition function (\ref{eq:pffinal2}) is dominated by a Young diagram which is characterised by a density function $u(h)$

\be\label{eq:uhdef}
u(h) = - {d x\over d h}.
\ee

Since $h(x)$ is a monotonically decreasing function of $x$, Young density has an upper and lower cap $1\geq u(h) \ge 0 \ \forall \ x\in[0,1]$. Large $N$ phases are characterised by different $u(h)$. It is difficult to find a saddle point equation for $u(h)$ for a generic plaquette model (\ref{eq:partfuncplaq}), but one can reconstruct dominant Young diagrams \cite{Chattopadhyay} through the droplet picture. See \ref{app:YDalysis} for details.
