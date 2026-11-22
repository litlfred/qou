---
doc_id: arxiv-2607.03827v1
doc_title: "Affine cellular algebras and asymptotic algebras"
section_id: sec-003-4-the-asymptotic-algebra-of-an-affine-cellular-a
section_title: "The asymptotic algebra of an affine cellular algebra"
section_number: 4
pages: 13-17
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.961
doc_brief: "Affine cellular algebras and asymptotic algebras — The theory of affine cellular algebras A is extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between"
---
In this section, the asymptotic algebra of an affine cellular algebra
and the embedding of an affine cellular algebra into its asymptotic algebra
will be described in detail. Moreover, the asymptotic algebra will be
constructed as endomorphism ring in a double centraliser property.
This proves Theorems A and D. 

Let $A$ be an affine cellular algebra with cell chain 
\begin{equation}\label{notation:cellchain}
  0=J_0 \subset J_1 \subset \cdots \subset J_n=A,\end{equation} with cell data 
$(B_i, \sigma_i, \Delta_i, \psi^{(i)}, \alpha_i)$. 
In particular, 
\begin{equation}\label{notation:celldata}\alpha_i: J_i/J_{i-1} \to \Delta_i\otimes_ {B_i} \Delta_i' = (M_{d_i}(B_i),\psi^{(i)})\end{equation}
is an isomorphism of $A$-bimodules.


The \emph{asymptotic algebra} $\asym$ of an affine cellular $A$ has been
defined in \cite{KXaffine} as the direct product of all matrix algebras
$M_{d_i}(B_i)$ obtained from the cell data of the cell chain. In
\cite[comment before Lemma 5.5 on page 177]{KXaffine}, it has been mentioned
that the definition of the asymptotic algebra given in \cite{KXaffine}
coincides with Lusztig's asymptotic algebra in the case of the extended affine
Hecke algebra of type $A_{n-1}$. Further details will be given in the final
section when discussing examples and methods.








\begin{definition}
  
  The asymptotic algebra of $A$ is defined as 
$\asym = M_{d_n}(B_n) \times \cdots \times M_{d_1}(B_1)$. Set $\asym_i = M_{d_i}(B_i)$, for any $i$.
\end{definition}

For each $1\leq k \leq n$ denote the left multiplication of $A$ on $J_k/J_{k-1}$
by 
$\lambda_k: A \to \End( {J_k/J_{k-1}} )$, i.e. 
$$\lambda_k(a)=[x+J_{k-1} \mapsto ax + J_{k-1}],$$ for all $a\in A$ and $x\in J_k$. Note that $\lambda_k$ is right $A$-linear. Consider the ring homomorphism
\begin{equation}
    \lambda: A \to \End( {J_n/J_{n-1}} ) \times \End( {J_{n-1}/J_{n-2}} ) \times \cdots \times \End( {J_1} ), \qquad \lambda = (\lambda_n, \lambda_{n-1}, \cdots, \lambda_1)
\end{equation}

Due to \cite[Lemmas 4.2, 3.2]{CKLS}, the map $\lambda$ is injective if and only if no determinant $\det(\psi^{(k)})$ is a zero-divisor in $B_k$. By \cite[Theorem 3.3]{CKLS}, the ring $\End( {J_k/J_{k-1}})$ is isomorphic to $M_{d_k}(B_k)$ if $\det(\psi^{(k)})$ is not a zero-divisor in $B_k$ (or if  $J_k/J_{k-1}$ is idempotent).  We will briefly recall the steps of the proof of \cite[Theorem 3.3]{CKLS}. Let $J$ be an affine cell ideal with cell datum $(B,\sigma, \Delta, \psi,\alpha)$ with $n=\rank_B(\Delta)$. Assume that $J$ is idempotent or $\det(\psi)$ is not a zero-divisor in $B$.  Then in a first step one shows that the right $A$-linear endomorphisms of $J$ coincide with the right $J$-linear endomorphisms  of $J$, i.e. $\End(J_A)=\End(J_J)$. Moreover, the isomorphism $\alpha: J \to (M_n(B),\psi)=:\widetilde{M_n(B)}$ induces an isomorphism between $\End(J_J)$ and $\End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}})$ given by $f\mapsto \alpha f \alpha^{-1}$.  Finally one checks that the ring homomorphism $l:M_n(B)\to \End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}})$ given by left multiplication, $l(X)=[Y\mapsto XY]$, for any matrices $X,Y \in M_n(B)$ is invertible, with inverse given by $l^{-1}(g) = g(\idm)$, for any $g\in \End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}})$. Hence the isomorphism between $\End(J_A)$ and $M_n(B)$ is given by $f\mapsto \alpha(f(\alpha^{-1}(\idm)))$.

We summarise the situation as follows:
The isomorphism $$\alpha: J \to (M_n(B),\psi)= \widetilde{M_n(B)}$$
induces an isomorphism $\End(J_A) \cong  M_n(B), 
f  \mapsto  \alpha(f(\alpha^{-1}(\idm)))$,                       
                        which is the composition \medskip

\begin{center}
$\begin{array}{ccccc}
  \End(J_A) = \End(J_J) & \stackrel{\alpha}{\rightarrow} &
\End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}}) &
\stackrel{l^{-1}}{\rightarrow} & M_n(B) \\
f & \mapsto & \alpha f \alpha^{-1} & & \\
& & g & \mapsto & g(\idm)
 \end{array}$
 \end{center}

\medskip

\noindent For $1\leq k \leq n$ let $e_k = \alpha_k^{-1}(\mathbf{I}_{d_k})\in J_k/J_{k-1}$. Combining the left multiplication ${\lambda_k:A\to \End(J_k/J_{k-1})}$ with the isomorphism between $\End(J_k/J_{k-1})$ and $M_{d_k}(B_k)$ yields a ring homomorphism
$\Theta_k: A \to M_{d_k}(B_k)$ given by 
\begin{equation}\Theta_k(a)=\alpha_k(ae_k),\end{equation}
for all $a\in A$. Since the multiplication on $J_k/J_{k-1}$ is encoded in $\psi^{(k)}$, by (\ref{eq2}) any element $a\in J'_k$ satisfies:
\begin{equation}\label{eq:image-theta-k}\Theta_k(a)=\alpha_k(ae_k) = \alpha_k(\overline{a})\psi^{(k)},\end{equation}
where $\overline{a} = a + J_{k-1}$.

\begin{theorem}[Theorem \ref{TheoremA}] \label{TheoremAtext}
    Let $A$ be an affine cellular algebra such that no determinant $\det(\psi^{(k)})$ is a zero-divisor in $B_k$. Then $\Theta:A\to \asym$ given by $\Theta = (\Theta_n, \cdots, \Theta_1)$, is an embedding of $A$ into its asymptotic algebra. 
    More concretely,
\begin{equation}\label{notation:embedding}
    \Theta(a) = (\alpha_n(ae_n), \ldots, \alpha_1(ae_1)), \qquad a\in A.
\end{equation}
Let $1\leq k \leq n$, then for any $a\in J'_k$:
\begin{equation}
    \Theta(a) = (\alpha_n(ae_n), \cdots, \alpha_{k}(ae_{k}), \alpha_k(\overline{a})\psi^{(k)}, 0, \ldots, 0), 
\end{equation}
since $\Theta_l(a)=0$, for all $l<k$.
\end{theorem}

\begin{remark} 
  The same proof shows that there is the following embedding
  of $A$ into a more economic version of $\asym$: 
  
  Let $m$ be the least non-negative integer such that $J_m/J_{m-1}$ is a
  faithful left $A/J_{m-1}$-module. Then there is an embedding of $A$
  into $M_{d_m}(B_m) \times \cdots \times M_{d_1}(B_1)$.
  
 In particular, when the affine cell ideal $J_1$ is a faithful $A$-module, one
 may choose $m=1$ and get an embedding into the matrix algebra
 $M_{d_1}(B_1)$.

 We choose however not to take this abbreviation, for the following
 reason: By \cite{KXaffine}, simple $A$-modules are classified by
 subsets of the disjoint union of the maximal spectra of the matrix
 components of $\asym$. The abbreviation using $m < n$ would confuse this
 approach and Theorem \ref{TheoremC} could not be formulated any more.
\end{remark}







In the second part of this section we will show that the asymptotic algebra can also be constructed as the double centraliser of the direct sum of cell modules. 

\iffalse
Let $A$ be an affine cellular algebra $A$ with cell chain as above. $0=J_0 \subset J_1 \subset \cdots \subset J_N=A$, such that each affine cell ideal $J_k/J_{k-1}$ has cell datum $(B_k, \sigma_k, \Delta_k, \psi^{(k)}, \alpha_k)$, i.e. $J_k/J_{k-1}\cong \Delta_k \otimes_{B_k}  \Delta_k' \cong \left( M_{d_k}(B_k), \psi^{(k)} \right)$ as $A$-bimodules, for $d_k=\rank_{B_k}(\Delta_k)$ In \cite{CKLS} the authors showed that if no determinant $\det(\psi^{(k)})$ is a zero-divisor, then $A$ embeds into its asymptotic algebra $\asym = M_{n_1}(B_0)\times \cdots \times M_{n_d}(B_d)$, where $d$ is the least integer $i$ such that $J_i/J_{i-1}$ is a faithful left $A/J_{i-1}$-module. 
We will shortly revise a slightly modified version of this embedding.
\fi

Let $J$ be an affine cell ideal of $A$, with cell datum $(B,\sigma,\Delta, \psi,\alpha)$ and $n=\rank_B(\Delta)$. Let ${\alpha:J \to \Delta \otimes_B \Delta'}$ be the given $A$-bimodule isomorphism with $\Delta = V\otimes B$ an $A$-$B$-bimodule, $V$ free of rank $n$ over $k$ and $\Delta' = B\otimes V$ the induced $B$-$A$-bimodule. Then $J\cong \Delta^n$ as left $A$-module and $J \cong (\Delta')^n$ as right $A$-module. Moreover, ${_B\Delta} \cong  {_BB}^n \cong {\Delta'_B}$ as $B$-modules.


By Lemma \ref{lemma12} or \cite[Theorem 3.3]{CKLS},  $\End({_A\Delta}) \cong B$, if $J$ is idempotent or $\det(\psi)$ is not a zero-divisor in $B$. 

Similarly,  the map $\mathbf{l}_b:\Delta' \to \Delta'$ given by $\mathbf{l}_b(x)=bx$, for any $b\in B$ is  right $A$-linear and yields an injective ring homomorphism $\mathbf{l}:B\to \End({\Delta'_A})$. 
In case $J$ is idempotent or $\det(\psi)$ is not a zero-divisor in $B$, it can be shown as in Lemma \ref{lemma12} that the map $\mathbf{l}$ is an isomorphism.
\iffalse
 It remains to show that $\mathbf{l}$ is surjective. This is done in two steps, using that if $\det(\psi)$ is not a zero-divisor, then $\psi^+$, the adjoint of $\psi$, is a central and not a zero-divisor in $\widetilde{M_n(B)}=(M_n(B),\psi)$. Firstly one needs to show that  $\End({\Delta'_A})=\End({\Delta'_{\widetilde{M_n(B)}}})$ holds and secondly one uses \cite[Proposition 2.2]{CKLS}, saying that any element $f\in \End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}})$ is given by left multiplication with $f(I_n)$, where $I_n$ is the identity matrix of $M_n(B)$. Hence if we identify $\Delta'$ with the first row of $M_n(B)$ and consider $f\in \End({\Delta'_A})$, then  $f$ can be extended to $\overline{f}\in \End({\widetilde{M_n(B)}_{\widetilde{M_n(B)}}})$ such that $\overline{f}(E_{ij})=0$, for $i>1$. Since $\overline{f}$ is given by left multiplication with $\overline{f}(I_n)$ and 
$$\overline{f}(I_n) = \sum_{i=1}^n \overline{f}(E_{ii}) = f(E_{11}) = \sum_{j=1}^n b_j E_{1j}\in \Delta',$$ for some $b_j\in B$, we conclude $f(X)=f(E_{11})X = b_1 X = \mathbf{l}_{b_1}(X)$, for all $X\in \Delta'$. Hence $\mathbf{l}:B\to \End(\Delta'_A)$ is surjective.
\fi 
Thus in this case we obtain the following chain of isomorphisms, using $J\cong (\Delta')^n$ as right $A$-modules:
\begin{equation}\label{eqn1}\End(J_A) \cong M_n(\End(\Delta'_A)) \cong  M_n(B) \cong \End(B^n_B) = \End(\Delta_B).\end{equation}

The left multiplication of $A$ on $J$, i.e. $\lambda(a)=:\lambda_a\in \End(J_A) \cong \End(\Delta_B)$ is defined by $\lambda_a(x)=ax$, for all $x\in J$. 
Identifying $J\cong  \Delta \otimes_B \Delta' \cong \Delta^n$, the left $A$-action $\lambda_a$ on $J$ and its restriction, say $\lambda'_a$, on $\Delta$ coincide. 

The map $\Theta:A\to A/J\times \End(J_A)$, with $\Theta(a) = (a+J, \lambda_a)$, for all $a\in A$, is a ring homomorphism. By Lemma \ref{lemma1}, $\Theta$ is injective if and only if $\det(\psi)$ is not a zero-divisor in $B$. Using equation (\ref{eqn1}) we obtain an injective ring homomorphism
$$\Theta:A \to A/J \times \End(\Delta_B),\qquad  a \mapsto (a+J, \lambda'_a),$$
with $\lambda'_a$ the left action of $A$ on $\Delta$. Repeating this process along a cell chain yields an embedding of rings:
$$\Theta:A \to \prod_{i=1}^n \End( (\Delta_i)_{B_i}), \qquad a \mapsto (\lambda'^{(n)}_a, \cdots , \lambda'^{(1)}_a),$$
where $\lambda'^{(i)}_a$ denotes the left action of $a\in A$ on $\Delta_i$.

By Corollary \ref{regular}, $\Hom_A(\Delta_i,\Delta_j)=0$ for $i\neq j$, if for all $i$ the ideal $J_i/J_{i-1}$ is idempotent and $\det(\psi^{(i)})$ is not a zero-divisor in $B_i$. Therefore, the faithful $A$-module $M=\bigoplus_{i=1}^n \Delta_i$ satisfies:
\begin{eqnarray}
\End_A(M)&=&\prod_{i=1}^n \End_A(\Delta_i)\\
 \End(M_{\End_A(M)}) &=& \prod_{i=1}^n \End( {\Delta_i}_{B_i})
\end{eqnarray}
Thus we have proven the following Theorem:

\begin{theorem}\label{TheoremDtext}
  Let $A$ be an affine cellular algebra with cell chain $0=J_0 \subset J_1 \subset \cdots \subset J_n=A$ and cell datum $(B_i,\sigma_i,\Delta_i, \psi^{(i)}, \alpha_i)$ and $n_i=\rank_{B_i}(\Delta_i)$, for all $i$.

If for all $i$, the ideal $J_i/J_{i-1}$ is idempotent and $\det(\psi^{(i)})$ is not a zero-divisor, then the following hold.
\begin{enumerate}
    \item $M=\bigoplus_{i=1}^n \Delta_i$ is a faithful left $A$-module.
    \item $T=\End_A(M)=\prod_{i=1}^n \End_A(\Delta_i)$.
    \item The left $A$-module action of $A$ on $M$ induces an embedding of rings
    $$\lambda: A \to \End(M_T) = \prod_{i=1}^n \End( {\Delta_i}_{B_i}) \cong M_{d_n}(B_n)\times \cdots \times M_{d_1}(B_1) = \asym,$$
    which coincides with the embedding of $A\to \asym$ as shown in \cite{CKLS}.
\end{enumerate} 
\end{theorem}
\begin{proof}
\iffalse
In order to use Lemma \ref{lemma2}, note that for any $0 \leq k \leq N-1$: $X=\Delta_N\oplus \cdots \oplus 
\Delta_{k+1}$ 
is an $A/J_k$-module, i.e. $J_{k}X=0$. Let $Y=\Delta_k$. Since $J_k/J_{k-1}$ is an idempotent ideal and $J_k/J_{k-1}$ 
is 
an affine cell ideal of $A/J_{k-1}$, we have $J_kY=Y$ by Lemma \ref{lemma1}. Also by Lemma \ref{lemma1},   
$\ann_{Y}\left(J_k/J_{k-1}\right)=0$ as $\mathrm{det}(\psi^{(k)})$ is not a zero-divisor in $B_k$.
By Lemma \ref{lemma2} we have that
 $$\mathrm{End}( {_{A/J_{k-1}} X\oplus Y} ) \cong \mathrm{End} ({_{A/J_{k}}X}) \times \mathrm{End} ({_{A/J_{k-1}}Y}) = 
\mathrm{End} ({_{A/J_{k}} \Delta_N \oplus \cdots \oplus \Delta_{k+1}}) \times B_k,$$
since by Lemma \ref{lemma1}, $\mathrm{End}({_{A/J_{k-1}}X}) = \mathrm{End}(_A\Delta_k)\cong B_k$.
Using  Lemma \ref{lemma2} iteratively, we have
\begin{eqnarray*}
\mathrm{End}\left( {_A\left(\Delta_N \oplus \cdots \oplus \Delta_1\right) \oplus \Delta_0} \right) 
&\cong & \mathrm{End}\left( {_{A/J_0} \left(\Delta_N \oplus \cdots \oplus \Delta_2\right) \oplus \Delta_1}\right) 
\times 
 B_0 \\
&\cong & \mathrm{End}\left( {_{A/J_1}\Delta_N \oplus \cdots \oplus \Delta_2}\right) \times B_1  \times B_0 \\
&\vdots&\\
&\cong & \mathrm{End}\left( {_{A/J_{N-1}}\Delta_N}\right) \times B_{N-1} \times \cdots \times B_0 \\
&\cong & B_N \times B_{N-1} \times \cdots  \times B_0 
\end{eqnarray*}
Each endomorphism of $M$ is a sum of endomorphisms of $\Delta_k$, which act componentwise. Hence 
$$\mathrm{End}(M_S) = \mathrm{End}\left({\Delta_N}_{B_N}\right) \times \cdots \times 
\mathrm{End}\left({\Delta_0}_{B_0}\right) \cong  M_{d_N}\left(B_N\right) \times \cdots \times 
M_{d_0}\left(B_0\right),$$
since ${\Delta_k}_{B_k}\cong B_k^{d_k}$ as right $B_k$-modules.
\fi
Note that $M$ is a faithful left $A$-module, because if $aM=0$, then $a\Delta_i=0$, for all $i$. Hence, $a(J_i/J_{i-1})=0$, for all $i$. Thus $a + J_{i-1}\in \ann_{J_{i-1}/J_{i-2}}(J_{i-1}/J_{i-2})$. As $\mathrm{det}(\psi^{(i-1)})$ are not
zero-divisors by assumption,  $a\in J_{i-1}$, for all $i$. Thus $a\in J_{0}=0$. In particular, the left action of $A$ on $M$ yields an embedding of $A$ into $\End(M_T)$, where $T=\End(_AM)$. By the previous argument, $\End(M_T)\cong \prod_{i=1}^n \End({\Delta_i}_{B_i}) \cong \asym$.
\end{proof}
