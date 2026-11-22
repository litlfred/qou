---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-009-26-algebras-over-a-closed-interval
section_title: "Algebras over a closed interval"
section_number: 2.6
pages: 30-32
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.971
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
\begin{definition}[$\Ass^{\sf RL}$]\label{Assoc}
Let $\Ass^{\sf RL}$ denote an $\infty$-operad corepresenting triples $(A;Q,P)$ consisting of an associative algebra together with a unital left and a unital right module.  
Specifically, it is a unital multi-category whose space of colors is the three-element set $\{M, R, L\}$, and with spaces of multi-morphisms given as follows.  Let $I\xra{\sigma}\{M,R,L\}$ be a map from a finite set.
\begin{itemize}
\item $\Ass^{\sf RL}(\sigma, M)$ is the set of linear orders on $I$ for which no element is related to an element of $\sigma^{-1}(\{R,L\})$.
In other words, should $\sigma^{-1}(\{R,L\})$ be empty, then there is one multi-morphism from $\sigma$ to $M$ for each linear order on $\sigma^{-1}(M)$; should $\sigma^{-1}(\{R,L\})$ not be empty, then there are no multi-morphisms from $\sigma$ to $M$. 


\item $\Ass^{\sf RL}(\sigma, L)$ is the set of linear orders on $I$ for which each element of $\sigma^{-1}(L)$ is a minimum, and no element is related to an element of $\sigma^{-1}(R)$.  
In other words, should $\sigma^{-1}(\{R\})$ be empty and $\sigma^{-1}(\{L\})$ have cardinality at most $1$, then there is one multi-morphism from $\sigma$ to $M$ for each linear order on $\sigma^{-1}(M)$;  should $\sigma^{-1}(\{R\})$ not be empty or $\sigma^{-1}(\{L\})$ have cardinality greater than $1$, then there are no multi-morphisms from $\sigma$ to $M$. 


\item $\Ass^{\sf RL}(\sigma, R)$ is the set of linear orders on $I$ for which each element of $\sigma^{-1}(R)$ is a maximum, and no element is related to an element of $\sigma^{-1}(L)$.
In other words, should $\sigma^{-1}(\{L\})$ be empty and $\sigma^{-1}(\{R\})$ have cardinality at most $1$, then there is one multi-morphism from $\sigma$ to $M$ for each linear order on $\sigma^{-1}(M)$;  should $\sigma^{-1}(\{L\})$ not be empty or $\sigma^{-1}(\{R\})$ have cardinality greater than $1$, then there are no multi-morphisms from $\sigma$ to $M$. 


\end{itemize}
Composition of multi-morphisms is given by concatenating linear orders.  

\end{definition}

Consider the oriented $1$-manifold with boundary $[-1,1]$, which is the closed interval, that we regard as a structured stratified space in the sense of~\cite{aft1}.  
Taking connected components depicts a map of symmetric monoidal $\infty$-categories
\[
[-]\colon \diskd^{\sf or}_1 \longrightarrow {\sf Env}\bigl(\Ass^{\sf RL}\bigr)
\]
to the symmetric monoidal envelope,
where $[\RR] = M$, $[\RR_{\geq 0}] = L$, and $[\RR_{\leq 0}] = R$.  

\begin{observation}\label{disk-assoc}
The symmetric monoidal functor $\diskd^{ \partial, \sf or}_1 \xra{[-]}{\sf Env}\bigl(\Ass^{\sf RL}\bigr)$ factors as an equivalence of symmetric monoidal $\infty$-categories:
\begin{equation}\label{disk-comb}
\disk^{\partial, \sf or}_1  \xra{~\simeq~}  {\sf Env}\bigl(\Ass^{\sf RL}\bigr)
\end{equation}
-- this follows by inspecting the morphism spaces of the $\infty$-category $\disk^{\partial, \sf or}_1$, which are discrete.
\end{observation}

\begin{observation}\label{interval-assoc}
Consider the ordinary category $\sO^{\sf RL}$ for which an object is a linearly ordered finite set $(I,\leq)$ together with a pair of disjoint subsets $R\subset I \supset L$ for which each element of $R$ is a minimum and each element of $L$ is a maximum, and for which a morphism $(I,\leq, R,L)\to (I',\leq',R',L')$ is an order preserving map $I\xra{f} I'$ for which $f(R\sqcup L)\subset R'\sqcup L'$.  
(Note that the cardinality of each of $L$ and of $R$ is at most one.)
Concatenating linear orders makes $\sO^{\sf RL}$ into a multi-category, and it is equipped with a canonical maps of operads to ${\sf Env}\bigl(\Ass^{\sf RL}\bigr)$.  
By inspection, the equivalence~(\ref{disk-comb}) of Observation~\ref{disk-assoc} lifts to an equivalence of $\infty$-operads, 
\begin{equation}\label{interval-comb}
[-]\colon \disk^{\partial, {\sf or}}_{1/[-1,1]} \xra{\simeq} \sO^{\sf RL}~.
\end{equation} 

\end{observation}

After these observations, there is this immediate consequence.
\begin{cor}\label{assoc-interval}
There is a canonical equivalence of $\infty$-categories:
\[
\int_-\colon \Alg_{\Ass^{\sf RL}}(\cV) \xra{~\simeq~} \Alg_{[-1,1]}(\cV)~.
\]
\end{cor}

\begin{proof}
So the remaining point to check is that restriction along the map of $\infty$-operads $\disk^{\partial, \sf or}_{1/[-1,1]}\to \disk^{\partial, \sf or}_1$ implements an equivalence of symmetric monoidal $\infty$-categories ${\sf Env}\bigl(\disk^{\partial, \sf or}_{1/[-1,1]}\bigr) \xra{\simeq} \disk^{\partial, \sf or}_1$ from the symmetric monoidal envelope. 
Well, for each object $U\in \sD^{\partial, \sf or}_1$ it is standard that the space of morphisms $\mfld^{\partial, \sf or}_1\bigl(U,[-1,1]\bigr) \simeq \ast$ is contractible; and it follows that this functor gives an equivalence on spaces of objects of underlying $\infty$-categories.  
That this functor gives an equivalence on the space of morphisms follows because the functor on the active $\infty$-subcategories $\disk^{\partial, \sf or}_{1/[-1,1]} \to \disk^{\partial, \sf or}_1$ is a right fibration.  

\end{proof}

\begin{prop}\label{tensor-prod}
Let $(A;P,Q)$ be an $\Ass^{\sf RL}$-algebra in $\cV$; which is to say an associative algebra $A$ together with a unital left and a unital right $A$-module.
Applying Observation~\ref{disk-assoc}, regard $(A;P,Q)$ as a $\disk^{\partial, \sf or}_1$-algebra in $\cV$. 
There is a canonical equivalence in $\cV$:
\[
Q\underset{A}\ot P\xra{~\simeq~} \int_{[-1,1]} (A;P,Q)~.  
\]

\end{prop}

\begin{proof}
There is the standard fully faithful functor $\bDelta^{\op}\subset \sO^{\sf RL}$ whose essential image consists of those objects $(I,\leq , R, L)$ for which $R\neq \emptyset \neq L$.  
Adjoining minima and maxima gives a left adjoint to this functor, and so it is final.   
Through Observation~\ref{interval-assoc}, there is a final functor $\bDelta^{\op} \to \disk^{\partial, {\sf or}}_{1/[-1,1]}$; and the resulting simplicial object 
\[
{\sf Bar}_\bullet\bigl(Q,A,P\bigr)\colon \bDelta^{\op} \to \disk^{\partial, {\sf or}}_{1/[-1,1]} \to \disk^{\partial, \sf or}_1 \xra{[-]}{\sf Env}\bigl(\Ass^{\sf RL}\bigr) \xra{(A;P,Q)} \cV
\]
is identified as the two-sided bar construction, as indicated. 
We conclude the equivalence in $\cV$:
\[
Q\underset{A}\ot P \simeq \colim\bigl(\bDelta^{\op} \xra{{\sf Bar}_\bullet\bigl(Q,A,P\bigr)} \cV\bigr)\xra{\simeq} \int_{[-1,1]}(A;P,Q)~.
\]

\end{proof}




Lemma~\ref{f-inv-factr} and Proposition~\ref{tensor-prod} assemble as the next result.  
\begin{cor}\label{excision-arrow}
Let $F\colon \mfld(\cB) \longrightarrow \cV$ be a symmetric monoidal functor.  
Let $X\cong X_- \underset{\RR\times X_0}\bigcup X_+$ be a collar-gluing among $\cB$-manifolds.  
Then there is a canonical arrow in $\cV$:
\begin{equation}\label{exc-compare}
F(X_-)\underset{F(X_0)} \bigotimes F(X_+) \longrightarrow F(X)~.
\end{equation}

\end{cor}

\begin{proof}
The collar-gluing is prescribed by a constructible bundle $\w{X}\xra{f}[-1,1]$ from a refinement of $X$. 
From Lemma~\ref{f-inv-factr}, there is the composite map of $\infty$-operads 
\[
f^{-1}\colon \disk^{\partial, {\sf or}}_{1/[-1,1]} \xra{f^{-1}} \mfld(\cB)_{/\w{X}} \to \mfld(\cB) \xra{F} \cV~.
\] 
The universal property of factorization homology as a left adjoint gives the canonical arrow:
\[
F(X_-) \underset{F(X_0)}\bigotimes F(X_+)~{}~ \underset{\rm Prop~\ref{tensor-prod}}\simeq ~{}~\int_{[-1,1]} F_f~{}~ \longrightarrow ~{}~ F\bigl(f^{-1}([-1,1])\bigr) =  F(X)~;
\]
namely, this arrow is the counit of the adjunction $\int \colon \Alg_{\disk(\cB)}(\cV) \rightleftarrows \Fun^\ot\bigl(\mfld(\cB),\cV\bigr)$, evaluated on $F$.


\end{proof}
