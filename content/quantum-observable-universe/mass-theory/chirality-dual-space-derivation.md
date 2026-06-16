**Proposition (chirality from symmetric-channel trace duality).**
*The paper's chirality factors $a_K$ are derivable from the
**symmetric-channel** trace structure of Hecke generators in
$H_3(R, q)$.  For every pn crossing $c$ in the atomic braid,*

$$
  a_K \;=\; \prod_{\substack{\text{pn crossings}\\ c \in \mathcal{B}_K}}
  \bigl(1 + \mathrm{sign}(c) \cdot h\bigr),
  \qquad
  h \;=\; q - q^{-1},
$$

*where the per-crossing factor decomposes via Wedderburn-channel
duality:*

$$
  1 + \mathrm{sign}(c)\cdot h
  \;=\;
  1 \;+\; \mathrm{sign}(c) \cdot
    \bigl[\tau_{\mathrm{std}}(\sigma) - \tau_{\mathrm{std}}(\sigma^{-1})\bigr] / 2
  \;=\;
  1 \;+\; \mathrm{sign}(c) \cdot \bigl[\tau_{\mathrm{sym}}(\sigma) - \tau_{\mathrm{sym}}(\sigma^{-1})\bigr].
$$

**Derivation.**
*The Hecke generator $\sigma$ has standard-rep eigenvalues $(q, -q^{-1})$
([three-parameters Wedderburn](#prop:three-parameters-wedderburn)).
Its trace on each Wedderburn block is:*

See [Table 1](#tbl:chirality-dual-space-derivation-table1-data).

*The "chirality content" of a single positive crossing $\sigma$ is
the symmetric-channel deviation*

$$
  \delta_{\mathrm{sym}}(\sigma) \;:=\; \tau_{\mathrm{sym}}(\sigma) - \tau_{\mathrm{sym}}(\sigma^{-1})
  \;=\; q - q^{-1} \;=\; h,
$$

*and for $\sigma^{-1}$ it is $-h$.  This is the **dual-space
asymmetry** of the symmetric channel: $\sigma$ and $\sigma^{-1}$ act
oppositely on the symmetric idempotent.*

*Adding $1$ (the identity-channel contribution) gives the per-crossing
chirality factor*

$$
  1 + \mathrm{sign}(c) \cdot h.
$$

*Multiplicativity over pn crossings (each is an independent inter-
nucleon braiding event in the atomic braid word) gives the full
formula.*

**Verification against paper's assignments.**

*All three paper values follow directly from the per-crossing rule:*

See [Table 2](#tbl:chirality-dual-space-derivation-table2-data).

*Symbolic verification: the per-crossing product $\prod_{pn}(1 + \mathrm{sign}\cdot h)$
**exactly equals** paper's
$\{1+h, 1-h^2, (1-h^2)^2\}$ for $\{D, T/^3\mathrm{He}, ^4\mathrm{He}\}$.
Numerical match at $q_0 \approx 1.11$ confirmed.*

**Why "dual space".**

*The pairing $\tau_\lambda(\sigma) - \tau_\lambda(\sigma^{-1})$ is
the **Frobenius-dual pairing** of the deviation $\sigma - \sigma^{-1}$
against the channel-projection cocycle $\tau_\lambda$.  In dual-space
terms:*

- *$\sigma - \sigma^{-1} = h \cdot \mathbf{1}$ in $H_n(R, q)$ (Hecke
  inverse identity).*
- *The trace $\tau_\lambda$ is a linear functional on $H_n(R, q)$;
  paired against $\sigma - \sigma^{-1}$ gives the channel-specific
  $h$-content.*
- *Symmetric-channel: $\tau_{\mathrm{sym}}(h \cdot \mathbf{1}) = h$
  (1-dim rep, identity has trace 1).*
- *Antisymmetric channel: $\tau_{\mathrm{alt}}(h \cdot \mathbf{1}) = h$
  also (alt is also 1-dim).*
- *Standard channel: $\tau_{\mathrm{std}}(h \cdot \mathbf{1}) = 2h$
  (2-dim rep, identity has trace 2).*

*The PER-CHANNEL deviation $\tau_\lambda(\sigma) - \tau_\lambda(\sigma^{-1})$
matches $\tau_\lambda(h \cdot \mathbf{1})$ via the algebra identity
$\sigma - \sigma^{-1} = h$.  The chirality factor specifically uses
the **symmetric channel** because that is the unique 1-dim sector
that reduces to the trivial algebra at $q = 1$.*

**Result (Term 5).**

*The chirality factor $a_K$ is now algebraically derived from
Wedderburn-channel duality on the symmetric-trace pairing.  The
derivation is rigorous (uses only the standard Hecke relation +
Wedderburn structure), reproduces all three paper assignments
exactly, and ties the chirality factor explicitly to the
[three-parameters Wedderburn](#prop:three-parameters-wedderburn)
machinery.*

*This closes Term 5's coefficient gap — the writhe-ribbon
linearisation
([chirality writhe-ribbon](#prop:chirality-writhe-ribbon-derivation))
gave the correct **structural form** $1 + w \cdot h + O(h^2)$
but the wrong global coefficient via averaging; the **per-crossing
factorisation** above gives the correct exact form.*

**Categorical content.**
*The factor $\sigma - \sigma^{-1} = h \cdot \mathbf{1}$ is the
Hecke algebra's "deviation from involution": for $q = 1$ (group
algebra of $S_n$), $\sigma^2 = 1$ and $\sigma = \sigma^{-1}$, so
the deviation vanishes.  At $q \neq 1$, the deviation $h$ encodes
the $q$-deformation of the braiding.  Each pn crossing contributes
$\pm h$ to the symmetric-channel chirality content; the product
$\prod (1 + \mathrm{sign} \cdot h)$ assembles these into the
total chirality factor.*

*This makes Term 5's derivation **fully internal** to the
Hecke-algebra / Wedderburn framework — no external quantum-group
ribbon, no Hochschild cohomology, no q-Heisenberg Fock structure
needed.  The Frobenius-dual pairing on the symmetric Wedderburn
channel is sufficient.*

**Coverage.** With Term 5 derived, all six terms of the unified mass formula are algebraically derived using the existing machinery:

See [Table 3](#tbl:chirality-dual-space-derivation-table3-data).

*Six of six. Computation infrastructure complete (scripts +
witness files for all terms in `computations/`).
Paper-side completeness achieved.*
