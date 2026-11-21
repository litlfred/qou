---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS"
section_id: sec-002-2-simplicial-sections
section_title: "Simplicial Sections"
section_number: 2
pages: 8-10
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.926
doc_brief: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS — We present an averaging process for sections of a torsor under a unipotent group."
---
\label{sec2}

In this section we show how the averaging process is used to 
obtain simplicial sections of certain bundles. 

Suppose $H$ and $G$ are affine group schemes over $\K$, and $H$ 
acts on $G$ by automorphisms. Namely there is a morphism of 
schemes $H \times G \to G$ which  for every $\K$-scheme $Y$ 
induces a group homomorphism
$H(Y) \to \opn{Aut}_{\cat{Groups}}(G(Y))$.
Then $H \times G$ has a structure of a group scheme, and we denote 
this group by $H \ltimes G$; it is a geometric semi-direct 
product. 

Recall that an affine group scheme $G$ is called
{\em pro-unipotent} if it is isomorphic to an inverse limit
$\lim_{\leftarrow i} G_i$ of an inverse system
$\{ G_i \}_{i \geq 0}$ of (finite type affine) unipotent groups. 
One may assume that each of the morphisms
$G \to G_{i} \to G_{i-1}$ is surjective. 
Thus $G_i \cong G / N_i$ where $N_i$ is a 
normal closed subgroup of $G$.

We will be concerned with the following geometric situation.

\begin{sce} \label{sce2.1}
Let $H \ltimes G$ be an affine group scheme over $\K$.
Assume $G$ is pro-unipotent, and moreover there exists a 
sequence $\{ N_i \}_{i \geq 0}$ of $H$-invariant 
closed normal subgroups of $G$ such that 
$G \cong \lim_{\leftarrow i} G / N_i$ and each 
$G / N_i$ is unipotent. Let $\pi : Z \to X$ be an 
$H \ltimes G$ -torsor over $X$ 
which is locally trivial for the Zariski 
topology of $X$. Define $\bar{Z} := Z / H$ and let 
$\bar{\pi} : \bar{Z} \to X$ be the projection.
\end{sce}

\begin{thm} \label{thm5.2}
Assume Scenario \tup{\ref{sce2.1}}.
Suppose $U \subset X$ is an open set 
and \linebreak
$\sigma_0, \ldots, \sigma_q : U \to \bar{Z}$ are sections of 
$\bar{\pi}$. Then there exists a morphism 
\[ \sigma : \bsym{\Delta}^q_{\K} \times U \to \bar{Z} \]
such that the diagram
\[ \begin{CD}
\bsym{\Delta}^q_{\K} \times U @>{\sigma}>>
\bar{Z} \\
@V{\mrm{p}_2}VV @V{\bar{\pi}}VV \\
U @>{}>> X 
\end{CD} \]
is commutative. The morphism $\sigma$ depends functorially 
on $U$ and simplicially on the sequence 
$(\sigma_0, \ldots, \sigma_q)$.
If $q = 0$ then $\sigma = \sigma_0$.
\end{thm}

\begin{proof}
We might as well assume that $U = X$. Consider the quotient 
$Z / G$. Since $G$ is normal in $H \ltimes G$ it follows that
$Z / G$ is a torsor under $H \times X$. Let's write 
$\pi_H : Z \to \bar{Z} = Z / H$ and 
$\pi_G : Z \to Z / G$ for the projections. 

Pick an open set $V \subset X$ which trivializes $\pi : Z \to X$. 
Let's write $Z|_V := \pi^{-1}(V)$. 
Because $\pi_H|_V : Z|_V \to \bar{Z}|_V$ is a trivial torsor under
$H \times \bar{Z}|_V$, we can lift the sections 
$\sigma_0, \ldots, \sigma_q$ to sections
$\til{\sigma}_0, \ldots, \til{\sigma}_q : V \to Z$
such that $\pi_H \circ \til{\sigma}_j  = \sigma_j$.
Furthermore, since $\pi_G : Z \to Z / G$ is $H$-equivariant
and $Z / G$ is a torsor under $H \times X$, it follows that we can 
choose $\til{\sigma}_0, \ldots, \til{\sigma}_q$ such that 
$\pi_G \circ \til{\sigma}_j = \tau$ for some 
section $\tau : V \to Z / G$.

Let $F \subset Z|_V$ be the fiber over $\tau$, i.e.\
$F := V \times_{Z / G} Z$ via the morphisms 
$\pi_G : Z \to Z / G$ and $\tau : V \to Z / G$. Then $F$ is a 
torsor under $G \times V$, and
$\til{\sigma}_0, \ldots, \til{\sigma}_q \in 
\opn{Hom}_X(V, F)$.
See diagram below. 
\[ \UseTips  \xymatrix @C=5ex @R=5ex {
& Z 
\ar[dl]_{\pi_H}
\ar[dd]_{\pi}
\ar[dr]^{\pi_G}
& & F 
\ar[ll]_{\supset} \\
\bar{Z} = Z / H 
\ar[dr]^{\bar{\pi}}
& & Z / G
\ar[dl] \\
& X \\
& & & V
\ar[ull]_{\supset}
\ar@{-->}[uul]^{\tau}
\ar@{-->}[uuu]^{\til{\sigma}_i}

\ar@/^5.5ex/[llluu]^{\sigma_i}
} \]

For any $i$ define $F_i := F / N_i$, which is a torsor 
under $(G / N_i) \times V$. Let $\alpha_i : F \to F_i$ be the 
projection, so 
$\alpha_i \circ \til{\sigma}_j \in \opn{Hom}_{X}(V, F_i)$.
By Theorem \ref{thm5.1} we get an average
\begin{equation} \label{eqn2.6}
\rho_i := \opn{wav}_{G / N_i}(\alpha_i \circ \til{\sigma}_0, 
\ldots, \alpha_i \circ \til{\sigma}_q) : 
\bsym{\Delta}^q_{\K} \times V \to F_i .
\end{equation}
The functoriality of $\opn{wav}$ says that the $\rho_i$ form an 
inverse system, and we let
\begin{equation} \label{eqn2.7}
\rho := \lim_{\leftarrow i} \rho_i : 
\bsym{\Delta}^q_{\K} \times V \to F 
\end{equation}
and
\begin{equation} \label{eqn5.5}
\sigma := \pi_H \circ \rho : 
\bsym{\Delta}^q_{\K} \times V \to \bar{Z} . 
\end{equation}

We claim that the morphism $\sigma$ does not depend 
on the choice of the section $\tau : V \to Z / G$. 
Suppose $\tau' : V \to Z / G$ is another such section.
Let $F'$ be the fiber over $\tau'$, and let
$\rho' : \bsym{\Delta}^q_{\K} \times V \to F'$
be the corresponding morphism as in (\ref{eqn2.7}). Now
$\tau' = h \cdot \tau$ for some morphism $h : V \to H$. 
Then $F' = h \cdot F$, and $h : F \to F'$ is a $G \times V$
-equivariant morphism of torsors, 
with respect to the group-scheme automorphism
$\opn{Ad}(h) : G \times V \to G \times V$. 
The new lift of $\sigma_j$ is 
$\til{\sigma}'_j := h \cdot \til{\sigma}_j : V \to F'$.
Define $F_i' := F' / N_i$,
and let $\rho'_i : \bsym{\Delta}^q_{\K} \times V \to F'_i$
be the morphism as in (\ref{eqn2.6}). 
Since $N_i \times V = \opn{Ad}(h)(N_i \times V)$,
we get a group-scheme automorphism
$\opn{Ad}(h) : (G/N_i) \times V \to (G/N_i) \times V$,
and a $(G/N_i) \times V$ -equivariant morphism of 
torsors $h : F_i \to h \cdot F'_i$. 
By functoriality of $\opn{wav}$ (property 3 in Theorem \ref{thm5.1})
it follows that $\rho'_i = h \cdot \rho_i$. Therefore 
$\rho' = h \cdot \rho$, and
$\pi_{H} \circ \rho' = \pi_{H} \circ \rho = \sigma$. 

Property 2 in Theorem \ref{thm5.1}
implies that $\sigma$ depends 
simplicially on $(\sigma_0, \ldots, \sigma_q)$.

Finally take an open covering $X = \bigcup V_j$ such that each 
$V_j$ trivializes $\pi : Z \to X$, and let
$\sigma_j : \bsym{\Delta}^q_{\K} \times V_j \to \bar{Z}|_{V_j}$ 
be the morphism constructed in 
(\ref{eqn5.5}). Since no choices were made we have
$\sigma_j|_{V_j \cap V_k} = \sigma_k|_{V_j \cap V_k}$
for any two indices. Therefore these sections can be glued to a 
morphism 
$\sigma : \bsym{\Delta}^q_{\K} \times X \to \bar{Z}$. 
The functorial and simplicial 
properties of $\sigma$ are clear from its construction.
\end{proof}

Let $X$ be a $\K$-scheme, and let
$X = \bigcup_{i = 0}^m U_{(i)}$ be an open covering, with 
inclusions $g_{(i)} : U_{(i)} \to X$. We denote this covering by 
$\bsym{U}$. For any multi-index
$\bsym{i} = (i_0, \ldots, i_q) \in \bsym{\Delta}^m_q$
we write $U_{\bsym{i}} := \bigcap_{j = 0}^q U_{(i_j)}$,
and we define the scheme
$U_{q} := \coprod_{\bsym{i} \in \bsym{\Delta}^m_q}
U_{\bsym{i}}.$
Given $\alpha \in \bsym{\Delta}_p^q$ and 
$\bsym{i} \in \bsym{\Delta}^m_q$ there is an inclusion of open 
sets
$\alpha_* : U_{\bsym{i}} \to U_{\alpha_*(\bsym{i})}$. 
These patch to a morphism of schemes
$\alpha_* : U_q \to U_p$,
making $\{ U_q \}_{q \in \mbb{N}}$ into a simplicial 
scheme. The inclusions $g_{(i)} : U_{(i)} \to X$ induce inclusions
$g_{\bsym{i}} : U_{\bsym{i}} \to X$
and morphisms 
$g_q : U_q \to X$; and one has the relations
$g_p \circ \alpha_* = g_q$
for any $\alpha \in \bsym{\Delta}_p^q$.

\begin{dfn} \label{dfn3.2}
Let $\pi : Z \to X$ be a morphism of $\K$-schemes.
A {\em simplicial section of 
$\pi$} based on the covering $\bsym{U}$ is a sequence of morphisms
\[ \bsym{\sigma} = \{ \sigma_q : 
\bsym{\Delta}^q_{\K} \times U_q \to Z \}_{q \in \mbb{N}}  \]
satisfying the following conditions.
\begin{enumerate}
\rmitem{i} For any $q$ the diagram
\[ \begin{CD}
\bsym{\Delta}^q_{\K} \times U_q @>{\sigma_q}>>
Z \\
@V{\mrm{p}_2}VV @V{\pi}VV \\
U_q @>{g_q}>> X 
\end{CD} \]
is commutative.

\rmitem{ii} For any $\alpha \in \bsym{\Delta}_p^q$
the diagram
\[ \UseTips \xymatrix @=4.5ex {
& \bsym{\Delta}^{p}_{\K} \times U_p
\ar[dr]^{\sigma_{p}} 
\\
\bsym{\Delta}^{p}_{\K} \times U_q
\ar[ur]^{\bsym{1} \times \alpha^*} 
\ar[dr]_{\alpha_* \times \bsym{1}} 
& & Z \\
& \bsym{\Delta}^{q}_{\K} \times U_q
\ar[ur]_{\sigma_{q}} 
} \]
is commutative.
\end{enumerate}
\end{dfn}

\begin{cor} \label{cor2.1}
Assume Scenario \tup{\ref{sce2.1}}.
Let $\bsym{U} = \{ U_{(i)} \}_{i=0}^m$ be an open covering
of $X$. Suppose that for any $i \in \{ 0, \ldots, m \}$ we are 
given some section 
$\sigma_{(i)} : U_{(i)} \to \bar{Z}$ of 
$\bar{\pi}$. Then there exists a simplicial section
\[ \bsym{\sigma} = \{ \sigma_q : 
\bsym{\Delta}^q_{\K} \times U_q \to \bar{Z} \}_{q \in \mbb{N}} \]
based on $\bsym{U}$, such that 
$\sigma_0|_{U_{(i)}} = \sigma_{(i)}$
for all $i \in \{ 0, \ldots, m \}$. 
\end{cor}

\begin{proof}
For any multi-index
$\bsym{i} = (i_0, \ldots, i_q)$ we have sections
$\sigma_{(i_0)}, \ldots, \sigma_{(i_q)} : U_{\bsym{i}} \to 
\bar{Z}$. 
Let
$\sigma_{\bsym{i}} : \bsym{\Delta}^q_{\K} \times U_{\bsym{i}} \to  
\bar{Z}$
be the morphism provided by Theorem \ref{thm5.2}. For fixed $q$ 
these patch to a morphism
$\sigma_q : \bsym{\Delta}^q_{\K} \times U_q \to \bar{Z}$.
The functorial and simplicial properties in Theorem \ref{thm5.2} 
imply that this is a simplicial section.
\end{proof}

This result (with $H$ trivial) is illustrated in Figure \ref{fig1}.

\begin{figure}
\includegraphics{fig1.eps}













































































































































\caption{Simplicial sections, $q = 1$. 
We start with sections over two open sets $U_{(0)}$ and $U_{(1)}$ 
in the left diagram; and we pass to a simplicial 
section $\sigma_{(0, 1)}$ on the right. As can be seen, 
$\sigma_{(0, 1)}$ interpolates between $\sigma_{(0)}$ and 
$\sigma_{(1)}$.}
\label{fig1}
\end{figure}
