---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-010-43-f-is-essentially-surjective
section_title: "$F$ is essentially surjective"
section_number: 4.3
pages: 25-29
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.973
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{esssurj}
In order to conclude that $F$ establishes an equivalence 
$\2B\stackrel{\otimes}{\cong}\2Z_1(\2C)$ of tensor categories it remains to prove that $F$
is essentially surjective, viz. that for every object $Y$ of $\2B$ there is
$(X,e_X)\in\2Z_1(\2C)$ such that $F(X,e_X)\cong Y$. We begin with a result due to Izumi
\cite{iz2}. 

\blemma Let $Y\in\2C$ be simple. Then the 1-morphisms 
$(Y\boxtimes\11)J,\, (\11\boxtimes Y^\op)J: \ \6B\rarr\6A$ and 
$\oj(Y\boxtimes\11),\, \oj(\11\boxtimes Y^\op): \6A\rarr\6B$ are
simple. Furthermore, 
\bean 
  (Y\boxtimes\11)J &\cong & (\11\boxtimes\ol{Y}^\op)J, \\
  \oj(Y\boxtimes\11) &\cong & \oj(\11\boxtimes\ol{Y}^\op). 
\eean
\label{iz1}\elemma
\prf Let $Y,Z\in\2C$. By duality be have the isomorphism
\[ \Hom_\2E((Y\boxtimes\11)J, (Z\boxtimes\11)J)\cong
  \Hom_\2E((Y\boxtimes\11)J\oj, Z\boxtimes\11)=
  \Hom_\2A((Y\boxtimes\11)Q, Z\boxtimes\11) \]
of vector spaces. In view of $Q\cong\bigoplus_i X_i\boxtimes X^\op_i$ this
implies 
\[ \Hom_\2E((Y\boxtimes\11)J, (Z\boxtimes\11)J)\cong \Hom_\2C(Y,Z). \]
In particular, if $Y\in\2C$ is simple then 
$(Y\boxtimes\11)J\in\Hom_\2E(\6B,\6A)$ is simple, and so is
$(\11\boxtimes Y^\op)J$ by a similar argument. Furthermore,
\[ \Hom_\2E((Y\boxtimes\11)J, (\11\boxtimes\ol{Y}^\op)J)
  \cong \Hom_\2E(Y\boxtimes Y^\op, J\oj) = \Hom_\2A(Y\boxtimes Y^\op, Q). \]
Now, $Y\boxtimes Y^\op$ is simple and contained in $Q$ with
multiplicity one, thus these spaces are one dimensional and
\[ (Y\boxtimes\11)J \cong (\11\boxtimes\ol{Y}^\op)J. \]
Similar arguments apply to the $\6A-\6B$-morphisms. \qed

\bcoro \label{cor}
Let $X, Y\in\2C$. Then there is $Z\in\2C$ such that
\[ \oj(X\boxtimes Y^\op)J\cong \oj(Z\boxtimes\11)J \]
and such that the isomorphisms 
\bean e &\in& \Hom_\2E(\oj(X\boxtimes Y^\op)J, \oj(Z\boxtimes\11)J)
  \equiv\Hom_\2A((X\boxtimes Y^\op)Q, Q(Z\boxtimes\11)), \\
  f &\in& \Hom_\2E(\oj(Z\boxtimes\11)J, \oj(X\boxtimes Y^\op)J)\equiv
  \Hom_\2A((Z\boxtimes\11)Q, Q(X\boxtimes Y^\op)) \eean
can be chosen such that
\[ e=v\otimes \tilde{e},\quad f=v\otimes \tilde{f} \]
with $\tilde{e}\in\Hom_\2A((X\boxtimes Y^\op)Q, Z\boxtimes\11)$ and 
$\tilde{f}\in\Hom_\2A((Z\boxtimes\11)Q, X\boxtimes Y^\op)$. (Alternatively, one can 
find morphisms of the form $e=\tilde{e}\otimes v', f=\tilde{f}\otimes v'$.)
\ecoro
\prf Using the lemma we compute 
\[ \oj(X\boxtimes Y^\op)J=\oj(X\boxtimes\11)(\11\boxtimes Y^\op)J\cong
  \oj(X\boxtimes\11)(\ol{Y}\boxtimes\11)J=\oj(X\ol{Y}\boxtimes\11)J. \]
We put $Z=X\ol{Y}$ and denote by $\hat{e}$ the isomorphism 
$(\11\boxtimes Y^\op)J\rarr(\ol{Y}\boxtimes\11)J$ provided by the preceding lemma.
Now the claim follows with $\tilde{e}=\id_{X\boxtimes\11}\times\hat{e}$ if we keep in mind
that tensoring $\tilde{e}$ with $\id_{\oj}$ (in $\2E$) amounts to tensoring with $v$ in
$\2A$, as follows from the definition of $\2E$. $\tilde{f}$ is defined
similarly. Alternatively, using the isomorphism 
$\oj(X\boxtimes\11)\cong\oj(\11\boxtimes\ol{X}^\op)$ one obtains a solution with
$e=\tilde{e}\otimes v'$ etc.
\qed

The lemma implies that every object of $\2B$ is isomorphic to one of the form
$(\oj(X\otimes\11)J, p_X)$. This looks quite promising since also $F(X,e_X)$ has this
form. In fact, by Lemma \ref{11mor} and Lemma \ref{halfbr} we obtain a family of morphisms 
$\{ e_X(Y): XY\rarr YX,\ Y\in\2C\}$ natural w.r.t.\ $Y$. Yet, in order to conclude that
this is a half braiding (and therefore $(\oj(X\otimes\11)J, p)=F(X, e_X)$) we need that
$p$ satisfies (\ref{uu2}) and $p[0]=\id_X$. Not every object of $\2B$ satisfies these
conditions as is exemplified, e.g., the object
$\oj(X\boxtimes\11)J=(\oj(X\boxtimes\11)J,p)$ where 
\[ p=\id_{\oj(X\boxtimes\11)J}=v\otimes\id_{X\boxtimes\11}\otimes v'
  \in\Hom_\2A((X\boxtimes\11)Q,Q(X\boxtimes\11)). \]
One easily verifies that $p$ does not satisfy (\ref{uu2}). In view of
$p[i]=\delta_{i0}\id_X$ it is also clear that the corresponding $e_X(Y)$ fails to be
invertible for all $Y$.

The following result on the 2-category $\2E$ is quite general in that it does not rely on 
$\2A=\2C\boxtimes\2C^\op$.
\blemma \label{qq-lemma}
Let $X\in\2A$ and $p=p\bullet p\in\End_\2E(\oj XJ)$. Then there is $Y\in\2A$, 
$q=q\bullet q\in\End_\2E(\oj YJ)$ such that $(\oj YJ, q)\cong(\oj XJ, p)$ and in addition
\begin{equation} \label{qq}
\begin{tangle}
\object{Q}\step\object{Q}\step[.7]\object{Y}\\
\hh\id\step\id\hstep\id\\
\hcu\hstep\id\\
\hh\hstep\frabox{q}\\
\hstep\id\step\id\\
\hstep\object{Y}\step\object{Q}
\end{tangle}
\quad=\lambda\quad
\begin{tangle}
\object{Q}\step\object{Q}\step\object{Y}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{q}\\
\hh\id\step\id\step\id\\
\hh\frabox{q}\step\id\\
\id\step\hcu\\
\object{Y}\step[1.5]\object{Q}
\end{tangle} 
\end{equation}
\elemma

\brem The condition (\ref{qq}) implies $q\bullet q=q$ as is seen by multiplication with
$w'\otimes\id_Y$ from the left.  
\erem
\prf Using the (non-strict) unit $\6B-\6B$ morphism $\11_\6B=(\oj J, \lambda^{-1}\id_Q)$
we put $(Y,q)=\11_\6B(X,p)=(QX, \lambda^{-1}\id_Q\times p)$. The isomorphism 
$(\oj YJ, q)\cong(\oj XJ, p)$ was proven in \cite[Theorem 3.12]{mue09}. We claim that $q$
satisfies (\ref{qq}). In terms of $(Y,q)$ (and keeping in mind that $Y=QX$ !) the left
hand side of (\ref{qq}) is given by 
\[ \lambda^{-1}\quad
\begin{tangle}
\hh\hcu\step\id\step[1.5]\id\\
\hh\hstep\id\step\hcd\step\id\\
\hh\hstep\id\step\id\step\frabox{p}\\
\hstep\hcu\step\id\step\id\\
\hstep\hstep\object{Q}\step[1.5]\object{X}\step\object{Q}
\end{tangle}
\]
For the right hand side we compute
\[ \lambda\cdot\lambda^{-2}\quad
\begin{tangle}
\id\hstep\hstep\id\step\hcd\step\id\\
\hh\id\hstep\hstep\id\step\id\step\frabox{p}\\
\hh\id\hstep\hstep\hcu\step\id\step\id\\
\hh\id\step\hcd\step\id\step\id\\
\hh\id\step\id\step\frabox{p}\step\id\\
\hh\hcu\step\id\step\id\step\id\\
\hh\hstep\id\step[1.5]\id\step\hcu\\
\hstep\object{Q}\step[1.5]\object{X}\step[1.5]\object{Q}
\end{tangle}
\quad=\lambda^{-1}\quad
\begin{tangle}
\id\step\cu\step[1.5]\id\\
\id\step\cd\step[1.5]\id\\
\hh\id\step\id\step[1.5]\hcd\step\id\\
\hh\id\step\id\step[1.5]\id\step\frabox{p}\\
\hh\id\step\id\step[1.5]\id\step\id\step\id\\
\hh\id\step\id\step[1.5]\frabox{p}\step\id\\
\hh\hcu\step[1.5]\id\step\id\step\id\\
\hh\hstep\id\Step\id\step\hcu\\
\hstep\object{Q}\Step\object{X}\step[1.5]\object{Q}
\end{tangle}
\quad=\lambda^{-1}\quad
\begin{tangle}
\hh\id\step\cu\step\id\\
\hh\id\step\cd\step\id\\
\hh\id\step\id\step\frabox{p}\\
\hcu\step\id\step\id\\
\hstep\object{Q}\step[1.5]\object{X}\step\object{Q}
\end{tangle}
\]
In the last step we have used $p\bullet p=p$. That the result coincides with the left hand
side follows now from a standard computation using the properties of a Frobenius algebra.
\qed

\bprop Every object of $\2B$ is isomorphic to one of the form
$(\oj(Z\boxtimes\11)J, q)$ where $q\in\End_\2B(\oj(Z\boxtimes\11)J)$ satisfies (\ref{qq})
(with $Y=Z\boxtimes\11$).
\eprop
\prf By the preceding lemma every object $(\oj(X\boxtimes Y^\op)J,p)$ of $\2B$ is
isomorphic to one which satisfies (\ref{qq}), which allows us to assume this property in
the rest of the proof. By Corollary \ref{cor} there is $Z\in\2C$ such that 
$\oj(X\boxtimes Y^\op)J\cong\oj(Z\boxtimes\11)J$. Let
$e: \oj(X\boxtimes Y^\op)J\rarr\oj(Z\boxtimes\11)J$, 
$f: \oj(Z\boxtimes\11)J\rarr\oj(X\boxtimes Y^\op)J$ be a pair of mutually inverse
isomorphisms. Then with $q=e\bullet p\bullet f$ we have
$(\oj(Z\boxtimes\11)J, q)\cong(\oj(X\boxtimes Y^\op)J, p)$. If we can show that 
also $q$ satisfies (\ref{qq}) Lemma \ref{uulemma} applies and the claim follows.
Now by Corollary  \ref{cor} $Z, e, f$ can be chosen such that $e=v\otimes\tilde{e},
f=v\otimes\tilde{f}$, where $\tilde{e}, \tilde{f}$ are mutually inverse 2-morphisms
between $(X\otimes Y)J$ and $(Z\otimes\11)J$. Therefore, 
\[ q=e\bullet p\bullet f =\quad
\begin{tangle}
\step\object{Q}\Step\object{Z}\\
\hh\step\id\Step\id\\
\sw1\id\se1\step\id\\
\hh\id\step\id\step\frabox{e}\\
\hh\id\step\id\step\id\mmobj{X}\step\id\\
\hh\id\step\frabox{p}\step\id\\
\hh\id\step\id\mmobj{X}\step\id\step\id\\
\hh\frabox{f}\step\id\step\id\\
\id\step\nw1\id\ne1\\
\hh\id\Step\id\\
\object{Z}\Step\object{Q}
\end{tangle}
\quad=\quad
\begin{tangle}
\step\object{Q}\Step\object{Z}\\
\hh\step\id\Step\id\\
\hh\step\id\step\frabox{\tilde{e}}\\
\hh\step\id\step\id\mmobj{X}\step\id\\
\hh\step\frabox{p}\step\id\\
\hh\step\id\mmobj{X}\step\id\step\id\\
\hh\frabox{\tilde{f}}\step\id\step\id\\
\id\step\nw1\id\ne1\\
\hh\id\Step\id\\
\object{Z}\Step\object{Q}
\end{tangle}
\]
where the four-fold vertices denote triple (co)products.
That $q$ satisfies (\ref{qq}) is now obvious from the respective property of $p$ and 
$\tilde{f}\bullet\tilde{e}=\id$.
\qed

\bprop \label{prop-ess}
The preceding proposition remains true if one adds the requirement that
$q[0]=\lambda^{-1}\id_Z$ (notation of Lemma \ref{11mor}).
\eprop
\prf Let $Z, q$ be as in the preceding proposition. Multiplying (\ref{qq}) with 
$v'\otimes v'\otimes\id_{Z\boxtimes\11}$ and using 
$v'\otimes\id_{Z\boxtimes\11}\circ q=q[0]\otimes v$ we obtain 
$\lambda q[0]^2=q[0]\in\End_\2C(Z)$. 
Let $f: \tilde{Z}\rarr Z,\, g: Z\rarr\tilde{Z}$ be a splitting of the idempotent
$\lambda q[0]$. Then it is easy to verify that with 
\[ \tilde{q}=\id_Q\otimes (g\boxtimes\id_\11) \mcirc q\mcirc (f\boxtimes\id_\11)\otimes\id_Q \]
we have $(\oj(\tilde{Z}\boxtimes\11)J, \tilde{q})\cong(\oj(Z\boxtimes\11)J, q)$. This
$\tilde{q}$ still verifies (\ref{qq}) and, in addition,
$\tilde{q}[0]=\lambda^{-1}\id_{\tilde{Z}}$.
\qed

Now we are ready to state our first main result.

\btheor The tensor categories $\2B$ and $\2Z_1(\2C)$ are equivalent as spherical categories,
thus we have the weak monoidal Morita equivalence (in the sense of \cite{mue09})
$\2Z_1(\2C)\approx\2C\boxtimes\2C^\op$. In particular,
\[ \dim\2Z_1(\2C)=(\dim\2C)^2. \]
\etheor
\prf We have shown that every simple object in $\2B$ isomorphic to the image under $F$ of
a simple object in $\2Z_1(\2C)$. Since $\2Z_1(\2C)$ and $\2B$ are both semisimple (in
particular closed under direct sums and subobjects) we conclude that $F$ is essentially
surjective. Since $F$ is also fully faithful we have an equivalence of categories by
\cite[Theorem IV.4.1]{cwm}. $F$ being monoidal we have an equivalence of monoidal categories
by \cite[I.4.4]{sr}. (This already implies that $\2B$ and $\2Z_1(\2C)$ have the same
dimension, since by \cite[Proposition 2.4]{mue09} the latter are well-defined independently of
the chosen spherical or $*$-structure and, of course, invariant under monoidal equivalence.)

It remains to show that the spherical structures are compatible. As to the conjugation
maps, we have
\bean \ol{F(X,e_X)} &=& \ol{(\oj(X\boxtimes\11)J,p_{e_X})}=(\oj(\ol{X}\boxtimes\11)J,\ol{p_{e_X}}), \\
   F(\ol{(X,e_X)}) &=& F((\ol{X},e_{\ol{X}}))=(\oj(\ol{X}\boxtimes\11)J, p_{e_{\ol{X}}}). \eean
Putting together Proposition \ref{hb-conj} and Lemma \ref{iii-iv}, $e_{\ol{X}}(X_i)$ is as in
Fig.\ \ref{fig1}, where the pair of unlabeled morphisms is any solution of the duality
equations. 
\begin{figure}
\[ e_{\ol{X}}(X_i)=\quad
\begin{tangle}
\step[1.5]\object{\ol{\ve}(\ol{X})}\step[2.5]\object{X_i}\step\object{\ol{X}}\\
\mcoev\step\id\step\id\\
\hh\id\step\hcoev\step\id\step\id\step\id\\
\hh\id\step\id\step\frabox{e_X(X_{\ol{\imath}})}\step\id\step\id\\
\hh\id\step\id\step\id\step\hev\step\id\\
\id\step\id\step\mev\\
\object{\ol{X}}\step\object{X_i}\step[2.5]\object{\ve(X)}
\end{tangle}
\quad\quad\quad\quad
\ol{p_{e_X}}=\quad
\begin{tangle}
\step[1.5]\object{\ol{\ve}(\ol{X}\boxtimes\11)}\step[2.5]\object{Q}\step[1.5]\object{\ol{X}\boxtimes\11}\\
\mcoev\step\id\step\id\\
\hh\id\step[.8]\mobj{r'}\step[.2]\hcoev\step\id\step\id\step\id\\
\hh\id\step\id\step\frabox{p_{e_X}}\step\id\step\id\\
\hh\id\step\id\step\id\step\hev\mobj{r}\step\id\\
\id\step\id\step\mev\\
\step[-.5]\object{\ol{X}\boxtimes\11}\step[1.5]\object{Q}\step[2.5]\object{\ve(X\boxtimes\11)}
\end{tangle}
\]
\caption{$e_{\ol{X}}(X_i)$ and $\ol{p_{e_X}}$}
\label{fig1}
\end{figure}
In view of the definition of $p_X$ in Proposition \ref{funcf} and of $\ol{p_{e_X}}$ in
\cite[Theorem 5.14]{mue09}, cf.\ Fig.\ \ref{fig1}, it is clear that
$\ol{p_{e_X}}=p_{e_{\ol{X}}}$ and therefore 
\[ \ol{F(X,e_X)}=F(\ol{(X,e_X)}). \]

Now by Proposition \ref{hb-conj}, the spherical structure of $\2Z_1(\2C)$ is inherited from 
$\2C$, concretely $\ve_{\2Z_1(\2C)}(X,e_X)=\ve_\2C(X)$. Considering how the spherical
structures of $\2E_0$ and $\2E$ arise from that of $\2A$ in \cite[Theorem 5.13]{mue09} it
is essentially obvious that $F: \2Z_1(\2C)\rarr\2B$ is an equivalence of spherical
categories irrespective of the fact that the latter is neither strict monoidal nor strict
spherical. We omit the easy details.
\qed

\brem 1. In the case where $\2C$ is the representation category of a finite dimensional
involutive semisimple and cosemisimple Hopf algebra $H$, $\2Z_1(\2C)$ is equivalent
\cite[Theorem XIII.5.1]{ka} to the representation category of the quantum double $D(H)$
and our result is just the fact $\dim D(H)=(\dim H)^2$.

2. It seems likely that a simpler proof of the theorem can be given using the
interpretation of the tensor category $\2B=\END_\2E(\6B)$ as bimodule category
$Q-\mbox{Mod}-Q$, together with the recent work \cite{ostr}.
\erem
