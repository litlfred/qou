---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-014-53-computation-of-the-gauss-sums
section_title: "Computation of the Gauss sums"
section_number: 5.3
pages: 39-41
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.962
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
