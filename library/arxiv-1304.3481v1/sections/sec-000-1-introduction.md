---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.986
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
The categorification of quantum knot invariants started with Khovanov's seminal paper \cite{Khfirst}, where he defined a doubly-graded homology theory, whose homotopy type is an invariant of a knot, and such that its graded Euler characteristic is equal to the Jones polynomial. This opened a fast-growing field in low-dimensional topology and started work on categorification of other quantum knot invariants. Unlike the quantum polynomial invariants of a knot $K$, denoted by $P^{g,\lambda}(K)(q)$, which are explicitly defined for any representation $\lambda$ of Lie algebra $g$, their categorifications are known only in very few cases. In particular, in the case of the Lie algebras $sl(N)$ --- which is the case on which we focus in this paper --- the explicit categorification is known in the case of the fundamental representations $\lambda=\tableau1$ \cite{KRa}, and in a very few other cases. In addition, apart from the case of the Jones polynomial (fundamental representation of $sl(2)$), the definition of the homology theory is very complicated, which makes the computation of such invariants extremely hard.

For a fixed Young diagram $\lambda$ and a knot $K$, the $sl(N)$ quantum polynomials $P^{sl(N),\lambda}(K)(q)$ can be organized in a single two-variable $\lambda$-colored HOMFLY polynomial $P^{\lambda}(K)(a,q)$, so that the $sl(N)$-quantum polynomials are obtained as $a=q^N$ specializations, i.e.
\be
P^{sl(N),\lambda}(K)(q)=P^{\lambda}(K)(a=q^N,q).
\label{PPN}
\ee
A triply-graded homology categorifying uncolored ($\lambda=\tableau1$) HOMFLY polynomial was defined in \cite{KRb}. Throughout the paper, we are mainly focusing on the reduced polynomials, i.e. normalized such that the value of the unknot is equal to 1, and unless otherwise stated, the (colored) HOMFLY polynomial means the reduced (colored) HOMFLY polynomial.

A remarkable property of the quantum knot invariants and their categorifications is that they are related to many different areas of mathematics and physics, all of them bringing new viewpoints to this topic. The relationship between quantum field theory, in particular the Chern-Simons theory, and the quantum knot invariants was discovered in celebrated paper by Witten \cite{Witt}, and the physics insights have been extremely fruitful ever since.

In the case of the categorifications, the realization of knot homologies as the space of certain BPS states gave rise to various prediction on the structure of the (colored) HOMFLY homologies, see e.g. \cite{GSaberi} for a friendly introduction and a review.
Thus, in \cite{DGR} N. Dunfield, the second author and J. Rasmussen predicted the existence of a triply-graded knot homology theory $\CH^{\tableau1}(K)$, whose Euler characteristic is given by the HOMFLY polynomial, and which comes equipped with the collection of anti-commuting differentials $\{d_N\}_{N\in\Z}$ lifting the $sl(N)$ specialization property of the HOMFLY polynomial. More precisely, the differentials $d_N$, for $N>0$, are such that the homology of $\CH^{\tableau1}(K)$ with respect to $d_N$ is isomorphic to the homology $\CH^{sl(N),\tableau1}(K)$ that categorifies $P^{sl(N),\tableau1}(K)(q)$. Additionally, $\CH^{\tableau1}(K)$ has an involution $\phi$ extending the $q\leftrightarrow q^{-1}$ symmetry of the HOMFLY polynomial:
\be
P^{\tableau1}(K)(a,q)=P^{\tableau1}(K)(a,q^{-1}),
\ee
It exchanges the positive and negative differentials: $\phi d_N = d_{-N} \phi$.

Such a rigid structure enabled the computation of triply graded homology of various knots. In addition such a triply-graded homology theory was constructed mathematically in \cite{KRb}, and it was shown in \cite{Ras} that it also carries  the differentials $d_N$ with the wanted properties.


In \cite{GS} the second and the third authors extended this picture and described various structures in the {\em colored} HOMFLY homology in the case of the symmetric ($S^r$) and anti-symmetric ($\Lambda^r$) representations. For such representation $\lambda$ and a knot $K$ one can associate an $(a,q,t)$-graded vector space $\CH^{\lambda}(K)$ such that its Euler characteristic with respect to the $t$-grading equals to the $\lambda$-colored HOMFLY polynomial $P^{\lambda}(K)(a,q)$ of $K$. Like in the uncolored case, these homology theories come with the collection of the differentials corresponding to the $sl(N)$ specializations. The main new feature is the existence of another collection of the so-called {\em colored} differentials which give ``dynamics'' in the sequence of the homology theories $\CH^{S^r}(K)$, for various $r$. For every pair of nonnegative integers $r$ and $k$ with $r>k$ there are two different differentials  $d^{+}_{S^{r}\to S^{k}}$ and $d^{-}_{S^{r}\to S^{k}}$ on $\CH^{S^r}(K)$ such that the homology of $\CH^{S^r}(K)$ with respect to any of the two differentials $d^{\pm}_{S^{r}\to S^{k}}$ is isomorphic to $\CH^{S^k}(K)$.

The involution $\phi$  becomes the so-called {\em mirror symmetry} in colored homology, that relates the homologies $\CH^{\lambda}(K)$ and $\CH^{\lambda^t}(K)$: there exists an isomorphism between $\CH^{S^r}(K)$ and $\CH^{\Lambda^r}(K)$  preserving the $a$-grading and reversing the $q$-grading. It lifts the following relation between the colored HOMFLY polynomials
\be
P^{\lambda}(K)(a,q)=P^{\lambda^t}(K)(a,q^{-1}).
\label{PPmir}
\ee


Surprisingly, in \cite{GS}
it was realized that the {\em exponential growth property} holds for certain classes of knots, i.e. the size of the $S^r$-colored homology grows exponentially in $r$:
\be
\dim \CH^{S^r}(K)=\left(\dim \CH^{\tableau1}(K) \right)^{r}.
\ee
Although this property does not hold for all knots, it holds for various large classes of knots, like 2-bridge knots and torus knots. Moreover, the refined exponential growth is valid  for the two-variable $q=1$ specializations of the Poincar\'e polynomials of the corresponding homology theories. 

Such a large predicted structure made possible the explicit computation of colored HOMFLY homologies for various knots and colors, that in turn have shown the consistency of all
the conjectured properties.\\



In present article we give more quantitative description of the results of \cite{GS}.
 We extend the description of the colored differentials and the exponential growth conjecture to rectangular diagrams $\lambda$. This allows us to give a more unified treatment of the $\Lambda^r$ and $S^r$ colored homology.

The major novelty is endowing the space $\CH^{\lambda}(K)$ with the fourth grading. In other words, we conjecture the colored HOMFLY homology $\CH^{\lambda}(K)$ of a knot $K$ to carry four independent gradings, which we will denote by $a,q,t_{r},t_{c}$: apart from the $a$  and $q$ gradings from the polynomial invariants, we introduce two homological (or refined) $t$-gradings, denoted $t_r$ and  $t_c$.  Both $t$-gradings on the HOMFLY homology give a categorification of $P^{\lambda}(K)$. In other words, if $\CP^{\lambda}_r(K)$ and $\CP^{\lambda}_c(K)$ are three-variable Poincar\'e polynomials of $\CH^{\lambda}(K)$ with respect to $t_r$ and $t_c$ gradings, respectively, then
\[
\CP^{\lambda}_r(K) (a,q,t_{r}=-1) \; = \; \CP^{\lambda}_c(K) (a,q,t_{c}=-1) \; = \; P^{\lambda}(K)(a,q),
\]
The appearance of the fourth grading is yet mysterious for us from geometric point of view, but it seems to be inevitable. Let us list some of the evidences.

First of all,
in such a way we managed to reconcile the two different conventions
for the homological grading in the case of symmetric representations:
 $t_r$ is the $t$-grading assigned to a generator of $\CH^{\lambda}(K)$
in the grading conventions of \cite{GS}, whereas one can interpret $t_{c}$ as
the $t$-grading assigned to a generator of $\CH^{\lambda}(K)$ in grading conventions of \cite{AShakirov,DMMSS,DGR,GWalcher}.
The ``mirror symmetry'' exchanges the two grading conventions. Therefore, one practical application of
``mirror symmetry'' is that it allows to convert from one set of grading conventions used in the literature
to the other one by looking at the HOMFLY homology of the knot colored by transposed Young tableaux $\lambda^t$.

One advantage of the quadruply-graded theory is that it makes
all of the structural properties and isomorphisms completely explicit. This cannot be achieved within a triply-graded theory: for example in the case of the symmetric representations (see \cite{GS}) only a few of the isomorphisms and symmetries could be made explicit.
Now, quadruply-graded theory $\CH^{\lambda}(K)$ has remarkable properties: it gives an explicit re-gradings of all colored isomorphisms, enables
explicit expression in all gradings for the mirror symmetry, and makes the exponential growth property manifest as a fully refined exponential growth property of three-variable polynomials. In addition, miraculously, we discovered a new symmetry on $\CH^{\lambda}(K)$ that we call {\em self-symmetry}. This symmetry requires all four gradings, and unlike the mirror symmetry it does not lift any known relation
of the colored HOMFLY polynomials.

What is even more surprising, is that all these symmetries, isomorphism re-gradings and exponential growth property have
rather simple and pleasant expressions. Moreover, all of them
become particularly elegant when expressed in terms of an auxiliary
grading, called $Q$-grading, defined in the following simple way when $\lambda$ is a rectangular Young diagram with $R$ rows:
\be\label{Qgrad}
Q=\frac{q+t_r-t_c}{R}.
\ee
This new grading, which can be considered as a certain ``corrected'' $q$-grading,  cannot be seen on the decategorified, polynomial level, and as the formula indicates, both $t$-gradings are
needed for its definition. Therefore we need the quadruply-graded theory in order to have all properties manifest,
while only a small fraction of this rich structure can be seen at the polynomial, ``decategorified'' level.

Finally, the symmetries take the most elegant form when the homology is written in $(a,Q,t_r,t_c)$-gradings. Because of a linear relation between the gradings (\ref{Qgrad}), this is just a simple re-grading of $\CH^{\lambda}(K)$. However, due to its importance, we give it a special name, $\tilde{\CH}^{\lambda}(K)$, and refer to it as the {\it tilde-version} of colored HOMFLY homology. Thus, it is given by
\be
\tilde{\CH}^{\lambda}_{i,j,k,l}(K) \; := \; {\CH}^{\lambda}_{i,Rj-k+l,k,l}(K).
\ee

We note that only in the uncolored case the $t_{r}$ and $t_{c}$ gradings coincide (as well as $Q$ and $q$ gradings), and the resulting homology is triply graded in agreement with \cite{DGR}.\\


The second major novelty is that we extend the definition of the differentials $d_N$ to a two-dimensional family of differentials $d_{n|m}$ labeled by Lie superalgebras ${sl}(n|m)$. Then, the value of $N$ from the familiar one-parameter family of the differentials $\{ d_N \}$ corresponds to the difference $n-m$ which is precisely the super-rank of ${sl}(n|m)$. This gives a much more natural treatment of the differentials $d_N$, for non-positive $N$, together with their gradings. We show that these new differentials are nontrivial even in the uncolored homology (for sufficiently large knots) and bring an interesting structure both to colored and uncolored knot homology. We also describe explicitly the interaction between the differentials  $d_{n|m}$ and the colored differentials for the rectangle-colored homology.

While it still deserves a much deeper understanding, the appearance of $sl(n|m)$ is natural for a number reasons. Primarily, the representation theory of $sl(n|m)$ explains the behavior of the colored differentials. For each rectangular Young diagram $\lambda$ we define colored differentials removing any number of columns or rows from $\lambda$. These differentials naturally appear from the identification of the representations of the superalgebra $sl(n|m)$ labeled by two different rectangles $\lambda$ and $\mu$. It turns out that these are such that $\mu$ is obtained from $\lambda$ by erasing some of its rows or some of its columns.  Then, the corresponding colored differential,
$d_{\lambda \to \mu}$, closes the following commutative diagram:

\begin{center}
\begin{tabular}[c]{ccc}
$\CH^{\lambda}(K)$ & $\xrightarrow{d_{\lambda\to \mu}}$ & $\CH^{\mu}(K)$\cr
 $\vline$ & & $\vline$ \cr
${d_{n|m}}$ & & ${d_{n|m}}$\cr
 $\downarrow$ & & $\downarrow$ \cr
$\CH^{sl(n|m),\lambda}(K)$ & $\xrightarrow{\qquad \cong\qquad}$ & $\CH^{sl(n|m),\mu}(K)$
\end{tabular}
\end{center}

Furthermore, the differentials $d_{n|m}$ on $\CH^{\lambda}(K)$ exist for all pairs of nonnegative integer $(n,m)$ such that the superalgebra $sl(n|m)$ has a representation corresponding to the Young diagram $\lambda$. In such a way, all differentials have natural interpretation, unlike the single-parameter family of differentials $\{d_N\}_{N\in\Z}$ for which only the ones with $N>0$ have clear interpretation as $sl(N)$ specialization differentials.
In addition, supergroups and the corresponding Lie superalgebras are familiar in the study of brane/anti-brane systems \cite{VafaUNM,WittenK}:
much like a collection of $N$ coincident D-branes carries a gauge bundle with the structure group $U(N)$, a similar system of $n$ branes and $m$ anti-branes carries $U(n|m)$ gauge symmetry. Therefore, since many physical realizations of knot homologies that we encounter
in sections \ref{sec:geomphys}, \ref{sec:supermn}, \ref{sec:mirror}, and \ref{sec:inst-surf} are based on branes, it is not inconceivable that appearance of supergroups and superalgebras is rooted there (although we will not try to pursue this interpretation in the present paper).\\

Another direction of our study is the construction of the models for colored homology
for certain knots satisfying all above properties. We give a combinatorial model for the unreduced homology of the unknot and study various differentials on it. The HOMFLY homology is conjectured to be a free supercommutative algebra,
\be
\CA \; = \; \CH^{\lambda} (\unknot)
\label{Aunknot}
\ee
and the differentials are described by the Koszul construction. We compare this approach with other mathematical and physical approaches (potentials and matrix factorizations, categorification of the Jones-Wenzl projectors, algebra of BPS states).
We give an algebraic model for the $S^r$ colored homology of torus knots and compare it with the approaches of \cite{GORS} and \cite{EGL}. We study  various differentials in this model as well and show how the differentials $d_{n|m}$ naturally appear from the rational Cherednik algebra. Finally, to demonstrate the full strength and robustness of our approach, we describe the colored homology for the figure eight knot, which is a non-torus knot.






















\subsection{Structure of the paper}

In Section \ref{sec:bosonic} we describe a model for the unreduced colored homology of the unknot.
It is a a free supercommutative algebra $\CA$ with one even and one odd generator per each box of the diagram $\lambda$.
For the representation $S^n$, this algebra can be naturally identified with the algebra of $S_n$-invariant differential forms on $\C^n$. Using the physics of BPS states, we describe some of these even and odd generators geometrically. We also check that the Poincar\'e polynomial for this algebra agrees with the evaluation formulas for the Macdonald polynomial, that various authors \cite{AShakirov,Ch,DMMSS} recently assign to the unknot in the refined Chern-Simons theory.

Both $d_{m|n}$ and the colored differentials can be interpreted as the Koszul differentials on this algebra, sending odd generators to certain polynomials in even generators. We show that the approach of \cite{GWalcher}, where the homology of the unknot is interpreted as the Jacobi ring of a certain potential $W$, fits into this framework if the Koszul complex is associated with the partial derivatives of $W$:
$$d(\xi_i)=\frac{\partial W}{\partial x_i},\ d(x_i)=0.$$
Using this model, we also derive the equations for the colored differentials: if the representations of $sl(m|n)$ labelled by $\lambda$ and $\mu$ are isomorphic, we show that in some  examples the isomorphism between the corresponding Jacobi rings follows from the equation
$$W_{m|n}^{\lambda}(x_1,\ldots,x_{|\lambda|})=W_{m|n}^{\mu}(x_1,\ldots,x_{|\mu|})+W_{\lambda\to \mu}(x_{|\mu|+1},\ldots,x_{|\lambda|}),$$
where $W_{\lambda\to \mu}$ is a non-degenerate quadratic function. We conjecture that the colored differential
$d_{\lambda\to \mu}$ is a Koszul differential associated with the partial derivatives of $W_{\lambda\to \mu}$.

In Section \ref{sec:gradings} we describe the general structures on the colored HOMFLY homology.
We give a detailed list of the properties of the quadruply-graded  colored HOMFLY homology $\CH^{\lambda}(K)$ of a general knot $K$, together with the $sl(n|m)$ and colored differentials. Furthermore we describe explicitly the degrees of all colored differentials and re-gradings in the corresponding colored isomorphisms. We end the section with the two particular features in the case of the symmetric representations: the  $\delta$-grading and the existence of the HFK-like differential on the $S^r$-colored homology. Also, we discuss similarities and differences between the case of rectangle-labeled  representations, which are the main topic of our present paper, and the case of non-rectangular representations.

Section \ref{sec:examples} contains the computations of the quadruply-graded homologies for various knots and representations. Due to a large number of predicted properties such computations present a highly non-trivial check and confirmation of the theory.

Section \ref{sec:algmodel} is devoted to torus knots.
In Section  \ref{sec:torus} we recall the statement about the stabilization of the HOMFLY polynomials of $(p,q)$ torus knots in the limit $q\to \infty$. We relate such stable $\lambda$-colored invariant of $(p,\infty)$ torus knot
to the invariant of the $p\lambda$-colored unknot. Then, we conjecture a similar relation between the corresponding colored homology theories of stable torus knots and that of the unknot. The $\lambda$-colored homology of the finite $(p,m)$ torus knot can be realized as a certain quotient of this stable homology. This allows us to use the algebraic description of the homology of the unknot, and in Section \ref{sec:alggrad} we give a precise description of the generators in the rectangular homology of a torus knot and their quadruple gradings.
We describe and check the structural properties of colored homology using this algebraic model.
We show the existence of a symmetry between $\lambda$- and $\lambda^{t}$-colored homology, exchanging $t_r$ and $t_c$ gradings and preserving the $Q$-grading. We check the refined exponential growth conjecture for the stable homology of torus knots. We also describe respectively the self-duality involution  and the action of differentials in the rectangular homology of torus knots.


Generalizing the results of \cite{GORS} and \cite{EGL}, we identify the
colored homology of torus knots with the certain representations of the rational Cherednik algebra. For $\lambda=S^r$, we make this description precise and describe the space $\CH^{S^r}(T(m,n))$ as a space of differential forms on a certain non-reduced scheme
$$\CM_{m,n,r}:=\{(u_{r+1},\ldots, u_{nr};v_{r+1},\ldots, v_{mr}\ |\ U(z)^m=V(z)^n\},$$
where the polynomials $U(z)$ and $V(z)$ are defined by the equations
$$U(z)=1+z^{r+1}u_{r+1}+\ldots+z^{nr}u_{nr},\ V(z)=1+z^{r+1}u_{r+1}+\ldots+z^{mr}u_{mr}.$$
This description is ideally suited for a realization of colored HOMFLY homology via Landau-Ginzburg B-model,
which is the subject of Section \ref{sec:mirror}.
Using mirror symmetry we also reformulate it in terms of the A-model and Lagrangian Floer homology.
We also provide some explicit formulas for the differentials acting on the HOMFLY homology
and describe $\CH^{S^r}(T(m,n))$ as a Jacobi ring of a certain potential on a supermanifold.

Finally, section \ref{sec:bottom} is devoted to the ``bottom row'' of the HOMFLY homology, i.e. $a=0$ limit.
We compare it to certain combinatorial models of Haglund et. al., generalizing the models for $q,t$-Catalan numbers
which played important role in \cite{GORS}, and to the geometric models for coupled instanton-vortex systems proposed in \cite{DGH}.


\subsection{Acknowledgements}

We are grateful to
M. Abouzaid, M. Aganagic, J.M. Baptista, I. Cherednik,
K. Costello, R. Elliot, P. Etingof, A. Gorsky, K. Hikami, M. Khovanov, B. Kim, A. N. Kirillov and A. A. Kirillov Jr.,
I. Losev, A. Morozov, H. Nakajima, A. Negut,  N.~Nekrasov, A. Oblomkov, A. Okounkov, J. Rasmussen, L. Rozansky,
S. Shakirov, V. Shende, C. Vafa, O. Viro, E. Witten, and C. Woodward
for the useful discussions.
E. G. would like to thank the California Institute of Technology and Kyoto Research Institute for Mathematical Sciences for the hospitality.
The research of E. G. is partially supported by the grants RFBR-10-01-678, NSh-8462.2010.1 and the Simons foundation.
S.G. would like to thank Instituto Superior Tecnico in Lisbon and the Simons Center for Geometry and Physics at Stony Brook for hospitality during the key stages of this work.
The work of S. G. is supported in part by DOE Grant DE-FG03-92-ER40701FG-02 and in part by NSF Grant PHY-0757647.
M. S. would like to thank the California Institute of Technology for hospitality during which part of this work was done. 
The work of M. S. was partially supported by the Portuguese Funda\c c\~ao para a Ci\^encia e a Tecnologia through ISR/IST plurianual funding and through the project number PTDC/MAT/101503/2008, New Geometry and Topology, and by the Ministry of Science of Serbia, project no. 174012.
Opinions and conclusions expressed here are those of the authors and do not necessarily reflect the views of funding agencies.
