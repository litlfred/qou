---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-014-52-marked-words
section_title: "Marked words"
section_number: 5.2
pages: 13-17
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.95
---
We now introduce a combinatorial set-up which we'll use to prove  Proposition \ref{prop:mainrel} below.  A \textbf{marked word} is a word in the elements of $I$ with one letter marked: $\ba=(i_1,i_2,...,\ul{i_\ell},...,i_n)$.  From $\ba$ we can define a functor and an element of $W$: 
\begin{align*}
\Phi(\ba)&=\Theta_{i_1}\cdots\Theta_{i_{\ell-1}}\sF_{i_\ell}\Theta_{i_{\ell1}}\cdots \Theta_{i_n}\bone_\lambda, \\
w(\ba)&=s_{i_1}\cdots s_{i_n}.
\end{align*}
Note that unlike $\Phi(\ba)$, $w(\ba)$ forgets the location of the marked letter.  We say that $\ba$ is \textbf{reduced}, if the corresponding unmarked word is a reduced expression for $w(\ba)$. 

We will apply braid relations to marked words.  Away from the marked letter these operate as usual, and at the marked letter we have:
\begin{align}
\label{rel1}(\hdots,k,\ul{\ell},\hdots) &\leftrightarrow (\hdots,\ul{\ell},k,\hdots),\quad \text{ if } (k,\ell)=0 \text{ and,}\\
\label{rel2}(\hdots,\ell,k,\ul{\ell},\hdots) &\leftrightarrow (\hdots,\ul{k},\ell,k,\hdots),\quad \text{ if } (k,\ell)=-1.
\end{align}
For marked words $\ba,\bb$ we write $\ba \sim \bb$ if they are related by a sequence of braid relations.  
\begin{Lemma}
Let $\ba,\bb$ be marked words which differ by a single braid relation.  Then  there exists $k\in \{0,\pm 1\}$ such that $\Phi(\ba) \cong \Phi(\bb)[k]\langle -k \rangle$.
\end{Lemma}
\begin{proof}
If the relation doesn't involve the marked letter then $\Phi(\ba)\cong \Phi(\bb)$ since Rickard complexes satisfy the braid relations \cite[Theorem 2.10]{CK3}.  Suppose then that the relation does involve the marked letter.
If $(j,\ell)=0$ the result follows from the fact that $\Theta_j\sF_\ell \cong \sF_\ell \Theta_j$.  Otherwise $(j,\ell)=-1$.  Set $\mu=s_\ell s_j(\lambda)-\alpha_j$.  Applying Lemma \ref{lem:Cau} (twice) we deduce that
\begin{align*}
\bone_\mu\Theta_\ell\Theta_j \sF_\ell \bone_\lambda = \Theta_\ell\Theta_j \sF_\ell \bone_\lambda &\cong
\begin{cases}
\Theta_\ell \sF_{j\ell}\Theta_j\bone_\lambda, &\text{ if } \lambda_j\geq 0,\\
\Theta_\ell \sF_{j\ell}\Theta_j\bone_\lambda[1]\langle -1 \rangle, &\text{ if } \lambda_j< 0.
\end{cases}\\
&\cong
\begin{cases}

\sF_j\Theta_\ell\Theta_j\bone_\lambda[-1]\langle 1 \rangle &\text{ if } \lambda_j \geq0, \mu_\ell > 0,\\
\sF_j\Theta_\ell\Theta_j\bone_\lambda[1]\langle -1 \rangle &\text{ if } \lambda_j <0, \mu_\ell \leq 0,\\
\sF_j\Theta_\ell\Theta_j\bone_\lambda &\text{ otherwise.}
\end{cases}
\end{align*}
Hence the result follows.
\end{proof}

\begin{Corollary}\label{lem:markwrds1}
Let $\ba,\bb$ be marked words such that $\ba \sim \bb$.  Then there exists an integer $k$ such that $\Phi(\ba) \cong \Phi(\bb)[k]\langle -k \rangle$.
\end{Corollary}

\begin{Lemma}\label{lem:markwrds2}
Let $\ba=(i_1,...,i_n,\ul{\ell})$ and $\bb=(\ul{\ell'},i_1,...,i_n)$ be reduced marked words such that $w(\ba)=w(\bb)$.  Then $\ba \sim \bb$.  
\end{Lemma}

\begin{proof}
We prove the claim by induction on $n$.  Since $w(\ba)=w(\bb)$ there is a Matsumoto sequence of length $M$ relating the unmarked words  $\fa=(i_1,...,i_n,\ell)$ and $\fb=(\ell',i_1,...,i_n)$.  Let $\fa_0=\fa \to \fa_1 \to\cdots\to \fa_M=\fb$ denote the 
resulting sequence of unmarked words, starting at $\fa$ and ending $\fb$.  Let $\fa_{r+1}$ be the first word in this sequence whose last entry is not $\ell$.  In other words, the first $r$ steps in the sequence do not involve the last entry of $\fa$, but the $(r+1)^{st}$ step does.  

We will now consider  the same sequence of steps, but applied to the marked words.  We then obtain a sequence of marked words $\ba_0=\ba \to \ba_1 \to \cdots\;$.  Further, we know that $\ba_r=(j_1,\dots,j_n,\ul{\ell})$ for some $j_1,\hdots,j_n$, and the next step involves the marked letter.  

If the $(r+1)^{st}$ step is an application of (\ref{rel2}) then $j_{n-1}=\ell$ and the step is:
\begin{align*}
\ba_r=(j_1,\hdots,j_{n-2},\ell,j_n,\ul{\ell}) \to \ba_{r+1}=(j_1,\hdots,j_{n-2},\ul{j_n},\ell,j_n).
\end{align*}
Let $\bb':=(\ul{\ell'},j_1,...,j_{n-2},\ell,j_n)$, i.e. $\bb'$ is obtained from $\bb$ by applying the first $r$ steps to its (last $n$) entries as were used for the (first $n$) entries of $\ba$. Note that $\ba_{r+1}$ and $\bb'$ are reduced marked words such that $w(\ba_{r+1})=w(\bb')$, and both end in $(\ell,j_n)$.    Hence, if we delete these last two entries we obtain two reduced marked words $\ba''=(j_1,...,j_{n-2},\ul{j_n})$ and $\bb''=(\ul{\ell'},j_1,...,j_{n-2})$ such that $w(\ba'')=w(\bb'')$.  
By induction $\ba'' \sim \bb''$ and therefore $\ba_{r+1} \sim \bb'$.  Since clearly $\bb' \sim \bb$, we have our desired result:
$$
\ba \sim \ba_r \sim \ba_{r+1} \sim \bb' \sim \bb.
$$

If  the $(r+1)^{st}$ step  is an application of (\ref{rel1}) then the step is:
\begin{align*}
\ba_r=(j_1,\hdots,j_{n-1},j_n,\ul{\ell}) \to \ba_{r+1}=(j_1,\hdots,j_{n-1},\ul{\ell},j_n).
\end{align*}
 Note that  $\ba_{r+1}$ and $\bb':=(\ul{\ell'},j_1,...,j_{n-1},j_n)$ are reduced marked words such that $w(\ba_{r+1})=w(\bb')$, and both end in $j_n$.  Hence we can delete this last entry and apply a similar analysis as above.



















\end{proof}



\subsection{The relation between $\Theta_{w_0}$ and Chevalley functors}

We now have the machinery in place to prove our main relation.  

\begin{Proposition}\label{prop:mainrel}
For any $i\in I, \lambda \in X$ we have the following relations:
\begin{align*}
\Theta_{w_0}\sE_i\bone_\lambda &\cong \sF_{\tau(i)}\Theta_{w_0}\bone_\lambda[1]\langle \lambda_i \rangle, 
\\
\Theta_{w_0}\sF_i\bone_\lambda &\cong \sE_{\tau(i)}\Theta_{w_0}\bone_\lambda[1]\langle -\lambda_i \rangle. 
\end{align*}
\end{Proposition}

\begin{proof}
We'll prove the first relation, the second being entirely analogous.  
For two functors $\sF,\sG$ we write $\sF \equiv \sG$ if there exist integers $\ell,k$ such that $\sF \cong \sG[\ell]\langle k \rangle$.  

We first show that $\Theta_{w_0}\sE_i \equiv \sF_{\tau(i)}\Theta_{w_0}$ by induction on the rank of $\fg$.   The base case, when $\fg=\fsl_2$,  follows from Lemma \ref{lem:Cau0}.  For the inductive step let $J \subset I$ be a strict subdiagram containing $i$.  Recall the bijection $\tau_J:I\to I$ induced by the longest element $w_0^J \in W_J$.  Let $u=w_0(w_0^J)^{-1}$ and let $u=s_{i_1}\cdots s_{i_n}$ be a reduced expression.  Define two marked words:
\begin{align*}
\ba&=(i_1,\hdots,i_n,\ul{\tau_J(i)}),\\
\bb&=(\ul{\tau(i)},i_1,\hdots,i_n).
\end{align*}
Note that $w(\ba)=w(\bb)$.  By the inductive hypothesis we have $\Theta_{w_0^J}\sE_i 
\equiv  \sF_{\tau_J(i)}\Theta_{w_0^J}$, and therefore
\begin{align*}
\Theta_{w_0}\sE_i \equiv \Theta_u\Theta_{w_0^J}\sE_i 
\equiv  \Theta_u\sF_{\tau_J(i)}\Theta_{w_0^J} \equiv \Phi(\ba)\Theta_{w_0^J}.
\end{align*}
Note that $\ba,\bb$ satisfy the hypothesis of Lemma \ref{lem:markwrds2}, so by Lemmas \ref{lem:markwrds1} and \ref{lem:markwrds2}
we have that $\Phi(\ba)\equiv\Phi(\bb)$, and hence
$\Theta_{w_0}\sE_i \equiv \Phi(\bb)\Theta_{w_0^J} \equiv \sF_{\tau(i)}\Theta_{w_0}.$

We now know there exist integers $k,\ell$ such that $\Theta_{w_0}\sE_i\bone_\lambda \cong \sF_{\tau(i)}\Theta_{w_0}\bone_\lambda[\ell]\langle k \rangle$, and it remains to show that $\ell=1, k=\lambda_i$.  Let $u=w_0s_i$ and let $u=s_{i_1}\cdots s_{i_n}$ be a reduced expression.  Define two marked words:
\begin{align*}
\ba&=(i_1,\hdots,i_n,\ul{i}),\\
\bb&=(\ul{\tau(i)},i_1,\hdots,i_n).
\end{align*}
Note that $\ba,\bb$ satisfy the hypothesis of Lemma \ref{lem:markwrds2}, so by Lemmas \ref{lem:markwrds1} and \ref{lem:markwrds2} there exists an integer $m$ such that $\Phi(\ba)\cong \Phi(\bb)[m]\langle -m \rangle$.  Hence we have that
\begin{align*}
\Theta_{w_0} \sE_i \bone_\lambda &\cong \Theta_u \Theta_i \sE_i\bone_\lambda \\
& \cong \Theta_u \sF_i \Theta_i\bone_\lambda [1]\langle \lambda_i \rangle \\
& \cong \sF_{\tau(i)}\Theta_u \Theta_i \bone_\lambda[m+1]\langle -m+\lambda_i \rangle \\
& \cong \sF_{\tau(i)}\Theta_{w_0} \bone_\lambda[m+1]\langle -m+\lambda_i \rangle
\end{align*}
showing that $\ell+k=1+\lambda_i$.  

On the other hand, we can deduce $k$ by inspecting the relation on the level of Grothendieck groups.  Namely, by \cite[Lemma 5.4]{KT}, we have that 
$$
\st_{w_0}E_i\sone_\lambda = -q^{-\lambda_i}F_{\tau(i)}\st_{w_0}\sone_\lambda,
$$
showing that $k=\lambda_i$.
\end{proof}





















































































































\section{On t-exactness and perversity of $\Theta_{w_0}$}

In this section we will state and prove the central results of the paper.  We fix throughout a categorical representation $\cC$ of  $U_q(\fg)$, and let $w_0=s_{i_1}s_{i_2} \cdots s_{i_n}$ be a reduced expression.





\subsection{$\Theta_{w_0}$ on isotypic categorifications}	In this section we prove that $\Theta_{w_0}$ is t-exact on any isotypic categorification.  Fix $\lambda \in X_+$.  We write $\Theta=\Theta_{w_0}, L=L(\lambda)$ and $\cL=\cL(\lambda)$.

\begin{Lemma}\label{lem:techbit}
Let $k\in\{2,\hdots,n\}$ and set $\mu=s_{i_k}\cdots s_{i_n}(w_0(\lambda))$.  The weight space $L(\lambda)_{\mu-\alpha_{i_{k-1}}}$ is zero.
\end{Lemma}

\begin{proof}
By \cite[Proposition 21.3]{Humph}, it suffices to find $u\in W$ such that $u(\mu-\alpha_{i_{k-1}}) \nsucc w_0(\lambda)$.  Take $u=s_{i_{k-1}}$ and, noting that $(\mu,\alpha_{i_{k-1}})<0$, the result follows.
\end{proof}

Recall that $v_\lambda$ and $v_\lambda^{low}$ are the highest and lowest weight elements of the canonical basis $\bB(\lambda)$.

\begin{Lemma}\cite[Comment 5.10]{KT}\label{lemma:KT}
We have $\st_{w_0}(v_\lambda^{low})=v_\lambda$.
\end{Lemma}

\begin{Proposition}\label{prop:lowestwt}
The equivalence $\Theta\bone_{w_0(\lambda)}:D^b(\cL_{w_0(\lambda)})\to D^b(\cL_{\lambda})$ satisfies $\kk_{low}\mapsto\kk_{high}$, where both are considered as complexes concentrated in degree zero.  In particular, under the equivalences $\cL_\lambda \cong \cL_{w_0(\lambda)}\cong \kk\mmod_\ZZ$,  $\Theta\bone_{w_0(\lambda)}$ is isomorphic to the identity autofunctor of $D^b(\kk\mmod_\ZZ)$.
\end{Proposition}

\begin{proof}
Consider first the case $\fg=\fsl_2$.  On the minimal categorification of highest weight $m$, we have that $\Theta\bone_{-m}(\kk_{low})=\kk_{high}\langle \ell \rangle$ for some $\ell$ by \cite[Theorem 6.6]{CR}.  Since $[\Theta\bone_{-m}]=\st_{1}\sone_{-m}$, by Lemma \ref{lemma:KT} we conclude that $\ell=0$, and hence $\Theta\bone_{-m}(\kk_{low})=\kk_{high}$.

For general $\fg$, suppose $X \in \cL_\nu$ is simple and  $\sF_iX=0$ for some $i \in I$.  Consider $\cL$ as a categorical representation of $\fsl_2$ by restriction to the $i$-th root subalgebra. 
Then for some $m$ we have a morphism of categorical $\fsl_2$ representations
$
R_X:\cL(m) \to \cL,
$
such that $R_X(\kk_{low})=X$ \cite[Theorem 5.24]{CR}.  

The functor $R_X$ is equivariant for the categorical $\fsl_2$ action on $\cC$ determined by $\sE_i,\sF_i$ (in fact it is strongly equivariant in the sense of \cite[Definition 3.1]{LoWe}), and hence commutes with $\Theta_i\bone_\nu$.  Therefore we have that 
\begin{align*}
\Theta_i\bone_{\nu}(X) &\cong  \Theta_i\bone_{\nu}(R_X(\kk_{low})) \\
&\cong R_X(\Theta_i\bone_{\nu}(\kk_{low})) \\
&\cong R_X(\kk_{high}) \in \cL,
\end{align*}
and so $\Theta_i\bone_{\nu}(X)$ is in homological degree zero.  
It follows that in the case when $X$ is not necessarily simple (but still assume that $\sF_iX=0$), $\Theta_i\bone_{\nu}(X)$ is still in homological degree zero.  Indeed, by induction on the length of a Jordan-H\"older filtration of $X$ one deduces this since $\cL \subset D^b(\cL)$ is extension closed. 





Now we study $\Theta\bone_{w_0(\lambda)}$ applied to $\kk_{low}$.  For $k=2,\hdots,n$, by Lemma \ref{lem:techbit}, $$\sF_{i_{k-1}}(\Theta_{i_k}\cdots\Theta_{i_n}\bone_{w_0(\lambda)}(\kk_{low}))=0.$$ By the previous paragraph, it follows that $\Theta_{i_{k-1}}\cdots\Theta_{i_n}\bone_{w_0(\lambda)}(\kk_{low})$ is in homological degree zero, and in particular, $\Theta\bone_{w_0(\lambda)}(\kk_{low})$ is supported in homological degree zero.  Since in addition $$[\Theta\bone_{w_0(\lambda)}]=\st_{w_0}\sone_{w_0(\lambda)},$$ by Lemma \ref{lemma:KT} we conclude that $\Theta\bone_{w_0(\lambda)}(\kk_{low})\cong\kk_{high}$.
\end{proof}

\begin{Theorem}\label{thm:mincat}
Let $\lambda \in X_+$ and set $\cL=\cL(\lambda)$.  For any $\mu \in X$, $$\Theta\bone_\mu[-n]:D^b(\cL_\mu) \to D^b(\cL_{w_0(\mu)})$$ is t-exact, where $n=ht(\mu-w_0(\lambda))$.
\end{Theorem}

\begin{proof}
Consider  $P=\sE_{i_1}\cdots \sE_{i_\ell}(\kk_{low}) \in \cL_\mu$.  We will first prove by induction on $n$ that there exists an integer $k$ such that 
\begin{align}\label{eq:ind}
\Theta(P)[-n] \cong \sF_{j_1}\cdots \sF_{j_\ell}(\kk_{high})\langle k \rangle \in \cL_{w_0(\mu)},
\end{align}
where $j_r=\tau(i_{r})$.

The base case when $n=0$ follows by Proposition \ref{prop:lowestwt}.  For the inductive step write $P=\sE_{i_1}(Q)$. Note that $Q\in \cL_{\mu-\alpha_{i_1}}$.  By Proposition \ref{prop:mainrel} we have that 
\begin{align*}
\Theta\bone_\mu(P)[-n] &= \Theta \sE_{i_1}\bone_{\mu-\alpha_{i_1}}(Q)[-n] \\
&\cong \sF_{\tau(i_1)}\Theta\bone_{\mu-\alpha_{i_1}}(Q)[-n+1]\langle (\mu-\alpha_{i_1},\alpha_{i_1}) \rangle.
\end{align*}
By hypothesis $$\Theta\bone_{\mu-\alpha_{i_1}}(Q)[-n+1] \cong \sF_{j_2}\cdots \sF_{j_\ell}(\kk_{high})\langle k \rangle \in \cL_{w_0(\mu-\alpha_{i_1})}$$ for some $k$, and hence Equation (\ref{eq:ind}) follows.

Since up to grading shift, any projective indecomposable object in $\cL_\mu$, respectively $\cL_{w_0(\mu)}$, is a summand of an object of the form $\sE_{i_1}\cdots \sE_{i_\ell}(\kk_{low})$ (respectively $\sF_{j_1}\cdots \sF_{j_\ell}(\kk_{high})$), it follows that $\Theta\bone_\mu[-n]$ takes projective objects in $\cL_\mu$ to projective objects in $\cL_{w_0(\mu)}$.  Since $\Theta\bone_\mu[-n]$ is a derived equivalence it follows that it is t-exact.








\end{proof}


\begin{Remark}
Theorem \ref{thm:mincat} is a generalisation of  \cite[Theorem 6.6]{CR}, which covers the $\fsl_2$ case.  Note that \cite[Theorem 6.6]{CR} is crucial in the work of Chuang and Rouquier, since it's one of the main technical results needed to prove that Rickard complexes are invertible.  Our proof in the general case follows a completely different approach, but   it does not give a new proof in the case of $\fsl_2$. Indeed we use \cite[Theorem 6.6]{CR} explicitly in the proof of Proposition \ref{prop:lowestwt}, and more generally we use the fact the $\Theta_i$ is invertible throughout.  
\end{Remark}

\begin{Corollary}\label{cor:mainthm}
Suppose $\cC$ is an isotypic categorification of type $\lambda$, for some $\lambda \in X_+$, and let $\mu \in X$.  Then $\Theta\bone_\mu[-n]:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})$ is a t-exact equivalence, where $n=ht(\mu-w_0(\lambda))$.  
\end{Corollary}

\begin{proof}
By Lemma \ref{lem:isocat}, there exists an abelian $\kk$-linear category $\cA$ such that $\cC \cong \cL(\lambda)\otimes_\kk \cA$ as categorical representations.  We have that 
$$
\Theta\bone_\mu[-n](\cL(\lambda)_\mu\otimes_\kk \cA) \cong \Theta\bone_\mu[-n](\cL(\lambda)_\mu) \otimes_\kk \cA \cong \cL(\lambda)_{w_0(\mu)}\otimes_\kk \cA,
$$
proving that $\Theta\bone_\mu[-n]:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})$ is a t-exact equivalence.

\end{proof}


\subsection{$\Theta_{w_0}$ on general categorical representations}\label{sec:mainpf}

In this section we prove that $\Theta_{w_0}$ is a perverse equivalence on an arbitrary categorical representation.
Fix $\mu \in X$ such that $\cC_\mu$ is nonzero.  For ease of notation, set $\cA=\cC_\mu$ and $\cA'=\cC_{w_0(\mu)}$.    


Consider a filtration by Serre subcategories
\begin{align*}
0=\cC_0\subset \cC_1\subset \cdots \subset \cC_r=\cC,
\end{align*}
which can be either the Jordan-H\"older filtration (Theorem \ref{thm:JH}) or the isotypic filtration (Remark \ref{rem:isofilts}).  So for every $i$,  $\cC_i$ is a subrepresentation of $\cC$, and $\cC_i/\cC_{i-1}$ is either a simple categorification or an isotypic one.  Define $\lambda_i \in X_+$ by requiring that $[\cC_i/\cC_{i-1}]_{\CC(q)}$ is a representation of type $\lambda_i$.  




Construct filtrations of $\cA$ and $\cA'$ by $\cA_i=\cC_i\cap \cA, \cA_i'=\cC_i \cap \cA'$.  These are Serre subcategories of $\cA$ and $\cA'$ respectively.  Let $p:\{0,...,r\}\to \ZZ$ be given by 
$p(i)=ht(\mu-w_0(\lambda_i))$.  

\begin{Theorem}
\label{thm:perveq}
$\Theta_{w_0}\bone_\mu:D^b(\cA) \to D^b(\cA')$ is a perverse equivalence with respect to $(\cA_\bullet, \cA_\bullet',p)$ for either the Jordan-H\"older or the isotypic filtration. 
\end{Theorem}



\begin{proof}
Since $\cC_i \subset \cC$ is a categorical subrepresentation, the terms of the functor $\Theta_{w_0}\bone_\mu$ leave $\cC_i$ invariant, and in particular take objects in $\cA_i$ to $\cA_i'$.  By Lemma \ref{lem:trianginv} this implies that $\Theta_{w_0}\bone_\mu (D^b_{\cA_i}(\cA)) \subseteq D^b_{\cA_i'}(\cA')$.

Now, $\cC_i/\cC_{i-1}$ is a simple or isotypic categorification (of type $\lambda_i$).  By Corollary \ref{cor:mainthm}, $\Theta_{w_0}\bone_\mu[-p(i)]$ restricts to an abelian equivalence $\cA_i/\cA_{i-1} \to \cA_i'/\cA_{i-1}'$, i.e. the functor 
$$
\Theta_{w_0}\bone_\mu[-p(i)]:D^b_{\cA_i}(\cA)/D^b_{\cA_{i-1}}(\cA) \to D^b_{\cA'_i}(\cA')/D^b_{\cA'_{i-1}}(\cA')
$$
is a t-exact equivalence.  This shows that $\Theta_{w_0}\bone_\mu$ is a perverse equivalence with respect to $(\cA_\bullet, \cA'_\bullet, p)$.
\end{proof}

\begin{Remark}
The $\fsl_2$ case of Theorem \ref{thm:perveq} appears as \cite[Proposition 8.4]{CRperv}, by a different argument relying on a technical lemma \cite[Lemma 4.12]{CRperv}.  
\end{Remark}
