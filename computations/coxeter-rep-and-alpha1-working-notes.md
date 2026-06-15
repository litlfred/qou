# Working notes: depth-$k$ representatives at $H_n$ and $\alpha_1$ nonzero

These are *agent working notes*, not paper content.  They sketch
attempts and identify the structural questions that need cohomological
input.

## (A) Coxeter-element representatives at $H_n$ — what's needed

**$H_3$ canonical representatives** (from
[H_3 explicit](#prop:spectral-sequence-h3-explicit)):

| depth $k$ | representative $r_k$ | length | symmetry |
|:--:|--|:--:|--|
| $0$ | $1$ | $0$ | trivial |
| $1$ | $\sigma_1 - \sigma_2$ | $1$ | alternating-pair |
| $2$ | $\sigma_1 \sigma_2 + \sigma_2 \sigma_1$ | $2$ | cyclic-symmetric |
| $3$ | $\sigma_1 \sigma_2 \sigma_1$ | $3$ | longest-element |

**Pattern observed**: each $r_k$ is a length-$k$ word that is
**unique up to the Markov-trace equivalence** in the surviving
$E_\infty^{0, 0}$ class of the $H_3$ spectral sequence.  The H_3
proof relies on the small partition count $p(3) = 3$ to identify
$r_k$ canonically with the Wedderburn idempotent $e_\lambda$ of
height $k+1$.

### Proposed pattern for $H_n$, $n \geq 4$

Conjecture: at $H_n$, the depth-$k$ canonical representative is

$$
  r_k(H_n) \;=\; \mathrm{Sym}^{(k)}_{\mathrm{cyclic}}\!
    \bigl(\sigma_1 \sigma_2 \cdots \sigma_k\bigr),
$$

i.e.\ the cyclic-symmetric average of the length-$k$ Coxeter prefix.
Concretely:

- $r_0 = 1$ (always)
- $r_1 = \sigma_1 - \sigma_{n-1}$ (longest-distance alternating pair —
  matches $H_3$ where $\sigma_2 = \sigma_{n-1}$ for $n = 3$)
- $r_2 = \sigma_1 \sigma_2 + \sigma_{n-2} \sigma_{n-1}$
- $r_k = \sum_{\text{cyclic shifts}} \pm \sigma_{i_1} \cdots \sigma_{i_k}$

**What's needed for cohomological justification**: at each $n$, prove
that $r_k$ above is the **unique** $E_\infty^{0, 0}$-page representative
of the depth-$k$ class up to $d_2$-image equivalence
([spectral sequence collapse](#prop:spectral-sequence-collapse) /
[H_3 explicit](#prop:spectral-sequence-h3-explicit) generalisation).

**Why this is non-trivial**: at $H_n$ for $n \geq 4$ the spectral
sequence has multiple length-$k$ words at each depth, and the
cyclic-symmetric subspace may be larger than 1-dimensional.  The
"right" $r_k$ is the one whose Markov pairing $\langle \mathrm{tr}_M,
r_k \rangle$ extracts only the depth-$k$ stratum (orthogonal to lower
depths in the Wedderburn decomposition).

**Test computation needed**: at $H_6$, enumerate length-$k$ reduced
words for $k = 0, 1, 2, 3, 4, 5$ and compute $\mathrm{tr}_M(r_k)$ via
the witness $y_\lambda$ values.  Words whose pairing equals
$\sum_{\lambda \in \Lambda_k} y_\lambda \chi_\lambda(r_k)$ with all
non-depth-$k$ terms vanishing are the canonical $r_k$.

This is a finite enumeration — feasible in one agent session if
Hoefsmit characters are evaluated on each candidate word.

## (B) $\alpha_1$ nonzero — is the Gerstenhaber bracket actually needed?

**The user's question is sharp**: with this much structure, why
isn't $\alpha_1$ just a different choice of representative?

### Argument that $\alpha_1 = 0$ is forced

**At $H_3$, direct Markov pairing on any length-1 word:**

$$
  \mathrm{tr}_M(\sigma_i) \;=\; z \quad \text{for every } i = 1, 2,
$$

by the Markov property itself.  Any $R$-linear combination of length-1
words pairs to $(c_1 + c_2) \cdot z$.  Setting this to zero forces
$c_1 + c_2 = 0$ (so $r_1 \propto \sigma_1 - \sigma_2$, giving
$\mathrm{tr}_M = 0$), or makes the pairing equal $z \cdot
\sum_i c_i$ — a *non-vanishing* but *trivially-redundant* number
already accounted for by $\alpha_0 = 1$.

So either $\alpha_1 = 0$ (the alternating choice, which is the
"new structural information" — distinct from $\alpha_0$), or
$\alpha_1$ is degenerate with $\alpha_0$.  The H_3 proof picks the
alternating choice as **the only choice that adds new information**.

### Why Gerstenhaber bracket would help

To get $\alpha_1$ nonzero **and not redundant with $\alpha_0$**, the
pairing must be sensitive to *order* of the generators
$\sigma_1, \sigma_2$ — but cyclicity of $\mathrm{tr}_M$ says

$$
  \mathrm{tr}_M(\sigma_1) = \mathrm{tr}_M(\sigma_2),
$$

so any *linear* pairing is symmetric.  A *bilinear* pairing — the
Gerstenhaber bracket $[\sigma_1, \sigma_2] := \sigma_1 \sigma_2 -
\sigma_2 \sigma_1$ — would distinguish them, except that
$\mathrm{tr}_M[\sigma_1, \sigma_2] = 0$ also by cyclicity.

**The non-trivial observation**: the Gerstenhaber bracket on
$HH^*(H_n(R, q))$ is a *cohomological* operation, not a trace
pairing.  At generic $q$, $HH^k = 0$ for $k \geq 1$
([spectral sequence collapse](#prop:spectral-sequence-collapse)),
so the bracket has no domain — it lives only on $HH^0$ and
$[HH^0, HH^0] \subset HH^{-1} = 0$.

**Conclusion**: at generic $q$, $\alpha_1 = 0$ is **structurally
forced**.  There is no Gerstenhaber bracket calculation to do; the
target is empty.

### Where might nonzero $\alpha_1$ come from?

Three avenues, in increasing structural depth:

1. **Non-generic $q$**: at special $q$ (roots of unity), $HH^k(H_n(q))
   \neq 0$ — a Gerstenhaber bracket calculation would be non-trivial.
   But the substrate $q_0 = 1.110$ is generic, so this doesn't apply.

2. **Different stratum**: $\alpha_1$ in the *physical* mass formula
   may pick up contributions from the depth-1 partition $(n - 1, 1)$
   via its Plancherel weight $y_{(n-1, 1)}$.  At $H_3$:
   $y_{(2, 1)} = 0.281$ (witness file), so the depth-1 stratum
   contributes
   $0.281 \cdot \chi_{(2, 1)}(\beta) \cdot \log|\chi_{(2, 1)}(\beta)|$
   to the unified mass formula — this is **not** zero, even though
   the structural $\alpha_1 = 0$.  The two notions of "$\alpha_1$"
   are different.

3. **Higher-Hochschild operation beyond Gerstenhaber**: the next
   candidate is the **String-bracket / BV-operator** on the cyclic
   Hochschild complex.  This requires a Calabi–Yau / Frobenius
   structure on $H_n(q)$, which exists ([symmetric algebra
   structure of Hecke at generic $q$, see Linckelmann, Kessar]).
   No agent-feasible explicit computation is currently available.

### What the witness already provides

For the *physical* $\alpha_1$ (avenue 2), the witness data gives:

| $n$ | $\sum_{\lambda \vdash n,\, \mathrm{depth}(\lambda) = 1} y_\lambda$ |
|:--:|---:|
| $3$ | $0.280930$ |
| $4$ | $0.257342$ |
| $5$ | $0.171102$ |
| $6$ | $0.113366$ |
| $9$ | $0.020327$ |
| $12$ | $0.002847$ |

These are non-zero structural numbers — they are the depth-1
Plancherel mass and contribute to the depth-1 stratum coefficient
in [unified mass formula](#prop:unified-curvature-rank-mass-formula).

**Recommendation**: re-name "$\alpha_1$" to disambiguate.  The
*spectral-sequence* $\alpha_1$ is structurally $0$ at generic $q$
(no Gerstenhaber work needed).  The *Plancherel-mass* depth-1
contribution is non-zero and already tabulated.  The unified mass
formula uses the latter.

## Computational effort estimates (agent-session)

| Task | Effort | Status |
|--|:--:|--|
| Confirm Coxeter pattern $r_k$ at $H_4$ | 1–2 sessions | ready: enumerate length-$k$ words, pair via witness |
| Confirm at $H_5, H_6$ | 2–3 sessions | feasible: $p(6) = 11$, witness tabulated |
| Confirm at $H_9$ | 4–5 sessions | $p(9) = 30$, may need symmetry-class enumeration |
| Confirm at $H_{12}$ | $\geq$ 8 sessions | $p(12) = 77$, needs partition-class symmetry pruning |
| Disambiguate $\alpha_1$ definitions | 1 session | content-edit task: clarify in mass-formula doc |
| String-bracket / BV-operator on cyclic $HH^*(H_n)$ | research-grade | beyond single-agent capability |
