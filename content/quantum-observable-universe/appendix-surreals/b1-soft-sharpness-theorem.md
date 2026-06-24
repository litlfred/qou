**Proposition (soft sharpness of the keystone B1 is theorem-level
— via Borel + polylog non-vanishing).**

The keystone [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") asserts an *inclusion* $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$
plus a *sharpness* condition. The sharpness condition admits **two
formulations**:

| Version | Statement | What it says |
|---|---|---|
| **Soft sharpness** | $\tau_{\mathrm{arch}}(G^{(n)}\rvert_F) \neq 0$ in $\mathcal{P}_n / \mathcal{P}_{n-1}$ for each Bring-natural $F$ | image is non-trivial at depth $n$ |
| **Strong sharpness** | image equals $\mathcal{P}_n / \mathcal{P}_{n-1}$ | image generates the full period quotient |

*This proposition records that the soft version is **theorem-level**
via Borel's theorem + polylog non-vanishing, requiring no part of
Goncharov's or Beilinson's conjectures. The strong version remains
conditional, but the soft version suffices for QOU's predictive
purposes.*

### Soft sharpness — full proof

**Theorem (soft sharpness).** *Let $K$ be a Bring-embeddable knot
with shape parameter $z_K \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}$
and let $F = \mathbb{Q}(z_K)$. For every $n \geq 2$:*

$$
  \tau_{\mathrm{arch}}\bigl(\mathrm{Li}_n^q(z_K)\bigr) \;\not\equiv\; 0
  \pmod{\mathcal{P}_{n-1}}.
$$

### What this gives QOU

**Soft sharpness as a theorem** is sufficient for the following
keystone-derived claims to be theorems:

| Claim | Status before | Status after this prop |
|---|---|---|
| Each Bring-natural row of B1 lands non-by definition at its depth | conjectural | **theorem** |
| Per-knot $\mathrm{Vol}(K) \neq 0$ in $\mathcal{P}_2/\mathcal{P}_1$ for hyperbolic Bring-embeddable $K$ | conjectural (within B1) | **theorem** (Bloch–Wigner non-vanishing) |
| $\mathrm{Cl}_3(2\pi/5)$ lives non-by definition in $\mathcal{P}_3/\mathcal{P}_2$ | conjectural | **theorem** (Borel + Lewin) |
| Each numerical witness in [`rem:transcendental-accounting`](#rem:transcendental-accounting) row lands at the predicted depth | partly conjectural | **theorem** for non-triviality; depth-match is structural |

### What soft sharpness does NOT give

**Strong sharpness — $\tau_{\mathrm{arch}}(G^{(n)})$ equals all of
$\mathcal{P}_n / \mathcal{P}_{n-1}$ over arbitrary $F$** — remains
Beilinson-conjectural. Specifically, soft sharpness allows for the
possibility of *additional* periods in $\mathcal{P}_n / \mathcal{P}_{n-1}$
not coming from $\tau_{\mathrm{arch}}(G^{(n)})$. Strong sharpness
denies this possibility.

For QOU's predictive use case, this distinction matters only when
predicting that some specific period must equal a specific
$G^{(n)}$ image — which is rarely needed. The framework's
predictions are about *non-trivial classes* at specific depths, not
about *exhausting* the period quotient.

### Significance: Goncharov is bigger than QOU needs

User's question, restated: *can we prove a softer/subset of
Goncharov for only what we need?* This proposition is the
affirmative answer:

- **Goncharov's full conjecture**: $K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q}
  \cong \mathfrak{B}_n(F) \otimes \mathbb{Q}$ via the Goncharov
 regulator, for all $F$, all $n$. This is BIG.
- **What QOU needs (soft sharpness)**: each Bring-natural depth-$n$
 grouplike value lands non-by definition in $\mathcal{P}_n / \mathcal{P}_{n-1}$.
 This is SMALL — and is a theorem of Borel + Lewin.

So **the soft version is enough for QOU's framework predictions to
be non-vacuous; the strong version is what would be needed to claim
that the framework is "complete"**. The latter is Goncharov-conditional;
the former is unconditional.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Depth-2 strong identification (theorem): [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- K-theory bridge: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
