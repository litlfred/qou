---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-031-75-the-right-regular-corepresentation
section_title: "The right regular corepresentation"
section_number: 7.5
pages: 72-75
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.945
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:double:right}
In analogy to the left regular action, there is a notion of a right regular action. First we consider the quantum plane.
\begin{Prop} Given $W$ that defines the left regular corepresentation, 
\Eq{W_R:=(\hat{J}\ox\hat{J}) W_{21}^* (\hat{J}\ox\hat{J})\in \cB(\cH)\ox \cA}
is also a multiplicative unitary and satisfies
\Eq{(1\ox \D)W_R=W_{R,12}W_{R,13},}
i.e. it defines a corepresentation, called the right-regular corepresentation.
\end{Prop}
Using the realization of $Ad \hat{J}$, we see that $W_R$ is given by 
\Eq{W_R=e^{\frac{i}{2\pi b^2}\log A_*\ox \log A}g_b(B_*\ox B)=e^{\frac{i}{2\pi b^2}\log A_*\ox \log A}\int_{\R+i0} B_*^{ib\inv \t}\ox B^{ib\inv \t}\frac{e^{-\pi i\t^2}}{G_b(Q+i\t)}d\t,}
where on the space $\cH_{corep}$ we have 
$\hat{J}=\over[f](t,s)$ so that
\Eq{A_* = e^{-2\pi bt},\tab B_* = e^{-2\pi bp_t}.}
Therefore we see that the corepresentation is acting on the $t$-coordinate by:
\Eq{f(s,t)\mapsto \int_{\R+i0} f(s,t-\t)\frac{e^{-\pi i\t^2}}{G_b(Q+i\t)}A^{-ib\inv t}B^{ib\inv \t}d\t,}
in which under the pairing we have:
\Eq{X_r = e^{-2\pi b t}, \tab Y_r=e^{-2\pi b p_t},}
\Eq{\til[X]_r=e^{-2\pi b\inv t},\tab \til[Y]_r=e^{-2\pi b\inv p_t}.}
In other words, under the transform $t\mapsto -t$, we conclude together with Proposition \ref{Bqaction} that
\begin{Prop} We have the equivalence
\Eq{L^2(\cA)\simeq \cH_{irr}\ox \cH_{irr}}
as representation of $\cB_{q\til[q],L}\ox \cB_{q\til[q],R}\simeq \cB_{q\til[q]}\ox \cB_{q\til[q]}$, where $\cH_{irr}:=L^2(\R)$ is the canonical representation of $\cB_{q\til[q]}$ on $L^2(\R)$. Hence this is an analogue to the classical ``Peter-Weyl" theorem on ``functions on the quantum plane".
\end{Prop}

Now let us look at the case for $\cD(\cA)$. To define the right regular corepresentation, we need the corresponding multiplicative unitary $\bW_R$. It is known that $\bW_R$ is given by
\Eq{\bW_R=(\cU\ox 1)\bW_{3412}(\cU^*\ox 1),}
where 
\Eq{\cU=\hat{\bJ}_m\bJ_m = (J\hat{J}\ox \hat{J}J)Z\in \cA\ox \hat{\cA}.}
We simplify the expression and express $\bW_R$ in terms of 4 $g_b$'s as before.

\begin{Prop} $\bW_R$ is given by (cf. \eqref{Wmsimple})
\Eq{\bW_R=V_{32}W_{R,13}V_{32}^{''*}\hat{W}_{R,24},}
where
$V^{''*} = (\hat{J}\ox\hat{J})V^*(\hat{J}\ox\hat{J}).$
\end{Prop}
\begin{proof}
From (\cite{KV2} Prop 2.15), we have:
\begin{eqnarray*}
\hat{W}&=&W_{21}^*,\\
W_R&=&(\hat{J}\ox\hat{J})W_{21}^*(\hat{J}\ox\hat{J})\\
&=&(\hat{J}\ox\hat{J})(J\ox\hat{J})W_{21}(J\ox\hat{J})(\hat{J}\ox\hat{J})\\
&=&(\hat{J}J\ox 1)W_{21}(J\hat{J}\ox 1),\\
\hat{W}_R&=&(J\ox J)W(J\ox J)\\
&=&(J\ox J)(\hat{J}\ox J)W^*(\hat{J}\ox J)(J\ox J)\\
&=&(J\hat{J}\ox 1)W^*(\hat{J}J\ox 1).\\
\end{eqnarray*}
Hence we obtain (the indices indicate the legs in which the operators are acting):
\begin{eqnarray*}
\bW_R&=& ((J_1\hat{J}_1\hat{J}_2J_2)Z_{12})W_{31}Z_{12}^*\hat{W}_{42}Z_{12}(Z_{12}^* (\hat{J}_1J_1 J_2\hat{J}_2))\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)Z_{12}W_{31}Z_{12}^*\hat{W}_{42}(\hat{J}_1J_1 J_2\hat{J}_2)\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)V_{12}V_{12}'W_{31}V_{12}^{*'}V_{12}^*\hat{W}_{42}(\hat{J}_1J_1 J_2\hat{J}_2)\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)V_{12}W_{31}V_{12}^*\hat{W}_{42}(\hat{J}_1J_1 J_2\hat{J}_2)\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)W_{31}V_{32}\hat{W}_{42}(\hat{J}_1J_1 J_2\hat{J}_2)\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)W_{31}V_{32}(J_1 \hat{J}_1J_2\hat{J}_2)\hat{W}_{R,24}\\
&=&(J_1\hat{J}_1\hat{J}_2J_2)(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)(\hat{J}_1J_1 )W_{R,13}V_{32}(J_2\hat{J}_2)\hat{W}_{R,24}\\
&=&(\hat{J}_2J_2)(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)W_{R,13}V_{32}(J_2\hat{J}_2)\hat{W}_{R,24}\\
&=&(J_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)W_{R,13}V_{32}(\hat{J}_2J_2)\hat{W}_{R,24}\\
&=&V_{32}(J_2\hat{J}_3)(\hat{J}_2\hat{J}_3)W_{R,13}V_{32}(\hat{J}_2J_2)\hat{W}_{R,24}\\
&=&V_{32}W_{R,13}(J_2\hat{J}_2)V_{32}(\hat{J}_2J_2)\hat{W}_{R,24}\\
&=&V_{32}W_{R,13}(J_2\hat{J}_2)(J_2\hat{J}_3)V_{32}^*(J_2\hat{J}_3)(\hat{J}_2J_2)\hat{W}_{R,24}\\
&=&V_{32}W_{R,13}(\hat{J}_2\hat{J}_3)V_{32}^*(\hat{J}_2\hat{J}_3)\hat{W}_{R,24}.\\
\end{eqnarray*}
\end{proof}

Now we can realize the action on $\cH_{corep}\ox\hat{\cH}_{corep}$ as in previous section:
\begin{Prop} The action of the components of $\bW_R$ is given by
\begin{eqnarray*}
\hat{W}_{R,24}&=&e^{-\frac{i}{2\pi b^2}\log \hat{A}_*\ox \log \hat{A}}g_b^*(\hat{B}_*\ox \hat{B})\\
f(s_1,t_1)g(s_2,t_2)&\mapsto& \int f(s_1,t_1)g(s_2,t_2-\t)e^{-2\pi i\t t_2+\pi i\t^2}G_b(-i\t)\hat{B}^{ib\inv \t} \hat{A}^{-ib\inv t_2}d\t,\\
W_{R,13}&=&e^{\frac{i}{2\pi b^2}\log A_*\ox \log A}g_b(B_*\ox B)\\
f(s_1,t_1)g(s_2,t_2)&\mapsto& \int f(s_1,t_1-\t)g(s_2,t_2)\frac{e^{-\pi i\t^2}}{G_b(Q+i\t)} A^{-ib\inv t_1}B^{ib\inv \t}d\t,\\
V_{32}&=&e^{\frac{i}{2\pi b^2}\log \hat{A}\inv\ox \log A\inv}g_b(q\hat{B}\hat{A}\inv\ox B)\\
f(s_1,t_1)g(s_2,t_2)&\mapsto&\int_\R\int_{\R+i0}\int_\R f(s_1,t_1)g(s_2+\a,t_2+\a+\t)\\
&&\frac{e^{2\pi i(\a\b+\a\t+\b\t+s_2\t)}G_b(\frac{Q}{2}+is_2-it_2)}{G_b(\frac{Q}{2}+is_2-it_2-i\t)G_b(Q+i\t)}A^{ib\inv \b}B^{ib\inv \t}d\a d\t d\b,\\
V_{32}^{''*}&=&e^{\frac{i}{2\pi b^2}\log A_*\ox \log A}g_b(B_*\ox B)\\
f(s_1,t_1)g(s_2,t_2)&\mapsto&\int_\R\int_{\R+i0}\int_\R g(s_2+\a,t_2+\a+\t)\\
&&\frac{e^{2\pi i\a(t_2-s_2-\b)}e^{-\pi i\t^2}G_b(\frac{Q}{2}+is_2-it_2)}{G_b(\frac{Q}{2}+is_2-it_2-i\t)G_b(Q+i\t)}A^{ib\inv \b}B^{ib\inv \t}d\a d\t d\b.\\
\end{eqnarray*}
\end{Prop}

\begin{Thm} The right regular corepresentation is given by
\begin{eqnarray*}
f(s_1,t_1)g(s_2,t_2)&\mapsto&\int_{\R+i\e_\t} \int_\R \int_C d\s d\a d\t f(s_1,t_1-\s)g(s_2+\s,t_2+\t-\a)\\
&&e^{\pi Q(-\a+\t)+2\pi i(-\s s_2+\a \t-\a t_2+\s t_2)}\\
&&\frac{G_b(-i\s)G_b(\frac{Q}{2}+is_2-it_2)G_b(i\s-i\t)G_b(\frac{Q}{2}-i\s+it_1-it_2)}{G_b(\frac{Q}{2}+is_2-it_2+i\s-i\t)G_b(Q+i\a)G_b(\frac{Q}{2}-i\t+it_1-it_2)}\\
&&A^{ib\inv(t_2-t_1-s_2)}B^{ib\inv \t}\hat{B}^{ib\inv \a} \hat{A}^{-ib\inv (t_2+\t)} d\a d\t d\s,
\end{eqnarray*}
where the contour $C$ of $\s$ goes above $\s=0$ and below $\s=\t$.
\end{Thm}

We have to follow the transformations given in the left regular picture. So we apply the transformations after Theorem \ref{leftco} and an extra one that does not affect the previous action:
\begin{eqnarray*}
s_2&\mapsto& s_2-t_1,\\
s_1&\mapsto& s_1+\frac{s_2}{2},\\
t_1&\mapsto& t_1+\frac{s_2}{2},\\
t_2&\mapsto& t_2+\frac{s_2}{2},\\
\end{eqnarray*}
and obtain
\begin{eqnarray}
f\ox g&\mapsto&\int_{\R+i\e_\t} \int_\R \int_C d\s d\a d\t f(s_1,t_1-\s)g(s_2,t_2+\t-\a)\nonumber\\
&&e^{\pi Q(-\a+\t)+2\pi i(\s t_1+\a \t-\a t_2+\s t_2)}e^{-\pi i \a s_2}\nonumber\\
&&\frac{G_b(-i\s)G_b(\frac{Q}{2}-it_1-it_2)G_b(i\s-i\t)G_b(\frac{Q}{2}-i\s+it_1-it_2)}{G_b(\frac{Q}{2}-it_1-it_2+i\s-i\t)G_b(Q+i\a)G_b(\frac{Q}{2}-i\t+it_1-it_2)}\nonumber\\
&&\label{rightcorep}A^{ib\inv(t_2-\frac{s_2}{2})}B^{ib\inv \t}\hat{B}^{ib\inv \a} \hat{A}^{ib\inv (-t_2-\t-\frac{s_2}{2})}d\a d\t d\s.
\end{eqnarray}
