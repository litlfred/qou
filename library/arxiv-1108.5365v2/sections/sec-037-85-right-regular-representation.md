---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-037-85-right-regular-representation
section_title: "Right regular representation"
section_number: 8.5
pages: 85-87
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:regular:right}
Similarly by applying the pairing to the right regular corepresentation we obtain
\begin{Thm}\label{ThmRight} The right regular corepresentation is equivalent to $$ L^2(\R, ds_1)\ox\int_\R\int_{\R^+}^\o+ \cP_{\l,-s_2/2}|S_b(Q+2i\l)|^2d\l ds_2.$$
\end{Thm}
\begin{proof} We apply the pairing to \eqref{rightcorep} and get
{
\allowdisplaybreaks
\begin{eqnarray*}
K_0&=& e^{-\pi b\frac{s_2}{2}},\\
K&=&e^{\pi bt_2},\\
E&=&\frac{(-iq^{1/2})(-q^2)e^{-\pi iQb}}{1-q^2} e^{\frac{\pi b}{2}s_2}e^{-\pi bt_2}\left( e^{\pi b(2t_1+2t_2)}e^{2\pi b(-p_{t_1}+p_{t_2})}+\right.\\
&&\left. \frac{G_b(\frac{Q}{2}-it_1-it_2)G_b(\frac{Q}{2}+it_1-it_2)}{G_b(\frac{Q}{2}-it_1-it_2-b)G_b(\frac{Q}{2}+it_1-it_2-b)}e^{2\pi bp_{t_2}}\right)\\
&=&\frac{i}{q-q\inv}e^{\frac{\pi b}{2}s_2}e^{-\pi bt_2}\left(e^{\pi b(-2p_{t_1}+2t_1+2p_{t_2}+t_2)}+\right.\\
&&\left.q^{1/2}(1+q\inv e^{2\pi b(t_1+t_2)})(1+q\inv e^{2\pi b(-t_1+t_2)})e^{2\pi b p_{t_2}}\right)\\
&=&\frac{i}{q-q\inv}e^{\frac{\pi b}{2}s_2}\left(e^{\pi b(2p_{t_2}-t_2)}+e^{\pi b(2p_{t_2}+3t_2)}+(e^{2\pi b t_1}+e^{-2\pi bt_1}+e^{\pi b(-2p_{t_1}+2t_1)})e^{\pi b(2p_{t_2}+t_2)}\right),\\\\
F&=&\frac{iq^{-1/2}e^{\pi iQb}}{1-q^2}e^{\frac{\pi b}{2}s_2+\pi bt_2}e^{-2\pi bt_2-\pi bs_2}e^{-2\pi bp_{t_2}}\\
&=&\frac{i}{q-q\inv}e^{-\frac{\pi b}{2}s_2}e^{-\pi b(t_2+2p_{t_2})}.\\
\end{eqnarray*}
}

Again by shifting $p_{t_1}\mapsto p_{t_1}+t_1$ as in the left representation, the action of $E$ becomes
$$E=\frac{i}{q-q\inv}e^{\frac{\pi b}{2}s_2}\left(e^{\pi b(2p_{t_2}-t_2)}+e^{\pi b(2p_{t_2}+3t_2)}+\bC e^{\pi b(2p_{t_2}-t_2)}\right).$$

Hence under the unitary transformation $\Phi$, $E$ becomes
$$E=\frac{i}{q-q\inv}e^{\frac{\pi b}{2}s_2}\left(e^{\pi b(2p_{t_2}-t_2)}+e^{\pi b(2p_{t_2}+3t_2)}+(e^{2\pi b\l}+e^{-2\pi b\l}) e^{\pi b(2p_{t_2}-t_2)}\right).$$

Finally, the remaining transformation used in the left regular representation doesn't change these actions.
In exactly the same way if we apply:
\begin{eqnarray*}
multiplication&by& G_b(\frac{Q}{2}+i\l-it_2)\inv,\\
\circ t_2\mapsto -t_2&:& t_2\mapsto -t_2, p_{t_2}\mapsto -p_{t_2},\\
\circ e^{-\pi it_2 \l}&:& p_{\l}\mapsto p_{\l}-\frac{t_2}{2},p_{t_2}\mapsto p_{t_2}-\frac{\l}{2},\\
\circ e^{-\frac{\pi i}{2} s_2t_2}&:&p_{s_2}\mapsto p_{s_2}+\frac{t_2}{4},p_{t_2}\mapsto p_{t_2}+\frac{s_2}{4},\\
\end{eqnarray*}
that does not change the left representation either, it becomes:
\begin{eqnarray*}
K_0&=& e^{-\pi b\frac{s_2}{2}}\\
K&=&e^{-\pi bt_2}\\
E&=&\frac{i}{q-q\inv}(q^{\frac{1}{2}}e^{\pi b(t_2-\l)}+q^{-\frac{1}{2}}e^{-\pi b(t_2-\l)})e^{-2\pi bp_{t_2}}\\
&=&[\frac{Q}{2b}-\frac{i}{b}(t_2-\l)]_q e^{-2\pi bp_{t_2}}\\
F&=&\frac{i}{q-q\inv}(q^{-\frac{1}{2}}e^{\pi b(t_2+\l)}+q^{\frac{1}{2}}e^{-\pi b(t_2+\l)})e^{2\pi bp_{t_2}}\\
&=&[\frac{Q}{2b}+\frac{i}{b}(t_2+\l)]_q e^{2\pi bp_{t_2}}\\
\end{eqnarray*}
which is precisely the representation denoted by $\cP_{\l, -s_2/2}$.
\end{proof}


Combining Theorem \ref{ThmLeft} and \ref{ThmRight}, and note that all the transformations used are unitary, we conclude the main theorem:
\begin{Thm} \label{main} As a representation of $U_q(\gl(2,\R))_L \ox U_q(\gl(2,\R))_R$, 
\Eq{L^2(GL_q^+(2,\R))\simeq \int_\R^\o+\int_{\R^+}^\o+ \cP_{\l,s}\ox \cP_{\l,-s} |S_b(Q+2i\l)|^2 d\l ds}
and the equivalence is unitary.
\end{Thm}
In particular, we proved Ponsot-Teschner's claim in \cite{PT1} for $U_q(\sl(2,\R))$ by setting $s_2=0$ which corresponds to the determinant element $N=A\hat{A}$, as well as the action of the central element $K_0$.
