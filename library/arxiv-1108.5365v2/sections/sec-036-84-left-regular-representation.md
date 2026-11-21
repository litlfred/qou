---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-036-84-left-regular-representation
section_title: "Left regular representation"
section_number: 8.4
pages: 82-85
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.991
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:regular:left}
Now we apply the pairing to the left corepresentation \eqref{leftcorep}.

\begin{Thm} \label{ThmLeft}The representation of $U_q(\gl(2,\R))$ is equivalent to $$\int_\R\int_{\R^+}^\o+\cP_{\l,s_2/2}|S_b(Q+2i\l)|^2d\l ds_2\ox L^2(\R, dt_2),$$ where the representation space $\cP_{\l,s_2/2}=L^2(\R,ds_1)$ is defined in Theorem \ref{fundrep}.
\end{Thm}
\begin{proof} Recall that we have to multiply the expression by $\frac{G_b(Q+i\a)G_b(Q+i\t)}{(1-q^2)^{ib\inv (\a+\t)}}$ under the pairing. Also since the resulting expression is analytic in $\a, \t$ on the lower half plane, by taking $\a, \t$ to $0, -ib$ we mean the analytic continuation from $\R$ to the corresponding point, while respecting the contour of $\s$.

The pairing of $K_0$ and $K$ is then given by $\t=0, \a=0$.
The factor $$\frac{G_b(-i\s)G_b(-i\a+i\s)}{G_b(Q+i\t)} G_b(Q+i\a)G_b(Q+i\t)$$ becomes $\d(\s)$ which means we also set $\s=0$. Hence we obtain
\Eq{K_0\cdot f(s_1,t_1)g(s_2,t_2)= f(s_1,t_1)g(s_2,t_2)e^{-\frac{\pi b}{2}s_2},}
\Eq{K\cdot f(s_1,t_1)g(s_2,t_2)= f(s_1,t_1)g(s_2,t_2)e^{\pi bs_1}.}

The pairing of $E$ is given by $\t=-ib$ and $\a=0$, so that again $\s=0$ and is given by
\begin{eqnarray*}
E\cdot f(s_1,t_1)g(s_2,t_2)&=&-iq^{1/2} f(s_1-ib,t_1)g(s_2,t_2)\frac{e^{2\pi bs_1+\pi bs_2}e^{-\pi bs_1-\frac{\pi b}{2}s_2}}{1-q^2}\\
&=&-iq^{1/2}f(s_1-ib,t_1)g(s_2,t_2)\frac{e^{\pi bs_1+\frac{\pi b}{2}s_2}}{1-q^2},
\end{eqnarray*}
or simply
\Eq{E=\frac{i}{q-q\inv} e^{\frac{\pi b}{2}s_2} e^{\pi bs_1+2\pi bp_{s_1}}.}

Finally the pairing of $F$ is given by $\t=0, \a=-ib$. By Corollary \ref{delta} we have
\begin{eqnarray*}
&&\frac{G_b(-i\s)G_b(-i\a+i\s)}{G_b(Q+i\t)} G_b(Q+i\a)G_b(Q+i\t)\\
&=&e^{-\pi i\s^2-\pi Q\s}\frac{G_b(i\s-b)G_b(Q+b)}{G_b(Q+i\s)}\\
&=&-q^2\d(\s)-q^2\d(\s+ib),
\end{eqnarray*}
so that we obtain
\begin{eqnarray*}
F\cdot f(s_1,t_1)g(s_2,t_2)&=&iq^{-1/2}\frac{-q^2}{1-q^2}e^{\pi bs_1-\frac{\pi b}{2}s_2}\left(e^{2\pi b(t_1-s_1)}f(s_1+ib,t_1+ib)g(s_2,t_2) \right.\\
&&\left.+ f(s_1+ib,t_1)g(s_2,t_2)\frac{G_b(\frac{Q}{2}+is_1-it_1)G_b(\frac{Q}{2}+is_1+it_1)}{G_b(\frac{Q}{2}+is_1-it_1-b)G_b(\frac{Q}{2}+is_1+it_1-b)}\right).
\end{eqnarray*}
Using $\frac{G_b(ix)}{G_b(ix-b)} = (1-e^{2\pi ib(ix-b)})$, we expand the expression:
\begin{eqnarray*}
F&=&\frac{iq^{1/2}e^{-\frac{\pi b}{2}s_2}}{q-q\inv}\left(e^{-\pi b(s_1-2t_1)}e^{-2\pi b(p_{t_1}+p_{s_1})}+\right.\\
&&\left.(1+q\inv e^{-2\pi b(s_1-t_1)})(1+q\inv e^{2\pi b(-s_1-t_1)})e^{2\pi b s_1}e^{-2\pi bp_{s_1}}\right)\\
&=&\frac{ie^{-\frac{\pi b}{2}s_2}}{q-q\inv}\left(e^{-\pi b(2p_{s_1}-s_1)}+e^{-\pi b(2p_{s_1}+3s_1)}+(e^{2\pi bt_1}+e^{-2\pi bt_1}+e^{-2\pi b(p_{t_1}-t_1)})e^{-\pi b(2p_{s_1}+s_1)}\right),\\
\end{eqnarray*}
so that under multiplication by $e^{-\pi it_1^2}$ which changes $p_{t_1}\mapsto p_{t_1}+t_1$, we get

\Eq{F=\frac{ie^{-\frac{\pi b}{2}s_2}}{q-q\inv}\left(e^{-\pi b(2p_{s_1}-s_1)}+e^{-\pi b(2p_{s_1}+3s_1)}+\bC e^{-\pi b(2p_{s_1}+s_1)}\right),}
where $\bC$ depending only on $t_1$ is the operator defined in the previous section.
Therefore under the unitary transformation $\Phi$ defined previously, the representation is equivalent to
\begin{eqnarray*}
K_0&=&e^{\frac{\pi b}{2}s_2},\\
K&=&e^{\pi bs_1},\\
E&=&\frac{i}{q-q\inv} e^{\frac{\pi b}{2}s_2} e^{\pi bs_1+2\pi bp_{s_1}},\\
F&=&\frac{ie^{-\frac{\pi b}{2}s_2}}{q-q\inv}\left(e^{-\pi b(2p_{s_1}-s_1)}+e^{-\pi b(2p_{s_1}+3s_1)}+(e^{2\pi b\l}+e^{-2\pi b\l})e^{-\pi b(2p_{s_1}+s_1)}\right),
\end{eqnarray*}
where the measure $d\mu(\l)$ is now $|S_b(Q+2i\l)|^2d\l$.

Motivated from the expression of the corepresentation, we multiply the space by $G_b(\frac{Q}{2}+is_1-i\l)\inv$, and in effect changes the action of $e^{2\pi bp_{s_1}}$ to $(1+qe^{-2\pi bs_1+2\pi b\l})e^{2\pi bp_{s_1}}$. The action of $E$ and $F$ then become:

$$E=\frac{i}{q-q\inv}e^{\frac{\pi b}{2}s_2}(e^{\pi bs_1+2\pi bp_{s_1}}+e^{-\pi bs_1+2\pi b\l+2\pi bp_{s_1}}),$$
$$F=\frac{i}{q-q\inv}e^{-\frac{\pi b}{2}s_2}(e^{\pi bs_1-2\pi bp_{s_1}}+e^{-\pi bs_1-2\pi b\l-2\pi bp_{s_1}}).$$
Now we make the following changes of variables (unitary transformations):
\begin{eqnarray*}
\circ s_1\mapsto -s_1 &:& p_{s_1}\mapsto -p_{s_1},\\
\circ e^{\pi i s_1\l} &:& p_{s_1}\mapsto p_{s_1}-\frac{\l}{2},\tab p_{\l}-\frac{s_1}{2},\\
\circ e^{-\frac{\pi i}{2}s_1s_2}&:& p_{s_1}\mapsto p_{s_1}-\frac{s_2}{4},\tab p_{s_2}\mapsto p_{s_2}-\frac{s_1}{4}.\\
\end{eqnarray*}
In other words, the transformation:
$$f(s_1,t_1)g(\l,t_2)\mapsto f(-s_1,t_1)g(\l,t_2)e^{\frac{\pi i}{2}s_1(2\l-s_2)}.$$

Then the representation (denoted by $\cP_{\l,t_1}$) becomes:
\begin{eqnarray*}
K_0 &=& e^{\frac{\pi b}{2}s_2},\\
K&=& e^{-\pi bs_1},\\
E&=&\frac{i}{q-q\inv}(e^{\pi b(-2p_{s_1}-s_1+\l)}+e^{\pi b(-2p_{s_1}+s_1-\l)})\\
&=&\frac{i}{q-q\inv}(q^{1/2}e^{\pi b(s_1-\l)}+q^{-1/2}e^{-\pi b(s_1-\l)})e^{-2\pi bp_{s_1}}\\
&=&[\frac{Q}{2b}-\frac{i}{b}(s_1-\l)]_q e^{-2\pi bp_{s_1}},\\
F&=&\frac{i}{q-q\inv}(e^{\pi b(2p_{s_1}-s_1-\l)}+e^{\pi b(2p_{s_1}+s_1+\l)})\\
&=&\frac{i}{q-q\inv}(q^{-1/2}e^{\pi b(s_1+\l)}+q^{1/2}e^{-\pi b(s_1+\l)})e^{2\pi bp_{s_1}}\\
&=&[\frac{Q}{2b}+\frac{i}{b}(s_1+\l)]_q e^{2\pi bp_{s_1}}.\\
\end{eqnarray*}
\end{proof}
\begin{Rem} We note that there is a freedom of choice in multiplication by $G_b$ in the above action. In fact this precisely says that
\begin{eqnarray}
\cP_{\l,t}&\simeq& \cP_{-\l,t}\\
f(x)&\mapsto& \frac{G_b(\frac{Q}{2}+i\l-ix)}{G_b(\frac{Q}{2}-i\l-ix)}f(x)
\end{eqnarray}
as observed in \cite{PT2}.
\end{Rem}

Since the pairing is non-degenerate, we obtain the following important realization of the multiplicative unitary $\bW$:
\begin{Cor}\label{Wdecompose} As a corepresentation on $L^2(\R)$, $\bW$ is equivalent to
\Eq{\bW=\int_\R\int_{\R_+}^{\o+} T^{\l,t/2} d\mu(\l)dt,}
where $d\mu(\l)=|S_b(Q+2i\l)|^2 d\l$.
\end{Cor}

This is a generalization of Podle\'{s}-Woronowicz's definition \cite{PW} of a multiplicative unitary for a compact group
\Eq{u = {\sum_{\a\in \hat{G}}}^{\o+} u^\a,}
where $\hat{G}$ is the set of all (finite dimensional) irreducible unitary representation of $G$, and 
$$u^\a:V_\a\mapsto V_\a\ox G$$
is the irreducible corepresentation on some finite dimensional vector space $V_\a$. In particular, this defines the multiplicative unitary in a coordinate free canonical way.

Furthermore, by applying the transformations that was done in the proof of Theorem \ref{ThmLeft} to the expression \eqref{leftcorep}, and comparing the result with the expression of $T^{\l,t/2}$ given in \eqref{fundcorep}, we recover the ``6-9 relation" of $G_b$ that is first observed by Volkov \cite{Vo}. See Section \ref{sec:meaning} for further details.
