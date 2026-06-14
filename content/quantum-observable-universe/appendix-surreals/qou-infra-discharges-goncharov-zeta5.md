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

See [Table 1](#tbl:qou-infra-discharges-goncharov-zeta5-table1-data).

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

See [Table 2](#tbl:qou-infra-discharges-goncharov-zeta5-table2-data).

This is **a substantive but partial result**: it would close one
specific cyclotomic case, not the general statement.
### Cross-references

- Keystone: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) ("B1")
- Depth-2 theorem-level identification: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Joint Galois $\times$ braid action: [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Conway-KT precedent: [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- K-theory bridge: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
