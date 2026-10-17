---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-018-52-fusion-homomorphisms
section_title: "Fusion homomorphisms"
section_number: 5.2
pages: 27-28
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.968
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
We write $[\cat{C}]$ for the Grothendieck ring of a fusion category. The following property of quantum dimensions is well-known.
\begin{lem} Given a pivotal structure $\gamma$ on a fusion category $\cat{C}$, the quantum dimension map $\dim_{\gamma} \colon [\cat{C}] \rightarrow
\mathbb{C}$ which sends $[V] \mapsto \dim_\gamma (V)$ satisfies the following:
 \begin{itemize}
  \item It is a ring homomorphism,
  \item $\dim_\gamma [X_i] \dim_\gamma [X_i^*] = d_{\{i,i^*\}}$ for all
simple objects $X_i$.
 \end{itemize}
\end{lem}
This motivates the following definition.
\begin{defn} Let $\cat{C}$ be a fusion category. We call a function $f \colon [\cat{C}] \rightarrow \mathbb{C}$ a {\em fusion homomorphism} if it is a ring homomorphism and if $f[X_i]
f[X_i^*] = d_{\{i,i^*\}}$ for all simple objects $X_i$. 
\end{defn}
For a fusion category $\cat{C}$, it is interesting to consider whether the injective map
\[
 \text{Pivotal structures}(\cat{C}) \rightarrow \{\text{Fusion homomorphisms $f : [\cat{C}] \rightarrow \mathbb{C}$}\}
\]
is also surjective. The following case is instructive. Fix a finite group $G$.
\begin{prop} The pivotal structures on $\Rep(G)$ are in 1-1 correspondence
with the fusion homomorphisms from $[\Rep(G)]$ to $\mathbb{C}$.
\end{prop}
\begin{proof} We have
 \begin{align*}
  \text{Pivotal structures}(\Rep(G)) & \cong \Aut_\otimes(\id) \\
   & \cong Z(G) \\
   & = \{ g \in G \colon |\Tr_{V_i} (g) | = \dim V_i \text{ for all
irreducibles $V_i$}\} \\
   & \cong \{\text{Fusion homomorphisms } f \colon [\Rep(G)] \rightarrow
\mathbb{C} \}.
  \end{align*}
The first isomorphism uses the fact the fact that $\Rep(G)$ comes with a canonical pivotal structure, and that in general the set of pivotal structures is a torsor for $\Aut_\otimes (\id_C)$. The second isomorphism is a result
of M\"{u}ger \cite{muger2004center}. The equality in the third
line is a basic result of representation theory \cite[Cor 2.28]{isaacs1976-character}. The final isomorphism uses two facts. Firstly,
every ring homomorphism
 \[
  [\Rep(G)] \rightarrow \mathbb{C}
 \]
must take the form $V \mapsto \Tr_V(g)$ for some fixed $g \in G$ ---
because a character like this certainly {\em is} a ring homomorphism,
and there are as many such distinct characters as there are conjugacy
classes in the group, which must exhaust all the ring homomorphisms
since $[\Rep(G)]_\mathbb{C}$ is isomorphic to the space of functions
on the conjugacy classes. Secondly, in $\Rep(G)$ the paired dimensions
$d_{\{i,i^*\}}$ are just $\dim(V_i)^2$, so that a fusion homomorphism
must satisfy $| f(V_i) | = \dim V_i$.
\end{proof}
