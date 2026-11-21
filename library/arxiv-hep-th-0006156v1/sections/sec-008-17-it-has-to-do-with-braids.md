---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-008-17-it-has-to-do-with-braids
section_title: "It has to do with braids"
section_number: 1.7
pages: 6-6
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.963
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
Let us compile a list of what we know about the $b$'s. They are periodic, $b_{n+N}=b_n$, they are this "local" $$b_mb_n=b_nb_m\qquad
\text{if }|m-n|\not\equiv1\pmod{N} ,$$ and they satisfy "global" relations which closed the previous subsection $$b_1b_2\ldots b_{N-1}=b_2b_3\ldots b_N
=\cdots=b_Nb_{N+1}\ldots b_{N-2}\;.$$ Let us now consider these as defining relations and identify the emerging group. It is $B_N$, the group of braids of $N$ strings in 3 dimensions, alternatively defined by an exhaustive list of (Artin's) relations $$b_nb_{n-1}b_n=b_{n-1}b_nb_{n-1}\qquad
\qquad b_nb_m=b_mb_n\mbox{ if }|n-m|\neq1$$ imposed on $N-1$ generators $b_1,b_2,\ldots,b_{N-1}$. We leave it as an (instructive) exercise to check that our list is equivalent to Artin's, provided the leftmost of our "global" relations is read as $$b_N=(b_2\ldots b_{N-1})^{-1}
b_1b_2\ldots b_{N-1}$$ and understood as the definition of $b_N$. Just in case, let us warn against mistaking $b_N$ for the $N$'th generator of $B_{N+1}$, ours is just an element of $B_N$ explicitly defined above. Those familiar with the braid group must have already recognized in it the first string crossing the very last one behind all the others, let us picture it for $N=4$: $$\setlength{\unitlength}{1mm}
\raisebox{4mm}{\(b_1=\;\;\)}
\begin{picture}(12,11)\linethickness{0.3mm}
\qbezier(0,10)(-1,8)(1,6)\qbezier(3,4)(5,2)(4,0)
\qbezier(4,10)(4,6)(2,5)\qbezier(2,5)(0,4)(0,0)
\qbezier(8,10)(8,5)(8,0)\qbezier(12,10)(12,5)(12,0)
\end{picture}\qquad
\raisebox{4mm}{\(b_2=\;\;\)} \setlength{\unitlength}{1mm}
\begin{picture}(12,11)\linethickness{0.3mm}
\qbezier(4,10)(3,8)(5,6)\qbezier(7,4)(9,2)(8,0)
\qbezier(8,10)(8,6)(6,5)\qbezier(6,5)(4,4)(4,0)
\qbezier(0,10)(0,5)(0,0)\qbezier(12,10)(12,5)(12,0)
\end{picture}\qquad
\raisebox{4mm}{\(b_3=\;\;\)}
\begin{picture}(12,11)\linethickness{0.3mm}
\qbezier(8,10)(7,8)(9,6)\qbezier(11,4)(13,2)(12,0)
\qbezier(12,10)(12,6)(10,5)\qbezier(10,5)(8,4)(8,0)
\qbezier(0,10)(0,5)(0,0)\qbezier(4,10)(4,5)(4,0)
\end{picture}\qquad
\raisebox{4mm}{\(b_4=\;\;\)} \setlength{\unitlength}{1mm}
\begin{picture}(12,11)\linethickness{0.3mm}
\qbezier(0,10)(-2,6)(1,5)
\qbezier[2](4,4)(7,3)(10,2)
\qbezier(10,2)(13,1)(12,0)
\qbezier(12,10)(13,8.5)(10,7.5)
\qbezier[2](10,7.5)(7,6.5)(4,5.5)
\qbezier(4,5.5)(1,4.5)(0,0)
\qbezier(4,10)(7,5)(4,0)\qbezier(8,10)(9,5)(8,0)
\end{picture}\raisebox{4mm}{ .}$$ A picture of the evolution operator $$\raisebox{4mm}{\(Q=b_1b_2b_3=b_2b_3b_4
  =b_3b_4b_1=b_4b_1b_2=\;\;\)} \setlength{\unitlength}{1mm}
\begin{picture}(12,11)\linethickness{0.3mm}
\qbezier(0,10)(0,8)(1,7.5)
\qbezier(11,2.5)(12,2)(12,0)
\qbezier(4,10)(4,9)(2,6)\qbezier(2,6)(0,3)(0,0)
\qbezier(8,10)(8,8)(6,5)\qbezier(6,5)(4,2)(4,0)
\qbezier(12,10)(12,7)(10,4)\qbezier(10,4)(8,1)(8,0)
\qbezier[3](1,7.5)(6,5)(11,2.5)
\end{picture}\raisebox{4mm}{ ,}$$ now explains better than words how it manages to be ordered and cyclic at the same time.
