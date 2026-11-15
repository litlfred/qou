---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-022-44-basic-determinant-formula-for-the-free-fermio
section_title: "Basic determinant formula for the free-fermion correlator"
section_number: 4.4
pages: 83-87
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.914
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Let us consider the following matrix element:
\be
\tau_N\{t,\bar t\mid G\} =
\langle N \mid e^H \ G \ e^{\bar H} \mid N \rangle
\label{pretaf}
\ee
where
\be
\new
\begin{array}{c}
\psi( z) = \sum_{n\in Z}\psi_n z^n d z^{1/2}; \ \ \
\tilde\psi( z) = \sum_{n\in Z}\tilde\psi_n z^{-n-1}d z^{1/2};\\
G = \exp\left( \sum_{m,n\in Z}{A}_{mn}\psi_m\tilde\psi_n \right);  \\
H = \sum_{k>0} t_kJ_k, \ \ \ \bar H = \sum_{k>0} \bar t_kJ_{-k} \\



J( z) = \psi( z)\tilde\psi( z) =
\sum_{n\in Z}J_n z^{-n-1}d z; \ \ \ J_n =
\sum_k\psi_k\tilde\psi_{k+n};   \\
\phantom. [\tilde\psi_m,\psi_n]_+ = \delta_{m,n}; \ \ \
[J_m,J_n] = m\delta_{m+n,0};  \\
\psi_m\mid N \rangle = 0, \ \ m<N; \ \ \ \
\langle N \mid \psi_m = 0, \ \ m\geq N;  \\
\tilde\psi_m\mid N \rangle = 0, \ \ m\geq N; \ \ \ \
\langle N \mid \tilde\psi_m = 0, \ \ m< N;  \\
J_m\mid N \rangle = 0,\ \ m>0; \ \ \ \
\langle N \mid J_m = 0, \ \ m<0.
\end{array}
\label{notfermcor}
\ee
The "$N$-th vacuum" $\mid N \rangle$ is defined as the Dirac sea, filled up to
the level $N$:
\be
\mid N \rangle =
\prod_{i=N}^\infty \tilde\psi_i\mid\infty\rangle =
\prod_{i=-\infty}^{N-1} \psi_i \mid-\infty\rangle \ ; \nn \\
\langle N \mid = \langle \infty\mid \prod_{i=N}^\infty \psi_i =
\langle -\infty\mid \prod_{i=-\infty}^{N-1} \tilde\psi_i,
\ee
where the "empty" (bare) and "completely filled" vacua  are defined so that:
\be
&\tilde\psi_m \mid -\infty \rangle = 0, \ \ \ \langle -\infty \mid \psi_m = 0,
\nn \\
&\psi_m \mid \infty \rangle = 0, \ \ \ \langle \infty \mid \tilde\psi_m = 0
\ee
for $any$ $m\in Z$. For the only reason that operators $J$, $H$, $\bar H$ and
$G$ are defined so that they have usually $\tilde\psi$ at the very right and
$\psi$ at the very left, we have also:
\be
&J_m \mid -\infty \rangle = 0, \ \ \ \langle -\infty\mid  J_m = 0,
\nn \\
&G^{\pm 1} \mid-\infty \rangle = \mid-\infty \rangle; \ \ \
\langle -\infty \mid G^{\pm 1} = \langle -\infty \mid; \nn \\
&e^{\pm \bar H}  \mid-\infty \rangle = \mid-\infty \rangle; \ \ \
\langle -\infty \mid e^{\pm H} = \langle -\infty \mid.
\ee
Now we can use all these formulas to rewrite our original correlator
(\ref{pretaf}) as:
\be
\new
\begin{array}{c}
\langle N \mid e^H \ G\ e^{\bar H}\mid N \rangle =  \\
=  \langle  -\infty\mid \left(\prod_{i=-\infty}^{N-1} \tilde\psi_i\right)
                  e^H \ G\ e^{\bar H}
\left(\prod_{i=-\infty}^{N-1} \psi_i\right) \mid-\infty\rangle =  \\
= \langle  -\infty\mid e^{-H} \left(\prod_{i=-\infty}^{N-1}\tilde\psi_i\right)
                  e^H \ G\ e^{\bar H}
\left(\prod_{i=-\infty}^{N-1} \psi_i\right) e^{-\bar H}\mid-\infty\rangle =
 \\
= \langle  -\infty\mid \prod_{i=-\infty}^{N-1} \tilde\Psi_i[t]
\prod_{j=-\infty}^{N-1} \Psi_j^G[\bar t] \mid-\infty\rangle =
 \\
= {\rm Det}_{-\infty < i,j < N}
\langle  -\infty\mid \tilde\Psi_i[t] \Psi_j^G[\bar t] \mid-\infty\rangle =
 \\
= {\rm Det}_{i,j<0} {\cal H}_{i+N,j+N}.
\end{array}
\label{pretafdet}
\ee
The last two steps here were introduction of "$GL(\infty)$-rotated" fermions,
\be
\tilde\Psi_i[t] \equiv e^{-H}\psi_i e^H; \ \ \

\Psi_j[\bar t] \equiv e^{\bar H} \psi_j e^{-\bar H};\ \ \
\Psi_j^G[\bar t] \equiv G\Psi_j[\bar t] G^{-1},
\label{bigpsi}
\ee
and application of the Wick theorem to express multifermion correlation
function through pair correlators
\be
\new
\begin{array}{c}
{\cal H}_{ij}(t,\bar t) \equiv
\langle  -\infty\mid \tilde\Psi_i[t] \Psi_j^G[\bar t] \mid-\infty\rangle =
 \\ =
\langle  -\infty\mid \tilde\Psi_i[t]\ G \ \Psi_j[\bar t] \mid-\infty\rangle ,
\end{array}
\label{Hmatrcor}
\ee
(once again the fact that $G^{-1}\mid-\infty\rangle = \mid-\infty\rangle$
was used). The only non-trivial dynamical information entered through
applicability of the Wick theorem, and for that  it was crucial that all the
operators $e^H,\ e^{\bar H},\ G$ are $quadratic$ exponents, i.e. can only
modify the shape of the propagator, but do not destroy the quadratic form of
the action (fields remain $free$).
This is exactly equivalent to the statement that "heisenberg" operators
$\Psi[t]$ are just "rotations"
of $\psi$, i.e. that transformations (\ref{bigpsi}) are $linear$.

We shall now describe these transformations in  a little more explicit form.
Namely, their entire time-dependence can be encoded in terms of "Shur
polinomials" $P_n(t)$.
These are defined to have a very simple generating
function (which we already encountered many times in the theory of matrix
models):
\be
\sum_{n\geq 0} P_n(t)z^n = \exp\left({\sum_{k=1}^{\infty} t_kz^k}\right)
\ee
(i.e. $P_0 = 1,\ \ P_1 = t_1,\ \ P_2 = \frac{t_1^2}{2} + t^2$ etc.), and
satisfy the relation
\be
\frac{\partial P_n}{\partial t_k} = P_{n-k}.
\ee
Since
\be
\exp\left({\sum_{k=1}^{\infty} t_kz^k}\right) =
\prod_{k>0} \left(\sum_{n_k\geq 0}\frac{1}{n_k!}\ t_k^{n_k}z^{kn_k}\right),
\nn
\ee
Shur polinomials can be also represented as
\be
P_n(t) = \sum_{\stackrel{\{n_k\}}{\sum_{k>0} kn_k = n}}
\left(\prod_{k> 0}\frac{1}{n_k!}\ t_k^{n_k}\right).
\label{Shupoex}
\ee
Now, since
\be
e^{-B}Ae^B = A + [A,B] + \frac{1}{2!}[[A,B],B] +
\frac{1}{3!}[[[A,B],B],B] + \ldots
\nn
\ee
and
\be
\phantom. [\tilde\psi_i,J_k] = \tilde\psi_{i+k}, \ \
[ [\tilde\psi_i,J_{k_1}], J_{k_2}] = \tilde\psi_{i+k_1+k_2}, \ \ldots,
\nn
\ee
we have for every fixed $k$:
\be
e^{-t_kJ_k} \tilde\psi_i e^{t_kJ_k} =
\sum_{n_k\geq 0} \frac{t_k^{n_k}}{n_k!}\ \tilde\psi_{i+kn_k}.
\nn
\ee
It remains to note that all the harmonics of $J$ in $H = \sum_{k>0} t_kJ_k$
commute with each other, to obtain:
\be
\new
\begin{array}{c}
\tilde\Psi_i(t) = e^{-H} \tilde\psi_i e^H =
\left( \prod_{k>0} e^{-t_kJ_k}\right) \tilde\psi_i
\left( \prod_{k>0}e^{t_kJ_k}\right) =  \\
= \sum_{n\geq 0}\tilde\psi_{i+n} \left(
 \sum_{\stackrel{\{n_k\}}{\sum_{k>0} kn_k = n}}
\left(\prod_{k> 0}\frac{1}{n_k!}\  t_k^{n_k}\right)\right)
\stackrel{(\ref{Shupoex})}{=} \\
= \sum_{n\geq 0}\tilde\psi_{i+n} P_n(t) = \sum_{l\geq i}\tilde\psi_{l}
P_{l-i}(t).
\end{array}
\ee
Similarly, relation $[J_k,\psi_j] = \psi_{k+j}$ implies, that
\be
\Psi_j(\bar t) = e^{\bar H}\psi_j e^{-\bar H} =
\sum_{n\geq 0}\psi_{j+n} P_n(\bar t) = \sum_{m\geq j}\psi_{m}P_{m-j}(\bar t)
\label{bigpsishur}
\ee
and finally\footnote{
Eqs.(\ref{bigpsishur}) can be  also interpreted as representations of Shur
polinomials in terms of fermionic correlators in the bare vacuum:
\be
&P_m(\bar t) = \langle -\infty \mid \tilde\psi_{j+m}e^{\bar H} \psi_j
\mid-\infty \rangle\ ; \nn \\
&P_m( t) = \langle -\infty \mid \tilde\psi_i e^{H} \psi_{i+m}
\mid-\infty \rangle\  \nn
\ee
}
\be
&{\cal H}_{ij} = \sum_{\stackrel{l\geq i}{m\geq j}}
\langle -\infty \mid \tilde\psi_l\ G\ \psi_m \mid-\infty \rangle\
P_{l-i}(t)P_{m-j}(\bar t) = \nn \\         & =
\sum_{\stackrel{l\geq i}{m\geq j}} T_{lm} P_{l-i}(t)P_{m-j}(\bar t),
\label{HversTlm}
\ee
which implies also that
\be
\frac{\partial{\cal H}_{ij}}{\partial t_k} = {\cal H}_{i+k,j}; \nn \\
\frac{\partial{\cal H}_{ij}}{\partial\bar t_k} = {\cal H}_{i,j+k} .
\label{todaeqforH}
\ee
Matrix
\be
T_{lm} \equiv \langle -\infty \mid \tilde\psi_l\ G\ \psi_m \mid-\infty \rangle
\ee
is the one which defines fermion rotations under the action of
$GL(\infty)$-group element $G$:
\be
&G\psi_mG^{-1} = \sum_{l\in Z} \psi_lT_{lm}; \nn \\
&G^{-1}\tilde\psi_l G = \sum_{m\in Z} T_{lm}\tilde\psi_m,\ {\rm or}\
G\tilde\psi_l G^{-1} = \sum_{m\in Z} (T^{-1})_{lm}\tilde\psi_m.
\ee
If $G=1$, $T_{lm} = \delta_{lm}$. If all $t_k = \bar t_k = 0$,
${\cal H}_{ij} = T_{ij}$.
