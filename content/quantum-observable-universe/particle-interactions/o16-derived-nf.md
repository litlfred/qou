**Example.**
Oxygen-16 ($Z = 8$, $N = 8$, $A = 16$) is the first
**doubly-magic** nucleus beyond helium-4.  Both $Z = 8$ and
$N = 8$ are nuclear magic numbers, corresponding to closure of
the $1p$ shell.

## Construction

The derived atom $\mathcal{A}(8, 8)$ is built by the
5-step construction
([derived atom](#def:derived-atom)):

1. **48 pair productions** ($3 \times 16$ photon collisions)
   $\to$ 16 quark triples.

2. **16 Borromean confinements** ($\mathcal{B}_3$ for each nucleon)
   $\to$ 8 proton NFs + 8 neutron NFs.

3. **Inductive nuclear assembly** — 15 inter-nucleon crossings,
   each followed by Gröbner--Shirshov reduction
   ([inductive GB reduction](#prop:inductive-gb-reduction)):

$$
  \mathcal{N}_{\leq k+1}
  =
  \mathrm{NF}\!\left(
    \mathcal{N}_{\leq k}
    \cdot \Phi_k
    \cdot \mathfrak{N}_{k+1}
  \right)
$$

   where $\Phi_k$ is the demand-minimizing operator at step $k$
   ([nuclear operator regimes](#prop:nuclear-operator-regimes)).

4. **8 electron Hopf links** $\to$ closed $1s^2 2s^2 2p^4$
   electron configuration.

## Expected operator sequence

By the three-regime theory
([nuclear operator regimes](#prop:nuclear-operator-regimes)),
the 15 inter-nucleon operators are predicted to follow the pattern:

| Steps | Shell | Operators | Regime |
|:---|:---|:---|:---:|
| $1 \to 4$ | $1s$ filling | $T_{2,5}$, $L_+$, $L_+$ | I $\to$ II |
| $5 \to 8$ | $1p$ proton fill | $L_-$, $C_{pn}$, $C_{pp}$, $C_{pn}$ | II $\to$ III |
| $9 \to 12$ | $1p$ neutron fill | $L_+$, $C_{pn}$, $C_{nn}$, $C_{pn}$ | II $\to$ III |
| $13 \to 16$ | shell closure | $L_+$ (magic), ... | II |

At step 16 ($N = 8$, magic), the final operator should be a
Hopf link achieving demand closure — the $1p$ neutron shell
closes.

## Scaling

The inductive reduction for $A = 16$ requires at most 15 Hecke
multiplications, each involving NF elements of bounded size.
The NF at each step has at most $\binom{15}{k}$ terms of
length $\leq 15$, but the Hecke reduction collapses this
to a polynomial number of NF basis elements
([inductive GB reduction](#prop:inductive-gb-reduction)).

At $A = 16$, the unreduced braid word has $\sim 10^{10}$ terms.
The inductive approach reduces this to $\leq 128$ NF terms
with $\leq 480$ Hecke steps — tractable with the existing
Hecke engine.

## Doubly magic prediction

The periodic table demand conjecture
([demand conjecture](#conj:periodic-table-demand))
predicts that $\mathcal{A}(8, 8)$ minimizes
$|\mathrm{dem}|$ among all $A = 16$ isotopes.
This requires computing $\mathcal{A}(Z, 16 - Z)$ for all
$0 \leq Z \leq 16$ and comparing demand magnitudes.

If both the proton ($Z = 8$) and neutron ($N = 8$) shells
achieve demand closure independently, then the doubly-magic
nucleus has $|\mathrm{dem}| = 0$ — complete stability.

**Witness**: computation pending
(`four-term-photon-to-atoms.py` with $A = 16$ extension).
