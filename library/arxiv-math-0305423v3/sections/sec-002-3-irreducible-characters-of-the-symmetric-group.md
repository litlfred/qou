---
doc_id: arxiv-math-0305423v3
doc_title: "Stein's method and Plancherel measure of the symmetric group"
section_id: sec-002-3-irreducible-characters-of-the-symmetric-group
section_title: "Irreducible characters of the symmetric group"
section_number: 3
pages: 8-10
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.95
doc_brief: "Stein's method and Plancherel measure of the symmetric group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
\label{repreview}

	This section collects properties we will use about
	characters of irreducible representations of the symmetric
	group. For more background on this topic, see the book
	\cite{Sa}. Lemmas \ref{orth1}, \ref{mult}, and $\ref{real}$ are
	well known. Lemma \ref{countsol} is known but not well
	known. Lemmas \ref{induced}, \ref{parents} are elementary
	consequences of known facts but perhaps new.

	Throughout $\overline{z}$ denotes the complex conjugate of $z$, and $Irr(G)$ denotes the set of characters of irreducible representations of a finite group $G$. The notation $dim(\chi)$ denotes the dimension of the representation with character $\chi$.

\begin{lemma} \label{orth1} Let $C(g)$ be the conjugacy class of $G$ containing the element $g$. Then for $g \in G$, \[ \sum_{\chi \in Irr(G)} \chi(g) \overline{\chi(h)} \] is equal to $\frac{|G|}{|C(g)|}$ if $h,g$ are conjugate and is $0$ otherwise.
\end{lemma}

\begin{lemma} \label{mult} Let $\nu$ be an irreducible character of a finite group $G$, and $\chi$ any character of $G$. Then the multiplicity of $\nu$ in $\chi$ is equal to \[ \frac{1}{|G|} \sum_{g \in G} \nu(g) \overline{\chi(g)}. \] \end{lemma}

\begin{lemma} \label{real} The irreducible characters of the symmetric group $S_n$ are real valued. \end{lemma}

	Note that Lemma \ref{countsol} generalizes Lemma \ref{orth1}. 

\begin{lemma} (\cite{Sta}, Exercise 7.67) \label{countsol} Let $G$ be a finite group
 with conjugacy classes $C_1, \cdots, C_r$. Let $C_k$ be the conjugacy class of an element $w \in G$. Then the number of
 $m$-tuples $(g_1,\cdots,g_m) \in G^m$ such that $g_j \in C_{i_j}$ and $g_1 \cdots g_m=w$ is \[
 \frac{\prod_{j=1}^m |C_{i_j}|}{|G|} \sum_{\chi \in Irr(G)}
 \frac{1}{dim(\chi)^{m-1}} \chi(C_{i_1}) \cdots \chi(C_{i_m})
 \overline{\chi(C_k)} .\] \end{lemma}

	For the application of Stein's method we shall only need the case $k=1$ of Lemmas \ref{induced} and \ref{parents}.

\begin{lemma} \label{induced} Let $\chi$ be a character of the symmetric group $S_n$. Let $n_i(g)$ denote the number of cycles of $g$ of length $i$. Let $Res,Ind$ denote the operations of restriction and induction. Then for $k \geq 1$, \[ Res^{S_{n+k}}_{S_n}(Ind_{S_n}^{S_{n+k}}(\chi)) [g] = \chi(g) (n_1(g)+1) \cdots (n_1(g)+k).\]
\[ Ind_{S_{n-k}}^{S_n}(Res^{S_n}_{S_{n-k}}(\chi)) [g] = \chi(g) (n_1(g)) \cdots (n_1(g)-k+1).\]
\end{lemma}

\begin{proof} Let us prove the first assertion, the second being similar. It is well known (\cite{Sa}) that if $H$ is a subgroup of a finite group $G$, and $\chi$ is a character of $H$, then \[ Ind_H^G(\chi)[g] = \frac{1}{|H|} \sum_{t \in G \atop t^{-1}gt \in H} \chi(t^{-1}gt).\] Now apply this to $H=S_n$, $G=S_{n+k}$, using the fact that if two elements of $S_n$ are conjugate by an element of $S_{n+k}$, they are conjugate in $S_n$. Letting $Cent_G(g)$ denote the centralizer size of an element $g$ in a group $G$, it follows that the induced character at $g \in S_n$ is equal to \[ \chi(g) \frac{|Cent_{S_{n+k}}(g)|} {|Cent_{S_{n}}(g)|} = \chi(g) (n_1(g)+1) \cdots (n_1(g)+k).\] Here we have used the fact that $\prod_j j^{n_j} n_j!$ is the centralizer size in $S_{\sum_j jn_j}$ of an element with $n_j$ cycles of length $j$. \end{proof}

	In Lemma \ref{parents} we use the notation that $dim(\mu/\tau)$ is the number of paths in the Young lattice from $\tau$ to $\mu$ (or equivalently the number of ways of adding boxes one at a time to get from $\tau$ to $\mu$). We let $|\lambda|$ denote the size of a partition.

\begin{lemma} \label{parents} Let $\mu,\lambda$ be partitions of $n$. Let $n_1(g)$ denote the number of fixed points of a permutation $g$. Then \[ \sum_{\tau \atop |\tau|=n+k} dim(\tau / \lambda) dim(\tau / \mu) = \frac{1}{n!} \sum_{g \in S_n} \chi^{\mu}(g) \chi^{\lambda}(g) (n_1(g)+1) \cdots (n_1(g)+k)\] 
\[ \sum_{\tau \atop |\tau|=n-k} dim(\lambda / \tau) dim(\mu / \tau) = \frac{1}{n!} \sum_{g \in S_n} \chi^{\mu}(g) \chi^{\lambda}(g) (n_1(g)) \cdots (n_1(g)-k+1).\]
\end{lemma}

\begin{proof} We prove only the first part as the second part is similar. Both sides of this equation enumerate the multiplicity of $\mu$ in the representation $Res^{S_{n+k}}_{S_n}(Ind_{S_n}^{S_{n+k}}(\lambda))$. This multiplicity is equal to the left hand side by the branching rules for induction and restriction in the symmetric group (Theorem 2.8.3 in \cite {Sa}). That the right hand side computes the same multiplicity follows from Lemmas \ref{mult}, \ref{real}, and \ref{induced}. \end{proof}

	Note that as a special case of Lemma \ref{parents}, \[ |parents(\mu,\lambda)| = \frac{1}{n!} \sum_{g \in S_n} \chi^{\mu}(g) \chi^{\lambda}(g) (n_1(g)+1).\]
