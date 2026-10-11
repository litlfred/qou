---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-034-8-modifications-in-the-degenerate-case
section_title: "Modifications in the degenerate case"
section_number: 8
pages: 54-56
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
\label{sdeg}

Assume in this section that $\k$ is a field of characteristic $p \geq 0$.
As we have said already in the introduction, when $z=0$, the
category $\OS(z,t)$ should be replaced with the oriented Brauer
category $\OB(\delta)$ studied in \cite{BCNR}.

\begin{proof}[Proof of Theorem~\ref{websup}]
This follows by the same general argument as used to prove Theorem~\ref{webs} (also
Remark~\ref{websrem}).
Instead of the quantized Schur-Weyl duality used before, one uses classical 
Schur-Weyl duality in its ``characteristic free'' form
established in \cite[Theorems 4.1--4.2]{dCP}.
\end{proof}

Now we discuss the degenerate analog of the results in sections 5, 6 and 7.

For section 5, we work with the locally finite-dimensional locally unital algebra
$$
OB = \bigoplus_{\a,\b \in \words} 1_\a OB 1_\b
\qquad\text{where}\qquad
1_\a OB 1_\b = \Hom_{\OB(\delta)}(\b,\a).
$$
It has a triangular decomposition $$
OB \cong OB^+ \otimes_\K OB^0
\otimes_\K OB^-$$ 
like in Lemma~\ref{td}. This actually becomes 
easier since there is no longer any need to be careful about upward strands passing
underneath downward strands when defining $OB^0$.
The subsequent arguments in section 5 then
go through easily on replacing the Hecke algebra $H_r$ with the
group algebra $\k \Sym_r$ of the symmetric group
and $e$ with $p$.

The results in section 6 go through too, but this needs a little more
work since the definitions of the various Jucys-Murphy elements from
(\ref{arun}), (\ref{JMstupid}) and
(\ref{chile2})--(\ref{chile5}) need some modifications, and the
details in the proofs of Lemmas~\ref{fur} and \ref{newz} then
need to be rechecked carefully.
The affine Hecke algebra $AH_r$ becomes the {\em degenerate affine
  Hecke algebra} $dAH_r$ whose polynomial generators $x_1,\dots,x_r$
satisfy the relations
\begin{align}
x_i x_j &= x_j x_i,
&
s_i x_{i+1} &= x_i s_i + 1
\end{align}
in place of (\ref{AHR}).
The unique homomorphism $dAH_r \twoheadrightarrow \k \Sym_r$
sending $s_i \mapsto s_i$ and $x_1 \mapsto 0$ 
sends $x_r$ to the {\em Jucys-Murphy element}
\begin{equation}
\jm_r := \sum_{i=1}^{r-1} (i\:\:r) \in \k \Sym_r.
\end{equation}
These elements are the replacements for (\ref{JMstupid}).
Then the contents of nodes of an ordinary Young diagram (which should
always be interpreted as
elements of the field $\k$) are as in the
following example
$$
\diagram{$ 0$&$ 1$&$2$&$3$&$4$\cr $
  -1$&$ 0$&$1$\cr
  $ -2$ & $ -1$ \cr}.
$$
In place of (\ref{Ic}), we set
\begin{equation}\label{Id}
I_c := \{c + n\:|\:n \in \ZZ\}  \subseteq \k
\end{equation}
for $c \in \k$.
The appropriate analog of Lemma~\ref{classical} uses $I_{0} \subseteq \k$ in
place of $I_1 \subseteq \k^\times$. 
It is a classical result in the (modular) representation theory of the
symmetric group.

The Jucys-Murphy elements of $\OB(\delta)$
are the images of corresponding elements of the
{\em affine oriented Brauer category} $\AOB(\delta)$ introduced in
\cite{BCNR}. This strict $\k$-linear monoidal category is defined by
by adjoining an additional generating
morphism $\mathord{
\begin{tikzpicture}[baseline = -1mm]
      \node at (0,0) {$\color{darkblue}\scriptstyle\bullet$};
	\draw[<-,thick,darkblue] (0,0.25) to (0,-0.25);
\end{tikzpicture}
}$ to $\OB(\delta)$,
subject to the relation ($\text{dA}$) from Figure 1.
The analog of Lemma~\ref{notmon} is explained in \cite[Theorem
3.3]{BCNR}: there is a $\k$-linear functor
$\beta:\AOB(\delta)\rightarrow \OB(\delta)$ sending diagrams with no dots to
the same diagrams in $\OB(\delta)$, and sending $\mathord{
\begin{tikzpicture}[baseline = -1mm]
      \node at (0,0) {$\color{darkblue}\scriptstyle\bullet$};
	\draw[<-,thick,darkblue] (0,0.25) to (0,-0.25);
\end{tikzpicture}
}\mapsto 0$.
The following computes the image of
$\mathord{
\begin{tikzpicture}[baseline = -1mm]
      \node at (0,0.025) {$\color{darkblue}\scriptstyle\bullet$};
	\draw[->,thick,darkblue] (0,0.25) to (0,-0.25);
\end{tikzpicture}
}$ (which is defined so that (\ref{d5})--(\ref{d4}) hold):
$$
\mathord{
\begin{tikzpicture}[baseline = -0.5mm]
	\draw[->,thick,darkblue] (0,0.6) to (0,-0.6);
     \node at (0,0) {$\color{darkblue}\bullet$};
\end{tikzpicture}
}
=
\mathord{
\begin{tikzpicture}[baseline = -0.5mm]
	\draw[-,thick,darkblue] (0,0.6) to (0,0.3);
	\draw[-,thick,darkblue] (0,0.3) to [out=-90,in=180] (.3,-0.2);
	\draw[-,thick,darkblue] (0.3,-0.2) to [out=0,in=-90](.5,0);
	\draw[-,thick,darkblue] (0.5,0) to [out=90,in=0](.3,0.2);
	\draw[-,thick,darkblue] (0.3,.2) to [out=180,in=90](0,-0.3);
	\draw[->,thick,darkblue] (0,-0.3) to (0,-0.6);
      \node at (0,.4) {$\color{darkblue}\bullet$};
\end{tikzpicture}
}
=
\mathord{
\begin{tikzpicture}[baseline = -0.5mm]
	\draw[-,thick,darkblue] (0,0.6) to (0,0.3);
	\draw[-,thick,darkblue] (0,0.3) to [out=-90,in=180] (.3,-0.2);
	\draw[-,thick,darkblue] (0.3,-0.2) to [out=0,in=-90](.5,0);
	\draw[-,thick,darkblue] (0.5,0) to [out=90,in=0](.3,0.2);
	\draw[-,thick,darkblue] (0.3,.2) to [out=180,in=90](0,-0.3);
	\draw[->,thick,darkblue] (0,-0.3) to (0,-0.6);
      \node at (0.48,.02) {$\color{darkblue}\bullet$};
\end{tikzpicture}
}
-
\mathord{
\begin{tikzpicture}[baseline = -0.5mm]
	\draw[->,thick,darkblue] (0,0.6) to (0,-0.6);
\end{tikzpicture}
}
\:\:\:\mathord{
\begin{tikzpicture}[baseline = 1.25mm]
  \draw[-,thick,darkblue] (0.2,0.2) to[out=90,in=0] (0,.4);
  \draw[-,thick,darkblue] (0,0.4) to[out=180,in=90] (-.2,0.2);
\draw[-,thick,darkblue] (-.2,0.2) to[out=-90,in=180] (0,0);
  \draw[->,thick,darkblue] (0,0) to[out=0,in=-90] (0.2,0.2);
\end{tikzpicture}
}\:\mapsto\:
-\delta\:
\mathord{
\begin{tikzpicture}[baseline = -0.5mm]
	\draw[->,thick,darkblue] (0,0.6) to (0,-0.6);
\end{tikzpicture}
}\,.
$$
Then we define $x(\b) \in \Hom_{\OB(\delta)}(\b,\b)$ in the same way as (\ref{JM})
for any $\varnothing \neq \b \in \words$.
There is no longer such a nice diagrammatic interpretation of these
elements like (\ref{arun}), but there
is a recursive definition as in (\ref{JMa})--(\ref{JMb}): we have that
$x(\up) = 0, x(\down) = -\delta 1_\down$, and 
\begin{align}\label{JManew}
x(\up \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.16,.3) {$\scriptstyle x(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.08,.3) rectangle ++(24pt,10pt);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}
+
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,-.3) to (-.3,.9);
\draw[->,thick,darkblue] (-.3,-.3) to (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}\,,
&
x(\up \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.16,.3) {$\scriptstyle x(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.08,.3) rectangle ++(24pt,10pt);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}-
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[<-,thick,darkblue] (0,-.3) to [out=90,in=0] (-.15,0.1);
\draw[-,thick,darkblue] (-.15,0.1) to [out=180,in=90] (-.3,-.3);
\draw[<-,thick,darkblue] (-.3,.9) to [out=-90,in=-180] (-.15,.5);
\draw[-,thick,darkblue] (-.15,.5) to [out=0,in=-90] (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}
\:,\\
x(\down \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.08,.3) rectangle ++(24pt,10pt);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.16,.3) {$\scriptstyle x(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}-
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[<-,thick,darkblue] (0,-.3) to (-.3,.9);
\draw[<-,thick,darkblue] (-.3,-.3) to (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}\,,
&
x(\down \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.08,.3) rectangle ++(24pt,10pt);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.16,.3) {$\scriptstyle x(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}+
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-,thick,darkblue] (0,-.3) to [out=90,in=0] (-.15,0.1);
\draw[->,thick,darkblue] (-.15,0.1) to [out=180,in=90] (-.3,-.3);
\draw[-,thick,darkblue] (-.3,.9) to [out=-90,in=-180] (-.15,.5);
\draw[->,thick,darkblue] (-.15,.5) to [out=0,in=-90] (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}
\:,\label{JMbnew}
\end{align}
for any word $\b$.
Finally, the Jucys-Murphy elements $x^\circ(\b)$ of $\OB^\circ(\delta)$, i.e., the
subcategory consisting of all objects but only morphisms represented
by diagrams with no cups or caps, 
are defined from
$x^\circ(\up) := 0, x^\circ(\down) := -\delta 1_\down$, and
\begin{align}\label{JMcnew}
x^\circ(\up \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.17,.3) {$\scriptstyle x^\circ(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}
+
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,-.3) to (-.3,.9);
\draw[->,thick,darkblue] (-.3,-.3) to (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}\,,
&
x^\circ(\up \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\draw[-,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\node at (0.17,.3) {$\scriptstyle x^\circ(\up \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:,\\
x^\circ(\down \down \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[-,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[->,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.17,.3) {$\scriptstyle x^\circ(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}-
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[<-,thick,darkblue] (0,-.3) to (-.3,.9);
\draw[<-,thick,darkblue] (-.3,-.3) to (0,.9);
\draw[-, thick,double,darkblue] (.25,.9) to (.25,-.3);
\node at (0.25,-.44) {$\b$};
\end{tikzpicture}}\,,
&
x^\circ(\down \up \b) &:= 
\mathord{
\begin{tikzpicture}[baseline=2.5mm]
\draw[->,thick,darkblue] (-.42,.27) to [out=90,in=-120] (-0.05,.9);
\draw[-,thick,darkblue] (0,.47) to [out=90,in=-90] (-.42,.9);
\draw[darkblue,thick,yshift=-5pt,xshift=-5pt] (-.1,.3) rectangle ++(26pt,10pt);
\draw[->,thick,darkblue] (0,.12) to [out=-90,in=90] (-.42,-.3);
\draw[-,thick,darkblue] (-.42,.27) to [out=-90,in=120] (-0.05,-.3);
\node at (0.17,.3) {$\scriptstyle x^\circ(\down \b)$};
\draw[-, thick,double,darkblue] (.25,.12) to (.25,-.3);
\draw[-, thick,double,darkblue] (.25,.48) to (.25,.9);
\node at (0.25,-.44) {$\b$};
\node at (0.25,1.07) {$\b$};
\end{tikzpicture}}\:.\label{JMdnew}
\end{align}
We leave it to the reader to verify with these new definitions
that Lemmas~\ref{fur} and \ref{newz} go through; see also \cite{R}. In
the statement of Lemma~\ref{fur}, one should replace 
$t^{-2}i^{-1}$ with $-i-\delta$,
$I_1$ with $I_0$, and $I_{t^{-2}}$ with $I_{-\delta}$.
Also
 the set $I$ from (\ref{I}) becomes
\begin{equation}
I := I_{0} \cup I_{-\delta} = \{n, -n - \delta\:|\:n \in \ZZ\} \subseteq \k.
\end{equation}
Adjusting the subsequent combinatorics in analogous ways, all of
the other results of section 6 follow as before.

Moving on to section 7, 
the Lie algebra $\g$ is the Kac-Moody algebra associated to the Cartan
matrix
$(c_{i,j})_{i,j \in I}$ defined by (\ref{cartan2}).
The module $V(-\Lambda_1|\Lambda_{t^{-2}})$ becomes
$V(-\Lambda_0|\Lambda_{-\delta})$, and
the degenerate analogs of (\ref{css1})--(\ref{css2}) are
\begin{align}\label{css1}
\wt^\up(\LA)
&:=-\La_0 + \sum_{A \in \la^\up}
\alpha_{\cont(A)},\\\label{css2}
\wt^\down(\LA)
&:=\La_{-\delta} - \sum_{A \in \la^\down}
\alpha_{-\!\cont(A)-\delta},.
\end{align}
There are no other significant discrepancies.

\begin{proof}[Proof of Theorem~\ref{aisha2}]
This is the same as the proof of
Theorem~\ref{evalthm} given in the previous section.
\end{proof}
