---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-007-35-the-triangle-inequality
section_title: "The triangle inequality"
section_number: 3.5
pages: 13-15
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.967
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:triangle}
An interesting additional fact about circuit imbalances is that the logarithm of the weights satisfy the triangle inequality; this was shown in \cite{DHNV20}. Here, we formulate a stronger version and give a simpler proof. Throughout, we assume that ${\cal M}(W)$ is non-separable. Thus, according to Proposition~\ref{prop:conn}, for any $i,j\in [n]$ there is a circuit $C\in \circuits_W$ with $i,j\in C$.
\begin{theorem}\label{thm:imbalance_triangle_inequality}
Let $W\subseteq \R^n$ be a linear space, and assume ${\cal M}(W)$ is non-separable. Then, 
  \begin{enumerate}[(i)]
  \item\label{i:set_triangle_inequality} for any distinct $i,j,k\in [n]$,
  $\KK_{ij}^W \subseteq \KK_{ik}^W \cdot\KK_{kj}^W$; and 
  \item \label{i:triangle} for any distinct $i,j,k\in [n]$,
  $\Le_{ij} \leq \Le_{ik}\cdot \Le_{kj}$.
  \end{enumerate}
  \end{theorem}

The proof relies on the following technical lemma that analyzes the scenario when almost all vectors in $W$ are elementary.
\begin{lemma}
  \label{lem:helper_triangle}
   Let $W \subseteq \R^n$ be a subspace s.t.\ $\mathcal{M}(W)$ is non-separable. 
  \begin{enumerate}[(i)]
  \item \label{it:prop_helper_second} If $\EE(W) = \set{g \in W\setminus\{0\} : \supp(g)\neq [n]}$, then $\KK_{ij}^W \subseteq \KK_{ik}^W\cdot \KK_{kj}^W$. 
    \item \label{it:prop_helper_first} If there exists $g \in \EE(W)$ such that $|\supp(g)| = n - 1$, then 
$$\EE(W) = \set{g \in W\setminus\{0\} : \supp(g)\neq [n]}\, .$$
\end{enumerate}
\end{lemma}
\begin{proof}
  For part \ref{it:prop_helper_second}, 
let $\delta \in \KK_{ij}^W$ and let $g \in \EE(W)$ such that $\{i,j\} \subset \supp(g)$ and $|g_j/g_i| = \delta$. If $k \in \supp(g)$, then $|g_j/g_i| = |g_k/g_i| \cdot |g_j/g_k|$ shows the claim.

Assume $k\notin \supp(g)$, and pick $h \in \EE(W)$ such that $\{i,k\} \subset \supp(h)$ and let $\tilde h = h_jg - g_jh$; such a $h$ exists by Proposition~\ref{prop:conn}. Then $\tilde h_j = 0$ and $\tilde h_k \neq 0$, so $\tilde h \in \EE(W)$ by the assumption. If $\tilde h_i = 0$ then $h_jg_i = g_jh_i$ and so $\{i,j,k\} \subset \supp(h)$ with $h_j/h_i = g_j/g_i$, therefore $h$ certifies the statement as $|h_j/h_i| = |h_k/h_i| \cdot |h_j/h_k|$.
Otherwise, $\tilde h_i \neq 0$ and $h':= \tilde h_ig - g_i\tilde h$ fulfills $h' \in \EE(W)$ as $h'_i = 0$, $\{j, k\} \subset \supp(h')$.
Now, using that $\tilde h_j = 0$ and $g_k = 0$ it is easy to see that
\begin{equation}
  \left|\frac{\tilde h_k}{\tilde h_i}\cdot \frac{h'_j}{h'_k} \right|
  = \left| \frac{\tilde h_k}{\tilde h_i}\cdot \frac{\tilde h_i g_j - g_i \tilde h_j}{\tilde h_i g_k - g_i\tilde h_k} \right|
  =  \left| \frac{\tilde h_k}{\tilde h_i}\cdot \frac{\tilde h_i g_j}{g_i\tilde h_k} \right|
   = \left| \frac{g_j}{g_i} \right| \, .
\end{equation}
We now turn to part \ref{it:prop_helper_first}. Since there exists $g \in \EE(W)$ with $\supp(g) \neq n$, we cannot have $[n] \in \circuits(W)$. 

Let $g \in \EE(W)$ and $i \in [n]$ such that $\supp(g) = [n] \setminus \set{i}$. Consider any $h \in W$, $\supp(h) \neq \supp(g)$ such that $\supp(h) \neq [n]$. If $h \notin \EE(W)$ there exists $\ell \in \EE(W)$ such that $\supp(\ell) \subsetneq \supp(h)$. We must have $i \in \supp(\ell)$, since $\supp(\ell)\setminus \supp(g)\neq \emptyset$. Then $\tilde h: = h_i\ell - \ell_ih$ fulfills $\tilde h\neq 0$, $\tilde h_i = 0$ and $\supp(\tilde h) \subsetneq [n]\setminus \set{i}$, a contradiction to $g \in \EE(W)$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:imbalance_triangle_inequality}]
  \label{proof:lem:imbalance_triangle_inequality}
Part \ref{i:triangle} immediately follows from part \ref{i:set_triangle_inequality}, when taking
 $C \in \circuits_W$ such that $|g_j^C/g_i^C| = \Le_{ij}$. We now prove part \ref{i:set_triangle_inequality}.
 
 Let $\delta \in \KK_{ij}^W$ and $C\in \circuits_W$ such that $i,j\in C$ and for $g=g^C$, $|g_j/g_i| = \delta$. If $k \in C$ then clearly $|g_j/g_i| = |g_k/g_i| \cdot |g_j/g_k| \in \KK_{ik}^W\cdot \KK_{kj}^W$. Otherwise,
 let us select $C'\in \circuits_W$ such that $i,k\in C'$, and $|C\cup C'|$ is minimal. Let $h=g^{C'}$ and $J=C'\setminus (C\cup\{k\})$.
 
\begin{claim}
Let $G = (C \cup C') \setminus J$. Then for the space
$\hat W := \pi_{G}(W_{C \cup C'})$ we have that $g_G, h_G \in \EE(\hat W)$. 
\end{claim}
\begin{proof}
The statement that $h_G \in \EE(\hat W)$ is clear as $h_{C \cup C'} \in \EE (W_{C \cup C'})$ and the variables we project out $J$ fulfill $J \subseteq \supp(h)$.
For the statement on $g_G$ assume that there exists $\hat g \in \EE(\hat W)$ such that $\supp(\hat g) \subsetneq \supp(g_G)$. Then there exists a lift  $\tilde g \in \EE(W_{C \cup C'})$ of $\hat g$ and some $\ell \in J$ such that $\ell \in \supp(\tilde g)$; note also that $\tilde g_k = g_k = 0$. The vector $\hat h := h_\ell \tilde g - \tilde g_\ell h$ fulfills $\ell \notin \supp(\hat h)$ and $k \in \supp(\hat h)$.

Now pick any circuit $\tilde h \in \EE(\hat W)$ such that $k \in \supp(\tilde h)$ and $\supp(\tilde h) \subseteq \supp(\hat h)$. 
Note that $J \cup \{k\}$ is independent, as $J \cup \{k\} \subseteq C' \setminus \{i\} \subsetneq C'$. Therefore, $\supp(\tilde h) \cap \supp(g) \neq \emptyset$.
Hence, for $T := C \cup \supp(\tilde h)$ we have that $\mathcal M(W_T)$ is non-separable. In particular there exists a circuit $h' \in \EE(W_T)$ such that $i,k \in \supp(h')$. As $T \subseteq (C \cup C')\setminus \{\ell\}$, this is a contradiction to the minimal choice of $C'$.  
\end{proof}
As $\supp(h_D) \cup \supp(g_D) = D$ and $\supp(h_D) \cap \supp(g_D) \neq \emptyset$ we have that $\EE(W')$ is non-separable. Further $|\supp(g_D)| = |D| - 1$, so we can apply Lemma~\ref{lem:helper_triangle} to learn $\delta \in \KK_{ij}^{W'} \subseteq \KK_{ik}^{W'} \cdot \KK_{kj}^{W'}$. We can conclude   $\delta \in \KK_{ik}^W \cdot \KK_{kj}^W$ from Lemma~\ref{lem:circuit_minors}.
\end{proof}

If $\Le_W=1$, then the reverse inclusion 
$ \KK_{ik}^W \cdot \KK_{kj}^W \subseteq \KK_{ij}^W$ trivially holds, since 1 is the only element in these sets. In Proposition~\ref{prop:reverse-kappa-1}, we give a necessary and sufficient condition for $\KK_{ij}^W= \KK_{ik}^W \cdot \KK_{kj}^W$.

One may ask under which circumstances an element $\alpha \in \KK_{ik}^W\cdot \KK_{kj}^W$ is also contained in $\KK_{ij}^W$. We give a partial answer by stating a sufficient condition in a  restrictive setting. For a basis $B$ of ${\cal M}(W)$, recall $\EE_B(W^\perp)$ from Lemma~\ref{lem:basis_circuits}. Then, Lemmas~\ref{lem:basis_circuits} and \ref{lem:dual-circuit} together imply:

\begin{lemma}
Given a basis $B \subseteq [n]$ in $\mathcal{M}(W)$ and $g,h \in \EE_B \subseteq \EE(W^\perp)$ such that $i \in \supp(g) \cap B$, $j \in \supp(h) \cap B$ and $k \in \supp(g) \cap \supp(h)$.
Then $|h_j/h_k|\cdot |g_k/g_i| \in \KK_{ij}^W$.
\end{lemma}
