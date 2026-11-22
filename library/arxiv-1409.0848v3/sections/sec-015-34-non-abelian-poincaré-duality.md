---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-015-34-non-abelian-poincaré-duality
section_title: "Non-abelian Poincaré duality"
section_number: 3.4
pages: 40-42
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.977
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
\begin{definition}[Coefficient system]\label{def.coef-sys}
A \emph{coefficient system (for $\cB$-manifolds)} is a pointed presheaf on $\cB$.  
Let $E$ be a coefficient system.
The \emph{compactly supported sections} functor is the composition of the symmetric monoidal functors
\[
\Gamma_{\!\sf c}^E\colon \mfld(\cB)^{\sf fin} \xra{\tau^+} \Psh^{\sf fin}_\ast(\cB)^{\op} \xra{\Map_{\Psh_\ast(\cB)}(-,E)} \spaces_\ast
\]
where the target is equipped with the symmetric monoidal structure given by product.
We denote the resulting $\disk(\cB)$-algebra
\[
A_E~:=~ \bigl(\Gamma_{\!\sf c}^E\bigr)_{|\disk(\cB)}~\in\Alg_{\disk(\cB)}(\spaces_\ast)~.
\]
\end{definition}

\begin{example}
Consider a flag of maps of based spaces $\ZZ_{\geq 0}^{\op} \xra{Z_\bullet} \spaces_\ast$.  It corresponds to a right fibration $Z\to \ZZ_{\geq 0}$, equipped with a section.  
In~\cite{aft1} is constructed the functor ${\sf Depth}\colon \bsc \to \ZZ_{\geq 0}$.  
There results the coefficient system ${\sf Depth}^\ast Z \to \bsc$.  

\end{example}

\begin{example}\label{ordinary-coefs}
Let $\cB = \sD^{\fr}_n\simeq \ast$. Then a coefficient system is equivalent to the datum of a based space $Z$.  
Such a coefficient system is connective, in the sense of Definition \ref{connective-coefs}, exactly if $Z$ is $n$-connective.  

\end{example}

\begin{example}\label{coefs-corners}
A coefficient system on $\sD^\partial_n$ is map of fibrations 
\[
\xymatrix{
E_{n-1}  \ar[r]  \ar[d]
&
E_n   \ar[d]
\\
{\BO}(n-1) \ar[r]  
&
{\BO}(n)
}
\]
together with a pair of (compatible) sections of each.  

Consider the more elaborate example $\sD_{\langle n \rangle}$ codifying smooth $n$-manifolds with corners.  
A coefficient system on $\sD_{\langle n \rangle}$ is the data of a fibration $E_S \to\BO(\RR^S)$ for each subset $S\subset \{1,\dots,n\}$, and for each inclusion $S\subset T$ a map $E_S \to E_T$ over the inclusion $\BO(\RR^S) \xra{-\oplus \RR^{T\smallsetminus S}} \BO(\RR^T)$, which respect composition; together with a compatible section of each of these fibrations.  

\end{example}

We now concern ourselves with the question of when $\Gamma_{\!\sf c}^E$ is a homology theory.
We will only consider this question in the case that there is an integer $n\geq 0$ such that each basic $U\in \cB$ has pure dimension $n$ -- that is to say, the local topological dimension at each point in the underlying stratified space equals $n$.  
To address the problem, it is convenient to extend $\Gamma_{\!\sf c}^E$ to stratified spaces $X$ equipped with a $\cB$-structure on $\RR^{n-k}\times X$ for some $k$.
Here are the relevant temporary definitions.
\begin{definition}[$\mfld(\cB_k)$]\label{B-less-than}
Let $k$ be an integer.
Denote the $\infty$-categories which are the pullbacks
\[
\xymatrix{
\cB_k \ar[r]  \ar[d]
&
\mfld(\cB_{k})  \ar[rr]^-{\RR^{n-r}\times -}  \ar[d]
&&
\mfld(\cB)  \ar[d]
\\
\bsc  \ar[r]^-{\iota}
&
\snglr \ar[rr]^-{\RR^{n-k}\times -}
&&
\snglr.
}
\]
Denote the composite functor 
\[
\Gamma_{\!\sf c}^E\colon \mfld(\cB_k) \xra{\bigl((-1,1)^{n-k} \subset \RR^{n-k}\bigr)\times -} \Fun\bigl([1],\mfld(\cB)\bigr)\xra{{\sf Entr}\bigl({\sf ev}_0(-)_{{\sf ev}_1(-)^+}\bigr)} \spaces_\ast~.
\]
Explicitly, this functor evaluates as
\[
\Gamma_{\!\sf c}^E\colon X~\mapsto~{\sf Entr}\Bigl(\bigl((-1,1)^{n-k}\times X\bigr)_{(\RR^{n-k}\times X)^+}\Bigr)
\]
which we think of as ``sections of $E_{|\RR^{n-k}\times X}$ that are compactly supported in the $X$-direction''.  

\end{definition}

\begin{definition}\label{connective-coefs}
Let $\cB$ be a category of basics each of pure dimension $n$.
Say the coefficient system $E$ is \emph{connective} if the based space $\Gamma_{\!\sf c}^E(V)$ is connected for every $V\in \cB_{k}$ with $k<n$.  
\end{definition}

\begin{example}\label{fr-coefs}

Consider the case $\cB=\sD_n^{\fr}\simeq \ast$.
Here, a connective coefficient system is the datum of an $n$-connective based space $Z$, and the associated $\disk^{\fr}_n$-algebra is $\Omega^n Z$.
This $\disk_n^{\sf fr}$-algebra is \emph{group-like}.  
Through May's recognition principle there is an equivalence of $\infty$-categories between connective coefficient systems for framed $n$-manifolds, and that of group-like $\cE_n$-spaces.  
Accordingly, one can think of the data of a connective coefficient system as a generalization of the notion of a group-like algebra, for the structured stratified setting.
\end{example}

\begin{example}
Let us return to Example~\ref{coefs-corners} for the case of $\sD_n^\partial$.   
For simplicity, let us assume the two fibrations are trivialized with (based) fibers $Z_n$ and $Z_{n-1}$ respectively.  
This coefficient system is connective exactly if $Z_n$ is $n$-connective and the map $Z_{n-1} \to Z_n$ is $n$-connective; the last condition being equivalent to saying the homotopy fiber $F$ of the map $Z_{n-1}\to Z_n$ is $(n-1)$-connective.  
Indeed, for this coefficient system to be connective, then both $\Gamma_{\!\sf c}^E(\RR^k) \simeq \Omega^k Z_n$ and $\Gamma_{\!\sf c}^E(\HH^k)\simeq \Omega^k F$ must be connected for each $k<n$.
Now, recall from Example~\ref{deligne-boundary} a consolidation of the data of a $\disk_n^\partial$-algebra.
The associated $\disk^{\partial}_n$-algebra $A_E$ is the data $(\Omega^n Z_n, \Omega^{n-1}F , \alpha)$ where $\alpha$ is the action of $\Omega^n Z_n$ on $\Omega^{n-1} F$ from the $\Omega$-Puppe sequence of the fibration $F \to Z_{n-1} \to Z_n$.  
\end{example}

\begin{remark}
The previous example can be generalized to the case of $\sD_{\langle n\rangle}$, as we indicate here.
For simplicity, let us assume each of the said fibrations is trivial with respective fibers $Z_S$.  Denote by $F_T = \mathsf{hofib}(Z_T \to \holim_{S\subsetneq T} Z_S)$ the total homotopy fiber of the $T$-subcube.  
This coefficient system is connective exactly if each $F_T$ is $(n-|T|)$-connective.  
The associated $\disk_{\langle n \rangle}$-algebra $A_E$ is the data $\bigl((\Omega^{n\smallsetminus S} F_S\bigr)_{S\subset \{1,\dots,n\}}; \bigl(a_{S\subset T})\bigr)$ where $a_{S\subset T}$ is the action of $\Omega^{n\smallsetminus S}F_S$ on $\Omega^{n\smallsetminus T} F_T$ from an elaboration of the $\Omega$-Puppe sequence.  
\end{remark}


\begin{theorem}(Non-abelian Poincar\'e duality)\label{non-abel}
Let $\cB$ be an $\oo$-category of basics each of pure dimension $n$.  
Let $E$ be a connective coefficient system for $\cB$-manifolds.
Then the canonical arrow
\[
\int_- A_E~\xra{~\simeq~} ~\Gamma_{\!\sf c}^E(-)
\]
is an equivalence of functors $\mfld(\cB)^{\sf fin} \to \spaces_\ast$. 

\end{theorem}

\begin{proof}
From Theorem~\ref{hmlgy=FH}, we must show $\Gamma_{\!\sf c}^E\colon \mfld(\cB) \to \spaces$ satisfies excision.  
Consider a collar-gluing $X\cong X_-\underset{\RR\times X_0}\bigcup X_+$ among $\cB_{k}$-manifolds where $-1\leq k \leq n$.
We will show that the canonical map
\[
\Gamma_{\!\sf c}^E(X_-)\underset{\Gamma_{\!\sf c}^E(\RR\times V)} \bigotimes \Gamma_{\!\sf c}^E(X_+) \longrightarrow \Gamma_{\!\sf c}^E(X)~,
\]
is an equivalence; the desired case is $k=n$.  
There is the sequence of maps of pointed spaces
\begin{equation}\label{conn-base?}
\Gamma_{\!\sf c}^E(X_-)\times \Gamma_{\!\sf c}^E(X_+) \to \Gamma_{\!\sf c}^E(X) \to \Gamma_{\!\sf c}^E(X_0)~,
\end{equation}
which is a fiber sequence because of Lemma~\ref{pre-excision} applied to the modified collar-gluing $X \cong (X_-\sqcup X_+)\underset{\RR\times (X_0\sqcup X_0)}\bigcup \RR\times X_0$.
It is sufficient to show that the base of this fiber sequence is connected.  
We will do this by induction on $k$.  

Let $Y$ be a finitary $\cB_k$ manifold.
If $k=-1$, then $\Gamma_{\!\sf c}^E(Y) \simeq \ast$ is terminal.  In particular it is connected.
So suppose $\Gamma_{\!\sf c}^E(W)$ is connected for each $\cB_j$ manifold $W$ for $j<k$.   
From Theorem~\ref{recollections}, $Y$ can be witnessed as a finite iteration of collar-gluings of basics.  
We prove $\Gamma_{\!\sf c}^E(Y)$ is connected by induction on the minimal number $r$ of iterated collar-gluings to obtain $Y$.  
If $r=0$ the statement is vacuously true.   
If $Y$ is a basic then $\Gamma_{\!\sf c}^E(Y)$ is connected, by the connectivity assumption.  
If $r\geq 2$, write $Y = Y_-\underset{\RR\times W}\bigcup Y_+$ with each of the $\cB_k$-manifolds $Y_\pm$ witnessed through strictly fewer than $r$ collar-gluings, and with $W$ a $\cB_{k-1}$-manifold.  
By induction on $r$, each of the spaces $\Gamma_{\!\sf c}^E(Y_\pm)$ is connected.  
As in~(\ref{conn-base?}), there is the fiber sequence of pointed spaces
\[
\Gamma_{\!\sf c}^E(Y_-)\times \Gamma_{\!\sf c}^E(Y_+) \to \Gamma_{\!\sf c}^E(Y) \to \Gamma_{\!\sf c}^E(W)~;
\]
now the base is connected, by induction on $k$.
It follows that $\Gamma_{\!\sf c}^E(Y)$ is connected.  
\end{proof}

\begin{remark}\label{remark:grouplike}
We elaborate on Example~\ref{fr-coefs}.  
The space of stratified continuous maps is a homotopy invariant of the underlying stratified space $X$. 
In this sense, Theorem~\ref{non-abel} tells us that connective coefficient systems (think, `$\disk(\cB)$-spaces that are \emph{group-like}') cannot detect more than the stratified proper homotopy type of $\cB$-manifolds. 

\end{remark}
