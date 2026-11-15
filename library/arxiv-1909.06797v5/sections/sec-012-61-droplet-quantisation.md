---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-012-61-droplet-quantisation
section_title: "Droplet quantisation"
section_number: 6.1
pages: 19-25
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.984
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:fluctuation}


The single particle Hamiltonian (\ref{eq:singleh}) is not in diagonal form. We define a new variable

\ben
\bar h = h-S(\theta).
\een

In terms of this new variables $(\bar h, \theta)$ the Hamiltonian density is given by

\ben\label{eq:singleh2}
\mathfrak{h}(\bar h,\theta) = \frac{\bar h^2}2 -\frac{\pi^2}2 \rho(\theta)^2
\een

and the droplet boundary is given by

\ben\label{eq:boundaryeqn2}
\bar h_{\pm}(\theta) = \pm \pi \rho(\theta).
\een

The phase space Hamiltonian (\ref{eq:Hh}) can be calculated by integrating over $\bar h$ from $\bar h_{-}(\theta)$ to $\bar h_{+}(\theta)$ and is given by,

\ben\label{eq:Hh1}
H_h = \frac1{3\pi \hbar}\int d\theta \ \pi^3 \rho(\theta)^3.
\een

The phase space boundary is doubly degenerate, i.e. for a given $\theta$ there are two boundaries, $\bar h_{\pm}$ corresponding to two signs on the right hand side of (\ref{eq:boundaryeqn2}). Hence, we write the Hamiltonian (\ref{eq:Hh1}) over the two segments of droplets \cite{Maoz:2005nk}

\ben\label{eq:Hhtwoboundary}
H_h = \frac1{6\pi \hbar}\left[\int_+ d\theta \ \bar h^3_+(t,\theta) - \int_- d\theta \ \bar h^3_-(t,\theta)  \right].
\een

From the single particle Hamiltonian (\ref{eq:singleh2}) we find that the equations of motion satisfied by the droplet boundaries are given by\footnote{Equations of motion from (\ref{eq:singleh2}) are given by 
\ben\label{eq:eom}
\dot{\bar h}(t) = -\frac{\partial \mathfrak h}{\partial \theta} = \pi^2 \rho(\theta) \rho'(\theta), \qquad \dot \theta(t) = \frac{\partial \mathfrak h}{\partial \bar h} = \bar h(t)
\een

Substituting the boundary relations (\ref{eq:boundaryeqn2}) in these equations, one finds (\ref{eq:boundeq}).},

\ben\label{eq:boundeq}
\dot{\bar h}_{\pm}(t,\theta) = \bar h_\pm(t,\theta)\bar h_\pm'(t,\theta)
\een

{where the dot and prime denote derivative with respect to $t$ and $\theta$ respectively} \footnote{{At this point one should note that (\ref{eq:boundeq}) is in the standard from of an inviscid Burger's equation, which is a KdV type equation. The appearance of KdV type equations is quite common in random matrix theories which indicates that the problem is exactly solvable. For the Fermi fluid picture that appears in the context of unitary matrix model one can actually construct an infinite set of commuting \emph{Hamiltonians/conserved charges} \cite{Avan:1991kq,Avan:1991ik}, signifying the integrability of the system. In fact, in \cite{Avan:1991ik} the authors have used analogous variables of (\ref{eq:hpm1}) to deduce the Lax pairs with the same Hamiltonian as (\ref{eq:Hhtwoboundary}). Further, the commuting Hamiltonians described in \cite{Avan:1991ik,Jevicki:1993qn} can be shown to be similar to different moments of the diagram (\ref{eq:moments}) and the resolvent (\ref{eq:Hresolvent}) or similarly the moment generating function (\ref{eq:momgenfunc}) includes information about the full \emph{spectrum} of the Hamiltonians. Therefore from the integrability structure emergent from the matrix model side one can show that all the moments of the diagram as described by \cite{Kerov1} is conserved. In the current context we are interested in \emph{canonically quantising} the droplets, rather than looking at the underlying integrability structure of (\ref{eq:Hhtwoboundary}).}}.

In order to quantise the droplets we find a simplectic form such that the Hamilton's equation

\be\label{eq:Hameq2}
\dot {\bar h}_{\pm}(t,\theta) = \{\bar h_\pm(t,\theta),H_h\}
\ee

would coincide with (\ref{eq:boundeq}) \cite{Grant:2005qc,Maoz:2005nk}. To achieve the above goal we introduce Poisson brackets between $\bar h_{\pm}(t,\theta)$ and $\bar h_{\pm}(t,\theta')$

\ben\label{eq:poisson}
\{\bar h_\pm(t,\theta),\bar h_\pm(t,\theta')\} = \pm {\pi \hbar} \delta'(\theta-\theta')\quad \text{and} \quad \{\bar h_+(t,\theta),\bar h_-(t,\theta')\} =0.
\een

It is easy to check that using these Poisson brackets, equation (\ref{eq:Hameq2}) boils down to (\ref{eq:boundeq}). {Also,

\be
\{ H_h, \cA \}=0
\ee

where

\be
\mathcal{A}=\int_{-\pi}^{\pi} d\theta\, (\overline{h}_+(t,\theta) - \overline{h}_-(t,\theta))
\ee

is the area of the phase space droplets. This implies that the area is preserved under classical time evolution.}

The circular droplet ($\rho(\theta) =\frac1{2\pi}$) corresponds to $\bar h_\pm(t,\theta)=\pm \frac12$ and satisfy the classical equations of motion (\ref{eq:boundeq}). We consider quantum fluctuations about this classical circular droplet

\ben\label{eq:hpmode}
\bar h_{\pm}(t,\theta) = \pm\frac12+ \hbar\ \tilde h_\pm(t,\theta).
\een

We also assume that the fluctuations preserve the total area of the droplet. This implies that 

\ben\label{eq:tildehcons}
\int_{-\pi}^{\pi} d\theta (\tilde h_+(t,\theta) - \tilde h_-(t,\theta))=0.
\een

The Hamiltonian (\ref{eq:Hhtwoboundary}) for these fluctuations is given by

\ben\label{eq:Hhtwoboundary2}
H_h = \frac{1}{12\hbar} + \frac{\hbar}{4\pi}\int_{-\pi}^{\pi} \lb \tilde h_+^2(t,\theta) + \tilde h_-^2(t,\theta) \rb d\theta + \frac{\hbar^2}{6 \pi} \int_{-\pi}^{\pi} \lb \tilde h_+^3(t,\theta) - \tilde h_-^3(t,\theta) \rb d\theta.
\een


From equation (\ref{eq:poisson}), we find that the Poisson bracket for $\tilde h_\pm(t,\theta)$ are given by

\ben\label{eq:poisson2}
\{\tilde h_\pm(t,\theta), \tilde h_\pm(t,\theta')\} =\pm \frac{\pi}{\hbar} \delta'(\theta-\theta') \quad \text{and} \quad \{\tilde h_+(t,\theta),\tilde h_-(t,\theta')\} =0.
\een

To quantise the above classical system we promote the Poisson brackets (\ref{eq:poisson2}) to commutation relations

\be\label{eq:commutation}
\left[ \tilde h_{\pm}(t,\theta), \tilde h_{\pm}(t,\theta')\right] = \pm \pi i \delta'(\theta-\theta')\quad \text{and}\quad [\tilde h_{+}(t,\theta),\tilde h_-(t,\theta')]=0.
\ee

We decompose $\tilde{h}_\pm(t,\theta)$ into Fourier modes

\ben\label{eq:hpmode}
\tilde h_{+}(t,\theta) = \sum_{n=-\infty}^\infty a_{-n}(t) e^{i n \theta}
\een

and

\ben\label{eq:hmmode}
\tilde h_{-}(t,\theta) =  - \sum_{n=-\infty}^\infty b_{n}(t) e^{i n \theta}.
\een

From the constraint equation (\ref{eq:tildehcons}), we see that the zero-modes $a_0$ and $b_0$ are equal up to a sign

\ben
a_0=-b_0=\pi_0.
\een

It follows from equation (\ref{eq:poisson2}) that the Fourier modes $a_n$ and $b_n$ satisfy $U(1)$ \emph{Kac-Moody} algebra

\ben \label{eq:U1KM}
[a_m(t),a_n(t)]={\frac{1}{2}}m\delta_{m+n},\quad [b_m(t),b_n(t)]={\frac{1}{2}}m\delta_{m+n}, \quad \tand \quad [a_m(t),b_n(t)]=0.
\een

Since $\tilde h_\pm(t,\theta)$ are real we have $a_{-n}=a_n^\dagger$ and $b_{-n}=b_n^\dagger$. The Hamiltonian (\ref{eq:Hhtwoboundary2}) in terms of these modes is given by (up to over all constant factors)

\ben
\tilde H = H_+ + H_-
\een

where

\ben
\begin{split}
H_{+} = & \frac{\hbar}{2}a_{0}^2 + \frac{\hbar^2}{3}a_{0}^3 - \frac{\hbar^2}{24}a_{0} + \hbar (1+2\hbar a_0)\sum_{n>0} a_n^\dagger a_n \\
 &+ \hbar^2\sum_{m,n>0} \lb a_{m+n}^\dagger a_m a_n+ h.c. \rb
\end{split}
\een

and $H_-$ has a similar expression in terms of modes $b_n$'s.\\
Since $\pi_0$ commutes with all the $a_n, b_n$ and hence with $\tilde H$, application of $a_n$'s and $b_n$'s cannot change the eigenvalue of $\pi_0$. Therefore the Hilbert space is constructed upon a one parameter family of vacua $\ket{s,s}\equiv \ket s$ where,

\ben
\label{eq:KMprimary}
\begin{split}
   & a_n\ket{s} = 0, \quad b_n\ket{s} = 0 \quad \for\  n>0\\
\tand \quad & a_0\ket{s} = - b_0\ket{s} =\pi_0\ket{s} = s \ket{s}.
\end{split}
\een

Starting with the primary $\ket{s}$ we can now construct a Hilbert space $\cH$ which is a $s$ charged module. Let us denote $\cH_+$ and $\cH_-$ as Hilbert spaces associated with $a$ and $b$ sectors respectively. The commutativity of $a$ and $b$ operators implies that the full Hilbert space is factorizable into $\cH_+$ and $\cH_-$ i.e. $\cH=\cH_+ \otimes \cH_-$.

A generic excited state in $\cH$ is given by

\ben\label{eq:basisstatek}
\ket{\vec k,\vec l} = \prod_{n,m=1}^{\infty} \lb a^\dagger_n\rb^{k_n}\lb b^\dagger_m\rb^{l_m}\ket{s}.
\een

The $\vec k$ and $\vec l$ vectors correspond to excitations in the upper and lower Fermi surfaces. Since $a_n$ and $b_n$ commute, generic excitation $\ket{\vec k, \vec l} \in \cH$ can be written as a direct product of states belonging to the two sectors i.e. $\ket{\vec k, \vec l}=\ket{\vec k} \otimes \ket{\vec l}$.

The excited states in $\cH_+$ are orthogonal with the normalization

\ben\label{eq:knormalization}
\langle {\vec{k'}}|{\vec k}\rangle =z_{\vec k}\delta_{\vec k \vec{k'}}\ \ \text{where}\ z_{\vec{k}}=\prod_j k_j! {\left(\frac{j}{2}\right)}^{k_j}
\een

and has $\pi_0$ eigenvalue $s$. They also satisfy the completeness relation

\ben
\sum_{\vec k}\frac{1}{z_{\vec k}} \ket{\vec k}\bra{\vec k} = {\mathbb{I}}_{\cH_+}
\een
and hence form a basis in $\cH_+$. The particle like excited states $\ket{\vec k}$ in either sectors are eigenstates of the free Hamiltonian of the corresponding sectors

\ben
H^\pm_{\text{free}}\ket{\vec k} = \hbar(1 \pm 2s\hbar)\lb\sum_{n=1}^\infty n k_n\rb \ket{\vec k},
\een

but not an eigenstate of the full Hamiltonian. The interaction Hamiltonian is such that its action on an excited state doesn't change the level of the state. Explicitly stated, the interaction Hamiltonian takes a state $\ket{\vec k}$ to $\ket{\vec{k'}}$ satisfying $\sum_n n k_n =\sum_n n{k'}_n$. The expectation value of $\bar h_+(t,\theta)$ operator in $\ket{\vec k}$ state is $(1/2+\hbar s)$. The quantum dispersion, $\Delta \bar{h}_+$ in $\ket{\vec k}$ state is $O(\hbar)$ and hence a generic $\ket{\vec k}$ state can be interpreted as quantum fluctuations over the ground state.

A generic coherent state in $\cH_+$ can be defined as\footnote{{A rather interesting feature of coherent states written in this form is pointed out by \cite{Dijkgraaf:1992kv, Segal:1985aga, Date:1981qy}. One can show that the inner product between the coherent state (\ref{eq:coherentstate}) and a state lying in the Grassmannian is tau function of the KP hiererchy.}}

\ben\label{eq:coherentstate}
\ket{\t_+} = \exp\lb {\sum_{n=1}^\infty \frac{2\t_{n}^+ a_n^\dagger}{n\hbar}}\rb \ket{s}.
\een

The state $\ket{\t_+}$ is not normalised. The normalization is given by 

\ben
\braket{\tau_+^a}{\tau^b_+} = \exp\lb\sum_n \frac{4\t_{n+}^a\t_{n+}^b}{n\hbar^2}\rb.
\een

The coherent state $\ket{\t_+} $ is an eigenstate of $a_n$ ($\forall\, n>0$) operator with eigenvalue $\t_{n}^+/\hbar$. A coherent state $\ket{\t_+}$ can be expanded in $\ket{\vec k}$ basis in the following way

\ben
\ket {\t_+} = \sum_{\vec k} \frac{\t^+_{\vec k}}{z_{\vec k}}\ket{\vec k}, \quad \where \quad \t^+_{\vec k} = \prod_m \lb\frac{\t^+_{m}}{\hbar}\rb^{k_m}.
\een

The expectation value of $ \bar{h}_+$ operator in a coherent state $\ket {\t_+}$ is given by

\ben
\omega_{\t_+}(z)= \frac{ \bra{\t_+}\frac{\bar h_+(z)}{\pi} \ket{\t_+}}{\braket{\t_+}{\t_+}} =\frac{1}{2\pi} + \frac{s\hbar}{\pi}+\frac{1}{\pi}\sum_{n>0}\t^+_{n}\lb z^n +\frac{1}{z^n}\rb.
\een

Value of $\omega_{\t_+}(z)$ on the unit circle ($|z|=1$) in the complex $z$ plane is given by, 

\ben\label{eq:coherentprofile}
\begin{split}
\omega_{\t_+}(\theta) \equiv \omega_{\t_+}(z=e^{i\theta}) & = \frac{1}{2\pi}  + \frac{s\hbar}{\pi} + \tilde{\omega}_{\t_+}(\theta)\\
\text{where} \quad \tilde{\omega}_{\t_+}(\theta) &=\frac{2}{\pi} 
\sum_{n>0}\t^+_{n} \cos n\theta.
\end{split}
\een

Since the quantum dispersion of $\bar{h}_+$ in a coherent state is zero, we call such states \emph{classical}. 

We set up a map between a state $\ket{\psi} \in \cH_+$ and shape of the upper Fermi surface

\ben\label{eq:maping}
\ket{\psi} \ra \{\bra{\psi}\bar{h}_+(\theta)\ket{\psi}\}.
\een

This maps the following three types of states in $\cH_+$ to three different types of shapes of the upper Fermi surface $\bar h_+$. Such a mapping has been also discussed in \cite{Chattopadhyay:2020rle}. Expectation value of $\bar h_+$ in ground state is given by $\frac12 + s \hbar$ and has zero dispersion. Thus, ground state $\ket s$ corresponds to an overall shift of $\bar h_+$ by an amount $s/N$ over the classical value. Generic \emph{normalised} excited states correspond to ${\cal O}(\hbar)$ ripples on $\bar h_+$. In this case, the expectation value of $\bar{h}_+$ picks up a non-zero dispersion at ${\cal O}(\hbar)$. ${\cal O}(1)$ deformation to the upper Fermi surface $\bar{h}_+$ is mapped to coherent states $\ket{\tau_+}$ in $\cH_+$ as is evident from \ref{eq:coherentprofile}. Here we have assumed $\langle \tau_+|\bar{h}_+(\theta)|\tau_+\rangle$ is a single valued function of $\theta$. An important thing to note here is that the classical deformations do not disturb the quadratic profile of the droplets \emph{i.e} for a given $\theta$, there exists unique values of $h_\pm(\theta)$.

We now consider the mapping between the automodel diagrams and states in the Hilbert space. The automodel diagrams corresponds to

\ben
\bar h_\pm(\theta) = \pm \lb \frac12 +\xi \cos\theta\rb. 
\een

The set of coherent states with $\tau_1=\xi/2$ , $\tau_n = 0$ $\forall n > 1$ are mapped to the automodel diagrams. In particular, the state corresponding to the limit shape is given by

\ben
|\tau* \rangle = \text{exp}\left(\frac{a_{1}^{\dagger}\xi}{\hbar}\right) |0\rangle. \quad
\een

Thus Plancherel growth of Young diagrams is mapped to evolution of classical states \cite{Chattopadhyay:2020rle}. One can also compute the transition amplitude of such evolution process. The ground state $\xi=0$ is an eigenstate of the Hamiltonian and hence its evolution is trivial. Therefore, we take our initial state as

\ben
\ket{\tau_i} = \exp{2a_1^\dagger}\ket{s}.
\een

Such state corresponds to a droplet with $\frac12 +\hbar \cos\theta$. The transition amplitude for evolution from this state to a automodel state in time $T$ is therefore given by \cite{Chattopadhyay:2020rle}

\ben
\mathbb{T} \sim \sum_R\lb \frac{\dim R}{k!}\rb^2 \lb \frac{\xi}{\hbar}\rb^{|R|} e^{i T \hbar C_2(R)}
\een

where $C_2(R)$ is given by

\ben
C_{2}(R) = N \sum_{i=1} l_{i} + \sum_{i=1}l_i(l_i - 2 i + 1)
\een

Here $l_i$ is the number of boxes in the $i$th row of the Young diagram $R$.

Excitations over this state correspond to $O(\hbar)$ fluctuations of the limit shape. Consider the states

\ben\label{state:coh}
\text{exp}\left( \frac{a_{1}^{\dagger}\xi}{\hbar} + \sum_{n>1}\frac{2\alpha_{n} a_{n}^{\dagger}}{\sqrt{n}} \right) |0\rangle
\een

The expectation value of $\bar h_+(\theta)$ in such a state gives

\ben\label{expect:coh}
\frac{1}{2} + \xi \cos{\theta} + 2\hbar \sum_{n>1}\sqrt{n}\alpha_{n}\cos{n\theta}
\een

which is essentially the result (\ref{eq:flucLS}) of Ivanov and Olshanki \cite{2003math.4010I}.
