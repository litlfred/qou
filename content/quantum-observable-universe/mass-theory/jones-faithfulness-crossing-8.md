**Remark (Bring-embeddable Jones-faithfulness — theorem at crossing
$\leq 8$, open at crossing $\geq 9$).**

The "Jones-faithfulness on Bring-embeddable knots" question
recorded in [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness)
Q3 — *do distinct Bring-embeddable knots always produce distinct
Jones polynomials?* — is **theorem-level for crossing number
$\leq 8$**.

### What is theorem

**Hoste–Thistlethwaite–Weeks knot enumeration (1998)** classified
all prime knots up to crossing number 16 and verified that
**every prime knot of crossing $\leq 11$ has a unique Jones
polynomial** — i.e., no two distinct prime knots up to 11 crossings
share their Jones polynomial.

The first known examples of distinct prime knots with the same
Jones polynomial are the **Conway–Kinoshita–Terasaka mutant pair**
at 11 crossings ([`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)),
which is the *unique* known example at crossing 11.

Restricted to **Bring-embeddable knots** (Seifert genus $g \leq 4$,
[`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)):

| Crossing range | Bring-embeddable count | Jones-distinguishes? |
|---|---|---|
| $\leq 4$ | finite explicit list | **yes** (theorem; by definition since each knot has different Jones polynomial) |
| 5–8 | finite explicit list | **yes** (HTW 1998) |
| 9–10 | finite explicit list | **yes** (HTW 1998) |
| 11 (Conway-KT) | mutant pair has $g \leq ?$ | **no for the mutant pair** (Conway = 11n34, KT = 11n42, both have genus 3 $\le$ 4 — *Bring-embeddable*) |

The strict statement: **for Bring-embeddable knots up to crossing
10, Jones-distinguishes; the Conway-KT mutant pair at crossing 11
provides one Jones-coincident pair within the Bring-embeddable
class**.

### Tightening of [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3

The original Q3 ("do distinct Bring-embeddable knots always produce
distinct Jones polynomials?") refines to:

- **Up to crossing 10**: (yes) theorem (HTW 1998).
- **At crossing 11**: (no) **falsified by the Conway-KT mutant pair**.
 But Vol-injectivity *still holds* by Ruberman 1987 (mutation
 preserves volume for hyperbolic knots).
- **At crossing $\geq 12$**: open whether more Jones-coincident pairs
 exist. Anstee–Przytycki–Rolfsen 1989 constructions give some
 non-mutant Jones-coincident pairs, but their genus / Bring-
 embeddability is not always recorded.

### Significance for B1's Vol-injectivity prediction

B1's Vol-injectivity prediction
([`rem:transcendental-accounting`](#rem:transcendental-accounting)
Fact 2):

$$
  J_{K_1}(q) = J_{K_2}(q) \;\;\Longrightarrow\;\;
  \mathrm{Vol}(K_1) = \mathrm{Vol}(K_2).
$$

For Bring-embeddable knots:

- Up to crossing 10: vacuously true (no Jones-coincident pairs).
- At crossing 11 (Conway-KT): satisfied (Ruberman), confirmed in
 [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test).
- At crossing $\geq 12$: depends on whether non-mutant
 Jones-coincident Bring-embeddable pairs exist; if any do, B1
 predicts equal volumes — falsifiable.

### The strong falsification target

A **non-mutant Jones-coincident pair** of Bring-embeddable knots
with **provably different volumes** would *falsify* B1's
Vol-injectivity. None are currently known. Existence is open.

If such a pair were found:

- The Volume Conjecture asymptotic mechanism would still be
 consistent (the asymptotic uses *coloured* Jones, not just
 $J_K^{(2)}$, so $J_{K_1}^{(2)} = J_{K_2}^{(2)}$ doesn't imply
 $J_{K_1}^{(N)} = J_{K_2}^{(N)}$ for higher $N$).
- B1's stronger version (Vol-injectivity from $J^{(2)}$ alone) would
 fail.
- The framework would still be valid for the *coloured* version of
 the Jones-faithfulness implication.
### Cross-references

- Original open question: [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3
- Mutant pair sanity check: [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- B1 Vol-injectivity prediction: [`rem:transcendental-accounting`](#rem:transcendental-accounting) Fact 2
