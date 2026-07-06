## Statement

**Proposition (operator-valued trace decomposition).**
*Let $\lambda \vdash n$ with $n = n_1 + n_2$, $\beta_1 \in H_{n_1}(q)$,
$\beta_2 \in H_{n_2}(q)$, and $I \in H_n(q)$ supported on the boundary
strands $\{n_1, n_1+1\}$. Under the [Wenzl 1988] LR decomposition
$V_\lambda \big|_{H_{n_1}(q) \otimes H_{n_2}(q)} = \bigoplus_{(\mu, \nu)} c^\lambda_{\mu, \nu} \, V_\mu \otimes V_\nu$,*

$$
  \boxed{
    \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
    \;=\;
    \sum_{(\mu, \nu)} \,
    \operatorname{Tr}_{V_\mu \otimes V_\nu}\!\Bigl(
       A^\lambda_{\mu, \nu}(I) \cdot
       \bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr)
    \Bigr),
  }
$$

*where $A^\lambda_{\mu, \nu}(I) := \sum_{k=1}^{c^\lambda_{\mu, \nu}} A^\lambda_{\mu, \nu, k}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)$
is the diagonal-summed $(\mu, \nu)$-block of $\rho_\lambda(I)$ in the LR basis,
summing over multiplicity copies. **In general $A^\lambda_{\mu, \nu}(I)$ is
not a scalar multiple of the identity** — it is genuinely operator-valued.*

This is the **refined Sub-lemma 2.1** of
[`conj:confinement-nf-structure-forcing`](#conj:confinement-nf-structure-forcing);
the original scalar formulation $A^\lambda_{\mu, \nu}(I) = \alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu) \cdot \mathbf{1}$
is empirically falsified for $9$ of $11$ partitions $\lambda \vdash 6$
in the deuteron interface case.

## Numerical verification

`sublemma-2-1-A-operator-extract.witness.json` extracts $A^\lambda_{\mu, \nu}(I)$
matrix entries via bilinear-system inversion across $144$ $(\beta_1, \beta_2)$
test pairs in $H_3(q_0) \times H_3(q_0)$ for the deuteron interface
$I = \sigma_2 - \tfrac{1}{2}(q - q^{-1}) \cdot \mathbf{1}$:

| $\lambda \vdash 6$ | unknowns | rel residual |
|---|---:|---:|
| $(6)$ | $1$ | $7 \times 10^{-16}$ |
| $(5, 1)$ | $9$ | $2 \times 10^{-15}$ |
| $(4, 2)$ | $25$ | $6 \times 10^{-15}$ |
| $(4, 1, 1)$ | $26$ | $6 \times 10^{-15}$ |
| $(3, 3)$ | $17$ | $6 \times 10^{-15}$ |
| $(3, 2, 1)$ | $32$ | $7 \times 10^{-15}$ (incl. $c = 2$) |
| $(3, 1, 1, 1)$ | $26$ | $5 \times 10^{-15}$ |
| $(2, 2, 2)$ | $17$ | $5 \times 10^{-15}$ |
| $(2, 2, 1, 1)$ | $25$ | $5 \times 10^{-15}$ |
| $(2, 1, 1, 1, 1)$ | $9$ | $2 \times 10^{-15}$ |
| $(1^6)$ | $1$ | $5 \times 10^{-16}$ |

**All $11$ of $11$ partitions verify to ~$10^{-15}$ relative precision** (machine floating-point limit).
Of the $30$ $(\mu, \nu)$ blocks across these, $12$ are scalar (multiples of the identity)
and $18$ are non-scalar operators.

## Proof

The proof is the standard Wenzl 1988 Hecke branching theorem combined
with Hoefsmit 1974 seminormal matrix-element formulas. Six steps
(detailed in [`docs/audits/2026-05-04-sublemma-2-1-categorical-proof.md`](../../docs/audits/2026-05-04-sublemma-2-1-categorical-proof.md)):

**Step 1 ([Wenzl 1988] LR decomposition).** $V_\lambda \downarrow \bigoplus c^\lambda_{\mu\nu} V_\mu \otimes V_\nu$ at the level of seminormal Hecke modules.

**Step 2 (Block-diagonal action of $\beta_1, \beta_2$).** Standard parabolic restriction: $\beta_1 \in H_{n_1}(q) \subset H_n(q)$ acts as $\rho_\mu(\beta_1) \otimes \mathbf{1}_\nu$ on each $(\mu, \nu)$-block; similarly for $\beta_2$.

**Step 3 ([Hoefsmit 1974] interface action).** $\rho_\lambda(\sigma_{n_1})$ has explicit matrix elements in the seminormal basis:
- diagonal: $\rho_\lambda(\sigma_{n_1})_{T,T} = h_q(d_T)$ where $d_T = c_T(n_1+1) - c_T(n_1)$ is the axial distance between cells containing entries $n_1, n_1+1$ in $T$
- off-diagonal: $\rho_\lambda(\sigma_{n_1})_{T,T'} = \sqrt{1 - h_q(d_T)^2}$ when $T' = s_{n_1}(T)$ is a valid SYT

**Step 4 (Trace formula).** Direct calculation modulo Steps 1–3, using the cyclic property of trace and the tensor-product structure of $\rho_\lambda(\beta_1)$, $\rho_\lambda(\beta_2)$ on each $(\mu, \nu)$-block.

**Step 5 (Scalar special case for $\dim V_\lambda = 1$).** When $\lambda \in \{(n), (1^n)\}$, $A^\lambda_{\mu, \nu}(I)$ reduces to a scalar — the unique eigenvalue of $\sigma_{n_1}$ in the trivial 1-dim rep. Empirically verified to machine precision: $A^{(6)}(I) = (q + q^{-1})/2 \approx +1.005$, $A^{(1^6)}(I) = -(q + q^{-1})/2 \approx -1.005$ at $q_0$ for $I = \sigma_2 - h/2$.

**Step 6 (Torus-knot specialisation).** For $I = T_{p,k}$ acting on column-rep $V_{(1^n)}$, recovers the proved scalar formula $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ from [`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot).

The non-scalar nature of $A^\lambda_{\mu, \nu}(I)$ for higher-dim $V_\mu \otimes V_\nu$ follows from Step 3: the axial distance $d_T$ varies across SYTs $T$ within the same $(\mu, \nu)$-block (different LR interleavings place the boundary cells at different axial distances), so $\rho_\lambda(\sigma_{n_1})$ acts with **distinct diagonal entries** on different SYTs in the block.

## Recursive corner formula (partial)

The $(T_\mu \otimes T_\nu, \pi)$-diagonal entry of $A^\lambda_{\mu, \nu}(\sigma_{n_1})$ admits a corner-content prediction

$$
  A^\lambda_{\mu, \nu}(\sigma_{n_1})_{(T_\mu, T_\nu, \pi)}
  \;\stackrel{?}{=}\;
  h_q\bigl(c(q^\pi_\nu) - c(\omega(T_\mu))\bigr)
$$

where $\omega(T_\mu) \in \mathrm{corners}(\mu)$ is the cell containing entry $n_1$ in $T_\mu$,
and $q^\pi_\nu$ is the LR-Yamanouchi-extending corner for multiplicity copy $\pi$.
This formula is **exact for the scalar (1-dim) cases** and gives the right
qualitative structure for higher-dim cases (`sublemma-2-1-A-recursive-formula.witness.json`).
For higher-dim cases the formula needs refinement to account for the full
LR-rectification combinatorics of the skew shape $\lambda / \mu_T$ — open
work toward an explicit closed form.

## Significance for the categorical mass program

The refined statement modifies the bottleneck for closing the
nucleon-mass anchors $m_\mathfrak{p}/m_e$ and $m_\mathfrak{n}/m_e$
([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)):
the atomic-shift coefficients $(18, 3, 1)$
([w3 audit](../../docs/audits/2026-05-03-w3-habiro-unblocked.md))
are **not isolated scalars** but **maximum pole orders over the
matrix entries of $A^\lambda_{\mu, \nu}(\sigma_{n_1})$ in the
maximizing LR block** — closing $(18, 3, 1)$ categorically reduces to
explicit Hoefsmit-block computations for the relevant $(\lambda, \mu, \nu)$.
The closing computation is now executed for the proton and deuteron
in
[`per_irrep_pole_atom.py`](../../computations/per_irrep_pole_atom.py)
(witnesses
[`per-irrep-pole-proton-h3.witness.json`](../../computations/per-irrep-pole-proton-h3.witness.json)
+
[`per-irrep-pole-deuteron-h6.witness.json`](../../computations/per-irrep-pole-deuteron-h6.witness.json)),
yielding $\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_p) = 19$ and
$\mathrm{shift}_{\mathrm{NF}}(\beta_D) = 40$ — exact matches to
$18 \cdot Z + 21 \cdot N + 1$ from
[`prop:per-nucleon-shift-additive-linearity`](#prop:per-nucleon-shift-additive-linearity).
A $\ge$ 3 atoms (T, ${}^{3}$He, ${}^{4}$He) follow the same pipeline; chi cache
emission is the only new compute per atom.

## Witnesses

- `sublemma-2-1-A-operator-extract.witness.json` — extracted $A^\lambda_{\mu, \nu}(I)$ matrices for $H_6$, all 11 partitions verified.
- `sublemma-2-1-deuteron-branching.witness.json` — Wenzl 1988 branching identity, no-interface case.
- `sublemma-2-1-A-recursive-formula.witness.json` — corner-content prediction (partial).

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92** (1988), 349–383. Theorem 3.4 (Hecke branching).
- [Hoefsmit 1974] *Representations of Hecke algebras of finite groups with $BN$-pairs of classical type*, PhD thesis, UBC. Seminormal matrix elements.
