**Setting.** *Let $R$ be a commutative ring and $q \in R^\times$. The Hecke algebra $H_n(R, q)$ is free over $R$ with standard basis $\{T_w : w \in S_n\}$ \cite{geckpfeiffer2000}, and for a simple reflection $s$*

```tex
\[
  T_s T_w \;=\;
  \begin{cases}
    T_{sw}, & \ell(sw) = \ell(w) + 1, \\
    (q - q^{-1})\,T_w + T_{sw}, & \ell(sw) = \ell(w) - 1,
  \end{cases}
\]
```

*where $\ell$ is the Coxeter length (the number of inversions). Write $N = \ell(w_0) = n(n-1)/2$.*

**Definition (length filtration).** *For $a \in \mathbb{Z}$ put $L_a = \operatorname{span}_R\{T_w : \ell(w) \le a\}$. On the Hochschild cochains $C^k = \operatorname{Hom}_R\bigl(H_n(R, q)^{\otimes k}, H_n(R, q)\bigr)$ put*

$$
  F^p C^k \;=\; \bigl\{\, f \in C^k \;:\; f(L_{a_1} \otimes \cdots \otimes L_{a_k}) \subseteq L_{a_1 + \cdots + a_k - p} \text{ for all } a_1, \dots, a_k \,\bigr\}.
$$

*Equivalently, $F^p C^k$ is spanned by the elementary cochains $T_{w_1} \otimes \cdots \otimes T_{w_k} \mapsto T_v$ of weight $\ell(w_1) + \cdots + \ell(w_k) - \ell(v) \ge p$.*

**Proposition (length spectral sequence).** *Let $d$ be the Hochschild differential of $H_n(R, q)$ with coefficients in itself, and index pages $E_r^{p,k}$ by the filtration degree $p$ and the cochain degree $k$.*

1. *$L_a L_b \subseteq L_{a+b}$, and $d(F^p C^k) \subseteq F^p C^{k+1}$, so $(C^\bullet, d, F^\bullet)$ is a filtered cochain complex with a spectral sequence $(E_r^{p,k}, d_r)$, $d_r \colon E_r^{p,k} \to E_r^{p+r,k+1}$.*
2. *$E_1^{p,k}$ is the weight-$p$ part of $HH^k\bigl(\operatorname{gr}_L H_n, \operatorname{gr}_L H_n\bigr)$, where $\operatorname{gr}_L H_n$ is the nil-Coxeter algebra: basis $\{\bar T_w\}$ with $\bar T_u \bar T_w = \bar T_{uw}$ if $\ell(uw) = \ell(u) + \ell(w)$ and $0$ otherwise.*
3. *In cochain degree $k$ the filtration is finite, with weights in $[-N, kN]$. Hence $E_r^{\bullet,k} = E_\infty^{\bullet,k}$ for $r > (k+2)N$, and*

$$
  E_\infty^{p,k} \;\cong\; \operatorname{gr}^p HH^k\bigl(H_n(R, q), H_n(R, q)\bigr).
$$

*When $R$ is a field over which $H_n(R, q)$ is split semisimple, the abutment is the centre $Z(H_n(R, q))$ in degree $0$, of rank the number of partitions of $n$, and $0$ in positive degree.*

**Proof.**

*(1) Multiplicativity.* *If $\ell(w) \le b$, the displayed rule shows that $T_s T_w$ lies in $L_{b+1}$. Writing $T_u = T_{s_1} \cdots T_{s_a}$ along a reduced word of $u$ and inducting on $a$ gives $T_u L_b \subseteq L_{a+b}$, hence $L_a L_b \subseteq L_{a+b}$.*

*Filtration preservation.* *The Hochschild differential is*

```tex
\[
  (d f)(x_0 \otimes \cdots \otimes x_k)
  \;=\;
  x_0\, f(x_1 \otimes \cdots \otimes x_k)
  + \sum_{i=0}^{k-1} (-1)^{i+1} f(x_0 \otimes \cdots \otimes x_i x_{i+1} \otimes \cdots \otimes x_k)
  + (-1)^{k+1} f(x_0 \otimes \cdots \otimes x_{k-1})\, x_k .
\]
```

*Let $f \in F^p C^k$ and $x_i \in L_{a_i}$, and put $A = a_0 + \cdots + a_k$. The first term lies in $L_{a_0} L_{A - a_0 - p} \subseteq L_{A - p}$. In the middle terms $x_i x_{i+1} \in L_{a_i + a_{i+1}}$, so each lies in $L_{A - p}$. The last term is symmetric to the first. Hence $d f \in F^p C^{k+1}$. The identity $d \circ d = 0$ holds for every associative $R$-algebra, and a filtered cochain complex has a spectral sequence with $E_0^{p,\bullet} = F^p C^\bullet / F^{p+1} C^\bullet$ \cite{weibel1994}.*

*(2) The first page.* *The filtrations are split by the standard basis, so $\operatorname{gr}^p C^k$ is the span of the elementary cochains of weight exactly $p$, and $d_0$ is the weight-preserving part of $d$. In the product $T_u T_w$ only the coefficient of $T_{uw}$ with $\ell(uw) = \ell(u) + \ell(w)$ has top weight: by induction on $\ell(u)$ using the displayed rule, $T_u T_w = T_{uw}$ when the lengths add and $T_u T_w \in L_{\ell(u)+\ell(w)-1}$ otherwise. So the weight-preserving part of the multiplication is the nil-Coxeter product, and $d_0$ is the Hochschild differential of $\operatorname{gr}_L H_n$ restricted to weight $p$. Taking cohomology gives $E_1$.*

*(3) Convergence.* *An elementary cochain in $C^k$ has weight between $0 - N = -N$ and $kN - 0 = kN$, so $F^{-N} C^k = C^k$ and $F^{kN+1} C^k = 0$. A differential $d_r$ out of $E_r^{p,k}$ lands in filtration degree $p + r \le (k+1)N$ with $p \ge -N$, so it vanishes for $r > (k+2)N$, and one into $E_r^{p,k}$ vanishes for $r > (k+1)N$. A finite filtration of each cochain group gives the stated convergence \cite{weibel1994}. For a split semisimple algebra, $HH^0$ is the centre and $HH^k = 0$ for $k > 0$, since such an algebra is separable. $\qquad\blacksquare$*

**Example ($n = 3$).** *An exact computation over $\mathbb{F}_P$ at $q = 2$ and $q = 3$, for two primes $P$ (`computations/probes/gb_spectral_sequence_h3_probe.py`), gives the following. In cochain degree $0$, $E_1 = E_\infty$ has one class in each of the filtration degrees $0, -2, -3$, matching the rank-$3$ centre of $H_3$. In degree $1$, $E_1$ has classes in filtration degrees $0$ and $-2$. In degree $2$, $E_1$ is two-dimensional in filtration degree $2$. The differentials $d_1$ and $d_3$ vanish, while $d_2$ and $d_4$ each have rank $1$ from degree $1$ to degree $2$. So $E_5 = E_\infty$ and the sequence does not collapse at $E_2$.*
