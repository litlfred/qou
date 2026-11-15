---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-005-6-application-i-regev-type-formula
section_title: "Application I: Regev-type formula"
section_number: 6
pages: 25-34
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.981
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
\label{s:Regev}
In this section, as the first application of our Murnaghan--Nakayama rule, we are devoted to giving the Regev formula for the cyclotomic Hecke algebra $\mathscr{H}_{m,n}(q,\bm{u})$. Once the Murnaghan--Nakayama rule is set up right,
 the proof of the Regev formula, which is based on the classical deep work on symmetric groups and Hecke algebras in type $A$, is remarkably natural. To proceed with it, we initially, in accordance with \cite{Zhao1}, review the permutation super representation of the cyclotomic Hecke algebra $\mathscr{H}_{m,n}(q,\bm{u})$, as well as the Schur–Sergeev duality that exists between a certain quantum superalgebra $\mathscr{U}_q(\bm{g})$ and $\mathscr{H}_{m,n}(q,\bm{u})$.

We refer to a superspace $W$ as a $\mathbb{Z}_{2}$-graded vector space with decomposition $W=W_{\Bar{0}}\oplus W_{\Bar{1}}$. An element $w\in W$ is homogeneous with degree $\Bar{i}$ if $w\in W_{\Bar{i}}$, $i=0,1$. We also define the dimension of $W$ by $\rm{dim}(W):={\rm dim}(W_{\Bar{0}})| {\rm dim}(W_{\Bar{1}})$.

Let $V$ represent a direct sum of $m$ superspaces, denoted as $V=\bigoplus_{i=1}^m V^{(i)}$. In this context, we assume ${\rm dim}(V^{(i)})=k_i| l_i$ and $\{v^{(i)}_1,v^{(i)}_2,\cdots, v^{(i)}_{k_i}, v^{(i)}_{k_i+1},\cdots, v^{(i)}_{k_i+l_i}\}$ forms a homogeneous basis of $V^{(i)}$. Evidently, ${\rm dim}(V)=k| l$ with $k=\sum k_i$ and $l=\sum l_i$. Additionally, $\mathfrak{B}:=\{v_1,v_2,\cdots,v_{k+l}\}$ constitutes a homogeneous basis for $V$ with $v_d=v^{(s)}_t$ if $d=\sum_{i=1}^{s}(k_i+l_i)+t$. The entity $c(v_i)=r$ is defined contingent upon the condition $v_i\in V^{(r)}$. The term $c(\cdot)$ is occasionally referred to as the {\em color function}.

Introduce the linear map $\omega:~V\longrightarrow V$ defined by $\omega(v_i)=u_{c(v_i)}v_i$. Define the linear operators $\pi, \sigma:~ V\otimes V\longrightarrow V\otimes V$ by 
\begin{align}
    \pi(v_i\otimes v_j)&=
    \begin{cases}
        (q-q^{-1})v_i\otimes v_j+(-1)^{\Bar{i}\Bar{j}}v_j\otimes v_i, & \text{if $i<j$};\\
        \frac{(q-q^{-1})+(-1)^{\Bar{i}}(q+q^{-1})}{2}v_i\otimes v_i, & \text{if $i=j$};\\
        (-1)^{\Bar{i}\Bar{j}}v_j\otimes v_i, & \text{if $i>j$}.
        \end{cases}\\
        \sigma(v_i\otimes v_j)&=
    \begin{cases}
        \pi(v_i\otimes v_j), & \text{if $c(v_i)=c(v_j)$};\\
        (-1)^{\Bar{i}\Bar{j}}v_j\otimes v_i, & \text{if $c(v_i)\neq c(v_j)$}.
    \end{cases}
\end{align}
We can demonstrate $\pi^2=(q-q^{-1})\pi+1$, which implies $\pi$ is invertible and $\pi^{-1}=\pi-(q-q^{-1}){\rm Id}$.
We canonically extend $\pi$ and $\sigma$ to linear maps $\pi_i,\sigma_i (i=1,2,\cdots,n-1):~V^{\otimes n}\longrightarrow V^{\otimes n}$ by
\begin{align}
    \pi^{\pm 1}_{i}&:={\rm Id}^{\otimes (i-1)}\otimes \pi^{\pm 1}\otimes {\rm Id}^{\otimes(n-i-1)}\\
    \sigma_{i}&:={\rm Id}^{\otimes (i-1)}\otimes \sigma\otimes {\rm Id}^{\otimes(n-i-1)}\\
    \omega_{i}&:={\rm Id}^{\otimes (i-1)}\otimes \omega\otimes {\rm Id}^{\otimes(n-i)}.
\end{align}
Furthermore, we define $\pi_0:=\pi_{1}^{-1}\pi_2^{-1}\cdots\pi_{n-1}^{-1}\sigma_{n-1}\cdots\sigma_{1}\omega_1$. As is shown in \cite[Theorem 3.6]{Zhao1}, the map
\begin{align*}
    \Xi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}: ~\mathscr{H}_{m,n}(q,\bm{u})&\longrightarrow {\rm End}_{\mathbb{K}}V^{\otimes n}\\
    g_{i}~ &\longmapsto \pi_{i-1}, \quad i=1,2,\cdots,n.
\end{align*}
gives a (super) representation of $\mathscr{H}_{m,n}(q,\bm{u})$, called {\em permutation super representation} of $\mathscr{H}_{m,n}(q,\bm{u})$. We denote by $\chi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}(g(\bm{\mu}))$ the value of the character $\chi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}$ of $\Xi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}$ on the standard element $g(\bm{\mu})$. 



Let $\bm{k}=(k_1,k_2,\cdots,k_m)$ and $\bm{l}=(l_1,l_2,\cdots,l_m)$ be two compositions. For a given nonnegative integer $n$, we define the set $\mathfrak{C}(n;\bm{k}\mid\bm{l})$ of pairs of $m$-multicompositions associated with $\bm{k}$ and $\bm{l}$ by
\begin{align*}
 \mathfrak{C}(n;\bm{k}|\bm{l}):=\left\{(\bm{\alpha},\bm{\beta})\left| \, 
\begin{array}{l}
 \bm{\alpha}=(\alpha^{(1)},\cdots,\alpha^{(m)}) \text{ with $l(\alpha^{(i)})\leq k_i$ } \\
\bm{\beta}=(\beta^{(1)},\cdots,\beta^{(m)})\text{ with $l(\beta^{(i)})\leq l_i$ }
\end{array}
\right.\text{and $|\bm{\alpha}|+|\bm{\beta}|=n$} \right\}.   
\end{align*}
The main result in this section is the following formula for $\chi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}(g(\bm{\mu}))$, which is referred to as Regev's formula.
\begin{thm}\label{t:Regev}
Let $\bm{\mu}$ be a $m$-multipartition of $n$, then the value of the character of the permutation super representation on the standard element $g(\bm{\mu})$ is given by
\begin{align}\label{e:Regev}
\begin{split}
    &\chi^{\bm{u},q}_{\bm{k}|\bm{l};n}(g(\bm{\mu}))\\
=&q^{n-l(\bm{\mu})}\prod_{r=1}^m\prod_{j=1}^{l(\mu^{(r)})}\sum_{(\bm{\alpha};\bm{\beta})\in \mathfrak{C}(\mu^{(r)}_j;\bm{k}\mid\bm{l})} \bm{u}^r_{\overrightarrow{l}(\bm{\alpha};\bm{\beta})}(1-q^{-2})^{l(\balp;\bbeta)-1}(-q^{-2})^{|\bbeta|-l(\bbeta)}\prod_{i=1}^m\binom{k_i}{l(\alpha^{(i)})}\binom{l_i}{l(\beta^{(i)})}
\end{split}
\end{align}
where $\overrightarrow{l}(\bm{\alpha};\bm{\beta}):=\max\{1\leq i\leq m\mid l(\alpha^{(i)})+l(\beta^{(i)})>0\}$ and $l(\balp;\bbeta):=l(\balp)+l(\bbeta)$.
\end{thm}

\begin{rem}
    In a recent development, Zhao \cite{Zhao2} has proposed an alternative method to derive Theorem \ref{t:Regev}. It should be noted that his formulation is slightly different from ours, due to a distinct choice of presentation of $\mathscr{H}_{m,n}(q,\bm{u})$, as well as the standard elements $g(\bm{\mu})$.
\end{rem}

Next we will introduce a series of notations. Let $\bm{\la}$ be a $m$-multipartition with diagram $\D(\bm{\la})$. A {\em $(\bm{k},\bm{l})$-semistandard tableau} $\bm{\T}_{\bm{\la}}$ of shape $\bm{\la}$ is a $m$-tuple of $(k_i,l_i)$-semistandard tableaux (cf. \cite{BR}) obtained by filling each component $\D(\bm{\la}^{(i)})$ of $\D(\bm{\la})$ with variables $\{a^{(i)}_1<a^{(i)}_2<\cdots<a^{(i)}_{k_i}<b^{(i)}_1<b^{(i)}_2<\cdots<b^{(i)}_{l_i}, i=1,2,\cdots,m\}$, satisfying
\begin{enumerate}
    \item the cells filled with $a^{(i)}_{j}$'s form a tableau;
    \item $a^{(i)}_{j}$'s are nondecreasing in rows, strictly increasing in columns;
    \item $b^{(i)}_{j}$'s are nondecreasing in columns, strictly increasing in rows.
\end{enumerate}
Denote $s_{\bm{k},\bm{l}}(\bm{\la}):=\#\{(\bm{k},\bm{l})\text{-semistandard tableaux of shape $\la$}\}$. For a given $(\bm{\alpha},\bm{\beta})\in \mathfrak{C}(n;\bm{k}|\bm{l})$, we say that a $(\bm{k},\bm{l})$-semistandard tableau $\bm{\T}_{\bm{\la}}$ is of weight $(\bm{\alpha},\bm{\beta})$ if the number of $a^{(i)}_j$ (resp. $b^{(i)}_j$) in $\bm{\T}_{\bm{\la}}$ equals $\alpha^{(i)}_j$ (resp. $\beta^{(i)}_j$). Furthermore, denote by $s_{(\bm{\alpha},\bm{\beta})}(\bm{\la})$ the number of all $(\bm{k},\bm{l})$-semistandard tableaux of shape $\bm{\la}$ with weight $(\bm{\alpha},\bm{\beta})$. Clearly we have
\begin{align}\label{e:semi-tab}
    s_{\bm{k},\bm{l}}(\bm{\la})=\sum_{(\bm{\alpha},\bm{\beta})\in\mathfrak{C}(n;\bm{k}|\bm{l})}s_{(\bm{\alpha},\bm{\beta})}(\bm{\la})
\end{align} 
for any $m$-multipartition $\bm{\la}$ of $n$.

Define $H(k| l;n):=\{\la\vdash n\mid \la_{k+1}\leq l\}$. An element in $H(k| l;n)$ is called a {\em $(k,l)$-hook partition}. More generally, a multipartition is called a {\em $(\bm{k},\bm{l})$-hook multipartition} if each $\la^{(i)}$ is a $(k_i,l_i)$-hook partition for $i=1,2,\cdots,m$. Denote by $H(\bm{k}|\bm{l};n)$ the set of all $(\bm{k},\bm{l})$-hook multipartitions of $n$. Clearly, $H((1^m)| (1^m);n)$ consists of all multipartitions $\bm{\la}$ of $n$ such that each component of $\bm{\la}$ is a hook partition. Note that the assertion in \cite[Definition 2.4]{BR} implies that $s_{\bm{k},\bm{l}}(\bm{\la})\neq 0$ if and only if $\bm{\la}\in H(\bm{k}| \bm{l};n)$ for a multipartition $\bm{\la}$ of $n$.

Now we will express $\chi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}$ as a linear combination of irreducible characters $\chi^{\bm{\la}}$ using the above notations. To continue with this development, the Schur–Sergeev duality between $\mathscr{H}_{m,n}(q,\bm{u})$ and the quantum superalgebra $\mathscr{U}_{q}(\bm{g})$ is needed. Where $\mathscr{U}_{q}(\bm{g}):=\mathscr{U}_{q}(\bm{gl}(k_1| l_1))\otimes\cdots\otimes \mathscr{U}_{q}(\bm{gl}(k_m| l_m))$, among which $\mathscr{U}_{q}(\bm{gl}(k_i| l_i))$, introduced in \cite{BKK}, is the quantum enveloping superalgebra of $\bm{gl}(k_i| l_i)$. $V$ can be a representation of $\mathscr{U}_{q}(\bm{g})$, referred to as {\em vector presentation}. The Hopf structure of $\mathscr{U}_{q}(\bm{g})$ induces an action on $V^{\otimes n}$, denoted by $\Theta_n$. As is demonstrated in \cite{BKK}, the irreducible summands of the representation $V^{\otimes n}$ of $\mathscr{U}_q(gl(k,l))$ are indexed by the $(k,l)$-hook partitions of $n$, with each irreducible summand possessing the dimension $s_{k,l}(\la)$. Consequently, the irreducible summands of the representation $(\Theta_n, V^{\otimes n})$ of $\mathscr{U}_q(\bm{g})$ are characterized by the $(\bm{k},\bm{l})$-hook partitions of $n$, with each irreducible summand affording the dimension $s_{\bm{k},\bm{l}}(\bm{\la})$.

It is confirmed in \cite[Theorem 4.9]{Zhao1} that $(\Xi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}, V^{\otimes n})$ and $(\Theta_n, V^{\otimes n})$ satisfy the Schur–Sergeev duality, i.e.,
\begin{align}
    \Xi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}(\mathscr{H}_{m,n}(q,\bm{u}))={\rm End}_{\mathscr{U}_{q}(\bm{g})}V^{\otimes n}, \quad \Theta_n(\mathscr{U}_{q}(\bm{g}))={\rm End}_{\mathscr{H}_{m,n}(q,\bm{u})}V^{\otimes n}
\end{align}
Moreover, as a $(\mathscr{U}_q(\bm{g}), \mathscr{H}_{m,n}(q,\bm{u})$-bimodule,
\begin{align}
    V^{\otimes n}\cong\bigoplus_{\bm{\la}\in H(\bm{k}\mid\bm{l};n)}W_{\bm{\la}}\otimes W^{\bm{\la}},
\end{align}
where $W_{\bm{\la}}$ (resp. $W^{\bm{\la}}$) is the irreducible module of $\mathscr{U}_q(\bm{g})$ (resp. $\mathscr{H}_{m,n}(q,\bm{u})$) indexed by $\bm{\la}$. This gives the following decomposition:
\begin{align}
    V^{\otimes n}\cong\bigoplus_{\bm{\la}\in H(\bm{k}\mid\bm{l};n)}s_{\bm{k},\bm{l}}(\bm{\la})W^{\bm{\la}},
\end{align}
which is equivalent to
\begin{align}\label{e:expression}
\chi^{\bm{u},q}_{\bm{k}\mid\bm{l};n}=\sum_{\bm{\la}\in H(\bm{k}\mid\bm{l};n)} s_{\bm{k},\bm{l}}(\bm{\la})\chi^{\bm{\la}}.
\end{align}

Now we introduce the {\em skew characters} of $\mathscr{H}_{m,n}(q,\bm{u})$ via the Jacobi--Trudi rule.
Let $\bmu\subset\bla$ be two $m$-multipartitions (with $|\bmu|\le |\bla|$). For each $1\le r\le m$ and $a\in\mathbb Z$, set
\[
h_a^{(r)} :=
\begin{cases}
\chi^{\bvar_r^a}, & a\ge 1,\\
1, & a=0,\\
0, & a<0,
\end{cases}
\]
where $1$ denotes the unit character (for the degree $0$ algebra). We define
\begin{align}\label{e:def-skew-character}
\chi^{\bla/\bmu}:=\widehat{\bigotimes_{r=1}^{m}}
\det_{1\le i,j\le l(\la^{(r)})}\big(h^{(r)}_{\la^{(r)}_i-i-\mu^{(r)}_j+j}\big),
\end{align}
where the determinant is taken in the character ring with multiplication given by the outer product.







Next, we will restate our Murnaghan--Nakayama rule in terms of the skew characters. Before that, we need some terminologies about skew diagrams. Let $\bla/\bmu$ be a $m$-multi skew diagram, denote by ${\rm SE}(\bla/\bmu)$ the subset of $\bla/\bmu$ consisting of the southeast ribbon which starts from the northeastmost box and ends at the southeastmost box in each connected component in $\D(\bla/\bmu)$.
\begin{figure}
\begin{align*}
\left( \begin{array}{ccccc}
\begin{tikzpicture}[scale = 0.5]
      \begin{scope}
        \clip (0,0) -| (3,2) -| (4,3) -| (6,4) -- (2,4) |- (1,3) |- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (6,4);
      \end{scope}
      \draw [thick] (0,0) -| (3,2) -| (4,3) -| (6,4) -- (2,4) |- (1,3) |- (0,1) -- (0,0);
      \filldraw[fill = green]
    (0,0) rectangle (1,1) (1,0) rectangle (2,1) (2,0)rectangle (3,1) (2,1)rectangle(3,2) (2,2)rectangle(3,3) (3,2)rectangle(4,3) (3,3)rectangle(4,4) (4,3)rectangle(5,4) (5,3)rectangle(6,4);
      \node at (2.5,0.5) {$\bullet$};
      \node at (2.5,1.5) {$\bullet$};
    \end{tikzpicture},~&
    \begin{tikzpicture}[scale = 0.5]
      \begin{scope}
        \clip (0,0) -| (3,3) -| (6,4) -- (2,4) |- (1,2) |- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (6,4);
      \end{scope}
      \draw [thick] (0,0) -| (3,3) -| (6,4) -- (2,4) |- (1,2) |- (0,1) -- (0,0);
      \filldraw[fill = green]
    (0,0) rectangle (1,1) (1,0) rectangle (2,1) (2,0)rectangle (3,1) (2,1)rectangle(3,2) (2,2)rectangle(3,3) (2,3)rectangle(3,4) (3,3)rectangle(4,4) (4,3)rectangle(5,4) (5,3)rectangle(6,4);
      \node at (2.5,0.5) {$\bullet$};
      \node at (4.5,3.5) {$\bullet$};
      \node at (5.5,3.5) {$\bullet$};
    \end{tikzpicture},~&
    \begin{tikzpicture}[scale = 0.5]
      \begin{scope}
        \clip (0,0) -| (2,2) -| (5,3) -| (9,4) -- (3,4) |- (2,3) |- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (9,4);
      \end{scope}
      \draw [thick] (0,0) -| (2,2) -| (5,3) -| (9,4) -- (3,4) |- (2,3) |- (0,2) -- (0,0);
      \filldraw[fill = green]
    (0,0) rectangle (1,1) (1,0) rectangle (2,1) (1,1)rectangle (2,2) (2,2)rectangle(3,3) (3,2)rectangle(4,3) (4,2)rectangle(5,3) (4,3)rectangle(5,4) (5,3)rectangle(6,4) (6,3)rectangle(7,4) (7,3)rectangle(8,4) (8,3)rectangle(9,4);
      \node at (1.5,0.5) {$\bullet$};
      \node at (4.5,2.5) {$\bullet$};
      \node at (7.5,3.5) {$\bullet$};
      \node at (8.5,3.5) {$\bullet$};
    \end{tikzpicture}

\end{array}  \right)
\end{align*}
\caption{${\rm SE}(\bla/\bmu)$ consists of the green boxes. The subset formed by the boxes with bullets is an element of $\R_9(\bla/\bmu)$.}\label{F:SE}
    \end{figure}
We identify a box in the $a$-th row and the $b$-th column of $\D(\bla^{(i)}/\bmu^{(i)})$ with the coordinate $(a^{(i)},b^{(i)})$, $i=1,2,\cdots,m$. Let $\R_{t}(\bla/\bmu)$ be the set of all subsets $R$ of ${\rm SE}(\bla/\bmu)$ satisfying
\begin{itemize}
    \item $R$ has size $t$;
    \item For any $(a^{(i)},b^{(i)})\in R$ and $(x^{(i)},y^{(i)})\in {\rm SE}(\bla/\bmu)\setminus R$, we have either $x^{(i)}<a^{(i)}$ or $y^{(i)}<b^{(i)}$.
\end{itemize}
Figure \ref{F:SE} presents an example for ${\rm SE}(\bla/\bmu)$ and $\R_{t}(\bla/\bmu)$. It is not hard to see that for any $m$-multi skew diagram $\D(\bla/\bmu)$ and $R\in\R_t(\bla/\bmu)$, $\D(\bla/\bmu)\setminus R$ is still a $m$-multi skew diagram. For $R\in\R_{t}(\bla/\bmu)$, denote by $cc(R)$ the number of connected components of $R$. If $R$ has $d$ connected components $R_1,R_2,\cdots,R_d$, define $ht(R):=\sum_{i=1}^d ht(R_i)$.










Let $\bm\nu\in\mathcal P_{|\bla|-|\bmu|,m}$, and fix $1\le r\le m$, $1\le j\le l(\nu^{(r)})$. Then we have the following skew-diagram version of the Murnaghan--Nakayama rule:
\begin{align}\label{e:skew-m-n}
    \chi^{\bla/\bmu}_{\bm{\nu}}
    =q^{\nu^{(r)}_j-1}\sum_{R\in\R_{\nu^{(r)}_j}(\bla/\bmu)}
    u^{r}_{\overrightarrow{R}}(1-q^{-2})^{cc(R)-1}(-q^{-2})^{ht(R)}
    \chi^{(\bla/\bmu)\setminus R}_{\bm{\nu}\setminus \nu^{(r)}_j}.
\end{align}
Here
\[
\overrightarrow{R}:=\max\{1\leq i\leq m\mid \text{there exists at least one box of $R$ in }\bla^{(i)}/\bmu^{(i)}\}.
\]
Equation \eqref{e:skew-m-n} can be deduced from Corollary \ref{t:m-n2} using arguments similar to those in \cite[Chap.~2.4]{JK} (see also \cite[Theorem~5.2]{Zhao3}). More precisely, one applies Corollary \ref{t:m-n2} to the terms arising from the Jacobi--Trudi determinant expansion defining $\chi^{\bla/\bmu}$, and then regroups the resulting terms according to the subsets $R\in \R_{\nu^{(r)}_j}(\bla/\bmu)$ of ${\rm SE}(\bla/\bmu)$. The regrouped terms are precisely the skew characters $\chi^{(\bla/\bmu)\setminus R}$.



For $(\balp,\bbeta)\in\mathfrak{C}(n;\bm{k}|\bm{l})$, denote by $R_{\balp,\bbeta}$ some (any) $m$-multi skew diagrams $\D(\bla/\bmu)$ (This is not unique!) such that the connected components of $D(\la^{(i)}/\mu^{(i)})$ are horizontal strips $H^{(i)}_1,H^{(i)}_2,\cdots,H^{(i)}_{k_i}$ and vertical strips $V^{(i)}_1,V^{(i)}_2,\cdots,V^{(i)}_{l_i}$ $(i=1,2,\cdots,m)$ satisfying 
\begin{align}
   (H^{(i)}_1,H^{(i)}_2,\cdots,H^{(i)}_{k_i})=(\alpha^{(i)}_1,\alpha^{(i)}_2,\cdots,\alpha^{(i)}_{k_i}),\quad (V^{(i)}_1,V^{(i)}_2,\cdots,V^{(i)}_{l_i})=(\beta^{(i)}_1,\beta^{(i)}_2,\cdots,\beta^{(i)}_{l_i}). 
\end{align}

\begin{figure}
\begin{align*}
\left( \begin{array}{ccccc}
 \begin{tikzpicture}[scale = 0.4]
      \begin{scope}
        \clip (0,0) -| (1,3) -| (4,4) -| (5,6) -| (7,7) -- (0,7) -- (0,0);
        \draw [color=black!25] (0,0) grid (7,7);
      \end{scope}
      \draw [thick] (0,0) -| (1,3) -| (4,4) -| (5,6) -| (7,7) -- (0,7) -- (0,0);
      \filldraw[fill = green]
    (0,0) rectangle (1,1) (0,1) rectangle (1,2) (1,3)rectangle (2,4) (2,3)rectangle(3,4) (3,3)rectangle(4,4) (4,4)rectangle(5,5) (4,5)rectangle(5,6) (5,6)rectangle(6,7) (6,6)rectangle(7,7);
    \end{tikzpicture},\qquad&
    \begin{tikzpicture}[scale = 0.4]
      \begin{scope}
        \clip (0,0) -| (2,1) -| (3,4) -| (5,6) -| (8,7) -- (0,7) -- (0,0);
        \draw [color=black!25] (0,0) grid (8,7);
      \end{scope}
      \draw [thick] (0,0) -| (2,1) -| (3,4) -| (5,6) -| (8,7) -- (0,7) -- (0,0);
      \filldraw[fill = green]
    (0,0) rectangle (1,1) (1,0) rectangle (2,1) (2,1)rectangle (3,2) (2,2)rectangle(3,3) (2,3)rectangle(3,4) (3,4)rectangle(4,5) (4,4)rectangle(5,5) (5,6)rectangle(6,7) (6,6)rectangle(7,7) (7,6)rectangle(8,7);
    \end{tikzpicture}
    
\end{array}  \right)
\end{align*}
\caption{An example for $R_{\balp,\bbeta}$ where $\balp=((2,3), (3,2,2))$ and $\bbeta=((2,2),(3))$. The corresponding skew character can be written as $\chi^{(\balp,\bbeta)}=\chi^{(2)}\hat{\otimes}\chi^{(3)}\hat{\otimes}\chi^{(1^2)}\hat{\otimes}\chi^{(1^2)}\hat{\otimes}\chi^{(3)}\hat{\otimes}\chi^{(2)}\hat{\otimes}\chi^{(2)}\hat{\otimes}\chi^{(1^3)}.$}\label{F:HV}
    \end{figure}

For $R_{\balp,\bbeta}$, define the character related to $R_{\balp,\bbeta}$ by 
\begin{align}
    \chi^{(\balp;\bbeta)}:=\widehat{\bigotimes\limits_{1\leq i\leq m}}\left(\chi^{(\alpha^{(i)}_1)}\hat{\otimes}\cdots\hat{\otimes}\chi^{(\alpha^{(i)}_{k_i})}\hat{\otimes}\chi^{(1^{\beta^{(i)}_{1}})}\hat{\otimes}\cdots\hat{\otimes}\chi^{(1^{\beta^{(i)}_{l_i}})}\right).
\end{align}
See Figure \ref{F:HV} for an example for $R_{\balp,\bbeta}$. 

Due to \cite[Lemma 3.23]{BR} (see also \cite[Lemma 3.2]{Tay}, \cite[Corollary 5.5]{Zhao3}), we have the following decomposition for $\chi^{(\balp;\bbeta)}$ in terms of irreducible characters.
\begin{align}\label{e:alp-beta}
    \chi^{(\balp;\bbeta)}=\sum_{\bla\in H(\bm{k}|\bm{l};n)}s_{(\balp,\bbeta)}(\bla)\chi^{\bla}.
\end{align}

Now we restate our skew version of the Murnaghan--Nakayama rule in a special case. $R_{\balp,\bbeta}$ is a $m$-multi skew diagram as mentioned above. Then 
\begin{align}
    \R_t(R_{\balp,\bbeta})=\{R_{\bgam,\bdel}\mid (\bgam,\bdel)\subset(\balp,\bbeta), |\bgam|+|\bdel|=t\}.
\end{align}
Furthermore, if $R_{\bgam,\bdel}\in \R_t(R_{\balp,\bbeta})$, then we have $cc\left(R_{\bgam,\bdel}\right)=l(\bgam)+l(\bdel)=l(\bgam;\bdel)$, $ht(R_{\bgam,\bdel})=|\bdel|-l(\bdel)$ and $\overrightarrow{R_{\bgam,\bdel}}=\overrightarrow{l}(\bgam;\bdel)$. We can restate \eqref{e:skew-m-n} in the following special setting.
\begin{align}\label{e:skew-m-n2}
    \chi^{(\balp;\bbeta)}_{\bm{\nu}}=q^{\nu^{(r)}_j-1}\sum_{\substack{
(\bgam,\bdel)\subset(\balp,\bbeta)\\ |\bgam|+|\bdel|=\nu^{(r)}_j}} u^{r}_{\overrightarrow{l}(\bgam,\bdel)}(1-q^{-2})^{l(\bgam;\bdel)-1}(-q^{-2})^{|\bdel|-l(\bdel)}\chi^{(\balp;\bbeta)\setminus(\bgam;\bdel)}_{\bm{\nu}\setminus\nu^{(r)}_j}.
\end{align}

We are ready to prove Theorem \ref{t:Regev}.\\
{\em Proof of Theorem \ref{t:Regev}.} 
\begin{align*}
    &\chi^{\bm{u},q}_{\bm{k}|\bm{l};n}(g(\bm{\mu}))\\
    =&\sum_{\bm{\la}\in H(\bm{k}\mid\bm{l};n)} s_{\bm{k},\bm{l}}(\bm{\la})\chi^{\bm{\la}} \quad \text{(by \eqref{e:expression})}\\
    =&\sum_{\bm{\la}\in H(\bm{k}\mid\bm{l};n)} 
    \sum_{(\bm{\alpha},\bm{\beta})\in\mathfrak{C}(n;\bm{k}|\bm{l})}s_{(\bm{\alpha},\bm{\beta})}(\bm{\la})\chi^{\bm{\la}} \quad \text{(by \eqref{e:semi-tab})}\\
    =&\sum_{(\bm{\alpha},\bm{\beta})\in\mathfrak{C}(n;\bm{k}|\bm{l})} \chi^{(\balp;\bbeta)} \quad \text{(by \eqref{e:alp-beta})}\\
    =&\sum_{(\bm{\alpha},\bm{\beta})\in\mathfrak{C}(n;\bm{k}|\bm{l})}q^{\mu^{(r)}_j-1}\sum_{\substack{
(\bgam,\bdel)\subset(\balp,\bbeta)\\ |\bgam|+|\bdel|=\mu^{(r)}_j}} u^{r}_{\overrightarrow{l}(\bgam,\bdel)}(1-q^{-2})^{l(\bgam;\bdel)-1}(-q^{-2})^{|\bdel|-l(\bdel)}\chi^{(\balp;\bbeta)\setminus(\bgam;\bdel)}_{\bm{\mu}\setminus\mu^{(r)}_j}\quad \text{(by \eqref{e:skew-m-n2})}.
\end{align*}
For a given $(\bm{\alpha}^{'},\bm{\beta}^{'})\in\mathfrak{C}(n-\mu^{(r)}_j;\bm{k}|\bm{l})$, if $(\bm{\alpha},\bm{\beta})\setminus(\bgam,\bdel)=(\bm{\alpha}^{'},\bm{\beta}^{'})$, then the number of $(\bgam,\bdel)$'s contributing the coefficient
\begin{align*}
    q^{\mu^{(r)}_j-1}u^{r}_{\overrightarrow{l}(\bgam,\bdel)}(1-q^{-2})^{l(\bgam;\bdel)-1}(-q^{-2})^{|\bdel|-l(\bdel)}
\end{align*}
is exactly
\begin{align*}
    \prod_{i=1}^m\binom{k_i}{l(\gamma^{(i)})}\binom{l_i}{l(\delta^{(i)})}.
\end{align*}
Therefore,
\begin{align*}
    &\chi^{\bm{u},q}_{\bm{k}|\bm{l};n}(g(\bm{\mu}))\\
    =&\left(\sum_{(\bm{\gamma},\bm{\delta})\in\mathfrak{C}(\mu^{(r)}_j;\bm{k}|\bm{l})}q^{\mu^{(r)}_j-1} u^{r}_{\overrightarrow{l}(\bgam,\bdel)}(1-q^{-2})^{l(\bgam;\bdel)-1}(-q^{-2})^{|\bdel|-l(\bdel)}\prod_{i=1}^m\binom{k_i}{l(\gamma^{(i)})}\binom{l_i}{l(\delta^{(i)})}\right)\\
    &\times \sum_{(\bm{\alpha}^{'},\bm{\beta}^{'})\in\mathfrak{C}(n-\mu^{(r)}_j;\bm{k}|\bm{l})}\chi^{(\balp^{'};\bbeta^{'})}_{\bm{\mu}\setminus\mu^{(r)}_j}.
\end{align*}
An induction argument completes the proof. $\hspace{15em}\Box$

Next, we consider the special case $(\bm{k}|\bm{l})=((1^m)|(1^m))$. It follows from the proof of Theorem \ref{t:Regev} that
\begin{align}\label{e:equality}
    \chi^{\bm{u},q}_{(1^m)|(1^m);n}=\sum_{(\bm{\alpha},\bm{\beta})\in\mathfrak{C}(n;(1^m)|(1^m))} \chi^{(\balp;\bbeta)}. 
\end{align}
Note that every $(\balp,\bbeta)$ in $\mathfrak{C}(n;(1^m)|(1^m))$ has the form
$$(\balp,\bbeta)=((\alpha_1),(\alpha_2),\cdots,(\alpha_m),(\beta_1),(\beta_2),\cdots,(\beta_m))$$
with $\sum_{i=1}^m(\alpha_i+\beta_i)=n$. So
\begin{align}\label{e:q2}
    \text{RHS of \eqref{e:equality} }=\sum_{\substack{
c_1+c_2+\cdots+c_m=n\\ c_i\geq 0}}\widehat{\bigotimes_{1\leq i\leq m}}\sum_{\alpha_i=0}^{c_i}\chi^{(\alpha_i;c_i-\alpha_i)}.
\end{align}
By \cite[Remark 3.3]{Tay}, 
\begin{align}
    \sum_{\alpha_i=0}^{c_i}\chi^{(\alpha_i;c_i-\alpha_i)}=
    \begin{cases}
        1 &\text{if $c_i=0$};\\
        2\sum_{\alpha_i=0}^{c_i-1}\chi^{(c_i-\alpha_i,1^{\alpha_i})} &\text{if $c_i\geq 1$}.
    \end{cases}
\end{align}
Substituting this into \eqref{e:q2} gives that
\begin{align}\label{e:q3}
 \text{RHS of \eqref{e:equality} }=\sum_{\bla\in H((1^m)| (1^m);n)}   2^{L(\bla)}\chi^{\bla}.
\end{align}
Recall that $H((1^m)| (1^m);n)$ consists of all $m$-multipartitions $\bm{\la}$ of $n$ such that each component $\la^{(i)}$ is a hook partition. Here $L(\bla):=\#\{1\leq i\leq m\mid \la^{(i)}\neq \varnothing\}$.

On the other hand, by \eqref{e:Regev},
\begin{align}\label{e:q4}
 \chi^{\bm{u},q}_{(1^m)|(1^m);n}(g(\bm{\mu}))
=q^{n-l(\bm{\mu})}\prod_{r=1}^m\prod_{j=1}^{l(\mu^{(r)})}\sum_{(\alpha;\beta)} \bm{u}^r_{\overrightarrow{l}(\alpha;\beta)}(1-q^{-2})^{l(\alpha)+l(\beta)-1}(-q^{-2})^{|\beta|-l(\beta)}
\end{align}
the inner sum runs over all pairs of $m$-compositions $(\alpha;\beta)$ with $|\alpha|+|\beta|=\mu^{(r)}_j$.

Note that
\begin{align}
\begin{split}\label{e:q5}
 &\sum_{\substack{(\alpha;\beta)\\
 |\alpha|+|\beta|=\mu^{(r)}_j}} \bm{u}^r_{\overrightarrow{l}(\alpha;\beta)}(1-q^{-2})^{l(\alpha)+l(\beta)-1}(-q^{-2})^{|\beta|-l(\beta)}\\
 =&\frac{1}{1-q^{-2}}\sum_{\substack{
c_1+c_2+\cdots+c_m=\mu^{(r)}_j\\ c_i\geq 0}}\bm{u}^r_{\overrightarrow{c}}\sum_{\substack{(\alpha;\beta)\\
 |\alpha|+|\beta|=c_i}}(1-q^{-2})^{\sum_{i=1}^m(2-\delta_{\beta_i,c_i}-\delta_{\beta_i,0})}(-q^{-2})^{\sum_{i=1}^m(\beta_i+\delta_{\beta_i,0}-1)}\\
 =&\frac{1}{1-q^{-2}}\sum_{\substack{
c_1+c_2+\cdots+c_m=\mu^{(r)}_j\\ c_i\geq 0}}\bm{u}^r_{\overrightarrow{c}}\sum_{\substack{(\alpha;\beta)\\
 |\alpha|+|\beta|=c_i}}\prod_{i=1}^m(1-q^{-2})^{2-\delta_{\beta_i,c_i}-\delta_{\beta_i,0}}(-q^{-2})^{\beta_i+\delta_{\beta_i,0}-1}\\
 =&\frac{1}{1-q^{-2}}\sum_{\substack{
c_1+c_2+\cdots+c_m=\mu^{(r)}_j\\ c_i\geq 0}}\bm{u}^r_{\overrightarrow{c}}\prod_{i=1}^m\sum_{\beta_i=0}^{c_i}(1-q^{-2})^{2-\delta_{\beta_i,c_i}-\delta_{\beta_i,0}}(-q^{-2})^{\beta_i+\delta_{\beta_i,0}-1}\\
=&\sum_{\substack{
c_1+c_2+\cdots+c_m=\mu^{(r)}_j\\ c_i\geq 0}}\bm{u}^r_{\overrightarrow{c}}2^{\#c}(1-q^{-2})^{\#c-1}\prod_{i=1}^m[c_i]_{-q^{-2}},
\end{split}
\end{align}
where $\overrightarrow{c}:=\max\{1\leq i\leq m\mid c_i\neq 0\}$, $c:=\{1\leq i\leq m\mid c_i\neq 0\}$ and $[k]_q:=\frac{1-q^k}{1-q}$ (Here $k\geq 0$ and $[0]_q:=1$) is the standard $q$-integer. The last equation holds for the following identity:
\begin{align*}
   \sum_{\beta_i=0}^{c_i}(1-q^{-2})^{2-\delta_{\beta_i,c_i}-\delta_{\beta_i,0}}(-q^{-2})^{\beta_i+\delta_{\beta_i,0}-1}=
   \begin{cases}
       2(1-q^{-2})[c_i]_{-q^{-2}} & \text{if $c_i>0$}\\
       1 & \text{if $c_i=0$}.
   \end{cases}
\end{align*}

We say that a $m$-tuple of matrices $(M^{(1)},M^{(2)},\cdots,M^{(m)})$ is a {\em $m$-multimatrix} if each $M^{(i)}$ has $m$ columns with entries nonnegative integers.  Denote by $\mathcal{M}_{m}$ the set of all $m$-multimatrices. For a $m$-multimatrix $\bm{M}=(M^{(1)},M^{(2)},\cdots,M^{(m)})$, define
\begin{align*}
    \bm{r}(\bm{M}):=\sum_{i=1}^m r(M^{(i)}),\quad   \bm{u}_{\bm{M}}:=\prod_{i=1}^{m}\prod_{j=1}^{r(M^{(i)})}u^{i}_{\overrightarrow{r}_j(M^{(i)})}.
\end{align*}
Here we use the notations  $r(M^{(i)})$ and $\overrightarrow{r}_j(M^{(i)})$ to present the number of rows in matrix $M^{(i)}$ and the $j$-th row vector of matrix $M^{(i)}$, respectively.

Thus $u_{\overrightarrow{r}_j(M^{(i)})}=u_{f_{ij}}$ with $f_{ij}$ the column containing the first non-zero element from right to left in the $j$th row of $M^{(i)}$. For instance, if
\begin{align}\label{e:example}

\bm{M}=\left( \begin{array}{ccc}
\begin{pmatrix}3 &  \textcolor{orange}{2} & 0 \\
 0 & 1 & \textcolor{orange}{6}
\end{pmatrix},~&
    \begin{pmatrix}\textcolor{orange}{2} & 0 & 0 \\
 0 & 4 & \textcolor{orange}{2}\\
 \textcolor{orange}{8}& 0 & 0
\end{pmatrix},~&
\begin{pmatrix}2, \textcolor{orange}{2}, 0 
\end{pmatrix} 
\end{array}  \right).
\end{align}
We have marked the last non-zero element in each row in \textcolor{orange}{orange}. Thus,
\begin{align*}

(f_{ij})=\left( \begin{array}{ccc}
\begin{pmatrix}  2  \\
 3
\end{pmatrix},~&
    \begin{pmatrix}1 \\
 3\\
 1
\end{pmatrix},~&
 \begin{pmatrix}2
\end{pmatrix}
\end{array}  \right),\quad \bm{u}_{\bm{M}}=u^4_1u^4_2u_3^3.
\end{align*}

Substituting \eqref{e:q5} into \eqref{e:q4} gives that
\begin{align}\label{e:q6}
 \chi^{\bm{u},q}_{(1^m)|(1^l);n}(g(\bm{\mu}))=\sum_{\bm{M}}u_{\bm{M}}2^{\#\bm{M}}(q-q^{-1})^{\#\bm{M}-l(\bmu)}\prod_{m^{(r)}_{ij}\in\bm{M}}[m^{(r)}_{ij}]_{-q^{-2}},
 \end{align}
 summed over all $m$-multimatrices $(M^{(1)},\cdots,M^{(m)})\in\mathcal{M}_m$ such that the $j$-th row sum of $M^{(r)}$ equals $\mu^{(r)}_j$. Where $\#\bm{M}$ is the number of nonzero entries in $\bm{M}$.

 Now we have obtained the following result.
 \begin{cor}\label{t:special-hook}
    Let $\bmu$ be a multipartition of $n$. Then we have the following combinatorial formula, which is also referred as the Regev formula. 
     \begin{align}\label{e:special-hook}
 \sum_{\substack{\bla\vdash n\\ {\rm all}~\la^{(i)}~{\rm hook}}}   2^{L(\bla)}\chi^{\bla}_{\bmu}=\sum_{\bm{M}}u_{\bm{M}}2^{\#\bm{M}}(q-q^{-1})^{\#\bm{M}-l(\bmu)}\prod_{m^{(r)}_{ij}\in\bm{M}}[m^{(r)}_{ij}]_{-q^{-2}},
 \end{align}
 summed over all $m$-multimatrices $(M^{(1)},\cdots,M^{(m)})$ such that the $j$th row sum of $M^{(r)}$ equals $\mu^{(r)}_j$.
     \begin{proof}
         It follows from \eqref{e:equality}, \eqref{e:q3} and \eqref{e:q6} by noticing that $H((1^m)| (1^m);n)$ consists of all multipartitions $\bla$ of $n$ with each component $\la^{(i)}$ being hook shape.
     \end{proof}
 \end{cor}

\begin{rem}
We remark that Zhao \cite{Zhao2} obtained an asymptotic formula for the LHS of \eqref{e:special-hook}.
It is pertinent to point out that an alternative proof for Corollary \ref{t:special-hook} is presented by establishing a connection between the irreducible characters of $\mathscr{H}_{m,n}(q,\bm{u})$ and those of Hecke algebra in type $A$. This proof relies on the Regev formula for Hecke algebra in type $A$. To prevent redundancy, we leave this proof in the appendix \ref{app}.
   \end{rem}
   
 Recall that $\mathscr{H}_{m,n}(q,\bm{u})$ will reduce to Hecke algebra $\mathscr{H}_{n}(q)$ (resp. complex reflection group $\mathscr{W}_{m,n}$) when $m=1$, $u_1=1$ (resp. $q=1$, $\bm{u}=\{1,\zeta,\cdots,\zeta^{m-1}\}$). Here $\zeta$ is the primitive $m$-th root of unity. Before closing this section, we want to examine how the Regev formula adapts in these two special cases. To do so, we will analyze each case individually.  For the first case, i.e., $m=1$, $u_1=1$, it is easy to see \eqref{e:special-hook} is degraded to
 \begin{align}
     \sum_{\la~\text{hook}}\psi^{\la}_{\mu}=2^{l(\mu)-1}\prod_{i=1}^{l(\mu)}[\mu_i]_{-q^{-2}}.
 \end{align}
Where $\psi^{\la}$ is the irreducible character of $\mathscr{H}_{n}(q)$ indexed by $\la$. This is exactly the Regev formula for the Hecke algebra in type $A$ established in \cite{JL1,Zhao3}. For the second case, i.e., $q=1$, $\bm{u}=\{1,\zeta,\cdots,\zeta^{m-1}\}$, we have
\begin{align*}
   &\sum_{\bm{M}}u_{\bm{M}}2^{\#\bm{M}}(q-q^{-1})^{\#\bm{M}-l(\bmu)}\prod_{m^{(r)}_{ij}\in\bm{M}}[m^{(r)}_{ij}]_{-q^{-2}}=
   \begin{cases}
       \sum\limits_{\bm{M}} \bm{u}_{\bm{M}} 2^{l(\bm{\mu})} & \text{if all $\mu^{(r)}_j$'s are odd}\\
       0 & \text{otherwise}
   \end{cases}
\end{align*}
summed over all $m$-multimatrices $\bm{M}$ such that $j$-th row of $M^{(r)}$ has only one nonzore entry $\mu^{(r)}_{j}$. Moreover, if all $\mu^{(r)}_j$'s are odd, then
\begin{align*}
  \sum\limits_{\bm{M}} \bm{u}_{\bm{M}} 2^{l(\bm{\mu})}=\prod_{r=1}^m\prod_{j=1}^{l(\mu^{(r)})}2\sum_{i=1}^{m}\zeta^{(r-1)i}=
  \begin{cases}
      (2m)^{l(\mu^{(1)})}, & \text{if $\bmu=(\mu^{(1)},0,\cdots,0)$};\\
      0, &\text{otherwise}.
  \end{cases}
\end{align*}
The last equation holds for the following identity:
\begin{align*}
    \sum_{i=1}^m\zeta^{(r-1)i}=
    \begin{cases}
        m, &\text{if $r=1$};\\
        0, &\text{if $1<r\leq m$}.
    \end{cases}
\end{align*}

We have reached the Regev formula for $\mathscr{W}_{m,n}$.
\begin{cor}
    Suppose $\bmu$ is a $m$-multipartition of $n$, then
    \begin{align}
        \sum_{\substack{\bla\vdash n\\ \la^{(i)}~{\rm hook}}}\phi^{\bla}_{\bmu}=
        \begin{cases}
            (2m)^{l(\mu^{(1)})}, &\text{if $\bmu=(\mu^{(1)},0,\cdots,0)$ with all parts odd;}\\
            0, &\text{otherwise}.
        \end{cases}
    \end{align}
    Where $\phi^{\bla}$ is the irreducible character of $\mathscr{W}_{m,n}$ indexed by multipartition $\bla$.
\end{cor}
