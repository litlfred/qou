---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-009-3-the-khovanov-seidel-quiver-algebra-and-grading
section_title: "The Khovanov-Seidel quiver algebra and gradings"
section_number: 3
pages: 17-19
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.981
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
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
