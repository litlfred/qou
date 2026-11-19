**Algorithm (Gröbner–Shirshov Coxeter-length filtration and $E_2$ spectral-sequence collapse).**
*Construct the ascending Coxeter-length filtration $F_\bullet H_n(q)$ induced by the Gröbner–Shirshov basis of $H_n(q)$, compute its associated graded module $\bigoplus_{\ell=0}^{\binom{n}{2}} \mathrm{gr}_\ell H_n(q)$, and certify $E_2$-page collapse ($d_r = 0$ for all $r \ge 2$).*

### Input

- *Strand count $n \in \mathbb{N}_{\ge 1}$ and Iwahori–Hecke algebra $H_n(q)$ in its reduced Coxeter basis $\{T_w : w \in S_n\}$.*

### Output

- *Ascending filtration $0 = F_{-1} \subset F_0 \subset F_1 \subset \cdots \subset F_{\binom{n}{2}} = H_n(q)$ with $F_\ell = \mathrm{span}_{\mathbb{Z}[q, q^{-1}]}\{T_w : \ell(w) \le \ell\}$, associated graded ranks $\mathrm{rk}\,\mathrm{gr}_\ell H_n(q) = |\{w \in S_n : \ell(w) = \ell\}|$, and vanishing differentials $d_r = 0$ for all $r \ge 2$.*

### Algorithm

1. **Partition by Coxeter inversion count:** For each $w \in S_n$, compute its inversion number $\ell(w) = |\{(i, j) : 1 \le i < j \le n,\; w(i) > w(j)\}| \in \{0, 1, \dots, \binom{n}{2}\}$ and assign $T_w$ to filtration stratum $F_{\ell(w)}$.
2. **Form the associated graded algebra:** Verify that for $\ell(u) = \ell_1$ and $\ell(v) = \ell_2$, quadratic reduction $T_s^2 = h\,T_s + 1$ keeps $T_u T_v \in F_{\ell_1 + \ell_2}$, making $H_n(q)$ a filtered algebra whose graded quotient $\mathrm{gr}_\bullet H_n(q) = \bigoplus_{\ell=0}^{\binom{n}{2}} F_\ell / F_{\ell - 1}$ has Poincaré polynomial
   $$
     \sum_{\ell=0}^{\binom{n}{2}} \bigl(\mathrm{rk}\,\mathrm{gr}_\ell H_n(q)\bigr)\,t^\ell
     \;=\;
     \prod_{k=1}^{n} \frac{1 - t^k}{1 - t}.
   $$
3. **Certify $E_2$ collapse:** Because $h = q - q^{-1}$ carries valuation $1$ in the classical-limit ideal $J = (q - 1)$ and the Gröbner–Shirshov basis is confluent across all overlaps without syzygy defects in degree $\ge 2$, verify that the induced differentials $d_r \colon E_r^{p,q} \to E_r^{p+r,\, q-r+1}$ vanish identically for every $r \ge 2$.

### Termination and Complexity

Inversion counting takes $O(n^2)$ per permutation across $|S_n| = n!$ basis elements, for a total of $O(n^2\,n!)$ integer operations; the Poincaré rank profile itself is computed in $O(n^3)$ integer additions by polynomial multiplication without enumerating $S_n$.

### Mathematical Justification

By [the Gröbner–Shirshov spectral-sequence proposition](#prop:gb-spectral-sequence), confluence of the quadratic Hecke rewriting system forces the filtration spectral sequence to degenerate at $E_2$, preventing higher differentials from mixing distinct Coxeter length strata during the $q \to 1$ jet transport of [Step 8](#alg:jet-prefix-transport).
