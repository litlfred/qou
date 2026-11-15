---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-020-71-number-of-connected-components-special-trace
section_title: "Number of connected components, special trace and change of variables"
section_number: 7.1
pages: 42-44
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.97
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
If $\beta$ is a braid on $n$ strands, then its closure $L$ is an oriented link. As before,
we denote
$\ell : B_n \to \Z$
the abelianization morphism which maps $\sigma_i$ to $1$.
We will use the following
classical fact :

\begin{lemma} \label{lemwrithe} If $\beta \in B_n$ and $L$ is the closure of $\beta$, then
$n+\ell(\beta) \equiv (\# L)  \mod 2$, where $\# L$ denote the number of
components of the link $L$.
\end{lemma}
\begin{proof}
Decomposing the projection
$\overline{\beta} \in \mathfrak{S}_n$ 
of $\beta$ under $B_n \to \mathfrak{S}_n$
into a product of disjoint cycles,
we get
$r$ cycles of even lengths $2 a_1,\dots,2 a_r$
and $s$ cycles of odd lengths $b_1,\dots,b_s$.
Then $\# L = r+s$, $n = 2 \sum a_i + \sum b_i \equiv s \mod 2$
and $\ell(\beta) \equiv r \mod 2$. This proves the claim.


\end{proof}


This provides a simple interpretation of the trace $t_n^{\dagger\dagger}$, with values in $S^{\dagger\dagger}$. Recall that $a^2 = 1$
inside $S^{\dagger \dagger}$.

\begin{prop} \label{propinvdagdag} If $\beta \in B_n$ and $L$ is the closure of $\beta$, then $t_n^{\dagger \dagger}(\beta) = a^{\# L}$.
\end{prop}
\begin{proof}
By construction, we have $t_n^{\dagger\dagger}(\beta) = a^n a^{\ell (\beta)} = a^{n + \ell(\beta)}$. Since $a^2 = 1$
the conclusion follows from lemma \ref{lemwrithe}.
\end{proof}

There is a well-known connection between `two versions' of the
Kauffman polynomial, one being connected to the
other through a sign depending on the number of connected
components of the link. In our formalism this is seen as
follows, using
the automorphism $\overline{E}$ 
of $\overline{BMW}_n \otimes_{\overline{R}} \overline{S} = BMW_n^+ \oplus BMW_n^-$. 
First recall that the values of $t_n^+$ and $t_n^-$ on braids belong to
a submodule $S_0 = \Q[a^{\pm 1},x^{\pm 1}]$ of $S_+$ and $S_-$, respectively.
Also recall that $S_0$ can be considered as a submodule of $\Q(\alpha,q)$
under $a \mapsto \alpha^{-2}$, $x \mapsto \alpha^{-1}(q\pm q^{-1})$.
We let $\tau_n^{\pm}$ denote the Markov traces $t_n^{\pm}$ viewed
as functions with values in the same ring $S_0$.

We can now show how this well-known connection between the two versions
fits into our setting. This connection can be stated as follows (see e.g. \cite{LICKO}, p. 177).

\begin{prop} \label{invlcorrespBMWplusmoins} If $\beta$ is a braid on $n$ strands whose closure is the link $L$,
then 
$$
 \left.  \tau_n^-
  (\beta)
   \right|_{\stackrel{a\mapsto -a}{x \mapsto -x}} = (-1)^{\# L -1} \tau_n^+(\beta)$$
where we identified $\beta$ with its image in $BMW_n^+$ on the LHS, and its image in $BMW_n^-$ in the RHS,
and $\# L$ denotes the number of
components of $L$.
\end{prop}
\begin{proof}
The LHS can be viewed inside $S_+$ as $\eta \circ t_n^- \circ \overline{E}( \overline{E}(\beta))$, which is equal to
$(-1)^{n-1} t_n^+(\overline{E}(\beta))$ by corollary \ref{cortnplusettnmoins}. 
Now $(-1)^{n-1} t_n^+(\overline{E}(\beta)) = (-1)^{n-1} (-1)^{\ell(\beta)} t_n^+(\beta)$
where $\ell : B_n \to \Z$ denotes as before the abelianization
morphism.
The conclusion then follows from the identity
$n+\ell(\beta) \equiv (\# L)  \mod 2$, proved in lemma \ref{lemwrithe}.
\end{proof}







\subsection{The special case $a = \pm 1$, $b = \mp j$, $c = \mp j^2$}

Recall that $j$ denotes a primitive $3$-root of $1$. We have $y = 1$, $x = a$. In this case, the link invariant afforded
by the Kauffman trace $t_n^+$ is constant equal to 1 (that is, it takes the value 1 on every link), see \cite{LICKO} p. 186, table 16.3 row A,
and this is reproved by the observation that, in this case, $\delta_K = a$ hence $t_n^K = t_n^{\dagger\dagger}$.
For $y= 1$ and $x = a = -1$, according to \cite{LICKO} p. 186, table 16.3 row D, the link invariant associated to $t_n^H$
maps a link $L$ to $(\ii \sqrt{2})^{d_2(T(L))}$, where $T(L)$ is the 3-fold cyclic cover of $S^3$ branched over $L$,
and $d_2(T(L)) = \dim_{\mathbbm{F}_2} H_1(T(L),\mathbbm{F}_2)$. When $y=1$, $x=a=1$, we consider the automorphism $\varphi$
of the group algebra of the braid group defined by $s_i \mapsto s_i^{-1}$, and show that, as in the proposition \ref{invlcorrespBMWplusmoins}  and
corollary \ref{cortnplusettnmoins}, the formula
$T_n(b) = (-1)^{n-1} t_n(\varphi(b))$ induces a bijection between the traces factorizing through the two Hecke algebras
with quadratic conditions $s^2 + s + 1 = 0$ and $s^2 - s+1 = 0$, hence the two invariants are related by multiplication by $(-1)^{\# L -1}$.
As a consequence we get the general formula $t_n^H(\beta) = a^{\# \hat{\beta} - 1} (\ii \sqrt{2})^{d_2(T(L))}$.






We are looking for a Markov trace $t_n^0$ on $\WBMW_n \otimes_R R/(a=\pm 1, b= \mp j, c = \mp j^2)$
such that $t_3^0(1) = t_3^0(s_1) = 0$ and $t_3^0(s_1s_2) = 1$. This implies $t_3^0(s_1^{\alpha} s_2^{\beta}) = 1$ for all $\alpha,\beta \in \{-1,1 \}$.


We checked by computer that there is a (necessarily unique) extension of $t_3^0$ to $F_4$ satisfying the
Markov property. If there is an obstruction to these traces to genuine Markov traces one
thus needs to look for it on at least 5 strands.

\begin{conj} The trace $t_3^0$ can be extended to a Markov trace on the tower $(F_n)$.
\end{conj}

Assuming that conjecture, we get that
the corresponding link
invariant would take the value $a^n \times(4.2^n - 4 - 2n)$ on the $(n+3)$-components unlink.





\subsection{The special case $a =b=c= \pm 1$}

We have $y = 1$, $x = 2a=\pm2 $. In this case, $\delta_H = a$, hence $t_n^H$ coincides
with $t_n^{\dagger\dagger}$ (see also \cite{LICKO} table 6.3, row A), and, for $a=y=1$,
the Kauffman invariant maps a link $L$ to $(\det L)^2$, where $\det L = \Delta_{L}(-1) = \nabla_L(0)$
(see \cite{LICKO} table 6.3, row B). Since this invariant is afforded by $t_n^+$, and because of proposition \ref{invlcorrespBMWplusmoins}, this implies
that $t_n^K(\beta) = a^{\# \hat{\beta} -1} (\det \hat{\beta} )^2$ for every braid $\beta \in B_n$.


 We are looking for a Markov trace $t_n^0$ on $\WBMW_n \otimes_R R/(a=b=c=\pm 1)$
such that $t_3^0(1) = 1$, $t_3^0(s_1) = t_3^0(s_1s_2) = 0$. This implies $t_3^0(s_1^{\alpha} s_2^{\beta}) = 0$ for all $\alpha,\beta \in \{-1,1 \}$.
By theorem \ref{theoexistencetracedeltanul} we know that such a Markov trace exists, factoring through $\overline{F}_n$.
Moreover, by induction we easily get that $t_{n+3}^0(1) = a^n \times(n+1)$, and therefore the
corresponding link invariant takes the value $a^n \times(n+1)$ on the $(n+3)$-components unlink.
Finally, we can easily identify its restriction to the subalgebra $\widetilde{TL}_n(0)$, as follows.

\begin{prop} \label{proptracet0x2a} There exists a family of traces 
$t_n : \widetilde{TL}_n(0) \to A_0$
satisfying $t_{n}(C) =a^{n}$, $t_1(1) = 0$, $t_n(1) = (n-2)a^{n+1}$ if $n \geq 2$,
that would coincide with the restriction of $t_n^0$ to $\widetilde{TL}_n(0)$
if $(t_n^0)$ is well-defined.
\end{prop}
\begin{proof} Letting $u_n = - a^n$,$v_1 = 0$, $v_n = (n-2) a^{n+1}$
in proposition \ref{proptracesTL0} provides a family of traces $t_n$. We know prove that
$t_n$ necessarily coincides with the restriction of the putative Markov trace $t_n^0$.
We have $t_n(1) = t_n^0(1)$ for $n \leq 3$ and, by proposition \ref{proprelrecutraceFn} (iii), 
$t_{n+3}^0(1) = 2a t_{n+2}^0(1) - t_{n+1}^0(1)$ since, we know that $t_n^0$ factors through $(F_n)$ by theorem \ref{theoisomddaggerFn}.
Because of this, we have $t_n^0(1) = t_n(1)$ for all $n$. By proposition \ref{proprelrecutraceFn} we also get $t_n(C) = t_n^0(C)$
for all $n$. From the relation $e_i = (s_i+s_i^{-1})/2 - a$ and the Markov property we get $t_n^0(e_i) = t_n(e_i)$ for all $i$.
It is well-known that the Temperley-Lieb algebra admits a basis made of words in the $e_i$ which has the property
that the $e_i$ of maximal index appears exactly once. Let us consider such a basis element of $\widetilde{TL}_n$ of the form $Ae_iB$ with $A,B$ words in the $e_j$ for $j < i$.
Expanding $e_i$ as before, we get from the Markov property that $t_{n+1}^0(A e_i B) = t_n^0(A B) - at_{n+1}^0(AB)$.
By induction on the length of the words in the $e_i$'s, we get from this formula that $t_{n+1}^0(Ae_i B) = 0$  as soon as $A$ or $B$
has length $\geq 1$, and therefore $t_n^0$ coincides on $t_n$ on every basis element of $\widetilde{TL}_n(0)$, which proves the claim. 



\end{proof}
