---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-007-51-general-inductive-properties
section_title: "General inductive properties"
section_number: 5.1
pages: 19-21
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.89
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
The following proposition is a corollary of proposition \ref{propstructgenWBMW} (ii).

\begin{prop} \label{unicitetn1} For all $n \geq 2$, $t_{n+1}$ is uniquely determined by $t_n$ and $t_{n+1}(1)$.
\end{prop}
\begin{proof}
In the sequel, we abuse notations by letting $\WBMW_r$ denote the image of $\WBMW_r$ inside $\WBMW_{n+1}$. 
We prove that, for all $r \leq n+1$, $t_{n+1}$ is uniquely determined by $t_n$ and by its value
on $\WBMW_r$. The case $r = 1$ is the statement of the proposition, since $\WBMW_1 = R$.
We prove this by descending induction on $r$, the case $r = n+1$ being trivial.
Because of proposition \ref{propstructgenWBMW} (ii) we know that
$\WBMW_{r+1} = \WBMW_r + \WBMW_r s_r \WBMW_r +  \WBMW_r s_r^{-1} \WBMW_r$.
If $x,y \in \WBMW_r$, we have $t_{n+1} (x s_r^{\pm 1} y) = t_{n+1} (yx s_r^{\pm 1} )$. Conjugating by 
$(s_1 s_2 \dots s_{n})^{n-r}$ maps $s_r^{\pm 1}$ to $s_n$ and $x,y$ to elements $x',y'$ of $\WBMW_n$. This yields
$ t_{n+1} (yx s_r^{\pm 1} ) =  t_{n+1} (y'x' s_n^{\pm 1} )= t_n(y'x')$. This proves that $t_{n+1}$ is determined by
$t_n$ and by its restriction to $\WBMW_r$. The conclusion follows by induction.
\end{proof}

\begin{prop} \label{prop:unicitetracegen} Let $t'_n$ be the composition of $t_n$ with $M \to M \otimes_R R[(a^2-bc)^{-1},(b+c)^{-1}]$. Then $(t'_n)$ is uniquely determined
by $ t'_1(1)$ and $t'_2(1)$.
\end{prop}
\begin{proof}
In view of the previous proposition, it is sufficient to prove that,
for all $n \geq 2$, $t'_{n+1}(1)$ is determined by $t'_n$.
We have that $\mathcal{R}_{n-1}$ belongs to
$$
H_n s_n H_n + H_n s_n^{-1} H_n - (b+c) b^2c^2 s_{n}^{-2}+ (b+c) s_{n-1}^2 + (bc)^2 s_n^{-1} s_{n-1} s_n^{-1}.
$$
Since $s_n^{-1} s_{n-1} s_n^{-1}$ is conjugated to $s_{n-1}^{-1} s_n s_{n-1}^{-1}$, the Markov property implies that 
$(b+c)t_{n+1}(s_{n-1}^2 - (bc)^2 s_n^{-2})$ is determined by $t_n$. It is straightforward to check that,
because of the cubic relation, $s_{n-1}^2 - (bc)^2 s_n^{-2}$ is equal to $\frac{(b+c)}{a}(a^2-bc).1$ plus a linear
combination of $s_{n-1}$, $s_{n-1}^{-1}$, $s_n$, $s_n^{-1}$, on which the value of $t_{n+1}$ is clearly determined
by $t_n$. It follows that $(b+c)^2(a^2-bc)t_{n+1}(1)$ is uniquely determined by $t_n$, and the conclusion follows.


\end{proof}

We may compare this statement with the stronger assertion one has on $BMW_n^+$.
\begin{prop} \label{prop:unicitetracegenplus} If $(T_n : BMW_n^+ \to S_+)$ is a Markov trace, then it is uniquely
determined by $T_1(1)$ and $T_2(1)$.

\end{prop}
\begin{proof}
As before it is sufficient to prove that,
for all $n \geq 2$, $T_{n+1}(1)$ is determined by $T_n$.
We have that the 12 terms relation can be written as
$$
\begin{array}{lcl}
e_{n-1} s_n e_{n-1} - e_{n-1}&=&x^{-2}
s_{n-1} s_{n} s_{n-1} -yx^{-1}s_{n-1}^{-1}s_{n}-yx^{-1}s_{n}s_{n-1}^{-1}+s_{n}-x^{-1}s_{n-1}s_{n}\\ & & -x^{-1}s_{n}s_{n-1}
+yx^{-2}s_{n-1}s_{n}s_{n-1}^{-1}+yx^{-2}s_{n-1}^{-1} s_{n} s_{n-1}
\\ & & +y^2x^{-2}s_{n-1}^{-1} s_{n} s_{n-1}^{-1}-x^{-1}s_{n-1}-yx^{-1}s_{n-1}^{-1}+1
\end{array}
$$ 
hence belongs to $  BMW_n^+ s_n BMW_n^+ + BMW_n^+ s_n^{-1} BMW_n^+ - x s_{n-1}-yx^{-1}s_{n-1}^{-1}+1$,
hence, since $T_{n+1}(s_{n-1}^{\pm 1}) = T_{n+1}(s_{n}^{\pm 1}) = T_n(1)$, we get that $T_{n+1}(1)$ is indeed determined by $T_n$ and the conclusion follows.
\end{proof}


\begin{cor} \label{cortnplusettnmoins} Over $BMW_n^+$, we have $t_n^+ = (-1)^{n-1} \eta \circ t_n^- \circ \overline{E}$.
\end{cor}
\begin{proof}
We first prove that the RHS defines a Markov trace on $BMW_n^+$, with values in $S_+$.
We denote $T_n$ this RHS.
We clearly have $T_n(\la \beta) = \la T_n( \beta)$, $T_n(\alpha+ \beta) = T_n(\alpha) + T_n(\beta)$ and $T_n(\alpha \beta) = 
T_n(\beta \alpha)$ for all braids $\alpha, \beta \in BMW_n^+$ and scalar $\la \in S_+$, and
also $T_{n+1}(\beta s_n^{\pm 1}) 
= (-1)^n t_{n+1}^-(\overline{E} (\beta s_n^{\pm 1}))
= (-1)^n t_{n+1}^-(\overline{E} (\beta) \overline{E}(s_n^{\pm 1})))
= (-1)^{n-1} t_{n+1}^-(\overline{E} (\beta) s_n^{\pm 1}))
= (-1)^{n-1} t_n^-(\overline{E} (\beta) )) = T_n(\beta)$.
By the proposition above we first need to prove that $T_2(1) = t_2^+(1)$ and $T_2(s_1) = t_2^+(s_1)$.
Recall that $t_2^{\pm}(1) =\delta_K^{\pm}$, $t_2^{\pm}(s_1) = 1$ with
$$
\delta_K^{\pm} = \frac{y \mp x + 1}{x}.
$$
Since $\eta(\delta_K^-) = - \delta_K^+$ we
get $T_2(1) =  \delta_K^+ = t_2^+(1)$ and $T_2(s_1) =1= t_2^+(s_1)$, and the
conclusion follows.

\end{proof}

This corollary proves that the `natural' diagram below
is commutative only up to a sign depending on $n$.

$$
\xymatrix{
 & \overline{BMW}_n \otimes_{\overline{R}} \overline{S}  \ar[dl] \ar[dr] & \\
 BMW_n^+ \ar[d]_{t_n^+} \ar[rr]^{\overline{E}} & & BMW_n^- \ar[d]^{t_n^-} \\
 S_+ \ar[dr] & & S_- \ar[ll]^{\eta} \ar[dl] \\
 & S & }
$$
