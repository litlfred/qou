**Remark (curvature-rank as confinement layer).**

Per
[confinement-categorical](#prop:confinement-categorical), the
collapse of the GB-filtration spectral sequence is the categorical
content of color confinement. Reading the algebraic statement through
QCD vocabulary gives the following dictionary.

**Confinement layers.**

The GB filtration $J^0 \supset J^1 \supset \cdots$ stratifies $A =
H_n(R, q)$ by curvature-rank $k = \mathrm{depth}(\lambda) - 1$. Each
stratum $J^k / J^{k+1}$ is a "confinement layer":

- $k = 0$ (centre): elements are gauge-invariant; this is the
  observable hadron content.
- $k \geq 1$: extracting an element from the layer requires energy
  proportional to the curvature 2-cocycle $F$ (the Hecke + Yang–Baxter
  obstruction), categorically the **string tension**.

**String tension = curvature 2-cocycle.**

The Hecke relation $T^2 = (q - q^{-1}) T + 1$ and Yang–Baxter
relations together define a 2-cocycle $F$ on the GB filtration. $F$
is the obstruction to extracting a non-central element along the
filtration, exactly as the QCD string tension is the obstruction to
extracting an isolated colored quark. The "string" in the QCD
picture is the chain of commutators $[a, b]$ that must be paid to
move an element through layers $J^k$.

**Gluon condensate = chirality channel.**

The chirality cells $D_q^2 = 0$ in the q-Dirac cell scanner ($\lambda =
(2, 1)$ for $H_3$ and analogues at higher $n$) are exactly the
S-fixed central elements of $A$. They form a persistent
gauge-invariant background — the categorical analogue of the **gluon
condensate** in QCD. The match $\mathrm{Vol}(B_3) = 8 G$ with the
gluon octet $\dim \mathfrak{su}(3) = 8$ is the operator-side
identification.

**Hadron mass = sum of confinement layers.**

The unified mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
$$

is then read as: total hadron mass = sum over confinement layers,
each layer contributing its q-deformed Wedderburn-weighted
log-character content (cf. $\tilde w_\lambda$ in
[`prop:plancherel-term-7-formulation`](../braids-and-knots/plancherel-term-7-formulation.md)).

| Stratum | Confinement layer | Physical content |
|---|---|---|
| $k = 0$ | centre / vacuum | photon-like / unconfined |
| $k = 1, 2$ | low-tower | specific hyperbolic-knot ideals (named knots) |
| $k = 3$ | chirality layer | $D_q^2 = 0$, gluon-condensate background |
| $k \geq 4$ | universal residue | Frobenius co-Casimir tail (no specific knot) |

**Predictive consequence.**

Confinement is then not a separate dynamical mechanism on top of the
QOU framework — it is *built in* as the spectral-sequence collapse.
Every prediction of the framework
([universal residue](#prop:plancherel-term-7-formulation),
[$\mathfrak{Q}_\beta$ structural derivation](#)) is automatically gauge-invariant
because the spectral-sequence projection forces it through $Z(A)$.
The rank-3 chirality residue $\mathrm{Vol}(6_1) \cdot |(q;q)_3|$ in
the $\mathfrak{Q}_\beta$ formula is a **gluon-condensate background term**, and
the rank-$\geq 4$ universal Pochhammer tail $|(q;q)_4|$ is the
**Frobenius co-Casimir** — both confinement residues, not free
parameters.
