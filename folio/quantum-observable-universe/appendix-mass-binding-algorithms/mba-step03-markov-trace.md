**Algorithm (Convention-D Markov trace on $H_n(q)$).**
*Evaluate the normalised Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q)$ under Convention D ($z = z_D = \frac{q^3}{q^2 + 1}$) either symbolically as an exact rational function in $\mathbb{Q}(q)$ or numerically in arbitrary-precision ball arithmetic at $q = q_0$.*

### Input

- *Hecke normal form $x = \mathrm{NF}(w) = \sum_{u \in S_n} c_u(q)\,T_u \in H_n(q)$ (from [Step 2](#alg:gs-reduce-to-hecke-nf)), or a monotone generator factorisation $w = \prod_{g=1}^{n-1} O_g(\sigma_g)$.*
- *Convention-D Markov parameter $z_D(q) = \frac{q^3}{q^2 + 1} \in \mathbb{Q}(q)$.*

### Output

- *Exact rational function $\mathrm{tr}_M(x) \in \mathbb{Q}(q)$ (symbolic regime), or enclosed real scalar $\mathrm{tr}_M(x)\big|_{q = q_0}$ at $\ge 80$ decimal digits (numerical regime).*

### Algorithm

1. **Direct strand-elimination descent ($n$ arbitrary, general words):**
   Using the Jones–Coxeter double-coset decomposition $H_n(q) = H_{n-1}(q) \oplus H_{n-1}(q)\,T_{s_{n-1}}\,H_{n-1}(q)$, express each basis element $T_u$ ($u \in S_n$) either as $T_u \in H_{n-1}(q)$ (if $u(n) = n$) or as $a\,T_{s_{n-1}}\,b$ with $a, b \in H_{n-1}(q)$ (if $u(n) < n$). Apply trace cyclicity and the Markov stabilisation rule
   $$
     \mathrm{tr}_M(a\,T_{s_{n-1}}\,b)
     \;=\;
     \mathrm{tr}_M(b\,a\,T_{s_{n-1}})
     \;=\;
     z_D(q)\,\mathrm{tr}_M(b\,a),
   $$
   reducing $b\,a \in H_{n-1}(q)$ via [Step 2](#alg:gs-reduce-to-hecke-nf) and recursing down to $H_1(q) \cong \mathbb{Q}(q)$ where $\mathrm{tr}_M(1) = 1$.
2. **Monotone fine-Bratteli transfer sweep (multi-strand braids with non-decreasing generator index):**
   When $x = \prod_{g=1}^{n-1} O_g(\sigma_g)$ visits each adjacent generator $\sigma_g$ in non-decreasing order, evaluate the character sum $\mathrm{tr}_M(x) = \sum_{\lambda \vdash n,\, \ell(\lambda) \le 2} w_\lambda(z_D)\,\chi^\lambda(x)$ on the multiplicity-free Hoefsmit–Gelfand–Zetlin basis indexed by standard Young tableau chains $\varnothing = \lambda^{(0)} \subset \lambda^{(1)} \subset \cdots \subset \lambda^{(n)} = \lambda$. Because $O_g(\sigma_g)$ acts solely on the step $\lambda^{(g-1)} \subset \lambda^{(g)} \subset \lambda^{(g+1)}$ and trace closure discards off-diagonal blocks, propagate scalar weights forward along edges of the Young lattice from rank $0$ to rank $n$ without instantiating $d_\lambda \times d_\lambda$ matrices.

### Termination and Complexity

Method 1 strictly decreases the strand index $n \mapsto n - 1$ at every recursive step and terminates in at most $n - 1$ levels; memoising trace values $\mathrm{tr}_M(T_u)$ on minimal conjugacy-class representatives in $S_n$ reduces evaluation of $\mathrm{tr}_M(x)$ to an $O(|\mathrm{supp}(x)|)$ dot product. Method 2 runs in time linear in the number of fine-Bratteli edges at $\ell(\lambda) \le 2$, which grows polynomially per two-row stratum rather than as $n!$.

### Mathematical Justification

1. **Uniqueness of the Markov functional:** By [the axiomatic closed-form proposition](#prop:markov-trace-axiomatic-closed-form) and [the recursive Markov-trace reducer](#prop:markov-trace-recursive-reducer), $\mathrm{tr}_M$ is the unique $\mathbb{Q}(q)$-linear trace on the inductive tower $\{H_n(q)\}_{n \ge 1}$ obeying $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$, $\mathrm{tr}_M(a\,T_{s_{n-1}}) = z\,\mathrm{tr}_M(a)$ for $a \in H_{n-1}(q)$, and $\mathrm{tr}_M(1) = 1$.
2. **Convention-D selection:** By [Convention-D uniqueness](#prop:convention-d-kills-antisymmetriser), $z_D = \frac{q^3}{q^2 + 1}$ is the unique non-trivial Markov parameter at which the three-row antisymmetric Wenzl weight $w_{(1^3)}(z)$ vanishes identically, projecting the bare Markov trace onto two-row spin/isospin strata while isolating higher-row contributions to the renormalised GPMT trace of [Step 5](#alg:wedderburn-decomposition).
