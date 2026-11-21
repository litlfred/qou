---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-006-3-version-i-groupoid-valued-cohomology
section_title: "Version I: Groupoid-valued Cohomology"
section_number: 3
pages: 16-18
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.985
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{versionI}

We have already mentioned group valued \v Cech 1-cocycles in the introduction. They consist of an open cover $\mathscr{U} = \{U_i\}_{i\in I}$ of $M$ and smooth functions 
$g_{ij}: U_i \cap U_j \to G$ satisfying the cocycle condition
$ g_{ij} \cdot g_{jk} = g_{ik}$. 
Segal realized \cite{segal3} that this is the same as a smooth functor 
$$g: \vC (\mathscr{U}) \to \mathcal{B}G $$
where $\mathcal{B} G $ denotes the one-object groupoid introduced in Example \ref{example_groupoids} \eqref{exBG} and 
$\vC (\mathscr{U})$ denotes the \emph{\v Cech groupoid} corresponding to the cover $\mathscr{U}$. It has objects $\bigsqcup_{i\in I} U_i$ and morphisms $\bigsqcup_{i,j\in I} U_i \cap U_j$,  and its structure maps are
\begin{equation*}
s(x,i,j) = (x,i)  
\quomma
t(x,i,j) =  (x,j)
\quomma
\id_{(x,i)} = (x,i,i)
\quand
(x,j,k) \circ (x,i,j) = (x,i,k)\text{.}
\end{equation*}


Analogously, smooth natural transformations between smooth functors $\vC (\mathscr{U}) \to \mathcal{B}G$ give rise to \v Cech coboundaries. Thus the set $\big[\vC(\mathscr{U}), \mathcal{B}G\big]$ of equivalence classes of smooth functors equals the usual first \v Cech cohomology with respect to the cover $\mathscr{U}$. The classical first \v Cech-cohomology $\h^1(M,G)$  of $M$ is hence given by the colimit over all open covers $\mathscr{U}$ of $M$
$$  \h^1(M,G) = \varinjlim_{\mathscr{U}} \big[\vC(\mathscr{U}), \mathcal{B}G\big]\text{.} $$

We use this coincidence  in order  to define the 0-th \v Cech cohomology with coefficients in a general Lie groupoid $\Gamma$:

\begin{definition}
If $\Gamma$ is a Lie groupoid we set
$$ \h^0(M,\Gamma) := \varinjlim_{\mathscr{U}} \big[\vC(\mathscr{U}), \Gamma\big]$$
where the colimit is taken over all covers $\mathscr{U}$ of $M$ and $\big[\vC(\mathscr{U}), \Gamma\big]$ denotes the set of equivalence classes of smooth functors $\vC(\mathscr{U}) \to \Gamma$.
\end{definition}

\begin{remark}
The choice of the degree is such that $ \h^0(M,\Gamma)$ agrees in the case $\Gamma = \idmorph G$  (Example \ref{example_groupoids} \eqref{exM}) with the classical 0-th \v Cech-cohomology $ \h^0 (M, G)$ of $M$ with values in $G$.
\end{remark}

\begin{comment}
Unwinding the above definition, a $\Gamma$-cocycle in degree zero with respect to an open cover  $\mathscr{U}=\left \lbrace U_{\alpha} \right \rbrace$ is a pair $(f_{\alpha},g_{\alpha\beta})$ consisting of smooth maps
\begin{equation*}
f_{\alpha}: U_{\alpha} \to \Gamma_0
\quad\text{ and }\quad
g_{\alpha\beta}: U_{\alpha} \cap U_{\beta} \to \Gamma_1
\end{equation*}
satisfying
\begin{equation*}
s(g_{\alpha\beta}) = f_{\alpha}
\quad\text{, }\quad
t(g_{\alpha\beta}) = f_{\beta}
\quad\text{ and }\quad
g_{\beta\gamma} \circ g_{\alpha\beta} = g_{\alpha\gamma}\text{.}
\end{equation*}


Two $\Gamma$-cocycles $(f_{\alpha},g_{\alpha\beta})$ and $(f_{\alpha}', g_{\alpha\beta}')$ in degree zero are equivalent, 
if there exist  smooth maps $h_{\alpha}: U_{\alpha} \to \Gamma_1$ satisfying
\begin{equation*}
s(h_{\alpha}) = f_{\alpha}
\quad\text{, }\quad
t(h_{\alpha}) = f_{\alpha}'
\quad\text{ and }\quad
h_{\beta} \circ g_{\alpha\beta} = g_{\alpha\beta}' \circ h_{\alpha}\text{.}
\end{equation*}
\end{comment}

The geometrical meaning of the set is given in the following well-known theorem, which can be proved e.g. using Lemma \ref{homsets}.
\begin{theorem}
\label{bijection}
There is a  bijection
\begin{equation*}
\h^0(M,\Gamma) \cong \bigset{4.2cm}{Isomorphism classes of principal $\Gamma$-bundles over $M$}\text{.}
\end{equation*}
\end{theorem}



If $\Gamma$ is not only a Lie 2-groupoid but a Lie 2-group one can also define a \emph{first} cohomology group $ \h^1(M,\Gamma)$. Indeed, in this case one can consider the Lie 2-groupoid $\mathcal {B} \Gamma$ with one object, morphisms  $\Gamma_0$ and 2-morphisms  $\Gamma_1$.
Multiplication in $\Gamma$ gives the composition of morphisms in $\mathcal B \Gamma$. Let 
$\big[ \vC(\mathscr{U}) , \mathcal B \Gamma]$
denote the set of equivalence classes of smooth, weak 2-functors from the \v Cech-groupoid $\vC(\mathscr{U})$ to the Lie 2-groupoid
$\mathcal B \Gamma$. For the definition of weak functors see \cite{benabou2} -- below we will determine this set   explicitly.

\begin{definition}
\label{def:cohomology}
For a 2-group $\Gamma$ we set
$$ \h^1(M,\Gamma) := \varinjlim_{\mathscr{U}} \big[\vC( \mathscr{U} ), \mathcal B\Gamma\big]\text{.}$$
\end{definition} 

\begin{remark}
This agrees for  $\Gamma = \idmorph G$ with the classical $ \h^1(M,G)$. Furthermore, for an abelian Lie group $A$ the Lie groupoid $\mathcal BA$ is even a 2-group and $ \h^1(M,\mathcal B A)$ agrees with the classical \v Cech-cohomology $ \h^2(M,A)$.
\end{remark}

Unwinding the above definition, we get Version I of smooth $\Gamma$-gerbes:

\begin{definition}
\label{def:cocycles}
Let $\Gamma$ be a Lie 2-group, and let $\mathscr{U}=\left \lbrace U_{\alpha} \right \rbrace_{\alpha \in A}$ be an open cover of $M$.
\begin{enumerate}
\item 
A \emph{$\Gamma$-1-cocycle} with respect to $\mathscr{U}$ is a pair $(f_{\alpha\beta}, g_{\alpha\beta\gamma})$ of smooth maps
\begin{equation*}
 f_{\alpha\beta} : U_\alpha \cap U_\beta \to \Gamma_0 
\quad \text{ and } \quad
g_{\alpha\beta\gamma} : U_\alpha \cap U_\beta \cap U_\beta \to \Gamma_1
\end{equation*}
satisfying $s(g_{\alpha\beta\gamma}) = f_{\beta\gamma} \cdot f_{\alpha\beta}$ and $t(g_{\alpha\beta\gamma}) = f_{\alpha\gamma}$, and
\begin{equation}
\label{cocyclecond}
g_{\alpha\beta\delta} \circ (g_{\beta\gamma\delta} \cdot \id_{f_{\alpha\beta}}) = 
g_{\alpha \gamma \delta} \circ (\id_{f_{\gamma\delta}} \cdot g_{\alpha\beta\gamma}) \text{.}
\end{equation}
Here, the symbols $\circ$ and $\cdot$ stand for the composition and multiplication of $\Gamma$, respectively.

\item
Two $\Gamma$-1-cocycles $(f_{\alpha\beta},g_{\alpha\beta\gamma})$ and $(f_{\alpha\beta}', g_{\alpha\beta\gamma}')$ are \emph{equivalent}, 
if there exist smooth maps $h_{\alpha}: U_{\alpha} \to \Gamma_0$ and 
$s_{\alpha\beta}: U_{\alpha} \cap U_{\beta} \to \Gamma_1$
with
\begin{multline*}
s(s_{\alpha\beta}) = g_{\alpha\beta}' \cdot h_{\alpha}
\quad\text{, }\quad
t(s_{\alpha\beta}) = h_{\beta} \cdot g_{\alpha\beta}
\\\quad\text{ and }\quad
(\id_{h_{\gamma}} \cdot g_{\alpha\beta\gamma})  \circ (s_{\beta\gamma} \cdot \id_{f_{\alpha\beta}}) \circ (\id_{f_{\beta\gamma}} \cdot s_{\alpha\beta}) = s_{\alpha\gamma} \circ (g'_{\alpha\beta\gamma} \cdot \id_{h_{\alpha}})\text{.}
\end{multline*}
\end{enumerate}
\end{definition}


\begin{comment}
Equality \erf{cocyclecond} corresponds to the following diagram in the 2-groupoid $\mathcal B \Gamma$: \\
\begin{equation*}
\alxydim{}{
\bullet & & & &
\bullet \ar[llll]_{f_{\gamma\delta}}\\
& & \ar@{=>}[ll]_{g_{\alpha\gamma\delta}}& & \\
\bullet \ar[uurrrr] \ar[uu]^{f_{\alpha\delta}}\ar[rrrr]_{f_{\alpha\beta}} 
& & & &
\bullet \ar[uu]_{f_{\beta\gamma}} \ar@{=>}[llu]_{g_{\alpha\beta\gamma}}
}
\quad
=
\quad
\alxydim{}{
\bullet & & & & 
\bullet \ar[llll]_{f_{\gamma\delta}} \ar@{=>}[lld]^{g_{\beta\gamma\delta}}\\
& & \ar@{=>}[ll]^{g_{\alpha\beta\delta}}& & \\
\bullet\ar[uu]^{f_{\alpha\delta}}\ar[rrrr]_{f_{\alpha\beta}} 
& & & &
\bullet \ar[uu]_{f_{\beta\gamma}}  \ar[lllluu]
}
\end{equation*}
\end{comment}

\begin{remark}
For a crossed module $t:H \to G$ and $\Gamma := \act GH$ the associated Lie 2-group (Example \ref{crossedmodule}) one can reduce $\Gamma$-1-cocycles  to pairs 
\begin{equation*}
 \tilde f_{\alpha\beta} : U_\alpha \cap U_\beta \to G 
\quad \text{ and } \quad
\tilde g_{\alpha\beta\gamma} : U_\alpha \cap U_\beta \cap U_\beta \to H
\end{equation*}
which satisfies then a cocycle condition similar to \erf{cocyclecond}. Analogously, coboundaries can be reduced to pairs 
\begin{equation*}
\tilde h_{\alpha}: U_{\alpha} \to G \quad \text{ and } \quad
\tilde s_{\alpha\beta}: U_{\alpha} \cap U_{\beta} \to H \text{.}
\end{equation*}
This yields the  common definition of non-abelian cocycles, which can for example be found in \cite{breen3} or \cite{baez8}.   
\end{remark}


\begin{example}
In  case of the crossed module $i:H \to \mathrm{Aut}(H)$ with $\Gamma = \mathrm{AUT}(H)$ (see Example \ref{aut2group}) $\Gamma$-1-cocycles consist of pairs $\tilde f_{\alpha\beta}: U_{\alpha} \cap U_{\beta} \to \mathrm{Aut}(H)$ and $\tilde g_{\alpha\beta}: U_{\alpha} \cap U_{\beta} \cap U_{\gamma} \to H$.  Cocycles of this kind classify so-called Lie groupoid $H$-extensions \cite[Proposition 3.14]{laurent1}, which can hence be seen as another equivalent version for $\mathrm{AUT}(H)$-gerbes.
\end{example}


\setsecnumdepth{1}
