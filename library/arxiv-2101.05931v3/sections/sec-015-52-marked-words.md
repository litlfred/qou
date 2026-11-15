---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-015-52-marked-words
section_title: "Marked words"
section_number: 5.2
pages: 13-14
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.936
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
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
