---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-012-61-definition
section_title: "Definition"
section_number: 6.1
pages: 24-32
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.969
---
We define an algebra $F_n$ over $A = \Q[a,x,x^{-1}]/(a^2 = 1)$ by generators
$s_1,\dots,s_{n-1}$, $e_1,\dots,e_{n-1},C$ and relations
\begin{enumerate}
\item $s_i s_{i+1} s_i  = s_{i+1} s_i s_{i+1}$, $s_i s_j = s_j s_j$
\item $(s_i -a)(s_i^2 -x s_i+1)=0$
\item $e_i = a \left( \frac{ s_i^{-1} + s_i}{x} - 1 \right)$
\item $s_i e_i = a e_i$
\item $e_i s_{i+1} e_i =  e_i+C$
\item $e_i s_{i-1} e_i =  e_i+C$
\item $e_i s_{i+1}^{-1} e_i =  e_i+C$
\item $e_i s_{i-1}^{-1} e_i =  e_i+C$
\item $s_i C = C s_i = a C$.
\end{enumerate}
Letting  $\tilde{\delta} = 2 - ax $, we have $e_i^2= \tilde{\delta}x^{-1} e_i$. 
Immediate consequences of these relations are
$s_i^{-1} C = C s_i^{-1} = a C$, $e_i C = C e_i = x^{-1} \tilde{\delta}C$,
$C^2 = (x^{-2} \tilde{\delta}^2 a - x^{-1} \tilde{\delta})C = x^{-1} \tilde{\delta}(a x^{-1} \tilde{\delta} - 1) C
= 2x^{-2} \tilde{\delta}( a-x) C$. Note
that, in the specializations $x = a$ and $x = 2a$, we have $C^2 = 0$.

The following is easily checked
\begin{prop} \label{propbasiqueFn}
\begin{enumerate}
\item The $S^{\dagger\dagger}$-algebra $F_n \otimes_A S^{\dagger\dagger}$ is a quotient of $H_n \otimes_R S^{\dagger\dagger}$ through $s_i \mapsto s_i$ and $A \to S^{\dagger\dagger}$ being given by $x \mapsto b+c$. This quotient factorizes through $BMW_n^{\dagger\dagger}$.
\item There is a surjective morphism of $S^{\dagger\dagger}_{\pm}$-algebras $F_n \otimes_A S^{\dagger\dagger}_{\pm} \onto BMW_n^{\pm} \otimes_{S_{\pm}} S^{\dagger\dagger}_{\pm}$ satisfying
$s_i \mapsto s_i$, $e_i \mapsto e_i$, $C \mapsto 0$. Its kernel is the linear span of $C$.
\item The automorphism and antiautomorphism of $A$-algebras of the group algebra $A B_n$
defined by $s_i \mapsto s_i^{-1}$ induce an automorphism and a antiautomorphism of $F_n$.
\item Every Markov trace $(t_n)$ factorizing through $F_n$ is uniquely determined by $t_3(1)$, $t_3(s_1)$
and $t_3(s_1s_2)$.
\end{enumerate}
\end{prop}

\begin{proof}
We start with (i). Only the fact that we have a factorization through $BMW_n^{\dagger\dagger}$ requires a justification.
According to proposition \ref{proppresWBMWidemp}, it is sufficient to show that $s_1 e_2s_1$ and $s_2^{-1} e_1 s_2^{-1}$
are mapped to the same element. Using the same computations as in the proof of proposition \ref{propWBMWetendbien}
we easily get that both are sent to $x e_1 s_2^{-1} + ax C + x e_2 s_1 - s_2 e_1 s_2^{-1}$, and this proves the claim. 
(ii) is easy, because the linear span of $C$ is clearly a two-sided ideal of $F_n$. (iii) is easily checked from the defining relations of $F_n$.
We now prove (iv). From the arguments of proposition \ref{prop:unicitetracegenplus}  one
easily gets that such a Markov trace is uniquely determined by $t_3$ together with the collection of the $t_n(C)$,
since $C = e_{n-1} s_n e_{n-1} - e_{n-1}$.  Because $Cs_n = aC$ we get $a t_{n+1}(C) = t_n(C)$, whence the Markov trace is uniquely determined by $t_3$, and
therefore by $t_3(1)$, $t_3(s_1)$ together with $t_3(s_1s_2)$ by proposition \ref{prop:MT3bmw}. 


\end{proof}

\begin{cor} If $(t_n)$ is a Markov trace factoring through $F_n$, then the associated link invariant
does not distinguish mirrors and does not detect non-invertible links.
\end{cor}
\begin{proof} This follows from the items (iii) and (iv) of the proposition : the mirror of the closed braid $\hat{\beta}$
is the closure of the image of $\beta$ under the automorphism $s_i \mapsto s_i^{-1}$,  the mirror of the inverse is the closure of the image of $\beta$
under the antiautomorphism $s_i \mapsto s_i^{-1}$. Since $t_3(s_1) = t_3(s_1^{-1})$,
$t_3(1) = t_3(1^{-1})$, $t_3(s_1s_2) = t_3(s_1^{-1} s_2^{-1})$, such a Markov trace coincides by (iv) with its 
composite with the (anti-)automorphisms defined in (iii), whence the conclusion. 
\end{proof}

\begin{prop} \label{proprelrecutraceFn} If $(t_n)$ is a Markov trace factoring through $F_n$, then
\begin{enumerate}
\item $\forall n \geq 3 \ \ t_{n+1}(C) = a t_n(C)$
\item $\forall n \geq 2\ \ t_{n+1}(C) = a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$
\item For all $n \geq 1$,
$$t_{n+3}(1)=   \left( a+\frac{\tilde{\delta} + 2}{x}\right)t_{n+2}(1) -\frac{1}{x} \left(2 \frac{\tilde{\delta}}{x}+a(\tilde{\delta} + 2) \right) t_{n+1}(1) 
 +2a \frac{\tilde{\delta}}{x^2} t_{n}(1)$$
\end{enumerate}
\end{prop}
\begin{proof} (i) is trivially deduced from $s_n C = a C$ and the Markov property.
From $C = e_{n-1} s_n e_{n-1} - e_{n-1}$ we get
$t_{n+1}(C) = t_{n+1}(e_{n-1}^2 s_n) - t_3(e_{n-1}) = \tilde{\delta}x^{-1}t_{n+1}(e_{n-1} s_n) - t_{n+1}(e_{n-1})
= \tilde{\delta}x^{-1}t_n(e_{n-1}) - t_{n+1}(e_n)$ by the Markov property and because $e_{n-1}$ and $e_n$ are conjugates.
Expanding $e_i = (a/x)(s_i + s_i^{-1}) - a$ and using the Markov property again we
get
$t_{n+1}(C) = \tilde{\delta}x^{-1}(2a/x t_{n-1}(1) - a t_n(1)) - (2a/x t_n(1) - a t_{n+1}(1)) =
a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$, namely (ii).
By (i) we know $t_{n+1}(C) = a t_{n+2}(C)$ hence, by (ii), we get
$t_{n+1}(C) = a t_{n+2}(C) =  t_{n+2}(1) -  x^{-1}(\tilde{\delta} + 2)t_{n+1}(1) +2 \tilde{\delta} x^{-2} t_{n}(1)$
 hence, again by (ii),  $t_{n+2}(1) -  x^{-1}(\tilde{\delta} + 2)t_{n+1}(1) +2 \tilde{\delta} x^{-2} t_{n}(1) = 
a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$
hence 
$$t_{n+2}(1)=   \left( a+\frac{\tilde{\delta} + 2}{x}\right)t_{n+1}(1) -\frac{1}{x} \left(2 \frac{\tilde{\delta}}{x}+a(\tilde{\delta} + 2) \right) t_{n}(1) 
 +2a \frac{\tilde{\delta}}{x^2} t_{n-1}(1)$$
which proves (iii).
\end{proof}

At this stage, $C$ could well be $0$. We now prove that this is not the case.

\subsection{A genuine extension of $BMW_n^{\pm}$}


Using the abelianization morphism $B_n \onto \Z$ we can define a 3-dimensional $H_n \otimes_R S^{\dagger \dagger}$-module
by
$$
s_i \mapsto \begin{pmatrix}  a & 1 & 0 \\ 0 & b & 1 \\ 0 & 0 & b^{-1} \end{pmatrix}
$$
It is easily checked that $\mathcal{R}_1$ acts by $0$ in this module, hence we get a 3-dimensional
$BMW_n^{\dagger\dagger}$-module. We get that $e_i = a((s_i + s_i^{-1})/x - 1)$
is mapped to
$$
\left[ \begin {array}{ccc} {\frac { \left( ab-1 \right)  \left( -b+a
 \right) }{{b}^{2}+1}}&{\frac {ab-1}{{b}^{2}+1}}&{\frac {b}{{b}^{2}+1}
}\\ \noalign{\medskip}0&0&0\\ \noalign{\medskip}0&0&0\end {array}
 \right] 
$$
while $e_i s_{i+1} e_i - e_i$ and $e_i s_{i+1}^{-1} e_i - e_i$ are both mapped
to
$$
2 \frac{ab-b^2-1}{(b^2+1)^2}
\begin{pmatrix} (ab-1)(a-b) & ab-1 & b \\ 0 & 0 & 0 \\ 0 & 0 & 0
\end{pmatrix}
$$
{}
This proves that this module induces a $F_n\otimes_A S^{\dagger\dagger}$-module,
and therefore a $F_n\otimes_A S^{\dagger\dagger}_{\pm}$-module,
which do not factorize through $BMW_n^{\pm}$.
It follows that $BMW_n^{\dagger\dagger}$ and $F_n$ are genuine extensions of the Birman-Wenzl-Murakami algebra.
We need to prove a similar result for the specializations appearing in the previous section.
However, for one of them the above argument does not work, because it corresponds
to a root of $ab-b^2-1$. 
Nevertheless, we know by proposition  \ref{propstructgenWBMW} (iii) that $BMW_n^{\dagger\dagger}$ is finitely
generated as a $S^{\dagger\dagger}$-module. Because of this, the dimension of every specialization
is at least the dimension of $BMW_n^{\dagger\dagger}$ over the field of fractions of $S^{\dagger\dagger}$
(this classical fact follows for instance from Nakayama's lemma, by replacing $S^{\dagger\dagger}$ by its
localization at the defining ideal of the specialization). This proves the following.


\begin{prop} \label{propFnVraieextension} For every morphism $\la : S^{\dagger \dagger} \to \C$,
$BMW_n^{\dagger \dagger} \otimes_{\la} \C$ and $(F_n\otimes_A S^{\dagger\dagger})\otimes_{\la} \C$ have dimension at least $1 + \dim BMW_n^+$.
\end{prop}


\begin{cor} For every morphism $\la : S^{\dagger \dagger} \into \C$,
the image of $C$ inside 
$(F_n\otimes_A S^{\dagger\dagger})\otimes_{\la} \C$ 
is nonzero.
\end{cor}

\begin{cor} \label{cordimFn}  The $A$-module $F_n$ is free of rank $1+\dim BMW_n^{\pm}$
\end{cor}
\begin{proof}
Let us denote $A_{\pm} = \Q[a,x,x^{-1}]/(a\mp 1) \simeq \Q[x,x^{-1}]$. By the natural $A$-module
decomposition $A \simeq A_+ \oplus A_-$ it is enough to prove that $F_n^{\pm} = F_n \otimes_A A_{\pm}$
is a free $A_{\pm}$-module of rank $1+N$ with $N = \dim BMW_n^{\pm}$.  Now notice that $BMW_n^{\pm} \otimes_{S_{\pm}} S^{\dagger\dagger}_{\pm}$ is actually defined by a presentation with coefficients in $A_{\pm}$, and that
the corresponding $A_{\pm}$-form is free of rank $N$ by \cite{MORTONWASSERMANN}. Therefore, as in proposition \ref{propbasiqueFn} (ii),
we get a surjective $A_{\pm}$-morphisme $F_n^{\pm} \onto A_{\pm}^N$ by mapping $C$ to $0$. Letting $s_{\pm}$
denote a section of this morphism, we get a surjective morphism $u_{\pm} : A_{\pm}^{1+N} \simeq (A_{\pm} C)\oplus A_{\pm}^N \to
F_n^{\pm}$ by $(\la C,m) \mapsto \la C + s_{\pm}(m)$. Letting $K_{\pm}$ denote the quotient field
of $A_{\pm}$, it follows that $u_{\pm} \otimes_{A_{\pm}} K_{\pm}$ is surjective. But proposition \ref{propFnVraieextension}
implies that $F_n^{\pm} \otimes_{A_{\pm}} K_{\pm}$ has dimension $1+N$. Therefore
the source and target of $u_{\pm} \otimes_{A_{\pm}} K_{\pm}$ have the same dimension hence $u_{\pm} \otimes K_{\pm}$
is injective. Since the source of $u_{\pm}$ is a free module this implies that $u_{\pm}$ is injective and this proves the claim.

\end{proof}

\begin{cor} \label{corFnFnp1}  The natural algebra morphism $F_n \to F_{n+1}$ is injective.
\end{cor}
\begin{proof}
As before, using the notations of the previous proof, it is equivalent to show that the natural maps $F_n^{\pm} \to F_{n+1}^{\pm}$ are
injective. This is true because the following diagram of horizontal short exact sequences is commutative, and because its two extremal vertical arrows
are known to be injective.
$$
\xymatrix{
0 \ar[r] & A_{\pm} C \ar[r]\ar[d] & F_n^{\pm} \ar[r] \ar[d]& BMW_n^{\pm} \ar[r] \ar[d]& 0 \\
0 \ar[r] & A_{\pm} C \ar[r] & F_{n+1}^{\pm} \ar[r] & BMW_{n+1}^{\pm} \ar[r] & 0 \\
}
$$
\end{proof}

\subsection{The algebra $F_n$ as a specialization of $\WBMW_n$}


The goal of this section is to prove the following theorem.

\begin{theor} \label{theoisomddaggerFn} The morphism of $S^{\dagger\dagger}$-algebras $BMW_n^{\dagger\dagger} \to F_n \otimes_A S^{\dagger\dagger}$
induces an isomorphism after tensorisation by $S^{\dagger\dagger}[(x+2a)^{-1}]$.
\end{theor}

We define $\mathcal{S}_ i = e_i s_{i+1} e_i - e_i$, 
$\mathcal{S}'_ i = e_i s_{i+1}^{-1} e_i - e_i \in H_n \otimes_R S^{\dagger\dagger}$, and also
$\widehat{\mathcal{R}_i} = (s_i s_{i+1} s_i)\mathcal{R}_i (s_i s_{i+1} s_i)^{-1}$,
and similarly $\widehat{\mathcal{S}_i} = (s_i s_{i+1} s_i) (\mathcal{S}_i) (s_i s_{i+1} s_i)^{-1}$.
The two formulas below hold inside $H_3 \otimes S^{\dagger\dagger}$ and can be checked
computationally by using the morphism $\Phi_{H_3}$, as we did for lemma \ref{lemRimpliesS} (these
formulas were found by a similar procedure, too).

\begin{equation}
\mathcal{S}_1- \mathcal{S}'_1 
= \frac{1}{x} \mathcal{R}_1 s_2 -\frac{1}{x^2}s_1^{-1} \mathcal{R}_1 s_2 
- \frac{1}{x^2}s_1 \mathcal{R}_1 s_2 = \frac{1}{x^2}(x - s_1^{-1} - s_1) \mathcal{R}_1 s_2 
= \frac{1}{(b+c)^2} (s_1 -b)(s_1-c) s_1^{-1} \mathcal{R}_1 s_2  \label{eqssprime}
\end{equation}
\begin{equation}
2x^2 \left(  \mathcal{S}_{1} - \widehat{\mathcal{S}}_{1}\right)=
 (x- s_1^{-1} - s_1) \mathcal{R}_1 s_2 -  \mathcal{R}_1 + (-x +  s_2^{-1} + s_2) \widehat{\mathcal{R}_1} s_1
+  \widehat{\mathcal{R}_1} \label{eqssym}
\end{equation}


We now want to show that $\mathcal{S}_1 - \mathcal{S}_2$ also belongs to the ideal generated by $\mathcal{R}_1$. For this
we need to work inside $H_4 \otimes S^{\dagger\dagger}$. Since the computations become quite complicated, we specialize
at $a=1$. There is no loss of generality in doing this, as we justify it now. The natural decomposition $S^{\dagger\dagger}
= S^{\dagger\dagger}_+ \oplus S^{\dagger\dagger}_-$ induces a $\Q$-vector space decomposition $H_n \otimes_R S^{\dagger\dagger} = H_n^+ \oplus
H_n^-$ with projectors $p_+,p_-$ given by the multiplication by $(a-1)/2$ and $(a+1)/2$. It is straightforward to
check that the involutive automorphism $E^{\dagger}$ of $H_n \otimes_R S^{\dagger\dagger}$ induced by
$\hat{E}$ and $\eta$ (see the notations of proposition \ref{propdefE} and before) exchanges $H_n^+$ and $H_n^-$, maps
$\mathcal{S}_i \mapsto -\mathcal{S}_i$, $\mathcal{R}_i \mapsto -\mathcal{R}_i$ and intertwines $p_+$ and $p_-$ up
to a sign (that is: $E^{\dagger} \circ p_+ = - p_- \circ E^{\dagger}$,
$E^{\dagger} \circ p_- = - p_+ \circ E^{\dagger}$). Because of this, any expression of $p_+(\mathcal{S}_1 - \mathcal{S}_2) = (\mathcal{S}_1)_+
- (\mathcal{S}_2)_+$ immediately yields an expression of $p_-(\mathcal{S}_1 - \mathcal{S}_2)$
and therefore of $\mathcal{S}_1 - \mathcal{S}_2$.

We now use the fact that $H_4$ is a free $R$-module of rank 648 in order to do explicit computations. More precisely,
the computations are made as follows. First of all, we build a basis of $H_4$ as follows. We
consider the collection $\mathcal{B}_2$ of 27 words in $s_i, s_i^{-1}$ given in proposition 4.8 of \cite{CUBIC5}.
They form a basis of $H_4$ as a $H_3$-module. Together with the list of 24 words $\mathcal{B}_1$ 
given by proposition \ref{prop:H3libre} (ii), which induces a basis of $H_3$, we get a
collection $\mathcal{B}_3 = \{ g_1 g_2 ; (g_1, g_2) \in \mathcal{B}_1 \times \mathcal{B}_2\}$
of $24 \times 27 = 648$ words which induces a basis of $H_4$. From this and the implicit rewriting rules of \cite{CUBIC5} we
build an explicit regular representation $H_4 \into Mat_{648}(R)$ and therefore an injective map
 $\Phi_{H_4} : H_4 \otimes_R S_+^{\dagger \dagger} \to Mat_{648}(S_+^{\dagger \dagger})$, that we use in order to check equalities.
 
 

Letting $(\mathcal{S}_1)_{\pm} = \mathcal{S}_{\pm}$,
we let $(\mathcal{S}_2)_{\pm} = (s_1 s_2)( \mathcal{S}_1)_{\pm} (s_1 s_2)^{-1}$.
Inside $H_4 \otimes_R R/(a-1,y-1)$ we find that $2 (x+2)^2 x^4 ((\mathcal{S}_1)_+ -( \mathcal{S}_2)_+)$
can be expressed as a sum of 161 terms obviously belonging to $I_4$, see Figures \ref{S12a}, \ref{S12b}, \ref{S12c}.



These terms were found as follows. For computational reasons (and the limited power of the computers we have at disposal) it is too difficult to
compute the linear span of $I_4$ inside the field of fractions $\Q(x)$ or $\Q(b)$, so we need to circumvent this obstacle by computing inside specialisations in $x$.
For some specific value of $x$ we get a basis $\mathcal{B}^1$ of the linear span of the image of $I_4$ inside $\Q^{648}$.
The one we get is made of terms of the form $g \mathcal{R}_1 g'$ where $g,g'$ are products of elements $s_i,s_i^{-1}$
(chosen inside the basis of $H_4$ mentionned above), or $g \mathcal{R}_2 g'$ or $g \widehat{\mathcal{R}_1} g'$ or $g \widehat{\mathcal{R}_2} g'$.
The same elements form a basis of the specializations of $H_4$ for infinitely many values of $x$. We chose a number of values for which
we got an expression of $\mathcal{S}_1 - \mathcal{S}_2$ as linear combination of the elements of $\mathcal{B}^1$. Assuming that these
coefficients should be rational fractions in $x$ whose denominators have low degree, we get these rational fractions by interpolation. We then check that the
corresponding equality is correct by direct computation inside $H_4 \otimes \Q(x)$. It so happens that the choices we made in this process provide an expression of $(x-1)(x+2)^2(x^2+x-1)x^4 (\mathcal{S}_1 - \mathcal{S}_2)$. Recall that, in order to deal with the odd cases of the previous
section, we need to specialize at $x=1$.  For this alone, we need to start again with this specialization, and we get this time, as a linear combinations of another basis $\mathcal{B}^2$, a polynomial expression of $(x+1)(x+2)^2x^4 (\mathcal{S}_1 - \mathcal{S}_2)$. By Bezout theorem both results combined provide an expression of $2 (x+2)^2 x^4 ((\mathcal{S}_1)_+ -( \mathcal{S}_2)_+)$
as a linear combination of $\mathcal{B}^1 \cup \mathcal{B}^2$, and this is the result that is expressed here (the cardinality of
$\mathcal{B}^1 \cup \mathcal{B}^2$ is 161).


Needless to say, one could have hoped to get a nicer expression. Unfortunately we failed to find one.


The $x^4$ factor in this expression prevents the specialization $x=0$, which is to be expected. The $x+2$ factor prevents the specialization
$x=-2a$, which was not expected, but is explained by the proposition below. This proposition implies that the morphism under consideration
does not induce an isomorphism under this specialization, since the algebras $BMW_4^{\pm}$ have dimension 105.
Note that $(S^{\dagger\dagger}_{\pm})/(x+2a) \simeq \Q[b]/(b+ b^{-1} \pm 2) \simeq \Q[b]/(b \pm 1)^2$.

\begin{prop} \label{propdimBMWm2a}
The $\Q$-algebras $BMW_4^{\dagger\dagger} \otimes_{S^{\dagger\dagger}} \Q[b]/(b \pm 1)$ both have dimension 115.
\end{prop}
\begin{proof}
Direct computations prove that their defining ideals inside $H_4 \otimes_R R/(a\mp 1,b\pm 1, c \pm 1) \simeq \Q^{648}$ have dimension $533$,
hence the corresponding quotients have dimension $648-533 = 115$.
\end{proof}
\begin{figure}
$$
\begin{array}{ll}
 & (x+2)(x^7+4x^6-x^5-12x^4-5x^3+9x^2-1)x\mathcal{R}_1+ (-x^7-4x^6+8x^4+2x^3-8x^2-2x+6)\mathcal{R}_1s_3^{-1}\\ +&
  (2x+4)\mathcal{R}_1s_3^{-1}s_2^{-1}s_1^{-1}
  +   (x+2)(x^2-x-1)(x^5+3x^4-3x^3-5x^2+3x-2)x\mathcal{R}_1s_1 \\
+&  (x+2)(x^2-x-1)x^2\mathcal{R}_1s_1s_3^{-1}+ (-x-2)(x^2-x-1)(x^3+3x^2-2x-3)x^2\mathcal{R}_1s_1s_3 \\+&
  (-x^8-5x^7-3x^6+13x^5+17x^4-4x^3-10x^2+6x+6)\mathcal{R}_1s_3+(2x+4)\mathcal{R}_1s_3s_2s_1\\+& (-x-2)(x^3+2x^2+2x-1)x\mathcal{R}_2+ 
  (x^5+4x^4+3x^3-3x^2-2x-2)\mathcal{R}_2s_1^{-1}\\+& (x+1)(x+2)(x^2-x-1)(x^4+4x^3+2x^2-2x-4)x\mathcal{R}_2s_1^{-1}s_3+ 
  (x^5+4x^4+3x^3-3x^2-2x-2)\mathcal{R}_2s_1\\ +& (x+1)(x+2)(x^2-x-1)(x^4+4x^3+2x^2-2x-4)x\mathcal{R}_2s_1s_3\\ + & 
  (-x-1)(x+2)(x^2-x-1)(x^4+3x^3-2x^2-x+2)x\mathcal{R}_2s_2\\ + & (-x-2)(x^5+2x^4-6x^3-7x^2+2x+9)x\widehat{\mathcal{R}}_1+
  (2x^7+9x^6+2x^5-26x^4-29x^3-x^2+12x+4)\widehat{\mathcal{R}}_1s_3^{-1}\\ + &  (-2x-4)\widehat{\mathcal{R}}_1s_3^{-1}s_2^{-1}s_1^{-1}+ 
  (x^8+5x^7+4x^6-11x^5-25x^4-14x^3+9x^2+14x+4)\widehat{\mathcal{R}}_1s_3\\+&( -2x-4)\widehat{\mathcal{R}}_1s_3s_2s_1+
  (-x-1)(x+2)(x^6+3x^5-4x^4-9x^3+2x^2+9x+1)x\widehat{\mathcal{R}}_2\\ + &
  (x^9+7x^8+14x^7-4x^6-47x^5-49x^4+5x^3+34x^2+10x-4)\widehat{\mathcal{R}}_2s_1^{-1}\\+& 
  (x^9+7x^8+14x^7-3x^6-44x^5-52x^4+32x^2+12x-4)\widehat{\mathcal{R}}_2s_1\\ + & 
  (-x^8-5x^7-2x^6+17x^5+25x^4+3x^3-24x^2-20x-2s_3^{-1})\mathcal{R}_1+ (2x+4)(x^2+x+2)s_3^{-1}\mathcal{R}_1s_3^{-1}\\ + &
  (-x^6-3x^5-4x^4-2x^3+7x^2+10x+4)s_3^{-1}\mathcal{R}_1s_1^{-1}\\+& (-x^8-5x^7-x^6+14x^5+9x^4-11x^3-10x^2+4x+4)s_3^{-1}\mathcal{R}_1s_1\\+& 
  (x-1)(x+2)(x^2-x-1)(x^2+4x+2)xs_3^{-1}\mathcal{R}_1s_1s_3\\ +& (-x^8-4x^7+x^6+12x^5+12x^4+5x^3-4x^2-12x-10)s_3^{-1}\mathcal{R}_1s_2\\+& 
  (x+1)(x^5+3x^4-4x^3-9x^2+2x+10)xs_3^{-1}\mathcal{R}_1s_3+ (2x+4)s_3^{-1}\mathcal{R}_1s_3s_2^{-1} \\ + & 
  (-x^8-5x^7-3x^6+13x^5+25x^4+15x^3-5x^2-12x-4)s_3^{-1}\widehat{\mathcal{R}}_1 \\ + &
  (-x-2)(x^5+3x^4-3x^3-7x^2-4x+2)s_3^{-1}\widehat{\mathcal{R}}_1s_3^{-1}+
  (x+2)(x^4+x^3+2x^2-3)xs_3^{-1}\widehat{\mathcal{R}}_1s_2^{-1}\\ + & 
  (x^7+4x^6-2x^5-14x^4-15x^3-2x^2+14x+8)s_3^{-1}\widehat{\mathcal{R}}_1s_1^{-1}\\+& 
  (x^5-4x^4-12x^3-4x^2+10x+6)s_3^{-1}\widehat{\mathcal{R}}_1s_1\\+&( -x^7-4x^6+10x^4+12x^3+3x^2-4x-6)s_3^{-1}\widehat{\mathcal{R}}_1s_3+ 
  (-x-1)(x+2)(x^2+x-1)xs_3^{-1}\widehat{\mathcal{R}}_2\\+& (x^5+4x^4+3x^3-3x^2-2x-2)s_3^{-1}\widehat{\mathcal{R}}_2s_1^{-1}+ 
  (x^5+4x^4+3x^3-3x^2-2x-2)s_3^{-1}\widehat{\mathcal{R}}_2s_1\\+& (x-1)(x^2+4x+2)s_3^{-1}s_2^{-1}\widehat{\mathcal{R}}_1s_3+
  (2x+4)s_3^{-1}s_2^{-1}s_1\mathcal{R}_2+ (-2x-4)s_3^{-1}s_2^{-1}s_1\widehat{\mathcal{R}}_2\\+& 
  (-x-2)(x^5+3x^4-3x^3-7x^2-4x+2)s_3^{-1}s_2\mathcal{R}_1s_3^{-1}+( -x^5-3x^4+4x^3+10x^2+4x-4)s_3^{-1}s_2\mathcal{R}_1s_3\\+&
  (x+1)(x^5+3x^4-4x^3-8x^2+6x+11)x^2s_2^{-1}\mathcal{R}_2+( -x^5-4x^4-5x^3-x^2+2x-2)s_2^{-1}\mathcal{R}_2s_1^{-1}\\+&
  (-x^7-4x^6-x^5+6x^4+6x^3-x^2-2)s_2^{-1}\mathcal{R}_2s_1+ (x+2)(x^4+3x^3-6x+1)xs_2^{-1}\widehat{\mathcal{R}}_1\\+&
  (-x^4-3x^3+3x+2)xs_2^{-1}\widehat{\mathcal{R}}_1s_3^{-1}+ (-x^4-4x^3-3x^2+5x+4)xs_2^{-1}\widehat{\mathcal{R}}_1s_3\\+&
  (x+1)(x^5+2x^4-6x^3-x^2+10x+6)xs_2^{-1}\widehat{\mathcal{R}}_2\\+& 
  (-x^8-5x^7-4x^6+10x^5+18x^4+6x^3-7x^2-4x-2)s_2^{-1}\widehat{\mathcal{R}}_2s_1^{-1}\\+& 
 ( -x^8-5x^7-4x^6+10x^5+18x^4+6x^3-7x^2-4x-2)s_2^{-1}\widehat{\mathcal{R}}_2s_1+( -2x-4)s_2^{-1}s_1\mathcal{R}_2s_1^{-1}\\+&
  (2x+4)s_2^{-1}s_3\widehat{\mathcal{R}}_1s_3^{-1}+ (-x^7-4x^6+8x^4-7x^2-x-4)xs_1^{-1}\mathcal{R}_1\\+& 
  (-x^8-3x^7+5x^6+13x^5-9x^3+2x^2+4x-2)s_1^{-1}\mathcal{R}_1s_3^{-1}+( x^7+4x^6-9x^4-3x^3+4x^2-2)s_1^{-1}\mathcal{R}_1s_3\\+& 
  (-x^7-3x^6-2x^5+2x^4+7x^3+2x^2-4x+2)s_1^{-1}\mathcal{R}_2\\+& (x^7+4x^6-2x^5-10x^4+x^3+2x^2-7x-6)xs_1^{-1}\mathcal{R}_2s_2^{-1}\\+&
  (x^8+4x^7-2x^6-10x^5+x^4+2x^3-7x^2-4x+4)xs_1^{-1}\mathcal{R}_2s_2\\+& (-x^7-4x^6+2x^5+10x^4-x^3-2x^2+7x+6)xs_1^{-1}\mathcal{R}_2s_3\\+&
  (-x+1)(x+1)(x^4+2x^3-5x^2+2x+14)xs_1^{-1}\widehat{\mathcal{R}}_1\\+&
  (-x^7-4x^6+11x^4+15x^3+5x^2-2x-6)s_1^{-1}\widehat{\mathcal{R}}_1s_3^{-1}\\+&
  (-x-1)(x^6+2x^5-5x^4-3x^3-5x^2+2x+6)s_1^{-1}\widehat{\mathcal{R}}_1s_3 \\ + & \dots
  \end{array}
  $$
   \caption{For $a=1$, $2 (x+2)^2 x^4 (\mathcal{S}_1 - \mathcal{S}_2)$ to be continued.}
   \label{S12a}
  \end{figure}
  \begin{figure}
  $$
  \begin{array}{ll}& \dots\\
  +& 
  (-x^7-4x^6+2x^5+10x^4-x^3+15x+14)xs_1^{-1}\widehat{\mathcal{R}}_2\\+& 
  (-x^7-3x^6-2x^5+2x^4+7x^3+2x^2-4x+2)s_1^{-1}\widehat{\mathcal{R}}_2s_3^{-1} \\+& 
  (2x^6+7x^5-6x^4-11x^3+2x^2-10x-4)xs_1^{-1}\widehat{\mathcal{R}}_2s_2^{-1}\\+&
  (-x+1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1^{-1}\widehat{\mathcal{R}}_2s_1^{-1}\\+&
  (-x^7-4x^6+10x^4+11x^3-2x^2-6x-4)s_1^{-1}\widehat{\mathcal{R}}_2s_1+( -2x-4)s_1^{-1}\widehat{\mathcal{R}}_2s_1s_2^{-1}\\+&
  (2x^8+8x^7-3x^6-24x^5-10x^4+12x^3+6x^2-2x-2)s_1^{-1}\widehat{\mathcal{R}}_2s_2\\+&
  (x^7+4x^6-x^5-13x^4-10x^3+x^2-6)s_1^{-1}s_3^{-1}\mathcal{R}_1s_3^{-1}+ (-x^3-5x^2-2x-2s_1^{-1})s_3^{-1}\mathcal{R}_1s_3\\+&
  (x^6+4x^5-10x^3-13x^2-4x-2)s_1^{-1}s_3^{-1}\widehat{\mathcal{R}}_1s_3^{-1}\\+&
  (x^6+3x^5-3x^4-7x^3-6x^2-2x+4)s_1^{-1}s_3^{-1}\widehat{\mathcal{R}}_1s_3\\+& 
  (-x^7-4x^6+x^5+13x^4+10x^3-x^2+6)s_1^{-1}s_2^{-1}\mathcal{R}_2s_1^{-1}\\+& (-x^7-3x^6+5x^5+13x^4-12x^2+8)s_1^{-1}s_2^{-1}\mathcal{R}_2s_1
+(  2x+4)s_1^{-1}s_2^{-1}s_3^{-1}\mathcal{R}_1+( -2x-4)s_1^{-1}s_2^{-1}s_3^{-1}\widehat{\mathcal{R}}_1
\\+&
  (2x+4)s_1^{-1}s_2^{-1}s_3\mathcal{R}_1+ (-2x-4)s_1^{-1}s_2^{-1}s_3\widehat{\mathcal{R}}_1\\+&
  (-x-2)(x^2-x-1)(x^5+3x^4-4x^3-2x^2+3x-4)xs_1^{-1}s_2\mathcal{R}_2\\+&
  (x+1)(x^5+3x^4-4x^3-10x^2-4x+4)xs_1^{-1}s_3\mathcal{R}_1s_3^{-1}+ (-x-1)(x+2)(x^2+2x-2)s_1^{-1}s_3\mathcal{R}_1s_3\\+&
  (-x+1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1^{-1}s_3\mathcal{R}_2s_1^{-1}\\+&( -x^7-4x^6+10x^4+11x^3-2x^2-6x-4)s_1^{-1}s_3\mathcal{R}_2s_1\\+& 
  (x+1)(x^6+4x^5-x^4-13x^3-9x^2+2x+6)s_1^{-1}s_3\widehat{\mathcal{R}}_1s_3^{-1}\\+& 
  (x+2)(x^6+3x^5-4x^4-9x^3-x^2+2x+6)s_1^{-1}s_3\widehat{\mathcal{R}}_1s_3\\+&
  (-x^8-4x^7+2x^6+17x^5+5x^4-22x^3-18x^2+2x+10)xs_1\mathcal{R}_1\\+& (-x^7-4x^6-x^5+10x^4+18x^3+7x^2-2x-6)s_1\mathcal{R}_1s_3^{-1}\\+&
  (x^8+3x^7-5x^6-13x^5+5x^4+21x^3+9x^2-8x-6)s_1\mathcal{R}_1s_3\\+&(-x^6-2x^5-x^4-4x^3-8x^2-8x+2)s_1\mathcal{R}_2
\\+&  (x^5+3x^4+4x^3-3x^2-9x-2)xs_1\mathcal{R}_2s_2^{-1}+ (2x+4)s_1\mathcal{R}_2s_1^{-1}s_2\\+& 
  (x^7+5x^6+2x^5-9x^4-11x^3-4x^2-2)xs_1\mathcal{R}_2s_2\\+& (x^7+4x^6-2x^5-16x^4-12x^3+10x^2+17x+4)xs_1\mathcal{R}_2s_3\\+&
  (x^8+5x^7+4x^6-10x^5-23x^4-20x^3+3x^2+19x+12)xs_1\widehat{\mathcal{R}}_1\\+& 
  (-x^7-6x^6-8x^5+11x^4+34x^3+22x^2-5x-10)xs_1\widehat{\mathcal{R}}_1s_3^{-1}\\+&
  (-2x^7-9x^6-3x^5+24x^4+33x^3+7x^2-15x-8)xs_1\widehat{\mathcal{R}}_1s_3\\+&
  (x^7+4x^6-2x^5-16x^4-12x^3+10x^2+17x+4)xs_1\widehat{\mathcal{R}}_2\\+& (-x^6-2x^5-x^4-2x^3+2)s_1\widehat{\mathcal{R}}_2s_3^{-1}\\+&
  (-x^6-3x^5+6x^4+13x^3+3x^2-14x-10)xs_1\widehat{\mathcal{R}}_2s_2^{-1}\\+& 
  (-x^8-5x^7-3x^6+15x^5+24x^4-2x^3-20x^2-8x+8)s_1\widehat{\mathcal{R}}_2s_1^{-1}\\+&
 ( -x^8-5x^7-3x^6+14x^5+21x^4+x^3-15x^2-6x+6)s_1\widehat{\mathcal{R}}_2s_1\\+&
  (x^9+5x^8+3x^7-14x^6-22x^5+3x^4+20x^3+4x^2-8x-2)s_1\widehat{\mathcal{R}}_2s_2\\+&
  (x+2)(x^2-x-1)(x^5+5x^4+3x^3-2x^2-2x-2)s_1s_3^{-1}\mathcal{R}_1\\+& (x^6+4x^5-10x^3-13x^2-4x-2)s_1s_3^{-1}\mathcal{R}_1s_3^{-1}\\+&
  (-x^7-3x^6+5x^5+12x^4-5x^3-16x^2-6x+4)s_1s_3^{-1}\mathcal{R}_1s_3\\+&
  (x^7+5x^6+4x^5-10x^4-21x^3-11x^2+2x+6)s_1s_3^{-1}\widehat{\mathcal{R}}_1s_3^{-1}\\+&
  (2x+2)(x^2+4x+2)(x^4-x^3-3/2x^2+1)s_1s_3^{-1}\widehat{\mathcal{R}}_1s_3 \\+ & \dots
  \end{array}
  $$
   \caption{For $a=1$, $2 (x+2)^2 x^4 (\mathcal{S}_1 - \mathcal{S}_2)$, continued.}
      \label{S12b} 
  \end{figure}
\begin{figure}
  $$
  \begin{array}{ll}+& 
  (-x-1)(x^5+3x^4-3x^3-7x^2-6x+2)s_1s_2^{-1}\mathcal{R}_2s_1^{-1}+ (2x+4)xs_1s_2^{-1}\mathcal{R}_2s_1\\+&
  (x-1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2^{-1}\widehat{\mathcal{R}}_2s_1^{-1}\\+&
  (x-1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2^{-1}\widehat{\mathcal{R}}_2s_1\\+& (-x-2)(x^2-x-1)(x^4+5x^3+3x^2-x-4)xs_1s_2\mathcal{R}_2\\+& 
  (x-1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2\mathcal{R}_2s_1^{-1}\\+& (x-1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2\mathcal{R}_2s_1\\+&
  (-x+1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2\widehat{\mathcal{R}}_2s_1^{-1}\\+&
  (-x+1)(x+1)^2(x^2-x-1)(x^2+4x+2)s_1s_2\widehat{\mathcal{R}}_2s_1+ (2x+4)s_1s_2s_3^{-1}\mathcal{R}_1\\+& 
  (-2x-4)s_1s_2s_3^{-1}\widehat{\mathcal{R}}_1+ (2x+4)s_1s_2s_3\mathcal{R}_1+( -2x-4)s_1s_2s_3\widehat{\mathcal{R}}_1\\+&
  (x+2)(x^2-x-1)(x^4+x^3-4x^2-2)s_1s_3\mathcal{R}_1\\+& (x+1)(x^6+4x^5-x^4-13x^3-9x^2+2x+6)s_1s_3\mathcal{R}_1s_3^{-1}\\+&
  (x+2)(x^5+2x^4-6x^3-5x^2+6)s_1s_3\mathcal{R}_1s_3\\+&( -x^8-5x^7-3x^6+15x^5+24x^4-2x^3-20x^2-8x+8)s_1s_3\mathcal{R}_2s_1^{-1}\\+&
  (-x^8-5x^7-3x^6+14x^5+21x^4+x^3-15x^2-6x+6)s_1s_3\mathcal{R}_2s_1\\+&
  (x+1)^2(x^2+4x+2)(x^4-x^3-x^2-x+1)s_1s_3\widehat{\mathcal{R}}_1s_3^{-1}\\+&
  (x+2)(x^6+4x^5-x^4-13x^3-9x^2+4x+8)xs_1s_3\widehat{\mathcal{R}}_1s_3\\+& (-x-2)(x^5+2x^4-6x^3-7x^2+4x+5)xs_2\mathcal{R}_1+
  (x^3-2x-2)(x^4+5x^3+5x^2-x-1)s_2\mathcal{R}_1s_3^{-1}\\+& (x^6+3x^5-4x^4-13x^3-6x^2+4x+2)s_2\mathcal{R}_1s_3\\+&
  (x+1)(x^7+4x^6-x^5-12x^4-5x^3+8x^2+6x+2)xs_2\mathcal{R}_2\\+& (-x^8-5x^7-4x^6+10x^5+18x^4+6x^3-7x^2-4x-2)s_2\mathcal{R}_2s_1^{-1}\\+&
  (-x^8-5x^7-4x^6+10x^5+18x^4+6x^3-7x^2-4x-2)s_2\mathcal{R}_2s_1\\+& (x^6+4x^5-x^4-12x^3-4x^2+13x+11)x^2s_2\widehat{\mathcal{R}}_2\\+&
  (-x^9-6x^8-9x^7+7x^6+34x^5+31x^4-9x^3-26x^2-6x+8)s_2\widehat{\mathcal{R}}_2s_1^{-1}\\+&
  (-x^9-6x^8-9x^7+7x^6+34x^5+31x^4-9x^3-26x^2-6x+8)s_2\widehat{\mathcal{R}}_2s_1+( -2x-4)s_2s_3^{-1}\mathcal{R}_1s_3\\+&
  (2x+4)s_2s_1^{-1}\widehat{\mathcal{R}}_2s_1+ (-x^7-3x^6+4x^5+14x^4+6x^3-10x^2-12x-2)s_3\mathcal{R}_1\\+&
  (-x-1)(x+1)(x^5+2x^4-6x^3-4x^2+4)s_3\mathcal{R}_1s_3^{-1}+ (-x-1)(x^5+2x^4-x^3-x^2-4x-4)s_3\mathcal{R}_1s_1^{-1}\\+&
  (-x^7-x^6+7x^5+2x^4-13x^3-10x^2+4x+4)s_3\mathcal{R}_1s_1\\+& (x-1)(x+2)(x^2-x-1)(x^2+4x+2)xs_3\mathcal{R}_1s_1s_3\\+&
  (-x+1)(x^8+6x^7+9x^6-6x^5-29x^4-28x^3-16x^2-14x-10)s_3\mathcal{R}_1s_2\\+& (x+2)(x^3+3x^2-6)s_3\mathcal{R}_1s_3\\+&
  (-x-1)(x+2)(x^6+3x^5-4x^4-9x^3+2x^2+7x+1)xs_3\mathcal{R}_2\\+& (x^8+6x^7+7x^6-13x^5-27x^4-9x^3+10x^2+2x-4)s_3\mathcal{R}_2s_1^{-1}\\+&
  (x^8+6x^7+8x^6-10x^5-30x^4-14x^3+8x^2+4x-4s_3)\mathcal{R}_2s_1\\+& (-x^7-3x^6+3x^5+11x^4+13x^3+7x^2-2x-4)s_3\widehat{\mathcal{R}}_1\\+& 
  (-x-1)(x^7+4x^6-10x^4-12x^3-3x^2+4x+6)s_3\widehat{\mathcal{R}}_1s_3^{-1}+ (-2x-4)s_3\widehat{\mathcal{R}}_1s_3^{-1}s_2\\+&
  (x^5+3x^4+x^3-x-8)xs_3\widehat{\mathcal{R}}_1s_2^{-1}+( x^6+x^5-7x^4-5x^3-4x^2+10x+8)s_3\widehat{\mathcal{R}}_1s_1^{-1}\\+&
  (-x^6-2x^5+2x^4-3x^3-4x^2+6x+6)s_3\widehat{\mathcal{R}}_1s_1\\+& (-x-1)(x+2)(x^6+3x^5-4x^4-9x^3+4x+4)s_3\widehat{\mathcal{R}}_1s_3\\+&
  (x-1)(x+1)(x^2+4x+2)s_3s_2^{-1}\widehat{\mathcal{R}}_1s_3^{-1}+ (x-1)(x+2)(x^2+4x+2)s_3s_2^{-1}\widehat{\mathcal{R}}_1s_3\\+&
  (-x-1)(x^5+3x^4-4x^3-10x^2-4x+4)s_3s_2\mathcal{R}_1s_3^{-1}+ (x+1)(x+2)(x^2+2x-2)s_3s_2\mathcal{R}_1s_3\\+&
  (2x+4)s_3s_2s_1^{-1}\mathcal{R}_2+ (-2x-4)s_3s_2s_1^{-1}\widehat{\mathcal{R}}_2.
 \end{array}
 $$
 \caption{For $a=1$, $2 (x+2)^2 x^4 (\mathcal{S}_1 - \mathcal{S}_2)$, last part.}
    \label{S12c}
 
 \end{figure}
 
We will elaborate a bit more on the case $x = -2a$ in section \ref{subsectm2a}. For now, let $\pi : BMW_n^{\dagger \dagger}\otimes S^{\dagger\dagger}[(x+2a)^{-1}] \onto F_n \otimes_A S^{\dagger\dagger}[(x+2a)^{-1}]$ be the obvious
 projection. We need to find a section $f$ such that $f \circ \pi = \mathrm{Id}$, and for this it is enough
 to check that the natural projection $f : H_n \otimes S^{\dagger\dagger}[(x+2a)^{-1}] \onto BMW_n^{\dagger \dagger}\otimes S^{\dagger\dagger}[(x+2a)^{-1}] $ factorizes through $F_n \otimes_A S^{\dagger\dagger}[(x+2a)^{-1}] $. Using the decomposition $S^{\dagger\dagger} = S^{\dagger\dagger}_+ \oplus
 S^{\dagger\dagger}_-$ and the Galois automorphism mapping $a \mapsto -a$,
   it is sufficient to check this for $f_+ : H_n \otimes S^{\dagger\dagger}_+[(x+2)^{-1}] \onto BMW_n^{\dagger \dagger}\otimes S_+^{\dagger\dagger}[(x+2)^{-1}] $. It is clear that the relators associated to $(i)-(iv)$ are mapped to $0$.
 Now $C = e_1 s_2 e_1 - e_1$ is mapped to $\mathcal{S}_1$, and the relations \ref{eqssprime}, \ref{eqssym} and the fact that
 $\mathcal{S}_1- \mathcal{S}_2 \in I_n$ (hence $\mathcal{S}_i - \mathcal{S}_{i+1} \in I_n$ for all $i$) then imply, using conjugation by
 elements of the braid groups, that the relators associated to (v) and (viii) are also mapped to $0$. Since $s_1 e_1 = e_1 s_1 = a e_1$
 it is clear that $s_1 \mathcal{S}_1 =  \mathcal{S}_1s_1 = a s_1$ and this implies $s_i C - a C \mapsto 0, Cs_i - a C \mapsto 0$ for all $i$,
 which justifies that the 9th type of relator is also mapped to $0$. This completes the proof of the theorem.
 

\begin{cor} \label{corclasstracesddagger}
Let $(t_n)$ be a Markov trace on $(BMW_n^{\dagger\dagger})$ with value in some $S^{\dagger\dagger}$-module $M$, and $t'_n$
its composite with $M \to M \otimes S^{\dagger\dagger}[(a-x)^{-1},(2a-x)^{-1},(2a+x)^{-1} ]$. Then $t'_n$ is a linear combination
$t_n^H$, $t_n^K$ , $t_n^{\dagger\dagger}$
with coefficients in $M \otimes_R S^{\dagger\dagger}[(a-x)^{-1},(2a-x)^{-1},(2a+x)^{-1} ]$.
\end{cor}
\begin{proof}
We know from proposition \ref{propclassmarkovddagger3} (ii) that $t'_3$ is a linear combination of $t_3^H$, $t_3^K$, $t_3^{\dagger \dagger}$.
The statement is then a consequence of theorem \ref{theoisomddaggerFn} together with proposition \ref{propbasiqueFn} (iv).
\end{proof}
