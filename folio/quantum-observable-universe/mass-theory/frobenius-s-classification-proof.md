*Proof.*
We verify each $S$-eigenvalue in turn.

**Coefficients.** The action $q \mapsto q^{-1}$ extends to the
underlying field of fractions and acts on each coefficient:

- $D = q^4 + 4q^2 + 1$ is palindromic in $q^2$: under $q \to q^{-1}$,
  $D \to q^{-4} + 4q^{-2} + 1 = q^{-4}(1 + 4q^2 + q^4) = q^{-4} D$.
  Then $W_{\mathrm{sym}} = q^2/D \to q^{-2}/(q^{-4} D) = q^2/D$,
  invariant.  Same for $W_{\mathrm{alt}}$.  For $W_{\mathrm{std}}$:
  $(q^2+1)^2 \to (q^{-2}+1)^2 = q^{-4}(1+q^2)^2$, so
  $W_{\mathrm{std}} \to q^{-4}(1+q^2)^2 / (q^{-4} D) = W_{\mathrm{std}}$.
- $[3]_q = q^2 + 1 + q^{-2}$: invariant under $q \to q^{-1}$.
- $h_{\mathrm{A}} = q - q^{-1} \to q^{-1} - q = -h_{\mathrm{A}}$, so $h_{\mathrm{A}}$ has eigenvalue
  $-1$ and $h_{\mathrm{A}}^2$ has eigenvalue $+1$.
- $z$: at the canonical weight $z = q^3/(q^2+1)$ the action gives
  $z \mapsto 1/(q(q^2+1)) = z - h_{\mathrm{A}}$, the negative-crossing loop
  value $\mathrm{tr}_M(\sigma^{-1})$. So $z$ is not an $S$-eigenvector: $S$
  exchanges the two loop values. Equivalently, the Markov trace commutes with
  $S$, $\mathrm{tr}_M(S(X)) = S(\mathrm{tr}_M(X))$, and the relation
  $z(q^{-1}) = z(q) - h_{\mathrm{A}}$ is exactly the condition for this. (The
  excised convention-C weight $1/(q^{1/2}+q^{-1/2})$ is fixed by $S$, but its
  trace does not commute with $S$.)
- Catalan's constant $G$, Borromean volume $8G$, electron mass
  $m_e$, and binding scale $\alpha$ are real canonical constants
  unaffected by the algebraic action.

**Functional $\Phi_2$.** The transfer matrix is
$T(c, d) = \begin{pmatrix} ch_{\mathrm{A}} + d & c \\ c & d \end{pmatrix}$
with $\det T = d(ch_{\mathrm{A}} + d) - c^2$.  The Frobenius antipode
maps the primitive factor $(c, d)$ to $(\bar c, \bar d - \bar c h_{\mathrm{A}})$,
where the bar is $q \mapsto q^{-1}$ on the coefficients (this swaps
$\sigma \leftrightarrow \sigma^{-1}$ and inverts $q$; without barring the
coefficients, $ud = (1, -h_{\mathrm{A}}/2)$ would map to
$(1, -3h_{\mathrm{A}}/2)$ rather than to itself).  Direct computation:

See [Table 3](#tbl:frobenius-s-classification-table3-data).

For each primitive the determinant is $S$-invariant.  Since
$\det$ is multiplicative on chain products, $\Phi_2 = \sum_i
\log\lvert\det M_i\rvert$ is $S$-invariant.

**Functional $\Phi_3$.** For each primitive, direct computation
shows
$\chi^{\mathrm{sym}}(S(c, d)) = -\chi^{\mathrm{alt}}(c, d)$ and
$\chi^{\mathrm{alt}}(S(c, d)) = -\chi^{\mathrm{sym}}(c, d)$
(verify: for $(1, 0)$ with $\chi^{\mathrm{sym}} = q$,
$\chi^{\mathrm{alt}} = -1/q$, and $S(1, 0) = (1, -h_{\mathrm{A}})$ giving
$\chi^{\mathrm{sym}} = q + (-h_{\mathrm{A}}) = q^{-1}$ and
$\chi^{\mathrm{alt}} = -1/q + (-h_{\mathrm{A}}) = -q$, matching the swap with
sign).  For a chain product

$$
  \frac{\chi^{\mathrm{sym}}(S(\beta))}{\chi^{\mathrm{alt}}(S(\beta))}
  = \frac{(-1)^n \chi^{\mathrm{alt}}(\beta)}{(-1)^n \chi^{\mathrm{sym}}(\beta)}
  = \left(\frac{\chi^{\mathrm{sym}}(\beta)}{\chi^{\mathrm{alt}}(\beta)}\right)^{-1}
$$

so $\Phi_3(S(\beta)) = -\Phi_3(\beta)$, eigenvalue $-1$.

**Functional $\Phi_1$.** Because the canonical Markov trace commutes with
$S$, $S$ acts on $\Phi_1$ by inverting the evaluation point:
$\Phi_1(S(\beta); q_0) = \Phi_1(\beta; q_0^{-1})$. The raw $\Phi_1$ is
therefore not an $S$-eigenvector. It splits as
$\Phi_1 = \Phi_1^{+} + \Phi_1^{-}$ with
$\Phi_1^{\pm} = \tfrac12\bigl(\Phi_1(\beta) \pm \Phi_1(S(\beta))\bigr)$;
the eigenvalue $+1$ in Table 1 is that of the projection $\Phi_1^{+}$, which is
$S$-even by construction, and $\Phi_1^{-}$ is $S$-odd. $\square$

**Corollary.** Since $\Phi_2$ is $S$-even and $\Phi_3$ is $S$-odd,

$$
  \mathfrak{m}(S(\beta)) - \mathfrak{m}(\beta)
  = -2 \alpha \bigl(\Phi_1^{-}(\beta) + h_{\mathrm{A}}^2 \Phi_3(\beta)\bigr).
$$

The chirality term is the unique $S$-odd channel only when $\Phi_1^{-}$
vanishes. It does not vanish in general: on the proton chain $uud$ at the
proton pin, $\Phi_1^{-} \approx 0.0526$ against
$h_{\mathrm{A}}^2 \Phi_3 \approx 0.00912$, a ratio $\approx 5.77$
(`computations/probes/frobenius_s_parity_convention_d_probe.py`).

Since $S$ maps the proton braid (uud) to a braid with quark content (ddu),
the $S$-odd part of the mass is the structural carrier of the
proton-neutron splitting at the Wedderburn formula level, and it has two
sources, $\Phi_1^{-}$ and $h_{\mathrm{A}}^2\Phi_3$, not one.

**Witness**:
the formal derivation
verifies the eigenvalue assignments canonical at $q_0$ and
confirms that $\Phi_3 \approx 0$ for inter-nucleon-only chains in
free $A=1$ nucleons (consistent with the $S$-eigenspace
decomposition).
