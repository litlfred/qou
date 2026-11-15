---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-001-11-the-framework
section_title: "The framework"
section_number: 1.1
pages: 1-5
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.947
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-intropart1}

In this paper we study the quantum group 
$\Uq=\Uq(\mathfrak{sl}_2)$, where $q$ is 
a root of unity, its category of 
tilting modules $\T$ and the category 
of projective endofunctors $\Endo(\T)$ 
combinatorially and diagrammatically.




Everything we do is completely explicit and ``down to earth'', 
but motivated and deduced from a general machinery that 
comes, from the side of representation theory, from 
pioneering work of Soergel~\cite{soe1}, 
Beilinson-Ginzburg-Soergel~\cite{bgs}, 
Kazhdan-Lusztig~\cite{kalu} and 
Stroppel~\cite{st2}, and from the side of 
combinatorics and diagrammatics, from work of
Soergel~\cite{soe2}, Khovanov-Lauda~\cite{kl5} 
and Elias-Khovanov~\cite{ek1}.



Let us motivate and explain our approach.





\subsubsection{Quantum groups at roots of unity: non-semisimplicity, modular representation theory and affine Weyl groups}\label{subsub-intropart1}
Fix a simple complex Lie algebra $\mathfrak{g}$. 
Then the finite-dimensional\footnote{If not otherwise stated: 
modules in this paper are assumed to be finite-dimensional. 
There are only few exceptions in this paper, e.g. $\Tn{\bbin}$ 
from Definition~\ref{defn-tiltgen}. We hope it is clear from the context.} representation 
theory of the quantum deformation $\Uv(\mathfrak{g})$ 
of $\Uu(\mathfrak{g})$ is, for \textit{generic} parameter $v$, 
semisimple and very similar to the classical representation theory for $\Uu(\mathfrak{g})$.



This drastically changes when specializing $v$ 
to an $l$-th (we allow any $l>2$ throughout the paper) 
root of unity $q$: the representation theory 
of $\Uq(\mathfrak{g})$ is non-semisimple. 
This is mostly due to the fact that the so-called 
Weyl modules at roots of unity are, in 
general, \textit{not simple} and filtrations by 
Weyl modules \textit{do not necessarily split}. 
A lot of questions remain open about the 
representation theory at roots of unity. 
In fact, the representation 
theory of $\Uq(\mathfrak{g})$ over $\mathbb{C}$ has 
many similarities to the representation theory 
of a corresponding almost simple, simply connected 
algebraic group $G$ over an algebraically closed 
field $K$ of prime characteristic, see 
for example~\cite{ajs} or~\cite{lu1}.



It turns out, when studying the 
representation theory of $\Uq(\mathfrak{g})$, 
a certain category of \textit{tilting modules} $\T$ 
comes up naturally. The category $\T$ is inspired 
by the corresponding category of tilting modules 
for reductive algebraic groups due to Donkin~\cite{don} 
(see also Ringel~\cite{ringel}) and shares most of its 
properties, see for example~\cite{an1}. It is our main object under study in this paper.




Note that the ``combinatorics'' (the irreducible characters) 
of $G$ and $\Uq(\mathfrak{g})$ was conjectured by 
Lusztig (see~\cite{lu3} for $G$ and~\cite{lu1} for 
$\Uq(\mathfrak{g})$) to be related to values at $1$ 
of the Kazhdan-Lusztig polynomial associated to the 
\textit{affine} Weyl group for $\mathfrak{g}$. In addition, 
Kazhdan and Lusztig proved later that the category 
of finite-dimensional $\Uq(\mathfrak{g})$-modules 
(of type $1$) is equivalent to a category of 
modules for the corresponding affine Kac-Moody algebra, see~\cite{kalu}.



This combined with the solution of Kashiwara 
and Tanisaki~\cite{kt} of the Kazhdan-Lusztig 
conjecture in the affine Kac-Moody case then 
solved the above mentioned conjecture for the 
irreducible characters of $\Uq(\mathfrak{g})$. 
Even closer related to our work: Soergel first 
conjectured in~\cite{soe3} and later proved 
in~\cite{soe4} a corresponding statement about 
indecomposable tilting modules. In our 
little $\mathfrak{sl}_2$ case we do not need 
these deep results because we can work out 
both, the irreducible characters and the 
indecomposable tilting modules, \textit{``by hand''}. 






\subsubsection{Categorification and graded categories}\label{subsub-intropart3}




A ground-breaking development towards 
giving an 
\textit{algebraic} proof of the Kazhdan-Lusztig conjectures 
was initiated by Soergel in~\cite{soe2}. He defines a 
combinatorial category $\mathcal S$ consisting of 
objects that are bimodules over a polynomial ring $R$. 
These bimodules are nowadays commonly called 
Soergel bimodules and are indecomposable 
direct summands of tensor products of certain 
algebraically/combinatorially defined $R$-bimodules.




His category is additive, monoidal and graded 
and he proves that its Grothendieck group $K_0$ 
is isomorphic to an integral form of the Hecke algebra 
$H_v(W)$ associated to the Weyl group $W$ of the simple 
Lie algebra $\mathfrak{g}$ in question. Here the grading 
and the corresponding shifting functors give on the level 
of Grothendieck groups rise to the indeterminate $v$ of $H_v(W)$.
Thus, we can say that Soergel's has 
\textit{categorified} $H_v(W)$ (actually, the 
categorification works for any Coxeter group $W$ 
and its associated Hecke algebra $H_v(W)$).



In fact, in the spirit of categorification 
outlined by Crane and Frenkel in the mid-nineties, 
\textit{graded} categories $\mathcal C$ 
(or \textit{graded} $2$-categories) give rise to a structure 
of a $\bZ[v,v^{-1}]$-module on $K_0(\mathcal C)$ 
(where ``shifting decategorifies'' to multiplication by $v$). 
Many examples of this kind of categorification are 
known. For example, Khovanov's categorification 
of the Jones polynomial (sometimes also called 
$\mathfrak{sl}_2$-polynomial)~\cite{kh1}, Khovanov-Rozansky's categorification 
of the $\mathfrak{sl}_n$-polynomial in~\cite{kr1} (all of these, 
although originally defined differently, 
can be obtained using $2$-functors on graded $2$-categories), 
or Khovanov-Lauda and Rouquier's categorification of 
$\Uv(\mathfrak{g})$ and its highest weight modules, 
see for example~\cite{kl5} and~\cite{rou} using the so-called 
Khovanov-Lauda Rouquier algebra, are among 
the more popular ones and have opened new directions of research.



Thus, it is natural to ask if we can introduce 
a \textit{non-trivial grading} on $\T$ as well. 
We do this in Section~\ref{sec-quiver} by using 
an argument pioneered by Soergel (see~\cite{soe1}) 
in the ungraded and Stroppel (see~\cite{st2}) in 
the graded case for category $\mathcal O$. Namely, 
the usage of Soergel's combinatorial functor $\mathbb{V}$ 
that gives rise to an equivalence of a block of 
$\mathcal O$ (for $\mathfrak{g}$) and a certain 
full subcategory of $\ModA$. The algebra $A$ is 
the endomorphism ring of the \textit{anti-dominant projective} 
in the block and it can be explicitly (when the block is regular) 
identified with the algebra of coinvariants for the Weyl group 
associated to $\mathfrak{g}$. This algebra can be given a 
\textit{$\bZ$-grading} and, as Stroppel explains in~\cite{st2}, 
this set-up gives rise to \textit{graded} versions of 
blocks of category $\mathcal O$ and the categories of 
\textit{graded} endofunctors on these blocks.
In fact, as Stroppel explains in~\cite{st2}, her 
approach is a combinatorial alternative to the 
approach of Beilinson, Ginzburg and Soergel given in~\cite{bgs}.



As in the other cases above, the \textit{grading} 
is the crucial point: in category $\mathcal O$ the 
multiplicity $[\Vn{\lambda}:\Ln{\mu}]$ of the 
simple module $\Ln{\mu}$ inside of the Verma 
$\Vn{\lambda}$ is given by evaluating the 
corresponding Kazhdan-Lusztig polynomial at $1$. 
The Kazhdan-Lusztig polynomial is a polynomial 
and not just a number and the grading of $\mathcal O$ 
``explains'' now the \textit{individual coefficients} of these polynomials as well.



In our case the role of $A$ is, as we explain 
in Section~\ref{sec-quiver}, played by an 
``infinite version'' $\Ai$ of a quiver algebra 
$\Am$ that Khovanov and Seidel introduced in~\cite{ks1} 
in their study of Floer homology\footnote{Around the 
same time this quiver algebra was considered 
independently by Braden in~\cite{bra}. We stay with Khovanov and Seidel's formulation 
(but write $\Am$ instead of $A_m$ as they do)
because the functors they considered on the category 
of representations of this algebra are closely 
connected to translation functors in our context.}. 
Its ``Koszul version'' appears in various contexts 
related to symplectic topology, algebraic geometry and representation theory. 
In particular, it appears as a subquotient of Khovanov's arc algebra that 
he introduced in~\cite{kh4} to give an algebraic structure 
underlying Khovanov homology and whose representation 
theory is known to be highly interesting as outlined 
in a series of papers by Brundan and Stroppel, 
see~\cite{bs1},~\cite{bs2},~\cite{bs3},~\cite{bs4} 
and~\cite{bs5}. The grading can be seen as coming from the 
corresponding grading of some Khovanov-Lauda Rouquier algebra and we use it 
to introduce the grading on $\T$ (for each block $\T_{\lambda}$) 
and we obtain a graded category $\Tgr$. 



We stress that this grading is a ``\textit{root of unity phenomenon}'': 
the category of finite-dimensional $\Uv$-modules is 
semisimple and has therefore no interesting grading. 
On the other hand, the grading on $\Tgr$ is non-trivial 
and gives for example rise (as mentioned above) to a 
grading for similar modules of reductive algebraic groups over 
algebraical closed fields $K$ of prime characteristic.



Thus, an intriguing question is if one can use 
the grading on $\Tgr$ to obtain new information 
about link invariants or about the 
Witten-Reshetikhin-Turaev invariants 
of $3$-manifolds that can be deduced from $\T$, see~\cite{an1} 
or~\cite{tur}. Note 
that, as we deduce in Remark~\ref{rem-grothendieck1a}, 
each block $\Tgrl$ of $\Tgr$ decategorifies to the 
Burau representation of the braid group 
$B_{\infty}$ with $\infty$-many strands 
(the split Grothendieck group $K_0^{\oplus}$ carries an action of $B_{\infty}$), 
which already gives a hint how these topological invariants could be related to our work.




\subsubsection{Diagram categories, biadjoint functors and diagrammatic categorification}\label{subsub-intropart4}








Khovanov and Lauda have categorified 
$\Uv(\mathfrak{sl}_k)$, see~\cite{kl5}. 
Their approach, that has turned out to be very fruitful, was to 
use \textit{diagrammatic categorification}: 
they defined a certain $2$-category $\mathcal U(\mathfrak{sl}_k)$ 
consisting of a certain type of so-called string diagrams 
whose (split) Grothendieck group 
$K_0^{\oplus}(\mathcal U(\mathfrak{sl}_k))$ gives the idempotented, integral form $\Uvd(\mathfrak{sl}_k)_{\bZ}$ of $\Uv(\mathfrak{sl}_k)$. One of 
their main observations was that the $E$'s and $F$'s of 
$\Uvd(\mathfrak{sl}_k)_{\bZ}$ behave like biadjoint 
induction and restriction functors on certain categories. 
As outlined in an even more general framework by Khovanov 
in~\cite{kh5} (although it was folklore knowledge for some 
years and appears in a more rigorous form in for 
example~\cite{js} or~\cite{mueg}), biadjoint functors 
have a \textit{``built-in topology''} since, roughly, 
biadjointness means that we can straighten out diagrams.


Let us denote by $B_i$ the bimodules from Soergel's 
categorification of the Hecke algebra $H_v(W)$ from above.
A main feature of the $B_i$'s is 
that tensoring with $B_i$ is a self-adjoint endofunctor 
and, even stronger, a \textit{Frobenius object}, i.e. there are morphisms
\[
B_i\to R,\quad R\to B_i,\quad B_i\to B_i\otimes_R B_i\quad\text{and}\quad B_i\otimes_R B_i \to B_i
\]
pictured as (we read from bottom to top and right to left)
\[
\xy
(0,-3)*{\includegraphics[scale=0.8]{res/figs/diacath/iso3}};
(0,8)*{\scriptstyle R};
(0,-9)*{\scriptstyle B_i};
\endxy\quad,\quad
\raisebox{-0.025cm}{\xy
(0,3)*{\rotatebox{180}{\includegraphics[scale=0.8]{res/figs/diacath/iso3}}};
(0,9)*{\scriptstyle B_i};
(0,-8)*{\scriptstyle R};
\endxy}\quad,\quad
\xy
(0,0)*{\includegraphics[scale=0.8]{res/figs/diacath/iso4}};
(-6.5,8)*{\scriptstyle B_i};
(0,8)*{\scriptstyle \otimes};
(6.5,8)*{\scriptstyle B_i};
(0,-9)*{\scriptstyle B_i};
\endxy
\quad,\quad
\xy
(0,0)*{\rotatebox{180}{\includegraphics[scale=0.8]{res/figs/diacath/iso4}}};
(-6.5,-9)*{\scriptstyle B_i};
(0,-9)*{\scriptstyle \otimes};
(6.5,-9)*{\scriptstyle B_i};
(0,8)*{\scriptstyle B_i};
\endxy
\]
that satisfy the \textit{Frobenius relations} (plus reflections of these)
\[
\text{\textbf{Frob1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob2}};
\endxy=
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob1}};
\endxy\quad,\quad\text{\textbf{Frob2}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob3}};
\endxy\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob5}};
\endxy
\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob4}};
\endxy
\]
It is tempting to ask if one can give a 
\textit{diagrammatic} categorification in 
the spirit of $\Uu_v(\mathfrak{sl}_n)$-string 
diagrams of Khovanov-Lauda (see~\cite{kl5}) for
Soergel's categorification as well. The observations 
from above, as Khovanov explains in~\cite[Section~3]{kh5}, 
were the main reason why Elias and Khovanov started to look for such a description.



They were (very) successful in their search 
and their diagrammatic categorification given 
in~\cite{ek1} (in fact, the diagrams 
above are the ones they use) has inspired many successive works. 
Most mentionable for this paper: Elias' 
categorification $\D$ of the Hecke algebra 
$H_v(D_{\infty})$ 
(where $D_{\infty}$ is the infinite dihedral group) 
from~\cite{el1} called 
the \textit{dihedral cathedral} or, alternatively, the 
presentation in terms of
generators and relations 
of the same category given by Libedinsky~\cite{lib}.



This has already led to seminal results: 
as Elias and Williamson explain in~\cite[Subsection~1.3]{ew2}, 
their algebraic proof that the Kazhdan-Lusztig polynomials have positive 
coefficients for \textit{arbitrary} Coxeter 
systems was discovered using the diagrammatic framework 
from~\cite{ew1} and~\cite{ew3}.



In our context: the combinatorics of the 
blocks $\T_{\lambda}$, as explained in Subsection~\ref{sub-translation}, 
is mostly governed by two functors $\Theta_s$ 
and $\Theta_t$ called translation through the 
$s$ and $t$-wall respectively. Here 
$s$ and $t$ are the two reflections that generate 
the \textit{affine} Weyl group 
$W_l\cong D_{\infty}$ of $\mathfrak{sl}_2$.
These functors, motivated from the category $\mathcal O$ 
analogs, are \textit{biadjoint} and satisfy 
\textit{Frobenius relations}. Moreover, we show in 
Lemma~\ref{lem-adjoint} and Theorem~\ref{thm-struktursatz2} 
that this \textit{still holds} in the graded setting.
Thus, it seems reasonable to expect that 
$\Tgrl$ and its category of (graded) projective endofunctors 
$\Endo(\Tgrl)$ have a \textit{diagrammatic} 
description as well. And, since $W_l\cong D_{\infty}$, 
it seems reasonable to expect a relation to Elias' \textit{dihedral cathedral} 
$\D$ from~\cite{el1}. We prove this in Section~\ref{sec-dia} by 
introducing certain quotients of $\D$ giving rise to a diagrammatic presentation 
of $\Tgrl$ and $\Endo(\Tgrl)$.
