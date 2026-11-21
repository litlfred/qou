---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED"
section_id: sec-002-2-free-resolutions-of-a-adic-systems
section_title: "Free Resolutions of a-Adic Systems"
section_number: 2
pages: 7-9
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.94
doc_brief: "FLATNESS AND COMPLETION REVISITED — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
\label{sec:res-adic-sys}

As before, $A$ is a commutative ring and $\a$ is an ideal in it. 

Let us recall some definitions 
from our paper \cite{Ye1}. Let $Z$ be a set and let $N$ be an 
$A$-module. The set of all functions $f : Z \to N$ is denoted by 
$\opn{F}(Z, N)$. 
It is an $A$-module in the obvious way. The {\em support} of a  function 
$f : Z \to N$ is the set 
$\{ z \in Z \mid f(z) \neq 0 \}$.  
We denote by 
$\opn{F}_{\mrm{fin}}(Z, N)$ 
the submodule of $\opn{F}(Z, N)$ consisting of finite support functions.
For $N = A$, the $A$-module 
$\opn{F}_{\mrm{fin}}(Z, A)$
is free, with basis the collection 
$\{ \de_z \}_{z \in Z}$ of delta functions.
For every $A$-module $N$ there are canonical isomorphisms
\begin{equation} \label{eqn:73}
\opn{F}_{\mrm{fin}}(Z, A) \ot_A N \cong 
\opn{F}_{\mrm{fin}}(Z, N) \cong 
\bigoplus_{z \in Z} \, N . 
\end{equation}

Given a set $Z$, we have an $\a$-adic system of $A$-modules 
$\bigl\{ \opn{F}_{\mrm{fin}}(Z, A_k) \bigr\}_{k \in \N}$. 
See Definition \ref{dfn:22} regarding morphisms of $\a$-adic systems.  

\begin{dfn} \label{dfn:20}
An $\a$-adic system of $A$-modules $\bsym{P}$
is said to be a {\em free $\a$-adic system} if there is an 
isomorphism of $\a$-adic systems 
\[ \bsym{P} \cong \bigl\{ \opn{F}_{\mrm{fin}}(Z, A_k) \bigr\}_{k \in \N}  \]
for some set $Z$.
\end{dfn}

\begin{dfn} \label{dfn:70}
Let  $\bsym{M} = \{ M_k \}_{k \in \N}$ be an $\a$-adic system of 
$A$-modules. A {\em free resolution of $\bsym{M}$} is a  diagram of $\a$-adic 
systems
\[ \cdots \to \bsym{P}^{-2} \xar{\bsym{\d}^{-1}} \bsym{P}^{-1} 
\xar{\bsym{\d}^0} \bsym{P}^{0} 
\xar{\bsym{\eta}} \bsym{M} \to 0 , \]
such that each 
$\bsym{P}^i = \{ P_k^i \}_{k \in \N}$ is a free $\a$-adic system, and for every 
$k$ the diagram of $A$-modules 
\begin{equation} \label{eqn:115}
\cdots \to P_k^{-2} \xar{\d^{-1}_k} P_k^{-1} \xar{\d^0_k} P_k^{0} 
\xar{\eta_k} M_k \to 0 
\end{equation}
is an exact sequence, i.e.\ it is a free resolution of the $A_k$-module 
$M_k$. We denote this resolution by 
$\bsym{\eta} : \bsym{P} \to \bsym{M}$. 
\end{dfn}

In other words, a free resolution of $\bsym{M} = \{ M_k \}_{k \in \N}$ is a 
commutative diagram 
\[ \UseTips \xymatrix @C=5ex @R=4ex {
&
\vdots 
\ar[d]
&
\vdots 
\ar[d]
&
\vdots 
\ar[d]
&
\vdots 
\ar[d]
\\
\cdots 
\ar[r]
&
P_1^{-2}
\ar[r]
\ar[d]
&
P_1^{-1}
\ar[r]
\ar[d]
&
P_1^{0}
\ar[r]
\ar[d]
&
M_1^{}
\ar[r]
\ar[d]
&
0
\\
\cdots 
\ar[r]
&
P_0^{-2}
\ar[r]
&
P_0^{-1}
\ar[r]
&
P_0^{0}
\ar[r]
&
M_0^{}
\ar[r]
&
0
} \]
in $\cat{Mod} A$, where 
$P^{-i}_k \cong \opn{F}_{\mrm{fin}}(Z_i, A_k)$ for some sets $Z_i$,
the vertical homomorphisms come from the ring surjections 
$A_{k + 1} \to A_k$, and the rows are exact. 

For each $k \geq 0$ let $P_k$ be the complex of free $A_k$-modules 
\begin{equation} \label{eqn:320}
P_k := \bigl( \cdots \to P_k^{-2} \xar{\d_k^{-1}} P_k^{-1} 
\xar{\d_k^0} P_k^{0} \to 0  \to \cdots \bigr) 
\end{equation}
that occurs as part of the resolution (\ref{eqn:115}).
So there is a quasi-isomorphic of complexes $\eta_k : P_k \to M_k$.

\begin{lem} \label{lem:40}
Let $B$ be a commutative ring, with nilpotent ideal $\b$, and 
let $M$ be a $B$-module. Define the ring 
$\bar{B} := B / \b$ and the $\bar{B}$-module 
$\bar{M} := \bar{B} \ot_B M$. 
Suppose 
\begin{equation} \label{eqn:40}
\cdots \to \bar{P}^{-2} \xar{\bar{\d}^{-1}} \bar{P}^{-1} \xar{\bar{\d}^0}  
\bar{P}^{0} \xar{\bar{\eta}} \bar{M} \to 0 
\end{equation}
is a free resolution of the module $\bar{M}$ over the ring $\bar{B}$,
such that for each $i \geq 0$ we have 
$\bar{P}^{-i} = \opn{F}_{\mrm{fin}}(Z_i, \bar{B})$
for some set $Z_i$. 
Also suppose that 
$\opn{Tor}^{B}_i(\bar{B}, M) = 0$ for all $i > 0$. 

Then the resolution \tup{(\ref{eqn:40})} can be lifted to $B$. Namely, there is 
a free resolution
\begin{equation} \label{eqn:41}
\cdots \to P^{-2} \xar{\d^{-1}} P^{-1} \xar{\d^0}  
P^{0} \xar{\eta} M \to 0 
\end{equation}
of the $B$-module $M$, such that 
$P^{-i} = \opn{F}_{\mrm{fin}}(Z_i, B)$
for every $i$, and the sequence \tup{(\ref{eqn:40})} is gotten from the 
sequence \tup{(\ref{eqn:41})} by applying the functor 
$\bar{B} \ot_B -$. 
\end{lem}

\begin{proof}
The proof is by induction on $i = 0, 1, 2, \ldots$.

We start with $i = 0$. For each $z \in Z_0$, we choose an arbitrary element
$m_z \in M$ lifting the element $\bar{\eta}(\de_z) \in \bar{M}$. 
This determines a homomorphism of $B$-modules 
\[ \eta : \opn{F}_{\mrm{fin}}(Z_0, B) \to M . \]
The Nakayama Lemma (in its nilpotent version) says that $\eta$ is surjective. 

Now we take some $i \geq 0$, and we assume that a partial free resolution 
\begin{equation} \label{eqn:55}
P^{-i} \xar{\d^{-i + 1}} P^{-i + 1} \to \cdots \xar{\d^0} P^{0} 
\xar{\eta} M \to 0 
\end{equation}
was found, lifting 
\begin{equation} \label{eqn:56}
\bar{P}^{-i} \xar{\bar{\d}^{-i + 1}} \bar{P}^{-i + 1} \to \cdots 
\xar{\bar{\d}^0} \bar{P}^{0} \xar{\bar{\eta}} \bar{M} \to 0 \, ; 
\end{equation}
namely the sequence (\ref{eqn:56}) is gotten from (\ref{eqn:55}) by the 
operation $\bar{B} \ot_B -$. 
Define the modules $L^{-i}$ and $\bar{L}^{-i}$ to be the submodules of 
$P^{-i}$ and $\bar{P}^{-i}$ respectively that make the sequences 
\begin{equation} \label{eqn:57}
0 \to L^{-i} \to P^{-i} \xar{\d^{-i + 1}} P^{-i + 1} \to \cdots \xar{\d^0} 
P^{0} \xar{\eta} M \to 0 
\end{equation}
and 
\begin{equation} \label{eqn:204} 
0 \to \bar{L}^{-i} \to 
\bar{P}^{-i} \xar{\bar{\d}^{-i + 1}} \bar{P}^{-i + 1} \to \cdots 
\xar{\bar{\d}^0} \bar{P}^{0} \xar{\bar{\eta}} \bar{M} \to 0  
\end{equation}
exact. There is a homomorphism 
$\phi : L^{-i} \to \bar{L}^{-i}$ 
that is induced from the surjection $P^{-i} \to \bar{P}^{-i}$.

We are given that the $B$-modules $M, P^0, \ldots, P^{-i}$ satisfy 
$\opn{Tor}^{B}_j(\bar{B}, -) = 0$
for every $j > 0$. By the usual syzygy argument this is also satisfied by 
$L^{-i}$. Therefore the sequence gotten 
by applying $\bar{B} \ot_B - $ to the exact sequence (\ref{eqn:57}) remains 
exact, and thus it is isomorphic to the sequence (\ref{eqn:204}). 
This implies that the homomorphism 
$\bar{B} \ot_B L^{-i} \to \bar{L}^{-i}$ is bijective; and hence 
$\phi : L^{-i} \to \bar{L}^{-i}$ is surjective. 
As before, using the Nakayama Lemma, we can lift the given surjection 
\[ \bar{\d}^{-i} : \bar{P}^{-i - 1} = \opn{F}_{\mrm{fin}}(Z_{i + 1}, \bar{B}) 
\to \bar{L}^{-i} \]
to a surjection
\[ \d^{-i} : P^{-i - 1} = \opn{F}_{\mrm{fin}}(Z_{i + 1}, B) \to L^{-i} .  \]
\end{proof}

\begin{thm} \label{thm:164}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and let 
$\bsym{M} = \{ M_k \}_{k \in \N}$ be an $\a$-adic system of 
$A$-modules. 
The following conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} The $\a$-adic system $\bsym{M}$ admits a free resolution. 
\rmitem{ii} For every $k \geq 0$ and $i > 0$, the module 
$\opn{Tor}^{A_{k + 1}}_i(A_{k}, M_{k + 1})$ vanishes.  
\end{enumerate}
\end{thm}

\begin{proof}
(i) $\Rightarrow$ (ii): Assume $\bsym{M}$ admits a free 
resolution $\bsym{\eta} : \bsym{P} \to \bsym{M}$. We can calculate 
$\opn{Tor}^{A_{k + 1}}_i(A_{k}, M_{k + 1})$
using the free resolution 
$\eta_{k + 1} : P_{k + 1} \to M_{k + 1}$;
see formula (\ref{eqn:320}). Now the complex
$A_k \ot_{A_{k + 1}} P_{k + 1}$ 
is isomorphic to the complex $P_k$, and therefore 
\[ \opn{H}^{-i}(A_k \ot_{A_{k + 1}} P_{k + 1}) = 0 \]
for all $i > 0$. 

\medskip \noindent
(ii) $\Rightarrow$ (i): 
The proof is by induction on $k$. For $k = 0$ we choose a free resolution 
\[ \cdots \to P_0^{-2} \xar{\d^{-1}_0} P_0^{-1} \xar{\d^0_0} P_0^{0} 
\xar{\eta_0} M_0 \to 0 \]
of the $A_0$-module $M_0$,
where 
$P^{-i}_0 = \opn{F}_{\mrm{fin}}(Z_i, A_0)$ for some sets $Z_i$.
 
Now assume that for $k \geq 0$ we found a free resolution of the truncated 
$\a$-adic system $\{ M_{k'} \}_{ 0 \leq k' \leq k}$. Let 
$B := A_{k + 1}$ and $\bar{B} := A_{k}$. Consider the free resolution 
\[ \cdots \to P_k^{-2} \xar{\d^{-1}_k} P_k^{-1} \xar{\d^0_k} P_k^{0} 
\xar{\eta_k} M_k \to 0 \]


over the ring $\bar{B}$. By Lemma \ref{lem:40} this resolution can be lifted to 
a free resolution of $M_{k + 1}$ over ring $B$, with the same indexing sets 
$Z_{0},  Z_{1}, \ldots$. 
\end{proof}

The theorem immediately implies:

\begin{cor} \label{cor:290}
If $\bsym{M}$ is a flat $\a$-adic system, then it has a free resolution. 
\end{cor}
