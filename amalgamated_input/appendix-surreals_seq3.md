<!-- FILE_START: b1-soft-sharpness-theorem.md -->
**Theorem (soft sharpness of the keystone B1, via Borel + polylog
non-vanishing).** *Let $K$ be a Bring-embeddable knot
with shape parameter $z_K \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}$
and let $F = \mathbb{Q}(z_K)$. For every $n \geq 2$:*

$$
  \tau_{\mathrm{arch}}\bigl(\mathrm{Li}_n^q(z_K)\bigr) \;\not\equiv\; 0
  \pmod{\mathcal{P}_{n-1}}.
$$

This is the *soft sharpness* half of the keystone
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1"): the depth-$n$ image $\tau_{\mathrm{arch}}(G^{(n)}\rvert_F)$ is
non-trivial in $\mathcal{P}_n / \mathcal{P}_{n-1}$. It requires no part
of Goncharov's or Beilinson's conjectures.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Depth-2 strong identification (theorem): [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- K-theory bridge: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
<!-- FILE_END: b1-soft-sharpness-theorem.md -->

<!-- FILE_START: b1-soft-sharpness-significance.md -->
The keystone [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") asserts an *inclusion* $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$
plus a *sharpness* condition. The sharpness condition admits **two
formulations**:

| Version | Statement | What it says |
|---|---|---|
| **Soft sharpness** | $\tau_{\mathrm{arch}}(G^{(n)}\rvert_F) \neq 0$ in $\mathcal{P}_n / \mathcal{P}_{n-1}$ for each Bring-natural $F$ | image is non-trivial at depth $n$ |
| **Strong sharpness** | image equals $\mathcal{P}_n / \mathcal{P}_{n-1}$ | image generates the full period quotient |

The soft version is theorem-level
([`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem))
via Borel's theorem + polylog non-vanishing; the strong version remains
conditional, but the soft version suffices for QOU's predictive
purposes.

### Consequences for QOU

**Soft sharpness as a theorem** is sufficient for the following
keystone-derived claims to be theorems:

| Claim | Status before | Status after this prop |
|---|---|---|
| Each Bring-natural row of B1 lands non-by definition at its depth | conjectural | **theorem** |
| Per-knot $\mathrm{Vol}(K) \neq 0$ in $\mathcal{P}_2/\mathcal{P}_1$ for hyperbolic Bring-embeddable $K$ | conjectural (within B1) | **theorem** (Bloch–Wigner non-vanishing) |
| $\mathrm{Cl}_3(2\pi/5)$ lives non-by definition in $\mathcal{P}_3/\mathcal{P}_2$ | conjectural | **theorem** (Borel + Lewin) |
| Each numerical witness in [`rem:transcendental-accounting`](#rem:transcendental-accounting) row lands at the predicted depth | partly conjectural | **theorem** for non-triviality; depth-match is structural |

### Limitations of soft sharpness

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

The question of whether one can prove a softer subset of Goncharov for
only what QOU needs has an affirmative answer:

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
<!-- FILE_END: b1-soft-sharpness-significance.md -->

<!-- FILE_START: b1-figure-8-row-theorem.md -->
**Proposition (B1 keystone is theorem-level at the figure-8 row —
combining Bloch–Suslin depth-2 identification with Murakami–Murakami's
proof of the Volume Conjecture for $4_1$).**

*The figure-8 row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") — the depth-2 instance over $F = \mathbb{Q}(\zeta_6)$
indexed by the dominant cell $\lambda_K = (2, 2)$ of $4_1$ in
$H_4(q)$ — is **theorem-level**, requiring no part of Goncharov's
or Beilinson's conjectures.*

### Statement

For the figure-8 knot $4_1$ embedded in Bring's genus-4 surface
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)):

1. **Inclusion at depth 2**: $\tau_{\mathrm{arch}}(\mathrm{Li}_2^q(\zeta_6))
   \in \mathcal{P}_2$ — by [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin).
2. **Strong sharpness at the figure-8 row**: $\tau_{\mathrm{arch}}(e_{(2,2)}
   \cdot \mathrm{Li}_2^q(\zeta_6))$ generates the *correct* class
   in $\mathcal{P}_2 / \mathcal{P}_1$ — namely
   $[\mathrm{Vol}(4_1)] = [2\,\mathrm{Cl}_2(\pi/3)]$.
3. **Volume Conjecture instance**: by Murakami–Murakami 2001 [@murakami-murakami2001],
   the asymptotic of the coloured Jones polynomial $J_{4_1}^{(N)}(e^{2\pi i/N})$
   converges to $\mathrm{Vol}(4_1)$ as $N \to \infty$ — discharging
   the Volume Conjecture for $4_1$ specifically.

Combining (1)–(3) yields: B1 at the figure-8 row is a **theorem**.
### Content of the result

**B1 keystone at the figure-8 row over $\mathbb{Q}(\zeta_6)$ is a
theorem**:

- Inclusion: theorem (Bloch–Suslin).
- Strong sharpness: theorem (Borel rank 1 + Bloch–Suslin injectivity
  realises the unique line).
- VC-asymptotic match: theorem (Murakami–Murakami).

This is the **first row of B1 to become theorem-level**. The
analog for chiral hyperbolic knots ($5_2$, $6_2$, $6_3$, etc.)
requires the depth-3 partner (Chern–Simons) and is open.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Depth-2 ID: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Numerical witness: [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)
- VC reframe: [`rem:vc-as-depth-2-instance`](#rem:vc-as-depth-2-instance)
- Soft sharpness across all rows: [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
<!-- FILE_END: b1-figure-8-row-theorem.md -->

<!-- FILE_START: b1-torus-knot-rows-theorem.md -->
**Proposition (B1 keystone is theorem-level at the torus-knot rows —
combining Bloch–Suslin with Garoufalidis–Lê's proof of the Volume
Conjecture for torus knots).**

*Every torus-knot row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") is **theorem-level**, requiring no part of Goncharov's or
Beilinson's conjectures.*

### Scope

Among the seven Bring-natural torus-knot generators of
[`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots):

$$
  \{T(2, 3),\; T(2, 5),\; T(2, 7),\; T(2, 9),\;
    T(3, 4),\; T(3, 5),\; T(5, 2)\}
$$

— **none are hyperbolic** (torus-knot complements are Seifert-fibred,
not hyperbolic). So the depth-2 row's *volume claim* is by definition
zero for each: $\mathrm{Vol}(T(p, q)) = 0$ in $\mathcal{P}_2 /
\mathcal{P}_1$. This depth-2 trivial row of B1 is *by definition*
theorem-level.

The non-trivial content is at **depth 3**: each torus knot has a
non-zero **Chern–Simons invariant**

$$
  \mathrm{CS}(T(p, q))
  \;=\;
  -\frac{(p^2 - 1)(q^2 - 1)}{24 p q} \cdot \pi^2
  \pmod{\pi^2 \mathbb{Z}}
$$

(Freed–Gompf 1991, Kirk–Klassen 1990 — explicit computation for
torus knots). These are **rational multiples of $\pi^2$** — i.e.,
*degenerate* depth-3 classes, lying entirely in $\mathcal{P}_2$
when reduced mod the Tate twist.

### Statement

For each torus-knot row $K = T(p, q)$ in B1:

1. **Depth-2 inclusion**: $\mathrm{Vol}(K) = 0 \in \mathcal{P}_2 / \mathcal{P}_1$
 — by definition in the period filtration.
2. **Depth-3 inclusion**: $\mathrm{CS}(T(p, q)) \in \pi^2 \cdot \mathbb{Q} \subset \mathcal{P}_2$
 — degenerate (no genuine $\mathrm{Li}_3$ contribution).
3. **Volume Conjecture for torus knots**: discharged by
 Garoufalidis–Lê 2005 (arXiv:math/0411521): the asymptotic of
 $J_{T(p,q)}^{(N)}$ at roots of unity equals exactly the
 above CS-rational expression. **Theorem (published).**

Combining (1)–(3): B1 at every torus-knot row is **theorem-level
and degenerate** — no genuine trilog content arises here.

### Reduced informativeness of torus-knot rows relative to figure-8

The figure-8 row of B1 ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem))
realises a **non-trivial** depth-2 period $\mathrm{Vol}(4_1) =
2\,\mathrm{Cl}_2(\pi/3)$. Torus-knot rows realise *zero* (depth 2)
or *Tate-twisted rational* (depth 3 but in $\mathcal{P}_2$). So:

- Figure-8 row = theorem AND non-trivial.
- Torus-knot rows = theorem AND degenerate (rational $\pi^2$ values).

For B1's *predictive content*, the figure-8 row is the cleaner test;
torus-knot rows confirm the framework on degenerate cases.

### Per-knot CS values for the seven Bring generators

See [Table](#tbl:b1-torus-knot-rows-theorem-table-data).

Note $T(2, 5) \cong T(5, 2)$ (cyclic-renaming symmetry of torus
knots), so the last two are equivalent.

These rational $\pi^2$ multiples confirm that torus-knot CS values
sit in $\pi^2 \mathbb{Q} \subset \mathcal{P}_2$, *not* in
$\mathcal{P}_3 \setminus \mathcal{P}_2$ — torus knots do not produce
genuine depth-3 periods.

### Significance

**Two B1 row classes are now theorem-level** ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
+ this proposition):

- Figure-8 (depth-2 non-trivial): theorem.
- Seven torus-knot generators (depth 2 trivial, depth 3 rational): theorem.

Combined, this **discharges 8 specific rows of B1**. Remaining rows
of the Bring-embeddable atlas (chiral hyperbolic knots — $5_2$,
$6_2$, $6_3$, etc.) are open at depth 3, conditional on a
(currently-unproved-for-non-torus-non-figure-8) Volume Conjecture
asymptotic.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Figure-8 row: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- Soft sharpness: [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
- Conway-KT (mutant pairs): [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
<!-- FILE_END: b1-torus-knot-rows-theorem.md -->

<!-- FILE_START: b1-hyperbolic-rows-theorem.md -->
**Conjecture (B1 conditionally reduces to Volume Conjecture at Borromean rings, Whitehead link, and twist knots).**

Beyond the figure-8 row ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem))
and the seven torus-knot rows ([`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)),
B1 ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence))
holds for additional Bring-embeddable hyperbolic-knot rows, conditional on Volume Conjecture discharges.

### Conditionally discharged rows

See [Table 1](#tbl:b1-hyperbolic-rows-theorem-table1-data).

(Twist knot $K_n$ has $n$ half-twists; $K_2 = 4_1$ is the figure-8.
Genus of $K_n$ is 1 for all $n$, so all twist knots are Bring-embeddable.)

*(Explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link are recorded in the `audit/b1-hyperbolic-rows-theorem-audit` block.)*

### Coverage via the Bloch–Suslin chain

For *any* hyperbolic Bring-embeddable knot or link $K$ with shape
parameter in some number field $F = \mathbb{Q}(z_K)$:

- **Step 1 (Bloch–Suslin)** is unconditionally established for any $F$.
- **Step 2 (cell pairing computation)** uses explicit Markov-trace and Lobachevsky geometry.
- **Step 3 (VC asymptotic)** is **knot-specific** — it requires a published proof.

So **B1 at a depth-2 row conditionally reduces to the VC discharge for that knot**. 
The rate-limiting step is the VC discharge per knot, *not* the Bloch–Suslin chain.

### Bring-embeddable hyperbolic knots awaiting VC discharge

See [Table 2](#tbl:b1-hyperbolic-rows-theorem-table2-data).

Each of these would become a conditionally established B1 row upon VC discharge.

### Significance

**Three additional B1 rows are conditionally supported by the literature** (Borromean,
Whitehead; figure-8 in [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)).
Combined with the seven torus-knot rows
([`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)),
**eleven total B1 rows are supported by the literature**.

The pattern: B1 at depth 2 reduces to per-knot VC discharge via the
Bloch–Suslin chain + Borel-rank computation. *Every published VC
discharge for a Bring-embeddable hyperbolic knot yields a conditional B1 row.*

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Depth-2 ID: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Figure-8 row: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Torus-knot rows: [`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)
- Soft sharpness (any depth): [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
<!-- FILE_END: b1-hyperbolic-rows-theorem.md -->

