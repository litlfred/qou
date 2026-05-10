**Conjecture (QOU's Hecke-NF + Bring-$S_5$ infrastructure
discharges Goncharov's depth-3 conjecture at $F = \mathbb{Q}(\zeta_5)$).**

The depth-2 identification
([`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin))
is theorem-level via Bloch–Suslin. The depth-3 case requires
**Goncharov's motivic conjecture** as the missing piece (Step 2 of
the proof chain there). *This conjecture proposes that QOU's
existing infrastructure suffices to discharge Goncharov's
conjecture for $F = \mathbb{Q}(\zeta_5)$.*

### The reduced target

Goncharov's conjecture asserts $K_5^{\mathrm{ind}}(F) \otimes \mathbb{Q}
\cong \mathfrak{B}_3(F) \otimes \mathbb{Q}$, with $\mathfrak{B}_3(F)$
the weight-3 Bloch group on $F^\times$ modulo the **22-term
relation** (the trilog analog of Bloch's 5-term).

For $F = \mathbb{Q}(\zeta_5)$: Borel gives
$\dim_\mathbb{Q} K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q} = 2$
([`prop:borel-partial-resolution`](#prop:borel-partial-resolution)).
The Goncharov regulator maps this rank-2 space into
$\mathcal{P}_3 / \mathcal{P}_2$ over $\mathbb{Q}(\zeta_5)$.

The **reduced target** for QOU: prove that $\{\mathrm{Li}_3(\zeta_5^k) : k = 1, 2, 3, 4\}$
modulo the multiplication-formula identity span exactly this rank-2
image, with the only further relation being the Goncharov 22-term
restricted to $\zeta_5$-arguments.

### QOU's tools available

| Tool | Role in attacking Goncharov at $\mathbb{Q}(\zeta_5)$ |
|---|---|
| Recursive atom-knot atlas | explicit braid words for $g \leq 4$ knots over Bring-natural shape parameters |
| Hecke normal form (Gröbner–Shirshov) | canonical reduction; equality of NF $\Leftrightarrow$ equality in $H_n(q)$ |
| Markov trace pinning | unique trace; equality of Markov traces $\Leftrightarrow$ Jones-coincident pair |
| GB stratification (depth grading) | filters Hecke centre by max-hook; depth-$k$ projector $\mathrm{proj}_{Z^{(k)}(A)}$ extracts depth-$k$ component |
| JM-element + Lagrange-interpolation $e_\lambda$ | explicit central idempotents — concrete generators of period classes per [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent) |
| Bring's $S_5$-cyclotomic structure | natural action on $\{\zeta_5^k : k \in (\mathbb{Z}/5)^\times\}$ |
| Joint Galois × braid action ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) | structures the period-class permutations |

### Avenue A — Jones-coincident pair generation

For each Jones-coincident pair of Bring-embeddable knots
$(K_1, K_2)$ with $J_{K_1}(q) = J_{K_2}(q) \in \mathbb{Z}[q^{\pm 1}]$,
one obtains:

- a depth-2 equality $\mathrm{Vol}(K_1) = \mathrm{Vol}(K_2)$
  (Volume Conjecture asymptotic + Ruberman for mutants);
- a depth-3 equality $\mathrm{CS}(K_1) = \pm\mathrm{CS}(K_2)$
  (chirality factor depending on whether the pair is mutant or
  not).

If we **enumerate** Jones-coincident pairs over the Bring-embeddable
class systematically (Hecke-NF gives canonical representatives, so
two distinct NFs with equal Markov trace = a Jones-coincident pair),
we obtain a **generating list of depth-3 relations** among CS
invariants. Question: do these relations **span** the kernel of
$K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q} \to \mathbb{R}/\pi^4\mathbb{Q}$?

If yes — **Goncharov's conjecture at $\mathbb{Q}(\zeta_5)$ is
implied by Hecke NF redundancy**, dischargeable in QOU's framework.

### Avenue B — Direct construction of the 22-term-style relation

Goncharov's 22-term relation, restricted to $z \in \{\zeta_5^k\}$:
expressible as a specific element $G_{22}(\zeta_5) \in
\mathbb{Q}\langle \mathrm{Li}_3(\zeta_5), \mathrm{Li}_3(\zeta_5^2),
\ldots \rangle$ that equals $0$ modulo $\mathcal{P}_2$.

**Program**: find a Hecke element $\beta \in H_n(q)$ for some $n$
with:

1. *Markov trace condition*. $\tau_{\mathrm{arch}}(\mathrm{tr}_M(\beta))$
   at $q \to \zeta_5$ equals $G_{22}(\zeta_5)$.

2. *NF-reduction condition*. The Hecke NF of $\beta$ reduces to
   the identity element in $H_n(q)$ modulo depth-$\leq 2$ terms
   under the GB stratification.

If both hold, $\mathrm{tr}_M(\beta) = 0 \pmod{\text{depth} \leq 2}$
in $\mathcal{H}_q$, so $G_{22}(\zeta_5) = 0$ in $\mathcal{P}_3 / \mathcal{P}_2$
**by NF reduction alone**. The 22-term relation at $\zeta_5$ becomes
a **theorem** of QOU's infra rather than a Goncharov conjecture.

The hardest step is (1): expressing $G_{22}(\zeta_5)$ as a Markov
trace of a *specific* Hecke element. This is doable:

- The Markov trace of any closed-braid product
  $\sigma_{i_1}^{a_1} \sigma_{i_2}^{a_2} \cdots$ at $q = \zeta_5$
  is a $\mathbb{Z}[\zeta_5]$-linear combination of $\mathrm{Li}_3$
  values via the Faddeev–Kashaev / Reshetikhin–Turaev quantum-invariant
  expansion.
- The 22-term relation involves 22 specific algebraic arguments;
  each can be realised as a Markov trace of an explicit braid in
  some $H_n(q)$.

### What this would discharge / not discharge

If Avenue A or B succeeds:

| Discharged | Not discharged |
|---|---|
| Goncharov's conjecture at $F = \mathbb{Q}(\zeta_5)$, depth 3 | Goncharov over arbitrary $F$ |
| Image identification $G^{(3)}\big|_{\mathbb{Q}(\zeta_5)} \cong K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q}$ | Same identification for non-Bring-natural fields |
| Depth-3 case of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) at one specific cyclotomic field | Beilinson's full conjecture at depths $\geq 4$ |
| Goncharov's motivic conjecture at $\mathbb{Q}(\zeta_5)$ | Same conjecture at $\mathbb{Q}(\zeta_n)$ for $n \neq 5, 6, 4$ |

This is **a substantive but partial result**: it would close one
specific cyclotomic case, not the general statement.

### Status and roadmap

**Open.** Both avenues require non-trivial new computation:

- Avenue A: need to enumerate Jones-coincident pairs in the
  Bring-embeddable class. The recursive atom-knot atlas already
  has the braid words; the Hecke NF reduction would highlight
  pairs with identical NF tail but different head. The
  Anstee–Przytycki–Rolfsen 1989 construction provides explicit
  examples to start from.
- Avenue B: need to express the Goncharov 22-term relation at
  $\zeta_5$ as a Markov trace of an explicit Hecke element. The
  key technical step is identifying the right $H_n(q)$ and the
  right braid word.

Both are concrete projects of approximately 1–2 weeks of focused
work for a contributor familiar with both QOU's Hecke / NF
infrastructure and Goncharov's depth-3 polylogarithm machinery.

### Cross-references

- Keystone: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) ("B1")
- Depth-2 theorem-level identification: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Joint Galois × braid action: [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Conway-KT precedent: [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- K-theory bridge: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
