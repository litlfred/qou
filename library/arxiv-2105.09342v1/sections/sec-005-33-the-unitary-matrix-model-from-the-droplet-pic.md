---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-005-33-the-unitary-matrix-model-from-the-droplet-pic
section_title: "The unitary matrix model from the droplet picture"
section_number: 3.3
pages: 12-15
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.994
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
\label{sec:umm-droplet}
In order to give a Hilbert space description of the \qd growth process we need to find a UMM whose large $N$ phase can capture the growth of Young diagrams. For ordinary Plancherel growth it was shown in \cite{Chattopadhyay:2019pkl} that using the Frobenius formula one can write the partition function as GWW model. In case of \qd Plancherel growth (\ref{eq:qdeformedgrowthpf2}), it is tricky to use the Frobenius formula for \qd dimension. So, we take a different route. We use the droplet picture \cite{duttagopakumar,Chattopadhyay} to find the UMM that captures the asymptotic growth of Young diagrams under \qd Plancherel measure. Eynard \cite{Eynard:2008mt} also gave a matrix model for \qd Plancherel growth. The partition function was given by an integral over hermitian matrices with eigenvalues running over a circle of some specified radius. Similar connection was also pointed out in \cite{1998math.10105B}. Here, we explicitly find the unitary matrix model.

It was first observed in \cite{duttagopakumar} and subsequently by \cite{duttadutta,Chattopadhyay,Chattopadhyay:2019pkl} that the large $N$ phases of a generic UMM (known as single plaquette model), given by
\ben\label{eq:UMM}
\cZ = \int [DU] \exp\lB N\sum_{n=1}^\infty \frac{\beta_n}{n}\lb \Tr U^n+\Tr U^{\dagger n}\rb\rB,
\een
can be described in two different but equivalent ways - in terms of eigenvalue distribution and Young diagram distribution\footnote{It is well known that eigenvalues of unitary matrices behave like position of free fermions \cite{BIPZ} and the hook lengths of Young diagrams are like momenta of these fermions \cite{duttagopakumar,douglas2}.}. Different large $N$ phases can be characterised by both eigenvalue density and Young diagram distribution. Therefore, it is expected that there is a relation between these two descriptions. The relation is given by \cite{Chattopadhyay}

\ben\label{eq:hrhorel}
h^2-2S(\theta) h + S^2(\theta)-\pi^2 \rho^2(\theta) = 0
\een

where 

\ben\label{eq:Stheta}
S(\theta)=\frac12+\sum_n \beta_n \cos n\theta.
\een

The relation (\ref{eq:hrhorel}) allows us to provide a phase space picture for different large N phases of UMM
in terms of free fermi droplets (two dimensional distributions). These distributions/droplets are
similar to Thomas-Fermi distributions. Equation (\ref{eq:hrhorel}) has two possible solutions, $h_\pm(\theta)$
given by

\ben\label{eq:hpmtheta}
h_\pm(\theta) = S(\theta) \pm \pi \rho(\theta).
\een

Using this relation, one can define a distribution $\omega(h,\theta)$ in a two dimensional plane spanned by $(h,\theta)$

\be \label{eq:phasespacedistri}
\omega(h,\q) = \Theta\lb{(h-h_-(\q))(h_+(\q)-h)\over 2}\rb
\ee

such that the eigenvalue distribution can be obtained by integrating out $h$ for a given $\theta$

\be\label{eq:rhofromphasespace}
\r(\q)= \frac1{2\pi}\int dh \ \omega(h,\q) = {h_+(\q)-h_-(\q)\over 2\pi}.
\ee

The distribution also satisfies the normalisation condition

\ben\label{eq:omeganormalisation}
\frac1{2\pi}\int dh \ d\theta \ \omega(h,\theta) =1.
\een

The function $S(\q)$ can also be written in terms of phase space geometry as following

\be\label{eq:Sfromphasespace}
S(\q) = \frac1{2\pi \r}\int_0^\infty dh \ h \ \o(h,\q) =
{h_+(\q)+h_-(\q) \over 2}.
\ee

Integrating $\omega(h,\theta)$ over $\theta$ for a given $h$, one obtains a distribution of hook numbers $h$

\ben\label{eq:hdistribution}
u(h) = \frac1{2\pi}\int d\theta \ \omega(h,\theta)\quad \with \quad \int dh \ u(h) =1.
\een

If $\omega(h,\theta)$ has a single boundary for a given $h$ and $\theta >0$, then there is another identification between eigenvalue $\theta$ and the Young diagram density
\ben\label{eq:uhtheta}
\pi u(h) = \theta.
\een
In general, it is difficult to find the Young diagram distributions for different large $N$ phases of (\ref{eq:UMM}). However using the droplet picture one can obtain the dominant representations in the large $N$ limit for different phases of (\ref{eq:UMM}) \cite{Chattopadhyay}.

Contrary to \cite{Chattopadhyay}, here we know the large $N$ phases of (\ref{eq:qdeformedgrowthpf2}) in terms of dominant Young diagrams. Our goal is to find the corresponding eigenvalue distribution and hence the UMM. From the Young diagram distribution of automodel class (\ref{q-automodel-D}), we see that $u(h)$ is a smooth function of $h$. Inverting the relation, we find that $h$ and $\theta$ (using \ref{eq:uhtheta}) satisfy
\ben
h=1-\frac{1}{\lambda} \log\lB 1-2\lambda \xi \cos\theta+\lambda^2\xi^2 \rB.
\een
Comparing this with (\ref{eq:rhofromphasespace}) and (\ref{eq:Sfromphasespace}), we have
\ben
\label{eq:Stheta1}
\begin{split}
S(\theta) = \pi \rho(\theta) = \frac{h_+(\theta)}{2} & = \frac12-\frac{1}{2\lambda} \log\lB  1-2\lambda \xi \cos\theta+\lambda^2\xi^2 \rB \\
&= \frac12+ \sum_{n=1}^\infty \frac{\xi^n\lambda^{n-1}}{n} \cos n\theta
\end{split}
\een
and 
\ben
h_-(\theta) =0.
\een
Now, comparing (\ref{eq:Stheta1}) with (\ref{eq:Stheta}), we get
\ben\label{eq:betan}
\beta_n = \frac{\xi^n \lambda^{n-1}}{n}.
\een

In order to complete the story, we note that the regularised partition function (\ref{eq:qdeformedgrowthpf2}) admits a phase transition in the large $N$ limit at \ben
\xi = \frac{1}{\lambda}(e^{\lambda/2}-1).
\een
For $\xi > \frac{1}{\lambda}(e^{\lambda/2}-1)$, the Young diagram density does not saturate the upper bound and is given by (see \ref{app:qGWWPT} for derivation)
\be
\label{eq:uh_gapped_phase}
u(h) =\frac{1}{\pi } \cos^{-1}\left[\frac{ 1+e^{\lambda} e^{-2 \lambda h} -2 e^{\lambda/2}e^{-\lambda h}(1+\lambda\xi)+\lambda\xi(2e^{-\lambda h} +\lambda\xi)}{2\lambda (1-e^{-\lambda h}) \xi}\right].
\ee
We need to confirm that the dictionary (\ref{eq:rhofromphasespace}) and (\ref{eq:Sfromphasespace}) renders the same UMM in this phase of the theory. Inverting \eqref{eq:uh_gapped_phase}, we see that there exist two possible solutions for $h$ for a given $\pi u(h)=\theta$. It is easy to check using (\ref{eq:Sfromphasespace}) that we obtain the same $S(\theta)$ (see \ref{app:qGWWPT} for details). Thus, we conclude that the asymptotic (large $N$) structure of the \qd partition function (\ref{eq:qdeformedgrowthpf2}) is captured by a UMM (\ref{eq:UMM}) with $\beta_n$ given by (\ref{eq:betan}). The \qd growth of Young diagrams is captured by the no-gap phase of this UMM.
