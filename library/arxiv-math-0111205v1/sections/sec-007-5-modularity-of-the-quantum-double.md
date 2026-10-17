---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-007-5-modularity-of-the-quantum-double
section_title: "Modularity of the Quantum Double"
section_number: 5
pages: 29-39
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.936
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{sec-modular}

\subsection{The `Tube algebra'} \label{ss-tube}
By definition \cite{mue09} of $\2E$, every simple $\6B-\6B$ morphism is contained in
$\oj(X\boxtimes Y^\op)J$ for some simple $X, Y$. In view of Lemma \ref{iz1} every simple
$\6B-\6B$-morphism is  in fact contained in  $\oj (X\boxtimes\11)J$ for some simple
$X\in\2C$ (as well as in $\oj (\11\boxtimes \ol{X}^\op) J$). Defining
\[ \hat{Y}_L = \bigoplus_{i\in \Gamma} X_i\boxtimes \11, \quad\quad
   \hat{Y}_R = \bigoplus_{i\in \Gamma} \11\boxtimes X_i^\op, \]
we conclude that either of $\oj \hat{Y}_LJ,\ \oj \hat{Y}_RJ$ 
contains all simple $\6B-\6B$-morphisms. With
\[ \Xi_L = \End_\2E(\oj \hat{Y}_LJ), \quad\quad  \Xi_R = \End_\2E(\oj \hat{Y}_R J) \]
we thus have a one-to-one correspondence between isomorphism classes of simple 
$\6B-\6B$-morphisms and minimal central idempotents in $\Xi_L$ or, equivalently, in
$\Xi_R$. From now on we will stick to $\Xi_L$. By construction of $\2E$ we have 
$\Xi_L=\Hom_\2A(\hat{Y}_LQ,Q\hat{Y}_L)$ as a vector space. Thus
\bean \Xi_L &\cong& \bigoplus_{i,j,k,l} \, \Hom_\2A(X_iX_j\boxtimes X_j^\op,
   X_kX_l\boxtimes X_k^\op) \\
  &\cong& \bigoplus_{i,j,k,l} \, \Hom_\2C(X_iX_j,X_kX_l) \,\otimes_\7F \,
  \Hom_{\2C^\op}(X_j^\op, X_k^\op)  \\
  &\cong& \bigoplus_{i,j,l} \, \Hom_\2C(X_iX_j,X_jX_l). \eean
We therefore have 
\begin{equation}\End_\2E(\oj \hat{Y}_L J)\equiv\Hom_\2A(\hat{Y}_LQ,Q\hat{Y}_L)\cong
   \bigoplus_{i,j,k} \, \Hom_\2C(X_iX_j,X_jX_k), \label{tube1}\end{equation}
and in complete analogy to the proof of (\ref{mul}) one shows that the multiplication in
$\Xi_L$ is given by
\begin{equation}(v\bullet u)[i,j,k]= (d_j\lambda)^{-1} \sum_{l,m,n\in \Gamma} 
  \sum_{\alpha=1}^{N_{mn}^j} d_md_n \ 
\begin{tangle}
\step[1.5]\hstep\object{X_j}\step[1.5]\object{X_k}\\
\hh\mobj{{t'}_{mn}^{j\alpha}}\step[1.5]\hcd\step\id\\
\hh\step[1.5]\id\mobj{X_m}\step\id\mobj{X_n}\step\id\\
\hh\step[1.5]\id\step\frabox{v[l,n,k]} \\
\hh\step[1.5]\id\step\id\obj{X_l}\step\id\\
\hh\step[1.5]\frabox{u[i,m,l]}\step\id \\
\hh\step[1.5]\id\step\id\obj{X_m}\step\id\obj{X_n}\\
\hh\step[1.5]\id\step\hcu\obj{t_{mn}^{j\alpha}}\\
\step[1.5]\object{X_i}\step[1.5]\object{X_j}
\end{tangle}
\label{tube2}\end{equation}

\brem 1. We observe that up to a different normalization (\ref{tube1}) and (\ref{tube2})
coincide with Ocneanu's definition of the `tube algebra', cf. \cite{ocn3,ek1,iz2}. 
(The $(ij|X|jk)$ of Izumi corresponds to our $u[i,j,k]\cdot\frac{d_j}{\lambda}$.)
Note, however, that we {\it derive} (\ref{tube1}, \ref{tube2}) from an intrinsic
definition of the algebra $\Xi_L=\End_\2E(\oj \hat{Y}_LJ)$, which makes the
correspondence between the minimal central idempotents of $\Xi_L$ and the isomorphism
classes of simple objects in $\2B$ completely obvious. (Compare this to the laborious
proof in \cite{iz2}.) The above considerations therefore completely clarify the r\^{o}le
of the tube algebra. We suspect that Ocneanu arrived at his definition of the tube algebra
by similar considerations.

2. Note that in the definition of $\Xi_L$ we could replace $\hat{Y}_L$ by
\[ \hat{Y}^N_L = \bigoplus_{i\in \Gamma} N_i\,(X_i\boxtimes \11) \] 
with arbitrary $\{N_i\}\in\7N^\Gamma$. The algebras $\End_\2E(\oj \hat{Y}^N_L J)$, of
which the tube algebra happens to be the smallest, all have the same center, thus are
Morita equivalent. We emphasize that only this common center has an invariant meaning, and
in fact it has a well-known interpretation in terms of TQFTs, see Subsection \ref{TQFT}.
\erem

\blemma \label{adj}
Let $(X,e_X)\in \2Z_1(\2C)$ and $Y\in\2C$. Then there is a isomorphism between the 
vector spaces $\Hom_\2C(X,Y)$ and $\Hom_\2B(F(X,e_X), \oj (Y\boxtimes\11)J)$. 
\elemma
\prf The proof is similar to the one of Proposition \ref{fullf}, but simpler. Let
$s\in\Hom_\2C(X,Y)$ and let 
$\ul{t}\in\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$ be defined (using Lemma
\ref{11mor}) by $\ul{t}[i]=\delta_{i0}s$. Then the map 
$\pi: s\mapsto\ul{s}=\ul{t}\bullet p_{(X,e_X)}\in\Hom_\2B(F(X,e_X),\oj (Y\boxtimes\11)J)$ 
is injective since 
$(\ul{t}\bullet p_{(X,e_X)})[i]=\lambda^{-1}\id_{X_i}\otimes s\circ e_X(X_i)$, in
particular $(\ul{t}\bullet p_{(X,e_X)})[0]=\lambda^{-1}s$. Let, conversely, 
$\ul{s}\in\Hom_\2B(F(X,e_X),\oj (Y\boxtimes\11)J)$, i.e.\
$\ul{s}=\ul{s}\bullet p_{(X,e_X)}\in\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$. 
Then 
\[ d_k\lambda^2\cdot \ul{s}[k]= 
\sum_{m,l\in \Gamma}\sum_{\alpha=1}^{N_{ml}^k} \ d_md_l \ \ 
\begin{tangle}
\hstep\object{X_k}\step[1.5]\object{Y}\\
\hh\hstep\id\step[1.5]\id\\
\hh\step[-1.5]\mmobj{t_{m,l}^{'k\alpha}}\step[1.5]\hcd\step\id\\
\hh\step[-1.2]\mobj{X_m}\step[1.2]\id\step\id\step\id\\
\hh\id\step\frabox{\ul{s}[l]} \\
\hxx\step\id\mobj{X_l}\\
\hh\id\step\hcu\mobj{t_{m,l}^{k\alpha}}\\
\hh\id\step[1.5]\id\\
\object{X}\step[1.5]\object{X_k}
\end{tangle}
\ \ = \ \sum_{m,l\in \Gamma}\sum_\alpha \ d_md_l\frac{d_k}{d_m}
\begin{tangle}
\object{X_k}\step[1.5]\object{\ol{\ve}(\ol{X_l})}\step[1.5]\object{Y}\\
\hh\id\step\hcoev\step\id\\
\hh\step[-1.2]\mmobj{s_{k\ol{l}}^{m\alpha}}\step[1.2]\hcu\step\id\step\id\\
\hh\hstep\id\step[1.5]\frabox{\ul{s}[l]} \\
\hstep\id\step\ddh\hstep\id\\
\hstep\hxx\mobj{X_m}\step[1.5]\id\mobj{X_l}\\
\step[-0.5]\hdd\step[-0.5]\mmobj{{s'}_{k\ol{l}}^{m\alpha}}\step\hcd\step\id\\
\hh\id\step\id\step\hev\mmobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_k}
\end{tangle}
\]
\[ = d_k \ \sum_{m,l\in \Gamma}\sum_\alpha  d_l \ \ 
\begin{tangle}
\object{X_k}\step[3]\object{Y}\\
\hh\id\step\hcoev\step\id\\
\hh\hcu\step\id\step\id\\
\hh\step[-0.7]\mobj{X_m}\step[1.2]\id\step[1.5]\frabox{\ul{s}[l]} \\
\hh\hcd\step\id\step\id\\
\id\step\hxx\step\id\mobj{X_l}\\
\hxx\step\hev\\
\object{X}\step\object{X_k}
\end{tangle}
\ \ = d_k \ \sum_{l\in \Gamma} \ d_l \ \
\begin{tangle}
\object{X_k}\step[1.5]\object{\ol{\ve}(\ol{X_l})}\step[1.5]\object{Y}\\
\hh\id\step\hcoev\step\id\\
\hh\id\step\id\step\id\step\id\\
\hh\id\step\id\step\frabox{\ul{s}[l]} \\
\hh\id\step\id\step\id\step\id\\
\id\step\hxx\step\id\mobj{X_l}\\
\hxx\step\hev\step[-.5]\mmobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_k}
\end{tangle}
\]
Putting $k=0$ we obtain
\[ \lambda^2\cdot \ul{s}[0]= \sum_l d_l \ \  
\begin{tangle}
\Step\object{Y}\\
\hh\hcoev\step\id\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{\ul{s}[l]} \\

\hxx\step\id\mobj{X_l}\\
\hh\id\step\hev\\
\object{X}
\end{tangle}
\]
and plugging this back into the preceding equation we obtain
\[ \ul{s}[k]=\id_{X_i}\otimes \ul{s}[0]\circ e_X(X_i). \]
Thus $\ul{s}$ is in the image of $\pi$, which proves that $\pi$ is an isomorphism.
\qed

\bprop Let $(X,e_X)\in \2Z_1(\2C)$ be simple and let $N^X_i=\dim\Hom_\2C(X_i,X)$.
Then the (simple) object $F(X,e_X)\in\2B$ is contained in $\oj (X_i\boxtimes\11)J$
with multiplicity $N^X_i$. Let $\{ p_i^\alpha \}, \{ {p'}_i^\alpha \}$ be bases in 
$\Hom_\2C(X_i,X), \Hom_\2C(X, X_i)$, respectively, normalized by
${p'}_i^{\alpha}\circ p_i^\beta=\delta_{\alpha\beta}\id_{X_i}$. Then
$q_i^\alpha\in\Hom_\2E(F(X,e_X), \oj (X_i\boxtimes\11)J)$,
${q'}_i^{\alpha}\in\Hom_\2E(\oj (X_i\boxtimes\11)J,F(X,e_X))$ defined by 
\bean q_i^\alpha[k] &=& \left(\frac{d(X)}{\lambda^2 d_i}\right)^{1/2} \id_{X_k}\otimes
  {p'}_i^{\alpha} \mcirc e_X(X_k),\\ 
   {q'}_i^{\alpha}[k] &=& \left(\frac{d(X)}{\lambda^2 d_i}\right)^{1/2} e_X(X_k) \mcirc
   p_i^{\alpha}\otimes \id_{X_k}  
\eean
satisfy ${q'}_i^{\alpha}\bullet q_i^\beta= \delta_{\alpha\beta} \, \id_{F(X,e_X)}$. 
The idempotent $z^i_{(X,e_X)}=\sum_{\alpha=1}^{N^X_i}q_i^\alpha\bullet {q'}_i^\alpha$ in 
$\End_\2E(\oj (X_i\boxtimes\11)J)$ corresponding to the isotypic component of $(X,e_X)$
is given by 
\begin{equation}z^i_{(X,e_X)}[k]= \frac{d(X)}{\lambda d_i} \sum_{\alpha=1}^{N^X_i} \id_{X_k}\otimes
  {p'_i}^\alpha \circ e_X(X_k) \circ p_i^\alpha \otimes\id_{X_k}. \end{equation}
\label{dualb}\eprop

\brem The choice of square root of $d(X)$ is immaterial, but it must be the same in the 
equations defining $q_i^\alpha$ and ${q'}_i^\alpha$.
\erem
\prf In view of the preceding lemma all that remains to be verified is the normalization. 
Since $(X,e_X)$ is simple we have 
${q'}_i^{\alpha}\bullet q_i^\beta=c_{\alpha\beta}\,\id_{F(X,e_X)}$. Plugging
$q_i^\alpha[k], {q'}_i^\alpha[k]$ into (\ref{mul}) and comparing with the middle term of
the computation in Lemma \ref{condexp1} (with $Z=X_k$) we see that 
\bean ({q'}_i^{\alpha}\bullet q_i^\beta)[k] &=& \frac{d(X)}{\lambda d_i} \
   \id_{X_k}\otimes E_{X,X}(p_i^{\alpha}\circ{p'}_i^\beta)\mcirc e_X(X_k) \\
 &=& \frac{tr_X\circ E_{X,X}(p_i^{\alpha}\circ{p'}_i^\beta)}{\lambda d_i} \  e_X(X_k), 
\eean
since $E_{X,X}(p_i^{\alpha}\circ{p'}_i^\beta)$ is a scalar multiple of $\id_X$ due to the
simplicity of $(X,e_X)$. Now, by definition of the functor $F$ we have
$\id_{F(X,e_X)}[k]=\lambda^{-1}e_X(X_k)$, thus by comparison we find
$c_{\alpha\beta}=d_i^{-1} tr_X\circ E_{X,X}(p_i^{\alpha}\circ{p'}_i^\beta)$. Computing
\[ tr_X\circ E_{X,X}(p_i^{\alpha}\circ{p'}_i^\beta)=tr_X(p_i^{\alpha}\circ{p'}_i^\beta)=
  tr_{X_i}({p'}_i^{\alpha}\circ p_i^\beta)=d_i   \delta_{\alpha\beta}, \] 
where we used the invariance of the trace under the conditional expectation and cyclic
permutations, we obtain $c_{\alpha\beta}=\delta_{\alpha\beta}$ as claimed.

Now we can compute $z^i_{(X,e_X)}=\sum_\alpha q_i^\alpha\bullet {q'}_i^\alpha$ as follows:
\[ z^i_{(X,e_X)}[k]= \frac{d(X)}{\lambda^2 d_i} \sum_{\alpha=1}^{N^X_i} 
    \sum_{l,m\in \Gamma} \sum_{\beta=1}^{N_{lm}^k} \frac{d_ld_m}{\lambda d_k} \ 
\begin{tangle}
\step[1.5]\hstep\object{X_k}\step[1.5]\object{X_i}\\
\hh\mobj{{t'}_{l,m}^{k,\beta}}\step[1.5]\hcd\step\id\\
\hh\step[1.5]\id\mobj{X_l}\step\id\mobj{X_m}\step\id\\
\step[1.5]\id\step\id\step\O {{p'}_i^\alpha} \\
\step[1.5]\id\step\hxx \\
\hh\step[1.5]\id\step\id\obj{X}\step\id\\
\step[1.5]\hxx\step\id \\
\step[1.5]\O {p_i^\alpha}\step\id\step\id \\
\hh\step[1.5]\id\step\id\obj{X_l}\step\id\obj{X_m}\\
\hh\step[1.5]\id\step\hcu\obj{t_{l,m}^{k,\beta}}\\
\step[1.5]\object{X_i}\step[1.5]\object{X_k}
\end{tangle}
\ \ = \ \ 
\frac{d(X)}{\lambda d_i} \sum_{\alpha=1}^{N^X_i} \ \ 
\begin{tangle}
\hstep\object{X_k}\step\object{X_i}\\
\hh\hstep\id\step\id\\
\hstep\id\step\O {{p'}_i^\alpha} \\
\mobj{X}\hstep\hxx \\
\hstep\O {p_i^\alpha}\step\id \\
\hh\hstep\id\step\id\\
\hstep\object{X_i}\step\object{X_k}\\
\end{tangle}
\]
We have pulled ${t'}_{lm}^{k\beta}$ through the braiding and used (\ref{ddN}).


\qed

\bprop Let $(X,e_X)\in \2Z_1(\2C)$ be simple. The minimal central idempotent $z_{(X,e_X)}$
in $\Xi_L$ corresponding to $F(X,e_X)$ is given by
\begin{equation}z_{(X,e_X)}[i,j,k]= \delta_{ik} \frac{d(X)}{\lambda d_i}
  \sum_{\alpha=1}^{N^X_i} \id_{X_j}\otimes {p'_i}^\alpha \circ 
   e_X(X_j) \circ p_i^\alpha \otimes\id_{X_j}, \label{isotyp}\end{equation}
where the $\{ p_i^\alpha \}, \{ {p'_i}^\alpha \},\ i\in \Gamma, \alpha=1,\ldots,N^X_i$
are bases as in Proposition \ref{dualb}. \eprop
\prf Since $\oj \hat{Y}_LJ$ is a direct sum $\bigoplus_i \oj (X_i\boxtimes\11)J$ we
only need to add up the idempotents in $\End_\2E(\oj (X_i\boxtimes\11)J)$, which we
identified in Proposition \ref{dualb}, inside $\Xi_L=\End_\2E(\oj \hat{Y}_LJ)$. With the
isomorphism (\ref{tube1}) the claimed identity follows. \qed

As a first application of the tube algebra we can give an easy bound on the `size' of the
quantum double:
\bcoro The number $\#\2Z_1(\2C)$ of isomorphism classes of simple objects of $\2Z_1(\2C)$
satisfies 
\[ \#\2Z_1(\2C) \le \sum_{i,j\in \Gamma} \dim\Hom_\2C(X_iX_j,X_jX_i). \]
\ecoro
\prf By the equivalence $\2Z_1(\2C)\stackrel{\otimes}{\simeq}\2B$ and the above
considerations we have $\#\2Z_1(\2C)=\dim Z(\Xi_L)$. Since the center of $\Xi_L$ is spanned
by the $z_{(X,e_X)}$ constructed above and since $z_{(X,e_X)}[i,j,k]=0$ if $i\ne k$ we
have 
\[ Z(\Xi_L)\subset\bigoplus_{i,j}\Hom_\2C(X_iX_j,X_jX_i), \]
which implies the bound.
\qed

\brem If $G$ is a finite abelian group whose order is non-zero in $\7F$ then
$G-\mbox{mod}$ is semisimple, symmetric and all simple objects have dimension one. Thus
the right hand side of the above inequality equals $|G|^2$. In view of
$\2Z_1(G-\mbox{mod})\simeq D(G)-\mbox{mod}$ we have $\#\2Z_1(G-\mbox{mod})=|G|^2$, which
proves that the bound is optimal.
\erem

The next two subsections, which do not pretend much originality, will follow \cite{iz2}
quite closely except for shortcuts in the proofs.







\subsection{Invertibility of the $S$-matrix}\label{modular}
In this subsection we will prove that the $S$-matrix 
\[ S((X,e_X),(Y,e_Y))=\quad
\begin{tangle}
\coev\step\coev\\
\id\Step\hxx\Step\id\\
\id\step[.2]{\scriptsize \mobj{(X,e_X)}}\step[1.8]\hxx\step[-.2]{\scriptsize \mobj{(Y,e_Y)}}\step[2.2]\id\\
\step[-3]\mobj{\ve(\ol{(X,e_X)})}\step[3]\ev\step\ev\mobj{\ve((Y,e_Y))}
\end{tangle}
\]
of $\2Z_1(\2C)$ is invertible, thus $\2Z_1(\2C)$ is modular in the sense of Turaev
\cite{t}. The strategy will be to define a vector space isomorphism $\6S$ of the
subspace 
\[ \Xi_0=\bigoplus_{i,j\in \Gamma}\Hom_\2C(X_iX_j,X_jX_i) \]
of $\Xi_L$ which we have seen to contain the center of $\Xi_L$. We will prove that $\6S$
leaves $Z(\Xi_L)$ stable and that the $S$-matrix of $\2Z_1(\2C)$ is the matrix
representation of $\6S\restr Z(\Xi_L)$ w.r.t.\ the basis 
$\{ d(X)^{-1}z_{(X,e_X)},\ (X,e_X)\ \mbox{simple}\}$.

\blemma 
The application $\6S: \Xi_0\rarr\Xi_0$ defined by
\begin{equation}
\begin{tangle}
\object{X_j}\step\object{X_i}\\
\hh\id\step\id\\
\hh\frabox{s}\\
\hh\id\step\id\\
\object{X_i}\step\object{X_j}
\end{tangle} \quad\ \  \mapsto \quad
\begin{tangle}
\Step\object{X_i}\step\object{X_{\ol{\jmath}}}\\
\hh\hcoev\step\id\step\id\\
\hh\id\step\id\mobj{X_j}\step\id\step\id\\
\hh\id\step\frabox{s}\step\id\\
\hh\id\step\id\step\mobj{X_j}\id\step\id\\
\hh\id\step\id\step\hev\\
\object{X_{\ol{\jmath}}}\step\object{X_i}
\end{tangle}
\label{slocal}\end{equation}
on the direct summands, where $\begin{tangle}\hh\hcoev\end{tangle}$,
$\begin{tangle}\hh\hev\end{tangle}$ are any solution of the duality equation for
$X_j, X_{\ol{\jmath}}$, is a vector space isomorphism of order four. 
\elemma 
\prf The above map
$\Hom_\2C(X_iX_j,X_jX_i)\rarr\Hom_\2C(X_{\ol{\jmath}}X_i,X_iX_{\ol{\jmath}})$ is an
isomorphism by duality. The same holds for $\6S$ which is just a direct sum of such
isomorphisms, since the map $(i,j)\mapsto(\ol{\jmath},i)$ is a permutation of 
$\Gamma\times \Gamma$. That $\6S$ has order four is an obvious consequence of sphericity 
of $\2C$. 
\qed 

\blemma \label{slemma}Let $(X,e_X), (Y,e_Y)$ be simple objects in $\2Z_1(\2C)$. Then
\begin{equation}\label{smat}
  z_{(Y,e_Y)}\6S(z_{(X,e_X)})= \frac{d(X)}{d(Y)\lambda^2}S(\ol{(X,e_X)},(Y,e_Y))\cdot
  z_{(Y,e_Y)}.  
\end{equation}
\elemma
\prf With (\ref{isotyp}), (\ref{slocal}), and (\ref{tube2}) we compute
\bean \lefteqn{ \left( z_{(Y,e_Y)}\6S(z_{(X,e_X)}) \right)[i,j,i]}  \\
 && = (d_j\lambda)^{-1}
\sum_{k,l}\sum_{\alpha=1}^{N_{kl}^j}\sum_{\beta=1}^{N_k^X}\sum_{\gamma=1}^{N_i^Y} 
d_kd_l \frac{d(X)}{\lambda d_k}\frac{d(Y)}{\lambda d_i} \quad
\begin{tangle}
\step[4]\object{X_j}\Step\object{X_i}\\
\step[2]\mobj{{t'}_{kl}^{j\alpha}}\step\cd\step\id\\
\step[3]\id\Step\id\step\O {{q'}_i^\gamma}\\
\step[2]\mobj{X_k}\step\id\step[1.5]\mobj{Y}\hstep\hxx\\
\step[3]\id\Step\O {q_i^\gamma}\step\id\\
\coev\step\id\Step\id\step\id\\
\id\Step\id\step\O {{p'}_k^\beta}\Step\id\step\id\\
\id\step[1.5]\mobj{X}\hstep\hxx\step\mobj{X_i}\step\id\step\id\\
\id\Step\O {p_k^\beta}\step\id\Step\id\step\id\\
\id\Step\id\mobj{X_k}\step\ev\step\id\mobj{X_l}\\
\id\Step\Cu\step[-.2]\mobj{t_{kl}^{j\alpha}}\\
\object{X_i}\step[4]\object{X_j}
\end{tangle}
\eean
\[ =(d_j\lambda)^{-1}\sum_{k,l}\sum_{\alpha=1}^{N_{kl}^j}\sum_{\beta=1}^{N_k^X}
\sum_{\gamma=1}^{N_i^Y} d_kd_l \frac{d(X)}{\lambda d_k}\frac{d(Y)}{\lambda d_i} 
\quad\quad\quad
\begin{tangle}
\step\object{X_j}\step[3]\object{X_i}\\
\step[-1]\mobj{{t'}_{kl}^{j\alpha}}\step\cd\Step\O {{q'}_i^\gamma}\\
\id\mobj{X_k}\Step\mobj{Y}\xx\mobj{e_Y(X_l)}\\
\O {{p'}_k^\beta}\Step\O {q_i^\gamma}\Step\id\\
\step[-2.5]\mmobj{e_X(X_i)^{-1}}\step[2.5]\x\mobj{X}\Step\id\\
\id\Step\O {p_k^\beta}\Step\id\mobj{X_l}\\
\id\Step\cu\mobj{t_{kl}^{j\alpha}}\\
\object{X_i}\step[3]\object{X_j}
\end{tangle}
\]
where we have used Lemma \ref{l3}.
Replacing 
\[
\begin{tangle}
\object{X_k}\Step\object{X_l}\\
\cu\mobj{t_{kl}^{j\alpha}}\\
\step\object{X_j}
\end{tangle}
\quad\quad\quad \mbox{by}\quad\quad \left(\frac{d_j}{d_l}\right)^{1/2}
\begin{tangle}
\object{X_k}\step[3]\object{X_l}\\
\id\Step\cd\mmmobj{{s'}_{\ol{k}j}^{l\alpha}}\\
\ev\step[-.5]\mobj{\ve(X_k)}\step[2.5]\id\\
\step[4]\object{X_j}
\end{tangle} 
\]
where $\{{s'}_{\ol{k}j}^{l\alpha}\}$ is a basis in $\Hom(\ol{X_k}X_j,X_l)$, 
and correspondingly for the dual basis, pulling ${s'}_{\ol{k}j}^{l\alpha}$
through the half braiding $e_Y(\cdot)$ and summing over $l, \alpha$ we obtain 
\[ = \frac{d(X)d(Y)}{d_i\lambda^3} \sum_k\sum_{\beta=1}^{N_k^X}\sum_{\gamma=1}^{N_i^Y}
\quad\quad 
\begin{tangle}
\step[4]\object{X_j}\Step\object{X_i}\\
\mobj{\ol{\ve}(X_k)}\step[4]\id\Step\O {{q'}_i^\gamma}\\
\coev\Step\xx\\
\step[-1]\mobj{X_k}\step\id\Step\mobj{Y}\xx\Step\id\\
\O {{p'}_k^\beta}\Step\O {q_i^\gamma}\Step\id\Step\id\\
\x\mobj{X}\Step\id\Step\id\\
\id\Step\O {p_k^\beta}\Step\id\mobj{\ol{X_k}}\Step\id\\
\id\Step\ev\step[-2]\mobj{\ve(X_k)}\step[4]\id\\
\object{X_i}\step[6]\object{X_j}
\end{tangle}
\]
By sphericity of $\2C$, naturality of the $e_Y(\cdot)$ and 
$\sum_{k,\beta} p_k^\beta\circ {p'}_k^\beta=\id_X$ this equals
\[ = \frac{d(X)d(Y)}{d_i\lambda^3} \sum_{\gamma=1}^{N_i^Y} \quad\quad
\begin{tangle}
\step[4]\object{X_j}\Step\object{X_i}\\
\mobj{\ol{\ve}(X)}\step[4]\id\Step\O {{q'}_i^\gamma}\\
\coev\Step\xx\\
\step[-.6]\mobj{X}\step[.6]\id\Step\mobj{Y}\xx\Step\id\\
\id\Step\O {q_i^\gamma}\Step\id\Step\id\\
\x\mobj{X}\Step\id\Step\id\mobj{\ol{X}}\\
\id\Step\ev\step[-2]\mobj{\ve(X)}\step[4]\id\\
\object{X_i}\step[6]\object{X_j}
\end{tangle}
\]
Using naturality of $e_X(\cdot)$ we can pull $q_i^\gamma$ through
$e_X(X_i)^{-1}$. Furthermore, since $(Y,e_Y)$ is simple we have 
\[
\begin{tangle}
\object{\ol{\ve}(X)}\Step\object{Y}\\
\hh\hcoev\step\id\\
\step[-.6]\mobj{X}\step[.6]\id\step\hxx\mobj{e_Y(\ol{X})}\\
\step[-2.5]\mobj{e_X(Y)^{-1}}\step[2.5]\hx\step\id\\
\hh\id\step\hev\\
\object{Y}\step\mmobj{\ve(X)}
\end{tangle} 
\quad\quad\quad = \quad\quad
\begin{tangle}
\object{\ol{\ve}(X)}\Step\object{Y}\\
\hh\hcoev\step\id\\
\id\step\hxx\mobj{e_Y(\ol{X})}\\
\step[-.6]\mobj{X}\step[.6]\id\step\hxx\mobj{e_{\ol{X}}(Y)}\\
\hh\hev\step\id\\
\object{\ve(X)}\Step\object{Y}
\end{tangle}
\quad\quad\quad =\frac{S(\ol{(X,e_X)},(Y,e_Y))}{d(Y)}\,\id_Y, \]
and (\ref{smat}) follows by comparison with (\ref{isotyp}).
\qed

\bprop $\6S$ maps the center of $\Xi_L$ into itself. The modular matrix $S$ is invertible.
\eprop
\prf Summing (\ref{smat}) over all classes of simple $(Y,e_Y)$ and using 
$\sum_{(X,e_X)} z_{(X,e_X)}=1_{\Xi_L}$ we obtain
\begin{equation}\6S \left(\frac{z_{(X,e_X)}}{d(X)}\right)= 
\sum_{(Y,e_Y)} \lambda^{-2}S(\ol{(X,e_X)},(Y,e_Y)) \, \frac{z_{(Y,e_Y)}}{d(Y)}, 
\label{sss}\end{equation}
whence the first claim. Therefore the isomorphism $\6S: \Xi_0\rarr\Xi_0$ restricts to
$Z(\Xi_L)$ and the matrix $\lambda^{-1}S(\ol{\cdot},\cdot)$ expresses the action of
$\6S\restr Z(\Xi_L)$ in terms of the basis $\{ d(X)^{-1}z_{(X,e_X)} \}$. Thus $S$ is
invertible. 
\qed 

\brem 1. Note that $\lambda^2=\dim\2C=\sqrt{\dim\2Z_1(\2C)}$. This is the correct
normalization since $(\dim\2M)^{-1/2}S$ is known to be of order four in every modular
category $\2M$ \cite{t,khr1}.

2. An alternative proof of the modularity of $\2Z_1(\2C)$ and of
$\dim\2Z_1(\2C)=(\dim\2C)^2$ could be given as follows. If $\2C$ satisfies the assumptions
of our Theorem \ref{main1}, there exists a finite dimensional quantum groupoid $H$ such
that $\2C$ is monoidally equivalent to the category $H-\mbox{Mod}$ of left modules over
$H$. In \cite{ntv}, the quantum double of finite dimensional quantum groupoids was
defined, and the category $D(H)-\mbox{Mod}$ was shown to be modular. Modularity of
$\2Z_1(\2C)$ follows, provided one proves the equivalence $\2Z_1(\2C)\simeq
D(H)-\mbox{Mod}$ of braided tensor categories. Proceeding in analogy to the Hopf algebra
case \cite{ka}, this should not present any serious difficulty. Yet, we think that a
direct categorical proof which avoids weak Hopf algebras is more satisfactory.

3. The tensor category $\2B=\END_\2E(\6B)$ defined in \cite{mue09} is known to be
equivalent to the category of $Q-Q$-bimodules, cf.\ \cite[Remark 3.18]{mue09}. Combining
this with the ideas of \cite{ostr}, it should be possible to give a considerably simpler
proof of the braided equivalence $\2Z_1(\2C)\simeq\2B$.
\erem

In order to give the promised analogue of the (rather trivial) observation
$Z_1(Z_0(S))=\{\id_S\}$ from the Introduction we need the following
\bdefin The center $\2Z_2(\2C)$ of a braided monoidal category $\2C$ is the full
subcategory defined by
\[ \obj\,\2Z_2(\2C)=\{ X\in\obj\,\2C\ | \ c(X,Y)=c(Y,X)^{-1} \ \forall Y\in\obj\,\2C \}. \]
\label{Z2}\edefin
Obviously the subcategory $\2Z_2(\2C)$ is symmetric, contains the monoidal unit and is
stable w.r.t. \ direct sums, retractions (in particular isomorphisms, thus replete) and
duals. 

\bcoro The category $\2Z_2(\2Z_1(\2C))$ is trivial, i.e. all objects are direct multiples
of the monoidal unit. 
\ecoro
\prf It is well known that a semisimple braided category $\2A$ containing a simple object
$X\not\cong\11$ in $\2Z_2(\2A)$ is not modular. ($X\in\2Z_2(\2A)$ implies
$S(X,Y)=d(X)d(Y)$ for all $Y$. This is colinear to $S(\11,Y)=d(Y)$.) 
\qed

\brem One can in fact prove \cite{bebl} that $\2C$ is modular iff $\dim\2C\ne 0$ and
the center $\2Z_2(\2C)$ consists only of the direct multiples of the unit or,
equivalently, iff all simple objects of $\2Z_2(\2C)$ are isomorphic to the unit object. We
will show this in Subsection \ref{moddoub} as a byproduct of a more general computation. 
\erem

\brem There is little doubt that a more conceptual understanding of the above proof (and
of the subsequent subsection) can be gained by looking at them in the light of
Lyubashenko's works \cite{ly1,ly2}. The latter also raise the question whether there is a
generalization to non-semisimple Noetherian categories. We hope to pursue this elsewhere. 
\erem

\brem It is natural to ask whether there are higher dimensional analogues to the above
result in $d=1$ and the trivial case $d=0$ mentioned in the Introduction. (See
\cite{baez2} for a review of the theory of n-categories.) Thus, considering the center
constructions in $d=2$ \cite{baez,crans}, can one show that
$\2Z^{(2)}_3(\2Z^{(2)}_2(\2C))$ is trivial? Here
$\2C, \2Z^{(2)}_2(\2C), \2Z^{(2)}_3(\2Z^{(2)}_2(\2C))$ are (semisimple spherical) braided,
sylleptic and symmetric 2-categories, respectively.
\erem
