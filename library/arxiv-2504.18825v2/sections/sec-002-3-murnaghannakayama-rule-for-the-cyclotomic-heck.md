---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-002-3-murnaghannakayama-rule-for-the-cyclotomic-heck
section_title: "Murnaghan–Nakayama rule for the cyclotomic Hecke algebra"
section_number: 3
pages: 12-18
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.972
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
\label{s:M-N}
In this section, we will present our Murnaghan--Nakayama rule for the cyclotomic Hecke algebra.


\subsection{Murnaghan--Nakayama rule}
A skew diagram $\lambda/\mu$ is a {\it vertical} (resp. {\it horizontal}) {\it strip} if each row (resp. column) contains at most one box. We say a skew diagram of $\la/\mu$ is a {\it ribbon} (also known as {\it border strip} or {\it rim hook}) if it is connected and contains no $2\times 2$ blocks \begin{tikzpicture}
  \draw[step=0.2cm, color=black] (-0.2,-0.2) grid (0.2,0.2); 
\end{tikzpicture}. The {\it height} (denoted by $ht(\la/\mu)$) of a ribbon $\la/\mu$ is defined as the number of the rows in $\la/\mu$ minus $1$.  More generally, a {\it generalized ribbon} is a skew diagram without $2\times 2$ blocks (not necessarily connected). Any generalized ribbon is a union of its connected components, each of which is a ribbon. For a generalized ribbon $\la/\mu$ with connected components $\xi_1,\xi_2,\cdots,\xi_m$, define the height of $\la/\mu$ as the sum of the heights of connected components of $\la/\mu$, i.e., $ht(\la/\mu)=\sum_{i=1}^{m}ht(\xi_i)$, and use $cc(\la/\mu)$ to denote the number of connected components of $\la/\mu$. Define the {\it weight} of a generalized ribbon $\la/\mu$ by
\begin{align}
\wt(\la/\mu;t):=(1-t)^{cc(\la/\mu)}(-t)^{ht(\la/\mu)}.
\end{align}

The following lemma is essential for us to obtain our Murnaghan--Nakayama rule, with part of the proof techniques inspired by \cite[(6.7)]{HR95}.
\begin{lem}\label{t:qs}
Let $k$ be a non-negative integer, then
\begin{align}\label{e:qs}
q_k(x;t)s_{\mu}=\sum_{\la}\wt(\la/\mu;t)s_{\la}
\end{align}
summed over all partitions $\la\vdash |\mu|+k$ such that $\la/\mu$ is a generalized ribbon.
\end{lem}
\begin{proof}
Recall the identity in \cite[Corollary 3.2]{JL3} $\big(q=t=0,\bm{a}=(1,0,\cdots)~\text{and}~\bm{b}=(t,0,\cdots)\big)$ that
\begin{align}
\sigma^k\big((1-t)X\big)s_{\mu}(x)=\sum_{\mu\subset\la}s^{\la/\mu}(1-t)s_{\la}(x).
\end{align}





By \eqref{e:q-laring}, it suffices to prove $s^{\la/\mu}(1-t)=\wt(\la/\mu;t)$ if $\la/\mu$ is a generalized ribbon and $0$ otherwise. By \eqref{e:schurrule}, we have
\begin{align*}
s^{\la/\mu}(1-t)&=\sum_{\nu}s^{\nu/\mu}(1)s^{\la/\nu}(-t) \quad \text{(by sum rule)}\\
&=\sum_{\nu}(-1)^{|\la/\nu|}s^{\nu/\mu}(1)s^{\la^{t}/\nu^{t}}(t)\quad \text{(by duality rule)}\\
&=\sum_{\nu}(-t)^{|\la/\nu|}s^{\nu/\mu}(1)s^{\la^{t}/\nu^{t}}(1)\quad \text{(by homogeneity)}.
\end{align*}
It is well known that 
\begin{align*}
    s^{\nu/\mu}(1)=\begin{cases} 1& \text{if $\nu/\mu$ is a horizontal strip}\\ 0& \text{otherwise}\end{cases}\quad \text{and}\quad 
     s^{\la^{t}/\nu^{t}}(1)=\begin{cases} 1& \text{if $\la/\nu$ is a vertical strip}\\ 0& \text{otherwise}\end{cases},
\end{align*}
which yields that $s^{\la/\mu}(1-t)=0$ unless $\la$ is obtained from $\mu$ as follows: firstly add a horizontal strip to $\mu$ to obtain $\nu$ and then add a vertical strip to $\nu$ to get $\la$, i.e., $\la/\mu$ is a generalized ribbon. In this case, then each box in $\la/\mu$ satisfies one of the following (see Fig. \ref{F:hv}): 
\begin{enumerate}[label={(\roman*)}]
\item  There is a box of $\la/\mu$ immediately to the left (labeled by $h$);
\item There is a box of $\la/\mu$ immediately below it (labeled by $v$);
\item  Neither (i) nor (ii) holds (labeled by $*$).
\end{enumerate}
\begin{figure}
\begin{tikzpicture}[scale = 0.4]
      \draw [thick] (0,0) -| (1,3) -| (6,6) -| (9,7) -| (10,8) -| (15,9) -- (0,9) -- (0,0);
      \draw [thick] (0,3) -- (2,3);
      \draw [thick] (5,3) |- (9,7);
      \draw[thick] (10,8) -- (10,9);
      \begin{scope}
        \clip (0,0) -| (1,3) -- (0,3) -- (0,0);
        \draw [color=black!85] (0,0) grid (1,3);
      \end{scope}
      \begin{scope}
        \clip (5,3) -| (6,6) -| (9,7) -- (5,7) -- (5,3);
        \draw [color=black!85] (5,3) grid (9,7);
      \end{scope}
      \begin{scope}
        \clip (10,8) -| (15,9) -- (10,9) -- (10,8);
        \draw [color=black!85] (10,8) grid (15,9);
      \end{scope}
      \node [inner sep=2pt] at (0.5,0.5) { $*$}; 
       \node [inner sep=2pt] at (0.5,1.5) { $v$}; 
        \node [inner sep=2pt] at (0.5,2.5) { $v$}; 
         \node [inner sep=2pt] at (5.5,3.5) { $*$}; 
          \node [inner sep=2pt] at (5.5,4.5) { $v$}; 
           \node [inner sep=2pt] at (5.5,5.5) { $v$}; 
            \node [inner sep=2pt] at (5.5,6.5) { $v$}; 
             \node [inner sep=2pt] at (6.5,6.5) { $h$}; 
              \node [inner sep=2pt] at (7.5,6.5) { $h$}; 
               \node [inner sep=2pt] at (8.5,6.5) { $h$}; 
                \node [inner sep=2pt] at (10.5,8.5) { $*$}; 
                 \node [inner sep=2pt] at (11.5,8.5) { $h$}; 
                  \node [inner sep=2pt] at (12.5,8.5) { $h$}; 
                   \node [inner sep=2pt] at (13.5,8.5) { $h$}; 
                    \node [inner sep=2pt] at (14.5,8.5) { $h$}; 
    \end{tikzpicture}
    \caption{$\la$ is obtained from $\mu$ by adding a horizontal strip (to get $\nu$) and then adding a vertical strip (to $\nu$).}\label{F:hv}
    \end{figure}
Correspondingly, we have the following observations:
\begin{itemize}
    \item Each box in case (i) (resp. (ii)) must come from the application of the horizontal (resp. vertical) strip to $\mu$ and thus this box has weight $1$ (resp. $-t$);
    \item Each connected component (ribbon) $\xi_i$ in $\la/\mu$ has $c(\xi_i)-1$ (resp. $r(\xi_i)-1$) boxes in case (i) (resp. (ii));
\item Each connected component (ribbon) in $\la/\mu$ has exactly one box in case (iii), in which case this box has weight $1-t$.
\end{itemize}
Here $c(\xi_i)$ (resp. $r(\xi_i)$) presents the number of the columns (resp. rows) in $\xi_i$. Thus the product of these weights is exactly 
\begin{align*}
    (1-t)^{cc(\la/\mu)}\prod_{i}1^{c(\xi_i)-1}(-t)^{r(\xi_i)-1}=\wt(\la/\mu;t),
\end{align*}
which completes the proof.
\end{proof}

Suppose $\bm{\la}, \bm{\mu}\in \mathcal{P}_{n,m}$ and $\bm{\mu}\subset\bm{\la}$. We say $\bm{\la}/\bm{\mu}=(\la^{(1)}/\mu^{(1)},\cdots,\la^{(m)}/\mu^{(m)})$ is a {\it generalized $m$-multi-ribbon} if $\la^{(i)}/\mu^{(i)}$ is a generalized ribbon for all $1\leq i\leq m$. Analogously, we define
\begin{align}
cc(\bm{\la/\mu})&:=\sum_{i=1}^{m}cc(\la^{(i)}/\mu^{(i)}); \quad ht(\bm{\la/\mu}):=\sum_{i=1}^{m}ht(\la^{(i)}/\mu^{(i)}); \notag \\\label{e:defwt}
\wt(\bm{\la/\mu};t,\bm{u},r)&:=u^r_{\bm{\la/\mu}}\prod_{i=1}^{m}\wt(\la^{(i)}/\mu^{(i)};t)=u^r_{\bm{\la/\mu}}(1-t)^{cc(\bm{\la/\mu})}(-t)^{ht(\bm{\la/\mu})},
\end{align}
where $1\leq r\leq m$, $u_{\bm{\la/\mu}}:=u_s$ and $s$ presents the first non-empty entry in $\bm{\la/\mu}$ from right to left. For convention, we let $u_{\bla/\bla}:=1$. A generalized $m$-multi-ribbon $\bm{\la/\mu}$ is called a {\em $k$-generalized $m$-multi-ribbon} if $\sum_{i=1}^{m}|\la^{(i)}/\mu^{(i)}|=k$. Sometimes we will omit $m$, saying a generalized multi-ribbon for a generalized $m$-multi-ribbon in short.


\begin{exmp}
$\bm{\la/\mu}$ in \eqref{e:la/mu} is an $11$-generalized $5$-multi-ribbon. In this case, $cc(\bm{\la/\mu})=6$, $ht(\bm{\la/\mu})=1+1=2$ and $u_{\bla/\bmu}=u_5$. Thus, $\wt(\bm{\la/\mu};t,\bm{u},r)=u_5^rt^2(1-t)^6.$
\end{exmp}

With the above notations in hand, we are now in position to give the Murnaghan--Nakayama rule for the cyclotomic Hecke algebra, before which the following result is needed.
\begin{thm}\label{t:m-n}
Let $k$ be a non-negative integer and $1\leq r\leq m$, $\bm{\mu}\in \mathcal{P}_{n,m}$. Then
\begin{align}\label{e:m-n}
q^{(r)}_{k}(x;q,\bm{u})s_{\bm{\mu}}=\frac{q^k}{q-q^{-1}}\sum_{\bm{\la}}\wt(\bm{\la/\mu};q^{-2},\bm{u},r)s_{\bm{\la}}
\end{align}
summed over all multipartitions $\bm{\mu}\subset \bm{\la}\in\mathcal{P}_{n+k,m}$ such that $\bm{\la/\mu}$ is a $k$-generalized $m$-multi-ribbon.
\end{thm}
\begin{proof}
By definition, we have
\begin{align*}
q^{(r)}_{k}(x;q,\bm{u})s_{\bm{\mu}}=&\frac{q^k}{q-q^{-1}}\left(\sum_{c\in C_{k,m}}u^r_c\prod_{j=1}^{m}q_{c_j}(x^{(j)};q^{-2})\right)\prod_{i=1}^{m}s_{\mu^{(i)}}(x^{(i)})\\
=&\frac{q^k}{q-q^{-1}}\sum_{c\in C_{k,m}}u^r_c\prod_{j=1}^{m}q_{c_j}(x^{(j)};q^{-2})s_{\mu^{(j)}}(x^{(j)})\\
=&\frac{q^k}{q-q^{-1}}\sum_{c\in C_{k,m}}u^r_c\prod_{j=1}^{m}\left(\sum_{\la^{(j)}}\wt(\la^{(j)}/\mu^{(j)};q^{-2})s_{\la^{(j)}}(x^{(j)})\right)\quad \text{(by Lemma \ref{t:qs})}
\end{align*}
Swapping the inner summation and the product in the above equation implies that
\begin{align*}
q^{(r)}_{k}(x;q,\bm{u})s_{\bm{\mu}}=\frac{q^k}{q-q^{-1}}\sum_{c\in C_{k,m}}\sum_{\bm{\la}}\wt(\bm{\la/\mu};q^{-2},\bm{u},r)s_{\bm{\la}},
\end{align*}
where $\bm{\la}$ runs over all multipartitions $\bm{\mu}\subset \bm{\la}\in\mathcal{P}_{n+k,m}$ such that $\bm{\la/\mu}$ is a generalized multi-ribbon and $|\la^{(j)}/\mu^{(j)}|=c_j$, $j=1,2,\cdots,m$. This deduces \eqref{e:m-n}.
\end{proof}

As a straightforward result, the following corollary is an iterative formula for the irreducible characters, which is referred to as the Murnaghan--Nakayama rule.

\begin{cor}\label{t:m-n2}
Let $\bm{\la},\bm{\mu}\in \mathcal{P}_{n,m}$, $1\leq r\leq m$, $1\leq j\leq l(\mu^{(r)})$, then
\begin{align}\label{e:m-n2}
\chi_{\bm{\mu}}^{\bm{\la}}=\sum_{\bm{\nu}}\frac{q^{\mu^{(r)}_j}}{q-q^{-1}}\wt(\bm{\la/\nu};q^{-2},\bm{u},r)\chi^{\bm{\nu}}_{\bm{\mu}\setminus \mu^{(r)}_j}
\end{align}
summed over all multipartitions $\bm{\nu}\subset \bm{\la}$ such that $\bm{\la/\nu}$ is a $\mu^{(r)}_j$-generalized multi-ribbon, where $\bm{\mu}\setminus \mu^{(r)}_j$ is the multipartition obtained from $\bm{\mu}$ by removing the $j$-th part from the $r$-th partition $\mu^{(r)}$.
\end{cor}
\begin{proof}
By the Frobenius formula \eqref{e:fro}, we have
\begin{align}
q_{\bm{\mu}\setminus\mu^{(r)}_{j}}=\sum_{\bm{\nu}}\chi^{\bm{\nu}}_{\bm{\mu}\setminus\mu^{(r)}_{j}}s_{\bm{\nu}}.
\end{align}
Multiplying both sides by $q^{(r)}_{\mu^{(r)}_{j}}$ yields that
\begin{align}\label{e:I1}
\begin{split}
q_{\bm{\mu}}=&\sum_{\bm{\nu}}\chi^{\bm{\nu}}_{\bm{\mu}\setminus\mu^{(r)}_{j}}q^{(r)}_{\mu^{(r)}_{j}}s_{\bm{\nu}}\\
=&\sum_{\bm{\nu}}\chi^{\bm{\nu}}_{\bm{\mu}\setminus\mu^{(r)}_{j}}\frac{q^{\mu^{(r)}_{j}}}{q-q^{-1}}\sum_{\bm{\la}}\wt(\bm{\la/\nu};q^{-2},\bm{u},r)
s_{\bm{\la}} \quad\text{(by \eqref{e:m-n})}\\
=&\sum_{\bm{\la}}\sum_{\bm{\nu}}\chi^{\bm{\nu}}_{\bm{\mu}\setminus\mu^{(r)}_{j}}\frac{q^{\mu^{(r)}_{j}}}{q-q^{-1}}\wt(\bm{\la/\nu};q^{-2},\bm{u},r)
s_{\bm{\la}}
\end{split}
\end{align}
Note that $\{s_{\bm{\la}}\mid\bm{\la}\in \mathcal{P}_{n,m}\}$ forms an orthonormal basis in $\Lambda_{\mathbb{Q}}^{\otimes m}$. Comparing the coefficient of $s_{\bm{\la}}$ in \eqref{e:I1} and \eqref{e:fro} gives \eqref{e:m-n2}.
\end{proof}

\begin{exmp}
Suppose $\bm{\la}=((2,2),(4))$, $\bm{\mu}=((2,1),(3,2))$. Choose $r=j=2$. Then $\mu^{(r)}_{j}=2$ and there are $4$ $\bm{\nu}$'s such that $\bm{\la/\nu}$ is a $2$-generalized $2$-multi-ribbon. They are
\begin{align*}
\left(\begin{array}{cc}
\begin{tikzpicture}[scale = 0.33]
      \begin{scope}
        \clip (0,0) -| (2,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (2,2);
      \end{scope}
      \draw [thick] (0,0) -| (2,2) -- (0,2) -- (0,0);
      \draw [thick, rounded corners] (1.5,0.5) -- (1.5,1.5);
      \draw [color=black,fill=black,thick] (1.5,1.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (1.5,0.5) { }; 
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale = 0.33]
    \begin{scope}
        \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (4,1);
      \end{scope}
      \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
    \end{tikzpicture}
\end{array}\right)\quad
\left(\begin{array}{cc}
\begin{tikzpicture}[scale = 0.33]
      \begin{scope}
        \clip (0,0) -| (2,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (2,2);
      \end{scope}
      \draw [thick] (0,0) -| (2,2) -- (0,2) -- (0,0);
      \draw [thick, rounded corners] (0.5,0.5) -- (1.5,0.5);
      \draw [color=black,fill=black,thick] (1.5,0.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (0.5,0.5) { }; 
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale = 0.33]
    \begin{scope}
        \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (4,1);
      \end{scope}
      \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
    \end{tikzpicture}
\end{array}\right)\quad
\left(\begin{array}{cc}
\begin{tikzpicture}[scale = 0.33]
      \begin{scope}
        \clip (0,0) -| (2,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (2,2);
      \end{scope}
      \draw [thick] (0,0) -| (2,2) -- (0,2) -- (0,0);
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale = 0.33]
    \begin{scope}
        \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (4,1);
      \end{scope}
      \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
      \draw [thick, rounded corners] (2.5,0.5) -- (3.5,0.5);
      \draw [color=black,fill=black,thick] (3.5,0.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (2.5,0.5) { }; 
    \end{tikzpicture}
\end{array}\right)\quad
\left(\begin{array}{cc}
\begin{tikzpicture}[scale = 0.33]
      \begin{scope}
        \clip (0,0) -| (2,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (2,2);
      \end{scope}
      \draw [thick] (0,0) -| (2,2) -- (0,2) -- (0,0);
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (1.5,0.5) { }; 
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale = 0.33]
    \begin{scope}
        \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (4,1);
      \end{scope}
      \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (3.5,0.5) { }; 
    \end{tikzpicture}
\end{array}\right).
\end{align*}
The weights of these $2$-generalized $2$-multi-ribbons are $u_1^2(1-t)(-t)$, $u_1^2(1-t)$, $u_2^2(1-t)$ and $u_2^2(1-t)^2$ respectively. Therefore,
\begin{align*}
\chi^{((2,2),(4))}_{((2,1),(3,2))}=&\frac{q^2}{q-q^{-1}}
\left(u_1^2(1-q^{-2})(-q^{-2})\chi^{((1,1),(4))}_{((2,1),(3))} +u_1^2(1-q^{-2})\chi^{((2),(4))}_{((2,1),(3))}\right.\\
&\left.+u_2^2(1-q^{-2})\chi^{((2,2),(2))}_{((2,1),(3))} +u_2^2(1-q^{-2})^2\chi^{((2,1),(3))}_{((2,1),(3))} \right).
\end{align*}
\end{exmp}

For given $\bm{\la}\in\mathcal{P}_{n,m}$, a {\it generalized $m$-multi-ribbon tableau} $\bm{\T}$ of shape $\bm{\la}$ is defined as a sequence
\begin{align}
\bm{\T}: \quad \bm{\varnothing}=\bm{\la^{(0)}}\subset\bm{\la^{(1)}}\subset\cdots\subset\bm{\la^{(l-1)}}\subset\bm{\la^{(l)}}=\bm{\la}
\end{align}
such that $\bm{\la^{(i)}/\la^{(i-1)}}$ $(1\leq i\leq l)$ is a generalized $m$-multi-ribbon.

Define an {\it order} on the set $\{i_j\mid i\geq 1, j\geq 1\}$ by
\begin{align}
a_b\leq c_d\quad \Longleftrightarrow \quad a< c~~\text{or } a=c \text{, } b\leq d.
\end{align}

A generalized $m$-multi-ribbon tableau $\bm{\T}$ can also be described by a tuple of tableaux, in which the cells of each partition are marked $i_j$ $(i\geq 1, j\geq 1)$, satisfying
\begin{enumerate}[label=(\roman*)]
\item the numbers $i_j$ inserted in the diagram of each partition of $\bm{\T}$ must increase weakly down each column and along each row from left to right;
\item the cells marked same number consist of a generalized $m$-multi-ribbon.
\end{enumerate}
The {\it content} of $\bm{\T}$ is defined as a multicomposition $\bm{c}=(c^{(1)},c^{(2)},\cdots)$ such that $c^{(i)}_j$ equals the number of cells marked $i_j$ in $\bm{\T}$. For a given $\bm{\T}$, introduce a map $f_{\bm{\T}}:~ \{i_j\mid i\geq1, j\geq1, i_j\in\bm{\T}\} \rightarrow \{1,2,\cdots,m\}$ by
\begin{align*}
f_{\bm{\T}}:~ i_j \longmapsto  \text{the rightmost entry in $\bm{\T}$ containing $i_j$}.
\end{align*}
For a generalized multi-ribbon tableau $\bm{\T}$ of shape $\bm{\la}$ with content $\bm{\mu}$, we define the {\it weight} of $\bm{\T}$ by
\begin{align}
\wt(\bm{\T};\bm{u},t):=(1-t)^{cc(\bm{\T})}(-t)^{ht(\bm{\T})}\prod_{i=1}^m\prod_{j=1}^{l(\mu^{(i)})}u^{i}_{f_{\bm{\T}}(i_j)}
\end{align}
where
\begin{align*}
cc(\bm{\T}):=\sum_{i=1}^m\sum_{j=1}^{l(\mu^{(i)})}cc(\bm{\xi}(i_j)),\quad ht(\bm{\T}):=\sum_{i=1}^m\sum_{j=1}^{l(\mu^{(i)})}ht(\bm{\xi}(i_j))
\end{align*}
and $\bm{\xi}(i_j)$ is the generalized multi-ribbon marked $i_j$.

\begin{exmp}
Below is a generalized multi-ribbon tableau $\bm{\T}$ of shape $\bm{\la}=((4,3),(2),(1,1))$ with content $\bm{\mu}=((3,2),(4),(2))$. In this case, $f_{\bm{\T}}(1_1)=1$, $f_{\bm{\T}}(1_2)=1$, $f_{\bm{\T}}(2_1)=3$, $f_{\bm{\T}}(3_1)=3$.
\begin{align*}
\bm{\T}=
\setlength{\arraycolsep}{15pt}
\left( \begin{array}{ccc}
\begin{tikzpicture}[scale=0.6]
   \begin{scope}
        \clip (0,0) -| (3,1) -| (4,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (4,2);
      \end{scope}
      \draw [thick] (0,0) -| (3,1) -| (4,2) -- (0,2) -- (0,0);
    \node at(0.5,0.5) {$1_1$};
    \node at(0.5,1.5) {$1_1$};
    \node at(1.5,1.5) {$1_1$};
    \node at(1.5,0.5) {$1_2$};
    \node at(2.5,1.5) {$1_2$};
    \node at(2.5,0.5) {$2_1$};
    \node at(3.5,1.5) {$2_1$};
    \end{tikzpicture},&
    \begin{tikzpicture}[scale=0.6]
    \begin{scope}
        \clip (0,0) -| (2,1) -- (0,1) -- (0,0);
        \draw [color=black!25] (0,0) grid (2,1);
      \end{scope}
      \draw [thick] (0,0) -| (2,1) -- (0,1) -- (0,0);
    \node at(0.5,0.5) {$2_1$};
\node at(1.5,0.5) {$3_1$};
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale=0.6]
    \begin{scope}
        \clip (0,0) -| (1,2) -- (0,2) -- (0,0);
        \draw [color=black!25] (0,0) grid (1,2);
      \end{scope}
      \draw [thick] (0,0) -| (1,2) -- (0,2) -- (0,0);
\node at(0.5,1.5) {$2_1$};
\node at(0.5,0.5) {$3_1$};
    \end{tikzpicture}
\end{array}  \right)
\end{align*}
$cc(\bm{\T})=1+2+4+2=9$, $ht(\bm{\T})=1$. So $\wt(\bm{\T};\bm{u},t)=u_1\cdot u_1\cdot u_3^2\cdot u_3^3(1-t)^{9}(-t)=u_1^2u_3^5(-t)(1-t)^9$.
\end{exmp}

\begin{cor}\label{t:m-n3}
Suppose $\bm{\la},\bm{\mu}\in\mathcal{P}_{n,m}$, we have the following general formula for $\chi^{\bm{\la}}_{\bm{\mu}}$ in terms of generalized $m$-multi-ribbon tableaux as follows:
\begin{align}
\chi^{\bm{\la}}_{\bm{\mu}}=\frac{q^n}{(q-q^{-1})^{l(\bm{\mu})}}\sum_{\bm{\T}}\wt(\bm{\T};\bm{u},q^{-2})
\end{align}
summed over all generalized $m$-multi-ribbon tableaux of shape $\bm{\la}$ with content $\bm{\mu}$.
\end{cor}
\begin{proof}
It is straightforward by using Corollary \ref{t:m-n2} repeatedly.
\end{proof}


\subsection{Examples and numerical relations} Now we apply our Murnaghan--Nakayama rule to compute some irreducible characters in special cases and establish an equality relation. 
We use the short-hand notation $\bvar^{1}_j$ (resp. $\bvar^{n}_j$) to present the multipartition with $(1^n)$ (resp. $(n)$) in the $j$-th entry and $\varnothing$ anywhere else.
\begin{exmp}
    We list the following simple results coming from our Murnaghan--Nakayama rule.
    \begin{itemize}
        \item If we denote by $f^{\la^{(i)}}$ the number of standard Young tableaux of shape $\la^{(i)}$, which is given by 
        \begin{align*}
            f^{\la^{(i)}}=\frac{|\la^{(i)}|!}{\prod_{x\in\la^{(i)}}h_x}
        \end{align*}
        where $h_x$ is the hook length at $x$. Then we have 
        \begin{align}
           \chi^{\bla}_{\bvar^{1}_j}=\prod_{i=1}^m f^{\la^{(i)}}u_i^{j|\la^{(i)}|}. 
        \end{align}
        \item Denote $L(\bla)=\#\{i\mid \la^{(i)}\neq\varnothing\}$ and $s=\max\{i\mid \la^{(i)}\neq \varnothing\}$. Then 
        \begin{align}
            \chi^{\bla}_{\bvar^{n}_j}=
        \begin{cases}
            q^{n-1}u^j_s(1-q^{-2})^{L(\bla)-1}(-q^{-2})^{\sum_{i}b_i}, &\text{if $\la^{(i)}=(a_i,1^{b_i})$, $i=1,\cdots,m$}\\
            0, &\text{otherwise}.
        \end{cases}
        \end{align}
        \item Denote $\mathcal{L}_{\bm{\mu}\bm{\mu}}:=\sum_{i=1}^m i l(\mu^{(i)})$.\footnote{We adopt this notation to be consistent with that in Theorem \ref{t:Sq}.} Then 
        \begin{align}
        \chi_{\bmu}^{\bvar^{1}_j}=&(-q)^{l(\bmu)-n}u_j^{\mathcal{L}_{\bmu\bmu}};\\
          \chi_{\bmu}^{\bvar^{n}_j}=&q^{n-l(\bmu)}u_j^{\mathcal{L}_{\bmu\bmu}}.  
        \end{align}
    \end{itemize}
    \end{exmp}
\begin{prop}\label{p:replace}
    Let $\bmu$ be an arbitrary $m$-multipartition of $n$. Suppose for $1\leq j\leq m$
    $$\bla=(\varnothing,\cdots,\varnothing,\la^{(j)},\cdots,\la^{(m)}) \quad \text{and}\quad \bla'=(\la^{(j)},\varnothing,\cdots,\varnothing,\la^{(j+1)},\cdots,\la^{(m)}).$$
    Then
    \begin{align}\label{e:replace}
\chi^{\bla}_{\bmu}=\chi^{\bla'}_{\bmu}\Big|_{u_1\rightarrow u_j}
    \end{align}
    where $f\Big|_{u_1\rightarrow u_j}$
 means replacing $u_1$ by $u_j$ in $f$. 
 \end{prop}
 \begin{proof}
    We observe that there exists a natural one-to-one correspondence between the set of generalized multi-ribbon tableaux of shape $\bla$ with content $\bmu$ and those of shape $\bla'$ with content $\bmu$. Applying Corollary \ref{t:m-n3} to both $\chi^{\bla}_{\bmu}$ and $\chi^{\bla'}_{\bmu}$, we find that the presence of $u_j$ in some monomial $M$ of $\chi^{\bla}_{\bmu}$ is equivalent to the presence of $i_j$ exclusively in $\la^{(j)}$. Under this one-to-one correspondence, this is further equivalent to the presence of $u_1$ in the corresponding monomial $M'$ of $\chi^{\bla'}_{\bmu}$. Moreover, all other factors remain identical. The only difference between the factors of $M$ and $M'$ lies in the replacement of $u_1$ with $u_j$. Thus, $\chi^{\bla}_{\bmu}$ can be obtained from $\chi^{\bla'}_{\bmu}$ by substituting $u_1$ with $u_j$.
 \end{proof}
