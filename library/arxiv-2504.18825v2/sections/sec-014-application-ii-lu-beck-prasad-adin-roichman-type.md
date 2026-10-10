---
doc_id: arxiv-2504.18825v2
doc_title: "MURNAGHAN\u2013NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU"
section_id: sec-014-application-ii-lu-beck-prasad-adin-roichman-type
section_title: "Application II: Lu\u0308beck\u2013Prasad\u2013Adin\u2013Roichman-type formula"
section_number: 7
pages: 34-43
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.985
doc_brief: "MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU — 16 sections: Introduction; Preliminaries; Murnaghan–Nakayama rule for the cy"
---
\label{s:LPAR}
In this section, as the second application of our Murnaghan--Nakayama rule, we will establish a  L\"ubeck--Prasad--Adin--Roichman formula for the cyclotomic Hecke algebra $\mathscr{H}_{m,n}(q,\bm{u})$. To proceed with this, We will present an algorithm for $\chi^{(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})}_{\bmu}$ using the corresponding single partition $\la$ with empty $m$-core and $(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ as its $m$-quotient. Finally, we will explain how our formula recovers the Adin-Roichman formula for the complex reflection group $\mathscr{W}_{m,n}$ \cite{AR}, and particularly the L\"ubeck-Prasad formula for the hyperoctahedral group \cite{LP}.

\subsection{A restatement of the Murnaghan--Nakayama rule}
In this subsection, we restate the Murnaghan--Nakayama rule established in Section \ref{s:M-N} in terms of $\eta^{\bla}_{\btau;r}$ defined as below. 
\begin{defn}\label{d:eta}
    Let $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})\in \mathcal{P}_{n,m}$, $\btau=(\tau^{(1)},\tau^{(2)},\cdots,\tau^{(t)})$ be a $t$-tuple of partitions with each partition having at most $m$ parts and $r$ be a positive integer. Define $\eta^{\bla}_{\btau;r}$ as the sum of values obtained by all possible applications of the following algorithm:\\
    {\em Initialization}: $\varepsilon:=1$.
    \begin{enumerate}
        \item If $t=0$, end the program and output $\varepsilon$.
        \item If $l(\tau^{(t)})<m$, add $0$'s to the tail to make sure $\tau^{(t)}$ has $m$ components.
        \item Choose a permutation $\sigma\in \mathfrak{S}_m$. Remove a $\tau^{(t)}_{\sigma(j)}$-generalized ribbon $\theta_j$ from $\la^{(j)}$ for all $j=1,2,\cdots,m$. If there is no such $\sigma$ to do the removal process, set $\varepsilon=0$ and end the program.
        \item Multiply $\varepsilon$ by $u^r_{\m}(1-q^{-2})^{-1+\sum_{j=1}^{m}cc(\theta_j)}(-q^{-2})^{\sum_{j=1}^{m}ht(\theta_j)}$, where $cc(\theta_j)$ (resp. $ht(\theta_j)$) is the number of connected components (resp. the height) of $\theta_j$. And $\m:=\max\{1\leq j\leq m\mid \tau^{(t)}_{\sigma(j)}\neq 0\}$.
        \item Redefine $\btau:=(\tau^{(1)},\tau^{(2)},\cdots,\tau^{(t-1)})$ and $t:=t-1$.
        \item Return to step (1). 
    \end{enumerate}
\end{defn}
Figure \ref{F:remove} presents four possible removal processes. 
\begin{figure}
	\centering
	
    \begin{tikzpicture}[>=Stealth, line width=.9pt, every node/.style={inner sep=0pt}]

\node (root) at (0,0)   {$\left(\YDthreeone\qquad\YDtwoonone\qquad\YDtwtwo\right)$};

\node (L)    at (-4,-3) {$\left(\YDtwo\quad\YDtwoonone\quad\YDtwtwo\right)$};
\node (R)    at ( 4,-3) {$\left(\YDonesone\quad\YDtwoonone\quad\YDtwtwo\right)$};

\node (LL)   at (-6,-6) {$\left(\YDtwo\quad\YDfourcol\quad\YDtwtwo\right)$};
\node (LR)   at (-2,-6) {$\left(\YDtwo\quad\YDtweone\quad\YDtwtwo\right)$};

\node (RL)   at ( 2,-6) {$\left(\YDonesone\quad\YDfourcol\quad\YDtwtwo\right)$};
\node (RR)   at ( 6,-6) {$\left(\YDonesone\quad\YDtweone\quad\YDtwtwo\right)$};


\draw[->,shorten <=6pt,shorten >=6pt] (root) -- (L);
\draw[->,shorten <=6pt,shorten >=6pt] (root) -- (R);

\draw[->,shorten <=6pt,shorten >=6pt] (L) -- (LL);
\draw[->,shorten <=6pt,shorten >=6pt] (L) -- (LR);

\draw[->,shorten <=6pt,shorten >=6pt] (R) -- (RL);
\draw[->,shorten <=6pt,shorten >=6pt] (R) -- (RR);

\end{tikzpicture}
	\caption{Four possible removal processes for $\eta^{(3,1),(2,1,1),(2,2)}_{(2,1);r}$. Here $t=1$ and we choose $\sigma=id$. The sum terms they contribute are respectively $u^r_2(1-q^{-2})^3(-q^{-2})^0$, $u^r_2(1-q^{-2})^3(-q^{-2})^0$, $u^r_2(1-q^{-2})^2(-q^{-2})^0$ and $u^r_2(1-q^{-2})^2(-q^{-2})^0$.}\label{F:remove}
\end{figure}

For a partition $\mu=(\mu_1,\mu_2,\cdots,\mu_t)$ $(\mu_t>0)$, define $\mathcal{P}_m(\mu):=\{(\tau^{(1)},\tau^{(2)},\cdots,\tau^{(t)})\mid \tau^{(j)}\vdash \mu_j ~\text{and}~ l(\tau^{(j)})\leq m, 1\leq j\leq t\}$. Let $\bla,\bmu\in\mathcal{P}_{n,m}$. Then we have the following restatement of the Murnaghan--Nakayama rule:
\begin{align}\label{e:restate-MN}
    \chi^{\bla}_{\bmu}=q^{n-l(\bmu)}\sum_{r=1}^m\sum_{\btau\in\mathcal{P}_m(\mu^{(r)})}\eta^{\bla}_{\btau;r}.
\end{align}

\subsection{A  L\"ubeck--Prasad--Adin--Roichman-type formula}
Now, we will identify a partition $\la$ with its {\em boundary sequence} $\partial(\la)$, which is a finite $0/1$ sequence constructed as follows: commence at the southwestern vertex of the diagram of $\la$, and traverse along the edges of the southeastern boundary proceeding towards the northeastern vertex; represent each horizontal movement by a $1$, and each vertical movement by a $0$. Clearly, $\la$ is determined by its boundary sequence $\partial(\la)$ and invariant under adding $0$'s (resp. $1$'s) to the head (resp. tail) of $\partial(\la)$. We define the {\em anchor} of $\partial(\la)=(s_1,s_2,\cdots,s_t)$ is the position $i$ such that $\#\{1\leq j\leq i\mid s_j=1\}=\#\{i+1\leq j\leq t\mid s_j=0\}$. We usually insert a vertical line ``$\mid$" into $\partial(\la)$ to indicate the anchor. See Figure \ref{F:partial} for an example. 
\begin{figure}
\begin{tikzpicture}[scale=0.5]
    \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (14,0);
    \coordinate (YAxisMin) at (0,0);
    \coordinate (YAxisMax) at (0,-14);
    \draw [thin, black] (0,0) -- (7,0);
    \draw [thin, black] (0,-1) --(7,-1);
    \draw [thin, black] (0,-2) -- (7,-2);
    \draw [thin, black] (0,-3) -- (7,-3);
    \draw [thin, black] (0,-4) -- (6,-4);
    \draw [thin, black] (0,-5) -- (3,-5);
    \draw [thin, black] (0,-6) -- (3,-6);
    \draw [thin, black] (0,-7) -- (2,-7);
     \draw [thin, black] (0,-8) -- (1,-8);
     \draw [thin, black] (0,0) -- (0,-8);
     \draw [thin, black] (1,0) -- (1,-8);
      \draw [thin, black] (2,0) -- (2,-7);
     \draw [thin, black] (3,0) -- (3,-6);
     \draw [thin, black] (4,0) -- (4,-4);
     \draw [thin, black] (5,0) -- (5,-4);
      \draw [thin, black] (6,0) -- (6,-4);
      \draw [thin, black] (7,0) -- (7,-3);
      \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (0,-8) -- (1,-8);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (1,-8) -- (1,-7);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (1,-7) -- (2,-7);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (2,-7) -- (2,-6);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (2,-6) -- (3,-6);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (3,-6) -- (3,-5);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (3,-5) -- (3,-4);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (3,-4) -- (4,-4);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (4,-4) -- (5,-4);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (5,-4) -- (6,-4);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (6,-4) -- (6,-3);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (6,-3) -- (7,-3);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (7,-3) -- (7,-2);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (7,-2) -- (7,-1);
        \draw[postaction={decorate}, decoration={markings, 
        mark=at position 0.6 with {\arrow{stealth}}}] (7,-1) -- (7,0);
     \end{tikzpicture}
    \caption{$\la=(7,7,7,6,3,3,2,1)$, the boundary of $\la$ is marked by arrows. Thus, $\partial(\la)=10101001 \mid 1101000$ and the anchor of $\partial(\la)$ is $8$.}\label{F:partial}
    \end{figure}

Now we describe the bijection $\Psi_m$ between the set of $m$-multipartitions of $n$ (denoted by $\mathcal{P}_{n,m}$) and the set of partitions of $mn$ with empty $m$-core (denoted by $\mathcal{P}^{0}_{mn}$). Here, the $m$-core of a partition $\la$ is obtained by removing as many $m$-ribbons from $\la$ as possible.

\begin{defn}\label{d:quotient}
   For a given $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})\in \mathcal{P}_{n,m}$, suppose $\partial(\la^{(i)})=(s^{(i)}_{1},\cdots,s^{(i)}_{d})$, $i=1,2,\cdots,m$. Here we add the leading $0$'s and trailing $1$'s to make $\partial(\la^{(i)})$ have the same length $d$ and the same anchor for all $1\leq i\leq m$. We let $\Psi_m(\bla)$ be the unique partition such that $\partial(\Psi_m(\bla))$ is
   \begin{align*}       s^{(1)}_{1},s^{(2)}_1,\cdots,s^{(m)}_1,s^{(1)}_{2},s^{(2)}_2,\cdots,s^{(m)}_2,\cdots,s^{(1)}_{d},s^{(2)}_d,\cdots,s^{(m)}_d.
   \end{align*}
We claim $\Psi_m$ is a bijection. Indeed, $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ is the $m$-quotient of $\Psi_m(\bla)$. Moreover, we have $|\Psi_m(\bla)|=m|\bla|$ (see also \cite[Remark 2.9]{AR}).    
\end{defn}

\begin{exmp}
    We choose $\bla$ as follows:
    \begin{align*}
\setlength{\arraycolsep}{15pt}
\left( \begin{array}{ccc}
\begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (3,0);
    \draw [thin, black] (0,-1) -- (3,-1);
    \draw [thin, black] (0,-2) -- (1,-2);
    
    \draw [thin, black] (0,0) -- (0,-2);
    \draw [thin, black] (1,0) -- (1,-2);
    \draw [thin, black] (2,0) -- (2,-1);
    \draw [thin, black] (3,0) -- (3,-1);
    \end{tikzpicture},&
    \begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (2,0);
    \draw [thin, black] (0,-1) -- (2,-1);
    \draw [thin, black] (0,-2) -- (1,-2);
    \draw [thin, black] (0,-3) -- (1,-3);
    \draw [thin, black] (0,0) -- (0,-3);
    \draw [thin, black] (1,0) -- (1,-3);
    \draw [thin, black] (2,0) -- (2,-1);
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (2,0);
    \draw [thin, black] (0,-1) -- (2,-1);
    \draw [thin, black] (0,-2) -- (2,-2);
    \draw [thin, black] (0,0) -- (0,-2);
    \draw [thin, black] (1,0) -- (1,-2);
     \draw [thin, black] (2,0) -- (2,-2);
    \end{tikzpicture}
\end{array}  \right).
\end{align*}
The boundary sequence of each component of $\bla$ is $10\mid110$, $100\mid10$ and $11\mid00$, respectively. Add the leading $0$'s and tailing $1$'s to make sure they have the same length and the same anchor. So their boundary sequences can be presented as follows:
\begin{align*}
    010 \mid 110 \\ 
100 \mid 101\\ 
011 \mid 001 \\ 
\end{align*}









Therefore, the boundary sequence of $\Psi_{m}(\bla)$ is $010101001\mid110100011$. This is exactly the partition in Figure \ref{F:partial} when remove the leading $0$'s and the tailing $1$'s.
\end{exmp}

\begin{figure}
\begin{tikzpicture}[scale=0.5]
    \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (14,0);
    \coordinate (YAxisMin) at (0,0);
    \coordinate (YAxisMax) at (0,-14);
    \draw [thin, black] (0,0) -- (7,0);
    \draw [thin, black] (0,-1) --(7,-1);
    \draw [thin, black] (0,-2) -- (7,-2);
    \draw [thin, black] (0,-3) -- (7,-3);
    \draw [thin, black] (0,-4) -- (6,-4);
    \draw [thin, black] (0,-5) -- (3,-5);
    \draw [thin, black] (0,-6) -- (3,-6);
    \draw [thin, black] (0,-7) -- (2,-7);
     \draw [thin, black] (0,-8) -- (1,-8);
     \draw [thin, black] (0,0) -- (0,-8);
     \draw [thin, black] (1,0) -- (1,-8);
      \draw [thin, black] (2,0) -- (2,-7);
     \draw [thin, black] (3,0) -- (3,-6);
     \draw [thin, black] (4,0) -- (4,-4);
     \draw [thin, black] (5,0) -- (5,-4);
      \draw [thin, black] (6,0) -- (6,-4);
      \draw [thin, black] (7,0) -- (7,-3);
       \node at(-0.5,-0.5) {$1$};
       \node at(-0.5,-1.5) {$3$};
       \node at(-0.5,-2.5) {$2$};
       \node at(-0.5,-3.5) {$3$};
       \node at(-0.5,-4.5) {$2$};
       \node at(-0.5,-5.5) {$1$};
       \node at(-0.5,-6.5) {$2$};
       \node at(-0.5,-7.5) {$3$};
        \filldraw[fill = green]
     (4,-3) rectangle (5,-4)
     (5,-3) rectangle (6,-4)
     (5,-2) rectangle (6,-3) 
     (6,-2) rectangle (7,-3) 
     (6,-1) rectangle (7,-2)
     (6,0) rectangle (7,-1) 
     (1,-6) rectangle (2,-7)
     (1,-5) rectangle (2,-6) 
     (2,-5) rectangle (3,-6); 
     \end{tikzpicture}
    \caption{$\tilde{\partial}(\la)=010101001 \mid 110100011$, $k(\tilde{\partial}(\la))=9$ and the row-color sequence is marked in the leftmost column. Thus, the green generalized ribbon is colored by $1$.}\label{F:row-color}
    \end{figure}


\begin{lem}\label{l:fact}
    Let $\la=(\la_1,\cdots,\la_l)$ $(\la_l\geq 0)$ be a partition with its boundary sequence $\partial(\la)=(s_1,s_2,\cdots)$. We collect the following facts from \cite{AR}:
    \begin{enumerate}
\item Removing a $k$-ribbon from $\la$ is equivalent to exchanging $s_{i}=1$ with $s_{i+k}=0$, for some $i$.
   \item The position in $\partial(\la)$ of the zero corresponding to $\la_i$ is equal to $\la_i+l-i+1$. 
     
    \end{enumerate}
\end{lem}


For a given partition $\la$ with empty $m$-core and length $l$, denote by $\tilde{\partial}(\la)$ the boundary sequence given by Definition \ref{d:quotient} (before removing the leading $0$'s and the tailing $1$'s). Note that $\tilde{\partial}(\la)$ relies on the choice of $\partial(\la^{(1)}), \partial(\la^{(2)}),\cdots,\partial(\la^{(m)})$. Define $k(\tilde{\partial}(\la)):=\#\{j\mid \tilde{\partial}(\la)_j=0\}$. We define the {\em row-color sequence} $a(\la)$ of $\la$ by $a(\la):=(a_1,\cdots,a_l)$, where $1\leq a_i\leq m$ and $a_i\equiv \la_i+k(\tilde{\partial}(\la))-i+1 ~({\rm mod}~ m)$, $i=1,2,\cdots,l$.\footnote{We remark that the definition of the row-color sequence is slightly different from that in \cite[Definition 3.3]{AR}.} We claim that $a(\la)$ is independent of the choice of $\tilde{\partial}(\la)$. Indeed, if we have another boundary sequence $\hat{\partial}(\la)$ obtained from Definition \ref{d:quotient} via distinct choice of $\partial(\la^{(1)}), \partial(\la^{(2)}),\cdots,\partial(\la^{(m)})$, then $m\mid(k(\tilde{\partial}(\la))-k(\hat{\partial}(\la)))$, which implies they gives the same $a(\la)$ by definition. 

We say the {\em starting point} (resp. {\em ending point}) of a ribbon is the northeastmost (resp. southwestmost) box of the ribbon. A ribbon is {\em colored by $i$} if the row-color of the row containing the starting point of the ribbon equals $i$. That is, if the starting point is in the $j$-th row then $a_j=i$. More generally, We say a generalized ribbon is colored by $i$ if all of its connected components are colored by $i$. See Figure \ref{F:row-color} for an example.

\begin{prop}\label{p:equiv}
    Let $\la$ be a partition with empty $m$-core and $m$-quotient $(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$. We have that removing a $k$-generalized ribbon with $p$ connected components from $\la^{(i)}$ is equivalent to removing a $km$-generalized ribbon with $p$ connected components colored by $i$ from $\la$. 
\end{prop}
\begin{proof}  
Suppose $\partial(\la^{(i)})=(s^{(i)}_1,s^{(i)}_2,\cdots)$ is the boundary sequence of $\la^{(i)}$ and $\tilde{\partial}(\la)=(s_1,s_2,\cdots)$ is the boundary sequence given by Definition \ref{d:quotient}. By Lemma \ref{l:fact} (1), removing a $k$-generalized ribbon with $p$ connected components from $\la^{(i)}$ is equivalent to exchanging $s^{(i)}_{i_1}=1$ with $s^{(i)}_{j_1}=0$, $s^{(i)}_{i_2}=1$ with $s^{(i)}_{j_2}=0$, $\cdots$, $s^{(i)}_{i_p}=1$ with $s^{(i)}_{j_p}=0$ in $\partial(\la^{(i)})$ for some $i_1<j_1<i_2<j_2<\cdots<i_p<j_p$ such that $\sum_{a=1}^p(j_a-i_a)=k$. It follows from the definition of $\Psi_m$ that this is further equivalent to exchanging $s_{u_1}=1$ with $s_{v_1}=0$, $s_{u_2}=1$ with $s_{v_2}=0$, $\cdots$, $s_{u_p}=1$ with $s_{v_p}=0$ such that $\sum_{a=1}^p(v_a-u_a)=km$ and $u_a\equiv v_a\equiv i~({\rm mod}~m)$, $1\leq a\leq p$. Lemma \ref{l:fact} (1) implies that this is equivalent to removing a $km$-generalized ribbon with $p$ connected components from $\la$. If we assume the starting points of the connected components of this $km$-generalized ribbon are respectively in the row $t_1, t_2,\cdots, t_p$ in $\la$, then Lemma \ref{l:fact} (2) yields that $\la_{t_a}+k(\tilde{\partial}(\la))-t_a+1=v_a$, $1\leq a\leq p$. So $\la_{t_a}+k(\tilde{\partial}(\la))-t_a+1\equiv i~({\rm mod}~m)$, $1\leq a\leq p$, i.e., this $km$-generalized ribbon is colored by $i$, which completes the proof.
\end{proof}

\begin{exmp}
 If we remove the generalized ribbon (its two components are in color yellow and green) from $\la^{(2)}=(2,1,1)$ as follows:   
\begin{align*}
\setlength{\arraycolsep}{15pt}
\left( \begin{array}{ccc}
\begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (3,0);
    \draw [thin, black] (0,-1) -- (3,-1);
    \draw [thin, black] (0,-2) -- (1,-2);
    
    \draw [thin, black] (0,0) -- (0,-2);
    \draw [thin, black] (1,0) -- (1,-2);
    \draw [thin, black] (2,0) -- (2,-1);
    \draw [thin, black] (3,0) -- (3,-1);
    \end{tikzpicture},&
    \begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (2,0);
    \draw [thin, black] (0,-1) -- (2,-1);
    \draw [thin, black] (0,-2) -- (1,-2);
    \draw [thin, black] (0,-3) -- (1,-3);
    \draw [thin, black] (0,0) -- (0,-3);
    \draw [thin, black] (1,0) -- (1,-3);
    \draw [thin, black] (2,0) -- (2,-1);
     \filldraw[fill = green]
     (0,-1) rectangle (1,-2) (0,-2) rectangle (1,-3); 
     \filldraw[fill = yellow]
     (1,0) rectangle (2,-1);
    \end{tikzpicture}~,&
    \begin{tikzpicture}[scale=0.6]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,0) -- (2,0);
    \draw [thin, black] (0,-1) -- (2,-1);
    \draw [thin, black] (0,-2) -- (2,-2);
    \draw [thin, black] (0,0) -- (0,-2);
    \draw [thin, black] (1,0) -- (1,-2);
     \draw [thin, black] (2,0) -- (2,-2);
    \end{tikzpicture}
\end{array}  \right).
\end{align*}
This is equivalent to removing the following generalized ribbon colored by $2$ (its two components are in color yellow and green) from $(7,7,7,6,3,3,2,1)$:
\begin{gather*}
\begin{tikzpicture}[scale=0.5]
    \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (14,0);
    \coordinate (YAxisMin) at (0,0);
    \coordinate (YAxisMax) at (0,-14);
    \draw [thin, black] (0,0) -- (7,0);
    \draw [thin, black] (0,-1) --(7,-1);
    \draw [thin, black] (0,-2) -- (7,-2);
    \draw [thin, black] (0,-3) -- (7,-3);
    \draw [thin, black] (0,-4) -- (6,-4);
    \draw [thin, black] (0,-5) -- (3,-5);
    \draw [thin, black] (0,-6) -- (3,-6);
    \draw [thin, black] (0,-7) -- (2,-7);
     \draw [thin, black] (0,-8) -- (1,-8);
     \draw [thin, black] (0,0) -- (0,-8);
     \draw [thin, black] (1,0) -- (1,-8);
      \draw [thin, black] (2,0) -- (2,-7);
     \draw [thin, black] (3,0) -- (3,-6);
     \draw [thin, black] (4,0) -- (4,-4);
     \draw [thin, black] (5,0) -- (5,-4);
      \draw [thin, black] (6,0) -- (6,-4);
      \draw [thin, black] (7,0) -- (7,-3);
       \node at(-0.5,-0.5) {$1$};
       \node at(-0.5,-1.5) {$3$};
       \node at(-0.5,-2.5) {$2$};
       \node at(-0.5,-3.5) {$3$};
       \node at(-0.5,-4.5) {$2$};
       \node at(-0.5,-5.5) {$1$};
       \node at(-0.5,-6.5) {$2$};
       \node at(-0.5,-7.5) {$3$};
        \filldraw[fill = green]
     (0,-7) rectangle (1,-8) (0,-6) rectangle (1,-7) (1,-6) rectangle (2,-7) (1,-5) rectangle (2,-6) (2,-5) rectangle (3,-6) (2,-4) rectangle (3,-5); 
     \filldraw[fill = yellow]
     (5,-3) rectangle (6,-4) (5,-2) rectangle (6,-3) (6,-2) rectangle (7,-3);
     \end{tikzpicture}
  \end{gather*}
\end{exmp}

For any finite sequence $\bm{a}=(a_1,a_2,\cdots)$, we define its {\em inversion number} by  \begin{align*}
        {\rm inv}(\bm{a}):=\# \{(i,j)\mid i<j, a_i>a_j\}.
    \end{align*}
Let $a(\la)=(a_1,a_2,\cdots,a_l)$ be the row-color sequence of $\la$. Define its {\em $m$-inversion number} by
    \begin{align*}
        {\rm inv}_m(\la):={\rm inv}(a(\la)).
    \end{align*}
For any finite sequence $\bm{a}=(a_1,\cdots,a_d)$, we assume that $\bm{b}=(b_1,\cdots,b_d)$ is a permutation of $\bm{a}$. Define $\I(\bm{a};\bm{b})$ by
\begin{align*}
    \I(\bm{a};\bm{b}):=\min\{{\rm inv}(\sigma)\mid \sigma\in\mathfrak{S}_d, ~\text{such that}~a_i=b_{\sigma(i)}~\text{for all}~ i=1,2,\cdots,d\}.
\end{align*}
Here the permutation $\sigma$ is viewed as a word (or sequence). For instance, 
$\sigma=(13254)$ is identified with the word $35214$ for the reason that
\begin{align*}
\sigma=
   \begin{pmatrix}1 &  2 & 3 & 4 & 5 \\
 3 & 5 & 2 & 1 &4
\end{pmatrix}. 
\end{align*}
For example, we choose $\bm{a}=(1,2,5,1,3,2,7)$, $\bm{b}=(2,5,1,3,2,7,1)$. Then the permutation $\sigma$ with the minimal inversion number satisfying $a_i=b_{\sigma(i)}$ is $3127456$. So $\I(\bm{a};\bm{b})=5$.

\begin{rem}\label{r:graph}
    $\I(\bm{a};\bm{b})$ can be computed graphically. Indeed, $\I(\bm{a};\bm{b})$ is equal to the minimal value of all possible applications of the following process:
    \begin{enumerate}
        \item Put sequences $\bm{a}$ and $\bm{b}$ in two rows and align them;
        \item  Connect the same number in the generic manner: no three lines intersect at one point;
         \item  Count the intersection number of the lines.
    \end{enumerate}
    In the above example, we can draw the lines, which produce the minimal intersection number as follows:
    \begin{gather*}
     \begin{tikzpicture}[scale=0.8]
   \coordinate (Origin)   at (0,0);
    \coordinate (XAxisMin) at (0,0);
    \coordinate (XAxisMax) at (4,0);
    \coordinate (YAxisMin) at (0,-3);
    \coordinate (YAxisMax) at (0,0);
\draw [thin, black] (0,-0.3) -- (2,-1.7);
    \draw [thin, black] (1,-0.3) -- (0,-1.7);
    \draw [thin, black] (2,-0.3) -- (1,-1.7);
    
    \draw [thin, black] (3,-0.3) -- (6,-1.7);
    \draw [thin, black] (4,-0.3) -- (3,-1.7);
    \draw [thin, black] (5,-0.3) -- (4,-1.7);
    \draw [thin, black] (6,-0.3) -- (5,-1.7);
    
    \node at(0,0) {$1$}; \node at(1,0) {$2$}; \node at(2,0) {$5$}; \node at(3,0) {$1$}; \node at(4,0) {$3$}; \node at(5,0) {$2$};\node at(6,0) {$7$};
    \node at(0,-2) {$2$}; \node at(1,-2) {$5$}; \node at(2,-2) {$1$}; \node at(3,-2) {$3$}; \node at(4,-2) {$2$}; \node at(5,-2) {$7$};\node at(6,-2) {$1$};
    \end{tikzpicture} 
    \end{gather*}
    So $\I(\bm{a};\bm{b})=5$.
\end{rem}



\begin{lem}\label{l:inv}
    Let $\la^{'}$ be a partition obtained from $\la$ by removing a generalized ribbon with connected components $\xi_1,\xi_2,\cdots,\xi_p$. Suppose $u_i$ and $v_i$ are respectively the indices of the rows in $\la$ containing the starting point and ending point of $\xi_i$ $(1\leq i\leq p)$ such that $u_1<v_1<u_2<v_2<\cdots<u_p<v_p$. If we assume the row-color sequence of $\la$ is
    \begin{align*}
        a(\la)=(\cdots,\underbrace{a_{u_1},\cdots,a_{v_1}}_{v_1-u_1+1},\cdots,\underbrace{a_{u_2},\cdots,a_{v_2}}_{v_2-u_2+1},\cdots,\underbrace{a_{u_p},\cdots,a_{v_p}}_{v_p-u_p+1},\cdots).
    \end{align*}
  Then we have
\begin{align}
     a(\la^{'})=(\cdots,\underbrace{a_{u_{1}+1},\cdots,a_{v_1},a_{u_1}}_{v_1-u_1+1},\cdots,&\underbrace{a_{u_{2}+1},\cdots,a_{v_2},a_{u_2}}_{v_2-u_2+1},\cdots,\underbrace{a_{u_{p}+1},\cdots,a_{v_p},a_{u_p}}_{v_p-u_p+1},\cdots);\label{e:ala}\\
     \I(\la/\la^{'}):=\I(a(\la);a(\la^{'}))&=\sum_{i=1}^p\#\{j\mid u_i<j\leq v_i, a_j\neq a_{u_i}\}; \label{e:I}\\
     (-1)^{{\rm inv}_m(\la)-{\rm inv}_m(\la^{'})}&=(-1)^{\I(\la/\la^{'})}.\label{e:iI}
\end{align}
\end{lem}
\begin{proof}
    \eqref{e:ala} can be obtained by using the same arguments as those in \cite[Lemma 3.5]{AR}. \eqref{e:I} follows from \eqref{e:ala} by definition (or Remark \ref{r:graph}). Now we show \eqref{e:iI}. It follows from \eqref{e:ala} that 
    \begin{align*}
        {\rm inv}_m(\la)-{\rm inv}_m(\la^{'})=\sum_{i=1}^p\big(\#\{j\mid u_i<j\leq v_i, a_j< a_{u_i}\}-\#\{j\mid u_i<j\leq v_i, a_j> a_{u_i}\}\big),
    \end{align*}
 which has the same parity as $\I(\la/\la^{'})$ by \eqref{e:I}. This completes the proof.   
\end{proof}

\begin{defn}\label{d:eta'}
 Let $\la$ be a partition of $mn$, $\btau=(\tau^{(1)},\tau^{(2)},\cdots,\tau^{(t)})$ be a $t$-tuple of partitions with each partition having at most $m$ parts and $r$ be a positive integer. Define $\eta^{\la}_{\btau;r}$ as the sum of values obtained by all possible applications of the following algorithm:\\
 {\em Initialization}: $\varepsilon:=1$.
    \begin{enumerate}
        \item If $t=0$, end the program and output $\varepsilon$.
        \item If $l(\tau^{(t)})<m$, add $0$'s to the tail to make sure $\tau^{(t)}$ has $m$ components.
        \item Choose a permutation $\sigma\in \mathfrak{S}_m$. Remove a $m\tau^{(t)}_{\sigma(1)}$-generalized ribbon $\theta^{'}_1$ colored by $1$ from $\la$, and then remove a $m\tau^{(t)}_{\sigma(2)}$-generalized ribbon $\theta^{'}_2$ colored by $2$ from $\la/\theta^{'}_1$. Continue this process until we remove a $m\tau^{(t)}_{\sigma(m)}$-generalized ribbon $\theta^{'}_{m}$ colored by $m$ from $\la/(\theta^{'}_1\cup\cdots\cup\theta^{'}_{m-1})$. If there is no such $\sigma$ to do the removal process, set $\varepsilon=0$ and end the program.
        \item Multiply $\varepsilon$ by $u^r_{\m}(1-q^{-2})^{-1+\sum_{j=1}^{m}cc(\theta^{'}_j)}(-q^{-2})^{\sum_{j=1}^{m}(ht(\theta^{'}_j)-\I(\theta^{'}_j))}$, where $cc(\theta^{'}_j)$ (resp. $ht(\theta^{'}_j)$) is the number of connected components (resp. the height) of $\theta^{'}_j$. And $\m:=\max\{1\leq j\leq m\mid \tau^{(t)}_{\sigma(j)}\neq 0\}$.
        \item Redefine $\btau:=(\tau^{(1)},\tau^{(2)},\cdots,\tau^{(t-1)})$ and $t:=t-1$.
        \item Return to step (1). 
    \end{enumerate}
\end{defn}

Now we are ready to give a L\"ubeck--Prasad--Adin--Roichman formula for the cyclotomic Hecke algebra, computing the irreducible characters by using partitions instead of $m$-multipartitions.
\begin{thm}\label{t:AR}
Let $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)}),\bmu\in \mathcal{P}_{n,m}$. We assume that $\la$ is the unique partition with empty $m$-core and $(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ as its $m$-quotient. Then we have
\begin{align}\label{e:AR}
    \chi^{\bla}_{\bmu}=q^{n-l(\bmu)}\sum_{r=1}^m\sum_{\btau\in\mathcal{P}_m(\mu^{(r)})}\eta^{\la}_{\btau;r},
\end{align}
    
    
    
    
    
    
    
    
    
    
\end{thm}
\begin{proof}
    By \eqref{e:restate-MN}, Definition \ref{d:eta} and Proposition \ref{p:equiv}, it suffices to show that $\eta^{\bla}_{\btau;r}=\eta^{\la}_{\btau;r}$, for which it is sufficient to verify that the factors of corresponding removal process under the bijection established in Proposition \ref{p:equiv} differ by some power of $-q^{-2}$. To be precise, if we remove a $k$-generalized ribbon $\theta_i$ with height $ht(\theta_{i})$ from $\la^{(i)}$, which, due to Proposition \ref{p:equiv}, is equivalent to removing a $km$-generalized ribbon $\theta^{'}_i$ colored by $i$ with height $ht(\theta^{'}_{i})$ from $\la$, then we need to verify $ht(\theta_i)=ht(\theta^{'}_i)-\I(\theta^{'}_i)$. For the sake of argument, we make the following assumptions:
    \begin{itemize}
        \item $\theta_i$ (resp. $\theta^{'}_i$) has $p$ connected components $\xi_1,\xi_2,\cdots,\xi_p$ (resp. $\xi^{'}_1,\xi^{'}_2,\cdots,\xi^{'}_p$).
        \item Let $u_1<v_1<u_2<v_2<\cdots<u_p<v_p$ (resp. $u^{(i)}_1<v^{(i)}_1<u^{(i)}_2<v^{(i)}_2<\cdots<u^{(i)}_p<v^{(i)}_p$) be the indices of rows in $\la$ (resp. $\la^{(i)}$) such that the $u_q$-th (resp. $u^{(i)}_q$-th) row and the $v_q$-th (resp. $v^{(i)}_q$-th) row contain respectively the starting point and ending point of $\xi^{'}_q$ (resp. $\xi_{q}$), $q=1,2,\cdots,p.$
        \item Let $b_1<d_1<b_2<d_2<\cdots<b_p<d_p$ (resp. $b^{(i)}_1<d^{(i)}_1<b^{(i)}_2<d^{(i)}_2<\cdots<b^{(i)}_p<d^{(i)}_p$) be the indices of positions in $\partial(\la)$ (resp. $\partial(\la^{(i)})$) such that we swap $s_{b_q}=1$ with $s_{d_q}=0$ (resp. $s^{i}_{b^{(i)}_q}=1$ with $s^{(i)}_{d^{(i)}_q}=0$) when remove $\xi^{'}_q$ (resp. $\xi_q$) from $\la$ (resp. $\la^{(i)}$).
    \end{itemize}
    Thus, with the above notations in hand, we have 
    $$ ht(\xi^{'}_q)=\#\{t\mid s_t=0, b_q\leq t<d_q\}, \quad ht(\xi_q)=\#\{t\mid s^{(i)}_t=0, b^{(i)}_q\leq t<d^{(i)}_q\}.$$
    By the definition of $\Psi_m$, we hence have 
    $$\#\{t\mid s^{(i)}_t=0, b^{(i)}_q\leq t<d^{(i)}_q\}=\#\{t\mid s_t=0, b_q\leq t<d_q, t\equiv i~({\rm mod}~ m)\}.$$
    Therefore, 
    \begin{align*}
        ht(\theta^{'}_i)-ht(\theta_i)=&\sum_{q=1}^p \big(ht(\xi_q^{'})-ht(\xi_q)\big)\\
        =&\sum_{q=1}^p \#\{t\mid s_t=0, b_q\leq t<d_q, t\not\equiv i~({\rm mod}~ m)\}\\
        =&\sum_{q=1}^p \#\{t\mid u_q< t\leq v_q, a_t\neq a_{u_q}\}\quad \text{(by the definition of $a(\la)$)}\\
        =&\I(\theta^{'}_i)\quad \text{(by Lemma \ref{l:inv})}.
    \end{align*}




















    This finishes the proof.
\end{proof}







\begin{figure}[ht]
\centering
\begin{tikzpicture}[>=Stealth, line width=.9pt, every node/.style={inner sep=0pt}]

\node (T)  at (0,0)        {\YDTop};
\node (ML) at (-4.5,-5.5)  {\YDMidL};
\node (MR) at ( 4.5,-5.5)  {\YDMidR};

\node (B1) at (-7,-11)  {\YDBotI};
\node (B2) at (-2,-11)  {\YDBotII};
\node (B3) at ( 2,-11)  {\YDBotIII};
\node (B4) at ( 6,-11)  {\YDBotIV};

\node[font=\small] at (0,-3.1) {Remove generalized ribbons colored by $1$};
\node[font=\small] at (-0.7,-7) {Remove generalized ribbons colored by $2$};

\draw[->,shorten <=10pt,shorten >=10pt] (T.south west) -- (ML.north);
\draw[->,shorten <=10pt,shorten >=10pt] (T.south east) -- (MR.north);

\draw[->,shorten <=8pt,shorten >=8pt] (ML.south west) -- (B1.north);
\draw[->,shorten <=8pt,shorten >=8pt] (ML.south east) -- (B2.north);

\draw[->,shorten <=8pt,shorten >=8pt] (MR.south west) -- (B3.north);
\draw[->,shorten <=8pt,shorten >=8pt] (MR.south east) -- (B4.north);

\end{tikzpicture}
\caption{Four removal processes corresponding to those in Figure \ref{F:remove}. The sum terms they contribute are same as those in Figure \ref{F:remove}.}\label{F:remove2}
\end{figure}

\begin{exmp}
    Figure \ref{F:remove2} presents four removal processes corresponding to those of Figure \ref{F:remove}. Let us take the leftmost one as an example. We firstly remove a $6$-generalized ribbon $\theta^{'}_1$ colored by $1$, which has two connected components. So $ht(\theta^{'}_1)=2+1=3$. As we can see, $a(\la)=(1,3,2,3,2,1,2,3)$ and $a(\la\setminus\theta^{'}_1)=(3,2,1,3,2,2,1,3)$. So $\I(\theta^{'}_1)=3$. Similarly, we have $ht(\theta^{'}_2)=2$ and $\I(\theta^{'}_2)=2$. Thus, this process contribute the sum term $u^r_2(1-q^{-2})^3(-q^{-2})^0$.
\end{exmp}

\subsection{Specialization to $\mathscr{W}_{m,n}$ case} This subsection aims to explain how our result (Theorem \ref{t:AR}) reduces to the special case for $\mathscr{W}_{m,n}$, which was considered in \cite{AR}. As we mentioned in section \ref{s:special}, the irreducible character $\phi^{\bm{\la}}$ can be obtained from $\chi^{\bla}$ by specializing $\bm{u}=\bm{\zeta}=(1,\zeta,\zeta^2,\cdots,\zeta^{m-1})$ and $q=1$, where $\zeta$ is the primitive $m$-th root of unity. In this case, $\eta^{\la}_{\btau;m}=0$ unless each partition $\tau^{(i)}$ ($1\leq i\leq l(\mu^{(m)})$) has only one row, i.e., $\tau^{(i)}=(\mu^{(m)}_i)$. Moreover, only those processes of removing ribbons (not generalized ribbons) from $\la$ can contribute the summation. Therefore, if $\btau\in\mathcal{P}_m(\mu^{(m)})$, then $\eta^{\la}_{\btau;m}\Big|_{\substack{
\bm{u}=\bm{\zeta}\\ q=1}}$ equals the sum of values obtained by all possible applications of the following algorithm:\\
    {\em Initialization}: $\varepsilon:=1$.
    \begin{enumerate}
        \item If $t=0$, end the program and output $\varepsilon$.
\item Remove a $m\mu^{(m)}_t$-ribbon $\theta$ from $\la$. If we can not find such a ribbon, set $\varepsilon=0$ and end the program.
     \item Multiply $\varepsilon$ by $(-1)^{ht(\theta)-\I(\theta)}$. 
     \item Redefine $\btau:=\big((\mu^{(m)}_1),(\mu^{(m)}_2),\cdots,(\mu^{(m)}_{t-1})\big)$ and $t:=t-1$.
        \item Return to step (1). 
      \end{enumerate}
        
        
        
       Let $\varnothing=\la^{(0)}\subset \la^{(1)}\subset\cdots\subset\la^{(r)}=\la$ be a chain such that $\la^{(i+1)}/\la^{(i)}$ is a ribbon. Then it follows from equation \eqref{e:iI} that $(-1)^{\sum_{i=0}^{r-1}\I(\la^{(i+1)}/\la^{(i)})}=(-1)^{\sum_{i=0}^{r-1}\big({\rm inv}_m(\la^{(i+1)})-{\rm inv}_m(\la^{(i)})\big)}=(-1)^{{\rm inv}_m(\la)-{\rm inv}_m(\varnothing)}$. This, together with the above algorithm, implies that 
       \begin{align}\label{e:special-eta}
         \eta^{\la}_{\btau;m}\Big|_{\substack{
\bm{u}=\bm{\zeta}\\ q=1}}=(-1)^{{\rm inv}_m(\la)-{\rm inv}_m(\varnothing)} \gamma^{\la}_{m\mu^{(m)}}.
       \end{align}
Here $\gamma^{\la}$ is the irreducible character of the symmetric group indexed by the partition $\la$ with $\bla=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ as its $m$-quotient, $m\mu^{(m)}=(m\mu^{(m)}_1, m\mu^{(m)}_2,\cdots)$ and $\btau\in\mathcal{P}_m(\mu^{(m)})$.

Summarizing above, we get the special case of Theorem \ref{t:AR} as below, which firstly appears in \cite[Theorem 3.1]{AR}.
\begin{cor}
    Let $\la\vdash mn, \mu\vdash n$. Suppose the $m$-quotient of $\la$ is $(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$. Then we have
    \begin{align}\label{e:special-AR}
    \phi^{(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})}_{(\varnothing,\cdots,\varnothing,\mu)}=(-1)^{{\rm inv}_m(\la)-{\rm inv}_m(\varnothing)}\gamma^{\la}_{m\mu},
    \end{align}
    where $\phi^{(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})}$ (resp. $\gamma^{\la}$) is the irreducible character of the complex reflection group (resp. the symmetric group) indexed by $(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ (resp. $\la$).
\end{cor}
\begin{proof}
    Taking specialization $\bm{u}=\bm{\zeta}$, $q=1$ and $\bmu=(\varnothing,\cdots,\varnothing,\mu)$ on both sides of \eqref{e:AR} gives that
    \begin{align}
    \phi^{(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})}_{(\varnothing,\cdots,\varnothing,\mu)}=\eta^{\la}_{((\mu^{(m)}_1),(\mu^{(m)}_2),\cdots,);m}\Big|_{\substack{
\bm{u}=\bm{\zeta}\\ q=1}},
    \end{align}
    which, together with \eqref{e:special-eta}, yields \eqref{e:special-AR}. As desired. 
\end{proof}

\begin{rem}
It would be interesting to find a representation-theoretic interpretation of
\(
\sum_{\btau\in \mathcal{P}_m(\mu^{(m)})}\eta^{\la}_{\btau;m}
\)
(up to an explicit normalization factor, e.g. involving $q^{n-l(\mu^{(m)})}$ and possibly a power of $-q^{-2}$),
for $\la$ with empty $m$-core and $m$-quotient
$(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$.
More precisely, one may ask whether this quantity arises as the value of a natural character (or virtual character) associated with a suitable algebra related to $\mathscr{H}_{m,n}(q,\bm{u})$, for example a subalgebra, a corner algebra, or a quotient/subquotient, evaluated at an element corresponding to $g((\varnothing,\cdots,\varnothing,\mu^{(m)}))$.
In the $\mathscr{W}_{m,n}$ case, this interpretation is given by the symmetric group $\mathfrak{S}_n$.
\end{rem}
