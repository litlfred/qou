**Definition (filtered differential algebra).**
*The Hecke algebra $H_n(R, q)$ with the confinement filtration $J^\bullet(q)$ ([confinement level](#def:confinement-level)) carries a natural differential $d$ induced by three Gröbner–Shirshov rewriting rules — the Hecke relation, far commutativity, and Yang–Baxter ([Hecke normal form](#def:hecke-normal-form)):*

```tex
\[
\begin{aligned}
  &d_{\mathrm{H}}(\sigma_i^2) = (q - q^{-1})\sigma_i + \mathbf{1}, \\
  &d_{\mathrm{F}}(\sigma_i \sigma_j) = \sigma_j \sigma_i \quad (|i - j| \geq 2), \\
  &d_{\mathrm{YB}}(\sigma_i \sigma_{i+1} \sigma_i) = \sigma_{i+1} \sigma_i \sigma_{i+1}.
\end{aligned}
\]
```

*Each rule lowers filtration degree. The direct sum $d = d_H + d_F + d_{YB}$ satisfies $d \circ d = 0$ on the filtered complex. This makes $(H_n(R, q), J^\bullet, d)$ a filtered differential algebra.*

**Proposition (GB spectral sequence).**
*The filtered differential algebra $(H_n(R, q), J^\bullet, d)$ has an associated spectral sequence $(E_r^{\ell, *}, d_r)$ with:*

$$
  E_0^{\ell, *} \;=\; J^\ell(q) / J^{\ell+1}(q)
  \qquad \text{(associated graded)},
$$

$$
  E_1^{\ell, *} \;=\; H^*\bigl(J^\ell / J^{\ell+1},\ d\bigr)
  \qquad \text{(Hochschild-type cohomology of each stratum)},
$$

*and higher pages $E_r^{\ell, *}$ obtained by successive homology of $d_r$.*

*Convergence:*

$$
  E_\infty^{\ell, *}
  \;\Longrightarrow\;
  \mathrm{gr}^\ell\bigl(H_n(R, q)\bigr).
$$

*The Markov trace $\mathrm{tr}_M: H_n(R, q) \to \mathbb{C}$ forms a $d$-closed linear functional. It descends to $E_\infty$.*

**Proof.**

**Derivation of $d \circ d = 0$ (via Hochschild complex).**

*The rewriting rules $d_H, d_F, d_{YB}$ define a reduction procedure. To obtain $d \circ d = 0$, we pass to the Hochschild cochain complex over the natural ground ring $R$:*

$$
  C^k(H_n(R, q), H_n(R, q))
  \;:=\;
  \mathrm{Hom}_R\bigl(H_n(R, q)^{\otimes k},\ H_n(R, q)\bigr),
$$

*where $R$ forms the categorical base ring. This forms the target of the fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ ([Tannaka–Krein reconstruction](#prop:tannaka-krein-reconstruction)). $R$ is the commutative ring in which Markov-trace values live before archimedean calibration $\tau \colon R \to \mathbb{R}$ ([categorical mass, Markov](#prop:categorical-mass-markov)).*

*Under different realisations ([knot operator energy](#def:knot-operator-energy)):*

- *Archimedean: $R$ contains $\mathbb{R}[q, q^{-1}]$, evaluated at $q = q_0 \in \mathbb{R}$.*
- *$p$-adic: $R$ contains $\mathbb{Q}_p[q, q^{-1}]$.*
- *Finite-field: $R$ contains $\mathbb{F}_p[q, q^{-1}]$.*

*The spectral-sequence construction operates over any such $R$. The physics application uses the archimedean realisation. The derivation is ring-agnostic. Complex numbers appear only as a derived embedding $R \hookrightarrow \mathbb{C}$ when we extract residues at roots of unity ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*

*We equip the complex with the standard Hochschild differential:*

$$
  (d\,f)(a_0 \otimes \cdots \otimes a_k)
  \;=\;
  a_0 \cdot f(a_1 \otimes \cdots \otimes a_k)
  + \sum_{i=0}^{k-1} (-1)^{i+1} f\bigl(a_0 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_k\bigr)
  + (-1)^{k+1} f(a_0 \otimes \cdots \otimes a_{k-1}) \cdot a_k.
$$

*The identity $d \circ d = 0$ is a classical theorem for any associative $R$-algebra. It holds verbatim for $H_n(R, q)$. The Markov trace $\mathrm{tr}_M$ forms a cyclic $0$-cochain (satisfying $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$). It is therefore $d$-closed at degree $0$.*

*The confinement filtration $J^\bullet(q)$ induces a decreasing filtration on $C^\bullet$:*

$$
  F^p C^k
  \;:=\;
  \{f \in C^k \mid f\bigl(J^{p_1}(q)^{\otimes k}\bigr) \subset J^{p + p_1}(q)\},
$$

*This filtration maintains compatibility with the Hochschild differential ($d(F^p) \subset F^p$), forming the filtered Hochschild complex.*

*Therefore:*

1. **$d \circ d = 0$ holds** *on the filtered complex.*
2. **Filtration preservation** *follows because $J^\bullet$ provides an ideal-filtration compatible with multiplication.*

*Hence $(C^\bullet(H_n(R, q)), d, F^\bullet)$ forms a filtered cochain complex with spectral sequence pages $(E_r^{p, q}, d_r)$.*

**Convergence $E_\infty \Rightarrow \mathrm{gr}\,H_n(R, q)$.**

*The filtration $J^\bullet(q)$ is:*

1. *Bounded below: $J^0 = H_n(R, q)$.*
2. *Exhaustive: $\bigcap_\ell J^\ell = 0$ for any generic $q = q_0$. Partition energies $E_\ell(q_0)$ are distinct and positive ([confinement level, uniqueness](#prop:confinement-level-unique)).*
3. *Finite-dimensional at each degree $J^\ell(q)/J^{\ell+1}(q)$.*

*These provide the classical convergence conditions for a filtered spectral sequence. Therefore:*

$$
  E_\infty^{p, q}
  \;\cong\;
  \mathrm{gr}^p\,H^{p+q}\bigl(H_n(R, q), H_n(R, q)\bigr),
$$

*The total Hochschild cohomology equals the sum over pages. Pairing this with the Markov-trace cocycle $\mathrm{tr}_M$ yields the six-term mass decomposition.*
