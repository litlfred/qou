---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-001-11-the-moduli-space-and-complex-chern-simons-val
section_title: "The moduli space and complex Chern-Simons values"
section_number: 1.1
pages: 6-15
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.977
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
We now begin our investigation of $\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{C})),$ which closely follows [@FintushelStern90]. We have the following presentation of the fundamental group of $X$ $$\label{presentation}
\pi_1(X) \simeq \left\langle h,  x_1,...,x_n \mid  x_1x_2\cdots x_n, x_j^{p_j}h^{-q_j}, [x_j,h], j=1,...,n  \right\rangle.$$

Let us first recall a few of Fintushel and Stern's results concerning the moduli space $\mathcal{M}(X,\mathop{\mathrm{SU}}(2))$ establish in [@FintushelStern90]. As $X$ is an integral homology sphere, the only reducible representation into $SU(2)$ is the trivial one. For an irreducible representation $\rho:\pi_1(X) \rightarrow \mathop{\mathrm{SU}}(2)$ at most $n-3$ of the $\rho(x_j)$ are $\pm I,$ and if exactly $n-m$ of the $\rho(x_j)$ are equal to $\pm I,$ then the component of $\rho$ in $\mathcal{M}(X,\mathop{\mathrm{SU}}(2))$ is of dimension $2(n-m)-6.$

Let $L(p_1,...,p_n) \subset \mathbb{N}^{n}$ be the the set of $n$-tuples $l=(l_1,...,l_n)$ which satisfies the following condition. We have $0\leq l_1 \leq p_1$ and $0\leq l_j \leq \frac{p_j-1}{2},$ for $j=2,...,n$ and there exists at least three distinct ${j_1}<{j_2}<{j_3}$ with $l_{j_t}\not=0$ for $t=1,2,3.$ The following proposition is an adaptation and generalization of Lemma $2$ in [@BodenCurtis06] and Lemma $2.1$ and Lemma $2.2$ in [@FintushelStern90].

::: proposition
[]{#rho_l label="rho_l"} Let $l=(l_1,l_2,...,l_n) \in L(p_1,...,p_n).$ Then there exists matrices $Q_j \in \mathop{\mathrm{SL}}(2,\mathbb{C})$ and a representation $\rho_l: \pi_1(X) \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ with $$\label{X_1}
\rho_l(x_1)= Q_1\begin{pmatrix} e^{\frac{\pi i l_1}{p_1}} & 0
\\ 0 &  e^{-\frac{\pi i l_1}{p_1}} \end{pmatrix}Q_1^{-1}, \ \ \   \rho_l(x_j)= Q_j\begin{pmatrix} e^{\frac{2\pi i l_j}{p_j}} & 0
\\ 0 &  e^{-\frac{2\pi i l_j}{p_j}} \end{pmatrix}Q_j^{-1}$$ for $j=2,\ldots n$. In fact we can choose $Q_j=I$ for $j\not=j_2,j_3.$

Furthermore we can choose the $Q_j$'s such that $$\rho_l : \pi_1(X) \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{R})$$ or $$\rho_l: \pi_1(X) \rightarrow \mathop{\mathrm{SU}}(2)$$ depending on properties of $l$. For any non-trivial representation $\rho: \pi_1(X) \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ there exists $l' \in \mathbb{N}^n$ such that $p_j$ divides $l'_j$ for at most $n-3$ of the indices $j=1,2,3,...,n$ and such that $\rho$ is of the form $$\label{randomrep}
\rho(x_1)= S_1\begin{pmatrix} e^{\frac{\pi i l'_1}{p_1}} & 0
\\ 0 &  e^{-\frac{\pi il'_1 }{p_1}} \end{pmatrix}S_1^{-1}, \ \ \   \rho(x_j)= S_j\begin{pmatrix} e^{\frac{2\pi i l'_j}{p_j}} & 0
\\ 0 &  e^{-\frac{2\pi i l'_j}{p_j}} \end{pmatrix}S_j^{-1}$$ for some $S_1,...,S_n \in \mathop{\mathrm{SL}}(2,\mathbb{C}).$

Finally we have that the map which associates $l\in L(p_1,...,p_n)$ to a non-trivial representation $\rho : \pi_1(X) \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ via [\[randomrep\]](#randomrep){reference-type="eqref" reference="randomrep"} induces an isomorphism $$\pi_0(\mathcal{M}^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))) \cong L(p_1,...,p_n)$$
:::

The family of Brieskorn integral homology spheres ($n=3$) is very special due to the fact that the moduli space $\mathcal{M}(\Sigma(p_1,p_2,p_3), \mathop{\mathrm{SL}}(2,\mathbb{C}))$ is finite with cardinality given by the $\mathop{\mathrm{SL}}(2,\mathbb{C})$ Casson invariant introduced by Curtis [@Curtis01; @Curtis03] $$\lambda_{\mathop{\mathrm{SL}}(2,\mathbb{C})}(\Sigma(p_1,p_2,p_3))=(p_1-1)(p_2-1)(p_3-1)/4.$$ This is shown by Boden and Curtis [@BodenCurtis06]. Prior to this and in relation to Floer homology, Fintuschel and Stern [@FintushelStern90] analyzed the $\mathop{\mathrm{SU}}(2)$ moduli space $\mathcal{M}(X,\mathop{\mathrm{SU}}(2))$ of the Seifert fibered three manifold $X$ considered in this paper and their work shows that the components are even dimensional manifolds with top dimension $2n-6.$ This is in stark contrast to the finiteness of the moduli space $\mathcal{M}(\Sigma(p_1,p_2,p_3), \mathop{\mathrm{SL}}(2,\mathbb{C}))$. In the three fibered case Kitano and Yamaguchi [@KitanoYamaguchi16] has gives a decomposition $$\mathcal{M}(\Sigma,\mathop{\mathrm{SL}}(2,\mathbb{C}))=\mathcal{M}(\Sigma,\mathop{\mathrm{SL}}(2,\mathbb{R})) \bigcup_{\mathcal{M}(\Sigma,\text{U}(1))} \mathcal{M}(\Sigma,\mathop{\mathrm{SU}}(2)).$$ Where $\Sigma=\Sigma(p_1,p_2,p_3).$ Here we can observe the following generalization of this work as an imidiate corollary of Proposition [\[rho_l\]](#rho_l){reference-type="ref" reference="rho_l"}.

::: theorem
[]{#thm:decompSL2C label="thm:decompSL2C"} The natural inclusion $$\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{R}))\sqcup_{\mathcal{M}(X,\text{U}(1))} \mathcal{M}(X,\mathop{\mathrm{SU}}(2)) \rightarrow  \mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$$ induces an isomorphism on the level of $\pi_0$ $$\pi_0(\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{R}))\sqcup_{\mathcal{M}(X,\text{U}(1))} \mathcal{M}(X,\mathop{\mathrm{SU}}(2))) \cong \pi_0(\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))).$$
:::

By this corollary we can in particular conclude that all Chern-Simons values are real and they only depend on $l\in  L(p_1,...,p_n)$. In Proposition [\[CSvalues\]](#CSvalues){reference-type="ref" reference="CSvalues"} below we actually provide an explicit formula.

Before commencing the proof let us introduce the following notation $$\exp(x)=\begin{pmatrix} e^{x} & 0
\\ 0 &  e^{-x} \end{pmatrix},$$ which should not cause any ambiguities as long as the context shows that we are dealing with a matrix.

::: proof
*Proof.* We start with the construction of $\rho_l.$ Introduce the matrices $$X_1=\exp(\pi i l_1/p_1), \ \ \ X_j=\exp(2\pi il_j/p_j)$$ for $j\in \{2,....,n\}\setminus \{j_2,j_3\}.$ Rewrite the relation $\prod_{j=1}^n x_j=1$ as the equivalent relation $$x_{{j_3}+1}\cdots x_n x_1\cdots x_{j_1} \cdots x_{j_2}\cdots x_{j_{3}-1}=x_{j_3}^{-1}.$$ Assume we can chosen $Q_{j_2},Q_{j_3} \in \mathop{\mathrm{SL}}(2,\mathbb{C})$ such that $$\label{veryfinnny}
X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots Q_{j_2}X_{j_2}Q_{j_2}^{-1}\cdots X_{j_{3}-1}=Q_{j_3}^{-1}X_{j_3}^{-1}Q_{j_3}.$$ Taking $Q_j=I$ for $j\notin \{j_2,j_3\},$ we can define $\rho:\pi_1(X)\rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ by the assigment $$\rho(x_j)=Q_jX_jQ_j^{-1}, \ \rho(h)=X_1^{p_1}.$$ To see this, observe that $B:=X_1^{p_1}=(-I)^{l_1}$ is central and as $q_1$ is odd whereas $q_j$ is even for $j\geq 2,$ we also have $X_j^{p_j}=B^{q_j}, \forall j.$ The last relation in $\pi_1(X)$ is ensured by [\[veryfinnny\]](#veryfinnny){reference-type="eqref" reference="veryfinnny"}. Observe that it will suffice to choose $Q_{j_2} \in \mathop{\mathrm{SL}}(2,\mathbb{C})$ such that $$\label{radadadadadadada}
 \mathop{\mathrm{tr}}\left( X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots Q_{j_2}X_{j_2}Q_{j_2}^{-1}\cdots X_{j_{3}-1} \right) =2  \cos\left( \frac{2\pi l_{j_3}}{p_{j_3}}\right)$$ because this will ensure that there exists some $Q_{j_3} \in \mathop{\mathrm{SL}}(2,\mathbb{C})$ with the property that $$Q_{j_3} X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots Q_{j_2}X_{j_2}Q_{j_2}^{-1}\cdots X_{j_{3}-1} Q_{j_3}^{-1}=X_{j_3},$$ since non-diagonalizable elements of $\mathop{\mathrm{SL}}(2,\mathbb{C})$ have trace $\pm2$, given that the unit determinant condition implies that the unique eigenvalue with multiplicity two for such elements must be either $1$ or $-1$ and we have that $$2  \left|\cos\left( \frac{2\pi l_{j_3}}{p_{j_3}}\right) \right|<2.$$ For [\[radadadadadadada\]](#radadadadadadada){reference-type="eqref" reference="radadadadadadada"} we used our assumption on $j_3.$ Write $$\begin{aligned}
&X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots X_{j_2-1}=\exp(ia),
\\ &X_{j_2}=\exp(ib),
 \\ &X_{j_2+1} \cdots X_{j_{3}-1}=\exp(ic),
 \\ &X_{j_3} =\exp(id).
\end{aligned}$$ We observe that by the conditions on $(l_{j_2},p_{j_2})$ and $(l_{j_3},p_{j_3})$ we have that $$b,d \notin \pi \mathbb{Z}.$$ Let $Q_{j_2}=\tilde Q$ where $$\tilde Q =  \tilde Q(u,v,w,z) =\begin{pmatrix} u & v
\\ w & z
\end{pmatrix}$$ for $u,v,w,z$ to be chosen below. Assume $uz-vw=1$ so that $\tilde Q\in \mathop{\mathrm{SL}}(2,\mathbb{C}).$ We compute $$\begin{gathered}
X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots X_{j_2-1} \tilde QX_{j_2} \tilde Q^{-1} X_{j_2+1}\cdots X_{j_{3}-1} 
\\ = \begin{pmatrix} zue^{i(a+b+c)}-wve^{i(a-b+c)} & -uve^{i(a+b-c)}+uve^{i(a-b-c)}
\\ zve^{i(b+c-a)}-zwe^{i(c-a-b)} & -vwe^{-i(a+b+c)}+zue^{i(b-a-c)} \end{pmatrix}.
\end{gathered}$$ Thus we have that $$\begin{gathered}
 \text{tr}\begin{pmatrix} zue^{i(a+b+c)}-wve^{i(a-b+c)} & -uve^{i(a+b-c)}+uve^{i(a-b-c)}
\\ zwe^{i(b+c-a)}-zwe^{i(c-a-b)} & -vwe^{-i(a+b+c)}+zue^{i(b-a-c)} \end{pmatrix}\\ =2zu\cos(a+b+c)-2wv\cos(a+c-b).
\end{gathered}$$ It follows that we must solve $$\label{system}
\begin{pmatrix} \cos(a+b+c) & \cos(a+c-b)
\\ 1 & 1
\end{pmatrix} \begin{pmatrix} zu \\ -wv \end{pmatrix}=\begin{pmatrix} 2\cos(d) \\ 1 \end{pmatrix}.$$ Using the trigonometric identity $\cos(x+y) - \cos(x-y)=-2\sin(x)\sin(y)$ we get $$\begin{aligned}
 \det \begin{pmatrix} \cos(a+b+c) & \cos(a+c-b)
\\ 1 & 1
\end{pmatrix}&= \cos((a+c)+b)-\cos((a+c)-b)
\\ &=-2\sin(a+c)\sin(b).
 
\end{aligned}$$ Thus it remains to argue $a+c \notin \pi \mathbb{Z}$ and $b \notin \pi\mathbb{Z}.$ Assume towards a contradiction that $a+c =\pi m$ for some $m \in \mathbb{Z}.$ Hence we would have $P(a+c)=Pm\pi$ for some integer $m$, which would imply $$l_{j_1} 2^{\epsilon} \prod_{t\not=j_1} p_t = 0 \ \mathop{\mathrm{mod}}\ p_{j_1}$$ for $\epsilon \in \{0,1\},$ with $\epsilon =0$ for $j_1=1$ and $\epsilon=0$ otherwise. This is a contradiction, as $2^{\epsilon} \prod_{t\not=j_1} p_t$ is invertible in $\mathbb{Z}/p_{j_1} \mathbb{Z}$ and $1\leq l_{j_1} \leq (p_{j_1}-1)/2^{\epsilon}.$ We see that $b\notin \pi \mathbb{Z}$ directly from the conditions on $l_{j_2}$. Thus we can solve [\[system\]](#system){reference-type="eqref" reference="system"}, and hence find the needed $u,v,w,z$, which concludes the proof of the first part of the proposition.

Let us now prove that we can actually choose the $Q_j$'s such that we obtain an $\mathop{\mathrm{SL}}(2,\mathbb{R})$-representation. We will denote this new choice of the $Q_j$ by $Q_j^\mathbb{R}$. We set $Q^\mathbb{R}_j = Q$ for $j\in \{1, \ldots j_2-1 ,j_3+1, \ldots, n\}$, where $$Q=\frac{\sqrt{2}}{2}\begin{pmatrix} 1& -i
\\ -i & 1
\end{pmatrix}.$$ which has the following property $$Q \exp(a) Q^{-1} = \begin{pmatrix} \cos(a) & -\sin(a)
\\ \sin(a) & \cos(a)
\end{pmatrix}.$$ Introduce the notation $\tilde X_j = Q X_j Q^{-1}$ and observe by the above computations that $$\begin{gathered}
\mathop{\mathrm{tr}}(\tilde X_{{j_3}+1}\cdots \tilde X_n \tilde X_1\cdots \tilde X_{j_1} \cdots \tilde X_{j_2-1}Q \tilde QX_{j_2}(Q\tilde Q)^{-1}) =
\\ \mathop{\mathrm{tr}}(X_{{j_3}+1}\cdots X_n X_1\cdots X_{j_1} \cdots X_{j_2-1} \tilde QX_{j_2}\tilde Q^{-1}) =
\\ =2zu\cos(a+b)-2wv\cos(a-b).
\end{gathered}$$ To understand which values, say $t$, this trace can take, we consider in analogy with [\[system\]](#system){reference-type="eqref" reference="system"} the equation $$\label{system2}
\begin{pmatrix} \cos(a+b) & \cos(a-b)
\\ 1 & 1
\end{pmatrix} \begin{pmatrix} zu \\ -wv \end{pmatrix}=\begin{pmatrix} t \\ 1 \end{pmatrix}.$$ The determinant is $D = -2\sin(a)\sin(b)$, which is non-vanishing since $a,b\notin \pi \mathbb{Z}$. Then we have that $$\label{system3}
\begin{pmatrix} zu \\ -wv \end{pmatrix} = \frac1D \begin{pmatrix} t - \cos(a-b) \\ -t+\cos(a+b) \end{pmatrix}.$$ For $t\in \mathbb{R}$ we observe that $zu\in \mathbb{R}$ and $wv\in \mathbb{R}$. Now we compute $$\begin{gathered}
Q\tilde Q X_{j_2}(Q\tilde Q)^{-1}=
\\ \begin{pmatrix} (uz-wv)\cos(b) + (uv+wz) \sin(b) & 
(-(uz+wv) - i(uv-wz))\sin(b)
\\ ((uz+wv) - i(uv-wz))\sin(b) &
(uz-wv)\cos(b) - (uv+wz) \sin(b) \end{pmatrix}.
\end{gathered}$$ From which we see that $$Q\tilde QX_{j_2}(Q\tilde Q)^{-1}\in SL(2,\mathbb{R})$$ if and only if $$\text{Im}(uv+wz) = 0, \ \ \ \text{Re}(uv-wz) =0$$ or equivalently $$uv = \overline{wz}$$ whenever $t\in \mathbb{R}$. But then this implies that $$|u|^2 |v|^2 = \frac{(t-\cos(a+b))(t-\cos(a-b))}{D^2}.$$ Which we can solve when $t> \cos(a\pm b)$ by letting $$u= \frac{\sqrt{t-\cos(a+b)}}{D}, \ \ \ v= \frac{\sqrt{t-\cos(a-b)}}{D}$$ and then $$z = \sqrt{t-\cos(a+b)}, \ \ \ w= \sqrt{t-\cos(a-b)}$$ and when $t< \cos(a\pm b)$ then we can take $$u= \frac{\sqrt{\cos(a+b) - t }}{D}, \ \ \ v= \frac{\sqrt{\cos(a-b)-t}}{D}$$ and then $$z = \sqrt{\cos(a+b)-t}, \ \ \ w= \sqrt{\cos(a-b)-t}.$$ This allows us to complete the construction as follows. First we assume that $a, c\notin \pi \mathbb{Z}$. For $$\tilde Q_i = \tilde Q(u_i,v_i,w_i,z_i)$$ for $i=1,2$ we consider the equation $$\left[\tilde X_{{j_3}+1}\cdots \tilde X_n  \tilde X_1\cdots \tilde X_{j_1} \cdots Q \tilde Q_1X_{j_2}(Q \tilde Q_1)^{-1}\right]  =
\left[\left(\tilde X_{j_2+1} \ldots \tilde X_{j_3-1} Q \tilde Q_2 X_{j_3}(Q \tilde Q_2)^{-1}\right)^{-1}\right]$$ which is equivalent to $$\mathop{\mathrm{tr}}\left(\tilde X_{{j_3}+1}\cdots \tilde X_n  \tilde X_1\cdots \tilde X_{j_1} \cdots Q \tilde Q_1X_{j_2}(Q \tilde Q_1)^{-1}\right) =
\mathop{\mathrm{tr}}\left(\tilde X_{j_2+1} \ldots \tilde X_{j_3-1} Q \tilde Q_2 X_{j_3}(Q \tilde Q_2)^{-1}\right)$$ since these are certainly all $\mathop{\mathrm{SL}}(2,\mathbb{C})$ matrices. But now, using that we also have that $c,d \notin \pi\mathbb{Z}$, we can chose $t$ bigger than $\cos(a \pm b)$ and $\cos(c\pm d)$ and fix $\tilde Q_i$ as above such that $$\label{tra1}
 \mathop{\mathrm{tr}}\left(\tilde X_{{j_3}+1}\cdots \tilde X_n  \tilde X_1\cdots \tilde X_{j_1} \cdots Q \tilde Q_1X_{j_2}(Q \tilde Q_1)^{-1}\right)  = t$$ and $$\label{tra2}
 \mathop{\mathrm{tr}}\left(\tilde X_{j_2+1} \ldots \tilde X_{j_3-1} Q \tilde Q_2 X_{j_3}(Q \tilde Q_2)^{-1}\right) = t$$ Thus we can now conclude that there exist $Q^{\mathbb{R}} \in \mathop{\mathrm{SL}}(2,\mathbb{R})$ such that $$\begin{gathered}
\tilde X_{{j_3}+1}\cdots \tilde X_n  \tilde X_1\cdots \tilde X_{j_1} \cdots Q \tilde Q_1X_{j_2}(Q \tilde Q_1)^{-1} = \\Q^\mathbb{R}\left(\tilde X_{j_2+1} \ldots \tilde X_{j_3-1} Q \tilde Q_2 X_{j_3}(Q \tilde Q_2)^{-1}\right)^{-1} (Q^\mathbb{R})^{-1} =
\\  Q^\mathbb{R}Q \tilde Q_2 X_{j_3}^{-1}  (Q^\mathbb{R}Q \tilde Q_2)^{-1} Q^\mathbb{R}\tilde X_{j_3-1}^{-1} (Q^\mathbb{R})^{-1} \ldots Q^\mathbb{R}\tilde X_{j_2+1}^{-1} (Q^\mathbb{R})^{-1}  .
\end{gathered}$$ Thus if we further set $$Q^\mathbb{R}_{j_2} = Q \tilde Q_1, Q^\mathbb{R}_{j_3} = Q^\mathbb{R}Q \tilde Q_2$$ and $$Q^\mathbb{R}_j = Q^\mathbb{R}Q$$ for $j\in \{j_2+1,\ldots,j_3-1\}$, then we have found the needed conjugation to obtain an $\mathop{\mathrm{SL}}(2,\mathbb{R})$-representation. Let us now consider the remanning cases. Suppose that $a\in \pi Z$ but $c\notin \pi \mathbb{Z}$. Then the common trace $t$ is by [\[tra1\]](#tra1){reference-type="eqref" reference="tra1"} forced to be $e^{ia} \cos b$, so we can solve [\[tra2\]](#tra2){reference-type="eqref" reference="tra2"} if and only if $e^{ia} \cos b$ is not contained in the interval spanned by the two values $\cos(c\pm d)$. If this is the case we proceed with the argument as above. If on the other hand $e^{ia} \cos b$ is contained in the interval spanned by $\cos(c\pm d)$, then it is well known that we can choose $Q_j \in \mathop{\mathrm{SU}}(2)$ so as to obtain an $\mathop{\mathrm{SU}}(2)$-representation. A similar argument of course works in the case where $c\in \pi Z$ but $a\notin \pi \mathbb{Z}$. If we have $a,c \in \pi\mathbb{Z}$, then $a+c \in \pi\mathbb{Z}$, but this we have already argued is impossible.

Now let $\rho: \pi_1(X) \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ be an arbitrary non-trivial representation. As remarked before any non-trivial representation is irreducible since $X$ is an integral homology three sphere. Since $\rho(h)$ commutes with the image of $\rho$, we see that $\rho(h) = \pm I$. Hence the relation $x_j^{p_j}=h^{q_j}$ implies that $\rho(x_j)^{p_j}=\pm I,$ and for $j=2,...,n$ we must have $\rho(x_j)^{p_j}=I,$ since $q_j$ is even. Hence $\rho$ must be of the form [\[randomrep\]](#randomrep){reference-type="eqref" reference="randomrep"} for some $l'\in \mathbb{N}^n.$ It only remains to argue that at most $n-3$ of the $\rho(x_j)$ are $\pm I.$ If not, the relation $x_1x_2 \cdots x_n=1$ implies that there is $j_1<j_2$ with $\rho(x_{j_1})\rho(x_{j_2})=\pm I.$ As $p_{j_1}$ and $p_{j_2}$ are relatively coprime, this is only possible if $\rho(x_{j_1})=\pm I$ and $\rho(x_{j_2})=\pm I.$ This would imply that $\rho(\pi_1(X))\subset \{\pm 1\}=Z(\mathop{\mathrm{SU}}(2))$ which contradicts the fact that $\rho$ is irreducible since it was assumed non-trivial.

We describe the connected components of $\mathcal{M}^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$. First we assume that $l_1 \in \{1, \ldots p_1-1\}$ and $l_2 >0$ for an $l\in L(p_1,...,p_n)$. We will now prove that the subset $\mathcal{M}_l^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$ of $\mathcal{M}^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$ consisting of conjugacy classes of representations $\rho$ for which $$\mathop{\mathrm{tr}}(\rho(x_1)) = 2\cos(\pi l_1/p_1), \ \ \ \mathop{\mathrm{tr}}(\rho(x_j)) = 2\cos(2\pi l_j/p_j), \ \ j = 2, \ldots n$$ is connected. Let $$T  =    \bigtimes_{j=3}^{n} \left[\exp\left(\frac{2\pi il_j}{p_j}\right)\right].$$ It is obvious that $T$ is connected. Let now $m : T \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ be the algebraic product map. Let $P\subset \mathop{\mathrm{SL}}(2,\mathbb{C})$ be the set of non-diagonalizable elements in $\mathop{\mathrm{SL}}(2,\mathbb{C})$ and observe that $P$ has complex co-dimension one, thus so does $m^{-1}(P) \subset T$, but then it follows that $T' = T- m^{-1}(P)$ is also connected. For any $$(M_3, \ldots, M_n) \in T',$$ we observe that the set of $(Q_1,Q)\in \mathop{\mathrm{SL}}(2,\mathbb{C})$ which solves $$\label{eqa1}
 \exp(\pi l_1/p_1) Q_1 \exp(2 \pi  l_2/p_2) Q_1^{-1} = Q M_n^{-1} \ldots M_3^{-1} Q^{-1}$$ is non empty and connected since it is acted transitively on by $(\mathbb{C}^*)^2 \times \mathbb{C}^*$, where the first factor comes from the ambiguity from solving [\[system2\]](#system2){reference-type="eqref" reference="system2"} and the second comes from the stabiliser of $M_n^{-1} \ldots M_3^{-1}$ under conjugation. But then we see that an open dense subset of $\mathcal{M}_l^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$ is connected, thus $\mathcal{M}_l^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$ it self must be connected. If $l_1\in \{0,p_1\}$ or $l_2 =0$, we proceed as follows. Choose $j_1, j_2 \in \{1,\ldots, n-2\}$ such that $$a = \pi \frac{l_1}{p_1} + 2\pi \sum_{j=2}^{j_1} \frac{l_j}{p_j}, \ \ \ b = 2\pi \sum_{j=j_1+1}^{j_2} \frac{l_j}{p_j},$$ has the property that $a,b\notin \pi \mathbb{Z}$. Now consider the equation $$\label{eqa2}
\exp(a) Q_1 \exp(b) Q_1^{-1} = Q M_n^{-1} \ldots M_{j_2+1}^{-1} Q^{-1}.$$ The connectedness is now argued in exactly the same way, with [\[eqa2\]](#eqa2){reference-type="eqref" reference="eqa2"} in place of [\[eqa1\]](#eqa1){reference-type="eqref" reference="eqa1"}. ◻
:::

For an $\mathop{\mathrm{SL}}(2,\mathbb{C})$-connection $a$ in the trivial $\mathop{\mathrm{SL}}(2,\mathbb{C})$-bundle on $X$ we recall the Chern-Simons action is given by $$\label{eq:CSaction} \mathop{\mathrm{S_{CS}}}(a)=\frac{1}{8\pi^2 }\int_X \mathop{\mathrm{tr}}\left(a\mathop{\mathrm{{d}\hskip-.6mm}}a +\frac{2}{3}a^3\right) \mod \mathbb{Z}.$$

We now compute the Chern-Simons values of the representations constructed above.

::: proposition
[]{#CSvalues label="CSvalues"} For any representation $\rho : \pi_1(X) \rightarrow SL(2,\mathbb{C})$, define $l=(l_1,...,l_n) \in L(p_1,...,p_n),$ so that $$\mathop{\mathrm{tr}}(\rho(x_1)) = 2\cos(\pi l_1/p_1), \ \ \ \mathop{\mathrm{tr}}(\rho(x_j)) = 2\cos(2\pi l_j/p_j), \ \ j = 2, \ldots n.$$ Then we have that $$\label{CS}
\mathop{\mathrm{S_{CS}}}\left( \rho \right) = -\frac{P}{4}\left(\frac{l_1}{p_1}+\sum_{j=2}^{n} \frac{2l_j}{p_j}\right)^2 \  \mathop{\mathrm{mod}}\ \mathbb{Z}.$$
:::

Formula [\[CS\]](#CS){reference-type="eqref" reference="CS"} was proven for $\mathop{\mathrm{SU}}(2)$ connections by Kirk and Klassen and it is stated in Theorem $5.2$ in [@KirkKlassen90]. It is proven using the following general result. Let $M$ be a closed oriented three manifold containing a knot $K.$ Let $Y$ be the complement of a tubular neighborhood of $K$ in $M.$ With respect to an identification $M\setminus Y \simeq D^2 \times S^1,$ choose simple closed curves $\mu, \lambda$ on $\partial Y$ intersecting in a single point such that $\mu$ bounds a disc of the form $D^2 \times \{1\}.$ Let $\rho_t:\pi_1(Y) \rightarrow \text{SU}(2)$ be a path of representations such that $\rho_0(\mu)=\rho_1(\mu)=1,$ and for which there exists continuous piecewise differentiable functions $$\alpha,\beta:I \rightarrow \mathbb{R}$$ with $$\begin{aligned}
\begin{split}
\rho_t(\mu)= \begin{pmatrix} e^{2\pi i \alpha(t)} & 0
\\ 0 &  e^{-2\pi i \alpha(t)} \end{pmatrix}, \  \rho_t(\lambda)=\begin{pmatrix} e^{2\pi i \beta(t)} & 0
\\ 0 &  e^{-2\pi i \beta(t)} \end{pmatrix}.
\end{split}
\end{aligned}$$ Thinking of $\rho_1,\rho_0$ as flat connections on $M$ we have $$\label{KK}
\mathop{\mathrm{S_{CS}}}(\rho_0)-\mathop{\mathrm{S_{CS}}}(\rho_1)=-2 \int_0^1 \beta(t) \alpha'(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t \ \text{mod} \ \mathbb{Z}.$$ Notice that formula [\[KK\]](#KK){reference-type="eqref" reference="KK"} differs from the corresponding formula in [@KirkKlassen90] by a sign. This discrepancy was already discussed by Freed and Gompf in [@FreedGompf91] and is due to a sign convention. See the footnote on page $98$ in [@FreedGompf91]. The formula [\[KK\]](#KK){reference-type="eqref" reference="KK"} was also used in the work [@AndersenHansen] by the first author and Hansen.

::: proof
*Proof of Proposition [\[CSvalues\]](#CSvalues){reference-type="ref" reference="CSvalues"}.* Let $K\subset X$ be the $n$'th exceptional fiber. Let $Y$ be the complement of a tubular neighborhood of $K$ in $X.$ Removing $K$ has the effect on $\pi_1$ of removing the relation $x_n^{p_n}=h^{-q_n}$, i.e. we have a presentation $$\label{presentation2}
\pi_1(Y) \simeq \left\langle h,  x_1,...,x_n \mid  x_1x_2\cdots x_n, x_1^{p_1}h^{-q_1},...,x_{n-1}^{p_{n-1}}h^{-q_{n-1}} , \forall j [x_j,h]   \right\rangle.$$ As the meridian and longitude of $\partial Y$ we can take $\mu=x_n^{p_n}h^{q_n}$ and $\lambda=x_n^{-p_1\cdots p_{n-1}}h^c$ respectively, where $c=\sum_{j=1}^{n-1} \frac{p_1\cdots p_{n-1}q_j}{p_j}.$ These choices of meridian and longitude coincide with the choices made in [@FintushelStern90].

Let $\rho:\pi_1(X)\rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$ be any irreducible representation with its corresponding $l=(l_1,...,l_n) \in L(p_1,...,p_n)$. Now $\rho(h)=\exp(\pi i v)$ for some integer $v\in \mathbb{Z}$. Introduce the two quantities $$\xi= P\left(\frac{l_1}{p_1}+\sum_{j=2}^{n} \frac{2l_j}{p_j}\right)$$ and $$\eta=\frac{\xi}{P}.$$

The proof of [\[CS\]](#CS){reference-type="eqref" reference="CS"} presented here consists analogously with the proof of Theorem $5.2$ in [@KirkKlassen90] of two parts. In the first part, we find a path of $\mathop{\mathrm{SL}}(2,\mathbb{C})$ connections on $X$ connecting $\rho$ to an abelian representation $\rho_0$. In fact $\rho_0$ will be an $\mathop{\mathrm{SU}}(2)$ connection on $X.$ In the second part, we then find a path from $\rho_0$ to the trivial representation $\rho^{\text{triv}}$ and we then apply Kirk and Klassens formula [\[KK\]](#KK){reference-type="eqref" reference="KK"}. The only difference from the proof in [@KirkKlassen90] is that we need to explicitly ensure that our paths stay away from parabolic representations. The relevant paths are chosen such that $\lambda,\mu$ are mapped to the maximal $\mathbb{C}^*$ torus of diagonal matrices.

After conjugating by $S_n^{-1}$ we have $\rho(x_n)=\exp\left(\frac{2\pi i l_n}{p_n}\right).$ Consider the subset $$S\subset \text{Hom}\left(\pi_1(Y),\mathop{\mathrm{SL}}(2,\mathbb{C})\right)$$ of representations $\tilde{\rho}$ satisfying $$\tilde{\rho}(h)=\rho(h), \ [\tilde{\rho}(x_1)]=\left[\exp\left(\frac{\pi il_1}{p_1}\right)\right]\, $$
and
$$\ [\tilde{\rho}(x_j)]=\left[\exp\left(\frac{2\pi il_j}{p_j}\right)\right], \ \text{for }2\leq j\leq n-1.$$ where $[Q]$ denotes the $\mathop{\mathrm{SL}}(2,\mathbb{C})$ conjugacy class of $Q \in \mathop{\mathrm{SL}}(2,\mathbb{C}).$ By considering the presentation [\[presentation2\]](#presentation2){reference-type="eqref" reference="presentation2"}, we see that $S$ is naturally homeomorphic to the product of the $n-1$ conjugacy classes $$S\simeq \left[\exp\left(\frac{\pi il_1}{p_1}\right)\right]\times  \bigtimes_{j=2}^{n-1} \left[\exp\left(\frac{2\pi il_j}{p_j}\right)\right].$$ Therefore the connectedness of $\mathop{\mathrm{SL}}(2,\mathbb{C})$ implies that $S$ is connected. Following a similar argument use in the proof of the previous proposition, we let $$m : S \rightarrow \mathop{\mathrm{SL}}(2,\mathbb{C})$$ be the algebraic product map. Let $P\subset \mathop{\mathrm{SL}}(2,\mathbb{C})$ be the set of non-diagonalizable elements in $\mathop{\mathrm{SL}}(2,\mathbb{C})$ and observe that $P$ has complex co-dimension one, thus so does $m^{-1}(P) \subset S$, but then it follows that $S' = S- m^{-1}(P)$ is also connected.

Write $\rho=\rho_1$ and observe that $\rho_1 \in S'$. Choose a smooth path $\rho_t$ in $S'$ connecting $\rho_1$ to $\rho_0 \in S'$ given by $$\rho_0(x_1)=\exp\left(-\frac{\pi i l_1}{p_1}\right), \ \rho_0(x_j)=\exp\left(-\frac{2\pi i l_j}{p_j}\right), \ j=2,...,n-1$$ and $\rho_0(x_n)=\exp\left(\frac{\pi i l_1}{p_1}+\sum_{j=2}^{n-1}\frac{2\pi i l_j}{p_j}\right).$ By an over all conjugation we can choose the arc $\rho_t$ such that $\rho_t(x_n)=\exp(2\pi if(t))$ for a smooth function $f(t).$ We have $f(0)=\frac{l_1}{2p_1}+\sum_{j=2}^{n-1} \frac{l_j}{p_j}$ and $f(1)=\frac{l_n}{p_n}.$ Notice that $f(0)=\frac{\eta}{2}-f(1).$ As $q_n$ is even we have the following two equalities $$\begin{aligned}
\rho_t(\mu)=\rho_t(x_n)^{p_n}\rho_t(h)^{q_n}=&\exp(2\pi i p_nf(t)),
\\ \rho_t(\lambda)=\rho_t(x_n)^{-p_1\cdots p_{n-1}}\rho_t(h)^c &= \exp\left(-2\pi i p_1\cdots p_{n-1}f(t)+vc\pi i\right).
\end{aligned}$$ Write $y=vc\in \mathbb{Z}.$ Define $\alpha_1(t)=p_nf(t)$ and $\beta_1(t)=-\frac{P}{p_n}f(t)+\frac{y}{2}.$ We have that $$\begin{aligned}
 \label{firstintegral}\begin{split}
-2 \int_0^1 \alpha'_1(t)\beta_1(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t&=-2 \int_0^1 p_nf'(t)\left(-\frac{P}{p_n}f(t)+\frac{y}{2}\right) \ \mathop{\mathrm{{d}\hskip-.6mm}}t
\\ &=-2 \int_{f(0}^{f(1)} \left(-Pu+\frac{p_n y}{2}\right) \ \mathop{\mathrm{{d}\hskip-.6mm}}u
\\ &= -2\left[-\frac{Pu^2}{2}+\frac{p_ny u}{2}\right]_{u=f(0)}^{u=f(1)}
\\ &=Pf(1)^2-yp_nf(1)-Pf(0)^2+yp_nf(0)
\\ &= Pf(1)^2-Pf(0)^2+yp_nf(0) \text{ mod } \mathbb{Z}.
\end{split}
\end{aligned}$$ For the last identity we used that $yp_nf(1)=yl_n \in \mathbb{Z}.$

For the second part we use the fact that $H_1(Y) \simeq \mathbb{Z}$ with generator $\mu$ to conclude that the abelian $\mathop{\mathrm{SU}}(2)$ connection $\rho_0$ can be connected to the trivial representation $\rho^{\text{triv}}$ by a path of $\mathop{\mathrm{SU}}(2)$ representations $\sigma_t$ with $\sigma_t(\mu)=\exp(2\pi it \alpha_1(0))$ and $\sigma_t(\lambda)=\exp(2\pi i \beta_1(0)).$ Let $\alpha_0(t)=t\alpha_1(0)$ and $\beta_0(t)=\beta_1(0).$ As $\mathop{\mathrm{S_{CS}}}(\rho^{\text{triv}})=0,$ we can apply Kirk and Klassen's formula [\[KK\]](#KK){reference-type="eqref" reference="KK"} to obtain $$-\mathop{\mathrm{S_{CS}}}(\rho) = \mathop{\mathrm{S_{CS}}}(\rho^{\text{triv}})-\mathop{\mathrm{S_{CS}}}(\rho)= -2 \int_0^1 \alpha'_0(t)\beta_0(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t-2\int_0^1 \alpha'_1(t)\beta_1(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t.$$ We have $$\begin{aligned}
-2\int_0^1 \alpha'_0(t)\beta_0(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t&=-2f(0)(-Pf(0)+\frac{yp_n}{2})=2Pf(0)^2-yp_nf(0).
\end{aligned}$$ Comparing this with [\[firstintegral\]](#firstintegral){reference-type="eqref" reference="firstintegral"} we get that $$\begin{aligned}
-\mathop{\mathrm{S_{CS}}}(\rho) & = P(f(1)^2+f(0)^2) \ \mathop{\mathrm{mod}}\ \mathbb{Z}
\\ &=P((f(1)+f(0))^2-2f(0)f(1)) \ \mathop{\mathrm{mod}}\ \mathbb{Z}
\\ &= \frac{\xi^2}{4P} \ \mathop{\mathrm{mod}}\ \mathbb{Z}.
\end{aligned}$$ For the last equality we used that $2Pf(0)f(1)\in \mathbb{Z}$ and that $$f(0)+f(1)=\frac{\eta}{2}=\frac{\xi}{2P}.$$ This is what we wanted. ◻
:::

For $x \in \mathbb{Q}$ let $[x]=x \mod  \mathbb{Z}.$ Introduce the set $$\begin{gathered}
 \mathcal{W}(p_1,...,p_n)= \left\{ \left[ \frac{-m^2}{4P}\right]  : \text{  $m \in \mathbb{Z}$ is divisible by at most $n-3$ of the $p_j$'s}\right\}.
\end{gathered}$$ Recall that the classical complex Chern-Simons values $\mathop{\mathrm{CS}}^*_{\mathbb{C}}(X)$ is the range of the restriction of $\mathop{\mathrm{S_{CS}}}$ to $\mathcal{M}^*(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))$. Thus we can compute $\mathop{\mathrm{CS}}_{\mathbb{C}}^*(X)$ as a corollary of Proposition [\[CSvalues\]](#CSvalues){reference-type="ref" reference="CSvalues"}.

::: corollary
[]{#cor:HUHU label="cor:HUHU"} We have that $$\mathop{\mathrm{CS}}^*_{\mathbb{C}}(X)= \mathcal{W}(p_1,...,p_n).$$
:::

::: proof
*Proof.* It is clear that $\mathop{\mathrm{CS}}_{\mathbb{C}}^*(X) \subset \mathcal{W}(p_1,...,p_n).$ We must show that for any $y \in \mathbb{Z}$ which is not divisible by more than three of the $p_j$ we can find $l=(l_1,...,l_n) \in L(p_1,...,p_n)$ which solves the congruence equation $$\label{congruence}
y^2 = \left(P\left( \frac{l_1}{p_1}+\sum_{j=2}^{n} \frac{2 l_j}{p_j}\right) \right)^2 \  \mathop{\mathrm{mod}}\ 4P\mathbb{Z}$$ For $x \in \mathbb{Z}$ and $d \in \mathbb{N}$ let $[x]_d$ denote the congruence class of $x$ in the quotient ring $\mathbb{Z} / d\mathbb{Z}.$ Since $p_j$ is odd for $j\geq 2,$ it follows that $4p_1,p_2,...,p_n$ are also pairwise co-prime. Hence the Chinese remainder theorem applies and the natural ring homomorphism $q:\mathbb{Z} \rightarrow \mathbb{Z}/4p_1\mathbb{Z} \oplus_{j=2}^n \mathbb{Z}/p_j\mathbb{Z},$ given by $x \mapsto ([x]_{4p_1},...,[x]_{p_n}),$ descends to an isomorphism of rings $$\overline{q}: \mathbb{Z}/4P\mathbb{Z} \overset{\sim}{\rightarrow} \mathbb{Z}/4p_1\mathbb{Z} \ \oplus \ \bigoplus_{j=2}^n \mathbb{Z}/p_j\mathbb{Z} .$$ It follows that [\[congruence\]](#congruence){reference-type="eqref" reference="congruence"} is in fact equivalent to the following $n$ congruence equations $$\begin{aligned}
\label{congruence2}
[{y]^2}_{4p_1}&=\left[l_1\prod_{j=2}^n p_j+2\left(\sum_{j=2}^{n} l_j \prod_{t\not=j} p_t\right)\right]^2_{4p_1}, 
\\ [y]^2_{p_j}&=\left[2l_j \prod_{t\not=j}p_t \right]^2_{p_j}, \ \forall j\geq 2.
\end{aligned}$$ The coprimality conditions ensures that $2\prod_{t\not=j} p_t$ is an invertible element in $\mathbb{Z}/p_j\mathbb{Z}$ and therefore solving the last $n-1$ of the equations in [\[congruence2\]](#congruence2){reference-type="eqref" reference="congruence2"} can indeed be done with $0 \leq l_j\leq (p_j-1)/2.$ It remains only to consider the first of the equations in [\[congruence2\]](#congruence2){reference-type="eqref" reference="congruence2"}. To this end we first observe that $$\left( l_1 \prod_{j=2}^n p_j + 2 \sum_{j=2}^n l_j  \prod_{t\neq j} p_j\right)^2 = \left( l_1 \prod_{j=2}^n p_j \right)^2 \text{ mod } 4 p_1$$ But then we can solve $$y^2 = l_1^2 \prod_{j=2}^n p^2_j \text{ mod } 4 p_1$$ for $0 \leq l_1 \leq 2p_1$. But we also have that $$y^2 = (-l_1 \pm 2 p_1)^2 \prod_{j=2}^n p_j^2\text{ mod } 4 p_1.$$ Thus it follows that we can in fact solve [\[congruence2\]](#congruence2){reference-type="eqref" reference="congruence2"} with $l_1\in \{0,...,p_1\}.$ Thus we have shown that $\mathop{\mathrm{CS}}_{\mathbb{C}}^*(X) = \mathcal{W}(p_1,...,p_n).$ ◻
:::

Our analysis of the components of the $\mathop{\mathrm{SL}}(2,\mathbb{C})$ moduli space and the Chern-Simons values now allow us to prove the following.

::: theorem
[]{#ThmBrieskornSphere label="ThmBrieskornSphere"} The Chern-Simons action $$\mathop{\mathrm{S_{CS}}}: \pi_0(\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))) \rightarrow \mathbb{R}/\mathbb{Z}$$ is injective and induces an isomorphism $$\pi_0(\mathcal{M}(X,\mathop{\mathrm{SL}}(2,\mathbb{C}))) \cong \mathcal{W}(p_1,\ldots, p_n) \sqcup \{0\}.$$
:::

::: proof
*Proof.* We use the inverse of the isomorphism $$\overline{q}: \mathbb{Z}/4P\mathbb{Z} \overset{\sim}{\rightarrow} \mathbb{Z}/4p_1\mathbb{Z} \bigoplus_{j=2}^n \mathbb{Z}/p_j\mathbb{Z}$$ to conclude that for each Chern-Simons value in $\mathcal{W}(p_1,\ldots, p_n)$, there is a unique $l\in L(p_1,\ldots, p_n)$ with the given Chern-Simons value, concluding the proof by the last statement of Proposition [\[rho_l\]](#rho_l){reference-type="ref" reference="rho_l"}. ◻
:::

Thereom [\[thm:cs\]](#thm:cs){reference-type="ref" reference="thm:cs"} is a summary of the main results obtained in this section.

::: proof
*Proof of Theorem [\[thm:cs\]](#thm:cs){reference-type="ref" reference="thm:cs"}.* This follows from Theorem [\[thm:decompSL2C\]](#thm:decompSL2C){reference-type="ref" reference="thm:decompSL2C"}, Corollary [\[cor:HUHU\]](#cor:HUHU){reference-type="ref" reference="cor:HUHU"} and Theorem [\[ThmBrieskornSphere\]](#ThmBrieskornSphere){reference-type="ref" reference="ThmBrieskornSphere"}. ◻
:::
