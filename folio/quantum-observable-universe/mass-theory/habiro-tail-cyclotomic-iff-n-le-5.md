**Proposition (computer-assisted).** *Let $S(n) = \sum_{\lambda \vdash n}\dim_q(\lambda)$ with
balanced quantum integers, and $D(n) = S(n) - S(n-1) - [n-1]_q\,S(n-2)$. Then $D(n)$ is of the
form $c\,q^j\prod_i\Phi_{k_i}(q)$ with $c \in \mathbb Z$ if and only if $n \le 5$.*

*Proof.* For $n \le 5$ the factorisations are explicit: $D(2) = D(3) = 0$,
$D(4) = q^{-2}\Phi_1^2\Phi_3$ and $D(5) = 2q^{-4}\Phi_1^2\Phi_2^2\Phi_3\Phi_6$, derived from the
hook-length formula in `QOU.Mass.CyclotomicBoundaryCertified`. For $6 \le n \le 8$ the same module
gives a finite mod-$p$ order witness that refutes every such factorisation.

For $n \ge 9$, put $q = e^t$ and write $D(n) = d_2t^2 + d_4t^4 + O(t^6)$. A product
$c\,q^j\prod\Phi_{k_i}$ with the factors $(q-1)$ removed has $12\kappa_2 = \sum_i J_2(k_i) \in \mathbb Z$
\cite{billeyswanson2023}, and for $D(n)$ this quantity is $24d_4/d_2 - 2$. The closed forms of
$d_2$ and $d_4$ in the involution numbers $I_{n-8}$, $I_{n-9}$, the 2-adic valuation of $I_m$
(`QOU.Mass.InvolutionTwoAdic`) and a size bound show that $d_2 \nmid 24d_4$ for every $n \ge 9$.
The derivation is given in
[the cyclotomic boundary conjecture](#conj:cyclotomic-boundary-at-keystone). $\square$
