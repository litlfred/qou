**Conjecture (closed-sector state-integral bridge — Vol-conjecture-style adoption).**
For a hyperbolic knot $K \subseteq S^3$, the resurgent Stokes constant of the
state integral of $S^3 \setminus K$ on its distinguished (geometric Borel) ray
is a **Donaldson--Thomas invariant / BPS degeneracy** of the associated
$3$d $\mathcal{N}=2$ theory $T[K]$:

$$
  \mathfrak{S}(K) \;=\; \Omega_{\mathrm{DT}}(K) \;=\; \dim \mathcal{H}_{\mathrm{BPS}}(T[K]),
$$

where $\mathfrak{S}(K)$ is the Stokes constant, $\Omega_{\mathrm{DT}}(K)$ the
Donaldson--Thomas / Kontsevich--Soibelman invariant of the $q$-difference
structure, and $\mathcal{H}_{\mathrm{BPS}}(T[K])$ the space of BPS states whose
graded dimension categorifies the $3$d index.

For the general setting of the middle term: a BPS structure $(Z, \Gamma, \Omega)$ carries Donaldson--Thomas invariants $\Omega(\gamma)$, and to it is attached a Riemann--Hilbert problem \cite[\S2, \S4]{bridgeland2016}. For finite, uncoupled, integral BPS structures that problem has an explicit solution in products of gamma functions \cite[\S3.2]{bridgeland2016}. The knot BPS structures in this conjecture are not shown to be uncoupled, so that result is context, not a case of the conjecture. On the state-integral side, one-dimensional state integrals of products of Faddeev quantum dilogarithms, including those of $4_1$ and $5_2$, are finite sums of products of a $q$-series and a $\tilde q$-series, and the generating $q$-series is admissible in the sense of Kontsevich--Soibelman \cite[\S1.1, \S1.3--1.4]{garoufalidis2013}.

The first equality is
[`garoufalidis-gu-marino2023peacock`] Conjecture 3(d) — *"the Stokes
constants are integers corresponding to the Donaldson--Thomas invariants and the
BPS degeneracies"* — which Garoufalidis--Gu--Mariño state as a **conjecture and
do not prove for any knot**, $4_1$ included. What they prove is their
Conjecture 5 for $4_1$ and $5_2$ (their Theorem 6, via Theorems 17 and 25), and
they verify Conjecture 4 for both knots by computation (§5.2, §6.2). The second is the [`gukov-pei-putrov-vafa2017`] (GPPV) realisation of the
DT/BPS count as the graded dimension of the fivebrane BPS Hilbert space of
$T[M_3]$ on $M_3 \times D^2$, categorifying the $3$d $\mathcal{N}=2$ indices. The
$3$d--$3$d dictionary itself --- the assignment of a $3$d $\mathcal{N}=2$ theory
$T[M]$ to an ideally triangulated $3$-manifold, with $S^3 \setminus 4_1$ worked
explicitly, and the assembly of its $S^3_b$ partition function (the state integral
whose Stokes constants appear above) from tetrahedron factors --- is
[`dimofte-gaiotto2011`] §4.1, §4.6 and §6.3. The $3$d index of that theory is
[`dimofte-gaiotto-gukov2013`] (DGG).

Part of the second equality is a theorem on a restricted class: [`murakami-y2022`]
proves that for plumbed $3$-manifolds with negative-definite linking matrix the
Witten--Reshetikhin--Turaev invariant is the radial limit of the homological block
$\hat{Z}$. That class consists of closed manifolds; $S^3 \setminus K$ for a
hyperbolic knot is cusped and not plumbed, so the result does not reach the objects
this conjecture quantifies over, and the field `dt_eq_bps` below stays an assumption
rather than a citation.

### Which BPS sector — the non-degeneracy result

Two published knot-homology/BPS bridges live in the literature, and they identify
**different** BPS spaces:

| Bridge | BPS sector | $4_1$ count |
|--------|-----------|-------------|
| Gukov--Stošić [`gukov-stosic2012`] | **open** BPS states (conormal $L_K \subset T^*S^3$; colored HOMFLY homology) | $\det(4_1) = 5$ |
| GPPV [`gukov-pei-putrov-vafa2017`] + GGM Conj 3(d) | **closed** / state-integral ($\hat{Z}$; resurgent Stokes) | $3$ |

The closed-sector entry is the $4_1$ Stokes integer of GGM eq. (60) (§3.1, *the
$4_1$ knot when $u = 0$*). The integer $4$ that has been quoted beside it comes
from GGM eqs. (96)/(98), which are **$5_2$ data** (§3.2), not $4_1$ data.

The **open**-HOMFLY count is fixed by the knots--quivers correspondence
[`kucharski-reineke-stosic-sulkowski2017`]: the quiver of a knot has one node per
HOMFLY-PT homology generator, so the $4_1$ open-BPS count is $\det(4_1) = 5$.

That count is **read off a published quiver, not inferred from the determinant**.
Singh et al. [`singh-physrevd108106023`] give the figure-eight explicitly, as a
motivic sum over $d_1 + \cdots + d_5 = r$ with a symmetric $5 \times 5$ matrix
$C_{4_1}$: five nodes, directly. The correspondence's rule --- node count equals
determinant --- is itself confirmed at four knots rather than at one, so the
identification is not a coincidence of the figure-eight:

| knot | published quiver | $\det$ |
|---|---|---|
| $3_1$ | $3 \times 3$ (worked trefoil of [`kucharski-reineke-stosic-sulkowski2017`]) | $3$ |
| $4_1$ | $5 \times 5$ | $5$ |
| $6_1$ | $9 \times 9$ | $9$ |
| $8_1$ | $13 \times 13$ | $13$ |

All four counts equal $1 + 4pm$, the determinant of the double twist knot
$K(p, -m)$ implied by the Alexander polynomial of [`singh-physrevd108106023`].
Since $5 \neq 3$, the **open**-HOMFLY Gukov--Stošić bridge does *not* reproduce
the $4_1$ Stokes integer $3$ of GGM eq. (60) and does *not* license
$A_\omega = 3$. Only the **closed**-sector bridge stated above relates to that
integer; its $q \to 0$ anchor $S^+(0)_{01} = 3$ is machine-checked
unconditionally (`QOU.QBeta.StokesQZeroDTCount`).

We therefore adopt the **closed**-sector bridge, and A_ω=3 is made
conditional on it downstream
([The figure-eight Stokes integer $A_\omega(4_1) = 3$ is a BPS/DT count](#thm:aomega-fourone-dt-count)) — conditional for
every knot, $4_1$ included, since GGM's Conjecture 3(d) is not proved for $4_1$. It is *not* the open-HOMFLY bridge.

### Lean axiomatisation

The bridge is a Lean typeclass `QOU.QBeta.StokesDTBPSBridge` carrying the two
identifications as fields:

```lean
class StokesDTBPSBridge (Knot : Type*) where
  stokesConstant : Knot → ℤ
  dtInvariant    : Knot → ℤ
  bpsDim         : Knot → ℤ
  stokes_eq_dt : ∀ K, stokesConstant K = dtInvariant K   -- GGM Conj 3(d)
  dt_eq_bps    : ∀ K, dtInvariant K   = bpsDim K          -- GPPV
```

The fields are the conjecture's *inputs*; no field asserts a value of $A_\omega$.
Any instance is the conjecture holding; none is supplied (the general statement is
open for every knot, $4_1$ included). Downstream results take
`[StokesDTBPSBridge Knot]` as an explicit hypothesis and are then fully verified
by Lean modulo that class instance, following the same pattern as
[`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md).
