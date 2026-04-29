**Proof of [partition-depth stratification of $\Phi_q$](#prop:quantum-dilogarithm-stratified).**

*Step 1 (Frobenius dual decomposition of $Z(A)$).* By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the centre $Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda$
admits the GB-depth grading
$Z(A) = \bigoplus_{k \geq 0} Z^{(k)}(A)$. The Frobenius pairing
$\langle a, b \rangle = \int_A a \cdot b$ restricts to $Z(A)$ as a
non-degenerate bilinear form, and the depth strata $Z^{(k)}(A)$ are
mutually orthogonal under this pairing
([Frobenius duality of strata](#prop:spectral-sequence-collapse)
"§Frobenius duality of strata"):

$$
  \langle Z^{(k)}(A),\, Z^{(\ell)}(A) \rangle \;=\; 0
  \qquad \text{whenever } k + \ell \neq N,
$$

where $N$ is the maximal GB-depth in $Z(A)$. The self-dual pairing
$Z^{(k)} \times Z^{(N-k)} \to R$ is the **Poincaré duality of
curvature-rank strata**.

*Step 2 (existence of $\phi_q^{(k)}(z_i)$).* By
[cor: quantum dilogarithm](#cor:quantum-dilogarithm), the level-$i$
torsion-volume contribution to the mass is
$\mathrm{tr}_{\mathrm{trans}}(\varrho, p_i) = \Phi_q(z_i)$. Since the
mass functional is centre-valued by
[categorical mass = Markov trace](#prop:categorical-mass-markov), the
$\Phi_q(z_i)$-action on $Z(A)$ via the Markov pairing factors through
$Z(A)$. Decomposing along the depth grading,

$$
  \Phi_q(z_i) \cdot \mathrm{id}_{Z(A)}
  \;=\;
  \sum_{k \geq 0} \Phi_q(z_i) \cdot \mathrm{proj}_{Z^{(k)}(A)}.
$$

Define $\phi_q^{(k)}(z_i) := \mathrm{proj}_{Z^{(k)}(A)}(\Phi_q(z_i))$
as the depth-$k$ projection of the Frobenius dual.

*Step 3 (truncation identity at depth $k$).* The cyclotomic factor
$(1 - q^{-k} z_i)^{-1}$ in $\Phi_q(z_i)$ is, by inspection of the
$q$-Pochhammer expansion, the unique factor whose pole locus
$z_i = q^k$ is the **defining locus of partition depth $k$** in the
GB stratification: the partitions $\lambda \vdash n$ with
$\mathrm{depth}_{\mathrm{GB}}(\lambda) = k$ are exactly those whose
$q$-character $\chi_\lambda(q)$ has a leading-order pole at $z_i = q^k$
under the Markov-trace pairing. Consequently the partial product

$$
  \Phi_q^{[\leq k]}(z_i) \;:=\; \prod_{j = 1}^{k} (1 - q^{-j} z_i)^{-1}
$$

contains exactly the cyclotomic factors corresponding to depths
$\leq k$, and

$$
  \Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)
  \;\equiv\; \phi_q^{(k)}(z_i) \pmod{\bigoplus_{\ell \neq k} Z^{(\ell)}(A)}.
$$

*Step 4 (Frobenius truncation for $T_w$).* For $T_w \in H_n(R, q)$
with NF support depth
$k_\star(T_w) = \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda)$,
$T_w$ has zero projection on $Z^{(k)}(A)$ for every $k > k_\star(T_w)$
by definition of $k_\star$. By Step 3, $\phi_q^{(k)}(z_i) \in Z^{(k)}(A)$,
so

$$
  \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle \;=\; 0
  \qquad \text{for } k > k_\star(T_w).
$$

The Frobenius-paired sum truncates:

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \sum_{k = 0}^{\infty} \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle
  \;=\;
  \sum_{k = 0}^{k_\star(T_w)} \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr).
$$

The second equality uses depth orthogonality (Step 1); the third uses
Step 3's identification of the partial product with the
$\bigoplus_{j \leq k_\star(T_w)} Z^{(j)}$-content. $\square$

**Open: numerical bound.**
The proof above is a Frobenius-paired *equality*, not a numerical
identity. It says the Frobenius-pairing of $\Phi_q(z_i)$ with $T_w$
equals the Frobenius-pairing of $\Phi_q^{[\leq k_\star(T_w)]}(z_i)$
with $T_w$. To conclude that the *numerical* mass formula evaluated
with $\Phi_q$ replaced by $\Phi_q^{[\leq k_\star(T_w)]}$ gives the same
answer, one needs the projections $\mathrm{proj}_{Z^{(k)}}(\Phi_q(z_i))$
to be uniformly bounded as $|z_i| \to q$ — equivalently, no spurious
analytic mass leaks into $Z^{(k)}(A)$ from the divergent infinite
product. Establishing this uniform bound is the conjectural target of
[$z$-Habiro completion](#conj:brane-tower-z-habiro) and the open part
of [$\Phi_q$ categorical truncation](#prop:phi-q-categorical-truncation).

The argument above is solid as a **categorical (Frobenius-paired)
identity** but does not by itself rule out that the infinite analytic
product diverges at $|z_i| = q$ in a way that the finite Frobenius
truncation does not capture in real-valued terms. Step 3's identification
of cyclotomic factors with depth strata also requires a careful
argument at the level of the $q$-character expansion; this is
asserted, not derived in detail.
