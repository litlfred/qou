---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-005-trace-functional-and-a-pairing-on-hws
section_title: "Trace functional and a pairing on H(W,S)."
section_number: null
pages: 3-4
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.882
latex_coverage_ratio: 0.978
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
Let $x \mapsto \overline{x}$ be the Kazhdan-Lusztig involution on $\He(W,S)$. It is a $\mathbb{Q}$-algebra involution, defined by the assignments $\overline{v} = v^{-1}, \overline{t_w} = t_{w^{-1}}^{-1}.$ Let $i:\He(W,S)$ stand for the $\mathcal{A}$-linear algebra anti-involution defined by $i(t_w) = t_{w^{-1}}$. 

For $h \in \He(W,S), x \in W,$ let $h_x$ stand for the $t_x^{-1}$-coefficient of $h$ in the basis $t_w^{-1},$ where $w$ runs through $W$. Let $\tau: \He(W,S) \to \mathcal{A}$ be a functional defined by  $\tau(h) = h_e,$ where $e \in W$ is the unit.  For $h, h' \in \He(W,S)$, define a pairing $\langle h, h' \rangle = \tau(i(\overline{h})h')$. We have the following standard proposition, see, for example, \cite[Chapter 8]{geck2000characters}.
\begin{proposition}[]
  \label{sec:trace-funct-pair}
  The functional $\tau$ and the pairing $\langle\, , \rangle$ satisfies the following properties.
  \begin{enumerate}[label=(\alph*)., ref=(\alph*)]
  \item The functional $\tau$ is an $\mathcal{A}$-linear trace on $\He(W,S),$ that is $\tau(hh') = \tau(h'h).$
  \item The pairing $\langle\, , \rangle$ is $\mathcal{A}$-antilinear in the first argument, $\mathcal{A}$-linear in the second argument and satisfies the orthogonality relation
    \(   \langle t_{w_1} , t^{-1}_{w_2} \rangle = \delta_{w_1, w_2^{-1}}.
    \)
   \item \label{item:3} We have \(\langle h_1h_2, h_3 \rangle = \langle h_1, h_3 i(\overline{h_2})\rangle = \langle h_2,  i(\overline{h_1})h_3\rangle\) for any $h_1, h_2, h_3 \in \He(W,S).$
  \end{enumerate}
\end{proposition}
We will use the following straightforward corollary of this proposition repeatedly.
\begin{corollary}
  \label{sec:trace-funct-pair-1}
  Let $(W',S')$ be a parabolic subgroup of $W$. Assume that $x, y \in \He(W',S') \subset \He(W,S)$, and assume that $z \in \mathrm{span}_\mathcal{A}\langle t_w, w \in W\backslash W'\rangle$ (resp. $z \in \mathrm{span}_\mathcal{A}\langle t_w^{-1}, w \in W\backslash W'\rangle$). Then $\langle xz, y \rangle = \langle zx, y \rangle = 0$ (resp. $\langle x, yz \rangle = \langle x, zy \rangle =0$).
\end{corollary}
