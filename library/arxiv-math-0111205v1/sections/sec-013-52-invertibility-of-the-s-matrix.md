---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-013-52-invertibility-of-the-s-matrix
section_title: "Invertibility of the $S$-matrix"
section_number: 5.2
pages: 34-39
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.956
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{modular}
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
