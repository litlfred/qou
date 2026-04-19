Let $H_n(q)$ be the Iwahori--Hecke algebra with generators
$T_1, \ldots, T_{n-1}$ and defining relations

$$
\begin{aligned}
  \text{(H1)}\quad & T_i^2 = (q - q^{-1})\,T_i + 1, \\
  \text{(H2)}\quad & T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}, \\
  \text{(H3)}\quad & T_i T_j = T_j T_i \qquad (|i - j| \geq 2).
\end{aligned}
$$

The Lean sibling indexes generators $0$-based via
`HeckeGen n = Fin n`, so $T_i$ in this prose corresponds to
`⟨i - 1⟩ : HeckeGen n` in `UGB.GrobnerShirshov.HeckeGS`.

Let $\rho \colon \mathbb{Z} B_n \to H_n(q)$ be the Jones--Iwahori
representation of the braid group and $\mathrm{tr}_M$ the Markov
trace ([Markov trace](quantum-observable-universe:thm:jones-markov-trace));
in the Lean formalisation the Hecke parameter is a real
$q > 0$, $q \neq 1$ (the field `HeckeParams.q_ne_one`), and the
trace is the real-valued evaluation
$\mathrm{tr}_M \colon H_n(q) \to \mathbb{R}$ at that parameter.
Write $\mathrm{NF}(f)$ for the Gröbner--Shirshov normal form of
$f \in H_n(q)$ under (H1)/(H2)/(H3) oriented with leading monomials
$T_i^2$, $T_i T_{i+1} T_i$, and $T_i T_j$ ($i > j + 1$).

**Proposition.** Let $\beta \in B_n$ and write $\widehat{\beta}$
for its Markov closure.

1. (H1), oriented as $T_i^2 \to (q - q^{-1})\,T_i + 1$, is the
   Jones skein relation $L_+ - L_- = (q - q^{-1})\,L_0$ under the
   dictionary $L_+ \leftrightarrow T_i^2$,
   $L_0 \leftrightarrow T_i$, $L_- \leftrightarrow 1$. Rules (H2)
   and (H3) preserve the multiset of leading coefficients.

2. $J_{\widehat{\beta}}(q)
     = \mathrm{tr}_M\!\bigl(\mathrm{NF}(\rho(\beta))\bigr)$.

3. The Hecke cost
   $
     \mathrm{cost}(f) := \sum_{m \in \mathrm{supp}(f)} |c_m(q)|
   $
   (the `heckeCost` function of the Lean sibling,
   `UGB.GrobnerShirshov.Hecke.heckeCost`), evaluated on
   $\mathrm{NF}(\rho(\beta))$, is independent of the reduction
   order.

*Proof.* Expanding $\mathrm{heckeRelation}$ gives the term list
$([T_i, T_i], 1),\; ([T_i], -(q - q^{-1})),\; ([\,], -1)$, which
matches the skein weights $(1, -(q - q^{-1}), -1)$ on
$(L_+, L_0, L_-)$; this is (1). For (2),
[Buchberger's theorem](#thm:ugb-buchberger) applied to
(H1)/(H2)/(H3) --- whose S-polynomials all resolve by
[S-polynomial decomposition](#prop:ugb-s-poly-decomposition) ---
implies that $\mathrm{NF}(\rho(\beta))$ is unique. The Markov
trace of this normal form equals the writhe-normalised Jones
polynomial of $\widehat{\beta}$ by Jones 1987, Theorem 5.1.
Claim (3) is then immediate: equal normal forms have equal cost.
$\square$
