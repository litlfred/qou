The [metallic character proposition](#prop:metallic-character-knot)
classifies metals by the size of the residual sub-link $R$.
Metallic character is strongest when $|R|$ is smallest and the
shell number $n$ is largest.  Both conditions are simultaneously
extremised by a single element: **francium** ($p = 87$).

**Francium's electron cloud.**

Francium has 87 electrons partitioned as

$$
  \mathcal{E}(87)
  = 
  \underbrace{S_1 \sqcup S_2 \sqcup \cdots \sqcup S_6}_{86
  \text{ electrons in closed sub-links (radon core)}}
  \sqcup
  \underbrace{R}_{|R| = 1}.
$$

The inner 86 trefoils form the
[noble gas](#prop:noble-gas-characterization) configuration of
radon — six fully closed sub-Hopf links, every curl interlocked.
The 87th trefoil sits alone in shell $n = 7$: a **single loose
curl** weakly Hopf-linked to the radon core.

**Why francium is extremal.**

Among all stable (or near-stable) atoms, francium minimises the
outermost crossing energy in two independent ways:

1. **Minimal residual**: $|R| = 1$.  The lone trefoil has no
   partner to interlock with — it occupies an open linking
   site with no compensating closure.  Any element with
   $|R| \geq 2$ has at least partial interlocking among its
   residual trefoils, raising the detachment energy.

2. **Maximal shell depth**: $n = 7$.  The crossing energy
   scales as
   $\mathfrak{E}_{\mathrm{cross}} \propto 1/n^2$
   ([crossing energy](#def:crossing-energy)), so the $n = 7$
   trefoil is the most weakly bound of any alkali.

Together these give francium:

- The **lowest ionization energy** of any element
  ($E_{\mathrm{ion}} \approx 4.07 \mathrm{eV}$).
- The **highest electropositive character** — it donates its
  lone curl more readily than any other atom.
- The **strongest metallic bonding tendency** — its single
  open linking site couples to any neighbouring residual
  sub-link with negligible crossing cost.

**The alkali series as a monotone sequence.**

The alkali metals form a sequence of atoms with $|R| = 1$ at
increasing shell depth:

| Alkali | $p$ | Shell $n$ | $E_{\mathrm{ion}}$ (eV) | Curls in residual |
|--------|----:|----------:|------------------------:|:-----------------:|
| Li | 3 | 2 | 5.39 | 1 |
| Na | 11 | 3 | 5.14 | 1 |
| K | 19 | 4 | 4.34 | 1 |
| Rb | 37 | 5 | 4.18 | 1 |
| Cs | 55 | 6 | 3.89 | 1 |
| Fr | 87 | 7 | 4.07 | 1 |

Each has exactly one loose trefoil; the crossing energy
decreases monotonically with $n$ (the slight uptick for
francium reflects relativistic contraction of the $7s$ orbital,
which in the knot picture corresponds to a small tightening
of the Hopf linking to the nuclear Borromean core at high $p$).

**Dual extremum: fluorine.**

At the opposite end of the residual spectrum sits **fluorine**
($p = 9$), with $|R| = 7$ out of a shell-2 capacity of 8.
Its residual sub-link is one trefoil short of closure — one
empty linking site.  This makes fluorine the **most
electronegative** element: it pulls in a trefoil from any
neighbour to close its sub-link, the topological dual of
francium donating its lone curl.

$$
  \underbrace{\text{Fr}: |R| = 1}_{\text{most metallic}}
  \qquad\longleftrightarrow\qquad
  \underbrace{\text{F}: |R| = 2n^2 - 1}_{\text{most nonmetallic}}
$$

The entire metallic--nonmetallic spectrum is thus parametrised
by a single topological invariant: the **filling fraction**
$|R| / 2n^2$ of the outermost sub-Hopf link.
