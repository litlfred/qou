---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-002-21-the-large-n-droplets
section_title: "The large N droplets"
section_number: 2.1
pages: 7-9
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.994
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:connection}

Droplet description of large $N$ phases is based on the fact that the partition function of UMM has two equivalent descriptions - in eigenvalue basis and in Young diagram basis. It is well known that eigenvalues of unitary matrices behave like position of free fermions \cite{BIPZ}. On the other hand, hook lengths of Young diagrams are like momenta of these fermions \cite{duttagopakumar,douglas2}. A relation between these two pictures offers droplet or phase space description for different classical phases \cite{duttagopakumar,duttadutta,Chattopadhyay}.


It was first observed in \cite{duttagopakumar} that the eigenvalue and the Young diagram distributions are functional inverses of each other for a particular class of unitary matrix model, namely the $(a,b)$ model whose phase structure is similar to that of GWW model. Later in a series of papers \cite{duttadutta,riemannzero,Chattopadhyay} such relations were proved for a generic class of UMM. The details of the calculation is given in \ref{app:connection}. Here we present the main result.

In the large $N$ limit, the connection between eigenvalue density $\rho(\theta)$ and hook number $h$ is given by

\ben\label{eq:hrhorel}
h^2-2S(\theta) h + S^2(\theta)-\pi^2 \rho^2(\theta) =0
\een

where 

\ben\label{eq:Stheta}
S(\theta)=\frac12+\sum_n \beta_n \cos n\theta.
\een

Using this equation one can also define a spectral curve for the generic UMM. See \ref{app:speccurve}.

The relation (\ref{eq:hrhorel}) allows us to provide a phase space picture for different large $N$ phases of UMM in terms of free fermi droplets (two dimensional distributions). These distributions/droplets are similar to Thomas-Fermi distributions \cite{thomasfermi1,thomasfermi2}. Equation (\ref{eq:hrhorel}) has two possible solutions $h_{\pm}(\theta)$ given by

\ben\label{eq:hpm1}
h_{\pm}(\theta)=S(\theta)\pm \pi \rho(\theta).
\een

Using this relation we define a distribution function $\omega(h,\theta)$ in $(h,\theta)$ plane

\be \label{eq:phasespacedistri}
\omega(h,\q) = \Theta\lb{(h-h_-(\q))(h_+(\q)-h)\over 2}\rb
\ee

such that $\o(h,\q)=1$ for $h_-(\q)<h<h_+(\q)$ and zero otherwise.
Eigenvalue distribution, by construction, can be obtained by integrating
out $h$ for a given $\q$ and is given by

\be\label{eq:rhofromphasespace}
\r(\q)= \frac1{2\pi}\int dh \ \omega(h,\q) = {h_+(\q)-h_-(\q)\over 2\pi}.
\ee

The distribution also satisfies the normalisation condition

\ben\label{eq:omeganormalisation}
\frac1{2\pi}\int dh \ d\theta \ \omega(h,\theta) =1.
\een

The function $S(\q)$ can also be written in terms of phase space geometry

\be\label{eq:Sfromphasespace}
S(\q) = \frac1{2\pi \r}\int_0^\infty dh \ h \ \o(h,\q) =
{h_+(\q)+h_-(\q) \over 2}.
\ee

Integrating $\omega(h,\theta)$ over $\theta$ for a given $h$ gives a distribution of hook numbers $h$

\ben\label{eq:hdistribution}
w(h) = \frac1{2\pi}\int d\theta \ \omega(h,\theta)\quad \with \quad \int dh \ w(h) =1.
\een

$w(h)$ captures the information about large $N$ representations. Since $\omega^2(h,\theta) = \omega(h,\theta)$, it is actually the shape (i.e. boundary) of this distribution function which captures information about different large N phases of the theory. We call such two dimensional distributions large $N$ droplets.

The matrix model, we are considering, has no dynamics. Different large $N$ phases, obtained by solving the saddle point equation, are possible minimum free energy configurations of the model. Hence the corresponding droplets are static - the shapes are not changing with time. To incorporate dynamics into the picture, we follow an \emph{ad hoc} way : identify large $N$ droplets with Thomas-Fermi distribution at zero temperature and obtain the single particle Hamiltonian by comparing the two\footnote{One can also construct similar droplet description for time dependent unitary matrix model. In that case time evolution of these droplets are inherent \cite{Chattopadhyay:2020rle}}. In this way it is possible to incorporate time in our system.

Comparing the distribution function (\ref{eq:phasespacedistri}) with Fermi distribution at zero temperature

\be
\Delta(p,q) = \Theta(\mu - \mathfrak{h}(p,q))
\ee

($\mu$ is chemical potential and $\mathfrak{h}(p,q)$ is single particle Hamiltonian density) we find that the single particle Hamiltonian density is given by

\ben\label{eq:singleh}
\mathfrak{h}(h,\q)= {h^2\over 2} - S(\q)h + {g(\q)\over 2} + \mu, \quad 
\where \quad g(\q) = h_+(\q) h_-(\q).
\een

Total Hamiltonian\footnote{One can show that \cite{Chattopadhyay} integrating over $h$, the total Hamiltonian (without the $\hbar$ factor) is same as the collective field theory Hamiltonian of Jevicki and Sakita \cite{jevicki} 
	
\ben
\begin{split}\label{eq:Hamcoll}
H_h & = - \int d\q \lb \frac{S^2 \r}2 + \frac{\pi^2 \r^3}6 + V_{eff}(\theta)\rho\rb 
+\m
\end{split}
\een

with an effective potential.} can be obtained by integrating $\mathfrak{h}(h,\q)$ over the phase space

\ben\label{eq:Hh}
\begin{split}
	H_h &=\frac1{2\pi \hbar} \int d\q 	\int dh \ \o(h,\q) \ \mathfrak{h}(h,\q).
\end{split}
\een

We have taken into account the fact that one state occupies a phase space area of $2\pi \hbar$ in semi-classical approximation. It needs to modify the normalisation of phase space density

\ben
\frac{1}{2\pi \hbar}\int dh d\theta \omega(h,\theta) = N, \quad \with \quad  \hbar N =1 
\een

where, $N$ is total number of states available inside a droplet. The classical limit corresponds to $\hbar\ra0, \ N\ra \infty \ \with \  \hbar N =1$.
