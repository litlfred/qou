---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-030-74-the-left-regular-corepresentation
section_title: "The left regular corepresentation"
section_number: 7.4
pages: 66-72
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.966
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:double:left}
With the construction of the multiplicative unitary $\bW$, we can talk about the corepresentation induced by it. By the unitary transformations given in Section \ref{sec:Trans:corep}, we can choose the Hilbert space to be $\cH_{corep}\ox\hat{\cH}_{corep}$ so that the action can be nicely described. 

Recall that the left regular corepresentation is given by 
\Eq{f\ox g \mapsto \bW'(f\ox g\ox 1\ox 1),}
where $f\ox g\in \cH_{corep}\ox\hat{\cH}_{corep}$ and $\bW' = \bW_{3412}\in \cB(\cH_{corep}\ox\hat{\cH}_{corep})\ox \cA\ox \hat{\cA}$. Here we realize $\cA \ox \hat{\cA}$ as operators in the 3rd and 4th components.

\begin{Thm} \label{leftco} The left regular corepresentation is given by
\begin{eqnarray*}&&f(s_1,t_1)g(s_2,t_2)\mapsto\\
&=&\int_{\R+i0} \int_\R \int_C f(s_1-\a+\t,t_1-\s)g(s_2+\s,t_2)\\
&&\frac{G_b(-i\s)G_b(-i\a+i\s)G_b(\frac{Q}{2}+is_1-it_1+i\t)G_b(\frac{Q}{2}+is_1-is_2-i\s+i\t)}{G_b(Q+i\t)G_b(\frac{Q}{2}+is_1-it_1-i\a+i\s+i\t)G_b(\frac{Q}{2}+is_1-is_2-i\a+i\t)}\\
&&e^{2\pi i\s(t_1-s_1-\t)}e^{2\pi is_1\t}A^{ib\inv s_1}B^{ib\inv \t}\ox\hat{B}^{ib\inv\a}\hat{A}^{ib\inv (t_1+s_2-s_1-\t)} d\s d\a d\t,\\
\end{eqnarray*}
where the contour $C$ of $\s$ goes above $\s=0$ and below $\s=\a$.
\end{Thm}

\begin{proof} Since we have used a permutation, now $\bW'$ reads
\Eq{\bW' = \bW_{3412} = W_{31}V''_{14}\hat{W}_{42}V_{14}^*.}

On the space $\cH_{corep}\ox \hat{\cH}_{corep}$, the coaction of the components of $\bW$ is given by:
\begin{eqnarray*}
W_{31}: f(s_1,t_1)g(s_2,t_2)&\mapsto& \int_{\R+i0} f(s_1+\t,t_1)g(s_2,t_2)\frac{e^{2\pi is_1\t}}{G_b(Q+i\t)}A^{ib\inv s}B^{ib\inv \t} d\t,\\
\hat{W}_{42}: f(s_1,t_1)g(s_2,t_2)&\mapsto& \int_{\R+i0} f(s_1,t_1)g(s_2+\s,t_2)G_b(-i\s)\hat{B}^{ib\inv\s}\hat{A}^{ib\inv s_2}d\s.\\
\end{eqnarray*}
The actions for $V$ and $V''$ are harder to describe since they involve formally $A^{ib\inv p}$. Therefore we use $\cS$ (cf. Proposition \ref{Strans}) to sent the first component back to $\cH_{rep}$ and obtain their actions.
\begin{eqnarray*}
&&\cS V_{14}^* \cS\inv:f\ox g \\
&\mapsto &\cS\cdot \left(\int_{\R+i0} B^{ib\inv \t}\ox \hat{B}^{ib\inv\t}\hat{A}^{-ib\inv \t}   G_b(-i\t)d\t \right) e^{\frac{i}{2\pi b^2} \log \hat{A}\ox\log A}\cdot\\
&& \int_\R f(\a-s_1,\a-t_1)g(s_2,t_2)G_b(\frac{Q}{2}-it_1+is_1) e^{-2\pi i(\a-s_1) s_1}d\a\\
&=&\cS\cdot \int_{\R+i0}\int_\R f(\a-s_1-\t,\a-t_1)g(s_2,t_2)G_b(\frac{Q}{2}-it_1+is_1+i\t)G_b(-i\t)  \cdot\\
&&e^{-2\pi i(\a-s_1-\t) (s_1+\t)} \hat{B}^{ib\inv\t}\hat{A}^{ib\inv s_1}d\a d\t\\
&=&\int_\R\int_{\R+i0}\int_\R f(\a-\b+s_1-\t,\a-\b+t_1)g(s_2,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t)}{G_b(\frac{Q}{2}+it_1-is_1)}  \cdot\\
&&e^{-2\pi i(\a-\b+s_1-\t) (\b-s_1+\t)}e^{2\pi i(\b-s_1)s_1} \hat{B}^{ib\inv\t}\hat{A}^{ib\inv (\b-s_1)}d\a d\t d\b\\
&& \mbox{shifting $\a\mapsto \a+\b+\t, \b\mapsto \b+s_1$:}\\
&=&\int_\R\int_{\R+i0}\int_\R f(s_1+\a,t_1+\a+\t)g(s_2,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t) }{G_b(\frac{Q}{2}+it_1-is_1)}\cdot\\
&&e^{-2\pi i(\a\b+\a\t+s_1\t)} \hat{B}^{ib\inv\t}\hat{A}^{ib\inv \b} d\a d\t d\b,\\
\end{eqnarray*}
and finally for $V''$:
\begin{eqnarray*}
&&\cS V_{14}'' \cS\inv:f\ox g \\
&\mapsto&\cS\cdot \left(e^{\frac{i}{2\pi b^2}\log\hat{A}_*\ox\log\hat{A}\inv}\int_{\R+i0}\hat{B}_*^{ib\inv \t}\ox \hat{B}^{ib\inv \t} e^{\pi i\t^2}G_b(-i\t)d\t\right)\cdot\\
&&\int_\R f(\a-s_1,\a-t_1)g(s_2,t_2)G_b(\frac{Q}{2}-it_1+is_1) e^{-2\pi i(\a-s_1) s_1}d\a\\
&=&\cS\cdot \int_{\R+i0}\int_\R f(\a-s_1\a-t_1+\t)g(s_2,t_2)G_b(\frac{Q}{2}-it_1+is_1+i\t) \\
&&e^{-2\pi i(\a-s_1) s_1}e^{\pi i\t^2}G_b(-i\t) \hat{A}^{-ib\inv t_1}\hat{B}^{ib\inv\t}d\a d\t\\
&=&\int_\R\int_{\R+i0}\int_\R f(\a-\b+s_1,\a-\b+t_1+\t)g(s_2,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t)}{G_b(\frac{Q}{2}+it_1-is_1)} \\
&&e^{-2\pi i(\a-\b+s_1)(\b-s_1)}e^{\pi i\t^2}e^{2\pi i(\b-s_1)s_1}e^{2\pi i\t(t_1-\b)}\hat{B}^{ib\inv\t}\hat{A}^{ib\inv (t_1-\b)}d\a d\t d\b 
\end{eqnarray*}
\begin{eqnarray*}
&& \mbox{shifting $\a\mapsto \a+\b, \b\mapsto t_1-\b$:}\\
&=&\int_\R\int_{\R+i0}\int_\R f(s_1+\a,t_1+\a+\t)g(s_2,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t)}{G_b(\frac{Q}{2}+it_1-is_1)} \\
&&e^{-2\pi i\a(t_1-s_1)}e^{2\pi i\b(\a+\t)}e^{\pi i\t^2}\hat{B}^{ib\inv\t}\hat{A}^{ib\inv \b} d\a d\t d\b.\\
\end{eqnarray*}
Combining, we have 
\begin{eqnarray*}
&&f\ox g\\
&\mapsto_{V^*}&\int_\R\int_{\R+i\e_\t}\int_\R d\a d\t d\b f(s_1+\a,t_1+\a+\t)g(s_2,t_2)\cdot\\
&&\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t) }{G_b(\frac{Q}{2}+it_1-is_1)}e^{-2\pi i(\a\b+\a\t+s_1\t)} \hat{B}^{ib\inv\t}\hat{A}^{ib\inv \b}\\
&\mapsto_{\hat{W}}&\int_{\R+i\e_\s}\int_\R\int_{\R+i\e_\t}\int_\R d\a d\t d\b d\s f(s_1+\a,t_1+\a+\t)g(s_2+\s,t_2)\cdot\\
&&\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\t)G_b(-i\s) }{G_b(\frac{Q}{2}+it_1-is_1)}e^{-2\pi i(\a\b+\a\t+s_1\t)} e^{2\pi is_2\t}\hat{B}^{ib\inv(\s+\t)}\hat{A}^{ib\inv (\b+s_2)}.\\
\end{eqnarray*}
The integral for $\b$ and $\s$ are independent, hence we can interchange them. Furthermore from the decay properties for $f\ox g$ and the asymptotic properties for $G_b(-i\t)G_b(-i\s)$, the integral for $\a,\t$ and $\s$ is absolutely convergent, hence we can interchange the order so that $d\s$ goes to the inner most layer.

\begin{eqnarray*}
&\mapsto_{V''}&\int_\R\int_{\R+i\e_\t'}\int_\R\int_\R\int_{\R+i\e_\t}\int_\R \int_{\R+i\e_\s} d\s d\a d\t d\b  d\a' d\t' d\b'\\ &&f(s_1+\a+\a',t_1+\a+\a'+\t+\t')g(s_2+\s,t_2)\\
&&\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t+i\t')G_b(-i\t)G_b(-i\s) }{G_b(\frac{Q}{2}+it_1-is_1+i\t')}\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t')G_b(-i\t')}{G_b(\frac{Q}{2}+it_1-is_1)}\cdot\\
&&e^{-2\pi i(\a\b+\a\t+(s_1+\a')\t)} e^{2\pi is_2\t}e^{-2\pi i\a'(t_1-s_1)}e^{2\pi i\b'(\a'+\t')}e^{\pi i\t'^2}e^{2\pi i\b'(\s+\t)}\\
&&\hat{B}^{ib\inv(\s+\t+\t')}\hat{A}^{ib\inv (\b+\b'+s_2)}
\end{eqnarray*}
\begin{eqnarray*}
&&\mbox{shifting $\a\mapsto \a-\a', \b\mapsto \b-\b', \t\mapsto \t-\t'$:}\\
&=&\int_\R\int_{\R+i\e_\t'}\int_\R \int_\R\int_{\R+i\e_\t-i\e_\t'}\int_\R \int_{\R+i\e_\s}d\s d\a d\t d\b d\a' d\t' d\b'\\ &&f(s_1+\a,t_1+\a+\t)g(s_2+\s,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(i\t'-i\t)G_b(-i\s)G_b(-i\t')}{G_b(\frac{Q}{2}+it_1-is_1)}\\
&&e^{2\pi i\b'(\a+\s+\t)}e^{2\pi i\a'(\b+s_1-t_1)}e^{2\pi i(\a+s_1-s_2)(\t'-\t)-2\pi i\a\b+\pi i\t'^2}\hat{B}^{ib\inv(\s+\t)}\hat{A}^{ib\inv (\b+s_2)}.\\
\end{eqnarray*}

The integral over $d\b d\a'$ are just Fourier transforms, hence we can integrate over $\a'$ to get $\b=t_1-s_1$:
\begin{eqnarray*}
&=&\int_\R\int_{\R+i\e_\t'}\int_{\R+i\e_\t-i\e_\t'}\int_\R \int_{\R+i\e_\s} d\s d\a d\t d\t' d\b'\\ &&f(s_1+\a,t_1+\a+\t)g(s_2+\s,t_2)\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(i\t'-i\t)G_b(-i\s)G_b(-i\t')}{G_b(\frac{Q}{2}+it_1-is_1)}\\
&&e^{2\pi i\b'(\a+\s+\t)}e^{2\pi i(\a+s_1-s_2)(\t'-\t)-2\pi i\a(t_1-s_1)+\pi i\t'^2}\hat{B}^{ib\inv(\s+\t)}\hat{A}^{ib\inv (t_1+s_2-s_1)}.\\
\end{eqnarray*}
Next from the decay properties for $G_b(i\t'-i\t)G_b(-i\t')$ this is integrable over $\t'$. By shifting $\t\mapsto \t-\s-\a$ we see also that the integrations over $\s,\t, \a$ are absolutely convergent, and furthermore integrations over $\a, \s$ do not depend on $\b'$. Hence we can interchange the order for $d\t d\t'$ and then $d\s d\a$ to get
$$\int_\R \int_{\R+i\e_\s}\int_\R\int_{\R+i\e_\t-i\e_\t'}\int_{\R+i\e_\t'}d\t' d\t d\b'  d\s d\a .$$
Using the reflection properties, we bring $G_b(-i\t')$ to the denominator. Notice that the contour goes above $\t'=0$ and below $\t'=\t$, hence we can integrate over $\t'$ using Lemma \ref{tau} to get

\begin{eqnarray*}
&=&\int_\R \int_{\R+i\e_\s}\int_\R\int_{\R+i\e_\t-i\e_\t'}d\t d\b'  d\s d\a f(s_1+\a,t_1+\a+\t)g(s_2+\s,t_2)\\ &&\frac{G_b(\frac{Q}{2}+it_1-is_1+i\t)G_b(-i\s)G_b(-i\t)G_b(\frac{Q}{2}-i\a+is_2-is_1)}{G_b(\frac{Q}{2}+it_1-is_1)G_b(\frac{Q}{2}-i\a-i\t+is_2-is_1)}\\
&&e^{2\pi i\b'(\a+\s+\t)}e^{-2\pi i(\a+s_1-s_2)\t-2\pi i\a(t_1-s_1)} \hat{B}^{ib\inv(\s+\t)}\hat{A}^{ib\inv (t_1+s_2-s_1)}\\
&=&\int_\R \int_{\R+i\e_\s}\int_\R\int_{\R+i\e_\t-i\e_\t'}d\t d\b'  d\s d\a f(s_1-\a,t_1-\a+\t)g(s_2+\s,t_2)\\ &&\frac{G_b(\frac{Q}{2}+is_1-it_1)G_b(-i\s)G_b(-i\t)G_b(\frac{Q}{2}+is_1-is_2-i\a+i\t)}{G_b(\frac{Q}{2}+is_1-it_1-i\t)G_b(\frac{Q}{2}+is_1-is_2-i\a)}\\
&&e^{2\pi i\b'(\s+\t-\a)}e^{2\pi i (t_1-s_1)(\t-\a)} \hat{B}^{ib\inv(\s+\t)}\hat{A}^{ib\inv (t_1+s_2-s_1)},\\
\end{eqnarray*}
where we used the reflection properties again, and flipping $\a\mapsto -\a$. Now we can integrate $\t$ and $\b'$ by Fourier transform to get $\t=\a-\s$. However, this should be interpreted as a function of $\s$ over $\R$, and then analytic continued to $\R+i\e_\s$, so that the contour for $\s$ will be pushed under the pole for $\s=\a$ in $G_b(-i\t)\mapsto G_b(i\s-i\a)$. We get
\begin{eqnarray*}
&=&\int_\R \int_C d\s d\a f(s_1-\a,t_1-\s)g(s_2+\s,t_2)\\ &&\frac{G_b(\frac{Q}{2}+is_1-it_1)G_b(-i\s)G_b(i\s-i\a)G_b(\frac{Q}{2}+is_1-is_2-i\s)}{G_b(\frac{Q}{2}+is_1-it_1-i\a+i\s)G_b(\frac{Q}{2}+is_1-is_2-i\a)}\\
&&e^{2\pi i (t_1-s_1)\s} \hat{B}^{ib\inv \a}\hat{A}^{ib\inv (t_1+s_2-s_1)}.\\
\end{eqnarray*}

Finally we apply $W_{31}$ to get
\begin{eqnarray*}
&\mapsto_W& \int_{\R+i\e_\t} \int_\R \int_C d\s d\a d\t f(s_1-\a+\t,t_1-\s)g(s_2+\s,t_2)\\
&&\frac{G_b(-i\s)G_b(-i\a+i\s)G_b(\frac{Q}{2}+is_1-it_1+i\t)G_b(\frac{Q}{2}+is_1-is_2-i\s+i\t)}{G_b(Q+i\t)G_b(\frac{Q}{2}+is_1-it_1-i\a+i\s+i\t)G_b(\frac{Q}{2}+is_1-is_2-i\a+i\t)}\\
&&e^{2\pi i\s(t_1-s_1-\t)}e^{2\pi is_1\t}A^{ib\inv s_1}B^{ib\inv \t}\ox\hat{B}^{ib\inv\a}\hat{A}^{ib\inv (t_1+s_2-s_1-\t).}
\end{eqnarray*}
\end{proof}

We can further simplify the expression by the following unitary transformations, which will also be used in the right picture:
\begin{eqnarray*}
s_2&\mapsto& s_2-t_1,\\
s_1&\mapsto& s_1+\frac{s_2}{2},\\
t_1&\mapsto& t_1+\frac{s_2}{2},\\
\end{eqnarray*}
or equivalently
\Eq{f\ox g\mapsto f(s_1+\frac{s_2}{2},\frac{s_2}{2}-t_1)g(t_1+\frac{s_2}{2},t_2),}
so that the expression becomes:
\begin{eqnarray}
&=& \int_{\R+i\e_\t} \int_\R \int_C d\s d\a d\t  f(s_1-\a+\t,t_1-\s)g(s_2,t_2)\nonumber\\
&&\frac{G_b(-i\s)G_b(-i\a+i\s)G_b(\frac{Q}{2}+is_1-it_1+i\t)G_b(\frac{Q}{2}+is_1+it_1-i\s+i\t)}{G_b(Q+i\t)G_b(\frac{Q}{2}+is_1-it_1-i\a+i\s+i\t)G_b(\frac{Q}{2}+is_1+it_1-i\a+i\t)}\nonumber\\
&&e^{2\pi i\s(t_1-s_1-\t)}e^{2\pi is_1\t}e^{\pi is_2\t}A^{ib\inv (s_1+\frac{s_2}{2})}B^{ib\inv \t}\ox\hat{B}^{ib\inv\a}\hat{A}^{ib\inv (\frac{s_2}{2}-s_1-\t)}.\nonumber\\\label{leftcorep}
\end{eqnarray}
