---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-002-13-weak-hopf-algebras
section_title: "Weak Hopf algebras"
section_number: 1.3
pages: 9-12
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
In this Subsection we
will show how the existence of an antipode relates $\PL$, $A^L$
with $\PR$, $A^R$ and derive the expected properties
of $S$ that have been axioms in earlier formulations.
The two most important results will be invertibility of the
antipode and separability of the algebras $A^L$ and $A^R$.
Let us start with the question of uniqueness of the antipode.
\begin{lem} \label{lem: uniq S}
The unit, the counit, and the antipode, if exist, are unique. I.e.
if \break
$(A,\mu,u,\cop,\eps,S)$ and $(A,\mu,u',\cop,\eps',S')$ are both
weak Hopf algebras then $u'=u$, $\eps'=\eps$,\break and $S'=S$.
\end{lem}
\Proof The uniqueness of the unit and the counit are obvious.
Therefore $\PL$ and $\PR$ are common in these two WHA-s. In order
to prove $S'=S$ introduce the convolution product
\beq
(f\diamond g)(x)\ :=\ f(x\c)g(x\cc)\ ,\qquad x\in A
\eeq
on functions $f,g\in\Hom_K(A,A)$. This is an associative operation
in terms of which the antipode axioms take the form
\[\id\diamond S=\PL,\qquad S\diamond\id\diamond S=S,\qquad
  S\diamond\id=\PR\ .\]
Now $S'$ satisfies the same equations with the same $\PL,\PR$,
therefore
\[
S'=S'\diamond\id\diamond S'=S'\diamond\PL=S'\diamond\id\diamond S
  =\PR\diamond S=S\diamond\id\diamond S=S\ .\]
\qed
 
As a preparation for the Theorem below notice that the
definitions (\ref{Pi}) have counterparts involving the antipode:
\begin{lrarray}
\PL(x)=\eps(S(x)\1\c)\1\cc\eql &
\PR(x)=\1\c\eps(\1\cc S(x))\eqr\label{18}
\end{lrarray}
As a matter of fact
\beanon
\PL(x)&=&\eps(\1\c\PL(x))\1\cc=\eps(\PL(x)\1\c)\1\cc=
       \eps(x\c S(x\cc)\1\c)\1\cc=\\
      &=&\eps(\PR(x\c)S(x\cc)\1\c)\1\cc=\eps(S(x\c)x\cc S(x\ccc)
        \1\c)\1\cc=\\
      &=&\eps(S(x)\1\c)\1\cc
\eeanon
where in the subsequent equations (\ref{Pi}), (\ref{LR=RL}),
(A.8a), (\ref{5}b), (A.8b), and finally (A.9) have been used.
Eqn(2.23b) can be proven analogously. As the duals of
(2.23a-b) we have automatically the identities
\begin{lrarray}
\PL(x)=S(\1\c)\eps(\1\cc x)\eql&
\PR(x)=\eps(x\1\c)S(\1\cc).\eqr \label{19}
\end{lrarray}
\begin{lem}
In a WHA $A$ the following identities hold:
\beabc
\PL\circ S\ =&\PL\circ\PR&=\ S\circ\PR\label{20a}\\
\PR\circ S\ =&\PR\circ\PL&=\ S\circ\PL\label{20b}
\eeabc
\end{lem}
\Proof It is sufficient to prove the first equalities in
(\ref{20a}) and (\ref{20b}) because the second ones then follow by
duality.
\beanon
\PL\circ S(x)&=&\eps(\1\c S(x))\1\cc=\eps(\1\c S(x\c)x\cc
               S(x\ccc))\1\cc=\\
             &=&\eps(\1\c S(x\c)\PL(x\cc))\1\cc=\eps(\1\c S(x\c)
               x\cc)\1\cc\\
             &=&\PL\circ\PR(x).
\eeanon
In a similar way one can verify $\PR\circ S=\PR\circ\PL$.\qed
 
The above Lemma implies that $S(A^R)\subset A^L$ and
$S(A^L)\subset A^R$. On the other hand Eqns(2.24a-b) say that
$A^L\subset S(A^R)$ and $A^R\subset S(A^L)$. Therefore the
antipode maps $A^L$ onto $A^R$ bijectively and maps $A^R$ onto
$A^L$ bijectively.
 
\begin{thm}   \label{thm: S}
Let $A$ be a WHA. Then the antipode is antimultiplicative and anti
comultiplicative,
\bea
S(xy)&=&S(y)S(x)\qquad\qquad x,y\in A\ ,\label{21}\\
S(x)\c\o S(x)\cc&=&S(x\cc)\o S(x\c)\qquad\qquad x\in A\
                                                   ,\label{22}
\eea
and the restrictions $S|_{A^L}$ and $S|_{A^R}$ are bijections such
that
\beq
S(A^L)\ =\ A^R\ ,\qquad\qquad S(A^R)\ =\ A^L\ .      \label{23}
\eeq
The unit and the counit are $S$-invariant,
\begin{lrarray}
S(\1)\ =\ \1\ ,\eql&
\eps\circ S\ =\ \eps\ .\eqr\label{24}
\end{lrarray}
Furthermore $S\colon A\to A$ is invertible.
\end{thm}
\Proof We have already shown (\ref{23}). (\ref{22}) is the dual of
(\ref{21}) and (2.29a) is the dual of (2.29b).
\beanon
S(xy)&=&S(x\c y\c)x\cc y\cc S(x\ccc y\ccc)=S(x\c y\c)
                   \PL(x\cc\PL(y\cc))=\\
&=&S(x\c y\c)x\cc\PL(y\cc)S(x\ccc)=\PR(\PR(x\c)
                    y\c)S(y\cc)S(x\cc)=\\
&=&S(y\c)\PR(x\c)y\cc S(y\ccc)S(x\ccc)=S(y\c)y\cc S(y\ccc)
                    S(x\c)x\cc S(x\ccc)=\\
&=&S(y)S(x)\ .
\eeanon
Next we prove (2.29b).
\beanon
\eps(S(x))&=&\eps(S(x\c)x\cc S(x\ccc))=\eps(S(x\c)\PL(x\cc))=
            \eps(S(x\c)x\cc)=\eps(\PR(x))=\\
          &=&\eps(x)\ .
\eeanon
In order to prove invertibility of $S$ notice that the descending
chain $A\supset S(A)\supset S^2(A)\supset\dots$ of WHAs all
contain $\1$ by (2.29a). This implies the existence
of $n\in\N$ such that
\[
\1\ \in\ S^{n+1}(A)\ =\ S^n(A)\ \subset\ S^{n-1}(A)\ .
\]
We want to show that this implies $S^n(A)=S^{n-1}(A)$.
Replacing $A$ by $S^{n-1}(A)$ it is
therefore enough to prove invertibility of $S$
under the additional assumption $S^2(A)=S(A)$, implying
\[
\Ker S\ \cap\ S(A)\ =\ 0\ .
\]
In this case let $\bar S:=S|_{S(A)}$, then $\bar S\colon S(A)\to
S(A)$ is bijective and
\[
P_S\ :=\ {\bar S}^{-1}\circ S\ \colon\ A\to S(A)
\]
is a multiplicative idempotent satisfying
\[
P_S(xS(y))\ =\ P_S(x)S(y)\,,\qquad x,y\in A\ .
\]
By (\ref{23}) $A^{L,R}\subset S(A)$.
Now taking into account the identity $x=x_{(1)}
S(x_{(2)})x_{(3)}$,
which follows directly from axioms (A.8a) and (A.4), then
using also $P_S(\1)=\1$ we have
\beanon
P_S(x)&=&P_S( x_{(1)} S(x_{(2)})x_{(3)})=P_S(x_{(1)})
S(x_{(2)})x_{(3)}= P_S(x_{(1)} S(x_{(2)}))x_{(3)}=\\
&=&P_S(\1)x_{(1)} S(x_{(2)})x_{(3)}=x,
\eeanon
so $\Ker P_S=\Ker S=0$.\qed
 
We are now able to derive (versions of) the original antipode
axioms of \cite{BSz,Sz}:
\beabc
x\c\o x\cc S(x\ccc)&=&\1\c x\o\1\cc\\
S(x\c)x\cc\o x\ccc&=&\1\c\o x\1\cc  \label{eq: 2.29b}\\
x\c\o S(x\cc)x\ccc&=&x\1\c\o S(\1\cc)\\
x\c S(x\cc)\o x\ccc&=&S(\1\c)\o\1\cc x
\eeabc
The first two are just rewritings of the bialgebra identities
(\ref{13a}-b). The second two are more delicate.
\beanon
x\c\o S(x\cc)x\ccc&=&x\c\o\eps(x\cc\1\c)S(\1\cc)
                   =x\c\1\cp\o\eps(x\cc\1\ccp\1\c)S(\1\cc)=\\
                  &=&x\c\1\c\eps(x\cc\1\cc)\o S(\1\ccc)
                   =x\1\c\o S(\1\cc)\\
x\c S(x\cc)\o x\ccc&=&S(\1\c)\eps(\1\cc x\c)\o x\cc
                    =S(\1\c)\eps(\1\cc\1\cp x\c)\o \1\ccp x\cc=\\
                   &=&S(\1\c)\o\eps(\1\cc x\c)\1\ccc x\cc
                    =S(\1\c)\o\1\cc x
\eeanon
The following Proposition also holds, if $A$ is just a WBA, see
\cite{WBA}.
 
\begin{prop} \label{pro:sepa}
Let $A$ be a WHA over $K$. Then $A^L$ and $A^R$ are separable
$K$-algebras, in particular, they are semisimple.
\end{prop}
\Proof Recall that an algebra $A$ is separable if and
only if there exists a $q\in A\o A$ such that $(x\o\1)q=q(\1\o x)$
holds for all $x\in A$ and furthermore $\mu(q)=\1$, where $\mu$
denotes the multiplication map of $A$ \cite{Pierce} . Such a $q$ will be
called
a {\em separable idempotent}\footnote{In fact $q$ is an idempotent
only if considered as an element of $A\o A^{op}$.}. So, our proof
will consist of showing that $q^L=S(\1\c)\o\1\cc\in A^L\o
A^L$ and $q^R=\1\c\o S(\1\cc)\in A^R\o A^R$ are separable
idempotents of $A^L$ and $A^R$, respectively. In fact we will
prove the somewhat more general identities
\beabc \label{separ}
x\c y^R\o x\cc&=&x\c\o x\cc S(y^R)\\
x\c\o y^L x\cc&=&S(y^L)x\c\o x\cc
\eeabc
valid for all $x\in A$ and $y^L\in A^L$, $y^R\in A^R$.
Pairing the LHS of (\ref{separ}) with $\varphi\o\psi$, we obtain
\beanon
\bra\varphi\o\psi,LHS\ket&=&\bra\varphi(y^R\la\du1),x\c\ket
\bra\psi,x\cc\ket=\bra\varphi,x\c\ket\bra(S(y^R)\la\du1)\psi,x\cc\ket=\\
&=&\bra\varphi\o\psi,RHS\ket\ .
\eeanon
The proof of (2.31b) is simply the mirror image of the
above argument. \qed
