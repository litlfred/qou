---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-004-6-branching-rules-and-characters
section_title: "Branching rules and characters"
section_number: 6
pages: 36-46
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.961
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an oriented link, in the same"
---
\label{schars}

We continue with the setup of the previous section.
In this section, we introduce a biadjoint pair of endofunctors
$E$ and $F$ of $\Mod OS$, which lift the endofunctors $\up \otimes ?$ and $\down
\otimes ?$ of $\OS(z,t)$.
We will use the Jucys-Murphy elements from section \ref{aos}
to decompose these endofunctors
into direct sums of refined functors $E_i$ and
$F_i$, which we study by comparing them 
to some well-known induction and restriction functors on $\Mod OS^\circ$.

To start with, let us recall some standard facts about induction and
restriction for the Iwahori-Hecke algebra $H_r$.
Let 
\begin{equation}
\ind_{r-1}^{r} 
:\Mod H_{r-1} \rightarrow \Mod H_{r},
\qquad
\res_{r-1}^{r} :\Mod H_{r} \rightarrow \Mod H_{r-1}
\end{equation} be the usual 
induction and restriction functors with respect to the natural embedding $H_{r-1}
\hookrightarrow H_{r}, S_i \mapsto S_i$.
So $\ind_{r-1}^{r}$ is defined by tensoring over $H_{r-1}$ with $H_{r}$
viewed as an $(H_{r-1}, H_{r})$-bimodule and 
$\res_{r-1}^{r}$ is defined by tensoring over $H_{r}$ with $H_{r}$
viewed as an $(H_{r}, H_{r-1})$-bimodule;
equivalently, $\res_{r-1}^{r}$ is the functor $\Hom_{H_{r}}(H_{r}, ?)$.
Adjointness of tensor and hom implies that
induction is left adjoint to the restriction functor
$\res_{r-1}^{r}$. It is also right adjoint; cf. \cite[Theorem 2.6]{DJ}.
The {\em Jucys-Murphy element} 
\begin{equation}\label{JMstupid}
\JM_r := S_{r-1} \cdots S_2 S_1 S_1 S_2 \cdots
S_{r-1} \in H_{r}
\end{equation} 
centralizes $H_{r-1}$, so left multiplication
by it defines an
endomorphism of the $(H_{r-1},
H_{r})$-bimodule $H_{r}$. For any $i \in \k$, let $i\text{-\!}\ind_{r-1}^{r}$
be the {\em $i$-induction functor} defined by tensoring with the
summand of this bimodule that arises as the generalized $i$-eigenspace
of this endomorphism. Let $i\text{-\!}\res_{r-1}^{r}$ be the biadjoint
{\em $i$-restriction functor}; explicitly, $i\text{-\!}\res_{r-1}^{r} M$
may be realized as the generalized $i$-eigenspace of $\JM_r$ on $\res^{r}_{r-1} M$. 

The following ``classical'' branching rules\footnote{Probably the best way to prove them
is by applying the ``Schur functor'' to an analogous result for quantum
$GL_n$.} describe the effect of
these functors on the Specht module $\SS_\lambda$. 
In formulating the result, we identify partition $\lambda$ with
its 
{\em Young diagram}, that is, the set
$\{(i,j)\:|\:i \geq 1, 1 \leq j \leq \lambda_r\}$, and
define the {\em content} of the {\em node} $\mathsf{A} = (i,j) \in \NN\times\NN$
from $\cont(\mathsf{A}) := q^{2(j-i)} \in \k$.
For example, here is the Young diagram $\lambda = (5,3,2)$ with
its nodes labeled by their contents:
$$
\diagram{$ 1$&$ q^2$&$
  q^4$&$ q^6$&$ q^8$\cr $
  q^{-2}$&$ 1$&$q^2$\cr
  $ q^{-4}$ & $ q^{-2}$ \cr}.
$$
Let $I_1$ be the set of all
possible contents of nodes of partitions. More generally, for any $c
\in \k^\times$, we let
\begin{equation}\label{Ic}
I_c := \{c q^{2n}\:|\:n \in \ZZ\}  \subseteq \k^\times.
\end{equation}

\begin{lemma}\label{classical}
The following hold for each $i \in \k^\times$:
\begin{enumerate}
\item For $\lambda \vdash (r-1)$, the $H_{r}$-module $i\text{-\!}\ind_{r-1}^{r} \SS_\lambda$ has a
multiplicity-free filtration
with sections $\SS_\mu$ for $\mu \vdash r$
obtained by adding a node
of content $i$ to the Young diagram of $\la$.
\item For $\lambda \vdash r$,
the $H_{r}$-module $i\text{-\!}\res^{r}_{r-1} \SS_\lambda$ has 
multiplicity-free filtration
with sections 
$\cong \SS_{\mu}$ for $\mu \vdash (r-1)$
obtained by removing a node of content $i$ from the Young diagram of $\la$.
\end{enumerate}
In both cases, the filtration should be ordered according to the
usual dominance ordering on the partitions labelling the sections,
most dominant at the bottom.
Hence:
\begin{equation}\label{decomp}
\ind_{r-1}^r = \bigoplus_{i \in I_1} 
i\text{-\!}\ind_{r-1}^r,
\qquad
\res_{r-1}^r = \bigoplus_{i \in I_1} i\text{-\!}\res_{r-1}^r.
\end{equation}
\end{lemma}

The results just explained extend immediately to
$H_{r,s} = H_r \otimes H_s$.
For these algebras, there are two commuting $i$-induction functors
$i\text{-\!}\ind_{r-1,s}^{r,s}$ and 
$i\text{-\!}\ind_{r,s-1}^{r,s}$, defined
by tensoring with the bimodules that arise by taking the generalized
$i$-eigenspaces of 
the endomorphisms of 
$H_{r,s}$ defined by left multiplication by $\JM_r \otimes
1$ or $1 \otimes \JM_s$, respectively.
The biadjoint $i$-restriction functors are denoted $i\text{-\!}\res^{r,s}_{r-1,s}$
 and $i\text{-\!}\res^{r,s}_{r,s-1}$.
Lemma~\ref{classical} extends in an obvious way to 
describe
the effect of these functors on the modules
$\SS_{\la^\up} \boxtimes \SS_{\la^\down}$.

The next step is to use the Morita equivalences from
Lemma~\ref{cartanlem} to transport the branching rules for $H_{r,s}$ just
described to the
algebra $OS^\circ$.
Let 
\begin{align}
\i^\circ_\down:&OS^\circ \rightarrow OS^\circ, \qquad f \mapsto \down\otimes f,\\
\i^\circ_\up:&OS^\circ\rightarrow OS^\circ, \qquad 
f \mapsto \up \otimes f
\end{align} 
be the algebra homomorphisms associated to
the functors $\down \otimes-:\OS^\circ(z,t) \rightarrow \OS^\circ(z,t)$ and $\up\otimes-:\OS^\circ(z,t)
\rightarrow \OS^\circ(z,t)$.
These are not {\em locally unital} algebra homomorphisms:
they send the idempotent $1_\a$ to $1_{\up \a}$ and to $1_{\down \a}$, respectively.
Then let
\begin{align}\label{dib1}
{_\up} OS^\circ &:= \bigoplus_{\a,\b \in \words} 1_{\up \a} OS^\circ 1_\b,
&
OS^\circ_\up &:= \bigoplus_{\a,\b \in \words} 1_\a OS^\circ 1_{\up \b},\\
{_\down} OS^\circ &:= \bigoplus_{\a,\b \in \words} 1_{\down \a} OS^\circ 1_\b,&
OS^\circ_\down &:= \bigoplus_{\a,\b \in \words} 1_\a OS^\circ 1_{\down \b},\label{dib2}
\end{align}
which we view as $(OS^\circ, OS^\circ)$-bimodules
with left and right actions of $a,b \in OS^\circ$ on $f$ defined by $a\cdot
f\cdot b :=
\i^\circ_\up(a) f b,
a f \i^\circ_\up(b), \i^\circ_\down(a) f b$ and $a f \i^\circ_\down(b)$,
respectively.
Tensoring with these bimodules give us four endofunctors of $\Mod{OS^\circ}$:
\begin{align}\label{fan1}
E^\up := ? \otimes_{OS^\circ} {_\up} OS^\circ&:\Mod{OS^\circ} \rightarrow
\Mod{OS^\circ},\\
F^\up := ?\otimes_{OS^\circ} OS^\circ_\up&:\Mod{OS^\circ}\rightarrow \Mod{OS^\circ},\\
F^\down := ? \otimes_{OS^\circ} {_\down} OS^\circ&:\Mod{OS^\circ} \rightarrow
\Mod{OS^\circ},\\
E^\down := ?\otimes_{OS^\circ} OS^\circ_\down&:\Mod{OS^\circ}\rightarrow
\Mod{OS^\circ}.\label{fan4}
\end{align}
The functors $E^\up$ and $F^\down$ 
send $OS^\circ_{r,s}$-modules to $OS^\circ_{r+1,s}$- and
$OS^\circ_{r,s+1}$-modules, respectively; they will be called {\em
  induction functors}.
The functors $F^\up$ and $E^\down$
send $OS^\circ_{r,s}$-modules to $OS^\circ_{r-1,s}$- and
$OS^\circ_{r,s-1}$-modules, respectively; they will be called {\em
  restriction functors}.
This terminology is justified by the following lemma.

\begin{lemma}\label{fan}
The following diagrams commute up to natural isomorphisms:
\begin{align*}
&\begin{CD}
\Mod H_{r+1,s} &@>\Upsilon_{r+1,s}>>&\Mod OS_{r+1,s}^\circ\\
@AA\ind_{r,s}^{r+1,s}A \searrow^{\!\!\!\alpha}&@AAE^\up A\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}
&\qquad
&\begin{CD}
\Mod H_{r+1,s} &@>\Upsilon_{r+1,s}>>&\Mod OS_{r+1,s}^\circ\\
@VV\res_{r,s}^{r+1,s}V ^{\beta\!\!\!\!\!\!}\nearrow&@VVF^\up V\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}\\
&\begin{CD}
\Mod H_{r,s+1} &@>\Upsilon_{r,s+1}>>&\Mod OS_{r,s+1}^\circ\\
@AA\ind_{r,s}^{r,s+1}A \searrow^{\!\!\!\gamma}&@AAF^\down A\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}
&\qquad
&\begin{CD}
\Mod H_{r,s+1} &@>\Upsilon_{r,s+1}>>&\Mod OS_{r,s+1}^\circ\\
@VV\res_{r,s}^{r,s+1}V ^{\delta\!\!\!\!\!}\nearrow&@VVE^\down V\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ.
\end{CD}
\end{align*}
Hence, the functors $E^\up$ and $F^\up$ are biadjoint, as are the
functors
$E^\down$ and $F^\down$.
\end{lemma}

\begin{proof}
First we construct the 
isomorphism $\alpha:\Upsilon_{r+1,s} \circ \ind_{r,s}^{r+1,s}
\stackrel{\sim}{\rightarrow} E^\up \circ \Upsilon_{r,s}$.
The northwest functor is defined by tensoring over $H_{r,s}$
with the $(H_{r,s},
OS^\circ)$-bimodule
$$
H_{r+1,s} \otimes_{H_{r+1,s}} 1_{\down^s \up^{r+1}} OS^\circ
\cong 1_{ \down^s\up^{r+1}} OS^\circ.
$$
The southeast functor is defined by tensoring with
$$
1_{\down^s \up^r} OS^\circ \otimes_{OS^\circ}
{_\up} OS^\circ
\cong
1_{\up \down^s \up^r} OS^\circ.
$$ 
The following gives an isomorphism between
these two bimodules:
\begin{align*}
1_{\down^s \up^{r+1}} OS^\circ
&\stackrel{\sim}{\rightarrow}
1_{\up\down^s\up^r} OS^\circ,
\\
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-,thick,double,darkblue] (0,.12) to (0,-.3);
\draw[<-,ultra thick,darkblue] (-.12,.47) to (-.32,1.09);
\draw[->,thick,darkblue] (0,.47) to (0,1.09);
\draw[->, ultra thick,darkblue] (.12,.47) to (.36,1.09);
\node at (0,-.42) {$\a$};
\node at (-.31,1.2) {$\scriptstyle s$};
\node at (.35,1.2) {$\scriptstyle r$};
\end{tikzpicture}
}
&\mapsto 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=60,in=-50] (-.32,1.09);
\draw[-,line width=3pt,white] (-.12,.47) to [out=100,in=-140] (0.05,1.09);
\draw[<-,ultra thick,darkblue] (-.12,.47) to [out=100,in=-140] (0.05,1.09);
\draw[->,ultra thick,darkblue] (.12,.47) to (.36,1.09);
\node at (0,-.42) {$\a$};
\node at (0.05,1.2) {$\scriptstyle s$};
\node at (.36,1.2) {$\scriptstyle r$};
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\end{tikzpicture}
}
\end{align*}
for any $f \in 1_{\down^s\up^{r+1}} OS^\circ 1_\a$.
This establishes the existence of $\alpha$.

To deduce the existence of $\beta$,
we claim that $F^\up$ is right adjoint to $E^\up$.
To see this, $F^\up M = M \otimes_{OS^\circ} OS^\circ_\up
= \bigoplus_{\a \in \words} M 1_{\up \a}
\cong 
\bigoplus_{\a \in \words} \Hom_{OS^\circ}(1_{\up \a} OS^\circ, M)
$. So, by adjointness of tensor and hom, $F^\up$ is right adjoint
to
$\bigoplus_{\a \in \words} ? \otimes_{OS^\circ} 1_{\up \a} OS^\circ = ?
\otimes_{OS^\circ} {_\up} OS^\circ = E^\up$.
Since $\res^{r+1,s}_{r,s}$ is right adjoint to $\ind^{r+1,s}_{r,s}$,
and the horizontal functors in our diagrams are equivalences of
categories, we can now deduce the existence of the desired isomorphism $\beta$ using the previous
paragraph and unicity of right adjoints.

The construction of $\gamma$ is very similar to that of $\alpha$. In
fact, it is even easier since both of the $(H_{r,s}, OS^\circ)$-bimodules
being considered turn out to be the same bimodule
$1_{\down^{s+1}\up^r} OS^\circ$, so we can take $\gamma$ to be induced by
the identity map.
Then we get $\delta$ from $\gamma$ as in the previous paragraph.
\end{proof}

Now we need versions of Jucys-Murphy elements for $OS^\circ$, which
extend the Jucys-Murphy elements of $H_{r,s}$.
For $\varnothing \neq \b \in \words$, define $X^\circ(\b) \in 1_\b OS^\circ 1_\b$ by setting
$X^\circ(\up) := 1_\up$,
$X^\circ(\down) := t^{-2} 1_\down$,
and then recursively defining
\begin{align}\label{chile2}
X^\circ(\up \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,line width=4pt,white] (-.42,.27) to [out=90,in=-120] (-0.05,.9); 
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,line width=4pt,white] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.16,.3) {$\scriptstyle X^\circ(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\node at (0.25,-.43) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:,
&
X^\circ(\up \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,line width=4pt,white] (-.42,.27) to [out=90,in=-120] (-0.05,.9); 
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[-,line width=4pt,white] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.16,.3) {$\scriptstyle X^\circ(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.43) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:,\\
X^\circ(\down \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,line width=4pt,white] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[-,line width=4pt,white] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.16,.3) {$\scriptstyle X^\circ(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.43) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:,
&
X^\circ(\down \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,line width=4pt,white] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,line width=4pt,white] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.16,.3) {$\scriptstyle X^\circ(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.43) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:,\label{chile5}
\end{align}
for any $\a \in \words$; cf. (\ref{JMa})--(\ref{JMb}).

Let ${_{\up}}X^\circ:{_\up} OS^\circ \rightarrow {_\up} OS^\circ$
and $X^\circ_{\up}:OS^\circ_\up \rightarrow OS^\circ_\up$
be the linear endomorphisms defined on $1_{\up \a} OS^\circ$ 
or
$OS^\circ 1_{\up \a}$ 
by
left or right multiplication by $X^\circ(\up \a)$, respectively.
Similarly, replacing $\up$ by $\down$ everywhere, we define
linear endomorphisms 
${_{\down}}X^\circ$ and $X^\circ_{\down}$ of ${_\down} OS^\circ$ and $OS^\circ_\down$.

\begin{lemma}\label{chile0}
All of the linear endomorphisms ${_{\up}}X^\circ, X^\circ_{\up}, {_{\down}}X^\circ$ and $X^\circ_{\down}$
are $(OS^\circ, OS^\circ)$-bimodule endomorphisms.
\end{lemma}

\begin{proof}
We just explain the argument for ${_{\up}}X^\circ$. It is obvious that this
defines a right $OS^\circ$-module homomorphism. To see that it also
commutes with the left action of $OS^\circ$, it suffices to check that it
commutes with left multiplication by
any element of $OS^\circ$ defined by
a crossing of a neighboring pairs of strands (excluding the leftmost strand).
This quickly reduces by induction to checking the following four
identities:
\begin{align*}
X^\circ(\up\up\up) \circ \:
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[->,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,->] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
&= 
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[->,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,->] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
\circ X^\circ(\up\up\up),
&
X^\circ(\up\down\down) \circ \:
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[<-,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,<-] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
&= 
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[<-,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,<-] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
\circ X^\circ(\up\down\down),\\
X^\circ(\up\down\up) \circ \:
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[thick,darkblue,->] (-0.28,-.3) to (0.28,.4);
	\draw[-,line width=4pt,white] (0.28,-.3) to (-0.28,.4);
	\draw[<-,thick,darkblue] (0.28,-.3) to (-0.28,.4);
\end{tikzpicture}
}
&= 
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[thick,darkblue,->] (-0.28,-.3) to (0.28,.4);
	\draw[-,line width=4pt,white] (0.28,-.3) to (-0.28,.4);
	\draw[<-,thick,darkblue] (0.28,-.3) to (-0.28,.4);
\end{tikzpicture}
}
\circ X^\circ(\up\up\down),
&
X^\circ(\up\up\down) \circ \:
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[->,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,<-] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
&= 
\mathord{
\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (-0.6,-.3) to (-0.6,.4);
	\draw[->,thick,darkblue] (0.28,-.3) to (-0.28,.4);
 	\draw[line width=4pt,white,-] (-0.28,-.3) to (0.28,.4);
	\draw[thick,darkblue,<-] (-0.28,-.3) to (0.28,.4);
\end{tikzpicture}
}
\circ X^\circ(\up\down\up).
\end{align*}
These are all straightforward on drawing the diagrams for these $X^\circ$'s explicity.
\end{proof}

For $i \in \k^\times$,
let  $E_i^\up$ be the subfunctor of $E$ that is defined by tensoring
with the bimodule that is the generalized $i$-eigenspace of
${_{\up}}X^\circ:{_\up} OS^\circ \rightarrow {_\up} OS^\circ$.
Define $F_i^\up, F_i^\down$ and $E_i^\down$ similarly
using the endomorphisms $X^\circ_{\up}, {_{\down}}X^\circ$ and $X^\circ_{\down}$.

\begin{lemma}\label{fur}
The following diagrams commute up to natural isomorphisms:
\begin{align*}
&\begin{CD}
\Mod H_{r+1,s} &@>\Upsilon_{r+1,s}>>&\Mod OS_{r+1,s}^\circ\\
@AAi\text{-\!}\ind_{r,s}^{r+1,s}A &&@AAE_i^{\up} A\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}
&\qquad
&\begin{CD}
\Mod H_{r+1,s} &@>\Upsilon_{r+1,s}>>&\Mod OS_{r+1,s}^\circ\\
@VV i\text{-\!}\res_{r,s}^{r+1,s}V& &@VVF_i^{\up} V\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}\\
&\begin{CD}
\Mod H_{r,s+1} &@>\Upsilon_{r,s+1}>>&\Mod OS_{r,s+1}^\circ\\
@AA t^{-2}i^{-1}\text{-\!}\ind_{r,s}^{r,s+1}A &&@AAF_i^\down A\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ,
\end{CD}
&\qquad
&\begin{CD}
\Mod H_{r,s+1} &@>\Upsilon_{r,s+1}>>&\Mod OS_{r,s+1}^\circ\\
@VVt^{-2}i^{-1}\text{-\!}\res_{r,s}^{r,s+1}V &&@VVE_i^{\down} V\\
\Mod H_{r,s}&@>>\Upsilon_{r,s}>&\Mod OS_{r,s}^\circ.
\end{CD}
\end{align*}
Hence, the functors $E_i^{\up}$ and $F_i^{\up}$ are biadjoint, as are the
functors
$E_i^{\down}$ and $F_i^{\down}$.
Moreover:
\begin{equation}\label{decomp1}
E^\up = \bigoplus_{i \in I_1} E_i^\up,
\quad
F^\up = \bigoplus_{i \in I_1} F_i^\up,\quad
F^\down = \bigoplus_{i \in I_{t^{-2}}} F_i^\down,
\quad
E^\down = \bigoplus_{i \in I_{t^{-2}}} E_i^\down.
\end{equation}
\end{lemma}

\begin{proof}
Consider the first diagram.
In the proof of Lemma~\ref{fan}, the isomorphism of functors
$\alpha$ was induced by an explicit bimodule isomorphism
$1_{\down^s \up^{r+1}} OS^\circ \rightarrow 1_{\up \down^s \up^r} OS^\circ$.
This isomorphism intertwines the endomorphism of
$1_{\down^s \up^{r+1}} OS^\circ$ 
defined by left multiplication by $\i_{r+1,s}(\JM_{r+1} \otimes 1)$ with
the endomorphism of 
$1_{\up \down^s \up^r} OS^\circ$ defined by left multiplication by $X^\circ(\up
  \down^s \up^r)$; the appropriate picture needed to see this is as
follows:
$$
\mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,thick,darkblue] (0.6,-0.1) to[out=90,in=-90] (-.6,.5);
	\draw[-,line width=4pt,white] (-.3,-.5) to (-.3,.5);
	\draw[-,line width=4pt,white] (.4,-.5) to (.4,.5);
	\draw[<-,ultra thick,darkblue] (-.3,-.5) to (-.3,.5);
	\draw[->,ultra thick,darkblue] (.4,-.5) to (.4,.5);
	\draw[-,line width=4pt,white] (0,-.5) to[out=90,in=-90] (.6,-.1);
	\draw[-,thick,darkblue] (0,-.5) to[out=90,in=-90] (.6,-.1);
      \node at (-.3,.65) {$\scriptstyle s$};
      \node at (.4,.65) {$\scriptstyle r$};
\end{tikzpicture}
}
=
\mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,thick,darkblue] (0.6,0) to[out=90,in=-90] (-.5,.5);
	\draw[-,thick,darkblue] (0.1,-.5) to[out=80,in=-90] (-.6,-.1);
	\draw[-,thick,darkblue] (-.6,-.1) to[out=90,in=160] (.1,0);
	\draw[-,line width=4pt,white] (-.3,-.5) to (-.3,.5);
	\draw[-,line width=4pt,white] (.4,-.5) to (.4,.5);
	\draw[<-,ultra thick,darkblue] (-.3,-.5) to (-.3,.5);
	\draw[->,ultra thick,darkblue] (.4,-.5) to (.4,.5);
	\draw[-,line width=4pt,white] (.1,0) to[out=-20,in=-90] (.6,0);
	\draw[-,thick,darkblue] (.1,0) to[out=-20,in=-90] (.6,0);
      \node at (-.3,.65) {$\scriptstyle s$};
      \node at (.4,.65) {$\scriptstyle r$};
\end{tikzpicture}
}
\:.
$$
Consequently, this bimodule isomorphism restricts to an isomorphism
between the appropriate
summands of these bimodules, showing that the
restriction of $\alpha$ gives the desired natural transformation.

The second diagram follows from the first by unicity of adjoints on
observing that
$F_i^\up$ is right adjoint to $E_i^\up$, which follows from the explicit construction of the adjunction in the
second paragraph of the proof of Lemma~\ref{fan}.

The third diagram 
is established in the same way as the first diagram.
One needs to check that the endomorphisms of
$1_{\down^{s+1} \up^{r}} OS^\circ$ 
defined by left multiplication by $t^{-2} \i_{r,s+1}(1 \otimes
\JM_{s+1})^{-1}$
and by $X^\circ(\down^{s+1} \up^r)$ are equal, which is clear from the
following picture:
$$
t^{-2}\left(\mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,ultra thick,darkblue] (.8,-.5) to (.8,.5);
	\draw[-,thick,darkblue] (.6,0) to[out=90,in=-90] (0,.5);
	\draw[-,line width=4pt,white] (.3,-.5) to (.3,.5);
	\draw[<-,ultra thick,darkblue] (.3,-.5) to (.3,.5);
	\draw[-,line width=4pt,white] (0,-.5) to[out=90,in=-90] (.6,0);
	\draw[<-,thick,darkblue] (0,-.5) to[out=90,in=-90] (.6,0);
      \node at (.8,.65) {$\scriptstyle r$};
      \node at (.3,.65) {$\scriptstyle s$};
\end{tikzpicture}}\right)^{-1}=
 t^{-2} \mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,ultra thick,darkblue] (.7,-.5) to (.7,.5);
	\draw[-,line width=4pt,white] (0,-.5) to[out=90,in=-90] (.9,0);
	\draw[<-,thick,darkblue] (0,-.5) to[out=90,in=-90] (.9,0);
	\draw[-,line width=4pt,white] (.3,-.5) to (.3,.5);
	\draw[<-,ultra thick,darkblue] (.3,-.5) to (.3,.5);
	\draw[-,line width=4pt,white] (.9,0) to[out=90,in=-90] (0,.5);
	\draw[-,thick,darkblue] (.9,0) to[out=90,in=-90] (0,.5);
      \node at (.7,.65) {$\scriptstyle r$};
      \node at (.3,.65) {$\scriptstyle s$};
\end{tikzpicture}
}
\:.
$$

The fourth  diagram follows by adjunction as before.

The final statement of the lemma follows using these diagrams plus facts we have
already discussed about the induction and restriction functors for
$H_{r,s}$.
\end{proof}

We assemble the results so far into the following theorem, which describes
all of the branching rules for the functors
$E_i^\up$, $F_i^\up$,
$F_i^\down$
and $E_i^\down$.

\begin{lemma}\label{newfirst}
The following hold for $i \in \k^\times$
and $\LA \in \Par_{r,s}$.
\begin{enumerate}
\item $E_i^\up \SS(\LA)$ has a multiplicity-free filtration
with sections $\SS(\MU)$
for $\MU \in \Par_{r+1,s}$ obtained by adding a node of
content $i$ to the Young diagram of $\la^\up$.
\item $F_i^\up \SS(\LA)$ has a multiplicity-free filtration
with sections $\SS(\MU)$
for $\MU \in \Par_{r-1,s}$ obtained by removing a node of
content $i$ from the Young diagram of $\la^\up$.
\item $F_i^\down \SS(\LA)$ has a multiplicity-free filtration
with sections $\SS(\MU)$
for $\MU \in \Par_{r,s+1}$ obtained by adding a node of
content $t^{-2} i^{-1}$ to the Young diagram of $\la^\down$.
\item $E_i^\down \SS(\LA)$ has a multiplicity-free filtration
with sections $\SS(\MU)$
for $\MU \in \Par_{r,s-1}$ obtained by removing a node of
content $t^{-2} i^{-1}$ from the Young diagram of $\la^\down$.
\end{enumerate}
In all cases, the filtrations should be ordered according to the
usual dominance ordering on the partitions labelling the sections,
most dominant at the bottom.
\end{lemma}

\begin{proof}
This follows from Lemmas~\ref{fur} and \ref{classical}.
\end{proof}

Now we turn our attention at last to $OS$ itself.
Mimicking the definitions made above for $OS^\circ$,
we  write $\i_\down:OS \rightarrow OS$ and
$\i_\up:OS\rightarrow OS$ for the algebra homomorphisms associated to
the functors $\down \otimes-:\OS(z,t) \rightarrow \OS(z,t)$ and $\up\otimes-:\OS(z,t)
\rightarrow \OS(z,t)$. 
Then let
\begin{align}\label{dob1}
{_\up} OS &:= \bigoplus_{\a,\b \in \words} 1_{\up \a} OS 1_\b,
&
OS_\up &:= \bigoplus_{\a,\b \in \words} 1_\a OS 1_{\up \b},\\
{_\down} OS &:= \bigoplus_{\a,\b \in \words} 1_{\down \a} OS 1_\b,&
OS_\down &:= \bigoplus_{\a,\b \in \words} 1_\a OS 1_{\down \b},\label{dob2}
\end{align}
which we view as $(OS, OS)$-bimodules
with left and right actions of $a,b \in OS$ on $f$ defined by $a\cdot
f\cdot b :=
\i_\up(a) f b,
a f \i_\up(b), \i_\down(a) f b$ and $a f \i_\down(b)$, respectively.
A key difference to the situation for $OS^\circ$ emerges right away:

\begin{lemma}\label{easy}
We have that $OS_\up \cong {_\down}OS$ and $OS_\down \cong {_\up}OS$
as $(OS, OS)$-bimodules.
\end{lemma}

\begin{proof}
The mutually inverse bimodule isomorphisms
$OS_\down \rightarrow {_\up} OS$ and ${_\up} OS \rightarrow OS_\down$
are defined on diagrams by the maps
$$
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[->, thick,darkblue] (-.12,.12) to (-.12,-.3);
\draw[-, thick,double,darkblue] (.12,.12) to (.12,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.89);
\node at (0,1.02) {$\a$};
\node at (.12,-.44) {$\b$};
\end{tikzpicture}
}
\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,darkblue] (-.22,-.2) to [out=0,in=-90] (-.12,.12);
\draw[<-, thick,darkblue] (-.3,.89) to [out=-90,in=180] (-.22,-.2);
\draw[-, thick,double,darkblue] (.12,.12) to (.12,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.89);
\node at (0,1.02) {$\a$};
\node at (.12,-.44) {$\b$};
\end{tikzpicture}
}
\qquad\text{and}\qquad
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[->,thick,darkblue] (-.12,.47) to (-.12,.89);
\draw[-, thick,double,darkblue] (.12,.47) to (.12,.89);
\node at (.12,1.02) {$\a$};
\node at (0,-.44) {$\b$};
\end{tikzpicture}
}
\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-,thick,darkblue] (-.12,.47) to [out=90,in=0] (-.22,.8);
\draw[<-,thick,darkblue] (-.3,-.3) to [out=90,in=180] (-.22,.8);
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[-, thick,double,darkblue] (.12,.47) to (.12,.89);
\node at (.12,1.02) {$\a$};
\node at (0,-.44) {$\b$};
\end{tikzpicture}
},
$$
respectively. The isomorphism $OS_\up \cong {_\down} OS$ is
constructed similarly.
\end{proof}

This means that we only need to define {\em two} functors:
\begin{align}\label{edef}
E:= ?\otimes_{OS} {_\up}OS
\,\cong\:
 ?\otimes_{OS} OS_{\down} &:\Mod OS \rightarrow \Mod OS,\\
 F:= ?\otimes_{OS} {_\down}OS\,\cong\: ?\otimes_{OS} OS_{\up} &:\Mod OS \rightarrow \Mod OS.
\end{align}
Note that
\begin{equation}\label{theee}
E (1_\a OS) = 1_\a OS \otimes_{OS} ({_\up} OS) = 1_\a({_\up}
OS) = 1_{\up \a} OS,
\end{equation} and
similarly $F(1_\a OS) = 1_{\down \a} OS$.
By adjointness of tensor and hom, the functor $E$ has a canonical 
right adjoint
\begin{equation}\label{Ra}
\bigoplus_{\a \in \words} \Hom_{OS}(1_{\up \a}OS, ?)
\cong \:? \otimes_{OS} OS_{\up}, 
\end{equation}
with the isomorphism here
sending $f$ 
in the $\a$th summand to 
$f(1_{\up \a}) \otimes 1_{\up \a}$.
In view of Lemma~\ref{easy}, the functor
$? \otimes_{OS} OS_{\up}$ on the right hand side of (\ref{Ra}) is isomorphic to $F$.
Thus, we see that $(E,F)$ is an adjoint pair.
Explicitly, the unit $\operatorname{Id} \rightarrow FE$ 
of this adjunction is 
defined by the bimodule homomorphism
\begin{align}\label{unit}
&OS \rightarrow {_\up}OS\otimes_{OS}{_\down}OS,&
&\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.1);
\draw[-, thick,double,darkblue] (0,.47) to (0,.69);
\node at (0,.85) {$\a$};
\node at (0,-.27) {$\b$};
\end{tikzpicture}
}
\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[->, thick,darkblue] (-.35,-.1) to (-.35,.69);
\draw[-, thick,double,darkblue] (0,.12) to (0,-.1);
\draw[-, thick,double,darkblue] (0,.47) to (0,.69);
\node at (0,.85) {$\a$};
\node at (0,-.27) {$\b$};
\end{tikzpicture}
}
\otimes
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-, thick,darkblue] (-.5,.4) to [out=180,in=-90] (-.7,.69);
\draw[->, thick,darkblue] (-.5,.4) to [out=0,in=-90] (-.3,.69);
\draw[-, thick,double,darkblue] (-0.05,-.1) to (-0.05,.69);
\node at (-0.05,-.27) {$\b$};
\end{tikzpicture}
},
\\\intertext{and the counit
$EF \rightarrow \operatorname{Id}$ is defined by}
&{_\down}OS \otimes_{OS} {_\up} OS
\rightarrow OS,
&&
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[<-,thick,darkblue] (-.12,.47) to (-.12,.89);
\draw[-, thick,double,darkblue] (.12,.47) to (.12,.89);
\node at (.12,1.05) {$\a$};
\node at (0,-.45) {$\b$};
\end{tikzpicture}
}\otimes\:\,
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle g$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[->,thick,darkblue] (-.12,.47) to (-.12,.89);
\draw[-, thick,double,darkblue] (.12,.47) to (.12,.89);
\node at (.12,1.07) {$\b$};
\node at (0,-.45) {$\c$};
\end{tikzpicture}
}
\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-, thick,double,darkblue] (.12,.7) to (.12,.89);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.53) rectangle ++(10pt,10pt);
\node at (0,.53) {$\scriptstyle f$};
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,0) rectangle ++(10pt,10pt);
\node at (0,0) {$\scriptstyle g$};
\draw[-, thick,double,darkblue] (0,-.18) to (0,-.3);
\draw[-,thick,darkblue] (-.12,.17) to [out=90,in=-90] (-.4,.5);
\draw[-,thick,darkblue] (-.4,.5) to[out=90,in=180] (-.25,.9);
\draw[->,thick,darkblue] (-.25,.9) to[out=0,in=90] (-.12,.7);
\draw[-, thick,double,darkblue] (.12,.17) to (.12,.35);
\node at (0,-.45) {$\c$};
\node at (.12,1.05) {$\a$};
\end{tikzpicture}
}.\label{counit}
\end{align}
Reversing the roles of $\up$ and $\down$ in this argument, we get another canonical
adjunction making
$(F,E)$ is an adjoint pair.
So $E$ and $F$ are biadjoint, hence, they are exact, and
preserve locally finite-dimensional, finitely generated, finitely
cogenerated, projective and injective objects;
cf. \cite[Theorem 2.11]{BD}.

Recalling (\ref{JM}),
let ${_{\up}}X:{_\up} OS \rightarrow {_\up} OS$
be the bimodule endomorphism defined on $1_{\up \b} OS$ 
by
left multiplication by $X(\up \b)$, 
and 
let 
$X_{\down}:OS_\down\rightarrow OS_\down$ be defined on $1_\b OS_{\down \b}$ by right multiplication
by $X(\down \b)$.
These are intertwined by the isomorphism from Lemma~\ref{easy}; this
depends on (\ref{d4}).
Similarly, switching $\up$ with $\down$ everywhere, we get
endomorphisms ${_{\down}}X:{_\down}OS\rightarrow {_\down} OS$ and
$X_{\up}:OS_\up \rightarrow OS_\up$, which are again intertwined by the
isomorphism from Lemma~\ref{easy}.

\begin{lemma}\label{newz}
There are short exact sequence of $(OS^\circ, OS)$-bimodules
\begin{align}
0
&\longrightarrow
OS^\circ_\up \otimes_{OS^\sharp} OS 
\stackrel{\alpha}{\longrightarrow}
OS^\circ \otimes_{OS^\sharp} OS_\up
\stackrel{\beta}{\longrightarrow}
{_\down}OS^\circ\otimes_{OS^\sharp} OS
\longrightarrow 0,\label{ses1}\\
0
&\longrightarrow
OS^\circ_\down \otimes_{OS^\sharp} OS 
\stackrel{\alpha}{\longrightarrow}
OS^\circ \otimes_{OS^\sharp} OS_\down
\stackrel{\beta}{\longrightarrow}
{_\up}OS^\circ\otimes_{OS^\sharp} OS
\longrightarrow 0.\label{ses2}
\end{align}
The maps $\alpha$ and $\beta$ in the first sequence 
satisfy $\alpha \circ (X^\circ_{\up} \otimes \id)= (\id
\otimes X_{\up})\circ \alpha$ and $\beta \circ (\id \otimes X_{\up}) = ({_{\down}}X^\circ \otimes \id) \circ \beta$.
The maps in the second sequence have analogous properties.
\end{lemma}

\begin{proof}
We just go through the details for the first short exact sequence. 
The bimodule homomorphisms $\alpha$ and $\beta$ are defined on pure
tensors as follows:
\begin{align}\label{alpha}
\alpha:
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[->, thick,darkblue] (-.1,-.3) to (-.1,.12);
\draw[-, thick,double,darkblue] (0.1,.12) to (0.1,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0.1,-.45) {$\b$};
\node at (0,1.02) {$\a$};
\end{tikzpicture}
}
\otimes
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle g$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,1.05) {$\b$};
\node at (0,-.45) {$\c$};
\end{tikzpicture}
}
&\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[->, thick,darkblue] (-.1,-.3) to (-.1,.12);
\draw[-, thick,double,darkblue] (0.1,.12) to (0.1,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0.1,-.45) {$\b$};
\node at (0,1.02) {$\a$};
\end{tikzpicture}
}
\otimes
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle g$};
\draw[->, thick,darkblue] (-.35,-.3) to (-.35,.85);
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,1.05) {$\b$};
\node at (0,-.45) {$\c$};
\end{tikzpicture}
}\:,&
\beta:
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,-.45) {$\b$};
\node at (0,1.02) {$\a$};
\end{tikzpicture}
}
\otimes
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle g$};
\draw[<-, thick,darkblue] (-0.1,.12) to (-0.1,-.3);
\draw[-, thick,double,darkblue] (0.1,.12) to (0.1,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,1.05) {$\b$};
\node at (0.1,-.45) {$\c$};
\end{tikzpicture}
}
&\mapsto
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle f$};
\draw[->, thick,darkblue] (-.35,.85) to (-.35,-.3);
\draw[-, thick,double,darkblue] (0,.12) to (0,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,1.02) {$\a$};
\node at (0,-.45) {$\b$};
\end{tikzpicture}
}
\otimes
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (0,.3) rectangle ++(10pt,10pt);
\node at (0,.3) {$\scriptstyle g$};
\draw[-, thick,darkblue] (-.4,.85) to (-.4,.1);
\draw[-, thick,darkblue] (-.4,.1) to [out=-90,in=180] (-.25,-.1);
\draw[->, thick,darkblue] (-.25,-.1) to [out=0,in=-90] (-.1,.12);
\draw[-, thick,double,darkblue] (0.1,.12) to (0.1,-.3);
\draw[-, thick,double,darkblue] (0,.47) to (0,.85);
\node at (0,1.05) {$\b$};
\node at (0.1,-.45) {$\c$};
\end{tikzpicture}
}\:.
\end{align}
It is straightforward to see these are well-defined bimodule
homomorphisms.
Also $\beta \circ \alpha = 0$. 
Indeed, if we apply $\beta \circ \alpha$ to a pure tensor as above, we
produce a pure tensor of the form $f \otimes g$ 
such that
the strand of $g$ starting in
the top left corner is a rightward cup. This cup commutes past the tensor to give zero
since we are viewing ${_\down}OS^\circ$ as a right $OS^\sharp$-module by inflation.

To show that the sequence is exact, we pick bases.
Recall that $\words_{r,s}$ denotes words which have exactly $r$ letters $\up$ and $s$
letters $\down$.
For $\a,\b \in \words_{r,s}$, let $A_{\a,\b}$ be a basis for $1_\a OS^\circ 1_\b$ 
consisting of reduced lifts of matchings. 
Similarly, for $\b \in \words_{r,s}$ and $\c \in \words_{r+t,s+t}$ for $t \geq 0$, 
let $B_{\b,\c}$ be a basis for $1_\b OS^- 1_\c$ consisting of reduced
lifts of matchings.
By Lemma~\ref{td}, we see that
\begin{align*}
P &:= \left\{f \otimes g\:\bigg|\:
\begin{array}{l}
f \in A_{\a, \up \b}, g \in B_{\b,\c}\text{ for }
r,s,t\geq 0\text{ and }\\
\a \in \words_{r+1,s}, \b \in \words_{r,s}, \c \in \words_{r+t,s+t},
\end{array}
\right\},\\
Q &:= \left\{f \otimes g\:\bigg|\:
\begin{array}{l}
f \in A_{\a, \b}, g \in B_{\b,\up \c}\text{ for }
r,s,t\geq 0\text{ with }s+t\geq 1\text{ and }\\
\a, \b \in \words_{r,s}, \c \in \words_{r+t,s+t-1},
\end{array}
\right\},\\
R &:= \left\{f \otimes g\:\bigg|\:
\begin{array}{l}
f \in A_{\down \a, \b}, g \in B_{\b,\c}\text{ for }
r,s,t\geq 0\text{ and }\\
\a \in \words_{r,s}, \b \in \words_{r,s+1}, \c \in \words_{r+t,s+t+1},
\end{array}
\right\}
\end{align*}
are bases for $OS^\circ_\up \otimes_{OS^\sharp} OS$,
$OS^\circ \otimes_{OS^\sharp} OS_\up$ and ${_\down}OS^\circ\otimes_{OS^\sharp}
OS$, respectively.
Then we partition the set $Q$ as $Q_1\sqcup Q_2$
so that $Q_1$ consists of all $f \otimes g \in Q$ such that the
reduced lift $g$ has a propagating upward strand on its left edge,
and $Q_2$ consists of all remaining elements of $Q$.
Note for each $f \otimes g \in Q_2$ that 
the strand of $g$ starting in
the bottom left corner is a rightward cap. Then it is clear that the
map $\alpha$ maps $P$ bijectively onto $Q_1$ and $\beta$ maps $Q_2$
bijectively onto $R$. This completes the proof.

Now we check that
$\alpha \circ (X^\circ_{\up}\otimes \id) = (\id \otimes X_{\up}) \circ \alpha$.
Take
$f \otimes g\in
OS^\circ_\up \otimes_{OS^\sharp} OS$.
We must show that
$(f \circ X^\circ(\up \b)) \otimes (\up g) = f \otimes ((\up g) \circ X(\up
  \c))$ for $f \in 1_\a OS^\circ 1_{\up \b}$ and $g \in 1_\b OS 1_{\c}$.
We can move $X^\circ(\up \b)$ over the first tensor product and commute $X(\up \c)$
with $\up g$, to reduce to checking that
$1_{\up \b} \otimes X(\up \b) =1_{\up \b} \otimes X^\circ(\up \b).$
The morphism $X^\circ(\up \b)$ can be transformed into $X(\up \b)$ 
by using the quadratic relation to switch 
some positive crossings to negative crossings. This produces some
error terms which involve caps at the top of the picture, which become
zero when commuted back over the tensor product.
(This argument can be made more formal by using induction on the
length of the word $\b$, using the recursions (\ref{JMa}) and (\ref{chile2}).)

The proof that
$\beta \circ (\id \otimes X_{\up}) =
({_{\down}}X^\circ \otimes \id)\circ \beta$ is similar; one needs to use also
(\ref{d5}) and Lemma~\ref{chile0}.
\end{proof}

Finally, we refine the functors $E$ and $F$.
For $i \in \k^\times$, let $E_i$ be the subfunctor of $E$ that is
defined by tensoring with the bimodule that is the generalized
$i$-eigenspace of ${_{\up}}X:{_\up}OS \rightarrow {_\up} OS$;
equivalently, it may be defined by tensoring
with the generalized $i$-eigenspace of 
$X_{\down}:OS_\down \rightarrow OS_\down$.
Similarly, switching $\up$ and $\down$ everywhere, defines a
subfunctor $F_i$ of $F$.
Let
\begin{equation}\label{I}
I := I_1 \cup I_{t^{-2}} = \left\{q^{2n}, t^{-2} q^{-2n}\:\big|\:n\in \ZZ\right\} \subset \k^\times.
\end{equation}

\begin{lemma}\label{phew}
There are short exact sequences of functors
for each $i \in \k^\times$:
\begin{align}\label{sesI}
0&\longrightarrow
\Delta \circ F_i^\up \longrightarrow F_i \circ \Delta \longrightarrow
\Delta \circ F_i^\down \longrightarrow 0,\\\label{sesII}
0&\longrightarrow
\Delta \circ E_i^\down \longrightarrow E_i \circ \Delta \longrightarrow
\Delta \circ E_i^\up \longrightarrow 0.
\end{align}
Moreover,
the functors $E_i$ and $F_i$ are biadjoint, and we have that
\begin{equation}\label{decomp2}
E = \bigoplus_{i \in I} E_i,
\qquad
F = \bigoplus_{i \in I} F_i.
\end{equation}
\end{lemma}

\begin{proof}
Note to start with that although ${_\down} OS$ is not
finite-dimensional (or even a direct sum of finite-dimensional
bimodules as was the case for ${_\down} OS^\circ$), it is locally
finite-dimensional in the sense that it is the direct sum of
the finite-dimensional vector spaces $1_{\down \a} OS 1_\b$ for $\a,\b \in
\words$. The endomorphism ${_{\down}}X$ leaves each of these
finite-dimensional vector
spaces invariant. This is enough to see that each generalized $i$-eigenspace of
${_{\down}}X$ is a summand of the bimodule ${_\down} OS$.
However, until we have proved (\ref{decomp2}), there may also be summands
arising from generalized
eigenspaces corresponding to eigenvalues of ${_{\down}}X$ not in $I
\subset \k^\times$, and there could
also be summands arising from non-linear irreducible factors of the
characteristic polynomial.
Similar remarks apply to $F_i$.

To define an adjunction making $(E_i,F_i)$ into an adjoint pair,
we project the adunction for $(E,F)$ onto the summands $E_i$ and $F_i$.
To see that this does the job, 
one needs to use the explicit forms for the unit and counit of the adjunction $(E,F)$
given in (\ref{unit})--(\ref{counit}). The key point is that
${_{\up}}X \otimes \operatorname{id} = \operatorname{id} \otimes
{_{\down}}X$ as an endomorphism of ${_\up} OS \otimes_{OS} {_\down} OS$
and ${_{\down}}X \otimes \operatorname{id} = \operatorname{id} \otimes
{_{\up}}X$ as an endomorphism of ${_\down} OS \otimes_{OS} {_\up} OS$.
A similar argument produces an adjunction $(F_i,E_i)$ the other way
around.
It then follows that $E_i$ and $F_i$ are both exact; one can also see
this since they are summands of the exact functors $E$ and$F$.

The short exact sequences from Lemma~\ref{newz} may be viewed
equivalently as short exact sequences of functors
\begin{align*}
0&\longrightarrow
\Delta \circ F^\up \longrightarrow F \circ \Delta \longrightarrow
\Delta \circ F^\down \longrightarrow 0,\\
0&\longrightarrow
\Delta \circ E^\down \longrightarrow E \circ \Delta \longrightarrow
\Delta \circ E^\up \longrightarrow 0.
\end{align*}
Similarly, using the final assertion of the lemma, we get
(\ref{sesI})--(\ref{sesII}) from
Lemma~\ref{newz} on passing to the appropriate generalized
eigenspaces.

Finally, we must establish (\ref{decomp2}).
The short exact sequences of functors obtained in the previous paragraph plus
(\ref{decomp1})
imply that (\ref{decomp2}) holds on any standard module $\Delta(\LA)$.
By exactness and Corollary~\ref{BGG}, it follows that it also holds on
any indecomposable projective module.
Hence, it is true on any module.
\end{proof}

With these branching rules in hand, we can proceed to the definition
of the formal character of a locally finite-dimensional $OS$-module.

First, we must refine the idempotents $1_\a$ for $\a \in \words$.
Let $\Words$ be the set of words in the
letters $\{\up_i, \down_i\:|\:i \in I\}$.
Thus, an element of $\Words$ has the form
$\a_\bi = (\a_n)_{i_n}\cdots (\a_1)_{i_1}$
for words $\a = \a_n \cdots \a_1 \in \words$
and $\bi = i_n \cdots i_1 \in \langle I \rangle$.
Take a word $\a_\bi \in \Words$ of length $n$.
Let $X_i$ be the Jucys-Murphy element in $1_\a OS 1_\a$ that is defined by a dot
on the $i$th strand from the right, so that
 $X_1,\dots,X_n$ generate a commutative subalgebra of the
finite-dimensional algebra $1_\a OS 1_\a$.
It follows that there is an idempotent $1_{\a_\bi} \in 1_\a OS 1_\a$
which projects any $1_\a OS 1_\a$-module onto the simultaneous
generalized eigenspaces of $X_1,\dots,X_n$
corresponding to eigenvalues $i_1,\dots,i_n$, respectively.
For a given $\a$, all but finitely many $1_{\a_\bi}$ are zero.

Now define the {\em formal character} of a locally finite-dimensional
$OS$-module $M$ by
\begin{equation}
\ch M := \sum_{\a_\bi\in\Words} (\dim M 1_{\a_\bi}) \a_\bi,
\end{equation}
which is an element of the ring of (possibly infinite) $\ZZ$-linear combinations of elements of
the monoid $\Words$.
From the proof of the following lemma plus (\ref{decomp2}), one sees
that $1_\a = \sum_{\bi} 1_{\a_\bi}$.
Note also that $\ch$ is additive on short exact sequences.

\begin{lemma}\label{basically}
$\ch M = \sum_{i \in I} \down_i (\ch E_i M) 
+ \sum_{i \in I} \up_i (\ch F_i M).$
\end{lemma}

\begin{proof}
Take $\a_\bi\in \Words$
and suppose that $\a = \up \b, \bi = i \bj$.
We claim that $\dim M 1_{\a_\bi} = \dim (F_i M) 1_{\b_\bj}$.
The lemma follows from this together with
the analogous statement 
argument with $\up$ replaced with $\down$ and $F_i$ replaced with
$E_i$. 
To prove the claim, 
using (\ref{theee}), we have that
\begin{align*}
M 1_{\a}\cong\Hom_{OS}(1_{\a} OS, M)&\cong\Hom_{OS}(E (1_\b OS), M)\\
&\cong \Hom_{OS}(1_\b OS, F M)
\cong (FM) 1_\b.
\end{align*}
Under this isomorphism, the generalized $i$-eigenspace of 
$\mathord{
\begin{tikzpicture}[baseline = -1mm]
      \node at (0,0) {$\color{darkblue}\scriptstyle\bullet$};
	\draw[<-,thick,darkblue] (0,0.25) to (0,-0.25);
\end{tikzpicture}
} \otimes 1_\b$
corresponds to the summand $(F_i M) 1_\b$.
The result follows.
\end{proof}

\begin{lemma}
The characters 
$\left\{\ch \L(\LA)\:\big|\:\LA \in \RPar\right\}$
of the irreducible $OS$-modules
are linearly independent.
\end{lemma}

\begin{proof}
Take $\LA \in \RPar_{r,s}$.
As $\L(\LA)$ is the shortest word module of type $\LA$, its formal
character is a sum $A_\lambda$ of words of the form $\down_{i_{r+s}}
\cdots \down_{i_{r+1}} \up_{i_r} \cdots \up_{i_1}$, 
plus a sum $B_\lambda$ of words that are
obtained from the ones in $A_\lambda$ by properly shuffling the $\down$'s and $\up$'s,
plus a sum $C_\lambda$ of strictly longer words.
By unitriangularity, it suffices to show that the ``leading terms''
$A_\lambda$ are linearly independent for fixed $r,s$ and all $\LA \in
\RPar_{r,s}$.
But $A_\lambda$ is just the product of the formal characters of
$\D_{\la^\down}$ and $\D_{\la^\up}$ in the usual sense of the 
Hecke algebras $H_s$ and $H_r$.
So these words are linearly independent by the well-known linear
independence of irreducible characters for the Hecke
algebra\footnote{This may be proved in
the same way as is explained for the symmetric group in \cite[Lemma 11.2.5]{Kbook}.}.
\end{proof}


Now we define the ($t$-shifted) {\em bipartition graph} to be the $I$-colored directed
graph with vertices $\Par$ and an edge $\LA \stackrel{i}{\rightarrow}
\MU$ if one of the following holds:
\begin{itemize}
\item $\MU$ is obtained from $\LA$ by adding a node of content $i$ to
 $\la^\up$;
\item $\LA$ is obtained from $\MU$ by adding a node of
  content $t^{-2}i^{-1}$
to $\mu^\down$.
\end{itemize}
A small piece of this graph is displayed in Figure 2.
\begin{figure}[hb]
\[
\mathord{
\begin{tikzpicture}[scale=0.7]
	
	\node (a) at (0, 4) {\small$\NOTHING$};
	\node (b) at (-4, 2) {$\left(\text{\tiny$\yng(1)$} , {\scriptstyle\varnothing}\right)$};
	\node (c) at (4, 2) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(1)$}\right)$};
	\node (d) at (-8, 0) {$\left(\text{\tiny$\yng(1,1)$}, {\scriptstyle\varnothing}\right)$};
	\node (e) at (-4, 0) {$\left(\text{\tiny$\yng(2)$}, {\scriptstyle\varnothing}\right)$};
	\node (f) at (0, 0) {$\left({\text{\tiny$\yng(1)$}, \text{\tiny$\yng(1)$}}\right)$};
	\node (g) at (4, 0) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(1,1)$}\right)$};
	\node (h) at (8, 0) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(2)$}\right)$};
	\node (i) at (-9, -4) {$\left({\text{\tiny$\yng(1,1,1)$}}, {\scriptstyle\varnothing}\right)$};
	\node (j) at (-7, -4) {$\left({\text{\tiny$\yng(2,1)$}}, {\scriptstyle\varnothing}\right)$};
	\node (k) at (-5, -4) {$\left({\text{\tiny$\yng(3)$}}, {\scriptstyle\varnothing}\right)$};
	\node (l) at (-3, -4) {$\left({\text{\tiny$\yng(1,1)$}, \text{\tiny$\yng(1)$}}\right)$};
	\node (m) at (-1, -4) {$\left({\text{\tiny$\yng(2)$}, \text{\tiny$\yng(1)$}}\right)$};
	\node (n) at (1, -4) {$\left({\text{\tiny$\yng(1)$}, \text{\tiny$\yng(1,1)$}}\right)$};
	\node (o) at (3, -4) {$\left({\text{\tiny$\yng(1)$}, \text{\tiny$\yng(2)$}}\right)$};
	\node (p) at (5, -4) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(1,1,1)$}\right)$};
	\node (q) at (7, -4) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(2,1)$}\right)$};
	\node (r) at (9, -4) {$\left({\scriptstyle\varnothing}, \text{\tiny$\yng(3)$}\right)$};
	
	\draw[->] (a) to node[above]{$\scriptstyle 1$} (b);
	\draw[<-] (a) to node[above]{$\scriptstyle\:\:\:t^{-2}$} (c);
	
	\draw[->] (b) to node[above]{$\scriptstyle q^{-2}$} (d);
	\draw[->] (b) to node[right]{$\scriptstyle q^2$} (e);
	\draw[<-] (b) to node[above]{$\scriptstyle \:\:\:t^{-2}$} (f);
	
	\draw[->] (c) to node[above]{$\scriptstyle 1$} (f);
	\draw[<-] (c) to node[right]{$\!\scriptstyle t^{-2}q^2$}(g);
	\draw[<-] (c) to node[above]{$\:\:\:\:\:\scriptstyle t^{-2}q^{-2}$} (h);
	
	\draw[->] (d) to node[left]{$\scriptstyle q^{-4}$} (i);
	\draw[->] (d) to node[right]{$\scriptstyle \!q^2$} (j);
	\draw[<-] (d) to node[near start, above]{$\scriptstyle \:\:\:\:t^{-2}$} (l);
	
	\draw[->] (e) to node[near end, below right]{$\scriptstyle \!\!\!\!\!q^{-2}$} (j);
	\draw[->] (e) to node[right]{$\scriptstyle\! q^4$} (k);
	\draw[<-] (e) to node[near start, above right]{$\scriptstyle \!\!\!t^{-2}$} (m);
	
	\draw[->] (f) to node[above left]{$\scriptstyle q^{-2}\!\!\!\!\!\!$} (l);
	\draw[->] (f) to node[below left]{$\scriptstyle q^2$} (m);
	\draw[<-] (f) to node[below left,near end]{$\scriptstyle t^{-2}q^2\!\!\!$} (n);
	\draw[<-] (f) to node[near start, above right]{$\scriptstyle\!\!\!\! t^{-2}q^{-2}$} (o);
	
	\draw[->] (g) to node[above left]{$\scriptstyle 1\!\!\!$} (n);
	\draw[<-] (g) to node[left]{$\scriptstyle t^{-2}q^{4}\!$} (p);
	\draw[<-] (g) to node[near start, above right]{$\scriptstyle\!\!\!\!\! t^{-2}q^{-2}$} (q);
	
	\draw[->] (h) to node[near start, above]{$\scriptstyle 1\!\!\!$} (o);
	\draw[<-] (h) to node[left]{$\scriptstyle t^{-2}q^2\!\!$} (q);
	\draw[<-] (h) to node[right]{$\scriptstyle \!t^{-2}q^{-4}$} (r);
\end{tikzpicture}
}
\]
\caption[Bipartition graph up to word length $3$]{Bipartition graph up to
  word length $3$}
\end{figure}

By a {\em path} $\gamma:\LA \rightsquigarrow \MU$ we mean an undirected path in
the bipartition graph
starting at $\LA$ and ending
at $\MU$.
The {\em type} of
such a path $\gamma$ is $\type(\gamma):=\a_\bi \in
\Words$ 
where $\bi = i_n \cdots i_1$ records the colors on the edges of the path
$\LA \stackrel{i_1}{\rule{5mm}{0.5pt}} \cdots \stackrel{i_n}{\rule{5mm}{0.5pt}} \MU$
and $\a = \a_n \cdots \a_1\in\words$ is defined so $\a_m = \up$ or
$\down$ according to whether
the $m$th edge is traversed forwards or backwards according to its direction.
For example, the path
$$
\left(\,\text{\small$\yng(1)$}\,,\,\varnothing\right)
\stackrel{\:t^{-2}\!}{\longleftarrow}  \left(\,\text{\small$\yng(1)$}\,,\,\text{\small$\yng(1)$}\,\right)
\stackrel{1}{\longleftarrow}  \left(\varnothing\,,\,\text{\small$\yng(1)$}\,\right)
\stackrel{t^{-2}}{\longrightarrow} \NOTHING
\stackrel{t^{-2}}{\longleftarrow}
\left(\varnothing\,,\,\text{\small$\yng(1)$}\,\right)$$
is of type $\down_{t^{-2}}\up_{t^{-2}} \down_1 \down_{t^{-2}}$.

\begin{theorem}\label{characters}
For $\LA \in \Par$, we have that
$\displaystyle\ch \tilde \Delta(\LA) =
\sum_{\gamma:\NOTHING\rightsquigarrow \LA} \type(\gamma).$
\end{theorem}

\begin{proof}
Note the infinite
sum in the theorem makes sense since there are only finitely
many paths of any given length.
From (\ref{sesI})--(\ref{sesII}) and Lemma~\ref{newfirst},
we get some explicit $\tilde\Delta$-filtrations of
 $E_i \tilde\Delta(\LA)$
and $F_i \tilde\Delta(\LA)$ with sections $\tilde\Delta(\MU)$ 
for each $\MU \stackrel{i}{\leftarrow}
\LA$ or
$\MU \stackrel{i}{\rightarrow} \LA$, respectively.
Applying Lemma~\ref{basically}, we deduce that
$$
\ch \tilde\Delta(\LA) = \sum_{i\in I}\Big(\sum_{\MU
  \stackrel{i}{\leftarrow} \LA} \down_i \ch \tilde\Delta(\MU)+
 \sum_{\MU
  \stackrel{i}{\rightarrow} \LA} \up_i \ch \tilde\Delta(\MU)\Big).
$$
Now use induction on path length.
\end{proof}

\begin{corollary}\label{Canpath}
Take $\LA \in \Par$ and $\MU \in \RPar$.
If $\L(\MU)$ is a composition factor of $\tilde\Delta(\LA)$
then there is a path $\gamma:\NOTHING\rightsquigarrow\LA$ 
and a minimal length path $\delta:\NOTHING\rightsquigarrow \MU$
such that $\type(\gamma)=\type(\delta)$.
\end{corollary}

\begin{proof}
Pick any word $\a_\bi \in \words_I$ that appears with non-zero
coefficient in the formal character of the shortest word space of
$\L(\MU)$.
Since 
$[\widetilde\Delta(\LA):\L(\MU)]$ and
$[\widetilde\Delta(\MU):\L(\MU)]$ are both non-zero, 
$\a_\bi$ also has non-zero coefficients in $\ch \widetilde\Delta(\LA)$
and $\ch \widetilde\Delta(\MU)$.
So
Theorem~\ref{characters} implies
that there are paths $\gamma:\NOTHING \rightsquigarrow \LA$ and 
$\delta:\NOTHING \rightsquigarrow \MU$ of the same type
$\a_\bi$. Moreover, $\delta$ is of minimal length amongst all paths
$\NOTHING \rightsquigarrow \MU$.
\end{proof}

\begin{corollary}\label{morocco}
Suppose that $\MU \in \RPar_{r,s}$. 
If {\em either} $t \notin \{\pm q^n\:|\:n \in \ZZ\}$, {\em or}
$e=0$, $t = q^{n}$ for $n \in \NN$ and $h(\MU) \leq n$,
then we have that $\P(\MU) = \Delta(\MU)$.
\end{corollary}

\begin{proof}
In view of Corollary~\ref{BGG}, it suffices to show that
$[\bar\Delta(\LA):\L(\MU)] = \delta_{\LA,\MU}$ for all $ \LA \in \RPar$.
Since $\bar\Delta(\LA)$ and $\L(\MU)$ have the same shortest word
spaces, this follows if we can show for $\LA \in \RPar$ that
$[\bar\Delta(\LA):\L(\MU)] \neq 0
\Rightarrow \LA \in \RPar_{r,s}$.
So suppose that $[\bar\Delta(\LA):\L(\MU)]\neq 0$.
Corollary~\ref{Canpath} implies that 
there is a path $\gamma:\NOTHING\rightsquigarrow\LA$
of the same type as a minimal length path $\delta:\NOTHING
\rightsquigarrow \MU$.
Being of minimal length means that $\delta$ is some permutation of the word
$\up_{i_{r+s}}\cdots\up_{i_{r+1}}\down_{i_{r}}\cdots\down_{i_{1}}$,
where $i_1,\dots,i_r$ are the $\up$-contents of the nodes of $\mu^\up$
and $i_{r+1},\dots,i_{r+s}$ are the $\down$-contents of the nodes of
$\mu^\down$.

If $t \notin \{\pm q^n\:|\:n \in \ZZ\}$, then the set of possible
$\up$-contents of nodes of partitions is disjoint from the set of
possible $\down$-contents.
So any path of type $\delta$ starting at $\NOTHING$ necessarily 
ends at an element of $\Par_{r,s}$. We deduce that $\LA
\in \RPar_{r,s}$ as required.
Instead, suppose that $e=0, t = q^n$ for $n \in \NN$, and $h(\MU)
\leq |n|$. 
Recalling that $h(\MU)$ is the total number of non-zero
parts in both $\mu^\up$ and $\mu^\down$,
these assumptions imply that 
$i_1,\dots,i_{r+s}$ are all distinct, and there is a unique path of type $\delta$
starting at $\NOTHING$. This shows that $\gamma=\delta$, hence, $\LA = \MU$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{selection}]
Corollary~\ref{morocco} shows that $\P(\LA) = \Delta(\LA)$ for all $\LA
\in \RPar$. 
So the standardization functor $\Delta$ 
sends the indecomposable projectives $\{\Y(\LA)\:|\:\LA\in\RPar\}$ in $\Mod OS^\circ$
to the indecomposable projectives $\{\P(\LA)\:|\:\LA \in \RPar\}$ in $\Mod OS$.
Since this functor is also exact, it follows that it is an equivalence
of categories.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{sscase}]
Suppose that $q$ is not a root of unity and $t \notin \{\pm
q^n\:|\:n \in \ZZ\}$.
The first assumption means that $e=0$, so $OS^\circ$ is semisimple.
Hence, $OS$, or equivalently $\dot\OS(z,t)$, is semisimple thanks to Theorem~\ref{selection}.
The parametrization of indecomposable objects in $\dot\OS(z,t)$
follows from Theorem~\ref{class}: up to isomorphism they correspond to the irreducible
projective modules
$\{\Delta(\LA)\:|\:\LA \in \Par\}$.
Moreover, Theorem~\ref{thegg} shows in this case that
$K_0(\dot\OS(z,t))$ may be identified with $\SYM\otimes_\ZZ\SYM$ so that
$[\Delta(\LA)] \leftrightarrow \chi_\LA$.

It remains to show that $OS$ is not semisimple 
for all other parameter choices.
If $q$ is a root of unity and $t \notin \{\pm q^n\:|\:n \in \ZZ\}$,
this follows from Theorem~\ref{selection}, since Hecke algebras are not
semisimple at roots of unity.
Finally, suppose that $q$ is arbitrary but $t = \pm q^n$ for some $n \in \ZZ$.
Using the isomorphisms (\ref{pi})--(\ref{signaut}), we may as well assume that
$t = q^n$ for $n \in \NN$.
Example~\ref{swex} shows that $\bar\Delta(((n),\varnothing))$ is
reducible, since it has a composition factor isomorphic to
$\L(((n+1),(1)))$.
Since $\bar\Delta(((n),\varnothing))$ is a finitely generated module with
irreducible head, it is therefore not completely reducible,
and $OS$ is not semisimple.
\end{proof}
