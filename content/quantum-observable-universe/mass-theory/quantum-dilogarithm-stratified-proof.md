**Proof of [partition-depth stratification of $\Phi_q$](#prop:quantum-dilogarithm-stratified).**

*Step 1 (Frobenius dual decomposition of $Z(A)$).* By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification)
— **together with the partition-vs-word identification this proof itself
flags as unestablished at Step 3 below, and which is not supplied by that
proposition** —
the centre $Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda$
admits the GB-depth grading
$Z(A) = \bigoplus_{k \geq 0} Z^{(k)}(A)$. The Frobenius pairing
$\langle a, b \rangle = \int_A a \cdot b$ restricts to $Z(A)$ as a
non-degenerate bilinear form, and the depth strata $Z^{(k)}(A)$ are
mutually orthogonal under this pairing
([Frobenius duality of strata](#prf:spectral-sequence-collapse)
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

*Step 3 (cyclotomic factors $\leftrightarrow$ depth-$k$ partitions).*
The cyclotomic factor $(1 - q^{-k} z_i)^{-1}$ in $\Phi_q(z_i)$ has its
pole locus at $z_i = q^k$. We identify this locus with the
depth-$k$ centre stratum $Z^{(k)}(A)$ via the $q$-content / hook-length
structure:

(a) The q-deformed Wedderburn-block weight is
$w_\lambda(q) = \dim_q^2 V_\lambda / [n]_q!$ (distinct from the
classical Plancherel measure $w_\lambda(1) = (\dim V_\lambda)^2/n!$ —
the two coincide at $q = 1$; see
[`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)),
where
$\dim_q V_\lambda = [n]_q! \,/\, \prod_{\square \in \lambda} [h(\square)]_q$
and $[h]_q = (q^h - q^{-h})/(q - q^{-1})$ is the symmetric quantum
integer
([Hoefsmit pipeline](#conj:hoefsmit-scattering-pipeline)).

(b) The hook lengths $h(\square)$ for $\square \in \lambda$ encode
the partition's depth in the GB filtration. Here
$\mathrm{depth}_{\mathrm{GB}}(\lambda) = \max_{\square \in \lambda} h(\square)$
(the partition's **maximum hook length**) is a *definition* — it is
`QOU.BraidKnot.gbDepth`, the supremum of the hook length over the
cells of $\lambda$ — not a consequence of
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
which stratifies $J^{\,r}/J^{\,r+1}$ by the curvature rank $r(T_w)$ of
**words** and mentions no partition. The two are different indexings of
depth, and the reading of $\mathrm{depth}_{\mathrm{GB}}(\lambda)$ as
the minimal number of $R_H, R_{YB}$ rewrites needed to put any element
of the $\lambda$-isotypic component in NF is the identification of the
partition grading with the word filtration, which that proposition does
not supply.

(c) Therefore $\dim_q V_\lambda$ has a factor of $[k]_q$ in its
hook-length expansion exactly when $\lambda$ contains a box with
$h(\square) = k$, equivalently $\mathrm{depth}_{\mathrm{GB}}(\lambda) \geq k$.
Under the substitution $z_i \to q^k$, the factor $[k]_q$ vanishes —
$\dim_q V_\lambda(q)\big|_{z_i = q^k}$ has a zero, and the
corresponding $w_\lambda^{-1}$ specialisation has a pole.

(d) The Markov-trace generating function for the centre is the
formal series
$F_n(z) = \sum_{\lambda \vdash n} \dim_q^{-1}(V_\lambda) \cdot z^{|\lambda|}$,
and its expansion as an infinite product in $z$ is
$F_n(z) = \prod_{k \geq 1} (1 - q^{-k} z)^{-c_k(n)} \cdot u_n(q)$
where $c_k(n) = \#\{\lambda \vdash n : \max\text{-hook}(\lambda) = k\}$
and $u_n(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is a unit. The exponent
$c_k(n)$ counts depth-exactly-$k$ partitions; the factor
$(1 - q^{-k} z)^{-c_k(n)}$ contributes the depth-$k$ stratum of $Z(A)$.

(e) The single-stratum factor $(1 - q^{-k}z)^{-1}$ in $\Phi_q$ is
the $c_k = 1$ specialisation of (d) — applicable when each depth-$k$
stratum is one-dimensional or when factoring over irreducible
strata. For the brane-tower, each exceptional divisor $p_i$
contributes one $(1 - q^{-k} z_i)^{-1}$ per depth $k$, and the full
$\Phi_q(z_i) = \prod_k (1 - q^{-k} z_i)^{-1}$ is the universal
generating function over all depths.

(f) Combining (a)–(e): the partial product
$\Phi_q^{[\leq k]}(z_i) = \prod_{j=1}^{k}(1-q^{-j}z_i)^{-1}$ generates
exactly the contributions from depths $1, 2, \ldots, k$, and the
truncation increment
$\Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)$ is the
depth-exactly-$k$ generator. Identifying this with the Frobenius dual
$\phi_q^{(k)}(z_i)$ from Step 2 (modulo orthogonal strata) gives

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

**Open: canonical bound.**
The proof above is a Frobenius-paired *equality*, not a canonical
identity. It says the Frobenius-pairing of $\Phi_q(z_i)$ with $T_w$
equals the Frobenius-pairing of $\Phi_q^{[\leq k_\star(T_w)]}(z_i)$
with $T_w$. To conclude that the *canonical* mass formula evaluated
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
truncation does not capture in real-valued terms. Step 3's
identification (a)–(f) reduces the cyclotomic-factor / depth-stratum
correspondence to the standard $q$-content / hook-length formula plus
[curvature-rank stratification §Step 3](#prop:curvature-rank-gb-stratification)
(GB-depth = max hook length), so the structural identification is now
explicit — **but "explicit" here means *written down*, not *established*.
The citation does not supply the identification; the passage above, at
"not a consequence of [curvature-rank stratification] … which … mentions no
partition", states the position of this proof.** The remaining open piece in Step 3 is **(d)'s product
expansion** $F_n(z) = \prod_k (1 - q^{-k}z)^{-c_k(n)} \cdot u_n(q)$:
the existence of such an expansion follows from finiteness of
$\dim_q^{-1}$ as a Laurent polynomial and unique factorisation in
$\mathbb{Z}[q^{\pm 1/2}][z]$, but the explicit identification of the
exponents $c_k(n)$ with $\#\{\lambda : \max\text{-hook} = k\}$
requires verification on small cases (D's $H_6$ and ${}^3\mathrm{He}$'s
$H_9$ are tractable computations).
