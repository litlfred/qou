---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-014-41-the-basics-diagrammatic-categories-additive-c
section_title: "The basics: diagrammatic categories, additive closures and Karoubi envelopes"
section_number: 4.1
pages: 31-46
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.975
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-basiccats}
We consider \textit{diagrammatic} categories 
in the following. We encourage the reader 
to take a look in the rather extensive literature 
(in the authors opinion, a good start is~\cite[Section 2]{lau1}).
Although these categories 
have a natural $2$-categorical structure, 
we phrase everything in terms of $1$-categories.



Furthermore, we note that we \textit{only} use 
$\bC$-linear categories. Recall that a category 
$\mathcal C$ is called $\bC$\textit{-linear} if each 
hom-space $\Hom_{\mathcal C}(O,O^{\prime})$ for 
$O,O^{\prime}\in\Ob(\mathcal C)$ has the 
structure of a $\bC$-vector space and the composition of morphisms is $\bC$-bilinear 
(this includes the existence of 
a zero morphism $0$). 
We use $\bC$\textit{-linear functors} for such categories: 
functors which induce $\bC$-linear maps on each hom-space. 
We, as in Subsection~\ref{sub-grad}, \textit{only} consider ($\bZ$-)graded categories.









\begin{defnn}(\textbf{Additive closure of $\mathcal C$})\label{defn-addclosure} 
Given a $\bC$-linear category $\mathcal C$, we define its \textit{additive closure}, 
denoted by $\Mat(\mathcal C)$, to be the $\bC$-linear category consisting of the following.
\begin{itemize}
\item The objects are finite (possibly empty), 
formal direct sums $\oplus_{i=1}^NO_i$ with $O_i\in\Ob(\mathcal C)$ 
(note that 
the empty object is the zero object).
\item Given two objects $O=\oplus_{k=1}^NO_k,\,O^{\prime}=\oplus_{k=1}^{N^{\prime}}O^{\prime}_k$, then a morphism $F\in\Hom_{\Mat(\mathcal C)}(O,O^{\prime})$ is a $N\times N^{\prime}$ matrix $F=(f_{i^{\prime}i})$ consisting of morphisms $f_{i^{\prime}i}\in\Hom_{\mathcal C}(O_i,O^{\prime}_{i^{\prime}})$.
\item One can add the matrices component-wise and 
scalar multiplication with elements from $\bC$ is also component-wise.
\item Composition of morphisms is multiplication 
of matrices.\maketriqed
\end{itemize}
\end{defnn}

It is easy to check that this definition gives a category.



\begin{defnn}(\textbf{Karoubi envelope of $\mathcal C$})\label{defn-karoubi}
Let $\mathcal C$ be a category and 
$A\in\Ob(\mathcal C)$ be an object of 
$\mathcal C$. Let $e,e^{\prime}\colon O\to O$ 
denote idempotents in $\End_{\mathcal C}(O)$. 
The \textit{Karoubi envelope of} $\mathcal C$, 
denoted by $\Kar(\mathcal C)$, is the following category.
\begin{itemize}
\item Objects are ordered pairs $(O,e)$ 
consisting of an object $O$ and an idempotent $e\in\End_{\mathcal C}(O)$.
\item Morphisms 
$f\colon(O,e)\to(O^{\prime},e^{\prime})$ in $\Kar(\mathcal C)$ 
are all morphisms $f\colon O\to O^{\prime}$ of $\mathcal C$ such that the equations $f=f\circ e=e^{\prime}\circ f$ hold.
\item Compositions are induced by compositions in $\mathcal C$.\maketriqed
\end{itemize}
\end{defnn}

Again, it is immediate that this 
is indeed a category.


The 
identity on $(O,e)$ is $e$ itself. 
Moreover, there is a faithful functor 
$\mathrm{im}\colon \mathcal C\to\Kar(\mathcal C)$,
called \textit{the image}, that sends $A$ to 
$(O,\mathrm{id})$ and $f\colon O\to O^{\prime}$ 
to $f\colon(O,\mathrm{id})\to(O^{\prime},\mathrm{id})$.
Categories $\mathcal C$ such that $C\cong\Kar(\mathcal C)$ 
are called \textit{idempotent complete}.


We point out that $\Mat(\mathcal{C})$ 
is ``combinatorial the same'' as $\mathcal{C}$ -- in contrast to 
$\Kar(\mathcal{C})$ which is usually very hard to describe 
combinatorially/diagrammatically.




\subsection{The dihedral cathedral \texorpdfstring{$\D$}{Dinfty}}\label{sub-dcath}
For the reader familiar with~\cite{el1}: be careful that Elias' 
``root of unity case'' \textit{does not} 
correspond to our root of unity case from Section~\ref{sec-tilting}. 
Moreover, we slightly rescale his 
``barbell forcing relation'', see \textbf{BF2}~\eqref{eq-barbforc}.



Following~\cite{el1}, we encode the two different generators of 
$W_l=\langle s,t\rangle$ using two colors. 
Our convention, that is different from the one used 
by Elias, is that $s$ is displayed 
in \textit{red} and $t$ in \textit{green}. 
The ``third color'' is for $1\in W_l$ which is displayed as 
\textit{white colored or empty}.



\begin{defn}(\textbf{Soergel graph})\label{defn-soergeldia}
A \textit{pre}-Soergel graph 
$\tilde G$ is a colored, planar graph
embedded in $[0,1]\times[0,1]$ 
whose bottom (or source) boundary is in 
$[0,1]\times\{0\}$ and whose top (or target) 
boundary is in $[0,1]\times\{1\}$. The only 
vertices are univalent (called \textit{dots}) 
or trivalent. The edges of a Soergel graph 
are colored by red (or $r$) and green (or $g$) 
such that at each trivalent vertex all adjacent 
edges have the same color. We display dots 
and trivalent vertices locally as
\[
\text{Dots:}\quad
\xy
(0,0)*{\includegraphics[scale=0.8]{res/figs/diacath/iso3}};
(0,-8.5)*{l(\cdot)=1};
\endxy\hspace*{0.3cm}\text{or}\hspace*{0.3cm}
\xy
(0,0)*{\includegraphics[scale=0.8]{res/figs/diacath/iso3b}};
(0,-8.5)*{l(\cdot)=1};
\endxy\hspace*{1cm}\text{Trivalent vertices:}\quad
\xy
(0,0)*{\includegraphics[scale=0.8]{res/figs/diacath/iso4}};
(0,-8.5)*{l(\cdot)=-1};
\endxy\hspace*{0.3cm}\text{or}\hspace*{0.3cm}
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso4b}};
(0,-8.5)*{l(\cdot)=-1};
\endxy
\]
where we tend (as above) 
not to display the $r$ and $g$. 
Moreover, the illustration above 
is locally and Soergel graphs 
also include for example horizontal 
reflections of the ones above. 
In addition, given a pre-Soergel 
graph $\tilde G$, we define its 
\textit{degree $l(\tilde G)$} to be the sum of the local degrees as above.



A \textit{Soergel graph $G$} is an 
equivalence class of pre-Soergel graphs 
modulo boundary preserving isotopies of 
colored, planar graphs (which are 
all locally of the forms as in~\eqref{eq-iso}). Note that the 
degree is still well-defined for a 
Soergel graph and we denote it by $l(G)$. 
The empty diagram 
$\bbz$ is also a Soergel graph and of degree $l(\bbz)=0$.




Each Soergel graph gives rise 
to a bottom sequence $b(G)=b_i\dots b_2b_1$ and 
a top sequence $t(G)=t_{i^{\prime}}\dots t_2t_1$ 
of colors $b_k,t_k\in\{r,g\}$ by reading the colors 
at the bottom or top boundary from \textit{right to left} 
respectively. We also allow the empty sequence, if the 
boundary is empty (at bottom or top). We call a Soergel 
graph (or a local piece of it) \textit{floating}, if 
both boundaries are empty. We call floating Soergel 
graphs consisting of only one edge \textit{barbells}.
\end{defn}



Our reading conventions are thus 
from \textit{right to left} (we think of the pictures 
as applying functors to a module) and \textit{bottom to top}. 
Moreover, we think of Soergel graphs as embedded into a 
rectangle (although we never illustrate the rectangle), 
and thus, it make sense to speak about \textit{faces} of 
Soergel graphs. Each Soergel graph has a unique rightmost 
face $F_r$ and a unique leftmost face $F_l$.
\begin{ex}\label{ex-soergelgraph}
An example of two representatives of a Soergel graph $G$ are
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/example1}};
(-18,-16)*{\scriptstyle r};
(-10.75,-16)*{\scriptstyle r};
(-3.5,-16)*{\scriptstyle r};
(3.5,-16)*{\scriptstyle g};
(10.75,-16)*{\scriptstyle g};
(18,-16)*{\scriptstyle r};
(-18,16)*{\scriptstyle r};
(-10.75,16)*{\scriptstyle g};
(-3.5,16)*{\scriptstyle r};
(3.5,16)*{\scriptstyle g};
(10.75,16)*{\scriptstyle r};
(18,16)*{\scriptstyle r};
(-16,0)*{\scriptstyle F_l};
(20,0)*{\scriptstyle F_r};
\endxy=
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/example4}};
(-18,-16)*{\scriptstyle r};
(-10.75,-16)*{\scriptstyle r};
(-3.5,-16)*{\scriptstyle r};
(3.5,-16)*{\scriptstyle g};
(10.75,-16)*{\scriptstyle g};
(18,-16)*{\scriptstyle r};
(-18,16)*{\scriptstyle r};
(-10.75,16)*{\scriptstyle g};
(-3.5,16)*{\scriptstyle r};
(3.5,16)*{\scriptstyle g};
(10.75,16)*{\scriptstyle r};
(18,16)*{\scriptstyle r};
(-16,0)*{\scriptstyle F_l};
(16,0)*{\scriptstyle F_r};
\endxy
\]
Here $l(G)=4$, $b(G)=rrrggr$ and $t(G)=rgrgrr$. 
The graph above has one (green) barbell. We have 
marked the unique right- and leftmost faces with $F_r$ and $F_l$ respectively.
\end{ex}



Note that, since $G$ completely 
determines $b(G)$ and $t(G)$, we do not display these anymore.




\begin{defn}(\textbf{Elias' dihedral cathedral $\D$})\label{defn-diacath} We 
consider the $\bC$-linear, graded, monoidal category 
called the \textit{free} dihedral cathedral, 
denote by $\D_{f}$, consisting of the following.
\begin{itemize}
\item Objects $\Ob(\D_f)$ are finite 
sequences $x=x_i\dots x_2x_1$ with 
$x_i\in\{r,g\}$. Moreover, the empty sequence $\emptyset$ is also an object.
\item The space of morphisms 
$\Hom_{\D_f}(x,x^{\prime})$ for 
$x,x^{\prime}\in\Ob(\D_f)$ is the 
$\bC$-linear span of all Soergel graphs $G$ with $b(G)=x$ and $t(G)=x^{\prime}$.
\item Composition (vertical) of morphisms 
$G^{\prime}\circv G$ is defined by 
glueing $G^{\prime}$ on top of $G$.
\item The monoidal product (horizontal) $\circh$ is, 
for $x=x_i\dots x_2x_1$ and 
$x^{\prime}=x^{\prime}_{i^{\prime}}\dots x^{\prime}_2x^{\prime}_1$, 
given by concatenation $x^{\prime}\circh x=x^{\prime}x$, and 
for $G^{\prime}\circh G$ via placing 
$G^{\prime}$ to the left of $G$.
\item The spaces $\Hom_{\D_f}(x,x^{\prime})$ 
are graded $\bC$-vector spaces where the 
degree of a Soergel graph $G$ is given by $l(G)$. 
\end{itemize}
The category $\D$ is 
the quotient category of $\D_f$ obtained 
by taking the quotient by the following local 
relations and their 
\textit{color-inverted} (red\raisebox{-0.05cm}{$\leftrightarrows$}green) counterparts.



The \textit{two Frobenius relations}:
\begin{equation}\label{eq-frob}
\text{\textbf{Frob1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob2}};
\endxy=
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/frob1}};
\endxy,\quad\quad\text{\textbf{Frob2}}:\quad
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
\end{equation}
The \textit{needle relation}:
\begin{equation}\label{eq-needle}
\text{\textbf{Needle}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/needle}};
\endxy=0
\end{equation}
The \textit{barbell forcing relations}:
\begin{equation}\label{eq-barbforc}
\text{\textbf{BF1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing1a}};
\endxy=2\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing3}};
\endxy-\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing2a}};
\endxy,\quad\quad\text{\textbf{BF2}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing1b}};
\endxy=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing2b}};
\endxy+2\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing3}};
\endxy-2\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/forcing2a}};
\endxy
\end{equation}
Note that the isotopy invariance 
can be locally displayed via the \textit{isotopy relations}:
\begin{equation}\label{eq-iso}
\text{\textbf{Iso1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso1}};
\endxy\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso3}};
\endxy
\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso2}};
\endxy,\quad\quad\text{\textbf{Iso2}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso5}};
\endxy\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso4}};
\endxy
\;=\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/iso6}};
\endxy
\end{equation}
together with a horizontal reflection of the two relations.



We also note that all relations 
are homogeneous with respect to 
$l(G)$ and thus, $\D$ inherits 
the grading from $\D_f$. The monoidal product 
$\circh$ also carries over to $\D$ without difficulties.



Moreover, we use the following 
convention: we call elements of 
$\Hom_{\D_f}(x,x^{\prime})$ Soergel 
graphs and, on the other hand, elements 
of $\Hom_{\D}(x,x^{\prime})$ \textit{Soergel diagrams} 
(for all possible $x,x^{\prime}\in\Ob(\D_f)=\Ob(\D)$). 
We call a face of a Soergel diagram \textit{empty} 
if it has no internal floating Soergel diagrams (as for example barbells).
\end{defn}



\begin{ex}\label{ex-soergelgraph1}
An example of two representatives of Soergel diagrams are
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/example1b}};
\endxy=
2\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/example3}};
\endxy
-\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/example2}};
\endxy
\]
Here we used the left (green) barbell forcing relation~\eqref{eq-barbforc} on the marked piece.
\end{ex}




\begin{lem}\label{lem-cycle}
A Soergel diagram $G$ with an 
internal cycle which bounds an empty face is zero.\makeqed
\end{lem}



\begin{proof}
Use repeatedly the first Frobenius 
relations~\eqref{eq-frob} as illustrated 
below (note that each step reduces the number 
of adjacent edges of the face and we have 
indicated where to use the first Frobenius 
relation \textbf{Frob1}~\eqref{eq-frob} in the last step)
\[
\cdots\;
\overset{\text{\textbf{Frob1}}}{=}
\;\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/cyclelem1}};
\endxy\;
\overset{\text{\textbf{Frob1}}}{=}
\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/cyclelem2}};
\endxy\;
\overset{\text{\textbf{Frob1}}}{=}
\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/cyclelem3}};
\endxy\;
\overset{\text{\textbf{Frob1}}}{=}
\;
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/cyclelem4}};
\endxy\;
\overset{\text{\textbf{Needle}}}{=}
\;0
\]
until we can use the needle 
relation~\eqref{eq-needle} to see that we get zero.
\end{proof}



A \textit{tree} is a connected Soergel 
graph $G$ with no cycles. We 
call a Soergel diagram \textit{reduced} if 
all of its connected components are trees or 
barbells and all barbells are in the rightmost face.



The following is~\cite[Proposition~5.19]{el1} converted to our conventions.
\begin{prop}\label{prop-soergeldiagrams}
Each Soergel diagram can be written 
as a $\bC$-linear sum of reduced 
Soergel diagrams. Thus, reduced Soergel 
diagrams form spanning sets of the hom-spaces of $\D$.\makeqed
\end{prop}



\begin{proof}
Note that it follows from a repeated 
application of the Frobenius 
relations~\eqref{eq-frob} that all floating 
trees are barbells and, by combining 
Lemma~\ref{lem-cycle} with \textbf{BF1} and 
\textbf{BF2}~\eqref{eq-barbforc}, all other 
floating Soergel diagrams are $\bC$-linear combinations of barbells.



Thus, we can restrict to Soergel diagrams whose only floating components are barbells.



Now, given a Soergel diagram $G$, we 
can first use \textbf{BF1} and \textbf{BF2}~\eqref{eq-barbforc} 
to express $G$ as a direct sum of Soergel 
diagrams $G_i$ (with $i=1,\dots,k$) with only 
barbells in the rightmost face. By 
Lemma~\ref{lem-cycle} all Soergel diagrams 
$G_i$ with an internal cycle are zero now.
\end{proof}



We point out the following corollary. 
This can be compared to~\cite[Corollary~5.20]{el1} and 
the corresponding statement, in our case for 
$\Tgr$, will later be completely different, 
see Lemma~\ref{lem-noaction}.
For this purpose, denote by $\bC[b_r,b_g]$ 
the graded $\bC$-algebras 
of polynomials in $b_r,b_g$, with the generators $b_r,b_g$ being of degree $2$. 

\begin{cor}\label{cor-endoring}
We have $\bC[b_r,b_g]\cong \Endbf_{\D}(\emptyset)$ as 
graded $\bC$-algebras.\makeqed
\end{cor}


\begin{proof}
By Proposition~\ref{prop-soergeldiagrams} 
the map that sends $b_r\mapsto$``red barbell'' 
and $b_g\mapsto$``green barbell'' is an isomorphism 
of graded $\bC$-algebras. To see this note that a bunch of 
barbells do not satisfy any extra relations 
(the barbell forcing relations~\eqref{eq-barbforc} do not give anything new).
\end{proof}




\begin{lem}\label{lem-decom1}
Soergel diagrams satisfy
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced1r}};
\endxy=\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced2r}};
\endxy+\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced3r}};
\endxy
\quad\text{and}\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced1g}};
\endxy=\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced2g}};
\endxy+\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reduced3g}};
\endxy
\hspace{0.6cm}
\raisebox{-0.625cm}{\makeqed}
\hspace{-0.6cm}
\]
\end{lem}


\begin{proof}
Use \textbf{Frob1}~\eqref{eq-frob} on the 
right side followed by \textbf{BF1}~\eqref{eq-barbforc} for the middle edge.
\end{proof}



This implies the useful fact that we can focus 
on alternating sequences (the case where the 
sequence is a reduced word in $\D$) of red 
and green if we go to $\Mat(\D)$ (where we use $\circ$ 
for the matrix multiplication).



\begin{lem}\label{lem-decom2}
We have
\[
rr\cong r\langle-1\rangle\oplus r\langle+1\rangle\quad\text{and}\quad gg\cong g\langle-1\rangle\oplus g\langle+1\rangle.
\]
which are isomorphisms in $\Mat(\D)$.\makeqed
\end{lem}



\begin{proof}
The isomorphism for the red case is induced by
\[
\begin{xy}
  \xymatrix{
      rr \ar[rrrrr]|/-1.5em/{\begin{pmatrix}
 1\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reducediso1}};
\endxy \\
 \frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reducediso2}};
\endxy 
\end{pmatrix}}  & & & &  &  r\langle-1\rangle\oplus r\langle+1\rangle \ar[rrrrr]|/1.05em/{\begin{pmatrix}
 \frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reducediso3}};
\endxy & 1\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/reducediso4}};
\endxy
\end{pmatrix}} & & & & & rr,
  }
\end{xy}
\]
where we 
check (with Lemma~\ref{lem-decom1} for 
``right$\circ$left'' and Lemma~\ref{lem-cycle} 
together with BF1~\eqref{eq-barbforc} for 
``left$\circ$right'') that the two matrices above are inverses.
The green case works analogous.
\end{proof}




\begin{defn}(\textbf{Jones-Wenzl projectors})\label{defn-jwpro}
Denote by $x_{k-tst}$ a 
sequence $x_k\dots x_2x_1$ of length $k$ 
that alternates in the colors red and green 
and starts with $x_1=g$ (thus, ends in $r$ iff $k$ is even).



We define for each $i\geq 0$ the 
$i$\textit{-th green Jones Wenzl} 
projector $\JWg_i$ recursively as the 
element of $\Endbf_{\D}(x_{i-tst})$ obtained 
via the convention that $\JWg_0$ is 
$\bbz\colon \emptyset\to \emptyset$, $\JWg_1$ 
is $\mathrm{id}\colon g\to g$, $\JWg_2$ is 
$\mathrm{id}\colon rg\to rg$ and recursion rule for $i>2$ given by
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jwrecursion1}};
(0,0)*{\JWg_{i}};
\endxy=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jwrecursion2}};
(2.5,0)*{\JWg_{i-1}};
\endxy-\frac{i-2}{i-1}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jwrecursion3}};
(10,0)*{\JWg_{i-3}};
(2.5,20)*{\JWg_{i-1}};
(2.5,-21)*{\JWg_{i-1}};
\endxy
\]
Here we have only illustrated the case for odd $i$.
Similar for even $i$ and red projectors $\JWr_i$.
\end{defn}




\begin{ex}\label{ex-jw}
The first four (green) Jones-Wenzl projectors are
\[
\JWg_0=\bbz,\quad\quad
\JWg_1=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jw1}};
\endxy,\quad\quad\JWg_2=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jw2}};
\endxy,\quad\quad\JWg_3=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jw3a}};
\endxy-\frac{1}{2}\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/jw3b}};
\endxy
\]
as follows by an easy calculation.
\end{ex}




For each $i^{\prime}>2$ we call a diagram of the form
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchalt}};
\endxy
\]
a \textit{green alternating $i^{\prime}$-pitchfork} 
(here $i^{\prime}=7$). We denote it by $P^g_{i^{\prime}}$ 
and similarly for $P^r_{i^{\prime}}$, which is the 
\textit{$i^{\prime}$-th red alternating pitchfork}. 
We note that $b(P^g_{i^{\prime}})$ as well as 
$b(P^r_{i^{\prime}})$ consist of $i^{\prime}$ 
elements. Moreover, we write $D_i(P^g_{i^{\prime}})$ 
for a bigger diagram with $i\geq i^{\prime}>2$ which somewhere 
at the bottom has a green alternating pitchfork, i.e.
\begin{equation}\label{eq-pitch}
D_i(P^g_{i^{\prime}})=D\circ (\mathrm{id}_x\,P^g_{i^{\prime}}\,\mathrm{id}_{x^{\prime}})
\end{equation}
for some sequences $x,x^{\prime}$ and some diagram $D$. Similarly for red again.



\begin{lem}\label{lem-pitch}
Let $i\geq i^{\prime}>2$. 
Then $D_i(P^g_{i^{\prime}})\circ \JWg_i=0$. Similarly for red.\makeqed
\end{lem}



\begin{proof}
This follows recursively. 
To see the first step $i=i^{\prime}=3$, we 
compose $P^g_{3}$ with the second term of 
$\JWg_3$ from Example~\ref{ex-jw} and obtain 
by using \textbf{BF2}~\eqref{eq-barbforc} 
and Lemma~\ref{lem-cycle} for the first 
step and \textbf{Frob2}~\eqref{eq-frob} for the second:
\begin{equation*}
-\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchlem1}};
\endxy=-\frac{1}{2}\cdot 2\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchlem2}};
\endxy=-\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchlem3}};
\endxy
\end{equation*}
giving minus the composition of $P^g_{3}$ 
with the first term of $\JWg_3$.
Thus, 
$D_3(P^g_{3})\circ \JWg_3=0$.



Now we use induction on $i$ and fix $i^{\prime}=3$. 
If $i>3$ and $D_i(P^g_{3})$ has $x\neq \emptyset$ 
(see~\eqref{eq-pitch}), then the recursion rule 
from Definition~\ref{defn-jwpro} (the $3$-pitchfork 
is on top of the smaller box that corresponds to the 
$i-1$-th Jones-Wenzl projector) shows by induction 
that we get zero. If, on the other hand, $x=\emptyset$, 
then we can 
use a similar argument as above. Hence, 
we always have $D_i(P^g_{3})\circ \JWg_i=0$.



But the case $i^{\prime}=3$ suffices as the following illustrates.
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchalt1}};
\endxy=\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchalt2}};
\endxy+\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/diacath/pitchalt3}};
\endxy
\]
Here we used \textbf{Frob2}~\eqref{eq-frob} ``backwards'' 
on a bigger alternating pitchfork followed by 
\textbf{BF1}~\eqref{eq-barbforc}. We see now two smaller 
pitchforks and thus, the case $i^{\prime}=3$ 
suffices to verify the lemma.
\end{proof}


Lemma~\ref{lem-pitch} holds, mutatis mutandis, by attaching horizontally 
reflected pitchforks form the bottom as well.
Moreover, it is easy to deduce that the Jones-Wenzl 
projectors are (degree zero) idempotents 
of $x_{i-tst}$ and $x_{i-sts}$, respectively. 
We associate these to the corresponding 
alternating sequences. Furthermore, by Lemma~\ref{lem-decom2}, we can, by going to $\Mat(\D)$, associate to each $x\in\Ob(\D)$ a (shifted) direct sum of Jones-Wenzl 
projectors. We denote this sum that consists of 
these projectors for $x$ by $\JWx$. This motivates the following category.


\begin{defn}\label{defn-matdia}
Denote by $\Mat(\Dk)$ the full subcategory 
of $\Kar(\Mat(\D))$ generated by $\mathrm{im}(\JWx)$ for all $x\in\Ob(\D)$.
\end{defn}
Diagrammatically $\Mat(\Dk)$ is given similarly to 
$\Mat(\D)$, but has some extra relations. For example, 
Lemma~\ref{lem-pitch} says that, whenever we see a
pitchfork at the bottom (or its reflection at the top) 
boundary, then the corresponding Soergel diagram is zero.





\subsection{The quotient \texorpdfstring{$\QD$}{QDinfty}}\label{sub-qd}



We are now able to define the category 
whose combinatorics and diagrammatic 
govern the tilting category $\Tgr$. 
We call it for short \textit{the quotient}.



\begin{defn}(\textbf{The quotient})\label{defn-thequotient}
We denote by $\QD_f$ the $\bC$-linear full 
subcategory of $\D$, called \textit{``free quotient''}, consisting of the following.



\begin{itemize}
\item Objects $\Ob(\QD_f)$ are finite sequences 
$x=x_i\dots x_2x_1$ with $x_k\in\{r,g\}$. Moreover, 
the empty sequence $\emptyset$ is also an object.



\item The hom-space $\Hom_{\QD_f}(x,x^{\prime})$ 
for $x,x^{\prime}\in\Ob(\QD_f)$ is the $\bC$-linear 
span of all Soergel graphs $G$ with $b(G)=x$ and 
$t(G)=x^{\prime}$ whose rightmost face is marked with the \textit{dead-end symbol}.



\item Composition $G^{\prime}\circv G$ is defined 
by glueing $G^{\prime}$ on top of $G$. The dead-end symbol is just a 
marker and behaves as an idempotent under composition 
and can not be moved from the rightmost face.




\item The morphisms in $\Hom_{\QD_f}(x,x^{\prime})$ 
satisfy the relations of the corresponding morphisms 
(\textit{without} the dead-end marker) is 
$\Hom_{\D}(x,x^{\prime})$ given in Definition~\ref{defn-diacath}.



\item The spaces $\Hom_{\QD_f}(x,x^{\prime})$ are 
graded $\bC$-vector spaces with degree given by $l(G)$.
\end{itemize}



The \textit{quotient $\QD$} is the quotient of 
$\QD_f$ by the following extra relations which 
we call \textit{the dead-end relations}:
\begin{equation}\label{eq-dead}
\text{\textbf{DE1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/deadend1}};
\endxy=
0,\quad\quad\text{\textbf{DE2}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/deadend2}};
\endxy=0
\end{equation}
We stress that we do not allow the 
color inverted counterparts of~\eqref{eq-dead}. 
All relations are homogeneous with 
respect to $l(G)$ and thus, $\QD$ inherits the grading from $\D$. 
We call the morphisms in $\QD$ \textit{marked} Soergel diagrams.
\end{defn}




\begin{ex}\label{ex-soergelgraph2}
An example of a Soergel diagram that 
is zero as a marked Soergel diagrams is
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/example5}};
\endxy=
2\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/example6}};
\endxy
-\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/example7}};
\endxy=0
\]
Here the middle diagrams is zero due to \textbf{DE2} and the right-hand due to \textbf{DE1}.
\end{ex}


Let \textit{reduced}, marked Soergel diagrams be the evident analogues of 
reduced Soergel diagrams.

\begin{lem}\label{lem-noaction}
Each marked Soergel diagram can be 
written as a $\bC$-linear sum of marked, 
reduced Soergel diagrams. Thus, marked, 
reduced Soergel diagrams without barbells 
form spanning sets of the hom-spaces of $\QD$. 
The right action of $\Endbf_{\D}(\emptyset)$ by 
placing barbells in the rightmost face is the trivial action.\makeqed
\end{lem}



\begin{proof}
Use repeatedly \textbf{BF1} and 
\textbf{BF2}~\eqref{eq-barbforc} to 
shift all existing barbells to 
the rightmost region. Then use 
the two dead-end relations \textbf{DE1} 
and \textbf{DE2}~\eqref{eq-dead} to see that 
only terms without barbells are not 
killed. The remaining diagrams are 
reduced by Proposition~\ref{prop-soergeldiagrams}.
\end{proof}



Note that, as a consequence of Lemma~\ref{lem-noaction}, 
a marked, reduced Soergel diagram does 
not have any floating components anymore.




\begin{defn}\label{defn-matdia2}
Denote by $\Mat(\QDk)$ the full 
subcategory of $\Kar(\Mat(\QD))$ generated by $\mathrm{im}(\JWx)$ for all $x\in\Ob(\QD)$.
\end{defn}



Thus, by using Lemma~\ref{lem-decom2} and 
\textbf{DE1}~\eqref{eq-dead}, we usually can focus 
on alternating sequences $x$ that start with $g$ in the following.



Given a marked, reduced Soergel diagram $G$, 
we call two edges $E_1,E_2$ \textit{face sharing}, 
if $E_1$ and $E_2$ are adjacent to some common face. 
Marked, reduced Soergel diagrams $G$ (with color 
alternating boundary) with face sharing edges of 
the same color come in four types, where we, by 
Lemma~\ref{lem-pitch}, ignore diagrams with pitchforks. The first two 
types are
\begin{equation}\label{eq-type12}
\text{\textbf{Type 1}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case1a}};
(-4.1,8)*{\scriptstyle \underbrace{}};
(-4.1,5.5)*{\scriptstyle k\geq 1};
(-4.1,-8)*{\scriptstyle \overbrace{•}};
(-4.1,-5)*{\scriptstyle k^{\prime}\geq 1};
\endxy,\quad\quad\text{\textbf{Type 2}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case2a}};
(-4.1,8)*{\scriptstyle \underbrace{•}};
(-4.1,5.5)*{\scriptstyle k\geq 2};
(-4.1,-8)*{\scriptstyle \overbrace{•}};
(-4.1,-5)*{\scriptstyle k^{\prime}\geq 2};
\endxy
\end{equation}


where the dots $\cdots$ mean an arbitrary (possible empty) 
diagram in between and we do not require the picture to 
by symmetric. Moreover, $k,k^{\prime}$ are odd in \textbf{Type 1} 
and even in \textbf{Type 2}. We should note that only the first 
edge has to be green, but we allow 
possible color inversion of the rest 
of the picture (that is, after the rightmost dots).
The other two types are
\begin{equation}\label{eq-type34}
\text{\textbf{Type 3}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3a}};
(-10,8)*{\scriptstyle \underbrace{•}};
(-10,5.5)*{\scriptstyle k\geq 2};
(-10,-8)*{\scriptstyle \overbrace{•}};
(-10,-5)*{\scriptstyle k^{\prime}\geq 0};
\endxy,\quad\quad\text{\textbf{Type 4}}:\quad
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4b}};
\endxy
\end{equation}
The difference between the types 
1,2 and 3,4 is that 1,2 have face sharing 
edges for a non-extremal face, while 
3,4 have face sharing edges for the leftmost 
face. We note that \textbf{Type 3} should 
also include the horizontal reflection (fixing the dead-end symbol) 
of the first diagram in~\eqref{eq-type34}.




\begin{lem}\label{lem-facesharing}
If a marked, reduced Soergel diagram 
$G\in\Hom_{\Mat(\QDk)}(x,x^{\prime})$ has 
two face sharing edges of one of the three types 1,2 or 3, then it is zero.\makeqed
\end{lem}



\begin{proof}
A case-by-case check. We assume that there is at 
least one such face.



\textbf{Type 1}. This follows via
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case1b}};
\endxy=\frac{1}{2}\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case1c}};
(-4,-5)*{\text{\tiny pitchfork}};
\endxy + \frac{1}{2}\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case1d}};
(-4,5)*{\text{\tiny pitchfork}};
\endxy
\]
That both diagrams are zero follows from Lemma~\ref{lem-pitch} 
(recalling that we have restricted ourself to alternating sequences of colors), since 
the marked faces above are, by~\eqref{eq-frob}, pitchforks.



\textbf{Type 2}. This follows similarly to \textbf{Type 3} below.



\textbf{Type 3}. Note that the number of bottom edges 
at the end does not matter and we thus, by 
simplicity, assume that there are none of these. 
In addition, we only illustrate the case with 
two dotted edges at the top since all the 
others will be similar. And, without loss 
of generality, we assume that this is the only 
face with adjacent edges of the same color.




We proceed by induction on $j$, where $j>0$ 
is the minimal number of cuts that a line 
drawn from the rightmost face to the face 
in question needs. The case $j=1$ can be deduced via
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3b}};
\endxy=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3c}};
\endxy=\frac{1}{2}\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3d}};
\endxy + \frac{1}{2}\cdot \xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3e}};
\endxy
\]
Note that the rightmost 
diagram is zero by Lemma~\ref{lem-pitch}. Thus, we 
continue as
\[
\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3d}};
\endxy=-\frac{1}{2}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3f}};
\endxy+\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3g}};
\endxy=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case3h}};
\endxy=0
\]
where the last diagram is zero due 
to \textbf{DE1}~\eqref{eq-dead}.




This shows that our starting diagram was 
already zero. The induction $j>1$ works 
now in a similar fashion where we perform 
the same sequence of moves until we are 
in a situation as the last step above. 
Then we can use induction, since we have 
created a face with edges of the same 
color, but ``closer'' to the rightmost face. This finishes the proof.
\end{proof}





\begin{cor}\label{cor-homspaces2}
Let $i,i^{\prime}\in\bN$. Then we have 
the following for $i,i^{\prime}\neq 0$.
\[
\Hom_{\Mat(\QDk)}(x_{i-tst},x_{i^{\prime}-tst})\cong\begin{cases}\bC\bbi\oplus\bC\varepsilon_i,&\text{if }|i-i^{\prime}|=0,\\
\bC u_{i},&\text{if }i^{\prime}-i=1,\\
\bC d_{i},&\text{if }i-i^{\prime}=1,\\
0,&\text{if }|i-i^{\prime}|>1,\end{cases}
\]
with diagrams for $i=1,2,\dots$ 
(and possible color inverted left sides)
\[
\bbi=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4a}};
(-10,-16)*{\scriptstyle x_i};
(-2,-16)*{\scriptstyle x_{i-1}};
(4.5,-16)*{\scriptstyle x_1};
(-10,15.5)*{\scriptstyle x_i};
(-2,15.5)*{\scriptstyle x_{i-1}};
(4.5,15.5)*{\scriptstyle x_1};
\endxy\;,\;\varepsilon_i=\frac{1}{2^i}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4b}};
(-10,-16)*{\scriptstyle x_i};
(-2,-16)*{\scriptstyle x_{i-1}};
(4.5,-16)*{\scriptstyle x_1};
(-10,15.5)*{\scriptstyle x_i};
(-2,15.5)*{\scriptstyle x_{i-1}};
(4.5,15.5)*{\scriptstyle x_1};
\endxy\;,\; u_{i-1}=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4c}};
(-2,-16)*{\scriptstyle x_{i-1}};
(4.5,-16)*{\scriptstyle x_1};
(-10,15.5)*{\scriptstyle x_i};
(-2,15.5)*{\scriptstyle x_{i-1}};
(4.5,15.5)*{\scriptstyle x_1};
\endxy\;,\; d_i=\frac{1}{2^{i}}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4d}};
(-10,-16)*{\scriptstyle x_i};
(-2,-16)*{\scriptstyle x_{i-1}};
(4.5,-16)*{\scriptstyle x_1};
(-2,15.5)*{\scriptstyle x_{i-1}};
(4.5,15.5)*{\scriptstyle x_1};
\endxy
\]
of degree $l(\bbi)=0$, $l(u_i)=l(d_i)=1$ 
and $l(\varepsilon_i)=2$. In addition, 
$\Hom_{\Mat(\QDk)}(\emptyset,\emptyset)$ 
is one dimensional and spanned by the empty diagram $\bbz$ of degree $l(\bbz)=0$.\makeqed
\end{cor}



\begin{proof}
A case-by-case check using Lemma~\ref{lem-facesharing}. That $\Hom_{\Mat(\QDk)}(\emptyset,\emptyset)\cong\bC\bbz$ follows from \textbf{DE1} and \textbf{DE2}~\eqref{eq-dead} since no floating diagrams can exist.




If $|i-i^{\prime}|>1$, then each Soergel diagram has a pitchfork or is of \textbf{Type 3}~\eqref{eq-type34}. Both are zero by Lemmas~\ref{lem-pitch} and~\ref{lem-facesharing}.
If $|i-i^{\prime}|=1$, then, by Lemma~\ref{lem-facesharing} again, only diagrams of the form $u_i$ or $d_i$ as above can be non-zero and these are clearly non-zero.
If $|i-i^{\prime}|=0$, then, again by Lemma~\ref{lem-facesharing}, only diagrams of the form $\bbi$ or $\varepsilon_i$ as above can be non-zero (which they clearly are).



All these diagrams are linearly independent for degree reasons.
\end{proof}

\begin{rem}\label{rem-nonzero}
Let $\mathcal C$ be a category 
given by generators and relations. Usually 
it is very hard to see ``by hand'' that the 
calculus provided by $\mathcal C$ does not collapse. A way to 
show that this is not the case is to represent $\mathcal C$ 
on a category ``under control'', e.g. on module categories.


We formally have to do the same to see that the four maps from above are indeed non-zero. 
What we use in our case is Lemma~\ref{lem-welldef} which identifies 
the four maps with the evident $\Uq$-intertwiners (we point out that 
we do not need Corollary~\ref{cor-homspaces2} to prove Lemma~\ref{lem-welldef}).
\end{rem}


\begin{prop}\label{prop-quiverrel}
We have
\begin{gather*}
u_{i}\circ u_{i-1}=0=d_i\circ d_{i+1},\;i=1,2,\dots,\quad\quad d_{i+1}\circ u_i=\varepsilon_i=u_{i-1}\circ d_{i},\;i=1,2,\dots
\\
d_1\circ u_0=0, 
\end{gather*}
where we use the notation from Corollary~\ref{cor-homspaces2}.\makeqed
\end{prop}



\begin{proof}
The relation $d_1\circ u_0$ is \textbf{DE2}~\eqref{eq-dead}. 
For $u_{i}\circ u_{i-1}=0$ the corresponding diagrams are
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4e}};
\endxy
\circ
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4c}};
\endxy=\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4f}};
\endxy=0
\]
The relation $d_i\circ d_{i+1}=0$ follows similar and 
$u_{i-1}\circ d_{i}=\varepsilon_i$ can be verified directly as
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4c}};
\endxy
\circ\frac{1}{2^{i}}\cdot
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4d}};
\endxy=\frac{1}{2^{i}}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4b}};
\endxy
\]
while $d_{i+1}\circ u_i=\varepsilon_i$ follows via
\[
\frac{1}{2^{i+1}}\cdot
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4g}};
\endxy
\circ
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4e}};
\endxy=\frac{1}{2^{i+1}}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4h}};
\endxy=\frac{1}{2^{i}}\cdot\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/quotient/case4b}};
\endxy
\]
where we use \textbf{BF2}~\eqref{eq-barbforc} 
together with Lemma~\ref{lem-facesharing} 
to see that the only surviving term is 
the ``broken'' one from \textbf{BF2}~\eqref{eq-barbforc}. This finishes the proof.
\end{proof}





\subsection{\texorpdfstring{$\QD$}{QDinfty} and the tilting category \texorpdfstring{$\Tgr$}{Tgr}}\label{sub-diatil}


Given a sequence $x\in\Ob(\QD)$ of the 
form $x_i\dots x_2x_1$ with $x_k\in\{r,g\}$ 
we denote by $\tilde{\ell}(x)$ the 
\textit{number of color changes} 
(including the first from empty to green), 
e.g. $\tilde{\ell}(g)=\tilde{\ell}(gg)=1$, 
$\tilde{\ell}(ggrgrgrr)=6$ and $\ell(x)=\tilde{\ell}(x)$ iff $x$ is alternating.



\begin{defn}(\textbf{Diagrammatic presentation})\label{defn-functor}
Define a $\bC$-linear functor
\[
\mathcal{D}_{\infty}\colon \Mat(\QDk)\to\Tgrl
\]
of graded categories by the following convention.



On objects (we treat degree 
shifted objects in the evident way):
\begin{itemize}
\item Send the empty sequence $\emptyset$ to $\Tn{\bbz}$. If $x\in\Ob(\QD)$ is of the 
form $x_i\dots x_2x_1$ with $x_k\in\{r,g\}$, then define
\[
\mathcal{D}_{\infty}(x)=p_{\Tn{\lambda_{\tilde{\ell}(x)}}}\circ\Theta_{x_i}\circ\dots\circ\Theta_{x_2}\circ\Theta_{x_1}\Tn{\bbz},
\]
where we use the convention 
$r=s, g=t$ and $p_{\Tn{\lambda_{\tilde{\ell}(x)}}}$ projects 
to the $\Tn{\lambda_{\tilde{\ell}(x)}}$ part.



\item Send a general $x\in\Ob(\Mat(\QDk))$ to the direct sum of the images of its components.
\end{itemize}



All marked Soergel diagrams are 
compositions of diagrams of the form 
$D^{\prime}GD$ with identity diagrams 
$D$ and $D^{\prime}$ and a generator 
$G$ in between. On morphisms:
\begin{itemize}
\item We describe the image of marked Soergel 
diagrams \textit{inductively from right to left}. 
That is, we describe what the functor does if 
one has already an identity diagram 
$D\colon x\to x$ and $\mathcal{D}_{\infty}(D)\colon M_k\to M_k$ 
(with $\mathcal{D}_{\infty}(x)\cong M_k$) and one adds a generator to the \textit{left}.
 
 
 
\item By construction of the image on objects 
and Corollaries~\ref{cor-theta} and~\ref{cor-funcgrad3}, 
$M_k$ will be just one $\Tn{\lambda_k}$ with 
some multiplicity and grading shifts and some 
$k\in\{0,\dots,i\}$ giving two cases, namely 
$k=\tilde{l}(x)$ even or odd. That is, we have
\[
M_k=\Tn{\lambda_k}\langle s_1\rangle\oplus \cdots\oplus \Tn{\lambda_k}\langle s_{k^{\prime}}\rangle.
\]
Note that the translation functors $\Theta_s$ 
and $\Theta_t$ act on the summands as in 
Corollaries~\ref{cor-theta} and~\ref{cor-funcgrad3} 
separately. To simplify notation, we write 
$\Theta_t(M_k)=M_{k+1}$ if $k$ is even and 
$\Theta_t(M_k)=M_{k}\langle-1\rangle\oplus M_{k}\langle+1\rangle=\tilde{M}_k$ 
if $k$ is odd and vice versa for $\Theta_s$. Moreover, 
in the case $k=0$ we send any red generator to zero.



\item The inductive description has four cases. 
We call these \textit{green-even}, \textit{green-odd}, 
\textit{red-even} and \textit{red-odd} where we only 
give the list for the first two since the other two 
are similar with exchanged conventions for even and 
odd. Each case has five sub-cases (for the five generators) 
giving twenty cases in total. We write $D_{0}$ (even) and 
$D_{1}$ (odd) for the two different cases. 
Since the $M_k$'s could already consist of multiple, shifted 
copies of $\Tn{\bbi}$'s, the entries in the matrices below 
are shorthand notations for matrices \textit{themselves}.




\item Basic pieces: send the empty 
sequence $\bbz$ to $\mathrm{id}\colon\Tn{\bbz}\to\Tn{\bbz}$. 
Moreover, for a green identity we assign
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor6}};
(0.5,0)*{D_{0}};
\endxy\mapsto\mathrm{id}\colon M_{k+1}\to M_{k+1},\quad\quad\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor6}};
(0.5,0)*{D_{1}};
\endxy\mapsto\begin{pmatrix}
 \mathrm{id} & 0\\
 0 & \mathrm{id}
\end{pmatrix}\colon \tilde M_{k}\to \tilde M_{k}
\]
For the up dotted edge we assign 
(recalling the rescaling $\tilde{\varepsilon}_k=2^k\varepsilon_k$)
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor7}};
(0.5,0)*{D_{0}};
\endxy\mapsto u_k\colon M_{k}\to M_{k+1},\quad\quad\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor7}};
(0.5,0)*{D_{1}};
\endxy\mapsto\begin{pmatrix}
 \tilde{\varepsilon}_k\\
 \mathrm{id}
\end{pmatrix}\colon M_{k}\to \tilde M_{k}
\]
For the down dotted edge we assign 
(recalling the rescaling $\tilde{d}_k=2^kd_k$)
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor8}};
(0.5,0)*{D_{0}};
\endxy\mapsto \tilde{d}_{k+1}\colon M_{k+1}\to M_{k},\quad\quad\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor8}};
(0.5,0)*{D_{1}};
\endxy\mapsto\begin{pmatrix}
 \mathrm{id} & \tilde{\varepsilon}_k
\end{pmatrix}\colon \tilde M_{k}\to M_{k}
\]
For the merges and splits in 
the even case we assign
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor9}};
(4.5,0)*{D_{0}};
\endxy\mapsto \begin{pmatrix}
 0 & \mathrm{id}
\end{pmatrix}\colon \tilde M_{k+1}\to M_{k+1},\quad\quad\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor10}};
(4.5,0)*{D_{0}};
\endxy\mapsto\begin{pmatrix}
 \mathrm{id}\\ 0
\end{pmatrix}\colon M_{k+1}\to \tilde M_{k+1}
\]
For the merges in the odd case we assign
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor9}};
(4.5,0)*{D_{1}};
\endxy\mapsto \begin{pmatrix}
 0 & 0 & \mathrm{id} & 0\\ 0 & 0 & 0 & \mathrm{id}
\end{pmatrix}\colon \tilde{\tilde{M}}_{k}\to \tilde M_{k}
\]
(with $\tilde{\tilde{M}}_{k}=M_k\langle-2\rangle\oplus M_k\langle0\rangle\oplus M_k\langle0\rangle\oplus M_k\langle+2\rangle$) and last but not least
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor10}};
(4.5,0)*{D_{1}};
\endxy\mapsto \begin{pmatrix}
 \mathrm{id} & 0\\ 0 & \mathrm{id}\\ 0& 0\\0& 0
\end{pmatrix}\colon \tilde M_k\to\tilde{\tilde{M}}_{k}.
\]



\item ``Fill up the generators to the left'': for each 
red identity strand to the left of the local generators 
from above apply a $\Theta_s$ to the elements of the 
matrices component-wise and likewise for green strands 
and $\Theta_t$. This can be made explicit as explained in Example~\ref{ex-howtofunctor}.



\item If $f$ is a homomorphism $f\in\Hom(\QD)$, 
then decompose it into generators and define 
$\mathcal{D}_{\infty}(f)$ to be the composition of its local pieces.
\end{itemize}
We extend linearly for a general $F\in\Hom(\Mat(\QDk))$.
\end{defn}




\begin{ex}\label{ex-functor}
It is easy to see 
how the assignment is 
for alternating sequences. For example
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor2}};
\endxy\mapsto u_0\colon \Tn{\bbz}\to \Tn{\bbo},\quad\quad\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor3}};
\endxy\mapsto \tilde{d}_1\colon\Tn{\bbo}\to\Tn{\bbz}
\]
and similar for all other diagrams of this kind. Furthermore, we have
\begin{gather*}
\begin{aligned}
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor4}};
\endxy &\mapsto \begin{pmatrix}
 0 & \mathrm{id}
\end{pmatrix}\colon \Tn{\bbo}\langle-1\rangle\oplus \Tn{\bbo}\langle+1\rangle\to \Tn{\bbo}
\\
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/functor5}};
\endxy &\mapsto \begin{pmatrix}
 \mathrm{id}\\ 0
\end{pmatrix}\colon\Tn{\bbo}\to\Tn{\bbo}\langle-1\rangle\oplus \Tn{\bbo}\langle+1\rangle
\end{aligned}
\end{gather*}
where we see that the degree 
is preserved. Moreover, the entries in the matrices 
of the list above are in general already matrices. 
For example, the matrix that corresponds to (here $M_1=\Tn{\bbo}$)
\[
\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/examplewelldef}};
\endxy\mapsto \begin{pmatrix}
 \mathrm{id} & \tilde{\varepsilon}_1 & 0 & 0\\ 0& 0&\mathrm{id} & \tilde{\varepsilon}_1
\end{pmatrix}\colon\tilde{\tilde{M_1}}\to\tilde{M_1}
\]
Likewise for the horizontally flipped diagram.
\end{ex}




\begin{lem}\label{lem-welldef}
$\mathcal{D}_{\infty}\colon \Mat(\QDk)\to\Tgrl$ is well-defined, $\bC$-linear and
degree preserving.\makeqed
\end{lem}



\begin{proof}
It is immediate that $\mathcal{D}_{\infty}$ is $\bC$-linear and degree preserving.



Moreover, note that, by part (b) of 
Corollary~\ref{cor-theta} and part (c) of 
Corollary~\ref{cor-funcgrad3}, the assignment is 
well-defined on objects $x$, since we send $x$ to a 
repeated application of $\Theta_s$ and $\Theta_t$ to 
the trivial $\Uq$-module $\Tn{\bbz}$ together with a 
projection onto the leading  
factor $\Tn{\bbi}$. Thus, without taking relations into account, 
we get a well-defined functor from $\Mat(\D_f)$ to $\Tgrl$ 
since our assignment for the generating Soergel diagrams are all $\Uq$-intertwiners.



Thus, the main part is to show that 
the relations are satisfied. This is 
now a case-by-case check where we only 
do a few as examples and leave the rest to the reader.



\textbf{Frobenius and isotopy relations}: 
we do not have to check the Frobenius relations 
\textbf{Frob1} and \textbf{Frob2}~\eqref{eq-frob} and the isotopy relations \textbf{Iso1} and \textbf{Iso2}~\eqref{eq-iso}, since, 
by part (a) of Corollary~\ref{cor-funcgrad3}, we see that $\Theta_s$ and $\Theta_t$ 
are (graded) self-adjoint functors. 
By a more general principle such functors always give rise to a Frobenius structure, see e.g.~\cite[Lemma~3.4]{mueg}.





\textbf{Needle}: for simplicity of 
notation, we assume that we are in the even case. We show
\[
\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/needlecheck}};
(0,-0.5)*{\circ};
\endxy\right)=0
\]
This follows from
\[
\xymatrix{
  M_{k+1}  \ar[rr]|/0.0em/{\begin{pmatrix}
  \mathrm{id} \\ 0
\end{pmatrix}}  &   & \tilde M_{k+1}  \ar[rr]|/0.0em/{\begin{pmatrix}
  0 & 
\mathrm{id}
\end{pmatrix}}  & &  M_{k+1}\\
}
\]
The odd case is similar. 
This clearly implies the needle relation.



\textbf{The dead-end relations 1+2}: \textbf{DE1} follows by construction. The \textbf{DE2} relation is
\[
\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/decheck}};
(-4.1,-0.2)*{\circ};
\endxy\right)=0
\]
This follows from
\[
\xymatrix{
  \Tn{\bbz}  \ar[r]^/0.0em/{u_0}  & \Tn{\bbo}  \ar[r]^/0.0em/{\tilde{d}_1}  &  \Tn{\bbz}\\
}
\]
which is the dead-end relation in the tilting case.



\textbf{Barbell forcing 1}: we only do one case (the one with equal colors) 
and leave the other (similar) case to the reader. 
Again, for simplicity of notation, we focus on
\[
\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/BF1check1}};
(-4.1,-0.25)*{\circ};
\endxy\right)=2\cdot \mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/BF1check2}};
(-0.5,-0.25)*{\circ};
\endxy\right)-\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/BF1check3}};
(-4.4,-0.25)*{\circ};
\endxy\right)
\]
The general case follows completely similar. 
We have already explained in Example~\ref{ex-functor} 
how to obtain the left two matrices. Thus, we obtain
\[
\begin{pmatrix}
 \mathrm{id} & \varepsilon_1 & 0 & 0\\ 0& 0&\mathrm{id} & \tilde{\varepsilon}_1
\end{pmatrix}\circ \begin{pmatrix}
 \varepsilon_1 & 0\\ \mathrm{id} & 0\\0& \tilde{\varepsilon}_1\\ 0 & \mathrm{id}
\end{pmatrix}=\begin{pmatrix}
 2\tilde{\varepsilon}_1 & 0\\ 0& 2\tilde{\varepsilon}_1
\end{pmatrix}
\]
for the left side. The middle (without the factor $2$) can be directly read off as
\[
\begin{pmatrix}
 \tilde{\varepsilon}_1\\ \mathrm{id}
\end{pmatrix}\circ \begin{pmatrix}
 \mathrm{id} & \tilde{\varepsilon}_1
\end{pmatrix}=\begin{pmatrix}
 \tilde{\varepsilon}_1 & 0\\ \mathrm{id}& \tilde{\varepsilon}_1
\end{pmatrix}
\]
The rightmost term is the result of 
applying $\Theta_t$ to $2\tilde{\varepsilon}_1$ 
(which is the composite of the diagram for the 
first two strands). This can be computed as 
explained in Section~\ref{sec-quiver}. Thus, we obtain
\[
\begin{pmatrix}
 2\tilde{\varepsilon}_1 & 0\\ 0& 2\tilde{\varepsilon}_1
\end{pmatrix}=2\cdot \begin{pmatrix}
 \tilde{\varepsilon}_1 & 0\\ \mathrm{id}& \tilde{\varepsilon}_1
\end{pmatrix}- \begin{pmatrix}
 0 & 0\\ 2\cdot\mathrm{id}& 0
\end{pmatrix}
\]



\textbf{Barbell forcing 2}: this is very similar to \textbf{BF1} 
(only two terms are different) and we only sketch it 
here. As before we only consider one particular case 
(the same as above for \textbf{BF1}) and leave the others for the reader to verify. 
The different two terms are now
\[
\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/BF2check1}};
(-4.1,-0.25)*{\circ};
\endxy\right),\quad\quad\mathcal D_{\infty}\left(\xy
(0,0)*{\includegraphics[scale=0.85]{res/figs/functor/BF2check2}};
(-4.4,-0.25)*{\circ};
\endxy\right)
\]
These two cases give the matrices
\[
\begin{pmatrix}
 2\cdot\tilde{\varepsilon}_1 & 0\\ 0& 2\cdot\tilde{\varepsilon}_1
\end{pmatrix}\quad\text{and}\quad\begin{pmatrix}
 0 & 0\\ 2\cdot\mathrm{id}& 0
\end{pmatrix}
\]
and the equation \textbf{BF2}~\eqref{eq-barbforc} then reads as
\[
\begin{pmatrix}
 2\cdot\tilde{\varepsilon}_1 & 0\\ 0& 2\cdot\tilde{\varepsilon}_1
\end{pmatrix}=\begin{pmatrix}
 0 & 0\\ 2\cdot\mathrm{id}& 0
\end{pmatrix}+2\begin{pmatrix}
 \tilde{\varepsilon}_1 & 0\\ \mathrm{id}& \tilde{\varepsilon}_1
\end{pmatrix}- 2\begin{pmatrix}
 0 & 0\\ 2\cdot\mathrm{id}& 0
\end{pmatrix}
\]
This finishes the proof.
\end{proof}




\begin{thm}(\textbf{Diagram categories for $\Tgrl$})\label{thm-diafortilt}
The functor $\mathcal{D}_{\infty}\colon \Mat(\QDk)\to\Tgrl$ is an equivalence of graded categories.\makeqed
\end{thm}



\begin{proof}
We have to show that $\mathcal{D}_{\infty}$ is 
essentially surjective, full and faithful.



\textbf{Essentially surjective}: we have to show 
that, given some arbitrary object $M\in\Ob(\Tgrl)$, 
then there is an object $x\in\Ob(\Mat(\QDk))$ such 
that $\mathcal{D}_{\infty}(x)\cong M$. To see this, 
note that, by part (c) of Proposition~\ref{prop-tilt}, 
it is enough to verify this for indecomposable 
$\Uq$-modules $\Tn{\bbi}$ in the ungraded setting 
(using Proposition~\ref{prop-grading} the same is still true in the graded setting).
Now, because of our construction and part 
(b) of Corollary~\ref{cor-theta}, we see that 
$\mathcal{D}_{\infty}(x_{i-tst})\cong\Tn{\bbi}$ 
which shows that the functor is essentially surjective.



\textbf{Fully faithful}: by Lemmas~\ref{lem-decom2} and~\ref{lem-welldef} 
it is enough to show that
\[
\Hom_{\Mat(\QDk)}(x,x^{\prime})\cong\Hom_{\Tgrl}(\mathcal{D}_{\infty}(x),\mathcal{D}_{\infty}(x^{\prime}))
\]
holds as graded $\bC$-vector spaces for alternating sequences $x=x_{i-tst}$ and $x^{\prime}_{i^{\prime}-tst}$.
We have already computed both sides: the 
right side was computed in 
Corollary~\ref{cor-homspaces} and the 
left in Corollary~\ref{cor-homspaces2}. 
By our construction, the (graded) isomorphism 
is induced by the assignment 
$\bbi\mapsto\bbi$, $u_i\mapsto u_i$, 
$d_i\mapsto \tilde{d}_i$ and 
$\varepsilon_i\mapsto\tilde{\varepsilon}_i$ 
whenever this makes sense.
\end{proof}



\begin{cor}\label{cor-diafrotilt}
The category $\Mat(\QDk)$ is idempotent complete.\makeqed
\end{cor}



\begin{proof}
This follows from Theorem~\ref{thm-diafortilt} 
because in $\Tgrl\cong\T_{\lambda}$ every module 
decomposes into a direct sum of (shifted copies of) $\Tn{\bbi}$'s. 
\end{proof}




\begin{cor}(\textbf{Diagram categories for the center})\label{cor-diafrocenter}
The graded $\bC$-algebra $\End^{\mathrm{fs}}_{\mathrm{gr}}(\mathrm{id})$ of 
natural transformations in $\Endo(\Tgrl)$ of the 
identity functor $\mathrm{id}$ is given by the 
diagonal part of finitely supported (only a finite number of non-zero entries) matrices
\begin{equation}\label{eq-fcenter}
F\colon \emptyset\oplus g\oplus rg\oplus grg\oplus rgrg\oplus\dots\to\emptyset\oplus g\oplus rg\oplus grg\oplus rgrg\oplus\dots
\end{equation}
of marked Soergel diagrams with no identity 
diagram entry. In contrast, 
$\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})\cong \Ai$ is 
given by all such matrices and not just the diagonal part.\makeqed
\end{cor}



\begin{proof}
An alternating sequence of red and green of 
length $i$ corresponds under the equivalence 
from Theorem~\ref{thm-diafortilt} to $\Tn{\bbi}$, 
since, by Proposition~\ref{prop-quiverrel}, the 
quiver relations are satisfied. This module 
corresponds under the isomorphisms from 
Corollary~\ref{cor-center} to ${}_iP$. Thus, the 
claim follows by Theorem~\ref{thm-diafortilt} and 
Proposition~\ref{prop-endograd2}, since (graded) 
equivalent categories have (graded) isomorphic 
centers and the observation that an $F$ as 
in~\eqref{eq-fcenter} is a natural transformation 
iff it commutes with all other such $F$'s 
(compare also to~\eqref{eq-natural}). That 
the center of the matrix ring is as stated 
above is then an easy to deduce fact: the 
$\bbi$ are not central (as already noted 
after Definition~\ref{def-ksquiver1}), while 
the $\varepsilon_i$ compose with everything to zero 
(and are therefore in the center).
\end{proof}




\begin{rem}\label{rem-overfinitefields}
Relaxing the conditions 
to work over another field and not $\bC$ is actually a 
problem in Section~\ref{sec-tilting} since the 
indecomposable tilting modules and their hom-spaces 
are much more complicated in positive characteristic. 
For the KS quiver algebras from Section~\ref{sec-quiver} working over 
$\bZ$ is not a huge problem, while for the diagrammatic category 
$\QD$ we need to work over $\bQ$.
\end{rem}
