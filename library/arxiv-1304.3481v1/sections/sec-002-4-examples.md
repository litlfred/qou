---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots"
section_id: sec-002-4-examples
section_title: "Examples"
section_number: 4
pages: 35-68
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
doc_brief: "Quadruply-graded colored homology of knots — W e conjecture the existence of four independent gradings in the colored HOMFLY homology."
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.976
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




\section{Colored HOMFLY homology for torus knots}
\label{sec:algmodel}

In this part we describe various algebraic and geometric approaches to the colored homology of
torus knots.


\subsection{Stable HOMFLY homology of torus knots}
\label{sec:torus}


We will be interested in the stable limit of the colored HOMFLY polynomials of $(n,m)$ torus knots at $m\to\infty$.
Using e.g. \cite[eq. (5.4)]{stevan}, one can prove the following result.

\begin{proposition}
Let $\kappa(\mu)=\sum_{(i,j)\in \mu}(i-j).$
Define
$$P_{st}^{\lambda}(T({m,n})) := q^{-mn\kappa(\lambda)+\frac{m}{n}\kappa(n\lambda)}a^{-\frac{m(n-1)|\lambda|}{2}}P^{\lambda}(T({m,n})).$$
Then
\begin{equation}
\label{stable poly}
\lim_{m\to\infty}P_{st}^{\lambda}(T({m,n}))=P^{n\lambda}(a,q).
\end{equation}
\end{proposition}
As a corollary, one can compute the stable colored invariants of torus knots using the hook formula (\ref{plambda}).
One can easily check that the unreduced stable polynomial $P^{\lambda}(T(n,\infty))=P^{n\lambda}(\unknot ; a,q)$ is
a series in $(-a)$ and $q$ with nonnegative coefficients.


Let us compute the stable polynomial of the $(2,\infty)$ torus knot colored by the Young diagram $\lambda=(2,1)$.
By (\ref{stable poly}) it is the same as the polynomial of the unknot colored by the Young diagram $2\lambda=(4,2)$.
The hook formula (\ref{plambda}) gives the following answer (up to an overall scaling):
$$P^{2\lambda}(\unknot)=\frac{(1-aq^{-1})(1-a)^2(1-aq)(1-aq^2)(1-aq^{3})}{(1-q)^2(1-q^2)^2(1-q^4)(1-q^5)}.$$
Note that
$$P^{\lambda}(\unknot)=\frac{(1-aq^{-1})(1-a)(1-aq)}{(1-q)^2(1-q^3)}.$$
The reduced polynomial
$P^{red}_{\lambda}(T(2,\infty))=\frac{P^{\lambda}(T(2,\infty))}{P^{\lambda}(a,q)}$ has positive and negative terms
in the $q$-expansion of the coefficient at $a^{0}$:
$$\frac{(1-q^3)}{(1-q^2)^2(1-q^4)(1-q^5)}=1 + 2 q^2 - q^3 + 4 q^4 - q^5 + 6 q^6 - 2 q^7 + 8 q^8 - 2 q^9 +
 11 q^{10}+\dots$$




We would like to use the equation (\ref{stable poly}) as a definition of the stable colored homology of $(n,\infty)$ torus knot.
More precisely, we conjecture that as a vector space $\CH^{\lambda}(n,\infty)$ is isomorphic to $\CH^{n\lambda}(\unknot)$, moreover, the $a,q,t_{c}$ gradings on these spaces match. This suggests that $\CH^{\lambda}(n,\infty)$
is a free supercommutative algebra with bosonic and fermionic generators labelled by the boxes of $n\lambda$.


Let $\lambda$ be an $R \times S$ rectangular Young diagram, and let $K=T(p,q)$ be a $(p,q)$-torus knot.
We assume that  $\CH^{\lambda}(K)$ is a quotient of $\CH^{\lambda}(T(p,\infty))$, the latter space being
$(a,q,t_{c})$-graded isomorphic to the $p\lambda$-colored homology of the unknot. Under this assumption,
the multiplicative generators of $\CH^{\lambda}(K)$ coincide with the ones of $\CH^{\lambda}(T(p,\infty))$,
while some additional relations are imposed.  Let us determine the gradings of these generators.
The diagram $p\lambda$ is a $R\times pS$ rectangle, which can be naturally divided into $p$ different $R\times S$ rectangles.
Let us denote by $u_{ij}^{(n)}$ a bosonic generator in $n$-th rectangle {\em from the right} at box $(i,j)$,
and by   $\xi_{ij}^{(n)}$ a fermionic generator in $n$-th rectangle {\em from the left} at box $(i,j)$, as in Figures \ref{nrect1} and \ref{nrect2} .
\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,3)--(12,3)--(12,0)--(0,0);
\draw (4,0)--(4,3);
\draw (8,0)--(8,3);
\draw (2,1) node {$\bullet$};
\draw [<->,>=stealth] (0,1)--(1.9,1);
\draw [<->,>=stealth] (2,0)--(2,0.9);
\draw [<->,>=stealth] (4,-0.2)--(12,-0.2);
\draw (1,1.2) node {$i$};
\draw (2.2,0.5) node {$j$};
\draw (8,-0.5) node {$(n-1)S$};
\end{tikzpicture}
\caption{Generators $u_{ij}^{(n)}$}
\label{nrect1}
\end{figure}
\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,3)--(12,3)--(12,0)--(0,0);
\draw (4,0)--(4,3);
\draw (8,0)--(8,3);
\draw (10,1) node {$\bullet$};
\draw [<->,>=stealth] (8,1)--(9.9,1);
\draw [<->,>=stealth] (10,0)--(10,0.9);
\draw [<->,>=stealth] (0,-0.2)--(8,-0.2);
\draw (9,1.2) node {$i$};
\draw (10.2,0.5) node {$j$};
\draw (4,-0.5) node {$(n-1)S$};
\end{tikzpicture}
\caption{Generators $\xi_{ij}^{(n)}$}
\label{nrect2}
\end{figure}
Their gradings are given by the following equations:
\begin{eqnarray*}
(a,q)\left[u_{ij}^{(n)}\right]=(0,2(nS-i+R-j+1)),\\
(t_c,t_r)\left[u_{ij}^{(n)}\right]=2(nS-i),2((n-1)R+j-1)),\\
(a,q)\left[\xi_{ij}^{(n)}\right]=(2,2((n-1)S+i-j)),\\
(t_c,t_r)\left[\xi_{ij}^{(n)}\right]=(2((n-1)S+i)-1,2((n-1)R+j)-1).
\end{eqnarray*}
Note that $t_{r}$ is constant in rows and $t_{c}$ is constant in columns. This explains the notations
$t_{r}$ and $t_{c}$. Using the equation $Q=\frac{q+t_r-t_c}{R}$, we get
$$Q\left[u_{ij}^{(n)}\right]=2n,\quad Q\left[\xi_{ij}^{(n)}\right]=2n-2.$$

It is important to note that these elements generate {\em unreduced} stable homology. To work with the reduced homology,
one should consider $u_{ij}^{(n)},\xi_{ij}^{(n)}$ for $n\ge 2$ since the subalgebra generated by  $u_{ij}^{(1)},\xi_{ij}^{(1)}$
coincides with the unreduced homology of the unknot.

There exists a map $M_{\lambda} :\CH^{\lambda}(T(p,\infty))\to \CH^{\lambda^t}(T(p,\infty))$
such that for any $w$ we have
\begin{equation}
\label{gradings of M}
(Q,t_{c},t_{r})[M_{\lambda} (w)]=(Q,t_{r},t_{c})[w].
\end{equation}
The  map $M_{\lambda}$ is defined by the equations
$$M_{\lambda} \left(u_{ij}^{(n)}\right):=u_{R-j+1,S-i+1}^{(n)},\quad M_{\lambda} \left(\xi_{ij}^{(n)}\right):=\xi_{ji}^{(n)}.$$
One can check that it satisfies (\ref{gradings of M}).
The refined exponential growth conjecture also holds for the stable homology $\CH^{\lambda}(T(p,\infty)):$
\be
\label{stable exp growth}
\CP^{R\times S}(T(p,\infty),a,Q,t_{r})=\left(\CP^{\Lambda^R}(T(p,\infty),a,Q,t_{r})\right)^{S}.
\ee
The exponential growth conjecture follows from the fact that $t_{r}$ is constant in rows:
if we consider generators in $(a,Q,t_{r})$ gradings, then we get $S$ copies of $\CH^{\Lambda^R}(T(p,\infty))$ in the same gradings, which in turn implies (\ref{stable exp growth}).

Let us recall that in (\ref{Llambda}) we conjectured that the self-duality map $\Phi$ can be obtained as follows:
there exists a ``D0-brane'' operator $L_{\lambda}:\CH^{\lambda}(K)\to\CH^{\lambda}(K)$
such that
\begin{equation}
(a,q,Q,t_r,t_c)[L_{\lambda}]=(0,R+S,2,R,S),\quad \Phi_{\lambda}(x)=L_{\lambda}^{-Q(x)}.
\end{equation}
We conjecture that for torus knots colored by $\lambda=R\times S$ rectangular diagrams
such operator $L_{\lambda}$ coincides with the multiplication operator by $u_{S,1}^{(2)}.$ One can check that it has
the prescribed degrees. Moreover, the mirror map $M_{\lambda}$ is chosen in such a way that $M_{\lambda} (u_{S,1}^{(2)})=u_{R,1}^{(2)}$,
and so for the rectangular diagrams we have an equation
$$M_{\lambda} \circ L_{\lambda}=L_{\lambda^t}\circ M_{\lambda}, $$
and therefore
$$M_{\lambda} \circ \Phi_{\lambda} = \Phi_{\lambda^t}\circ M_{\lambda} .$$
This is indeed the required compatibility relation between $M$ and $\Phi$.


Now let us describe the action of colored differentials
in this algebraic model.
The positive row-removing differentials are given by the equation
$$d^{+}_{R\times S\to k\times S}\left(\xi_{i,j}^{(n)}\right)=u_{S+1-i,j-k}^{(n)}, j>k.$$
The positive column-removing differentials are given by the equation
$$d^{+}_{R\times S\to R\times l}\left(\xi_{i,j}^{(n)}\right)=u_{S+l+1-i,j}^{(n)}, i>l.$$
The negative row-removing differentials are given by the equation
$$d^{-}_{R\times S\to k\times S}\left(\xi_{1,k+1}^{(2)}\right)=1.$$
The negative column-removing differentials are given by the equation
$$d^{-}_{R\times S\to R\times l}\left(\xi_{l+1,1}^{(2)}\right)=1.$$
The differentials vanish on all other generators of the colored HOMFLY homology.
One can check that the degrees of these differentials agree with the expected ones.

The duality between positive and negative differentials is party explained by the identities
$$d^{+}_{R\times S\to k\times S}(\xi_{1,k+1}^{(2)})=u_{S,1}^{(2)},\ d^{-}_{R\times S\to k\times S}(\xi_{1,k+1}^{(2)})=1,$$
$$d^{+}_{R\times S\to R\times l}(\xi_{l+1,1}^{(2)})=u_{S,1}^{(2)},\ d^{-}_{R\times S\to R\times l}(\xi_{l+1,1}^{(2)})=1.$$
Finally, we describe the action of the universal differentials. As a model example, consider the unreduced $S^2$ homology of the unknot. It has two even generators $u_1,u_2$ and two odd generators $\xi_1,\xi_2$.
We define the universal differential on the bottom row by the formula
$$d(f(u_1,u_2))=u_2\frac{f(u_1,u_2)-f(-u_1,u_2)}{u_1}.$$
In other words,
$$d(u_1^{a}u_2^{b})=\begin{cases}
2u_1^{a-1}u_2^{b+1},& {\rm if}\ a\ {\rm is\ odd},\\
0,& {\rm if}\ a\ {\rm is\ even}.\\
\end{cases}$$
It is clear that $d^2=0$ and the homology of $d$ is isomorphic to $\mathbb{C}[u_1^2]$, as predicted by the grading restrictions in Section \ref{sec:gradings}. Similarly, on higher levels we define the differential by the equation
$d(\xi_1)=\xi_2$, so $d(\xi_1\wedge \xi_2)=0$. The total homology is a free algebra generated by $u_1^2$ and $\xi_1\xi_2$.

In general, we can always split variables into pairs, define a universal differential in each pair as above and extend it to the whole algebra by the Leibnitz rule. For example, in stable $S^2$ homology of the $(2,\infty)$ torus knot we have two even generators $u_3,u_4$ and two odd generators $\xi_3,\xi_4$. As in the above example, one can define a universal differential by the equations
$$d(u_3^{a}u_4^{b})=\begin{cases}
2u_3^{a-1}u_4^{b+1},& {\rm if}\ a\ {\rm is\ odd},\\
0,& {\rm if}\ a\ {\rm is\ even},\\
\end{cases}
\quad d(\xi_3)=\xi_4.
$$
It clearly agrees with the description of the universal differential for the trefoil in Section \ref{sec:trefoil}.


\subsection{Differential forms}
\label{sec:symtorusforms}

\begin{definition}
The {\em unreduced} moduli space $\overline{\CM}_{p,q}(r)$ is defined in the affine space
with the coordinates $u_1, \ldots, u_{rp}; v_1,\ldots,v_{rq}$ by the equation
\begin{equation}
\label{equv}
(1+u_1z+u_2z^2+\ldots+u_{rp}z^{rp})^{q}=(1+v_1z+v_2z^2+\ldots+v_{rq}z^{rq})^{p}.
\end{equation}
which should hold at every coefficient of its expansion in powers of  $z$.
\end{definition}

The space $\overline{\CM}_{p,q}(r)$ can be also defined in the affine space
with the coordinates $u_1,\ldots,u_{rp}$ by the coefficients in the $z$-expansion of the equation
$$(1+u_1z+u_2z^2+\ldots+u_{rp}z^{rp})^{q/p},$$
starting from $(qr+1)$-st. Indeed, one can rewrite the equation (\ref{equv}) as
$$(1+u_1z+u_2z^2+\ldots+u_{pr}z^{pr})^{q/p}=(1+v_1z+v_2z^2+\ldots+v_{qr}z^{qr}).$$
This will express $v_i$ through $u_j$. The dimension of $\overline{\CM}_{p,q}(r)$ equals to $r$.
Indeed, let us forget the scheme structure and study the underlying subset of the affine space.
One has $U(z)^{q}=V(z)^{p}$ for coprime $p$ and $q$ iff there exists a polynomial $F(z)$ such that
$U(z)=F(z)^{p}, V(z)=F(z)^{q}$. Since $F(z)$ starts from 1 and has degree $r$, we have $r$ parameters at our disposal.

\begin{conjecture}
\label{symmetric torus unreduced}
The {\em unreduced} $S^r$ homology of the $(p,q)$ torus knot is the space of differential forms on $\overline{\CM}_{p,q}(r)$:
\begin{equation}
\overline{\CH}^{S^r} (T(p,q)) \; = \; \Omega^{\bullet}(\overline{\CM}_{p,q}(r)) \,.
\label{HMunreduced}
\end{equation}
\end{conjecture}

As an illustration of this conjecture, let us consider an example of the unknot. We can choose $p=q=1$, so (\ref{equv}) takes the form
$$1+u_1z+u_2z^2+\ldots+u_{r}z^r=1+v_1z+v_2z^2+\ldots+v_{r}z^r$$
Therefore $\overline{\CM}_{p,q}(r)=\Spec\C[u_1,\ldots,u_r],$
and $$\Omega^{\bullet}(\overline{\CM}_{p,q}(r))=\C[u_1,\ldots,u_r,du_1,\ldots,du_r].$$
This agrees with the above description of the unreduced $S^r$-colored triply graded homology of the unknot.

For a more interesting example, consider the $S^2$-colored trefoil knot.
The  generators are $u_2$, $u_3$, $u_4$, and the defining equations are
\be
\label{s2 colored trefoil}
-\frac{3}{16} u_3 (u_2^2 - 4 u_4)=\frac{3}{128} (u_2^4 - 8 u_2 u_3^2 - 8 u_2^2 u_4 + 16 u_4^2)=0,
\ee
$$-\frac{1}{32} u_3 (-3 u_2^3 + 2 u_3^2 + 12 u_2 u_4)=0.$$

\begin{definition}
The {\em reduced} moduli space $\CM_{p,q}(r)$ is defined in the affine space
with the coordinates $u_{r+1},\ldots,u_{pr}; v_{r+1},\ldots,v_{qr}$ by all coefficients in the $z$-expansion of the equation
\begin{equation}
\label{equvred}
(1+u_{r+1}z^{r+1}+u_{r+2}z^{r+2}+\ldots+u_{pr}z^{pr})^{q}=(1+v_{r+1}z+v_2z^2+\ldots+v_{qr}z^{qr})^{p}
\end{equation}
\end{definition}

One can check that $\CM_{p,q}(r)$ defines a single point 0, so it is zero-dimensional.
We propose the following

\begin{conjecture}
\label{symmetric torus reduced}
The {\em reduced} $S^r$ homology of the $(p,q)$ torus knot is the space of differential forms on $\CM_{p,q}(r)$:
\begin{equation}
\CH^{S^r} (T(p,q)) \; = \; \Omega^{\bullet}(\CM_{p,q}(r)) \,.
\label{HMreduced}
\end{equation}
\end{conjecture}

For $r=1$ this conjecture is equivalent to the main conjecture of \cite{GORS}, since by the results of \cite{Gdaha} the right hand side of (\ref{HMreduced}) can be identified with a certain isotypic component of the finite-dimensional representation of rational Cherednik algebra with parameter $p/q$.
Moreover, it follows from \cite{GORS} for $r=1$ and from \cite{EGL} for general $r$ that the $(a,q)$-character
of $\Omega^{*}(\overline{\CM}_{p,q}(r))$ is equal to the unreduced $S^r$-colored HOMFLY polynomial of the $(p,q)$ torus knot.
One can also check (\cite{EGL}) that the $(a,q)$-character of $\Omega^{*}(\CM_{p,q}(r))$ is equal to the reduced $S^r$-colored HOMFLY polynomial
of the same knot. 

Let us describe the gradings on the space $\Omega^{*}(\CM_{p,q}(r))$.
The $a$-grading is defined by the degree of a differential form, so that $a(u_i)=0,\ a(du_i)=2.$ Furthermore, we define the $(q,t_r,t_c)$ gradings by the formula
\be
\label{deg ui for symmetric}
(q,t_c,t_r)[u_i]=\left(2i,2i-2,2\left\lfloor\frac{i-1}{r}\right\rfloor\right),
\ee
$$(q,t_r,t_c)[du_i]=\left(2i-2,2i-1,2\left\lfloor\frac{i-1}{r}\right\rfloor+1\right).$$
It is easy to check that the defining equations of $\CM_{p,q}(r)$ are homogeneous in $q$-grading and not homogeneous in $t$-gradings. Therefore, strictly speaking, on $\Omega^{*}(\CM_{p,q}(r))$ we get  $(a,q)$ bigrading and a pair of filtrations $(t_r,t_c)$.

For example, in the uncolored case the reduced homology of the trefoil knot has only one bosonic generator $u_2$,
and the defining equation for $\CM_{2,3} (1)$ reads as
\be
u_2^2=0
\label{tref3876}
\ee
Similarly, for the $(3,4)$ torus knot the reduced uncolored homology has two bosonic generators $u_2$ and $u_3$,
with the following defining equations for $\CM_{3,4} (1)$:
\be
u_2u_3=0,\ \frac{2 u_2^3}{9} = u_3^2.
\label{knot34829054}
\ee
Finally, the reduced $S^2$-colored homology of the trefoil knot
has two even generators $u_3$ and $u_4$ and the defining equations can be obtained from (\ref{s2 colored trefoil}) by setting $u_2=0$:
$$u_3u_4=u_4^2=u_3^3=0.$$
Their differentials have the form
$$u_3du_4+u_4du_3=2u_4du_4=3u_3^2du_3=0.$$
Therefore one can check that the monomial basis in $\Omega^{*}(\CM_{2,3} (2))$ is given by
\be
1,~ u_3,~ u_4,~ u_3^2,~ du_3,~ du_4,~ u_3du_3,~ u_3du_4,~ du_3\wedge du_4.
\label{tref456}
\ee
We illustrate this homology with the Figure \ref{s2tref} (compare with the Figures in Section \ref{sec:trefoil}).

\begin{figure}
\begin{tikzpicture}
\draw (0,0) node {$1$};
\draw (6,0) node {$u_3$};
\draw (8,0) node {$u_4$};
\draw (12,0) node {$u_3^2$};
\draw (4,1) node {$du_3$};
\draw (6,1) node {$du_4$};
\draw (10,1) node {$u_3du_3$};
\draw (11.7,1) node {$u_3du_4$};
\draw (10,2) node {$du_3\wedge du_4$};
\draw (0,-1)--(12,-1);
\draw (0,-1.1)--(0,-0.9);
\draw (2,-1.1)--(2,-0.9);
\draw (4,-1.1)--(4,-0.9);
\draw (6,-1.1)--(6,-0.9);
\draw (8,-1.1)--(8,-0.9);
\draw (10,-1.1)--(10,-0.9);
\draw (12,-1.1)--(12,-0.9);
\draw (0,-1.3) node {0};
\draw (2,-1.3) node {2};
\draw (4,-1.3) node {4};
\draw (6,-1.3) node {6};
\draw (8,-1.3) node {8};
\draw (10,-1.3) node {10};
\draw (12,-1.3) node {12};
\draw (11,-1.5) node {$q$};








\end{tikzpicture}
\caption{Algebraic model for the $S^2$ homology of the trefoil.}
\label{s2tref}
\end{figure}

For example, by computing the gradings of the basic elements \eqref{tref456} one finds
the Poincar\'e polynomial of the $S^2$-colored trefoil knot (in the $(a,q,t_r)$ grading):
\be
\CP^{S^2}(3_1)=1+q^6t^2+q^8t^2+q^{12}t^4+a^2q^4t^3+a^2q^6t^3+a^2q^{10}t^5+a^2q^{12}t^5+a^4q^{10}t^6.
\ee
More generally, for the $S^r$-colored reduced homology of the trefoil knot
the $(a,q,t_r)$ gradings of the generators are given by the equations:
$$(a,q,t_r)[u_i]=(0,2i,2),\  (a,q,t_r)[du_i]=(2,2i-2,3).$$
In particular, the monomial $u_{r+1}^{i}\cdot du_{r+1}\wedge du_{r+2}\wedge du_{r+j}$
has grading
$$i(0,2r+2,2)+\sum_{l=1}^{j}(2,2r+2l-2,3)=(2j,2(r+1)i+2jr+j(j-1),2i+3j)$$
and contributes the term
$a^{2j} q^{2(r+1)i+2rj+j(j-1)}t_r^{2i+3j}$ in the Poincar\'e polynomial
\begin{equation}\label{f1}
\CP^{S^r}(3_1)= a^{2r}q^{-r} \sum_{i+j\le r} { a^{2j} q^{2(r+1)i+2rj+j(j-1)}t_r^{2i+3j} \frac{ [r]!}{[i]![j]![r-i-j]!}, }
\end{equation}
obtained from the categorification of the Volume Conjecture and the super-$A$-polynomial \cite{FGS1,FGS2,FGSS}.
Here $[N]!$ is the unbalanced quantum factorial:
\[
[N]!=[N]\cdot [N-1]\cdot \ldots[2]\cdot[1]',
\]
\[
[N]'=\frac{q^N-1}{q-1}=1+q+\ldots +q^{N-1}.
\]
and one can easily verify that (\ref{f1}) satisfies the refined exponential growth conjecture
as well as the rest of the structural properties of section \ref{sec:gradings}.

Finally, let us match the gradings \eqref{deg ui for symmetric} with those in the construction of Section \ref{sec:alggrad}.
We have $R=1, S=r$, so there are  generators $u_{i,1}^{(n)},\xi_{i,1}^{(n)},\ 1\le i\le r$ with gradings
$$(a,q,t_c,t_r)[u_{i,1}^{(n)}]=(0,2+2rn-2i,2rn-2i,2n-2),\ $$
$$(a,q,t_c,t_r)[\xi_{i,1}^{(n)}]=(2,2r(n-1)+2i-2,2r(n-1)+2i-1,2n-1).$$
Indeed, these gradings agree with (\ref{deg ui for symmetric}) if one identifies
$$u_{i,1}^{(n)}=u_{rn+1-i},\ \xi_{i,1}^{(n)}=du_{r(n-1)+i}.$$












\subsection{Differentials for supergroups}

It has been conjectured in \cite[Conj. 3.22]{G} that the differentials $d_{0},d_{\pm n}$ belong to a bigger algebra.
In particular, for the uncolored homology of $(4,5)$ torus knot the following operators were introduced:
$\alpha_2$ of $(a,q,t)$ degree $(-2,-2,-5)$, $\alpha_1$ of $(a,q,t)$ degree $(-2,2,-3)$.
Their introduction was motivated by the observation that the ``usual'' differentials $d_N$ applied to the (unique)
generator with top $a$-degree 6 do not generate uncolored triply graded homology: there are 7 nontrivial differentials
$d_{0},d_{\pm n}$, while there are 9 generators with $a$-degree 4. The extra differentials solve this problem.
We can now identify these operators with the supergroup differentials:
$$\alpha_2=d_{1|2}, \quad \alpha_1=d_{2|1}.$$
In total, for the uncolored (4,5) knot we have 9 nontrivial differentials:
$$d_1=d_{1|0},\ \quad d_{-1}=d_{0|1},$$
$$d_2=d_{2|0},\ \quad d_0=d_{1|1},\ \quad d_{-2}=d_{0|2},$$
$$d_{3}=d_{3|0},\ \quad \alpha_1 =d_{2|1},\ \quad \alpha_2=d_{1|2},\ \quad d_{-3}=d_{0|3}.$$
For a general $(n,m)$ torus knot $(m>n)$ we will have all differentials $d_{a|b}$ with $a+b<n$,  of total number
$$2+3+4+...+n=\frac{n(n+1)}{2}-1=\frac{(n+2)(n-1)}{2}.$$
It has been explained in \cite{GORS} that the differentials are tightly related to the
(conjectural) action of the rational Cherednik algebra $H_{c}$ on the triply graded homology of torus knots.
More precisely, \cite[Definitions 7.2-7.3]{GORS} assign a differential to every $S_n$-equivariant copy
of the standard $(n-1)$-dimensional irreducible representation $V_{n}$ inside $H_c$. These differentials satisfy some nice
properties: for example, if the two copies $\alpha$ and $\beta$ are {\em pure}, then by \cite[Lemma 7.7]{GORS} the corresponding differentials
$d_{\alpha}$ and $d_{\beta}$ anticommute.

The new supergroup differentials can be naturally embedded in this framework.
Namely, recall that $H_{c}$ has generators $x_i, y_j$.
We define $\alpha(m|k)$ to be a copy of  $V_{n}$ spanned by $x_{i}^{m}y_{i}^{k}$,
and
$$d_{m|k}=d_{\alpha(m|k)}.$$
Since this copy is pure in the sense of \cite{GORS}, the corresponding differentials anticommute.
Moreover, one can check that $\alpha(m|k)$ span $\Hom_{S_{n}}(V_{n},H_{c})$, so the supergroup differentials
form a complete collection of differentials for the uncolored torus knot homology. The grading conventions of \cite{GORS}
assure that $d_{m|n}$ have the prescribed gradings.


\subsection{Examples}

We have compared the results of \ref{sec:trefoil} with the algebraic model in (\ref{tref456}). Let us make the similar comparisons for other torus knots in Section \ref{sec:examples}.

The stable reduced $\tableau{2 2}$-colored homology
of $(2,\infty)$ torus knot have 4 even and 4 odd generators
$u_{ij}^{(2)}$ and $\xi_{ij}^{(2)}$ (see Section \ref{sec:torus}). They have the following $(a,q,t_c,t_r)$-degrees:
$$\deg[u_{11}^{(2)}]=(0,10,6,4),\ \deg[u_{12}^{(2)}]=(0,8,6,6),$$
$$\deg[u_{21}^{(2)}]=(0,8,4,4),\ \deg[u_{22}^{(2)}]=(0,6,4,6),$$
$$\deg[\xi_{11}^{(2)}]=(2,4,5,5),\ \deg[\xi_{12}^{(2)}]=(2,2,5,7),$$
$$\deg[\xi_{21}^{(2)}]=(2,6,7,5),\ \deg[\xi_{22}^{(2)}]=(2,4,7,7).$$
As explained in Section \ref{sec:torus},  $Q\left[u_{ij}^{(2)}\right]=4$ and $Q\left[\xi_{ij}^{(2)}\right]=2$.
For example, the ``bottom row'' of the homology (with appropriate shift of gradings) is 16-dimensional and has monomial basis
$$1,~u_{21}^{(2)},~\left(u_{21}^{(2)}\right)^2,~\left(u_{21}^{(2)}\right)^3,~\left(u_{21}^{(2)}\right)^4,$$
$$u_{11}^{(2)},~u_{11}^{(2)}u_{21}^{(2)},~u_{11}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$u_{12}^{(2)},~u_{12}^{(2)}u_{21}^{(2)},~u_{12}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$u_{22}^{(2)},~u_{22}^{(2)}u_{21}^{(2)},~u_{22}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$\left(u_{22}^{(2)}\right)^2,\left(u_{11}^{(2)}\right)^2.$$
The self-symmetry map $\Phi$ reflects first four sets of monomials in the vertical axis, and preserved two remaining monomials.

The stable reduced $\tableau{2 2 2}$-colored homology
of $(2,\infty)$ torus knot have 6 even and 6 odd generators. They have the following $(a,q,t_c,t_r)$-degrees:
$$\deg[u_{11}^{(2)}]=(0,12,6,6),\ \deg[u_{12}^{(2)}]=(0,10,6,8),$$
$$\deg[u_{13}^{(2)}]=(0,8,6,10),\ \deg[u_{21}^{(2)}]=(0,10,4,6),$$
$$\deg[u_{22}^{(2)}]=(0,8,4,8),\ \deg[u_{23}^{(2)}]=(0,6,4,10),$$
$$\deg[\xi_{11}^{(2)}]=(2,4,5,7),\ \deg[\xi_{12}^{(2)}]=(2,2,5,9),$$
$$\deg[\xi_{13}^{(2)}]=(2,0,5,11),\ \deg[\xi_{21}^{(2)}]=(2,6,7,7).$$
$$\deg[\xi_{22}^{(2)}]=(2,4,7,9),\ \deg[\xi_{23}^{(2)}]=(2,2,7,11).$$
Indeed,  $Q\left[u_{ij}^{(2)}\right]=4$ and $Q\left[\xi_{ij}^{(2)}\right]=2$.

Finally, consider the $S^2$-colored $(3,4)$ torus knot.
In the notations of Section \ref{sec:symtorusforms}, we have
4 generators $u_3,u_4,u_5,u_6$ of $(a,q,t_c,t_r)$ gradings
$$\deg u_3=(0,6,4,2),\ \deg u_4=(0,8,6,2),$$
$$\deg u_5=(0,10,8,4),\ \deg u_6=(0,12,10,4).$$
Note that in the notations of Section \ref{sec:torus},
one would have
$$u_3=u_{21}^{(2)},\ u_4=u_{11}^{(2)},\ u_5=u_{21}^{(3)},\ u_6=u_{11}^{(3)},$$
and the grading conventions agree.
The defining relations have the form
$$u_3^3 - 9 u_4 u_5 - 9 u_3 u_6=2 u_3^2 u_4 - 3 (u_5^2 + 2 u_4 u_6)=u_3 u_4^2 + u_3^2 u_5 - 3 u_5 u_6=0,$$ $$5 u_3^4 - 12 u_4^3 - 72 u_3 u_4 u_5 - 36 u_3^2 u_6 + 54 u_6^2=5 u_3^3 u_4 - 9 u_4^2 u_5 - 9 u_3 (u_5^2 + 2 u_4 u_6) =0.$$
One can check that the monomial basis on the ``bottom row'' is given by the following 25 monomials:
$$1,\ u_3,\ u_3^2,\ u_3^3,\ u_3^4,\ u_3^5,\ u_3^6,$$
$$u_4,\ u_4u_3,\ u_4u_3^2,\ u_4u_3^3,\ u_4u_3^4,$$
$$u_5,\ u_5u_3,\ u_5u_3^2,\ u_5u_3^3,$$
$$u_6,\ u_6u_3,\ u_6u_3^2,\ u_6u_3^3,$$
$$u_4^2\, u_4^2u_3,\ u_4^2u_3^2,$$
$$u_5^2, u_4^3.$$
The self-symmetry map $\Phi$ reflects first five sets of monomials in the vertical axis, and preserved two remaining monomials.




\section{HOMFLY homology from A-model and B-model}
\label{sec:mirror}

In this section, we wish to look for geometric and physical models for colored HOMFLY homology,
eventually formulating it in the language of symplectic geometry or the so-called A-model.

Indeed, in mirror symmetry, the so-called B-model is famous for its formulation in the language of
complex (algebraic) geometry, while the A-model side involves symplectic invariants, Fukaya category, and quantum cohomology \cite{KontsevichHMS}.
Clearly, the algebraic model described in the previous section is closer to the B-model, and therefore
it will be our natural starting point here.
Then, we will relate it to various problems --- that are interesting in their own right --- in mirror symmetry and in symplectic geometry.
We will give several reformulations, in terms of A-model and B-model, open and closed ({\it i.e.} with and without D-branes),
in all of which colored HOMFLY homology will be realized as cohomology of a suitable BRST operator $Q$, such that $Q^2 = 0$:
\be
\CH^{\lambda} (K) \quad = \quad  Q\text{-cohomology} \,.
\ee
In physics literature, $Q$ is often called ``supercharge'' and
its cohomology is often called the {\it space of BPS states} since its elements
are the so-called BPS states (= supersymmetric configurations).
Even though precisely this interpretation of knot homology was proposed in \cite{GSV} and studied from various
vantage points in \cite{AShakirov,DGH,GukovRTN,IK,fiveknots}, the A-model and B-model reformulations discussed here
appear to be completely new and do not make direct contact with any of the existent geometric / physical models of knot homologies.
Therefore, by pursuing some of these new geometric descriptions further one is likely to learn a lot about colored HOMFLY homology and, possibly, even about homological mirror symmetry.




\subsection{B-model on a supermanifold}
\label{sec:Bmodel}

With this goal in mind, we start by reformulating the Conjectures \ref{symmetric torus unreduced} and \ref{symmetric torus reduced}
in terms of B-model on a super-manifold $\C^{d|d}$ with a certain Landau-Ginzburg potential $W_{super} (K; \lambda)$, such that
\be
\CH^{\lambda} (K) \; \cong \; Jac (W_{super} (K;\lambda))
\label{HasJac}
\ee
Note, that $\C^{d|d}$ is a super-Calabi-Yau manifold (see \cite{AVsuper,Schwarz,Wtwistor}).

Specifically, consider the potential $W (T(p,q); S^r)$ on the $u$-space given by the formula
\be
W (T(p,q); S^r) =\Coef_{(p+q)r+1}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q+p}{p}}.
\label{WTpqr}
\ee
Let us rename $du_i$ by $\xi_i$ and introduce a potential $W_{super} (T(p,q); S^r)$ on the superspace $\C^{pr|pr}$
with coordinates $u_i,\xi_i$ by the formula
\be
W_{super} (T(p,q); S^r) :=\sum_{i}\frac{\partial W}{\partial u_{i}}\xi_{i} \,.
\label{WsuperTpqr}
\ee
The space of differential forms $\Omega^{\bullet}\left(\overline{\CM}_{p,q}(r)\right)$ is isomorphic to the Jacobi ring of $W_{super} (T(p,q); S^r)$:
\begin{equation}
\label{W super}
\Omega\left[\overline{\CM}_{p,q}(r)\right]=\C[u_1,\ldots,u_{pr},\xi_1,\ldots,\xi_{pr}]/\left(\frac{\partial W_{super}}{\partial u_{i}},\frac{\partial W_{super}}{\partial \xi_{i}}\right).
\end{equation}
According to the Conjecture \ref{symmetric torus unreduced}, both spaces represent the unreduced $S^r$-colored homology of the $(p,q)$ torus knot. Indeed, the partial derivatives of $W (T(p,q); S^r)$ are equal to
$$\frac{\partial W (T(p,q); S^r)}{\partial u_{i}}
=\Coef_{(p+q)r+1}\frac{\partial}{\partial u_{i}}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q+p}{p}}=$$
$$\frac{q+p}{p}\Coef_{(p+q)r}\left[z^{i}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q}{p}}\right]=$$
$$\frac{q+p}{p}\Coef_{(p+q)r+1-i}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q}{p}},\ i=1\ldots pr.$$
Therefore the ring of functions on $\overline{\CM}_{p,q}(r)$ coincides with the Jacobi ring of $W$:
\begin{equation}
\C\left[\overline{\CM}_{p,q}(r)\right]=\C[u_1,\ldots,u_{pr}]/\left(\frac{\partial W}{\partial u_{i}}\right).
\end{equation}

The full space of differential forms $\Omega^{\bullet}\left(\overline{\CM}_{p,q}(r)\right)$ is a quotient of the space 
of all differential forms on $\C^{pr}$ by the equations
\begin{equation}
\label{forms eq}
\frac{\partial W}{\partial u_{i}}=0,\quad \sum_{j}\frac{\partial^2 W}{\partial u_{i}\partial u_j}\cdot du_{j}=0.
\end{equation}
The Jacobi ring of $W_{super}$ is defined by the following equations:
$$\frac{\partial W_{super}}{\partial \xi_{i}}=\frac{\partial W}{\partial u_{i}}=0$$
$$\frac{\partial W_{super}}{\partial u_{i}}=\sum_{j}\frac{\partial^2 W}{\partial u_{j}\partial u_{i}}\xi_{j}=0.$$
Since these equations coincide with (\ref{forms eq}), we get the relation (\ref{W super}).

In the mirror symmetry literature \cite{Schwarz,Sethi,AVsuper,Katzarkov},
the setup we just described is called a Landau-Ginzburg B-model with target space $\C^{d|d}$
and superpotential $W_{super} (K;\lambda)$. The function $W_{super} (K;\lambda)$ is called
{\it superpotential} even when the target space is an ordinary (bosonic) manifold,
{\it e.g.} $W(u_i)$ in our discussion might be called superpotential of a Landau-Ginzburg model on $\C^{pr}$.
As a final clarification of terminology, we should mention that a model is called {\it Landau-Ginzburg model}
when the superpotential is non-zero, and is referred to as the {\it sigma-model} (on a certain target manifold) when $W=0$.

In our case, the colored HOMFLY homology (of torus knots) is realized as the Jacobi ring\footnote{also known as
the ``chiral ring'' or ``ring of observables,'' see below} \eqref{HasJac} - \eqref{W super}
of a Landau-Ginzburg model on $\C^{pr|pr}$ with the superpotential $W_{super} (T(p,q); S^r)$.
There are several aspects of this B-model that make it rather special and interesting,
the main of which is undoubtedly the fact that the target space $\C^{pr|pr}$ is a supermanifold.

It is instructive, though, to start with a more familiar and conventional B-model with a target space $X$.
Then, we will extend it to a Landau-Ginzburg model with a superpotential $W$ and will see
why \eqref{HasJac} - \eqref{W super} can be interpreted as a ring of observables with and without D-branes
(called B-branes in the context of the B-model).
In general, we shall use $X$ for the target space of the B-model and $Y$ for the target space of the $A$-model,
so that $X$ and $Y$ are mirror manifolds in most of our applications.

First, as a warm-up and a lightning review of the relevant facts about B-model, let us consider
a B-model with target space $X$.
The space of observables --- or, to be more precise, the space of {\it closed (string) observables} ---
in such model is then identified with the $\bar \p$-cohomology of $X$ with values in $\bigwedge^p T_{X}$:
\be
\label{hom of polyvectors}
H^q \left( X, \bigwedge^p T^{1,0}_{X} \right)
\ee
Indeed, every $(0,q)$-form on $X$ with values in $\bigwedge^p T_{X}$
\be
A = d \bar z^{\bar k_1} \ldots d \bar z^{\bar k_q}
A^{j_1 \ldots j_p}_{\bar k_1 \ldots \bar k_q} \frac{\p}{\p z_{j_1}} \ldots \frac{\p}{\p z_{j_p}}
\ee
in the topological B-model defines an observable:
\be
\CO_A = \eta^{\bar k_1} \ldots \eta^{\bar k_q} A^{j_1 \ldots j_p}_{\bar k_1 \ldots \bar k_q} \theta_{j_1} \ldots \theta_{j_p}
\ee
Contracting this ``$(-p,q)$-form'' with the holomorphic $(n,0)$-form $\Omega$ on $X$ we obtain an isomorphism
between this space and $(n-p,q)$-forms, where $n$ is the total (complex) dimension of $X$.
Moreover, $\{ Q, \CO_A \} = - \CO_{\bar \p A}$, so that observables in the B-model are Dolbeault cohomology
of forms valued in exterior powers of the holomorphic tangent bundle, {\it i.e.} elements of \eqref{hom of polyvectors}.

Incorporating a superpotential $W \ne 0$ leads to a Landau-Ginzburg model where
the $Q$-operator acts as a differential $Q = \bar \p + Q_{\text{bdry}}$, such that
\be
Q^2 = W \cdot \text{id}
\ee
As a result, the space of closed string states in the Landau-Ginzburg model can be described
as a Hochschild homology or, equivalently, as a hypercohomology:
\be
HH_* (MF (X, W)) \cong \mathbb{H}^* (\Lambda^* \Omega_{X}, dW \wedge)
\ee
where $\Lambda^* \Omega_{X}$ denotes the exterior powers of the sheaf of differential forms.
The dual cohomology theory is
\be
HH^* (MF (X, W)) \cong \mathbb{H}^* (\Lambda^* T_{X}, [W, - ])
\ee
where $\Lambda^* T_{X}$ denotes exterior powers of the tangent sheaf and $[W, - ]$ denotes the Lie bracket with $W$.
In particular, if $f_1, \ldots, f_n$ are sections of line bundles $\CE_i$ on a smooth variety $V$,
then they define a function $W: \text{Tot} (\oplus \CE_i^*) \to \C$ and we have the following equivalence
of categories\footnote{The analogous statement for the topological A-model is:
$$
Fuk (Y,W) \cong Fuk (Sing (W)) \,.
$$}
\be
MF (\text{Tot} (\oplus \CE_i^*), W) \cong QCoh ( \{ f_i = 0 \} )
\ee
that allows to describe B-branes in a Landau-Ginzburg theory with the superpotential $W$
({\it i.e.} objects in the category of matrix factorizations of $W$)
in terms of the category of coherent sheaves on the critical variety of $W$.

\begin{theorem}[\cite{Orlov}]
\be
H^0 (MF (W)) \cong \CD^b_{sing} (W^{-1} (0))
\ee
\end{theorem}

Note, this brings us very close to our applications \eqref{HMunreduced} and \eqref{HMreduced},
where the moduli spaces $\overline{\CM}_{p,q}(r)$ and $\CM_{p,q}(r)$
are defined by polynomial equations $f_i (u_j) = 0$ in the space $X = \C^{pr}$ of $u$'s.
In situations like this, when the equations $f_i (u_j) = 0$ integrate to a superpotential $W (u_j)$
the chiral ring (also known as the $(c,c)$ ring) of the Landau-Ginzburg model on $X = \C^n$
is isomorphic to the quotient of the ring of polynomial functions $\C[u_1, ... , u_n]$ by $dW$,
\be
\CR_{\text{closed}} (\C^n, W) \; = \; \C [u_i] / (dW)
\label{Rclosed}
\ee
When $W$ is quasihomogeneous, this ring is graded by the R-charge symmetry $U(1)_R$.

In order to interpret the colored HOMFLY homology, though,
in the Landau-Ginzburg model we need not only to find a natural home for the moduli spaces
$\overline{\CM}_{p,q}(r)$ and $\CM_{p,q}(r)$
but also to describe the corresponding spaces of differential forms \eqref{HMunreduced} and \eqref{HMreduced} in the B-model language.
One way to do this is to replace the target space $\C^n$ by the supermanifold $X = \C^{n|n}$
and to replace the superpotential $W(u_i)$ by $W_{super} (u_i, \xi_i)$ defined in \eqref{WsuperTpqr}.
This gives then
\be
\CR_{\text{closed}} (\C^{n|n}, W_{super}) \; = \; \Omega^* (\CM)
\ee
where $\CM = \{ u \in \C \vert f_i (u) \equiv \p_i W (u) = 0 \}$.
Specifically, for the superpotential $W_{super}$ defined by \eqref{WTpqr} and \eqref{WsuperTpqr}
we get a B-model realization of the $S^r$-colored HOMFLY homology of torus knots.
For instance, from \eqref{s2 colored trefoil}, \eqref{tref3876}, and \eqref{knot34829054}
we find the following potentials in simple examples considered earlier:
$$W (3_1; \tableau1)=u_2^3,$$
$$W_{super} (3_1; \tableau1)=3u_2^2\xi_2,$$
$$W (8_{19}; \tableau1)=-\frac{7 u_2^4}{243} + \frac{14 u_2 u_3^2}{27},$$
$$W_{super} (8_{19}; \tableau1) = \left(-\frac{28 u_2^3}{243} + \frac{14 u_3^2}{27}\right) \xi_2+\frac{28 u_2 u_3}{27} \xi_3,$$
$$W (3_1; \tableau2)=\frac{5}{256}u_3 (3 u_2^4 - 8 u_2 u_3^2 - 24 u_2^2 u_4 + 48 u_4^2).$$


\vskip 0.25cm


Although conceptually this Landau-Ginzburg model should be the effective two-dimensional $\CN=2$ theory
on $D$ in the brane construction \eqref{theoryB} studied in \cite{DGH,FGS2,FGSS},
the setup appears to be surprisingly different.
Yet, in both cases, the Poincar\'e polynomial of the colored HOMFLY homology is realized as
a supersymmetric index (character) of the two-dimensional $\CN=2$ theory on $D$.
One important difference is that here we have a different 2d $\CN=2$ theory for each particular value of the color,
whereas in loc. cit. a single 2d $\CN=2$ theory determines $S^r$-colored superpolynomials for all values of $r$.
It would be interesting to understand better how the new Landau-Ginzburg realization of the colored HOMFLY homology
discussed here relates to the 2d $\CN=2$ theory on $D$ studied in \cite{DGH,FGS2,FGSS}.


\subsection{B-branes and open B-model}

There is another way, however, to describe the space of differential forms that is familiar to practitioners of mirror symmetry.
This will require introducing one more ingredient in our story, namely D-branes, and considering the space of open string states,
{\it i.e.} the states of open strings stretched between branes.
In the context of topological B-model branes are usually called B-branes.
Mathematically, B-branes are objects of the derived category of coherent sheaves $\CD^b (X)$ in the case of the sigma-model (when $W=0$),
or the category of matrix factorizations $MF (X, W)$ in the case of Landau-Ginzburg model with the target space $X$ and superpotential $W$.
We already saw both of these categories in our previous discussion and now we will spend more time discussing their objects, or B-branes.

Note that both the derived category of coherent sheaves and the category of matrix factorizations
are also familiar to practitioners of knot homology: these categories play a key role
in the constructions of {\it e.g.} \cite{CKamnitzer,KRa,KRb,Webster,Wu,Yonezawa}.

Now, let us describe the ``open'' analogue of \eqref{hom of polyvectors} and \eqref{Rclosed},
{\it i.e.} the space of states of open strings ending on a brane $\CB$ in the B-model,
starting with the sigma-model on $X$ (with $W=0$), as we did in our previous discussion,
and then extend it to branes in more general Landau-Ginzburg models.
In both cases, the conclusion will be that open strings ending on $\CB$ form an algebra, which is the Ext algebra\footnote{The algebra structure comes from the Yoneda product on the self-Ext groups.}
\be
\CR_{\text{open}} (\CB) \; = \; \Ext^* (\CB,\CB) \,.
\label{Ropen}
\ee
In order to see how it comes about, let us first consider two different branes, $\CB_1$ and $\CB_2$,
represented by shaves $\CE$ and $\CF$ supported on $S \subset X$.
Then, states of open strings stretched between $\CB_1$ and $\CB_2$ are elements of
\be
\label{homs of tensor prod}
H^q \left( S , \CE^{\vee} \otimes \CF \otimes \bigwedge^p \CN_{S/ X} \right)
\ee
There is a spectral sequence with \eqref{homs of tensor prod} as the second page that converges to \cite{Sharpe}:
\be
\Ext^{p+q}_{X} (\CE, \CF)
\ee
and in many cases one has
\be
\Ext^{n}_{X} (\CE, \CF) \; \cong \;
\bigoplus_{p+q=n} H^q \left( S , \CE^{\vee} \otimes \CF \otimes \bigwedge^p \CN_{S/ X} \right)
\ee
because the spectral sequence degenerates at $E_2$.



Now let us see how the boundary chiral ring \eqref{Ropen} can help us to produce
yet another interpretation of \eqref{HMunreduced} and \eqref{HMreduced} in {\it open} B-model.
The simplest example is the unknot colored by $\lambda = S^r$, whose HOMFLY homology
$\overline{\CH}^{S^r} (\unknot)$ is realized as the space of differential forms on
$V = \Spec\C[u_1,\ldots,u_r]$.
The corresponding choice of B-brane is closely related to SYZ brane \cite{SYZ} that plays an important role in mirror symmetry.
Namely, it is well known that for a ``zero-brane'' ({\it i.e.} a skyscraper sheaf $\CO_p$)
supported at a smooth point on a manifold $X$ of complex dimension $r$ the open string algebra \eqref{Ropen}
is the exterior algebra
\be
\Ext^* (\CO_p , \CO_p) \; \cong \; \Lambda^* (V)
\ee
where $V = T_p X  \cong  \Lambda^* \C^r$.
In order to upgrade $\Lambda^* (V)$ to the space of differential forms
$\Omega^* (V) = \C [V] \otimes \Lambda (V^{\vee})$,
one simply needs to replace $X \cong \C^r$ by its complexification $X_{\C} \cong X \times X$,
and consider a B-brane $\CB = \CO_{\Delta}$, where $\Delta \cong \C^r$
is the diagonal in $X \times X \cong \C^r \times \C^r$.
Note, the new target space $X \times X \cong \C^{2r}$
can be viewed as a SYZ torus fibration with a singular fiber at the origin.
To facilitate a discussion of the mirror A-model that will follow next,
it is convenient to replace $X = \C^r$ by $X = (\C^*)^r$.
Then, the target space $X \times X \cong (\C^*)^{2r}$ is also a $T^{2r}$
fibration, but without singular fibers and one has
\be
\CR_{\text{open}} (\CB) \; = \; \Ext^* (\CO_\Delta,\CO_\Delta) \; \cong \; \C [u_i^{\pm 1} , du_i]
\label{openDD}
\ee
Before we proceed to the mirror A-model, let us briefly discuss another interesting feature of this example.



Note that \eqref{openDD} can be identified with $HH^* (\CD^b (X)) \cong \C [u_i^{\pm 1} , du_i]$
which, according to our previous discussion, describes {\it closed} string states, not {\it open}.
This is an illustration of a more general phenomenon:
open string states \eqref{Ropen} of a B-brane supported on the diagonal $\Delta \subset X \times X$
can be identified with the closed string states \eqref{hom of polyvectors} of a B-model on $X$.
The mathematical content of this statement is summarized in the following:

\begin{theorem}[Hochschild-Kostant-Rosenberg isomorphism \cite{HKR}]
\be
\Ext^{n}_{X \times X} (\CO_{\Delta}, \CO_{\Delta}) \; \cong \;
\bigoplus_{p+q=n} H^q \left( X , \bigwedge^p T_{X} \right)
\ee
where $\Delta$ is the diagonal in $X \times X$.
\end{theorem}

Moreover, Yekutieli \cite{Yekutieli} shows that there is an isomorphism from the hypercohomology to self-Ext:
\be
\mathbb{H}^n (X, D_{poly} (X)) = \Ext^n_{X \times X} (\CO_X, \CO_X)
\ee
which is compatible with the cup product on the left and the Yoneda product on the right.
And using the isomorphism between the Hochschild cohomology and the polyvector field cohomology \cite{GSchack}, one has
\be
HH^* (\CD^b (X)) \; \cong \; \Ext^*_{X \times X} (\CO_\Delta,\CO_\Delta) \; \cong \; H^* (X, \Lambda^* T_X )
\label{HHExtDD}
\ee




\subsection{HOMFLY homology from symplectic geometry}
\label{sec:Amodel}

Now, let us see what kind of A-models one gets by applying mirror symmetry to the open and closed B-models in the above discussion.

In general, we denote by $Y$ the mirror of $X$.
The simplest example is $X = (\C^*)^r$ viewed as a (trivial) $T^r$ fibration over $\R^r$.
Then, mirror symmetry is simply a T-duality (a ``Fourier transform'') along the fibers,
and the mirror manifold is $Y \cong T^* T^r$.
The mirror of the statement $HH^* (\CD^b (X)) \cong \C [u_i^{\pm 1} , du_i]$
is the statement about the Hochschild cohomology of the Fukaya category $\CF (Y)$,
\be
HH^* \left( \CF (T^* T^r) \right) \; \cong \; \C [u_i^{\pm 1} , du_i]
\label{HHTTex}
\ee
which, by analogy with \eqref{HHExtDD}, can be also realized as the boundary OPE algebra
in the A-model of $Y \times \bar Y$, where $\bar Y$ denotes the space $Y$ with the symplectic form $- \omega$.
Indeed, in general, when a symplectic manifold $Y$ has ``enough'' Lagrangians,
the Hochschild cohomology its Fukaya category $\CF (Y)$ is expected \cite{Abouzaid,KontsevichHMS,Costello}
to be isomorphic to the Lagrangian Floer cohomology of the (anti-)diagonal $\Delta_Y \hookrightarrow Y \times \bar Y$,
\be
HH^* \left( \CF (Y) \right) \; \cong \; HF^* (\Delta_Y , \Delta_Y)
\label{HHHFdiag}
\ee
Thus, in our basic example of \eqref{openDD} and \eqref{HHTTex} mirror symmetry maps a B-brane $\CB = \CO_{\Delta_X}$
to a Lagrangian A-brane supported on the conormal bundle $T_{\Delta}^{\vee}$ to $T_{\Delta} \subset T^n \times T^n$
in $Y \times Y = T^* T^r \times T^* T^r$, so that
\be
HF^* (T_{\Delta}^{\vee},T_{\Delta}^{\vee}) \; \cong \; \C [u_i^{\pm 1} , du_i]
\ee
This is an open A-model version of \eqref{HHTTex} and a concrete illustration of \eqref{HHHFdiag}.

In general, this leads us to the following picture, where the (colored) HOMFLY homology is realized
either in terms of closed A-model of a symplectic manifold $Y$
\be
\CH^{S^r} (K) \; = \; HH^* \left( \CF (Y) \right)
\ee
or in terms of open A-model (Floer homology) of a certain Lagrangian submanifold $L$,
\be
\CH^{S^r} (K) \; = \; HF^* (L,L)
\label{HKLL}
\ee
(In our previous discussion, $L$ was the (anti-)diagonal $\Delta_Y \hookrightarrow Y \times \bar Y$,
but we allow more general Lagrangian submanifolds and more general symplectic manifolds here.)
For torus knots, the closed A-model version can be obtained by applying
the supermanifold version of mirror symmetry \cite{AVsuper,Katzarkov,Sethi}
to the B-model in section \ref{sec:Bmodel}.
We plan to return to a systematic study of this mirror symmetry elsewhere.

Here, let us simply point out that even for non-torus knots one might hope to find a realization of the form \eqref{HKLL}.
For example, for the figure-eight knot $K=4_1$ and $r=1$ a natural guess is
\be
L = {\bf S}^2 \text{~with 3 punctures}
\ee
embedded in some symplectic manifold $Y$, such that $HF^* (L,L) \cong H^* (L)$.






\section{``Bottom row'' of the colored HOMFLY homology}
\label{sec:bottom}

In this part we wish to study the ``bottom row'' of the colored superpolynomial, defined as
\be
\CP^{\lambda}_{\text{bottom}} (q,t) \; : = \; \lim_{\a \to 0} \, \a^{\#} \, \CP^{\lambda} (\a,q,t) \,,
\label{bottomrow}
\ee
where $\a^{\#}$ denotes the appropriate power of $a$, such that the product $\a^{\#} \, \CP^{\lambda} (\a,q,t)$
contains only non-negative $a$-degrees starting from zero.


\subsection{Combinatorial interpretation for torus knots}
\label{sec:combbot}

First, let us recall the conjectural combinatorial description of the uncolored triply graded homology
for a $(p,q)$ torus knot \cite{G,GM,ORS}. Consider a $p\times q$ rectangle and a $NW-SE$ diagonal in it.

\begin{proposition}(\cite{G})
\label{prop:bottom1}
The dimension of the ``bottom row'' of the reduced uncolored homology equals to the number of lattice paths
in this rectangle strictly below the diagonal:
$$\dim \CH_{\text{bottom}} (T(p,q)) \; = \; c_{p,q}=\frac{(p+q-1)!}{p!q!}.$$
\end{proposition}

For example, if $q=p+1$, this dimension equals to the $p$-th Catalan number.

\begin{proposition}(\cite{G})
The dimension of the ``$k$-th row'' of the reduced uncolored homology equals to the number of lattice paths
below the diagonal with $k$ marked corners:
$$\dim \CH_{a=k} (T(p,q)) \; = \; \frac{(p+q-k-1)!}{ p\cdot q\cdot k!\cdot (p-k-1)!(q-k-1)!}.$$
\end{proposition}

A $q$-analogue of this formula was discussed in \cite[eq. (3.46)]{BEM}.
Both of these propositions motivate the following combinatorial construction,
completed in \cite{ORS} where it was matched to the algebro-geometric constructions of \cite{os}.

The basis in $\CH_{p,q}$ is enumerated by the lattice paths in the $p\times q$ rectangle with marked corners. To every such path we assign three gradings, where $a$-grading corresponds to the number of marked corners. Let us describe $q-$ and $t-$ gradings.
For simplicity, we will focus on the bottom row, considered in details in \cite{GM}. Corrections for the higher rows can be found in \cite{ORS}.

Let us interpret a lattice path as a Young diagram $D$. Consider the $\C^{*}\times \C^{*}$ action on the Hilbert scheme of
$N$ points on $\C^2$, and let us restrict it to a one-parameter subgroup $(t^p,t^q)$. One can check (see {\it e.g.} \cite{Nakajima})
that the action of this subgroup has isolated fixed points parametrized by the Young diagrams with $N$ boxes. Therefore the corresponding moment map is a Morse function on $\Hilb^{N}(\C^2)$, and its gradient flow induces the Bialynicki-Birula cell decomposition of the Hilbert scheme \cite{Nakajima,Elstro}. We are interested in the dimension of the cell $C_{D}$ labelled by the fixed point $D$, which is given by the following formula:
$$\dim C_{D}=|D|+h^{+}_{p/q}(D),$$
where
\begin{equation}
\label{hplus}
h^{+}_{p/q}(D)=\sharp\left\{c\in D~~ \vline~~ \frac{a(c)}{l(c)+1}\le \frac{p}{q}< \frac{a(c)+1}{l(c)}\right\}.
\end{equation}
Here $a(c)$ and $l(c)$ denote the arm and the leg of a cell $c$ in a diagram $D$:

\begin{tikzpicture}
\draw  (0,0)--(0,4)--(5,0)--(0,0);
\draw  (1.5,0.5)--(1.5,0.7)--(1.7,0.7)--(1.7,0.5)--(1.5,0.5);
\draw [thick] (0,3)--(0.5,3) -- (0.5,2) -- (2.3,2)--(2.3,1.3)--(3,1.3)--(3,0.5)--(4,0.5)--(4,0)--(0,0)--(0,3);
\draw [<->,>=stealth] (1.7,0.6) -- (3,0.6);
\draw [<->,>=stealth] (1.6,0.7) -- (1.6,2);
\draw (2.3,0.4) node {${a(c)}$};
\draw (1.3,1.3) node {${l(c)}$};
\draw (2.5,-0.2) node {$p$};
\draw (-0.2,2) node {$q$};
\draw [->,>=stealth] (2.6,-0.15) -- (5,-0.15);
\draw [->,>=stealth] (2.4,-0.15) -- (0,-0.15);
\draw [->,>=stealth] (-0.15,1.8) -- (-0.15,0);
\draw [->,>=stealth] (-0.15,2.2) -- (-0.15,4);
\end{tikzpicture}

The statistics $h^{+}_{p/q}(D)$ was introduced in \cite{LW} in connection with some combinatorial models of the bigraded Catalan numbers.

\begin{proposition}
\label{prop:bottom3}
The gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $q$-grading assigned to $D$ equals to $2\left[|D|+2h^{+}_{p/q}(D)\right]$.}

\item{The $t$-grading assigned to $D$ equals to $2|D|$.}
\end{enumerate}
\end{proposition}


Motivated the refined exponential growth conjecture, we assume that the dimension of the $S^r$-colored homology is equal to the $r$-th power of the uncolored homology, {\it i.e.} the $r$-th power of the generalized Catalan number $c_{p,q}$.
Therefore it is natural to assume that one can find a basis in the $S^r$-colored homology labelled by all possible $r$-tuples of Young diagrams in $p\times q$ rectangle below the diagonal.

\begin{conjecture}
\label{prop:bottom4}
The bottom row of the $S^r$ colored homology of the $(p,q)$ torus knot has a basis labeled by the $r$-tuples $(D_1,\ldots,D_r)$ of the Dyck paths in $p\times q$ rectangle. The $(Q,t_r)$ gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $Q$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}\left[|D_i|+2h^{+}_{p/q}(D_i)\right]$.}

\item{The $t_r$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}|D_i|$.}
\end{enumerate}
\end{conjecture}

The $q$-grading (and, therefore, the $t_c$-grading) has yet to be constructed. We expect it to be related to the combinatorial constructions of \cite{BDZ} and \cite{HMZ}.




\subsection{Coupled instanton-vortex counting}
\label{sec:inst-surf}

The ``bottom row'' \eqref{bottomrow} has a simple and beautiful interpretation in terms of instanton / vortex counting.
As a warm-up, let us start with a simple vortex counting problem that is easy to do ``by hand''
and that has all the essential features. Then, we shall upgrade it to the equivariant instanton counting relevant to arbitrary knots and links.

Let $\CV_m$ be the moduli space of $m$ abelian vortices on a two-dimensional plane, $D = \R^2$.
In other words, $\CV_m$ is the moduli space of solutions to the PDEs
\be
\begin{array}{rl}
* F_A & =~ i |\phi|^2 - it \\
\bar \partial_A \phi & =~ 0
\end{array}
\label{abelianvorteq}
\ee
where $A$ is a connection on a $U(1)$ bundle of first Chern class $m$, and $t$ is a parameter.
These equations describe supersymmetric configurations (BPS states) in a two-dimensional theory
on $D$ with $\CN=(2,2)$ supersymmetry:
\be
\CT_{\text{vortex}}~:~ U(1)~\text{gauge theory with a single charged field}~\phi
\ee

It is well known that $\CV_m$ is a K\"ahler manifold of (real) dimension $2m$. Namely,
\be
\CV_m \; = \; \Sym^m (\C) \; \equiv \; \C^m / S_m \,,
\label{vortsymm}
\ee
where one can think of coordinates on $\CV_m$ as vortex positions on $D = \R^2 \cong \C$.

Since $D$ admits a circle action, one can consider the equivariant character, $Ch_q (\CV_m)$,
with respect to the rotation group $U(1)_q$ acting on $D$.
Indeed, $U(1)_q$ acts on $\CV_m$ in a natural way, by equal phase rotations on all factors in the symmetric product \eqref{vortsymm}.
Moreover, identifying the vortex moduli space $\CV_m = \Sym^m (\C)$
with the space of monic polynomials of degree $m$,
\be
f (x) \; = \; \prod_{j=1}^m (x - x_j) = x^m + a_1 x^{m-1} + \ldots + a_m \,,
\ee
we immediately deduce the isomorphism $\CV_m \cong \C^m = (\{ a_1, \ldots, a_m \})$
and also learn that $U(1)_q$ acts on the space $\CV_m$ with weights $(1, 2, \ldots, m)$.
Therefore, the $U(1)_q$-equivariant character of $\CV_m$ is
\be
Ch_q (\CV_m) \; = \; \frac{1}{(1-q)(1-q^2) \ldots (1-q^m)} \,,
\label{unknotvortchar}
\ee
in which a careful reader will recognize the ``bottom row'' of the \textsl{unnormalized} $S^m$-colored HOMFLY polynomial of the unknot.

This is not an accident, of course, and the physics setup \eqref{theoryB} predicts that the ``bottom row''
of any $\lambda$-colored HOMFLY homology of any knot $K$ has a similar interpretation in terms
of equivariant vortex counting on $D = \R^2$.
In order to explain this relation, we need to generalize our warm-up example in two important ways:
first, we need to introduce the homological $t$-grading, and secondly we need a generalization to arbitrary knots.
Both of these problems can be achieved by embedding $D = \R^2$ into a larger space $M_4 = \R^4$,
and realizing our vortex counting problem on $D$ as a special case of counting solutions
to coupled \textsl{instanton-vortex equations} or, equivalently, via equivariant instanton
counting on the 4-manifold $M_4$ in the presence of ramification along $D \subset M_4$.

However, before we proceed to generalizations, let us stay a bit longer in the world of vortex equations
and explore the picture which seems to emerge:
\be
\text{knot}~K \quad \leadsto \quad \text{2d vortex theory}~\CT_{\text{vortex}} (K) \quad \leadsto \quad \CV_m (K)
\ee
so that a suitable version $Ch_{q,t} (\CV_m)$ of the equivariant character computes the bottom row of
the colored superpolynomial \eqref{bottomrow} with $\lambda = S^m$,
\be
Ch_{q,t} (\CV_m) \; = \; \CP^{S^m}_{\text{bottom}} (q,t) \,.
\label{naiveVmP}
\ee
Already at this stage the reader might suspect that incorporating the $t$-grading and passing to knot homologies
can be addressed by considering equivariant cohomology or K-theory of the vortex moduli space,
\be
H^*_{U(1)_q} (\CV_m (K)) \,,
\label{naiveHvort}
\ee
where $t$-grading is identified with the homological grading.
Although this idea is a little too naive, it is actually on the right track, and it is instructive to pursue it a little further.

Therefore, as the natural next step let us consider a non-abelian generalization of \eqref{abelianvorteq}
that describes supersymmetric solutions in the 2d theory:
\be
\CT_{\text{vortex}}~:~ U(p+1)~\text{gauge theory with}~p+1~\text{fundamental fields}~\phi_i
\ee
The corresponding vortex equations
\be
\begin{array}{rl}
* F_A & =~ i\sum_{i=1}^{p+1} \phi_i \phi_i^{\dagger} - i t \\
\bar \partial_A \phi_i & =~ 0
\end{array}
\label{vortexeq}
\ee
involve a $U(p+1)$ gauge connection and $p+1$ Higgs fields $\phi_i$ in the fundamental
representation of the gauge group. Again, the $m$-vortex moduli space is a K\"ahler manifold
of real dimension
\be
\dim~ \CV_m^{U(p+1)} = 2 m (p+1) \,,
\label{mmndimension}
\ee
In particular, the single-vortex moduli space is well known to be a $(2p+2)$-dimensional space
\be
\CV_1^{U(p+1)} \; \cong \; \C \times \cp^p
\ee
where the factor $\C$ parametrized by the ``center-of-mass'' position,
while $\cp^p$ encodes the ``internal degrees of freedom'' of a single non-abelian vortex.
The rotation symmetry $U(1)_q$ acts on $\C$ with weight 1,
so we expect that it contributes to the equivariant character a factor $\frac{1}{1-q}$.
However, unlike our first example (related to the unknot), now the moduli space $\CV_1^{U(p+1)}$
has non-trivial topology and, therefore, if $t$-grading is simply the homological grading on \eqref{naiveHvort}
the suitable generalization of the equivariant character should be a product of $\frac{1}{1-q}$
and the Poincar\'e polynomial of $\cp^p$,
\be
\frac{1}{1-q} \sum_{i=0}^p t^{2i}
\ee
This turns out to be the correct answer for the bottom row of the HOMFLY homology of the $(2,2p+1)$ torus knot.


Now let us explain why all these examples are ``working'' and where the connection with vortex equations come from.
The reason, in fact, is already contained in section~\ref{sec:geomphys}
where we reviewed the interpretation~\eqref{HHBPS} of homological knot invariants
in terms of supersymmetric configurations (BPS states) in the string theory setup~\eqref{theoryB}.
What this interpretation tells us is that specializing to the bottom row \eqref{bottomrow},
{\it i.e.} taking the limit $\a \to 0$, means the ``large volume limit.''
Indeed, according to the identification of the parameters \eqref{NvolCP1},
in this limit the interesting geometry (and topology) of the Calabi-Yau space $X$
is replaced by the simplest Calabi-Yau 3-fold, namely a flat space:
\be
X \;\overset{\a \to 0}{\leadsto}\; \C^3 \,.
\label{Xatozero}
\ee

In other words, the bottom row of the colored HOMFLY homology is described by
a much simpler ``toy model'' of \eqref{theoryB} in which the pair $(X,L_K)$ is replaced by $(\C^3, L_K)$.
(Not much happens to the Lagrangian submanifold $L_K$ in this limit.)

The next step is to look at this system from the vantage point of the 4-manifold $M_4 \cong \R^4$
and the defect (called the ``surface operator'' \cite{Ramified}) supported on $D \cong \R^2$.
Before we took the limit $\a \to 0$, the compactification on $X$ produces abelian gauge theory
on $M_4$ with gauge group $U(1)$ \cite{KKV}.
Incorporating an extra brane in this setup means including the so-called surface operator supported on $D$
or, mathematically speaking, ramification in the gauge theory on $M_4$.

Let $\CM_{k,m}$ be the moduli space of abelian instantons on $M_4 = \R^4$ with ramification along $D \subset M_4$.
In other words, $\CM_{k,m}$ is the moduli space of solutions to the self-duality equation on $M_4 \setminus D$,
\be
F_A^+ \; = \; 0
\label{sdeq}
\ee
with the second Chern class $k$, with the monopole number $m = \frac{1}{2\pi} \int_D F_A$,
and with the prescribed behavior along $D$.
The latter is what we call the ramification data;
{\it e.g.} a simple example of the so-called \textsl{tame} ramification
can be obtained by introducing a $\delta$-function source
in the self-duality equation \eqref{sdeq} on $M_4$:
\be
F_A^+ \; = \; 2\pi \alpha (\delta_D)^+ \,.
\ee
The gauge connections which solve this equation have a first-order pole at $D$.
More generally, one can study solutions to self-duality equations with singularities of arbitrarily high order,
\be
A = dz  \left( \frac{\alpha_1}{z} + \frac{\alpha_2}{z^2} + \ldots \right) + d \bar z \left( \ldots \right) \,.
\ee
This is called \textsl{wild} ramification and is precisely how the dependence on the knot $K$ will enter,
via the choice of the ramification data.\footnote{For instance, it was conjectured~\cite{DGH} that $(2,2p+1)$ torus knots
correspond to wild ramification of order $p$.}
Let us denote the corresponding moduli space by $\CM_{k,m} (K)$.

Much like the vortex moduli space $\CV_m$ enjoyed an action of the rotation group $U(1)_q$,
the moduli space of ``ramified instantons'' on $M_4 \setminus D \cong \C \times \C^*$
has an action of the rotation group $U(1)_q \times U(1)_t$,
where $U(1)_q$ acts by rotations of $D = \C$ and $U(1)_t$ acts by rotations of its normal bundle, $\C^*$.

Then, in the limit \eqref{Xatozero} the physical interpretation \eqref{HHBPS} of the colored HOMFLY homology predicts
\be
Ch_{q,t} (\CM_{0,m} (K)) \; = \; \bar \CP^{S^m}_{\text{bottom}} (K; q,t)
\ee
which is very close to \eqref{naiveVmP} and, in fact, is exactly the sought-after proper generalization of it.











The connection with vortex equations is now easy to see. At least for some knots
the moduli space $\CM_{k,m} (K)$ can be equivalently described as the moduli space of solutions
to the coupled \textsl{instanton-vortex equations}:
\begin{eqnarray}
F_A^+ & = & 2\pi \phi \otimes \phi^{\dagger} \; (\delta_D)^+  \nonumber \\
*_{D} F_B & = & i \phi^{\dagger} \otimes \phi - i t {\bf 1}_E \label{coupledvort} \\
\bar \partial_{A,B} \phi & = & 0 \nonumber
\end{eqnarray}
where $A$ is a unitary connection on the line bundle $\CL$ over $M_4$,
$B$ is a unitary connection on the bundle $E$ over $D \subset M_4$,
$\phi$ is an element $\phi \in H^0 (\Hom (E,\CL \vert_D ))$, and $\phi^{\dagger}$ is its adjoint.


As far as we know the instanton-vortex equations \eqref{coupledvort} are new and have not appeared in the literature previously.
Their closest cousin is a set of the so-called coupled vortex equations studied {\it e.g.} in~\cite{BGP1,BGP2},
where both $E$ and $\CL$ are bundles over $D$. In other words, our equations \eqref{coupledvort} can be viewed
as analogs of the coupled vortex equations where one of the bundles is extended over $M_4$.
For instance, for a $(2,2p+1)$ torus knot $T^{2,2p+1}$ one takes $E$ to be a unitary bundle of rank $p+1$.

Then, as before, to get the ``bottom row'' of the \textsl{unreduced} $S^m$-colored HOMFLY homology we need to consider
the equivariant character of $\CM_{0,m} (K)$ with instanton number $k=0$ and vortex number $m$.
In situations where $\CM_{k,m} (K)$ can be identified with the moduli space of solutions to \eqref{coupledvort}
this boils down to studying non-abelian vortex equations on $D$.
Thus, for $2p+1$ torus knots we end up with $U(p+1)$ vortex equations,
so that the equivariant character of $\CM_{0,m} (T^{2,2p+1}) \cong \CV_m^{U(p+1)}$
essentially consists of $p+1$ copies of the abelian vortex character that we discussed earlier, {\it cf.} \eqref{unknotvortchar}.

Our prediction is that the equivariant character of the $m$-vortex moduli space $\CV_m^{U(p+1)}$
is the ``bottom row'' of the $S^m$-colored HOMFLY homology of the $(2,2p+1)$ torus knot, {\it i.e.}
\begin{eqnarray}\nonumber
\!\!\!\!\!\!\!\!Ch_{q,t} (\CV_m^{U(p+1)})  &=& \frac{q^{-pm}}{(q;q)_m}  \sum_{0\le k_p \le \ldots \le k_2 \le k_1 \le m}
\left[\!\begin{array}{c} m \\k_1 \end{array}\!\right]\left[\!\begin{array}{c} k_1\\k_2 \end{array}
\!\right]\cdots\left[\!\begin{array}{c} k_{p-1}\\k_p \end{array}\!\right]  \times\\
& & \nonumber \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \times \,\,\, q^{(2m+1)(k_1+k_2+\ldots+k_p)-\sum_{i=1}^p k_{i-1}k_i}
t^{2(k_1+k_2+\ldots+k_p)} ,
\end{eqnarray}
with the convention $k_0:=m$.
For example, when $m=2$ and $p=1$, {\it i.e.} for the $(2,3)$ torus knot (= trefoil knot $3_1$) colored by $\lambda = \tableau{2}$ we have
\be
Ch_{q,t} (\CV_2^{U(2)}) \; = \; q^{-2} \frac{1 + q^3 t^2 + q^4 t^2 + q^6 t^4}{(1-q)(1-q^2)}
\label{S2chtref}
\ee
which can be verified using equivariant $U(2)$ action on $\CV_2^{U(2)}$, see {\it e.g.} \cite{DGH} and \cite{Taipale}.

It would be interesting to understand better the relation between vortex moduli spaces
and the combinatorics of the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}
that also determines the bottom row of the colored HOMFLY homology.
Thus, in the above example \eqref{S2chtref} of the $S^2$-colored trefoil, the corresponding
moduli space of two $U(2)$ vortices $\CV_2^{U(2)}$ has been studied in the literature \cite{Tong,Shifman,Baptista}
and is known to have two strata, which correspond to separated vortices and coincident vortices.
The first stratum --- of complex dimension 4 --- is simply the product of two single-vortex moduli spaces $\CV_1^{U(2)}$,
modulo the permutation of the two vortices,
\be
\CU_1 ( \CV_2^{U(2)} ) \; \cong \; \C \times \frac{\C \times \cp^1 \times \cp^1}{\Z_2}
\ee
with the ``diagonal'' removed.
The second stratum --- of complex dimension 3 ---  is known to be the space of Hecke modifications
(times the center of mass position),
\be
\CU_2 ( \CV_2^{U(2)} ) \; \cong \;  \C \times \mathbb{W} \cp^2_{(1,1,2)} \,.
\ee
See \cite{GS} for color graphics illustrating the bottom row of the $S^2$-colored HOMFLY homology
and the role of $\mathbb{W} \cp^2_{(1,1,2)}$ in its construction.
In this, and more general examples, it would be interesting to match the geometry of these strata
with the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}.

Another direction for future work, already mentioned in Section \ref{sec:Bmodel},
is the relation between theory $\CT_{\text{vortex}} (K)$ and the surface operator theory considered in \cite{FGS2,FGSS}.
Indeed, here, in Section \ref{sec:Bmodel}, and in \cite{FGS2,FGSS} the Poincar\'e polynomial
of the colored HOMFLY homology (a.k.a. the superpolynomial) is realized as a certain index (or, character)
of a two-dimensional $\CN=2$ theory that describes the physics on $D$ in the brane construction \eqref{theoryB}.
Yet, the key difference is that here and in Section \ref{sec:Bmodel} there is a different $\CN=2$ theory
for each choice of ``color'' $\lambda$; the index of such theories determines colored superpolynomials
and {\it a priori} all such theories are unrelated.
In \cite{FGS2,FGSS}, on the other hand, a single $\CN=2$ theory $\CT_K$ (that depends only on the knot $K$)
determines the entire tower of $S^m$-colored homological invariants, via specializations of its supersymmetric index:
\be
\bar \CP^{S^m}_K (a,q,t) \; = \; \CI_{\CT_K} (x = q^m; a,q,t) \,.
\ee
Moreover, recursion relations found in \cite{FGS2,Nawata,FGSS}, which have a natural meaning\footnote{{\it e.g.} the characteristic
variety of the corresponding $q$-difference equations has a nice interpretation as the moduli space of SUSY parameters, {\it etc.}}
in the $\CN=2$ theory $\CT_K$, relate equivariant characters $Ch_{q,t} (\CM_{0,m} (K))$
with different values of the ``vortex number'' $m = \frac{1}{2 \pi} \int_D F$.
Similarly, from the vantage point of Section \ref{sec:Bmodel}, the recursion relations of \cite{FGS2,Nawata,FGSS}
relate B-models with target manifolds of different (super-)dimension
in a way reminiscent of the notions of ``endoscopy'' and ``transfer'' in the geometric Langlands correspondence \cite{FW}.
Thus, in the case of the trefoil knot we have:
\begin{align}
\CP^{S^{m+2}}_{\text{bottom}}
- (q^{-1} - t^2 q^m + (1+q) q^{2m} t^2) \CP^{S^{m+1}}_{\text{bottom}}
& \\
+ t^4 q^{3m-1} (q^m - 1) \CP^{S^{m}}_{\text{bottom}} & = 0 \notag
\end{align}



\begin{appendix}
