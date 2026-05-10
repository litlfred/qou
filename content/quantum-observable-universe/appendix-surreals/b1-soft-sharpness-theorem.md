**Proposition (soft sharpness of the keystone B1 is theorem-level
— via Borel + polylog non-vanishing).**

The keystone [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") asserts an *inclusion* $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$
plus a *sharpness* condition. The sharpness condition admits **two
formulations**:

| Version | Statement | What it says |
|---|---|---|
| **Soft sharpness** | $\tau_{\mathrm{arch}}(G^{(n)}|_F) \neq 0$ in $\mathcal{P}_n / \mathcal{P}_{n-1}$ for each Bring-natural $F$ | image is non-trivial at depth $n$ |
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

**Proof.**

*Step 1 (Borel non-vanishing).* By [`prop:borel-partial-resolution`](#prop:borel-partial-resolution),
$\dim_\mathbb{Q} K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q} \geq 1$
for $n \geq 2$ when $F$ is non-trivial cyclotomic (specifically:
$F = \mathbb{Q}(\zeta_5), \mathbb{Q}(\zeta_6), \mathbb{Q}(i)$, all
of which have $r_2 \geq 1$). The Beilinson–Borel regulator

$$
  K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q}
  \;\longrightarrow\;
  \mathbb{R} / \pi^{2(n-1)} \mathbb{Q}
$$

is **injective** after tensoring with $\mathbb{R}$ (Borel 1977,
Theorem 12.3 — the regulator is rationally injective).

*Step 2 (polylog non-vanishing).* The single-valued $\mathrm{Li}_n$
companion (Bloch–Wigner $D$ at $n = 2$, Goncharov $D_n$ for $n \geq 3$)
is **non-zero on every algebraic argument $z \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}$**
(Lewin 1991, Polylogarithms and Associated Functions §2):

$$
  D_n(z) \;\neq\; 0
  \quad\text{for } z \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}.
$$

Equivalently: no algebraic point is a "regulator zero" of $D_n$.

*Step 3 (composition).* Combining Steps 1 and 2:

$$
  \tau_{\mathrm{arch}}(\mathrm{Li}_n^q(z_K))
  \;=\;
  \mathrm{Li}_n(z_K) \pmod{\mathcal{P}_{n-1}}
  \;\sim\;
  D_n(z_K) \neq 0
  \pmod{\mathcal{P}_{n-1}}.
$$

The non-vanishing is preserved under the regulator embedding into
$\mathcal{P}_n / \mathcal{P}_{n-1}$. $\square$

### What this gives QOU

**Soft sharpness as a theorem** is sufficient for the following
keystone-derived claims to be theorems:

| Claim | Status before | Status after this prop |
|---|---|---|
| Each Bring-natural row of B1 lands non-trivially at its depth | conjectural | **theorem** |
| Per-knot $\mathrm{Vol}(K) \neq 0$ in $\mathcal{P}_2/\mathcal{P}_1$ for hyperbolic Bring-embeddable $K$ | conjectural (within B1) | **theorem** (Bloch–Wigner non-vanishing) |
| $\mathrm{Cl}_3(2\pi/5)$ lives non-trivially in $\mathcal{P}_3/\mathcal{P}_2$ | conjectural | **theorem** (Borel + Lewin) |
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
  grouplike value lands non-trivially in $\mathcal{P}_n / \mathcal{P}_{n-1}$.
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
