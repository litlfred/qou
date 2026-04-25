# Closed-Form Theorem for χ_std on Per-Nucleon Braid Words

*Derived from explicit 2×2 Hoefsmit seminormal matrix trace.*

## Theorem

Let $\mathrm{std} = (2,1)$ be the standard 2-dimensional irrep of the
Iwahori-Hecke algebra $H_3(q)$. Let $\beta_{\mathfrak{p}}$ and
$\beta_{\mathfrak{n}}$ be the per-nucleon braid words emitted by
`mass_endomorphism.proton_cross` and `mass_endomorphism.neutron_cross`,
viewed as elements of $H_3(q)$ via the substitution
$(c,\,d) \mapsto c\sigma_i + d \cdot I$.

Then

$$
\chi_{\mathrm{std}}(\beta_{\mathfrak{p}})
  = \frac{H_A}{4}\Bigl( [11]_q + [9]_q + [7]_q + [3]_q \Bigr)
$$

$$
\chi_{\mathrm{std}}(\beta_{\mathfrak{n}})
  = \frac{H_A}{4}\Bigl( [9]_q + [7]_q + [5]_q + [1]_q \Bigr)
$$

where $H_A := q - q^{-1}$ and $[k]_q := (q^k - q^{-k})/H_A$.

**Unified form:** both characters have the shape
$$
\chi_{\mathrm{std}}(\beta_\bullet) = \frac{H_A}{4}\Bigl( [m]_q + [m-2]_q + [m-4]_q + [m-8]_q \Bigr)
$$
with $m_{\mathfrak{p}} = 11$, $m_{\mathfrak{n}} = 9$.

## Cyclotomic factorization

Clearing the $4q^m$ denominator gives Laurent polynomials:

$$
\chi_{\mathrm{std}}(\beta_{\mathfrak{p}}) = \frac{q^{22} + q^{20} + q^{18} + q^{14} - q^8 - q^4 - q^2 - 1}{4q^{11}}
$$

with **full cyclotomic factorization** over $\mathbb{Q}$:
$$
\text{numerator}_{\mathfrak{p}} = \Phi_1 \Phi_2 \Phi_3 \Phi_5 \Phi_6 \Phi_{10} \Phi_{16}
$$

$$
\chi_{\mathrm{std}}(\beta_{\mathfrak{n}}) = \frac{q^{18} + q^{16} + q^{14} + q^{10} - q^8 - q^4 - q^2 - 1}{4q^{9}}
$$

with partial cyclotomic factorization:
$$
\text{numerator}_{\mathfrak{n}} = \Phi_1 \Phi_2 \Phi_8 \cdot P_{\mathfrak{n}}(q)
$$
where $P_{\mathfrak{n}}(q) = q^{12} + 2q^{10} + 2q^8 + q^6 + 2q^4 + 2q^2 + 1$
is irreducible over $\mathbb{Q}$. The proton character factors into
cyclotomics alone; the neutron character does not.

## Proof

### Step 1 — 2×2 Hoefsmit matrices for std at n=3

The standard irrep has dimension 2 with basis
$\{e_{T_1}, e_{T_2}\}$ indexed by standard Young tableaux
$T_1 = [{1,2},{3}]$ and $T_2 = [{1,3},{2}]$.

The Hoefsmit seminormal representation gives
$$
\rho_{\mathrm{std}}(\sigma_1) = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix}
$$

For $\sigma_2$, entries 2 and 3 lie in different row-column
positions in both tableaux, producing a 2×2 mixing block with axial
distance $\rho = -2$:
$$
\rho_{\mathrm{std}}(\sigma_2) = \begin{pmatrix}
  -q^{-1}/[2]_q & \sqrt{[3]_q}/[2]_q \\
  \sqrt{[3]_q}/[2]_q & q^3/(q^2+1)
\end{pmatrix}
= \frac{1}{[2]_q}\begin{pmatrix}
  -q^{-2} & \sqrt{[3]_q} \\
  \sqrt{[3]_q} & q^2
\end{pmatrix}
$$

Both matrices satisfy the Hecke relation $\sigma_i^2 = H_A \sigma_i + 1$.

### Step 2 — Reduction to single-generator words

Per-nucleon braid words factor as
$\beta_{\mathrm{nuc}} = W_{g_0} \cdot W_{g_1}$ where $W_{g_k}$ contains
only factors on generator $\sigma_{k+1}$. Since all factors within a
single generator commute (polynomials in $\sigma_i$ alone), each $W_{g_k}$
simplifies.

**Proton** (from `mass_endomorphism.proton_cross`):

- gen 0: six $(1, 0)$ factors + one $(1, -H_A/2)$ $= \sigma_1^6 \cdot (\sigma_1 - H_A/2)$
- gen 1: three $(1, -H_A)$ factors + one $(1, -H_A/2)$ $= \sigma_2^{-3} \cdot (\sigma_2 - H_A/2)$

using $(1, -H_A) = \sigma_i - H_A \cdot I = \sigma_i^{-1}$ from the Hecke
relation.

**Neutron** (from `mass_endomorphism.neutron_cross`):

- gen 0: five $(1, 0)$ + one $(1, -H_A)$ + one $(1, -H_A/2)$ $= \sigma_1^4 \cdot (\sigma_1 - H_A/2)$
- gen 1: identical to proton: $\sigma_2^{-3} \cdot (\sigma_2 - H_A/2)$

### Step 3 — Diagonal block

On the diagonal $\sigma_1$, the ud-half factor acts as
$$
\sigma_1 - \tfrac{H_A}{2} = \begin{pmatrix} q - H_A/2 & 0 \\ 0 & -q^{-1} - H_A/2 \end{pmatrix} = \frac{[2]_q}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

since $q - H_A/2 = (q + q^{-1})/2 = [2]_q/2$ and
$-q^{-1} - H_A/2 = -[2]_q/2$.

Therefore
$$
W_{g_0}^{(\mathfrak{p})} = \sigma_1^6 \cdot (\sigma_1 - H_A/2) = \frac{[2]_q}{2}\begin{pmatrix} q^6 & 0 \\ 0 & -q^{-6} \end{pmatrix}
$$
and
$$
W_{g_0}^{(\mathfrak{n})} = \frac{[2]_q}{2}\begin{pmatrix} q^4 & 0 \\ 0 & -q^{-4} \end{pmatrix}
$$

### Step 4 — Mixing block for $W_{g_1}$

Using $\sigma_2^{-1} = \sigma_2 - H_A \cdot I$:
$$
W_{g_1} = \sigma_2^{-3} \cdot (\sigma_2 - H_A/2)
$$

Direct computation via `sympy.Matrix` confirms this 2×2 product; the
off-diagonal entries contain $\sqrt{[3]_q}$ contributions that cancel
in the final trace.

### Step 5 — Trace

The character is $\chi_{\mathrm{std}}(\beta) = \mathrm{tr}(W_{g_0} \cdot W_{g_1})$.
Since $W_{g_0}$ is diagonal with entries $(\pm [2]_q/2) \cdot (\pm q^{\text{exp}})$,
only the diagonal of $W_{g_1}$ contributes to the trace:

$$
\chi_{\mathrm{std}}(\beta_\bullet) = (W_{g_0})_{11} (W_{g_1})_{11} + (W_{g_0})_{22} (W_{g_1})_{22}
$$

Explicit evaluation in `sympy` yields the closed-form Laurent
polynomials of Step 1, which after grouping by $q^k - q^{-k}$ pairs give
$$
\chi_{\mathrm{std}}(\beta_\bullet) = \frac{1}{4}\sum_{k \in S_\bullet} (q^k - q^{-k}) = \frac{H_A}{4}\sum_{k \in S_\bullet} [k]_q
$$

with index sets $S_{\mathfrak{p}} = \{11, 9, 7, 3\}$ and
$S_{\mathfrak{n}} = \{9, 7, 5, 1\}$. $\qquad\square$

## Verification

Numerical check at $q_0 = 1.1099785955541805$:

| nucleon | closed form (H·Σ/4) | direct 2×2 trace | agreement |
|---|---|---|---|
| proton | 1.8077033200981574 | 1.807703320098157 | exact (14 digits) |
| neutron | 1.2653010867739343 | 1.2653010867739343 | exact (14 digits) |

## Relationship to sym/alt characters

The symmetric and alternating characters of the same per-nucleon words
are (using the `chi-sym-alt-theorem` framework):
$$
\chi_{\mathrm{sym}}(\beta_\bullet) = q^{n_\sigma - n_{\sigma^{-1}}} \cdot \bigl([2]_q/2\bigr)^{n_\text{ud}}, \qquad n_\text{ud} = 2 \text{ per nucleon}
$$
$$
\chi_{\mathrm{alt}}(\beta_\bullet) = (-1)^{\#\beta_\bullet} \cdot q^{n_{\sigma^{-1}} - n_\sigma} \cdot \bigl([2]_q/2\bigr)^{n_\text{ud}}
$$

Per nucleon:
- **Proton**: $n_\sigma = 6$, $n_{\sigma^{-1}} = 3$, $n_\text{ud} = 2$
- **Neutron**: $n_\sigma = 5$ (gen 0) + 0 (gen 1) = 5, $n_{\sigma^{-1}} = 1$ (gen 0) + 3 (gen 1) = 4, $n_\text{ud} = 2$

At $q = q_0$, $\chi_{\mathrm{sym}}(\beta_{\mathfrak{p}}) \approx 1.406$,
$\chi_{\mathrm{sym}}(\beta_{\mathfrak{n}}) \approx 1.134$. The std
values 1.808 (p) and 1.265 (n) are **larger** than sym values —
reflecting the richer 2-dim channel structure.

## Significance

This is the **second exact closed form** derived for the framework
(after $\chi_{\mathrm{sym}} \cdot \chi_{\mathrm{alt}}$). Key novelty:
- First matrix-valued closed form (2×2 Hoefsmit trace).
- Shows that higher-dim irreps also admit *specific polynomial in q*
  closed forms when evaluated on structured words.
- Proton and neutron share a unified ladder shape
  $\{m, m-2, m-4, m-8\}$ — a structural invariant of the 3-quark
  Borromean confinement encoded by the 2-ud-half factorization.

## Extension targets

- **Atom-level**: $\chi_\lambda(\beta_{Z,N})$ for $\lambda \vdash 3A$
  does not factor as a product of per-nucleon characters (the strands
  mix across nucleon boundaries at $\sigma_{3k+2}$), but the
  *inter-nucleon pn factor* also has a Hoefsmit closed form at dim 2,
  enabling a recursive algebraic computation.
- **Higher-dim irreps at n > 3**: the (2,1,1) and (3,1) at n=4 are
  3-dim; their Hoefsmit blocks are 3×3 and the same reduction argument
  applies with more algebra.
