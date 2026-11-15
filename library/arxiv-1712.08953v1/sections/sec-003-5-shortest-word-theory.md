---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-003-5-shortest-word-theory
section_title: "Shortest word theory"
section_number: 5
pages: 25-36
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.957
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an oriented link, in the same"
---
\label{sswt}

For the next few sections, we assume that $\k$ is a field of
characteristic $p \geq 0$ and $z = q-q^{-1}$ for $q \in
\k^\times\setminus\{\pm 1\}$.
Since we are going to be discussing linear representations rather than tensor
ones, it is natural to replace the category $\OS(z,t)$ with the associative
algebra
$$
OS = \bigoplus_{\a,\b \in \words} 1_\a OS 1_\b
\qquad\text{where}\qquad
1_\a OS 1_\b := \Hom_{\OS(z,t)}(\b,\a),
$$
multiplication being induced by composition in $\OS(z,t)$.
This algebra is {\em locally unital} rather than unital,
with a distinguished system of local units given by the mutually
orthogonal idempotents 
$\{1_\a\:|\:\a \in \words\}$.
The functor 
category $\Mod \OS(z,t)$ of $\OS(z,t)$-modules as defined in the introduction
may be identified with the usual algebraic category $\Mod OS$ of all {\em right
  $OS$-modules} $M$ which are locally unital in the sense that
$M = \bigoplus_{\a \in \words} M 1_\a$. 
The additive Karoubi envelope $\dot\OS(z,t)$ is
equivalent to the full subcategory $\pMod OS$ of $\Mod OS$ consisting of {\em finitely generated
  projective modules},
i.e., modules isomorphic to finite direct sums of right ideals
$e OS$ for idempotents $e \in OS$.
This means that we may identify $K_0(\dot\OS(z,t))$ with the split
Grothendieck group $K_0(\pMod OS)$;
the resulting ring structure on $K_0(\pMod OS)$ is determined by
$$
[e OS] [f OS] = [(e\otimes f) OS]
$$
for idempotents $e,f \in OS$.

Each $1_\a OS 1_\b$ is finite-dimensional by Theorem~\ref{bt}, hence,
$OS$ is {\em locally finite-dimensional}, and $\Mod OS$ is a
{\em locally Schurian category} in the sense of \cite[$\S$2]{BD}.
We will freely use the general language and results about such categories explained
there, most of which boil down to the observation that 
$\Mod OS$ is a Grothendieck category.
In particular, we let $\lfdMod OS$ be the subcategory of $\Mod OS$ consisting of all
{\em locally finite-dimensional modules}, i.e., the $OS$-modules $M$
such that 
$\dim_\k M 1_\a < \infty$ for all $\a \in \words$.
These are exactly the modules that have finite composition
multiplicities.
Any finitely generated
$OS$-module $M$ is locally finite-dimensional, so that $\pMod OS$ is a
subcategory of $\lfdMod OS$.

In this section, we are going to classify the irreducible $OS$-modules.
The key to our approach is that the algebra $OS$ has a {\em
  triangular decomposition}.
Any ribbon has three sorts of component: 
\begin{itemize}
\item cups
whose boundary is on $y=1$;
\item
caps whose boundary is on $y=0$;
\item
propagating strands whose boundary intersects both $y=0$ and $y=1$.
\end{itemize}
The cups and caps carry an overall orientation that is either leftward or rightward, while the
propagating strands are either upward strands or downward strands.
Introduce the following locally unital subalgebras of $OS$:
\begin{itemize}
\item[$OS^\circ_{r,s}$:] 
The $\k$-span of all ribbons that have 
$r$ propagating upward strands and $s$ propagating downward strands,
no components that are cups or caps,
and in 
which propagating upward strands only cross underneath propagating
downward strands.
\item[$OS^\circ$:] $\bigoplus_{r,s \geq 0} OS^\circ_{r,s}$.
\item[$OS^+$:] The $\k$-span of all ribbons that have no components that are caps and in which no
  two propagating strands cross.
\item[$OS^\sharp$:] The $\k$-span of all ribbons with no components
  that are caps 
and in 
which propagating upward strands only cross underneath propagating
downward strands.
\item[$OS^-$:] The $\k$-span of all ribbons that have no components that are cups and in which no
  two propagating strands cross.
\item[$OS^\flat$:] The $\k$-span of all ribbons with no components
  that are cups 
and in 
which propagating upward strands only cross underneath propagating
downward strands.
\end{itemize}
It is obvious that these are all locally unital subalgebras of $OS$. Also, $OS$ is
graded as $OS = \bigoplus_{d \in \ZZ} OS[d]$ with $OS[d]$ spanned by
all ribbons such that the total number of cups minus the total number
of caps equals $d$. This induces a grading on each of the subalgebras
above. Moreover, $OS^\sharp[0] = OS^\flat[0] = OS^\circ$.
We have already introduced the right $OS$-module categories $\Mod
OS, \lfdMod OS$ and $\pMod OS$. We adopt analogous notation for all of
these other locally unital algebras.
Also let $$\fdMod OS^\circ = \coprod_{r,s\geq 0} \fdMod OS_{r,s}^\circ
$$ 
be the category of (globally) finite-dimensional right
$OS^\circ$-modules.

In the following lemma, we take tensor products of locally unital modules over the
locally unital algebra $\K
:= \bigoplus_{\a \in \words} \k 1_\a < OS$. In terms of the usual tensor
product $\otimes$ over the ground field $\k$, we have that
$V \otimes_\K W = \bigoplus_{\a \in \words} V 1_\a \otimes 1_\a W$.

\begin{lemma}\label{td}
Multiplication define a  vector space isomorphism
\begin{align*}
OS^+ \otimes_\K OS^\circ \otimes_\K OS^- &\stackrel{\sim}{\rightarrow}
OS.
\end{align*}
Similarly, there are isomorphisms
$OS^+ \otimes_\K OS^\circ\stackrel{\sim}{\rightarrow} OS^\sharp$ and 
$OS^\circ \otimes_\K OS^- \stackrel{\sim}{\rightarrow} OS^\flat$.
\end{lemma}

\begin{proof}
We apply Theorem~\ref{bt} to pick a basis for $OS^+$
consisting of cap-free generic reduced lifts of matchings.
Similarly, we pick a basis for $OS^-$.
Finally, we pick a basis for $OS^\circ$ consisting of cup- and cap-free generic ribbons, all
of whose rightward crossings are positive and leftward crossings are
negative.
To prove the lemma, it remains to observe that
the non-zero images of the pure tensors in these basis elements under
the multiplication
$OS^+ \otimes_\K OS^\circ \otimes_\K OS^-\rightarrow OS$ give a basis for $OS$
itself: it is just another of the bases from Theorem~\ref{bt}
consisting
of generic reduced lifts with all cups at the top, all crossings
of propagating strands in the middle, and all caps at
the bottom of the picture.
\end{proof}

Recall the Iwahori-Hecke algebras $H_r$ 
from (\ref{hecke}) and the homomorphism $\i_r$ from (\ref{iotap1}).
Theorem~\ref{bt} shows that this is an isomorphism.
More generally, let
\begin{equation}\label{belt}
H_{r,s} := H_r \otimes H_s
\end{equation}
for any $r,s \geq 0$. Then there is an injective (but no longer 
surjective) homomorphism
\begin{align}\label{iotap2}
\i_{r,s}
:
H_{r,s}
&\rightarrow 1_{\down^s\up^r} OS 1_{\down^s \up^r}
\end{align}
sending $S_i \otimes 1$ to the positive crossing 
$\begin{tikzpicture}[baseline = -.5mm]
	\draw[->,thick,darkblue] (0.2,-.2) to (-0.2,.3);
	\draw[line width=4pt,white,-] (-0.2,-.2) to (0.2,.3);
	\draw[thick,darkblue,->] (-0.2,-.2) to (0.2,.3);
\end{tikzpicture}
$ of the $i$th and $(i+1)$th strands
and $1 \otimes S_j$ to the positive crossing
$\begin{tikzpicture}[baseline = -.5mm]
	\draw[<-,thick,darkblue] (0.2,-.2) to (-0.2,.3);
	\draw[line width=4pt,white,-] (-0.2,-.2) to (0.2,.3);
	\draw[thick,darkblue,<-] (-0.2,-.2) to (0.2,.3);
\end{tikzpicture}
$ 
of the $(r+j)$th and $(r+j+1)$th
strands, again numbering strands from right to left.


\begin{lemma}\label{cartanlem}
The map $\i_{r,s}$ is an algebra isomorphism
$H_{r,s} \stackrel{\sim}{\rightarrow} 1_{\down^s \up^r} OS_{r,s}^\circ
1_{\down^s \up^r}.$
Moreover, $OS_{r,s}^\circ$ is isomorphic to the matrix algebra
$\Mat_{\binom{r+s}{r}}(H_{r,s})$.
Hence,
the functor $$
\Upsilon_{r,s} := 
? \otimes_{H_{r,s}} 1_{\down^s \up^r}
OS^\circ_{r,s}:\Mod{H_{r,s}} \rightarrow \Mod{OS^\circ_{r,s}}.
$$
is an equivalence of categories,
with quasi-inverse defined by right multiplication by the idempotent
$1_{\down^s \up^r}$.
\end{lemma}

\begin{proof}
The first statement follows from Theorem~\ref{bt}.
To deduce the second statement, let $\words_{r,s}$ denote the
$\binom{r+s}{r}$ different words which have $r$ letters $\up$ and $s$
letters $\down$. Note that $OS^\circ_{r,s} = \bigoplus_{\a,\b \in
  \words_{r,s}} 1_\a OS^\circ_{r,s} 1_\b$.
For each $\a,\b \in \words_{r,s}$, let $e_{\a,\b} \in 1_\a OS_{r,s}^\circ 1_\b$
be the unique (up to planar isotopy) reduced $(\b,\a)$-ribbon which only
involves positive rightward crossings and negative leftward crossings, and has no
cups, caps or upward/downward crossings. For example, $e_{\a,\a} = 1_\a$ for
each $\a$.
We have that $e_{\a,\b} e_{\b',\c} = \delta_{\b,\b'} e_{\a,\c}$.
Hence, the map
$$
H_{r,s} \rightarrow
1_\a OS^\circ_{r,s} 1_\b, \qquad
f \mapsto e_{\a,{\down^s \up^r}} \i_{r,s}(f) e_{{\down^s \up^r},\b}
$$
is a bijection, and
$OS^\circ_{r,s} = \bigoplus_{\a, \b \in \words_{r,s}} H_{r,s} e_{\a,\b}$ is the matrix algebra as claimed.
\end{proof}

Next we are going to mimic the usual arguments of highest weight theory for
semisimple Lie algebras, with the role of ``Borel subalgebra'' being
played by $OS^\sharp$, and the role of ``Cartan subalgebra'' being
played by $OS^\circ$.
To parametrize the isomorphism classes of
irreducible representations of $OS^\circ$, we need some
facts about the representation
theory of the Iwahori-Hecke algebra $H_r$; e.g. see \cite{DJ}. 

The algebra $H_r$ is semisimple
if $q$ is not a root of unity, with irreducible representations 
being the Specht modules $\SS_\lambda$
parametrized by partitions $\lambda \vdash r$.
To construct $\SS_\lambda$ explicitly, recall the elements $x_\lambda$
and $y_\lambda$
from (\ref{symmetrizers}).
The right ideals $x_\lambda H_r$ and $y_\lambda H_r$ are the {\em permutation module}
$M_\lambda$ and the {\em signed permutation module} $N_\lambda$,
respectively.
By \cite[Theorem 3.3]{DJ}, the space $\Hom_{H_r}(M_\lambda,
N_{\lambda^\trans})$ is one-dimensional. Then the {\em Specht module}
$\SS_\lambda$ is the image of any non-zero homomorphism in this space.

The definition just given also makes sense when $q$ is a root of unity (remembering
$q^2 \neq 1$); the resulting Specht module $\SS_\lambda$ 
is related to the module $\SS^\lambda$ constructed in \cite{DJ} by $\SS_\lambda \cong (\SS^{\lambda^\trans})^\#$.
In general, we define $e$ to be the smallest positive integer such
that $q^{2e}=1$,
setting $e := 0$ if $q$ is not a root of unity.
A partition $\lambda$ is {\em $e$-restricted} if either $e=0$, or $e >
0$ and $\lambda_i - \lambda_{i+1} < e$ for each $i=1,2,\dots$.
For $e$-restricted $\lambda\vdash r$, the Specht module $\SS_\lambda$ has
irreducible head $\D_\lambda$, and these modules for all $e$-restricted
$\lambda\vdash r$
give a complete set of pairwise inequivalent irreducible right
$H_r$-modules.

Let $\Y_\lambda$ be a projective cover of $\D_\lambda$; since $H_r$
is a symmetric algebra, this is
also an injective hull.
If $e=0$ we have simply that
$\D_\lambda=\SS_\lambda=\Y_\lambda$, and they are all equal to the right ideal
$e_\lambda H_r$ where $e_\lambda$ is the Young symmetrizer from
(\ref{youngsymmetrizer}).
In general, it is known
that $\Y_\lambda$ has a finite
filtration\footnote{This is proved by applying the ``Schur
functor'' to the analogous result for the
$q$-Schur algebra.} with sections $\SS_\mu$, each appearing
$[\SS_\mu:\D_\lambda]$ times.
Consequently,
\begin{equation*}
[\Y_\lambda] = \sum_{\mu \vdash r} [\SS_\mu:\D_\lambda] [\SS_\mu]
\end{equation*}
in the Grothendieck group $K_0(\fdMod H_r)$ of the Abelian category
$\fdMod H_r$.
We refer to this decomposition as {\em Brauer reciprocity};
it may also be proved by lifting idempotents.


Now let $\Par_{r,s} := \{\LA = (\lambda^\up,\lambda^\down)\:|\:\lambda\vdash r, \mu \vdash
s\}$ be the set of {\em bipartitions} of $(r,s)$,
and let $\RPar_{r,s} \subseteq \Par_{r,s}$ be the $e$-restricted ones.
In particular, we denote the empty bipartition
$(\varnothing,\varnothing)$ by $\NOTHING$.
From the previous paragraph, it follows that $\RPar_{r,s}$ parametrizes
the irreducible $H_{r,s}$-modules.
Applying Lemma~\ref{cartanlem}, we get from them irreducible $OS^\circ$-modules
\begin{equation}
\D(\LA):=
(\D_{\lambda^\up} \boxtimes \D_{\la^\down}) \otimes_{H_{r,s}} 1_{\down^s \up^r} OS^\circ_{r,s}.
\end{equation}
Define 
$\SS(\LA)$ 
for $\LA\in\Par_{r,s}$ and
$\Y(\LA)$ for $\LA\in\RPar_{r,s}$
in similar ways,
starting from $\SS_{\lambda^\up} \boxtimes \SS_{\la^\down}$ or $\Y_{\lambda^\up}\boxtimes
\Y_{\la^\down}$, respectively.
For $\LA\in\RPar_{r,s}$, $\Y(\LA)$ 
is a projective cover and an injective hull of $\D(\LA)$,
and it has a filtration with sections $\SS(\MU)$ for $\MU
\in \Par_{r,s}$, each appearing
$[\SS(\MU):\D(\LA)] = [\SS_{\mu^\up}:\D_{\la^\up}] [\SS_{\mu^\down}: \D_{\la^\down}]$
in the filtration.
Finally, we put these modules all together: setting
$\Par := \bigsqcup_{r,s \geq 0} \Par_{r,s}$ and
$\RPar := \bigsqcup_{r,s \geq 0} \RPar_{r,s}$,
the modules
$\{\D(\LA)\:|\:\LA \in \RPar\}$
are a complete set of pairwise inequivalent irreducible
$OS^\circ$-modules.

The projection of $OS^\sharp$ onto its degree zero component
$OS^\sharp[0]$ is a surjective homomorphism $OS^\sharp
\twoheadrightarrow OS^\circ$. Using this, we can view any $OS^\circ$-module
instead as an $OS^\sharp$-module. We denote the resulting
inflation
functor by $\infl^{\sharp}$; similarly, there is an inflation
functor
$\infl^{\flat}$ taking $OS^\circ$-modules to $OS^\flat$-modules.
Define
\begin{align}\label{eclipse1}
\bar\Delta(\LA) &:= \infl^{\sharp} \D(\LA) \otimes_{OS^\sharp} OS,
\\
\tilde\Delta(\LA) &:= \infl^\sharp \SS(\LA) \otimes_{OS^\sharp} OS,
\\
\Delta(\LA) &:= \infl^\sharp \Y(\LA) \otimes_{OS^\sharp} OS,\label{eclipse3}
\end{align}
for $\la \in \RPar, \Par$ and $\RPar$, respectively.
We call $\bar\Delta(\LA)$ the {\em proper standard module}
and $\Delta(\LA)$ the {\em standard module}
associated to $\LA \in \RPar$.
These are locally finite-dimensional but not ``globally'' finite-dimensional $OS$-modules.
Note also if $e=0$ that
$\bar\Delta(\LA)=\tilde\Delta(\LA)=\Delta(\LA)$
for each $\LA \in \Par$.

Any $OS$-module $M$ decomposes as $\bigoplus_{\a \in \words} M 1_\a$.
We refer to the direct sum of the subspaces $M 1_\a$ taken over all $\a \in \words$ of
minimal length such that $M 1_\a \neq 0$
as the {\em shortest word space} of $M$.
It is automatically an $OS^\sharp$-submodule of $M$ on which
$\bigoplus_{d > 0} OS^\sharp[d]$ acts as zero. We say that $M$ is a
{\em shortest word module} of type $\LA \in \RPar$ if $M$ is
generated as an $OS$-module by its shortest word space, and this space
is isomorphic to $\D(\LA)$ as an $OS^\circ$-module.
Then, since $\D(\LA)$ is irreducible, $M$ is actually
generated by any non-zero vector in its shortest word
space. 

\begin{theorem}\label{class}
For $\LA\in\RPar$, the proper standard module $\bar\Delta(\LA)$ has a unique
maximal submodule $\rad\,\bar\Delta(\LA)$.
Setting
$\L(\LA) := \bar\Delta(\LA) / \rad\,
\bar\Delta(\LA)$,
we obtain a complete set of pairwise inequivalent irreducible
$OS$-modules
$\{\L(\LA)\:|\:\LA\in\RPar\}$.
Moreover, each $\L(\LA)$ is absolutely irreducible.
\end{theorem}

\begin{proof}
By Lemma~\ref{td}, we have that
$\bar\Delta(\LA) = \D(\LA)
\otimes_{OS^\sharp}  OS 
=
\D(\LA) \otimes_\K OS^-$
as a right $\K$-module. Hence, it is a non-zero shortest word module
of type $\LA$.
Since any non-zero vector in $\D(\LA) \otimes OS^-[0]$ generates all of $\bar\Delta(\LA)$,
any proper submodule of $\bar\Delta(\LA)$ must be a subspace of 
$\bigoplus_{d < 0} \D(\LA) \otimes_\K OS^-[d]$.
This implies that the sum of all proper submodules
of $\bar\Delta(\LA)$ is itself proper, hence, it is the unique maximal submodule
$\rad\, \bar\Delta(\LA)$ of $\bar\Delta(\LA)$. 
Thus, the quotient modules $\L(\LA) := \bar\Delta(\LA) /
\rad\,\Delta(\LA)$
are irreducible.

Now let $L$ be any irreducible $OS$-module.
Pick an irreducible $OS^\circ$-submodule $L^\circ \cong \D(\LA)$ of its
shortest word space. Then by
Frobenius reciprocity we get an $OS$-module homomorphism
$\bar\Delta(\LA) \rightarrow L$
lifting an isomorphism $\D(\LA)\stackrel{\sim}{\rightarrow} L^\circ$. 
This map is surjective since $L$ is irreducible, hence, we get that $L \cong \L(\LA)$.

Finally, if $\L(\LA)\cong \L(\MU)$,
then their shortest word spaces must be isomorphic as $OS^\circ$-modules,
so $\LA=\MU$. Also, since $\End_{OS}(\L(\LA)) \cong \End_{OS^\circ}(\D(\LA))$, the absolute
irreducibility follows from the analogous assertion for Hecke algebras,
which is well known.
\end{proof}

\begin{example}\label{swex}
To illustrate ``shortest word theory,''
we use it to prove the existence of a non-zero homomorphism
$\bar\Delta(\MU)\rightarrow \bar\Delta(\LA)$
when $t = q^n$ for $n \in \NN$,
 $\LA := ((1^n), \varnothing)$ and
$\MU = ((1^{n+1}), (1))$.
The irreducible $OS^\circ_{n,0}$-module $\D(\LA)$
comes from the ``sign representation'' of $H_n$. So it 
is one-dimensional and is spanned by a vector
on which $1_{\up^n}$ acts as the identity and any
positive upward crossing acts as $-q^{-1}$.
Let $v$ be the generator of
$\bar\Delta(\LA) = \D(\LA)
\otimes_{OS^\sharp} OS$
defined by this vector tensored $1_{\up^n} \in OS$.
Also for $i,j=0,\dots,n$ define
$$
a_i := 
\mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,ultra thick,darkblue] (.7,-.3) to (.7,.5);
	\draw[->,ultra thick,darkblue] (.1,-.3) to (.1,.5);
        \draw[-,line width=4pt, white] (-.2,-.3) to [out=90,in=180] (.1,0);
        \draw[-,line width=4pt, white] (.1,0) to [out=0,in=90] (.4,-.3);
        \draw[<-,thick, darkblue] (-.2,-.3) to [out=90,in=180] (.1,0);
        \draw[-,thick,darkblue] (.1,0) to [out=0,in=90] (.4,-.3);
      \node at (.75,-.45) {$\scriptstyle n-i$};
      \node at (.1,-.45) {$\scriptstyle i$};
\end{tikzpicture}
},
\qquad\qquad
b_j := 
\mathord{
\begin{tikzpicture}[baseline =0mm]
	\draw[->,ultra thick,darkblue] (.7,-.3) to (.7,.5);
	\draw[->,ultra thick,darkblue] (.1,-.3) to (.1,.5);
        \draw[-,line width=4pt, white] (-.2,.5) to [out=-90,in=180] (.1,.1);
        \draw[-,line width=4pt, white] (.1,.1) to [out=0,in=-90] (.4,.5);
        \draw[-,thick, darkblue] (-.2,.5) to [out=-90,in=180] (.1,.1);
        \draw[->,thick,darkblue] (.1,.1) to [out=0,in=-90] (.4,.5);
      \node at (.75,-.45) {$\scriptstyle n-j$};
      \node at (.1,-.45) {$\scriptstyle j$};
\end{tikzpicture}
}\:.
$$
A calculation with relations shows that 
$$
v a_ib_j = \left\{\begin{array}{ll}
[n]_q v&\text{if $i=j$,}\\
q^n (-q)^{i-j+1}v&\text{if $i < j$,}\\
q^{-n} (-q)^{i-j-1}v&\text{if $i > j$.}
\end{array}\right.
$$
Now consider the vector 
$$
w := \sum_{i=0}^n (-q)^i v a_i \in \bar\Delta(\LA).
$$
This is non-zero by Lemma~\ref{td}.
We claim:
\begin{itemize}
\item[(1)]
$w b_j = 0$ for each $j=0,1,\dots,n$;
\item[(2)]
$w \i_{n+1,1}(S_i) = -q^{-1} w$ for $i=1,\dots,n$.
\end{itemize}
To see (1), we have that
$$
w b_j = \left[(-q)^j [n]_q + \sum_{i=0}^{j-1} q^n (-q)^{i-j+1} (-q)^i
+ \sum_{i=j+1}^n q^{-n} (-q)^{i-j-1} (-q)^i\right] v,
$$
which is zero since $[n]_q = \sum_{i=0}^{j-1} q^{-n+2i-2j+1} + \sum_{i=j+1}^n
q^{-n+2i-2j-1}$.
We leave the check of (2) to the reader.
It means that $w$ spans a one-dimensional $H_{n+1,1}$-submodule
of $\bar\Delta(\LA)$ isomorphic to its ``sign representation,''
so the $OS^\circ$-submodule generated by $w$ is a copy of $\D(\MU)$.
In view of (1), it is actually an $OS^\sharp$-submodule isomorphic to
$\infl^\sharp \D(\MU)$.
Finally,
by Frobenius reciprocity, we get
a non-zero $OS$-module homomorphism
$\bar\Delta(\MU)\rightarrow \bar\Delta(\LA)$.
\end{example}


The various flavors of standard module introduced in
(\ref{eclipse1})--(\ref{eclipse3})
are obtained by applying the {\em standardization functor}
\begin{equation}\label{sta}
\Delta := (\infl^\sharp -)\otimes_{OS^\sharp} OS:\Mod{OS^\circ} \rightarrow
\Mod{OS}
\end{equation}
to the $OS^\circ$-modules $\D(\LA), \SS(\LA)$ and $\Y(\LA)$.
By Lemma~\ref{td}, the composition of this functor followed by the forgetful
functor to vector spaces is isomorphic to $- \otimes_\K OS^-$. Hence, $\Delta$
is exact.
There is also the {\em costandardization functor}
\begin{equation}\label{costa}
\nabla:= \bigoplus_{\a \in \words} 
\Hom_{OS^\flat}(1_\a OS,
\infl^\flat -):
\Mod{OS^\circ}\rightarrow \Mod{OS},
\end{equation}
where the action of $a \in 1_\a OS 1_\b$ on $f \in
\Hom_{OS^\flat}(1_{\a'} OS, \infl^\flat M)$ is 
zero unless $\a=\a'$, in which case, 
it is the element of 
$\Hom_{OS^\flat}(1_\b OS, \infl^\flat M)$
defined from 
$(fa)(b) :=f(ab)$.
This functor is exact since 
$$
1_\a OS \cong 1_\a OS^+ \otimes_\K OS^\flat
\cong \bigoplus_{\b \in \words} \dim_\k(1_\a OS^+ 1_\b) 1_\b OS^\flat
$$ as a right
$OS^\flat$-module, which is finitely generated and projective.
We refer to the modules
\begin{equation}
\bar\nabla(\LA) := 
\nabla \D(\LA),\qquad
\nabla(\LA) := \nabla \Y(\LA)
\end{equation}
as the {\em proper costandard} and {\em costandard modules}, respectively.


There is a well-known duality functor $\circledast$ on finite-dimensional modules over the Hecke
algebra with $\D_\lambda^\circledast \cong \D_\lambda$, hence, $\Y_\lambda^\circledast \cong \Y_\lambda$. 
The corresponding duality $\circledast$ on $\fdMod OS^\circ$
takes a right module to its linear dual with the natural left action
twisted into a right action using the
antiautomorphism arising from the restriction of the isomorphism $\tau$ from (\ref{tau}).
In an entirely analogous way, $\tau$ gives rise to a duality, also
denoted $\circledast$, on the category
$\lfdMod OS$; this sends a module to the direct sum of the linear
duals of its word spaces.
Since $\D(\LA)^\circledast \cong \D(\LA)$ and $\Y(\LA)^\circledast \cong \Y(\LA)$, 
the following lemma implies that
\begin{align}\label{duality2}
\L(\LA)^\circledast &\cong \L(\LA),&
\Delta(\LA)^\circledast &\cong \nabla(\LA),&
\bar\Delta(\LA)^\circledast \cong \bar\nabla(\LA),
\end{align}
for any $\LA \in \RPar$. In particular, this means that $\L(\LA)$ can
also
be realized as the
irreducible socle of $\bar\nabla(\LA)$.

\begin{lemma}
The functors $\Delta$ and $\nabla$ send finite-dimensional
$OS^\circ$-modules to locally finite-dimensional $OS$-modules. Moreover,
the functors $\circledast \circ \Delta$ and $\nabla \circ \circledast$
are isomorphic on finite-dimensional $OS^\circ$-modules.
\end{lemma}

\begin{proof}
The first statement is easy to see from the definitions; for $\nabla$,
one needs to
know that $1_\a OS$ is a finitely generated right $OS^\flat$-module by Lemma~\ref{td}.
Then, for a finite-dimensional $OS^\circ$-module $M$, we define an $OS$-module homomorphism
$$
(\infl^\sharp M \otimes_{\OS^\sharp} OS)^\circledast\rightarrow
\bigoplus_{\a \in \words} \Hom_{OS^\flat}(1_\a OS, \infl^\flat (M^\circledast)),
\qquad
\theta \mapsto \widehat{\theta}
$$
where $\widehat{\theta}(f)(v) = \theta(v \otimes \tau(f))$
for $v \in M, f \in 1_\a OS$.
There is a two-sided inverse
$$
\bigoplus_{\a \in \words} \Hom_{OS^\flat}(1_\a OS, \infl^\flat
(M^\circledast))
\rightarrow
(\infl^\sharp M \otimes_{\OS^\sharp} OS)^\circledast,
\qquad
\psi \mapsto \widetilde{\psi}
$$
where $\widetilde{\psi}(v \otimes f) = \psi(\tau(f))(v)$.
\end{proof}

We say that an $OS$-module $M$ has a {\em finite $\Delta$-flag} if it has a
finite filtration whose sections are isomorphic to standard modules
$\Delta(\LA)$ for various $\LA \in \RPar$.
Let $\deltaMod OS$ be the full subcategory of
$\Mod OS$ consisting of all modules with a finite $\Delta$-flag.
We view it as an exact category with admissible sequences being the
ones that are exact in $\Mod OS$.
The next three lemmas are all well known in this sort of situation.

\begin{lemma}\label{rflat}
The restriction of $\Delta(\LA)$ to $OS^\flat$ is isomorphic to
$\Y(\LA) \otimes_{OS^\circ} OS^\flat$. These modules give all of the
indecomposable projective $OS^\flat$-modules (up to isomorphism).
\end{lemma}

\begin{proof}
The first statement is clear from Lemma~\ref{td}.
For the second, observe that
the $OS^\flat$-modules $\Y(\LA) \otimes_{OS^\circ} OS^\flat$ are induced
from the projective $OS^\circ$-modules, hence, they are projective and every
indecomposable projective $OS^\flat$-module is isomorphic to a summand of one of
them.
It remains to show that $\Y(\LA)\otimes_{OS^\circ} OS^\flat$ is
indecomposable. This follows because
$\End_{OS^\flat}(\Y(\LA) \otimes_{OS^\circ} OS^\flat)
\cong \End_{OS^\circ}(\Y(\LA))$, which is local as $\Y(\LA)$ is
indecomposable.
\end{proof}

In view of the following lemma, the Grothendieck group $K_0(\deltaMod
OS)$ of the exact category $\deltaMod OS$
is the free $\ZZ$-module on basis
$\{[\Delta(\LA)]\:|\:\LA \in \RPar\}$.

\begin{lemma}\label{fly}
For $\LA,\MU \in \RPar$ and $d \geq 0$, we have that
$$
\dim \operatorname{Ext}^d_{OS}(\Delta(\LA),\bar\nabla(\MU)) = 
\left\{
\begin{array}{ll}
1&\text{if $d=0$ and $\LA=\MU$,}\\
0&\text{otherwise.}
\end{array}
\right.
$$
Hence, for any $M \in \Mod OS$ with a finite $\Delta$-flag, the multiplicity
$(M:\Delta(\LA))$ of $\Delta(\LA)$ as a section of such a flag
is well defined independent of the particular choice of flag, and it satisfies
$(M:\Delta(\LA)) = \dim \Hom_{OS}(M, \bar\nabla(\LA))$.
\end{lemma}

\begin{proof}
For the first statement, we have natural isomorphisms
\begin{align*}
\operatorname{Ext}^d_{OS}(\Delta(\LA),\bar\nabla(\MU))
&\cong
\operatorname{Ext}^d_{OS}\Bigg(\Delta(\LA),
\bigoplus_{\a \in \words}
\Hom_{OS^\flat}\left(1_\a OS, \infl^\flat \D(\MU)\right)\Bigg)\\
&\cong
\operatorname{Ext}^d_{OS^\flat}(\Y(\LA) \otimes_{OS^\circ} OS^\flat,
\infl^\flat \D(\MU))\\
&\cong
\operatorname{Ext}^d_{OS^\circ}(\Y(\LA),
\D(\MU)).
\end{align*}
This is zero unless $\LA=\MU$ and $d=0$ as $\Y(\LA)$ is the projective
cover of $\D(\LA)$.
It follows that $\dim \Hom_{OS}(M,\bar\nabla(\LA))$ counts the
multiplicity of $\Delta(\LA)$ in a $\Delta$-flag of $M$, giving the
second statement.
\end{proof}

The next lemma shows that $\deltaMod OS$ is Karoubian.

\begin{lemma}\label{crit}
An $OS$-module $M$
has a finite $\Delta$-flag if and only if it is finitely generated and projective as an
  $OS^\flat$-module.
Hence, any direct summand of a module with a finite $\Delta$-flag also
has a finite $\Delta$-flag.
\end{lemma}

\begin{proof}
If $M$ has a finite $\Delta$-flag, then it is finitely generated and
projective over $OS^\flat$ thanks to Lemma~\ref{rflat}.
Conversely, suppose that $M$ is finitely generated and projective over
$OS^\flat$, so that the restriction of $M$ to $OS^\flat$
is isomorphic to a direct sum of some number $n$ of $OS^\flat$-modules of the form
$\Y(\LA)\otimes_{OS^\circ} OS^\flat$.
We show that $M$ has a finite $\Delta$-flag by induction on $n$.
The case $n=0$ is trivial.
If $n> 0$, we choose $r,s\geq 0$ with $r+s$ minimal
such that the restriction of $M$ to $OS^\flat$ has a summand $M'
\cong \Y(\LA)\otimes_{OS^\circ} OS^\flat$
for some $\LA \in \RPar_{r,s}$.
The $OS^\circ$-module homomorphism $\Y(\LA) \cong \Y(\LA) \otimes_{OS^\circ}
OS^\flat[0]
\hookrightarrow M'$ is actually an $OS^\sharp$-module
homomorphism $\infl^\sharp \Y(\LA) \hookrightarrow M$ since its image is
in the shortest word space of $M$. Hence, we get induced an $OS$-module
homomorphism $\Delta(\LA) \rightarrow M$ with image $M'$.
This shows that $M'$ is
actually an $OS$-submodule of $M$ and $M' \cong \Delta(\LA)$.
The quotient $M / M'$ is finitely generated and projective over
$OS^\flat$ with one fewer indecomposable summand.
It remains to apply the induction hypothesis to deduce that $M / M'$
has a finite $\Delta$-flag, hence, so does $M$.
\end{proof}

Now we look at projectives.
Let $\P(\LA)$ be a projective cover of $\L(\LA)$.
The classes $\{[\P(\LA)]\:|\:\LA \in \RPar\}$ give a basis for
$K_0(\pMod OS)$.
The $OS$-module 
\begin{equation}\label{qd}
\Q(\LA) := \Y(\LA) \otimes_{OS^\circ} OS
\end{equation}
described by the following theorem should be viewed as a first approximation
to $\P(\LA)$.

\begin{theorem}\label{koike1}
For $\LA \in \RPar_{r,s}$,
the module $\Q(\LA)$
has a canonical
filtration with sections indexed by $d=0,1,\dots,\min(r,s)$ appearing
in order from top to bottom, such that the $d$th section is isomorphic to
\begin{equation}\label{hmm}
\bigoplus_{\MU \in \RPar_{r-d,s-d}} 
\Delta(\MU)^{\oplus M^\LA_\MU(e,p)}
\end{equation}
where
$M^\LA_\MU(e,p) :=
\sum_{\NU \in \RPar_{d,d}}
\big[\D_{\mu^\up} \circ \D_{\nu^\up}:\D_{\lambda^\up}\big]
\big[\D_{\mu^\down} \circ \D_{\nu^\down}:\D_{\lambda^\down}\big]
[\Y_{\nu^\up}:\D_{\nu^\down}]$ (which depends on $e$ and the
characteristic $p$ of the field $\k$).
\end{theorem}

\begin{proof}
Take $0 \leq d \leq \min(r,s)$.
We always view $H_{d}$ as a subalgebra of $H_r$ or $H_s$ via the
natural embeddings.
We
also need the ``unnatural'' embeddings $H_{r-d} \hookrightarrow H_r$
and $H_{s-d}\hookrightarrow H_s$ 
which send $S_i \mapsto S_{d+i}$; the images of these embeddings
centralize $H_d$.
Let $\Hom_{H_d}(H_s,H_r)$ be the space of all right $H_d$-module
homomorphisms.
Using the unnatural embeddings for $H_{r-d}$ and $H_{s-d}$,
this is an $(H_r \otimes H_{s-d}, H_{r-d}\otimes H_s)$-bimodule.
Let $\tau\text{-\!}\Hom_{H_d}(H_s,H_r)$ be the 
the same space but with the left action of $H_{s-d}$ and right action of
$H_{s}$ twisted into right and left actions, respectively, using the
anti-automorphism $\tau$ which sends $S_w \mapsto
S_{w^{-1}}$.
This means that
$\tau\text{-\!}\Hom_{H_d}(H_s,H_r)$ is an $(H_{r,s}, H_{r-d,s-d})$-bimodule.
The space $1_{\down^s \up^r} OS^\sharp 1_{\down^{s-d} \up^{r-d}}$
is also naturally an $(H_{r,s}, H_{r-d,s-d})$-bimodule. 
We claim that these two bimodules are isomorphic.

To prove the claim, 
$H_s$ is a free right
$H_d$-module with basis $\{S_y\:|\:y \in \mathfrak{D}\}$ where $\mathfrak{D}$ is the set of
minimal length $\Sym_s / \Sym_d$-coset representatives.
So the $H_d$-module homomorphisms $\left\{f_{x,y}:H_s\rightarrow H_r\:|\:x \in \Sym_r, y \in \mathfrak{D}\right\}$
defined from
$f_{x,y}(S_z) := \delta_{y,z} S_x$
for $x\in\Sym_r, y,z \in \mathfrak{D}$
give a linear basis for $\tau\text{-\!}\Hom_{H_d}(H_s,H_r)$.
Let
$$
c := 
\mathord{
\begin{tikzpicture}[baseline = -6mm]
\node at (.2,-1.1) {$\scriptstyle r-d$};
\node at (-.25,-.05) {$\scriptstyle d$};
\node at (-.7,-1.1) {$\scriptstyle s-d$};
\draw[->,ultra thick,darkblue] (-.65,-.2) to (-.65,-1);
\draw[<-,ultra thick,darkblue] (.25,-.2) to (.25,-1);
\draw[-,line width=5pt,white] (.15,-.6) to [out=0,in=-90] (.55,-.2);
\draw[->,ultra thick,darkblue] (.15,-.6) to [out=0,in=-90] (.55,-.2);
\draw[-,ultra thick,darkblue] (-.25,-.2) to [out=-90,in=180] (.15,-.6);
\end{tikzpicture}
}
\in 1_{\down^s \up^r} OS^\sharp 
1_{\down^{s-d} \up^{r-d}},
$$
where the thick arrows labelled by a number represent that number of parallel thin ones.
We will show that
the linear map
$$
\theta:\tau\text{-\!}\Hom_{H_d}(H_s,H_r) \rightarrow
1_{\down^s \up^r} OS^\sharp 1_{\down^{s-d} \up^{r-d}},
\qquad
f_{x,y} \mapsto \i_{r,s}(S_x \otimes S_y) c
$$
is an $(H_{r,s}, H_{r-d,s-d})$-bimodule isomorphism.
To see this, it is clear from Theorem~\ref{bt} that $\theta$ is a vector
space isomorphism. We must check that it is a bimodule homomorphism.
This is straightforward for the left action of $H_r$ and the right
action of $H_{r-d}$. In the next two paragraphs, we check it for the
left action of $H_s$ and the right action of $H_{s-d}$, respectively.

To show $\theta$ is a left $H_s$-module
homomorphism, take $x \in \Sym_r, y \in \mathfrak{D}$ and $1 \leq i < s$.
By \cite[Lemma 1.1]{DJ}, exactly one of the following holds: (a) $s_i
y \in \mathfrak{D}$; (b) $s_{y^{-1}(i)} \in \Sym_d$.
In case (a), $S_i S_y = S_{s_i y}$ if $\ell(s_iy) > \ell(y)$
or $S_{s_i y} + (q-q^{-1}) S_y$ if $\ell(s_i y) < \ell(y)$.
In case (b), $S_i S_y = S_y S_{y^{-1}(i)}$
and $$
\i_{r,s}(S_x \otimes S_i S_y) c = 
\i_{r,s}(S_x \otimes S_y S_{y^{-1}(i)}) c
= \i_{r,s}(S_x S_{y^{-1}(i)} \otimes S_y) c.
$$
We deduce for $z \in \mathfrak{D}$ that
\begin{align*}
(\theta^{-1}(S_i &\theta(f_{x,y})))(S_z) = 
(\theta^{-1}( \i_{r,s}(S_x \otimes S_i S_y) c))(S_z)\\
&=
\left\{
\begin{array}{ll}
f_{x,s_i y}(S_z)&\text{if $s_i y \in \mathfrak{D}, \ell(s_i y) > \ell(y)$,}\\
(f_{x,s_i y} + (q-q^{-1}) f_{x,y})(S_z)&\text{if $s_i y \in \mathfrak{D}, \ell(s_i y) < \ell(y)$,}\\
f_{x s_{y^{-1}(i)},y}(S_z)&\text{if $s_i y \notin \mathfrak{D}, \ell(x s_{y^{-1}(i)}) > \ell(x)$,}\\
(f_{x s_{y^{-1}(i)},y}+(q-q^{-1}) f_{x ,y})(S_z)&\text{if $s_i y \notin \mathfrak{D}, \ell(x s_{y^{-1}(i)}) < \ell(x)$}
\end{array}
\right.\\
&=
\left\{
\begin{array}{ll}
\delta_{s_i y, z} S_x\hspace{36.8mm}&\text{if $s_i y \in \mathfrak{D}, \ell(s_i y) > \ell(y)$,}\\
\delta_{s_i y, z} S_x + (q-q^{-1}) \delta_{y,z} S_x&\text{if $s_i y \in \mathfrak{D}, \ell(s_i y) < \ell(y)$,}\\
\delta_{y,z} S_x S_{y^{-1}(i)}&\text{if $s_i y \notin \mathfrak{D}$}.
\end{array}
\right.
\end{align*}
We need to show this is equal to
$$
(S_i f_{x,y})(S_z) = f_{x,y}(S_i S_z) = 
\left\{
\begin{array}{ll}
\delta_{y,s_i  z} S_x&\text{if $s_i z \in \mathfrak{D}, \ell(s_i z) > \ell(z)$},\\
\delta_{y,s_i  z} S_x + (q-q^{-1}) \delta_{y,z} S_x&\text{if $s_i z \in \mathfrak{D}, \ell(s_i z) < \ell(z)$},\\
\delta_{y,z} S_x S_{y^{-1}(i)}&\text{if $s_i z \notin \mathfrak{D}$}.\\
\end{array}\right.
$$
This follows easily by considering several cases: (a) $y = z$; (b) $y = s_i
z$; (c) $s_i y = z$; (d) none of the above.

To show that $\theta$ is a right $H_{s-d}$-module homomorphism,
take $x \in \Sym_r, y, z \in \mathfrak{D}$ and $1 \leq i < s-d$.
We must show that
$(\theta^{-1}(\theta(f_{x,y}) S_i))(S_z)
= (f_{x,y} S_{d+i}) (S_z)$, i.e.,
$$
(\theta^{-1}(\i_{r,s}(S_x \otimes S_y S_{d+i})c)(S_z)
=
f_{x,y}(S_z S_{d+i}).
$$
This time, 
$y s_{d+i} \in \mathfrak{D}$ always.
So the left hand side of the identity to be proved equals
$$
\left\{\begin{array}{ll}
\delta_{y s_{d+i}, z} S_x
&\text{if $\ell(y s_{d+i}) > \ell(y)$,}\\
\delta_{y s_{d+i}, z}S_x + \delta_{y,z} (q-q^{-1})S_x&\text{if $\ell(y s_{d+i}) < \ell(y)$.}
\end{array}\right.
$$
Similarly, the right hand side is
$$
\left\{\begin{array}{ll}
\delta_{y,z s_{d+i}} S_x
&\text{if $\ell(z s_{d+i}) > \ell(z)$,}\\
\delta_{y, z s_{d+i}}S_x + \delta_{y,z} (q-q^{-1})S_x\:&\text{if $\ell(z s_{d+i}) < \ell(z)$.}
\end{array}\right.
$$
The two sides are equal by considering four cases like before.

We have now proved the claim made in the opening paragraph.
To prove the theorem, we must construct the filtration of $\Q(\LA)$.
By transitivity of induction,  
$$
\Q(\LA) = (\Y(\LA) \otimes_{OS^\circ} OS^\sharp) \otimes_{OS^\sharp} OS.
$$
Since $OS^\sharp$ is positively graded, the grading gives us a filtration of 
$\Y(\LA)
\otimes_{OS^\circ} OS^\sharp$ as an $OS^\sharp$-module
with sections $\Y(\LA) \otimes_{OS^\circ} OS^\sharp[d]$ for $d=0,1,\dots$
appearing in order from top to bottom. The $d$th section is clearly zero unless $d
\leq \min(r,s)$.
Since the functor $? \otimes_{OS^\sharp} OS$ is exact, we are thus reduced
to checking
for $0 \leq d \leq \min(r,s)$ that
$$
\Y(\LA) \otimes_{OS^\circ} OS^\sharp[d] \cong
\bigoplus_{\MU \in \RPar_{r-d,s-d}} 
\Y(\MU)^{\oplus M^\LA_\MU(e,p)}
$$
as a right $OS^\circ$-module.
Using Lemma~\ref{cartanlem}, we show equivalently that
$$
(\Y_{\la^\up} \boxtimes \Y_{\la^\down}) \otimes_{H_{r,s}}
1_{\down^s\up^r} OS^\sharp 1_{\down^{s-d}\up^{r-d}}
\cong \bigoplus_{\mu \in \RPar_{r-d,s-d}} (\Y_{\mu^\up} \otimes
\Y_{\mu^\down})^{\bigoplus M^\LA_\MU(e,p)}
$$
as a right $H_{r-d,s-d}$-module.
By the opening claim, the module on the left hand side is isomorphic
to
$$
(\Y_{\la^\up} \boxtimes \Y_{\la^\down}) \otimes_{H_{r,s}}
\tau\text{-\!}\Hom_{H_d}(H_s,H_r)
\cong 
\tau\text{-\!}\Hom_{H_d}(\Y_{\la^\down},\Y_{\la^\up}),
$$
where we have used the self-duality of $\Y_{\la^\down}$.
Then we note by Frobenius reciprocity
that
\begin{align*}
\res^{H_r}_{H_{r-d,d}} \Y_{\la^\up} &\cong
\bigoplus_{\mu^\up \vdash (r-d), \nu^\up \vdash d} 
(\Y_{\mu^\up} \boxtimes \Y_{\nu^\up})^{\oplus
[\D_{\mu^\up}\circ \D_{\nu^\up}:\D_{\la^\up}]},\\
\res^{H_s}_{H_{s-d,d}} \Y_{\la^\down} &\cong
\bigoplus_{\mu^\down \vdash (s-d), \nu^\down \vdash d} 
(\Y_{\mu^\down} \boxtimes  \Y_{\nu^\down})^{\oplus [\D_{\mu^\down}\circ \D_{\nu^\down}:\D_{\la^\down}]}.
\end{align*}
Making these substitutions in
$\tau\text{-\!}\Hom_{H_d}(\Y_{\la^\down},\Y_{\la^\up})$, using also
$\dim \Hom_{H_d}(\Y_{\nu^\down}, \Y_{\nu^\up}) = \left[\Y_{\nu^\up}:\D_{\nu^\down}\right]$
and self-duality of $\Y_{\mu^\down}$, gives the conclusion.
\end{proof}

\begin{corollary}\label{kio}
For $\LA \in \RPar_{r,s}$, the module $\Q(\LA)$ is isomorphic
$\P(\LA)$ plus a finite direct sum of projectives
$\P(\MU)$ for bipartitions $\MU \in \bigsqcup_{d = 0}^{\min(r,s)-1}
\RPar_{r-d,s-d}$.
Hence, the classes $\{[\Q(\LA)]\:|\:\LA \in \RPar\}$ give another basis for
$K_0(\pMod OS)$.
\end{corollary}

\begin{proof}
Note that $\Q(\LA)$ is projective since the
functor
$? \otimes_{OS^\circ} OS$ sends projectives to projectives.
Also the top section of the $\Delta$-flag of $\Q(\LA)$ constructed in Theorem~\ref{koike1}
is $\Delta(\LA)$, so $\Q(\LA)$ has $\P(\LA)$ as an indecomposable summand.
The other sections only involve 
$\Delta(\MU)$ for $\MU \in \bigsqcup_{d = 0}^{\min(r,s)-1} \Par_{r-d,s-d}$,
so all other summands are of the form $\P(\MU)$ for such $\MU$.
\end{proof}

\begin{corollary}\label{BGG}
The projective cover $\P(\LA)$ of $\L(\LA)$ has a finite $\Delta$-flag
such that
$$
(\P(\LA):\Delta(\MU)) =[\bar\Delta(\MU):\L(\LA)].
$$
 \end{corollary}

\begin{proof}
By Corollary~\ref{kio} and Theorem~\ref{koike1}, $\P(\LA)$ is a summand of $\Q(\LA)$, and $\Q(\LA)$ has
a finite $\Delta$-flag.
Hence, $\P(\LA)$ has one too due to Lemma~\ref{crit}.
To deduce the BGG reciprocity formula, 
we use Lemma~\ref{fly}:
$
(\P(\LA):\Delta(\MU))=
\dim \Hom_{OS}(\P(\LA), \bar\nabla(\MU)) = [\bar\nabla(\MU):\L(\LA)].
$
This equals $[\bar\Delta(\MU):\L(\LA)]$ by (\ref{duality2}).
\end{proof}

\begin{corollary}\label{exactsubcat}
By Corollary~\ref{BGG}, there is an embedding $\pMod OS \rightarrow\deltaMod OS$.
This induces an
isomorphism
$K_0(\pMod OS) \stackrel{\sim}{\rightarrow} K_0(\deltaMod OS)$.
\end{corollary}

\begin{proof}
The transition matrix arising from (\ref{hmm}) can
be inverted to express each $[\Delta(\LA)]$ as a finite linear
combination of $[\Q(\MU)]$'s.
\end{proof}

\begin{corollary}\label{BGGplus}
For $\LA \in \RPar_{r,s}$, $\P(\LA)$ has a finite filtration with sections $\tilde\Delta(\MU)$ for
$\MU \in \bigsqcup_{d=0}^{\min(r,s)}\Par_{r-d,s-d}$, 
each appearing $[\tilde\Delta(\MU):\L(\LA)]$
times.
\end{corollary}

\begin{proof}
Recall for $\LA \in \RPar_{r,s}$ 
that $\Y(\LA)$ has a finite filtration with sections $\SS(\MU)$, each
appearing $[\SS(\MU):\D(\LA)]$ times.
Applying the exact standardization functor, we deduce that
$\Delta(\LA)$ has a finite filtration with sections
$\tilde\Delta(\MU)$, each
appearing $[\SS(\MU):\D(\LA)]$ times.
Combined with Corollary~\ref{BGG}, it follows that $\P(\LA)$ has a finite
filtration with sections $\tilde\Delta(\MU)$, each appearing 
with multiplicity
$$
\sum_{\NU \in \RPar} [\bar\Delta(\NU):\L(\LA)] [\SS(\MU):\D(\NU)].
$$
Also, applying $\Delta$ to a composition series of $\SS(\MU)$, we see
that 
$\tilde\Delta(\MU)$ has a filtration with sections
$\bar\Delta(\NU)$, each appearing $[\SS(\MU):\D(\NU)]$ times.
Hence, the multiplicity just displayed is equal to
$[\tilde\Delta(\MU):\L(\LA)]$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{delection}]
The monoidal functor $\OS{^\circ}(z,t) \rightarrow \OS(z,t)$
corresponds to the induction functor
$?\otimes_{OS^\circ} OS:\pMod OS^\circ \rightarrow \pMod OS$, since the latter
sends $e OS^\circ$ to $e OS$ for any idempotent $e$.
So by the definition (\ref{qd}) it sends $\Y(\LA)$ to $\Q(\LA)$.
Theorem~\ref{delection} follows because 
the classes
$\left\{[\Q(\LA)]\:|\:\LA \in \RPar\right\}$
form a basis for $K_0(\pMod OS)$ according to Corollary~\ref{kio}.
\end{proof}

For the next lemma, we return to the situation of
Theorem~\ref{webs}.
We want to relate the labelling of irreducible $OS$-modules obtained
thus far with the usual labelling of irreducible
$U_q(\mathfrak{gl}_{n})$-modules
via their highest weights.
Take $\LA \in \Par_{r,s}$.
Since $e=0$, Theorem~\ref{koike1} tells us simply that $\Q(\LA)$ has a
filtration with sections 
\begin{equation}\label{koike3}
\bigoplus_{\MU \in \Par_{r-d,s-d}}
\Delta(\MU)^{\oplus M^\LA_\MU}
\qquad\text{where}\qquad
M^\LA_\MU:= M^\LA_\MU(0,0) =
\sum_{\nu \vdash d}
LR^{\lambda^\up}_{\mu^\up, \nu}
LR^{\lambda^\down}_{\mu^\down, \nu}
\end{equation}
for $d=0,\dots,\min(r,s)$,
and it decomposes as $\P(\LA)$ plus a direct sum of projectives
$\P(\MU)$ for various bipartitions $\MU$ obtained from $\LA$ by
removing the same number $d > 0$
of boxes from both $\la^\up$ and $\la^\down$.
Recalling 
the Young symmetrizer (\ref{youngsymmetrizer}),
we have that $\Y(\LA) = \SS(\LA) = \D(\LA) = \i_{r,s}(e_{\la^\up} \otimes
e_{\la^\down}) OS^\circ$. Hence,
\begin{equation}\label{youngsymmetrizer2}
\Q(\LA) = \i_{r,s}(e_{\la^\up} \otimes
e_{\la^\down}) OS.
\end{equation}
Let $e_\LA$ 
be the projection of $\Q(\LA)$ onto its unique summand that
is isomorphic to $\P(\LA)$. Thus,
$e_\LA$ is a primitive idempotent in the quantized walled Brauer algebra
$B_{r,s}$. The following recovers results of \cite{KM1, KM2}.

\begin{lemma}\label{koike2}
Let  notation be as in Theorem~\ref{webs} and assume $n \geq 0$.
Take $\LA \in \Par_{r,s}$ such that $h(\LA)$, its total number of non-zero
parts, is $\leq n$.
Consider the idempotent $\Psi(e_\LA)\in
\End_{U_q(\mathfrak{gl}_{n})}\left((V^-)^{\otimes s}
  \otimes (V^+)^{\otimes r}\right)$.
Its image is the irreducible $U_q(\mathfrak{gl}_{n})$-module $\V(\LA)$ labelled by
the dominant weight
\begin{equation}\label{displayed}
(\la_1^\up-\la_{n}^\down) \eps_1+(\la_2^\up-\la_{n-1}^\down)\eps_2+\cdots + (\la_{n}^\up-\la_1^\down)
\eps_{n},
\end{equation}
using standard conventions for the root system of $\mathfrak{gl}_{n}$.
\end{lemma}

\begin{proof}
We proceed by induction on $r+s$, the case $r+s=0$ being trivial.
Since $e_{\lambda^\up}$ is the Young symmetrizer, the image of
$\Psi(e_{\lambda^\up})\in \End_{U_q(\mathfrak{gl}_{n})}\left((V^+)^{\otimes
    r}\right)$
is the irreducible polynomial representation 
$\V(\la^\up)$ of $U_q(\mathfrak{gl}_{n})$
of highest weight $\lambda_1^\up\eps_1+\cdots+\lambda_{n}^\up\eps_{n}$.
Similarly, the image of $\Psi(e_{\lambda^\down})$ is the dual
irreducible polynomial representation 
$\V(\la^\down)^*$ of highest weight 
$-\la_{n}^\down \eps_1+\cdots+\la_1^\down\eps_{n}$.
Hence, the image of 
$\Psi(\i_{r,s}(e_{\la^\up} \otimes
e_{\la^\down}))$ 
is 
$\V(\la^\down)^* \otimes \V(\la^\up)$.
Using characters, it is easy to see that this tensor product has a unique irreducible
constituent $\V(\LA)$ of
highest weight (\ref{displayed}), plus a sum of irreducible
modules $\V(\MU)$ for bipartitions
$\MU \in \bigsqcup_{d > 0}\Par_{r-d,s-d}$ with $h(\MU) \leq n$.
Now using induction, we deduce that $\Psi(e_\LA)$ must be the
projection onto $\V(\LA)$.
\end{proof}

\begin{remark}
A helpful picture of the weight (\ref{displayed}) is displayed in
\cite[Figure 2]{Koike}. It is also worth noting that multiplicities
$M^\LA_\MU$
appearing in (\ref{koike3}) are the same as the 
$U_q(\mathfrak{gl}_{n})$-composition multiplicities $[\V(\la^\down)^* \otimes \V(\la^\up):\V(\MU)]$
computed in \cite[Corollary 2.3.1]{Koike}.
Given this, the same induction as used to prove Lemma~\ref{koike2}
can be used to show that $\Delta(\LA) = \P(\LA)$ when in the situation
of the lemma.
We will prove this in a different way in Corollary~\ref{morocco} below.
\end{remark}

\begin{remark}
To get the appropriate analog of Lemma~\ref{koike2} when $n \leq 0$, 
one just needs to twist by the isomorphism $\#$. 
Recalling at the level of the Hecke algebra that this is ``tensoring
with sign,''
one can show that $\#$ 
maps
the primitive idempotent 
$e_\LA$ to a conjugate of
$e_{\LA^\trans}$, where $\LA^t := \left((\la^\up)^\trans,
  (\la^\down)^\trans\right)$.
So, for negative $n$,
the $U_q(\mathfrak{gl}_n)$-module
$V(\LA)$ arises as the image of $\Psi(e_{\LA^\trans})$ (instead of $\Psi(e_\LA)$).
\end{remark}

The final result in the section justifies the description of $K_0(\dot\OS(z,t))$
made after Theorem~\ref{delection} in the introduction; the discussion
there also depends on Theorem~\ref{selection} which will be proved in the
next section, and the highest weight/standardly stratified structure
which will be explained in section~\ref{tpc}.

\begin{lemma}\label{commute}
For $\LA \in \RPar_{r,s}$ and $\NU \in \Par_{r-d,s-d}$, we have that
$$
\sum_{\MU \in \Par_{r,s}} [\SS(\MU):\D(\LA)] M^\MU_\NU
=
\sum_{\MU \in \RPar_{r-d,s-d}} M^\LA_\MU(e,p) [\SS(\NU):\D(\MU)].
$$
\end{lemma}

\begin{proof}
We have that
$$
\sum_{\MU \in \RPar_{r-d,s-d}} M^\LA_\MU(e,p) [\SS(\NU):\D(\MU)]\hspace{65mm}
$$ \vspace{-7mm}
\begin{align*}
\qquad\qquad&=
\sum_{\substack{\MU \in \RPar_{r-d,s-d}\\\KAPPA \in \RPar_{d,d}, \gamma
  \vdash d}}
\begin{array}{l}
\\
\big[\D_{\mu^\up} \circ \D_{\kappa^\up}:\D_{\la^\up}\big]
\big[\SS_{\nu^\up}:\D_{\mu^\up}\big]
\big[\SS_\gamma:\D_{\kappa^\up}\big]\times\\
\qquad\qquad\qquad\big[\D_{\mu^\down} \circ \D_{\kappa^\down}:\D_{\la^\down}\big]
\big[\SS_{\nu^\down}:\D_{\mu^\down}\big]
\big[\SS_\gamma:\D_{\kappa^\down}\big]
\end{array}
\\
&=
\sum_{\substack{\KAPPA \in \RPar_{d,d}, \gamma
  \vdash d}}\big[\SS_{\nu^\up} \circ \D_{\kappa^\up}:\D_{\la^\up}\big]
\big[\SS_\gamma:\D_{\kappa^\up}\big]
\big[\SS_{\nu^\down} \circ \D_{\kappa^\down}:\D_{\la^\down}\big]
\big[\SS_\gamma:\D_{\kappa^\down}\big]\\
&=
\qquad\sum_{\gamma
  \vdash d}\big[\SS_{\nu^\up} \circ \SS_\gamma:\D_{\la^\up}\big]
\big[\SS_{\nu^\down} \circ \SS_\gamma:\D_{\la^\down}\big]\\
&=
\:\,\sum_{\substack{\MU \in \Par_{r,s}, \gamma
  \vdash d}}\big[\SS_{\nu^\up} \circ \SS_\gamma:\SS_{\mu^\up}\big]
\big[\SS_{\mu^\up}:\D_{\lambda^\up}]
\big[\SS_{\nu^\down} \circ \SS_{\gamma}:\SS_{\mu^\down}\big]
\big[\SS_{\mu^\down}:\D_{\lambda^\down}]\\
&=
\quad\sum_{\MU \in \Par_{r,s}}
[\SS(\MU):\D(\LA)]M^\MU_\NU.
\end{align*}
\end{proof}

\begin{theorem}\label{thegg}
For any choices of $q$ and $t$, 
the ring $K_0(\pMod OS)$ may be identified with a
subring of $\SYM\otimes_\ZZ\SYM$ so that (\ref{k0b}) 
and (\ref{k0c}) hold.
\end{theorem}

\begin{proof}
When $e=0$, 
Lemma~\ref{cartanlem} and the well-known representation theory of Hecke
algebras
imply that the rings
$K_0(\pMod OS^\circ)$ and $\SYM\otimes_\ZZ \SYM$ 
may be identified so that 
$[\SS(\LA)] \leftrightarrow \chi_{\la^\up}\otimes \chi_{\la^\down}.$
For general $e$, using also Brauer reciprocity for the Hecke algebra, we may identify
 $K_0(\pMod OS^\circ)$ with a subring of
$\SYM\otimes_\ZZ\SYM$
so that $$
[\Y(\LA)] \leftrightarrow \sum_{\MU \in \Par_{r,s}} [\SS(\MU):\D(\LA)]
\chi_{\mu^\up}\otimes \chi_{\mu^\down}
$$
for $\LA \in \RPar_{r,s}$ and $r,s\geq 0$.
In view of Theorem~\ref{delection} (and its proof), we deduce that
$K_0(\pMod OS)$ is identified with a subring of $\SYM\otimes_\ZZ\SYM$ so that
$$
[\Q(\LA)] \leftrightarrow  
\sum_{\MU \in \Par_{r,s}} [\SS(\MU):\D(\LA)]
\chi_{\mu^\up}\otimes \chi_{\mu^\down}
$$
for $\LA \in \RPar_{r,s}$ and $r,s\geq 0$.
Now recall the definition (\ref{nlamu}) and (\ref{koike3}).
Setting $N^\LA_\MU = M^\LA_\MU := 0$ whenever $\LA \in \Par_{r,s}$ and 
$\MU \notin \bigsqcup_{d=0}^{\min(r,s)} \Par_{r-d,s-d}$,
the matrix 
$(N^\LA_\MU)_{\LA,\MU \in \Par}$ is inverse to the matrix
$(M^\LA_\MU)_{\LA,\MU \in \Par}$ by 
\cite[Theorem 2.3]{Koike}.
So
$$
[\Q(\LA)] \leftrightarrow  
\sum_{\substack{\MU \in \Par_{r,s}\\0 \leq d \leq \min(r,s)\\\NU \in \Par_{r-d,s-d}}} [\SS(\MU):\D(\LA)] M^\MU_\NU \chi_\NU
$$
for $\LA \in \RPar_{r,s}$ and $r,s \geq 0$.
By Lemma~\ref{commute}, this gives
$$
[\Q(\LA)] \leftrightarrow
\sum_{\substack{0 \leq d \leq \min(r,s)\\\LA \in \RPar_{r-d,s-d}\\\NU
    \in \Par_{r-d,s-d}}} 
M^\LA_\MU(e,p) [\SS(\NU):\D(\MU)] \chi_\NU.
$$
Now use Corollary~\ref{exactsubcat} to identify
$K_0(\pMod OS) = K_0(\deltaMod OS)$.
Comparing with (\ref{hmm}), we deduce that
$$
[\Delta(\LA)] \leftrightarrow
\sum_{\NU \in \Par_{r,s}}
[\SS(\NU):\D(\LA)] \chi_\NU
$$
for $\LA \in \RPar_{r,s}$.
This establishes (\ref{k0b}).
To get (\ref{k0c}) too, use
Corollary~\ref{BGG}.
\end{proof}
