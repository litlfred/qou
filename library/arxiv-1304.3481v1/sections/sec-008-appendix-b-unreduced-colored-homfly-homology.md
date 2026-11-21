---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-008-appendix-b-unreduced-colored-homfly-homology
section_title: "Appendix B. Unreduced colored HOMFLY homology"
section_number: null
pages: 69-75
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.971
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\subsection{General structure}
As explained in Section \ref{sec:geomphys}, the unreduced $\lambda$-colored homology $\bar{\CH}^{\lambda}(K)$ for any rectangular diagram $\lambda$ and any knot $K$ is a free module over the unreduced $\lambda$-colored homology of the unknot $\bar{\CH}^{\lambda}(U)$. Therefore, for every knot $K$ the unreduced homology $\bar{\CH}^{\lambda}(K)$ is determined by the reduced homology ${\CH}^{\lambda}(K)$
and the unreduced homology of the unknot $\bar{\CH}^{\lambda}(U)$. In terms of the corresponding Poincare polynomials we have:
\be\label{simprel}
\bar{\CP}^{\lambda}(K)={\CP}^{\lambda}(K)\bar{\CP}^{\lambda}(U).
\ee
Hence, the unreduced colored homology  is determined by the reduced one.

In order to simplify the presentation, we focus on the symmetric representations $\lambda=S^r$. 

Some of the properties of reduced homology extend to the unreduced case: these include the existence and the behaviour of the positive colored differentials and the totally refined exponential growth property. By (\ref{simprel}) these properties will follow from the fact the unreduced homology of the unknot satisfies these properties.  

The unreduced colored homology of the unknot is described in Section \ref{sec:unknot} in terms of the bosonic and fermionic generators. Their expicit $(a,Q,t_r,t_c)$-gradings have been obtained, which gives the following Poincare polynomial of the tilde-version of the unreduced $S^r$-colored homology of the unknot:
\be
\tilde{\bar{\CP}}^{S^r}(U)(a,Q,t_r,t_c)=a^{-r}Q^{r}\prod_{i=1}^r \frac{1+a^2t_rt_c^{2i-1}}{1-Q^2t_c^{2i-2}}.
\ee
In ``standard" $(a,q,t_r,t_c)$-gradings we have (the same convention, $Q=q+t_r-t_c$, holds for the symmetric representations as in the case of the reduced homology):
\be
{\bar{\CP}}^{S^r}(U)(a,q,t_r,t_c)=a^{-r}q^{r}\prod_{i=1}^r \frac{1+a^2q^{2i-2}t_rt_c^{2i-1}}{1-q^{2i}t_c^{2i-2}}.
\ee

The degrees of the positive colored differentials are as in the reduced case:
\be
(a,q,t_r,t_c)[d^{col}_{1|k}]=(-2,2(1-k),-1,-2k-1),\quad 0\le k <r.
\ee
They also have the ``colored" property, i.e. we have:
\be\label{unredcol}
H^*(\bar{\CH}^{S^r}(K),d^{col}_{1|k})\cong \bar{\CH}^{S^k}(K),\quad 0\le k <r.
\ee
Indeed, the last follows from the following Lemma which shows that (\ref{unredcol}) holds for the unknot and with the re-gradings in the corresponding isomorphisms being exactly the same as for the reduced homology (Section \ref{coldif}):

\begin{lemma}
For all nonnegative integers $r$ and $k$, with $k<r$, we have that the following holds
\be
\tilde{\bar{\CP}}^{S^r}(U)(a,Q,t_r,t_c)-\tilde{\bar{\CP}}^{S^k}(U)(a,Qt_c^{r-k},t_r,t_c)=
(1+a^{-2}Q^2t_r^{-1}t_c^{-2k-1})X,
\ee
for some Laurent polynomial $X(a,Q,t_r,t_c)$ whose all coefficients are nonnegative  integers, i.e. $X\in \Z_+[a^{\pm 1},Q^{\pm 1},t_r^{\pm 1},t_c^{\pm 1}]$. 
\end{lemma}
\textit{Proof:} Straightforward computation.\\

The totally refined exponential growth property also holds for the unreduced homology of the unknot. Indeed:
\be
\tilde{\bar{\CP}}^{S^r}(U)(a,Q,t_r=t,t_c=1)=\prod_{i=1}^r \frac{1+a^2t}{1-Q^2}=\left(\tilde{\bar{\CP}}^{\tableau1}(U)(a,Q,t_r=t,t_c=1)\right)^r.
\ee

\vskip 0.25cm

On the other hand there are some differences between the reduced and unreduced homology of any knot.

The first clear distinction from the reduced case is that the unreduced homology is infinite-dimensional, since such is the unreduced homology of the unknot. In particular there can be no symmetry that inverts the $Q$, or $q$-grading and therefore the selfsymmetry is not satisfied for the unreduced homology. Consequently, there are no negative colored differentials in this case (recall that selfsymmetry exchanges positive and negative colored differentials).

The second distinction from the reduced homology case is that all differentials $d_{n|0}$, for $n>0$, are nontrivial now, even for the unknot. This is the reason why there is no such a simple relation like (\ref{simprel}) between the unreduced and reduced $sl(n)$ homology.
In the next section we compute $sl(n)$ colored HOMFLY homology for some simple knots.


\subsection{$sl(n)$ colored HOMFLY homology}

The unreduced $(sl(n),S^r)$-colored homology of a knot $K$, denoted $\bar{\CH}^{sl(n),S^r}(K)$, is obtained as the homology of $\bar{\CH}^{S^r}(K)$ with respect to $d_{n|0}$, followed by collapsing of grading by setting $a=q^n$. We observe $\bar{\CH}^{S^r}(K)$ here as triply-graded theory in $(a,q,t_c)$-gradings, and also to simplify the notation we denote $t_c$ simply by $t$.
Therefore, $\bar{\CH}^{sl(n),S^r}(K)$ becomes doubly-graded theory in $(q,t)$-degrees.

Unlike the reduced homology case, here all differentials $d_{n|0}$, with $n>0$, are highly nontrivial, even for the unknot. Below we compute $sl(2)$ homologies for the fundamental and the second-symmetric representation of the unknot, trefoil and the figure-eight knot.

The $(a,q,t)$-degrees of the $sl(n)$ differentials, $d_{n|0}$, $n>0$, are as for the reduced homology:
\be
(a,q,t)[d_{n|0}]=(-2,2n,-1),\quad n>0.
\ee

For all three knots we assume that $d_{n|0}$ is such that it cancels all pairs of generators
of $\bar{\CH}^{S^r}(K)$ whose $(a,q,t)$-degrees differ by $(-2,2n,-1)$.


\subsubsection{Unknot}
In the fundamental representation, we have that the Poincare polynomial of the unreduced uncolored HOMFLY homology is given by:
\[
{\bar{\CP}}^{\tableau1}(U)(a,q,t)=a^{-1}q \frac{1+a^2t}{1-q^{2}}.
\]
Then the homology with respect to $d_{n|0}$ is finite-dimensional  for any $n$:
\be
({\bar{\CH}}^{\tableau1}(U),d_{n|0})=a^{-1}q(1+q^2+\ldots+q^{2(n-1)}).
\ee
Finally, after collapsing the tri-grading by setting $a=q^n$, we get the familiar 
expression for the uncolored $sl(n)$ homology of the unknot:
\be
{\bar{\CP}}^{sl(n),\tableau1}(U)(q,t)=({\bar{\CH}}^{\tableau1}(U),d_{n|0})_{|_{a=q^n}}=q^{1-n}+q^{3-n}+\ldots+q^{(n-1)}.
\ee

The $S^2$-colored unreduced homology of the unknot is given by:
\be\label{s2un}
\bar{\CP}^{\tableau2}(U)=a^{-2}q^2\frac{(1+a^2t)(1+a^2q^2t^3)}{(1-q^2)(1-q^4t^2)}.
\ee
To simplify the further computation of the homology with respect to $d_{2|0}$ in terms of the Poincare polynomial, we say that $P_1$ is equal to  $P_2$ {\it modulo} $d_{2|0}$ if $P_1-P_2=(1+a^{-2}q^4t^{-1}) Y$ for some Laurent polynomial $Y$ in variables $a,q$ and $t$ whose all coefficients are nonnegative integers.

Then by using the result from the uncolored case, we have that modulo $d_{2|0}$ the expression (\ref{s2un}) equals to:
\[
a^{-2}q^2(1+q^2)\frac{1+a^2q^2t^3}{1-q^4t^2}=(1+q^2+q^4t^2\frac{1+a^2t}{1-q^4t^2})+
(1+a^{-2}q^4t^{-1})\frac{a^2q^2t^3}{1-q^4t^2}.
\]
Therefore:
\be
({\bar{\CH}}^{\tableau2}(U),d_{2|0})=a^{-2}q^2(1+q^2+q^4t^2\frac{1+a^2t}{1-q^4t^2}),
\ee
and so 
\be
{\bar{\CP}}^{sl(2),\tableau2}(U)(q,t)=({\bar{\CH}}^{\tableau2}(U),d_{2|0})_{|_{a=q^2}}=q^{-2}+1+q^2t^2\frac{1+q^4t}{1-q^4t^2}.
\ee


\subsubsection{Trefoil}
For the trefoil, we have:
\be
\bar{\CP}^{\tableau1}(3_1)={\CP}^{\tableau1}(3_1)\bar{\CP}^{\tableau1}(U)=(a^2q^{-2}+a^2q^2t^2+a^4t^3)a^{-1}q\frac{1+a^2t}{1-q^2}.
\ee
Now after taking the homology with respect to $d_{2|0}$ which cancels all pairs 
of generators which differ in $(a,q,t)$-degree by $(-2,4,-1)$, we are left with
\be
(\bar{\CH}^{\tableau1}(3_1),d_{2|0})=a(q^{-1}+q+q^3t^2)+a^3q^3t^3,
\ee
which after setting $a=q^2$ gives 
\[
\bar{\CP}^{sl(2),\tableau1}(3_1)(q,t)=(\bar{\CH}^{\tableau1}(3_1),d_{2|0})|_{a=q^2}=q+q^3+q^5t^2+q^9t^3,
\]
which equals precisely the free part of the
(unreduced) Khovanov homology of the trefoil.\\

For the second-symmetric representation, we have:
\be\label{gl31}
\bar{\CP}^{\tableau2}(3_1)={\CP}^{\tableau2}(3_1)\bar{\CP}^{\tableau2}(U),
\ee
where the reduced homology of the trefoil was computed in Section \ref{sec:examples}:
\be
{\CP}^{\tableau2}(3_1)=
a^4(q^{-4}+q^2t^4+q^4t^6+q^8t^8)+a^6(t^5+q^2t^7+q^6t^9+q^8t^{11})+a^8q^6t^{12}.
\ee



As we have seen above, the Poincare polynomial of the unknot $\bar{\CP}^{\tableau2}(U)$
modulo $d_{2|0}$ equals 
\be\label{sl2s2u}
(\bar{\CH}^{\tableau2}(U),d_{2|0})=a^{-2}(q^2+q^4+q^6t^2\frac{1+a^2t}{1-q^4t^2}).
\ee
As for the the reduced $S^2$-colored Poincare polynomial of the trefoil, ${\CP}^{\tableau2}(3_1)$, we split it according to the canceling differential $d^{col}_{0|2}$:
\be
{\CP}^{\tableau2}(3_1)=(1+a^2q^4t^5)(a^4q^{-4}+a^4q^2t^4+a^4q^4t^6+a^6q^2t^7)+a^4q^8t^8.
\ee
Multiplying the factor $(1+a^2q^4t^5)$ with the RHS of (\ref{sl2s2u}) gives:
\begin{eqnarray*}
&&(1+a^2q^4t^5)a^{-2}(q^2+q^4+q^6t^2\frac{1+a^2t}{1-q^4t^2})=\\
&&=(1+a^2q^4t^5)a^{-2}(q^2+q^4)+a^{-2}q^6t^2(1+a^2q^4t^5)\frac{1+a^2t}{1-q^4t^2})=\\
&&=(1+a^2q^4t^5)a^{-2}(q^2+q^4)+\\
&&\quad +\, a^{-2}q^6t^2(1+a^2t+q^4t^2+a^2q^4t^3+(1+a^{-2}q^4t^{-1})a^2q^4t^5\frac{1+a^2t}{1-q^4t^2})=\\
&&=a^{-2}q^2(1+q^2+q^4t^2+a^2q^4t^3+a^2q^6t^5+a^2q^8t^5)+\\
&&\quad\quad + \,(1+a^{-2}q^4t^{-1})(q^6t^5+q^{10}t^7\frac{1+a^2t}{1-q^4t^2}).
\end{eqnarray*} 
Therefore, after replacing this in (\ref{gl31}), we have that $\bar{\CP}^{\tableau2}(3_1)$ modulo $d_{2|0}$ equals:
\begin{eqnarray*}
&\!\!\!\!\!\!\!a^{-2}q^2(1+q^2+q^4t^2+a^2q^4t^3+a^2q^6t^5+a^2q^8t^5)(a^4q^{-4}+a^4q^2t^4+a^4q^4t^6+a^6q^2t^7)+\\
&\quad \quad + a^2q^8t^8 (q^2+q^4+q^6t^2\frac{1+a^2t}{1-q^4t^2}).
\end{eqnarray*}
By canceling all possible remaining pairs of generators by $d_{2|0}$ we get:
\begin{eqnarray*}
(\bar{\CH}^{\tableau2}(3_1),d_{2|0})\!\!&\!=\!&\!\! a^2(q^{-2}+1)+a^2q^2t^2+a^4q^2t^3\!+\!a^2(q^4+q^6)t^4\!+\!a^4(q^4+q^6)t^5+\\
&&\,\,+\,a^4(q^6+q^8)t^7+a^2q^{10}t^8+a^4q^{10}t^9+a^4q^{12}t^{11}+a^6q^{12}t^{12}+\\
&&\quad\quad +a^2q^6t^6(1+q^2+q^4t^2\frac{1+a^2t}{1-q^4t^2}).
\end{eqnarray*}
Finally, by setting $a=q^2$, we obtain the following $(sl(2),S^2)$-colored homology of the trefoil:
\begin{eqnarray*}
\CP^{sl(2),\tableau2}(3_1)(q,t)&=&(\bar{\CH}^{\tableau2}(3_1),d_{2|0})_{|_{a=q^2}}=\\
&&\, = (q^2+q^4)+q^6t^2+q^{10}t^3+(q^{8}+q^{10})t^4+(q^{12}+q^{14})t^5+\\
&&\quad + (q^{14}+q^{16})t^7+q^{14}t^8+q^{18}t^9+q^{20}t^{11}+q^{24}t^{12} +\\
&&\quad + q^{10}t^6 (1+q^2+q^4t^2 \frac{1+q^4t}{1-q^4t^2}).
\end{eqnarray*}
We note that this result for the free part of the homology coincides (up to an overall shift) with the one obtained in \cite{CHKrushkal}. \footnote{Note that the $so(3)$ homology corresponding to the fundamental representation that is computed in \cite{CHKrushkal} is indeed isomorphic to the homology $\CH^{sl(2),\tableau2}$, due to the well-known isomorphism between the fundamental (vector) representation of $so(3)$ and the second-symmetric representation of $sl(2)$.}\\



\subsubsection{Figure-eight knot}
Similarly, for the figure-eight knot, we have 
\be
\bar{\CP}^{\tableau1}(4_1)={\CP}^{\tableau1}(4_1)\bar{\CP}^{\tableau1}(U)=(a^2t^2+q^{-2}t^{-1}+1+q^2t+a^{-2}t^{-2})a^{-1}q\frac{1+a^2t}{1-q^2}.
\ee
After taking homology with respect to $d_{2|0}$ (i.e. modulo $(1+a^{-2}q^4t^{-1})$), we get
\be
(\bar{\CH}^{\tableau1}(4_1),d_{2|0})=a^2qt^2+q^{-1}(t^{-1}+1)+q(1+t)+a^{-2}q^{-1}t^{-2},
\ee
and after setting $a=q^2$, we are left with 
\[
(\bar{\CH}^{\tableau1}(4_1),d_{2|0})_{|_{a=q^2}}=q^5t^2+qt+q+q^{-1}+q^{-1}t^{-1}+q^{-5}t^{-2},
\]
which is the free part of the
(unreduced) Khovanov homology of the figure-eight knot.\\


For the second-symmetric representation we have: 
\be\label{gl41}
\bar{\CP}^{\tableau2}(4_1)={\CP}^{\tableau2}(4_1)\bar{\CP}^{\tableau2}(U),
\ee
where the reduced $S^2$-homology is already computed in Section \ref{sec:examples} 
\begin{eqnarray*}
{\CP}^{\tableau2}(4_1)&=&1+(1+q^2t^2)a^{-2}q^{-2}t^{-4}(1+a^{2}q^{-2}t)(1+a^{2}q^{4}t^{5})+\\
&&\quad +
a^{-4}q^{-4}t^{-8}(1+a^{2}q^{-2}t)(1+a^{2}t^{3})(1+a^{2}q^{4}t^{5})(1+a^{2}q^{6}t^{7}).
\end{eqnarray*}
In the same way as above for the trefoil, after grouping all terms with the factor $1+a^2q^4t^5$ and multiplying with the RHS of (\ref{sl2s2u}), we get that modulo $d_{2|0}$ the polynomial
$\bar{\CP}^{\tableau2}(4_1)$ equals to:
\begin{eqnarray*}
&\!\!\!\!\!\!a^{-2}q^2(1\!+\!q^2\!+\!q^4t^2\!+\!a^2q^4t^3\!+\!a^2q^6t^5\!+\!a^2q^8t^8)((1+q^2t^2)(1+a^{2}q^{-2}t)a^{-2}q^{-2}t^{-4}+\\
&\quad +a^{-4}q^{-4}t^{-8}(1+a^{2}q^{-2}t)(1+a^{2}t^{3})(1+a^{2}q^{6}t^{7}))+\\
&\quad \quad + a^{-2}(q^2+q^4+q^6t^2\frac{1+a^2t}{1-q^4t^2}).
\end{eqnarray*}
Finally, by canceling by $d_{2|0}$ all possible remaining pairs of generators we get:
\begin{eqnarray*}
(\bar{\CH}^{\tableau2}(4_1),d_{2|0})&=& 
a^{-4}(t^{-4}+(q^2+q^4)t^{-2}+q^6)+ \\
&&\quad\quad + a^{-2}(t^{-3}+2q^2t^{-1}+q^4(t^{-1}+t)+2q^6t+q^8t^3)+\\
&&\quad\quad +(q^2+(q^4+q^6)t^2+q^8t^4)+\\
&&\quad + a^{-6}q^{-2}t^{-8}+a^{-4}(q^{-2}t^{-7}+t^{-5}+q^2t^{-3}+q^4t^{-1})+\\
&&\quad\quad + a^{-2}(t^{-4}+q^2t^{-2}+2q^4+q^6t^2+q^8t^4)+\\
&&\quad\quad + (q^4t+q^6t^3+q^8t^5+q^{10}t^7)+a^2q^{10}t^8+\\
&&\quad\quad + a^{-2}q^2(1+q^2+q^4\frac{1+a^2t}{1-q^4t^2}).
\end{eqnarray*}
After setting $a=q^2$ in the above expression, we get the $(sl(2),S^2)$-colored homology of the figure-eight knot:
\begin{eqnarray*}
\CP^{sl(2),\tableau2}(4_1)(q,t)&=&(\bar{\CH}^{\tableau2}(4_1),d_{2|0})_{|_{a=q^2}}=\\
&&\quad = q^{-14}t^{-8}+q^{-10}t^{-7}+ q^{-8}t^{-5}+(q^{-8}+q^{-4})t^{-4}+\\
&&\quad\quad + (q^{-6}+q^{-4})t^{-3}+ (q^{-6}+q^{-4}+q^{-2})t^{-2} + \\
&&\quad\quad + (q^{-4}+2q^{-2}+1)t^{-1}+(q^{-2}+2+q^2)+\\
&&\quad\quad + (1+2q^2+q^4)t+ (q^2+q^4+q^6)t^2+(q^4+q^6)t^3+\\
&&\quad\quad + (q^4+q^8)t^4+q^8t^5+q^{10}t^7+q^{14}t^8+\\
&&\quad\quad\quad + q^{-2}+1+q^{2}t^2\frac{1+q^4t}{1-q^4t^2}.
\end{eqnarray*}
Again, the obtained homology matches the result from \cite{CHKrushkal}. 


\subsection{Comparison with the algebraic model}

Following Section \ref{sec:extension} and \cite{GOR}, we can compare the above computations with the corresponding algebraic models. Recall that the $S^r$-colored triply graded homology of the unknot has even generators $u_1,\ldots,u_r$ and odd generators $\xi_1,\ldots,\xi_r$ such that
$$[a,q,t_{c}]u_i=(0,2i,2i-2),\ [a,q,t_{c}]\xi_i=(2,2i-2,2i-1).$$
The differential $d_{2|0}$ is defined by the equation $d_{2|0}(\xi_i)=\sum_{i=1}^{j+1}u_ju_{i+1-j}$,
in particular,
\begin{equation}
\label{d20}
d_{2|0}(\xi_1)=u_1^2,\ d_{2|0}(\xi_2)=2u_1u_2,\ d_{2|0}(\xi_3)=u_2^2+2u_1u_3,\ d_{2|0}(\xi_4)=2u_1u_4+2u_2u_3.
\end{equation}

The uncolored HOMFLY homology of the unknot is a free algebra generated by $u_1$ and $\xi_1$, so the uncolored
$sl(2)$ homology is two-dimensional and spanned by $1$ and $u_1$. 

Using (\ref{d20}), one can check that the $(S^2, sl(2))$ homology of the unknot is spanned by
$$1,\ u_1,\ \mu_1,\ u_2^{k},\  u_2^{k}\mu_1,\qquad k\ge 1,$$
where $\mu_1=2u_2\xi_1-u_1\xi_2$. Note that the homology has nontrivial $\mathbb{Z}_2$-torsion that we do not consider here, see \cite{GOR} for more details.

The reduced triply graded homology of the trefoil is three-dimensional and spanned by $1,u_2,\xi_2$.
Therefore the uncolored $sl(2)$ homology of the trefoil can be considered as a quotient of $(S^2, sl(2))$ 
homology of the unknot by $u_2^2$ and $u_2\mu_1$, hence it is spanned by $1,u_1,u_2$ and $\mu_1$.

Finally, let us consider the $(S^2, sl(2))$ homology of the trefoil. Following (\ref{tref456}), the reduced $S^2$ HOMFLY homology of the trefoil is given by is spanned by $$1,\ u_3,\ u_4,\ u_3^2,\ \xi_3,\ \xi_4,\ u_3\xi_3, u_4\xi_3=-u_3\xi_4,\ \xi_3\xi_4.$$
For simplicity, let us focus on the bottom row. The unreduced $S^2$ HOMFLY homology of the trefoil has form
$$\langle 1,\ u_1,\ u_2^{k} \rangle\otimes\langle 1,\ u_3,\ u_4,\ u_3^2 \rangle.$$
Using (\ref{d20}), we can eliminate $u_1u_3$ and $u_1u_4$. Moreover, 
$$u_1u_3^2=d_{2|0}\left(\frac{1}{2}u_3\xi_3-\frac{1}{4}x_2\xi_4+\frac{1}{4}x_4\xi_2\right),$$
$$u_2^2u_3=d_{2|0}\left(\frac{1}{2}x_2\xi_4-\frac{1}{2}x_4\xi_2\right),$$
$$u_2^2u_4=d_{2|0}(\xi_3u_4-\xi_4u_3)+2u_2u_3^2,\ 
u_2^3=d_{2|0}(u_2\xi_3-u_3\xi_2).$$
and can be eliminated too. Therefore the bottom row of the unreduced $(S^2, sl(2))$ homology of the trefoil 
is spanned by
$$1,\ u_1,\ u_2,\ u_3,\ u_4,\ u_2^2,\ u_2u_4,\ u_2u_3,\ u_2^{k}u_3^2,\ k\ge 0.$$
The homology of $d_{2|0}$ on higher levels can be computed by similar methods.




\end{appendix}

\bibliographystyle{amsalpha}
