---
doc_id: arxiv-1502.06472v1
doc_title: "Gröbner-Shirshov bases and PBW theorems∗ L. A. Bokut†"
section_id: sec-010-36-dendriform-algebrasrota-baxter-algebras-chen
section_title: "Dendriform algebras–Rota-Baxter algebras (Chen-Mo, Kolesnikov)"
section_number: 3.6
pages: 6-7
source_pdf: 1502.06472v1.pdf
source_sha256: 381cd869fcc06f08
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.952
---
Rota-Baxter identity: $$\begin{aligned}
P(x)P(y)=P(P(x)y)+P(xP(y)), \forall x,y\in A.
\end{aligned}$$ Dendriform identities: $(x\prec y)\prec z=x\prec(y\prec z+y\succ
z),\ (x\succ y)\prec z=x\succ(y\prec z),\ (x\prec y+x\succ y)\succ
z=x\succ(y\succ z).$ $$\begin{aligned}
D&=&Den(X|x_i\prec x_j=\{x_i\prec x_j\},\  x_i\succ x_j=\{x_i\succ x_j\}, x_i,x_j\in X);\\
U(D)&=&RB(X|x_iP(x_j)=\{x_i\prec x_j\},\  P(x_i)x_j=\{x_i\succ
x_j\}, x_i,x_j\in X).
\end{aligned}$$

Then $D\subset U(D)$, see Chen-Mo [@ChenMo-AMS].

## Shirshov's, Cartier's, Cohn's counter examples to PBW for Lie algebras over commutative algebra

Shirshov [@{[Sh53b]}] 1953 and Cartier [@{[Cartier]}] 1958 give counter examples to PBW for Lie algebras over commutative algebra. Cohn [@{[Cohn63]}] 1963 posts the conjecture: $$\begin{aligned}
\mathcal{L}_p&=&Lie_{K}(x_1,x_2,x_3 \ | \ y_3x_3=y_2x_2+y_1x_1),\\
K&=&k[y_1,y_2,y_3|y_i^p=0, i=1,2,3].
\end{aligned}$$ $\mathcal{L}_p$ can not be embedded into its universal enveloping associative algebra.

Bokut-Chen-Chen [@{[BCC11]}] establish GS bases theory for Lie algebras over a commutative algebra. We prove Cohn's conjecture is correct for $p=2,3,5$.

##  "1/2 PBW theorem\" (Bokut-Fong-Ke)

Let $k$ be a field with the characteristic 0 and $C$ a $k$-algebra with operations $a(n)b,\ n\geq 0$, and $D(a)$. Then $C$ is called a conformal algebra, if

\(1\) (the locality condition). For any $a,b\in C$, there exist $N(a,b)\geq 0$ such that $a(n)b=0$ for $n\geq N(a,b)$.

\(2\) $D(a(n)b)= D(a)(n)b +a(n)D(b)$ and $D(a)(n)b= -na(n-1)b$.

Let $C$ be a conformal algebra. Then $C$ is an associative conformal algebra if $$(As)\ \ (a(n)b)(m)c= \sum_{s\geq 0}(-1)^sC{_n}^s a(n-s)(b(m+s)c);$$ $C$ is a Lie conformal algebra if $$\begin{aligned}
&&(Lie)\ \  \mbox{(anti-commutativity) }\ (a[n]b)=\{b[n]a\}, \\
&& \ \ \ \ \mbox{ where }\ \{b[n]a\} = \sum_{s\geq
0}(-1)^{n+s}D^{(s)}(b[n+s]a),\
D^{(s)}=1/s!D^s,\\
&& \mbox{(Jacoby) }\ ((a[n]b)[m]c) = \sum_{s\geq
0}(-1)^{s}C_{n}^s((a[n-s](b[m+s]c))- (b[m+s](a[n-s]c))).
\end{aligned}$$

Gröbner-Shirshov bases for conformal associative algebras ($n$-conformal associative algebras) are established in Bokut-Fong-Ke [@BFK04] and Bokut-Chen-Zhang [@BoChZhang-n-conf].

There is a 1/2 PBW-theorem for Lie conformal algebras: Let $$L=LieCon(\{a_i,\ i\in I\}, N| a_i[n]a_j =\sum\alpha_{ij}^k a_k,\
i\geq j,\ n<N)$$ be a Lie conformal algebra with the linear basis $\{a_i,\ i\in I\}$ over $k[D]$ and the locality $N$. Let $$U(L) = AsCon(\{a_i,\ i\in I\}, N| S=\{s_{ij}^n= a_i(n)a_j -
\{a_j(n)a_i\} - a_i[n]a_j,\ i\geq j,\ n<N\})$$ be the universal enveloping associative conformal algebra for $L$.

Then any composition $(s_{ij}^n, s_{jk}^m)_w=s_{ij}^n(m)a_k -
a_i(n)s_{jk}^m,\ i>j>k,\ n,m<N$ is trivial $mod(S,w),\
w=a_i(n)a_j(m)a_k$.

  

There is also a 1/2 PBW theorem between $n$-conformal Lie algebras and $n$-conformal associative algebras, see [@BoChZhang-n-conf].
