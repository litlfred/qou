---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.995
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Define the `center' $Z_0(X)$ of a set $X$ to be the monoid of all functions 
$f\colon X\rightarrow X$ (with composition as product and the identity map as unit.)
Then the usual center $Z_1\equiv Z$ of the monoid $Z_0(X)$
is trivial: $Z_1(Z_0(X))=\{\id_X\}$. The cardinality of $Z_0(X)$ is 
given by $\#Z_0(X)=\#X^{\#X}$. The aim of the present work is to prove 1-categorical
analogues of these trivial set theoretic (= 0-categorical) observations.
(I owe the above definition of $Z_0(X)$ to J.\ Baez.)

Given an arbitrary monoidal category (or tensor category) $\2C$ its center $\2Z(\2C)$
is a braided monoidal category which was defined independently by Drinfel'd (unpublished),
Majid \cite{ma1} and Joyal and Street \cite{js2}. (See Section \ref{sec-semisim} for the
definition.) In order to avoid confusion with another notion of center, we will write
$\2Z_1(\2C)$ throughout. In the present work, as in \cite{ma1, js2}, we will assume $\2C$
to be strict, but this is exclusively for notational convenience. The definition of the
center $\2Z_1$ and all results in this paper extend immediately to the non-strict
case. The other assumptions which we must make on $\2C$ are more restrictive, but we are
still left with a class of categories which appears in contexts like low dimensional
topology and subfactor theory. We assume $\2C$ to be linear over a ground field which is
algebraically closed. Furthermore, $\2C$ is semisimple with simple tensor unit and
spherical \cite{bw2}. (A semisimple category is spherical iff it is pivotal 
\cite{bw2} (=sovereign) and every simple object has the same dimension as its dual, cf.\
\cite[Lemma 2.8]{mue09}.) See \cite{bw2} or \cite[Section 2]{mue09} for the precise
definitions.

\bdefin \label{catdim}
Let $\2C$ be a semisimple spherical tensor category with simple unit and let $\Gamma$ be
the set of isomorphism classes of simple objects. If $\Gamma$ is  finite we define 
\[ \dim\2C=\sum_{i\in\Gamma} d(X_i)^2, \]
otherwise we write $\dim\2C=\infty$. 

If $\2C$ is finite dimensional and braided then the Gauss sums of $\2C$ are given by
\[ \Delta_\pm(\2C)=\sum_{i\in\Gamma} \omega(X_i)^{\pm 1}d(X_i)^2, \]
where $\theta(X)=\omega(X)\id_X$ is the twist of the simple object $X$ which is defined by
the spherical structure \cite{y}. 
\edefin

We can now state our Main Theorem:
\btheor \label{main1}
Let $\7F$ be an algebraically closed field and $\2C$ a spherical $\7F$-linear tensor
category with $\End(\11)\cong\7F$. We assume that $\2C$ is semisimple with finitely many
simple objects and $\dim\2C\ne 0$. Then also the center $\2Z_1(\2C)$ has all these
properties and is a modular category \cite{t}. Furthermore, the dimension and the Gauss
sums are given by
\bean \dim\2Z_1(\2C) &=& (\dim\2C)^2, \\
   \Delta_+ (\2Z_1(\2C)) &=& \Delta_-(\2Z_1(\2C)) = \dim\2C. \eean
\etheor
Defining the center $\2Z_2(\2C)$ of a {\it braided} tensor category $\2C$ to be the 
full subcategory whose objects are those $X$ which satisfy
\[ c(X,Y)=c(Y,X)^{-1} \quad\forall Y\in\obj\,\2C, \]
one easily sees that $\2Z_2(\2C)$ is stable w.r.t.\ isomorphisms (thus replete), direct
sums, retractions, tensor products and duals, the inherited braiding obviously being
symmetric. One can show that a braided category satisfying the properties in the theorem 
(i.e.\ a premodular category \cite{brug1}) is modular iff the center $\2Z_2(\2C)$ is
trivial, in the sense that all objects of $\2Z_2(\2C)$ are multiples of the tensor
unit. (This was done in \cite{khr1} for $*$-categories and in \cite{bebl} for spherical 
categories with $\dim\2C\ne0$, see also Corollary \ref{rem-mod} below.) Thus
$\2Z_2(\2Z_1(\2C))$ is trivial for all $\2C$ as in the Main Theorem, which is the promised
analogue of the 0-categorical observation $Z_1(Z_0(X))=\{\11\}$. 

The Main Theorem can be generalized slightly: If $\2C$ is as before except for $\7F$ not
being algebraically closed then there is a finite extension $\7F'\supset\7F$ 
such that $\2Z_1(\2C\otimes_\7F \7F')$ is modular. Concerning the prospects of further  
generalizations the author is not optimistic. There is little hope of proving
semisimplicity of $\2Z_1(\2C)$ without assuming $\dim\2C\ne 0$. (Furthermore, it is known
\cite{t} that the dimension of a modular category must be non-zero.) In the non-semisimple
case one might hope to prove that the center of a spherical noetherian category satisfies
the non-degeneracy condition on the the braiding introduced in \cite{ly2}. But the methods
of this paper will most likely not apply. 

The results of the present work can be considered as generalizations of known results
concerning Hopf algebras and we briefly comment on this in order to put our results into
their context. We recall that the quantum double of a Hopf algebra was introduced, among
many other things, in Drinfel'd's seminal work \cite{drin}. In the following discussion
all Hopf algebras are finite dimensional over some field $\7F$. The quantum double $D(H)$
of a Hopf algebra $H$ is a certain Hopf algebra which contains $H$ and the dual $\hat{H}$
as Hopf subalgebras and it is generated as an algebra by these. We refrain from repeating
the well known definition and refer to \cite{ka} for a nice  treatment. We only remark
that $D(H)\cong H\otimes_\7F\hat{H}$ as a vector space, thus  
\[ \dim_\7F D(H)=(\dim_\7F H)^2. \]
Furthermore, $D(H)$ is quasitriangular, i.e.\ there is an invertible 
$R\in D(H)\otimes D(H)$ such that $\sigma\circ\Delta=R \Delta(\cdot)R^{-1}$ where
$\sigma$ is the flip automorphism of the tensor product. The constructions of the quantum
double of a Hopf algebra and of the center of a monoidal category are linked by the
equivalence 
\[ D(H)\mbox{-mod} \stackrel{\otimes}{\simeq}_{br} \2Z_1(H\mbox{-mod}) \]
of braided monoidal categories, where $H\mbox{-mod}$ and $D(H)\mbox{-mod}$ are the 
categories of finite dimensional left $H$- and $D(H)$-modules, respectively, the 
braiding of $D(H)\mbox{-mod}$ being provided by the R-matrix. Again, see 
\cite[Chapter XIII.4]{ka} for a detailed account. 

Now, the R-matrix of a quantum double $D(H)$ is non-degenerate in a certain sense, 
$D(H)$ being `factorizable' \cite{rst}. If $H$ is semisimple and cosemisimple then $D(H)$ 
is semisimple \cite{rad}. It then turns out to be also modular and the category 
$D(H)\mbox{-mod}$ of finite dimensional left $D(H)$-modules is modular in the sense of 
Turaev \cite{t}. (This was proved in \cite{eg} for algebras over algebraically closed
fields of characteristic zero, but the latter condition can be dropped. In the appendix we
give a general proof.) Furthermore, one clearly has 
\begin{equation}\dim \2Z_1(H\mbox{-mod}) = \dim D(H)\mbox{-mod} = \dim D(H)=(\dim H)^2 =
   (\dim H\mbox{-mod})^2, \label{dims}\end{equation}
where $\dim\2C$ is the dimension of the monoidal category $\2C$ as defined above.

It is now clear that our Main Theorem can be considered as an extension of the above
results to tensor categories which are not necessarily representation categories of Hopf
algebras. Here one remark on the notation is in order. In \cite{kt} Kassel and Turaev
introduced a modified version of the construction of the center $\2Z_1(\2C)$ and called it
the quantum double $\2D(\2C)$, see also \cite{s}. Their category is the categorical
version of a construction of Reshetikhin (which adjoins a certain square root $\theta$ to
a quasitriangular Hopf algebra $H$ in order to turn it into a ribbon algebra $H(\theta)$)
applied to a quantum double, cf.\ \cite[Theorem 5.4.1]{kt}. In the context of \cite{kt}
the starting point was that even if $\2C$ is rigid this need not be true for $\2Z_1(\2C)$,
whereas the category $\2D(\2C)$ is rigid. As we will see, spherical categories (tensor
categories with nice two sided duals) are better behaved in the sense that their centers
$\2Z_1$ are again spherical. In addition, whereas $\2Z_1(\2C)$ is modular for the
categories satisfying the conditions of our Main Theorem, this is never true for
$\2D(\2C)$! This is why we stick to the original definition $\2Z_1(\2C)$. Apart from
writing $\2Z_1(\2C)$ instead of $\2Z(\2C)$, we do not attempt to change the established
symbols, but we use the expression `quantum double' as a synonym for $\2Z_1(\2C)$ rather
than $\2D(\2C)$. 

Unfortunately, the work on Hopf algebras mentioned above provides no clues on how to prove 
Theorem \ref{main1}. This is where subfactor theory enters the present story. Starting from
an inclusion $N\subset M$ of hyperfinite type $II_1$ factors of finite index and depth,
Ocneanu \cite{ocn2} defined an `asymptotic subfactor' $B\subset A$: 
\[ B=M \vee (M_\infty\cap M')\subset M_\infty=A. \]
(Here $N\subset M\subset M_1\subset M_2\subset\ldots$ is the Jones tower associated with
$N\subset M$ and $M_\infty=\vee_i M_i$.) In \cite{ocn3} he argued that a certain monoidal
category associated with $B\subset A$ is braided, concluding that the asymptotic subfactor
is an `analogue' of Drinfel'd's quantum double of a Hopf algebra. In fact, Ocneanu does
not use category language and does not refer to the quantum double (center) of monoidal
categories. In \cite{ek1} Evans and Kawahigashi published proofs for most of Ocneanu's
announcements. In the paper \cite{lre}, which otherwise has little to do with the
asymptotic subfactor, Longo and Rehren then constructed a subfactor $B\subset A$ 
from an infinite factor $M$ and a -- in our language -- finite dimensional full monoidal 
subcategory $\2C$ of $\End(M)$ and conjectured that it is related to Ocneanu's
construction. This conjecture was made precise and proven in \cite{mas}.
The author's involvement in the present story began when in 1998 he received
a copy of a short preprint \cite{iz1} by M. Izumi. In the meantime a full account 
of Izumi's results has appeared in \cite{iz2}. In \cite{iz1,iz2} Izumi gives an in-depth
analysis of the LR-subfactor, in particular its $B-B$ sectors. Seeing \cite{iz1} the
present author was struck by the fact that its main theorem implicitly contained the
definition of the center of a monoidal category. In fact properly formulated, Izumi's
results provide a precise and completely general form of Ocneanu's `analogy' between
the asymptotic subfactor (or the LR-subfactor) and the quantum double, albeit the 
categorical one instead of the one for Hopf algebras. In Section \ref{ss-subf} we will
rephrase Izumi's results in categorical language to make this evident. Yet, this is not
the main purpose of the present work.

In \cite{ocn3} it has been argued that the braided monoidal category associated with 
$B\subset A$ is modular and a complete proof has been provided in \cite{iz2}, where 
it was also shown that the dimension of the category in question is given by $(\dim\2C)^2$.
As in our discussion of the Hopf algebra quantum double, it is again natural to ask
whether a purely categorical version of these results can be proven. Here we have to face
the problem that finite-index subfactors have a lot of `in-built' categorical structure
which is not a priori available in a purely categorical setting. (In particular, most of
\cite{iz2} strongly relies on this structure.) Yet this problem can be overcome once one
realizes that the more algebraic part of subfactor theory can be cast into the language of
2-categories. This is the content of \cite{mue09}, which in a sense can be considered a
continuation of \cite{lro}, though in a somewhat more general setting.

The paper is organized as follows. In Section 2 we first recall some of the less standard 
definitions from \cite{mue09}. We then summarize the main results of \cite{mue09} on
Frobenius algebras in tensor categories, related 2-categories and the notion of weak
monoidal Morita equivalence of tensor categories. This section can by no means replace
\cite{mue09}. Our study of the quantum double $\2Z_1(\2C)$ begins in Section
\ref{sec-semisim}, where we show that it preserves the closedness w.r.t.\ direct sums and
subobjects and sphericity. Most importantly and least trivially, we prove the
semisimplicity of $\2Z_1(\2C)$. These results do not yet rely on the machinery of
\cite{mue09}. In Section \ref{sec-morita} we prove the weak monoidal Morita equivalence  
$\2Z_1(\2C)\approx\2C\otimes_\7F\2C^\op$, which in particular implies that the double
construction squares the dimension of the category. Section \ref{sec-modular} is devoted
to the proof of modularity of $\2Z_1(\2C)$, equivalent to triviality of the category
$\2Z_2(\2Z_1(\2C))$. As an important first step we analyze the structure of the simple
objects of the double, providing an explanation for Ocneanu's `tube algebra'. 
The next two sections consider the case of categories with a positive $*$-structure
($C^*$-categories or unitary categories) and the special case where $\2C$ is already
braided. In Section \ref{sec-appl} we consider applications to the invariants of
3-manifolds, proving a conjecture of Gelfand and Kazhdan and speculating about a far
stronger result. Finally, we establish the link with subfactor theory, relying heavily on
Izumi's work, improving on it only slightly.
