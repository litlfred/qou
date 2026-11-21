---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-003-4-examples
section_title: "Examples"
section_number: 4
pages: 35-47
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.98
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\label{sec:examples}

In this section we give some examples of the quadruply-graded colored HOMFLY homology that exhibit all of the structure and satisfy all of the conjectures from the previous sections. This gives a highly non-trivial check of the existence and consistency of such large and beautiful structure in the colored HOMFLY homology.



\subsection{Trefoil}
\label{sec:trefoil}

We start with the trefoil and its $S^2$ and $\Lambda^2$ colored homologies.
The uncolored HOMFLY homology of the trefoil is (\cite{DGR}):
\be\label{fund31}
\CP^{\tableau1}(3_1)(a,q,t)=a^2q^{-2}+a^2q^2t^2+a^4t^3.
\ee
The uncolored homology is the only one where two $t$-gradings coincide, i.e.
\[
\CP^{\tableau1}(3_1)(a,q,t_r,t_c)=\CP^{\tableau1}(3_1)(a,q,t=t_rt_c).
\]
From (\ref{fund31}) we can get the value of the $S$-invariant
of the trefoil (that we denote $\Sigma$ in this paper):
\be
\Sigma(3_1)=2.
\ee
For easier visualization, triply-graded homologies are usually presented in a diagram form. A generator of $(a,q,t)$-degree $(i,j,k)$
is presented as a dot in the $(q,a)$-plane at the position $(j,i)$ and it
is labeled by its $t$-degree $k$. The triply-graded homology of the
trefoil is presented in a diagram on the left of the Figure \ref{fig:colored3141} below.

\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored3141}
\caption{The uncolored homologies of the trefoil (left diagram) and figure-eight knot (right diagram).}
\label{fig:colored3141}
\end{figure}

The (reduced) $\tableau2$-colored HOMFLY polynomial of the trefoil knot is equal to:
\[
P^{\tableau2}(3_1)(a,q) = a^{4}q^{-4} + a^4q^2 + a^4q^4 + a^4q^8 - a^6 - a^6q^2 - a^6 q^6 - a^6 q^8 + a^8q^6 \,.
\]
The value of the four-variable $\tableau2$-colored superpolynomial (the Poincar\'e polynomial of the quadruply-graded $\CH^{\tableau2}(3_1)$) of the trefoil is given by
\be\label{quad31}
\CP^{\tableau2}(3_1)(a,q,t_r,t_c)= a^4(q^{-4} +q^2t_r^2t_c^4+q^4t_r^2t_c^6 +q^8t_r^4t_c^8) + $$ $$ a^6 (t_r^3t_c^5+q^2t_r^3t_c^7 + q^6t_r^5t_c^9+q^8t_r^5t_c^{11}) +a^8q^6t_r^6t_c^{12}.
\ee
The triply-graded $S^2$-homology of the trefoil that is computed in \cite{GS} is obtained from (\ref{quad31}) by setting $t_c=1$, whereas the homology obtained in \cite{AShakirov} or \cite{DMMSS} is obtained after setting $t_r=1$.

For the second-symmetric representation the $Q$-grading is expressed as $Q=q+t_r-t_c$. Then the tilde-version, i.e. the quadruply-graded $\tableau2$-homology in $(a,Q,t_r,t_c)$-gradings
is given by:
\be\label{tilquad31}
\tilde{\CP}^{\tableau2}(3_1)(a,Q,t_r,t_c)= a^4(Q^{-4} +t_r^2t_c^4+t_r^2t_c^6 +Q^4t_r^4t_c^8) +$$ $$ a^6 (Q^{-2}t_r^3t_c^5+Q^{-2}t_r^3t_c^7 + Q^2t_r^5t_c^9+Q^2t_r^5t_c^{11}) +a^8t_r^6t_c^{12}.
\ee
We note that all generators have the same $\delta$-grading equal to  $+2$. Moreover, the last homology is self-symmetric: in terms of the Poincar\'e polynomial this amounts to:
\[
\tilde{\CP}^{\tableau2}(3_1)(a,Q^{-1}t_r^{-1}t_c^{-2},t_r,t_c)=\tilde{\CP}^{\tableau2}(3_1)(a,Q,t_r,t_c).
\]
The quadruply-graded homologies we represent in the form of a diagram in the following way: for each generator we place a dot in the $(q,a)$-plane. If $(q,a)$-degree of a generator $x$ is $(i,j)$ then
we put a dot at a point with coordinates $(i,j)$. The two $t$-degrees are drawn as labels near the dot: the $t_r$-grading is written above the dot (and colored light green), while the $t_c$-grading of a generator is written below the corresponding dot. In such a way, the homology $\CH^{\tableau2}(3_1)$ is presented in Figure \ref{fig:colored31}.

\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored314}
\caption{The $S^2$-colored homology of the trefoil knot.}
\label{fig:colored31}
\end{figure}

We can see all five non-trivial colored differentials on this diagram:
There are two canceling ones $d^{col}_{1|0}$ and  $d^{col}_{0|2}$, represented by blue and red arrows, respectively, both leaving a single generator.  Furthermore the two $sl(n|m)$ colored differentials $d^{col}_{1|1}$ (dash-and-dot arrows) and $d^{col}_{0|3}$ (dashed arrows), both leaving the homology isomorphic to $\CH^{\tableau1}(3_1)$. And finally the universal one $d^{\leftarrow}$ (magenta arrows), also leaving the homology isomorphic to $\CH^{\tableau1}(3_1)$.
We note that the re-gradings are exactly as predicted in Sections \ref{coldif} and \ref{unicolor}.

The diagram for the tilde-version of the homology $\CH^{\tableau2}(3_1)$ is shown in Figure \ref{fig:colored315}.
\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored315}
\caption{The tilde-version of the $S^2$-colored homology of the trefoil knot  ($Q=q+t_r-t_c$).}
\label{fig:colored315}
\end{figure}
The refined exponential growth is indeed satisfied:
\[
\tilde{\CP}^{\tableau2}(3_1)(a,Q=q,t_r=t,t_c=1)=\left(\CP^{\tableau1}(3_1)(a,q,t)\right)^2.
\]
As for the second antisymmetric representation, we have that
the $\Lambda^2$-colored HOMFLY polynomial of the trefoil is given by
\be
P^{\tableau{1 1}} (3_1)(a,q) \; = \;
a^4 (q^{-8} + q^{-4} + q^{-2} + q^4)
- a^6 (q^{-8} + q^{-6} + q^{-2} + 1)
+ a^8 q^{-6}
\ee
The Poincar\'e polynomial of the quadruply-graded homology $\CH^{\tableau{1 1}}(3_1)$ equals
\be
\CP^{\tableau{1 1}} (3_1) (a,q,t_r,t_c)\; = \;
a^4 (q^{-8} + q^{-4} t_r^6t_c^2 + q^{-2} t_r^4t_c^2 + q^4 t_r^8t_c^4)
+$$ $$ a^6 (q^{-8} t_r^7t_c^3 + q^{-6} t_r^5 t_c^3 + q^{-2} t_r^{11}t_c^5 + t_r^9 t_c^5)
+ a^8 q^{-6} t_r^{12}t_c^6.
\ee
The corresponding diagram, together with the colored differentials, is presented in Figure \ref{fig:colored31A2}.
\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored314A2}
\caption{The $\Lambda^2$-colored homology of the trefoil knot.}
\label{fig:colored31A2}
\end{figure}
By comparing Figures \ref{fig:colored31} and \ref{fig:colored31A2}
one can immediately see the mirror symmetry \eqref{mirsymnew}. This symmetry sends $q\mapsto -q$, and commutes with the action of the colored differentials, as can be seen from the diagrams. We remark that all re-gradings from the isomorphisms induced by colored differentials are exactly as predicted in Sections \ref{coldif} and \ref{unicolor}.

Mirror symmetry is even better seen on the tilde-version of the homology. For the second-antisymmetric representation $\tableau{1 1}$, the $Q$-grading is obtained by $Q=(q+t_r-t_c)/2$, and so we get:
\be
\tilde{\CP}^{\tableau{1 1}} (3_1) (a,Q,t_r,t_c)\; = \;
a^4 (Q^{-4} +  t_r^6t_c^2 + t_r^4t_c^2 + Q^4 t_r^8t_c^4)
+ $$ $$a^6 (Q^{-2} t_r^7t_c^3 + Q^{-2} t_r^5 t_c^3 + Q^{2} t_r^{11}t_c^5 + Q^2t_r^9 t_c^5)
+ a^8  t_r^{12}t_c^6.
\ee
Its diagram is given in Figure \ref{fig:colored315A2}.
\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored315A2}
\caption{The tilde-version of the $\Lambda^2$-colored homology of the trefoil knot  ($Q=\frac{q+t_r-t_c}{2}$).}
\label{fig:colored315A2}
\end{figure}
Comparison of Figures \ref{fig:colored315} and \ref{fig:colored315A2} shows that the two are related by a simple exchange of $t_r$ and $t_c$ gradings, as predicted by mirror symmetry (\ref{mirsym}). Also, one can easily check that the explicit
form of the other mirror symmetry (\ref{mirsymnew}) is satisfied, too.



Before passing to further examples, we note that with the explicit mirror symmetries, whenever we know the quadruply-graded $\lambda$-colored homology of a knot $K$, then we automatically have $\lambda^t$-colored homology of $K$, as well:
\[
\tilde{\CP}^{\lambda^t}(K)(a,Q,t_r,t_c)=\tilde{\CP}^{\lambda}(K)(a,Q,t_c,t_r).
\]
Therefore, in the remaining examples we present the results only for one diagram of each pair, $\lambda$ and $\lambda^t$.


\subsection{Figure-eight knot}
We emphasize that our conjectures and predicted structures are for all knots, and not just torus knots. In particular, all homologies computed in \cite{GS} (that includes $S^2$-colored homologies of all prime knots with up to 6 crossings) can be extended to quadruply-graded homologies which have all of the wanted properties. Here we present the explicit expressions for the $S^2$-colored homology of the figure-eight knot.
The uncolored homology of the figure-eight knot is given by:
\[
\CP^{\tableau1}(4_1)(\a,q,t)=\a^2t^2+(q^{-2}t^{-1} + 1 + q^2 t) + \a^{-2}t^{-2},
\]
and its is $S$-invariant is $\Sigma(4_1)=0$.  The triply-graded homology of the figure-eight knot is presented in a diagram on the right of the Figure \ref{fig:colored3141}.
The $\tableau2$-colored HOMFLY polynomial of the figure-eight knot equals to:
$$
P^{\tableau2}(4_1)(\a,q)=\a^4q^4 +\a^2 (-q^{-2} +q^2-  q^4- q^6) +(q^{-6}-q^{-4}+3-q^4+q^6)+$$ $$
\a^{-2}(-q^{-6}-q^{-4}+q^{-2}-q^2) +\a^{-4}q^{-4}.
$$
The quadruply-graded $\tableau2$-colored HOMFLY homology of the figure-eight knot that we computed is given by:
$$
\CP^{\tableau2}(4_1)(\a,q,t_r,t_c)= \a^4q^4t_r^4t_c^8+\a^2 (q^{-2}t_rt_c+t_rt_c^3 +t_r^2t_c^2+ q^2t_r^2t_c^4 +  q^4t_r^3t_c^5+ q^6t_r^3t_c^7) +$$ $$
+(q^{-6}t_r^{-2}t_c^{-4} +q^{-4}t_r^{-1}t_c^{-3}+q^{-2}t_r^{-1}t_c^{-1} + q^{-2}t_c^{-2}+3+q^2t_c^2 + q^2t_rt_c+q^4t_rt_c^3+q^6t_r^2t_c^4)+$$ $$
+\a^{-2}(q^{-6}t_r^{-3}t_c^{-7}+q^{-4}t_r^{-3}t_c^{-5}+q^{-2}t_r^{-2}t_c^{-4}+t_r^{-2}t_c^{-2}+t_r^{-1}t_c^{-3}+q^2t_r^{-1}t_c^{-1}) + \a^{-4}q^{-4}t_r^{-4}t_c^{-8}.
$$

It is presented in a diagram form in Figure \ref{fig:colored41S2}.
\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored41}
\caption{The $S^2$-colored homology of the figure-eight knot.}
\label{fig:colored41S2}
\end{figure}
All generators have the same $\delta$-degree 0, in accordance with the fact that $4_1$ is a thin knot.
The homology $\CH^{\tableau2}(4_1)$ has five colored differentials: two canceling ones $d^{col}_{1|0}$ and $d^{col}_{0|2}$, further two colored $sl(m|n)$ differentials $d^{col}_{1|1}$ and $d^{col}_{0|3}$ both leaving homology isomorphic to $\CH^{\tableau1}(4_1)$ and the universal one $d^{\leftarrow}$ also leaving  homology isomorphic to $\CH^{\tableau1}(4_1)$. All re-gradings are as given in Sections \ref{coldif} and \ref{unicolor}.

The $Q$-grading is given by $Q=q+t_r-t_c$.
So, the tilde-version of the $\tableau2$-colored HOMFLY homology of the figure-eight knot becomes:
$$
\tilde{\CP}^{\tableau2}(4_1)(\a,Q,t_r,t_c)=\a^4t_r^4t_c^8+\a^2 (Q^{-2}t_rt_c+Q^{-2}t_rt_c^3 +t_r^2t_c^2+ t_r^2t_c^4 +  Q^2t_r^3t_c^5+ Q^2t_r^3t_c^7) +$$ $$
(Q^{-4}t_r^{-2}t_c^{-4} +Q^{-2}t_r^{-1}t_c^{-3}+Q^{-2}t_r^{-1}t_c^{-1} + t_c^{-2}+3+t_c^2 + Q^2t_rt_c+Q^2t_rt_c^3+Q^4t_r^2t_c^4)+$$ $$
\a^{-2}(Q^{-2}t_r^{-3}t_c^{-7}+Q^{-2}t_r^{-3}t_c^{-5}+t_r^{-2}t_c^{-4}+t_r^{-2}t_c^{-2}+Q^2t_r^{-1}t_c^{-3}+Q^2t_r^{-1}t_c^{-1}) +\a^{-4}t_r^{-4}t_c^{-8}.
$$
The tilde-version is presented in Figure \ref{fig:colored41t2} in $(a,Q,t_r,t_c)$-gradings.
\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored41t}
\caption{The tilde-version of $S^2$-colored homology of the figure-eight knot.}
\label{fig:colored41t2}
\end{figure}
It indeed satisfies self-symmetry (\ref{selfsym}) and refined exponential growth (\ref{reduced refined exp growth for S}).


\subsection{(3,4)-torus knot}
In this section we describe the quadruply-graded $S^2$ colored homology of the (3,4)-torus knot $T_{3,4}$ (i.e. $8_{19}$ knot) and show that it satisfies all of the desired properties. This knot is a thick knot, and has nontrivial differential $d_{1|1}$ (i.e. $d_0$) on the uncolored homology, which makes this a highly-nontrivial consistency check of all predicted properties.
The uncolored homology of $T_{3,4}$ is given by \cite{DGR}:
$$
\CP^{\tableau1}(T_{3,4})(\a,q,t)=\a^6q^{-6}+\a^8q^{-4}t^3+\a^6q^{-2}t^2+\a^8t^5+\a^6q^2t^4+\a^8q^{4}t^7+\a^6q^{6}t^6+ $$ $$
+\a^{10}t^8+\a^8q^{-2}t^5+\a^8q^{2}t^7+\a^6t^4.
$$
Its $S$-invariant is $\Sigma(T_{3,4})=6$.
There is a non-trivial differential $d_0$ (or $d_{1|1}$) on $\CH^{\tableau1}(T_{3,4})$ of $(a,q,t)$-degree $(-2,0,-3)$ leaving 5-dimensional homology isomorphic to the knot Floer homology of $T_{3,4}$:

\be
(\CH^{\tableau1}(T_{3,4}),d_{1|1})=\a^6q^{-6}+\a^8q^{-4}t^3+\a^6t^4+\a^8q^{4}t^7+\a^6q^{6}t^6.
\ee
The quadruply-graded $\tableau2$-colored homology of $T_{3,4}$ that we have computed has 121 generators. Its Poincar\'e polynomial is given by:
\begin{multline*}
\tilde{\CP}^{\tableau2}(T_{3,4})(\a,Q,t_r,t_c)=a^{12}(Q^{-12}+Q^{-8}t_r^2(t_c^4+t_c^6)+Q^{-6}t_r^4(t_c^8+t_c^{10})+\\ Q^{-4}t_r^4(t_c^8+t_c^{10}+t_c^{12})+
Q^{-2}t_r^6(t_c^{12}+t_c^{14})+t_r^6(t_c^{12}+t_c^{14}+t_c^{16}+t_c^{18})+t_r^8t_c^{16}+Q^2t_r^8(t_c^{16}+t_c^{18})+\\ Q^4t_r^8(t_c^{16}+t_c^{18}+t_c^{20})+Q^6t_r^{10}(t_c^{20}+t_c^{22})+Q^8t_r^{10}(t_c^{20}+t_c^{22})+Q^{12}t_r^{12}t_c^{24})+\\
\a^{14}(Q^{-10}t_r^{3}(t_c^{5}+t_c^{7})+Q^{-8}t_r^{5}(t_c^{9}+t_c^{11})+Q^{-6}t_r^{5}(t_c^{9}+2t_c^{11}+t_c^{13})+\\ Q^{-4}t_r^{7}(2t_c^{13}+3t_c^{15}+t_c^{17})
+Q^{-2}t_r^{7}(t_c^{13}+2t_c^{15}+2t_c^{17}+t_c^{19})+\\
Q^{-2}t_r^{9}(t_c^{17}+t_c^{19})+t_r^9(2t_c^{17}+3t_c^{19}+t_c^{21})
+ Q^2t_r^{9}(t_c^{17}+2t_c^{19}+2t_c^{21}+t_c^{23})+
 Q^2t_r^{11}(t_c^{21}+t_c^{23})+\\
 Q^4t_r^{11}(2t_c^{21}+3t_c^{23}+t_c^{25})+
Q^6t_r^{11}(t_c^{21}+2t_c^{23}+t_c^{25})+Q^8t_r^{13}(t_c^{25}+t_c^{27})+Q^{10}t_r^{13}(t_c^{25}+t_c^{27}))+\\
+\a^{16}(Q^{-8}t_r^{6}t_c^{12}+Q^{-6}t_r^{8}(t_c^{14}+2t_c^{16}+t_c^{18})+Q^{-4}t_r^{8}(t_c^{16}+t_c^{18})+Q^{-4}t_r^{10}t_c^{20}+\\
Q^{-2}t_r^{10}(t_c^{18}+3t_c^{20}+2t_c^{22})+t_r^{10}(t_c^{20}+t_c^{22}+t_c^{24})+ t_r^{12}(t_c^{22}+2t_c^{24}+t_c^{26}) + \\
 Q^2t_r^{12}(t_c^{22}+3t_c^{24}+2t_c^{26}) + Q^4t_r^{12}(t_c^{24}+t_c^{26}) +Q^4t_r^{14}t_c^{28}+q^6t_r^{14}(t_c^{26}+2t_c^{28}+t_c^{30})+q^8t_r^{14}t_c^{28})+\\
+\a^{18}(Q^{-4}t_r^{11}(t_c^{21}+t_c^{23})\!+\!Q^{-2}t_r^{13}(t_c^{25}+t_c^{27})+t_r^{13}(t_c^{25}+t_c^{27})+Q^{2}t_r^{15}(t_c^{29}+t_c^{31})+\\
+Q^{4}t_r^{15}(t_c^{29}+t_c^{31}))
+\a^{20}t_r^{16}t_c^{32}.
\end{multline*}
The Poincar\'e polynomial in $(a,q,t_r,t_c)$-gradings can be obtained from the above expression by:
\[
\CP^{\tableau2}(T_{3,4})(a,q,t_r,t_c)=\tilde{\CP}^{\tableau2}(T_{3,4})(a,Q=q,t_r=t_r q^{-1},t_c=t_c q).
\]
This homology satisfies all of the expected properties: there are four colored $sl(m|n)$ differentials $d^{col}_{1|0}$, $d^{col}_{0|2}$, $d^{col}_{1|1}$ and $d^{col}_{0|3}$, with the properties and re-gradings exactly matching the predicted behaviour from Section \ref{coldif}. Moreover, there exists a universal colored differential $d^{\leftarrow}$ as predicted in Section \ref{unicolor}.
Furthermore, the homology $\tilde{\CH}^{\tableau2}(T_{3,4})$ satisfies the self-symmetry property:
\[
\tilde{\CP}^{\tableau2}(T_{3,4})(a,Q^{-1}t_r^{-1}t_c^{-2},t_r,t_c)=\tilde{\CP}^{\tableau2}(T_{3,4})(a,Q,t_r,t_c).
\]
It also satisfies the refined exponential growth property:
\[
\tilde{\CP}^{\tableau2}(T_{3,4})(a,Q=q,t_r=t,t_c=1)=\left(\CP^{\tableau1}(T_{3,4})(a,q,t)\right)^2.
\]
Moreover, since HFK differential $d_0$ on $\CH^{\tableau1}(T_{3,4})$ is nontrivial, this time the HFK-like exponential growth property (\ref{HFKgrowth}) is giving a new relation on the homologies. Indeed, there exists a differential $d_{1|2}$ on $\tilde{\CH}^{\tableau2}(T_{3,4})$ of $(a,Q,t_r,t_c)$-degree $(-2,0,-3,-5)$, so that the homology $H^*(\tilde{\CH}^{\tableau2}(T_{3,4}),d_{1|2})$ is 25-dimensional with the following
Poincar\'e polynomial:
\begin{multline*}
(\tilde{\CH}^{\tableau2}(T_{3,4}),d_{1|2})(\a,Q,t_r,t_c)=\a^{12}(Q^{-12}+Q^{-6}t_r^4(t_c^8+t_c^{10})+t_r^6(t_c^{16}+ t_c^{18})+t_r^8 t_c^{16}+\\ Q^{6} t_r^{10} (t_c^{20}+t_c^{22}) + Q^{12} t_r^{12} t_c^{24})
+ \a^{14} (Q^{-10} t_r^3 (t_c^5+t_c^7) + Q^{-4} t_r^7 (t_c^{13}+t_c^{15}) + \\ Q^{-2} t_r^7 (t_c^{17}+t_c^{19})+Q^{2} t_r^9 (t_c^{21}+t_c^{23})  +Q^{4} t_r^{11} (t_c^{21}+t_c^{23}) + Q^{10} t_r^{13} (t_c^{25}+t_c^{27}) ) +\\
+ \a^{16} (Q^{-8} t_r^6 t_c^{12} + t_r^{10} (t_c^{22} + t_c^{24} ) + Q^8 t_r^{14} t_c^{28}).
\end{multline*}
Therefore
\be\label{HFKgrowtht34}
(\tilde{\CH}^{\tableau2}(T_{3,4}),d_{1|2})(a,Q=q,t_r=t,t_c=1)=\left(\CH^{\tableau 1}(T_{3,4}),d_{1|1})(a,q,t)\right)^2.
\ee


\subsection{$(2,2)$ representation}
\label{sec:22}
In this section we describe the $\tableau{2 2}$-colored HOMFLY homology of the trefoil knot.
It should categorify the reduced $\tableau{2 2}$-colored HOMFLY polynomial of the trefoil:
\begin{multline*}
P^{\tableau{2 2}} (3_1)(\a,q) =
\a^{16}
 + \a^{14} (-q^{-6} - 2q^{-4} - q^{-2} - q^2 - 2 q^4 - q^6)\\
+ \a^{12} (4 + 2q^{-10} + 2q^{-8} + 2 q^{-6} + q^{-4} + 3 q^{-2} + 3 q^2 + q^4 + 2 q^6 + 2 q^8 + 2 q^{10})\\
+ \a^{10} (-2 - q^{-14} - 2 q^{-12} - q^{-10} - q^{-8} - 3 q^{-6}\\ - 4 q^{-4} - 3 q^{-2} - 3 q^2 - 4 q^4 - 3 q^6 - q^8 - q^{10} - 2 q^{12} - q^{14})\\
+ \a^{8} (2 + q^{-16} + q^{-10} + 2 q^{-8} + q^{-6} + q^{-4} + q^{-2} + q^2 + q^4 + q^6 + 2 q^8 + q^{10} + q^{16})
\end{multline*}
 The  $\tableau{2 2}$-colored HOMFLY homology of the trefoil knot that we computed, has 81 generators. Its four-variable Poincar\'e polynomial is given by:
\begin{multline*}
\CP^{\tableau{2 2}} (3_1) (\a,q,t_r,t_c) =
\a^{16} t_r^{24}  t_c^{24}+ \a^{14} (q^{-6}{t_r^{19}t_c^{17}} + q^{-4}({t_r^{17}t_c^{17}} +{t_r^{19}t_c^{19}})+\\ q^{-2}{t_r^{17}t_c^{19}}+ q^2 t_r^{23}t_c^{21} + q^4 (t_r^{21}t_c^{21} + t_r^{23}t_c^{23}) + q^6 t_r^{21}t_c^{23})+  \\
 + \a^{12} (q^{-10}({t_r^{12}t_c^{10}} + {t_r^{14}t_c^{12}}) + 2q^{-8}{t_r^{12} t_c^{12}} + q^{-6}(t_r^{10}{t_c^{12}} +  t_r^{12}{t_c^{14}}) +q^{-4}t_r^{18}{t_c^{14}} +\\
+ q^{-2}({t_r^{16}t_c^{14}}  + 2t_r^{14}{t_c^{16}})+ (3t_r^{16} t_c^{16}+t_r^{18}t_c^{18}) + q^2 (t_r^{14}t_c^{16} + 2  t_r^{16}t_c^{18}) + \\
+ q^4 t_r^{14}t_c^{18} + q^6 (t_r^{20}t_c^{18} + t_r^{22}t_c^{20}) + 2 q^8 t_r^{20}t_c^{20} +  q^{10} (t_r^{18}t_c^{20} + t_r^{20} t_c^{22}))+ \\
 + \a^{10} (q^{-14}t_r^{7}{t_c^5} + q^{-12}({t_r^{5}t_c^5} + t_r^{7}{t_c^7}) + q^{-10}t_r^{5}{t_c^7} + q^{-8}t_r^{13}{t_c^9} +  q^{-6} (2t_r^{11}{t_c^9}  +t_r^{13}{t_c^{11}})+\\
 + q^{-4}(t_r^{9}{t_c^9} + 3t_r^{11}{t_c^{11}}) + q^{-2}(2t_r^{9}{t_c^{11}}+t_r^{11}{t_c^{13}})+ (t_r^{9} t_c^{13} +t_r^{17}t_r^{13})+\\
 +  q^2 (2t_r^{15}t_c^{13} +t_r^{17}t_c^{15}) + q^4 (t_r^{13}t_c^{13} +3t_r^{15}t_c^{15})
+ q^6 (2 t_r^{13}t_c^{15} +  t_r^{15}t_c^{17}) + \\
+ q^8 t_r^{13} t_c^{17} + q^{10} t_r^{19}t_c^{17} + q^{12} (t_r^{17}t_c^{17} +t_r^{19}t_c^{19}) + q^{14} t_r^{17}t_c^{19}) +\\
 + \a^{8} (q^{-16} + q^{-10}t_r^{6}{t_c^4} + q^{-8}(t_r^{4}{t_c^4} + t_r^{6}{t_c^6}) + q^{-6}t_r^{4}{t_c^6}
+ q^{-4}t_r^{12}{t_c^8} + q^{-2}t_r^{10}{t_c^8}+\\
 (t_r^{8}t_c^8 + t_r^{10}t_c^{10}) + q^2 t_r^{8}t_c^{10} + q^4 t_r^{8}t_c^{12}  + q^6 t_r^{14}t_c^{12} + q^8(t_r^{12}t_c^{12} + t_r^{14} t_c^{14}) + q^{10} t_r^{12}t_c^{14} + q^{16} t_r^{16}t_c^{16}).
\end{multline*}
Let us list various differentials and their $(\a,q,t_r,t_c)$-degrees. Everywhere in this section $\lambda=\tableau{2 2}$.

\noindent
1. {Categorification:}
$$
\CP^{\lambda} (3_1) (\a,q,t_r=-1,t_c=1)= P^{\lambda} (3_1)(\a,q) = \CP^{\lambda} (3_1) (\a,q,t_r=1,t_c=-1).
$$
2. { Canceling differentials:} There exist differentials $d^{col}_{2|0}$ and $d^{col}_{0|2}$, with  degrees $(-2,4,-1,-1)$ and $(-2,-4,-5,-5)$, respectively. Remaining generators have degrees $(8,-16,0,0)$ and $(8,16,16,16)$, respectively.

\noindent
3. { Row-removing differentials:} There exist differentials $d^{col}_{3|0}$ and $d^{col}_{1|2}$ of degrees $(-2,6,-3,-1)$ and $(-2,-2,-7,-5)$, respectively, such that

\[
H^*\left( \CH^{\lambda}(3_1), d^{col}_{3|0} \right) \; \cong \; \CH^{\tableau{2}}(3_1),
\]
\[
H^*\left( \CH^{\lambda}(3_1), d^{col}_{1|2} \right) \; \cong \; \CH^{\tableau{2}}(3_1).
\]

4. { Column-removing differentials:} There exist differentials $d^{col}_{0|3}$ and $d^{col}_{2|1}$ of degrees  $(-2,-6,-5,-7)$ and $(-2,2,-1,-3)$, respectively, such that

\[
H^*\left( \CH^{\lambda}(3_1), d^{col}_{0|3} \right) \; \cong \; \CH^{\tableau{1 1}}(3_1),
\]
\[
H^*\left( \CH^{\lambda}(3_1), d^{col}_{2|1} \right) \; \cong \; \CH^{\tableau{1 1}}(3_1).
\]
5. { Universal colored differentials:} There exist differentials $d^{\uparrow}$ and $d^{\leftarrow}$ of  degrees $(0,2,-2,0)$ and $(0,2,0,2)$, respectively, such that






\[
H^*\left( \CH^{\lambda}(3_1), d^{\uparrow} \right) \; \cong \; \CH^{\tableau{2}}(3_1),
\]
\[
H^*\left( \CH^{\lambda}(3_1), d^{\leftarrow} \right) \; \cong \; \CH^{\tableau{1 1}}(3_1).
\]
The remaining properties are best seen in the $(\a,Q,t_r,t_c)$-gradings. Recall that in this case the $Q$-grading can be expressed via the other ones by the equation $$Q=(q+t_r-t_c)/2.$$ We denote the $\lambda$-colored homology in these four gradings by $\tilde{\CH}^{\lambda}(3_1)$ and the corresponding four-variable Poincar\'e polynomial by $\tilde{\CP}^{\lambda}(3_1)(\a,Q,t_r,t_c)$. In terms of $\CP^{\lambda}(3_1)$, we have
\[
\tilde{\CP}^{\lambda}(3_1)(\a,Q,t_r,t_c)={\CP}^{\lambda}(3_1)(\a,Q^{1/2},t_rQ^{1/2},t_cQ^{-1/2}).
\]
6. { Self-symmetry:}
\[
 \tilde{\CH}^{\lambda}_{i,j,k,l}(3_1) \cong \tilde{\CH}^{\lambda}_{i,-j,k-2j,l-2j}(3_1).
\]
7. { Mirror symmetry:}
Since $\tableau{2 2}^t = \tableau{2 2}$, the mirror symmetry in this case is an another, different symmetry on $\tilde{\CH}^{\lambda}(3_1)$:
\[
 \tilde{\CH}^{\lambda}_{i,j,k,l}(3_1) \cong \tilde{\CH}^{\lambda}_{i,j,l,k}(3_1).
\]
8. { Refined exponential growth:}
\[
\tilde{\CP}^{\lambda}(3_1)(\a,Q,t_r,t_c=1)=\left(\tilde{\CP}^{\tableau{1 1}}(3_1)(\a,Q,t_r,t_c=1)\right)^2.
\]





\subsection{$(2,2,2)$ representation}
\label{sec:222}

In this section we give the result for the $\tableau{2 2 2}$-colored homology of the trefoil. Although this homology is very large (729-dimensional) it
contains all colored differentials predicted in Section \ref{coldif}.
Due to its size, and in order to simplify the presentation, we give the homology and the differentials in $(\a,q,t_c)$-gradings, and simply denote $t_c$ by $t$.
In $(\a,q,t_c)$-gradings the Poincar\'e polynomial $\CP^{\lambda}(3_1)$  is given by:

$$
{\scriptstyle{
\CP^{\tableau{2 2 2}}(3_1)=\a^{12}(q^{-36}+q^{-30}t^4+q^{-28}(t^4+t^6)+q^{-26}(t^4+t^6)+q^{-24}(t^6+t^8)+q^{-22}t^8 }} $$ $$
{\scriptstyle{+q^{-20}(2t^8+t^{10})+q^{-18}(t^8+2t^{10})+q^{-16}(t^8+2t^{10}+t^{12})+q^{-14}(t^{10}+2t^{12}) }} $$ $$
{\scriptstyle{+q^{-12}(3t^{12}+t^{14})+q^{-10}(2t^{12}+2t^{14})+q^{-8}(t^{12}+3t^{14})+q^{-6}(t^{12}+2t^{14}+t^{16})+q^{-4}(t^{14}+2t^{16}) }} $$ $$
{\scriptstyle{+2q^{-2}t^{16}+q^{0}(2t^{16}+2t^{18})+q^{2}(t^{16}+2t^{18})+}} $$ $$ {\scriptstyle{q^{4}(t^{16}+2t^{18}+t^{20})+q^{6}(t^{18}+t^{20})+}}
{\scriptstyle{+q^{8}t^{20}+q^{10}t^{20}+q^{12}(t^{20}+t^{22})+q^{14}(t^{20}+t^{22})+q^{16}t^{22}+q^{24}t^{24}) }} $$ $$
{\scriptstyle{+\a^{14}(q^{-36}t^5+q^{-34}(t^5+t^7)+q^{-32}(t^5+t^7)
+q^{-30}(t^7+t^9)+q^{-28}(2t^9+t^{11})+q^{-26}(3t^9+3t^{11}) }} $$ $$
{\scriptstyle{+q^{-24}(2t^9+5t^{11}+t^{13})+q^{-22}(t^9+4t^{11}+3t^{13})+q^{-20}(2t^{11}+5t^{13}+t^{15})+q^{-18}(5t^{13}+4t^{15}) }} $$ $$
{\scriptstyle{+q^{-16}(4t^{13}+7t^{15}+t^{17})+q^{-14}(2t^{13}+8t^{15}+3t^{17})+ q^{-12}(t^{13}+5t^{15}+6t^{17})+q^{-10}(2t^{15}+7t^{17}+2t^{19}) }} $$ $$
{\scriptstyle{+q^{-8}(6t^{17}+5t^{19})+q^{-6}(4t^{17}+8t^{19}+t^{21})+q^{-4}(2t^{17}+8t^{19}+3t^{21})+ q^{-2}(t^{17}+5t^{19}+5t^{21}) }} $$ $$
{\scriptstyle{+q^{0}(2t^{19}+5t^{21}+t^{23})+q^{2}(4t^{21}+2t^{23})+q^{4}(3t^{21}+4t^{23})+q^{6}(2t^{21}+5t^{23}+t^{25}) }} $$ $$
{\scriptstyle{+q^{8}(t^{21}+4t^{23}+2t^{25})+q^{10}(2t^{23}+2t^{25})+q^{12}t^{25}+q^{14}t^{25}+q^{16}(t^{25}+t^{27})+q^{18}(t^{25}+t^{27})+q^{20}t^{27})+}} $$ $$
{\scriptstyle{+\a^{16}(q^{-34}(t^{10}+t^{12})+q^{-32}(t^{10}+2t^{12})
+q^{-30}(t^{10}+3t^{12}+t^{14})+q^{-28}(2t^{12}+2t^{14})}}  $$ $${\scriptstyle{+q^{-26}(t^{12}+3t^{14}+2t^{16})+q^{-24}(3t^{14}+5t^{16}+t^{18})+q^{-22}(2t^{14}+8t^{16}+3t^{18})}}$$ $${\scriptstyle{q^{-20}(t^{14}+7t^{16}+6t^{18})+q^{-18}(4t^{16}+8t^{18}+2t^{20}) }} $$ $$
{\scriptstyle{+q^{-16}(t^{16}+7t^{18}+5t^{20})+q^{-14}(5t^{18}+10t^{20}+2t^{22})+ q^{-12}(2t^{18}+11t^{20}+5t^{22})+}} $$ $${\scriptstyle{q^{-10}(t^{18}+9t^{20}+9t^{22}+t^{24})+
q^{-8}(4t^{20}+9t^{22}+2t^{24})+q^{-6}(t^{20}+7t^{22}+5t^{24})}}  $$ $${\scriptstyle{q^{-4}(4t^{22}+7t^{24}+t^{26})+ q^{-2}(2t^{22}+9t^{24}+3t^{26})+}} $$ $$
{\scriptstyle{\quad+q^{0}(t^{22}+7t^{24}+6t^{26})+q^{2}(4t^{24}+6t^{26}+t^{28})+q^{4}(t^{24}+4t^{26}+t^{28})+q^{6}(2t^{26}+2t^{28})+}} $$ $$
{\scriptstyle{\quad+q^{8}(t^{26}+2t^{28})+q^{10}(t^{26}+3t^{28}+t^{30})+q^{12}(2t^{28}+t^{30})+q^{14}(t^{28}+t^{30})+}} $$ $$
{\scriptstyle{\!\!\!\!+\a^{18}(q^{-32}t^{17}
+q^{-30}(t^{15}+2t^{17}+t^{19})+q^{-28}(3t^{17}+2t^{19})+q^{-26}(2t^{17}+3t^{19})+q^{-24}(t^{17}+3t^{19}+2t^{21})+}} $$ $$
{\scriptstyle{\quad+q^{-22}(2t^{19}+4t^{21}+t^{23})+q^{-20}(t^{19}+6t^{21}+4t^{23})+q^{-18}(6t^{21}+7t^{23}+t^{25})+q^{-16}(3t^{21}+8t^{23}+2t^{25})+}} $$ $$
{\scriptstyle{\quad+q^{-14}(t^{21}+6t^{23}+4t^{25})+ q^{-12}(3t^{23}+6t^{25}+t^{27})+q^{-10}(t^{23}+7t^{25}+4t^{27})+q^{-8}(6t^{25}+7t^{27}+t^{29})+}} $$ $$
{\scriptstyle{\quad+q^{-6}(3t^{25}+8t^{27}+2t^{29})+q^{-4}(t^{25}+5t^{27}+3t^{29})+ q^{-2}(2t^{27}+3t^{29})+q^{0}(t^{27}+3t^{29}+t^{31})+}} $$ $$
{\scriptstyle{\quad+q^{2}(3t^{29}+2t^{31})+q^{4}(2t^{29}+3t^{31})+q^{6}(t^{29}+2t^{31}+t^{33})+q^{8}t^{31})+}} $$ $$
{\scriptstyle{
\!\!\!\!+\a^{20}(q^{-28}(t^{22}+t^{24})+q^{-26}(t^{22}+2t^{24})+q^{-24}(t^{22}+3t^{24}+t^{26})+q^{-22}(2t^{24}+t^{26})+q^{-20}
(t^{24}+2t^{26})}} $$ $$
{\scriptstyle{\quad+q^{-18}(2t^{26}+2t^{28})+q^{-16}(2t^{26}+4t^{28}+t^{30})+q^{-14}(t^{26}+5t^{28}+2t^
{30})+ q^{-12}(3t^{28}+3t^{30})+}} $$ $$
{\scriptstyle{\quad+q^{-10}(t^{28}+2t^{30})+q^{-8}(2t^{30}+t^{32})+q^{-6}(t^{30}+2t^{32})+q^{-4}(t^{30}+3t^{32}+t^{34})+
q^{-2}(2t^{32}+t^{34})+}} $$ $$
{\scriptstyle{q^{0}(t^{32}+t^{34}))+\a^{22}(q^{-24}t^{29}+q^{-22}(t^{29}+t^{31})+q^{-20}
(t^{29}+t^{31})+q^{-18}t^{31} +q^{-14}t^{33}+ q^{-12}(t^{33}+t^{35})+}} $$ $$
{\scriptstyle{q^{-10}(t^{33}+t^{35})+q^{-8}t^{35}) +}}
{\scriptstyle{\!\!\!\!+ \a^{24}q^{-18}t^{36}.
}}
$$
On such a big homology $\CH^{\lambda}(3_1)$ categorifying the reduced $\lambda$-colored HOMFLY polynomial of the trefoil knot, there exist all of the predicted colored differentials:

\noindent
1. Canceling differential $d^{col}_{3|0}$ of $(\a,q,t_c)$-degree $(-2,6,-1)$ such that the homology $H^*(\CH^{\lambda}(3_1),d^{col}_{3|0})$ is one-dimensional, and the remaining generator has $(\a,q,t_c)$-degree $(12,-36,0)$.

\noindent
2. Canceling differential $d^{col}_{0|2}$ of degree $(-2,-4,-5)$, such that the homology $H^*(\CH^{\lambda}(3_1),d^{col}_{0|2})$ is one-dimensional, and the remaining generator has $(\a,q,t_c)$-degree $(12,24,24)$.

\noindent
3. Positive row-removing differential $d^{col}_{4|0}$ of  degree $(-2,8,-1)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{4|0}) \cong \CH^{\tableau2}(3_1).
\]
4. Negative row-removing differential $d^{col}_{1|2}$ of  degree $(-2,-2,-5)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{1|2}) \cong \CH^{\tableau2}(3_1).
\]
5. Positive row-removing differential $d^{col}_{5|0}$ of  degree $(-2,10,-1)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{5|0}) \cong \CH^{\tableau{2 2}}(3_1).
\]
6.  Negative row-removing differential $d^{col}_{2|2}$ of  degree $(-2,0,-5)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{2|2}) \cong \CH^{\tableau{2 2}}(3_1).
\]
7.   Negative column-removing differential $d^{col}_{0|3}$ of  degree $(-2,-6,-7)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{0|3}) \cong \CH^{\tableau{1 1 1}}(3_1).
\]
8. Positive column-removing differential $d^{col}_{3|1}$ of  degree $(-2,-4,-3)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{col}_{3|1}) \cong \CH^{\tableau{1 1 1}}(3_1).
\]
9.  Universal colored differential $d^{\leftarrow}$ of  degree $(0,2,2)$, such that
\[
H^*(\CH^{\lambda}(3_1),d^{\leftarrow}) \cong \CH^{\tableau{1 1 1}}(3_1).
\]



\subsection{$(2,1)$ ``hook'' representation}

The $\tableau{2 1}$-colored HOMFLY polynomial of the trefoil is given by
\begin{align}
P^{\tableau{2 1}} (3_1)(a,q) \; = \;
& -a^{12} + a^{10} (q^{-6} + q^{-4} + q^{-2} + q^2 + q^4 + q^6) \notag \\
& + a^{8} (-q^{-10} - 2 q^{-6} - 3 q^{-2} - 3 q^2 - 2 q^6 - q^{10}) \notag \\
& + a^{6} (q^{-10} + 2 q^{-6} - q^{-4} + 2 q^{-2} + 2 q^2 - q^4 + 2 q^6 + q^{10}). \notag
\end{align}
This polynomial has 31 terms, and therefore any homology theory categorifying it, should have at least 31 generators. This already indicates distinction between rectangular and hook diagrams: this time, already for the trefoil, the exponential growth property  cannot be satisfied (the uncolored homology of the trefoil is 3-dimensional and $31>3^3$). However, some of the structural properties still exist in the colored HOMFLY homology theories for the hook-shaped Young diagrams.

As a $sl(n|m)$ representation, $\lambda = \tableau{2 1}$ has three nice isomorphisms for particular values of $n$ and $m$. Namely we have that $\tableau{2 1}\cong \tableau1$ as $sl(2|0)$, as $sl(1|1)$ and as $sl(0|2)$ representations. Therefore, we expect three colored differentials, $d^{col}_{2|0}$, $d^{col}_{1|1}$ and $d^{col}_{0|2}$ on $\CH^{\tableau{2 1}}(K)$, such that

\begin{eqnarray}
H^*(\CH^{\tableau{2 1}}(K),d^{col}_{2|0})&\cong& \CH^{\tableau{1}}(K)\label{ht1},\\
H^*(\CH^{\tableau{2 1}}(K),d^{col}_{1|1})&\cong&\CH^{\tableau{1}}(K) \label{ht2},\\
H^*(\CH^{\tableau{2 1}}(K),d^{col}_{0|2})&\cong& \CH^{\tableau{1}}(K).\label{ht3}
\end{eqnarray}
The $(a,q,t)$-degrees of these three differentials are:
\be
\deg d^{col}_{2|0} = (-2,4,-1), \quad\quad \deg d^{col}_{1|1} = (-2,0,-3), \quad\quad \deg d^{col}_{0|2} = (-2,-4,-5).
\ee
The requirement that $\CH^{\tableau{2 1}}(3_1)$ should categorify $P^{\tableau{2 1}} (3_1)(a,q)$, together with the existence of the colored differentials $d^{col}_{2|0}$, $d^{col}_{1|1}$ and $d^{col}_{0|2}$
essentially determine the $\tableau{2 1}$-colored homology of the trefoil knot. It has 41 generators and its Poincar\'e polynomial is given by:
\begin{multline}
\label{barebones}
\CP^{\tableau{2 1}} (3_1)(a,q,t)=
a^{12} t^{13} + a^{10} (q^{-6} t^8 + q^{-4} t^8 + q^{-2} t^{10} + t^{10}+t^{11}\\ + q^2 t^{12} + q^4 t^{12} + q^6 t^{14})
+ a^{8} (q^{-10} t^3 + 2 q^{-6} t^5 + q^{-4} t^5 + q^{-4} t^6+3 q^{-2} t^7 + t^7 + t^8 + 3 q^2 t^9 \\ + q^4 t^9 + q^4 t^{10} + 2 q^6 t^{11} + q^{10} t^{13})
+ a^{6} (q^{-10} + 2 q^{-6} t^2 + q^{-4} t^3 + 2 q^{-2} t^4 + t^4+t^5\\+ 2 q^2 t^6 + q^4 t^7 + 2 q^6 t^8 + q^{10} t^{10}).
\end{multline}
Additional nice properties that this homology satisfies, and which also exist in the rectangular case, is the mirror symmetry. Since ${\tableau{2 1}}^t={\tableau{2 1}}$ this becomes a symmetry on $\CH^{{\tableau{2 1}}}(3_1)$:

\be
M_{\tableau{2 1}} : \CH^{\tableau{2 1}}_{i,j,k}(3_1) \to \CH^{\tableau{2 1}}_{i,-j,k-j}(3_1),
\ee
with the property that
\be
M_{\tableau{2 1}} d_{n|m} \; = \; d_{m|n} M_{\tableau{2 1}}.
\ee

There are some properties that we predict in the case of rectangular representations and which do not exist for the hook diagram. First of all, already for the trefoil the exponential growth property is not satisfied. The homology is 41-dimensional, and the ${\tableau{2 1}}$-colored HOMFLY polynomial already has 31 terms.

Second, this time the isomorphisms (\ref{ht1})-(\ref{ht3}) are valid only after
appropriate collapse of tri-grading, i.e. after setting $a=q^{n-m}$ in the case of the differential $d_{n|m}$.
Additionally, there is no explicit re-grading in these isomorphisms, and we could not find the second $t$-grading. Therefore the theory that we propose is triply-graded.

Finally, we note that there exists the $SL(2)$ Lefschetz-like action on homology \eqref{barebones} with raising operator of degree $(0,4,2)$.
According to the ``dictionary'' \eqref{aqtgradings}, this raising operator corresponds to forming a bound state with a BPS state of D0-brane charge $n=4$.
