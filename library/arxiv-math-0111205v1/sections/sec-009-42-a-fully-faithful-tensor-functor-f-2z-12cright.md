---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-009-42-a-fully-faithful-tensor-functor-f-2z-12cright
section_title: "A fully faithful tensor functor $F: \2Z_1(\2C)\rightarrow\2B$"
section_number: 4.2
pages: 18-25
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.894
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{fff}
In this subsection we will construct a functor $F: \2Z_1(\2C)\rightarrow\2B$ and prove
that it is fully faithful and monoidal. This already implies that $\2Z_1(\2C)$ has finitely 
many isomorphism classes of simple objects, which is not at all obvious from
Definition \ref{defdouble}.

\blemma \label{11mor}
Let $X,Y\in\2C$. There is a one-to-one correspondence between morphisms 
$u\in \Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))\equiv\Hom_\2E(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$
and families $\{ u[i]\in\Hom_\2C(XX_i,X_iY),\ i\in \Gamma\}$. With $Z\in\2C$ and 
$v\in \Hom_\2A((Y\boxtimes\11)Q,Q(Z\boxtimes\11))\equiv\Hom_\2E(\oj (Y\boxtimes\11)J,\oj (Z\boxtimes\11)J)$ we have
\begin{equation}(v\bullet u)[k]= (d_k\,\lambda)^{-1} \sum_{i,j\in \Gamma}
   \sum_{\alpha=1}^{N_{ij}^k} d_i d_j \  
\begin{tangle}
\step[1.5]\hstep\object{X_k}\step[1.5]\object{Z}\\
\hh\mobj{{t'}_{ij}^{k\alpha}}\step[1.5]\hcd\step\id\\
\hh\step[1.5]\id\mobj{X_i}\step\id\mobj{X_j}\step\id\\
\hh\step[1.5]\id\step\frabox{v[j]} \\
\hh\step[1.5]\id\step\id\obj{Y}\step\id\\
\hh\step[1.5]\frabox{u[i]}\step\id \\
\hh\step[1.5]\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hh\step[1.5]\id\step\hcu\obj{t_{ij}^{k\alpha}}\\
\step[1.5]\object{X}\step[1.5]\object{X_k}
\end{tangle}
\label{mul}\end{equation}
\elemma
\prf Let $u\in \Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))$. Then
\[ v'_j\otimes\id_{Y\boxtimes\11}\mcirc u\mcirc \id_{X\boxtimes\11} \otimes v_i \]
is in
\[\Hom_\2A((X\boxtimes\11)\hat{X}_i,\hat{X}_j(Y\boxtimes\11)) 
  =\Hom_\2C(X X_i, X_jY)\otimes_\7F \Hom_{\2C^\op}(X^\op_i, X^\op_j), \]
which vanishes if $i\ne j$. Thus 
\[ v'_i\otimes\id_{Y\boxtimes\11} \mcirc u\mcirc \id_{X\boxtimes\11}
  \otimes v_i= u[i]\boxtimes\id_{X^\op_i} \]
defines $u[i]\in\Hom_\2C(X X_i,X_iY)$. Conversely, given
$\{ u[i]\in\Hom_\2C(X X_i,X_iY), i\in \Gamma\}$, 
\begin{equation}u=\sum_i v_i\otimes\id_{Y\boxtimes\11} \mcirc
   u[i]\boxtimes\id_{X^\op_i} \mcirc\id_{X\boxtimes\11} \otimes v'_i 
\label{U-ve}\end{equation}
defines a morphism $u\in\Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))$. 

Eq. (\ref{mul}) follows easily from (\ref{U-ve}), the definition 
\cite[Proposition 3.8]{mue09} of the $\bullet$-multiplication in $\2E$ and the formula
(\ref{defW}) for $w, w'$.
\qed

\blemma \label{uulemma}
Let $u\in\End_\2B(J(X\boxtimes\11)\oj)$. Then the associated family $\{ u[i]\}$ satisfies 
the braiding fusion equation 
\be
\begin{tangle}
\object{X_i}\step\object{X_j}\step\object{X}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{u[j]}\\
\hh\id\step\id\obj{X}\step\id\\
\hh\frabox{u[i]}\step\id\\
\hh\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hh\id\step\frabox{t}\\
\hh\id\step[1.5]\id\\
\object{X}\step[1.5]\object{X_k}
\end{tangle} \ \ = \ \ \ \
\begin{tangle}
\object{X_i}\step\object{X_j}\step\object{X}\\
\hh\id\step\id\step\id\\
\hh\frabox{t}\step\id\\
\hh\step\id\obj{X_k}\step\id\\
\hh\step\frabox{u[k]}\\
\hh\step\id\step\id\\
\hh\step\object{X}\step\object{X_k}
\end{tangle}
\label{bfe}\end{equation}
for all $i,j,k\in \Gamma$ and all $t\in\Hom_\2C(X_k,X_iX_j)$ iff $u$ satisfies
\be
\begin{tangle}
\object{Q}\step\object{Q}\Step\object{X\boxtimes\11}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{u}\\
\hh\id\step\id\step\id\\
\hh\frabox{u}\step\id\\
\hh\id\step\hcu\obj{w}\\
\hh\id\step[1.5]\id\\
\step[-.5]\object{X\boxtimes\11}\Step\object{Q}
\end{tangle} \ \ = \ \ \
\begin{tangle}
\object{Q}\step\object{Q}\step[1.7]\object{X\boxtimes\11}\\
\hh\id\step\id\hstep\id\\
\hh\step[-.3]\obj{w}\step[.3]\hcu\hstep\id\\
\hh\hstep\id\step\id\\
\hh\hstep\frabox{u}\\
\hh\hstep\id\step\id\\
\hh\hstep\id\step\mobj{Q}\\
\hstep\object{X\boxtimes\11}
\end{tangle}
\label{uu2}\end{equation}
\elemma
\prf In view of the definition (\ref{defW}) of $w\in\Hom_\2A(Q,Q^2)$ and of 
(\ref{U-ve}), the left hand side of (\ref{uu2}) is seen to equal
\begin{multline*}
 \lambda^{-1/2} \sum_{i,j,k}\sqrt{\frac{d_id_j}{d_k}} v_i\otimes
  v_j\otimes\id_{X\boxtimes\11} 
   \mcirc \id_{\hat{X}_i}\otimes u[j]\boxtimes\id_{X^\op_j}\mcirc
    u[i]\boxtimes\id_{X^\op_i}\otimes\id_{\hat{X}_j} \\
 \mcirc\id_{X\boxtimes\11}\otimes\hat{t}^k_{ij}\mcirc
  \id_{X\boxtimes\11}\otimes v'_k, 
\end{multline*}
whereas the right hand side equals
\[ \lambda^{-1/2}\sum_{i,j,k}\sqrt{\frac{d_id_j}{d_k}} v_i\otimes
   v_j\otimes\id_{X\boxtimes \11}\mcirc \hat{t}^k_{ij}\otimes\id_{X\boxtimes\11}\mcirc 
   u[k]\boxtimes \id_{X^\op_k}\mcirc\id_{X\boxtimes\11}\otimes
   v'_k. \]
In view of the orthogonality relation satisfied by the $v's$, these two expressions
are equal iff
\begin{multline*} \lefteqn{\id_{\hat{X}_i}\otimes u[j]\boxtimes\id_{X^\op_j}\mcirc
    u[i]\boxtimes\id_{X^\op_i}\otimes\id_{\hat{X}_i}\mcirc
   \id_{X\boxtimes\11}\otimes\hat{t}^k_{ij}} \\
   =\hat{t}^k_{ij}\otimes\id_{X\boxtimes\11}\mcirc u[k]\boxtimes
   \id_{X^\op_k} \quad\quad\forall i,j,k\in \Gamma. 
\end{multline*}
Inserting 
$\hat{t}^k_{ij}=\sum_\alpha t^{k\alpha}_{ij}\boxtimes {t'}^{k\alpha}_{ij}$,
this becomes 
\bea \sum_{\alpha=1}^{N_{ij}^k} \left( \id_{X_i}\otimes u[j]\mcirc
   u[i]\otimes\id_{X_j}\mcirc \id_X\otimes t_{ij}^{k\alpha}\right)
  &\boxtimes& {t'}^{k\alpha}_{ij} \nn\\ = \ \ 
  \sum_{\alpha=1}^{N_{ij}^k} \left( t_{ij}^{k\alpha}\otimes\id_X\mcirc u[k] \right) 
  &\boxtimes& {t'}^{k\alpha}_{ij}. \label{cond1}\eea
Multiplying from the right with 
$\id_{XX_k}\boxtimes {t}^{k\alpha}_{ij}$, we arrive at the condition
(\ref{bfe}). Conversely, $\boxtimes$-tensoring (\ref{bfe}) with 
${t'}^{k\alpha}_{ij}$ and summing over $\alpha$ we obtain (\ref{cond1}). 
\qed


\bprop \label{funcf}
There is a faithful functor $F: \2Z_1(\2C)\rightarrow\2B$.
\eprop
\prf Let $(X,e_X)\in\2Z_1(\2C)$. By Lemma \ref{11mor} the half braiding 
$\{ e_X(Z), Z\in\2C\}$ provides us with an element $p^0_X$ in 
$\End_\2B(\oj (X\boxtimes\11)J)\equiv\Hom_\2A((X\boxtimes\11)Q,Q(X\boxtimes\11))$.
Since $e_X(\cdot)$ satisfies the braiding fusion relation (\ref{bfe}), $p^0_X$ 
satisfies (\ref{uu2}). Now, multiplying (\ref{uu2}) from the left with 
$w'\otimes\id_{X\boxtimes\11}$ and using (\ref{W4}) we obtain 
\begin{equation}w'\otimes\id_{X\boxtimes\11}\mcirc\id_Q\otimes p^0_X\mcirc p^0_X\otimes 
  \id_Q\mcirc\id_{X\boxtimes\11}\otimes w = \lambda p^0_X, \label{idemp}\end{equation}
which is just $p^0_X\bullet p^0_X=\lambda p^0_X$ in $\End_\2E(\oj (X\boxtimes\11)J)$. 
Thus with $p_X=\lambda^{-1}p^0_X$, 
\begin{equation}F((X,e_X)):=(\oj (X\boxtimes\11)J, p_X) \label{deff}\end{equation}
is an object in $\2B$, which defines the functor $F$ on the objects. We will mostly write
$F(X,e_X)$ instead of $F((X,e_X))$. Let $(X,e_X)\in\2Z_1(\2C)$ with the above idempotent 
$p_X\in\Hom_\2A((X\otimes\11)Q,Q(X\otimes\11))\equiv\End_\2E(\oj (X\boxtimes\11)J)$
and similarly $(Y,e_Y),\ p_Y$. Consider now
$s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))\subset\Hom_\2C(X,Y)$. Then condition (\ref{dmor}) 
implies 
\begin{equation}\id_Q\otimes (s\boxtimes\id_{\11}) \circ p_X =
    p_Y \circ (s\boxtimes\id_{\11})\otimes\id_Q. \label{emor}\end{equation}
The element of $u\in\Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))\equiv\Hom_\2E(\oj
(X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$ defined by (\ref{emor}) clearly satisfies
$p_Y\bullet u\bullet p_X=u$ and is therefore a morphism in 
$\Hom_\2E((\oj (X\boxtimes\11)J,p_X),(\oj (Y\boxtimes\11)J,p_Y)$. That the map 
$s\mapsto u$ is faithful follows from the first term in (\ref{emor}) and the fact that the
$e_X(X_i),\ i\in \Gamma$, and thus $p_X$ (as a morphism in $\2A$) are invertible. This
defines $F$ on the morphisms, and $F$ is faithful. The simple argument proving that $F$
respects the composition of morphisms is left to the reader. 
\qed


\bprop The functor $F$ is full. \label{fullf}\eprop
\prf We must show that every morphism in $\Hom_\2B(F(X,e_X),F(Y,e_Y))$, where
$(X,e_X),$ $(Y,e_Y)\in\2Z_1(\2C)$, is of the form $F(s)$ with 
$s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))$.
Now, the morphisms in $\Hom_\2B((\oj (X\boxtimes\11)J,p_X),(\oj (Y\boxtimes\11)J,p_Y))$
are those elements $s$ in $\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$ which
satisfy $s=p_Y\bullet s\bullet p_X$. $p_X, p_Y$ being idempotents, every such $s$
obviously is of the form $s=p_Y\bullet t\bullet p_X$ for some
$t\in\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$. By definition of $\2B$ and
by Lemma \ref{11mor}, $s$ and $t$ are represented by elements $\{s[i]\},\ \{t[i]\}$ of
$\bigoplus_{i\in \Gamma} \Hom_\2C(XX_i,X_iY)$.  Given arbitrary $t$ and setting 
$s=p_Y\bullet t\bullet p_X$ we will show that 
$s[0]\in\Hom_\2C(X,Y)$ is in fact in $\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))$ and that
\[ s[m]= \id_{X_m}\otimes s[0] \mcirc e_X(X_m) \quad\forall m\in \Gamma, \]
which is equivalent to 
\[ s= \id_Q\otimes (s[0]\boxtimes\id_{\11}) \circ p_X = F(s[0]).
\]
Starting from the explicit statement of $s=p_Y\bullet t\bullet p_X$ we compute:
\[ d_m\lambda^4\cdot s[m]=\sum_{i,j,k,l\in \Gamma}\sum_{\alpha,\beta} d_id_jd_k \ \ 
\begin{tangle}
\hstep\object{X_m}\step[2.5]\object{Y}\\
\hh\step[-1]\mobj{{t'}_{kl}^{m\alpha}}\step\hcd\Step\id\\
\id\step\hdcd\step\id\\
\id\step\id\step\hxx\\
\hh\id\step\frabox{t[i]}\step\id \\
\hh\step[-1]\mobj{X_k}\step\id\step\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hxx\step\hddcu\step[-0.5]\mobj{X_l}\\
\hh\id\step\hcu\obj{t_{kl}^{m\alpha}}\\
\object{X}\step[1.5]\object{X_m}
\end{tangle}
\]
\[ =  \sum_{{i,j,k,l\in \Gamma}\atop{\alpha,\beta}} d_id_jd_k\frac{d_m}{d_k}\frac{d_l}{d_j}
\quad\quad
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\Step\mobj{X_l}\step\id\\
\hh\id\step\id\step\hcoev\step\id\step\id\\
\id\step\id\step\id\step\hcu\step[-.4]\mobj{s_{\ol{\imath}l}^{j\beta}}\step[.9]\ddh\\
\id\step\id\step\id\mobj{X_i}\step[1.5]\hxx\\
\step[-.7]\mobj{s_{m\ol{l}}^{k\alpha}}\step[.7]\hcu\step\id\hstep\hdd\step\id\\
\hh\hstep\id\step[1.5]\frabox{t[i]}\step[1.5]\id\mobj{X_j} \\
\step[-.3]\mobj{X_k}\step[.3]\dh\step\id\step\id\mobj{X_i}\step\hcd\mobj{{s'}_{\ol{\imath}l}^{j\beta}}\\
\step\hxx\step\hev\step[-1.2]\mobj{\ve(X_i)}\step[2.2]\id\mobj{X_l}\\
\step\id\step\hdcd\mobj{{s'}_{m\ol{l}}^{k\alpha}}\Step\id\\
\step\id\step\id\step\ev\mobj{\ve(\ol{X_l})}\\
\step\object{X}\step\object{X_m}
\end{tangle} 
= \ \sum_{{i,j,k,l\in \Gamma}\atop{\alpha,\beta}} d_id_md_l \quad\quad
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\step[3]\id\\
\id\step\id\step\hcoev\step\hxx\\
\id\step\id\step\id\step\hxx\step\id\mobj{X_l}\\
\hh\step[-1.2]\mmobj{s_{m\ol{l}}^{k\alpha}}\step[1.2]\hcu\step\id\step\id\step\hcu\mmobj{s_{\ol{\imath}l}^{j\beta}}\\
\hh\step[-0.5]\mobj{X_k}\step\id\step[1.5]\frabox{t[i]}\step[1.5]\id\mobj{X_j} \\
\hh\step[-1.2]\mmobj{{s'}_{m\ol{l}}^{k\alpha}}\step[1.2]\hcd\step\id\step\id\mobj{X_i}\step\hcd\mmobj{{s'}_{\ol{\imath}l}^{j\beta}}\\
\id\step\hxx\step\hev\step\id\mobj{X_l}\\
\hxx\step\Ev\step[1.5]\mobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_m}
\end{tangle}
\]
\[ = d_m \sum_{i,l\in \Gamma} d_id_l \ 
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\step[3]\id\\
\id\step\id\step\hcoev\step\hxx\\
\id\step\id\step\id\step\hxx\step\id\\
\hh\id\step\id\step\frabox{t[i]}\step\id\step\id\mobj{X_l} \\
\hh\id\step\id\step\id\step\id\mobj{X_i}\step\id\step\id\\
\id\step\hxx\step\hev\step[-1]\mobj{\ve(X_i)}\Step\id\\
\hxx\step\Ev\step[1.5]\mobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_m}
\end{tangle}
\quad = \ \ d_m  \ \ 
\begin{tangle}
\object{X_m}\Step\object{Y}\\
\id\Step\id\\
\hh\id\step[1.5]\frabox{E_{X,Y}(u)}\\
\xx\\
\hh\id\Step\id\\
\object{X}\Step\object{X_m}
\end{tangle}
\]
where $u\in\Hom_\2C(X,Y)$ does not depend on $m$. (On the very left, $p_X, p_Y$ and each
of the $\bullet$-operations contribute one factor $\lambda$. Furthermore,
$s_{m\ol{l}}^{k\alpha}, \alpha=1,\ldots,N_{m\ol{l}}^k$ is a basis in 
$\Hom(X_k,X_m\ol{X_l})$ with dual basis $s'$. We do not use $t_{m\ol{l}}^{k\alpha}$ since
we cannot assume $\ol{X_l}=X_{\ol{l}}$ without losing generality.)
For $m=0$ we have $X_m=\11$ and thus
$s[0]=\lambda^{-4}E_{X,Y}(u)$, thus $s[0]\in\Hom_{\2Z_1(\2C)}((X,e_X), (Y,e_Y))$.
Plugging this into the above equation for $m\ne 0$ we obtain
$s[m]=\id_{X_m}\otimes s[0]\mcirc e_X(X_m)$ and therefore $s=F(\lambda s[0])$. 
We conclude that the functor $F$ is full. \qed

\bprop The functor $F$ is strong monoidal. \eprop
\prf First we observe that $F(\11_{\2Z_1(\2C)})=F(\11_\2C,\id_X)=(\oj J,\lambda^{-1}\id_Q)$,
which follows from (\ref{deff}) by putting $X=\11$ and $e_X(X_i)=\id_{X_i}\ \forall i$.
Comparing with \cite[Theorem 3.12]{mue09} we see $F(\11_{\2Z_1(\2C)})=\11_\6B$.

Now we have to show that $F(X,e_X)F(Y,e_Y)$ and $F((X,e_X)(Y,e_Y))$ are naturally
isomorphic. We compute 
\bean F(X,e_X)F(Y,e_Y) &=& (\oj (X\boxtimes\11)J,p_X)(\oj (Y\boxtimes\11)J,p_Y) \\
   &=&    (\oj (X\boxtimes\11)Q(Y\boxtimes\11)J,u_1(X,Y)), \\
   F((X,e_X)(Y,e_Y)) &=& F(XY,e_{XY}) = (\oj (XY\boxtimes\11)J,u_2(X,Y)), \eean
where
\[ u_1(X,Y) = \ \ 
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \quad\quad\quad\quad\quad
u_2(X,Y) = \lambda \quad
\begin{tangle} 
\step[1.2]\object{X\boxtimes\11}\\
\hh\obj{Q}\step\id\Step\object{Y\boxtimes\11}\\
\hh\id\step\id\step\id\\
\hh\frabox{p_X}\step\id\\
\hh\id\step\id\mobj{Q}\step\id\\
\hh\id\step\frabox{p_Y}\\
\hh\id\step\id\step\id\\
\hh\step[-0.3]\object{X\boxtimes\11}\step[1.3]\id\step\obj{Q}\\
\step[1.2]\object{Y\boxtimes\11}
\end{tangle}
\]
Obviously, $F$ is not strict. But with 
$s(X,Y)\in\Hom_\2E((X\boxtimes\11)(Y\boxtimes\11), (X\boxtimes\11)Q(Y\boxtimes\11))$ and
$t(X,Y)\in\Hom_\2E((X\boxtimes\11)Q(Y\boxtimes\11),(X\boxtimes\11)(Y\boxtimes\11))$
defined by 
\[ s(X,Y)= \quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\id\step[1.5]\counit\step[1.5]\id\step\id\\
\hh\id\step[3]\id\step\mobj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \quad\quad\quad\quad\quad
 t(X,Y)= \lambda\quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\obj{Q}\step\id\step[1.5]\unit\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle}
\]
we compute
\[ t(X,Y)\bullet s(X,Y)= \lambda\quad
\begin{tangle}
\hstep\object{Q}\step[1.7]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hcd\step\id\step[1.5]\unit\step[1.5]\id\\
\hh\id\step\id\step\id\step\hcd\step\id\\
\hh\id\step\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\id\step\hcu\step\id\step\id\\
\hh\id\step\id\step\hcd\step\id\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step\id\step\id\step\id\\
\id\step[1.5]\counit\step[1.5]\id\step\hcu\\
\step[.2]\object{X\boxtimes\11}\step[2.7]\object{Y\boxtimes\11}\step[1.5]\object{Q}
\end{tangle} \ \ = \lambda\quad
\begin{tangle}
\hstep\object{Q}\step[1.7]\object{X\boxtimes\11}\step[5]\object{Y\boxtimes\11}\\
\hstep\id\step[1.5]\id\step[1.5]\coev\step[1.5]\id\\
\hh\hcd\step\id\step[1.5]\id\step[1.5]\hcd\step\id\\
\hh\id\step\frabox{p_X}\step[1.5]\id\step[1.5]\id\step\frabox{p_Y}\\
\hh\id\step\id\step\id\step[1.5]\id\step[1.5]\id\step\id\step\id\\
\hh\frabox{p_X}\step\id\step[1.5]\id\step[1.5]\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step[1.5]\id\step[1.5]\id\step\hcu\\
\id\step[1.5]\ev\step[1.5]\id\step[1.5]\id\\
\step[.2]\object{X\boxtimes\11}\step[5]\object{Y\boxtimes\11}\step[1.5]\object{Q}
\end{tangle}
\]
Here the second equality follows (verify!) by repeated use of the equations
(\ref{W1}-\ref{W3}). Using $p_X\bullet p_X=p_X, p_Y\bullet p_Y=p_Y$ and the duality
equation for $Q$ we obtain $t(X,Y)\bullet s(X,Y)=u_2(X,Y)$. Now,
\[ s(X,Y)\bullet t(X,Y)= \lambda\quad
\begin{tangle}
\step\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\hstep\obj{Q}\step[1.5]\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\hcd\step\id\step\hcd\step\id\\
\hh\id\step\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\id\step\hcu\step\id\step\id\\
\id\step\id\step[1.5]\counit\step[1.5]\id\step\id\\
\id\step\id\step[1.5]\unit\step[1.5]\id\step\id\\
\hh\id\step\id\step\hcd\step\id\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step\id\step\hcu\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step[1.5]\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \ \ = \lambda^{-1}\quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\Step\obj{Q}\step\id\\
\hh\id\step\id\Step\id\step\id \\
\hh\frabox{p_X}\Step\id\step\id\\
\hh\id\hstep\hcd\step\hcd\hstep\id\\
\hh\id\hstep\id\step\hev\step\id\hstep\id\\
\hh\id\hstep\id\step\hcoev\step\id\hstep\id\\
\hh\id\hstep\id\step\id\step\hcu\hstep\id\\
\hh\id\hstep\id\step\id\step[1.5]\frabox{p_Y}\\
\hh\id\hstep\hcu\step[1.5]\id\step\id\\
\hh\id\step\mobj{Q}\Step\id\step\mobj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle}
\]
Here we used that $p_X, p_Y$ come from half-braidings, implying that we have (\ref{uu2})
and its dual version by Lemma \ref{uulemma}. (Take into account two factors of $\lambda$
which come from the normalization of $p_{X/Y}$.) It is easy to see that the last
expression equals $u_1(X,Y)$. 

It remains to verify that the functor $F$ is coherent in the sense of
\cite[XI.2]{cwm}. The computations present no difficulties and are simplified by the fact
that the categories $\2Z_1(\2C)$ and $\2B$ are strict except for the unit in
$\2B=\End_\2E(\6B)$. We refrain from spelling out the details. \qed
