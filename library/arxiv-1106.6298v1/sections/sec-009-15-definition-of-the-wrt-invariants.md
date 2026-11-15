---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-009-15-definition-of-the-wrt-invariants
section_title: "Definition of the WRT invariants"
section_number: 1.5
pages: 7-8
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.957
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
Let
\[


 F_{L}(\xi):= {\sum_{n_i}}^\xi\; \prod_{i=1}^m [n_i]\;
  J_{L}(n_1,\dots,n_m).\]


\begin{Thm} \label{K1M}{\rm [Reshetikhin--Turaev]}
$F_L(\xi)$ is invariant under K1--Move.
\end{Thm}



An important special case is when $L=U^b$, the unknot with framing
$b \neq 0$. In that case $F_{U^{b}}(\xi)$ can be calculated
using the Gauss sum and is nonzero.

 Let $\sigma_+ $ (respectively $\sigma_-$) be the number of
positive (negative) eigenvalues of the linking matrix of $L$.
 Then we define


\begin{equation}
\tau_{M}(\xi) =
\frac{F_{L}(\xi)}{(F_{U^{+1}}(\xi))^{\sigma_+}\,
(F_{U^{-1}}(\xi))^{\sigma_-} }\, .
\label{def_qi}
\end{equation}

It is easy to see that  $\tau_M(\xi)$ is invariant under
K2--Move, and hence, by Theorem \ref{K1M}, it is a topological
invariant of $M$ called the $SO(3)$ WRT invariant.
 Moreover,
 $\tau_{M}(\xi)$ is multiplicative with
respect to the connected sum.

\vskip2mm
\noindent
{\bf Remark.}
If we drop the condition that the colors in the summation are
odd, and sum over all (odd and even) colors, the result will be
the $SU(2)$ WRT invariant  $\tau^{SU(2)}_M (\xi)$.
In this case, the order of $\xi$ could also be even.
\vskip2mm

 The $SO(3)$  WRT invariant  extends naturally to the invariant
of the pair $(M,L')$, where
the manifold $M$ contains a link $L'$ inside. In this case we have
to replace the surgery link $L$ of $M$ by $L\cup L'$ in all definitions,
fix colors on $L'$ and sum over all colorings of
$L$ only. We omit here the precise definition and refer to \cite{BBL}
for more details.


For example, the $SO(3)$ invariant of the lens space $L(b,1)$,
obtained by surgery along $U^b$,  is
\begin{equation} \tau_{L(b,1)} (\xi)= \frac{ F_{U^b}(\xi)}{F_{U^{\sn(b)}}(\xi) },
\label{2005}
\end{equation}
were $\sn(b)$ is the sign of the integer $b$.






Suppose
$M$ is a rational homology
3--sphere.

Then there is a unique decomposition
 $ H_1(M,\Z)=\bigoplus_{i}
\Z/{b_{i}\Z}$, where each $b_i$ is a prime power.
We renormalize the $SO(3)$  WRT invariant  as follows:
\begin{equation}
\tau'_{M}(\xi)=\frac{\tau_{M}(\xi)}
{\prod\limits_{i}\;\,
\tau_{L(b_{i},1)}(\xi)}\; ,




\label{0910}
\end{equation}
where $L(b,a)$ denotes the $(b,a)$ lens space. Note that
$\tau_{L(b,1)}(\xi)$ is always nonzero.



Let us focus on the special case when the linking matrix of
$L$ is diagonal.

Assume each $L_{ii}=b_i$ is a power of a prime or 1, up to sign.
Then $H_1(M,\Z) = \oplus_{i=1}^m \Z/|b_i|$, and
$$\sigma_+ = {\rm card}\, \{ i\mid b_i >0\}, \quad \sigma_- =
{\rm card}\, \{ i \mid b_i < 0\}.$$
Thus from the definitions \eqref{def_qi}, \eqref{2005} and \eqref{0910} we have
\begin{equation}
 \tau'_{M}(\xi) = \left( \prod_{i=1}^m  \tau'_{L(b_i,1)}(\xi)
 \right)\,
\frac{F_{L}(\xi)}
{\prod_{i=1}^m F_{U^{b_i}}(\xi) }
\,  ,
\label{0077}
\end{equation}
with
$$\tau'_{L(b_i,1)}(\xi)= \frac{\tau_{L(b_i,1)}(\xi)}{\tau_{L(|b_i|,1)}(\xi)}\, .$$

The collection of $SO(3)$ WRT invariants is difficult to study, since
their definition heavily depends on the order of $\xi$.
The following cyclotomic expansion will play an important role
for the unification of the WRT invariants.
