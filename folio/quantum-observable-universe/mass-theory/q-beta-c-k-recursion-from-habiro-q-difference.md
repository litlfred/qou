*Let $F(q) \in \mathbb{Z}[q, q^{-1}]^\wedge$ be a fibre-level Habiro element associated to the operator-valued $T_\beta$ selection ([Min-Frobenius-norm collapse](t-beta-markov-frobenius-collapse.md)). Let $F(q)$ satisfy a $q$-difference equation of depth $d$:*

$$
F(q\xi) \;=\; R(q,\xi)\cdot F(\xi), \qquad R(q,\xi) \in \mathbb{Q}(q)[\xi, \xi^{-1}] \text{ of degree} \le d.
$$

*The precision-ladder coefficients $c_k$ satisfy a depth-$d$ linear recursion:*

$$
c_{k+1} \;=\; \sum_{j=1}^{d} a_j(q_0)\cdot c_{k+1-j}, \qquad a_j(q_0) \in \mathbb{Q}(q_0),
$$

*with kernel coefficients $\{a_j\}$ extracted from $R(q_0, \xi)$ via the $(u;u)_m \to u^k$ Habiro change-of-basis.*

The operator content is $T_\beta = S \cdot \mathbf{1}$, with $S$ pinned by the SDP constraint. The selector direction is $S$-independent and $q$-rational. The scalar $S = \mathfrak{Q}_\beta/E_0$ is not the ladder normalization. Together, these define $F(q) = \mathfrak{Q}_\beta(q)/[Q_A(q) \cdot \cos(\alpha_{\mathrm{eff}}(q))]$ as a single fibre-level Habiro object. Its $q$-difference structure generates the $c_k$.

The sequence $c_2, \ldots, c_8$ collapses to the proved seed $c_2 = -1$ and a kernel $R(q_0, \xi)$ of bounded degree $d$. The recursion generates $c_3, \ldots, c_8$ automatically.

We write the recursion coefficients as elementary symmetric polynomials $a_j = e_j(\{r_\lambda\})$ of the per-mode rates $r_\lambda = (q-1)\mu_\lambda$. Under the bar involution $q \mapsto q^{-1}$, the rates are bar-odd. We formally prove that $a_j$ alternates bar-parity. The recursion step and the parity-alternation theorem form the structural law behind the ladder's parity bookkeeping.

The cyclotomic factors $\Phi_d$ for $d \in \{2,3,6\}$ and for all primes $p$ are self-reciprocal. Divisibility by $\Phi_n$ is invariant under the bar involution for every $n > 1$. The identity $\Phi_n(1/q)\,q^{\varphi(n)} = \Phi_n(q)$ guarantees period-3 closure.

The Habiro element $F(q)$ is the trace of the $q$-heat kernel over the Hecke modules:

$$Z_q(t) = \sum_{\lambda \in \Lambda} d_\lambda(q) \cdot \exp_q(-\mu_\lambda(q) \cdot t).$$

The $q$-difference equation for $F(q)$ derives from the depth-1 Jackson equations of each mode. The net partition function satisfies a $q$-difference equation of depth $|\Lambda|$. The $c_k$ coefficients are extracted at $q_0$.

At the fibre level, $Z_q$ is a Hahn--Exton q-Bessel function. The coefficients $c_k$ obey the q-Bessel second-order q-difference equation. This identification applies at the fibre level only. Archimedean closure of $c_3$ via a substrate-fixed q-Bessel is refuted. The q-Bessel object lives in the brane-tower limit.
