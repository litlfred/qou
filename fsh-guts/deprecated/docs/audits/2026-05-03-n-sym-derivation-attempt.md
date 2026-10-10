> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# $\mathcal{N}_{\rm sym}$ derivation attempt — log

**Compiled** 2026-05-03 on `claude/4-parallel-followup-tests`.

After the user's correction "no fitting / no ansatz / N_sym → derivation",
this document logs an honest attempt at the categorical derivation of
$\mathcal{N}_{\rm sym}(q)$ + the obstacles encountered. It is **not** a
closure of the open problem; it is a research record.

## Derivation chain identified

Per `conj:categorical-higgs-idempotent` (PR #515 follow-up), the target
identity is:

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  \mathrm{tr}_F\!\bigl(e_{\rm sym}^{\rm EW} \cdot e_H\bigr)
$$

where:

- $e_{\rm sym}^{\rm EW} = \bigotimes_{k=2,3,4} e_{\rm sym}^{(T(2,2k))}$
  is the EW symmetric-channel projector across the three hosts
  (per `conj:weak-spectral-completeness`)
- $e_H$ is the categorical Higgs idempotent projecting onto the unbroken
  $\mathrm{U}(1)_{em}$ direction $T_3 + Y$
- $\mathrm{tr}_F$ is the Frobenius trace
  ($\langle X, Y \rangle_F = \mathrm{tr}_M(X \cdot Y)$).

Verification target: $\mathcal{N}_{\rm sym}(q_0) = 213.111807\ldots$.

## Per-host Frobenius-trace computation (partial)

For a single host with $T(2, 2k) = \widehat{\sigma_1^{2k}}$ in $B_2$,
the sym idempotent on $H_2(q)$ is

$$
  e_{\rm sym} \;=\; \frac{\sigma_1 + q^{-1}}{[2]_q}
$$

(projector onto eigenvalue $q$; the alt block has eigenvalue $-q^{-1}$;
$e_{\rm sym}^2 = e_{\rm sym}$, $e_{\rm sym} \cdot e_{\rm alt} = 0$).

Markov trace at $H_2$ with parameter $z = 1/(q^{1/2} + q^{-1/2})$:

$$
  \mathrm{tr}_M(1) = 1, \qquad \mathrm{tr}_M(\sigma_1) = z.
$$

Hence

$$
  \mathrm{tr}_M(e_{\rm sym})
  \;=\; \frac{z + q^{-1}}{[2]_q}.
$$

At $q_0 = 1.10998$: $z + q^{-1} \approx 0.4993 + 0.9009 \approx 1.4002$,
$[2]_q \approx 2.011$, so $\mathrm{tr}_M(e_{\rm sym}) \approx 0.6964$.

**Note**: this is k-independent — the sym idempotent on $H_2$ doesn't
depend on $k$ (the projector is on the $\sigma_1$-eigenvalue, not on
$\sigma_1^{2k}$). The k-dependence enters only through which host
the idempotent lives on.

For three independent hosts (assuming the three host Hecke algebras
are independent direct summands):

$$
  \mathrm{tr}_F(e_{\rm sym}^{\rm EW})
  \;=\; \prod_{k=2,3,4} \mathrm{tr}_M(e_{\rm sym}^{(k)})
  \;=\; \bigl((z + q^{-1})/[2]_q\bigr)^3
$$

At $q_0$: $0.6964^3 = 0.3378$. **Way off from 213.11.**

This shows: the bare product of per-host sym-idempotent traces is **not**
$\mathcal{N}_{\rm sym}(q)$. Either:

1. The three hosts are NOT independent — their tensor product carries
   additional cross-host structure (e.g., the $G$-equivariance under
   $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ couples them).
2. $e_H$ is NOT the identity — it adds a non-trivial multiplicative
   factor in the trace.
3. The Frobenius trace on the EW sector uses a **different**
   normalization than the per-host Markov trace
   (e.g., includes a Plancherel weight $1/\dim_q$ factor or similar).

## Obstacle: no concrete construction

Going further requires:

- **Explicit cross-host structure** — how does $\mathrm{SU}(2)_L \times
  \mathrm{U}(1)_Y$ act on the joint $H_2(q)^{\otimes 3}$ algebra?
  This is not specified in the QOU framework as currently authored.
- **Concrete $\langle\Phi\rangle$** — the Higgs vacuum value as a
  specific morphism $\mathbf{1} \to A$. Per `def:mass-identity`,
  vortex morphisms exist; identifying $\langle\Phi\rangle$ with a
  specific one requires authoring the $G$-action on $A$ first.
- **Frobenius normalization across hosts** — does
  $\mathrm{tr}_F^{\rm EW}$ inherit from $\mathrm{tr}_M^{(k)}$
  multiplicatively or via a Plancherel weight?

These are **research-grade content-authoring tasks**. Not derivable
in a single computational session.

## Two competing path-α-coherent structural anchors (both UNPROVEN)

Two structural forms admit categorical justification — each factor has
a categorical reason — but neither is a derivation:

### Anchor I: $\mathcal{N}_{\rm sym} \approx [3]_q \cdot [4]_q^3$ (0.87% off)

- $[3]_q$ = q-dim of $\mathrm{SU}(2)_L$ **adjoint** (3 broken
  generators)
- $[4]_q^3$ = three Goldstones at the W-host scale (assumes uniform
  $g$-coupling for all 3 broken directions, **contradicting** the
  $W^3$-$B$ mixing that gives Z a different coupling)

### Anchor II: $\mathcal{N}_{\rm sym} \approx [2]_q \cdot [4]_q^2 \cdot [6]_q$ (1.81% off)

- $[2]_q$ = q-dim of $\mathrm{SU}(2)_L$ **fundamental** (Higgs doublet)
- $[4]_q^2$ = two $W^\pm$ Goldstones at the W-host scale (genus 1,
  $T(2,4)$); identical because $W^\pm$ are mass-degenerate by isospin
- $[6]_q$ = the $Z$ Goldstone at the Z-host scale (genus 2, $T(2,6)$);
  different from W± because Z has the mixed $T_3$-$Y$ coupling

Anchor II is **physically more coherent** — it accounts for
$W^3$-$B$ mixing — but lands at 1.81% off vs Anchor I's 0.87%.

### Cannot select between them without derivation

Both anchors are **path-α structural ansatze**, not derivations. The
user's "no ansatz" rule means we cannot promote either to a closed
form by numerical preference alone; the categorical
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ computation is the
arbiter.

The 0.87% gap on Anchor I and the 1.81% gap on Anchor II are
**different categorical phenomena**:
- Anchor I's gap could be the residual Higgs scalar
- Anchor II's gap could be a Plancherel reweighting / vacuum-volume
  factor

Without the explicit $G$-action on the substrate (above), we cannot
distinguish.

## Cannot fit further without categorical input

The next-order correction (the $\sim 0.1\%$ residual after $[3]_q [4]_q^3
(1 + \hbar_q^2)$) cannot be pinned down without categorical derivation.
Searching for $\hbar_q^4 \cdot [k]_q$ candidate forms is multiple-
comparison fitting and is explicitly avoided per the user's instruction.

## Recommended path forward (not yet attempted)

1. **Author $G$-action on substrate** — extends `def:frobenius-hopf-substrate`
   to include explicit $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ structure
   on $A$. Roughly 2-3 days of content authoring.
2. **Identify $\langle\Phi\rangle$ as vortex morphism** — concrete
   $\mathbf{1} \to A$ morphism; uses `def:mass-identity` infrastructure.
   Roughly 1 day.
3. **Compute** $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ in
   closed form via the resulting structure; verify against $213.11$.
   1-2 days once (1) and (2) are in place.

Total: ~4-6 days of content-authoring work to convert
`conj:categorical-higgs-idempotent` from sketch to derivation.

## Status

🟡 **Open**. Derivation chain identified; per-host computation done
($\mathrm{tr}_M(e_{\rm sym}) = 0.6964$ at $q_0$); product-of-hosts
$0.3378$ does not match $213.11$, so cross-host structure is needed.
Research-grade work required to author the $G$-action on the substrate
and the explicit Higgs-vacuum morphism.

The structural interpretation $[3]_q \cdot [4]_q^3$ provides an
*anchor* for the future derivation — when the categorical pipeline is
complete, the leading-order term should match this form (with the
remaining 0.87% explainable as the Higgs-scalar contribution).
