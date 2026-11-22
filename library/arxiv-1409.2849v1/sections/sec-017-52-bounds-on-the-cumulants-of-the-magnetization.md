---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-017-52-bounds-on-the-cumulants-of-the-magnetization
section_title: "Bounds on the cumulants of the magnetization"
section_number: 5.2
pages: 41-48
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.968
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
As explained in the introduction, we now have to gather the estimates given by Theorem \ref{thm:jointcumulant} to get the asymptotics of the cumulants $\kappa^{(2r)}(M_n)$ of the magnetization. 


\subsubsection{Reordering of indices and compositions} Since the joint cumulants of spins have been computed for ordered spins $i_1\leq i_2\leq\ldots\leq i_{2r}$, in the right-hand side of the expansion
 $$\kappa^{(2r)}(M_n)=\sum_{i_1,\ldots,i_{2r}=1}^n\kappa(\sigma(i_1),\ldots,\sigma(i_{2r})),$$
we need to reorder the indices $i_1,\ldots,i_{2r}$, and take care of the possible identities between these indices. We shall say that a sequence of indices $i_1,\ldots,i_{r}$ has type $c=(c_1,\ldots,c_l)$ with the $c_i$ positive integers and $|c|=\sum_{i=1}^l c_i = r$ if, after reordering, the sequence of indices writes as
$$i_1'=i_2'=\ldots=i_{c_1}'<i_{c_1+1}'=i_{c_1+2}'=\cdots = i_{c_1+c_2}'<i_{c_1+c_2+1}' = \cdots.$$
Here, $i_k'$ stands for the $k$-th element of the reordered sequence. For instance, the sequence of indices $(3,2,3,5,1,2)$ becomes after reordering $(1,2,2,3,3,5)$, so it has type $(1,2,2,1)$. The type of a sequence of indices of length $r$ can be any composition of size $r$, and we denote $\cym_{r}$ the set of these compositions. Conversely, given a composition of size $r$ and length $l$, in order to construct a sequence of indices $(i_1,\ldots,i_r)$ with type $c$ and with values in $\lle 1,n\rre$, one needs:\vspace{1mm}
\begin{itemize}
\item  to choose which indices $i$ will fall into each class $(i_1',\ldots,i_{c_1}')$, $(i_2',\ldots,i_{c_1+c_2}')$, \emph{etc}.; there are
$$\binom{r}{c}=\frac{r!}{c_1!\,c_2!\cdots c_l!}$$
possibilities there.
\vspace{1mm}
\item and then to choose $1\leq j_1<j_2<\cdots <j_l \leq n$ so that $j_1=i_1'=\cdots=i_{c_1}'$, $j_2=i_2'=\cdots=i_{c_1+c_2}'$, \emph{etc}.\vspace{1mm}
\end{itemize}
As a consequence,
\begin{align*}\kappa^{(2r)}(M_n)&=\sum_{c \in \cym_{2r}} \sum_{1\leq j_1<j_2<\cdots <j_{\ell(c)} \leq n} \binom{2r}{c}\, \kappa\left(\sigma(j_1)^{c_1},\ldots,\sigma(j_{\ell(c)})^{c_{\ell(c)}}\right)\\
&=(-1)^{r-1}\sum_{c\in \cym_{2r}}\sum_{\delta \in \dym_{2r}^*}  \binom{2r}{c}\, C(\delta)\,B(n,c,\delta)
\end{align*}
where $C(\delta)=\prod_{i=1}^{2r-1} \delta_i$ is the quantity computed in the previous paragraph, and 
$$B(n,c,\delta)=\sum_{1\leq j_1<j_2<\cdots <j_{\ell(c)} \leq n} x^{\sum_{\{a<b\}\in \nu(\delta)} (i_b-i_a)},$$
the indices $i$ being computed from the indices $j$ according to the rule previously explained, namely,
\begin{align*}
j_1&=i_1=\cdots=i_{c_1};\\
j_2&=i_{c_1+1}=\cdots=i_{c_1+c_2};\\
\vdots & \qquad\qquad \qquad \vdots\\
j_{\ell(c)}&=i_{c_1+\cdots+c_{\ell(c)-1}+1}=\cdots=i_{2r}.
\end{align*}

\begin{example}
Suppose $r=1$. There are two compositions of size $2$, namely, $(2)$ and $(1,1)$, and one trivial tree with $0$ edge; therefore,
\begin{align*}
\kappa^{(2)}(M_n)&=B(n,(2),\bullet)+2\,B(n,(1,1),\bullet)\\ 
&=\sum_{ j_1 =1}^{ n} 1 \,\,\,\,+\,\,2\!\!\!\sum_{1\leq j_1<j_2 \leq n} x^{j_2-j_1}. \end{align*}
The double geometric sum has the same asymptotics as $\sum_{j_1 =1}^n\sum_{j_2=j_1+1}^\infty x^{j_2-j_1} = n\,\frac{x}{1-x},$
so $$\kappa^{(2)}(M_n) \simeq n\,\frac{1+x}{1-x} = n\,\E^{2\beta}.$$
\end{example}\bigskip

It is not hard to convince oneself that the approximation performed in the previous example can be done in any case, so that a correct estimate of $B(n,c,\delta)$ is $n\, B(c,\delta)$, with
$$B(c,\delta)=\sum_{0=j_1<j_2<\cdots<j_{\ell(c)}} x^{\sum_{\{a<b\}\in \nu(\delta)} (i_b-i_a)}.$$
In this new expression, the indices $j$ are unbounded (except the first one, fixed to $0$), and what we mean by approximation is that $$n\,B(c,\delta)= B(n,c,\delta)+O(1),$$ with a positive remainder corresponding to terms of the geometric series with indices larger than $n$. So:

\begin{proposition}\label{prop:firstestimate}
An upper bound, and in fact an estimate of $|\kappa^{(2r)}(M_n)|$ is
$$|\kappa^{(2r)}(M_n)|\leq n\,\sum_{c \in\cym_{2r}}\sum_{\delta \in \dym_{2r}^*} \binom{2r}{c}\,B(c,\delta)\,C(\delta).$$
\end{proposition}




\subsubsection{Computation of the functional $B$}
There is a simple algorithm that allows to compute $B(c,\delta)$ for any Dyck path $\delta$ and any composition $c$. Let us explain it with the path $\delta$ associated to the non-crossing pairing $\nu$ of Figure \ref{fig:restriction} and with the composition $c=(3,2,1,2,2)$. This composition $c$ corresponds to some identifications of indices, which we make appear on the diagram of the pairing $\nu$ as follows:
\figcap{identification.pdf}{Identifications of indices corresponding to the composition $c=(3,2,1,2,2)$.}
We now contract the green edges added above, obtaining thus: \vspace{-2mm}
\figcap{rho5.pdf}{Contraction of the diagram of a non-crossing partition along a composition.\label{fig:contracteddiagram}}
This new diagram corresponds to the following simplification of the sum $B(c,\delta)$:
\begin{align*}
B(c,\delta)&= \sum_{0=i_1=i_2=i_3<i_4=i_5<i_6<i_7=i_8<i_9=i_{10}} x^{i_{10}+i_9+i_8-i_7+i_6-i_5-i_4+i_3-i_2-i_1}\\
&=\sum_{0=i_1<i_4<i_6<i_7<i_9} x^{2i_9+i_5-2i_4-i_1}\qquad \text{because of the identities of indices};\\
&=\sum_{0=j_1<j_2<j_3<j_4<j_5} x^{(j_5-j_1)+(j_5-j_2)+(j_3-j_2)}\qquad \,\,\text{by relabeling the indices}.
\end{align*}
So, the new diagram, which we call the \emph{contraction of $\nu$ along $c$} and denote $\nu\!\downarrow_c$, can be read similarly as the previous diagrams of pairings, that is to say that
$$B(c,\delta)=\sum_{0=j_1<j_2<j_3<j_4<j_5} x^{(\nu(\delta))\downarrow_c},$$
where $x^{\nu\downarrow_c}$ stands for the product of factors $x^{b-a}$, $\{a<b\}$ running over the bonds of the contracted diagram $\nu\!\downarrow_c$.\bigskip

Given a contracted diagram $\rho=\nu\!\downarrow_c$ of length $\ell(c)$, denote $\delta_1(\rho)$ the number of bonds opened between $j_1$ and $j_2$; $\delta_2(\rho)$ the number of bonds opened between $j_2$ and $j_3$; $\delta_3(\rho)$ the number of bonds opened between $j_3$ and $j_4$; \emph{etc.} up to $\delta_{\ell(c)-1}(\rho)$. For instance, in the previous example, there is one bond opened between $j_1$ and $j_2$ (the one starting from $j_1$); $3$ bonds opened between $j_2$ and $j_3$ (the previous bond, which has not been closed, and the two bonds starting from $j_2$); and $2$ bonds opened between $j_3$ and $j_4$ and between $j_4$ and $j_5$. So $(\delta_1,\delta_2,\delta_3,\delta_4)=(1,3,2,2)$.

\begin{proposition}\label{prop:functionalB}
Set $\rho=(\nu(\delta))\!\downarrow_c$. One has
$$B(c,\delta)=\prod_{i=1}^{\ell(c)-1}\frac{x^{\delta_i(\rho)}}{1-x^{\delta_i(\rho)}}.$$
\end{proposition}

\begin{example}
Consider the previous contracted diagram $\rho_5$, and the corresponding sum $$B_5=\sum_{0=j_1<j_2<j_3<j_4<j_5} x^{(j_5-j_1)+(j_5-j_2)+(j_3-j_2)}.$$ We reduce inductively the size of the contracted diagram as follows. We first write
\begin{align*}B_5&=\sum_{0=j_1<j_2<j_3<j_4<j_5} x^{2(j_5-j_4)+(j_4-j_1)+(j_4-j_2)+(j_3-j_2)}\\
&=\left(\sum_{0=j_1<j_2<j_3<j_4} x^{(j_4-j_1)+(j_4-j_2)+(j_3-j_2)}\right)\left( \sum_{j_5=j_4+1}^\infty x^{2(j_5-j_4)} \right)\\
&=\frac{x^2}{1-x^2}\left(\sum_{0=j_1<j_2<j_3<j_4} x^{(j_4-j_1)+(j_4-j_2)+(j_3-j_2)}\right)=\frac{x^{\delta_4}}{1-x^{\delta_4}}\,B_4,
\end{align*}
where $B_4$ is the sum corresponding to the diagram $\rho_4$ which is obtained from $\rho_5$ by identifying $j_4$ and $j_5$:
\figcap{rho4.pdf}{Reduction of the diagram of Figure \ref{fig:contracteddiagram}.}
We can then do it again to go to size $3$:
\begin{align*}B_4&=\sum_{0=j_1<j_2<j_3<j_4} x^{2(j_4-j_3)+(j_3-j_1)+(j_3-j_2)+(j_3-j_2)}\\
&=\left(\sum_{0=j_1<j_2<j_3} x^{(j_3-j_1)+2(j_3-j_2)}\right)\left( \sum_{j_4=j_3+1}^\infty x^{2(j_4-j_3)} \right)\\
&=\frac{x^2}{1-x^2}\left(\sum_{0=j_1<j_2<j_3} x^{(j_3-j_1)+2(j_3-j_2)}\right)=\frac{x^{\delta_3}}{1-x^{\delta_3}}\,B_3,
\end{align*}
where $B_3$ is the sum corresponding to the diagram $\rho_3$ which is obtained from $\rho_4$ by identifying $j_3$ and $j_4$:
\figcap{rho3.pdf}{Further reduction of the diagram of Figure \ref{fig:contracteddiagram}.}
Two more operations yield similarly the factors $\frac{x^{\delta_2}}{1-x^{\delta_2}}$ and $\frac{x^{\delta_1}}{1-x^{\delta_1}}$.
\end{example}

\begin{proof}[Proof of Proposition \ref{prop:functionalB}]
The algorithm presented above on the example gives clearly a proof of the formula by induction on $\ell(c)$. Indeed, at each step of the induction, the term that is factorized is $$\sum_{j_{\ell(c)}=j_{\ell(c)-1}+1}^\infty x^{\delta_{\ell(c)-1}(j_{\ell(c)}-j_{\ell(c)-1})}=\frac{x^{\delta_{\ell(c)-1}}}{1-x^{\delta_{\ell(c)-1}}},$$
because $\delta_{\ell(c)-1}$ is the number of bonds ending at $j_{\ell(c)}$. Then, as for the other factor, one obtains it by replacing $j_{\ell(c)}$ by $j_{\ell(c)-1}$ in the sum $B(c,\delta)$, and this amounts to do the identification between $j_{\ell(c)-1}$ and $j_{\ell(c)}$ in the contracted diagram. This identification and reduction to lower length does not change the values $\delta_1,\ldots,\delta_{\ell(c)-2}$, so the formula is proven.
\end{proof}
\bigskip

We recall that a descent of a composition $c=(c_1,\ldots,c_\ell)$ is one of the integers $$c_1, c_1+c_2, c_1+c_2+c_3,\ldots,c_1+\cdots+c_{\ell-1}.$$ For instance, the descents of $c=(3,2,1,2,2)$ are $3$, $5$, $6$ and $8$. The set of descents $D(c)$ of a composition $c$ of size $r$ can be any subset of $\lle 1,r-1\rre$, so in particular, $\mathrm{card}\,\cym_r=2^{r-1}$. The contraction of diagrams along compositions presented at the beginning of this paragraph satisfies the rule:
$$\{\delta_1(\rho),\ldots,\delta_{\ell(c)-1}(\rho)\}=\{\delta_d,\,\,d \in D(c)\} \quad \text{if }\rho=(\nu(\delta))\!\downarrow_c.$$
So, $B(c,\delta)=\prod_{d \in D(c)} \frac{x^{\delta_d}}{1-x^{\delta_d}}$, and Proposition \ref{prop:firstestimate} becomes:

\begin{theorem}
An upper bound, and  in fact an estimate of $|\kappa^{(2r)}(M_n)|$ is
$$\frac{|\kappa^{(2r)}(M_n)|}{n}\leq\sum_{c \in \cym_{2r}} \sum_{\delta \in \dym_{2r}^*} A(c)\,B(c,\delta)\,C(\delta)$$
with $A(c)=\binom{2r}{c}$, $B(c,\delta)=\prod_{d \in D(c)}\frac{x^{\delta_d}}{1-x^{\delta_d}}$ and $C(\delta)=\prod_{i=1}^{2r-1}\delta_i$.
\end{theorem}\bigskip

\begin{example}
Suppose $r=2$. There is one Dyck path in $\dym_4^*$, with $C(\delta)=2$ since $\delta_1=\delta_3=1$ and $\delta_2=2$. The compositions of size $4$ are $(4)$, $(3,1)$, $(2,2)$, $(1,3)$, $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ and $(1,1,1,1)$; their contributions $A(c)\,B(c,\delta)$ are equal to
$$1,\,\,\frac{4x}{1-x},\,\,\frac{6x^2}{1-x^2},\,\,\frac{4x}{1-x},\,\,\frac{12x^3}{(1-x)(1-x^2)},\,\,\frac{12x^2}{(1-x)^2},\,\,\frac{12x^3}{(1-x)(1-x^2)},\,\,\frac{24x^4}{(1-x)^2(1-x^2)}.$$
So,
\begin{align*}|\kappa^{(4)}(M_n)| &\simeq 2n\,\left(1+\frac{8x}{1-x}+\frac{6x^2}{1-x^2}+\frac{12x^2}{(1-x)^2}+\frac{24x^3}{(1-x)(1-x^2)}+\frac{24x^4}{(1-x)^2(1-x^2)}\right)\\
&\simeq 2n \,\,\frac{(1+x)(1+4x+x^2)}{(1-x)^3}=n\,(3\,\E^{6\beta}-\E^{2\beta}).
\end{align*}
\end{example}




\subsubsection{Explicit bound on cumulants and the mod-Gaussian convergence}
By examining the asymptotics of the first cumulants written as rational functions in $x$, one is lead to the following result. Set 
$$P_r(x) = \left(\sum_{c \in \cym_{2r}} \sum_{\delta \in \dym_{2r}^*} A(c)\,B(c,\delta)\,C(\delta)\right)\,(1-x)^{2r-1}.$$
For instance, $P_1(x)=1+x$ and $P_2(x)=2\,(1+x)(1+4x+x^2)$. 

\begin{proposition}\label{prop:polynomial}
For every $r \geq 1$ and every $x \in (0,1)$, $$0 \leq P_r(x) \leq \frac{(2r)!}{r!}\,\frac{(2r-2)!}{(r-1)!}.$$
\end{proposition}

\begin{proof}For every composition $c$ and every path $\delta$, $B(c,\delta)\,(1-x)^{2r-1}$ is a non-negative and convex function of $x$ on $[0,1]$. Therefore, $0\leq P_r(x) \leq x\,P_r(0)+(1-x)\,P_r(1)$. When $x=1$, all the rational functions $B(c,\delta)\,(1-x)^{2r-1}$ vanish, except when $c$ has $2r-1$ descents, that is to say that $c=(1,1,\ldots,1)$. Then, $A(c)=(2r)!$, and
$$\lim_{x \to 1}\, B(c,\delta)= \prod_{i=1}^{2r-1} \frac{1}{\delta_i}=\frac{1}{C(\delta)}.$$
Therefore, 
$$P_r(1)=(2r)!\,(\card \,\dym_{2r}^*) = \frac{(2r)!}{r!}\,\frac{(2r-2)!}{(r-1)!}.$$
On the other hand, when $x=0$, all the rational functions $B(c,\delta)\,(1-x)^{2r-1}$ vanish, except when $c$ has no descent, that is to say that $c=(2r)$. Then, $A(c)=1$ and 
$$P_r(0)=Q(r)=\sum_{\delta \in \dym_{2r}^*}A(\delta).$$
Among all Dyck paths in $\dym_{2r}^*$, the one with the maximal product of values $G(\delta)$ is 
$(0,1,2,\ldots,r-1,r,r-1,\ldots,2,1,0)$. So,
$$
P_r(0) \leq r!\,(r-1)!\,(\card \,\dym_{2r}^*) = (2r-2 )! \leq P_r(1).
$$
It follows that $P_r(x) \leq x\,P_r(1)+(1-x)\,P_r(1)=P_r(1)$. 
\end{proof}
\bigskip

\begin{corollary}
For every $r$,
$$|\kappa^{(2r)}(M_n)|\leq n\,(2r-1)!!\,(2r-3)!! \,(\E^{2\beta}+1)^{2r-1}.$$
\end{corollary}

\begin{proof}
Indeed,
\begin{align*}
|\kappa^{(2r)}(M_n)| &\leq n \, \left(\sum_{c \in \cym_{2r}} \sum_{\delta \in \dym_{2r}^*} A(c)\,B(c,\delta)\,C(\delta)\right) = n\,\frac{P_r(x)}{(1-x)^{2r-1}} \\
&\leq n\,\frac{P_r(1)}{(1-x)^{2r-1}} = n\,\left(\frac{1}{1-x}\right)^{2r-1}\,\frac{(2r)!}{r!}\,\frac{(2r-2)!}{(r-1)!}. 
\end{align*}
Replacing $x$ by $\tanh \beta$ allows to conclude, and this gives another proof of Theorem \ref{thm:modgaussising}. We rewrite the logarithm of the Laplace transform of $n^{-1/4}M_n$ as
$$\sum_{r=1}^\infty \frac{\kappa^{(2r)}(M_n)}{(2r)!}\,z^{2r}\,n^{-r/2} = \frac{\kappa^{(2)}(M_n)\,z^2}{2n^{1/2}}+\frac{\kappa^{(4)}(M_n)\,z^4}{24n}+\sum_{r=3}^\infty \frac{\kappa^{(2r)}(M_n)}{(2r)!}\,z^{2r}\,n^{-r/2}.$$
The series on the right-hand side is smaller than
\begin{align*}\sum_{r=3}^\infty \frac{(2r-1)!!\,(2r-3)!!}{(2r)!} \, (\E^\beta+1)^{2r-1}\,z^{2r}\,n^{1-r/2} &\leq n^{-1/2}\sum_{r=3}^\infty ((\E^{2\beta} + 1)z)^{2r} \,n^{-(r-3)/2}\\
&\leq n^{-1/2}\,\,\frac{((\E^{2\beta} + 1)z)^{6}}{1-((\E^{2\beta} + 1)z)^{2}\,n^{-1/2}},
\end{align*}
so it goes uniformly to zero on every compact set of the plane. On the other hand, we have seen that $\kappa^{(2)}(M_n)=n\,\E^{2\beta} - O(1)$ and $-\kappa^{(4)}(M_n)=n\,(3\,\E^{6\beta}-\E^{2\beta}) - O(1)$, so we conclude that
$$\esper\!\left[\E^{z\,\frac{M_n}{n^{1/4}}}\right]\,\E^{-\frac{n^{1/2}\E^{2\beta}\,z^2}{2}}=\E^{-\frac{(3\,\E^{6\beta}-\E^{2\beta})\,z^4}{24}}\,\left(1+O(n^{-1/2})\right),$$
and this is indeed the content of Theorem \ref{thm:modgaussising}.
\end{proof}


\bibliographystyle{alpha}
