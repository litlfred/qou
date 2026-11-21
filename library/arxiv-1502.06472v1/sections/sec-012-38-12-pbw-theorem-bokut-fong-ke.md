---
doc_id: arxiv-1502.06472v1
doc_title: "Gröbner-Shirshov bases and PBW theorems"
section_id: sec-012-38-12-pbw-theorem-bokut-fong-ke
section_title: "``1/2 PBW theorem' (Bokut-Fong-Ke)"
section_number: 3.8
pages: 6-7
source_pdf: 1502.06472v1.pdf
source_sha256: 381cd869fcc06f08
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.952
doc_brief: "Gröbner-Shirshov bases and PBW theorems — We review some applications of Gr¨obner-Shirshov bases, including PBW the- orems, linear bases of free universal algebras, normal forms for groups and"
---
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
