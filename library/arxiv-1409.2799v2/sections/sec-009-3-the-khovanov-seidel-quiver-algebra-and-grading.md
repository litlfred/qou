---
doc_id: arxiv-1409.2799v2
doc_title: "Diagram categories for Uq-tilting modules at roots of unity"
section_id: sec-009-3-the-khovanov-seidel-quiver-algebra-and-grading
section_title: "The Khovanov-Seidel quiver algebra and gradings"
section_number: 3
pages: 17-27
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.976
doc_brief: "Diagram categories for Uq-tilting modules at roots of unity — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
\label{sec-quiver}

In the present section\footnote{We use \textit{right} modules in this 
section and read from right to left: we think of the paths 
in the quiver as applying morphisms/functors. The reason for this 
will become clear in Subsection~\ref{sub-ainfty}.} we identify 
the quiver for the blocks $\T_{\lambda}$. We show how the 
quiver description can be used to define a grading on $\T$. We 
obtain a grading on $\Endo(\T)$ as well.



Additionally, we show how the translation functors of $\T_{\lambda}$ 
can be used to get a categorification of the action of the 
braid group on the (split) Grothendieck group of $\T_{\lambda}$ which realizes the 
Burau representation on the (split) Grothendieck group. Moreover, we show how 
the category of projective endofunctors on $\T_{\lambda}$ can be used to 
categorify 
(parts of) the Temperley-Lieb $\bQ(v)$-algebras (where the grading decategorifies to the 
indeterminate $v$).


By an algebra we always mean an associative, but not necessarily unital $\bC$-algebra.



\subsection{The quiver algebras \texorpdfstring{$\Am$}{Qm} and \texorpdfstring{$\Ai$}{Ain}}\label{sub-qalg}
Let $m\in\bN$. We consider the following quiver
\begin{equation}\label{eq-quiver}
\xymatrix{
  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbm};\endxy}  \ar@<-2pt>[r]_/-0.25em/{d_{m}}  &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbmd};\endxy}  \ar@<-2pt>[l]_{u_{m-1}}\ar@<-2pt>[r]_{d_{m-1}} & 
\raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbmdd};\endxy}  \ar@<-2pt>[l]_{u_{m-2}}\ar@<-2pt>[r]_{d_{m-2}} &  
  \cdots \ar@<-2pt>[l]_{u_{m-3}}\ar@<-2pt>[r]_/+0.2em/{d_{3}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy}  \ar@<-2pt>[l]_/-0.2em/{u_{2}}\ar@<-2pt>[r]_{d_{2}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy}  \ar@<-2pt>[l]_{u_{1}}\ar@<-2pt>[r]_{d_{1}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}  \ar@<-2pt>[l]_{u_0}\\
}
\end{equation}
having $m+1$ vertices $\bbz,\bbo,\dots,\bbm$ and $2m$ arrows called \textit{up and down}:
\[
u_i\colon \bbi\to \bbiu,\;i=0,\dots,m-1,\quad\quad d_i\colon \bbi\to \bbid,\;i=1,\dots,m.
\]



The \textit{path algebra} $P_m$ of the quiver 
from~\eqref{eq-quiver} is defined to 
be the $\bC$-algebra whose underlying 
$\bC$-module is the $\bC$-vector 
space spanned by all finite paths 
with multiplication given by composition 
of paths if possible and zero otherwise.


Recall that a $\bZ$\textit{-graded} 
$\bC$-algebra $A$ (or simply \textit{graded}) is a 
$\bC$-algebra $A=\oplus_{i\in\bZ} A^i$ such that $A^iA^j\subset A^{i+j}$ 
for all $i,j\in\bZ$.
The path algebra $P_m$ is a graded 
$\bC$-algebra\footnote{Note that Khovanov and Seidel 
use free $\bZ$-modules instead of $\bC$-vector spaces. 
In order to avoid too many different overlapping notations, 
we only use the $\bC$-vector space version, but it is not a big problem to work over $\bZ$.}, 
that is
\[
P_m=\bigoplus_{k\in\bZ_{\geq 0}}P^k_m,\quad\text{with}\; P^k_m=\{\text{All paths in }P_m\text{ of length }k\},
\]
since we clearly have 
$P^k_m\circ P^{k^{\prime}}_m\subset P^{k+k^{\prime}}_m$. We 
write $l(\cdot)$ for the grading on $P_m$ (the ``length'').





\begin{defn}\label{def-ksquiver1}(\textbf{Khovanov-Seidel's $m$-quiver algebra})
Let $\Am$ denote the quotient algebra obtained from the path algebra 
$P_m$ for the quiver from~\eqref{eq-quiver} by the defining relations
\begin{gather*}
u_{i}\circ u_{i-1}=0=d_i\circ d_{i+1},\;i=1,\dots,m-1,\quad\quad d_{i+1}\circ u_i=u_{i-1}\circ d_{i},\;i=1,\dots,m-1,\\
d_1\circ u_0=0.
\end{gather*}
The latter is called the \textit{dead-end relation}.
Given two paths $p,p^{\prime}\in \Am$ we write $p^{\prime}p$ 
instead of $p^{\prime}\circ p$. The algebra $\Am$ 
inherits the grading $l(\cdot)$ from $P_m$ 
since all the relations are homogeneous. 
We call $\Am$ for short \textit{KS} $m$\textit{-quiver algebra}.
\end{defn}




We denote, by abuse of notation, the path of length $0$ that 
starts and ends at $\bbi$ also by $\bbi$. Note that 
the $\bbi$ are projectors or idempotents, because 
$\bbi\bbi=\bbi$, $p\bbi=p$ if $p$ starts in $\bbi$ 
and $0$ else and $\bbi p=p$ if $p$ ends in $\bbi$ 
and $0$ else. Moreover, they form a complete set of 
pairwise orthogonal idempotents, that 
is $1=\bbz+\bbo+\dots+\bbm$ and $\bbi\bbj=\delta(\bbi,\bbj)$, 
where $1\in \Am$ is the unit. Note that $0\neq \bbz$, 
$1\neq \bbo$ and the $\bbi$'s are not central 
for $m>0$, since e.g. $0=\bbi u_i\neq u_i\bbi=u_i$ for $i=0,\dots,m-1$.



Moreover, we denote for $i=1,\dots,m$ by $\varepsilon_i=u_{i-1}d_i$ 
the loop that starts at $\bbi$ and goes via $d_i$ to $\bbid$ 
and then back via $u_{i-1}$. Note that the relations imply 
that $\varepsilon_i=d_{i+1}u_i$ (if possible, i.e. if $i+1\leq m$). 
Thus, the $\bC$-algebra $\Am$ has a basis given by $\bbi$ 
(for $i=0,\dots,m$) and $u_i$ (for $i=0,\dots,m-1$) and 
$d_i, \varepsilon_i$ (for $i=1,\dots,m$) with $l(\bbi)=0,l(u_i)=l(d_i)=1$ and $l(\varepsilon_i)=2$.


We call an algebra homomorphism $f\colon A\to B$ between 
graded algebras $A$ and $B$ a 
\textit{homomorphism of graded algebras}, if $f(A^k)\subset B^k$ for all $k\in\bZ$.
We have the following.

\begin{lem}\label{lem-inclusion}
There is a sequence of (non-unital!) inclusions of graded algebras
\[
\xymatrix{
  Q_0 \ar@^{(->}[r]^{\iota_0} &  Q_1  \ar@^{(->}[r]^{\iota_1}  & Q_2  \ar@^{(->}[r]^{\iota_2} & \dots,
}
\]
where $\iota_m\colon Q_m\to Q_{m+1}$ is defined by $\bbi,u_i,d_i,\varepsilon_i\mapsto \bbi,u_i,d_i,\varepsilon_i$ for all suitable indices $i$.\makeqed
\end{lem}



\begin{proof}
This follows because $P_m$ includes 
into $P_{m+1}$ and the set of relations for 
$\Am$ is included in the ones for $Q_{m+1}$. 
That these morphisms respect the grading and are injective is immediate.
\end{proof}




This motivates the following definition.
\begin{defn}\label{def-ksquiver2}(\textbf{Khovanov-Seidel's $\infty$-quiver algebra})
Define $\Ai$ to be the inductive limit 
of the sequence of inclusions of graded 
algebras from Lemma~\ref{lem-inclusion}, that is $\Ai=\varinjlim \Am$. 
We call it for short 
\textit{KS} $\infty$\textit{-quiver algebra}.
\end{defn}



Note that $\Ai$ is a graded $\bC$-vector 
space of countable dimension. Moreover, 
$\Ai$ is an algebra with a 
complete set of pairwise orthogonal 
idempotents $\{\bbi\mid i\in\bN\}$, 
but $\Ai$ is a \textit{non-unital} algebra, 
since the unit would have to be an infinite sum of the $\bbi$'s. Such 
an algebra is sometimes called \textit{idempotented}.


\begin{ex}\label{ex-quiver}
$Q_0$ consists just of $\bC$-multiples of 
$\bbz$. The algebra $Q_{m>0}$ can be visualized as
\[
\xymatrix{
  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbm};\endxy} \ar@(ul,ur)|{\varepsilon_m} \ar@<-2pt>[r]_{d_{m}} & \cdots \ar@<-2pt>[l]_{u_{m-1}}\ar@<-2pt>[r]_/+0.2em/{d_{i+1}} &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy} \ar@(ul,ur)|{\varepsilon_i} \ar@<-2pt>[l]_/-0.2em/{u_{i}}\ar@<-2pt>[r]_{d_{i}} & \cdots \ar@<-2pt>[l]_{u_{i-1}}\ar@<-2pt>[r]_/+0.2em/{d_{3}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy} \ar@(ul,ur)|{\varepsilon_2} \ar@<-2pt>[l]_/-0.2em/{u_{2}}\ar@<-2pt>[r]_{d_{2}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy} \ar@(ul,ur)|{\varepsilon_1} \ar@<-2pt>[l]_{u_{1}}\ar@<-2pt>[r]_{d_{1}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}  \ar@<-2pt>[l]_{u_0}\\
}
\]
The KS $\infty$-quiver algebra $\Ai$ can be visualized as
\[
\xymatrix{
   \cdots\ar@<-2pt>[r]_/+0.2em/{d_{i+1}} &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy} \ar@(ul,ur)|{\varepsilon_i} \ar@<-2pt>[l]_/-0.2em/{u_{i}}\ar@<-2pt>[r]_{d_{i}} & \cdots \ar@<-2pt>[l]_{u_{i-1}}\ar@<-2pt>[r]_/+0.2em/{d_{3}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy} \ar@(ul,ur)|{\varepsilon_2} \ar@<-2pt>[l]_/-0.2em/{u_{2}}\ar@<-2pt>[r]_{d_{2}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy} \ar@(ul,ur)|{\varepsilon_1} \ar@<-2pt>[l]_{u_{1}}\ar@<-2pt>[r]_{d_{1}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}  \ar@<-2pt>[l]_{u_0}\\
}
\]
We point out that $\Ai$ only has one 
asymmetry coming from the dead-end 
relation. Moreover, $\Ai$ is graded by the 
path length $l(\cdot)$ due to the fact 
that $\Ai$ does not contain infinite paths.
\end{ex}



In order to be able to also consider the 
semisimple blocks $\T_{-1}$ and $\T_{l-1}$ of 
our category $\T$, we also introduce another 
quotient of the path algebra $P_m$, denoted 
by $\At$, (and take a limit as above). Since 
the corresponding module categories should be 
semisimple, the quotient $\At$ is rather trivial 
and we call it \textit{KS trivial $m$-quiver algebra}.




\begin{defn}\label{defn-trivial}(\textbf{Khovanov-Seidel's trivial $m$-quiver algebra})
Let $\At$ denote the quotient algebra 
obtained from the path algebra $P_m$ for 
the quiver from~\eqref{eq-quiver} by the defining relations
\[
u_{i}=0=d_{i+1},\;i=0,\dots,m-1.
\]
The algebra $\At$ inherits the grading 
$l(\cdot)$ from $P_m$, but this grading is trivial. 
$\At$ consists only of orthogonal idempotents $\bbi$ for $i=0,\dots, m$. These idempotents 
form a set of pairwise non-isomorphic, central, orthogonal idempotents which shows 
that $\At$ is a semisimple algebra. Moreover, the algebra $\At$ is clearly isomorphic to $\bC\times\dots\times\bC$ (with $m+1$ factors).



As before we define \textit{Khovanov-Seidel's trivial} $\infty$\textit{-quiver algebra} via $\Att=\varinjlim\At$. We note that this can be visualized as
\[
\xymatrix{
   \cdots &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy}  & \cdots  & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}\\
}
\]
where we take the inductive limit as above.
\end{defn}



For convenience we set $u_m=d_0=\varepsilon_0=0$ for all $\Am$ and $d_0=\varepsilon_0=0$ for $\Ai$ in the following.




\subsection{Combinatorics of the graded, right \texorpdfstring{$\Am$}{Qm}- and \texorpdfstring{$\Ai$}{Ain}-modules}\label{sub-ammod}
Recall that, if $A$ denotes some 
graded $\bC$-algebra, then a (right) 
$A$-module $M$ is called \textit{$\bZ$-graded} (or simply \textit{graded}), if
\[
M=\bigoplus_{k\in\bZ}M^k\quad\text{and}\quad M^k\cdot A^{k^{\prime}}\subset M^{k+k^{\prime}}.
\]
An $A$-module homomorphism between 
graded modules $f\colon M\to N$ is called 
\textit{degree preserving}, if $f(M^k)\subset N^k$ 
for all $k\in\bZ$ and \textit{homogeneous 
(of degree $d\in\bZ$)} if $f(M^k)\subset N^{k+d}$ for all $k\in\bZ$.
We denote by $\ModgrA$ the category of 
\textit{graded}, finitely generated $A$-modules 
whose morphisms from $M$ to $M^{\prime}$ are given by
\begin{equation}\label{eq-gradhom}
\Hom_{\ModgrA}(M,M^{\prime})=\bigoplus_{s\in\bZ}\Hom_{A}(M,M^{\prime}\langle s\rangle)_{0},
\end{equation}
where the zero should mean \textit{degree preserving} 
morphisms and $\langle s\rangle$ 
denotes a shift as below. Thus, all morphisms in $\ModgrA$ are finite 
direct sums of homogeneous morphisms.




The endofunctor $\cdot\langle s\rangle\colon\ModgrA\to\ModgrA$, 
called \textit{shift\footnote{In our convention a positive number shifts the degree \textit{up}.} 
by $s\in\bZ$} sends the $k-s$-th degree part of a module to the 
$k$-th of the shift $M\langle s\rangle$, that is, $M\langle s\rangle^k=M^{k-s}$.



We use similar notions for left modules 
(we denote such categories by e.g. $\AModgr$) 
or projective modules (we denote such categories 
by e.g. $\pModgrA$). We \textit{only} 
work in categories of (graded) finitely generated (projective) modules.



$\Am$ acts on itself from the right 
by \textit{pre}-composition and from the 
left by \textit{post}-composition of paths.
This makes a difference: 
let us denote by $P_i$ the 
left ideal of $\Am$ generated 
by $\bbi$. Similar, ${}_iP$ denotes 
the right ideal generated by $\bbi$. We have as $\bC$-vector spaces
\[
P_i=\bC\bbi\oplus\bC u_i\oplus\bC d_i\oplus\bC\varepsilon_i,\quad\quad{}_iP=\bC\bbi\oplus\bC u_{i-1}\oplus\bC d_{i+1}\oplus\bC\varepsilon_i,
\]
with homogeneous components of degree $0,1,1,2$ (from left to right).




The $P_i$ and the ${}_iP$ are graded 
$\Am$-modules (left and right respectively) that can be visualized as
\[
P_i=\xymatrix{
  \cdots  & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy}\ar@(ul,ur)|{\varepsilon_i}  \ar@<-2pt>[l]_/-0.2em/{u_i}\ar@<-2pt>[r]_/-0.2em/{d_i} &\cdots \\
},\quad\quad{}_iP=\xymatrix{
   \cdots \ar@<-2pt>[r]_{d_{i+1}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy}\ar@(ul,ur)|{\varepsilon_i}   &\cdots \ar@<-2pt>[l]_{u_{i-1}}.\\
}
\]
Thus, the $P_i$'s and the ${}_iP$'s 
are projective, since we have (as left, respectively right, $\Am$-modules)
\[
\Am=\bigoplus_{i=0}^m P_i,\quad\quad \Am=\bigoplus_{i=0}^m {}_iP.
\]
Moreover, they are all indecomposable because 
they are the projective covers of the simple left, respectively right, $\Am$-modules $L_i$ 
and ${}_iL$ 
obtained from $P_i$ 
and ${}_iP$ by killing $u_i,d_i$ and $\varepsilon_i$ 
respectively $u_{i-1}$, $d_{i+1}$ and $\varepsilon_i$.
Furthermore, it is easy to see that all 
indecomposable left, respectively right, 
$\Am$-modules are of the form $P_i\langle s\rangle$, 
respectively ${}_iP\langle s\rangle$, for some $s\in\bZ$: 
this follows directly from the fact that $\Am$ is 
finite-dimensional. Thus, all indecomposable projective $\Am$-modules are 
direct summands of $\Am$ considered as a (left or right) $\Am$-module.




\begin{ex}\label{ex-decomp}
One easily checks that the same is true for 
the corresponding notions for $\Ai$ and 
that one gets a decomposition into ${}_iP$'s as 
follows (we have indicated the neighbouring ${}_iP$'s 
using alternating colors and we for simplicity assume that the $i$ below is odd)
\[
\xymatrix{
   \cdots\ar@[blue]@<-2pt>[r]_/+0.2em/{{\color{blue}d_{i+1}}} &  {\color{blue}\raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy}} \ar@[blue]@(ul,ur)|{{\color{blue}\varepsilon_i}} \ar@[green]@<-2pt>[l]_/-0.2em/{{\color{green}u_{i}}}\ar@[green]@<-2pt>[r]_{{\color{green}d_{i}}} & \cdots \ar@[blue]@<-2pt>[l]_{{\color{blue}u_{i-1}}}\ar@[green]@<-2pt>[r]_/+0.2em/{{\color{green}d_{3}}} & {\color{green}\raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy}} \ar@[green]@(ul,ur)|{{\color{green}\varepsilon_2}} \ar@[blue]@<-2pt>[l]_/-0.2em/{{\color{blue}u_{2}}}\ar@[blue]@<-2pt>[r]_{{\color{blue}d_{2}}} & {\color{blue}\raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy}} \ar@[blue]@(ul,ur)|{{\color{blue}\varepsilon_1}} \ar@[green]@<-2pt>[l]_{{\color{green}u_{1}}}\ar@[green]@<-2pt>[r]_{{\color{green}d_{1}}} & {\color{green}\raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}} \ar@[blue]@<-2pt>[l]_{{\color{blue}u_0}}\\
}
\]
We encourage the reader to draw the 
decomposition into $P_i$'s. Again, all 
finitely generated, graded projective, 
indecomposable right $\Ai$-modules are, up 
to a shift, of the form ${}_iP$. Same for 
the left modules and the $P_i$'s. This can 
be deduced directly, but is 
true in more generality for idempotented 
algebras, see for example~\cite[Proposition~5.3.1]{klms}.
\end{ex}



Similarly for $\At$ and $\Att$ which decompose into the 
corresponding (left and right) modules denoted 
by $P_i^{\mathrm{triv}}$ and ${}_iP^{\mathrm{triv}}$.





\subsection{Endofunctors on \texorpdfstring{$\pModgr$-$\Am$}{pMod-Qm} and \texorpdfstring{$\pModgr$-$\Ai$}{pMod-Qin}}\label{sub-endo}
Set\footnote{Note that we use a different convention than Khovanov and Seidel for the gradings by shifting ${}_iP$ down by one.} 
$B_i=P_i\otimes_{\bC}{}_iP\langle -1\rangle$ for all 
indices $i=1,\dots,m$. Note that the $B_i$'s are 
graded $\Am$-bimodules with the tensor product 
$p\otimes p^{\prime}$ of degree $l(p\otimes p^{\prime})=l(p)+l(p^{\prime})$ 
for $p$ of degree $l(p)$ and $p^{\prime}$ of degree $l(p^{\prime})$. 
We define functors
\[
\mathcal U_i\colon \pModgrAm\to \pModgrAm,\;\mathcal U_i= \cdot \otimes_{\Am}B_i\quad\text{for}\quad i=1,\dots,m.
\]
Note that we have
\begin{equation}\label{eq-ufunctors}
{}_{i^{\prime}}P\otimes_{\Am}P_i\cong\biggl\{
\begin{matrix}
 \bC\bbi\oplus\bC\varepsilon_i,\; \text{if }|i-i^{\prime}|=0, & & \bC u_{i},\;\text{if }i^{\prime}-i=1,\\
 \bC d_{i},\;\text{if }i-i^{\prime}=1, & & 0,\;\text{if }|i-i^{\prime}|>1.
\end{matrix}
\end{equation}
This can be easily seen by considering (here $i=i^{\prime}$ as an example)
\[
\xymatrix{
   \cdots \ar@<-2pt>[r]_{d_{i+1}} & \raisebox{0.1cm}{\xy(0,0)*{{\color{green}\bullet}};(0,-2.5)*{{\color{green}\scriptstyle \bbi}};\endxy}\ar@[green]@(ul,ur)|{{\color{green}\varepsilon_i}}   &\cdots \ar@<-2pt>[l]_{u_{i-1}}\\
}\otimes_{\Am}\xymatrix{
  \cdots  & \raisebox{0.1cm}{\xy(0,0)*{{\color{green}\bullet}};(0,-2.5)*{{\color{green}\scriptstyle \bbi}};\endxy}\ar@[green]@(ul,ur)|{{\color{green}\varepsilon_i}}  \ar@<-2pt>[l]_/-0.3em/{u_i}\ar@<-2pt>[r]_/-0.3em/{d_i} &\cdots, \\
}
\]
where we have illustrated the 
overlapping pieces of ${}_iP$ and $P_i$. This clearly implies
\begin{equation}\label{eq-tlcat}
\mathcal U_i ({}_{i^{\prime}}P)\cong\begin{cases}{}_iP\langle -1\rangle\oplus {}_iP\langle +1\rangle,&\text{if }|i-i^{\prime}|=0,\\
{}_iP,&\text{if }|i-i^{\prime}|=1,\\
0,&\text{if }|i-i^{\prime}|>1.\end{cases}
\end{equation}
We note that we can see ${}_{i^{\prime}}P\otimes_{\Am}P_i$ as a 
graded, right $\At$-module where the action of $\bbi$ kills 
everything that does not start in $\bbi$. Note that, in this 
notation, $\bC\bbi,\bQ u_{i},\bC d_{i}$ and $\bC\varepsilon_i$ 
are all one dimensional $\At$-modules concentrated 
in degrees $0,1,1$ and $2$ respectively.
Hence, as graded, 
right $\At$-modules, 
$\bC u_{i}\cong\bC \bbi\langle+1\rangle$, $\bC d_{i}\cong\bC \bbi\langle+1\rangle$ and $\bC \varepsilon_{i}\cong\bC \bbi\langle+2\rangle$.



\begin{cor}\label{cor-tlfunctor}
The functors $\mathcal U_i\colon\pModgrAm\to\pModgrAm$ satisfy the following.
\begin{itemize}
\item[(a)] $\mathcal U_i\circ\mathcal U_i\cong \mathcal U_i\langle -1\rangle\oplus \mathcal U_i\langle +1\rangle$ for $i=1,\dots,m$.
\item[(b)] Let $i^{\prime}=i\pm 1$ such that $i,i^{\prime}\in\{1,\dots,m\}$. Then $\mathcal U_i\circ\mathcal U_{i^{\prime}}\circ\mathcal U_i\cong\mathcal U_i$.
\item[(c)] $\mathcal U_i\circ\mathcal U_{i^{\prime}}\cong 0$, if $|i-i^{\prime}|>1$.\makeqed
\end{itemize}
\end{cor}



\begin{proof}
This follows directly from~\eqref{eq-tlcat}.
\end{proof}



Finally we set
\[
\mathcal U_{\mathrm{even}}=\!\!\bigoplus_{1\leq i, 2i\leq m}\!\!\mathcal U_{2i},\quad\quad\mathcal U_{\mathrm{odd}}=\!\!\bigoplus_{0\leq i, 2i+1\leq m}\!\!\mathcal U_{2i+1}.
\]
By Corollary~\ref{cor-tlfunctor} we see that
\begin{equation}\label{eq-evenodd}
\mathcal U_{\mathrm{even}}\circ \mathcal U_{\mathrm{even}}\cong \mathcal U_{\mathrm{even}}\langle -1\rangle\oplus \mathcal U_{\mathrm{even}}\langle +1\rangle,\quad\quad\mathcal U_{\mathrm{odd}}\circ \mathcal U_{\mathrm{odd}}\cong \mathcal U_{\mathrm{odd}}\langle -1\rangle\oplus \mathcal U_{\mathrm{odd}}\langle +1\rangle.
\end{equation}
It is clear that we can easily adapt 
the definition of the $\mathcal U_i$'s 
to the $\Ai$ case. We denote these 
functors by $\mathcal U^{\infty}_i$ 
for all $i\in\bZ_{>0}$. These functors satisfy completely similar relations as before.



We also define $\mathcal U^{\infty}_{\mathrm{even}}$ 
and $\mathcal U^{\infty}_{\mathrm{odd}}$ completely 
analogously by taking the direct sum over all 
$i\in\bZ_{>0}$. The reader is still invited to 
check that these two satisfy similar relations as in~\eqref{eq-evenodd}.



We also refine 
the definitions of the functors $\mathcal U_i$ 
by \textit{factoring through} the category of 
graded (right) $\At$-modules which we denote by 
$\ModgrAt$. To be precise, we define $\mathcal U_i^t$ and $\mathcal U^i_t$ via
\begin{gather*}
\mathcal U_i^t\colon\ModgrAm\to\ModgrAt,\; \mathcal U_i^t=\cdot\otimes_{\Am}P_i
\\
\mathcal U^i_t\colon\ModgrAt\to\ModgrAm,\; \mathcal U^i_t=\cdot\otimes_{\bC}{}_iP\langle -1\rangle.
\end{gather*}
It is immediate that $\mathcal U_i=\mathcal U^i_t\circ\mathcal U^t_i$. 
We define even and odd versions of these refinements 
as before where we use $\mathcal U^t_{\mathrm{even}}$ 
and $\mathcal U_t^{\mathrm{even}}$ as notations (similar for the odd versions).



The following lemma can be seen, by Remark~\ref{rem-cato} below, 
as an analog of~\cite[Theorem~8.4]{st2}.



\begin{lem}\label{lem-adjoint}
As graded functors: $\mathcal U^t_i\langle+1\rangle$ is 
the right adjoint of $\mathcal U_t^i$, $\mathcal U^t_i$ 
is the left adjoint of $\mathcal U_t^i\langle-1\rangle$. 
Similar for the even/odd versions. The functors $\mathcal U_i$, $\mathcal U_{\mathrm{even}}$ 
and $\mathcal U_{\mathrm{odd}}$ are all graded self adjoint.\makeqed
\end{lem}



\begin{proof}
This is a case-by-case check. 
We use that, as graded $\bC$-vector spaces, we have
\begin{equation}\label{eq-homps}
\Hom_{\pModgrAm}({}_iP,{}_{i^{\prime}}P)\cong\biggl\{
\begin{matrix}
 \bC\bbi\oplus\bC\varepsilon_i,\; \text{if }|i-i^{\prime}|=0, & & \bC u_{i},\;\text{if }i^{\prime}-i=1,\\
 \bC d_{i},\;\text{if }i-i^{\prime}=1, & & 0,\;\text{if }|i-i^{\prime}|>1.
\end{matrix}
\end{equation}
The isomorphism is given by mapping a 
path $p$ on the right-hand side to the 
homomorphism ${}_iP\to {}_{i^{\prime}}P$ 
given by left multiplication 
(\textit{post}-composition) with $p$. 
Note that this is a homogeneous morphism of degree $l(p)$.


We only 
prove that $\mathcal U^t_i\langle+1\rangle$ is 
the right adjoint of $\mathcal U_t^i$ and leave the rest to the reader.
To this end, we have to show that there are isomorphisms of graded vector spaces
\[
\Hom_{\pModgrAm}(\mathcal U_t^i(\bC\bbi),{}_{i^{\prime}}P)\cong\Hom_{\pModgrAt}(\bC\bbi,\mathcal U^t_i\langle+1\rangle({}_{i^{\prime}}P)),
\]
where we can restrict to check only for objects 
as above by additivity. Note that we have three 
cases depending on $i-i^{\prime}$, since the case 
$|i-i^{\prime}|>1$ is clear.


$\boldsymbol{i=i^{\prime}}$. The left-hand side is 
$\Hom_{\pModgrAm}({}_iP\langle-1\rangle,{}_iP)\cong \bC\bbi\langle+1\rangle\oplus \bC\varepsilon_i\langle+1\rangle$, which follows from~\eqref{eq-homps}. 
Moreover, by~\eqref{eq-ufunctors} and the shift by $+1$, we get the same for the right side.



$\boldsymbol{i^{\prime}=i+1}$. The left-hand 
side gives $\Hom_{\pModgrAm}({}_iP\langle-1\rangle,{}_{i+1}P)\cong \bC u_i\langle+1\rangle$. This follows again by~\eqref{eq-homps}. The right-hand side gives, 
by~\eqref{eq-ufunctors} and the shift by 
$+1$, the same result.

$\boldsymbol{i^{\prime}=i-1}$. Similarly to the case $\boldsymbol{i^{\prime}=i+1}$.


Thus, we have an adjoint pair 
$(\mathcal U_t^i,\mathcal U^t_i\langle+1\rangle)$. 
The other statements follow analogously.
\end{proof}


The same holds, mutatis mutandis, for the infinity 
versions as well.











\subsection{\texorpdfstring{$\Ai$}{Ain} and the tilting category \texorpdfstring{$\T$}{T}}\label{sub-ainfty}
Recall that the category 
$\T_{\lambda}$ denotes the 
$\lambda$-block of $\T$ for $\lambda$ 
in the fundamental alcove $\mathcal A_0$, see Subsection~\ref{sub-blocks}. 
We fix any such $\lambda$ and denote everything 
using the simplified notation without the $\lambda$'s. In particular, recall our notation from Definition~\ref{defn-tiltgen} for the tilting generators $\Tn{\bbin}$ and $\Tn{\leq\bbm}$.
We denote by $\T_{\lambda}(\leq\bbm)$ the 
full subcategory of $\T_{\lambda}$ consisting of 
objects whose indecomposable summands are all from 
the set $\{\Tn{\lambda_0},\dots,\Tn{\lambda_m}\}$ for some fixed $m\in\bN$.
We also use completely similar notations for 
the walls $\mu$ by indicating this case with a superscript $t$. 








\begin{prop}\label{prop-isoofalg1}
We have
\[
\End_{\Uq}(\Tn{\leq\bbm})\cong \Am\quad\text{and}\quad\End_{\Uq}(\Tn{\leq\bbm}^t)\cong \At,
\]
which are isomorphisms of $\bC$-algebras.\makeqed
\end{prop}



\begin{proof}
We are going to construct these 
isomorphisms explicitly. Moreover, 
if we simply write $\bbi$ for $\Tn{\bbi}$, 
then we can visualize $\End_{\Uq}(\Tn{\leq\bbm})$ 
using Proposition~\ref{prop-link} for all $m>0$ as
\[
\xymatrix{
  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbm};\endxy} \ar@(ul,ur)|{\varepsilon_m} \ar@<-2pt>[r]_{d_{m}} & \cdots \ar@<-2pt>[l]_{u_{m-1}}\ar@<-2pt>[r]_/+0.2em/{d_{i+1}} &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy} \ar@(ul,ur)|{\varepsilon_i} \ar@<-2pt>[l]_/-0.2em/{u_{i}}\ar@<-2pt>[r]_{d_{i}} & \cdots \ar@<-2pt>[l]_{u_{i-1}}\ar@<-2pt>[r]_/+0.2em/{d_{3}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbt};\endxy} \ar@(ul,ur)|{\varepsilon_2} \ar@<-2pt>[l]_/-0.2em/{u_{2}}\ar@<-2pt>[r]_{d_{2}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbo};\endxy} \ar@(ul,ur)|{\varepsilon_1} \ar@<-2pt>[l]_{u_{1}}\ar@<-2pt>[r]_{d_{1}} & \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbz};\endxy}  \ar@<-2pt>[l]_{u_0}\\
}
\]
Thus, we consider the 
(by Proposition~\ref{prop-link} well-defined) $\bC$-algebra homomorphism
\[
\phi\colon \Am\to\End_{\Uq}(\Tn{\leq\bbm}), u_i\mapsto u_i, d_i\mapsto d_i,\varepsilon_i\mapsto \varepsilon_i
\]
for all suitable indices $i$. 
Using Corollary~\ref{cor-homspaces} 
we see that this is an isomorphism. 
The case $m=0$ and the 
``trivial case'' cases are immediate which proves the statement.
\end{proof}



The morphisms of $\End_{\Uq}(\Tn{\bbin})$ are 
``matrices'' $f=\prod_{i,i^{\prime}\in\bN} f_{i^{\prime}i}$ 
with $f_{i^{\prime}i}\colon \Tn{\bbi}\to\Tn{\bbi^{\prime}}$ and each 
row consists only of finitely many non-zero entries 
(this follows from Corollary~\ref{cor-homspaces}). 
Now $\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})$ should be the 
(non-unital) subalgebra of $\End_{\Uq}(\Tn{\bbin})$ 
of all matrices with only finitely many non-zero rows, i.e.
\[
\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})\cong \bigoplus_{i,i^{\prime}=0}^{\infty} \Hom_{\Uq}(\Tn{\bbi},\Tn{\bbi^{\prime}}).
\]
Similarly, of course, in the ``trivial'' case.



\begin{prop}\label{prop-isoofalg2}
We have
\begin{gather*}
\begin{aligned}
\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})&\cong\bigoplus_{i,i^{\prime}=0}^{\infty}\Hom_{\Uq}(\Tn{\bbi},\Tn{\bbi^{\prime}})\cong \Ai,
\\
\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin}^t)&\cong\bigoplus_{i,i^{\prime}=0}^{\infty}\Hom_{\Uq}(\Tn{\bbi}^t,\Tn{\bbi^{\prime}}^t)\cong \Att,
\end{aligned}
\end{gather*}
which are isomorphisms of $\bC$-algebras.\makeqed
\end{prop}



\begin{proof}
We only show the first isomorphism since the other is clear.
By using Corollary~\ref{cor-homspaces} and the definition 
of $\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})$ from above we 
see that, for each $f\in\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})$, 
there exists some $m\in\bN$ such that $f_{i^{\prime}i}=0$ for $i,i^{\prime}>m$.
Those matrices describe elements in $\End_{\Uq}(\Tn{\leq\bbm})$ by ``forgetting'' the parts for $i,i^{\prime}>m$. Thus, we have
\[
\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})\cong \varinjlim \End_{\Uq}(\Tn{\leq\bbm}).
\]
By Proposition~\ref{prop-isoofalg1} we see that this implies
\[
\End^{\mathrm{fs}}_{\Uq}(\Tn{\bbin})\cong \varinjlim \Am\cong\Ai.
\]
This finishes the proof.
\end{proof}



We are now able to relate 
$\T_{\lambda}(\leq \bbm)$ to 
$\pModAm$ and thus, $\T_{\lambda}$ to $\pModAi$. 
We define
\begin{gather*}
\bV\colon\T_{\lambda}(\leq \bbm)\to\ModAm, \bV(M)=\Hom_{\Uq}(\Tn{\leq\bbm},M),
\\
\bVi\colon\T_{\lambda}\to\ModAi, \bVi(M)=\Hom^{\mathrm{fs}}_{\Uq}(\Tn{\bbin},M)\cong \bigoplus_{i=0}^{\infty}\Hom_{\Uq}(\Tn{\bbi},M),
\end{gather*}
for $M$ in either $\Ob(\T(\leq \bbm))$ or $\Ob(\T_{\lambda})$ 
respectively where the isomorphism follows from 
Proposition~\ref{prop-isoofalg2}. Similarly for 
the walls $\mu$ where we indicate the functors 
$\bV^t$ and $\bVi^t$ (and everything else) with 
superscripts $t$. We note that the hom-spaces above 
are right $\Am$-modules (or $\Ai$, $\At$ or $\Ait$-modules) by \textit{pre}-composition.



Note that $\Theta_s,\Theta_t\in\Ob(\End(\T_{\lambda}))$ 
from Definition~\ref{defn-trans} clearly descent 
to $\T_{\lambda}(\leq\bbm)$ for all $m\in\bN$. 
We denote these restrictions, by abuse of notation, 
also by $\Theta_s,\Theta_t$. Furthermore, 
recall the notation $\Theta_{s\text{ or }t}^i$ for $i\in\bZ_{>0}$ 
which are defined via ($p_{\bbi}$ projects to the $\Tn{\bbi}$-part)
\[
\Theta_{s\text{ or }t}^i=\begin{cases}p_{\bbi}\circ\Theta_{s}, &\text{if }i\text{ is even },\\
p_{\bbi}\circ\Theta_{t}, &\text{if }i\text{ is odd }.
\end{cases}
\]
We use the 
same conventions and notations in the finite case by killing everything above $m$.



Similarly: the functors $\mathcal T_{\lambda}^{\mu}$ 
and $\mathcal T^{\lambda}_{\mu}$ from Definition~\ref{defn-onout} also 
descent to the finite case where we again denote them by the same symbols.



We consider the right side for the tilting embedding theorem 
(finite and infinite) as ungraded modules/functors. 
Moreover $\pMod$ always denotes categories of projective modules.



\begin{thm}(\textbf{Tilting embedding theorem - finite version})\label{thm-struktursatz1}
We have the following.
\begin{itemize}
\item[(a)] The functor $\bV$ is fully faithful.
\item[(b)] The functor $\bV$ sends objects 
$M\in\Ob(\T_{\lambda}(\leq\bbm))$ to projective 
$\Am$-modules and is an equivalence  between $\T_{\lambda}(\leq\bbm)$ and $\pModAm$.
\item[(c)] We have the following commuting diagram.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\leq\bbm) \ar[r]^/-0.1em/{\bV} \ar[d]_{\Theta^i_{s\text{ or }t}}    &   \pModAm \ar[d]^{\mathcal U_{i}} \\
      \T_{\lambda}(\leq\bbm) \ar[r]_/-0.1em/{\bV}             &   \pModAm.  
  }
\end{xy}
\]
\item[(d)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\leq\bbm) \ar[r]^/-0.1em/{\bV} \ar[d]_{\Theta_s}    &   \pModAm \ar[d]^{\mathcal U_{\mathrm{even}}}  \\
      \T_{\lambda}(\leq\bbm) \ar[r]_/-0.1em/{\bV}             &   \pModAm   
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\leq\bbm) \ar[r]^/-0.1em/{\bV} \ar[d]_{\Theta_t}    &   \pModAm \ar[d]^{\mathcal U_{\mathrm{odd}}}  \\
      \T_{\lambda}(\leq\bbm) \ar[r]_/-0.1em/{\bV}             &   \pModAm.  
  }
\end{xy}
\]
\item[(e)] The same as in (a)+(b) works for the walls $\mu$ as well by using $\bV^t$.
\item[(f)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\leq\bbm) \ar[r]^/-0.1em/{\bV} \ar[d]_{\mathcal{T}_{\lambda}^{-1}}    &   \pModAm \ar[d]^{\mathcal U_{\mathrm{even}}^t}  \\
      \T_{-1}(\leq\bbm)\ar[r]_/-0.1em/{\bV^t}             &   \pModAt  
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\leq\bbm) \ar[r]^/-0.1em/{\bV} \ar[d]_{\mathcal{T}_{\lambda}^{l-1}}    &   \pModAm \ar[d]^{\mathcal U_{\mathrm{odd}}^t}  \\
      \T_{l-1}(\leq\bbm)\ar[r]_/-0.1em/{\bV^t}             &   \pModAt.  
  }
\end{xy}
\]
\item[(g)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{-1}(\leq\bbm) \ar[r]^/-0.1em/{\bV^t} \ar[d]_{\mathcal{T}^{\lambda}_{-1}}    &   \pModAt \ar[d]^{\mathcal U^{\mathrm{even}}_t}  \\
      \T_{\lambda}(\leq\bbm) \ar[r]_/-0.1em/{\bV}             &   \pModAm  
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{l-1}(\leq\bbm) \ar[r]^/-0.1em/{\bV^t} \ar[d]_{\mathcal{T}^{\lambda}_{l-1}}    &   \pModAt \ar[d]^{\mathcal U^{\mathrm{odd}}_t}  \\
      \T_{\lambda}(\leq\bbm) \ar[r]_/-0.1em/{\bV}             &   \pModAm.  
  }
\end{xy}
\hspace{1.95cm}
\raisebox{-1.55cm}{\makeqed}
\hspace{-1.95cm} 
\]
\end{itemize}
\end{thm}



\begin{proof}
We are careless with the indices in the proof 
and hope that this does not cause confusion. All 
appearing indices should be such that everything 
below $0$ or above $m$ is defined to be zero.



\textbf{(a).} By Proposition~\ref{prop-tilt} part 
(c) and Lemma~\ref{lem-tiltcat} part (a) it is enough 
to verify the statement for $M=\Tn\bbi$ for $i=0,\dots,m$. 
Moreover, by using Corollary~\ref{cor-homspaces} together 
with the discussion in Subsection~\ref{sub-ammod}, we 
get isomorphisms $\bV(\Tn\bbi)=\Hom_{\Uq}(\Tn{\leq \bbm},\Tn\bbi)\cong {}_iP$. 
Thus, $\bV$ is fully faithful.



\textbf{(b).} From (a) by using the discussion in 
Subsection~\ref{sub-ammod}.



\textbf{(c).} This follows by combining 
$\bV(\Tn\bbi)=\Hom_{\Uq}(\Tn{\leq \bbm},\Tn\bbi)\cong {}_iP$ 
with~\eqref{eq-tlcat} and part (c) of Proposition~\ref{prop-functors}.



\textbf{(d).} This follows directly from (c) 
and the definition of $\mathcal U_{\mathrm{even}}$ and $\mathcal U_{\mathrm{odd}}$. 



\textbf{(e).} The ``trivial'' cases are clear.



\textbf{(f).} We do the left case here. Note that $\bV(\Tn{\bbi})\cong {}_iP$. 
Thus, using~\eqref{eq-ufunctors}, we see that 
$\mathcal U^{\mathrm{even}}_t\bV^t$ sends 
$\Tn{\bbi}$ to $\bC\bbi\oplus\bC\varepsilon_i$ 
for even $i$ and $\bC u_{i-1}\oplus \bC d_{i+1}$ for odd $i$.
This, by the discussion in Subsection~\ref{sub-endo}, 
is isomorphic as right $\At$-modules to 
$\bC\bbi\oplus\bC\bbi$ and $\bC\bbid\oplus\bC\bbiu$ 
respectively. In addition, $\mathcal T^{-1}_{\lambda}$ 
sends $\Tn{\bbi}$ to $\Tn{\mu_i}\oplus\Tn{\mu_i}$ 
(for $i$ even) or to $\Tn{\mu_{i-1}}\oplus\Tn{\mu_{i+1}}$ 
(for $i$ odd). These are then sent to $\bC\bbi\oplus\bC\bbi$ (for $i$ even) 
respectively $\bC\bbid\oplus\bC\bbiu$ (for $i$ odd).



\textbf{(g)}: Analogously to (f).
\end{proof}



\begin{thm}(\textbf{Tilting embedding theorem - infinite version})\label{thm-struktursatz2}
We have the following.
\begin{itemize}
\item[(a)] The functor $\bVi$ is fully faithful.
\item[(b)] The functor $\bVi$ sends objects $M\in\Ob(\T)$ to projective $\Ai$-modules and is an equivalence  between $\T_{\lambda}$ and $\pModAi$.
\item[(c)] We have the following commuting diagram.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda} \ar[r]^/-0.75em/{\bVi} \ar[d]_{\Theta^i_{s\text{ or }t}}    &   \pModAi \ar[d]^{\mathcal U^{\infty}_{i}}  \\
      \T_{\lambda} \ar[r]_/-0.75em/{\bVi}             &   \pModAi.   
  }
\end{xy}
\]
\item[(d)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda} \ar[r]^/-0.75em/{\bVi} \ar[d]_{\Theta_s}    &   \pModAi \ar[d]^{\mathcal U^{\infty}_{\mathrm{even}}}  \\
      \T_{\lambda} \ar[r]_/-0.75em/{\bVi}             &   \pModAi   
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{\lambda} \ar[r]^/-0.75em/{\bVi} \ar[d]_{\Theta_t}    &   \pModAi \ar[d]^{\mathcal U^{\infty}_{\mathrm{odd}}}  \\
      \T_{\lambda} \ar[r]_/-0.75em/{\bVi}             &   \pModAi.  
  }
\end{xy}
\]
\item[(e)] The same as in (a)+(b) works for the walls $\mu$ as well by using $\bVi^t$.
\item[(f)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\bbin) \ar[r]^/-0.1em/{\bVi} \ar[d]_{\mathcal{T}_{\lambda}^{-1}}    &   \pModAi \ar[d]^{\mathcal U_{\mathrm{even}}^t}  \\
      \T_{-1}(\bbin) \ar[r]_/-0.1em/{\bVi^t}             &   \pModAtt
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{\lambda}(\bbin) \ar[r]^/-0.1em/{\bVi} \ar[d]_{\mathcal{T}_{\lambda}^{l-1}}    &   \pModAi \ar[d]^{\mathcal U_{\mathrm{odd}}^t}  \\
      \T_{l-1}(\bbin) \ar[r]_/-0.1em/{\bVi^t}             &   \pModAtt.  
  }
\end{xy}
\]
\item[(g)] We have the following commuting diagrams.
\[
\begin{xy}
  \xymatrix{
      \T_{-1}(\bbin) \ar[r]^/-0.1em/{\bVi^t} \ar[d]_{\mathcal{T}^{\lambda}_{-1}}    &   \pModAtt \ar[d]^{\mathcal U^{\mathrm{even}}_t}  \\
      \T_{\lambda}(\bbin) \ar[r]_/-0.1em/{\bVi}             &   \pModAi  
  }
\end{xy}
\quad\raisebox{-0.75cm}{\text{and}}\quad
\begin{xy}
  \xymatrix{
      \T_{l-1}(\bbin) \ar[r]^/-0.1em/{\bVi^t} \ar[d]_{\mathcal{T}^{\lambda}_{l-1}}    &   \pModAtt \ar[d]^{\mathcal U^{\mathrm{odd}}_t}  \\
      \T_{\lambda}(\bbin) \ar[r]_/-0.1em/{\bVi}             &   \pModAi.  
  }
\end{xy}
\hspace{2.3cm}
\raisebox{-1.55cm}{\makeqed}
\hspace{-2.3cm}
\]
\end{itemize}
\end{thm}


\begin{proof}
The proofs of (a)-(g) is similar to 
the proofs given in Theorem~\ref{thm-struktursatz1} 
by using arguments as in Proposition~\ref{prop-isoofalg2}. We leave it to the reader.
\end{proof}



\begin{rem}\label{rem-othermaps}
We encourage the reader to work out the 
translations onto and out of the wall 
commuting diagrams similar to part (c) of the theorems above.
\end{rem}




We note the following corollary for completeness.
\begin{cor}\label{cor-struktursatz}
For all $\lambda,\lambda^{\prime}\in\mathcal A_0$ we have $\T_{\lambda}\cong \T_{\lambda^{\prime}}$. Thus,
\[
\T(\leq\bbm)\cong \bigoplus_{i=0}^{l-2}\pModAm\oplus\bigoplus_{i=0}^{1}\pModAt,
\quad\T\cong \bigoplus_{i=0}^{l-2}\pModAi\oplus\bigoplus_{i=0}^{1}\pModAtt,
\]
with semisimple categories $\pModAt$ and $\pModAtt$.\makeqed
\end{cor}



\begin{proof}
This follows from Lemma~\ref{lem-block} 
and Theorems~\ref{thm-struktursatz1} 
and~\ref{thm-struktursatz2} because the 
right-hand sides are always the same independent of $\lambda\in\mathcal A_0$.
\end{proof}



\begin{ex}(\textbf{How to compute the images of the translation functors on $\Uq$-morphisms})\label{ex-howtofunctor}
Combining the commuting diagrams of the 
Theorems~\ref{thm-struktursatz1} and~\ref{thm-struktursatz2} 
we obtain an explicit way to compute $\Theta_s$ and $\Theta_t$ 
not just on the $\Tn{\bbi}$'s (as we already know by part (c) 
of Proposition~\ref{prop-functors}), but also 
on the $\Uq$-intertwiners in $\Hom_{\Uq}(\Tn{\bbi},\Tn{\bbi^{\prime}})$.



This follows by using~\eqref{eq-homps} together 
with $\Theta_s\leftrightsquigarrow \mathcal U_{\mathrm{even}}$ 
and $\Theta_t\leftrightsquigarrow \mathcal U_{\mathrm{odd}}$. 
For example, given $u_0\colon\Tn{\bbz}\to\Tn{\bbo}$, we can 
compute $\Theta_t(u_0)$ as follows. First note that 
$\bVi\Theta_t(\Tn{\bbz})\cong {}_1P$ and $\bVi\Theta_t(\Tn{\bbo})\cong {}_1P\oplus {}_1P$ by~\eqref{eq-tlcat} and Theorem~\ref{thm-struktursatz2}. By using~\eqref{eq-homps} 
we see
\[
\Theta_t(u_0)=\begin{pmatrix}
 0 \\
 \mathrm{id}
\end{pmatrix}\colon \Tn{\bbo}\to\Tn{\bbo}\oplus \Tn{\bbo}.
\]
We see that this is actually
\[
\Theta_t(u_0)=\begin{pmatrix}
 0 \\
 \mathrm{id} 
\end{pmatrix}\colon \Tn{\bbo}\to\Tn{\bbo}\langle-1\rangle\oplus \Tn{\bbo}\langle+1\rangle,
\]
by using the results we are going to explain in Subsection~\ref{sub-grad}. Indeed, 
the grading is very helpful to calculate the images of the $\Uq$-interwiners, e.g. 
$\Theta_t(u_0)$ can only be zero on the first component, since we will show 
that there will not be  suitable $\Uq$-intertwiners lowering the degree.
\end{ex}



\begin{rem}\label{rem-cato}
Let $\mathfrak{g}=\mathfrak{sl}_{m+1}$ and 
$\mathfrak{p}=\mathfrak{p}_1$ be a maximal 
parabolic subalgebra for $S_1\times S_{m-1}$ 
(for a definition see for example~\cite[Chapter~9]{hum}). 
Denote by $\mathcal O^{\mathfrak{p}}$ the corresponding 
parabolic category $\mathcal O$ (for a definition and 
some properties see e.g.~\cite[Section~9.3]{hum}). Moreover, 
denote by $\mathcal O^{\mathfrak{p}}_0$ the principle block. 
As Khovanov and Seidel show in~\cite[Proposition~2.9]{ks1} 
there is an equivalence of categories 
$\mathcal O^{\mathfrak{p}}_0\cong \ModAm$. 
Thus, by Theorems~\ref{thm-struktursatz1} 
and~\ref{thm-struktursatz2}, we see that 
$\T_{\lambda}$ governs $\mathcal O^{\mathfrak{p}}_0$ for all $m$.
Similarly for the projective endofunctors: 
as explained in~\cite[below Proposition~2.9]{ks1}, 
the functors $\mathcal U_i$ correspond to the translation 
through the $i$-th wall (note that, under the equivalence 
above, the $\mathfrak{sl}_{m+1}$ has Weyl group generators 
$s_1,\dots,s_m$ and therefore translation functors indexed 
by $i=1,\dots,m$). Moreover, $\mathcal U_i^t$ corresponds 
to the translation onto and $\mathcal U^i_t$ corresponds to 
the translation out off the wall functors.
Hence, by Theorems~\ref{thm-struktursatz1} 
and~\ref{thm-struktursatz2}, we can say 
that these are governed by the combinatorics 
of $\mathcal T_{\lambda}^{\mu}$, 
$\mathcal T^{\lambda}_{\mu}$ 
and $\Theta^{\lambda}_{s\text{ or }t}$ from our tilting case.



Another point is, as Khovanov and Seidel explain 
after~\cite[Proposition~2.9]{ks1}, that the path length grading gives rise 
to a \textit{Koszul grading} in the sense of~\cite{bgs} on 
the $\Am$'s, see also~\cite[Example~1.1]{st1}. 
The same holds for $\Ai$. This can either be 
seen ``by hand'' or by using a more general 
theory for (quotients of) not necessary 
finite quiver algebras that can be found for example in~\cite{mos}.
\end{rem}




\begin{rem}\label{rem-webalg}
Khovanov and Seidel's quiver is also 
related to Khovanov's arc algebra 
$H^m$ (for $m$ even) that he introduced 
in~\cite{kh4} to give an algebraic interpretation 
of Khovanov homology. The arc algebra categorifies the 
invariant tensors of $V^{\otimes m}$ where $V$ is the 
two dimensional vector representation of $\Uv$.
In addition, together with Chen he extended in~\cite{chkh} 
this categorification to the full tensor 
product $V^{\otimes m}$ by defining a certain 
subquotient $\prod_k A^{k,m-k}$ (this quotient can 
be seen as the quasi-hereditary cover of $H^m$). 
All of these have a topological interpretation 
as algebras consisting of cobordisms, 
see e.g.~\cite[Section~2]{chkh}, and they are 
graded by \textit{the Euler characteristic} of these cobordisms.
As explained in~\cite[Section~3]{chkh}, 
the $A^{1,m-1}$-part of this subquotient is graded 
isomorphic to $\Am$. Thus, we see that $\T$ governs $A^{1,m-1}$ for all $m$.
Moreover, this gives a hint for a  
generalization of our work: we think 
that analogs of the Theorems~\ref{thm-struktursatz1} and~\ref{thm-struktursatz2} 
can be proven for certain subquotients of the $\mathfrak{sl}_n$ 
generalizations of $H^m$ studied in e.g.~\cite{mack1},~\cite{mpt},~\cite{tub3} or~\cite{tub4}.
\end{rem}
