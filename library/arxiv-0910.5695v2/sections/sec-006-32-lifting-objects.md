---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-006-32-lifting-objects
section_title: "Lifting objects"
section_number: 3.2
pages: 15-21
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.912
---
Let $K$ denote the field of fractions of $F[[T-t]]$ where $T$ is an indeterminate. In this section we use the process of lifting idempotents (see appendix \ref{liftingappendix}) to lift objects in $\uRep(S_t; F)$ to objects in $\uRep(S_T; K)$.  
We then prove some useful properties of these lifted objects.  In the next section we will show that $\uRep(S_T; K)$ is semisimple (see Corollary \ref{ssT}), and hence uncomplicated from our point of view.  The process of  lifting objects developed in this section will be used later in the paper to compare the structure of $\uRep(S_t; F)$ with that of the semisimple category $\uRep(S_T; K)$.  
The following theorem will be used to define the notion of lifting objects.

\begin{theorem}\label{lifttoK} Suppose $e$ is an idempotent in $FP_n(t)$.  Then there exists an idempotent $\ep\in KP_n(T)$ of the form $\ep=\sum_{\pi\in P_{n,n}}a_\pi\pi$ with $a_\pi\in F[[T-t]]$ for all $\pi\in P_{n,n}$ such that $\ep|_{T=t}=e$ (we say $\ep$ is a lift of $e$).  Moreover, if $([n_1], e_1)$ and $([n_2], e_2)$ are isomorphic objects in $\uRep(S_t; F)$ and $\ep_1, \ep_2$ are lifts of $e_1, e_2$ respectively, then $([n_1], \ep_1)$ and $([n_2], \ep_2)$ are isomorphic in $\uRep(S_T; K)$.  
\end{theorem}

\begin{proof} The existence of a lift of $e$ is guaranteed by the first statement of Theorem \ref{appenlift}.  Now suppose $([n_1], e_1)\cong([n_2], e_2)$ in $\uRep(S_t; F)$.  To prove the remainder of the theorem we may assume $n_1\leq n_2$.  If $n_1=0$ the theorem is easy to check, so assume $n_1>0$.  Set $$\phi:=\left\{\begin{array}{ll}\id_{n_1} & \text{if }n_1=n_2 \\
\phi_{n_2}\cdots\phi_{n_1+1} & \text{if }n_1<n_2
\end{array}\right.\quad\text{and}\quad \phi':=\left\{\begin{array}{ll}\id_{n_1} & \text{if }n_1=n_2 \\
\phi'_{n_1+1}\cdots\phi'_{n_2} & \text{if }n_1<n_2
\end{array}\right.$$ where $\phi_{n}$ and $\phi'_{n}$ are as in the proof of Lemma \ref{classifylemma}.  Then $([n_1], e_1)\cong([n_2], \phi e_1\phi')$ and $\phi\ep_1\phi'$ is a lift of $\phi e_1\phi'$.  Hence it suffices to show the theorem is true when $n_1=n_2$.  
In this case the remainder of the theorem follows from the second statement of Theorem \ref{appenlift} along with Proposition \ref{proprep}(2).  
\end{proof}

Lifted idempotents satisfy the following property.

\begin{proposition}\label{liftsums} If $([n], e)\cong ([n_1], e_1)\oplus([n_2], e_2)$ in $\uRep(S_t; F)$ and $\ep, \ep_1, \ep_2$ are lifts of $e, e_1, e_2$ respectively, then $([n], \ep)\cong([n_1], \ep_1)\oplus([n_2], \ep_2)$ in $\uRep(S_T; K)$.
\end{proposition}

\begin{proof} By the Krull-Schmidt property there exist $\bar{e}_1, \bar{e}_2\in FP_n(t)$ with the property $([n_i] , e_i)\cong ([n], \bar{e}_i)$ for $i=1,2$ such that $e=\bar{e}_1+\bar{e}_2$ is an orthogonal decomposition of the idempotent $e$.  Let $\bar{\ep}_1, \bar{\ep}_2\in KP_n(T)$ be lifts of $\bar{e}_1, \bar{e}_2$ respectively.  Then  $\bar{\ep}_1+\bar{\ep}_2$ is a lift of $e$.  Hence, by Theorem \ref{appenlift} and Proposition \ref{proprep}(2) $([n], \ep)\cong([n], \bar{\ep}_1+\bar{\ep}_2)$ in $\uRep(S_T; K)$.  Since $\bar{\ep}_1$ and $\bar{\ep}_2$ are orthogonal idempotents (see Theorem \ref{appenlift}) we have $([n], \bar{\ep}_1+\bar{\ep}_2)\cong([n], \bar{\ep}_1)\oplus([n], \bar{\ep}_2)$ in $\uRep(S_T; K)$.  The result now follows from the last statement of Theorem \ref{lifttoK}.
\end{proof}

By Proposition \ref{proprep}(2) any object in $\uRep(S_t; F)$ is a finite direct sum of objects of the form $([n], e)$.  Hence, setting $\Lift_t([n], e):=([n], \ep)$, where $\ep\in KP_n(T)$ is a lift of $e\in FP_n(t)$ and extending to all objects in $\uRep(S_t; F)$ by requiring $\Lift_t(A\oplus B)=\Lift_t(A)\oplus \Lift_t(B)$ gives the operation

$$\Lift_t:\left\{\begin{tabular}{c}
objects in $\uRep(S_t; F)$\\
up to isomorphism
\end{tabular}
\right\}\longrightarrow\left\{\begin{tabular}{c}
objects in $\uRep(S_T; K)$\\
up to isomorphism
\end{tabular}
\right\}$$
Theorem \ref{lifttoK} along with Proposition \ref{liftsums} show that $\Lift_t$ is well defined.   

\begin{example}\label{lift1}  (0) $\Lift_t(L(\varnothing))=\Lift_t(([0], \id_0))=([0], \id_0)=L(\varnothing)$ for all $t\in F$.

(1) Notice $\Lift_t(([1], \id_1))=([1], \id_1)=L(\Box)\oplus L(\varnothing)$ in $\uRep(S_T; K)$ for all $t\in F$.  If $t\not=0$, then $([1], \id_1)=L(\Box)\oplus L(\varnothing)$. Hence (using part (0) and the additivity of $\Lift_t$) we have $\Lift_t(L(\Box))=L(\Box)$ whenever $t\not=0$.  On the other hand, $([1], \id_1)\cong L(\Box)$ in $\uRep(S_0; F)$.  Hence $\Lift_0(L(\Box))=L(\Box)\oplus L(\varnothing)$.
\end{example}

The following proposition lists some useful properties of $\Lift_t$.

\begin{proposition}\label{Liftprop} For this proposition suppose $A$ and $B$ are objects in $\uRep(S_t; F)$.   



(1) $\Lift_t(A\otimes B)=\Lift_t(A)\otimes\Lift_t(B)$ for all $t\in F$.

(2) $(\dim_{\uRep(S_T; K)}\Lift_t(A))|_{T=t}=\dim_{\uRep(S_t; F)}A$ for all $t\in F$.

(3) Suppose $t\in F$ and $\lambda, \lambda^{(1)}, \ldots, \lambda^{(m)}$ are Young diagrams with the property  $\Lift_t(L(\lambda))=L(\lambda^{(1)})\oplus\cdots\oplus L(\lambda^{(m)})$ in $\uRep(S_T; K)$.  Then there exists a unique $j\in\{1,\ldots, m\}$ with $\lambda^{(j)}=\lambda$.  Moreover, $|\lambda^{(i)}|<|\lambda|$ for all $i\not=j$.  In particular, $\Lift_t$ is injective. 

(4) Fix a Young diagram $\lambda$.   $\Lift_t(L(\lambda))=L(\lambda)$ for all but finitely many $t\in F$.

(5) $\dim_K\Hom_{\uRep(S_T; K)}(\Lift_t(A), \Lift_t(B))=\dim_F\Hom_{\uRep(S_t; F)}(A, B)$ for all $t\in F$.

\end{proposition}

\begin{proof}  (1) It suffices to prove the statement when $A$ and $B$ are objects of the form $A=([n], e)$, $B=([n'], e')$.  Suppose $\ep, \ep'$ are lifts of $e, e'$ respectively.  Then $\ep\otimes\ep'$ is a lift of $e\otimes e'$, hence $$\Lift_t(A\otimes B)=\Lift_t([n+n'], e\otimes e')=([n+n'], \ep\otimes\ep')=\Lift_t(A)\otimes\Lift_t(B).$$

(2) Again, we may assume $A$ is of the form $A=([n], e)$. Let  $\ep$ denote a lift of $e$.  Then $\dim_{\uRep(S_T; K)}\Lift_t(A)=\tr(\ep)$, and $\dim_{\uRep(S_t; F)}A=\tr(e)=\tr(\ep)|_{T=t}$.

(3) It is easy to show $\Lift_t(L(\varnothing))=L(\varnothing)$ for all $t\in F$, $\Lift_t(L(\Box))=L(\Box)$ for all nonzero $t\in F$, and $\Lift_0(L(\Box))=L(\varnothing)\oplus L(\Box)$.  Hence, we can assume $n:=|\lambda|>1$.   Suppose $e\in FP_n(t)$ is an idempotent and  $\ep\in KP_n(T)$ is a lift of $e$.  Let $\tilde{e}$ (resp. $\tilde{\ep}$) denote the image of $e$ (resp. $\ep$) under the quotient map $FP_n(t)\to FP_n(t)/(\zeta)\cong FS_n$ (resp.  $KP_n(T)\to KP_n(T)/(\zeta)\cong KS_n$) where $\zeta$ is as in Lemma \ref{ees}.  Then $\tilde{\ep}\in KS_n$ is a lift of $\tilde{e}\in FS_n$.  However, $\tilde{e}$ (viewed as an element of $KS_n$) is also a lift of $\tilde{e}$ (viewed as an element of $FS_n$).  Thus (by Theorem \ref{appenlift}) $\tilde{\ep}$ is conjugate to $\tilde{e}$ in $KS_n$.  Now suppose $L(\lambda)\cong([n], e)$.  Then $\tilde{e}$ is a primitive idempotent in $FS_n$ corresponding to $\lambda$ (see Remark \ref{zeta}).  Thus $\tilde{e}$ (and hence $\tilde{\ep}$) is also a primitive idempotent in $KS_n$ corresponding to $\lambda$.  Therefore, any orthogonal decomposition of $\ep$ into primitive idempotents must contain exactly one primitive idempotent corresponding to $\lambda$ and all other idempotents corresponding to Young diagrams with smaller size than $\lambda$ (see Remark \ref{zeta}).  The result follows.

(4)  Set $K':=F(T)$ (field of fractions of the polynomial ring $F[T]$) viewed as a subfield of $K$.  Now suppose $\ep\in K'P_n(T)$ is a primitive idempotent corresponding to $\lambda$.  Then by Proposition \ref{fieldex}, $\ep$ is also primitive when viewed as an element of $KP_n(T)$.  Now write $\ep=\sum_{\pi\in P_{n,n}}a_\pi \pi$ where $a_\pi\in K'$.  Let $Q\subset F$ denote the finite set consisting of all roots of all denominators of the $a_\pi$'s.  If $t\not\in Q$, then $a_\pi\in F[[T-t]]$ for all $\pi\in P_{n,n}$.  Thus, if $t\not\in Q$ then $\ep$ is a lift of $e:=\ep|_{T=t}\in FP_n(t)$.  It is easy to show that $e$ is primitive in $FP_n(t)$.  Hence $([n], e)\cong L(\mu)$ for some Young diagram $\mu$ (see Theorem \ref{Youngclass}).  Thus $\Lift_t(L(\mu))=L(\lambda)$ for all $t\not\in Q$.  By part (3) we have $\mu=\lambda$ and we are done.

(5) Set $A=([n], e_1)$, $B=([n'], e_1')$, $e_2=1-e_1\in FP_n(t)$, $e_2'=1-e_1'\in FP_{n'}(t)$, and suppose $\ep_i\in KP_n(T)$ (resp. $\ep'_i\in KP_{n'}(T)$) is a lift of $e_i$ (resp. $e'_i$) for $i\in\{1,2\}$.  Then \begin{equation}\label{ineq} \dim_K\ep_i'KP_{n,n'}\ep_j\geq \dim_Fe_i' FP_{n,n'}e_j\end{equation} for all $i,j\in\{1,2\}$ since evaluating $T=t$ certainly cannot increase dimension.  On the other hand, $$ KP_{n,n'}=\bigoplus_{1\leq i, j\leq 2}\ep'_iKP_{n,n'}\ep_j\quad\text{and}\quad FP_{n,n'}=\bigoplus_{1\leq i, j\leq 2}e'_iFP_{n,n'}e_j.$$  Comparing dimensions we get $$|P_{n,n'}|=\sum_{1\leq i,j \leq 2}\dim_K\ep'_iKP_{n,n'}\ep_j\geq\sum_{1\leq i,j \leq 2}\dim_Fe'_iFP_{n,n'}e_j=|P_{n,n'}|.$$  Hence equality must hold in (\ref{ineq}) for all $i, j\in\{1,2\}$.  In particular, equality holds in (\ref{ineq}) when $i=j=1$ which gives the desired statement.  
\end{proof}









\subsection{On $ \uRep(S_t; F)$ for generic $t$}\label{genericSt}  In this section we will show that $ \uRep(S_t; F)$ is semisimple for ``generic" values of $t$.  Deligne showed that $ \uRep(S_t; F)$ is not semisimple if and only if $t$ is a nonnegative integer (see \cite{Del07}).  That result will follow from our description of the blocks in $ \uRep(S_t; F)$ (see Corollary \ref{ss}).  For now we confine ourselves to prove a weaker result (see Theorem \ref{generic}) which allows us to conclude that $\uRep(S_T; K)$ is semisimple (see Corollary \ref{ssT}).

The following well-known lemma will be useful in showing that $\uRep(S_t; F)$ is generically semisimple.


\begin{lemma}\label{trform}  Suppose $A$ is a finite dimensional $F$-algebra.  For $a\in A$, let $\phi_a$ denote the $F$-linear map $A\to A$ given by $x\mapsto ax$.  Define the \emph{trace form} on $A$ by $(a, b):=\tr(\phi_a\phi_b)$.  Then $A$ is a semisimple algebra if and only if the trace form on $A$ is non-degenerate.  
\end{lemma}

\begin{proof} Let $S:=\{a\in A~|~(a, b)=0\text{ for all }b\in A\}$.  We will show that $S$ is equal to $J(A)$ (the Jacobson radical of $A$).  Suppose $a\in J(A)$.  Since $J(A)$ is a nilpotent ideal, $ab$ is nilpotent for every $b\in A$.  Hence $(a, b)=0$ for all $b\in A$, so $J(A)\subset S$.  To show $S\subset J(A)$ it suffices to show that every element of $S$ is nilpotent.  
If $a\in S$ then $\tr(\phi_a^n)=0$ for all integers $n>0$.   If we let $x_1,\ldots, x_r\in F$ denote the eigenvalues of $\phi_a$, then we have $\sum_{i=1}^rx_i^n=0$ for all $n>0$.  Hence, any non-constant symmetric polynomial in $x_1,\ldots, x_r$ is zero (see for example \cite{MR1354144}).  Thus the characteristic polynomial of $\phi_a$ must be $\chi(X)=X^r$.  
Therefore $\phi_a$, and thus $a$, is nilpotent.  
\end{proof}

Before showing $\uRep(S_t; F)$ is generically semisimple we give two examples illustrating the usefulness of Lemma \ref{trform}.  The reader may find these examples helpful when reading the proof of Theorem \ref{generic}. 

\begin{example} (1) Consider the partition algebra $FP_1(t)$. Let $\pi$ be as in the proof of Theorem \ref{idemP} and fix the ordered basis $P_{1,1}=\{\id_1, \pi\}$ for $FP_1(t)$.  Under this ordered basis 
 the matrix with entries $(x, y)$ for $x, y\in P_{1,1}$ is $$\left(\begin{array}{cc} 2 & t\\ t & t^2\\\end{array}\right)$$
Since the determinant of the matrix above is $t^2$, we conclude (by Lemma \ref{trform}) that $FP_1(t)$ is semisimple if and only if $t\not=0$.


(2)  Consider the partition algebra $FP_2(t)$.  Using the ordered basis $$\includegraphics{diss35.pdf}$$ the matrix with entries $(\pi, \mu)$ for $\pi, \mu\in P_{2,2}$ is 
$${\scriptsize \left(\begin{array}{ccccccccccccccc}
2t^4 & 2t^3 & 2t^3 & 2t^3 & 2t^3 & 2t^3 & 2t^3 & 2t^2 & 2t^2 & 2t^2 & 2t^2 & 2t^2 & 2t^2 & 2t^2 & 2t\\
2t^3& 5t^2& 2t^2& 2t^2& 2t^2& 2t^2& 2t^2& 5t& 2t& 2t& 2t& 5t& 5t& 2t& 5\\
2t^3& 2t^2& 5t^2& 2t^2& 2t^2& 2t^2& 2t^2& 5t& 2t& 2t& 5t& 2t& 2t& 5t& 5\\
2t^3& 2t^2& 2t^2& 2t^2& 2t^3& 2t^2& 2t^2& 2t& 2t^2& 2t& 2t^2& 2t^2& 2t& 2t& 2t\\
2t^3& 2t^2& 2t^2& 2t^3& 2t^2& 2t^2& 2t^2& 2t& 2t^2& 2t& 2t& 2t& 2t^2& 2t^2& 2t\\
2t^3& 2t^2& 2t^2& 2t^2& 2t^2& 2t^2& 5t^2& 2t& 2t& 5t& 5t& 2t& 5t& 2t& 5\\
2t^3& 2t^2& 2t^2& 2t^2& 2t^2& 5t^2& 2t^2& 2t& 2t& 5t& 2t& 5t& 2t& 5t& 5\\
2t^2& 5t& 5t& 2t& 2t& 2t& 2t& 15& 2t& 7& 5& 5& 5& 5& 5\\
2t^2& 2t& 2t& 2t^2& 2t^2& 2t& 2t& 2t& 2t^2& 2t& 2t& 2t& 2t& 2t& 2t\\
2t^2& 2t& 2t& 2t& 2t& 5t& 5t& 7& 2t& 15& 5& 5& 5& 5& 5\\
2t^2& 2t& 5t& 2t^2& 2t& 5t& 2t& 5& 2t& 5& 5& 5& 2t& 5t& 5\\
2t^2& 5t& 2t& 2t^2& 2t& 2t& 5t& 5& 2t& 5& 5& 5& 5t& 2t& 5\\
2t^2& 5t& 2t& 2t& 2t^2& 5t& 2t& 5& 2t& 5& 2t& 5t& 5& 5& 5\\
2t^2& 2t& 5t& 2t& 2t^2& 2t& 5t& 5& 2t& 5& 5t& 2t& 5& 5& 5\\
2t& 5& 5& 2t& 2t& 5& 5& 5& 2t& 5& 5& 5& 5& 5& 5\\
\end{array}\right)}$$ The determinant of the matrix above is $1259712t^{14}(t-1)^4(t-2)^6$.  Hence, by Lemma \ref{trform}, $FP_2(t)$ is semisimple if and only if $t\not=0, 1, 2$.\hfill$\Dox$ 
\end{example}

Now to prove that $\uRep(S_t; F)$ is generically semisimple.

\begin{theorem}\label{generic} $ \uRep(S_t; F)$ is semisimple for all but countably many values of $t$.  Moreover, if $ \uRep(S_t; F)$ is not semisimple, then $t$ is an algebraic integer.
\end{theorem}

\begin{proof}  We may assume $t\not=0$.  Suppose $L_1$ and $L_2$ are two indecomposable objects in $\uRep(S_t; F)$.  By Proposition \ref{proprep}(2) along with Lemma \ref{classifylemma}(1)(2) we can find a nonnegative integer $n$ and idempotents $e_1, e_2\in FP_n(t)$ so that $L_1\cong([n], e_1)$ and $L_2\cong([n], e_2)$.  Whence $\Hom_{ \uRep(S_t; F)}(L_1, L_2)=e_2FP_n(t)e_1$.  Thus, in order to show $\Hom_{ \uRep(S_t; F)}(L_1, L_2)$ is either zero or a finite dimensional division algebra over $F$, it suffices to show $FP_n(t)$ is a semisimple algebra.  Therefore, for a fixed $t\in F$, $ \uRep(S_t; F)$ is semisimple whenever $FP_n(t)$ are semisimple for all $n\geq 0$.  

Let $M_n(t)$ denote the matrix whose rows and columns are labelled by the elements of $P_{n,n}$ (in some fixed order) with the $x,y$-entry equal to $(x, y)$ (the trace form on $FP_n(t)$, see Lemma \ref{trform}).  Then the entries of $M_n(t)$ are in $\Z[t]$.  Hence $\det M_n(t)\in\Z[t]$.  It follows from Lemma \ref{trform} that $FP_n(t)$ is semisimple if and only if $\det M_n(t)\not=0$.  However, from Theorem \ref{sw}, we know that $FP_n(d)$ is semisimple for integers $d\geq 2n$.  Hence, $\det M_n(t)$ is a polynomial in $t$ which is not identically zero.
Thus, for each $n\geq0$ there are only finitely many values of $t$ for which $\det M_n(t)=0$.  Therefore there are only countably many values of $t$ for which $FP_n(t)$ is not semisimple for all $n\geq 0$.   
\end{proof}
       


\begin{remark} If $t\in F$ is not an algebraic integer, then by Theorem \ref{generic} we know $ \uRep(S_t; F)$ is semisimple.  However, given an arbitrary $t\in F$, 
neither Theorem \ref{generic} nor its proof allow us to determine if $\uRep(S_t; F)$ is semisimple.   As mentioned at the beginning of this section, we will eventually show that $\uRep(S_t; F)$ is semisimple if and only if $t$ is not a nonnegative integer.
\end{remark}

We close this section with one final observation.

\begin{corollary}\label{ssT}  $\uRep(S_T; K)$ is semisimple.
\end{corollary}

\begin{proof} This follows from Theorem \ref{generic} as $T$ is not an algebraic integer.\end{proof}







\subsection{The interpolation functor $\uRep(S_d; F)\to \Rep(S_d; F)$}\label{interpolationSt} Throughout this section we assume $d$ is a nonnegative integer.
In this section we will describe following \cite[\S 6]{Del07} how $\uRep(S_d; F)$ ``interpolates" the category $\Rep(S_d; F)$.  More precisely, we will show $\Rep(S_d; F)$ is equivalent to the quotient of $\uRep(S_t; F)$ by the so-called ``negligible morphisms."  To start, let us define the \emph{interpolation functor}.

\begin{definition}\label{Ffunc} $\cat{F}: \uRep(S_d; F)\to  \Rep(S_d; F)$ is the functor defined on indecomposable objects by $\cat{F}([n], e)=f(e)(V_d^{\otimes n})$, and on morphisms $\alpha:([n], e)\to([n'], e')$ by $\cat{F}(\alpha)=f(\alpha)$.  Here $f$ and $V_d$ are as in section \ref{motivation}.
\end{definition}

Notice that $\cat{F}$ is clearly a tensor functor.  From the discussion in section \ref{motivation} we have the following.

\begin{proposition}\label{fully}  $\cat{F}$ is surjective on objects and morphisms.
\end{proposition}

\begin{proof}
This follows from Proposition \ref{full} and Theorem \ref{sw}(1).
\end{proof}

However, by Theorem \ref{sw}(2) we know that $\cat{F}$ does not induce an equivalence of categories.  To illustrate the amount by which $\cat{F}$ fails to induce an equivalence of categories we need the following definition.

\begin{definition} A morphism $f:X\to Y$ in a tensor category is called \emph{negligible} if $\tr(fg)=0$ for all $g:Y\to X$.  Set $\cat{N}(X, Y):=\{f:X\to Y~|~f\text{ is negligible}\}.$
\end{definition}

\begin{example}\label{neg} (1)  The only morphisms in $\uRep_0(S_0; F)$ which are not negligible are nonzero scalar multiples of $\id_0$ (see Example \ref{traces}(1)). 

(2) Let $\pi:[1]\to[1]$ be as in the proof of Theorem \ref{idemP}.  Then $x_\pi:[1]\to[1]$, defined by equation (\ref{xpi}), is given by $x_\pi=\pi-\id_1$.  Since $\tr(\pi)=t=\tr(\id_1)$, we have $\tr(x_\pi)=0$.  Moreover, $x_\pi\pi=(t-1)\pi$ so that $\tr(x_\pi\pi)=t(t-1)$.  We conclude that $x_\pi$ is negligible if and only if $t=0, 1$.

(3) Consider the morphism $\pi\in\Hom_{\uRep_0(S_t; F)}([1], [2])$ given by $$\includegraphics{diss40.pdf}$$  From equation (\ref{xpi}) we get $x_\pi=\pi-\mu_1-\mu_2-\mu_3+2\mu_4$ where $$\includegraphics{diss41.pdf}$$  If we set $$\includegraphics{diss42.pdf}$$
then one can compute $\tr(x_\pi\nu_0)=t(t-1)(t-2)$, and $\tr(x_\pi\nu_i)=0$ for $i=1, 2, 3, 4$.  Thus $x_\pi$ is negligible if and only if $t=0, 1, 2$.\hfill$\Dox$
\end{example}


\begin{remark}  Each of the examples \ref{neg} follow from the following fact:  In $\uRep_0(S_t; F)$ $$\cat{N}([n], [m])=\left\{\begin{array}{ll}
\text{Span}_F\{x_\pi~|~\pi\in P_{n,m}\text{ has more than $t$ parts}\}, & \text{if }t\in\Z_{\geq 0}\\
0, & \text{otherwise.}
\end{array}\right.$$
For $t\in\Z_{\geq 0}$ this fact follows from Theorem \ref{sw}(2), Remark \ref{fzero}, along with the following Proposition \ref{N}(2).  For $t\not\in\Z_{\geq0}$ we will eventually show that the larger category $\uRep(S_t; F)$ is semisimple (see Corollary \ref{ss}).  It is well-known that there are no nonzero negligible morphisms in a semisimple category.
\end{remark}

\begin{proposition}\label{N} The following statements hold in any tensor category.

(1) $\cat{N}$ is a tensor ideal.

(2) The image under a full tensor functor of a morphism $f$ is negligible if and only if $f$ is negligible.
\end{proposition}

\begin{proof} Suppose $f:A\to B$, $g:B\to A$, and $h:B\otimes C\to A\otimes C$ are morphisms in a tensor category.  Observe that $\tr(f\circ g)=\tr(g\circ f)$.  Moreover, one can show $\tr((f\otimes \id_C)\circ h)=\tr(f\circ(\id_A\otimes ev_C)\circ (h\otimes\id_C)\circ(\id_B\otimes coev_C))$.  Statement (1) follows.  Statement (2) follows from the fact that a tensor functor preserves the trace of a morphism.
\end{proof}

Since there are no nonzero negligible morphisms in $\Rep(S_d; F)$, by Proposition \ref{N}(2) we conclude the functor $\cat{F}:\uRep(S_d; F)\to \Rep(S_d; F)$ sends all negligible morphisms to zero.  Thus $\cat{F}$ induces a functor $\cat{\overline{F}}:\uRep(S_d; F)/\cat{N}\to \Rep(S_d; F)$.

\begin{theorem} $\cat{\overline{F}}$ induces an equivalence of categories $\uRep(S_d; F)/\cat{N}\cong \Rep(S_d; F)$.
\end{theorem}

\begin{proof} This follows from Proposition \ref{fully} and Proposition \ref{N}(2).
\end{proof}

We finish this section with the following proposition concerning the functor $\cat{F}$.  For proof of the proposition we refer the reader to \cite[Proposition 6.4]{Del07}\footnote{Deligne assumes $d\geq 2|\lambda|$ in \cite[Proposition 6.4]{Del07}.  If that assumption is removed, Deligne's proof will show Proposition \ref{Findy}.}.

\begin{proposition}\label{Findy}  Suppose $d$ is a nonnegative integer and $\lambda=(\lambda_1, \lambda_2, \ldots)$ is a Young diagram. 
If $d-|\lambda|\geq \lambda_1$, then $\cat{F}(L(\lambda))=L_{\lambda(d)}$.  If $d-|\lambda|<\lambda_1$, then $\cat{F}(L(\lambda))=0$.

\end{proposition}
