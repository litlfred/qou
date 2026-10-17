---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-008-53-computation-of-the-gauss-sums
section_title: "Computation of the Gauss sums"
section_number: 5.3
pages: 39-44
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.947
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{gss}
If $\2C$ is a braided spherical tensor category a theorem of Deligne, cf.\ \cite[Proposition
2.11]{y}, implies that $\2Z_1(\2C)$ is a ribbon category (or balanced). Namely, 
\[
\theta_X=\quad\quad
\begin{tangle}
\object{\ol{\ve}(\ol{X})}\Step\object{X}\\
\hh\hcoev\step\id\\
\step[-.8]\mobj{\ol{X}}\step[.8]\id\step\hxx\\
\hh\hev\step\id\\
\object{\ve(\ol{X})}\Step\object{X}
\end{tangle}
\quad\quad \mbox{for } X\in\2C
\]
defines a natural automorphism $\{ \theta_X, X\in\obj\,\2C \}$ of the identity functor
which satisfies 
\[ \theta_{XY}=\theta_X\otimes\theta_Y\mcirc c(Y,X)\mcirc c(X,Y) \quad
   \forall X,Y, \]
\[ \theta_{\ol{X}}=\ol{\theta_X}, \quad\forall X. \]
(A similar results hold for $*$-categories, cf.\ \cite{lro}.) For the simple objects we
have $\theta_X=\omega_X\id_X$ with $\omega_X\in\7F^*$. 

The quantum double $\2Z_1(\2C)$ is braided and by the arguments in Section \ref{sec-semisim}
we know that it has a spherical structure which is induced by the one on $\2C$. We will
show that the numbers $\omega_{(X,e_X)}$ can be computed in terms of the tube algebra and
will compute the Gauss sum 
\[ \Delta_\pm(\2Z_1(\2C))= \sum_{(X,e_X)} \omega^{\pm 1}_{(X,e_X)} d(X,e_X)^2, \]
which plays an important role in the construction of topological invariants.

Following \cite{iz2} we consider the element $t\in\Xi_L$ defined by
\begin{equation}t[i,j,k]= \frac{\lambda}{d_i} \delta_{ik}\delta_{ij} \id_{X_i^2}. 
\label{deft}\end{equation}
It will turn out that $t$ is in the center of $\Xi_L$.

\blemma For simple $(X,e_x)\in\2Z_1(\2C)$ we have
\[ tz_{(X,e_X)} = \omega^{-1}_{(X,e_X)}z_{(X,e_X)}. \]
\elemma
\prf From (\ref{tube2}), (\ref{isotyp}) and (\ref{deft}) we obtain
\[ (tz_{(X,e_X)})[i,j,k] = 
\delta_{ik} \frac{\lambda}{d_i}\frac{d(X)}{\lambda d_i}\sum_{m\in \Gamma}
   \sum_{\alpha=1}^{N_{mi}^j} \sum_{\beta=1}^{N^X_i} \frac{d_md_i}{d_j\lambda}
\begin{tangle}
\step[1.5]\hstep\object{X_j}\step[1.5]\object{X_i}\\
\hh\mobj{{t'}_{mi}^{j\alpha}}\step[1.5]\hcd\step\id\\
\hh\hstep\mobj{X_m}\step\id\step\id\obj{X_i}\step\id\\
\step[1.5]\id\step\O {{p'}^\beta_i}\step\id \\
\step\obj{X}\hstep\hxx\step\id \\
\step[1.5]\O {p^\beta_i}\step\id\step\id \\
\hh\step[1.5]\id\step\id\obj{X_m}\step\id\\
\hh\step[1.5]\id\step\hcu\obj{t_{mi}^{j\alpha}}\\
\step[1.5]\object{X_i}\step[1.5]\object{X_j}
\end{tangle}
\]
\[ = \delta_{ik} \frac{d(X)}{\lambda d_i}\sum_{m\in \Gamma} \sum_{\alpha=1}^{N_{mi}^j}
  \sum_{\beta=1}^{N^X_i} 
\begin{tangle}
\hstep\object{X_j}\step[1.5]\object{\ol{\ve}(\ol{X_i})}\step[2.5]\object{X_i}\\
\hh\hstep\id\step\hcoev\Step\id\\
\hh\step[-1]\mobj{s_{j\ol{\imath}}^{m\alpha}}\step[1.5]\hcu\step\id\Step\id\\
\step[0.5]\dh\step\O {{p'}^\beta_i}\Step\id \\
\step\obj{X}\hstep\hxx\Step\id \\
\step[1.5]\O {p^\beta_i}\step\hd\step[-0.5]\obj{m}\step[1.5]\id \\
\hh\step[1.5]\id\step\hcd\step\id\\
\hh\step[1.5]\id\step\id\step\hev\mobj{\ve(\ol{X_i})}\\
\step[1.5]\object{X_i}\step\object{X_j}
\end{tangle}
\  =\delta_{ik} \frac{d(X)}{\lambda d_i}\sum_{\beta=1}^{N^X_i} 
\begin{tangle}
\hstep\object{X_j}\step[1.5]\object{\ol{\ve}(\ol{X_i})}\step[1.5]\object{X_i}\\
\hh\hstep\id\step\hcoev\step\id\\
\step[0.5]\id\step\id\step\O {{p'}^\beta_i}\step\id \\
\step[0.5]\id\step\hxx\step\id\\
\obj{X}\hstep\hxx\step\hev\step[-.5]\mobj{\ve(\ol{X_i})}\\
\hstep\O {p^\beta_i}\step\id\\
\hh\hstep\id\step\id\\
\hstep\object{X_i}\step\object{X_j}
\end{tangle}
\]
Now the claim is a consequence of the following computation
\[ 
\begin{tangle}
\step[2]\object{X_i}\\
\hh\hcoev\step\id\\
\id\step\O {{p'}^\beta_i}\step\id \\
\hxx\step\id\\
\hh\id\step\hev\\
\object{X}
\end{tangle}
\ \ = \ \
\begin{tangle}
\step[2]\object{X_i}\\
\hh\hcoev\step\id\\
\O {p^\beta_i}\step\id\step\id \\
\hxx\step\id\\
\hh\id\step\hev\\
\object{X}
\end{tangle}
\ \ = \ \
\begin{tangle}
\step[2]\object{X_i}\\
\hh\hcoev\step\id\\
\hxx\step\id\\
\id\step\O {p^\beta_i}\step\id \\
\hh\id\step\hev\\
\object{X}
\end{tangle}
\ \ = \ \
\begin{tangle}
\step[2]\object{X_i}\\
\Step\O {{p'}^\beta_i}\\
\hh\hcoev\step\id\\
\hxx\step\id\\
\hh\id\step\hev\\
\object{X}
\end{tangle}
\ \ = \ \
\begin{tangle}
\Step\object{X_i}\\
\Step\O {{p'}^\beta_i}\\
\hh\hcoev\step\id\\
\id\step\hx\\
\hh\hev\step\id\\
\Step\object{X}
\end{tangle}
\ = \omega^{-1}_{(X,e_X)}\,{p'}^\beta_i,
\]
which is justified by the same arguments as in the proof of Lemma \ref{slemma}. Here we
used standard properties of the spherical structure in the first and third equalities and 
naturality of the half braiding $e_X(\cdot)$ w.r.t.\ the second argument in the second
equality. The rest follows since $(X,e_X)$ is simple. \qed

\bprop We have
\[ \Delta_\pm(\2Z_1(\2C)) = \dim\2C. \]
\eprop
\prf In view of $\sum z_{(X,e_X)}=\11_{\Xi_L}$ the lemma implies
\[ t=\sum_{(X,e_X)} \omega_{(X,e_X)}^{-1} z_{(X,e_X)}, \]
which proves that $t$ is central in $\Xi_L$.
To this equation we apply the linear form $\phi\in\Xi_{L}^*$
\[  \phi(x)= \lambda\sum_{i\in \Gamma} d_i \, tr_{X_i}(x[i,0,i]). \]
One one hand by (\ref{deft}) we clearly have $\phi(t)=\lambda^2$. On the other hand with
(\ref{isotyp}) we compute
\[ \phi(z_{(X,e_X)})= d(X) \sum_{i\in \Gamma} tr_{X_i}\left( \sum_{\alpha=1}^{N^X_i} 
  {p'}^\alpha_i \circ p^\alpha_i \right) =d(X)\sum_{i\in \Gamma} d_i N^X_i= d(X)^2. \] 
Putting everything together we obtain $\Delta_-(\2Z_1(\2C))=\lambda^2=\dim\2C$. The equality
for $\Delta_+$ follows from $\dim\2Z_1(\2C)=(\dim\2C)^2$ and the fact 
$\Delta_+(\2M)\Delta_-(\2M)=\dim\2M$, which holds for every modular category $\2M$
\cite{t,khr1}. 
\qed\\

This completes the proof of Theorem \ref{main1}.

\brem 1. A modular category satisfying $\Delta_+(\2C)=\Delta_-(\2C)$ gives rise to an
anomaly-free surgery TQFT, cf.\ \cite{t}. Thus for quantum doubles the construction of the 
associated TQFTs simplifies considerably. 

2. The representation category of a rational conformal quantum field theory is a 
braided $*$-category and the central charge $c\in\7R$ of the CQFT is related, cf.\ e.g.\ 
\cite{khr1}, to the Gauss sums $\Delta_-(\2C)$ by 
\[ \frac{\Delta_-(\2C)}{|\Delta_-(\2C)|}= \exp \left(\frac{2\pi ic_\2C}{8} \right). \]
Since the Gauss sum of a quantum double is given by $\Delta_-(\2Z_1(\2C))=\dim\2C$, thus
positive, we conclude that the `central charge' of a double satisfies
\[ c_{\2Z_1(\2C)}\equiv 0 \ (\mbox{mod}\ 8). \]
\erem







\section{The quantum double of a $*$-category}
Consider the quantum double $\2Z_1(\2C)$ of a $*$-category $\2C$. If 
$s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))\subset\Hom_\2C(X,Y)$ then clearly
$s^*\in\Hom_\2C(Y,X)$. It does, not, however, follow that
$s^*\in\Hom_{\2Z_1(\2C)}((Y,e_Y),(X,e_X))$. But there is a suitable full subcategory of
$\2Z_1(\2C)$ which is a $*$-category. 

\bdefin Let $\2C$ be a tensor $*$-category. Then the unitary quantum double 
$\2Z_1^*(\2C)$ is defined as $\2Z_1(\2C)$ except that the half braidings $e_X(Y)$ are 
required to be unitary, not just invertible. \edefin
\blemma Let $\2C$ be a tensor $*$-category. Then $\2Z_1^*(\2C)$ is a $*$-category. \elemma
\prf For $s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))\subset\Hom_\2C(X,Y)$ we have
\[ \id_Z\otimes s\mcirc e_X(Z)= e_Y(Z)\mcirc s\otimes\id_Z\quad\forall Z. \]
Starring this equation and using $e_X(Z)^*=e_X(Z)^{-1}$ we obtain
\[ \id_Z\otimes s^*\mcirc e_Y(Z)= e_X(Z)\mcirc s^*\otimes\id_Z\quad\forall Z, \]
thus $s^*\in\Hom_{\2Z_1(\2C)}((Y,e_Y),(X,e_X))$. \qed\\

In the applications of the quantum double to operator algebras, like to the asymptotic
subfactor \cite{iz2} or quantum field theory \cite{klm}, one is mainly interested in the
unitary quantum double. In order for the results of Theorem \ref{main1} to remain valid for
$\2Z_1^*(\2C)\subset \2Z_1(\2C)$ one must show $\2Z_1^*(\2C)$ that is equivalent to $\2Z_1(\2C)$
as a tensor category. Given an isomorphism $s: X\rarr Y$ in a $W^*$-category we can use
polar decomposition \cite{glr} to obtain a unitary morphism $\tilde{s}: X\rarr Y$. But
we cannot construct a unitary half-braiding in this way since it is not clear that the
unitaries $e_X(Z), Z\in\2C$ can be chosen such that naturality (\ref{hb-i}) and the braid
relation (\ref{hb-ii}) hold. Therefore a global approach is needed, which we develop using
our machinery from Section \ref{sec-morita}. 

Let $\2C$ be a $*$-category with conjugates, simple unit and finitely many simple objects.
All dimensions $d(X)$ are positive, and we choose the square roots of the latter and of
$\dim\2C$ to be positive. Reconsidering the constructions of Section \ref{sec-morita} we
now choose the bases $\{ t_{ij}^{k\alpha}\}$ in $\Hom_\2C(X_k,X_iX_j)$ to be orthonormal,
i.e.\ ${t'}_{ij}^{k\alpha}={t_{ij}^{k\alpha}}^*$, and similarly $v_i'=v_i^*$. Then
$v'=v^*$ and $w'=w^*$, such that the considerations of \cite[Subsection 5.3]{mue09} apply.  
We thus obtain a $*$-bicategory $\2E_*\subset\2E$ which is equivalent to $\2E$. The
considerations in Sections \ref{sec-morita} and \ref{sec-modular} of this paper remain
essentially unchanged except for replacing $\ve(X), \ol{\ve}(X)$ by standard solutions
$r_X, \ol{r}_X$ of the conjugate equations \cite{lro} everywhere.

\blemma \label{orthp}
Let $\2C$ be a $*$-category. Let $(X,e_X)\in\2Z_1(\2C)$ and 
$F(X,e_X)=(\oj(X\boxtimes\11)J,p_X)$. Then the idempotent 
$p_X\in\End_\2E(\oj(X\boxtimes\11)J)$ satisfies $p_X=p_X^{\#}$ iff $e_X(Z)$ is unitary for
all $Z$.
\elemma 
\prf We recall from Proposition \ref{funcf} that $p_X$ is given by
\[ p_X=\lambda^{-1} \sum_i v_i\otimes\id_{X\boxtimes\11} \mcirc
   e_X(X_i)\boxtimes\id_{X^\op_i} \mcirc\id_{X\boxtimes\11} \otimes v'_i.
\]
In view of the definition \cite[Subsection 5.3]{mue09} of the involution $\#$ on 
$\End_\2E(\oj (X\boxtimes\11)J)\equiv\Hom_\2A(\oj (X\boxtimes\11)JQ,Q\oj (X\boxtimes\11)J)$ 
we have 
\[ p_X^\#= \lambda^{-1} \sum_i \quad
\begin{tangle}
\object{Q}\step[1.5]\object{X\boxtimes\11}\\
\id\step\id\step\hcoev\mobj{r^*}\\
\hh\id\step\id\step\mfrabox{v_i}\id\\
\hh\id\step\id\step\id\obj{\hat{X}_i}\step\id\\
\hh\id\step\frabox{e^*_i}\step\id\\
\hh\id\step\id\obj{\hat{X}_i}\step\id\step\id\\
\hh\id\step\mfrabox{v_i^*}\id\step\id\\
\mobj{r}\hev\step\id\step\id\\
\step[1.5]\object{X\boxtimes\11}\step[1.5]\object{Q}
\end{tangle}
\]
where $e_i^*\equiv e_X(X_i)^*\boxtimes\id_{X_i^\op}$ and $r=w\circ v: \11\rarr Q^2$.
In view of (\ref{gamma}) it is clear that there are uniquely determined  
$\hat{r}_i: \11\rarr \hat{X}_{\ol{\imath}}\otimes\hat{X}_i,\ i\in \Gamma$ such that
\[ r = \sum_i v_{\ol{\imath}}\otimes v_i\mcirc\hat{r}_i. \]
Using $\id_Q\otimes r^*\mcirc r\otimes\id_Q=\id_Q$ one easily shows
\[ \id_{\hat{X}_i}\otimes\hat{r}^*_i\mcirc\hat{r}_{\ol{\imath}}\otimes\id_{\hat{X}_i} =
  \id_{\hat{X}_i}. \]
(This amounts to the identification $\ol{\hat{r}_i}=\hat{r}_{\ol{\imath}}$ which is
possible since all the self-conjugate $\hat{X}_i, i\in \Gamma$ are orthogonal.) Thus
\[ v_i^*\otimes\id_Q\mcirc r = \id_{\hat{X}_i}\otimes v_{\ol{\imath}}\mcirc
  \hat{r}_{\ol{\imath}}, \quad \quad
   \id_Q\otimes v_i^*\mcirc r = v_{\ol{\imath}}\otimes\id_{\hat{X}_i}\mcirc\hat{r}_i, \]
and we obtain
\[ p_X^\#= \lambda^{-1} \sum_i \quad
\begin{tangle}
\object{Q}\step[1.5]\object{X\boxtimes\11}\\
\id\step\id\step\hcoev\mobj{\hat{r}^*_{\ol{\imath}}}\\
\hh\id\step\id\step\id\step\mfrabox{v^*_{\ol{\imath}}}\\
\hh\id\step\id\step\id\obj{\hat{X}_i}\step\id\\
\hh\id\step\frabox{e^*_i}\step\id\\
\hh\id\step\id\obj{\hat{X}_i}\step\id\step\id\\
\hh\mfrabox{v_{\ol{\imath}}}\id\step\id\step\id\\
\mobj{\hat{r}_i}\hev\step\id\step\id\\
\step[1.5]\object{X\boxtimes\11}\step[1.5]\object{Q}
\end{tangle}
\]
This equals $p_X$ iff
\[ \id_{X_{\ol{\imath}}X}\otimes \ol{r}^*_i \mcirc 
  \id_{X_{\ol{\imath}}}\otimes e_X(X_i)^*\otimes\id_{X_{\ol{\imath}}} \mcirc
  r_i\otimes\id_{XX_{\ol{\imath}}}=e_X(X_{\ol{\imath}}) \quad\forall i\in \Gamma. \]
Considering Lemma \ref{l3}, this is the case iff $e_X(X_i)^*=e_X(X_i)^{-1}$ for all
$i\in \Gamma$. In view of Lemma \ref{halfbr} and the fact that the $x_i^\alpha$ occurring in
its proof are automatically isometries, this is equivalent to unitarity of $e_X(Z)$ for
all $Z$.
\qed


\btheor Let $\2C$ be a tensor $*$-category with simple unit, finitely many simple objects,
conjugates, direct sums and subobjects. Then $\2Z_1^*(\2C)$ is monoidally equivalent to
$\2Z_1(\2C)$, thus modular. \etheor  
\prf Let $(X,e_X)\in\2Z_1(\2C)$ and $(\oj(X\otimes\11)J,p_X)=F(X,e_X)$. Since
$\End_\2E(\oj(X\otimes\11)J)$ is a finite dimensional von Neumann algebra it contains an
orthogonal projection $q_X=q_X^2=q_X^*$ and an invertible element $s$ such that
$sp_Xs^{-1}=q_X$. It is clear that
$(\oj(X\boxtimes\11)J,q_X)\cong(\oj(X\boxtimes\11)J,p_X)$, and
by the lemma there is a unitary half braiding $\tilde{e}_X(\cdot)$ such that 
$F(X,\tilde{e}_X)=(\oj(X\boxtimes\11)J,q_X)$. Thus 
\[
\2Z_1^*(\2C)\ \stackrel{\otimes}{\simeq}\ \2B_*\ \stackrel{\otimes}{\simeq}\ \2B\
  \stackrel{\otimes}{\simeq} \2Z_1(\2C), \]
where 
$\2B_*\equiv\End_{\2E_*}(\6B)$. (The equivalence $\2B_*\cong\2B$ has already been
demonstrated in \cite[Proposition 5.6]{mue09}.)
\qed
