---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-006-7-examples
section_title: "Examples"
section_number: 7
pages: 11-17
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.919
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-examples}
\setcounter{equation}{0}

In this section we present a variety of closed-form evaluations of integrals of 
rational functions. \\

\no
{\bf Example 1}. The integral 
\ba
\ift \frac{z^2}{(z^4 + 4z^2 + 1)^9} \; dz & = & \frac{23698523 \, \pi}
{12230590464 \sqrt{6} } \nn
\ea
\no
is computed by Mathematica 3.0 using (\ref{quartic1}) in $.01$ seconds. The 
direct calculation took $12.27$ seconds and $6.4$ extra seconds to simplify 
the answer. \\



\no
{\bf Example 2}. The integral of any even rational function with denominator a 
power of an even quartic polynomial can be computed directly by using 
Corollary \ref{cor62}. For example:
\ba
\ift \frac{z^{6} \, dz}{ (2z^{4} + 2z^{2} + 3)^{11}  } & = & \frac{11 \pi  
(14229567 + 4937288 \, \sqrt{6})}{440301256704 \, ( 1 + \sqrt{6} \, )^{21/2} }.
\nn
\ea
\vskip 10pt

\no
{\bf Example 3}. The case $n=0$ in (\ref{quartic1}) deserves special attention:
\ba
N_{0,4}(a;m) & = &  \frac{\pi}{2^{m+3/2} (a+1)^{m+1/2}} P_{m}(a) \label{no4}
\ea
\no
where 
\ba
P_{m}(a) & = & 2^{-2m} \sum_{k=0}^{m} 2^{k} \binom{2m-2k}{m-k} \binom{m+k}{m} 
(a+1)^{k}. \label{polyam}
\ea
\no
The polynomial $P_{m}(a)$ has been studied in \cite{unim} and \cite{hyp}. \\

\no
{\bf Example 4}. The case $n = m$ in (\ref{quartic1}) yields 
\ba
N_{m,4}(a;m) =  
\int_{0}^{\infty} \frac{z^{2m} \; dz}{(z^{4} + 2az^{2} + 
1)^{m+1}} 
  =  \frac{\pi}{2^{3m+3/2} (1+a)^{m+1/2}} \times \binom{2m}{m}. \nn
\ea
\no
The change of variable $z \to \sqrt{z}$ converts this integral to 
\ba
N_{m,4}(a;m) & = & \frac{1}{2} \int_{0}^{\infty} 
\frac{z^{m-1/2} \; dz}{(z^{2} + 2az + 1)^{m+1} }, \nn
\ea
\no
which is  \cite{gr} 3.257.9.


\vskip 10pt

\no
{\bf Example 5}. A symmetric function of degree $6$. 
The integral
\ba
I  =   \ift \frac{x^{8}}{(x^{6} + 4x^{4} + 4x^{2} + 1)^{5}} \, dx  = 
\ift  \frac{x^{8}}{\left[ (x^{2} + 1)(x^{4} + 3x^{2} + 1 ) 
\right]^{5} } \, dx \nn
\ea
\no
can be computed by decomposing the integrand into partial fractions as
\ba
- \frac{1}{(x^{2} + 1)^{5}} - \frac{1}{(x^{2} + 1)^{4}} 
- \frac{6}{(x^{2} + 1)^{3}} - \frac{11}{(x^{2} + 1)^{2}} 
 -   \frac{31}{(x^{2} + 1)} \nn \\
+ \frac{1}{(x^{4} + 3x^{2} +1)^{5}} + 
\frac{2x^{2}}{(x^{4} + 3x^{2} + 1)^{5}} 
 -   \frac{4}{(x^{4} + 3x^{2} +1)^{4}} 
-\frac{3x^{2}}{(x^{4} + 3x^{2} + 1)^{4}}  + \nn \\
\frac{12}{(x^{4} + 3x^{2} +1)^{3}} +
   \frac{6x^{2}}{(x^{4} + 3x^{2} + 1)^{3}} 
 - \frac{32}{(x^{4} + 3x^{2} +1)^{2}}
 - \frac{14x^{2}}{(x^{4} + 3x^{2} + 1)^{2}}  \nn \\
  +   \frac{73}{(x^{4} + 3x^{2} +1)} + 
  \frac{31x^{2}}{(x^{4} + 3x^{2} + 1)}.  \nn
\ea
\no
Each of these terms is now computable yielding
\ba
I & = & \frac{1407326 \sqrt{5} - 3146875}{160000} \times \pi. \nn
\ea

\vskip 10pt

\no
{\bf Example 6}. Non-symmetric functions of degree $6$. In this case we 
can use the scheme (\ref{scheme6}) to produce 
numerical approximations to the integral. For example, the evaluation of
\ba
\ift \frac{45z^{4} + 25000z^{2} + 1230}{z^{6} + z^{4} + 3000z^{2} + 1} \; dz
 \nn
\ea
\no
is shown below:

\begin{center}
\begin{tabular}[h]{||c|c|c|c|c|c||}
\hline
$n$ & $a_{1}^{n}$ & $a_{2}^{n}$ & $b_{0}^{n}$ & $b_{1}^{n}$ & $b_{2}^{n}$  
\\ \hline 
0 & 1 & 3000 & 45 & 25000 & 1230  \\
1 &.415786 & 14.4465 & 126.233 & 63.2884 & 88.3741 \\
2 & 2.06562 & 3.17262 & 42.2607 & 156.015 & 83.6896 \\
3 & 2.98142 & 3.00338 & 75.3541 & 137.717 & 65.1111 \\
4 & 2.99999 & 3. & 69.6338 & 139.925 & 70.2771 \\
5 & 3. & 3. & 69.9589 & 139.914 & 69.9555 \\
6 & 3. & 3. & 69.9572 & 139.914 & 69.9572 \\
7 & 3. & 3. & 69.9572 & 139.914 & 69.9572 \\
\hline
\end{tabular}
\end{center}

\vskip 10pt

\no
Thus $L \sim 69.9572$ and 
\ba
\ift \frac{45x^{4} + 25000x^{2} + 1230}{x^{6} + x^{4} + 3000x^{2} + 1}
 \; dx & \sim &
69.9572 \times \frac{\pi}{2} \cong 109.889. \nn
\ea

\vskip 5pt 

\no
{\bf Example 7}. Symmetric functions of degree $8$. These integrals
can be evaluated using Theorem \ref{thmsym8}. For example:
\ba
\ift \frac{dz}{(z^{8} + 5z^{6} + 14z^{4} + 5z^{2} + 1)^{4} } & = &
\frac{(14325195794 + 2815367209 \, \sqrt{26} \, ) \, \pi}
{14623232 \, ( 9 + 2 \sqrt{26} \,)^{7/2} }. \nn
\ea

\vskip 5pt

\no
{\bf Example 8}. As in the case of degree $6$ we can provide numerical 
approximations to nonsymmetric integrals of degree $8$. The 
iteration (\ref{scheme6}) is now replaced by  \\
\ba
a_{1}^{n+1} & = & 
\frac{a_{2}^{n}(a_{1}^{n}+a_{3}^{n}) + 4a_{1}^{n}a_{3}^{n} + 
10(a_{1}^{n}+a_{3}^{n}) + 
8(a_{2}^{n}+2)}{(a_{1}^{n}+a_{2}^{n}+a_{3}^{n}+2)^{3/2} } \nn \\
a_{2}^{n+1} & = & \frac{a_{1}^{n}a_{3}^{n}+6(a_{1}^{n}+a_{3}^{n}) 
+ 2(a_{2}^{n}+10) }{a_{1}^{n}+a_{2}^{n}+a_{3}^{3}+2} \nn \\
a_{3}^{n+1} & = & \frac{a_{1}^{n}+a_{3}^{n}+8}{(a_{1}^{n} + a_{2}^{n} + a_{3}^{n}+2)^{1/2}} \nn \\
b_{0}^{n+1} & = & \frac{b_{0}^{n}+b_{1}^{n}+b_{2}^{n}+b_{3}^{n}}{(a_{1}^{n} + a_{2}^{n} + a_{3}^{n}+2)^{3/4}} \nn \\
b_{1}^{n+1} & = & \frac{b_{3}^{n}(3a_{1}^{n}+a_{2}^{n}+6)+b_{2}^{n}(a_{1}^{n}+4) +b_{1}^{n}(a_{3}^{n}+4) +b_{0}^{n}(3a_{3}^{n}+a_{2}^{n}+6) }
{(a_{1}^{n} + a_{2}^{n} + a_{3}^{n} +2)^{5/4} } 
\nn \\
b_{2}^{n+1} & = & \frac{b_{3}^{n}(a_{1}^{n}+5) + b_{2}^{n}+b_{1}^{n} + b_{0}^{n}(a_{3}^{n}+5) }{(a_{1}^{n} + a_{2}^{n} + a_{3}^{n}+2)^{3/4}} \nn \\
b_{3}^{n+1} & = & \frac{b_{0}^{n}+b_{3}^{n}}{(a_{1}^{n} + a_{2}^{n} + a_{3}^{n} +2)^{1/4}} \nn
\ea
\no
with initial conditions
$a_{1}^{0},a_{2}^{0},a_{3}^{0},b_{0}^{0},b_{1}^{0},b_{2}^{0},b_{3}^{0}$. 
Then 
\ba
U_{8}(a_{1},a_{2},a_{3},b_{0},b_{1},b_{2},b_{3}) & := & \int_{0}^{\infty} 
\frac{b_{0}x^{6} + b_{1}x^{4} + b_{2}x^{2} + b_{3}}{x^{8} + a_{1}x^{6} + 
a_{2}x^{4} + a_{3}x^{2} + 1} \; dx  \label{19u8}
\ea
\no
is invariant under these transformations.  \\

\no
{\bf Note}. Numerical calculations show that $(a_{1}^{n},a_{2}^{n},a_{3}^{n}) 
\to (4,6,4)$ and that $(b_{0}^{n},b_{1}^{n},b_{2}^{n},b_{3}^{n}) 
\to (1,3,3,1) \, L$ for some $L$ depending upon the initial conditions.

\vskip 10pt

\no
{\bf Example 9}. A symmetric function of degree $12$. We 
use Theorem \ref{main} to evaluate 
\ba
I & := & \ift \frac{z^{18} \, dz}{( z^{12} + 14z^{10} + 15z^{8} + 4z^{6} +
15z^{4} + 14z^{2} + 1)^{3}}  \nn
\ea
as
\ba
I & = & \frac{25 \pi ( 25 \sqrt{56} - 54) }{301989888}. \label{exam3}
\ea
\vskip 5pt

\no
Here $p =3, \; n=9$, and $m=2$, so $n > (m+1)p-1 $ and we need to 
apply the transformation $z \to 1/z$ to reduce the value of $n$. 
Indeed, we have 
\ba
I & = & \ift \frac{z^{16} \; dz}{ (z^{12} + 14z^{10} + 15z^{8} + 4z^{6} +
15z^{4} + 14z^{2} + 1)^{3}}, \nn
\ea
\no
and Theorem \ref{main} now yields
\ba
I & = & 2^{-17} \ift \frac{z^{16} \; dz}{ 131072 (1 + z^{2})^{3} 
( 1 + 4z^{2} + z^{4})^{3}}. \nn
\ea
\no
The new integrand is expanded in partial fractions in the variable $t = z^{2}$
to produce (\ref{exam3}). 

\vskip 15pt 

\no
{\bf Example 10}. We use Theorem \ref{main} to evaluate
\ba
I & := & \ift \frac{z^{10} \; dz }{Q^{2}(z)} \nn
\ea
\no
where
\ba
Q(z) & = & z^{20} + 6z^{18} + 93z^{16} -24z^{14} + 162z^{12}
+548z^{10} + 162z^8 -24z^6 +93z^4 +6z^2 +1. \nn
\ea
\no
The factorization 
\ba
Q(z) & = & ( 1+ z^{2})^2 T(z) T(-z)  \nn
\ea
\no
with 
\ba
T(z) & = & z^{8} -2z^{7} + 4z^{6} +14z^{5} +6z^{4} -14z^{3} + 4z^{2} + 2z +1
\nn
\ea
\no
leads to a partial fraction expansion containing the term
$$ 
\frac{72 -501 z + 1994z^2-2617z^3+1228z^4-43z^5 + 34z^6 -55z^7}
{8388608 ( 1 -2z+4z^2 +14z^3+6z^4 - 14z^5 + 4z^{6} + 2z^{7} +z^{8} )^{2} },   
$$
\no 
which we were unable to integrate; furthemore, the roots of $T(z)=0$ cannot 
be evaluated by radicals.  The 
procedure described in Theorem \ref{main}, however,  shows that
\ba
I & = & \ift \frac{z^{10} ( 4 + z^{2}) ( z^6 + 36z^4 +96z^2 + 64) \; dz }
{524288 (z^2 + 1)^2 \, (z^8 + 3z^6 + 8z^4 + 3z^2 +1)^2},  \nn
\ea 
\no
the integrand of which can be expanded to yield
\ba
I & = & - \frac{9}{8388608} \ift \frac{dz}{(z^{2} + 1)^{2} } 
- \frac{75}{8388608} \ift \frac{dz}{z^{2} + 1} \nn \\
 & & + \ift \frac{ 1921z^{6} + 10815z^4 +4111z^2 +1462} 
{2097152 \, (z^{8} + 3z^{6} + 8z^{4} + 3z^{2} + 1)^{2} } \; dz \nn \\
 & & \nn \\
 & & +  \ift \frac{ 91z^6 +719z^4 +1259z^2 -5764}
{8388608(z^{8} + 3z^{6} + 8z^{4} + 3z^{2} + 1)} \; dz. \nn
\ea
\no
Every piece is now computable, with the final result
$$ I =  \frac{(6480 - 509 \sqrt{15} ) \, \pi }{24159191040}.$$


\vskip 5pt 

\no
{\bf Example 11}. The symmetric functions of degree $16$ have denominator 
\ba
D_{4}(d_{1},d_{2},d_{3},d_{4};z) & = & z^{16} + d_{4}z^{14} + d_{3}z^{12} + 
d_{2}z^{10} +  2d_{1}z^{8} + d_{2}z^{6} + d_{3}z^{4} + d_{4}z^{2} + 1, \nn
\ea
the integral of which is computed in terms of 
\ba
E_{4}(d_{1},d_{2},d_{3},d_{4};z) & = & (1+d_{1}+d_{2}+d_{3}+d_{4})z^{8} + 
2(16+d_{2}+4d_{3}+ 9d_{4})z^{6}  \nn \\
 &  + & 8(20+d_{3}+6d_{4})z^{4} + 32(8+d_{4})z^{2} + 128. \nn
\ea
\no
This new integral is symmetric provided 
\ba
\begin{bmatrix}
d_{1} \\
d_{2} 
\end{bmatrix}
 & = & 
\begin{bmatrix}
15 \\
112 
\end{bmatrix}
+ 
\begin{bmatrix}
3 \\
-4 
\end{bmatrix}
d_{3} + 
\begin{bmatrix}
-8 \\
7 
\end{bmatrix}
d_{4}. 
\label{param16}
\ea
\no
Introduce the new parameters 
\ba
e_{j} = d_{j} - \binom{8}{5-j} \; \text{ for  } 2 \leq j \leq 4 \; 
\text{ and } 
e_{1}  =  d_{1} - \tfrac{1}{2} \binom{8}{4}. \nn
\ea
\no
Then (\ref{param16}) yields 
\ba
\begin{bmatrix}
e_{1} \\
e_{2} 
\end{bmatrix}
 & = & 
\begin{bmatrix}
3 \\
-4 
\end{bmatrix}
e_{3} + 
\begin{bmatrix}
-8 \\
7 
\end{bmatrix}
e_{4}. 
\label{newparam16}
\ea
\no
Thus, if the original denominator has the form 
\ba
D_{4}(z) & = & (z^{16} + 1 ) + d_{4}(z^{14}+z^{2}) + 
d_{3}(z^{12}+z^{4}) + (112 - 4d_{3}+7d_{4})(z^{10}+z^{6}) \nn \\
 &  & + 2(15+3d_{3}-8d_{4})z^{8}, \nn
\nn
\ea
\no
the integral
\ba
\ift \frac{P(z)}{\left( \; D_{4}(z) \; \right)^{m+1} } \, dz  \nn
\ea
\no
is reduced to an integral with symmetric denominator of degree $8$ and 
these are computable. We can thus evaluate 
a $2$-parameter family of symmetric  integrals 
of degree $16$.

For example, take $d_{3} = d_{4} = 1$ to obtain
\ba
R_{1}(z) & = &  \frac{z^{4}}{(z^{16} + z^{14} + z^{12} + 115z^{10} + 
20 z^{8} + 115z^{6} + z^{4} + z^{2} + 1)^{2}}. \label{fun1}
\ea
\no
The main theorem yields
\ba
R_{2}(z) & = & \frac{1024 z^{4} + 2304z^{6} + 1792 z^{8} + 560 z^{10} + 
60 z^{12} + z^{14} }{2^{7} ( 16z^{8} + 36z^{6} + 27z^{4} + 36z^{2} + 16)^{2}}
\label{fun2}
\ea
\no 
so that 
\ba
\ift R_{1}(z) \, dz & = & \ift R_{2}(z) \, dz. 
\nn
\ea
\no
Letting $f[n]:= N_{n,8}[1,n,27/32,9/4]$ we obtain
\ba
\ift R_{1}(z) \; dz & = & 2^{-15} \left( f[0]+60f[1]+1584f[2] + 
4096 f[3] \right) \nn
\ea
\no
and conclude that 
$$
\ift 
\frac{z^{4} \; dz }{(z^{16} + z^{14} + z^{12} + 115z^{10} + 
20 z^{8} + 115z^{6} + z^{4} + z^{2} + 1)^{2}}  \; =  $$
\vskip 2pt 
$$
= \; \frac{(149288517 + 12947003 \sqrt{131}) \pi}{1124663296 \sqrt{ 54925 + 
4798 \sqrt{131} } }. $$

\vskip 10pt

\no
{\bf Example 12}.  We classify the 
symmetric denominators of degree $32$ that yield computable integrals. 
These functions  depend on $8$ parameters
\ba
D_{8}(d_{1}, \cdots,d_{8};z) & = & \sum_{k=0}^{8} d_{9-k} 
(z^{2k} + z^{2(16-k)}) 
\ea
and the main theorem expresses the integral in terms of $E_{8}$. The 
conditions for $E_{8}$ to be 
symmetric yield 
\ba
d_{1} & = & -3441 + 35d_{5} +64d_{6} -312 d_{7} -3264 d_{8} \nn \\
d_{2} & = & 34720-56d_{5} -110d_{6} + 560d_{7} + 4565d_{8} \nn \\
d_{3} & = & -3472 + 28d_{5} + 64d_{6} -329d_{7} -2240d_{8} \nn \\
d_{4} & = & 4960 - 8d_{5} -19d_{6} + 80d_{7} + 938d_{8} \nn
\ea
\no
and the symmetric $E_{8}$ is 
\ba
E_{8}(d_{5},d_{6},d_{7},d_{8};z)  =  32768(1+z^{16}) + 
(131072 + 8192d_{8})(z^{2} + z^{14}) +   \nn
\ea
\ba
(212992 + 2048d_{7}+28672d_{8})(z^{4} + z^{12}) + 
(180224 + 512d_{6} + 6144d_{7} + 39424d_{8})(z^{6} + z^{10}) + \nn
\ea
\ba
+ (84480 + 128d_{5} + 1280d_{6} + 6912d_{7} + 26880d_{8})z^{8}. \nn
\ea
\no
The symmetry of $E_{8}$  now determines $d_{5},d_{6}$ in terms of 
$d_{7},d_{8}$ and we obtain
\ba
\begin{bmatrix}
d_{1} \\
d_{2} \\ 
d_{3} \\
d_{4} \\
d_{5} \\
d_{6} 
\end{bmatrix}
 & = & 
-31     
\begin{bmatrix}
63475 \\
-100800 \\ 
47936 \\
-13664 \\
2220 \\
- 224
\end{bmatrix}
 + 
\begin{bmatrix}
9166  \\
-14392\\ 
6895 \\
-1964 \\
322 \\
- 28
\end{bmatrix}
d_{7} + 
\begin{bmatrix}
54640  \\
-86645 \\ 
41664 \\
-11471  \\
2000  \\
-189
\end{bmatrix}
d_{8}. 
\label{parameter32}
\ea
\no
The function $(z^{2} + 1)^{16}$ is a symmetric polynomial of degree $32$ 
and yields a particular solution to (\ref{parameter32}). 

As before let 
\ba
e_{j}  =  d_{j} - \binom{16}{9-j} \; \text{ for  } 2 \leq j \leq 8 \; 
\text{ and }  
e_{1}  =  d_{1} - \tfrac{1}{2} \binom{16}{8}. \nn
\ea
\no
Then
\ba
\begin{bmatrix}
e_{1} \\
e_{2} \\ 
e_{3} \\
e_{4} \\
e_{5} \\
e_{6} 
\end{bmatrix}
 & = & 
\begin{bmatrix}
9166  \\
-14392\\ 
6895 \\
-1964 \\
322 \\
- 28
\end{bmatrix}
e_{7} + 
\begin{bmatrix}
54640  \\
-86645 \\ 
41664 \\
-11471  \\
2000  \\
-189
\end{bmatrix}
e_{8} 
\label{newparameter32}
\ea
\no
and as in the case of degree $16$ we can compute a $2$-parameter family of 
symmetric integrals of degree $32$. \\

\vskip 15pt



\no
